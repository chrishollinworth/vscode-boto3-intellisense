"""
Type annotations for chime-sdk-media-pipelines service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.type_defs import ArtifactsConcatenationConfigurationTypeDef

    data: ArtifactsConcatenationConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ArtifactsConcatenationStateType,
    ArtifactsStateType,
    AudioChannelsOptionType,
    AudioMuxTypeType,
    ContentShareLayoutOptionType,
    LiveConnectorMuxTypeType,
    MediaPipelineStatusType,
    PresenterPositionType,
    ResolutionOptionType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArtifactsConcatenationConfigurationTypeDef",
    "ArtifactsConfigurationTypeDef",
    "AudioArtifactsConfigurationTypeDef",
    "AudioConcatenationConfigurationTypeDef",
    "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    "ChimeSdkMeetingConfigurationTypeDef",
    "ChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    "CompositedVideoArtifactsConfigurationTypeDef",
    "CompositedVideoConcatenationConfigurationTypeDef",
    "ConcatenationSinkTypeDef",
    "ConcatenationSourceTypeDef",
    "ContentArtifactsConfigurationTypeDef",
    "ContentConcatenationConfigurationTypeDef",
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    "CreateMediaCapturePipelineResponseTypeDef",
    "CreateMediaConcatenationPipelineRequestRequestTypeDef",
    "CreateMediaConcatenationPipelineResponseTypeDef",
    "CreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    "DataChannelConcatenationConfigurationTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "DeleteMediaPipelineRequestRequestTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "GetMediaPipelineRequestRequestTypeDef",
    "GetMediaPipelineResponseTypeDef",
    "GridViewConfigurationTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ListMediaPipelinesRequestRequestTypeDef",
    "ListMediaPipelinesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LiveConnectorRTMPConfigurationTypeDef",
    "LiveConnectorSinkConfigurationTypeDef",
    "LiveConnectorSourceConfigurationTypeDef",
    "MediaCapturePipelineSourceConfigurationTypeDef",
    "MediaCapturePipelineSummaryTypeDef",
    "MediaCapturePipelineTypeDef",
    "MediaConcatenationPipelineTypeDef",
    "MediaLiveConnectorPipelineTypeDef",
    "MediaPipelineSummaryTypeDef",
    "MediaPipelineTypeDef",
    "MeetingEventsConcatenationConfigurationTypeDef",
    "PresenterOnlyConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketSinkConfigurationTypeDef",
    "SelectedVideoStreamsTypeDef",
    "SourceConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VideoArtifactsConfigurationTypeDef",
    "VideoConcatenationConfigurationTypeDef",
)

ArtifactsConcatenationConfigurationTypeDef = TypedDict(
    "ArtifactsConcatenationConfigurationTypeDef",
    {
        "Audio": "AudioConcatenationConfigurationTypeDef",
        "Video": "VideoConcatenationConfigurationTypeDef",
        "Content": "ContentConcatenationConfigurationTypeDef",
        "DataChannel": "DataChannelConcatenationConfigurationTypeDef",
        "TranscriptionMessages": "TranscriptionMessagesConcatenationConfigurationTypeDef",
        "MeetingEvents": "MeetingEventsConcatenationConfigurationTypeDef",
        "CompositedVideo": "CompositedVideoConcatenationConfigurationTypeDef",
    },
)

_RequiredArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredArtifactsConfigurationTypeDef",
    {
        "Audio": "AudioArtifactsConfigurationTypeDef",
        "Video": "VideoArtifactsConfigurationTypeDef",
        "Content": "ContentArtifactsConfigurationTypeDef",
    },
)
_OptionalArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalArtifactsConfigurationTypeDef",
    {
        "CompositedVideo": "CompositedVideoArtifactsConfigurationTypeDef",
    },
    total=False,
)

class ArtifactsConfigurationTypeDef(
    _RequiredArtifactsConfigurationTypeDef, _OptionalArtifactsConfigurationTypeDef
):
    pass

AudioArtifactsConfigurationTypeDef = TypedDict(
    "AudioArtifactsConfigurationTypeDef",
    {
        "MuxType": AudioMuxTypeType,
    },
)

AudioConcatenationConfigurationTypeDef = TypedDict(
    "AudioConcatenationConfigurationTypeDef",
    {
        "State": Literal["Enabled"],
    },
)

ChimeSdkMeetingConcatenationConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    {
        "ArtifactsConfiguration": "ArtifactsConcatenationConfigurationTypeDef",
    },
)

ChimeSdkMeetingConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationTypeDef",
    {
        "SourceConfiguration": "SourceConfigurationTypeDef",
        "ArtifactsConfiguration": "ArtifactsConfigurationTypeDef",
    },
    total=False,
)

_RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef = TypedDict(
    "_RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    {
        "Arn": str,
        "MuxType": LiveConnectorMuxTypeType,
    },
)
_OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef = TypedDict(
    "_OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    {
        "CompositedVideo": "CompositedVideoArtifactsConfigurationTypeDef",
        "SourceConfiguration": "SourceConfigurationTypeDef",
    },
    total=False,
)

class ChimeSdkMeetingLiveConnectorConfigurationTypeDef(
    _RequiredChimeSdkMeetingLiveConnectorConfigurationTypeDef,
    _OptionalChimeSdkMeetingLiveConnectorConfigurationTypeDef,
):
    pass

_RequiredCompositedVideoArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredCompositedVideoArtifactsConfigurationTypeDef",
    {
        "GridViewConfiguration": "GridViewConfigurationTypeDef",
    },
)
_OptionalCompositedVideoArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalCompositedVideoArtifactsConfigurationTypeDef",
    {
        "Layout": Literal["GridView"],
        "Resolution": ResolutionOptionType,
    },
    total=False,
)

class CompositedVideoArtifactsConfigurationTypeDef(
    _RequiredCompositedVideoArtifactsConfigurationTypeDef,
    _OptionalCompositedVideoArtifactsConfigurationTypeDef,
):
    pass

CompositedVideoConcatenationConfigurationTypeDef = TypedDict(
    "CompositedVideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

ConcatenationSinkTypeDef = TypedDict(
    "ConcatenationSinkTypeDef",
    {
        "Type": Literal["S3Bucket"],
        "S3BucketSinkConfiguration": "S3BucketSinkConfigurationTypeDef",
    },
)

ConcatenationSourceTypeDef = TypedDict(
    "ConcatenationSourceTypeDef",
    {
        "Type": Literal["MediaCapturePipeline"],
        "MediaCapturePipelineSourceConfiguration": "MediaCapturePipelineSourceConfigurationTypeDef",
    },
)

_RequiredContentArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredContentArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
    },
)
_OptionalContentArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalContentArtifactsConfigurationTypeDef",
    {
        "MuxType": Literal["ContentOnly"],
    },
    total=False,
)

class ContentArtifactsConfigurationTypeDef(
    _RequiredContentArtifactsConfigurationTypeDef, _OptionalContentArtifactsConfigurationTypeDef
):
    pass

ContentConcatenationConfigurationTypeDef = TypedDict(
    "ContentConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

_RequiredCreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
    },
)
_OptionalCreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ChimeSdkMeetingConfiguration": "ChimeSdkMeetingConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMediaCapturePipelineRequestRequestTypeDef(
    _RequiredCreateMediaCapturePipelineRequestRequestTypeDef,
    _OptionalCreateMediaCapturePipelineRequestRequestTypeDef,
):
    pass

CreateMediaCapturePipelineResponseTypeDef = TypedDict(
    "CreateMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": "MediaCapturePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef",
    {
        "Sources": List["ConcatenationSourceTypeDef"],
        "Sinks": List["ConcatenationSinkTypeDef"],
    },
)
_OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMediaConcatenationPipelineRequestRequestTypeDef(
    _RequiredCreateMediaConcatenationPipelineRequestRequestTypeDef,
    _OptionalCreateMediaConcatenationPipelineRequestRequestTypeDef,
):
    pass

CreateMediaConcatenationPipelineResponseTypeDef = TypedDict(
    "CreateMediaConcatenationPipelineResponseTypeDef",
    {
        "MediaConcatenationPipeline": "MediaConcatenationPipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    {
        "Sources": List["LiveConnectorSourceConfigurationTypeDef"],
        "Sinks": List["LiveConnectorSinkConfigurationTypeDef"],
    },
)
_OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMediaLiveConnectorPipelineRequestRequestTypeDef(
    _RequiredCreateMediaLiveConnectorPipelineRequestRequestTypeDef,
    _OptionalCreateMediaLiveConnectorPipelineRequestRequestTypeDef,
):
    pass

CreateMediaLiveConnectorPipelineResponseTypeDef = TypedDict(
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    {
        "MediaLiveConnectorPipeline": "MediaLiveConnectorPipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataChannelConcatenationConfigurationTypeDef = TypedDict(
    "DataChannelConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

DeleteMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

DeleteMediaPipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

GetMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "GetMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

GetMediaCapturePipelineResponseTypeDef = TypedDict(
    "GetMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": "MediaCapturePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMediaPipelineRequestRequestTypeDef = TypedDict(
    "GetMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

GetMediaPipelineResponseTypeDef = TypedDict(
    "GetMediaPipelineResponseTypeDef",
    {
        "MediaPipeline": "MediaPipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGridViewConfigurationTypeDef = TypedDict(
    "_RequiredGridViewConfigurationTypeDef",
    {
        "ContentShareLayout": ContentShareLayoutOptionType,
    },
)
_OptionalGridViewConfigurationTypeDef = TypedDict(
    "_OptionalGridViewConfigurationTypeDef",
    {
        "PresenterOnlyConfiguration": "PresenterOnlyConfigurationTypeDef",
    },
    total=False,
)

class GridViewConfigurationTypeDef(
    _RequiredGridViewConfigurationTypeDef, _OptionalGridViewConfigurationTypeDef
):
    pass

ListMediaCapturePipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMediaCapturePipelinesResponseTypeDef = TypedDict(
    "ListMediaCapturePipelinesResponseTypeDef",
    {
        "MediaCapturePipelines": List["MediaCapturePipelineSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMediaPipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaPipelinesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMediaPipelinesResponseTypeDef = TypedDict(
    "ListMediaPipelinesResponseTypeDef",
    {
        "MediaPipelines": List["MediaPipelineSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLiveConnectorRTMPConfigurationTypeDef = TypedDict(
    "_RequiredLiveConnectorRTMPConfigurationTypeDef",
    {
        "Url": str,
    },
)
_OptionalLiveConnectorRTMPConfigurationTypeDef = TypedDict(
    "_OptionalLiveConnectorRTMPConfigurationTypeDef",
    {
        "AudioChannels": AudioChannelsOptionType,
        "AudioSampleRate": str,
    },
    total=False,
)

class LiveConnectorRTMPConfigurationTypeDef(
    _RequiredLiveConnectorRTMPConfigurationTypeDef, _OptionalLiveConnectorRTMPConfigurationTypeDef
):
    pass

LiveConnectorSinkConfigurationTypeDef = TypedDict(
    "LiveConnectorSinkConfigurationTypeDef",
    {
        "SinkType": Literal["RTMP"],
        "RTMPConfiguration": "LiveConnectorRTMPConfigurationTypeDef",
    },
)

LiveConnectorSourceConfigurationTypeDef = TypedDict(
    "LiveConnectorSourceConfigurationTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "ChimeSdkMeetingLiveConnectorConfiguration": "ChimeSdkMeetingLiveConnectorConfigurationTypeDef",
    },
)

MediaCapturePipelineSourceConfigurationTypeDef = TypedDict(
    "MediaCapturePipelineSourceConfigurationTypeDef",
    {
        "MediaPipelineArn": str,
        "ChimeSdkMeetingConfiguration": "ChimeSdkMeetingConcatenationConfigurationTypeDef",
    },
)

MediaCapturePipelineSummaryTypeDef = TypedDict(
    "MediaCapturePipelineSummaryTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
    },
    total=False,
)

MediaCapturePipelineTypeDef = TypedDict(
    "MediaCapturePipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "Status": MediaPipelineStatusType,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ChimeSdkMeetingConfiguration": "ChimeSdkMeetingConfigurationTypeDef",
    },
    total=False,
)

MediaConcatenationPipelineTypeDef = TypedDict(
    "MediaConcatenationPipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "Sources": List["ConcatenationSourceTypeDef"],
        "Sinks": List["ConcatenationSinkTypeDef"],
        "Status": MediaPipelineStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

MediaLiveConnectorPipelineTypeDef = TypedDict(
    "MediaLiveConnectorPipelineTypeDef",
    {
        "Sources": List["LiveConnectorSourceConfigurationTypeDef"],
        "Sinks": List["LiveConnectorSinkConfigurationTypeDef"],
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "Status": MediaPipelineStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

MediaPipelineSummaryTypeDef = TypedDict(
    "MediaPipelineSummaryTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
    },
    total=False,
)

MediaPipelineTypeDef = TypedDict(
    "MediaPipelineTypeDef",
    {
        "MediaCapturePipeline": "MediaCapturePipelineTypeDef",
        "MediaLiveConnectorPipeline": "MediaLiveConnectorPipelineTypeDef",
        "MediaConcatenationPipeline": "MediaConcatenationPipelineTypeDef",
    },
    total=False,
)

MeetingEventsConcatenationConfigurationTypeDef = TypedDict(
    "MeetingEventsConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

PresenterOnlyConfigurationTypeDef = TypedDict(
    "PresenterOnlyConfigurationTypeDef",
    {
        "PresenterPosition": PresenterPositionType,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

S3BucketSinkConfigurationTypeDef = TypedDict(
    "S3BucketSinkConfigurationTypeDef",
    {
        "Destination": str,
    },
)

SelectedVideoStreamsTypeDef = TypedDict(
    "SelectedVideoStreamsTypeDef",
    {
        "AttendeeIds": List[str],
        "ExternalUserIds": List[str],
    },
    total=False,
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "SelectedVideoStreams": "SelectedVideoStreamsTypeDef",
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TranscriptionMessagesConcatenationConfigurationTypeDef = TypedDict(
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredVideoArtifactsConfigurationTypeDef = TypedDict(
    "_RequiredVideoArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
    },
)
_OptionalVideoArtifactsConfigurationTypeDef = TypedDict(
    "_OptionalVideoArtifactsConfigurationTypeDef",
    {
        "MuxType": Literal["VideoOnly"],
    },
    total=False,
)

class VideoArtifactsConfigurationTypeDef(
    _RequiredVideoArtifactsConfigurationTypeDef, _OptionalVideoArtifactsConfigurationTypeDef
):
    pass

VideoConcatenationConfigurationTypeDef = TypedDict(
    "VideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)
