"""
Type annotations for grafana service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_grafana import ManagedGrafanaClient

    client: ManagedGrafanaClient = boto3.client("grafana")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AccountAccessTypeType,
    AuthenticationProviderTypesType,
    DataSourceTypeType,
    LicenseTypeType,
    PermissionTypeType,
    UserTypeType,
)
from .paginator import ListPermissionsPaginator, ListWorkspacesPaginator
from .type_defs import (
    AssociateLicenseResponseTypeDef,
    CreateWorkspaceResponseTypeDef,
    DeleteWorkspaceResponseTypeDef,
    DescribeWorkspaceAuthenticationResponseTypeDef,
    DescribeWorkspaceResponseTypeDef,
    DisassociateLicenseResponseTypeDef,
    ListPermissionsResponseTypeDef,
    ListWorkspacesResponseTypeDef,
    SamlConfigurationTypeDef,
    UpdateInstructionTypeDef,
    UpdatePermissionsResponseTypeDef,
    UpdateWorkspaceAuthenticationResponseTypeDef,
    UpdateWorkspaceResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ManagedGrafanaClient",)

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

class ManagedGrafanaClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        ManagedGrafanaClient exceptions.
        """
    def associate_license(
        self, *, licenseType: LicenseTypeType, workspaceId: str
    ) -> AssociateLicenseResponseTypeDef:
        """
        Assigns a Grafana Enterprise license to a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.associate_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#associate_license)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#can_paginate)
        """
    def create_workspace(
        self,
        *,
        accountAccessType: AccountAccessTypeType,
        authenticationProviders: List[AuthenticationProviderTypesType],
        permissionType: PermissionTypeType,
        clientToken: str = None,
        organizationRoleName: str = None,
        stackSetName: str = None,
        workspaceDataSources: List[DataSourceTypeType] = None,
        workspaceDescription: str = None,
        workspaceName: str = None,
        workspaceNotificationDestinations: List[Literal["SNS"]] = None,
        workspaceOrganizationalUnits: List[str] = None,
        workspaceRoleArn: str = None
    ) -> CreateWorkspaceResponseTypeDef:
        """
        Creates a *workspace*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.create_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#create_workspace)
        """
    def delete_workspace(self, *, workspaceId: str) -> DeleteWorkspaceResponseTypeDef:
        """
        Deletes an Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.delete_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#delete_workspace)
        """
    def describe_workspace(self, *, workspaceId: str) -> DescribeWorkspaceResponseTypeDef:
        """
        Displays information about one Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.describe_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#describe_workspace)
        """
    def describe_workspace_authentication(
        self, *, workspaceId: str
    ) -> DescribeWorkspaceAuthenticationResponseTypeDef:
        """
        Displays information about the authentication methods used in one Amazon Managed
        Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.describe_workspace_authentication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#describe_workspace_authentication)
        """
    def disassociate_license(
        self, *, licenseType: LicenseTypeType, workspaceId: str
    ) -> DisassociateLicenseResponseTypeDef:
        """
        Removes the Grafana Enterprise license from a workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.disassociate_license)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#disassociate_license)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#generate_presigned_url)
        """
    def list_permissions(
        self,
        *,
        workspaceId: str,
        groupId: str = None,
        maxResults: int = None,
        nextToken: str = None,
        userId: str = None,
        userType: UserTypeType = None
    ) -> ListPermissionsResponseTypeDef:
        """
        Lists the users and groups who have the Grafana `Admin` and `Editor` roles in
        this workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.list_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#list_permissions)
        """
    def list_workspaces(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListWorkspacesResponseTypeDef:
        """
        Returns a list of Amazon Managed Grafana workspaces in the account, with some
        information about each workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.list_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#list_workspaces)
        """
    def update_permissions(
        self, *, updateInstructionBatch: List["UpdateInstructionTypeDef"], workspaceId: str
    ) -> UpdatePermissionsResponseTypeDef:
        """
        Updates which users in a workspace have the Grafana `Admin` or `Editor` roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.update_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#update_permissions)
        """
    def update_workspace(
        self,
        *,
        workspaceId: str,
        accountAccessType: AccountAccessTypeType = None,
        organizationRoleName: str = None,
        permissionType: PermissionTypeType = None,
        stackSetName: str = None,
        workspaceDataSources: List[DataSourceTypeType] = None,
        workspaceDescription: str = None,
        workspaceName: str = None,
        workspaceNotificationDestinations: List[Literal["SNS"]] = None,
        workspaceOrganizationalUnits: List[str] = None,
        workspaceRoleArn: str = None
    ) -> UpdateWorkspaceResponseTypeDef:
        """
        Modifies an existing Amazon Managed Grafana workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.update_workspace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#update_workspace)
        """
    def update_workspace_authentication(
        self,
        *,
        authenticationProviders: List[AuthenticationProviderTypesType],
        workspaceId: str,
        samlConfiguration: "SamlConfigurationTypeDef" = None
    ) -> UpdateWorkspaceAuthenticationResponseTypeDef:
        """
        Use this operation to define the identity provider (IdP) that this workspace
        authenticates users from, using SAML.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Client.update_workspace_authentication)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/client.html#update_workspace_authentication)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_permissions"]
    ) -> ListPermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Paginator.ListPermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listpermissionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_workspaces"]) -> ListWorkspacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/grafana.html#ManagedGrafana.Paginator.ListWorkspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_grafana/paginators.html#listworkspacespaginator)
        """
