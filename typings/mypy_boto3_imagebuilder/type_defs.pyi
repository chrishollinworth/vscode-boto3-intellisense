"""
Main interface for imagebuilder service type definitions.

Usage::

    ```python
    from mypy_boto3_imagebuilder.type_defs import AmiDistributionConfigurationTypeDef

    data: AmiDistributionConfigurationTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AmiDistributionConfigurationTypeDef",
    "AmiTypeDef",
    "ComponentConfigurationTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "ComponentVersionTypeDef",
    "ContainerDistributionConfigurationTypeDef",
    "ContainerRecipeSummaryTypeDef",
    "ContainerRecipeTypeDef",
    "ContainerTypeDef",
    "DistributionConfigurationSummaryTypeDef",
    "DistributionConfigurationTypeDef",
    "DistributionTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "ImagePipelineTypeDef",
    "ImageRecipeSummaryTypeDef",
    "ImageRecipeTypeDef",
    "ImageStateTypeDef",
    "ImageSummaryTypeDef",
    "ImageTestsConfigurationTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "InfrastructureConfigurationSummaryTypeDef",
    "InfrastructureConfigurationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "LaunchPermissionConfigurationTypeDef",
    "LoggingTypeDef",
    "OutputResourcesTypeDef",
    "S3LogsTypeDef",
    "ScheduleTypeDef",
    "TargetContainerRepositoryTypeDef",
    "CancelImageCreationResponseTypeDef",
    "CreateComponentResponseTypeDef",
    "CreateContainerRecipeResponseTypeDef",
    "CreateDistributionConfigurationResponseTypeDef",
    "CreateImagePipelineResponseTypeDef",
    "CreateImageRecipeResponseTypeDef",
    "CreateImageResponseTypeDef",
    "CreateInfrastructureConfigurationResponseTypeDef",
    "DeleteComponentResponseTypeDef",
    "DeleteContainerRecipeResponseTypeDef",
    "DeleteDistributionConfigurationResponseTypeDef",
    "DeleteImagePipelineResponseTypeDef",
    "DeleteImageRecipeResponseTypeDef",
    "DeleteImageResponseTypeDef",
    "DeleteInfrastructureConfigurationResponseTypeDef",
    "FilterTypeDef",
    "GetComponentPolicyResponseTypeDef",
    "GetComponentResponseTypeDef",
    "GetContainerRecipePolicyResponseTypeDef",
    "GetContainerRecipeResponseTypeDef",
    "GetDistributionConfigurationResponseTypeDef",
    "GetImagePipelineResponseTypeDef",
    "GetImagePolicyResponseTypeDef",
    "GetImageRecipePolicyResponseTypeDef",
    "GetImageRecipeResponseTypeDef",
    "GetImageResponseTypeDef",
    "GetInfrastructureConfigurationResponseTypeDef",
    "ImportComponentResponseTypeDef",
    "ListComponentBuildVersionsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "ListContainerRecipesResponseTypeDef",
    "ListDistributionConfigurationsResponseTypeDef",
    "ListImageBuildVersionsResponseTypeDef",
    "ListImagePipelineImagesResponseTypeDef",
    "ListImagePipelinesResponseTypeDef",
    "ListImageRecipesResponseTypeDef",
    "ListImagesResponseTypeDef",
    "ListInfrastructureConfigurationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutComponentPolicyResponseTypeDef",
    "PutContainerRecipePolicyResponseTypeDef",
    "PutImagePolicyResponseTypeDef",
    "PutImageRecipePolicyResponseTypeDef",
    "StartImagePipelineExecutionResponseTypeDef",
    "UpdateDistributionConfigurationResponseTypeDef",
    "UpdateImagePipelineResponseTypeDef",
    "UpdateInfrastructureConfigurationResponseTypeDef",
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

ComponentConfigurationTypeDef = TypedDict("ComponentConfigurationTypeDef", {"componentArn": str})

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": Literal["Windows", "Linux"],
        "supportedOsVersions": List[str],
        "type": Literal["BUILD", "TEST"],
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
        "type": Literal["BUILD", "TEST"],
        "platform": Literal["Windows", "Linux"],
        "supportedOsVersions": List[str],
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
        "platform": Literal["Windows", "Linux"],
        "supportedOsVersions": List[str],
        "type": Literal["BUILD", "TEST"],
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)

_RequiredContainerDistributionConfigurationTypeDef = TypedDict(
    "_RequiredContainerDistributionConfigurationTypeDef",
    {"targetRepository": "TargetContainerRepositoryTypeDef"},
)
_OptionalContainerDistributionConfigurationTypeDef = TypedDict(
    "_OptionalContainerDistributionConfigurationTypeDef",
    {"description": str, "containerTags": List[str]},
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
        "platform": Literal["Windows", "Linux"],
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
        "platform": Literal["Windows", "Linux"],
        "owner": str,
        "version": str,
        "components": List["ComponentConfigurationTypeDef"],
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
    "ContainerTypeDef", {"region": str, "imageUris": List[str]}, total=False
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
    "_RequiredDistributionConfigurationTypeDef", {"timeoutMinutes": int}
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


_RequiredDistributionTypeDef = TypedDict("_RequiredDistributionTypeDef", {"region": str})
_OptionalDistributionTypeDef = TypedDict(
    "_OptionalDistributionTypeDef",
    {
        "amiDistributionConfiguration": "AmiDistributionConfigurationTypeDef",
        "containerDistributionConfiguration": "ContainerDistributionConfigurationTypeDef",
        "licenseConfigurationArns": List[str],
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
        "volumeType": Literal["standard", "io1", "io2", "gp2", "sc1", "st1"],
    },
    total=False,
)

ImagePipelineTypeDef = TypedDict(
    "ImagePipelineTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "platform": Literal["Windows", "Linux"],
        "enhancedImageMetadataEnabled": bool,
        "imageRecipeArn": str,
        "containerRecipeArn": str,
        "infrastructureConfigurationArn": str,
        "distributionConfigurationArn": str,
        "imageTestsConfiguration": "ImageTestsConfigurationTypeDef",
        "schedule": "ScheduleTypeDef",
        "status": Literal["DISABLED", "ENABLED"],
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
        "platform": Literal["Windows", "Linux"],
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
        "type": Literal["AMI", "DOCKER"],
        "name": str,
        "description": str,
        "platform": Literal["Windows", "Linux"],
        "owner": str,
        "version": str,
        "components": List["ComponentConfigurationTypeDef"],
        "parentImage": str,
        "blockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "dateCreated": str,
        "tags": Dict[str, str],
        "workingDirectory": str,
    },
    total=False,
)

ImageStateTypeDef = TypedDict(
    "ImageStateTypeDef",
    {
        "status": Literal[
            "PENDING",
            "CREATING",
            "BUILDING",
            "TESTING",
            "DISTRIBUTING",
            "INTEGRATING",
            "AVAILABLE",
            "CANCELLED",
            "FAILED",
            "DEPRECATED",
            "DELETED",
        ],
        "reason": str,
    },
    total=False,
)

ImageSummaryTypeDef = TypedDict(
    "ImageSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "type": Literal["AMI", "DOCKER"],
        "version": str,
        "platform": Literal["Windows", "Linux"],
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
    {"imageTestsEnabled": bool, "timeoutMinutes": int},
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "arn": str,
        "type": Literal["AMI", "DOCKER"],
        "name": str,
        "version": str,
        "platform": Literal["Windows", "Linux"],
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
        "type": Literal["AMI", "DOCKER"],
        "version": str,
        "platform": Literal["Windows", "Linux"],
        "osVersion": str,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
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

LaunchPermissionConfigurationTypeDef = TypedDict(
    "LaunchPermissionConfigurationTypeDef",
    {"userIds": List[str], "userGroups": List[str]},
    total=False,
)

LoggingTypeDef = TypedDict("LoggingTypeDef", {"s3Logs": "S3LogsTypeDef"}, total=False)

OutputResourcesTypeDef = TypedDict(
    "OutputResourcesTypeDef",
    {"amis": List["AmiTypeDef"], "containers": List["ContainerTypeDef"]},
    total=False,
)

S3LogsTypeDef = TypedDict("S3LogsTypeDef", {"s3BucketName": str, "s3KeyPrefix": str}, total=False)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "scheduleExpression": str,
        "pipelineExecutionStartCondition": Literal[
            "EXPRESSION_MATCH_ONLY", "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
        ],
    },
    total=False,
)

TargetContainerRepositoryTypeDef = TypedDict(
    "TargetContainerRepositoryTypeDef", {"service": Literal["ECR"], "repositoryName": str}
)

CancelImageCreationResponseTypeDef = TypedDict(
    "CancelImageCreationResponseTypeDef",
    {"requestId": str, "clientToken": str, "imageBuildVersionArn": str},
    total=False,
)

CreateComponentResponseTypeDef = TypedDict(
    "CreateComponentResponseTypeDef",
    {"requestId": str, "clientToken": str, "componentBuildVersionArn": str},
    total=False,
)

CreateContainerRecipeResponseTypeDef = TypedDict(
    "CreateContainerRecipeResponseTypeDef",
    {"requestId": str, "clientToken": str, "containerRecipeArn": str},
    total=False,
)

CreateDistributionConfigurationResponseTypeDef = TypedDict(
    "CreateDistributionConfigurationResponseTypeDef",
    {"requestId": str, "clientToken": str, "distributionConfigurationArn": str},
    total=False,
)

CreateImagePipelineResponseTypeDef = TypedDict(
    "CreateImagePipelineResponseTypeDef",
    {"requestId": str, "clientToken": str, "imagePipelineArn": str},
    total=False,
)

CreateImageRecipeResponseTypeDef = TypedDict(
    "CreateImageRecipeResponseTypeDef",
    {"requestId": str, "clientToken": str, "imageRecipeArn": str},
    total=False,
)

CreateImageResponseTypeDef = TypedDict(
    "CreateImageResponseTypeDef",
    {"requestId": str, "clientToken": str, "imageBuildVersionArn": str},
    total=False,
)

CreateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "CreateInfrastructureConfigurationResponseTypeDef",
    {"requestId": str, "clientToken": str, "infrastructureConfigurationArn": str},
    total=False,
)

DeleteComponentResponseTypeDef = TypedDict(
    "DeleteComponentResponseTypeDef",
    {"requestId": str, "componentBuildVersionArn": str},
    total=False,
)

DeleteContainerRecipeResponseTypeDef = TypedDict(
    "DeleteContainerRecipeResponseTypeDef",
    {"requestId": str, "containerRecipeArn": str},
    total=False,
)

DeleteDistributionConfigurationResponseTypeDef = TypedDict(
    "DeleteDistributionConfigurationResponseTypeDef",
    {"requestId": str, "distributionConfigurationArn": str},
    total=False,
)

DeleteImagePipelineResponseTypeDef = TypedDict(
    "DeleteImagePipelineResponseTypeDef", {"requestId": str, "imagePipelineArn": str}, total=False
)

DeleteImageRecipeResponseTypeDef = TypedDict(
    "DeleteImageRecipeResponseTypeDef", {"requestId": str, "imageRecipeArn": str}, total=False
)

DeleteImageResponseTypeDef = TypedDict(
    "DeleteImageResponseTypeDef", {"requestId": str, "imageBuildVersionArn": str}, total=False
)

DeleteInfrastructureConfigurationResponseTypeDef = TypedDict(
    "DeleteInfrastructureConfigurationResponseTypeDef",
    {"requestId": str, "infrastructureConfigurationArn": str},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"name": str, "values": List[str]}, total=False)

GetComponentPolicyResponseTypeDef = TypedDict(
    "GetComponentPolicyResponseTypeDef", {"requestId": str, "policy": str}, total=False
)

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef", {"requestId": str, "component": "ComponentTypeDef"}, total=False
)

GetContainerRecipePolicyResponseTypeDef = TypedDict(
    "GetContainerRecipePolicyResponseTypeDef", {"requestId": str, "policy": str}, total=False
)

GetContainerRecipeResponseTypeDef = TypedDict(
    "GetContainerRecipeResponseTypeDef",
    {"requestId": str, "containerRecipe": "ContainerRecipeTypeDef"},
    total=False,
)

GetDistributionConfigurationResponseTypeDef = TypedDict(
    "GetDistributionConfigurationResponseTypeDef",
    {"requestId": str, "distributionConfiguration": "DistributionConfigurationTypeDef"},
    total=False,
)

GetImagePipelineResponseTypeDef = TypedDict(
    "GetImagePipelineResponseTypeDef",
    {"requestId": str, "imagePipeline": "ImagePipelineTypeDef"},
    total=False,
)

GetImagePolicyResponseTypeDef = TypedDict(
    "GetImagePolicyResponseTypeDef", {"requestId": str, "policy": str}, total=False
)

GetImageRecipePolicyResponseTypeDef = TypedDict(
    "GetImageRecipePolicyResponseTypeDef", {"requestId": str, "policy": str}, total=False
)

GetImageRecipeResponseTypeDef = TypedDict(
    "GetImageRecipeResponseTypeDef",
    {"requestId": str, "imageRecipe": "ImageRecipeTypeDef"},
    total=False,
)

GetImageResponseTypeDef = TypedDict(
    "GetImageResponseTypeDef", {"requestId": str, "image": "ImageTypeDef"}, total=False
)

GetInfrastructureConfigurationResponseTypeDef = TypedDict(
    "GetInfrastructureConfigurationResponseTypeDef",
    {"requestId": str, "infrastructureConfiguration": "InfrastructureConfigurationTypeDef"},
    total=False,
)

ImportComponentResponseTypeDef = TypedDict(
    "ImportComponentResponseTypeDef",
    {"requestId": str, "clientToken": str, "componentBuildVersionArn": str},
    total=False,
)

ListComponentBuildVersionsResponseTypeDef = TypedDict(
    "ListComponentBuildVersionsResponseTypeDef",
    {"requestId": str, "componentSummaryList": List["ComponentSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {"requestId": str, "componentVersionList": List["ComponentVersionTypeDef"], "nextToken": str},
    total=False,
)

ListContainerRecipesResponseTypeDef = TypedDict(
    "ListContainerRecipesResponseTypeDef",
    {
        "requestId": str,
        "containerRecipeSummaryList": List["ContainerRecipeSummaryTypeDef"],
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
    },
    total=False,
)

ListImageBuildVersionsResponseTypeDef = TypedDict(
    "ListImageBuildVersionsResponseTypeDef",
    {"requestId": str, "imageSummaryList": List["ImageSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListImagePipelineImagesResponseTypeDef = TypedDict(
    "ListImagePipelineImagesResponseTypeDef",
    {"requestId": str, "imageSummaryList": List["ImageSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListImagePipelinesResponseTypeDef = TypedDict(
    "ListImagePipelinesResponseTypeDef",
    {"requestId": str, "imagePipelineList": List["ImagePipelineTypeDef"], "nextToken": str},
    total=False,
)

ListImageRecipesResponseTypeDef = TypedDict(
    "ListImageRecipesResponseTypeDef",
    {
        "requestId": str,
        "imageRecipeSummaryList": List["ImageRecipeSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListImagesResponseTypeDef = TypedDict(
    "ListImagesResponseTypeDef",
    {"requestId": str, "imageVersionList": List["ImageVersionTypeDef"], "nextToken": str},
    total=False,
)

ListInfrastructureConfigurationsResponseTypeDef = TypedDict(
    "ListInfrastructureConfigurationsResponseTypeDef",
    {
        "requestId": str,
        "infrastructureConfigurationSummaryList": List["InfrastructureConfigurationSummaryTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PutComponentPolicyResponseTypeDef = TypedDict(
    "PutComponentPolicyResponseTypeDef", {"requestId": str, "componentArn": str}, total=False
)

PutContainerRecipePolicyResponseTypeDef = TypedDict(
    "PutContainerRecipePolicyResponseTypeDef",
    {"requestId": str, "containerRecipeArn": str},
    total=False,
)

PutImagePolicyResponseTypeDef = TypedDict(
    "PutImagePolicyResponseTypeDef", {"requestId": str, "imageArn": str}, total=False
)

PutImageRecipePolicyResponseTypeDef = TypedDict(
    "PutImageRecipePolicyResponseTypeDef", {"requestId": str, "imageRecipeArn": str}, total=False
)

StartImagePipelineExecutionResponseTypeDef = TypedDict(
    "StartImagePipelineExecutionResponseTypeDef",
    {"requestId": str, "clientToken": str, "imageBuildVersionArn": str},
    total=False,
)

UpdateDistributionConfigurationResponseTypeDef = TypedDict(
    "UpdateDistributionConfigurationResponseTypeDef",
    {"requestId": str, "clientToken": str, "distributionConfigurationArn": str},
    total=False,
)

UpdateImagePipelineResponseTypeDef = TypedDict(
    "UpdateImagePipelineResponseTypeDef",
    {"requestId": str, "clientToken": str, "imagePipelineArn": str},
    total=False,
)

UpdateInfrastructureConfigurationResponseTypeDef = TypedDict(
    "UpdateInfrastructureConfigurationResponseTypeDef",
    {"requestId": str, "clientToken": str, "infrastructureConfigurationArn": str},
    total=False,
)
