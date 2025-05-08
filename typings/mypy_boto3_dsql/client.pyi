"""
Type annotations for dsql service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_dsql.client import AuroraDSQLClient

    session = Session()
    client: AuroraDSQLClient = session.client("dsql")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListClustersPaginator
from .type_defs import (
    CreateClusterInputTypeDef,
    CreateClusterOutputTypeDef,
    CreateMultiRegionClustersInputTypeDef,
    CreateMultiRegionClustersOutputTypeDef,
    DeleteClusterInputTypeDef,
    DeleteClusterOutputTypeDef,
    DeleteMultiRegionClustersInputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetClusterInputTypeDef,
    GetClusterOutputTypeDef,
    GetVpcEndpointServiceNameInputTypeDef,
    GetVpcEndpointServiceNameOutputTypeDef,
    ListClustersInputTypeDef,
    ListClustersOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateClusterInputTypeDef,
    UpdateClusterOutputTypeDef,
)
from .waiter import ClusterActiveWaiter, ClusterNotExistsWaiter

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("AuroraDSQLClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AuroraDSQLClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql.html#AuroraDSQL.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AuroraDSQLClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql.html#AuroraDSQL.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#generate_presigned_url)
        """

    def create_cluster(
        self, **kwargs: Unpack[CreateClusterInputTypeDef]
    ) -> CreateClusterOutputTypeDef:
        """
        Creates a cluster in Amazon Aurora DSQL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/create_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#create_cluster)
        """

    def create_multi_region_clusters(
        self, **kwargs: Unpack[CreateMultiRegionClustersInputTypeDef]
    ) -> CreateMultiRegionClustersOutputTypeDef:
        """
        Creates multi-Region clusters in Amazon Aurora DSQL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/create_multi_region_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#create_multi_region_clusters)
        """

    def delete_cluster(
        self, **kwargs: Unpack[DeleteClusterInputTypeDef]
    ) -> DeleteClusterOutputTypeDef:
        """
        Deletes a cluster in Amazon Aurora DSQL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/delete_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#delete_cluster)
        """

    def delete_multi_region_clusters(
        self, **kwargs: Unpack[DeleteMultiRegionClustersInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a multi-Region cluster in Amazon Aurora DSQL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/delete_multi_region_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#delete_multi_region_clusters)
        """

    def get_cluster(self, **kwargs: Unpack[GetClusterInputTypeDef]) -> GetClusterOutputTypeDef:
        """
        Retrieves information about a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/get_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#get_cluster)
        """

    def get_vpc_endpoint_service_name(
        self, **kwargs: Unpack[GetVpcEndpointServiceNameInputTypeDef]
    ) -> GetVpcEndpointServiceNameOutputTypeDef:
        """
        Retrieves the VPC endpoint service name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/get_vpc_endpoint_service_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#get_vpc_endpoint_service_name)
        """

    def list_clusters(
        self, **kwargs: Unpack[ListClustersInputTypeDef]
    ) -> ListClustersOutputTypeDef:
        """
        Retrieves information about a list of clusters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/list_clusters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#list_clusters)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists all of the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#list_tags_for_resource)
        """

    def tag_resource(
        self, **kwargs: Unpack[TagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Tags a resource with a map of key and value pairs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#tag_resource)
        """

    def untag_resource(
        self, **kwargs: Unpack[UntagResourceInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes a tag from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#untag_resource)
        """

    def update_cluster(
        self, **kwargs: Unpack[UpdateClusterInputTypeDef]
    ) -> UpdateClusterOutputTypeDef:
        """
        Updates a cluster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/update_cluster.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#update_cluster)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_clusters"]
    ) -> ListClustersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cluster_active"]
    ) -> ClusterActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["cluster_not_exists"]
    ) -> ClusterNotExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dsql/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dsql/client/#get_waiter)
        """
