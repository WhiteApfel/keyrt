from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class FlatItem(BaseModel):
    id: int
    number: str


class UserInfo(BaseModel):
    id: int
    email: str
    login: str
    phone_number: str
    status: str


class Company(BaseModel):
    id: int


class Device(BaseModel):
    id: int
    company: Company
    type: str
    title: str
    full_code: Any
    call_number: Any


class Status(BaseModel):
    device: Device
    status_changed_at: str
    status: str


class Code(BaseModel):
    id: int
    code: str
    type: str
    title: Any
    flat: Optional[FlatItem]
    company: Optional[Company]
    owner_type: str
    owner: Optional[UserInfo]
    creator_type: str
    creator: Optional[UserInfo]
    created_at: str
    begin_at: str
    expires_at: str
    statuses: List[Status]


class Codes(BaseModel):
    items: List[Code]
    total: int


class CodesResponse(BaseModel):
    request_id: str
    data: Codes
    error: Any
