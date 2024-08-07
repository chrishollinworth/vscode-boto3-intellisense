"""
Type annotations for imagebuilder service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_imagebuilder import imagebuilderClient

    client: imagebuilderClient = boto3.client("imagebuilder")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ComponentTypeType,
    LifecyclePolicyResourceTypeType,
    LifecyclePolicyStatusType,
    OwnershipType,
    PipelineStatusType,
    PlatformType,
    WorkflowStepActionTypeType,
    WorkflowTypeType,
)
from .type_defs import (
    AdditionalInstanceConfigurationTypeDef,
    CancelImageCreationResponseTypeDef,
    CancelLifecycleExecutionResponseTypeDef,
    ComponentConfigurationTypeDef,
    CreateComponentResponseTypeDef,
    CreateContainerRecipeResponseTypeDef,
    CreateDistributionConfigurationResponseTypeDef,
    CreateImagePipelineResponseTypeDef,
    CreateImageRecipeResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateInfrastructureConfigurationResponseTypeDef,
    CreateLifecyclePolicyResponseTypeDef,
    CreateWorkflowResponseTypeDef,
    DeleteComponentResponseTypeDef,
    DeleteContainerRecipeResponseTypeDef,
    DeleteDistributionConfigurationResponseTypeDef,
    DeleteImagePipelineResponseTypeDef,
    DeleteImageRecipeResponseTypeDef,
    DeleteImageResponseTypeDef,
    DeleteInfrastructureConfigurationResponseTypeDef,
    DeleteLifecyclePolicyResponseTypeDef,
    DeleteWorkflowResponseTypeDef,
    DistributionTypeDef,
    FilterTypeDef,
    GetComponentPolicyResponseTypeDef,
    GetComponentResponseTypeDef,
    GetContainerRecipePolicyResponseTypeDef,
    GetContainerRecipeResponseTypeDef,
    GetDistributionConfigurationResponseTypeDef,
    GetImagePipelineResponseTypeDef,
    GetImagePolicyResponseTypeDef,
    GetImageRecipePolicyResponseTypeDef,
    GetImageRecipeResponseTypeDef,
    GetImageResponseTypeDef,
    GetInfrastructureConfigurationResponseTypeDef,
    GetLifecycleExecutionResponseTypeDef,
    GetLifecyclePolicyResponseTypeDef,
    GetWorkflowExecutionResponseTypeDef,
    GetWorkflowResponseTypeDef,
    GetWorkflowStepExecutionResponseTypeDef,
    ImageScanFindingsFilterTypeDef,
    ImageScanningConfigurationTypeDef,
    ImageTestsConfigurationTypeDef,
    ImportComponentResponseTypeDef,
    ImportVmImageResponseTypeDef,
    InstanceBlockDeviceMappingTypeDef,
    InstanceConfigurationTypeDef,
    InstanceMetadataOptionsTypeDef,
    LifecyclePolicyDetailTypeDef,
    LifecyclePolicyResourceSelectionTypeDef,
    ListComponentBuildVersionsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListContainerRecipesResponseTypeDef,
    ListDistributionConfigurationsResponseTypeDef,
    ListImageBuildVersionsResponseTypeDef,
    ListImagePackagesResponseTypeDef,
    ListImagePipelineImagesResponseTypeDef,
    ListImagePipelinesResponseTypeDef,
    ListImageRecipesResponseTypeDef,
    ListImageScanFindingAggregationsResponseTypeDef,
    ListImageScanFindingsResponseTypeDef,
    ListImagesResponseTypeDef,
    ListInfrastructureConfigurationsResponseTypeDef,
    ListLifecycleExecutionResourcesResponseTypeDef,
    ListLifecycleExecutionsResponseTypeDef,
    ListLifecyclePoliciesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWaitingWorkflowStepsResponseTypeDef,
    ListWorkflowBuildVersionsResponseTypeDef,
    ListWorkflowExecutionsResponseTypeDef,
    ListWorkflowsResponseTypeDef,
    ListWorkflowStepExecutionsResponseTypeDef,
    LoggingTypeDef,
    PutComponentPolicyResponseTypeDef,
    PutContainerRecipePolicyResponseTypeDef,
    PutImagePolicyResponseTypeDef,
    PutImageRecipePolicyResponseTypeDef,
    ResourceStateTypeDef,
    ResourceStateUpdateExclusionRulesTypeDef,
    ResourceStateUpdateIncludeResourcesTypeDef,
    ScheduleTypeDef,
    SendWorkflowStepActionResponseTypeDef,
    StartImagePipelineExecutionResponseTypeDef,
    StartResourceStateUpdateResponseTypeDef,
    TargetContainerRepositoryTypeDef,
    UpdateDistributionConfigurationResponseTypeDef,
    UpdateImagePipelineResponseTypeDef,
    UpdateInfrastructureConfigurationResponseTypeDef,
    UpdateLifecyclePolicyResponseTypeDef,
    WorkflowConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("imagebuilderClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    CallRateLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    IdempotentParameterMismatchException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    InvalidVersionNumberException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceDependencyException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]

class imagebuilderClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        imagebuilderClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#can_paginate)
        """

    def cancel_image_creation(
        self, *, imageBuildVersionArn: str, clientToken: str
    ) -> CancelImageCreationResponseTypeDef:
        """
        CancelImageCreation cancels the creation of Image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.cancel_image_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#cancel_image_creation)
        """

    def cancel_lifecycle_execution(
        self, *, lifecycleExecutionId: str, clientToken: str
    ) -> CancelLifecycleExecutionResponseTypeDef:
        """
        Cancel a specific image lifecycle policy runtime instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.cancel_lifecycle_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#cancel_lifecycle_execution)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#close)
        """

    def create_component(
        self,
        *,
        name: str,
        semanticVersion: str,
        platform: PlatformType,
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        supportedOsVersions: List[str] = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None
    ) -> CreateComponentResponseTypeDef:
        """
        Creates a new component that can be used to build, validate, test, and assess
        your image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_component)
        """

    def create_container_recipe(
        self,
        *,
        containerType: Literal["DOCKER"],
        name: str,
        semanticVersion: str,
        components: List["ComponentConfigurationTypeDef"],
        parentImage: str,
        targetRepository: "TargetContainerRepositoryTypeDef",
        clientToken: str,
        description: str = None,
        instanceConfiguration: "InstanceConfigurationTypeDef" = None,
        dockerfileTemplateData: str = None,
        dockerfileTemplateUri: str = None,
        platformOverride: PlatformType = None,
        imageOsVersionOverride: str = None,
        tags: Dict[str, str] = None,
        workingDirectory: str = None,
        kmsKeyId: str = None
    ) -> CreateContainerRecipeResponseTypeDef:
        """
        Creates a new container recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_container_recipe)
        """

    def create_distribution_configuration(
        self,
        *,
        name: str,
        distributions: List["DistributionTypeDef"],
        clientToken: str,
        description: str = None,
        tags: Dict[str, str] = None
    ) -> CreateDistributionConfigurationResponseTypeDef:
        """
        Creates a new distribution configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_distribution_configuration)
        """

    def create_image(
        self,
        *,
        infrastructureConfigurationArn: str,
        clientToken: str,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        tags: Dict[str, str] = None,
        imageScanningConfiguration: "ImageScanningConfigurationTypeDef" = None,
        workflows: List["WorkflowConfigurationTypeDef"] = None,
        executionRole: str = None
    ) -> CreateImageResponseTypeDef:
        """
        Creates a new image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_image)
        """

    def create_image_pipeline(
        self,
        *,
        name: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        schedule: "ScheduleTypeDef" = None,
        status: PipelineStatusType = None,
        tags: Dict[str, str] = None,
        imageScanningConfiguration: "ImageScanningConfigurationTypeDef" = None,
        workflows: List["WorkflowConfigurationTypeDef"] = None,
        executionRole: str = None
    ) -> CreateImagePipelineResponseTypeDef:
        """
        Creates a new image pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_image_pipeline)
        """

    def create_image_recipe(
        self,
        *,
        name: str,
        semanticVersion: str,
        components: List["ComponentConfigurationTypeDef"],
        parentImage: str,
        clientToken: str,
        description: str = None,
        blockDeviceMappings: List["InstanceBlockDeviceMappingTypeDef"] = None,
        tags: Dict[str, str] = None,
        workingDirectory: str = None,
        additionalInstanceConfiguration: "AdditionalInstanceConfigurationTypeDef" = None
    ) -> CreateImageRecipeResponseTypeDef:
        """
        Creates a new image recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_image_recipe)
        """

    def create_infrastructure_configuration(
        self,
        *,
        name: str,
        instanceProfileName: str,
        clientToken: str,
        description: str = None,
        instanceTypes: List[str] = None,
        securityGroupIds: List[str] = None,
        subnetId: str = None,
        logging: "LoggingTypeDef" = None,
        keyPair: str = None,
        terminateInstanceOnFailure: bool = None,
        snsTopicArn: str = None,
        resourceTags: Dict[str, str] = None,
        instanceMetadataOptions: "InstanceMetadataOptionsTypeDef" = None,
        tags: Dict[str, str] = None
    ) -> CreateInfrastructureConfigurationResponseTypeDef:
        """
        Creates a new infrastructure configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_infrastructure_configuration)
        """

    def create_lifecycle_policy(
        self,
        *,
        name: str,
        executionRole: str,
        resourceType: LifecyclePolicyResourceTypeType,
        policyDetails: List["LifecyclePolicyDetailTypeDef"],
        resourceSelection: "LifecyclePolicyResourceSelectionTypeDef",
        clientToken: str,
        description: str = None,
        status: LifecyclePolicyStatusType = None,
        tags: Dict[str, str] = None
    ) -> CreateLifecyclePolicyResponseTypeDef:
        """
        Create a lifecycle policy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_lifecycle_policy)
        """

    def create_workflow(
        self,
        *,
        name: str,
        semanticVersion: str,
        clientToken: str,
        type: WorkflowTypeType,
        description: str = None,
        changeDescription: str = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None
    ) -> CreateWorkflowResponseTypeDef:
        """
        Create a new workflow or a new version of an existing workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.create_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_workflow)
        """

    def delete_component(self, *, componentBuildVersionArn: str) -> DeleteComponentResponseTypeDef:
        """
        Deletes a component build version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_component)
        """

    def delete_container_recipe(
        self, *, containerRecipeArn: str
    ) -> DeleteContainerRecipeResponseTypeDef:
        """
        Deletes a container recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_container_recipe)
        """

    def delete_distribution_configuration(
        self, *, distributionConfigurationArn: str
    ) -> DeleteDistributionConfigurationResponseTypeDef:
        """
        Deletes a distribution configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_distribution_configuration)
        """

    def delete_image(self, *, imageBuildVersionArn: str) -> DeleteImageResponseTypeDef:
        """
        Deletes an Image Builder image resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image)
        """

    def delete_image_pipeline(self, *, imagePipelineArn: str) -> DeleteImagePipelineResponseTypeDef:
        """
        Deletes an image pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image_pipeline)
        """

    def delete_image_recipe(self, *, imageRecipeArn: str) -> DeleteImageRecipeResponseTypeDef:
        """
        Deletes an image recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image_recipe)
        """

    def delete_infrastructure_configuration(
        self, *, infrastructureConfigurationArn: str
    ) -> DeleteInfrastructureConfigurationResponseTypeDef:
        """
        Deletes an infrastructure configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_infrastructure_configuration)
        """

    def delete_lifecycle_policy(
        self, *, lifecyclePolicyArn: str
    ) -> DeleteLifecyclePolicyResponseTypeDef:
        """
        Delete the specified lifecycle policy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_lifecycle_policy)
        """

    def delete_workflow(self, *, workflowBuildVersionArn: str) -> DeleteWorkflowResponseTypeDef:
        """
        Deletes a specific workflow resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.delete_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_workflow)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#generate_presigned_url)
        """

    def get_component(self, *, componentBuildVersionArn: str) -> GetComponentResponseTypeDef:
        """
        Gets a component object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_component)
        """

    def get_component_policy(self, *, componentArn: str) -> GetComponentPolicyResponseTypeDef:
        """
        Gets a component policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_component_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_component_policy)
        """

    def get_container_recipe(self, *, containerRecipeArn: str) -> GetContainerRecipeResponseTypeDef:
        """
        Retrieves a container recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_container_recipe)
        """

    def get_container_recipe_policy(
        self, *, containerRecipeArn: str
    ) -> GetContainerRecipePolicyResponseTypeDef:
        """
        Retrieves the policy for a container recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_container_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_container_recipe_policy)
        """

    def get_distribution_configuration(
        self, *, distributionConfigurationArn: str
    ) -> GetDistributionConfigurationResponseTypeDef:
        """
        Gets a distribution configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_distribution_configuration)
        """

    def get_image(self, *, imageBuildVersionArn: str) -> GetImageResponseTypeDef:
        """
        Gets an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image)
        """

    def get_image_pipeline(self, *, imagePipelineArn: str) -> GetImagePipelineResponseTypeDef:
        """
        Gets an image pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_pipeline)
        """

    def get_image_policy(self, *, imageArn: str) -> GetImagePolicyResponseTypeDef:
        """
        Gets an image policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_image_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_policy)
        """

    def get_image_recipe(self, *, imageRecipeArn: str) -> GetImageRecipeResponseTypeDef:
        """
        Gets an image recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_recipe)
        """

    def get_image_recipe_policy(
        self, *, imageRecipeArn: str
    ) -> GetImageRecipePolicyResponseTypeDef:
        """
        Gets an image recipe policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_image_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_recipe_policy)
        """

    def get_infrastructure_configuration(
        self, *, infrastructureConfigurationArn: str
    ) -> GetInfrastructureConfigurationResponseTypeDef:
        """
        Gets an infrastructure configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_infrastructure_configuration)
        """

    def get_lifecycle_execution(
        self, *, lifecycleExecutionId: str
    ) -> GetLifecycleExecutionResponseTypeDef:
        """
        Get the runtime information that was logged for a specific runtime instance of
        the lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_lifecycle_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_lifecycle_execution)
        """

    def get_lifecycle_policy(self, *, lifecyclePolicyArn: str) -> GetLifecyclePolicyResponseTypeDef:
        """
        Get details for the specified image lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_lifecycle_policy)
        """

    def get_workflow(self, *, workflowBuildVersionArn: str) -> GetWorkflowResponseTypeDef:
        """
        Get a workflow resource object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_workflow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_workflow)
        """

    def get_workflow_execution(
        self, *, workflowExecutionId: str
    ) -> GetWorkflowExecutionResponseTypeDef:
        """
        Get the runtime information that was logged for a specific runtime instance of
        the workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_workflow_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_workflow_execution)
        """

    def get_workflow_step_execution(
        self, *, stepExecutionId: str
    ) -> GetWorkflowStepExecutionResponseTypeDef:
        """
        Get the runtime information that was logged for a specific runtime instance of
        the workflow step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.get_workflow_step_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_workflow_step_execution)
        """

    def import_component(
        self,
        *,
        name: str,
        semanticVersion: str,
        type: ComponentTypeType,
        format: Literal["SHELL"],
        platform: PlatformType,
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None
    ) -> ImportComponentResponseTypeDef:
        """
        Imports a component and transforms its data into a component document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.import_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#import_component)
        """

    def import_vm_image(
        self,
        *,
        name: str,
        semanticVersion: str,
        platform: PlatformType,
        vmImportTaskId: str,
        clientToken: str,
        description: str = None,
        osVersion: str = None,
        tags: Dict[str, str] = None
    ) -> ImportVmImageResponseTypeDef:
        """
        When you export your virtual machine (VM) from its virtualization environment,
        that process creates a set of one or more disk container files that act as
        snapshots of your VM’s environment, settings, and data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.import_vm_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#import_vm_image)
        """

    def list_component_build_versions(
        self, *, componentVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListComponentBuildVersionsResponseTypeDef:
        """
        Returns the list of component build versions for the specified semantic version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_component_build_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_component_build_versions)
        """

    def list_components(
        self,
        *,
        owner: OwnershipType = None,
        filters: List["FilterTypeDef"] = None,
        byName: bool = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListComponentsResponseTypeDef:
        """
        Returns the list of components that can be filtered by name, or by using the
        listed `filters` to streamline results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_components)
        """

    def list_container_recipes(
        self,
        *,
        owner: OwnershipType = None,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListContainerRecipesResponseTypeDef:
        """
        Returns a list of container recipes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_container_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_container_recipes)
        """

    def list_distribution_configurations(
        self,
        *,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListDistributionConfigurationsResponseTypeDef:
        """
        Returns a list of distribution configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_distribution_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_distribution_configurations)
        """

    def list_image_build_versions(
        self,
        *,
        imageVersionArn: str,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImageBuildVersionsResponseTypeDef:
        """
        Returns a list of image build versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_image_build_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_build_versions)
        """

    def list_image_packages(
        self, *, imageBuildVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListImagePackagesResponseTypeDef:
        """
        List the Packages that are associated with an Image Build Version, as determined
        by Amazon Web Services Systems Manager Inventory at build time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_image_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_packages)
        """

    def list_image_pipeline_images(
        self,
        *,
        imagePipelineArn: str,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImagePipelineImagesResponseTypeDef:
        """
        Returns a list of images created by the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_image_pipeline_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_pipeline_images)
        """

    def list_image_pipelines(
        self,
        *,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImagePipelinesResponseTypeDef:
        """
        Returns a list of image pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_image_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_pipelines)
        """

    def list_image_recipes(
        self,
        *,
        owner: OwnershipType = None,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImageRecipesResponseTypeDef:
        """
        Returns a list of image recipes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_image_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_recipes)
        """

    def list_image_scan_finding_aggregations(
        self, *, filter: "FilterTypeDef" = None, nextToken: str = None
    ) -> ListImageScanFindingAggregationsResponseTypeDef:
        """
        Returns a list of image scan aggregations for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_image_scan_finding_aggregations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_scan_finding_aggregations)
        """

    def list_image_scan_findings(
        self,
        *,
        filters: List["ImageScanFindingsFilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListImageScanFindingsResponseTypeDef:
        """
        Returns a list of image scan findings for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_image_scan_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_scan_findings)
        """

    def list_images(
        self,
        *,
        owner: OwnershipType = None,
        filters: List["FilterTypeDef"] = None,
        byName: bool = None,
        maxResults: int = None,
        nextToken: str = None,
        includeDeprecated: bool = None
    ) -> ListImagesResponseTypeDef:
        """
        Returns the list of images that you have access to.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_images)
        """

    def list_infrastructure_configurations(
        self,
        *,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListInfrastructureConfigurationsResponseTypeDef:
        """
        Returns a list of infrastructure configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_infrastructure_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_infrastructure_configurations)
        """

    def list_lifecycle_execution_resources(
        self,
        *,
        lifecycleExecutionId: str,
        parentResourceId: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListLifecycleExecutionResourcesResponseTypeDef:
        """
        List resources that the runtime instance of the image lifecycle identified for
        lifecycle actions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_lifecycle_execution_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_lifecycle_execution_resources)
        """

    def list_lifecycle_executions(
        self, *, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListLifecycleExecutionsResponseTypeDef:
        """
        Get the lifecycle runtime history for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_lifecycle_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_lifecycle_executions)
        """

    def list_lifecycle_policies(
        self,
        *,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListLifecyclePoliciesResponseTypeDef:
        """
        Get a list of lifecycle policies in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_lifecycle_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_lifecycle_policies)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the list of tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_tags_for_resource)
        """

    def list_waiting_workflow_steps(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListWaitingWorkflowStepsResponseTypeDef:
        """
        Get a list of workflow steps that are waiting for action for workflows in your
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_waiting_workflow_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_waiting_workflow_steps)
        """

    def list_workflow_build_versions(
        self, *, workflowVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListWorkflowBuildVersionsResponseTypeDef:
        """
        Returns a list of build versions for a specific workflow resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_workflow_build_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_workflow_build_versions)
        """

    def list_workflow_executions(
        self, *, imageBuildVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListWorkflowExecutionsResponseTypeDef:
        """
        Returns a list of workflow runtime instance metadata objects for a specific
        image build version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_workflow_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_workflow_executions)
        """

    def list_workflow_step_executions(
        self, *, workflowExecutionId: str, maxResults: int = None, nextToken: str = None
    ) -> ListWorkflowStepExecutionsResponseTypeDef:
        """
        Returns runtime data for each step in a runtime instance of the workflow that
        you specify in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_workflow_step_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_workflow_step_executions)
        """

    def list_workflows(
        self,
        *,
        owner: OwnershipType = None,
        filters: List["FilterTypeDef"] = None,
        byName: bool = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> ListWorkflowsResponseTypeDef:
        """
        Lists workflow build versions based on filtering parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.list_workflows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_workflows)
        """

    def put_component_policy(
        self, *, componentArn: str, policy: str
    ) -> PutComponentPolicyResponseTypeDef:
        """
        Applies a policy to a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.put_component_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_component_policy)
        """

    def put_container_recipe_policy(
        self, *, containerRecipeArn: str, policy: str
    ) -> PutContainerRecipePolicyResponseTypeDef:
        """
        Applies a policy to a container image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.put_container_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_container_recipe_policy)
        """

    def put_image_policy(self, *, imageArn: str, policy: str) -> PutImagePolicyResponseTypeDef:
        """
        Applies a policy to an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.put_image_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_image_policy)
        """

    def put_image_recipe_policy(
        self, *, imageRecipeArn: str, policy: str
    ) -> PutImageRecipePolicyResponseTypeDef:
        """
        Applies a policy to an image recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.put_image_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_image_recipe_policy)
        """

    def send_workflow_step_action(
        self,
        *,
        stepExecutionId: str,
        imageBuildVersionArn: str,
        action: WorkflowStepActionTypeType,
        clientToken: str,
        reason: str = None
    ) -> SendWorkflowStepActionResponseTypeDef:
        """
        Pauses or resumes image creation when the associated workflow runs a
        `WaitForAction` step.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.send_workflow_step_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#send_workflow_step_action)
        """

    def start_image_pipeline_execution(
        self, *, imagePipelineArn: str, clientToken: str
    ) -> StartImagePipelineExecutionResponseTypeDef:
        """
        Manually triggers a pipeline to create an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.start_image_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#start_image_pipeline_execution)
        """

    def start_resource_state_update(
        self,
        *,
        resourceArn: str,
        state: "ResourceStateTypeDef",
        clientToken: str,
        executionRole: str = None,
        includeResources: "ResourceStateUpdateIncludeResourcesTypeDef" = None,
        exclusionRules: "ResourceStateUpdateExclusionRulesTypeDef" = None,
        updateAt: Union[datetime, str] = None
    ) -> StartResourceStateUpdateResponseTypeDef:
        """
        Begin asynchronous resource state update for lifecycle changes to the specified
        image resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.start_resource_state_update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#start_resource_state_update)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#untag_resource)
        """

    def update_distribution_configuration(
        self,
        *,
        distributionConfigurationArn: str,
        distributions: List["DistributionTypeDef"],
        clientToken: str,
        description: str = None
    ) -> UpdateDistributionConfigurationResponseTypeDef:
        """
        Updates a new distribution configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.update_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update_distribution_configuration)
        """

    def update_image_pipeline(
        self,
        *,
        imagePipelineArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        imageRecipeArn: str = None,
        containerRecipeArn: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        schedule: "ScheduleTypeDef" = None,
        status: PipelineStatusType = None,
        imageScanningConfiguration: "ImageScanningConfigurationTypeDef" = None,
        workflows: List["WorkflowConfigurationTypeDef"] = None,
        executionRole: str = None
    ) -> UpdateImagePipelineResponseTypeDef:
        """
        Updates an image pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.update_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update_image_pipeline)
        """

    def update_infrastructure_configuration(
        self,
        *,
        infrastructureConfigurationArn: str,
        instanceProfileName: str,
        clientToken: str,
        description: str = None,
        instanceTypes: List[str] = None,
        securityGroupIds: List[str] = None,
        subnetId: str = None,
        logging: "LoggingTypeDef" = None,
        keyPair: str = None,
        terminateInstanceOnFailure: bool = None,
        snsTopicArn: str = None,
        resourceTags: Dict[str, str] = None,
        instanceMetadataOptions: "InstanceMetadataOptionsTypeDef" = None
    ) -> UpdateInfrastructureConfigurationResponseTypeDef:
        """
        Updates a new infrastructure configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.update_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update_infrastructure_configuration)
        """

    def update_lifecycle_policy(
        self,
        *,
        lifecyclePolicyArn: str,
        executionRole: str,
        resourceType: LifecyclePolicyResourceTypeType,
        policyDetails: List["LifecyclePolicyDetailTypeDef"],
        resourceSelection: "LifecyclePolicyResourceSelectionTypeDef",
        clientToken: str,
        description: str = None,
        status: LifecyclePolicyStatusType = None
    ) -> UpdateLifecyclePolicyResponseTypeDef:
        """
        Update the specified lifecycle policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/imagebuilder.html#imagebuilder.Client.update_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update_lifecycle_policy)
        """
