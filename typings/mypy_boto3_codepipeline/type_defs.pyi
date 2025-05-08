"""
Type annotations for codepipeline service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef

    data: AWSSessionCredentialsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActionCategoryType,
    ActionConfigurationPropertyTypeType,
    ActionExecutionStatusType,
    ActionOwnerType,
    ApprovalStatusType,
    ConditionExecutionStatusType,
    ConditionTypeType,
    ExecutionModeType,
    ExecutionTypeType,
    ExecutorTypeType,
    FailureTypeType,
    GitPullRequestEventTypeType,
    JobStatusType,
    PipelineExecutionStatusType,
    PipelineTypeType,
    ResultType,
    RetryTriggerType,
    RuleConfigurationPropertyTypeType,
    RuleExecutionStatusType,
    SourceRevisionTypeType,
    StageExecutionStatusType,
    StageRetryModeType,
    StageTransitionTypeType,
    StartTimeRangeType,
    TriggerTypeType,
    WebhookAuthenticationTypeType,
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
    "AWSSessionCredentialsTypeDef",
    "AcknowledgeJobInputTypeDef",
    "AcknowledgeJobOutputTypeDef",
    "AcknowledgeThirdPartyJobInputTypeDef",
    "AcknowledgeThirdPartyJobOutputTypeDef",
    "ActionConfigurationPropertyTypeDef",
    "ActionConfigurationTypeDef",
    "ActionContextTypeDef",
    "ActionDeclarationOutputTypeDef",
    "ActionDeclarationTypeDef",
    "ActionExecutionDetailTypeDef",
    "ActionExecutionFilterTypeDef",
    "ActionExecutionInputTypeDef",
    "ActionExecutionOutputTypeDef",
    "ActionExecutionResultTypeDef",
    "ActionExecutionTypeDef",
    "ActionRevisionOutputTypeDef",
    "ActionRevisionTypeDef",
    "ActionRevisionUnionTypeDef",
    "ActionStateTypeDef",
    "ActionTypeArtifactDetailsTypeDef",
    "ActionTypeDeclarationOutputTypeDef",
    "ActionTypeDeclarationTypeDef",
    "ActionTypeDeclarationUnionTypeDef",
    "ActionTypeExecutorOutputTypeDef",
    "ActionTypeExecutorTypeDef",
    "ActionTypeIdTypeDef",
    "ActionTypeIdentifierTypeDef",
    "ActionTypePermissionsOutputTypeDef",
    "ActionTypePermissionsTypeDef",
    "ActionTypePropertyTypeDef",
    "ActionTypeSettingsTypeDef",
    "ActionTypeTypeDef",
    "ActionTypeUrlsTypeDef",
    "ApprovalResultTypeDef",
    "ArtifactDetailTypeDef",
    "ArtifactDetailsTypeDef",
    "ArtifactLocationTypeDef",
    "ArtifactRevisionTypeDef",
    "ArtifactStoreTypeDef",
    "ArtifactTypeDef",
    "BeforeEntryConditionsOutputTypeDef",
    "BeforeEntryConditionsTypeDef",
    "BlockerDeclarationTypeDef",
    "ConditionExecutionTypeDef",
    "ConditionOutputTypeDef",
    "ConditionStateTypeDef",
    "ConditionTypeDef",
    "CreateCustomActionTypeInputTypeDef",
    "CreateCustomActionTypeOutputTypeDef",
    "CreatePipelineInputTypeDef",
    "CreatePipelineOutputTypeDef",
    "CurrentRevisionTypeDef",
    "DeleteCustomActionTypeInputTypeDef",
    "DeletePipelineInputTypeDef",
    "DeleteWebhookInputTypeDef",
    "DeregisterWebhookWithThirdPartyInputTypeDef",
    "DisableStageTransitionInputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableStageTransitionInputTypeDef",
    "EncryptionKeyTypeDef",
    "EnvironmentVariableTypeDef",
    "ErrorDetailsTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionTriggerTypeDef",
    "ExecutorConfigurationOutputTypeDef",
    "ExecutorConfigurationTypeDef",
    "FailureConditionsOutputTypeDef",
    "FailureConditionsTypeDef",
    "FailureDetailsTypeDef",
    "GetActionTypeInputTypeDef",
    "GetActionTypeOutputTypeDef",
    "GetJobDetailsInputTypeDef",
    "GetJobDetailsOutputTypeDef",
    "GetPipelineExecutionInputTypeDef",
    "GetPipelineExecutionOutputTypeDef",
    "GetPipelineInputTypeDef",
    "GetPipelineOutputTypeDef",
    "GetPipelineStateInputTypeDef",
    "GetPipelineStateOutputTypeDef",
    "GetThirdPartyJobDetailsInputTypeDef",
    "GetThirdPartyJobDetailsOutputTypeDef",
    "GitBranchFilterCriteriaOutputTypeDef",
    "GitBranchFilterCriteriaTypeDef",
    "GitConfigurationOutputTypeDef",
    "GitConfigurationTypeDef",
    "GitFilePathFilterCriteriaOutputTypeDef",
    "GitFilePathFilterCriteriaTypeDef",
    "GitPullRequestFilterOutputTypeDef",
    "GitPullRequestFilterTypeDef",
    "GitPushFilterOutputTypeDef",
    "GitPushFilterTypeDef",
    "GitTagFilterCriteriaOutputTypeDef",
    "GitTagFilterCriteriaTypeDef",
    "InputArtifactTypeDef",
    "JobDataTypeDef",
    "JobDetailsTypeDef",
    "JobTypeDef",
    "JobWorkerExecutorConfigurationOutputTypeDef",
    "JobWorkerExecutorConfigurationTypeDef",
    "LambdaExecutorConfigurationTypeDef",
    "LatestInPipelineExecutionFilterTypeDef",
    "ListActionExecutionsInputPaginateTypeDef",
    "ListActionExecutionsInputTypeDef",
    "ListActionExecutionsOutputTypeDef",
    "ListActionTypesInputPaginateTypeDef",
    "ListActionTypesInputTypeDef",
    "ListActionTypesOutputTypeDef",
    "ListPipelineExecutionsInputPaginateTypeDef",
    "ListPipelineExecutionsInputTypeDef",
    "ListPipelineExecutionsOutputTypeDef",
    "ListPipelinesInputPaginateTypeDef",
    "ListPipelinesInputTypeDef",
    "ListPipelinesOutputTypeDef",
    "ListRuleExecutionsInputPaginateTypeDef",
    "ListRuleExecutionsInputTypeDef",
    "ListRuleExecutionsOutputTypeDef",
    "ListRuleTypesInputTypeDef",
    "ListRuleTypesOutputTypeDef",
    "ListTagsForResourceInputPaginateTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWebhookItemTypeDef",
    "ListWebhooksInputPaginateTypeDef",
    "ListWebhooksInputTypeDef",
    "ListWebhooksOutputTypeDef",
    "OutputArtifactOutputTypeDef",
    "OutputArtifactTypeDef",
    "OverrideStageConditionInputTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineContextTypeDef",
    "PipelineDeclarationOutputTypeDef",
    "PipelineDeclarationTypeDef",
    "PipelineDeclarationUnionTypeDef",
    "PipelineExecutionFilterTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineMetadataTypeDef",
    "PipelineRollbackMetadataTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTriggerDeclarationOutputTypeDef",
    "PipelineTriggerDeclarationTypeDef",
    "PipelineVariableDeclarationTypeDef",
    "PipelineVariableTypeDef",
    "PollForJobsInputTypeDef",
    "PollForJobsOutputTypeDef",
    "PollForThirdPartyJobsInputTypeDef",
    "PollForThirdPartyJobsOutputTypeDef",
    "PutActionRevisionInputTypeDef",
    "PutActionRevisionOutputTypeDef",
    "PutApprovalResultInputTypeDef",
    "PutApprovalResultOutputTypeDef",
    "PutJobFailureResultInputTypeDef",
    "PutJobSuccessResultInputTypeDef",
    "PutThirdPartyJobFailureResultInputTypeDef",
    "PutThirdPartyJobSuccessResultInputTypeDef",
    "PutWebhookInputTypeDef",
    "PutWebhookOutputTypeDef",
    "RegisterWebhookWithThirdPartyInputTypeDef",
    "ResolvedPipelineVariableTypeDef",
    "ResponseMetadataTypeDef",
    "RetryConfigurationTypeDef",
    "RetryStageExecutionInputTypeDef",
    "RetryStageExecutionOutputTypeDef",
    "RetryStageMetadataTypeDef",
    "RollbackStageInputTypeDef",
    "RollbackStageOutputTypeDef",
    "RuleConfigurationPropertyTypeDef",
    "RuleDeclarationOutputTypeDef",
    "RuleDeclarationTypeDef",
    "RuleExecutionDetailTypeDef",
    "RuleExecutionFilterTypeDef",
    "RuleExecutionInputTypeDef",
    "RuleExecutionOutputTypeDef",
    "RuleExecutionResultTypeDef",
    "RuleExecutionTypeDef",
    "RuleRevisionTypeDef",
    "RuleStateTypeDef",
    "RuleTypeIdTypeDef",
    "RuleTypeSettingsTypeDef",
    "RuleTypeTypeDef",
    "S3ArtifactLocationTypeDef",
    "S3LocationTypeDef",
    "SourceRevisionOverrideTypeDef",
    "SourceRevisionTypeDef",
    "StageConditionStateTypeDef",
    "StageConditionsExecutionTypeDef",
    "StageContextTypeDef",
    "StageDeclarationOutputTypeDef",
    "StageDeclarationTypeDef",
    "StageExecutionTypeDef",
    "StageStateTypeDef",
    "StartPipelineExecutionInputTypeDef",
    "StartPipelineExecutionOutputTypeDef",
    "StopExecutionTriggerTypeDef",
    "StopPipelineExecutionInputTypeDef",
    "StopPipelineExecutionOutputTypeDef",
    "SucceededInStageFilterTypeDef",
    "SuccessConditionsOutputTypeDef",
    "SuccessConditionsTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "ThirdPartyJobDataTypeDef",
    "ThirdPartyJobDetailsTypeDef",
    "ThirdPartyJobTypeDef",
    "TimestampTypeDef",
    "TransitionStateTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateActionTypeInputTypeDef",
    "UpdatePipelineInputTypeDef",
    "UpdatePipelineOutputTypeDef",
    "WebhookAuthConfigurationTypeDef",
    "WebhookDefinitionOutputTypeDef",
    "WebhookDefinitionTypeDef",
    "WebhookDefinitionUnionTypeDef",
    "WebhookFilterRuleTypeDef",
)

class AWSSessionCredentialsTypeDef(TypedDict):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str

class AcknowledgeJobInputTypeDef(TypedDict):
    jobId: str
    nonce: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AcknowledgeThirdPartyJobInputTypeDef(TypedDict):
    jobId: str
    nonce: str
    clientToken: str

ActionConfigurationPropertyTypeDef = TypedDict(
    "ActionConfigurationPropertyTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": NotRequired[bool],
        "description": NotRequired[str],
        "type": NotRequired[ActionConfigurationPropertyTypeType],
    },
)

class ActionConfigurationTypeDef(TypedDict):
    configuration: NotRequired[Dict[str, str]]

class ActionContextTypeDef(TypedDict):
    name: NotRequired[str]
    actionExecutionId: NotRequired[str]

class ActionTypeIdTypeDef(TypedDict):
    category: ActionCategoryType
    owner: ActionOwnerType
    provider: str
    version: str

class EnvironmentVariableTypeDef(TypedDict):
    name: str
    value: str

class InputArtifactTypeDef(TypedDict):
    name: str

class OutputArtifactOutputTypeDef(TypedDict):
    name: str
    files: NotRequired[List[str]]

class OutputArtifactTypeDef(TypedDict):
    name: str
    files: NotRequired[Sequence[str]]

class LatestInPipelineExecutionFilterTypeDef(TypedDict):
    pipelineExecutionId: str
    startTimeRange: StartTimeRangeType

class ErrorDetailsTypeDef(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]

class ActionRevisionOutputTypeDef(TypedDict):
    revisionId: str
    revisionChangeId: str
    created: datetime

TimestampTypeDef = Union[datetime, str]

class ActionTypeArtifactDetailsTypeDef(TypedDict):
    minimumCount: int
    maximumCount: int

class ActionTypeIdentifierTypeDef(TypedDict):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str

class ActionTypePermissionsOutputTypeDef(TypedDict):
    allowedAccounts: List[str]

class ActionTypePropertyTypeDef(TypedDict):
    name: str
    optional: bool
    key: bool
    noEcho: bool
    queryable: NotRequired[bool]
    description: NotRequired[str]

class ActionTypeUrlsTypeDef(TypedDict):
    configurationUrl: NotRequired[str]
    entityUrlTemplate: NotRequired[str]
    executionUrlTemplate: NotRequired[str]
    revisionUrlTemplate: NotRequired[str]

class ActionTypePermissionsTypeDef(TypedDict):
    allowedAccounts: Sequence[str]

class ActionTypeSettingsTypeDef(TypedDict):
    thirdPartyConfigurationUrl: NotRequired[str]
    entityUrlTemplate: NotRequired[str]
    executionUrlTemplate: NotRequired[str]
    revisionUrlTemplate: NotRequired[str]

class ArtifactDetailsTypeDef(TypedDict):
    minimumCount: int
    maximumCount: int

class ApprovalResultTypeDef(TypedDict):
    summary: str
    status: ApprovalStatusType

class S3LocationTypeDef(TypedDict):
    bucket: NotRequired[str]
    key: NotRequired[str]

class S3ArtifactLocationTypeDef(TypedDict):
    bucketName: str
    objectKey: str

class ArtifactRevisionTypeDef(TypedDict):
    name: NotRequired[str]
    revisionId: NotRequired[str]
    revisionChangeIdentifier: NotRequired[str]
    revisionSummary: NotRequired[str]
    created: NotRequired[datetime]
    revisionUrl: NotRequired[str]

EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "id": str,
        "type": Literal["KMS"],
    },
)
BlockerDeclarationTypeDef = TypedDict(
    "BlockerDeclarationTypeDef",
    {
        "name": str,
        "type": Literal["Schedule"],
    },
)

class ConditionExecutionTypeDef(TypedDict):
    status: NotRequired[ConditionExecutionStatusType]
    summary: NotRequired[str]
    lastStatusChange: NotRequired[datetime]

class TagTypeDef(TypedDict):
    key: str
    value: str

class DeleteCustomActionTypeInputTypeDef(TypedDict):
    category: ActionCategoryType
    provider: str
    version: str

class DeletePipelineInputTypeDef(TypedDict):
    name: str

class DeleteWebhookInputTypeDef(TypedDict):
    name: str

class DeregisterWebhookWithThirdPartyInputTypeDef(TypedDict):
    webhookName: NotRequired[str]

class DisableStageTransitionInputTypeDef(TypedDict):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType
    reason: str

class EnableStageTransitionInputTypeDef(TypedDict):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType

class ExecutionDetailsTypeDef(TypedDict):
    summary: NotRequired[str]
    externalExecutionId: NotRequired[str]
    percentComplete: NotRequired[int]

class ExecutionTriggerTypeDef(TypedDict):
    triggerType: NotRequired[TriggerTypeType]
    triggerDetail: NotRequired[str]

class JobWorkerExecutorConfigurationOutputTypeDef(TypedDict):
    pollingAccounts: NotRequired[List[str]]
    pollingServicePrincipals: NotRequired[List[str]]

class LambdaExecutorConfigurationTypeDef(TypedDict):
    lambdaFunctionArn: str

class JobWorkerExecutorConfigurationTypeDef(TypedDict):
    pollingAccounts: NotRequired[Sequence[str]]
    pollingServicePrincipals: NotRequired[Sequence[str]]

class RetryConfigurationTypeDef(TypedDict):
    retryMode: NotRequired[StageRetryModeType]

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "type": FailureTypeType,
        "message": str,
        "externalExecutionId": NotRequired[str],
    },
)

class GetActionTypeInputTypeDef(TypedDict):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str

class GetJobDetailsInputTypeDef(TypedDict):
    jobId: str

class GetPipelineExecutionInputTypeDef(TypedDict):
    pipelineName: str
    pipelineExecutionId: str

class GetPipelineInputTypeDef(TypedDict):
    name: str
    version: NotRequired[int]

class PipelineMetadataTypeDef(TypedDict):
    pipelineArn: NotRequired[str]
    created: NotRequired[datetime]
    updated: NotRequired[datetime]
    pollingDisabledAt: NotRequired[datetime]

class GetPipelineStateInputTypeDef(TypedDict):
    name: str

class GetThirdPartyJobDetailsInputTypeDef(TypedDict):
    jobId: str
    clientToken: str

class GitBranchFilterCriteriaOutputTypeDef(TypedDict):
    includes: NotRequired[List[str]]
    excludes: NotRequired[List[str]]

class GitBranchFilterCriteriaTypeDef(TypedDict):
    includes: NotRequired[Sequence[str]]
    excludes: NotRequired[Sequence[str]]

class GitFilePathFilterCriteriaOutputTypeDef(TypedDict):
    includes: NotRequired[List[str]]
    excludes: NotRequired[List[str]]

class GitFilePathFilterCriteriaTypeDef(TypedDict):
    includes: NotRequired[Sequence[str]]
    excludes: NotRequired[Sequence[str]]

class GitTagFilterCriteriaOutputTypeDef(TypedDict):
    includes: NotRequired[List[str]]
    excludes: NotRequired[List[str]]

class GitTagFilterCriteriaTypeDef(TypedDict):
    includes: NotRequired[Sequence[str]]
    excludes: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListActionTypesInputTypeDef(TypedDict):
    actionOwnerFilter: NotRequired[ActionOwnerType]
    nextToken: NotRequired[str]
    regionFilter: NotRequired[str]

class ListPipelinesInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PipelineSummaryTypeDef(TypedDict):
    name: NotRequired[str]
    version: NotRequired[int]
    pipelineType: NotRequired[PipelineTypeType]
    executionMode: NotRequired[ExecutionModeType]
    created: NotRequired[datetime]
    updated: NotRequired[datetime]

class ListRuleTypesInputTypeDef(TypedDict):
    ruleOwnerFilter: NotRequired[Literal["AWS"]]
    regionFilter: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListWebhooksInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class OverrideStageConditionInputTypeDef(TypedDict):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    conditionType: ConditionTypeType

class StageContextTypeDef(TypedDict):
    name: NotRequired[str]

class PipelineVariableDeclarationTypeDef(TypedDict):
    name: str
    defaultValue: NotRequired[str]
    description: NotRequired[str]

class SucceededInStageFilterTypeDef(TypedDict):
    stageName: NotRequired[str]

class PipelineRollbackMetadataTypeDef(TypedDict):
    rollbackTargetPipelineExecutionId: NotRequired[str]

class SourceRevisionTypeDef(TypedDict):
    actionName: str
    revisionId: NotRequired[str]
    revisionSummary: NotRequired[str]
    revisionUrl: NotRequired[str]

class StopExecutionTriggerTypeDef(TypedDict):
    reason: NotRequired[str]

class ResolvedPipelineVariableTypeDef(TypedDict):
    name: NotRequired[str]
    resolvedValue: NotRequired[str]

class PipelineVariableTypeDef(TypedDict):
    name: str
    value: str

class ThirdPartyJobTypeDef(TypedDict):
    clientId: NotRequired[str]
    jobId: NotRequired[str]

class RegisterWebhookWithThirdPartyInputTypeDef(TypedDict):
    webhookName: NotRequired[str]

class RetryStageExecutionInputTypeDef(TypedDict):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    retryMode: StageRetryModeType

class RetryStageMetadataTypeDef(TypedDict):
    autoStageRetryAttempt: NotRequired[int]
    manualStageRetryAttempt: NotRequired[int]
    latestRetryTrigger: NotRequired[RetryTriggerType]

class RollbackStageInputTypeDef(TypedDict):
    pipelineName: str
    stageName: str
    targetPipelineExecutionId: str

RuleConfigurationPropertyTypeDef = TypedDict(
    "RuleConfigurationPropertyTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
        "queryable": NotRequired[bool],
        "description": NotRequired[str],
        "type": NotRequired[RuleConfigurationPropertyTypeType],
    },
)

class RuleTypeIdTypeDef(TypedDict):
    category: Literal["Rule"]
    provider: str
    owner: NotRequired[Literal["AWS"]]
    version: NotRequired[str]

class RuleRevisionTypeDef(TypedDict):
    revisionId: str
    revisionChangeId: str
    created: datetime

class RuleTypeSettingsTypeDef(TypedDict):
    thirdPartyConfigurationUrl: NotRequired[str]
    entityUrlTemplate: NotRequired[str]
    executionUrlTemplate: NotRequired[str]
    revisionUrlTemplate: NotRequired[str]

class SourceRevisionOverrideTypeDef(TypedDict):
    actionName: str
    revisionType: SourceRevisionTypeType
    revisionValue: str

class StageConditionsExecutionTypeDef(TypedDict):
    status: NotRequired[ConditionExecutionStatusType]
    summary: NotRequired[str]

StageExecutionTypeDef = TypedDict(
    "StageExecutionTypeDef",
    {
        "pipelineExecutionId": str,
        "status": StageExecutionStatusType,
        "type": NotRequired[ExecutionTypeType],
    },
)

class TransitionStateTypeDef(TypedDict):
    enabled: NotRequired[bool]
    lastChangedBy: NotRequired[str]
    lastChangedAt: NotRequired[datetime]
    disabledReason: NotRequired[str]

class StopPipelineExecutionInputTypeDef(TypedDict):
    pipelineName: str
    pipelineExecutionId: str
    abandon: NotRequired[bool]
    reason: NotRequired[str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class WebhookAuthConfigurationTypeDef(TypedDict):
    AllowedIPRange: NotRequired[str]
    SecretToken: NotRequired[str]

class WebhookFilterRuleTypeDef(TypedDict):
    jsonPath: str
    matchEquals: NotRequired[str]

class AcknowledgeJobOutputTypeDef(TypedDict):
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class AcknowledgeThirdPartyJobOutputTypeDef(TypedDict):
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class PutActionRevisionOutputTypeDef(TypedDict):
    newRevision: bool
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutApprovalResultOutputTypeDef(TypedDict):
    approvedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RetryStageExecutionOutputTypeDef(TypedDict):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackStageOutputTypeDef(TypedDict):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipelineExecutionOutputTypeDef(TypedDict):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopPipelineExecutionOutputTypeDef(TypedDict):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PollForJobsInputTypeDef(TypedDict):
    actionTypeId: ActionTypeIdTypeDef
    maxBatchSize: NotRequired[int]
    queryParam: NotRequired[Mapping[str, str]]

class PollForThirdPartyJobsInputTypeDef(TypedDict):
    actionTypeId: ActionTypeIdTypeDef
    maxBatchSize: NotRequired[int]

class ActionDeclarationOutputTypeDef(TypedDict):
    name: str
    actionTypeId: ActionTypeIdTypeDef
    runOrder: NotRequired[int]
    configuration: NotRequired[Dict[str, str]]
    commands: NotRequired[List[str]]
    outputArtifacts: NotRequired[List[OutputArtifactOutputTypeDef]]
    inputArtifacts: NotRequired[List[InputArtifactTypeDef]]
    outputVariables: NotRequired[List[str]]
    roleArn: NotRequired[str]
    region: NotRequired[str]
    namespace: NotRequired[str]
    timeoutInMinutes: NotRequired[int]
    environmentVariables: NotRequired[List[EnvironmentVariableTypeDef]]

class ActionDeclarationTypeDef(TypedDict):
    name: str
    actionTypeId: ActionTypeIdTypeDef
    runOrder: NotRequired[int]
    configuration: NotRequired[Mapping[str, str]]
    commands: NotRequired[Sequence[str]]
    outputArtifacts: NotRequired[Sequence[OutputArtifactTypeDef]]
    inputArtifacts: NotRequired[Sequence[InputArtifactTypeDef]]
    outputVariables: NotRequired[Sequence[str]]
    roleArn: NotRequired[str]
    region: NotRequired[str]
    namespace: NotRequired[str]
    timeoutInMinutes: NotRequired[int]
    environmentVariables: NotRequired[Sequence[EnvironmentVariableTypeDef]]

class ActionExecutionFilterTypeDef(TypedDict):
    pipelineExecutionId: NotRequired[str]
    latestInPipelineExecution: NotRequired[LatestInPipelineExecutionFilterTypeDef]

class RuleExecutionFilterTypeDef(TypedDict):
    pipelineExecutionId: NotRequired[str]
    latestInPipelineExecution: NotRequired[LatestInPipelineExecutionFilterTypeDef]

class ActionExecutionResultTypeDef(TypedDict):
    externalExecutionId: NotRequired[str]
    externalExecutionSummary: NotRequired[str]
    externalExecutionUrl: NotRequired[str]
    errorDetails: NotRequired[ErrorDetailsTypeDef]
    logStreamARN: NotRequired[str]

class ActionExecutionTypeDef(TypedDict):
    actionExecutionId: NotRequired[str]
    status: NotRequired[ActionExecutionStatusType]
    summary: NotRequired[str]
    lastStatusChange: NotRequired[datetime]
    token: NotRequired[str]
    lastUpdatedBy: NotRequired[str]
    externalExecutionId: NotRequired[str]
    externalExecutionUrl: NotRequired[str]
    percentComplete: NotRequired[int]
    errorDetails: NotRequired[ErrorDetailsTypeDef]
    logStreamARN: NotRequired[str]

class RuleExecutionResultTypeDef(TypedDict):
    externalExecutionId: NotRequired[str]
    externalExecutionSummary: NotRequired[str]
    externalExecutionUrl: NotRequired[str]
    errorDetails: NotRequired[ErrorDetailsTypeDef]

class RuleExecutionTypeDef(TypedDict):
    ruleExecutionId: NotRequired[str]
    status: NotRequired[RuleExecutionStatusType]
    summary: NotRequired[str]
    lastStatusChange: NotRequired[datetime]
    token: NotRequired[str]
    lastUpdatedBy: NotRequired[str]
    externalExecutionId: NotRequired[str]
    externalExecutionUrl: NotRequired[str]
    errorDetails: NotRequired[ErrorDetailsTypeDef]

class ActionRevisionTypeDef(TypedDict):
    revisionId: str
    revisionChangeId: str
    created: TimestampTypeDef

class CurrentRevisionTypeDef(TypedDict):
    revision: str
    changeIdentifier: str
    created: NotRequired[TimestampTypeDef]
    revisionSummary: NotRequired[str]

ActionTypeTypeDef = TypedDict(
    "ActionTypeTypeDef",
    {
        "id": ActionTypeIdTypeDef,
        "inputArtifactDetails": ArtifactDetailsTypeDef,
        "outputArtifactDetails": ArtifactDetailsTypeDef,
        "settings": NotRequired[ActionTypeSettingsTypeDef],
        "actionConfigurationProperties": NotRequired[List[ActionConfigurationPropertyTypeDef]],
    },
)

class PutApprovalResultInputTypeDef(TypedDict):
    pipelineName: str
    stageName: str
    actionName: str
    result: ApprovalResultTypeDef
    token: str

class ArtifactDetailTypeDef(TypedDict):
    name: NotRequired[str]
    s3location: NotRequired[S3LocationTypeDef]

ArtifactLocationTypeDef = TypedDict(
    "ArtifactLocationTypeDef",
    {
        "type": NotRequired[Literal["S3"]],
        "s3Location": NotRequired[S3ArtifactLocationTypeDef],
    },
)
ArtifactStoreTypeDef = TypedDict(
    "ArtifactStoreTypeDef",
    {
        "type": Literal["S3"],
        "location": str,
        "encryptionKey": NotRequired[EncryptionKeyTypeDef],
    },
)

class CreateCustomActionTypeInputTypeDef(TypedDict):
    category: ActionCategoryType
    provider: str
    version: str
    inputArtifactDetails: ArtifactDetailsTypeDef
    outputArtifactDetails: ArtifactDetailsTypeDef
    settings: NotRequired[ActionTypeSettingsTypeDef]
    configurationProperties: NotRequired[Sequence[ActionConfigurationPropertyTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class ExecutorConfigurationOutputTypeDef(TypedDict):
    lambdaExecutorConfiguration: NotRequired[LambdaExecutorConfigurationTypeDef]
    jobWorkerExecutorConfiguration: NotRequired[JobWorkerExecutorConfigurationOutputTypeDef]

class ExecutorConfigurationTypeDef(TypedDict):
    lambdaExecutorConfiguration: NotRequired[LambdaExecutorConfigurationTypeDef]
    jobWorkerExecutorConfiguration: NotRequired[JobWorkerExecutorConfigurationTypeDef]

class PutJobFailureResultInputTypeDef(TypedDict):
    jobId: str
    failureDetails: FailureDetailsTypeDef

class PutThirdPartyJobFailureResultInputTypeDef(TypedDict):
    jobId: str
    clientToken: str
    failureDetails: FailureDetailsTypeDef

class GitPullRequestFilterOutputTypeDef(TypedDict):
    events: NotRequired[List[GitPullRequestEventTypeType]]
    branches: NotRequired[GitBranchFilterCriteriaOutputTypeDef]
    filePaths: NotRequired[GitFilePathFilterCriteriaOutputTypeDef]

class GitPullRequestFilterTypeDef(TypedDict):
    events: NotRequired[Sequence[GitPullRequestEventTypeType]]
    branches: NotRequired[GitBranchFilterCriteriaTypeDef]
    filePaths: NotRequired[GitFilePathFilterCriteriaTypeDef]

class GitPushFilterOutputTypeDef(TypedDict):
    tags: NotRequired[GitTagFilterCriteriaOutputTypeDef]
    branches: NotRequired[GitBranchFilterCriteriaOutputTypeDef]
    filePaths: NotRequired[GitFilePathFilterCriteriaOutputTypeDef]

class GitPushFilterTypeDef(TypedDict):
    tags: NotRequired[GitTagFilterCriteriaTypeDef]
    branches: NotRequired[GitBranchFilterCriteriaTypeDef]
    filePaths: NotRequired[GitFilePathFilterCriteriaTypeDef]

class ListActionTypesInputPaginateTypeDef(TypedDict):
    actionOwnerFilter: NotRequired[ActionOwnerType]
    regionFilter: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPipelinesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceInputPaginateTypeDef(TypedDict):
    resourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWebhooksInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPipelinesOutputTypeDef(TypedDict):
    pipelines: List[PipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PipelineContextTypeDef(TypedDict):
    pipelineName: NotRequired[str]
    stage: NotRequired[StageContextTypeDef]
    action: NotRequired[ActionContextTypeDef]
    pipelineArn: NotRequired[str]
    pipelineExecutionId: NotRequired[str]

class PipelineExecutionFilterTypeDef(TypedDict):
    succeededInStage: NotRequired[SucceededInStageFilterTypeDef]

class PipelineExecutionSummaryTypeDef(TypedDict):
    pipelineExecutionId: NotRequired[str]
    status: NotRequired[PipelineExecutionStatusType]
    statusSummary: NotRequired[str]
    startTime: NotRequired[datetime]
    lastUpdateTime: NotRequired[datetime]
    sourceRevisions: NotRequired[List[SourceRevisionTypeDef]]
    trigger: NotRequired[ExecutionTriggerTypeDef]
    stopTrigger: NotRequired[StopExecutionTriggerTypeDef]
    executionMode: NotRequired[ExecutionModeType]
    executionType: NotRequired[ExecutionTypeType]
    rollbackMetadata: NotRequired[PipelineRollbackMetadataTypeDef]

class PipelineExecutionTypeDef(TypedDict):
    pipelineName: NotRequired[str]
    pipelineVersion: NotRequired[int]
    pipelineExecutionId: NotRequired[str]
    status: NotRequired[PipelineExecutionStatusType]
    statusSummary: NotRequired[str]
    artifactRevisions: NotRequired[List[ArtifactRevisionTypeDef]]
    variables: NotRequired[List[ResolvedPipelineVariableTypeDef]]
    trigger: NotRequired[ExecutionTriggerTypeDef]
    executionMode: NotRequired[ExecutionModeType]
    executionType: NotRequired[ExecutionTypeType]
    rollbackMetadata: NotRequired[PipelineRollbackMetadataTypeDef]

class PollForThirdPartyJobsOutputTypeDef(TypedDict):
    jobs: List[ThirdPartyJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleDeclarationOutputTypeDef(TypedDict):
    name: str
    ruleTypeId: RuleTypeIdTypeDef
    configuration: NotRequired[Dict[str, str]]
    commands: NotRequired[List[str]]
    inputArtifacts: NotRequired[List[InputArtifactTypeDef]]
    roleArn: NotRequired[str]
    region: NotRequired[str]
    timeoutInMinutes: NotRequired[int]

class RuleDeclarationTypeDef(TypedDict):
    name: str
    ruleTypeId: RuleTypeIdTypeDef
    configuration: NotRequired[Mapping[str, str]]
    commands: NotRequired[Sequence[str]]
    inputArtifacts: NotRequired[Sequence[InputArtifactTypeDef]]
    roleArn: NotRequired[str]
    region: NotRequired[str]
    timeoutInMinutes: NotRequired[int]

RuleTypeTypeDef = TypedDict(
    "RuleTypeTypeDef",
    {
        "id": RuleTypeIdTypeDef,
        "inputArtifactDetails": ArtifactDetailsTypeDef,
        "settings": NotRequired[RuleTypeSettingsTypeDef],
        "ruleConfigurationProperties": NotRequired[List[RuleConfigurationPropertyTypeDef]],
    },
)

class StartPipelineExecutionInputTypeDef(TypedDict):
    name: str
    variables: NotRequired[Sequence[PipelineVariableTypeDef]]
    clientRequestToken: NotRequired[str]
    sourceRevisions: NotRequired[Sequence[SourceRevisionOverrideTypeDef]]

class WebhookDefinitionOutputTypeDef(TypedDict):
    name: str
    targetPipeline: str
    targetAction: str
    filters: List[WebhookFilterRuleTypeDef]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfigurationTypeDef

class WebhookDefinitionTypeDef(TypedDict):
    name: str
    targetPipeline: str
    targetAction: str
    filters: Sequence[WebhookFilterRuleTypeDef]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfigurationTypeDef

ListActionExecutionsInputPaginateTypeDef = TypedDict(
    "ListActionExecutionsInputPaginateTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[ActionExecutionFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListActionExecutionsInputTypeDef = TypedDict(
    "ListActionExecutionsInputTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[ActionExecutionFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListRuleExecutionsInputPaginateTypeDef = TypedDict(
    "ListRuleExecutionsInputPaginateTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[RuleExecutionFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRuleExecutionsInputTypeDef = TypedDict(
    "ListRuleExecutionsInputTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[RuleExecutionFilterTypeDef],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

class ActionStateTypeDef(TypedDict):
    actionName: NotRequired[str]
    currentRevision: NotRequired[ActionRevisionOutputTypeDef]
    latestExecution: NotRequired[ActionExecutionTypeDef]
    entityUrl: NotRequired[str]
    revisionUrl: NotRequired[str]

class RuleExecutionOutputTypeDef(TypedDict):
    executionResult: NotRequired[RuleExecutionResultTypeDef]

class RuleStateTypeDef(TypedDict):
    ruleName: NotRequired[str]
    currentRevision: NotRequired[RuleRevisionTypeDef]
    latestExecution: NotRequired[RuleExecutionTypeDef]
    entityUrl: NotRequired[str]
    revisionUrl: NotRequired[str]

ActionRevisionUnionTypeDef = Union[ActionRevisionTypeDef, ActionRevisionOutputTypeDef]

class PutJobSuccessResultInputTypeDef(TypedDict):
    jobId: str
    currentRevision: NotRequired[CurrentRevisionTypeDef]
    continuationToken: NotRequired[str]
    executionDetails: NotRequired[ExecutionDetailsTypeDef]
    outputVariables: NotRequired[Mapping[str, str]]

class PutThirdPartyJobSuccessResultInputTypeDef(TypedDict):
    jobId: str
    clientToken: str
    currentRevision: NotRequired[CurrentRevisionTypeDef]
    continuationToken: NotRequired[str]
    executionDetails: NotRequired[ExecutionDetailsTypeDef]

class CreateCustomActionTypeOutputTypeDef(TypedDict):
    actionType: ActionTypeTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListActionTypesOutputTypeDef(TypedDict):
    actionTypes: List[ActionTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ActionExecutionInputTypeDef(TypedDict):
    actionTypeId: NotRequired[ActionTypeIdTypeDef]
    configuration: NotRequired[Dict[str, str]]
    resolvedConfiguration: NotRequired[Dict[str, str]]
    roleArn: NotRequired[str]
    region: NotRequired[str]
    inputArtifacts: NotRequired[List[ArtifactDetailTypeDef]]
    namespace: NotRequired[str]

class ActionExecutionOutputTypeDef(TypedDict):
    outputArtifacts: NotRequired[List[ArtifactDetailTypeDef]]
    executionResult: NotRequired[ActionExecutionResultTypeDef]
    outputVariables: NotRequired[Dict[str, str]]

class RuleExecutionInputTypeDef(TypedDict):
    ruleTypeId: NotRequired[RuleTypeIdTypeDef]
    configuration: NotRequired[Dict[str, str]]
    resolvedConfiguration: NotRequired[Dict[str, str]]
    roleArn: NotRequired[str]
    region: NotRequired[str]
    inputArtifacts: NotRequired[List[ArtifactDetailTypeDef]]

class ArtifactTypeDef(TypedDict):
    name: NotRequired[str]
    revision: NotRequired[str]
    location: NotRequired[ArtifactLocationTypeDef]

ActionTypeExecutorOutputTypeDef = TypedDict(
    "ActionTypeExecutorOutputTypeDef",
    {
        "configuration": ExecutorConfigurationOutputTypeDef,
        "type": ExecutorTypeType,
        "policyStatementsTemplate": NotRequired[str],
        "jobTimeout": NotRequired[int],
    },
)
ActionTypeExecutorTypeDef = TypedDict(
    "ActionTypeExecutorTypeDef",
    {
        "configuration": ExecutorConfigurationTypeDef,
        "type": ExecutorTypeType,
        "policyStatementsTemplate": NotRequired[str],
        "jobTimeout": NotRequired[int],
    },
)

class GitConfigurationOutputTypeDef(TypedDict):
    sourceActionName: str
    push: NotRequired[List[GitPushFilterOutputTypeDef]]
    pullRequest: NotRequired[List[GitPullRequestFilterOutputTypeDef]]

class GitConfigurationTypeDef(TypedDict):
    sourceActionName: str
    push: NotRequired[Sequence[GitPushFilterTypeDef]]
    pullRequest: NotRequired[Sequence[GitPullRequestFilterTypeDef]]

ListPipelineExecutionsInputPaginateTypeDef = TypedDict(
    "ListPipelineExecutionsInputPaginateTypeDef",
    {
        "pipelineName": str,
        "filter": NotRequired[PipelineExecutionFilterTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPipelineExecutionsInputTypeDef = TypedDict(
    "ListPipelineExecutionsInputTypeDef",
    {
        "pipelineName": str,
        "maxResults": NotRequired[int],
        "filter": NotRequired[PipelineExecutionFilterTypeDef],
        "nextToken": NotRequired[str],
    },
)

class ListPipelineExecutionsOutputTypeDef(TypedDict):
    pipelineExecutionSummaries: List[PipelineExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetPipelineExecutionOutputTypeDef(TypedDict):
    pipelineExecution: PipelineExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConditionOutputTypeDef(TypedDict):
    result: NotRequired[ResultType]
    rules: NotRequired[List[RuleDeclarationOutputTypeDef]]

class ConditionTypeDef(TypedDict):
    result: NotRequired[ResultType]
    rules: NotRequired[Sequence[RuleDeclarationTypeDef]]

class ListRuleTypesOutputTypeDef(TypedDict):
    ruleTypes: List[RuleTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebhookItemTypeDef(TypedDict):
    definition: WebhookDefinitionOutputTypeDef
    url: str
    errorMessage: NotRequired[str]
    errorCode: NotRequired[str]
    lastTriggered: NotRequired[datetime]
    arn: NotRequired[str]
    tags: NotRequired[List[TagTypeDef]]

WebhookDefinitionUnionTypeDef = Union[WebhookDefinitionTypeDef, WebhookDefinitionOutputTypeDef]

class ConditionStateTypeDef(TypedDict):
    latestExecution: NotRequired[ConditionExecutionTypeDef]
    ruleStates: NotRequired[List[RuleStateTypeDef]]

class PutActionRevisionInputTypeDef(TypedDict):
    pipelineName: str
    stageName: str
    actionName: str
    actionRevision: ActionRevisionUnionTypeDef

ActionExecutionDetailTypeDef = TypedDict(
    "ActionExecutionDetailTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "actionExecutionId": NotRequired[str],
        "pipelineVersion": NotRequired[int],
        "stageName": NotRequired[str],
        "actionName": NotRequired[str],
        "startTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "status": NotRequired[ActionExecutionStatusType],
        "input": NotRequired[ActionExecutionInputTypeDef],
        "output": NotRequired[ActionExecutionOutputTypeDef],
    },
)
RuleExecutionDetailTypeDef = TypedDict(
    "RuleExecutionDetailTypeDef",
    {
        "pipelineExecutionId": NotRequired[str],
        "ruleExecutionId": NotRequired[str],
        "pipelineVersion": NotRequired[int],
        "stageName": NotRequired[str],
        "ruleName": NotRequired[str],
        "startTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "updatedBy": NotRequired[str],
        "status": NotRequired[RuleExecutionStatusType],
        "input": NotRequired[RuleExecutionInputTypeDef],
        "output": NotRequired[RuleExecutionOutputTypeDef],
    },
)

class JobDataTypeDef(TypedDict):
    actionTypeId: NotRequired[ActionTypeIdTypeDef]
    actionConfiguration: NotRequired[ActionConfigurationTypeDef]
    pipelineContext: NotRequired[PipelineContextTypeDef]
    inputArtifacts: NotRequired[List[ArtifactTypeDef]]
    outputArtifacts: NotRequired[List[ArtifactTypeDef]]
    artifactCredentials: NotRequired[AWSSessionCredentialsTypeDef]
    continuationToken: NotRequired[str]
    encryptionKey: NotRequired[EncryptionKeyTypeDef]

class ThirdPartyJobDataTypeDef(TypedDict):
    actionTypeId: NotRequired[ActionTypeIdTypeDef]
    actionConfiguration: NotRequired[ActionConfigurationTypeDef]
    pipelineContext: NotRequired[PipelineContextTypeDef]
    inputArtifacts: NotRequired[List[ArtifactTypeDef]]
    outputArtifacts: NotRequired[List[ArtifactTypeDef]]
    artifactCredentials: NotRequired[AWSSessionCredentialsTypeDef]
    continuationToken: NotRequired[str]
    encryptionKey: NotRequired[EncryptionKeyTypeDef]

ActionTypeDeclarationOutputTypeDef = TypedDict(
    "ActionTypeDeclarationOutputTypeDef",
    {
        "executor": ActionTypeExecutorOutputTypeDef,
        "id": ActionTypeIdentifierTypeDef,
        "inputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "outputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "description": NotRequired[str],
        "permissions": NotRequired[ActionTypePermissionsOutputTypeDef],
        "properties": NotRequired[List[ActionTypePropertyTypeDef]],
        "urls": NotRequired[ActionTypeUrlsTypeDef],
    },
)
ActionTypeDeclarationTypeDef = TypedDict(
    "ActionTypeDeclarationTypeDef",
    {
        "executor": ActionTypeExecutorTypeDef,
        "id": ActionTypeIdentifierTypeDef,
        "inputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "outputArtifactDetails": ActionTypeArtifactDetailsTypeDef,
        "description": NotRequired[str],
        "permissions": NotRequired[ActionTypePermissionsTypeDef],
        "properties": NotRequired[Sequence[ActionTypePropertyTypeDef]],
        "urls": NotRequired[ActionTypeUrlsTypeDef],
    },
)

class PipelineTriggerDeclarationOutputTypeDef(TypedDict):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationOutputTypeDef

class PipelineTriggerDeclarationTypeDef(TypedDict):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationTypeDef

class BeforeEntryConditionsOutputTypeDef(TypedDict):
    conditions: List[ConditionOutputTypeDef]

class FailureConditionsOutputTypeDef(TypedDict):
    result: NotRequired[ResultType]
    retryConfiguration: NotRequired[RetryConfigurationTypeDef]
    conditions: NotRequired[List[ConditionOutputTypeDef]]

class SuccessConditionsOutputTypeDef(TypedDict):
    conditions: List[ConditionOutputTypeDef]

class BeforeEntryConditionsTypeDef(TypedDict):
    conditions: Sequence[ConditionTypeDef]

class FailureConditionsTypeDef(TypedDict):
    result: NotRequired[ResultType]
    retryConfiguration: NotRequired[RetryConfigurationTypeDef]
    conditions: NotRequired[Sequence[ConditionTypeDef]]

class SuccessConditionsTypeDef(TypedDict):
    conditions: Sequence[ConditionTypeDef]

class ListWebhooksOutputTypeDef(TypedDict):
    webhooks: List[ListWebhookItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutWebhookOutputTypeDef(TypedDict):
    webhook: ListWebhookItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutWebhookInputTypeDef(TypedDict):
    webhook: WebhookDefinitionUnionTypeDef
    tags: NotRequired[Sequence[TagTypeDef]]

class StageConditionStateTypeDef(TypedDict):
    latestExecution: NotRequired[StageConditionsExecutionTypeDef]
    conditionStates: NotRequired[List[ConditionStateTypeDef]]

class ListActionExecutionsOutputTypeDef(TypedDict):
    actionExecutionDetails: List[ActionExecutionDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRuleExecutionsOutputTypeDef(TypedDict):
    ruleExecutionDetails: List[RuleExecutionDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired[JobDataTypeDef],
        "accountId": NotRequired[str],
    },
)
JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired[JobDataTypeDef],
        "nonce": NotRequired[str],
        "accountId": NotRequired[str],
    },
)
ThirdPartyJobDetailsTypeDef = TypedDict(
    "ThirdPartyJobDetailsTypeDef",
    {
        "id": NotRequired[str],
        "data": NotRequired[ThirdPartyJobDataTypeDef],
        "nonce": NotRequired[str],
    },
)

class GetActionTypeOutputTypeDef(TypedDict):
    actionType: ActionTypeDeclarationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ActionTypeDeclarationUnionTypeDef = Union[
    ActionTypeDeclarationTypeDef, ActionTypeDeclarationOutputTypeDef
]

class StageDeclarationOutputTypeDef(TypedDict):
    name: str
    actions: List[ActionDeclarationOutputTypeDef]
    blockers: NotRequired[List[BlockerDeclarationTypeDef]]
    onFailure: NotRequired[FailureConditionsOutputTypeDef]
    onSuccess: NotRequired[SuccessConditionsOutputTypeDef]
    beforeEntry: NotRequired[BeforeEntryConditionsOutputTypeDef]

class StageDeclarationTypeDef(TypedDict):
    name: str
    actions: Sequence[ActionDeclarationTypeDef]
    blockers: NotRequired[Sequence[BlockerDeclarationTypeDef]]
    onFailure: NotRequired[FailureConditionsTypeDef]
    onSuccess: NotRequired[SuccessConditionsTypeDef]
    beforeEntry: NotRequired[BeforeEntryConditionsTypeDef]

class StageStateTypeDef(TypedDict):
    stageName: NotRequired[str]
    inboundExecution: NotRequired[StageExecutionTypeDef]
    inboundExecutions: NotRequired[List[StageExecutionTypeDef]]
    inboundTransitionState: NotRequired[TransitionStateTypeDef]
    actionStates: NotRequired[List[ActionStateTypeDef]]
    latestExecution: NotRequired[StageExecutionTypeDef]
    beforeEntryConditionState: NotRequired[StageConditionStateTypeDef]
    onSuccessConditionState: NotRequired[StageConditionStateTypeDef]
    onFailureConditionState: NotRequired[StageConditionStateTypeDef]
    retryStageMetadata: NotRequired[RetryStageMetadataTypeDef]

class GetJobDetailsOutputTypeDef(TypedDict):
    jobDetails: JobDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PollForJobsOutputTypeDef(TypedDict):
    jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetThirdPartyJobDetailsOutputTypeDef(TypedDict):
    jobDetails: ThirdPartyJobDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActionTypeInputTypeDef(TypedDict):
    actionType: ActionTypeDeclarationUnionTypeDef

class PipelineDeclarationOutputTypeDef(TypedDict):
    name: str
    roleArn: str
    stages: List[StageDeclarationOutputTypeDef]
    artifactStore: NotRequired[ArtifactStoreTypeDef]
    artifactStores: NotRequired[Dict[str, ArtifactStoreTypeDef]]
    version: NotRequired[int]
    executionMode: NotRequired[ExecutionModeType]
    pipelineType: NotRequired[PipelineTypeType]
    variables: NotRequired[List[PipelineVariableDeclarationTypeDef]]
    triggers: NotRequired[List[PipelineTriggerDeclarationOutputTypeDef]]

class PipelineDeclarationTypeDef(TypedDict):
    name: str
    roleArn: str
    stages: Sequence[StageDeclarationTypeDef]
    artifactStore: NotRequired[ArtifactStoreTypeDef]
    artifactStores: NotRequired[Mapping[str, ArtifactStoreTypeDef]]
    version: NotRequired[int]
    executionMode: NotRequired[ExecutionModeType]
    pipelineType: NotRequired[PipelineTypeType]
    variables: NotRequired[Sequence[PipelineVariableDeclarationTypeDef]]
    triggers: NotRequired[Sequence[PipelineTriggerDeclarationTypeDef]]

class GetPipelineStateOutputTypeDef(TypedDict):
    pipelineName: str
    pipelineVersion: int
    stageStates: List[StageStateTypeDef]
    created: datetime
    updated: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePipelineOutputTypeDef(TypedDict):
    pipeline: PipelineDeclarationOutputTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPipelineOutputTypeDef(TypedDict):
    pipeline: PipelineDeclarationOutputTypeDef
    metadata: PipelineMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineOutputTypeDef(TypedDict):
    pipeline: PipelineDeclarationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

PipelineDeclarationUnionTypeDef = Union[
    PipelineDeclarationTypeDef, PipelineDeclarationOutputTypeDef
]

class CreatePipelineInputTypeDef(TypedDict):
    pipeline: PipelineDeclarationUnionTypeDef
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdatePipelineInputTypeDef(TypedDict):
    pipeline: PipelineDeclarationUnionTypeDef
