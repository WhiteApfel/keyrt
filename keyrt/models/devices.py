from typing import Any, List, Optional

from pydantic import BaseModel


class Capability(BaseModel):
    name: str
    setup: bool


class InterCode(BaseModel):
    id: int
    code: str
    start_date: str
    end_date: Any
    inter_code_type: str


class Device(BaseModel):
    id: str
    device_type: str
    serial_number: str
    device_group: List[str]
    entrance: int
    utc_offset_minutes: int
    camera_id: str
    description: str
    is_favorite: bool
    is_active: bool
    name_by_company: str
    name_by_user: str
    accept_concierge_call: bool
    capabilities: List[Capability]
    inter_codes: List[InterCode]


class Devices(BaseModel):
    devices: List[Device]


class DevicesResponse(BaseModel):
    data: Devices
