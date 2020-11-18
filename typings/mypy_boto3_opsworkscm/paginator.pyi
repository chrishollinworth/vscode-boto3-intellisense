# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for opsworkscm service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_opsworkscm import OpsWorksCMClient
    from mypy_boto3_opsworkscm.paginator import (
        DescribeBackupsPaginator,
        DescribeEventsPaginator,
        DescribeServersPaginator,
        ListTagsForResourcePaginator,
    )

    client: OpsWorksCMClient = boto3.client("opsworkscm")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_servers_paginator: DescribeServersPaginator = client.get_paginator("describe_servers")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_opsworkscm.type_defs import (
    DescribeBackupsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeBackupsPaginator",
    "DescribeEventsPaginator",
    "DescribeServersPaginator",
    "ListTagsForResourcePaginator",
)


class DescribeBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)
    """

    def paginate(
        self,
        BackupId: str = None,
        ServerName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeBackupsResponseTypeDef]:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)
    """

    def paginate(
        self, ServerName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEventsResponseTypeDef]:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents.paginate)
        """


class DescribeServersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)
    """

    def paginate(
        self, ServerName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeServersResponseTypeDef]:
        """
        [DescribeServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.ListTagsForResource)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/opsworkscm.html#OpsWorksCM.Paginator.ListTagsForResource.paginate)
        """
