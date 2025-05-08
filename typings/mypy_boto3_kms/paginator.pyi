"""
Type annotations for kms service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_kms.client import KMSClient
    from mypy_boto3_kms.paginator import (
        DescribeCustomKeyStoresPaginator,
        ListAliasesPaginator,
        ListGrantsPaginator,
        ListKeyPoliciesPaginator,
        ListKeyRotationsPaginator,
        ListKeysPaginator,
        ListResourceTagsPaginator,
        ListRetirableGrantsPaginator,
    )

    session = Session()
    client: KMSClient = session.client("kms")

    describe_custom_key_stores_paginator: DescribeCustomKeyStoresPaginator = client.get_paginator("describe_custom_key_stores")
    list_aliases_paginator: ListAliasesPaginator = client.get_paginator("list_aliases")
    list_grants_paginator: ListGrantsPaginator = client.get_paginator("list_grants")
    list_key_policies_paginator: ListKeyPoliciesPaginator = client.get_paginator("list_key_policies")
    list_key_rotations_paginator: ListKeyRotationsPaginator = client.get_paginator("list_key_rotations")
    list_keys_paginator: ListKeysPaginator = client.get_paginator("list_keys")
    list_resource_tags_paginator: ListResourceTagsPaginator = client.get_paginator("list_resource_tags")
    list_retirable_grants_paginator: ListRetirableGrantsPaginator = client.get_paginator("list_retirable_grants")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeCustomKeyStoresRequestPaginateTypeDef,
    DescribeCustomKeyStoresResponseTypeDef,
    ListAliasesRequestPaginateTypeDef,
    ListAliasesResponseTypeDef,
    ListGrantsRequestPaginateTypeDef,
    ListGrantsResponseTypeDef,
    ListKeyPoliciesRequestPaginateTypeDef,
    ListKeyPoliciesResponseTypeDef,
    ListKeyRotationsRequestPaginateTypeDef,
    ListKeyRotationsResponseTypeDef,
    ListKeysRequestPaginateTypeDef,
    ListKeysResponseTypeDef,
    ListResourceTagsRequestPaginateTypeDef,
    ListResourceTagsResponseTypeDef,
    ListRetirableGrantsRequestPaginateTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeCustomKeyStoresPaginator",
    "ListAliasesPaginator",
    "ListGrantsPaginator",
    "ListKeyPoliciesPaginator",
    "ListKeyRotationsPaginator",
    "ListKeysPaginator",
    "ListResourceTagsPaginator",
    "ListRetirableGrantsPaginator",
)

if TYPE_CHECKING:
    _DescribeCustomKeyStoresPaginatorBase = Paginator[DescribeCustomKeyStoresResponseTypeDef]
else:
    _DescribeCustomKeyStoresPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCustomKeyStoresPaginator(_DescribeCustomKeyStoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/DescribeCustomKeyStores.html#KMS.Paginator.DescribeCustomKeyStores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#describecustomkeystorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCustomKeyStoresRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCustomKeyStoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/DescribeCustomKeyStores.html#KMS.Paginator.DescribeCustomKeyStores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#describecustomkeystorespaginator)
        """

if TYPE_CHECKING:
    _ListAliasesPaginatorBase = Paginator[ListAliasesResponseTypeDef]
else:
    _ListAliasesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAliasesPaginator(_ListAliasesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListAliases.html#KMS.Paginator.ListAliases)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listaliasespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAliasesRequestPaginateTypeDef]
    ) -> PageIterator[ListAliasesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListAliases.html#KMS.Paginator.ListAliases.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listaliasespaginator)
        """

if TYPE_CHECKING:
    _ListGrantsPaginatorBase = Paginator[ListGrantsResponseTypeDef]
else:
    _ListGrantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGrantsPaginator(_ListGrantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListGrants.html#KMS.Paginator.ListGrants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listgrantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGrantsRequestPaginateTypeDef]
    ) -> PageIterator[ListGrantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListGrants.html#KMS.Paginator.ListGrants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listgrantspaginator)
        """

if TYPE_CHECKING:
    _ListKeyPoliciesPaginatorBase = Paginator[ListKeyPoliciesResponseTypeDef]
else:
    _ListKeyPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeyPoliciesPaginator(_ListKeyPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListKeyPolicies.html#KMS.Paginator.ListKeyPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listkeypoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeyPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListKeyPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListKeyPolicies.html#KMS.Paginator.ListKeyPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listkeypoliciespaginator)
        """

if TYPE_CHECKING:
    _ListKeyRotationsPaginatorBase = Paginator[ListKeyRotationsResponseTypeDef]
else:
    _ListKeyRotationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeyRotationsPaginator(_ListKeyRotationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListKeyRotations.html#KMS.Paginator.ListKeyRotations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listkeyrotationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeyRotationsRequestPaginateTypeDef]
    ) -> PageIterator[ListKeyRotationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListKeyRotations.html#KMS.Paginator.ListKeyRotations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listkeyrotationspaginator)
        """

if TYPE_CHECKING:
    _ListKeysPaginatorBase = Paginator[ListKeysResponseTypeDef]
else:
    _ListKeysPaginatorBase = Paginator  # type: ignore[assignment]

class ListKeysPaginator(_ListKeysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListKeys.html#KMS.Paginator.ListKeys)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listkeyspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListKeysRequestPaginateTypeDef]
    ) -> PageIterator[ListKeysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListKeys.html#KMS.Paginator.ListKeys.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listkeyspaginator)
        """

if TYPE_CHECKING:
    _ListResourceTagsPaginatorBase = Paginator[ListResourceTagsResponseTypeDef]
else:
    _ListResourceTagsPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceTagsPaginator(_ListResourceTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListResourceTags.html#KMS.Paginator.ListResourceTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listresourcetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceTagsRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceTagsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListResourceTags.html#KMS.Paginator.ListResourceTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listresourcetagspaginator)
        """

if TYPE_CHECKING:
    _ListRetirableGrantsPaginatorBase = Paginator[ListGrantsResponseTypeDef]
else:
    _ListRetirableGrantsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRetirableGrantsPaginator(_ListRetirableGrantsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListRetirableGrants.html#KMS.Paginator.ListRetirableGrants)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listretirablegrantspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRetirableGrantsRequestPaginateTypeDef]
    ) -> PageIterator[ListGrantsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/kms/paginator/ListRetirableGrants.html#KMS.Paginator.ListRetirableGrants.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kms/paginators/#listretirablegrantspaginator)
        """
