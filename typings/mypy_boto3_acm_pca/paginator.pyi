"""
Type annotations for acm-pca service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html)

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
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ResourceOwnerType
from .type_defs import (
    ListCertificateAuthoritiesResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListCertificateAuthoritiesPaginator", "ListPermissionsPaginator", "ListTagsPaginator")

class ListCertificateAuthoritiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listcertificateauthoritiespaginator)
    """

    def paginate(
        self,
        *,
        ResourceOwner: ResourceOwnerType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificateAuthoritiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/acm-pca.html#ACMPCA.Paginator.ListCertificateAuthorities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listcertificateauthoritiespaginator)
        """

class ListPermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listpermissionspaginator)
    """

    def paginate(
        self, *, CertificateAuthorityArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPermissionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/acm-pca.html#ACMPCA.Paginator.ListPermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listpermissionspaginator)
        """

class ListTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listtagspaginator)
    """

    def paginate(
        self, *, CertificateAuthorityArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/acm-pca.html#ACMPCA.Paginator.ListTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm_pca/paginators.html#listtagspaginator)
        """
