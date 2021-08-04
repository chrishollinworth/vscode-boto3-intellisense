"""
Type annotations for greengrass service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/literals.html)

Usage::

    ```python
    from mypy_boto3_greengrass.literals import BulkDeploymentStatusType

    data: BulkDeploymentStatusType = "Completed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BulkDeploymentStatusType",
    "ConfigurationSyncStatusType",
    "DeploymentTypeType",
    "EncodingTypeType",
    "FunctionIsolationModeType",
    "ListBulkDeploymentDetailedReportsPaginatorName",
    "ListBulkDeploymentsPaginatorName",
    "ListConnectorDefinitionVersionsPaginatorName",
    "ListConnectorDefinitionsPaginatorName",
    "ListCoreDefinitionVersionsPaginatorName",
    "ListCoreDefinitionsPaginatorName",
    "ListDeploymentsPaginatorName",
    "ListDeviceDefinitionVersionsPaginatorName",
    "ListDeviceDefinitionsPaginatorName",
    "ListFunctionDefinitionVersionsPaginatorName",
    "ListFunctionDefinitionsPaginatorName",
    "ListGroupVersionsPaginatorName",
    "ListGroupsPaginatorName",
    "ListLoggerDefinitionVersionsPaginatorName",
    "ListLoggerDefinitionsPaginatorName",
    "ListResourceDefinitionVersionsPaginatorName",
    "ListResourceDefinitionsPaginatorName",
    "ListSubscriptionDefinitionVersionsPaginatorName",
    "ListSubscriptionDefinitionsPaginatorName",
    "LoggerComponentType",
    "LoggerLevelType",
    "LoggerTypeType",
    "PermissionType",
    "SoftwareToUpdateType",
    "TelemetryType",
    "UpdateAgentLogLevelType",
    "UpdateTargetsArchitectureType",
    "UpdateTargetsOperatingSystemType",
)

BulkDeploymentStatusType = Literal[
    "Completed", "Failed", "Initializing", "Running", "Stopped", "Stopping"
]
ConfigurationSyncStatusType = Literal["InSync", "OutOfSync"]
DeploymentTypeType = Literal[
    "ForceResetDeployment", "NewDeployment", "Redeployment", "ResetDeployment"
]
EncodingTypeType = Literal["binary", "json"]
FunctionIsolationModeType = Literal["GreengrassContainer", "NoContainer"]
ListBulkDeploymentDetailedReportsPaginatorName = Literal["list_bulk_deployment_detailed_reports"]
ListBulkDeploymentsPaginatorName = Literal["list_bulk_deployments"]
ListConnectorDefinitionVersionsPaginatorName = Literal["list_connector_definition_versions"]
ListConnectorDefinitionsPaginatorName = Literal["list_connector_definitions"]
ListCoreDefinitionVersionsPaginatorName = Literal["list_core_definition_versions"]
ListCoreDefinitionsPaginatorName = Literal["list_core_definitions"]
ListDeploymentsPaginatorName = Literal["list_deployments"]
ListDeviceDefinitionVersionsPaginatorName = Literal["list_device_definition_versions"]
ListDeviceDefinitionsPaginatorName = Literal["list_device_definitions"]
ListFunctionDefinitionVersionsPaginatorName = Literal["list_function_definition_versions"]
ListFunctionDefinitionsPaginatorName = Literal["list_function_definitions"]
ListGroupVersionsPaginatorName = Literal["list_group_versions"]
ListGroupsPaginatorName = Literal["list_groups"]
ListLoggerDefinitionVersionsPaginatorName = Literal["list_logger_definition_versions"]
ListLoggerDefinitionsPaginatorName = Literal["list_logger_definitions"]
ListResourceDefinitionVersionsPaginatorName = Literal["list_resource_definition_versions"]
ListResourceDefinitionsPaginatorName = Literal["list_resource_definitions"]
ListSubscriptionDefinitionVersionsPaginatorName = Literal["list_subscription_definition_versions"]
ListSubscriptionDefinitionsPaginatorName = Literal["list_subscription_definitions"]
LoggerComponentType = Literal["GreengrassSystem", "Lambda"]
LoggerLevelType = Literal["DEBUG", "ERROR", "FATAL", "INFO", "WARN"]
LoggerTypeType = Literal["AWSCloudWatch", "FileSystem"]
PermissionType = Literal["ro", "rw"]
SoftwareToUpdateType = Literal["core", "ota_agent"]
TelemetryType = Literal["Off", "On"]
UpdateAgentLogLevelType = Literal[
    "DEBUG", "ERROR", "FATAL", "INFO", "NONE", "TRACE", "VERBOSE", "WARN"
]
UpdateTargetsArchitectureType = Literal["aarch64", "armv6l", "armv7l", "x86_64"]
UpdateTargetsOperatingSystemType = Literal["amazon_linux", "openwrt", "raspbian", "ubuntu"]
