# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for kinesis-video-media service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_media import KinesisVideoMediaClient

    client: KinesisVideoMediaClient = boto3.client("kinesis-video-media")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_kinesis_video_media.type_defs import GetMediaOutputTypeDef, StartSelectorTypeDef

__all__ = ("KinesisVideoMediaClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ClientLimitExceededException: Type[BotocoreClientError]
    ConnectionLimitExceededException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidEndpointException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class KinesisVideoMediaClient:
    """
    [KinesisVideoMedia.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.generate_presigned_url)
        """

    def get_media(
        self, StartSelector: StartSelectorTypeDef, StreamName: str = None, StreamARN: str = None
    ) -> GetMediaOutputTypeDef:
        """
        [Client.get_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.get_media)
        """
