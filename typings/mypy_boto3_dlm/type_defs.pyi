"""
Type annotations for dlm service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dlm/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_dlm.type_defs import RetentionArchiveTierTypeDef

    data: RetentionArchiveTierTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    DefaultPoliciesTypeValuesType,
    DefaultPolicyTypeValuesType,
    GettablePolicyStateValuesType,
    LocationValuesType,
    PolicyLanguageValuesType,
    PolicyTypeValuesType,
    ResourceLocationValuesType,
    ResourceTypeValuesType,
    RetentionIntervalUnitValuesType,
    SettablePolicyStateValuesType,
    StageValuesType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "ArchiveRetainRuleTypeDef",
    "ArchiveRuleTypeDef",
    "CreateLifecyclePolicyRequestTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "CreateRuleOutputTypeDef",
    "CreateRuleTypeDef",
    "CrossRegionCopyActionTypeDef",
    "CrossRegionCopyDeprecateRuleTypeDef",
    "CrossRegionCopyRetainRuleTypeDef",
    "CrossRegionCopyRuleTypeDef",
    "CrossRegionCopyTargetTypeDef",
    "DeleteLifecyclePolicyRequestTypeDef",
    "DeprecateRuleTypeDef",
    "EncryptionConfigurationTypeDef",
    "EventParametersOutputTypeDef",
    "EventParametersTypeDef",
    "EventSourceOutputTypeDef",
    "EventSourceTypeDef",
    "ExclusionsOutputTypeDef",
    "ExclusionsTypeDef",
    "ExclusionsUnionTypeDef",
    "FastRestoreRuleOutputTypeDef",
    "FastRestoreRuleTypeDef",
    "GetLifecyclePoliciesRequestTypeDef",
    "GetLifecyclePoliciesResponseTypeDef",
    "GetLifecyclePolicyRequestTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParametersOutputTypeDef",
    "ParametersTypeDef",
    "PolicyDetailsOutputTypeDef",
    "PolicyDetailsTypeDef",
    "PolicyDetailsUnionTypeDef",
    "ResponseMetadataTypeDef",
    "RetainRuleTypeDef",
    "RetentionArchiveTierTypeDef",
    "ScheduleOutputTypeDef",
    "ScheduleTypeDef",
    "ScriptOutputTypeDef",
    "ScriptTypeDef",
    "ShareRuleOutputTypeDef",
    "ShareRuleTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLifecyclePolicyRequestTypeDef",
)

class RetentionArchiveTierTypeDef(TypedDict):
    Count: NotRequired[int]
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class CrossRegionCopyTargetTypeDef(TypedDict):
    TargetRegion: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ScriptOutputTypeDef(TypedDict):
    ExecutionHandler: str
    Stages: NotRequired[List[StageValuesType]]
    ExecutionHandlerService: NotRequired[Literal["AWS_SYSTEMS_MANAGER"]]
    ExecuteOperationOnScriptFailure: NotRequired[bool]
    ExecutionTimeout: NotRequired[int]
    MaximumRetryCount: NotRequired[int]

class ScriptTypeDef(TypedDict):
    ExecutionHandler: str
    Stages: NotRequired[Sequence[StageValuesType]]
    ExecutionHandlerService: NotRequired[Literal["AWS_SYSTEMS_MANAGER"]]
    ExecuteOperationOnScriptFailure: NotRequired[bool]
    ExecutionTimeout: NotRequired[int]
    MaximumRetryCount: NotRequired[int]

class CrossRegionCopyRetainRuleTypeDef(TypedDict):
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class EncryptionConfigurationTypeDef(TypedDict):
    Encrypted: bool
    CmkArn: NotRequired[str]

class CrossRegionCopyDeprecateRuleTypeDef(TypedDict):
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class DeleteLifecyclePolicyRequestTypeDef(TypedDict):
    PolicyId: str

class DeprecateRuleTypeDef(TypedDict):
    Count: NotRequired[int]
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class EventParametersOutputTypeDef(TypedDict):
    EventType: Literal["shareSnapshot"]
    SnapshotOwner: List[str]
    DescriptionRegex: str

class EventParametersTypeDef(TypedDict):
    EventType: Literal["shareSnapshot"]
    SnapshotOwner: Sequence[str]
    DescriptionRegex: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class FastRestoreRuleOutputTypeDef(TypedDict):
    AvailabilityZones: List[str]
    Count: NotRequired[int]
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class FastRestoreRuleTypeDef(TypedDict):
    AvailabilityZones: Sequence[str]
    Count: NotRequired[int]
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class GetLifecyclePoliciesRequestTypeDef(TypedDict):
    PolicyIds: NotRequired[Sequence[str]]
    State: NotRequired[GettablePolicyStateValuesType]
    ResourceTypes: NotRequired[Sequence[ResourceTypeValuesType]]
    TargetTags: NotRequired[Sequence[str]]
    TagsToAdd: NotRequired[Sequence[str]]
    DefaultPolicyType: NotRequired[DefaultPoliciesTypeValuesType]

class LifecyclePolicySummaryTypeDef(TypedDict):
    PolicyId: NotRequired[str]
    Description: NotRequired[str]
    State: NotRequired[GettablePolicyStateValuesType]
    Tags: NotRequired[Dict[str, str]]
    PolicyType: NotRequired[PolicyTypeValuesType]
    DefaultPolicy: NotRequired[bool]

class GetLifecyclePolicyRequestTypeDef(TypedDict):
    PolicyId: str

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class RetainRuleTypeDef(TypedDict):
    Count: NotRequired[int]
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class ShareRuleOutputTypeDef(TypedDict):
    TargetAccounts: List[str]
    UnshareInterval: NotRequired[int]
    UnshareIntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class ShareRuleTypeDef(TypedDict):
    TargetAccounts: Sequence[str]
    UnshareInterval: NotRequired[int]
    UnshareIntervalUnit: NotRequired[RetentionIntervalUnitValuesType]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class ArchiveRetainRuleTypeDef(TypedDict):
    RetentionArchiveTier: RetentionArchiveTierTypeDef

class CreateLifecyclePolicyResponseTypeDef(TypedDict):
    PolicyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleOutputTypeDef(TypedDict):
    Location: NotRequired[LocationValuesType]
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[Literal["HOURS"]]
    Times: NotRequired[List[str]]
    CronExpression: NotRequired[str]
    Scripts: NotRequired[List[ScriptOutputTypeDef]]

class CreateRuleTypeDef(TypedDict):
    Location: NotRequired[LocationValuesType]
    Interval: NotRequired[int]
    IntervalUnit: NotRequired[Literal["HOURS"]]
    Times: NotRequired[Sequence[str]]
    CronExpression: NotRequired[str]
    Scripts: NotRequired[Sequence[ScriptTypeDef]]

class CrossRegionCopyActionTypeDef(TypedDict):
    Target: str
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    RetainRule: NotRequired[CrossRegionCopyRetainRuleTypeDef]

class CrossRegionCopyRuleTypeDef(TypedDict):
    Encrypted: bool
    TargetRegion: NotRequired[str]
    Target: NotRequired[str]
    CmkArn: NotRequired[str]
    CopyTags: NotRequired[bool]
    RetainRule: NotRequired[CrossRegionCopyRetainRuleTypeDef]
    DeprecateRule: NotRequired[CrossRegionCopyDeprecateRuleTypeDef]

EventSourceOutputTypeDef = TypedDict(
    "EventSourceOutputTypeDef",
    {
        "Type": Literal["MANAGED_CWE"],
        "Parameters": NotRequired[EventParametersOutputTypeDef],
    },
)
EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Type": Literal["MANAGED_CWE"],
        "Parameters": NotRequired[EventParametersTypeDef],
    },
)

class ExclusionsOutputTypeDef(TypedDict):
    ExcludeBootVolumes: NotRequired[bool]
    ExcludeVolumeTypes: NotRequired[List[str]]
    ExcludeTags: NotRequired[List[TagTypeDef]]

class ExclusionsTypeDef(TypedDict):
    ExcludeBootVolumes: NotRequired[bool]
    ExcludeVolumeTypes: NotRequired[Sequence[str]]
    ExcludeTags: NotRequired[Sequence[TagTypeDef]]

class ParametersOutputTypeDef(TypedDict):
    ExcludeBootVolume: NotRequired[bool]
    NoReboot: NotRequired[bool]
    ExcludeDataVolumeTags: NotRequired[List[TagTypeDef]]

class ParametersTypeDef(TypedDict):
    ExcludeBootVolume: NotRequired[bool]
    NoReboot: NotRequired[bool]
    ExcludeDataVolumeTags: NotRequired[Sequence[TagTypeDef]]

class GetLifecyclePoliciesResponseTypeDef(TypedDict):
    Policies: List[LifecyclePolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ArchiveRuleTypeDef(TypedDict):
    RetainRule: ArchiveRetainRuleTypeDef

class ActionOutputTypeDef(TypedDict):
    Name: str
    CrossRegionCopy: List[CrossRegionCopyActionTypeDef]

class ActionTypeDef(TypedDict):
    Name: str
    CrossRegionCopy: Sequence[CrossRegionCopyActionTypeDef]

ExclusionsUnionTypeDef = Union[ExclusionsTypeDef, ExclusionsOutputTypeDef]

class ScheduleOutputTypeDef(TypedDict):
    Name: NotRequired[str]
    CopyTags: NotRequired[bool]
    TagsToAdd: NotRequired[List[TagTypeDef]]
    VariableTags: NotRequired[List[TagTypeDef]]
    CreateRule: NotRequired[CreateRuleOutputTypeDef]
    RetainRule: NotRequired[RetainRuleTypeDef]
    FastRestoreRule: NotRequired[FastRestoreRuleOutputTypeDef]
    CrossRegionCopyRules: NotRequired[List[CrossRegionCopyRuleTypeDef]]
    ShareRules: NotRequired[List[ShareRuleOutputTypeDef]]
    DeprecateRule: NotRequired[DeprecateRuleTypeDef]
    ArchiveRule: NotRequired[ArchiveRuleTypeDef]

class ScheduleTypeDef(TypedDict):
    Name: NotRequired[str]
    CopyTags: NotRequired[bool]
    TagsToAdd: NotRequired[Sequence[TagTypeDef]]
    VariableTags: NotRequired[Sequence[TagTypeDef]]
    CreateRule: NotRequired[CreateRuleTypeDef]
    RetainRule: NotRequired[RetainRuleTypeDef]
    FastRestoreRule: NotRequired[FastRestoreRuleTypeDef]
    CrossRegionCopyRules: NotRequired[Sequence[CrossRegionCopyRuleTypeDef]]
    ShareRules: NotRequired[Sequence[ShareRuleTypeDef]]
    DeprecateRule: NotRequired[DeprecateRuleTypeDef]
    ArchiveRule: NotRequired[ArchiveRuleTypeDef]

class PolicyDetailsOutputTypeDef(TypedDict):
    PolicyType: NotRequired[PolicyTypeValuesType]
    ResourceTypes: NotRequired[List[ResourceTypeValuesType]]
    ResourceLocations: NotRequired[List[ResourceLocationValuesType]]
    TargetTags: NotRequired[List[TagTypeDef]]
    Schedules: NotRequired[List[ScheduleOutputTypeDef]]
    Parameters: NotRequired[ParametersOutputTypeDef]
    EventSource: NotRequired[EventSourceOutputTypeDef]
    Actions: NotRequired[List[ActionOutputTypeDef]]
    PolicyLanguage: NotRequired[PolicyLanguageValuesType]
    ResourceType: NotRequired[ResourceTypeValuesType]
    CreateInterval: NotRequired[int]
    RetainInterval: NotRequired[int]
    CopyTags: NotRequired[bool]
    CrossRegionCopyTargets: NotRequired[List[CrossRegionCopyTargetTypeDef]]
    ExtendDeletion: NotRequired[bool]
    Exclusions: NotRequired[ExclusionsOutputTypeDef]

class PolicyDetailsTypeDef(TypedDict):
    PolicyType: NotRequired[PolicyTypeValuesType]
    ResourceTypes: NotRequired[Sequence[ResourceTypeValuesType]]
    ResourceLocations: NotRequired[Sequence[ResourceLocationValuesType]]
    TargetTags: NotRequired[Sequence[TagTypeDef]]
    Schedules: NotRequired[Sequence[ScheduleTypeDef]]
    Parameters: NotRequired[ParametersTypeDef]
    EventSource: NotRequired[EventSourceTypeDef]
    Actions: NotRequired[Sequence[ActionTypeDef]]
    PolicyLanguage: NotRequired[PolicyLanguageValuesType]
    ResourceType: NotRequired[ResourceTypeValuesType]
    CreateInterval: NotRequired[int]
    RetainInterval: NotRequired[int]
    CopyTags: NotRequired[bool]
    CrossRegionCopyTargets: NotRequired[Sequence[CrossRegionCopyTargetTypeDef]]
    ExtendDeletion: NotRequired[bool]
    Exclusions: NotRequired[ExclusionsTypeDef]

class LifecyclePolicyTypeDef(TypedDict):
    PolicyId: NotRequired[str]
    Description: NotRequired[str]
    State: NotRequired[GettablePolicyStateValuesType]
    StatusMessage: NotRequired[str]
    ExecutionRoleArn: NotRequired[str]
    DateCreated: NotRequired[datetime]
    DateModified: NotRequired[datetime]
    PolicyDetails: NotRequired[PolicyDetailsOutputTypeDef]
    Tags: NotRequired[Dict[str, str]]
    PolicyArn: NotRequired[str]
    DefaultPolicy: NotRequired[bool]

PolicyDetailsUnionTypeDef = Union[PolicyDetailsTypeDef, PolicyDetailsOutputTypeDef]

class GetLifecyclePolicyResponseTypeDef(TypedDict):
    Policy: LifecyclePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLifecyclePolicyRequestTypeDef(TypedDict):
    ExecutionRoleArn: str
    Description: str
    State: SettablePolicyStateValuesType
    PolicyDetails: NotRequired[PolicyDetailsUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    DefaultPolicy: NotRequired[DefaultPolicyTypeValuesType]
    CreateInterval: NotRequired[int]
    RetainInterval: NotRequired[int]
    CopyTags: NotRequired[bool]
    ExtendDeletion: NotRequired[bool]
    CrossRegionCopyTargets: NotRequired[Sequence[CrossRegionCopyTargetTypeDef]]
    Exclusions: NotRequired[ExclusionsUnionTypeDef]

class UpdateLifecyclePolicyRequestTypeDef(TypedDict):
    PolicyId: str
    ExecutionRoleArn: NotRequired[str]
    State: NotRequired[SettablePolicyStateValuesType]
    Description: NotRequired[str]
    PolicyDetails: NotRequired[PolicyDetailsUnionTypeDef]
    CreateInterval: NotRequired[int]
    RetainInterval: NotRequired[int]
    CopyTags: NotRequired[bool]
    ExtendDeletion: NotRequired[bool]
    CrossRegionCopyTargets: NotRequired[Sequence[CrossRegionCopyTargetTypeDef]]
    Exclusions: NotRequired[ExclusionsUnionTypeDef]
