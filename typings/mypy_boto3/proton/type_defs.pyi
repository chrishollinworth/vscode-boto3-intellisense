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
    DeploymentStatusType,
    DeploymentUpdateTypeType,
    EnvironmentAccountConnectionRequesterAccountTypeType,
    EnvironmentAccountConnectionStatusType,
    ServiceStatusType,
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
    "CancelEnvironmentDeploymentInputRequestTypeDef",
    "CancelEnvironmentDeploymentOutputTypeDef",
    "CancelServiceInstanceDeploymentInputRequestTypeDef",
    "CancelServiceInstanceDeploymentOutputTypeDef",
    "CancelServicePipelineDeploymentInputRequestTypeDef",
    "CancelServicePipelineDeploymentOutputTypeDef",
    "CompatibleEnvironmentTemplateInputTypeDef",
    "CompatibleEnvironmentTemplateTypeDef",
    "CreateEnvironmentAccountConnectionInputRequestTypeDef",
    "CreateEnvironmentAccountConnectionOutputTypeDef",
    "CreateEnvironmentInputRequestTypeDef",
    "CreateEnvironmentOutputTypeDef",
    "CreateEnvironmentTemplateInputRequestTypeDef",
    "CreateEnvironmentTemplateOutputTypeDef",
    "CreateEnvironmentTemplateVersionInputRequestTypeDef",
    "CreateEnvironmentTemplateVersionOutputTypeDef",
    "CreateServiceInputRequestTypeDef",
    "CreateServiceOutputTypeDef",
    "CreateServiceTemplateInputRequestTypeDef",
    "CreateServiceTemplateOutputTypeDef",
    "CreateServiceTemplateVersionInputRequestTypeDef",
    "CreateServiceTemplateVersionOutputTypeDef",
    "DeleteEnvironmentAccountConnectionInputRequestTypeDef",
    "DeleteEnvironmentAccountConnectionOutputTypeDef",
    "DeleteEnvironmentInputRequestTypeDef",
    "DeleteEnvironmentOutputTypeDef",
    "DeleteEnvironmentTemplateInputRequestTypeDef",
    "DeleteEnvironmentTemplateOutputTypeDef",
    "DeleteEnvironmentTemplateVersionInputRequestTypeDef",
    "DeleteEnvironmentTemplateVersionOutputTypeDef",
    "DeleteServiceInputRequestTypeDef",
    "DeleteServiceOutputTypeDef",
    "DeleteServiceTemplateInputRequestTypeDef",
    "DeleteServiceTemplateOutputTypeDef",
    "DeleteServiceTemplateVersionInputRequestTypeDef",
    "DeleteServiceTemplateVersionOutputTypeDef",
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
    "GetEnvironmentAccountConnectionInputRequestTypeDef",
    "GetEnvironmentAccountConnectionOutputTypeDef",
    "GetEnvironmentInputRequestTypeDef",
    "GetEnvironmentOutputTypeDef",
    "GetEnvironmentTemplateInputRequestTypeDef",
    "GetEnvironmentTemplateOutputTypeDef",
    "GetEnvironmentTemplateVersionInputRequestTypeDef",
    "GetEnvironmentTemplateVersionOutputTypeDef",
    "GetServiceInputRequestTypeDef",
    "GetServiceInstanceInputRequestTypeDef",
    "GetServiceInstanceOutputTypeDef",
    "GetServiceOutputTypeDef",
    "GetServiceTemplateInputRequestTypeDef",
    "GetServiceTemplateOutputTypeDef",
    "GetServiceTemplateVersionInputRequestTypeDef",
    "GetServiceTemplateVersionOutputTypeDef",
    "ListEnvironmentAccountConnectionsInputRequestTypeDef",
    "ListEnvironmentAccountConnectionsOutputTypeDef",
    "ListEnvironmentTemplateVersionsInputRequestTypeDef",
    "ListEnvironmentTemplateVersionsOutputTypeDef",
    "ListEnvironmentTemplatesInputRequestTypeDef",
    "ListEnvironmentTemplatesOutputTypeDef",
    "ListEnvironmentsInputRequestTypeDef",
    "ListEnvironmentsOutputTypeDef",
    "ListServiceInstancesInputRequestTypeDef",
    "ListServiceInstancesOutputTypeDef",
    "ListServiceTemplateVersionsInputRequestTypeDef",
    "ListServiceTemplateVersionsOutputTypeDef",
    "ListServiceTemplatesInputRequestTypeDef",
    "ListServiceTemplatesOutputTypeDef",
    "ListServicesInputRequestTypeDef",
    "ListServicesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RejectEnvironmentAccountConnectionInputRequestTypeDef",
    "RejectEnvironmentAccountConnectionOutputTypeDef",
    "ResponseMetadataTypeDef",
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
    "TemplateVersionSourceInputTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateAccountSettingsInputRequestTypeDef",
    "UpdateAccountSettingsOutputTypeDef",
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
        "pipelineServiceRoleArn": str,
    },
    total=False,
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
        "description": str,
        "environmentAccountConnectionId": str,
        "protonServiceRoleArn": str,
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
    },
)

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
        "deploymentStatusMessage": str,
        "description": str,
        "environmentAccountConnectionId": str,
        "environmentAccountId": str,
        "protonServiceRoleArn": str,
        "provisioning": Literal["CUSTOMER_MANAGED"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
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

UpdateEnvironmentAccountConnectionInputRequestTypeDef = TypedDict(
    "UpdateEnvironmentAccountConnectionInputRequestTypeDef",
    {
        "id": str,
        "roleArn": str,
    },
)

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
        "description": str,
        "environmentAccountConnectionId": str,
        "protonServiceRoleArn": str,
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

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
