"""
Type annotations for dataexchange service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_dataexchange.client import DataExchangeClient
    from mypy_boto3_dataexchange.paginator import (
        ListDataGrantsPaginator,
        ListDataSetRevisionsPaginator,
        ListDataSetsPaginator,
        ListEventActionsPaginator,
        ListJobsPaginator,
        ListReceivedDataGrantsPaginator,
        ListRevisionAssetsPaginator,
    )

    session = Session()
    client: DataExchangeClient = session.client("dataexchange")

    list_data_grants_paginator: ListDataGrantsPaginator = client.get_paginator("list_data_grants")
    list_data_set_revisions_paginator: ListDataSetRevisionsPaginator = client.get_paginator("list_data_set_revisions")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_event_actions_paginator: ListEventActionsPaginator = client.get_paginator("list_event_actions")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_received_data_grants_paginator: ListReceivedDataGrantsPaginator = client.get_paginator("list_received_data_grants")
    list_revision_assets_paginator: ListRevisionAssetsPaginator = client.get_paginator("list_revision_assets")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDataGrantsRequestPaginateTypeDef,
    ListDataGrantsResponseTypeDef,
    ListDataSetRevisionsRequestPaginateTypeDef,
    ListDataSetRevisionsResponseTypeDef,
    ListDataSetsRequestPaginateTypeDef,
    ListDataSetsResponseTypeDef,
    ListEventActionsRequestPaginateTypeDef,
    ListEventActionsResponseTypeDef,
    ListJobsRequestPaginateTypeDef,
    ListJobsResponseTypeDef,
    ListReceivedDataGrantsRequestPaginateTypeDef,
    ListReceivedDataGrantsResponseTypeDef,
    ListRevisionAssetsRequestPaginateTypeDef,
    ListRevisionAssetsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDataGrantsPaginator",
    "ListDataSetRevisionsPaginator",
    "ListDataSetsPaginator",
    "ListEventActionsPaginator",
    "ListJobsPaginator",
    "ListReceivedDataGrantsPaginator",
    "ListRevisionAssetsPaginator",
)

if TYPE_CHECKING:
    _ListDataGrantsPaginatorBase = Paginator[ListDataGrantsResponseTypeDef]
else:
    _ListDataGrantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataGrantsPaginator(_ListDataGrantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListDataGrants.html#DataExchange.Paginator.ListDataGrants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listdatagrantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataGrantsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataGrantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListDataGrants.html#DataExchange.Paginator.ListDataGrants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listdatagrantspaginator)
        """

if TYPE_CHECKING:
    _ListDataSetRevisionsPaginatorBase = Paginator[ListDataSetRevisionsResponseTypeDef]
else:
    _ListDataSetRevisionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSetRevisionsPaginator(_ListDataSetRevisionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListDataSetRevisions.html#DataExchange.Paginator.ListDataSetRevisions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listdatasetrevisionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSetRevisionsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSetRevisionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListDataSetRevisions.html#DataExchange.Paginator.ListDataSetRevisions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listdatasetrevisionspaginator)
        """

if TYPE_CHECKING:
    _ListDataSetsPaginatorBase = Paginator[ListDataSetsResponseTypeDef]
else:
    _ListDataSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSetsPaginator(_ListDataSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListDataSets.html#DataExchange.Paginator.ListDataSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListDataSets.html#DataExchange.Paginator.ListDataSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listdatasetspaginator)
        """

if TYPE_CHECKING:
    _ListEventActionsPaginatorBase = Paginator[ListEventActionsResponseTypeDef]
else:
    _ListEventActionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEventActionsPaginator(_ListEventActionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListEventActions.html#DataExchange.Paginator.ListEventActions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listeventactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEventActionsRequestPaginateTypeDef]
    ) -> PageIterator[ListEventActionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListEventActions.html#DataExchange.Paginator.ListEventActions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listeventactionspaginator)
        """

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsResponseTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListJobs.html#DataExchange.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListJobs.html#DataExchange.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listjobspaginator)
        """

if TYPE_CHECKING:
    _ListReceivedDataGrantsPaginatorBase = Paginator[ListReceivedDataGrantsResponseTypeDef]
else:
    _ListReceivedDataGrantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListReceivedDataGrantsPaginator(_ListReceivedDataGrantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListReceivedDataGrants.html#DataExchange.Paginator.ListReceivedDataGrants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listreceiveddatagrantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListReceivedDataGrantsRequestPaginateTypeDef]
    ) -> PageIterator[ListReceivedDataGrantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListReceivedDataGrants.html#DataExchange.Paginator.ListReceivedDataGrants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listreceiveddatagrantspaginator)
        """

if TYPE_CHECKING:
    _ListRevisionAssetsPaginatorBase = Paginator[ListRevisionAssetsResponseTypeDef]
else:
    _ListRevisionAssetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRevisionAssetsPaginator(_ListRevisionAssetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListRevisionAssets.html#DataExchange.Paginator.ListRevisionAssets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listrevisionassetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRevisionAssetsRequestPaginateTypeDef]
    ) -> PageIterator[ListRevisionAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dataexchange/paginator/ListRevisionAssets.html#DataExchange.Paginator.ListRevisionAssets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/paginators/#listrevisionassetspaginator)
        """
