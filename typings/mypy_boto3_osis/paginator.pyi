"""
Type annotations for osis service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_osis.client import OpenSearchIngestionClient
    from mypy_boto3_osis.paginator import (
        ListPipelineEndpointConnectionsPaginator,
        ListPipelineEndpointsPaginator,
    )

    session = Session()
    client: OpenSearchIngestionClient = session.client("osis")

    list_pipeline_endpoint_connections_paginator: ListPipelineEndpointConnectionsPaginator = client.get_paginator("list_pipeline_endpoint_connections")
    list_pipeline_endpoints_paginator: ListPipelineEndpointsPaginator = client.get_paginator("list_pipeline_endpoints")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListPipelineEndpointConnectionsRequestPaginateTypeDef,
    ListPipelineEndpointConnectionsResponseTypeDef,
    ListPipelineEndpointsRequestPaginateTypeDef,
    ListPipelineEndpointsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListPipelineEndpointConnectionsPaginator", "ListPipelineEndpointsPaginator")

if TYPE_CHECKING:
    _ListPipelineEndpointConnectionsPaginatorBase = Paginator[
        ListPipelineEndpointConnectionsResponseTypeDef
    ]
else:
    _ListPipelineEndpointConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPipelineEndpointConnectionsPaginator(_ListPipelineEndpointConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/paginator/ListPipelineEndpointConnections.html#OpenSearchIngestion.Paginator.ListPipelineEndpointConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/paginators/#listpipelineendpointconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPipelineEndpointConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPipelineEndpointConnectionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/paginator/ListPipelineEndpointConnections.html#OpenSearchIngestion.Paginator.ListPipelineEndpointConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/paginators/#listpipelineendpointconnectionspaginator)
        """

if TYPE_CHECKING:
    _ListPipelineEndpointsPaginatorBase = Paginator[ListPipelineEndpointsResponseTypeDef]
else:
    _ListPipelineEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPipelineEndpointsPaginator(_ListPipelineEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/paginator/ListPipelineEndpoints.html#OpenSearchIngestion.Paginator.ListPipelineEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/paginators/#listpipelineendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPipelineEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListPipelineEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/osis/paginator/ListPipelineEndpoints.html#OpenSearchIngestion.Paginator.ListPipelineEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/paginators/#listpipelineendpointspaginator)
        """
