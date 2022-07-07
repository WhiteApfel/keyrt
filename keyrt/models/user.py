from typing import Any, List, Optional

from pydantic import BaseModel


class Company(BaseModel):
    id: int
    vc_id: int
    title: str
    utc_offset: int
    link_title: Any
    ios_deep_link: Any
    ios_app_store_link: Any
    android_package_id: Any
    huawei_appgallery_package_name: Any
    web_link: Any
    link_description: Any


class Account(BaseModel):
    number: int
    modified_at: str
    type: str


class UserSettings(BaseModel):
    redirect_to_mobile_application: bool
    devices_call_redirect_to_pstn: bool
    devices_call_redirect_to_sip: bool


class RoomPermissions(BaseModel):
    devices_rfids_intercom_access_behavior: bool
    devices_call_redirect_to_sip_behavior: bool
    devices_call_redirect_to_pstn_behavior: bool
    devices_call_redirect_to_mobile_app_behavior: bool
    devices_rfids_barrier_access_behavior: bool
    barriers_full_code_generate_behavior: bool
    devices_rfids_access_control_panel_access_behavior: bool
    fr_intercom_access_behavior: bool


class Flat(BaseModel):
    id: int
    company_id: int
    name: str
    area: int
    account: Account
    sips: List
    tfop_phones: List
    user_settings: UserSettings
    type: str
    room_permissions: RoomPermissions
    actions_permissions: List[str]
    is_subscription_enable: bool


class Floor(BaseModel):
    id: str
    name: str
    flats: List[Flat]


class Entrance(BaseModel):
    id: str
    name: str
    floors: List[Floor]


class Building(BaseModel):
    id: int
    mrf_id: int
    rf_id: int
    place: str
    street: str
    numbering: Any
    fias_id: Any
    orpon_id: int
    company_id: int
    utc_offset: int
    entrances: List[Entrance]


class User(BaseModel):
    id: int
    type: str
    login: str
    phone_number: str
    email: str
    status: str
    is_new: bool
    sso_id: str
    mos_sso_id: Any
    sso_user_id: int
    sso_linked: bool
    ory_id: str
    vc_id: int
    ustore_id: int
    mrf_id: int
    rf_id: int
    company: Company
    creator_user_id: int
    created_by: str
    phone_number_verified: bool
    email_verified: bool
    created_at: str
    archived_at: Any
    updated_at: str
    buildings: List[Building]


class UserResponse(BaseModel):
    request_id: str
    data: User
    error: Any
