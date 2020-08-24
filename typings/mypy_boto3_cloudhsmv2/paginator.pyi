# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for cloudhsmv2 service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudhsmv2 import CloudHSMV2Client
    from mypy_boto3_cloudhsmv2.paginator import (
        DescribeBackupsPaginator,
        DescribeClustersPaginator,
        ListTagsPaginator,
    )

    client: CloudHSMV2Client = boto3.client("cloudhsmv2")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""
from typing import Dict, Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_cloudhsmv2.type_defs import (
    DescribeBackupsResponseTypeDef,
    DescribeClustersResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeBackupsPaginator", "DescribeClustersPaginator", "ListTagsPaginator")


class DescribeBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups)
    """

    def paginate(
        self,
        Filters: Dict[str, List[str]] = None,
        SortAscending: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeBackupsResponseTypeDef]:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeBackups.paginate)
        """


class DescribeClustersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters)
    """

    def paginate(
        self, Filters: Dict[str, List[str]] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClustersResponseTypeDef]:
        """
        [DescribeClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.DescribeClusters.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags)
    """

    def paginate(
        self, ResourceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/cloudhsmv2.html#CloudHSMV2.Paginator.ListTags.paginate)
        """
