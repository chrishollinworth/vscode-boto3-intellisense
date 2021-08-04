"""
Type annotations for cloudhsmv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudhsmv2.type_defs import BackupRetentionPolicyTypeDef

    data: BackupRetentionPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import BackupStateType, ClusterStateType, HsmStateType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "BackupRetentionPolicyTypeDef",
    "BackupTypeDef",
    "CertificatesTypeDef",
    "ClusterTypeDef",
    "CopyBackupToRegionRequestRequestTypeDef",
    "CopyBackupToRegionResponseTypeDef",
    "CreateClusterRequestRequestTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateHsmRequestRequestTypeDef",
    "CreateHsmResponseTypeDef",
    "DeleteBackupRequestRequestTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteClusterRequestRequestTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteHsmRequestRequestTypeDef",
    "DeleteHsmResponseTypeDef",
    "DescribeBackupsRequestRequestTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeClustersRequestRequestTypeDef",
    "DescribeClustersResponseTypeDef",
    "DestinationBackupTypeDef",
    "HsmTypeDef",
    "InitializeClusterRequestRequestTypeDef",
    "InitializeClusterResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ModifyBackupAttributesRequestRequestTypeDef",
    "ModifyBackupAttributesResponseTypeDef",
    "ModifyClusterRequestRequestTypeDef",
    "ModifyClusterResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreBackupRequestRequestTypeDef",
    "RestoreBackupResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

BackupRetentionPolicyTypeDef = TypedDict(
    "BackupRetentionPolicyTypeDef",
    {
        "Type": Literal["DAYS"],
        "Value": str,
    },
    total=False,
)

_RequiredBackupTypeDef = TypedDict(
    "_RequiredBackupTypeDef",
    {
        "BackupId": str,
    },
)
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "BackupState": BackupStateType,
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
        "NeverExpires": bool,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
        "DeleteTimestamp": datetime,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

class BackupTypeDef(_RequiredBackupTypeDef, _OptionalBackupTypeDef):
    pass

CertificatesTypeDef = TypedDict(
    "CertificatesTypeDef",
    {
        "ClusterCsr": str,
        "HsmCertificate": str,
        "AwsHardwareCertificate": str,
        "ManufacturerHardwareCertificate": str,
        "ClusterCertificate": str,
    },
    total=False,
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "BackupPolicy": Literal["DEFAULT"],
        "BackupRetentionPolicy": "BackupRetentionPolicyTypeDef",
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List["HsmTypeDef"],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": ClusterStateType,
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": "CertificatesTypeDef",
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

_RequiredCopyBackupToRegionRequestRequestTypeDef = TypedDict(
    "_RequiredCopyBackupToRegionRequestRequestTypeDef",
    {
        "DestinationRegion": str,
        "BackupId": str,
    },
)
_OptionalCopyBackupToRegionRequestRequestTypeDef = TypedDict(
    "_OptionalCopyBackupToRegionRequestRequestTypeDef",
    {
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

class CopyBackupToRegionRequestRequestTypeDef(
    _RequiredCopyBackupToRegionRequestRequestTypeDef,
    _OptionalCopyBackupToRegionRequestRequestTypeDef,
):
    pass

CopyBackupToRegionResponseTypeDef = TypedDict(
    "CopyBackupToRegionResponseTypeDef",
    {
        "DestinationBackup": "DestinationBackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClusterRequestRequestTypeDef",
    {
        "HsmType": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateClusterRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClusterRequestRequestTypeDef",
    {
        "BackupRetentionPolicy": "BackupRetentionPolicyTypeDef",
        "SourceBackupId": str,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

class CreateClusterRequestRequestTypeDef(
    _RequiredCreateClusterRequestRequestTypeDef, _OptionalCreateClusterRequestRequestTypeDef
):
    pass

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHsmRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHsmRequestRequestTypeDef",
    {
        "ClusterId": str,
        "AvailabilityZone": str,
    },
)
_OptionalCreateHsmRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHsmRequestRequestTypeDef",
    {
        "IpAddress": str,
    },
    total=False,
)

class CreateHsmRequestRequestTypeDef(
    _RequiredCreateHsmRequestRequestTypeDef, _OptionalCreateHsmRequestRequestTypeDef
):
    pass

CreateHsmResponseTypeDef = TypedDict(
    "CreateHsmResponseTypeDef",
    {
        "Hsm": "HsmTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBackupRequestRequestTypeDef = TypedDict(
    "DeleteBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)

DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterRequestRequestTypeDef = TypedDict(
    "DeleteClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteHsmRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteHsmRequestRequestTypeDef",
    {
        "ClusterId": str,
    },
)
_OptionalDeleteHsmRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteHsmRequestRequestTypeDef",
    {
        "HsmId": str,
        "EniId": str,
        "EniIp": str,
    },
    total=False,
)

class DeleteHsmRequestRequestTypeDef(
    _RequiredDeleteHsmRequestRequestTypeDef, _OptionalDeleteHsmRequestRequestTypeDef
):
    pass

DeleteHsmResponseTypeDef = TypedDict(
    "DeleteHsmResponseTypeDef",
    {
        "HsmId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBackupsRequestRequestTypeDef = TypedDict(
    "DescribeBackupsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": Dict[str, List[str]],
        "SortAscending": bool,
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

DescribeClustersRequestRequestTypeDef = TypedDict(
    "DescribeClustersRequestRequestTypeDef",
    {
        "Filters": Dict[str, List[str]],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {
        "Clusters": List["ClusterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationBackupTypeDef = TypedDict(
    "DestinationBackupTypeDef",
    {
        "CreateTimestamp": datetime,
        "SourceRegion": str,
        "SourceBackup": str,
        "SourceCluster": str,
    },
    total=False,
)

_RequiredHsmTypeDef = TypedDict(
    "_RequiredHsmTypeDef",
    {
        "HsmId": str,
    },
)
_OptionalHsmTypeDef = TypedDict(
    "_OptionalHsmTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "State": HsmStateType,
        "StateMessage": str,
    },
    total=False,
)

class HsmTypeDef(_RequiredHsmTypeDef, _OptionalHsmTypeDef):
    pass

InitializeClusterRequestRequestTypeDef = TypedDict(
    "InitializeClusterRequestRequestTypeDef",
    {
        "ClusterId": str,
        "SignedCert": str,
        "TrustAnchor": str,
    },
)

InitializeClusterResponseTypeDef = TypedDict(
    "InitializeClusterResponseTypeDef",
    {
        "State": ClusterStateType,
        "StateMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalListTagsRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListTagsRequestRequestTypeDef(
    _RequiredListTagsRequestRequestTypeDef, _OptionalListTagsRequestRequestTypeDef
):
    pass

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyBackupAttributesRequestRequestTypeDef = TypedDict(
    "ModifyBackupAttributesRequestRequestTypeDef",
    {
        "BackupId": str,
        "NeverExpires": bool,
    },
)

ModifyBackupAttributesResponseTypeDef = TypedDict(
    "ModifyBackupAttributesResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyClusterRequestRequestTypeDef = TypedDict(
    "ModifyClusterRequestRequestTypeDef",
    {
        "BackupRetentionPolicy": "BackupRetentionPolicyTypeDef",
        "ClusterId": str,
    },
)

ModifyClusterResponseTypeDef = TypedDict(
    "ModifyClusterResponseTypeDef",
    {
        "Cluster": "ClusterTypeDef",
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

RestoreBackupRequestRequestTypeDef = TypedDict(
    "RestoreBackupRequestRequestTypeDef",
    {
        "BackupId": str,
    },
)

RestoreBackupResponseTypeDef = TypedDict(
    "RestoreBackupResponseTypeDef",
    {
        "Backup": "BackupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagList": List["TagTypeDef"],
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
        "ResourceId": str,
        "TagKeyList": List[str],
    },
)
