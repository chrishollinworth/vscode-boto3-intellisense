"""
Type annotations for greengrass service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/type_defs.html)

Usage::

    ```python
    from mypy_boto3_greengrass.type_defs import AssociateRoleToGroupRequestRequestTypeDef

    data: AssociateRoleToGroupRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    BulkDeploymentStatusType,
    ConfigurationSyncStatusType,
    DeploymentTypeType,
    EncodingTypeType,
    FunctionIsolationModeType,
    LoggerComponentType,
    LoggerLevelType,
    LoggerTypeType,
    PermissionType,
    SoftwareToUpdateType,
    TelemetryType,
    UpdateAgentLogLevelType,
    UpdateTargetsArchitectureType,
    UpdateTargetsOperatingSystemType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateRoleToGroupRequestRequestTypeDef",
    "AssociateRoleToGroupResponseTypeDef",
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "BulkDeploymentMetricsTypeDef",
    "BulkDeploymentResultTypeDef",
    "BulkDeploymentTypeDef",
    "ConnectivityInfoTypeDef",
    "ConnectorDefinitionVersionTypeDef",
    "ConnectorTypeDef",
    "CoreDefinitionVersionTypeDef",
    "CoreTypeDef",
    "CreateConnectorDefinitionRequestRequestTypeDef",
    "CreateConnectorDefinitionResponseTypeDef",
    "CreateConnectorDefinitionVersionRequestRequestTypeDef",
    "CreateConnectorDefinitionVersionResponseTypeDef",
    "CreateCoreDefinitionRequestRequestTypeDef",
    "CreateCoreDefinitionResponseTypeDef",
    "CreateCoreDefinitionVersionRequestRequestTypeDef",
    "CreateCoreDefinitionVersionResponseTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDeviceDefinitionRequestRequestTypeDef",
    "CreateDeviceDefinitionResponseTypeDef",
    "CreateDeviceDefinitionVersionRequestRequestTypeDef",
    "CreateDeviceDefinitionVersionResponseTypeDef",
    "CreateFunctionDefinitionRequestRequestTypeDef",
    "CreateFunctionDefinitionResponseTypeDef",
    "CreateFunctionDefinitionVersionRequestRequestTypeDef",
    "CreateFunctionDefinitionVersionResponseTypeDef",
    "CreateGroupCertificateAuthorityRequestRequestTypeDef",
    "CreateGroupCertificateAuthorityResponseTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateGroupVersionRequestRequestTypeDef",
    "CreateGroupVersionResponseTypeDef",
    "CreateLoggerDefinitionRequestRequestTypeDef",
    "CreateLoggerDefinitionResponseTypeDef",
    "CreateLoggerDefinitionVersionRequestRequestTypeDef",
    "CreateLoggerDefinitionVersionResponseTypeDef",
    "CreateResourceDefinitionRequestRequestTypeDef",
    "CreateResourceDefinitionResponseTypeDef",
    "CreateResourceDefinitionVersionRequestRequestTypeDef",
    "CreateResourceDefinitionVersionResponseTypeDef",
    "CreateSoftwareUpdateJobRequestRequestTypeDef",
    "CreateSoftwareUpdateJobResponseTypeDef",
    "CreateSubscriptionDefinitionRequestRequestTypeDef",
    "CreateSubscriptionDefinitionResponseTypeDef",
    "CreateSubscriptionDefinitionVersionRequestRequestTypeDef",
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    "DefinitionInformationTypeDef",
    "DeleteConnectorDefinitionRequestRequestTypeDef",
    "DeleteCoreDefinitionRequestRequestTypeDef",
    "DeleteDeviceDefinitionRequestRequestTypeDef",
    "DeleteFunctionDefinitionRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteLoggerDefinitionRequestRequestTypeDef",
    "DeleteResourceDefinitionRequestRequestTypeDef",
    "DeleteSubscriptionDefinitionRequestRequestTypeDef",
    "DeploymentTypeDef",
    "DeviceDefinitionVersionTypeDef",
    "DeviceTypeDef",
    "DisassociateRoleFromGroupRequestRequestTypeDef",
    "DisassociateRoleFromGroupResponseTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "ErrorDetailTypeDef",
    "FunctionConfigurationEnvironmentTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionDefaultConfigTypeDef",
    "FunctionDefaultExecutionConfigTypeDef",
    "FunctionDefinitionVersionTypeDef",
    "FunctionExecutionConfigTypeDef",
    "FunctionRunAsConfigTypeDef",
    "FunctionTypeDef",
    "GetAssociatedRoleRequestRequestTypeDef",
    "GetAssociatedRoleResponseTypeDef",
    "GetBulkDeploymentStatusRequestRequestTypeDef",
    "GetBulkDeploymentStatusResponseTypeDef",
    "GetConnectivityInfoRequestRequestTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "GetConnectorDefinitionRequestRequestTypeDef",
    "GetConnectorDefinitionResponseTypeDef",
    "GetConnectorDefinitionVersionRequestRequestTypeDef",
    "GetConnectorDefinitionVersionResponseTypeDef",
    "GetCoreDefinitionRequestRequestTypeDef",
    "GetCoreDefinitionResponseTypeDef",
    "GetCoreDefinitionVersionRequestRequestTypeDef",
    "GetCoreDefinitionVersionResponseTypeDef",
    "GetDeploymentStatusRequestRequestTypeDef",
    "GetDeploymentStatusResponseTypeDef",
    "GetDeviceDefinitionRequestRequestTypeDef",
    "GetDeviceDefinitionResponseTypeDef",
    "GetDeviceDefinitionVersionRequestRequestTypeDef",
    "GetDeviceDefinitionVersionResponseTypeDef",
    "GetFunctionDefinitionRequestRequestTypeDef",
    "GetFunctionDefinitionResponseTypeDef",
    "GetFunctionDefinitionVersionRequestRequestTypeDef",
    "GetFunctionDefinitionVersionResponseTypeDef",
    "GetGroupCertificateAuthorityRequestRequestTypeDef",
    "GetGroupCertificateAuthorityResponseTypeDef",
    "GetGroupCertificateConfigurationRequestRequestTypeDef",
    "GetGroupCertificateConfigurationResponseTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetGroupVersionRequestRequestTypeDef",
    "GetGroupVersionResponseTypeDef",
    "GetLoggerDefinitionRequestRequestTypeDef",
    "GetLoggerDefinitionResponseTypeDef",
    "GetLoggerDefinitionVersionRequestRequestTypeDef",
    "GetLoggerDefinitionVersionResponseTypeDef",
    "GetResourceDefinitionRequestRequestTypeDef",
    "GetResourceDefinitionResponseTypeDef",
    "GetResourceDefinitionVersionRequestRequestTypeDef",
    "GetResourceDefinitionVersionResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "GetSubscriptionDefinitionRequestRequestTypeDef",
    "GetSubscriptionDefinitionResponseTypeDef",
    "GetSubscriptionDefinitionVersionRequestRequestTypeDef",
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    "GetThingRuntimeConfigurationRequestRequestTypeDef",
    "GetThingRuntimeConfigurationResponseTypeDef",
    "GroupCertificateAuthorityPropertiesTypeDef",
    "GroupInformationTypeDef",
    "GroupOwnerSettingTypeDef",
    "GroupVersionTypeDef",
    "ListBulkDeploymentDetailedReportsRequestRequestTypeDef",
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    "ListBulkDeploymentsRequestRequestTypeDef",
    "ListBulkDeploymentsResponseTypeDef",
    "ListConnectorDefinitionVersionsRequestRequestTypeDef",
    "ListConnectorDefinitionVersionsResponseTypeDef",
    "ListConnectorDefinitionsRequestRequestTypeDef",
    "ListConnectorDefinitionsResponseTypeDef",
    "ListCoreDefinitionVersionsRequestRequestTypeDef",
    "ListCoreDefinitionVersionsResponseTypeDef",
    "ListCoreDefinitionsRequestRequestTypeDef",
    "ListCoreDefinitionsResponseTypeDef",
    "ListDeploymentsRequestRequestTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListDeviceDefinitionVersionsRequestRequestTypeDef",
    "ListDeviceDefinitionVersionsResponseTypeDef",
    "ListDeviceDefinitionsRequestRequestTypeDef",
    "ListDeviceDefinitionsResponseTypeDef",
    "ListFunctionDefinitionVersionsRequestRequestTypeDef",
    "ListFunctionDefinitionVersionsResponseTypeDef",
    "ListFunctionDefinitionsRequestRequestTypeDef",
    "ListFunctionDefinitionsResponseTypeDef",
    "ListGroupCertificateAuthoritiesRequestRequestTypeDef",
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    "ListGroupVersionsRequestRequestTypeDef",
    "ListGroupVersionsResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListLoggerDefinitionVersionsRequestRequestTypeDef",
    "ListLoggerDefinitionVersionsResponseTypeDef",
    "ListLoggerDefinitionsRequestRequestTypeDef",
    "ListLoggerDefinitionsResponseTypeDef",
    "ListResourceDefinitionVersionsRequestRequestTypeDef",
    "ListResourceDefinitionVersionsResponseTypeDef",
    "ListResourceDefinitionsRequestRequestTypeDef",
    "ListResourceDefinitionsResponseTypeDef",
    "ListSubscriptionDefinitionVersionsRequestRequestTypeDef",
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    "ListSubscriptionDefinitionsRequestRequestTypeDef",
    "ListSubscriptionDefinitionsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocalDeviceResourceDataTypeDef",
    "LocalVolumeResourceDataTypeDef",
    "LoggerDefinitionVersionTypeDef",
    "LoggerTypeDef",
    "PaginatorConfigTypeDef",
    "ResetDeploymentsRequestRequestTypeDef",
    "ResetDeploymentsResponseTypeDef",
    "ResourceAccessPolicyTypeDef",
    "ResourceDataContainerTypeDef",
    "ResourceDefinitionVersionTypeDef",
    "ResourceDownloadOwnerSettingTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3MachineLearningModelResourceDataTypeDef",
    "SageMakerMachineLearningModelResourceDataTypeDef",
    "SecretsManagerSecretResourceDataTypeDef",
    "StartBulkDeploymentRequestRequestTypeDef",
    "StartBulkDeploymentResponseTypeDef",
    "StopBulkDeploymentRequestRequestTypeDef",
    "SubscriptionDefinitionVersionTypeDef",
    "SubscriptionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TelemetryConfigurationTypeDef",
    "TelemetryConfigurationUpdateTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectivityInfoRequestRequestTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
    "UpdateConnectorDefinitionRequestRequestTypeDef",
    "UpdateCoreDefinitionRequestRequestTypeDef",
    "UpdateDeviceDefinitionRequestRequestTypeDef",
    "UpdateFunctionDefinitionRequestRequestTypeDef",
    "UpdateGroupCertificateConfigurationRequestRequestTypeDef",
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateLoggerDefinitionRequestRequestTypeDef",
    "UpdateResourceDefinitionRequestRequestTypeDef",
    "UpdateSubscriptionDefinitionRequestRequestTypeDef",
    "UpdateThingRuntimeConfigurationRequestRequestTypeDef",
    "VersionInformationTypeDef",
)

AssociateRoleToGroupRequestRequestTypeDef = TypedDict(
    "AssociateRoleToGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "RoleArn": str,
    },
)

AssociateRoleToGroupResponseTypeDef = TypedDict(
    "AssociateRoleToGroupResponseTypeDef",
    {
        "AssociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateServiceRoleToAccountRequestRequestTypeDef = TypedDict(
    "AssociateServiceRoleToAccountRequestRequestTypeDef",
    {
        "RoleArn": str,
    },
)

AssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "AssociateServiceRoleToAccountResponseTypeDef",
    {
        "AssociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BulkDeploymentMetricsTypeDef = TypedDict(
    "BulkDeploymentMetricsTypeDef",
    {
        "InvalidInputRecords": int,
        "RecordsProcessed": int,
        "RetryAttempts": int,
    },
    total=False,
)

BulkDeploymentResultTypeDef = TypedDict(
    "BulkDeploymentResultTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentType": DeploymentTypeType,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "GroupArn": str,
    },
    total=False,
)

BulkDeploymentTypeDef = TypedDict(
    "BulkDeploymentTypeDef",
    {
        "BulkDeploymentArn": str,
        "BulkDeploymentId": str,
        "CreatedAt": str,
    },
    total=False,
)

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {
        "HostAddress": str,
        "Id": str,
        "Metadata": str,
        "PortNumber": int,
    },
    total=False,
)

ConnectorDefinitionVersionTypeDef = TypedDict(
    "ConnectorDefinitionVersionTypeDef",
    {
        "Connectors": List["ConnectorTypeDef"],
    },
    total=False,
)

_RequiredConnectorTypeDef = TypedDict(
    "_RequiredConnectorTypeDef",
    {
        "ConnectorArn": str,
        "Id": str,
    },
)
_OptionalConnectorTypeDef = TypedDict(
    "_OptionalConnectorTypeDef",
    {
        "Parameters": Dict[str, str],
    },
    total=False,
)

class ConnectorTypeDef(_RequiredConnectorTypeDef, _OptionalConnectorTypeDef):
    pass

CoreDefinitionVersionTypeDef = TypedDict(
    "CoreDefinitionVersionTypeDef",
    {
        "Cores": List["CoreTypeDef"],
    },
    total=False,
)

_RequiredCoreTypeDef = TypedDict(
    "_RequiredCoreTypeDef",
    {
        "CertificateArn": str,
        "Id": str,
        "ThingArn": str,
    },
)
_OptionalCoreTypeDef = TypedDict(
    "_OptionalCoreTypeDef",
    {
        "SyncShadow": bool,
    },
    total=False,
)

class CoreTypeDef(_RequiredCoreTypeDef, _OptionalCoreTypeDef):
    pass

CreateConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "CreateConnectorDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "ConnectorDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateConnectorDefinitionResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateConnectorDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectorDefinitionVersionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)
_OptionalCreateConnectorDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectorDefinitionVersionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "Connectors": List["ConnectorTypeDef"],
    },
    total=False,
)

class CreateConnectorDefinitionVersionRequestRequestTypeDef(
    _RequiredCreateConnectorDefinitionVersionRequestRequestTypeDef,
    _OptionalCreateConnectorDefinitionVersionRequestRequestTypeDef,
):
    pass

CreateConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCoreDefinitionRequestRequestTypeDef = TypedDict(
    "CreateCoreDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "CoreDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateCoreDefinitionResponseTypeDef = TypedDict(
    "CreateCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCoreDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCoreDefinitionVersionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)
_OptionalCreateCoreDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCoreDefinitionVersionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "Cores": List["CoreTypeDef"],
    },
    total=False,
)

class CreateCoreDefinitionVersionRequestRequestTypeDef(
    _RequiredCreateCoreDefinitionVersionRequestRequestTypeDef,
    _OptionalCreateCoreDefinitionVersionRequestRequestTypeDef,
):
    pass

CreateCoreDefinitionVersionResponseTypeDef = TypedDict(
    "CreateCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeploymentRequestRequestTypeDef",
    {
        "DeploymentType": DeploymentTypeType,
        "GroupId": str,
    },
)
_OptionalCreateDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeploymentRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "DeploymentId": str,
        "GroupVersionId": str,
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
        "DeploymentArn": str,
        "DeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "CreateDeviceDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "DeviceDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateDeviceDefinitionResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDeviceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeviceDefinitionVersionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)
_OptionalCreateDeviceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeviceDefinitionVersionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "Devices": List["DeviceTypeDef"],
    },
    total=False,
)

class CreateDeviceDefinitionVersionRequestRequestTypeDef(
    _RequiredCreateDeviceDefinitionVersionRequestRequestTypeDef,
    _OptionalCreateDeviceDefinitionVersionRequestRequestTypeDef,
):
    pass

CreateDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "CreateFunctionDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "FunctionDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateFunctionDefinitionResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFunctionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionDefinitionVersionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)
_OptionalCreateFunctionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionDefinitionVersionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "DefaultConfig": "FunctionDefaultConfigTypeDef",
        "Functions": List["FunctionTypeDef"],
    },
    total=False,
)

class CreateFunctionDefinitionVersionRequestRequestTypeDef(
    _RequiredCreateFunctionDefinitionVersionRequestRequestTypeDef,
    _OptionalCreateFunctionDefinitionVersionRequestRequestTypeDef,
):
    pass

CreateFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupCertificateAuthorityRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalCreateGroupCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupCertificateAuthorityRequestRequestTypeDef",
    {
        "AmznClientToken": str,
    },
    total=False,
)

class CreateGroupCertificateAuthorityRequestRequestTypeDef(
    _RequiredCreateGroupCertificateAuthorityRequestRequestTypeDef,
    _OptionalCreateGroupCertificateAuthorityRequestRequestTypeDef,
):
    pass

CreateGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "GroupVersionTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateGroupRequestRequestTypeDef(
    _RequiredCreateGroupRequestRequestTypeDef, _OptionalCreateGroupRequestRequestTypeDef
):
    pass

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupVersionRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalCreateGroupVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupVersionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)

class CreateGroupVersionRequestRequestTypeDef(
    _RequiredCreateGroupVersionRequestRequestTypeDef,
    _OptionalCreateGroupVersionRequestRequestTypeDef,
):
    pass

CreateGroupVersionResponseTypeDef = TypedDict(
    "CreateGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "CreateLoggerDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "LoggerDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateLoggerDefinitionResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoggerDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLoggerDefinitionVersionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)
_OptionalCreateLoggerDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLoggerDefinitionVersionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "Loggers": List["LoggerTypeDef"],
    },
    total=False,
)

class CreateLoggerDefinitionVersionRequestRequestTypeDef(
    _RequiredCreateLoggerDefinitionVersionRequestRequestTypeDef,
    _OptionalCreateLoggerDefinitionVersionRequestRequestTypeDef,
):
    pass

CreateLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceDefinitionRequestRequestTypeDef = TypedDict(
    "CreateResourceDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "ResourceDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateResourceDefinitionResponseTypeDef = TypedDict(
    "CreateResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResourceDefinitionVersionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)
_OptionalCreateResourceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResourceDefinitionVersionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "Resources": List["ResourceTypeDef"],
    },
    total=False,
)

class CreateResourceDefinitionVersionRequestRequestTypeDef(
    _RequiredCreateResourceDefinitionVersionRequestRequestTypeDef,
    _OptionalCreateResourceDefinitionVersionRequestRequestTypeDef,
):
    pass

CreateResourceDefinitionVersionResponseTypeDef = TypedDict(
    "CreateResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSoftwareUpdateJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSoftwareUpdateJobRequestRequestTypeDef",
    {
        "S3UrlSignerRole": str,
        "SoftwareToUpdate": SoftwareToUpdateType,
        "UpdateTargets": List[str],
        "UpdateTargetsArchitecture": UpdateTargetsArchitectureType,
        "UpdateTargetsOperatingSystem": UpdateTargetsOperatingSystemType,
    },
)
_OptionalCreateSoftwareUpdateJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSoftwareUpdateJobRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "UpdateAgentLogLevel": UpdateAgentLogLevelType,
    },
    total=False,
)

class CreateSoftwareUpdateJobRequestRequestTypeDef(
    _RequiredCreateSoftwareUpdateJobRequestRequestTypeDef,
    _OptionalCreateSoftwareUpdateJobRequestRequestTypeDef,
):
    pass

CreateSoftwareUpdateJobResponseTypeDef = TypedDict(
    "CreateSoftwareUpdateJobResponseTypeDef",
    {
        "IotJobArn": str,
        "IotJobId": str,
        "PlatformSoftwareVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "CreateSubscriptionDefinitionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "InitialVersion": "SubscriptionDefinitionVersionTypeDef",
        "Name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSubscriptionDefinitionResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubscriptionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSubscriptionDefinitionVersionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)
_OptionalCreateSubscriptionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSubscriptionDefinitionVersionRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "Subscriptions": List["SubscriptionTypeDef"],
    },
    total=False,
)

class CreateSubscriptionDefinitionVersionRequestRequestTypeDef(
    _RequiredCreateSubscriptionDefinitionVersionRequestRequestTypeDef,
    _OptionalCreateSubscriptionDefinitionVersionRequestRequestTypeDef,
):
    pass

CreateSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefinitionInformationTypeDef = TypedDict(
    "DefinitionInformationTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DeleteConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)

DeleteCoreDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)

DeleteDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)

DeleteFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

DeleteLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)

DeleteResourceDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)

DeleteSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": DeploymentTypeType,
        "GroupArn": str,
    },
    total=False,
)

DeviceDefinitionVersionTypeDef = TypedDict(
    "DeviceDefinitionVersionTypeDef",
    {
        "Devices": List["DeviceTypeDef"],
    },
    total=False,
)

_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef",
    {
        "CertificateArn": str,
        "Id": str,
        "ThingArn": str,
    },
)
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {
        "SyncShadow": bool,
    },
    total=False,
)

class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass

DisassociateRoleFromGroupRequestRequestTypeDef = TypedDict(
    "DisassociateRoleFromGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

DisassociateRoleFromGroupResponseTypeDef = TypedDict(
    "DisassociateRoleFromGroupResponseTypeDef",
    {
        "DisassociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    {
        "DisassociatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "DetailedErrorCode": str,
        "DetailedErrorMessage": str,
    },
    total=False,
)

FunctionConfigurationEnvironmentTypeDef = TypedDict(
    "FunctionConfigurationEnvironmentTypeDef",
    {
        "AccessSysfs": bool,
        "Execution": "FunctionExecutionConfigTypeDef",
        "ResourceAccessPolicies": List["ResourceAccessPolicyTypeDef"],
        "Variables": Dict[str, str],
    },
    total=False,
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "EncodingType": EncodingTypeType,
        "Environment": "FunctionConfigurationEnvironmentTypeDef",
        "ExecArgs": str,
        "Executable": str,
        "MemorySize": int,
        "Pinned": bool,
        "Timeout": int,
    },
    total=False,
)

FunctionDefaultConfigTypeDef = TypedDict(
    "FunctionDefaultConfigTypeDef",
    {
        "Execution": "FunctionDefaultExecutionConfigTypeDef",
    },
    total=False,
)

FunctionDefaultExecutionConfigTypeDef = TypedDict(
    "FunctionDefaultExecutionConfigTypeDef",
    {
        "IsolationMode": FunctionIsolationModeType,
        "RunAs": "FunctionRunAsConfigTypeDef",
    },
    total=False,
)

FunctionDefinitionVersionTypeDef = TypedDict(
    "FunctionDefinitionVersionTypeDef",
    {
        "DefaultConfig": "FunctionDefaultConfigTypeDef",
        "Functions": List["FunctionTypeDef"],
    },
    total=False,
)

FunctionExecutionConfigTypeDef = TypedDict(
    "FunctionExecutionConfigTypeDef",
    {
        "IsolationMode": FunctionIsolationModeType,
        "RunAs": "FunctionRunAsConfigTypeDef",
    },
    total=False,
)

FunctionRunAsConfigTypeDef = TypedDict(
    "FunctionRunAsConfigTypeDef",
    {
        "Gid": int,
        "Uid": int,
    },
    total=False,
)

_RequiredFunctionTypeDef = TypedDict(
    "_RequiredFunctionTypeDef",
    {
        "Id": str,
    },
)
_OptionalFunctionTypeDef = TypedDict(
    "_OptionalFunctionTypeDef",
    {
        "FunctionArn": str,
        "FunctionConfiguration": "FunctionConfigurationTypeDef",
    },
    total=False,
)

class FunctionTypeDef(_RequiredFunctionTypeDef, _OptionalFunctionTypeDef):
    pass

GetAssociatedRoleRequestRequestTypeDef = TypedDict(
    "GetAssociatedRoleRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetAssociatedRoleResponseTypeDef = TypedDict(
    "GetAssociatedRoleResponseTypeDef",
    {
        "AssociatedAt": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBulkDeploymentStatusRequestRequestTypeDef = TypedDict(
    "GetBulkDeploymentStatusRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)

GetBulkDeploymentStatusResponseTypeDef = TypedDict(
    "GetBulkDeploymentStatusResponseTypeDef",
    {
        "BulkDeploymentMetrics": "BulkDeploymentMetricsTypeDef",
        "BulkDeploymentStatus": BulkDeploymentStatusType,
        "CreatedAt": str,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectivityInfoRequestRequestTypeDef = TypedDict(
    "GetConnectivityInfoRequestRequestTypeDef",
    {
        "ThingName": str,
    },
)

GetConnectivityInfoResponseTypeDef = TypedDict(
    "GetConnectivityInfoResponseTypeDef",
    {
        "ConnectivityInfo": List["ConnectivityInfoTypeDef"],
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "GetConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)

GetConnectorDefinitionResponseTypeDef = TypedDict(
    "GetConnectorDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConnectorDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredGetConnectorDefinitionVersionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
        "ConnectorDefinitionVersionId": str,
    },
)
_OptionalGetConnectorDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalGetConnectorDefinitionVersionRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetConnectorDefinitionVersionRequestRequestTypeDef(
    _RequiredGetConnectorDefinitionVersionRequestRequestTypeDef,
    _OptionalGetConnectorDefinitionVersionRequestRequestTypeDef,
):
    pass

GetConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "GetConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "ConnectorDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDefinitionRequestRequestTypeDef = TypedDict(
    "GetCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)

GetCoreDefinitionResponseTypeDef = TypedDict(
    "GetCoreDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetCoreDefinitionVersionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
        "CoreDefinitionVersionId": str,
    },
)

GetCoreDefinitionVersionResponseTypeDef = TypedDict(
    "GetCoreDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "CoreDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeploymentStatusRequestRequestTypeDef = TypedDict(
    "GetDeploymentStatusRequestRequestTypeDef",
    {
        "DeploymentId": str,
        "GroupId": str,
    },
)

GetDeploymentStatusResponseTypeDef = TypedDict(
    "GetDeploymentStatusResponseTypeDef",
    {
        "DeploymentStatus": str,
        "DeploymentType": DeploymentTypeType,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "UpdatedAt": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "GetDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)

GetDeviceDefinitionResponseTypeDef = TypedDict(
    "GetDeviceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeviceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredGetDeviceDefinitionVersionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
        "DeviceDefinitionVersionId": str,
    },
)
_OptionalGetDeviceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalGetDeviceDefinitionVersionRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetDeviceDefinitionVersionRequestRequestTypeDef(
    _RequiredGetDeviceDefinitionVersionRequestRequestTypeDef,
    _OptionalGetDeviceDefinitionVersionRequestRequestTypeDef,
):
    pass

GetDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "GetDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "DeviceDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "GetFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)

GetFunctionDefinitionResponseTypeDef = TypedDict(
    "GetFunctionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFunctionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredGetFunctionDefinitionVersionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
        "FunctionDefinitionVersionId": str,
    },
)
_OptionalGetFunctionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalGetFunctionDefinitionVersionRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetFunctionDefinitionVersionRequestRequestTypeDef(
    _RequiredGetFunctionDefinitionVersionRequestRequestTypeDef,
    _OptionalGetFunctionDefinitionVersionRequestRequestTypeDef,
):
    pass

GetFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "GetFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "FunctionDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "GetGroupCertificateAuthorityRequestRequestTypeDef",
    {
        "CertificateAuthorityId": str,
        "GroupId": str,
    },
)

GetGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "GetGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupCertificateConfigurationRequestRequestTypeDef = TypedDict(
    "GetGroupCertificateConfigurationRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "GetGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupVersionRequestRequestTypeDef = TypedDict(
    "GetGroupVersionRequestRequestTypeDef",
    {
        "GroupId": str,
        "GroupVersionId": str,
    },
)

GetGroupVersionResponseTypeDef = TypedDict(
    "GetGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "GroupVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "GetLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)

GetLoggerDefinitionResponseTypeDef = TypedDict(
    "GetLoggerDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLoggerDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredGetLoggerDefinitionVersionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
        "LoggerDefinitionVersionId": str,
    },
)
_OptionalGetLoggerDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalGetLoggerDefinitionVersionRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetLoggerDefinitionVersionRequestRequestTypeDef(
    _RequiredGetLoggerDefinitionVersionRequestRequestTypeDef,
    _OptionalGetLoggerDefinitionVersionRequestRequestTypeDef,
):
    pass

GetLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "GetLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "LoggerDefinitionVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceDefinitionRequestRequestTypeDef = TypedDict(
    "GetResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)

GetResourceDefinitionResponseTypeDef = TypedDict(
    "GetResourceDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceDefinitionVersionRequestRequestTypeDef = TypedDict(
    "GetResourceDefinitionVersionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
        "ResourceDefinitionVersionId": str,
    },
)

GetResourceDefinitionVersionResponseTypeDef = TypedDict(
    "GetResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "ResourceDefinitionVersionTypeDef",
        "Id": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRoleForAccountResponseTypeDef = TypedDict(
    "GetServiceRoleForAccountResponseTypeDef",
    {
        "AssociatedAt": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "GetSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)

GetSubscriptionDefinitionResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSubscriptionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_RequiredGetSubscriptionDefinitionVersionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
        "SubscriptionDefinitionVersionId": str,
    },
)
_OptionalGetSubscriptionDefinitionVersionRequestRequestTypeDef = TypedDict(
    "_OptionalGetSubscriptionDefinitionVersionRequestRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class GetSubscriptionDefinitionVersionRequestRequestTypeDef(
    _RequiredGetSubscriptionDefinitionVersionRequestRequestTypeDef,
    _OptionalGetSubscriptionDefinitionVersionRequestRequestTypeDef,
):
    pass

GetSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "SubscriptionDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetThingRuntimeConfigurationRequestRequestTypeDef = TypedDict(
    "GetThingRuntimeConfigurationRequestRequestTypeDef",
    {
        "ThingName": str,
    },
)

GetThingRuntimeConfigurationResponseTypeDef = TypedDict(
    "GetThingRuntimeConfigurationResponseTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupCertificateAuthorityPropertiesTypeDef = TypedDict(
    "GroupCertificateAuthorityPropertiesTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
    },
    total=False,
)

GroupInformationTypeDef = TypedDict(
    "GroupInformationTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "LastUpdatedTimestamp": str,
        "LatestVersion": str,
        "LatestVersionArn": str,
        "Name": str,
    },
    total=False,
)

GroupOwnerSettingTypeDef = TypedDict(
    "GroupOwnerSettingTypeDef",
    {
        "AutoAddGroupOwner": bool,
        "GroupOwner": str,
    },
    total=False,
)

GroupVersionTypeDef = TypedDict(
    "GroupVersionTypeDef",
    {
        "ConnectorDefinitionVersionArn": str,
        "CoreDefinitionVersionArn": str,
        "DeviceDefinitionVersionArn": str,
        "FunctionDefinitionVersionArn": str,
        "LoggerDefinitionVersionArn": str,
        "ResourceDefinitionVersionArn": str,
        "SubscriptionDefinitionVersionArn": str,
    },
    total=False,
)

_RequiredListBulkDeploymentDetailedReportsRequestRequestTypeDef = TypedDict(
    "_RequiredListBulkDeploymentDetailedReportsRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)
_OptionalListBulkDeploymentDetailedReportsRequestRequestTypeDef = TypedDict(
    "_OptionalListBulkDeploymentDetailedReportsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListBulkDeploymentDetailedReportsRequestRequestTypeDef(
    _RequiredListBulkDeploymentDetailedReportsRequestRequestTypeDef,
    _OptionalListBulkDeploymentDetailedReportsRequestRequestTypeDef,
):
    pass

ListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    {
        "Deployments": List["BulkDeploymentResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBulkDeploymentsRequestRequestTypeDef = TypedDict(
    "ListBulkDeploymentsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListBulkDeploymentsResponseTypeDef = TypedDict(
    "ListBulkDeploymentsResponseTypeDef",
    {
        "BulkDeployments": List["BulkDeploymentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListConnectorDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListConnectorDefinitionVersionsRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)
_OptionalListConnectorDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListConnectorDefinitionVersionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListConnectorDefinitionVersionsRequestRequestTypeDef(
    _RequiredListConnectorDefinitionVersionsRequestRequestTypeDef,
    _OptionalListConnectorDefinitionVersionsRequestRequestTypeDef,
):
    pass

ListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectorDefinitionsRequestRequestTypeDef = TypedDict(
    "ListConnectorDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListConnectorDefinitionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCoreDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListCoreDefinitionVersionsRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)
_OptionalListCoreDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListCoreDefinitionVersionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListCoreDefinitionVersionsRequestRequestTypeDef(
    _RequiredListCoreDefinitionVersionsRequestRequestTypeDef,
    _OptionalListCoreDefinitionVersionsRequestRequestTypeDef,
):
    pass

ListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreDefinitionsRequestRequestTypeDef = TypedDict(
    "ListCoreDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListCoreDefinitionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeploymentsRequestRequestTypeDef = TypedDict(
    "_RequiredListDeploymentsRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalListDeploymentsRequestRequestTypeDef = TypedDict(
    "_OptionalListDeploymentsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListDeploymentsRequestRequestTypeDef(
    _RequiredListDeploymentsRequestRequestTypeDef, _OptionalListDeploymentsRequestRequestTypeDef
):
    pass

ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {
        "Deployments": List["DeploymentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDeviceDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDeviceDefinitionVersionsRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)
_OptionalListDeviceDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDeviceDefinitionVersionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListDeviceDefinitionVersionsRequestRequestTypeDef(
    _RequiredListDeviceDefinitionVersionsRequestRequestTypeDef,
    _OptionalListDeviceDefinitionVersionsRequestRequestTypeDef,
):
    pass

ListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceDefinitionsRequestRequestTypeDef = TypedDict(
    "ListDeviceDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListDeviceDefinitionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListFunctionDefinitionVersionsRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)
_OptionalListFunctionDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListFunctionDefinitionVersionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListFunctionDefinitionVersionsRequestRequestTypeDef(
    _RequiredListFunctionDefinitionVersionsRequestRequestTypeDef,
    _OptionalListFunctionDefinitionVersionsRequestRequestTypeDef,
):
    pass

ListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionDefinitionsRequestRequestTypeDef = TypedDict(
    "ListFunctionDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListFunctionDefinitionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

ListGroupCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    {
        "GroupCertificateAuthorities": List["GroupCertificateAuthorityPropertiesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupVersionsRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalListGroupVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupVersionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListGroupVersionsRequestRequestTypeDef(
    _RequiredListGroupVersionsRequestRequestTypeDef, _OptionalListGroupVersionsRequestRequestTypeDef
):
    pass

ListGroupVersionsResponseTypeDef = TypedDict(
    "ListGroupVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLoggerDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLoggerDefinitionVersionsRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)
_OptionalListLoggerDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLoggerDefinitionVersionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListLoggerDefinitionVersionsRequestRequestTypeDef(
    _RequiredListLoggerDefinitionVersionsRequestRequestTypeDef,
    _OptionalListLoggerDefinitionVersionsRequestRequestTypeDef,
):
    pass

ListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoggerDefinitionsRequestRequestTypeDef = TypedDict(
    "ListLoggerDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListLoggerDefinitionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceDefinitionVersionsRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)
_OptionalListResourceDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceDefinitionVersionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListResourceDefinitionVersionsRequestRequestTypeDef(
    _RequiredListResourceDefinitionVersionsRequestRequestTypeDef,
    _OptionalListResourceDefinitionVersionsRequestRequestTypeDef,
):
    pass

ListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceDefinitionsRequestRequestTypeDef = TypedDict(
    "ListResourceDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListResourceDefinitionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSubscriptionDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSubscriptionDefinitionVersionsRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)
_OptionalListSubscriptionDefinitionVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSubscriptionDefinitionVersionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

class ListSubscriptionDefinitionVersionsRequestRequestTypeDef(
    _RequiredListSubscriptionDefinitionVersionsRequestRequestTypeDef,
    _OptionalListSubscriptionDefinitionVersionsRequestRequestTypeDef,
):
    pass

ListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Versions": List["VersionInformationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscriptionDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSubscriptionDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": str,
        "NextToken": str,
    },
    total=False,
)

ListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionsResponseTypeDef",
    {
        "Definitions": List["DefinitionInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalDeviceResourceDataTypeDef = TypedDict(
    "LocalDeviceResourceDataTypeDef",
    {
        "GroupOwnerSetting": "GroupOwnerSettingTypeDef",
        "SourcePath": str,
    },
    total=False,
)

LocalVolumeResourceDataTypeDef = TypedDict(
    "LocalVolumeResourceDataTypeDef",
    {
        "DestinationPath": str,
        "GroupOwnerSetting": "GroupOwnerSettingTypeDef",
        "SourcePath": str,
    },
    total=False,
)

LoggerDefinitionVersionTypeDef = TypedDict(
    "LoggerDefinitionVersionTypeDef",
    {
        "Loggers": List["LoggerTypeDef"],
    },
    total=False,
)

_RequiredLoggerTypeDef = TypedDict(
    "_RequiredLoggerTypeDef",
    {
        "Component": LoggerComponentType,
        "Id": str,
        "Level": LoggerLevelType,
        "Type": LoggerTypeType,
    },
)
_OptionalLoggerTypeDef = TypedDict(
    "_OptionalLoggerTypeDef",
    {
        "Space": int,
    },
    total=False,
)

class LoggerTypeDef(_RequiredLoggerTypeDef, _OptionalLoggerTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredResetDeploymentsRequestRequestTypeDef = TypedDict(
    "_RequiredResetDeploymentsRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalResetDeploymentsRequestRequestTypeDef = TypedDict(
    "_OptionalResetDeploymentsRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "Force": bool,
    },
    total=False,
)

class ResetDeploymentsRequestRequestTypeDef(
    _RequiredResetDeploymentsRequestRequestTypeDef, _OptionalResetDeploymentsRequestRequestTypeDef
):
    pass

ResetDeploymentsResponseTypeDef = TypedDict(
    "ResetDeploymentsResponseTypeDef",
    {
        "DeploymentArn": str,
        "DeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResourceAccessPolicyTypeDef = TypedDict(
    "_RequiredResourceAccessPolicyTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalResourceAccessPolicyTypeDef = TypedDict(
    "_OptionalResourceAccessPolicyTypeDef",
    {
        "Permission": PermissionType,
    },
    total=False,
)

class ResourceAccessPolicyTypeDef(
    _RequiredResourceAccessPolicyTypeDef, _OptionalResourceAccessPolicyTypeDef
):
    pass

ResourceDataContainerTypeDef = TypedDict(
    "ResourceDataContainerTypeDef",
    {
        "LocalDeviceResourceData": "LocalDeviceResourceDataTypeDef",
        "LocalVolumeResourceData": "LocalVolumeResourceDataTypeDef",
        "S3MachineLearningModelResourceData": "S3MachineLearningModelResourceDataTypeDef",
        "SageMakerMachineLearningModelResourceData": "SageMakerMachineLearningModelResourceDataTypeDef",
        "SecretsManagerSecretResourceData": "SecretsManagerSecretResourceDataTypeDef",
    },
    total=False,
)

ResourceDefinitionVersionTypeDef = TypedDict(
    "ResourceDefinitionVersionTypeDef",
    {
        "Resources": List["ResourceTypeDef"],
    },
    total=False,
)

ResourceDownloadOwnerSettingTypeDef = TypedDict(
    "ResourceDownloadOwnerSettingTypeDef",
    {
        "GroupOwner": str,
        "GroupPermission": PermissionType,
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Name": str,
        "ResourceDataContainer": "ResourceDataContainerTypeDef",
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

RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "TelemetryConfiguration": "TelemetryConfigurationTypeDef",
    },
    total=False,
)

S3MachineLearningModelResourceDataTypeDef = TypedDict(
    "S3MachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": "ResourceDownloadOwnerSettingTypeDef",
        "S3Uri": str,
    },
    total=False,
)

SageMakerMachineLearningModelResourceDataTypeDef = TypedDict(
    "SageMakerMachineLearningModelResourceDataTypeDef",
    {
        "DestinationPath": str,
        "OwnerSetting": "ResourceDownloadOwnerSettingTypeDef",
        "SageMakerJobArn": str,
    },
    total=False,
)

SecretsManagerSecretResourceDataTypeDef = TypedDict(
    "SecretsManagerSecretResourceDataTypeDef",
    {
        "ARN": str,
        "AdditionalStagingLabelsToDownload": List[str],
    },
    total=False,
)

_RequiredStartBulkDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredStartBulkDeploymentRequestRequestTypeDef",
    {
        "ExecutionRoleArn": str,
        "InputFileUri": str,
    },
)
_OptionalStartBulkDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalStartBulkDeploymentRequestRequestTypeDef",
    {
        "AmznClientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class StartBulkDeploymentRequestRequestTypeDef(
    _RequiredStartBulkDeploymentRequestRequestTypeDef,
    _OptionalStartBulkDeploymentRequestRequestTypeDef,
):
    pass

StartBulkDeploymentResponseTypeDef = TypedDict(
    "StartBulkDeploymentResponseTypeDef",
    {
        "BulkDeploymentArn": str,
        "BulkDeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopBulkDeploymentRequestRequestTypeDef = TypedDict(
    "StopBulkDeploymentRequestRequestTypeDef",
    {
        "BulkDeploymentId": str,
    },
)

SubscriptionDefinitionVersionTypeDef = TypedDict(
    "SubscriptionDefinitionVersionTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
    },
    total=False,
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "Id": str,
        "Source": str,
        "Subject": str,
        "Target": str,
    },
)

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

_RequiredTelemetryConfigurationTypeDef = TypedDict(
    "_RequiredTelemetryConfigurationTypeDef",
    {
        "Telemetry": TelemetryType,
    },
)
_OptionalTelemetryConfigurationTypeDef = TypedDict(
    "_OptionalTelemetryConfigurationTypeDef",
    {
        "ConfigurationSyncStatus": ConfigurationSyncStatusType,
    },
    total=False,
)

class TelemetryConfigurationTypeDef(
    _RequiredTelemetryConfigurationTypeDef, _OptionalTelemetryConfigurationTypeDef
):
    pass

TelemetryConfigurationUpdateTypeDef = TypedDict(
    "TelemetryConfigurationUpdateTypeDef",
    {
        "Telemetry": TelemetryType,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateConnectivityInfoRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectivityInfoRequestRequestTypeDef",
    {
        "ThingName": str,
    },
)
_OptionalUpdateConnectivityInfoRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectivityInfoRequestRequestTypeDef",
    {
        "ConnectivityInfo": List["ConnectivityInfoTypeDef"],
    },
    total=False,
)

class UpdateConnectivityInfoRequestRequestTypeDef(
    _RequiredUpdateConnectivityInfoRequestRequestTypeDef,
    _OptionalUpdateConnectivityInfoRequestRequestTypeDef,
):
    pass

UpdateConnectivityInfoResponseTypeDef = TypedDict(
    "UpdateConnectivityInfoResponseTypeDef",
    {
        "Message": str,
        "Version": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectorDefinitionRequestRequestTypeDef",
    {
        "ConnectorDefinitionId": str,
    },
)
_OptionalUpdateConnectorDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectorDefinitionRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateConnectorDefinitionRequestRequestTypeDef(
    _RequiredUpdateConnectorDefinitionRequestRequestTypeDef,
    _OptionalUpdateConnectorDefinitionRequestRequestTypeDef,
):
    pass

_RequiredUpdateCoreDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCoreDefinitionRequestRequestTypeDef",
    {
        "CoreDefinitionId": str,
    },
)
_OptionalUpdateCoreDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCoreDefinitionRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateCoreDefinitionRequestRequestTypeDef(
    _RequiredUpdateCoreDefinitionRequestRequestTypeDef,
    _OptionalUpdateCoreDefinitionRequestRequestTypeDef,
):
    pass

_RequiredUpdateDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDeviceDefinitionRequestRequestTypeDef",
    {
        "DeviceDefinitionId": str,
    },
)
_OptionalUpdateDeviceDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDeviceDefinitionRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateDeviceDefinitionRequestRequestTypeDef(
    _RequiredUpdateDeviceDefinitionRequestRequestTypeDef,
    _OptionalUpdateDeviceDefinitionRequestRequestTypeDef,
):
    pass

_RequiredUpdateFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionDefinitionRequestRequestTypeDef",
    {
        "FunctionDefinitionId": str,
    },
)
_OptionalUpdateFunctionDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionDefinitionRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateFunctionDefinitionRequestRequestTypeDef(
    _RequiredUpdateFunctionDefinitionRequestRequestTypeDef,
    _OptionalUpdateFunctionDefinitionRequestRequestTypeDef,
):
    pass

_RequiredUpdateGroupCertificateConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupCertificateConfigurationRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalUpdateGroupCertificateConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupCertificateConfigurationRequestRequestTypeDef",
    {
        "CertificateExpiryInMilliseconds": str,
    },
    total=False,
)

class UpdateGroupCertificateConfigurationRequestRequestTypeDef(
    _RequiredUpdateGroupCertificateConfigurationRequestRequestTypeDef,
    _OptionalUpdateGroupCertificateConfigurationRequestRequestTypeDef,
):
    pass

UpdateGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalUpdateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateGroupRequestRequestTypeDef(
    _RequiredUpdateGroupRequestRequestTypeDef, _OptionalUpdateGroupRequestRequestTypeDef
):
    pass

_RequiredUpdateLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLoggerDefinitionRequestRequestTypeDef",
    {
        "LoggerDefinitionId": str,
    },
)
_OptionalUpdateLoggerDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLoggerDefinitionRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateLoggerDefinitionRequestRequestTypeDef(
    _RequiredUpdateLoggerDefinitionRequestRequestTypeDef,
    _OptionalUpdateLoggerDefinitionRequestRequestTypeDef,
):
    pass

_RequiredUpdateResourceDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResourceDefinitionRequestRequestTypeDef",
    {
        "ResourceDefinitionId": str,
    },
)
_OptionalUpdateResourceDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResourceDefinitionRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateResourceDefinitionRequestRequestTypeDef(
    _RequiredUpdateResourceDefinitionRequestRequestTypeDef,
    _OptionalUpdateResourceDefinitionRequestRequestTypeDef,
):
    pass

_RequiredUpdateSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSubscriptionDefinitionRequestRequestTypeDef",
    {
        "SubscriptionDefinitionId": str,
    },
)
_OptionalUpdateSubscriptionDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSubscriptionDefinitionRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateSubscriptionDefinitionRequestRequestTypeDef(
    _RequiredUpdateSubscriptionDefinitionRequestRequestTypeDef,
    _OptionalUpdateSubscriptionDefinitionRequestRequestTypeDef,
):
    pass

_RequiredUpdateThingRuntimeConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateThingRuntimeConfigurationRequestRequestTypeDef",
    {
        "ThingName": str,
    },
)
_OptionalUpdateThingRuntimeConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateThingRuntimeConfigurationRequestRequestTypeDef",
    {
        "TelemetryConfiguration": "TelemetryConfigurationUpdateTypeDef",
    },
    total=False,
)

class UpdateThingRuntimeConfigurationRequestRequestTypeDef(
    _RequiredUpdateThingRuntimeConfigurationRequestRequestTypeDef,
    _OptionalUpdateThingRuntimeConfigurationRequestRequestTypeDef,
):
    pass

VersionInformationTypeDef = TypedDict(
    "VersionInformationTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Id": str,
        "Version": str,
    },
    total=False,
)
