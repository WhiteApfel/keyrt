import pytest
import respx
from httpx import Response

from keyrt import KeyRT
from tests.conftest import USER_RESPONSE_JSON


@pytest.mark.asyncio
@respx.mock
async def test_user(keyrt_client: KeyRT):
    respx.get('https://household.key.rt.ru/api/v3/app/users/current').mock(
        Response(status_code=200, content=USER_RESPONSE_JSON)
    )

    user_response = await keyrt_client.current_user()

    assert user_response.data.id == 123456
    assert user_response.data.login == 'rtkid_1112223334445'
