# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for codepipeline service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codepipeline import CodePipelineClient

    client: CodePipelineClient = boto3.client("codepipeline")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codepipeline.paginator import (
    ListActionExecutionsPaginator,
    ListActionTypesPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelinesPaginator,
    ListTagsForResourcePaginator,
    ListWebhooksPaginator,
)
from mypy_boto3_codepipeline.type_defs import (
    AcknowledgeJobOutputTypeDef,
    AcknowledgeThirdPartyJobOutputTypeDef,
    ActionConfigurationPropertyTypeDef,
    ActionExecutionFilterTypeDef,
    ActionRevisionTypeDef,
    ActionTypeIdTypeDef,
    ActionTypeSettingsTypeDef,
    ApprovalResultTypeDef,
    ArtifactDetailsTypeDef,
    CreateCustomActionTypeOutputTypeDef,
    CreatePipelineOutputTypeDef,
    CurrentRevisionTypeDef,
    ExecutionDetailsTypeDef,
    FailureDetailsTypeDef,
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
    PollForJobsOutputTypeDef,
    PollForThirdPartyJobsOutputTypeDef,
    PutActionRevisionOutputTypeDef,
    PutApprovalResultOutputTypeDef,
    PutWebhookOutputTypeDef,
    RetryStageExecutionOutputTypeDef,
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


class Exceptions:
    ActionNotFoundException: Type[Boto3ClientError]
    ActionTypeNotFoundException: Type[Boto3ClientError]
    ApprovalAlreadyCompletedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConcurrentModificationException: Type[Boto3ClientError]
    DuplicatedStopRequestException: Type[Boto3ClientError]
    InvalidActionDeclarationException: Type[Boto3ClientError]
    InvalidApprovalTokenException: Type[Boto3ClientError]
    InvalidArnException: Type[Boto3ClientError]
    InvalidBlockerDeclarationException: Type[Boto3ClientError]
    InvalidClientTokenException: Type[Boto3ClientError]
    InvalidJobException: Type[Boto3ClientError]
    InvalidJobStateException: Type[Boto3ClientError]
    InvalidNextTokenException: Type[Boto3ClientError]
    InvalidNonceException: Type[Boto3ClientError]
    InvalidStageDeclarationException: Type[Boto3ClientError]
    InvalidStructureException: Type[Boto3ClientError]
    InvalidTagsException: Type[Boto3ClientError]
    InvalidWebhookAuthenticationParametersException: Type[Boto3ClientError]
    InvalidWebhookFilterPatternException: Type[Boto3ClientError]
    JobNotFoundException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    NotLatestPipelineExecutionException: Type[Boto3ClientError]
    OutputVariablesSizeExceededException: Type[Boto3ClientError]
    PipelineExecutionNotFoundException: Type[Boto3ClientError]
    PipelineExecutionNotStoppableException: Type[Boto3ClientError]
    PipelineNameInUseException: Type[Boto3ClientError]
    PipelineNotFoundException: Type[Boto3ClientError]
    PipelineVersionNotFoundException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    StageNotFoundException: Type[Boto3ClientError]
    StageNotRetryableException: Type[Boto3ClientError]
    TooManyTagsException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]
    WebhookNotFoundException: Type[Boto3ClientError]


class CodePipelineClient:
    """
    [CodePipeline.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client)
    """

    exceptions: Exceptions

    def acknowledge_job(self, jobId: str, nonce: str) -> AcknowledgeJobOutputTypeDef:
        """
        [Client.acknowledge_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_job)
        """

    def acknowledge_third_party_job(
        self, jobId: str, nonce: str, clientToken: str
    ) -> AcknowledgeThirdPartyJobOutputTypeDef:
        """
        [Client.acknowledge_third_party_job documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.acknowledge_third_party_job)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.can_paginate)
        """

    def create_custom_action_type(
        self,
        category: Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        provider: str,
        version: str,
        inputArtifactDetails: "ArtifactDetailsTypeDef",
        outputArtifactDetails: "ArtifactDetailsTypeDef",
        settings: "ActionTypeSettingsTypeDef" = None,
        configurationProperties: List["ActionConfigurationPropertyTypeDef"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateCustomActionTypeOutputTypeDef:
        """
        [Client.create_custom_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.create_custom_action_type)
        """

    def create_pipeline(
        self, pipeline: "PipelineDeclarationTypeDef", tags: List["TagTypeDef"] = None
    ) -> CreatePipelineOutputTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.create_pipeline)
        """

    def delete_custom_action_type(
        self,
        category: Literal["Source", "Build", "Deploy", "Test", "Invoke", "Approval"],
        provider: str,
        version: str,
    ) -> None:
        """
        [Client.delete_custom_action_type documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.delete_custom_action_type)
        """

    def delete_pipeline(self, name: str) -> None:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.delete_pipeline)
        """

    def delete_webhook(self, name: str) -> Dict[str, Any]:
        """
        [Client.delete_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.delete_webhook)
        """

    def deregister_webhook_with_third_party(self, webhookName: str = None) -> Dict[str, Any]:
        """
        [Client.deregister_webhook_with_third_party documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.deregister_webhook_with_third_party)
        """

    def disable_stage_transition(
        self,
        pipelineName: str,
        stageName: str,
        transitionType: Literal["Inbound", "Outbound"],
        reason: str,
    ) -> None:
        """
        [Client.disable_stage_transition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.disable_stage_transition)
        """

    def enable_stage_transition(
        self, pipelineName: str, stageName: str, transitionType: Literal["Inbound", "Outbound"]
    ) -> None:
        """
        [Client.enable_stage_transition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.enable_stage_transition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.generate_presigned_url)
        """

    def get_job_details(self, jobId: str) -> GetJobDetailsOutputTypeDef:
        """
        [Client.get_job_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.get_job_details)
        """

    def get_pipeline(self, name: str, version: int = None) -> GetPipelineOutputTypeDef:
        """
        [Client.get_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline)
        """

    def get_pipeline_execution(
        self, pipelineName: str, pipelineExecutionId: str
    ) -> GetPipelineExecutionOutputTypeDef:
        """
        [Client.get_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_execution)
        """

    def get_pipeline_state(self, name: str) -> GetPipelineStateOutputTypeDef:
        """
        [Client.get_pipeline_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.get_pipeline_state)
        """

    def get_third_party_job_details(
        self, jobId: str, clientToken: str
    ) -> GetThirdPartyJobDetailsOutputTypeDef:
        """
        [Client.get_third_party_job_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.get_third_party_job_details)
        """

    def list_action_executions(
        self,
        pipelineName: str,
        filter: ActionExecutionFilterTypeDef = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListActionExecutionsOutputTypeDef:
        """
        [Client.list_action_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.list_action_executions)
        """

    def list_action_types(
        self,
        actionOwnerFilter: Literal["AWS", "ThirdParty", "Custom"] = None,
        nextToken: str = None,
    ) -> ListActionTypesOutputTypeDef:
        """
        [Client.list_action_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.list_action_types)
        """

    def list_pipeline_executions(
        self, pipelineName: str, maxResults: int = None, nextToken: str = None
    ) -> ListPipelineExecutionsOutputTypeDef:
        """
        [Client.list_pipeline_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.list_pipeline_executions)
        """

    def list_pipelines(self, nextToken: str = None) -> ListPipelinesOutputTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.list_pipelines)
        """

    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.list_tags_for_resource)
        """

    def list_webhooks(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListWebhooksOutputTypeDef:
        """
        [Client.list_webhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.list_webhooks)
        """

    def poll_for_jobs(
        self,
        actionTypeId: "ActionTypeIdTypeDef",
        maxBatchSize: int = None,
        queryParam: Dict[str, str] = None,
    ) -> PollForJobsOutputTypeDef:
        """
        [Client.poll_for_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.poll_for_jobs)
        """

    def poll_for_third_party_jobs(
        self, actionTypeId: "ActionTypeIdTypeDef", maxBatchSize: int = None
    ) -> PollForThirdPartyJobsOutputTypeDef:
        """
        [Client.poll_for_third_party_jobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.poll_for_third_party_jobs)
        """

    def put_action_revision(
        self,
        pipelineName: str,
        stageName: str,
        actionName: str,
        actionRevision: "ActionRevisionTypeDef",
    ) -> PutActionRevisionOutputTypeDef:
        """
        [Client.put_action_revision documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.put_action_revision)
        """

    def put_approval_result(
        self,
        pipelineName: str,
        stageName: str,
        actionName: str,
        result: ApprovalResultTypeDef,
        token: str,
    ) -> PutApprovalResultOutputTypeDef:
        """
        [Client.put_approval_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.put_approval_result)
        """

    def put_job_failure_result(self, jobId: str, failureDetails: FailureDetailsTypeDef) -> None:
        """
        [Client.put_job_failure_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.put_job_failure_result)
        """

    def put_job_success_result(
        self,
        jobId: str,
        currentRevision: CurrentRevisionTypeDef = None,
        continuationToken: str = None,
        executionDetails: ExecutionDetailsTypeDef = None,
        outputVariables: Dict[str, str] = None,
    ) -> None:
        """
        [Client.put_job_success_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.put_job_success_result)
        """

    def put_third_party_job_failure_result(
        self, jobId: str, clientToken: str, failureDetails: FailureDetailsTypeDef
    ) -> None:
        """
        [Client.put_third_party_job_failure_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_failure_result)
        """

    def put_third_party_job_success_result(
        self,
        jobId: str,
        clientToken: str,
        currentRevision: CurrentRevisionTypeDef = None,
        continuationToken: str = None,
        executionDetails: ExecutionDetailsTypeDef = None,
    ) -> None:
        """
        [Client.put_third_party_job_success_result documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.put_third_party_job_success_result)
        """

    def put_webhook(
        self, webhook: "WebhookDefinitionTypeDef", tags: List["TagTypeDef"] = None
    ) -> PutWebhookOutputTypeDef:
        """
        [Client.put_webhook documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.put_webhook)
        """

    def register_webhook_with_third_party(self, webhookName: str = None) -> Dict[str, Any]:
        """
        [Client.register_webhook_with_third_party documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.register_webhook_with_third_party)
        """

    def retry_stage_execution(
        self,
        pipelineName: str,
        stageName: str,
        pipelineExecutionId: str,
        retryMode: Literal["FAILED_ACTIONS"],
    ) -> RetryStageExecutionOutputTypeDef:
        """
        [Client.retry_stage_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.retry_stage_execution)
        """

    def start_pipeline_execution(
        self, name: str, clientRequestToken: str = None
    ) -> StartPipelineExecutionOutputTypeDef:
        """
        [Client.start_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.start_pipeline_execution)
        """

    def stop_pipeline_execution(
        self, pipelineName: str, pipelineExecutionId: str, abandon: bool = None, reason: str = None
    ) -> StopPipelineExecutionOutputTypeDef:
        """
        [Client.stop_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.stop_pipeline_execution)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.untag_resource)
        """

    def update_pipeline(
        self, pipeline: "PipelineDeclarationTypeDef"
    ) -> UpdatePipelineOutputTypeDef:
        """
        [Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Client.update_pipeline)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_action_executions"]
    ) -> ListActionExecutionsPaginator:
        """
        [Paginator.ListActionExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_action_types"]
    ) -> ListActionTypesPaginator:
        """
        [Paginator.ListActionTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Paginator.ListActionTypes)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> ListPipelineExecutionsPaginator:
        """
        [Paginator.ListPipelineExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelineExecutions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Paginator.ListPipelines)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_webhooks"]) -> ListWebhooksPaginator:
        """
        [Paginator.ListWebhooks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codepipeline.html#CodePipeline.Paginator.ListWebhooks)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
