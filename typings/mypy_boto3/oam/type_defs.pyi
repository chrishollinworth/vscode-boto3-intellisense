"""
Type annotations for oam service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_oam/type_defs.html)

Usage::

    ```python
    from mypy_boto3_oam.type_defs import CreateLinkInputRequestTypeDef

    data: CreateLinkInputRequestTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

from .literals import ResourceTypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateLinkInputRequestTypeDef",
    "CreateLinkOutputTypeDef",
    "CreateSinkInputRequestTypeDef",
    "CreateSinkOutputTypeDef",
    "DeleteLinkInputRequestTypeDef",
    "DeleteSinkInputRequestTypeDef",
    "GetLinkInputRequestTypeDef",
    "GetLinkOutputTypeDef",
    "GetSinkInputRequestTypeDef",
    "GetSinkOutputTypeDef",
    "GetSinkPolicyInputRequestTypeDef",
    "GetSinkPolicyOutputTypeDef",
    "LinkConfigurationTypeDef",
    "ListAttachedLinksInputRequestTypeDef",
    "ListAttachedLinksItemTypeDef",
    "ListAttachedLinksOutputTypeDef",
    "ListLinksInputRequestTypeDef",
    "ListLinksItemTypeDef",
    "ListLinksOutputTypeDef",
    "ListSinksInputRequestTypeDef",
    "ListSinksItemTypeDef",
    "ListSinksOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LogGroupConfigurationTypeDef",
    "MetricConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PutSinkPolicyInputRequestTypeDef",
    "PutSinkPolicyOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateLinkInputRequestTypeDef",
    "UpdateLinkOutputTypeDef",
)

_RequiredCreateLinkInputRequestTypeDef = TypedDict(
    "_RequiredCreateLinkInputRequestTypeDef",
    {
        "LabelTemplate": str,
        "ResourceTypes": List[ResourceTypeType],
        "SinkIdentifier": str,
    },
)
_OptionalCreateLinkInputRequestTypeDef = TypedDict(
    "_OptionalCreateLinkInputRequestTypeDef",
    {
        "LinkConfiguration": "LinkConfigurationTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateLinkInputRequestTypeDef(
    _RequiredCreateLinkInputRequestTypeDef, _OptionalCreateLinkInputRequestTypeDef
):
    pass

CreateLinkOutputTypeDef = TypedDict(
    "CreateLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "LinkConfiguration": "LinkConfigurationTypeDef",
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSinkInputRequestTypeDef = TypedDict(
    "_RequiredCreateSinkInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateSinkInputRequestTypeDef = TypedDict(
    "_OptionalCreateSinkInputRequestTypeDef",
    {
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateSinkInputRequestTypeDef(
    _RequiredCreateSinkInputRequestTypeDef, _OptionalCreateSinkInputRequestTypeDef
):
    pass

CreateSinkOutputTypeDef = TypedDict(
    "CreateSinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLinkInputRequestTypeDef = TypedDict(
    "DeleteLinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteSinkInputRequestTypeDef = TypedDict(
    "DeleteSinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetLinkInputRequestTypeDef = TypedDict(
    "GetLinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetLinkOutputTypeDef = TypedDict(
    "GetLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "LinkConfiguration": "LinkConfigurationTypeDef",
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSinkInputRequestTypeDef = TypedDict(
    "GetSinkInputRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetSinkOutputTypeDef = TypedDict(
    "GetSinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSinkPolicyInputRequestTypeDef = TypedDict(
    "GetSinkPolicyInputRequestTypeDef",
    {
        "SinkIdentifier": str,
    },
)

GetSinkPolicyOutputTypeDef = TypedDict(
    "GetSinkPolicyOutputTypeDef",
    {
        "Policy": str,
        "SinkArn": str,
        "SinkId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LinkConfigurationTypeDef = TypedDict(
    "LinkConfigurationTypeDef",
    {
        "LogGroupConfiguration": "LogGroupConfigurationTypeDef",
        "MetricConfiguration": "MetricConfigurationTypeDef",
    },
    total=False,
)

_RequiredListAttachedLinksInputRequestTypeDef = TypedDict(
    "_RequiredListAttachedLinksInputRequestTypeDef",
    {
        "SinkIdentifier": str,
    },
)
_OptionalListAttachedLinksInputRequestTypeDef = TypedDict(
    "_OptionalListAttachedLinksInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAttachedLinksInputRequestTypeDef(
    _RequiredListAttachedLinksInputRequestTypeDef, _OptionalListAttachedLinksInputRequestTypeDef
):
    pass

ListAttachedLinksItemTypeDef = TypedDict(
    "ListAttachedLinksItemTypeDef",
    {
        "Label": str,
        "LinkArn": str,
        "ResourceTypes": List[str],
    },
    total=False,
)

ListAttachedLinksOutputTypeDef = TypedDict(
    "ListAttachedLinksOutputTypeDef",
    {
        "Items": List["ListAttachedLinksItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLinksInputRequestTypeDef = TypedDict(
    "ListLinksInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListLinksItemTypeDef = TypedDict(
    "ListLinksItemTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "ResourceTypes": List[str],
        "SinkArn": str,
    },
    total=False,
)

ListLinksOutputTypeDef = TypedDict(
    "ListLinksOutputTypeDef",
    {
        "Items": List["ListLinksItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSinksInputRequestTypeDef = TypedDict(
    "ListSinksInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListSinksItemTypeDef = TypedDict(
    "ListSinksItemTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
    },
    total=False,
)

ListSinksOutputTypeDef = TypedDict(
    "ListSinksOutputTypeDef",
    {
        "Items": List["ListSinksItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogGroupConfigurationTypeDef = TypedDict(
    "LogGroupConfigurationTypeDef",
    {
        "Filter": str,
    },
)

MetricConfigurationTypeDef = TypedDict(
    "MetricConfigurationTypeDef",
    {
        "Filter": str,
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

PutSinkPolicyInputRequestTypeDef = TypedDict(
    "PutSinkPolicyInputRequestTypeDef",
    {
        "Policy": str,
        "SinkIdentifier": str,
    },
)

PutSinkPolicyOutputTypeDef = TypedDict(
    "PutSinkPolicyOutputTypeDef",
    {
        "Policy": str,
        "SinkArn": str,
        "SinkId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateLinkInputRequestTypeDef = TypedDict(
    "_RequiredUpdateLinkInputRequestTypeDef",
    {
        "Identifier": str,
        "ResourceTypes": List[ResourceTypeType],
    },
)
_OptionalUpdateLinkInputRequestTypeDef = TypedDict(
    "_OptionalUpdateLinkInputRequestTypeDef",
    {
        "LinkConfiguration": "LinkConfigurationTypeDef",
    },
    total=False,
)

class UpdateLinkInputRequestTypeDef(
    _RequiredUpdateLinkInputRequestTypeDef, _OptionalUpdateLinkInputRequestTypeDef
):
    pass

UpdateLinkOutputTypeDef = TypedDict(
    "UpdateLinkOutputTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Label": str,
        "LabelTemplate": str,
        "LinkConfiguration": "LinkConfigurationTypeDef",
        "ResourceTypes": List[str],
        "SinkArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
