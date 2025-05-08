"""
Type annotations for pcs service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pcs.client import ParallelComputingServiceClient

    session = Session()
    client: ParallelComputingServiceClient = session.client("pcs")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListClustersPaginator, ListComputeNodeGroupsPaginator, ListQueuesPaginator
from .type_defs import (
    CreateClusterRequestTypeDef,
    CreateClusterResponseTypeDef,
    CreateComputeNodeGroupRequestTypeDef,
    CreateComputeNodeGroupResponseTypeDef,
    CreateQueueRequestTypeDef,
    CreateQueueResponseTypeDef,
    DeleteClusterRequestTypeDef,
    DeleteComputeNodeGroupRequestTypeDef,
    DeleteQueueRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetClusterRequestTypeDef,
    GetClusterResponseTypeDef,
    GetComputeNodeGroupRequestTypeDef,
    GetComputeNodeGroupResponseTypeDef,
    GetQueueRequestTypeDef,
    GetQueueResponseTypeDef,
    ListClustersRequestTypeDef,
    ListClustersResponseTypeDef,
    ListComputeNodeGroupsRequestTypeDef,
    ListComputeNodeGroupsResponseTypeDef,
    ListQueuesRequestTypeDef,
    ListQueuesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    RegisterComputeNodeGroupInstanceRequestTypeDef,
    RegisterComputeNodeGroupInstanceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateComputeNodeGroupRequestTypeDef,
    UpdateComputeNodeGroupResponseTypeDef,
    UpdateQueueRequestTypeDef,
    UpdateQueueResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ParallelComputingServiceClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ParallelComputingServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs.html#ParallelComputingService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ParallelComputingServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs.html#ParallelComputingService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#generate_presigned_url)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterRequestTypeDef]
    ) -> CreateClusterResponseTypeDef:
        """
        Creates a cluster in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/create_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#create_cluster)
        """

    def create_compute_node_group(
        self, **kwargs: Unpack[CreateComputeNodeGroupRequestTypeDef]
    ) -> CreateComputeNodeGroupResponseTypeDef:
        """
        Creates a managed set of compute nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/create_compute_node_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#create_compute_node_group)
        """

    def create_queue(
        self, **kwargs: Unpack[CreateQueueRequestTypeDef]
    ) -> CreateQueueResponseTypeDef:
        """
        Creates a job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/create_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#create_queue)
        """

    def delete_cluster(self, **kwargs: Unpack[DeleteClusterRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a cluster and all its linked resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/delete_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#delete_cluster)
        """

    def delete_compute_node_group(
        self, **kwargs: Unpack[DeleteComputeNodeGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a compute node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/delete_compute_node_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#delete_compute_node_group)
        """

    def delete_queue(self, **kwargs: Unpack[DeleteQueueRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a job queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/delete_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#delete_queue)
        """

    def get_cluster(self, **kwargs: Unpack[GetClusterRequestTypeDef]) -> GetClusterResponseTypeDef:
        """
        Returns detailed information about a running cluster in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/get_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#get_cluster)
        """

    def get_compute_node_group(
        self, **kwargs: Unpack[GetComputeNodeGroupRequestTypeDef]
    ) -> GetComputeNodeGroupResponseTypeDef:
        """
        Returns detailed information about a compute node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/get_compute_node_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#get_compute_node_group)
        """

    def get_queue(self, **kwargs: Unpack[GetQueueRequestTypeDef]) -> GetQueueResponseTypeDef:
        """
        Returns detailed information about a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/get_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#get_queue)
        """

    def list_clusters(
        self, **kwargs: Unpack[ListClustersRequestTypeDef]
    ) -> ListClustersResponseTypeDef:
        """
        Returns a list of running clusters in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/list_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#list_clusters)
        """

    def list_compute_node_groups(
        self, **kwargs: Unpack[ListComputeNodeGroupsRequestTypeDef]
    ) -> ListComputeNodeGroupsResponseTypeDef:
        """
        Returns a list of all compute node groups associated with a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/list_compute_node_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#list_compute_node_groups)
        """

    def list_queues(self, **kwargs: Unpack[ListQueuesRequestTypeDef]) -> ListQueuesResponseTypeDef:
        """
        Returns a list of all queues associated with a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/list_queues.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#list_queues)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of all tags on an Amazon Web Services PCS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#list_tags_for_resource)
        """

    def register_compute_node_group_instance(
        self, **kwargs: Unpack[RegisterComputeNodeGroupInstanceRequestTypeDef]
    ) -> RegisterComputeNodeGroupInstanceResponseTypeDef:
        """
        This API action isn't intended for you to use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/register_compute_node_group_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#register_compute_node_group_instance)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or edits tags on an Amazon Web Services PCS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes tags from an Amazon Web Services PCS resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#untag_resource)
        """

    def update_compute_node_group(
        self, **kwargs: Unpack[UpdateComputeNodeGroupRequestTypeDef]
    ) -> UpdateComputeNodeGroupResponseTypeDef:
        """
        Updates a compute node group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/update_compute_node_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#update_compute_node_group)
        """

    def update_queue(
        self, **kwargs: Unpack[UpdateQueueRequestTypeDef]
    ) -> UpdateQueueResponseTypeDef:
        """
        Updates the compute node group configuration of a queue.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/update_queue.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#update_queue)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_clusters"]
    ) -> ListClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_compute_node_groups"]
    ) -> ListComputeNodeGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_queues"]
    ) -> ListQueuesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pcs/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pcs/client/#get_paginator)
        """
