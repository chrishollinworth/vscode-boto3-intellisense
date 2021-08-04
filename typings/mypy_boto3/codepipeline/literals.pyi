"""
Type annotations for codepipeline service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/literals.html)

Usage::

    ```python
    from mypy_boto3_codepipeline.literals import ActionCategoryType

    data: ActionCategoryType = "Approval"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionCategoryType",
    "ActionConfigurationPropertyTypeType",
    "ActionExecutionStatusType",
    "ActionOwnerType",
    "ApprovalStatusType",
    "ArtifactLocationTypeType",
    "ArtifactStoreTypeType",
    "BlockerTypeType",
    "EncryptionKeyTypeType",
    "ExecutorTypeType",
    "FailureTypeType",
    "JobStatusType",
    "ListActionExecutionsPaginatorName",
    "ListActionTypesPaginatorName",
    "ListPipelineExecutionsPaginatorName",
    "ListPipelinesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListWebhooksPaginatorName",
    "PipelineExecutionStatusType",
    "StageExecutionStatusType",
    "StageRetryModeType",
    "StageTransitionTypeType",
    "TriggerTypeType",
    "WebhookAuthenticationTypeType",
)

ActionCategoryType = Literal["Approval", "Build", "Deploy", "Invoke", "Source", "Test"]
ActionConfigurationPropertyTypeType = Literal["Boolean", "Number", "String"]
ActionExecutionStatusType = Literal["Abandoned", "Failed", "InProgress", "Succeeded"]
ActionOwnerType = Literal["AWS", "Custom", "ThirdParty"]
ApprovalStatusType = Literal["Approved", "Rejected"]
ArtifactLocationTypeType = Literal["S3"]
ArtifactStoreTypeType = Literal["S3"]
BlockerTypeType = Literal["Schedule"]
EncryptionKeyTypeType = Literal["KMS"]
ExecutorTypeType = Literal["JobWorker", "Lambda"]
FailureTypeType = Literal[
    "ConfigurationError",
    "JobFailed",
    "PermissionError",
    "RevisionOutOfSync",
    "RevisionUnavailable",
    "SystemUnavailable",
]
JobStatusType = Literal[
    "Created", "Dispatched", "Failed", "InProgress", "Queued", "Succeeded", "TimedOut"
]
ListActionExecutionsPaginatorName = Literal["list_action_executions"]
ListActionTypesPaginatorName = Literal["list_action_types"]
ListPipelineExecutionsPaginatorName = Literal["list_pipeline_executions"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListWebhooksPaginatorName = Literal["list_webhooks"]
PipelineExecutionStatusType = Literal[
    "Cancelled", "Failed", "InProgress", "Stopped", "Stopping", "Succeeded", "Superseded"
]
StageExecutionStatusType = Literal[
    "Cancelled", "Failed", "InProgress", "Stopped", "Stopping", "Succeeded"
]
StageRetryModeType = Literal["FAILED_ACTIONS"]
StageTransitionTypeType = Literal["Inbound", "Outbound"]
TriggerTypeType = Literal[
    "CloudWatchEvent",
    "CreatePipeline",
    "PollForSourceChanges",
    "PutActionRevision",
    "StartPipelineExecution",
    "Webhook",
]
WebhookAuthenticationTypeType = Literal["GITHUB_HMAC", "IP", "UNAUTHENTICATED"]
