"""
Type annotations for detective service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_detective import DetectiveClient

    client: DetectiveClient = boto3.client("detective")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import DatasourcePackageType
from .type_defs import (
    AccountTypeDef,
    BatchGetGraphMemberDatasourcesResponseTypeDef,
    BatchGetMembershipDatasourcesResponseTypeDef,
    CreateGraphResponseTypeDef,
    CreateMembersResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    GetMembersResponseTypeDef,
    ListDatasourcePackagesResponseTypeDef,
    ListGraphsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
)

__all__ = ("DetectiveClient",)

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
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class DetectiveClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        DetectiveClient exceptions.
        """
    def accept_invitation(self, *, GraphArn: str) -> None:
        """
        Accepts an invitation for the member account to contribute data to a behavior
        graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#accept_invitation)
        """
    def batch_get_graph_member_datasources(
        self, *, GraphArn: str, AccountIds: List[str]
    ) -> BatchGetGraphMemberDatasourcesResponseTypeDef:
        """
        Gets data source package information for the behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.batch_get_graph_member_datasources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#batch_get_graph_member_datasources)
        """
    def batch_get_membership_datasources(
        self, *, GraphArns: List[str]
    ) -> BatchGetMembershipDatasourcesResponseTypeDef:
        """
        Gets information on the data source package history for an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.batch_get_membership_datasources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#batch_get_membership_datasources)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#close)
        """
    def create_graph(self, *, Tags: Dict[str, str] = None) -> CreateGraphResponseTypeDef:
        """
        Creates a new behavior graph for the calling account, and sets that account as
        the administrator account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.create_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#create_graph)
        """
    def create_members(
        self,
        *,
        GraphArn: str,
        Accounts: List["AccountTypeDef"],
        Message: str = None,
        DisableEmailNotification: bool = None
    ) -> CreateMembersResponseTypeDef:
        """
        `CreateMembers` is used to send invitations to accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.create_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#create_members)
        """
    def delete_graph(self, *, GraphArn: str) -> None:
        """
        Disables the specified behavior graph and queues it to be deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.delete_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#delete_graph)
        """
    def delete_members(
        self, *, GraphArn: str, AccountIds: List[str]
    ) -> DeleteMembersResponseTypeDef:
        """
        Removes the specified member accounts from the behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.delete_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#delete_members)
        """
    def describe_organization_configuration(
        self, *, GraphArn: str
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        Returns information about the configuration for the organization behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#describe_organization_configuration)
        """
    def disable_organization_admin_account(self) -> None:
        """
        Removes the Detective administrator account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#disable_organization_admin_account)
        """
    def disassociate_membership(self, *, GraphArn: str) -> None:
        """
        Removes the member account from the specified behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.disassociate_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#disassociate_membership)
        """
    def enable_organization_admin_account(self, *, AccountId: str) -> None:
        """
        Designates the Detective administrator account for the organization in the
        current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#enable_organization_admin_account)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#generate_presigned_url)
        """
    def get_members(self, *, GraphArn: str, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        Returns the membership details for specified member accounts for a behavior
        graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.get_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#get_members)
        """
    def list_datasource_packages(
        self, *, GraphArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListDatasourcePackagesResponseTypeDef:
        """
        Lists data source packages in the behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.list_datasource_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list_datasource_packages)
        """
    def list_graphs(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListGraphsResponseTypeDef:
        """
        Returns the list of behavior graphs that the calling account is an administrator
        account of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.list_graphs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list_graphs)
        """
    def list_invitations(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListInvitationsResponseTypeDef:
        """
        Retrieves the list of open and accepted behavior graph invitations for the
        member account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list_invitations)
        """
    def list_members(
        self, *, GraphArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMembersResponseTypeDef:
        """
        Retrieves the list of member accounts for a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list_members)
        """
    def list_organization_admin_accounts(
        self, *, NextToken: str = None, MaxResults: int = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        Returns information about the Detective administrator account for an
        organization.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list_organization_admin_accounts)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Returns the tag values that are assigned to a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list_tags_for_resource)
        """
    def reject_invitation(self, *, GraphArn: str) -> None:
        """
        Rejects an invitation to contribute the account data to a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.reject_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#reject_invitation)
        """
    def start_monitoring_member(self, *, GraphArn: str, AccountId: str) -> None:
        """
        Sends a request to enable data ingest for a member account that has a status of
        `ACCEPTED_BUT_DISABLED`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.start_monitoring_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#start_monitoring_member)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Applies tag values to a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from a behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#untag_resource)
        """
    def update_datasource_packages(
        self, *, GraphArn: str, DatasourcePackages: List[DatasourcePackageType]
    ) -> None:
        """
        Starts a data source packages for the behavior graph.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.update_datasource_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#update_datasource_packages)
        """
    def update_organization_configuration(self, *, GraphArn: str, AutoEnable: bool = None) -> None:
        """
        Updates the configuration for the Organizations integration in the current
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/detective.html#Detective.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#update_organization_configuration)
        """
