"""
Type annotations for acm service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_acm.client import ACMClient
    from mypy_boto3_acm.paginator import (
        ListCertificatesPaginator,
    )

    session = Session()
    client: ACMClient = session.client("acm")

    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import ListCertificatesRequestPaginateTypeDef, ListCertificatesResponseTypeDef

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListCertificatesPaginator",)

if TYPE_CHECKING:
    _ListCertificatesPaginatorBase = Paginator[ListCertificatesResponseTypeDef]
else:
    _ListCertificatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListCertificatesPaginator(_ListCertificatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm/paginator/ListCertificates.html#ACM.Paginator.ListCertificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm/paginators/#listcertificatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCertificatesRequestPaginateTypeDef]
    ) -> PageIterator[ListCertificatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/acm/paginator/ListCertificates.html#ACM.Paginator.ListCertificates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_acm/paginators/#listcertificatespaginator)
        """
