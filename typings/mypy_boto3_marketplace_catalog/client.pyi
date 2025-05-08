"""
Type annotations for marketplace-catalog service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_catalog.client import MarketplaceCatalogClient

    session = Session()
    client: MarketplaceCatalogClient = session.client("marketplace-catalog")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListChangeSetsPaginator, ListEntitiesPaginator
from .type_defs import (
    BatchDescribeEntitiesRequestTypeDef,
    BatchDescribeEntitiesResponseTypeDef,
    CancelChangeSetRequestTypeDef,
    CancelChangeSetResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DescribeChangeSetRequestTypeDef,
    DescribeChangeSetResponseTypeDef,
    DescribeEntityRequestTypeDef,
    DescribeEntityResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    ListChangeSetsRequestTypeDef,
    ListChangeSetsResponseTypeDef,
    ListEntitiesRequestTypeDef,
    ListEntitiesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    StartChangeSetRequestTypeDef,
    StartChangeSetResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("MarketplaceCatalogClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        MarketplaceCatalogClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog.html#MarketplaceCatalog.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#generate_presigned_url)
        """

    def batch_describe_entities(
        self, **kwargs: Unpack[BatchDescribeEntitiesRequestTypeDef]
    ) -> BatchDescribeEntitiesResponseTypeDef:
        """
        Returns metadata and content for multiple entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/batch_describe_entities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#batch_describe_entities)
        """

    def cancel_change_set(
        self, **kwargs: Unpack[CancelChangeSetRequestTypeDef]
    ) -> CancelChangeSetResponseTypeDef:
        """
        Used to cancel an open change request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/cancel_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#cancel_change_set)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a resource-based policy on an entity that is identified by its resource
        ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#delete_resource_policy)
        """

    def describe_change_set(
        self, **kwargs: Unpack[DescribeChangeSetRequestTypeDef]
    ) -> DescribeChangeSetResponseTypeDef:
        """
        Provides information about a given change set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/describe_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#describe_change_set)
        """

    def describe_entity(
        self, **kwargs: Unpack[DescribeEntityRequestTypeDef]
    ) -> DescribeEntityResponseTypeDef:
        """
        Returns the metadata and content of the entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/describe_entity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#describe_entity)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Gets a resource-based policy of an entity that is identified by its resource
        ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#get_resource_policy)
        """

    def list_change_sets(
        self, **kwargs: Unpack[ListChangeSetsRequestTypeDef]
    ) -> ListChangeSetsResponseTypeDef:
        """
        Returns the list of change sets owned by the account being used to make the
        call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/list_change_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#list_change_sets)
        """

    def list_entities(
        self, **kwargs: Unpack[ListEntitiesRequestTypeDef]
    ) -> ListEntitiesResponseTypeDef:
        """
        Provides the list of entities of a given type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/list_entities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#list_entities)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags that have been added to a resource (either an <a
        href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities">entity</a>
        or <a
        href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-chang...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#list_tags_for_resource)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Attaches a resource-based policy to an entity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#put_resource_policy)
        """

    def start_change_set(
        self, **kwargs: Unpack[StartChangeSetRequestTypeDef]
    ) -> StartChangeSetResponseTypeDef:
        """
        Allows you to request changes for your entities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/start_change_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#start_change_set)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags a resource (either an <a
        href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities">entity</a>
        or <a
        href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets">change
        set</a>).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes a tag or list of tags from a resource (either an <a
        href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#catalog-api-entities">entity</a>
        or <a
        href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-se...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#untag_resource)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_change_sets"]
    ) -> ListChangeSetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_entities"]
    ) -> ListEntitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/marketplace-catalog/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/client/#get_paginator)
        """
