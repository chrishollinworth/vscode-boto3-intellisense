"""
Type annotations for redshift-serverless service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_serverless/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift_serverless.type_defs import ConfigParameterTypeDef

    data: ConfigParameterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    LogExportType,
    NamespaceStatusType,
    SnapshotStatusType,
    UsageLimitBreachActionType,
    UsageLimitPeriodType,
    UsageLimitUsageTypeType,
    WorkgroupStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ConfigParameterTypeDef",
    "ConvertRecoveryPointToSnapshotRequestRequestTypeDef",
    "ConvertRecoveryPointToSnapshotResponseTypeDef",
    "CreateEndpointAccessRequestRequestTypeDef",
    "CreateEndpointAccessResponseTypeDef",
    "CreateNamespaceRequestRequestTypeDef",
    "CreateNamespaceResponseTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResponseTypeDef",
    "CreateUsageLimitRequestRequestTypeDef",
    "CreateUsageLimitResponseTypeDef",
    "CreateWorkgroupRequestRequestTypeDef",
    "CreateWorkgroupResponseTypeDef",
    "DeleteEndpointAccessRequestRequestTypeDef",
    "DeleteEndpointAccessResponseTypeDef",
    "DeleteNamespaceRequestRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotResponseTypeDef",
    "DeleteUsageLimitRequestRequestTypeDef",
    "DeleteUsageLimitResponseTypeDef",
    "DeleteWorkgroupRequestRequestTypeDef",
    "DeleteWorkgroupResponseTypeDef",
    "EndpointAccessTypeDef",
    "EndpointTypeDef",
    "GetCredentialsRequestRequestTypeDef",
    "GetCredentialsResponseTypeDef",
    "GetEndpointAccessRequestRequestTypeDef",
    "GetEndpointAccessResponseTypeDef",
    "GetNamespaceRequestRequestTypeDef",
    "GetNamespaceResponseTypeDef",
    "GetRecoveryPointRequestRequestTypeDef",
    "GetRecoveryPointResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSnapshotRequestRequestTypeDef",
    "GetSnapshotResponseTypeDef",
    "GetUsageLimitRequestRequestTypeDef",
    "GetUsageLimitResponseTypeDef",
    "GetWorkgroupRequestRequestTypeDef",
    "GetWorkgroupResponseTypeDef",
    "ListEndpointAccessRequestRequestTypeDef",
    "ListEndpointAccessResponseTypeDef",
    "ListNamespacesRequestRequestTypeDef",
    "ListNamespacesResponseTypeDef",
    "ListRecoveryPointsRequestRequestTypeDef",
    "ListRecoveryPointsResponseTypeDef",
    "ListSnapshotsRequestRequestTypeDef",
    "ListSnapshotsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsageLimitsRequestRequestTypeDef",
    "ListUsageLimitsResponseTypeDef",
    "ListWorkgroupsRequestRequestTypeDef",
    "ListWorkgroupsResponseTypeDef",
    "NamespaceTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RecoveryPointTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreFromRecoveryPointRequestRequestTypeDef",
    "RestoreFromRecoveryPointResponseTypeDef",
    "RestoreFromSnapshotRequestRequestTypeDef",
    "RestoreFromSnapshotResponseTypeDef",
    "SnapshotTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEndpointAccessRequestRequestTypeDef",
    "UpdateEndpointAccessResponseTypeDef",
    "UpdateNamespaceRequestRequestTypeDef",
    "UpdateNamespaceResponseTypeDef",
    "UpdateSnapshotRequestRequestTypeDef",
    "UpdateSnapshotResponseTypeDef",
    "UpdateUsageLimitRequestRequestTypeDef",
    "UpdateUsageLimitResponseTypeDef",
    "UpdateWorkgroupRequestRequestTypeDef",
    "UpdateWorkgroupResponseTypeDef",
    "UsageLimitTypeDef",
    "VpcEndpointTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WorkgroupTypeDef",
)

ConfigParameterTypeDef = TypedDict(
    "ConfigParameterTypeDef",
    {
        "parameterKey": str,
        "parameterValue": str,
    },
    total=False,
)

_RequiredConvertRecoveryPointToSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredConvertRecoveryPointToSnapshotRequestRequestTypeDef",
    {
        "recoveryPointId": str,
        "snapshotName": str,
    },
)
_OptionalConvertRecoveryPointToSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalConvertRecoveryPointToSnapshotRequestRequestTypeDef",
    {
        "retentionPeriod": int,
    },
    total=False,
)

class ConvertRecoveryPointToSnapshotRequestRequestTypeDef(
    _RequiredConvertRecoveryPointToSnapshotRequestRequestTypeDef,
    _OptionalConvertRecoveryPointToSnapshotRequestRequestTypeDef,
):
    pass

ConvertRecoveryPointToSnapshotResponseTypeDef = TypedDict(
    "ConvertRecoveryPointToSnapshotResponseTypeDef",
    {
        "snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEndpointAccessRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEndpointAccessRequestRequestTypeDef",
    {
        "endpointName": str,
        "subnetIds": List[str],
        "workgroupName": str,
    },
)
_OptionalCreateEndpointAccessRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEndpointAccessRequestRequestTypeDef",
    {
        "vpcSecurityGroupIds": List[str],
    },
    total=False,
)

class CreateEndpointAccessRequestRequestTypeDef(
    _RequiredCreateEndpointAccessRequestRequestTypeDef,
    _OptionalCreateEndpointAccessRequestRequestTypeDef,
):
    pass

CreateEndpointAccessResponseTypeDef = TypedDict(
    "CreateEndpointAccessResponseTypeDef",
    {
        "endpoint": "EndpointAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNamespaceRequestRequestTypeDef",
    {
        "namespaceName": str,
    },
)
_OptionalCreateNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNamespaceRequestRequestTypeDef",
    {
        "adminUserPassword": str,
        "adminUsername": str,
        "dbName": str,
        "defaultIamRoleArn": str,
        "iamRoles": List[str],
        "kmsKeyId": str,
        "logExports": List[LogExportType],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateNamespaceRequestRequestTypeDef(
    _RequiredCreateNamespaceRequestRequestTypeDef, _OptionalCreateNamespaceRequestRequestTypeDef
):
    pass

CreateNamespaceResponseTypeDef = TypedDict(
    "CreateNamespaceResponseTypeDef",
    {
        "namespace": "NamespaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestRequestTypeDef",
    {
        "namespaceName": str,
        "snapshotName": str,
    },
)
_OptionalCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestRequestTypeDef",
    {
        "retentionPeriod": int,
    },
    total=False,
)

class CreateSnapshotRequestRequestTypeDef(
    _RequiredCreateSnapshotRequestRequestTypeDef, _OptionalCreateSnapshotRequestRequestTypeDef
):
    pass

CreateSnapshotResponseTypeDef = TypedDict(
    "CreateSnapshotResponseTypeDef",
    {
        "snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUsageLimitRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUsageLimitRequestRequestTypeDef",
    {
        "amount": int,
        "resourceArn": str,
        "usageType": UsageLimitUsageTypeType,
    },
)
_OptionalCreateUsageLimitRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUsageLimitRequestRequestTypeDef",
    {
        "breachAction": UsageLimitBreachActionType,
        "period": UsageLimitPeriodType,
    },
    total=False,
)

class CreateUsageLimitRequestRequestTypeDef(
    _RequiredCreateUsageLimitRequestRequestTypeDef, _OptionalCreateUsageLimitRequestRequestTypeDef
):
    pass

CreateUsageLimitResponseTypeDef = TypedDict(
    "CreateUsageLimitResponseTypeDef",
    {
        "usageLimit": "UsageLimitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWorkgroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWorkgroupRequestRequestTypeDef",
    {
        "namespaceName": str,
        "workgroupName": str,
    },
)
_OptionalCreateWorkgroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWorkgroupRequestRequestTypeDef",
    {
        "baseCapacity": int,
        "configParameters": List["ConfigParameterTypeDef"],
        "enhancedVpcRouting": bool,
        "publiclyAccessible": bool,
        "securityGroupIds": List[str],
        "subnetIds": List[str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateWorkgroupRequestRequestTypeDef(
    _RequiredCreateWorkgroupRequestRequestTypeDef, _OptionalCreateWorkgroupRequestRequestTypeDef
):
    pass

CreateWorkgroupResponseTypeDef = TypedDict(
    "CreateWorkgroupResponseTypeDef",
    {
        "workgroup": "WorkgroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEndpointAccessRequestRequestTypeDef = TypedDict(
    "DeleteEndpointAccessRequestRequestTypeDef",
    {
        "endpointName": str,
    },
)

DeleteEndpointAccessResponseTypeDef = TypedDict(
    "DeleteEndpointAccessResponseTypeDef",
    {
        "endpoint": "EndpointAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNamespaceRequestRequestTypeDef",
    {
        "namespaceName": str,
    },
)
_OptionalDeleteNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNamespaceRequestRequestTypeDef",
    {
        "finalSnapshotName": str,
        "finalSnapshotRetentionPeriod": int,
    },
    total=False,
)

class DeleteNamespaceRequestRequestTypeDef(
    _RequiredDeleteNamespaceRequestRequestTypeDef, _OptionalDeleteNamespaceRequestRequestTypeDef
):
    pass

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "namespace": "NamespaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

DeleteSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteSnapshotRequestRequestTypeDef",
    {
        "snapshotName": str,
    },
)

DeleteSnapshotResponseTypeDef = TypedDict(
    "DeleteSnapshotResponseTypeDef",
    {
        "snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUsageLimitRequestRequestTypeDef = TypedDict(
    "DeleteUsageLimitRequestRequestTypeDef",
    {
        "usageLimitId": str,
    },
)

DeleteUsageLimitResponseTypeDef = TypedDict(
    "DeleteUsageLimitResponseTypeDef",
    {
        "usageLimit": "UsageLimitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkgroupRequestRequestTypeDef = TypedDict(
    "DeleteWorkgroupRequestRequestTypeDef",
    {
        "workgroupName": str,
    },
)

DeleteWorkgroupResponseTypeDef = TypedDict(
    "DeleteWorkgroupResponseTypeDef",
    {
        "workgroup": "WorkgroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndpointAccessTypeDef = TypedDict(
    "EndpointAccessTypeDef",
    {
        "address": str,
        "endpointArn": str,
        "endpointCreateTime": datetime,
        "endpointName": str,
        "endpointStatus": str,
        "port": int,
        "subnetIds": List[str],
        "vpcEndpoint": "VpcEndpointTypeDef",
        "vpcSecurityGroups": List["VpcSecurityGroupMembershipTypeDef"],
        "workgroupName": str,
    },
    total=False,
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "address": str,
        "port": int,
        "vpcEndpoints": List["VpcEndpointTypeDef"],
    },
    total=False,
)

_RequiredGetCredentialsRequestRequestTypeDef = TypedDict(
    "_RequiredGetCredentialsRequestRequestTypeDef",
    {
        "workgroupName": str,
    },
)
_OptionalGetCredentialsRequestRequestTypeDef = TypedDict(
    "_OptionalGetCredentialsRequestRequestTypeDef",
    {
        "dbName": str,
        "durationSeconds": int,
    },
    total=False,
)

class GetCredentialsRequestRequestTypeDef(
    _RequiredGetCredentialsRequestRequestTypeDef, _OptionalGetCredentialsRequestRequestTypeDef
):
    pass

GetCredentialsResponseTypeDef = TypedDict(
    "GetCredentialsResponseTypeDef",
    {
        "dbPassword": str,
        "dbUser": str,
        "expiration": datetime,
        "nextRefreshTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEndpointAccessRequestRequestTypeDef = TypedDict(
    "GetEndpointAccessRequestRequestTypeDef",
    {
        "endpointName": str,
    },
)

GetEndpointAccessResponseTypeDef = TypedDict(
    "GetEndpointAccessResponseTypeDef",
    {
        "endpoint": "EndpointAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamespaceRequestRequestTypeDef = TypedDict(
    "GetNamespaceRequestRequestTypeDef",
    {
        "namespaceName": str,
    },
)

GetNamespaceResponseTypeDef = TypedDict(
    "GetNamespaceResponseTypeDef",
    {
        "namespace": "NamespaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecoveryPointRequestRequestTypeDef = TypedDict(
    "GetRecoveryPointRequestRequestTypeDef",
    {
        "recoveryPointId": str,
    },
)

GetRecoveryPointResponseTypeDef = TypedDict(
    "GetRecoveryPointResponseTypeDef",
    {
        "recoveryPoint": "RecoveryPointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "resourcePolicy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotRequestRequestTypeDef = TypedDict(
    "GetSnapshotRequestRequestTypeDef",
    {
        "ownerAccount": str,
        "snapshotArn": str,
        "snapshotName": str,
    },
    total=False,
)

GetSnapshotResponseTypeDef = TypedDict(
    "GetSnapshotResponseTypeDef",
    {
        "snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUsageLimitRequestRequestTypeDef = TypedDict(
    "GetUsageLimitRequestRequestTypeDef",
    {
        "usageLimitId": str,
    },
)

GetUsageLimitResponseTypeDef = TypedDict(
    "GetUsageLimitResponseTypeDef",
    {
        "usageLimit": "UsageLimitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkgroupRequestRequestTypeDef = TypedDict(
    "GetWorkgroupRequestRequestTypeDef",
    {
        "workgroupName": str,
    },
)

GetWorkgroupResponseTypeDef = TypedDict(
    "GetWorkgroupResponseTypeDef",
    {
        "workgroup": "WorkgroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointAccessRequestRequestTypeDef = TypedDict(
    "ListEndpointAccessRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "vpcId": str,
        "workgroupName": str,
    },
    total=False,
)

ListEndpointAccessResponseTypeDef = TypedDict(
    "ListEndpointAccessResponseTypeDef",
    {
        "endpoints": List["EndpointAccessTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamespacesRequestRequestTypeDef = TypedDict(
    "ListNamespacesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListNamespacesResponseTypeDef = TypedDict(
    "ListNamespacesResponseTypeDef",
    {
        "namespaces": List["NamespaceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecoveryPointsRequestRequestTypeDef = TypedDict(
    "ListRecoveryPointsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "maxResults": int,
        "namespaceName": str,
        "nextToken": str,
        "startTime": Union[datetime, str],
    },
    total=False,
)

ListRecoveryPointsResponseTypeDef = TypedDict(
    "ListRecoveryPointsResponseTypeDef",
    {
        "nextToken": str,
        "recoveryPoints": List["RecoveryPointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSnapshotsRequestRequestTypeDef = TypedDict(
    "ListSnapshotsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "maxResults": int,
        "namespaceArn": str,
        "namespaceName": str,
        "nextToken": str,
        "ownerAccount": str,
        "startTime": Union[datetime, str],
    },
    total=False,
)

ListSnapshotsResponseTypeDef = TypedDict(
    "ListSnapshotsResponseTypeDef",
    {
        "nextToken": str,
        "snapshots": List["SnapshotTypeDef"],
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsageLimitsRequestRequestTypeDef = TypedDict(
    "ListUsageLimitsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resourceArn": str,
        "usageType": UsageLimitUsageTypeType,
    },
    total=False,
)

ListUsageLimitsResponseTypeDef = TypedDict(
    "ListUsageLimitsResponseTypeDef",
    {
        "nextToken": str,
        "usageLimits": List["UsageLimitTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkgroupsRequestRequestTypeDef = TypedDict(
    "ListWorkgroupsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListWorkgroupsResponseTypeDef = TypedDict(
    "ListWorkgroupsResponseTypeDef",
    {
        "nextToken": str,
        "workgroups": List["WorkgroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NamespaceTypeDef = TypedDict(
    "NamespaceTypeDef",
    {
        "adminUsername": str,
        "creationDate": datetime,
        "dbName": str,
        "defaultIamRoleArn": str,
        "iamRoles": List[str],
        "kmsKeyId": str,
        "logExports": List[LogExportType],
        "namespaceArn": str,
        "namespaceId": str,
        "namespaceName": str,
        "status": NamespaceStatusType,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "availabilityZone": str,
        "networkInterfaceId": str,
        "privateIpAddress": str,
        "subnetId": str,
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

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "resourcePolicy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecoveryPointTypeDef = TypedDict(
    "RecoveryPointTypeDef",
    {
        "namespaceName": str,
        "recoveryPointCreateTime": datetime,
        "recoveryPointId": str,
        "totalSizeInMegaBytes": float,
        "workgroupName": str,
    },
    total=False,
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policy": str,
        "resourceArn": str,
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

RestoreFromRecoveryPointRequestRequestTypeDef = TypedDict(
    "RestoreFromRecoveryPointRequestRequestTypeDef",
    {
        "namespaceName": str,
        "recoveryPointId": str,
        "workgroupName": str,
    },
)

RestoreFromRecoveryPointResponseTypeDef = TypedDict(
    "RestoreFromRecoveryPointResponseTypeDef",
    {
        "namespace": "NamespaceTypeDef",
        "recoveryPointId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreFromSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreFromSnapshotRequestRequestTypeDef",
    {
        "namespaceName": str,
        "workgroupName": str,
    },
)
_OptionalRestoreFromSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreFromSnapshotRequestRequestTypeDef",
    {
        "ownerAccount": str,
        "snapshotArn": str,
        "snapshotName": str,
    },
    total=False,
)

class RestoreFromSnapshotRequestRequestTypeDef(
    _RequiredRestoreFromSnapshotRequestRequestTypeDef,
    _OptionalRestoreFromSnapshotRequestRequestTypeDef,
):
    pass

RestoreFromSnapshotResponseTypeDef = TypedDict(
    "RestoreFromSnapshotResponseTypeDef",
    {
        "namespace": "NamespaceTypeDef",
        "ownerAccount": str,
        "snapshotName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "accountsWithProvisionedRestoreAccess": List[str],
        "accountsWithRestoreAccess": List[str],
        "actualIncrementalBackupSizeInMegaBytes": float,
        "adminUsername": str,
        "backupProgressInMegaBytes": float,
        "currentBackupRateInMegaBytesPerSecond": float,
        "elapsedTimeInSeconds": int,
        "estimatedSecondsToCompletion": int,
        "kmsKeyId": str,
        "namespaceArn": str,
        "namespaceName": str,
        "ownerAccount": str,
        "snapshotArn": str,
        "snapshotCreateTime": datetime,
        "snapshotName": str,
        "snapshotRemainingDays": int,
        "snapshotRetentionPeriod": int,
        "snapshotRetentionStartTime": datetime,
        "status": SnapshotStatusType,
        "totalBackupSizeInMegaBytes": float,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateEndpointAccessRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEndpointAccessRequestRequestTypeDef",
    {
        "endpointName": str,
    },
)
_OptionalUpdateEndpointAccessRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEndpointAccessRequestRequestTypeDef",
    {
        "vpcSecurityGroupIds": List[str],
    },
    total=False,
)

class UpdateEndpointAccessRequestRequestTypeDef(
    _RequiredUpdateEndpointAccessRequestRequestTypeDef,
    _OptionalUpdateEndpointAccessRequestRequestTypeDef,
):
    pass

UpdateEndpointAccessResponseTypeDef = TypedDict(
    "UpdateEndpointAccessResponseTypeDef",
    {
        "endpoint": "EndpointAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNamespaceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateNamespaceRequestRequestTypeDef",
    {
        "namespaceName": str,
    },
)
_OptionalUpdateNamespaceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateNamespaceRequestRequestTypeDef",
    {
        "adminUserPassword": str,
        "adminUsername": str,
        "defaultIamRoleArn": str,
        "iamRoles": List[str],
        "kmsKeyId": str,
        "logExports": List[LogExportType],
    },
    total=False,
)

class UpdateNamespaceRequestRequestTypeDef(
    _RequiredUpdateNamespaceRequestRequestTypeDef, _OptionalUpdateNamespaceRequestRequestTypeDef
):
    pass

UpdateNamespaceResponseTypeDef = TypedDict(
    "UpdateNamespaceResponseTypeDef",
    {
        "namespace": "NamespaceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSnapshotRequestRequestTypeDef",
    {
        "snapshotName": str,
    },
)
_OptionalUpdateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSnapshotRequestRequestTypeDef",
    {
        "retentionPeriod": int,
    },
    total=False,
)

class UpdateSnapshotRequestRequestTypeDef(
    _RequiredUpdateSnapshotRequestRequestTypeDef, _OptionalUpdateSnapshotRequestRequestTypeDef
):
    pass

UpdateSnapshotResponseTypeDef = TypedDict(
    "UpdateSnapshotResponseTypeDef",
    {
        "snapshot": "SnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateUsageLimitRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateUsageLimitRequestRequestTypeDef",
    {
        "usageLimitId": str,
    },
)
_OptionalUpdateUsageLimitRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateUsageLimitRequestRequestTypeDef",
    {
        "amount": int,
        "breachAction": UsageLimitBreachActionType,
    },
    total=False,
)

class UpdateUsageLimitRequestRequestTypeDef(
    _RequiredUpdateUsageLimitRequestRequestTypeDef, _OptionalUpdateUsageLimitRequestRequestTypeDef
):
    pass

UpdateUsageLimitResponseTypeDef = TypedDict(
    "UpdateUsageLimitResponseTypeDef",
    {
        "usageLimit": "UsageLimitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWorkgroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWorkgroupRequestRequestTypeDef",
    {
        "workgroupName": str,
    },
)
_OptionalUpdateWorkgroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWorkgroupRequestRequestTypeDef",
    {
        "baseCapacity": int,
        "configParameters": List["ConfigParameterTypeDef"],
        "enhancedVpcRouting": bool,
        "publiclyAccessible": bool,
        "securityGroupIds": List[str],
        "subnetIds": List[str],
    },
    total=False,
)

class UpdateWorkgroupRequestRequestTypeDef(
    _RequiredUpdateWorkgroupRequestRequestTypeDef, _OptionalUpdateWorkgroupRequestRequestTypeDef
):
    pass

UpdateWorkgroupResponseTypeDef = TypedDict(
    "UpdateWorkgroupResponseTypeDef",
    {
        "workgroup": "WorkgroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsageLimitTypeDef = TypedDict(
    "UsageLimitTypeDef",
    {
        "amount": int,
        "breachAction": UsageLimitBreachActionType,
        "period": UsageLimitPeriodType,
        "resourceArn": str,
        "usageLimitArn": str,
        "usageLimitId": str,
        "usageType": UsageLimitUsageTypeType,
    },
    total=False,
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "vpcEndpointId": str,
        "vpcId": str,
    },
    total=False,
)

VpcSecurityGroupMembershipTypeDef = TypedDict(
    "VpcSecurityGroupMembershipTypeDef",
    {
        "status": str,
        "vpcSecurityGroupId": str,
    },
    total=False,
)

WorkgroupTypeDef = TypedDict(
    "WorkgroupTypeDef",
    {
        "baseCapacity": int,
        "configParameters": List["ConfigParameterTypeDef"],
        "creationDate": datetime,
        "endpoint": "EndpointTypeDef",
        "enhancedVpcRouting": bool,
        "namespaceName": str,
        "publiclyAccessible": bool,
        "securityGroupIds": List[str],
        "status": WorkgroupStatusType,
        "subnetIds": List[str],
        "workgroupArn": str,
        "workgroupId": str,
        "workgroupName": str,
    },
    total=False,
)