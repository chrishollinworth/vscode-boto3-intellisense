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
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ComponentTypeType, OwnershipType, PipelineStatusType, PlatformType
from .type_defs import (
    AdditionalInstanceConfigurationTypeDef,
    CancelImageCreationResponseTypeDef,
    ComponentConfigurationTypeDef,
    CreateComponentResponseTypeDef,
    CreateContainerRecipeResponseTypeDef,
    CreateDistributionConfigurationResponseTypeDef,
    CreateImagePipelineResponseTypeDef,
    CreateImageRecipeResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateInfrastructureConfigurationResponseTypeDef,
    DeleteComponentResponseTypeDef,
    DeleteContainerRecipeResponseTypeDef,
    DeleteDistributionConfigurationResponseTypeDef,
    DeleteImagePipelineResponseTypeDef,
    DeleteImageRecipeResponseTypeDef,
    DeleteImageResponseTypeDef,
    DeleteInfrastructureConfigurationResponseTypeDef,
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
    ImageTestsConfigurationTypeDef,
    ImportComponentResponseTypeDef,
    ImportVmImageResponseTypeDef,
    InstanceBlockDeviceMappingTypeDef,
    InstanceConfigurationTypeDef,
    InstanceMetadataOptionsTypeDef,
    ListComponentBuildVersionsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListContainerRecipesResponseTypeDef,
    ListDistributionConfigurationsResponseTypeDef,
    ListImageBuildVersionsResponseTypeDef,
    ListImagePackagesResponseTypeDef,
    ListImagePipelineImagesResponseTypeDef,
    ListImagePipelinesResponseTypeDef,
    ListImageRecipesResponseTypeDef,
    ListImagesResponseTypeDef,
    ListInfrastructureConfigurationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingTypeDef,
    PutComponentPolicyResponseTypeDef,
    PutContainerRecipePolicyResponseTypeDef,
    PutImagePolicyResponseTypeDef,
    PutImageRecipePolicyResponseTypeDef,
    ScheduleTypeDef,
    StartImagePipelineExecutionResponseTypeDef,
    TargetContainerRepositoryTypeDef,
    UpdateDistributionConfigurationResponseTypeDef,
    UpdateImagePipelineResponseTypeDef,
    UpdateInfrastructureConfigurationResponseTypeDef,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#can_paginate)
        """
    def cancel_image_creation(
        self, *, imageBuildVersionArn: str, clientToken: str
    ) -> CancelImageCreationResponseTypeDef:
        """
        CancelImageCreation cancels the creation of Image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.cancel_image_creation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#cancel_image_creation)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.create_component)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.create_container_recipe)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.create_distribution_configuration)
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
        tags: Dict[str, str] = None
    ) -> CreateImageResponseTypeDef:
        """
        Creates a new image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.create_image)
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
        tags: Dict[str, str] = None
    ) -> CreateImagePipelineResponseTypeDef:
        """
        Creates a new image pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.create_image_pipeline)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.create_image_recipe)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.create_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#create_infrastructure_configuration)
        """
    def delete_component(self, *, componentBuildVersionArn: str) -> DeleteComponentResponseTypeDef:
        """
        Deletes a component build version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.delete_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_component)
        """
    def delete_container_recipe(
        self, *, containerRecipeArn: str
    ) -> DeleteContainerRecipeResponseTypeDef:
        """
        Deletes a container recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.delete_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_container_recipe)
        """
    def delete_distribution_configuration(
        self, *, distributionConfigurationArn: str
    ) -> DeleteDistributionConfigurationResponseTypeDef:
        """
        Deletes a distribution configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.delete_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_distribution_configuration)
        """
    def delete_image(self, *, imageBuildVersionArn: str) -> DeleteImageResponseTypeDef:
        """
        Deletes an Image Builder image resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image)
        """
    def delete_image_pipeline(self, *, imagePipelineArn: str) -> DeleteImagePipelineResponseTypeDef:
        """
        Deletes an image pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.delete_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image_pipeline)
        """
    def delete_image_recipe(self, *, imageRecipeArn: str) -> DeleteImageRecipeResponseTypeDef:
        """
        Deletes an image recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.delete_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_image_recipe)
        """
    def delete_infrastructure_configuration(
        self, *, infrastructureConfigurationArn: str
    ) -> DeleteInfrastructureConfigurationResponseTypeDef:
        """
        Deletes an infrastructure configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.delete_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#delete_infrastructure_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#generate_presigned_url)
        """
    def get_component(self, *, componentBuildVersionArn: str) -> GetComponentResponseTypeDef:
        """
        Gets a component object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_component)
        """
    def get_component_policy(self, *, componentArn: str) -> GetComponentPolicyResponseTypeDef:
        """
        Gets a component policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_component_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_component_policy)
        """
    def get_container_recipe(self, *, containerRecipeArn: str) -> GetContainerRecipeResponseTypeDef:
        """
        Retrieves a container recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_container_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_container_recipe)
        """
    def get_container_recipe_policy(
        self, *, containerRecipeArn: str
    ) -> GetContainerRecipePolicyResponseTypeDef:
        """
        Retrieves the policy for a container recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_container_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_container_recipe_policy)
        """
    def get_distribution_configuration(
        self, *, distributionConfigurationArn: str
    ) -> GetDistributionConfigurationResponseTypeDef:
        """
        Gets a distribution configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_distribution_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_distribution_configuration)
        """
    def get_image(self, *, imageBuildVersionArn: str) -> GetImageResponseTypeDef:
        """
        Gets an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image)
        """
    def get_image_pipeline(self, *, imagePipelineArn: str) -> GetImagePipelineResponseTypeDef:
        """
        Gets an image pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_image_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_pipeline)
        """
    def get_image_policy(self, *, imageArn: str) -> GetImagePolicyResponseTypeDef:
        """
        Gets an image policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_image_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_policy)
        """
    def get_image_recipe(self, *, imageRecipeArn: str) -> GetImageRecipeResponseTypeDef:
        """
        Gets an image recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_image_recipe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_recipe)
        """
    def get_image_recipe_policy(
        self, *, imageRecipeArn: str
    ) -> GetImageRecipePolicyResponseTypeDef:
        """
        Gets an image recipe policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_image_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_image_recipe_policy)
        """
    def get_infrastructure_configuration(
        self, *, infrastructureConfigurationArn: str
    ) -> GetInfrastructureConfigurationResponseTypeDef:
        """
        Gets an infrastructure configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.get_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#get_infrastructure_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.import_component)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.import_vm_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#import_vm_image)
        """
    def list_component_build_versions(
        self, *, componentVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListComponentBuildVersionsResponseTypeDef:
        """
        Returns the list of component build versions for the specified semantic version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_component_build_versions)
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
        Returns the list of component build versions for the specified semantic version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_components)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_container_recipes)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_distribution_configurations)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_image_build_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_build_versions)
        """
    def list_image_packages(
        self, *, imageBuildVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListImagePackagesResponseTypeDef:
        """
        List the Packages that are associated with an Image Build Version, as determined
        by Amazon Web Services Systems Manager Inventory at build time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_image_packages)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_image_pipeline_images)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_image_pipelines)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_image_recipes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_image_recipes)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_images)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_infrastructure_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_infrastructure_configurations)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the list of tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#list_tags_for_resource)
        """
    def put_component_policy(
        self, *, componentArn: str, policy: str
    ) -> PutComponentPolicyResponseTypeDef:
        """
        Applies a policy to a component.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.put_component_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_component_policy)
        """
    def put_container_recipe_policy(
        self, *, containerRecipeArn: str, policy: str
    ) -> PutContainerRecipePolicyResponseTypeDef:
        """
        Applies a policy to a container image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.put_container_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_container_recipe_policy)
        """
    def put_image_policy(self, *, imageArn: str, policy: str) -> PutImagePolicyResponseTypeDef:
        """
        Applies a policy to an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.put_image_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_image_policy)
        """
    def put_image_recipe_policy(
        self, *, imageRecipeArn: str, policy: str
    ) -> PutImageRecipePolicyResponseTypeDef:
        """
        Applies a policy to an image recipe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.put_image_recipe_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#put_image_recipe_policy)
        """
    def start_image_pipeline_execution(
        self, *, imagePipelineArn: str, clientToken: str
    ) -> StartImagePipelineExecutionResponseTypeDef:
        """
        Manually triggers a pipeline to create an image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.start_image_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#start_image_pipeline_execution)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds a tag to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.untag_resource)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.update_distribution_configuration)
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
        status: PipelineStatusType = None
    ) -> UpdateImagePipelineResponseTypeDef:
        """
        Updates an image pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.update_image_pipeline)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/imagebuilder.html#imagebuilder.Client.update_infrastructure_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/client.html#update_infrastructure_configuration)
        """
