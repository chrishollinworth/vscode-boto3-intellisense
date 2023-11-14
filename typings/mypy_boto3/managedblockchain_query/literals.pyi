"""
Type annotations for managedblockchain-query service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/literals.html)

Usage::

    ```python
    from mypy_boto3_managedblockchain_query.literals import ErrorTypeType

    data: ErrorTypeType = "RESOURCE_NOT_FOUND_EXCEPTION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ErrorTypeType",
    "ListAssetContractsPaginatorName",
    "ListTokenBalancesPaginatorName",
    "ListTransactionEventsPaginatorName",
    "ListTransactionsPaginatorName",
    "ListTransactionsSortByType",
    "QueryNetworkType",
    "QueryTokenStandardType",
    "QueryTransactionEventTypeType",
    "QueryTransactionStatusType",
    "SortOrderType",
)

ErrorTypeType = Literal["RESOURCE_NOT_FOUND_EXCEPTION", "VALIDATION_EXCEPTION"]
ListAssetContractsPaginatorName = Literal["list_asset_contracts"]
ListTokenBalancesPaginatorName = Literal["list_token_balances"]
ListTransactionEventsPaginatorName = Literal["list_transaction_events"]
ListTransactionsPaginatorName = Literal["list_transactions"]
ListTransactionsSortByType = Literal["TRANSACTION_TIMESTAMP"]
QueryNetworkType = Literal[
    "BITCOIN_MAINNET", "BITCOIN_TESTNET", "ETHEREUM_MAINNET", "ETHEREUM_SEPOLIA_TESTNET"
]
QueryTokenStandardType = Literal["ERC1155", "ERC20", "ERC721"]
QueryTransactionEventTypeType = Literal[
    "BITCOIN_VIN",
    "BITCOIN_VOUT",
    "ERC1155_TRANSFER",
    "ERC20_BURN",
    "ERC20_DEPOSIT",
    "ERC20_MINT",
    "ERC20_TRANSFER",
    "ERC20_WITHDRAWAL",
    "ERC721_TRANSFER",
    "ETH_TRANSFER",
    "INTERNAL_ETH_TRANSFER",
]
QueryTransactionStatusType = Literal["FAILED", "FINAL"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
