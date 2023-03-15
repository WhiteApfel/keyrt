from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel


class Capability(BaseModel):
    name: str
    setup: bool


class InterCode(BaseModel):
    id: int
    code: str
    start_date: datetime
    end_date: datetime | None
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
    name_by_user: str | None
    accept_concierge_call: bool
    capabilities: List[Capability]
    inter_codes: List[InterCode]


class Devices(BaseModel):
    devices: List[Device]

    def __getitem__(self, item):
        # by device id
        for device in self.devices:
            if device.id == str(item):
                return device

        # by serial_number
        for device in self.devices:
            if device.serial_number == str(item):
                return device

        # by camera_id
        for device in self.devices:
            if device.camera_id == str(item):
                return device

        # by name_by_user
        for device in self.devices:
            if device.name_by_user == str(item):
                return device

        return self.devices[item]

    def __iter__(self):
        return iter(self.devices)

    def __len__(self):
        return len(self.devices)


class DevicesResponse(BaseModel):
    data: Devices
