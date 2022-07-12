import pytest

from keyrt import KeyRT

KEYRT_ACCESS_TOKEN_VALID = "rocketbank_sexy"
KEYRT_ACCESS_TOKEN_INVALID = "sberbank_pesiy_anus"

USER_RESPONSE_JSON = """
{
  "request_id": "d9eede02-c9f8-4637-8c3d-8972d76f8c50",
  "data": {
    "id": 123456,
    "type": "master",
    "login": "rtkid_1112223334445",
    "phone_number": "+79998887766",
    "email": "name@mail.ru",
    "status": "active",
    "is_new": true,
    "sso_id": "f:c3dd0b8e-79e6-469c-9f2e-96d9b79bd4e5:2223334",
    "mos_sso_id": null,
    "sso_user_id": 2223334,
    "sso_linked": false,
    "ory_id": "bWFzdGVyOjc6NDc6NG9tb1NmR28zOURGZUFobE9LRWdMMTNrYUZZcz0=",
    "vc_id": 888666,
    "ustore_id": 111222,
    "mrf_id": 7,
    "rf_id": 47,
    "company": {
      "id": 811,
      "vc_id": 38827,
      "title": "ООО УК Аквамарин",
      "utc_offset": 180,
      "link_title": null,
      "ios_deep_link": null,
      "ios_app_store_link": null,
      "android_package_id": null,
      "huawei_appgallery_package_name": null,
      "web_link": null,
      "link_description": null
    },
    "creator_user_id": 12345,
    "created_by": "mrf",
    "phone_number_verified": true,
    "email_verified": false,
    "created_at": "2021-09-21T16:49:26Z",
    "archived_at": null,
    "updated_at": "2022-04-23T16:51:45Z",
    "buildings": [
      {
        "id": 4422,
        "mrf_id": 7,
        "rf_id": 47,
        "place": "г. Нижний Новгород",
        "street": "ул. Академика Сахарова, д. 115, к. 1",
        "numbering": null,
        "fias_id": null,
        "orpon_id": 70465790,
        "company_id": 811,
        "utc_offset": 180,
        "entrances": [
          {
            "id": "1",
            "name": "1",
            "floors": [
              {
                "id": "1",
                "name": "1",
                "flats": [
                  {
                    "id": 425783,
                    "company_id": 811,
                    "name": "212",
                    "area": 0,
                    "account": {
                      "number": 314020432230,
                      "modified_at": "2021-09-21T13:49:26Z",
                      "type": "rtk"
                    },
                    "sips": [],
                    "tfop_phones": [],
                    "user_settings": {
                      "redirect_to_mobile_application": true,
                      "devices_call_redirect_to_pstn": false,
                      "devices_call_redirect_to_sip": true
                    },
                    "type": "apartment",
                    "room_permissions": {
                      "devices_rfids_intercom_access_behavior": false,
                      "devices_call_redirect_to_sip_behavior": false,
                      "devices_call_redirect_to_pstn_behavior": false,
                      "devices_call_redirect_to_mobile_app_behavior": false,
                      "devices_rfids_barrier_access_behavior": false,
                      "barriers_full_code_generate_behavior": false,
                      "devices_rfids_access_control_panel_access_behavior": false,
                      "fr_intercom_access_behavior": false
                    },
                    "actions_permissions": [
                      "get_video_archive",
                      "get_devices_camera",
                      "get_events_intercom",
                      "get_devices_intercom",
                      "get_devices_rfids_intercom",
                      "post_devices_codes_intercom",
                      "get_devices_codes_intercom",
                      "get_video_archive_intercom",
                      "post_devices_open_intercom",
                      "get_devices_camera_intercom",
                      "post_devices_rfids_intercom",
                      "delete_devices_codes_intercom",
                      "delete_devices_rfids_intercom"
                    ],
                    "is_subscription_enable": false
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  },
  "error": null
}
"""

DEVICES_RESPONSE_JSON = """
{
  "data": {
    "devices": [
      {
        "id": "131313",
        "device_type": "intercom",
        "serial_number": "16N12554",
        "device_group": [
          "Подъезд"
        ],
        "entrance": 1,
        "utc_offset_minutes": 180,
        "camera_id": "4ec6fa8b-b9de-4efe-b74d-02fe662337e5",
        "description": "Подъезд №1",
        "is_favorite": false,
        "is_active": true,
        "name_by_company": "Подъезд №1",
        "name_by_user": "115/1",
        "accept_concierge_call": false,
        "capabilities": [
          {
            "name": "temporary_key",
            "setup": true
          },
          {
            "name": "constant_key",
            "setup": true
          },
          {
            "name": "sip_calls",
            "setup": true
          },
          {
            "name": "open_door",
            "setup": true
          },
          {
            "name": "dtmf_code",
            "setup": true
          },
          {
            "name": "sip_video",
            "setup": true
          },
          {
            "name": "ntp",
            "setup": true
          },
          {
            "name": "syslog",
            "setup": true
          },
          {
            "name": "emergency_door",
            "setup": true
          }
        ],
        "inter_codes": [
          {
            "id": 989866,
            "code": "0000005FF246BB",
            "start_date": "2021-09-09T14:15:55.583555Z",
            "end_date": null,
            "inter_code_type": "constant"
          },
          {
            "id": 989867,
            "code": "0000005FF246BC",
            "start_date": "2021-09-09T14:15:58.214372Z",
            "end_date": null,
            "inter_code_type": "constant"
          }
        ]
      }
    ]
  }
}
"""

CAMERAS_RESPONSE_JSON = """
{
  "data": {
    "items": [
      {
        "archive_length": null,
        "category": {
          "id": 2,
          "title": "Домофон",
          "type": "intercom"
        },
        "created_at": "2021-09-09T16:24:19.320+03:00",
        "id": "ad34ea5b-4c39-40c2-8fbf-66da45993fc3",
        "ip": "0.0.0.0",
        "location": {
          "lat": null,
          "lng": null
        },
        "mac": "00:00:00:00:00:00",
        "model": "",
        "screenshot_precise_url_template": "https://media-vdk4.camera.rt.ru/image/precise/{size}/ad34ea5b-4c39-40c2-8fbc-66da45993fc3/{timestamp}.jpg?token={cdn_token}",
        "screenshot_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6ImRlZsfdsdfsfcHJvZHVjdGlvbiJ9.eyJpc3MiOiJ2Y2Zyb250X3Byb2R1Y3Rpb24iLCJleHAiOjE2NTcyNDU2MDAsInN1YiI6ODUyNjA4LCJpcCI6IjEwLjc4LjMyLjEzOCIsImNoYW5uZWwiOiI3ZTQ1MTNjZS02NDQ0LTRjYTQtYWQ2My1iYzEzNDkyNmM0NTEifQ.ajTlVCgQymM-wZIR0HRqkdQk6fLjJY1msVruZtw9g",
        "screenshot_url_template": "https://media-vdk4.camera.rt.ru/image/{size}/ad34ea5b-4c39-40c2-8fbc-66da45993fc3/{timestamp}.jpg?token={cdn_token}",
        "serial_number": "",
        "status": {
          "id": 1,
          "title": "Доступна",
          "type": "online"
        },
        "streamer_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1abdycHJvZHVjdGlvbiJ9.eyJpc3MiOiJ2Y2Zyb250X3Byb2R1Y3Rpb24iLCJleHAiOjE2NTcyNDU2MDAsInN1YiI6ODUyNjA4LCJpcCI6IjEwLjc4LjMyLjEzOCIsImNoYW5uZWwiOiI3ZTQ1MTNjZS02NDQ0LTRjYTQtYWQ2My1iYzEzNDkyNmM0NTEifQ.ajTlVCgQymM-wZIR0HRqkdQk6fLjJY12_msVruZtw9g",
        "streamer_url": "https://live-vdk4.camera.rt.ru/blue7",
        "title": "Сахарова 115/1",
        "updated_at": "2021-10-27T11:22:38.501+03:00",
        "user_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1sgsgsgsgmRlZmF1bHRfcHJvZHVjdGlvbiJ9.eyJzdWIiOjg1MjYwOH0.tO1T1n3HoCIhNy7I87aFYLdqM_Z1dMal0tk4_Y3V0fw",
        "utc_offset": 180,
        "vendor": ""
      }
    ],
    "total": 1
  },
  "error": null,
  "request_id": "f3adc6d9-9fa8-42b1-a383-6b8a83029784"
}
"""

CODES_RESPONSE_JSON = """
{
  "request_id": "c5dd542b-d749-494b-9f54-6d460e8e4dab",
  "data": {
    "items": [
      {
        "id": 2437454,
        "code": "26618",
        "type": "emergency",
        "title": null,
        "flat": null,
        "company": null,
        "owner_type": "system",
        "owner": null,
        "creator_type": "system",
        "creator": null,
        "created_at": "2022-07-01T13:11:41Z",
        "begin_at": "2022-07-01T13:11:41Z",
        "expires_at": "2022-07-08T13:11:41Z",
        "statuses": [
          {
            "device": {
              "id": 12164,
              "company": {
                "id": 811
              },
              "type": "intercom",
              "title": "Подъезд №1",
              "full_code": null,
              "call_number": null
            },
            "status_changed_at": "2022-07-01T13:11:46Z",
            "status": "loaded"
          }
        ]
      },
      {
        "id": 2452536,
        "code": "93626",
        "type": "temporary",
        "title": null,
        "flat": {
          "id": 425783,
          "number": "212"
        },
        "company": {
          "id": 811
        },
        "owner_type": "master",
        "owner": {
          "id": 123456,
          "email": "name@mail.ru",
          "login": "rtkid_1112223334445",
          "phone_number": "+79998887766",
          "status": "active"
        },
        "creator_type": "master",
        "creator": {
          "id": 123456,
          "email": "name@mail.ru",
          "login": "rtkid_1112223334445",
          "phone_number": "+79998887766",
          "status": "active"
        },
        "created_at": "2022-07-06T06:48:58Z",
        "begin_at": "2022-07-06T06:48:58Z",
        "expires_at": "2022-07-07T06:48:58Z",
        "statuses": [
          {
            "device": {
              "id": 12164,
              "company": {
                "id": 811
              },
              "type": "intercom",
              "title": "115/1",
              "full_code": null,
              "call_number": null
            },
            "status_changed_at": "2022-07-06T06:48:59Z",
            "status": "loaded"
          }
        ]
      }
    ],
    "total": 2
  },
  "error": null
}
"""


@pytest.fixture
def keyrt_client():
    return KeyRT(access_token=KEYRT_ACCESS_TOKEN_VALID)
