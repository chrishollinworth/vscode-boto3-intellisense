"""
Type annotations for cloudhsmv2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_cloudhsmv2.client import CloudHSMV2Client
    from mypy_boto3_cloudhsmv2.paginator import (
        DescribeBackupsPaginator,
        DescribeClustersPaginator,
        ListTagsPaginator,
    )

    session = Session()
    client: CloudHSMV2Client = session.client("cloudhsmv2")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeBackupsRequestPaginateTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeClustersRequestPaginateTypeDef,
    DescribeClustersResponseTypeDef,
    ListTagsRequestPaginateTypeDef,
    ListTagsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("DescribeBackupsPaginator", "DescribeClustersPaginator", "ListTagsPaginator")

if TYPE_CHECKING:
    _DescribeBackupsPaginatorBase = Paginator[DescribeBackupsResponseTypeDef]
else:
    _DescribeBackupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBackupsPaginator(_DescribeBackupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/paginator/DescribeBackups.html#CloudHSMV2.Paginator.DescribeBackups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators/#describebackupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBackupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBackupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/paginator/DescribeBackups.html#CloudHSMV2.Paginator.DescribeBackups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators/#describebackupspaginator)
        """

if TYPE_CHECKING:
    _DescribeClustersPaginatorBase = Paginator[DescribeClustersResponseTypeDef]
else:
    _DescribeClustersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClustersPaginator(_DescribeClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/paginator/DescribeClusters.html#CloudHSMV2.Paginator.DescribeClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators/#describeclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClustersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/paginator/DescribeClusters.html#CloudHSMV2.Paginator.DescribeClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators/#describeclusterspaginator)
        """

if TYPE_CHECKING:
    _ListTagsPaginatorBase = Paginator[ListTagsResponseTypeDef]
else:
    _ListTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsPaginator(_ListTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/paginator/ListTags.html#CloudHSMV2.Paginator.ListTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators/#listtagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudhsmv2/paginator/ListTags.html#CloudHSMV2.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudhsmv2/paginators/#listtagspaginator)
        """
