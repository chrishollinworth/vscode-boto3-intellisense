# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for ivs service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ivs import IVSClient

    client: IVSClient = boto3.client("ivs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_ivs.paginator import (
    ListChannelsPaginator,
    ListPlaybackKeyPairsPaginator,
    ListStreamKeysPaginator,
    ListStreamsPaginator,
)
from mypy_boto3_ivs.type_defs import (
    BatchGetChannelResponseTypeDef,
    BatchGetStreamKeyResponseTypeDef,
    CreateChannelResponseTypeDef,
    CreateStreamKeyResponseTypeDef,
    GetChannelResponseTypeDef,
    GetPlaybackKeyPairResponseTypeDef,
    GetStreamKeyResponseTypeDef,
    GetStreamResponseTypeDef,
    ImportPlaybackKeyPairResponseTypeDef,
    ListChannelsResponseTypeDef,
    ListPlaybackKeyPairsResponseTypeDef,
    ListStreamKeysResponseTypeDef,
    ListStreamsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    UpdateChannelResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IVSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ChannelNotBroadcasting: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    PendingVerification: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    StreamUnavailable: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class IVSClient:
    """
    [IVS.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_get_channel(self, arns: List[str]) -> BatchGetChannelResponseTypeDef:
        """
        [Client.batch_get_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.batch_get_channel)
        """

    def batch_get_stream_key(self, arns: List[str]) -> BatchGetStreamKeyResponseTypeDef:
        """
        [Client.batch_get_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.batch_get_stream_key)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.can_paginate)
        """

    def create_channel(
        self,
        name: str = None,
        latencyMode: Literal["NORMAL", "LOW"] = None,
        type: Literal["BASIC", "STANDARD"] = None,
        authorized: bool = None,
        tags: Dict[str, str] = None,
    ) -> CreateChannelResponseTypeDef:
        """
        [Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.create_channel)
        """

    def create_stream_key(
        self, channelArn: str, tags: Dict[str, str] = None
    ) -> CreateStreamKeyResponseTypeDef:
        """
        [Client.create_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.create_stream_key)
        """

    def delete_channel(self, arn: str) -> None:
        """
        [Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.delete_channel)
        """

    def delete_playback_key_pair(self, arn: str) -> Dict[str, Any]:
        """
        [Client.delete_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.delete_playback_key_pair)
        """

    def delete_stream_key(self, arn: str) -> None:
        """
        [Client.delete_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.delete_stream_key)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.generate_presigned_url)
        """

    def get_channel(self, arn: str) -> GetChannelResponseTypeDef:
        """
        [Client.get_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.get_channel)
        """

    def get_playback_key_pair(self, arn: str) -> GetPlaybackKeyPairResponseTypeDef:
        """
        [Client.get_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.get_playback_key_pair)
        """

    def get_stream(self, channelArn: str) -> GetStreamResponseTypeDef:
        """
        [Client.get_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.get_stream)
        """

    def get_stream_key(self, arn: str) -> GetStreamKeyResponseTypeDef:
        """
        [Client.get_stream_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.get_stream_key)
        """

    def import_playback_key_pair(
        self, publicKeyMaterial: str, name: str = None, tags: Dict[str, str] = None
    ) -> ImportPlaybackKeyPairResponseTypeDef:
        """
        [Client.import_playback_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.import_playback_key_pair)
        """

    def list_channels(
        self, filterByName: str = None, nextToken: str = None, maxResults: int = None
    ) -> ListChannelsResponseTypeDef:
        """
        [Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.list_channels)
        """

    def list_playback_key_pairs(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListPlaybackKeyPairsResponseTypeDef:
        """
        [Client.list_playback_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.list_playback_key_pairs)
        """

    def list_stream_keys(
        self, channelArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListStreamKeysResponseTypeDef:
        """
        [Client.list_stream_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.list_stream_keys)
        """

    def list_streams(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListStreamsResponseTypeDef:
        """
        [Client.list_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.list_streams)
        """

    def list_tags_for_resource(
        self, resourceArn: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.list_tags_for_resource)
        """

    def put_metadata(self, channelArn: str, metadata: str) -> None:
        """
        [Client.put_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.put_metadata)
        """

    def stop_stream(self, channelArn: str) -> Dict[str, Any]:
        """
        [Client.stop_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.stop_stream)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.untag_resource)
        """

    def update_channel(
        self,
        arn: str,
        name: str = None,
        latencyMode: Literal["NORMAL", "LOW"] = None,
        type: Literal["BASIC", "STANDARD"] = None,
        authorized: bool = None,
    ) -> UpdateChannelResponseTypeDef:
        """
        [Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Client.update_channel)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListChannels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_playback_key_pairs"]
    ) -> ListPlaybackKeyPairsPaginator:
        """
        [Paginator.ListPlaybackKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListPlaybackKeyPairs)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_stream_keys"]) -> ListStreamKeysPaginator:
        """
        [Paginator.ListStreamKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListStreamKeys)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Paginator.ListStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ivs.html#IVS.Paginator.ListStreams)
        """
