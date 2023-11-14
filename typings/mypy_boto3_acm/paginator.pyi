"""
Type annotations for acm service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_acm import ACMClient
    from mypy_boto3_acm.paginator import (
        ListCertificatesPaginator,
    )

    client: ACMClient = boto3.client("acm")

    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import CertificateStatusType, SortOrderType
from .type_defs import FiltersTypeDef, ListCertificatesResponseTypeDef, PaginatorConfigTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListCertificatesPaginator",)

class ListCertificatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/acm.html#ACM.Paginator.ListCertificates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/paginators.html#listcertificatespaginator)
    """

    def paginate(
        self,
        *,
        CertificateStatuses: List[CertificateStatusType] = None,
        Includes: "FiltersTypeDef" = None,
        SortBy: Literal["CREATED_AT"] = None,
        SortOrder: SortOrderType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/acm.html#ACM.Paginator.ListCertificates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_acm/paginators.html#listcertificatespaginator)
        """
