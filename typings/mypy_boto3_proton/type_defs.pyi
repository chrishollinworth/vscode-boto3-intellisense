"""
Type annotations for proton service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_proton/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_proton.type_defs import AcceptEnvironmentAccountConnectionInputTypeDef

    data: AcceptEnvironmentAccountConnectionInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    BlockerStatusType,
    ComponentDeploymentUpdateTypeType,
    DeploymentStatusType,
    DeploymentTargetResourceTypeType,
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    ListServiceInstancesFilterByType,
    ListServiceInstancesSortByType,
    ProvisionedResourceEngineType,
    RepositoryProviderType,
    RepositorySyncStatusType,
    ResourceDeploymentStatusType,
    ResourceSyncStatusType,
    ServiceStatusType,
    SortOrderType,
    SyncTypeType,
    TemplateTypeType,
    TemplateVersionStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AcceptEnvironmentAccountConnectionInputTypeDef",
    "AcceptEnvironmentAccountConnectionOutputTypeDef",
    "AccountSettingsTypeDef",
    "CancelComponentDeploymentInputTypeDef",
    "CancelComponentDeploymentOutputTypeDef",
    "CancelEnvironmentDeploymentInputTypeDef",
    "CancelEnvironmentDeploymentOutputTypeDef",
    "CancelServiceInstanceDeploymentInputTypeDef",
    "CancelServiceInstanceDeploymentOutputTypeDef",
    "CancelServicePipelineDeploymentInputTypeDef",
    "CancelServicePipelineDeploymentOutputTypeDef",
    "CompatibleEnvironmentTemplateInputTypeDef",
    "CompatibleEnvironmentTemplateTypeDef",
    "ComponentStateTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "CountsSummaryTypeDef",
    "CreateComponentInputTypeDef",
    "CreateComponentOutputTypeDef",
    "CreateEnvironmentAccountConnectionInputTypeDef",
    "CreateEnvironmentAccountConnectionOutputTypeDef",
    "CreateEnvironmentInputTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateEnvironmentTemplateInputTypeDef",
    "CreateEnvironmentTemplateOutputTypeDef",
    "CreateEnvironmentTemplateVersionInputTypeDef",
    "CreateEnvironmentTemplateVersionOutputTypeDef",
    "CreateRepositoryInputTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateServiceInputTypeDef",
    "CreateServiceInstanceInputTypeDef",
    "CreateServiceInstanceOutputTypeDef",
    "CreateServiceOutputTypeDef",
    "CreateServiceSyncConfigInputTypeDef",
    "CreateServiceSyncConfigOutputTypeDef",
    "CreateServiceTemplateInputTypeDef",
    "CreateServiceTemplateOutputTypeDef",
    "CreateServiceTemplateVersionInputTypeDef",
    "CreateServiceTemplateVersionOutputTypeDef",
    "CreateTemplateSyncConfigInputTypeDef",
    "CreateTemplateSyncConfigOutputTypeDef",
    "DeleteComponentInputTypeDef",
    "DeleteComponentOutputTypeDef",
    "DeleteDeploymentInputTypeDef",
    "DeleteDeploymentOutputTypeDef",
    "DeleteEnvironmentAccountConnectionInputTypeDef",
    "DeleteEnvironmentAccountConnectionOutputTypeDef",
    "DeleteEnvironmentInputTypeDef",
    "DeleteEnvironmentOutputTypeDef",
    "DeleteEnvironmentTemplateInputTypeDef",
    "DeleteEnvironmentTemplateOutputTypeDef",
    "DeleteEnvironmentTemplateVersionInputTypeDef",
    "DeleteEnvironmentTemplateVersionOutputTypeDef",
    "DeleteRepositoryInputTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DeleteServiceInputTypeDef",
    "DeleteServiceOutputTypeDef",
    "DeleteServiceSyncConfigInputTypeDef",
    "DeleteServiceSyncConfigOutputTypeDef",
    "DeleteServiceTemplateInputTypeDef",
    "DeleteServiceTemplateOutputTypeDef",
    "DeleteServiceTemplateVersionInputTypeDef",
    "DeleteServiceTemplateVersionOutputTypeDef",
    "DeleteTemplateSyncConfigInputTypeDef",
    "DeleteTemplateSyncConfigOutputTypeDef",
    "DeploymentStateTypeDef",
    "DeploymentSummaryTypeDef",
    "DeploymentTypeDef",
    "EnvironmentAccountConnectionSummaryTypeDef",
    "EnvironmentAccountConnectionTypeDef",
    "EnvironmentStateTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentTemplateFilterTypeDef",
    "EnvironmentTemplateSummaryTypeDef",
    "EnvironmentTemplateTypeDef",
    "EnvironmentTemplateVersionSummaryTypeDef",
    "EnvironmentTemplateVersionTypeDef",
    "EnvironmentTypeDef",
    "GetAccountSettingsOutputTypeDef",
    "GetComponentInputTypeDef",
    "GetComponentInputWaitExtraTypeDef",
    "GetComponentInputWaitTypeDef",
    "GetComponentOutputTypeDef",
    "GetDeploymentInputTypeDef",
    "GetDeploymentOutputTypeDef",
    "GetEnvironmentAccountConnectionInputTypeDef",
    "GetEnvironmentAccountConnectionOutputTypeDef",
    "GetEnvironmentInputTypeDef",
    "GetEnvironmentInputWaitTypeDef",
    "GetEnvironmentOutputTypeDef",
    "GetEnvironmentTemplateInputTypeDef",
    "GetEnvironmentTemplateOutputTypeDef",
    "GetEnvironmentTemplateVersionInputTypeDef",
    "GetEnvironmentTemplateVersionInputWaitTypeDef",
    "GetEnvironmentTemplateVersionOutputTypeDef",
    "GetRepositoryInputTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositorySyncStatusInputTypeDef",
    "GetRepositorySyncStatusOutputTypeDef",
    "GetResourcesSummaryOutputTypeDef",
    "GetServiceInputTypeDef",
    "GetServiceInputWaitExtraExtraExtraTypeDef",
    "GetServiceInputWaitExtraExtraTypeDef",
    "GetServiceInputWaitExtraTypeDef",
    "GetServiceInputWaitTypeDef",
    "GetServiceInstanceInputTypeDef",
    "GetServiceInstanceInputWaitTypeDef",
    "GetServiceInstanceOutputTypeDef",
    "GetServiceInstanceSyncStatusInputTypeDef",
    "GetServiceInstanceSyncStatusOutputTypeDef",
    "GetServiceOutputTypeDef",
    "GetServiceSyncBlockerSummaryInputTypeDef",
    "GetServiceSyncBlockerSummaryOutputTypeDef",
    "GetServiceSyncConfigInputTypeDef",
    "GetServiceSyncConfigOutputTypeDef",
    "GetServiceTemplateInputTypeDef",
    "GetServiceTemplateOutputTypeDef",
    "GetServiceTemplateVersionInputTypeDef",
    "GetServiceTemplateVersionInputWaitTypeDef",
    "GetServiceTemplateVersionOutputTypeDef",
    "GetTemplateSyncConfigInputTypeDef",
    "GetTemplateSyncConfigOutputTypeDef",
    "GetTemplateSyncStatusInputTypeDef",
    "GetTemplateSyncStatusOutputTypeDef",
    "ListComponentOutputsInputPaginateTypeDef",
    "ListComponentOutputsInputTypeDef",
    "ListComponentOutputsOutputTypeDef",
    "ListComponentProvisionedResourcesInputPaginateTypeDef",
    "ListComponentProvisionedResourcesInputTypeDef",
    "ListComponentProvisionedResourcesOutputTypeDef",
    "ListComponentsInputPaginateTypeDef",
    "ListComponentsInputTypeDef",
    "ListComponentsOutputTypeDef",
    "ListDeploymentsInputPaginateTypeDef",
    "ListDeploymentsInputTypeDef",
    "ListDeploymentsOutputTypeDef",
    "ListEnvironmentAccountConnectionsInputPaginateTypeDef",
    "ListEnvironmentAccountConnectionsInputTypeDef",
    "ListEnvironmentAccountConnectionsOutputTypeDef",
    "ListEnvironmentOutputsInputPaginateTypeDef",
    "ListEnvironmentOutputsInputTypeDef",
    "ListEnvironmentOutputsOutputTypeDef",
    "ListEnvironmentProvisionedResourcesInputPaginateTypeDef",
    "ListEnvironmentProvisionedResourcesInputTypeDef",
    "ListEnvironmentProvisionedResourcesOutputTypeDef",
    "ListEnvironmentTemplateVersionsInputPaginateTypeDef",
    "ListEnvironmentTemplateVersionsInputTypeDef",
    "ListEnvironmentTemplateVersionsOutputTypeDef",
    "ListEnvironmentTemplatesInputPaginateTypeDef",
    "ListEnvironmentTemplatesInputTypeDef",
    "ListEnvironmentTemplatesOutputTypeDef",
    "ListEnvironmentsInputPaginateTypeDef",
    "ListEnvironmentsInputTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListRepositoriesInputPaginateTypeDef",
    "ListRepositoriesInputTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListRepositorySyncDefinitionsInputPaginateTypeDef",
    "ListRepositorySyncDefinitionsInputTypeDef",
    "ListRepositorySyncDefinitionsOutputTypeDef",
    "ListServiceInstanceOutputsInputPaginateTypeDef",
    "ListServiceInstanceOutputsInputTypeDef",
    "ListServiceInstanceOutputsOutputTypeDef",
    "ListServiceInstanceProvisionedResourcesInputPaginateTypeDef",
    "ListServiceInstanceProvisionedResourcesInputTypeDef",
    "ListServiceInstanceProvisionedResourcesOutputTypeDef",
    "ListServiceInstancesFilterTypeDef",
    "ListServiceInstancesInputPaginateTypeDef",
    "ListServiceInstancesInputTypeDef",
    "ListServiceInstancesOutputTypeDef",
    "ListServicePipelineOutputsInputPaginateTypeDef",
    "ListServicePipelineOutputsInputTypeDef",
    "ListServicePipelineOutputsOutputTypeDef",
    "ListServicePipelineProvisionedResourcesInputPaginateTypeDef",
    "ListServicePipelineProvisionedResourcesInputTypeDef",
    "ListServicePipelineProvisionedResourcesOutputTypeDef",
    "ListServiceTemplateVersionsInputPaginateTypeDef",
    "ListServiceTemplateVersionsInputTypeDef",
    "ListServiceTemplateVersionsOutputTypeDef",
    "ListServiceTemplatesInputPaginateTypeDef",
    "ListServiceTemplatesInputTypeDef",
    "ListServiceTemplatesOutputTypeDef",
    "ListServicesInputPaginateTypeDef",
    "ListServicesInputTypeDef",
    "ListServicesOutputTypeDef",
    "ListTagsForResourceInputPaginateTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "NotifyResourceDeploymentStatusChangeInputTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedResourceTypeDef",
    "RejectEnvironmentAccountConnectionInputTypeDef",
    "RejectEnvironmentAccountConnectionOutputTypeDef",
    "RepositoryBranchInputTypeDef",
    "RepositoryBranchTypeDef",
    "RepositorySummaryTypeDef",
    "RepositorySyncAttemptTypeDef",
    "RepositorySyncDefinitionTypeDef",
    "RepositorySyncEventTypeDef",
    "RepositoryTypeDef",
    "ResourceCountsSummaryTypeDef",
    "ResourceSyncAttemptTypeDef",
    "ResourceSyncEventTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionTypeDef",
    "S3ObjectSourceTypeDef",
    "ServiceInstanceStateTypeDef",
    "ServiceInstanceSummaryTypeDef",
    "ServiceInstanceTypeDef",
    "ServicePipelineStateTypeDef",
    "ServicePipelineTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceSyncBlockerSummaryTypeDef",
    "ServiceSyncConfigTypeDef",
    "ServiceTemplateSummaryTypeDef",
    "ServiceTemplateTypeDef",
    "ServiceTemplateVersionSummaryTypeDef",
    "ServiceTemplateVersionTypeDef",
    "ServiceTypeDef",
    "SyncBlockerContextTypeDef",
    "SyncBlockerTypeDef",
    "TagResourceInputTypeDef",
    "TagTypeDef",
    "TemplateSyncConfigTypeDef",
    "TemplateVersionSourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateAccountSettingsInputTypeDef",
    "UpdateAccountSettingsOutputTypeDef",
    "UpdateComponentInputTypeDef",
    "UpdateComponentOutputTypeDef",
    "UpdateEnvironmentAccountConnectionInputTypeDef",
    "UpdateEnvironmentAccountConnectionOutputTypeDef",
    "UpdateEnvironmentInputTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateEnvironmentTemplateInputTypeDef",
    "UpdateEnvironmentTemplateOutputTypeDef",
    "UpdateEnvironmentTemplateVersionInputTypeDef",
    "UpdateEnvironmentTemplateVersionOutputTypeDef",
    "UpdateServiceInputTypeDef",
    "UpdateServiceInstanceInputTypeDef",
    "UpdateServiceInstanceOutputTypeDef",
    "UpdateServiceOutputTypeDef",
    "UpdateServicePipelineInputTypeDef",
    "UpdateServicePipelineOutputTypeDef",
    "UpdateServiceSyncBlockerInputTypeDef",
    "UpdateServiceSyncBlockerOutputTypeDef",
    "UpdateServiceSyncConfigInputTypeDef",
    "UpdateServiceSyncConfigOutputTypeDef",
    "UpdateServiceTemplateInputTypeDef",
    "UpdateServiceTemplateOutputTypeDef",
    "UpdateServiceTemplateVersionInputTypeDef",
    "UpdateServiceTemplateVersionOutputTypeDef",
    "UpdateTemplateSyncConfigInputTypeDef",
    "UpdateTemplateSyncConfigOutputTypeDef",
    "WaiterConfigTypeDef",
)

AcceptEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
    },
)
EnvironmentAccountConnectionTypeDef = TypedDict(
    "EnvironmentAccountConnectionTypeDef",
    {
        "arn": str,
        "environmentAccountId": str,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "managementAccountId": str,
        "requestedAt": datetime,
        "roleArn": str,
        "status": EnvironmentAccountConnectionStatusType,
        "codebuildRoleArn": NotRequired[str],
        "componentRoleArn": NotRequired[str],
    },
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class RepositoryBranchTypeDef(TypedDict):
    arn: str
    branch: str
    name: str
    provider: RepositoryProviderType

class CancelComponentDeploymentInputTypeDef(TypedDict):
    componentName: str

class ComponentTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    lastModifiedAt: datetime
    name: str
    deploymentStatusMessage: NotRequired[str]
    description: NotRequired[str]
    lastAttemptedDeploymentId: NotRequired[str]
    lastClientRequestToken: NotRequired[str]
    lastDeploymentAttemptedAt: NotRequired[datetime]
    lastDeploymentSucceededAt: NotRequired[datetime]
    lastSucceededDeploymentId: NotRequired[str]
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]
    serviceSpec: NotRequired[str]

class CancelEnvironmentDeploymentInputTypeDef(TypedDict):
    environmentName: str

class CancelServiceInstanceDeploymentInputTypeDef(TypedDict):
    serviceInstanceName: str
    serviceName: str

class ServiceInstanceTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    name: str
    serviceName: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    deploymentStatusMessage: NotRequired[str]
    lastAttemptedDeploymentId: NotRequired[str]
    lastClientRequestToken: NotRequired[str]
    lastSucceededDeploymentId: NotRequired[str]
    spec: NotRequired[str]

class CancelServicePipelineDeploymentInputTypeDef(TypedDict):
    serviceName: str

class ServicePipelineTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    deploymentStatusMessage: NotRequired[str]
    lastAttemptedDeploymentId: NotRequired[str]
    lastSucceededDeploymentId: NotRequired[str]
    spec: NotRequired[str]

class CompatibleEnvironmentTemplateInputTypeDef(TypedDict):
    majorVersion: str
    templateName: str

class CompatibleEnvironmentTemplateTypeDef(TypedDict):
    majorVersion: str
    templateName: str

class ComponentStateTypeDef(TypedDict):
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]
    serviceSpec: NotRequired[str]
    templateFile: NotRequired[str]

class ComponentSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    lastModifiedAt: datetime
    name: str
    deploymentStatusMessage: NotRequired[str]
    lastAttemptedDeploymentId: NotRequired[str]
    lastDeploymentAttemptedAt: NotRequired[datetime]
    lastDeploymentSucceededAt: NotRequired[datetime]
    lastSucceededDeploymentId: NotRequired[str]
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]

class ResourceCountsSummaryTypeDef(TypedDict):
    total: int
    behindMajor: NotRequired[int]
    behindMinor: NotRequired[int]
    failed: NotRequired[int]
    upToDate: NotRequired[int]

class TagTypeDef(TypedDict):
    key: str
    value: str

class RepositoryBranchInputTypeDef(TypedDict):
    branch: str
    name: str
    provider: RepositoryProviderType

class EnvironmentTemplateTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: NotRequired[str]
    displayName: NotRequired[str]
    encryptionKey: NotRequired[str]
    provisioning: NotRequired[Literal["CUSTOMER_MANAGED"]]
    recommendedVersion: NotRequired[str]

class EnvironmentTemplateVersionTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    majorVersion: str
    minorVersion: str
    status: TemplateVersionStatusType
    templateName: str
    description: NotRequired[str]
    recommendedMinorVersion: NotRequired[str]
    schema: NotRequired[str]
    statusMessage: NotRequired[str]

class RepositoryTypeDef(TypedDict):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: NotRequired[str]

class CreateServiceSyncConfigInputTypeDef(TypedDict):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class ServiceSyncConfigTypeDef(TypedDict):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class ServiceTemplateTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: NotRequired[str]
    displayName: NotRequired[str]
    encryptionKey: NotRequired[str]
    pipelineProvisioning: NotRequired[Literal["CUSTOMER_MANAGED"]]
    recommendedVersion: NotRequired[str]

class CreateTemplateSyncConfigInputTypeDef(TypedDict):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: NotRequired[str]

class TemplateSyncConfigTypeDef(TypedDict):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: NotRequired[str]

class DeleteComponentInputTypeDef(TypedDict):
    name: str

DeleteDeploymentInputTypeDef = TypedDict(
    "DeleteDeploymentInputTypeDef",
    {
        "id": str,
    },
)
DeleteEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
    },
)

class DeleteEnvironmentInputTypeDef(TypedDict):
    name: str

class DeleteEnvironmentTemplateInputTypeDef(TypedDict):
    name: str

class DeleteEnvironmentTemplateVersionInputTypeDef(TypedDict):
    majorVersion: str
    minorVersion: str
    templateName: str

class DeleteRepositoryInputTypeDef(TypedDict):
    name: str
    provider: RepositoryProviderType

class DeleteServiceInputTypeDef(TypedDict):
    name: str

class DeleteServiceSyncConfigInputTypeDef(TypedDict):
    serviceName: str

class DeleteServiceTemplateInputTypeDef(TypedDict):
    name: str

class DeleteServiceTemplateVersionInputTypeDef(TypedDict):
    majorVersion: str
    minorVersion: str
    templateName: str

class DeleteTemplateSyncConfigInputTypeDef(TypedDict):
    templateName: str
    templateType: TemplateTypeType

class EnvironmentStateTypeDef(TypedDict):
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    spec: NotRequired[str]

class ServiceInstanceStateTypeDef(TypedDict):
    spec: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    lastSuccessfulComponentDeploymentIds: NotRequired[List[str]]
    lastSuccessfulEnvironmentDeploymentId: NotRequired[str]
    lastSuccessfulServicePipelineDeploymentId: NotRequired[str]

class ServicePipelineStateTypeDef(TypedDict):
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    spec: NotRequired[str]

DeploymentSummaryTypeDef = TypedDict(
    "DeploymentSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "targetArn": str,
        "targetResourceCreatedAt": datetime,
        "targetResourceType": DeploymentTargetResourceTypeType,
        "completedAt": NotRequired[datetime],
        "componentName": NotRequired[str],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)
EnvironmentAccountConnectionSummaryTypeDef = TypedDict(
    "EnvironmentAccountConnectionSummaryTypeDef",
    {
        "arn": str,
        "environmentAccountId": str,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "managementAccountId": str,
        "requestedAt": datetime,
        "roleArn": str,
        "status": EnvironmentAccountConnectionStatusType,
        "componentRoleArn": NotRequired[str],
    },
)

class EnvironmentSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    name: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    componentRoleArn: NotRequired[str]
    deploymentStatusMessage: NotRequired[str]
    description: NotRequired[str]
    environmentAccountConnectionId: NotRequired[str]
    environmentAccountId: NotRequired[str]
    lastAttemptedDeploymentId: NotRequired[str]
    lastSucceededDeploymentId: NotRequired[str]
    protonServiceRoleArn: NotRequired[str]
    provisioning: NotRequired[Literal["CUSTOMER_MANAGED"]]

class EnvironmentTemplateFilterTypeDef(TypedDict):
    majorVersion: str
    templateName: str

class EnvironmentTemplateSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: NotRequired[str]
    displayName: NotRequired[str]
    provisioning: NotRequired[Literal["CUSTOMER_MANAGED"]]
    recommendedVersion: NotRequired[str]

class EnvironmentTemplateVersionSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    majorVersion: str
    minorVersion: str
    status: TemplateVersionStatusType
    templateName: str
    description: NotRequired[str]
    recommendedMinorVersion: NotRequired[str]
    statusMessage: NotRequired[str]

class GetComponentInputTypeDef(TypedDict):
    name: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

GetDeploymentInputTypeDef = TypedDict(
    "GetDeploymentInputTypeDef",
    {
        "id": str,
        "componentName": NotRequired[str],
        "environmentName": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
    },
)
GetEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
    },
)

class GetEnvironmentInputTypeDef(TypedDict):
    name: str

class GetEnvironmentTemplateInputTypeDef(TypedDict):
    name: str

class GetEnvironmentTemplateVersionInputTypeDef(TypedDict):
    majorVersion: str
    minorVersion: str
    templateName: str

class GetRepositoryInputTypeDef(TypedDict):
    name: str
    provider: RepositoryProviderType

class GetRepositorySyncStatusInputTypeDef(TypedDict):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType

class GetServiceInputTypeDef(TypedDict):
    name: str

class GetServiceInstanceInputTypeDef(TypedDict):
    name: str
    serviceName: str

class GetServiceInstanceSyncStatusInputTypeDef(TypedDict):
    serviceInstanceName: str
    serviceName: str

class RevisionTypeDef(TypedDict):
    branch: str
    directory: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    sha: str

class GetServiceSyncBlockerSummaryInputTypeDef(TypedDict):
    serviceName: str
    serviceInstanceName: NotRequired[str]

class GetServiceSyncConfigInputTypeDef(TypedDict):
    serviceName: str

class GetServiceTemplateInputTypeDef(TypedDict):
    name: str

class GetServiceTemplateVersionInputTypeDef(TypedDict):
    majorVersion: str
    minorVersion: str
    templateName: str

class GetTemplateSyncConfigInputTypeDef(TypedDict):
    templateName: str
    templateType: TemplateTypeType

class GetTemplateSyncStatusInputTypeDef(TypedDict):
    templateName: str
    templateType: TemplateTypeType
    templateVersion: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListComponentOutputsInputTypeDef(TypedDict):
    componentName: str
    deploymentId: NotRequired[str]
    nextToken: NotRequired[str]

class OutputTypeDef(TypedDict):
    key: NotRequired[str]
    valueString: NotRequired[str]

class ListComponentProvisionedResourcesInputTypeDef(TypedDict):
    componentName: str
    nextToken: NotRequired[str]

class ProvisionedResourceTypeDef(TypedDict):
    identifier: NotRequired[str]
    name: NotRequired[str]
    provisioningEngine: NotRequired[ProvisionedResourceEngineType]

class ListComponentsInputTypeDef(TypedDict):
    environmentName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]

class ListDeploymentsInputTypeDef(TypedDict):
    componentName: NotRequired[str]
    environmentName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]

class ListEnvironmentAccountConnectionsInputTypeDef(TypedDict):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    statuses: NotRequired[Sequence[EnvironmentAccountConnectionStatusType]]

class ListEnvironmentOutputsInputTypeDef(TypedDict):
    environmentName: str
    deploymentId: NotRequired[str]
    nextToken: NotRequired[str]

class ListEnvironmentProvisionedResourcesInputTypeDef(TypedDict):
    environmentName: str
    nextToken: NotRequired[str]

class ListEnvironmentTemplateVersionsInputTypeDef(TypedDict):
    templateName: str
    majorVersion: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEnvironmentTemplatesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListRepositoriesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class RepositorySummaryTypeDef(TypedDict):
    arn: str
    connectionArn: str
    name: str
    provider: RepositoryProviderType

class ListRepositorySyncDefinitionsInputTypeDef(TypedDict):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    nextToken: NotRequired[str]

class RepositorySyncDefinitionTypeDef(TypedDict):
    branch: str
    directory: str
    parent: str
    target: str

class ListServiceInstanceOutputsInputTypeDef(TypedDict):
    serviceInstanceName: str
    serviceName: str
    deploymentId: NotRequired[str]
    nextToken: NotRequired[str]

class ListServiceInstanceProvisionedResourcesInputTypeDef(TypedDict):
    serviceInstanceName: str
    serviceName: str
    nextToken: NotRequired[str]

class ListServiceInstancesFilterTypeDef(TypedDict):
    key: NotRequired[ListServiceInstancesFilterByType]
    value: NotRequired[str]

class ServiceInstanceSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    environmentName: str
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    name: str
    serviceName: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    deploymentStatusMessage: NotRequired[str]
    lastAttemptedDeploymentId: NotRequired[str]
    lastSucceededDeploymentId: NotRequired[str]

class ListServicePipelineOutputsInputTypeDef(TypedDict):
    serviceName: str
    deploymentId: NotRequired[str]
    nextToken: NotRequired[str]

class ListServicePipelineProvisionedResourcesInputTypeDef(TypedDict):
    serviceName: str
    nextToken: NotRequired[str]

class ListServiceTemplateVersionsInputTypeDef(TypedDict):
    templateName: str
    majorVersion: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ServiceTemplateVersionSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    majorVersion: str
    minorVersion: str
    status: TemplateVersionStatusType
    templateName: str
    description: NotRequired[str]
    recommendedMinorVersion: NotRequired[str]
    statusMessage: NotRequired[str]

class ListServiceTemplatesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ServiceTemplateSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    description: NotRequired[str]
    displayName: NotRequired[str]
    pipelineProvisioning: NotRequired[Literal["CUSTOMER_MANAGED"]]
    recommendedVersion: NotRequired[str]

class ListServicesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ServiceSummaryTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    status: ServiceStatusType
    templateName: str
    description: NotRequired[str]
    statusMessage: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

RejectEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
    },
)
RepositorySyncEventTypeDef = TypedDict(
    "RepositorySyncEventTypeDef",
    {
        "event": str,
        "time": datetime,
        "type": str,
        "externalId": NotRequired[str],
    },
)
ResourceSyncEventTypeDef = TypedDict(
    "ResourceSyncEventTypeDef",
    {
        "event": str,
        "time": datetime,
        "type": str,
        "externalId": NotRequired[str],
    },
)

class S3ObjectSourceTypeDef(TypedDict):
    bucket: str
    key: str

class SyncBlockerContextTypeDef(TypedDict):
    key: str
    value: str

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateComponentInputTypeDef(TypedDict):
    deploymentType: ComponentDeploymentUpdateTypeType
    name: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]
    serviceSpec: NotRequired[str]
    templateFile: NotRequired[str]

UpdateEnvironmentAccountConnectionInputTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionInputTypeDef",
    {
        "id": str,
        "codebuildRoleArn": NotRequired[str],
        "componentRoleArn": NotRequired[str],
        "roleArn": NotRequired[str],
    },
)

class UpdateEnvironmentTemplateInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    displayName: NotRequired[str]

class UpdateEnvironmentTemplateVersionInputTypeDef(TypedDict):
    majorVersion: str
    minorVersion: str
    templateName: str
    description: NotRequired[str]
    status: NotRequired[TemplateVersionStatusType]

class UpdateServiceInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    spec: NotRequired[str]

class UpdateServiceInstanceInputTypeDef(TypedDict):
    deploymentType: DeploymentUpdateTypeType
    name: str
    serviceName: str
    clientToken: NotRequired[str]
    spec: NotRequired[str]
    templateMajorVersion: NotRequired[str]
    templateMinorVersion: NotRequired[str]

class UpdateServicePipelineInputTypeDef(TypedDict):
    deploymentType: DeploymentUpdateTypeType
    serviceName: str
    spec: str
    templateMajorVersion: NotRequired[str]
    templateMinorVersion: NotRequired[str]

UpdateServiceSyncBlockerInputTypeDef = TypedDict(
    "UpdateServiceSyncBlockerInputTypeDef",
    {
        "id": str,
        "resolvedReason": str,
    },
)

class UpdateServiceSyncConfigInputTypeDef(TypedDict):
    branch: str
    filePath: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    serviceName: str

class UpdateServiceTemplateInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    displayName: NotRequired[str]

class UpdateTemplateSyncConfigInputTypeDef(TypedDict):
    branch: str
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    templateName: str
    templateType: TemplateTypeType
    subdirectory: NotRequired[str]

class AcceptEnvironmentAccountConnectionOutputTypeDef(TypedDict):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentAccountConnectionOutputTypeDef(TypedDict):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentAccountConnectionOutputTypeDef(TypedDict):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentAccountConnectionOutputTypeDef(TypedDict):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RejectEnvironmentAccountConnectionOutputTypeDef(TypedDict):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentAccountConnectionOutputTypeDef(TypedDict):
    environmentAccountConnection: EnvironmentAccountConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccountSettingsTypeDef(TypedDict):
    pipelineCodebuildRoleArn: NotRequired[str]
    pipelineProvisioningRepository: NotRequired[RepositoryBranchTypeDef]
    pipelineServiceRoleArn: NotRequired[str]

class EnvironmentTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    deploymentStatus: DeploymentStatusType
    lastDeploymentAttemptedAt: datetime
    lastDeploymentSucceededAt: datetime
    name: str
    templateMajorVersion: str
    templateMinorVersion: str
    templateName: str
    codebuildRoleArn: NotRequired[str]
    componentRoleArn: NotRequired[str]
    deploymentStatusMessage: NotRequired[str]
    description: NotRequired[str]
    environmentAccountConnectionId: NotRequired[str]
    environmentAccountId: NotRequired[str]
    lastAttemptedDeploymentId: NotRequired[str]
    lastSucceededDeploymentId: NotRequired[str]
    protonServiceRoleArn: NotRequired[str]
    provisioning: NotRequired[Literal["CUSTOMER_MANAGED"]]
    provisioningRepository: NotRequired[RepositoryBranchTypeDef]
    spec: NotRequired[str]

class CancelComponentDeploymentOutputTypeDef(TypedDict):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentOutputTypeDef(TypedDict):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteComponentOutputTypeDef(TypedDict):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentOutputTypeDef(TypedDict):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComponentOutputTypeDef(TypedDict):
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelServiceInstanceDeploymentOutputTypeDef(TypedDict):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceInstanceOutputTypeDef(TypedDict):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceInstanceOutputTypeDef(TypedDict):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceInstanceOutputTypeDef(TypedDict):
    serviceInstance: ServiceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelServicePipelineDeploymentOutputTypeDef(TypedDict):
    pipeline: ServicePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastModifiedAt: datetime
    name: str
    spec: str
    status: ServiceStatusType
    templateName: str
    branchName: NotRequired[str]
    description: NotRequired[str]
    pipeline: NotRequired[ServicePipelineTypeDef]
    repositoryConnectionArn: NotRequired[str]
    repositoryId: NotRequired[str]
    statusMessage: NotRequired[str]

class UpdateServicePipelineOutputTypeDef(TypedDict):
    pipeline: ServicePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateVersionInputTypeDef(TypedDict):
    majorVersion: str
    minorVersion: str
    templateName: str
    compatibleEnvironmentTemplates: NotRequired[Sequence[CompatibleEnvironmentTemplateInputTypeDef]]
    description: NotRequired[str]
    status: NotRequired[TemplateVersionStatusType]
    supportedComponentSources: NotRequired[Sequence[Literal["DIRECTLY_DEFINED"]]]

class ServiceTemplateVersionTypeDef(TypedDict):
    arn: str
    compatibleEnvironmentTemplates: List[CompatibleEnvironmentTemplateTypeDef]
    createdAt: datetime
    lastModifiedAt: datetime
    majorVersion: str
    minorVersion: str
    status: TemplateVersionStatusType
    templateName: str
    description: NotRequired[str]
    recommendedMinorVersion: NotRequired[str]
    schema: NotRequired[str]
    statusMessage: NotRequired[str]
    supportedComponentSources: NotRequired[List[Literal["DIRECTLY_DEFINED"]]]

class ListComponentsOutputTypeDef(TypedDict):
    components: List[ComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CountsSummaryTypeDef(TypedDict):
    components: NotRequired[ResourceCountsSummaryTypeDef]
    environmentTemplates: NotRequired[ResourceCountsSummaryTypeDef]
    environments: NotRequired[ResourceCountsSummaryTypeDef]
    pipelines: NotRequired[ResourceCountsSummaryTypeDef]
    serviceInstances: NotRequired[ResourceCountsSummaryTypeDef]
    serviceTemplates: NotRequired[ResourceCountsSummaryTypeDef]
    services: NotRequired[ResourceCountsSummaryTypeDef]

class CreateComponentInputTypeDef(TypedDict):
    manifest: str
    name: str
    templateFile: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    environmentName: NotRequired[str]
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]
    serviceSpec: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateEnvironmentAccountConnectionInputTypeDef(TypedDict):
    environmentName: str
    managementAccountId: str
    clientToken: NotRequired[str]
    codebuildRoleArn: NotRequired[str]
    componentRoleArn: NotRequired[str]
    roleArn: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateEnvironmentTemplateInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    displayName: NotRequired[str]
    encryptionKey: NotRequired[str]
    provisioning: NotRequired[Literal["CUSTOMER_MANAGED"]]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateRepositoryInputTypeDef(TypedDict):
    connectionArn: str
    name: str
    provider: RepositoryProviderType
    encryptionKey: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateServiceInputTypeDef(TypedDict):
    name: str
    spec: str
    templateMajorVersion: str
    templateName: str
    branchName: NotRequired[str]
    description: NotRequired[str]
    repositoryConnectionArn: NotRequired[str]
    repositoryId: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    templateMinorVersion: NotRequired[str]

class CreateServiceInstanceInputTypeDef(TypedDict):
    name: str
    serviceName: str
    spec: str
    clientToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]
    templateMajorVersion: NotRequired[str]
    templateMinorVersion: NotRequired[str]

class CreateServiceTemplateInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    displayName: NotRequired[str]
    encryptionKey: NotRequired[str]
    pipelineProvisioning: NotRequired[Literal["CUSTOMER_MANAGED"]]
    tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateEnvironmentInputTypeDef(TypedDict):
    name: str
    spec: str
    templateMajorVersion: str
    templateName: str
    codebuildRoleArn: NotRequired[str]
    componentRoleArn: NotRequired[str]
    description: NotRequired[str]
    environmentAccountConnectionId: NotRequired[str]
    protonServiceRoleArn: NotRequired[str]
    provisioningRepository: NotRequired[RepositoryBranchInputTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]
    templateMinorVersion: NotRequired[str]

class UpdateAccountSettingsInputTypeDef(TypedDict):
    deletePipelineProvisioningRepository: NotRequired[bool]
    pipelineCodebuildRoleArn: NotRequired[str]
    pipelineProvisioningRepository: NotRequired[RepositoryBranchInputTypeDef]
    pipelineServiceRoleArn: NotRequired[str]

class UpdateEnvironmentInputTypeDef(TypedDict):
    deploymentType: DeploymentUpdateTypeType
    name: str
    codebuildRoleArn: NotRequired[str]
    componentRoleArn: NotRequired[str]
    description: NotRequired[str]
    environmentAccountConnectionId: NotRequired[str]
    protonServiceRoleArn: NotRequired[str]
    provisioningRepository: NotRequired[RepositoryBranchInputTypeDef]
    spec: NotRequired[str]
    templateMajorVersion: NotRequired[str]
    templateMinorVersion: NotRequired[str]

class CreateEnvironmentTemplateOutputTypeDef(TypedDict):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentTemplateOutputTypeDef(TypedDict):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentTemplateOutputTypeDef(TypedDict):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentTemplateOutputTypeDef(TypedDict):
    environmentTemplate: EnvironmentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentTemplateVersionOutputTypeDef(TypedDict):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentTemplateVersionOutputTypeDef(TypedDict):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentTemplateVersionOutputTypeDef(TypedDict):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentTemplateVersionOutputTypeDef(TypedDict):
    environmentTemplateVersion: EnvironmentTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryOutputTypeDef(TypedDict):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryOutputTypeDef(TypedDict):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryOutputTypeDef(TypedDict):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceSyncConfigOutputTypeDef(TypedDict):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceSyncConfigOutputTypeDef(TypedDict):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSyncConfigOutputTypeDef(TypedDict):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceSyncConfigOutputTypeDef(TypedDict):
    serviceSyncConfig: ServiceSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceTemplateOutputTypeDef(TypedDict):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceTemplateOutputTypeDef(TypedDict):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceTemplateOutputTypeDef(TypedDict):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateOutputTypeDef(TypedDict):
    serviceTemplate: ServiceTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTemplateSyncConfigOutputTypeDef(TypedDict):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTemplateSyncConfigOutputTypeDef(TypedDict):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateSyncConfigOutputTypeDef(TypedDict):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTemplateSyncConfigOutputTypeDef(TypedDict):
    templateSyncConfig: TemplateSyncConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentStateTypeDef(TypedDict):
    component: NotRequired[ComponentStateTypeDef]
    environment: NotRequired[EnvironmentStateTypeDef]
    serviceInstance: NotRequired[ServiceInstanceStateTypeDef]
    servicePipeline: NotRequired[ServicePipelineStateTypeDef]

class ListDeploymentsOutputTypeDef(TypedDict):
    deployments: List[DeploymentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentAccountConnectionsOutputTypeDef(TypedDict):
    environmentAccountConnections: List[EnvironmentAccountConnectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentsOutputTypeDef(TypedDict):
    environments: List[EnvironmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentsInputTypeDef(TypedDict):
    environmentTemplates: NotRequired[Sequence[EnvironmentTemplateFilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListEnvironmentTemplatesOutputTypeDef(TypedDict):
    templates: List[EnvironmentTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentTemplateVersionsOutputTypeDef(TypedDict):
    templateVersions: List[EnvironmentTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetComponentInputWaitExtraTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetComponentInputWaitTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetEnvironmentInputWaitTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetEnvironmentTemplateVersionInputWaitTypeDef(TypedDict):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetServiceInputWaitExtraExtraExtraTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetServiceInputWaitExtraExtraTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetServiceInputWaitExtraTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetServiceInputWaitTypeDef(TypedDict):
    name: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetServiceInstanceInputWaitTypeDef(TypedDict):
    name: str
    serviceName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetServiceTemplateVersionInputWaitTypeDef(TypedDict):
    majorVersion: str
    minorVersion: str
    templateName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class ListComponentOutputsInputPaginateTypeDef(TypedDict):
    componentName: str
    deploymentId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListComponentProvisionedResourcesInputPaginateTypeDef(TypedDict):
    componentName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListComponentsInputPaginateTypeDef(TypedDict):
    environmentName: NotRequired[str]
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDeploymentsInputPaginateTypeDef(TypedDict):
    componentName: NotRequired[str]
    environmentName: NotRequired[str]
    serviceInstanceName: NotRequired[str]
    serviceName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentAccountConnectionsInputPaginateTypeDef(TypedDict):
    requestedBy: EnvironmentAccountConnectionRequesterAccountTypeType
    environmentName: NotRequired[str]
    statuses: NotRequired[Sequence[EnvironmentAccountConnectionStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentOutputsInputPaginateTypeDef(TypedDict):
    environmentName: str
    deploymentId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentProvisionedResourcesInputPaginateTypeDef(TypedDict):
    environmentName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentTemplateVersionsInputPaginateTypeDef(TypedDict):
    templateName: str
    majorVersion: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentTemplatesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEnvironmentsInputPaginateTypeDef(TypedDict):
    environmentTemplates: NotRequired[Sequence[EnvironmentTemplateFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRepositoriesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRepositorySyncDefinitionsInputPaginateTypeDef(TypedDict):
    repositoryName: str
    repositoryProvider: RepositoryProviderType
    syncType: SyncTypeType
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceInstanceOutputsInputPaginateTypeDef(TypedDict):
    serviceInstanceName: str
    serviceName: str
    deploymentId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceInstanceProvisionedResourcesInputPaginateTypeDef(TypedDict):
    serviceInstanceName: str
    serviceName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicePipelineOutputsInputPaginateTypeDef(TypedDict):
    serviceName: str
    deploymentId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicePipelineProvisionedResourcesInputPaginateTypeDef(TypedDict):
    serviceName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceTemplateVersionsInputPaginateTypeDef(TypedDict):
    templateName: str
    majorVersion: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceTemplatesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceInputPaginateTypeDef(TypedDict):
    resourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListComponentOutputsOutputTypeDef(TypedDict):
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentOutputsOutputTypeDef(TypedDict):
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceInstanceOutputsOutputTypeDef(TypedDict):
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServicePipelineOutputsOutputTypeDef(TypedDict):
    outputs: List[OutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class NotifyResourceDeploymentStatusChangeInputTypeDef(TypedDict):
    resourceArn: str
    deploymentId: NotRequired[str]
    outputs: NotRequired[Sequence[OutputTypeDef]]
    status: NotRequired[ResourceDeploymentStatusType]
    statusMessage: NotRequired[str]

class ListComponentProvisionedResourcesOutputTypeDef(TypedDict):
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListEnvironmentProvisionedResourcesOutputTypeDef(TypedDict):
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceInstanceProvisionedResourcesOutputTypeDef(TypedDict):
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServicePipelineProvisionedResourcesOutputTypeDef(TypedDict):
    provisionedResources: List[ProvisionedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRepositoriesOutputTypeDef(TypedDict):
    repositories: List[RepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRepositorySyncDefinitionsOutputTypeDef(TypedDict):
    syncDefinitions: List[RepositorySyncDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceInstancesInputPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[ListServiceInstancesFilterTypeDef]]
    serviceName: NotRequired[str]
    sortBy: NotRequired[ListServiceInstancesSortByType]
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceInstancesInputTypeDef(TypedDict):
    filters: NotRequired[Sequence[ListServiceInstancesFilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    serviceName: NotRequired[str]
    sortBy: NotRequired[ListServiceInstancesSortByType]
    sortOrder: NotRequired[SortOrderType]

class ListServiceInstancesOutputTypeDef(TypedDict):
    serviceInstances: List[ServiceInstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceTemplateVersionsOutputTypeDef(TypedDict):
    templateVersions: List[ServiceTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceTemplatesOutputTypeDef(TypedDict):
    templates: List[ServiceTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServicesOutputTypeDef(TypedDict):
    services: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RepositorySyncAttemptTypeDef(TypedDict):
    events: List[RepositorySyncEventTypeDef]
    startedAt: datetime
    status: RepositorySyncStatusType

class ResourceSyncAttemptTypeDef(TypedDict):
    events: List[ResourceSyncEventTypeDef]
    initialRevision: RevisionTypeDef
    startedAt: datetime
    status: ResourceSyncStatusType
    target: str
    targetRevision: RevisionTypeDef

class TemplateVersionSourceInputTypeDef(TypedDict):
    s3: NotRequired[S3ObjectSourceTypeDef]

SyncBlockerTypeDef = TypedDict(
    "SyncBlockerTypeDef",
    {
        "createdAt": datetime,
        "createdReason": str,
        "id": str,
        "status": BlockerStatusType,
        "type": Literal["AUTOMATED"],
        "contexts": NotRequired[List[SyncBlockerContextTypeDef]],
        "resolvedAt": NotRequired[datetime],
        "resolvedReason": NotRequired[str],
    },
)

class GetAccountSettingsOutputTypeDef(TypedDict):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsOutputTypeDef(TypedDict):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelEnvironmentDeploymentOutputTypeDef(TypedDict):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentOutputTypeDef(TypedDict):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEnvironmentOutputTypeDef(TypedDict):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnvironmentOutputTypeDef(TypedDict):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnvironmentOutputTypeDef(TypedDict):
    environment: EnvironmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceOutputTypeDef(TypedDict):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceOutputTypeDef(TypedDict):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceOutputTypeDef(TypedDict):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceOutputTypeDef(TypedDict):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceTemplateVersionOutputTypeDef(TypedDict):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceTemplateVersionOutputTypeDef(TypedDict):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceTemplateVersionOutputTypeDef(TypedDict):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceTemplateVersionOutputTypeDef(TypedDict):
    serviceTemplateVersion: ServiceTemplateVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcesSummaryOutputTypeDef(TypedDict):
    counts: CountsSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "id": str,
        "lastModifiedAt": datetime,
        "targetArn": str,
        "targetResourceCreatedAt": datetime,
        "targetResourceType": DeploymentTargetResourceTypeType,
        "completedAt": NotRequired[datetime],
        "componentName": NotRequired[str],
        "deploymentStatusMessage": NotRequired[str],
        "initialState": NotRequired[DeploymentStateTypeDef],
        "lastAttemptedDeploymentId": NotRequired[str],
        "lastSucceededDeploymentId": NotRequired[str],
        "serviceInstanceName": NotRequired[str],
        "serviceName": NotRequired[str],
        "targetState": NotRequired[DeploymentStateTypeDef],
    },
)

class GetRepositorySyncStatusOutputTypeDef(TypedDict):
    latestSync: RepositorySyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceInstanceSyncStatusOutputTypeDef(TypedDict):
    desiredState: RevisionTypeDef
    latestSuccessfulSync: ResourceSyncAttemptTypeDef
    latestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTemplateSyncStatusOutputTypeDef(TypedDict):
    desiredState: RevisionTypeDef
    latestSuccessfulSync: ResourceSyncAttemptTypeDef
    latestSync: ResourceSyncAttemptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEnvironmentTemplateVersionInputTypeDef(TypedDict):
    source: TemplateVersionSourceInputTypeDef
    templateName: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    majorVersion: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateServiceTemplateVersionInputTypeDef(TypedDict):
    compatibleEnvironmentTemplates: Sequence[CompatibleEnvironmentTemplateInputTypeDef]
    source: TemplateVersionSourceInputTypeDef
    templateName: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    majorVersion: NotRequired[str]
    supportedComponentSources: NotRequired[Sequence[Literal["DIRECTLY_DEFINED"]]]
    tags: NotRequired[Sequence[TagTypeDef]]

class ServiceSyncBlockerSummaryTypeDef(TypedDict):
    serviceName: str
    latestBlockers: NotRequired[List[SyncBlockerTypeDef]]
    serviceInstanceName: NotRequired[str]

class UpdateServiceSyncBlockerOutputTypeDef(TypedDict):
    serviceInstanceName: str
    serviceName: str
    serviceSyncBlocker: SyncBlockerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeploymentOutputTypeDef(TypedDict):
    deployment: DeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentOutputTypeDef(TypedDict):
    deployment: DeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceSyncBlockerSummaryOutputTypeDef(TypedDict):
    serviceSyncBlockerSummary: ServiceSyncBlockerSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
