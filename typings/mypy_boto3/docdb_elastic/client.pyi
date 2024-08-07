"""
Type annotations for docdb-elastic service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_docdb_elastic import DocDBElasticClient

    client: DocDBElasticClient = boto3.client("docdb-elastic")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import AuthType
from .paginator import ListClusterSnapshotsPaginator, ListClustersPaginator
from .type_defs import (
    CopyClusterSnapshotOutputTypeDef,
    CreateClusterOutputTypeDef,
    CreateClusterSnapshotOutputTypeDef,
    DeleteClusterOutputTypeDef,
    DeleteClusterSnapshotOutputTypeDef,
    GetClusterOutputTypeDef,
    GetClusterSnapshotOutputTypeDef,
    ListClusterSnapshotsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
    RestoreClusterFromSnapshotOutputTypeDef,
    StartClusterOutputTypeDef,
    StopClusterOutputTypeDef,
    UpdateClusterOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("DocDBElasticClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DocDBElasticClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DocDBElasticClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#close)
        """

    def copy_cluster_snapshot(
        self,
        *,
        snapshotArn: str,
        targetSnapshotName: str,
        copyTags: bool = None,
        kmsKeyId: str = None,
        tags: Dict[str, str] = None
    ) -> CopyClusterSnapshotOutputTypeDef:
        """
        Copies a snapshot of an elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.copy_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#copy_cluster_snapshot)
        """

    def create_cluster(
        self,
        *,
        adminUserName: str,
        adminUserPassword: str,
        authType: AuthType,
        clusterName: str,
        shardCapacity: int,
        shardCount: int,
        backupRetentionPeriod: int = None,
        clientToken: str = None,
        kmsKeyId: str = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        shardInstanceCount: int = None,
        subnetIds: List[str] = None,
        tags: Dict[str, str] = None,
        vpcSecurityGroupIds: List[str] = None
    ) -> CreateClusterOutputTypeDef:
        """
        Creates a new Amazon DocumentDB elastic cluster and returns its cluster
        structure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#create_cluster)
        """

    def create_cluster_snapshot(
        self, *, clusterArn: str, snapshotName: str, tags: Dict[str, str] = None
    ) -> CreateClusterSnapshotOutputTypeDef:
        """
        Creates a snapshot of an elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.create_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#create_cluster_snapshot)
        """

    def delete_cluster(self, *, clusterArn: str) -> DeleteClusterOutputTypeDef:
        """
        Delete an elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#delete_cluster)
        """

    def delete_cluster_snapshot(self, *, snapshotArn: str) -> DeleteClusterSnapshotOutputTypeDef:
        """
        Delete an elastic cluster snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.delete_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#delete_cluster_snapshot)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#generate_presigned_url)
        """

    def get_cluster(self, *, clusterArn: str) -> GetClusterOutputTypeDef:
        """
        Returns information about a specific elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.get_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#get_cluster)
        """

    def get_cluster_snapshot(self, *, snapshotArn: str) -> GetClusterSnapshotOutputTypeDef:
        """
        Returns information about a specific elastic cluster snapshot See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-
        elastic-2022-11-28/GetClusterSnapshot>`_ **Request Syntax** response =
        client.get_cluster_snapshot( snapshotArn='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.get_cluster_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#get_cluster_snapshot)
        """

    def list_cluster_snapshots(
        self,
        *,
        clusterArn: str = None,
        maxResults: int = None,
        nextToken: str = None,
        snapshotType: str = None
    ) -> ListClusterSnapshotsOutputTypeDef:
        """
        Returns information about snapshots for a specified elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.list_cluster_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#list_cluster_snapshots)
        """

    def list_clusters(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListClustersOutputTypeDef:
        """
        Returns information about provisioned Amazon DocumentDB elastic clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#list_clusters)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags on a elastic cluster resource See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/docdb-
        elastic-2022-11-28/ListTagsForResource>`_ **Request Syntax** response =
        client.list_tags_for_resource( resourceArn='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#list_tags_for_resource)
        """

    def restore_cluster_from_snapshot(
        self,
        *,
        clusterName: str,
        snapshotArn: str,
        kmsKeyId: str = None,
        shardCapacity: int = None,
        shardInstanceCount: int = None,
        subnetIds: List[str] = None,
        tags: Dict[str, str] = None,
        vpcSecurityGroupIds: List[str] = None
    ) -> RestoreClusterFromSnapshotOutputTypeDef:
        """
        Restores an elastic cluster from a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.restore_cluster_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#restore_cluster_from_snapshot)
        """

    def start_cluster(self, *, clusterArn: str) -> StartClusterOutputTypeDef:
        """
        Restarts the stopped elastic cluster that is specified by `clusterARN`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.start_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#start_cluster)
        """

    def stop_cluster(self, *, clusterArn: str) -> StopClusterOutputTypeDef:
        """
        Stops the running elastic cluster that is specified by `clusterArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.stop_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#stop_cluster)
        """

    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds metadata tags to an elastic cluster resource See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-
        elastic-2022-11-28/TagResource>`_ **Request Syntax** response =
        client.tag_resource( resourceArn='string', tags={ 'string': 'string' ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#tag_resource)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes metadata tags from an elastic cluster resource See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/docdb-
        elastic-2022-11-28/UntagResource>`_ **Request Syntax** response =
        client.untag_resource( resourceArn='string', tagKeys=[ 'string'...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#untag_resource)
        """

    def update_cluster(
        self,
        *,
        clusterArn: str,
        adminUserPassword: str = None,
        authType: AuthType = None,
        backupRetentionPeriod: int = None,
        clientToken: str = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        shardCapacity: int = None,
        shardCount: int = None,
        shardInstanceCount: int = None,
        subnetIds: List[str] = None,
        vpcSecurityGroupIds: List[str] = None
    ) -> UpdateClusterOutputTypeDef:
        """
        Modifies an elastic cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Client.update_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/client.html#update_cluster)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_cluster_snapshots"]
    ) -> ListClusterSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusterSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators.html#listclustersnapshotspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/docdb-elastic.html#DocDBElastic.Paginator.ListClusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb_elastic/paginators.html#listclusterspaginator)
        """
