"""
Main interface for mediapackage service type definitions.

Usage::

    ```python
    from mypy_boto3_mediapackage.type_defs import AuthorizationTypeDef

    data: AuthorizationTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AuthorizationTypeDef",
    "ChannelTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageTypeDef",
    "DashEncryptionTypeDef",
    "DashPackageTypeDef",
    "HarvestJobTypeDef",
    "HlsEncryptionTypeDef",
    "HlsIngestTypeDef",
    "HlsManifestCreateOrUpdateParametersTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "IngestEndpointTypeDef",
    "MssEncryptionTypeDef",
    "MssPackageTypeDef",
    "OriginEndpointTypeDef",
    "S3DestinationTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "CmafPackageCreateOrUpdateParametersTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateHarvestJobResponseTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeHarvestJobResponseTypeDef",
    "DescribeOriginEndpointResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RotateChannelCredentialsResponseTypeDef",
    "RotateIngestEndpointCredentialsResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef", {"CdnIdentifierSecret": str, "SecretsRoleArn": str}
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredCmafEncryptionTypeDef = TypedDict(
    "_RequiredCmafEncryptionTypeDef", {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"}
)
_OptionalCmafEncryptionTypeDef = TypedDict(
    "_OptionalCmafEncryptionTypeDef", {"KeyRotationIntervalSeconds": int}, total=False
)


class CmafEncryptionTypeDef(_RequiredCmafEncryptionTypeDef, _OptionalCmafEncryptionTypeDef):
    pass


CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "Encryption": "CmafEncryptionTypeDef",
        "HlsManifests": List["HlsManifestTypeDef"],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredDashEncryptionTypeDef = TypedDict(
    "_RequiredDashEncryptionTypeDef", {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"}
)
_OptionalDashEncryptionTypeDef = TypedDict(
    "_OptionalDashEncryptionTypeDef", {"KeyRotationIntervalSeconds": int}, total=False
)


class DashEncryptionTypeDef(_RequiredDashEncryptionTypeDef, _OptionalDashEncryptionTypeDef):
    pass


DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": "DashEncryptionTypeDef",
        "ManifestLayout": Literal["FULL", "COMPACT"],
        "ManifestWindowSeconds": int,
        "MinBufferTimeSeconds": int,
        "MinUpdatePeriodSeconds": int,
        "PeriodTriggers": List[Literal["ADS"]],
        "Profile": Literal["NONE", "HBBTV_1_5"],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": Literal[
            "NUMBER_WITH_TIMELINE", "TIME_WITH_TIMELINE", "NUMBER_WITH_DURATION"
        ],
        "StreamSelection": "StreamSelectionTypeDef",
        "SuggestedPresentationDelaySeconds": int,
    },
    total=False,
)

HarvestJobTypeDef = TypedDict(
    "HarvestJobTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

_RequiredHlsEncryptionTypeDef = TypedDict(
    "_RequiredHlsEncryptionTypeDef", {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"}
)
_OptionalHlsEncryptionTypeDef = TypedDict(
    "_OptionalHlsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": Literal["AES_128", "SAMPLE_AES"],
        "KeyRotationIntervalSeconds": int,
        "RepeatExtXKey": bool,
    },
    total=False,
)


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, _OptionalHlsEncryptionTypeDef):
    pass


HlsIngestTypeDef = TypedDict(
    "HlsIngestTypeDef", {"IngestEndpoints": List["IngestEndpointTypeDef"]}, total=False
)

_RequiredHlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "_RequiredHlsManifestCreateOrUpdateParametersTypeDef", {"Id": str}
)
_OptionalHlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "_OptionalHlsManifestCreateOrUpdateParametersTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH", "DATERANGE"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
    },
    total=False,
)


class HlsManifestCreateOrUpdateParametersTypeDef(
    _RequiredHlsManifestCreateOrUpdateParametersTypeDef,
    _OptionalHlsManifestCreateOrUpdateParametersTypeDef,
):
    pass


_RequiredHlsManifestTypeDef = TypedDict("_RequiredHlsManifestTypeDef", {"Id": str})
_OptionalHlsManifestTypeDef = TypedDict(
    "_OptionalHlsManifestTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH", "DATERANGE"],
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "Url": str,
    },
    total=False,
)


class HlsManifestTypeDef(_RequiredHlsManifestTypeDef, _OptionalHlsManifestTypeDef):
    pass


HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "AdMarkers": Literal["NONE", "SCTE35_ENHANCED", "PASSTHROUGH", "DATERANGE"],
        "AdTriggers": List[
            Literal[
                "SPLICE_INSERT",
                "BREAK",
                "PROVIDER_ADVERTISEMENT",
                "DISTRIBUTOR_ADVERTISEMENT",
                "PROVIDER_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_PLACEMENT_OPPORTUNITY",
                "PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY",
                "DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY",
            ]
        ],
        "AdsOnDeliveryRestrictions": Literal["NONE", "RESTRICTED", "UNRESTRICTED", "BOTH"],
        "Encryption": "HlsEncryptionTypeDef",
        "IncludeIframeOnlyStream": bool,
        "PlaylistType": Literal["NONE", "EVENT", "VOD"],
        "PlaylistWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": "StreamSelectionTypeDef",
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef", {"Id": str, "Password": str, "Url": str, "Username": str}, total=False
)

MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef", {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"}
)

MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "Encryption": "MssEncryptionTypeDef",
        "ManifestWindowSeconds": int,
        "SegmentDurationSeconds": int,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

OriginEndpointTypeDef = TypedDict(
    "OriginEndpointTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef", {"BucketName": str, "ManifestKey": str, "RoleArn": str}
)

_RequiredSpekeKeyProviderTypeDef = TypedDict(
    "_RequiredSpekeKeyProviderTypeDef",
    {"ResourceId": str, "RoleArn": str, "SystemIds": List[str], "Url": str},
)
_OptionalSpekeKeyProviderTypeDef = TypedDict(
    "_OptionalSpekeKeyProviderTypeDef", {"CertificateArn": str}, total=False
)


class SpekeKeyProviderTypeDef(_RequiredSpekeKeyProviderTypeDef, _OptionalSpekeKeyProviderTypeDef):
    pass


StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": Literal["ORIGINAL", "VIDEO_BITRATE_ASCENDING", "VIDEO_BITRATE_DESCENDING"],
    },
    total=False,
)

CmafPackageCreateOrUpdateParametersTypeDef = TypedDict(
    "CmafPackageCreateOrUpdateParametersTypeDef",
    {
        "Encryption": "CmafEncryptionTypeDef",
        "HlsManifests": List["HlsManifestCreateOrUpdateParametersTypeDef"],
        "SegmentDurationSeconds": int,
        "SegmentPrefix": str,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateHarvestJobResponseTypeDef = TypedDict(
    "CreateHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

CreateOriginEndpointResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DescribeHarvestJobResponseTypeDef = TypedDict(
    "DescribeHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
        "Status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
    },
    total=False,
)

DescribeOriginEndpointResponseTypeDef = TypedDict(
    "DescribeOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {"Channels": List["ChannelTypeDef"], "NextToken": str},
    total=False,
)

ListHarvestJobsResponseTypeDef = TypedDict(
    "ListHarvestJobsResponseTypeDef",
    {"HarvestJobs": List["HarvestJobTypeDef"], "NextToken": str},
    total=False,
)

ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {"NextToken": str, "OriginEndpoints": List["OriginEndpointTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RotateChannelCredentialsResponseTypeDef = TypedDict(
    "RotateChannelCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

RotateIngestEndpointCredentialsResponseTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

UpdateOriginEndpointResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": Literal["ALLOW", "DENY"],
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
    },
    total=False,
)
