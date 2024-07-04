"""
Type annotations for bedrock service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_bedrock import BedrockClient

    client: BedrockClient = boto3.client("bedrock")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    CommitmentDurationType,
    CustomizationTypeType,
    EvaluationJobStatusType,
    FineTuningJobStatusType,
    InferenceTypeType,
    ModelCustomizationType,
    ModelModalityType,
    ProvisionedModelStatusType,
    SortOrderType,
)
from .paginator import (
    ListCustomModelsPaginator,
    ListEvaluationJobsPaginator,
    ListGuardrailsPaginator,
    ListModelCustomizationJobsPaginator,
    ListProvisionedModelThroughputsPaginator,
)
from .type_defs import (
    CreateEvaluationJobResponseTypeDef,
    CreateGuardrailResponseTypeDef,
    CreateGuardrailVersionResponseTypeDef,
    CreateModelCustomizationJobResponseTypeDef,
    CreateProvisionedModelThroughputResponseTypeDef,
    EvaluationConfigTypeDef,
    EvaluationInferenceConfigTypeDef,
    EvaluationOutputDataConfigTypeDef,
    GetCustomModelResponseTypeDef,
    GetEvaluationJobResponseTypeDef,
    GetFoundationModelResponseTypeDef,
    GetGuardrailResponseTypeDef,
    GetModelCustomizationJobResponseTypeDef,
    GetModelInvocationLoggingConfigurationResponseTypeDef,
    GetProvisionedModelThroughputResponseTypeDef,
    GuardrailContentPolicyConfigTypeDef,
    GuardrailSensitiveInformationPolicyConfigTypeDef,
    GuardrailTopicPolicyConfigTypeDef,
    GuardrailWordPolicyConfigTypeDef,
    ListCustomModelsResponseTypeDef,
    ListEvaluationJobsResponseTypeDef,
    ListFoundationModelsResponseTypeDef,
    ListGuardrailsResponseTypeDef,
    ListModelCustomizationJobsResponseTypeDef,
    ListProvisionedModelThroughputsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingConfigTypeDef,
    OutputDataConfigTypeDef,
    TagTypeDef,
    TrainingDataConfigTypeDef,
    UpdateGuardrailResponseTypeDef,
    ValidationDataConfigTypeDef,
    VpcConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BedrockClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BedrockClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BedrockClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#close)
        """

    def create_evaluation_job(
        self,
        *,
        jobName: str,
        roleArn: str,
        evaluationConfig: "EvaluationConfigTypeDef",
        inferenceConfig: "EvaluationInferenceConfigTypeDef",
        outputDataConfig: "EvaluationOutputDataConfigTypeDef",
        jobDescription: str = None,
        clientRequestToken: str = None,
        customerEncryptionKeyId: str = None,
        jobTags: List["TagTypeDef"] = None
    ) -> CreateEvaluationJobResponseTypeDef:
        """
        API operation for creating and managing Amazon Bedrock automatic model
        evaluation jobs and model evaluation jobs that use human workers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.create_evaluation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#create_evaluation_job)
        """

    def create_guardrail(
        self,
        *,
        name: str,
        blockedInputMessaging: str,
        blockedOutputsMessaging: str,
        description: str = None,
        topicPolicyConfig: "GuardrailTopicPolicyConfigTypeDef" = None,
        contentPolicyConfig: "GuardrailContentPolicyConfigTypeDef" = None,
        wordPolicyConfig: "GuardrailWordPolicyConfigTypeDef" = None,
        sensitiveInformationPolicyConfig: "GuardrailSensitiveInformationPolicyConfigTypeDef" = None,
        kmsKeyId: str = None,
        tags: List["TagTypeDef"] = None,
        clientRequestToken: str = None
    ) -> CreateGuardrailResponseTypeDef:
        """
        Creates a guardrail to block topics and to filter out harmful content.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.create_guardrail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#create_guardrail)
        """

    def create_guardrail_version(
        self, *, guardrailIdentifier: str, description: str = None, clientRequestToken: str = None
    ) -> CreateGuardrailVersionResponseTypeDef:
        """
        Creates a version of the guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.create_guardrail_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#create_guardrail_version)
        """

    def create_model_customization_job(
        self,
        *,
        jobName: str,
        customModelName: str,
        roleArn: str,
        baseModelIdentifier: str,
        trainingDataConfig: "TrainingDataConfigTypeDef",
        outputDataConfig: "OutputDataConfigTypeDef",
        hyperParameters: Dict[str, str],
        clientRequestToken: str = None,
        customizationType: CustomizationTypeType = None,
        customModelKmsKeyId: str = None,
        jobTags: List["TagTypeDef"] = None,
        customModelTags: List["TagTypeDef"] = None,
        validationDataConfig: "ValidationDataConfigTypeDef" = None,
        vpcConfig: "VpcConfigTypeDef" = None
    ) -> CreateModelCustomizationJobResponseTypeDef:
        """
        Creates a fine-tuning job to customize a base model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.create_model_customization_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#create_model_customization_job)
        """

    def create_provisioned_model_throughput(
        self,
        *,
        modelUnits: int,
        provisionedModelName: str,
        modelId: str,
        clientRequestToken: str = None,
        commitmentDuration: CommitmentDurationType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateProvisionedModelThroughputResponseTypeDef:
        """
        Creates dedicated throughput for a base or custom model with the model units and
        for the duration that you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.create_provisioned_model_throughput)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#create_provisioned_model_throughput)
        """

    def delete_custom_model(self, *, modelIdentifier: str) -> Dict[str, Any]:
        """
        Deletes a custom model that you created earlier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.delete_custom_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#delete_custom_model)
        """

    def delete_guardrail(
        self, *, guardrailIdentifier: str, guardrailVersion: str = None
    ) -> Dict[str, Any]:
        """
        Deletes a guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.delete_guardrail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#delete_guardrail)
        """

    def delete_model_invocation_logging_configuration(self) -> Dict[str, Any]:
        """
        Delete the invocation logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.delete_model_invocation_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#delete_model_invocation_logging_configuration)
        """

    def delete_provisioned_model_throughput(self, *, provisionedModelId: str) -> Dict[str, Any]:
        """
        Deletes a Provisioned Throughput.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.delete_provisioned_model_throughput)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#delete_provisioned_model_throughput)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#generate_presigned_url)
        """

    def get_custom_model(self, *, modelIdentifier: str) -> GetCustomModelResponseTypeDef:
        """
        Get the properties associated with a Amazon Bedrock custom model that you have
        created.For more information, see `Custom models
        <https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html>`__ in
        the Amazon Bedrock User Guide.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.get_custom_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#get_custom_model)
        """

    def get_evaluation_job(self, *, jobIdentifier: str) -> GetEvaluationJobResponseTypeDef:
        """
        Retrieves the properties associated with a model evaluation job, including the
        status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.get_evaluation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#get_evaluation_job)
        """

    def get_foundation_model(self, *, modelIdentifier: str) -> GetFoundationModelResponseTypeDef:
        """
        Get details about a Amazon Bedrock foundation model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.get_foundation_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#get_foundation_model)
        """

    def get_guardrail(
        self, *, guardrailIdentifier: str, guardrailVersion: str = None
    ) -> GetGuardrailResponseTypeDef:
        """
        Gets details about a guardrail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.get_guardrail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#get_guardrail)
        """

    def get_model_customization_job(
        self, *, jobIdentifier: str
    ) -> GetModelCustomizationJobResponseTypeDef:
        """
        Retrieves the properties associated with a model-customization job, including
        the status of the job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.get_model_customization_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#get_model_customization_job)
        """

    def get_model_invocation_logging_configuration(
        self,
    ) -> GetModelInvocationLoggingConfigurationResponseTypeDef:
        """
        Get the current configuration values for model invocation logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.get_model_invocation_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#get_model_invocation_logging_configuration)
        """

    def get_provisioned_model_throughput(
        self, *, provisionedModelId: str
    ) -> GetProvisionedModelThroughputResponseTypeDef:
        """
        Returns details for a Provisioned Throughput.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.get_provisioned_model_throughput)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#get_provisioned_model_throughput)
        """

    def list_custom_models(
        self,
        *,
        creationTimeBefore: Union[datetime, str] = None,
        creationTimeAfter: Union[datetime, str] = None,
        nameContains: str = None,
        baseModelArnEquals: str = None,
        foundationModelArnEquals: str = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: Literal["CreationTime"] = None,
        sortOrder: SortOrderType = None
    ) -> ListCustomModelsResponseTypeDef:
        """
        Returns a list of the custom models that you have created with the
        `CreateModelCustomizationJob` operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.list_custom_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#list_custom_models)
        """

    def list_evaluation_jobs(
        self,
        *,
        creationTimeAfter: Union[datetime, str] = None,
        creationTimeBefore: Union[datetime, str] = None,
        statusEquals: EvaluationJobStatusType = None,
        nameContains: str = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: Literal["CreationTime"] = None,
        sortOrder: SortOrderType = None
    ) -> ListEvaluationJobsResponseTypeDef:
        """
        Lists model evaluation jobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.list_evaluation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#list_evaluation_jobs)
        """

    def list_foundation_models(
        self,
        *,
        byProvider: str = None,
        byCustomizationType: ModelCustomizationType = None,
        byOutputModality: ModelModalityType = None,
        byInferenceType: InferenceTypeType = None
    ) -> ListFoundationModelsResponseTypeDef:
        """
        Lists Amazon Bedrock foundation models that you can use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.list_foundation_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#list_foundation_models)
        """

    def list_guardrails(
        self, *, guardrailIdentifier: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListGuardrailsResponseTypeDef:
        """
        Lists details about all the guardrails in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.list_guardrails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#list_guardrails)
        """

    def list_model_customization_jobs(
        self,
        *,
        creationTimeAfter: Union[datetime, str] = None,
        creationTimeBefore: Union[datetime, str] = None,
        statusEquals: FineTuningJobStatusType = None,
        nameContains: str = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: Literal["CreationTime"] = None,
        sortOrder: SortOrderType = None
    ) -> ListModelCustomizationJobsResponseTypeDef:
        """
        Returns a list of model customization jobs that you have submitted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.list_model_customization_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#list_model_customization_jobs)
        """

    def list_provisioned_model_throughputs(
        self,
        *,
        creationTimeAfter: Union[datetime, str] = None,
        creationTimeBefore: Union[datetime, str] = None,
        statusEquals: ProvisionedModelStatusType = None,
        modelArnEquals: str = None,
        nameContains: str = None,
        maxResults: int = None,
        nextToken: str = None,
        sortBy: Literal["CreationTime"] = None,
        sortOrder: SortOrderType = None
    ) -> ListProvisionedModelThroughputsResponseTypeDef:
        """
        Lists the Provisioned Throughputs in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.list_provisioned_model_throughputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#list_provisioned_model_throughputs)
        """

    def list_tags_for_resource(self, *, resourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        List the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#list_tags_for_resource)
        """

    def put_model_invocation_logging_configuration(
        self, *, loggingConfig: "LoggingConfigTypeDef"
    ) -> Dict[str, Any]:
        """
        Set the configuration values for model invocation logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.put_model_invocation_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#put_model_invocation_logging_configuration)
        """

    def stop_evaluation_job(self, *, jobIdentifier: str) -> Dict[str, Any]:
        """
        Stops an in progress model evaluation job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.stop_evaluation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#stop_evaluation_job)
        """

    def stop_model_customization_job(self, *, jobIdentifier: str) -> Dict[str, Any]:
        """
        Stops an active model customization job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.stop_model_customization_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#stop_model_customization_job)
        """

    def tag_resource(self, *, resourceARN: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associate tags with a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Remove one or more tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#untag_resource)
        """

    def update_guardrail(
        self,
        *,
        guardrailIdentifier: str,
        name: str,
        blockedInputMessaging: str,
        blockedOutputsMessaging: str,
        description: str = None,
        topicPolicyConfig: "GuardrailTopicPolicyConfigTypeDef" = None,
        contentPolicyConfig: "GuardrailContentPolicyConfigTypeDef" = None,
        wordPolicyConfig: "GuardrailWordPolicyConfigTypeDef" = None,
        sensitiveInformationPolicyConfig: "GuardrailSensitiveInformationPolicyConfigTypeDef" = None,
        kmsKeyId: str = None
    ) -> UpdateGuardrailResponseTypeDef:
        """
        Updates a guardrail with the values you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.update_guardrail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#update_guardrail)
        """

    def update_provisioned_model_throughput(
        self,
        *,
        provisionedModelId: str,
        desiredProvisionedModelName: str = None,
        desiredModelId: str = None
    ) -> Dict[str, Any]:
        """
        Updates the name or associated model for a Provisioned Throughput.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Client.update_provisioned_model_throughput)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/client.html#update_provisioned_model_throughput)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_models"]
    ) -> ListCustomModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Paginator.ListCustomModels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listcustommodelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_evaluation_jobs"]
    ) -> ListEvaluationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Paginator.ListEvaluationJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listevaluationjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_guardrails"]) -> ListGuardrailsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Paginator.ListGuardrails)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listguardrailspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_customization_jobs"]
    ) -> ListModelCustomizationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Paginator.ListModelCustomizationJobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listmodelcustomizationjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioned_model_throughputs"]
    ) -> ListProvisionedModelThroughputsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/bedrock.html#Bedrock.Paginator.ListProvisionedModelThroughputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock/paginators.html#listprovisionedmodelthroughputspaginator)
        """
