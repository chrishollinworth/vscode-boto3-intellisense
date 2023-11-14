"""
Type annotations for chime-sdk-media-pipelines service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/literals.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.literals import ActiveSpeakerPositionType

    data: ActiveSpeakerPositionType = "BottomLeft"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActiveSpeakerPositionType",
    "ArtifactsConcatenationStateType",
    "ArtifactsStateType",
    "AudioArtifactsConcatenationStateType",
    "AudioChannelsOptionType",
    "AudioMuxTypeType",
    "BorderColorType",
    "CallAnalyticsLanguageCodeType",
    "CanvasOrientationType",
    "ConcatenationSinkTypeType",
    "ConcatenationSourceTypeType",
    "ContentMuxTypeType",
    "ContentRedactionOutputType",
    "ContentShareLayoutOptionType",
    "ContentTypeType",
    "FragmentSelectorTypeType",
    "HighlightColorType",
    "HorizontalTilePositionType",
    "KinesisVideoStreamPoolStatusType",
    "LayoutOptionType",
    "LiveConnectorMuxTypeType",
    "LiveConnectorSinkTypeType",
    "LiveConnectorSourceTypeType",
    "MediaEncodingType",
    "MediaInsightsPipelineConfigurationElementTypeType",
    "MediaPipelineElementStatusType",
    "MediaPipelineSinkTypeType",
    "MediaPipelineSourceTypeType",
    "MediaPipelineStatusType",
    "MediaPipelineStatusUpdateType",
    "MediaPipelineTaskStatusType",
    "MediaStreamPipelineSinkTypeType",
    "MediaStreamTypeType",
    "PartialResultsStabilityType",
    "ParticipantRoleType",
    "PresenterPositionType",
    "RealTimeAlertRuleTypeType",
    "RecordingFileFormatType",
    "ResolutionOptionType",
    "SentimentTypeType",
    "TileOrderType",
    "VerticalTilePositionType",
    "VideoMuxTypeType",
    "VocabularyFilterMethodType",
    "VoiceAnalyticsConfigurationStatusType",
    "VoiceAnalyticsLanguageCodeType",
)

ActiveSpeakerPositionType = Literal["BottomLeft", "BottomRight", "TopLeft", "TopRight"]
ArtifactsConcatenationStateType = Literal["Disabled", "Enabled"]
ArtifactsStateType = Literal["Disabled", "Enabled"]
AudioArtifactsConcatenationStateType = Literal["Enabled"]
AudioChannelsOptionType = Literal["Mono", "Stereo"]
AudioMuxTypeType = Literal["AudioOnly", "AudioWithActiveSpeakerVideo", "AudioWithCompositedVideo"]
BorderColorType = Literal["Black", "Blue", "Green", "Red", "White", "Yellow"]
CallAnalyticsLanguageCodeType = Literal[
    "de-DE", "en-AU", "en-GB", "en-US", "es-US", "fr-CA", "fr-FR", "it-IT", "pt-BR"
]
CanvasOrientationType = Literal["Landscape", "Portrait"]
ConcatenationSinkTypeType = Literal["S3Bucket"]
ConcatenationSourceTypeType = Literal["MediaCapturePipeline"]
ContentMuxTypeType = Literal["ContentOnly"]
ContentRedactionOutputType = Literal["redacted", "redacted_and_unredacted"]
ContentShareLayoutOptionType = Literal[
    "ActiveSpeakerOnly", "Horizontal", "PresenterOnly", "Vertical"
]
ContentTypeType = Literal["PII"]
FragmentSelectorTypeType = Literal["ProducerTimestamp", "ServerTimestamp"]
HighlightColorType = Literal["Black", "Blue", "Green", "Red", "White", "Yellow"]
HorizontalTilePositionType = Literal["Bottom", "Top"]
KinesisVideoStreamPoolStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
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
    "VoiceEnhancementSink",
]
MediaPipelineElementStatusType = Literal[
    "Failed",
    "InProgress",
    "Initializing",
    "NotStarted",
    "NotSupported",
    "Paused",
    "Stopped",
    "Stopping",
]
MediaPipelineSinkTypeType = Literal["S3Bucket"]
MediaPipelineSourceTypeType = Literal["ChimeSdkMeeting"]
MediaPipelineStatusType = Literal[
    "Failed", "InProgress", "Initializing", "NotStarted", "Paused", "Stopped", "Stopping"
]
MediaPipelineStatusUpdateType = Literal["Pause", "Resume"]
MediaPipelineTaskStatusType = Literal[
    "Failed", "InProgress", "Initializing", "NotStarted", "Stopped", "Stopping"
]
MediaStreamPipelineSinkTypeType = Literal["KinesisVideoStreamPool"]
MediaStreamTypeType = Literal["IndividualAudio", "MixedAudio"]
PartialResultsStabilityType = Literal["high", "low", "medium"]
ParticipantRoleType = Literal["AGENT", "CUSTOMER"]
PresenterPositionType = Literal["BottomLeft", "BottomRight", "TopLeft", "TopRight"]
RealTimeAlertRuleTypeType = Literal["IssueDetection", "KeywordMatch", "Sentiment"]
RecordingFileFormatType = Literal["Opus", "Wav"]
ResolutionOptionType = Literal["FHD", "HD"]
SentimentTypeType = Literal["NEGATIVE"]
TileOrderType = Literal["JoinSequence", "SpeakerSequence"]
VerticalTilePositionType = Literal["Left", "Right"]
VideoMuxTypeType = Literal["VideoOnly"]
VocabularyFilterMethodType = Literal["mask", "remove", "tag"]
VoiceAnalyticsConfigurationStatusType = Literal["Disabled", "Enabled"]
VoiceAnalyticsLanguageCodeType = Literal["en-US"]
