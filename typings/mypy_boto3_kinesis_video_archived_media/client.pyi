"""
Type annotations for kinesis-video-archived-media service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_archived_media import KinesisVideoArchivedMediaClient

    client: KinesisVideoArchivedMediaClient = boto3.client("kinesis-video-archived-media")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ContainerFormatType,
    DASHDisplayFragmentNumberType,
    DASHDisplayFragmentTimestampType,
    DASHPlaybackModeType,
    HLSDiscontinuityModeType,
    HLSDisplayFragmentTimestampType,
    HLSPlaybackModeType,
)
from .paginator import ListFragmentsPaginator
from .type_defs import (
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

class KinesisVideoArchivedMediaClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        KinesisVideoArchivedMediaClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#can_paginate)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#generate_presigned_url)
        """
    def get_clip(
        self,
        *,
        ClipFragmentSelector: "ClipFragmentSelectorTypeDef",
        StreamName: str = None,
        StreamARN: str = None
    ) -> GetClipOutputTypeDef:
        """
        Downloads an MP4 file (clip) containing the archived, on-demand media from the
        specified video stream over the specified time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_clip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#get_clip)
        """
    def get_dash_streaming_session_url(
        self,
        *,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: DASHPlaybackModeType = None,
        DisplayFragmentTimestamp: DASHDisplayFragmentTimestampType = None,
        DisplayFragmentNumber: DASHDisplayFragmentNumberType = None,
        DASHFragmentSelector: "DASHFragmentSelectorTypeDef" = None,
        Expires: int = None,
        MaxManifestFragmentResults: int = None
    ) -> GetDASHStreamingSessionURLOutputTypeDef:
        """
        Retrieves an MPEG Dynamic Adaptive Streaming over HTTP (DASH) URL for the
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_dash_streaming_session_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#get_dash_streaming_session_url)
        """
    def get_hls_streaming_session_url(
        self,
        *,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: HLSPlaybackModeType = None,
        HLSFragmentSelector: "HLSFragmentSelectorTypeDef" = None,
        ContainerFormat: ContainerFormatType = None,
        DiscontinuityMode: HLSDiscontinuityModeType = None,
        DisplayFragmentTimestamp: HLSDisplayFragmentTimestampType = None,
        Expires: int = None,
        MaxMediaPlaylistFragmentResults: int = None
    ) -> GetHLSStreamingSessionURLOutputTypeDef:
        """
        Retrieves an HTTP Live Streaming (HLS) URL for the stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_hls_streaming_session_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#get_hls_streaming_session_url)
        """
    def get_media_for_fragment_list(
        self, *, Fragments: List[str], StreamName: str = None, StreamARN: str = None
    ) -> GetMediaForFragmentListOutputTypeDef:
        """
        Gets media for a list of fragments (specified by fragment number) from the
        archived data in an Amazon Kinesis video stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_media_for_fragment_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#get_media_for_fragment_list)
        """
    def list_fragments(
        self,
        *,
        StreamName: str = None,
        StreamARN: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        FragmentSelector: "FragmentSelectorTypeDef" = None
    ) -> ListFragmentsOutputTypeDef:
        """
        Returns a list of  Fragment objects from the specified stream and timestamp
        range within the archived data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.list_fragments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#list_fragments)
        """
    def get_paginator(self, operation_name: Literal["list_fragments"]) -> ListFragmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators.html#listfragmentspaginator)
        """
