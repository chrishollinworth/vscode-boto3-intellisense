"""
Type annotations for ivs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivs.type_defs import AudioConfigurationTypeDef

    data: AudioConfigurationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ChannelLatencyModeType,
    ChannelTypeType,
    RecordingConfigurationStateType,
    RecordingModeType,
    RenditionConfigurationRenditionSelectionType,
    RenditionConfigurationRenditionType,
    StreamHealthType,
    StreamStateType,
    ThumbnailConfigurationResolutionType,
    ThumbnailConfigurationStorageType,
    TranscodePresetType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AudioConfigurationTypeDef",
    "BatchErrorTypeDef",
    "BatchGetChannelRequestRequestTypeDef",
    "BatchGetChannelResponseTypeDef",
    "BatchGetStreamKeyRequestRequestTypeDef",
    "BatchGetStreamKeyResponseTypeDef",
    "BatchStartViewerSessionRevocationErrorTypeDef",
    "BatchStartViewerSessionRevocationRequestRequestTypeDef",
    "BatchStartViewerSessionRevocationResponseTypeDef",
    "BatchStartViewerSessionRevocationViewerSessionTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreatePlaybackRestrictionPolicyRequestRequestTypeDef",
    "CreatePlaybackRestrictionPolicyResponseTypeDef",
    "CreateRecordingConfigurationRequestRequestTypeDef",
    "CreateRecordingConfigurationResponseTypeDef",
    "CreateStreamKeyRequestRequestTypeDef",
    "CreateStreamKeyResponseTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeletePlaybackKeyPairRequestRequestTypeDef",
    "DeletePlaybackRestrictionPolicyRequestRequestTypeDef",
    "DeleteRecordingConfigurationRequestRequestTypeDef",
    "DeleteStreamKeyRequestRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "GetChannelRequestRequestTypeDef",
    "GetChannelResponseTypeDef",
    "GetPlaybackKeyPairRequestRequestTypeDef",
    "GetPlaybackKeyPairResponseTypeDef",
    "GetPlaybackRestrictionPolicyRequestRequestTypeDef",
    "GetPlaybackRestrictionPolicyResponseTypeDef",
    "GetRecordingConfigurationRequestRequestTypeDef",
    "GetRecordingConfigurationResponseTypeDef",
    "GetStreamKeyRequestRequestTypeDef",
    "GetStreamKeyResponseTypeDef",
    "GetStreamRequestRequestTypeDef",
    "GetStreamResponseTypeDef",
    "GetStreamSessionRequestRequestTypeDef",
    "GetStreamSessionResponseTypeDef",
    "ImportPlaybackKeyPairRequestRequestTypeDef",
    "ImportPlaybackKeyPairResponseTypeDef",
    "IngestConfigurationTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListPlaybackKeyPairsRequestRequestTypeDef",
    "ListPlaybackKeyPairsResponseTypeDef",
    "ListPlaybackRestrictionPoliciesRequestRequestTypeDef",
    "ListPlaybackRestrictionPoliciesResponseTypeDef",
    "ListRecordingConfigurationsRequestRequestTypeDef",
    "ListRecordingConfigurationsResponseTypeDef",
    "ListStreamKeysRequestRequestTypeDef",
    "ListStreamKeysResponseTypeDef",
    "ListStreamSessionsRequestRequestTypeDef",
    "ListStreamSessionsResponseTypeDef",
    "ListStreamsRequestRequestTypeDef",
    "ListStreamsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlaybackKeyPairSummaryTypeDef",
    "PlaybackKeyPairTypeDef",
    "PlaybackRestrictionPolicySummaryTypeDef",
    "PlaybackRestrictionPolicyTypeDef",
    "PutMetadataRequestRequestTypeDef",
    "RecordingConfigurationSummaryTypeDef",
    "RecordingConfigurationTypeDef",
    "RenditionConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigurationTypeDef",
    "SrtTypeDef",
    "StartViewerSessionRevocationRequestRequestTypeDef",
    "StopStreamRequestRequestTypeDef",
    "StreamEventTypeDef",
    "StreamFiltersTypeDef",
    "StreamKeySummaryTypeDef",
    "StreamKeyTypeDef",
    "StreamSessionSummaryTypeDef",
    "StreamSessionTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThumbnailConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdatePlaybackRestrictionPolicyRequestRequestTypeDef",
    "UpdatePlaybackRestrictionPolicyResponseTypeDef",
    "VideoConfigurationTypeDef",
)

AudioConfigurationTypeDef = TypedDict(
    "AudioConfigurationTypeDef",
    {
        "channels": int,
        "codec": str,
        "sampleRate": int,
        "targetBitrate": int,
    },
    total=False,
)

BatchErrorTypeDef = TypedDict(
    "BatchErrorTypeDef",
    {
        "arn": str,
        "code": str,
        "message": str,
    },
    total=False,
)

BatchGetChannelRequestRequestTypeDef = TypedDict(
    "BatchGetChannelRequestRequestTypeDef",
    {
        "arns": List[str],
    },
)

BatchGetChannelResponseTypeDef = TypedDict(
    "BatchGetChannelResponseTypeDef",
    {
        "channels": List["ChannelTypeDef"],
        "errors": List["BatchErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetStreamKeyRequestRequestTypeDef = TypedDict(
    "BatchGetStreamKeyRequestRequestTypeDef",
    {
        "arns": List[str],
    },
)

BatchGetStreamKeyResponseTypeDef = TypedDict(
    "BatchGetStreamKeyResponseTypeDef",
    {
        "errors": List["BatchErrorTypeDef"],
        "streamKeys": List["StreamKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchStartViewerSessionRevocationErrorTypeDef = TypedDict(
    "_RequiredBatchStartViewerSessionRevocationErrorTypeDef",
    {
        "channelArn": str,
        "viewerId": str,
    },
)
_OptionalBatchStartViewerSessionRevocationErrorTypeDef = TypedDict(
    "_OptionalBatchStartViewerSessionRevocationErrorTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

class BatchStartViewerSessionRevocationErrorTypeDef(
    _RequiredBatchStartViewerSessionRevocationErrorTypeDef,
    _OptionalBatchStartViewerSessionRevocationErrorTypeDef,
):
    pass

BatchStartViewerSessionRevocationRequestRequestTypeDef = TypedDict(
    "BatchStartViewerSessionRevocationRequestRequestTypeDef",
    {
        "viewerSessions": List["BatchStartViewerSessionRevocationViewerSessionTypeDef"],
    },
)

BatchStartViewerSessionRevocationResponseTypeDef = TypedDict(
    "BatchStartViewerSessionRevocationResponseTypeDef",
    {
        "errors": List["BatchStartViewerSessionRevocationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchStartViewerSessionRevocationViewerSessionTypeDef = TypedDict(
    "_RequiredBatchStartViewerSessionRevocationViewerSessionTypeDef",
    {
        "channelArn": str,
        "viewerId": str,
    },
)
_OptionalBatchStartViewerSessionRevocationViewerSessionTypeDef = TypedDict(
    "_OptionalBatchStartViewerSessionRevocationViewerSessionTypeDef",
    {
        "viewerSessionVersionsLessThanOrEqualTo": int,
    },
    total=False,
)

class BatchStartViewerSessionRevocationViewerSessionTypeDef(
    _RequiredBatchStartViewerSessionRevocationViewerSessionTypeDef,
    _OptionalBatchStartViewerSessionRevocationViewerSessionTypeDef,
):
    pass

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "arn": str,
        "authorized": bool,
        "insecureIngest": bool,
        "latencyMode": ChannelLatencyModeType,
        "name": str,
        "playbackRestrictionPolicyArn": str,
        "preset": TranscodePresetType,
        "recordingConfigurationArn": str,
        "tags": Dict[str, str],
        "type": ChannelTypeType,
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "arn": str,
        "authorized": bool,
        "ingestEndpoint": str,
        "insecureIngest": bool,
        "latencyMode": ChannelLatencyModeType,
        "name": str,
        "playbackRestrictionPolicyArn": str,
        "playbackUrl": str,
        "preset": TranscodePresetType,
        "recordingConfigurationArn": str,
        "srt": "SrtTypeDef",
        "tags": Dict[str, str],
        "type": ChannelTypeType,
    },
    total=False,
)

CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "authorized": bool,
        "insecureIngest": bool,
        "latencyMode": ChannelLatencyModeType,
        "name": str,
        "playbackRestrictionPolicyArn": str,
        "preset": TranscodePresetType,
        "recordingConfigurationArn": str,
        "tags": Dict[str, str],
        "type": ChannelTypeType,
    },
    total=False,
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlaybackRestrictionPolicyRequestRequestTypeDef = TypedDict(
    "CreatePlaybackRestrictionPolicyRequestRequestTypeDef",
    {
        "allowedCountries": List[str],
        "allowedOrigins": List[str],
        "enableStrictOriginEnforcement": bool,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

CreatePlaybackRestrictionPolicyResponseTypeDef = TypedDict(
    "CreatePlaybackRestrictionPolicyResponseTypeDef",
    {
        "playbackRestrictionPolicy": "PlaybackRestrictionPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecordingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRecordingConfigurationRequestRequestTypeDef",
    {
        "destinationConfiguration": "DestinationConfigurationTypeDef",
    },
)
_OptionalCreateRecordingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRecordingConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "recordingReconnectWindowSeconds": int,
        "renditionConfiguration": "RenditionConfigurationTypeDef",
        "tags": Dict[str, str],
        "thumbnailConfiguration": "ThumbnailConfigurationTypeDef",
    },
    total=False,
)

class CreateRecordingConfigurationRequestRequestTypeDef(
    _RequiredCreateRecordingConfigurationRequestRequestTypeDef,
    _OptionalCreateRecordingConfigurationRequestRequestTypeDef,
):
    pass

CreateRecordingConfigurationResponseTypeDef = TypedDict(
    "CreateRecordingConfigurationResponseTypeDef",
    {
        "recordingConfiguration": "RecordingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamKeyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStreamKeyRequestRequestTypeDef",
    {
        "channelArn": str,
    },
)
_OptionalCreateStreamKeyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStreamKeyRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateStreamKeyRequestRequestTypeDef(
    _RequiredCreateStreamKeyRequestRequestTypeDef, _OptionalCreateStreamKeyRequestRequestTypeDef
):
    pass

CreateStreamKeyResponseTypeDef = TypedDict(
    "CreateStreamKeyResponseTypeDef",
    {
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeletePlaybackKeyPairRequestRequestTypeDef = TypedDict(
    "DeletePlaybackKeyPairRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeletePlaybackRestrictionPolicyRequestRequestTypeDef = TypedDict(
    "DeletePlaybackRestrictionPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRecordingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRecordingConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteStreamKeyRequestRequestTypeDef = TypedDict(
    "DeleteStreamKeyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "s3": "S3DestinationConfigurationTypeDef",
    },
    total=False,
)

GetChannelRequestRequestTypeDef = TypedDict(
    "GetChannelRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetChannelResponseTypeDef = TypedDict(
    "GetChannelResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlaybackKeyPairRequestRequestTypeDef = TypedDict(
    "GetPlaybackKeyPairRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetPlaybackKeyPairResponseTypeDef = TypedDict(
    "GetPlaybackKeyPairResponseTypeDef",
    {
        "keyPair": "PlaybackKeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlaybackRestrictionPolicyRequestRequestTypeDef = TypedDict(
    "GetPlaybackRestrictionPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetPlaybackRestrictionPolicyResponseTypeDef = TypedDict(
    "GetPlaybackRestrictionPolicyResponseTypeDef",
    {
        "playbackRestrictionPolicy": "PlaybackRestrictionPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecordingConfigurationRequestRequestTypeDef = TypedDict(
    "GetRecordingConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetRecordingConfigurationResponseTypeDef = TypedDict(
    "GetRecordingConfigurationResponseTypeDef",
    {
        "recordingConfiguration": "RecordingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamKeyRequestRequestTypeDef = TypedDict(
    "GetStreamKeyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetStreamKeyResponseTypeDef = TypedDict(
    "GetStreamKeyResponseTypeDef",
    {
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamRequestRequestTypeDef = TypedDict(
    "GetStreamRequestRequestTypeDef",
    {
        "channelArn": str,
    },
)

GetStreamResponseTypeDef = TypedDict(
    "GetStreamResponseTypeDef",
    {
        "stream": "StreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetStreamSessionRequestRequestTypeDef = TypedDict(
    "_RequiredGetStreamSessionRequestRequestTypeDef",
    {
        "channelArn": str,
    },
)
_OptionalGetStreamSessionRequestRequestTypeDef = TypedDict(
    "_OptionalGetStreamSessionRequestRequestTypeDef",
    {
        "streamId": str,
    },
    total=False,
)

class GetStreamSessionRequestRequestTypeDef(
    _RequiredGetStreamSessionRequestRequestTypeDef, _OptionalGetStreamSessionRequestRequestTypeDef
):
    pass

GetStreamSessionResponseTypeDef = TypedDict(
    "GetStreamSessionResponseTypeDef",
    {
        "streamSession": "StreamSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportPlaybackKeyPairRequestRequestTypeDef = TypedDict(
    "_RequiredImportPlaybackKeyPairRequestRequestTypeDef",
    {
        "publicKeyMaterial": str,
    },
)
_OptionalImportPlaybackKeyPairRequestRequestTypeDef = TypedDict(
    "_OptionalImportPlaybackKeyPairRequestRequestTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ImportPlaybackKeyPairRequestRequestTypeDef(
    _RequiredImportPlaybackKeyPairRequestRequestTypeDef,
    _OptionalImportPlaybackKeyPairRequestRequestTypeDef,
):
    pass

ImportPlaybackKeyPairResponseTypeDef = TypedDict(
    "ImportPlaybackKeyPairResponseTypeDef",
    {
        "keyPair": "PlaybackKeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IngestConfigurationTypeDef = TypedDict(
    "IngestConfigurationTypeDef",
    {
        "audio": "AudioConfigurationTypeDef",
        "video": "VideoConfigurationTypeDef",
    },
    total=False,
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "filterByName": str,
        "filterByPlaybackRestrictionPolicyArn": str,
        "filterByRecordingConfigurationArn": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "channels": List["ChannelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaybackKeyPairsRequestRequestTypeDef = TypedDict(
    "ListPlaybackKeyPairsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListPlaybackKeyPairsResponseTypeDef = TypedDict(
    "ListPlaybackKeyPairsResponseTypeDef",
    {
        "keyPairs": List["PlaybackKeyPairSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaybackRestrictionPoliciesRequestRequestTypeDef = TypedDict(
    "ListPlaybackRestrictionPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListPlaybackRestrictionPoliciesResponseTypeDef = TypedDict(
    "ListPlaybackRestrictionPoliciesResponseTypeDef",
    {
        "nextToken": str,
        "playbackRestrictionPolicies": List["PlaybackRestrictionPolicySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListRecordingConfigurationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListRecordingConfigurationsResponseTypeDef = TypedDict(
    "ListRecordingConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "recordingConfigurations": List["RecordingConfigurationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListStreamKeysRequestRequestTypeDef",
    {
        "channelArn": str,
    },
)
_OptionalListStreamKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListStreamKeysRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListStreamKeysRequestRequestTypeDef(
    _RequiredListStreamKeysRequestRequestTypeDef, _OptionalListStreamKeysRequestRequestTypeDef
):
    pass

ListStreamKeysResponseTypeDef = TypedDict(
    "ListStreamKeysResponseTypeDef",
    {
        "nextToken": str,
        "streamKeys": List["StreamKeySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListStreamSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredListStreamSessionsRequestRequestTypeDef",
    {
        "channelArn": str,
    },
)
_OptionalListStreamSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalListStreamSessionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListStreamSessionsRequestRequestTypeDef(
    _RequiredListStreamSessionsRequestRequestTypeDef,
    _OptionalListStreamSessionsRequestRequestTypeDef,
):
    pass

ListStreamSessionsResponseTypeDef = TypedDict(
    "ListStreamSessionsResponseTypeDef",
    {
        "nextToken": str,
        "streamSessions": List["StreamSessionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsRequestRequestTypeDef = TypedDict(
    "ListStreamsRequestRequestTypeDef",
    {
        "filterBy": "StreamFiltersTypeDef",
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListStreamsResponseTypeDef = TypedDict(
    "ListStreamsResponseTypeDef",
    {
        "nextToken": str,
        "streams": List["StreamSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PlaybackKeyPairSummaryTypeDef = TypedDict(
    "PlaybackKeyPairSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

PlaybackKeyPairTypeDef = TypedDict(
    "PlaybackKeyPairTypeDef",
    {
        "arn": str,
        "fingerprint": str,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredPlaybackRestrictionPolicySummaryTypeDef = TypedDict(
    "_RequiredPlaybackRestrictionPolicySummaryTypeDef",
    {
        "allowedCountries": List[str],
        "allowedOrigins": List[str],
        "arn": str,
    },
)
_OptionalPlaybackRestrictionPolicySummaryTypeDef = TypedDict(
    "_OptionalPlaybackRestrictionPolicySummaryTypeDef",
    {
        "enableStrictOriginEnforcement": bool,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class PlaybackRestrictionPolicySummaryTypeDef(
    _RequiredPlaybackRestrictionPolicySummaryTypeDef,
    _OptionalPlaybackRestrictionPolicySummaryTypeDef,
):
    pass

_RequiredPlaybackRestrictionPolicyTypeDef = TypedDict(
    "_RequiredPlaybackRestrictionPolicyTypeDef",
    {
        "allowedCountries": List[str],
        "allowedOrigins": List[str],
        "arn": str,
    },
)
_OptionalPlaybackRestrictionPolicyTypeDef = TypedDict(
    "_OptionalPlaybackRestrictionPolicyTypeDef",
    {
        "enableStrictOriginEnforcement": bool,
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class PlaybackRestrictionPolicyTypeDef(
    _RequiredPlaybackRestrictionPolicyTypeDef, _OptionalPlaybackRestrictionPolicyTypeDef
):
    pass

PutMetadataRequestRequestTypeDef = TypedDict(
    "PutMetadataRequestRequestTypeDef",
    {
        "channelArn": str,
        "metadata": str,
    },
)

_RequiredRecordingConfigurationSummaryTypeDef = TypedDict(
    "_RequiredRecordingConfigurationSummaryTypeDef",
    {
        "arn": str,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "state": RecordingConfigurationStateType,
    },
)
_OptionalRecordingConfigurationSummaryTypeDef = TypedDict(
    "_OptionalRecordingConfigurationSummaryTypeDef",
    {
        "name": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class RecordingConfigurationSummaryTypeDef(
    _RequiredRecordingConfigurationSummaryTypeDef, _OptionalRecordingConfigurationSummaryTypeDef
):
    pass

_RequiredRecordingConfigurationTypeDef = TypedDict(
    "_RequiredRecordingConfigurationTypeDef",
    {
        "arn": str,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "state": RecordingConfigurationStateType,
    },
)
_OptionalRecordingConfigurationTypeDef = TypedDict(
    "_OptionalRecordingConfigurationTypeDef",
    {
        "name": str,
        "recordingReconnectWindowSeconds": int,
        "renditionConfiguration": "RenditionConfigurationTypeDef",
        "tags": Dict[str, str],
        "thumbnailConfiguration": "ThumbnailConfigurationTypeDef",
    },
    total=False,
)

class RecordingConfigurationTypeDef(
    _RequiredRecordingConfigurationTypeDef, _OptionalRecordingConfigurationTypeDef
):
    pass

RenditionConfigurationTypeDef = TypedDict(
    "RenditionConfigurationTypeDef",
    {
        "renditionSelection": RenditionConfigurationRenditionSelectionType,
        "renditions": List[RenditionConfigurationRenditionType],
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

S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "bucketName": str,
    },
)

SrtTypeDef = TypedDict(
    "SrtTypeDef",
    {
        "endpoint": str,
        "passphrase": str,
    },
    total=False,
)

_RequiredStartViewerSessionRevocationRequestRequestTypeDef = TypedDict(
    "_RequiredStartViewerSessionRevocationRequestRequestTypeDef",
    {
        "channelArn": str,
        "viewerId": str,
    },
)
_OptionalStartViewerSessionRevocationRequestRequestTypeDef = TypedDict(
    "_OptionalStartViewerSessionRevocationRequestRequestTypeDef",
    {
        "viewerSessionVersionsLessThanOrEqualTo": int,
    },
    total=False,
)

class StartViewerSessionRevocationRequestRequestTypeDef(
    _RequiredStartViewerSessionRevocationRequestRequestTypeDef,
    _OptionalStartViewerSessionRevocationRequestRequestTypeDef,
):
    pass

StopStreamRequestRequestTypeDef = TypedDict(
    "StopStreamRequestRequestTypeDef",
    {
        "channelArn": str,
    },
)

StreamEventTypeDef = TypedDict(
    "StreamEventTypeDef",
    {
        "eventTime": datetime,
        "name": str,
        "type": str,
    },
    total=False,
)

StreamFiltersTypeDef = TypedDict(
    "StreamFiltersTypeDef",
    {
        "health": StreamHealthType,
    },
    total=False,
)

StreamKeySummaryTypeDef = TypedDict(
    "StreamKeySummaryTypeDef",
    {
        "arn": str,
        "channelArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

StreamKeyTypeDef = TypedDict(
    "StreamKeyTypeDef",
    {
        "arn": str,
        "channelArn": str,
        "tags": Dict[str, str],
        "value": str,
    },
    total=False,
)

StreamSessionSummaryTypeDef = TypedDict(
    "StreamSessionSummaryTypeDef",
    {
        "endTime": datetime,
        "hasErrorEvent": bool,
        "startTime": datetime,
        "streamId": str,
    },
    total=False,
)

StreamSessionTypeDef = TypedDict(
    "StreamSessionTypeDef",
    {
        "channel": "ChannelTypeDef",
        "endTime": datetime,
        "ingestConfiguration": "IngestConfigurationTypeDef",
        "recordingConfiguration": "RecordingConfigurationTypeDef",
        "startTime": datetime,
        "streamId": str,
        "truncatedEvents": List["StreamEventTypeDef"],
    },
    total=False,
)

StreamSummaryTypeDef = TypedDict(
    "StreamSummaryTypeDef",
    {
        "channelArn": str,
        "health": StreamHealthType,
        "startTime": datetime,
        "state": StreamStateType,
        "streamId": str,
        "viewerCount": int,
    },
    total=False,
)

StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "channelArn": str,
        "health": StreamHealthType,
        "playbackUrl": str,
        "startTime": datetime,
        "state": StreamStateType,
        "streamId": str,
        "viewerCount": int,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

ThumbnailConfigurationTypeDef = TypedDict(
    "ThumbnailConfigurationTypeDef",
    {
        "recordingMode": RecordingModeType,
        "resolution": ThumbnailConfigurationResolutionType,
        "storage": List[ThumbnailConfigurationStorageType],
        "targetIntervalSeconds": int,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "authorized": bool,
        "insecureIngest": bool,
        "latencyMode": ChannelLatencyModeType,
        "name": str,
        "playbackRestrictionPolicyArn": str,
        "preset": TranscodePresetType,
        "recordingConfigurationArn": str,
        "type": ChannelTypeType,
    },
    total=False,
)

class UpdateChannelRequestRequestTypeDef(
    _RequiredUpdateChannelRequestRequestTypeDef, _OptionalUpdateChannelRequestRequestTypeDef
):
    pass

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePlaybackRestrictionPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePlaybackRestrictionPolicyRequestRequestTypeDef",
    {
        "arn": str,
    },
)
_OptionalUpdatePlaybackRestrictionPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePlaybackRestrictionPolicyRequestRequestTypeDef",
    {
        "allowedCountries": List[str],
        "allowedOrigins": List[str],
        "enableStrictOriginEnforcement": bool,
        "name": str,
    },
    total=False,
)

class UpdatePlaybackRestrictionPolicyRequestRequestTypeDef(
    _RequiredUpdatePlaybackRestrictionPolicyRequestRequestTypeDef,
    _OptionalUpdatePlaybackRestrictionPolicyRequestRequestTypeDef,
):
    pass

UpdatePlaybackRestrictionPolicyResponseTypeDef = TypedDict(
    "UpdatePlaybackRestrictionPolicyResponseTypeDef",
    {
        "playbackRestrictionPolicy": "PlaybackRestrictionPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VideoConfigurationTypeDef = TypedDict(
    "VideoConfigurationTypeDef",
    {
        "avcLevel": str,
        "avcProfile": str,
        "codec": str,
        "encoder": str,
        "targetBitrate": int,
        "targetFramerate": int,
        "videoHeight": int,
        "videoWidth": int,
    },
    total=False,
)
