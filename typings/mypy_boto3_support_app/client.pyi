"""
Type annotations for support-app service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_support_app import SupportAppClient

    client: SupportAppClient = boto3.client("support-app")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .literals import NotificationSeverityLevelType
from .type_defs import (
    GetAccountAliasResultTypeDef,
    ListSlackChannelConfigurationsResultTypeDef,
    ListSlackWorkspaceConfigurationsResultTypeDef,
    RegisterSlackWorkspaceForOrganizationResultTypeDef,
    UpdateSlackChannelConfigurationResultTypeDef,
)

__all__ = ("SupportAppClient",)

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
    ValidationException: Type[BotocoreClientError]

class SupportAppClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SupportAppClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#close)
        """
    def create_slack_channel_configuration(
        self,
        *,
        channelId: str,
        channelRoleArn: str,
        notifyOnCaseSeverity: NotificationSeverityLevelType,
        teamId: str,
        channelName: str = None,
        notifyOnAddCorrespondenceToCase: bool = None,
        notifyOnCreateOrReopenCase: bool = None,
        notifyOnResolveCase: bool = None
    ) -> Dict[str, Any]:
        """
        Creates a Slack channel configuration for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.create_slack_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#create_slack_channel_configuration)
        """
    def delete_account_alias(self) -> Dict[str, Any]:
        """
        Deletes an alias for an Amazon Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.delete_account_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#delete_account_alias)
        """
    def delete_slack_channel_configuration(self, *, channelId: str, teamId: str) -> Dict[str, Any]:
        """
        Deletes a Slack channel configuration from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.delete_slack_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#delete_slack_channel_configuration)
        """
    def delete_slack_workspace_configuration(self, *, teamId: str) -> Dict[str, Any]:
        """
        Deletes a Slack workspace configuration from your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.delete_slack_workspace_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#delete_slack_workspace_configuration)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#generate_presigned_url)
        """
    def get_account_alias(self) -> GetAccountAliasResultTypeDef:
        """
        Retrieves the alias from an Amazon Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.get_account_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#get_account_alias)
        """
    def list_slack_channel_configurations(
        self, *, nextToken: str = None
    ) -> ListSlackChannelConfigurationsResultTypeDef:
        """
        Lists the Slack channel configurations for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.list_slack_channel_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#list_slack_channel_configurations)
        """
    def list_slack_workspace_configurations(
        self, *, nextToken: str = None
    ) -> ListSlackWorkspaceConfigurationsResultTypeDef:
        """
        Lists the Slack workspace configurations for an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.list_slack_workspace_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#list_slack_workspace_configurations)
        """
    def put_account_alias(self, *, accountAlias: str) -> Dict[str, Any]:
        """
        Creates or updates an individual alias for each Amazon Web Services account ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.put_account_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#put_account_alias)
        """
    def register_slack_workspace_for_organization(
        self, *, teamId: str
    ) -> RegisterSlackWorkspaceForOrganizationResultTypeDef:
        """
        Registers a Slack workspace for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.register_slack_workspace_for_organization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#register_slack_workspace_for_organization)
        """
    def update_slack_channel_configuration(
        self,
        *,
        channelId: str,
        teamId: str,
        channelName: str = None,
        channelRoleArn: str = None,
        notifyOnAddCorrespondenceToCase: bool = None,
        notifyOnCaseSeverity: NotificationSeverityLevelType = None,
        notifyOnCreateOrReopenCase: bool = None,
        notifyOnResolveCase: bool = None
    ) -> UpdateSlackChannelConfigurationResultTypeDef:
        """
        Updates the configuration for a Slack channel, such as case update
        notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.13/reference/services/support-app.html#SupportApp.Client.update_slack_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_support_app/client.html#update_slack_channel_configuration)
        """
