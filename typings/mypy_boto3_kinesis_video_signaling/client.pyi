# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for kinesis-video-signaling service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_signaling import KinesisVideoSignalingChannelsClient

    client: KinesisVideoSignalingChannelsClient = boto3.client("kinesis-video-signaling")
    ```
"""
import sys
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_kinesis_video_signaling.type_defs import (
    GetIceServerConfigResponseTypeDef,
    SendAlexaOfferToMasterResponseTypeDef,
)

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


class KinesisVideoSignalingChannelsClient:
    """
    [KinesisVideoSignalingChannels.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.generate_presigned_url)
        """

    def get_ice_server_config(
        self,
        ChannelARN: str,
        ClientId: str = None,
        Service: Literal["TURN"] = None,
        Username: str = None,
    ) -> GetIceServerConfigResponseTypeDef:
        """
        [Client.get_ice_server_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.get_ice_server_config)
        """

    def send_alexa_offer_to_master(
        self, ChannelARN: str, SenderClientId: str, MessagePayload: str
    ) -> SendAlexaOfferToMasterResponseTypeDef:
        """
        [Client.send_alexa_offer_to_master documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-signaling.html#KinesisVideoSignalingChannels.Client.send_alexa_offer_to_master)
        """
