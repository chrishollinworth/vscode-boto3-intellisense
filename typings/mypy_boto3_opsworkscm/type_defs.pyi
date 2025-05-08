"""
Type annotations for opsworkscm service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_opsworkscm.type_defs import AccountAttributeTypeDef

    data: AccountAttributeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    BackupStatusType,
    BackupTypeType,
    MaintenanceStatusType,
    NodeAssociationStatusType,
    ServerStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AccountAttributeTypeDef",
    "AssociateNodeRequestTypeDef",
    "AssociateNodeResponseTypeDef",
    "BackupTypeDef",
    "CreateBackupRequestTypeDef",
    "CreateBackupResponseTypeDef",
    "CreateServerRequestTypeDef",
    "CreateServerResponseTypeDef",
    "DeleteBackupRequestTypeDef",
    "DeleteServerRequestTypeDef",
    "DescribeAccountAttributesResponseTypeDef",
    "DescribeBackupsRequestPaginateTypeDef",
    "DescribeBackupsRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeEventsRequestPaginateTypeDef",
    "DescribeEventsRequestTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeNodeAssociationStatusRequestTypeDef",
    "DescribeNodeAssociationStatusRequestWaitTypeDef",
    "DescribeNodeAssociationStatusResponseTypeDef",
    "DescribeServersRequestPaginateTypeDef",
    "DescribeServersRequestTypeDef",
    "DescribeServersResponseTypeDef",
    "DisassociateNodeRequestTypeDef",
    "DisassociateNodeResponseTypeDef",
    "EngineAttributeTypeDef",
    "ExportServerEngineAttributeRequestTypeDef",
    "ExportServerEngineAttributeResponseTypeDef",
    "ListTagsForResourceRequestPaginateTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreServerRequestTypeDef",
    "RestoreServerResponseTypeDef",
    "ServerEventTypeDef",
    "ServerTypeDef",
    "StartMaintenanceRequestTypeDef",
    "StartMaintenanceResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateServerEngineAttributesRequestTypeDef",
    "UpdateServerEngineAttributesResponseTypeDef",
    "UpdateServerRequestTypeDef",
    "UpdateServerResponseTypeDef",
    "WaiterConfigTypeDef",
)

class AccountAttributeTypeDef(TypedDict):
    Name: NotRequired[str]
    Maximum: NotRequired[int]
    Used: NotRequired[int]

class EngineAttributeTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BackupTypeDef(TypedDict):
    BackupArn: NotRequired[str]
    BackupId: NotRequired[str]
    BackupType: NotRequired[BackupTypeType]
    CreatedAt: NotRequired[datetime]
    Description: NotRequired[str]
    Engine: NotRequired[str]
    EngineModel: NotRequired[str]
    EngineVersion: NotRequired[str]
    InstanceProfileArn: NotRequired[str]
    InstanceType: NotRequired[str]
    KeyPair: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    S3DataSize: NotRequired[int]
    S3DataUrl: NotRequired[str]
    S3LogUrl: NotRequired[str]
    SecurityGroupIds: NotRequired[List[str]]
    ServerName: NotRequired[str]
    ServiceRoleArn: NotRequired[str]
    Status: NotRequired[BackupStatusType]
    StatusDescription: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    ToolsVersion: NotRequired[str]
    UserArn: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class DeleteBackupRequestTypeDef(TypedDict):
    BackupId: str

class DeleteServerRequestTypeDef(TypedDict):
    ServerName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeBackupsRequestTypeDef(TypedDict):
    BackupId: NotRequired[str]
    ServerName: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeEventsRequestTypeDef(TypedDict):
    ServerName: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ServerEventTypeDef(TypedDict):
    CreatedAt: NotRequired[datetime]
    ServerName: NotRequired[str]
    Message: NotRequired[str]
    LogUrl: NotRequired[str]

class DescribeNodeAssociationStatusRequestTypeDef(TypedDict):
    NodeAssociationStatusToken: str
    ServerName: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeServersRequestTypeDef(TypedDict):
    ServerName: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class RestoreServerRequestTypeDef(TypedDict):
    BackupId: str
    ServerName: str
    InstanceType: NotRequired[str]
    KeyPair: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateServerEngineAttributesRequestTypeDef(TypedDict):
    ServerName: str
    AttributeName: str
    AttributeValue: NotRequired[str]

class UpdateServerRequestTypeDef(TypedDict):
    ServerName: str
    DisableAutomatedBackup: NotRequired[bool]
    BackupRetentionCount: NotRequired[int]
    PreferredMaintenanceWindow: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]

class AssociateNodeRequestTypeDef(TypedDict):
    ServerName: str
    NodeName: str
    EngineAttributes: Sequence[EngineAttributeTypeDef]

class DisassociateNodeRequestTypeDef(TypedDict):
    ServerName: str
    NodeName: str
    EngineAttributes: NotRequired[Sequence[EngineAttributeTypeDef]]

class ExportServerEngineAttributeRequestTypeDef(TypedDict):
    ExportAttributeName: str
    ServerName: str
    InputAttributes: NotRequired[Sequence[EngineAttributeTypeDef]]

class ServerTypeDef(TypedDict):
    AssociatePublicIpAddress: NotRequired[bool]
    BackupRetentionCount: NotRequired[int]
    ServerName: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    CloudFormationStackArn: NotRequired[str]
    CustomDomain: NotRequired[str]
    DisableAutomatedBackup: NotRequired[bool]
    Endpoint: NotRequired[str]
    Engine: NotRequired[str]
    EngineModel: NotRequired[str]
    EngineAttributes: NotRequired[List[EngineAttributeTypeDef]]
    EngineVersion: NotRequired[str]
    InstanceProfileArn: NotRequired[str]
    InstanceType: NotRequired[str]
    KeyPair: NotRequired[str]
    MaintenanceStatus: NotRequired[MaintenanceStatusType]
    PreferredMaintenanceWindow: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    SecurityGroupIds: NotRequired[List[str]]
    ServiceRoleArn: NotRequired[str]
    Status: NotRequired[ServerStatusType]
    StatusReason: NotRequired[str]
    SubnetIds: NotRequired[List[str]]
    ServerArn: NotRequired[str]

class StartMaintenanceRequestTypeDef(TypedDict):
    ServerName: str
    EngineAttributes: NotRequired[Sequence[EngineAttributeTypeDef]]

class AssociateNodeResponseTypeDef(TypedDict):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountAttributesResponseTypeDef(TypedDict):
    Attributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNodeAssociationStatusResponseTypeDef(TypedDict):
    NodeAssociationStatus: NodeAssociationStatusType
    EngineAttributes: List[EngineAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateNodeResponseTypeDef(TypedDict):
    NodeAssociationStatusToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportServerEngineAttributeResponseTypeDef(TypedDict):
    EngineAttribute: EngineAttributeTypeDef
    ServerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBackupResponseTypeDef(TypedDict):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsResponseTypeDef(TypedDict):
    Backups: List[BackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateBackupRequestTypeDef(TypedDict):
    ServerName: str
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateServerRequestTypeDef(TypedDict):
    Engine: str
    ServerName: str
    InstanceProfileArn: str
    InstanceType: str
    ServiceRoleArn: str
    AssociatePublicIpAddress: NotRequired[bool]
    CustomDomain: NotRequired[str]
    CustomCertificate: NotRequired[str]
    CustomPrivateKey: NotRequired[str]
    DisableAutomatedBackup: NotRequired[bool]
    EngineModel: NotRequired[str]
    EngineVersion: NotRequired[str]
    EngineAttributes: NotRequired[Sequence[EngineAttributeTypeDef]]
    BackupRetentionCount: NotRequired[int]
    KeyPair: NotRequired[str]
    PreferredMaintenanceWindow: NotRequired[str]
    PreferredBackupWindow: NotRequired[str]
    SecurityGroupIds: NotRequired[Sequence[str]]
    SubnetIds: NotRequired[Sequence[str]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    BackupId: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class DescribeBackupsRequestPaginateTypeDef(TypedDict):
    BackupId: NotRequired[str]
    ServerName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsRequestPaginateTypeDef(TypedDict):
    ServerName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeServersRequestPaginateTypeDef(TypedDict):
    ServerName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceRequestPaginateTypeDef(TypedDict):
    ResourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeEventsResponseTypeDef(TypedDict):
    ServerEvents: List[ServerEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeNodeAssociationStatusRequestWaitTypeDef(TypedDict):
    NodeAssociationStatusToken: str
    ServerName: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class CreateServerResponseTypeDef(TypedDict):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServersResponseTypeDef(TypedDict):
    Servers: List[ServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RestoreServerResponseTypeDef(TypedDict):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMaintenanceResponseTypeDef(TypedDict):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServerEngineAttributesResponseTypeDef(TypedDict):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServerResponseTypeDef(TypedDict):
    Server: ServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
