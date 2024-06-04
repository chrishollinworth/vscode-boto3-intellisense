"""
Type annotations for chime-sdk-media-pipelines service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_media_pipelines/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_media_pipelines.type_defs import ActiveSpeakerOnlyConfigurationTypeDef

    data: ActiveSpeakerOnlyConfigurationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActiveSpeakerPositionType,
    ArtifactsConcatenationStateType,
    ArtifactsStateType,
    AudioChannelsOptionType,
    AudioMuxTypeType,
    BorderColorType,
    CallAnalyticsLanguageCodeType,
    CanvasOrientationType,
    ContentRedactionOutputType,
    ContentShareLayoutOptionType,
    FragmentSelectorTypeType,
    HighlightColorType,
    HorizontalTilePositionType,
    KinesisVideoStreamPoolStatusType,
    LiveConnectorMuxTypeType,
    MediaInsightsPipelineConfigurationElementTypeType,
    MediaPipelineElementStatusType,
    MediaPipelineStatusType,
    MediaPipelineStatusUpdateType,
    MediaPipelineTaskStatusType,
    MediaStreamTypeType,
    PartialResultsStabilityType,
    ParticipantRoleType,
    PresenterPositionType,
    RealTimeAlertRuleTypeType,
    RecordingFileFormatType,
    ResolutionOptionType,
    TileOrderType,
    VerticalTilePositionType,
    VocabularyFilterMethodType,
    VoiceAnalyticsConfigurationStatusType,
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
    "ActiveSpeakerOnlyConfigurationTypeDef",
    "AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    "AmazonTranscribeProcessorConfigurationTypeDef",
    "ArtifactsConcatenationConfigurationTypeDef",
    "ArtifactsConfigurationTypeDef",
    "AudioArtifactsConfigurationTypeDef",
    "AudioConcatenationConfigurationTypeDef",
    "ChannelDefinitionTypeDef",
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
    "CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    "CreateMediaInsightsPipelineRequestRequestTypeDef",
    "CreateMediaInsightsPipelineResponseTypeDef",
    "CreateMediaLiveConnectorPipelineRequestRequestTypeDef",
    "CreateMediaLiveConnectorPipelineResponseTypeDef",
    "CreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    "CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    "CreateMediaStreamPipelineRequestRequestTypeDef",
    "CreateMediaStreamPipelineResponseTypeDef",
    "DataChannelConcatenationConfigurationTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    "DeleteMediaPipelineRequestRequestTypeDef",
    "FragmentSelectorTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "GetMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "GetMediaInsightsPipelineConfigurationResponseTypeDef",
    "GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    "GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    "GetMediaPipelineRequestRequestTypeDef",
    "GetMediaPipelineResponseTypeDef",
    "GetSpeakerSearchTaskRequestRequestTypeDef",
    "GetSpeakerSearchTaskResponseTypeDef",
    "GetVoiceToneAnalysisTaskRequestRequestTypeDef",
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    "GridViewConfigurationTypeDef",
    "HorizontalLayoutConfigurationTypeDef",
    "IssueDetectionConfigurationTypeDef",
    "KeywordMatchConfigurationTypeDef",
    "KinesisDataStreamSinkConfigurationTypeDef",
    "KinesisVideoStreamConfigurationTypeDef",
    "KinesisVideoStreamConfigurationUpdateTypeDef",
    "KinesisVideoStreamPoolConfigurationTypeDef",
    "KinesisVideoStreamPoolSummaryTypeDef",
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
    "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
    "KinesisVideoStreamSourceTaskConfigurationTypeDef",
    "LambdaFunctionSinkConfigurationTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef",
    "ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    "ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef",
    "ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef",
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
    "MediaInsightsPipelineConfigurationElementTypeDef",
    "MediaInsightsPipelineConfigurationSummaryTypeDef",
    "MediaInsightsPipelineConfigurationTypeDef",
    "MediaInsightsPipelineElementStatusTypeDef",
    "MediaInsightsPipelineTypeDef",
    "MediaLiveConnectorPipelineTypeDef",
    "MediaPipelineSummaryTypeDef",
    "MediaPipelineTypeDef",
    "MediaStreamPipelineTypeDef",
    "MediaStreamSinkTypeDef",
    "MediaStreamSourceTypeDef",
    "MeetingEventsConcatenationConfigurationTypeDef",
    "PostCallAnalyticsSettingsTypeDef",
    "PresenterOnlyConfigurationTypeDef",
    "RealTimeAlertConfigurationTypeDef",
    "RealTimeAlertRuleTypeDef",
    "RecordingStreamConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3BucketSinkConfigurationTypeDef",
    "S3RecordingSinkConfigurationTypeDef",
    "S3RecordingSinkRuntimeConfigurationTypeDef",
    "SelectedVideoStreamsTypeDef",
    "SentimentConfigurationTypeDef",
    "SnsTopicSinkConfigurationTypeDef",
    "SourceConfigurationTypeDef",
    "SpeakerSearchTaskTypeDef",
    "SqsQueueSinkConfigurationTypeDef",
    "StartSpeakerSearchTaskRequestRequestTypeDef",
    "StartSpeakerSearchTaskResponseTypeDef",
    "StartVoiceToneAnalysisTaskRequestRequestTypeDef",
    "StartVoiceToneAnalysisTaskResponseTypeDef",
    "StopSpeakerSearchTaskRequestRequestTypeDef",
    "StopVoiceToneAnalysisTaskRequestRequestTypeDef",
    "StreamChannelDefinitionTypeDef",
    "StreamConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimestampRangeTypeDef",
    "TranscriptionMessagesConcatenationConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    "UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    "UpdateMediaInsightsPipelineStatusRequestRequestTypeDef",
    "UpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    "UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    "VerticalLayoutConfigurationTypeDef",
    "VideoArtifactsConfigurationTypeDef",
    "VideoAttributeTypeDef",
    "VideoConcatenationConfigurationTypeDef",
    "VoiceAnalyticsProcessorConfigurationTypeDef",
    "VoiceEnhancementSinkConfigurationTypeDef",
    "VoiceToneAnalysisTaskTypeDef",
)

ActiveSpeakerOnlyConfigurationTypeDef = TypedDict(
    "ActiveSpeakerOnlyConfigurationTypeDef",
    {
        "ActiveSpeakerPosition": ActiveSpeakerPositionType,
    },
    total=False,
)

_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "_RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
    },
)
_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "_OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
    {
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "LanguageModelName": str,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "FilterPartialResults": bool,
        "PostCallAnalyticsSettings": "PostCallAnalyticsSettingsTypeDef",
        "CallAnalyticsStreamCategories": List[str],
    },
    total=False,
)

class AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef(
    _RequiredAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef,
    _OptionalAmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef,
):
    pass

AmazonTranscribeProcessorConfigurationTypeDef = TypedDict(
    "AmazonTranscribeProcessorConfigurationTypeDef",
    {
        "LanguageCode": CallAnalyticsLanguageCodeType,
        "VocabularyName": str,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethodType,
        "ShowSpeakerLabel": bool,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": PartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "LanguageModelName": str,
        "FilterPartialResults": bool,
        "IdentifyLanguage": bool,
        "LanguageOptions": str,
        "PreferredLanguage": CallAnalyticsLanguageCodeType,
        "VocabularyNames": str,
        "VocabularyFilterNames": str,
    },
    total=False,
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

_RequiredChannelDefinitionTypeDef = TypedDict(
    "_RequiredChannelDefinitionTypeDef",
    {
        "ChannelId": int,
    },
)
_OptionalChannelDefinitionTypeDef = TypedDict(
    "_OptionalChannelDefinitionTypeDef",
    {
        "ParticipantRole": ParticipantRoleType,
    },
    total=False,
)

class ChannelDefinitionTypeDef(
    _RequiredChannelDefinitionTypeDef, _OptionalChannelDefinitionTypeDef
):
    pass

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

_RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "ResourceAccessRoleArn": str,
        "Elements": List["MediaInsightsPipelineConfigurationElementTypeDef"],
    },
)
_OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "RealTimeAlertConfiguration": "RealTimeAlertConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef(
    _RequiredCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
    _OptionalCreateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
):
    pass

CreateMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "CreateMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": "MediaInsightsPipelineConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMediaInsightsPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaInsightsPipelineRequestRequestTypeDef",
    {
        "MediaInsightsPipelineConfigurationArn": str,
    },
)
_OptionalCreateMediaInsightsPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaInsightsPipelineRequestRequestTypeDef",
    {
        "KinesisVideoStreamSourceRuntimeConfiguration": "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
        "MediaInsightsRuntimeMetadata": Dict[str, str],
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration": "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
        "S3RecordingSinkRuntimeConfiguration": "S3RecordingSinkRuntimeConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientRequestToken": str,
    },
    total=False,
)

class CreateMediaInsightsPipelineRequestRequestTypeDef(
    _RequiredCreateMediaInsightsPipelineRequestRequestTypeDef,
    _OptionalCreateMediaInsightsPipelineRequestRequestTypeDef,
):
    pass

CreateMediaInsightsPipelineResponseTypeDef = TypedDict(
    "CreateMediaInsightsPipelineResponseTypeDef",
    {
        "MediaInsightsPipeline": "MediaInsightsPipelineTypeDef",
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

_RequiredCreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "StreamConfiguration": "KinesisVideoStreamConfigurationTypeDef",
        "PoolName": str,
    },
)
_OptionalCreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(
    _RequiredCreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef,
    _OptionalCreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef,
):
    pass

CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef = TypedDict(
    "CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    {
        "KinesisVideoStreamPoolConfiguration": "KinesisVideoStreamPoolConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMediaStreamPipelineRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMediaStreamPipelineRequestRequestTypeDef",
    {
        "Sources": List["MediaStreamSourceTypeDef"],
        "Sinks": List["MediaStreamSinkTypeDef"],
    },
)
_OptionalCreateMediaStreamPipelineRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMediaStreamPipelineRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMediaStreamPipelineRequestRequestTypeDef(
    _RequiredCreateMediaStreamPipelineRequestRequestTypeDef,
    _OptionalCreateMediaStreamPipelineRequestRequestTypeDef,
):
    pass

CreateMediaStreamPipelineResponseTypeDef = TypedDict(
    "CreateMediaStreamPipelineResponseTypeDef",
    {
        "MediaStreamPipeline": "MediaStreamPipelineTypeDef",
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

DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteMediaPipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaPipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": "TimestampRangeTypeDef",
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

GetMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "GetMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "GetMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": "MediaInsightsPipelineConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef = TypedDict(
    "GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    {
        "KinesisVideoStreamPoolConfiguration": "KinesisVideoStreamPoolConfigurationTypeDef",
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

GetSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "GetSpeakerSearchTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "SpeakerSearchTaskId": str,
    },
)

GetSpeakerSearchTaskResponseTypeDef = TypedDict(
    "GetSpeakerSearchTaskResponseTypeDef",
    {
        "SpeakerSearchTask": "SpeakerSearchTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "GetVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "VoiceToneAnalysisTaskId": str,
    },
)

GetVoiceToneAnalysisTaskResponseTypeDef = TypedDict(
    "GetVoiceToneAnalysisTaskResponseTypeDef",
    {
        "VoiceToneAnalysisTask": "VoiceToneAnalysisTaskTypeDef",
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
        "ActiveSpeakerOnlyConfiguration": "ActiveSpeakerOnlyConfigurationTypeDef",
        "HorizontalLayoutConfiguration": "HorizontalLayoutConfigurationTypeDef",
        "VerticalLayoutConfiguration": "VerticalLayoutConfigurationTypeDef",
        "VideoAttribute": "VideoAttributeTypeDef",
        "CanvasOrientation": CanvasOrientationType,
    },
    total=False,
)

class GridViewConfigurationTypeDef(
    _RequiredGridViewConfigurationTypeDef, _OptionalGridViewConfigurationTypeDef
):
    pass

HorizontalLayoutConfigurationTypeDef = TypedDict(
    "HorizontalLayoutConfigurationTypeDef",
    {
        "TileOrder": TileOrderType,
        "TilePosition": HorizontalTilePositionType,
        "TileCount": int,
        "TileAspectRatio": str,
    },
    total=False,
)

IssueDetectionConfigurationTypeDef = TypedDict(
    "IssueDetectionConfigurationTypeDef",
    {
        "RuleName": str,
    },
)

_RequiredKeywordMatchConfigurationTypeDef = TypedDict(
    "_RequiredKeywordMatchConfigurationTypeDef",
    {
        "RuleName": str,
        "Keywords": List[str],
    },
)
_OptionalKeywordMatchConfigurationTypeDef = TypedDict(
    "_OptionalKeywordMatchConfigurationTypeDef",
    {
        "Negate": bool,
    },
    total=False,
)

class KeywordMatchConfigurationTypeDef(
    _RequiredKeywordMatchConfigurationTypeDef, _OptionalKeywordMatchConfigurationTypeDef
):
    pass

KinesisDataStreamSinkConfigurationTypeDef = TypedDict(
    "KinesisDataStreamSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

_RequiredKinesisVideoStreamConfigurationTypeDef = TypedDict(
    "_RequiredKinesisVideoStreamConfigurationTypeDef",
    {
        "Region": str,
    },
)
_OptionalKinesisVideoStreamConfigurationTypeDef = TypedDict(
    "_OptionalKinesisVideoStreamConfigurationTypeDef",
    {
        "DataRetentionInHours": int,
    },
    total=False,
)

class KinesisVideoStreamConfigurationTypeDef(
    _RequiredKinesisVideoStreamConfigurationTypeDef, _OptionalKinesisVideoStreamConfigurationTypeDef
):
    pass

KinesisVideoStreamConfigurationUpdateTypeDef = TypedDict(
    "KinesisVideoStreamConfigurationUpdateTypeDef",
    {
        "DataRetentionInHours": int,
    },
    total=False,
)

KinesisVideoStreamPoolConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamPoolConfigurationTypeDef",
    {
        "PoolArn": str,
        "PoolName": str,
        "PoolId": str,
        "PoolStatus": KinesisVideoStreamPoolStatusType,
        "PoolSize": int,
        "StreamConfiguration": "KinesisVideoStreamConfigurationTypeDef",
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

KinesisVideoStreamPoolSummaryTypeDef = TypedDict(
    "KinesisVideoStreamPoolSummaryTypeDef",
    {
        "PoolName": str,
        "PoolId": str,
        "PoolArn": str,
    },
    total=False,
)

KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
    {
        "Streams": List["RecordingStreamConfigurationTypeDef"],
        "FragmentSelector": "FragmentSelectorTypeDef",
    },
)

KinesisVideoStreamSourceRuntimeConfigurationTypeDef = TypedDict(
    "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
    {
        "Streams": List["StreamConfigurationTypeDef"],
        "MediaEncoding": Literal["pcm"],
        "MediaSampleRate": int,
    },
)

_RequiredKinesisVideoStreamSourceTaskConfigurationTypeDef = TypedDict(
    "_RequiredKinesisVideoStreamSourceTaskConfigurationTypeDef",
    {
        "StreamArn": str,
        "ChannelId": int,
    },
)
_OptionalKinesisVideoStreamSourceTaskConfigurationTypeDef = TypedDict(
    "_OptionalKinesisVideoStreamSourceTaskConfigurationTypeDef",
    {
        "FragmentNumber": str,
    },
    total=False,
)

class KinesisVideoStreamSourceTaskConfigurationTypeDef(
    _RequiredKinesisVideoStreamSourceTaskConfigurationTypeDef,
    _OptionalKinesisVideoStreamSourceTaskConfigurationTypeDef,
):
    pass

LambdaFunctionSinkConfigurationTypeDef = TypedDict(
    "LambdaFunctionSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
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

ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef = TypedDict(
    "ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMediaInsightsPipelineConfigurationsResponseTypeDef = TypedDict(
    "ListMediaInsightsPipelineConfigurationsResponseTypeDef",
    {
        "MediaInsightsPipelineConfigurations": List[
            "MediaInsightsPipelineConfigurationSummaryTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef = TypedDict(
    "ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef = TypedDict(
    "ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef",
    {
        "KinesisVideoStreamPools": List["KinesisVideoStreamPoolSummaryTypeDef"],
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

_RequiredMediaInsightsPipelineConfigurationElementTypeDef = TypedDict(
    "_RequiredMediaInsightsPipelineConfigurationElementTypeDef",
    {
        "Type": MediaInsightsPipelineConfigurationElementTypeType,
    },
)
_OptionalMediaInsightsPipelineConfigurationElementTypeDef = TypedDict(
    "_OptionalMediaInsightsPipelineConfigurationElementTypeDef",
    {
        "AmazonTranscribeCallAnalyticsProcessorConfiguration": "AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef",
        "AmazonTranscribeProcessorConfiguration": "AmazonTranscribeProcessorConfigurationTypeDef",
        "KinesisDataStreamSinkConfiguration": "KinesisDataStreamSinkConfigurationTypeDef",
        "S3RecordingSinkConfiguration": "S3RecordingSinkConfigurationTypeDef",
        "VoiceAnalyticsProcessorConfiguration": "VoiceAnalyticsProcessorConfigurationTypeDef",
        "LambdaFunctionSinkConfiguration": "LambdaFunctionSinkConfigurationTypeDef",
        "SqsQueueSinkConfiguration": "SqsQueueSinkConfigurationTypeDef",
        "SnsTopicSinkConfiguration": "SnsTopicSinkConfigurationTypeDef",
        "VoiceEnhancementSinkConfiguration": "VoiceEnhancementSinkConfigurationTypeDef",
    },
    total=False,
)

class MediaInsightsPipelineConfigurationElementTypeDef(
    _RequiredMediaInsightsPipelineConfigurationElementTypeDef,
    _OptionalMediaInsightsPipelineConfigurationElementTypeDef,
):
    pass

MediaInsightsPipelineConfigurationSummaryTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationSummaryTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "MediaInsightsPipelineConfigurationId": str,
        "MediaInsightsPipelineConfigurationArn": str,
    },
    total=False,
)

MediaInsightsPipelineConfigurationTypeDef = TypedDict(
    "MediaInsightsPipelineConfigurationTypeDef",
    {
        "MediaInsightsPipelineConfigurationName": str,
        "MediaInsightsPipelineConfigurationArn": str,
        "ResourceAccessRoleArn": str,
        "RealTimeAlertConfiguration": "RealTimeAlertConfigurationTypeDef",
        "Elements": List["MediaInsightsPipelineConfigurationElementTypeDef"],
        "MediaInsightsPipelineConfigurationId": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

MediaInsightsPipelineElementStatusTypeDef = TypedDict(
    "MediaInsightsPipelineElementStatusTypeDef",
    {
        "Type": MediaInsightsPipelineConfigurationElementTypeType,
        "Status": MediaPipelineElementStatusType,
    },
    total=False,
)

MediaInsightsPipelineTypeDef = TypedDict(
    "MediaInsightsPipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "MediaInsightsPipelineConfigurationArn": str,
        "Status": MediaPipelineStatusType,
        "KinesisVideoStreamSourceRuntimeConfiguration": "KinesisVideoStreamSourceRuntimeConfigurationTypeDef",
        "MediaInsightsRuntimeMetadata": Dict[str, str],
        "KinesisVideoStreamRecordingSourceRuntimeConfiguration": "KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef",
        "S3RecordingSinkRuntimeConfiguration": "S3RecordingSinkRuntimeConfigurationTypeDef",
        "CreatedTimestamp": datetime,
        "ElementStatuses": List["MediaInsightsPipelineElementStatusTypeDef"],
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
        "MediaInsightsPipeline": "MediaInsightsPipelineTypeDef",
        "MediaStreamPipeline": "MediaStreamPipelineTypeDef",
    },
    total=False,
)

MediaStreamPipelineTypeDef = TypedDict(
    "MediaStreamPipelineTypeDef",
    {
        "MediaPipelineId": str,
        "MediaPipelineArn": str,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "Status": MediaPipelineStatusType,
        "Sources": List["MediaStreamSourceTypeDef"],
        "Sinks": List["MediaStreamSinkTypeDef"],
    },
    total=False,
)

MediaStreamSinkTypeDef = TypedDict(
    "MediaStreamSinkTypeDef",
    {
        "SinkArn": str,
        "SinkType": Literal["KinesisVideoStreamPool"],
        "ReservedStreamCapacity": int,
        "MediaStreamType": MediaStreamTypeType,
    },
)

MediaStreamSourceTypeDef = TypedDict(
    "MediaStreamSourceTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
    },
)

MeetingEventsConcatenationConfigurationTypeDef = TypedDict(
    "MeetingEventsConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

_RequiredPostCallAnalyticsSettingsTypeDef = TypedDict(
    "_RequiredPostCallAnalyticsSettingsTypeDef",
    {
        "OutputLocation": str,
        "DataAccessRoleArn": str,
    },
)
_OptionalPostCallAnalyticsSettingsTypeDef = TypedDict(
    "_OptionalPostCallAnalyticsSettingsTypeDef",
    {
        "ContentRedactionOutput": ContentRedactionOutputType,
        "OutputEncryptionKMSKeyId": str,
    },
    total=False,
)

class PostCallAnalyticsSettingsTypeDef(
    _RequiredPostCallAnalyticsSettingsTypeDef, _OptionalPostCallAnalyticsSettingsTypeDef
):
    pass

PresenterOnlyConfigurationTypeDef = TypedDict(
    "PresenterOnlyConfigurationTypeDef",
    {
        "PresenterPosition": PresenterPositionType,
    },
    total=False,
)

RealTimeAlertConfigurationTypeDef = TypedDict(
    "RealTimeAlertConfigurationTypeDef",
    {
        "Disabled": bool,
        "Rules": List["RealTimeAlertRuleTypeDef"],
    },
    total=False,
)

_RequiredRealTimeAlertRuleTypeDef = TypedDict(
    "_RequiredRealTimeAlertRuleTypeDef",
    {
        "Type": RealTimeAlertRuleTypeType,
    },
)
_OptionalRealTimeAlertRuleTypeDef = TypedDict(
    "_OptionalRealTimeAlertRuleTypeDef",
    {
        "KeywordMatchConfiguration": "KeywordMatchConfigurationTypeDef",
        "SentimentConfiguration": "SentimentConfigurationTypeDef",
        "IssueDetectionConfiguration": "IssueDetectionConfigurationTypeDef",
    },
    total=False,
)

class RealTimeAlertRuleTypeDef(
    _RequiredRealTimeAlertRuleTypeDef, _OptionalRealTimeAlertRuleTypeDef
):
    pass

RecordingStreamConfigurationTypeDef = TypedDict(
    "RecordingStreamConfigurationTypeDef",
    {
        "StreamArn": str,
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

S3RecordingSinkConfigurationTypeDef = TypedDict(
    "S3RecordingSinkConfigurationTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
    },
    total=False,
)

S3RecordingSinkRuntimeConfigurationTypeDef = TypedDict(
    "S3RecordingSinkRuntimeConfigurationTypeDef",
    {
        "Destination": str,
        "RecordingFileFormat": RecordingFileFormatType,
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

SentimentConfigurationTypeDef = TypedDict(
    "SentimentConfigurationTypeDef",
    {
        "RuleName": str,
        "SentimentType": Literal["NEGATIVE"],
        "TimePeriod": int,
    },
)

SnsTopicSinkConfigurationTypeDef = TypedDict(
    "SnsTopicSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
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

SpeakerSearchTaskTypeDef = TypedDict(
    "SpeakerSearchTaskTypeDef",
    {
        "SpeakerSearchTaskId": str,
        "SpeakerSearchTaskStatus": MediaPipelineTaskStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)

SqsQueueSinkConfigurationTypeDef = TypedDict(
    "SqsQueueSinkConfigurationTypeDef",
    {
        "InsightsTarget": str,
    },
    total=False,
)

_RequiredStartSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartSpeakerSearchTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "VoiceProfileDomainArn": str,
    },
)
_OptionalStartSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartSpeakerSearchTaskRequestRequestTypeDef",
    {
        "KinesisVideoStreamSourceTaskConfiguration": "KinesisVideoStreamSourceTaskConfigurationTypeDef",
        "ClientRequestToken": str,
    },
    total=False,
)

class StartSpeakerSearchTaskRequestRequestTypeDef(
    _RequiredStartSpeakerSearchTaskRequestRequestTypeDef,
    _OptionalStartSpeakerSearchTaskRequestRequestTypeDef,
):
    pass

StartSpeakerSearchTaskResponseTypeDef = TypedDict(
    "StartSpeakerSearchTaskResponseTypeDef",
    {
        "SpeakerSearchTask": "SpeakerSearchTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "LanguageCode": Literal["en-US"],
    },
)
_OptionalStartVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "KinesisVideoStreamSourceTaskConfiguration": "KinesisVideoStreamSourceTaskConfigurationTypeDef",
        "ClientRequestToken": str,
    },
    total=False,
)

class StartVoiceToneAnalysisTaskRequestRequestTypeDef(
    _RequiredStartVoiceToneAnalysisTaskRequestRequestTypeDef,
    _OptionalStartVoiceToneAnalysisTaskRequestRequestTypeDef,
):
    pass

StartVoiceToneAnalysisTaskResponseTypeDef = TypedDict(
    "StartVoiceToneAnalysisTaskResponseTypeDef",
    {
        "VoiceToneAnalysisTask": "VoiceToneAnalysisTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSpeakerSearchTaskRequestRequestTypeDef = TypedDict(
    "StopSpeakerSearchTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "SpeakerSearchTaskId": str,
    },
)

StopVoiceToneAnalysisTaskRequestRequestTypeDef = TypedDict(
    "StopVoiceToneAnalysisTaskRequestRequestTypeDef",
    {
        "Identifier": str,
        "VoiceToneAnalysisTaskId": str,
    },
)

_RequiredStreamChannelDefinitionTypeDef = TypedDict(
    "_RequiredStreamChannelDefinitionTypeDef",
    {
        "NumberOfChannels": int,
    },
)
_OptionalStreamChannelDefinitionTypeDef = TypedDict(
    "_OptionalStreamChannelDefinitionTypeDef",
    {
        "ChannelDefinitions": List["ChannelDefinitionTypeDef"],
    },
    total=False,
)

class StreamChannelDefinitionTypeDef(
    _RequiredStreamChannelDefinitionTypeDef, _OptionalStreamChannelDefinitionTypeDef
):
    pass

_RequiredStreamConfigurationTypeDef = TypedDict(
    "_RequiredStreamConfigurationTypeDef",
    {
        "StreamArn": str,
        "StreamChannelDefinition": "StreamChannelDefinitionTypeDef",
    },
)
_OptionalStreamConfigurationTypeDef = TypedDict(
    "_OptionalStreamConfigurationTypeDef",
    {
        "FragmentNumber": str,
    },
    total=False,
)

class StreamConfigurationTypeDef(
    _RequiredStreamConfigurationTypeDef, _OptionalStreamConfigurationTypeDef
):
    pass

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

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
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

_RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "ResourceAccessRoleArn": str,
        "Elements": List["MediaInsightsPipelineConfigurationElementTypeDef"],
    },
)
_OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef",
    {
        "RealTimeAlertConfiguration": "RealTimeAlertConfigurationTypeDef",
    },
    total=False,
)

class UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef(
    _RequiredUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
    _OptionalUpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef,
):
    pass

UpdateMediaInsightsPipelineConfigurationResponseTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineConfigurationResponseTypeDef",
    {
        "MediaInsightsPipelineConfiguration": "MediaInsightsPipelineConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMediaInsightsPipelineStatusRequestRequestTypeDef = TypedDict(
    "UpdateMediaInsightsPipelineStatusRequestRequestTypeDef",
    {
        "Identifier": str,
        "UpdateStatus": MediaPipelineStatusUpdateType,
    },
)

_RequiredUpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef",
    {
        "StreamConfiguration": "KinesisVideoStreamConfigurationUpdateTypeDef",
    },
    total=False,
)

class UpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(
    _RequiredUpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef,
    _OptionalUpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef,
):
    pass

UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef = TypedDict(
    "UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef",
    {
        "KinesisVideoStreamPoolConfiguration": "KinesisVideoStreamPoolConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VerticalLayoutConfigurationTypeDef = TypedDict(
    "VerticalLayoutConfigurationTypeDef",
    {
        "TileOrder": TileOrderType,
        "TilePosition": VerticalTilePositionType,
        "TileCount": int,
        "TileAspectRatio": str,
    },
    total=False,
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

VideoAttributeTypeDef = TypedDict(
    "VideoAttributeTypeDef",
    {
        "CornerRadius": int,
        "BorderColor": BorderColorType,
        "HighlightColor": HighlightColorType,
        "BorderThickness": int,
    },
    total=False,
)

VideoConcatenationConfigurationTypeDef = TypedDict(
    "VideoConcatenationConfigurationTypeDef",
    {
        "State": ArtifactsConcatenationStateType,
    },
)

VoiceAnalyticsProcessorConfigurationTypeDef = TypedDict(
    "VoiceAnalyticsProcessorConfigurationTypeDef",
    {
        "SpeakerSearchStatus": VoiceAnalyticsConfigurationStatusType,
        "VoiceToneAnalysisStatus": VoiceAnalyticsConfigurationStatusType,
    },
    total=False,
)

VoiceEnhancementSinkConfigurationTypeDef = TypedDict(
    "VoiceEnhancementSinkConfigurationTypeDef",
    {
        "Disabled": bool,
    },
    total=False,
)

VoiceToneAnalysisTaskTypeDef = TypedDict(
    "VoiceToneAnalysisTaskTypeDef",
    {
        "VoiceToneAnalysisTaskId": str,
        "VoiceToneAnalysisTaskStatus": MediaPipelineTaskStatusType,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
    },
    total=False,
)
