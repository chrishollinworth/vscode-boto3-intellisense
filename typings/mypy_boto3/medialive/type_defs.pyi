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
    Ac3AttenuationControlType,
    Ac3BitstreamModeType,
    Ac3CodingModeType,
    Ac3DrcProfileType,
    Ac3LfeFilterType,
    Ac3MetadataControlType,
    AccessibilityTypeType,
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
    ChannelPipelineIdToRestartType,
    ChannelStateType,
    CloudWatchAlarmTemplateComparisonOperatorType,
    CloudWatchAlarmTemplateStatisticType,
    CloudWatchAlarmTemplateTargetResourceTypeType,
    CloudWatchAlarmTemplateTreatMissingDataType,
    CmafIngestSegmentLengthUnitsType,
    CmafNielsenId3BehaviorType,
    ColorSpaceType,
    DashRoleAudioType,
    DashRoleCaptionType,
    DeviceSettingsSyncStateType,
    DeviceUpdateStatusType,
    DolbyEProgramSelectionType,
    DvbDashAccessibilityType,
    DvbSdtOutputSdtType,
    DvbSubDestinationAlignmentType,
    DvbSubDestinationBackgroundColorType,
    DvbSubDestinationFontColorType,
    DvbSubDestinationOutlineColorType,
    DvbSubDestinationShadowColorType,
    DvbSubDestinationTeletextGridControlType,
    DvbSubOcrLanguageType,
    Eac3AtmosCodingModeType,
    Eac3AtmosDrcLineType,
    Eac3AtmosDrcRfType,
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
    EventBridgeRuleTemplateEventTypeType,
    FeatureActivationsInputPrepareScheduleActionsType,
    FeatureActivationsOutputStaticImageOverlayScheduleActionsType,
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
    H265MvOverPictureBoundariesType,
    H265MvTemporalPredictorType,
    H265ProfileType,
    H265RateControlModeType,
    H265ScanTypeType,
    H265SceneChangeDetectType,
    H265TierType,
    H265TilePaddingType,
    H265TimecodeInsertionBehaviorType,
    H265TreeblockSizeType,
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
    HlsProgramDateTimeClockType,
    HlsProgramDateTimeType,
    HlsRedundantManifestType,
    HlsScte35SourceTypeType,
    HlsSegmentationModeType,
    HlsStreamInfResolutionType,
    HlsTimedMetadataId3FrameType,
    HlsTsFileModeType,
    HlsWebdavHttpTransferModeType,
    IFrameOnlyPlaylistTypeType,
    IncludeFillerNalUnitsType,
    InputClassType,
    InputCodecType,
    InputDeblockFilterType,
    InputDenoiseFilterType,
    InputDeviceActiveInputType,
    InputDeviceCodecType,
    InputDeviceConfigurableAudioChannelPairProfileType,
    InputDeviceConfiguredInputType,
    InputDeviceConnectionStateType,
    InputDeviceIpSchemeType,
    InputDeviceOutputTypeType,
    InputDeviceScanTypeType,
    InputDeviceStateType,
    InputDeviceTransferTypeType,
    InputDeviceTypeType,
    InputDeviceUhdAudioChannelPairProfileType,
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
    M3u8KlvBehaviorType,
    M3u8NielsenId3BehaviorType,
    M3u8PcrControlType,
    M3u8Scte35BehaviorType,
    M3u8TimedMetadataBehaviorType,
    MaintenanceDayType,
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
    NielsenWatermarksCbetStepasideType,
    NielsenWatermarksDistributionTypesType,
    NielsenWatermarkTimezonesType,
    PipelineIdType,
    PreferredChannelPipelineType,
    RebootInputDeviceForceType,
    ReservationAutomaticRenewalType,
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
    Scte35InputModeType,
    Scte35NoRegionalBlackoutFlagType,
    Scte35SegmentationCancelIndicatorType,
    Scte35SegmentationScopeType,
    Scte35SpliceInsertNoRegionalBlackoutBehaviorType,
    Scte35SpliceInsertWebDeliveryAllowedBehaviorType,
    Scte35TypeType,
    Scte35WebDeliveryAllowedFlagType,
    SignalMapMonitorDeploymentStatusType,
    SignalMapStatusType,
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
    ThumbnailStateType,
    ThumbnailTypeType,
    TimecodeBurninFontSizeType,
    TimecodeBurninPositionType,
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
    "AccountConfigurationTypeDef",
    "AncillarySourceSettingsTypeDef",
    "ArchiveCdnSettingsTypeDef",
    "ArchiveContainerSettingsTypeDef",
    "ArchiveGroupSettingsTypeDef",
    "ArchiveOutputSettingsTypeDef",
    "ArchiveS3SettingsTypeDef",
    "AudioChannelMappingTypeDef",
    "AudioCodecSettingsTypeDef",
    "AudioDescriptionTypeDef",
    "AudioDolbyEDecodeTypeDef",
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
    "AudioWatermarkSettingsTypeDef",
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
    "ClaimDeviceRequestRequestTypeDef",
    "CloudWatchAlarmTemplateGroupSummaryTypeDef",
    "CloudWatchAlarmTemplateSummaryTypeDef",
    "CmafIngestGroupSettingsTypeDef",
    "CmafIngestOutputSettingsTypeDef",
    "ColorCorrectionSettingsTypeDef",
    "ColorCorrectionTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    "CreateCloudWatchAlarmTemplateGroupResponseTypeDef",
    "CreateCloudWatchAlarmTemplateRequestRequestTypeDef",
    "CreateCloudWatchAlarmTemplateResponseTypeDef",
    "CreateEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    "CreateEventBridgeRuleTemplateGroupResponseTypeDef",
    "CreateEventBridgeRuleTemplateRequestRequestTypeDef",
    "CreateEventBridgeRuleTemplateResponseTypeDef",
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
    "CreateSignalMapRequestRequestTypeDef",
    "CreateSignalMapResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteChannelResponseTypeDef",
    "DeleteCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    "DeleteCloudWatchAlarmTemplateRequestRequestTypeDef",
    "DeleteEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    "DeleteEventBridgeRuleTemplateRequestRequestTypeDef",
    "DeleteInputRequestRequestTypeDef",
    "DeleteInputSecurityGroupRequestRequestTypeDef",
    "DeleteMultiplexProgramRequestRequestTypeDef",
    "DeleteMultiplexProgramResponseTypeDef",
    "DeleteMultiplexRequestRequestTypeDef",
    "DeleteMultiplexResponseTypeDef",
    "DeleteReservationRequestRequestTypeDef",
    "DeleteReservationResponseTypeDef",
    "DeleteScheduleRequestRequestTypeDef",
    "DeleteSignalMapRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DescribeAccountConfigurationResponseTypeDef",
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
    "DescribeThumbnailsRequestRequestTypeDef",
    "DescribeThumbnailsResponseTypeDef",
    "DvbNitSettingsTypeDef",
    "DvbSdtSettingsTypeDef",
    "DvbSubDestinationSettingsTypeDef",
    "DvbSubSourceSettingsTypeDef",
    "DvbTdtSettingsTypeDef",
    "Eac3AtmosSettingsTypeDef",
    "Eac3SettingsTypeDef",
    "EbuTtDDestinationSettingsTypeDef",
    "EmbeddedSourceSettingsTypeDef",
    "EncoderSettingsTypeDef",
    "EpochLockingSettingsTypeDef",
    "EsamTypeDef",
    "EventBridgeRuleTemplateGroupSummaryTypeDef",
    "EventBridgeRuleTemplateSummaryTypeDef",
    "EventBridgeRuleTemplateTargetTypeDef",
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
    "GetCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    "GetCloudWatchAlarmTemplateGroupResponseTypeDef",
    "GetCloudWatchAlarmTemplateRequestRequestTypeDef",
    "GetCloudWatchAlarmTemplateResponseTypeDef",
    "GetEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    "GetEventBridgeRuleTemplateGroupResponseTypeDef",
    "GetEventBridgeRuleTemplateRequestRequestTypeDef",
    "GetEventBridgeRuleTemplateResponseTypeDef",
    "GetSignalMapRequestRequestTypeDef",
    "GetSignalMapResponseTypeDef",
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
    "InputDeviceConfigurableAudioChannelPairConfigTypeDef",
    "InputDeviceConfigurableSettingsTypeDef",
    "InputDeviceHdSettingsTypeDef",
    "InputDeviceMediaConnectConfigurableSettingsTypeDef",
    "InputDeviceMediaConnectSettingsTypeDef",
    "InputDeviceNetworkSettingsTypeDef",
    "InputDeviceRequestTypeDef",
    "InputDeviceSettingsTypeDef",
    "InputDeviceSummaryTypeDef",
    "InputDeviceUhdAudioChannelPairConfigTypeDef",
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
    "ListCloudWatchAlarmTemplateGroupsRequestRequestTypeDef",
    "ListCloudWatchAlarmTemplateGroupsResponseTypeDef",
    "ListCloudWatchAlarmTemplatesRequestRequestTypeDef",
    "ListCloudWatchAlarmTemplatesResponseTypeDef",
    "ListEventBridgeRuleTemplateGroupsRequestRequestTypeDef",
    "ListEventBridgeRuleTemplateGroupsResponseTypeDef",
    "ListEventBridgeRuleTemplatesRequestRequestTypeDef",
    "ListEventBridgeRuleTemplatesResponseTypeDef",
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
    "ListSignalMapsRequestRequestTypeDef",
    "ListSignalMapsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "M2tsSettingsTypeDef",
    "M3u8SettingsTypeDef",
    "MaintenanceCreateSettingsTypeDef",
    "MaintenanceStatusTypeDef",
    "MaintenanceUpdateSettingsTypeDef",
    "MediaConnectFlowRequestTypeDef",
    "MediaConnectFlowTypeDef",
    "MediaPackageGroupSettingsTypeDef",
    "MediaPackageOutputDestinationSettingsTypeDef",
    "MediaResourceNeighborTypeDef",
    "MediaResourceTypeDef",
    "MonitorDeploymentTypeDef",
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
    "NielsenCBETTypeDef",
    "NielsenConfigurationTypeDef",
    "NielsenNaesIiNwTypeDef",
    "NielsenWatermarksSettingsTypeDef",
    "OfferingTypeDef",
    "OutputDestinationSettingsTypeDef",
    "OutputDestinationTypeDef",
    "OutputGroupSettingsTypeDef",
    "OutputGroupTypeDef",
    "OutputLocationRefTypeDef",
    "OutputLockingSettingsTypeDef",
    "OutputSettingsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PauseStateScheduleActionSettingsTypeDef",
    "PipelineDetailTypeDef",
    "PipelinePauseStateSettingsTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RebootInputDeviceRequestRequestTypeDef",
    "RejectInputDeviceTransferRequestRequestTypeDef",
    "RemixSettingsTypeDef",
    "RenewalSettingsTypeDef",
    "ReservationResourceSpecificationTypeDef",
    "ReservationTypeDef",
    "ResponseMetadataTypeDef",
    "RestartChannelPipelinesRequestRequestTypeDef",
    "RestartChannelPipelinesResponseTypeDef",
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
    "Scte35InputScheduleActionSettingsTypeDef",
    "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
    "Scte35SegmentationDescriptorTypeDef",
    "Scte35SpliceInsertScheduleActionSettingsTypeDef",
    "Scte35SpliceInsertTypeDef",
    "Scte35TimeSignalAposTypeDef",
    "Scte35TimeSignalScheduleActionSettingsTypeDef",
    "SignalMapSummaryTypeDef",
    "StandardHlsSettingsTypeDef",
    "StartChannelRequestRequestTypeDef",
    "StartChannelResponseTypeDef",
    "StartDeleteMonitorDeploymentRequestRequestTypeDef",
    "StartDeleteMonitorDeploymentResponseTypeDef",
    "StartInputDeviceMaintenanceWindowRequestRequestTypeDef",
    "StartInputDeviceRequestRequestTypeDef",
    "StartMonitorDeploymentRequestRequestTypeDef",
    "StartMonitorDeploymentResponseTypeDef",
    "StartMultiplexRequestRequestTypeDef",
    "StartMultiplexResponseTypeDef",
    "StartTimecodeTypeDef",
    "StartUpdateSignalMapRequestRequestTypeDef",
    "StartUpdateSignalMapResponseTypeDef",
    "StaticImageActivateScheduleActionSettingsTypeDef",
    "StaticImageDeactivateScheduleActionSettingsTypeDef",
    "StaticImageOutputActivateScheduleActionSettingsTypeDef",
    "StaticImageOutputDeactivateScheduleActionSettingsTypeDef",
    "StaticKeySettingsTypeDef",
    "StopChannelRequestRequestTypeDef",
    "StopChannelResponseTypeDef",
    "StopInputDeviceRequestRequestTypeDef",
    "StopMultiplexRequestRequestTypeDef",
    "StopMultiplexResponseTypeDef",
    "StopTimecodeTypeDef",
    "SuccessfulMonitorDeploymentTypeDef",
    "TeletextSourceSettingsTypeDef",
    "TemporalFilterSettingsTypeDef",
    "ThumbnailConfigurationTypeDef",
    "ThumbnailDetailTypeDef",
    "ThumbnailTypeDef",
    "TimecodeBurninSettingsTypeDef",
    "TimecodeConfigTypeDef",
    "TransferInputDeviceRequestRequestTypeDef",
    "TransferringInputDeviceSummaryTypeDef",
    "TtmlDestinationSettingsTypeDef",
    "UdpContainerSettingsTypeDef",
    "UdpGroupSettingsTypeDef",
    "UdpOutputSettingsTypeDef",
    "UpdateAccountConfigurationRequestRequestTypeDef",
    "UpdateAccountConfigurationResponseTypeDef",
    "UpdateChannelClassRequestRequestTypeDef",
    "UpdateChannelClassResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    "UpdateCloudWatchAlarmTemplateGroupResponseTypeDef",
    "UpdateCloudWatchAlarmTemplateRequestRequestTypeDef",
    "UpdateCloudWatchAlarmTemplateResponseTypeDef",
    "UpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    "UpdateEventBridgeRuleTemplateGroupResponseTypeDef",
    "UpdateEventBridgeRuleTemplateRequestRequestTypeDef",
    "UpdateEventBridgeRuleTemplateResponseTypeDef",
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
        "AttenuationControl": Ac3AttenuationControlType,
    },
    total=False,
)

AcceptInputDeviceTransferRequestRequestTypeDef = TypedDict(
    "AcceptInputDeviceTransferRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

AccountConfigurationTypeDef = TypedDict(
    "AccountConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
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
        "Eac3AtmosSettings": "Eac3AtmosSettingsTypeDef",
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
        "AudioWatermarkingSettings": "AudioWatermarkSettingsTypeDef",
        "CodecSettings": "AudioCodecSettingsTypeDef",
        "LanguageCode": str,
        "LanguageCodeControl": AudioDescriptionLanguageCodeControlType,
        "RemixSettings": "RemixSettingsTypeDef",
        "StreamName": str,
        "AudioDashRoles": List[DashRoleAudioType],
        "DvbDashAccessibility": DvbDashAccessibilityType,
    },
    total=False,
)

class AudioDescriptionTypeDef(_RequiredAudioDescriptionTypeDef, _OptionalAudioDescriptionTypeDef):
    pass

AudioDolbyEDecodeTypeDef = TypedDict(
    "AudioDolbyEDecodeTypeDef",
    {
        "ProgramSelection": DolbyEProgramSelectionType,
    },
)

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

_RequiredAudioTrackSelectionTypeDef = TypedDict(
    "_RequiredAudioTrackSelectionTypeDef",
    {
        "Tracks": List["AudioTrackTypeDef"],
    },
)
_OptionalAudioTrackSelectionTypeDef = TypedDict(
    "_OptionalAudioTrackSelectionTypeDef",
    {
        "DolbyEDecode": "AudioDolbyEDecodeTypeDef",
    },
    total=False,
)

class AudioTrackSelectionTypeDef(
    _RequiredAudioTrackSelectionTypeDef, _OptionalAudioTrackSelectionTypeDef
):
    pass

AudioTrackTypeDef = TypedDict(
    "AudioTrackTypeDef",
    {
        "Track": int,
    },
)

AudioWatermarkSettingsTypeDef = TypedDict(
    "AudioWatermarkSettingsTypeDef",
    {
        "NielsenWatermarksSettings": "NielsenWatermarksSettingsTypeDef",
    },
    total=False,
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
        "Scte35SegmentationScope": Scte35SegmentationScopeType,
    },
    total=False,
)

AvailSettingsTypeDef = TypedDict(
    "AvailSettingsTypeDef",
    {
        "Esam": "EsamTypeDef",
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
        "Accessibility": AccessibilityTypeType,
        "DestinationSettings": "CaptionDestinationSettingsTypeDef",
        "LanguageCode": str,
        "LanguageDescription": str,
        "CaptionDashRoles": List[DashRoleCaptionType],
        "DvbDashAccessibility": DvbDashAccessibilityType,
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
        "Maintenance": "MaintenanceStatusTypeDef",
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
        "Maintenance": "MaintenanceStatusTypeDef",
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

ClaimDeviceRequestRequestTypeDef = TypedDict(
    "ClaimDeviceRequestRequestTypeDef",
    {
        "Id": str,
    },
    total=False,
)

_RequiredCloudWatchAlarmTemplateGroupSummaryTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmTemplateGroupSummaryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Id": str,
        "Name": str,
        "TemplateCount": int,
    },
)
_OptionalCloudWatchAlarmTemplateGroupSummaryTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmTemplateGroupSummaryTypeDef",
    {
        "Description": str,
        "ModifiedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CloudWatchAlarmTemplateGroupSummaryTypeDef(
    _RequiredCloudWatchAlarmTemplateGroupSummaryTypeDef,
    _OptionalCloudWatchAlarmTemplateGroupSummaryTypeDef,
):
    pass

_RequiredCloudWatchAlarmTemplateSummaryTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmTemplateSummaryTypeDef",
    {
        "Arn": str,
        "ComparisonOperator": CloudWatchAlarmTemplateComparisonOperatorType,
        "CreatedAt": datetime,
        "EvaluationPeriods": int,
        "GroupId": str,
        "Id": str,
        "MetricName": str,
        "Name": str,
        "Period": int,
        "Statistic": CloudWatchAlarmTemplateStatisticType,
        "TargetResourceType": CloudWatchAlarmTemplateTargetResourceTypeType,
        "Threshold": float,
        "TreatMissingData": CloudWatchAlarmTemplateTreatMissingDataType,
    },
)
_OptionalCloudWatchAlarmTemplateSummaryTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmTemplateSummaryTypeDef",
    {
        "DatapointsToAlarm": int,
        "Description": str,
        "ModifiedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CloudWatchAlarmTemplateSummaryTypeDef(
    _RequiredCloudWatchAlarmTemplateSummaryTypeDef, _OptionalCloudWatchAlarmTemplateSummaryTypeDef
):
    pass

_RequiredCmafIngestGroupSettingsTypeDef = TypedDict(
    "_RequiredCmafIngestGroupSettingsTypeDef",
    {
        "Destination": "OutputLocationRefTypeDef",
    },
)
_OptionalCmafIngestGroupSettingsTypeDef = TypedDict(
    "_OptionalCmafIngestGroupSettingsTypeDef",
    {
        "NielsenId3Behavior": CmafNielsenId3BehaviorType,
        "Scte35Type": Scte35TypeType,
        "SegmentLength": int,
        "SegmentLengthUnits": CmafIngestSegmentLengthUnitsType,
        "SendDelayMs": int,
    },
    total=False,
)

class CmafIngestGroupSettingsTypeDef(
    _RequiredCmafIngestGroupSettingsTypeDef, _OptionalCmafIngestGroupSettingsTypeDef
):
    pass

CmafIngestOutputSettingsTypeDef = TypedDict(
    "CmafIngestOutputSettingsTypeDef",
    {
        "NameModifier": str,
    },
    total=False,
)

ColorCorrectionSettingsTypeDef = TypedDict(
    "ColorCorrectionSettingsTypeDef",
    {
        "GlobalColorCorrections": List["ColorCorrectionTypeDef"],
    },
)

ColorCorrectionTypeDef = TypedDict(
    "ColorCorrectionTypeDef",
    {
        "InputColorSpace": ColorSpaceType,
        "OutputColorSpace": ColorSpaceType,
        "Uri": str,
    },
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
        "Maintenance": "MaintenanceCreateSettingsTypeDef",
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

_RequiredCreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef(
    _RequiredCreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef,
    _OptionalCreateCloudWatchAlarmTemplateGroupRequestRequestTypeDef,
):
    pass

CreateCloudWatchAlarmTemplateGroupResponseTypeDef = TypedDict(
    "CreateCloudWatchAlarmTemplateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCloudWatchAlarmTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCloudWatchAlarmTemplateRequestRequestTypeDef",
    {
        "ComparisonOperator": CloudWatchAlarmTemplateComparisonOperatorType,
        "EvaluationPeriods": int,
        "GroupIdentifier": str,
        "MetricName": str,
        "Name": str,
        "Period": int,
        "Statistic": CloudWatchAlarmTemplateStatisticType,
        "TargetResourceType": CloudWatchAlarmTemplateTargetResourceTypeType,
        "Threshold": float,
        "TreatMissingData": CloudWatchAlarmTemplateTreatMissingDataType,
    },
)
_OptionalCreateCloudWatchAlarmTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCloudWatchAlarmTemplateRequestRequestTypeDef",
    {
        "DatapointsToAlarm": int,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateCloudWatchAlarmTemplateRequestRequestTypeDef(
    _RequiredCreateCloudWatchAlarmTemplateRequestRequestTypeDef,
    _OptionalCreateCloudWatchAlarmTemplateRequestRequestTypeDef,
):
    pass

CreateCloudWatchAlarmTemplateResponseTypeDef = TypedDict(
    "CreateCloudWatchAlarmTemplateResponseTypeDef",
    {
        "Arn": str,
        "ComparisonOperator": CloudWatchAlarmTemplateComparisonOperatorType,
        "CreatedAt": datetime,
        "DatapointsToAlarm": int,
        "Description": str,
        "EvaluationPeriods": int,
        "GroupId": str,
        "Id": str,
        "MetricName": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Period": int,
        "Statistic": CloudWatchAlarmTemplateStatisticType,
        "Tags": Dict[str, str],
        "TargetResourceType": CloudWatchAlarmTemplateTargetResourceTypeType,
        "Threshold": float,
        "TreatMissingData": CloudWatchAlarmTemplateTreatMissingDataType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventBridgeRuleTemplateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateEventBridgeRuleTemplateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateEventBridgeRuleTemplateGroupRequestRequestTypeDef(
    _RequiredCreateEventBridgeRuleTemplateGroupRequestRequestTypeDef,
    _OptionalCreateEventBridgeRuleTemplateGroupRequestRequestTypeDef,
):
    pass

CreateEventBridgeRuleTemplateGroupResponseTypeDef = TypedDict(
    "CreateEventBridgeRuleTemplateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventBridgeRuleTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventBridgeRuleTemplateRequestRequestTypeDef",
    {
        "EventType": EventBridgeRuleTemplateEventTypeType,
        "GroupIdentifier": str,
        "Name": str,
    },
)
_OptionalCreateEventBridgeRuleTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventBridgeRuleTemplateRequestRequestTypeDef",
    {
        "Description": str,
        "EventTargets": List["EventBridgeRuleTemplateTargetTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateEventBridgeRuleTemplateRequestRequestTypeDef(
    _RequiredCreateEventBridgeRuleTemplateRequestRequestTypeDef,
    _OptionalCreateEventBridgeRuleTemplateRequestRequestTypeDef,
):
    pass

CreateEventBridgeRuleTemplateResponseTypeDef = TypedDict(
    "CreateEventBridgeRuleTemplateResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "EventTargets": List["EventBridgeRuleTemplateTargetTypeDef"],
        "EventType": EventBridgeRuleTemplateEventTypeType,
        "GroupId": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
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

_RequiredCreateSignalMapRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSignalMapRequestRequestTypeDef",
    {
        "DiscoveryEntryPointArn": str,
        "Name": str,
    },
)
_OptionalCreateSignalMapRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSignalMapRequestRequestTypeDef",
    {
        "CloudWatchAlarmTemplateGroupIdentifiers": List[str],
        "Description": str,
        "EventBridgeRuleTemplateGroupIdentifiers": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateSignalMapRequestRequestTypeDef(
    _RequiredCreateSignalMapRequestRequestTypeDef, _OptionalCreateSignalMapRequestRequestTypeDef
):
    pass

CreateSignalMapResponseTypeDef = TypedDict(
    "CreateSignalMapResponseTypeDef",
    {
        "Arn": str,
        "CloudWatchAlarmTemplateGroupIds": List[str],
        "CreatedAt": datetime,
        "Description": str,
        "DiscoveryEntryPointArn": str,
        "ErrorMessage": str,
        "EventBridgeRuleTemplateGroupIds": List[str],
        "FailedMediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "Id": str,
        "LastDiscoveredAt": datetime,
        "LastSuccessfulMonitorDeployment": "SuccessfulMonitorDeploymentTypeDef",
        "MediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "ModifiedAt": datetime,
        "MonitorChangesPendingDeployment": bool,
        "MonitorDeployment": "MonitorDeploymentTypeDef",
        "Name": str,
        "Status": SignalMapStatusType,
        "Tags": Dict[str, str],
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
        "Maintenance": "MaintenanceStatusTypeDef",
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

DeleteCloudWatchAlarmTemplateGroupRequestRequestTypeDef = TypedDict(
    "DeleteCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteCloudWatchAlarmTemplateRequestRequestTypeDef = TypedDict(
    "DeleteCloudWatchAlarmTemplateRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteEventBridgeRuleTemplateGroupRequestRequestTypeDef = TypedDict(
    "DeleteEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteEventBridgeRuleTemplateRequestRequestTypeDef = TypedDict(
    "DeleteEventBridgeRuleTemplateRequestRequestTypeDef",
    {
        "Identifier": str,
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
        "RenewalSettings": "RenewalSettingsTypeDef",
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

DeleteSignalMapRequestRequestTypeDef = TypedDict(
    "DeleteSignalMapRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

DescribeAccountConfigurationResponseTypeDef = TypedDict(
    "DescribeAccountConfigurationResponseTypeDef",
    {
        "AccountConfiguration": "AccountConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "Maintenance": "MaintenanceStatusTypeDef",
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
        "Type": InputDeviceTypeType,
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
        "Tags": Dict[str, str],
        "AvailabilityZone": str,
        "MedialiveInputArns": List[str],
        "OutputType": InputDeviceOutputTypeType,
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
        "RenewalSettings": "RenewalSettingsTypeDef",
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

DescribeThumbnailsRequestRequestTypeDef = TypedDict(
    "DescribeThumbnailsRequestRequestTypeDef",
    {
        "ChannelId": str,
        "PipelineId": str,
        "ThumbnailType": str,
    },
)

DescribeThumbnailsResponseTypeDef = TypedDict(
    "DescribeThumbnailsResponseTypeDef",
    {
        "ThumbnailDetails": List["ThumbnailDetailTypeDef"],
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

Eac3AtmosSettingsTypeDef = TypedDict(
    "Eac3AtmosSettingsTypeDef",
    {
        "Bitrate": float,
        "CodingMode": Eac3AtmosCodingModeType,
        "Dialnorm": int,
        "DrcLine": Eac3AtmosDrcLineType,
        "DrcRf": Eac3AtmosDrcRfType,
        "HeightTrim": float,
        "SurroundTrim": float,
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
        "ThumbnailConfiguration": "ThumbnailConfigurationTypeDef",
        "ColorCorrectionSettings": "ColorCorrectionSettingsTypeDef",
    },
    total=False,
)

class EncoderSettingsTypeDef(_RequiredEncoderSettingsTypeDef, _OptionalEncoderSettingsTypeDef):
    pass

EpochLockingSettingsTypeDef = TypedDict(
    "EpochLockingSettingsTypeDef",
    {
        "CustomEpoch": str,
        "JamSyncTime": str,
    },
    total=False,
)

_RequiredEsamTypeDef = TypedDict(
    "_RequiredEsamTypeDef",
    {
        "AcquisitionPointId": str,
        "PoisEndpoint": str,
    },
)
_OptionalEsamTypeDef = TypedDict(
    "_OptionalEsamTypeDef",
    {
        "AdAvailOffset": int,
        "PasswordParam": str,
        "Username": str,
        "ZoneIdentity": str,
    },
    total=False,
)

class EsamTypeDef(_RequiredEsamTypeDef, _OptionalEsamTypeDef):
    pass

_RequiredEventBridgeRuleTemplateGroupSummaryTypeDef = TypedDict(
    "_RequiredEventBridgeRuleTemplateGroupSummaryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Id": str,
        "Name": str,
        "TemplateCount": int,
    },
)
_OptionalEventBridgeRuleTemplateGroupSummaryTypeDef = TypedDict(
    "_OptionalEventBridgeRuleTemplateGroupSummaryTypeDef",
    {
        "Description": str,
        "ModifiedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

class EventBridgeRuleTemplateGroupSummaryTypeDef(
    _RequiredEventBridgeRuleTemplateGroupSummaryTypeDef,
    _OptionalEventBridgeRuleTemplateGroupSummaryTypeDef,
):
    pass

_RequiredEventBridgeRuleTemplateSummaryTypeDef = TypedDict(
    "_RequiredEventBridgeRuleTemplateSummaryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "EventTargetCount": int,
        "EventType": EventBridgeRuleTemplateEventTypeType,
        "GroupId": str,
        "Id": str,
        "Name": str,
    },
)
_OptionalEventBridgeRuleTemplateSummaryTypeDef = TypedDict(
    "_OptionalEventBridgeRuleTemplateSummaryTypeDef",
    {
        "Description": str,
        "ModifiedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

class EventBridgeRuleTemplateSummaryTypeDef(
    _RequiredEventBridgeRuleTemplateSummaryTypeDef, _OptionalEventBridgeRuleTemplateSummaryTypeDef
):
    pass

EventBridgeRuleTemplateTargetTypeDef = TypedDict(
    "EventBridgeRuleTemplateTargetTypeDef",
    {
        "Arn": str,
    },
)

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
        "OutputStaticImageOverlayScheduleActions": FeatureActivationsOutputStaticImageOverlayScheduleActionsType,
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
        "TimecodeBurninSettings": "TimecodeBurninSettingsTypeDef",
    },
    total=False,
)

GetCloudWatchAlarmTemplateGroupRequestRequestTypeDef = TypedDict(
    "GetCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetCloudWatchAlarmTemplateGroupResponseTypeDef = TypedDict(
    "GetCloudWatchAlarmTemplateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudWatchAlarmTemplateRequestRequestTypeDef = TypedDict(
    "GetCloudWatchAlarmTemplateRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetCloudWatchAlarmTemplateResponseTypeDef = TypedDict(
    "GetCloudWatchAlarmTemplateResponseTypeDef",
    {
        "Arn": str,
        "ComparisonOperator": CloudWatchAlarmTemplateComparisonOperatorType,
        "CreatedAt": datetime,
        "DatapointsToAlarm": int,
        "Description": str,
        "EvaluationPeriods": int,
        "GroupId": str,
        "Id": str,
        "MetricName": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Period": int,
        "Statistic": CloudWatchAlarmTemplateStatisticType,
        "Tags": Dict[str, str],
        "TargetResourceType": CloudWatchAlarmTemplateTargetResourceTypeType,
        "Threshold": float,
        "TreatMissingData": CloudWatchAlarmTemplateTreatMissingDataType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventBridgeRuleTemplateGroupRequestRequestTypeDef = TypedDict(
    "GetEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetEventBridgeRuleTemplateGroupResponseTypeDef = TypedDict(
    "GetEventBridgeRuleTemplateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventBridgeRuleTemplateRequestRequestTypeDef = TypedDict(
    "GetEventBridgeRuleTemplateRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetEventBridgeRuleTemplateResponseTypeDef = TypedDict(
    "GetEventBridgeRuleTemplateResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "EventTargets": List["EventBridgeRuleTemplateTargetTypeDef"],
        "EventType": EventBridgeRuleTemplateEventTypeType,
        "GroupId": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSignalMapRequestRequestTypeDef = TypedDict(
    "GetSignalMapRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetSignalMapResponseTypeDef = TypedDict(
    "GetSignalMapResponseTypeDef",
    {
        "Arn": str,
        "CloudWatchAlarmTemplateGroupIds": List[str],
        "CreatedAt": datetime,
        "Description": str,
        "DiscoveryEntryPointArn": str,
        "ErrorMessage": str,
        "EventBridgeRuleTemplateGroupIds": List[str],
        "FailedMediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "Id": str,
        "LastDiscoveredAt": datetime,
        "LastSuccessfulMonitorDeployment": "SuccessfulMonitorDeploymentTypeDef",
        "MediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "ModifiedAt": datetime,
        "MonitorChangesPendingDeployment": bool,
        "MonitorDeployment": "MonitorDeploymentTypeDef",
        "Name": str,
        "Status": SignalMapStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "OutputLockingSettings": "OutputLockingSettingsTypeDef",
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
        "TimecodeBurninSettings": "TimecodeBurninSettingsTypeDef",
    },
    total=False,
)

H265ColorSpaceSettingsTypeDef = TypedDict(
    "H265ColorSpaceSettingsTypeDef",
    {
        "ColorSpacePassthroughSettings": Dict[str, Any],
        "DolbyVision81Settings": Dict[str, Any],
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
        "TimecodeBurninSettings": "TimecodeBurninSettingsTypeDef",
        "MvOverPictureBoundaries": H265MvOverPictureBoundariesType,
        "MvTemporalPredictor": H265MvTemporalPredictorType,
        "TileHeight": int,
        "TilePadding": H265TilePaddingType,
        "TileWidth": int,
        "TreeblockSize": H265TreeblockSizeType,
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
        "ProgramDateTimeClock": HlsProgramDateTimeClockType,
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
        "Id3": str,
    },
    total=False,
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

InputDeviceConfigurableAudioChannelPairConfigTypeDef = TypedDict(
    "InputDeviceConfigurableAudioChannelPairConfigTypeDef",
    {
        "Id": int,
        "Profile": InputDeviceConfigurableAudioChannelPairProfileType,
    },
    total=False,
)

InputDeviceConfigurableSettingsTypeDef = TypedDict(
    "InputDeviceConfigurableSettingsTypeDef",
    {
        "ConfiguredInput": InputDeviceConfiguredInputType,
        "MaxBitrate": int,
        "LatencyMs": int,
        "Codec": InputDeviceCodecType,
        "MediaconnectSettings": "InputDeviceMediaConnectConfigurableSettingsTypeDef",
        "AudioChannelPairs": List["InputDeviceConfigurableAudioChannelPairConfigTypeDef"],
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
        "LatencyMs": int,
    },
    total=False,
)

InputDeviceMediaConnectConfigurableSettingsTypeDef = TypedDict(
    "InputDeviceMediaConnectConfigurableSettingsTypeDef",
    {
        "FlowArn": str,
        "RoleArn": str,
        "SecretArn": str,
        "SourceName": str,
    },
    total=False,
)

InputDeviceMediaConnectSettingsTypeDef = TypedDict(
    "InputDeviceMediaConnectSettingsTypeDef",
    {
        "FlowArn": str,
        "RoleArn": str,
        "SecretArn": str,
        "SourceName": str,
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
        "Type": InputDeviceTypeType,
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
        "Tags": Dict[str, str],
        "AvailabilityZone": str,
        "MedialiveInputArns": List[str],
        "OutputType": InputDeviceOutputTypeType,
    },
    total=False,
)

InputDeviceUhdAudioChannelPairConfigTypeDef = TypedDict(
    "InputDeviceUhdAudioChannelPairConfigTypeDef",
    {
        "Id": int,
        "Profile": InputDeviceUhdAudioChannelPairProfileType,
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
        "LatencyMs": int,
        "Codec": InputDeviceCodecType,
        "MediaconnectSettings": "InputDeviceMediaConnectSettingsTypeDef",
        "AudioChannelPairs": List["InputDeviceUhdAudioChannelPairConfigTypeDef"],
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
        "Scte35Pid": int,
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

ListCloudWatchAlarmTemplateGroupsRequestRequestTypeDef = TypedDict(
    "ListCloudWatchAlarmTemplateGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Scope": str,
        "SignalMapIdentifier": str,
    },
    total=False,
)

ListCloudWatchAlarmTemplateGroupsResponseTypeDef = TypedDict(
    "ListCloudWatchAlarmTemplateGroupsResponseTypeDef",
    {
        "CloudWatchAlarmTemplateGroups": List["CloudWatchAlarmTemplateGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCloudWatchAlarmTemplatesRequestRequestTypeDef = TypedDict(
    "ListCloudWatchAlarmTemplatesRequestRequestTypeDef",
    {
        "GroupIdentifier": str,
        "MaxResults": int,
        "NextToken": str,
        "Scope": str,
        "SignalMapIdentifier": str,
    },
    total=False,
)

ListCloudWatchAlarmTemplatesResponseTypeDef = TypedDict(
    "ListCloudWatchAlarmTemplatesResponseTypeDef",
    {
        "CloudWatchAlarmTemplates": List["CloudWatchAlarmTemplateSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventBridgeRuleTemplateGroupsRequestRequestTypeDef = TypedDict(
    "ListEventBridgeRuleTemplateGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SignalMapIdentifier": str,
    },
    total=False,
)

ListEventBridgeRuleTemplateGroupsResponseTypeDef = TypedDict(
    "ListEventBridgeRuleTemplateGroupsResponseTypeDef",
    {
        "EventBridgeRuleTemplateGroups": List["EventBridgeRuleTemplateGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventBridgeRuleTemplatesRequestRequestTypeDef = TypedDict(
    "ListEventBridgeRuleTemplatesRequestRequestTypeDef",
    {
        "GroupIdentifier": str,
        "MaxResults": int,
        "NextToken": str,
        "SignalMapIdentifier": str,
    },
    total=False,
)

ListEventBridgeRuleTemplatesResponseTypeDef = TypedDict(
    "ListEventBridgeRuleTemplatesResponseTypeDef",
    {
        "EventBridgeRuleTemplates": List["EventBridgeRuleTemplateSummaryTypeDef"],
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

ListSignalMapsRequestRequestTypeDef = TypedDict(
    "ListSignalMapsRequestRequestTypeDef",
    {
        "CloudWatchAlarmTemplateGroupIdentifier": str,
        "EventBridgeRuleTemplateGroupIdentifier": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSignalMapsResponseTypeDef = TypedDict(
    "ListSignalMapsResponseTypeDef",
    {
        "NextToken": str,
        "SignalMaps": List["SignalMapSummaryTypeDef"],
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
        "Scte35PrerollPullupMilliseconds": float,
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
        "KlvBehavior": M3u8KlvBehaviorType,
        "KlvDataPids": str,
    },
    total=False,
)

MaintenanceCreateSettingsTypeDef = TypedDict(
    "MaintenanceCreateSettingsTypeDef",
    {
        "MaintenanceDay": MaintenanceDayType,
        "MaintenanceStartTime": str,
    },
    total=False,
)

MaintenanceStatusTypeDef = TypedDict(
    "MaintenanceStatusTypeDef",
    {
        "MaintenanceDay": MaintenanceDayType,
        "MaintenanceDeadline": str,
        "MaintenanceScheduledDate": str,
        "MaintenanceStartTime": str,
    },
    total=False,
)

MaintenanceUpdateSettingsTypeDef = TypedDict(
    "MaintenanceUpdateSettingsTypeDef",
    {
        "MaintenanceDay": MaintenanceDayType,
        "MaintenanceScheduledDate": str,
        "MaintenanceStartTime": str,
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

_RequiredMediaResourceNeighborTypeDef = TypedDict(
    "_RequiredMediaResourceNeighborTypeDef",
    {
        "Arn": str,
    },
)
_OptionalMediaResourceNeighborTypeDef = TypedDict(
    "_OptionalMediaResourceNeighborTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class MediaResourceNeighborTypeDef(
    _RequiredMediaResourceNeighborTypeDef, _OptionalMediaResourceNeighborTypeDef
):
    pass

MediaResourceTypeDef = TypedDict(
    "MediaResourceTypeDef",
    {
        "Destinations": List["MediaResourceNeighborTypeDef"],
        "Name": str,
        "Sources": List["MediaResourceNeighborTypeDef"],
    },
    total=False,
)

_RequiredMonitorDeploymentTypeDef = TypedDict(
    "_RequiredMonitorDeploymentTypeDef",
    {
        "Status": SignalMapMonitorDeploymentStatusType,
    },
)
_OptionalMonitorDeploymentTypeDef = TypedDict(
    "_OptionalMonitorDeploymentTypeDef",
    {
        "DetailsUri": str,
        "ErrorMessage": str,
    },
    total=False,
)

class MonitorDeploymentTypeDef(
    _RequiredMonitorDeploymentTypeDef, _OptionalMonitorDeploymentTypeDef
):
    pass

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
        "TimecodeBurninSettings": "TimecodeBurninSettingsTypeDef",
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

NielsenCBETTypeDef = TypedDict(
    "NielsenCBETTypeDef",
    {
        "CbetCheckDigitString": str,
        "CbetStepaside": NielsenWatermarksCbetStepasideType,
        "Csid": str,
    },
)

NielsenConfigurationTypeDef = TypedDict(
    "NielsenConfigurationTypeDef",
    {
        "DistributorId": str,
        "NielsenPcmToId3Tagging": NielsenPcmToId3TaggingStateType,
    },
    total=False,
)

_RequiredNielsenNaesIiNwTypeDef = TypedDict(
    "_RequiredNielsenNaesIiNwTypeDef",
    {
        "CheckDigitString": str,
        "Sid": float,
    },
)
_OptionalNielsenNaesIiNwTypeDef = TypedDict(
    "_OptionalNielsenNaesIiNwTypeDef",
    {
        "Timezone": NielsenWatermarkTimezonesType,
    },
    total=False,
)

class NielsenNaesIiNwTypeDef(_RequiredNielsenNaesIiNwTypeDef, _OptionalNielsenNaesIiNwTypeDef):
    pass

NielsenWatermarksSettingsTypeDef = TypedDict(
    "NielsenWatermarksSettingsTypeDef",
    {
        "NielsenCbetSettings": "NielsenCBETTypeDef",
        "NielsenDistributionType": NielsenWatermarksDistributionTypesType,
        "NielsenNaesIiNwSettings": "NielsenNaesIiNwTypeDef",
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
        "CmafIngestGroupSettings": "CmafIngestGroupSettingsTypeDef",
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

OutputLockingSettingsTypeDef = TypedDict(
    "OutputLockingSettingsTypeDef",
    {
        "EpochLockingSettings": "EpochLockingSettingsTypeDef",
        "PipelineLockingSettings": Dict[str, Any],
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
        "CmafIngestOutputSettings": "CmafIngestOutputSettingsTypeDef",
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
        "RenewalSettings": "RenewalSettingsTypeDef",
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

_RequiredRebootInputDeviceRequestRequestTypeDef = TypedDict(
    "_RequiredRebootInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)
_OptionalRebootInputDeviceRequestRequestTypeDef = TypedDict(
    "_OptionalRebootInputDeviceRequestRequestTypeDef",
    {
        "Force": RebootInputDeviceForceType,
    },
    total=False,
)

class RebootInputDeviceRequestRequestTypeDef(
    _RequiredRebootInputDeviceRequestRequestTypeDef, _OptionalRebootInputDeviceRequestRequestTypeDef
):
    pass

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

RenewalSettingsTypeDef = TypedDict(
    "RenewalSettingsTypeDef",
    {
        "AutomaticRenewal": ReservationAutomaticRenewalType,
        "RenewalCount": int,
    },
    total=False,
)

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
        "RenewalSettings": "RenewalSettingsTypeDef",
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

_RequiredRestartChannelPipelinesRequestRequestTypeDef = TypedDict(
    "_RequiredRestartChannelPipelinesRequestRequestTypeDef",
    {
        "ChannelId": str,
    },
)
_OptionalRestartChannelPipelinesRequestRequestTypeDef = TypedDict(
    "_OptionalRestartChannelPipelinesRequestRequestTypeDef",
    {
        "PipelineIds": List[ChannelPipelineIdToRestartType],
    },
    total=False,
)

class RestartChannelPipelinesRequestRequestTypeDef(
    _RequiredRestartChannelPipelinesRequestRequestTypeDef,
    _OptionalRestartChannelPipelinesRequestRequestTypeDef,
):
    pass

RestartChannelPipelinesResponseTypeDef = TypedDict(
    "RestartChannelPipelinesResponseTypeDef",
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
        "Maintenance": "MaintenanceStatusTypeDef",
        "MaintenanceStatus": str,
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
        "IncludeFillerNalUnits": IncludeFillerNalUnitsType,
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
        "Scte35InputSettings": "Scte35InputScheduleActionSettingsTypeDef",
        "Scte35ReturnToNetworkSettings": "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
        "Scte35SpliceInsertSettings": "Scte35SpliceInsertScheduleActionSettingsTypeDef",
        "Scte35TimeSignalSettings": "Scte35TimeSignalScheduleActionSettingsTypeDef",
        "StaticImageActivateSettings": "StaticImageActivateScheduleActionSettingsTypeDef",
        "StaticImageDeactivateSettings": "StaticImageDeactivateScheduleActionSettingsTypeDef",
        "StaticImageOutputActivateSettings": "StaticImageOutputActivateScheduleActionSettingsTypeDef",
        "StaticImageOutputDeactivateSettings": "StaticImageOutputDeactivateScheduleActionSettingsTypeDef",
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

_RequiredScte35InputScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredScte35InputScheduleActionSettingsTypeDef",
    {
        "Mode": Scte35InputModeType,
    },
)
_OptionalScte35InputScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalScte35InputScheduleActionSettingsTypeDef",
    {
        "InputAttachmentNameReference": str,
    },
    total=False,
)

class Scte35InputScheduleActionSettingsTypeDef(
    _RequiredScte35InputScheduleActionSettingsTypeDef,
    _OptionalScte35InputScheduleActionSettingsTypeDef,
):
    pass

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

_RequiredSignalMapSummaryTypeDef = TypedDict(
    "_RequiredSignalMapSummaryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Id": str,
        "MonitorDeploymentStatus": SignalMapMonitorDeploymentStatusType,
        "Name": str,
        "Status": SignalMapStatusType,
    },
)
_OptionalSignalMapSummaryTypeDef = TypedDict(
    "_OptionalSignalMapSummaryTypeDef",
    {
        "Description": str,
        "ModifiedAt": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)

class SignalMapSummaryTypeDef(_RequiredSignalMapSummaryTypeDef, _OptionalSignalMapSummaryTypeDef):
    pass

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
        "Maintenance": "MaintenanceStatusTypeDef",
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

StartDeleteMonitorDeploymentRequestRequestTypeDef = TypedDict(
    "StartDeleteMonitorDeploymentRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

StartDeleteMonitorDeploymentResponseTypeDef = TypedDict(
    "StartDeleteMonitorDeploymentResponseTypeDef",
    {
        "Arn": str,
        "CloudWatchAlarmTemplateGroupIds": List[str],
        "CreatedAt": datetime,
        "Description": str,
        "DiscoveryEntryPointArn": str,
        "ErrorMessage": str,
        "EventBridgeRuleTemplateGroupIds": List[str],
        "FailedMediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "Id": str,
        "LastDiscoveredAt": datetime,
        "LastSuccessfulMonitorDeployment": "SuccessfulMonitorDeploymentTypeDef",
        "MediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "ModifiedAt": datetime,
        "MonitorChangesPendingDeployment": bool,
        "MonitorDeployment": "MonitorDeploymentTypeDef",
        "Name": str,
        "Status": SignalMapStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartInputDeviceMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "StartInputDeviceMaintenanceWindowRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

StartInputDeviceRequestRequestTypeDef = TypedDict(
    "StartInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
    },
)

_RequiredStartMonitorDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredStartMonitorDeploymentRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalStartMonitorDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalStartMonitorDeploymentRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class StartMonitorDeploymentRequestRequestTypeDef(
    _RequiredStartMonitorDeploymentRequestRequestTypeDef,
    _OptionalStartMonitorDeploymentRequestRequestTypeDef,
):
    pass

StartMonitorDeploymentResponseTypeDef = TypedDict(
    "StartMonitorDeploymentResponseTypeDef",
    {
        "Arn": str,
        "CloudWatchAlarmTemplateGroupIds": List[str],
        "CreatedAt": datetime,
        "Description": str,
        "DiscoveryEntryPointArn": str,
        "ErrorMessage": str,
        "EventBridgeRuleTemplateGroupIds": List[str],
        "FailedMediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "Id": str,
        "LastDiscoveredAt": datetime,
        "LastSuccessfulMonitorDeployment": "SuccessfulMonitorDeploymentTypeDef",
        "MediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "ModifiedAt": datetime,
        "MonitorChangesPendingDeployment": bool,
        "MonitorDeployment": "MonitorDeploymentTypeDef",
        "Name": str,
        "Status": SignalMapStatusType,
        "Tags": Dict[str, str],
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

_RequiredStartUpdateSignalMapRequestRequestTypeDef = TypedDict(
    "_RequiredStartUpdateSignalMapRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalStartUpdateSignalMapRequestRequestTypeDef = TypedDict(
    "_OptionalStartUpdateSignalMapRequestRequestTypeDef",
    {
        "CloudWatchAlarmTemplateGroupIdentifiers": List[str],
        "Description": str,
        "DiscoveryEntryPointArn": str,
        "EventBridgeRuleTemplateGroupIdentifiers": List[str],
        "ForceRediscovery": bool,
        "Name": str,
    },
    total=False,
)

class StartUpdateSignalMapRequestRequestTypeDef(
    _RequiredStartUpdateSignalMapRequestRequestTypeDef,
    _OptionalStartUpdateSignalMapRequestRequestTypeDef,
):
    pass

StartUpdateSignalMapResponseTypeDef = TypedDict(
    "StartUpdateSignalMapResponseTypeDef",
    {
        "Arn": str,
        "CloudWatchAlarmTemplateGroupIds": List[str],
        "CreatedAt": datetime,
        "Description": str,
        "DiscoveryEntryPointArn": str,
        "ErrorMessage": str,
        "EventBridgeRuleTemplateGroupIds": List[str],
        "FailedMediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "Id": str,
        "LastDiscoveredAt": datetime,
        "LastSuccessfulMonitorDeployment": "SuccessfulMonitorDeploymentTypeDef",
        "MediaResourceMap": Dict[str, "MediaResourceTypeDef"],
        "ModifiedAt": datetime,
        "MonitorChangesPendingDeployment": bool,
        "MonitorDeployment": "MonitorDeploymentTypeDef",
        "Name": str,
        "Status": SignalMapStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredStaticImageOutputActivateScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredStaticImageOutputActivateScheduleActionSettingsTypeDef",
    {
        "Image": "InputLocationTypeDef",
        "OutputNames": List[str],
    },
)
_OptionalStaticImageOutputActivateScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalStaticImageOutputActivateScheduleActionSettingsTypeDef",
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

class StaticImageOutputActivateScheduleActionSettingsTypeDef(
    _RequiredStaticImageOutputActivateScheduleActionSettingsTypeDef,
    _OptionalStaticImageOutputActivateScheduleActionSettingsTypeDef,
):
    pass

_RequiredStaticImageOutputDeactivateScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredStaticImageOutputDeactivateScheduleActionSettingsTypeDef",
    {
        "OutputNames": List[str],
    },
)
_OptionalStaticImageOutputDeactivateScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalStaticImageOutputDeactivateScheduleActionSettingsTypeDef",
    {
        "FadeOut": int,
        "Layer": int,
    },
    total=False,
)

class StaticImageOutputDeactivateScheduleActionSettingsTypeDef(
    _RequiredStaticImageOutputDeactivateScheduleActionSettingsTypeDef,
    _OptionalStaticImageOutputDeactivateScheduleActionSettingsTypeDef,
):
    pass

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
        "Maintenance": "MaintenanceStatusTypeDef",
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

StopInputDeviceRequestRequestTypeDef = TypedDict(
    "StopInputDeviceRequestRequestTypeDef",
    {
        "InputDeviceId": str,
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

SuccessfulMonitorDeploymentTypeDef = TypedDict(
    "SuccessfulMonitorDeploymentTypeDef",
    {
        "DetailsUri": str,
        "Status": SignalMapMonitorDeploymentStatusType,
    },
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

ThumbnailConfigurationTypeDef = TypedDict(
    "ThumbnailConfigurationTypeDef",
    {
        "State": ThumbnailStateType,
    },
)

ThumbnailDetailTypeDef = TypedDict(
    "ThumbnailDetailTypeDef",
    {
        "PipelineId": str,
        "Thumbnails": List["ThumbnailTypeDef"],
    },
    total=False,
)

ThumbnailTypeDef = TypedDict(
    "ThumbnailTypeDef",
    {
        "Body": str,
        "ContentType": str,
        "ThumbnailType": ThumbnailTypeType,
        "TimeStamp": datetime,
    },
    total=False,
)

_RequiredTimecodeBurninSettingsTypeDef = TypedDict(
    "_RequiredTimecodeBurninSettingsTypeDef",
    {
        "FontSize": TimecodeBurninFontSizeType,
        "Position": TimecodeBurninPositionType,
    },
)
_OptionalTimecodeBurninSettingsTypeDef = TypedDict(
    "_OptionalTimecodeBurninSettingsTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class TimecodeBurninSettingsTypeDef(
    _RequiredTimecodeBurninSettingsTypeDef, _OptionalTimecodeBurninSettingsTypeDef
):
    pass

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

UpdateAccountConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAccountConfigurationRequestRequestTypeDef",
    {
        "AccountConfiguration": "AccountConfigurationTypeDef",
    },
    total=False,
)

UpdateAccountConfigurationResponseTypeDef = TypedDict(
    "UpdateAccountConfigurationResponseTypeDef",
    {
        "AccountConfiguration": "AccountConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

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
        "Maintenance": "MaintenanceUpdateSettingsTypeDef",
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

_RequiredUpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef(
    _RequiredUpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef,
    _OptionalUpdateCloudWatchAlarmTemplateGroupRequestRequestTypeDef,
):
    pass

UpdateCloudWatchAlarmTemplateGroupResponseTypeDef = TypedDict(
    "UpdateCloudWatchAlarmTemplateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateCloudWatchAlarmTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCloudWatchAlarmTemplateRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateCloudWatchAlarmTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCloudWatchAlarmTemplateRequestRequestTypeDef",
    {
        "ComparisonOperator": CloudWatchAlarmTemplateComparisonOperatorType,
        "DatapointsToAlarm": int,
        "Description": str,
        "EvaluationPeriods": int,
        "GroupIdentifier": str,
        "MetricName": str,
        "Name": str,
        "Period": int,
        "Statistic": CloudWatchAlarmTemplateStatisticType,
        "TargetResourceType": CloudWatchAlarmTemplateTargetResourceTypeType,
        "Threshold": float,
        "TreatMissingData": CloudWatchAlarmTemplateTreatMissingDataType,
    },
    total=False,
)

class UpdateCloudWatchAlarmTemplateRequestRequestTypeDef(
    _RequiredUpdateCloudWatchAlarmTemplateRequestRequestTypeDef,
    _OptionalUpdateCloudWatchAlarmTemplateRequestRequestTypeDef,
):
    pass

UpdateCloudWatchAlarmTemplateResponseTypeDef = TypedDict(
    "UpdateCloudWatchAlarmTemplateResponseTypeDef",
    {
        "Arn": str,
        "ComparisonOperator": CloudWatchAlarmTemplateComparisonOperatorType,
        "CreatedAt": datetime,
        "DatapointsToAlarm": int,
        "Description": str,
        "EvaluationPeriods": int,
        "GroupId": str,
        "Id": str,
        "MetricName": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Period": int,
        "Statistic": CloudWatchAlarmTemplateStatisticType,
        "Tags": Dict[str, str],
        "TargetResourceType": CloudWatchAlarmTemplateTargetResourceTypeType,
        "Threshold": float,
        "TreatMissingData": CloudWatchAlarmTemplateTreatMissingDataType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef(
    _RequiredUpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef,
    _OptionalUpdateEventBridgeRuleTemplateGroupRequestRequestTypeDef,
):
    pass

UpdateEventBridgeRuleTemplateGroupResponseTypeDef = TypedDict(
    "UpdateEventBridgeRuleTemplateGroupResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEventBridgeRuleTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventBridgeRuleTemplateRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)
_OptionalUpdateEventBridgeRuleTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventBridgeRuleTemplateRequestRequestTypeDef",
    {
        "Description": str,
        "EventTargets": List["EventBridgeRuleTemplateTargetTypeDef"],
        "EventType": EventBridgeRuleTemplateEventTypeType,
        "GroupIdentifier": str,
        "Name": str,
    },
    total=False,
)

class UpdateEventBridgeRuleTemplateRequestRequestTypeDef(
    _RequiredUpdateEventBridgeRuleTemplateRequestRequestTypeDef,
    _OptionalUpdateEventBridgeRuleTemplateRequestRequestTypeDef,
):
    pass

UpdateEventBridgeRuleTemplateResponseTypeDef = TypedDict(
    "UpdateEventBridgeRuleTemplateResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "EventTargets": List["EventBridgeRuleTemplateTargetTypeDef"],
        "EventType": EventBridgeRuleTemplateEventTypeType,
        "GroupId": str,
        "Id": str,
        "ModifiedAt": datetime,
        "Name": str,
        "Tags": Dict[str, str],
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
        "AvailabilityZone": str,
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
        "Type": InputDeviceTypeType,
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
        "Tags": Dict[str, str],
        "AvailabilityZone": str,
        "MedialiveInputArns": List[str],
        "OutputType": InputDeviceOutputTypeType,
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
        "RenewalSettings": "RenewalSettingsTypeDef",
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
