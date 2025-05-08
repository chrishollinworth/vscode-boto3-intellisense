"""
Type annotations for grafana service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_grafana.client import ManagedGrafanaClient

    session = Session()
    client: ManagedGrafanaClient = session.client("grafana")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListPermissionsPaginator,
    ListVersionsPaginator,
    ListWorkspaceServiceAccountsPaginator,
    ListWorkspaceServiceAccountTokensPaginator,
    ListWorkspacesPaginator,
)
from .type_defs import (
    AssociateLicenseRequestTypeDef,
    AssociateLicenseResponseTypeDef,
    CreateWorkspaceApiKeyRequestTypeDef,
    CreateWorkspaceApiKeyResponseTypeDef,
    CreateWorkspaceRequestTypeDef,
    CreateWorkspaceResponseTypeDef,
    CreateWorkspaceServiceAccountRequestTypeDef,
    CreateWorkspaceServiceAccountResponseTypeDef,
    CreateWorkspaceServiceAccountTokenRequestTypeDef,
    CreateWorkspaceServiceAccountTokenResponseTypeDef,
    DeleteWorkspaceApiKeyRequestTypeDef,
    DeleteWorkspaceApiKeyResponseTypeDef,
    DeleteWorkspaceRequestTypeDef,
    DeleteWorkspaceResponseTypeDef,
    DeleteWorkspaceServiceAccountRequestTypeDef,
    DeleteWorkspaceServiceAccountResponseTypeDef,
    DeleteWorkspaceServiceAccountTokenRequestTypeDef,
    DeleteWorkspaceServiceAccountTokenResponseTypeDef,
    DescribeWorkspaceAuthenticationRequestTypeDef,
    DescribeWorkspaceAuthenticationResponseTypeDef,
    DescribeWorkspaceConfigurationRequestTypeDef,
    DescribeWorkspaceConfigurationResponseTypeDef,
    DescribeWorkspaceRequestTypeDef,
    DescribeWorkspaceResponseTypeDef,
    DisassociateLicenseRequestTypeDef,
    DisassociateLicenseResponseTypeDef,
    ListPermissionsRequestTypeDef,
    ListPermissionsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVersionsRequestTypeDef,
    ListVersionsResponseTypeDef,
    ListWorkspaceServiceAccountsRequestTypeDef,
    ListWorkspaceServiceAccountsResponseTypeDef,
    ListWorkspaceServiceAccountTokensRequestTypeDef,
    ListWorkspaceServiceAccountTokensResponseTypeDef,
    ListWorkspacesRequestTypeDef,
    ListWorkspacesResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdatePermissionsRequestTypeDef,
    UpdatePermissionsResponseTypeDef,
    UpdateWorkspaceAuthenticationRequestTypeDef,
    UpdateWorkspaceAuthenticationResponseTypeDef,
    UpdateWorkspaceConfigurationRequestTypeDef,
    UpdateWorkspaceRequestTypeDef,
    UpdateWorkspaceResponseTypeDef,
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

__all__ = ("ManagedGrafanaClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ManagedGrafanaClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ManagedGrafanaClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana.html#ManagedGrafana.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#generate_presigned_url)
        """

    def associate_license(
        self, **kwargs: Unpack[AssociateLicenseRequestTypeDef]
    ) -> AssociateLicenseResponseTypeDef:
        """
        Assigns a Grafana Enterprise license to a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/associate_license.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#associate_license)
        """

    def create_workspace(
        self, **kwargs: Unpack[CreateWorkspaceRequestTypeDef]
    ) -> CreateWorkspaceResponseTypeDef:
        """
        Creates a <i>workspace</i>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/create_workspace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#create_workspace)
        """

    def create_workspace_api_key(
        self, **kwargs: Unpack[CreateWorkspaceApiKeyRequestTypeDef]
    ) -> CreateWorkspaceApiKeyResponseTypeDef:
        """
        Creates a Grafana API key for the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/create_workspace_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#create_workspace_api_key)
        """

    def create_workspace_service_account(
        self, **kwargs: Unpack[CreateWorkspaceServiceAccountRequestTypeDef]
    ) -> CreateWorkspaceServiceAccountResponseTypeDef:
        """
        Creates a service account for the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/create_workspace_service_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#create_workspace_service_account)
        """

    def create_workspace_service_account_token(
        self, **kwargs: Unpack[CreateWorkspaceServiceAccountTokenRequestTypeDef]
    ) -> CreateWorkspaceServiceAccountTokenResponseTypeDef:
        """
        Creates a token that can be used to authenticate and authorize Grafana HTTP API
        operations for the given <a
        href="https://docs.aws.amazon.com/grafana/latest/userguide/service-accounts.html">workspace
        service account</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/create_workspace_service_account_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#create_workspace_service_account_token)
        """

    def delete_workspace(
        self, **kwargs: Unpack[DeleteWorkspaceRequestTypeDef]
    ) -> DeleteWorkspaceResponseTypeDef:
        """
        Deletes an Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/delete_workspace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#delete_workspace)
        """

    def delete_workspace_api_key(
        self, **kwargs: Unpack[DeleteWorkspaceApiKeyRequestTypeDef]
    ) -> DeleteWorkspaceApiKeyResponseTypeDef:
        """
        Deletes a Grafana API key for the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/delete_workspace_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#delete_workspace_api_key)
        """

    def delete_workspace_service_account(
        self, **kwargs: Unpack[DeleteWorkspaceServiceAccountRequestTypeDef]
    ) -> DeleteWorkspaceServiceAccountResponseTypeDef:
        """
        Deletes a workspace service account from the workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/delete_workspace_service_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#delete_workspace_service_account)
        """

    def delete_workspace_service_account_token(
        self, **kwargs: Unpack[DeleteWorkspaceServiceAccountTokenRequestTypeDef]
    ) -> DeleteWorkspaceServiceAccountTokenResponseTypeDef:
        """
        Deletes a token for the workspace service account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/delete_workspace_service_account_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#delete_workspace_service_account_token)
        """

    def describe_workspace(
        self, **kwargs: Unpack[DescribeWorkspaceRequestTypeDef]
    ) -> DescribeWorkspaceResponseTypeDef:
        """
        Displays information about one Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/describe_workspace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#describe_workspace)
        """

    def describe_workspace_authentication(
        self, **kwargs: Unpack[DescribeWorkspaceAuthenticationRequestTypeDef]
    ) -> DescribeWorkspaceAuthenticationResponseTypeDef:
        """
        Displays information about the authentication methods used in one Amazon
        Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/describe_workspace_authentication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#describe_workspace_authentication)
        """

    def describe_workspace_configuration(
        self, **kwargs: Unpack[DescribeWorkspaceConfigurationRequestTypeDef]
    ) -> DescribeWorkspaceConfigurationResponseTypeDef:
        """
        Gets the current configuration string for the given workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/describe_workspace_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#describe_workspace_configuration)
        """

    def disassociate_license(
        self, **kwargs: Unpack[DisassociateLicenseRequestTypeDef]
    ) -> DisassociateLicenseResponseTypeDef:
        """
        Removes the Grafana Enterprise license from a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/disassociate_license.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#disassociate_license)
        """

    def list_permissions(
        self, **kwargs: Unpack[ListPermissionsRequestTypeDef]
    ) -> ListPermissionsResponseTypeDef:
        """
        Lists the users and groups who have the Grafana <code>Admin</code> and
        <code>Editor</code> roles in this workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/list_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_permissions)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        The <code>ListTagsForResource</code> operation returns the tags that are
        associated with the Amazon Managed Service for Grafana resource specified by
        the <code>resourceArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_tags_for_resource)
        """

    def list_versions(
        self, **kwargs: Unpack[ListVersionsRequestTypeDef]
    ) -> ListVersionsResponseTypeDef:
        """
        Lists available versions of Grafana.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/list_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_versions)
        """

    def list_workspace_service_account_tokens(
        self, **kwargs: Unpack[ListWorkspaceServiceAccountTokensRequestTypeDef]
    ) -> ListWorkspaceServiceAccountTokensResponseTypeDef:
        """
        Returns a list of tokens for a workspace service account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/list_workspace_service_account_tokens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_workspace_service_account_tokens)
        """

    def list_workspace_service_accounts(
        self, **kwargs: Unpack[ListWorkspaceServiceAccountsRequestTypeDef]
    ) -> ListWorkspaceServiceAccountsResponseTypeDef:
        """
        Returns a list of service accounts for a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/list_workspace_service_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_workspace_service_accounts)
        """

    def list_workspaces(
        self, **kwargs: Unpack[ListWorkspacesRequestTypeDef]
    ) -> ListWorkspacesResponseTypeDef:
        """
        Returns a list of Amazon Managed Grafana workspaces in the account, with some
        information about each workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/list_workspaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#list_workspaces)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        The <code>TagResource</code> operation associates tags with an Amazon Managed
        Grafana resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        The <code>UntagResource</code> operation removes the association of the tag
        with the Amazon Managed Grafana resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#untag_resource)
        """

    def update_permissions(
        self, **kwargs: Unpack[UpdatePermissionsRequestTypeDef]
    ) -> UpdatePermissionsResponseTypeDef:
        """
        Updates which users in a workspace have the Grafana <code>Admin</code> or
        <code>Editor</code> roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/update_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#update_permissions)
        """

    def update_workspace(
        self, **kwargs: Unpack[UpdateWorkspaceRequestTypeDef]
    ) -> UpdateWorkspaceResponseTypeDef:
        """
        Modifies an existing Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/update_workspace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#update_workspace)
        """

    def update_workspace_authentication(
        self, **kwargs: Unpack[UpdateWorkspaceAuthenticationRequestTypeDef]
    ) -> UpdateWorkspaceAuthenticationResponseTypeDef:
        """
        Use this operation to define the identity provider (IdP) that this workspace
        authenticates users from, using SAML.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/update_workspace_authentication.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#update_workspace_authentication)
        """

    def update_workspace_configuration(
        self, **kwargs: Unpack[UpdateWorkspaceConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates the configuration string for the given workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/update_workspace_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#update_workspace_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_permissions"]
    ) -> ListPermissionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_versions"]
    ) -> ListVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workspace_service_account_tokens"]
    ) -> ListWorkspaceServiceAccountTokensPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workspace_service_accounts"]
    ) -> ListWorkspaceServiceAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workspaces"]
    ) -> ListWorkspacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/grafana/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_grafana/client/#get_paginator)
        """
