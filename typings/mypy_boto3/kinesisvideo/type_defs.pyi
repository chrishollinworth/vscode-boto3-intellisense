"""
Type annotations for kinesisvideo service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesisvideo.type_defs import ChannelInfoTypeDef

    data: ChannelInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    APINameType,
    ChannelProtocolType,
    ChannelRoleType,
    ChannelTypeType,
    ConfigurationStatusType,
    FormatType,
    ImageSelectorTypeType,
    MediaStorageConfigurationStatusType,
    MediaUriTypeType,
    RecorderStatusType,
    StatusType,
    StrategyOnFullSizeType,
    SyncStatusType,
    UpdateDataRetentionOperationType,
    UploaderStatusType,
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
    "ChannelInfoTypeDef",
    "ChannelNameConditionTypeDef",
    "CreateSignalingChannelInputRequestTypeDef",
    "CreateSignalingChannelOutputTypeDef",
    "CreateStreamInputRequestTypeDef",
    "CreateStreamOutputTypeDef",
    "DeleteEdgeConfigurationInputRequestTypeDef",
    "DeleteSignalingChannelInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "DeletionConfigTypeDef",
    "DescribeEdgeConfigurationInputRequestTypeDef",
    "DescribeEdgeConfigurationOutputTypeDef",
    "DescribeImageGenerationConfigurationInputRequestTypeDef",
    "DescribeImageGenerationConfigurationOutputTypeDef",
    "DescribeMappedResourceConfigurationInputRequestTypeDef",
    "DescribeMappedResourceConfigurationOutputTypeDef",
    "DescribeMediaStorageConfigurationInputRequestTypeDef",
    "DescribeMediaStorageConfigurationOutputTypeDef",
    "DescribeNotificationConfigurationInputRequestTypeDef",
    "DescribeNotificationConfigurationOutputTypeDef",
    "DescribeSignalingChannelInputRequestTypeDef",
    "DescribeSignalingChannelOutputTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "DescribeStreamOutputTypeDef",
    "EdgeAgentStatusTypeDef",
    "EdgeConfigTypeDef",
    "GetDataEndpointInputRequestTypeDef",
    "GetDataEndpointOutputTypeDef",
    "GetSignalingChannelEndpointInputRequestTypeDef",
    "GetSignalingChannelEndpointOutputTypeDef",
    "ImageGenerationConfigurationTypeDef",
    "ImageGenerationDestinationConfigTypeDef",
    "LastRecorderStatusTypeDef",
    "LastUploaderStatusTypeDef",
    "ListEdgeAgentConfigurationsEdgeConfigTypeDef",
    "ListEdgeAgentConfigurationsInputRequestTypeDef",
    "ListEdgeAgentConfigurationsOutputTypeDef",
    "ListSignalingChannelsInputRequestTypeDef",
    "ListSignalingChannelsOutputTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "LocalSizeConfigTypeDef",
    "MappedResourceConfigurationListItemTypeDef",
    "MediaSourceConfigTypeDef",
    "MediaStorageConfigurationTypeDef",
    "NotificationConfigurationTypeDef",
    "NotificationDestinationConfigTypeDef",
    "PaginatorConfigTypeDef",
    "RecorderConfigTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ResponseMetadataTypeDef",
    "ScheduleConfigTypeDef",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "SingleMasterConfigurationTypeDef",
    "StartEdgeConfigurationUpdateInputRequestTypeDef",
    "StartEdgeConfigurationUpdateOutputTypeDef",
    "StreamInfoTypeDef",
    "StreamNameConditionTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagStreamInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UntagStreamInputRequestTypeDef",
    "UpdateDataRetentionInputRequestTypeDef",
    "UpdateImageGenerationConfigurationInputRequestTypeDef",
    "UpdateMediaStorageConfigurationInputRequestTypeDef",
    "UpdateNotificationConfigurationInputRequestTypeDef",
    "UpdateSignalingChannelInputRequestTypeDef",
    "UpdateStreamInputRequestTypeDef",
    "UploaderConfigTypeDef",
)

ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": ChannelTypeType,
        "ChannelStatus": StatusType,
        "CreationTime": datetime,
        "SingleMasterConfiguration": "SingleMasterConfigurationTypeDef",
        "Version": str,
    },
    total=False,
)

ChannelNameConditionTypeDef = TypedDict(
    "ChannelNameConditionTypeDef",
    {
        "ComparisonOperator": Literal["BEGINS_WITH"],
        "ComparisonValue": str,
    },
    total=False,
)

_RequiredCreateSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredCreateSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": str,
    },
)
_OptionalCreateSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalCreateSignalingChannelInputRequestTypeDef",
    {
        "ChannelType": ChannelTypeType,
        "SingleMasterConfiguration": "SingleMasterConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSignalingChannelInputRequestTypeDef(
    _RequiredCreateSignalingChannelInputRequestTypeDef,
    _OptionalCreateSignalingChannelInputRequestTypeDef,
):
    pass

CreateSignalingChannelOutputTypeDef = TypedDict(
    "CreateSignalingChannelOutputTypeDef",
    {
        "ChannelARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStreamInputRequestTypeDef = TypedDict(
    "_RequiredCreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalCreateStreamInputRequestTypeDef = TypedDict(
    "_OptionalCreateStreamInputRequestTypeDef",
    {
        "DeviceName": str,
        "MediaType": str,
        "KmsKeyId": str,
        "DataRetentionInHours": int,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateStreamInputRequestTypeDef(
    _RequiredCreateStreamInputRequestTypeDef, _OptionalCreateStreamInputRequestTypeDef
):
    pass

CreateStreamOutputTypeDef = TypedDict(
    "CreateStreamOutputTypeDef",
    {
        "StreamARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEdgeConfigurationInputRequestTypeDef = TypedDict(
    "DeleteEdgeConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

_RequiredDeleteSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredDeleteSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalDeleteSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalDeleteSignalingChannelInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class DeleteSignalingChannelInputRequestTypeDef(
    _RequiredDeleteSignalingChannelInputRequestTypeDef,
    _OptionalDeleteSignalingChannelInputRequestTypeDef,
):
    pass

_RequiredDeleteStreamInputRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamInputRequestTypeDef",
    {
        "StreamARN": str,
    },
)
_OptionalDeleteStreamInputRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class DeleteStreamInputRequestTypeDef(
    _RequiredDeleteStreamInputRequestTypeDef, _OptionalDeleteStreamInputRequestTypeDef
):
    pass

DeletionConfigTypeDef = TypedDict(
    "DeletionConfigTypeDef",
    {
        "EdgeRetentionInHours": int,
        "LocalSizeConfig": "LocalSizeConfigTypeDef",
        "DeleteAfterUpload": bool,
    },
    total=False,
)

DescribeEdgeConfigurationInputRequestTypeDef = TypedDict(
    "DescribeEdgeConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeEdgeConfigurationOutputTypeDef = TypedDict(
    "DescribeEdgeConfigurationOutputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "SyncStatus": SyncStatusType,
        "FailedStatusDetails": str,
        "EdgeConfig": "EdgeConfigTypeDef",
        "EdgeAgentStatus": "EdgeAgentStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageGenerationConfigurationInputRequestTypeDef = TypedDict(
    "DescribeImageGenerationConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeImageGenerationConfigurationOutputTypeDef = TypedDict(
    "DescribeImageGenerationConfigurationOutputTypeDef",
    {
        "ImageGenerationConfiguration": "ImageGenerationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMappedResourceConfigurationInputRequestTypeDef = TypedDict(
    "DescribeMappedResourceConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMappedResourceConfigurationOutputTypeDef = TypedDict(
    "DescribeMappedResourceConfigurationOutputTypeDef",
    {
        "MappedResourceConfigurationList": List["MappedResourceConfigurationListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMediaStorageConfigurationInputRequestTypeDef = TypedDict(
    "DescribeMediaStorageConfigurationInputRequestTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
    },
    total=False,
)

DescribeMediaStorageConfigurationOutputTypeDef = TypedDict(
    "DescribeMediaStorageConfigurationOutputTypeDef",
    {
        "MediaStorageConfiguration": "MediaStorageConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationConfigurationInputRequestTypeDef = TypedDict(
    "DescribeNotificationConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeNotificationConfigurationOutputTypeDef = TypedDict(
    "DescribeNotificationConfigurationOutputTypeDef",
    {
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSignalingChannelInputRequestTypeDef = TypedDict(
    "DescribeSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
    },
    total=False,
)

DescribeSignalingChannelOutputTypeDef = TypedDict(
    "DescribeSignalingChannelOutputTypeDef",
    {
        "ChannelInfo": "ChannelInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamInfo": "StreamInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EdgeAgentStatusTypeDef = TypedDict(
    "EdgeAgentStatusTypeDef",
    {
        "LastRecorderStatus": "LastRecorderStatusTypeDef",
        "LastUploaderStatus": "LastUploaderStatusTypeDef",
    },
    total=False,
)

_RequiredEdgeConfigTypeDef = TypedDict(
    "_RequiredEdgeConfigTypeDef",
    {
        "HubDeviceArn": str,
        "RecorderConfig": "RecorderConfigTypeDef",
    },
)
_OptionalEdgeConfigTypeDef = TypedDict(
    "_OptionalEdgeConfigTypeDef",
    {
        "UploaderConfig": "UploaderConfigTypeDef",
        "DeletionConfig": "DeletionConfigTypeDef",
    },
    total=False,
)

class EdgeConfigTypeDef(_RequiredEdgeConfigTypeDef, _OptionalEdgeConfigTypeDef):
    pass

_RequiredGetDataEndpointInputRequestTypeDef = TypedDict(
    "_RequiredGetDataEndpointInputRequestTypeDef",
    {
        "APIName": APINameType,
    },
)
_OptionalGetDataEndpointInputRequestTypeDef = TypedDict(
    "_OptionalGetDataEndpointInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class GetDataEndpointInputRequestTypeDef(
    _RequiredGetDataEndpointInputRequestTypeDef, _OptionalGetDataEndpointInputRequestTypeDef
):
    pass

GetDataEndpointOutputTypeDef = TypedDict(
    "GetDataEndpointOutputTypeDef",
    {
        "DataEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSignalingChannelEndpointInputRequestTypeDef = TypedDict(
    "_RequiredGetSignalingChannelEndpointInputRequestTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalGetSignalingChannelEndpointInputRequestTypeDef = TypedDict(
    "_OptionalGetSignalingChannelEndpointInputRequestTypeDef",
    {
        "SingleMasterChannelEndpointConfiguration": "SingleMasterChannelEndpointConfigurationTypeDef",
    },
    total=False,
)

class GetSignalingChannelEndpointInputRequestTypeDef(
    _RequiredGetSignalingChannelEndpointInputRequestTypeDef,
    _OptionalGetSignalingChannelEndpointInputRequestTypeDef,
):
    pass

GetSignalingChannelEndpointOutputTypeDef = TypedDict(
    "GetSignalingChannelEndpointOutputTypeDef",
    {
        "ResourceEndpointList": List["ResourceEndpointListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImageGenerationConfigurationTypeDef = TypedDict(
    "_RequiredImageGenerationConfigurationTypeDef",
    {
        "Status": ConfigurationStatusType,
        "ImageSelectorType": ImageSelectorTypeType,
        "DestinationConfig": "ImageGenerationDestinationConfigTypeDef",
        "SamplingInterval": int,
        "Format": FormatType,
    },
)
_OptionalImageGenerationConfigurationTypeDef = TypedDict(
    "_OptionalImageGenerationConfigurationTypeDef",
    {
        "FormatConfig": Dict[Literal["JPEGQuality"], str],
        "WidthPixels": int,
        "HeightPixels": int,
    },
    total=False,
)

class ImageGenerationConfigurationTypeDef(
    _RequiredImageGenerationConfigurationTypeDef, _OptionalImageGenerationConfigurationTypeDef
):
    pass

ImageGenerationDestinationConfigTypeDef = TypedDict(
    "ImageGenerationDestinationConfigTypeDef",
    {
        "Uri": str,
        "DestinationRegion": str,
    },
)

LastRecorderStatusTypeDef = TypedDict(
    "LastRecorderStatusTypeDef",
    {
        "JobStatusDetails": str,
        "LastCollectedTime": datetime,
        "LastUpdatedTime": datetime,
        "RecorderStatus": RecorderStatusType,
    },
    total=False,
)

LastUploaderStatusTypeDef = TypedDict(
    "LastUploaderStatusTypeDef",
    {
        "JobStatusDetails": str,
        "LastCollectedTime": datetime,
        "LastUpdatedTime": datetime,
        "UploaderStatus": UploaderStatusType,
    },
    total=False,
)

ListEdgeAgentConfigurationsEdgeConfigTypeDef = TypedDict(
    "ListEdgeAgentConfigurationsEdgeConfigTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "SyncStatus": SyncStatusType,
        "FailedStatusDetails": str,
        "EdgeConfig": "EdgeConfigTypeDef",
    },
    total=False,
)

_RequiredListEdgeAgentConfigurationsInputRequestTypeDef = TypedDict(
    "_RequiredListEdgeAgentConfigurationsInputRequestTypeDef",
    {
        "HubDeviceArn": str,
    },
)
_OptionalListEdgeAgentConfigurationsInputRequestTypeDef = TypedDict(
    "_OptionalListEdgeAgentConfigurationsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListEdgeAgentConfigurationsInputRequestTypeDef(
    _RequiredListEdgeAgentConfigurationsInputRequestTypeDef,
    _OptionalListEdgeAgentConfigurationsInputRequestTypeDef,
):
    pass

ListEdgeAgentConfigurationsOutputTypeDef = TypedDict(
    "ListEdgeAgentConfigurationsOutputTypeDef",
    {
        "EdgeConfigs": List["ListEdgeAgentConfigurationsEdgeConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSignalingChannelsInputRequestTypeDef = TypedDict(
    "ListSignalingChannelsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChannelNameCondition": "ChannelNameConditionTypeDef",
    },
    total=False,
)

ListSignalingChannelsOutputTypeDef = TypedDict(
    "ListSignalingChannelsOutputTypeDef",
    {
        "ChannelInfoList": List["ChannelInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "StreamNameCondition": "StreamNameConditionTypeDef",
    },
    total=False,
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamInfoList": List["StreamInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "NextToken": str,
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocalSizeConfigTypeDef = TypedDict(
    "LocalSizeConfigTypeDef",
    {
        "MaxLocalMediaSizeInMB": int,
        "StrategyOnFullSize": StrategyOnFullSizeType,
    },
    total=False,
)

MappedResourceConfigurationListItemTypeDef = TypedDict(
    "MappedResourceConfigurationListItemTypeDef",
    {
        "Type": str,
        "ARN": str,
    },
    total=False,
)

MediaSourceConfigTypeDef = TypedDict(
    "MediaSourceConfigTypeDef",
    {
        "MediaUriSecretArn": str,
        "MediaUriType": MediaUriTypeType,
    },
)

_RequiredMediaStorageConfigurationTypeDef = TypedDict(
    "_RequiredMediaStorageConfigurationTypeDef",
    {
        "Status": MediaStorageConfigurationStatusType,
    },
)
_OptionalMediaStorageConfigurationTypeDef = TypedDict(
    "_OptionalMediaStorageConfigurationTypeDef",
    {
        "StreamARN": str,
    },
    total=False,
)

class MediaStorageConfigurationTypeDef(
    _RequiredMediaStorageConfigurationTypeDef, _OptionalMediaStorageConfigurationTypeDef
):
    pass

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "Status": ConfigurationStatusType,
        "DestinationConfig": "NotificationDestinationConfigTypeDef",
    },
)

NotificationDestinationConfigTypeDef = TypedDict(
    "NotificationDestinationConfigTypeDef",
    {
        "Uri": str,
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

_RequiredRecorderConfigTypeDef = TypedDict(
    "_RequiredRecorderConfigTypeDef",
    {
        "MediaSourceConfig": "MediaSourceConfigTypeDef",
    },
)
_OptionalRecorderConfigTypeDef = TypedDict(
    "_OptionalRecorderConfigTypeDef",
    {
        "ScheduleConfig": "ScheduleConfigTypeDef",
    },
    total=False,
)

class RecorderConfigTypeDef(_RequiredRecorderConfigTypeDef, _OptionalRecorderConfigTypeDef):
    pass

ResourceEndpointListItemTypeDef = TypedDict(
    "ResourceEndpointListItemTypeDef",
    {
        "Protocol": ChannelProtocolType,
        "ResourceEndpoint": str,
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

ScheduleConfigTypeDef = TypedDict(
    "ScheduleConfigTypeDef",
    {
        "ScheduleExpression": str,
        "DurationInSeconds": int,
    },
)

SingleMasterChannelEndpointConfigurationTypeDef = TypedDict(
    "SingleMasterChannelEndpointConfigurationTypeDef",
    {
        "Protocols": List[ChannelProtocolType],
        "Role": ChannelRoleType,
    },
    total=False,
)

SingleMasterConfigurationTypeDef = TypedDict(
    "SingleMasterConfigurationTypeDef",
    {
        "MessageTtlSeconds": int,
    },
    total=False,
)

_RequiredStartEdgeConfigurationUpdateInputRequestTypeDef = TypedDict(
    "_RequiredStartEdgeConfigurationUpdateInputRequestTypeDef",
    {
        "EdgeConfig": "EdgeConfigTypeDef",
    },
)
_OptionalStartEdgeConfigurationUpdateInputRequestTypeDef = TypedDict(
    "_OptionalStartEdgeConfigurationUpdateInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class StartEdgeConfigurationUpdateInputRequestTypeDef(
    _RequiredStartEdgeConfigurationUpdateInputRequestTypeDef,
    _OptionalStartEdgeConfigurationUpdateInputRequestTypeDef,
):
    pass

StartEdgeConfigurationUpdateOutputTypeDef = TypedDict(
    "StartEdgeConfigurationUpdateOutputTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "SyncStatus": SyncStatusType,
        "FailedStatusDetails": str,
        "EdgeConfig": "EdgeConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": StatusType,
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)

StreamNameConditionTypeDef = TypedDict(
    "StreamNameConditionTypeDef",
    {
        "ComparisonOperator": Literal["BEGINS_WITH"],
        "ComparisonValue": str,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

_RequiredTagStreamInputRequestTypeDef = TypedDict(
    "_RequiredTagStreamInputRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
)
_OptionalTagStreamInputRequestTypeDef = TypedDict(
    "_OptionalTagStreamInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

class TagStreamInputRequestTypeDef(
    _RequiredTagStreamInputRequestTypeDef, _OptionalTagStreamInputRequestTypeDef
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeyList": List[str],
    },
)

_RequiredUntagStreamInputRequestTypeDef = TypedDict(
    "_RequiredUntagStreamInputRequestTypeDef",
    {
        "TagKeyList": List[str],
    },
)
_OptionalUntagStreamInputRequestTypeDef = TypedDict(
    "_OptionalUntagStreamInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

class UntagStreamInputRequestTypeDef(
    _RequiredUntagStreamInputRequestTypeDef, _OptionalUntagStreamInputRequestTypeDef
):
    pass

_RequiredUpdateDataRetentionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDataRetentionInputRequestTypeDef",
    {
        "CurrentVersion": str,
        "Operation": UpdateDataRetentionOperationType,
        "DataRetentionChangeInHours": int,
    },
)
_OptionalUpdateDataRetentionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDataRetentionInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class UpdateDataRetentionInputRequestTypeDef(
    _RequiredUpdateDataRetentionInputRequestTypeDef, _OptionalUpdateDataRetentionInputRequestTypeDef
):
    pass

UpdateImageGenerationConfigurationInputRequestTypeDef = TypedDict(
    "UpdateImageGenerationConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "ImageGenerationConfiguration": "ImageGenerationConfigurationTypeDef",
    },
    total=False,
)

UpdateMediaStorageConfigurationInputRequestTypeDef = TypedDict(
    "UpdateMediaStorageConfigurationInputRequestTypeDef",
    {
        "ChannelARN": str,
        "MediaStorageConfiguration": "MediaStorageConfigurationTypeDef",
    },
)

UpdateNotificationConfigurationInputRequestTypeDef = TypedDict(
    "UpdateNotificationConfigurationInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
    },
    total=False,
)

_RequiredUpdateSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSignalingChannelInputRequestTypeDef",
    {
        "SingleMasterConfiguration": "SingleMasterConfigurationTypeDef",
    },
    total=False,
)

class UpdateSignalingChannelInputRequestTypeDef(
    _RequiredUpdateSignalingChannelInputRequestTypeDef,
    _OptionalUpdateSignalingChannelInputRequestTypeDef,
):
    pass

_RequiredUpdateStreamInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
)
_OptionalUpdateStreamInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "DeviceName": str,
        "MediaType": str,
    },
    total=False,
)

class UpdateStreamInputRequestTypeDef(
    _RequiredUpdateStreamInputRequestTypeDef, _OptionalUpdateStreamInputRequestTypeDef
):
    pass

UploaderConfigTypeDef = TypedDict(
    "UploaderConfigTypeDef",
    {
        "ScheduleConfig": "ScheduleConfigTypeDef",
    },
)
