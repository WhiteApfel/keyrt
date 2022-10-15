from typing import Any

from pydantic import BaseModel


class OauthKeyData(BaseModel):
    id_token: str
    token_type: str
    access_token: str
    refresh_token: str
    expires_in: int
    scope: str | list[str]


class OauthTokenData(BaseModel):
    key: OauthKeyData
    vc: Any


class OauthTokensResponse(BaseModel):
    request_id: str
    data: OauthTokenData
    error: Any
