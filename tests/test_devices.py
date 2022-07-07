import pytest
import respx
from httpx import Response

from keyrt import KeyRT
from tests.conftest import DEVICES_RESPONSE_JSON


@pytest.mark.asyncio
@respx.mock
async def test_devices(keyrt_client: KeyRT):
    respx.get('https://household.key.rt.ru/api/v2/app/devices/intercom').mock(
        Response(status_code=200, content=DEVICES_RESPONSE_JSON)
    )

    devices_response = await keyrt_client.get_devices()

    assert len(devices_response.data.devices) == 1


@pytest.mark.asyncio
@respx.mock
async def test_open_device(keyrt_client: KeyRT):
    respx.get('https://household.key.rt.ru/api/v2/app/devices/intercom').mock(
        Response(status_code=200, content=DEVICES_RESPONSE_JSON)
    )
    respx.post('https://household.key.rt.ru/api/v2/app/devices/131313/open').mock(
        Response(status_code=200)
    )

    devices_response = await keyrt_client.get_devices()

    assert await keyrt_client.open_device(devices_response.data.devices[0].id)
