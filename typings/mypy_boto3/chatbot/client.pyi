"""
Type annotations for chatbot service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chatbot.client import ChatbotClient

    session = Session()
    client: ChatbotClient = session.client("chatbot")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeChimeWebhookConfigurationsPaginator,
    DescribeSlackChannelConfigurationsPaginator,
    DescribeSlackUserIdentitiesPaginator,
    DescribeSlackWorkspacesPaginator,
    ListAssociationsPaginator,
    ListCustomActionsPaginator,
    ListMicrosoftTeamsChannelConfigurationsPaginator,
    ListMicrosoftTeamsConfiguredTeamsPaginator,
    ListMicrosoftTeamsUserIdentitiesPaginator,
)
from .type_defs import (
    AssociateToConfigurationRequestTypeDef,
    CreateChimeWebhookConfigurationRequestTypeDef,
    CreateChimeWebhookConfigurationResultTypeDef,
    CreateCustomActionRequestTypeDef,
    CreateCustomActionResultTypeDef,
    CreateSlackChannelConfigurationRequestTypeDef,
    CreateSlackChannelConfigurationResultTypeDef,
    CreateTeamsChannelConfigurationRequestTypeDef,
    CreateTeamsChannelConfigurationResultTypeDef,
    DeleteChimeWebhookConfigurationRequestTypeDef,
    DeleteCustomActionRequestTypeDef,
    DeleteMicrosoftTeamsUserIdentityRequestTypeDef,
    DeleteSlackChannelConfigurationRequestTypeDef,
    DeleteSlackUserIdentityRequestTypeDef,
    DeleteSlackWorkspaceAuthorizationRequestTypeDef,
    DeleteTeamsChannelConfigurationRequestTypeDef,
    DeleteTeamsConfiguredTeamRequestTypeDef,
    DescribeChimeWebhookConfigurationsRequestTypeDef,
    DescribeChimeWebhookConfigurationsResultTypeDef,
    DescribeSlackChannelConfigurationsRequestTypeDef,
    DescribeSlackChannelConfigurationsResultTypeDef,
    DescribeSlackUserIdentitiesRequestTypeDef,
    DescribeSlackUserIdentitiesResultTypeDef,
    DescribeSlackWorkspacesRequestTypeDef,
    DescribeSlackWorkspacesResultTypeDef,
    DisassociateFromConfigurationRequestTypeDef,
    GetAccountPreferencesResultTypeDef,
    GetCustomActionRequestTypeDef,
    GetCustomActionResultTypeDef,
    GetTeamsChannelConfigurationRequestTypeDef,
    GetTeamsChannelConfigurationResultTypeDef,
    ListAssociationsRequestTypeDef,
    ListAssociationsResultTypeDef,
    ListCustomActionsRequestTypeDef,
    ListCustomActionsResultTypeDef,
    ListMicrosoftTeamsConfiguredTeamsRequestTypeDef,
    ListMicrosoftTeamsConfiguredTeamsResultTypeDef,
    ListMicrosoftTeamsUserIdentitiesRequestTypeDef,
    ListMicrosoftTeamsUserIdentitiesResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTeamsChannelConfigurationsRequestTypeDef,
    ListTeamsChannelConfigurationsResultTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAccountPreferencesRequestTypeDef,
    UpdateAccountPreferencesResultTypeDef,
    UpdateChimeWebhookConfigurationRequestTypeDef,
    UpdateChimeWebhookConfigurationResultTypeDef,
    UpdateCustomActionRequestTypeDef,
    UpdateCustomActionResultTypeDef,
    UpdateSlackChannelConfigurationRequestTypeDef,
    UpdateSlackChannelConfigurationResultTypeDef,
    UpdateTeamsChannelConfigurationRequestTypeDef,
    UpdateTeamsChannelConfigurationResultTypeDef,
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

__all__ = ("ChatbotClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    CreateChimeWebhookConfigurationException: Type[BotocoreClientError]
    CreateSlackChannelConfigurationException: Type[BotocoreClientError]
    CreateTeamsChannelConfigurationException: Type[BotocoreClientError]
    DeleteChimeWebhookConfigurationException: Type[BotocoreClientError]
    DeleteMicrosoftTeamsUserIdentityException: Type[BotocoreClientError]
    DeleteSlackChannelConfigurationException: Type[BotocoreClientError]
    DeleteSlackUserIdentityException: Type[BotocoreClientError]
    DeleteSlackWorkspaceAuthorizationFault: Type[BotocoreClientError]
    DeleteTeamsChannelConfigurationException: Type[BotocoreClientError]
    DeleteTeamsConfiguredTeamException: Type[BotocoreClientError]
    DescribeChimeWebhookConfigurationsException: Type[BotocoreClientError]
    DescribeSlackChannelConfigurationsException: Type[BotocoreClientError]
    DescribeSlackUserIdentitiesException: Type[BotocoreClientError]
    DescribeSlackWorkspacesException: Type[BotocoreClientError]
    GetAccountPreferencesException: Type[BotocoreClientError]
    GetTeamsChannelConfigurationException: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ListMicrosoftTeamsConfiguredTeamsException: Type[BotocoreClientError]
    ListMicrosoftTeamsUserIdentitiesException: Type[BotocoreClientError]
    ListTeamsChannelConfigurationsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UpdateAccountPreferencesException: Type[BotocoreClientError]
    UpdateChimeWebhookConfigurationException: Type[BotocoreClientError]
    UpdateSlackChannelConfigurationException: Type[BotocoreClientError]
    UpdateTeamsChannelConfigurationException: Type[BotocoreClientError]

class ChatbotClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot.html#Chatbot.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChatbotClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot.html#Chatbot.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#generate_presigned_url)
        """

    def associate_to_configuration(
        self, **kwargs: Unpack[AssociateToConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Links a resource (for example, a custom action) to a channel configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/associate_to_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#associate_to_configuration)
        """

    def create_chime_webhook_configuration(
        self, **kwargs: Unpack[CreateChimeWebhookConfigurationRequestTypeDef]
    ) -> CreateChimeWebhookConfigurationResultTypeDef:
        """
        Creates an AWS Chatbot configuration for Amazon Chime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/create_chime_webhook_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#create_chime_webhook_configuration)
        """

    def create_custom_action(
        self, **kwargs: Unpack[CreateCustomActionRequestTypeDef]
    ) -> CreateCustomActionResultTypeDef:
        """
        Creates a custom action that can be invoked as an alias or as a button on a
        notification.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/create_custom_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#create_custom_action)
        """

    def create_microsoft_teams_channel_configuration(
        self, **kwargs: Unpack[CreateTeamsChannelConfigurationRequestTypeDef]
    ) -> CreateTeamsChannelConfigurationResultTypeDef:
        """
        Creates an AWS Chatbot configuration for Microsoft Teams.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/create_microsoft_teams_channel_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#create_microsoft_teams_channel_configuration)
        """

    def create_slack_channel_configuration(
        self, **kwargs: Unpack[CreateSlackChannelConfigurationRequestTypeDef]
    ) -> CreateSlackChannelConfigurationResultTypeDef:
        """
        Creates an AWS Chatbot confugration for Slack.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/create_slack_channel_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#create_slack_channel_configuration)
        """

    def delete_chime_webhook_configuration(
        self, **kwargs: Unpack[DeleteChimeWebhookConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Amazon Chime webhook configuration for AWS Chatbot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/delete_chime_webhook_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#delete_chime_webhook_configuration)
        """

    def delete_custom_action(
        self, **kwargs: Unpack[DeleteCustomActionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a custom action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/delete_custom_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#delete_custom_action)
        """

    def delete_microsoft_teams_channel_configuration(
        self, **kwargs: Unpack[DeleteTeamsChannelConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Microsoft Teams channel configuration for AWS Chatbot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/delete_microsoft_teams_channel_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#delete_microsoft_teams_channel_configuration)
        """

    def delete_microsoft_teams_configured_team(
        self, **kwargs: Unpack[DeleteTeamsConfiguredTeamRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the Microsoft Teams team authorization allowing for channels to be
        configured in that Microsoft Teams team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/delete_microsoft_teams_configured_team.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#delete_microsoft_teams_configured_team)
        """

    def delete_microsoft_teams_user_identity(
        self, **kwargs: Unpack[DeleteMicrosoftTeamsUserIdentityRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Identifes a user level permission for a channel configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/delete_microsoft_teams_user_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#delete_microsoft_teams_user_identity)
        """

    def delete_slack_channel_configuration(
        self, **kwargs: Unpack[DeleteSlackChannelConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Slack channel configuration for AWS Chatbot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/delete_slack_channel_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#delete_slack_channel_configuration)
        """

    def delete_slack_user_identity(
        self, **kwargs: Unpack[DeleteSlackUserIdentityRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a user level permission for a Slack channel configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/delete_slack_user_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#delete_slack_user_identity)
        """

    def delete_slack_workspace_authorization(
        self, **kwargs: Unpack[DeleteSlackWorkspaceAuthorizationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the Slack workspace authorization that allows channels to be configured
        in that workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/delete_slack_workspace_authorization.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#delete_slack_workspace_authorization)
        """

    def describe_chime_webhook_configurations(
        self, **kwargs: Unpack[DescribeChimeWebhookConfigurationsRequestTypeDef]
    ) -> DescribeChimeWebhookConfigurationsResultTypeDef:
        """
        Lists Amazon Chime webhook configurations optionally filtered by
        ChatConfigurationArn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/describe_chime_webhook_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#describe_chime_webhook_configurations)
        """

    def describe_slack_channel_configurations(
        self, **kwargs: Unpack[DescribeSlackChannelConfigurationsRequestTypeDef]
    ) -> DescribeSlackChannelConfigurationsResultTypeDef:
        """
        Lists Slack channel configurations optionally filtered by ChatConfigurationArn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/describe_slack_channel_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#describe_slack_channel_configurations)
        """

    def describe_slack_user_identities(
        self, **kwargs: Unpack[DescribeSlackUserIdentitiesRequestTypeDef]
    ) -> DescribeSlackUserIdentitiesResultTypeDef:
        """
        Lists all Slack user identities with a mapped role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/describe_slack_user_identities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#describe_slack_user_identities)
        """

    def describe_slack_workspaces(
        self, **kwargs: Unpack[DescribeSlackWorkspacesRequestTypeDef]
    ) -> DescribeSlackWorkspacesResultTypeDef:
        """
        List all authorized Slack workspaces connected to the AWS Account onboarded
        with AWS Chatbot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/describe_slack_workspaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#describe_slack_workspaces)
        """

    def disassociate_from_configuration(
        self, **kwargs: Unpack[DisassociateFromConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Unlink a resource, for example a custom action, from a channel configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/disassociate_from_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#disassociate_from_configuration)
        """

    def get_account_preferences(self) -> GetAccountPreferencesResultTypeDef:
        """
        Returns AWS Chatbot account preferences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_account_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_account_preferences)
        """

    def get_custom_action(
        self, **kwargs: Unpack[GetCustomActionRequestTypeDef]
    ) -> GetCustomActionResultTypeDef:
        """
        Returns a custom action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_custom_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_custom_action)
        """

    def get_microsoft_teams_channel_configuration(
        self, **kwargs: Unpack[GetTeamsChannelConfigurationRequestTypeDef]
    ) -> GetTeamsChannelConfigurationResultTypeDef:
        """
        Returns a Microsoft Teams channel configuration in an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_microsoft_teams_channel_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_microsoft_teams_channel_configuration)
        """

    def list_associations(
        self, **kwargs: Unpack[ListAssociationsRequestTypeDef]
    ) -> ListAssociationsResultTypeDef:
        """
        Lists resources associated with a channel configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/list_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#list_associations)
        """

    def list_custom_actions(
        self, **kwargs: Unpack[ListCustomActionsRequestTypeDef]
    ) -> ListCustomActionsResultTypeDef:
        """
        Lists custom actions defined in this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/list_custom_actions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#list_custom_actions)
        """

    def list_microsoft_teams_channel_configurations(
        self, **kwargs: Unpack[ListTeamsChannelConfigurationsRequestTypeDef]
    ) -> ListTeamsChannelConfigurationsResultTypeDef:
        """
        Lists all AWS Chatbot Microsoft Teams channel configurations in an AWS account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/list_microsoft_teams_channel_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#list_microsoft_teams_channel_configurations)
        """

    def list_microsoft_teams_configured_teams(
        self, **kwargs: Unpack[ListMicrosoftTeamsConfiguredTeamsRequestTypeDef]
    ) -> ListMicrosoftTeamsConfiguredTeamsResultTypeDef:
        """
        Lists all authorized Microsoft Teams for an AWS Account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/list_microsoft_teams_configured_teams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#list_microsoft_teams_configured_teams)
        """

    def list_microsoft_teams_user_identities(
        self, **kwargs: Unpack[ListMicrosoftTeamsUserIdentitiesRequestTypeDef]
    ) -> ListMicrosoftTeamsUserIdentitiesResultTypeDef:
        """
        A list all Microsoft Teams user identities with a mapped role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/list_microsoft_teams_user_identities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#list_microsoft_teams_user_identities)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all of the tags associated with the Amazon Resource Name (ARN) that you
        specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Attaches a key-value pair to a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Detaches a key-value pair from a resource, as identified by its Amazon Resource
        Name (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#untag_resource)
        """

    def update_account_preferences(
        self, **kwargs: Unpack[UpdateAccountPreferencesRequestTypeDef]
    ) -> UpdateAccountPreferencesResultTypeDef:
        """
        Updates AWS Chatbot account preferences.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/update_account_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#update_account_preferences)
        """

    def update_chime_webhook_configuration(
        self, **kwargs: Unpack[UpdateChimeWebhookConfigurationRequestTypeDef]
    ) -> UpdateChimeWebhookConfigurationResultTypeDef:
        """
        Updates a Amazon Chime webhook configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/update_chime_webhook_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#update_chime_webhook_configuration)
        """

    def update_custom_action(
        self, **kwargs: Unpack[UpdateCustomActionRequestTypeDef]
    ) -> UpdateCustomActionResultTypeDef:
        """
        Updates a custom action.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/update_custom_action.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#update_custom_action)
        """

    def update_microsoft_teams_channel_configuration(
        self, **kwargs: Unpack[UpdateTeamsChannelConfigurationRequestTypeDef]
    ) -> UpdateTeamsChannelConfigurationResultTypeDef:
        """
        Updates an Microsoft Teams channel configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/update_microsoft_teams_channel_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#update_microsoft_teams_channel_configuration)
        """

    def update_slack_channel_configuration(
        self, **kwargs: Unpack[UpdateSlackChannelConfigurationRequestTypeDef]
    ) -> UpdateSlackChannelConfigurationResultTypeDef:
        """
        Updates a Slack channel configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/update_slack_channel_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#update_slack_channel_configuration)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_chime_webhook_configurations"]
    ) -> DescribeChimeWebhookConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_slack_channel_configurations"]
    ) -> DescribeSlackChannelConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_slack_user_identities"]
    ) -> DescribeSlackUserIdentitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_slack_workspaces"]
    ) -> DescribeSlackWorkspacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associations"]
    ) -> ListAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_custom_actions"]
    ) -> ListCustomActionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_microsoft_teams_channel_configurations"]
    ) -> ListMicrosoftTeamsChannelConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_microsoft_teams_configured_teams"]
    ) -> ListMicrosoftTeamsConfiguredTeamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_microsoft_teams_user_identities"]
    ) -> ListMicrosoftTeamsUserIdentitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/chatbot/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client/#get_paginator)
        """
