"""
Main interface for shield service type definitions.

Usage::

    ```python
    from mypy_boto3_shield.type_defs import AttackDetailTypeDef

    data: AttackDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttackDetailTypeDef",
    "AttackPropertyTypeDef",
    "AttackStatisticsDataItemTypeDef",
    "AttackSummaryTypeDef",
    "AttackVectorDescriptionTypeDef",
    "AttackVolumeStatisticsTypeDef",
    "AttackVolumeTypeDef",
    "ContributorTypeDef",
    "EmergencyContactTypeDef",
    "LimitTypeDef",
    "MitigationTypeDef",
    "ProtectionGroupArbitraryPatternLimitsTypeDef",
    "ProtectionGroupLimitsTypeDef",
    "ProtectionGroupPatternTypeLimitsTypeDef",
    "ProtectionGroupTypeDef",
    "ProtectionLimitsTypeDef",
    "ProtectionTypeDef",
    "SubResourceSummaryTypeDef",
    "SubscriptionLimitsTypeDef",
    "SubscriptionTypeDef",
    "SummarizedAttackVectorTypeDef",
    "SummarizedCounterTypeDef",
    "TimeRangeTypeDef",
    "CreateProtectionResponseTypeDef",
    "DescribeAttackResponseTypeDef",
    "DescribeAttackStatisticsResponseTypeDef",
    "DescribeDRTAccessResponseTypeDef",
    "DescribeEmergencyContactSettingsResponseTypeDef",
    "DescribeProtectionGroupResponseTypeDef",
    "DescribeProtectionResponseTypeDef",
    "DescribeSubscriptionResponseTypeDef",
    "GetSubscriptionStateResponseTypeDef",
    "ListAttacksResponseTypeDef",
    "ListProtectionGroupsResponseTypeDef",
    "ListProtectionsResponseTypeDef",
    "ListResourcesInProtectionGroupResponseTypeDef",
    "PaginatorConfigTypeDef",
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
        "AttackLayer": Literal["NETWORK", "APPLICATION"],
        "AttackPropertyIdentifier": Literal[
            "DESTINATION_URL",
            "REFERRER",
            "SOURCE_ASN",
            "SOURCE_COUNTRY",
            "SOURCE_IP_ADDRESS",
            "SOURCE_USER_AGENT",
            "WORDPRESS_PINGBACK_REFLECTOR",
            "WORDPRESS_PINGBACK_SOURCE",
        ],
        "TopContributors": List["ContributorTypeDef"],
        "Unit": Literal["BITS", "BYTES", "PACKETS", "REQUESTS"],
        "Total": int,
    },
    total=False,
)

_RequiredAttackStatisticsDataItemTypeDef = TypedDict(
    "_RequiredAttackStatisticsDataItemTypeDef", {"AttackCount": int}
)
_OptionalAttackStatisticsDataItemTypeDef = TypedDict(
    "_OptionalAttackStatisticsDataItemTypeDef", {"AttackVolume": "AttackVolumeTypeDef"}, total=False
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

AttackVectorDescriptionTypeDef = TypedDict("AttackVectorDescriptionTypeDef", {"VectorType": str})

AttackVolumeStatisticsTypeDef = TypedDict("AttackVolumeStatisticsTypeDef", {"Max": float})

AttackVolumeTypeDef = TypedDict(
    "AttackVolumeTypeDef",
    {
        "BitsPerSecond": "AttackVolumeStatisticsTypeDef",
        "PacketsPerSecond": "AttackVolumeStatisticsTypeDef",
        "RequestsPerSecond": "AttackVolumeStatisticsTypeDef",
    },
    total=False,
)

ContributorTypeDef = TypedDict("ContributorTypeDef", {"Name": str, "Value": int}, total=False)

_RequiredEmergencyContactTypeDef = TypedDict(
    "_RequiredEmergencyContactTypeDef", {"EmailAddress": str}
)
_OptionalEmergencyContactTypeDef = TypedDict(
    "_OptionalEmergencyContactTypeDef", {"PhoneNumber": str, "ContactNotes": str}, total=False
)


class EmergencyContactTypeDef(_RequiredEmergencyContactTypeDef, _OptionalEmergencyContactTypeDef):
    pass


LimitTypeDef = TypedDict("LimitTypeDef", {"Type": str, "Max": int}, total=False)

MitigationTypeDef = TypedDict("MitigationTypeDef", {"MitigationName": str}, total=False)

ProtectionGroupArbitraryPatternLimitsTypeDef = TypedDict(
    "ProtectionGroupArbitraryPatternLimitsTypeDef", {"MaxMembers": int}
)

ProtectionGroupLimitsTypeDef = TypedDict(
    "ProtectionGroupLimitsTypeDef",
    {"MaxProtectionGroups": int, "PatternTypeLimits": "ProtectionGroupPatternTypeLimitsTypeDef"},
)

ProtectionGroupPatternTypeLimitsTypeDef = TypedDict(
    "ProtectionGroupPatternTypeLimitsTypeDef",
    {"ArbitraryPatternLimits": "ProtectionGroupArbitraryPatternLimitsTypeDef"},
)

_RequiredProtectionGroupTypeDef = TypedDict(
    "_RequiredProtectionGroupTypeDef",
    {
        "ProtectionGroupId": str,
        "Aggregation": Literal["SUM", "MEAN", "MAX"],
        "Pattern": Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"],
        "Members": List[str],
    },
)
_OptionalProtectionGroupTypeDef = TypedDict(
    "_OptionalProtectionGroupTypeDef",
    {
        "ResourceType": Literal[
            "CLOUDFRONT_DISTRIBUTION",
            "ROUTE_53_HOSTED_ZONE",
            "ELASTIC_IP_ALLOCATION",
            "CLASSIC_LOAD_BALANCER",
            "APPLICATION_LOAD_BALANCER",
            "GLOBAL_ACCELERATOR",
        ]
    },
    total=False,
)


class ProtectionGroupTypeDef(_RequiredProtectionGroupTypeDef, _OptionalProtectionGroupTypeDef):
    pass


ProtectionLimitsTypeDef = TypedDict(
    "ProtectionLimitsTypeDef", {"ProtectedResourceTypeLimits": List["LimitTypeDef"]}
)

ProtectionTypeDef = TypedDict(
    "ProtectionTypeDef",
    {"Id": str, "Name": str, "ResourceArn": str, "HealthCheckIds": List[str]},
    total=False,
)

SubResourceSummaryTypeDef = TypedDict(
    "SubResourceSummaryTypeDef",
    {
        "Type": Literal["IP", "URL"],
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
    "_RequiredSubscriptionTypeDef", {"SubscriptionLimits": "SubscriptionLimitsTypeDef"}
)
_OptionalSubscriptionTypeDef = TypedDict(
    "_OptionalSubscriptionTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "TimeCommitmentInSeconds": int,
        "AutoRenew": Literal["ENABLED", "DISABLED"],
        "Limits": List["LimitTypeDef"],
        "ProactiveEngagementStatus": Literal["ENABLED", "DISABLED", "PENDING"],
    },
    total=False,
)


class SubscriptionTypeDef(_RequiredSubscriptionTypeDef, _OptionalSubscriptionTypeDef):
    pass


_RequiredSummarizedAttackVectorTypeDef = TypedDict(
    "_RequiredSummarizedAttackVectorTypeDef", {"VectorType": str}
)
_OptionalSummarizedAttackVectorTypeDef = TypedDict(
    "_OptionalSummarizedAttackVectorTypeDef",
    {"VectorCounters": List["SummarizedCounterTypeDef"]},
    total=False,
)


class SummarizedAttackVectorTypeDef(
    _RequiredSummarizedAttackVectorTypeDef, _OptionalSummarizedAttackVectorTypeDef
):
    pass


SummarizedCounterTypeDef = TypedDict(
    "SummarizedCounterTypeDef",
    {"Name": str, "Max": float, "Average": float, "Sum": float, "N": int, "Unit": str},
    total=False,
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef", {"FromInclusive": datetime, "ToExclusive": datetime}, total=False
)

CreateProtectionResponseTypeDef = TypedDict(
    "CreateProtectionResponseTypeDef", {"ProtectionId": str}, total=False
)

DescribeAttackResponseTypeDef = TypedDict(
    "DescribeAttackResponseTypeDef", {"Attack": "AttackDetailTypeDef"}, total=False
)

DescribeAttackStatisticsResponseTypeDef = TypedDict(
    "DescribeAttackStatisticsResponseTypeDef",
    {"TimeRange": "TimeRangeTypeDef", "DataItems": List["AttackStatisticsDataItemTypeDef"]},
)

DescribeDRTAccessResponseTypeDef = TypedDict(
    "DescribeDRTAccessResponseTypeDef", {"RoleArn": str, "LogBucketList": List[str]}, total=False
)

DescribeEmergencyContactSettingsResponseTypeDef = TypedDict(
    "DescribeEmergencyContactSettingsResponseTypeDef",
    {"EmergencyContactList": List["EmergencyContactTypeDef"]},
    total=False,
)

DescribeProtectionGroupResponseTypeDef = TypedDict(
    "DescribeProtectionGroupResponseTypeDef", {"ProtectionGroup": "ProtectionGroupTypeDef"}
)

DescribeProtectionResponseTypeDef = TypedDict(
    "DescribeProtectionResponseTypeDef", {"Protection": "ProtectionTypeDef"}, total=False
)

DescribeSubscriptionResponseTypeDef = TypedDict(
    "DescribeSubscriptionResponseTypeDef", {"Subscription": "SubscriptionTypeDef"}, total=False
)

GetSubscriptionStateResponseTypeDef = TypedDict(
    "GetSubscriptionStateResponseTypeDef", {"SubscriptionState": Literal["ACTIVE", "INACTIVE"]}
)

ListAttacksResponseTypeDef = TypedDict(
    "ListAttacksResponseTypeDef",
    {"AttackSummaries": List["AttackSummaryTypeDef"], "NextToken": str},
    total=False,
)

_RequiredListProtectionGroupsResponseTypeDef = TypedDict(
    "_RequiredListProtectionGroupsResponseTypeDef",
    {"ProtectionGroups": List["ProtectionGroupTypeDef"]},
)
_OptionalListProtectionGroupsResponseTypeDef = TypedDict(
    "_OptionalListProtectionGroupsResponseTypeDef", {"NextToken": str}, total=False
)


class ListProtectionGroupsResponseTypeDef(
    _RequiredListProtectionGroupsResponseTypeDef, _OptionalListProtectionGroupsResponseTypeDef
):
    pass


ListProtectionsResponseTypeDef = TypedDict(
    "ListProtectionsResponseTypeDef",
    {"Protections": List["ProtectionTypeDef"], "NextToken": str},
    total=False,
)

_RequiredListResourcesInProtectionGroupResponseTypeDef = TypedDict(
    "_RequiredListResourcesInProtectionGroupResponseTypeDef", {"ResourceArns": List[str]}
)
_OptionalListResourcesInProtectionGroupResponseTypeDef = TypedDict(
    "_OptionalListResourcesInProtectionGroupResponseTypeDef", {"NextToken": str}, total=False
)


class ListResourcesInProtectionGroupResponseTypeDef(
    _RequiredListResourcesInProtectionGroupResponseTypeDef,
    _OptionalListResourcesInProtectionGroupResponseTypeDef,
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
