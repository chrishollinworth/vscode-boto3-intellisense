"""
Type annotations for workspaces-web service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workspaces_web.client import WorkSpacesWebClient

    session = Session()
    client: WorkSpacesWebClient = session.client("workspaces-web")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListDataProtectionSettingsPaginator, ListSessionsPaginator
from .type_defs import (
    AssociateBrowserSettingsRequestTypeDef,
    AssociateBrowserSettingsResponseTypeDef,
    AssociateDataProtectionSettingsRequestTypeDef,
    AssociateDataProtectionSettingsResponseTypeDef,
    AssociateIpAccessSettingsRequestTypeDef,
    AssociateIpAccessSettingsResponseTypeDef,
    AssociateNetworkSettingsRequestTypeDef,
    AssociateNetworkSettingsResponseTypeDef,
    AssociateTrustStoreRequestTypeDef,
    AssociateTrustStoreResponseTypeDef,
    AssociateUserAccessLoggingSettingsRequestTypeDef,
    AssociateUserAccessLoggingSettingsResponseTypeDef,
    AssociateUserSettingsRequestTypeDef,
    AssociateUserSettingsResponseTypeDef,
    CreateBrowserSettingsRequestTypeDef,
    CreateBrowserSettingsResponseTypeDef,
    CreateDataProtectionSettingsRequestTypeDef,
    CreateDataProtectionSettingsResponseTypeDef,
    CreateIdentityProviderRequestTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateIpAccessSettingsRequestTypeDef,
    CreateIpAccessSettingsResponseTypeDef,
    CreateNetworkSettingsRequestTypeDef,
    CreateNetworkSettingsResponseTypeDef,
    CreatePortalRequestTypeDef,
    CreatePortalResponseTypeDef,
    CreateTrustStoreRequestTypeDef,
    CreateTrustStoreResponseTypeDef,
    CreateUserAccessLoggingSettingsRequestTypeDef,
    CreateUserAccessLoggingSettingsResponseTypeDef,
    CreateUserSettingsRequestTypeDef,
    CreateUserSettingsResponseTypeDef,
    DeleteBrowserSettingsRequestTypeDef,
    DeleteDataProtectionSettingsRequestTypeDef,
    DeleteIdentityProviderRequestTypeDef,
    DeleteIpAccessSettingsRequestTypeDef,
    DeleteNetworkSettingsRequestTypeDef,
    DeletePortalRequestTypeDef,
    DeleteTrustStoreRequestTypeDef,
    DeleteUserAccessLoggingSettingsRequestTypeDef,
    DeleteUserSettingsRequestTypeDef,
    DisassociateBrowserSettingsRequestTypeDef,
    DisassociateDataProtectionSettingsRequestTypeDef,
    DisassociateIpAccessSettingsRequestTypeDef,
    DisassociateNetworkSettingsRequestTypeDef,
    DisassociateTrustStoreRequestTypeDef,
    DisassociateUserAccessLoggingSettingsRequestTypeDef,
    DisassociateUserSettingsRequestTypeDef,
    ExpireSessionRequestTypeDef,
    GetBrowserSettingsRequestTypeDef,
    GetBrowserSettingsResponseTypeDef,
    GetDataProtectionSettingsRequestTypeDef,
    GetDataProtectionSettingsResponseTypeDef,
    GetIdentityProviderRequestTypeDef,
    GetIdentityProviderResponseTypeDef,
    GetIpAccessSettingsRequestTypeDef,
    GetIpAccessSettingsResponseTypeDef,
    GetNetworkSettingsRequestTypeDef,
    GetNetworkSettingsResponseTypeDef,
    GetPortalRequestTypeDef,
    GetPortalResponseTypeDef,
    GetPortalServiceProviderMetadataRequestTypeDef,
    GetPortalServiceProviderMetadataResponseTypeDef,
    GetSessionRequestTypeDef,
    GetSessionResponseTypeDef,
    GetTrustStoreCertificateRequestTypeDef,
    GetTrustStoreCertificateResponseTypeDef,
    GetTrustStoreRequestTypeDef,
    GetTrustStoreResponseTypeDef,
    GetUserAccessLoggingSettingsRequestTypeDef,
    GetUserAccessLoggingSettingsResponseTypeDef,
    GetUserSettingsRequestTypeDef,
    GetUserSettingsResponseTypeDef,
    ListBrowserSettingsRequestTypeDef,
    ListBrowserSettingsResponseTypeDef,
    ListDataProtectionSettingsRequestTypeDef,
    ListDataProtectionSettingsResponseTypeDef,
    ListIdentityProvidersRequestTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListIpAccessSettingsRequestTypeDef,
    ListIpAccessSettingsResponseTypeDef,
    ListNetworkSettingsRequestTypeDef,
    ListNetworkSettingsResponseTypeDef,
    ListPortalsRequestTypeDef,
    ListPortalsResponseTypeDef,
    ListSessionsRequestTypeDef,
    ListSessionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTrustStoreCertificatesRequestTypeDef,
    ListTrustStoreCertificatesResponseTypeDef,
    ListTrustStoresRequestTypeDef,
    ListTrustStoresResponseTypeDef,
    ListUserAccessLoggingSettingsRequestTypeDef,
    ListUserAccessLoggingSettingsResponseTypeDef,
    ListUserSettingsRequestTypeDef,
    ListUserSettingsResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBrowserSettingsRequestTypeDef,
    UpdateBrowserSettingsResponseTypeDef,
    UpdateDataProtectionSettingsRequestTypeDef,
    UpdateDataProtectionSettingsResponseTypeDef,
    UpdateIdentityProviderRequestTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateIpAccessSettingsRequestTypeDef,
    UpdateIpAccessSettingsResponseTypeDef,
    UpdateNetworkSettingsRequestTypeDef,
    UpdateNetworkSettingsResponseTypeDef,
    UpdatePortalRequestTypeDef,
    UpdatePortalResponseTypeDef,
    UpdateTrustStoreRequestTypeDef,
    UpdateTrustStoreResponseTypeDef,
    UpdateUserAccessLoggingSettingsRequestTypeDef,
    UpdateUserAccessLoggingSettingsResponseTypeDef,
    UpdateUserSettingsRequestTypeDef,
    UpdateUserSettingsResponseTypeDef,
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

__all__ = ("WorkSpacesWebClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WorkSpacesWebClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web.html#WorkSpacesWeb.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#generate_presigned_url)
        """

    def associate_browser_settings(
        self, **kwargs: Unpack[AssociateBrowserSettingsRequestTypeDef]
    ) -> AssociateBrowserSettingsResponseTypeDef:
        """
        Associates a browser settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/associate_browser_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#associate_browser_settings)
        """

    def associate_data_protection_settings(
        self, **kwargs: Unpack[AssociateDataProtectionSettingsRequestTypeDef]
    ) -> AssociateDataProtectionSettingsResponseTypeDef:
        """
        Associates a data protection settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/associate_data_protection_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#associate_data_protection_settings)
        """

    def associate_ip_access_settings(
        self, **kwargs: Unpack[AssociateIpAccessSettingsRequestTypeDef]
    ) -> AssociateIpAccessSettingsResponseTypeDef:
        """
        Associates an IP access settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/associate_ip_access_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#associate_ip_access_settings)
        """

    def associate_network_settings(
        self, **kwargs: Unpack[AssociateNetworkSettingsRequestTypeDef]
    ) -> AssociateNetworkSettingsResponseTypeDef:
        """
        Associates a network settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/associate_network_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#associate_network_settings)
        """

    def associate_trust_store(
        self, **kwargs: Unpack[AssociateTrustStoreRequestTypeDef]
    ) -> AssociateTrustStoreResponseTypeDef:
        """
        Associates a trust store with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/associate_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#associate_trust_store)
        """

    def associate_user_access_logging_settings(
        self, **kwargs: Unpack[AssociateUserAccessLoggingSettingsRequestTypeDef]
    ) -> AssociateUserAccessLoggingSettingsResponseTypeDef:
        """
        Associates a user access logging settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/associate_user_access_logging_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#associate_user_access_logging_settings)
        """

    def associate_user_settings(
        self, **kwargs: Unpack[AssociateUserSettingsRequestTypeDef]
    ) -> AssociateUserSettingsResponseTypeDef:
        """
        Associates a user settings resource with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/associate_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#associate_user_settings)
        """

    def create_browser_settings(
        self, **kwargs: Unpack[CreateBrowserSettingsRequestTypeDef]
    ) -> CreateBrowserSettingsResponseTypeDef:
        """
        Creates a browser settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_browser_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_browser_settings)
        """

    def create_data_protection_settings(
        self, **kwargs: Unpack[CreateDataProtectionSettingsRequestTypeDef]
    ) -> CreateDataProtectionSettingsResponseTypeDef:
        """
        Creates a data protection settings resource that can be associated with a web
        portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_data_protection_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_data_protection_settings)
        """

    def create_identity_provider(
        self, **kwargs: Unpack[CreateIdentityProviderRequestTypeDef]
    ) -> CreateIdentityProviderResponseTypeDef:
        """
        Creates an identity provider resource that is then associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_identity_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_identity_provider)
        """

    def create_ip_access_settings(
        self, **kwargs: Unpack[CreateIpAccessSettingsRequestTypeDef]
    ) -> CreateIpAccessSettingsResponseTypeDef:
        """
        Creates an IP access settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_ip_access_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_ip_access_settings)
        """

    def create_network_settings(
        self, **kwargs: Unpack[CreateNetworkSettingsRequestTypeDef]
    ) -> CreateNetworkSettingsResponseTypeDef:
        """
        Creates a network settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_network_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_network_settings)
        """

    def create_portal(
        self, **kwargs: Unpack[CreatePortalRequestTypeDef]
    ) -> CreatePortalResponseTypeDef:
        """
        Creates a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_portal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_portal)
        """

    def create_trust_store(
        self, **kwargs: Unpack[CreateTrustStoreRequestTypeDef]
    ) -> CreateTrustStoreResponseTypeDef:
        """
        Creates a trust store that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_trust_store)
        """

    def create_user_access_logging_settings(
        self, **kwargs: Unpack[CreateUserAccessLoggingSettingsRequestTypeDef]
    ) -> CreateUserAccessLoggingSettingsResponseTypeDef:
        """
        Creates a user access logging settings resource that can be associated with a
        web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_user_access_logging_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_user_access_logging_settings)
        """

    def create_user_settings(
        self, **kwargs: Unpack[CreateUserSettingsRequestTypeDef]
    ) -> CreateUserSettingsResponseTypeDef:
        """
        Creates a user settings resource that can be associated with a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/create_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#create_user_settings)
        """

    def delete_browser_settings(
        self, **kwargs: Unpack[DeleteBrowserSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_browser_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_browser_settings)
        """

    def delete_data_protection_settings(
        self, **kwargs: Unpack[DeleteDataProtectionSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes data protection settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_data_protection_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_data_protection_settings)
        """

    def delete_identity_provider(
        self, **kwargs: Unpack[DeleteIdentityProviderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_identity_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_identity_provider)
        """

    def delete_ip_access_settings(
        self, **kwargs: Unpack[DeleteIpAccessSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes IP access settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_ip_access_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_ip_access_settings)
        """

    def delete_network_settings(
        self, **kwargs: Unpack[DeleteNetworkSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_network_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_network_settings)
        """

    def delete_portal(self, **kwargs: Unpack[DeletePortalRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_portal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_portal)
        """

    def delete_trust_store(
        self, **kwargs: Unpack[DeleteTrustStoreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_trust_store)
        """

    def delete_user_access_logging_settings(
        self, **kwargs: Unpack[DeleteUserAccessLoggingSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_user_access_logging_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_user_access_logging_settings)
        """

    def delete_user_settings(
        self, **kwargs: Unpack[DeleteUserSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/delete_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#delete_user_settings)
        """

    def disassociate_browser_settings(
        self, **kwargs: Unpack[DisassociateBrowserSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates browser settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/disassociate_browser_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#disassociate_browser_settings)
        """

    def disassociate_data_protection_settings(
        self, **kwargs: Unpack[DisassociateDataProtectionSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates data protection settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/disassociate_data_protection_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#disassociate_data_protection_settings)
        """

    def disassociate_ip_access_settings(
        self, **kwargs: Unpack[DisassociateIpAccessSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates IP access settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/disassociate_ip_access_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#disassociate_ip_access_settings)
        """

    def disassociate_network_settings(
        self, **kwargs: Unpack[DisassociateNetworkSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates network settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/disassociate_network_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#disassociate_network_settings)
        """

    def disassociate_trust_store(
        self, **kwargs: Unpack[DisassociateTrustStoreRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates a trust store from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/disassociate_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#disassociate_trust_store)
        """

    def disassociate_user_access_logging_settings(
        self, **kwargs: Unpack[DisassociateUserAccessLoggingSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates user access logging settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/disassociate_user_access_logging_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#disassociate_user_access_logging_settings)
        """

    def disassociate_user_settings(
        self, **kwargs: Unpack[DisassociateUserSettingsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates user settings from a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/disassociate_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#disassociate_user_settings)
        """

    def expire_session(self, **kwargs: Unpack[ExpireSessionRequestTypeDef]) -> Dict[str, Any]:
        """
        Expires an active secure browser session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/expire_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#expire_session)
        """

    def get_browser_settings(
        self, **kwargs: Unpack[GetBrowserSettingsRequestTypeDef]
    ) -> GetBrowserSettingsResponseTypeDef:
        """
        Gets browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_browser_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_browser_settings)
        """

    def get_data_protection_settings(
        self, **kwargs: Unpack[GetDataProtectionSettingsRequestTypeDef]
    ) -> GetDataProtectionSettingsResponseTypeDef:
        """
        Gets the data protection settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_data_protection_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_data_protection_settings)
        """

    def get_identity_provider(
        self, **kwargs: Unpack[GetIdentityProviderRequestTypeDef]
    ) -> GetIdentityProviderResponseTypeDef:
        """
        Gets the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_identity_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_identity_provider)
        """

    def get_ip_access_settings(
        self, **kwargs: Unpack[GetIpAccessSettingsRequestTypeDef]
    ) -> GetIpAccessSettingsResponseTypeDef:
        """
        Gets the IP access settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_ip_access_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_ip_access_settings)
        """

    def get_network_settings(
        self, **kwargs: Unpack[GetNetworkSettingsRequestTypeDef]
    ) -> GetNetworkSettingsResponseTypeDef:
        """
        Gets the network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_network_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_network_settings)
        """

    def get_portal(self, **kwargs: Unpack[GetPortalRequestTypeDef]) -> GetPortalResponseTypeDef:
        """
        Gets the web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_portal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_portal)
        """

    def get_portal_service_provider_metadata(
        self, **kwargs: Unpack[GetPortalServiceProviderMetadataRequestTypeDef]
    ) -> GetPortalServiceProviderMetadataResponseTypeDef:
        """
        Gets the service provider metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_portal_service_provider_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_portal_service_provider_metadata)
        """

    def get_session(self, **kwargs: Unpack[GetSessionRequestTypeDef]) -> GetSessionResponseTypeDef:
        """
        Gets information for a secure browser session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_session)
        """

    def get_trust_store(
        self, **kwargs: Unpack[GetTrustStoreRequestTypeDef]
    ) -> GetTrustStoreResponseTypeDef:
        """
        Gets the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_trust_store)
        """

    def get_trust_store_certificate(
        self, **kwargs: Unpack[GetTrustStoreCertificateRequestTypeDef]
    ) -> GetTrustStoreCertificateResponseTypeDef:
        """
        Gets the trust store certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_trust_store_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_trust_store_certificate)
        """

    def get_user_access_logging_settings(
        self, **kwargs: Unpack[GetUserAccessLoggingSettingsRequestTypeDef]
    ) -> GetUserAccessLoggingSettingsResponseTypeDef:
        """
        Gets user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_user_access_logging_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_user_access_logging_settings)
        """

    def get_user_settings(
        self, **kwargs: Unpack[GetUserSettingsRequestTypeDef]
    ) -> GetUserSettingsResponseTypeDef:
        """
        Gets user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_user_settings)
        """

    def list_browser_settings(
        self, **kwargs: Unpack[ListBrowserSettingsRequestTypeDef]
    ) -> ListBrowserSettingsResponseTypeDef:
        """
        Retrieves a list of browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_browser_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_browser_settings)
        """

    def list_data_protection_settings(
        self, **kwargs: Unpack[ListDataProtectionSettingsRequestTypeDef]
    ) -> ListDataProtectionSettingsResponseTypeDef:
        """
        Retrieves a list of data protection settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_data_protection_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_data_protection_settings)
        """

    def list_identity_providers(
        self, **kwargs: Unpack[ListIdentityProvidersRequestTypeDef]
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        Retrieves a list of identity providers for a specific web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_identity_providers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_identity_providers)
        """

    def list_ip_access_settings(
        self, **kwargs: Unpack[ListIpAccessSettingsRequestTypeDef]
    ) -> ListIpAccessSettingsResponseTypeDef:
        """
        Retrieves a list of IP access settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_ip_access_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_ip_access_settings)
        """

    def list_network_settings(
        self, **kwargs: Unpack[ListNetworkSettingsRequestTypeDef]
    ) -> ListNetworkSettingsResponseTypeDef:
        """
        Retrieves a list of network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_network_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_network_settings)
        """

    def list_portals(
        self, **kwargs: Unpack[ListPortalsRequestTypeDef]
    ) -> ListPortalsResponseTypeDef:
        """
        Retrieves a list or web portals.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_portals.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_portals)
        """

    def list_sessions(
        self, **kwargs: Unpack[ListSessionsRequestTypeDef]
    ) -> ListSessionsResponseTypeDef:
        """
        Lists information for multiple secure browser sessions from a specific portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_sessions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves a list of tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_tags_for_resource)
        """

    def list_trust_store_certificates(
        self, **kwargs: Unpack[ListTrustStoreCertificatesRequestTypeDef]
    ) -> ListTrustStoreCertificatesResponseTypeDef:
        """
        Retrieves a list of trust store certificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_trust_store_certificates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_trust_store_certificates)
        """

    def list_trust_stores(
        self, **kwargs: Unpack[ListTrustStoresRequestTypeDef]
    ) -> ListTrustStoresResponseTypeDef:
        """
        Retrieves a list of trust stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_trust_stores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_trust_stores)
        """

    def list_user_access_logging_settings(
        self, **kwargs: Unpack[ListUserAccessLoggingSettingsRequestTypeDef]
    ) -> ListUserAccessLoggingSettingsResponseTypeDef:
        """
        Retrieves a list of user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_user_access_logging_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_user_access_logging_settings)
        """

    def list_user_settings(
        self, **kwargs: Unpack[ListUserSettingsRequestTypeDef]
    ) -> ListUserSettingsResponseTypeDef:
        """
        Retrieves a list of user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/list_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#list_user_settings)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes one or more tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#untag_resource)
        """

    def update_browser_settings(
        self, **kwargs: Unpack[UpdateBrowserSettingsRequestTypeDef]
    ) -> UpdateBrowserSettingsResponseTypeDef:
        """
        Updates browser settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_browser_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_browser_settings)
        """

    def update_data_protection_settings(
        self, **kwargs: Unpack[UpdateDataProtectionSettingsRequestTypeDef]
    ) -> UpdateDataProtectionSettingsResponseTypeDef:
        """
        Updates data protection settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_data_protection_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_data_protection_settings)
        """

    def update_identity_provider(
        self, **kwargs: Unpack[UpdateIdentityProviderRequestTypeDef]
    ) -> UpdateIdentityProviderResponseTypeDef:
        """
        Updates the identity provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_identity_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_identity_provider)
        """

    def update_ip_access_settings(
        self, **kwargs: Unpack[UpdateIpAccessSettingsRequestTypeDef]
    ) -> UpdateIpAccessSettingsResponseTypeDef:
        """
        Updates IP access settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_ip_access_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_ip_access_settings)
        """

    def update_network_settings(
        self, **kwargs: Unpack[UpdateNetworkSettingsRequestTypeDef]
    ) -> UpdateNetworkSettingsResponseTypeDef:
        """
        Updates network settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_network_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_network_settings)
        """

    def update_portal(
        self, **kwargs: Unpack[UpdatePortalRequestTypeDef]
    ) -> UpdatePortalResponseTypeDef:
        """
        Updates a web portal.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_portal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_portal)
        """

    def update_trust_store(
        self, **kwargs: Unpack[UpdateTrustStoreRequestTypeDef]
    ) -> UpdateTrustStoreResponseTypeDef:
        """
        Updates the trust store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_trust_store.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_trust_store)
        """

    def update_user_access_logging_settings(
        self, **kwargs: Unpack[UpdateUserAccessLoggingSettingsRequestTypeDef]
    ) -> UpdateUserAccessLoggingSettingsResponseTypeDef:
        """
        Updates the user access logging settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_user_access_logging_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_user_access_logging_settings)
        """

    def update_user_settings(
        self, **kwargs: Unpack[UpdateUserSettingsRequestTypeDef]
    ) -> UpdateUserSettingsResponseTypeDef:
        """
        Updates the user settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/update_user_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#update_user_settings)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_data_protection_settings"]
    ) -> ListDataProtectionSettingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sessions"]
    ) -> ListSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/workspaces-web/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_web/client/#get_paginator)
        """
