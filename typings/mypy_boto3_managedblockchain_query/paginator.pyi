"""
Type annotations for managedblockchain-query service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_managedblockchain_query import ManagedBlockchainQueryClient
    from mypy_boto3_managedblockchain_query.paginator import (
        ListAssetContractsPaginator,
        ListTokenBalancesPaginator,
        ListTransactionEventsPaginator,
        ListTransactionsPaginator,
    )

    client: ManagedBlockchainQueryClient = boto3.client("managedblockchain-query")

    list_asset_contracts_paginator: ListAssetContractsPaginator = client.get_paginator("list_asset_contracts")
    list_token_balances_paginator: ListTokenBalancesPaginator = client.get_paginator("list_token_balances")
    list_transaction_events_paginator: ListTransactionEventsPaginator = client.get_paginator("list_transaction_events")
    list_transactions_paginator: ListTransactionsPaginator = client.get_paginator("list_transactions")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import QueryNetworkType
from .type_defs import (
    BlockchainInstantTypeDef,
    ContractFilterTypeDef,
    ListAssetContractsOutputTypeDef,
    ListTokenBalancesOutputTypeDef,
    ListTransactionEventsOutputTypeDef,
    ListTransactionsOutputTypeDef,
    ListTransactionsSortTypeDef,
    OwnerFilterTypeDef,
    PaginatorConfigTypeDef,
    TokenFilterTypeDef,
)

__all__ = (
    "ListAssetContractsPaginator",
    "ListTokenBalancesPaginator",
    "ListTransactionEventsPaginator",
    "ListTransactionsPaginator",
)

class ListAssetContractsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListAssetContracts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listassetcontractspaginator)
    """

    def paginate(
        self,
        *,
        contractFilter: "ContractFilterTypeDef",
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssetContractsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListAssetContracts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listassetcontractspaginator)
        """

class ListTokenBalancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTokenBalances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtokenbalancespaginator)
    """

    def paginate(
        self,
        *,
        tokenFilter: "TokenFilterTypeDef",
        ownerFilter: "OwnerFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTokenBalancesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTokenBalances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtokenbalancespaginator)
        """

class ListTransactionEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactionEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtransactioneventspaginator)
    """

    def paginate(
        self,
        *,
        transactionHash: str,
        network: QueryNetworkType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTransactionEventsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactionEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtransactioneventspaginator)
        """

class ListTransactionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtransactionspaginator)
    """

    def paginate(
        self,
        *,
        address: str,
        network: QueryNetworkType,
        fromBlockchainInstant: "BlockchainInstantTypeDef" = None,
        toBlockchainInstant: "BlockchainInstantTypeDef" = None,
        sort: "ListTransactionsSortTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTransactionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtransactionspaginator)
        """
