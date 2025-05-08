"""
Type annotations for cloudhsmv2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef

    data: BackupRetentionPolicyTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import (
    BackupStateType,
    ClusterModeType,
    ClusterStateType,
    HsmStateType,
    NetworkTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "BackupRetentionPolicyTypeDef",
    "BackupTypeDef",
    "CertificatesTypeDef",
    "ClusterTypeDef",
    "CopyBackupToRegionRequestTypeDef",
    "CopyBackupToRegionResponseTypeDef",
    "CreateClusterRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateHsmRequestTypeDef",
    "CreateHsmResponseTypeDef",
    "DeleteBackupRequestTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteClusterRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteHsmRequestTypeDef",
    "DeleteHsmResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "DescribeBackupsRequestPaginateTypeDef",
    "DescribeBackupsRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeClustersRequestPaginateTypeDef",
    "DescribeClustersRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DestinationBackupTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "HsmTypeDef",
    "InitializeClusterRequestTypeDef",
    "InitializeClusterResponseTypeDef",
    "ListTagsRequestPaginateTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ModifyBackupAttributesRequestTypeDef",
    "ModifyBackupAttributesResponseTypeDef",
    "ModifyClusterRequestTypeDef",
    "ModifyClusterResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreBackupRequestTypeDef",
    "RestoreBackupResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
)

BackupRetentionPolicyTypeDef = TypedDict(
    "BackupRetentionPolicyTypeDef",
    {
        "Type": NotRequired[Literal["DAYS"]],
        "Value": NotRequired[str],
    },
)

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CertificatesTypeDef(TypedDict):
    ClusterCsr: NotRequired[str]
    HsmCertificate: NotRequired[str]
    AwsHardwareCertificate: NotRequired[str]
    ManufacturerHardwareCertificate: NotRequired[str]
    ClusterCertificate: NotRequired[str]

class HsmTypeDef(TypedDict):
    HsmId: str
    AvailabilityZone: NotRequired[str]
    ClusterId: NotRequired[str]
    SubnetId: NotRequired[str]
    EniId: NotRequired[str]
    EniIp: NotRequired[str]
    EniIpV6: NotRequired[str]
    HsmType: NotRequired[str]
    State: NotRequired[HsmStateType]
    StateMessage: NotRequired[str]

class DestinationBackupTypeDef(TypedDict):
    CreateTimestamp: NotRequired[datetime]
    SourceRegion: NotRequired[str]
    SourceBackup: NotRequired[str]
    SourceCluster: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateHsmRequestTypeDef(TypedDict):
    ClusterId: str
    AvailabilityZone: str
    IpAddress: NotRequired[str]

class DeleteBackupRequestTypeDef(TypedDict):
    BackupId: str

class DeleteClusterRequestTypeDef(TypedDict):
    ClusterId: str

class DeleteHsmRequestTypeDef(TypedDict):
    ClusterId: str
    HsmId: NotRequired[str]
    EniId: NotRequired[str]
    EniIp: NotRequired[str]

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeBackupsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    Filters: NotRequired[Mapping[str, Sequence[str]]]
    Shared: NotRequired[bool]
    SortAscending: NotRequired[bool]

class DescribeClustersRequestTypeDef(TypedDict):
    Filters: NotRequired[Mapping[str, Sequence[str]]]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: NotRequired[str]

class InitializeClusterRequestTypeDef(TypedDict):
    ClusterId: str
    SignedCert: str
    TrustAnchor: str

class ListTagsRequestTypeDef(TypedDict):
    ResourceId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ModifyBackupAttributesRequestTypeDef(TypedDict):
    BackupId: str
    NeverExpires: bool

class PutResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    Policy: NotRequired[str]

class RestoreBackupRequestTypeDef(TypedDict):
    BackupId: str

class UntagResourceRequestTypeDef(TypedDict):
    ResourceId: str
    TagKeyList: Sequence[str]

class ModifyClusterRequestTypeDef(TypedDict):
    ClusterId: str
    HsmType: NotRequired[str]
    BackupRetentionPolicy: NotRequired[BackupRetentionPolicyTypeDef]

class BackupTypeDef(TypedDict):
    BackupId: str
    BackupArn: NotRequired[str]
    BackupState: NotRequired[BackupStateType]
    ClusterId: NotRequired[str]
    CreateTimestamp: NotRequired[datetime]
    CopyTimestamp: NotRequired[datetime]
    NeverExpires: NotRequired[bool]
    SourceRegion: NotRequired[str]
    SourceBackup: NotRequired[str]
    SourceCluster: NotRequired[str]
    DeleteTimestamp: NotRequired[datetime]
    TagList: NotRequired[List[TagTypeDef]]
    HsmType: NotRequired[str]
    Mode: NotRequired[ClusterModeType]

class CopyBackupToRegionRequestTypeDef(TypedDict):
    DestinationRegion: str
    BackupId: str
    TagList: NotRequired[Sequence[TagTypeDef]]

class CreateClusterRequestTypeDef(TypedDict):
    HsmType: str
    SubnetIds: Sequence[str]
    BackupRetentionPolicy: NotRequired[BackupRetentionPolicyTypeDef]
    SourceBackupId: NotRequired[str]
    NetworkType: NotRequired[NetworkTypeType]
    TagList: NotRequired[Sequence[TagTypeDef]]
    Mode: NotRequired[ClusterModeType]

class TagResourceRequestTypeDef(TypedDict):
    ResourceId: str
    TagList: Sequence[TagTypeDef]

class ClusterTypeDef(TypedDict):
    BackupPolicy: NotRequired[Literal["DEFAULT"]]
    BackupRetentionPolicy: NotRequired[BackupRetentionPolicyTypeDef]
    ClusterId: NotRequired[str]
    CreateTimestamp: NotRequired[datetime]
    Hsms: NotRequired[List[HsmTypeDef]]
    HsmType: NotRequired[str]
    HsmTypeRollbackExpiration: NotRequired[datetime]
    PreCoPassword: NotRequired[str]
    SecurityGroup: NotRequired[str]
    SourceBackupId: NotRequired[str]
    State: NotRequired[ClusterStateType]
    StateMessage: NotRequired[str]
    SubnetMapping: NotRequired[Dict[str, str]]
    VpcId: NotRequired[str]
    NetworkType: NotRequired[NetworkTypeType]
    Certificates: NotRequired[CertificatesTypeDef]
    TagList: NotRequired[List[TagTypeDef]]
    Mode: NotRequired[ClusterModeType]

class CopyBackupToRegionResponseTypeDef(TypedDict):
    DestinationBackup: DestinationBackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmResponseTypeDef(TypedDict):
    Hsm: HsmTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHsmResponseTypeDef(TypedDict):
    HsmId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyResponseTypeDef(TypedDict):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitializeClusterResponseTypeDef(TypedDict):
    State: ClusterStateType
    StateMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutResourcePolicyResponseTypeDef(TypedDict):
    ResourceArn: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Mapping[str, Sequence[str]]]
    Shared: NotRequired[bool]
    SortAscending: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeClustersRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[Mapping[str, Sequence[str]]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsRequestPaginateTypeDef(TypedDict):
    ResourceId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DeleteBackupResponseTypeDef(TypedDict):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupsResponseTypeDef(TypedDict):
    Backups: List[BackupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ModifyBackupAttributesResponseTypeDef(TypedDict):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreBackupResponseTypeDef(TypedDict):
    Backup: BackupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersResponseTypeDef(TypedDict):
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ModifyClusterResponseTypeDef(TypedDict):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
