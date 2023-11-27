"""
Type annotations for ivschat service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ivschat import ivschatClient

    client: ivschatClient = boto3.client("ivschat")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import ChatTokenCapabilityType
from .type_defs import (
    CreateChatTokenResponseTypeDef,
    CreateLoggingConfigurationResponseTypeDef,
    CreateRoomResponseTypeDef,
    DeleteMessageResponseTypeDef,
    DestinationConfigurationTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetRoomResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRoomsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MessageReviewHandlerTypeDef,
    SendEventResponseTypeDef,
    UpdateLoggingConfigurationResponseTypeDef,
    UpdateRoomResponseTypeDef,
)

__all__ = ("ivschatClient",)

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
    PendingVerification: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class ivschatClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ivschatClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#close)
        """
    def create_chat_token(
        self,
        *,
        roomIdentifier: str,
        userId: str,
        attributes: Dict[str, str] = None,
        capabilities: List[ChatTokenCapabilityType] = None,
        sessionDurationInMinutes: int = None
    ) -> CreateChatTokenResponseTypeDef:
        """
        Creates an encrypted token that is used by a chat participant to establish an
        individual WebSocket chat connection to a room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.create_chat_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#create_chat_token)
        """
    def create_logging_configuration(
        self,
        *,
        destinationConfiguration: "DestinationConfigurationTypeDef",
        name: str = None,
        tags: Dict[str, str] = None
    ) -> CreateLoggingConfigurationResponseTypeDef:
        """
        Creates a logging configuration that allows clients to store and record sent
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.create_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#create_logging_configuration)
        """
    def create_room(
        self,
        *,
        loggingConfigurationIdentifiers: List[str] = None,
        maximumMessageLength: int = None,
        maximumMessageRatePerSecond: int = None,
        messageReviewHandler: "MessageReviewHandlerTypeDef" = None,
        name: str = None,
        tags: Dict[str, str] = None
    ) -> CreateRoomResponseTypeDef:
        """
        Creates a room that allows clients to connect and pass messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.create_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#create_room)
        """
    def delete_logging_configuration(self, *, identifier: str) -> None:
        """
        Deletes the specified logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.delete_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#delete_logging_configuration)
        """
    def delete_message(
        self, *, id: str, roomIdentifier: str, reason: str = None
    ) -> DeleteMessageResponseTypeDef:
        """
        Sends an event to a specific room which directs clients to delete a specific
        message; that is, unrender it from view and delete it from the client’s chat
        history.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.delete_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#delete_message)
        """
    def delete_room(self, *, identifier: str) -> None:
        """
        Deletes the specified room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.delete_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#delete_room)
        """
    def disconnect_user(
        self, *, roomIdentifier: str, userId: str, reason: str = None
    ) -> Dict[str, Any]:
        """
        Disconnects all connections using a specified user ID from a room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.disconnect_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#disconnect_user)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#generate_presigned_url)
        """
    def get_logging_configuration(
        self, *, identifier: str
    ) -> GetLoggingConfigurationResponseTypeDef:
        """
        Gets the specified logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.get_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#get_logging_configuration)
        """
    def get_room(self, *, identifier: str) -> GetRoomResponseTypeDef:
        """
        Gets the specified room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.get_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#get_room)
        """
    def list_logging_configurations(
        self, *, maxResults: int = None, nextToken: str = None
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        Gets summary information about all your logging configurations in the AWS region
        where the API request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.list_logging_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#list_logging_configurations)
        """
    def list_rooms(
        self,
        *,
        loggingConfigurationIdentifier: str = None,
        maxResults: int = None,
        messageReviewHandlerUri: str = None,
        name: str = None,
        nextToken: str = None
    ) -> ListRoomsResponseTypeDef:
        """
        Gets summary information about all your rooms in the AWS region where the API
        request is processed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.list_rooms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#list_rooms)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Gets information about AWS tags for the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#list_tags_for_resource)
        """
    def send_event(
        self, *, eventName: str, roomIdentifier: str, attributes: Dict[str, str] = None
    ) -> SendEventResponseTypeDef:
        """
        Sends an event to a room.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.send_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#send_event)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds or updates tags for the AWS resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes tags from the resource with the specified ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#untag_resource)
        """
    def update_logging_configuration(
        self,
        *,
        identifier: str,
        destinationConfiguration: "DestinationConfigurationTypeDef" = None,
        name: str = None
    ) -> UpdateLoggingConfigurationResponseTypeDef:
        """
        Updates a specified logging configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.update_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#update_logging_configuration)
        """
    def update_room(
        self,
        *,
        identifier: str,
        loggingConfigurationIdentifiers: List[str] = None,
        maximumMessageLength: int = None,
        maximumMessageRatePerSecond: int = None,
        messageReviewHandler: "MessageReviewHandlerTypeDef" = None,
        name: str = None
    ) -> UpdateRoomResponseTypeDef:
        """
        Updates a room’s configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ivschat.html#ivschat.Client.update_room)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/client.html#update_room)
        """
