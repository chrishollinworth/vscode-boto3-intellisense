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

import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import IntentType, OwnershipTypeType
from .paginator import ListChangeSetsPaginator, ListEntitiesPaginator
from .type_defs import (
    BatchDescribeEntitiesResponseTypeDef,
    CancelChangeSetResponseTypeDef,
    ChangeTypeDef,
    DescribeChangeSetResponseTypeDef,
    DescribeEntityResponseTypeDef,
    EntityRequestTypeDef,
    EntityTypeFiltersTypeDef,
    EntityTypeSortTypeDef,
    FilterTypeDef,
    GetResourcePolicyResponseTypeDef,
    ListChangeSetsResponseTypeDef,
    ListEntitiesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SortTypeDef,
    StartChangeSetResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceCatalogClient exceptions.
        """

    def batch_describe_entities(
        self, *, EntityRequestList: List["EntityRequestTypeDef"]
    ) -> BatchDescribeEntitiesResponseTypeDef:
        """
        Returns metadata and content for multiple entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.batch_describe_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#batch_describe_entities)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#can_paginate)
        """

    def cancel_change_set(
        self, *, Catalog: str, ChangeSetId: str
    ) -> CancelChangeSetResponseTypeDef:
        """
        Used to cancel an open change request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.cancel_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#cancel_change_set)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#close)
        """

    def delete_resource_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Deletes a resource-based policy on an entity that is identified by its resource
        ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#delete_resource_policy)
        """

    def describe_change_set(
        self, *, Catalog: str, ChangeSetId: str
    ) -> DescribeChangeSetResponseTypeDef:
        """
        Provides information about a given change set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#describe_change_set)
        """

    def describe_entity(self, *, Catalog: str, EntityId: str) -> DescribeEntityResponseTypeDef:
        """
        Returns the metadata and content of the entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.describe_entity)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#generate_presigned_url)
        """

    def get_resource_policy(self, *, ResourceArn: str) -> GetResourcePolicyResponseTypeDef:
        """
        Gets a resource-based policy of an entity that is identified by its resource
        ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#get_resource_policy)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_change_sets)
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
        MaxResults: int = None,
        OwnershipType: OwnershipTypeType = None,
        EntityTypeFilters: "EntityTypeFiltersTypeDef" = None,
        EntityTypeSort: "EntityTypeSortTypeDef" = None
    ) -> ListEntitiesResponseTypeDef:
        """
        Provides the list of entities of a given type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_entities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#list_entities)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags that have been added to a resource (either an `entity
        <https://docs.aws.amazon.com/marketplace-catalog/latest/api-
        reference/welcome.html#catalog-api-entities>`__ or `change set
        <https://docs.aws.amazon.com/marketplace-catalog/latest/api-
        reference/welcome.html#working-with-change-se...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#list_tags_for_resource)
        """

    def put_resource_policy(self, *, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        Attaches a resource-based policy to an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#put_resource_policy)
        """

    def start_change_set(
        self,
        *,
        Catalog: str,
        ChangeSet: List["ChangeTypeDef"],
        ChangeSetName: str = None,
        ClientRequestToken: str = None,
        ChangeSetTags: List["TagTypeDef"] = None,
        Intent: IntentType = None
    ) -> StartChangeSetResponseTypeDef:
        """
        Allows you to request changes for your entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.start_change_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#start_change_set)
        """

    def tag_resource(self, *, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Tags a resource (either an `entity <https://docs.aws.amazon.com/marketplace-
        catalog/latest/api-reference/welcome.html#catalog-api-entities>`__ or `change
        set <https://docs.aws.amazon.com/marketplace-catalog/latest/api-
        reference/welcome.html#working-with-change-sets>`__).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes a tag or list of tags from a resource (either an `entity
        <https://docs.aws.amazon.com/marketplace-catalog/latest/api-
        reference/welcome.html#catalog-api-entities>`__ or `change set
        <https://docs.aws.amazon.com/marketplace-catalog/latest/api-
        reference/welcome.html#working-with-change-sets>`...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client.html#untag_resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_change_sets"]) -> ListChangeSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListChangeSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators.html#listchangesetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_entities"]) -> ListEntitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/marketplace-catalog.html#MarketplaceCatalog.Paginator.ListEntities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/paginators.html#listentitiespaginator)
        """
