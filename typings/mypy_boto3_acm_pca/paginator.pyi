"""
Type annotations for acm-pca service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_acm_pca.client import ACMPCAClient
    from mypy_boto3_acm_pca.paginator import (
        ListCertificateAuthoritiesPaginator,
        ListPermissionsPaginator,
        ListTagsPaginator,
    )

    session = Session()
    client: ACMPCAClient = session.client("acm-pca")

    list_certificate_authorities_paginator: ListCertificateAuthoritiesPaginator = client.get_paginator("list_certificate_authorities")
    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListCertificateAuthoritiesRequestPaginateTypeDef,
    ListCertificateAuthoritiesResponseTypeDef,
    ListPermissionsRequestPaginateTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsRequestPaginateTypeDef,
    ListTagsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListCertificateAuthoritiesPaginator", "ListPermissionsPaginator", "ListTagsPaginator")

if TYPE_CHECKING:
    _ListCertificateAuthoritiesPaginatorBase = Paginator[ListCertificateAuthoritiesResponseTypeDef]
else:
    _ListCertificateAuthoritiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCertificateAuthoritiesPaginator(_ListCertificateAuthoritiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/paginator/ListCertificateAuthorities.html#ACMPCA.Paginator.ListCertificateAuthorities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators/#listcertificateauthoritiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCertificateAuthoritiesRequestPaginateTypeDef]
    ) -> PageIterator[ListCertificateAuthoritiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/paginator/ListCertificateAuthorities.html#ACMPCA.Paginator.ListCertificateAuthorities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators/#listcertificateauthoritiespaginator)
        """

if TYPE_CHECKING:
    _ListPermissionsPaginatorBase = Paginator[ListPermissionsResponseTypeDef]
else:
    _ListPermissionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPermissionsPaginator(_ListPermissionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/paginator/ListPermissions.html#ACMPCA.Paginator.ListPermissions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators/#listpermissionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPermissionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/paginator/ListPermissions.html#ACMPCA.Paginator.ListPermissions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators/#listpermissionspaginator)
        """

if TYPE_CHECKING:
    _ListTagsPaginatorBase = Paginator[ListTagsResponseTypeDef]
else:
    _ListTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsPaginator(_ListTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/paginator/ListTags.html#ACMPCA.Paginator.ListTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators/#listtagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm-pca/paginator/ListTags.html#ACMPCA.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators/#listtagspaginator)
        """
