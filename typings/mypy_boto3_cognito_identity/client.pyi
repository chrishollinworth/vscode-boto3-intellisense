"""
Type annotations for cognito-identity service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cognito_identity import CognitoIdentityClient

    client: CognitoIdentityClient = boto3.client("cognito-identity")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .paginator import ListIdentityPoolsPaginator
from .type_defs import (
    CognitoIdentityProviderTypeDef,
    DeleteIdentitiesResponseTypeDef,
    GetCredentialsForIdentityResponseTypeDef,
    GetIdentityPoolRolesResponseTypeDef,
    GetIdResponseTypeDef,
    GetOpenIdTokenForDeveloperIdentityResponseTypeDef,
    GetOpenIdTokenResponseTypeDef,
    GetPrincipalTagAttributeMapResponseTypeDef,
    IdentityDescriptionResponseMetadataTypeDef,
    IdentityPoolTypeDef,
    ListIdentitiesResponseTypeDef,
    ListIdentityPoolsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LookupDeveloperIdentityResponseTypeDef,
    MergeDeveloperIdentitiesResponseTypeDef,
    RoleMappingTypeDef,
    SetPrincipalTagAttributeMapResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("CognitoIdentityClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CognitoIdentityClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#close)
        """
    def create_identity_pool(
        self,
        *,
        IdentityPoolName: str,
        AllowUnauthenticatedIdentities: bool,
        AllowClassicFlow: bool = None,
        SupportedLoginProviders: Dict[str, str] = None,
        DeveloperProviderName: str = None,
        OpenIdConnectProviderARNs: List[str] = None,
        CognitoIdentityProviders: List["CognitoIdentityProviderTypeDef"] = None,
        SamlProviderARNs: List[str] = None,
        IdentityPoolTags: Dict[str, str] = None
    ) -> IdentityPoolTypeDef:
        """
        Creates a new identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.create_identity_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#create_identity_pool)
        """
    def delete_identities(
        self, *, IdentityIdsToDelete: List[str]
    ) -> DeleteIdentitiesResponseTypeDef:
        """
        Deletes identities from an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.delete_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#delete_identities)
        """
    def delete_identity_pool(self, *, IdentityPoolId: str) -> None:
        """
        Deletes an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.delete_identity_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#delete_identity_pool)
        """
    def describe_identity(self, *, IdentityId: str) -> IdentityDescriptionResponseMetadataTypeDef:
        """
        Returns metadata related to the given identity, including when the identity was
        created and any associated linked logins.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#describe_identity)
        """
    def describe_identity_pool(self, *, IdentityPoolId: str) -> IdentityPoolTypeDef:
        """
        Gets details about a particular identity pool, including the pool name, ID
        description, creation date, and current number of users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.describe_identity_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#describe_identity_pool)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#generate_presigned_url)
        """
    def get_credentials_for_identity(
        self, *, IdentityId: str, Logins: Dict[str, str] = None, CustomRoleArn: str = None
    ) -> GetCredentialsForIdentityResponseTypeDef:
        """
        Returns credentials for the provided identity ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.get_credentials_for_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#get_credentials_for_identity)
        """
    def get_id(
        self, *, IdentityPoolId: str, AccountId: str = None, Logins: Dict[str, str] = None
    ) -> GetIdResponseTypeDef:
        """
        Generates (or retrieves) a Cognito ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.get_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#get_id)
        """
    def get_identity_pool_roles(
        self, *, IdentityPoolId: str
    ) -> GetIdentityPoolRolesResponseTypeDef:
        """
        Gets the roles for an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.get_identity_pool_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#get_identity_pool_roles)
        """
    def get_open_id_token(
        self, *, IdentityId: str, Logins: Dict[str, str] = None
    ) -> GetOpenIdTokenResponseTypeDef:
        """
        Gets an OpenID token, using a known Cognito ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.get_open_id_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#get_open_id_token)
        """
    def get_open_id_token_for_developer_identity(
        self,
        *,
        IdentityPoolId: str,
        Logins: Dict[str, str],
        IdentityId: str = None,
        PrincipalTags: Dict[str, str] = None,
        TokenDuration: int = None
    ) -> GetOpenIdTokenForDeveloperIdentityResponseTypeDef:
        """
        Registers (or retrieves) a Cognito `IdentityId` and an OpenID Connect token for
        a user authenticated by your backend authentication process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.get_open_id_token_for_developer_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#get_open_id_token_for_developer_identity)
        """
    def get_principal_tag_attribute_map(
        self, *, IdentityPoolId: str, IdentityProviderName: str
    ) -> GetPrincipalTagAttributeMapResponseTypeDef:
        """
        Use `GetPrincipalTagAttributeMap` to list all mappings between `PrincipalTags`
        and user attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.get_principal_tag_attribute_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#get_principal_tag_attribute_map)
        """
    def list_identities(
        self,
        *,
        IdentityPoolId: str,
        MaxResults: int,
        NextToken: str = None,
        HideDisabled: bool = None
    ) -> ListIdentitiesResponseTypeDef:
        """
        Lists the identities in an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.list_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#list_identities)
        """
    def list_identity_pools(
        self, *, MaxResults: int, NextToken: str = None
    ) -> ListIdentityPoolsResponseTypeDef:
        """
        Lists all of the Cognito identity pools registered for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.list_identity_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#list_identity_pools)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags that are assigned to an Amazon Cognito identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#list_tags_for_resource)
        """
    def lookup_developer_identity(
        self,
        *,
        IdentityPoolId: str,
        IdentityId: str = None,
        DeveloperUserIdentifier: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> LookupDeveloperIdentityResponseTypeDef:
        """
        Retrieves the `IdentityID` associated with a `DeveloperUserIdentifier` or the
        list of `DeveloperUserIdentifier` values associated with an `IdentityId` for an
        existing identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.lookup_developer_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#lookup_developer_identity)
        """
    def merge_developer_identities(
        self,
        *,
        SourceUserIdentifier: str,
        DestinationUserIdentifier: str,
        DeveloperProviderName: str,
        IdentityPoolId: str
    ) -> MergeDeveloperIdentitiesResponseTypeDef:
        """
        Merges two users having different `IdentityId`s, existing in the same identity
        pool, and identified by the same developer provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.merge_developer_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#merge_developer_identities)
        """
    def set_identity_pool_roles(
        self,
        *,
        IdentityPoolId: str,
        Roles: Dict[str, str],
        RoleMappings: Dict[str, "RoleMappingTypeDef"] = None
    ) -> None:
        """
        Sets the roles for an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.set_identity_pool_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#set_identity_pool_roles)
        """
    def set_principal_tag_attribute_map(
        self,
        *,
        IdentityPoolId: str,
        IdentityProviderName: str,
        UseDefaults: bool = None,
        PrincipalTags: Dict[str, str] = None
    ) -> SetPrincipalTagAttributeMapResponseTypeDef:
        """
        You can use this operation to use default (username and clientID) attribute or
        custom attribute mappings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.set_principal_tag_attribute_map)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#set_principal_tag_attribute_map)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Assigns a set of tags to the specified Amazon Cognito identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#tag_resource)
        """
    def unlink_developer_identity(
        self,
        *,
        IdentityId: str,
        IdentityPoolId: str,
        DeveloperProviderName: str,
        DeveloperUserIdentifier: str
    ) -> None:
        """
        Unlinks a `DeveloperUserIdentifier` from an existing identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.unlink_developer_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#unlink_developer_identity)
        """
    def unlink_identity(
        self, *, IdentityId: str, Logins: Dict[str, str], LoginsToRemove: List[str]
    ) -> None:
        """
        Unlinks a federated identity from an existing account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.unlink_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#unlink_identity)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified Amazon Cognito identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#untag_resource)
        """
    def update_identity_pool(
        self,
        *,
        IdentityPoolId: str,
        IdentityPoolName: str,
        AllowUnauthenticatedIdentities: bool,
        AllowClassicFlow: bool = None,
        SupportedLoginProviders: Dict[str, str] = None,
        DeveloperProviderName: str = None,
        OpenIdConnectProviderARNs: List[str] = None,
        CognitoIdentityProviders: List["CognitoIdentityProviderTypeDef"] = None,
        SamlProviderARNs: List[str] = None,
        IdentityPoolTags: Dict[str, str] = None
    ) -> IdentityPoolTypeDef:
        """
        Updates an identity pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Client.update_identity_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/client.html#update_identity_pool)
        """
    def get_paginator(
        self, operation_name: Literal["list_identity_pools"]
    ) -> ListIdentityPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/cognito-identity.html#CognitoIdentity.Paginator.ListIdentityPools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/paginators.html#listidentitypoolspaginator)
        """
