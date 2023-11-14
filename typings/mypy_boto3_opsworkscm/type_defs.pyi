"""
Type annotations for opsworkscm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    BackupStatusType,
    BackupTypeType,
    MaintenanceStatusType,
    NodeAssociationStatusType,
    ServerStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountAttributeTypeDef",
    "AssociateNodeRequestRequestTypeDef",
    "AssociateNodeResponseTypeDef",
    "BackupTypeDef",
    "CreateBackupRequestRequestTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateServerRequestRequestTypeDef",
    "CreateServerResponseTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteServerRequestRequestTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeEventsRequestRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeNodeAssociationStatusRequestRequestTypeDef",
    "DescribeNodeAssociationStatusResponseTypeDef",
    "DescribeServersRequestRequestTypeDef",
    "DescribeServersResponseTypeDef",
    "DisassociateNodeRequestRequestTypeDef",
    "DisassociateNodeResponseTypeDef",
    "EngineAttributeTypeDef",
    "ExportServerEngineAttributeRequestRequestTypeDef",
    "ExportServerEngineAttributeResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreServerRequestRequestTypeDef",
    "RestoreServerResponseTypeDef",
    "ServerEventTypeDef",
    "ServerTypeDef",
    "StartMaintenanceRequestRequestTypeDef",
    "StartMaintenanceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateServerEngineAttributesRequestRequestTypeDef",
    "UpdateServerEngineAttributesResponseTypeDef",
    "UpdateServerRequestRequestTypeDef",
    "UpdateServerResponseTypeDef",
    "WaiterConfigTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "Name": str,
        "Maximum": int,
        "Used": int,
    },
    total=False,
)

AssociateNodeRequestRequestTypeDef = TypedDict(
    "AssociateNodeRequestRequestTypeDef",
    {
        "ServerName": str,
        "NodeName": str,
        "EngineAttributes": List["EngineAttributeTypeDef"],
    },
)

AssociateNodeResponseTypeDef = TypedDict(
    "AssociateNodeResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": BackupTypeType,
        "CreatedAt": datetime,
        "Description": str,
        "Engine": str,
        "EngineModel": str,
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "PreferredBackupWindow": str,
        "PreferredMaintenanceWindow": str,
        "S3DataSize": int,
        "S3DataUrl": str,
        "S3LogUrl": str,
        "SecurityGroupIds": List[str],
        "ServerName": str,
        "ServiceRoleArn": str,
        "Status": BackupStatusType,
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
    },
    total=False,
)

_RequiredCreateBackupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBackupRequestRequestTypeDef",
    {
        "ServerName": str,
    },
)
_OptionalCreateBackupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBackupRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateBackupRequestRequestTypeDef(
    _RequiredCreateBackupRequestRequestTypeDef, _OptionalCreateBackupRequestRequestTypeDef
):
    pass

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServerRequestRequestTypeDef",
    {
        "Engine": str,
        "ServerName": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "ServiceRoleArn": str,
    },
)
_OptionalCreateServerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServerRequestRequestTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "CustomDomain": str,
        "CustomCertificate": str,
        "CustomPrivateKey": str,
        "DisableAutomatedBackup": bool,
        "EngineModel": str,
        "EngineVersion": str,
        "EngineAttributes": List["EngineAttributeTypeDef"],
        "BackupRetentionCount": int,
        "KeyPair": str,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
        "Tags": List["TagTypeDef"],
        "BackupId": str,
    },
    total=False,
)

class CreateServerRequestRequestTypeDef(
    _RequiredCreateServerRequestRequestTypeDef, _OptionalCreateServerRequestRequestTypeDef
):
    pass

CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupRequestRequestTypeDef = TypedDict(
    "DeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)

DeleteServerRequestRequestTypeDef = TypedDict(
    "DeleteServerRequestRequestTypeDef",
    {
        "ServerName": str,
    },
)

DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {
        "Attributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "BackupId": str,
        "ServerName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {
        "Backups": List["BackupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEventsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEventsRequestRequestTypeDef",
    {
        "ServerName": str,
    },
)
_OptionalDescribeEventsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEventsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeEventsRequestRequestTypeDef(
    _RequiredDescribeEventsRequestRequestTypeDef, _OptionalDescribeEventsRequestRequestTypeDef
):
    pass

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {
        "ServerEvents": List["ServerEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNodeAssociationStatusRequestRequestTypeDef = TypedDict(
    "DescribeNodeAssociationStatusRequestRequestTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ServerName": str,
    },
)

DescribeNodeAssociationStatusResponseTypeDef = TypedDict(
    "DescribeNodeAssociationStatusResponseTypeDef",
    {
        "NodeAssociationStatus": NodeAssociationStatusType,
        "EngineAttributes": List["EngineAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServersRequestRequestTypeDef = TypedDict(
    "DescribeServersRequestRequestTypeDef",
    {
        "ServerName": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeServersResponseTypeDef = TypedDict(
    "DescribeServersResponseTypeDef",
    {
        "Servers": List["ServerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateNodeRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateNodeRequestRequestTypeDef",
    {
        "ServerName": str,
        "NodeName": str,
    },
)
_OptionalDisassociateNodeRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateNodeRequestRequestTypeDef",
    {
        "EngineAttributes": List["EngineAttributeTypeDef"],
    },
    total=False,
)

class DisassociateNodeRequestRequestTypeDef(
    _RequiredDisassociateNodeRequestRequestTypeDef, _OptionalDisassociateNodeRequestRequestTypeDef
):
    pass

DisassociateNodeResponseTypeDef = TypedDict(
    "DisassociateNodeResponseTypeDef",
    {
        "NodeAssociationStatusToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EngineAttributeTypeDef = TypedDict(
    "EngineAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

_RequiredExportServerEngineAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredExportServerEngineAttributeRequestRequestTypeDef",
    {
        "ExportAttributeName": str,
        "ServerName": str,
    },
)
_OptionalExportServerEngineAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalExportServerEngineAttributeRequestRequestTypeDef",
    {
        "InputAttributes": List["EngineAttributeTypeDef"],
    },
    total=False,
)

class ExportServerEngineAttributeRequestRequestTypeDef(
    _RequiredExportServerEngineAttributeRequestRequestTypeDef,
    _OptionalExportServerEngineAttributeRequestRequestTypeDef,
):
    pass

ExportServerEngineAttributeResponseTypeDef = TypedDict(
    "ExportServerEngineAttributeResponseTypeDef",
    {
        "EngineAttribute": "EngineAttributeTypeDef",
        "ServerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
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

_RequiredRestoreServerRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreServerRequestRequestTypeDef",
    {
        "BackupId": str,
        "ServerName": str,
    },
)
_OptionalRestoreServerRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreServerRequestRequestTypeDef",
    {
        "InstanceType": str,
        "KeyPair": str,
    },
    total=False,
)

class RestoreServerRequestRequestTypeDef(
    _RequiredRestoreServerRequestRequestTypeDef, _OptionalRestoreServerRequestRequestTypeDef
):
    pass

RestoreServerResponseTypeDef = TypedDict(
    "RestoreServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServerEventTypeDef = TypedDict(
    "ServerEventTypeDef",
    {
        "CreatedAt": datetime,
        "ServerName": str,
        "Message": str,
        "LogUrl": str,
    },
    total=False,
)

ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "BackupRetentionCount": int,
        "ServerName": str,
        "CreatedAt": datetime,
        "CloudFormationStackArn": str,
        "CustomDomain": str,
        "DisableAutomatedBackup": bool,
        "Endpoint": str,
        "Engine": str,
        "EngineModel": str,
        "EngineAttributes": List["EngineAttributeTypeDef"],
        "EngineVersion": str,
        "InstanceProfileArn": str,
        "InstanceType": str,
        "KeyPair": str,
        "MaintenanceStatus": MaintenanceStatusType,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": ServerStatusType,
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

_RequiredStartMaintenanceRequestRequestTypeDef = TypedDict(
    "_RequiredStartMaintenanceRequestRequestTypeDef",
    {
        "ServerName": str,
    },
)
_OptionalStartMaintenanceRequestRequestTypeDef = TypedDict(
    "_OptionalStartMaintenanceRequestRequestTypeDef",
    {
        "EngineAttributes": List["EngineAttributeTypeDef"],
    },
    total=False,
)

class StartMaintenanceRequestRequestTypeDef(
    _RequiredStartMaintenanceRequestRequestTypeDef, _OptionalStartMaintenanceRequestRequestTypeDef
):
    pass

StartMaintenanceResponseTypeDef = TypedDict(
    "StartMaintenanceResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateServerEngineAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServerEngineAttributesRequestRequestTypeDef",
    {
        "ServerName": str,
        "AttributeName": str,
    },
)
_OptionalUpdateServerEngineAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServerEngineAttributesRequestRequestTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

class UpdateServerEngineAttributesRequestRequestTypeDef(
    _RequiredUpdateServerEngineAttributesRequestRequestTypeDef,
    _OptionalUpdateServerEngineAttributesRequestRequestTypeDef,
):
    pass

UpdateServerEngineAttributesResponseTypeDef = TypedDict(
    "UpdateServerEngineAttributesResponseTypeDef",
    {
        "Server": "ServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServerRequestRequestTypeDef",
    {
        "ServerName": str,
    },
)
_OptionalUpdateServerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServerRequestRequestTypeDef",
    {
        "DisableAutomatedBackup": bool,
        "BackupRetentionCount": int,
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
    },
    total=False,
)

class UpdateServerRequestRequestTypeDef(
    _RequiredUpdateServerRequestRequestTypeDef, _OptionalUpdateServerRequestRequestTypeDef
):
    pass

UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef",
    {
        "Server": "ServerTypeDef",
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
