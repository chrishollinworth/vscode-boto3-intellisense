# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for kinesis-video-archived-media service client

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_archived_media import KinesisVideoArchivedMediaClient

    client: KinesisVideoArchivedMediaClient = boto3.client("kinesis-video-archived-media")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_kinesis_video_archived_media.paginator import ListFragmentsPaginator
from mypy_boto3_kinesis_video_archived_media.type_defs import (
    ClipFragmentSelectorTypeDef,
    DASHFragmentSelectorTypeDef,
    FragmentSelectorTypeDef,
    GetClipOutputTypeDef,
    GetDASHStreamingSessionURLOutputTypeDef,
    GetHLSStreamingSessionURLOutputTypeDef,
    GetMediaForFragmentListOutputTypeDef,
    HLSFragmentSelectorTypeDef,
    ListFragmentsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisVideoArchivedMediaClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ClientLimitExceededException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidCodecPrivateDataException: Type[BotocoreClientError]
    InvalidMediaFrameException: Type[BotocoreClientError]
    MissingCodecPrivateDataException: Type[BotocoreClientError]
    NoDataRetentionException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    UnsupportedStreamMediaTypeException: Type[BotocoreClientError]


class KinesisVideoArchivedMediaClient:
    """
    [KinesisVideoArchivedMedia.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.generate_presigned_url)
        """

    def get_clip(
        self,
        ClipFragmentSelector: ClipFragmentSelectorTypeDef,
        StreamName: str = None,
        StreamARN: str = None,
    ) -> GetClipOutputTypeDef:
        """
        [Client.get_clip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_clip)
        """

    def get_dash_streaming_session_url(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"] = None,
        DisplayFragmentTimestamp: Literal["ALWAYS", "NEVER"] = None,
        DisplayFragmentNumber: Literal["ALWAYS", "NEVER"] = None,
        DASHFragmentSelector: DASHFragmentSelectorTypeDef = None,
        Expires: int = None,
        MaxManifestFragmentResults: int = None,
    ) -> GetDASHStreamingSessionURLOutputTypeDef:
        """
        [Client.get_dash_streaming_session_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_dash_streaming_session_url)
        """

    def get_hls_streaming_session_url(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"] = None,
        HLSFragmentSelector: HLSFragmentSelectorTypeDef = None,
        ContainerFormat: Literal["FRAGMENTED_MP4", "MPEG_TS"] = None,
        DiscontinuityMode: Literal["ALWAYS", "NEVER", "ON_DISCONTINUITY"] = None,
        DisplayFragmentTimestamp: Literal["ALWAYS", "NEVER"] = None,
        Expires: int = None,
        MaxMediaPlaylistFragmentResults: int = None,
    ) -> GetHLSStreamingSessionURLOutputTypeDef:
        """
        [Client.get_hls_streaming_session_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_hls_streaming_session_url)
        """

    def get_media_for_fragment_list(
        self, StreamName: str, Fragments: List[str]
    ) -> GetMediaForFragmentListOutputTypeDef:
        """
        [Client.get_media_for_fragment_list documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_media_for_fragment_list)
        """

    def list_fragments(
        self,
        StreamName: str,
        MaxResults: int = None,
        NextToken: str = None,
        FragmentSelector: FragmentSelectorTypeDef = None,
    ) -> ListFragmentsOutputTypeDef:
        """
        [Client.list_fragments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.list_fragments)
        """

    def get_paginator(self, operation_name: Literal["list_fragments"]) -> ListFragmentsPaginator:
        """
        [Paginator.ListFragments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)
        """
