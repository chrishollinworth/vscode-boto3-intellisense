"""
Type annotations for sms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sms.type_defs import AppSummaryTypeDef

    data: AppSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AppLaunchConfigurationStatusType,
    AppLaunchStatusType,
    AppReplicationConfigurationStatusType,
    AppReplicationStatusType,
    AppStatusType,
    ConnectorCapabilityType,
    ConnectorStatusType,
    LicenseTypeType,
    OutputFormatType,
    ReplicationJobStateType,
    ReplicationRunStateType,
    ReplicationRunTypeType,
    ScriptTypeType,
    ServerCatalogStatusType,
    ValidationStatusType,
    VmManagerTypeType,
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
    "AppSummaryTypeDef",
    "AppValidationConfigurationTypeDef",
    "AppValidationOutputTypeDef",
    "ConnectorTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateReplicationJobRequestRequestTypeDef",
    "CreateReplicationJobResponseTypeDef",
    "DeleteAppLaunchConfigurationRequestRequestTypeDef",
    "DeleteAppReplicationConfigurationRequestRequestTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppValidationConfigurationRequestRequestTypeDef",
    "DeleteReplicationJobRequestRequestTypeDef",
    "DisassociateConnectorRequestRequestTypeDef",
    "GenerateChangeSetRequestRequestTypeDef",
    "GenerateChangeSetResponseTypeDef",
    "GenerateTemplateRequestRequestTypeDef",
    "GenerateTemplateResponseTypeDef",
    "GetAppLaunchConfigurationRequestRequestTypeDef",
    "GetAppLaunchConfigurationResponseTypeDef",
    "GetAppReplicationConfigurationRequestRequestTypeDef",
    "GetAppReplicationConfigurationResponseTypeDef",
    "GetAppRequestRequestTypeDef",
    "GetAppResponseTypeDef",
    "GetAppValidationConfigurationRequestRequestTypeDef",
    "GetAppValidationConfigurationResponseTypeDef",
    "GetAppValidationOutputRequestRequestTypeDef",
    "GetAppValidationOutputResponseTypeDef",
    "GetConnectorsRequestRequestTypeDef",
    "GetConnectorsResponseTypeDef",
    "GetReplicationJobsRequestRequestTypeDef",
    "GetReplicationJobsResponseTypeDef",
    "GetReplicationRunsRequestRequestTypeDef",
    "GetReplicationRunsResponseTypeDef",
    "GetServersRequestRequestTypeDef",
    "GetServersResponseTypeDef",
    "ImportAppCatalogRequestRequestTypeDef",
    "LaunchAppRequestRequestTypeDef",
    "LaunchDetailsTypeDef",
    "ListAppsRequestRequestTypeDef",
    "ListAppsResponseTypeDef",
    "NotificationContextTypeDef",
    "NotifyAppValidationOutputRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutAppLaunchConfigurationRequestRequestTypeDef",
    "PutAppReplicationConfigurationRequestRequestTypeDef",
    "PutAppValidationConfigurationRequestRequestTypeDef",
    "ReplicationJobTypeDef",
    "ReplicationRunStageDetailsTypeDef",
    "ReplicationRunTypeDef",
    "ResponseMetadataTypeDef",
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
    "StartAppReplicationRequestRequestTypeDef",
    "StartOnDemandAppReplicationRequestRequestTypeDef",
    "StartOnDemandReplicationRunRequestRequestTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "StopAppReplicationRequestRequestTypeDef",
    "TagTypeDef",
    "TerminateAppRequestRequestTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "UpdateAppResponseTypeDef",
    "UpdateReplicationJobRequestRequestTypeDef",
    "UserDataTypeDef",
    "UserDataValidationParametersTypeDef",
    "ValidationOutputTypeDef",
    "VmServerAddressTypeDef",
    "VmServerTypeDef",
)

AppSummaryTypeDef = TypedDict(
    "AppSummaryTypeDef",
    {
        "appId": str,
        "importedAppId": str,
        "name": str,
        "description": str,
        "status": AppStatusType,
        "statusMessage": str,
        "replicationConfigurationStatus": AppReplicationConfigurationStatusType,
        "replicationStatus": AppReplicationStatusType,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchConfigurationStatus": AppLaunchConfigurationStatusType,
        "launchStatus": AppLaunchStatusType,
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
    "AppValidationOutputTypeDef",
    {
        "ssmOutput": "SSMOutputTypeDef",
    },
    total=False,
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": ConnectorStatusType,
        "capabilityList": List[ConnectorCapabilityType],
        "vmManagerName": str,
        "vmManagerType": VmManagerTypeType,
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)

CreateAppRequestRequestTypeDef = TypedDict(
    "CreateAppRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
        "roleName": str,
        "clientToken": str,
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplicationJobRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReplicationJobRequestRequestTypeDef",
    {
        "serverId": str,
        "seedReplicationTime": Union[datetime, str],
    },
)
_OptionalCreateReplicationJobRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReplicationJobRequestRequestTypeDef",
    {
        "frequency": int,
        "runOnce": bool,
        "licenseType": LicenseTypeType,
        "roleName": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

class CreateReplicationJobRequestRequestTypeDef(
    _RequiredCreateReplicationJobRequestRequestTypeDef,
    _OptionalCreateReplicationJobRequestRequestTypeDef,
):
    pass

CreateReplicationJobResponseTypeDef = TypedDict(
    "CreateReplicationJobResponseTypeDef",
    {
        "replicationJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

DeleteAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

DeleteAppRequestRequestTypeDef = TypedDict(
    "DeleteAppRequestRequestTypeDef",
    {
        "appId": str,
        "forceStopAppReplication": bool,
        "forceTerminateApp": bool,
    },
    total=False,
)

DeleteAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)

DeleteReplicationJobRequestRequestTypeDef = TypedDict(
    "DeleteReplicationJobRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)

DisassociateConnectorRequestRequestTypeDef = TypedDict(
    "DisassociateConnectorRequestRequestTypeDef",
    {
        "connectorId": str,
    },
)

GenerateChangeSetRequestRequestTypeDef = TypedDict(
    "GenerateChangeSetRequestRequestTypeDef",
    {
        "appId": str,
        "changesetFormat": OutputFormatType,
    },
    total=False,
)

GenerateChangeSetResponseTypeDef = TypedDict(
    "GenerateChangeSetResponseTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateTemplateRequestRequestTypeDef = TypedDict(
    "GenerateTemplateRequestRequestTypeDef",
    {
        "appId": str,
        "templateFormat": OutputFormatType,
    },
    total=False,
)

GenerateTemplateResponseTypeDef = TypedDict(
    "GenerateTemplateResponseTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "GetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List["ServerGroupLaunchConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "GetAppReplicationConfigurationResponseTypeDef",
    {
        "serverGroupReplicationConfigurations": List["ServerGroupReplicationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppRequestRequestTypeDef = TypedDict(
    "GetAppRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "GetAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppValidationConfigurationResponseTypeDef = TypedDict(
    "GetAppValidationConfigurationResponseTypeDef",
    {
        "appValidationConfigurations": List["AppValidationConfigurationTypeDef"],
        "serverGroupValidationConfigurations": List["ServerGroupValidationConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppValidationOutputRequestRequestTypeDef = TypedDict(
    "GetAppValidationOutputRequestRequestTypeDef",
    {
        "appId": str,
    },
)

GetAppValidationOutputResponseTypeDef = TypedDict(
    "GetAppValidationOutputResponseTypeDef",
    {
        "validationOutputList": List["ValidationOutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectorsRequestRequestTypeDef = TypedDict(
    "GetConnectorsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetConnectorsResponseTypeDef = TypedDict(
    "GetConnectorsResponseTypeDef",
    {
        "connectorList": List["ConnectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReplicationJobsRequestRequestTypeDef = TypedDict(
    "GetReplicationJobsRequestRequestTypeDef",
    {
        "replicationJobId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

GetReplicationJobsResponseTypeDef = TypedDict(
    "GetReplicationJobsResponseTypeDef",
    {
        "replicationJobList": List["ReplicationJobTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReplicationRunsRequestRequestTypeDef = TypedDict(
    "_RequiredGetReplicationRunsRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalGetReplicationRunsRequestRequestTypeDef = TypedDict(
    "_OptionalGetReplicationRunsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetReplicationRunsRequestRequestTypeDef(
    _RequiredGetReplicationRunsRequestRequestTypeDef,
    _OptionalGetReplicationRunsRequestRequestTypeDef,
):
    pass

GetReplicationRunsResponseTypeDef = TypedDict(
    "GetReplicationRunsResponseTypeDef",
    {
        "replicationJob": "ReplicationJobTypeDef",
        "replicationRunList": List["ReplicationRunTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServersRequestRequestTypeDef = TypedDict(
    "GetServersRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "vmServerAddressList": List["VmServerAddressTypeDef"],
    },
    total=False,
)

GetServersResponseTypeDef = TypedDict(
    "GetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": ServerCatalogStatusType,
        "serverList": List["ServerTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportAppCatalogRequestRequestTypeDef = TypedDict(
    "ImportAppCatalogRequestRequestTypeDef",
    {
        "roleName": str,
    },
    total=False,
)

LaunchAppRequestRequestTypeDef = TypedDict(
    "LaunchAppRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

LaunchDetailsTypeDef = TypedDict(
    "LaunchDetailsTypeDef",
    {
        "latestLaunchTime": datetime,
        "stackName": str,
        "stackId": str,
    },
    total=False,
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "appIds": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "apps": List["AppSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationContextTypeDef = TypedDict(
    "NotificationContextTypeDef",
    {
        "validationId": str,
        "status": ValidationStatusType,
        "statusMessage": str,
    },
    total=False,
)

_RequiredNotifyAppValidationOutputRequestRequestTypeDef = TypedDict(
    "_RequiredNotifyAppValidationOutputRequestRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalNotifyAppValidationOutputRequestRequestTypeDef = TypedDict(
    "_OptionalNotifyAppValidationOutputRequestRequestTypeDef",
    {
        "notificationContext": "NotificationContextTypeDef",
    },
    total=False,
)

class NotifyAppValidationOutputRequestRequestTypeDef(
    _RequiredNotifyAppValidationOutputRequestRequestTypeDef,
    _OptionalNotifyAppValidationOutputRequestRequestTypeDef,
):
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

PutAppLaunchConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppLaunchConfigurationRequestRequestTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List["ServerGroupLaunchConfigurationTypeDef"],
    },
    total=False,
)

PutAppReplicationConfigurationRequestRequestTypeDef = TypedDict(
    "PutAppReplicationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
        "serverGroupReplicationConfigurations": List["ServerGroupReplicationConfigurationTypeDef"],
    },
    total=False,
)

_RequiredPutAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutAppValidationConfigurationRequestRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalPutAppValidationConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutAppValidationConfigurationRequestRequestTypeDef",
    {
        "appValidationConfigurations": List["AppValidationConfigurationTypeDef"],
        "serverGroupValidationConfigurations": List["ServerGroupValidationConfigurationTypeDef"],
    },
    total=False,
)

class PutAppValidationConfigurationRequestRequestTypeDef(
    _RequiredPutAppValidationConfigurationRequestRequestTypeDef,
    _OptionalPutAppValidationConfigurationRequestRequestTypeDef,
):
    pass

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
        "licenseType": LicenseTypeType,
        "roleName": str,
        "latestAmiId": str,
        "state": ReplicationJobStateType,
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
    "ReplicationRunStageDetailsTypeDef",
    {
        "stage": str,
        "stageProgress": str,
    },
    total=False,
)

ReplicationRunTypeDef = TypedDict(
    "ReplicationRunTypeDef",
    {
        "replicationRunId": str,
        "state": ReplicationRunStateType,
        "type": ReplicationRunTypeType,
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
    total=False,
)

SSMOutputTypeDef = TypedDict(
    "SSMOutputTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

SSMValidationParametersTypeDef = TypedDict(
    "SSMValidationParametersTypeDef",
    {
        "source": "SourceTypeDef",
        "instanceId": str,
        "scriptType": ScriptTypeType,
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
    {
        "serverGroupId": str,
        "name": str,
        "serverList": List["ServerTypeDef"],
    },
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
        "configureScriptType": ScriptTypeType,
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
        "licenseType": LicenseTypeType,
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
    "ServerValidationOutputTypeDef",
    {
        "server": "ServerTypeDef",
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

StartAppReplicationRequestRequestTypeDef = TypedDict(
    "StartAppReplicationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

_RequiredStartOnDemandAppReplicationRequestRequestTypeDef = TypedDict(
    "_RequiredStartOnDemandAppReplicationRequestRequestTypeDef",
    {
        "appId": str,
    },
)
_OptionalStartOnDemandAppReplicationRequestRequestTypeDef = TypedDict(
    "_OptionalStartOnDemandAppReplicationRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class StartOnDemandAppReplicationRequestRequestTypeDef(
    _RequiredStartOnDemandAppReplicationRequestRequestTypeDef,
    _OptionalStartOnDemandAppReplicationRequestRequestTypeDef,
):
    pass

_RequiredStartOnDemandReplicationRunRequestRequestTypeDef = TypedDict(
    "_RequiredStartOnDemandReplicationRunRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalStartOnDemandReplicationRunRequestRequestTypeDef = TypedDict(
    "_OptionalStartOnDemandReplicationRunRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class StartOnDemandReplicationRunRequestRequestTypeDef(
    _RequiredStartOnDemandReplicationRunRequestRequestTypeDef,
    _OptionalStartOnDemandReplicationRunRequestRequestTypeDef,
):
    pass

StartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "StartOnDemandReplicationRunResponseTypeDef",
    {
        "replicationRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopAppReplicationRequestRequestTypeDef = TypedDict(
    "StopAppReplicationRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TerminateAppRequestRequestTypeDef = TypedDict(
    "TerminateAppRequestRequestTypeDef",
    {
        "appId": str,
    },
    total=False,
)

UpdateAppRequestRequestTypeDef = TypedDict(
    "UpdateAppRequestRequestTypeDef",
    {
        "appId": str,
        "name": str,
        "description": str,
        "roleName": str,
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReplicationJobRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateReplicationJobRequestRequestTypeDef",
    {
        "replicationJobId": str,
    },
)
_OptionalUpdateReplicationJobRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateReplicationJobRequestRequestTypeDef",
    {
        "frequency": int,
        "nextReplicationRunStartTime": Union[datetime, str],
        "licenseType": LicenseTypeType,
        "roleName": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

class UpdateReplicationJobRequestRequestTypeDef(
    _RequiredUpdateReplicationJobRequestRequestTypeDef,
    _OptionalUpdateReplicationJobRequestRequestTypeDef,
):
    pass

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "s3Location": "S3LocationTypeDef",
    },
    total=False,
)

UserDataValidationParametersTypeDef = TypedDict(
    "UserDataValidationParametersTypeDef",
    {
        "source": "SourceTypeDef",
        "scriptType": ScriptTypeType,
    },
    total=False,
)

ValidationOutputTypeDef = TypedDict(
    "ValidationOutputTypeDef",
    {
        "validationId": str,
        "name": str,
        "status": ValidationStatusType,
        "statusMessage": str,
        "latestValidationTime": datetime,
        "appValidationOutput": "AppValidationOutputTypeDef",
        "serverValidationOutput": "ServerValidationOutputTypeDef",
    },
    total=False,
)

VmServerAddressTypeDef = TypedDict(
    "VmServerAddressTypeDef",
    {
        "vmManagerId": str,
        "vmId": str,
    },
    total=False,
)

VmServerTypeDef = TypedDict(
    "VmServerTypeDef",
    {
        "vmServerAddress": "VmServerAddressTypeDef",
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": VmManagerTypeType,
        "vmPath": str,
    },
    total=False,
)
