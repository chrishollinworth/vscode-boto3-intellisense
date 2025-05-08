"""
Type annotations for appsync service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_appsync.client import AppSyncClient

    session = Session()
    client: AppSyncClient = session.client("appsync")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListApiKeysPaginator,
    ListApisPaginator,
    ListChannelNamespacesPaginator,
    ListDataSourcesPaginator,
    ListDomainNamesPaginator,
    ListFunctionsPaginator,
    ListGraphqlApisPaginator,
    ListResolversByFunctionPaginator,
    ListResolversPaginator,
    ListSourceApiAssociationsPaginator,
    ListTypesByAssociationPaginator,
    ListTypesPaginator,
)
from .type_defs import (
    AssociateApiRequestTypeDef,
    AssociateApiResponseTypeDef,
    AssociateMergedGraphqlApiRequestTypeDef,
    AssociateMergedGraphqlApiResponseTypeDef,
    AssociateSourceGraphqlApiRequestTypeDef,
    AssociateSourceGraphqlApiResponseTypeDef,
    CreateApiCacheRequestTypeDef,
    CreateApiCacheResponseTypeDef,
    CreateApiKeyRequestTypeDef,
    CreateApiKeyResponseTypeDef,
    CreateApiRequestTypeDef,
    CreateApiResponseTypeDef,
    CreateChannelNamespaceRequestTypeDef,
    CreateChannelNamespaceResponseTypeDef,
    CreateDataSourceRequestTypeDef,
    CreateDataSourceResponseTypeDef,
    CreateDomainNameRequestTypeDef,
    CreateDomainNameResponseTypeDef,
    CreateFunctionRequestTypeDef,
    CreateFunctionResponseTypeDef,
    CreateGraphqlApiRequestTypeDef,
    CreateGraphqlApiResponseTypeDef,
    CreateResolverRequestTypeDef,
    CreateResolverResponseTypeDef,
    CreateTypeRequestTypeDef,
    CreateTypeResponseTypeDef,
    DeleteApiCacheRequestTypeDef,
    DeleteApiKeyRequestTypeDef,
    DeleteApiRequestTypeDef,
    DeleteChannelNamespaceRequestTypeDef,
    DeleteDataSourceRequestTypeDef,
    DeleteDomainNameRequestTypeDef,
    DeleteFunctionRequestTypeDef,
    DeleteGraphqlApiRequestTypeDef,
    DeleteResolverRequestTypeDef,
    DeleteTypeRequestTypeDef,
    DisassociateApiRequestTypeDef,
    DisassociateMergedGraphqlApiRequestTypeDef,
    DisassociateMergedGraphqlApiResponseTypeDef,
    DisassociateSourceGraphqlApiRequestTypeDef,
    DisassociateSourceGraphqlApiResponseTypeDef,
    EvaluateCodeRequestTypeDef,
    EvaluateCodeResponseTypeDef,
    EvaluateMappingTemplateRequestTypeDef,
    EvaluateMappingTemplateResponseTypeDef,
    FlushApiCacheRequestTypeDef,
    GetApiAssociationRequestTypeDef,
    GetApiAssociationResponseTypeDef,
    GetApiCacheRequestTypeDef,
    GetApiCacheResponseTypeDef,
    GetApiRequestTypeDef,
    GetApiResponseTypeDef,
    GetChannelNamespaceRequestTypeDef,
    GetChannelNamespaceResponseTypeDef,
    GetDataSourceIntrospectionRequestTypeDef,
    GetDataSourceIntrospectionResponseTypeDef,
    GetDataSourceRequestTypeDef,
    GetDataSourceResponseTypeDef,
    GetDomainNameRequestTypeDef,
    GetDomainNameResponseTypeDef,
    GetFunctionRequestTypeDef,
    GetFunctionResponseTypeDef,
    GetGraphqlApiEnvironmentVariablesRequestTypeDef,
    GetGraphqlApiEnvironmentVariablesResponseTypeDef,
    GetGraphqlApiRequestTypeDef,
    GetGraphqlApiResponseTypeDef,
    GetIntrospectionSchemaRequestTypeDef,
    GetIntrospectionSchemaResponseTypeDef,
    GetResolverRequestTypeDef,
    GetResolverResponseTypeDef,
    GetSchemaCreationStatusRequestTypeDef,
    GetSchemaCreationStatusResponseTypeDef,
    GetSourceApiAssociationRequestTypeDef,
    GetSourceApiAssociationResponseTypeDef,
    GetTypeRequestTypeDef,
    GetTypeResponseTypeDef,
    ListApiKeysRequestTypeDef,
    ListApiKeysResponseTypeDef,
    ListApisRequestTypeDef,
    ListApisResponseTypeDef,
    ListChannelNamespacesRequestTypeDef,
    ListChannelNamespacesResponseTypeDef,
    ListDataSourcesRequestTypeDef,
    ListDataSourcesResponseTypeDef,
    ListDomainNamesRequestTypeDef,
    ListDomainNamesResponseTypeDef,
    ListFunctionsRequestTypeDef,
    ListFunctionsResponseTypeDef,
    ListGraphqlApisRequestTypeDef,
    ListGraphqlApisResponseTypeDef,
    ListResolversByFunctionRequestTypeDef,
    ListResolversByFunctionResponseTypeDef,
    ListResolversRequestTypeDef,
    ListResolversResponseTypeDef,
    ListSourceApiAssociationsRequestTypeDef,
    ListSourceApiAssociationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTypesByAssociationRequestTypeDef,
    ListTypesByAssociationResponseTypeDef,
    ListTypesRequestTypeDef,
    ListTypesResponseTypeDef,
    PutGraphqlApiEnvironmentVariablesRequestTypeDef,
    PutGraphqlApiEnvironmentVariablesResponseTypeDef,
    StartDataSourceIntrospectionRequestTypeDef,
    StartDataSourceIntrospectionResponseTypeDef,
    StartSchemaCreationRequestTypeDef,
    StartSchemaCreationResponseTypeDef,
    StartSchemaMergeRequestTypeDef,
    StartSchemaMergeResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateApiCacheRequestTypeDef,
    UpdateApiCacheResponseTypeDef,
    UpdateApiKeyRequestTypeDef,
    UpdateApiKeyResponseTypeDef,
    UpdateApiRequestTypeDef,
    UpdateApiResponseTypeDef,
    UpdateChannelNamespaceRequestTypeDef,
    UpdateChannelNamespaceResponseTypeDef,
    UpdateDataSourceRequestTypeDef,
    UpdateDataSourceResponseTypeDef,
    UpdateDomainNameRequestTypeDef,
    UpdateDomainNameResponseTypeDef,
    UpdateFunctionRequestTypeDef,
    UpdateFunctionResponseTypeDef,
    UpdateGraphqlApiRequestTypeDef,
    UpdateGraphqlApiResponseTypeDef,
    UpdateResolverRequestTypeDef,
    UpdateResolverResponseTypeDef,
    UpdateSourceApiAssociationRequestTypeDef,
    UpdateSourceApiAssociationResponseTypeDef,
    UpdateTypeRequestTypeDef,
    UpdateTypeResponseTypeDef,
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

__all__ = ("AppSyncClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ApiKeyLimitExceededException: Type[BotocoreClientError]
    ApiKeyValidityOutOfBoundsException: Type[BotocoreClientError]
    ApiLimitExceededException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    GraphQLSchemaException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]

class AppSyncClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppSyncClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync.html#AppSync.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#generate_presigned_url)
        """

    def associate_api(
        self, **kwargs: Unpack[AssociateApiRequestTypeDef]
    ) -> AssociateApiResponseTypeDef:
        """
        Maps an endpoint to your custom domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/associate_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#associate_api)
        """

    def associate_merged_graphql_api(
        self, **kwargs: Unpack[AssociateMergedGraphqlApiRequestTypeDef]
    ) -> AssociateMergedGraphqlApiResponseTypeDef:
        """
        Creates an association between a Merged API and source API using the source
        API's identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/associate_merged_graphql_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#associate_merged_graphql_api)
        """

    def associate_source_graphql_api(
        self, **kwargs: Unpack[AssociateSourceGraphqlApiRequestTypeDef]
    ) -> AssociateSourceGraphqlApiResponseTypeDef:
        """
        Creates an association between a Merged API and source API using the Merged
        API's identifier.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/associate_source_graphql_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#associate_source_graphql_api)
        """

    def create_api(self, **kwargs: Unpack[CreateApiRequestTypeDef]) -> CreateApiResponseTypeDef:
        """
        Creates an <code>Api</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_api)
        """

    def create_api_cache(
        self, **kwargs: Unpack[CreateApiCacheRequestTypeDef]
    ) -> CreateApiCacheResponseTypeDef:
        """
        Creates a cache for the GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_api_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_api_cache)
        """

    def create_api_key(
        self, **kwargs: Unpack[CreateApiKeyRequestTypeDef]
    ) -> CreateApiKeyResponseTypeDef:
        """
        Creates a unique key that you can distribute to clients who invoke your API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_api_key)
        """

    def create_channel_namespace(
        self, **kwargs: Unpack[CreateChannelNamespaceRequestTypeDef]
    ) -> CreateChannelNamespaceResponseTypeDef:
        """
        Creates a <code>ChannelNamespace</code> for an <code>Api</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_channel_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_channel_namespace)
        """

    def create_data_source(
        self, **kwargs: Unpack[CreateDataSourceRequestTypeDef]
    ) -> CreateDataSourceResponseTypeDef:
        """
        Creates a <code>DataSource</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_data_source)
        """

    def create_domain_name(
        self, **kwargs: Unpack[CreateDomainNameRequestTypeDef]
    ) -> CreateDomainNameResponseTypeDef:
        """
        Creates a custom <code>DomainName</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_domain_name)
        """

    def create_function(
        self, **kwargs: Unpack[CreateFunctionRequestTypeDef]
    ) -> CreateFunctionResponseTypeDef:
        """
        Creates a <code>Function</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_function)
        """

    def create_graphql_api(
        self, **kwargs: Unpack[CreateGraphqlApiRequestTypeDef]
    ) -> CreateGraphqlApiResponseTypeDef:
        """
        Creates a <code>GraphqlApi</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_graphql_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_graphql_api)
        """

    def create_resolver(
        self, **kwargs: Unpack[CreateResolverRequestTypeDef]
    ) -> CreateResolverResponseTypeDef:
        """
        Creates a <code>Resolver</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_resolver)
        """

    def create_type(self, **kwargs: Unpack[CreateTypeRequestTypeDef]) -> CreateTypeResponseTypeDef:
        """
        Creates a <code>Type</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/create_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#create_type)
        """

    def delete_api(self, **kwargs: Unpack[DeleteApiRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an <code>Api</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_api)
        """

    def delete_api_cache(self, **kwargs: Unpack[DeleteApiCacheRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an <code>ApiCache</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_api_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_api_cache)
        """

    def delete_api_key(self, **kwargs: Unpack[DeleteApiKeyRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_api_key)
        """

    def delete_channel_namespace(
        self, **kwargs: Unpack[DeleteChannelNamespaceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a <code>ChannelNamespace</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_channel_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_channel_namespace)
        """

    def delete_data_source(
        self, **kwargs: Unpack[DeleteDataSourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a <code>DataSource</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_data_source)
        """

    def delete_domain_name(
        self, **kwargs: Unpack[DeleteDomainNameRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a custom <code>DomainName</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_domain_name)
        """

    def delete_function(self, **kwargs: Unpack[DeleteFunctionRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a <code>Function</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_function)
        """

    def delete_graphql_api(
        self, **kwargs: Unpack[DeleteGraphqlApiRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a <code>GraphqlApi</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_graphql_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_graphql_api)
        """

    def delete_resolver(self, **kwargs: Unpack[DeleteResolverRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a <code>Resolver</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_resolver)
        """

    def delete_type(self, **kwargs: Unpack[DeleteTypeRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a <code>Type</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/delete_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#delete_type)
        """

    def disassociate_api(self, **kwargs: Unpack[DisassociateApiRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes an <code>ApiAssociation</code> object from a custom domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/disassociate_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#disassociate_api)
        """

    def disassociate_merged_graphql_api(
        self, **kwargs: Unpack[DisassociateMergedGraphqlApiRequestTypeDef]
    ) -> DisassociateMergedGraphqlApiResponseTypeDef:
        """
        Deletes an association between a Merged API and source API using the source
        API's identifier and the association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/disassociate_merged_graphql_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#disassociate_merged_graphql_api)
        """

    def disassociate_source_graphql_api(
        self, **kwargs: Unpack[DisassociateSourceGraphqlApiRequestTypeDef]
    ) -> DisassociateSourceGraphqlApiResponseTypeDef:
        """
        Deletes an association between a Merged API and source API using the Merged
        API's identifier and the association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/disassociate_source_graphql_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#disassociate_source_graphql_api)
        """

    def evaluate_code(
        self, **kwargs: Unpack[EvaluateCodeRequestTypeDef]
    ) -> EvaluateCodeResponseTypeDef:
        """
        Evaluates the given code and returns the response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/evaluate_code.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#evaluate_code)
        """

    def evaluate_mapping_template(
        self, **kwargs: Unpack[EvaluateMappingTemplateRequestTypeDef]
    ) -> EvaluateMappingTemplateResponseTypeDef:
        """
        Evaluates a given template and returns the response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/evaluate_mapping_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#evaluate_mapping_template)
        """

    def flush_api_cache(self, **kwargs: Unpack[FlushApiCacheRequestTypeDef]) -> Dict[str, Any]:
        """
        Flushes an <code>ApiCache</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/flush_api_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#flush_api_cache)
        """

    def get_api(self, **kwargs: Unpack[GetApiRequestTypeDef]) -> GetApiResponseTypeDef:
        """
        Retrieves an <code>Api</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_api)
        """

    def get_api_association(
        self, **kwargs: Unpack[GetApiAssociationRequestTypeDef]
    ) -> GetApiAssociationResponseTypeDef:
        """
        Retrieves an <code>ApiAssociation</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_api_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_api_association)
        """

    def get_api_cache(
        self, **kwargs: Unpack[GetApiCacheRequestTypeDef]
    ) -> GetApiCacheResponseTypeDef:
        """
        Retrieves an <code>ApiCache</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_api_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_api_cache)
        """

    def get_channel_namespace(
        self, **kwargs: Unpack[GetChannelNamespaceRequestTypeDef]
    ) -> GetChannelNamespaceResponseTypeDef:
        """
        Retrieves the channel namespace for a specified <code>Api</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_channel_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_channel_namespace)
        """

    def get_data_source(
        self, **kwargs: Unpack[GetDataSourceRequestTypeDef]
    ) -> GetDataSourceResponseTypeDef:
        """
        Retrieves a <code>DataSource</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_data_source)
        """

    def get_data_source_introspection(
        self, **kwargs: Unpack[GetDataSourceIntrospectionRequestTypeDef]
    ) -> GetDataSourceIntrospectionResponseTypeDef:
        """
        Retrieves the record of an existing introspection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_data_source_introspection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_data_source_introspection)
        """

    def get_domain_name(
        self, **kwargs: Unpack[GetDomainNameRequestTypeDef]
    ) -> GetDomainNameResponseTypeDef:
        """
        Retrieves a custom <code>DomainName</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_domain_name)
        """

    def get_function(
        self, **kwargs: Unpack[GetFunctionRequestTypeDef]
    ) -> GetFunctionResponseTypeDef:
        """
        Get a <code>Function</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_function)
        """

    def get_graphql_api(
        self, **kwargs: Unpack[GetGraphqlApiRequestTypeDef]
    ) -> GetGraphqlApiResponseTypeDef:
        """
        Retrieves a <code>GraphqlApi</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_graphql_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_graphql_api)
        """

    def get_graphql_api_environment_variables(
        self, **kwargs: Unpack[GetGraphqlApiEnvironmentVariablesRequestTypeDef]
    ) -> GetGraphqlApiEnvironmentVariablesResponseTypeDef:
        """
        Retrieves the list of environmental variable key-value pairs associated with an
        API by its ID value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_graphql_api_environment_variables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_graphql_api_environment_variables)
        """

    def get_introspection_schema(
        self, **kwargs: Unpack[GetIntrospectionSchemaRequestTypeDef]
    ) -> GetIntrospectionSchemaResponseTypeDef:
        """
        Retrieves the introspection schema for a GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_introspection_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_introspection_schema)
        """

    def get_resolver(
        self, **kwargs: Unpack[GetResolverRequestTypeDef]
    ) -> GetResolverResponseTypeDef:
        """
        Retrieves a <code>Resolver</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_resolver)
        """

    def get_schema_creation_status(
        self, **kwargs: Unpack[GetSchemaCreationStatusRequestTypeDef]
    ) -> GetSchemaCreationStatusResponseTypeDef:
        """
        Retrieves the current status of a schema creation operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_schema_creation_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_schema_creation_status)
        """

    def get_source_api_association(
        self, **kwargs: Unpack[GetSourceApiAssociationRequestTypeDef]
    ) -> GetSourceApiAssociationResponseTypeDef:
        """
        Retrieves a <code>SourceApiAssociation</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_source_api_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_source_api_association)
        """

    def get_type(self, **kwargs: Unpack[GetTypeRequestTypeDef]) -> GetTypeResponseTypeDef:
        """
        Retrieves a <code>Type</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_type)
        """

    def list_api_keys(
        self, **kwargs: Unpack[ListApiKeysRequestTypeDef]
    ) -> ListApiKeysResponseTypeDef:
        """
        Lists the API keys for a given API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_api_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_api_keys)
        """

    def list_apis(self, **kwargs: Unpack[ListApisRequestTypeDef]) -> ListApisResponseTypeDef:
        """
        Lists the APIs in your AppSync account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_apis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_apis)
        """

    def list_channel_namespaces(
        self, **kwargs: Unpack[ListChannelNamespacesRequestTypeDef]
    ) -> ListChannelNamespacesResponseTypeDef:
        """
        Lists the channel namespaces for a specified <code>Api</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_channel_namespaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_channel_namespaces)
        """

    def list_data_sources(
        self, **kwargs: Unpack[ListDataSourcesRequestTypeDef]
    ) -> ListDataSourcesResponseTypeDef:
        """
        Lists the data sources for a given API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_data_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_data_sources)
        """

    def list_domain_names(
        self, **kwargs: Unpack[ListDomainNamesRequestTypeDef]
    ) -> ListDomainNamesResponseTypeDef:
        """
        Lists multiple custom domain names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_domain_names.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_domain_names)
        """

    def list_functions(
        self, **kwargs: Unpack[ListFunctionsRequestTypeDef]
    ) -> ListFunctionsResponseTypeDef:
        """
        List multiple functions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_functions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_functions)
        """

    def list_graphql_apis(
        self, **kwargs: Unpack[ListGraphqlApisRequestTypeDef]
    ) -> ListGraphqlApisResponseTypeDef:
        """
        Lists your GraphQL APIs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_graphql_apis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_graphql_apis)
        """

    def list_resolvers(
        self, **kwargs: Unpack[ListResolversRequestTypeDef]
    ) -> ListResolversResponseTypeDef:
        """
        Lists the resolvers for a given API and type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_resolvers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_resolvers)
        """

    def list_resolvers_by_function(
        self, **kwargs: Unpack[ListResolversByFunctionRequestTypeDef]
    ) -> ListResolversByFunctionResponseTypeDef:
        """
        List the resolvers that are associated with a specific function.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_resolvers_by_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_resolvers_by_function)
        """

    def list_source_api_associations(
        self, **kwargs: Unpack[ListSourceApiAssociationsRequestTypeDef]
    ) -> ListSourceApiAssociationsResponseTypeDef:
        """
        Lists the <code>SourceApiAssociationSummary</code> data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_source_api_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_source_api_associations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_tags_for_resource)
        """

    def list_types(self, **kwargs: Unpack[ListTypesRequestTypeDef]) -> ListTypesResponseTypeDef:
        """
        Lists the types for a given API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_types)
        """

    def list_types_by_association(
        self, **kwargs: Unpack[ListTypesByAssociationRequestTypeDef]
    ) -> ListTypesByAssociationResponseTypeDef:
        """
        Lists <code>Type</code> objects by the source API association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/list_types_by_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#list_types_by_association)
        """

    def put_graphql_api_environment_variables(
        self, **kwargs: Unpack[PutGraphqlApiEnvironmentVariablesRequestTypeDef]
    ) -> PutGraphqlApiEnvironmentVariablesResponseTypeDef:
        """
        Creates a list of environmental variables in an API by its ID value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/put_graphql_api_environment_variables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#put_graphql_api_environment_variables)
        """

    def start_data_source_introspection(
        self, **kwargs: Unpack[StartDataSourceIntrospectionRequestTypeDef]
    ) -> StartDataSourceIntrospectionResponseTypeDef:
        """
        Creates a new introspection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/start_data_source_introspection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#start_data_source_introspection)
        """

    def start_schema_creation(
        self, **kwargs: Unpack[StartSchemaCreationRequestTypeDef]
    ) -> StartSchemaCreationResponseTypeDef:
        """
        Adds a new schema to your GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/start_schema_creation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#start_schema_creation)
        """

    def start_schema_merge(
        self, **kwargs: Unpack[StartSchemaMergeRequestTypeDef]
    ) -> StartSchemaMergeResponseTypeDef:
        """
        Initiates a merge operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/start_schema_merge.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#start_schema_merge)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Tags a resource with user-supplied tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Untags a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#untag_resource)
        """

    def update_api(self, **kwargs: Unpack[UpdateApiRequestTypeDef]) -> UpdateApiResponseTypeDef:
        """
        Updates an <code>Api</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_api)
        """

    def update_api_cache(
        self, **kwargs: Unpack[UpdateApiCacheRequestTypeDef]
    ) -> UpdateApiCacheResponseTypeDef:
        """
        Updates the cache for the GraphQL API.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_api_cache.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_api_cache)
        """

    def update_api_key(
        self, **kwargs: Unpack[UpdateApiKeyRequestTypeDef]
    ) -> UpdateApiKeyResponseTypeDef:
        """
        Updates an API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_api_key)
        """

    def update_channel_namespace(
        self, **kwargs: Unpack[UpdateChannelNamespaceRequestTypeDef]
    ) -> UpdateChannelNamespaceResponseTypeDef:
        """
        Updates a <code>ChannelNamespace</code> associated with an <code>Api</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_channel_namespace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_channel_namespace)
        """

    def update_data_source(
        self, **kwargs: Unpack[UpdateDataSourceRequestTypeDef]
    ) -> UpdateDataSourceResponseTypeDef:
        """
        Updates a <code>DataSource</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_data_source.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_data_source)
        """

    def update_domain_name(
        self, **kwargs: Unpack[UpdateDomainNameRequestTypeDef]
    ) -> UpdateDomainNameResponseTypeDef:
        """
        Updates a custom <code>DomainName</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_domain_name.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_domain_name)
        """

    def update_function(
        self, **kwargs: Unpack[UpdateFunctionRequestTypeDef]
    ) -> UpdateFunctionResponseTypeDef:
        """
        Updates a <code>Function</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_function.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_function)
        """

    def update_graphql_api(
        self, **kwargs: Unpack[UpdateGraphqlApiRequestTypeDef]
    ) -> UpdateGraphqlApiResponseTypeDef:
        """
        Updates a <code>GraphqlApi</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_graphql_api.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_graphql_api)
        """

    def update_resolver(
        self, **kwargs: Unpack[UpdateResolverRequestTypeDef]
    ) -> UpdateResolverResponseTypeDef:
        """
        Updates a <code>Resolver</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_resolver.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_resolver)
        """

    def update_source_api_association(
        self, **kwargs: Unpack[UpdateSourceApiAssociationRequestTypeDef]
    ) -> UpdateSourceApiAssociationResponseTypeDef:
        """
        Updates some of the configuration choices of a particular source API
        association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_source_api_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_source_api_association)
        """

    def update_type(self, **kwargs: Unpack[UpdateTypeRequestTypeDef]) -> UpdateTypeResponseTypeDef:
        """
        Updates a <code>Type</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/update_type.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#update_type)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_api_keys"]
    ) -> ListApiKeysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_apis"]
    ) -> ListApisPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channel_namespaces"]
    ) -> ListChannelNamespacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_sources"]
    ) -> ListDataSourcesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domain_names"]
    ) -> ListDomainNamesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_functions"]
    ) -> ListFunctionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_graphql_apis"]
    ) -> ListGraphqlApisPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolvers_by_function"]
    ) -> ListResolversByFunctionPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resolvers"]
    ) -> ListResolversPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_source_api_associations"]
    ) -> ListSourceApiAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_types_by_association"]
    ) -> ListTypesByAssociationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_types"]
    ) -> ListTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/appsync/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appsync/client/#get_paginator)
        """
