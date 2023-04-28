"""
Type annotations for kinesis-video-signaling service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_signaling import KinesisVideoSignalingChannelsClient

    client: KinesisVideoSignalingChannelsClient = boto3.client("kinesis-video-signaling")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import GetIceServerConfigResponseTypeDef, SendAlexaOfferToMasterResponseTypeDef

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("KinesisVideoSignalingChannelsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    ClientLimitExceededException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidClientException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    SessionExpiredException: Type[BotocoreClientError]

class KinesisVideoSignalingChannelsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisVideoSignalingChannelsClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/client.html#generate_presigned_url)
        """
    def get_ice_server_config(
        self,
        *,
        ChannelARN: str,
        ClientId: str = None,
        Service: Literal["TURN"] = None,
        Username: str = None
    ) -> GetIceServerConfigResponseTypeDef:
        """
        Gets the Interactive Connectivity Establishment (ICE) server configuration
        information, including URIs, username, and password which can be used to
        configure the WebRTC connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.get_ice_server_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/client.html#get_ice_server_config)
        """
    def send_alexa_offer_to_master(
        self, *, ChannelARN: str, SenderClientId: str, MessagePayload: str
    ) -> SendAlexaOfferToMasterResponseTypeDef:
        """
        This API allows you to connect WebRTC-enabled devices with Alexa display
        devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.send_alexa_offer_to_master)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_signaling/client.html#send_alexa_offer_to_master)
        """
