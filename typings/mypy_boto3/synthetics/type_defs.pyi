"""
Type annotations for synthetics service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_synthetics/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_synthetics.type_defs import S3EncryptionConfigTypeDef

    data: S3EncryptionConfigTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    BrowserTypeType,
    CanaryRunStateReasonCodeType,
    CanaryRunStateType,
    CanaryRunTestResultType,
    CanaryStateReasonCodeType,
    CanaryStateType,
    EncryptionModeType,
    ProvisionedResourceCleanupSettingType,
    RunTypeType,
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
    "ArtifactConfigInputTypeDef",
    "ArtifactConfigOutputTypeDef",
    "AssociateResourceRequestTypeDef",
    "BaseScreenshotOutputTypeDef",
    "BaseScreenshotTypeDef",
    "BaseScreenshotUnionTypeDef",
    "BlobTypeDef",
    "BrowserConfigTypeDef",
    "CanaryCodeInputTypeDef",
    "CanaryCodeOutputTypeDef",
    "CanaryDryRunConfigOutputTypeDef",
    "CanaryLastRunTypeDef",
    "CanaryRunConfigInputTypeDef",
    "CanaryRunConfigOutputTypeDef",
    "CanaryRunStatusTypeDef",
    "CanaryRunTimelineTypeDef",
    "CanaryRunTypeDef",
    "CanaryScheduleInputTypeDef",
    "CanaryScheduleOutputTypeDef",
    "CanaryStatusTypeDef",
    "CanaryTimelineTypeDef",
    "CanaryTypeDef",
    "CreateCanaryRequestTypeDef",
    "CreateCanaryResponseTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "DeleteCanaryRequestTypeDef",
    "DeleteGroupRequestTypeDef",
    "DependencyTypeDef",
    "DescribeCanariesLastRunRequestTypeDef",
    "DescribeCanariesLastRunResponseTypeDef",
    "DescribeCanariesRequestTypeDef",
    "DescribeCanariesResponseTypeDef",
    "DescribeRuntimeVersionsRequestTypeDef",
    "DescribeRuntimeVersionsResponseTypeDef",
    "DisassociateResourceRequestTypeDef",
    "DryRunConfigOutputTypeDef",
    "EngineConfigTypeDef",
    "GetCanaryRequestTypeDef",
    "GetCanaryResponseTypeDef",
    "GetCanaryRunsRequestTypeDef",
    "GetCanaryRunsResponseTypeDef",
    "GetGroupRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "ListAssociatedGroupsRequestTypeDef",
    "ListAssociatedGroupsResponseTypeDef",
    "ListGroupResourcesRequestTypeDef",
    "ListGroupResourcesResponseTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RetryConfigInputTypeDef",
    "RetryConfigOutputTypeDef",
    "RuntimeVersionTypeDef",
    "S3EncryptionConfigTypeDef",
    "StartCanaryDryRunRequestTypeDef",
    "StartCanaryDryRunResponseTypeDef",
    "StartCanaryRequestTypeDef",
    "StopCanaryRequestTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCanaryRequestTypeDef",
    "VisualReferenceInputTypeDef",
    "VisualReferenceOutputTypeDef",
    "VpcConfigInputTypeDef",
    "VpcConfigOutputTypeDef",
)

class S3EncryptionConfigTypeDef(TypedDict):
    EncryptionMode: NotRequired[EncryptionModeType]
    KmsKeyArn: NotRequired[str]

class AssociateResourceRequestTypeDef(TypedDict):
    GroupIdentifier: str
    ResourceArn: str

class BaseScreenshotOutputTypeDef(TypedDict):
    ScreenshotName: str
    IgnoreCoordinates: NotRequired[List[str]]

class BaseScreenshotTypeDef(TypedDict):
    ScreenshotName: str
    IgnoreCoordinates: NotRequired[Sequence[str]]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BrowserConfigTypeDef(TypedDict):
    BrowserType: NotRequired[BrowserTypeType]

DependencyTypeDef = TypedDict(
    "DependencyTypeDef",
    {
        "Reference": str,
        "Type": NotRequired[Literal["LambdaLayer"]],
    },
)

class CanaryDryRunConfigOutputTypeDef(TypedDict):
    DryRunId: NotRequired[str]

class CanaryRunConfigInputTypeDef(TypedDict):
    TimeoutInSeconds: NotRequired[int]
    MemoryInMB: NotRequired[int]
    ActiveTracing: NotRequired[bool]
    EnvironmentVariables: NotRequired[Mapping[str, str]]
    EphemeralStorage: NotRequired[int]

class CanaryRunConfigOutputTypeDef(TypedDict):
    TimeoutInSeconds: NotRequired[int]
    MemoryInMB: NotRequired[int]
    ActiveTracing: NotRequired[bool]
    EphemeralStorage: NotRequired[int]

class CanaryRunStatusTypeDef(TypedDict):
    State: NotRequired[CanaryRunStateType]
    StateReason: NotRequired[str]
    StateReasonCode: NotRequired[CanaryRunStateReasonCodeType]
    TestResult: NotRequired[CanaryRunTestResultType]

class CanaryRunTimelineTypeDef(TypedDict):
    Started: NotRequired[datetime]
    Completed: NotRequired[datetime]
    MetricTimestampForRunAndRetries: NotRequired[datetime]

class RetryConfigInputTypeDef(TypedDict):
    MaxRetries: int

class RetryConfigOutputTypeDef(TypedDict):
    MaxRetries: NotRequired[int]

class CanaryStatusTypeDef(TypedDict):
    State: NotRequired[CanaryStateType]
    StateReason: NotRequired[str]
    StateReasonCode: NotRequired[CanaryStateReasonCodeType]

class CanaryTimelineTypeDef(TypedDict):
    Created: NotRequired[datetime]
    LastModified: NotRequired[datetime]
    LastStarted: NotRequired[datetime]
    LastStopped: NotRequired[datetime]

class DryRunConfigOutputTypeDef(TypedDict):
    DryRunId: NotRequired[str]
    LastDryRunExecutionStatus: NotRequired[str]

class EngineConfigTypeDef(TypedDict):
    EngineArn: NotRequired[str]
    BrowserType: NotRequired[BrowserTypeType]

class VpcConfigOutputTypeDef(TypedDict):
    VpcId: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    SecurityGroupIds: NotRequired[List[str]]
    Ipv6AllowedForDualStack: NotRequired[bool]

class VpcConfigInputTypeDef(TypedDict):
    SubnetIds: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]
    Ipv6AllowedForDualStack: NotRequired[bool]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateGroupRequestTypeDef(TypedDict):
    Name: str
    Tags: NotRequired[Mapping[str, str]]

class GroupTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    CreatedTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]

class DeleteCanaryRequestTypeDef(TypedDict):
    Name: str
    DeleteLambda: NotRequired[bool]

class DeleteGroupRequestTypeDef(TypedDict):
    GroupIdentifier: str

class DescribeCanariesLastRunRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Names: NotRequired[Sequence[str]]
    BrowserType: NotRequired[BrowserTypeType]

class DescribeCanariesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Names: NotRequired[Sequence[str]]

class DescribeRuntimeVersionsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RuntimeVersionTypeDef(TypedDict):
    VersionName: NotRequired[str]
    Description: NotRequired[str]
    ReleaseDate: NotRequired[datetime]
    DeprecationDate: NotRequired[datetime]

class DisassociateResourceRequestTypeDef(TypedDict):
    GroupIdentifier: str
    ResourceArn: str

class GetCanaryRequestTypeDef(TypedDict):
    Name: str
    DryRunId: NotRequired[str]

class GetCanaryRunsRequestTypeDef(TypedDict):
    Name: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    DryRunId: NotRequired[str]
    RunType: NotRequired[RunTypeType]

class GetGroupRequestTypeDef(TypedDict):
    GroupIdentifier: str

class GroupSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Arn: NotRequired[str]

class ListAssociatedGroupsRequestTypeDef(TypedDict):
    ResourceArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListGroupResourcesRequestTypeDef(TypedDict):
    GroupIdentifier: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListGroupsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class StartCanaryRequestTypeDef(TypedDict):
    Name: str

class StopCanaryRequestTypeDef(TypedDict):
    Name: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class ArtifactConfigInputTypeDef(TypedDict):
    S3Encryption: NotRequired[S3EncryptionConfigTypeDef]

class ArtifactConfigOutputTypeDef(TypedDict):
    S3Encryption: NotRequired[S3EncryptionConfigTypeDef]

class VisualReferenceOutputTypeDef(TypedDict):
    BaseScreenshots: NotRequired[List[BaseScreenshotOutputTypeDef]]
    BaseCanaryRunId: NotRequired[str]
    BrowserType: NotRequired[BrowserTypeType]

BaseScreenshotUnionTypeDef = Union[BaseScreenshotTypeDef, BaseScreenshotOutputTypeDef]

class CanaryCodeInputTypeDef(TypedDict):
    S3Bucket: NotRequired[str]
    S3Key: NotRequired[str]
    S3Version: NotRequired[str]
    ZipFile: NotRequired[BlobTypeDef]
    Handler: NotRequired[str]
    BlueprintTypes: NotRequired[Sequence[str]]
    Dependencies: NotRequired[Sequence[DependencyTypeDef]]

class CanaryCodeOutputTypeDef(TypedDict):
    SourceLocationArn: NotRequired[str]
    Handler: NotRequired[str]
    BlueprintTypes: NotRequired[List[str]]
    Dependencies: NotRequired[List[DependencyTypeDef]]

class CanaryRunTypeDef(TypedDict):
    Id: NotRequired[str]
    ScheduledRunId: NotRequired[str]
    RetryAttempt: NotRequired[int]
    Name: NotRequired[str]
    Status: NotRequired[CanaryRunStatusTypeDef]
    Timeline: NotRequired[CanaryRunTimelineTypeDef]
    ArtifactS3Location: NotRequired[str]
    DryRunConfig: NotRequired[CanaryDryRunConfigOutputTypeDef]
    BrowserType: NotRequired[BrowserTypeType]

class CanaryScheduleInputTypeDef(TypedDict):
    Expression: str
    DurationInSeconds: NotRequired[int]
    RetryConfig: NotRequired[RetryConfigInputTypeDef]

class CanaryScheduleOutputTypeDef(TypedDict):
    Expression: NotRequired[str]
    DurationInSeconds: NotRequired[int]
    RetryConfig: NotRequired[RetryConfigOutputTypeDef]

class ListGroupResourcesResponseTypeDef(TypedDict):
    Resources: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartCanaryDryRunResponseTypeDef(TypedDict):
    DryRunConfig: DryRunConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(TypedDict):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(TypedDict):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRuntimeVersionsResponseTypeDef(TypedDict):
    RuntimeVersions: List[RuntimeVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListAssociatedGroupsResponseTypeDef(TypedDict):
    Groups: List[GroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGroupsResponseTypeDef(TypedDict):
    Groups: List[GroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class VisualReferenceInputTypeDef(TypedDict):
    BaseCanaryRunId: str
    BaseScreenshots: NotRequired[Sequence[BaseScreenshotUnionTypeDef]]
    BrowserType: NotRequired[BrowserTypeType]

class CanaryLastRunTypeDef(TypedDict):
    CanaryName: NotRequired[str]
    LastRun: NotRequired[CanaryRunTypeDef]

class GetCanaryRunsResponseTypeDef(TypedDict):
    CanaryRuns: List[CanaryRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateCanaryRequestTypeDef(TypedDict):
    Name: str
    Code: CanaryCodeInputTypeDef
    ArtifactS3Location: str
    ExecutionRoleArn: str
    Schedule: CanaryScheduleInputTypeDef
    RuntimeVersion: str
    RunConfig: NotRequired[CanaryRunConfigInputTypeDef]
    SuccessRetentionPeriodInDays: NotRequired[int]
    FailureRetentionPeriodInDays: NotRequired[int]
    VpcConfig: NotRequired[VpcConfigInputTypeDef]
    ResourcesToReplicateTags: NotRequired[Sequence[Literal["lambda-function"]]]
    ProvisionedResourceCleanup: NotRequired[ProvisionedResourceCleanupSettingType]
    BrowserConfigs: NotRequired[Sequence[BrowserConfigTypeDef]]
    Tags: NotRequired[Mapping[str, str]]
    ArtifactConfig: NotRequired[ArtifactConfigInputTypeDef]

class CanaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Name: NotRequired[str]
    Code: NotRequired[CanaryCodeOutputTypeDef]
    ExecutionRoleArn: NotRequired[str]
    Schedule: NotRequired[CanaryScheduleOutputTypeDef]
    RunConfig: NotRequired[CanaryRunConfigOutputTypeDef]
    SuccessRetentionPeriodInDays: NotRequired[int]
    FailureRetentionPeriodInDays: NotRequired[int]
    Status: NotRequired[CanaryStatusTypeDef]
    Timeline: NotRequired[CanaryTimelineTypeDef]
    ArtifactS3Location: NotRequired[str]
    EngineArn: NotRequired[str]
    RuntimeVersion: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigOutputTypeDef]
    VisualReference: NotRequired[VisualReferenceOutputTypeDef]
    ProvisionedResourceCleanup: NotRequired[ProvisionedResourceCleanupSettingType]
    BrowserConfigs: NotRequired[List[BrowserConfigTypeDef]]
    EngineConfigs: NotRequired[List[EngineConfigTypeDef]]
    VisualReferences: NotRequired[List[VisualReferenceOutputTypeDef]]
    Tags: NotRequired[Dict[str, str]]
    ArtifactConfig: NotRequired[ArtifactConfigOutputTypeDef]
    DryRunConfig: NotRequired[DryRunConfigOutputTypeDef]

class StartCanaryDryRunRequestTypeDef(TypedDict):
    Name: str
    Code: NotRequired[CanaryCodeInputTypeDef]
    RuntimeVersion: NotRequired[str]
    RunConfig: NotRequired[CanaryRunConfigInputTypeDef]
    VpcConfig: NotRequired[VpcConfigInputTypeDef]
    ExecutionRoleArn: NotRequired[str]
    SuccessRetentionPeriodInDays: NotRequired[int]
    FailureRetentionPeriodInDays: NotRequired[int]
    VisualReference: NotRequired[VisualReferenceInputTypeDef]
    ArtifactS3Location: NotRequired[str]
    ArtifactConfig: NotRequired[ArtifactConfigInputTypeDef]
    ProvisionedResourceCleanup: NotRequired[ProvisionedResourceCleanupSettingType]
    BrowserConfigs: NotRequired[Sequence[BrowserConfigTypeDef]]
    VisualReferences: NotRequired[Sequence[VisualReferenceInputTypeDef]]

class UpdateCanaryRequestTypeDef(TypedDict):
    Name: str
    Code: NotRequired[CanaryCodeInputTypeDef]
    ExecutionRoleArn: NotRequired[str]
    RuntimeVersion: NotRequired[str]
    Schedule: NotRequired[CanaryScheduleInputTypeDef]
    RunConfig: NotRequired[CanaryRunConfigInputTypeDef]
    SuccessRetentionPeriodInDays: NotRequired[int]
    FailureRetentionPeriodInDays: NotRequired[int]
    VpcConfig: NotRequired[VpcConfigInputTypeDef]
    VisualReference: NotRequired[VisualReferenceInputTypeDef]
    ArtifactS3Location: NotRequired[str]
    ArtifactConfig: NotRequired[ArtifactConfigInputTypeDef]
    ProvisionedResourceCleanup: NotRequired[ProvisionedResourceCleanupSettingType]
    DryRunId: NotRequired[str]
    VisualReferences: NotRequired[Sequence[VisualReferenceInputTypeDef]]
    BrowserConfigs: NotRequired[Sequence[BrowserConfigTypeDef]]

class DescribeCanariesLastRunResponseTypeDef(TypedDict):
    CanariesLastRun: List[CanaryLastRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateCanaryResponseTypeDef(TypedDict):
    Canary: CanaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCanariesResponseTypeDef(TypedDict):
    Canaries: List[CanaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetCanaryResponseTypeDef(TypedDict):
    Canary: CanaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
