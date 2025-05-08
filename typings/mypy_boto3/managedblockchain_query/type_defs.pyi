"""
Type annotations for managedblockchain-query service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_managedblockchain_query.type_defs import AddressIdentifierFilterTypeDef

    data: AddressIdentifierFilterTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ConfirmationStatusType,
    ErrorTypeType,
    ExecutionStatusType,
    QueryNetworkType,
    QueryTokenStandardType,
    QueryTransactionEventTypeType,
    SortOrderType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AddressIdentifierFilterTypeDef",
    "AssetContractTypeDef",
    "BatchGetTokenBalanceErrorItemTypeDef",
    "BatchGetTokenBalanceInputItemTypeDef",
    "BatchGetTokenBalanceInputTypeDef",
    "BatchGetTokenBalanceOutputItemTypeDef",
    "BatchGetTokenBalanceOutputTypeDef",
    "BlockchainInstantOutputTypeDef",
    "BlockchainInstantTypeDef",
    "BlockchainInstantUnionTypeDef",
    "ConfirmationStatusFilterTypeDef",
    "ContractFilterTypeDef",
    "ContractIdentifierTypeDef",
    "ContractMetadataTypeDef",
    "GetAssetContractInputTypeDef",
    "GetAssetContractOutputTypeDef",
    "GetTokenBalanceInputTypeDef",
    "GetTokenBalanceOutputTypeDef",
    "GetTransactionInputTypeDef",
    "GetTransactionOutputTypeDef",
    "ListAssetContractsInputPaginateTypeDef",
    "ListAssetContractsInputTypeDef",
    "ListAssetContractsOutputTypeDef",
    "ListFilteredTransactionEventsInputPaginateTypeDef",
    "ListFilteredTransactionEventsInputTypeDef",
    "ListFilteredTransactionEventsOutputTypeDef",
    "ListFilteredTransactionEventsSortTypeDef",
    "ListTokenBalancesInputPaginateTypeDef",
    "ListTokenBalancesInputTypeDef",
    "ListTokenBalancesOutputTypeDef",
    "ListTransactionEventsInputPaginateTypeDef",
    "ListTransactionEventsInputTypeDef",
    "ListTransactionEventsOutputTypeDef",
    "ListTransactionsInputPaginateTypeDef",
    "ListTransactionsInputTypeDef",
    "ListTransactionsOutputTypeDef",
    "ListTransactionsSortTypeDef",
    "OwnerFilterTypeDef",
    "OwnerIdentifierTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TimeFilterTypeDef",
    "TimestampTypeDef",
    "TokenBalanceTypeDef",
    "TokenFilterTypeDef",
    "TokenIdentifierTypeDef",
    "TransactionEventTypeDef",
    "TransactionOutputItemTypeDef",
    "TransactionTypeDef",
    "VoutFilterTypeDef",
)

class AddressIdentifierFilterTypeDef(TypedDict):
    transactionEventToAddress: Sequence[str]

class ContractIdentifierTypeDef(TypedDict):
    network: QueryNetworkType
    contractAddress: str

class BlockchainInstantOutputTypeDef(TypedDict):
    time: NotRequired[datetime]

class OwnerIdentifierTypeDef(TypedDict):
    address: str

class TokenIdentifierTypeDef(TypedDict):
    network: QueryNetworkType
    contractAddress: NotRequired[str]
    tokenId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class ConfirmationStatusFilterTypeDef(TypedDict):
    include: Sequence[ConfirmationStatusType]

class ContractFilterTypeDef(TypedDict):
    network: QueryNetworkType
    tokenStandard: QueryTokenStandardType
    deployerAddress: str

class ContractMetadataTypeDef(TypedDict):
    name: NotRequired[str]
    symbol: NotRequired[str]
    decimals: NotRequired[int]

class GetTransactionInputTypeDef(TypedDict):
    network: QueryNetworkType
    transactionHash: NotRequired[str]
    transactionId: NotRequired[str]

TransactionTypeDef = TypedDict(
    "TransactionTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "transactionTimestamp": datetime,
        "transactionIndex": int,
        "numberOfTransactions": int,
        "to": str,
        "blockHash": NotRequired[str],
        "blockNumber": NotRequired[str],
        "from": NotRequired[str],
        "contractAddress": NotRequired[str],
        "gasUsed": NotRequired[str],
        "cumulativeGasUsed": NotRequired[str],
        "effectiveGasPrice": NotRequired[str],
        "signatureV": NotRequired[int],
        "signatureR": NotRequired[str],
        "signatureS": NotRequired[str],
        "transactionFee": NotRequired[str],
        "transactionId": NotRequired[str],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
        "executionStatus": NotRequired[ExecutionStatusType],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListFilteredTransactionEventsSortTypeDef(TypedDict):
    sortBy: NotRequired[Literal["blockchainInstant"]]
    sortOrder: NotRequired[SortOrderType]

class VoutFilterTypeDef(TypedDict):
    voutSpent: bool

class OwnerFilterTypeDef(TypedDict):
    address: str

class TokenFilterTypeDef(TypedDict):
    network: QueryNetworkType
    contractAddress: NotRequired[str]
    tokenId: NotRequired[str]

class ListTransactionEventsInputTypeDef(TypedDict):
    network: QueryNetworkType
    transactionHash: NotRequired[str]
    transactionId: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTransactionsSortTypeDef(TypedDict):
    sortBy: NotRequired[Literal["TRANSACTION_TIMESTAMP"]]
    sortOrder: NotRequired[SortOrderType]

class TransactionOutputItemTypeDef(TypedDict):
    transactionHash: str
    network: QueryNetworkType
    transactionTimestamp: datetime
    transactionId: NotRequired[str]
    confirmationStatus: NotRequired[ConfirmationStatusType]

class AssetContractTypeDef(TypedDict):
    contractIdentifier: ContractIdentifierTypeDef
    tokenStandard: QueryTokenStandardType
    deployerAddress: str

class GetAssetContractInputTypeDef(TypedDict):
    contractIdentifier: ContractIdentifierTypeDef

TransactionEventTypeDef = TypedDict(
    "TransactionEventTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "eventType": QueryTransactionEventTypeType,
        "from": NotRequired[str],
        "to": NotRequired[str],
        "value": NotRequired[str],
        "contractAddress": NotRequired[str],
        "tokenId": NotRequired[str],
        "transactionId": NotRequired[str],
        "voutIndex": NotRequired[int],
        "voutSpent": NotRequired[bool],
        "spentVoutTransactionId": NotRequired[str],
        "spentVoutTransactionHash": NotRequired[str],
        "spentVoutIndex": NotRequired[int],
        "blockchainInstant": NotRequired[BlockchainInstantOutputTypeDef],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
    },
)

class BatchGetTokenBalanceErrorItemTypeDef(TypedDict):
    errorCode: str
    errorMessage: str
    errorType: ErrorTypeType
    tokenIdentifier: NotRequired[TokenIdentifierTypeDef]
    ownerIdentifier: NotRequired[OwnerIdentifierTypeDef]
    atBlockchainInstant: NotRequired[BlockchainInstantOutputTypeDef]

class BatchGetTokenBalanceOutputItemTypeDef(TypedDict):
    balance: str
    atBlockchainInstant: BlockchainInstantOutputTypeDef
    ownerIdentifier: NotRequired[OwnerIdentifierTypeDef]
    tokenIdentifier: NotRequired[TokenIdentifierTypeDef]
    lastUpdatedTime: NotRequired[BlockchainInstantOutputTypeDef]

class TokenBalanceTypeDef(TypedDict):
    balance: str
    atBlockchainInstant: BlockchainInstantOutputTypeDef
    ownerIdentifier: NotRequired[OwnerIdentifierTypeDef]
    tokenIdentifier: NotRequired[TokenIdentifierTypeDef]
    lastUpdatedTime: NotRequired[BlockchainInstantOutputTypeDef]

class GetTokenBalanceOutputTypeDef(TypedDict):
    ownerIdentifier: OwnerIdentifierTypeDef
    tokenIdentifier: TokenIdentifierTypeDef
    balance: str
    atBlockchainInstant: BlockchainInstantOutputTypeDef
    lastUpdatedTime: BlockchainInstantOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BlockchainInstantTypeDef(TypedDict):
    time: NotRequired[TimestampTypeDef]

class ListAssetContractsInputTypeDef(TypedDict):
    contractFilter: ContractFilterTypeDef
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class GetAssetContractOutputTypeDef(TypedDict):
    contractIdentifier: ContractIdentifierTypeDef
    tokenStandard: QueryTokenStandardType
    deployerAddress: str
    metadata: ContractMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransactionOutputTypeDef(TypedDict):
    transaction: TransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetContractsInputPaginateTypeDef(TypedDict):
    contractFilter: ContractFilterTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTransactionEventsInputPaginateTypeDef(TypedDict):
    network: QueryNetworkType
    transactionHash: NotRequired[str]
    transactionId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTokenBalancesInputPaginateTypeDef(TypedDict):
    tokenFilter: TokenFilterTypeDef
    ownerFilter: NotRequired[OwnerFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTokenBalancesInputTypeDef(TypedDict):
    tokenFilter: TokenFilterTypeDef
    ownerFilter: NotRequired[OwnerFilterTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTransactionsOutputTypeDef(TypedDict):
    transactions: List[TransactionOutputItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAssetContractsOutputTypeDef(TypedDict):
    contracts: List[AssetContractTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFilteredTransactionEventsOutputTypeDef(TypedDict):
    events: List[TransactionEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTransactionEventsOutputTypeDef(TypedDict):
    events: List[TransactionEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchGetTokenBalanceOutputTypeDef(TypedDict):
    tokenBalances: List[BatchGetTokenBalanceOutputItemTypeDef]
    errors: List[BatchGetTokenBalanceErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTokenBalancesOutputTypeDef(TypedDict):
    tokenBalances: List[TokenBalanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

BlockchainInstantUnionTypeDef = Union[BlockchainInstantTypeDef, BlockchainInstantOutputTypeDef]

class BatchGetTokenBalanceInputItemTypeDef(TypedDict):
    tokenIdentifier: TokenIdentifierTypeDef
    ownerIdentifier: OwnerIdentifierTypeDef
    atBlockchainInstant: NotRequired[BlockchainInstantUnionTypeDef]

class GetTokenBalanceInputTypeDef(TypedDict):
    tokenIdentifier: TokenIdentifierTypeDef
    ownerIdentifier: OwnerIdentifierTypeDef
    atBlockchainInstant: NotRequired[BlockchainInstantUnionTypeDef]

class ListTransactionsInputPaginateTypeDef(TypedDict):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: NotRequired[BlockchainInstantUnionTypeDef]
    toBlockchainInstant: NotRequired[BlockchainInstantUnionTypeDef]
    sort: NotRequired[ListTransactionsSortTypeDef]
    confirmationStatusFilter: NotRequired[ConfirmationStatusFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTransactionsInputTypeDef(TypedDict):
    address: str
    network: QueryNetworkType
    fromBlockchainInstant: NotRequired[BlockchainInstantUnionTypeDef]
    toBlockchainInstant: NotRequired[BlockchainInstantUnionTypeDef]
    sort: NotRequired[ListTransactionsSortTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    confirmationStatusFilter: NotRequired[ConfirmationStatusFilterTypeDef]

TimeFilterTypeDef = TypedDict(
    "TimeFilterTypeDef",
    {
        "from": NotRequired[BlockchainInstantUnionTypeDef],
        "to": NotRequired[BlockchainInstantUnionTypeDef],
    },
)

class BatchGetTokenBalanceInputTypeDef(TypedDict):
    getTokenBalanceInputs: NotRequired[Sequence[BatchGetTokenBalanceInputItemTypeDef]]

class ListFilteredTransactionEventsInputPaginateTypeDef(TypedDict):
    network: str
    addressIdentifierFilter: AddressIdentifierFilterTypeDef
    timeFilter: NotRequired[TimeFilterTypeDef]
    voutFilter: NotRequired[VoutFilterTypeDef]
    confirmationStatusFilter: NotRequired[ConfirmationStatusFilterTypeDef]
    sort: NotRequired[ListFilteredTransactionEventsSortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFilteredTransactionEventsInputTypeDef(TypedDict):
    network: str
    addressIdentifierFilter: AddressIdentifierFilterTypeDef
    timeFilter: NotRequired[TimeFilterTypeDef]
    voutFilter: NotRequired[VoutFilterTypeDef]
    confirmationStatusFilter: NotRequired[ConfirmationStatusFilterTypeDef]
    sort: NotRequired[ListFilteredTransactionEventsSortTypeDef]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
