"""
Type annotations for docdb-elastic service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/type_defs.html)

Usage::

    ```python
    from mypy_boto3_docdb_elastic.type_defs import ClusterInListTypeDef

    data: ClusterInListTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import AuthType, StatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ClusterInListTypeDef",
    "ClusterSnapshotInListTypeDef",
    "ClusterSnapshotTypeDef",
    "ClusterTypeDef",
    "CreateClusterInputRequestTypeDef",
    "CreateClusterOutputTypeDef",
    "CreateClusterSnapshotInputRequestTypeDef",
    "CreateClusterSnapshotOutputTypeDef",
    "DeleteClusterInputRequestTypeDef",
    "DeleteClusterOutputTypeDef",
    "DeleteClusterSnapshotInputRequestTypeDef",
    "DeleteClusterSnapshotOutputTypeDef",
    "GetClusterInputRequestTypeDef",
    "GetClusterOutputTypeDef",
    "GetClusterSnapshotInputRequestTypeDef",
    "GetClusterSnapshotOutputTypeDef",
    "ListClusterSnapshotsInputRequestTypeDef",
    "ListClusterSnapshotsOutputTypeDef",
    "ListClustersInputRequestTypeDef",
    "ListClustersOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreClusterFromSnapshotInputRequestTypeDef",
    "RestoreClusterFromSnapshotOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateClusterInputRequestTypeDef",
    "UpdateClusterOutputTypeDef",
)

ClusterInListTypeDef = TypedDict(
    "ClusterInListTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "status": StatusType,
    },
)

ClusterSnapshotInListTypeDef = TypedDict(
    "ClusterSnapshotInListTypeDef",
    {
        "clusterArn": str,
        "snapshotArn": str,
        "snapshotCreationTime": str,
        "snapshotName": str,
        "status": StatusType,
    },
)

ClusterSnapshotTypeDef = TypedDict(
    "ClusterSnapshotTypeDef",
    {
        "adminUserName": str,
        "clusterArn": str,
        "clusterCreationTime": str,
        "kmsKeyId": str,
        "snapshotArn": str,
        "snapshotCreationTime": str,
        "snapshotName": str,
        "status": StatusType,
        "subnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
    },
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "adminUserName": str,
        "authType": AuthType,
        "clusterArn": str,
        "clusterEndpoint": str,
        "clusterName": str,
        "createTime": str,
        "kmsKeyId": str,
        "preferredMaintenanceWindow": str,
        "shardCapacity": int,
        "shardCount": int,
        "status": StatusType,
        "subnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
    },
)

_RequiredCreateClusterInputRequestTypeDef = TypedDict(
    "_RequiredCreateClusterInputRequestTypeDef",
    {
        "adminUserName": str,
        "adminUserPassword": str,
        "authType": AuthType,
        "clusterName": str,
        "shardCapacity": int,
        "shardCount": int,
    },
)
_OptionalCreateClusterInputRequestTypeDef = TypedDict(
    "_OptionalCreateClusterInputRequestTypeDef",
    {
        "clientToken": str,
        "kmsKeyId": str,
        "preferredMaintenanceWindow": str,
        "subnetIds": List[str],
        "tags": Dict[str, str],
        "vpcSecurityGroupIds": List[str],
    },
    total=False,
)

class CreateClusterInputRequestTypeDef(
    _RequiredCreateClusterInputRequestTypeDef, _OptionalCreateClusterInputRequestTypeDef
):
    pass

CreateClusterOutputTypeDef = TypedDict(
    "CreateClusterOutputTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClusterSnapshotInputRequestTypeDef = TypedDict(
    "_RequiredCreateClusterSnapshotInputRequestTypeDef",
    {
        "clusterArn": str,
        "snapshotName": str,
    },
)
_OptionalCreateClusterSnapshotInputRequestTypeDef = TypedDict(
    "_OptionalCreateClusterSnapshotInputRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateClusterSnapshotInputRequestTypeDef(
    _RequiredCreateClusterSnapshotInputRequestTypeDef,
    _OptionalCreateClusterSnapshotInputRequestTypeDef,
):
    pass

CreateClusterSnapshotOutputTypeDef = TypedDict(
    "CreateClusterSnapshotOutputTypeDef",
    {
        "snapshot": "ClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterInputRequestTypeDef = TypedDict(
    "DeleteClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)

DeleteClusterOutputTypeDef = TypedDict(
    "DeleteClusterOutputTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClusterSnapshotInputRequestTypeDef = TypedDict(
    "DeleteClusterSnapshotInputRequestTypeDef",
    {
        "snapshotArn": str,
    },
)

DeleteClusterSnapshotOutputTypeDef = TypedDict(
    "DeleteClusterSnapshotOutputTypeDef",
    {
        "snapshot": "ClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClusterInputRequestTypeDef = TypedDict(
    "GetClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)

GetClusterOutputTypeDef = TypedDict(
    "GetClusterOutputTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClusterSnapshotInputRequestTypeDef = TypedDict(
    "GetClusterSnapshotInputRequestTypeDef",
    {
        "snapshotArn": str,
    },
)

GetClusterSnapshotOutputTypeDef = TypedDict(
    "GetClusterSnapshotOutputTypeDef",
    {
        "snapshot": "ClusterSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClusterSnapshotsInputRequestTypeDef = TypedDict(
    "ListClusterSnapshotsInputRequestTypeDef",
    {
        "clusterArn": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListClusterSnapshotsOutputTypeDef = TypedDict(
    "ListClusterSnapshotsOutputTypeDef",
    {
        "nextToken": str,
        "snapshots": List["ClusterSnapshotInListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListClustersInputRequestTypeDef = TypedDict(
    "ListClustersInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListClustersOutputTypeDef = TypedDict(
    "ListClustersOutputTypeDef",
    {
        "clusters": List["ClusterInListTypeDef"],
        "nextToken": str,
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

_RequiredRestoreClusterFromSnapshotInputRequestTypeDef = TypedDict(
    "_RequiredRestoreClusterFromSnapshotInputRequestTypeDef",
    {
        "clusterName": str,
        "snapshotArn": str,
    },
)
_OptionalRestoreClusterFromSnapshotInputRequestTypeDef = TypedDict(
    "_OptionalRestoreClusterFromSnapshotInputRequestTypeDef",
    {
        "kmsKeyId": str,
        "subnetIds": List[str],
        "tags": Dict[str, str],
        "vpcSecurityGroupIds": List[str],
    },
    total=False,
)

class RestoreClusterFromSnapshotInputRequestTypeDef(
    _RequiredRestoreClusterFromSnapshotInputRequestTypeDef,
    _OptionalRestoreClusterFromSnapshotInputRequestTypeDef,
):
    pass

RestoreClusterFromSnapshotOutputTypeDef = TypedDict(
    "RestoreClusterFromSnapshotOutputTypeDef",
    {
        "cluster": "ClusterTypeDef",
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

_RequiredUpdateClusterInputRequestTypeDef = TypedDict(
    "_RequiredUpdateClusterInputRequestTypeDef",
    {
        "clusterArn": str,
    },
)
_OptionalUpdateClusterInputRequestTypeDef = TypedDict(
    "_OptionalUpdateClusterInputRequestTypeDef",
    {
        "adminUserPassword": str,
        "authType": AuthType,
        "clientToken": str,
        "preferredMaintenanceWindow": str,
        "shardCapacity": int,
        "shardCount": int,
        "subnetIds": List[str],
        "vpcSecurityGroupIds": List[str],
    },
    total=False,
)

class UpdateClusterInputRequestTypeDef(
    _RequiredUpdateClusterInputRequestTypeDef, _OptionalUpdateClusterInputRequestTypeDef
):
    pass

UpdateClusterOutputTypeDef = TypedDict(
    "UpdateClusterOutputTypeDef",
    {
        "cluster": "ClusterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
