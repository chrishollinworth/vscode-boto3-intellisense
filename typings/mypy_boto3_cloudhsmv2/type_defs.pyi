"""
Main interface for cloudhsmv2 service type definitions.

Usage::

    ```python
    from mypy_boto3_cloudhsmv2.type_defs import BackupTypeDef

    data: BackupTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BackupTypeDef",
    "CertificatesTypeDef",
    "ClusterTypeDef",
    "DestinationBackupTypeDef",
    "HsmTypeDef",
    "TagTypeDef",
    "CopyBackupToRegionResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateHsmResponseTypeDef",
    "DeleteBackupResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteHsmResponseTypeDef",
    "DescribeBackupsResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "InitializeClusterResponseTypeDef",
    "ListTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RestoreBackupResponseTypeDef",
)

_RequiredBackupTypeDef = TypedDict("_RequiredBackupTypeDef", {"BackupId": str})
_OptionalBackupTypeDef = TypedDict(
    "_OptionalBackupTypeDef",
    {
        "BackupState": Literal["CREATE_IN_PROGRESS", "READY", "DELETED", "PENDING_DELETION"],
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "CopyTimestamp": datetime,
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
        "ClusterId": str,
        "CreateTimestamp": datetime,
        "Hsms": List["HsmTypeDef"],
        "HsmType": str,
        "PreCoPassword": str,
        "SecurityGroup": str,
        "SourceBackupId": str,
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
        "SubnetMapping": Dict[str, str],
        "VpcId": str,
        "Certificates": "CertificatesTypeDef",
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

DestinationBackupTypeDef = TypedDict(
    "DestinationBackupTypeDef",
    {"CreateTimestamp": datetime, "SourceRegion": str, "SourceBackup": str, "SourceCluster": str},
    total=False,
)

_RequiredHsmTypeDef = TypedDict("_RequiredHsmTypeDef", {"HsmId": str})
_OptionalHsmTypeDef = TypedDict(
    "_OptionalHsmTypeDef",
    {
        "AvailabilityZone": str,
        "ClusterId": str,
        "SubnetId": str,
        "EniId": str,
        "EniIp": str,
        "State": Literal[
            "CREATE_IN_PROGRESS", "ACTIVE", "DEGRADED", "DELETE_IN_PROGRESS", "DELETED"
        ],
        "StateMessage": str,
    },
    total=False,
)


class HsmTypeDef(_RequiredHsmTypeDef, _OptionalHsmTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CopyBackupToRegionResponseTypeDef = TypedDict(
    "CopyBackupToRegionResponseTypeDef",
    {"DestinationBackup": "DestinationBackupTypeDef"},
    total=False,
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

CreateHsmResponseTypeDef = TypedDict("CreateHsmResponseTypeDef", {"Hsm": "HsmTypeDef"}, total=False)

DeleteBackupResponseTypeDef = TypedDict(
    "DeleteBackupResponseTypeDef", {"Backup": "BackupTypeDef"}, total=False
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef", {"Cluster": "ClusterTypeDef"}, total=False
)

DeleteHsmResponseTypeDef = TypedDict("DeleteHsmResponseTypeDef", {"HsmId": str}, total=False)

DescribeBackupsResponseTypeDef = TypedDict(
    "DescribeBackupsResponseTypeDef",
    {"Backups": List["BackupTypeDef"], "NextToken": str},
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {"Clusters": List["ClusterTypeDef"], "NextToken": str},
    total=False,
)

InitializeClusterResponseTypeDef = TypedDict(
    "InitializeClusterResponseTypeDef",
    {
        "State": Literal[
            "CREATE_IN_PROGRESS",
            "UNINITIALIZED",
            "INITIALIZE_IN_PROGRESS",
            "INITIALIZED",
            "ACTIVE",
            "UPDATE_IN_PROGRESS",
            "DELETE_IN_PROGRESS",
            "DELETED",
            "DEGRADED",
        ],
        "StateMessage": str,
    },
    total=False,
)

_RequiredListTagsResponseTypeDef = TypedDict(
    "_RequiredListTagsResponseTypeDef", {"TagList": List["TagTypeDef"]}
)
_OptionalListTagsResponseTypeDef = TypedDict(
    "_OptionalListTagsResponseTypeDef", {"NextToken": str}, total=False
)


class ListTagsResponseTypeDef(_RequiredListTagsResponseTypeDef, _OptionalListTagsResponseTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RestoreBackupResponseTypeDef = TypedDict(
    "RestoreBackupResponseTypeDef", {"Backup": "BackupTypeDef"}, total=False
)
