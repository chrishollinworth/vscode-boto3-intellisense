"""
Type annotations for b2bi service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_b2bi.client import B2BIClient
    from mypy_boto3_b2bi.paginator import (
        ListCapabilitiesPaginator,
        ListPartnershipsPaginator,
        ListProfilesPaginator,
        ListTransformersPaginator,
    )

    session = Session()
    client: B2BIClient = session.client("b2bi")

    list_capabilities_paginator: ListCapabilitiesPaginator = client.get_paginator("list_capabilities")
    list_partnerships_paginator: ListPartnershipsPaginator = client.get_paginator("list_partnerships")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    list_transformers_paginator: ListTransformersPaginator = client.get_paginator("list_transformers")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCapabilitiesRequestPaginateTypeDef,
    ListCapabilitiesResponseTypeDef,
    ListPartnershipsRequestPaginateTypeDef,
    ListPartnershipsResponseTypeDef,
    ListProfilesRequestPaginateTypeDef,
    ListProfilesResponseTypeDef,
    ListTransformersRequestPaginateTypeDef,
    ListTransformersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListCapabilitiesPaginator",
    "ListPartnershipsPaginator",
    "ListProfilesPaginator",
    "ListTransformersPaginator",
)

if TYPE_CHECKING:
    _ListCapabilitiesPaginatorBase = Paginator[ListCapabilitiesResponseTypeDef]
else:
    _ListCapabilitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCapabilitiesPaginator(_ListCapabilitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/paginator/ListCapabilities.html#B2BI.Paginator.ListCapabilities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/#listcapabilitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCapabilitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListCapabilitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/paginator/ListCapabilities.html#B2BI.Paginator.ListCapabilities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/#listcapabilitiespaginator)
        """

if TYPE_CHECKING:
    _ListPartnershipsPaginatorBase = Paginator[ListPartnershipsResponseTypeDef]
else:
    _ListPartnershipsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPartnershipsPaginator(_ListPartnershipsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/paginator/ListPartnerships.html#B2BI.Paginator.ListPartnerships)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/#listpartnershipspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPartnershipsRequestPaginateTypeDef]
    ) -> PageIterator[ListPartnershipsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/paginator/ListPartnerships.html#B2BI.Paginator.ListPartnerships.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/#listpartnershipspaginator)
        """

if TYPE_CHECKING:
    _ListProfilesPaginatorBase = Paginator[ListProfilesResponseTypeDef]
else:
    _ListProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProfilesPaginator(_ListProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/paginator/ListProfiles.html#B2BI.Paginator.ListProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/#listprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/paginator/ListProfiles.html#B2BI.Paginator.ListProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/#listprofilespaginator)
        """

if TYPE_CHECKING:
    _ListTransformersPaginatorBase = Paginator[ListTransformersResponseTypeDef]
else:
    _ListTransformersPaginatorBase = Paginator  # type: ignore[assignment]

class ListTransformersPaginator(_ListTransformersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/paginator/ListTransformers.html#B2BI.Paginator.ListTransformers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/#listtransformerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTransformersRequestPaginateTypeDef]
    ) -> PageIterator[ListTransformersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/b2bi/paginator/ListTransformers.html#B2BI.Paginator.ListTransformers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_b2bi/paginators/#listtransformerspaginator)
        """
