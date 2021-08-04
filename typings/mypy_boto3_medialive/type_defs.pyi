"""
Type annotations for medialive service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/type_defs.html)

Usage::

    ```python
    from mypy_boto3_medialive.type_defs import AacSettingsTypeDef

    data: AacSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from .literals import (
    AacCodingModeType,
    AacInputTypeType,
    AacProfileType,
    AacRateControlModeType,
    AacRawFormatType,
    AacSpecType,
    AacVbrQualityType,
    Ac3BitstreamModeType,
    Ac3CodingModeType,
    Ac3DrcProfileType,
    Ac3LfeFilterType,
    Ac3MetadataControlType,
    AfdSignalingType,
    AudioDescriptionAudioTypeControlType,
    AudioDescriptionLanguageCodeControlType,
    AudioLanguageSelectionPolicyType,
    AudioNormalizationAlgorithmType,
    AudioOnlyHlsSegmentTypeType,
    AudioOnlyHlsTrackTypeType,
    AudioTypeType,
    AuthenticationSchemeType,
    AvailBlankingStateType,
    BlackoutSlateNetworkEndBlackoutType,
    BlackoutSlateStateType,
    BurnInAlignmentType,
    BurnInBackgroundColorType,
    BurnInFontColorType,
    BurnInOutlineColorType,
    BurnInShadowColorType,
    BurnInTeletextGridControlType,
    CdiInputResolutionType,
    ChannelClassType,
    ChannelStateType,
    DeviceSettingsSyncStateType,
    DeviceUpdateStatusType,
    DvbSdtOutputSdtType,
    DvbSubDestinationAlignmentType,
    DvbSubDestinationBackgroundColorType,
    DvbSubDestinationFontColorType,
    DvbSubDestinationOutlineColorType,
    DvbSubDestinationShadowColorType,
    DvbSubDestinationTeletextGridControlType,
    DvbSubOcrLanguageType,
    Eac3AttenuationControlType,
    Eac3BitstreamModeType,
    Eac3CodingModeType,
    Eac3DcFilterType,
    Eac3DrcLineType,
    Eac3DrcRfType,
    Eac3LfeControlType,
    Eac3LfeFilterType,
    Eac3MetadataControlType,
    Eac3PassthroughControlType,
    Eac3PhaseControlType,
    Eac3StereoDownmixType,
    Eac3SurroundExModeType,
    Eac3SurroundModeType,
    EbuTtDDestinationStyleControlType,
    EbuTtDFillLineGapControlType,
    EmbeddedConvert608To708Type,
    EmbeddedScte20DetectionType,
    FeatureActivationsInputPrepareScheduleActionsType,
    FecOutputIncludeFecType,
    FixedAfdType,
    Fmp4NielsenId3BehaviorType,
    Fmp4TimedMetadataBehaviorType,
    FollowPointType,
    FrameCaptureIntervalUnitType,
    GlobalConfigurationInputEndActionType,
    GlobalConfigurationLowFramerateInputsType,
    GlobalConfigurationOutputLockingModeType,
    GlobalConfigurationOutputTimingSourceType,
    H264AdaptiveQuantizationType,
    H264ColorMetadataType,
    H264EntropyEncodingType,
    H264FlickerAqType,
    H264ForceFieldPicturesType,
    H264FramerateControlType,
    H264GopBReferenceType,
    H264GopSizeUnitsType,
    H264LevelType,
    H264LookAheadRateControlType,
    H264ParControlType,
    H264ProfileType,
    H264QualityLevelType,
    H264RateControlModeType,
    H264ScanTypeType,
    H264SceneChangeDetectType,
    H264SpatialAqType,
    H264SubGopLengthType,
    H264SyntaxType,
    H264TemporalAqType,
    H264TimecodeInsertionBehaviorType,
    H265AdaptiveQuantizationType,
    H265AlternativeTransferFunctionType,
    H265ColorMetadataType,
    H265FlickerAqType,
    H265GopSizeUnitsType,
    H265LevelType,
    H265LookAheadRateControlType,
    H265ProfileType,
    H265RateControlModeType,
    H265ScanTypeType,
    H265SceneChangeDetectType,
    H265TierType,
    H265TimecodeInsertionBehaviorType,
    HlsAdMarkersType,
    HlsAkamaiHttpTransferModeType,
    HlsCaptionLanguageSettingType,
    HlsClientCacheType,
    HlsCodecSpecificationType,
    HlsDirectoryStructureType,
    HlsDiscontinuityTagsType,
    HlsEncryptionTypeType,
    HlsH265PackagingTypeType,
    HlsId3SegmentTaggingStateType,
    HlsIncompleteSegmentBehaviorType,
    HlsIvInManifestType,
    HlsIvSourceType,
    HlsManifestCompressionType,
    HlsManifestDurationFormatType,
    HlsModeType,
    HlsOutputSelectionType,
    HlsProgramDateTimeType,
    HlsRedundantManifestType,
    HlsScte35SourceTypeType,
    HlsSegmentationModeType,
    HlsStreamInfResolutionType,
    HlsTimedMetadataId3FrameType,
    HlsTsFileModeType,
    HlsWebdavHttpTransferModeType,
    IFrameOnlyPlaylistTypeType,
    InputClassType,
    InputCodecType,
    InputDeblockFilterType,
    InputDenoiseFilterType,
    InputDeviceActiveInputType,
    InputDeviceConfiguredInputType,
    InputDeviceConnectionStateType,
    InputDeviceIpSchemeType,
    InputDeviceScanTypeType,
    InputDeviceStateType,
    InputDeviceTransferTypeType,
    InputFilterType,
    InputLossActionForHlsOutType,
    InputLossActionForMsSmoothOutType,
    InputLossActionForRtmpOutType,
    InputLossActionForUdpOutType,
    InputLossImageTypeType,
    InputMaximumBitrateType,
    InputPreferenceType,
    InputResolutionType,
    InputSecurityGroupStateType,
    InputSourceEndBehaviorType,
    InputSourceTypeType,
    InputStateType,
    InputTimecodeSourceType,
    InputTypeType,
    LastFrameClippingBehaviorType,
    LogLevelType,
    M2tsAbsentInputAudioBehaviorType,
    M2tsAribCaptionsPidControlType,
    M2tsAribType,
    M2tsAudioBufferModelType,
    M2tsAudioIntervalType,
    M2tsAudioStreamTypeType,
    M2tsBufferModelType,
    M2tsCcDescriptorType,
    M2tsEbifControlType,
    M2tsEbpPlacementType,
    M2tsEsRateInPesType,
    M2tsKlvType,
    M2tsNielsenId3BehaviorType,
    M2tsPcrControlType,
    M2tsRateModeType,
    M2tsScte35ControlType,
    M2tsSegmentationMarkersType,
    M2tsSegmentationStyleType,
    M2tsTimedMetadataBehaviorType,
    M3u8NielsenId3BehaviorType,
    M3u8PcrControlType,
    M3u8Scte35BehaviorType,
    M3u8TimedMetadataBehaviorType,
    MotionGraphicsInsertionType,
    Mp2CodingModeType,
    Mpeg2AdaptiveQuantizationType,
    Mpeg2ColorMetadataType,
    Mpeg2ColorSpaceType,
    Mpeg2DisplayRatioType,
    Mpeg2GopSizeUnitsType,
    Mpeg2ScanTypeType,
    Mpeg2SubGopLengthType,
    Mpeg2TimecodeInsertionBehaviorType,
    MsSmoothH265PackagingTypeType,
    MultiplexStateType,
    NetworkInputServerValidationType,
    NielsenPcmToId3TaggingStateType,
    PipelineIdType,
    PreferredChannelPipelineType,
    ReservationCodecType,
    ReservationMaximumBitrateType,
    ReservationMaximumFramerateType,
    ReservationResolutionType,
    ReservationResourceTypeType,
    ReservationSpecialFeatureType,
    ReservationStateType,
    ReservationVideoQualityType,
    RtmpCacheFullBehaviorType,
    RtmpCaptionDataType,
    RtmpOutputCertificateModeType,
    S3CannedAclType,
    Scte20Convert608To708Type,
    Scte27OcrLanguageType,
    Scte35AposNoRegionalBlackoutBehaviorType,
    Scte35AposWebDeliveryAllowedBehaviorType,
    Scte35ArchiveAllowedFlagType,
    Scte35DeviceRestrictionsType,
    Scte35NoRegionalBlackoutFlagType,
    Scte35SegmentationCancelIndicatorType,
    Scte35SpliceInsertNoRegionalBlackoutBehaviorType,
    Scte35SpliceInsertWebDeliveryAllowedBehaviorType,
    Scte35WebDeliveryAllowedFlagType,
    SmoothGroupAudioOnlyTimecodeControlType,
    SmoothGroupCertificateModeType,
    SmoothGroupEventIdModeType,
    SmoothGroupEventStopBehaviorType,
    SmoothGroupSegmentationModeType,
    SmoothGroupSparseTrackTypeType,
    SmoothGroupStreamManifestBehaviorType,
    SmoothGroupTimestampOffsetModeType,
    Smpte2038DataPreferenceType,
    TemporalFilterPostFilterSharpeningType,
    TemporalFilterStrengthType,
    TimecodeConfigSourceType,
    TtmlDestinationStyleControlType,
    UdpTimedMetadataId3FrameType,
    VideoDescriptionRespondToAfdType,
    VideoDescriptionScalingBehaviorType,
    VideoSelectorColorSpaceType,
    VideoSelectorColorSpaceUsageType,
    WavCodingModeType,
    WebvttDestinationStyleControlType,
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
    "AacSettingsTypeDef",
    "Ac3SettingsTypeDef",
    "AcceptInputDeviceTransferRequestRequestTypeDef",
    "AncillarySourceSettingsTypeDef",
    "ArchiveCdnSettingsTypeDef",
    "ArchiveContainerSettingsTypeDef",
    "ArchiveGroupSettingsTypeDef",
    "ArchiveOutputSettingsTypeDef",
    "ArchiveS3SettingsTypeDef",
    "AudioChannelMappingTypeDef",
    "AudioCodecSettingsTypeDef",
    "AudioDescriptionTypeDef",
    "AudioHlsRenditionSelectionTypeDef",
    "AudioLanguageSelectionTypeDef",
    "AudioNormalizationSettingsTypeDef",
    "AudioOnlyHlsSettingsTypeDef",
    "AudioPidSelectionTypeDef",
    "AudioSelectorSettingsTypeDef",
    "AudioSelectorTypeDef",
    "AudioSilenceFailoverSettingsTypeDef",
    "AudioTrackSelectionTypeDef",
    "AudioTrackTypeDef",
    "AutomaticInputFailoverSettingsTypeDef",
    "AvailBlankingTypeDef",
    "AvailConfigurationTypeDef",
    "AvailSettingsTypeDef",
    "BatchDeleteRequestRequestTypeDef",
    "BatchDeleteResponseTypeDef",
    "BatchFailedResultModelTypeDef",
    "BatchScheduleActionCreateRequestTypeDef",
    "BatchScheduleActionCreateResultTypeDef",
    "BatchScheduleActionDeleteRequestTypeDef",
    "BatchScheduleActionDeleteResultTypeDef",
    "BatchStartRequestRequestTypeDef",
    "BatchStartResponseTypeDef",
    "BatchStopRequestRequestTypeDef",
    "BatchStopResponseTypeDef",
    "BatchSuccessfulResultModelTypeDef",
    "BatchUpdateScheduleRequestRequestTypeDef",
    "BatchUpdateScheduleResponseTypeDef",
    "BlackoutSlateTypeDef",
    "BurnInDestinationSettingsTypeDef",
    "CancelInputDeviceTransferRequestRequestTypeDef",
    "CaptionDescriptionTypeDef",
    "CaptionDestinationSettingsTypeDef",
    "CaptionLanguageMappingTypeDef",
    "CaptionRectangleTypeDef",
    "CaptionSelectorSettingsTypeDef",
    "CaptionSelectorTypeDef",
    "CdiInputSpecificationTypeDef",
    "ChannelEgressEndpointTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateInputRequestRequestTypeDef",
    "CreateInputResponseTypeDef",
    "CreateInputSecurityGroupRequestRequestTypeDef",
    "CreateInputSecurityGroupResponseTypeDef",
    "CreateMultiplexProgramRequestRequestTypeDef",
    "CreateMultiplexProgramResponseTypeDef",
    "CreateMultiplexRequestRequestTypeDef",
    "CreateMultiplexResponseTypeDef",
    "CreatePartnerInputRequestRequestTypeDef",
    "CreatePartnerInputResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteChannelResponseTypeDef",
    "DeleteInputRequestRequestTypeDef",
    "DeleteInputSecurityGroupRequestRequestTypeDef",
    "DeleteMultiplexProgramRequestRequestTypeDef",
    "DeleteMultiplexProgramResponseTypeDef",
    "DeleteMultiplexRequestRequestTypeDef",
    "DeleteMultiplexResponseTypeDef",
    "DeleteReservationRequestRequestTypeDef",
    "DeleteReservationResponseTypeDef",
    "DeleteScheduleRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeInputDeviceRequestRequestTypeDef",
    "DescribeInputDeviceResponseTypeDef",
    "DescribeInputDeviceThumbnailRequestRequestTypeDef",
    "DescribeInputDeviceThumbnailResponseTypeDef",
    "DescribeInputRequestRequestTypeDef",
    "DescribeInputResponseTypeDef",
    "DescribeInputSecurityGroupRequestRequestTypeDef",
    "DescribeInputSecurityGroupResponseTypeDef",
    "DescribeMultiplexProgramRequestRequestTypeDef",
    "DescribeMultiplexProgramResponseTypeDef",
    "DescribeMultiplexRequestRequestTypeDef",
    "DescribeMultiplexResponseTypeDef",
    "DescribeOfferingRequestRequestTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationRequestRequestTypeDef",
    "DescribeReservationResponseTypeDef",
    "DescribeScheduleRequestRequestTypeDef",
    "DescribeScheduleResponseTypeDef",
    "DvbNitSettingsTypeDef",
    "DvbSdtSettingsTypeDef",
    "DvbSubDestinationSettingsTypeDef",
    "DvbSubSourceSettingsTypeDef",
    "DvbTdtSettingsTypeDef",
    "Eac3SettingsTypeDef",
    "EbuTtDDestinationSettingsTypeDef",
    "EmbeddedSourceSettingsTypeDef",
    "EncoderSettingsTypeDef",
    "FailoverConditionSettingsTypeDef",
    "FailoverConditionTypeDef",
    "FeatureActivationsTypeDef",
    "FecOutputSettingsTypeDef",
    "FixedModeScheduleActionStartSettingsTypeDef",
    "Fmp4HlsSettingsTypeDef",
    "FollowModeScheduleActionStartSettingsTypeDef",
    "FrameCaptureCdnSettingsTypeDef",
    "FrameCaptureGroupSettingsTypeDef",
    "FrameCaptureOutputSettingsTypeDef",
    "FrameCaptureS3SettingsTypeDef",
    "FrameCaptureSettingsTypeDef",
    "GlobalConfigurationTypeDef",
    "H264ColorSpaceSettingsTypeDef",
    "H264FilterSettingsTypeDef",
    "H264SettingsTypeDef",
    "H265ColorSpaceSettingsTypeDef",
    "H265FilterSettingsTypeDef",
    "H265SettingsTypeDef",
    "Hdr10SettingsTypeDef",
    "HlsAkamaiSettingsTypeDef",
    "HlsBasicPutSettingsTypeDef",
    "HlsCdnSettingsTypeDef",
    "HlsGroupSettingsTypeDef",
    "HlsId3SegmentTaggingScheduleActionSettingsTypeDef",
    "HlsInputSettingsTypeDef",
    "HlsMediaStoreSettingsTypeDef",
    "HlsOutputSettingsTypeDef",
    "HlsS3SettingsTypeDef",
    "HlsSettingsTypeDef",
    "HlsTimedMetadataScheduleActionSettingsTypeDef",
    "HlsWebdavSettingsTypeDef",
    "InputAttachmentTypeDef",
    "InputChannelLevelTypeDef",
    "InputClippingSettingsTypeDef",
    "InputDestinationRequestTypeDef",
    "InputDestinationTypeDef",
    "InputDestinationVpcTypeDef",
    "InputDeviceConfigurableSettingsTypeDef",
    "InputDeviceHdSettingsTypeDef",
    "InputDeviceNetworkSettingsTypeDef",
    "InputDeviceRequestTypeDef",
    "InputDeviceSettingsTypeDef",
    "InputDeviceSummaryTypeDef",
    "InputDeviceUhdSettingsTypeDef",
    "InputLocationTypeDef",
    "InputLossBehaviorTypeDef",
    "InputLossFailoverSettingsTypeDef",
    "InputPrepareScheduleActionSettingsTypeDef",
    "InputSecurityGroupTypeDef",
    "InputSettingsTypeDef",
    "InputSourceRequestTypeDef",
    "InputSourceTypeDef",
    "InputSpecificationTypeDef",
    "InputSwitchScheduleActionSettingsTypeDef",
    "InputTypeDef",
    "InputVpcRequestTypeDef",
    "InputWhitelistRuleCidrTypeDef",
    "InputWhitelistRuleTypeDef",
    "KeyProviderSettingsTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListInputDeviceTransfersRequestRequestTypeDef",
    "ListInputDeviceTransfersResponseTypeDef",
    "ListInputDevicesRequestRequestTypeDef",
    "ListInputDevicesResponseTypeDef",
    "ListInputSecurityGroupsRequestRequestTypeDef",
    "ListInputSecurityGroupsResponseTypeDef",
    "ListInputsRequestRequestTypeDef",
    "ListInputsResponseTypeDef",
    "ListMultiplexProgramsRequestRequestTypeDef",
    "ListMultiplexProgramsResponseTypeDef",
    "ListMultiplexesRequestRequestTypeDef",
    "ListMultiplexesResponseTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsRequestRequestTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "M2tsSettingsTypeDef",
    "M3u8SettingsTypeDef",
    "MediaConnectFlowRequestTypeDef",
    "MediaConnectFlowTypeDef",
    "MediaPackageGroupSettingsTypeDef",
    "MediaPackageOutputDestinationSettingsTypeDef",
    "MotionGraphicsActivateScheduleActionSettingsTypeDef",
    "MotionGraphicsConfigurationTypeDef",
    "MotionGraphicsSettingsTypeDef",
    "Mp2SettingsTypeDef",
    "Mpeg2FilterSettingsTypeDef",
    "Mpeg2SettingsTypeDef",
    "MsSmoothGroupSettingsTypeDef",
    "MsSmoothOutputSettingsTypeDef",
    "MultiplexMediaConnectOutputDestinationSettingsTypeDef",
    "MultiplexOutputDestinationTypeDef",
    "MultiplexOutputSettingsTypeDef",
    "MultiplexProgramChannelDestinationSettingsTypeDef",
    "MultiplexProgramPacketIdentifiersMapTypeDef",
    "MultiplexProgramPipelineDetailTypeDef",
    "MultiplexProgramServiceDescriptorTypeDef",
    "MultiplexProgramSettingsTypeDef",
    "MultiplexProgramSummaryTypeDef",
    "MultiplexProgramTypeDef",
    "MultiplexSettingsSummaryTypeDef",
    "MultiplexSettingsTypeDef",
    "MultiplexStatmuxVideoSettingsTypeDef",
    "MultiplexSummaryTypeDef",
    "MultiplexTypeDef",
    "MultiplexVideoSettingsTypeDef",
    "NetworkInputSettingsTypeDef",
    "NielsenConfigurationTypeDef",
    "OfferingTypeDef",
    "OutputDestinationSettingsTypeDef",
    "OutputDestinationTypeDef",
    "OutputGroupSettingsTypeDef",
    "OutputGroupTypeDef",
    "OutputLocationRefTypeDef",
    "OutputSettingsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PauseStateScheduleActionSettingsTypeDef",
    "PipelineDetailTypeDef",
    "PipelinePauseStateSettingsTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RejectInputDeviceTransferRequestRequestTypeDef",
    "RemixSettingsTypeDef",
    "ReservationResourceSpecificationTypeDef",
    "ReservationTypeDef",
    "ResponseMetadataTypeDef",
    "RtmpGroupSettingsTypeDef",
    "RtmpOutputSettingsTypeDef",
    "ScheduleActionSettingsTypeDef",
    "ScheduleActionStartSettingsTypeDef",
    "ScheduleActionTypeDef",
    "Scte20SourceSettingsTypeDef",
    "Scte27SourceSettingsTypeDef",
    "Scte35DeliveryRestrictionsTypeDef",
    "Scte35DescriptorSettingsTypeDef",
    "Scte35DescriptorTypeDef",
    "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
    "Scte35SegmentationDescriptorTypeDef",
    "Scte35SpliceInsertScheduleActionSettingsTypeDef",
    "Scte35SpliceInsertTypeDef",
    "Scte35TimeSignalAposTypeDef",
    "Scte35TimeSignalScheduleActionSettingsTypeDef",
    "StandardHlsSettingsTypeDef",
    "StartChannelRequestRequestTypeDef",
    "StartChannelResponseTypeDef",
    "StartMultiplexRequestRequestTypeDef",
    "StartMultiplexResponseTypeDef",
    "StartTimecodeTypeDef",
    "StaticImageActivateScheduleActionSettingsTypeDef",
    "StaticImageDeactivateScheduleActionSettingsTypeDef",
    "StaticKeySettingsTypeDef",
    "StopChannelRequestRequestTypeDef",
    "StopChannelResponseTypeDef",
    "StopMultiplexRequestRequestTypeDef",
    "StopMultiplexResponseTypeDef",
    "StopTimecodeTypeDef",
    "TeletextSourceSettingsTypeDef",
    "TemporalFilterSettingsTypeDef",
    "TimecodeConfigTypeDef",
    "TransferInputDeviceRequestRequestTypeDef",
    "TransferringInputDeviceSummaryTypeDef",
    "TtmlDestinationSettingsTypeDef",
    "UdpContainerSettingsTypeDef",
    "UdpGroupSettingsTypeDef",
    "UdpOutputSettingsTypeDef",
    "UpdateChannelClassRequestRequestTypeDef",
    "UpdateChannelClassResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateInputDeviceRequestRequestTypeDef",
    "UpdateInputDeviceResponseTypeDef",
    "UpdateInputRequestRequestTypeDef",
    "UpdateInputResponseTypeDef",
    "UpdateInputSecurityGroupRequestRequestTypeDef",
    "UpdateInputSecurityGroupResponseTypeDef",
    "UpdateMultiplexProgramRequestRequestTypeDef",
    "UpdateMultiplexProgramResponseTypeDef",
    "UpdateMultiplexRequestRequestTypeDef",
    "UpdateMultiplexResponseTypeDef",
    "UpdateReservationRequestRequestTypeDef",
    "UpdateReservationResponseTypeDef",
    "VideoBlackFailoverSettingsTypeDef",
    "VideoCodecSettingsTypeDef",
    "VideoDescriptionTypeDef",
    "VideoSelectorColorSpaceSettingsTypeDef",
    "VideoSelectorPidTypeDef",
    "VideoSelectorProgramIdTypeDef",
    "VideoSelectorSettingsTypeDef",
    "VideoSelectorTypeDef",
    "VpcOutputSettingsDescriptionTypeDef",
    "VpcOutputSettingsTypeDef",
    "WaiterConfigTypeDef",
    "WavSettingsTypeDef",
    "WebvttDestinationSettingsTypeDef",
)

AacSettingsTypeDef = TypedDict(
    "AacSettingsTypeDef",
    {
        "Bitrate": float,
        "CodingMode": AacCodingModeType,
        "InputType": AacInputTypeType,
        "Profile": AacProfileType,
        "RateControlMode": AacRateControlModeType,
        "RawFormat": AacRawFormatType,
        "SampleRate": float,
        "Spec": AacSpecType,
        "VbrQuality": AacVbrQualityType,
    },
    total=False,
)

Ac3SettingsTypeDef = TypedDict(
    "Ac3SettingsTypeDef",
    {
        "Bitrate": float,
        "BitstreamMode": Ac3BitstreamModeType,
        "CodingMode": Ac3CodingModeType,
        "Dialnorm": int,
        "DrcProfile": Ac3DrcProfileType,
        "LfeFilter": Ac3LfeFilterType,
        "MetadataControl": Ac3MetadataControlType,
    },
    total=False,
)

AcceptInputDeviceTransferRequestRequestTypeDef = TypedDict(
    "AcceptInputDeviceTransferRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

AncillarySourceSettingsTypeDef = TypedDict(
    "AncillarySourceSettingsTypeDef",
    {
        "SourceAncillaryChannelNumber": int,
    },
    total=False,
)

ArchiveCdnSettingsTypeDef = TypedDict(
    "ArchiveCdnSettingsTypeDef",
    {
        "ArchiveS3Settings": "ArchiveS3SettingsTypeDef",
    },
    total=False,
)

ArchiveContainerSettingsTypeDef = TypedDict(
    "ArchiveContainerSettingsTypeDef",
    {
        "M2tsSettings": "M2tsSettingsTypeDef",
        "RawSettings": Dict[str, Any],
    },
    total=False,
)

_RequiredArchiveGroupSettingsTypeDef = TypedDict(
    "_RequiredArchiveGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)
_OptionalArchiveGroupSettingsTypeDef = TypedDict(
    "_OptionalArchiveGroupSettingsTypeDef",
    {
        "ArchiveCdnSettings": "ArchiveCdnSettingsTypeDef",
        "RolloverInterval": int,
    },
    total=False,
)

class ArchiveGroupSettingsTypeDef(
    _RequiredArchiveGroupSettingsTypeDef, _OptionalArchiveGroupSettingsTypeDef
):
    pass

_RequiredArchiveOutputSettingsTypeDef = TypedDict(
    "_RequiredArchiveOutputSettingsTypeDef",
    {
        "ContainerSettings": "ArchiveContainerSettingsTypeDef",
    },
)
_OptionalArchiveOutputSettingsTypeDef = TypedDict(
    "_OptionalArchiveOutputSettingsTypeDef",
    {
        "Extension": str,
        "NameModifier": str,
    },
    total=False,
)

class ArchiveOutputSettingsTypeDef(
    _RequiredArchiveOutputSettingsTypeDef, _OptionalArchiveOutputSettingsTypeDef
):
    pass

ArchiveS3SettingsTypeDef = TypedDict(
    "ArchiveS3SettingsTypeDef",
    {
        "CannedAcl": S3CannedAclType,
    },
    total=False,
)

AudioChannelMappingTypeDef = TypedDict(
    "AudioChannelMappingTypeDef",
    {
        "InputChannelLevels": List["InputChannelLevelTypeDef"],
        "OutputChannel": int,
    },
)

AudioCodecSettingsTypeDef = TypedDict(
    "AudioCodecSettingsTypeDef",
    {
        "AacSettings": "AacSettingsTypeDef",
        "Ac3Settings": "Ac3SettingsTypeDef",
        "Eac3Settings": "Eac3SettingsTypeDef",
        "Mp2Settings": "Mp2SettingsTypeDef",
        "PassThroughSettings": Dict[str, Any],
        "WavSettings": "WavSettingsTypeDef",
    },
    total=False,
)

_RequiredAudioDescriptionTypeDef = TypedDict(
    "_RequiredAudioDescriptionTypeDef",
    {
        "AudioSelectorName": str,
        "Name": str,
    },
)
_OptionalAudioDescriptionTypeDef = TypedDict(
    "_OptionalAudioDescriptionTypeDef",
    {
        "AudioNormalizationSettings": "AudioNormalizationSettingsTypeDef",
        "AudioType": AudioTypeType,
        "AudioTypeControl": AudioDescriptionAudioTypeControlType,
        "CodecSettings": "AudioCodecSettingsTypeDef",
        "LanguageCode": str,
        "LanguageCodeControl": AudioDescriptionLanguageCodeControlType,
        "RemixSettings": "RemixSettingsTypeDef",
        "StreamName": str,
    },
    total=False,
)

class AudioDescriptionTypeDef(_RequiredAudioDescriptionTypeDef, _OptionalAudioDescriptionTypeDef):
    pass

AudioHlsRenditionSelectionTypeDef = TypedDict(
    "AudioHlsRenditionSelectionTypeDef",
    {
        "GroupId": str,
        "Name": str,
    },
)

_RequiredAudioLanguageSelectionTypeDef = TypedDict(
    "_RequiredAudioLanguageSelectionTypeDef",
    {
        "LanguageCode": str,
    },
)
_OptionalAudioLanguageSelectionTypeDef = TypedDict(
    "_OptionalAudioLanguageSelectionTypeDef",
    {
        "LanguageSelectionPolicy": AudioLanguageSelectionPolicyType,
    },
    total=False,
)

class AudioLanguageSelectionTypeDef(
    _RequiredAudioLanguageSelectionTypeDef, _OptionalAudioLanguageSelectionTypeDef
):
    pass

AudioNormalizationSettingsTypeDef = TypedDict(
    "AudioNormalizationSettingsTypeDef",
    {
        "Algorithm": AudioNormalizationAlgorithmType,
        "AlgorithmControl": Literal["CORRECT_AUDIO"],
        "TargetLkfs": float,
    },
    total=False,
)

AudioOnlyHlsSettingsTypeDef = TypedDict(
    "AudioOnlyHlsSettingsTypeDef",
    {
        "AudioGroupId": str,
        "AudioOnlyImage": "InputLocationTypeDef",
        "AudioTrackType": AudioOnlyHlsTrackTypeType,
        "SegmentType": AudioOnlyHlsSegmentTypeType,
    },
    total=False,
)

AudioPidSelectionTypeDef = TypedDict(
    "AudioPidSelectionTypeDef",
    {
        "Pid": int,
    },
)

AudioSelectorSettingsTypeDef = TypedDict(
    "AudioSelectorSettingsTypeDef",
    {
        "AudioHlsRenditionSelection": "AudioHlsRenditionSelectionTypeDef",
        "AudioLanguageSelection": "AudioLanguageSelectionTypeDef",
        "AudioPidSelection": "AudioPidSelectionTypeDef",
        "AudioTrackSelection": "AudioTrackSelectionTypeDef",
    },
    total=False,
)

_RequiredAudioSelectorTypeDef = TypedDict(
    "_RequiredAudioSelectorTypeDef",
    {
        "Name": str,
    },
)
_OptionalAudioSelectorTypeDef = TypedDict(
    "_OptionalAudioSelectorTypeDef",
    {
        "SelectorSettings": "AudioSelectorSettingsTypeDef",
    },
    total=False,
)

class AudioSelectorTypeDef(_RequiredAudioSelectorTypeDef, _OptionalAudioSelectorTypeDef):
    pass

_RequiredAudioSilenceFailoverSettingsTypeDef = TypedDict(
    "_RequiredAudioSilenceFailoverSettingsTypeDef",
    {
        "AudioSelectorName": str,
    },
)
_OptionalAudioSilenceFailoverSettingsTypeDef = TypedDict(
    "_OptionalAudioSilenceFailoverSettingsTypeDef",
    {
        "AudioSilenceThresholdMsec": int,
    },
    total=False,
)

class AudioSilenceFailoverSettingsTypeDef(
    _RequiredAudioSilenceFailoverSettingsTypeDef, _OptionalAudioSilenceFailoverSettingsTypeDef
):
    pass

AudioTrackSelectionTypeDef = TypedDict(
    "AudioTrackSelectionTypeDef",
    {
        "Tracks": List["AudioTrackTypeDef"],
    },
)

AudioTrackTypeDef = TypedDict(
    "AudioTrackTypeDef",
    {
        "Track": int,
    },
)

_RequiredAutomaticInputFailoverSettingsTypeDef = TypedDict(
    "_RequiredAutomaticInputFailoverSettingsTypeDef",
    {
        "SecondaryInputId": str,
    },
)
_OptionalAutomaticInputFailoverSettingsTypeDef = TypedDict(
    "_OptionalAutomaticInputFailoverSettingsTypeDef",
    {
        "ErrorClearTimeMsec": int,
        "FailoverConditions": List["FailoverConditionTypeDef"],
        "InputPreference": InputPreferenceType,
    },
    total=False,
)

class AutomaticInputFailoverSettingsTypeDef(
    _RequiredAutomaticInputFailoverSettingsTypeDef, _OptionalAutomaticInputFailoverSettingsTypeDef
):
    pass

AvailBlankingTypeDef = TypedDict(
    "AvailBlankingTypeDef",
    {
        "AvailBlankingImage": "InputLocationTypeDef",
        "State": AvailBlankingStateType,
    },
    total=False,
)

AvailConfigurationTypeDef = TypedDict(
    "AvailConfigurationTypeDef",
    {
        "AvailSettings": "AvailSettingsTypeDef",
    },
    total=False,
)

AvailSettingsTypeDef = TypedDict(
    "AvailSettingsTypeDef",
    {
        "Scte35SpliceInsert": "Scte35SpliceInsertTypeDef",
        "Scte35TimeSignalApos": "Scte35TimeSignalAposTypeDef",
    },
    total=False,
)

BatchDeleteRequestRequestTypeDef = TypedDict(
    "BatchDeleteRequestRequestTypeDef",
    {
        "ChannelIds": List[str],
        "InputIds": List[str],
        "InputSecurityGroupIds": List[str],
        "MultiplexIds": List[str],
    },
    total=False,
)

BatchDeleteResponseTypeDef = TypedDict(
    "BatchDeleteResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchFailedResultModelTypeDef = TypedDict(
    "BatchFailedResultModelTypeDef",
    {
        "Arn": str,
        "Code": str,
        "Id": str,
        "Message": str,
    },
    total=False,
)

BatchScheduleActionCreateRequestTypeDef = TypedDict(
    "BatchScheduleActionCreateRequestTypeDef",
    {
        "ScheduleActions": List["ScheduleActionTypeDef"],
    },
)

BatchScheduleActionCreateResultTypeDef = TypedDict(
    "BatchScheduleActionCreateResultTypeDef",
    {
        "ScheduleActions": List["ScheduleActionTypeDef"],
    },
)

BatchScheduleActionDeleteRequestTypeDef = TypedDict(
    "BatchScheduleActionDeleteRequestTypeDef",
    {
        "ActionNames": List[str],
    },
)

BatchScheduleActionDeleteResultTypeDef = TypedDict(
    "BatchScheduleActionDeleteResultTypeDef",
    {
        "ScheduleActions": List["ScheduleActionTypeDef"],
    },
)

BatchStartRequestRequestTypeDef = TypedDict(
    "BatchStartRequestRequestTypeDef",
    {
        "ChannelIds": List[str],
        "MultiplexIds": List[str],
    },
    total=False,
)

BatchStartResponseTypeDef = TypedDict(
    "BatchStartResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStopRequestRequestTypeDef = TypedDict(
    "BatchStopRequestRequestTypeDef",
    {
        "ChannelIds": List[str],
        "MultiplexIds": List[str],
    },
    total=False,
)

BatchStopResponseTypeDef = TypedDict(
    "BatchStopResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchSuccessfulResultModelTypeDef = TypedDict(
    "BatchSuccessfulResultModelTypeDef",
    {
        "Arn": str,
        "Id": str,
        "State": str,
    },
    total=False,
)

_RequiredBatchUpdateScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredBatchUpdateScheduleRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)
_OptionalBatchUpdateScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalBatchUpdateScheduleRequestRequestTypeDef",
    {
        "Creates": "BatchScheduleActionCreateRequestTypeDef",
        "Deletes": "BatchScheduleActionDeleteRequestTypeDef",
    },
    total=False,
)

class BatchUpdateScheduleRequestRequestTypeDef(
    _RequiredBatchUpdateScheduleRequestRequestTypeDef,
    _OptionalBatchUpdateScheduleRequestRequestTypeDef,
):
    pass

BatchUpdateScheduleResponseTypeDef = TypedDict(
    "BatchUpdateScheduleResponseTypeDef",
    {
        "Creates": "BatchScheduleActionCreateResultTypeDef",
        "Deletes": "BatchScheduleActionDeleteResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlackoutSlateTypeDef = TypedDict(
    "BlackoutSlateTypeDef",
    {
        "BlackoutSlateImage": "InputLocationTypeDef",
        "NetworkEndBlackout": BlackoutSlateNetworkEndBlackoutType,
        "NetworkEndBlackoutImage": "InputLocationTypeDef",
        "NetworkId": str,
        "State": BlackoutSlateStateType,
    },
    total=False,
)

BurnInDestinationSettingsTypeDef = TypedDict(
    "BurnInDestinationSettingsTypeDef",
    {
        "Alignment": BurnInAlignmentType,
        "BackgroundColor": BurnInBackgroundColorType,
        "BackgroundOpacity": int,
        "Font": "InputLocationTypeDef",
        "FontColor": BurnInFontColorType,
        "FontOpacity": int,
        "FontResolution": int,
        "FontSize": str,
        "OutlineColor": BurnInOutlineColorType,
        "OutlineSize": int,
        "ShadowColor": BurnInShadowColorType,
        "ShadowOpacity": int,
        "ShadowXOffset": int,
        "ShadowYOffset": int,
        "TeletextGridControl": BurnInTeletextGridControlType,
        "XPosition": int,
        "YPosition": int,
    },
    total=False,
)

CancelInputDeviceTransferRequestRequestTypeDef = TypedDict(
    "CancelInputDeviceTransferRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

_RequiredCaptionDescriptionTypeDef = TypedDict(
    "_RequiredCaptionDescriptionTypeDef",
    {
        "CaptionSelectorName": str,
        "Name": str,
    },
)
_OptionalCaptionDescriptionTypeDef = TypedDict(
    "_OptionalCaptionDescriptionTypeDef",
    {
        "DestinationSettings": "CaptionDestinationSettingsTypeDef",
        "LanguageCode": str,
        "LanguageDescription": str,
    },
    total=False,
)

class CaptionDescriptionTypeDef(
    _RequiredCaptionDescriptionTypeDef, _OptionalCaptionDescriptionTypeDef
):
    pass

CaptionDestinationSettingsTypeDef = TypedDict(
    "CaptionDestinationSettingsTypeDef",
    {
        "AribDestinationSettings": Dict[str, Any],
        "BurnInDestinationSettings": "BurnInDestinationSettingsTypeDef",
        "DvbSubDestinationSettings": "DvbSubDestinationSettingsTypeDef",
        "EbuTtDDestinationSettings": "EbuTtDDestinationSettingsTypeDef",
        "EmbeddedDestinationSettings": Dict[str, Any],
        "EmbeddedPlusScte20DestinationSettings": Dict[str, Any],
        "RtmpCaptionInfoDestinationSettings": Dict[str, Any],
        "Scte20PlusEmbeddedDestinationSettings": Dict[str, Any],
        "Scte27DestinationSettings": Dict[str, Any],
        "SmpteTtDestinationSettings": Dict[str, Any],
        "TeletextDestinationSettings": Dict[str, Any],
        "TtmlDestinationSettings": "TtmlDestinationSettingsTypeDef",
        "WebvttDestinationSettings": "WebvttDestinationSettingsTypeDef",
    },
    total=False,
)

CaptionLanguageMappingTypeDef = TypedDict(
    "CaptionLanguageMappingTypeDef",
    {
        "CaptionChannel": int,
        "LanguageCode": str,
        "LanguageDescription": str,
    },
)

CaptionRectangleTypeDef = TypedDict(
    "CaptionRectangleTypeDef",
    {
        "Height": float,
        "LeftOffset": float,
        "TopOffset": float,
        "Width": float,
    },
)

CaptionSelectorSettingsTypeDef = TypedDict(
    "CaptionSelectorSettingsTypeDef",
    {
        "AncillarySourceSettings": "AncillarySourceSettingsTypeDef",
        "AribSourceSettings": Dict[str, Any],
        "DvbSubSourceSettings": "DvbSubSourceSettingsTypeDef",
        "EmbeddedSourceSettings": "EmbeddedSourceSettingsTypeDef",
        "Scte20SourceSettings": "Scte20SourceSettingsTypeDef",
        "Scte27SourceSettings": "Scte27SourceSettingsTypeDef",
        "TeletextSourceSettings": "TeletextSourceSettingsTypeDef",
    },
    total=False,
)

_RequiredCaptionSelectorTypeDef = TypedDict(
    "_RequiredCaptionSelectorTypeDef",
    {
        "Name": str,
    },
)
_OptionalCaptionSelectorTypeDef = TypedDict(
    "_OptionalCaptionSelectorTypeDef",
    {
        "LanguageCode": str,
        "SelectorSettings": "CaptionSelectorSettingsTypeDef",
    },
    total=False,
)

class CaptionSelectorTypeDef(_RequiredCaptionSelectorTypeDef, _OptionalCaptionSelectorTypeDef):
    pass

CdiInputSpecificationTypeDef = TypedDict(
    "CdiInputSpecificationTypeDef",
    {
        "Resolution": CdiInputResolutionType,
    },
    total=False,
)

ChannelEgressEndpointTypeDef = TypedDict(
    "ChannelEgressEndpointTypeDef",
    {
        "SourceIp": str,
    },
    total=False,
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
    },
    total=False,
)

CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "RequestId": str,
        "Reserved": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsTypeDef",
    },
    total=False,
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInputRequestRequestTypeDef = TypedDict(
    "CreateInputRequestRequestTypeDef",
    {
        "Destinations": List["InputDestinationRequestTypeDef"],
        "InputDevices": List["InputDeviceSettingsTypeDef"],
        "InputSecurityGroups": List[str],
        "MediaConnectFlows": List["MediaConnectFlowRequestTypeDef"],
        "Name": str,
        "RequestId": str,
        "RoleArn": str,
        "Sources": List["InputSourceRequestTypeDef"],
        "Tags": Dict[str, str],
        "Type": InputTypeType,
        "Vpc": "InputVpcRequestTypeDef",
    },
    total=False,
)

CreateInputResponseTypeDef = TypedDict(
    "CreateInputResponseTypeDef",
    {
        "Input": "InputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "CreateInputSecurityGroupRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "WhitelistRules": List["InputWhitelistRuleCidrTypeDef"],
    },
    total=False,
)

CreateInputSecurityGroupResponseTypeDef = TypedDict(
    "CreateInputSecurityGroupResponseTypeDef",
    {
        "SecurityGroup": "InputSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMultiplexProgramRequestRequestTypeDef = TypedDict(
    "CreateMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "ProgramName": str,
        "RequestId": str,
    },
)

CreateMultiplexProgramResponseTypeDef = TypedDict(
    "CreateMultiplexProgramResponseTypeDef",
    {
        "MultiplexProgram": "MultiplexProgramTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMultiplexRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMultiplexRequestRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "RequestId": str,
    },
)
_OptionalCreateMultiplexRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMultiplexRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateMultiplexRequestRequestTypeDef(
    _RequiredCreateMultiplexRequestRequestTypeDef, _OptionalCreateMultiplexRequestRequestTypeDef
):
    pass

CreateMultiplexResponseTypeDef = TypedDict(
    "CreateMultiplexResponseTypeDef",
    {
        "Multiplex": "MultiplexTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePartnerInputRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePartnerInputRequestRequestTypeDef",
    {
        "InputId": str,
    },
)
_OptionalCreatePartnerInputRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePartnerInputRequestRequestTypeDef",
    {
        "RequestId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreatePartnerInputRequestRequestTypeDef(
    _RequiredCreatePartnerInputRequestRequestTypeDef,
    _OptionalCreatePartnerInputRequestRequestTypeDef,
):
    pass

CreatePartnerInputResponseTypeDef = TypedDict(
    "CreatePartnerInputResponseTypeDef",
    {
        "Input": "InputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTagsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalCreateTagsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTagsRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateTagsRequestRequestTypeDef(
    _RequiredCreateTagsRequestRequestTypeDef, _OptionalCreateTagsRequestRequestTypeDef
):
    pass

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

DeleteChannelResponseTypeDef = TypedDict(
    "DeleteChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInputRequestRequestTypeDef = TypedDict(
    "DeleteInputRequestRequestTypeDef",
    {
        "InputId": str,
    },
)

DeleteInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "DeleteInputSecurityGroupRequestRequestTypeDef",
    {
        "InputSecurityGroupId": str,
    },
)

DeleteMultiplexProgramRequestRequestTypeDef = TypedDict(
    "DeleteMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "ProgramName": str,
    },
)

DeleteMultiplexProgramResponseTypeDef = TypedDict(
    "DeleteMultiplexProgramResponseTypeDef",
    {
        "ChannelId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "PacketIdentifiersMap": "MultiplexProgramPacketIdentifiersMapTypeDef",
        "PipelineDetails": List["MultiplexProgramPipelineDetailTypeDef"],
        "ProgramName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMultiplexRequestRequestTypeDef = TypedDict(
    "DeleteMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)

DeleteMultiplexResponseTypeDef = TypedDict(
    "DeleteMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteReservationRequestRequestTypeDef = TypedDict(
    "DeleteReservationRequestRequestTypeDef",
    {
        "ReservationId": str,
    },
)

DeleteReservationResponseTypeDef = TypedDict(
    "DeleteReservationResponseTypeDef",
    {
        "Arn": str,
        "Count": int,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "FixedPrice": float,
        "Name": str,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": Literal["NO_UPFRONT"],
        "Region": str,
        "ReservationId": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "Start": str,
        "State": ReservationStateType,
        "Tags": Dict[str, str],
        "UsagePrice": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteScheduleRequestRequestTypeDef = TypedDict(
    "DeleteScheduleRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputDeviceRequestRequestTypeDef = TypedDict(
    "DescribeInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

DescribeInputDeviceResponseTypeDef = TypedDict(
    "DescribeInputDeviceResponseTypeDef",
    {
        "Arn": str,
        "ConnectionState": InputDeviceConnectionStateType,
        "DeviceSettingsSyncState": DeviceSettingsSyncStateType,
        "DeviceUpdateStatus": DeviceUpdateStatusType,
        "HdDeviceSettings": "InputDeviceHdSettingsTypeDef",
        "Id": str,
        "MacAddress": str,
        "Name": str,
        "NetworkSettings": "InputDeviceNetworkSettingsTypeDef",
        "SerialNumber": str,
        "Type": Literal["HD"],
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputDeviceThumbnailRequestRequestTypeDef = TypedDict(
    "DescribeInputDeviceThumbnailRequestRequestTypeDef",
    {
        "InputDeviceId": str,
        "Accept": Literal["image/jpeg"],
    },
)

DescribeInputDeviceThumbnailResponseTypeDef = TypedDict(
    "DescribeInputDeviceThumbnailResponseTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": Literal["image/jpeg"],
        "ContentLength": int,
        "ETag": str,
        "LastModified": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputRequestRequestTypeDef = TypedDict(
    "DescribeInputRequestRequestTypeDef",
    {
        "InputId": str,
    },
)

DescribeInputResponseTypeDef = TypedDict(
    "DescribeInputResponseTypeDef",
    {
        "Arn": str,
        "AttachedChannels": List[str],
        "Destinations": List["InputDestinationTypeDef"],
        "Id": str,
        "InputClass": InputClassType,
        "InputDevices": List["InputDeviceSettingsTypeDef"],
        "InputPartnerIds": List[str],
        "InputSourceType": InputSourceTypeType,
        "MediaConnectFlows": List["MediaConnectFlowTypeDef"],
        "Name": str,
        "RoleArn": str,
        "SecurityGroups": List[str],
        "Sources": List["InputSourceTypeDef"],
        "State": InputStateType,
        "Tags": Dict[str, str],
        "Type": InputTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "DescribeInputSecurityGroupRequestRequestTypeDef",
    {
        "InputSecurityGroupId": str,
    },
)

DescribeInputSecurityGroupResponseTypeDef = TypedDict(
    "DescribeInputSecurityGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Inputs": List[str],
        "State": InputSecurityGroupStateType,
        "Tags": Dict[str, str],
        "WhitelistRules": List["InputWhitelistRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMultiplexProgramRequestRequestTypeDef = TypedDict(
    "DescribeMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "ProgramName": str,
    },
)

DescribeMultiplexProgramResponseTypeDef = TypedDict(
    "DescribeMultiplexProgramResponseTypeDef",
    {
        "ChannelId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "PacketIdentifiersMap": "MultiplexProgramPacketIdentifiersMapTypeDef",
        "PipelineDetails": List["MultiplexProgramPipelineDetailTypeDef"],
        "ProgramName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMultiplexRequestRequestTypeDef = TypedDict(
    "DescribeMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)

DescribeMultiplexResponseTypeDef = TypedDict(
    "DescribeMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOfferingRequestRequestTypeDef = TypedDict(
    "DescribeOfferingRequestRequestTypeDef",
    {
        "OfferingId": str,
    },
)

DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef",
    {
        "Arn": str,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "FixedPrice": float,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": Literal["NO_UPFRONT"],
        "Region": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "UsagePrice": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservationRequestRequestTypeDef = TypedDict(
    "DescribeReservationRequestRequestTypeDef",
    {
        "ReservationId": str,
    },
)

DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef",
    {
        "Arn": str,
        "Count": int,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "FixedPrice": float,
        "Name": str,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": Literal["NO_UPFRONT"],
        "Region": str,
        "ReservationId": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "Start": str,
        "State": ReservationStateType,
        "Tags": Dict[str, str],
        "UsagePrice": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScheduleRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeScheduleRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)
_OptionalDescribeScheduleRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeScheduleRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeScheduleRequestRequestTypeDef(
    _RequiredDescribeScheduleRequestRequestTypeDef, _OptionalDescribeScheduleRequestRequestTypeDef
):
    pass

DescribeScheduleResponseTypeDef = TypedDict(
    "DescribeScheduleResponseTypeDef",
    {
        "NextToken": str,
        "ScheduleActions": List["ScheduleActionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDvbNitSettingsTypeDef = TypedDict(
    "_RequiredDvbNitSettingsTypeDef",
    {
        "NetworkId": int,
        "NetworkName": str,
    },
)
_OptionalDvbNitSettingsTypeDef = TypedDict(
    "_OptionalDvbNitSettingsTypeDef",
    {
        "RepInterval": int,
    },
    total=False,
)

class DvbNitSettingsTypeDef(_RequiredDvbNitSettingsTypeDef, _OptionalDvbNitSettingsTypeDef):
    pass

DvbSdtSettingsTypeDef = TypedDict(
    "DvbSdtSettingsTypeDef",
    {
        "OutputSdt": DvbSdtOutputSdtType,
        "RepInterval": int,
        "ServiceName": str,
        "ServiceProviderName": str,
    },
    total=False,
)

DvbSubDestinationSettingsTypeDef = TypedDict(
    "DvbSubDestinationSettingsTypeDef",
    {
        "Alignment": DvbSubDestinationAlignmentType,
        "BackgroundColor": DvbSubDestinationBackgroundColorType,
        "BackgroundOpacity": int,
        "Font": "InputLocationTypeDef",
        "FontColor": DvbSubDestinationFontColorType,
        "FontOpacity": int,
        "FontResolution": int,
        "FontSize": str,
        "OutlineColor": DvbSubDestinationOutlineColorType,
        "OutlineSize": int,
        "ShadowColor": DvbSubDestinationShadowColorType,
        "ShadowOpacity": int,
        "ShadowXOffset": int,
        "ShadowYOffset": int,
        "TeletextGridControl": DvbSubDestinationTeletextGridControlType,
        "XPosition": int,
        "YPosition": int,
    },
    total=False,
)

DvbSubSourceSettingsTypeDef = TypedDict(
    "DvbSubSourceSettingsTypeDef",
    {
        "OcrLanguage": DvbSubOcrLanguageType,
        "Pid": int,
    },
    total=False,
)

DvbTdtSettingsTypeDef = TypedDict(
    "DvbTdtSettingsTypeDef",
    {
        "RepInterval": int,
    },
    total=False,
)

Eac3SettingsTypeDef = TypedDict(
    "Eac3SettingsTypeDef",
    {
        "AttenuationControl": Eac3AttenuationControlType,
        "Bitrate": float,
        "BitstreamMode": Eac3BitstreamModeType,
        "CodingMode": Eac3CodingModeType,
        "DcFilter": Eac3DcFilterType,
        "Dialnorm": int,
        "DrcLine": Eac3DrcLineType,
        "DrcRf": Eac3DrcRfType,
        "LfeControl": Eac3LfeControlType,
        "LfeFilter": Eac3LfeFilterType,
        "LoRoCenterMixLevel": float,
        "LoRoSurroundMixLevel": float,
        "LtRtCenterMixLevel": float,
        "LtRtSurroundMixLevel": float,
        "MetadataControl": Eac3MetadataControlType,
        "PassthroughControl": Eac3PassthroughControlType,
        "PhaseControl": Eac3PhaseControlType,
        "StereoDownmix": Eac3StereoDownmixType,
        "SurroundExMode": Eac3SurroundExModeType,
        "SurroundMode": Eac3SurroundModeType,
    },
    total=False,
)

EbuTtDDestinationSettingsTypeDef = TypedDict(
    "EbuTtDDestinationSettingsTypeDef",
    {
        "CopyrightHolder": str,
        "FillLineGap": EbuTtDFillLineGapControlType,
        "FontFamily": str,
        "StyleControl": EbuTtDDestinationStyleControlType,
    },
    total=False,
)

EmbeddedSourceSettingsTypeDef = TypedDict(
    "EmbeddedSourceSettingsTypeDef",
    {
        "Convert608To708": EmbeddedConvert608To708Type,
        "Scte20Detection": EmbeddedScte20DetectionType,
        "Source608ChannelNumber": int,
        "Source608TrackNumber": int,
    },
    total=False,
)

_RequiredEncoderSettingsTypeDef = TypedDict(
    "_RequiredEncoderSettingsTypeDef",
    {
        "AudioDescriptions": List["AudioDescriptionTypeDef"],
        "OutputGroups": List["OutputGroupTypeDef"],
        "TimecodeConfig": "TimecodeConfigTypeDef",
        "VideoDescriptions": List["VideoDescriptionTypeDef"],
    },
)
_OptionalEncoderSettingsTypeDef = TypedDict(
    "_OptionalEncoderSettingsTypeDef",
    {
        "AvailBlanking": "AvailBlankingTypeDef",
        "AvailConfiguration": "AvailConfigurationTypeDef",
        "BlackoutSlate": "BlackoutSlateTypeDef",
        "CaptionDescriptions": List["CaptionDescriptionTypeDef"],
        "FeatureActivations": "FeatureActivationsTypeDef",
        "GlobalConfiguration": "GlobalConfigurationTypeDef",
        "MotionGraphicsConfiguration": "MotionGraphicsConfigurationTypeDef",
        "NielsenConfiguration": "NielsenConfigurationTypeDef",
    },
    total=False,
)

class EncoderSettingsTypeDef(_RequiredEncoderSettingsTypeDef, _OptionalEncoderSettingsTypeDef):
    pass

FailoverConditionSettingsTypeDef = TypedDict(
    "FailoverConditionSettingsTypeDef",
    {
        "AudioSilenceSettings": "AudioSilenceFailoverSettingsTypeDef",
        "InputLossSettings": "InputLossFailoverSettingsTypeDef",
        "VideoBlackSettings": "VideoBlackFailoverSettingsTypeDef",
    },
    total=False,
)

FailoverConditionTypeDef = TypedDict(
    "FailoverConditionTypeDef",
    {
        "FailoverConditionSettings": "FailoverConditionSettingsTypeDef",
    },
    total=False,
)

FeatureActivationsTypeDef = TypedDict(
    "FeatureActivationsTypeDef",
    {
        "InputPrepareScheduleActions": FeatureActivationsInputPrepareScheduleActionsType,
    },
    total=False,
)

FecOutputSettingsTypeDef = TypedDict(
    "FecOutputSettingsTypeDef",
    {
        "ColumnDepth": int,
        "IncludeFec": FecOutputIncludeFecType,
        "RowLength": int,
    },
    total=False,
)

FixedModeScheduleActionStartSettingsTypeDef = TypedDict(
    "FixedModeScheduleActionStartSettingsTypeDef",
    {
        "Time": str,
    },
)

Fmp4HlsSettingsTypeDef = TypedDict(
    "Fmp4HlsSettingsTypeDef",
    {
        "AudioRenditionSets": str,
        "NielsenId3Behavior": Fmp4NielsenId3BehaviorType,
        "TimedMetadataBehavior": Fmp4TimedMetadataBehaviorType,
    },
    total=False,
)

FollowModeScheduleActionStartSettingsTypeDef = TypedDict(
    "FollowModeScheduleActionStartSettingsTypeDef",
    {
        "FollowPoint": FollowPointType,
        "ReferenceActionName": str,
    },
)

FrameCaptureCdnSettingsTypeDef = TypedDict(
    "FrameCaptureCdnSettingsTypeDef",
    {
        "FrameCaptureS3Settings": "FrameCaptureS3SettingsTypeDef",
    },
    total=False,
)

_RequiredFrameCaptureGroupSettingsTypeDef = TypedDict(
    "_RequiredFrameCaptureGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)
_OptionalFrameCaptureGroupSettingsTypeDef = TypedDict(
    "_OptionalFrameCaptureGroupSettingsTypeDef",
    {
        "FrameCaptureCdnSettings": "FrameCaptureCdnSettingsTypeDef",
    },
    total=False,
)

class FrameCaptureGroupSettingsTypeDef(
    _RequiredFrameCaptureGroupSettingsTypeDef, _OptionalFrameCaptureGroupSettingsTypeDef
):
    pass

FrameCaptureOutputSettingsTypeDef = TypedDict(
    "FrameCaptureOutputSettingsTypeDef",
    {
        "NameModifier": str,
    },
    total=False,
)

FrameCaptureS3SettingsTypeDef = TypedDict(
    "FrameCaptureS3SettingsTypeDef",
    {
        "CannedAcl": S3CannedAclType,
    },
    total=False,
)

FrameCaptureSettingsTypeDef = TypedDict(
    "FrameCaptureSettingsTypeDef",
    {
        "CaptureInterval": int,
        "CaptureIntervalUnits": FrameCaptureIntervalUnitType,
    },
    total=False,
)

GlobalConfigurationTypeDef = TypedDict(
    "GlobalConfigurationTypeDef",
    {
        "InitialAudioGain": int,
        "InputEndAction": GlobalConfigurationInputEndActionType,
        "InputLossBehavior": "InputLossBehaviorTypeDef",
        "OutputLockingMode": GlobalConfigurationOutputLockingModeType,
        "OutputTimingSource": GlobalConfigurationOutputTimingSourceType,
        "SupportLowFramerateInputs": GlobalConfigurationLowFramerateInputsType,
    },
    total=False,
)

H264ColorSpaceSettingsTypeDef = TypedDict(
    "H264ColorSpaceSettingsTypeDef",
    {
        "ColorSpacePassthroughSettings": Dict[str, Any],
        "Rec601Settings": Dict[str, Any],
        "Rec709Settings": Dict[str, Any],
    },
    total=False,
)

H264FilterSettingsTypeDef = TypedDict(
    "H264FilterSettingsTypeDef",
    {
        "TemporalFilterSettings": "TemporalFilterSettingsTypeDef",
    },
    total=False,
)

H264SettingsTypeDef = TypedDict(
    "H264SettingsTypeDef",
    {
        "AdaptiveQuantization": H264AdaptiveQuantizationType,
        "AfdSignaling": AfdSignalingType,
        "Bitrate": int,
        "BufFillPct": int,
        "BufSize": int,
        "ColorMetadata": H264ColorMetadataType,
        "ColorSpaceSettings": "H264ColorSpaceSettingsTypeDef",
        "EntropyEncoding": H264EntropyEncodingType,
        "FilterSettings": "H264FilterSettingsTypeDef",
        "FixedAfd": FixedAfdType,
        "FlickerAq": H264FlickerAqType,
        "ForceFieldPictures": H264ForceFieldPicturesType,
        "FramerateControl": H264FramerateControlType,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopBReference": H264GopBReferenceType,
        "GopClosedCadence": int,
        "GopNumBFrames": int,
        "GopSize": float,
        "GopSizeUnits": H264GopSizeUnitsType,
        "Level": H264LevelType,
        "LookAheadRateControl": H264LookAheadRateControlType,
        "MaxBitrate": int,
        "MinIInterval": int,
        "NumRefFrames": int,
        "ParControl": H264ParControlType,
        "ParDenominator": int,
        "ParNumerator": int,
        "Profile": H264ProfileType,
        "QualityLevel": H264QualityLevelType,
        "QvbrQualityLevel": int,
        "RateControlMode": H264RateControlModeType,
        "ScanType": H264ScanTypeType,
        "SceneChangeDetect": H264SceneChangeDetectType,
        "Slices": int,
        "Softness": int,
        "SpatialAq": H264SpatialAqType,
        "SubgopLength": H264SubGopLengthType,
        "Syntax": H264SyntaxType,
        "TemporalAq": H264TemporalAqType,
        "TimecodeInsertion": H264TimecodeInsertionBehaviorType,
    },
    total=False,
)

H265ColorSpaceSettingsTypeDef = TypedDict(
    "H265ColorSpaceSettingsTypeDef",
    {
        "ColorSpacePassthroughSettings": Dict[str, Any],
        "Hdr10Settings": "Hdr10SettingsTypeDef",
        "Rec601Settings": Dict[str, Any],
        "Rec709Settings": Dict[str, Any],
    },
    total=False,
)

H265FilterSettingsTypeDef = TypedDict(
    "H265FilterSettingsTypeDef",
    {
        "TemporalFilterSettings": "TemporalFilterSettingsTypeDef",
    },
    total=False,
)

_RequiredH265SettingsTypeDef = TypedDict(
    "_RequiredH265SettingsTypeDef",
    {
        "FramerateDenominator": int,
        "FramerateNumerator": int,
    },
)
_OptionalH265SettingsTypeDef = TypedDict(
    "_OptionalH265SettingsTypeDef",
    {
        "AdaptiveQuantization": H265AdaptiveQuantizationType,
        "AfdSignaling": AfdSignalingType,
        "AlternativeTransferFunction": H265AlternativeTransferFunctionType,
        "Bitrate": int,
        "BufSize": int,
        "ColorMetadata": H265ColorMetadataType,
        "ColorSpaceSettings": "H265ColorSpaceSettingsTypeDef",
        "FilterSettings": "H265FilterSettingsTypeDef",
        "FixedAfd": FixedAfdType,
        "FlickerAq": H265FlickerAqType,
        "GopClosedCadence": int,
        "GopSize": float,
        "GopSizeUnits": H265GopSizeUnitsType,
        "Level": H265LevelType,
        "LookAheadRateControl": H265LookAheadRateControlType,
        "MaxBitrate": int,
        "MinIInterval": int,
        "ParDenominator": int,
        "ParNumerator": int,
        "Profile": H265ProfileType,
        "QvbrQualityLevel": int,
        "RateControlMode": H265RateControlModeType,
        "ScanType": H265ScanTypeType,
        "SceneChangeDetect": H265SceneChangeDetectType,
        "Slices": int,
        "Tier": H265TierType,
        "TimecodeInsertion": H265TimecodeInsertionBehaviorType,
    },
    total=False,
)

class H265SettingsTypeDef(_RequiredH265SettingsTypeDef, _OptionalH265SettingsTypeDef):
    pass

Hdr10SettingsTypeDef = TypedDict(
    "Hdr10SettingsTypeDef",
    {
        "MaxCll": int,
        "MaxFall": int,
    },
    total=False,
)

HlsAkamaiSettingsTypeDef = TypedDict(
    "HlsAkamaiSettingsTypeDef",
    {
        "ConnectionRetryInterval": int,
        "FilecacheDuration": int,
        "HttpTransferMode": HlsAkamaiHttpTransferModeType,
        "NumRetries": int,
        "RestartDelay": int,
        "Salt": str,
        "Token": str,
    },
    total=False,
)

HlsBasicPutSettingsTypeDef = TypedDict(
    "HlsBasicPutSettingsTypeDef",
    {
        "ConnectionRetryInterval": int,
        "FilecacheDuration": int,
        "NumRetries": int,
        "RestartDelay": int,
    },
    total=False,
)

HlsCdnSettingsTypeDef = TypedDict(
    "HlsCdnSettingsTypeDef",
    {
        "HlsAkamaiSettings": "HlsAkamaiSettingsTypeDef",
        "HlsBasicPutSettings": "HlsBasicPutSettingsTypeDef",
        "HlsMediaStoreSettings": "HlsMediaStoreSettingsTypeDef",
        "HlsS3Settings": "HlsS3SettingsTypeDef",
        "HlsWebdavSettings": "HlsWebdavSettingsTypeDef",
    },
    total=False,
)

_RequiredHlsGroupSettingsTypeDef = TypedDict(
    "_RequiredHlsGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)
_OptionalHlsGroupSettingsTypeDef = TypedDict(
    "_OptionalHlsGroupSettingsTypeDef",
    {
        "AdMarkers": List[HlsAdMarkersType],
        "BaseUrlContent": str,
        "BaseUrlContent1": str,
        "BaseUrlManifest": str,
        "BaseUrlManifest1": str,
        "CaptionLanguageMappings": List["CaptionLanguageMappingTypeDef"],
        "CaptionLanguageSetting": HlsCaptionLanguageSettingType,
        "ClientCache": HlsClientCacheType,
        "CodecSpecification": HlsCodecSpecificationType,
        "ConstantIv": str,
        "DirectoryStructure": HlsDirectoryStructureType,
        "DiscontinuityTags": HlsDiscontinuityTagsType,
        "EncryptionType": HlsEncryptionTypeType,
        "HlsCdnSettings": "HlsCdnSettingsTypeDef",
        "HlsId3SegmentTagging": HlsId3SegmentTaggingStateType,
        "IFrameOnlyPlaylists": IFrameOnlyPlaylistTypeType,
        "IncompleteSegmentBehavior": HlsIncompleteSegmentBehaviorType,
        "IndexNSegments": int,
        "InputLossAction": InputLossActionForHlsOutType,
        "IvInManifest": HlsIvInManifestType,
        "IvSource": HlsIvSourceType,
        "KeepSegments": int,
        "KeyFormat": str,
        "KeyFormatVersions": str,
        "KeyProviderSettings": "KeyProviderSettingsTypeDef",
        "ManifestCompression": HlsManifestCompressionType,
        "ManifestDurationFormat": HlsManifestDurationFormatType,
        "MinSegmentLength": int,
        "Mode": HlsModeType,
        "OutputSelection": HlsOutputSelectionType,
        "ProgramDateTime": HlsProgramDateTimeType,
        "ProgramDateTimePeriod": int,
        "RedundantManifest": HlsRedundantManifestType,
        "SegmentLength": int,
        "SegmentationMode": HlsSegmentationModeType,
        "SegmentsPerSubdirectory": int,
        "StreamInfResolution": HlsStreamInfResolutionType,
        "TimedMetadataId3Frame": HlsTimedMetadataId3FrameType,
        "TimedMetadataId3Period": int,
        "TimestampDeltaMilliseconds": int,
        "TsFileMode": HlsTsFileModeType,
    },
    total=False,
)

class HlsGroupSettingsTypeDef(_RequiredHlsGroupSettingsTypeDef, _OptionalHlsGroupSettingsTypeDef):
    pass

HlsId3SegmentTaggingScheduleActionSettingsTypeDef = TypedDict(
    "HlsId3SegmentTaggingScheduleActionSettingsTypeDef",
    {
        "Tag": str,
    },
)

HlsInputSettingsTypeDef = TypedDict(
    "HlsInputSettingsTypeDef",
    {
        "Bandwidth": int,
        "BufferSegments": int,
        "Retries": int,
        "RetryInterval": int,
        "Scte35Source": HlsScte35SourceTypeType,
    },
    total=False,
)

HlsMediaStoreSettingsTypeDef = TypedDict(
    "HlsMediaStoreSettingsTypeDef",
    {
        "ConnectionRetryInterval": int,
        "FilecacheDuration": int,
        "MediaStoreStorageClass": Literal["TEMPORAL"],
        "NumRetries": int,
        "RestartDelay": int,
    },
    total=False,
)

_RequiredHlsOutputSettingsTypeDef = TypedDict(
    "_RequiredHlsOutputSettingsTypeDef",
    {
        "HlsSettings": "HlsSettingsTypeDef",
    },
)
_OptionalHlsOutputSettingsTypeDef = TypedDict(
    "_OptionalHlsOutputSettingsTypeDef",
    {
        "H265PackagingType": HlsH265PackagingTypeType,
        "NameModifier": str,
        "SegmentModifier": str,
    },
    total=False,
)

class HlsOutputSettingsTypeDef(
    _RequiredHlsOutputSettingsTypeDef, _OptionalHlsOutputSettingsTypeDef
):
    pass

HlsS3SettingsTypeDef = TypedDict(
    "HlsS3SettingsTypeDef",
    {
        "CannedAcl": S3CannedAclType,
    },
    total=False,
)

HlsSettingsTypeDef = TypedDict(
    "HlsSettingsTypeDef",
    {
        "AudioOnlyHlsSettings": "AudioOnlyHlsSettingsTypeDef",
        "Fmp4HlsSettings": "Fmp4HlsSettingsTypeDef",
        "FrameCaptureHlsSettings": Dict[str, Any],
        "StandardHlsSettings": "StandardHlsSettingsTypeDef",
    },
    total=False,
)

HlsTimedMetadataScheduleActionSettingsTypeDef = TypedDict(
    "HlsTimedMetadataScheduleActionSettingsTypeDef",
    {
        "Id3": str,
    },
)

HlsWebdavSettingsTypeDef = TypedDict(
    "HlsWebdavSettingsTypeDef",
    {
        "ConnectionRetryInterval": int,
        "FilecacheDuration": int,
        "HttpTransferMode": HlsWebdavHttpTransferModeType,
        "NumRetries": int,
        "RestartDelay": int,
    },
    total=False,
)

InputAttachmentTypeDef = TypedDict(
    "InputAttachmentTypeDef",
    {
        "AutomaticInputFailoverSettings": "AutomaticInputFailoverSettingsTypeDef",
        "InputAttachmentName": str,
        "InputId": str,
        "InputSettings": "InputSettingsTypeDef",
    },
    total=False,
)

InputChannelLevelTypeDef = TypedDict(
    "InputChannelLevelTypeDef",
    {
        "Gain": int,
        "InputChannel": int,
    },
)

_RequiredInputClippingSettingsTypeDef = TypedDict(
    "_RequiredInputClippingSettingsTypeDef",
    {
        "InputTimecodeSource": InputTimecodeSourceType,
    },
)
_OptionalInputClippingSettingsTypeDef = TypedDict(
    "_OptionalInputClippingSettingsTypeDef",
    {
        "StartTimecode": "StartTimecodeTypeDef",
        "StopTimecode": "StopTimecodeTypeDef",
    },
    total=False,
)

class InputClippingSettingsTypeDef(
    _RequiredInputClippingSettingsTypeDef, _OptionalInputClippingSettingsTypeDef
):
    pass

InputDestinationRequestTypeDef = TypedDict(
    "InputDestinationRequestTypeDef",
    {
        "StreamName": str,
    },
    total=False,
)

InputDestinationTypeDef = TypedDict(
    "InputDestinationTypeDef",
    {
        "Ip": str,
        "Port": str,
        "Url": str,
        "Vpc": "InputDestinationVpcTypeDef",
    },
    total=False,
)

InputDestinationVpcTypeDef = TypedDict(
    "InputDestinationVpcTypeDef",
    {
        "AvailabilityZone": str,
        "NetworkInterfaceId": str,
    },
    total=False,
)

InputDeviceConfigurableSettingsTypeDef = TypedDict(
    "InputDeviceConfigurableSettingsTypeDef",
    {
        "ConfiguredInput": InputDeviceConfiguredInputType,
        "MaxBitrate": int,
    },
    total=False,
)

InputDeviceHdSettingsTypeDef = TypedDict(
    "InputDeviceHdSettingsTypeDef",
    {
        "ActiveInput": InputDeviceActiveInputType,
        "ConfiguredInput": InputDeviceConfiguredInputType,
        "DeviceState": InputDeviceStateType,
        "Framerate": float,
        "Height": int,
        "MaxBitrate": int,
        "ScanType": InputDeviceScanTypeType,
        "Width": int,
    },
    total=False,
)

InputDeviceNetworkSettingsTypeDef = TypedDict(
    "InputDeviceNetworkSettingsTypeDef",
    {
        "DnsAddresses": List[str],
        "Gateway": str,
        "IpAddress": str,
        "IpScheme": InputDeviceIpSchemeType,
        "SubnetMask": str,
    },
    total=False,
)

InputDeviceRequestTypeDef = TypedDict(
    "InputDeviceRequestTypeDef",
    {
        "Id": str,
    },
    total=False,
)

InputDeviceSettingsTypeDef = TypedDict(
    "InputDeviceSettingsTypeDef",
    {
        "Id": str,
    },
    total=False,
)

InputDeviceSummaryTypeDef = TypedDict(
    "InputDeviceSummaryTypeDef",
    {
        "Arn": str,
        "ConnectionState": InputDeviceConnectionStateType,
        "DeviceSettingsSyncState": DeviceSettingsSyncStateType,
        "DeviceUpdateStatus": DeviceUpdateStatusType,
        "HdDeviceSettings": "InputDeviceHdSettingsTypeDef",
        "Id": str,
        "MacAddress": str,
        "Name": str,
        "NetworkSettings": "InputDeviceNetworkSettingsTypeDef",
        "SerialNumber": str,
        "Type": Literal["HD"],
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
    },
    total=False,
)

InputDeviceUhdSettingsTypeDef = TypedDict(
    "InputDeviceUhdSettingsTypeDef",
    {
        "ActiveInput": InputDeviceActiveInputType,
        "ConfiguredInput": InputDeviceConfiguredInputType,
        "DeviceState": InputDeviceStateType,
        "Framerate": float,
        "Height": int,
        "MaxBitrate": int,
        "ScanType": InputDeviceScanTypeType,
        "Width": int,
    },
    total=False,
)

_RequiredInputLocationTypeDef = TypedDict(
    "_RequiredInputLocationTypeDef",
    {
        "Uri": str,
    },
)
_OptionalInputLocationTypeDef = TypedDict(
    "_OptionalInputLocationTypeDef",
    {
        "PasswordParam": str,
        "Username": str,
    },
    total=False,
)

class InputLocationTypeDef(_RequiredInputLocationTypeDef, _OptionalInputLocationTypeDef):
    pass

InputLossBehaviorTypeDef = TypedDict(
    "InputLossBehaviorTypeDef",
    {
        "BlackFrameMsec": int,
        "InputLossImageColor": str,
        "InputLossImageSlate": "InputLocationTypeDef",
        "InputLossImageType": InputLossImageTypeType,
        "RepeatFrameMsec": int,
    },
    total=False,
)

InputLossFailoverSettingsTypeDef = TypedDict(
    "InputLossFailoverSettingsTypeDef",
    {
        "InputLossThresholdMsec": int,
    },
    total=False,
)

InputPrepareScheduleActionSettingsTypeDef = TypedDict(
    "InputPrepareScheduleActionSettingsTypeDef",
    {
        "InputAttachmentNameReference": str,
        "InputClippingSettings": "InputClippingSettingsTypeDef",
        "UrlPath": List[str],
    },
    total=False,
)

InputSecurityGroupTypeDef = TypedDict(
    "InputSecurityGroupTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Inputs": List[str],
        "State": InputSecurityGroupStateType,
        "Tags": Dict[str, str],
        "WhitelistRules": List["InputWhitelistRuleTypeDef"],
    },
    total=False,
)

InputSettingsTypeDef = TypedDict(
    "InputSettingsTypeDef",
    {
        "AudioSelectors": List["AudioSelectorTypeDef"],
        "CaptionSelectors": List["CaptionSelectorTypeDef"],
        "DeblockFilter": InputDeblockFilterType,
        "DenoiseFilter": InputDenoiseFilterType,
        "FilterStrength": int,
        "InputFilter": InputFilterType,
        "NetworkInputSettings": "NetworkInputSettingsTypeDef",
        "Smpte2038DataPreference": Smpte2038DataPreferenceType,
        "SourceEndBehavior": InputSourceEndBehaviorType,
        "VideoSelector": "VideoSelectorTypeDef",
    },
    total=False,
)

InputSourceRequestTypeDef = TypedDict(
    "InputSourceRequestTypeDef",
    {
        "PasswordParam": str,
        "Url": str,
        "Username": str,
    },
    total=False,
)

InputSourceTypeDef = TypedDict(
    "InputSourceTypeDef",
    {
        "PasswordParam": str,
        "Url": str,
        "Username": str,
    },
    total=False,
)

InputSpecificationTypeDef = TypedDict(
    "InputSpecificationTypeDef",
    {
        "Codec": InputCodecType,
        "MaximumBitrate": InputMaximumBitrateType,
        "Resolution": InputResolutionType,
    },
    total=False,
)

_RequiredInputSwitchScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredInputSwitchScheduleActionSettingsTypeDef",
    {
        "InputAttachmentNameReference": str,
    },
)
_OptionalInputSwitchScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalInputSwitchScheduleActionSettingsTypeDef",
    {
        "InputClippingSettings": "InputClippingSettingsTypeDef",
        "UrlPath": List[str],
    },
    total=False,
)

class InputSwitchScheduleActionSettingsTypeDef(
    _RequiredInputSwitchScheduleActionSettingsTypeDef,
    _OptionalInputSwitchScheduleActionSettingsTypeDef,
):
    pass

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "Arn": str,
        "AttachedChannels": List[str],
        "Destinations": List["InputDestinationTypeDef"],
        "Id": str,
        "InputClass": InputClassType,
        "InputDevices": List["InputDeviceSettingsTypeDef"],
        "InputPartnerIds": List[str],
        "InputSourceType": InputSourceTypeType,
        "MediaConnectFlows": List["MediaConnectFlowTypeDef"],
        "Name": str,
        "RoleArn": str,
        "SecurityGroups": List[str],
        "Sources": List["InputSourceTypeDef"],
        "State": InputStateType,
        "Tags": Dict[str, str],
        "Type": InputTypeType,
    },
    total=False,
)

_RequiredInputVpcRequestTypeDef = TypedDict(
    "_RequiredInputVpcRequestTypeDef",
    {
        "SubnetIds": List[str],
    },
)
_OptionalInputVpcRequestTypeDef = TypedDict(
    "_OptionalInputVpcRequestTypeDef",
    {
        "SecurityGroupIds": List[str],
    },
    total=False,
)

class InputVpcRequestTypeDef(_RequiredInputVpcRequestTypeDef, _OptionalInputVpcRequestTypeDef):
    pass

InputWhitelistRuleCidrTypeDef = TypedDict(
    "InputWhitelistRuleCidrTypeDef",
    {
        "Cidr": str,
    },
    total=False,
)

InputWhitelistRuleTypeDef = TypedDict(
    "InputWhitelistRuleTypeDef",
    {
        "Cidr": str,
    },
    total=False,
)

KeyProviderSettingsTypeDef = TypedDict(
    "KeyProviderSettingsTypeDef",
    {
        "StaticKeySettings": "StaticKeySettingsTypeDef",
    },
    total=False,
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List["ChannelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInputDeviceTransfersRequestRequestTypeDef = TypedDict(
    "_RequiredListInputDeviceTransfersRequestRequestTypeDef",
    {
        "TransferType": str,
    },
)
_OptionalListInputDeviceTransfersRequestRequestTypeDef = TypedDict(
    "_OptionalListInputDeviceTransfersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListInputDeviceTransfersRequestRequestTypeDef(
    _RequiredListInputDeviceTransfersRequestRequestTypeDef,
    _OptionalListInputDeviceTransfersRequestRequestTypeDef,
):
    pass

ListInputDeviceTransfersResponseTypeDef = TypedDict(
    "ListInputDeviceTransfersResponseTypeDef",
    {
        "InputDeviceTransfers": List["TransferringInputDeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputDevicesRequestRequestTypeDef = TypedDict(
    "ListInputDevicesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInputDevicesResponseTypeDef = TypedDict(
    "ListInputDevicesResponseTypeDef",
    {
        "InputDevices": List["InputDeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputSecurityGroupsRequestRequestTypeDef = TypedDict(
    "ListInputSecurityGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInputSecurityGroupsResponseTypeDef = TypedDict(
    "ListInputSecurityGroupsResponseTypeDef",
    {
        "InputSecurityGroups": List["InputSecurityGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInputsRequestRequestTypeDef = TypedDict(
    "ListInputsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListInputsResponseTypeDef = TypedDict(
    "ListInputsResponseTypeDef",
    {
        "Inputs": List["InputTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMultiplexProgramsRequestRequestTypeDef = TypedDict(
    "_RequiredListMultiplexProgramsRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)
_OptionalListMultiplexProgramsRequestRequestTypeDef = TypedDict(
    "_OptionalListMultiplexProgramsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListMultiplexProgramsRequestRequestTypeDef(
    _RequiredListMultiplexProgramsRequestRequestTypeDef,
    _OptionalListMultiplexProgramsRequestRequestTypeDef,
):
    pass

ListMultiplexProgramsResponseTypeDef = TypedDict(
    "ListMultiplexProgramsResponseTypeDef",
    {
        "MultiplexPrograms": List["MultiplexProgramSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMultiplexesRequestRequestTypeDef = TypedDict(
    "ListMultiplexesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListMultiplexesResponseTypeDef = TypedDict(
    "ListMultiplexesResponseTypeDef",
    {
        "Multiplexes": List["MultiplexSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "ChannelClass": str,
        "ChannelConfiguration": str,
        "Codec": str,
        "Duration": str,
        "MaxResults": int,
        "MaximumBitrate": str,
        "MaximumFramerate": str,
        "NextToken": str,
        "Resolution": str,
        "ResourceType": str,
        "SpecialFeature": str,
        "VideoQuality": str,
    },
    total=False,
)

ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "Offerings": List["OfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReservationsRequestRequestTypeDef = TypedDict(
    "ListReservationsRequestRequestTypeDef",
    {
        "ChannelClass": str,
        "Codec": str,
        "MaxResults": int,
        "MaximumBitrate": str,
        "MaximumFramerate": str,
        "NextToken": str,
        "Resolution": str,
        "ResourceType": str,
        "SpecialFeature": str,
        "VideoQuality": str,
    },
    total=False,
)

ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {
        "NextToken": str,
        "Reservations": List["ReservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

M2tsSettingsTypeDef = TypedDict(
    "M2tsSettingsTypeDef",
    {
        "AbsentInputAudioBehavior": M2tsAbsentInputAudioBehaviorType,
        "Arib": M2tsAribType,
        "AribCaptionsPid": str,
        "AribCaptionsPidControl": M2tsAribCaptionsPidControlType,
        "AudioBufferModel": M2tsAudioBufferModelType,
        "AudioFramesPerPes": int,
        "AudioPids": str,
        "AudioStreamType": M2tsAudioStreamTypeType,
        "Bitrate": int,
        "BufferModel": M2tsBufferModelType,
        "CcDescriptor": M2tsCcDescriptorType,
        "DvbNitSettings": "DvbNitSettingsTypeDef",
        "DvbSdtSettings": "DvbSdtSettingsTypeDef",
        "DvbSubPids": str,
        "DvbTdtSettings": "DvbTdtSettingsTypeDef",
        "DvbTeletextPid": str,
        "Ebif": M2tsEbifControlType,
        "EbpAudioInterval": M2tsAudioIntervalType,
        "EbpLookaheadMs": int,
        "EbpPlacement": M2tsEbpPlacementType,
        "EcmPid": str,
        "EsRateInPes": M2tsEsRateInPesType,
        "EtvPlatformPid": str,
        "EtvSignalPid": str,
        "FragmentTime": float,
        "Klv": M2tsKlvType,
        "KlvDataPids": str,
        "NielsenId3Behavior": M2tsNielsenId3BehaviorType,
        "NullPacketBitrate": float,
        "PatInterval": int,
        "PcrControl": M2tsPcrControlType,
        "PcrPeriod": int,
        "PcrPid": str,
        "PmtInterval": int,
        "PmtPid": str,
        "ProgramNum": int,
        "RateMode": M2tsRateModeType,
        "Scte27Pids": str,
        "Scte35Control": M2tsScte35ControlType,
        "Scte35Pid": str,
        "SegmentationMarkers": M2tsSegmentationMarkersType,
        "SegmentationStyle": M2tsSegmentationStyleType,
        "SegmentationTime": float,
        "TimedMetadataBehavior": M2tsTimedMetadataBehaviorType,
        "TimedMetadataPid": str,
        "TransportStreamId": int,
        "VideoPid": str,
    },
    total=False,
)

M3u8SettingsTypeDef = TypedDict(
    "M3u8SettingsTypeDef",
    {
        "AudioFramesPerPes": int,
        "AudioPids": str,
        "EcmPid": str,
        "NielsenId3Behavior": M3u8NielsenId3BehaviorType,
        "PatInterval": int,
        "PcrControl": M3u8PcrControlType,
        "PcrPeriod": int,
        "PcrPid": str,
        "PmtInterval": int,
        "PmtPid": str,
        "ProgramNum": int,
        "Scte35Behavior": M3u8Scte35BehaviorType,
        "Scte35Pid": str,
        "TimedMetadataBehavior": M3u8TimedMetadataBehaviorType,
        "TimedMetadataPid": str,
        "TransportStreamId": int,
        "VideoPid": str,
    },
    total=False,
)

MediaConnectFlowRequestTypeDef = TypedDict(
    "MediaConnectFlowRequestTypeDef",
    {
        "FlowArn": str,
    },
    total=False,
)

MediaConnectFlowTypeDef = TypedDict(
    "MediaConnectFlowTypeDef",
    {
        "FlowArn": str,
    },
    total=False,
)

MediaPackageGroupSettingsTypeDef = TypedDict(
    "MediaPackageGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)

MediaPackageOutputDestinationSettingsTypeDef = TypedDict(
    "MediaPackageOutputDestinationSettingsTypeDef",
    {
        "ChannelId": str,
    },
    total=False,
)

MotionGraphicsActivateScheduleActionSettingsTypeDef = TypedDict(
    "MotionGraphicsActivateScheduleActionSettingsTypeDef",
    {
        "Duration": int,
        "PasswordParam": str,
        "Url": str,
        "Username": str,
    },
    total=False,
)

_RequiredMotionGraphicsConfigurationTypeDef = TypedDict(
    "_RequiredMotionGraphicsConfigurationTypeDef",
    {
        "MotionGraphicsSettings": "MotionGraphicsSettingsTypeDef",
    },
)
_OptionalMotionGraphicsConfigurationTypeDef = TypedDict(
    "_OptionalMotionGraphicsConfigurationTypeDef",
    {
        "MotionGraphicsInsertion": MotionGraphicsInsertionType,
    },
    total=False,
)

class MotionGraphicsConfigurationTypeDef(
    _RequiredMotionGraphicsConfigurationTypeDef, _OptionalMotionGraphicsConfigurationTypeDef
):
    pass

MotionGraphicsSettingsTypeDef = TypedDict(
    "MotionGraphicsSettingsTypeDef",
    {
        "HtmlMotionGraphicsSettings": Dict[str, Any],
    },
    total=False,
)

Mp2SettingsTypeDef = TypedDict(
    "Mp2SettingsTypeDef",
    {
        "Bitrate": float,
        "CodingMode": Mp2CodingModeType,
        "SampleRate": float,
    },
    total=False,
)

Mpeg2FilterSettingsTypeDef = TypedDict(
    "Mpeg2FilterSettingsTypeDef",
    {
        "TemporalFilterSettings": "TemporalFilterSettingsTypeDef",
    },
    total=False,
)

_RequiredMpeg2SettingsTypeDef = TypedDict(
    "_RequiredMpeg2SettingsTypeDef",
    {
        "FramerateDenominator": int,
        "FramerateNumerator": int,
    },
)
_OptionalMpeg2SettingsTypeDef = TypedDict(
    "_OptionalMpeg2SettingsTypeDef",
    {
        "AdaptiveQuantization": Mpeg2AdaptiveQuantizationType,
        "AfdSignaling": AfdSignalingType,
        "ColorMetadata": Mpeg2ColorMetadataType,
        "ColorSpace": Mpeg2ColorSpaceType,
        "DisplayAspectRatio": Mpeg2DisplayRatioType,
        "FilterSettings": "Mpeg2FilterSettingsTypeDef",
        "FixedAfd": FixedAfdType,
        "GopClosedCadence": int,
        "GopNumBFrames": int,
        "GopSize": float,
        "GopSizeUnits": Mpeg2GopSizeUnitsType,
        "ScanType": Mpeg2ScanTypeType,
        "SubgopLength": Mpeg2SubGopLengthType,
        "TimecodeInsertion": Mpeg2TimecodeInsertionBehaviorType,
    },
    total=False,
)

class Mpeg2SettingsTypeDef(_RequiredMpeg2SettingsTypeDef, _OptionalMpeg2SettingsTypeDef):
    pass

_RequiredMsSmoothGroupSettingsTypeDef = TypedDict(
    "_RequiredMsSmoothGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)
_OptionalMsSmoothGroupSettingsTypeDef = TypedDict(
    "_OptionalMsSmoothGroupSettingsTypeDef",
    {
        "AcquisitionPointId": str,
        "AudioOnlyTimecodeControl": SmoothGroupAudioOnlyTimecodeControlType,
        "CertificateMode": SmoothGroupCertificateModeType,
        "ConnectionRetryInterval": int,
        "EventId": str,
        "EventIdMode": SmoothGroupEventIdModeType,
        "EventStopBehavior": SmoothGroupEventStopBehaviorType,
        "FilecacheDuration": int,
        "FragmentLength": int,
        "InputLossAction": InputLossActionForMsSmoothOutType,
        "NumRetries": int,
        "RestartDelay": int,
        "SegmentationMode": SmoothGroupSegmentationModeType,
        "SendDelayMs": int,
        "SparseTrackType": SmoothGroupSparseTrackTypeType,
        "StreamManifestBehavior": SmoothGroupStreamManifestBehaviorType,
        "TimestampOffset": str,
        "TimestampOffsetMode": SmoothGroupTimestampOffsetModeType,
    },
    total=False,
)

class MsSmoothGroupSettingsTypeDef(
    _RequiredMsSmoothGroupSettingsTypeDef, _OptionalMsSmoothGroupSettingsTypeDef
):
    pass

MsSmoothOutputSettingsTypeDef = TypedDict(
    "MsSmoothOutputSettingsTypeDef",
    {
        "H265PackagingType": MsSmoothH265PackagingTypeType,
        "NameModifier": str,
    },
    total=False,
)

MultiplexMediaConnectOutputDestinationSettingsTypeDef = TypedDict(
    "MultiplexMediaConnectOutputDestinationSettingsTypeDef",
    {
        "EntitlementArn": str,
    },
    total=False,
)

MultiplexOutputDestinationTypeDef = TypedDict(
    "MultiplexOutputDestinationTypeDef",
    {
        "MediaConnectSettings": "MultiplexMediaConnectOutputDestinationSettingsTypeDef",
    },
    total=False,
)

MultiplexOutputSettingsTypeDef = TypedDict(
    "MultiplexOutputSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)

MultiplexProgramChannelDestinationSettingsTypeDef = TypedDict(
    "MultiplexProgramChannelDestinationSettingsTypeDef",
    {
        "MultiplexId": str,
        "ProgramName": str,
    },
    total=False,
)

MultiplexProgramPacketIdentifiersMapTypeDef = TypedDict(
    "MultiplexProgramPacketIdentifiersMapTypeDef",
    {
        "AudioPids": List[int],
        "DvbSubPids": List[int],
        "DvbTeletextPid": int,
        "EtvPlatformPid": int,
        "EtvSignalPid": int,
        "KlvDataPids": List[int],
        "PcrPid": int,
        "PmtPid": int,
        "PrivateMetadataPid": int,
        "Scte27Pids": List[int],
        "Scte35Pid": int,
        "TimedMetadataPid": int,
        "VideoPid": int,
    },
    total=False,
)

MultiplexProgramPipelineDetailTypeDef = TypedDict(
    "MultiplexProgramPipelineDetailTypeDef",
    {
        "ActiveChannelPipeline": str,
        "PipelineId": str,
    },
    total=False,
)

MultiplexProgramServiceDescriptorTypeDef = TypedDict(
    "MultiplexProgramServiceDescriptorTypeDef",
    {
        "ProviderName": str,
        "ServiceName": str,
    },
)

_RequiredMultiplexProgramSettingsTypeDef = TypedDict(
    "_RequiredMultiplexProgramSettingsTypeDef",
    {
        "ProgramNumber": int,
    },
)
_OptionalMultiplexProgramSettingsTypeDef = TypedDict(
    "_OptionalMultiplexProgramSettingsTypeDef",
    {
        "PreferredChannelPipeline": PreferredChannelPipelineType,
        "ServiceDescriptor": "MultiplexProgramServiceDescriptorTypeDef",
        "VideoSettings": "MultiplexVideoSettingsTypeDef",
    },
    total=False,
)

class MultiplexProgramSettingsTypeDef(
    _RequiredMultiplexProgramSettingsTypeDef, _OptionalMultiplexProgramSettingsTypeDef
):
    pass

MultiplexProgramSummaryTypeDef = TypedDict(
    "MultiplexProgramSummaryTypeDef",
    {
        "ChannelId": str,
        "ProgramName": str,
    },
    total=False,
)

MultiplexProgramTypeDef = TypedDict(
    "MultiplexProgramTypeDef",
    {
        "ChannelId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "PacketIdentifiersMap": "MultiplexProgramPacketIdentifiersMapTypeDef",
        "PipelineDetails": List["MultiplexProgramPipelineDetailTypeDef"],
        "ProgramName": str,
    },
    total=False,
)

MultiplexSettingsSummaryTypeDef = TypedDict(
    "MultiplexSettingsSummaryTypeDef",
    {
        "TransportStreamBitrate": int,
    },
    total=False,
)

_RequiredMultiplexSettingsTypeDef = TypedDict(
    "_RequiredMultiplexSettingsTypeDef",
    {
        "TransportStreamBitrate": int,
        "TransportStreamId": int,
    },
)
_OptionalMultiplexSettingsTypeDef = TypedDict(
    "_OptionalMultiplexSettingsTypeDef",
    {
        "MaximumVideoBufferDelayMilliseconds": int,
        "TransportStreamReservedBitrate": int,
    },
    total=False,
)

class MultiplexSettingsTypeDef(
    _RequiredMultiplexSettingsTypeDef, _OptionalMultiplexSettingsTypeDef
):
    pass

MultiplexStatmuxVideoSettingsTypeDef = TypedDict(
    "MultiplexStatmuxVideoSettingsTypeDef",
    {
        "MaximumBitrate": int,
        "MinimumBitrate": int,
        "Priority": int,
    },
    total=False,
)

MultiplexSummaryTypeDef = TypedDict(
    "MultiplexSummaryTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsSummaryTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

MultiplexTypeDef = TypedDict(
    "MultiplexTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

MultiplexVideoSettingsTypeDef = TypedDict(
    "MultiplexVideoSettingsTypeDef",
    {
        "ConstantBitrate": int,
        "StatmuxSettings": "MultiplexStatmuxVideoSettingsTypeDef",
    },
    total=False,
)

NetworkInputSettingsTypeDef = TypedDict(
    "NetworkInputSettingsTypeDef",
    {
        "HlsInputSettings": "HlsInputSettingsTypeDef",
        "ServerValidation": NetworkInputServerValidationType,
    },
    total=False,
)

NielsenConfigurationTypeDef = TypedDict(
    "NielsenConfigurationTypeDef",
    {
        "DistributorId": str,
        "NielsenPcmToId3Tagging": NielsenPcmToId3TaggingStateType,
    },
    total=False,
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "Arn": str,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "FixedPrice": float,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": Literal["NO_UPFRONT"],
        "Region": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "UsagePrice": float,
    },
    total=False,
)

OutputDestinationSettingsTypeDef = TypedDict(
    "OutputDestinationSettingsTypeDef",
    {
        "PasswordParam": str,
        "StreamName": str,
        "Url": str,
        "Username": str,
    },
    total=False,
)

OutputDestinationTypeDef = TypedDict(
    "OutputDestinationTypeDef",
    {
        "Id": str,
        "MediaPackageSettings": List["MediaPackageOutputDestinationSettingsTypeDef"],
        "MultiplexSettings": "MultiplexProgramChannelDestinationSettingsTypeDef",
        "Settings": List["OutputDestinationSettingsTypeDef"],
    },
    total=False,
)

OutputGroupSettingsTypeDef = TypedDict(
    "OutputGroupSettingsTypeDef",
    {
        "ArchiveGroupSettings": "ArchiveGroupSettingsTypeDef",
        "FrameCaptureGroupSettings": "FrameCaptureGroupSettingsTypeDef",
        "HlsGroupSettings": "HlsGroupSettingsTypeDef",
        "MediaPackageGroupSettings": "MediaPackageGroupSettingsTypeDef",
        "MsSmoothGroupSettings": "MsSmoothGroupSettingsTypeDef",
        "MultiplexGroupSettings": Dict[str, Any],
        "RtmpGroupSettings": "RtmpGroupSettingsTypeDef",
        "UdpGroupSettings": "UdpGroupSettingsTypeDef",
    },
    total=False,
)

_RequiredOutputGroupTypeDef = TypedDict(
    "_RequiredOutputGroupTypeDef",
    {
        "OutputGroupSettings": "OutputGroupSettingsTypeDef",
        "Outputs": List["OutputTypeDef"],
    },
)
_OptionalOutputGroupTypeDef = TypedDict(
    "_OptionalOutputGroupTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class OutputGroupTypeDef(_RequiredOutputGroupTypeDef, _OptionalOutputGroupTypeDef):
    pass

OutputLocationRefTypeDef = TypedDict(
    "OutputLocationRefTypeDef",
    {
        "DestinationRefId": str,
    },
    total=False,
)

OutputSettingsTypeDef = TypedDict(
    "OutputSettingsTypeDef",
    {
        "ArchiveOutputSettings": "ArchiveOutputSettingsTypeDef",
        "FrameCaptureOutputSettings": "FrameCaptureOutputSettingsTypeDef",
        "HlsOutputSettings": "HlsOutputSettingsTypeDef",
        "MediaPackageOutputSettings": Dict[str, Any],
        "MsSmoothOutputSettings": "MsSmoothOutputSettingsTypeDef",
        "MultiplexOutputSettings": "MultiplexOutputSettingsTypeDef",
        "RtmpOutputSettings": "RtmpOutputSettingsTypeDef",
        "UdpOutputSettings": "UdpOutputSettingsTypeDef",
    },
    total=False,
)

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef",
    {
        "OutputSettings": "OutputSettingsTypeDef",
    },
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "AudioDescriptionNames": List[str],
        "CaptionDescriptionNames": List[str],
        "OutputName": str,
        "VideoDescriptionName": str,
    },
    total=False,
)

class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PauseStateScheduleActionSettingsTypeDef = TypedDict(
    "PauseStateScheduleActionSettingsTypeDef",
    {
        "Pipelines": List["PipelinePauseStateSettingsTypeDef"],
    },
    total=False,
)

PipelineDetailTypeDef = TypedDict(
    "PipelineDetailTypeDef",
    {
        "ActiveInputAttachmentName": str,
        "ActiveInputSwitchActionName": str,
        "ActiveMotionGraphicsActionName": str,
        "ActiveMotionGraphicsUri": str,
        "PipelineId": str,
    },
    total=False,
)

PipelinePauseStateSettingsTypeDef = TypedDict(
    "PipelinePauseStateSettingsTypeDef",
    {
        "PipelineId": PipelineIdType,
    },
)

_RequiredPurchaseOfferingRequestRequestTypeDef = TypedDict(
    "_RequiredPurchaseOfferingRequestRequestTypeDef",
    {
        "Count": int,
        "OfferingId": str,
    },
)
_OptionalPurchaseOfferingRequestRequestTypeDef = TypedDict(
    "_OptionalPurchaseOfferingRequestRequestTypeDef",
    {
        "Name": str,
        "RequestId": str,
        "Start": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class PurchaseOfferingRequestRequestTypeDef(
    _RequiredPurchaseOfferingRequestRequestTypeDef, _OptionalPurchaseOfferingRequestRequestTypeDef
):
    pass

PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectInputDeviceTransferRequestRequestTypeDef = TypedDict(
    "RejectInputDeviceTransferRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

_RequiredRemixSettingsTypeDef = TypedDict(
    "_RequiredRemixSettingsTypeDef",
    {
        "ChannelMappings": List["AudioChannelMappingTypeDef"],
    },
)
_OptionalRemixSettingsTypeDef = TypedDict(
    "_OptionalRemixSettingsTypeDef",
    {
        "ChannelsIn": int,
        "ChannelsOut": int,
    },
    total=False,
)

class RemixSettingsTypeDef(_RequiredRemixSettingsTypeDef, _OptionalRemixSettingsTypeDef):
    pass

ReservationResourceSpecificationTypeDef = TypedDict(
    "ReservationResourceSpecificationTypeDef",
    {
        "ChannelClass": ChannelClassType,
        "Codec": ReservationCodecType,
        "MaximumBitrate": ReservationMaximumBitrateType,
        "MaximumFramerate": ReservationMaximumFramerateType,
        "Resolution": ReservationResolutionType,
        "ResourceType": ReservationResourceTypeType,
        "SpecialFeature": ReservationSpecialFeatureType,
        "VideoQuality": ReservationVideoQualityType,
    },
    total=False,
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "Arn": str,
        "Count": int,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "FixedPrice": float,
        "Name": str,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": Literal["NO_UPFRONT"],
        "Region": str,
        "ReservationId": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "Start": str,
        "State": ReservationStateType,
        "Tags": Dict[str, str],
        "UsagePrice": float,
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

RtmpGroupSettingsTypeDef = TypedDict(
    "RtmpGroupSettingsTypeDef",
    {
        "AdMarkers": List[Literal["ON_CUE_POINT_SCTE35"]],
        "AuthenticationScheme": AuthenticationSchemeType,
        "CacheFullBehavior": RtmpCacheFullBehaviorType,
        "CacheLength": int,
        "CaptionData": RtmpCaptionDataType,
        "InputLossAction": InputLossActionForRtmpOutType,
        "RestartDelay": int,
    },
    total=False,
)

_RequiredRtmpOutputSettingsTypeDef = TypedDict(
    "_RequiredRtmpOutputSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)
_OptionalRtmpOutputSettingsTypeDef = TypedDict(
    "_OptionalRtmpOutputSettingsTypeDef",
    {
        "CertificateMode": RtmpOutputCertificateModeType,
        "ConnectionRetryInterval": int,
        "NumRetries": int,
    },
    total=False,
)

class RtmpOutputSettingsTypeDef(
    _RequiredRtmpOutputSettingsTypeDef, _OptionalRtmpOutputSettingsTypeDef
):
    pass

ScheduleActionSettingsTypeDef = TypedDict(
    "ScheduleActionSettingsTypeDef",
    {
        "HlsId3SegmentTaggingSettings": "HlsId3SegmentTaggingScheduleActionSettingsTypeDef",
        "HlsTimedMetadataSettings": "HlsTimedMetadataScheduleActionSettingsTypeDef",
        "InputPrepareSettings": "InputPrepareScheduleActionSettingsTypeDef",
        "InputSwitchSettings": "InputSwitchScheduleActionSettingsTypeDef",
        "MotionGraphicsImageActivateSettings": "MotionGraphicsActivateScheduleActionSettingsTypeDef",
        "MotionGraphicsImageDeactivateSettings": Dict[str, Any],
        "PauseStateSettings": "PauseStateScheduleActionSettingsTypeDef",
        "Scte35ReturnToNetworkSettings": "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
        "Scte35SpliceInsertSettings": "Scte35SpliceInsertScheduleActionSettingsTypeDef",
        "Scte35TimeSignalSettings": "Scte35TimeSignalScheduleActionSettingsTypeDef",
        "StaticImageActivateSettings": "StaticImageActivateScheduleActionSettingsTypeDef",
        "StaticImageDeactivateSettings": "StaticImageDeactivateScheduleActionSettingsTypeDef",
    },
    total=False,
)

ScheduleActionStartSettingsTypeDef = TypedDict(
    "ScheduleActionStartSettingsTypeDef",
    {
        "FixedModeScheduleActionStartSettings": "FixedModeScheduleActionStartSettingsTypeDef",
        "FollowModeScheduleActionStartSettings": "FollowModeScheduleActionStartSettingsTypeDef",
        "ImmediateModeScheduleActionStartSettings": Dict[str, Any],
    },
    total=False,
)

ScheduleActionTypeDef = TypedDict(
    "ScheduleActionTypeDef",
    {
        "ActionName": str,
        "ScheduleActionSettings": "ScheduleActionSettingsTypeDef",
        "ScheduleActionStartSettings": "ScheduleActionStartSettingsTypeDef",
    },
)

Scte20SourceSettingsTypeDef = TypedDict(
    "Scte20SourceSettingsTypeDef",
    {
        "Convert608To708": Scte20Convert608To708Type,
        "Source608ChannelNumber": int,
    },
    total=False,
)

Scte27SourceSettingsTypeDef = TypedDict(
    "Scte27SourceSettingsTypeDef",
    {
        "OcrLanguage": Scte27OcrLanguageType,
        "Pid": int,
    },
    total=False,
)

Scte35DeliveryRestrictionsTypeDef = TypedDict(
    "Scte35DeliveryRestrictionsTypeDef",
    {
        "ArchiveAllowedFlag": Scte35ArchiveAllowedFlagType,
        "DeviceRestrictions": Scte35DeviceRestrictionsType,
        "NoRegionalBlackoutFlag": Scte35NoRegionalBlackoutFlagType,
        "WebDeliveryAllowedFlag": Scte35WebDeliveryAllowedFlagType,
    },
)

Scte35DescriptorSettingsTypeDef = TypedDict(
    "Scte35DescriptorSettingsTypeDef",
    {
        "SegmentationDescriptorScte35DescriptorSettings": "Scte35SegmentationDescriptorTypeDef",
    },
)

Scte35DescriptorTypeDef = TypedDict(
    "Scte35DescriptorTypeDef",
    {
        "Scte35DescriptorSettings": "Scte35DescriptorSettingsTypeDef",
    },
)

Scte35ReturnToNetworkScheduleActionSettingsTypeDef = TypedDict(
    "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
    {
        "SpliceEventId": int,
    },
)

_RequiredScte35SegmentationDescriptorTypeDef = TypedDict(
    "_RequiredScte35SegmentationDescriptorTypeDef",
    {
        "SegmentationCancelIndicator": Scte35SegmentationCancelIndicatorType,
        "SegmentationEventId": int,
    },
)
_OptionalScte35SegmentationDescriptorTypeDef = TypedDict(
    "_OptionalScte35SegmentationDescriptorTypeDef",
    {
        "DeliveryRestrictions": "Scte35DeliveryRestrictionsTypeDef",
        "SegmentNum": int,
        "SegmentationDuration": int,
        "SegmentationTypeId": int,
        "SegmentationUpid": str,
        "SegmentationUpidType": int,
        "SegmentsExpected": int,
        "SubSegmentNum": int,
        "SubSegmentsExpected": int,
    },
    total=False,
)

class Scte35SegmentationDescriptorTypeDef(
    _RequiredScte35SegmentationDescriptorTypeDef, _OptionalScte35SegmentationDescriptorTypeDef
):
    pass

_RequiredScte35SpliceInsertScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredScte35SpliceInsertScheduleActionSettingsTypeDef",
    {
        "SpliceEventId": int,
    },
)
_OptionalScte35SpliceInsertScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalScte35SpliceInsertScheduleActionSettingsTypeDef",
    {
        "Duration": int,
    },
    total=False,
)

class Scte35SpliceInsertScheduleActionSettingsTypeDef(
    _RequiredScte35SpliceInsertScheduleActionSettingsTypeDef,
    _OptionalScte35SpliceInsertScheduleActionSettingsTypeDef,
):
    pass

Scte35SpliceInsertTypeDef = TypedDict(
    "Scte35SpliceInsertTypeDef",
    {
        "AdAvailOffset": int,
        "NoRegionalBlackoutFlag": Scte35SpliceInsertNoRegionalBlackoutBehaviorType,
        "WebDeliveryAllowedFlag": Scte35SpliceInsertWebDeliveryAllowedBehaviorType,
    },
    total=False,
)

Scte35TimeSignalAposTypeDef = TypedDict(
    "Scte35TimeSignalAposTypeDef",
    {
        "AdAvailOffset": int,
        "NoRegionalBlackoutFlag": Scte35AposNoRegionalBlackoutBehaviorType,
        "WebDeliveryAllowedFlag": Scte35AposWebDeliveryAllowedBehaviorType,
    },
    total=False,
)

Scte35TimeSignalScheduleActionSettingsTypeDef = TypedDict(
    "Scte35TimeSignalScheduleActionSettingsTypeDef",
    {
        "Scte35Descriptors": List["Scte35DescriptorTypeDef"],
    },
)

_RequiredStandardHlsSettingsTypeDef = TypedDict(
    "_RequiredStandardHlsSettingsTypeDef",
    {
        "M3u8Settings": "M3u8SettingsTypeDef",
    },
)
_OptionalStandardHlsSettingsTypeDef = TypedDict(
    "_OptionalStandardHlsSettingsTypeDef",
    {
        "AudioRenditionSets": str,
    },
    total=False,
)

class StandardHlsSettingsTypeDef(
    _RequiredStandardHlsSettingsTypeDef, _OptionalStandardHlsSettingsTypeDef
):
    pass

StartChannelRequestRequestTypeDef = TypedDict(
    "StartChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

StartChannelResponseTypeDef = TypedDict(
    "StartChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMultiplexRequestRequestTypeDef = TypedDict(
    "StartMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)

StartMultiplexResponseTypeDef = TypedDict(
    "StartMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTimecodeTypeDef = TypedDict(
    "StartTimecodeTypeDef",
    {
        "Timecode": str,
    },
    total=False,
)

_RequiredStaticImageActivateScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredStaticImageActivateScheduleActionSettingsTypeDef",
    {
        "Image": "InputLocationTypeDef",
    },
)
_OptionalStaticImageActivateScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalStaticImageActivateScheduleActionSettingsTypeDef",
    {
        "Duration": int,
        "FadeIn": int,
        "FadeOut": int,
        "Height": int,
        "ImageX": int,
        "ImageY": int,
        "Layer": int,
        "Opacity": int,
        "Width": int,
    },
    total=False,
)

class StaticImageActivateScheduleActionSettingsTypeDef(
    _RequiredStaticImageActivateScheduleActionSettingsTypeDef,
    _OptionalStaticImageActivateScheduleActionSettingsTypeDef,
):
    pass

StaticImageDeactivateScheduleActionSettingsTypeDef = TypedDict(
    "StaticImageDeactivateScheduleActionSettingsTypeDef",
    {
        "FadeOut": int,
        "Layer": int,
    },
    total=False,
)

_RequiredStaticKeySettingsTypeDef = TypedDict(
    "_RequiredStaticKeySettingsTypeDef",
    {
        "StaticKeyValue": str,
    },
)
_OptionalStaticKeySettingsTypeDef = TypedDict(
    "_OptionalStaticKeySettingsTypeDef",
    {
        "KeyProviderServer": "InputLocationTypeDef",
    },
    total=False,
)

class StaticKeySettingsTypeDef(
    _RequiredStaticKeySettingsTypeDef, _OptionalStaticKeySettingsTypeDef
):
    pass

StopChannelRequestRequestTypeDef = TypedDict(
    "StopChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)

StopChannelResponseTypeDef = TypedDict(
    "StopChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClassType,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelStateType,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopMultiplexRequestRequestTypeDef = TypedDict(
    "StopMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)

StopMultiplexResponseTypeDef = TypedDict(
    "StopMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopTimecodeTypeDef = TypedDict(
    "StopTimecodeTypeDef",
    {
        "LastFrameClippingBehavior": LastFrameClippingBehaviorType,
        "Timecode": str,
    },
    total=False,
)

TeletextSourceSettingsTypeDef = TypedDict(
    "TeletextSourceSettingsTypeDef",
    {
        "OutputRectangle": "CaptionRectangleTypeDef",
        "PageNumber": str,
    },
    total=False,
)

TemporalFilterSettingsTypeDef = TypedDict(
    "TemporalFilterSettingsTypeDef",
    {
        "PostFilterSharpening": TemporalFilterPostFilterSharpeningType,
        "Strength": TemporalFilterStrengthType,
    },
    total=False,
)

_RequiredTimecodeConfigTypeDef = TypedDict(
    "_RequiredTimecodeConfigTypeDef",
    {
        "Source": TimecodeConfigSourceType,
    },
)
_OptionalTimecodeConfigTypeDef = TypedDict(
    "_OptionalTimecodeConfigTypeDef",
    {
        "SyncThreshold": int,
    },
    total=False,
)

class TimecodeConfigTypeDef(_RequiredTimecodeConfigTypeDef, _OptionalTimecodeConfigTypeDef):
    pass

_RequiredTransferInputDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredTransferInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)
_OptionalTransferInputDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalTransferInputDeviceRequestRequestTypeDef",
    {
        "TargetCustomerId": str,
        "TargetRegion": str,
        "TransferMessage": str,
    },
    total=False,
)

class TransferInputDeviceRequestRequestTypeDef(
    _RequiredTransferInputDeviceRequestRequestTypeDef,
    _OptionalTransferInputDeviceRequestRequestTypeDef,
):
    pass

TransferringInputDeviceSummaryTypeDef = TypedDict(
    "TransferringInputDeviceSummaryTypeDef",
    {
        "Id": str,
        "Message": str,
        "TargetCustomerId": str,
        "TransferType": InputDeviceTransferTypeType,
    },
    total=False,
)

TtmlDestinationSettingsTypeDef = TypedDict(
    "TtmlDestinationSettingsTypeDef",
    {
        "StyleControl": TtmlDestinationStyleControlType,
    },
    total=False,
)

UdpContainerSettingsTypeDef = TypedDict(
    "UdpContainerSettingsTypeDef",
    {
        "M2tsSettings": "M2tsSettingsTypeDef",
    },
    total=False,
)

UdpGroupSettingsTypeDef = TypedDict(
    "UdpGroupSettingsTypeDef",
    {
        "InputLossAction": InputLossActionForUdpOutType,
        "TimedMetadataId3Frame": UdpTimedMetadataId3FrameType,
        "TimedMetadataId3Period": int,
    },
    total=False,
)

_RequiredUdpOutputSettingsTypeDef = TypedDict(
    "_RequiredUdpOutputSettingsTypeDef",
    {
        "ContainerSettings": "UdpContainerSettingsTypeDef",
        "Destination": "OutputLocationRefTypeDef",
    },
)
_OptionalUdpOutputSettingsTypeDef = TypedDict(
    "_OptionalUdpOutputSettingsTypeDef",
    {
        "BufferMsec": int,
        "FecOutputSettings": "FecOutputSettingsTypeDef",
    },
    total=False,
)

class UdpOutputSettingsTypeDef(
    _RequiredUdpOutputSettingsTypeDef, _OptionalUdpOutputSettingsTypeDef
):
    pass

_RequiredUpdateChannelClassRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelClassRequestRequestTypeDef",
    {
        "ChannelClass": ChannelClassType,
        "ChannelId": str,
    },
)
_OptionalUpdateChannelClassRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelClassRequestRequestTypeDef",
    {
        "Destinations": List["OutputDestinationTypeDef"],
    },
    total=False,
)

class UpdateChannelClassRequestRequestTypeDef(
    _RequiredUpdateChannelClassRequestRequestTypeDef,
    _OptionalUpdateChannelClassRequestRequestTypeDef,
):
    pass

UpdateChannelClassResponseTypeDef = TypedDict(
    "UpdateChannelClassResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "Destinations": List["OutputDestinationTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevelType,
        "Name": str,
        "RoleArn": str,
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
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInputDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)
_OptionalUpdateInputDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInputDeviceRequestRequestTypeDef",
    {
        "HdDeviceSettings": "InputDeviceConfigurableSettingsTypeDef",
        "Name": str,
        "UhdDeviceSettings": "InputDeviceConfigurableSettingsTypeDef",
    },
    total=False,
)

class UpdateInputDeviceRequestRequestTypeDef(
    _RequiredUpdateInputDeviceRequestRequestTypeDef, _OptionalUpdateInputDeviceRequestRequestTypeDef
):
    pass

UpdateInputDeviceResponseTypeDef = TypedDict(
    "UpdateInputDeviceResponseTypeDef",
    {
        "Arn": str,
        "ConnectionState": InputDeviceConnectionStateType,
        "DeviceSettingsSyncState": DeviceSettingsSyncStateType,
        "DeviceUpdateStatus": DeviceUpdateStatusType,
        "HdDeviceSettings": "InputDeviceHdSettingsTypeDef",
        "Id": str,
        "MacAddress": str,
        "Name": str,
        "NetworkSettings": "InputDeviceNetworkSettingsTypeDef",
        "SerialNumber": str,
        "Type": Literal["HD"],
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInputRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInputRequestRequestTypeDef",
    {
        "InputId": str,
    },
)
_OptionalUpdateInputRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInputRequestRequestTypeDef",
    {
        "Destinations": List["InputDestinationRequestTypeDef"],
        "InputDevices": List["InputDeviceRequestTypeDef"],
        "InputSecurityGroups": List[str],
        "MediaConnectFlows": List["MediaConnectFlowRequestTypeDef"],
        "Name": str,
        "RoleArn": str,
        "Sources": List["InputSourceRequestTypeDef"],
    },
    total=False,
)

class UpdateInputRequestRequestTypeDef(
    _RequiredUpdateInputRequestRequestTypeDef, _OptionalUpdateInputRequestRequestTypeDef
):
    pass

UpdateInputResponseTypeDef = TypedDict(
    "UpdateInputResponseTypeDef",
    {
        "Input": "InputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInputSecurityGroupRequestRequestTypeDef",
    {
        "InputSecurityGroupId": str,
    },
)
_OptionalUpdateInputSecurityGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInputSecurityGroupRequestRequestTypeDef",
    {
        "Tags": Dict[str, str],
        "WhitelistRules": List["InputWhitelistRuleCidrTypeDef"],
    },
    total=False,
)

class UpdateInputSecurityGroupRequestRequestTypeDef(
    _RequiredUpdateInputSecurityGroupRequestRequestTypeDef,
    _OptionalUpdateInputSecurityGroupRequestRequestTypeDef,
):
    pass

UpdateInputSecurityGroupResponseTypeDef = TypedDict(
    "UpdateInputSecurityGroupResponseTypeDef",
    {
        "SecurityGroup": "InputSecurityGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMultiplexProgramRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexId": str,
        "ProgramName": str,
    },
)
_OptionalUpdateMultiplexProgramRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMultiplexProgramRequestRequestTypeDef",
    {
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
    },
    total=False,
)

class UpdateMultiplexProgramRequestRequestTypeDef(
    _RequiredUpdateMultiplexProgramRequestRequestTypeDef,
    _OptionalUpdateMultiplexProgramRequestRequestTypeDef,
):
    pass

UpdateMultiplexProgramResponseTypeDef = TypedDict(
    "UpdateMultiplexProgramResponseTypeDef",
    {
        "MultiplexProgram": "MultiplexProgramTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMultiplexRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMultiplexRequestRequestTypeDef",
    {
        "MultiplexId": str,
    },
)
_OptionalUpdateMultiplexRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMultiplexRequestRequestTypeDef",
    {
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
    },
    total=False,
)

class UpdateMultiplexRequestRequestTypeDef(
    _RequiredUpdateMultiplexRequestRequestTypeDef, _OptionalUpdateMultiplexRequestRequestTypeDef
):
    pass

UpdateMultiplexResponseTypeDef = TypedDict(
    "UpdateMultiplexResponseTypeDef",
    {
        "Multiplex": "MultiplexTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateReservationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateReservationRequestRequestTypeDef",
    {
        "ReservationId": str,
    },
)
_OptionalUpdateReservationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateReservationRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class UpdateReservationRequestRequestTypeDef(
    _RequiredUpdateReservationRequestRequestTypeDef, _OptionalUpdateReservationRequestRequestTypeDef
):
    pass

UpdateReservationResponseTypeDef = TypedDict(
    "UpdateReservationResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VideoBlackFailoverSettingsTypeDef = TypedDict(
    "VideoBlackFailoverSettingsTypeDef",
    {
        "BlackDetectThreshold": float,
        "VideoBlackThresholdMsec": int,
    },
    total=False,
)

VideoCodecSettingsTypeDef = TypedDict(
    "VideoCodecSettingsTypeDef",
    {
        "FrameCaptureSettings": "FrameCaptureSettingsTypeDef",
        "H264Settings": "H264SettingsTypeDef",
        "H265Settings": "H265SettingsTypeDef",
        "Mpeg2Settings": "Mpeg2SettingsTypeDef",
    },
    total=False,
)

_RequiredVideoDescriptionTypeDef = TypedDict(
    "_RequiredVideoDescriptionTypeDef",
    {
        "Name": str,
    },
)
_OptionalVideoDescriptionTypeDef = TypedDict(
    "_OptionalVideoDescriptionTypeDef",
    {
        "CodecSettings": "VideoCodecSettingsTypeDef",
        "Height": int,
        "RespondToAfd": VideoDescriptionRespondToAfdType,
        "ScalingBehavior": VideoDescriptionScalingBehaviorType,
        "Sharpness": int,
        "Width": int,
    },
    total=False,
)

class VideoDescriptionTypeDef(_RequiredVideoDescriptionTypeDef, _OptionalVideoDescriptionTypeDef):
    pass

VideoSelectorColorSpaceSettingsTypeDef = TypedDict(
    "VideoSelectorColorSpaceSettingsTypeDef",
    {
        "Hdr10Settings": "Hdr10SettingsTypeDef",
    },
    total=False,
)

VideoSelectorPidTypeDef = TypedDict(
    "VideoSelectorPidTypeDef",
    {
        "Pid": int,
    },
    total=False,
)

VideoSelectorProgramIdTypeDef = TypedDict(
    "VideoSelectorProgramIdTypeDef",
    {
        "ProgramId": int,
    },
    total=False,
)

VideoSelectorSettingsTypeDef = TypedDict(
    "VideoSelectorSettingsTypeDef",
    {
        "VideoSelectorPid": "VideoSelectorPidTypeDef",
        "VideoSelectorProgramId": "VideoSelectorProgramIdTypeDef",
    },
    total=False,
)

VideoSelectorTypeDef = TypedDict(
    "VideoSelectorTypeDef",
    {
        "ColorSpace": VideoSelectorColorSpaceType,
        "ColorSpaceSettings": "VideoSelectorColorSpaceSettingsTypeDef",
        "ColorSpaceUsage": VideoSelectorColorSpaceUsageType,
        "SelectorSettings": "VideoSelectorSettingsTypeDef",
    },
    total=False,
)

VpcOutputSettingsDescriptionTypeDef = TypedDict(
    "VpcOutputSettingsDescriptionTypeDef",
    {
        "AvailabilityZones": List[str],
        "NetworkInterfaceIds": List[str],
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
    },
    total=False,
)

_RequiredVpcOutputSettingsTypeDef = TypedDict(
    "_RequiredVpcOutputSettingsTypeDef",
    {
        "SubnetIds": List[str],
    },
)
_OptionalVpcOutputSettingsTypeDef = TypedDict(
    "_OptionalVpcOutputSettingsTypeDef",
    {
        "PublicAddressAllocationIds": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

class VpcOutputSettingsTypeDef(
    _RequiredVpcOutputSettingsTypeDef, _OptionalVpcOutputSettingsTypeDef
):
    pass

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

WavSettingsTypeDef = TypedDict(
    "WavSettingsTypeDef",
    {
        "BitDepth": float,
        "CodingMode": WavCodingModeType,
        "SampleRate": float,
    },
    total=False,
)

WebvttDestinationSettingsTypeDef = TypedDict(
    "WebvttDestinationSettingsTypeDef",
    {
        "StyleControl": WebvttDestinationStyleControlType,
    },
    total=False,
)
