"""
Type annotations for greengrassv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_greengrassv2.type_defs import AssociateClientDeviceWithCoreDeviceEntryTypeDef

    data: AssociateClientDeviceWithCoreDeviceEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    CloudComponentStateType,
    ComponentDependencyTypeType,
    ComponentVisibilityScopeType,
    CoreDeviceStatusType,
    DeploymentComponentUpdatePolicyActionType,
    DeploymentFailureHandlingPolicyType,
    DeploymentHistoryFilterType,
    DeploymentStatusType,
    EffectiveDeploymentExecutionStatusType,
    InstalledComponentLifecycleStateType,
    IoTJobExecutionFailureTypeType,
    LambdaEventSourceTypeType,
    LambdaFilesystemPermissionType,
    LambdaInputPayloadEncodingTypeType,
    LambdaIsolationModeType,
    RecipeOutputFormatType,
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
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    "AssociatedClientDeviceTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef",
    "CancelDeploymentRequestRequestTypeDef",
    "CancelDeploymentResponseTypeDef",
    "CloudComponentStatusTypeDef",
    "ComponentCandidateTypeDef",
    "ComponentConfigurationUpdateTypeDef",
    "ComponentDependencyRequirementTypeDef",
    "ComponentDeploymentSpecificationTypeDef",
    "ComponentLatestVersionTypeDef",
    "ComponentPlatformTypeDef",
    "ComponentRunWithTypeDef",
    "ComponentTypeDef",
    "ComponentVersionListItemTypeDef",
    "CoreDeviceTypeDef",
    "CreateComponentVersionRequestRequestTypeDef",
    "CreateComponentVersionResponseTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteCoreDeviceRequestRequestTypeDef",
    "DeploymentComponentUpdatePolicyTypeDef",
    "DeploymentConfigurationValidationPolicyTypeDef",
    "DeploymentIoTJobConfigurationTypeDef",
    "DeploymentPoliciesTypeDef",
    "DeploymentTypeDef",
    "DescribeComponentRequestRequestTypeDef",
    "DescribeComponentResponseTypeDef",
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    "EffectiveDeploymentTypeDef",
    "GetComponentRequestRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetComponentVersionArtifactRequestRequestTypeDef",
    "GetComponentVersionArtifactResponseTypeDef",
    "GetCoreDeviceRequestRequestTypeDef",
    "GetCoreDeviceResponseTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentResponseTypeDef",
    "InstalledComponentTypeDef",
    "IoTJobAbortConfigTypeDef",
    "IoTJobAbortCriteriaTypeDef",
    "IoTJobExecutionsRolloutConfigTypeDef",
    "IoTJobExponentialRolloutRateTypeDef",
    "IoTJobRateIncreaseCriteriaTypeDef",
    "IoTJobTimeoutConfigTypeDef",
    "LambdaContainerParamsTypeDef",
    "LambdaDeviceMountTypeDef",
    "LambdaEventSourceTypeDef",
    "LambdaExecutionParametersTypeDef",
    "LambdaFunctionRecipeSourceTypeDef",
    "LambdaLinuxProcessParamsTypeDef",
    "LambdaVolumeMountTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef",
    "ListComponentVersionsRequestRequestTypeDef",
    "ListComponentVersionsResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListCoreDevicesRequestRequestTypeDef",
    "ListCoreDevicesResponseTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListEffectiveDeploymentsRequestRequestTypeDef",
    "ListEffectiveDeploymentsResponseTypeDef",
    "ListInstalledComponentsRequestRequestTypeDef",
    "ListInstalledComponentsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResolveComponentCandidatesRequestRequestTypeDef",
    "ResolveComponentCandidatesResponseTypeDef",
    "ResolvedComponentVersionTypeDef",
    "ResponseMetadataTypeDef",
    "SystemResourceLimitsTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

AssociateClientDeviceWithCoreDeviceEntryTypeDef = TypedDict(
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    {
        "thingName": str,
    },
)

AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef = TypedDict(
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    {
        "thingName": str,
        "code": str,
        "message": str,
    },
    total=False,
)

AssociatedClientDeviceTypeDef = TypedDict(
    "AssociatedClientDeviceTypeDef",
    {
        "thingName": str,
        "associationTimestamp": datetime,
    },
    total=False,
)

_RequiredBatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredBatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalBatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalBatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef",
    {
        "entries": List["AssociateClientDeviceWithCoreDeviceEntryTypeDef"],
    },
    total=False,
)

class BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef(
    _RequiredBatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef,
    _OptionalBatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef,
):
    pass

BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef = TypedDict(
    "BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef",
    {
        "errorEntries": List["AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalBatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef",
    {
        "entries": List["DisassociateClientDeviceFromCoreDeviceEntryTypeDef"],
    },
    total=False,
)

class BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef(
    _RequiredBatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef,
    _OptionalBatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef,
):
    pass

BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef = TypedDict(
    "BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef",
    {
        "errorEntries": List["DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelDeploymentRequestRequestTypeDef = TypedDict(
    "CancelDeploymentRequestRequestTypeDef",
    {
        "deploymentId": str,
    },
)

CancelDeploymentResponseTypeDef = TypedDict(
    "CancelDeploymentResponseTypeDef",
    {
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudComponentStatusTypeDef = TypedDict(
    "CloudComponentStatusTypeDef",
    {
        "componentState": CloudComponentStateType,
        "message": str,
        "errors": Dict[str, str],
    },
    total=False,
)

ComponentCandidateTypeDef = TypedDict(
    "ComponentCandidateTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "versionRequirements": Dict[str, str],
    },
    total=False,
)

ComponentConfigurationUpdateTypeDef = TypedDict(
    "ComponentConfigurationUpdateTypeDef",
    {
        "merge": str,
        "reset": List[str],
    },
    total=False,
)

ComponentDependencyRequirementTypeDef = TypedDict(
    "ComponentDependencyRequirementTypeDef",
    {
        "versionRequirement": str,
        "dependencyType": ComponentDependencyTypeType,
    },
    total=False,
)

ComponentDeploymentSpecificationTypeDef = TypedDict(
    "ComponentDeploymentSpecificationTypeDef",
    {
        "componentVersion": str,
        "configurationUpdate": "ComponentConfigurationUpdateTypeDef",
        "runWith": "ComponentRunWithTypeDef",
    },
    total=False,
)

ComponentLatestVersionTypeDef = TypedDict(
    "ComponentLatestVersionTypeDef",
    {
        "arn": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "description": str,
        "publisher": str,
        "platforms": List["ComponentPlatformTypeDef"],
    },
    total=False,
)

ComponentPlatformTypeDef = TypedDict(
    "ComponentPlatformTypeDef",
    {
        "name": str,
        "attributes": Dict[str, str],
    },
    total=False,
)

ComponentRunWithTypeDef = TypedDict(
    "ComponentRunWithTypeDef",
    {
        "posixUser": str,
        "systemResourceLimits": "SystemResourceLimitsTypeDef",
    },
    total=False,
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "arn": str,
        "componentName": str,
        "latestVersion": "ComponentLatestVersionTypeDef",
    },
    total=False,
)

ComponentVersionListItemTypeDef = TypedDict(
    "ComponentVersionListItemTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "arn": str,
    },
    total=False,
)

CoreDeviceTypeDef = TypedDict(
    "CoreDeviceTypeDef",
    {
        "coreDeviceThingName": str,
        "status": CoreDeviceStatusType,
        "lastStatusUpdateTimestamp": datetime,
    },
    total=False,
)

CreateComponentVersionRequestRequestTypeDef = TypedDict(
    "CreateComponentVersionRequestRequestTypeDef",
    {
        "inlineRecipe": Union[bytes, IO[bytes], StreamingBody],
        "lambdaFunction": "LambdaFunctionRecipeSourceTypeDef",
        "tags": Dict[str, str],
        "clientToken": str,
    },
    total=False,
)

CreateComponentVersionResponseTypeDef = TypedDict(
    "CreateComponentVersionResponseTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "status": "CloudComponentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestRequestTypeDef",
    {
        "targetArn": str,
    },
)
_OptionalCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestRequestTypeDef",
    {
        "deploymentName": str,
        "components": Dict[str, "ComponentDeploymentSpecificationTypeDef"],
        "iotJobConfiguration": "DeploymentIoTJobConfigurationTypeDef",
        "deploymentPolicies": "DeploymentPoliciesTypeDef",
        "tags": Dict[str, str],
        "clientToken": str,
    },
    total=False,
)

class CreateDeploymentRequestRequestTypeDef(
    _RequiredCreateDeploymentRequestRequestTypeDef, _OptionalCreateDeploymentRequestRequestTypeDef
):
    pass

CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {
        "deploymentId": str,
        "iotJobId": str,
        "iotJobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteCoreDeviceRequestRequestTypeDef = TypedDict(
    "DeleteCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)

DeploymentComponentUpdatePolicyTypeDef = TypedDict(
    "DeploymentComponentUpdatePolicyTypeDef",
    {
        "timeoutInSeconds": int,
        "action": DeploymentComponentUpdatePolicyActionType,
    },
    total=False,
)

DeploymentConfigurationValidationPolicyTypeDef = TypedDict(
    "DeploymentConfigurationValidationPolicyTypeDef",
    {
        "timeoutInSeconds": int,
    },
    total=False,
)

DeploymentIoTJobConfigurationTypeDef = TypedDict(
    "DeploymentIoTJobConfigurationTypeDef",
    {
        "jobExecutionsRolloutConfig": "IoTJobExecutionsRolloutConfigTypeDef",
        "abortConfig": "IoTJobAbortConfigTypeDef",
        "timeoutConfig": "IoTJobTimeoutConfigTypeDef",
    },
    total=False,
)

DeploymentPoliciesTypeDef = TypedDict(
    "DeploymentPoliciesTypeDef",
    {
        "failureHandlingPolicy": DeploymentFailureHandlingPolicyType,
        "componentUpdatePolicy": "DeploymentComponentUpdatePolicyTypeDef",
        "configurationValidationPolicy": "DeploymentConfigurationValidationPolicyTypeDef",
    },
    total=False,
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "targetArn": str,
        "revisionId": str,
        "deploymentId": str,
        "deploymentName": str,
        "creationTimestamp": datetime,
        "deploymentStatus": DeploymentStatusType,
        "isLatestForTarget": bool,
    },
    total=False,
)

DescribeComponentRequestRequestTypeDef = TypedDict(
    "DescribeComponentRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DescribeComponentResponseTypeDef = TypedDict(
    "DescribeComponentResponseTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "publisher": str,
        "description": str,
        "status": "CloudComponentStatusTypeDef",
        "platforms": List["ComponentPlatformTypeDef"],
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateClientDeviceFromCoreDeviceEntryTypeDef = TypedDict(
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    {
        "thingName": str,
    },
)

DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef = TypedDict(
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    {
        "thingName": str,
        "code": str,
        "message": str,
    },
    total=False,
)

_RequiredEffectiveDeploymentTypeDef = TypedDict(
    "_RequiredEffectiveDeploymentTypeDef",
    {
        "deploymentId": str,
        "deploymentName": str,
        "targetArn": str,
        "coreDeviceExecutionStatus": EffectiveDeploymentExecutionStatusType,
        "creationTimestamp": datetime,
        "modifiedTimestamp": datetime,
    },
)
_OptionalEffectiveDeploymentTypeDef = TypedDict(
    "_OptionalEffectiveDeploymentTypeDef",
    {
        "iotJobId": str,
        "iotJobArn": str,
        "description": str,
        "reason": str,
    },
    total=False,
)

class EffectiveDeploymentTypeDef(
    _RequiredEffectiveDeploymentTypeDef, _OptionalEffectiveDeploymentTypeDef
):
    pass

_RequiredGetComponentRequestRequestTypeDef = TypedDict(
    "_RequiredGetComponentRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalGetComponentRequestRequestTypeDef = TypedDict(
    "_OptionalGetComponentRequestRequestTypeDef",
    {
        "recipeOutputFormat": RecipeOutputFormatType,
    },
    total=False,
)

class GetComponentRequestRequestTypeDef(
    _RequiredGetComponentRequestRequestTypeDef, _OptionalGetComponentRequestRequestTypeDef
):
    pass

GetComponentResponseTypeDef = TypedDict(
    "GetComponentResponseTypeDef",
    {
        "recipeOutputFormat": RecipeOutputFormatType,
        "recipe": bytes,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentVersionArtifactRequestRequestTypeDef = TypedDict(
    "GetComponentVersionArtifactRequestRequestTypeDef",
    {
        "arn": str,
        "artifactName": str,
    },
)

GetComponentVersionArtifactResponseTypeDef = TypedDict(
    "GetComponentVersionArtifactResponseTypeDef",
    {
        "preSignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDeviceRequestRequestTypeDef = TypedDict(
    "GetCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)

GetCoreDeviceResponseTypeDef = TypedDict(
    "GetCoreDeviceResponseTypeDef",
    {
        "coreDeviceThingName": str,
        "coreVersion": str,
        "platform": str,
        "architecture": str,
        "status": CoreDeviceStatusType,
        "lastStatusUpdateTimestamp": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "deploymentId": str,
    },
)

GetDeploymentResponseTypeDef = TypedDict(
    "GetDeploymentResponseTypeDef",
    {
        "targetArn": str,
        "revisionId": str,
        "deploymentId": str,
        "deploymentName": str,
        "deploymentStatus": DeploymentStatusType,
        "iotJobId": str,
        "iotJobArn": str,
        "components": Dict[str, "ComponentDeploymentSpecificationTypeDef"],
        "deploymentPolicies": "DeploymentPoliciesTypeDef",
        "iotJobConfiguration": "DeploymentIoTJobConfigurationTypeDef",
        "creationTimestamp": datetime,
        "isLatestForTarget": bool,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstalledComponentTypeDef = TypedDict(
    "InstalledComponentTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "lifecycleState": InstalledComponentLifecycleStateType,
        "lifecycleStateDetails": str,
        "isRoot": bool,
    },
    total=False,
)

IoTJobAbortConfigTypeDef = TypedDict(
    "IoTJobAbortConfigTypeDef",
    {
        "criteriaList": List["IoTJobAbortCriteriaTypeDef"],
    },
)

IoTJobAbortCriteriaTypeDef = TypedDict(
    "IoTJobAbortCriteriaTypeDef",
    {
        "failureType": IoTJobExecutionFailureTypeType,
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

IoTJobExecutionsRolloutConfigTypeDef = TypedDict(
    "IoTJobExecutionsRolloutConfigTypeDef",
    {
        "exponentialRate": "IoTJobExponentialRolloutRateTypeDef",
        "maximumPerMinute": int,
    },
    total=False,
)

IoTJobExponentialRolloutRateTypeDef = TypedDict(
    "IoTJobExponentialRolloutRateTypeDef",
    {
        "baseRatePerMinute": int,
        "incrementFactor": float,
        "rateIncreaseCriteria": "IoTJobRateIncreaseCriteriaTypeDef",
    },
)

IoTJobRateIncreaseCriteriaTypeDef = TypedDict(
    "IoTJobRateIncreaseCriteriaTypeDef",
    {
        "numberOfNotifiedThings": int,
        "numberOfSucceededThings": int,
    },
    total=False,
)

IoTJobTimeoutConfigTypeDef = TypedDict(
    "IoTJobTimeoutConfigTypeDef",
    {
        "inProgressTimeoutInMinutes": int,
    },
    total=False,
)

LambdaContainerParamsTypeDef = TypedDict(
    "LambdaContainerParamsTypeDef",
    {
        "memorySizeInKB": int,
        "mountROSysfs": bool,
        "volumes": List["LambdaVolumeMountTypeDef"],
        "devices": List["LambdaDeviceMountTypeDef"],
    },
    total=False,
)

_RequiredLambdaDeviceMountTypeDef = TypedDict(
    "_RequiredLambdaDeviceMountTypeDef",
    {
        "path": str,
    },
)
_OptionalLambdaDeviceMountTypeDef = TypedDict(
    "_OptionalLambdaDeviceMountTypeDef",
    {
        "permission": LambdaFilesystemPermissionType,
        "addGroupOwner": bool,
    },
    total=False,
)

class LambdaDeviceMountTypeDef(
    _RequiredLambdaDeviceMountTypeDef, _OptionalLambdaDeviceMountTypeDef
):
    pass

LambdaEventSourceTypeDef = TypedDict(
    "LambdaEventSourceTypeDef",
    {
        "topic": str,
        "type": LambdaEventSourceTypeType,
    },
)

LambdaExecutionParametersTypeDef = TypedDict(
    "LambdaExecutionParametersTypeDef",
    {
        "eventSources": List["LambdaEventSourceTypeDef"],
        "maxQueueSize": int,
        "maxInstancesCount": int,
        "maxIdleTimeInSeconds": int,
        "timeoutInSeconds": int,
        "statusTimeoutInSeconds": int,
        "pinned": bool,
        "inputPayloadEncodingType": LambdaInputPayloadEncodingTypeType,
        "execArgs": List[str],
        "environmentVariables": Dict[str, str],
        "linuxProcessParams": "LambdaLinuxProcessParamsTypeDef",
    },
    total=False,
)

_RequiredLambdaFunctionRecipeSourceTypeDef = TypedDict(
    "_RequiredLambdaFunctionRecipeSourceTypeDef",
    {
        "lambdaArn": str,
    },
)
_OptionalLambdaFunctionRecipeSourceTypeDef = TypedDict(
    "_OptionalLambdaFunctionRecipeSourceTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "componentPlatforms": List["ComponentPlatformTypeDef"],
        "componentDependencies": Dict[str, "ComponentDependencyRequirementTypeDef"],
        "componentLambdaParameters": "LambdaExecutionParametersTypeDef",
    },
    total=False,
)

class LambdaFunctionRecipeSourceTypeDef(
    _RequiredLambdaFunctionRecipeSourceTypeDef, _OptionalLambdaFunctionRecipeSourceTypeDef
):
    pass

LambdaLinuxProcessParamsTypeDef = TypedDict(
    "LambdaLinuxProcessParamsTypeDef",
    {
        "isolationMode": LambdaIsolationModeType,
        "containerParams": "LambdaContainerParamsTypeDef",
    },
    total=False,
)

_RequiredLambdaVolumeMountTypeDef = TypedDict(
    "_RequiredLambdaVolumeMountTypeDef",
    {
        "sourcePath": str,
        "destinationPath": str,
    },
)
_OptionalLambdaVolumeMountTypeDef = TypedDict(
    "_OptionalLambdaVolumeMountTypeDef",
    {
        "permission": LambdaFilesystemPermissionType,
        "addGroupOwner": bool,
    },
    total=False,
)

class LambdaVolumeMountTypeDef(
    _RequiredLambdaVolumeMountTypeDef, _OptionalLambdaVolumeMountTypeDef
):
    pass

_RequiredListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef(
    _RequiredListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef,
    _OptionalListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef,
):
    pass

ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef = TypedDict(
    "ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef",
    {
        "associatedClientDevices": List["AssociatedClientDeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListComponentVersionsRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalListComponentVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListComponentVersionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListComponentVersionsRequestRequestTypeDef(
    _RequiredListComponentVersionsRequestRequestTypeDef,
    _OptionalListComponentVersionsRequestRequestTypeDef,
):
    pass

ListComponentVersionsResponseTypeDef = TypedDict(
    "ListComponentVersionsResponseTypeDef",
    {
        "componentVersions": List["ComponentVersionListItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "scope": ComponentVisibilityScopeType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "components": List["ComponentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreDevicesRequestRequestTypeDef = TypedDict(
    "ListCoreDevicesRequestRequestTypeDef",
    {
        "thingGroupArn": str,
        "status": CoreDeviceStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListCoreDevicesResponseTypeDef = TypedDict(
    "ListCoreDevicesResponseTypeDef",
    {
        "coreDevices": List["CoreDeviceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeploymentsRequestRequestTypeDef = TypedDict(
    "ListDeploymentsRequestRequestTypeDef",
    {
        "targetArn": str,
        "historyFilter": DeploymentHistoryFilterType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {
        "deployments": List["DeploymentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEffectiveDeploymentsRequestRequestTypeDef = TypedDict(
    "_RequiredListEffectiveDeploymentsRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalListEffectiveDeploymentsRequestRequestTypeDef = TypedDict(
    "_OptionalListEffectiveDeploymentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListEffectiveDeploymentsRequestRequestTypeDef(
    _RequiredListEffectiveDeploymentsRequestRequestTypeDef,
    _OptionalListEffectiveDeploymentsRequestRequestTypeDef,
):
    pass

ListEffectiveDeploymentsResponseTypeDef = TypedDict(
    "ListEffectiveDeploymentsResponseTypeDef",
    {
        "effectiveDeployments": List["EffectiveDeploymentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInstalledComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredListInstalledComponentsRequestRequestTypeDef",
    {
        "coreDeviceThingName": str,
    },
)
_OptionalListInstalledComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalListInstalledComponentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListInstalledComponentsRequestRequestTypeDef(
    _RequiredListInstalledComponentsRequestRequestTypeDef,
    _OptionalListInstalledComponentsRequestRequestTypeDef,
):
    pass

ListInstalledComponentsResponseTypeDef = TypedDict(
    "ListInstalledComponentsResponseTypeDef",
    {
        "installedComponents": List["InstalledComponentTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResolveComponentCandidatesRequestRequestTypeDef = TypedDict(
    "ResolveComponentCandidatesRequestRequestTypeDef",
    {
        "platform": "ComponentPlatformTypeDef",
        "componentCandidates": List["ComponentCandidateTypeDef"],
    },
)

ResolveComponentCandidatesResponseTypeDef = TypedDict(
    "ResolveComponentCandidatesResponseTypeDef",
    {
        "resolvedComponentVersions": List["ResolvedComponentVersionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolvedComponentVersionTypeDef = TypedDict(
    "ResolvedComponentVersionTypeDef",
    {
        "arn": str,
        "componentName": str,
        "componentVersion": str,
        "recipe": bytes,
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

SystemResourceLimitsTypeDef = TypedDict(
    "SystemResourceLimitsTypeDef",
    {
        "memory": int,
        "cpus": float,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)
