from typing import Any, List, Optional, Iterator

from pydantic import BaseModel, Field


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
    cameras: List[Camera] = Field(..., alias="items")
    total: int

    def __getitem__(self, item):
        # by camera id
        for camera in self.cameras:
            if camera.id == str(item):
                return camera

        # by title
        for camera in self.cameras:
            if camera.title == str(item):
                return camera

        return self.cameras[item]

    def __iter__(self) -> Iterator[Camera]:
        return iter(self.cameras)

    def __len__(self):
        return len(self.cameras)


class CamerasResponse(BaseModel):
    data: Cameras
    error: Any
    request_id: str
