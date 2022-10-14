"""
Type annotations for proton service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_proton/type_defs.html)

Usage::

    ```python
    from mypy_boto3_proton.type_defs import AcceptEnvironmentAccountConnectionInputRequestTypeDef

    data: AcceptEnvironmentAccountConnectionInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ComponentDeploymentUpdateTypeType,
    DeploymentStatusType,
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    ProvisionedResourceEngineType,
    RepositoryProviderType,
    RepositorySyncStatusType,
    ResourceDeploymentStatusType,
    ResourceSyncStatusType,
    ServiceStatusType,
    TemplateTypeType,
    TemplateVersionStatusType,
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
    "AcceptEnvironmentAccountConnectionInputRequestTypeDef",
    "AcceptEnvironmentAccountConnectionOutputTypeDef",
    "AccountSettingsTypeDef",
    "CancelComponentDeploymentInputRequestTypeDef",
    "CancelComponentDeploymentOutputTypeDef",
    "CancelEnvironmentDeploymentInputRequestTypeDef",
    "CancelEnvironmentDeploymentOutputTypeDef",
    "CancelServiceInstanceDeploymentInputRequestTypeDef",
    "CancelServiceInstanceDeploymentOutputTypeDef",
    "CancelServicePipelineDeploymentInputRequestTypeDef",
    "CancelServicePipelineDeploymentOutputTypeDef",
    "CompatibleEnvironmentTemplateInputTypeDef",
    "CompatibleEnvironmentTemplateTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "CreateComponentInputRequestTypeDef",
    "CreateComponentOutputTypeDef",
    "CreateEnvironmentAccountConnectionInputRequestTypeDef",
    "CreateEnvironmentAccountConnectionOutputTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateEnvironmentTemplateInputRequestTypeDef",
    "CreateEnvironmentTemplateOutputTypeDef",
    "CreateEnvironmentTemplateVersionInputRequestTypeDef",
    "CreateEnvironmentTemplateVersionOutputTypeDef",
    "CreateRepositoryInputRequestTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateServiceInputRequestTypeDef",
    "CreateServiceOutputTypeDef",
    "CreateServiceTemplateInputRequestTypeDef",
    "CreateServiceTemplateOutputTypeDef",
    "CreateServiceTemplateVersionInputRequestTypeDef",
    "CreateServiceTemplateVersionOutputTypeDef",
    "CreateTemplateSyncConfigInputRequestTypeDef",
    "CreateTemplateSyncConfigOutputTypeDef",
    "DeleteComponentInputRequestTypeDef",
    "DeleteComponentOutputTypeDef",
    "DeleteEnvironmentAccountConnectionInputRequestTypeDef",
    "DeleteEnvironmentAccountConnectionOutputTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DeleteEnvironmentOutputTypeDef",
    "DeleteEnvironmentTemplateInputRequestTypeDef",
    "DeleteEnvironmentTemplateOutputTypeDef",
    "DeleteEnvironmentTemplateVersionInputRequestTypeDef",
    "DeleteEnvironmentTemplateVersionOutputTypeDef",
    "DeleteRepositoryInputRequestTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DeleteServiceInputRequestTypeDef",
    "DeleteServiceOutputTypeDef",
    "DeleteServiceTemplateInputRequestTypeDef",
    "DeleteServiceTemplateOutputTypeDef",
    "DeleteServiceTemplateVersionInputRequestTypeDef",
    "DeleteServiceTemplateVersionOutputTypeDef",
    "DeleteTemplateSyncConfigInputRequestTypeDef",
    "DeleteTemplateSyncConfigOutputTypeDef",
    "EnvironmentAccountConnectionSummaryTypeDef",
    "EnvironmentAccountConnectionTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentTemplateFilterTypeDef",
    "EnvironmentTemplateSummaryTypeDef",
    "EnvironmentTemplateTypeDef",
    "EnvironmentTemplateVersionSummaryTypeDef",
    "EnvironmentTemplateVersionTypeDef",
    "EnvironmentTypeDef",
    "GetAccountSettingsOutputTypeDef",
    "GetComponentInputRequestTypeDef",
    "GetComponentOutputTypeDef",
    "GetEnvironmentAccountConnectionInputRequestTypeDef",
    "GetEnvironmentAccountConnectionOutputTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentOutputTypeDef",
    "GetEnvironmentTemplateInputRequestTypeDef",
    "GetEnvironmentTemplateOutputTypeDef",
    "GetEnvironmentTemplateVersionInputRequestTypeDef",
    "GetEnvironmentTemplateVersionOutputTypeDef",
    "GetRepositoryInputRequestTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositorySyncStatusInputRequestTypeDef",
    "GetRepositorySyncStatusOutputTypeDef",
    "GetServiceInputRequestTypeDef",
    "GetServiceInstanceInputRequestTypeDef",
    "GetServiceInstanceOutputTypeDef",
    "GetServiceOutputTypeDef",
    "GetServiceTemplateInputRequestTypeDef",
    "GetServiceTemplateOutputTypeDef",
    "GetServiceTemplateVersionInputRequestTypeDef",
    "GetServiceTemplateVersionOutputTypeDef",
    "GetTemplateSyncConfigInputRequestTypeDef",
    "GetTemplateSyncConfigOutputTypeDef",
    "GetTemplateSyncStatusInputRequestTypeDef",
    "GetTemplateSyncStatusOutputTypeDef",
    "ListComponentOutputsInputRequestTypeDef",
    "ListComponentOutputsOutputTypeDef",
    "ListComponentProvisionedResourcesInputRequestTypeDef",
    "ListComponentProvisionedResourcesOutputTypeDef",
    "ListComponentsInputRequestTypeDef",
    "ListComponentsOutputTypeDef",
    "ListEnvironmentAccountConnectionsInputRequestTypeDef",
    "ListEnvironmentAccountConnectionsOutputTypeDef",
    "ListEnvironmentOutputsInputRequestTypeDef",
    "ListEnvironmentOutputsOutputTypeDef",
    "ListEnvironmentProvisionedResourcesInputRequestTypeDef",
    "ListEnvironmentProvisionedResourcesOutputTypeDef",
    "ListEnvironmentTemplateVersionsInputRequestTypeDef",
    "ListEnvironmentTemplateVersionsOutputTypeDef",
    "ListEnvironmentTemplatesInputRequestTypeDef",
    "ListEnvironmentTemplatesOutputTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListRepositoriesInputRequestTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListRepositorySyncDefinitionsInputRequestTypeDef",
    "ListRepositorySyncDefinitionsOutputTypeDef",
    "ListServiceInstanceOutputsInputRequestTypeDef",
    "ListServiceInstanceOutputsOutputTypeDef",
    "ListServiceInstanceProvisionedResourcesInputRequestTypeDef",
    "ListServiceInstanceProvisionedResourcesOutputTypeDef",
    "ListServiceInstancesInputRequestTypeDef",
    "ListServiceInstancesOutputTypeDef",
    "ListServicePipelineOutputsInputRequestTypeDef",
    "ListServicePipelineOutputsOutputTypeDef",
    "ListServicePipelineProvisionedResourcesInputRequestTypeDef",
    "ListServicePipelineProvisionedResourcesOutputTypeDef",
    "ListServiceTemplateVersionsInputRequestTypeDef",
    "ListServiceTemplateVersionsOutputTypeDef",
    "ListServiceTemplatesInputRequestTypeDef",
    "ListServiceTemplatesOutputTypeDef",
    "ListServicesInputRequestTypeDef",
    "ListServicesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "NotifyResourceDeploymentStatusChangeInputRequestTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedResourceTypeDef",
    "RejectEnvironmentAccountConnectionInputRequestTypeDef",
    "RejectEnvironmentAccountConnectionOutputTypeDef",
    "RepositoryBranchInputTypeDef",
    "RepositoryBranchTypeDef",
    "RepositorySummaryTypeDef",
    "RepositorySyncAttemptTypeDef",
    "RepositorySyncDefinitionTypeDef",
    "RepositorySyncEventTypeDef",
    "RepositoryTypeDef",
    "ResourceSyncAttemptTypeDef",
    "ResourceSyncEventTypeDef",
    "ResponseMetadataTypeDef",
    "RevisionTypeDef",
    "S3ObjectSourceTypeDef",
    "ServiceInstanceSummaryTypeDef",
    "ServiceInstanceTypeDef",
    "ServicePipelineTypeDef",
    "ServiceSummaryTypeDef",
    "ServiceTemplateSummaryTypeDef",
    "ServiceTemplateTypeDef",
    "ServiceTemplateVersionSummaryTypeDef",
    "ServiceTemplateVersionTypeDef",
    "ServiceTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TemplateSyncConfigTypeDef",
    "TemplateVersionSourceInputTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAccountSettingsInputRequestTypeDef",
    "UpdateAccountSettingsOutputTypeDef",
    "UpdateComponentInputRequestTypeDef",
    "UpdateComponentOutputTypeDef",
    "UpdateEnvironmentAccountConnectionInputRequestTypeDef",
    "UpdateEnvironmentAccountConnectionOutputTypeDef",
    "UpdateEnvironmentInputRequestTypeDef",
    "UpdateEnvironmentOutputTypeDef",
    "UpdateEnvironmentTemplateInputRequestTypeDef",
    "UpdateEnvironmentTemplateOutputTypeDef",
    "UpdateEnvironmentTemplateVersionInputRequestTypeDef",
    "UpdateEnvironmentTemplateVersionOutputTypeDef",
    "UpdateServiceInputRequestTypeDef",
    "UpdateServiceInstanceInputRequestTypeDef",
    "UpdateServiceInstanceOutputTypeDef",
    "UpdateServiceOutputTypeDef",
    "UpdateServicePipelineInputRequestTypeDef",
    "UpdateServicePipelineOutputTypeDef",
    "UpdateServiceTemplateInputRequestTypeDef",
    "UpdateServiceTemplateOutputTypeDef",
    "UpdateServiceTemplateVersionInputRequestTypeDef",
    "UpdateServiceTemplateVersionOutputTypeDef",
    "UpdateTemplateSyncConfigInputRequestTypeDef",
    "UpdateTemplateSyncConfigOutputTypeDef",
    "WaiterConfigTypeDef",
)

AcceptEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)

AcceptEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "AcceptEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "pipelineProvisioningRepository": "RepositoryBranchTypeDef",
        "pipelineServiceRoleArn": str,
    },
    total=False,
)

CancelComponentDeploymentInputRequestTypeDef = TypedDict(
    "CancelComponentDeploymentInputRequestTypeDef",
    {
        "componentName": str,
    },
)

CancelComponentDeploymentOutputTypeDef = TypedDict(
    "CancelComponentDeploymentOutputTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelEnvironmentDeploymentInputRequestTypeDef = TypedDict(
    "CancelEnvironmentDeploymentInputRequestTypeDef",
    {
        "environmentName": str,
    },
)

CancelEnvironmentDeploymentOutputTypeDef = TypedDict(
    "CancelEnvironmentDeploymentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelServiceInstanceDeploymentInputRequestTypeDef = TypedDict(
    "CancelServiceInstanceDeploymentInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
    },
)

CancelServiceInstanceDeploymentOutputTypeDef = TypedDict(
    "CancelServiceInstanceDeploymentOutputTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelServicePipelineDeploymentInputRequestTypeDef = TypedDict(
    "CancelServicePipelineDeploymentInputRequestTypeDef",
    {
        "serviceName": str,
    },
)

CancelServicePipelineDeploymentOutputTypeDef = TypedDict(
    "CancelServicePipelineDeploymentOutputTypeDef",
    {
        "pipeline": "ServicePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompatibleEnvironmentTemplateInputTypeDef = TypedDict(
    "CompatibleEnvironmentTemplateInputTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

CompatibleEnvironmentTemplateTypeDef = TypedDict(
    "CompatibleEnvironmentTemplateTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

_RequiredComponentSummaryTypeDef = TypedDict(
    "_RequiredComponentSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalComponentSummaryTypeDef = TypedDict(
    "_OptionalComponentSummaryTypeDef",
    {
        "deploymentStatusMessage": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "serviceInstanceName": str,
        "serviceName": str,
    },
    total=False,
)

class ComponentSummaryTypeDef(_RequiredComponentSummaryTypeDef, _OptionalComponentSummaryTypeDef):
    pass

_RequiredComponentTypeDef = TypedDict(
    "_RequiredComponentTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalComponentTypeDef = TypedDict(
    "_OptionalComponentTypeDef",
    {
        "deploymentStatusMessage": str,
        "description": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "serviceInstanceName": str,
        "serviceName": str,
        "serviceSpec": str,
    },
    total=False,
)

class ComponentTypeDef(_RequiredComponentTypeDef, _OptionalComponentTypeDef):
    pass

_RequiredCreateComponentInputRequestTypeDef = TypedDict(
    "_RequiredCreateComponentInputRequestTypeDef",
    {
        "manifest": str,
        "name": str,
        "templateFile": str,
    },
)
_OptionalCreateComponentInputRequestTypeDef = TypedDict(
    "_OptionalCreateComponentInputRequestTypeDef",
    {
        "description": str,
        "environmentName": str,
        "serviceInstanceName": str,
        "serviceName": str,
        "serviceSpec": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateComponentInputRequestTypeDef(
    _RequiredCreateComponentInputRequestTypeDef, _OptionalCreateComponentInputRequestTypeDef
):
    pass

CreateComponentOutputTypeDef = TypedDict(
    "CreateComponentOutputTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "environmentName": str,
        "managementAccountId": str,
        "roleArn": str,
    },
)
_OptionalCreateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "clientToken": str,
        "componentRoleArn": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEnvironmentAccountConnectionInputRequestTypeDef(
    _RequiredCreateEnvironmentAccountConnectionInputRequestTypeDef,
    _OptionalCreateEnvironmentAccountConnectionInputRequestTypeDef,
):
    pass

CreateEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "CreateEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentInputRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentInputRequestTypeDef",
    {
        "name": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateName": str,
    },
)
_OptionalCreateEnvironmentInputRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentInputRequestTypeDef",
    {
        "componentRoleArn": str,
        "description": str,
        "environmentAccountConnectionId": str,
        "protonServiceRoleArn": str,
        "provisioningRepository": "RepositoryBranchInputTypeDef",
        "tags": List["TagTypeDef"],
        "templateMinorVersion": str,
    },
    total=False,
)

class CreateEnvironmentInputRequestTypeDef(
    _RequiredCreateEnvironmentInputRequestTypeDef, _OptionalCreateEnvironmentInputRequestTypeDef
):
    pass

CreateEnvironmentOutputTypeDef = TypedDict(
    "CreateEnvironmentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentTemplateInputRequestTypeDef",
    {
        "description": str,
        "displayName": str,
        "encryptionKey": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEnvironmentTemplateInputRequestTypeDef(
    _RequiredCreateEnvironmentTemplateInputRequestTypeDef,
    _OptionalCreateEnvironmentTemplateInputRequestTypeDef,
):
    pass

CreateEnvironmentTemplateOutputTypeDef = TypedDict(
    "CreateEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "source": "TemplateVersionSourceInputTypeDef",
        "templateName": str,
    },
)
_OptionalCreateEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "majorVersion": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEnvironmentTemplateVersionInputRequestTypeDef(
    _RequiredCreateEnvironmentTemplateVersionInputRequestTypeDef,
    _OptionalCreateEnvironmentTemplateVersionInputRequestTypeDef,
):
    pass

CreateEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "CreateEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryInputRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryInputRequestTypeDef",
    {
        "connectionArn": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)
_OptionalCreateRepositoryInputRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryInputRequestTypeDef",
    {
        "encryptionKey": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRepositoryInputRequestTypeDef(
    _RequiredCreateRepositoryInputRequestTypeDef, _OptionalCreateRepositoryInputRequestTypeDef
):
    pass

CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceInputRequestTypeDef = TypedDict(
    "_RequiredCreateServiceInputRequestTypeDef",
    {
        "name": str,
        "spec": str,
        "templateMajorVersion": str,
        "templateName": str,
    },
)
_OptionalCreateServiceInputRequestTypeDef = TypedDict(
    "_OptionalCreateServiceInputRequestTypeDef",
    {
        "branchName": str,
        "description": str,
        "repositoryConnectionArn": str,
        "repositoryId": str,
        "tags": List["TagTypeDef"],
        "templateMinorVersion": str,
    },
    total=False,
)

class CreateServiceInputRequestTypeDef(
    _RequiredCreateServiceInputRequestTypeDef, _OptionalCreateServiceInputRequestTypeDef
):
    pass

CreateServiceOutputTypeDef = TypedDict(
    "CreateServiceOutputTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceTemplateInputRequestTypeDef = TypedDict(
    "_RequiredCreateServiceTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateServiceTemplateInputRequestTypeDef = TypedDict(
    "_OptionalCreateServiceTemplateInputRequestTypeDef",
    {
        "description": str,
        "displayName": str,
        "encryptionKey": str,
        "pipelineProvisioning": Literal["CUSTOMER_MANAGED"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateServiceTemplateInputRequestTypeDef(
    _RequiredCreateServiceTemplateInputRequestTypeDef,
    _OptionalCreateServiceTemplateInputRequestTypeDef,
):
    pass

CreateServiceTemplateOutputTypeDef = TypedDict(
    "CreateServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "_RequiredCreateServiceTemplateVersionInputRequestTypeDef",
    {
        "compatibleEnvironmentTemplates": List["CompatibleEnvironmentTemplateInputTypeDef"],
        "source": "TemplateVersionSourceInputTypeDef",
        "templateName": str,
    },
)
_OptionalCreateServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "_OptionalCreateServiceTemplateVersionInputRequestTypeDef",
    {
        "clientToken": str,
        "description": str,
        "majorVersion": str,
        "supportedComponentSources": List[Literal["DIRECTLY_DEFINED"]],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateServiceTemplateVersionInputRequestTypeDef(
    _RequiredCreateServiceTemplateVersionInputRequestTypeDef,
    _OptionalCreateServiceTemplateVersionInputRequestTypeDef,
):
    pass

CreateServiceTemplateVersionOutputTypeDef = TypedDict(
    "CreateServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "_RequiredCreateTemplateSyncConfigInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)
_OptionalCreateTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "_OptionalCreateTemplateSyncConfigInputRequestTypeDef",
    {
        "subdirectory": str,
    },
    total=False,
)

class CreateTemplateSyncConfigInputRequestTypeDef(
    _RequiredCreateTemplateSyncConfigInputRequestTypeDef,
    _OptionalCreateTemplateSyncConfigInputRequestTypeDef,
):
    pass

CreateTemplateSyncConfigOutputTypeDef = TypedDict(
    "CreateTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": "TemplateSyncConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteComponentInputRequestTypeDef = TypedDict(
    "DeleteComponentInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteComponentOutputTypeDef = TypedDict(
    "DeleteComponentOutputTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)

DeleteEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "DeleteEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEnvironmentOutputTypeDef = TypedDict(
    "DeleteEnvironmentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteEnvironmentTemplateOutputTypeDef = TypedDict(
    "DeleteEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "DeleteEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

DeleteEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "DeleteEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryInputRequestTypeDef = TypedDict(
    "DeleteRepositoryInputRequestTypeDef",
    {
        "name": str,
        "provider": RepositoryProviderType,
    },
)

DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceInputRequestTypeDef = TypedDict(
    "DeleteServiceInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteServiceOutputTypeDef = TypedDict(
    "DeleteServiceOutputTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceTemplateInputRequestTypeDef = TypedDict(
    "DeleteServiceTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)

DeleteServiceTemplateOutputTypeDef = TypedDict(
    "DeleteServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "DeleteServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

DeleteServiceTemplateVersionOutputTypeDef = TypedDict(
    "DeleteServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "DeleteTemplateSyncConfigInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)

DeleteTemplateSyncConfigOutputTypeDef = TypedDict(
    "DeleteTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": "TemplateSyncConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnvironmentAccountConnectionSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentAccountConnectionSummaryTypeDef",
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
    },
)
_OptionalEnvironmentAccountConnectionSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentAccountConnectionSummaryTypeDef",
    {
        "componentRoleArn": str,
    },
    total=False,
)

class EnvironmentAccountConnectionSummaryTypeDef(
    _RequiredEnvironmentAccountConnectionSummaryTypeDef,
    _OptionalEnvironmentAccountConnectionSummaryTypeDef,
):
    pass

_RequiredEnvironmentAccountConnectionTypeDef = TypedDict(
    "_RequiredEnvironmentAccountConnectionTypeDef",
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
    },
)
_OptionalEnvironmentAccountConnectionTypeDef = TypedDict(
    "_OptionalEnvironmentAccountConnectionTypeDef",
    {
        "componentRoleArn": str,
    },
    total=False,
)

class EnvironmentAccountConnectionTypeDef(
    _RequiredEnvironmentAccountConnectionTypeDef, _OptionalEnvironmentAccountConnectionTypeDef
):
    pass

_RequiredEnvironmentSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalEnvironmentSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentSummaryTypeDef",
    {
        "componentRoleArn": str,
        "deploymentStatusMessage": str,
        "description": str,
        "environmentAccountConnectionId": str,
        "environmentAccountId": str,
        "protonServiceRoleArn": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
    },
    total=False,
)

class EnvironmentSummaryTypeDef(
    _RequiredEnvironmentSummaryTypeDef, _OptionalEnvironmentSummaryTypeDef
):
    pass

EnvironmentTemplateFilterTypeDef = TypedDict(
    "EnvironmentTemplateFilterTypeDef",
    {
        "majorVersion": str,
        "templateName": str,
    },
)

_RequiredEnvironmentTemplateSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentTemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalEnvironmentTemplateSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentTemplateSummaryTypeDef",
    {
        "description": str,
        "displayName": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
        "recommendedVersion": str,
    },
    total=False,
)

class EnvironmentTemplateSummaryTypeDef(
    _RequiredEnvironmentTemplateSummaryTypeDef, _OptionalEnvironmentTemplateSummaryTypeDef
):
    pass

_RequiredEnvironmentTemplateTypeDef = TypedDict(
    "_RequiredEnvironmentTemplateTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalEnvironmentTemplateTypeDef = TypedDict(
    "_OptionalEnvironmentTemplateTypeDef",
    {
        "description": str,
        "displayName": str,
        "encryptionKey": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
        "recommendedVersion": str,
    },
    total=False,
)

class EnvironmentTemplateTypeDef(
    _RequiredEnvironmentTemplateTypeDef, _OptionalEnvironmentTemplateTypeDef
):
    pass

_RequiredEnvironmentTemplateVersionSummaryTypeDef = TypedDict(
    "_RequiredEnvironmentTemplateVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
    },
)
_OptionalEnvironmentTemplateVersionSummaryTypeDef = TypedDict(
    "_OptionalEnvironmentTemplateVersionSummaryTypeDef",
    {
        "description": str,
        "recommendedMinorVersion": str,
        "statusMessage": str,
    },
    total=False,
)

class EnvironmentTemplateVersionSummaryTypeDef(
    _RequiredEnvironmentTemplateVersionSummaryTypeDef,
    _OptionalEnvironmentTemplateVersionSummaryTypeDef,
):
    pass

_RequiredEnvironmentTemplateVersionTypeDef = TypedDict(
    "_RequiredEnvironmentTemplateVersionTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
    },
)
_OptionalEnvironmentTemplateVersionTypeDef = TypedDict(
    "_OptionalEnvironmentTemplateVersionTypeDef",
    {
        "description": str,
        "recommendedMinorVersion": str,
        "schema": str,
        "statusMessage": str,
    },
    total=False,
)

class EnvironmentTemplateVersionTypeDef(
    _RequiredEnvironmentTemplateVersionTypeDef, _OptionalEnvironmentTemplateVersionTypeDef
):
    pass

_RequiredEnvironmentTypeDef = TypedDict(
    "_RequiredEnvironmentTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalEnvironmentTypeDef = TypedDict(
    "_OptionalEnvironmentTypeDef",
    {
        "componentRoleArn": str,
        "deploymentStatusMessage": str,
        "description": str,
        "environmentAccountConnectionId": str,
        "environmentAccountId": str,
        "protonServiceRoleArn": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
        "provisioningRepository": "RepositoryBranchTypeDef",
        "spec": str,
    },
    total=False,
)

class EnvironmentTypeDef(_RequiredEnvironmentTypeDef, _OptionalEnvironmentTypeDef):
    pass

GetAccountSettingsOutputTypeDef = TypedDict(
    "GetAccountSettingsOutputTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentInputRequestTypeDef = TypedDict(
    "GetComponentInputRequestTypeDef",
    {
        "name": str,
    },
)

GetComponentOutputTypeDef = TypedDict(
    "GetComponentOutputTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)

GetEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "GetEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentInputRequestTypeDef = TypedDict(
    "GetEnvironmentInputRequestTypeDef",
    {
        "name": str,
    },
)

GetEnvironmentOutputTypeDef = TypedDict(
    "GetEnvironmentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "GetEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)

GetEnvironmentTemplateOutputTypeDef = TypedDict(
    "GetEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

GetEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "GetEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryInputRequestTypeDef = TypedDict(
    "GetRepositoryInputRequestTypeDef",
    {
        "name": str,
        "provider": RepositoryProviderType,
    },
)

GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositorySyncStatusInputRequestTypeDef = TypedDict(
    "GetRepositorySyncStatusInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "syncType": Literal["TEMPLATE_SYNC"],
    },
)

GetRepositorySyncStatusOutputTypeDef = TypedDict(
    "GetRepositorySyncStatusOutputTypeDef",
    {
        "latestSync": "RepositorySyncAttemptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceInputRequestTypeDef = TypedDict(
    "GetServiceInputRequestTypeDef",
    {
        "name": str,
    },
)

GetServiceInstanceInputRequestTypeDef = TypedDict(
    "GetServiceInstanceInputRequestTypeDef",
    {
        "name": str,
        "serviceName": str,
    },
)

GetServiceInstanceOutputTypeDef = TypedDict(
    "GetServiceInstanceOutputTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceOutputTypeDef = TypedDict(
    "GetServiceOutputTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceTemplateInputRequestTypeDef = TypedDict(
    "GetServiceTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)

GetServiceTemplateOutputTypeDef = TypedDict(
    "GetServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "GetServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)

GetServiceTemplateVersionOutputTypeDef = TypedDict(
    "GetServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "GetTemplateSyncConfigInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)

GetTemplateSyncConfigOutputTypeDef = TypedDict(
    "GetTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": "TemplateSyncConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemplateSyncStatusInputRequestTypeDef = TypedDict(
    "GetTemplateSyncStatusInputRequestTypeDef",
    {
        "templateName": str,
        "templateType": TemplateTypeType,
        "templateVersion": str,
    },
)

GetTemplateSyncStatusOutputTypeDef = TypedDict(
    "GetTemplateSyncStatusOutputTypeDef",
    {
        "desiredState": "RevisionTypeDef",
        "latestSuccessfulSync": "ResourceSyncAttemptTypeDef",
        "latestSync": "ResourceSyncAttemptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentOutputsInputRequestTypeDef = TypedDict(
    "_RequiredListComponentOutputsInputRequestTypeDef",
    {
        "componentName": str,
    },
)
_OptionalListComponentOutputsInputRequestTypeDef = TypedDict(
    "_OptionalListComponentOutputsInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListComponentOutputsInputRequestTypeDef(
    _RequiredListComponentOutputsInputRequestTypeDef,
    _OptionalListComponentOutputsInputRequestTypeDef,
):
    pass

ListComponentOutputsOutputTypeDef = TypedDict(
    "ListComponentOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListComponentProvisionedResourcesInputRequestTypeDef = TypedDict(
    "_RequiredListComponentProvisionedResourcesInputRequestTypeDef",
    {
        "componentName": str,
    },
)
_OptionalListComponentProvisionedResourcesInputRequestTypeDef = TypedDict(
    "_OptionalListComponentProvisionedResourcesInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListComponentProvisionedResourcesInputRequestTypeDef(
    _RequiredListComponentProvisionedResourcesInputRequestTypeDef,
    _OptionalListComponentProvisionedResourcesInputRequestTypeDef,
):
    pass

ListComponentProvisionedResourcesOutputTypeDef = TypedDict(
    "ListComponentProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List["ProvisionedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsInputRequestTypeDef = TypedDict(
    "ListComponentsInputRequestTypeDef",
    {
        "environmentName": str,
        "maxResults": int,
        "nextToken": str,
        "serviceInstanceName": str,
        "serviceName": str,
    },
    total=False,
)

ListComponentsOutputTypeDef = TypedDict(
    "ListComponentsOutputTypeDef",
    {
        "components": List["ComponentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentAccountConnectionsInputRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentAccountConnectionsInputRequestTypeDef",
    {
        "requestedBy": EnvironmentAccountConnectionRequesterAccountTypeType,
    },
)
_OptionalListEnvironmentAccountConnectionsInputRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentAccountConnectionsInputRequestTypeDef",
    {
        "environmentName": str,
        "maxResults": int,
        "nextToken": str,
        "statuses": List[EnvironmentAccountConnectionStatusType],
    },
    total=False,
)

class ListEnvironmentAccountConnectionsInputRequestTypeDef(
    _RequiredListEnvironmentAccountConnectionsInputRequestTypeDef,
    _OptionalListEnvironmentAccountConnectionsInputRequestTypeDef,
):
    pass

ListEnvironmentAccountConnectionsOutputTypeDef = TypedDict(
    "ListEnvironmentAccountConnectionsOutputTypeDef",
    {
        "environmentAccountConnections": List["EnvironmentAccountConnectionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentOutputsInputRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentOutputsInputRequestTypeDef",
    {
        "environmentName": str,
    },
)
_OptionalListEnvironmentOutputsInputRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentOutputsInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListEnvironmentOutputsInputRequestTypeDef(
    _RequiredListEnvironmentOutputsInputRequestTypeDef,
    _OptionalListEnvironmentOutputsInputRequestTypeDef,
):
    pass

ListEnvironmentOutputsOutputTypeDef = TypedDict(
    "ListEnvironmentOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentProvisionedResourcesInputRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentProvisionedResourcesInputRequestTypeDef",
    {
        "environmentName": str,
    },
)
_OptionalListEnvironmentProvisionedResourcesInputRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentProvisionedResourcesInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListEnvironmentProvisionedResourcesInputRequestTypeDef(
    _RequiredListEnvironmentProvisionedResourcesInputRequestTypeDef,
    _OptionalListEnvironmentProvisionedResourcesInputRequestTypeDef,
):
    pass

ListEnvironmentProvisionedResourcesOutputTypeDef = TypedDict(
    "ListEnvironmentProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List["ProvisionedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentTemplateVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentTemplateVersionsInputRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalListEnvironmentTemplateVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentTemplateVersionsInputRequestTypeDef",
    {
        "majorVersion": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListEnvironmentTemplateVersionsInputRequestTypeDef(
    _RequiredListEnvironmentTemplateVersionsInputRequestTypeDef,
    _OptionalListEnvironmentTemplateVersionsInputRequestTypeDef,
):
    pass

ListEnvironmentTemplateVersionsOutputTypeDef = TypedDict(
    "ListEnvironmentTemplateVersionsOutputTypeDef",
    {
        "nextToken": str,
        "templateVersions": List["EnvironmentTemplateVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentTemplatesInputRequestTypeDef = TypedDict(
    "ListEnvironmentTemplatesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListEnvironmentTemplatesOutputTypeDef = TypedDict(
    "ListEnvironmentTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "templates": List["EnvironmentTemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentsInputRequestTypeDef = TypedDict(
    "ListEnvironmentsInputRequestTypeDef",
    {
        "environmentTemplates": List["EnvironmentTemplateFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListEnvironmentsOutputTypeDef = TypedDict(
    "ListEnvironmentsOutputTypeDef",
    {
        "environments": List["EnvironmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesInputRequestTypeDef = TypedDict(
    "ListRepositoriesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {
        "nextToken": str,
        "repositories": List["RepositorySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRepositorySyncDefinitionsInputRequestTypeDef = TypedDict(
    "_RequiredListRepositorySyncDefinitionsInputRequestTypeDef",
    {
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "syncType": Literal["TEMPLATE_SYNC"],
    },
)
_OptionalListRepositorySyncDefinitionsInputRequestTypeDef = TypedDict(
    "_OptionalListRepositorySyncDefinitionsInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListRepositorySyncDefinitionsInputRequestTypeDef(
    _RequiredListRepositorySyncDefinitionsInputRequestTypeDef,
    _OptionalListRepositorySyncDefinitionsInputRequestTypeDef,
):
    pass

ListRepositorySyncDefinitionsOutputTypeDef = TypedDict(
    "ListRepositorySyncDefinitionsOutputTypeDef",
    {
        "nextToken": str,
        "syncDefinitions": List["RepositorySyncDefinitionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceInstanceOutputsInputRequestTypeDef = TypedDict(
    "_RequiredListServiceInstanceOutputsInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
    },
)
_OptionalListServiceInstanceOutputsInputRequestTypeDef = TypedDict(
    "_OptionalListServiceInstanceOutputsInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListServiceInstanceOutputsInputRequestTypeDef(
    _RequiredListServiceInstanceOutputsInputRequestTypeDef,
    _OptionalListServiceInstanceOutputsInputRequestTypeDef,
):
    pass

ListServiceInstanceOutputsOutputTypeDef = TypedDict(
    "ListServiceInstanceOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceInstanceProvisionedResourcesInputRequestTypeDef = TypedDict(
    "_RequiredListServiceInstanceProvisionedResourcesInputRequestTypeDef",
    {
        "serviceInstanceName": str,
        "serviceName": str,
    },
)
_OptionalListServiceInstanceProvisionedResourcesInputRequestTypeDef = TypedDict(
    "_OptionalListServiceInstanceProvisionedResourcesInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListServiceInstanceProvisionedResourcesInputRequestTypeDef(
    _RequiredListServiceInstanceProvisionedResourcesInputRequestTypeDef,
    _OptionalListServiceInstanceProvisionedResourcesInputRequestTypeDef,
):
    pass

ListServiceInstanceProvisionedResourcesOutputTypeDef = TypedDict(
    "ListServiceInstanceProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List["ProvisionedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceInstancesInputRequestTypeDef = TypedDict(
    "ListServiceInstancesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "serviceName": str,
    },
    total=False,
)

ListServiceInstancesOutputTypeDef = TypedDict(
    "ListServiceInstancesOutputTypeDef",
    {
        "nextToken": str,
        "serviceInstances": List["ServiceInstanceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServicePipelineOutputsInputRequestTypeDef = TypedDict(
    "_RequiredListServicePipelineOutputsInputRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalListServicePipelineOutputsInputRequestTypeDef = TypedDict(
    "_OptionalListServicePipelineOutputsInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListServicePipelineOutputsInputRequestTypeDef(
    _RequiredListServicePipelineOutputsInputRequestTypeDef,
    _OptionalListServicePipelineOutputsInputRequestTypeDef,
):
    pass

ListServicePipelineOutputsOutputTypeDef = TypedDict(
    "ListServicePipelineOutputsOutputTypeDef",
    {
        "nextToken": str,
        "outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServicePipelineProvisionedResourcesInputRequestTypeDef = TypedDict(
    "_RequiredListServicePipelineProvisionedResourcesInputRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalListServicePipelineProvisionedResourcesInputRequestTypeDef = TypedDict(
    "_OptionalListServicePipelineProvisionedResourcesInputRequestTypeDef",
    {
        "nextToken": str,
    },
    total=False,
)

class ListServicePipelineProvisionedResourcesInputRequestTypeDef(
    _RequiredListServicePipelineProvisionedResourcesInputRequestTypeDef,
    _OptionalListServicePipelineProvisionedResourcesInputRequestTypeDef,
):
    pass

ListServicePipelineProvisionedResourcesOutputTypeDef = TypedDict(
    "ListServicePipelineProvisionedResourcesOutputTypeDef",
    {
        "nextToken": str,
        "provisionedResources": List["ProvisionedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServiceTemplateVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListServiceTemplateVersionsInputRequestTypeDef",
    {
        "templateName": str,
    },
)
_OptionalListServiceTemplateVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListServiceTemplateVersionsInputRequestTypeDef",
    {
        "majorVersion": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListServiceTemplateVersionsInputRequestTypeDef(
    _RequiredListServiceTemplateVersionsInputRequestTypeDef,
    _OptionalListServiceTemplateVersionsInputRequestTypeDef,
):
    pass

ListServiceTemplateVersionsOutputTypeDef = TypedDict(
    "ListServiceTemplateVersionsOutputTypeDef",
    {
        "nextToken": str,
        "templateVersions": List["ServiceTemplateVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceTemplatesInputRequestTypeDef = TypedDict(
    "ListServiceTemplatesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListServiceTemplatesOutputTypeDef = TypedDict(
    "ListServiceTemplatesOutputTypeDef",
    {
        "nextToken": str,
        "templates": List["ServiceTemplateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesInputRequestTypeDef = TypedDict(
    "ListServicesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListServicesOutputTypeDef = TypedDict(
    "ListServicesOutputTypeDef",
    {
        "nextToken": str,
        "services": List["ServiceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "nextToken": str,
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNotifyResourceDeploymentStatusChangeInputRequestTypeDef = TypedDict(
    "_RequiredNotifyResourceDeploymentStatusChangeInputRequestTypeDef",
    {
        "resourceArn": str,
        "status": ResourceDeploymentStatusType,
    },
)
_OptionalNotifyResourceDeploymentStatusChangeInputRequestTypeDef = TypedDict(
    "_OptionalNotifyResourceDeploymentStatusChangeInputRequestTypeDef",
    {
        "deploymentId": str,
        "outputs": List["OutputTypeDef"],
        "statusMessage": str,
    },
    total=False,
)

class NotifyResourceDeploymentStatusChangeInputRequestTypeDef(
    _RequiredNotifyResourceDeploymentStatusChangeInputRequestTypeDef,
    _OptionalNotifyResourceDeploymentStatusChangeInputRequestTypeDef,
):
    pass

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "key": str,
        "valueString": str,
    },
    total=False,
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

ProvisionedResourceTypeDef = TypedDict(
    "ProvisionedResourceTypeDef",
    {
        "identifier": str,
        "name": str,
        "provisioningEngine": ProvisionedResourceEngineType,
    },
    total=False,
)

RejectEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)

RejectEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "RejectEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryBranchInputTypeDef = TypedDict(
    "RepositoryBranchInputTypeDef",
    {
        "branch": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)

RepositoryBranchTypeDef = TypedDict(
    "RepositoryBranchTypeDef",
    {
        "arn": str,
        "branch": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)

RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)

RepositorySyncAttemptTypeDef = TypedDict(
    "RepositorySyncAttemptTypeDef",
    {
        "events": List["RepositorySyncEventTypeDef"],
        "startedAt": datetime,
        "status": RepositorySyncStatusType,
    },
)

RepositorySyncDefinitionTypeDef = TypedDict(
    "RepositorySyncDefinitionTypeDef",
    {
        "branch": str,
        "directory": str,
        "parent": str,
        "target": str,
    },
)

_RequiredRepositorySyncEventTypeDef = TypedDict(
    "_RequiredRepositorySyncEventTypeDef",
    {
        "event": str,
        "time": datetime,
        "type": str,
    },
)
_OptionalRepositorySyncEventTypeDef = TypedDict(
    "_OptionalRepositorySyncEventTypeDef",
    {
        "externalId": str,
    },
    total=False,
)

class RepositorySyncEventTypeDef(
    _RequiredRepositorySyncEventTypeDef, _OptionalRepositorySyncEventTypeDef
):
    pass

_RequiredRepositoryTypeDef = TypedDict(
    "_RequiredRepositoryTypeDef",
    {
        "arn": str,
        "connectionArn": str,
        "name": str,
        "provider": RepositoryProviderType,
    },
)
_OptionalRepositoryTypeDef = TypedDict(
    "_OptionalRepositoryTypeDef",
    {
        "encryptionKey": str,
    },
    total=False,
)

class RepositoryTypeDef(_RequiredRepositoryTypeDef, _OptionalRepositoryTypeDef):
    pass

ResourceSyncAttemptTypeDef = TypedDict(
    "ResourceSyncAttemptTypeDef",
    {
        "events": List["ResourceSyncEventTypeDef"],
        "initialRevision": "RevisionTypeDef",
        "startedAt": datetime,
        "status": ResourceSyncStatusType,
        "target": str,
        "targetRevision": "RevisionTypeDef",
    },
)

_RequiredResourceSyncEventTypeDef = TypedDict(
    "_RequiredResourceSyncEventTypeDef",
    {
        "event": str,
        "time": datetime,
        "type": str,
    },
)
_OptionalResourceSyncEventTypeDef = TypedDict(
    "_OptionalResourceSyncEventTypeDef",
    {
        "externalId": str,
    },
    total=False,
)

class ResourceSyncEventTypeDef(
    _RequiredResourceSyncEventTypeDef, _OptionalResourceSyncEventTypeDef
):
    pass

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

RevisionTypeDef = TypedDict(
    "RevisionTypeDef",
    {
        "branch": str,
        "directory": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "sha": str,
    },
)

S3ObjectSourceTypeDef = TypedDict(
    "S3ObjectSourceTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)

_RequiredServiceInstanceSummaryTypeDef = TypedDict(
    "_RequiredServiceInstanceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "serviceName": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalServiceInstanceSummaryTypeDef = TypedDict(
    "_OptionalServiceInstanceSummaryTypeDef",
    {
        "deploymentStatusMessage": str,
    },
    total=False,
)

class ServiceInstanceSummaryTypeDef(
    _RequiredServiceInstanceSummaryTypeDef, _OptionalServiceInstanceSummaryTypeDef
):
    pass

_RequiredServiceInstanceTypeDef = TypedDict(
    "_RequiredServiceInstanceTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "environmentName": str,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "name": str,
        "serviceName": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalServiceInstanceTypeDef = TypedDict(
    "_OptionalServiceInstanceTypeDef",
    {
        "deploymentStatusMessage": str,
        "spec": str,
    },
    total=False,
)

class ServiceInstanceTypeDef(_RequiredServiceInstanceTypeDef, _OptionalServiceInstanceTypeDef):
    pass

_RequiredServicePipelineTypeDef = TypedDict(
    "_RequiredServicePipelineTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deploymentStatus": DeploymentStatusType,
        "lastDeploymentAttemptedAt": datetime,
        "lastDeploymentSucceededAt": datetime,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
        "templateName": str,
    },
)
_OptionalServicePipelineTypeDef = TypedDict(
    "_OptionalServicePipelineTypeDef",
    {
        "deploymentStatusMessage": str,
        "spec": str,
    },
    total=False,
)

class ServicePipelineTypeDef(_RequiredServicePipelineTypeDef, _OptionalServicePipelineTypeDef):
    pass

_RequiredServiceSummaryTypeDef = TypedDict(
    "_RequiredServiceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "status": ServiceStatusType,
        "templateName": str,
    },
)
_OptionalServiceSummaryTypeDef = TypedDict(
    "_OptionalServiceSummaryTypeDef",
    {
        "description": str,
        "statusMessage": str,
    },
    total=False,
)

class ServiceSummaryTypeDef(_RequiredServiceSummaryTypeDef, _OptionalServiceSummaryTypeDef):
    pass

_RequiredServiceTemplateSummaryTypeDef = TypedDict(
    "_RequiredServiceTemplateSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalServiceTemplateSummaryTypeDef = TypedDict(
    "_OptionalServiceTemplateSummaryTypeDef",
    {
        "description": str,
        "displayName": str,
        "pipelineProvisioning": Literal["CUSTOMER_MANAGED"],
        "recommendedVersion": str,
    },
    total=False,
)

class ServiceTemplateSummaryTypeDef(
    _RequiredServiceTemplateSummaryTypeDef, _OptionalServiceTemplateSummaryTypeDef
):
    pass

_RequiredServiceTemplateTypeDef = TypedDict(
    "_RequiredServiceTemplateTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
    },
)
_OptionalServiceTemplateTypeDef = TypedDict(
    "_OptionalServiceTemplateTypeDef",
    {
        "description": str,
        "displayName": str,
        "encryptionKey": str,
        "pipelineProvisioning": Literal["CUSTOMER_MANAGED"],
        "recommendedVersion": str,
    },
    total=False,
)

class ServiceTemplateTypeDef(_RequiredServiceTemplateTypeDef, _OptionalServiceTemplateTypeDef):
    pass

_RequiredServiceTemplateVersionSummaryTypeDef = TypedDict(
    "_RequiredServiceTemplateVersionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
    },
)
_OptionalServiceTemplateVersionSummaryTypeDef = TypedDict(
    "_OptionalServiceTemplateVersionSummaryTypeDef",
    {
        "description": str,
        "recommendedMinorVersion": str,
        "statusMessage": str,
    },
    total=False,
)

class ServiceTemplateVersionSummaryTypeDef(
    _RequiredServiceTemplateVersionSummaryTypeDef, _OptionalServiceTemplateVersionSummaryTypeDef
):
    pass

_RequiredServiceTemplateVersionTypeDef = TypedDict(
    "_RequiredServiceTemplateVersionTypeDef",
    {
        "arn": str,
        "compatibleEnvironmentTemplates": List["CompatibleEnvironmentTemplateTypeDef"],
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "majorVersion": str,
        "minorVersion": str,
        "status": TemplateVersionStatusType,
        "templateName": str,
    },
)
_OptionalServiceTemplateVersionTypeDef = TypedDict(
    "_OptionalServiceTemplateVersionTypeDef",
    {
        "description": str,
        "recommendedMinorVersion": str,
        "schema": str,
        "statusMessage": str,
        "supportedComponentSources": List[Literal["DIRECTLY_DEFINED"]],
    },
    total=False,
)

class ServiceTemplateVersionTypeDef(
    _RequiredServiceTemplateVersionTypeDef, _OptionalServiceTemplateVersionTypeDef
):
    pass

_RequiredServiceTypeDef = TypedDict(
    "_RequiredServiceTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "name": str,
        "spec": str,
        "status": ServiceStatusType,
        "templateName": str,
    },
)
_OptionalServiceTypeDef = TypedDict(
    "_OptionalServiceTypeDef",
    {
        "branchName": str,
        "description": str,
        "pipeline": "ServicePipelineTypeDef",
        "repositoryConnectionArn": str,
        "repositoryId": str,
        "statusMessage": str,
    },
    total=False,
)

class ServiceTypeDef(_RequiredServiceTypeDef, _OptionalServiceTypeDef):
    pass

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredTemplateSyncConfigTypeDef = TypedDict(
    "_RequiredTemplateSyncConfigTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)
_OptionalTemplateSyncConfigTypeDef = TypedDict(
    "_OptionalTemplateSyncConfigTypeDef",
    {
        "subdirectory": str,
    },
    total=False,
)

class TemplateSyncConfigTypeDef(
    _RequiredTemplateSyncConfigTypeDef, _OptionalTemplateSyncConfigTypeDef
):
    pass

TemplateVersionSourceInputTypeDef = TypedDict(
    "TemplateVersionSourceInputTypeDef",
    {
        "s3": "S3ObjectSourceTypeDef",
    },
    total=False,
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateAccountSettingsInputRequestTypeDef = TypedDict(
    "UpdateAccountSettingsInputRequestTypeDef",
    {
        "deletePipelineProvisioningRepository": bool,
        "pipelineProvisioningRepository": "RepositoryBranchInputTypeDef",
        "pipelineServiceRoleArn": str,
    },
    total=False,
)

UpdateAccountSettingsOutputTypeDef = TypedDict(
    "UpdateAccountSettingsOutputTypeDef",
    {
        "accountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateComponentInputRequestTypeDef = TypedDict(
    "_RequiredUpdateComponentInputRequestTypeDef",
    {
        "deploymentType": ComponentDeploymentUpdateTypeType,
        "name": str,
    },
)
_OptionalUpdateComponentInputRequestTypeDef = TypedDict(
    "_OptionalUpdateComponentInputRequestTypeDef",
    {
        "description": str,
        "serviceInstanceName": str,
        "serviceName": str,
        "serviceSpec": str,
        "templateFile": str,
    },
    total=False,
)

class UpdateComponentInputRequestTypeDef(
    _RequiredUpdateComponentInputRequestTypeDef, _OptionalUpdateComponentInputRequestTypeDef
):
    pass

UpdateComponentOutputTypeDef = TypedDict(
    "UpdateComponentOutputTypeDef",
    {
        "component": "ComponentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
    },
)
_OptionalUpdateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "componentRoleArn": str,
        "roleArn": str,
    },
    total=False,
)

class UpdateEnvironmentAccountConnectionInputRequestTypeDef(
    _RequiredUpdateEnvironmentAccountConnectionInputRequestTypeDef,
    _OptionalUpdateEnvironmentAccountConnectionInputRequestTypeDef,
):
    pass

UpdateEnvironmentAccountConnectionOutputTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionOutputTypeDef",
    {
        "environmentAccountConnection": "EnvironmentAccountConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "name": str,
    },
)
_OptionalUpdateEnvironmentInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentInputRequestTypeDef",
    {
        "componentRoleArn": str,
        "description": str,
        "environmentAccountConnectionId": str,
        "protonServiceRoleArn": str,
        "provisioningRepository": "RepositoryBranchInputTypeDef",
        "spec": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
    },
    total=False,
)

class UpdateEnvironmentInputRequestTypeDef(
    _RequiredUpdateEnvironmentInputRequestTypeDef, _OptionalUpdateEnvironmentInputRequestTypeDef
):
    pass

UpdateEnvironmentOutputTypeDef = TypedDict(
    "UpdateEnvironmentOutputTypeDef",
    {
        "environment": "EnvironmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateEnvironmentTemplateInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentTemplateInputRequestTypeDef",
    {
        "description": str,
        "displayName": str,
    },
    total=False,
)

class UpdateEnvironmentTemplateInputRequestTypeDef(
    _RequiredUpdateEnvironmentTemplateInputRequestTypeDef,
    _OptionalUpdateEnvironmentTemplateInputRequestTypeDef,
):
    pass

UpdateEnvironmentTemplateOutputTypeDef = TypedDict(
    "UpdateEnvironmentTemplateOutputTypeDef",
    {
        "environmentTemplate": "EnvironmentTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)
_OptionalUpdateEnvironmentTemplateVersionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentTemplateVersionInputRequestTypeDef",
    {
        "description": str,
        "status": TemplateVersionStatusType,
    },
    total=False,
)

class UpdateEnvironmentTemplateVersionInputRequestTypeDef(
    _RequiredUpdateEnvironmentTemplateVersionInputRequestTypeDef,
    _OptionalUpdateEnvironmentTemplateVersionInputRequestTypeDef,
):
    pass

UpdateEnvironmentTemplateVersionOutputTypeDef = TypedDict(
    "UpdateEnvironmentTemplateVersionOutputTypeDef",
    {
        "environmentTemplateVersion": "EnvironmentTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateServiceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceInputRequestTypeDef",
    {
        "description": str,
        "spec": str,
    },
    total=False,
)

class UpdateServiceInputRequestTypeDef(
    _RequiredUpdateServiceInputRequestTypeDef, _OptionalUpdateServiceInputRequestTypeDef
):
    pass

_RequiredUpdateServiceInstanceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceInstanceInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "name": str,
        "serviceName": str,
    },
)
_OptionalUpdateServiceInstanceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceInstanceInputRequestTypeDef",
    {
        "spec": str,
        "templateMajorVersion": str,
        "templateMinorVersion": str,
    },
    total=False,
)

class UpdateServiceInstanceInputRequestTypeDef(
    _RequiredUpdateServiceInstanceInputRequestTypeDef,
    _OptionalUpdateServiceInstanceInputRequestTypeDef,
):
    pass

UpdateServiceInstanceOutputTypeDef = TypedDict(
    "UpdateServiceInstanceOutputTypeDef",
    {
        "serviceInstance": "ServiceInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceOutputTypeDef = TypedDict(
    "UpdateServiceOutputTypeDef",
    {
        "service": "ServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServicePipelineInputRequestTypeDef = TypedDict(
    "_RequiredUpdateServicePipelineInputRequestTypeDef",
    {
        "deploymentType": DeploymentUpdateTypeType,
        "serviceName": str,
        "spec": str,
    },
)
_OptionalUpdateServicePipelineInputRequestTypeDef = TypedDict(
    "_OptionalUpdateServicePipelineInputRequestTypeDef",
    {
        "templateMajorVersion": str,
        "templateMinorVersion": str,
    },
    total=False,
)

class UpdateServicePipelineInputRequestTypeDef(
    _RequiredUpdateServicePipelineInputRequestTypeDef,
    _OptionalUpdateServicePipelineInputRequestTypeDef,
):
    pass

UpdateServicePipelineOutputTypeDef = TypedDict(
    "UpdateServicePipelineOutputTypeDef",
    {
        "pipeline": "ServicePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceTemplateInputRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceTemplateInputRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateServiceTemplateInputRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceTemplateInputRequestTypeDef",
    {
        "description": str,
        "displayName": str,
    },
    total=False,
)

class UpdateServiceTemplateInputRequestTypeDef(
    _RequiredUpdateServiceTemplateInputRequestTypeDef,
    _OptionalUpdateServiceTemplateInputRequestTypeDef,
):
    pass

UpdateServiceTemplateOutputTypeDef = TypedDict(
    "UpdateServiceTemplateOutputTypeDef",
    {
        "serviceTemplate": "ServiceTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceTemplateVersionInputRequestTypeDef",
    {
        "majorVersion": str,
        "minorVersion": str,
        "templateName": str,
    },
)
_OptionalUpdateServiceTemplateVersionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceTemplateVersionInputRequestTypeDef",
    {
        "compatibleEnvironmentTemplates": List["CompatibleEnvironmentTemplateInputTypeDef"],
        "description": str,
        "status": TemplateVersionStatusType,
        "supportedComponentSources": List[Literal["DIRECTLY_DEFINED"]],
    },
    total=False,
)

class UpdateServiceTemplateVersionInputRequestTypeDef(
    _RequiredUpdateServiceTemplateVersionInputRequestTypeDef,
    _OptionalUpdateServiceTemplateVersionInputRequestTypeDef,
):
    pass

UpdateServiceTemplateVersionOutputTypeDef = TypedDict(
    "UpdateServiceTemplateVersionOutputTypeDef",
    {
        "serviceTemplateVersion": "ServiceTemplateVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "_RequiredUpdateTemplateSyncConfigInputRequestTypeDef",
    {
        "branch": str,
        "repositoryName": str,
        "repositoryProvider": RepositoryProviderType,
        "templateName": str,
        "templateType": TemplateTypeType,
    },
)
_OptionalUpdateTemplateSyncConfigInputRequestTypeDef = TypedDict(
    "_OptionalUpdateTemplateSyncConfigInputRequestTypeDef",
    {
        "subdirectory": str,
    },
    total=False,
)

class UpdateTemplateSyncConfigInputRequestTypeDef(
    _RequiredUpdateTemplateSyncConfigInputRequestTypeDef,
    _OptionalUpdateTemplateSyncConfigInputRequestTypeDef,
):
    pass

UpdateTemplateSyncConfigOutputTypeDef = TypedDict(
    "UpdateTemplateSyncConfigOutputTypeDef",
    {
        "templateSyncConfig": "TemplateSyncConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
