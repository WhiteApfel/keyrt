import json

import pytest
import respx
from httpx import Response, Request

from keyrt import KeyRT
from tests.conftest import CODES_RESPONSE_JSON, USER_RESPONSE_JSON, DEVICES_RESPONSE_JSON


@pytest.mark.asyncio
@respx.mock
async def test_codes(keyrt_client: KeyRT):
    respx.get('https://household.key.rt.ru/api/v3/app/devices/codes').mock(
        Response(status_code=200, content=CODES_RESPONSE_JSON)
    )

    codes_response = await keyrt_client.get_codes()

    assert codes_response.data.total == 2
    assert len(codes_response.data.items) == 2


@pytest.mark.asyncio
@respx.mock
async def test_generate_codes(keyrt_client: KeyRT):
    respx.get('https://household.key.rt.ru/api/v3/app/users/current').mock(
        Response(status_code=200, content=USER_RESPONSE_JSON)
    )
    respx.get('https://household.key.rt.ru/api/v2/app/devices/intercom').mock(
        Response(status_code=200, content=DEVICES_RESPONSE_JSON)
    )
    def check_codes_generate_request(request: Request):
        status_code = 400
        if (
            (data := json.loads(request.content.decode()))
            and data['device_ids'] == ['131313']
            and data['flat_id'] == 425783
        ):
            status_code = 202
        return Response(status_code)
    respx.post('https://household.key.rt.ru/api/v3/app/codes/generate').mock(
        side_effect=check_codes_generate_request,
    )

    user_response = await keyrt_client.current_user()
    devices_response = await keyrt_client.get_devices()

    assert await keyrt_client.generate_code(
        device_ids=devices_response.data.devices[0].id,
        flat_id=user_response.data.buildings[0].entrances[0].floors[0].flats[0].id,
    )


@pytest.mark.asyncio
@respx.mock
async def test_delete_codes(keyrt_client: KeyRT):
    respx.get('https://household.key.rt.ru/api/v3/app/users/current').mock(
        Response(status_code=200, content=USER_RESPONSE_JSON)
    )
    respx.delete('https://household.key.rt.ru/api/v2/app/flats/425783/intercode').mock(
        Response(status_code=204)
    )

    user_response = await keyrt_client.current_user()

    assert await keyrt_client.delete_code(
        flat_id=user_response.data.buildings[0].entrances[0].floors[0].flats[0].id,
    )
