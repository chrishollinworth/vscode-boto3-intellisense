"""
Type annotations for rbin service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rbin/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rbin.type_defs import CreateRuleRequestRequestTypeDef

    data: CreateRuleRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import LockStateType, ResourceTypeType, RuleStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "GetRuleRequestRequestTypeDef",
    "GetRuleResponseTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LockConfigurationTypeDef",
    "LockRuleRequestRequestTypeDef",
    "LockRuleResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RuleSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UnlockDelayTypeDef",
    "UnlockRuleRequestRequestTypeDef",
    "UnlockRuleResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "UpdateRuleResponseTypeDef",
)

_RequiredCreateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestRequestTypeDef",
    {
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "ResourceType": ResourceTypeType,
    },
)
_OptionalCreateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ResourceTags": List["ResourceTagTypeDef"],
        "LockConfiguration": "LockConfigurationTypeDef",
    },
    total=False,
)

class CreateRuleRequestRequestTypeDef(
    _RequiredCreateRuleRequestRequestTypeDef, _OptionalCreateRuleRequestRequestTypeDef
):
    pass

CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ResourceType": ResourceTypeType,
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "LockConfiguration": "LockConfigurationTypeDef",
        "LockState": LockStateType,
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "LockConfiguration": "LockConfigurationTypeDef",
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRulesRequestRequestTypeDef = TypedDict(
    "_RequiredListRulesRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeType,
    },
)
_OptionalListRulesRequestRequestTypeDef = TypedDict(
    "_OptionalListRulesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ResourceTags": List["ResourceTagTypeDef"],
        "LockState": LockStateType,
    },
    total=False,
)

class ListRulesRequestRequestTypeDef(
    _RequiredListRulesRequestRequestTypeDef, _OptionalListRulesRequestRequestTypeDef
):
    pass

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "Rules": List["RuleSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LockConfigurationTypeDef = TypedDict(
    "LockConfigurationTypeDef",
    {
        "UnlockDelay": "UnlockDelayTypeDef",
    },
)

LockRuleRequestRequestTypeDef = TypedDict(
    "LockRuleRequestRequestTypeDef",
    {
        "Identifier": str,
        "LockConfiguration": "LockConfigurationTypeDef",
    },
)

LockRuleResponseTypeDef = TypedDict(
    "LockRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "LockConfiguration": "LockConfigurationTypeDef",
        "LockState": LockStateType,
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredResourceTagTypeDef = TypedDict(
    "_RequiredResourceTagTypeDef",
    {
        "ResourceTagKey": str,
    },
)
_OptionalResourceTagTypeDef = TypedDict(
    "_OptionalResourceTagTypeDef",
    {
        "ResourceTagValue": str,
    },
    total=False,
)

class ResourceTagTypeDef(_RequiredResourceTagTypeDef, _OptionalResourceTagTypeDef):
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

RetentionPeriodTypeDef = TypedDict(
    "RetentionPeriodTypeDef",
    {
        "RetentionPeriodValue": int,
        "RetentionPeriodUnit": Literal["DAYS"],
    },
)

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "LockState": LockStateType,
        "RuleArn": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UnlockDelayTypeDef = TypedDict(
    "UnlockDelayTypeDef",
    {
        "UnlockDelayValue": int,
        "UnlockDelayUnit": Literal["DAYS"],
    },
)

UnlockRuleRequestRequestTypeDef = TypedDict(
    "UnlockRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

UnlockRuleResponseTypeDef = TypedDict(
    "UnlockRuleResponseTypeDef",
    {
        "Identifier": str,
        "Description": str,
        "ResourceType": ResourceTypeType,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "LockConfiguration": "LockConfigurationTypeDef",
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleRequestRequestTypeDef",
    {
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "Description": str,
        "ResourceType": ResourceTypeType,
        "ResourceTags": List["ResourceTagTypeDef"],
    },
    total=False,
)

class UpdateRuleRequestRequestTypeDef(
    _RequiredUpdateRuleRequestRequestTypeDef, _OptionalUpdateRuleRequestRequestTypeDef
):
    pass

UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "Identifier": str,
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "Description": str,
        "ResourceType": ResourceTypeType,
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "LockState": LockStateType,
        "LockEndTime": datetime,
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
