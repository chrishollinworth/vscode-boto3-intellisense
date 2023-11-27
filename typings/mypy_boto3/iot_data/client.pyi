"""
Type annotations for iot-data service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_data import IoTDataPlaneClient

    client: IoTDataPlaneClient = boto3.client("iot-data")
    ```
"""
import sys
from typing import IO, Any, Dict, Type, Union

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import PayloadFormatIndicatorType
from .paginator import ListRetainedMessagesPaginator
from .type_defs import (
    DeleteThingShadowResponseTypeDef,
    GetRetainedMessageResponseTypeDef,
    GetThingShadowResponseTypeDef,
    ListNamedShadowsForThingResponseTypeDef,
    ListRetainedMessagesResponseTypeDef,
    UpdateThingShadowResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IoTDataPlaneClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    MethodNotAllowedException: Type[BotocoreClientError]
    RequestEntityTooLargeException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    UnsupportedDocumentEncodingException: Type[BotocoreClientError]

class IoTDataPlaneClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTDataPlaneClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#close)
        """
    def delete_thing_shadow(
        self, *, thingName: str, shadowName: str = None
    ) -> DeleteThingShadowResponseTypeDef:
        """
        Deletes the shadow for the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.delete_thing_shadow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#delete_thing_shadow)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#generate_presigned_url)
        """
    def get_retained_message(self, *, topic: str) -> GetRetainedMessageResponseTypeDef:
        """
        Gets the details of a single retained message for the specified topic.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.get_retained_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#get_retained_message)
        """
    def get_thing_shadow(
        self, *, thingName: str, shadowName: str = None
    ) -> GetThingShadowResponseTypeDef:
        """
        Gets the shadow for the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.get_thing_shadow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#get_thing_shadow)
        """
    def list_named_shadows_for_thing(
        self, *, thingName: str, nextToken: str = None, pageSize: int = None
    ) -> ListNamedShadowsForThingResponseTypeDef:
        """
        Lists the shadows for the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.list_named_shadows_for_thing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#list_named_shadows_for_thing)
        """
    def list_retained_messages(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListRetainedMessagesResponseTypeDef:
        """
        Lists summary information about the retained messages stored for the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.list_retained_messages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#list_retained_messages)
        """
    def publish(
        self,
        *,
        topic: str,
        qos: int = None,
        retain: bool = None,
        payload: Union[bytes, IO[bytes], StreamingBody] = None,
        userProperties: str = None,
        payloadFormatIndicator: PayloadFormatIndicatorType = None,
        contentType: str = None,
        responseTopic: str = None,
        correlationData: str = None,
        messageExpiry: int = None
    ) -> None:
        """
        Publishes an MQTT message.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.publish)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#publish)
        """
    def update_thing_shadow(
        self,
        *,
        thingName: str,
        payload: Union[bytes, IO[bytes], StreamingBody],
        shadowName: str = None
    ) -> UpdateThingShadowResponseTypeDef:
        """
        Updates the shadow for the specified thing.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Client.update_thing_shadow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/client.html#update_thing_shadow)
        """
    def get_paginator(
        self, operation_name: Literal["list_retained_messages"]
    ) -> ListRetainedMessagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iot-data.html#IoTDataPlane.Paginator.ListRetainedMessages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/paginators.html#listretainedmessagespaginator)
        """
