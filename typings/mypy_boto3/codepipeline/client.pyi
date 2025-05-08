"""
Type annotations for codepipeline service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codepipeline.client import CodePipelineClient

    session = Session()
    client: CodePipelineClient = session.client("codepipeline")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListActionExecutionsPaginator,
    ListActionTypesPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelinesPaginator,
    ListRuleExecutionsPaginator,
    ListTagsForResourcePaginator,
    ListWebhooksPaginator,
)
from .type_defs import (
    AcknowledgeJobInputTypeDef,
    AcknowledgeJobOutputTypeDef,
    AcknowledgeThirdPartyJobInputTypeDef,
    AcknowledgeThirdPartyJobOutputTypeDef,
    CreateCustomActionTypeInputTypeDef,
    CreateCustomActionTypeOutputTypeDef,
    CreatePipelineInputTypeDef,
    CreatePipelineOutputTypeDef,
    DeleteCustomActionTypeInputTypeDef,
    DeletePipelineInputTypeDef,
    DeleteWebhookInputTypeDef,
    DeregisterWebhookWithThirdPartyInputTypeDef,
    DisableStageTransitionInputTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableStageTransitionInputTypeDef,
    GetActionTypeInputTypeDef,
    GetActionTypeOutputTypeDef,
    GetJobDetailsInputTypeDef,
    GetJobDetailsOutputTypeDef,
    GetPipelineExecutionInputTypeDef,
    GetPipelineExecutionOutputTypeDef,
    GetPipelineInputTypeDef,
    GetPipelineOutputTypeDef,
    GetPipelineStateInputTypeDef,
    GetPipelineStateOutputTypeDef,
    GetThirdPartyJobDetailsInputTypeDef,
    GetThirdPartyJobDetailsOutputTypeDef,
    ListActionExecutionsInputTypeDef,
    ListActionExecutionsOutputTypeDef,
    ListActionTypesInputTypeDef,
    ListActionTypesOutputTypeDef,
    ListPipelineExecutionsInputTypeDef,
    ListPipelineExecutionsOutputTypeDef,
    ListPipelinesInputTypeDef,
    ListPipelinesOutputTypeDef,
    ListRuleExecutionsInputTypeDef,
    ListRuleExecutionsOutputTypeDef,
    ListRuleTypesInputTypeDef,
    ListRuleTypesOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListWebhooksInputTypeDef,
    ListWebhooksOutputTypeDef,
    OverrideStageConditionInputTypeDef,
    PollForJobsInputTypeDef,
    PollForJobsOutputTypeDef,
    PollForThirdPartyJobsInputTypeDef,
    PollForThirdPartyJobsOutputTypeDef,
    PutActionRevisionInputTypeDef,
    PutActionRevisionOutputTypeDef,
    PutApprovalResultInputTypeDef,
    PutApprovalResultOutputTypeDef,
    PutJobFailureResultInputTypeDef,
    PutJobSuccessResultInputTypeDef,
    PutThirdPartyJobFailureResultInputTypeDef,
    PutThirdPartyJobSuccessResultInputTypeDef,
    PutWebhookInputTypeDef,
    PutWebhookOutputTypeDef,
    RegisterWebhookWithThirdPartyInputTypeDef,
    RetryStageExecutionInputTypeDef,
    RetryStageExecutionOutputTypeDef,
    RollbackStageInputTypeDef,
    RollbackStageOutputTypeDef,
    StartPipelineExecutionInputTypeDef,
    StartPipelineExecutionOutputTypeDef,
    StopPipelineExecutionInputTypeDef,
    StopPipelineExecutionOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateActionTypeInputTypeDef,
    UpdatePipelineInputTypeDef,
    UpdatePipelineOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CodePipelineClient",)

class Exceptions(BaseClientExceptions):
    ActionNotFoundException: Type[BotocoreClientError]
    ActionTypeAlreadyExistsException: Type[BotocoreClientError]
    ActionTypeNotFoundException: Type[BotocoreClientError]
    ApprovalAlreadyCompletedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConcurrentPipelineExecutionsLimitExceededException: Type[BotocoreClientError]
    ConditionNotOverridableException: Type[BotocoreClientError]
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodePipelineClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline.html#CodePipeline.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#generate_presigned_url)
        """

    def acknowledge_job(
        self, **kwargs: Unpack[AcknowledgeJobInputTypeDef]
    ) -> AcknowledgeJobOutputTypeDef:
        """
        Returns information about a specified job and whether that job has been
        received by the job worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/acknowledge_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#acknowledge_job)
        """

    def acknowledge_third_party_job(
        self, **kwargs: Unpack[AcknowledgeThirdPartyJobInputTypeDef]
    ) -> AcknowledgeThirdPartyJobOutputTypeDef:
        """
        Confirms a job worker has received the specified job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/acknowledge_third_party_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#acknowledge_third_party_job)
        """

    def create_custom_action_type(
        self, **kwargs: Unpack[CreateCustomActionTypeInputTypeDef]
    ) -> CreateCustomActionTypeOutputTypeDef:
        """
        Creates a new custom action that can be used in all pipelines associated with
        the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/create_custom_action_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#create_custom_action_type)
        """

    def create_pipeline(
        self, **kwargs: Unpack[CreatePipelineInputTypeDef]
    ) -> CreatePipelineOutputTypeDef:
        """
        Creates a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/create_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#create_pipeline)
        """

    def delete_custom_action_type(
        self, **kwargs: Unpack[DeleteCustomActionTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Marks a custom action as deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/delete_custom_action_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#delete_custom_action_type)
        """

    def delete_pipeline(
        self, **kwargs: Unpack[DeletePipelineInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/delete_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#delete_pipeline)
        """

    def delete_webhook(self, **kwargs: Unpack[DeleteWebhookInputTypeDef]) -> Dict[str, Any]:
        """
        Deletes a previously created webhook by name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/delete_webhook.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#delete_webhook)
        """

    def deregister_webhook_with_third_party(
        self, **kwargs: Unpack[DeregisterWebhookWithThirdPartyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the connection between the webhook that was created by CodePipeline and
        the external tool with events to be detected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/deregister_webhook_with_third_party.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#deregister_webhook_with_third_party)
        """

    def disable_stage_transition(
        self, **kwargs: Unpack[DisableStageTransitionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Prevents artifacts in a pipeline from transitioning to the next stage in the
        pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/disable_stage_transition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#disable_stage_transition)
        """

    def enable_stage_transition(
        self, **kwargs: Unpack[EnableStageTransitionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables artifacts in a pipeline to transition to a stage in a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/enable_stage_transition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#enable_stage_transition)
        """

    def get_action_type(
        self, **kwargs: Unpack[GetActionTypeInputTypeDef]
    ) -> GetActionTypeOutputTypeDef:
        """
        Returns information about an action type created for an external provider,
        where the action is to be used by customers of the external provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_action_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_action_type)
        """

    def get_job_details(
        self, **kwargs: Unpack[GetJobDetailsInputTypeDef]
    ) -> GetJobDetailsOutputTypeDef:
        """
        Returns information about a job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_job_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_job_details)
        """

    def get_pipeline(self, **kwargs: Unpack[GetPipelineInputTypeDef]) -> GetPipelineOutputTypeDef:
        """
        Returns the metadata, structure, stages, and actions of a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_pipeline)
        """

    def get_pipeline_execution(
        self, **kwargs: Unpack[GetPipelineExecutionInputTypeDef]
    ) -> GetPipelineExecutionOutputTypeDef:
        """
        Returns information about an execution of a pipeline, including details about
        artifacts, the pipeline execution ID, and the name, version, and status of the
        pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_pipeline_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_pipeline_execution)
        """

    def get_pipeline_state(
        self, **kwargs: Unpack[GetPipelineStateInputTypeDef]
    ) -> GetPipelineStateOutputTypeDef:
        """
        Returns information about the state of a pipeline, including the stages and
        actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_pipeline_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_pipeline_state)
        """

    def get_third_party_job_details(
        self, **kwargs: Unpack[GetThirdPartyJobDetailsInputTypeDef]
    ) -> GetThirdPartyJobDetailsOutputTypeDef:
        """
        Requests the details of a job for a third party action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_third_party_job_details.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_third_party_job_details)
        """

    def list_action_executions(
        self, **kwargs: Unpack[ListActionExecutionsInputTypeDef]
    ) -> ListActionExecutionsOutputTypeDef:
        """
        Lists the action executions that have occurred in a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/list_action_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#list_action_executions)
        """

    def list_action_types(
        self, **kwargs: Unpack[ListActionTypesInputTypeDef]
    ) -> ListActionTypesOutputTypeDef:
        """
        Gets a summary of all CodePipeline action types associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/list_action_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#list_action_types)
        """

    def list_pipeline_executions(
        self, **kwargs: Unpack[ListPipelineExecutionsInputTypeDef]
    ) -> ListPipelineExecutionsOutputTypeDef:
        """
        Gets a summary of the most recent executions for a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/list_pipeline_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#list_pipeline_executions)
        """

    def list_pipelines(
        self, **kwargs: Unpack[ListPipelinesInputTypeDef]
    ) -> ListPipelinesOutputTypeDef:
        """
        Gets a summary of all of the pipelines associated with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/list_pipelines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#list_pipelines)
        """

    def list_rule_executions(
        self, **kwargs: Unpack[ListRuleExecutionsInputTypeDef]
    ) -> ListRuleExecutionsOutputTypeDef:
        """
        Lists the rule executions that have occurred in a pipeline configured for
        conditions with rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/list_rule_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#list_rule_executions)
        """

    def list_rule_types(
        self, **kwargs: Unpack[ListRuleTypesInputTypeDef]
    ) -> ListRuleTypesOutputTypeDef:
        """
        Lists the rules for the condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/list_rule_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#list_rule_types)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Gets the set of key-value pairs (metadata) that are used to manage the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#list_tags_for_resource)
        """

    def list_webhooks(
        self, **kwargs: Unpack[ListWebhooksInputTypeDef]
    ) -> ListWebhooksOutputTypeDef:
        """
        Gets a listing of all the webhooks in this Amazon Web Services Region for this
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/list_webhooks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#list_webhooks)
        """

    def override_stage_condition(
        self, **kwargs: Unpack[OverrideStageConditionInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used to override a stage condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/override_stage_condition.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#override_stage_condition)
        """

    def poll_for_jobs(self, **kwargs: Unpack[PollForJobsInputTypeDef]) -> PollForJobsOutputTypeDef:
        """
        Returns information about any jobs for CodePipeline to act on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/poll_for_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#poll_for_jobs)
        """

    def poll_for_third_party_jobs(
        self, **kwargs: Unpack[PollForThirdPartyJobsInputTypeDef]
    ) -> PollForThirdPartyJobsOutputTypeDef:
        """
        Determines whether there are any third party jobs for a job worker to act on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/poll_for_third_party_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#poll_for_third_party_jobs)
        """

    def put_action_revision(
        self, **kwargs: Unpack[PutActionRevisionInputTypeDef]
    ) -> PutActionRevisionOutputTypeDef:
        """
        Provides information to CodePipeline about new revisions to a source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/put_action_revision.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#put_action_revision)
        """

    def put_approval_result(
        self, **kwargs: Unpack[PutApprovalResultInputTypeDef]
    ) -> PutApprovalResultOutputTypeDef:
        """
        Provides the response to a manual approval request to CodePipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/put_approval_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#put_approval_result)
        """

    def put_job_failure_result(
        self, **kwargs: Unpack[PutJobFailureResultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Represents the failure of a job as returned to the pipeline by a job worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/put_job_failure_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#put_job_failure_result)
        """

    def put_job_success_result(
        self, **kwargs: Unpack[PutJobSuccessResultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Represents the success of a job as returned to the pipeline by a job worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/put_job_success_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#put_job_success_result)
        """

    def put_third_party_job_failure_result(
        self, **kwargs: Unpack[PutThirdPartyJobFailureResultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Represents the failure of a third party job as returned to the pipeline by a
        job worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/put_third_party_job_failure_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#put_third_party_job_failure_result)
        """

    def put_third_party_job_success_result(
        self, **kwargs: Unpack[PutThirdPartyJobSuccessResultInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Represents the success of a third party job as returned to the pipeline by a
        job worker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/put_third_party_job_success_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#put_third_party_job_success_result)
        """

    def put_webhook(self, **kwargs: Unpack[PutWebhookInputTypeDef]) -> PutWebhookOutputTypeDef:
        """
        Defines a webhook and returns a unique webhook URL generated by CodePipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/put_webhook.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#put_webhook)
        """

    def register_webhook_with_third_party(
        self, **kwargs: Unpack[RegisterWebhookWithThirdPartyInputTypeDef]
    ) -> Dict[str, Any]:
        """
        Configures a connection between the webhook that was created and the external
        tool with events to be detected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/register_webhook_with_third_party.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#register_webhook_with_third_party)
        """

    def retry_stage_execution(
        self, **kwargs: Unpack[RetryStageExecutionInputTypeDef]
    ) -> RetryStageExecutionOutputTypeDef:
        """
        You can retry a stage that has failed without having to run a pipeline again
        from the beginning.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/retry_stage_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#retry_stage_execution)
        """

    def rollback_stage(
        self, **kwargs: Unpack[RollbackStageInputTypeDef]
    ) -> RollbackStageOutputTypeDef:
        """
        Rolls back a stage execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/rollback_stage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#rollback_stage)
        """

    def start_pipeline_execution(
        self, **kwargs: Unpack[StartPipelineExecutionInputTypeDef]
    ) -> StartPipelineExecutionOutputTypeDef:
        """
        Starts the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/start_pipeline_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#start_pipeline_execution)
        """

    def stop_pipeline_execution(
        self, **kwargs: Unpack[StopPipelineExecutionInputTypeDef]
    ) -> StopPipelineExecutionOutputTypeDef:
        """
        Stops the specified pipeline execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/stop_pipeline_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#stop_pipeline_execution)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#untag_resource)
        """

    def update_action_type(
        self, **kwargs: Unpack[UpdateActionTypeInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates an action type that was created with any supported integration model,
        where the action type is to be used by customers of the action type provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/update_action_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#update_action_type)
        """

    def update_pipeline(
        self, **kwargs: Unpack[UpdatePipelineInputTypeDef]
    ) -> UpdatePipelineOutputTypeDef:
        """
        Updates a specified pipeline with edits or changes to its structure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/update_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#update_pipeline)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_action_executions"]
    ) -> ListActionExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_action_types"]
    ) -> ListActionTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> ListPipelineExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pipelines"]
    ) -> ListPipelinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_rule_executions"]
    ) -> ListRuleExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_webhooks"]
    ) -> ListWebhooksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codepipeline/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codepipeline/client/#get_paginator)
        """
