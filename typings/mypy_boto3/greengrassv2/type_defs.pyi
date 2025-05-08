"""
Type annotations for greengrassv2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_greengrassv2.type_defs import AssociateClientDeviceWithCoreDeviceEntryTypeDef

    data: AssociateClientDeviceWithCoreDeviceEntryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

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
    InstalledComponentTopologyFilterType,
    IotEndpointTypeType,
    IoTJobExecutionFailureTypeType,
    LambdaEventSourceTypeType,
    LambdaFilesystemPermissionType,
    LambdaInputPayloadEncodingTypeType,
    LambdaIsolationModeType,
    RecipeOutputFormatType,
    S3EndpointTypeType,
    VendorGuidanceType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssociateClientDeviceWithCoreDeviceEntryTypeDef",
    "AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef",
    "AssociateServiceRoleToAccountRequestTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "AssociatedClientDeviceTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceRequestTypeDef",
    "BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef",
    "BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef",
    "BlobTypeDef",
    "CancelDeploymentRequestTypeDef",
    "CancelDeploymentResponseTypeDef",
    "CloudComponentStatusTypeDef",
    "ComponentCandidateTypeDef",
    "ComponentConfigurationUpdateOutputTypeDef",
    "ComponentConfigurationUpdateTypeDef",
    "ComponentConfigurationUpdateUnionTypeDef",
    "ComponentDependencyRequirementTypeDef",
    "ComponentDeploymentSpecificationOutputTypeDef",
    "ComponentDeploymentSpecificationTypeDef",
    "ComponentDeploymentSpecificationUnionTypeDef",
    "ComponentLatestVersionTypeDef",
    "ComponentPlatformOutputTypeDef",
    "ComponentPlatformTypeDef",
    "ComponentPlatformUnionTypeDef",
    "ComponentRunWithTypeDef",
    "ComponentTypeDef",
    "ComponentVersionListItemTypeDef",
    "ConnectivityInfoTypeDef",
    "CoreDeviceTypeDef",
    "CreateComponentVersionRequestTypeDef",
    "CreateComponentVersionResponseTypeDef",
    "CreateDeploymentRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "DeleteComponentRequestTypeDef",
    "DeleteCoreDeviceRequestTypeDef",
    "DeleteDeploymentRequestTypeDef",
    "DeploymentComponentUpdatePolicyTypeDef",
    "DeploymentConfigurationValidationPolicyTypeDef",
    "DeploymentIoTJobConfigurationOutputTypeDef",
    "DeploymentIoTJobConfigurationTypeDef",
    "DeploymentIoTJobConfigurationUnionTypeDef",
    "DeploymentPoliciesTypeDef",
    "DeploymentTypeDef",
    "DescribeComponentRequestTypeDef",
    "DescribeComponentResponseTypeDef",
    "DisassociateClientDeviceFromCoreDeviceEntryTypeDef",
    "DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "EffectiveDeploymentStatusDetailsTypeDef",
    "EffectiveDeploymentTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetComponentRequestTypeDef",
    "GetComponentResponseTypeDef",
    "GetComponentVersionArtifactRequestTypeDef",
    "GetComponentVersionArtifactResponseTypeDef",
    "GetConnectivityInfoRequestTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "GetCoreDeviceRequestTypeDef",
    "GetCoreDeviceResponseTypeDef",
    "GetDeploymentRequestTypeDef",
    "GetDeploymentResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "InstalledComponentTypeDef",
    "IoTJobAbortConfigOutputTypeDef",
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
    "ListClientDevicesAssociatedWithCoreDeviceRequestPaginateTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceRequestTypeDef",
    "ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef",
    "ListComponentVersionsRequestPaginateTypeDef",
    "ListComponentVersionsRequestTypeDef",
    "ListComponentVersionsResponseTypeDef",
    "ListComponentsRequestPaginateTypeDef",
    "ListComponentsRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListCoreDevicesRequestPaginateTypeDef",
    "ListCoreDevicesRequestTypeDef",
    "ListCoreDevicesResponseTypeDef",
    "ListDeploymentsRequestPaginateTypeDef",
    "ListDeploymentsRequestTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListEffectiveDeploymentsRequestPaginateTypeDef",
    "ListEffectiveDeploymentsRequestTypeDef",
    "ListEffectiveDeploymentsResponseTypeDef",
    "ListInstalledComponentsRequestPaginateTypeDef",
    "ListInstalledComponentsRequestTypeDef",
    "ListInstalledComponentsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResolveComponentCandidatesRequestTypeDef",
    "ResolveComponentCandidatesResponseTypeDef",
    "ResolvedComponentVersionTypeDef",
    "ResponseMetadataTypeDef",
    "SystemResourceLimitsTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateConnectivityInfoRequestTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
)

class AssociateClientDeviceWithCoreDeviceEntryTypeDef(TypedDict):
    thingName: str

class AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef(TypedDict):
    thingName: NotRequired[str]
    code: NotRequired[str]
    message: NotRequired[str]

class AssociateServiceRoleToAccountRequestTypeDef(TypedDict):
    roleArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociatedClientDeviceTypeDef(TypedDict):
    thingName: NotRequired[str]
    associationTimestamp: NotRequired[datetime]

class DisassociateClientDeviceFromCoreDeviceEntryTypeDef(TypedDict):
    thingName: str

class DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef(TypedDict):
    thingName: NotRequired[str]
    code: NotRequired[str]
    message: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class CancelDeploymentRequestTypeDef(TypedDict):
    deploymentId: str

class CloudComponentStatusTypeDef(TypedDict):
    componentState: NotRequired[CloudComponentStateType]
    message: NotRequired[str]
    errors: NotRequired[Dict[str, str]]
    vendorGuidance: NotRequired[VendorGuidanceType]
    vendorGuidanceMessage: NotRequired[str]

class ComponentCandidateTypeDef(TypedDict):
    componentName: NotRequired[str]
    componentVersion: NotRequired[str]
    versionRequirements: NotRequired[Mapping[str, str]]

class ComponentConfigurationUpdateOutputTypeDef(TypedDict):
    merge: NotRequired[str]
    reset: NotRequired[List[str]]

class ComponentConfigurationUpdateTypeDef(TypedDict):
    merge: NotRequired[str]
    reset: NotRequired[Sequence[str]]

class ComponentDependencyRequirementTypeDef(TypedDict):
    versionRequirement: NotRequired[str]
    dependencyType: NotRequired[ComponentDependencyTypeType]

class ComponentPlatformOutputTypeDef(TypedDict):
    name: NotRequired[str]
    attributes: NotRequired[Dict[str, str]]

class ComponentPlatformTypeDef(TypedDict):
    name: NotRequired[str]
    attributes: NotRequired[Mapping[str, str]]

class SystemResourceLimitsTypeDef(TypedDict):
    memory: NotRequired[int]
    cpus: NotRequired[float]

class ComponentVersionListItemTypeDef(TypedDict):
    componentName: NotRequired[str]
    componentVersion: NotRequired[str]
    arn: NotRequired[str]

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "id": NotRequired[str],
        "hostAddress": NotRequired[str],
        "portNumber": NotRequired[int],
        "metadata": NotRequired[str],
    },
)

class CoreDeviceTypeDef(TypedDict):
    coreDeviceThingName: NotRequired[str]
    status: NotRequired[CoreDeviceStatusType]
    lastStatusUpdateTimestamp: NotRequired[datetime]
    platform: NotRequired[str]
    architecture: NotRequired[str]
    runtime: NotRequired[str]

class DeleteComponentRequestTypeDef(TypedDict):
    arn: str

class DeleteCoreDeviceRequestTypeDef(TypedDict):
    coreDeviceThingName: str

class DeleteDeploymentRequestTypeDef(TypedDict):
    deploymentId: str

class DeploymentComponentUpdatePolicyTypeDef(TypedDict):
    timeoutInSeconds: NotRequired[int]
    action: NotRequired[DeploymentComponentUpdatePolicyActionType]

class DeploymentConfigurationValidationPolicyTypeDef(TypedDict):
    timeoutInSeconds: NotRequired[int]

class IoTJobTimeoutConfigTypeDef(TypedDict):
    inProgressTimeoutInMinutes: NotRequired[int]

class DeploymentTypeDef(TypedDict):
    targetArn: NotRequired[str]
    revisionId: NotRequired[str]
    deploymentId: NotRequired[str]
    deploymentName: NotRequired[str]
    creationTimestamp: NotRequired[datetime]
    deploymentStatus: NotRequired[DeploymentStatusType]
    isLatestForTarget: NotRequired[bool]
    parentTargetArn: NotRequired[str]

class DescribeComponentRequestTypeDef(TypedDict):
    arn: str

class EffectiveDeploymentStatusDetailsTypeDef(TypedDict):
    errorStack: NotRequired[List[str]]
    errorTypes: NotRequired[List[str]]

class GetComponentRequestTypeDef(TypedDict):
    arn: str
    recipeOutputFormat: NotRequired[RecipeOutputFormatType]

class GetComponentVersionArtifactRequestTypeDef(TypedDict):
    arn: str
    artifactName: str
    s3EndpointType: NotRequired[S3EndpointTypeType]
    iotEndpointType: NotRequired[IotEndpointTypeType]

class GetConnectivityInfoRequestTypeDef(TypedDict):
    thingName: str

class GetCoreDeviceRequestTypeDef(TypedDict):
    coreDeviceThingName: str

class GetDeploymentRequestTypeDef(TypedDict):
    deploymentId: str

class InstalledComponentTypeDef(TypedDict):
    componentName: NotRequired[str]
    componentVersion: NotRequired[str]
    lifecycleState: NotRequired[InstalledComponentLifecycleStateType]
    lifecycleStateDetails: NotRequired[str]
    isRoot: NotRequired[bool]
    lastStatusChangeTimestamp: NotRequired[datetime]
    lastReportedTimestamp: NotRequired[datetime]
    lastInstallationSource: NotRequired[str]
    lifecycleStatusCodes: NotRequired[List[str]]

class IoTJobAbortCriteriaTypeDef(TypedDict):
    failureType: IoTJobExecutionFailureTypeType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int

class IoTJobRateIncreaseCriteriaTypeDef(TypedDict):
    numberOfNotifiedThings: NotRequired[int]
    numberOfSucceededThings: NotRequired[int]

class LambdaDeviceMountTypeDef(TypedDict):
    path: str
    permission: NotRequired[LambdaFilesystemPermissionType]
    addGroupOwner: NotRequired[bool]

class LambdaVolumeMountTypeDef(TypedDict):
    sourcePath: str
    destinationPath: str
    permission: NotRequired[LambdaFilesystemPermissionType]
    addGroupOwner: NotRequired[bool]

LambdaEventSourceTypeDef = TypedDict(
    "LambdaEventSourceTypeDef",
    {
        "topic": str,
        "type": LambdaEventSourceTypeType,
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListClientDevicesAssociatedWithCoreDeviceRequestTypeDef(TypedDict):
    coreDeviceThingName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListComponentVersionsRequestTypeDef(TypedDict):
    arn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListComponentsRequestTypeDef(TypedDict):
    scope: NotRequired[ComponentVisibilityScopeType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListCoreDevicesRequestTypeDef(TypedDict):
    thingGroupArn: NotRequired[str]
    status: NotRequired[CoreDeviceStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    runtime: NotRequired[str]

class ListDeploymentsRequestTypeDef(TypedDict):
    targetArn: NotRequired[str]
    historyFilter: NotRequired[DeploymentHistoryFilterType]
    parentTargetArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEffectiveDeploymentsRequestTypeDef(TypedDict):
    coreDeviceThingName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListInstalledComponentsRequestTypeDef(TypedDict):
    coreDeviceThingName: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    topologyFilter: NotRequired[InstalledComponentTopologyFilterType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ResolvedComponentVersionTypeDef(TypedDict):
    arn: NotRequired[str]
    componentName: NotRequired[str]
    componentVersion: NotRequired[str]
    recipe: NotRequired[bytes]
    vendorGuidance: NotRequired[VendorGuidanceType]
    message: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchAssociateClientDeviceWithCoreDeviceRequestTypeDef(TypedDict):
    coreDeviceThingName: str
    entries: NotRequired[Sequence[AssociateClientDeviceWithCoreDeviceEntryTypeDef]]

class AssociateServiceRoleToAccountResponseTypeDef(TypedDict):
    associatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef(TypedDict):
    errorEntries: List[AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelDeploymentResponseTypeDef(TypedDict):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(TypedDict):
    deploymentId: str
    iotJobId: str
    iotJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateServiceRoleFromAccountResponseTypeDef(TypedDict):
    disassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentResponseTypeDef(TypedDict):
    recipeOutputFormat: RecipeOutputFormatType
    recipe: bytes
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentVersionArtifactResponseTypeDef(TypedDict):
    preSignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreDeviceResponseTypeDef(TypedDict):
    coreDeviceThingName: str
    coreVersion: str
    platform: str
    architecture: str
    runtime: str
    status: CoreDeviceStatusType
    lastStatusUpdateTimestamp: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceRoleForAccountResponseTypeDef(TypedDict):
    associatedAt: str
    roleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoResponseTypeDef(TypedDict):
    version: str
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef(TypedDict):
    associatedClientDevices: List[AssociatedClientDeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchDisassociateClientDeviceFromCoreDeviceRequestTypeDef(TypedDict):
    coreDeviceThingName: str
    entries: NotRequired[Sequence[DisassociateClientDeviceFromCoreDeviceEntryTypeDef]]

class BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef(TypedDict):
    errorEntries: List[DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentVersionResponseTypeDef(TypedDict):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    status: CloudComponentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ComponentConfigurationUpdateUnionTypeDef = Union[
    ComponentConfigurationUpdateTypeDef, ComponentConfigurationUpdateOutputTypeDef
]

class ComponentLatestVersionTypeDef(TypedDict):
    arn: NotRequired[str]
    componentVersion: NotRequired[str]
    creationTimestamp: NotRequired[datetime]
    description: NotRequired[str]
    publisher: NotRequired[str]
    platforms: NotRequired[List[ComponentPlatformOutputTypeDef]]

class DescribeComponentResponseTypeDef(TypedDict):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    publisher: str
    description: str
    status: CloudComponentStatusTypeDef
    platforms: List[ComponentPlatformOutputTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

ComponentPlatformUnionTypeDef = Union[ComponentPlatformTypeDef, ComponentPlatformOutputTypeDef]

class ComponentRunWithTypeDef(TypedDict):
    posixUser: NotRequired[str]
    systemResourceLimits: NotRequired[SystemResourceLimitsTypeDef]
    windowsUser: NotRequired[str]

class ListComponentVersionsResponseTypeDef(TypedDict):
    componentVersions: List[ComponentVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetConnectivityInfoResponseTypeDef(TypedDict):
    connectivityInfo: List[ConnectivityInfoTypeDef]
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoRequestTypeDef(TypedDict):
    thingName: str
    connectivityInfo: Sequence[ConnectivityInfoTypeDef]

class ListCoreDevicesResponseTypeDef(TypedDict):
    coreDevices: List[CoreDeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DeploymentPoliciesTypeDef(TypedDict):
    failureHandlingPolicy: NotRequired[DeploymentFailureHandlingPolicyType]
    componentUpdatePolicy: NotRequired[DeploymentComponentUpdatePolicyTypeDef]
    configurationValidationPolicy: NotRequired[DeploymentConfigurationValidationPolicyTypeDef]

class ListDeploymentsResponseTypeDef(TypedDict):
    deployments: List[DeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class EffectiveDeploymentTypeDef(TypedDict):
    deploymentId: str
    deploymentName: str
    targetArn: str
    coreDeviceExecutionStatus: EffectiveDeploymentExecutionStatusType
    creationTimestamp: datetime
    modifiedTimestamp: datetime
    iotJobId: NotRequired[str]
    iotJobArn: NotRequired[str]
    description: NotRequired[str]
    reason: NotRequired[str]
    statusDetails: NotRequired[EffectiveDeploymentStatusDetailsTypeDef]

class ListInstalledComponentsResponseTypeDef(TypedDict):
    installedComponents: List[InstalledComponentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class IoTJobAbortConfigOutputTypeDef(TypedDict):
    criteriaList: List[IoTJobAbortCriteriaTypeDef]

class IoTJobAbortConfigTypeDef(TypedDict):
    criteriaList: Sequence[IoTJobAbortCriteriaTypeDef]

class IoTJobExponentialRolloutRateTypeDef(TypedDict):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: IoTJobRateIncreaseCriteriaTypeDef

class LambdaContainerParamsTypeDef(TypedDict):
    memorySizeInKB: NotRequired[int]
    mountROSysfs: NotRequired[bool]
    volumes: NotRequired[Sequence[LambdaVolumeMountTypeDef]]
    devices: NotRequired[Sequence[LambdaDeviceMountTypeDef]]

class ListClientDevicesAssociatedWithCoreDeviceRequestPaginateTypeDef(TypedDict):
    coreDeviceThingName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListComponentVersionsRequestPaginateTypeDef(TypedDict):
    arn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListComponentsRequestPaginateTypeDef(TypedDict):
    scope: NotRequired[ComponentVisibilityScopeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCoreDevicesRequestPaginateTypeDef(TypedDict):
    thingGroupArn: NotRequired[str]
    status: NotRequired[CoreDeviceStatusType]
    runtime: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDeploymentsRequestPaginateTypeDef(TypedDict):
    targetArn: NotRequired[str]
    historyFilter: NotRequired[DeploymentHistoryFilterType]
    parentTargetArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEffectiveDeploymentsRequestPaginateTypeDef(TypedDict):
    coreDeviceThingName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInstalledComponentsRequestPaginateTypeDef(TypedDict):
    coreDeviceThingName: str
    topologyFilter: NotRequired[InstalledComponentTopologyFilterType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ResolveComponentCandidatesResponseTypeDef(TypedDict):
    resolvedComponentVersions: List[ResolvedComponentVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentTypeDef(TypedDict):
    arn: NotRequired[str]
    componentName: NotRequired[str]
    latestVersion: NotRequired[ComponentLatestVersionTypeDef]

class ResolveComponentCandidatesRequestTypeDef(TypedDict):
    platform: NotRequired[ComponentPlatformUnionTypeDef]
    componentCandidates: NotRequired[Sequence[ComponentCandidateTypeDef]]

class ComponentDeploymentSpecificationOutputTypeDef(TypedDict):
    componentVersion: str
    configurationUpdate: NotRequired[ComponentConfigurationUpdateOutputTypeDef]
    runWith: NotRequired[ComponentRunWithTypeDef]

class ComponentDeploymentSpecificationTypeDef(TypedDict):
    componentVersion: str
    configurationUpdate: NotRequired[ComponentConfigurationUpdateUnionTypeDef]
    runWith: NotRequired[ComponentRunWithTypeDef]

class ListEffectiveDeploymentsResponseTypeDef(TypedDict):
    effectiveDeployments: List[EffectiveDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class IoTJobExecutionsRolloutConfigTypeDef(TypedDict):
    exponentialRate: NotRequired[IoTJobExponentialRolloutRateTypeDef]
    maximumPerMinute: NotRequired[int]

class LambdaLinuxProcessParamsTypeDef(TypedDict):
    isolationMode: NotRequired[LambdaIsolationModeType]
    containerParams: NotRequired[LambdaContainerParamsTypeDef]

class ListComponentsResponseTypeDef(TypedDict):
    components: List[ComponentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ComponentDeploymentSpecificationUnionTypeDef = Union[
    ComponentDeploymentSpecificationTypeDef, ComponentDeploymentSpecificationOutputTypeDef
]

class DeploymentIoTJobConfigurationOutputTypeDef(TypedDict):
    jobExecutionsRolloutConfig: NotRequired[IoTJobExecutionsRolloutConfigTypeDef]
    abortConfig: NotRequired[IoTJobAbortConfigOutputTypeDef]
    timeoutConfig: NotRequired[IoTJobTimeoutConfigTypeDef]

class DeploymentIoTJobConfigurationTypeDef(TypedDict):
    jobExecutionsRolloutConfig: NotRequired[IoTJobExecutionsRolloutConfigTypeDef]
    abortConfig: NotRequired[IoTJobAbortConfigTypeDef]
    timeoutConfig: NotRequired[IoTJobTimeoutConfigTypeDef]

class LambdaExecutionParametersTypeDef(TypedDict):
    eventSources: NotRequired[Sequence[LambdaEventSourceTypeDef]]
    maxQueueSize: NotRequired[int]
    maxInstancesCount: NotRequired[int]
    maxIdleTimeInSeconds: NotRequired[int]
    timeoutInSeconds: NotRequired[int]
    statusTimeoutInSeconds: NotRequired[int]
    pinned: NotRequired[bool]
    inputPayloadEncodingType: NotRequired[LambdaInputPayloadEncodingTypeType]
    execArgs: NotRequired[Sequence[str]]
    environmentVariables: NotRequired[Mapping[str, str]]
    linuxProcessParams: NotRequired[LambdaLinuxProcessParamsTypeDef]

class GetDeploymentResponseTypeDef(TypedDict):
    targetArn: str
    revisionId: str
    deploymentId: str
    deploymentName: str
    deploymentStatus: DeploymentStatusType
    iotJobId: str
    iotJobArn: str
    components: Dict[str, ComponentDeploymentSpecificationOutputTypeDef]
    deploymentPolicies: DeploymentPoliciesTypeDef
    iotJobConfiguration: DeploymentIoTJobConfigurationOutputTypeDef
    creationTimestamp: datetime
    isLatestForTarget: bool
    parentTargetArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

DeploymentIoTJobConfigurationUnionTypeDef = Union[
    DeploymentIoTJobConfigurationTypeDef, DeploymentIoTJobConfigurationOutputTypeDef
]

class LambdaFunctionRecipeSourceTypeDef(TypedDict):
    lambdaArn: str
    componentName: NotRequired[str]
    componentVersion: NotRequired[str]
    componentPlatforms: NotRequired[Sequence[ComponentPlatformUnionTypeDef]]
    componentDependencies: NotRequired[Mapping[str, ComponentDependencyRequirementTypeDef]]
    componentLambdaParameters: NotRequired[LambdaExecutionParametersTypeDef]

class CreateDeploymentRequestTypeDef(TypedDict):
    targetArn: str
    deploymentName: NotRequired[str]
    components: NotRequired[Mapping[str, ComponentDeploymentSpecificationUnionTypeDef]]
    iotJobConfiguration: NotRequired[DeploymentIoTJobConfigurationUnionTypeDef]
    deploymentPolicies: NotRequired[DeploymentPoliciesTypeDef]
    parentTargetArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]

class CreateComponentVersionRequestTypeDef(TypedDict):
    inlineRecipe: NotRequired[BlobTypeDef]
    lambdaFunction: NotRequired[LambdaFunctionRecipeSourceTypeDef]
    tags: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]
