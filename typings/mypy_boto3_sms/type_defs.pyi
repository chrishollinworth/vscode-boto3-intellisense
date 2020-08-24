"""
Main interface for sms service type definitions.

Usage::

    ```python
    from mypy_boto3_sms.type_defs import AppSummaryTypeDef

    data: AppSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppSummaryTypeDef",
    "AppValidationConfigurationTypeDef",
    "AppValidationOutputTypeDef",
    "ConnectorTypeDef",
    "LaunchDetailsTypeDef",
    "ReplicationJobTypeDef",
    "ReplicationRunStageDetailsTypeDef",
    "ReplicationRunTypeDef",
    "S3LocationTypeDef",
    "SSMOutputTypeDef",
    "SSMValidationParametersTypeDef",
    "ServerGroupLaunchConfigurationTypeDef",
    "ServerGroupReplicationConfigurationTypeDef",
    "ServerGroupTypeDef",
    "ServerGroupValidationConfigurationTypeDef",
    "ServerLaunchConfigurationTypeDef",
    "ServerReplicationConfigurationTypeDef",
    "ServerReplicationParametersTypeDef",
    "ServerTypeDef",
    "ServerValidationConfigurationTypeDef",
    "ServerValidationOutputTypeDef",
    "SourceTypeDef",
    "TagTypeDef",
    "UserDataTypeDef",
    "UserDataValidationParametersTypeDef",
    "ValidationOutputTypeDef",
    "VmServerAddressTypeDef",
    "VmServerTypeDef",
    "CreateAppResponseTypeDef",
    "CreateReplicationJobResponseTypeDef",
    "GenerateChangeSetResponseTypeDef",
    "GenerateTemplateResponseTypeDef",
    "GetAppLaunchConfigurationResponseTypeDef",
    "GetAppReplicationConfigurationResponseTypeDef",
    "GetAppResponseTypeDef",
    "GetAppValidationConfigurationResponseTypeDef",
    "GetAppValidationOutputResponseTypeDef",
    "GetConnectorsResponseTypeDef",
    "GetReplicationJobsResponseTypeDef",
    "GetReplicationRunsResponseTypeDef",
    "GetServersResponseTypeDef",
    "ListAppsResponseTypeDef",
    "NotificationContextTypeDef",
    "PaginatorConfigTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "UpdateAppResponseTypeDef",
)

AppSummaryTypeDef = TypedDict(
    "AppSummaryTypeDef",
    {
        "appId": str,
        "importedAppId": str,
        "name": str,
        "description": str,
        "status": Literal["CREATING", "ACTIVE", "UPDATING", "DELETING", "DELETED", "DELETE_FAILED"],
        "statusMessage": str,
        "replicationConfigurationStatus": Literal["NOT_CONFIGURED", "CONFIGURED"],
        "replicationStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_REPLICATION",
            "VALIDATION_IN_PROGRESS",
            "REPLICATION_PENDING",
            "REPLICATION_IN_PROGRESS",
            "REPLICATED",
            "PARTIALLY_REPLICATED",
            "DELTA_REPLICATION_IN_PROGRESS",
            "DELTA_REPLICATED",
            "DELTA_REPLICATION_FAILED",
            "REPLICATION_FAILED",
            "REPLICATION_STOPPING",
            "REPLICATION_STOP_FAILED",
            "REPLICATION_STOPPED",
        ],
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchConfigurationStatus": Literal["NOT_CONFIGURED", "CONFIGURED"],
        "launchStatus": Literal[
            "READY_FOR_CONFIGURATION",
            "CONFIGURATION_IN_PROGRESS",
            "CONFIGURATION_INVALID",
            "READY_FOR_LAUNCH",
            "VALIDATION_IN_PROGRESS",
            "LAUNCH_PENDING",
            "LAUNCH_IN_PROGRESS",
            "LAUNCHED",
            "PARTIALLY_LAUNCHED",
            "DELTA_LAUNCH_IN_PROGRESS",
            "DELTA_LAUNCH_FAILED",
            "LAUNCH_FAILED",
            "TERMINATE_IN_PROGRESS",
            "TERMINATE_FAILED",
            "TERMINATED",
        ],
        "launchStatusMessage": str,
        "launchDetails": "LaunchDetailsTypeDef",
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)

AppValidationConfigurationTypeDef = TypedDict(
    "AppValidationConfigurationTypeDef",
    {
        "validationId": str,
        "name": str,
        "appValidationStrategy": Literal["SSM"],
        "ssmValidationParameters": "SSMValidationParametersTypeDef",
    },
    total=False,
)

AppValidationOutputTypeDef = TypedDict(
    "AppValidationOutputTypeDef", {"ssmOutput": "SSMOutputTypeDef"}, total=False
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": Literal["HEALTHY", "UNHEALTHY"],
        "capabilityList": List[
            Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER", "SNAPSHOT_BATCHING", "SMS_OPTIMIZED"]
        ],
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)

LaunchDetailsTypeDef = TypedDict(
    "LaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)

ReplicationJobTypeDef = TypedDict(
    "ReplicationJobTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": Literal["VIRTUAL_MACHINE"],
        "vmServer": "VmServerTypeDef",
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": Literal["AWS", "BYOL"],
        "roleName": str,
        "latestAmiId": str,
        "state": Literal[
            "PENDING",
            "ACTIVE",
            "FAILED",
            "DELETING",
            "DELETED",
            "COMPLETED",
            "PAUSED_ON_FAILURE",
            "FAILING",
        ],
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List["ReplicationRunTypeDef"],
    },
    total=False,
)

ReplicationRunStageDetailsTypeDef = TypedDict(
    "ReplicationRunStageDetailsTypeDef", {"stage": str, "stageProgress": str}, total=False
)

ReplicationRunTypeDef = TypedDict(
    "ReplicationRunTypeDef",
    {
        "replicationRunId": str,
        "state": Literal[
            "PENDING", "MISSED", "ACTIVE", "FAILED", "COMPLETED", "DELETING", "DELETED"
        ],
        "type": Literal["ON_DEMAND", "AUTOMATIC"],
        "stageDetails": "ReplicationRunStageDetailsTypeDef",
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

S3LocationTypeDef = TypedDict("S3LocationTypeDef", {"bucket": str, "key": str}, total=False)

SSMOutputTypeDef = TypedDict("SSMOutputTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False)

SSMValidationParametersTypeDef = TypedDict(
    "SSMValidationParametersTypeDef",
    {
        "source": "SourceTypeDef",
        "instanceId": str,
        "scriptType": Literal["SHELL_SCRIPT", "POWERSHELL_SCRIPT"],
        "command": str,
        "executionTimeoutSeconds": int,
        "outputS3BucketName": str,
    },
    total=False,
)

ServerGroupLaunchConfigurationTypeDef = TypedDict(
    "ServerGroupLaunchConfigurationTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List["ServerLaunchConfigurationTypeDef"],
    },
    total=False,
)

ServerGroupReplicationConfigurationTypeDef = TypedDict(
    "ServerGroupReplicationConfigurationTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List["ServerReplicationConfigurationTypeDef"],
    },
    total=False,
)

ServerGroupTypeDef = TypedDict(
    "ServerGroupTypeDef",
    {"serverGroupId": str, "name": str, "serverList": List["ServerTypeDef"]},
    total=False,
)

ServerGroupValidationConfigurationTypeDef = TypedDict(
    "ServerGroupValidationConfigurationTypeDef",
    {
        "serverGroupId": str,
        "serverValidationConfigurations": List["ServerValidationConfigurationTypeDef"],
    },
    total=False,
)

ServerLaunchConfigurationTypeDef = TypedDict(
    "ServerLaunchConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": "UserDataTypeDef",
        "instanceType": str,
        "associatePublicIpAddress": bool,
        "iamInstanceProfileName": str,
        "configureScript": "S3LocationTypeDef",
        "configureScriptType": Literal["SHELL_SCRIPT", "POWERSHELL_SCRIPT"],
    },
    total=False,
)

ServerReplicationConfigurationTypeDef = TypedDict(
    "ServerReplicationConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "serverReplicationParameters": "ServerReplicationParametersTypeDef",
    },
    total=False,
)

ServerReplicationParametersTypeDef = TypedDict(
    "ServerReplicationParametersTypeDef",
    {
        "seedTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "licenseType": Literal["AWS", "BYOL"],
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "serverId": str,
        "serverType": Literal["VIRTUAL_MACHINE"],
        "vmServer": "VmServerTypeDef",
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ServerValidationConfigurationTypeDef = TypedDict(
    "ServerValidationConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "validationId": str,
        "name": str,
        "serverValidationStrategy": Literal["USERDATA"],
        "userDataValidationParameters": "UserDataValidationParametersTypeDef",
    },
    total=False,
)

ServerValidationOutputTypeDef = TypedDict(
    "ServerValidationOutputTypeDef", {"server": "ServerTypeDef"}, total=False
)

SourceTypeDef = TypedDict("SourceTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

UserDataTypeDef = TypedDict("UserDataTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False)

UserDataValidationParametersTypeDef = TypedDict(
    "UserDataValidationParametersTypeDef",
    {"source": "SourceTypeDef", "scriptType": Literal["SHELL_SCRIPT", "POWERSHELL_SCRIPT"]},
    total=False,
)

ValidationOutputTypeDef = TypedDict(
    "ValidationOutputTypeDef",
    {
        "validationId": str,
        "name": str,
        "status": Literal["READY_FOR_VALIDATION", "PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "statusMessage": str,
        "latestValidationTime": datetime,
        "appValidationOutput": "AppValidationOutputTypeDef",
        "serverValidationOutput": "ServerValidationOutputTypeDef",
    },
    total=False,
)

VmServerAddressTypeDef = TypedDict(
    "VmServerAddressTypeDef", {"vmManagerId": str, "vmId": str}, total=False
)

VmServerTypeDef = TypedDict(
    "VmServerTypeDef",
    {
        "vmServerAddress": "VmServerAddressTypeDef",
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": Literal["VSPHERE", "SCVMM", "HYPERV-MANAGER"],
        "vmPath": str,
    },
    total=False,
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CreateReplicationJobResponseTypeDef = TypedDict(
    "CreateReplicationJobResponseTypeDef", {"replicationJobId": str}, total=False
)

GenerateChangeSetResponseTypeDef = TypedDict(
    "GenerateChangeSetResponseTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False
)

GenerateTemplateResponseTypeDef = TypedDict(
    "GenerateTemplateResponseTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False
)

GetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "GetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List["ServerGroupLaunchConfigurationTypeDef"],
    },
    total=False,
)

GetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "GetAppReplicationConfigurationResponseTypeDef",
    {"serverGroupReplicationConfigurations": List["ServerGroupReplicationConfigurationTypeDef"]},
    total=False,
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

GetAppValidationConfigurationResponseTypeDef = TypedDict(
    "GetAppValidationConfigurationResponseTypeDef",
    {
        "appValidationConfigurations": List["AppValidationConfigurationTypeDef"],
        "serverGroupValidationConfigurations": List["ServerGroupValidationConfigurationTypeDef"],
    },
    total=False,
)

GetAppValidationOutputResponseTypeDef = TypedDict(
    "GetAppValidationOutputResponseTypeDef",
    {"validationOutputList": List["ValidationOutputTypeDef"]},
    total=False,
)

GetConnectorsResponseTypeDef = TypedDict(
    "GetConnectorsResponseTypeDef",
    {"connectorList": List["ConnectorTypeDef"], "nextToken": str},
    total=False,
)

GetReplicationJobsResponseTypeDef = TypedDict(
    "GetReplicationJobsResponseTypeDef",
    {"replicationJobList": List["ReplicationJobTypeDef"], "nextToken": str},
    total=False,
)

GetReplicationRunsResponseTypeDef = TypedDict(
    "GetReplicationRunsResponseTypeDef",
    {
        "replicationJob": "ReplicationJobTypeDef",
        "replicationRunList": List["ReplicationRunTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetServersResponseTypeDef = TypedDict(
    "GetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": Literal[
            "NOT_IMPORTED", "IMPORTING", "AVAILABLE", "DELETED", "EXPIRED"
        ],
        "serverList": List["ServerTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef", {"apps": List["AppSummaryTypeDef"], "nextToken": str}, total=False
)

NotificationContextTypeDef = TypedDict(
    "NotificationContextTypeDef",
    {
        "validationId": str,
        "status": Literal["READY_FOR_VALIDATION", "PENDING", "IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "statusMessage": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "StartOnDemandReplicationRunResponseTypeDef", {"replicationRunId": str}, total=False
)

UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)
