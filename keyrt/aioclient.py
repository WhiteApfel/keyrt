from httpx import AsyncClient

from keyrt.models.cameras import CamerasResponse
from keyrt.models.codes import CodesResponse
from keyrt.models.devices import DevicesResponse
from keyrt.models.user import UserResponse


class KeyRT:
    def __init__(self, access_token: str):
        self._access_token: str = access_token
        self._session: AsyncClient | None = None

    @property
    def session(self) -> AsyncClient:
        if self._session is None:
            self._session = AsyncClient(base_url="https://household.key.rt.ru/api")
            self._session.headers["Authorization"] = f"Bearer {self._access_token}"
        return self._session

    async def current_user(self) -> UserResponse:
        response = await self.session.get(
            url="/v3/app/users/current",
        )

        return UserResponse(**response.json())

    async def get_devices(self) -> DevicesResponse:
        response = await self.session.get(url="/v2/app/devices/intercom")

        return DevicesResponse(**response.json())

    async def get_cameras(self) -> CamerasResponse:
        response = await self.session.get(
            url="https://vc.key.rt.ru/api/v1/cameras",
            params={
                "offset": 0,
                "limit": 1000,
            },
        )

        return CamerasResponse(**response.json())

    async def open_device(self, device_id: str) -> int:
        response = await self.session.post(
            url=f"/v2/app/devices/{device_id}/open",
        )

        return response.status_code == 200

    async def get_codes(self) -> CodesResponse:
        response = await self.session.get(
            url="/v3/app/devices/codes",
        )

        return CodesResponse(**response.json())

    async def generate_code(self, device_ids: list[int] | int, flat_id: int) -> bool:
        response = await self.session.post(
            url="/v3/app/codes/generate",
            json={
                "device_ids": device_ids
                if isinstance(device_ids, list)
                else [device_ids],
                "flat_id": flat_id,
            },
        )

        return response.status_code == 202

    async def delete_code(self, flat_id: str) -> bool:
        response = await self.session.delete(url=f"/v2/app/flats/{flat_id}/intercode")

        return response.status_code == 204
