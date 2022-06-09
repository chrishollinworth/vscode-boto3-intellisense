"""
Type annotations for chime-sdk-media-pipelines service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.type_defs import ArtifactsConfigurationTypeDef

    data: ArtifactsConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ArtifactsStateType, AudioMuxTypeType, MediaPipelineStatusType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ArtifactsConfigurationTypeDef",
    "AudioArtifactsConfigurationTypeDef",
    "ChimeSdkMeetingConfigurationTypeDef",
    "ContentArtifactsConfigurationTypeDef",
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    "CreateMediaCapturePipelineResponseTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MediaCapturePipelineSummaryTypeDef",
    "MediaCapturePipelineTypeDef",
    "ResponseMetadataTypeDef",
    "SelectedVideoStreamsTypeDef",
    "SourceConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "VideoArtifactsConfigurationTypeDef",
)

ArtifactsConfigurationTypeDef = TypedDict(
    "ArtifactsConfigurationTypeDef",
    {
        "Audio": "AudioArtifactsConfigurationTypeDef",
        "Video": "VideoArtifactsConfigurationTypeDef",
        "Content": "ContentArtifactsConfigurationTypeDef",
    },
)

AudioArtifactsConfigurationTypeDef = TypedDict(
    "AudioArtifactsConfigurationTypeDef",
    {
        "MuxType": AudioMuxTypeType,
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

DeleteMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
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
