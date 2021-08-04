"""
Type annotations for codepipeline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codepipeline.type_defs import AWSSessionCredentialsTypeDef

    data: AWSSessionCredentialsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionCategoryType,
    ActionConfigurationPropertyTypeType,
    ActionExecutionStatusType,
    ActionOwnerType,
    ApprovalStatusType,
    ExecutorTypeType,
    FailureTypeType,
    JobStatusType,
    PipelineExecutionStatusType,
    StageExecutionStatusType,
    StageTransitionTypeType,
    TriggerTypeType,
    WebhookAuthenticationTypeType,
)

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
    "AcknowledgeJobInputRequestTypeDef",
    "AcknowledgeJobOutputTypeDef",
    "AcknowledgeThirdPartyJobInputRequestTypeDef",
    "AcknowledgeThirdPartyJobOutputTypeDef",
    "ActionConfigurationPropertyTypeDef",
    "ActionConfigurationTypeDef",
    "ActionContextTypeDef",
    "ActionDeclarationTypeDef",
    "ActionExecutionDetailTypeDef",
    "ActionExecutionFilterTypeDef",
    "ActionExecutionInputTypeDef",
    "ActionExecutionOutputTypeDef",
    "ActionExecutionResultTypeDef",
    "ActionExecutionTypeDef",
    "ActionRevisionTypeDef",
    "ActionStateTypeDef",
    "ActionTypeArtifactDetailsTypeDef",
    "ActionTypeDeclarationTypeDef",
    "ActionTypeExecutorTypeDef",
    "ActionTypeIdTypeDef",
    "ActionTypeIdentifierTypeDef",
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
    "BlockerDeclarationTypeDef",
    "CreateCustomActionTypeInputRequestTypeDef",
    "CreateCustomActionTypeOutputTypeDef",
    "CreatePipelineInputRequestTypeDef",
    "CreatePipelineOutputTypeDef",
    "CurrentRevisionTypeDef",
    "DeleteCustomActionTypeInputRequestTypeDef",
    "DeletePipelineInputRequestTypeDef",
    "DeleteWebhookInputRequestTypeDef",
    "DeregisterWebhookWithThirdPartyInputRequestTypeDef",
    "DisableStageTransitionInputRequestTypeDef",
    "EnableStageTransitionInputRequestTypeDef",
    "EncryptionKeyTypeDef",
    "ErrorDetailsTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionTriggerTypeDef",
    "ExecutorConfigurationTypeDef",
    "FailureDetailsTypeDef",
    "GetActionTypeInputRequestTypeDef",
    "GetActionTypeOutputTypeDef",
    "GetJobDetailsInputRequestTypeDef",
    "GetJobDetailsOutputTypeDef",
    "GetPipelineExecutionInputRequestTypeDef",
    "GetPipelineExecutionOutputTypeDef",
    "GetPipelineInputRequestTypeDef",
    "GetPipelineOutputTypeDef",
    "GetPipelineStateInputRequestTypeDef",
    "GetPipelineStateOutputTypeDef",
    "GetThirdPartyJobDetailsInputRequestTypeDef",
    "GetThirdPartyJobDetailsOutputTypeDef",
    "InputArtifactTypeDef",
    "JobDataTypeDef",
    "JobDetailsTypeDef",
    "JobTypeDef",
    "JobWorkerExecutorConfigurationTypeDef",
    "LambdaExecutorConfigurationTypeDef",
    "ListActionExecutionsInputRequestTypeDef",
    "ListActionExecutionsOutputTypeDef",
    "ListActionTypesInputRequestTypeDef",
    "ListActionTypesOutputTypeDef",
    "ListPipelineExecutionsInputRequestTypeDef",
    "ListPipelineExecutionsOutputTypeDef",
    "ListPipelinesInputRequestTypeDef",
    "ListPipelinesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWebhookItemTypeDef",
    "ListWebhooksInputRequestTypeDef",
    "ListWebhooksOutputTypeDef",
    "OutputArtifactTypeDef",
    "PaginatorConfigTypeDef",
    "PipelineContextTypeDef",
    "PipelineDeclarationTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineMetadataTypeDef",
    "PipelineSummaryTypeDef",
    "PollForJobsInputRequestTypeDef",
    "PollForJobsOutputTypeDef",
    "PollForThirdPartyJobsInputRequestTypeDef",
    "PollForThirdPartyJobsOutputTypeDef",
    "PutActionRevisionInputRequestTypeDef",
    "PutActionRevisionOutputTypeDef",
    "PutApprovalResultInputRequestTypeDef",
    "PutApprovalResultOutputTypeDef",
    "PutJobFailureResultInputRequestTypeDef",
    "PutJobSuccessResultInputRequestTypeDef",
    "PutThirdPartyJobFailureResultInputRequestTypeDef",
    "PutThirdPartyJobSuccessResultInputRequestTypeDef",
    "PutWebhookInputRequestTypeDef",
    "PutWebhookOutputTypeDef",
    "RegisterWebhookWithThirdPartyInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RetryStageExecutionInputRequestTypeDef",
    "RetryStageExecutionOutputTypeDef",
    "S3ArtifactLocationTypeDef",
    "S3LocationTypeDef",
    "SourceRevisionTypeDef",
    "StageContextTypeDef",
    "StageDeclarationTypeDef",
    "StageExecutionTypeDef",
    "StageStateTypeDef",
    "StartPipelineExecutionInputRequestTypeDef",
    "StartPipelineExecutionOutputTypeDef",
    "StopExecutionTriggerTypeDef",
    "StopPipelineExecutionInputRequestTypeDef",
    "StopPipelineExecutionOutputTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "ThirdPartyJobDataTypeDef",
    "ThirdPartyJobDetailsTypeDef",
    "ThirdPartyJobTypeDef",
    "TransitionStateTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateActionTypeInputRequestTypeDef",
    "UpdatePipelineInputRequestTypeDef",
    "UpdatePipelineOutputTypeDef",
    "WebhookAuthConfigurationTypeDef",
    "WebhookDefinitionTypeDef",
    "WebhookFilterRuleTypeDef",
)

AWSSessionCredentialsTypeDef = TypedDict(
    "AWSSessionCredentialsTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "sessionToken": str,
    },
)

AcknowledgeJobInputRequestTypeDef = TypedDict(
    "AcknowledgeJobInputRequestTypeDef",
    {
        "jobId": str,
        "nonce": str,
    },
)

AcknowledgeJobOutputTypeDef = TypedDict(
    "AcknowledgeJobOutputTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcknowledgeThirdPartyJobInputRequestTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobInputRequestTypeDef",
    {
        "jobId": str,
        "nonce": str,
        "clientToken": str,
    },
)

AcknowledgeThirdPartyJobOutputTypeDef = TypedDict(
    "AcknowledgeThirdPartyJobOutputTypeDef",
    {
        "status": JobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredActionConfigurationPropertyTypeDef = TypedDict(
    "_RequiredActionConfigurationPropertyTypeDef",
    {
        "name": str,
        "required": bool,
        "key": bool,
        "secret": bool,
    },
)
_OptionalActionConfigurationPropertyTypeDef = TypedDict(
    "_OptionalActionConfigurationPropertyTypeDef",
    {
        "queryable": bool,
        "description": str,
        "type": ActionConfigurationPropertyTypeType,
    },
    total=False,
)

class ActionConfigurationPropertyTypeDef(
    _RequiredActionConfigurationPropertyTypeDef, _OptionalActionConfigurationPropertyTypeDef
):
    pass

ActionConfigurationTypeDef = TypedDict(
    "ActionConfigurationTypeDef",
    {
        "configuration": Dict[str, str],
    },
    total=False,
)

ActionContextTypeDef = TypedDict(
    "ActionContextTypeDef",
    {
        "name": str,
        "actionExecutionId": str,
    },
    total=False,
)

_RequiredActionDeclarationTypeDef = TypedDict(
    "_RequiredActionDeclarationTypeDef",
    {
        "name": str,
        "actionTypeId": "ActionTypeIdTypeDef",
    },
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
        "status": ActionExecutionStatusType,
        "input": "ActionExecutionInputTypeDef",
        "output": "ActionExecutionOutputTypeDef",
    },
    total=False,
)

ActionExecutionFilterTypeDef = TypedDict(
    "ActionExecutionFilterTypeDef",
    {
        "pipelineExecutionId": str,
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
    },
    total=False,
)

ActionExecutionResultTypeDef = TypedDict(
    "ActionExecutionResultTypeDef",
    {
        "externalExecutionId": str,
        "externalExecutionSummary": str,
        "externalExecutionUrl": str,
    },
    total=False,
)

ActionExecutionTypeDef = TypedDict(
    "ActionExecutionTypeDef",
    {
        "actionExecutionId": str,
        "status": ActionExecutionStatusType,
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
    "ActionRevisionTypeDef",
    {
        "revisionId": str,
        "revisionChangeId": str,
        "created": datetime,
    },
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

ActionTypeArtifactDetailsTypeDef = TypedDict(
    "ActionTypeArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)

_RequiredActionTypeDeclarationTypeDef = TypedDict(
    "_RequiredActionTypeDeclarationTypeDef",
    {
        "executor": "ActionTypeExecutorTypeDef",
        "id": "ActionTypeIdentifierTypeDef",
        "inputArtifactDetails": "ActionTypeArtifactDetailsTypeDef",
        "outputArtifactDetails": "ActionTypeArtifactDetailsTypeDef",
    },
)
_OptionalActionTypeDeclarationTypeDef = TypedDict(
    "_OptionalActionTypeDeclarationTypeDef",
    {
        "description": str,
        "permissions": "ActionTypePermissionsTypeDef",
        "properties": List["ActionTypePropertyTypeDef"],
        "urls": "ActionTypeUrlsTypeDef",
    },
    total=False,
)

class ActionTypeDeclarationTypeDef(
    _RequiredActionTypeDeclarationTypeDef, _OptionalActionTypeDeclarationTypeDef
):
    pass

_RequiredActionTypeExecutorTypeDef = TypedDict(
    "_RequiredActionTypeExecutorTypeDef",
    {
        "configuration": "ExecutorConfigurationTypeDef",
        "type": ExecutorTypeType,
    },
)
_OptionalActionTypeExecutorTypeDef = TypedDict(
    "_OptionalActionTypeExecutorTypeDef",
    {
        "policyStatementsTemplate": str,
        "jobTimeout": int,
    },
    total=False,
)

class ActionTypeExecutorTypeDef(
    _RequiredActionTypeExecutorTypeDef, _OptionalActionTypeExecutorTypeDef
):
    pass

ActionTypeIdTypeDef = TypedDict(
    "ActionTypeIdTypeDef",
    {
        "category": ActionCategoryType,
        "owner": ActionOwnerType,
        "provider": str,
        "version": str,
    },
)

ActionTypeIdentifierTypeDef = TypedDict(
    "ActionTypeIdentifierTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)

ActionTypePermissionsTypeDef = TypedDict(
    "ActionTypePermissionsTypeDef",
    {
        "allowedAccounts": List[str],
    },
)

_RequiredActionTypePropertyTypeDef = TypedDict(
    "_RequiredActionTypePropertyTypeDef",
    {
        "name": str,
        "optional": bool,
        "key": bool,
        "noEcho": bool,
    },
)
_OptionalActionTypePropertyTypeDef = TypedDict(
    "_OptionalActionTypePropertyTypeDef",
    {
        "queryable": bool,
        "description": str,
    },
    total=False,
)

class ActionTypePropertyTypeDef(
    _RequiredActionTypePropertyTypeDef, _OptionalActionTypePropertyTypeDef
):
    pass

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

ActionTypeUrlsTypeDef = TypedDict(
    "ActionTypeUrlsTypeDef",
    {
        "configurationUrl": str,
        "entityUrlTemplate": str,
        "executionUrlTemplate": str,
        "revisionUrlTemplate": str,
    },
    total=False,
)

ApprovalResultTypeDef = TypedDict(
    "ApprovalResultTypeDef",
    {
        "summary": str,
        "status": ApprovalStatusType,
    },
)

ArtifactDetailTypeDef = TypedDict(
    "ArtifactDetailTypeDef",
    {
        "name": str,
        "s3location": "S3LocationTypeDef",
    },
    total=False,
)

ArtifactDetailsTypeDef = TypedDict(
    "ArtifactDetailsTypeDef",
    {
        "minimumCount": int,
        "maximumCount": int,
    },
)

ArtifactLocationTypeDef = TypedDict(
    "ArtifactLocationTypeDef",
    {
        "type": Literal["S3"],
        "s3Location": "S3ArtifactLocationTypeDef",
    },
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
    "_RequiredArtifactStoreTypeDef",
    {
        "type": Literal["S3"],
        "location": str,
    },
)
_OptionalArtifactStoreTypeDef = TypedDict(
    "_OptionalArtifactStoreTypeDef",
    {
        "encryptionKey": "EncryptionKeyTypeDef",
    },
    total=False,
)

class ArtifactStoreTypeDef(_RequiredArtifactStoreTypeDef, _OptionalArtifactStoreTypeDef):
    pass

ArtifactTypeDef = TypedDict(
    "ArtifactTypeDef",
    {
        "name": str,
        "revision": str,
        "location": "ArtifactLocationTypeDef",
    },
    total=False,
)

BlockerDeclarationTypeDef = TypedDict(
    "BlockerDeclarationTypeDef",
    {
        "name": str,
        "type": Literal["Schedule"],
    },
)

_RequiredCreateCustomActionTypeInputRequestTypeDef = TypedDict(
    "_RequiredCreateCustomActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
        "inputArtifactDetails": "ArtifactDetailsTypeDef",
        "outputArtifactDetails": "ArtifactDetailsTypeDef",
    },
)
_OptionalCreateCustomActionTypeInputRequestTypeDef = TypedDict(
    "_OptionalCreateCustomActionTypeInputRequestTypeDef",
    {
        "settings": "ActionTypeSettingsTypeDef",
        "configurationProperties": List["ActionConfigurationPropertyTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCustomActionTypeInputRequestTypeDef(
    _RequiredCreateCustomActionTypeInputRequestTypeDef,
    _OptionalCreateCustomActionTypeInputRequestTypeDef,
):
    pass

CreateCustomActionTypeOutputTypeDef = TypedDict(
    "CreateCustomActionTypeOutputTypeDef",
    {
        "actionType": "ActionTypeTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePipelineInputRequestTypeDef = TypedDict(
    "_RequiredCreatePipelineInputRequestTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
    },
)
_OptionalCreatePipelineInputRequestTypeDef = TypedDict(
    "_OptionalCreatePipelineInputRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePipelineInputRequestTypeDef(
    _RequiredCreatePipelineInputRequestTypeDef, _OptionalCreatePipelineInputRequestTypeDef
):
    pass

CreatePipelineOutputTypeDef = TypedDict(
    "CreatePipelineOutputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCurrentRevisionTypeDef = TypedDict(
    "_RequiredCurrentRevisionTypeDef",
    {
        "revision": str,
        "changeIdentifier": str,
    },
)
_OptionalCurrentRevisionTypeDef = TypedDict(
    "_OptionalCurrentRevisionTypeDef",
    {
        "created": Union[datetime, str],
        "revisionSummary": str,
    },
    total=False,
)

class CurrentRevisionTypeDef(_RequiredCurrentRevisionTypeDef, _OptionalCurrentRevisionTypeDef):
    pass

DeleteCustomActionTypeInputRequestTypeDef = TypedDict(
    "DeleteCustomActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "provider": str,
        "version": str,
    },
)

DeletePipelineInputRequestTypeDef = TypedDict(
    "DeletePipelineInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteWebhookInputRequestTypeDef = TypedDict(
    "DeleteWebhookInputRequestTypeDef",
    {
        "name": str,
    },
)

DeregisterWebhookWithThirdPartyInputRequestTypeDef = TypedDict(
    "DeregisterWebhookWithThirdPartyInputRequestTypeDef",
    {
        "webhookName": str,
    },
    total=False,
)

DisableStageTransitionInputRequestTypeDef = TypedDict(
    "DisableStageTransitionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
        "reason": str,
    },
)

EnableStageTransitionInputRequestTypeDef = TypedDict(
    "EnableStageTransitionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "transitionType": StageTransitionTypeType,
    },
)

EncryptionKeyTypeDef = TypedDict(
    "EncryptionKeyTypeDef",
    {
        "id": str,
        "type": Literal["KMS"],
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

ExecutionDetailsTypeDef = TypedDict(
    "ExecutionDetailsTypeDef",
    {
        "summary": str,
        "externalExecutionId": str,
        "percentComplete": int,
    },
    total=False,
)

ExecutionTriggerTypeDef = TypedDict(
    "ExecutionTriggerTypeDef",
    {
        "triggerType": TriggerTypeType,
        "triggerDetail": str,
    },
    total=False,
)

ExecutorConfigurationTypeDef = TypedDict(
    "ExecutorConfigurationTypeDef",
    {
        "lambdaExecutorConfiguration": "LambdaExecutorConfigurationTypeDef",
        "jobWorkerExecutorConfiguration": "JobWorkerExecutorConfigurationTypeDef",
    },
    total=False,
)

_RequiredFailureDetailsTypeDef = TypedDict(
    "_RequiredFailureDetailsTypeDef",
    {
        "type": FailureTypeType,
        "message": str,
    },
)
_OptionalFailureDetailsTypeDef = TypedDict(
    "_OptionalFailureDetailsTypeDef",
    {
        "externalExecutionId": str,
    },
    total=False,
)

class FailureDetailsTypeDef(_RequiredFailureDetailsTypeDef, _OptionalFailureDetailsTypeDef):
    pass

GetActionTypeInputRequestTypeDef = TypedDict(
    "GetActionTypeInputRequestTypeDef",
    {
        "category": ActionCategoryType,
        "owner": str,
        "provider": str,
        "version": str,
    },
)

GetActionTypeOutputTypeDef = TypedDict(
    "GetActionTypeOutputTypeDef",
    {
        "actionType": "ActionTypeDeclarationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobDetailsInputRequestTypeDef = TypedDict(
    "GetJobDetailsInputRequestTypeDef",
    {
        "jobId": str,
    },
)

GetJobDetailsOutputTypeDef = TypedDict(
    "GetJobDetailsOutputTypeDef",
    {
        "jobDetails": "JobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineExecutionInputRequestTypeDef = TypedDict(
    "GetPipelineExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
    },
)

GetPipelineExecutionOutputTypeDef = TypedDict(
    "GetPipelineExecutionOutputTypeDef",
    {
        "pipelineExecution": "PipelineExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPipelineInputRequestTypeDef = TypedDict(
    "_RequiredGetPipelineInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalGetPipelineInputRequestTypeDef = TypedDict(
    "_OptionalGetPipelineInputRequestTypeDef",
    {
        "version": int,
    },
    total=False,
)

class GetPipelineInputRequestTypeDef(
    _RequiredGetPipelineInputRequestTypeDef, _OptionalGetPipelineInputRequestTypeDef
):
    pass

GetPipelineOutputTypeDef = TypedDict(
    "GetPipelineOutputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "metadata": "PipelineMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPipelineStateInputRequestTypeDef = TypedDict(
    "GetPipelineStateInputRequestTypeDef",
    {
        "name": str,
    },
)

GetPipelineStateOutputTypeDef = TypedDict(
    "GetPipelineStateOutputTypeDef",
    {
        "pipelineName": str,
        "pipelineVersion": int,
        "stageStates": List["StageStateTypeDef"],
        "created": datetime,
        "updated": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThirdPartyJobDetailsInputRequestTypeDef = TypedDict(
    "GetThirdPartyJobDetailsInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
    },
)

GetThirdPartyJobDetailsOutputTypeDef = TypedDict(
    "GetThirdPartyJobDetailsOutputTypeDef",
    {
        "jobDetails": "ThirdPartyJobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputArtifactTypeDef = TypedDict(
    "InputArtifactTypeDef",
    {
        "name": str,
    },
)

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
    "JobDetailsTypeDef",
    {
        "id": str,
        "data": "JobDataTypeDef",
        "accountId": str,
    },
    total=False,
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "id": str,
        "data": "JobDataTypeDef",
        "nonce": str,
        "accountId": str,
    },
    total=False,
)

JobWorkerExecutorConfigurationTypeDef = TypedDict(
    "JobWorkerExecutorConfigurationTypeDef",
    {
        "pollingAccounts": List[str],
        "pollingServicePrincipals": List[str],
    },
    total=False,
)

LambdaExecutorConfigurationTypeDef = TypedDict(
    "LambdaExecutorConfigurationTypeDef",
    {
        "lambdaFunctionArn": str,
    },
)

_RequiredListActionExecutionsInputRequestTypeDef = TypedDict(
    "_RequiredListActionExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalListActionExecutionsInputRequestTypeDef = TypedDict(
    "_OptionalListActionExecutionsInputRequestTypeDef",
    {
        "filter": "ActionExecutionFilterTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListActionExecutionsInputRequestTypeDef(
    _RequiredListActionExecutionsInputRequestTypeDef,
    _OptionalListActionExecutionsInputRequestTypeDef,
):
    pass

ListActionExecutionsOutputTypeDef = TypedDict(
    "ListActionExecutionsOutputTypeDef",
    {
        "actionExecutionDetails": List["ActionExecutionDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListActionTypesInputRequestTypeDef = TypedDict(
    "ListActionTypesInputRequestTypeDef",
    {
        "actionOwnerFilter": ActionOwnerType,
        "nextToken": str,
        "regionFilter": str,
    },
    total=False,
)

ListActionTypesOutputTypeDef = TypedDict(
    "ListActionTypesOutputTypeDef",
    {
        "actionTypes": List["ActionTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPipelineExecutionsInputRequestTypeDef = TypedDict(
    "_RequiredListPipelineExecutionsInputRequestTypeDef",
    {
        "pipelineName": str,
    },
)
_OptionalListPipelineExecutionsInputRequestTypeDef = TypedDict(
    "_OptionalListPipelineExecutionsInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListPipelineExecutionsInputRequestTypeDef(
    _RequiredListPipelineExecutionsInputRequestTypeDef,
    _OptionalListPipelineExecutionsInputRequestTypeDef,
):
    pass

ListPipelineExecutionsOutputTypeDef = TypedDict(
    "ListPipelineExecutionsOutputTypeDef",
    {
        "pipelineExecutionSummaries": List["PipelineExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesInputRequestTypeDef = TypedDict(
    "ListPipelinesInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListPipelinesOutputTypeDef = TypedDict(
    "ListPipelinesOutputTypeDef",
    {
        "pipelines": List["PipelineSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWebhookItemTypeDef = TypedDict(
    "_RequiredListWebhookItemTypeDef",
    {
        "definition": "WebhookDefinitionTypeDef",
        "url": str,
    },
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

ListWebhooksInputRequestTypeDef = TypedDict(
    "ListWebhooksInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListWebhooksOutputTypeDef = TypedDict(
    "ListWebhooksOutputTypeDef",
    {
        "webhooks": List["ListWebhookItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OutputArtifactTypeDef = TypedDict(
    "OutputArtifactTypeDef",
    {
        "name": str,
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
    {
        "name": str,
        "roleArn": str,
        "stages": List["StageDeclarationTypeDef"],
    },
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
        "status": PipelineExecutionStatusType,
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
        "status": PipelineExecutionStatusType,
        "statusSummary": str,
        "artifactRevisions": List["ArtifactRevisionTypeDef"],
    },
    total=False,
)

PipelineMetadataTypeDef = TypedDict(
    "PipelineMetadataTypeDef",
    {
        "pipelineArn": str,
        "created": datetime,
        "updated": datetime,
    },
    total=False,
)

PipelineSummaryTypeDef = TypedDict(
    "PipelineSummaryTypeDef",
    {
        "name": str,
        "version": int,
        "created": datetime,
        "updated": datetime,
    },
    total=False,
)

_RequiredPollForJobsInputRequestTypeDef = TypedDict(
    "_RequiredPollForJobsInputRequestTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
    },
)
_OptionalPollForJobsInputRequestTypeDef = TypedDict(
    "_OptionalPollForJobsInputRequestTypeDef",
    {
        "maxBatchSize": int,
        "queryParam": Dict[str, str],
    },
    total=False,
)

class PollForJobsInputRequestTypeDef(
    _RequiredPollForJobsInputRequestTypeDef, _OptionalPollForJobsInputRequestTypeDef
):
    pass

PollForJobsOutputTypeDef = TypedDict(
    "PollForJobsOutputTypeDef",
    {
        "jobs": List["JobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPollForThirdPartyJobsInputRequestTypeDef = TypedDict(
    "_RequiredPollForThirdPartyJobsInputRequestTypeDef",
    {
        "actionTypeId": "ActionTypeIdTypeDef",
    },
)
_OptionalPollForThirdPartyJobsInputRequestTypeDef = TypedDict(
    "_OptionalPollForThirdPartyJobsInputRequestTypeDef",
    {
        "maxBatchSize": int,
    },
    total=False,
)

class PollForThirdPartyJobsInputRequestTypeDef(
    _RequiredPollForThirdPartyJobsInputRequestTypeDef,
    _OptionalPollForThirdPartyJobsInputRequestTypeDef,
):
    pass

PollForThirdPartyJobsOutputTypeDef = TypedDict(
    "PollForThirdPartyJobsOutputTypeDef",
    {
        "jobs": List["ThirdPartyJobTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutActionRevisionInputRequestTypeDef = TypedDict(
    "PutActionRevisionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "actionRevision": "ActionRevisionTypeDef",
    },
)

PutActionRevisionOutputTypeDef = TypedDict(
    "PutActionRevisionOutputTypeDef",
    {
        "newRevision": bool,
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutApprovalResultInputRequestTypeDef = TypedDict(
    "PutApprovalResultInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "actionName": str,
        "result": "ApprovalResultTypeDef",
        "token": str,
    },
)

PutApprovalResultOutputTypeDef = TypedDict(
    "PutApprovalResultOutputTypeDef",
    {
        "approvedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutJobFailureResultInputRequestTypeDef = TypedDict(
    "PutJobFailureResultInputRequestTypeDef",
    {
        "jobId": str,
        "failureDetails": "FailureDetailsTypeDef",
    },
)

_RequiredPutJobSuccessResultInputRequestTypeDef = TypedDict(
    "_RequiredPutJobSuccessResultInputRequestTypeDef",
    {
        "jobId": str,
    },
)
_OptionalPutJobSuccessResultInputRequestTypeDef = TypedDict(
    "_OptionalPutJobSuccessResultInputRequestTypeDef",
    {
        "currentRevision": "CurrentRevisionTypeDef",
        "continuationToken": str,
        "executionDetails": "ExecutionDetailsTypeDef",
        "outputVariables": Dict[str, str],
    },
    total=False,
)

class PutJobSuccessResultInputRequestTypeDef(
    _RequiredPutJobSuccessResultInputRequestTypeDef, _OptionalPutJobSuccessResultInputRequestTypeDef
):
    pass

PutThirdPartyJobFailureResultInputRequestTypeDef = TypedDict(
    "PutThirdPartyJobFailureResultInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
        "failureDetails": "FailureDetailsTypeDef",
    },
)

_RequiredPutThirdPartyJobSuccessResultInputRequestTypeDef = TypedDict(
    "_RequiredPutThirdPartyJobSuccessResultInputRequestTypeDef",
    {
        "jobId": str,
        "clientToken": str,
    },
)
_OptionalPutThirdPartyJobSuccessResultInputRequestTypeDef = TypedDict(
    "_OptionalPutThirdPartyJobSuccessResultInputRequestTypeDef",
    {
        "currentRevision": "CurrentRevisionTypeDef",
        "continuationToken": str,
        "executionDetails": "ExecutionDetailsTypeDef",
    },
    total=False,
)

class PutThirdPartyJobSuccessResultInputRequestTypeDef(
    _RequiredPutThirdPartyJobSuccessResultInputRequestTypeDef,
    _OptionalPutThirdPartyJobSuccessResultInputRequestTypeDef,
):
    pass

_RequiredPutWebhookInputRequestTypeDef = TypedDict(
    "_RequiredPutWebhookInputRequestTypeDef",
    {
        "webhook": "WebhookDefinitionTypeDef",
    },
)
_OptionalPutWebhookInputRequestTypeDef = TypedDict(
    "_OptionalPutWebhookInputRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class PutWebhookInputRequestTypeDef(
    _RequiredPutWebhookInputRequestTypeDef, _OptionalPutWebhookInputRequestTypeDef
):
    pass

PutWebhookOutputTypeDef = TypedDict(
    "PutWebhookOutputTypeDef",
    {
        "webhook": "ListWebhookItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterWebhookWithThirdPartyInputRequestTypeDef = TypedDict(
    "RegisterWebhookWithThirdPartyInputRequestTypeDef",
    {
        "webhookName": str,
    },
    total=False,
)

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

RetryStageExecutionInputRequestTypeDef = TypedDict(
    "RetryStageExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "stageName": str,
        "pipelineExecutionId": str,
        "retryMode": Literal["FAILED_ACTIONS"],
    },
)

RetryStageExecutionOutputTypeDef = TypedDict(
    "RetryStageExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ArtifactLocationTypeDef = TypedDict(
    "S3ArtifactLocationTypeDef",
    {
        "bucketName": str,
        "objectKey": str,
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
    total=False,
)

_RequiredSourceRevisionTypeDef = TypedDict(
    "_RequiredSourceRevisionTypeDef",
    {
        "actionName": str,
    },
)
_OptionalSourceRevisionTypeDef = TypedDict(
    "_OptionalSourceRevisionTypeDef",
    {
        "revisionId": str,
        "revisionSummary": str,
        "revisionUrl": str,
    },
    total=False,
)

class SourceRevisionTypeDef(_RequiredSourceRevisionTypeDef, _OptionalSourceRevisionTypeDef):
    pass

StageContextTypeDef = TypedDict(
    "StageContextTypeDef",
    {
        "name": str,
    },
    total=False,
)

_RequiredStageDeclarationTypeDef = TypedDict(
    "_RequiredStageDeclarationTypeDef",
    {
        "name": str,
        "actions": List["ActionDeclarationTypeDef"],
    },
)
_OptionalStageDeclarationTypeDef = TypedDict(
    "_OptionalStageDeclarationTypeDef",
    {
        "blockers": List["BlockerDeclarationTypeDef"],
    },
    total=False,
)

class StageDeclarationTypeDef(_RequiredStageDeclarationTypeDef, _OptionalStageDeclarationTypeDef):
    pass

StageExecutionTypeDef = TypedDict(
    "StageExecutionTypeDef",
    {
        "pipelineExecutionId": str,
        "status": StageExecutionStatusType,
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

_RequiredStartPipelineExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStartPipelineExecutionInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalStartPipelineExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStartPipelineExecutionInputRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class StartPipelineExecutionInputRequestTypeDef(
    _RequiredStartPipelineExecutionInputRequestTypeDef,
    _OptionalStartPipelineExecutionInputRequestTypeDef,
):
    pass

StartPipelineExecutionOutputTypeDef = TypedDict(
    "StartPipelineExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopExecutionTriggerTypeDef = TypedDict(
    "StopExecutionTriggerTypeDef",
    {
        "reason": str,
    },
    total=False,
)

_RequiredStopPipelineExecutionInputRequestTypeDef = TypedDict(
    "_RequiredStopPipelineExecutionInputRequestTypeDef",
    {
        "pipelineName": str,
        "pipelineExecutionId": str,
    },
)
_OptionalStopPipelineExecutionInputRequestTypeDef = TypedDict(
    "_OptionalStopPipelineExecutionInputRequestTypeDef",
    {
        "abandon": bool,
        "reason": str,
    },
    total=False,
)

class StopPipelineExecutionInputRequestTypeDef(
    _RequiredStopPipelineExecutionInputRequestTypeDef,
    _OptionalStopPipelineExecutionInputRequestTypeDef,
):
    pass

StopPipelineExecutionOutputTypeDef = TypedDict(
    "StopPipelineExecutionOutputTypeDef",
    {
        "pipelineExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

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
    {
        "id": str,
        "data": "ThirdPartyJobDataTypeDef",
        "nonce": str,
    },
    total=False,
)

ThirdPartyJobTypeDef = TypedDict(
    "ThirdPartyJobTypeDef",
    {
        "clientId": str,
        "jobId": str,
    },
    total=False,
)

TransitionStateTypeDef = TypedDict(
    "TransitionStateTypeDef",
    {
        "enabled": bool,
        "lastChangedBy": str,
        "lastChangedAt": datetime,
        "disabledReason": str,
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateActionTypeInputRequestTypeDef = TypedDict(
    "UpdateActionTypeInputRequestTypeDef",
    {
        "actionType": "ActionTypeDeclarationTypeDef",
    },
)

UpdatePipelineInputRequestTypeDef = TypedDict(
    "UpdatePipelineInputRequestTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
    },
)

UpdatePipelineOutputTypeDef = TypedDict(
    "UpdatePipelineOutputTypeDef",
    {
        "pipeline": "PipelineDeclarationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WebhookAuthConfigurationTypeDef = TypedDict(
    "WebhookAuthConfigurationTypeDef",
    {
        "AllowedIPRange": str,
        "SecretToken": str,
    },
    total=False,
)

WebhookDefinitionTypeDef = TypedDict(
    "WebhookDefinitionTypeDef",
    {
        "name": str,
        "targetPipeline": str,
        "targetAction": str,
        "filters": List["WebhookFilterRuleTypeDef"],
        "authentication": WebhookAuthenticationTypeType,
        "authenticationConfiguration": "WebhookAuthConfigurationTypeDef",
    },
)

_RequiredWebhookFilterRuleTypeDef = TypedDict(
    "_RequiredWebhookFilterRuleTypeDef",
    {
        "jsonPath": str,
    },
)
_OptionalWebhookFilterRuleTypeDef = TypedDict(
    "_OptionalWebhookFilterRuleTypeDef",
    {
        "matchEquals": str,
    },
    total=False,
)

class WebhookFilterRuleTypeDef(
    _RequiredWebhookFilterRuleTypeDef, _OptionalWebhookFilterRuleTypeDef
):
    pass
