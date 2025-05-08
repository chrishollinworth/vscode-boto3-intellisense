"""
Type annotations for payment-cryptography service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_payment_cryptography.client import PaymentCryptographyControlPlaneClient
    from mypy_boto3_payment_cryptography.paginator import (
        ListAliasesPaginator,
        ListKeysPaginator,
        ListTagsForResourcePaginator,
    )

    session = Session()
    client: PaymentCryptographyControlPlaneClient = session.client("payment-cryptography")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAliasesInputPaginateTypeDef,
    ListAliasesOutputTypeDef,
    ListKeysInputPaginateTypeDef,
    ListKeysOutputTypeDef,
    ListTagsForResourceInputPaginateTypeDef,
    ListTagsForResourceOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("ListAliasesPaginator", "ListKeysPaginator", "ListTagsForResourcePaginator")

if TYPE_CHECKING:
    _ListAliasesPaginatorBase = Paginator[ListAliasesOutputTypeDef]
else:
    _ListAliasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAliasesPaginator(_ListAliasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/paginator/ListAliases.html#PaymentCryptographyControlPlane.Paginator.ListAliases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators/#listaliasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAliasesInputPaginateTypeDef]
    ) -> PageIterator[ListAliasesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/paginator/ListAliases.html#PaymentCryptographyControlPlane.Paginator.ListAliases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators/#listaliasespaginator)
        """

if TYPE_CHECKING:
    _ListKeysPaginatorBase = Paginator[ListKeysOutputTypeDef]
else:
    _ListKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeysPaginator(_ListKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/paginator/ListKeys.html#PaymentCryptographyControlPlane.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators/#listkeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeysInputPaginateTypeDef]
    ) -> PageIterator[ListKeysOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/paginator/ListKeys.html#PaymentCryptographyControlPlane.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators/#listkeyspaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceOutputTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/paginator/ListTagsForResource.html#PaymentCryptographyControlPlane.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceInputPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/payment-cryptography/paginator/ListTagsForResource.html#PaymentCryptographyControlPlane.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators/#listtagsforresourcepaginator)
        """
