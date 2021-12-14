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
from typing import Any, Dict, List

from .literals import RuleStatusType

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
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RuleSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "UpdateRuleResponseTypeDef",
)

_RequiredCreateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestRequestTypeDef",
    {
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "ResourceType": Literal["EBS_SNAPSHOT"],
    },
)
_OptionalCreateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "ResourceTags": List["ResourceTagTypeDef"],
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
        "ResourceType": Literal["EBS_SNAPSHOT"],
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
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
        "ResourceType": Literal["EBS_SNAPSHOT"],
        "RetentionPeriod": "RetentionPeriodTypeDef",
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRulesRequestRequestTypeDef = TypedDict(
    "_RequiredListRulesRequestRequestTypeDef",
    {
        "ResourceType": Literal["EBS_SNAPSHOT"],
    },
)
_OptionalListRulesRequestRequestTypeDef = TypedDict(
    "_OptionalListRulesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ResourceTags": List["ResourceTagTypeDef"],
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
        "ResourceType": Literal["EBS_SNAPSHOT"],
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
        "ResourceType": Literal["EBS_SNAPSHOT"],
        "ResourceTags": List["ResourceTagTypeDef"],
        "Status": RuleStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
