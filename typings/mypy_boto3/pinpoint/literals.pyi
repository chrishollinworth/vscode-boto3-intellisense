"""
Type annotations for pinpoint service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/literals.html)

Usage::

    ```python
    from mypy_boto3_pinpoint.literals import ActionType

    data: ActionType = "DEEP_LINK"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionType",
    "AlignmentType",
    "AttributeTypeType",
    "ButtonActionType",
    "CampaignStatusType",
    "ChannelTypeType",
    "DayOfWeekType",
    "DeliveryStatusType",
    "DimensionTypeType",
    "DurationType",
    "FilterTypeType",
    "FormatType",
    "FrequencyType",
    "IncludeType",
    "JobStatusType",
    "JourneyRunStatusType",
    "LayoutType",
    "MessageTypeType",
    "ModeType",
    "OperatorType",
    "RecencyTypeType",
    "SegmentTypeType",
    "SourceTypeType",
    "StateType",
    "TemplateTypeType",
    "TypeType",
    "__EndpointTypesElementType",
    "__TimezoneEstimationMethodsElementType",
)

ActionType = Literal["DEEP_LINK", "OPEN_APP", "URL"]
AlignmentType = Literal["CENTER", "LEFT", "RIGHT"]
AttributeTypeType = Literal[
    "AFTER", "BEFORE", "BETWEEN", "CONTAINS", "EXCLUSIVE", "INCLUSIVE", "ON"
]
ButtonActionType = Literal["CLOSE", "DEEP_LINK", "LINK"]
CampaignStatusType = Literal[
    "COMPLETED", "DELETED", "EXECUTING", "INVALID", "PAUSED", "PENDING_NEXT_RUN", "SCHEDULED"
]
ChannelTypeType = Literal[
    "ADM",
    "APNS",
    "APNS_SANDBOX",
    "APNS_VOIP",
    "APNS_VOIP_SANDBOX",
    "BAIDU",
    "CUSTOM",
    "EMAIL",
    "GCM",
    "IN_APP",
    "PUSH",
    "SMS",
    "VOICE",
]
DayOfWeekType = Literal[
    "FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"
]
DeliveryStatusType = Literal[
    "DUPLICATE",
    "OPT_OUT",
    "PERMANENT_FAILURE",
    "SUCCESSFUL",
    "TEMPORARY_FAILURE",
    "THROTTLED",
    "UNKNOWN_FAILURE",
]
DimensionTypeType = Literal["EXCLUSIVE", "INCLUSIVE"]
DurationType = Literal["DAY_14", "DAY_30", "DAY_7", "HR_24"]
FilterTypeType = Literal["ENDPOINT", "SYSTEM"]
FormatType = Literal["CSV", "JSON"]
FrequencyType = Literal["DAILY", "EVENT", "HOURLY", "IN_APP_EVENT", "MONTHLY", "ONCE", "WEEKLY"]
IncludeType = Literal["ALL", "ANY", "NONE"]
JobStatusType = Literal[
    "COMPLETED",
    "COMPLETING",
    "CREATED",
    "FAILED",
    "FAILING",
    "INITIALIZING",
    "PENDING_JOB",
    "PREPARING_FOR_INITIALIZATION",
    "PROCESSING",
]
JourneyRunStatusType = Literal["CANCELLED", "COMPLETED", "RUNNING", "SCHEDULED"]
LayoutType = Literal[
    "BOTTOM_BANNER", "CAROUSEL", "MIDDLE_BANNER", "MOBILE_FEED", "OVERLAYS", "TOP_BANNER"
]
MessageTypeType = Literal["PROMOTIONAL", "TRANSACTIONAL"]
ModeType = Literal["DELIVERY", "FILTER"]
OperatorType = Literal["ALL", "ANY"]
RecencyTypeType = Literal["ACTIVE", "INACTIVE"]
SegmentTypeType = Literal["DIMENSIONAL", "IMPORT"]
SourceTypeType = Literal["ALL", "ANY", "NONE"]
StateType = Literal["ACTIVE", "CANCELLED", "CLOSED", "COMPLETED", "DRAFT", "PAUSED"]
TemplateTypeType = Literal["EMAIL", "INAPP", "PUSH", "SMS", "VOICE"]
TypeType = Literal["ALL", "ANY", "NONE"]
__EndpointTypesElementType = Literal[
    "ADM",
    "APNS",
    "APNS_SANDBOX",
    "APNS_VOIP",
    "APNS_VOIP_SANDBOX",
    "BAIDU",
    "CUSTOM",
    "EMAIL",
    "GCM",
    "IN_APP",
    "PUSH",
    "SMS",
    "VOICE",
]
__TimezoneEstimationMethodsElementType = Literal["PHONE_NUMBER", "POSTAL_CODE"]
