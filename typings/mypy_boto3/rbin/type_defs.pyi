"""
Type annotations for rbin service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_rbin.type_defs import ResourceTagTypeDef

    data: ResourceTagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import LockStateType, ResourceTypeType, RuleStatusType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "CreateRuleRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "DeleteRuleRequestTypeDef",
    "GetRuleRequestTypeDef",
    "GetRuleResponseTypeDef",
    "ListRulesRequestPaginateTypeDef",
    "ListRulesRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LockConfigurationTypeDef",
    "LockRuleRequestTypeDef",
    "LockRuleResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "RetentionPeriodTypeDef",
    "RuleSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UnlockDelayTypeDef",
    "UnlockRuleRequestTypeDef",
    "UnlockRuleResponseTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateRuleRequestTypeDef",
    "UpdateRuleResponseTypeDef",
)

class ResourceTagTypeDef(TypedDict):
    ResourceTagKey: str
    ResourceTagValue: NotRequired[str]

class RetentionPeriodTypeDef(TypedDict):
    RetentionPeriodValue: int
    RetentionPeriodUnit: Literal["DAYS"]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteRuleRequestTypeDef(TypedDict):
    Identifier: str

class GetRuleRequestTypeDef(TypedDict):
    Identifier: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class UnlockDelayTypeDef(TypedDict):
    UnlockDelayValue: int
    UnlockDelayUnit: Literal["DAYS"]

class UnlockRuleRequestTypeDef(TypedDict):
    Identifier: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class ListRulesRequestTypeDef(TypedDict):
    ResourceType: ResourceTypeType
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]
    LockState: NotRequired[LockStateType]
    ExcludeResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class RuleSummaryTypeDef(TypedDict):
    Identifier: NotRequired[str]
    Description: NotRequired[str]
    RetentionPeriod: NotRequired[RetentionPeriodTypeDef]
    LockState: NotRequired[LockStateType]
    RuleArn: NotRequired[str]

class UpdateRuleRequestTypeDef(TypedDict):
    Identifier: str
    RetentionPeriod: NotRequired[RetentionPeriodTypeDef]
    Description: NotRequired[str]
    ResourceType: NotRequired[ResourceTypeType]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]
    ExcludeResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleResponseTypeDef(TypedDict):
    Identifier: str
    RetentionPeriod: RetentionPeriodTypeDef
    Description: str
    ResourceType: ResourceTypeType
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ExcludeResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesRequestPaginateTypeDef(TypedDict):
    ResourceType: ResourceTypeType
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]
    LockState: NotRequired[LockStateType]
    ExcludeResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class LockConfigurationTypeDef(TypedDict):
    UnlockDelay: UnlockDelayTypeDef

class ListRulesResponseTypeDef(TypedDict):
    Rules: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateRuleRequestTypeDef(TypedDict):
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceType: ResourceTypeType
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]
    LockConfiguration: NotRequired[LockConfigurationTypeDef]
    ExcludeResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class CreateRuleResponseTypeDef(TypedDict):
    Identifier: str
    RetentionPeriod: RetentionPeriodTypeDef
    Description: str
    Tags: List[TagTypeDef]
    ResourceType: ResourceTypeType
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockConfiguration: LockConfigurationTypeDef
    LockState: LockStateType
    RuleArn: str
    ExcludeResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleResponseTypeDef(TypedDict):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockConfiguration: LockConfigurationTypeDef
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ExcludeResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LockRuleRequestTypeDef(TypedDict):
    Identifier: str
    LockConfiguration: LockConfigurationTypeDef

class LockRuleResponseTypeDef(TypedDict):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockConfiguration: LockConfigurationTypeDef
    LockState: LockStateType
    RuleArn: str
    ExcludeResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UnlockRuleResponseTypeDef(TypedDict):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockConfiguration: LockConfigurationTypeDef
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ExcludeResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
