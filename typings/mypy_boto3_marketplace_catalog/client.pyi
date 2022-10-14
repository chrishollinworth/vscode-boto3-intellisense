"""
Type annotations for marketplace-catalog service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_catalog import MarketplaceCatalogClient

    client: MarketplaceCatalogClient = boto3.client("marketplace-catalog")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CancelChangeSetResponseTypeDef,
    ChangeTypeDef,
    DescribeChangeSetResponseTypeDef,
    DescribeEntityResponseTypeDef,
    FilterTypeDef,
    ListChangeSetsResponseTypeDef,
    ListEntitiesResponseTypeDef,
    SortTypeDef,
    StartChangeSetResponseTypeDef,
)

__all__ = ("MarketplaceCatalogClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServiceException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceNotSupportedException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class MarketplaceCatalogClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceCatalogClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#can_paginate)
        """
    def cancel_change_set(
        self, *, Catalog: str, ChangeSetId: str
    ) -> CancelChangeSetResponseTypeDef:
        """
        Used to cancel an open change request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.cancel_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#cancel_change_set)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#close)
        """
    def describe_change_set(
        self, *, Catalog: str, ChangeSetId: str
    ) -> DescribeChangeSetResponseTypeDef:
        """
        Provides information about a given change set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#describe_change_set)
        """
    def describe_entity(self, *, Catalog: str, EntityId: str) -> DescribeEntityResponseTypeDef:
        """
        Returns the metadata and content of the entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_entity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#describe_entity)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#generate_presigned_url)
        """
    def list_change_sets(
        self,
        *,
        Catalog: str,
        FilterList: List["FilterTypeDef"] = None,
        Sort: "SortTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListChangeSetsResponseTypeDef:
        """
        Returns the list of change sets owned by the account being used to make the
        call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_change_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#list_change_sets)
        """
    def list_entities(
        self,
        *,
        Catalog: str,
        EntityType: str,
        FilterList: List["FilterTypeDef"] = None,
        Sort: "SortTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListEntitiesResponseTypeDef:
        """
        Provides the list of entities of a given type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#list_entities)
        """
    def start_change_set(
        self,
        *,
        Catalog: str,
        ChangeSet: List["ChangeTypeDef"],
        ChangeSetName: str = None,
        ClientRequestToken: str = None
    ) -> StartChangeSetResponseTypeDef:
        """
        This operation allows you to request changes for your entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.start_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#start_change_set)
        """
