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
    "AttackSummaryTypeDef",
    "AttackVectorDescriptionTypeDef",
    "ContributorTypeDef",
    "EmergencyContactTypeDef",
    "LimitTypeDef",
    "MitigationTypeDef",
    "ProtectionTypeDef",
    "SubResourceSummaryTypeDef",
    "SubscriptionTypeDef",
    "SummarizedAttackVectorTypeDef",
    "SummarizedCounterTypeDef",
    "CreateProtectionResponseTypeDef",
    "DescribeAttackResponseTypeDef",
    "DescribeDRTAccessResponseTypeDef",
    "DescribeEmergencyContactSettingsResponseTypeDef",
    "DescribeProtectionResponseTypeDef",
    "DescribeSubscriptionResponseTypeDef",
    "GetSubscriptionStateResponseTypeDef",
    "ListAttacksResponseTypeDef",
    "ListProtectionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "TimeRangeTypeDef",
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

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
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

CreateProtectionResponseTypeDef = TypedDict(
    "CreateProtectionResponseTypeDef", {"ProtectionId": str}, total=False
)

DescribeAttackResponseTypeDef = TypedDict(
    "DescribeAttackResponseTypeDef", {"Attack": "AttackDetailTypeDef"}, total=False
)

DescribeDRTAccessResponseTypeDef = TypedDict(
    "DescribeDRTAccessResponseTypeDef", {"RoleArn": str, "LogBucketList": List[str]}, total=False
)

DescribeEmergencyContactSettingsResponseTypeDef = TypedDict(
    "DescribeEmergencyContactSettingsResponseTypeDef",
    {"EmergencyContactList": List["EmergencyContactTypeDef"]},
    total=False,
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

ListProtectionsResponseTypeDef = TypedDict(
    "ListProtectionsResponseTypeDef",
    {"Protections": List["ProtectionTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef", {"FromInclusive": datetime, "ToExclusive": datetime}, total=False
)
