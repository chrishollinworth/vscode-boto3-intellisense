"""
Type annotations for opsworkscm service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_opsworkscm.client import OpsWorksCMClient
    from mypy_boto3_opsworkscm.paginator import (
        DescribeBackupsPaginator,
        DescribeEventsPaginator,
        DescribeServersPaginator,
        ListTagsForResourcePaginator,
    )

    session = Session()
    client: OpsWorksCMClient = session.client("opsworkscm")

    describe_backups_paginator: DescribeBackupsPaginator = client.get_paginator("describe_backups")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_servers_paginator: DescribeServersPaginator = client.get_paginator("describe_servers")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeBackupsRequestPaginateTypeDef,
    DescribeBackupsResponseTypeDef,
    DescribeEventsRequestPaginateTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeServersRequestPaginateTypeDef,
    DescribeServersResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeBackupsPaginator",
    "DescribeEventsPaginator",
    "DescribeServersPaginator",
    "ListTagsForResourcePaginator",
)

if TYPE_CHECKING:
    _DescribeBackupsPaginatorBase = Paginator[DescribeBackupsResponseTypeDef]
else:
    _DescribeBackupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeBackupsPaginator(_DescribeBackupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/paginator/DescribeBackups.html#OpsWorksCM.Paginator.DescribeBackups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/#describebackupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeBackupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeBackupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/paginator/DescribeBackups.html#OpsWorksCM.Paginator.DescribeBackups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/#describebackupspaginator)
        """

if TYPE_CHECKING:
    _DescribeEventsPaginatorBase = Paginator[DescribeEventsResponseTypeDef]
else:
    _DescribeEventsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEventsPaginator(_DescribeEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/paginator/DescribeEvents.html#OpsWorksCM.Paginator.DescribeEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/#describeeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEventsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/paginator/DescribeEvents.html#OpsWorksCM.Paginator.DescribeEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/#describeeventspaginator)
        """

if TYPE_CHECKING:
    _DescribeServersPaginatorBase = Paginator[DescribeServersResponseTypeDef]
else:
    _DescribeServersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeServersPaginator(_DescribeServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/paginator/DescribeServers.html#OpsWorksCM.Paginator.DescribeServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/#describeserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeServersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/paginator/DescribeServers.html#OpsWorksCM.Paginator.DescribeServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/#describeserverspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/paginator/ListTagsForResource.html#OpsWorksCM.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/opsworkscm/paginator/ListTagsForResource.html#OpsWorksCM.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_opsworkscm/paginators/#listtagsforresourcepaginator)
        """
