"""
Type annotations for resource-explorer-2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_resource_explorer_2.client import ResourceExplorerClient

    session = Session()
    client: ResourceExplorerClient = session.client("resource-explorer-2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListIndexesForMembersPaginator,
    ListIndexesPaginator,
    ListManagedViewsPaginator,
    ListResourcesPaginator,
    ListSupportedResourceTypesPaginator,
    ListViewsPaginator,
    SearchPaginator,
)
from .type_defs import (
    AssociateDefaultViewInputTypeDef,
    AssociateDefaultViewOutputTypeDef,
    BatchGetViewInputTypeDef,
    BatchGetViewOutputTypeDef,
    CreateIndexInputTypeDef,
    CreateIndexOutputTypeDef,
    CreateViewInputTypeDef,
    CreateViewOutputTypeDef,
    DeleteIndexInputTypeDef,
    DeleteIndexOutputTypeDef,
    DeleteViewInputTypeDef,
    DeleteViewOutputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAccountLevelServiceConfigurationOutputTypeDef,
    GetDefaultViewOutputTypeDef,
    GetIndexOutputTypeDef,
    GetManagedViewInputTypeDef,
    GetManagedViewOutputTypeDef,
    GetViewInputTypeDef,
    GetViewOutputTypeDef,
    ListIndexesForMembersInputTypeDef,
    ListIndexesForMembersOutputTypeDef,
    ListIndexesInputTypeDef,
    ListIndexesOutputTypeDef,
    ListManagedViewsInputTypeDef,
    ListManagedViewsOutputTypeDef,
    ListResourcesInputTypeDef,
    ListResourcesOutputTypeDef,
    ListSupportedResourceTypesInputTypeDef,
    ListSupportedResourceTypesOutputTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListViewsInputTypeDef,
    ListViewsOutputTypeDef,
    SearchInputTypeDef,
    SearchOutputTypeDef,
    TagResourceInputTypeDef,
    UntagResourceInputTypeDef,
    UpdateIndexTypeInputTypeDef,
    UpdateIndexTypeOutputTypeDef,
    UpdateViewInputTypeDef,
    UpdateViewOutputTypeDef,
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

__all__ = ("ResourceExplorerClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ResourceExplorerClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ResourceExplorerClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2.html#ResourceExplorer.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#generate_presigned_url)
        """

    def associate_default_view(
        self, **kwargs: Unpack[AssociateDefaultViewInputTypeDef]
    ) -> AssociateDefaultViewOutputTypeDef:
        """
        Sets the specified view as the default for the Amazon Web Services Region in
        which you call this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/associate_default_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#associate_default_view)
        """

    def batch_get_view(
        self, **kwargs: Unpack[BatchGetViewInputTypeDef]
    ) -> BatchGetViewOutputTypeDef:
        """
        Retrieves details about a list of views.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/batch_get_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#batch_get_view)
        """

    def create_index(self, **kwargs: Unpack[CreateIndexInputTypeDef]) -> CreateIndexOutputTypeDef:
        """
        Turns on Amazon Web Services Resource Explorer in the Amazon Web Services
        Region in which you called this operation by creating an index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/create_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#create_index)
        """

    def create_view(self, **kwargs: Unpack[CreateViewInputTypeDef]) -> CreateViewOutputTypeDef:
        """
        Creates a view that users can query by using the <a>Search</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/create_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#create_view)
        """

    def delete_index(self, **kwargs: Unpack[DeleteIndexInputTypeDef]) -> DeleteIndexOutputTypeDef:
        """
        Deletes the specified index and turns off Amazon Web Services Resource Explorer
        in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/delete_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#delete_index)
        """

    def delete_view(self, **kwargs: Unpack[DeleteViewInputTypeDef]) -> DeleteViewOutputTypeDef:
        """
        Deletes the specified view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/delete_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#delete_view)
        """

    def disassociate_default_view(self) -> EmptyResponseMetadataTypeDef:
        """
        After you call this operation, the affected Amazon Web Services Region no
        longer has a default view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/disassociate_default_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#disassociate_default_view)
        """

    def get_account_level_service_configuration(
        self,
    ) -> GetAccountLevelServiceConfigurationOutputTypeDef:
        """
        Retrieves the status of your account's Amazon Web Services service access, and
        validates the service linked role required to access the multi-account search
        feature.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_account_level_service_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_account_level_service_configuration)
        """

    def get_default_view(self) -> GetDefaultViewOutputTypeDef:
        """
        Retrieves the Amazon Resource Name (ARN) of the view that is the default for
        the Amazon Web Services Region in which you call this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_default_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_default_view)
        """

    def get_index(self) -> GetIndexOutputTypeDef:
        """
        Retrieves details about the Amazon Web Services Resource Explorer index in the
        Amazon Web Services Region in which you invoked the operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_index.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_index)
        """

    def get_managed_view(
        self, **kwargs: Unpack[GetManagedViewInputTypeDef]
    ) -> GetManagedViewOutputTypeDef:
        """
        Retrieves details of the specified <a
        href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html">Amazon
        Web Services-managed view</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_managed_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_managed_view)
        """

    def get_view(self, **kwargs: Unpack[GetViewInputTypeDef]) -> GetViewOutputTypeDef:
        """
        Retrieves details of the specified view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_view)
        """

    def list_indexes(self, **kwargs: Unpack[ListIndexesInputTypeDef]) -> ListIndexesOutputTypeDef:
        """
        Retrieves a list of all of the indexes in Amazon Web Services Regions that are
        currently collecting resource information for Amazon Web Services Resource
        Explorer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/list_indexes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_indexes)
        """

    def list_indexes_for_members(
        self, **kwargs: Unpack[ListIndexesForMembersInputTypeDef]
    ) -> ListIndexesForMembersOutputTypeDef:
        """
        Retrieves a list of a member's indexes in all Amazon Web Services Regions that
        are currently collecting resource information for Amazon Web Services Resource
        Explorer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/list_indexes_for_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_indexes_for_members)
        """

    def list_managed_views(
        self, **kwargs: Unpack[ListManagedViewsInputTypeDef]
    ) -> ListManagedViewsOutputTypeDef:
        """
        Lists the Amazon resource names (ARNs) of the <a
        href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html">Amazon
        Web Services-managed views</a> available in the Amazon Web Services Region in
        which you call this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/list_managed_views.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_managed_views)
        """

    def list_resources(
        self, **kwargs: Unpack[ListResourcesInputTypeDef]
    ) -> ListResourcesOutputTypeDef:
        """
        Returns a list of resources and their details that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/list_resources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_resources)
        """

    def list_supported_resource_types(
        self, **kwargs: Unpack[ListSupportedResourceTypesInputTypeDef]
    ) -> ListSupportedResourceTypesOutputTypeDef:
        """
        Retrieves a list of all resource types currently supported by Amazon Web
        Services Resource Explorer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/list_supported_resource_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_supported_resource_types)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceOutputTypeDef:
        """
        Lists the tags that are attached to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_tags_for_resource)
        """

    def list_views(self, **kwargs: Unpack[ListViewsInputTypeDef]) -> ListViewsOutputTypeDef:
        """
        Lists the <a
        href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon
        resource names (ARNs)</a> of the views available in the Amazon Web Services
        Region in which you call this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/list_views.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#list_views)
        """

    def search(self, **kwargs: Unpack[SearchInputTypeDef]) -> SearchOutputTypeDef:
        """
        Searches for resources and displays details about all resources that match the
        specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/search.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#search)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Adds one or more tag key and value pairs to an Amazon Web Services Resource
        Explorer view or index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tag key and value pairs from an Amazon Web Services
        Resource Explorer view or index.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#untag_resource)
        """

    def update_index_type(
        self, **kwargs: Unpack[UpdateIndexTypeInputTypeDef]
    ) -> UpdateIndexTypeOutputTypeDef:
        """
        Changes the type of the index from one of the following types to the other.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/update_index_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#update_index_type)
        """

    def update_view(self, **kwargs: Unpack[UpdateViewInputTypeDef]) -> UpdateViewOutputTypeDef:
        """
        Modifies some of the details of a view.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/update_view.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#update_view)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_indexes_for_members"]
    ) -> ListIndexesForMembersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_indexes"]
    ) -> ListIndexesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_managed_views"]
    ) -> ListManagedViewsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resources"]
    ) -> ListResourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_supported_resource_types"]
    ) -> ListSupportedResourceTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_views"]
    ) -> ListViewsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search"]
    ) -> SearchPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/resource-explorer-2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/client/#get_paginator)
        """
