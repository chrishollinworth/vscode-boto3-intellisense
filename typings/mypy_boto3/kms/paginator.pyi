"""
Type annotations for kms service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html)

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

from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kms.html#KMS.Paginator.ListAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listaliasespaginator)
    """

    def paginate(
        self, *, KeyId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kms.html#KMS.Paginator.ListAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listaliasespaginator)
        """

class ListGrantsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kms.html#KMS.Paginator.ListGrants)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listgrantspaginator)
    """

    def paginate(
        self,
        *,
        KeyId: str,
        GrantId: str = None,
        GranteePrincipal: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGrantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kms.html#KMS.Paginator.ListGrants.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listgrantspaginator)
        """

class ListKeyPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeypoliciespaginator)
    """

    def paginate(
        self, *, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeyPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kms.html#KMS.Paginator.ListKeyPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeypoliciespaginator)
        """

class ListKeysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kms.html#KMS.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeyspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.5/reference/services/kms.html#KMS.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeyspaginator)
        """
