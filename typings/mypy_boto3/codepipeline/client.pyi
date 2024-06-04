"""
Type annotations for codepipeline service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codepipeline import CodePipelineClient

    client: CodePipelineClient = boto3.client("codepipeline")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ActionCategoryType,
    ActionOwnerType,
    StageRetryModeType,
    StageTransitionTypeType,
)
from .paginator import (
    ListActionExecutionsPaginator,
    ListActionTypesPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelinesPaginator,
    ListTagsForResourcePaginator,
    ListWebhooksPaginator,
)
from .type_defs import (
    AcknowledgeJobOutputTypeDef,
    AcknowledgeThirdPartyJobOutputTypeDef,
    ActionConfigurationPropertyTypeDef,
    ActionExecutionFilterTypeDef,
    ActionRevisionTypeDef,
    ActionTypeDeclarationTypeDef,
    ActionTypeIdTypeDef,
    ActionTypeSettingsTypeDef,
    ApprovalResultTypeDef,
    ArtifactDetailsTypeDef,
    CreateCustomActionTypeOutputTypeDef,
    CreatePipelineOutputTypeDef,
    CurrentRevisionTypeDef,
    ExecutionDetailsTypeDef,
    FailureDetailsTypeDef,
    GetActionTypeOutputTypeDef,
    GetJobDetailsOutputTypeDef,
    GetPipelineExecutionOutputTypeDef,
    GetPipelineOutputTypeDef,
    GetPipelineStateOutputTypeDef,
    GetThirdPartyJobDetailsOutputTypeDef,
    ListActionExecutionsOutputTypeDef,
    ListActionTypesOutputTypeDef,
    ListPipelineExecutionsOutputTypeDef,
    ListPipelinesOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWebhooksOutputTypeDef,
    PipelineDeclarationTypeDef,
    PipelineExecutionFilterTypeDef,
    PipelineVariableTypeDef,
    PollForJobsOutputTypeDef,
    PollForThirdPartyJobsOutputTypeDef,
    PutActionRevisionOutputTypeDef,
    PutApprovalResultOutputTypeDef,
    PutWebhookOutputTypeDef,
    RetryStageExecutionOutputTypeDef,
    RollbackStageOutputTypeDef,
    SourceRevisionOverrideTypeDef,
    StartPipelineExecutionOutputTypeDef,
    StopPipelineExecutionOutputTypeDef,
    TagTypeDef,
    UpdatePipelineOutputTypeDef,
    WebhookDefinitionTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CodePipelineClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ActionNotFoundException: Type[BotocoreClientError]
    ActionTypeAlreadyExistsException: Type[BotocoreClientError]
    ActionTypeNotFoundException: Type[BotocoreClientError]
    ApprovalAlreadyCompletedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConcurrentPipelineExecutionsLimitExceededException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DuplicatedStopRequestException: Type[BotocoreClientError]
    InvalidActionDeclarationException: Type[BotocoreClientError]
    InvalidApprovalTokenException: Type[BotocoreClientError]
    InvalidArnException: Type[BotocoreClientError]
    InvalidBlockerDeclarationException: Type[BotocoreClientError]
    InvalidClientTokenException: Type[BotocoreClientError]
    InvalidJobException: Type[BotocoreClientError]
    InvalidJobStateException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidNonceException: Type[BotocoreClientError]
    InvalidStageDeclarationException: Type[BotocoreClientError]
    InvalidStructureException: Type[BotocoreClientError]
    InvalidTagsException: Type[BotocoreClientError]
    InvalidWebhookAuthenticationParametersException: Type[BotocoreClientError]
    InvalidWebhookFilterPatternException: Type[BotocoreClientError]
    JobNotFoundException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotLatestPipelineExecutionException: Type[BotocoreClientError]
    OutputVariablesSizeExceededException: Type[BotocoreClientError]
    PipelineExecutionNotFoundException: Type[BotocoreClientError]
    PipelineExecutionNotStoppableException: Type[BotocoreClientError]
    PipelineExecutionOutdatedException: Type[BotocoreClientError]
    PipelineNameInUseException: Type[BotocoreClientError]
    PipelineNotFoundException: Type[BotocoreClientError]
    PipelineVersionNotFoundException: Type[BotocoreClientError]
    RequestFailedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    StageNotFoundException: Type[BotocoreClientError]
    StageNotRetryableException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnableToRollbackStageException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]
    WebhookNotFoundException: Type[BotocoreClientError]

class CodePipelineClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodePipelineClient exceptions.
        """

    def acknowledge_job(self, *, jobId: str, nonce: str) -> AcknowledgeJobOutputTypeDef:
        """
        Returns information about a specified job and whether that job has been received
        by the job worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#acknowledge_job)
        """

    def acknowledge_third_party_job(
        self, *, jobId: str, nonce: str, clientToken: str
    ) -> AcknowledgeThirdPartyJobOutputTypeDef:
        """
        Confirms a job worker has received the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_third_party_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#acknowledge_third_party_job)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#close)
        """

    def create_custom_action_type(
        self,
        *,
        category: ActionCategoryType,
        provider: str,
        version: str,
        inputArtifactDetails: "ArtifactDetailsTypeDef",
        outputArtifactDetails: "ArtifactDetailsTypeDef",
        settings: "ActionTypeSettingsTypeDef" = None,
        configurationProperties: List["ActionConfigurationPropertyTypeDef"] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateCustomActionTypeOutputTypeDef:
        """
        Creates a new custom action that can be used in all pipelines associated with
        the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.create_custom_action_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#create_custom_action_type)
        """

    def create_pipeline(
        self, *, pipeline: "PipelineDeclarationTypeDef", tags: List["TagTypeDef"] = None
    ) -> CreatePipelineOutputTypeDef:
        """
        Creates a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.create_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#create_pipeline)
        """

    def delete_custom_action_type(
        self, *, category: ActionCategoryType, provider: str, version: str
    ) -> None:
        """
        Marks a custom action as deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.delete_custom_action_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#delete_custom_action_type)
        """

    def delete_pipeline(self, *, name: str) -> None:
        """
        Deletes the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#delete_pipeline)
        """

    def delete_webhook(self, *, name: str) -> Dict[str, Any]:
        """
        Deletes a previously created webhook by name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.delete_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#delete_webhook)
        """

    def deregister_webhook_with_third_party(self, *, webhookName: str = None) -> Dict[str, Any]:
        """
        Removes the connection between the webhook that was created by CodePipeline and
        the external tool with events to be detected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.deregister_webhook_with_third_party)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#deregister_webhook_with_third_party)
        """

    def disable_stage_transition(
        self,
        *,
        pipelineName: str,
        stageName: str,
        transitionType: StageTransitionTypeType,
        reason: str
    ) -> None:
        """
        Prevents artifacts in a pipeline from transitioning to the next stage in the
        pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.disable_stage_transition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#disable_stage_transition)
        """

    def enable_stage_transition(
        self, *, pipelineName: str, stageName: str, transitionType: StageTransitionTypeType
    ) -> None:
        """
        Enables artifacts in a pipeline to transition to a stage in a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.enable_stage_transition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#enable_stage_transition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#generate_presigned_url)
        """

    def get_action_type(
        self, *, category: ActionCategoryType, owner: str, provider: str, version: str
    ) -> GetActionTypeOutputTypeDef:
        """
        Returns information about an action type created for an external provider, where
        the action is to be used by customers of the external provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.get_action_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#get_action_type)
        """

    def get_job_details(self, *, jobId: str) -> GetJobDetailsOutputTypeDef:
        """
        Returns information about a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.get_job_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#get_job_details)
        """

    def get_pipeline(self, *, name: str, version: int = None) -> GetPipelineOutputTypeDef:
        """
        Returns the metadata, structure, stages, and actions of a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#get_pipeline)
        """

    def get_pipeline_execution(
        self, *, pipelineName: str, pipelineExecutionId: str
    ) -> GetPipelineExecutionOutputTypeDef:
        """
        Returns information about an execution of a pipeline, including details about
        artifacts, the pipeline execution ID, and the name, version, and status of the
        pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#get_pipeline_execution)
        """

    def get_pipeline_state(self, *, name: str) -> GetPipelineStateOutputTypeDef:
        """
        Returns information about the state of a pipeline, including the stages and
        actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#get_pipeline_state)
        """

    def get_third_party_job_details(
        self, *, jobId: str, clientToken: str
    ) -> GetThirdPartyJobDetailsOutputTypeDef:
        """
        Requests the details of a job for a third party action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.get_third_party_job_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#get_third_party_job_details)
        """

    def list_action_executions(
        self,
        *,
        pipelineName: str,
        filter: "ActionExecutionFilterTypeDef" = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListActionExecutionsOutputTypeDef:
        """
        Lists the action executions that have occurred in a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.list_action_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#list_action_executions)
        """

    def list_action_types(
        self,
        *,
        actionOwnerFilter: ActionOwnerType = None,
        nextToken: str = None,
        regionFilter: str = None
    ) -> ListActionTypesOutputTypeDef:
        """
        Gets a summary of all CodePipeline action types associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.list_action_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#list_action_types)
        """

    def list_pipeline_executions(
        self,
        *,
        pipelineName: str,
        maxResults: int = None,
        filter: "PipelineExecutionFilterTypeDef" = None,
        nextToken: str = None
    ) -> ListPipelineExecutionsOutputTypeDef:
        """
        Gets a summary of the most recent executions for a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.list_pipeline_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#list_pipeline_executions)
        """

    def list_pipelines(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListPipelinesOutputTypeDef:
        """
        Gets a summary of all of the pipelines associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.list_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#list_pipelines)
        """

    def list_tags_for_resource(
        self, *, resourceArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Gets the set of key-value pairs (metadata) that are used to manage the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#list_tags_for_resource)
        """

    def list_webhooks(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListWebhooksOutputTypeDef:
        """
        Gets a listing of all the webhooks in this Amazon Web Services Region for this
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.list_webhooks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#list_webhooks)
        """

    def poll_for_jobs(
        self,
        *,
        actionTypeId: "ActionTypeIdTypeDef",
        maxBatchSize: int = None,
        queryParam: Dict[str, str] = None
    ) -> PollForJobsOutputTypeDef:
        """
        Returns information about any jobs for CodePipeline to act on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.poll_for_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#poll_for_jobs)
        """

    def poll_for_third_party_jobs(
        self, *, actionTypeId: "ActionTypeIdTypeDef", maxBatchSize: int = None
    ) -> PollForThirdPartyJobsOutputTypeDef:
        """
        Determines whether there are any third party jobs for a job worker to act on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.poll_for_third_party_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#poll_for_third_party_jobs)
        """

    def put_action_revision(
        self,
        *,
        pipelineName: str,
        stageName: str,
        actionName: str,
        actionRevision: "ActionRevisionTypeDef"
    ) -> PutActionRevisionOutputTypeDef:
        """
        Provides information to CodePipeline about new revisions to a source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.put_action_revision)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#put_action_revision)
        """

    def put_approval_result(
        self,
        *,
        pipelineName: str,
        stageName: str,
        actionName: str,
        result: "ApprovalResultTypeDef",
        token: str
    ) -> PutApprovalResultOutputTypeDef:
        """
        Provides the response to a manual approval request to CodePipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.put_approval_result)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#put_approval_result)
        """

    def put_job_failure_result(
        self, *, jobId: str, failureDetails: "FailureDetailsTypeDef"
    ) -> None:
        """
        Represents the failure of a job as returned to the pipeline by a job worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.put_job_failure_result)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#put_job_failure_result)
        """

    def put_job_success_result(
        self,
        *,
        jobId: str,
        currentRevision: "CurrentRevisionTypeDef" = None,
        continuationToken: str = None,
        executionDetails: "ExecutionDetailsTypeDef" = None,
        outputVariables: Dict[str, str] = None
    ) -> None:
        """
        Represents the success of a job as returned to the pipeline by a job worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.put_job_success_result)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#put_job_success_result)
        """

    def put_third_party_job_failure_result(
        self, *, jobId: str, clientToken: str, failureDetails: "FailureDetailsTypeDef"
    ) -> None:
        """
        Represents the failure of a third party job as returned to the pipeline by a job
        worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_failure_result)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#put_third_party_job_failure_result)
        """

    def put_third_party_job_success_result(
        self,
        *,
        jobId: str,
        clientToken: str,
        currentRevision: "CurrentRevisionTypeDef" = None,
        continuationToken: str = None,
        executionDetails: "ExecutionDetailsTypeDef" = None
    ) -> None:
        """
        Represents the success of a third party job as returned to the pipeline by a job
        worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_success_result)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#put_third_party_job_success_result)
        """

    def put_webhook(
        self, *, webhook: "WebhookDefinitionTypeDef", tags: List["TagTypeDef"] = None
    ) -> PutWebhookOutputTypeDef:
        """
        Defines a webhook and returns a unique webhook URL generated by CodePipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.put_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#put_webhook)
        """

    def register_webhook_with_third_party(self, *, webhookName: str = None) -> Dict[str, Any]:
        """
        Configures a connection between the webhook that was created and the external
        tool with events to be detected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.register_webhook_with_third_party)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#register_webhook_with_third_party)
        """

    def retry_stage_execution(
        self,
        *,
        pipelineName: str,
        stageName: str,
        pipelineExecutionId: str,
        retryMode: StageRetryModeType
    ) -> RetryStageExecutionOutputTypeDef:
        """
        You can retry a stage that has failed without having to run a pipeline again
        from the beginning.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.retry_stage_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#retry_stage_execution)
        """

    def rollback_stage(
        self, *, pipelineName: str, stageName: str, targetPipelineExecutionId: str
    ) -> RollbackStageOutputTypeDef:
        """
        Rolls back a stage execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.rollback_stage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#rollback_stage)
        """

    def start_pipeline_execution(
        self,
        *,
        name: str,
        variables: List["PipelineVariableTypeDef"] = None,
        clientRequestToken: str = None,
        sourceRevisions: List["SourceRevisionOverrideTypeDef"] = None
    ) -> StartPipelineExecutionOutputTypeDef:
        """
        Starts the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.start_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#start_pipeline_execution)
        """

    def stop_pipeline_execution(
        self,
        *,
        pipelineName: str,
        pipelineExecutionId: str,
        abandon: bool = None,
        reason: str = None
    ) -> StopPipelineExecutionOutputTypeDef:
        """
        Stops the specified pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.stop_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#stop_pipeline_execution)
        """

    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#untag_resource)
        """

    def update_action_type(self, *, actionType: "ActionTypeDeclarationTypeDef") -> None:
        """
        Updates an action type that was created with any supported integration model,
        where the action type is to be used by customers of the action type provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.update_action_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#update_action_type)
        """

    def update_pipeline(
        self, *, pipeline: "PipelineDeclarationTypeDef"
    ) -> UpdatePipelineOutputTypeDef:
        """
        Updates a specified pipeline with edits or changes to its structure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Client.update_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client.html#update_pipeline)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_action_executions"]
    ) -> ListActionExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators.html#listactionexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_action_types"]
    ) -> ListActionTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators.html#listactiontypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> ListPipelineExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelineExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators.html#listpipelineexecutionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators.html#listpipelinespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Paginator.ListTagsForResource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators.html#listtagsforresourcepaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_webhooks"]) -> ListWebhooksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codepipeline.html#CodePipeline.Paginator.ListWebhooks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/paginators.html#listwebhookspaginator)
        """
