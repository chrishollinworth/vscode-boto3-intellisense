"""
Type annotations for bedrock service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock.client import BedrockClient

    session = Session()
    client: BedrockClient = session.client("bedrock")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListAutomatedReasoningPoliciesPaginator,
    ListAutomatedReasoningPolicyBuildWorkflowsPaginator,
    ListAutomatedReasoningPolicyTestCasesPaginator,
    ListAutomatedReasoningPolicyTestResultsPaginator,
    ListCustomModelDeploymentsPaginator,
    ListCustomModelsPaginator,
    ListEnforcedGuardrailsConfigurationPaginator,
    ListEvaluationJobsPaginator,
    ListGuardrailsPaginator,
    ListImportedModelsPaginator,
    ListInferenceProfilesPaginator,
    ListMarketplaceModelEndpointsPaginator,
    ListModelCopyJobsPaginator,
    ListModelCustomizationJobsPaginator,
    ListModelImportJobsPaginator,
    ListModelInvocationJobsPaginator,
    ListPromptRoutersPaginator,
    ListProvisionedModelThroughputsPaginator,
)
from .type_defs import (
    BatchDeleteEvaluationJobRequestTypeDef,
    BatchDeleteEvaluationJobResponseTypeDef,
    CancelAutomatedReasoningPolicyBuildWorkflowRequestTypeDef,
    CreateAutomatedReasoningPolicyRequestTypeDef,
    CreateAutomatedReasoningPolicyResponseTypeDef,
    CreateAutomatedReasoningPolicyTestCaseRequestTypeDef,
    CreateAutomatedReasoningPolicyTestCaseResponseTypeDef,
    CreateAutomatedReasoningPolicyVersionRequestTypeDef,
    CreateAutomatedReasoningPolicyVersionResponseTypeDef,
    CreateCustomModelDeploymentRequestTypeDef,
    CreateCustomModelDeploymentResponseTypeDef,
    CreateCustomModelRequestTypeDef,
    CreateCustomModelResponseTypeDef,
    CreateEvaluationJobRequestTypeDef,
    CreateEvaluationJobResponseTypeDef,
    CreateFoundationModelAgreementRequestTypeDef,
    CreateFoundationModelAgreementResponseTypeDef,
    CreateGuardrailRequestTypeDef,
    CreateGuardrailResponseTypeDef,
    CreateGuardrailVersionRequestTypeDef,
    CreateGuardrailVersionResponseTypeDef,
    CreateInferenceProfileRequestTypeDef,
    CreateInferenceProfileResponseTypeDef,
    CreateMarketplaceModelEndpointRequestTypeDef,
    CreateMarketplaceModelEndpointResponseTypeDef,
    CreateModelCopyJobRequestTypeDef,
    CreateModelCopyJobResponseTypeDef,
    CreateModelCustomizationJobRequestTypeDef,
    CreateModelCustomizationJobResponseTypeDef,
    CreateModelImportJobRequestTypeDef,
    CreateModelImportJobResponseTypeDef,
    CreateModelInvocationJobRequestTypeDef,
    CreateModelInvocationJobResponseTypeDef,
    CreatePromptRouterRequestTypeDef,
    CreatePromptRouterResponseTypeDef,
    CreateProvisionedModelThroughputRequestTypeDef,
    CreateProvisionedModelThroughputResponseTypeDef,
    DeleteAutomatedReasoningPolicyBuildWorkflowRequestTypeDef,
    DeleteAutomatedReasoningPolicyRequestTypeDef,
    DeleteAutomatedReasoningPolicyTestCaseRequestTypeDef,
    DeleteCustomModelDeploymentRequestTypeDef,
    DeleteCustomModelRequestTypeDef,
    DeleteEnforcedGuardrailConfigurationRequestTypeDef,
    DeleteFoundationModelAgreementRequestTypeDef,
    DeleteGuardrailRequestTypeDef,
    DeleteImportedModelRequestTypeDef,
    DeleteInferenceProfileRequestTypeDef,
    DeleteMarketplaceModelEndpointRequestTypeDef,
    DeletePromptRouterRequestTypeDef,
    DeleteProvisionedModelThroughputRequestTypeDef,
    DeregisterMarketplaceModelEndpointRequestTypeDef,
    ExportAutomatedReasoningPolicyVersionRequestTypeDef,
    ExportAutomatedReasoningPolicyVersionResponseTypeDef,
    GetAutomatedReasoningPolicyAnnotationsRequestTypeDef,
    GetAutomatedReasoningPolicyAnnotationsResponseTypeDef,
    GetAutomatedReasoningPolicyBuildWorkflowRequestTypeDef,
    GetAutomatedReasoningPolicyBuildWorkflowResponseTypeDef,
    GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequestTypeDef,
    GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponseTypeDef,
    GetAutomatedReasoningPolicyNextScenarioRequestTypeDef,
    GetAutomatedReasoningPolicyNextScenarioResponseTypeDef,
    GetAutomatedReasoningPolicyRequestTypeDef,
    GetAutomatedReasoningPolicyResponseTypeDef,
    GetAutomatedReasoningPolicyTestCaseRequestTypeDef,
    GetAutomatedReasoningPolicyTestCaseResponseTypeDef,
    GetAutomatedReasoningPolicyTestResultRequestTypeDef,
    GetAutomatedReasoningPolicyTestResultResponseTypeDef,
    GetCustomModelDeploymentRequestTypeDef,
    GetCustomModelDeploymentResponseTypeDef,
    GetCustomModelRequestTypeDef,
    GetCustomModelResponseTypeDef,
    GetEvaluationJobRequestTypeDef,
    GetEvaluationJobResponseTypeDef,
    GetFoundationModelAvailabilityRequestTypeDef,
    GetFoundationModelAvailabilityResponseTypeDef,
    GetFoundationModelRequestTypeDef,
    GetFoundationModelResponseTypeDef,
    GetGuardrailRequestTypeDef,
    GetGuardrailResponseTypeDef,
    GetImportedModelRequestTypeDef,
    GetImportedModelResponseTypeDef,
    GetInferenceProfileRequestTypeDef,
    GetInferenceProfileResponseTypeDef,
    GetMarketplaceModelEndpointRequestTypeDef,
    GetMarketplaceModelEndpointResponseTypeDef,
    GetModelCopyJobRequestTypeDef,
    GetModelCopyJobResponseTypeDef,
    GetModelCustomizationJobRequestTypeDef,
    GetModelCustomizationJobResponseTypeDef,
    GetModelImportJobRequestTypeDef,
    GetModelImportJobResponseTypeDef,
    GetModelInvocationJobRequestTypeDef,
    GetModelInvocationJobResponseTypeDef,
    GetModelInvocationLoggingConfigurationResponseTypeDef,
    GetPromptRouterRequestTypeDef,
    GetPromptRouterResponseTypeDef,
    GetProvisionedModelThroughputRequestTypeDef,
    GetProvisionedModelThroughputResponseTypeDef,
    GetUseCaseForModelAccessResponseTypeDef,
    ListAutomatedReasoningPoliciesRequestTypeDef,
    ListAutomatedReasoningPoliciesResponseTypeDef,
    ListAutomatedReasoningPolicyBuildWorkflowsRequestTypeDef,
    ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef,
    ListAutomatedReasoningPolicyTestCasesRequestTypeDef,
    ListAutomatedReasoningPolicyTestCasesResponseTypeDef,
    ListAutomatedReasoningPolicyTestResultsRequestTypeDef,
    ListAutomatedReasoningPolicyTestResultsResponseTypeDef,
    ListCustomModelDeploymentsRequestTypeDef,
    ListCustomModelDeploymentsResponseTypeDef,
    ListCustomModelsRequestTypeDef,
    ListCustomModelsResponseTypeDef,
    ListEnforcedGuardrailsConfigurationRequestTypeDef,
    ListEnforcedGuardrailsConfigurationResponseTypeDef,
    ListEvaluationJobsRequestTypeDef,
    ListEvaluationJobsResponseTypeDef,
    ListFoundationModelAgreementOffersRequestTypeDef,
    ListFoundationModelAgreementOffersResponseTypeDef,
    ListFoundationModelsRequestTypeDef,
    ListFoundationModelsResponseTypeDef,
    ListGuardrailsRequestTypeDef,
    ListGuardrailsResponseTypeDef,
    ListImportedModelsRequestTypeDef,
    ListImportedModelsResponseTypeDef,
    ListInferenceProfilesRequestTypeDef,
    ListInferenceProfilesResponseTypeDef,
    ListMarketplaceModelEndpointsRequestTypeDef,
    ListMarketplaceModelEndpointsResponseTypeDef,
    ListModelCopyJobsRequestTypeDef,
    ListModelCopyJobsResponseTypeDef,
    ListModelCustomizationJobsRequestTypeDef,
    ListModelCustomizationJobsResponseTypeDef,
    ListModelImportJobsRequestTypeDef,
    ListModelImportJobsResponseTypeDef,
    ListModelInvocationJobsRequestTypeDef,
    ListModelInvocationJobsResponseTypeDef,
    ListPromptRoutersRequestTypeDef,
    ListPromptRoutersResponseTypeDef,
    ListProvisionedModelThroughputsRequestTypeDef,
    ListProvisionedModelThroughputsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutEnforcedGuardrailConfigurationRequestTypeDef,
    PutEnforcedGuardrailConfigurationResponseTypeDef,
    PutModelInvocationLoggingConfigurationRequestTypeDef,
    PutUseCaseForModelAccessRequestTypeDef,
    RegisterMarketplaceModelEndpointRequestTypeDef,
    RegisterMarketplaceModelEndpointResponseTypeDef,
    StartAutomatedReasoningPolicyBuildWorkflowRequestTypeDef,
    StartAutomatedReasoningPolicyBuildWorkflowResponseTypeDef,
    StartAutomatedReasoningPolicyTestWorkflowRequestTypeDef,
    StartAutomatedReasoningPolicyTestWorkflowResponseTypeDef,
    StopEvaluationJobRequestTypeDef,
    StopModelCustomizationJobRequestTypeDef,
    StopModelInvocationJobRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAutomatedReasoningPolicyAnnotationsRequestTypeDef,
    UpdateAutomatedReasoningPolicyAnnotationsResponseTypeDef,
    UpdateAutomatedReasoningPolicyRequestTypeDef,
    UpdateAutomatedReasoningPolicyResponseTypeDef,
    UpdateAutomatedReasoningPolicyTestCaseRequestTypeDef,
    UpdateAutomatedReasoningPolicyTestCaseResponseTypeDef,
    UpdateCustomModelDeploymentRequestTypeDef,
    UpdateCustomModelDeploymentResponseTypeDef,
    UpdateGuardrailRequestTypeDef,
    UpdateGuardrailResponseTypeDef,
    UpdateMarketplaceModelEndpointRequestTypeDef,
    UpdateMarketplaceModelEndpointResponseTypeDef,
    UpdateProvisionedModelThroughputRequestTypeDef,
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

__all__ = ("BedrockClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BedrockClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#Bedrock.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BedrockClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html#Bedrock.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#generate_presigned_url)
        """

    def batch_delete_evaluation_job(
        self, **kwargs: Unpack[BatchDeleteEvaluationJobRequestTypeDef]
    ) -> BatchDeleteEvaluationJobResponseTypeDef:
        """
        Deletes a batch of evaluation jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/batch_delete_evaluation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#batch_delete_evaluation_job)
        """

    def cancel_automated_reasoning_policy_build_workflow(
        self, **kwargs: Unpack[CancelAutomatedReasoningPolicyBuildWorkflowRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels a running Automated Reasoning policy build workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/cancel_automated_reasoning_policy_build_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#cancel_automated_reasoning_policy_build_workflow)
        """

    def create_automated_reasoning_policy(
        self, **kwargs: Unpack[CreateAutomatedReasoningPolicyRequestTypeDef]
    ) -> CreateAutomatedReasoningPolicyResponseTypeDef:
        """
        Creates an Automated Reasoning policy for Amazon Bedrock Guardrails.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_automated_reasoning_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_automated_reasoning_policy)
        """

    def create_automated_reasoning_policy_test_case(
        self, **kwargs: Unpack[CreateAutomatedReasoningPolicyTestCaseRequestTypeDef]
    ) -> CreateAutomatedReasoningPolicyTestCaseResponseTypeDef:
        """
        Creates a test for an Automated Reasoning policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_automated_reasoning_policy_test_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_automated_reasoning_policy_test_case)
        """

    def create_automated_reasoning_policy_version(
        self, **kwargs: Unpack[CreateAutomatedReasoningPolicyVersionRequestTypeDef]
    ) -> CreateAutomatedReasoningPolicyVersionResponseTypeDef:
        """
        Creates a new version of an existing Automated Reasoning policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_automated_reasoning_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_automated_reasoning_policy_version)
        """

    def create_custom_model(
        self, **kwargs: Unpack[CreateCustomModelRequestTypeDef]
    ) -> CreateCustomModelResponseTypeDef:
        """
        Creates a new custom model in Amazon Bedrock.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_custom_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_custom_model)
        """

    def create_custom_model_deployment(
        self, **kwargs: Unpack[CreateCustomModelDeploymentRequestTypeDef]
    ) -> CreateCustomModelDeploymentResponseTypeDef:
        """
        Deploys a custom model for on-demand inference in Amazon Bedrock.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_custom_model_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_custom_model_deployment)
        """

    def create_evaluation_job(
        self, **kwargs: Unpack[CreateEvaluationJobRequestTypeDef]
    ) -> CreateEvaluationJobResponseTypeDef:
        """
        Creates an evaluation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_evaluation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_evaluation_job)
        """

    def create_foundation_model_agreement(
        self, **kwargs: Unpack[CreateFoundationModelAgreementRequestTypeDef]
    ) -> CreateFoundationModelAgreementResponseTypeDef:
        """
        Request a model access agreement for the specified model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_foundation_model_agreement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_foundation_model_agreement)
        """

    def create_guardrail(
        self, **kwargs: Unpack[CreateGuardrailRequestTypeDef]
    ) -> CreateGuardrailResponseTypeDef:
        """
        Creates a guardrail to block topics and to implement safeguards for your
        generative AI applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_guardrail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_guardrail)
        """

    def create_guardrail_version(
        self, **kwargs: Unpack[CreateGuardrailVersionRequestTypeDef]
    ) -> CreateGuardrailVersionResponseTypeDef:
        """
        Creates a version of the guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_guardrail_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_guardrail_version)
        """

    def create_inference_profile(
        self, **kwargs: Unpack[CreateInferenceProfileRequestTypeDef]
    ) -> CreateInferenceProfileResponseTypeDef:
        """
        Creates an application inference profile to track metrics and costs when
        invoking a model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_inference_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_inference_profile)
        """

    def create_marketplace_model_endpoint(
        self, **kwargs: Unpack[CreateMarketplaceModelEndpointRequestTypeDef]
    ) -> CreateMarketplaceModelEndpointResponseTypeDef:
        """
        Creates an endpoint for a model from Amazon Bedrock Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_marketplace_model_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_marketplace_model_endpoint)
        """

    def create_model_copy_job(
        self, **kwargs: Unpack[CreateModelCopyJobRequestTypeDef]
    ) -> CreateModelCopyJobResponseTypeDef:
        """
        Copies a model to another region so that it can be used there.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_model_copy_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_model_copy_job)
        """

    def create_model_customization_job(
        self, **kwargs: Unpack[CreateModelCustomizationJobRequestTypeDef]
    ) -> CreateModelCustomizationJobResponseTypeDef:
        """
        Creates a fine-tuning job to customize a base model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_model_customization_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_model_customization_job)
        """

    def create_model_import_job(
        self, **kwargs: Unpack[CreateModelImportJobRequestTypeDef]
    ) -> CreateModelImportJobResponseTypeDef:
        """
        Creates a model import job to import model that you have customized in other
        environments, such as Amazon SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_model_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_model_import_job)
        """

    def create_model_invocation_job(
        self, **kwargs: Unpack[CreateModelInvocationJobRequestTypeDef]
    ) -> CreateModelInvocationJobResponseTypeDef:
        """
        Creates a batch inference job to invoke a model on multiple prompts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_model_invocation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_model_invocation_job)
        """

    def create_prompt_router(
        self, **kwargs: Unpack[CreatePromptRouterRequestTypeDef]
    ) -> CreatePromptRouterResponseTypeDef:
        """
        Creates a prompt router that manages the routing of requests between multiple
        foundation models based on the routing criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_prompt_router.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_prompt_router)
        """

    def create_provisioned_model_throughput(
        self, **kwargs: Unpack[CreateProvisionedModelThroughputRequestTypeDef]
    ) -> CreateProvisionedModelThroughputResponseTypeDef:
        """
        Creates dedicated throughput for a base or custom model with the model units
        and for the duration that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/create_provisioned_model_throughput.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#create_provisioned_model_throughput)
        """

    def delete_automated_reasoning_policy(
        self, **kwargs: Unpack[DeleteAutomatedReasoningPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Automated Reasoning policy or policy version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_automated_reasoning_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_automated_reasoning_policy)
        """

    def delete_automated_reasoning_policy_build_workflow(
        self, **kwargs: Unpack[DeleteAutomatedReasoningPolicyBuildWorkflowRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Automated Reasoning policy build workflow and its associated
        artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_automated_reasoning_policy_build_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_automated_reasoning_policy_build_workflow)
        """

    def delete_automated_reasoning_policy_test_case(
        self, **kwargs: Unpack[DeleteAutomatedReasoningPolicyTestCaseRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an Automated Reasoning policy test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_automated_reasoning_policy_test_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_automated_reasoning_policy_test_case)
        """

    def delete_custom_model(
        self, **kwargs: Unpack[DeleteCustomModelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a custom model that you created earlier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_custom_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_custom_model)
        """

    def delete_custom_model_deployment(
        self, **kwargs: Unpack[DeleteCustomModelDeploymentRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a custom model deployment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_custom_model_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_custom_model_deployment)
        """

    def delete_enforced_guardrail_configuration(
        self, **kwargs: Unpack[DeleteEnforcedGuardrailConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the account-level enforced guardrail configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_enforced_guardrail_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_enforced_guardrail_configuration)
        """

    def delete_foundation_model_agreement(
        self, **kwargs: Unpack[DeleteFoundationModelAgreementRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete the model access agreement for the specified model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_foundation_model_agreement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_foundation_model_agreement)
        """

    def delete_guardrail(self, **kwargs: Unpack[DeleteGuardrailRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_guardrail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_guardrail)
        """

    def delete_imported_model(
        self, **kwargs: Unpack[DeleteImportedModelRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a custom model that you imported earlier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_imported_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_imported_model)
        """

    def delete_inference_profile(
        self, **kwargs: Unpack[DeleteInferenceProfileRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an application inference profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_inference_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_inference_profile)
        """

    def delete_marketplace_model_endpoint(
        self, **kwargs: Unpack[DeleteMarketplaceModelEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an endpoint for a model from Amazon Bedrock Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_marketplace_model_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_marketplace_model_endpoint)
        """

    def delete_model_invocation_logging_configuration(self) -> Dict[str, Any]:
        """
        Delete the invocation logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_model_invocation_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_model_invocation_logging_configuration)
        """

    def delete_prompt_router(
        self, **kwargs: Unpack[DeletePromptRouterRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a specified prompt router.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_prompt_router.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_prompt_router)
        """

    def delete_provisioned_model_throughput(
        self, **kwargs: Unpack[DeleteProvisionedModelThroughputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Provisioned Throughput.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/delete_provisioned_model_throughput.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#delete_provisioned_model_throughput)
        """

    def deregister_marketplace_model_endpoint(
        self, **kwargs: Unpack[DeregisterMarketplaceModelEndpointRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deregisters an endpoint for a model from Amazon Bedrock Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/deregister_marketplace_model_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#deregister_marketplace_model_endpoint)
        """

    def export_automated_reasoning_policy_version(
        self, **kwargs: Unpack[ExportAutomatedReasoningPolicyVersionRequestTypeDef]
    ) -> ExportAutomatedReasoningPolicyVersionResponseTypeDef:
        """
        Exports the policy definition for an Automated Reasoning policy version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/export_automated_reasoning_policy_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#export_automated_reasoning_policy_version)
        """

    def get_automated_reasoning_policy(
        self, **kwargs: Unpack[GetAutomatedReasoningPolicyRequestTypeDef]
    ) -> GetAutomatedReasoningPolicyResponseTypeDef:
        """
        Retrieves details about an Automated Reasoning policy or policy version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_automated_reasoning_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_automated_reasoning_policy)
        """

    def get_automated_reasoning_policy_annotations(
        self, **kwargs: Unpack[GetAutomatedReasoningPolicyAnnotationsRequestTypeDef]
    ) -> GetAutomatedReasoningPolicyAnnotationsResponseTypeDef:
        """
        Retrieves the current annotations for an Automated Reasoning policy build
        workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_automated_reasoning_policy_annotations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_automated_reasoning_policy_annotations)
        """

    def get_automated_reasoning_policy_build_workflow(
        self, **kwargs: Unpack[GetAutomatedReasoningPolicyBuildWorkflowRequestTypeDef]
    ) -> GetAutomatedReasoningPolicyBuildWorkflowResponseTypeDef:
        """
        Retrieves detailed information about an Automated Reasoning policy build
        workflow, including its status, configuration, and metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_automated_reasoning_policy_build_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_automated_reasoning_policy_build_workflow)
        """

    def get_automated_reasoning_policy_build_workflow_result_assets(
        self, **kwargs: Unpack[GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequestTypeDef]
    ) -> GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponseTypeDef:
        """
        Retrieves the resulting assets from a completed Automated Reasoning policy
        build workflow, including build logs, quality reports, and generated policy
        artifacts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_automated_reasoning_policy_build_workflow_result_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_automated_reasoning_policy_build_workflow_result_assets)
        """

    def get_automated_reasoning_policy_next_scenario(
        self, **kwargs: Unpack[GetAutomatedReasoningPolicyNextScenarioRequestTypeDef]
    ) -> GetAutomatedReasoningPolicyNextScenarioResponseTypeDef:
        """
        Retrieves the next test scenario for validating an Automated Reasoning policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_automated_reasoning_policy_next_scenario.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_automated_reasoning_policy_next_scenario)
        """

    def get_automated_reasoning_policy_test_case(
        self, **kwargs: Unpack[GetAutomatedReasoningPolicyTestCaseRequestTypeDef]
    ) -> GetAutomatedReasoningPolicyTestCaseResponseTypeDef:
        """
        Retrieves details about a specific Automated Reasoning policy test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_automated_reasoning_policy_test_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_automated_reasoning_policy_test_case)
        """

    def get_automated_reasoning_policy_test_result(
        self, **kwargs: Unpack[GetAutomatedReasoningPolicyTestResultRequestTypeDef]
    ) -> GetAutomatedReasoningPolicyTestResultResponseTypeDef:
        """
        Retrieves the test result for a specific Automated Reasoning policy test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_automated_reasoning_policy_test_result.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_automated_reasoning_policy_test_result)
        """

    def get_custom_model(
        self, **kwargs: Unpack[GetCustomModelRequestTypeDef]
    ) -> GetCustomModelResponseTypeDef:
        """
        Get the properties associated with a Amazon Bedrock custom model that you have
        created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_custom_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_custom_model)
        """

    def get_custom_model_deployment(
        self, **kwargs: Unpack[GetCustomModelDeploymentRequestTypeDef]
    ) -> GetCustomModelDeploymentResponseTypeDef:
        """
        Retrieves information about a custom model deployment, including its status,
        configuration, and metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_custom_model_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_custom_model_deployment)
        """

    def get_evaluation_job(
        self, **kwargs: Unpack[GetEvaluationJobRequestTypeDef]
    ) -> GetEvaluationJobResponseTypeDef:
        """
        Gets information about an evaluation job, such as the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_evaluation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_evaluation_job)
        """

    def get_foundation_model(
        self, **kwargs: Unpack[GetFoundationModelRequestTypeDef]
    ) -> GetFoundationModelResponseTypeDef:
        """
        Get details about a Amazon Bedrock foundation model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_foundation_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_foundation_model)
        """

    def get_foundation_model_availability(
        self, **kwargs: Unpack[GetFoundationModelAvailabilityRequestTypeDef]
    ) -> GetFoundationModelAvailabilityResponseTypeDef:
        """
        Get information about the Foundation model availability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_foundation_model_availability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_foundation_model_availability)
        """

    def get_guardrail(
        self, **kwargs: Unpack[GetGuardrailRequestTypeDef]
    ) -> GetGuardrailResponseTypeDef:
        """
        Gets details about a guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_guardrail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_guardrail)
        """

    def get_imported_model(
        self, **kwargs: Unpack[GetImportedModelRequestTypeDef]
    ) -> GetImportedModelResponseTypeDef:
        """
        Gets properties associated with a customized model you imported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_imported_model.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_imported_model)
        """

    def get_inference_profile(
        self, **kwargs: Unpack[GetInferenceProfileRequestTypeDef]
    ) -> GetInferenceProfileResponseTypeDef:
        """
        Gets information about an inference profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_inference_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_inference_profile)
        """

    def get_marketplace_model_endpoint(
        self, **kwargs: Unpack[GetMarketplaceModelEndpointRequestTypeDef]
    ) -> GetMarketplaceModelEndpointResponseTypeDef:
        """
        Retrieves details about a specific endpoint for a model from Amazon Bedrock
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_marketplace_model_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_marketplace_model_endpoint)
        """

    def get_model_copy_job(
        self, **kwargs: Unpack[GetModelCopyJobRequestTypeDef]
    ) -> GetModelCopyJobResponseTypeDef:
        """
        Retrieves information about a model copy job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_model_copy_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_model_copy_job)
        """

    def get_model_customization_job(
        self, **kwargs: Unpack[GetModelCustomizationJobRequestTypeDef]
    ) -> GetModelCustomizationJobResponseTypeDef:
        """
        Retrieves the properties associated with a model-customization job, including
        the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_model_customization_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_model_customization_job)
        """

    def get_model_import_job(
        self, **kwargs: Unpack[GetModelImportJobRequestTypeDef]
    ) -> GetModelImportJobResponseTypeDef:
        """
        Retrieves the properties associated with import model job, including the status
        of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_model_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_model_import_job)
        """

    def get_model_invocation_job(
        self, **kwargs: Unpack[GetModelInvocationJobRequestTypeDef]
    ) -> GetModelInvocationJobResponseTypeDef:
        """
        Gets details about a batch inference job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_model_invocation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_model_invocation_job)
        """

    def get_model_invocation_logging_configuration(
        self,
    ) -> GetModelInvocationLoggingConfigurationResponseTypeDef:
        """
        Get the current configuration values for model invocation logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_model_invocation_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_model_invocation_logging_configuration)
        """

    def get_prompt_router(
        self, **kwargs: Unpack[GetPromptRouterRequestTypeDef]
    ) -> GetPromptRouterResponseTypeDef:
        """
        Retrieves details about a prompt router.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_prompt_router.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_prompt_router)
        """

    def get_provisioned_model_throughput(
        self, **kwargs: Unpack[GetProvisionedModelThroughputRequestTypeDef]
    ) -> GetProvisionedModelThroughputResponseTypeDef:
        """
        Returns details for a Provisioned Throughput.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_provisioned_model_throughput.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_provisioned_model_throughput)
        """

    def get_use_case_for_model_access(self) -> GetUseCaseForModelAccessResponseTypeDef:
        """
        Get usecase for model access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_use_case_for_model_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_use_case_for_model_access)
        """

    def list_automated_reasoning_policies(
        self, **kwargs: Unpack[ListAutomatedReasoningPoliciesRequestTypeDef]
    ) -> ListAutomatedReasoningPoliciesResponseTypeDef:
        """
        Lists all Automated Reasoning policies in your account, with optional filtering
        by policy ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_automated_reasoning_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_automated_reasoning_policies)
        """

    def list_automated_reasoning_policy_build_workflows(
        self, **kwargs: Unpack[ListAutomatedReasoningPolicyBuildWorkflowsRequestTypeDef]
    ) -> ListAutomatedReasoningPolicyBuildWorkflowsResponseTypeDef:
        """
        Lists all build workflows for an Automated Reasoning policy, showing the
        history of policy creation and modification attempts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_automated_reasoning_policy_build_workflows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_automated_reasoning_policy_build_workflows)
        """

    def list_automated_reasoning_policy_test_cases(
        self, **kwargs: Unpack[ListAutomatedReasoningPolicyTestCasesRequestTypeDef]
    ) -> ListAutomatedReasoningPolicyTestCasesResponseTypeDef:
        """
        Lists tests for an Automated Reasoning policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_automated_reasoning_policy_test_cases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_automated_reasoning_policy_test_cases)
        """

    def list_automated_reasoning_policy_test_results(
        self, **kwargs: Unpack[ListAutomatedReasoningPolicyTestResultsRequestTypeDef]
    ) -> ListAutomatedReasoningPolicyTestResultsResponseTypeDef:
        """
        Lists test results for an Automated Reasoning policy, showing how the policy
        performed against various test scenarios and validation checks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_automated_reasoning_policy_test_results.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_automated_reasoning_policy_test_results)
        """

    def list_custom_model_deployments(
        self, **kwargs: Unpack[ListCustomModelDeploymentsRequestTypeDef]
    ) -> ListCustomModelDeploymentsResponseTypeDef:
        """
        Lists custom model deployments in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_custom_model_deployments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_custom_model_deployments)
        """

    def list_custom_models(
        self, **kwargs: Unpack[ListCustomModelsRequestTypeDef]
    ) -> ListCustomModelsResponseTypeDef:
        """
        Returns a list of the custom models that you have created with the
        <code>CreateModelCustomizationJob</code> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_custom_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_custom_models)
        """

    def list_enforced_guardrails_configuration(
        self, **kwargs: Unpack[ListEnforcedGuardrailsConfigurationRequestTypeDef]
    ) -> ListEnforcedGuardrailsConfigurationResponseTypeDef:
        """
        Lists the account-level enforced guardrail configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_enforced_guardrails_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_enforced_guardrails_configuration)
        """

    def list_evaluation_jobs(
        self, **kwargs: Unpack[ListEvaluationJobsRequestTypeDef]
    ) -> ListEvaluationJobsResponseTypeDef:
        """
        Lists all existing evaluation jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_evaluation_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_evaluation_jobs)
        """

    def list_foundation_model_agreement_offers(
        self, **kwargs: Unpack[ListFoundationModelAgreementOffersRequestTypeDef]
    ) -> ListFoundationModelAgreementOffersResponseTypeDef:
        """
        Get the offers associated with the specified model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_foundation_model_agreement_offers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_foundation_model_agreement_offers)
        """

    def list_foundation_models(
        self, **kwargs: Unpack[ListFoundationModelsRequestTypeDef]
    ) -> ListFoundationModelsResponseTypeDef:
        """
        Lists Amazon Bedrock foundation models that you can use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_foundation_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_foundation_models)
        """

    def list_guardrails(
        self, **kwargs: Unpack[ListGuardrailsRequestTypeDef]
    ) -> ListGuardrailsResponseTypeDef:
        """
        Lists details about all the guardrails in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_guardrails.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_guardrails)
        """

    def list_imported_models(
        self, **kwargs: Unpack[ListImportedModelsRequestTypeDef]
    ) -> ListImportedModelsResponseTypeDef:
        """
        Returns a list of models you've imported.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_imported_models.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_imported_models)
        """

    def list_inference_profiles(
        self, **kwargs: Unpack[ListInferenceProfilesRequestTypeDef]
    ) -> ListInferenceProfilesResponseTypeDef:
        """
        Returns a list of inference profiles that you can use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_inference_profiles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_inference_profiles)
        """

    def list_marketplace_model_endpoints(
        self, **kwargs: Unpack[ListMarketplaceModelEndpointsRequestTypeDef]
    ) -> ListMarketplaceModelEndpointsResponseTypeDef:
        """
        Lists the endpoints for models from Amazon Bedrock Marketplace in your Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_marketplace_model_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_marketplace_model_endpoints)
        """

    def list_model_copy_jobs(
        self, **kwargs: Unpack[ListModelCopyJobsRequestTypeDef]
    ) -> ListModelCopyJobsResponseTypeDef:
        """
        Returns a list of model copy jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_model_copy_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_model_copy_jobs)
        """

    def list_model_customization_jobs(
        self, **kwargs: Unpack[ListModelCustomizationJobsRequestTypeDef]
    ) -> ListModelCustomizationJobsResponseTypeDef:
        """
        Returns a list of model customization jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_model_customization_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_model_customization_jobs)
        """

    def list_model_import_jobs(
        self, **kwargs: Unpack[ListModelImportJobsRequestTypeDef]
    ) -> ListModelImportJobsResponseTypeDef:
        """
        Returns a list of import jobs you've submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_model_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_model_import_jobs)
        """

    def list_model_invocation_jobs(
        self, **kwargs: Unpack[ListModelInvocationJobsRequestTypeDef]
    ) -> ListModelInvocationJobsResponseTypeDef:
        """
        Lists all batch inference jobs in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_model_invocation_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_model_invocation_jobs)
        """

    def list_prompt_routers(
        self, **kwargs: Unpack[ListPromptRoutersRequestTypeDef]
    ) -> ListPromptRoutersResponseTypeDef:
        """
        Retrieves a list of prompt routers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_prompt_routers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_prompt_routers)
        """

    def list_provisioned_model_throughputs(
        self, **kwargs: Unpack[ListProvisionedModelThroughputsRequestTypeDef]
    ) -> ListProvisionedModelThroughputsResponseTypeDef:
        """
        Lists the Provisioned Throughputs in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_provisioned_model_throughputs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_provisioned_model_throughputs)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#list_tags_for_resource)
        """

    def put_enforced_guardrail_configuration(
        self, **kwargs: Unpack[PutEnforcedGuardrailConfigurationRequestTypeDef]
    ) -> PutEnforcedGuardrailConfigurationResponseTypeDef:
        """
        Sets the account-level enforced guardrail configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/put_enforced_guardrail_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#put_enforced_guardrail_configuration)
        """

    def put_model_invocation_logging_configuration(
        self, **kwargs: Unpack[PutModelInvocationLoggingConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Set the configuration values for model invocation logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/put_model_invocation_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#put_model_invocation_logging_configuration)
        """

    def put_use_case_for_model_access(
        self, **kwargs: Unpack[PutUseCaseForModelAccessRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Put usecase for model access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/put_use_case_for_model_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#put_use_case_for_model_access)
        """

    def register_marketplace_model_endpoint(
        self, **kwargs: Unpack[RegisterMarketplaceModelEndpointRequestTypeDef]
    ) -> RegisterMarketplaceModelEndpointResponseTypeDef:
        """
        Registers an existing Amazon SageMaker endpoint with Amazon Bedrock
        Marketplace, allowing it to be used with Amazon Bedrock APIs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/register_marketplace_model_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#register_marketplace_model_endpoint)
        """

    def start_automated_reasoning_policy_build_workflow(
        self, **kwargs: Unpack[StartAutomatedReasoningPolicyBuildWorkflowRequestTypeDef]
    ) -> StartAutomatedReasoningPolicyBuildWorkflowResponseTypeDef:
        """
        Starts a new build workflow for an Automated Reasoning policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/start_automated_reasoning_policy_build_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#start_automated_reasoning_policy_build_workflow)
        """

    def start_automated_reasoning_policy_test_workflow(
        self, **kwargs: Unpack[StartAutomatedReasoningPolicyTestWorkflowRequestTypeDef]
    ) -> StartAutomatedReasoningPolicyTestWorkflowResponseTypeDef:
        """
        Initiates a test workflow to validate Automated Reasoning policy tests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/start_automated_reasoning_policy_test_workflow.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#start_automated_reasoning_policy_test_workflow)
        """

    def stop_evaluation_job(
        self, **kwargs: Unpack[StopEvaluationJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops an evaluation job that is current being created or running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/stop_evaluation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#stop_evaluation_job)
        """

    def stop_model_customization_job(
        self, **kwargs: Unpack[StopModelCustomizationJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops an active model customization job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/stop_model_customization_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#stop_model_customization_job)
        """

    def stop_model_invocation_job(
        self, **kwargs: Unpack[StopModelInvocationJobRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stops a batch inference job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/stop_model_invocation_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#stop_model_invocation_job)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associate tags with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Remove one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#untag_resource)
        """

    def update_automated_reasoning_policy(
        self, **kwargs: Unpack[UpdateAutomatedReasoningPolicyRequestTypeDef]
    ) -> UpdateAutomatedReasoningPolicyResponseTypeDef:
        """
        Updates an existing Automated Reasoning policy with new rules, variables, or
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/update_automated_reasoning_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#update_automated_reasoning_policy)
        """

    def update_automated_reasoning_policy_annotations(
        self, **kwargs: Unpack[UpdateAutomatedReasoningPolicyAnnotationsRequestTypeDef]
    ) -> UpdateAutomatedReasoningPolicyAnnotationsResponseTypeDef:
        """
        Updates the annotations for an Automated Reasoning policy build workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/update_automated_reasoning_policy_annotations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#update_automated_reasoning_policy_annotations)
        """

    def update_automated_reasoning_policy_test_case(
        self, **kwargs: Unpack[UpdateAutomatedReasoningPolicyTestCaseRequestTypeDef]
    ) -> UpdateAutomatedReasoningPolicyTestCaseResponseTypeDef:
        """
        Updates an existing Automated Reasoning policy test.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/update_automated_reasoning_policy_test_case.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#update_automated_reasoning_policy_test_case)
        """

    def update_custom_model_deployment(
        self, **kwargs: Unpack[UpdateCustomModelDeploymentRequestTypeDef]
    ) -> UpdateCustomModelDeploymentResponseTypeDef:
        """
        Updates a custom model deployment with a new custom model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/update_custom_model_deployment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#update_custom_model_deployment)
        """

    def update_guardrail(
        self, **kwargs: Unpack[UpdateGuardrailRequestTypeDef]
    ) -> UpdateGuardrailResponseTypeDef:
        """
        Updates a guardrail with the values you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/update_guardrail.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#update_guardrail)
        """

    def update_marketplace_model_endpoint(
        self, **kwargs: Unpack[UpdateMarketplaceModelEndpointRequestTypeDef]
    ) -> UpdateMarketplaceModelEndpointResponseTypeDef:
        """
        Updates the configuration of an existing endpoint for a model from Amazon
        Bedrock Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/update_marketplace_model_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#update_marketplace_model_endpoint)
        """

    def update_provisioned_model_throughput(
        self, **kwargs: Unpack[UpdateProvisionedModelThroughputRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the name or associated model for a Provisioned Throughput.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/update_provisioned_model_throughput.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#update_provisioned_model_throughput)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automated_reasoning_policies"]
    ) -> ListAutomatedReasoningPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automated_reasoning_policy_build_workflows"]
    ) -> ListAutomatedReasoningPolicyBuildWorkflowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automated_reasoning_policy_test_cases"]
    ) -> ListAutomatedReasoningPolicyTestCasesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_automated_reasoning_policy_test_results"]
    ) -> ListAutomatedReasoningPolicyTestResultsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_custom_model_deployments"]
    ) -> ListCustomModelDeploymentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_custom_models"]
    ) -> ListCustomModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_enforced_guardrails_configuration"]
    ) -> ListEnforcedGuardrailsConfigurationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_evaluation_jobs"]
    ) -> ListEvaluationJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_guardrails"]
    ) -> ListGuardrailsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_imported_models"]
    ) -> ListImportedModelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_inference_profiles"]
    ) -> ListInferenceProfilesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_marketplace_model_endpoints"]
    ) -> ListMarketplaceModelEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_model_copy_jobs"]
    ) -> ListModelCopyJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_model_customization_jobs"]
    ) -> ListModelCustomizationJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_model_import_jobs"]
    ) -> ListModelImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_model_invocation_jobs"]
    ) -> ListModelInvocationJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_prompt_routers"]
    ) -> ListPromptRoutersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_provisioned_model_throughputs"]
    ) -> ListProvisionedModelThroughputsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client/#get_paginator)
        """
