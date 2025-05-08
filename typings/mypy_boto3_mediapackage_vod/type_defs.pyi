"""
Type annotations for mediapackage-vod service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_mediapackage_vod.type_defs import AssetShallowTypeDef

    data: AssetShallowTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import (
    AdMarkersType,
    EncryptionMethodType,
    ManifestLayoutType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ProfileType,
    ScteMarkersSourceType,
    SegmentTemplateFormatType,
    StreamOrderType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssetShallowTypeDef",
    "AuthorizationTypeDef",
    "CmafEncryptionOutputTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageOutputTypeDef",
    "CmafPackageTypeDef",
    "CmafPackageUnionTypeDef",
    "ConfigureLogsRequestTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateAssetRequestTypeDef",
    "CreateAssetResponseTypeDef",
    "CreatePackagingConfigurationRequestTypeDef",
    "CreatePackagingConfigurationResponseTypeDef",
    "CreatePackagingGroupRequestTypeDef",
    "CreatePackagingGroupResponseTypeDef",
    "DashEncryptionOutputTypeDef",
    "DashEncryptionTypeDef",
    "DashManifestTypeDef",
    "DashPackageOutputTypeDef",
    "DashPackageTypeDef",
    "DashPackageUnionTypeDef",
    "DeleteAssetRequestTypeDef",
    "DeletePackagingConfigurationRequestTypeDef",
    "DeletePackagingGroupRequestTypeDef",
    "DescribeAssetRequestTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribePackagingConfigurationRequestTypeDef",
    "DescribePackagingConfigurationResponseTypeDef",
    "DescribePackagingGroupRequestTypeDef",
    "DescribePackagingGroupResponseTypeDef",
    "EgressAccessLogsTypeDef",
    "EgressEndpointTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "HlsEncryptionOutputTypeDef",
    "HlsEncryptionTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageOutputTypeDef",
    "HlsPackageTypeDef",
    "HlsPackageUnionTypeDef",
    "ListAssetsRequestPaginateTypeDef",
    "ListAssetsRequestTypeDef",
    "ListAssetsResponseTypeDef",
    "ListPackagingConfigurationsRequestPaginateTypeDef",
    "ListPackagingConfigurationsRequestTypeDef",
    "ListPackagingConfigurationsResponseTypeDef",
    "ListPackagingGroupsRequestPaginateTypeDef",
    "ListPackagingGroupsRequestTypeDef",
    "ListPackagingGroupsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MssEncryptionOutputTypeDef",
    "MssEncryptionTypeDef",
    "MssManifestTypeDef",
    "MssPackageOutputTypeDef",
    "MssPackageTypeDef",
    "MssPackageUnionTypeDef",
    "PackagingConfigurationTypeDef",
    "PackagingGroupTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SpekeKeyProviderOutputTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdatePackagingGroupRequestTypeDef",
    "UpdatePackagingGroupResponseTypeDef",
)

class AssetShallowTypeDef(TypedDict):
    Arn: NotRequired[str]
    CreatedAt: NotRequired[str]
    Id: NotRequired[str]
    PackagingGroupId: NotRequired[str]
    ResourceId: NotRequired[str]
    SourceArn: NotRequired[str]
    SourceRoleArn: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class AuthorizationTypeDef(TypedDict):
    CdnIdentifierSecret: str
    SecretsRoleArn: str

class EgressAccessLogsTypeDef(TypedDict):
    LogGroupName: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateAssetRequestTypeDef(TypedDict):
    Id: str
    PackagingGroupId: str
    SourceArn: str
    SourceRoleArn: str
    ResourceId: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class EgressEndpointTypeDef(TypedDict):
    PackagingConfigurationId: NotRequired[str]
    Status: NotRequired[str]
    Url: NotRequired[str]

class StreamSelectionTypeDef(TypedDict):
    MaxVideoBitsPerSecond: NotRequired[int]
    MinVideoBitsPerSecond: NotRequired[int]
    StreamOrder: NotRequired[StreamOrderType]

class DeleteAssetRequestTypeDef(TypedDict):
    Id: str

class DeletePackagingConfigurationRequestTypeDef(TypedDict):
    Id: str

class DeletePackagingGroupRequestTypeDef(TypedDict):
    Id: str

class DescribeAssetRequestTypeDef(TypedDict):
    Id: str

class DescribePackagingConfigurationRequestTypeDef(TypedDict):
    Id: str

class DescribePackagingGroupRequestTypeDef(TypedDict):
    Id: str

class EncryptionContractConfigurationTypeDef(TypedDict):
    PresetSpeke20Audio: PresetSpeke20AudioType
    PresetSpeke20Video: PresetSpeke20VideoType

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAssetsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    PackagingGroupId: NotRequired[str]

class ListPackagingConfigurationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    PackagingGroupId: NotRequired[str]

class ListPackagingGroupsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdatePackagingGroupRequestTypeDef(TypedDict):
    Id: str
    Authorization: NotRequired[AuthorizationTypeDef]

class ConfigureLogsRequestTypeDef(TypedDict):
    Id: str
    EgressAccessLogs: NotRequired[EgressAccessLogsTypeDef]

class CreatePackagingGroupRequestTypeDef(TypedDict):
    Id: str
    Authorization: NotRequired[AuthorizationTypeDef]
    EgressAccessLogs: NotRequired[EgressAccessLogsTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class PackagingGroupTypeDef(TypedDict):
    ApproximateAssetCount: NotRequired[int]
    Arn: NotRequired[str]
    Authorization: NotRequired[AuthorizationTypeDef]
    CreatedAt: NotRequired[str]
    DomainName: NotRequired[str]
    EgressAccessLogs: NotRequired[EgressAccessLogsTypeDef]
    Id: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class ConfigureLogsResponseTypeDef(TypedDict):
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackagingGroupResponseTypeDef(TypedDict):
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackagingGroupResponseTypeDef(TypedDict):
    ApproximateAssetCount: int
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssetsResponseTypeDef(TypedDict):
    Assets: List[AssetShallowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackagingGroupResponseTypeDef(TypedDict):
    ApproximateAssetCount: int
    Arn: str
    Authorization: AuthorizationTypeDef
    CreatedAt: str
    DomainName: str
    EgressAccessLogs: EgressAccessLogsTypeDef
    Id: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssetResponseTypeDef(TypedDict):
    Arn: str
    CreatedAt: str
    EgressEndpoints: List[EgressEndpointTypeDef]
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAssetResponseTypeDef(TypedDict):
    Arn: str
    CreatedAt: str
    EgressEndpoints: List[EgressEndpointTypeDef]
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DashManifestTypeDef(TypedDict):
    ManifestLayout: NotRequired[ManifestLayoutType]
    ManifestName: NotRequired[str]
    MinBufferTimeSeconds: NotRequired[int]
    Profile: NotRequired[ProfileType]
    ScteMarkersSource: NotRequired[ScteMarkersSourceType]
    StreamSelection: NotRequired[StreamSelectionTypeDef]

class HlsManifestTypeDef(TypedDict):
    AdMarkers: NotRequired[AdMarkersType]
    IncludeIframeOnlyStream: NotRequired[bool]
    ManifestName: NotRequired[str]
    ProgramDateTimeIntervalSeconds: NotRequired[int]
    RepeatExtXKey: NotRequired[bool]
    StreamSelection: NotRequired[StreamSelectionTypeDef]

class MssManifestTypeDef(TypedDict):
    ManifestName: NotRequired[str]
    StreamSelection: NotRequired[StreamSelectionTypeDef]

class SpekeKeyProviderOutputTypeDef(TypedDict):
    RoleArn: str
    SystemIds: List[str]
    Url: str
    EncryptionContractConfiguration: NotRequired[EncryptionContractConfigurationTypeDef]

class SpekeKeyProviderTypeDef(TypedDict):
    RoleArn: str
    SystemIds: Sequence[str]
    Url: str
    EncryptionContractConfiguration: NotRequired[EncryptionContractConfigurationTypeDef]

class ListAssetsRequestPaginateTypeDef(TypedDict):
    PackagingGroupId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPackagingConfigurationsRequestPaginateTypeDef(TypedDict):
    PackagingGroupId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPackagingGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPackagingGroupsResponseTypeDef(TypedDict):
    PackagingGroups: List[PackagingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CmafEncryptionOutputTypeDef(TypedDict):
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef
    ConstantInitializationVector: NotRequired[str]

class DashEncryptionOutputTypeDef(TypedDict):
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef

class HlsEncryptionOutputTypeDef(TypedDict):
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef
    ConstantInitializationVector: NotRequired[str]
    EncryptionMethod: NotRequired[EncryptionMethodType]

class MssEncryptionOutputTypeDef(TypedDict):
    SpekeKeyProvider: SpekeKeyProviderOutputTypeDef

class CmafEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: NotRequired[str]

class DashEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: SpekeKeyProviderTypeDef

class HlsEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: SpekeKeyProviderTypeDef
    ConstantInitializationVector: NotRequired[str]
    EncryptionMethod: NotRequired[EncryptionMethodType]

class MssEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: SpekeKeyProviderTypeDef

class CmafPackageOutputTypeDef(TypedDict):
    HlsManifests: List[HlsManifestTypeDef]
    Encryption: NotRequired[CmafEncryptionOutputTypeDef]
    IncludeEncoderConfigurationInSegments: NotRequired[bool]
    SegmentDurationSeconds: NotRequired[int]

class DashPackageOutputTypeDef(TypedDict):
    DashManifests: List[DashManifestTypeDef]
    Encryption: NotRequired[DashEncryptionOutputTypeDef]
    IncludeEncoderConfigurationInSegments: NotRequired[bool]
    IncludeIframeOnlyStream: NotRequired[bool]
    PeriodTriggers: NotRequired[List[Literal["ADS"]]]
    SegmentDurationSeconds: NotRequired[int]
    SegmentTemplateFormat: NotRequired[SegmentTemplateFormatType]

class HlsPackageOutputTypeDef(TypedDict):
    HlsManifests: List[HlsManifestTypeDef]
    Encryption: NotRequired[HlsEncryptionOutputTypeDef]
    IncludeDvbSubtitles: NotRequired[bool]
    SegmentDurationSeconds: NotRequired[int]
    UseAudioRenditionGroup: NotRequired[bool]

class MssPackageOutputTypeDef(TypedDict):
    MssManifests: List[MssManifestTypeDef]
    Encryption: NotRequired[MssEncryptionOutputTypeDef]
    SegmentDurationSeconds: NotRequired[int]

class CmafPackageTypeDef(TypedDict):
    HlsManifests: Sequence[HlsManifestTypeDef]
    Encryption: NotRequired[CmafEncryptionTypeDef]
    IncludeEncoderConfigurationInSegments: NotRequired[bool]
    SegmentDurationSeconds: NotRequired[int]

class DashPackageTypeDef(TypedDict):
    DashManifests: Sequence[DashManifestTypeDef]
    Encryption: NotRequired[DashEncryptionTypeDef]
    IncludeEncoderConfigurationInSegments: NotRequired[bool]
    IncludeIframeOnlyStream: NotRequired[bool]
    PeriodTriggers: NotRequired[Sequence[Literal["ADS"]]]
    SegmentDurationSeconds: NotRequired[int]
    SegmentTemplateFormat: NotRequired[SegmentTemplateFormatType]

class HlsPackageTypeDef(TypedDict):
    HlsManifests: Sequence[HlsManifestTypeDef]
    Encryption: NotRequired[HlsEncryptionTypeDef]
    IncludeDvbSubtitles: NotRequired[bool]
    SegmentDurationSeconds: NotRequired[int]
    UseAudioRenditionGroup: NotRequired[bool]

class MssPackageTypeDef(TypedDict):
    MssManifests: Sequence[MssManifestTypeDef]
    Encryption: NotRequired[MssEncryptionTypeDef]
    SegmentDurationSeconds: NotRequired[int]

class CreatePackagingConfigurationResponseTypeDef(TypedDict):
    Arn: str
    CmafPackage: CmafPackageOutputTypeDef
    CreatedAt: str
    DashPackage: DashPackageOutputTypeDef
    HlsPackage: HlsPackageOutputTypeDef
    Id: str
    MssPackage: MssPackageOutputTypeDef
    PackagingGroupId: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackagingConfigurationResponseTypeDef(TypedDict):
    Arn: str
    CmafPackage: CmafPackageOutputTypeDef
    CreatedAt: str
    DashPackage: DashPackageOutputTypeDef
    HlsPackage: HlsPackageOutputTypeDef
    Id: str
    MssPackage: MssPackageOutputTypeDef
    PackagingGroupId: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PackagingConfigurationTypeDef(TypedDict):
    Arn: NotRequired[str]
    CmafPackage: NotRequired[CmafPackageOutputTypeDef]
    CreatedAt: NotRequired[str]
    DashPackage: NotRequired[DashPackageOutputTypeDef]
    HlsPackage: NotRequired[HlsPackageOutputTypeDef]
    Id: NotRequired[str]
    MssPackage: NotRequired[MssPackageOutputTypeDef]
    PackagingGroupId: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

CmafPackageUnionTypeDef = Union[CmafPackageTypeDef, CmafPackageOutputTypeDef]
DashPackageUnionTypeDef = Union[DashPackageTypeDef, DashPackageOutputTypeDef]
HlsPackageUnionTypeDef = Union[HlsPackageTypeDef, HlsPackageOutputTypeDef]
MssPackageUnionTypeDef = Union[MssPackageTypeDef, MssPackageOutputTypeDef]

class ListPackagingConfigurationsResponseTypeDef(TypedDict):
    PackagingConfigurations: List[PackagingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreatePackagingConfigurationRequestTypeDef(TypedDict):
    Id: str
    PackagingGroupId: str
    CmafPackage: NotRequired[CmafPackageUnionTypeDef]
    DashPackage: NotRequired[DashPackageUnionTypeDef]
    HlsPackage: NotRequired[HlsPackageUnionTypeDef]
    MssPackage: NotRequired[MssPackageUnionTypeDef]
    Tags: NotRequired[Mapping[str, str]]
