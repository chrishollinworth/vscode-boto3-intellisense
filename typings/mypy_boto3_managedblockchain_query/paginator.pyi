"""
Type annotations for managedblockchain-query service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_managedblockchain_query.client import ManagedBlockchainQueryClient
    from mypy_boto3_managedblockchain_query.paginator import (
        ListAssetContractsPaginator,
        ListFilteredTransactionEventsPaginator,
        ListTokenBalancesPaginator,
        ListTransactionEventsPaginator,
        ListTransactionsPaginator,
    )

    session = Session()
    client: ManagedBlockchainQueryClient = session.client("managedblockchain-query")

    list_asset_contracts_paginator: ListAssetContractsPaginator = client.get_paginator("list_asset_contracts")
    list_filtered_transaction_events_paginator: ListFilteredTransactionEventsPaginator = client.get_paginator("list_filtered_transaction_events")
    list_token_balances_paginator: ListTokenBalancesPaginator = client.get_paginator("list_token_balances")
    list_transaction_events_paginator: ListTransactionEventsPaginator = client.get_paginator("list_transaction_events")
    list_transactions_paginator: ListTransactionsPaginator = client.get_paginator("list_transactions")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAssetContractsInputPaginateTypeDef,
    ListAssetContractsOutputTypeDef,
    ListFilteredTransactionEventsInputPaginateTypeDef,
    ListFilteredTransactionEventsOutputTypeDef,
    ListTokenBalancesInputPaginateTypeDef,
    ListTokenBalancesOutputTypeDef,
    ListTransactionEventsInputPaginateTypeDef,
    ListTransactionEventsOutputTypeDef,
    ListTransactionsInputPaginateTypeDef,
    ListTransactionsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAssetContractsPaginator",
    "ListFilteredTransactionEventsPaginator",
    "ListTokenBalancesPaginator",
    "ListTransactionEventsPaginator",
    "ListTransactionsPaginator",
)

if TYPE_CHECKING:
    _ListAssetContractsPaginatorBase = Paginator[ListAssetContractsOutputTypeDef]
else:
    _ListAssetContractsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssetContractsPaginator(_ListAssetContractsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListAssetContracts.html#ManagedBlockchainQuery.Paginator.ListAssetContracts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listassetcontractspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssetContractsInputPaginateTypeDef]
    ) -> PageIterator[ListAssetContractsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListAssetContracts.html#ManagedBlockchainQuery.Paginator.ListAssetContracts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listassetcontractspaginator)
        """

if TYPE_CHECKING:
    _ListFilteredTransactionEventsPaginatorBase = Paginator[
        ListFilteredTransactionEventsOutputTypeDef
    ]
else:
    _ListFilteredTransactionEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFilteredTransactionEventsPaginator(_ListFilteredTransactionEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListFilteredTransactionEvents.html#ManagedBlockchainQuery.Paginator.ListFilteredTransactionEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listfilteredtransactioneventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFilteredTransactionEventsInputPaginateTypeDef]
    ) -> PageIterator[ListFilteredTransactionEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListFilteredTransactionEvents.html#ManagedBlockchainQuery.Paginator.ListFilteredTransactionEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listfilteredtransactioneventspaginator)
        """

if TYPE_CHECKING:
    _ListTokenBalancesPaginatorBase = Paginator[ListTokenBalancesOutputTypeDef]
else:
    _ListTokenBalancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTokenBalancesPaginator(_ListTokenBalancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListTokenBalances.html#ManagedBlockchainQuery.Paginator.ListTokenBalances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listtokenbalancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTokenBalancesInputPaginateTypeDef]
    ) -> PageIterator[ListTokenBalancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListTokenBalances.html#ManagedBlockchainQuery.Paginator.ListTokenBalances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listtokenbalancespaginator)
        """

if TYPE_CHECKING:
    _ListTransactionEventsPaginatorBase = Paginator[ListTransactionEventsOutputTypeDef]
else:
    _ListTransactionEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTransactionEventsPaginator(_ListTransactionEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListTransactionEvents.html#ManagedBlockchainQuery.Paginator.ListTransactionEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listtransactioneventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTransactionEventsInputPaginateTypeDef]
    ) -> PageIterator[ListTransactionEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListTransactionEvents.html#ManagedBlockchainQuery.Paginator.ListTransactionEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listtransactioneventspaginator)
        """

if TYPE_CHECKING:
    _ListTransactionsPaginatorBase = Paginator[ListTransactionsOutputTypeDef]
else:
    _ListTransactionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTransactionsPaginator(_ListTransactionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListTransactions.html#ManagedBlockchainQuery.Paginator.ListTransactions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listtransactionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTransactionsInputPaginateTypeDef]
    ) -> PageIterator[ListTransactionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/managedblockchain-query/paginator/ListTransactions.html#ManagedBlockchainQuery.Paginator.ListTransactions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators/#listtransactionspaginator)
        """
