"""
Type annotations for memorydb service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_memorydb.client import MemoryDBClient

    session = Session()
    client: MemoryDBClient = session.client("memorydb")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeACLsPaginator,
    DescribeClustersPaginator,
    DescribeEngineVersionsPaginator,
    DescribeEventsPaginator,
    DescribeMultiRegionClustersPaginator,
    DescribeParameterGroupsPaginator,
    DescribeParametersPaginator,
    DescribeReservedNodesOfferingsPaginator,
    DescribeReservedNodesPaginator,
    DescribeServiceUpdatesPaginator,
    DescribeSnapshotsPaginator,
    DescribeSubnetGroupsPaginator,
    DescribeUsersPaginator,
)
from .type_defs import (
    BatchUpdateClusterRequestTypeDef,
    BatchUpdateClusterResponseTypeDef,
    CopySnapshotRequestTypeDef,
    CopySnapshotResponseTypeDef,
    CreateACLRequestTypeDef,
    CreateACLResponseTypeDef,
    CreateClusterRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateMultiRegionClusterRequestTypeDef,
    CreateMultiRegionClusterResponseTypeDef,
    CreateParameterGroupRequestTypeDef,
    CreateParameterGroupResponseTypeDef,
    CreateSnapshotRequestTypeDef,
    CreateSnapshotResponseTypeDef,
    CreateSubnetGroupRequestTypeDef,
    CreateSubnetGroupResponseTypeDef,
    CreateUserRequestTypeDef,
    CreateUserResponseTypeDef,
    DeleteACLRequestTypeDef,
    DeleteACLResponseTypeDef,
    DeleteClusterRequestTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteMultiRegionClusterRequestTypeDef,
    DeleteMultiRegionClusterResponseTypeDef,
    DeleteParameterGroupRequestTypeDef,
    DeleteParameterGroupResponseTypeDef,
    DeleteSnapshotRequestTypeDef,
    DeleteSnapshotResponseTypeDef,
    DeleteSubnetGroupRequestTypeDef,
    DeleteSubnetGroupResponseTypeDef,
    DeleteUserRequestTypeDef,
    DeleteUserResponseTypeDef,
    DescribeACLsRequestTypeDef,
    DescribeACLsResponseTypeDef,
    DescribeClustersRequestTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeEngineVersionsRequestTypeDef,
    DescribeEngineVersionsResponseTypeDef,
    DescribeEventsRequestTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeMultiRegionClustersRequestTypeDef,
    DescribeMultiRegionClustersResponseTypeDef,
    DescribeParameterGroupsRequestTypeDef,
    DescribeParameterGroupsResponseTypeDef,
    DescribeParametersRequestTypeDef,
    DescribeParametersResponseTypeDef,
    DescribeReservedNodesOfferingsRequestTypeDef,
    DescribeReservedNodesOfferingsResponseTypeDef,
    DescribeReservedNodesRequestTypeDef,
    DescribeReservedNodesResponseTypeDef,
    DescribeServiceUpdatesRequestTypeDef,
    DescribeServiceUpdatesResponseTypeDef,
    DescribeSnapshotsRequestTypeDef,
    DescribeSnapshotsResponseTypeDef,
    DescribeSubnetGroupsRequestTypeDef,
    DescribeSubnetGroupsResponseTypeDef,
    DescribeUsersRequestTypeDef,
    DescribeUsersResponseTypeDef,
    FailoverShardRequestTypeDef,
    FailoverShardResponseTypeDef,
    ListAllowedMultiRegionClusterUpdatesRequestTypeDef,
    ListAllowedMultiRegionClusterUpdatesResponseTypeDef,
    ListAllowedNodeTypeUpdatesRequestTypeDef,
    ListAllowedNodeTypeUpdatesResponseTypeDef,
    ListTagsRequestTypeDef,
    ListTagsResponseTypeDef,
    PurchaseReservedNodesOfferingRequestTypeDef,
    PurchaseReservedNodesOfferingResponseTypeDef,
    ResetParameterGroupRequestTypeDef,
    ResetParameterGroupResponseTypeDef,
    TagResourceRequestTypeDef,
    TagResourceResponseTypeDef,
    UntagResourceRequestTypeDef,
    UntagResourceResponseTypeDef,
    UpdateACLRequestTypeDef,
    UpdateACLResponseTypeDef,
    UpdateClusterRequestTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateMultiRegionClusterRequestTypeDef,
    UpdateMultiRegionClusterResponseTypeDef,
    UpdateParameterGroupRequestTypeDef,
    UpdateParameterGroupResponseTypeDef,
    UpdateSubnetGroupRequestTypeDef,
    UpdateSubnetGroupResponseTypeDef,
    UpdateUserRequestTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MemoryDBClient",)

class Exceptions(BaseClientExceptions):
    ACLAlreadyExistsFault: Type[BotocoreClientError]
    ACLNotFoundFault: Type[BotocoreClientError]
    ACLQuotaExceededFault: Type[BotocoreClientError]
    APICallRateForCustomerExceededFault: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClusterAlreadyExistsFault: Type[BotocoreClientError]
    ClusterNotFoundFault: Type[BotocoreClientError]
    ClusterQuotaForCustomerExceededFault: Type[BotocoreClientError]
    DefaultUserRequired: Type[BotocoreClientError]
    DuplicateUserNameFault: Type[BotocoreClientError]
    InsufficientClusterCapacityFault: Type[BotocoreClientError]
    InvalidACLStateFault: Type[BotocoreClientError]
    InvalidARNFault: Type[BotocoreClientError]
    InvalidClusterStateFault: Type[BotocoreClientError]
    InvalidCredentialsException: Type[BotocoreClientError]
    InvalidKMSKeyFault: Type[BotocoreClientError]
    InvalidMultiRegionClusterStateFault: Type[BotocoreClientError]
    InvalidNodeStateFault: Type[BotocoreClientError]
    InvalidParameterCombinationException: Type[BotocoreClientError]
    InvalidParameterGroupStateFault: Type[BotocoreClientError]
    InvalidParameterValueException: Type[BotocoreClientError]
    InvalidSnapshotStateFault: Type[BotocoreClientError]
    InvalidSubnet: Type[BotocoreClientError]
    InvalidUserStateFault: Type[BotocoreClientError]
    InvalidVPCNetworkStateFault: Type[BotocoreClientError]
    MultiRegionClusterAlreadyExistsFault: Type[BotocoreClientError]
    MultiRegionClusterNotFoundFault: Type[BotocoreClientError]
    MultiRegionParameterGroupNotFoundFault: Type[BotocoreClientError]
    NoOperationFault: Type[BotocoreClientError]
    NodeQuotaForClusterExceededFault: Type[BotocoreClientError]
    NodeQuotaForCustomerExceededFault: Type[BotocoreClientError]
    ParameterGroupAlreadyExistsFault: Type[BotocoreClientError]
    ParameterGroupNotFoundFault: Type[BotocoreClientError]
    ParameterGroupQuotaExceededFault: Type[BotocoreClientError]
    ReservedNodeAlreadyExistsFault: Type[BotocoreClientError]
    ReservedNodeNotFoundFault: Type[BotocoreClientError]
    ReservedNodeQuotaExceededFault: Type[BotocoreClientError]
    ReservedNodesOfferingNotFoundFault: Type[BotocoreClientError]
    ServiceLinkedRoleNotFoundFault: Type[BotocoreClientError]
    ServiceUpdateNotFoundFault: Type[BotocoreClientError]
    ShardNotFoundFault: Type[BotocoreClientError]
    ShardsPerClusterQuotaExceededFault: Type[BotocoreClientError]
    SnapshotAlreadyExistsFault: Type[BotocoreClientError]
    SnapshotNotFoundFault: Type[BotocoreClientError]
    SnapshotQuotaExceededFault: Type[BotocoreClientError]
    SubnetGroupAlreadyExistsFault: Type[BotocoreClientError]
    SubnetGroupInUseFault: Type[BotocoreClientError]
    SubnetGroupNotFoundFault: Type[BotocoreClientError]
    SubnetGroupQuotaExceededFault: Type[BotocoreClientError]
    SubnetInUse: Type[BotocoreClientError]
    SubnetNotAllowedFault: Type[BotocoreClientError]
    SubnetQuotaExceededFault: Type[BotocoreClientError]
    TagNotFoundFault: Type[BotocoreClientError]
    TagQuotaPerResourceExceeded: Type[BotocoreClientError]
    TestFailoverNotAvailableFault: Type[BotocoreClientError]
    UserAlreadyExistsFault: Type[BotocoreClientError]
    UserNotFoundFault: Type[BotocoreClientError]
    UserQuotaExceededFault: Type[BotocoreClientError]

class MemoryDBClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MemoryDBClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb.html#MemoryDB.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#generate_presigned_url)
        """

    def batch_update_cluster(
        self, **kwargs: Unpack[BatchUpdateClusterRequestTypeDef]
    ) -> BatchUpdateClusterResponseTypeDef:
        """
        Apply the service update to a list of clusters supplied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/batch_update_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#batch_update_cluster)
        """

    def copy_snapshot(
        self, **kwargs: Unpack[CopySnapshotRequestTypeDef]
    ) -> CopySnapshotResponseTypeDef:
        """
        Makes a copy of an existing snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/copy_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#copy_snapshot)
        """

    def create_acl(self, **kwargs: Unpack[CreateACLRequestTypeDef]) -> CreateACLResponseTypeDef:
        """
        Creates an Access Control List.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/create_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_acl)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/create_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_cluster)
        """

    def create_multi_region_cluster(
        self, **kwargs: Unpack[CreateMultiRegionClusterRequestTypeDef]
    ) -> CreateMultiRegionClusterResponseTypeDef:
        """
        Creates a new multi-Region cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/create_multi_region_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_multi_region_cluster)
        """

    def create_parameter_group(
        self, **kwargs: Unpack[CreateParameterGroupRequestTypeDef]
    ) -> CreateParameterGroupResponseTypeDef:
        """
        Creates a new MemoryDB parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/create_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_parameter_group)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotRequestTypeDef]
    ) -> CreateSnapshotResponseTypeDef:
        """
        Creates a copy of an entire cluster at a specific moment in time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/create_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_snapshot)
        """

    def create_subnet_group(
        self, **kwargs: Unpack[CreateSubnetGroupRequestTypeDef]
    ) -> CreateSubnetGroupResponseTypeDef:
        """
        Creates a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/create_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_subnet_group)
        """

    def create_user(self, **kwargs: Unpack[CreateUserRequestTypeDef]) -> CreateUserResponseTypeDef:
        """
        Creates a MemoryDB user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/create_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#create_user)
        """

    def delete_acl(self, **kwargs: Unpack[DeleteACLRequestTypeDef]) -> DeleteACLResponseTypeDef:
        """
        Deletes an Access Control List.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/delete_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_acl)
        """

    def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterRequestTypeDef]
    ) -> DeleteClusterResponseTypeDef:
        """
        Deletes a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/delete_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_cluster)
        """

    def delete_multi_region_cluster(
        self, **kwargs: Unpack[DeleteMultiRegionClusterRequestTypeDef]
    ) -> DeleteMultiRegionClusterResponseTypeDef:
        """
        Deletes an existing multi-Region cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/delete_multi_region_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_multi_region_cluster)
        """

    def delete_parameter_group(
        self, **kwargs: Unpack[DeleteParameterGroupRequestTypeDef]
    ) -> DeleteParameterGroupResponseTypeDef:
        """
        Deletes the specified parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/delete_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_parameter_group)
        """

    def delete_snapshot(
        self, **kwargs: Unpack[DeleteSnapshotRequestTypeDef]
    ) -> DeleteSnapshotResponseTypeDef:
        """
        Deletes an existing snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/delete_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_snapshot)
        """

    def delete_subnet_group(
        self, **kwargs: Unpack[DeleteSubnetGroupRequestTypeDef]
    ) -> DeleteSubnetGroupResponseTypeDef:
        """
        Deletes a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/delete_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_subnet_group)
        """

    def delete_user(self, **kwargs: Unpack[DeleteUserRequestTypeDef]) -> DeleteUserResponseTypeDef:
        """
        Deletes a user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/delete_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#delete_user)
        """

    def describe_acls(
        self, **kwargs: Unpack[DescribeACLsRequestTypeDef]
    ) -> DescribeACLsResponseTypeDef:
        """
        Returns a list of ACLs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_acls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_acls)
        """

    def describe_clusters(
        self, **kwargs: Unpack[DescribeClustersRequestTypeDef]
    ) -> DescribeClustersResponseTypeDef:
        """
        Returns information about all provisioned clusters if no cluster identifier is
        specified, or about a specific cluster if a cluster name is supplied.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_clusters)
        """

    def describe_engine_versions(
        self, **kwargs: Unpack[DescribeEngineVersionsRequestTypeDef]
    ) -> DescribeEngineVersionsResponseTypeDef:
        """
        Returns a list of the available Redis OSS engine versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_engine_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_engine_versions)
        """

    def describe_events(
        self, **kwargs: Unpack[DescribeEventsRequestTypeDef]
    ) -> DescribeEventsResponseTypeDef:
        """
        Returns events related to clusters, security groups, and parameter groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_events)
        """

    def describe_multi_region_clusters(
        self, **kwargs: Unpack[DescribeMultiRegionClustersRequestTypeDef]
    ) -> DescribeMultiRegionClustersResponseTypeDef:
        """
        Returns details about one or more multi-Region clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_multi_region_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_multi_region_clusters)
        """

    def describe_parameter_groups(
        self, **kwargs: Unpack[DescribeParameterGroupsRequestTypeDef]
    ) -> DescribeParameterGroupsResponseTypeDef:
        """
        Returns a list of parameter group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_parameter_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_parameter_groups)
        """

    def describe_parameters(
        self, **kwargs: Unpack[DescribeParametersRequestTypeDef]
    ) -> DescribeParametersResponseTypeDef:
        """
        Returns the detailed parameter list for a particular parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_parameters)
        """

    def describe_reserved_nodes(
        self, **kwargs: Unpack[DescribeReservedNodesRequestTypeDef]
    ) -> DescribeReservedNodesResponseTypeDef:
        """
        Returns information about reserved nodes for this account, or about a specified
        reserved node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_reserved_nodes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_reserved_nodes)
        """

    def describe_reserved_nodes_offerings(
        self, **kwargs: Unpack[DescribeReservedNodesOfferingsRequestTypeDef]
    ) -> DescribeReservedNodesOfferingsResponseTypeDef:
        """
        Lists available reserved node offerings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_reserved_nodes_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_reserved_nodes_offerings)
        """

    def describe_service_updates(
        self, **kwargs: Unpack[DescribeServiceUpdatesRequestTypeDef]
    ) -> DescribeServiceUpdatesResponseTypeDef:
        """
        Returns details of the service updates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_service_updates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_service_updates)
        """

    def describe_snapshots(
        self, **kwargs: Unpack[DescribeSnapshotsRequestTypeDef]
    ) -> DescribeSnapshotsResponseTypeDef:
        """
        Returns information about cluster snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_snapshots)
        """

    def describe_subnet_groups(
        self, **kwargs: Unpack[DescribeSubnetGroupsRequestTypeDef]
    ) -> DescribeSubnetGroupsResponseTypeDef:
        """
        Returns a list of subnet group descriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_subnet_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_subnet_groups)
        """

    def describe_users(
        self, **kwargs: Unpack[DescribeUsersRequestTypeDef]
    ) -> DescribeUsersResponseTypeDef:
        """
        Returns a list of users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/describe_users.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#describe_users)
        """

    def failover_shard(
        self, **kwargs: Unpack[FailoverShardRequestTypeDef]
    ) -> FailoverShardResponseTypeDef:
        """
        Used to failover a shard.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/failover_shard.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#failover_shard)
        """

    def list_allowed_multi_region_cluster_updates(
        self, **kwargs: Unpack[ListAllowedMultiRegionClusterUpdatesRequestTypeDef]
    ) -> ListAllowedMultiRegionClusterUpdatesResponseTypeDef:
        """
        Lists the allowed updates for a multi-Region cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/list_allowed_multi_region_cluster_updates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#list_allowed_multi_region_cluster_updates)
        """

    def list_allowed_node_type_updates(
        self, **kwargs: Unpack[ListAllowedNodeTypeUpdatesRequestTypeDef]
    ) -> ListAllowedNodeTypeUpdatesResponseTypeDef:
        """
        Lists all available node types that you can scale to from your cluster's
        current node type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/list_allowed_node_type_updates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#list_allowed_node_type_updates)
        """

    def list_tags(self, **kwargs: Unpack[ListTagsRequestTypeDef]) -> ListTagsResponseTypeDef:
        """
        Lists all tags currently on a named resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/list_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#list_tags)
        """

    def purchase_reserved_nodes_offering(
        self, **kwargs: Unpack[PurchaseReservedNodesOfferingRequestTypeDef]
    ) -> PurchaseReservedNodesOfferingResponseTypeDef:
        """
        Allows you to purchase a reserved node offering.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/purchase_reserved_nodes_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#purchase_reserved_nodes_offering)
        """

    def reset_parameter_group(
        self, **kwargs: Unpack[ResetParameterGroupRequestTypeDef]
    ) -> ResetParameterGroupResponseTypeDef:
        """
        Modifies the parameters of a parameter group to the engine or system default
        value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/reset_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#reset_parameter_group)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> TagResourceResponseTypeDef:
        """
        Use this operation to add tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> UntagResourceResponseTypeDef:
        """
        Use this operation to remove tags on a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#untag_resource)
        """

    def update_acl(self, **kwargs: Unpack[UpdateACLRequestTypeDef]) -> UpdateACLResponseTypeDef:
        """
        Changes the list of users that belong to the Access Control List.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/update_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_acl)
        """

    def update_cluster(
        self, **kwargs: Unpack[UpdateClusterRequestTypeDef]
    ) -> UpdateClusterResponseTypeDef:
        """
        Modifies the settings for a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/update_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_cluster)
        """

    def update_multi_region_cluster(
        self, **kwargs: Unpack[UpdateMultiRegionClusterRequestTypeDef]
    ) -> UpdateMultiRegionClusterResponseTypeDef:
        """
        Updates the configuration of an existing multi-Region cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/update_multi_region_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_multi_region_cluster)
        """

    def update_parameter_group(
        self, **kwargs: Unpack[UpdateParameterGroupRequestTypeDef]
    ) -> UpdateParameterGroupResponseTypeDef:
        """
        Updates the parameters of a parameter group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/update_parameter_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_parameter_group)
        """

    def update_subnet_group(
        self, **kwargs: Unpack[UpdateSubnetGroupRequestTypeDef]
    ) -> UpdateSubnetGroupResponseTypeDef:
        """
        Updates a subnet group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/update_subnet_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_subnet_group)
        """

    def update_user(self, **kwargs: Unpack[UpdateUserRequestTypeDef]) -> UpdateUserResponseTypeDef:
        """
        Changes user password(s) and/or access string.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/update_user.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#update_user)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_acls"]
    ) -> DescribeACLsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_clusters"]
    ) -> DescribeClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_engine_versions"]
    ) -> DescribeEngineVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_events"]
    ) -> DescribeEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_multi_region_clusters"]
    ) -> DescribeMultiRegionClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_parameter_groups"]
    ) -> DescribeParameterGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_parameters"]
    ) -> DescribeParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_nodes_offerings"]
    ) -> DescribeReservedNodesOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_nodes"]
    ) -> DescribeReservedNodesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_service_updates"]
    ) -> DescribeServiceUpdatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_subnet_groups"]
    ) -> DescribeSubnetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_users"]
    ) -> DescribeUsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/memorydb/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_memorydb/client/#get_paginator)
        """
