"""
Type annotations for mediapackagev2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackagev2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediapackagev2.type_defs import ChannelGroupListConfigurationTypeDef

    data: ChannelGroupListConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    CmafEncryptionMethodType,
    ContainerTypeType,
    DrmSystemType,
    PresetSpeke20AudioType,
    PresetSpeke20VideoType,
    ScteFilterType,
    TsEncryptionMethodType,
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
    "ChannelGroupListConfigurationTypeDef",
    "ChannelListConfigurationTypeDef",
    "CreateChannelGroupRequestRequestTypeDef",
    "CreateChannelGroupResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateHlsManifestConfigurationTypeDef",
    "CreateLowLatencyHlsManifestConfigurationTypeDef",
    "CreateOriginEndpointRequestRequestTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DeleteChannelGroupRequestRequestTypeDef",
    "DeleteChannelPolicyRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteOriginEndpointPolicyRequestRequestTypeDef",
    "DeleteOriginEndpointRequestRequestTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "EncryptionMethodTypeDef",
    "EncryptionTypeDef",
    "FilterConfigurationTypeDef",
    "GetChannelGroupRequestRequestTypeDef",
    "GetChannelGroupResponseTypeDef",
    "GetChannelPolicyRequestRequestTypeDef",
    "GetChannelPolicyResponseTypeDef",
    "GetChannelRequestRequestTypeDef",
    "GetChannelResponseTypeDef",
    "GetHlsManifestConfigurationTypeDef",
    "GetLowLatencyHlsManifestConfigurationTypeDef",
    "GetOriginEndpointPolicyRequestRequestTypeDef",
    "GetOriginEndpointPolicyResponseTypeDef",
    "GetOriginEndpointRequestRequestTypeDef",
    "GetOriginEndpointResponseTypeDef",
    "IngestEndpointTypeDef",
    "ListChannelGroupsRequestRequestTypeDef",
    "ListChannelGroupsResponseTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListHlsManifestConfigurationTypeDef",
    "ListLowLatencyHlsManifestConfigurationTypeDef",
    "ListOriginEndpointsRequestRequestTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OriginEndpointListConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PutChannelPolicyRequestRequestTypeDef",
    "PutOriginEndpointPolicyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "ScteHlsTypeDef",
    "ScteTypeDef",
    "SegmentTypeDef",
    "SpekeKeyProviderTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelGroupRequestRequestTypeDef",
    "UpdateChannelGroupResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateOriginEndpointRequestRequestTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
)

_RequiredChannelGroupListConfigurationTypeDef = TypedDict(
    "_RequiredChannelGroupListConfigurationTypeDef",
    {
        "ChannelGroupName": str,
        "Arn": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
)
_OptionalChannelGroupListConfigurationTypeDef = TypedDict(
    "_OptionalChannelGroupListConfigurationTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class ChannelGroupListConfigurationTypeDef(
    _RequiredChannelGroupListConfigurationTypeDef, _OptionalChannelGroupListConfigurationTypeDef
):
    pass

_RequiredChannelListConfigurationTypeDef = TypedDict(
    "_RequiredChannelListConfigurationTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelGroupName": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
    },
)
_OptionalChannelListConfigurationTypeDef = TypedDict(
    "_OptionalChannelListConfigurationTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class ChannelListConfigurationTypeDef(
    _RequiredChannelListConfigurationTypeDef, _OptionalChannelListConfigurationTypeDef
):
    pass

_RequiredCreateChannelGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelGroupRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
    },
)
_OptionalCreateChannelGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelGroupRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateChannelGroupRequestRequestTypeDef(
    _RequiredCreateChannelGroupRequestRequestTypeDef,
    _OptionalCreateChannelGroupRequestRequestTypeDef,
):
    pass

CreateChannelGroupResponseTypeDef = TypedDict(
    "CreateChannelGroupResponseTypeDef",
    {
        "ChannelGroupName": str,
        "Arn": str,
        "EgressDomain": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChannelRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)
_OptionalCreateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChannelRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateChannelRequestRequestTypeDef(
    _RequiredCreateChannelRequestRequestTypeDef, _OptionalCreateChannelRequestRequestTypeDef
):
    pass

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelGroupName": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "IngestEndpoints": List["IngestEndpointTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHlsManifestConfigurationTypeDef = TypedDict(
    "_RequiredCreateHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
    },
)
_OptionalCreateHlsManifestConfigurationTypeDef = TypedDict(
    "_OptionalCreateHlsManifestConfigurationTypeDef",
    {
        "ChildManifestName": str,
        "ScteHls": "ScteHlsTypeDef",
        "ManifestWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "FilterConfiguration": "FilterConfigurationTypeDef",
    },
    total=False,
)

class CreateHlsManifestConfigurationTypeDef(
    _RequiredCreateHlsManifestConfigurationTypeDef, _OptionalCreateHlsManifestConfigurationTypeDef
):
    pass

_RequiredCreateLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "_RequiredCreateLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
    },
)
_OptionalCreateLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "_OptionalCreateLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ChildManifestName": str,
        "ScteHls": "ScteHlsTypeDef",
        "ManifestWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "FilterConfiguration": "FilterConfigurationTypeDef",
    },
    total=False,
)

class CreateLowLatencyHlsManifestConfigurationTypeDef(
    _RequiredCreateLowLatencyHlsManifestConfigurationTypeDef,
    _OptionalCreateLowLatencyHlsManifestConfigurationTypeDef,
):
    pass

_RequiredCreateOriginEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOriginEndpointRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
    },
)
_OptionalCreateOriginEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOriginEndpointRequestRequestTypeDef",
    {
        "Segment": "SegmentTypeDef",
        "ClientToken": str,
        "Description": str,
        "StartoverWindowSeconds": int,
        "HlsManifests": List["CreateHlsManifestConfigurationTypeDef"],
        "LowLatencyHlsManifests": List["CreateLowLatencyHlsManifestConfigurationTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateOriginEndpointRequestRequestTypeDef(
    _RequiredCreateOriginEndpointRequestRequestTypeDef,
    _OptionalCreateOriginEndpointRequestRequestTypeDef,
):
    pass

CreateOriginEndpointResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Segment": "SegmentTypeDef",
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "StartoverWindowSeconds": int,
        "HlsManifests": List["GetHlsManifestConfigurationTypeDef"],
        "LowLatencyHlsManifests": List["GetLowLatencyHlsManifestConfigurationTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChannelGroupRequestRequestTypeDef = TypedDict(
    "DeleteChannelGroupRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
    },
)

DeleteChannelPolicyRequestRequestTypeDef = TypedDict(
    "DeleteChannelPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)

DeleteOriginEndpointPolicyRequestRequestTypeDef = TypedDict(
    "DeleteOriginEndpointPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
    },
)

DeleteOriginEndpointRequestRequestTypeDef = TypedDict(
    "DeleteOriginEndpointRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
    },
)

EncryptionContractConfigurationTypeDef = TypedDict(
    "EncryptionContractConfigurationTypeDef",
    {
        "PresetSpeke20Audio": PresetSpeke20AudioType,
        "PresetSpeke20Video": PresetSpeke20VideoType,
    },
)

EncryptionMethodTypeDef = TypedDict(
    "EncryptionMethodTypeDef",
    {
        "TsEncryptionMethod": TsEncryptionMethodType,
        "CmafEncryptionMethod": CmafEncryptionMethodType,
    },
    total=False,
)

_RequiredEncryptionTypeDef = TypedDict(
    "_RequiredEncryptionTypeDef",
    {
        "EncryptionMethod": "EncryptionMethodTypeDef",
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)
_OptionalEncryptionTypeDef = TypedDict(
    "_OptionalEncryptionTypeDef",
    {
        "ConstantInitializationVector": str,
        "KeyRotationIntervalSeconds": int,
    },
    total=False,
)

class EncryptionTypeDef(_RequiredEncryptionTypeDef, _OptionalEncryptionTypeDef):
    pass

FilterConfigurationTypeDef = TypedDict(
    "FilterConfigurationTypeDef",
    {
        "ManifestFilter": str,
        "Start": Union[datetime, str],
        "End": Union[datetime, str],
        "TimeDelaySeconds": int,
    },
    total=False,
)

GetChannelGroupRequestRequestTypeDef = TypedDict(
    "GetChannelGroupRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
    },
)

GetChannelGroupResponseTypeDef = TypedDict(
    "GetChannelGroupResponseTypeDef",
    {
        "ChannelGroupName": str,
        "Arn": str,
        "EgressDomain": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelPolicyRequestRequestTypeDef = TypedDict(
    "GetChannelPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)

GetChannelPolicyResponseTypeDef = TypedDict(
    "GetChannelPolicyResponseTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelRequestRequestTypeDef = TypedDict(
    "GetChannelRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)

GetChannelResponseTypeDef = TypedDict(
    "GetChannelResponseTypeDef",
    {
        "Arn": str,
        "ChannelName": str,
        "ChannelGroupName": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "IngestEndpoints": List["IngestEndpointTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetHlsManifestConfigurationTypeDef = TypedDict(
    "_RequiredGetHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "Url": str,
    },
)
_OptionalGetHlsManifestConfigurationTypeDef = TypedDict(
    "_OptionalGetHlsManifestConfigurationTypeDef",
    {
        "ChildManifestName": str,
        "ManifestWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "ScteHls": "ScteHlsTypeDef",
        "FilterConfiguration": "FilterConfigurationTypeDef",
    },
    total=False,
)

class GetHlsManifestConfigurationTypeDef(
    _RequiredGetHlsManifestConfigurationTypeDef, _OptionalGetHlsManifestConfigurationTypeDef
):
    pass

_RequiredGetLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "_RequiredGetLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
        "Url": str,
    },
)
_OptionalGetLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "_OptionalGetLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ChildManifestName": str,
        "ManifestWindowSeconds": int,
        "ProgramDateTimeIntervalSeconds": int,
        "ScteHls": "ScteHlsTypeDef",
        "FilterConfiguration": "FilterConfigurationTypeDef",
    },
    total=False,
)

class GetLowLatencyHlsManifestConfigurationTypeDef(
    _RequiredGetLowLatencyHlsManifestConfigurationTypeDef,
    _OptionalGetLowLatencyHlsManifestConfigurationTypeDef,
):
    pass

GetOriginEndpointPolicyRequestRequestTypeDef = TypedDict(
    "GetOriginEndpointPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
    },
)

GetOriginEndpointPolicyResponseTypeDef = TypedDict(
    "GetOriginEndpointPolicyResponseTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOriginEndpointRequestRequestTypeDef = TypedDict(
    "GetOriginEndpointRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
    },
)

GetOriginEndpointResponseTypeDef = TypedDict(
    "GetOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Segment": "SegmentTypeDef",
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "StartoverWindowSeconds": int,
        "HlsManifests": List["GetHlsManifestConfigurationTypeDef"],
        "LowLatencyHlsManifests": List["GetLowLatencyHlsManifestConfigurationTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef",
    {
        "Id": str,
        "Url": str,
    },
    total=False,
)

ListChannelGroupsRequestRequestTypeDef = TypedDict(
    "ListChannelGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListChannelGroupsResponseTypeDef = TypedDict(
    "ListChannelGroupsResponseTypeDef",
    {
        "Items": List["ChannelGroupListConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChannelsRequestRequestTypeDef = TypedDict(
    "_RequiredListChannelsRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
    },
)
_OptionalListChannelsRequestRequestTypeDef = TypedDict(
    "_OptionalListChannelsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChannelsRequestRequestTypeDef(
    _RequiredListChannelsRequestRequestTypeDef, _OptionalListChannelsRequestRequestTypeDef
):
    pass

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Items": List["ChannelListConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHlsManifestConfigurationTypeDef = TypedDict(
    "_RequiredListHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
    },
)
_OptionalListHlsManifestConfigurationTypeDef = TypedDict(
    "_OptionalListHlsManifestConfigurationTypeDef",
    {
        "ChildManifestName": str,
        "Url": str,
    },
    total=False,
)

class ListHlsManifestConfigurationTypeDef(
    _RequiredListHlsManifestConfigurationTypeDef, _OptionalListHlsManifestConfigurationTypeDef
):
    pass

_RequiredListLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "_RequiredListLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ManifestName": str,
    },
)
_OptionalListLowLatencyHlsManifestConfigurationTypeDef = TypedDict(
    "_OptionalListLowLatencyHlsManifestConfigurationTypeDef",
    {
        "ChildManifestName": str,
        "Url": str,
    },
    total=False,
)

class ListLowLatencyHlsManifestConfigurationTypeDef(
    _RequiredListLowLatencyHlsManifestConfigurationTypeDef,
    _OptionalListLowLatencyHlsManifestConfigurationTypeDef,
):
    pass

_RequiredListOriginEndpointsRequestRequestTypeDef = TypedDict(
    "_RequiredListOriginEndpointsRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)
_OptionalListOriginEndpointsRequestRequestTypeDef = TypedDict(
    "_OptionalListOriginEndpointsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListOriginEndpointsRequestRequestTypeDef(
    _RequiredListOriginEndpointsRequestRequestTypeDef,
    _OptionalListOriginEndpointsRequestRequestTypeDef,
):
    pass

ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {
        "Items": List["OriginEndpointListConfigurationTypeDef"],
        "NextToken": str,
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

_RequiredOriginEndpointListConfigurationTypeDef = TypedDict(
    "_RequiredOriginEndpointListConfigurationTypeDef",
    {
        "Arn": str,
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
    },
)
_OptionalOriginEndpointListConfigurationTypeDef = TypedDict(
    "_OptionalOriginEndpointListConfigurationTypeDef",
    {
        "Description": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "HlsManifests": List["ListHlsManifestConfigurationTypeDef"],
        "LowLatencyHlsManifests": List["ListLowLatencyHlsManifestConfigurationTypeDef"],
    },
    total=False,
)

class OriginEndpointListConfigurationTypeDef(
    _RequiredOriginEndpointListConfigurationTypeDef, _OptionalOriginEndpointListConfigurationTypeDef
):
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

PutChannelPolicyRequestRequestTypeDef = TypedDict(
    "PutChannelPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "Policy": str,
    },
)

PutOriginEndpointPolicyRequestRequestTypeDef = TypedDict(
    "PutOriginEndpointPolicyRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "Policy": str,
    },
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

ScteHlsTypeDef = TypedDict(
    "ScteHlsTypeDef",
    {
        "AdMarkerHls": Literal["DATERANGE"],
    },
    total=False,
)

ScteTypeDef = TypedDict(
    "ScteTypeDef",
    {
        "ScteFilter": List[ScteFilterType],
    },
    total=False,
)

SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "SegmentDurationSeconds": int,
        "SegmentName": str,
        "TsUseAudioRenditionGroup": bool,
        "IncludeIframeOnlyStreams": bool,
        "TsIncludeDvbSubtitles": bool,
        "Scte": "ScteTypeDef",
        "Encryption": "EncryptionTypeDef",
    },
    total=False,
)

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "EncryptionContractConfiguration": "EncryptionContractConfigurationTypeDef",
        "ResourceId": str,
        "DrmSystems": List[DrmSystemType],
        "RoleArn": str,
        "Url": str,
    },
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

_RequiredUpdateChannelGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelGroupRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
    },
)
_OptionalUpdateChannelGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelGroupRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateChannelGroupRequestRequestTypeDef(
    _RequiredUpdateChannelGroupRequestRequestTypeDef,
    _OptionalUpdateChannelGroupRequestRequestTypeDef,
):
    pass

UpdateChannelGroupResponseTypeDef = TypedDict(
    "UpdateChannelGroupResponseTypeDef",
    {
        "ChannelGroupName": str,
        "Arn": str,
        "EgressDomain": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChannelRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateChannelRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
    },
)
_OptionalUpdateChannelRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateChannelRequestRequestTypeDef",
    {
        "Description": str,
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
        "Arn": str,
        "ChannelName": str,
        "ChannelGroupName": str,
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "IngestEndpoints": List["IngestEndpointTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateOriginEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOriginEndpointRequestRequestTypeDef",
    {
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
    },
)
_OptionalUpdateOriginEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOriginEndpointRequestRequestTypeDef",
    {
        "Segment": "SegmentTypeDef",
        "Description": str,
        "StartoverWindowSeconds": int,
        "HlsManifests": List["CreateHlsManifestConfigurationTypeDef"],
        "LowLatencyHlsManifests": List["CreateLowLatencyHlsManifestConfigurationTypeDef"],
    },
    total=False,
)

class UpdateOriginEndpointRequestRequestTypeDef(
    _RequiredUpdateOriginEndpointRequestRequestTypeDef,
    _OptionalUpdateOriginEndpointRequestRequestTypeDef,
):
    pass

UpdateOriginEndpointResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "ChannelGroupName": str,
        "ChannelName": str,
        "OriginEndpointName": str,
        "ContainerType": ContainerTypeType,
        "Segment": "SegmentTypeDef",
        "CreatedAt": datetime,
        "ModifiedAt": datetime,
        "Description": str,
        "StartoverWindowSeconds": int,
        "HlsManifests": List["GetHlsManifestConfigurationTypeDef"],
        "LowLatencyHlsManifests": List["GetLowLatencyHlsManifestConfigurationTypeDef"],
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
