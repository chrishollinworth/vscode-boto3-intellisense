"""
Main interface for dlm service type definitions.

Usage::

    ```python
    from mypy_boto3_dlm.type_defs import CreateRuleTypeDef

    data: CreateRuleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateRuleTypeDef",
    "CrossRegionCopyRetainRuleTypeDef",
    "CrossRegionCopyRuleTypeDef",
    "FastRestoreRuleTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "LifecyclePolicyTypeDef",
    "ParametersTypeDef",
    "PolicyDetailsTypeDef",
    "RetainRuleTypeDef",
    "ScheduleTypeDef",
    "TagTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "GetLifecyclePoliciesResponseTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
)

CreateRuleTypeDef = TypedDict(
    "CreateRuleTypeDef",
    {"Interval": int, "IntervalUnit": Literal["HOURS"], "Times": List[str], "CronExpression": str},
    total=False,
)

CrossRegionCopyRetainRuleTypeDef = TypedDict(
    "CrossRegionCopyRetainRuleTypeDef",
    {"Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)

_RequiredCrossRegionCopyRuleTypeDef = TypedDict(
    "_RequiredCrossRegionCopyRuleTypeDef", {"TargetRegion": str, "Encrypted": bool}
)
_OptionalCrossRegionCopyRuleTypeDef = TypedDict(
    "_OptionalCrossRegionCopyRuleTypeDef",
    {"CmkArn": str, "CopyTags": bool, "RetainRule": "CrossRegionCopyRetainRuleTypeDef"},
    total=False,
)


class CrossRegionCopyRuleTypeDef(
    _RequiredCrossRegionCopyRuleTypeDef, _OptionalCrossRegionCopyRuleTypeDef
):
    pass


_RequiredFastRestoreRuleTypeDef = TypedDict(
    "_RequiredFastRestoreRuleTypeDef", {"AvailabilityZones": List[str]}
)
_OptionalFastRestoreRuleTypeDef = TypedDict(
    "_OptionalFastRestoreRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)


class FastRestoreRuleTypeDef(_RequiredFastRestoreRuleTypeDef, _OptionalFastRestoreRuleTypeDef):
    pass


LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": Literal["ENABLED", "DISABLED", "ERROR"],
        "Tags": Dict[str, str],
        "PolicyType": Literal["EBS_SNAPSHOT_MANAGEMENT", "IMAGE_MANAGEMENT"],
    },
    total=False,
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "PolicyId": str,
        "Description": str,
        "State": Literal["ENABLED", "DISABLED", "ERROR"],
        "StatusMessage": str,
        "ExecutionRoleArn": str,
        "DateCreated": datetime,
        "DateModified": datetime,
        "PolicyDetails": "PolicyDetailsTypeDef",
        "Tags": Dict[str, str],
        "PolicyArn": str,
    },
    total=False,
)

ParametersTypeDef = TypedDict(
    "ParametersTypeDef", {"ExcludeBootVolume": bool, "NoReboot": bool}, total=False
)

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {
        "PolicyType": Literal["EBS_SNAPSHOT_MANAGEMENT", "IMAGE_MANAGEMENT"],
        "ResourceTypes": List[Literal["VOLUME", "INSTANCE"]],
        "TargetTags": List["TagTypeDef"],
        "Schedules": List["ScheduleTypeDef"],
        "Parameters": "ParametersTypeDef",
    },
    total=False,
)

RetainRuleTypeDef = TypedDict(
    "RetainRuleTypeDef",
    {"Count": int, "Interval": int, "IntervalUnit": Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]},
    total=False,
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "Name": str,
        "CopyTags": bool,
        "TagsToAdd": List["TagTypeDef"],
        "VariableTags": List["TagTypeDef"],
        "CreateRule": "CreateRuleTypeDef",
        "RetainRule": "RetainRuleTypeDef",
        "FastRestoreRule": "FastRestoreRuleTypeDef",
        "CrossRegionCopyRules": List["CrossRegionCopyRuleTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CreateLifecyclePolicyResponseTypeDef = TypedDict(
    "CreateLifecyclePolicyResponseTypeDef", {"PolicyId": str}, total=False
)

GetLifecyclePoliciesResponseTypeDef = TypedDict(
    "GetLifecyclePoliciesResponseTypeDef",
    {"Policies": List["LifecyclePolicySummaryTypeDef"]},
    total=False,
)

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef", {"Policy": "LifecyclePolicyTypeDef"}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)
