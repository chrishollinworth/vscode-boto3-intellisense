"""
Type annotations for kinesisanalyticsv2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_kinesisanalyticsv2.client import KinesisAnalyticsV2Client
    from mypy_boto3_kinesisanalyticsv2.paginator import (
        ListApplicationOperationsPaginator,
        ListApplicationSnapshotsPaginator,
        ListApplicationVersionsPaginator,
        ListApplicationsPaginator,
    )

    session = Session()
    client: KinesisAnalyticsV2Client = session.client("kinesisanalyticsv2")

    list_application_operations_paginator: ListApplicationOperationsPaginator = client.get_paginator("list_application_operations")
    list_application_snapshots_paginator: ListApplicationSnapshotsPaginator = client.get_paginator("list_application_snapshots")
    list_application_versions_paginator: ListApplicationVersionsPaginator = client.get_paginator("list_application_versions")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationOperationsRequestPaginateTypeDef,
    ListApplicationOperationsResponseTypeDef,
    ListApplicationSnapshotsRequestPaginateTypeDef,
    ListApplicationSnapshotsResponseTypeDef,
    ListApplicationsRequestPaginateTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsRequestPaginateTypeDef,
    ListApplicationVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationOperationsPaginator",
    "ListApplicationSnapshotsPaginator",
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
)

if TYPE_CHECKING:
    _ListApplicationOperationsPaginatorBase = Paginator[ListApplicationOperationsResponseTypeDef]
else:
    _ListApplicationOperationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationOperationsPaginator(_ListApplicationOperationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/paginator/ListApplicationOperations.html#KinesisAnalyticsV2.Paginator.ListApplicationOperations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/#listapplicationoperationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationOperationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationOperationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/paginator/ListApplicationOperations.html#KinesisAnalyticsV2.Paginator.ListApplicationOperations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/#listapplicationoperationspaginator)
        """

if TYPE_CHECKING:
    _ListApplicationSnapshotsPaginatorBase = Paginator[ListApplicationSnapshotsResponseTypeDef]
else:
    _ListApplicationSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationSnapshotsPaginator(_ListApplicationSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/paginator/ListApplicationSnapshots.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/#listapplicationsnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/paginator/ListApplicationSnapshots.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/#listapplicationsnapshotspaginator)
        """

if TYPE_CHECKING:
    _ListApplicationVersionsPaginatorBase = Paginator[ListApplicationVersionsResponseTypeDef]
else:
    _ListApplicationVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationVersionsPaginator(_ListApplicationVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/paginator/ListApplicationVersions.html#KinesisAnalyticsV2.Paginator.ListApplicationVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/#listapplicationversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/paginator/ListApplicationVersions.html#KinesisAnalyticsV2.Paginator.ListApplicationVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/#listapplicationversionspaginator)
        """

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/paginator/ListApplications.html#KinesisAnalyticsV2.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kinesisanalyticsv2/paginator/ListApplications.html#KinesisAnalyticsV2.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators/#listapplicationspaginator)
        """
