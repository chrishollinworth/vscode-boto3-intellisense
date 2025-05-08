"""
Type annotations for oam service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_oam/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_oam.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import ResourceTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateLinkInputTypeDef",
    "CreateLinkOutputTypeDef",
    "CreateSinkInputTypeDef",
    "CreateSinkOutputTypeDef",
    "DeleteLinkInputTypeDef",
    "DeleteSinkInputTypeDef",
    "GetLinkInputTypeDef",
    "GetLinkOutputTypeDef",
    "GetSinkInputTypeDef",
    "GetSinkOutputTypeDef",
    "GetSinkPolicyInputTypeDef",
    "GetSinkPolicyOutputTypeDef",
    "LinkConfigurationTypeDef",
    "ListAttachedLinksInputPaginateTypeDef",
    "ListAttachedLinksInputTypeDef",
    "ListAttachedLinksItemTypeDef",
    "ListAttachedLinksOutputTypeDef",
    "ListLinksInputPaginateTypeDef",
    "ListLinksInputTypeDef",
    "ListLinksItemTypeDef",
    "ListLinksOutputTypeDef",
    "ListSinksInputPaginateTypeDef",
    "ListSinksInputTypeDef",
    "ListSinksItemTypeDef",
    "ListSinksOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LogGroupConfigurationTypeDef",
    "MetricConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PutSinkPolicyInputTypeDef",
    "PutSinkPolicyOutputTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateLinkInputTypeDef",
    "UpdateLinkOutputTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateSinkInputTypeDef(TypedDict):
    Name: str
    Tags: NotRequired[Mapping[str, str]]

class DeleteLinkInputTypeDef(TypedDict):
    Identifier: str

class DeleteSinkInputTypeDef(TypedDict):
    Identifier: str

class GetLinkInputTypeDef(TypedDict):
    Identifier: str

class GetSinkInputTypeDef(TypedDict):
    Identifier: str

class GetSinkPolicyInputTypeDef(TypedDict):
    SinkIdentifier: str

class LogGroupConfigurationTypeDef(TypedDict):
    Filter: str

class MetricConfigurationTypeDef(TypedDict):
    Filter: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAttachedLinksInputTypeDef(TypedDict):
    SinkIdentifier: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListAttachedLinksItemTypeDef(TypedDict):
    Label: NotRequired[str]
    LinkArn: NotRequired[str]
    ResourceTypes: NotRequired[List[str]]

class ListLinksInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListLinksItemTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Label: NotRequired[str]
    ResourceTypes: NotRequired[List[str]]
    SinkArn: NotRequired[str]

class ListSinksInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListSinksItemTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceArn: str

class PutSinkPolicyInputTypeDef(TypedDict):
    Policy: str
    SinkIdentifier: str

class TagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class CreateSinkOutputTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSinkOutputTypeDef(TypedDict):
    Arn: str
    Id: str
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetSinkPolicyOutputTypeDef(TypedDict):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutSinkPolicyOutputTypeDef(TypedDict):
    Policy: str
    SinkArn: str
    SinkId: str
    ResponseMetadata: ResponseMetadataTypeDef

class LinkConfigurationTypeDef(TypedDict):
    LogGroupConfiguration: NotRequired[LogGroupConfigurationTypeDef]
    MetricConfiguration: NotRequired[MetricConfigurationTypeDef]

class ListAttachedLinksInputPaginateTypeDef(TypedDict):
    SinkIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLinksInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSinksInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAttachedLinksOutputTypeDef(TypedDict):
    Items: List[ListAttachedLinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListLinksOutputTypeDef(TypedDict):
    Items: List[ListLinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSinksOutputTypeDef(TypedDict):
    Items: List[ListSinksItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateLinkInputTypeDef(TypedDict):
    LabelTemplate: str
    ResourceTypes: Sequence[ResourceTypeType]
    SinkIdentifier: str
    LinkConfiguration: NotRequired[LinkConfigurationTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class CreateLinkOutputTypeDef(TypedDict):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinkOutputTypeDef(TypedDict):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLinkInputTypeDef(TypedDict):
    Identifier: str
    ResourceTypes: Sequence[ResourceTypeType]
    LinkConfiguration: NotRequired[LinkConfigurationTypeDef]

class UpdateLinkOutputTypeDef(TypedDict):
    Arn: str
    Id: str
    Label: str
    LabelTemplate: str
    LinkConfiguration: LinkConfigurationTypeDef
    ResourceTypes: List[str]
    SinkArn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef
