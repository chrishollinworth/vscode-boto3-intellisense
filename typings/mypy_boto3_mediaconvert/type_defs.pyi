"""
Main interface for mediaconvert service type definitions.

Usage::

    ```python
    from mypy_boto3_mediaconvert.type_defs import AacSettingsTypeDef

    data: AacSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

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
    "AccelerationSettingsTypeDef",
    "AiffSettingsTypeDef",
    "AncillarySourceSettingsTypeDef",
    "AudioChannelTaggingSettingsTypeDef",
    "AudioCodecSettingsTypeDef",
    "AudioDescriptionTypeDef",
    "AudioNormalizationSettingsTypeDef",
    "AudioSelectorGroupTypeDef",
    "AudioSelectorTypeDef",
    "AutomatedAbrSettingsTypeDef",
    "AutomatedEncodingSettingsTypeDef",
    "Av1QvbrSettingsTypeDef",
    "Av1SettingsTypeDef",
    "AvailBlankingTypeDef",
    "AvcIntraSettingsTypeDef",
    "AvcIntraUhdSettingsTypeDef",
    "BurninDestinationSettingsTypeDef",
    "CaptionDescriptionPresetTypeDef",
    "CaptionDescriptionTypeDef",
    "CaptionDestinationSettingsTypeDef",
    "CaptionSelectorTypeDef",
    "CaptionSourceFramerateTypeDef",
    "CaptionSourceSettingsTypeDef",
    "ChannelMappingTypeDef",
    "CmafAdditionalManifestTypeDef",
    "CmafEncryptionSettingsTypeDef",
    "CmafGroupSettingsTypeDef",
    "CmfcSettingsTypeDef",
    "ColorCorrectorTypeDef",
    "ContainerSettingsTypeDef",
    "DashAdditionalManifestTypeDef",
    "DashIsoEncryptionSettingsTypeDef",
    "DashIsoGroupSettingsTypeDef",
    "DeinterlacerTypeDef",
    "DestinationSettingsTypeDef",
    "DolbyVisionLevel6MetadataTypeDef",
    "DolbyVisionTypeDef",
    "DvbNitSettingsTypeDef",
    "DvbSdtSettingsTypeDef",
    "DvbSubDestinationSettingsTypeDef",
    "DvbSubSourceSettingsTypeDef",
    "DvbTdtSettingsTypeDef",
    "Eac3AtmosSettingsTypeDef",
    "Eac3SettingsTypeDef",
    "EmbeddedDestinationSettingsTypeDef",
    "EmbeddedSourceSettingsTypeDef",
    "EndpointTypeDef",
    "EsamManifestConfirmConditionNotificationTypeDef",
    "EsamSettingsTypeDef",
    "EsamSignalProcessingNotificationTypeDef",
    "F4vSettingsTypeDef",
    "FileGroupSettingsTypeDef",
    "FileSourceSettingsTypeDef",
    "FrameCaptureSettingsTypeDef",
    "H264QvbrSettingsTypeDef",
    "H264SettingsTypeDef",
    "H265QvbrSettingsTypeDef",
    "H265SettingsTypeDef",
    "Hdr10MetadataTypeDef",
    "HlsAdditionalManifestTypeDef",
    "HlsCaptionLanguageMappingTypeDef",
    "HlsEncryptionSettingsTypeDef",
    "HlsGroupSettingsTypeDef",
    "HlsSettingsTypeDef",
    "HopDestinationTypeDef",
    "Id3InsertionTypeDef",
    "ImageInserterTypeDef",
    "ImscDestinationSettingsTypeDef",
    "InputClippingTypeDef",
    "InputDecryptionSettingsTypeDef",
    "InputTemplateTypeDef",
    "InputTypeDef",
    "InsertableImageTypeDef",
    "JobMessagesTypeDef",
    "JobSettingsTypeDef",
    "JobTemplateSettingsTypeDef",
    "JobTemplateTypeDef",
    "JobTypeDef",
    "M2tsScte35EsamTypeDef",
    "M2tsSettingsTypeDef",
    "M3u8SettingsTypeDef",
    "MotionImageInserterTypeDef",
    "MotionImageInsertionFramerateTypeDef",
    "MotionImageInsertionOffsetTypeDef",
    "MovSettingsTypeDef",
    "Mp2SettingsTypeDef",
    "Mp3SettingsTypeDef",
    "Mp4SettingsTypeDef",
    "MpdSettingsTypeDef",
    "Mpeg2SettingsTypeDef",
    "MsSmoothAdditionalManifestTypeDef",
    "MsSmoothEncryptionSettingsTypeDef",
    "MsSmoothGroupSettingsTypeDef",
    "MxfSettingsTypeDef",
    "NexGuardFileMarkerSettingsTypeDef",
    "NielsenConfigurationTypeDef",
    "NielsenNonLinearWatermarkSettingsTypeDef",
    "NoiseReducerFilterSettingsTypeDef",
    "NoiseReducerSpatialFilterSettingsTypeDef",
    "NoiseReducerTemporalFilterSettingsTypeDef",
    "NoiseReducerTypeDef",
    "OpusSettingsTypeDef",
    "OutputChannelMappingTypeDef",
    "OutputDetailTypeDef",
    "OutputGroupDetailTypeDef",
    "OutputGroupSettingsTypeDef",
    "OutputGroupTypeDef",
    "OutputSettingsTypeDef",
    "OutputTypeDef",
    "PartnerWatermarkingTypeDef",
    "PresetSettingsTypeDef",
    "PresetTypeDef",
    "ProresSettingsTypeDef",
    "QueueTransitionTypeDef",
    "QueueTypeDef",
    "RectangleTypeDef",
    "RemixSettingsTypeDef",
    "ReservationPlanTypeDef",
    "ResourceTagsTypeDef",
    "ResponseMetadata",
    "S3DestinationAccessControlTypeDef",
    "S3DestinationSettingsTypeDef",
    "S3EncryptionSettingsTypeDef",
    "SccDestinationSettingsTypeDef",
    "SpekeKeyProviderCmafTypeDef",
    "SpekeKeyProviderTypeDef",
    "StaticKeyProviderTypeDef",
    "TeletextDestinationSettingsTypeDef",
    "TeletextSourceSettingsTypeDef",
    "TimecodeBurninTypeDef",
    "TimecodeConfigTypeDef",
    "TimedMetadataInsertionTypeDef",
    "TimingTypeDef",
    "TrackSourceSettingsTypeDef",
    "TtmlDestinationSettingsTypeDef",
    "Vc3SettingsTypeDef",
    "VideoCodecSettingsTypeDef",
    "VideoDescriptionTypeDef",
    "VideoDetailTypeDef",
    "VideoPreprocessorTypeDef",
    "VideoSelectorTypeDef",
    "VorbisSettingsTypeDef",
    "Vp8SettingsTypeDef",
    "Vp9SettingsTypeDef",
    "WavSettingsTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreatePresetResponseTypeDef",
    "CreateQueueResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "GetJobResponseTypeDef",
    "GetJobTemplateResponseTypeDef",
    "GetPresetResponseTypeDef",
    "GetQueueResponseTypeDef",
    "ListJobTemplatesResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListPresetsResponseTypeDef",
    "ListQueuesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReservationPlanSettingsTypeDef",
    "UpdateJobTemplateResponseTypeDef",
    "UpdatePresetResponseTypeDef",
    "UpdateQueueResponseTypeDef",
)

AacSettingsTypeDef = TypedDict(
    "AacSettingsTypeDef",
    {
        "AudioDescriptionBroadcasterMix": Literal["BROADCASTER_MIXED_AD", "NORMAL"],
        "Bitrate": int,
        "CodecProfile": Literal["LC", "HEV1", "HEV2"],
        "CodingMode": Literal[
            "AD_RECEIVER_MIX",
            "CODING_MODE_1_0",
            "CODING_MODE_1_1",
            "CODING_MODE_2_0",
            "CODING_MODE_5_1",
        ],
        "RateControlMode": Literal["CBR", "VBR"],
        "RawFormat": Literal["LATM_LOAS", "NONE"],
        "SampleRate": int,
        "Specification": Literal["MPEG2", "MPEG4"],
        "VbrQuality": Literal["LOW", "MEDIUM_LOW", "MEDIUM_HIGH", "HIGH"],
    },
    total=False,
)

Ac3SettingsTypeDef = TypedDict(
    "Ac3SettingsTypeDef",
    {
        "Bitrate": int,
        "BitstreamMode": Literal[
            "COMPLETE_MAIN",
            "COMMENTARY",
            "DIALOGUE",
            "EMERGENCY",
            "HEARING_IMPAIRED",
            "MUSIC_AND_EFFECTS",
            "VISUALLY_IMPAIRED",
            "VOICE_OVER",
        ],
        "CodingMode": Literal[
            "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_3_2_LFE"
        ],
        "Dialnorm": int,
        "DynamicRangeCompressionProfile": Literal["FILM_STANDARD", "NONE"],
        "LfeFilter": Literal["ENABLED", "DISABLED"],
        "MetadataControl": Literal["FOLLOW_INPUT", "USE_CONFIGURED"],
        "SampleRate": int,
    },
    total=False,
)

AccelerationSettingsTypeDef = TypedDict(
    "AccelerationSettingsTypeDef", {"Mode": Literal["DISABLED", "ENABLED", "PREFERRED"]}
)

AiffSettingsTypeDef = TypedDict(
    "AiffSettingsTypeDef", {"BitDepth": int, "Channels": int, "SampleRate": int}, total=False
)

AncillarySourceSettingsTypeDef = TypedDict(
    "AncillarySourceSettingsTypeDef",
    {
        "Convert608To708": Literal["UPCONVERT", "DISABLED"],
        "SourceAncillaryChannelNumber": int,
        "TerminateCaptions": Literal["END_OF_INPUT", "DISABLED"],
    },
    total=False,
)

AudioChannelTaggingSettingsTypeDef = TypedDict(
    "AudioChannelTaggingSettingsTypeDef",
    {
        "ChannelTag": Literal[
            "L",
            "R",
            "C",
            "LFE",
            "LS",
            "RS",
            "LC",
            "RC",
            "CS",
            "LSD",
            "RSD",
            "TCS",
            "VHL",
            "VHC",
            "VHR",
        ]
    },
    total=False,
)

AudioCodecSettingsTypeDef = TypedDict(
    "AudioCodecSettingsTypeDef",
    {
        "AacSettings": "AacSettingsTypeDef",
        "Ac3Settings": "Ac3SettingsTypeDef",
        "AiffSettings": "AiffSettingsTypeDef",
        "Codec": Literal[
            "AAC",
            "MP2",
            "MP3",
            "WAV",
            "AIFF",
            "AC3",
            "EAC3",
            "EAC3_ATMOS",
            "VORBIS",
            "OPUS",
            "PASSTHROUGH",
        ],
        "Eac3AtmosSettings": "Eac3AtmosSettingsTypeDef",
        "Eac3Settings": "Eac3SettingsTypeDef",
        "Mp2Settings": "Mp2SettingsTypeDef",
        "Mp3Settings": "Mp3SettingsTypeDef",
        "OpusSettings": "OpusSettingsTypeDef",
        "VorbisSettings": "VorbisSettingsTypeDef",
        "WavSettings": "WavSettingsTypeDef",
    },
    total=False,
)

AudioDescriptionTypeDef = TypedDict(
    "AudioDescriptionTypeDef",
    {
        "AudioChannelTaggingSettings": "AudioChannelTaggingSettingsTypeDef",
        "AudioNormalizationSettings": "AudioNormalizationSettingsTypeDef",
        "AudioSourceName": str,
        "AudioType": int,
        "AudioTypeControl": Literal["FOLLOW_INPUT", "USE_CONFIGURED"],
        "CodecSettings": "AudioCodecSettingsTypeDef",
        "CustomLanguageCode": str,
        "LanguageCode": Literal[
            "ENG",
            "SPA",
            "FRA",
            "DEU",
            "GER",
            "ZHO",
            "ARA",
            "HIN",
            "JPN",
            "RUS",
            "POR",
            "ITA",
            "URD",
            "VIE",
            "KOR",
            "PAN",
            "ABK",
            "AAR",
            "AFR",
            "AKA",
            "SQI",
            "AMH",
            "ARG",
            "HYE",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAM",
            "BAK",
            "EUS",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOS",
            "BRE",
            "BUL",
            "MYA",
            "CAT",
            "KHM",
            "CHA",
            "CHE",
            "NYA",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "HRV",
            "CES",
            "DAN",
            "DIV",
            "NLD",
            "DZO",
            "ENM",
            "EPO",
            "EST",
            "EWE",
            "FAO",
            "FIJ",
            "FIN",
            "FRM",
            "FUL",
            "GLA",
            "GLG",
            "LUG",
            "KAT",
            "ELL",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HMO",
            "HUN",
            "ISL",
            "IDO",
            "IBO",
            "IND",
            "INA",
            "ILE",
            "IKU",
            "IPK",
            "GLE",
            "JAV",
            "KAL",
            "KAN",
            "KAU",
            "KAS",
            "KAZ",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LUB",
            "LTZ",
            "MKD",
            "MLG",
            "MSA",
            "MAL",
            "MLT",
            "GLV",
            "MRI",
            "MAR",
            "MAH",
            "MON",
            "NAU",
            "NAV",
            "NDE",
            "NBL",
            "NDO",
            "NEP",
            "SME",
            "NOR",
            "NOB",
            "NNO",
            "OCI",
            "OJI",
            "ORI",
            "ORM",
            "OSS",
            "PLI",
            "FAS",
            "POL",
            "PUS",
            "QUE",
            "QAA",
            "RON",
            "ROH",
            "RUN",
            "SMO",
            "SAG",
            "SAN",
            "SRD",
            "SRB",
            "SNA",
            "III",
            "SND",
            "SIN",
            "SLK",
            "SLV",
            "SOM",
            "SOT",
            "SUN",
            "SWA",
            "SSW",
            "SWE",
            "TGL",
            "TAH",
            "TGK",
            "TAM",
            "TAT",
            "TEL",
            "THA",
            "BOD",
            "TIR",
            "TON",
            "TSO",
            "TSN",
            "TUR",
            "TUK",
            "TWI",
            "UIG",
            "UKR",
            "UZB",
            "VEN",
            "VOL",
            "WLN",
            "CYM",
            "FRY",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZUL",
            "ORJ",
            "QPC",
            "TNG",
        ],
        "LanguageCodeControl": Literal["FOLLOW_INPUT", "USE_CONFIGURED"],
        "RemixSettings": "RemixSettingsTypeDef",
        "StreamName": str,
    },
    total=False,
)

AudioNormalizationSettingsTypeDef = TypedDict(
    "AudioNormalizationSettingsTypeDef",
    {
        "Algorithm": Literal["ITU_BS_1770_1", "ITU_BS_1770_2", "ITU_BS_1770_3", "ITU_BS_1770_4"],
        "AlgorithmControl": Literal["CORRECT_AUDIO", "MEASURE_ONLY"],
        "CorrectionGateLevel": int,
        "LoudnessLogging": Literal["LOG", "DONT_LOG"],
        "PeakCalculation": Literal["TRUE_PEAK", "NONE"],
        "TargetLkfs": float,
    },
    total=False,
)

AudioSelectorGroupTypeDef = TypedDict(
    "AudioSelectorGroupTypeDef", {"AudioSelectorNames": List[str]}, total=False
)

AudioSelectorTypeDef = TypedDict(
    "AudioSelectorTypeDef",
    {
        "CustomLanguageCode": str,
        "DefaultSelection": Literal["DEFAULT", "NOT_DEFAULT"],
        "ExternalAudioFileInput": str,
        "LanguageCode": Literal[
            "ENG",
            "SPA",
            "FRA",
            "DEU",
            "GER",
            "ZHO",
            "ARA",
            "HIN",
            "JPN",
            "RUS",
            "POR",
            "ITA",
            "URD",
            "VIE",
            "KOR",
            "PAN",
            "ABK",
            "AAR",
            "AFR",
            "AKA",
            "SQI",
            "AMH",
            "ARG",
            "HYE",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAM",
            "BAK",
            "EUS",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOS",
            "BRE",
            "BUL",
            "MYA",
            "CAT",
            "KHM",
            "CHA",
            "CHE",
            "NYA",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "HRV",
            "CES",
            "DAN",
            "DIV",
            "NLD",
            "DZO",
            "ENM",
            "EPO",
            "EST",
            "EWE",
            "FAO",
            "FIJ",
            "FIN",
            "FRM",
            "FUL",
            "GLA",
            "GLG",
            "LUG",
            "KAT",
            "ELL",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HMO",
            "HUN",
            "ISL",
            "IDO",
            "IBO",
            "IND",
            "INA",
            "ILE",
            "IKU",
            "IPK",
            "GLE",
            "JAV",
            "KAL",
            "KAN",
            "KAU",
            "KAS",
            "KAZ",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LUB",
            "LTZ",
            "MKD",
            "MLG",
            "MSA",
            "MAL",
            "MLT",
            "GLV",
            "MRI",
            "MAR",
            "MAH",
            "MON",
            "NAU",
            "NAV",
            "NDE",
            "NBL",
            "NDO",
            "NEP",
            "SME",
            "NOR",
            "NOB",
            "NNO",
            "OCI",
            "OJI",
            "ORI",
            "ORM",
            "OSS",
            "PLI",
            "FAS",
            "POL",
            "PUS",
            "QUE",
            "QAA",
            "RON",
            "ROH",
            "RUN",
            "SMO",
            "SAG",
            "SAN",
            "SRD",
            "SRB",
            "SNA",
            "III",
            "SND",
            "SIN",
            "SLK",
            "SLV",
            "SOM",
            "SOT",
            "SUN",
            "SWA",
            "SSW",
            "SWE",
            "TGL",
            "TAH",
            "TGK",
            "TAM",
            "TAT",
            "TEL",
            "THA",
            "BOD",
            "TIR",
            "TON",
            "TSO",
            "TSN",
            "TUR",
            "TUK",
            "TWI",
            "UIG",
            "UKR",
            "UZB",
            "VEN",
            "VOL",
            "WLN",
            "CYM",
            "FRY",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZUL",
            "ORJ",
            "QPC",
            "TNG",
        ],
        "Offset": int,
        "Pids": List[int],
        "ProgramSelection": int,
        "RemixSettings": "RemixSettingsTypeDef",
        "SelectorType": Literal["PID", "TRACK", "LANGUAGE_CODE"],
        "Tracks": List[int],
    },
    total=False,
)

AutomatedAbrSettingsTypeDef = TypedDict(
    "AutomatedAbrSettingsTypeDef",
    {"MaxAbrBitrate": int, "MaxRenditions": int, "MinAbrBitrate": int},
    total=False,
)

AutomatedEncodingSettingsTypeDef = TypedDict(
    "AutomatedEncodingSettingsTypeDef", {"AbrSettings": "AutomatedAbrSettingsTypeDef"}, total=False
)

Av1QvbrSettingsTypeDef = TypedDict(
    "Av1QvbrSettingsTypeDef",
    {"QvbrQualityLevel": int, "QvbrQualityLevelFineTune": float},
    total=False,
)

Av1SettingsTypeDef = TypedDict(
    "Av1SettingsTypeDef",
    {
        "AdaptiveQuantization": Literal["OFF", "LOW", "MEDIUM", "HIGH", "HIGHER", "MAX"],
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopSize": float,
        "MaxBitrate": int,
        "NumberBFramesBetweenReferenceFrames": int,
        "QvbrSettings": "Av1QvbrSettingsTypeDef",
        "RateControlMode": Literal["QVBR"],
        "Slices": int,
        "SpatialAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
    },
    total=False,
)

AvailBlankingTypeDef = TypedDict("AvailBlankingTypeDef", {"AvailBlankingImage": str}, total=False)

AvcIntraSettingsTypeDef = TypedDict(
    "AvcIntraSettingsTypeDef",
    {
        "AvcIntraClass": Literal["CLASS_50", "CLASS_100", "CLASS_200", "CLASS_4K_2K"],
        "AvcIntraUhdSettings": "AvcIntraUhdSettingsTypeDef",
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "InterlaceMode": Literal[
            "PROGRESSIVE", "TOP_FIELD", "BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "FOLLOW_BOTTOM_FIELD"
        ],
        "ScanTypeConversionMode": Literal["INTERLACED", "INTERLACED_OPTIMIZE"],
        "SlowPal": Literal["DISABLED", "ENABLED"],
        "Telecine": Literal["NONE", "HARD"],
    },
    total=False,
)

AvcIntraUhdSettingsTypeDef = TypedDict(
    "AvcIntraUhdSettingsTypeDef",
    {"QualityTuningLevel": Literal["SINGLE_PASS", "MULTI_PASS"]},
    total=False,
)

BurninDestinationSettingsTypeDef = TypedDict(
    "BurninDestinationSettingsTypeDef",
    {
        "Alignment": Literal["CENTERED", "LEFT"],
        "BackgroundColor": Literal["NONE", "BLACK", "WHITE"],
        "BackgroundOpacity": int,
        "FontColor": Literal["WHITE", "BLACK", "YELLOW", "RED", "GREEN", "BLUE"],
        "FontOpacity": int,
        "FontResolution": int,
        "FontScript": Literal["AUTOMATIC", "HANS", "HANT"],
        "FontSize": int,
        "OutlineColor": Literal["BLACK", "WHITE", "YELLOW", "RED", "GREEN", "BLUE"],
        "OutlineSize": int,
        "ShadowColor": Literal["NONE", "BLACK", "WHITE"],
        "ShadowOpacity": int,
        "ShadowXOffset": int,
        "ShadowYOffset": int,
        "TeletextSpacing": Literal["FIXED_GRID", "PROPORTIONAL"],
        "XPosition": int,
        "YPosition": int,
    },
    total=False,
)

CaptionDescriptionPresetTypeDef = TypedDict(
    "CaptionDescriptionPresetTypeDef",
    {
        "CustomLanguageCode": str,
        "DestinationSettings": "CaptionDestinationSettingsTypeDef",
        "LanguageCode": Literal[
            "ENG",
            "SPA",
            "FRA",
            "DEU",
            "GER",
            "ZHO",
            "ARA",
            "HIN",
            "JPN",
            "RUS",
            "POR",
            "ITA",
            "URD",
            "VIE",
            "KOR",
            "PAN",
            "ABK",
            "AAR",
            "AFR",
            "AKA",
            "SQI",
            "AMH",
            "ARG",
            "HYE",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAM",
            "BAK",
            "EUS",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOS",
            "BRE",
            "BUL",
            "MYA",
            "CAT",
            "KHM",
            "CHA",
            "CHE",
            "NYA",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "HRV",
            "CES",
            "DAN",
            "DIV",
            "NLD",
            "DZO",
            "ENM",
            "EPO",
            "EST",
            "EWE",
            "FAO",
            "FIJ",
            "FIN",
            "FRM",
            "FUL",
            "GLA",
            "GLG",
            "LUG",
            "KAT",
            "ELL",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HMO",
            "HUN",
            "ISL",
            "IDO",
            "IBO",
            "IND",
            "INA",
            "ILE",
            "IKU",
            "IPK",
            "GLE",
            "JAV",
            "KAL",
            "KAN",
            "KAU",
            "KAS",
            "KAZ",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LUB",
            "LTZ",
            "MKD",
            "MLG",
            "MSA",
            "MAL",
            "MLT",
            "GLV",
            "MRI",
            "MAR",
            "MAH",
            "MON",
            "NAU",
            "NAV",
            "NDE",
            "NBL",
            "NDO",
            "NEP",
            "SME",
            "NOR",
            "NOB",
            "NNO",
            "OCI",
            "OJI",
            "ORI",
            "ORM",
            "OSS",
            "PLI",
            "FAS",
            "POL",
            "PUS",
            "QUE",
            "QAA",
            "RON",
            "ROH",
            "RUN",
            "SMO",
            "SAG",
            "SAN",
            "SRD",
            "SRB",
            "SNA",
            "III",
            "SND",
            "SIN",
            "SLK",
            "SLV",
            "SOM",
            "SOT",
            "SUN",
            "SWA",
            "SSW",
            "SWE",
            "TGL",
            "TAH",
            "TGK",
            "TAM",
            "TAT",
            "TEL",
            "THA",
            "BOD",
            "TIR",
            "TON",
            "TSO",
            "TSN",
            "TUR",
            "TUK",
            "TWI",
            "UIG",
            "UKR",
            "UZB",
            "VEN",
            "VOL",
            "WLN",
            "CYM",
            "FRY",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZUL",
            "ORJ",
            "QPC",
            "TNG",
        ],
        "LanguageDescription": str,
    },
    total=False,
)

CaptionDescriptionTypeDef = TypedDict(
    "CaptionDescriptionTypeDef",
    {
        "CaptionSelectorName": str,
        "CustomLanguageCode": str,
        "DestinationSettings": "CaptionDestinationSettingsTypeDef",
        "LanguageCode": Literal[
            "ENG",
            "SPA",
            "FRA",
            "DEU",
            "GER",
            "ZHO",
            "ARA",
            "HIN",
            "JPN",
            "RUS",
            "POR",
            "ITA",
            "URD",
            "VIE",
            "KOR",
            "PAN",
            "ABK",
            "AAR",
            "AFR",
            "AKA",
            "SQI",
            "AMH",
            "ARG",
            "HYE",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAM",
            "BAK",
            "EUS",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOS",
            "BRE",
            "BUL",
            "MYA",
            "CAT",
            "KHM",
            "CHA",
            "CHE",
            "NYA",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "HRV",
            "CES",
            "DAN",
            "DIV",
            "NLD",
            "DZO",
            "ENM",
            "EPO",
            "EST",
            "EWE",
            "FAO",
            "FIJ",
            "FIN",
            "FRM",
            "FUL",
            "GLA",
            "GLG",
            "LUG",
            "KAT",
            "ELL",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HMO",
            "HUN",
            "ISL",
            "IDO",
            "IBO",
            "IND",
            "INA",
            "ILE",
            "IKU",
            "IPK",
            "GLE",
            "JAV",
            "KAL",
            "KAN",
            "KAU",
            "KAS",
            "KAZ",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LUB",
            "LTZ",
            "MKD",
            "MLG",
            "MSA",
            "MAL",
            "MLT",
            "GLV",
            "MRI",
            "MAR",
            "MAH",
            "MON",
            "NAU",
            "NAV",
            "NDE",
            "NBL",
            "NDO",
            "NEP",
            "SME",
            "NOR",
            "NOB",
            "NNO",
            "OCI",
            "OJI",
            "ORI",
            "ORM",
            "OSS",
            "PLI",
            "FAS",
            "POL",
            "PUS",
            "QUE",
            "QAA",
            "RON",
            "ROH",
            "RUN",
            "SMO",
            "SAG",
            "SAN",
            "SRD",
            "SRB",
            "SNA",
            "III",
            "SND",
            "SIN",
            "SLK",
            "SLV",
            "SOM",
            "SOT",
            "SUN",
            "SWA",
            "SSW",
            "SWE",
            "TGL",
            "TAH",
            "TGK",
            "TAM",
            "TAT",
            "TEL",
            "THA",
            "BOD",
            "TIR",
            "TON",
            "TSO",
            "TSN",
            "TUR",
            "TUK",
            "TWI",
            "UIG",
            "UKR",
            "UZB",
            "VEN",
            "VOL",
            "WLN",
            "CYM",
            "FRY",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZUL",
            "ORJ",
            "QPC",
            "TNG",
        ],
        "LanguageDescription": str,
    },
    total=False,
)

CaptionDestinationSettingsTypeDef = TypedDict(
    "CaptionDestinationSettingsTypeDef",
    {
        "BurninDestinationSettings": "BurninDestinationSettingsTypeDef",
        "DestinationType": Literal[
            "BURN_IN",
            "DVB_SUB",
            "EMBEDDED",
            "EMBEDDED_PLUS_SCTE20",
            "IMSC",
            "SCTE20_PLUS_EMBEDDED",
            "SCC",
            "SRT",
            "SMI",
            "TELETEXT",
            "TTML",
            "WEBVTT",
        ],
        "DvbSubDestinationSettings": "DvbSubDestinationSettingsTypeDef",
        "EmbeddedDestinationSettings": "EmbeddedDestinationSettingsTypeDef",
        "ImscDestinationSettings": "ImscDestinationSettingsTypeDef",
        "SccDestinationSettings": "SccDestinationSettingsTypeDef",
        "TeletextDestinationSettings": "TeletextDestinationSettingsTypeDef",
        "TtmlDestinationSettings": "TtmlDestinationSettingsTypeDef",
    },
    total=False,
)

CaptionSelectorTypeDef = TypedDict(
    "CaptionSelectorTypeDef",
    {
        "CustomLanguageCode": str,
        "LanguageCode": Literal[
            "ENG",
            "SPA",
            "FRA",
            "DEU",
            "GER",
            "ZHO",
            "ARA",
            "HIN",
            "JPN",
            "RUS",
            "POR",
            "ITA",
            "URD",
            "VIE",
            "KOR",
            "PAN",
            "ABK",
            "AAR",
            "AFR",
            "AKA",
            "SQI",
            "AMH",
            "ARG",
            "HYE",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAM",
            "BAK",
            "EUS",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOS",
            "BRE",
            "BUL",
            "MYA",
            "CAT",
            "KHM",
            "CHA",
            "CHE",
            "NYA",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "HRV",
            "CES",
            "DAN",
            "DIV",
            "NLD",
            "DZO",
            "ENM",
            "EPO",
            "EST",
            "EWE",
            "FAO",
            "FIJ",
            "FIN",
            "FRM",
            "FUL",
            "GLA",
            "GLG",
            "LUG",
            "KAT",
            "ELL",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HMO",
            "HUN",
            "ISL",
            "IDO",
            "IBO",
            "IND",
            "INA",
            "ILE",
            "IKU",
            "IPK",
            "GLE",
            "JAV",
            "KAL",
            "KAN",
            "KAU",
            "KAS",
            "KAZ",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LUB",
            "LTZ",
            "MKD",
            "MLG",
            "MSA",
            "MAL",
            "MLT",
            "GLV",
            "MRI",
            "MAR",
            "MAH",
            "MON",
            "NAU",
            "NAV",
            "NDE",
            "NBL",
            "NDO",
            "NEP",
            "SME",
            "NOR",
            "NOB",
            "NNO",
            "OCI",
            "OJI",
            "ORI",
            "ORM",
            "OSS",
            "PLI",
            "FAS",
            "POL",
            "PUS",
            "QUE",
            "QAA",
            "RON",
            "ROH",
            "RUN",
            "SMO",
            "SAG",
            "SAN",
            "SRD",
            "SRB",
            "SNA",
            "III",
            "SND",
            "SIN",
            "SLK",
            "SLV",
            "SOM",
            "SOT",
            "SUN",
            "SWA",
            "SSW",
            "SWE",
            "TGL",
            "TAH",
            "TGK",
            "TAM",
            "TAT",
            "TEL",
            "THA",
            "BOD",
            "TIR",
            "TON",
            "TSO",
            "TSN",
            "TUR",
            "TUK",
            "TWI",
            "UIG",
            "UKR",
            "UZB",
            "VEN",
            "VOL",
            "WLN",
            "CYM",
            "FRY",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZUL",
            "ORJ",
            "QPC",
            "TNG",
        ],
        "SourceSettings": "CaptionSourceSettingsTypeDef",
    },
    total=False,
)

CaptionSourceFramerateTypeDef = TypedDict(
    "CaptionSourceFramerateTypeDef",
    {"FramerateDenominator": int, "FramerateNumerator": int},
    total=False,
)

CaptionSourceSettingsTypeDef = TypedDict(
    "CaptionSourceSettingsTypeDef",
    {
        "AncillarySourceSettings": "AncillarySourceSettingsTypeDef",
        "DvbSubSourceSettings": "DvbSubSourceSettingsTypeDef",
        "EmbeddedSourceSettings": "EmbeddedSourceSettingsTypeDef",
        "FileSourceSettings": "FileSourceSettingsTypeDef",
        "SourceType": Literal[
            "ANCILLARY",
            "DVB_SUB",
            "EMBEDDED",
            "SCTE20",
            "SCC",
            "TTML",
            "STL",
            "SRT",
            "SMI",
            "SMPTE_TT",
            "TELETEXT",
            "NULL_SOURCE",
            "IMSC",
        ],
        "TeletextSourceSettings": "TeletextSourceSettingsTypeDef",
        "TrackSourceSettings": "TrackSourceSettingsTypeDef",
    },
    total=False,
)

ChannelMappingTypeDef = TypedDict(
    "ChannelMappingTypeDef", {"OutputChannels": List["OutputChannelMappingTypeDef"]}, total=False
)

CmafAdditionalManifestTypeDef = TypedDict(
    "CmafAdditionalManifestTypeDef",
    {"ManifestNameModifier": str, "SelectedOutputs": List[str]},
    total=False,
)

CmafEncryptionSettingsTypeDef = TypedDict(
    "CmafEncryptionSettingsTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["SAMPLE_AES", "AES_CTR"],
        "InitializationVectorInManifest": Literal["INCLUDE", "EXCLUDE"],
        "SpekeKeyProvider": "SpekeKeyProviderCmafTypeDef",
        "StaticKeyProvider": "StaticKeyProviderTypeDef",
        "Type": Literal["SPEKE", "STATIC_KEY"],
    },
    total=False,
)

CmafGroupSettingsTypeDef = TypedDict(
    "CmafGroupSettingsTypeDef",
    {
        "AdditionalManifests": List["CmafAdditionalManifestTypeDef"],
        "BaseUrl": str,
        "ClientCache": Literal["DISABLED", "ENABLED"],
        "CodecSpecification": Literal["RFC_6381", "RFC_4281"],
        "Destination": str,
        "DestinationSettings": "DestinationSettingsTypeDef",
        "Encryption": "CmafEncryptionSettingsTypeDef",
        "FragmentLength": int,
        "ManifestCompression": Literal["GZIP", "NONE"],
        "ManifestDurationFormat": Literal["FLOATING_POINT", "INTEGER"],
        "MinBufferTime": int,
        "MinFinalSegmentLength": float,
        "MpdProfile": Literal["MAIN_PROFILE", "ON_DEMAND_PROFILE"],
        "SegmentControl": Literal["SINGLE_FILE", "SEGMENTED_FILES"],
        "SegmentLength": int,
        "StreamInfResolution": Literal["INCLUDE", "EXCLUDE"],
        "WriteDashManifest": Literal["DISABLED", "ENABLED"],
        "WriteHlsManifest": Literal["DISABLED", "ENABLED"],
        "WriteSegmentTimelineInRepresentation": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

CmfcSettingsTypeDef = TypedDict(
    "CmfcSettingsTypeDef",
    {
        "AudioDuration": Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"],
        "IFrameOnlyManifest": Literal["INCLUDE", "EXCLUDE"],
        "Scte35Esam": Literal["INSERT", "NONE"],
        "Scte35Source": Literal["PASSTHROUGH", "NONE"],
    },
    total=False,
)

ColorCorrectorTypeDef = TypedDict(
    "ColorCorrectorTypeDef",
    {
        "Brightness": int,
        "ColorSpaceConversion": Literal[
            "NONE", "FORCE_601", "FORCE_709", "FORCE_HDR10", "FORCE_HLG_2020"
        ],
        "Contrast": int,
        "Hdr10Metadata": "Hdr10MetadataTypeDef",
        "Hue": int,
        "Saturation": int,
    },
    total=False,
)

ContainerSettingsTypeDef = TypedDict(
    "ContainerSettingsTypeDef",
    {
        "CmfcSettings": "CmfcSettingsTypeDef",
        "Container": Literal[
            "F4V", "ISMV", "M2TS", "M3U8", "CMFC", "MOV", "MP4", "MPD", "MXF", "WEBM", "RAW"
        ],
        "F4vSettings": "F4vSettingsTypeDef",
        "M2tsSettings": "M2tsSettingsTypeDef",
        "M3u8Settings": "M3u8SettingsTypeDef",
        "MovSettings": "MovSettingsTypeDef",
        "Mp4Settings": "Mp4SettingsTypeDef",
        "MpdSettings": "MpdSettingsTypeDef",
        "MxfSettings": "MxfSettingsTypeDef",
    },
    total=False,
)

DashAdditionalManifestTypeDef = TypedDict(
    "DashAdditionalManifestTypeDef",
    {"ManifestNameModifier": str, "SelectedOutputs": List[str]},
    total=False,
)

DashIsoEncryptionSettingsTypeDef = TypedDict(
    "DashIsoEncryptionSettingsTypeDef",
    {
        "PlaybackDeviceCompatibility": Literal["CENC_V1", "UNENCRYPTED_SEI"],
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
    total=False,
)

DashIsoGroupSettingsTypeDef = TypedDict(
    "DashIsoGroupSettingsTypeDef",
    {
        "AdditionalManifests": List["DashAdditionalManifestTypeDef"],
        "BaseUrl": str,
        "Destination": str,
        "DestinationSettings": "DestinationSettingsTypeDef",
        "Encryption": "DashIsoEncryptionSettingsTypeDef",
        "FragmentLength": int,
        "HbbtvCompliance": Literal["HBBTV_1_5", "NONE"],
        "MinBufferTime": int,
        "MinFinalSegmentLength": float,
        "MpdProfile": Literal["MAIN_PROFILE", "ON_DEMAND_PROFILE"],
        "SegmentControl": Literal["SINGLE_FILE", "SEGMENTED_FILES"],
        "SegmentLength": int,
        "WriteSegmentTimelineInRepresentation": Literal["ENABLED", "DISABLED"],
    },
    total=False,
)

DeinterlacerTypeDef = TypedDict(
    "DeinterlacerTypeDef",
    {
        "Algorithm": Literal["INTERPOLATE", "INTERPOLATE_TICKER", "BLEND", "BLEND_TICKER"],
        "Control": Literal["FORCE_ALL_FRAMES", "NORMAL"],
        "Mode": Literal["DEINTERLACE", "INVERSE_TELECINE", "ADAPTIVE"],
    },
    total=False,
)

DestinationSettingsTypeDef = TypedDict(
    "DestinationSettingsTypeDef", {"S3Settings": "S3DestinationSettingsTypeDef"}, total=False
)

DolbyVisionLevel6MetadataTypeDef = TypedDict(
    "DolbyVisionLevel6MetadataTypeDef", {"MaxCll": int, "MaxFall": int}, total=False
)

DolbyVisionTypeDef = TypedDict(
    "DolbyVisionTypeDef",
    {
        "L6Metadata": "DolbyVisionLevel6MetadataTypeDef",
        "L6Mode": Literal["PASSTHROUGH", "RECALCULATE", "SPECIFY"],
        "Profile": Literal["PROFILE_5"],
    },
    total=False,
)

DvbNitSettingsTypeDef = TypedDict(
    "DvbNitSettingsTypeDef", {"NetworkId": int, "NetworkName": str, "NitInterval": int}, total=False
)

DvbSdtSettingsTypeDef = TypedDict(
    "DvbSdtSettingsTypeDef",
    {
        "OutputSdt": Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"],
        "SdtInterval": int,
        "ServiceName": str,
        "ServiceProviderName": str,
    },
    total=False,
)

DvbSubDestinationSettingsTypeDef = TypedDict(
    "DvbSubDestinationSettingsTypeDef",
    {
        "Alignment": Literal["CENTERED", "LEFT"],
        "BackgroundColor": Literal["NONE", "BLACK", "WHITE"],
        "BackgroundOpacity": int,
        "FontColor": Literal["WHITE", "BLACK", "YELLOW", "RED", "GREEN", "BLUE"],
        "FontOpacity": int,
        "FontResolution": int,
        "FontScript": Literal["AUTOMATIC", "HANS", "HANT"],
        "FontSize": int,
        "OutlineColor": Literal["BLACK", "WHITE", "YELLOW", "RED", "GREEN", "BLUE"],
        "OutlineSize": int,
        "ShadowColor": Literal["NONE", "BLACK", "WHITE"],
        "ShadowOpacity": int,
        "ShadowXOffset": int,
        "ShadowYOffset": int,
        "SubtitlingType": Literal["HEARING_IMPAIRED", "STANDARD"],
        "TeletextSpacing": Literal["FIXED_GRID", "PROPORTIONAL"],
        "XPosition": int,
        "YPosition": int,
    },
    total=False,
)

DvbSubSourceSettingsTypeDef = TypedDict("DvbSubSourceSettingsTypeDef", {"Pid": int}, total=False)

DvbTdtSettingsTypeDef = TypedDict("DvbTdtSettingsTypeDef", {"TdtInterval": int}, total=False)

Eac3AtmosSettingsTypeDef = TypedDict(
    "Eac3AtmosSettingsTypeDef",
    {
        "Bitrate": int,
        "BitstreamMode": Literal["COMPLETE_MAIN"],
        "CodingMode": Literal["CODING_MODE_9_1_6"],
        "DialogueIntelligence": Literal["ENABLED", "DISABLED"],
        "DynamicRangeCompressionLine": Literal[
            "NONE", "FILM_STANDARD", "FILM_LIGHT", "MUSIC_STANDARD", "MUSIC_LIGHT", "SPEECH"
        ],
        "DynamicRangeCompressionRf": Literal[
            "NONE", "FILM_STANDARD", "FILM_LIGHT", "MUSIC_STANDARD", "MUSIC_LIGHT", "SPEECH"
        ],
        "LoRoCenterMixLevel": float,
        "LoRoSurroundMixLevel": float,
        "LtRtCenterMixLevel": float,
        "LtRtSurroundMixLevel": float,
        "MeteringMode": Literal[
            "LEQ_A", "ITU_BS_1770_1", "ITU_BS_1770_2", "ITU_BS_1770_3", "ITU_BS_1770_4"
        ],
        "SampleRate": int,
        "SpeechThreshold": int,
        "StereoDownmix": Literal["NOT_INDICATED", "STEREO", "SURROUND", "DPL2"],
        "SurroundExMode": Literal["NOT_INDICATED", "ENABLED", "DISABLED"],
    },
    total=False,
)

Eac3SettingsTypeDef = TypedDict(
    "Eac3SettingsTypeDef",
    {
        "AttenuationControl": Literal["ATTENUATE_3_DB", "NONE"],
        "Bitrate": int,
        "BitstreamMode": Literal[
            "COMPLETE_MAIN", "COMMENTARY", "EMERGENCY", "HEARING_IMPAIRED", "VISUALLY_IMPAIRED"
        ],
        "CodingMode": Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"],
        "DcFilter": Literal["ENABLED", "DISABLED"],
        "Dialnorm": int,
        "DynamicRangeCompressionLine": Literal[
            "NONE", "FILM_STANDARD", "FILM_LIGHT", "MUSIC_STANDARD", "MUSIC_LIGHT", "SPEECH"
        ],
        "DynamicRangeCompressionRf": Literal[
            "NONE", "FILM_STANDARD", "FILM_LIGHT", "MUSIC_STANDARD", "MUSIC_LIGHT", "SPEECH"
        ],
        "LfeControl": Literal["LFE", "NO_LFE"],
        "LfeFilter": Literal["ENABLED", "DISABLED"],
        "LoRoCenterMixLevel": float,
        "LoRoSurroundMixLevel": float,
        "LtRtCenterMixLevel": float,
        "LtRtSurroundMixLevel": float,
        "MetadataControl": Literal["FOLLOW_INPUT", "USE_CONFIGURED"],
        "PassthroughControl": Literal["WHEN_POSSIBLE", "NO_PASSTHROUGH"],
        "PhaseControl": Literal["SHIFT_90_DEGREES", "NO_SHIFT"],
        "SampleRate": int,
        "StereoDownmix": Literal["NOT_INDICATED", "LO_RO", "LT_RT", "DPL2"],
        "SurroundExMode": Literal["NOT_INDICATED", "ENABLED", "DISABLED"],
        "SurroundMode": Literal["NOT_INDICATED", "ENABLED", "DISABLED"],
    },
    total=False,
)

EmbeddedDestinationSettingsTypeDef = TypedDict(
    "EmbeddedDestinationSettingsTypeDef",
    {"Destination608ChannelNumber": int, "Destination708ServiceNumber": int},
    total=False,
)

EmbeddedSourceSettingsTypeDef = TypedDict(
    "EmbeddedSourceSettingsTypeDef",
    {
        "Convert608To708": Literal["UPCONVERT", "DISABLED"],
        "Source608ChannelNumber": int,
        "Source608TrackNumber": int,
        "TerminateCaptions": Literal["END_OF_INPUT", "DISABLED"],
    },
    total=False,
)

EndpointTypeDef = TypedDict("EndpointTypeDef", {"Url": str}, total=False)

EsamManifestConfirmConditionNotificationTypeDef = TypedDict(
    "EsamManifestConfirmConditionNotificationTypeDef", {"MccXml": str}, total=False
)

EsamSettingsTypeDef = TypedDict(
    "EsamSettingsTypeDef",
    {
        "ManifestConfirmConditionNotification": "EsamManifestConfirmConditionNotificationTypeDef",
        "ResponseSignalPreroll": int,
        "SignalProcessingNotification": "EsamSignalProcessingNotificationTypeDef",
    },
    total=False,
)

EsamSignalProcessingNotificationTypeDef = TypedDict(
    "EsamSignalProcessingNotificationTypeDef", {"SccXml": str}, total=False
)

F4vSettingsTypeDef = TypedDict(
    "F4vSettingsTypeDef", {"MoovPlacement": Literal["PROGRESSIVE_DOWNLOAD", "NORMAL"]}, total=False
)

FileGroupSettingsTypeDef = TypedDict(
    "FileGroupSettingsTypeDef",
    {"Destination": str, "DestinationSettings": "DestinationSettingsTypeDef"},
    total=False,
)

FileSourceSettingsTypeDef = TypedDict(
    "FileSourceSettingsTypeDef",
    {
        "Convert608To708": Literal["UPCONVERT", "DISABLED"],
        "Framerate": "CaptionSourceFramerateTypeDef",
        "SourceFile": str,
        "TimeDelta": int,
    },
    total=False,
)

FrameCaptureSettingsTypeDef = TypedDict(
    "FrameCaptureSettingsTypeDef",
    {"FramerateDenominator": int, "FramerateNumerator": int, "MaxCaptures": int, "Quality": int},
    total=False,
)

H264QvbrSettingsTypeDef = TypedDict(
    "H264QvbrSettingsTypeDef",
    {"MaxAverageBitrate": int, "QvbrQualityLevel": int, "QvbrQualityLevelFineTune": float},
    total=False,
)

H264SettingsTypeDef = TypedDict(
    "H264SettingsTypeDef",
    {
        "AdaptiveQuantization": Literal["OFF", "AUTO", "LOW", "MEDIUM", "HIGH", "HIGHER", "MAX"],
        "Bitrate": int,
        "CodecLevel": Literal[
            "AUTO",
            "LEVEL_1",
            "LEVEL_1_1",
            "LEVEL_1_2",
            "LEVEL_1_3",
            "LEVEL_2",
            "LEVEL_2_1",
            "LEVEL_2_2",
            "LEVEL_3",
            "LEVEL_3_1",
            "LEVEL_3_2",
            "LEVEL_4",
            "LEVEL_4_1",
            "LEVEL_4_2",
            "LEVEL_5",
            "LEVEL_5_1",
            "LEVEL_5_2",
        ],
        "CodecProfile": Literal[
            "BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"
        ],
        "DynamicSubGop": Literal["ADAPTIVE", "STATIC"],
        "EntropyEncoding": Literal["CABAC", "CAVLC"],
        "FieldEncoding": Literal["PAFF", "FORCE_FIELD"],
        "FlickerAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopBReference": Literal["DISABLED", "ENABLED"],
        "GopClosedCadence": int,
        "GopSize": float,
        "GopSizeUnits": Literal["FRAMES", "SECONDS"],
        "HrdBufferInitialFillPercentage": int,
        "HrdBufferSize": int,
        "InterlaceMode": Literal[
            "PROGRESSIVE", "TOP_FIELD", "BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "FOLLOW_BOTTOM_FIELD"
        ],
        "MaxBitrate": int,
        "MinIInterval": int,
        "NumberBFramesBetweenReferenceFrames": int,
        "NumberReferenceFrames": int,
        "ParControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": Literal["SINGLE_PASS", "SINGLE_PASS_HQ", "MULTI_PASS_HQ"],
        "QvbrSettings": "H264QvbrSettingsTypeDef",
        "RateControlMode": Literal["VBR", "CBR", "QVBR"],
        "RepeatPps": Literal["DISABLED", "ENABLED"],
        "ScanTypeConversionMode": Literal["INTERLACED", "INTERLACED_OPTIMIZE"],
        "SceneChangeDetect": Literal["DISABLED", "ENABLED", "TRANSITION_DETECTION"],
        "Slices": int,
        "SlowPal": Literal["DISABLED", "ENABLED"],
        "Softness": int,
        "SpatialAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
        "Syntax": Literal["DEFAULT", "RP2027"],
        "Telecine": Literal["NONE", "SOFT", "HARD"],
        "TemporalAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
        "UnregisteredSeiTimecode": Literal["DISABLED", "ENABLED"],
    },
    total=False,
)

H265QvbrSettingsTypeDef = TypedDict(
    "H265QvbrSettingsTypeDef",
    {"MaxAverageBitrate": int, "QvbrQualityLevel": int, "QvbrQualityLevelFineTune": float},
    total=False,
)

H265SettingsTypeDef = TypedDict(
    "H265SettingsTypeDef",
    {
        "AdaptiveQuantization": Literal["OFF", "LOW", "MEDIUM", "HIGH", "HIGHER", "MAX"],
        "AlternateTransferFunctionSei": Literal["DISABLED", "ENABLED"],
        "Bitrate": int,
        "CodecLevel": Literal[
            "AUTO",
            "LEVEL_1",
            "LEVEL_2",
            "LEVEL_2_1",
            "LEVEL_3",
            "LEVEL_3_1",
            "LEVEL_4",
            "LEVEL_4_1",
            "LEVEL_5",
            "LEVEL_5_1",
            "LEVEL_5_2",
            "LEVEL_6",
            "LEVEL_6_1",
            "LEVEL_6_2",
        ],
        "CodecProfile": Literal[
            "MAIN_MAIN",
            "MAIN_HIGH",
            "MAIN10_MAIN",
            "MAIN10_HIGH",
            "MAIN_422_8BIT_MAIN",
            "MAIN_422_8BIT_HIGH",
            "MAIN_422_10BIT_MAIN",
            "MAIN_422_10BIT_HIGH",
        ],
        "DynamicSubGop": Literal["ADAPTIVE", "STATIC"],
        "FlickerAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopBReference": Literal["DISABLED", "ENABLED"],
        "GopClosedCadence": int,
        "GopSize": float,
        "GopSizeUnits": Literal["FRAMES", "SECONDS"],
        "HrdBufferInitialFillPercentage": int,
        "HrdBufferSize": int,
        "InterlaceMode": Literal[
            "PROGRESSIVE", "TOP_FIELD", "BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "FOLLOW_BOTTOM_FIELD"
        ],
        "MaxBitrate": int,
        "MinIInterval": int,
        "NumberBFramesBetweenReferenceFrames": int,
        "NumberReferenceFrames": int,
        "ParControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": Literal["SINGLE_PASS", "SINGLE_PASS_HQ", "MULTI_PASS_HQ"],
        "QvbrSettings": "H265QvbrSettingsTypeDef",
        "RateControlMode": Literal["VBR", "CBR", "QVBR"],
        "SampleAdaptiveOffsetFilterMode": Literal["DEFAULT", "ADAPTIVE", "OFF"],
        "ScanTypeConversionMode": Literal["INTERLACED", "INTERLACED_OPTIMIZE"],
        "SceneChangeDetect": Literal["DISABLED", "ENABLED", "TRANSITION_DETECTION"],
        "Slices": int,
        "SlowPal": Literal["DISABLED", "ENABLED"],
        "SpatialAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
        "Telecine": Literal["NONE", "SOFT", "HARD"],
        "TemporalAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
        "TemporalIds": Literal["DISABLED", "ENABLED"],
        "Tiles": Literal["DISABLED", "ENABLED"],
        "UnregisteredSeiTimecode": Literal["DISABLED", "ENABLED"],
        "WriteMp4PackagingType": Literal["HVC1", "HEV1"],
    },
    total=False,
)

Hdr10MetadataTypeDef = TypedDict(
    "Hdr10MetadataTypeDef",
    {
        "BluePrimaryX": int,
        "BluePrimaryY": int,
        "GreenPrimaryX": int,
        "GreenPrimaryY": int,
        "MaxContentLightLevel": int,
        "MaxFrameAverageLightLevel": int,
        "MaxLuminance": int,
        "MinLuminance": int,
        "RedPrimaryX": int,
        "RedPrimaryY": int,
        "WhitePointX": int,
        "WhitePointY": int,
    },
    total=False,
)

HlsAdditionalManifestTypeDef = TypedDict(
    "HlsAdditionalManifestTypeDef",
    {"ManifestNameModifier": str, "SelectedOutputs": List[str]},
    total=False,
)

HlsCaptionLanguageMappingTypeDef = TypedDict(
    "HlsCaptionLanguageMappingTypeDef",
    {
        "CaptionChannel": int,
        "CustomLanguageCode": str,
        "LanguageCode": Literal[
            "ENG",
            "SPA",
            "FRA",
            "DEU",
            "GER",
            "ZHO",
            "ARA",
            "HIN",
            "JPN",
            "RUS",
            "POR",
            "ITA",
            "URD",
            "VIE",
            "KOR",
            "PAN",
            "ABK",
            "AAR",
            "AFR",
            "AKA",
            "SQI",
            "AMH",
            "ARG",
            "HYE",
            "ASM",
            "AVA",
            "AVE",
            "AYM",
            "AZE",
            "BAM",
            "BAK",
            "EUS",
            "BEL",
            "BEN",
            "BIH",
            "BIS",
            "BOS",
            "BRE",
            "BUL",
            "MYA",
            "CAT",
            "KHM",
            "CHA",
            "CHE",
            "NYA",
            "CHU",
            "CHV",
            "COR",
            "COS",
            "CRE",
            "HRV",
            "CES",
            "DAN",
            "DIV",
            "NLD",
            "DZO",
            "ENM",
            "EPO",
            "EST",
            "EWE",
            "FAO",
            "FIJ",
            "FIN",
            "FRM",
            "FUL",
            "GLA",
            "GLG",
            "LUG",
            "KAT",
            "ELL",
            "GRN",
            "GUJ",
            "HAT",
            "HAU",
            "HEB",
            "HER",
            "HMO",
            "HUN",
            "ISL",
            "IDO",
            "IBO",
            "IND",
            "INA",
            "ILE",
            "IKU",
            "IPK",
            "GLE",
            "JAV",
            "KAL",
            "KAN",
            "KAU",
            "KAS",
            "KAZ",
            "KIK",
            "KIN",
            "KIR",
            "KOM",
            "KON",
            "KUA",
            "KUR",
            "LAO",
            "LAT",
            "LAV",
            "LIM",
            "LIN",
            "LIT",
            "LUB",
            "LTZ",
            "MKD",
            "MLG",
            "MSA",
            "MAL",
            "MLT",
            "GLV",
            "MRI",
            "MAR",
            "MAH",
            "MON",
            "NAU",
            "NAV",
            "NDE",
            "NBL",
            "NDO",
            "NEP",
            "SME",
            "NOR",
            "NOB",
            "NNO",
            "OCI",
            "OJI",
            "ORI",
            "ORM",
            "OSS",
            "PLI",
            "FAS",
            "POL",
            "PUS",
            "QUE",
            "QAA",
            "RON",
            "ROH",
            "RUN",
            "SMO",
            "SAG",
            "SAN",
            "SRD",
            "SRB",
            "SNA",
            "III",
            "SND",
            "SIN",
            "SLK",
            "SLV",
            "SOM",
            "SOT",
            "SUN",
            "SWA",
            "SSW",
            "SWE",
            "TGL",
            "TAH",
            "TGK",
            "TAM",
            "TAT",
            "TEL",
            "THA",
            "BOD",
            "TIR",
            "TON",
            "TSO",
            "TSN",
            "TUR",
            "TUK",
            "TWI",
            "UIG",
            "UKR",
            "UZB",
            "VEN",
            "VOL",
            "WLN",
            "CYM",
            "FRY",
            "WOL",
            "XHO",
            "YID",
            "YOR",
            "ZHA",
            "ZUL",
            "ORJ",
            "QPC",
            "TNG",
        ],
        "LanguageDescription": str,
    },
    total=False,
)

HlsEncryptionSettingsTypeDef = TypedDict(
    "HlsEncryptionSettingsTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES128", "SAMPLE_AES"],
        "InitializationVectorInManifest": Literal["INCLUDE", "EXCLUDE"],
        "OfflineEncrypted": Literal["ENABLED", "DISABLED"],
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
        "StaticKeyProvider": "StaticKeyProviderTypeDef",
        "Type": Literal["SPEKE", "STATIC_KEY"],
    },
    total=False,
)

HlsGroupSettingsTypeDef = TypedDict(
    "HlsGroupSettingsTypeDef",
    {
        "AdMarkers": List[Literal["ELEMENTAL", "ELEMENTAL_SCTE35"]],
        "AdditionalManifests": List["HlsAdditionalManifestTypeDef"],
        "AudioOnlyHeader": Literal["INCLUDE", "EXCLUDE"],
        "BaseUrl": str,
        "CaptionLanguageMappings": List["HlsCaptionLanguageMappingTypeDef"],
        "CaptionLanguageSetting": Literal["INSERT", "OMIT", "NONE"],
        "ClientCache": Literal["DISABLED", "ENABLED"],
        "CodecSpecification": Literal["RFC_6381", "RFC_4281"],
        "Destination": str,
        "DestinationSettings": "DestinationSettingsTypeDef",
        "DirectoryStructure": Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"],
        "Encryption": "HlsEncryptionSettingsTypeDef",
        "ManifestCompression": Literal["GZIP", "NONE"],
        "ManifestDurationFormat": Literal["FLOATING_POINT", "INTEGER"],
        "MinFinalSegmentLength": float,
        "MinSegmentLength": int,
        "OutputSelection": Literal["MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY"],
        "ProgramDateTime": Literal["INCLUDE", "EXCLUDE"],
        "ProgramDateTimePeriod": int,
        "SegmentControl": Literal["SINGLE_FILE", "SEGMENTED_FILES"],
        "SegmentLength": int,
        "SegmentsPerSubdirectory": int,
        "StreamInfResolution": Literal["INCLUDE", "EXCLUDE"],
        "TimedMetadataId3Frame": Literal["NONE", "PRIV", "TDRL"],
        "TimedMetadataId3Period": int,
        "TimestampDeltaMilliseconds": int,
    },
    total=False,
)

HlsSettingsTypeDef = TypedDict(
    "HlsSettingsTypeDef",
    {
        "AudioGroupId": str,
        "AudioOnlyContainer": Literal["AUTOMATIC", "M2TS"],
        "AudioRenditionSets": str,
        "AudioTrackType": Literal[
            "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
            "ALTERNATE_AUDIO_AUTO_SELECT",
            "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
            "AUDIO_ONLY_VARIANT_STREAM",
        ],
        "IFrameOnlyManifest": Literal["INCLUDE", "EXCLUDE"],
        "SegmentModifier": str,
    },
    total=False,
)

HopDestinationTypeDef = TypedDict(
    "HopDestinationTypeDef", {"Priority": int, "Queue": str, "WaitMinutes": int}, total=False
)

Id3InsertionTypeDef = TypedDict("Id3InsertionTypeDef", {"Id3": str, "Timecode": str}, total=False)

ImageInserterTypeDef = TypedDict(
    "ImageInserterTypeDef", {"InsertableImages": List["InsertableImageTypeDef"]}, total=False
)

ImscDestinationSettingsTypeDef = TypedDict(
    "ImscDestinationSettingsTypeDef",
    {"StylePassthrough": Literal["ENABLED", "DISABLED"]},
    total=False,
)

InputClippingTypeDef = TypedDict(
    "InputClippingTypeDef", {"EndTimecode": str, "StartTimecode": str}, total=False
)

InputDecryptionSettingsTypeDef = TypedDict(
    "InputDecryptionSettingsTypeDef",
    {
        "DecryptionMode": Literal["AES_CTR", "AES_CBC", "AES_GCM"],
        "EncryptedDecryptionKey": str,
        "InitializationVector": str,
        "KmsKeyRegion": str,
    },
    total=False,
)

InputTemplateTypeDef = TypedDict(
    "InputTemplateTypeDef",
    {
        "AudioSelectorGroups": Dict[str, "AudioSelectorGroupTypeDef"],
        "AudioSelectors": Dict[str, "AudioSelectorTypeDef"],
        "CaptionSelectors": Dict[str, "CaptionSelectorTypeDef"],
        "Crop": "RectangleTypeDef",
        "DeblockFilter": Literal["ENABLED", "DISABLED"],
        "DenoiseFilter": Literal["ENABLED", "DISABLED"],
        "FilterEnable": Literal["AUTO", "DISABLE", "FORCE"],
        "FilterStrength": int,
        "ImageInserter": "ImageInserterTypeDef",
        "InputClippings": List["InputClippingTypeDef"],
        "InputScanType": Literal["AUTO", "PSF"],
        "Position": "RectangleTypeDef",
        "ProgramNumber": int,
        "PsiControl": Literal["IGNORE_PSI", "USE_PSI"],
        "TimecodeSource": Literal["EMBEDDED", "ZEROBASED", "SPECIFIEDSTART"],
        "TimecodeStart": str,
        "VideoSelector": "VideoSelectorTypeDef",
    },
    total=False,
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "AudioSelectorGroups": Dict[str, "AudioSelectorGroupTypeDef"],
        "AudioSelectors": Dict[str, "AudioSelectorTypeDef"],
        "CaptionSelectors": Dict[str, "CaptionSelectorTypeDef"],
        "Crop": "RectangleTypeDef",
        "DeblockFilter": Literal["ENABLED", "DISABLED"],
        "DecryptionSettings": "InputDecryptionSettingsTypeDef",
        "DenoiseFilter": Literal["ENABLED", "DISABLED"],
        "FileInput": str,
        "FilterEnable": Literal["AUTO", "DISABLE", "FORCE"],
        "FilterStrength": int,
        "ImageInserter": "ImageInserterTypeDef",
        "InputClippings": List["InputClippingTypeDef"],
        "InputScanType": Literal["AUTO", "PSF"],
        "Position": "RectangleTypeDef",
        "ProgramNumber": int,
        "PsiControl": Literal["IGNORE_PSI", "USE_PSI"],
        "SupplementalImps": List[str],
        "TimecodeSource": Literal["EMBEDDED", "ZEROBASED", "SPECIFIEDSTART"],
        "TimecodeStart": str,
        "VideoSelector": "VideoSelectorTypeDef",
    },
    total=False,
)

InsertableImageTypeDef = TypedDict(
    "InsertableImageTypeDef",
    {
        "Duration": int,
        "FadeIn": int,
        "FadeOut": int,
        "Height": int,
        "ImageInserterInput": str,
        "ImageX": int,
        "ImageY": int,
        "Layer": int,
        "Opacity": int,
        "StartTime": str,
        "Width": int,
    },
    total=False,
)

JobMessagesTypeDef = TypedDict(
    "JobMessagesTypeDef", {"Info": List[str], "Warning": List[str]}, total=False
)

JobSettingsTypeDef = TypedDict(
    "JobSettingsTypeDef",
    {
        "AdAvailOffset": int,
        "AvailBlanking": "AvailBlankingTypeDef",
        "Esam": "EsamSettingsTypeDef",
        "Inputs": List["InputTypeDef"],
        "MotionImageInserter": "MotionImageInserterTypeDef",
        "NielsenConfiguration": "NielsenConfigurationTypeDef",
        "NielsenNonLinearWatermark": "NielsenNonLinearWatermarkSettingsTypeDef",
        "OutputGroups": List["OutputGroupTypeDef"],
        "TimecodeConfig": "TimecodeConfigTypeDef",
        "TimedMetadataInsertion": "TimedMetadataInsertionTypeDef",
    },
    total=False,
)

JobTemplateSettingsTypeDef = TypedDict(
    "JobTemplateSettingsTypeDef",
    {
        "AdAvailOffset": int,
        "AvailBlanking": "AvailBlankingTypeDef",
        "Esam": "EsamSettingsTypeDef",
        "Inputs": List["InputTemplateTypeDef"],
        "MotionImageInserter": "MotionImageInserterTypeDef",
        "NielsenConfiguration": "NielsenConfigurationTypeDef",
        "NielsenNonLinearWatermark": "NielsenNonLinearWatermarkSettingsTypeDef",
        "OutputGroups": List["OutputGroupTypeDef"],
        "TimecodeConfig": "TimecodeConfigTypeDef",
        "TimedMetadataInsertion": "TimedMetadataInsertionTypeDef",
    },
    total=False,
)

_RequiredJobTemplateTypeDef = TypedDict(
    "_RequiredJobTemplateTypeDef", {"Name": str, "Settings": "JobTemplateSettingsTypeDef"}
)
_OptionalJobTemplateTypeDef = TypedDict(
    "_OptionalJobTemplateTypeDef",
    {
        "AccelerationSettings": "AccelerationSettingsTypeDef",
        "Arn": str,
        "Category": str,
        "CreatedAt": datetime,
        "Description": str,
        "HopDestinations": List["HopDestinationTypeDef"],
        "LastUpdated": datetime,
        "Priority": int,
        "Queue": str,
        "StatusUpdateInterval": Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_15",
            "SECONDS_20",
            "SECONDS_30",
            "SECONDS_60",
            "SECONDS_120",
            "SECONDS_180",
            "SECONDS_240",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_600",
        ],
        "Type": Literal["SYSTEM", "CUSTOM"],
    },
    total=False,
)


class JobTemplateTypeDef(_RequiredJobTemplateTypeDef, _OptionalJobTemplateTypeDef):
    pass


_RequiredJobTypeDef = TypedDict(
    "_RequiredJobTypeDef", {"Role": str, "Settings": "JobSettingsTypeDef"}
)
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "AccelerationSettings": "AccelerationSettingsTypeDef",
        "AccelerationStatus": Literal[
            "NOT_APPLICABLE", "IN_PROGRESS", "ACCELERATED", "NOT_ACCELERATED"
        ],
        "Arn": str,
        "BillingTagsSource": Literal["QUEUE", "PRESET", "JOB_TEMPLATE", "JOB"],
        "CreatedAt": datetime,
        "CurrentPhase": Literal["PROBING", "TRANSCODING", "UPLOADING"],
        "ErrorCode": int,
        "ErrorMessage": str,
        "HopDestinations": List["HopDestinationTypeDef"],
        "Id": str,
        "JobPercentComplete": int,
        "JobTemplate": str,
        "Messages": "JobMessagesTypeDef",
        "OutputGroupDetails": List["OutputGroupDetailTypeDef"],
        "Priority": int,
        "Queue": str,
        "QueueTransitions": List["QueueTransitionTypeDef"],
        "RetryCount": int,
        "SimulateReservedQueue": Literal["DISABLED", "ENABLED"],
        "Status": Literal["SUBMITTED", "PROGRESSING", "COMPLETE", "CANCELED", "ERROR"],
        "StatusUpdateInterval": Literal[
            "SECONDS_10",
            "SECONDS_12",
            "SECONDS_15",
            "SECONDS_20",
            "SECONDS_30",
            "SECONDS_60",
            "SECONDS_120",
            "SECONDS_180",
            "SECONDS_240",
            "SECONDS_300",
            "SECONDS_360",
            "SECONDS_420",
            "SECONDS_480",
            "SECONDS_540",
            "SECONDS_600",
        ],
        "Timing": "TimingTypeDef",
        "UserMetadata": Dict[str, str],
    },
    total=False,
)


class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass


M2tsScte35EsamTypeDef = TypedDict("M2tsScte35EsamTypeDef", {"Scte35EsamPid": int}, total=False)

M2tsSettingsTypeDef = TypedDict(
    "M2tsSettingsTypeDef",
    {
        "AudioBufferModel": Literal["DVB", "ATSC"],
        "AudioDuration": Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"],
        "AudioFramesPerPes": int,
        "AudioPids": List[int],
        "Bitrate": int,
        "BufferModel": Literal["MULTIPLEX", "NONE"],
        "DvbNitSettings": "DvbNitSettingsTypeDef",
        "DvbSdtSettings": "DvbSdtSettingsTypeDef",
        "DvbSubPids": List[int],
        "DvbTdtSettings": "DvbTdtSettingsTypeDef",
        "DvbTeletextPid": int,
        "EbpAudioInterval": Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"],
        "EbpPlacement": Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"],
        "EsRateInPes": Literal["INCLUDE", "EXCLUDE"],
        "ForceTsVideoEbpOrder": Literal["FORCE", "DEFAULT"],
        "FragmentTime": float,
        "MaxPcrInterval": int,
        "MinEbpInterval": int,
        "NielsenId3": Literal["INSERT", "NONE"],
        "NullPacketBitrate": float,
        "PatInterval": int,
        "PcrControl": Literal["PCR_EVERY_PES_PACKET", "CONFIGURED_PCR_PERIOD"],
        "PcrPid": int,
        "PmtInterval": int,
        "PmtPid": int,
        "PrivateMetadataPid": int,
        "ProgramNumber": int,
        "RateMode": Literal["VBR", "CBR"],
        "Scte35Esam": "M2tsScte35EsamTypeDef",
        "Scte35Pid": int,
        "Scte35Source": Literal["PASSTHROUGH", "NONE"],
        "SegmentationMarkers": Literal[
            "NONE", "RAI_SEGSTART", "RAI_ADAPT", "PSI_SEGSTART", "EBP", "EBP_LEGACY"
        ],
        "SegmentationStyle": Literal["MAINTAIN_CADENCE", "RESET_CADENCE"],
        "SegmentationTime": float,
        "TimedMetadataPid": int,
        "TransportStreamId": int,
        "VideoPid": int,
    },
    total=False,
)

M3u8SettingsTypeDef = TypedDict(
    "M3u8SettingsTypeDef",
    {
        "AudioDuration": Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"],
        "AudioFramesPerPes": int,
        "AudioPids": List[int],
        "NielsenId3": Literal["INSERT", "NONE"],
        "PatInterval": int,
        "PcrControl": Literal["PCR_EVERY_PES_PACKET", "CONFIGURED_PCR_PERIOD"],
        "PcrPid": int,
        "PmtInterval": int,
        "PmtPid": int,
        "PrivateMetadataPid": int,
        "ProgramNumber": int,
        "Scte35Pid": int,
        "Scte35Source": Literal["PASSTHROUGH", "NONE"],
        "TimedMetadata": Literal["PASSTHROUGH", "NONE"],
        "TimedMetadataPid": int,
        "TransportStreamId": int,
        "VideoPid": int,
    },
    total=False,
)

MotionImageInserterTypeDef = TypedDict(
    "MotionImageInserterTypeDef",
    {
        "Framerate": "MotionImageInsertionFramerateTypeDef",
        "Input": str,
        "InsertionMode": Literal["MOV", "PNG"],
        "Offset": "MotionImageInsertionOffsetTypeDef",
        "Playback": Literal["ONCE", "REPEAT"],
        "StartTime": str,
    },
    total=False,
)

MotionImageInsertionFramerateTypeDef = TypedDict(
    "MotionImageInsertionFramerateTypeDef",
    {"FramerateDenominator": int, "FramerateNumerator": int},
    total=False,
)

MotionImageInsertionOffsetTypeDef = TypedDict(
    "MotionImageInsertionOffsetTypeDef", {"ImageX": int, "ImageY": int}, total=False
)

MovSettingsTypeDef = TypedDict(
    "MovSettingsTypeDef",
    {
        "ClapAtom": Literal["INCLUDE", "EXCLUDE"],
        "CslgAtom": Literal["INCLUDE", "EXCLUDE"],
        "Mpeg2FourCCControl": Literal["XDCAM", "MPEG"],
        "PaddingControl": Literal["OMNEON", "NONE"],
        "Reference": Literal["SELF_CONTAINED", "EXTERNAL"],
    },
    total=False,
)

Mp2SettingsTypeDef = TypedDict(
    "Mp2SettingsTypeDef", {"Bitrate": int, "Channels": int, "SampleRate": int}, total=False
)

Mp3SettingsTypeDef = TypedDict(
    "Mp3SettingsTypeDef",
    {
        "Bitrate": int,
        "Channels": int,
        "RateControlMode": Literal["CBR", "VBR"],
        "SampleRate": int,
        "VbrQuality": int,
    },
    total=False,
)

Mp4SettingsTypeDef = TypedDict(
    "Mp4SettingsTypeDef",
    {
        "AudioDuration": Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"],
        "CslgAtom": Literal["INCLUDE", "EXCLUDE"],
        "CttsVersion": int,
        "FreeSpaceBox": Literal["INCLUDE", "EXCLUDE"],
        "MoovPlacement": Literal["PROGRESSIVE_DOWNLOAD", "NORMAL"],
        "Mp4MajorBrand": str,
    },
    total=False,
)

MpdSettingsTypeDef = TypedDict(
    "MpdSettingsTypeDef",
    {
        "AccessibilityCaptionHints": Literal["INCLUDE", "EXCLUDE"],
        "AudioDuration": Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"],
        "CaptionContainerType": Literal["RAW", "FRAGMENTED_MP4"],
        "Scte35Esam": Literal["INSERT", "NONE"],
        "Scte35Source": Literal["PASSTHROUGH", "NONE"],
    },
    total=False,
)

Mpeg2SettingsTypeDef = TypedDict(
    "Mpeg2SettingsTypeDef",
    {
        "AdaptiveQuantization": Literal["OFF", "LOW", "MEDIUM", "HIGH"],
        "Bitrate": int,
        "CodecLevel": Literal["AUTO", "LOW", "MAIN", "HIGH1440", "HIGH"],
        "CodecProfile": Literal["MAIN", "PROFILE_422"],
        "DynamicSubGop": Literal["ADAPTIVE", "STATIC"],
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopClosedCadence": int,
        "GopSize": float,
        "GopSizeUnits": Literal["FRAMES", "SECONDS"],
        "HrdBufferInitialFillPercentage": int,
        "HrdBufferSize": int,
        "InterlaceMode": Literal[
            "PROGRESSIVE", "TOP_FIELD", "BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "FOLLOW_BOTTOM_FIELD"
        ],
        "IntraDcPrecision": Literal[
            "AUTO",
            "INTRA_DC_PRECISION_8",
            "INTRA_DC_PRECISION_9",
            "INTRA_DC_PRECISION_10",
            "INTRA_DC_PRECISION_11",
        ],
        "MaxBitrate": int,
        "MinIInterval": int,
        "NumberBFramesBetweenReferenceFrames": int,
        "ParControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": Literal["SINGLE_PASS", "MULTI_PASS"],
        "RateControlMode": Literal["VBR", "CBR"],
        "ScanTypeConversionMode": Literal["INTERLACED", "INTERLACED_OPTIMIZE"],
        "SceneChangeDetect": Literal["DISABLED", "ENABLED"],
        "SlowPal": Literal["DISABLED", "ENABLED"],
        "Softness": int,
        "SpatialAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
        "Syntax": Literal["DEFAULT", "D_10"],
        "Telecine": Literal["NONE", "SOFT", "HARD"],
        "TemporalAdaptiveQuantization": Literal["DISABLED", "ENABLED"],
    },
    total=False,
)

MsSmoothAdditionalManifestTypeDef = TypedDict(
    "MsSmoothAdditionalManifestTypeDef",
    {"ManifestNameModifier": str, "SelectedOutputs": List[str]},
    total=False,
)

MsSmoothEncryptionSettingsTypeDef = TypedDict(
    "MsSmoothEncryptionSettingsTypeDef",
    {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"},
    total=False,
)

MsSmoothGroupSettingsTypeDef = TypedDict(
    "MsSmoothGroupSettingsTypeDef",
    {
        "AdditionalManifests": List["MsSmoothAdditionalManifestTypeDef"],
        "AudioDeduplication": Literal["COMBINE_DUPLICATE_STREAMS", "NONE"],
        "Destination": str,
        "DestinationSettings": "DestinationSettingsTypeDef",
        "Encryption": "MsSmoothEncryptionSettingsTypeDef",
        "FragmentLength": int,
        "ManifestEncoding": Literal["UTF8", "UTF16"],
    },
    total=False,
)

MxfSettingsTypeDef = TypedDict(
    "MxfSettingsTypeDef",
    {
        "AfdSignaling": Literal["NO_COPY", "COPY_FROM_VIDEO"],
        "Profile": Literal["D_10", "XDCAM", "OP1A"],
    },
    total=False,
)

NexGuardFileMarkerSettingsTypeDef = TypedDict(
    "NexGuardFileMarkerSettingsTypeDef",
    {
        "License": str,
        "Payload": int,
        "Preset": str,
        "Strength": Literal["LIGHTEST", "LIGHTER", "DEFAULT", "STRONGER", "STRONGEST"],
    },
    total=False,
)

NielsenConfigurationTypeDef = TypedDict(
    "NielsenConfigurationTypeDef", {"BreakoutCode": int, "DistributorId": str}, total=False
)

NielsenNonLinearWatermarkSettingsTypeDef = TypedDict(
    "NielsenNonLinearWatermarkSettingsTypeDef",
    {
        "ActiveWatermarkProcess": Literal["NAES2_AND_NW", "CBET", "NAES2_AND_NW_AND_CBET"],
        "AdiFilename": str,
        "AssetId": str,
        "AssetName": str,
        "CbetSourceId": str,
        "EpisodeId": str,
        "MetadataDestination": str,
        "SourceId": int,
        "SourceWatermarkStatus": Literal["CLEAN", "WATERMARKED"],
        "TicServerUrl": str,
        "UniqueTicPerAudioTrack": Literal["RESERVE_UNIQUE_TICS_PER_TRACK", "SAME_TICS_PER_TRACK"],
    },
    total=False,
)

NoiseReducerFilterSettingsTypeDef = TypedDict(
    "NoiseReducerFilterSettingsTypeDef", {"Strength": int}, total=False
)

NoiseReducerSpatialFilterSettingsTypeDef = TypedDict(
    "NoiseReducerSpatialFilterSettingsTypeDef",
    {"PostFilterSharpenStrength": int, "Speed": int, "Strength": int},
    total=False,
)

NoiseReducerTemporalFilterSettingsTypeDef = TypedDict(
    "NoiseReducerTemporalFilterSettingsTypeDef",
    {
        "AggressiveMode": int,
        "PostTemporalSharpening": Literal["DISABLED", "ENABLED", "AUTO"],
        "Speed": int,
        "Strength": int,
    },
    total=False,
)

NoiseReducerTypeDef = TypedDict(
    "NoiseReducerTypeDef",
    {
        "Filter": Literal[
            "BILATERAL", "MEAN", "GAUSSIAN", "LANCZOS", "SHARPEN", "CONSERVE", "SPATIAL", "TEMPORAL"
        ],
        "FilterSettings": "NoiseReducerFilterSettingsTypeDef",
        "SpatialFilterSettings": "NoiseReducerSpatialFilterSettingsTypeDef",
        "TemporalFilterSettings": "NoiseReducerTemporalFilterSettingsTypeDef",
    },
    total=False,
)

OpusSettingsTypeDef = TypedDict(
    "OpusSettingsTypeDef", {"Bitrate": int, "Channels": int, "SampleRate": int}, total=False
)

OutputChannelMappingTypeDef = TypedDict(
    "OutputChannelMappingTypeDef",
    {"InputChannels": List[int], "InputChannelsFineTune": List[float]},
    total=False,
)

OutputDetailTypeDef = TypedDict(
    "OutputDetailTypeDef", {"DurationInMs": int, "VideoDetails": "VideoDetailTypeDef"}, total=False
)

OutputGroupDetailTypeDef = TypedDict(
    "OutputGroupDetailTypeDef", {"OutputDetails": List["OutputDetailTypeDef"]}, total=False
)

OutputGroupSettingsTypeDef = TypedDict(
    "OutputGroupSettingsTypeDef",
    {
        "CmafGroupSettings": "CmafGroupSettingsTypeDef",
        "DashIsoGroupSettings": "DashIsoGroupSettingsTypeDef",
        "FileGroupSettings": "FileGroupSettingsTypeDef",
        "HlsGroupSettings": "HlsGroupSettingsTypeDef",
        "MsSmoothGroupSettings": "MsSmoothGroupSettingsTypeDef",
        "Type": Literal[
            "HLS_GROUP_SETTINGS",
            "DASH_ISO_GROUP_SETTINGS",
            "FILE_GROUP_SETTINGS",
            "MS_SMOOTH_GROUP_SETTINGS",
            "CMAF_GROUP_SETTINGS",
        ],
    },
    total=False,
)

OutputGroupTypeDef = TypedDict(
    "OutputGroupTypeDef",
    {
        "AutomatedEncodingSettings": "AutomatedEncodingSettingsTypeDef",
        "CustomName": str,
        "Name": str,
        "OutputGroupSettings": "OutputGroupSettingsTypeDef",
        "Outputs": List["OutputTypeDef"],
    },
    total=False,
)

OutputSettingsTypeDef = TypedDict(
    "OutputSettingsTypeDef", {"HlsSettings": "HlsSettingsTypeDef"}, total=False
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "AudioDescriptions": List["AudioDescriptionTypeDef"],
        "CaptionDescriptions": List["CaptionDescriptionTypeDef"],
        "ContainerSettings": "ContainerSettingsTypeDef",
        "Extension": str,
        "NameModifier": str,
        "OutputSettings": "OutputSettingsTypeDef",
        "Preset": str,
        "VideoDescription": "VideoDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PartnerWatermarkingTypeDef = TypedDict(
    "PartnerWatermarkingTypeDef",
    {"NexguardFileMarkerSettings": "NexGuardFileMarkerSettingsTypeDef"},
    total=False,
)

PresetSettingsTypeDef = TypedDict(
    "PresetSettingsTypeDef",
    {
        "AudioDescriptions": List["AudioDescriptionTypeDef"],
        "CaptionDescriptions": List["CaptionDescriptionPresetTypeDef"],
        "ContainerSettings": "ContainerSettingsTypeDef",
        "VideoDescription": "VideoDescriptionTypeDef",
    },
    total=False,
)

_RequiredPresetTypeDef = TypedDict(
    "_RequiredPresetTypeDef", {"Name": str, "Settings": "PresetSettingsTypeDef"}
)
_OptionalPresetTypeDef = TypedDict(
    "_OptionalPresetTypeDef",
    {
        "Arn": str,
        "Category": str,
        "CreatedAt": datetime,
        "Description": str,
        "LastUpdated": datetime,
        "Type": Literal["SYSTEM", "CUSTOM"],
    },
    total=False,
)


class PresetTypeDef(_RequiredPresetTypeDef, _OptionalPresetTypeDef):
    pass


ProresSettingsTypeDef = TypedDict(
    "ProresSettingsTypeDef",
    {
        "CodecProfile": Literal[
            "APPLE_PRORES_422",
            "APPLE_PRORES_422_HQ",
            "APPLE_PRORES_422_LT",
            "APPLE_PRORES_422_PROXY",
        ],
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "InterlaceMode": Literal[
            "PROGRESSIVE", "TOP_FIELD", "BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "FOLLOW_BOTTOM_FIELD"
        ],
        "ParControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "ParDenominator": int,
        "ParNumerator": int,
        "ScanTypeConversionMode": Literal["INTERLACED", "INTERLACED_OPTIMIZE"],
        "SlowPal": Literal["DISABLED", "ENABLED"],
        "Telecine": Literal["NONE", "HARD"],
    },
    total=False,
)

QueueTransitionTypeDef = TypedDict(
    "QueueTransitionTypeDef",
    {"DestinationQueue": str, "SourceQueue": str, "Timestamp": datetime},
    total=False,
)

_RequiredQueueTypeDef = TypedDict("_RequiredQueueTypeDef", {"Name": str})
_OptionalQueueTypeDef = TypedDict(
    "_OptionalQueueTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "LastUpdated": datetime,
        "PricingPlan": Literal["ON_DEMAND", "RESERVED"],
        "ProgressingJobsCount": int,
        "ReservationPlan": "ReservationPlanTypeDef",
        "Status": Literal["ACTIVE", "PAUSED"],
        "SubmittedJobsCount": int,
        "Type": Literal["SYSTEM", "CUSTOM"],
    },
    total=False,
)


class QueueTypeDef(_RequiredQueueTypeDef, _OptionalQueueTypeDef):
    pass


RectangleTypeDef = TypedDict(
    "RectangleTypeDef", {"Height": int, "Width": int, "X": int, "Y": int}, total=False
)

RemixSettingsTypeDef = TypedDict(
    "RemixSettingsTypeDef",
    {"ChannelMapping": "ChannelMappingTypeDef", "ChannelsIn": int, "ChannelsOut": int},
    total=False,
)

ReservationPlanTypeDef = TypedDict(
    "ReservationPlanTypeDef",
    {
        "Commitment": Literal["ONE_YEAR"],
        "ExpiresAt": datetime,
        "PurchasedAt": datetime,
        "RenewalType": Literal["AUTO_RENEW", "EXPIRE"],
        "ReservedSlots": int,
        "Status": Literal["ACTIVE", "EXPIRED"],
    },
    total=False,
)

ResourceTagsTypeDef = TypedDict(
    "ResourceTagsTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

S3DestinationAccessControlTypeDef = TypedDict(
    "S3DestinationAccessControlTypeDef",
    {
        "CannedAcl": Literal[
            "PUBLIC_READ", "AUTHENTICATED_READ", "BUCKET_OWNER_READ", "BUCKET_OWNER_FULL_CONTROL"
        ]
    },
    total=False,
)

S3DestinationSettingsTypeDef = TypedDict(
    "S3DestinationSettingsTypeDef",
    {
        "AccessControl": "S3DestinationAccessControlTypeDef",
        "Encryption": "S3EncryptionSettingsTypeDef",
    },
    total=False,
)

S3EncryptionSettingsTypeDef = TypedDict(
    "S3EncryptionSettingsTypeDef",
    {
        "EncryptionType": Literal["SERVER_SIDE_ENCRYPTION_S3", "SERVER_SIDE_ENCRYPTION_KMS"],
        "KmsKeyArn": str,
    },
    total=False,
)

SccDestinationSettingsTypeDef = TypedDict(
    "SccDestinationSettingsTypeDef",
    {
        "Framerate": Literal[
            "FRAMERATE_23_97",
            "FRAMERATE_24",
            "FRAMERATE_25",
            "FRAMERATE_29_97_DROPFRAME",
            "FRAMERATE_29_97_NON_DROPFRAME",
        ]
    },
    total=False,
)

SpekeKeyProviderCmafTypeDef = TypedDict(
    "SpekeKeyProviderCmafTypeDef",
    {
        "CertificateArn": str,
        "DashSignaledSystemIds": List[str],
        "HlsSignaledSystemIds": List[str],
        "ResourceId": str,
        "Url": str,
    },
    total=False,
)

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "SystemIds": List[str], "Url": str},
    total=False,
)

StaticKeyProviderTypeDef = TypedDict(
    "StaticKeyProviderTypeDef",
    {"KeyFormat": str, "KeyFormatVersions": str, "StaticKeyValue": str, "Url": str},
    total=False,
)

TeletextDestinationSettingsTypeDef = TypedDict(
    "TeletextDestinationSettingsTypeDef",
    {
        "PageNumber": str,
        "PageTypes": List[
            Literal[
                "PAGE_TYPE_INITIAL",
                "PAGE_TYPE_SUBTITLE",
                "PAGE_TYPE_ADDL_INFO",
                "PAGE_TYPE_PROGRAM_SCHEDULE",
                "PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE",
            ]
        ],
    },
    total=False,
)

TeletextSourceSettingsTypeDef = TypedDict(
    "TeletextSourceSettingsTypeDef", {"PageNumber": str}, total=False
)

TimecodeBurninTypeDef = TypedDict(
    "TimecodeBurninTypeDef",
    {
        "FontSize": int,
        "Position": Literal[
            "TOP_CENTER",
            "TOP_LEFT",
            "TOP_RIGHT",
            "MIDDLE_LEFT",
            "MIDDLE_CENTER",
            "MIDDLE_RIGHT",
            "BOTTOM_LEFT",
            "BOTTOM_CENTER",
            "BOTTOM_RIGHT",
        ],
        "Prefix": str,
    },
    total=False,
)

TimecodeConfigTypeDef = TypedDict(
    "TimecodeConfigTypeDef",
    {
        "Anchor": str,
        "Source": Literal["EMBEDDED", "ZEROBASED", "SPECIFIEDSTART"],
        "Start": str,
        "TimestampOffset": str,
    },
    total=False,
)

TimedMetadataInsertionTypeDef = TypedDict(
    "TimedMetadataInsertionTypeDef", {"Id3Insertions": List["Id3InsertionTypeDef"]}, total=False
)

TimingTypeDef = TypedDict(
    "TimingTypeDef",
    {"FinishTime": datetime, "StartTime": datetime, "SubmitTime": datetime},
    total=False,
)

TrackSourceSettingsTypeDef = TypedDict(
    "TrackSourceSettingsTypeDef", {"TrackNumber": int}, total=False
)

TtmlDestinationSettingsTypeDef = TypedDict(
    "TtmlDestinationSettingsTypeDef",
    {"StylePassthrough": Literal["ENABLED", "DISABLED"]},
    total=False,
)

Vc3SettingsTypeDef = TypedDict(
    "Vc3SettingsTypeDef",
    {
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "InterlaceMode": Literal["INTERLACED", "PROGRESSIVE"],
        "ScanTypeConversionMode": Literal["INTERLACED", "INTERLACED_OPTIMIZE"],
        "SlowPal": Literal["DISABLED", "ENABLED"],
        "Telecine": Literal["NONE", "HARD"],
        "Vc3Class": Literal["CLASS_145_8BIT", "CLASS_220_8BIT", "CLASS_220_10BIT"],
    },
    total=False,
)

VideoCodecSettingsTypeDef = TypedDict(
    "VideoCodecSettingsTypeDef",
    {
        "Av1Settings": "Av1SettingsTypeDef",
        "AvcIntraSettings": "AvcIntraSettingsTypeDef",
        "Codec": Literal[
            "AV1",
            "AVC_INTRA",
            "FRAME_CAPTURE",
            "H_264",
            "H_265",
            "MPEG2",
            "PRORES",
            "VC3",
            "VP8",
            "VP9",
        ],
        "FrameCaptureSettings": "FrameCaptureSettingsTypeDef",
        "H264Settings": "H264SettingsTypeDef",
        "H265Settings": "H265SettingsTypeDef",
        "Mpeg2Settings": "Mpeg2SettingsTypeDef",
        "ProresSettings": "ProresSettingsTypeDef",
        "Vc3Settings": "Vc3SettingsTypeDef",
        "Vp8Settings": "Vp8SettingsTypeDef",
        "Vp9Settings": "Vp9SettingsTypeDef",
    },
    total=False,
)

VideoDescriptionTypeDef = TypedDict(
    "VideoDescriptionTypeDef",
    {
        "AfdSignaling": Literal["NONE", "AUTO", "FIXED"],
        "AntiAlias": Literal["DISABLED", "ENABLED"],
        "CodecSettings": "VideoCodecSettingsTypeDef",
        "ColorMetadata": Literal["IGNORE", "INSERT"],
        "Crop": "RectangleTypeDef",
        "DropFrameTimecode": Literal["DISABLED", "ENABLED"],
        "FixedAfd": int,
        "Height": int,
        "Position": "RectangleTypeDef",
        "RespondToAfd": Literal["NONE", "RESPOND", "PASSTHROUGH"],
        "ScalingBehavior": Literal["DEFAULT", "STRETCH_TO_OUTPUT"],
        "Sharpness": int,
        "TimecodeInsertion": Literal["DISABLED", "PIC_TIMING_SEI"],
        "VideoPreprocessors": "VideoPreprocessorTypeDef",
        "Width": int,
    },
    total=False,
)

VideoDetailTypeDef = TypedDict(
    "VideoDetailTypeDef", {"HeightInPx": int, "WidthInPx": int}, total=False
)

VideoPreprocessorTypeDef = TypedDict(
    "VideoPreprocessorTypeDef",
    {
        "ColorCorrector": "ColorCorrectorTypeDef",
        "Deinterlacer": "DeinterlacerTypeDef",
        "DolbyVision": "DolbyVisionTypeDef",
        "ImageInserter": "ImageInserterTypeDef",
        "NoiseReducer": "NoiseReducerTypeDef",
        "PartnerWatermarking": "PartnerWatermarkingTypeDef",
        "TimecodeBurnin": "TimecodeBurninTypeDef",
    },
    total=False,
)

VideoSelectorTypeDef = TypedDict(
    "VideoSelectorTypeDef",
    {
        "AlphaBehavior": Literal["DISCARD", "REMAP_TO_LUMA"],
        "ColorSpace": Literal["FOLLOW", "REC_601", "REC_709", "HDR10", "HLG_2020"],
        "ColorSpaceUsage": Literal["FORCE", "FALLBACK"],
        "Hdr10Metadata": "Hdr10MetadataTypeDef",
        "Pid": int,
        "ProgramNumber": int,
        "Rotate": Literal["DEGREE_0", "DEGREES_90", "DEGREES_180", "DEGREES_270", "AUTO"],
    },
    total=False,
)

VorbisSettingsTypeDef = TypedDict(
    "VorbisSettingsTypeDef", {"Channels": int, "SampleRate": int, "VbrQuality": int}, total=False
)

Vp8SettingsTypeDef = TypedDict(
    "Vp8SettingsTypeDef",
    {
        "Bitrate": int,
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopSize": float,
        "HrdBufferSize": int,
        "MaxBitrate": int,
        "ParControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": Literal["MULTI_PASS", "MULTI_PASS_HQ"],
        "RateControlMode": Literal["VBR"],
    },
    total=False,
)

Vp9SettingsTypeDef = TypedDict(
    "Vp9SettingsTypeDef",
    {
        "Bitrate": int,
        "FramerateControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "FramerateConversionAlgorithm": Literal["DUPLICATE_DROP", "INTERPOLATE", "FRAMEFORMER"],
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopSize": float,
        "HrdBufferSize": int,
        "MaxBitrate": int,
        "ParControl": Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"],
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": Literal["MULTI_PASS", "MULTI_PASS_HQ"],
        "RateControlMode": Literal["VBR"],
    },
    total=False,
)

WavSettingsTypeDef = TypedDict(
    "WavSettingsTypeDef",
    {"BitDepth": int, "Channels": int, "Format": Literal["RIFF", "RF64"], "SampleRate": int},
    total=False,
)

CreateJobResponseTypeDef = TypedDict("CreateJobResponseTypeDef", {"Job": "JobTypeDef"}, total=False)

CreateJobTemplateResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseTypeDef", {"JobTemplate": "JobTemplateTypeDef"}, total=False
)

CreatePresetResponseTypeDef = TypedDict(
    "CreatePresetResponseTypeDef", {"Preset": "PresetTypeDef"}, total=False
)

CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef", {"Queue": "QueueTypeDef"}, total=False
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {"Endpoints": List["EndpointTypeDef"], "NextToken": str},
    total=False,
)

GetJobResponseTypeDef = TypedDict("GetJobResponseTypeDef", {"Job": "JobTypeDef"}, total=False)

GetJobTemplateResponseTypeDef = TypedDict(
    "GetJobTemplateResponseTypeDef", {"JobTemplate": "JobTemplateTypeDef"}, total=False
)

GetPresetResponseTypeDef = TypedDict(
    "GetPresetResponseTypeDef", {"Preset": "PresetTypeDef"}, total=False
)

GetQueueResponseTypeDef = TypedDict(
    "GetQueueResponseTypeDef", {"Queue": "QueueTypeDef"}, total=False
)

ListJobTemplatesResponseTypeDef = TypedDict(
    "ListJobTemplatesResponseTypeDef",
    {"JobTemplates": List["JobTemplateTypeDef"], "NextToken": str},
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef", {"Jobs": List["JobTypeDef"], "NextToken": str}, total=False
)

ListPresetsResponseTypeDef = TypedDict(
    "ListPresetsResponseTypeDef", {"NextToken": str, "Presets": List["PresetTypeDef"]}, total=False
)

ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef", {"NextToken": str, "Queues": List["QueueTypeDef"]}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"ResourceTags": "ResourceTagsTypeDef"}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ReservationPlanSettingsTypeDef = TypedDict(
    "ReservationPlanSettingsTypeDef",
    {
        "Commitment": Literal["ONE_YEAR"],
        "RenewalType": Literal["AUTO_RENEW", "EXPIRE"],
        "ReservedSlots": int,
    },
)

UpdateJobTemplateResponseTypeDef = TypedDict(
    "UpdateJobTemplateResponseTypeDef", {"JobTemplate": "JobTemplateTypeDef"}, total=False
)

UpdatePresetResponseTypeDef = TypedDict(
    "UpdatePresetResponseTypeDef", {"Preset": "PresetTypeDef"}, total=False
)

UpdateQueueResponseTypeDef = TypedDict(
    "UpdateQueueResponseTypeDef", {"Queue": "QueueTypeDef"}, total=False
)
