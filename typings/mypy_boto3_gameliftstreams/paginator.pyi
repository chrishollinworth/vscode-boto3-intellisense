"""
Type annotations for gameliftstreams service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_gameliftstreams.client import GameLiftStreamsClient
    from mypy_boto3_gameliftstreams.paginator import (
        ListApplicationsPaginator,
        ListStreamGroupsPaginator,
        ListStreamSessionsByAccountPaginator,
        ListStreamSessionsPaginator,
    )

    session = Session()
    client: GameLiftStreamsClient = session.client("gameliftstreams")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_stream_groups_paginator: ListStreamGroupsPaginator = client.get_paginator("list_stream_groups")
    list_stream_sessions_by_account_paginator: ListStreamSessionsByAccountPaginator = client.get_paginator("list_stream_sessions_by_account")
    list_stream_sessions_paginator: ListStreamSessionsPaginator = client.get_paginator("list_stream_sessions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationsInputPaginateTypeDef,
    ListApplicationsOutputTypeDef,
    ListStreamGroupsInputPaginateTypeDef,
    ListStreamGroupsOutputTypeDef,
    ListStreamSessionsByAccountInputPaginateTypeDef,
    ListStreamSessionsByAccountOutputTypeDef,
    ListStreamSessionsInputPaginateTypeDef,
    ListStreamSessionsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationsPaginator",
    "ListStreamGroupsPaginator",
    "ListStreamSessionsByAccountPaginator",
    "ListStreamSessionsPaginator",
)

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsOutputTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/paginator/ListApplications.html#GameLiftStreams.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsInputPaginateTypeDef]
    ) -> PageIterator[ListApplicationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/paginator/ListApplications.html#GameLiftStreams.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListStreamGroupsPaginatorBase = Paginator[ListStreamGroupsOutputTypeDef]
else:
    _ListStreamGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamGroupsPaginator(_ListStreamGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/paginator/ListStreamGroups.html#GameLiftStreams.Paginator.ListStreamGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/#liststreamgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamGroupsInputPaginateTypeDef]
    ) -> PageIterator[ListStreamGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/paginator/ListStreamGroups.html#GameLiftStreams.Paginator.ListStreamGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/#liststreamgroupspaginator)
        """

if TYPE_CHECKING:
    _ListStreamSessionsByAccountPaginatorBase = Paginator[ListStreamSessionsByAccountOutputTypeDef]
else:
    _ListStreamSessionsByAccountPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamSessionsByAccountPaginator(_ListStreamSessionsByAccountPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/paginator/ListStreamSessionsByAccount.html#GameLiftStreams.Paginator.ListStreamSessionsByAccount)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/#liststreamsessionsbyaccountpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamSessionsByAccountInputPaginateTypeDef]
    ) -> PageIterator[ListStreamSessionsByAccountOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/paginator/ListStreamSessionsByAccount.html#GameLiftStreams.Paginator.ListStreamSessionsByAccount.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/#liststreamsessionsbyaccountpaginator)
        """

if TYPE_CHECKING:
    _ListStreamSessionsPaginatorBase = Paginator[ListStreamSessionsOutputTypeDef]
else:
    _ListStreamSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListStreamSessionsPaginator(_ListStreamSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/paginator/ListStreamSessions.html#GameLiftStreams.Paginator.ListStreamSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/#liststreamsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListStreamSessionsInputPaginateTypeDef]
    ) -> PageIterator[ListStreamSessionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/gameliftstreams/paginator/ListStreamSessions.html#GameLiftStreams.Paginator.ListStreamSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_gameliftstreams/paginators/#liststreamsessionspaginator)
        """
