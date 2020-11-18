"""
Main interface for codepipeline service type definitions.

Usage::

    ```python
    from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef

    data: AWSSessionCredentialsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AWSSessionCredentialsTypeDef",
    "ActionConfigurationPropertyTypeDef",
    "ActionConfigurationTypeDef",
    "ActionContextTypeDef",
    "ActionDeclarationTypeDef",
    "ActionExecutionDetailTypeDef",
    "ActionExecutionInputTypeDef",
    "ActionExecutionOutputTypeDef",
    "ActionExecutionResultTypeDef",
    "ActionExecutionTypeDef",
    "ActionRevisionTypeDef",
    "ActionStateTypeDef",
    "ActionTypeIdTypeDef",
    "ActionTypeSettingsTypeDef",
    "ActionTypeTypeDef",
    "ArtifactDetailTypeDef",
    "ArtifactDetailsTypeDef",
    "ArtifactLocationTypeDef",
    "ArtifactRevisionTypeDef",
    "ArtifactStoreTypeDef",
    "ArtifactTypeDef",
    "BlockerDeclarationTypeDef",
    "EncryptionKeyTypeDef",
    "ErrorDetailsTypeDef",
    "ExecutionTriggerTypeDef",
    "InputArtifactTypeDef",
    "JobDataTypeDef",
    "JobDetailsTypeDef",
    "JobTypeDef",
    "ListWebhookItemTypeDef",
    "OutputArtifactTypeDef",
    "PipelineContextTypeDef",
    "PipelineDeclarationTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineMetadataTypeDef",
    "PipelineSummaryTypeDef",
    "ResponseMetadata",
    "S3ArtifactLocationTypeDef",
    "S3LocationTypeDef",
    "SourceRevisionTypeDef",
    "StageContextTypeDef",
    "StageDeclarationTypeDef",
    "StageExecutionTypeDef",
    "StageStateTypeDef",
    "StopExecutionTriggerTypeDef",
    "TagTypeDef",
    "ThirdPartyJobDataTypeDef",
    "ThirdPartyJobDetailsTypeDef",
    "ThirdPartyJobTypeDef",
    "TransitionStateTypeDef",
    "WebhookAuthConfigurationTypeDef",
    "WebhookDefinitionTypeDef",
    "WebhookFilterRuleTypeDef",
    "AcknowledgeJobOutputTypeDef",
    "AcknowledgeThirdPartyJobOutputTypeDef",
    "ActionExecutionFilterTypeDef",
    "ApprovalResultTypeDef",
    "CreateCustomActionTypeOutputTypeDef",
    "CreatePipelineOutputTypeDef",
    "CurrentRevisionTypeDef",
    "ExecutionDetailsTypeDef",
    "FailureDetailsTypeDef",
    "GetJobDetailsOutputTypeDef",
    "GetPipelineExecutionOutputTypeDef",
    "GetPipelineOutputTypeDef",
    "GetPipelineStateOutputTypeDef",
    "GetThirdPartyJobDetailsOutputTypeDef",
    "ListActionExecutionsOutputTypeDef",
    "ListActionTypesOutputTypeDef",
    "ListPipelineExecutionsOutputTypeDef",
    "ListPipelinesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWebhooksOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PollForJobsOutputTypeDef",
    "PollForThirdPartyJobsOutputTypeDef",
    "PutActionRevisionOutputTypeDef",
    "PutApprovalResultOutputTypeDef",
    "PutWebhookOutputTypeDef",
    "RetryStageExecutionOutputTypeDef",
    "StartPipelineExecutionOutputTypeDef",
    "StopPipelineExecutionOutputTypeDef",
    "UpdatePipelineOutputTypeDef",
)

AWSSessionCredentialsTypeDef = TypedDict(
    "AWSSessionCredentialsTypeDef",
    {"accessKeyId": str, "secretAccessKey": str, "sessionToken": str},
)

_RequiredActionConfigurationPropertyTypeDef = TypedDict(
    "_RequiredActionConfigurationPropertyTypeDef",
    {"name": str, "required": bool, "key": bool, "secret": bool},
)
_OptionalActionConfigurationPropertyTypeDef = TypedDict(
    "_OptionalActionConfigurationPropertyTypeDef",
    {"queryable": bool, "description": str, "type": Literal["String", "Number", "Boolean"]},
    total=False,
)


class ActionConfigurationPropertyTypeDef(
    _RequiredActionConfigurationPropertyTypeDef, _OptionalActionConfigurationPropertyTypeDef
):
    pass


ActionConfigurationTypeDef = TypedDict(
    "ActionConfigurationTypeDef", {"configuration": Dict[str, str]}, total=False
)

ActionContextTypeDef = TypedDict(
    "ActionContextTypeDef", {"name": str, "actionExecutionId": str}, total=False
)

_RequiredActionDeclarationTypeDef = TypedDict(
    "_RequiredActionDeclarationTypeDef", {"name": str, "actionTypeId": "ActionTypeIdTypeDef"}
)
_OptionalActionDeclarationTypeDef = TypedDict(
    "_OptionalActionDeclarationTypeDef",
    {
        "runOrder": int,
        "configuration": Dict[str, str],
        "outputArtifacts": List["OutputArtifactTypeDef"],
        "inputArtifacts": List["InputArtifactTypeDef"],
        "roleArn": str,
        "region": str,
        "namespace": str,
    },
    total=False,
)


class ActionDeclarationTypeDef(
    _RequiredActionDeclarationTypeDef, _OptionalActionDeclarationTypeDef
):
    pass


ActionExecutionDetailTypeDef = TypedDict(
    "ActionExecutionDetailTypeDef",
    {
        "pipelineExecutionId": str,
        "actionExecutionId": str,
        "pipelineVersion": int,
        "stageName": str,
        "actionName": str,
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "status": Literal["InProgress", "Abandoned", "Succeeded", "Failed"],
        "input": "ActionExecutionInputTypeDef",
        "output": "ActionExecutionOutputTypeDef",
    },
    total=False,
)

ActionExecutionInputTypeDef = TypedDict(
    "ActionExecutionInputTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
        "configuration": Dict[str, str],
        "resolvedConfiguration": Dict[str, str],
        "roleArn": str,
        "region": str,
        "inputArtifacts": List["ArtifactDetailTypeDef"],
        "namespace": str,
    },
    total=False,
)

ActionExecutionOutputTypeDef = TypedDict(
    "ActionExecutionOutputTypeDef",
    {
        "outputArtifacts": List["ArtifactDetailTypeDef"],
        "executionResult": "ActionExecutionResultTypeDef",
        "outputVariables": Dict[str, str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ActionExecutionResultTypeDef = TypedDict(
    "ActionExecutionResultTypeDef",
    {"externalExecutionId": str, "externalExecutionSummary": str, "externalExecutionUrl": str},
    total=False,
)

ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "actionExecutionId": str,
        "status": Literal["InProgress", "Abandoned", "Succeeded", "Failed"],
        "summary": str,
        "lastStatusChange": datetime,
        "token": str,
        "lastUpdatedBy": str,
        "externalExecutionId": str,
        "externalExecutionUrl": str,
        "percentComplete": int,
        "errorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

ActionRevisionTypeDef = TypedDict(
    "ActionRevisionTypeDef", {"revisionId": str, "revisionChangeId": str, "created": datetime}
)

ActionStateTypeDef = TypedDict(
    "ActionStateTypeDef",
    {
        "actionName": str,
        "currentRevision": "ActionRevisionTypeDef",
        "latestExecution": "ActionExecutionTypeDef",
        "entityUrl": str,
        "revisionUrl": str,
    },
    total=False,
)

ActionTypeIdTypeDef = TypedDict(
    "ActionTypeIdTypeDef",
    {
        "category": Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        "owner": Literal["AWS", "ThirdParty", "Custom"],
        "provider": str,
        "version": str,
    },
)

ActionTypeSettingsTypeDef = TypedDict(
    "ActionTypeSettingsTypeDef",
    {
        "thirdPartyConfigurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

_RequiredActionTypeTypeDef = TypedDict(
    "_RequiredActionTypeTypeDef",
    {
        "id": "ActionTypeIdTypeDef",
        "inputArtifactDetails": "ArtifactDetailsTypeDef",
        "outputArtifactDetails": "ArtifactDetailsTypeDef",
    },
)
_OptionalActionTypeTypeDef = TypedDict(
    "_OptionalActionTypeTypeDef",
    {
        "settings": "ActionTypeSettingsTypeDef",
        "actionConfigurationProperties": List["ActionConfigurationPropertyTypeDef"],
    },
    total=False,
)


class ActionTypeTypeDef(_RequiredActionTypeTypeDef, _OptionalActionTypeTypeDef):
    pass


ArtifactDetailTypeDef = TypedDict(
    "ArtifactDetailTypeDef", {"name": str, "s3location": "S3LocationTypeDef"}, total=False
)

ArtifactDetailsTypeDef = TypedDict(
    "ArtifactDetailsTypeDef", {"minimumCount": int, "maximumCount": int}
)

ArtifactLocationTypeDef = TypedDict(
    "ArtifactLocationTypeDef",
    {"type": Literal["S3"], "s3Location": "S3ArtifactLocationTypeDef"},
    total=False,
)

ArtifactRevisionTypeDef = TypedDict(
    "ArtifactRevisionTypeDef",
    {
        "name": str,
        "revisionId": str,
        "revisionChangeIdentifier": str,
        "revisionSummary": str,
        "created": datetime,
        "revisionUrl": str,
    },
    total=False,
)

_RequiredArtifactStoreTypeDef = TypedDict(
    "_RequiredArtifactStoreTypeDef", {"type": Literal["S3"], "location": str}
)
_OptionalArtifactStoreTypeDef = TypedDict(
    "_OptionalArtifactStoreTypeDef", {"encryptionKey": "EncryptionKeyTypeDef"}, total=False
)


class ArtifactStoreTypeDef(_RequiredArtifactStoreTypeDef, _OptionalArtifactStoreTypeDef):
    pass


ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {"name": str, "revision": str, "location": "ArtifactLocationTypeDef"},
    total=False,
)

BlockerDeclarationTypeDef = TypedDict(
    "BlockerDeclarationTypeDef", {"name": str, "type": Literal["Schedule"]}
)

EncryptionKeyTypeDef = TypedDict("EncryptionKeyTypeDef", {"id": str, "type": Literal["KMS"]})

ErrorDetailsTypeDef = TypedDict("ErrorDetailsTypeDef", {"code": str, "message": str}, total=False)

ExecutionTriggerTypeDef = TypedDict(
    "ExecutionTriggerTypeDef",
    {
        "triggerType": Literal[
            "CreatePipeline",
            "StartPipelineExecution",
            "PollForSourceChanges",
            "Webhook",
            "CloudWatchEvent",
            "PutActionRevision",
        ],
        "triggerDetail": str,
    },
    total=False,
)

InputArtifactTypeDef = TypedDict("InputArtifactTypeDef", {"name": str})

JobDataTypeDef = TypedDict(
    "JobDataTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
        "actionConfiguration": "ActionConfigurationTypeDef",
        "pipelineContext": "PipelineContextTypeDef",
        "inputArtifacts": List["ArtifactTypeDef"],
        "outputArtifacts": List["ArtifactTypeDef"],
        "artifactCredentials": "AWSSessionCredentialsTypeDef",
        "continuationToken": str,
        "encryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef", {"id": str, "data": "JobDataTypeDef", "accountId": str}, total=False
)

JobTypeDef = TypedDict(
    "JobTypeDef", {"id": str, "data": "JobDataTypeDef", "nonce": str, "accountId": str}, total=False
)

_RequiredListWebhookItemTypeDef = TypedDict(
    "_RequiredListWebhookItemTypeDef", {"definition": "WebhookDefinitionTypeDef", "url": str}
)
_OptionalListWebhookItemTypeDef = TypedDict(
    "_OptionalListWebhookItemTypeDef",
    {
        "errorMessage": str,
        "errorCode": str,
        "lastTriggered": datetime,
        "arn": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class ListWebhookItemTypeDef(_RequiredListWebhookItemTypeDef, _OptionalListWebhookItemTypeDef):
    pass


OutputArtifactTypeDef = TypedDict("OutputArtifactTypeDef", {"name": str})

PipelineContextTypeDef = TypedDict(
    "PipelineContextTypeDef",
    {
        "pipelineName": str,
        "stage": "StageContextTypeDef",
        "action": "ActionContextTypeDef",
        "pipelineArn": str,
        "pipelineExecutionId": str,
    },
    total=False,
)

_RequiredPipelineDeclarationTypeDef = TypedDict(
    "_RequiredPipelineDeclarationTypeDef",
    {"name": str, "roleArn": str, "stages": List["StageDeclarationTypeDef"]},
)
_OptionalPipelineDeclarationTypeDef = TypedDict(
    "_OptionalPipelineDeclarationTypeDef",
    {
        "artifactStore": "ArtifactStoreTypeDef",
        "artifactStores": Dict[str, "ArtifactStoreTypeDef"],
        "version": int,
    },
    total=False,
)


class PipelineDeclarationTypeDef(
    _RequiredPipelineDeclarationTypeDef, _OptionalPipelineDeclarationTypeDef
):
    pass


PipelineExecutionSummaryTypeDef = TypedDict(
    "PipelineExecutionSummaryTypeDef",
    {
        "pipelineExecutionId": str,
        "status": Literal["InProgress", "Stopped", "Stopping", "Succeeded", "Superseded", "Failed"],
        "startTime": datetime,
        "lastUpdateTime": datetime,
        "sourceRevisions": List["SourceRevisionTypeDef"],
        "trigger": "ExecutionTriggerTypeDef",
        "stopTrigger": "StopExecutionTriggerTypeDef",
    },
    total=False,
)

PipelineExecutionTypeDef = TypedDict(
    "PipelineExecutionTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "pipelineExecutionId": str,
        "status": Literal["InProgress", "Stopped", "Stopping", "Succeeded", "Superseded", "Failed"],
        "artifactRevisions": List["ArtifactRevisionTypeDef"],
    },
    total=False,
)

PipelineMetadataTypeDef = TypedDict(
    "PipelineMetadataTypeDef",
    {"pipelineArn": str, "created": datetime, "updated": datetime},
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {"name": str, "version": int, "created": datetime, "updated": datetime},
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

S3ArtifactLocationTypeDef = TypedDict(
    "S3ArtifactLocationTypeDef", {"bucketName": str, "objectKey": str}
)

S3LocationTypeDef = TypedDict("S3LocationTypeDef", {"bucket": str, "key": str}, total=False)

_RequiredSourceRevisionTypeDef = TypedDict("_RequiredSourceRevisionTypeDef", {"actionName": str})
_OptionalSourceRevisionTypeDef = TypedDict(
    "_OptionalSourceRevisionTypeDef",
    {"revisionId": str, "revisionSummary": str, "revisionUrl": str},
    total=False,
)


class SourceRevisionTypeDef(_RequiredSourceRevisionTypeDef, _OptionalSourceRevisionTypeDef):
    pass


StageContextTypeDef = TypedDict("StageContextTypeDef", {"name": str}, total=False)

_RequiredStageDeclarationTypeDef = TypedDict(
    "_RequiredStageDeclarationTypeDef", {"name": str, "actions": List["ActionDeclarationTypeDef"]}
)
_OptionalStageDeclarationTypeDef = TypedDict(
    "_OptionalStageDeclarationTypeDef", {"blockers": List["BlockerDeclarationTypeDef"]}, total=False
)


class StageDeclarationTypeDef(_RequiredStageDeclarationTypeDef, _OptionalStageDeclarationTypeDef):
    pass


StageExecutionTypeDef = TypedDict(
    "StageExecutionTypeDef",
    {
        "pipelineExecutionId": str,
        "status": Literal["InProgress", "Failed", "Stopped", "Stopping", "Succeeded"],
    },
)

StageStateTypeDef = TypedDict(
    "StageStateTypeDef",
    {
        "stageName": str,
        "inboundExecution": "StageExecutionTypeDef",
        "inboundTransitionState": "TransitionStateTypeDef",
        "actionStates": List["ActionStateTypeDef"],
        "latestExecution": "StageExecutionTypeDef",
    },
    total=False,
)

StopExecutionTriggerTypeDef = TypedDict("StopExecutionTriggerTypeDef", {"reason": str}, total=False)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str})

ThirdPartyJobDataTypeDef = TypedDict(
    "ThirdPartyJobDataTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
        "actionConfiguration": "ActionConfigurationTypeDef",
        "pipelineContext": "PipelineContextTypeDef",
        "inputArtifacts": List["ArtifactTypeDef"],
        "outputArtifacts": List["ArtifactTypeDef"],
        "artifactCredentials": "AWSSessionCredentialsTypeDef",
        "continuationToken": str,
        "encryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)

ThirdPartyJobDetailsTypeDef = TypedDict(
    "ThirdPartyJobDetailsTypeDef",
    {"id": str, "data": "ThirdPartyJobDataTypeDef", "nonce": str},
    total=False,
)

ThirdPartyJobTypeDef = TypedDict(
    "ThirdPartyJobTypeDef", {"clientId": str, "jobId": str}, total=False
)

TransitionStateTypeDef = TypedDict(
    "TransitionStateTypeDef",
    {"enabled": bool, "lastChangedBy": str, "lastChangedAt": datetime, "disabledReason": str},
    total=False,
)

WebhookAuthConfigurationTypeDef = TypedDict(
    "WebhookAuthConfigurationTypeDef", {"AllowedIPRange": str, "SecretToken": str}, total=False
)

WebhookDefinitionTypeDef = TypedDict(
    "WebhookDefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List["WebhookFilterRuleTypeDef"],
        "authentication": Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"],
        "authenticationConfiguration": "WebhookAuthConfigurationTypeDef",
    },
)

_RequiredWebhookFilterRuleTypeDef = TypedDict(
    "_RequiredWebhookFilterRuleTypeDef", {"jsonPath": str}
)
_OptionalWebhookFilterRuleTypeDef = TypedDict(
    "_OptionalWebhookFilterRuleTypeDef", {"matchEquals": str}, total=False
)


class WebhookFilterRuleTypeDef(
    _RequiredWebhookFilterRuleTypeDef, _OptionalWebhookFilterRuleTypeDef
):
    pass


AcknowledgeJobOutputTypeDef = TypedDict(
    "AcknowledgeJobOutputTypeDef",
    {
        "status": Literal[
            "Created", "Queued", "Dispatched", "InProgress", "TimedOut", "Succeeded", "Failed"
        ],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

AcknowledgeThirdPartyJobOutputTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobOutputTypeDef",
    {
        "status": Literal[
            "Created", "Queued", "Dispatched", "InProgress", "TimedOut", "Succeeded", "Failed"
        ],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ActionExecutionFilterTypeDef = TypedDict(
    "ActionExecutionFilterTypeDef", {"pipelineExecutionId": str}, total=False
)

ApprovalResultTypeDef = TypedDict(
    "ApprovalResultTypeDef", {"summary": str, "status": Literal["Approved", "Rejected"]}
)

_RequiredCreateCustomActionTypeOutputTypeDef = TypedDict(
    "_RequiredCreateCustomActionTypeOutputTypeDef", {"actionType": "ActionTypeTypeDef"}
)
_OptionalCreateCustomActionTypeOutputTypeDef = TypedDict(
    "_OptionalCreateCustomActionTypeOutputTypeDef",
    {"tags": List["TagTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateCustomActionTypeOutputTypeDef(
    _RequiredCreateCustomActionTypeOutputTypeDef, _OptionalCreateCustomActionTypeOutputTypeDef
):
    pass


CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredCurrentRevisionTypeDef = TypedDict(
    "_RequiredCurrentRevisionTypeDef", {"revision": str, "changeIdentifier": str}
)
_OptionalCurrentRevisionTypeDef = TypedDict(
    "_OptionalCurrentRevisionTypeDef", {"created": datetime, "revisionSummary": str}, total=False
)


class CurrentRevisionTypeDef(_RequiredCurrentRevisionTypeDef, _OptionalCurrentRevisionTypeDef):
    pass


ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {"summary": str, "externalExecutionId": str, "percentComplete": int},
    total=False,
)

_RequiredFailureDetailsTypeDef = TypedDict(
    "_RequiredFailureDetailsTypeDef",
    {
        "type": Literal[
            "JobFailed",
            "ConfigurationError",
            "PermissionError",
            "RevisionOutOfSync",
            "RevisionUnavailable",
            "SystemUnavailable",
        ],
        "message": str,
    },
)
_OptionalFailureDetailsTypeDef = TypedDict(
    "_OptionalFailureDetailsTypeDef", {"externalExecutionId": str}, total=False
)


class FailureDetailsTypeDef(_RequiredFailureDetailsTypeDef, _OptionalFailureDetailsTypeDef):
    pass


GetJobDetailsOutputTypeDef = TypedDict(
    "GetJobDetailsOutputTypeDef",
    {"jobDetails": "JobDetailsTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetPipelineExecutionOutputTypeDef = TypedDict(
    "GetPipelineExecutionOutputTypeDef",
    {"pipelineExecution": "PipelineExecutionTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetPipelineOutputTypeDef = TypedDict(
    "GetPipelineOutputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "metadata": "PipelineMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetPipelineStateOutputTypeDef = TypedDict(
    "GetPipelineStateOutputTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List["StageStateTypeDef"],
        "created": datetime,
        "updated": datetime,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetThirdPartyJobDetailsOutputTypeDef = TypedDict(
    "GetThirdPartyJobDetailsOutputTypeDef",
    {"jobDetails": "ThirdPartyJobDetailsTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListActionExecutionsOutputTypeDef = TypedDict(
    "ListActionExecutionsOutputTypeDef",
    {
        "actionExecutionDetails": List["ActionExecutionDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

_RequiredListActionTypesOutputTypeDef = TypedDict(
    "_RequiredListActionTypesOutputTypeDef", {"actionTypes": List["ActionTypeTypeDef"]}
)
_OptionalListActionTypesOutputTypeDef = TypedDict(
    "_OptionalListActionTypesOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListActionTypesOutputTypeDef(
    _RequiredListActionTypesOutputTypeDef, _OptionalListActionTypesOutputTypeDef
):
    pass


ListPipelineExecutionsOutputTypeDef = TypedDict(
    "ListPipelineExecutionsOutputTypeDef",
    {
        "pipelineExecutionSummaries": List["PipelineExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelines": List["PipelineSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"tags": List["TagTypeDef"], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListWebhooksOutputTypeDef = TypedDict(
    "ListWebhooksOutputTypeDef",
    {
        "webhooks": List["ListWebhookItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PollForJobsOutputTypeDef = TypedDict(
    "PollForJobsOutputTypeDef",
    {"jobs": List["JobTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PollForThirdPartyJobsOutputTypeDef = TypedDict(
    "PollForThirdPartyJobsOutputTypeDef",
    {"jobs": List["ThirdPartyJobTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PutActionRevisionOutputTypeDef = TypedDict(
    "PutActionRevisionOutputTypeDef",
    {"newRevision": bool, "pipelineExecutionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PutApprovalResultOutputTypeDef = TypedDict(
    "PutApprovalResultOutputTypeDef",
    {"approvedAt": datetime, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PutWebhookOutputTypeDef = TypedDict(
    "PutWebhookOutputTypeDef",
    {"webhook": "ListWebhookItemTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RetryStageExecutionOutputTypeDef = TypedDict(
    "RetryStageExecutionOutputTypeDef",
    {"pipelineExecutionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StartPipelineExecutionOutputTypeDef = TypedDict(
    "StartPipelineExecutionOutputTypeDef",
    {"pipelineExecutionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StopPipelineExecutionOutputTypeDef = TypedDict(
    "StopPipelineExecutionOutputTypeDef",
    {"pipelineExecutionId": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdatePipelineOutputTypeDef = TypedDict(
    "UpdatePipelineOutputTypeDef",
    {"pipeline": "PipelineDeclarationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)
