"""
Type annotations for controlcatalog service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_controlcatalog.client import ControlCatalogClient
    from mypy_boto3_controlcatalog.paginator import (
        ListCommonControlsPaginator,
        ListControlsPaginator,
        ListDomainsPaginator,
        ListObjectivesPaginator,
    )

    session = Session()
    client: ControlCatalogClient = session.client("controlcatalog")

    list_common_controls_paginator: ListCommonControlsPaginator = client.get_paginator("list_common_controls")
    list_controls_paginator: ListControlsPaginator = client.get_paginator("list_controls")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_objectives_paginator: ListObjectivesPaginator = client.get_paginator("list_objectives")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCommonControlsRequestPaginateTypeDef,
    ListCommonControlsResponseTypeDef,
    ListControlsRequestPaginateTypeDef,
    ListControlsResponseTypeDef,
    ListDomainsRequestPaginateTypeDef,
    ListDomainsResponseTypeDef,
    ListObjectivesRequestPaginateTypeDef,
    ListObjectivesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListCommonControlsPaginator",
    "ListControlsPaginator",
    "ListDomainsPaginator",
    "ListObjectivesPaginator",
)

if TYPE_CHECKING:
    _ListCommonControlsPaginatorBase = Paginator[ListCommonControlsResponseTypeDef]
else:
    _ListCommonControlsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCommonControlsPaginator(_ListCommonControlsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/paginator/ListCommonControls.html#ControlCatalog.Paginator.ListCommonControls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/#listcommoncontrolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCommonControlsRequestPaginateTypeDef]
    ) -> PageIterator[ListCommonControlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/paginator/ListCommonControls.html#ControlCatalog.Paginator.ListCommonControls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/#listcommoncontrolspaginator)
        """

if TYPE_CHECKING:
    _ListControlsPaginatorBase = Paginator[ListControlsResponseTypeDef]
else:
    _ListControlsPaginatorBase = Paginator  # type: ignore[assignment]

class ListControlsPaginator(_ListControlsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/paginator/ListControls.html#ControlCatalog.Paginator.ListControls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/#listcontrolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListControlsRequestPaginateTypeDef]
    ) -> PageIterator[ListControlsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/paginator/ListControls.html#ControlCatalog.Paginator.ListControls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/#listcontrolspaginator)
        """

if TYPE_CHECKING:
    _ListDomainsPaginatorBase = Paginator[ListDomainsResponseTypeDef]
else:
    _ListDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainsPaginator(_ListDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/paginator/ListDomains.html#ControlCatalog.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/#listdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainsRequestPaginateTypeDef]
    ) -> PageIterator[ListDomainsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/paginator/ListDomains.html#ControlCatalog.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/#listdomainspaginator)
        """

if TYPE_CHECKING:
    _ListObjectivesPaginatorBase = Paginator[ListObjectivesResponseTypeDef]
else:
    _ListObjectivesPaginatorBase = Paginator  # type: ignore[assignment]

class ListObjectivesPaginator(_ListObjectivesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/paginator/ListObjectives.html#ControlCatalog.Paginator.ListObjectives)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/#listobjectivespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListObjectivesRequestPaginateTypeDef]
    ) -> PageIterator[ListObjectivesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/controlcatalog/paginator/ListObjectives.html#ControlCatalog.Paginator.ListObjectives.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/paginators/#listobjectivespaginator)
        """
