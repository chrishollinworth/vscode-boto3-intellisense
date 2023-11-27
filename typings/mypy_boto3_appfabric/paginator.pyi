"""
Type annotations for appfabric service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_appfabric import AppFabricClient
    from mypy_boto3_appfabric.paginator import (
        ListAppAuthorizationsPaginator,
        ListAppBundlesPaginator,
        ListIngestionDestinationsPaginator,
        ListIngestionsPaginator,
    )

    client: AppFabricClient = boto3.client("appfabric")

    list_app_authorizations_paginator: ListAppAuthorizationsPaginator = client.get_paginator("list_app_authorizations")
    list_app_bundles_paginator: ListAppBundlesPaginator = client.get_paginator("list_app_bundles")
    list_ingestion_destinations_paginator: ListIngestionDestinationsPaginator = client.get_paginator("list_ingestion_destinations")
    list_ingestions_paginator: ListIngestionsPaginator = client.get_paginator("list_ingestions")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListAppAuthorizationsResponseTypeDef,
    ListAppBundlesResponseTypeDef,
    ListIngestionDestinationsResponseTypeDef,
    ListIngestionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAppAuthorizationsPaginator",
    "ListAppBundlesPaginator",
    "ListIngestionDestinationsPaginator",
    "ListIngestionsPaginator",
)

class ListAppAuthorizationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListAppAuthorizations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listappauthorizationspaginator)
    """

    def paginate(
        self, *, appBundleIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppAuthorizationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListAppAuthorizations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listappauthorizationspaginator)
        """

class ListAppBundlesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListAppBundles)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listappbundlespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAppBundlesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListAppBundles.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listappbundlespaginator)
        """

class ListIngestionDestinationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListIngestionDestinations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listingestiondestinationspaginator)
    """

    def paginate(
        self,
        *,
        appBundleIdentifier: str,
        ingestionIdentifier: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIngestionDestinationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListIngestionDestinations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listingestiondestinationspaginator)
        """

class ListIngestionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListIngestions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listingestionspaginator)
    """

    def paginate(
        self, *, appBundleIdentifier: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIngestionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appfabric.html#AppFabric.Paginator.ListIngestions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appfabric/paginators.html#listingestionspaginator)
        """
