"""
Type annotations for workspaces-web service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_workspaces_web import WorkSpacesWebClient

    client: WorkSpacesWebClient = boto3.client("workspaces-web")
    ```
"""
from typing import IO, Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import AuthenticationTypeType, EnabledTypeType, IdentityProviderTypeType
from .type_defs import (
    AssociateBrowserSettingsResponseTypeDef,
    AssociateNetworkSettingsResponseTypeDef,
    AssociateTrustStoreResponseTypeDef,
    AssociateUserAccessLoggingSettingsResponseTypeDef,
    AssociateUserSettingsResponseTypeDef,
    CreateBrowserSettingsResponseTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateNetworkSettingsResponseTypeDef,
    CreatePortalResponseTypeDef,
    CreateTrustStoreResponseTypeDef,
    CreateUserAccessLoggingSettingsResponseTypeDef,
    CreateUserSettingsResponseTypeDef,
    GetBrowserSettingsResponseTypeDef,
    GetIdentityProviderResponseTypeDef,
    GetNetworkSettingsResponseTypeDef,
    GetPortalResponseTypeDef,
    GetPortalServiceProviderMetadataResponseTypeDef,
    GetTrustStoreCertificateResponseTypeDef,
    GetTrustStoreResponseTypeDef,
    GetUserAccessLoggingSettingsResponseTypeDef,
    GetUserSettingsResponseTypeDef,
    ListBrowserSettingsResponseTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListNetworkSettingsResponseTypeDef,
    ListPortalsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrustStoreCertificatesResponseTypeDef,
    ListTrustStoresResponseTypeDef,
    ListUserAccessLoggingSettingsResponseTypeDef,
    ListUserSettingsResponseTypeDef,
    TagTypeDef,
    UpdateBrowserSettingsResponseTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateNetworkSettingsResponseTypeDef,
    UpdatePortalResponseTypeDef,
    UpdateTrustStoreResponseTypeDef,
    UpdateUserAccessLoggingSettingsResponseTypeDef,
    UpdateUserSettingsResponseTypeDef,
)

__all__ = ("WorkSpacesWebClient",)

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
    TooManyTagsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class WorkSpacesWebClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkSpacesWebClient exceptions.
        """
    def associate_browser_settings(
        self, *, browserSettingsArn: str, portalArn: str
    ) -> AssociateBrowserSettingsResponseTypeDef:
        """
        Associates a browser settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_browser_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#associate_browser_settings)
        """
    def associate_network_settings(
        self, *, networkSettingsArn: str, portalArn: str
    ) -> AssociateNetworkSettingsResponseTypeDef:
        """
        Associates a network settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_network_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#associate_network_settings)
        """
    def associate_trust_store(
        self, *, portalArn: str, trustStoreArn: str
    ) -> AssociateTrustStoreResponseTypeDef:
        """
        Associates a trust store with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_trust_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#associate_trust_store)
        """
    def associate_user_access_logging_settings(
        self, *, portalArn: str, userAccessLoggingSettingsArn: str
    ) -> AssociateUserAccessLoggingSettingsResponseTypeDef:
        """
        Associates a user access logging settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_user_access_logging_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#associate_user_access_logging_settings)
        """
    def associate_user_settings(
        self, *, portalArn: str, userSettingsArn: str
    ) -> AssociateUserSettingsResponseTypeDef:
        """
        Associates a user settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.associate_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#associate_user_settings)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#close)
        """
    def create_browser_settings(
        self,
        *,
        browserPolicy: str,
        additionalEncryptionContext: Dict[str, str] = None,
        clientToken: str = None,
        customerManagedKey: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateBrowserSettingsResponseTypeDef:
        """
        Creates a browser settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_browser_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#create_browser_settings)
        """
    def create_identity_provider(
        self,
        *,
        identityProviderDetails: Dict[str, str],
        identityProviderName: str,
        identityProviderType: IdentityProviderTypeType,
        portalArn: str,
        clientToken: str = None
    ) -> CreateIdentityProviderResponseTypeDef:
        """
        Creates an identity provider resource that is then associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#create_identity_provider)
        """
    def create_network_settings(
        self,
        *,
        securityGroupIds: List[str],
        subnetIds: List[str],
        vpcId: str,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateNetworkSettingsResponseTypeDef:
        """
        Creates a network settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_network_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#create_network_settings)
        """
    def create_portal(
        self,
        *,
        additionalEncryptionContext: Dict[str, str] = None,
        authenticationType: AuthenticationTypeType = None,
        clientToken: str = None,
        customerManagedKey: str = None,
        displayName: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreatePortalResponseTypeDef:
        """
        Creates a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_portal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#create_portal)
        """
    def create_trust_store(
        self,
        *,
        certificateList: List[Union[bytes, IO[bytes], StreamingBody]],
        clientToken: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateTrustStoreResponseTypeDef:
        """
        Creates a trust store that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_trust_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#create_trust_store)
        """
    def create_user_access_logging_settings(
        self, *, kinesisStreamArn: str, clientToken: str = None, tags: List["TagTypeDef"] = None
    ) -> CreateUserAccessLoggingSettingsResponseTypeDef:
        """
        Creates a user access logging settings resource that can be associated with a
        web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_user_access_logging_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#create_user_access_logging_settings)
        """
    def create_user_settings(
        self,
        *,
        copyAllowed: EnabledTypeType,
        downloadAllowed: EnabledTypeType,
        pasteAllowed: EnabledTypeType,
        printAllowed: EnabledTypeType,
        uploadAllowed: EnabledTypeType,
        clientToken: str = None,
        disconnectTimeoutInMinutes: int = None,
        idleDisconnectTimeoutInMinutes: int = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateUserSettingsResponseTypeDef:
        """
        Creates a user settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.create_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#create_user_settings)
        """
    def delete_browser_settings(self, *, browserSettingsArn: str) -> Dict[str, Any]:
        """
        Deletes browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_browser_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#delete_browser_settings)
        """
    def delete_identity_provider(self, *, identityProviderArn: str) -> Dict[str, Any]:
        """
        Deletes the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#delete_identity_provider)
        """
    def delete_network_settings(self, *, networkSettingsArn: str) -> Dict[str, Any]:
        """
        Deletes network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_network_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#delete_network_settings)
        """
    def delete_portal(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Deletes a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_portal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#delete_portal)
        """
    def delete_trust_store(self, *, trustStoreArn: str) -> Dict[str, Any]:
        """
        Deletes the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_trust_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#delete_trust_store)
        """
    def delete_user_access_logging_settings(
        self, *, userAccessLoggingSettingsArn: str
    ) -> Dict[str, Any]:
        """
        Deletes user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_user_access_logging_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#delete_user_access_logging_settings)
        """
    def delete_user_settings(self, *, userSettingsArn: str) -> Dict[str, Any]:
        """
        Deletes user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.delete_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#delete_user_settings)
        """
    def disassociate_browser_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates browser settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_browser_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#disassociate_browser_settings)
        """
    def disassociate_network_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates network settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_network_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#disassociate_network_settings)
        """
    def disassociate_trust_store(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates a trust store from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_trust_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#disassociate_trust_store)
        """
    def disassociate_user_access_logging_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates user access logging settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_user_access_logging_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#disassociate_user_access_logging_settings)
        """
    def disassociate_user_settings(self, *, portalArn: str) -> Dict[str, Any]:
        """
        Disassociates user settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.disassociate_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#disassociate_user_settings)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#generate_presigned_url)
        """
    def get_browser_settings(self, *, browserSettingsArn: str) -> GetBrowserSettingsResponseTypeDef:
        """
        Gets browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_browser_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_browser_settings)
        """
    def get_identity_provider(
        self, *, identityProviderArn: str
    ) -> GetIdentityProviderResponseTypeDef:
        """
        Gets the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_identity_provider)
        """
    def get_network_settings(self, *, networkSettingsArn: str) -> GetNetworkSettingsResponseTypeDef:
        """
        Gets the network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_network_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_network_settings)
        """
    def get_portal(self, *, portalArn: str) -> GetPortalResponseTypeDef:
        """
        Gets the web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_portal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_portal)
        """
    def get_portal_service_provider_metadata(
        self, *, portalArn: str
    ) -> GetPortalServiceProviderMetadataResponseTypeDef:
        """
        Gets the service provider metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_portal_service_provider_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_portal_service_provider_metadata)
        """
    def get_trust_store(self, *, trustStoreArn: str) -> GetTrustStoreResponseTypeDef:
        """
        Gets the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_trust_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_trust_store)
        """
    def get_trust_store_certificate(
        self, *, thumbprint: str, trustStoreArn: str
    ) -> GetTrustStoreCertificateResponseTypeDef:
        """
        Gets the trust store certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_trust_store_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_trust_store_certificate)
        """
    def get_user_access_logging_settings(
        self, *, userAccessLoggingSettingsArn: str
    ) -> GetUserAccessLoggingSettingsResponseTypeDef:
        """
        Gets user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_user_access_logging_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_user_access_logging_settings)
        """
    def get_user_settings(self, *, userSettingsArn: str) -> GetUserSettingsResponseTypeDef:
        """
        Gets user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.get_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#get_user_settings)
        """
    def list_browser_settings(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListBrowserSettingsResponseTypeDef:
        """
        Retrieves a list of browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_browser_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_browser_settings)
        """
    def list_identity_providers(
        self, *, portalArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Retrieves a list of identity providers for a specific web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_identity_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_identity_providers)
        """
    def list_network_settings(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListNetworkSettingsResponseTypeDef:
        """
        Retrieves a list of network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_network_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_network_settings)
        """
    def list_portals(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListPortalsResponseTypeDef:
        """
        Retrieves a list or web portals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_portals)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_portals)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_tags_for_resource)
        """
    def list_trust_store_certificates(
        self, *, trustStoreArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListTrustStoreCertificatesResponseTypeDef:
        """
        Retrieves a list of trust store certificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_trust_store_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_trust_store_certificates)
        """
    def list_trust_stores(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListTrustStoresResponseTypeDef:
        """
        Retrieves a list of trust stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_trust_stores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_trust_stores)
        """
    def list_user_access_logging_settings(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListUserAccessLoggingSettingsResponseTypeDef:
        """
        Retrieves a list of user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_user_access_logging_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_user_access_logging_settings)
        """
    def list_user_settings(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListUserSettingsResponseTypeDef:
        """
        Retrieves a list of user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.list_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#list_user_settings)
        """
    def tag_resource(
        self, *, resourceArn: str, tags: List["TagTypeDef"], clientToken: str = None
    ) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#untag_resource)
        """
    def update_browser_settings(
        self, *, browserSettingsArn: str, browserPolicy: str = None, clientToken: str = None
    ) -> UpdateBrowserSettingsResponseTypeDef:
        """
        Updates browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_browser_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#update_browser_settings)
        """
    def update_identity_provider(
        self,
        *,
        identityProviderArn: str,
        clientToken: str = None,
        identityProviderDetails: Dict[str, str] = None,
        identityProviderName: str = None,
        identityProviderType: IdentityProviderTypeType = None
    ) -> UpdateIdentityProviderResponseTypeDef:
        """
        Updates the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#update_identity_provider)
        """
    def update_network_settings(
        self,
        *,
        networkSettingsArn: str,
        clientToken: str = None,
        securityGroupIds: List[str] = None,
        subnetIds: List[str] = None,
        vpcId: str = None
    ) -> UpdateNetworkSettingsResponseTypeDef:
        """
        Updates network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_network_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#update_network_settings)
        """
    def update_portal(
        self,
        *,
        portalArn: str,
        authenticationType: AuthenticationTypeType = None,
        displayName: str = None
    ) -> UpdatePortalResponseTypeDef:
        """
        Updates a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_portal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#update_portal)
        """
    def update_trust_store(
        self,
        *,
        trustStoreArn: str,
        certificatesToAdd: List[Union[bytes, IO[bytes], StreamingBody]] = None,
        certificatesToDelete: List[str] = None,
        clientToken: str = None
    ) -> UpdateTrustStoreResponseTypeDef:
        """
        Updates the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_trust_store)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#update_trust_store)
        """
    def update_user_access_logging_settings(
        self,
        *,
        userAccessLoggingSettingsArn: str,
        clientToken: str = None,
        kinesisStreamArn: str = None
    ) -> UpdateUserAccessLoggingSettingsResponseTypeDef:
        """
        Updates the user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_user_access_logging_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#update_user_access_logging_settings)
        """
    def update_user_settings(
        self,
        *,
        userSettingsArn: str,
        clientToken: str = None,
        copyAllowed: EnabledTypeType = None,
        disconnectTimeoutInMinutes: int = None,
        downloadAllowed: EnabledTypeType = None,
        idleDisconnectTimeoutInMinutes: int = None,
        pasteAllowed: EnabledTypeType = None,
        printAllowed: EnabledTypeType = None,
        uploadAllowed: EnabledTypeType = None
    ) -> UpdateUserSettingsResponseTypeDef:
        """
        Updates the user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/workspaces-web.html#WorkSpacesWeb.Client.update_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client.html#update_user_settings)
        """
