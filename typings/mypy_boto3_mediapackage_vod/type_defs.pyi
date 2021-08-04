"""
Type annotations for mediapackage-vod service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediapackage_vod.type_defs import AssetShallowTypeDef

    data: AssetShallowTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AdMarkersType,
    EncryptionMethodType,
    ManifestLayoutType,
    ProfileType,
    SegmentTemplateFormatType,
    StreamOrderType,
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
    "AssetShallowTypeDef",
    "AuthorizationTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageTypeDef",
    "ConfigureLogsRequestRequestTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateAssetRequestRequestTypeDef",
    "CreateAssetResponseTypeDef",
    "CreatePackagingConfigurationRequestRequestTypeDef",
    "CreatePackagingConfigurationResponseTypeDef",
    "CreatePackagingGroupRequestRequestTypeDef",
    "CreatePackagingGroupResponseTypeDef",
    "DashEncryptionTypeDef",
    "DashManifestTypeDef",
    "DashPackageTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeletePackagingConfigurationRequestRequestTypeDef",
    "DeletePackagingGroupRequestRequestTypeDef",
    "DescribeAssetRequestRequestTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribePackagingConfigurationRequestRequestTypeDef",
    "DescribePackagingConfigurationResponseTypeDef",
    "DescribePackagingGroupRequestRequestTypeDef",
    "DescribePackagingGroupResponseTypeDef",
    "EgressAccessLogsTypeDef",
    "EgressEndpointTypeDef",
    "HlsEncryptionTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "ListAssetsRequestRequestTypeDef",
    "ListAssetsResponseTypeDef",
    "ListPackagingConfigurationsRequestRequestTypeDef",
    "ListPackagingConfigurationsResponseTypeDef",
    "ListPackagingGroupsRequestRequestTypeDef",
    "ListPackagingGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MssEncryptionTypeDef",
    "MssManifestTypeDef",
    "MssPackageTypeDef",
    "PackagingConfigurationTypeDef",
    "PackagingGroupTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePackagingGroupRequestRequestTypeDef",
    "UpdatePackagingGroupResponseTypeDef",
)

AssetShallowTypeDef = TypedDict(
    "AssetShallowTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef",
    {
        "CdnIdentifierSecret": str,
        "SecretsRoleArn": str,
    },
)

_RequiredCmafEncryptionTypeDef = TypedDict(
    "_RequiredCmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)
_OptionalCmafEncryptionTypeDef = TypedDict(
    "_OptionalCmafEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
    },
    total=False,
)

class CmafEncryptionTypeDef(_RequiredCmafEncryptionTypeDef, _OptionalCmafEncryptionTypeDef):
    pass

_RequiredCmafPackageTypeDef = TypedDict(
    "_RequiredCmafPackageTypeDef",
    {
        "HlsManifests": List["HlsManifestTypeDef"],
    },
)
_OptionalCmafPackageTypeDef = TypedDict(
    "_OptionalCmafPackageTypeDef",
    {
        "Encryption": "CmafEncryptionTypeDef",
        "IncludeEncoderConfigurationInSegments": bool,
        "SegmentDurationSeconds": int,
    },
    total=False,
)

class CmafPackageTypeDef(_RequiredCmafPackageTypeDef, _OptionalCmafPackageTypeDef):
    pass

_RequiredConfigureLogsRequestRequestTypeDef = TypedDict(
    "_RequiredConfigureLogsRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalConfigureLogsRequestRequestTypeDef = TypedDict(
    "_OptionalConfigureLogsRequestRequestTypeDef",
    {
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
    },
    total=False,
)

class ConfigureLogsRequestRequestTypeDef(
    _RequiredConfigureLogsRequestRequestTypeDef, _OptionalConfigureLogsRequestRequestTypeDef
):
    pass

ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssetRequestRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
    },
)
_OptionalCreateAssetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssetRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateAssetRequestRequestTypeDef(
    _RequiredCreateAssetRequestRequestTypeDef, _OptionalCreateAssetRequestRequestTypeDef
):
    pass

CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List["EgressEndpointTypeDef"],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
    },
)
_OptionalCreatePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackagingConfigurationRequestRequestTypeDef",
    {
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "MssPackage": "MssPackageTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreatePackagingConfigurationRequestRequestTypeDef(
    _RequiredCreatePackagingConfigurationRequestRequestTypeDef,
    _OptionalCreatePackagingConfigurationRequestRequestTypeDef,
):
    pass

CreatePackagingConfigurationResponseTypeDef = TypedDict(
    "CreatePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePackagingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalCreatePackagingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackagingGroupRequestRequestTypeDef",
    {
        "Authorization": "AuthorizationTypeDef",
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreatePackagingGroupRequestRequestTypeDef(
    _RequiredCreatePackagingGroupRequestRequestTypeDef,
    _OptionalCreatePackagingGroupRequestRequestTypeDef,
):
    pass

CreatePackagingGroupResponseTypeDef = TypedDict(
    "CreatePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)

DashManifestTypeDef = TypedDict(
    "DashManifestTypeDef",
    {
        "ManifestLayout": ManifestLayoutType,
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": ProfileType,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredDashPackageTypeDef = TypedDict(
    "_RequiredDashPackageTypeDef",
    {
        "DashManifests": List["DashManifestTypeDef"],
    },
)
_OptionalDashPackageTypeDef = TypedDict(
    "_OptionalDashPackageTypeDef",
    {
        "Encryption": "DashEncryptionTypeDef",
        "IncludeEncoderConfigurationInSegments": bool,
        "PeriodTriggers": List[Literal["ADS"]],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": SegmentTemplateFormatType,
    },
    total=False,
)

class DashPackageTypeDef(_RequiredDashPackageTypeDef, _OptionalDashPackageTypeDef):
    pass

DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "DeletePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePackagingGroupRequestRequestTypeDef = TypedDict(
    "DeletePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAssetRequestRequestTypeDef = TypedDict(
    "DescribeAssetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAssetResponseTypeDef = TypedDict(
    "DescribeAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List["EgressEndpointTypeDef"],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribePackagingConfigurationResponseTypeDef = TypedDict(
    "DescribePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagingGroupRequestRequestTypeDef = TypedDict(
    "DescribePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribePackagingGroupResponseTypeDef = TypedDict(
    "DescribePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EgressAccessLogsTypeDef = TypedDict(
    "EgressAccessLogsTypeDef",
    {
        "LogGroupName": str,
    },
    total=False,
)

EgressEndpointTypeDef = TypedDict(
    "EgressEndpointTypeDef",
    {
        "PackagingConfigurationId": str,
        "Url": str,
    },
    total=False,
)

_RequiredHlsEncryptionTypeDef = TypedDict(
    "_RequiredHlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)
_OptionalHlsEncryptionTypeDef = TypedDict(
    "_OptionalHlsEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": EncryptionMethodType,
    },
    total=False,
)

class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, _OptionalHlsEncryptionTypeDef):
    pass

HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "AdMarkers": AdMarkersType,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredHlsPackageTypeDef = TypedDict(
    "_RequiredHlsPackageTypeDef",
    {
        "HlsManifests": List["HlsManifestTypeDef"],
    },
)
_OptionalHlsPackageTypeDef = TypedDict(
    "_OptionalHlsPackageTypeDef",
    {
        "Encryption": "HlsEncryptionTypeDef",
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)

class HlsPackageTypeDef(_RequiredHlsPackageTypeDef, _OptionalHlsPackageTypeDef):
    pass

ListAssetsRequestRequestTypeDef = TypedDict(
    "ListAssetsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "PackagingGroupId": str,
    },
    total=False,
)

ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {
        "Assets": List["AssetShallowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListPackagingConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "PackagingGroupId": str,
    },
    total=False,
)

ListPackagingConfigurationsResponseTypeDef = TypedDict(
    "ListPackagingConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingConfigurations": List["PackagingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagingGroupsRequestRequestTypeDef = TypedDict(
    "ListPackagingGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPackagingGroupsResponseTypeDef = TypedDict(
    "ListPackagingGroupsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingGroups": List["PackagingGroupTypeDef"],
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

MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)

MssManifestTypeDef = TypedDict(
    "MssManifestTypeDef",
    {
        "ManifestName": str,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredMssPackageTypeDef = TypedDict(
    "_RequiredMssPackageTypeDef",
    {
        "MssManifests": List["MssManifestTypeDef"],
    },
)
_OptionalMssPackageTypeDef = TypedDict(
    "_OptionalMssPackageTypeDef",
    {
        "Encryption": "MssEncryptionTypeDef",
        "SegmentDurationSeconds": int,
    },
    total=False,
)

class MssPackageTypeDef(_RequiredMssPackageTypeDef, _OptionalMssPackageTypeDef):
    pass

PackagingConfigurationTypeDef = TypedDict(
    "PackagingConfigurationTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

PackagingGroupTypeDef = TypedDict(
    "PackagingGroupTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
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

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "RoleArn": str,
        "SystemIds": List[str],
        "Url": str,
    },
)

StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": int,
        "MinVideoBitsPerSecond": int,
        "StreamOrder": StreamOrderType,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdatePackagingGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdatePackagingGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePackagingGroupRequestRequestTypeDef",
    {
        "Authorization": "AuthorizationTypeDef",
    },
    total=False,
)

class UpdatePackagingGroupRequestRequestTypeDef(
    _RequiredUpdatePackagingGroupRequestRequestTypeDef,
    _OptionalUpdatePackagingGroupRequestRequestTypeDef,
):
    pass

UpdatePackagingGroupResponseTypeDef = TypedDict(
    "UpdatePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
