"""
Type annotations for kms service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_kms import KMSClient
    from mypy_boto3_kms.paginator import (
        DescribeCustomKeyStoresPaginator,
        ListAliasesPaginator,
        ListGrantsPaginator,
        ListKeyPoliciesPaginator,
        ListKeysPaginator,
        ListResourceTagsPaginator,
        ListRetirableGrantsPaginator,
    )

    client: KMSClient = boto3.client("kms")

    describe_custom_key_stores_paginator: DescribeCustomKeyStoresPaginator = client.get_paginator("describe_custom_key_stores")
    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_grants_paginator: ListGrantsPaginator = client.get_paginator("list_grants")
    list_key_policies_paginator: ListKeyPoliciesPaginator = client.get_paginator("list_key_policies")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    list_resource_tags_paginator: ListResourceTagsPaginator = client.get_paginator("list_resource_tags")
    list_retirable_grants_paginator: ListRetirableGrantsPaginator = client.get_paginator("list_retirable_grants")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    DescribeCustomKeyStoresResponseTypeDef,
    ListAliasesResponseTypeDef,
    ListGrantsResponseTypeDef,
    ListKeyPoliciesResponseTypeDef,
    ListKeysResponseTypeDef,
    ListResourceTagsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeCustomKeyStoresPaginator",
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeysPaginator",
    "ListResourceTagsPaginator",
    "ListRetirableGrantsPaginator",
)

class DescribeCustomKeyStoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.DescribeCustomKeyStores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#describecustomkeystorespaginator)
    """

    def paginate(
        self,
        *,
        CustomKeyStoreId: str = None,
        CustomKeyStoreName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCustomKeyStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.DescribeCustomKeyStores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#describecustomkeystorespaginator)
        """

class ListAliasesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListAliases)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listaliasespaginator)
    """

    def paginate(
        self, *, KeyId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListAliases.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listaliasespaginator)
        """

class ListGrantsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListGrants)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListGrants.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listgrantspaginator)
        """

class ListKeyPoliciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListKeyPolicies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeypoliciespaginator)
    """

    def paginate(
        self, *, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeyPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListKeyPolicies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeypoliciespaginator)
        """

class ListKeysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeyspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listkeyspaginator)
        """

class ListResourceTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListResourceTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listresourcetagspaginator)
    """

    def paginate(
        self, *, KeyId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListResourceTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listresourcetagspaginator)
        """

class ListRetirableGrantsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListRetirableGrants)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listretirablegrantspaginator)
    """

    def paginate(
        self, *, RetiringPrincipal: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGrantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/kms.html#KMS.Paginator.ListRetirableGrants.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators.html#listretirablegrantspaginator)
        """
