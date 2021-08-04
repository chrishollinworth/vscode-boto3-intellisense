"""
Type annotations for imagebuilder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_imagebuilder.type_defs import AdditionalInstanceConfigurationTypeDef

    data: AdditionalInstanceConfigurationTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    ComponentTypeType,
    EbsVolumeTypeType,
    ImageStatusType,
    ImageTypeType,
    OwnershipType,
    PipelineExecutionStartConditionType,
    PipelineStatusType,
    PlatformType,
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
    "AdditionalInstanceConfigurationTypeDef",
    "AmiDistributionConfigurationTypeDef",
    "AmiTypeDef",
    "CancelImageCreationRequestRequestTypeDef",
    "CancelImageCreationResponseTypeDef",
    "ComponentConfigurationTypeDef",
    "ComponentParameterDetailTypeDef",
    "ComponentParameterTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVersionTypeDef",
    "ContainerDistributionConfigurationTypeDef",
    "ContainerRecipeSummaryTypeDef",
    "ContainerRecipeTypeDef",
    "ContainerTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateContainerRecipeRequestRequestTypeDef",
    "CreateContainerRecipeResponseTypeDef",
    "CreateDistributionConfigurationRequestRequestTypeDef",
    "CreateDistributionConfigurationResponseTypeDef",
    "CreateImagePipelineRequestRequestTypeDef",
    "CreateImagePipelineResponseTypeDef",
    "CreateImageRecipeRequestRequestTypeDef",
    "CreateImageRecipeResponseTypeDef",
    "CreateImageRequestRequestTypeDef",
    "CreateImageResponseTypeDef",
    "CreateInfrastructureConfigurationRequestRequestTypeDef",
    "CreateInfrastructureConfigurationResponseTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteComponentResponseTypeDef",
    "DeleteContainerRecipeRequestRequestTypeDef",
    "DeleteContainerRecipeResponseTypeDef",
    "DeleteDistributionConfigurationRequestRequestTypeDef",
    "DeleteDistributionConfigurationResponseTypeDef",
    "DeleteImagePipelineRequestRequestTypeDef",
    "DeleteImagePipelineResponseTypeDef",
    "DeleteImageRecipeRequestRequestTypeDef",
    "DeleteImageRecipeResponseTypeDef",
    "DeleteImageRequestRequestTypeDef",
    "DeleteImageResponseTypeDef",
    "DeleteInfrastructureConfigurationRequestRequestTypeDef",
    "DeleteInfrastructureConfigurationResponseTypeDef",
    "DistributionConfigurationSummaryTypeDef",
    "DistributionConfigurationTypeDef",
    "DistributionTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "FilterTypeDef",
    "GetComponentPolicyRequestRequestTypeDef",
    "GetComponentPolicyResponseTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetContainerRecipePolicyRequestRequestTypeDef",
    "GetContainerRecipePolicyResponseTypeDef",
    "GetContainerRecipeRequestRequestTypeDef",
    "GetContainerRecipeResponseTypeDef",
    "GetDistributionConfigurationRequestRequestTypeDef",
    "GetDistributionConfigurationResponseTypeDef",
    "GetImagePipelineRequestRequestTypeDef",
    "GetImagePipelineResponseTypeDef",
    "GetImagePolicyRequestRequestTypeDef",
    "GetImagePolicyResponseTypeDef",
    "GetImageRecipePolicyRequestRequestTypeDef",
    "GetImageRecipePolicyResponseTypeDef",
    "GetImageRecipeRequestRequestTypeDef",
    "GetImageRecipeResponseTypeDef",
    "GetImageRequestRequestTypeDef",
    "GetImageResponseTypeDef",
    "GetInfrastructureConfigurationRequestRequestTypeDef",
    "GetInfrastructureConfigurationResponseTypeDef",
    "ImagePackageTypeDef",
    "ImagePipelineTypeDef",
    "ImageRecipeSummaryTypeDef",
    "ImageRecipeTypeDef",
    "ImageStateTypeDef",
    "ImageSummaryTypeDef",
    "ImageTestsConfigurationTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "ImportComponentRequestRequestTypeDef",
    "ImportComponentResponseTypeDef",
    "InfrastructureConfigurationSummaryTypeDef",
    "InfrastructureConfigurationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceConfigurationTypeDef",
    "LaunchPermissionConfigurationTypeDef",
    "LaunchTemplateConfigurationTypeDef",
    "ListComponentBuildVersionsRequestRequestTypeDef",
    "ListComponentBuildVersionsResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListContainerRecipesRequestRequestTypeDef",
    "ListContainerRecipesResponseTypeDef",
    "ListDistributionConfigurationsRequestRequestTypeDef",
    "ListDistributionConfigurationsResponseTypeDef",
    "ListImageBuildVersionsRequestRequestTypeDef",
    "ListImageBuildVersionsResponseTypeDef",
    "ListImagePackagesRequestRequestTypeDef",
    "ListImagePackagesResponseTypeDef",
    "ListImagePipelineImagesRequestRequestTypeDef",
    "ListImagePipelineImagesResponseTypeDef",
    "ListImagePipelinesRequestRequestTypeDef",
    "ListImagePipelinesResponseTypeDef",
    "ListImageRecipesRequestRequestTypeDef",
    "ListImageRecipesResponseTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    "ListInfrastructureConfigurationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingTypeDef",
    "OutputResourcesTypeDef",
    "PutComponentPolicyRequestRequestTypeDef",
    "PutComponentPolicyResponseTypeDef",
    "PutContainerRecipePolicyRequestRequestTypeDef",
    "PutContainerRecipePolicyResponseTypeDef",
    "PutImagePolicyRequestRequestTypeDef",
    "PutImagePolicyResponseTypeDef",
    "PutImageRecipePolicyRequestRequestTypeDef",
    "PutImageRecipePolicyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3LogsTypeDef",
    "ScheduleTypeDef",
    "StartImagePipelineExecutionRequestRequestTypeDef",
    "StartImagePipelineExecutionResponseTypeDef",
    "SystemsManagerAgentTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetContainerRepositoryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDistributionConfigurationRequestRequestTypeDef",
    "UpdateDistributionConfigurationResponseTypeDef",
    "UpdateImagePipelineRequestRequestTypeDef",
    "UpdateImagePipelineResponseTypeDef",
    "UpdateInfrastructureConfigurationRequestRequestTypeDef",
    "UpdateInfrastructureConfigurationResponseTypeDef",
)

AdditionalInstanceConfigurationTypeDef = TypedDict(
    "AdditionalInstanceConfigurationTypeDef",
    {
        "systemsManagerAgent": "SystemsManagerAgentTypeDef",
        "userDataOverride": str,
    },
    total=False,
)

AmiDistributionConfigurationTypeDef = TypedDict(
    "AmiDistributionConfigurationTypeDef",
    {
        "name": str,
        "description": str,
        "targetAccountIds": List[str],
        "amiTags": Dict[str, str],
        "kmsKeyId": str,
        "launchPermission": "LaunchPermissionConfigurationTypeDef",
    },
    total=False,
)

AmiTypeDef = TypedDict(
    "AmiTypeDef",
    {
        "region": str,
        "image": str,
        "name": str,
        "description": str,
        "state": "ImageStateTypeDef",
        "accountId": str,
    },
    total=False,
)

CancelImageCreationRequestRequestTypeDef = TypedDict(
    "CancelImageCreationRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
        "clientToken": str,
    },
)

CancelImageCreationResponseTypeDef = TypedDict(
    "CancelImageCreationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredComponentConfigurationTypeDef = TypedDict(
    "_RequiredComponentConfigurationTypeDef",
    {
        "componentArn": str,
    },
)
_OptionalComponentConfigurationTypeDef = TypedDict(
    "_OptionalComponentConfigurationTypeDef",
    {
        "parameters": List["ComponentParameterTypeDef"],
    },
    total=False,
)

class ComponentConfigurationTypeDef(
    _RequiredComponentConfigurationTypeDef, _OptionalComponentConfigurationTypeDef
):
    pass

_RequiredComponentParameterDetailTypeDef = TypedDict(
    "_RequiredComponentParameterDetailTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalComponentParameterDetailTypeDef = TypedDict(
    "_OptionalComponentParameterDetailTypeDef",
    {
        "defaultValue": List[str],
        "description": str,
    },
    total=False,
)

class ComponentParameterDetailTypeDef(
    _RequiredComponentParameterDetailTypeDef, _OptionalComponentParameterDetailTypeDef
):
    pass

ComponentParameterTypeDef = TypedDict(
    "ComponentParameterTypeDef",
    {
        "name": str,
        "value": List[str],
    },
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "type": ComponentTypeType,
        "owner": str,
        "description": str,
        "changeDescription": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "changeDescription": str,
        "type": ComponentTypeType,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "parameters": List["ComponentParameterDetailTypeDef"],
        "owner": str,
        "data": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ComponentVersionTypeDef = TypedDict(
    "ComponentVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "type": ComponentTypeType,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)

_RequiredContainerDistributionConfigurationTypeDef = TypedDict(
    "_RequiredContainerDistributionConfigurationTypeDef",
    {
        "targetRepository": "TargetContainerRepositoryTypeDef",
    },
)
_OptionalContainerDistributionConfigurationTypeDef = TypedDict(
    "_OptionalContainerDistributionConfigurationTypeDef",
    {
        "description": str,
        "containerTags": List[str],
    },
    total=False,
)

class ContainerDistributionConfigurationTypeDef(
    _RequiredContainerDistributionConfigurationTypeDef,
    _OptionalContainerDistributionConfigurationTypeDef,
):
    pass

ContainerRecipeSummaryTypeDef = TypedDict(
    "ContainerRecipeSummaryTypeDef",
    {
        "arn": str,
        "containerType": Literal["DOCKER"],
        "name": str,
        "platform": PlatformType,
        "owner": str,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ContainerRecipeTypeDef = TypedDict(
    "ContainerRecipeTypeDef",
    {
        "arn": str,
        "containerType": Literal["DOCKER"],
        "name": str,
        "description": str,
        "platform": PlatformType,
        "owner": str,
        "version": str,
        "components": List["ComponentConfigurationTypeDef"],
        "instanceConfiguration": "InstanceConfigurationTypeDef",
        "dockerfileTemplateData": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
        "targetRepository": "TargetContainerRepositoryTypeDef",
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "region": str,
        "imageUris": List[str],
    },
    total=False,
)

_RequiredCreateComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateComponentRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "clientToken": str,
    },
)
_OptionalCreateComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateComponentRequestRequestTypeDef",
    {
        "description": str,
        "changeDescription": str,
        "supportedOsVersions": List[str],
        "data": str,
        "uri": str,
        "kmsKeyId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateComponentRequestRequestTypeDef(
    _RequiredCreateComponentRequestRequestTypeDef, _OptionalCreateComponentRequestRequestTypeDef
):
    pass

CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContainerRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContainerRecipeRequestRequestTypeDef",
    {
        "containerType": Literal["DOCKER"],
        "name": str,
        "semanticVersion": str,
        "components": List["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "targetRepository": "TargetContainerRepositoryTypeDef",
        "clientToken": str,
    },
)
_OptionalCreateContainerRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContainerRecipeRequestRequestTypeDef",
    {
        "description": str,
        "instanceConfiguration": "InstanceConfigurationTypeDef",
        "dockerfileTemplateData": str,
        "dockerfileTemplateUri": str,
        "platformOverride": PlatformType,
        "imageOsVersionOverride": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
        "kmsKeyId": str,
    },
    total=False,
)

class CreateContainerRecipeRequestRequestTypeDef(
    _RequiredCreateContainerRecipeRequestRequestTypeDef,
    _OptionalCreateContainerRecipeRequestRequestTypeDef,
):
    pass

CreateContainerRecipeResponseTypeDef = TypedDict(
    "CreateContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDistributionConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "distributions": List["DistributionTypeDef"],
        "clientToken": str,
    },
)
_OptionalCreateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDistributionConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateDistributionConfigurationRequestRequestTypeDef(
    _RequiredCreateDistributionConfigurationRequestRequestTypeDef,
    _OptionalCreateDistributionConfigurationRequestRequestTypeDef,
):
    pass

CreateDistributionConfigurationResponseTypeDef = TypedDict(
    "CreateDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImagePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImagePipelineRequestRequestTypeDef",
    {
        "name": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalCreateImagePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImagePipelineRequestRequestTypeDef",
    {
        "description": str,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "enhancedImageMetadataEnabled": bool,
        "schedule": "ScheduleTypeDef",
        "status": PipelineStatusType,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateImagePipelineRequestRequestTypeDef(
    _RequiredCreateImagePipelineRequestRequestTypeDef,
    _OptionalCreateImagePipelineRequestRequestTypeDef,
):
    pass

CreateImagePipelineResponseTypeDef = TypedDict(
    "CreateImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageRecipeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageRecipeRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "components": List["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "clientToken": str,
    },
)
_OptionalCreateImageRecipeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageRecipeRequestRequestTypeDef",
    {
        "description": str,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "tags": Dict[str, str],
        "workingDirectory": str,
        "additionalInstanceConfiguration": "AdditionalInstanceConfigurationTypeDef",
    },
    total=False,
)

class CreateImageRecipeRequestRequestTypeDef(
    _RequiredCreateImageRecipeRequestRequestTypeDef, _OptionalCreateImageRecipeRequestRequestTypeDef
):
    pass

CreateImageRecipeResponseTypeDef = TypedDict(
    "CreateImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalCreateImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "enhancedImageMetadataEnabled": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateImageRequestRequestTypeDef(
    _RequiredCreateImageRequestRequestTypeDef, _OptionalCreateImageRequestRequestTypeDef
):
    pass

CreateImageResponseTypeDef = TypedDict(
    "CreateImageResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "instanceProfileName": str,
        "clientToken": str,
    },
)
_OptionalCreateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "instanceTypes": List[str],
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": "LoggingTypeDef",
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "resourceTags": Dict[str, str],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateInfrastructureConfigurationRequestRequestTypeDef(
    _RequiredCreateInfrastructureConfigurationRequestRequestTypeDef,
    _OptionalCreateInfrastructureConfigurationRequestRequestTypeDef,
):
    pass

CreateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "CreateInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)

DeleteComponentResponseTypeDef = TypedDict(
    "DeleteComponentResponseTypeDef",
    {
        "requestId": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerRecipeRequestRequestTypeDef = TypedDict(
    "DeleteContainerRecipeRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

DeleteContainerRecipeResponseTypeDef = TypedDict(
    "DeleteContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)

DeleteDistributionConfigurationResponseTypeDef = TypedDict(
    "DeleteDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImagePipelineRequestRequestTypeDef = TypedDict(
    "DeleteImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)

DeleteImagePipelineResponseTypeDef = TypedDict(
    "DeleteImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageRecipeRequestRequestTypeDef = TypedDict(
    "DeleteImageRecipeRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

DeleteImageRecipeResponseTypeDef = TypedDict(
    "DeleteImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteImageRequestRequestTypeDef = TypedDict(
    "DeleteImageRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)

DeleteImageResponseTypeDef = TypedDict(
    "DeleteImageResponseTypeDef",
    {
        "requestId": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)

DeleteInfrastructureConfigurationResponseTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DistributionConfigurationSummaryTypeDef = TypedDict(
    "DistributionConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
        "regions": List[str],
    },
    total=False,
)

_RequiredDistributionConfigurationTypeDef = TypedDict(
    "_RequiredDistributionConfigurationTypeDef",
    {
        "timeoutMinutes": int,
    },
)
_OptionalDistributionConfigurationTypeDef = TypedDict(
    "_OptionalDistributionConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "distributions": List["DistributionTypeDef"],
        "dateCreated": str,
        "dateUpdated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class DistributionConfigurationTypeDef(
    _RequiredDistributionConfigurationTypeDef, _OptionalDistributionConfigurationTypeDef
):
    pass

_RequiredDistributionTypeDef = TypedDict(
    "_RequiredDistributionTypeDef",
    {
        "region": str,
    },
)
_OptionalDistributionTypeDef = TypedDict(
    "_OptionalDistributionTypeDef",
    {
        "amiDistributionConfiguration": "AmiDistributionConfigurationTypeDef",
        "containerDistributionConfiguration": "ContainerDistributionConfigurationTypeDef",
        "licenseConfigurationArns": List[str],
        "launchTemplateConfigurations": List["LaunchTemplateConfigurationTypeDef"],
    },
    total=False,
)

class DistributionTypeDef(_RequiredDistributionTypeDef, _OptionalDistributionTypeDef):
    pass

EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "encrypted": bool,
        "deleteOnTermination": bool,
        "iops": int,
        "kmsKeyId": str,
        "snapshotId": str,
        "volumeSize": int,
        "volumeType": EbsVolumeTypeType,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

GetComponentPolicyRequestRequestTypeDef = TypedDict(
    "GetComponentPolicyRequestRequestTypeDef",
    {
        "componentArn": str,
    },
)

GetComponentPolicyResponseTypeDef = TypedDict(
    "GetComponentPolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentRequestRequestTypeDef = TypedDict(
    "GetComponentRequestRequestTypeDef",
    {
        "componentBuildVersionArn": str,
    },
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "requestId": str,
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerRecipePolicyRequestRequestTypeDef = TypedDict(
    "GetContainerRecipePolicyRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

GetContainerRecipePolicyResponseTypeDef = TypedDict(
    "GetContainerRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerRecipeRequestRequestTypeDef = TypedDict(
    "GetContainerRecipeRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
    },
)

GetContainerRecipeResponseTypeDef = TypedDict(
    "GetContainerRecipeResponseTypeDef",
    {
        "requestId": str,
        "containerRecipe": "ContainerRecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "GetDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
    },
)

GetDistributionConfigurationResponseTypeDef = TypedDict(
    "GetDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "distributionConfiguration": "DistributionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImagePipelineRequestRequestTypeDef = TypedDict(
    "GetImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)

GetImagePipelineResponseTypeDef = TypedDict(
    "GetImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "imagePipeline": "ImagePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImagePolicyRequestRequestTypeDef = TypedDict(
    "GetImagePolicyRequestRequestTypeDef",
    {
        "imageArn": str,
    },
)

GetImagePolicyResponseTypeDef = TypedDict(
    "GetImagePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRecipePolicyRequestRequestTypeDef = TypedDict(
    "GetImageRecipePolicyRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

GetImageRecipePolicyResponseTypeDef = TypedDict(
    "GetImageRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRecipeRequestRequestTypeDef = TypedDict(
    "GetImageRecipeRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
    },
)

GetImageRecipeResponseTypeDef = TypedDict(
    "GetImageRecipeResponseTypeDef",
    {
        "requestId": str,
        "imageRecipe": "ImageRecipeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageRequestRequestTypeDef = TypedDict(
    "GetImageRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)

GetImageResponseTypeDef = TypedDict(
    "GetImageResponseTypeDef",
    {
        "requestId": str,
        "image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "GetInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
    },
)

GetInfrastructureConfigurationResponseTypeDef = TypedDict(
    "GetInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfiguration": "InfrastructureConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImagePackageTypeDef = TypedDict(
    "ImagePackageTypeDef",
    {
        "packageName": str,
        "packageVersion": str,
    },
    total=False,
)

ImagePipelineTypeDef = TypedDict(
    "ImagePipelineTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "platform": PlatformType,
        "enhancedImageMetadataEnabled": bool,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "infrastructureConfigurationArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "schedule": "ScheduleTypeDef",
        "status": PipelineStatusType,
        "dateCreated": str,
        "dateUpdated": str,
        "dateLastRun": str,
        "dateNextRun": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ImageRecipeSummaryTypeDef = TypedDict(
    "ImageRecipeSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "platform": PlatformType,
        "owner": str,
        "parentImage": str,
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ImageRecipeTypeDef = TypedDict(
    "ImageRecipeTypeDef",
    {
        "arn": str,
        "type": ImageTypeType,
        "name": str,
        "description": str,
        "platform": PlatformType,
        "owner": str,
        "version": str,
        "components": List["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "dateCreated": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
        "additionalInstanceConfiguration": "AdditionalInstanceConfigurationTypeDef",
    },
    total=False,
)

ImageStateTypeDef = TypedDict(
    "ImageStateTypeDef",
    {
        "status": ImageStatusType,
        "reason": str,
    },
    total=False,
)

ImageSummaryTypeDef = TypedDict(
    "ImageSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ImageTypeType,
        "version": str,
        "platform": PlatformType,
        "osVersion": str,
        "state": "ImageStateTypeDef",
        "owner": str,
        "dateCreated": str,
        "outputResources": "OutputResourcesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

ImageTestsConfigurationTypeDef = TypedDict(
    "ImageTestsConfigurationTypeDef",
    {
        "imageTestsEnabled": bool,
        "timeoutMinutes": int,
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "arn": str,
        "type": ImageTypeType,
        "name": str,
        "version": str,
        "platform": PlatformType,
        "enhancedImageMetadataEnabled": bool,
        "osVersion": str,
        "state": "ImageStateTypeDef",
        "imageRecipe": "ImageRecipeTypeDef",
        "containerRecipe": "ContainerRecipeTypeDef",
        "sourcePipelineName": str,
        "sourcePipelineArn": str,
        "infrastructureConfiguration": "InfrastructureConfigurationTypeDef",
        "distributionConfiguration": "DistributionConfigurationTypeDef",
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "dateCreated": str,
        "outputResources": "OutputResourcesTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

ImageVersionTypeDef = TypedDict(
    "ImageVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ImageTypeType,
        "version": str,
        "platform": PlatformType,
        "osVersion": str,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)

_RequiredImportComponentRequestRequestTypeDef = TypedDict(
    "_RequiredImportComponentRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "type": ComponentTypeType,
        "format": Literal["SHELL"],
        "platform": PlatformType,
        "clientToken": str,
    },
)
_OptionalImportComponentRequestRequestTypeDef = TypedDict(
    "_OptionalImportComponentRequestRequestTypeDef",
    {
        "description": str,
        "changeDescription": str,
        "data": str,
        "uri": str,
        "kmsKeyId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ImportComponentRequestRequestTypeDef(
    _RequiredImportComponentRequestRequestTypeDef, _OptionalImportComponentRequestRequestTypeDef
):
    pass

ImportComponentResponseTypeDef = TypedDict(
    "ImportComponentResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "componentBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InfrastructureConfigurationSummaryTypeDef = TypedDict(
    "InfrastructureConfigurationSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "dateCreated": str,
        "dateUpdated": str,
        "resourceTags": Dict[str, str],
        "tags": Dict[str, str],
        "instanceTypes": List[str],
        "instanceProfileName": str,
    },
    total=False,
)

InfrastructureConfigurationTypeDef = TypedDict(
    "InfrastructureConfigurationTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "instanceTypes": List[str],
        "instanceProfileName": str,
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": "LoggingTypeDef",
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "dateCreated": str,
        "dateUpdated": str,
        "resourceTags": Dict[str, str],
        "tags": Dict[str, str],
    },
    total=False,
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "deviceName": str,
        "ebs": "EbsInstanceBlockDeviceSpecificationTypeDef",
        "virtualName": str,
        "noDevice": str,
    },
    total=False,
)

InstanceConfigurationTypeDef = TypedDict(
    "InstanceConfigurationTypeDef",
    {
        "image": str,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
    },
    total=False,
)

LaunchPermissionConfigurationTypeDef = TypedDict(
    "LaunchPermissionConfigurationTypeDef",
    {
        "userIds": List[str],
        "userGroups": List[str],
    },
    total=False,
)

_RequiredLaunchTemplateConfigurationTypeDef = TypedDict(
    "_RequiredLaunchTemplateConfigurationTypeDef",
    {
        "launchTemplateId": str,
    },
)
_OptionalLaunchTemplateConfigurationTypeDef = TypedDict(
    "_OptionalLaunchTemplateConfigurationTypeDef",
    {
        "accountId": str,
        "setDefaultVersion": bool,
    },
    total=False,
)

class LaunchTemplateConfigurationTypeDef(
    _RequiredLaunchTemplateConfigurationTypeDef, _OptionalLaunchTemplateConfigurationTypeDef
):
    pass

_RequiredListComponentBuildVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentBuildVersionsRequestRequestTypeDef",
    {
        "componentVersionArn": str,
    },
)
_OptionalListComponentBuildVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentBuildVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListComponentBuildVersionsRequestRequestTypeDef(
    _RequiredListComponentBuildVersionsRequestRequestTypeDef,
    _OptionalListComponentBuildVersionsRequestRequestTypeDef,
):
    pass

ListComponentBuildVersionsResponseTypeDef = TypedDict(
    "ListComponentBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "componentSummaryList": List["ComponentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "byName": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "requestId": str,
        "componentVersionList": List["ComponentVersionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContainerRecipesRequestRequestTypeDef = TypedDict(
    "ListContainerRecipesRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListContainerRecipesResponseTypeDef = TypedDict(
    "ListContainerRecipesResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeSummaryList": List["ContainerRecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDistributionConfigurationsRequestRequestTypeDef = TypedDict(
    "ListDistributionConfigurationsRequestRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDistributionConfigurationsResponseTypeDef = TypedDict(
    "ListDistributionConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "distributionConfigurationSummaryList": List["DistributionConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImageBuildVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListImageBuildVersionsRequestRequestTypeDef",
    {
        "imageVersionArn": str,
    },
)
_OptionalListImageBuildVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListImageBuildVersionsRequestRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListImageBuildVersionsRequestRequestTypeDef(
    _RequiredListImageBuildVersionsRequestRequestTypeDef,
    _OptionalListImageBuildVersionsRequestRequestTypeDef,
):
    pass

ListImageBuildVersionsResponseTypeDef = TypedDict(
    "ListImageBuildVersionsResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List["ImageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImagePackagesRequestRequestTypeDef = TypedDict(
    "_RequiredListImagePackagesRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)
_OptionalListImagePackagesRequestRequestTypeDef = TypedDict(
    "_OptionalListImagePackagesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListImagePackagesRequestRequestTypeDef(
    _RequiredListImagePackagesRequestRequestTypeDef, _OptionalListImagePackagesRequestRequestTypeDef
):
    pass

ListImagePackagesResponseTypeDef = TypedDict(
    "ListImagePackagesResponseTypeDef",
    {
        "requestId": str,
        "imagePackageList": List["ImagePackageTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListImagePipelineImagesRequestRequestTypeDef = TypedDict(
    "_RequiredListImagePipelineImagesRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
    },
)
_OptionalListImagePipelineImagesRequestRequestTypeDef = TypedDict(
    "_OptionalListImagePipelineImagesRequestRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListImagePipelineImagesRequestRequestTypeDef(
    _RequiredListImagePipelineImagesRequestRequestTypeDef,
    _OptionalListImagePipelineImagesRequestRequestTypeDef,
):
    pass

ListImagePipelineImagesResponseTypeDef = TypedDict(
    "ListImagePipelineImagesResponseTypeDef",
    {
        "requestId": str,
        "imageSummaryList": List["ImageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagePipelinesRequestRequestTypeDef = TypedDict(
    "ListImagePipelinesRequestRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImagePipelinesResponseTypeDef = TypedDict(
    "ListImagePipelinesResponseTypeDef",
    {
        "requestId": str,
        "imagePipelineList": List["ImagePipelineTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageRecipesRequestRequestTypeDef = TypedDict(
    "ListImageRecipesRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImageRecipesResponseTypeDef = TypedDict(
    "ListImageRecipesResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeSummaryList": List["ImageRecipeSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImagesRequestRequestTypeDef = TypedDict(
    "ListImagesRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "byName": bool,
        "maxResults": int,
        "nextToken": str,
        "includeDeprecated": bool,
    },
    total=False,
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {
        "requestId": str,
        "imageVersionList": List["ImageVersionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInfrastructureConfigurationsRequestRequestTypeDef = TypedDict(
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListInfrastructureConfigurationsResponseTypeDef = TypedDict(
    "ListInfrastructureConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationSummaryList": List["InfrastructureConfigurationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "s3Logs": "S3LogsTypeDef",
    },
    total=False,
)

OutputResourcesTypeDef = TypedDict(
    "OutputResourcesTypeDef",
    {
        "amis": List["AmiTypeDef"],
        "containers": List["ContainerTypeDef"],
    },
    total=False,
)

PutComponentPolicyRequestRequestTypeDef = TypedDict(
    "PutComponentPolicyRequestRequestTypeDef",
    {
        "componentArn": str,
        "policy": str,
    },
)

PutComponentPolicyResponseTypeDef = TypedDict(
    "PutComponentPolicyResponseTypeDef",
    {
        "requestId": str,
        "componentArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutContainerRecipePolicyRequestRequestTypeDef = TypedDict(
    "PutContainerRecipePolicyRequestRequestTypeDef",
    {
        "containerRecipeArn": str,
        "policy": str,
    },
)

PutContainerRecipePolicyResponseTypeDef = TypedDict(
    "PutContainerRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImagePolicyRequestRequestTypeDef = TypedDict(
    "PutImagePolicyRequestRequestTypeDef",
    {
        "imageArn": str,
        "policy": str,
    },
)

PutImagePolicyResponseTypeDef = TypedDict(
    "PutImagePolicyResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutImageRecipePolicyRequestRequestTypeDef = TypedDict(
    "PutImageRecipePolicyRequestRequestTypeDef",
    {
        "imageRecipeArn": str,
        "policy": str,
    },
)

PutImageRecipePolicyResponseTypeDef = TypedDict(
    "PutImageRecipePolicyResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

S3LogsTypeDef = TypedDict(
    "S3LogsTypeDef",
    {
        "s3BucketName": str,
        "s3KeyPrefix": str,
    },
    total=False,
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "scheduleExpression": str,
        "timezone": str,
        "pipelineExecutionStartCondition": PipelineExecutionStartConditionType,
    },
    total=False,
)

StartImagePipelineExecutionRequestRequestTypeDef = TypedDict(
    "StartImagePipelineExecutionRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "clientToken": str,
    },
)

StartImagePipelineExecutionResponseTypeDef = TypedDict(
    "StartImagePipelineExecutionResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imageBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SystemsManagerAgentTypeDef = TypedDict(
    "SystemsManagerAgentTypeDef",
    {
        "uninstallAfterBuild": bool,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TargetContainerRepositoryTypeDef = TypedDict(
    "TargetContainerRepositoryTypeDef",
    {
        "service": Literal["ECR"],
        "repositoryName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDistributionConfigurationRequestRequestTypeDef",
    {
        "distributionConfigurationArn": str,
        "distributions": List["DistributionTypeDef"],
        "clientToken": str,
    },
)
_OptionalUpdateDistributionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDistributionConfigurationRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateDistributionConfigurationRequestRequestTypeDef(
    _RequiredUpdateDistributionConfigurationRequestRequestTypeDef,
    _OptionalUpdateDistributionConfigurationRequestRequestTypeDef,
):
    pass

UpdateDistributionConfigurationResponseTypeDef = TypedDict(
    "UpdateDistributionConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "distributionConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateImagePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateImagePipelineRequestRequestTypeDef",
    {
        "imagePipelineArn": str,
        "infrastructureConfigurationArn": str,
        "clientToken": str,
    },
)
_OptionalUpdateImagePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateImagePipelineRequestRequestTypeDef",
    {
        "description": str,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "enhancedImageMetadataEnabled": bool,
        "schedule": "ScheduleTypeDef",
        "status": PipelineStatusType,
    },
    total=False,
)

class UpdateImagePipelineRequestRequestTypeDef(
    _RequiredUpdateImagePipelineRequestRequestTypeDef,
    _OptionalUpdateImagePipelineRequestRequestTypeDef,
):
    pass

UpdateImagePipelineResponseTypeDef = TypedDict(
    "UpdateImagePipelineResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "imagePipelineArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "infrastructureConfigurationArn": str,
        "instanceProfileName": str,
        "clientToken": str,
    },
)
_OptionalUpdateInfrastructureConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInfrastructureConfigurationRequestRequestTypeDef",
    {
        "description": str,
        "instanceTypes": List[str],
        "securityGroupIds": List[str],
        "subnetId": str,
        "logging": "LoggingTypeDef",
        "keyPair": str,
        "terminateInstanceOnFailure": bool,
        "snsTopicArn": str,
        "resourceTags": Dict[str, str],
    },
    total=False,
)

class UpdateInfrastructureConfigurationRequestRequestTypeDef(
    _RequiredUpdateInfrastructureConfigurationRequestRequestTypeDef,
    _OptionalUpdateInfrastructureConfigurationRequestRequestTypeDef,
):
    pass

UpdateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "UpdateInfrastructureConfigurationResponseTypeDef",
    {
        "requestId": str,
        "clientToken": str,
        "infrastructureConfigurationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
