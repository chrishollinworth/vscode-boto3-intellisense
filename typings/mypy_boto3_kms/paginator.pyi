# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for kms service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_kms import KMSClient
    from mypy_boto3_kms.paginator import (
        ListAliasesPaginator,
        ListGrantsPaginator,
        ListKeyPoliciesPaginator,
        ListKeysPaginator,
    )

    client: KMSClient = boto3.client("kms")

    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_grants_paginator: ListGrantsPaginator = client.get_paginator("list_grants")
    list_key_policies_paginator: ListKeyPoliciesPaginator = client.get_paginator("list_key_policies")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_kms.type_defs import (
    ListAliasesResponseTypeDef,
    ListGrantsResponseTypeDef,
    ListKeyPoliciesResponseTypeDef,
    ListKeysResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeysPaginator",
)


class ListAliasesPaginator(Boto3Paginator):
    """
    [Paginator.ListAliases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListAliases)
    """

    def paginate(
        self, KeyId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesResponseTypeDef]:
        """
        [ListAliases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListAliases.paginate)
        """


class ListGrantsPaginator(Boto3Paginator):
    """
    [Paginator.ListGrants documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListGrants)
    """

    def paginate(
        self, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGrantsResponseTypeDef]:
        """
        [ListGrants.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListGrants.paginate)
        """


class ListKeyPoliciesPaginator(Boto3Paginator):
    """
    [Paginator.ListKeyPolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)
    """

    def paginate(
        self, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeyPoliciesResponseTypeDef]:
        """
        [ListKeyPolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListKeyPolicies.paginate)
        """


class ListKeysPaginator(Boto3Paginator):
    """
    [Paginator.ListKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListKeys)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeysResponseTypeDef]:
        """
        [ListKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kms.html#KMS.Paginator.ListKeys.paginate)
        """
