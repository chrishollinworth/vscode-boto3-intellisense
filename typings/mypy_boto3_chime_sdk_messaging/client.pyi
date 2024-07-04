"""
Type annotations for chime-sdk-messaging service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_chime_sdk_messaging import ChimeSDKMessagingClient

    client: ChimeSDKMessagingClient = boto3.client("chime-sdk-messaging")
    ```
"""

from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    SortOrderType,
)
from .type_defs import (
    BatchCreateChannelMembershipResponseTypeDef,
    ChannelFlowCallbackResponseTypeDef,
    ChannelMembershipPreferencesTypeDef,
    ChannelMessageCallbackTypeDef,
    CreateChannelBanResponseTypeDef,
    CreateChannelFlowResponseTypeDef,
    CreateChannelMembershipResponseTypeDef,
    CreateChannelModeratorResponseTypeDef,
    CreateChannelResponseTypeDef,
    DescribeChannelBanResponseTypeDef,
    DescribeChannelFlowResponseTypeDef,
    DescribeChannelMembershipForAppInstanceUserResponseTypeDef,
    DescribeChannelMembershipResponseTypeDef,
    DescribeChannelModeratedByAppInstanceUserResponseTypeDef,
    DescribeChannelModeratorResponseTypeDef,
    DescribeChannelResponseTypeDef,
    ElasticChannelConfigurationTypeDef,
    ExpirationSettingsTypeDef,
    GetChannelMembershipPreferencesResponseTypeDef,
    GetChannelMessageResponseTypeDef,
    GetChannelMessageStatusResponseTypeDef,
    GetMessagingSessionEndpointResponseTypeDef,
    GetMessagingStreamingConfigurationsResponseTypeDef,
    ListChannelBansResponseTypeDef,
    ListChannelFlowsResponseTypeDef,
    ListChannelMembershipsForAppInstanceUserResponseTypeDef,
    ListChannelMembershipsResponseTypeDef,
    ListChannelMessagesResponseTypeDef,
    ListChannelModeratorsResponseTypeDef,
    ListChannelsAssociatedWithChannelFlowResponseTypeDef,
    ListChannelsModeratedByAppInstanceUserResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListSubChannelsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageAttributeValueTypeDef,
    ProcessorTypeDef,
    PushNotificationConfigurationTypeDef,
    PutChannelExpirationSettingsResponseTypeDef,
    PutChannelMembershipPreferencesResponseTypeDef,
    PutMessagingStreamingConfigurationsResponseTypeDef,
    RedactChannelMessageResponseTypeDef,
    SearchChannelsResponseTypeDef,
    SearchFieldTypeDef,
    SendChannelMessageResponseTypeDef,
    StreamingConfigurationTypeDef,
    TagTypeDef,
    TargetTypeDef,
    UpdateChannelFlowResponseTypeDef,
    UpdateChannelMessageResponseTypeDef,
    UpdateChannelReadMarkerResponseTypeDef,
    UpdateChannelResponseTypeDef,
)

__all__ = ("ChimeSDKMessagingClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottledClientException: Type[BotocoreClientError]
    UnauthorizedClientException: Type[BotocoreClientError]

class ChimeSDKMessagingClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ChimeSDKMessagingClient exceptions.
        """

    def associate_channel_flow(
        self, *, ChannelArn: str, ChannelFlowArn: str, ChimeBearer: str
    ) -> None:
        """
        Associates a channel flow with a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.associate_channel_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#associate_channel_flow)
        """

    def batch_create_channel_membership(
        self,
        *,
        ChannelArn: str,
        MemberArns: List[str],
        ChimeBearer: str,
        Type: ChannelMembershipTypeType = None,
        SubChannelId: str = None
    ) -> BatchCreateChannelMembershipResponseTypeDef:
        """
        Adds a specified number of users and bots to a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.batch_create_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#batch_create_channel_membership)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#can_paginate)
        """

    def channel_flow_callback(
        self,
        *,
        CallbackId: str,
        ChannelArn: str,
        ChannelMessage: "ChannelMessageCallbackTypeDef",
        DeleteResource: bool = None
    ) -> ChannelFlowCallbackResponseTypeDef:
        """
        Calls back Amazon Chime SDK messaging with a processing response message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.channel_flow_callback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#channel_flow_callback)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#close)
        """

    def create_channel(
        self,
        *,
        AppInstanceArn: str,
        Name: str,
        ClientRequestToken: str,
        ChimeBearer: str,
        Mode: ChannelModeType = None,
        Privacy: ChannelPrivacyType = None,
        Metadata: str = None,
        Tags: List["TagTypeDef"] = None,
        ChannelId: str = None,
        MemberArns: List[str] = None,
        ModeratorArns: List[str] = None,
        ElasticChannelConfiguration: "ElasticChannelConfigurationTypeDef" = None,
        ExpirationSettings: "ExpirationSettingsTypeDef" = None
    ) -> CreateChannelResponseTypeDef:
        """
        Creates a channel to which you can add users and send messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#create_channel)
        """

    def create_channel_ban(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str
    ) -> CreateChannelBanResponseTypeDef:
        """
        Permanently bans a member from a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.create_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#create_channel_ban)
        """

    def create_channel_flow(
        self,
        *,
        AppInstanceArn: str,
        Processors: List["ProcessorTypeDef"],
        Name: str,
        ClientRequestToken: str,
        Tags: List["TagTypeDef"] = None
    ) -> CreateChannelFlowResponseTypeDef:
        """
        Creates a channel flow, a container for processors.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.create_channel_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#create_channel_flow)
        """

    def create_channel_membership(
        self,
        *,
        ChannelArn: str,
        MemberArn: str,
        Type: ChannelMembershipTypeType,
        ChimeBearer: str,
        SubChannelId: str = None
    ) -> CreateChannelMembershipResponseTypeDef:
        """
        Adds a member to a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.create_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#create_channel_membership)
        """

    def create_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str
    ) -> CreateChannelModeratorResponseTypeDef:
        """
        Creates a new `ChannelModerator`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.create_channel_moderator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#create_channel_moderator)
        """

    def delete_channel(self, *, ChannelArn: str, ChimeBearer: str) -> None:
        """
        Immediately makes a channel and its memberships inaccessible and marks them for
        deletion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#delete_channel)
        """

    def delete_channel_ban(self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str) -> None:
        """
        Removes a member from a channel's ban list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.delete_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#delete_channel_ban)
        """

    def delete_channel_flow(self, *, ChannelFlowArn: str) -> None:
        """
        Deletes a channel flow, an irreversible process.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.delete_channel_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#delete_channel_flow)
        """

    def delete_channel_membership(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str, SubChannelId: str = None
    ) -> None:
        """
        Removes a member from a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.delete_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#delete_channel_membership)
        """

    def delete_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str, SubChannelId: str = None
    ) -> None:
        """
        Deletes a channel message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.delete_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#delete_channel_message)
        """

    def delete_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str
    ) -> None:
        """
        Deletes a channel moderator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.delete_channel_moderator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#delete_channel_moderator)
        """

    def delete_messaging_streaming_configurations(self, *, AppInstanceArn: str) -> None:
        """
        Deletes the streaming configurations for an `AppInstance`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.delete_messaging_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#delete_messaging_streaming_configurations)
        """

    def describe_channel(
        self, *, ChannelArn: str, ChimeBearer: str
    ) -> DescribeChannelResponseTypeDef:
        """
        Returns the full details of a channel in an Amazon Chime `AppInstance`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#describe_channel)
        """

    def describe_channel_ban(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str
    ) -> DescribeChannelBanResponseTypeDef:
        """
        Returns the full details of a channel ban.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.describe_channel_ban)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#describe_channel_ban)
        """

    def describe_channel_flow(self, *, ChannelFlowArn: str) -> DescribeChannelFlowResponseTypeDef:
        """
        Returns the full details of a channel flow in an Amazon Chime `AppInstance`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.describe_channel_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#describe_channel_flow)
        """

    def describe_channel_membership(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str, SubChannelId: str = None
    ) -> DescribeChannelMembershipResponseTypeDef:
        """
        Returns the full details of a user's channel membership.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.describe_channel_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#describe_channel_membership)
        """

    def describe_channel_membership_for_app_instance_user(
        self, *, ChannelArn: str, AppInstanceUserArn: str, ChimeBearer: str
    ) -> DescribeChannelMembershipForAppInstanceUserResponseTypeDef:
        """
        Returns the details of a channel based on the membership of the specified
        `AppInstanceUser` or `AppInstanceBot`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.describe_channel_membership_for_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#describe_channel_membership_for_app_instance_user)
        """

    def describe_channel_moderated_by_app_instance_user(
        self, *, ChannelArn: str, AppInstanceUserArn: str, ChimeBearer: str
    ) -> DescribeChannelModeratedByAppInstanceUserResponseTypeDef:
        """
        Returns the full details of a channel moderated by the specified
        `AppInstanceUser` or `AppInstanceBot`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.describe_channel_moderated_by_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#describe_channel_moderated_by_app_instance_user)
        """

    def describe_channel_moderator(
        self, *, ChannelArn: str, ChannelModeratorArn: str, ChimeBearer: str
    ) -> DescribeChannelModeratorResponseTypeDef:
        """
        Returns the full details of a single ChannelModerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.describe_channel_moderator)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#describe_channel_moderator)
        """

    def disassociate_channel_flow(
        self, *, ChannelArn: str, ChannelFlowArn: str, ChimeBearer: str
    ) -> None:
        """
        Disassociates a channel flow from all its channels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.disassociate_channel_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#disassociate_channel_flow)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#generate_presigned_url)
        """

    def get_channel_membership_preferences(
        self, *, ChannelArn: str, MemberArn: str, ChimeBearer: str
    ) -> GetChannelMembershipPreferencesResponseTypeDef:
        """
        Gets the membership preferences of an `AppInstanceUser` or `AppInstanceBot` for
        the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.get_channel_membership_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#get_channel_membership_preferences)
        """

    def get_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str, SubChannelId: str = None
    ) -> GetChannelMessageResponseTypeDef:
        """
        Gets the full details of a channel message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.get_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#get_channel_message)
        """

    def get_channel_message_status(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str, SubChannelId: str = None
    ) -> GetChannelMessageStatusResponseTypeDef:
        """
        Gets message status for a specified `messageId`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.get_channel_message_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#get_channel_message_status)
        """

    def get_messaging_session_endpoint(self) -> GetMessagingSessionEndpointResponseTypeDef:
        """
        The details of the endpoint for the messaging session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.get_messaging_session_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#get_messaging_session_endpoint)
        """

    def get_messaging_streaming_configurations(
        self, *, AppInstanceArn: str
    ) -> GetMessagingStreamingConfigurationsResponseTypeDef:
        """
        Retrieves the data streaming configuration for an `AppInstance`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.get_messaging_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#get_messaging_streaming_configurations)
        """

    def list_channel_bans(
        self, *, ChannelArn: str, ChimeBearer: str, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelBansResponseTypeDef:
        """
        Lists all the users and bots banned from a particular channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channel_bans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channel_bans)
        """

    def list_channel_flows(
        self, *, AppInstanceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelFlowsResponseTypeDef:
        """
        Returns a paginated lists of all the channel flows created under a single Chime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channel_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channel_flows)
        """

    def list_channel_memberships(
        self,
        *,
        ChannelArn: str,
        ChimeBearer: str,
        Type: ChannelMembershipTypeType = None,
        MaxResults: int = None,
        NextToken: str = None,
        SubChannelId: str = None
    ) -> ListChannelMembershipsResponseTypeDef:
        """
        Lists all channel memberships in a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channel_memberships)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channel_memberships)
        """

    def list_channel_memberships_for_app_instance_user(
        self,
        *,
        ChimeBearer: str,
        AppInstanceUserArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListChannelMembershipsForAppInstanceUserResponseTypeDef:
        """
        Lists all channels that an `AppInstanceUser` or `AppInstanceBot` is a part of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channel_memberships_for_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channel_memberships_for_app_instance_user)
        """

    def list_channel_messages(
        self,
        *,
        ChannelArn: str,
        ChimeBearer: str,
        SortOrder: SortOrderType = None,
        NotBefore: Union[datetime, str] = None,
        NotAfter: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        SubChannelId: str = None
    ) -> ListChannelMessagesResponseTypeDef:
        """
        List all the messages in a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channel_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channel_messages)
        """

    def list_channel_moderators(
        self, *, ChannelArn: str, ChimeBearer: str, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelModeratorsResponseTypeDef:
        """
        Lists all the moderators for a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channel_moderators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channel_moderators)
        """

    def list_channels(
        self,
        *,
        AppInstanceArn: str,
        ChimeBearer: str,
        Privacy: ChannelPrivacyType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListChannelsResponseTypeDef:
        """
        Lists all Channels created under a single Chime App as a paginated list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channels)
        """

    def list_channels_associated_with_channel_flow(
        self, *, ChannelFlowArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListChannelsAssociatedWithChannelFlowResponseTypeDef:
        """
        Lists all channels associated with a specified channel flow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channels_associated_with_channel_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channels_associated_with_channel_flow)
        """

    def list_channels_moderated_by_app_instance_user(
        self,
        *,
        ChimeBearer: str,
        AppInstanceUserArn: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListChannelsModeratedByAppInstanceUserResponseTypeDef:
        """
        A list of the channels moderated by an `AppInstanceUser`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_channels_moderated_by_app_instance_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_channels_moderated_by_app_instance_user)
        """

    def list_sub_channels(
        self, *, ChannelArn: str, ChimeBearer: str, MaxResults: int = None, NextToken: str = None
    ) -> ListSubChannelsResponseTypeDef:
        """
        Lists all the SubChannels in an elastic channel when given a channel ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_sub_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_sub_channels)
        """

    def list_tags_for_resource(self, *, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags applied to an Amazon Chime SDK messaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#list_tags_for_resource)
        """

    def put_channel_expiration_settings(
        self,
        *,
        ChannelArn: str,
        ChimeBearer: str = None,
        ExpirationSettings: "ExpirationSettingsTypeDef" = None
    ) -> PutChannelExpirationSettingsResponseTypeDef:
        """
        Sets the number of days before the channel is automatically deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.put_channel_expiration_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#put_channel_expiration_settings)
        """

    def put_channel_membership_preferences(
        self,
        *,
        ChannelArn: str,
        MemberArn: str,
        ChimeBearer: str,
        Preferences: "ChannelMembershipPreferencesTypeDef"
    ) -> PutChannelMembershipPreferencesResponseTypeDef:
        """
        Sets the membership preferences of an `AppInstanceUser` or `AppInstanceBot` for
        the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.put_channel_membership_preferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#put_channel_membership_preferences)
        """

    def put_messaging_streaming_configurations(
        self, *, AppInstanceArn: str, StreamingConfigurations: List["StreamingConfigurationTypeDef"]
    ) -> PutMessagingStreamingConfigurationsResponseTypeDef:
        """
        Sets the data streaming configuration for an `AppInstance`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.put_messaging_streaming_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#put_messaging_streaming_configurations)
        """

    def redact_channel_message(
        self, *, ChannelArn: str, MessageId: str, ChimeBearer: str, SubChannelId: str = None
    ) -> RedactChannelMessageResponseTypeDef:
        """
        Redacts message content, but not metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.redact_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#redact_channel_message)
        """

    def search_channels(
        self,
        *,
        Fields: List["SearchFieldTypeDef"],
        ChimeBearer: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> SearchChannelsResponseTypeDef:
        """
        Allows the `ChimeBearer` to search channels by channel members.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.search_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#search_channels)
        """

    def send_channel_message(
        self,
        *,
        ChannelArn: str,
        Content: str,
        Type: ChannelMessageTypeType,
        Persistence: ChannelMessagePersistenceTypeType,
        ClientRequestToken: str,
        ChimeBearer: str,
        Metadata: str = None,
        PushNotification: "PushNotificationConfigurationTypeDef" = None,
        MessageAttributes: Dict[str, "MessageAttributeValueTypeDef"] = None,
        SubChannelId: str = None,
        ContentType: str = None,
        Target: List["TargetTypeDef"] = None
    ) -> SendChannelMessageResponseTypeDef:
        """
        Sends a message to a particular channel that the member is a part of.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.send_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#send_channel_message)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> None:
        """
        Applies the specified tags to the specified Amazon Chime SDK messaging resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> None:
        """
        Removes the specified tags from the specified Amazon Chime SDK messaging
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#untag_resource)
        """

    def update_channel(
        self,
        *,
        ChannelArn: str,
        ChimeBearer: str,
        Name: str = None,
        Mode: ChannelModeType = None,
        Metadata: str = None
    ) -> UpdateChannelResponseTypeDef:
        """
        Update a channel's attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#update_channel)
        """

    def update_channel_flow(
        self, *, ChannelFlowArn: str, Processors: List["ProcessorTypeDef"], Name: str
    ) -> UpdateChannelFlowResponseTypeDef:
        """
        Updates channel flow attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.update_channel_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#update_channel_flow)
        """

    def update_channel_message(
        self,
        *,
        ChannelArn: str,
        MessageId: str,
        Content: str,
        ChimeBearer: str,
        Metadata: str = None,
        SubChannelId: str = None,
        ContentType: str = None
    ) -> UpdateChannelMessageResponseTypeDef:
        """
        Updates the content of a message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.update_channel_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#update_channel_message)
        """

    def update_channel_read_marker(
        self, *, ChannelArn: str, ChimeBearer: str
    ) -> UpdateChannelReadMarkerResponseTypeDef:
        """
        The details of the time when a user last read messages in a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/chime-sdk-messaging.html#ChimeSDKMessaging.Client.update_channel_read_marker)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/client.html#update_channel_read_marker)
        """
