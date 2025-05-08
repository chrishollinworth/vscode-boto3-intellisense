"""
Type annotations for route53profiles service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_route53profiles.client import Route53ProfilesClient
    from mypy_boto3_route53profiles.paginator import (
        ListProfileAssociationsPaginator,
        ListProfileResourceAssociationsPaginator,
        ListProfilesPaginator,
    )

    session = Session()
    client: Route53ProfilesClient = session.client("route53profiles")

    list_profile_associations_paginator: ListProfileAssociationsPaginator = client.get_paginator("list_profile_associations")
    list_profile_resource_associations_paginator: ListProfileResourceAssociationsPaginator = client.get_paginator("list_profile_resource_associations")
    list_profiles_paginator: ListProfilesPaginator = client.get_paginator("list_profiles")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListProfileAssociationsRequestPaginateTypeDef,
    ListProfileAssociationsResponseTypeDef,
    ListProfileResourceAssociationsRequestPaginateTypeDef,
    ListProfileResourceAssociationsResponseTypeDef,
    ListProfilesRequestPaginateTypeDef,
    ListProfilesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListProfileAssociationsPaginator",
    "ListProfileResourceAssociationsPaginator",
    "ListProfilesPaginator",
)

if TYPE_CHECKING:
    _ListProfileAssociationsPaginatorBase = Paginator[ListProfileAssociationsResponseTypeDef]
else:
    _ListProfileAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProfileAssociationsPaginator(_ListProfileAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/paginator/ListProfileAssociations.html#Route53Profiles.Paginator.ListProfileAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators/#listprofileassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProfileAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListProfileAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/paginator/ListProfileAssociations.html#Route53Profiles.Paginator.ListProfileAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators/#listprofileassociationspaginator)
        """

if TYPE_CHECKING:
    _ListProfileResourceAssociationsPaginatorBase = Paginator[
        ListProfileResourceAssociationsResponseTypeDef
    ]
else:
    _ListProfileResourceAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListProfileResourceAssociationsPaginator(_ListProfileResourceAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/paginator/ListProfileResourceAssociations.html#Route53Profiles.Paginator.ListProfileResourceAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators/#listprofileresourceassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProfileResourceAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListProfileResourceAssociationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/paginator/ListProfileResourceAssociations.html#Route53Profiles.Paginator.ListProfileResourceAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators/#listprofileresourceassociationspaginator)
        """

if TYPE_CHECKING:
    _ListProfilesPaginatorBase = Paginator[ListProfilesResponseTypeDef]
else:
    _ListProfilesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProfilesPaginator(_ListProfilesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/paginator/ListProfiles.html#Route53Profiles.Paginator.ListProfiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators/#listprofilespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProfilesRequestPaginateTypeDef]
    ) -> PageIterator[ListProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53profiles/paginator/ListProfiles.html#Route53Profiles.Paginator.ListProfiles.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/paginators/#listprofilespaginator)
        """
