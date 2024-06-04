"""
Type annotations for managedblockchain-query service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/type_defs.html)

Usage::

    ```python
    from mypy_boto3_managedblockchain_query.type_defs import AddressIdentifierFilterTypeDef

    data: AddressIdentifierFilterTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ConfirmationStatusType,
    ErrorTypeType,
    ExecutionStatusType,
    QueryNetworkType,
    QueryTokenStandardType,
    QueryTransactionEventTypeType,
    SortOrderType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddressIdentifierFilterTypeDef",
    "AssetContractTypeDef",
    "BatchGetTokenBalanceErrorItemTypeDef",
    "BatchGetTokenBalanceInputItemTypeDef",
    "BatchGetTokenBalanceInputRequestTypeDef",
    "BatchGetTokenBalanceOutputItemTypeDef",
    "BatchGetTokenBalanceOutputTypeDef",
    "BlockchainInstantTypeDef",
    "ConfirmationStatusFilterTypeDef",
    "ContractFilterTypeDef",
    "ContractIdentifierTypeDef",
    "ContractMetadataTypeDef",
    "GetAssetContractInputRequestTypeDef",
    "GetAssetContractOutputTypeDef",
    "GetTokenBalanceInputRequestTypeDef",
    "GetTokenBalanceOutputTypeDef",
    "GetTransactionInputRequestTypeDef",
    "GetTransactionOutputTypeDef",
    "ListAssetContractsInputRequestTypeDef",
    "ListAssetContractsOutputTypeDef",
    "ListFilteredTransactionEventsInputRequestTypeDef",
    "ListFilteredTransactionEventsOutputTypeDef",
    "ListFilteredTransactionEventsSortTypeDef",
    "ListTokenBalancesInputRequestTypeDef",
    "ListTokenBalancesOutputTypeDef",
    "ListTransactionEventsInputRequestTypeDef",
    "ListTransactionEventsOutputTypeDef",
    "ListTransactionsInputRequestTypeDef",
    "ListTransactionsOutputTypeDef",
    "ListTransactionsSortTypeDef",
    "OwnerFilterTypeDef",
    "OwnerIdentifierTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TimeFilterTypeDef",
    "TokenBalanceTypeDef",
    "TokenFilterTypeDef",
    "TokenIdentifierTypeDef",
    "TransactionEventTypeDef",
    "TransactionOutputItemTypeDef",
    "TransactionTypeDef",
    "VoutFilterTypeDef",
)

AddressIdentifierFilterTypeDef = TypedDict(
    "AddressIdentifierFilterTypeDef",
    {
        "transactionEventToAddress": List[str],
    },
)

AssetContractTypeDef = TypedDict(
    "AssetContractTypeDef",
    {
        "contractIdentifier": "ContractIdentifierTypeDef",
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
    },
)

_RequiredBatchGetTokenBalanceErrorItemTypeDef = TypedDict(
    "_RequiredBatchGetTokenBalanceErrorItemTypeDef",
    {
        "errorCode": str,
        "errorMessage": str,
        "errorType": ErrorTypeType,
    },
)
_OptionalBatchGetTokenBalanceErrorItemTypeDef = TypedDict(
    "_OptionalBatchGetTokenBalanceErrorItemTypeDef",
    {
        "tokenIdentifier": "TokenIdentifierTypeDef",
        "ownerIdentifier": "OwnerIdentifierTypeDef",
        "atBlockchainInstant": "BlockchainInstantTypeDef",
    },
    total=False,
)

class BatchGetTokenBalanceErrorItemTypeDef(
    _RequiredBatchGetTokenBalanceErrorItemTypeDef, _OptionalBatchGetTokenBalanceErrorItemTypeDef
):
    pass

_RequiredBatchGetTokenBalanceInputItemTypeDef = TypedDict(
    "_RequiredBatchGetTokenBalanceInputItemTypeDef",
    {
        "tokenIdentifier": "TokenIdentifierTypeDef",
        "ownerIdentifier": "OwnerIdentifierTypeDef",
    },
)
_OptionalBatchGetTokenBalanceInputItemTypeDef = TypedDict(
    "_OptionalBatchGetTokenBalanceInputItemTypeDef",
    {
        "atBlockchainInstant": "BlockchainInstantTypeDef",
    },
    total=False,
)

class BatchGetTokenBalanceInputItemTypeDef(
    _RequiredBatchGetTokenBalanceInputItemTypeDef, _OptionalBatchGetTokenBalanceInputItemTypeDef
):
    pass

BatchGetTokenBalanceInputRequestTypeDef = TypedDict(
    "BatchGetTokenBalanceInputRequestTypeDef",
    {
        "getTokenBalanceInputs": List["BatchGetTokenBalanceInputItemTypeDef"],
    },
    total=False,
)

_RequiredBatchGetTokenBalanceOutputItemTypeDef = TypedDict(
    "_RequiredBatchGetTokenBalanceOutputItemTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": "BlockchainInstantTypeDef",
    },
)
_OptionalBatchGetTokenBalanceOutputItemTypeDef = TypedDict(
    "_OptionalBatchGetTokenBalanceOutputItemTypeDef",
    {
        "ownerIdentifier": "OwnerIdentifierTypeDef",
        "tokenIdentifier": "TokenIdentifierTypeDef",
        "lastUpdatedTime": "BlockchainInstantTypeDef",
    },
    total=False,
)

class BatchGetTokenBalanceOutputItemTypeDef(
    _RequiredBatchGetTokenBalanceOutputItemTypeDef, _OptionalBatchGetTokenBalanceOutputItemTypeDef
):
    pass

BatchGetTokenBalanceOutputTypeDef = TypedDict(
    "BatchGetTokenBalanceOutputTypeDef",
    {
        "tokenBalances": List["BatchGetTokenBalanceOutputItemTypeDef"],
        "errors": List["BatchGetTokenBalanceErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlockchainInstantTypeDef = TypedDict(
    "BlockchainInstantTypeDef",
    {
        "time": Union[datetime, str],
    },
    total=False,
)

ConfirmationStatusFilterTypeDef = TypedDict(
    "ConfirmationStatusFilterTypeDef",
    {
        "include": List[ConfirmationStatusType],
    },
)

ContractFilterTypeDef = TypedDict(
    "ContractFilterTypeDef",
    {
        "network": QueryNetworkType,
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
    },
)

ContractIdentifierTypeDef = TypedDict(
    "ContractIdentifierTypeDef",
    {
        "network": QueryNetworkType,
        "contractAddress": str,
    },
)

ContractMetadataTypeDef = TypedDict(
    "ContractMetadataTypeDef",
    {
        "name": str,
        "symbol": str,
        "decimals": int,
    },
    total=False,
)

GetAssetContractInputRequestTypeDef = TypedDict(
    "GetAssetContractInputRequestTypeDef",
    {
        "contractIdentifier": "ContractIdentifierTypeDef",
    },
)

GetAssetContractOutputTypeDef = TypedDict(
    "GetAssetContractOutputTypeDef",
    {
        "contractIdentifier": "ContractIdentifierTypeDef",
        "tokenStandard": QueryTokenStandardType,
        "deployerAddress": str,
        "metadata": "ContractMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTokenBalanceInputRequestTypeDef = TypedDict(
    "_RequiredGetTokenBalanceInputRequestTypeDef",
    {
        "tokenIdentifier": "TokenIdentifierTypeDef",
        "ownerIdentifier": "OwnerIdentifierTypeDef",
    },
)
_OptionalGetTokenBalanceInputRequestTypeDef = TypedDict(
    "_OptionalGetTokenBalanceInputRequestTypeDef",
    {
        "atBlockchainInstant": "BlockchainInstantTypeDef",
    },
    total=False,
)

class GetTokenBalanceInputRequestTypeDef(
    _RequiredGetTokenBalanceInputRequestTypeDef, _OptionalGetTokenBalanceInputRequestTypeDef
):
    pass

GetTokenBalanceOutputTypeDef = TypedDict(
    "GetTokenBalanceOutputTypeDef",
    {
        "ownerIdentifier": "OwnerIdentifierTypeDef",
        "tokenIdentifier": "TokenIdentifierTypeDef",
        "balance": str,
        "atBlockchainInstant": "BlockchainInstantTypeDef",
        "lastUpdatedTime": "BlockchainInstantTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransactionInputRequestTypeDef = TypedDict(
    "_RequiredGetTransactionInputRequestTypeDef",
    {
        "network": QueryNetworkType,
    },
)
_OptionalGetTransactionInputRequestTypeDef = TypedDict(
    "_OptionalGetTransactionInputRequestTypeDef",
    {
        "transactionHash": str,
        "transactionId": str,
    },
    total=False,
)

class GetTransactionInputRequestTypeDef(
    _RequiredGetTransactionInputRequestTypeDef, _OptionalGetTransactionInputRequestTypeDef
):
    pass

GetTransactionOutputTypeDef = TypedDict(
    "GetTransactionOutputTypeDef",
    {
        "transaction": "TransactionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssetContractsInputRequestTypeDef = TypedDict(
    "_RequiredListAssetContractsInputRequestTypeDef",
    {
        "contractFilter": "ContractFilterTypeDef",
    },
)
_OptionalListAssetContractsInputRequestTypeDef = TypedDict(
    "_OptionalListAssetContractsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListAssetContractsInputRequestTypeDef(
    _RequiredListAssetContractsInputRequestTypeDef, _OptionalListAssetContractsInputRequestTypeDef
):
    pass

ListAssetContractsOutputTypeDef = TypedDict(
    "ListAssetContractsOutputTypeDef",
    {
        "contracts": List["AssetContractTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFilteredTransactionEventsInputRequestTypeDef = TypedDict(
    "_RequiredListFilteredTransactionEventsInputRequestTypeDef",
    {
        "network": str,
        "addressIdentifierFilter": "AddressIdentifierFilterTypeDef",
    },
)
_OptionalListFilteredTransactionEventsInputRequestTypeDef = TypedDict(
    "_OptionalListFilteredTransactionEventsInputRequestTypeDef",
    {
        "timeFilter": "TimeFilterTypeDef",
        "voutFilter": "VoutFilterTypeDef",
        "confirmationStatusFilter": "ConfirmationStatusFilterTypeDef",
        "sort": "ListFilteredTransactionEventsSortTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListFilteredTransactionEventsInputRequestTypeDef(
    _RequiredListFilteredTransactionEventsInputRequestTypeDef,
    _OptionalListFilteredTransactionEventsInputRequestTypeDef,
):
    pass

ListFilteredTransactionEventsOutputTypeDef = TypedDict(
    "ListFilteredTransactionEventsOutputTypeDef",
    {
        "events": List["TransactionEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFilteredTransactionEventsSortTypeDef = TypedDict(
    "ListFilteredTransactionEventsSortTypeDef",
    {
        "sortBy": Literal["blockchainInstant"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

_RequiredListTokenBalancesInputRequestTypeDef = TypedDict(
    "_RequiredListTokenBalancesInputRequestTypeDef",
    {
        "tokenFilter": "TokenFilterTypeDef",
    },
)
_OptionalListTokenBalancesInputRequestTypeDef = TypedDict(
    "_OptionalListTokenBalancesInputRequestTypeDef",
    {
        "ownerFilter": "OwnerFilterTypeDef",
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTokenBalancesInputRequestTypeDef(
    _RequiredListTokenBalancesInputRequestTypeDef, _OptionalListTokenBalancesInputRequestTypeDef
):
    pass

ListTokenBalancesOutputTypeDef = TypedDict(
    "ListTokenBalancesOutputTypeDef",
    {
        "tokenBalances": List["TokenBalanceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTransactionEventsInputRequestTypeDef = TypedDict(
    "_RequiredListTransactionEventsInputRequestTypeDef",
    {
        "network": QueryNetworkType,
    },
)
_OptionalListTransactionEventsInputRequestTypeDef = TypedDict(
    "_OptionalListTransactionEventsInputRequestTypeDef",
    {
        "transactionHash": str,
        "transactionId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListTransactionEventsInputRequestTypeDef(
    _RequiredListTransactionEventsInputRequestTypeDef,
    _OptionalListTransactionEventsInputRequestTypeDef,
):
    pass

ListTransactionEventsOutputTypeDef = TypedDict(
    "ListTransactionEventsOutputTypeDef",
    {
        "events": List["TransactionEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTransactionsInputRequestTypeDef = TypedDict(
    "_RequiredListTransactionsInputRequestTypeDef",
    {
        "address": str,
        "network": QueryNetworkType,
    },
)
_OptionalListTransactionsInputRequestTypeDef = TypedDict(
    "_OptionalListTransactionsInputRequestTypeDef",
    {
        "fromBlockchainInstant": "BlockchainInstantTypeDef",
        "toBlockchainInstant": "BlockchainInstantTypeDef",
        "sort": "ListTransactionsSortTypeDef",
        "nextToken": str,
        "maxResults": int,
        "confirmationStatusFilter": "ConfirmationStatusFilterTypeDef",
    },
    total=False,
)

class ListTransactionsInputRequestTypeDef(
    _RequiredListTransactionsInputRequestTypeDef, _OptionalListTransactionsInputRequestTypeDef
):
    pass

ListTransactionsOutputTypeDef = TypedDict(
    "ListTransactionsOutputTypeDef",
    {
        "transactions": List["TransactionOutputItemTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTransactionsSortTypeDef = TypedDict(
    "ListTransactionsSortTypeDef",
    {
        "sortBy": Literal["TRANSACTION_TIMESTAMP"],
        "sortOrder": SortOrderType,
    },
    total=False,
)

OwnerFilterTypeDef = TypedDict(
    "OwnerFilterTypeDef",
    {
        "address": str,
    },
)

OwnerIdentifierTypeDef = TypedDict(
    "OwnerIdentifierTypeDef",
    {
        "address": str,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

TimeFilterTypeDef = TypedDict(
    "TimeFilterTypeDef",
    {
        "from": "BlockchainInstantTypeDef",
        "to": "BlockchainInstantTypeDef",
    },
    total=False,
)

_RequiredTokenBalanceTypeDef = TypedDict(
    "_RequiredTokenBalanceTypeDef",
    {
        "balance": str,
        "atBlockchainInstant": "BlockchainInstantTypeDef",
    },
)
_OptionalTokenBalanceTypeDef = TypedDict(
    "_OptionalTokenBalanceTypeDef",
    {
        "ownerIdentifier": "OwnerIdentifierTypeDef",
        "tokenIdentifier": "TokenIdentifierTypeDef",
        "lastUpdatedTime": "BlockchainInstantTypeDef",
    },
    total=False,
)

class TokenBalanceTypeDef(_RequiredTokenBalanceTypeDef, _OptionalTokenBalanceTypeDef):
    pass

_RequiredTokenFilterTypeDef = TypedDict(
    "_RequiredTokenFilterTypeDef",
    {
        "network": QueryNetworkType,
    },
)
_OptionalTokenFilterTypeDef = TypedDict(
    "_OptionalTokenFilterTypeDef",
    {
        "contractAddress": str,
        "tokenId": str,
    },
    total=False,
)

class TokenFilterTypeDef(_RequiredTokenFilterTypeDef, _OptionalTokenFilterTypeDef):
    pass

_RequiredTokenIdentifierTypeDef = TypedDict(
    "_RequiredTokenIdentifierTypeDef",
    {
        "network": QueryNetworkType,
    },
)
_OptionalTokenIdentifierTypeDef = TypedDict(
    "_OptionalTokenIdentifierTypeDef",
    {
        "contractAddress": str,
        "tokenId": str,
    },
    total=False,
)

class TokenIdentifierTypeDef(_RequiredTokenIdentifierTypeDef, _OptionalTokenIdentifierTypeDef):
    pass

_RequiredTransactionEventTypeDef = TypedDict(
    "_RequiredTransactionEventTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "eventType": QueryTransactionEventTypeType,
    },
)
_OptionalTransactionEventTypeDef = TypedDict(
    "_OptionalTransactionEventTypeDef",
    {
        "from": str,
        "to": str,
        "value": str,
        "contractAddress": str,
        "tokenId": str,
        "transactionId": str,
        "voutIndex": int,
        "voutSpent": bool,
        "spentVoutTransactionId": str,
        "spentVoutTransactionHash": str,
        "spentVoutIndex": int,
        "blockchainInstant": "BlockchainInstantTypeDef",
        "confirmationStatus": ConfirmationStatusType,
    },
    total=False,
)

class TransactionEventTypeDef(_RequiredTransactionEventTypeDef, _OptionalTransactionEventTypeDef):
    pass

_RequiredTransactionOutputItemTypeDef = TypedDict(
    "_RequiredTransactionOutputItemTypeDef",
    {
        "transactionHash": str,
        "network": QueryNetworkType,
        "transactionTimestamp": datetime,
    },
)
_OptionalTransactionOutputItemTypeDef = TypedDict(
    "_OptionalTransactionOutputItemTypeDef",
    {
        "transactionId": str,
        "confirmationStatus": ConfirmationStatusType,
    },
    total=False,
)

class TransactionOutputItemTypeDef(
    _RequiredTransactionOutputItemTypeDef, _OptionalTransactionOutputItemTypeDef
):
    pass

_RequiredTransactionTypeDef = TypedDict(
    "_RequiredTransactionTypeDef",
    {
        "network": QueryNetworkType,
        "transactionHash": str,
        "transactionTimestamp": datetime,
        "transactionIndex": int,
        "numberOfTransactions": int,
        "to": str,
    },
)
_OptionalTransactionTypeDef = TypedDict(
    "_OptionalTransactionTypeDef",
    {
        "blockHash": str,
        "blockNumber": str,
        "from": str,
        "contractAddress": str,
        "gasUsed": str,
        "cumulativeGasUsed": str,
        "effectiveGasPrice": str,
        "signatureV": int,
        "signatureR": str,
        "signatureS": str,
        "transactionFee": str,
        "transactionId": str,
        "confirmationStatus": ConfirmationStatusType,
        "executionStatus": ExecutionStatusType,
    },
    total=False,
)

class TransactionTypeDef(_RequiredTransactionTypeDef, _OptionalTransactionTypeDef):
    pass

VoutFilterTypeDef = TypedDict(
    "VoutFilterTypeDef",
    {
        "voutSpent": bool,
    },
)
