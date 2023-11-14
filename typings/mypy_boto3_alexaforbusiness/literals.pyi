"""
Type annotations for alexaforbusiness service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/literals.html)

Usage::

    ```python
    from mypy_boto3_alexaforbusiness.literals import BusinessReportFailureCodeType

    data: BusinessReportFailureCodeType = "ACCESS_DENIED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BusinessReportFailureCodeType",
    "BusinessReportFormatType",
    "BusinessReportIntervalType",
    "BusinessReportStatusType",
    "CommsProtocolType",
    "ConferenceProviderTypeType",
    "ConnectionStatusType",
    "DeviceEventTypeType",
    "DeviceStatusDetailCodeType",
    "DeviceStatusType",
    "DeviceUsageTypeType",
    "DistanceUnitType",
    "EnablementTypeFilterType",
    "EnablementTypeType",
    "EndOfMeetingReminderTypeType",
    "EnrollmentStatusType",
    "FeatureType",
    "ListBusinessReportSchedulesPaginatorName",
    "ListConferenceProvidersPaginatorName",
    "ListDeviceEventsPaginatorName",
    "ListSkillsPaginatorName",
    "ListSkillsStoreCategoriesPaginatorName",
    "ListSkillsStoreSkillsByCategoryPaginatorName",
    "ListSmartHomeAppliancesPaginatorName",
    "ListTagsPaginatorName",
    "LocaleType",
    "NetworkEapMethodType",
    "NetworkSecurityTypeType",
    "PhoneNumberTypeType",
    "RequirePinType",
    "SearchDevicesPaginatorName",
    "SearchProfilesPaginatorName",
    "SearchRoomsPaginatorName",
    "SearchSkillGroupsPaginatorName",
    "SearchUsersPaginatorName",
    "SipTypeType",
    "SkillTypeFilterType",
    "SkillTypeType",
    "SortValueType",
    "TemperatureUnitType",
    "WakeWordType",
)

BusinessReportFailureCodeType = Literal["ACCESS_DENIED", "INTERNAL_FAILURE", "NO_SUCH_BUCKET"]
BusinessReportFormatType = Literal["CSV", "CSV_ZIP"]
BusinessReportIntervalType = Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"]
BusinessReportStatusType = Literal["FAILED", "RUNNING", "SUCCEEDED"]
CommsProtocolType = Literal["H323", "SIP", "SIPS"]
ConferenceProviderTypeType = Literal[
    "BLUEJEANS",
    "CHIME",
    "CUSTOM",
    "FUZE",
    "GOOGLE_HANGOUTS",
    "POLYCOM",
    "RINGCENTRAL",
    "SKYPE_FOR_BUSINESS",
    "WEBEX",
    "ZOOM",
]
ConnectionStatusType = Literal["OFFLINE", "ONLINE"]
DeviceEventTypeType = Literal["CONNECTION_STATUS", "DEVICE_STATUS"]
DeviceStatusDetailCodeType = Literal[
    "ASSOCIATION_REJECTION",
    "AUTHENTICATION_FAILURE",
    "CERTIFICATE_AUTHORITY_ACCESS_DENIED",
    "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
    "CREDENTIALS_ACCESS_FAILURE",
    "DEVICE_SOFTWARE_UPDATE_NEEDED",
    "DEVICE_WAS_OFFLINE",
    "DHCP_FAILURE",
    "DNS_FAILURE",
    "INTERNET_UNAVAILABLE",
    "INVALID_CERTIFICATE_AUTHORITY",
    "INVALID_PASSWORD_STATE",
    "NETWORK_PROFILE_NOT_FOUND",
    "PASSWORD_MANAGER_ACCESS_DENIED",
    "PASSWORD_NOT_FOUND",
    "TLS_VERSION_MISMATCH",
    "UNKNOWN_FAILURE",
]
DeviceStatusType = Literal["DEREGISTERED", "FAILED", "PENDING", "READY", "WAS_OFFLINE"]
DeviceUsageTypeType = Literal["VOICE"]
DistanceUnitType = Literal["IMPERIAL", "METRIC"]
EnablementTypeFilterType = Literal["ENABLED", "PENDING"]
EnablementTypeType = Literal["ENABLED", "PENDING"]
EndOfMeetingReminderTypeType = Literal[
    "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
]
EnrollmentStatusType = Literal[
    "DEREGISTERING", "DISASSOCIATING", "INITIALIZED", "PENDING", "REGISTERED"
]
FeatureType = Literal[
    "ALL", "BLUETOOTH", "LISTS", "NETWORK_PROFILE", "NOTIFICATIONS", "SETTINGS", "SKILLS", "VOLUME"
]
ListBusinessReportSchedulesPaginatorName = Literal["list_business_report_schedules"]
ListConferenceProvidersPaginatorName = Literal["list_conference_providers"]
ListDeviceEventsPaginatorName = Literal["list_device_events"]
ListSkillsPaginatorName = Literal["list_skills"]
ListSkillsStoreCategoriesPaginatorName = Literal["list_skills_store_categories"]
ListSkillsStoreSkillsByCategoryPaginatorName = Literal["list_skills_store_skills_by_category"]
ListSmartHomeAppliancesPaginatorName = Literal["list_smart_home_appliances"]
ListTagsPaginatorName = Literal["list_tags"]
LocaleType = Literal["en-US"]
NetworkEapMethodType = Literal["EAP_TLS"]
NetworkSecurityTypeType = Literal["OPEN", "WEP", "WPA2_ENTERPRISE", "WPA2_PSK", "WPA_PSK"]
PhoneNumberTypeType = Literal["HOME", "MOBILE", "WORK"]
RequirePinType = Literal["NO", "OPTIONAL", "YES"]
SearchDevicesPaginatorName = Literal["search_devices"]
SearchProfilesPaginatorName = Literal["search_profiles"]
SearchRoomsPaginatorName = Literal["search_rooms"]
SearchSkillGroupsPaginatorName = Literal["search_skill_groups"]
SearchUsersPaginatorName = Literal["search_users"]
SipTypeType = Literal["WORK"]
SkillTypeFilterType = Literal["ALL", "PRIVATE", "PUBLIC"]
SkillTypeType = Literal["PRIVATE", "PUBLIC"]
SortValueType = Literal["ASC", "DESC"]
TemperatureUnitType = Literal["CELSIUS", "FAHRENHEIT"]
WakeWordType = Literal["ALEXA", "AMAZON", "COMPUTER", "ECHO"]
