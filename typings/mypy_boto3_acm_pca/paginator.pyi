# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for acm-pca service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_acm_pca import ACMPCAClient
    from mypy_boto3_acm_pca.paginator import (
        ListCertificateAuthoritiesPaginator,
        ListPermissionsPaginator,
        ListTagsPaginator,
    )

    client: ACMPCAClient = boto3.client("acm-pca")

    list_certificate_authorities_paginator: ListCertificateAuthoritiesPaginator = client.get_paginator("list_certificate_authorities")
    list_permissions_paginator: ListPermissionsPaginator = client.get_paginator("list_permissions")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_acm_pca.type_defs import (
    ListCertificateAuthoritiesResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListCertificateAuthoritiesPaginator", "ListPermissionsPaginator", "ListTagsPaginator")


class ListCertificateAuthoritiesPaginator(Boto3Paginator):
    """
    [Paginator.ListCertificateAuthorities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)
    """

    def paginate(
        self,
        ResourceOwner: Literal["SELF", "OTHER_ACCOUNTS"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCertificateAuthoritiesResponseTypeDef]:
        """
        [ListCertificateAuthorities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities.paginate)
        """


class ListPermissionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPermissions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)
    """

    def paginate(
        self, CertificateAuthorityArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionsResponseTypeDef]:
        """
        [ListPermissions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)
    """

    def paginate(
        self, CertificateAuthorityArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags.paginate)
        """
