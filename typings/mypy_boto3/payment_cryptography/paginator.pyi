"""
Type annotations for payment-cryptography service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_payment_cryptography import PaymentCryptographyControlPlaneClient
    from mypy_boto3_payment_cryptography.paginator import (
        ListAliasesPaginator,
        ListKeysPaginator,
        ListTagsForResourcePaginator,
    )

    client: PaymentCryptographyControlPlaneClient = boto3.client("payment-cryptography")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import KeyStateType
from .type_defs import (
    ListAliasesOutputTypeDef,
    ListKeysOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListAliasesPaginator", "ListKeysPaginator", "ListTagsForResourcePaginator")

class ListAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listaliasespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listaliasespaginator)
        """

class ListKeysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listkeyspaginator)
    """

    def paginate(
        self, *, KeyState: KeyStateType = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeysOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listkeyspaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/payment-cryptography.html#PaymentCryptographyControlPlane.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_payment_cryptography/paginators.html#listtagsforresourcepaginator)
        """
