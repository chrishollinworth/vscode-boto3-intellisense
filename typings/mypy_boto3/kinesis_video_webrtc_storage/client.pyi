"""
Type annotations for kinesis-video-webrtc-storage service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_webrtc_storage/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_webrtc_storage import KinesisVideoWebRTCStorageClient

    client: KinesisVideoWebRTCStorageClient = boto3.client("kinesis-video-webrtc-storage")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

__all__ = ("KinesisVideoWebRTCStorageClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientLimitExceededException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class KinesisVideoWebRTCStorageClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-webrtc-storage.html#KinesisVideoWebRTCStorage.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_webrtc_storage/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisVideoWebRTCStorageClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-webrtc-storage.html#KinesisVideoWebRTCStorage.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_webrtc_storage/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-webrtc-storage.html#KinesisVideoWebRTCStorage.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_webrtc_storage/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-webrtc-storage.html#KinesisVideoWebRTCStorage.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_webrtc_storage/client.html#generate_presigned_url)
        """
    def join_storage_session(self, *, channelArn: str) -> None:
        """
        Join the ongoing one way-video and/or multi-way audio WebRTC session as a video
        producing device for an input channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/kinesis-video-webrtc-storage.html#KinesisVideoWebRTCStorage.Client.join_storage_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_webrtc_storage/client.html#join_storage_session)
        """
