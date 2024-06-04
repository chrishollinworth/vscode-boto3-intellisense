"""
Main interface for managedblockchain-query service.

Usage::

    ```python
    import boto3
    from mypy_boto3_managedblockchain_query import (
        Client,
        ListAssetContractsPaginator,
        ListFilteredTransactionEventsPaginator,
        ListTokenBalancesPaginator,
        ListTransactionEventsPaginator,
        ListTransactionsPaginator,
        ManagedBlockchainQueryClient,
    )

    session = boto3.Session()

    client: ManagedBlockchainQueryClient = boto3.client("managedblockchain-query")
    session_client: ManagedBlockchainQueryClient = session.client("managedblockchain-query")

    list_asset_contracts_paginator: ListAssetContractsPaginator = client.get_paginator("list_asset_contracts")
    list_filtered_transaction_events_paginator: ListFilteredTransactionEventsPaginator = client.get_paginator("list_filtered_transaction_events")
    list_token_balances_paginator: ListTokenBalancesPaginator = client.get_paginator("list_token_balances")
    list_transaction_events_paginator: ListTransactionEventsPaginator = client.get_paginator("list_transaction_events")
    list_transactions_paginator: ListTransactionsPaginator = client.get_paginator("list_transactions")
    ```
"""

from .client import ManagedBlockchainQueryClient
from .paginator import (
    ListAssetContractsPaginator,
    ListFilteredTransactionEventsPaginator,
    ListTokenBalancesPaginator,
    ListTransactionEventsPaginator,
    ListTransactionsPaginator,
)

Client = ManagedBlockchainQueryClient

__all__ = (
    "Client",
    "ListAssetContractsPaginator",
    "ListFilteredTransactionEventsPaginator",
    "ListTokenBalancesPaginator",
    "ListTransactionEventsPaginator",
    "ListTransactionsPaginator",
    "ManagedBlockchainQueryClient",
)
