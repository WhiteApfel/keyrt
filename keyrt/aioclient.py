import time
from base64 import b64encode, b64decode
from typing import Literal

from httpx import AsyncClient

from keyrt.models.cameras import Cameras, CamerasResponse
from keyrt.models.codes import Codes, CodesResponse
from keyrt.models.devices import DevicesResponse, Devices
from keyrt.models.tokens import OauthTokensResponse
from keyrt.models.user import User, UserResponse


class KeyRT:
    def __init__(self, access_token: str = None):
        self._access_token: str = access_token
        self._session: AsyncClient | None = None

    @property
    def session(self) -> AsyncClient:
        if self._session is None:
            self._session = AsyncClient(base_url="https://household.key.rt.ru/api")
        self._session.headers["Authorization"] = f"Bearer {self._access_token}"
        return self._session

    async def request(
        self,
        method: Literal["GET", "POST", "PUT", "DELETE"],
        url: str,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        headers: dict | None = None,
        access_token: str | None = None,
    ):
        if access_token is not None:
            headers = (headers or {}) | {"Authorization": f"Bearer {access_token}"}
        return await self.session.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json,
            data=data,
        )

    async def current_user(self, access_token: str = None) -> User:
        response = await self.request(
            method="GET",
            url="/v3/app/users/current",
            access_token=access_token,
        )

        return UserResponse(**response.json()).data

    async def get_devices(self, access_token: str = None) -> Devices:
        response = await self.request(
            method="GET",
            url="/v2/app/devices/intercom",
            access_token=access_token,
        )

        return DevicesResponse(**response.json()).data

    async def get_cameras(self, access_token: str = None) -> Cameras:
        response = await self.request(
            method="GET",
            url="https://vc.key.rt.ru/api/v1/cameras",
            params={
                "offset": 0,
                "limit": 1000,
            },
            access_token=access_token,
        )

        return CamerasResponse(**response.json()).data

    async def open_device(self, device_id: str, access_token: str = None) -> bool:
        response = await self.request(
            method="POST",
            url=f"/v2/app/devices/{device_id}/open",
            access_token=access_token,
        )

        return response.status_code == 200

    async def get_codes(self, access_token: str = None) -> Codes:
        response = await self.request(
            method="GET",
            url="/v3/app/devices/codes",
            access_token=access_token,
        )

        return CodesResponse(**response.json()).data

    async def generate_code(
        self, devices_ids: list[int] | int, flat_id: int, access_token: str = None
    ) -> bool:
        response = await self.request(
            method="POST",
            url="/v3/app/codes/generate",
            json={
                "devices_ids": [int(d) for d in devices_ids]
                if isinstance(devices_ids, list)
                else [int(devices_ids)],
                "flat_id": flat_id,
            },
            access_token=access_token,
        )

        return response.status_code == 202

    async def delete_code(self, flat_id: str, access_token: str = None) -> bool:
        response = await self.request(
            method="DELETE",
            url=f"/v2/app/flats/{flat_id}/intercode",
            access_token=access_token,
        )

        return response.status_code == 204

    def generate_oauth_link(self, callback_url: str = "https://tochka-api.pfel.cc"):
        url = (
            "https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth"
            "?redirect_uri=https://sso.key.rt.ru/api/v1/oauth2/b2c/callback"
            "&client_id=lk_dmh"
            "&response_type=code"
            f"&state={b64encode(f'{callback_url}?t={int(time.time())}'.encode()).decode()}"
        )
        return url

    async def oauth_to_token(
        self, code: str, state: str, auto_set_access_token: bool = True
    ) -> OauthTokensResponse:
        response = await self.request(
            method="POST",
            url="/v3/app/sso/oauth2/token",
            data={
                "code": code,
                "state": state,
                "timestamp": b64decode(state).decode().split("=")[-1],
                "grant_type": "authorization_code",
            },
        )

        if response.status_code == 200:
            response_data = OauthTokensResponse(**response.json())
            if auto_set_access_token:
                self._access_token = response_data.data.key.access_token

            return response_data

        return response.json()
