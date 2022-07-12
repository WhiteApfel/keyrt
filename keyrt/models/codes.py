from __future__ import annotations

from typing import Any, Iterator, List, Optional

from pydantic import BaseModel, Field


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
    codes: List[Code] = Field(..., alias='items')
    total: int

    @property
    def temporary(self) -> Codes:
        codes = [code for code in self.codes if code.type == "temporary"]
        return Codes(items=codes, total=len(codes))

    @property
    def emergency(self) -> Codes:
        codes = [code for code in self.codes if code.type == "emergency"]
        return Codes(items=codes, total=len(codes))

    def __getitem__(self, item):
        # temporary by code id
        for code in self.temporary:
            if code.id == int(item):
                return code

        # temporary by device_id
        for code in self.temporary:
            if code.statuses[0].device.id == int(item):
                return code

        # temporary by name
        for code in self.temporary:
            if code.statuses[0].device.title == str(item):
                return code

        return self.codes[item]

    def __iter__(self) -> Iterator[Code]:
        return iter(self.codes)

    def __len__(self):
        return len(self.codes)


class CodesResponse(BaseModel):
    request_id: str
    data: Codes
    error: Any
