"""
Main interface for opsworkscm service type definitions.

Usage::

    ```python
    from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = {...}
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
    "AccountAttributeTypeDef",
    "BackupTypeDef",
    "EngineAttributeTypeDef",
    "ServerEventTypeDef",
    "ServerTypeDef",
    "TagTypeDef",
    "AssociateNodeResponseTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateServerResponseTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeNodeAssociationStatusResponseTypeDef",
    "DescribeServersResponseTypeDef",
    "DisassociateNodeResponseTypeDef",
    "ExportServerEngineAttributeResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartMaintenanceResponseTypeDef",
    "UpdateServerEngineAttributesResponseTypeDef",
    "UpdateServerResponseTypeDef",
    "WaiterConfigTypeDef",
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef", {"Name": str, "Maximum": int, "Used": int}, total=False
)

BackupTypeDef = TypedDict(
    "BackupTypeDef",
    {
        "BackupArn": str,
        "BackupId": str,
        "BackupType": Literal["AUTOMATED", "MANUAL"],
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
        "Status": Literal["IN_PROGRESS", "OK", "FAILED", "DELETING"],
        "StatusDescription": str,
        "SubnetIds": List[str],
        "ToolsVersion": str,
        "UserArn": str,
    },
    total=False,
)

EngineAttributeTypeDef = TypedDict(
    "EngineAttributeTypeDef", {"Name": str, "Value": str}, total=False
)

ServerEventTypeDef = TypedDict(
    "ServerEventTypeDef",
    {"CreatedAt": datetime, "ServerName": str, "Message": str, "LogUrl": str},
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
        "MaintenanceStatus": Literal["SUCCESS", "FAILED"],
        "PreferredMaintenanceWindow": str,
        "PreferredBackupWindow": str,
        "SecurityGroupIds": List[str],
        "ServiceRoleArn": str,
        "Status": Literal[
            "BACKING_UP",
            "CONNECTION_LOST",
            "CREATING",
            "DELETING",
            "MODIFYING",
            "FAILED",
            "HEALTHY",
            "RUNNING",
            "RESTORING",
            "SETUP",
            "UNDER_MAINTENANCE",
            "UNHEALTHY",
            "TERMINATED",
        ],
        "StatusReason": str,
        "SubnetIds": List[str],
        "ServerArn": str,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

AssociateNodeResponseTypeDef = TypedDict(
    "AssociateNodeResponseTypeDef", {"NodeAssociationStatusToken": str}, total=False
)

CreateBackupResponseTypeDef = TypedDict(
    "CreateBackupResponseTypeDef", {"Backup": "BackupTypeDef"}, total=False
)

CreateServerResponseTypeDef = TypedDict(
    "CreateServerResponseTypeDef", {"Server": "ServerTypeDef"}, total=False
)

DescribeAccountAttributesResponseTypeDef = TypedDict(
    "DescribeAccountAttributesResponseTypeDef",
    {"Attributes": List["AccountAttributeTypeDef"]},
    total=False,
)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {"Backups": List["BackupTypeDef"], "NextToken": str},
    total=False,
)

DescribeEventsResponseTypeDef = TypedDict(
    "DescribeEventsResponseTypeDef",
    {"ServerEvents": List["ServerEventTypeDef"], "NextToken": str},
    total=False,
)

DescribeNodeAssociationStatusResponseTypeDef = TypedDict(
    "DescribeNodeAssociationStatusResponseTypeDef",
    {
        "NodeAssociationStatus": Literal["SUCCESS", "FAILED", "IN_PROGRESS"],
        "EngineAttributes": List["EngineAttributeTypeDef"],
    },
    total=False,
)

DescribeServersResponseTypeDef = TypedDict(
    "DescribeServersResponseTypeDef",
    {"Servers": List["ServerTypeDef"], "NextToken": str},
    total=False,
)

DisassociateNodeResponseTypeDef = TypedDict(
    "DisassociateNodeResponseTypeDef", {"NodeAssociationStatusToken": str}, total=False
)

ExportServerEngineAttributeResponseTypeDef = TypedDict(
    "ExportServerEngineAttributeResponseTypeDef",
    {"EngineAttribute": "EngineAttributeTypeDef", "ServerName": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartMaintenanceResponseTypeDef = TypedDict(
    "StartMaintenanceResponseTypeDef", {"Server": "ServerTypeDef"}, total=False
)

UpdateServerEngineAttributesResponseTypeDef = TypedDict(
    "UpdateServerEngineAttributesResponseTypeDef", {"Server": "ServerTypeDef"}, total=False
)

UpdateServerResponseTypeDef = TypedDict(
    "UpdateServerResponseTypeDef", {"Server": "ServerTypeDef"}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
