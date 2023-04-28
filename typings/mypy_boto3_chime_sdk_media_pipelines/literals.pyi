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
    "CallAnalyticsLanguageCodeType",
    "ConcatenationSinkTypeType",
    "ConcatenationSourceTypeType",
    "ContentMuxTypeType",
    "ContentRedactionOutputType",
    "ContentShareLayoutOptionType",
    "ContentTypeType",
    "FragmentSelectorTypeType",
    "LayoutOptionType",
    "LiveConnectorMuxTypeType",
    "LiveConnectorSinkTypeType",
    "LiveConnectorSourceTypeType",
    "MediaEncodingType",
    "MediaInsightsPipelineConfigurationElementTypeType",
    "MediaPipelineSinkTypeType",
    "MediaPipelineSourceTypeType",
    "MediaPipelineStatusType",
    "MediaPipelineStatusUpdateType",
    "PartialResultsStabilityType",
    "ParticipantRoleType",
    "PresenterPositionType",
    "RealTimeAlertRuleTypeType",
    "RecordingFileFormatType",
    "ResolutionOptionType",
    "SentimentTypeType",
    "VideoMuxTypeType",
    "VocabularyFilterMethodType",
    "VoiceAnalyticsConfigurationStatusType",
)

ArtifactsConcatenationStateType = Literal["Disabled", "Enabled"]
ArtifactsStateType = Literal["Disabled", "Enabled"]
AudioArtifactsConcatenationStateType = Literal["Enabled"]
AudioChannelsOptionType = Literal["Mono", "Stereo"]
AudioMuxTypeType = Literal["AudioOnly", "AudioWithActiveSpeakerVideo", "AudioWithCompositedVideo"]
CallAnalyticsLanguageCodeType = Literal[
    "de-DE", "en-AU", "en-GB", "en-US", "es-US", "fr-CA", "fr-FR", "it-IT", "pt-BR"
]
ConcatenationSinkTypeType = Literal["S3Bucket"]
ConcatenationSourceTypeType = Literal["MediaCapturePipeline"]
ContentMuxTypeType = Literal["ContentOnly"]
ContentRedactionOutputType = Literal["redacted", "redacted_and_unredacted"]
ContentShareLayoutOptionType = Literal["Horizontal", "PresenterOnly", "Vertical"]
ContentTypeType = Literal["PII"]
FragmentSelectorTypeType = Literal["ProducerTimestamp", "ServerTimestamp"]
LayoutOptionType = Literal["GridView"]
LiveConnectorMuxTypeType = Literal["AudioWithActiveSpeakerVideo", "AudioWithCompositedVideo"]
LiveConnectorSinkTypeType = Literal["RTMP"]
LiveConnectorSourceTypeType = Literal["ChimeSdkMeeting"]
MediaEncodingType = Literal["pcm"]
MediaInsightsPipelineConfigurationElementTypeType = Literal[
    "AmazonTranscribeCallAnalyticsProcessor",
    "AmazonTranscribeProcessor",
    "KinesisDataStreamSink",
    "LambdaFunctionSink",
    "S3RecordingSink",
    "SnsTopicSink",
    "SqsQueueSink",
    "VoiceAnalyticsProcessor",
]
MediaPipelineSinkTypeType = Literal["S3Bucket"]
MediaPipelineSourceTypeType = Literal["ChimeSdkMeeting"]
MediaPipelineStatusType = Literal[
    "Failed", "InProgress", "Initializing", "Paused", "Stopped", "Stopping"
]
MediaPipelineStatusUpdateType = Literal["Pause", "Resume"]
PartialResultsStabilityType = Literal["high", "low", "medium"]
ParticipantRoleType = Literal["AGENT", "CUSTOMER"]
PresenterPositionType = Literal["BottomLeft", "BottomRight", "TopLeft", "TopRight"]
RealTimeAlertRuleTypeType = Literal["IssueDetection", "KeywordMatch", "Sentiment"]
RecordingFileFormatType = Literal["Opus", "Wav"]
ResolutionOptionType = Literal["FHD", "HD"]
SentimentTypeType = Literal["NEGATIVE"]
VideoMuxTypeType = Literal["VideoOnly"]
VocabularyFilterMethodType = Literal["mask", "remove", "tag"]
VoiceAnalyticsConfigurationStatusType = Literal["Disabled", "Enabled"]
