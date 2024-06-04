"""
Type annotations for chatbot service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_chatbot import ChatbotClient

    client: ChatbotClient = boto3.client("chatbot")
    ```
"""

from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    CreateChimeWebhookConfigurationResultTypeDef,
    CreateSlackChannelConfigurationResultTypeDef,
    CreateTeamsChannelConfigurationResultTypeDef,
    DescribeChimeWebhookConfigurationsResultTypeDef,
    DescribeSlackChannelConfigurationsResultTypeDef,
    DescribeSlackUserIdentitiesResultTypeDef,
    DescribeSlackWorkspacesResultTypeDef,
    GetAccountPreferencesResultTypeDef,
    GetTeamsChannelConfigurationResultTypeDef,
    ListMicrosoftTeamsConfiguredTeamsResultTypeDef,
    ListMicrosoftTeamsUserIdentitiesResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTeamsChannelConfigurationsResultTypeDef,
    TagTypeDef,
    UpdateAccountPreferencesResultTypeDef,
    UpdateChimeWebhookConfigurationResultTypeDef,
    UpdateSlackChannelConfigurationResultTypeDef,
    UpdateTeamsChannelConfigurationResultTypeDef,
)

__all__ = ("ChatbotClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    UpdateAccountPreferencesException: Type[BotocoreClientError]
    UpdateChimeWebhookConfigurationException: Type[BotocoreClientError]
    UpdateSlackChannelConfigurationException: Type[BotocoreClientError]
    UpdateTeamsChannelConfigurationException: Type[BotocoreClientError]

class ChatbotClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChatbotClient exceptions.
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#close)
        """

    def create_chime_webhook_configuration(
        self,
        *,
        WebhookDescription: str,
        WebhookUrl: str,
        SnsTopicArns: List[str],
        IamRoleArn: str,
        ConfigurationName: str,
        LoggingLevel: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateChimeWebhookConfigurationResultTypeDef:
        """
        Creates Chime Webhook Configuration See also: `AWS API Documentation <https://do
        cs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/CreateChimeWebhookConfiguration>`_ **Request Syntax** response =
        client.create_chime_webhook_configuration( WebhookDescription='string',
        WebhookUrl...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.create_chime_webhook_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#create_chime_webhook_configuration)
        """

    def create_microsoft_teams_channel_configuration(
        self,
        *,
        ChannelId: str,
        TeamId: str,
        TenantId: str,
        IamRoleArn: str,
        ConfigurationName: str,
        ChannelName: str = None,
        TeamName: str = None,
        SnsTopicArns: List[str] = None,
        LoggingLevel: str = None,
        GuardrailPolicyArns: List[str] = None,
        UserAuthorizationRequired: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateTeamsChannelConfigurationResultTypeDef:
        """
        Creates MS Teams Channel Configuration See also: `AWS API Documentation <https:/
        /docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/CreateMicrosoftTeamsChannelConfiguration>`_ **Request Syntax** response =
        client.create_microsoft_teams_channel_configuration( ChannelId='string', ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.create_microsoft_teams_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#create_microsoft_teams_channel_configuration)
        """

    def create_slack_channel_configuration(
        self,
        *,
        SlackTeamId: str,
        SlackChannelId: str,
        IamRoleArn: str,
        ConfigurationName: str,
        SlackChannelName: str = None,
        SnsTopicArns: List[str] = None,
        LoggingLevel: str = None,
        GuardrailPolicyArns: List[str] = None,
        UserAuthorizationRequired: bool = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateSlackChannelConfigurationResultTypeDef:
        """
        Creates Slack Channel Configuration See also: `AWS API Documentation <https://do
        cs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/CreateSlackChannelConfiguration>`_ **Request Syntax** response =
        client.create_slack_channel_configuration( SlackTeamId='string',
        SlackChannelId='s...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.create_slack_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#create_slack_channel_configuration)
        """

    def delete_chime_webhook_configuration(self, *, ChatConfigurationArn: str) -> Dict[str, Any]:
        """
        Deletes a Chime Webhook Configuration See also: `AWS API Documentation <https://
        docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/DeleteChimeWebhookConfiguration>`_ **Request Syntax** response =
        client.delete_chime_webhook_configuration( ChatConfigurationArn='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.delete_chime_webhook_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#delete_chime_webhook_configuration)
        """

    def delete_microsoft_teams_channel_configuration(
        self, *, ChatConfigurationArn: str
    ) -> Dict[str, Any]:
        """
        Deletes MS Teams Channel Configuration See also: `AWS API Documentation <https:/
        /docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/DeleteMicrosoftTeamsChannelConfiguration>`_ **Request Syntax** response =
        client.delete_microsoft_teams_channel_configuration( ChatConfigurationArn='s...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.delete_microsoft_teams_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#delete_microsoft_teams_channel_configuration)
        """

    def delete_microsoft_teams_configured_team(self, *, TeamId: str) -> Dict[str, Any]:
        """
        Deletes the Microsoft Teams team authorization allowing for channels to be
        configured in that Microsoft Teams team.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.delete_microsoft_teams_configured_team)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#delete_microsoft_teams_configured_team)
        """

    def delete_microsoft_teams_user_identity(
        self, *, ChatConfigurationArn: str, UserId: str
    ) -> Dict[str, Any]:
        """
        Deletes a Teams user identity See also: `AWS API Documentation <https://docs.aws
        .amazon.com/goto/WebAPI/chatbot-2017-10-11/DeleteMicrosoftTeamsUserIdentity>`_
        **Request Syntax** response = client.delete_microsoft_teams_user_identity(
        ChatConfigurationArn='string', UserId='str...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.delete_microsoft_teams_user_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#delete_microsoft_teams_user_identity)
        """

    def delete_slack_channel_configuration(self, *, ChatConfigurationArn: str) -> Dict[str, Any]:
        """
        Deletes Slack Channel Configuration See also: `AWS API Documentation <https://do
        cs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/DeleteSlackChannelConfiguration>`_ **Request Syntax** response =
        client.delete_slack_channel_configuration( ChatConfigurationArn='string' ).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.delete_slack_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#delete_slack_channel_configuration)
        """

    def delete_slack_user_identity(
        self, *, ChatConfigurationArn: str, SlackTeamId: str, SlackUserId: str
    ) -> Dict[str, Any]:
        """
        Deletes a Slack user identity See also: `AWS API Documentation <https://docs.aws
        .amazon.com/goto/WebAPI/chatbot-2017-10-11/DeleteSlackUserIdentity>`_ **Request
        Syntax** response = client.delete_slack_user_identity(
        ChatConfigurationArn='string', SlackTeamId='string', Sl...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.delete_slack_user_identity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#delete_slack_user_identity)
        """

    def delete_slack_workspace_authorization(self, *, SlackTeamId: str) -> Dict[str, Any]:
        """
        Deletes the Slack workspace authorization that allows channels to be configured
        in that workspace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.delete_slack_workspace_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#delete_slack_workspace_authorization)
        """

    def describe_chime_webhook_configurations(
        self, *, MaxResults: int = None, NextToken: str = None, ChatConfigurationArn: str = None
    ) -> DescribeChimeWebhookConfigurationsResultTypeDef:
        """
        Lists Chime Webhook Configurations optionally filtered by ChatConfigurationArn
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chatbo
        t-2017-10-11/DescribeChimeWebhookConfigurations>`_ **Request Syntax** response =
        client.describe_chime_webhook_configurations( ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.describe_chime_webhook_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#describe_chime_webhook_configurations)
        """

    def describe_slack_channel_configurations(
        self, *, MaxResults: int = None, NextToken: str = None, ChatConfigurationArn: str = None
    ) -> DescribeSlackChannelConfigurationsResultTypeDef:
        """
        Lists Slack Channel Configurations optionally filtered by ChatConfigurationArn
        See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chatbo
        t-2017-10-11/DescribeSlackChannelConfigurations>`_ **Request Syntax** response =
        client.describe_slack_channel_configurations( ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.describe_slack_channel_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#describe_slack_channel_configurations)
        """

    def describe_slack_user_identities(
        self, *, ChatConfigurationArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeSlackUserIdentitiesResultTypeDef:
        """
        Lists all Slack user identities with a mapped role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.describe_slack_user_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#describe_slack_user_identities)
        """

    def describe_slack_workspaces(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> DescribeSlackWorkspacesResultTypeDef:
        """
        Lists all authorized Slack Workspaces for AWS Account See also: `AWS API
        Documentation <https://docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/DescribeSlackWorkspaces>`_ **Request Syntax** response =
        client.describe_slack_workspaces( MaxResults=123, NextToken='string' )...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.describe_slack_workspaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#describe_slack_workspaces)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#generate_presigned_url)
        """

    def get_account_preferences(self) -> GetAccountPreferencesResultTypeDef:
        """
        Get Chatbot account level preferences See also: `AWS API Documentation <https://
        docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-11/GetAccountPreferences>`_
        **Request Syntax** response = client.get_account_preferences().

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.get_account_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#get_account_preferences)
        """

    def get_microsoft_teams_channel_configuration(
        self, *, ChatConfigurationArn: str
    ) -> GetTeamsChannelConfigurationResultTypeDef:
        """
        Get a single MS Teams Channel Configurations See also: `AWS API Documentation <h
        ttps://docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/GetMicrosoftTeamsChannelConfiguration>`_ **Request Syntax** response =
        client.get_microsoft_teams_channel_configuration( ChatConfigurationArn='s...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.get_microsoft_teams_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#get_microsoft_teams_channel_configuration)
        """

    def list_microsoft_teams_channel_configurations(
        self, *, MaxResults: int = None, NextToken: str = None, TeamId: str = None
    ) -> ListTeamsChannelConfigurationsResultTypeDef:
        """
        Lists MS Teams Channel Configurations optionally filtered by TeamId See also:
        `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/ListMicrosoftTeamsChannelConfigurations>`_ **Request Syntax** response =
        client.list_microsoft_teams_channel_configurations( ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.list_microsoft_teams_channel_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#list_microsoft_teams_channel_configurations)
        """

    def list_microsoft_teams_configured_teams(
        self, *, MaxResults: int = None, NextToken: str = None
    ) -> ListMicrosoftTeamsConfiguredTeamsResultTypeDef:
        """
        Lists all authorized MS teams for AWS Account See also: `AWS API Documentation <
        https://docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/ListMicrosoftTeamsConfiguredTeams>`_ **Request Syntax** response =
        client.list_microsoft_teams_configured_teams( MaxResults=123, NextToke...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.list_microsoft_teams_configured_teams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#list_microsoft_teams_configured_teams)
        """

    def list_microsoft_teams_user_identities(
        self, *, ChatConfigurationArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListMicrosoftTeamsUserIdentitiesResultTypeDef:
        """
        Lists all Microsoft Teams user identities with a mapped role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.list_microsoft_teams_user_identities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#list_microsoft_teams_user_identities)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the list of tags applied to a configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#list_tags_for_resource)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Applies the supplied tags to a configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the supplied tags from a configuration See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-11/UntagResource>`_
        **Request Syntax** response = client.untag_resource( ResourceARN='string',
        TagKeys=[ 'string', ] ) ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#untag_resource)
        """

    def update_account_preferences(
        self, *, UserAuthorizationRequired: bool = None, TrainingDataCollectionEnabled: bool = None
    ) -> UpdateAccountPreferencesResultTypeDef:
        """
        Update Chatbot account level preferences See also: `AWS API Documentation <https
        ://docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/UpdateAccountPreferences>`_ **Request Syntax** response =
        client.update_account_preferences( UserAuthorizationRequired=True|False,
        TrainingDat...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.update_account_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#update_account_preferences)
        """

    def update_chime_webhook_configuration(
        self,
        *,
        ChatConfigurationArn: str,
        WebhookDescription: str = None,
        WebhookUrl: str = None,
        SnsTopicArns: List[str] = None,
        IamRoleArn: str = None,
        LoggingLevel: str = None
    ) -> UpdateChimeWebhookConfigurationResultTypeDef:
        """
        Updates a Chime Webhook Configuration See also: `AWS API Documentation <https://
        docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/UpdateChimeWebhookConfiguration>`_ **Request Syntax** response =
        client.update_chime_webhook_configuration( ChatConfigurationArn='string',
        Webhoo...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.update_chime_webhook_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#update_chime_webhook_configuration)
        """

    def update_microsoft_teams_channel_configuration(
        self,
        *,
        ChatConfigurationArn: str,
        ChannelId: str,
        ChannelName: str = None,
        SnsTopicArns: List[str] = None,
        IamRoleArn: str = None,
        LoggingLevel: str = None,
        GuardrailPolicyArns: List[str] = None,
        UserAuthorizationRequired: bool = None
    ) -> UpdateTeamsChannelConfigurationResultTypeDef:
        """
        Updates MS Teams Channel Configuration See also: `AWS API Documentation <https:/
        /docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/UpdateMicrosoftTeamsChannelConfiguration>`_ **Request Syntax** response =
        client.update_microsoft_teams_channel_configuration( ChatConfigurationArn='s...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.update_microsoft_teams_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#update_microsoft_teams_channel_configuration)
        """

    def update_slack_channel_configuration(
        self,
        *,
        ChatConfigurationArn: str,
        SlackChannelId: str,
        SlackChannelName: str = None,
        SnsTopicArns: List[str] = None,
        IamRoleArn: str = None,
        LoggingLevel: str = None,
        GuardrailPolicyArns: List[str] = None,
        UserAuthorizationRequired: bool = None
    ) -> UpdateSlackChannelConfigurationResultTypeDef:
        """
        Updates Slack Channel Configuration See also: `AWS API Documentation <https://do
        cs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-
        11/UpdateSlackChannelConfiguration>`_ **Request Syntax** response =
        client.update_slack_channel_configuration( ChatConfigurationArn='string',
        SlackCha...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/chatbot.html#Chatbot.Client.update_slack_channel_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chatbot/client.html#update_slack_channel_configuration)
        """
