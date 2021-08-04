"""
Type annotations for shield service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/type_defs.html)

Usage::

    ```python
    from mypy_boto3_shield.type_defs import AssociateDRTLogBucketRequestRequestTypeDef

    data: AssociateDRTLogBucketRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateDRTLogBucketRequestRequestTypeDef",
    "AssociateDRTRoleRequestRequestTypeDef",
    "AssociateHealthCheckRequestRequestTypeDef",
    "AssociateProactiveEngagementDetailsRequestRequestTypeDef",
    "AttackDetailTypeDef",
    "AttackPropertyTypeDef",
    "AttackStatisticsDataItemTypeDef",
    "AttackSummaryTypeDef",
    "AttackVectorDescriptionTypeDef",
    "AttackVolumeStatisticsTypeDef",
    "AttackVolumeTypeDef",
    "ContributorTypeDef",
    "CreateProtectionGroupRequestRequestTypeDef",
    "CreateProtectionRequestRequestTypeDef",
    "CreateProtectionResponseTypeDef",
    "DeleteProtectionGroupRequestRequestTypeDef",
    "DeleteProtectionRequestRequestTypeDef",
    "DescribeAttackRequestRequestTypeDef",
    "DescribeAttackResponseTypeDef",
    "DescribeAttackStatisticsResponseTypeDef",
    "DescribeDRTAccessResponseTypeDef",
    "DescribeEmergencyContactSettingsResponseTypeDef",
    "DescribeProtectionGroupRequestRequestTypeDef",
    "DescribeProtectionGroupResponseTypeDef",
    "DescribeProtectionRequestRequestTypeDef",
    "DescribeProtectionResponseTypeDef",
    "DescribeSubscriptionResponseTypeDef",
    "DisassociateDRTLogBucketRequestRequestTypeDef",
    "DisassociateHealthCheckRequestRequestTypeDef",
    "EmergencyContactTypeDef",
    "GetSubscriptionStateResponseTypeDef",
    "LimitTypeDef",
    "ListAttacksRequestRequestTypeDef",
    "ListAttacksResponseTypeDef",
    "ListProtectionGroupsRequestRequestTypeDef",
    "ListProtectionGroupsResponseTypeDef",
    "ListProtectionsRequestRequestTypeDef",
    "ListProtectionsResponseTypeDef",
    "ListResourcesInProtectionGroupRequestRequestTypeDef",
    "ListResourcesInProtectionGroupResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MitigationTypeDef",
    "PaginatorConfigTypeDef",
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    "ProtectionGroupLimitsTypeDef",
    "ProtectionGroupPatternTypeLimitsTypeDef",
    "ProtectionGroupTypeDef",
    "ProtectionLimitsTypeDef",
    "ProtectionTypeDef",
    "ResponseMetadataTypeDef",
    "SubResourceSummaryTypeDef",
    "SubscriptionLimitsTypeDef",
    "SubscriptionTypeDef",
    "SummarizedAttackVectorTypeDef",
    "SummarizedCounterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEmergencyContactSettingsRequestRequestTypeDef",
    "UpdateProtectionGroupRequestRequestTypeDef",
    "UpdateSubscriptionRequestRequestTypeDef",
)

AssociateDRTLogBucketRequestRequestTypeDef = TypedDict(
    "AssociateDRTLogBucketRequestRequestTypeDef",
    {
        "LogBucket": str,
    },
)

AssociateDRTRoleRequestRequestTypeDef = TypedDict(
    "AssociateDRTRoleRequestRequestTypeDef",
    {
        "RoleArn": str,
    },
)

AssociateHealthCheckRequestRequestTypeDef = TypedDict(
    "AssociateHealthCheckRequestRequestTypeDef",
    {
        "ProtectionId": str,
        "HealthCheckArn": str,
    },
)

AssociateProactiveEngagementDetailsRequestRequestTypeDef = TypedDict(
    "AssociateProactiveEngagementDetailsRequestRequestTypeDef",
    {
        "EmergencyContactList": List["EmergencyContactTypeDef"],
    },
)

AttackDetailTypeDef = TypedDict(
    "AttackDetailTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "SubResources": List["SubResourceSummaryTypeDef"],
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackCounters": List["SummarizedCounterTypeDef"],
        "AttackProperties": List["AttackPropertyTypeDef"],
        "Mitigations": List["MitigationTypeDef"],
    },
    total=False,
)

AttackPropertyTypeDef = TypedDict(
    "AttackPropertyTypeDef",
    {
        "AttackLayer": AttackLayerType,
        "AttackPropertyIdentifier": AttackPropertyIdentifierType,
        "TopContributors": List["ContributorTypeDef"],
        "Unit": UnitType,
        "Total": int,
    },
    total=False,
)

_RequiredAttackStatisticsDataItemTypeDef = TypedDict(
    "_RequiredAttackStatisticsDataItemTypeDef",
    {
        "AttackCount": int,
    },
)
_OptionalAttackStatisticsDataItemTypeDef = TypedDict(
    "_OptionalAttackStatisticsDataItemTypeDef",
    {
        "AttackVolume": "AttackVolumeTypeDef",
    },
    total=False,
)

class AttackStatisticsDataItemTypeDef(
    _RequiredAttackStatisticsDataItemTypeDef, _OptionalAttackStatisticsDataItemTypeDef
):
    pass

AttackSummaryTypeDef = TypedDict(
    "AttackSummaryTypeDef",
    {
        "AttackId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "AttackVectors": List["AttackVectorDescriptionTypeDef"],
    },
    total=False,
)

AttackVectorDescriptionTypeDef = TypedDict(
    "AttackVectorDescriptionTypeDef",
    {
        "VectorType": str,
    },
)

AttackVolumeStatisticsTypeDef = TypedDict(
    "AttackVolumeStatisticsTypeDef",
    {
        "Max": float,
    },
)

AttackVolumeTypeDef = TypedDict(
    "AttackVolumeTypeDef",
    {
        "BitsPerSecond": "AttackVolumeStatisticsTypeDef",
        "PacketsPerSecond": "AttackVolumeStatisticsTypeDef",
        "RequestsPerSecond": "AttackVolumeStatisticsTypeDef",
    },
    total=False,
)

ContributorTypeDef = TypedDict(
    "ContributorTypeDef",
    {
        "Name": str,
        "Value": int,
    },
    total=False,
)

_RequiredCreateProtectionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
    },
)
_OptionalCreateProtectionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProtectionGroupRequestRequestTypeDef",
    {
        "ResourceType": ProtectedResourceTypeType,
        "Members": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProtectionGroupRequestRequestTypeDef(
    _RequiredCreateProtectionGroupRequestRequestTypeDef,
    _OptionalCreateProtectionGroupRequestRequestTypeDef,
):
    pass

_RequiredCreateProtectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProtectionRequestRequestTypeDef",
    {
        "Name": str,
        "ResourceArn": str,
    },
)
_OptionalCreateProtectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProtectionRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProtectionRequestRequestTypeDef(
    _RequiredCreateProtectionRequestRequestTypeDef, _OptionalCreateProtectionRequestRequestTypeDef
):
    pass

CreateProtectionResponseTypeDef = TypedDict(
    "CreateProtectionResponseTypeDef",
    {
        "ProtectionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProtectionGroupRequestRequestTypeDef = TypedDict(
    "DeleteProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)

DeleteProtectionRequestRequestTypeDef = TypedDict(
    "DeleteProtectionRequestRequestTypeDef",
    {
        "ProtectionId": str,
    },
)

DescribeAttackRequestRequestTypeDef = TypedDict(
    "DescribeAttackRequestRequestTypeDef",
    {
        "AttackId": str,
    },
)

DescribeAttackResponseTypeDef = TypedDict(
    "DescribeAttackResponseTypeDef",
    {
        "Attack": "AttackDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAttackStatisticsResponseTypeDef = TypedDict(
    "DescribeAttackStatisticsResponseTypeDef",
    {
        "TimeRange": "TimeRangeTypeDef",
        "DataItems": List["AttackStatisticsDataItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDRTAccessResponseTypeDef = TypedDict(
    "DescribeDRTAccessResponseTypeDef",
    {
        "RoleArn": str,
        "LogBucketList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEmergencyContactSettingsResponseTypeDef = TypedDict(
    "DescribeEmergencyContactSettingsResponseTypeDef",
    {
        "EmergencyContactList": List["EmergencyContactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectionGroupRequestRequestTypeDef = TypedDict(
    "DescribeProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)

DescribeProtectionGroupResponseTypeDef = TypedDict(
    "DescribeProtectionGroupResponseTypeDef",
    {
        "ProtectionGroup": "ProtectionGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProtectionRequestRequestTypeDef = TypedDict(
    "DescribeProtectionRequestRequestTypeDef",
    {
        "ProtectionId": str,
        "ResourceArn": str,
    },
    total=False,
)

DescribeProtectionResponseTypeDef = TypedDict(
    "DescribeProtectionResponseTypeDef",
    {
        "Protection": "ProtectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubscriptionResponseTypeDef = TypedDict(
    "DescribeSubscriptionResponseTypeDef",
    {
        "Subscription": "SubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateDRTLogBucketRequestRequestTypeDef = TypedDict(
    "DisassociateDRTLogBucketRequestRequestTypeDef",
    {
        "LogBucket": str,
    },
)

DisassociateHealthCheckRequestRequestTypeDef = TypedDict(
    "DisassociateHealthCheckRequestRequestTypeDef",
    {
        "ProtectionId": str,
        "HealthCheckArn": str,
    },
)

_RequiredEmergencyContactTypeDef = TypedDict(
    "_RequiredEmergencyContactTypeDef",
    {
        "EmailAddress": str,
    },
)
_OptionalEmergencyContactTypeDef = TypedDict(
    "_OptionalEmergencyContactTypeDef",
    {
        "PhoneNumber": str,
        "ContactNotes": str,
    },
    total=False,
)

class EmergencyContactTypeDef(_RequiredEmergencyContactTypeDef, _OptionalEmergencyContactTypeDef):
    pass

GetSubscriptionStateResponseTypeDef = TypedDict(
    "GetSubscriptionStateResponseTypeDef",
    {
        "SubscriptionState": SubscriptionStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Type": str,
        "Max": int,
    },
    total=False,
)

ListAttacksRequestRequestTypeDef = TypedDict(
    "ListAttacksRequestRequestTypeDef",
    {
        "ResourceArns": List[str],
        "StartTime": "TimeRangeTypeDef",
        "EndTime": "TimeRangeTypeDef",
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListAttacksResponseTypeDef = TypedDict(
    "ListAttacksResponseTypeDef",
    {
        "AttackSummaries": List["AttackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectionGroupsRequestRequestTypeDef = TypedDict(
    "ListProtectionGroupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProtectionGroupsResponseTypeDef = TypedDict(
    "ListProtectionGroupsResponseTypeDef",
    {
        "ProtectionGroups": List["ProtectionGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProtectionsRequestRequestTypeDef = TypedDict(
    "ListProtectionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListProtectionsResponseTypeDef = TypedDict(
    "ListProtectionsResponseTypeDef",
    {
        "Protections": List["ProtectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesInProtectionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListResourcesInProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
    },
)
_OptionalListResourcesInProtectionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListResourcesInProtectionGroupRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListResourcesInProtectionGroupRequestRequestTypeDef(
    _RequiredListResourcesInProtectionGroupRequestRequestTypeDef,
    _OptionalListResourcesInProtectionGroupRequestRequestTypeDef,
):
    pass

ListResourcesInProtectionGroupResponseTypeDef = TypedDict(
    "ListResourcesInProtectionGroupResponseTypeDef",
    {
        "ResourceArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MitigationTypeDef = TypedDict(
    "MitigationTypeDef",
    {
        "MitigationName": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ProtectionGroupArbitraryPatternLimitsTypeDef = TypedDict(
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    {
        "MaxMembers": int,
    },
)

ProtectionGroupLimitsTypeDef = TypedDict(
    "ProtectionGroupLimitsTypeDef",
    {
        "MaxProtectionGroups": int,
        "PatternTypeLimits": "ProtectionGroupPatternTypeLimitsTypeDef",
    },
)

ProtectionGroupPatternTypeLimitsTypeDef = TypedDict(
    "ProtectionGroupPatternTypeLimitsTypeDef",
    {
        "ArbitraryPatternLimits": "ProtectionGroupArbitraryPatternLimitsTypeDef",
    },
)

_RequiredProtectionGroupTypeDef = TypedDict(
    "_RequiredProtectionGroupTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
        "Members": List[str],
    },
)
_OptionalProtectionGroupTypeDef = TypedDict(
    "_OptionalProtectionGroupTypeDef",
    {
        "ResourceType": ProtectedResourceTypeType,
        "ProtectionGroupArn": str,
    },
    total=False,
)

class ProtectionGroupTypeDef(_RequiredProtectionGroupTypeDef, _OptionalProtectionGroupTypeDef):
    pass

ProtectionLimitsTypeDef = TypedDict(
    "ProtectionLimitsTypeDef",
    {
        "ProtectedResourceTypeLimits": List["LimitTypeDef"],
    },
)

ProtectionTypeDef = TypedDict(
    "ProtectionTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceArn": str,
        "HealthCheckIds": List[str],
        "ProtectionArn": str,
    },
    total=False,
)

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

SubResourceSummaryTypeDef = TypedDict(
    "SubResourceSummaryTypeDef",
    {
        "Type": SubResourceTypeType,
        "Id": str,
        "AttackVectors": List["SummarizedAttackVectorTypeDef"],
        "Counters": List["SummarizedCounterTypeDef"],
    },
    total=False,
)

SubscriptionLimitsTypeDef = TypedDict(
    "SubscriptionLimitsTypeDef",
    {
        "ProtectionLimits": "ProtectionLimitsTypeDef",
        "ProtectionGroupLimits": "ProtectionGroupLimitsTypeDef",
    },
)

_RequiredSubscriptionTypeDef = TypedDict(
    "_RequiredSubscriptionTypeDef",
    {
        "SubscriptionLimits": "SubscriptionLimitsTypeDef",
    },
)
_OptionalSubscriptionTypeDef = TypedDict(
    "_OptionalSubscriptionTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "TimeCommitmentInSeconds": int,
        "AutoRenew": AutoRenewType,
        "Limits": List["LimitTypeDef"],
        "ProactiveEngagementStatus": ProactiveEngagementStatusType,
        "SubscriptionArn": str,
    },
    total=False,
)

class SubscriptionTypeDef(_RequiredSubscriptionTypeDef, _OptionalSubscriptionTypeDef):
    pass

_RequiredSummarizedAttackVectorTypeDef = TypedDict(
    "_RequiredSummarizedAttackVectorTypeDef",
    {
        "VectorType": str,
    },
)
_OptionalSummarizedAttackVectorTypeDef = TypedDict(
    "_OptionalSummarizedAttackVectorTypeDef",
    {
        "VectorCounters": List["SummarizedCounterTypeDef"],
    },
    total=False,
)

class SummarizedAttackVectorTypeDef(
    _RequiredSummarizedAttackVectorTypeDef, _OptionalSummarizedAttackVectorTypeDef
):
    pass

SummarizedCounterTypeDef = TypedDict(
    "SummarizedCounterTypeDef",
    {
        "Name": str,
        "Max": float,
        "Average": float,
        "Sum": float,
        "N": int,
        "Unit": str,
    },
    total=False,
)

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

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "FromInclusive": datetime,
        "ToExclusive": datetime,
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

UpdateEmergencyContactSettingsRequestRequestTypeDef = TypedDict(
    "UpdateEmergencyContactSettingsRequestRequestTypeDef",
    {
        "EmergencyContactList": List["EmergencyContactTypeDef"],
    },
    total=False,
)

_RequiredUpdateProtectionGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProtectionGroupRequestRequestTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": ProtectionGroupAggregationType,
        "Pattern": ProtectionGroupPatternType,
    },
)
_OptionalUpdateProtectionGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProtectionGroupRequestRequestTypeDef",
    {
        "ResourceType": ProtectedResourceTypeType,
        "Members": List[str],
    },
    total=False,
)

class UpdateProtectionGroupRequestRequestTypeDef(
    _RequiredUpdateProtectionGroupRequestRequestTypeDef,
    _OptionalUpdateProtectionGroupRequestRequestTypeDef,
):
    pass

UpdateSubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateSubscriptionRequestRequestTypeDef",
    {
        "AutoRenew": AutoRenewType,
    },
    total=False,
)
