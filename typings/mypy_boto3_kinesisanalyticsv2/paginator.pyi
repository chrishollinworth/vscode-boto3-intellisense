"""
Type annotations for kinesisanalyticsv2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_kinesisanalyticsv2 import KinesisAnalyticsV2Client
    from mypy_boto3_kinesisanalyticsv2.paginator import (
        ListApplicationSnapshotsPaginator,
        ListApplicationsPaginator,
    )

    client: KinesisAnalyticsV2Client = boto3.client("kinesisanalyticsv2")

    list_application_snapshots_paginator: ListApplicationSnapshotsPaginator = client.get_paginator("list_application_snapshots")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListApplicationSnapshotsResponseTypeDef,
    ListApplicationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListApplicationSnapshotsPaginator", "ListApplicationsPaginator")

class ListApplicationSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html#listapplicationsnapshotspaginator)
    """

    def paginate(
        self, *, ApplicationName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationSnapshotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplicationSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html#listapplicationsnapshotspaginator)
        """

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.45/reference/services/kinesisanalyticsv2.html#KinesisAnalyticsV2.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalyticsv2/paginators.html#listapplicationspaginator)
        """
