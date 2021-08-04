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
    "AttributeTypeType",
    "CampaignStatusType",
    "ChannelTypeType",
    "DeliveryStatusType",
    "DimensionTypeType",
    "DurationType",
    "FilterTypeType",
    "FormatType",
    "FrequencyType",
    "IncludeType",
    "JobStatusType",
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
)

ActionType = Literal["DEEP_LINK", "OPEN_APP", "URL"]
AttributeTypeType = Literal[
    "AFTER", "BEFORE", "BETWEEN", "CONTAINS", "EXCLUSIVE", "INCLUSIVE", "ON"
]
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
    "PUSH",
    "SMS",
    "VOICE",
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
FrequencyType = Literal["DAILY", "EVENT", "HOURLY", "MONTHLY", "ONCE", "WEEKLY"]
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
MessageTypeType = Literal["PROMOTIONAL", "TRANSACTIONAL"]
ModeType = Literal["DELIVERY", "FILTER"]
OperatorType = Literal["ALL", "ANY"]
RecencyTypeType = Literal["ACTIVE", "INACTIVE"]
SegmentTypeType = Literal["DIMENSIONAL", "IMPORT"]
SourceTypeType = Literal["ALL", "ANY", "NONE"]
StateType = Literal["ACTIVE", "CANCELLED", "CLOSED", "COMPLETED", "DRAFT", "PAUSED"]
TemplateTypeType = Literal["EMAIL", "PUSH", "SMS", "VOICE"]
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
    "PUSH",
    "SMS",
    "VOICE",
]
