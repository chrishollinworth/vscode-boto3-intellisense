"""
Type annotations for schemas service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_schemas.type_defs import CreateDiscovererRequestTypeDef

    data: CreateDiscovererRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from botocore.response import StreamingBody

from .literals import CodeGenerationStatusType, DiscovererStateType, TypeType

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
    "CreateDiscovererRequestTypeDef",
    "CreateDiscovererResponseTypeDef",
    "CreateRegistryRequestTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "DeleteDiscovererRequestTypeDef",
    "DeleteRegistryRequestTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteSchemaRequestTypeDef",
    "DeleteSchemaVersionRequestTypeDef",
    "DescribeCodeBindingRequestTypeDef",
    "DescribeCodeBindingRequestWaitTypeDef",
    "DescribeCodeBindingResponseTypeDef",
    "DescribeDiscovererRequestTypeDef",
    "DescribeDiscovererResponseTypeDef",
    "DescribeRegistryRequestTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeSchemaRequestTypeDef",
    "DescribeSchemaResponseTypeDef",
    "DiscovererSummaryTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportSchemaRequestTypeDef",
    "ExportSchemaResponseTypeDef",
    "GetCodeBindingSourceRequestTypeDef",
    "GetCodeBindingSourceResponseTypeDef",
    "GetDiscoveredSchemaRequestTypeDef",
    "GetDiscoveredSchemaResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListDiscoverersRequestPaginateTypeDef",
    "ListDiscoverersRequestTypeDef",
    "ListDiscoverersResponseTypeDef",
    "ListRegistriesRequestPaginateTypeDef",
    "ListRegistriesRequestTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsRequestPaginateTypeDef",
    "ListSchemaVersionsRequestTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasRequestPaginateTypeDef",
    "ListSchemasRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutCodeBindingRequestTypeDef",
    "PutCodeBindingResponseTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RegistrySummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaVersionSummaryTypeDef",
    "SearchSchemaSummaryTypeDef",
    "SearchSchemaVersionSummaryTypeDef",
    "SearchSchemasRequestPaginateTypeDef",
    "SearchSchemasRequestTypeDef",
    "SearchSchemasResponseTypeDef",
    "StartDiscovererRequestTypeDef",
    "StartDiscovererResponseTypeDef",
    "StopDiscovererRequestTypeDef",
    "StopDiscovererResponseTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateDiscovererRequestTypeDef",
    "UpdateDiscovererResponseTypeDef",
    "UpdateRegistryRequestTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaRequestTypeDef",
    "UpdateSchemaResponseTypeDef",
    "WaiterConfigTypeDef",
)

class CreateDiscovererRequestTypeDef(TypedDict):
    SourceArn: str
    Description: NotRequired[str]
    CrossAccount: NotRequired[bool]
    Tags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateRegistryRequestTypeDef(TypedDict):
    RegistryName: str
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

CreateSchemaRequestTypeDef = TypedDict(
    "CreateSchemaRequestTypeDef",
    {
        "Content": str,
        "RegistryName": str,
        "SchemaName": str,
        "Type": TypeType,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

class DeleteDiscovererRequestTypeDef(TypedDict):
    DiscovererId: str

class DeleteRegistryRequestTypeDef(TypedDict):
    RegistryName: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    RegistryName: NotRequired[str]

class DeleteSchemaRequestTypeDef(TypedDict):
    RegistryName: str
    SchemaName: str

class DeleteSchemaVersionRequestTypeDef(TypedDict):
    RegistryName: str
    SchemaName: str
    SchemaVersion: str

class DescribeCodeBindingRequestTypeDef(TypedDict):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: NotRequired[str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeDiscovererRequestTypeDef(TypedDict):
    DiscovererId: str

class DescribeRegistryRequestTypeDef(TypedDict):
    RegistryName: str

class DescribeSchemaRequestTypeDef(TypedDict):
    RegistryName: str
    SchemaName: str
    SchemaVersion: NotRequired[str]

class DiscovererSummaryTypeDef(TypedDict):
    DiscovererArn: NotRequired[str]
    DiscovererId: NotRequired[str]
    SourceArn: NotRequired[str]
    State: NotRequired[DiscovererStateType]
    CrossAccount: NotRequired[bool]
    Tags: NotRequired[Dict[str, str]]

ExportSchemaRequestTypeDef = TypedDict(
    "ExportSchemaRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "Type": str,
        "SchemaVersion": NotRequired[str],
    },
)

class GetCodeBindingSourceRequestTypeDef(TypedDict):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: NotRequired[str]

GetDiscoveredSchemaRequestTypeDef = TypedDict(
    "GetDiscoveredSchemaRequestTypeDef",
    {
        "Events": Sequence[str],
        "Type": TypeType,
    },
)

class GetResourcePolicyRequestTypeDef(TypedDict):
    RegistryName: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListDiscoverersRequestTypeDef(TypedDict):
    DiscovererIdPrefix: NotRequired[str]
    Limit: NotRequired[int]
    NextToken: NotRequired[str]
    SourceArnPrefix: NotRequired[str]

class ListRegistriesRequestTypeDef(TypedDict):
    Limit: NotRequired[int]
    NextToken: NotRequired[str]
    RegistryNamePrefix: NotRequired[str]
    Scope: NotRequired[str]

class RegistrySummaryTypeDef(TypedDict):
    RegistryArn: NotRequired[str]
    RegistryName: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]

class ListSchemaVersionsRequestTypeDef(TypedDict):
    RegistryName: str
    SchemaName: str
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

SchemaVersionSummaryTypeDef = TypedDict(
    "SchemaVersionSummaryTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "SchemaVersion": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)

class ListSchemasRequestTypeDef(TypedDict):
    RegistryName: str
    Limit: NotRequired[int]
    NextToken: NotRequired[str]
    SchemaNamePrefix: NotRequired[str]

class SchemaSummaryTypeDef(TypedDict):
    LastModified: NotRequired[datetime]
    SchemaArn: NotRequired[str]
    SchemaName: NotRequired[str]
    Tags: NotRequired[Dict[str, str]]
    VersionCount: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class PutCodeBindingRequestTypeDef(TypedDict):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    Policy: str
    RegistryName: NotRequired[str]
    RevisionId: NotRequired[str]

SearchSchemaVersionSummaryTypeDef = TypedDict(
    "SearchSchemaVersionSummaryTypeDef",
    {
        "CreatedDate": NotRequired[datetime],
        "SchemaVersion": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)

class SearchSchemasRequestTypeDef(TypedDict):
    Keywords: str
    RegistryName: str
    Limit: NotRequired[int]
    NextToken: NotRequired[str]

class StartDiscovererRequestTypeDef(TypedDict):
    DiscovererId: str

class StopDiscovererRequestTypeDef(TypedDict):
    DiscovererId: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateDiscovererRequestTypeDef(TypedDict):
    DiscovererId: str
    Description: NotRequired[str]
    CrossAccount: NotRequired[bool]

class UpdateRegistryRequestTypeDef(TypedDict):
    RegistryName: str
    Description: NotRequired[str]

UpdateSchemaRequestTypeDef = TypedDict(
    "UpdateSchemaRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "ClientTokenId": NotRequired[str],
        "Content": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)

class CreateDiscovererResponseTypeDef(TypedDict):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistryResponseTypeDef(TypedDict):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DescribeCodeBindingResponseTypeDef(TypedDict):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDiscovererResponseTypeDef(TypedDict):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRegistryResponseTypeDef(TypedDict):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

DescribeSchemaResponseTypeDef = TypedDict(
    "DescribeSchemaResponseTypeDef",
    {
        "Content": str,
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

ExportSchemaResponseTypeDef = TypedDict(
    "ExportSchemaResponseTypeDef",
    {
        "Content": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Type": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetCodeBindingSourceResponseTypeDef(TypedDict):
    Body: StreamingBody
    ResponseMetadata: ResponseMetadataTypeDef

class GetDiscoveredSchemaResponseTypeDef(TypedDict):
    Content: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutCodeBindingResponseTypeDef(TypedDict):
    CreationDate: datetime
    LastModified: datetime
    SchemaVersion: str
    Status: CodeGenerationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(TypedDict):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDiscovererResponseTypeDef(TypedDict):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadataTypeDef

class StopDiscovererResponseTypeDef(TypedDict):
    DiscovererId: str
    State: DiscovererStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDiscovererResponseTypeDef(TypedDict):
    Description: str
    DiscovererArn: str
    DiscovererId: str
    SourceArn: str
    State: DiscovererStateType
    CrossAccount: bool
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegistryResponseTypeDef(TypedDict):
    Description: str
    RegistryArn: str
    RegistryName: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DescribeCodeBindingRequestWaitTypeDef(TypedDict):
    Language: str
    RegistryName: str
    SchemaName: str
    SchemaVersion: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class ListDiscoverersResponseTypeDef(TypedDict):
    Discoverers: List[DiscovererSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDiscoverersRequestPaginateTypeDef(TypedDict):
    DiscovererIdPrefix: NotRequired[str]
    SourceArnPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegistriesRequestPaginateTypeDef(TypedDict):
    RegistryNamePrefix: NotRequired[str]
    Scope: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchemaVersionsRequestPaginateTypeDef(TypedDict):
    RegistryName: str
    SchemaName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSchemasRequestPaginateTypeDef(TypedDict):
    RegistryName: str
    SchemaNamePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchSchemasRequestPaginateTypeDef(TypedDict):
    Keywords: str
    RegistryName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegistriesResponseTypeDef(TypedDict):
    Registries: List[RegistrySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSchemaVersionsResponseTypeDef(TypedDict):
    SchemaVersions: List[SchemaVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSchemasResponseTypeDef(TypedDict):
    Schemas: List[SchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchSchemaSummaryTypeDef(TypedDict):
    RegistryName: NotRequired[str]
    SchemaArn: NotRequired[str]
    SchemaName: NotRequired[str]
    SchemaVersions: NotRequired[List[SearchSchemaVersionSummaryTypeDef]]

class SearchSchemasResponseTypeDef(TypedDict):
    Schemas: List[SearchSchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
