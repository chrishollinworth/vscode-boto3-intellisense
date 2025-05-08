"""
Type annotations for cognito-identity service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cognito_identity.client import CognitoIdentityClient

    session = Session()
    client: CognitoIdentityClient = session.client("cognito-identity")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListIdentityPoolsPaginator
from .type_defs import (
    CreateIdentityPoolInputTypeDef,
    DeleteIdentitiesInputTypeDef,
    DeleteIdentitiesResponseTypeDef,
    DeleteIdentityPoolInputTypeDef,
    DescribeIdentityInputTypeDef,
    DescribeIdentityPoolInputTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCredentialsForIdentityInputTypeDef,
    GetCredentialsForIdentityResponseTypeDef,
    GetIdentityPoolRolesInputTypeDef,
    GetIdentityPoolRolesResponseTypeDef,
    GetIdInputTypeDef,
    GetIdResponseTypeDef,
    GetOpenIdTokenForDeveloperIdentityInputTypeDef,
    GetOpenIdTokenForDeveloperIdentityResponseTypeDef,
    GetOpenIdTokenInputTypeDef,
    GetOpenIdTokenResponseTypeDef,
    GetPrincipalTagAttributeMapInputTypeDef,
    GetPrincipalTagAttributeMapResponseTypeDef,
    IdentityDescriptionResponseTypeDef,
    IdentityPoolRequestTypeDef,
    IdentityPoolTypeDef,
    ListIdentitiesInputTypeDef,
    ListIdentitiesResponseTypeDef,
    ListIdentityPoolsInputTypeDef,
    ListIdentityPoolsResponseTypeDef,
    ListTagsForResourceInputTypeDef,
    ListTagsForResourceResponseTypeDef,
    LookupDeveloperIdentityInputTypeDef,
    LookupDeveloperIdentityResponseTypeDef,
    MergeDeveloperIdentitiesInputTypeDef,
    MergeDeveloperIdentitiesResponseTypeDef,
    SetIdentityPoolRolesInputTypeDef,
    SetPrincipalTagAttributeMapInputTypeDef,
    SetPrincipalTagAttributeMapResponseTypeDef,
    TagResourceInputTypeDef,
    UnlinkDeveloperIdentityInputTypeDef,
    UnlinkIdentityInputTypeDef,
    UntagResourceInputTypeDef,
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

__all__ = ("CognitoIdentityClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DeveloperUserAlreadyRegisteredException: Type[BotocoreClientError]
    ExternalServiceException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidIdentityPoolConfigurationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]

class CognitoIdentityClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CognitoIdentityClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity.html#CognitoIdentity.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#generate_presigned_url)
        """

    def create_identity_pool(
        self, **kwargs: Unpack[CreateIdentityPoolInputTypeDef]
    ) -> IdentityPoolTypeDef:
        """
        Creates a new identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/create_identity_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#create_identity_pool)
        """

    def delete_identities(
        self, **kwargs: Unpack[DeleteIdentitiesInputTypeDef]
    ) -> DeleteIdentitiesResponseTypeDef:
        """
        Deletes identities from an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/delete_identities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#delete_identities)
        """

    def delete_identity_pool(
        self, **kwargs: Unpack[DeleteIdentityPoolInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/delete_identity_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#delete_identity_pool)
        """

    def describe_identity(
        self, **kwargs: Unpack[DescribeIdentityInputTypeDef]
    ) -> IdentityDescriptionResponseTypeDef:
        """
        Returns metadata related to the given identity, including when the identity was
        created and any associated linked logins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/describe_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#describe_identity)
        """

    def describe_identity_pool(
        self, **kwargs: Unpack[DescribeIdentityPoolInputTypeDef]
    ) -> IdentityPoolTypeDef:
        """
        Gets details about a particular identity pool, including the pool name, ID
        description, creation date, and current number of users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/describe_identity_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#describe_identity_pool)
        """

    def get_credentials_for_identity(
        self, **kwargs: Unpack[GetCredentialsForIdentityInputTypeDef]
    ) -> GetCredentialsForIdentityResponseTypeDef:
        """
        Returns credentials for the provided identity ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/get_credentials_for_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#get_credentials_for_identity)
        """

    def get_id(self, **kwargs: Unpack[GetIdInputTypeDef]) -> GetIdResponseTypeDef:
        """
        Generates (or retrieves) IdentityID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/get_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#get_id)
        """

    def get_identity_pool_roles(
        self, **kwargs: Unpack[GetIdentityPoolRolesInputTypeDef]
    ) -> GetIdentityPoolRolesResponseTypeDef:
        """
        Gets the roles for an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/get_identity_pool_roles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#get_identity_pool_roles)
        """

    def get_open_id_token(
        self, **kwargs: Unpack[GetOpenIdTokenInputTypeDef]
    ) -> GetOpenIdTokenResponseTypeDef:
        """
        Gets an OpenID token, using a known Cognito ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/get_open_id_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#get_open_id_token)
        """

    def get_open_id_token_for_developer_identity(
        self, **kwargs: Unpack[GetOpenIdTokenForDeveloperIdentityInputTypeDef]
    ) -> GetOpenIdTokenForDeveloperIdentityResponseTypeDef:
        """
        Registers (or retrieves) a Cognito <code>IdentityId</code> and an OpenID
        Connect token for a user authenticated by your backend authentication process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/get_open_id_token_for_developer_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#get_open_id_token_for_developer_identity)
        """

    def get_principal_tag_attribute_map(
        self, **kwargs: Unpack[GetPrincipalTagAttributeMapInputTypeDef]
    ) -> GetPrincipalTagAttributeMapResponseTypeDef:
        """
        Use <code>GetPrincipalTagAttributeMap</code> to list all mappings between
        <code>PrincipalTags</code> and user attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/get_principal_tag_attribute_map.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#get_principal_tag_attribute_map)
        """

    def list_identities(
        self, **kwargs: Unpack[ListIdentitiesInputTypeDef]
    ) -> ListIdentitiesResponseTypeDef:
        """
        Lists the identities in an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/list_identities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#list_identities)
        """

    def list_identity_pools(
        self, **kwargs: Unpack[ListIdentityPoolsInputTypeDef]
    ) -> ListIdentityPoolsResponseTypeDef:
        """
        Lists all of the Cognito identity pools registered for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/list_identity_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#list_identity_pools)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceInputTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are assigned to an Amazon Cognito identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#list_tags_for_resource)
        """

    def lookup_developer_identity(
        self, **kwargs: Unpack[LookupDeveloperIdentityInputTypeDef]
    ) -> LookupDeveloperIdentityResponseTypeDef:
        """
        Retrieves the <code>IdentityID</code> associated with a
        <code>DeveloperUserIdentifier</code> or the list of
        <code>DeveloperUserIdentifier</code> values associated with an
        <code>IdentityId</code> for an existing identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/lookup_developer_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#lookup_developer_identity)
        """

    def merge_developer_identities(
        self, **kwargs: Unpack[MergeDeveloperIdentitiesInputTypeDef]
    ) -> MergeDeveloperIdentitiesResponseTypeDef:
        """
        Merges two users having different <code>IdentityId</code>s, existing in the
        same identity pool, and identified by the same developer provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/merge_developer_identities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#merge_developer_identities)
        """

    def set_identity_pool_roles(
        self, **kwargs: Unpack[SetIdentityPoolRolesInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets the roles for an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/set_identity_pool_roles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#set_identity_pool_roles)
        """

    def set_principal_tag_attribute_map(
        self, **kwargs: Unpack[SetPrincipalTagAttributeMapInputTypeDef]
    ) -> SetPrincipalTagAttributeMapResponseTypeDef:
        """
        You can use this operation to use default (username and clientID) attribute or
        custom attribute mappings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/set_principal_tag_attribute_map.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#set_principal_tag_attribute_map)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Assigns a set of tags to the specified Amazon Cognito identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#tag_resource)
        """

    def unlink_developer_identity(
        self, **kwargs: Unpack[UnlinkDeveloperIdentityInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Unlinks a <code>DeveloperUserIdentifier</code> from an existing identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/unlink_developer_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#unlink_developer_identity)
        """

    def unlink_identity(
        self, **kwargs: Unpack[UnlinkIdentityInputTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Unlinks a federated identity from an existing account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/unlink_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#unlink_identity)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceInputTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified Amazon Cognito identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#untag_resource)
        """

    def update_identity_pool(
        self, **kwargs: Unpack[IdentityPoolRequestTypeDef]
    ) -> IdentityPoolTypeDef:
        """
        Updates the configuration of an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/update_identity_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#update_identity_pool)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_identity_pools"]
    ) -> ListIdentityPoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-identity/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client/#get_paginator)
        """
