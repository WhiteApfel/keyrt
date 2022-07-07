from typing import Any, List, Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    title: str
    type: str


class Location(BaseModel):
    lat: Any
    lng: Any


class Status(BaseModel):
    id: int
    title: str
    type: str


class Camera(BaseModel):
    archive_length: Any
    category: Category
    created_at: str
    id: str
    ip: str
    location: Location
    mac: str
    model: str
    screenshot_precise_url_template: str
    screenshot_token: str
    screenshot_url_template: str
    serial_number: str
    status: Status
    streamer_token: str
    streamer_url: str
    title: str
    updated_at: str
    user_token: str
    utc_offset: int
    vendor: str


class Cameras(BaseModel):
    items: List[Camera]
    total: int


class CamerasResponse(BaseModel):
    data: Cameras
    error: Any
    request_id: str
