# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_kinesis_video_media.type_defs import GetMediaOutputTypeDef, StartSelectorTypeDef

__all__ = ("KinesisVideoMediaClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ClientLimitExceededException: Type[Boto3ClientError]
    ConnectionLimitExceededException: Type[Boto3ClientError]
    InvalidArgumentException: Type[Boto3ClientError]
    InvalidEndpointException: Type[Boto3ClientError]
    NotAuthorizedException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]


class KinesisVideoMediaClient:
    """
    [KinesisVideoMedia.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.generate_presigned_url)
        """

    def get_media(
        self, StartSelector: StartSelectorTypeDef, StreamName: str = None, StreamARN: str = None
    ) -> GetMediaOutputTypeDef:
        """
        [Client.get_media documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/kinesis-video-media.html#KinesisVideoMedia.Client.get_media)
        """
