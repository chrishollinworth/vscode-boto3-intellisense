"""
Type annotations for chime-sdk-media-pipelines service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/literals.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.literals import ArtifactsConcatenationStateType

    data: ArtifactsConcatenationStateType = "Disabled"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ArtifactsConcatenationStateType",
    "ArtifactsStateType",
    "AudioArtifactsConcatenationStateType",
    "AudioChannelsOptionType",
    "AudioMuxTypeType",
    "ConcatenationSinkTypeType",
    "ConcatenationSourceTypeType",
    "ContentMuxTypeType",
    "ContentShareLayoutOptionType",
    "LayoutOptionType",
    "LiveConnectorMuxTypeType",
    "LiveConnectorSinkTypeType",
    "LiveConnectorSourceTypeType",
    "MediaPipelineSinkTypeType",
    "MediaPipelineSourceTypeType",
    "MediaPipelineStatusType",
    "PresenterPositionType",
    "ResolutionOptionType",
    "VideoMuxTypeType",
)

ArtifactsConcatenationStateType = Literal["Disabled", "Enabled"]
ArtifactsStateType = Literal["Disabled", "Enabled"]
AudioArtifactsConcatenationStateType = Literal["Enabled"]
AudioChannelsOptionType = Literal["Mono", "Stereo"]
AudioMuxTypeType = Literal["AudioOnly", "AudioWithActiveSpeakerVideo", "AudioWithCompositedVideo"]
ConcatenationSinkTypeType = Literal["S3Bucket"]
ConcatenationSourceTypeType = Literal["MediaCapturePipeline"]
ContentMuxTypeType = Literal["ContentOnly"]
ContentShareLayoutOptionType = Literal["Horizontal", "PresenterOnly", "Vertical"]
LayoutOptionType = Literal["GridView"]
LiveConnectorMuxTypeType = Literal["AudioWithActiveSpeakerVideo", "AudioWithCompositedVideo"]
LiveConnectorSinkTypeType = Literal["RTMP"]
LiveConnectorSourceTypeType = Literal["ChimeSdkMeeting"]
MediaPipelineSinkTypeType = Literal["S3Bucket"]
MediaPipelineSourceTypeType = Literal["ChimeSdkMeeting"]
MediaPipelineStatusType = Literal["Failed", "InProgress", "Initializing", "Stopped", "Stopping"]
PresenterPositionType = Literal["BottomLeft", "BottomRight", "TopLeft", "TopRight"]
ResolutionOptionType = Literal["FHD", "HD"]
VideoMuxTypeType = Literal["VideoOnly"]
