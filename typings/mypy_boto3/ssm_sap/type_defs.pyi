"""
Type annotations for ssm-sap service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm_sap/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm_sap.type_defs import ApplicationCredentialTypeDef

    data: ApplicationCredentialTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AllocationTypeType,
    ApplicationDiscoveryStatusType,
    ApplicationStatusType,
    ApplicationTypeType,
    ClusterStatusType,
    ComponentStatusType,
    ComponentTypeType,
    DatabaseConnectionMethodType,
    DatabaseStatusType,
    DatabaseTypeType,
    FilterOperatorType,
    HostRoleType,
    OperationEventStatusType,
    OperationModeType,
    OperationStatusType,
    ReplicationModeType,
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
    "ApplicationCredentialTypeDef",
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "AssociatedHostTypeDef",
    "BackintConfigTypeDef",
    "ComponentSummaryTypeDef",
    "ComponentTypeDef",
    "DatabaseConnectionTypeDef",
    "DatabaseSummaryTypeDef",
    "DatabaseTypeDef",
    "DeleteResourcePermissionInputRequestTypeDef",
    "DeleteResourcePermissionOutputTypeDef",
    "DeregisterApplicationInputRequestTypeDef",
    "FilterTypeDef",
    "GetApplicationInputRequestTypeDef",
    "GetApplicationOutputTypeDef",
    "GetComponentInputRequestTypeDef",
    "GetComponentOutputTypeDef",
    "GetDatabaseInputRequestTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetOperationInputRequestTypeDef",
    "GetOperationOutputTypeDef",
    "GetResourcePermissionInputRequestTypeDef",
    "GetResourcePermissionOutputTypeDef",
    "HostTypeDef",
    "IpAddressMemberTypeDef",
    "ListApplicationsInputRequestTypeDef",
    "ListApplicationsOutputTypeDef",
    "ListComponentsInputRequestTypeDef",
    "ListComponentsOutputTypeDef",
    "ListDatabasesInputRequestTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListOperationEventsInputRequestTypeDef",
    "ListOperationEventsOutputTypeDef",
    "ListOperationsInputRequestTypeDef",
    "ListOperationsOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OperationEventTypeDef",
    "OperationTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePermissionInputRequestTypeDef",
    "PutResourcePermissionOutputTypeDef",
    "RegisterApplicationInputRequestTypeDef",
    "RegisterApplicationOutputTypeDef",
    "ResilienceTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "StartApplicationInputRequestTypeDef",
    "StartApplicationOutputTypeDef",
    "StartApplicationRefreshInputRequestTypeDef",
    "StartApplicationRefreshOutputTypeDef",
    "StopApplicationInputRequestTypeDef",
    "StopApplicationOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationSettingsInputRequestTypeDef",
    "UpdateApplicationSettingsOutputTypeDef",
)

ApplicationCredentialTypeDef = TypedDict(
    "ApplicationCredentialTypeDef",
    {
        "DatabaseName": str,
        "CredentialType": Literal["ADMIN"],
        "SecretId": str,
    },
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "Id": str,
        "DiscoveryStatus": ApplicationDiscoveryStatusType,
        "Type": ApplicationTypeType,
        "Arn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "Id": str,
        "Type": ApplicationTypeType,
        "Arn": str,
        "AppRegistryArn": str,
        "Status": ApplicationStatusType,
        "DiscoveryStatus": ApplicationDiscoveryStatusType,
        "Components": List[str],
        "LastUpdated": datetime,
        "StatusMessage": str,
    },
    total=False,
)

AssociatedHostTypeDef = TypedDict(
    "AssociatedHostTypeDef",
    {
        "Hostname": str,
        "Ec2InstanceId": str,
        "IpAddresses": List["IpAddressMemberTypeDef"],
        "OsVersion": str,
    },
    total=False,
)

BackintConfigTypeDef = TypedDict(
    "BackintConfigTypeDef",
    {
        "BackintMode": Literal["AWSBackup"],
        "EnsureNoBackupInProcess": bool,
    },
)

ComponentSummaryTypeDef = TypedDict(
    "ComponentSummaryTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "ComponentType": ComponentTypeType,
        "Tags": Dict[str, str],
        "Arn": str,
    },
    total=False,
)

ComponentTypeDef = TypedDict(
    "ComponentTypeDef",
    {
        "ComponentId": str,
        "Sid": str,
        "SystemNumber": str,
        "ParentComponent": str,
        "ChildComponents": List[str],
        "ApplicationId": str,
        "ComponentType": ComponentTypeType,
        "Status": ComponentStatusType,
        "SapHostname": str,
        "SapFeature": str,
        "SapKernelVersion": str,
        "HdbVersion": str,
        "Resilience": "ResilienceTypeDef",
        "AssociatedHost": "AssociatedHostTypeDef",
        "Databases": List[str],
        "Hosts": List["HostTypeDef"],
        "PrimaryHost": str,
        "DatabaseConnection": "DatabaseConnectionTypeDef",
        "LastUpdated": datetime,
        "Arn": str,
    },
    total=False,
)

DatabaseConnectionTypeDef = TypedDict(
    "DatabaseConnectionTypeDef",
    {
        "DatabaseConnectionMethod": DatabaseConnectionMethodType,
        "DatabaseArn": str,
        "ConnectionIp": str,
    },
    total=False,
)

DatabaseSummaryTypeDef = TypedDict(
    "DatabaseSummaryTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "DatabaseId": str,
        "DatabaseType": DatabaseTypeType,
        "Arn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "Credentials": List["ApplicationCredentialTypeDef"],
        "DatabaseId": str,
        "DatabaseName": str,
        "DatabaseType": DatabaseTypeType,
        "Arn": str,
        "Status": DatabaseStatusType,
        "PrimaryHost": str,
        "SQLPort": int,
        "LastUpdated": datetime,
    },
    total=False,
)

_RequiredDeleteResourcePermissionInputRequestTypeDef = TypedDict(
    "_RequiredDeleteResourcePermissionInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalDeleteResourcePermissionInputRequestTypeDef = TypedDict(
    "_OptionalDeleteResourcePermissionInputRequestTypeDef",
    {
        "ActionType": Literal["RESTORE"],
        "SourceResourceArn": str,
    },
    total=False,
)

class DeleteResourcePermissionInputRequestTypeDef(
    _RequiredDeleteResourcePermissionInputRequestTypeDef,
    _OptionalDeleteResourcePermissionInputRequestTypeDef,
):
    pass

DeleteResourcePermissionOutputTypeDef = TypedDict(
    "DeleteResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterApplicationInputRequestTypeDef = TypedDict(
    "DeregisterApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Value": str,
        "Operator": FilterOperatorType,
    },
)

GetApplicationInputRequestTypeDef = TypedDict(
    "GetApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ApplicationArn": str,
        "AppRegistryArn": str,
    },
    total=False,
)

GetApplicationOutputTypeDef = TypedDict(
    "GetApplicationOutputTypeDef",
    {
        "Application": "ApplicationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetComponentInputRequestTypeDef = TypedDict(
    "GetComponentInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
    },
)

GetComponentOutputTypeDef = TypedDict(
    "GetComponentOutputTypeDef",
    {
        "Component": "ComponentTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabaseInputRequestTypeDef = TypedDict(
    "GetDatabaseInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "DatabaseId": str,
        "DatabaseArn": str,
    },
    total=False,
)

GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationInputRequestTypeDef = TypedDict(
    "GetOperationInputRequestTypeDef",
    {
        "OperationId": str,
    },
)

GetOperationOutputTypeDef = TypedDict(
    "GetOperationOutputTypeDef",
    {
        "Operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetResourcePermissionInputRequestTypeDef = TypedDict(
    "_RequiredGetResourcePermissionInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalGetResourcePermissionInputRequestTypeDef = TypedDict(
    "_OptionalGetResourcePermissionInputRequestTypeDef",
    {
        "ActionType": Literal["RESTORE"],
    },
    total=False,
)

class GetResourcePermissionInputRequestTypeDef(
    _RequiredGetResourcePermissionInputRequestTypeDef,
    _OptionalGetResourcePermissionInputRequestTypeDef,
):
    pass

GetResourcePermissionOutputTypeDef = TypedDict(
    "GetResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "HostName": str,
        "HostIp": str,
        "EC2InstanceId": str,
        "InstanceId": str,
        "HostRole": HostRoleType,
        "OsVersion": str,
    },
    total=False,
)

IpAddressMemberTypeDef = TypedDict(
    "IpAddressMemberTypeDef",
    {
        "IpAddress": str,
        "Primary": bool,
        "AllocationType": AllocationTypeType,
    },
    total=False,
)

ListApplicationsInputRequestTypeDef = TypedDict(
    "ListApplicationsInputRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

ListApplicationsOutputTypeDef = TypedDict(
    "ListApplicationsOutputTypeDef",
    {
        "Applications": List["ApplicationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsInputRequestTypeDef = TypedDict(
    "ListComponentsInputRequestTypeDef",
    {
        "ApplicationId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListComponentsOutputTypeDef = TypedDict(
    "ListComponentsOutputTypeDef",
    {
        "Components": List["ComponentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatabasesInputRequestTypeDef = TypedDict(
    "ListDatabasesInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ComponentId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "Databases": List["DatabaseSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOperationEventsInputRequestTypeDef = TypedDict(
    "_RequiredListOperationEventsInputRequestTypeDef",
    {
        "OperationId": str,
    },
)
_OptionalListOperationEventsInputRequestTypeDef = TypedDict(
    "_OptionalListOperationEventsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class ListOperationEventsInputRequestTypeDef(
    _RequiredListOperationEventsInputRequestTypeDef, _OptionalListOperationEventsInputRequestTypeDef
):
    pass

ListOperationEventsOutputTypeDef = TypedDict(
    "ListOperationEventsOutputTypeDef",
    {
        "OperationEvents": List["OperationEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListOperationsInputRequestTypeDef = TypedDict(
    "_RequiredListOperationsInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalListOperationsInputRequestTypeDef = TypedDict(
    "_OptionalListOperationsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class ListOperationsInputRequestTypeDef(
    _RequiredListOperationsInputRequestTypeDef, _OptionalListOperationsInputRequestTypeDef
):
    pass

ListOperationsOutputTypeDef = TypedDict(
    "ListOperationsOutputTypeDef",
    {
        "Operations": List["OperationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationEventTypeDef = TypedDict(
    "OperationEventTypeDef",
    {
        "Description": str,
        "Resource": "ResourceTypeDef",
        "Status": OperationEventStatusType,
        "StatusMessage": str,
        "Timestamp": datetime,
    },
    total=False,
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": str,
        "Type": str,
        "Status": OperationStatusType,
        "StatusMessage": str,
        "Properties": Dict[str, str],
        "ResourceType": str,
        "ResourceId": str,
        "ResourceArn": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "LastUpdatedTime": datetime,
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

PutResourcePermissionInputRequestTypeDef = TypedDict(
    "PutResourcePermissionInputRequestTypeDef",
    {
        "ActionType": Literal["RESTORE"],
        "SourceResourceArn": str,
        "ResourceArn": str,
    },
)

PutResourcePermissionOutputTypeDef = TypedDict(
    "PutResourcePermissionOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterApplicationInputRequestTypeDef = TypedDict(
    "_RequiredRegisterApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
        "ApplicationType": ApplicationTypeType,
        "Instances": List[str],
    },
)
_OptionalRegisterApplicationInputRequestTypeDef = TypedDict(
    "_OptionalRegisterApplicationInputRequestTypeDef",
    {
        "SapInstanceNumber": str,
        "Sid": str,
        "Tags": Dict[str, str],
        "Credentials": List["ApplicationCredentialTypeDef"],
        "DatabaseArn": str,
    },
    total=False,
)

class RegisterApplicationInputRequestTypeDef(
    _RequiredRegisterApplicationInputRequestTypeDef, _OptionalRegisterApplicationInputRequestTypeDef
):
    pass

RegisterApplicationOutputTypeDef = TypedDict(
    "RegisterApplicationOutputTypeDef",
    {
        "Application": "ApplicationTypeDef",
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResilienceTypeDef = TypedDict(
    "ResilienceTypeDef",
    {
        "HsrTier": str,
        "HsrReplicationMode": ReplicationModeType,
        "HsrOperationMode": OperationModeType,
        "ClusterStatus": ClusterStatusType,
        "EnqueueReplication": bool,
    },
    total=False,
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
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

StartApplicationInputRequestTypeDef = TypedDict(
    "StartApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

StartApplicationOutputTypeDef = TypedDict(
    "StartApplicationOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartApplicationRefreshInputRequestTypeDef = TypedDict(
    "StartApplicationRefreshInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

StartApplicationRefreshOutputTypeDef = TypedDict(
    "StartApplicationRefreshOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopApplicationInputRequestTypeDef = TypedDict(
    "_RequiredStopApplicationInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalStopApplicationInputRequestTypeDef = TypedDict(
    "_OptionalStopApplicationInputRequestTypeDef",
    {
        "StopConnectedEntity": Literal["DBMS"],
        "IncludeEc2InstanceShutdown": bool,
    },
    total=False,
)

class StopApplicationInputRequestTypeDef(
    _RequiredStopApplicationInputRequestTypeDef, _OptionalStopApplicationInputRequestTypeDef
):
    pass

StopApplicationOutputTypeDef = TypedDict(
    "StopApplicationOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateApplicationSettingsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationSettingsInputRequestTypeDef",
    {
        "ApplicationId": str,
    },
)
_OptionalUpdateApplicationSettingsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationSettingsInputRequestTypeDef",
    {
        "CredentialsToAddOrUpdate": List["ApplicationCredentialTypeDef"],
        "CredentialsToRemove": List["ApplicationCredentialTypeDef"],
        "Backint": "BackintConfigTypeDef",
        "DatabaseArn": str,
    },
    total=False,
)

class UpdateApplicationSettingsInputRequestTypeDef(
    _RequiredUpdateApplicationSettingsInputRequestTypeDef,
    _OptionalUpdateApplicationSettingsInputRequestTypeDef,
):
    pass

UpdateApplicationSettingsOutputTypeDef = TypedDict(
    "UpdateApplicationSettingsOutputTypeDef",
    {
        "Message": str,
        "OperationIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
