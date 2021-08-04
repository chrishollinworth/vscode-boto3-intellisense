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
    StatusType,
    UpdateDataRetentionOperationType,
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
    "DeleteSignalingChannelInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "DescribeSignalingChannelInputRequestTypeDef",
    "DescribeSignalingChannelOutputTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "DescribeStreamOutputTypeDef",
    "GetDataEndpointInputRequestTypeDef",
    "GetDataEndpointOutputTypeDef",
    "GetSignalingChannelEndpointInputRequestTypeDef",
    "GetSignalingChannelEndpointOutputTypeDef",
    "ListSignalingChannelsInputRequestTypeDef",
    "ListSignalingChannelsOutputTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ResponseMetadataTypeDef",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "SingleMasterConfigurationTypeDef",
    "StreamInfoTypeDef",
    "StreamNameConditionTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagStreamInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UntagStreamInputRequestTypeDef",
    "UpdateDataRetentionInputRequestTypeDef",
    "UpdateSignalingChannelInputRequestTypeDef",
    "UpdateStreamInputRequestTypeDef",
)

ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": Literal["SINGLE_MASTER"],
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
        "ChannelType": Literal["SINGLE_MASTER"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

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
