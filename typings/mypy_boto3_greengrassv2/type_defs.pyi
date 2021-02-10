"""
Main interface for greengrassv2 service type definitions.

Usage::

    ```python
    from mypy_boto3_greengrassv2.type_defs import CloudComponentStatusTypeDef

    data: CloudComponentStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CloudComponentStatusTypeDef",
    "ComponentConfigurationUpdateTypeDef",
    "ComponentDependencyRequirementTypeDef",
    "ComponentDeploymentSpecificationTypeDef",
    "ComponentLatestVersionTypeDef",
    "ComponentPlatformTypeDef",
    "ComponentRunWithTypeDef",
    "ComponentTypeDef",
    "ComponentVersionListItemTypeDef",
    "CoreDeviceTypeDef",
    "DeploymentComponentUpdatePolicyTypeDef",
    "DeploymentConfigurationValidationPolicyTypeDef",
    "DeploymentIoTJobConfigurationTypeDef",
    "DeploymentPoliciesTypeDef",
    "DeploymentTypeDef",
    "EffectiveDeploymentTypeDef",
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
    "LambdaLinuxProcessParamsTypeDef",
    "LambdaVolumeMountTypeDef",
    "ResolvedComponentVersionTypeDef",
    "CancelDeploymentResponseTypeDef",
    "ComponentCandidateTypeDef",
    "CreateComponentVersionResponseTypeDef",
    "CreateDeploymentResponseTypeDef",
    "DescribeComponentResponseTypeDef",
    "GetComponentResponseTypeDef",
    "GetComponentVersionArtifactResponseTypeDef",
    "GetCoreDeviceResponseTypeDef",
    "GetDeploymentResponseTypeDef",
    "LambdaFunctionRecipeSourceTypeDef",
    "ListComponentVersionsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "ListCoreDevicesResponseTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListEffectiveDeploymentsResponseTypeDef",
    "ListInstalledComponentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResolveComponentCandidatesResponseTypeDef",
)

CloudComponentStatusTypeDef = TypedDict(
    "CloudComponentStatusTypeDef",
    {
        "componentState": Literal["REQUESTED", "INITIATED", "DEPLOYABLE", "FAILED", "DEPRECATED"],
        "message": str,
        "errors": Dict[str, str],
    },
    total=False,
)

ComponentConfigurationUpdateTypeDef = TypedDict(
    "ComponentConfigurationUpdateTypeDef", {"merge": str, "reset": List[str]}, total=False
)

ComponentDependencyRequirementTypeDef = TypedDict(
    "ComponentDependencyRequirementTypeDef",
    {"versionRequirement": str, "dependencyType": Literal["HARD", "SOFT"]},
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
    "ComponentPlatformTypeDef", {"name": str, "attributes": Dict[str, str]}, total=False
)

ComponentRunWithTypeDef = TypedDict("ComponentRunWithTypeDef", {"posixUser": str}, total=False)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {"arn": str, "componentName": str, "latestVersion": "ComponentLatestVersionTypeDef"},
    total=False,
)

ComponentVersionListItemTypeDef = TypedDict(
    "ComponentVersionListItemTypeDef",
    {"componentName": str, "componentVersion": str, "arn": str},
    total=False,
)

CoreDeviceTypeDef = TypedDict(
    "CoreDeviceTypeDef",
    {
        "coreDeviceThingName": str,
        "status": Literal["HEALTHY", "UNHEALTHY"],
        "lastStatusUpdateTimestamp": datetime,
    },
    total=False,
)

DeploymentComponentUpdatePolicyTypeDef = TypedDict(
    "DeploymentComponentUpdatePolicyTypeDef",
    {"timeoutInSeconds": int, "action": Literal["NOTIFY_COMPONENTS", "SKIP_NOTIFY_COMPONENTS"]},
    total=False,
)

DeploymentConfigurationValidationPolicyTypeDef = TypedDict(
    "DeploymentConfigurationValidationPolicyTypeDef", {"timeoutInSeconds": int}, total=False
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
        "failureHandlingPolicy": Literal["ROLLBACK", "DO_NOTHING"],
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
        "deploymentStatus": Literal["ACTIVE", "COMPLETED", "CANCELED", "FAILED", "INACTIVE"],
        "isLatestForTarget": bool,
    },
    total=False,
)

_RequiredEffectiveDeploymentTypeDef = TypedDict(
    "_RequiredEffectiveDeploymentTypeDef",
    {
        "deploymentId": str,
        "deploymentName": str,
        "targetArn": str,
        "coreDeviceExecutionStatus": Literal[
            "IN_PROGRESS", "QUEUED", "FAILED", "COMPLETED", "TIMED_OUT", "CANCELED", "REJECTED"
        ],
        "creationTimestamp": datetime,
        "modifiedTimestamp": datetime,
    },
)
_OptionalEffectiveDeploymentTypeDef = TypedDict(
    "_OptionalEffectiveDeploymentTypeDef",
    {"iotJobId": str, "iotJobArn": str, "description": str, "reason": str},
    total=False,
)


class EffectiveDeploymentTypeDef(
    _RequiredEffectiveDeploymentTypeDef, _OptionalEffectiveDeploymentTypeDef
):
    pass


InstalledComponentTypeDef = TypedDict(
    "InstalledComponentTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "lifecycleState": Literal[
            "NEW", "INSTALLED", "STARTING", "RUNNING", "STOPPING", "ERRORED", "BROKEN", "FINISHED"
        ],
        "lifecycleStateDetails": str,
        "isRoot": bool,
    },
    total=False,
)

IoTJobAbortConfigTypeDef = TypedDict(
    "IoTJobAbortConfigTypeDef", {"criteriaList": List["IoTJobAbortCriteriaTypeDef"]}
)

IoTJobAbortCriteriaTypeDef = TypedDict(
    "IoTJobAbortCriteriaTypeDef",
    {
        "failureType": Literal["FAILED", "REJECTED", "TIMED_OUT", "ALL"],
        "action": Literal["CANCEL"],
        "thresholdPercentage": float,
        "minNumberOfExecutedThings": int,
    },
)

IoTJobExecutionsRolloutConfigTypeDef = TypedDict(
    "IoTJobExecutionsRolloutConfigTypeDef",
    {"exponentialRate": "IoTJobExponentialRolloutRateTypeDef", "maximumPerMinute": int},
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
    {"numberOfNotifiedThings": int, "numberOfSucceededThings": int},
    total=False,
)

IoTJobTimeoutConfigTypeDef = TypedDict(
    "IoTJobTimeoutConfigTypeDef", {"inProgressTimeoutInMinutes": int}, total=False
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

_RequiredLambdaDeviceMountTypeDef = TypedDict("_RequiredLambdaDeviceMountTypeDef", {"path": str})
_OptionalLambdaDeviceMountTypeDef = TypedDict(
    "_OptionalLambdaDeviceMountTypeDef",
    {"permission": Literal["ro", "rw"], "addGroupOwner": bool},
    total=False,
)


class LambdaDeviceMountTypeDef(
    _RequiredLambdaDeviceMountTypeDef, _OptionalLambdaDeviceMountTypeDef
):
    pass


LambdaEventSourceTypeDef = TypedDict(
    "LambdaEventSourceTypeDef", {"topic": str, "type": Literal["PUB_SUB", "IOT_CORE"]}
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
        "inputPayloadEncodingType": Literal["json", "binary"],
        "execArgs": List[str],
        "environmentVariables": Dict[str, str],
        "linuxProcessParams": "LambdaLinuxProcessParamsTypeDef",
    },
    total=False,
)

LambdaLinuxProcessParamsTypeDef = TypedDict(
    "LambdaLinuxProcessParamsTypeDef",
    {
        "isolationMode": Literal["GreengrassContainer", "NoContainer"],
        "containerParams": "LambdaContainerParamsTypeDef",
    },
    total=False,
)

_RequiredLambdaVolumeMountTypeDef = TypedDict(
    "_RequiredLambdaVolumeMountTypeDef", {"sourcePath": str, "destinationPath": str}
)
_OptionalLambdaVolumeMountTypeDef = TypedDict(
    "_OptionalLambdaVolumeMountTypeDef",
    {"permission": Literal["ro", "rw"], "addGroupOwner": bool},
    total=False,
)


class LambdaVolumeMountTypeDef(
    _RequiredLambdaVolumeMountTypeDef, _OptionalLambdaVolumeMountTypeDef
):
    pass


ResolvedComponentVersionTypeDef = TypedDict(
    "ResolvedComponentVersionTypeDef",
    {"arn": str, "componentName": str, "componentVersion": str, "recipe": Union[bytes, IO[bytes]]},
    total=False,
)

CancelDeploymentResponseTypeDef = TypedDict(
    "CancelDeploymentResponseTypeDef", {"message": str}, total=False
)

ComponentCandidateTypeDef = TypedDict(
    "ComponentCandidateTypeDef",
    {"componentName": str, "componentVersion": str, "versionRequirements": Dict[str, str]},
    total=False,
)

_RequiredCreateComponentVersionResponseTypeDef = TypedDict(
    "_RequiredCreateComponentVersionResponseTypeDef",
    {
        "componentName": str,
        "componentVersion": str,
        "creationTimestamp": datetime,
        "status": "CloudComponentStatusTypeDef",
    },
)
_OptionalCreateComponentVersionResponseTypeDef = TypedDict(
    "_OptionalCreateComponentVersionResponseTypeDef", {"arn": str}, total=False
)


class CreateComponentVersionResponseTypeDef(
    _RequiredCreateComponentVersionResponseTypeDef, _OptionalCreateComponentVersionResponseTypeDef
):
    pass


CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef",
    {"deploymentId": str, "iotJobId": str, "iotJobArn": str},
    total=False,
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
    },
    total=False,
)

_RequiredGetComponentResponseTypeDef = TypedDict(
    "_RequiredGetComponentResponseTypeDef",
    {"recipeOutputFormat": Literal["JSON", "YAML"], "recipe": Union[bytes, IO[bytes]]},
)
_OptionalGetComponentResponseTypeDef = TypedDict(
    "_OptionalGetComponentResponseTypeDef", {"tags": Dict[str, str]}, total=False
)


class GetComponentResponseTypeDef(
    _RequiredGetComponentResponseTypeDef, _OptionalGetComponentResponseTypeDef
):
    pass


GetComponentVersionArtifactResponseTypeDef = TypedDict(
    "GetComponentVersionArtifactResponseTypeDef", {"preSignedUrl": str}
)

GetCoreDeviceResponseTypeDef = TypedDict(
    "GetCoreDeviceResponseTypeDef",
    {
        "coreDeviceThingName": str,
        "coreVersion": str,
        "platform": str,
        "architecture": str,
        "status": Literal["HEALTHY", "UNHEALTHY"],
        "lastStatusUpdateTimestamp": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

GetDeploymentResponseTypeDef = TypedDict(
    "GetDeploymentResponseTypeDef",
    {
        "targetArn": str,
        "revisionId": str,
        "deploymentId": str,
        "deploymentName": str,
        "deploymentStatus": Literal["ACTIVE", "COMPLETED", "CANCELED", "FAILED", "INACTIVE"],
        "iotJobId": str,
        "iotJobArn": str,
        "components": Dict[str, "ComponentDeploymentSpecificationTypeDef"],
        "deploymentPolicies": "DeploymentPoliciesTypeDef",
        "iotJobConfiguration": "DeploymentIoTJobConfigurationTypeDef",
        "creationTimestamp": datetime,
        "isLatestForTarget": bool,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredLambdaFunctionRecipeSourceTypeDef = TypedDict(
    "_RequiredLambdaFunctionRecipeSourceTypeDef", {"lambdaArn": str}
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


ListComponentVersionsResponseTypeDef = TypedDict(
    "ListComponentVersionsResponseTypeDef",
    {"componentVersions": List["ComponentVersionListItemTypeDef"], "nextToken": str},
    total=False,
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {"components": List["ComponentTypeDef"], "nextToken": str},
    total=False,
)

ListCoreDevicesResponseTypeDef = TypedDict(
    "ListCoreDevicesResponseTypeDef",
    {"coreDevices": List["CoreDeviceTypeDef"], "nextToken": str},
    total=False,
)

ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {"deployments": List["DeploymentTypeDef"], "nextToken": str},
    total=False,
)

ListEffectiveDeploymentsResponseTypeDef = TypedDict(
    "ListEffectiveDeploymentsResponseTypeDef",
    {"effectiveDeployments": List["EffectiveDeploymentTypeDef"], "nextToken": str},
    total=False,
)

ListInstalledComponentsResponseTypeDef = TypedDict(
    "ListInstalledComponentsResponseTypeDef",
    {"installedComponents": List["InstalledComponentTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ResolveComponentCandidatesResponseTypeDef = TypedDict(
    "ResolveComponentCandidatesResponseTypeDef",
    {"resolvedComponentVersions": List["ResolvedComponentVersionTypeDef"]},
    total=False,
)
