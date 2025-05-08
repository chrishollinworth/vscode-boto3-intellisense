"""
Type annotations for shield service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_shield/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_shield.type_defs import ResponseActionOutputTypeDef

    data: ResponseActionOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    ApplicationLayerAutomaticResponseStatusType,
    AttackLayerType,
    AttackPropertyIdentifierType,
    AutoRenewType,
    ProactiveEngagementStatusType,
    ProtectedResourceTypeType,
    ProtectionGroupAggregationType,
    ProtectionGroupPatternType,
    SubResourceTypeType,
    SubscriptionStateType,
    UnitType,
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
    "ApplicationLayerAutomaticResponseConfigurationTypeDef",
    "AssociateDRTLogBucketRequestTypeDef",
    "AssociateDRTRoleRequestTypeDef",
    "AssociateHealthCheckRequestTypeDef",
    "AssociateProactiveEngagementDetailsRequestTypeDef",
    "AttackDetailTypeDef",
    "AttackPropertyTypeDef",
    "AttackStatisticsDataItemTypeDef",
    "AttackSummaryTypeDef",
    "AttackVectorDescriptionTypeDef",
    "AttackVolumeStatisticsTypeDef",
    "AttackVolumeTypeDef",
    "ContributorTypeDef",
    "CreateProtectionGroupRequestTypeDef",
    "CreateProtectionRequestTypeDef",
    "CreateProtectionResponseTypeDef",
    "DeleteProtectionGroupRequestTypeDef",
    "DeleteProtectionRequestTypeDef",
    "DescribeAttackRequestTypeDef",
    "DescribeAttackResponseTypeDef",
    "DescribeAttackStatisticsResponseTypeDef",
    "DescribeDRTAccessResponseTypeDef",
    "DescribeEmergencyContactSettingsResponseTypeDef",
    "DescribeProtectionGroupRequestTypeDef",
    "DescribeProtectionGroupResponseTypeDef",
    "DescribeProtectionRequestTypeDef",
    "DescribeProtectionResponseTypeDef",
    "DescribeSubscriptionResponseTypeDef",
    "DisableApplicationLayerAutomaticResponseRequestTypeDef",
    "DisassociateDRTLogBucketRequestTypeDef",
    "DisassociateHealthCheckRequestTypeDef",
    "EmergencyContactTypeDef",
    "EnableApplicationLayerAutomaticResponseRequestTypeDef",
    "GetSubscriptionStateResponseTypeDef",
    "InclusionProtectionFiltersTypeDef",
    "InclusionProtectionGroupFiltersTypeDef",
    "LimitTypeDef",
    "ListAttacksRequestPaginateTypeDef",
    "ListAttacksRequestTypeDef",
    "ListAttacksResponseTypeDef",
    "ListProtectionGroupsRequestTypeDef",
    "ListProtectionGroupsResponseTypeDef",
    "ListProtectionsRequestPaginateTypeDef",
    "ListProtectionsRequestTypeDef",
    "ListProtectionsResponseTypeDef",
    "ListResourcesInProtectionGroupRequestTypeDef",
    "ListResourcesInProtectionGroupResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MitigationTypeDef",
    "PaginatorConfigTypeDef",
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    "ProtectionGroupLimitsTypeDef",
    "ProtectionGroupPatternTypeLimitsTypeDef",
    "ProtectionGroupTypeDef",
    "ProtectionLimitsTypeDef",
    "ProtectionTypeDef",
    "ResponseActionOutputTypeDef",
    "ResponseActionTypeDef",
    "ResponseActionUnionTypeDef",
    "ResponseMetadataTypeDef",
    "SubResourceSummaryTypeDef",
    "SubscriptionLimitsTypeDef",
    "SubscriptionTypeDef",
    "SummarizedAttackVectorTypeDef",
    "SummarizedCounterTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimeRangeOutputTypeDef",
    "TimeRangeTypeDef",
    "TimeRangeUnionTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateApplicationLayerAutomaticResponseRequestTypeDef",
    "UpdateEmergencyContactSettingsRequestTypeDef",
    "UpdateProtectionGroupRequestTypeDef",
    "UpdateSubscriptionRequestTypeDef",
)

class ResponseActionOutputTypeDef(TypedDict):
    Block: NotRequired[Dict[str, Any]]
    Count: NotRequired[Dict[str, Any]]

class AssociateDRTLogBucketRequestTypeDef(TypedDict):
    LogBucket: str

class AssociateDRTRoleRequestTypeDef(TypedDict):
    RoleArn: str

class AssociateHealthCheckRequestTypeDef(TypedDict):
    ProtectionId: str
    HealthCheckArn: str

class EmergencyContactTypeDef(TypedDict):
    EmailAddress: str
    PhoneNumber: NotRequired[str]
    ContactNotes: NotRequired[str]

class MitigationTypeDef(TypedDict):
    MitigationName: NotRequired[str]

class SummarizedCounterTypeDef(TypedDict):
    Name: NotRequired[str]
    Max: NotRequired[float]
    Average: NotRequired[float]
    Sum: NotRequired[float]
    N: NotRequired[int]
    Unit: NotRequired[str]

class ContributorTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[int]

class AttackVectorDescriptionTypeDef(TypedDict):
    VectorType: str

class AttackVolumeStatisticsTypeDef(TypedDict):
    Max: float

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteProtectionGroupRequestTypeDef(TypedDict):
    ProtectionGroupId: str

class DeleteProtectionRequestTypeDef(TypedDict):
    ProtectionId: str

class DescribeAttackRequestTypeDef(TypedDict):
    AttackId: str

class TimeRangeOutputTypeDef(TypedDict):
    FromInclusive: NotRequired[datetime]
    ToExclusive: NotRequired[datetime]

class DescribeProtectionGroupRequestTypeDef(TypedDict):
    ProtectionGroupId: str

ProtectionGroupTypeDef = TypedDict(
    "ProtectionGroupTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "Members": List[str],
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "ProtectionGroupArn": NotRequired[str],
    },
)

class DescribeProtectionRequestTypeDef(TypedDict):
    ProtectionId: NotRequired[str]
    ResourceArn: NotRequired[str]

class DisableApplicationLayerAutomaticResponseRequestTypeDef(TypedDict):
    ResourceArn: str

class DisassociateDRTLogBucketRequestTypeDef(TypedDict):
    LogBucket: str

class DisassociateHealthCheckRequestTypeDef(TypedDict):
    ProtectionId: str
    HealthCheckArn: str

class InclusionProtectionFiltersTypeDef(TypedDict):
    ResourceArns: NotRequired[Sequence[str]]
    ProtectionNames: NotRequired[Sequence[str]]
    ResourceTypes: NotRequired[Sequence[ProtectedResourceTypeType]]

class InclusionProtectionGroupFiltersTypeDef(TypedDict):
    ProtectionGroupIds: NotRequired[Sequence[str]]
    Patterns: NotRequired[Sequence[ProtectionGroupPatternType]]
    ResourceTypes: NotRequired[Sequence[ProtectedResourceTypeType]]
    Aggregations: NotRequired[Sequence[ProtectionGroupAggregationType]]

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Type": NotRequired[str],
        "Max": NotRequired[int],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListResourcesInProtectionGroupRequestTypeDef(TypedDict):
    ProtectionGroupId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class ProtectionGroupArbitraryPatternLimitsTypeDef(TypedDict):
    MaxMembers: int

class ResponseActionTypeDef(TypedDict):
    Block: NotRequired[Mapping[str, Any]]
    Count: NotRequired[Mapping[str, Any]]

TimestampTypeDef = Union[datetime, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

UpdateProtectionGroupRequestTypeDef = TypedDict(
    "UpdateProtectionGroupRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "Members": NotRequired[Sequence[str]],
    },
)

class UpdateSubscriptionRequestTypeDef(TypedDict):
    AutoRenew: NotRequired[AutoRenewType]

class ApplicationLayerAutomaticResponseConfigurationTypeDef(TypedDict):
    Status: ApplicationLayerAutomaticResponseStatusType
    Action: ResponseActionOutputTypeDef

class AssociateProactiveEngagementDetailsRequestTypeDef(TypedDict):
    EmergencyContactList: Sequence[EmergencyContactTypeDef]

class UpdateEmergencyContactSettingsRequestTypeDef(TypedDict):
    EmergencyContactList: NotRequired[Sequence[EmergencyContactTypeDef]]

class SummarizedAttackVectorTypeDef(TypedDict):
    VectorType: str
    VectorCounters: NotRequired[List[SummarizedCounterTypeDef]]

class AttackPropertyTypeDef(TypedDict):
    AttackLayer: NotRequired[AttackLayerType]
    AttackPropertyIdentifier: NotRequired[AttackPropertyIdentifierType]
    TopContributors: NotRequired[List[ContributorTypeDef]]
    Unit: NotRequired[UnitType]
    Total: NotRequired[int]

class AttackSummaryTypeDef(TypedDict):
    AttackId: NotRequired[str]
    ResourceArn: NotRequired[str]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    AttackVectors: NotRequired[List[AttackVectorDescriptionTypeDef]]

class AttackVolumeTypeDef(TypedDict):
    BitsPerSecond: NotRequired[AttackVolumeStatisticsTypeDef]
    PacketsPerSecond: NotRequired[AttackVolumeStatisticsTypeDef]
    RequestsPerSecond: NotRequired[AttackVolumeStatisticsTypeDef]

CreateProtectionGroupRequestTypeDef = TypedDict(
    "CreateProtectionGroupRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "ResourceType": NotRequired[ProtectedResourceTypeType],
        "Members": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)

class CreateProtectionRequestTypeDef(TypedDict):
    Name: str
    ResourceArn: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateProtectionResponseTypeDef(TypedDict):
    ProtectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDRTAccessResponseTypeDef(TypedDict):
    RoleArn: str
    LogBucketList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEmergencyContactSettingsResponseTypeDef(TypedDict):
    EmergencyContactList: List[EmergencyContactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubscriptionStateResponseTypeDef(TypedDict):
    SubscriptionState: SubscriptionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesInProtectionGroupResponseTypeDef(TypedDict):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProtectionGroupResponseTypeDef(TypedDict):
    ProtectionGroup: ProtectionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectionGroupsResponseTypeDef(TypedDict):
    ProtectionGroups: List[ProtectionGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProtectionsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    InclusionFilters: NotRequired[InclusionProtectionFiltersTypeDef]

class ListProtectionGroupsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    InclusionFilters: NotRequired[InclusionProtectionGroupFiltersTypeDef]

class ProtectionLimitsTypeDef(TypedDict):
    ProtectedResourceTypeLimits: List[LimitTypeDef]

class ListProtectionsRequestPaginateTypeDef(TypedDict):
    InclusionFilters: NotRequired[InclusionProtectionFiltersTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ProtectionGroupPatternTypeLimitsTypeDef(TypedDict):
    ArbitraryPatternLimits: ProtectionGroupArbitraryPatternLimitsTypeDef

ResponseActionUnionTypeDef = Union[ResponseActionTypeDef, ResponseActionOutputTypeDef]

class TimeRangeTypeDef(TypedDict):
    FromInclusive: NotRequired[TimestampTypeDef]
    ToExclusive: NotRequired[TimestampTypeDef]

class ProtectionTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    ResourceArn: NotRequired[str]
    HealthCheckIds: NotRequired[List[str]]
    ProtectionArn: NotRequired[str]
    ApplicationLayerAutomaticResponseConfiguration: NotRequired[
        ApplicationLayerAutomaticResponseConfigurationTypeDef
    ]

SubResourceSummaryTypeDef = TypedDict(
    "SubResourceSummaryTypeDef",
    {
        "Type": NotRequired[SubResourceTypeType],
        "Id": NotRequired[str],
        "AttackVectors": NotRequired[List[SummarizedAttackVectorTypeDef]],
        "Counters": NotRequired[List[SummarizedCounterTypeDef]],
    },
)

class ListAttacksResponseTypeDef(TypedDict):
    AttackSummaries: List[AttackSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AttackStatisticsDataItemTypeDef(TypedDict):
    AttackCount: int
    AttackVolume: NotRequired[AttackVolumeTypeDef]

class ProtectionGroupLimitsTypeDef(TypedDict):
    MaxProtectionGroups: int
    PatternTypeLimits: ProtectionGroupPatternTypeLimitsTypeDef

class EnableApplicationLayerAutomaticResponseRequestTypeDef(TypedDict):
    ResourceArn: str
    Action: ResponseActionUnionTypeDef

class UpdateApplicationLayerAutomaticResponseRequestTypeDef(TypedDict):
    ResourceArn: str
    Action: ResponseActionUnionTypeDef

TimeRangeUnionTypeDef = Union[TimeRangeTypeDef, TimeRangeOutputTypeDef]

class DescribeProtectionResponseTypeDef(TypedDict):
    Protection: ProtectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProtectionsResponseTypeDef(TypedDict):
    Protections: List[ProtectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AttackDetailTypeDef(TypedDict):
    AttackId: NotRequired[str]
    ResourceArn: NotRequired[str]
    SubResources: NotRequired[List[SubResourceSummaryTypeDef]]
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    AttackCounters: NotRequired[List[SummarizedCounterTypeDef]]
    AttackProperties: NotRequired[List[AttackPropertyTypeDef]]
    Mitigations: NotRequired[List[MitigationTypeDef]]

class DescribeAttackStatisticsResponseTypeDef(TypedDict):
    TimeRange: TimeRangeOutputTypeDef
    DataItems: List[AttackStatisticsDataItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionLimitsTypeDef(TypedDict):
    ProtectionLimits: ProtectionLimitsTypeDef
    ProtectionGroupLimits: ProtectionGroupLimitsTypeDef

class ListAttacksRequestPaginateTypeDef(TypedDict):
    ResourceArns: NotRequired[Sequence[str]]
    StartTime: NotRequired[TimeRangeUnionTypeDef]
    EndTime: NotRequired[TimeRangeUnionTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAttacksRequestTypeDef(TypedDict):
    ResourceArns: NotRequired[Sequence[str]]
    StartTime: NotRequired[TimeRangeUnionTypeDef]
    EndTime: NotRequired[TimeRangeUnionTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeAttackResponseTypeDef(TypedDict):
    Attack: AttackDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SubscriptionTypeDef(TypedDict):
    SubscriptionLimits: SubscriptionLimitsTypeDef
    StartTime: NotRequired[datetime]
    EndTime: NotRequired[datetime]
    TimeCommitmentInSeconds: NotRequired[int]
    AutoRenew: NotRequired[AutoRenewType]
    Limits: NotRequired[List[LimitTypeDef]]
    ProactiveEngagementStatus: NotRequired[ProactiveEngagementStatusType]
    SubscriptionArn: NotRequired[str]

class DescribeSubscriptionResponseTypeDef(TypedDict):
    Subscription: SubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
