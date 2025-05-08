"""
Type annotations for appfabric service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_appfabric.client import AppFabricClient
    from mypy_boto3_appfabric.paginator import (
        ListAppAuthorizationsPaginator,
        ListAppBundlesPaginator,
        ListIngestionDestinationsPaginator,
        ListIngestionsPaginator,
    )

    session = Session()
    client: AppFabricClient = session.client("appfabric")

    list_app_authorizations_paginator: ListAppAuthorizationsPaginator = client.get_paginator("list_app_authorizations")
    list_app_bundles_paginator: ListAppBundlesPaginator = client.get_paginator("list_app_bundles")
    list_ingestion_destinations_paginator: ListIngestionDestinationsPaginator = client.get_paginator("list_ingestion_destinations")
    list_ingestions_paginator: ListIngestionsPaginator = client.get_paginator("list_ingestions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAppAuthorizationsRequestPaginateTypeDef,
    ListAppAuthorizationsResponseTypeDef,
    ListAppBundlesRequestPaginateTypeDef,
    ListAppBundlesResponseTypeDef,
    ListIngestionDestinationsRequestPaginateTypeDef,
    ListIngestionDestinationsResponseTypeDef,
    ListIngestionsRequestPaginateTypeDef,
    ListIngestionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAppAuthorizationsPaginator",
    "ListAppBundlesPaginator",
    "ListIngestionDestinationsPaginator",
    "ListIngestionsPaginator",
)

if TYPE_CHECKING:
    _ListAppAuthorizationsPaginatorBase = Paginator[ListAppAuthorizationsResponseTypeDef]
else:
    _ListAppAuthorizationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAppAuthorizationsPaginator(_ListAppAuthorizationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric/paginator/ListAppAuthorizations.html#AppFabric.Paginator.ListAppAuthorizations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/#listappauthorizationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAppAuthorizationsRequestPaginateTypeDef]
    ) -> PageIterator[ListAppAuthorizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric/paginator/ListAppAuthorizations.html#AppFabric.Paginator.ListAppAuthorizations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/#listappauthorizationspaginator)
        """

if TYPE_CHECKING:
    _ListAppBundlesPaginatorBase = Paginator[ListAppBundlesResponseTypeDef]
else:
    _ListAppBundlesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAppBundlesPaginator(_ListAppBundlesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric/paginator/ListAppBundles.html#AppFabric.Paginator.ListAppBundles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/#listappbundlespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAppBundlesRequestPaginateTypeDef]
    ) -> PageIterator[ListAppBundlesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric/paginator/ListAppBundles.html#AppFabric.Paginator.ListAppBundles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/#listappbundlespaginator)
        """

if TYPE_CHECKING:
    _ListIngestionDestinationsPaginatorBase = Paginator[ListIngestionDestinationsResponseTypeDef]
else:
    _ListIngestionDestinationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIngestionDestinationsPaginator(_ListIngestionDestinationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric/paginator/ListIngestionDestinations.html#AppFabric.Paginator.ListIngestionDestinations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/#listingestiondestinationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIngestionDestinationsRequestPaginateTypeDef]
    ) -> PageIterator[ListIngestionDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric/paginator/ListIngestionDestinations.html#AppFabric.Paginator.ListIngestionDestinations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/#listingestiondestinationspaginator)
        """

if TYPE_CHECKING:
    _ListIngestionsPaginatorBase = Paginator[ListIngestionsResponseTypeDef]
else:
    _ListIngestionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIngestionsPaginator(_ListIngestionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric/paginator/ListIngestions.html#AppFabric.Paginator.ListIngestions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/#listingestionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIngestionsRequestPaginateTypeDef]
    ) -> PageIterator[ListIngestionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appfabric/paginator/ListIngestions.html#AppFabric.Paginator.ListIngestions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators/#listingestionspaginator)
        """
