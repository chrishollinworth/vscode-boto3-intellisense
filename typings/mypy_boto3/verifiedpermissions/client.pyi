"""
Type annotations for verifiedpermissions service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_verifiedpermissions import VerifiedPermissionsClient

    client: VerifiedPermissionsClient = boto3.client("verifiedpermissions")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .paginator import (
    ListIdentitySourcesPaginator,
    ListPoliciesPaginator,
    ListPolicyStoresPaginator,
    ListPolicyTemplatesPaginator,
)
from .type_defs import (
    ActionIdentifierTypeDef,
    ConfigurationTypeDef,
    ContextDefinitionTypeDef,
    CreateIdentitySourceOutputTypeDef,
    CreatePolicyOutputTypeDef,
    CreatePolicyStoreOutputTypeDef,
    CreatePolicyTemplateOutputTypeDef,
    EntitiesDefinitionTypeDef,
    EntityIdentifierTypeDef,
    GetIdentitySourceOutputTypeDef,
    GetPolicyOutputTypeDef,
    GetPolicyStoreOutputTypeDef,
    GetPolicyTemplateOutputTypeDef,
    GetSchemaOutputTypeDef,
    IdentitySourceFilterTypeDef,
    IsAuthorizedOutputTypeDef,
    IsAuthorizedWithTokenOutputTypeDef,
    ListIdentitySourcesOutputTypeDef,
    ListPoliciesOutputTypeDef,
    ListPolicyStoresOutputTypeDef,
    ListPolicyTemplatesOutputTypeDef,
    PolicyDefinitionTypeDef,
    PolicyFilterTypeDef,
    PutSchemaOutputTypeDef,
    SchemaDefinitionTypeDef,
    UpdateConfigurationTypeDef,
    UpdateIdentitySourceOutputTypeDef,
    UpdatePolicyDefinitionTypeDef,
    UpdatePolicyOutputTypeDef,
    UpdatePolicyStoreOutputTypeDef,
    UpdatePolicyTemplateOutputTypeDef,
    ValidationSettingsTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("VerifiedPermissionsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class VerifiedPermissionsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        VerifiedPermissionsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#close)
        """
    def create_identity_source(
        self,
        *,
        policyStoreId: str,
        configuration: "ConfigurationTypeDef",
        clientToken: str = None,
        principalEntityType: str = None
    ) -> CreateIdentitySourceOutputTypeDef:
        """
        Creates a reference to an Amazon Cognito user pool as an external identity
        provider (IdP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.create_identity_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#create_identity_source)
        """
    def create_policy(
        self, *, policyStoreId: str, definition: "PolicyDefinitionTypeDef", clientToken: str = None
    ) -> CreatePolicyOutputTypeDef:
        """
        Creates a Cedar policy and saves it in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#create_policy)
        """
    def create_policy_store(
        self, *, validationSettings: "ValidationSettingsTypeDef", clientToken: str = None
    ) -> CreatePolicyStoreOutputTypeDef:
        """
        Creates a policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.create_policy_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#create_policy_store)
        """
    def create_policy_template(
        self,
        *,
        policyStoreId: str,
        statement: str,
        clientToken: str = None,
        description: str = None
    ) -> CreatePolicyTemplateOutputTypeDef:
        """
        Creates a policy template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.create_policy_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#create_policy_template)
        """
    def delete_identity_source(
        self, *, policyStoreId: str, identitySourceId: str
    ) -> Dict[str, Any]:
        """
        Deletes an identity source that references an identity provider (IdP) such as
        Amazon Cognito.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.delete_identity_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#delete_identity_source)
        """
    def delete_policy(self, *, policyStoreId: str, policyId: str) -> Dict[str, Any]:
        """
        Deletes the specified policy from the policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#delete_policy)
        """
    def delete_policy_store(self, *, policyStoreId: str) -> Dict[str, Any]:
        """
        Deletes the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.delete_policy_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#delete_policy_store)
        """
    def delete_policy_template(
        self, *, policyStoreId: str, policyTemplateId: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified policy template from the policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.delete_policy_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#delete_policy_template)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#generate_presigned_url)
        """
    def get_identity_source(
        self, *, policyStoreId: str, identitySourceId: str
    ) -> GetIdentitySourceOutputTypeDef:
        """
        Retrieves the details about the specified identity source.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.get_identity_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#get_identity_source)
        """
    def get_policy(self, *, policyStoreId: str, policyId: str) -> GetPolicyOutputTypeDef:
        """
        Retrieves information about the specified policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#get_policy)
        """
    def get_policy_store(self, *, policyStoreId: str) -> GetPolicyStoreOutputTypeDef:
        """
        Retrieves details about a policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.get_policy_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#get_policy_store)
        """
    def get_policy_template(
        self, *, policyStoreId: str, policyTemplateId: str
    ) -> GetPolicyTemplateOutputTypeDef:
        """
        Retrieve the details for the specified policy template in the specified policy
        store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.get_policy_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#get_policy_template)
        """
    def get_schema(self, *, policyStoreId: str) -> GetSchemaOutputTypeDef:
        """
        Retrieve the details for the specified schema in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.get_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#get_schema)
        """
    def is_authorized(
        self,
        *,
        policyStoreId: str,
        principal: "EntityIdentifierTypeDef" = None,
        action: "ActionIdentifierTypeDef" = None,
        resource: "EntityIdentifierTypeDef" = None,
        context: "ContextDefinitionTypeDef" = None,
        entities: "EntitiesDefinitionTypeDef" = None
    ) -> IsAuthorizedOutputTypeDef:
        """
        Makes an authorization decision about a service request described in the
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.is_authorized)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#is_authorized)
        """
    def is_authorized_with_token(
        self,
        *,
        policyStoreId: str,
        identityToken: str = None,
        accessToken: str = None,
        action: "ActionIdentifierTypeDef" = None,
        resource: "EntityIdentifierTypeDef" = None,
        context: "ContextDefinitionTypeDef" = None,
        entities: "EntitiesDefinitionTypeDef" = None
    ) -> IsAuthorizedWithTokenOutputTypeDef:
        """
        Makes an authorization decision about a service request described in the
        parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.is_authorized_with_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#is_authorized_with_token)
        """
    def list_identity_sources(
        self,
        *,
        policyStoreId: str,
        nextToken: str = None,
        maxResults: int = None,
        filters: List["IdentitySourceFilterTypeDef"] = None
    ) -> ListIdentitySourcesOutputTypeDef:
        """
        Returns a paginated list of all of the identity sources defined in the specified
        policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.list_identity_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#list_identity_sources)
        """
    def list_policies(
        self,
        *,
        policyStoreId: str,
        nextToken: str = None,
        maxResults: int = None,
        filter: "PolicyFilterTypeDef" = None
    ) -> ListPoliciesOutputTypeDef:
        """
        Returns a paginated list of all policies stored in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.list_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#list_policies)
        """
    def list_policy_stores(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListPolicyStoresOutputTypeDef:
        """
        Returns a paginated list of all policy stores in the calling Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.list_policy_stores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#list_policy_stores)
        """
    def list_policy_templates(
        self, *, policyStoreId: str, nextToken: str = None, maxResults: int = None
    ) -> ListPolicyTemplatesOutputTypeDef:
        """
        Returns a paginated list of all policy templates in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.list_policy_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#list_policy_templates)
        """
    def put_schema(
        self, *, policyStoreId: str, definition: "SchemaDefinitionTypeDef"
    ) -> PutSchemaOutputTypeDef:
        """
        Creates or updates the policy schema in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.put_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#put_schema)
        """
    def update_identity_source(
        self,
        *,
        policyStoreId: str,
        identitySourceId: str,
        updateConfiguration: "UpdateConfigurationTypeDef",
        principalEntityType: str = None
    ) -> UpdateIdentitySourceOutputTypeDef:
        """
        Updates the specified identity source to use a new identity provider (IdP)
        source, or to change the mapping of identities from the IdP to a different
        principal entity type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.update_identity_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#update_identity_source)
        """
    def update_policy(
        self, *, policyStoreId: str, policyId: str, definition: "UpdatePolicyDefinitionTypeDef"
    ) -> UpdatePolicyOutputTypeDef:
        """
        Modifies a Cedar static policy in the specified policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.update_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#update_policy)
        """
    def update_policy_store(
        self, *, policyStoreId: str, validationSettings: "ValidationSettingsTypeDef"
    ) -> UpdatePolicyStoreOutputTypeDef:
        """
        Modifies the validation setting for a policy store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.update_policy_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#update_policy_store)
        """
    def update_policy_template(
        self, *, policyStoreId: str, policyTemplateId: str, statement: str, description: str = None
    ) -> UpdatePolicyTemplateOutputTypeDef:
        """
        Updates the specified policy template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Client.update_policy_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/client.html#update_policy_template)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_sources"]
    ) -> ListIdentitySourcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListIdentitySources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listidentitysourcespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_stores"]
    ) -> ListPolicyStoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyStores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpolicystorespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_policy_templates"]
    ) -> ListPolicyTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/verifiedpermissions.html#VerifiedPermissions.Paginator.ListPolicyTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_verifiedpermissions/paginators.html#listpolicytemplatespaginator)
        """
