"""
Type annotations for cloudcontrol service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudcontrol.client import CloudControlApiClient
    from mypy_boto3_cloudcontrol.paginator import (
        ListResourceRequestsPaginator,
        ListResourcesPaginator,
    )

    session = Session()
    client: CloudControlApiClient = session.client("cloudcontrol")

    list_resource_requests_paginator: ListResourceRequestsPaginator = client.get_paginator("list_resource_requests")
    list_resources_paginator: ListResourcesPaginator = client.get_paginator("list_resources")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListResourceRequestsInputPaginateTypeDef,
    ListResourceRequestsOutputTypeDef,
    ListResourcesInputPaginateTypeDef,
    ListResourcesOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListResourceRequestsPaginator", "ListResourcesPaginator")

if TYPE_CHECKING:
    _ListResourceRequestsPaginatorBase = Paginator[ListResourceRequestsOutputTypeDef]
else:
    _ListResourceRequestsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceRequestsPaginator(_ListResourceRequestsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/paginator/ListResourceRequests.html#CloudControlApi.Paginator.ListResourceRequests)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators/#listresourcerequestspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceRequestsInputPaginateTypeDef]
    ) -> PageIterator[ListResourceRequestsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/paginator/ListResourceRequests.html#CloudControlApi.Paginator.ListResourceRequests.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators/#listresourcerequestspaginator)
        """

if TYPE_CHECKING:
    _ListResourcesPaginatorBase = Paginator[ListResourcesOutputTypeDef]
else:
    _ListResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourcesPaginator(_ListResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/paginator/ListResources.html#CloudControlApi.Paginator.ListResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators/#listresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourcesInputPaginateTypeDef]
    ) -> PageIterator[ListResourcesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudcontrol/paginator/ListResources.html#CloudControlApi.Paginator.ListResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudcontrol/paginators/#listresourcespaginator)
        """
