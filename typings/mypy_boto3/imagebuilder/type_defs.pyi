"""
Type annotations for imagebuilder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_imagebuilder.type_defs import AccountAggregationTypeDef

    data: AccountAggregationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    BuildTypeType,
    ComponentTypeType,
    DiskImageFormatType,
    EbsVolumeTypeType,
    ImageScanStatusType,
    ImageSourceType,
    ImageStatusType,
    ImageTypeType,
    LifecycleExecutionResourceActionNameType,
    LifecycleExecutionResourceStatusType,
    LifecycleExecutionStatusType,
    LifecyclePolicyDetailActionTypeType,
    LifecyclePolicyDetailFilterTypeType,
    LifecyclePolicyResourceTypeType,
    LifecyclePolicyStatusType,
    LifecyclePolicyTimeUnitType,
    OnWorkflowFailureType,
    OwnershipType,
    PipelineExecutionStartConditionType,
    PipelineStatusType,
    PlatformType,
    ResourceStatusType,
    WorkflowExecutionStatusType,
    WorkflowStepActionTypeType,
    WorkflowStepExecutionRollbackStatusType,
    WorkflowStepExecutionStatusType,
    WorkflowTypeType,
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
    "AccountAggregationTypeDef",
    "AdditionalInstanceConfigurationTypeDef",
    "AmiDistributionConfigurationTypeDef",
    "AmiTypeDef",
    "CancelImageCreationRequestRequestTypeDef",
    "CancelImageCreationResponseTypeDef",
    "CancelLifecycleExecutionRequestRequestTypeDef",
    "CancelLifecycleExecutionResponseTypeDef",
    "ComponentConfigurationTypeDef",
    "ComponentParameterDetailTypeDef",
    "ComponentParameterTypeDef",
    "ComponentStateTypeDef",
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
    "CreateLifecyclePolicyRequestRequestTypeDef",
    "CreateLifecyclePolicyResponseTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CvssScoreAdjustmentTypeDef",
    "CvssScoreDetailsTypeDef",
    "CvssScoreTypeDef",
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
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    "DeleteLifecyclePolicyResponseTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "DistributionConfigurationSummaryTypeDef",
    "DistributionConfigurationTypeDef",
    "DistributionTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EcrConfigurationTypeDef",
    "FastLaunchConfigurationTypeDef",
    "FastLaunchLaunchTemplateSpecificationTypeDef",
    "FastLaunchSnapshotConfigurationTypeDef",
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
    "GetLifecycleExecutionRequestRequestTypeDef",
    "GetLifecycleExecutionResponseTypeDef",
    "GetLifecyclePolicyRequestRequestTypeDef",
    "GetLifecyclePolicyResponseTypeDef",
    "GetWorkflowExecutionRequestRequestTypeDef",
    "GetWorkflowExecutionResponseTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowStepExecutionRequestRequestTypeDef",
    "GetWorkflowStepExecutionResponseTypeDef",
    "ImageAggregationTypeDef",
    "ImagePackageTypeDef",
    "ImagePipelineAggregationTypeDef",
    "ImagePipelineTypeDef",
    "ImageRecipeSummaryTypeDef",
    "ImageRecipeTypeDef",
    "ImageScanFindingAggregationTypeDef",
    "ImageScanFindingTypeDef",
    "ImageScanFindingsFilterTypeDef",
    "ImageScanStateTypeDef",
    "ImageScanningConfigurationTypeDef",
    "ImageStateTypeDef",
    "ImageSummaryTypeDef",
    "ImageTestsConfigurationTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "ImportComponentRequestRequestTypeDef",
    "ImportComponentResponseTypeDef",
    "ImportVmImageRequestRequestTypeDef",
    "ImportVmImageResponseTypeDef",
    "InfrastructureConfigurationSummaryTypeDef",
    "InfrastructureConfigurationTypeDef",
    "InspectorScoreDetailsTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceConfigurationTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "LaunchPermissionConfigurationTypeDef",
    "LaunchTemplateConfigurationTypeDef",
    "LifecycleExecutionResourceActionTypeDef",
    "LifecycleExecutionResourceStateTypeDef",
    "LifecycleExecutionResourceTypeDef",
    "LifecycleExecutionResourcesImpactedSummaryTypeDef",
    "LifecycleExecutionSnapshotResourceTypeDef",
    "LifecycleExecutionStateTypeDef",
    "LifecycleExecutionTypeDef",
    "LifecyclePolicyDetailActionIncludeResourcesTypeDef",
    "LifecyclePolicyDetailActionTypeDef",
    "LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef",
    "LifecyclePolicyDetailExclusionRulesAmisTypeDef",
    "LifecyclePolicyDetailExclusionRulesTypeDef",
    "LifecyclePolicyDetailFilterTypeDef",
    "LifecyclePolicyDetailTypeDef",
    "LifecyclePolicyResourceSelectionRecipeTypeDef",
    "LifecyclePolicyResourceSelectionTypeDef",
    "LifecyclePolicySummaryTypeDef",
    "LifecyclePolicyTypeDef",
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
    "ListImageScanFindingAggregationsRequestRequestTypeDef",
    "ListImageScanFindingAggregationsResponseTypeDef",
    "ListImageScanFindingsRequestRequestTypeDef",
    "ListImageScanFindingsResponseTypeDef",
    "ListImagesRequestRequestTypeDef",
    "ListImagesResponseTypeDef",
    "ListInfrastructureConfigurationsRequestRequestTypeDef",
    "ListInfrastructureConfigurationsResponseTypeDef",
    "ListLifecycleExecutionResourcesRequestRequestTypeDef",
    "ListLifecycleExecutionResourcesResponseTypeDef",
    "ListLifecycleExecutionsRequestRequestTypeDef",
    "ListLifecycleExecutionsResponseTypeDef",
    "ListLifecyclePoliciesRequestRequestTypeDef",
    "ListLifecyclePoliciesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWaitingWorkflowStepsRequestRequestTypeDef",
    "ListWaitingWorkflowStepsResponseTypeDef",
    "ListWorkflowBuildVersionsRequestRequestTypeDef",
    "ListWorkflowBuildVersionsResponseTypeDef",
    "ListWorkflowExecutionsRequestRequestTypeDef",
    "ListWorkflowExecutionsResponseTypeDef",
    "ListWorkflowStepExecutionsRequestRequestTypeDef",
    "ListWorkflowStepExecutionsResponseTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LoggingTypeDef",
    "OutputResourcesTypeDef",
    "PackageVulnerabilityDetailsTypeDef",
    "PutComponentPolicyRequestRequestTypeDef",
    "PutComponentPolicyResponseTypeDef",
    "PutContainerRecipePolicyRequestRequestTypeDef",
    "PutContainerRecipePolicyResponseTypeDef",
    "PutImagePolicyRequestRequestTypeDef",
    "PutImagePolicyResponseTypeDef",
    "PutImageRecipePolicyRequestRequestTypeDef",
    "PutImageRecipePolicyResponseTypeDef",
    "RemediationRecommendationTypeDef",
    "RemediationTypeDef",
    "ResourceStateTypeDef",
    "ResourceStateUpdateExclusionRulesTypeDef",
    "ResourceStateUpdateIncludeResourcesTypeDef",
    "ResponseMetadataTypeDef",
    "S3ExportConfigurationTypeDef",
    "S3LogsTypeDef",
    "ScheduleTypeDef",
    "SendWorkflowStepActionRequestRequestTypeDef",
    "SendWorkflowStepActionResponseTypeDef",
    "SeverityCountsTypeDef",
    "StartImagePipelineExecutionRequestRequestTypeDef",
    "StartImagePipelineExecutionResponseTypeDef",
    "StartResourceStateUpdateRequestRequestTypeDef",
    "StartResourceStateUpdateResponseTypeDef",
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
    "UpdateLifecyclePolicyRequestRequestTypeDef",
    "UpdateLifecyclePolicyResponseTypeDef",
    "VulnerabilityIdAggregationTypeDef",
    "VulnerablePackageTypeDef",
    "WorkflowConfigurationTypeDef",
    "WorkflowExecutionMetadataTypeDef",
    "WorkflowParameterDetailTypeDef",
    "WorkflowParameterTypeDef",
    "WorkflowStateTypeDef",
    "WorkflowStepExecutionTypeDef",
    "WorkflowStepMetadataTypeDef",
    "WorkflowSummaryTypeDef",
    "WorkflowTypeDef",
    "WorkflowVersionTypeDef",
)

AccountAggregationTypeDef = TypedDict(
    "AccountAggregationTypeDef",
    {
        "accountId": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
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

CancelLifecycleExecutionRequestRequestTypeDef = TypedDict(
    "CancelLifecycleExecutionRequestRequestTypeDef",
    {
        "lifecycleExecutionId": str,
        "clientToken": str,
    },
)

CancelLifecycleExecutionResponseTypeDef = TypedDict(
    "CancelLifecycleExecutionResponseTypeDef",
    {
        "lifecycleExecutionId": str,
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

ComponentStateTypeDef = TypedDict(
    "ComponentStateTypeDef",
    {
        "status": Literal["DEPRECATED"],
        "reason": str,
    },
    total=False,
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "platform": PlatformType,
        "supportedOsVersions": List[str],
        "state": "ComponentStateTypeDef",
        "type": ComponentTypeType,
        "owner": str,
        "description": str,
        "changeDescription": str,
        "dateCreated": str,
        "tags": Dict[str, str],
        "publisher": str,
        "obfuscate": bool,
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
        "state": "ComponentStateTypeDef",
        "parameters": List["ComponentParameterDetailTypeDef"],
        "owner": str,
        "data": str,
        "kmsKeyId": str,
        "encrypted": bool,
        "dateCreated": str,
        "tags": Dict[str, str],
        "publisher": str,
        "obfuscate": bool,
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
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "workflows": List["WorkflowConfigurationTypeDef"],
        "executionRole": str,
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
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "workflows": List["WorkflowConfigurationTypeDef"],
        "executionRole": str,
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
        "instanceMetadataOptions": "InstanceMetadataOptionsTypeDef",
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

_RequiredCreateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLifecyclePolicyRequestRequestTypeDef",
    {
        "name": str,
        "executionRole": str,
        "resourceType": LifecyclePolicyResourceTypeType,
        "policyDetails": List["LifecyclePolicyDetailTypeDef"],
        "resourceSelection": "LifecyclePolicyResourceSelectionTypeDef",
        "clientToken": str,
    },
)
_OptionalCreateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLifecyclePolicyRequestRequestTypeDef",
    {
        "description": str,
        "status": LifecyclePolicyStatusType,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateLifecyclePolicyRequestRequestTypeDef(
    _RequiredCreateLifecyclePolicyRequestRequestTypeDef,
    _OptionalCreateLifecyclePolicyRequestRequestTypeDef,
):
    pass

CreateLifecyclePolicyResponseTypeDef = TypedDict(
    "CreateLifecyclePolicyResponseTypeDef",
    {
        "clientToken": str,
        "lifecyclePolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkflowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkflowRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "clientToken": str,
        "type": WorkflowTypeType,
    },
)
_OptionalCreateWorkflowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkflowRequestRequestTypeDef",
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

class CreateWorkflowRequestRequestTypeDef(
    _RequiredCreateWorkflowRequestRequestTypeDef, _OptionalCreateWorkflowRequestRequestTypeDef
):
    pass

CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "clientToken": str,
        "workflowBuildVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CvssScoreAdjustmentTypeDef = TypedDict(
    "CvssScoreAdjustmentTypeDef",
    {
        "metric": str,
        "reason": str,
    },
    total=False,
)

CvssScoreDetailsTypeDef = TypedDict(
    "CvssScoreDetailsTypeDef",
    {
        "scoreSource": str,
        "cvssSource": str,
        "version": str,
        "score": float,
        "scoringVector": str,
        "adjustments": List["CvssScoreAdjustmentTypeDef"],
    },
    total=False,
)

CvssScoreTypeDef = TypedDict(
    "CvssScoreTypeDef",
    {
        "baseScore": float,
        "scoringVector": str,
        "version": str,
        "source": str,
    },
    total=False,
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

DeleteLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "DeleteLifecyclePolicyRequestRequestTypeDef",
    {
        "lifecyclePolicyArn": str,
    },
)

DeleteLifecyclePolicyResponseTypeDef = TypedDict(
    "DeleteLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "workflowBuildVersionArn": str,
    },
)

DeleteWorkflowResponseTypeDef = TypedDict(
    "DeleteWorkflowResponseTypeDef",
    {
        "workflowBuildVersionArn": str,
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
        "s3ExportConfiguration": "S3ExportConfigurationTypeDef",
        "fastLaunchConfigurations": List["FastLaunchConfigurationTypeDef"],
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
        "throughput": int,
    },
    total=False,
)

EcrConfigurationTypeDef = TypedDict(
    "EcrConfigurationTypeDef",
    {
        "repositoryName": str,
        "containerTags": List[str],
    },
    total=False,
)

_RequiredFastLaunchConfigurationTypeDef = TypedDict(
    "_RequiredFastLaunchConfigurationTypeDef",
    {
        "enabled": bool,
    },
)
_OptionalFastLaunchConfigurationTypeDef = TypedDict(
    "_OptionalFastLaunchConfigurationTypeDef",
    {
        "snapshotConfiguration": "FastLaunchSnapshotConfigurationTypeDef",
        "maxParallelLaunches": int,
        "launchTemplate": "FastLaunchLaunchTemplateSpecificationTypeDef",
        "accountId": str,
    },
    total=False,
)

class FastLaunchConfigurationTypeDef(
    _RequiredFastLaunchConfigurationTypeDef, _OptionalFastLaunchConfigurationTypeDef
):
    pass

FastLaunchLaunchTemplateSpecificationTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationTypeDef",
    {
        "launchTemplateId": str,
        "launchTemplateName": str,
        "launchTemplateVersion": str,
    },
    total=False,
)

FastLaunchSnapshotConfigurationTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationTypeDef",
    {
        "targetResourceCount": int,
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

GetLifecycleExecutionRequestRequestTypeDef = TypedDict(
    "GetLifecycleExecutionRequestRequestTypeDef",
    {
        "lifecycleExecutionId": str,
    },
)

GetLifecycleExecutionResponseTypeDef = TypedDict(
    "GetLifecycleExecutionResponseTypeDef",
    {
        "lifecycleExecution": "LifecycleExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "GetLifecyclePolicyRequestRequestTypeDef",
    {
        "lifecyclePolicyArn": str,
    },
)

GetLifecyclePolicyResponseTypeDef = TypedDict(
    "GetLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicy": "LifecyclePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowExecutionRequestRequestTypeDef = TypedDict(
    "GetWorkflowExecutionRequestRequestTypeDef",
    {
        "workflowExecutionId": str,
    },
)

GetWorkflowExecutionResponseTypeDef = TypedDict(
    "GetWorkflowExecutionResponseTypeDef",
    {
        "requestId": str,
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "type": WorkflowTypeType,
        "status": WorkflowExecutionStatusType,
        "message": str,
        "totalStepCount": int,
        "totalStepsSucceeded": int,
        "totalStepsFailed": int,
        "totalStepsSkipped": int,
        "startTime": str,
        "endTime": str,
        "parallelGroup": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "workflowBuildVersionArn": str,
    },
)

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "workflow": "WorkflowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowStepExecutionRequestRequestTypeDef = TypedDict(
    "GetWorkflowStepExecutionRequestRequestTypeDef",
    {
        "stepExecutionId": str,
    },
)

GetWorkflowStepExecutionResponseTypeDef = TypedDict(
    "GetWorkflowStepExecutionResponseTypeDef",
    {
        "requestId": str,
        "stepExecutionId": str,
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "name": str,
        "description": str,
        "action": str,
        "status": WorkflowStepExecutionStatusType,
        "rollbackStatus": WorkflowStepExecutionRollbackStatusType,
        "message": str,
        "inputs": str,
        "outputs": str,
        "startTime": str,
        "endTime": str,
        "onFailure": str,
        "timeoutSeconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageAggregationTypeDef = TypedDict(
    "ImageAggregationTypeDef",
    {
        "imageBuildVersionArn": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

ImagePackageTypeDef = TypedDict(
    "ImagePackageTypeDef",
    {
        "packageName": str,
        "packageVersion": str,
    },
    total=False,
)

ImagePipelineAggregationTypeDef = TypedDict(
    "ImagePipelineAggregationTypeDef",
    {
        "imagePipelineArn": str,
        "severityCounts": "SeverityCountsTypeDef",
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
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "executionRole": str,
        "workflows": List["WorkflowConfigurationTypeDef"],
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

ImageScanFindingAggregationTypeDef = TypedDict(
    "ImageScanFindingAggregationTypeDef",
    {
        "accountAggregation": "AccountAggregationTypeDef",
        "imageAggregation": "ImageAggregationTypeDef",
        "imagePipelineAggregation": "ImagePipelineAggregationTypeDef",
        "vulnerabilityIdAggregation": "VulnerabilityIdAggregationTypeDef",
    },
    total=False,
)

ImageScanFindingTypeDef = TypedDict(
    "ImageScanFindingTypeDef",
    {
        "awsAccountId": str,
        "imageBuildVersionArn": str,
        "imagePipelineArn": str,
        "type": str,
        "description": str,
        "title": str,
        "remediation": "RemediationTypeDef",
        "severity": str,
        "firstObservedAt": datetime,
        "updatedAt": datetime,
        "inspectorScore": float,
        "inspectorScoreDetails": "InspectorScoreDetailsTypeDef",
        "packageVulnerabilityDetails": "PackageVulnerabilityDetailsTypeDef",
        "fixAvailable": str,
    },
    total=False,
)

ImageScanFindingsFilterTypeDef = TypedDict(
    "ImageScanFindingsFilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
    total=False,
)

ImageScanStateTypeDef = TypedDict(
    "ImageScanStateTypeDef",
    {
        "status": ImageScanStatusType,
        "reason": str,
    },
    total=False,
)

ImageScanningConfigurationTypeDef = TypedDict(
    "ImageScanningConfigurationTypeDef",
    {
        "imageScanningEnabled": bool,
        "ecrConfiguration": "EcrConfigurationTypeDef",
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
        "buildType": BuildTypeType,
        "imageSource": ImageSourceType,
        "deprecationTime": datetime,
        "lifecycleExecutionId": str,
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
        "buildType": BuildTypeType,
        "imageSource": ImageSourceType,
        "scanState": "ImageScanStateTypeDef",
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "deprecationTime": datetime,
        "lifecycleExecutionId": str,
        "executionRole": str,
        "workflows": List["WorkflowConfigurationTypeDef"],
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
        "buildType": BuildTypeType,
        "imageSource": ImageSourceType,
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

_RequiredImportVmImageRequestRequestTypeDef = TypedDict(
    "_RequiredImportVmImageRequestRequestTypeDef",
    {
        "name": str,
        "semanticVersion": str,
        "platform": PlatformType,
        "vmImportTaskId": str,
        "clientToken": str,
    },
)
_OptionalImportVmImageRequestRequestTypeDef = TypedDict(
    "_OptionalImportVmImageRequestRequestTypeDef",
    {
        "description": str,
        "osVersion": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ImportVmImageRequestRequestTypeDef(
    _RequiredImportVmImageRequestRequestTypeDef, _OptionalImportVmImageRequestRequestTypeDef
):
    pass

ImportVmImageResponseTypeDef = TypedDict(
    "ImportVmImageResponseTypeDef",
    {
        "requestId": str,
        "imageArn": str,
        "clientToken": str,
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
        "instanceMetadataOptions": "InstanceMetadataOptionsTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

InspectorScoreDetailsTypeDef = TypedDict(
    "InspectorScoreDetailsTypeDef",
    {
        "adjustedCvss": "CvssScoreDetailsTypeDef",
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

InstanceMetadataOptionsTypeDef = TypedDict(
    "InstanceMetadataOptionsTypeDef",
    {
        "httpTokens": str,
        "httpPutResponseHopLimit": int,
    },
    total=False,
)

LaunchPermissionConfigurationTypeDef = TypedDict(
    "LaunchPermissionConfigurationTypeDef",
    {
        "userIds": List[str],
        "userGroups": List[str],
        "organizationArns": List[str],
        "organizationalUnitArns": List[str],
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

LifecycleExecutionResourceActionTypeDef = TypedDict(
    "LifecycleExecutionResourceActionTypeDef",
    {
        "name": LifecycleExecutionResourceActionNameType,
        "reason": str,
    },
    total=False,
)

LifecycleExecutionResourceStateTypeDef = TypedDict(
    "LifecycleExecutionResourceStateTypeDef",
    {
        "status": LifecycleExecutionResourceStatusType,
        "reason": str,
    },
    total=False,
)

LifecycleExecutionResourceTypeDef = TypedDict(
    "LifecycleExecutionResourceTypeDef",
    {
        "accountId": str,
        "resourceId": str,
        "state": "LifecycleExecutionResourceStateTypeDef",
        "action": "LifecycleExecutionResourceActionTypeDef",
        "region": str,
        "snapshots": List["LifecycleExecutionSnapshotResourceTypeDef"],
        "imageUris": List[str],
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

LifecycleExecutionResourcesImpactedSummaryTypeDef = TypedDict(
    "LifecycleExecutionResourcesImpactedSummaryTypeDef",
    {
        "hasImpactedResources": bool,
    },
    total=False,
)

LifecycleExecutionSnapshotResourceTypeDef = TypedDict(
    "LifecycleExecutionSnapshotResourceTypeDef",
    {
        "snapshotId": str,
        "state": "LifecycleExecutionResourceStateTypeDef",
    },
    total=False,
)

LifecycleExecutionStateTypeDef = TypedDict(
    "LifecycleExecutionStateTypeDef",
    {
        "status": LifecycleExecutionStatusType,
        "reason": str,
    },
    total=False,
)

LifecycleExecutionTypeDef = TypedDict(
    "LifecycleExecutionTypeDef",
    {
        "lifecycleExecutionId": str,
        "lifecyclePolicyArn": str,
        "resourcesImpactedSummary": "LifecycleExecutionResourcesImpactedSummaryTypeDef",
        "state": "LifecycleExecutionStateTypeDef",
        "startTime": datetime,
        "endTime": datetime,
    },
    total=False,
)

LifecyclePolicyDetailActionIncludeResourcesTypeDef = TypedDict(
    "LifecyclePolicyDetailActionIncludeResourcesTypeDef",
    {
        "amis": bool,
        "snapshots": bool,
        "containers": bool,
    },
    total=False,
)

_RequiredLifecyclePolicyDetailActionTypeDef = TypedDict(
    "_RequiredLifecyclePolicyDetailActionTypeDef",
    {
        "type": LifecyclePolicyDetailActionTypeType,
    },
)
_OptionalLifecyclePolicyDetailActionTypeDef = TypedDict(
    "_OptionalLifecyclePolicyDetailActionTypeDef",
    {
        "includeResources": "LifecyclePolicyDetailActionIncludeResourcesTypeDef",
    },
    total=False,
)

class LifecyclePolicyDetailActionTypeDef(
    _RequiredLifecyclePolicyDetailActionTypeDef, _OptionalLifecyclePolicyDetailActionTypeDef
):
    pass

LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef = TypedDict(
    "LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef",
    {
        "value": int,
        "unit": LifecyclePolicyTimeUnitType,
    },
)

LifecyclePolicyDetailExclusionRulesAmisTypeDef = TypedDict(
    "LifecyclePolicyDetailExclusionRulesAmisTypeDef",
    {
        "isPublic": bool,
        "regions": List[str],
        "sharedAccounts": List[str],
        "lastLaunched": "LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef",
        "tagMap": Dict[str, str],
    },
    total=False,
)

LifecyclePolicyDetailExclusionRulesTypeDef = TypedDict(
    "LifecyclePolicyDetailExclusionRulesTypeDef",
    {
        "tagMap": Dict[str, str],
        "amis": "LifecyclePolicyDetailExclusionRulesAmisTypeDef",
    },
    total=False,
)

_RequiredLifecyclePolicyDetailFilterTypeDef = TypedDict(
    "_RequiredLifecyclePolicyDetailFilterTypeDef",
    {
        "type": LifecyclePolicyDetailFilterTypeType,
        "value": int,
    },
)
_OptionalLifecyclePolicyDetailFilterTypeDef = TypedDict(
    "_OptionalLifecyclePolicyDetailFilterTypeDef",
    {
        "unit": LifecyclePolicyTimeUnitType,
        "retainAtLeast": int,
    },
    total=False,
)

class LifecyclePolicyDetailFilterTypeDef(
    _RequiredLifecyclePolicyDetailFilterTypeDef, _OptionalLifecyclePolicyDetailFilterTypeDef
):
    pass

_RequiredLifecyclePolicyDetailTypeDef = TypedDict(
    "_RequiredLifecyclePolicyDetailTypeDef",
    {
        "action": "LifecyclePolicyDetailActionTypeDef",
        "filter": "LifecyclePolicyDetailFilterTypeDef",
    },
)
_OptionalLifecyclePolicyDetailTypeDef = TypedDict(
    "_OptionalLifecyclePolicyDetailTypeDef",
    {
        "exclusionRules": "LifecyclePolicyDetailExclusionRulesTypeDef",
    },
    total=False,
)

class LifecyclePolicyDetailTypeDef(
    _RequiredLifecyclePolicyDetailTypeDef, _OptionalLifecyclePolicyDetailTypeDef
):
    pass

LifecyclePolicyResourceSelectionRecipeTypeDef = TypedDict(
    "LifecyclePolicyResourceSelectionRecipeTypeDef",
    {
        "name": str,
        "semanticVersion": str,
    },
)

LifecyclePolicyResourceSelectionTypeDef = TypedDict(
    "LifecyclePolicyResourceSelectionTypeDef",
    {
        "recipes": List["LifecyclePolicyResourceSelectionRecipeTypeDef"],
        "tagMap": Dict[str, str],
    },
    total=False,
)

LifecyclePolicySummaryTypeDef = TypedDict(
    "LifecyclePolicySummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "status": LifecyclePolicyStatusType,
        "executionRole": str,
        "resourceType": LifecyclePolicyResourceTypeType,
        "dateCreated": datetime,
        "dateUpdated": datetime,
        "dateLastRun": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

LifecyclePolicyTypeDef = TypedDict(
    "LifecyclePolicyTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "status": LifecyclePolicyStatusType,
        "executionRole": str,
        "resourceType": LifecyclePolicyResourceTypeType,
        "policyDetails": List["LifecyclePolicyDetailTypeDef"],
        "resourceSelection": "LifecyclePolicyResourceSelectionTypeDef",
        "dateCreated": datetime,
        "dateUpdated": datetime,
        "dateLastRun": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

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

ListImageScanFindingAggregationsRequestRequestTypeDef = TypedDict(
    "ListImageScanFindingAggregationsRequestRequestTypeDef",
    {
        "filter": "FilterTypeDef",
        "nextToken": str,
    },
    total=False,
)

ListImageScanFindingAggregationsResponseTypeDef = TypedDict(
    "ListImageScanFindingAggregationsResponseTypeDef",
    {
        "requestId": str,
        "aggregationType": str,
        "responses": List["ImageScanFindingAggregationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListImageScanFindingsRequestRequestTypeDef = TypedDict(
    "ListImageScanFindingsRequestRequestTypeDef",
    {
        "filters": List["ImageScanFindingsFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListImageScanFindingsResponseTypeDef = TypedDict(
    "ListImageScanFindingsResponseTypeDef",
    {
        "requestId": str,
        "findings": List["ImageScanFindingTypeDef"],
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

_RequiredListLifecycleExecutionResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListLifecycleExecutionResourcesRequestRequestTypeDef",
    {
        "lifecycleExecutionId": str,
    },
)
_OptionalListLifecycleExecutionResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListLifecycleExecutionResourcesRequestRequestTypeDef",
    {
        "parentResourceId": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListLifecycleExecutionResourcesRequestRequestTypeDef(
    _RequiredListLifecycleExecutionResourcesRequestRequestTypeDef,
    _OptionalListLifecycleExecutionResourcesRequestRequestTypeDef,
):
    pass

ListLifecycleExecutionResourcesResponseTypeDef = TypedDict(
    "ListLifecycleExecutionResourcesResponseTypeDef",
    {
        "lifecycleExecutionId": str,
        "lifecycleExecutionState": "LifecycleExecutionStateTypeDef",
        "resources": List["LifecycleExecutionResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLifecycleExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLifecycleExecutionsRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListLifecycleExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLifecycleExecutionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListLifecycleExecutionsRequestRequestTypeDef(
    _RequiredListLifecycleExecutionsRequestRequestTypeDef,
    _OptionalListLifecycleExecutionsRequestRequestTypeDef,
):
    pass

ListLifecycleExecutionsResponseTypeDef = TypedDict(
    "ListLifecycleExecutionsResponseTypeDef",
    {
        "lifecycleExecutions": List["LifecycleExecutionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLifecyclePoliciesRequestRequestTypeDef = TypedDict(
    "ListLifecyclePoliciesRequestRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListLifecyclePoliciesResponseTypeDef = TypedDict(
    "ListLifecyclePoliciesResponseTypeDef",
    {
        "lifecyclePolicySummaryList": List["LifecyclePolicySummaryTypeDef"],
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

ListWaitingWorkflowStepsRequestRequestTypeDef = TypedDict(
    "ListWaitingWorkflowStepsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWaitingWorkflowStepsResponseTypeDef = TypedDict(
    "ListWaitingWorkflowStepsResponseTypeDef",
    {
        "steps": List["WorkflowStepExecutionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkflowBuildVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkflowBuildVersionsRequestRequestTypeDef",
    {
        "workflowVersionArn": str,
    },
)
_OptionalListWorkflowBuildVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkflowBuildVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListWorkflowBuildVersionsRequestRequestTypeDef(
    _RequiredListWorkflowBuildVersionsRequestRequestTypeDef,
    _OptionalListWorkflowBuildVersionsRequestRequestTypeDef,
):
    pass

ListWorkflowBuildVersionsResponseTypeDef = TypedDict(
    "ListWorkflowBuildVersionsResponseTypeDef",
    {
        "workflowSummaryList": List["WorkflowSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkflowExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkflowExecutionsRequestRequestTypeDef",
    {
        "imageBuildVersionArn": str,
    },
)
_OptionalListWorkflowExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkflowExecutionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListWorkflowExecutionsRequestRequestTypeDef(
    _RequiredListWorkflowExecutionsRequestRequestTypeDef,
    _OptionalListWorkflowExecutionsRequestRequestTypeDef,
):
    pass

ListWorkflowExecutionsResponseTypeDef = TypedDict(
    "ListWorkflowExecutionsResponseTypeDef",
    {
        "requestId": str,
        "workflowExecutions": List["WorkflowExecutionMetadataTypeDef"],
        "imageBuildVersionArn": str,
        "message": str,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWorkflowStepExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListWorkflowStepExecutionsRequestRequestTypeDef",
    {
        "workflowExecutionId": str,
    },
)
_OptionalListWorkflowStepExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListWorkflowStepExecutionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListWorkflowStepExecutionsRequestRequestTypeDef(
    _RequiredListWorkflowStepExecutionsRequestRequestTypeDef,
    _OptionalListWorkflowStepExecutionsRequestRequestTypeDef,
):
    pass

ListWorkflowStepExecutionsResponseTypeDef = TypedDict(
    "ListWorkflowStepExecutionsResponseTypeDef",
    {
        "requestId": str,
        "steps": List["WorkflowStepMetadataTypeDef"],
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "imageBuildVersionArn": str,
        "message": str,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "owner": OwnershipType,
        "filters": List["FilterTypeDef"],
        "byName": bool,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "workflowVersionList": List["WorkflowVersionTypeDef"],
        "nextToken": str,
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

_RequiredPackageVulnerabilityDetailsTypeDef = TypedDict(
    "_RequiredPackageVulnerabilityDetailsTypeDef",
    {
        "vulnerabilityId": str,
    },
)
_OptionalPackageVulnerabilityDetailsTypeDef = TypedDict(
    "_OptionalPackageVulnerabilityDetailsTypeDef",
    {
        "vulnerablePackages": List["VulnerablePackageTypeDef"],
        "source": str,
        "cvss": List["CvssScoreTypeDef"],
        "relatedVulnerabilities": List[str],
        "sourceUrl": str,
        "vendorSeverity": str,
        "vendorCreatedAt": datetime,
        "vendorUpdatedAt": datetime,
        "referenceUrls": List[str],
    },
    total=False,
)

class PackageVulnerabilityDetailsTypeDef(
    _RequiredPackageVulnerabilityDetailsTypeDef, _OptionalPackageVulnerabilityDetailsTypeDef
):
    pass

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

RemediationRecommendationTypeDef = TypedDict(
    "RemediationRecommendationTypeDef",
    {
        "text": str,
        "url": str,
    },
    total=False,
)

RemediationTypeDef = TypedDict(
    "RemediationTypeDef",
    {
        "recommendation": "RemediationRecommendationTypeDef",
    },
    total=False,
)

ResourceStateTypeDef = TypedDict(
    "ResourceStateTypeDef",
    {
        "status": ResourceStatusType,
    },
    total=False,
)

ResourceStateUpdateExclusionRulesTypeDef = TypedDict(
    "ResourceStateUpdateExclusionRulesTypeDef",
    {
        "amis": "LifecyclePolicyDetailExclusionRulesAmisTypeDef",
    },
    total=False,
)

ResourceStateUpdateIncludeResourcesTypeDef = TypedDict(
    "ResourceStateUpdateIncludeResourcesTypeDef",
    {
        "amis": bool,
        "snapshots": bool,
        "containers": bool,
    },
    total=False,
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

_RequiredS3ExportConfigurationTypeDef = TypedDict(
    "_RequiredS3ExportConfigurationTypeDef",
    {
        "roleName": str,
        "diskImageFormat": DiskImageFormatType,
        "s3Bucket": str,
    },
)
_OptionalS3ExportConfigurationTypeDef = TypedDict(
    "_OptionalS3ExportConfigurationTypeDef",
    {
        "s3Prefix": str,
    },
    total=False,
)

class S3ExportConfigurationTypeDef(
    _RequiredS3ExportConfigurationTypeDef, _OptionalS3ExportConfigurationTypeDef
):
    pass

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

_RequiredSendWorkflowStepActionRequestRequestTypeDef = TypedDict(
    "_RequiredSendWorkflowStepActionRequestRequestTypeDef",
    {
        "stepExecutionId": str,
        "imageBuildVersionArn": str,
        "action": WorkflowStepActionTypeType,
        "clientToken": str,
    },
)
_OptionalSendWorkflowStepActionRequestRequestTypeDef = TypedDict(
    "_OptionalSendWorkflowStepActionRequestRequestTypeDef",
    {
        "reason": str,
    },
    total=False,
)

class SendWorkflowStepActionRequestRequestTypeDef(
    _RequiredSendWorkflowStepActionRequestRequestTypeDef,
    _OptionalSendWorkflowStepActionRequestRequestTypeDef,
):
    pass

SendWorkflowStepActionResponseTypeDef = TypedDict(
    "SendWorkflowStepActionResponseTypeDef",
    {
        "stepExecutionId": str,
        "imageBuildVersionArn": str,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SeverityCountsTypeDef = TypedDict(
    "SeverityCountsTypeDef",
    {
        "all": int,
        "critical": int,
        "high": int,
        "medium": int,
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

_RequiredStartResourceStateUpdateRequestRequestTypeDef = TypedDict(
    "_RequiredStartResourceStateUpdateRequestRequestTypeDef",
    {
        "resourceArn": str,
        "state": "ResourceStateTypeDef",
        "clientToken": str,
    },
)
_OptionalStartResourceStateUpdateRequestRequestTypeDef = TypedDict(
    "_OptionalStartResourceStateUpdateRequestRequestTypeDef",
    {
        "executionRole": str,
        "includeResources": "ResourceStateUpdateIncludeResourcesTypeDef",
        "exclusionRules": "ResourceStateUpdateExclusionRulesTypeDef",
        "updateAt": Union[datetime, str],
    },
    total=False,
)

class StartResourceStateUpdateRequestRequestTypeDef(
    _RequiredStartResourceStateUpdateRequestRequestTypeDef,
    _OptionalStartResourceStateUpdateRequestRequestTypeDef,
):
    pass

StartResourceStateUpdateResponseTypeDef = TypedDict(
    "StartResourceStateUpdateResponseTypeDef",
    {
        "lifecycleExecutionId": str,
        "resourceArn": str,
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
        "imageScanningConfiguration": "ImageScanningConfigurationTypeDef",
        "workflows": List["WorkflowConfigurationTypeDef"],
        "executionRole": str,
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
        "instanceMetadataOptions": "InstanceMetadataOptionsTypeDef",
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

_RequiredUpdateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLifecyclePolicyRequestRequestTypeDef",
    {
        "lifecyclePolicyArn": str,
        "executionRole": str,
        "resourceType": LifecyclePolicyResourceTypeType,
        "policyDetails": List["LifecyclePolicyDetailTypeDef"],
        "resourceSelection": "LifecyclePolicyResourceSelectionTypeDef",
        "clientToken": str,
    },
)
_OptionalUpdateLifecyclePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLifecyclePolicyRequestRequestTypeDef",
    {
        "description": str,
        "status": LifecyclePolicyStatusType,
    },
    total=False,
)

class UpdateLifecyclePolicyRequestRequestTypeDef(
    _RequiredUpdateLifecyclePolicyRequestRequestTypeDef,
    _OptionalUpdateLifecyclePolicyRequestRequestTypeDef,
):
    pass

UpdateLifecyclePolicyResponseTypeDef = TypedDict(
    "UpdateLifecyclePolicyResponseTypeDef",
    {
        "lifecyclePolicyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VulnerabilityIdAggregationTypeDef = TypedDict(
    "VulnerabilityIdAggregationTypeDef",
    {
        "vulnerabilityId": str,
        "severityCounts": "SeverityCountsTypeDef",
    },
    total=False,
)

VulnerablePackageTypeDef = TypedDict(
    "VulnerablePackageTypeDef",
    {
        "name": str,
        "version": str,
        "sourceLayerHash": str,
        "epoch": int,
        "release": str,
        "arch": str,
        "packageManager": str,
        "filePath": str,
        "fixedInVersion": str,
        "remediation": str,
    },
    total=False,
)

_RequiredWorkflowConfigurationTypeDef = TypedDict(
    "_RequiredWorkflowConfigurationTypeDef",
    {
        "workflowArn": str,
    },
)
_OptionalWorkflowConfigurationTypeDef = TypedDict(
    "_OptionalWorkflowConfigurationTypeDef",
    {
        "parameters": List["WorkflowParameterTypeDef"],
        "parallelGroup": str,
        "onFailure": OnWorkflowFailureType,
    },
    total=False,
)

class WorkflowConfigurationTypeDef(
    _RequiredWorkflowConfigurationTypeDef, _OptionalWorkflowConfigurationTypeDef
):
    pass

WorkflowExecutionMetadataTypeDef = TypedDict(
    "WorkflowExecutionMetadataTypeDef",
    {
        "workflowBuildVersionArn": str,
        "workflowExecutionId": str,
        "type": WorkflowTypeType,
        "status": WorkflowExecutionStatusType,
        "message": str,
        "totalStepCount": int,
        "totalStepsSucceeded": int,
        "totalStepsFailed": int,
        "totalStepsSkipped": int,
        "startTime": str,
        "endTime": str,
        "parallelGroup": str,
    },
    total=False,
)

_RequiredWorkflowParameterDetailTypeDef = TypedDict(
    "_RequiredWorkflowParameterDetailTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalWorkflowParameterDetailTypeDef = TypedDict(
    "_OptionalWorkflowParameterDetailTypeDef",
    {
        "defaultValue": List[str],
        "description": str,
    },
    total=False,
)

class WorkflowParameterDetailTypeDef(
    _RequiredWorkflowParameterDetailTypeDef, _OptionalWorkflowParameterDetailTypeDef
):
    pass

WorkflowParameterTypeDef = TypedDict(
    "WorkflowParameterTypeDef",
    {
        "name": str,
        "value": List[str],
    },
)

WorkflowStateTypeDef = TypedDict(
    "WorkflowStateTypeDef",
    {
        "status": Literal["DEPRECATED"],
        "reason": str,
    },
    total=False,
)

WorkflowStepExecutionTypeDef = TypedDict(
    "WorkflowStepExecutionTypeDef",
    {
        "stepExecutionId": str,
        "imageBuildVersionArn": str,
        "workflowExecutionId": str,
        "workflowBuildVersionArn": str,
        "name": str,
        "action": str,
        "startTime": str,
    },
    total=False,
)

WorkflowStepMetadataTypeDef = TypedDict(
    "WorkflowStepMetadataTypeDef",
    {
        "stepExecutionId": str,
        "name": str,
        "description": str,
        "action": str,
        "status": WorkflowStepExecutionStatusType,
        "rollbackStatus": WorkflowStepExecutionRollbackStatusType,
        "message": str,
        "inputs": str,
        "outputs": str,
        "startTime": str,
        "endTime": str,
    },
    total=False,
)

WorkflowSummaryTypeDef = TypedDict(
    "WorkflowSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "changeDescription": str,
        "type": WorkflowTypeType,
        "owner": str,
        "state": "WorkflowStateTypeDef",
        "dateCreated": str,
        "tags": Dict[str, str],
    },
    total=False,
)

WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "changeDescription": str,
        "type": WorkflowTypeType,
        "state": "WorkflowStateTypeDef",
        "owner": str,
        "data": str,
        "kmsKeyId": str,
        "dateCreated": str,
        "tags": Dict[str, str],
        "parameters": List["WorkflowParameterDetailTypeDef"],
    },
    total=False,
)

WorkflowVersionTypeDef = TypedDict(
    "WorkflowVersionTypeDef",
    {
        "arn": str,
        "name": str,
        "version": str,
        "description": str,
        "type": WorkflowTypeType,
        "owner": str,
        "dateCreated": str,
    },
    total=False,
)
