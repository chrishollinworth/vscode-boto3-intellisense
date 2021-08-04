"""
Type annotations for medialive service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/literals.html)

Usage::

    ```python
    from mypy_boto3_medialive.literals import AacCodingModeType

    data: AacCodingModeType = "AD_RECEIVER_MIX"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AacCodingModeType",
    "AacInputTypeType",
    "AacProfileType",
    "AacRateControlModeType",
    "AacRawFormatType",
    "AacSpecType",
    "AacVbrQualityType",
    "Ac3BitstreamModeType",
    "Ac3CodingModeType",
    "Ac3DrcProfileType",
    "Ac3LfeFilterType",
    "Ac3MetadataControlType",
    "AcceptHeaderType",
    "AfdSignalingType",
    "AudioDescriptionAudioTypeControlType",
    "AudioDescriptionLanguageCodeControlType",
    "AudioLanguageSelectionPolicyType",
    "AudioNormalizationAlgorithmControlType",
    "AudioNormalizationAlgorithmType",
    "AudioOnlyHlsSegmentTypeType",
    "AudioOnlyHlsTrackTypeType",
    "AudioTypeType",
    "AuthenticationSchemeType",
    "AvailBlankingStateType",
    "BlackoutSlateNetworkEndBlackoutType",
    "BlackoutSlateStateType",
    "BurnInAlignmentType",
    "BurnInBackgroundColorType",
    "BurnInFontColorType",
    "BurnInOutlineColorType",
    "BurnInShadowColorType",
    "BurnInTeletextGridControlType",
    "CdiInputResolutionType",
    "ChannelClassType",
    "ChannelCreatedWaiterName",
    "ChannelDeletedWaiterName",
    "ChannelRunningWaiterName",
    "ChannelStateType",
    "ChannelStoppedWaiterName",
    "ContentTypeType",
    "DescribeSchedulePaginatorName",
    "DeviceSettingsSyncStateType",
    "DeviceUpdateStatusType",
    "DvbSdtOutputSdtType",
    "DvbSubDestinationAlignmentType",
    "DvbSubDestinationBackgroundColorType",
    "DvbSubDestinationFontColorType",
    "DvbSubDestinationOutlineColorType",
    "DvbSubDestinationShadowColorType",
    "DvbSubDestinationTeletextGridControlType",
    "DvbSubOcrLanguageType",
    "Eac3AttenuationControlType",
    "Eac3BitstreamModeType",
    "Eac3CodingModeType",
    "Eac3DcFilterType",
    "Eac3DrcLineType",
    "Eac3DrcRfType",
    "Eac3LfeControlType",
    "Eac3LfeFilterType",
    "Eac3MetadataControlType",
    "Eac3PassthroughControlType",
    "Eac3PhaseControlType",
    "Eac3StereoDownmixType",
    "Eac3SurroundExModeType",
    "Eac3SurroundModeType",
    "EbuTtDDestinationStyleControlType",
    "EbuTtDFillLineGapControlType",
    "EmbeddedConvert608To708Type",
    "EmbeddedScte20DetectionType",
    "FeatureActivationsInputPrepareScheduleActionsType",
    "FecOutputIncludeFecType",
    "FixedAfdType",
    "Fmp4NielsenId3BehaviorType",
    "Fmp4TimedMetadataBehaviorType",
    "FollowPointType",
    "FrameCaptureIntervalUnitType",
    "GlobalConfigurationInputEndActionType",
    "GlobalConfigurationLowFramerateInputsType",
    "GlobalConfigurationOutputLockingModeType",
    "GlobalConfigurationOutputTimingSourceType",
    "H264AdaptiveQuantizationType",
    "H264ColorMetadataType",
    "H264EntropyEncodingType",
    "H264FlickerAqType",
    "H264ForceFieldPicturesType",
    "H264FramerateControlType",
    "H264GopBReferenceType",
    "H264GopSizeUnitsType",
    "H264LevelType",
    "H264LookAheadRateControlType",
    "H264ParControlType",
    "H264ProfileType",
    "H264QualityLevelType",
    "H264RateControlModeType",
    "H264ScanTypeType",
    "H264SceneChangeDetectType",
    "H264SpatialAqType",
    "H264SubGopLengthType",
    "H264SyntaxType",
    "H264TemporalAqType",
    "H264TimecodeInsertionBehaviorType",
    "H265AdaptiveQuantizationType",
    "H265AlternativeTransferFunctionType",
    "H265ColorMetadataType",
    "H265FlickerAqType",
    "H265GopSizeUnitsType",
    "H265LevelType",
    "H265LookAheadRateControlType",
    "H265ProfileType",
    "H265RateControlModeType",
    "H265ScanTypeType",
    "H265SceneChangeDetectType",
    "H265TierType",
    "H265TimecodeInsertionBehaviorType",
    "HlsAdMarkersType",
    "HlsAkamaiHttpTransferModeType",
    "HlsCaptionLanguageSettingType",
    "HlsClientCacheType",
    "HlsCodecSpecificationType",
    "HlsDirectoryStructureType",
    "HlsDiscontinuityTagsType",
    "HlsEncryptionTypeType",
    "HlsH265PackagingTypeType",
    "HlsId3SegmentTaggingStateType",
    "HlsIncompleteSegmentBehaviorType",
    "HlsIvInManifestType",
    "HlsIvSourceType",
    "HlsManifestCompressionType",
    "HlsManifestDurationFormatType",
    "HlsMediaStoreStorageClassType",
    "HlsModeType",
    "HlsOutputSelectionType",
    "HlsProgramDateTimeType",
    "HlsRedundantManifestType",
    "HlsScte35SourceTypeType",
    "HlsSegmentationModeType",
    "HlsStreamInfResolutionType",
    "HlsTimedMetadataId3FrameType",
    "HlsTsFileModeType",
    "HlsWebdavHttpTransferModeType",
    "IFrameOnlyPlaylistTypeType",
    "InputAttachedWaiterName",
    "InputClassType",
    "InputCodecType",
    "InputDeblockFilterType",
    "InputDeletedWaiterName",
    "InputDenoiseFilterType",
    "InputDetachedWaiterName",
    "InputDeviceActiveInputType",
    "InputDeviceConfiguredInputType",
    "InputDeviceConnectionStateType",
    "InputDeviceIpSchemeType",
    "InputDeviceScanTypeType",
    "InputDeviceStateType",
    "InputDeviceTransferTypeType",
    "InputDeviceTypeType",
    "InputFilterType",
    "InputLossActionForHlsOutType",
    "InputLossActionForMsSmoothOutType",
    "InputLossActionForRtmpOutType",
    "InputLossActionForUdpOutType",
    "InputLossImageTypeType",
    "InputMaximumBitrateType",
    "InputPreferenceType",
    "InputResolutionType",
    "InputSecurityGroupStateType",
    "InputSourceEndBehaviorType",
    "InputSourceTypeType",
    "InputStateType",
    "InputTimecodeSourceType",
    "InputTypeType",
    "LastFrameClippingBehaviorType",
    "ListChannelsPaginatorName",
    "ListInputDeviceTransfersPaginatorName",
    "ListInputDevicesPaginatorName",
    "ListInputSecurityGroupsPaginatorName",
    "ListInputsPaginatorName",
    "ListMultiplexProgramsPaginatorName",
    "ListMultiplexesPaginatorName",
    "ListOfferingsPaginatorName",
    "ListReservationsPaginatorName",
    "LogLevelType",
    "M2tsAbsentInputAudioBehaviorType",
    "M2tsAribCaptionsPidControlType",
    "M2tsAribType",
    "M2tsAudioBufferModelType",
    "M2tsAudioIntervalType",
    "M2tsAudioStreamTypeType",
    "M2tsBufferModelType",
    "M2tsCcDescriptorType",
    "M2tsEbifControlType",
    "M2tsEbpPlacementType",
    "M2tsEsRateInPesType",
    "M2tsKlvType",
    "M2tsNielsenId3BehaviorType",
    "M2tsPcrControlType",
    "M2tsRateModeType",
    "M2tsScte35ControlType",
    "M2tsSegmentationMarkersType",
    "M2tsSegmentationStyleType",
    "M2tsTimedMetadataBehaviorType",
    "M3u8NielsenId3BehaviorType",
    "M3u8PcrControlType",
    "M3u8Scte35BehaviorType",
    "M3u8TimedMetadataBehaviorType",
    "MotionGraphicsInsertionType",
    "Mp2CodingModeType",
    "Mpeg2AdaptiveQuantizationType",
    "Mpeg2ColorMetadataType",
    "Mpeg2ColorSpaceType",
    "Mpeg2DisplayRatioType",
    "Mpeg2GopSizeUnitsType",
    "Mpeg2ScanTypeType",
    "Mpeg2SubGopLengthType",
    "Mpeg2TimecodeInsertionBehaviorType",
    "MsSmoothH265PackagingTypeType",
    "MultiplexCreatedWaiterName",
    "MultiplexDeletedWaiterName",
    "MultiplexRunningWaiterName",
    "MultiplexStateType",
    "MultiplexStoppedWaiterName",
    "NetworkInputServerValidationType",
    "NielsenPcmToId3TaggingStateType",
    "OfferingDurationUnitsType",
    "OfferingTypeType",
    "PipelineIdType",
    "PreferredChannelPipelineType",
    "ReservationCodecType",
    "ReservationMaximumBitrateType",
    "ReservationMaximumFramerateType",
    "ReservationResolutionType",
    "ReservationResourceTypeType",
    "ReservationSpecialFeatureType",
    "ReservationStateType",
    "ReservationVideoQualityType",
    "RtmpAdMarkersType",
    "RtmpCacheFullBehaviorType",
    "RtmpCaptionDataType",
    "RtmpOutputCertificateModeType",
    "S3CannedAclType",
    "Scte20Convert608To708Type",
    "Scte27OcrLanguageType",
    "Scte35AposNoRegionalBlackoutBehaviorType",
    "Scte35AposWebDeliveryAllowedBehaviorType",
    "Scte35ArchiveAllowedFlagType",
    "Scte35DeviceRestrictionsType",
    "Scte35NoRegionalBlackoutFlagType",
    "Scte35SegmentationCancelIndicatorType",
    "Scte35SpliceInsertNoRegionalBlackoutBehaviorType",
    "Scte35SpliceInsertWebDeliveryAllowedBehaviorType",
    "Scte35WebDeliveryAllowedFlagType",
    "SmoothGroupAudioOnlyTimecodeControlType",
    "SmoothGroupCertificateModeType",
    "SmoothGroupEventIdModeType",
    "SmoothGroupEventStopBehaviorType",
    "SmoothGroupSegmentationModeType",
    "SmoothGroupSparseTrackTypeType",
    "SmoothGroupStreamManifestBehaviorType",
    "SmoothGroupTimestampOffsetModeType",
    "Smpte2038DataPreferenceType",
    "TemporalFilterPostFilterSharpeningType",
    "TemporalFilterStrengthType",
    "TimecodeConfigSourceType",
    "TtmlDestinationStyleControlType",
    "UdpTimedMetadataId3FrameType",
    "VideoDescriptionRespondToAfdType",
    "VideoDescriptionScalingBehaviorType",
    "VideoSelectorColorSpaceType",
    "VideoSelectorColorSpaceUsageType",
    "WavCodingModeType",
    "WebvttDestinationStyleControlType",
)

AacCodingModeType = Literal[
    "AD_RECEIVER_MIX", "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_5_1"
]
AacInputTypeType = Literal["BROADCASTER_MIXED_AD", "NORMAL"]
AacProfileType = Literal["HEV1", "HEV2", "LC"]
AacRateControlModeType = Literal["CBR", "VBR"]
AacRawFormatType = Literal["LATM_LOAS", "NONE"]
AacSpecType = Literal["MPEG2", "MPEG4"]
AacVbrQualityType = Literal["HIGH", "LOW", "MEDIUM_HIGH", "MEDIUM_LOW"]
Ac3BitstreamModeType = Literal[
    "COMMENTARY",
    "COMPLETE_MAIN",
    "DIALOGUE",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "MUSIC_AND_EFFECTS",
    "VISUALLY_IMPAIRED",
    "VOICE_OVER",
]
Ac3CodingModeType = Literal[
    "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_3_2_LFE"
]
Ac3DrcProfileType = Literal["FILM_STANDARD", "NONE"]
Ac3LfeFilterType = Literal["DISABLED", "ENABLED"]
Ac3MetadataControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AcceptHeaderType = Literal["image/jpeg"]
AfdSignalingType = Literal["AUTO", "FIXED", "NONE"]
AudioDescriptionAudioTypeControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioDescriptionLanguageCodeControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioLanguageSelectionPolicyType = Literal["LOOSE", "STRICT"]
AudioNormalizationAlgorithmControlType = Literal["CORRECT_AUDIO"]
AudioNormalizationAlgorithmType = Literal["ITU_1770_1", "ITU_1770_2"]
AudioOnlyHlsSegmentTypeType = Literal["AAC", "FMP4"]
AudioOnlyHlsTrackTypeType = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",
]
AudioTypeType = Literal[
    "CLEAN_EFFECTS", "HEARING_IMPAIRED", "UNDEFINED", "VISUAL_IMPAIRED_COMMENTARY"
]
AuthenticationSchemeType = Literal["AKAMAI", "COMMON"]
AvailBlankingStateType = Literal["DISABLED", "ENABLED"]
BlackoutSlateNetworkEndBlackoutType = Literal["DISABLED", "ENABLED"]
BlackoutSlateStateType = Literal["DISABLED", "ENABLED"]
BurnInAlignmentType = Literal["CENTERED", "LEFT", "SMART"]
BurnInBackgroundColorType = Literal["BLACK", "NONE", "WHITE"]
BurnInFontColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurnInOutlineColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurnInShadowColorType = Literal["BLACK", "NONE", "WHITE"]
BurnInTeletextGridControlType = Literal["FIXED", "SCALED"]
CdiInputResolutionType = Literal["FHD", "HD", "SD", "UHD"]
ChannelClassType = Literal["SINGLE_PIPELINE", "STANDARD"]
ChannelCreatedWaiterName = Literal["channel_created"]
ChannelDeletedWaiterName = Literal["channel_deleted"]
ChannelRunningWaiterName = Literal["channel_running"]
ChannelStateType = Literal[
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "IDLE",
    "RECOVERING",
    "RUNNING",
    "STARTING",
    "STOPPING",
    "UPDATE_FAILED",
    "UPDATING",
]
ChannelStoppedWaiterName = Literal["channel_stopped"]
ContentTypeType = Literal["image/jpeg"]
DescribeSchedulePaginatorName = Literal["describe_schedule"]
DeviceSettingsSyncStateType = Literal["SYNCED", "SYNCING"]
DeviceUpdateStatusType = Literal["NOT_UP_TO_DATE", "UP_TO_DATE"]
DvbSdtOutputSdtType = Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"]
DvbSubDestinationAlignmentType = Literal["CENTERED", "LEFT", "SMART"]
DvbSubDestinationBackgroundColorType = Literal["BLACK", "NONE", "WHITE"]
DvbSubDestinationFontColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubDestinationOutlineColorType = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubDestinationShadowColorType = Literal["BLACK", "NONE", "WHITE"]
DvbSubDestinationTeletextGridControlType = Literal["FIXED", "SCALED"]
DvbSubOcrLanguageType = Literal["DEU", "ENG", "FRA", "NLD", "POR", "SPA"]
Eac3AttenuationControlType = Literal["ATTENUATE_3_DB", "NONE"]
Eac3BitstreamModeType = Literal[
    "COMMENTARY", "COMPLETE_MAIN", "EMERGENCY", "HEARING_IMPAIRED", "VISUALLY_IMPAIRED"
]
Eac3CodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"]
Eac3DcFilterType = Literal["DISABLED", "ENABLED"]
Eac3DrcLineType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3DrcRfType = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3LfeControlType = Literal["LFE", "NO_LFE"]
Eac3LfeFilterType = Literal["DISABLED", "ENABLED"]
Eac3MetadataControlType = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
Eac3PassthroughControlType = Literal["NO_PASSTHROUGH", "WHEN_POSSIBLE"]
Eac3PhaseControlType = Literal["NO_SHIFT", "SHIFT_90_DEGREES"]
Eac3StereoDownmixType = Literal["DPL2", "LO_RO", "LT_RT", "NOT_INDICATED"]
Eac3SurroundExModeType = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
Eac3SurroundModeType = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
EbuTtDDestinationStyleControlType = Literal["EXCLUDE", "INCLUDE"]
EbuTtDFillLineGapControlType = Literal["DISABLED", "ENABLED"]
EmbeddedConvert608To708Type = Literal["DISABLED", "UPCONVERT"]
EmbeddedScte20DetectionType = Literal["AUTO", "OFF"]
FeatureActivationsInputPrepareScheduleActionsType = Literal["DISABLED", "ENABLED"]
FecOutputIncludeFecType = Literal["COLUMN", "COLUMN_AND_ROW"]
FixedAfdType = Literal[
    "AFD_0000",
    "AFD_0010",
    "AFD_0011",
    "AFD_0100",
    "AFD_1000",
    "AFD_1001",
    "AFD_1010",
    "AFD_1011",
    "AFD_1101",
    "AFD_1110",
    "AFD_1111",
]
Fmp4NielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
Fmp4TimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
FollowPointType = Literal["END", "START"]
FrameCaptureIntervalUnitType = Literal["MILLISECONDS", "SECONDS"]
GlobalConfigurationInputEndActionType = Literal["NONE", "SWITCH_AND_LOOP_INPUTS"]
GlobalConfigurationLowFramerateInputsType = Literal["DISABLED", "ENABLED"]
GlobalConfigurationOutputLockingModeType = Literal["EPOCH_LOCKING", "PIPELINE_LOCKING"]
GlobalConfigurationOutputTimingSourceType = Literal["INPUT_CLOCK", "SYSTEM_CLOCK"]
H264AdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H264ColorMetadataType = Literal["IGNORE", "INSERT"]
H264EntropyEncodingType = Literal["CABAC", "CAVLC"]
H264FlickerAqType = Literal["DISABLED", "ENABLED"]
H264ForceFieldPicturesType = Literal["DISABLED", "ENABLED"]
H264FramerateControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264GopBReferenceType = Literal["DISABLED", "ENABLED"]
H264GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
H264LevelType = Literal[
    "H264_LEVEL_1",
    "H264_LEVEL_1_1",
    "H264_LEVEL_1_2",
    "H264_LEVEL_1_3",
    "H264_LEVEL_2",
    "H264_LEVEL_2_1",
    "H264_LEVEL_2_2",
    "H264_LEVEL_3",
    "H264_LEVEL_3_1",
    "H264_LEVEL_3_2",
    "H264_LEVEL_4",
    "H264_LEVEL_4_1",
    "H264_LEVEL_4_2",
    "H264_LEVEL_5",
    "H264_LEVEL_5_1",
    "H264_LEVEL_5_2",
    "H264_LEVEL_AUTO",
]
H264LookAheadRateControlType = Literal["HIGH", "LOW", "MEDIUM"]
H264ParControlType = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264ProfileType = Literal["BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"]
H264QualityLevelType = Literal["ENHANCED_QUALITY", "STANDARD_QUALITY"]
H264RateControlModeType = Literal["CBR", "MULTIPLEX", "QVBR", "VBR"]
H264ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
H264SceneChangeDetectType = Literal["DISABLED", "ENABLED"]
H264SpatialAqType = Literal["DISABLED", "ENABLED"]
H264SubGopLengthType = Literal["DYNAMIC", "FIXED"]
H264SyntaxType = Literal["DEFAULT", "RP2027"]
H264TemporalAqType = Literal["DISABLED", "ENABLED"]
H264TimecodeInsertionBehaviorType = Literal["DISABLED", "PIC_TIMING_SEI"]
H265AdaptiveQuantizationType = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H265AlternativeTransferFunctionType = Literal["INSERT", "OMIT"]
H265ColorMetadataType = Literal["IGNORE", "INSERT"]
H265FlickerAqType = Literal["DISABLED", "ENABLED"]
H265GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
H265LevelType = Literal[
    "H265_LEVEL_1",
    "H265_LEVEL_2",
    "H265_LEVEL_2_1",
    "H265_LEVEL_3",
    "H265_LEVEL_3_1",
    "H265_LEVEL_4",
    "H265_LEVEL_4_1",
    "H265_LEVEL_5",
    "H265_LEVEL_5_1",
    "H265_LEVEL_5_2",
    "H265_LEVEL_6",
    "H265_LEVEL_6_1",
    "H265_LEVEL_6_2",
    "H265_LEVEL_AUTO",
]
H265LookAheadRateControlType = Literal["HIGH", "LOW", "MEDIUM"]
H265ProfileType = Literal["MAIN", "MAIN_10BIT"]
H265RateControlModeType = Literal["CBR", "MULTIPLEX", "QVBR"]
H265ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
H265SceneChangeDetectType = Literal["DISABLED", "ENABLED"]
H265TierType = Literal["HIGH", "MAIN"]
H265TimecodeInsertionBehaviorType = Literal["DISABLED", "PIC_TIMING_SEI"]
HlsAdMarkersType = Literal["ADOBE", "ELEMENTAL", "ELEMENTAL_SCTE35"]
HlsAkamaiHttpTransferModeType = Literal["CHUNKED", "NON_CHUNKED"]
HlsCaptionLanguageSettingType = Literal["INSERT", "NONE", "OMIT"]
HlsClientCacheType = Literal["DISABLED", "ENABLED"]
HlsCodecSpecificationType = Literal["RFC_4281", "RFC_6381"]
HlsDirectoryStructureType = Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"]
HlsDiscontinuityTagsType = Literal["INSERT", "NEVER_INSERT"]
HlsEncryptionTypeType = Literal["AES128", "SAMPLE_AES"]
HlsH265PackagingTypeType = Literal["HEV1", "HVC1"]
HlsId3SegmentTaggingStateType = Literal["DISABLED", "ENABLED"]
HlsIncompleteSegmentBehaviorType = Literal["AUTO", "SUPPRESS"]
HlsIvInManifestType = Literal["EXCLUDE", "INCLUDE"]
HlsIvSourceType = Literal["EXPLICIT", "FOLLOWS_SEGMENT_NUMBER"]
HlsManifestCompressionType = Literal["GZIP", "NONE"]
HlsManifestDurationFormatType = Literal["FLOATING_POINT", "INTEGER"]
HlsMediaStoreStorageClassType = Literal["TEMPORAL"]
HlsModeType = Literal["LIVE", "VOD"]
HlsOutputSelectionType = Literal[
    "MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY", "VARIANT_MANIFESTS_AND_SEGMENTS"
]
HlsProgramDateTimeType = Literal["EXCLUDE", "INCLUDE"]
HlsRedundantManifestType = Literal["DISABLED", "ENABLED"]
HlsScte35SourceTypeType = Literal["MANIFEST", "SEGMENTS"]
HlsSegmentationModeType = Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
HlsStreamInfResolutionType = Literal["EXCLUDE", "INCLUDE"]
HlsTimedMetadataId3FrameType = Literal["NONE", "PRIV", "TDRL"]
HlsTsFileModeType = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
HlsWebdavHttpTransferModeType = Literal["CHUNKED", "NON_CHUNKED"]
IFrameOnlyPlaylistTypeType = Literal["DISABLED", "STANDARD"]
InputAttachedWaiterName = Literal["input_attached"]
InputClassType = Literal["SINGLE_PIPELINE", "STANDARD"]
InputCodecType = Literal["AVC", "HEVC", "MPEG2"]
InputDeblockFilterType = Literal["DISABLED", "ENABLED"]
InputDeletedWaiterName = Literal["input_deleted"]
InputDenoiseFilterType = Literal["DISABLED", "ENABLED"]
InputDetachedWaiterName = Literal["input_detached"]
InputDeviceActiveInputType = Literal["HDMI", "SDI"]
InputDeviceConfiguredInputType = Literal["AUTO", "HDMI", "SDI"]
InputDeviceConnectionStateType = Literal["CONNECTED", "DISCONNECTED"]
InputDeviceIpSchemeType = Literal["DHCP", "STATIC"]
InputDeviceScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
InputDeviceStateType = Literal["IDLE", "STREAMING"]
InputDeviceTransferTypeType = Literal["INCOMING", "OUTGOING"]
InputDeviceTypeType = Literal["HD"]
InputFilterType = Literal["AUTO", "DISABLED", "FORCED"]
InputLossActionForHlsOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForMsSmoothOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForRtmpOutType = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForUdpOutType = Literal["DROP_PROGRAM", "DROP_TS", "EMIT_PROGRAM"]
InputLossImageTypeType = Literal["COLOR", "SLATE"]
InputMaximumBitrateType = Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
InputPreferenceType = Literal["EQUAL_INPUT_PREFERENCE", "PRIMARY_INPUT_PREFERRED"]
InputResolutionType = Literal["HD", "SD", "UHD"]
InputSecurityGroupStateType = Literal["DELETED", "IDLE", "IN_USE", "UPDATING"]
InputSourceEndBehaviorType = Literal["CONTINUE", "LOOP"]
InputSourceTypeType = Literal["DYNAMIC", "STATIC"]
InputStateType = Literal["ATTACHED", "CREATING", "DELETED", "DELETING", "DETACHED"]
InputTimecodeSourceType = Literal["EMBEDDED", "ZEROBASED"]
InputTypeType = Literal[
    "AWS_CDI",
    "INPUT_DEVICE",
    "MEDIACONNECT",
    "MP4_FILE",
    "RTMP_PULL",
    "RTMP_PUSH",
    "RTP_PUSH",
    "UDP_PUSH",
    "URL_PULL",
]
LastFrameClippingBehaviorType = Literal["EXCLUDE_LAST_FRAME", "INCLUDE_LAST_FRAME"]
ListChannelsPaginatorName = Literal["list_channels"]
ListInputDeviceTransfersPaginatorName = Literal["list_input_device_transfers"]
ListInputDevicesPaginatorName = Literal["list_input_devices"]
ListInputSecurityGroupsPaginatorName = Literal["list_input_security_groups"]
ListInputsPaginatorName = Literal["list_inputs"]
ListMultiplexProgramsPaginatorName = Literal["list_multiplex_programs"]
ListMultiplexesPaginatorName = Literal["list_multiplexes"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListReservationsPaginatorName = Literal["list_reservations"]
LogLevelType = Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"]
M2tsAbsentInputAudioBehaviorType = Literal["DROP", "ENCODE_SILENCE"]
M2tsAribCaptionsPidControlType = Literal["AUTO", "USE_CONFIGURED"]
M2tsAribType = Literal["DISABLED", "ENABLED"]
M2tsAudioBufferModelType = Literal["ATSC", "DVB"]
M2tsAudioIntervalType = Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"]
M2tsAudioStreamTypeType = Literal["ATSC", "DVB"]
M2tsBufferModelType = Literal["MULTIPLEX", "NONE"]
M2tsCcDescriptorType = Literal["DISABLED", "ENABLED"]
M2tsEbifControlType = Literal["NONE", "PASSTHROUGH"]
M2tsEbpPlacementType = Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"]
M2tsEsRateInPesType = Literal["EXCLUDE", "INCLUDE"]
M2tsKlvType = Literal["NONE", "PASSTHROUGH"]
M2tsNielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M2tsPcrControlType = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M2tsRateModeType = Literal["CBR", "VBR"]
M2tsScte35ControlType = Literal["NONE", "PASSTHROUGH"]
M2tsSegmentationMarkersType = Literal[
    "EBP", "EBP_LEGACY", "NONE", "PSI_SEGSTART", "RAI_ADAPT", "RAI_SEGSTART"
]
M2tsSegmentationStyleType = Literal["MAINTAIN_CADENCE", "RESET_CADENCE"]
M2tsTimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8NielsenId3BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8PcrControlType = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M3u8Scte35BehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8TimedMetadataBehaviorType = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
MotionGraphicsInsertionType = Literal["DISABLED", "ENABLED"]
Mp2CodingModeType = Literal["CODING_MODE_1_0", "CODING_MODE_2_0"]
Mpeg2AdaptiveQuantizationType = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "OFF"]
Mpeg2ColorMetadataType = Literal["IGNORE", "INSERT"]
Mpeg2ColorSpaceType = Literal["AUTO", "PASSTHROUGH"]
Mpeg2DisplayRatioType = Literal["DISPLAYRATIO16X9", "DISPLAYRATIO4X3"]
Mpeg2GopSizeUnitsType = Literal["FRAMES", "SECONDS"]
Mpeg2ScanTypeType = Literal["INTERLACED", "PROGRESSIVE"]
Mpeg2SubGopLengthType = Literal["DYNAMIC", "FIXED"]
Mpeg2TimecodeInsertionBehaviorType = Literal["DISABLED", "GOP_TIMECODE"]
MsSmoothH265PackagingTypeType = Literal["HEV1", "HVC1"]
MultiplexCreatedWaiterName = Literal["multiplex_created"]
MultiplexDeletedWaiterName = Literal["multiplex_deleted"]
MultiplexRunningWaiterName = Literal["multiplex_running"]
MultiplexStateType = Literal[
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "IDLE",
    "RECOVERING",
    "RUNNING",
    "STARTING",
    "STOPPING",
]
MultiplexStoppedWaiterName = Literal["multiplex_stopped"]
NetworkInputServerValidationType = Literal[
    "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME", "CHECK_CRYPTOGRAPHY_ONLY"
]
NielsenPcmToId3TaggingStateType = Literal["DISABLED", "ENABLED"]
OfferingDurationUnitsType = Literal["MONTHS"]
OfferingTypeType = Literal["NO_UPFRONT"]
PipelineIdType = Literal["PIPELINE_0", "PIPELINE_1"]
PreferredChannelPipelineType = Literal["CURRENTLY_ACTIVE", "PIPELINE_0", "PIPELINE_1"]
ReservationCodecType = Literal["AUDIO", "AVC", "HEVC", "LINK", "MPEG2"]
ReservationMaximumBitrateType = Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
ReservationMaximumFramerateType = Literal["MAX_30_FPS", "MAX_60_FPS"]
ReservationResolutionType = Literal["FHD", "HD", "SD", "UHD"]
ReservationResourceTypeType = Literal["CHANNEL", "INPUT", "MULTIPLEX", "OUTPUT"]
ReservationSpecialFeatureType = Literal["ADVANCED_AUDIO", "AUDIO_NORMALIZATION", "MGHD", "MGUHD"]
ReservationStateType = Literal["ACTIVE", "CANCELED", "DELETED", "EXPIRED"]
ReservationVideoQualityType = Literal["ENHANCED", "PREMIUM", "STANDARD"]
RtmpAdMarkersType = Literal["ON_CUE_POINT_SCTE35"]
RtmpCacheFullBehaviorType = Literal["DISCONNECT_IMMEDIATELY", "WAIT_FOR_SERVER"]
RtmpCaptionDataType = Literal["ALL", "FIELD1_608", "FIELD1_AND_FIELD2_608"]
RtmpOutputCertificateModeType = Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]
S3CannedAclType = Literal[
    "AUTHENTICATED_READ", "BUCKET_OWNER_FULL_CONTROL", "BUCKET_OWNER_READ", "PUBLIC_READ"
]
Scte20Convert608To708Type = Literal["DISABLED", "UPCONVERT"]
Scte27OcrLanguageType = Literal["DEU", "ENG", "FRA", "NLD", "POR", "SPA"]
Scte35AposNoRegionalBlackoutBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35AposWebDeliveryAllowedBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35ArchiveAllowedFlagType = Literal["ARCHIVE_ALLOWED", "ARCHIVE_NOT_ALLOWED"]
Scte35DeviceRestrictionsType = Literal[
    "NONE", "RESTRICT_GROUP0", "RESTRICT_GROUP1", "RESTRICT_GROUP2"
]
Scte35NoRegionalBlackoutFlagType = Literal["NO_REGIONAL_BLACKOUT", "REGIONAL_BLACKOUT"]
Scte35SegmentationCancelIndicatorType = Literal[
    "SEGMENTATION_EVENT_CANCELED", "SEGMENTATION_EVENT_NOT_CANCELED"
]
Scte35SpliceInsertNoRegionalBlackoutBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35SpliceInsertWebDeliveryAllowedBehaviorType = Literal["FOLLOW", "IGNORE"]
Scte35WebDeliveryAllowedFlagType = Literal["WEB_DELIVERY_ALLOWED", "WEB_DELIVERY_NOT_ALLOWED"]
SmoothGroupAudioOnlyTimecodeControlType = Literal["PASSTHROUGH", "USE_CONFIGURED_CLOCK"]
SmoothGroupCertificateModeType = Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]
SmoothGroupEventIdModeType = Literal["NO_EVENT_ID", "USE_CONFIGURED", "USE_TIMESTAMP"]
SmoothGroupEventStopBehaviorType = Literal["NONE", "SEND_EOS"]
SmoothGroupSegmentationModeType = Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
SmoothGroupSparseTrackTypeType = Literal["NONE", "SCTE_35", "SCTE_35_WITHOUT_SEGMENTATION"]
SmoothGroupStreamManifestBehaviorType = Literal["DO_NOT_SEND", "SEND"]
SmoothGroupTimestampOffsetModeType = Literal["USE_CONFIGURED_OFFSET", "USE_EVENT_START_DATE"]
Smpte2038DataPreferenceType = Literal["IGNORE", "PREFER"]
TemporalFilterPostFilterSharpeningType = Literal["AUTO", "DISABLED", "ENABLED"]
TemporalFilterStrengthType = Literal[
    "AUTO",
    "STRENGTH_1",
    "STRENGTH_10",
    "STRENGTH_11",
    "STRENGTH_12",
    "STRENGTH_13",
    "STRENGTH_14",
    "STRENGTH_15",
    "STRENGTH_16",
    "STRENGTH_2",
    "STRENGTH_3",
    "STRENGTH_4",
    "STRENGTH_5",
    "STRENGTH_6",
    "STRENGTH_7",
    "STRENGTH_8",
    "STRENGTH_9",
]
TimecodeConfigSourceType = Literal["EMBEDDED", "SYSTEMCLOCK", "ZEROBASED"]
TtmlDestinationStyleControlType = Literal["PASSTHROUGH", "USE_CONFIGURED"]
UdpTimedMetadataId3FrameType = Literal["NONE", "PRIV", "TDRL"]
VideoDescriptionRespondToAfdType = Literal["NONE", "PASSTHROUGH", "RESPOND"]
VideoDescriptionScalingBehaviorType = Literal["DEFAULT", "STRETCH_TO_OUTPUT"]
VideoSelectorColorSpaceType = Literal["FOLLOW", "HDR10", "HLG_2020", "REC_601", "REC_709"]
VideoSelectorColorSpaceUsageType = Literal["FALLBACK", "FORCE"]
WavCodingModeType = Literal[
    "CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_4_0", "CODING_MODE_8_0"
]
WebvttDestinationStyleControlType = Literal["NO_STYLE_DATA", "PASSTHROUGH"]
