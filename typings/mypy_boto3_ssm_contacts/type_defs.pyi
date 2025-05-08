"""
Type annotations for ssm-contacts service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_contacts/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ssm_contacts.type_defs import AcceptPageRequestTypeDef

    data: AcceptPageRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptPageRequestTypeDef",
    "ActivateContactChannelRequestTypeDef",
    "ChannelTargetInfoTypeDef",
    "ContactChannelAddressTypeDef",
    "ContactChannelTypeDef",
    "ContactTargetInfoTypeDef",
    "ContactTypeDef",
    "CoverageTimeTypeDef",
    "CreateContactChannelRequestTypeDef",
    "CreateContactChannelResultTypeDef",
    "CreateContactRequestTypeDef",
    "CreateContactResultTypeDef",
    "CreateRotationOverrideRequestTypeDef",
    "CreateRotationOverrideResultTypeDef",
    "CreateRotationRequestTypeDef",
    "CreateRotationResultTypeDef",
    "DeactivateContactChannelRequestTypeDef",
    "DeleteContactChannelRequestTypeDef",
    "DeleteContactRequestTypeDef",
    "DeleteRotationOverrideRequestTypeDef",
    "DeleteRotationRequestTypeDef",
    "DescribeEngagementRequestTypeDef",
    "DescribeEngagementResultTypeDef",
    "DescribePageRequestTypeDef",
    "DescribePageResultTypeDef",
    "EngagementTypeDef",
    "GetContactChannelRequestTypeDef",
    "GetContactChannelResultTypeDef",
    "GetContactPolicyRequestTypeDef",
    "GetContactPolicyResultTypeDef",
    "GetContactRequestTypeDef",
    "GetContactResultTypeDef",
    "GetRotationOverrideRequestTypeDef",
    "GetRotationOverrideResultTypeDef",
    "GetRotationRequestTypeDef",
    "GetRotationResultTypeDef",
    "HandOffTimeTypeDef",
    "ListContactChannelsRequestPaginateTypeDef",
    "ListContactChannelsRequestTypeDef",
    "ListContactChannelsResultTypeDef",
    "ListContactsRequestPaginateTypeDef",
    "ListContactsRequestTypeDef",
    "ListContactsResultTypeDef",
    "ListEngagementsRequestPaginateTypeDef",
    "ListEngagementsRequestTypeDef",
    "ListEngagementsResultTypeDef",
    "ListPageReceiptsRequestPaginateTypeDef",
    "ListPageReceiptsRequestTypeDef",
    "ListPageReceiptsResultTypeDef",
    "ListPageResolutionsRequestPaginateTypeDef",
    "ListPageResolutionsRequestTypeDef",
    "ListPageResolutionsResultTypeDef",
    "ListPagesByContactRequestPaginateTypeDef",
    "ListPagesByContactRequestTypeDef",
    "ListPagesByContactResultTypeDef",
    "ListPagesByEngagementRequestPaginateTypeDef",
    "ListPagesByEngagementRequestTypeDef",
    "ListPagesByEngagementResultTypeDef",
    "ListPreviewRotationShiftsRequestPaginateTypeDef",
    "ListPreviewRotationShiftsRequestTypeDef",
    "ListPreviewRotationShiftsResultTypeDef",
    "ListRotationOverridesRequestPaginateTypeDef",
    "ListRotationOverridesRequestTypeDef",
    "ListRotationOverridesResultTypeDef",
    "ListRotationShiftsRequestPaginateTypeDef",
    "ListRotationShiftsRequestTypeDef",
    "ListRotationShiftsResultTypeDef",
    "ListRotationsRequestPaginateTypeDef",
    "ListRotationsRequestTypeDef",
    "ListRotationsResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "MonthlySettingTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PlanOutputTypeDef",
    "PlanTypeDef",
    "PlanUnionTypeDef",
    "PreviewOverrideTypeDef",
    "PutContactPolicyRequestTypeDef",
    "ReceiptTypeDef",
    "RecurrenceSettingsOutputTypeDef",
    "RecurrenceSettingsTypeDef",
    "RecurrenceSettingsUnionTypeDef",
    "ResolutionContactTypeDef",
    "ResponseMetadataTypeDef",
    "RotationOverrideTypeDef",
    "RotationShiftTypeDef",
    "RotationTypeDef",
    "SendActivationCodeRequestTypeDef",
    "ShiftDetailsTypeDef",
    "StageOutputTypeDef",
    "StageTypeDef",
    "StartEngagementRequestTypeDef",
    "StartEngagementResultTypeDef",
    "StopEngagementRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TimeRangeTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateContactChannelRequestTypeDef",
    "UpdateContactRequestTypeDef",
    "UpdateRotationRequestTypeDef",
    "WeeklySettingTypeDef",
)

class AcceptPageRequestTypeDef(TypedDict):
    PageId: str
    AcceptType: AcceptTypeType
    AcceptCode: str
    ContactChannelId: NotRequired[str]
    Note: NotRequired[str]
    AcceptCodeValidation: NotRequired[AcceptCodeValidationType]

class ActivateContactChannelRequestTypeDef(TypedDict):
    ContactChannelId: str
    ActivationCode: str

class ChannelTargetInfoTypeDef(TypedDict):
    ContactChannelId: str
    RetryIntervalInMinutes: NotRequired[int]

class ContactChannelAddressTypeDef(TypedDict):
    SimpleAddress: NotRequired[str]

class ContactTargetInfoTypeDef(TypedDict):
    IsEssential: bool
    ContactId: NotRequired[str]

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "Type": ContactTypeType,
        "DisplayName": NotRequired[str],
    },
)

class HandOffTimeTypeDef(TypedDict):
    HourOfDay: int
    MinuteOfHour: int

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class DeactivateContactChannelRequestTypeDef(TypedDict):
    ContactChannelId: str

class DeleteContactChannelRequestTypeDef(TypedDict):
    ContactChannelId: str

class DeleteContactRequestTypeDef(TypedDict):
    ContactId: str

class DeleteRotationOverrideRequestTypeDef(TypedDict):
    RotationId: str
    RotationOverrideId: str

class DeleteRotationRequestTypeDef(TypedDict):
    RotationId: str

class DescribeEngagementRequestTypeDef(TypedDict):
    EngagementId: str

class DescribePageRequestTypeDef(TypedDict):
    PageId: str

class EngagementTypeDef(TypedDict):
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: NotRequired[str]
    StartTime: NotRequired[datetime]
    StopTime: NotRequired[datetime]

class GetContactChannelRequestTypeDef(TypedDict):
    ContactChannelId: str

class GetContactPolicyRequestTypeDef(TypedDict):
    ContactArn: str

class GetContactRequestTypeDef(TypedDict):
    ContactId: str

class GetRotationOverrideRequestTypeDef(TypedDict):
    RotationId: str
    RotationOverrideId: str

class GetRotationRequestTypeDef(TypedDict):
    RotationId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListContactChannelsRequestTypeDef(TypedDict):
    ContactId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

ListContactsRequestTypeDef = TypedDict(
    "ListContactsRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AliasPrefix": NotRequired[str],
        "Type": NotRequired[ContactTypeType],
    },
)

class ListPageReceiptsRequestTypeDef(TypedDict):
    PageId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ReceiptTypeDef(TypedDict):
    ReceiptType: ReceiptTypeType
    ReceiptTime: datetime
    ContactChannelArn: NotRequired[str]
    ReceiptInfo: NotRequired[str]

class ListPageResolutionsRequestTypeDef(TypedDict):
    PageId: str
    NextToken: NotRequired[str]

ResolutionContactTypeDef = TypedDict(
    "ResolutionContactTypeDef",
    {
        "ContactArn": str,
        "Type": ContactTypeType,
        "StageIndex": NotRequired[int],
    },
)

class ListPagesByContactRequestTypeDef(TypedDict):
    ContactId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PageTypeDef(TypedDict):
    PageArn: str
    EngagementArn: str
    ContactArn: str
    Sender: str
    IncidentId: NotRequired[str]
    SentTime: NotRequired[datetime]
    DeliveryTime: NotRequired[datetime]
    ReadTime: NotRequired[datetime]

class ListPagesByEngagementRequestTypeDef(TypedDict):
    EngagementId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RotationOverrideTypeDef(TypedDict):
    RotationOverrideId: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime

class ListRotationsRequestTypeDef(TypedDict):
    RotationNamePrefix: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class PutContactPolicyRequestTypeDef(TypedDict):
    ContactArn: str
    Policy: str

class ShiftDetailsTypeDef(TypedDict):
    OverriddenContactIds: List[str]

class SendActivationCodeRequestTypeDef(TypedDict):
    ContactChannelId: str

class StartEngagementRequestTypeDef(TypedDict):
    ContactId: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: NotRequired[str]
    PublicContent: NotRequired[str]
    IncidentId: NotRequired[str]
    IdempotencyToken: NotRequired[str]

class StopEngagementRequestTypeDef(TypedDict):
    EngagementId: str
    Reason: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

ContactChannelTypeDef = TypedDict(
    "ContactChannelTypeDef",
    {
        "ContactChannelArn": str,
        "ContactArn": str,
        "Name": str,
        "DeliveryAddress": ContactChannelAddressTypeDef,
        "ActivationStatus": ActivationStatusType,
        "Type": NotRequired[ChannelTypeType],
    },
)
CreateContactChannelRequestTypeDef = TypedDict(
    "CreateContactChannelRequestTypeDef",
    {
        "ContactId": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": ContactChannelAddressTypeDef,
        "DeferActivation": NotRequired[bool],
        "IdempotencyToken": NotRequired[str],
    },
)

class UpdateContactChannelRequestTypeDef(TypedDict):
    ContactChannelId: str
    Name: NotRequired[str]
    DeliveryAddress: NotRequired[ContactChannelAddressTypeDef]

class TargetTypeDef(TypedDict):
    ChannelTargetInfo: NotRequired[ChannelTargetInfoTypeDef]
    ContactTargetInfo: NotRequired[ContactTargetInfoTypeDef]

class CoverageTimeTypeDef(TypedDict):
    Start: NotRequired[HandOffTimeTypeDef]
    End: NotRequired[HandOffTimeTypeDef]

class MonthlySettingTypeDef(TypedDict):
    DayOfMonth: int
    HandOffTime: HandOffTimeTypeDef

class WeeklySettingTypeDef(TypedDict):
    DayOfWeek: DayOfWeekType
    HandOffTime: HandOffTimeTypeDef

class CreateContactChannelResultTypeDef(TypedDict):
    ContactChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactResultTypeDef(TypedDict):
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRotationOverrideResultTypeDef(TypedDict):
    RotationOverrideId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRotationResultTypeDef(TypedDict):
    RotationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngagementResultTypeDef(TypedDict):
    ContactArn: str
    EngagementArn: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: str
    PublicContent: str
    IncidentId: str
    StartTime: datetime
    StopTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePageResultTypeDef(TypedDict):
    PageArn: str
    EngagementArn: str
    ContactArn: str
    Sender: str
    Subject: str
    Content: str
    PublicSubject: str
    PublicContent: str
    IncidentId: str
    SentTime: datetime
    ReadTime: datetime
    DeliveryTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

GetContactChannelResultTypeDef = TypedDict(
    "GetContactChannelResultTypeDef",
    {
        "ContactArn": str,
        "ContactChannelArn": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": ContactChannelAddressTypeDef,
        "ActivationStatus": ActivationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetContactPolicyResultTypeDef(TypedDict):
    ContactArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRotationOverrideResultTypeDef(TypedDict):
    RotationOverrideId: str
    RotationArn: str
    NewContactIds: List[str]
    StartTime: datetime
    EndTime: datetime
    CreateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListContactsResultTypeDef(TypedDict):
    Contacts: List[ContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StartEngagementResultTypeDef(TypedDict):
    EngagementArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateRotationOverrideRequestTypeDef(TypedDict):
    RotationId: str
    NewContactIds: Sequence[str]
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    IdempotencyToken: NotRequired[str]

class ListRotationOverridesRequestTypeDef(TypedDict):
    RotationId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListRotationShiftsRequestTypeDef(TypedDict):
    RotationId: str
    EndTime: TimestampTypeDef
    StartTime: NotRequired[TimestampTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class PreviewOverrideTypeDef(TypedDict):
    NewMembers: NotRequired[Sequence[str]]
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]

class TimeRangeTypeDef(TypedDict):
    StartTime: NotRequired[TimestampTypeDef]
    EndTime: NotRequired[TimestampTypeDef]

class ListEngagementsResultTypeDef(TypedDict):
    Engagements: List[EngagementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListContactChannelsRequestPaginateTypeDef(TypedDict):
    ContactId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListContactsRequestPaginateTypeDef = TypedDict(
    "ListContactsRequestPaginateTypeDef",
    {
        "AliasPrefix": NotRequired[str],
        "Type": NotRequired[ContactTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListPageReceiptsRequestPaginateTypeDef(TypedDict):
    PageId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPageResolutionsRequestPaginateTypeDef(TypedDict):
    PageId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPagesByContactRequestPaginateTypeDef(TypedDict):
    ContactId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPagesByEngagementRequestPaginateTypeDef(TypedDict):
    EngagementId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRotationOverridesRequestPaginateTypeDef(TypedDict):
    RotationId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRotationShiftsRequestPaginateTypeDef(TypedDict):
    RotationId: str
    EndTime: TimestampTypeDef
    StartTime: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRotationsRequestPaginateTypeDef(TypedDict):
    RotationNamePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPageReceiptsResultTypeDef(TypedDict):
    Receipts: List[ReceiptTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPageResolutionsResultTypeDef(TypedDict):
    PageResolutions: List[ResolutionContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPagesByContactResultTypeDef(TypedDict):
    Pages: List[PageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPagesByEngagementResultTypeDef(TypedDict):
    Pages: List[PageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRotationOverridesResultTypeDef(TypedDict):
    RotationOverrides: List[RotationOverrideTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

RotationShiftTypeDef = TypedDict(
    "RotationShiftTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "ContactIds": NotRequired[List[str]],
        "Type": NotRequired[ShiftTypeType],
        "ShiftDetails": NotRequired[ShiftDetailsTypeDef],
    },
)

class ListContactChannelsResultTypeDef(TypedDict):
    ContactChannels: List[ContactChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class StageOutputTypeDef(TypedDict):
    DurationInMinutes: int
    Targets: List[TargetTypeDef]

class StageTypeDef(TypedDict):
    DurationInMinutes: int
    Targets: Sequence[TargetTypeDef]

class RecurrenceSettingsOutputTypeDef(TypedDict):
    NumberOfOnCalls: int
    RecurrenceMultiplier: int
    MonthlySettings: NotRequired[List[MonthlySettingTypeDef]]
    WeeklySettings: NotRequired[List[WeeklySettingTypeDef]]
    DailySettings: NotRequired[List[HandOffTimeTypeDef]]
    ShiftCoverages: NotRequired[Dict[DayOfWeekType, List[CoverageTimeTypeDef]]]

class RecurrenceSettingsTypeDef(TypedDict):
    NumberOfOnCalls: int
    RecurrenceMultiplier: int
    MonthlySettings: NotRequired[Sequence[MonthlySettingTypeDef]]
    WeeklySettings: NotRequired[Sequence[WeeklySettingTypeDef]]
    DailySettings: NotRequired[Sequence[HandOffTimeTypeDef]]
    ShiftCoverages: NotRequired[Mapping[DayOfWeekType, Sequence[CoverageTimeTypeDef]]]

class ListEngagementsRequestPaginateTypeDef(TypedDict):
    IncidentId: NotRequired[str]
    TimeRangeValue: NotRequired[TimeRangeTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEngagementsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    IncidentId: NotRequired[str]
    TimeRangeValue: NotRequired[TimeRangeTypeDef]

class ListPreviewRotationShiftsResultTypeDef(TypedDict):
    RotationShifts: List[RotationShiftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListRotationShiftsResultTypeDef(TypedDict):
    RotationShifts: List[RotationShiftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PlanOutputTypeDef(TypedDict):
    Stages: NotRequired[List[StageOutputTypeDef]]
    RotationIds: NotRequired[List[str]]

class PlanTypeDef(TypedDict):
    Stages: NotRequired[Sequence[StageTypeDef]]
    RotationIds: NotRequired[Sequence[str]]

class GetRotationResultTypeDef(TypedDict):
    RotationArn: str
    Name: str
    ContactIds: List[str]
    StartTime: datetime
    TimeZoneId: str
    Recurrence: RecurrenceSettingsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RotationTypeDef(TypedDict):
    RotationArn: str
    Name: str
    ContactIds: NotRequired[List[str]]
    StartTime: NotRequired[datetime]
    TimeZoneId: NotRequired[str]
    Recurrence: NotRequired[RecurrenceSettingsOutputTypeDef]

RecurrenceSettingsUnionTypeDef = Union[RecurrenceSettingsTypeDef, RecurrenceSettingsOutputTypeDef]
GetContactResultTypeDef = TypedDict(
    "GetContactResultTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "DisplayName": str,
        "Type": ContactTypeType,
        "Plan": PlanOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PlanUnionTypeDef = Union[PlanTypeDef, PlanOutputTypeDef]

class ListRotationsResultTypeDef(TypedDict):
    Rotations: List[RotationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateRotationRequestTypeDef(TypedDict):
    Name: str
    ContactIds: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnionTypeDef
    StartTime: NotRequired[TimestampTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    IdempotencyToken: NotRequired[str]

class ListPreviewRotationShiftsRequestPaginateTypeDef(TypedDict):
    EndTime: TimestampTypeDef
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnionTypeDef
    RotationStartTime: NotRequired[TimestampTypeDef]
    StartTime: NotRequired[TimestampTypeDef]
    Overrides: NotRequired[Sequence[PreviewOverrideTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPreviewRotationShiftsRequestTypeDef(TypedDict):
    EndTime: TimestampTypeDef
    Members: Sequence[str]
    TimeZoneId: str
    Recurrence: RecurrenceSettingsUnionTypeDef
    RotationStartTime: NotRequired[TimestampTypeDef]
    StartTime: NotRequired[TimestampTypeDef]
    Overrides: NotRequired[Sequence[PreviewOverrideTypeDef]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class UpdateRotationRequestTypeDef(TypedDict):
    RotationId: str
    Recurrence: RecurrenceSettingsUnionTypeDef
    ContactIds: NotRequired[Sequence[str]]
    StartTime: NotRequired[TimestampTypeDef]
    TimeZoneId: NotRequired[str]

CreateContactRequestTypeDef = TypedDict(
    "CreateContactRequestTypeDef",
    {
        "Alias": str,
        "Type": ContactTypeType,
        "Plan": PlanUnionTypeDef,
        "DisplayName": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "IdempotencyToken": NotRequired[str],
    },
)

class UpdateContactRequestTypeDef(TypedDict):
    ContactId: str
    DisplayName: NotRequired[str]
    Plan: NotRequired[PlanUnionTypeDef]
