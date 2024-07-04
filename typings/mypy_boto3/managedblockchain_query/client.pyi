"""
Type annotations for managedblockchain-query service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_managedblockchain_query import ManagedBlockchainQueryClient

    client: ManagedBlockchainQueryClient = boto3.client("managedblockchain-query")
    ```
"""

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import QueryNetworkType
from .paginator import (
    ListAssetContractsPaginator,
    ListFilteredTransactionEventsPaginator,
    ListTokenBalancesPaginator,
    ListTransactionEventsPaginator,
    ListTransactionsPaginator,
)
from .type_defs import (
    AddressIdentifierFilterTypeDef,
    BatchGetTokenBalanceInputItemTypeDef,
    BatchGetTokenBalanceOutputTypeDef,
    BlockchainInstantTypeDef,
    ConfirmationStatusFilterTypeDef,
    ContractFilterTypeDef,
    ContractIdentifierTypeDef,
    GetAssetContractOutputTypeDef,
    GetTokenBalanceOutputTypeDef,
    GetTransactionOutputTypeDef,
    ListAssetContractsOutputTypeDef,
    ListFilteredTransactionEventsOutputTypeDef,
    ListFilteredTransactionEventsSortTypeDef,
    ListTokenBalancesOutputTypeDef,
    ListTransactionEventsOutputTypeDef,
    ListTransactionsOutputTypeDef,
    ListTransactionsSortTypeDef,
    OwnerFilterTypeDef,
    OwnerIdentifierTypeDef,
    TimeFilterTypeDef,
    TokenFilterTypeDef,
    TokenIdentifierTypeDef,
    VoutFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ManagedBlockchainQueryClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ManagedBlockchainQueryClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ManagedBlockchainQueryClient exceptions.
        """

    def batch_get_token_balance(
        self, *, getTokenBalanceInputs: List["BatchGetTokenBalanceInputItemTypeDef"] = None
    ) -> BatchGetTokenBalanceOutputTypeDef:
        """
        Gets the token balance for a batch of tokens by using the `BatchGetTokenBalance`
        action for every token in the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.batch_get_token_balance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#batch_get_token_balance)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#close)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#generate_presigned_url)
        """

    def get_asset_contract(
        self, *, contractIdentifier: "ContractIdentifierTypeDef"
    ) -> GetAssetContractOutputTypeDef:
        """
        Gets the information about a specific contract deployed on the blockchain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_asset_contract)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#get_asset_contract)
        """

    def get_token_balance(
        self,
        *,
        tokenIdentifier: "TokenIdentifierTypeDef",
        ownerIdentifier: "OwnerIdentifierTypeDef",
        atBlockchainInstant: "BlockchainInstantTypeDef" = None
    ) -> GetTokenBalanceOutputTypeDef:
        """
        Gets the balance of a specific token, including native tokens, for a given
        address (wallet or contract) on the blockchain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_token_balance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#get_token_balance)
        """

    def get_transaction(
        self, *, network: QueryNetworkType, transactionHash: str = None, transactionId: str = None
    ) -> GetTransactionOutputTypeDef:
        """
        Gets the details of a transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.get_transaction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#get_transaction)
        """

    def list_asset_contracts(
        self,
        *,
        contractFilter: "ContractFilterTypeDef",
        nextToken: str = None,
        maxResults: int = None
    ) -> ListAssetContractsOutputTypeDef:
        """
        Lists all the contracts for a given contract type deployed by an address (either
        a contract address or a wallet address).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_asset_contracts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#list_asset_contracts)
        """

    def list_filtered_transaction_events(
        self,
        *,
        network: str,
        addressIdentifierFilter: "AddressIdentifierFilterTypeDef",
        timeFilter: "TimeFilterTypeDef" = None,
        voutFilter: "VoutFilterTypeDef" = None,
        confirmationStatusFilter: "ConfirmationStatusFilterTypeDef" = None,
        sort: "ListFilteredTransactionEventsSortTypeDef" = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListFilteredTransactionEventsOutputTypeDef:
        """
        Lists all the transaction events for an address on the blockchain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_filtered_transaction_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#list_filtered_transaction_events)
        """

    def list_token_balances(
        self,
        *,
        tokenFilter: "TokenFilterTypeDef",
        ownerFilter: "OwnerFilterTypeDef" = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTokenBalancesOutputTypeDef:
        """
        This action returns the following for a given blockchain network * Lists all
        token balances owned by an address (either a contract address or a wallet
        address).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_token_balances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#list_token_balances)
        """

    def list_transaction_events(
        self,
        *,
        network: QueryNetworkType,
        transactionHash: str = None,
        transactionId: str = None,
        nextToken: str = None,
        maxResults: int = None
    ) -> ListTransactionEventsOutputTypeDef:
        """
        Lists all the transaction events for a transaction .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_transaction_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#list_transaction_events)
        """

    def list_transactions(
        self,
        *,
        address: str,
        network: QueryNetworkType,
        fromBlockchainInstant: "BlockchainInstantTypeDef" = None,
        toBlockchainInstant: "BlockchainInstantTypeDef" = None,
        sort: "ListTransactionsSortTypeDef" = None,
        nextToken: str = None,
        maxResults: int = None,
        confirmationStatusFilter: "ConfirmationStatusFilterTypeDef" = None
    ) -> ListTransactionsOutputTypeDef:
        """
        Lists all the transaction events for a transaction.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Client.list_transactions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/client.html#list_transactions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_asset_contracts"]
    ) -> ListAssetContractsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListAssetContracts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listassetcontractspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_filtered_transaction_events"]
    ) -> ListFilteredTransactionEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListFilteredTransactionEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listfilteredtransactioneventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_token_balances"]
    ) -> ListTokenBalancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTokenBalances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtokenbalancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transaction_events"]
    ) -> ListTransactionEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactionEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtransactioneventspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transactions"]
    ) -> ListTransactionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/managedblockchain-query.html#ManagedBlockchainQuery.Paginator.ListTransactions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain_query/paginators.html#listtransactionspaginator)
        """
