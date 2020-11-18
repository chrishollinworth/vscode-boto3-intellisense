"""
Main interface for greengrass service type definitions.

Usage::

    ```python
    from mypy_boto3_greengrass.type_defs import BulkDeploymentMetricsTypeDef

    data: BulkDeploymentMetricsTypeDef = {...}
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
    "BulkDeploymentMetricsTypeDef",
    "BulkDeploymentResultTypeDef",
    "BulkDeploymentTypeDef",
    "ConnectivityInfoTypeDef",
    "ConnectorDefinitionVersionTypeDef",
    "ConnectorTypeDef",
    "CoreDefinitionVersionTypeDef",
    "CoreTypeDef",
    "DefinitionInformationTypeDef",
    "DeploymentTypeDef",
    "DeviceDefinitionVersionTypeDef",
    "DeviceTypeDef",
    "ErrorDetailTypeDef",
    "FunctionConfigurationEnvironmentTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionDefaultConfigTypeDef",
    "FunctionDefaultExecutionConfigTypeDef",
    "FunctionDefinitionVersionTypeDef",
    "FunctionExecutionConfigTypeDef",
    "FunctionRunAsConfigTypeDef",
    "FunctionTypeDef",
    "GroupCertificateAuthorityPropertiesTypeDef",
    "GroupInformationTypeDef",
    "GroupOwnerSettingTypeDef",
    "GroupVersionTypeDef",
    "LocalDeviceResourceDataTypeDef",
    "LocalVolumeResourceDataTypeDef",
    "LoggerDefinitionVersionTypeDef",
    "LoggerTypeDef",
    "ResourceAccessPolicyTypeDef",
    "ResourceDataContainerTypeDef",
    "ResourceDefinitionVersionTypeDef",
    "ResourceDownloadOwnerSettingTypeDef",
    "ResourceTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3MachineLearningModelResourceDataTypeDef",
    "SageMakerMachineLearningModelResourceDataTypeDef",
    "SecretsManagerSecretResourceDataTypeDef",
    "SubscriptionDefinitionVersionTypeDef",
    "SubscriptionTypeDef",
    "TelemetryConfigurationTypeDef",
    "VersionInformationTypeDef",
    "AssociateRoleToGroupResponseTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "CreateConnectorDefinitionResponseTypeDef",
    "CreateConnectorDefinitionVersionResponseTypeDef",
    "CreateCoreDefinitionResponseTypeDef",
    "CreateCoreDefinitionVersionResponseTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDeviceDefinitionResponseTypeDef",
    "CreateDeviceDefinitionVersionResponseTypeDef",
    "CreateFunctionDefinitionResponseTypeDef",
    "CreateFunctionDefinitionVersionResponseTypeDef",
    "CreateGroupCertificateAuthorityResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateGroupVersionResponseTypeDef",
    "CreateLoggerDefinitionResponseTypeDef",
    "CreateLoggerDefinitionVersionResponseTypeDef",
    "CreateResourceDefinitionResponseTypeDef",
    "CreateResourceDefinitionVersionResponseTypeDef",
    "CreateSoftwareUpdateJobResponseTypeDef",
    "CreateSubscriptionDefinitionResponseTypeDef",
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    "DisassociateRoleFromGroupResponseTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "GetAssociatedRoleResponseTypeDef",
    "GetBulkDeploymentStatusResponseTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "GetConnectorDefinitionResponseTypeDef",
    "GetConnectorDefinitionVersionResponseTypeDef",
    "GetCoreDefinitionResponseTypeDef",
    "GetCoreDefinitionVersionResponseTypeDef",
    "GetDeploymentStatusResponseTypeDef",
    "GetDeviceDefinitionResponseTypeDef",
    "GetDeviceDefinitionVersionResponseTypeDef",
    "GetFunctionDefinitionResponseTypeDef",
    "GetFunctionDefinitionVersionResponseTypeDef",
    "GetGroupCertificateAuthorityResponseTypeDef",
    "GetGroupCertificateConfigurationResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetGroupVersionResponseTypeDef",
    "GetLoggerDefinitionResponseTypeDef",
    "GetLoggerDefinitionVersionResponseTypeDef",
    "GetResourceDefinitionResponseTypeDef",
    "GetResourceDefinitionVersionResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "GetSubscriptionDefinitionResponseTypeDef",
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    "GetThingRuntimeConfigurationResponseTypeDef",
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    "ListBulkDeploymentsResponseTypeDef",
    "ListConnectorDefinitionVersionsResponseTypeDef",
    "ListConnectorDefinitionsResponseTypeDef",
    "ListCoreDefinitionVersionsResponseTypeDef",
    "ListCoreDefinitionsResponseTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListDeviceDefinitionVersionsResponseTypeDef",
    "ListDeviceDefinitionsResponseTypeDef",
    "ListFunctionDefinitionVersionsResponseTypeDef",
    "ListFunctionDefinitionsResponseTypeDef",
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    "ListGroupVersionsResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListLoggerDefinitionVersionsResponseTypeDef",
    "ListLoggerDefinitionsResponseTypeDef",
    "ListResourceDefinitionVersionsResponseTypeDef",
    "ListResourceDefinitionsResponseTypeDef",
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    "ListSubscriptionDefinitionsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResetDeploymentsResponseTypeDef",
    "StartBulkDeploymentResponseTypeDef",
    "TelemetryConfigurationUpdateTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
    "UpdateGroupCertificateConfigurationResponseTypeDef",
)

BulkDeploymentMetricsTypeDef = TypedDict(
    "BulkDeploymentMetricsTypeDef",
    {"InvalidInputRecords": int, "RecordsProcessed": int, "RetryAttempts": int},
    total=False,
)

BulkDeploymentResultTypeDef = TypedDict(
    "BulkDeploymentResultTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentStatus": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "GroupArn": str,
    },
    total=False,
)

BulkDeploymentTypeDef = TypedDict(
    "BulkDeploymentTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str, "CreatedAt": str},
    total=False,
)

ConnectivityInfoTypeDef = TypedDict(
    "ConnectivityInfoTypeDef",
    {"HostAddress": str, "Id": str, "Metadata": str, "PortNumber": int},
    total=False,
)

ConnectorDefinitionVersionTypeDef = TypedDict(
    "ConnectorDefinitionVersionTypeDef", {"Connectors": List["ConnectorTypeDef"]}, total=False
)

_RequiredConnectorTypeDef = TypedDict("_RequiredConnectorTypeDef", {"ConnectorArn": str, "Id": str})
_OptionalConnectorTypeDef = TypedDict(
    "_OptionalConnectorTypeDef", {"Parameters": Dict[str, str]}, total=False
)


class ConnectorTypeDef(_RequiredConnectorTypeDef, _OptionalConnectorTypeDef):
    pass


CoreDefinitionVersionTypeDef = TypedDict(
    "CoreDefinitionVersionTypeDef", {"Cores": List["CoreTypeDef"]}, total=False
)

_RequiredCoreTypeDef = TypedDict(
    "_RequiredCoreTypeDef", {"CertificateArn": str, "Id": str, "ThingArn": str}
)
_OptionalCoreTypeDef = TypedDict("_OptionalCoreTypeDef", {"SyncShadow": bool}, total=False)


class CoreTypeDef(_RequiredCoreTypeDef, _OptionalCoreTypeDef):
    pass


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

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "CreatedAt": str,
        "DeploymentArn": str,
        "DeploymentId": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "GroupArn": str,
    },
    total=False,
)

DeviceDefinitionVersionTypeDef = TypedDict(
    "DeviceDefinitionVersionTypeDef", {"Devices": List["DeviceTypeDef"]}, total=False
)

_RequiredDeviceTypeDef = TypedDict(
    "_RequiredDeviceTypeDef", {"CertificateArn": str, "Id": str, "ThingArn": str}
)
_OptionalDeviceTypeDef = TypedDict("_OptionalDeviceTypeDef", {"SyncShadow": bool}, total=False)


class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass


ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef", {"DetailedErrorCode": str, "DetailedErrorMessage": str}, total=False
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
        "EncodingType": Literal["binary", "json"],
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
    {"Execution": "FunctionDefaultExecutionConfigTypeDef"},
    total=False,
)

FunctionDefaultExecutionConfigTypeDef = TypedDict(
    "FunctionDefaultExecutionConfigTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": "FunctionRunAsConfigTypeDef",
    },
    total=False,
)

FunctionDefinitionVersionTypeDef = TypedDict(
    "FunctionDefinitionVersionTypeDef",
    {"DefaultConfig": "FunctionDefaultConfigTypeDef", "Functions": List["FunctionTypeDef"]},
    total=False,
)

FunctionExecutionConfigTypeDef = TypedDict(
    "FunctionExecutionConfigTypeDef",
    {
        "IsolationMode": Literal["GreengrassContainer", "NoContainer"],
        "RunAs": "FunctionRunAsConfigTypeDef",
    },
    total=False,
)

FunctionRunAsConfigTypeDef = TypedDict(
    "FunctionRunAsConfigTypeDef", {"Gid": int, "Uid": int}, total=False
)

_RequiredFunctionTypeDef = TypedDict("_RequiredFunctionTypeDef", {"Id": str})
_OptionalFunctionTypeDef = TypedDict(
    "_OptionalFunctionTypeDef",
    {"FunctionArn": str, "FunctionConfiguration": "FunctionConfigurationTypeDef"},
    total=False,
)


class FunctionTypeDef(_RequiredFunctionTypeDef, _OptionalFunctionTypeDef):
    pass


GroupCertificateAuthorityPropertiesTypeDef = TypedDict(
    "GroupCertificateAuthorityPropertiesTypeDef",
    {"GroupCertificateAuthorityArn": str, "GroupCertificateAuthorityId": str},
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
    "GroupOwnerSettingTypeDef", {"AutoAddGroupOwner": bool, "GroupOwner": str}, total=False
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

LocalDeviceResourceDataTypeDef = TypedDict(
    "LocalDeviceResourceDataTypeDef",
    {"GroupOwnerSetting": "GroupOwnerSettingTypeDef", "SourcePath": str},
    total=False,
)

LocalVolumeResourceDataTypeDef = TypedDict(
    "LocalVolumeResourceDataTypeDef",
    {"DestinationPath": str, "GroupOwnerSetting": "GroupOwnerSettingTypeDef", "SourcePath": str},
    total=False,
)

LoggerDefinitionVersionTypeDef = TypedDict(
    "LoggerDefinitionVersionTypeDef", {"Loggers": List["LoggerTypeDef"]}, total=False
)

_RequiredLoggerTypeDef = TypedDict(
    "_RequiredLoggerTypeDef",
    {
        "Component": Literal["GreengrassSystem", "Lambda"],
        "Id": str,
        "Level": Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"],
        "Type": Literal["FileSystem", "AWSCloudWatch"],
    },
)
_OptionalLoggerTypeDef = TypedDict("_OptionalLoggerTypeDef", {"Space": int}, total=False)


class LoggerTypeDef(_RequiredLoggerTypeDef, _OptionalLoggerTypeDef):
    pass


_RequiredResourceAccessPolicyTypeDef = TypedDict(
    "_RequiredResourceAccessPolicyTypeDef", {"ResourceId": str}
)
_OptionalResourceAccessPolicyTypeDef = TypedDict(
    "_OptionalResourceAccessPolicyTypeDef", {"Permission": Literal["ro", "rw"]}, total=False
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
    "ResourceDefinitionVersionTypeDef", {"Resources": List["ResourceTypeDef"]}, total=False
)

ResourceDownloadOwnerSettingTypeDef = TypedDict(
    "ResourceDownloadOwnerSettingTypeDef",
    {"GroupOwner": str, "GroupPermission": Literal["ro", "rw"]},
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {"Id": str, "Name": str, "ResourceDataContainer": "ResourceDataContainerTypeDef"},
)

RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {"TelemetryConfiguration": "TelemetryConfigurationTypeDef"},
    total=False,
)

S3MachineLearningModelResourceDataTypeDef = TypedDict(
    "S3MachineLearningModelResourceDataTypeDef",
    {"DestinationPath": str, "OwnerSetting": "ResourceDownloadOwnerSettingTypeDef", "S3Uri": str},
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
    {"ARN": str, "AdditionalStagingLabelsToDownload": List[str]},
    total=False,
)

SubscriptionDefinitionVersionTypeDef = TypedDict(
    "SubscriptionDefinitionVersionTypeDef",
    {"Subscriptions": List["SubscriptionTypeDef"]},
    total=False,
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef", {"Id": str, "Source": str, "Subject": str, "Target": str}
)

_RequiredTelemetryConfigurationTypeDef = TypedDict(
    "_RequiredTelemetryConfigurationTypeDef", {"Telemetry": Literal["On", "Off"]}
)
_OptionalTelemetryConfigurationTypeDef = TypedDict(
    "_OptionalTelemetryConfigurationTypeDef",
    {"ConfigurationSyncStatus": Literal["InSync", "OutOfSync"]},
    total=False,
)


class TelemetryConfigurationTypeDef(
    _RequiredTelemetryConfigurationTypeDef, _OptionalTelemetryConfigurationTypeDef
):
    pass


VersionInformationTypeDef = TypedDict(
    "VersionInformationTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

AssociateRoleToGroupResponseTypeDef = TypedDict(
    "AssociateRoleToGroupResponseTypeDef", {"AssociatedAt": str}, total=False
)

AssociateServiceRoleToAccountResponseTypeDef = TypedDict(
    "AssociateServiceRoleToAccountResponseTypeDef", {"AssociatedAt": str}, total=False
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
    },
    total=False,
)

CreateConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "CreateConnectorDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
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
    },
    total=False,
)

CreateCoreDefinitionVersionResponseTypeDef = TypedDict(
    "CreateCoreDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

CreateDeploymentResponseTypeDef = TypedDict(
    "CreateDeploymentResponseTypeDef", {"DeploymentArn": str, "DeploymentId": str}, total=False
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
    },
    total=False,
)

CreateDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "CreateDeviceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
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
    },
    total=False,
)

CreateFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "CreateFunctionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

CreateGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "CreateGroupCertificateAuthorityResponseTypeDef",
    {"GroupCertificateAuthorityArn": str},
    total=False,
)

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
    },
    total=False,
)

CreateGroupVersionResponseTypeDef = TypedDict(
    "CreateGroupVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
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
    },
    total=False,
)

CreateLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "CreateLoggerDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
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
    },
    total=False,
)

CreateResourceDefinitionVersionResponseTypeDef = TypedDict(
    "CreateResourceDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

CreateSoftwareUpdateJobResponseTypeDef = TypedDict(
    "CreateSoftwareUpdateJobResponseTypeDef",
    {"IotJobArn": str, "IotJobId": str, "PlatformSoftwareVersion": str},
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
    },
    total=False,
)

CreateSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    {"Arn": str, "CreationTimestamp": str, "Id": str, "Version": str},
    total=False,
)

DisassociateRoleFromGroupResponseTypeDef = TypedDict(
    "DisassociateRoleFromGroupResponseTypeDef", {"DisassociatedAt": str}, total=False
)

DisassociateServiceRoleFromAccountResponseTypeDef = TypedDict(
    "DisassociateServiceRoleFromAccountResponseTypeDef", {"DisassociatedAt": str}, total=False
)

GetAssociatedRoleResponseTypeDef = TypedDict(
    "GetAssociatedRoleResponseTypeDef", {"AssociatedAt": str, "RoleArn": str}, total=False
)

GetBulkDeploymentStatusResponseTypeDef = TypedDict(
    "GetBulkDeploymentStatusResponseTypeDef",
    {
        "BulkDeploymentMetrics": "BulkDeploymentMetricsTypeDef",
        "BulkDeploymentStatus": Literal[
            "Initializing", "Running", "Completed", "Stopping", "Stopped", "Failed"
        ],
        "CreatedAt": str,
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "tags": Dict[str, str],
    },
    total=False,
)

GetConnectivityInfoResponseTypeDef = TypedDict(
    "GetConnectivityInfoResponseTypeDef",
    {"ConnectivityInfo": List["ConnectivityInfoTypeDef"], "Message": str},
    total=False,
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
    },
    total=False,
)

GetConnectorDefinitionVersionResponseTypeDef = TypedDict(
    "GetConnectorDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "ConnectorDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
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
    },
    total=False,
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
    },
    total=False,
)

GetDeploymentStatusResponseTypeDef = TypedDict(
    "GetDeploymentStatusResponseTypeDef",
    {
        "DeploymentStatus": str,
        "DeploymentType": Literal[
            "NewDeployment", "Redeployment", "ResetDeployment", "ForceResetDeployment"
        ],
        "ErrorDetails": List["ErrorDetailTypeDef"],
        "ErrorMessage": str,
        "UpdatedAt": str,
    },
    total=False,
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
    },
    total=False,
)

GetDeviceDefinitionVersionResponseTypeDef = TypedDict(
    "GetDeviceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "DeviceDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
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
    },
    total=False,
)

GetFunctionDefinitionVersionResponseTypeDef = TypedDict(
    "GetFunctionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "FunctionDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)

GetGroupCertificateAuthorityResponseTypeDef = TypedDict(
    "GetGroupCertificateAuthorityResponseTypeDef",
    {
        "GroupCertificateAuthorityArn": str,
        "GroupCertificateAuthorityId": str,
        "PemEncodedCertificate": str,
    },
    total=False,
)

GetGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "GetGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
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
    },
    total=False,
)

GetGroupVersionResponseTypeDef = TypedDict(
    "GetGroupVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "GroupVersionTypeDef",
        "Id": str,
        "Version": str,
    },
    total=False,
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
    },
    total=False,
)

GetLoggerDefinitionVersionResponseTypeDef = TypedDict(
    "GetLoggerDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "LoggerDefinitionVersionTypeDef",
        "Id": str,
        "Version": str,
    },
    total=False,
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
    },
    total=False,
)

GetResourceDefinitionVersionResponseTypeDef = TypedDict(
    "GetResourceDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "ResourceDefinitionVersionTypeDef",
        "Id": str,
        "Version": str,
    },
    total=False,
)

GetServiceRoleForAccountResponseTypeDef = TypedDict(
    "GetServiceRoleForAccountResponseTypeDef", {"AssociatedAt": str, "RoleArn": str}, total=False
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
    },
    total=False,
)

GetSubscriptionDefinitionVersionResponseTypeDef = TypedDict(
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    {
        "Arn": str,
        "CreationTimestamp": str,
        "Definition": "SubscriptionDefinitionVersionTypeDef",
        "Id": str,
        "NextToken": str,
        "Version": str,
    },
    total=False,
)

GetThingRuntimeConfigurationResponseTypeDef = TypedDict(
    "GetThingRuntimeConfigurationResponseTypeDef",
    {"RuntimeConfiguration": "RuntimeConfigurationTypeDef"},
    total=False,
)

ListBulkDeploymentDetailedReportsResponseTypeDef = TypedDict(
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    {"Deployments": List["BulkDeploymentResultTypeDef"], "NextToken": str},
    total=False,
)

ListBulkDeploymentsResponseTypeDef = TypedDict(
    "ListBulkDeploymentsResponseTypeDef",
    {"BulkDeployments": List["BulkDeploymentTypeDef"], "NextToken": str},
    total=False,
)

ListConnectorDefinitionVersionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionInformationTypeDef"]},
    total=False,
)

ListConnectorDefinitionsResponseTypeDef = TypedDict(
    "ListConnectorDefinitionsResponseTypeDef",
    {"Definitions": List["DefinitionInformationTypeDef"], "NextToken": str},
    total=False,
)

ListCoreDefinitionVersionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionInformationTypeDef"]},
    total=False,
)

ListCoreDefinitionsResponseTypeDef = TypedDict(
    "ListCoreDefinitionsResponseTypeDef",
    {"Definitions": List["DefinitionInformationTypeDef"], "NextToken": str},
    total=False,
)

ListDeploymentsResponseTypeDef = TypedDict(
    "ListDeploymentsResponseTypeDef",
    {"Deployments": List["DeploymentTypeDef"], "NextToken": str},
    total=False,
)

ListDeviceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionInformationTypeDef"]},
    total=False,
)

ListDeviceDefinitionsResponseTypeDef = TypedDict(
    "ListDeviceDefinitionsResponseTypeDef",
    {"Definitions": List["DefinitionInformationTypeDef"], "NextToken": str},
    total=False,
)

ListFunctionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionInformationTypeDef"]},
    total=False,
)

ListFunctionDefinitionsResponseTypeDef = TypedDict(
    "ListFunctionDefinitionsResponseTypeDef",
    {"Definitions": List["DefinitionInformationTypeDef"], "NextToken": str},
    total=False,
)

ListGroupCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    {"GroupCertificateAuthorities": List["GroupCertificateAuthorityPropertiesTypeDef"]},
    total=False,
)

ListGroupVersionsResponseTypeDef = TypedDict(
    "ListGroupVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionInformationTypeDef"]},
    total=False,
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {"Groups": List["GroupInformationTypeDef"], "NextToken": str},
    total=False,
)

ListLoggerDefinitionVersionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionInformationTypeDef"]},
    total=False,
)

ListLoggerDefinitionsResponseTypeDef = TypedDict(
    "ListLoggerDefinitionsResponseTypeDef",
    {"Definitions": List["DefinitionInformationTypeDef"], "NextToken": str},
    total=False,
)

ListResourceDefinitionVersionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionInformationTypeDef"]},
    total=False,
)

ListResourceDefinitionsResponseTypeDef = TypedDict(
    "ListResourceDefinitionsResponseTypeDef",
    {"Definitions": List["DefinitionInformationTypeDef"], "NextToken": str},
    total=False,
)

ListSubscriptionDefinitionVersionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    {"NextToken": str, "Versions": List["VersionInformationTypeDef"]},
    total=False,
)

ListSubscriptionDefinitionsResponseTypeDef = TypedDict(
    "ListSubscriptionDefinitionsResponseTypeDef",
    {"Definitions": List["DefinitionInformationTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ResetDeploymentsResponseTypeDef = TypedDict(
    "ResetDeploymentsResponseTypeDef", {"DeploymentArn": str, "DeploymentId": str}, total=False
)

StartBulkDeploymentResponseTypeDef = TypedDict(
    "StartBulkDeploymentResponseTypeDef",
    {"BulkDeploymentArn": str, "BulkDeploymentId": str},
    total=False,
)

TelemetryConfigurationUpdateTypeDef = TypedDict(
    "TelemetryConfigurationUpdateTypeDef", {"Telemetry": Literal["On", "Off"]}
)

UpdateConnectivityInfoResponseTypeDef = TypedDict(
    "UpdateConnectivityInfoResponseTypeDef", {"Message": str, "Version": str}, total=False
)

UpdateGroupCertificateConfigurationResponseTypeDef = TypedDict(
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    {
        "CertificateAuthorityExpiryInMilliseconds": str,
        "CertificateExpiryInMilliseconds": str,
        "GroupId": str,
    },
    total=False,
)
