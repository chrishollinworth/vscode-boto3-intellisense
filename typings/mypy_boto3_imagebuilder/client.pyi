# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for imagebuilder service client

Usage::

    ```python
    import boto3
    from mypy_boto3_imagebuilder import ImagebuilderClient

    client: ImagebuilderClient = boto3.client("imagebuilder")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_imagebuilder.type_defs import (
    CancelImageCreationResponseTypeDef,
    ComponentConfigurationTypeDef,
    CreateComponentResponseTypeDef,
    CreateDistributionConfigurationResponseTypeDef,
    CreateImagePipelineResponseTypeDef,
    CreateImageRecipeResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateInfrastructureConfigurationResponseTypeDef,
    DeleteComponentResponseTypeDef,
    DeleteDistributionConfigurationResponseTypeDef,
    DeleteImagePipelineResponseTypeDef,
    DeleteImageRecipeResponseTypeDef,
    DeleteImageResponseTypeDef,
    DeleteInfrastructureConfigurationResponseTypeDef,
    DistributionTypeDef,
    FilterTypeDef,
    GetComponentPolicyResponseTypeDef,
    GetComponentResponseTypeDef,
    GetDistributionConfigurationResponseTypeDef,
    GetImagePipelineResponseTypeDef,
    GetImagePolicyResponseTypeDef,
    GetImageRecipePolicyResponseTypeDef,
    GetImageRecipeResponseTypeDef,
    GetImageResponseTypeDef,
    GetInfrastructureConfigurationResponseTypeDef,
    ImageTestsConfigurationTypeDef,
    ImportComponentResponseTypeDef,
    InstanceBlockDeviceMappingTypeDef,
    ListComponentBuildVersionsResponseTypeDef,
    ListComponentsResponseTypeDef,
    ListDistributionConfigurationsResponseTypeDef,
    ListImageBuildVersionsResponseTypeDef,
    ListImagePipelineImagesResponseTypeDef,
    ListImagePipelinesResponseTypeDef,
    ListImageRecipesResponseTypeDef,
    ListImagesResponseTypeDef,
    ListInfrastructureConfigurationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingTypeDef,
    PutComponentPolicyResponseTypeDef,
    PutImagePolicyResponseTypeDef,
    PutImageRecipePolicyResponseTypeDef,
    ScheduleTypeDef,
    StartImagePipelineExecutionResponseTypeDef,
    UpdateDistributionConfigurationResponseTypeDef,
    UpdateImagePipelineResponseTypeDef,
    UpdateInfrastructureConfigurationResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ImagebuilderClient",)


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


class ImagebuilderClient:
    """
    [Imagebuilder.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.can_paginate)
        """

    def cancel_image_creation(
        self, imageBuildVersionArn: str, clientToken: str
    ) -> CancelImageCreationResponseTypeDef:
        """
        [Client.cancel_image_creation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.cancel_image_creation)
        """

    def create_component(
        self,
        name: str,
        semanticVersion: str,
        platform: Literal["Windows", "Linux"],
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        supportedOsVersions: List[str] = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateComponentResponseTypeDef:
        """
        [Client.create_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.create_component)
        """

    def create_distribution_configuration(
        self,
        name: str,
        distributions: List["DistributionTypeDef"],
        clientToken: str,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateDistributionConfigurationResponseTypeDef:
        """
        [Client.create_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.create_distribution_configuration)
        """

    def create_image(
        self,
        imageRecipeArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        tags: Dict[str, str] = None,
    ) -> CreateImageResponseTypeDef:
        """
        [Client.create_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.create_image)
        """

    def create_image_pipeline(
        self,
        name: str,
        imageRecipeArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        schedule: "ScheduleTypeDef" = None,
        status: Literal["DISABLED", "ENABLED"] = None,
        tags: Dict[str, str] = None,
    ) -> CreateImagePipelineResponseTypeDef:
        """
        [Client.create_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.create_image_pipeline)
        """

    def create_image_recipe(
        self,
        name: str,
        semanticVersion: str,
        components: List["ComponentConfigurationTypeDef"],
        parentImage: str,
        clientToken: str,
        description: str = None,
        blockDeviceMappings: List["InstanceBlockDeviceMappingTypeDef"] = None,
        tags: Dict[str, str] = None,
        workingDirectory: str = None,
    ) -> CreateImageRecipeResponseTypeDef:
        """
        [Client.create_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.create_image_recipe)
        """

    def create_infrastructure_configuration(
        self,
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
        tags: Dict[str, str] = None,
    ) -> CreateInfrastructureConfigurationResponseTypeDef:
        """
        [Client.create_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.create_infrastructure_configuration)
        """

    def delete_component(self, componentBuildVersionArn: str) -> DeleteComponentResponseTypeDef:
        """
        [Client.delete_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.delete_component)
        """

    def delete_distribution_configuration(
        self, distributionConfigurationArn: str
    ) -> DeleteDistributionConfigurationResponseTypeDef:
        """
        [Client.delete_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.delete_distribution_configuration)
        """

    def delete_image(self, imageBuildVersionArn: str) -> DeleteImageResponseTypeDef:
        """
        [Client.delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image)
        """

    def delete_image_pipeline(self, imagePipelineArn: str) -> DeleteImagePipelineResponseTypeDef:
        """
        [Client.delete_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image_pipeline)
        """

    def delete_image_recipe(self, imageRecipeArn: str) -> DeleteImageRecipeResponseTypeDef:
        """
        [Client.delete_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.delete_image_recipe)
        """

    def delete_infrastructure_configuration(
        self, infrastructureConfigurationArn: str
    ) -> DeleteInfrastructureConfigurationResponseTypeDef:
        """
        [Client.delete_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.delete_infrastructure_configuration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.generate_presigned_url)
        """

    def get_component(self, componentBuildVersionArn: str) -> GetComponentResponseTypeDef:
        """
        [Client.get_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_component)
        """

    def get_component_policy(self, componentArn: str) -> GetComponentPolicyResponseTypeDef:
        """
        [Client.get_component_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_component_policy)
        """

    def get_distribution_configuration(
        self, distributionConfigurationArn: str
    ) -> GetDistributionConfigurationResponseTypeDef:
        """
        [Client.get_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_distribution_configuration)
        """

    def get_image(self, imageBuildVersionArn: str) -> GetImageResponseTypeDef:
        """
        [Client.get_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_image)
        """

    def get_image_pipeline(self, imagePipelineArn: str) -> GetImagePipelineResponseTypeDef:
        """
        [Client.get_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_pipeline)
        """

    def get_image_policy(self, imageArn: str) -> GetImagePolicyResponseTypeDef:
        """
        [Client.get_image_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_policy)
        """

    def get_image_recipe(self, imageRecipeArn: str) -> GetImageRecipeResponseTypeDef:
        """
        [Client.get_image_recipe documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_recipe)
        """

    def get_image_recipe_policy(self, imageRecipeArn: str) -> GetImageRecipePolicyResponseTypeDef:
        """
        [Client.get_image_recipe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_image_recipe_policy)
        """

    def get_infrastructure_configuration(
        self, infrastructureConfigurationArn: str
    ) -> GetInfrastructureConfigurationResponseTypeDef:
        """
        [Client.get_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.get_infrastructure_configuration)
        """

    def import_component(
        self,
        name: str,
        semanticVersion: str,
        type: Literal["BUILD", "TEST"],
        format: Literal["SHELL"],
        platform: Literal["Windows", "Linux"],
        clientToken: str,
        description: str = None,
        changeDescription: str = None,
        data: str = None,
        uri: str = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None,
    ) -> ImportComponentResponseTypeDef:
        """
        [Client.import_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.import_component)
        """

    def list_component_build_versions(
        self, componentVersionArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListComponentBuildVersionsResponseTypeDef:
        """
        [Client.list_component_build_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_component_build_versions)
        """

    def list_components(
        self,
        owner: Literal["Self", "Shared", "Amazon"] = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListComponentsResponseTypeDef:
        """
        [Client.list_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_components)
        """

    def list_distribution_configurations(
        self, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListDistributionConfigurationsResponseTypeDef:
        """
        [Client.list_distribution_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_distribution_configurations)
        """

    def list_image_build_versions(
        self,
        imageVersionArn: str,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListImageBuildVersionsResponseTypeDef:
        """
        [Client.list_image_build_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_build_versions)
        """

    def list_image_pipeline_images(
        self,
        imagePipelineArn: str,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListImagePipelineImagesResponseTypeDef:
        """
        [Client.list_image_pipeline_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_pipeline_images)
        """

    def list_image_pipelines(
        self, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListImagePipelinesResponseTypeDef:
        """
        [Client.list_image_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_pipelines)
        """

    def list_image_recipes(
        self,
        owner: Literal["Self", "Shared", "Amazon"] = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListImageRecipesResponseTypeDef:
        """
        [Client.list_image_recipes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_image_recipes)
        """

    def list_images(
        self,
        owner: Literal["Self", "Shared", "Amazon"] = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListImagesResponseTypeDef:
        """
        [Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_images)
        """

    def list_infrastructure_configurations(
        self, filters: List[FilterTypeDef] = None, maxResults: int = None, nextToken: str = None
    ) -> ListInfrastructureConfigurationsResponseTypeDef:
        """
        [Client.list_infrastructure_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_infrastructure_configurations)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.list_tags_for_resource)
        """

    def put_component_policy(
        self, componentArn: str, policy: str
    ) -> PutComponentPolicyResponseTypeDef:
        """
        [Client.put_component_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.put_component_policy)
        """

    def put_image_policy(self, imageArn: str, policy: str) -> PutImagePolicyResponseTypeDef:
        """
        [Client.put_image_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.put_image_policy)
        """

    def put_image_recipe_policy(
        self, imageRecipeArn: str, policy: str
    ) -> PutImageRecipePolicyResponseTypeDef:
        """
        [Client.put_image_recipe_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.put_image_recipe_policy)
        """

    def start_image_pipeline_execution(
        self, imagePipelineArn: str, clientToken: str
    ) -> StartImagePipelineExecutionResponseTypeDef:
        """
        [Client.start_image_pipeline_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.start_image_pipeline_execution)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.untag_resource)
        """

    def update_distribution_configuration(
        self,
        distributionConfigurationArn: str,
        distributions: List["DistributionTypeDef"],
        clientToken: str,
        description: str = None,
    ) -> UpdateDistributionConfigurationResponseTypeDef:
        """
        [Client.update_distribution_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.update_distribution_configuration)
        """

    def update_image_pipeline(
        self,
        imagePipelineArn: str,
        imageRecipeArn: str,
        infrastructureConfigurationArn: str,
        clientToken: str,
        description: str = None,
        distributionConfigurationArn: str = None,
        imageTestsConfiguration: "ImageTestsConfigurationTypeDef" = None,
        enhancedImageMetadataEnabled: bool = None,
        schedule: "ScheduleTypeDef" = None,
        status: Literal["DISABLED", "ENABLED"] = None,
    ) -> UpdateImagePipelineResponseTypeDef:
        """
        [Client.update_image_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.update_image_pipeline)
        """

    def update_infrastructure_configuration(
        self,
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
    ) -> UpdateInfrastructureConfigurationResponseTypeDef:
        """
        [Client.update_infrastructure_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/imagebuilder.html#Imagebuilder.Client.update_infrastructure_configuration)
        """
