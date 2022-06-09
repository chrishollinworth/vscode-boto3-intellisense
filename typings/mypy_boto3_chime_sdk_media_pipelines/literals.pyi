"""
Type annotations for chime-sdk-media-pipelines service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/literals.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.literals import ArtifactsStateType

    data: ArtifactsStateType = "Disabled"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ArtifactsStateType",
    "AudioMuxTypeType",
    "ContentMuxTypeType",
    "MediaPipelineSinkTypeType",
    "MediaPipelineSourceTypeType",
    "MediaPipelineStatusType",
    "VideoMuxTypeType",
)

ArtifactsStateType = Literal["Disabled", "Enabled"]
AudioMuxTypeType = Literal["AudioOnly", "AudioWithActiveSpeakerVideo"]
ContentMuxTypeType = Literal["ContentOnly"]
MediaPipelineSinkTypeType = Literal["S3Bucket"]
MediaPipelineSourceTypeType = Literal["ChimeSdkMeeting"]
MediaPipelineStatusType = Literal["Failed", "InProgress", "Initializing", "Stopped", "Stopping"]
VideoMuxTypeType = Literal["VideoOnly"]
