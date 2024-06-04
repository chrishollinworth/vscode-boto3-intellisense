"""
Type annotations for ssm-contacts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm_contacts.type_defs import AcceptPageRequestRequestTypeDef

    data: AcceptPageRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AcceptCodeValidationType,
    AcceptTypeType,
    ActivationStatusType,
    ChannelTypeType,
    ContactTypeType,
    DayOfWeekType,
    ReceiptTypeType,
    ShiftTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AcceptPageRequestRequestTypeDef",
    "ActivateContactChannelRequestRequestTypeDef",
    "ChannelTargetInfoTypeDef",
    "ContactChannelAddressTypeDef",
    "ContactChannelTypeDef",
    "ContactTargetInfoTypeDef",
    "ContactTypeDef",
    "CoverageTimeTypeDef",
    "CreateContactChannelRequestRequestTypeDef",
    "CreateContactChannelResultTypeDef",
    "CreateContactRequestRequestTypeDef",
    "CreateContactResultTypeDef",
    "CreateRotationOverrideRequestRequestTypeDef",
    "CreateRotationOverrideResultTypeDef",
    "CreateRotationRequestRequestTypeDef",
    "CreateRotationResultTypeDef",
    "DeactivateContactChannelRequestRequestTypeDef",
    "DeleteContactChannelRequestRequestTypeDef",
    "DeleteContactRequestRequestTypeDef",
    "DeleteRotationOverrideRequestRequestTypeDef",
    "DeleteRotationRequestRequestTypeDef",
    "DescribeEngagementRequestRequestTypeDef",
    "DescribeEngagementResultTypeDef",
    "DescribePageRequestRequestTypeDef",
    "DescribePageResultTypeDef",
    "EngagementTypeDef",
    "GetContactChannelRequestRequestTypeDef",
    "GetContactChannelResultTypeDef",
    "GetContactPolicyRequestRequestTypeDef",
    "GetContactPolicyResultTypeDef",
    "GetContactRequestRequestTypeDef",
    "GetContactResultTypeDef",
    "GetRotationOverrideRequestRequestTypeDef",
    "GetRotationOverrideResultTypeDef",
    "GetRotationRequestRequestTypeDef",
    "GetRotationResultTypeDef",
    "HandOffTimeTypeDef",
    "ListContactChannelsRequestRequestTypeDef",
    "ListContactChannelsResultTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ListContactsResultTypeDef",
    "ListEngagementsRequestRequestTypeDef",
    "ListEngagementsResultTypeDef",
    "ListPageReceiptsRequestRequestTypeDef",
    "ListPageReceiptsResultTypeDef",
    "ListPageResolutionsRequestRequestTypeDef",
    "ListPageResolutionsResultTypeDef",
    "ListPagesByContactRequestRequestTypeDef",
    "ListPagesByContactResultTypeDef",
    "ListPagesByEngagementRequestRequestTypeDef",
    "ListPagesByEngagementResultTypeDef",
    "ListPreviewRotationShiftsRequestRequestTypeDef",
    "ListPreviewRotationShiftsResultTypeDef",
    "ListRotationOverridesRequestRequestTypeDef",
    "ListRotationOverridesResultTypeDef",
    "ListRotationShiftsRequestRequestTypeDef",
    "ListRotationShiftsResultTypeDef",
    "ListRotationsRequestRequestTypeDef",
    "ListRotationsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "MonthlySettingTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PlanTypeDef",
    "PreviewOverrideTypeDef",
    "PutContactPolicyRequestRequestTypeDef",
    "ReceiptTypeDef",
    "RecurrenceSettingsTypeDef",
    "ResolutionContactTypeDef",
    "ResponseMetadataTypeDef",
    "RotationOverrideTypeDef",
    "RotationShiftTypeDef",
    "RotationTypeDef",
    "SendActivationCodeRequestRequestTypeDef",
    "ShiftDetailsTypeDef",
    "StageTypeDef",
    "StartEngagementRequestRequestTypeDef",
    "StartEngagementResultTypeDef",
    "StopEngagementRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContactChannelRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
    "UpdateRotationRequestRequestTypeDef",
    "WeeklySettingTypeDef",
)

_RequiredAcceptPageRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptPageRequestRequestTypeDef",
    {
        "PageId": str,
        "AcceptType": AcceptTypeType,
        "AcceptCode": str,
    },
)
_OptionalAcceptPageRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptPageRequestRequestTypeDef",
    {
        "ContactChannelId": str,
        "Note": str,
        "AcceptCodeValidation": AcceptCodeValidationType,
    },
    total=False,
)

class AcceptPageRequestRequestTypeDef(
    _RequiredAcceptPageRequestRequestTypeDef, _OptionalAcceptPageRequestRequestTypeDef
):
    pass

ActivateContactChannelRequestRequestTypeDef = TypedDict(
    "ActivateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
        "ActivationCode": str,
    },
)

_RequiredChannelTargetInfoTypeDef = TypedDict(
    "_RequiredChannelTargetInfoTypeDef",
    {
        "ContactChannelId": str,
    },
)
_OptionalChannelTargetInfoTypeDef = TypedDict(
    "_OptionalChannelTargetInfoTypeDef",
    {
        "RetryIntervalInMinutes": int,
    },
    total=False,
)

class ChannelTargetInfoTypeDef(
    _RequiredChannelTargetInfoTypeDef, _OptionalChannelTargetInfoTypeDef
):
    pass

ContactChannelAddressTypeDef = TypedDict(
    "ContactChannelAddressTypeDef",
    {
        "SimpleAddress": str,
    },
    total=False,
)

_RequiredContactChannelTypeDef = TypedDict(
    "_RequiredContactChannelTypeDef",
    {
        "ContactChannelArn": str,
        "ContactArn": str,
        "Name": str,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
        "ActivationStatus": ActivationStatusType,
    },
)
_OptionalContactChannelTypeDef = TypedDict(
    "_OptionalContactChannelTypeDef",
    {
        "Type": ChannelTypeType,
    },
    total=False,
)

class ContactChannelTypeDef(_RequiredContactChannelTypeDef, _OptionalContactChannelTypeDef):
    pass

_RequiredContactTargetInfoTypeDef = TypedDict(
    "_RequiredContactTargetInfoTypeDef",
    {
        "IsEssential": bool,
    },
)
_OptionalContactTargetInfoTypeDef = TypedDict(
    "_OptionalContactTargetInfoTypeDef",
    {
        "ContactId": str,
    },
    total=False,
)

class ContactTargetInfoTypeDef(
    _RequiredContactTargetInfoTypeDef, _OptionalContactTargetInfoTypeDef
):
    pass

_RequiredContactTypeDef = TypedDict(
    "_RequiredContactTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "Type": ContactTypeType,
    },
)
_OptionalContactTypeDef = TypedDict(
    "_OptionalContactTypeDef",
    {
        "DisplayName": str,
    },
    total=False,
)

class ContactTypeDef(_RequiredContactTypeDef, _OptionalContactTypeDef):
    pass

CoverageTimeTypeDef = TypedDict(
    "CoverageTimeTypeDef",
    {
        "Start": "HandOffTimeTypeDef",
        "End": "HandOffTimeTypeDef",
    },
    total=False,
)

_RequiredCreateContactChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactChannelRequestRequestTypeDef",
    {
        "ContactId": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
    },
)
_OptionalCreateContactChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactChannelRequestRequestTypeDef",
    {
        "DeferActivation": bool,
        "IdempotencyToken": str,
    },
    total=False,
)

class CreateContactChannelRequestRequestTypeDef(
    _RequiredCreateContactChannelRequestRequestTypeDef,
    _OptionalCreateContactChannelRequestRequestTypeDef,
):
    pass

CreateContactChannelResultTypeDef = TypedDict(
    "CreateContactChannelResultTypeDef",
    {
        "ContactChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContactRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContactRequestRequestTypeDef",
    {
        "Alias": str,
        "Type": ContactTypeType,
        "Plan": "PlanTypeDef",
    },
)
_OptionalCreateContactRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContactRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Tags": List["TagTypeDef"],
        "IdempotencyToken": str,
    },
    total=False,
)

class CreateContactRequestRequestTypeDef(
    _RequiredCreateContactRequestRequestTypeDef, _OptionalCreateContactRequestRequestTypeDef
):
    pass

CreateContactResultTypeDef = TypedDict(
    "CreateContactResultTypeDef",
    {
        "ContactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRotationOverrideRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRotationOverrideRequestRequestTypeDef",
    {
        "RotationId": str,
        "NewContactIds": List[str],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalCreateRotationOverrideRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRotationOverrideRequestRequestTypeDef",
    {
        "IdempotencyToken": str,
    },
    total=False,
)

class CreateRotationOverrideRequestRequestTypeDef(
    _RequiredCreateRotationOverrideRequestRequestTypeDef,
    _OptionalCreateRotationOverrideRequestRequestTypeDef,
):
    pass

CreateRotationOverrideResultTypeDef = TypedDict(
    "CreateRotationOverrideResultTypeDef",
    {
        "RotationOverrideId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRotationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRotationRequestRequestTypeDef",
    {
        "Name": str,
        "ContactIds": List[str],
        "TimeZoneId": str,
        "Recurrence": "RecurrenceSettingsTypeDef",
    },
)
_OptionalCreateRotationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRotationRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "Tags": List["TagTypeDef"],
        "IdempotencyToken": str,
    },
    total=False,
)

class CreateRotationRequestRequestTypeDef(
    _RequiredCreateRotationRequestRequestTypeDef, _OptionalCreateRotationRequestRequestTypeDef
):
    pass

CreateRotationResultTypeDef = TypedDict(
    "CreateRotationResultTypeDef",
    {
        "RotationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateContactChannelRequestRequestTypeDef = TypedDict(
    "DeactivateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

DeleteContactChannelRequestRequestTypeDef = TypedDict(
    "DeleteContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

DeleteContactRequestRequestTypeDef = TypedDict(
    "DeleteContactRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)

DeleteRotationOverrideRequestRequestTypeDef = TypedDict(
    "DeleteRotationOverrideRequestRequestTypeDef",
    {
        "RotationId": str,
        "RotationOverrideId": str,
    },
)

DeleteRotationRequestRequestTypeDef = TypedDict(
    "DeleteRotationRequestRequestTypeDef",
    {
        "RotationId": str,
    },
)

DescribeEngagementRequestRequestTypeDef = TypedDict(
    "DescribeEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
    },
)

DescribeEngagementResultTypeDef = TypedDict(
    "DescribeEngagementResultTypeDef",
    {
        "ContactArn": str,
        "EngagementArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "StartTime": datetime,
        "StopTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePageRequestRequestTypeDef = TypedDict(
    "DescribePageRequestRequestTypeDef",
    {
        "PageId": str,
    },
)

DescribePageResultTypeDef = TypedDict(
    "DescribePageResultTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "SentTime": datetime,
        "ReadTime": datetime,
        "DeliveryTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEngagementTypeDef = TypedDict(
    "_RequiredEngagementTypeDef",
    {
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
    },
)
_OptionalEngagementTypeDef = TypedDict(
    "_OptionalEngagementTypeDef",
    {
        "IncidentId": str,
        "StartTime": datetime,
        "StopTime": datetime,
    },
    total=False,
)

class EngagementTypeDef(_RequiredEngagementTypeDef, _OptionalEngagementTypeDef):
    pass

GetContactChannelRequestRequestTypeDef = TypedDict(
    "GetContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

GetContactChannelResultTypeDef = TypedDict(
    "GetContactChannelResultTypeDef",
    {
        "ContactArn": str,
        "ContactChannelArn": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
        "ActivationStatus": ActivationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactPolicyRequestRequestTypeDef = TypedDict(
    "GetContactPolicyRequestRequestTypeDef",
    {
        "ContactArn": str,
    },
)

GetContactPolicyResultTypeDef = TypedDict(
    "GetContactPolicyResultTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactRequestRequestTypeDef = TypedDict(
    "GetContactRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)

GetContactResultTypeDef = TypedDict(
    "GetContactResultTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "DisplayName": str,
        "Type": ContactTypeType,
        "Plan": "PlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRotationOverrideRequestRequestTypeDef = TypedDict(
    "GetRotationOverrideRequestRequestTypeDef",
    {
        "RotationId": str,
        "RotationOverrideId": str,
    },
)

GetRotationOverrideResultTypeDef = TypedDict(
    "GetRotationOverrideResultTypeDef",
    {
        "RotationOverrideId": str,
        "RotationArn": str,
        "NewContactIds": List[str],
        "StartTime": datetime,
        "EndTime": datetime,
        "CreateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRotationRequestRequestTypeDef = TypedDict(
    "GetRotationRequestRequestTypeDef",
    {
        "RotationId": str,
    },
)

GetRotationResultTypeDef = TypedDict(
    "GetRotationResultTypeDef",
    {
        "RotationArn": str,
        "Name": str,
        "ContactIds": List[str],
        "StartTime": datetime,
        "TimeZoneId": str,
        "Recurrence": "RecurrenceSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HandOffTimeTypeDef = TypedDict(
    "HandOffTimeTypeDef",
    {
        "HourOfDay": int,
        "MinuteOfHour": int,
    },
)

_RequiredListContactChannelsRequestRequestTypeDef = TypedDict(
    "_RequiredListContactChannelsRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)
_OptionalListContactChannelsRequestRequestTypeDef = TypedDict(
    "_OptionalListContactChannelsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListContactChannelsRequestRequestTypeDef(
    _RequiredListContactChannelsRequestRequestTypeDef,
    _OptionalListContactChannelsRequestRequestTypeDef,
):
    pass

ListContactChannelsResultTypeDef = TypedDict(
    "ListContactChannelsResultTypeDef",
    {
        "NextToken": str,
        "ContactChannels": List["ContactChannelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactsRequestRequestTypeDef = TypedDict(
    "ListContactsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "AliasPrefix": str,
        "Type": ContactTypeType,
    },
    total=False,
)

ListContactsResultTypeDef = TypedDict(
    "ListContactsResultTypeDef",
    {
        "NextToken": str,
        "Contacts": List["ContactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngagementsRequestRequestTypeDef = TypedDict(
    "ListEngagementsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "IncidentId": str,
        "TimeRangeValue": "TimeRangeTypeDef",
    },
    total=False,
)

ListEngagementsResultTypeDef = TypedDict(
    "ListEngagementsResultTypeDef",
    {
        "NextToken": str,
        "Engagements": List["EngagementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPageReceiptsRequestRequestTypeDef = TypedDict(
    "_RequiredListPageReceiptsRequestRequestTypeDef",
    {
        "PageId": str,
    },
)
_OptionalListPageReceiptsRequestRequestTypeDef = TypedDict(
    "_OptionalListPageReceiptsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPageReceiptsRequestRequestTypeDef(
    _RequiredListPageReceiptsRequestRequestTypeDef, _OptionalListPageReceiptsRequestRequestTypeDef
):
    pass

ListPageReceiptsResultTypeDef = TypedDict(
    "ListPageReceiptsResultTypeDef",
    {
        "NextToken": str,
        "Receipts": List["ReceiptTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPageResolutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPageResolutionsRequestRequestTypeDef",
    {
        "PageId": str,
    },
)
_OptionalListPageResolutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPageResolutionsRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListPageResolutionsRequestRequestTypeDef(
    _RequiredListPageResolutionsRequestRequestTypeDef,
    _OptionalListPageResolutionsRequestRequestTypeDef,
):
    pass

ListPageResolutionsResultTypeDef = TypedDict(
    "ListPageResolutionsResultTypeDef",
    {
        "NextToken": str,
        "PageResolutions": List["ResolutionContactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPagesByContactRequestRequestTypeDef = TypedDict(
    "_RequiredListPagesByContactRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)
_OptionalListPagesByContactRequestRequestTypeDef = TypedDict(
    "_OptionalListPagesByContactRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPagesByContactRequestRequestTypeDef(
    _RequiredListPagesByContactRequestRequestTypeDef,
    _OptionalListPagesByContactRequestRequestTypeDef,
):
    pass

ListPagesByContactResultTypeDef = TypedDict(
    "ListPagesByContactResultTypeDef",
    {
        "NextToken": str,
        "Pages": List["PageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPagesByEngagementRequestRequestTypeDef = TypedDict(
    "_RequiredListPagesByEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
    },
)
_OptionalListPagesByEngagementRequestRequestTypeDef = TypedDict(
    "_OptionalListPagesByEngagementRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPagesByEngagementRequestRequestTypeDef(
    _RequiredListPagesByEngagementRequestRequestTypeDef,
    _OptionalListPagesByEngagementRequestRequestTypeDef,
):
    pass

ListPagesByEngagementResultTypeDef = TypedDict(
    "ListPagesByEngagementResultTypeDef",
    {
        "NextToken": str,
        "Pages": List["PageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPreviewRotationShiftsRequestRequestTypeDef = TypedDict(
    "_RequiredListPreviewRotationShiftsRequestRequestTypeDef",
    {
        "EndTime": Union[datetime, str],
        "Members": List[str],
        "TimeZoneId": str,
        "Recurrence": "RecurrenceSettingsTypeDef",
    },
)
_OptionalListPreviewRotationShiftsRequestRequestTypeDef = TypedDict(
    "_OptionalListPreviewRotationShiftsRequestRequestTypeDef",
    {
        "RotationStartTime": Union[datetime, str],
        "StartTime": Union[datetime, str],
        "Overrides": List["PreviewOverrideTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListPreviewRotationShiftsRequestRequestTypeDef(
    _RequiredListPreviewRotationShiftsRequestRequestTypeDef,
    _OptionalListPreviewRotationShiftsRequestRequestTypeDef,
):
    pass

ListPreviewRotationShiftsResultTypeDef = TypedDict(
    "ListPreviewRotationShiftsResultTypeDef",
    {
        "RotationShifts": List["RotationShiftTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRotationOverridesRequestRequestTypeDef = TypedDict(
    "_RequiredListRotationOverridesRequestRequestTypeDef",
    {
        "RotationId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)
_OptionalListRotationOverridesRequestRequestTypeDef = TypedDict(
    "_OptionalListRotationOverridesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRotationOverridesRequestRequestTypeDef(
    _RequiredListRotationOverridesRequestRequestTypeDef,
    _OptionalListRotationOverridesRequestRequestTypeDef,
):
    pass

ListRotationOverridesResultTypeDef = TypedDict(
    "ListRotationOverridesResultTypeDef",
    {
        "RotationOverrides": List["RotationOverrideTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRotationShiftsRequestRequestTypeDef = TypedDict(
    "_RequiredListRotationShiftsRequestRequestTypeDef",
    {
        "RotationId": str,
        "EndTime": Union[datetime, str],
    },
)
_OptionalListRotationShiftsRequestRequestTypeDef = TypedDict(
    "_OptionalListRotationShiftsRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListRotationShiftsRequestRequestTypeDef(
    _RequiredListRotationShiftsRequestRequestTypeDef,
    _OptionalListRotationShiftsRequestRequestTypeDef,
):
    pass

ListRotationShiftsResultTypeDef = TypedDict(
    "ListRotationShiftsResultTypeDef",
    {
        "RotationShifts": List["RotationShiftTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRotationsRequestRequestTypeDef = TypedDict(
    "ListRotationsRequestRequestTypeDef",
    {
        "RotationNamePrefix": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListRotationsResultTypeDef = TypedDict(
    "ListRotationsResultTypeDef",
    {
        "NextToken": str,
        "Rotations": List["RotationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonthlySettingTypeDef = TypedDict(
    "MonthlySettingTypeDef",
    {
        "DayOfMonth": int,
        "HandOffTime": "HandOffTimeTypeDef",
    },
)

_RequiredPageTypeDef = TypedDict(
    "_RequiredPageTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
    },
)
_OptionalPageTypeDef = TypedDict(
    "_OptionalPageTypeDef",
    {
        "IncidentId": str,
        "SentTime": datetime,
        "DeliveryTime": datetime,
        "ReadTime": datetime,
    },
    total=False,
)

class PageTypeDef(_RequiredPageTypeDef, _OptionalPageTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PlanTypeDef = TypedDict(
    "PlanTypeDef",
    {
        "Stages": List["StageTypeDef"],
        "RotationIds": List[str],
    },
    total=False,
)

PreviewOverrideTypeDef = TypedDict(
    "PreviewOverrideTypeDef",
    {
        "NewMembers": List[str],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

PutContactPolicyRequestRequestTypeDef = TypedDict(
    "PutContactPolicyRequestRequestTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
    },
)

_RequiredReceiptTypeDef = TypedDict(
    "_RequiredReceiptTypeDef",
    {
        "ReceiptType": ReceiptTypeType,
        "ReceiptTime": datetime,
    },
)
_OptionalReceiptTypeDef = TypedDict(
    "_OptionalReceiptTypeDef",
    {
        "ContactChannelArn": str,
        "ReceiptInfo": str,
    },
    total=False,
)

class ReceiptTypeDef(_RequiredReceiptTypeDef, _OptionalReceiptTypeDef):
    pass

_RequiredRecurrenceSettingsTypeDef = TypedDict(
    "_RequiredRecurrenceSettingsTypeDef",
    {
        "NumberOfOnCalls": int,
        "RecurrenceMultiplier": int,
    },
)
_OptionalRecurrenceSettingsTypeDef = TypedDict(
    "_OptionalRecurrenceSettingsTypeDef",
    {
        "MonthlySettings": List["MonthlySettingTypeDef"],
        "WeeklySettings": List["WeeklySettingTypeDef"],
        "DailySettings": List["HandOffTimeTypeDef"],
        "ShiftCoverages": Dict[DayOfWeekType, List["CoverageTimeTypeDef"]],
    },
    total=False,
)

class RecurrenceSettingsTypeDef(
    _RequiredRecurrenceSettingsTypeDef, _OptionalRecurrenceSettingsTypeDef
):
    pass

_RequiredResolutionContactTypeDef = TypedDict(
    "_RequiredResolutionContactTypeDef",
    {
        "ContactArn": str,
        "Type": ContactTypeType,
    },
)
_OptionalResolutionContactTypeDef = TypedDict(
    "_OptionalResolutionContactTypeDef",
    {
        "StageIndex": int,
    },
    total=False,
)

class ResolutionContactTypeDef(
    _RequiredResolutionContactTypeDef, _OptionalResolutionContactTypeDef
):
    pass

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RotationOverrideTypeDef = TypedDict(
    "RotationOverrideTypeDef",
    {
        "RotationOverrideId": str,
        "NewContactIds": List[str],
        "StartTime": datetime,
        "EndTime": datetime,
        "CreateTime": datetime,
    },
)

_RequiredRotationShiftTypeDef = TypedDict(
    "_RequiredRotationShiftTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
    },
)
_OptionalRotationShiftTypeDef = TypedDict(
    "_OptionalRotationShiftTypeDef",
    {
        "ContactIds": List[str],
        "Type": ShiftTypeType,
        "ShiftDetails": "ShiftDetailsTypeDef",
    },
    total=False,
)

class RotationShiftTypeDef(_RequiredRotationShiftTypeDef, _OptionalRotationShiftTypeDef):
    pass

_RequiredRotationTypeDef = TypedDict(
    "_RequiredRotationTypeDef",
    {
        "RotationArn": str,
        "Name": str,
    },
)
_OptionalRotationTypeDef = TypedDict(
    "_OptionalRotationTypeDef",
    {
        "ContactIds": List[str],
        "StartTime": datetime,
        "TimeZoneId": str,
        "Recurrence": "RecurrenceSettingsTypeDef",
    },
    total=False,
)

class RotationTypeDef(_RequiredRotationTypeDef, _OptionalRotationTypeDef):
    pass

SendActivationCodeRequestRequestTypeDef = TypedDict(
    "SendActivationCodeRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

ShiftDetailsTypeDef = TypedDict(
    "ShiftDetailsTypeDef",
    {
        "OverriddenContactIds": List[str],
    },
)

StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "DurationInMinutes": int,
        "Targets": List["TargetTypeDef"],
    },
)

_RequiredStartEngagementRequestRequestTypeDef = TypedDict(
    "_RequiredStartEngagementRequestRequestTypeDef",
    {
        "ContactId": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
    },
)
_OptionalStartEngagementRequestRequestTypeDef = TypedDict(
    "_OptionalStartEngagementRequestRequestTypeDef",
    {
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "IdempotencyToken": str,
    },
    total=False,
)

class StartEngagementRequestRequestTypeDef(
    _RequiredStartEngagementRequestRequestTypeDef, _OptionalStartEngagementRequestRequestTypeDef
):
    pass

StartEngagementResultTypeDef = TypedDict(
    "StartEngagementResultTypeDef",
    {
        "EngagementArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopEngagementRequestRequestTypeDef = TypedDict(
    "_RequiredStopEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
    },
)
_OptionalStopEngagementRequestRequestTypeDef = TypedDict(
    "_OptionalStopEngagementRequestRequestTypeDef",
    {
        "Reason": str,
    },
    total=False,
)

class StopEngagementRequestRequestTypeDef(
    _RequiredStopEngagementRequestRequestTypeDef, _OptionalStopEngagementRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "ChannelTargetInfo": "ChannelTargetInfoTypeDef",
        "ContactTargetInfo": "ContactTargetInfoTypeDef",
    },
    total=False,
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateContactChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)
_OptionalUpdateContactChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactChannelRequestRequestTypeDef",
    {
        "Name": str,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
    },
    total=False,
)

class UpdateContactChannelRequestRequestTypeDef(
    _RequiredUpdateContactChannelRequestRequestTypeDef,
    _OptionalUpdateContactChannelRequestRequestTypeDef,
):
    pass

_RequiredUpdateContactRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContactRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)
_OptionalUpdateContactRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContactRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Plan": "PlanTypeDef",
    },
    total=False,
)

class UpdateContactRequestRequestTypeDef(
    _RequiredUpdateContactRequestRequestTypeDef, _OptionalUpdateContactRequestRequestTypeDef
):
    pass

_RequiredUpdateRotationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRotationRequestRequestTypeDef",
    {
        "RotationId": str,
        "Recurrence": "RecurrenceSettingsTypeDef",
    },
)
_OptionalUpdateRotationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRotationRequestRequestTypeDef",
    {
        "ContactIds": List[str],
        "StartTime": Union[datetime, str],
        "TimeZoneId": str,
    },
    total=False,
)

class UpdateRotationRequestRequestTypeDef(
    _RequiredUpdateRotationRequestRequestTypeDef, _OptionalUpdateRotationRequestRequestTypeDef
):
    pass

WeeklySettingTypeDef = TypedDict(
    "WeeklySettingTypeDef",
    {
        "DayOfWeek": DayOfWeekType,
        "HandOffTime": "HandOffTimeTypeDef",
    },
)
