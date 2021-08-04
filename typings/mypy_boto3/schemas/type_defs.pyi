"""
Type annotations for schemas service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_schemas/type_defs.html)

Usage::

    ```python
    from mypy_boto3_schemas.type_defs import CreateDiscovererRequestRequestTypeDef

    data: CreateDiscovererRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import CodeGenerationStatusType, DiscovererStateType, TypeType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateDiscovererRequestRequestTypeDef",
    "CreateDiscovererResponseTypeDef",
    "CreateRegistryRequestRequestTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "DeleteDiscovererRequestRequestTypeDef",
    "DeleteRegistryRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSchemaVersionRequestRequestTypeDef",
    "DescribeCodeBindingRequestRequestTypeDef",
    "DescribeCodeBindingResponseTypeDef",
    "DescribeDiscovererRequestRequestTypeDef",
    "DescribeDiscovererResponseTypeDef",
    "DescribeRegistryRequestRequestTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeSchemaRequestRequestTypeDef",
    "DescribeSchemaResponseTypeDef",
    "DiscovererSummaryTypeDef",
    "ExportSchemaRequestRequestTypeDef",
    "ExportSchemaResponseTypeDef",
    "GetCodeBindingSourceRequestRequestTypeDef",
    "GetCodeBindingSourceResponseTypeDef",
    "GetDiscoveredSchemaRequestRequestTypeDef",
    "GetDiscoveredSchemaResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListDiscoverersRequestRequestTypeDef",
    "ListDiscoverersResponseTypeDef",
    "ListRegistriesRequestRequestTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsRequestRequestTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutCodeBindingRequestRequestTypeDef",
    "PutCodeBindingResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RegistrySummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaVersionSummaryTypeDef",
    "SearchSchemaSummaryTypeDef",
    "SearchSchemaVersionSummaryTypeDef",
    "SearchSchemasRequestRequestTypeDef",
    "SearchSchemasResponseTypeDef",
    "StartDiscovererRequestRequestTypeDef",
    "StartDiscovererResponseTypeDef",
    "StopDiscovererRequestRequestTypeDef",
    "StopDiscovererResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDiscovererRequestRequestTypeDef",
    "UpdateDiscovererResponseTypeDef",
    "UpdateRegistryRequestRequestTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaRequestRequestTypeDef",
    "UpdateSchemaResponseTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredCreateDiscovererRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDiscovererRequestRequestTypeDef",
    {
        "SourceArn": str,
    },
)
_OptionalCreateDiscovererRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDiscovererRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateDiscovererRequestRequestTypeDef(
    _RequiredCreateDiscovererRequestRequestTypeDef, _OptionalCreateDiscovererRequestRequestTypeDef
):
    pass

CreateDiscovererResponseTypeDef = TypedDict(
    "CreateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRegistryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)
_OptionalCreateRegistryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRegistryRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateRegistryRequestRequestTypeDef(
    _RequiredCreateRegistryRequestRequestTypeDef, _OptionalCreateRegistryRequestRequestTypeDef
):
    pass

CreateRegistryResponseTypeDef = TypedDict(
    "CreateRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSchemaRequestRequestTypeDef",
    {
        "Content": str,
        "RegistryName": str,
        "SchemaName": str,
        "Type": TypeType,
    },
)
_OptionalCreateSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSchemaRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateSchemaRequestRequestTypeDef(
    _RequiredCreateSchemaRequestRequestTypeDef, _OptionalCreateSchemaRequestRequestTypeDef
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDiscovererRequestRequestTypeDef = TypedDict(
    "DeleteDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

DeleteRegistryRequestRequestTypeDef = TypedDict(
    "DeleteRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
    total=False,
)

DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)

DeleteSchemaVersionRequestRequestTypeDef = TypedDict(
    "DeleteSchemaVersionRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": str,
    },
)

_RequiredDescribeCodeBindingRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeCodeBindingRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalDescribeCodeBindingRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeCodeBindingRequestRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)

class DescribeCodeBindingRequestRequestTypeDef(
    _RequiredDescribeCodeBindingRequestRequestTypeDef,
    _OptionalDescribeCodeBindingRequestRequestTypeDef,
):
    pass

DescribeCodeBindingResponseTypeDef = TypedDict(
    "DescribeCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": CodeGenerationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDiscovererRequestRequestTypeDef = TypedDict(
    "DescribeDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

DescribeDiscovererResponseTypeDef = TypedDict(
    "DescribeDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistryRequestRequestTypeDef = TypedDict(
    "DescribeRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)

DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalDescribeSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSchemaRequestRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)

class DescribeSchemaRequestRequestTypeDef(
    _RequiredDescribeSchemaRequestRequestTypeDef, _OptionalDescribeSchemaRequestRequestTypeDef
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiscovererSummaryTypeDef = TypedDict(
    "DiscovererSummaryTypeDef",
    {
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredExportSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredExportSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "Type": str,
    },
)
_OptionalExportSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalExportSchemaRequestRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)

class ExportSchemaRequestRequestTypeDef(
    _RequiredExportSchemaRequestRequestTypeDef, _OptionalExportSchemaRequestRequestTypeDef
):
    pass

ExportSchemaResponseTypeDef = TypedDict(
    "ExportSchemaResponseTypeDef",
    {
        "Content": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Type": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCodeBindingSourceRequestRequestTypeDef = TypedDict(
    "_RequiredGetCodeBindingSourceRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalGetCodeBindingSourceRequestRequestTypeDef = TypedDict(
    "_OptionalGetCodeBindingSourceRequestRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)

class GetCodeBindingSourceRequestRequestTypeDef(
    _RequiredGetCodeBindingSourceRequestRequestTypeDef,
    _OptionalGetCodeBindingSourceRequestRequestTypeDef,
):
    pass

GetCodeBindingSourceResponseTypeDef = TypedDict(
    "GetCodeBindingSourceResponseTypeDef",
    {
        "Body": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiscoveredSchemaRequestRequestTypeDef = TypedDict(
    "GetDiscoveredSchemaRequestRequestTypeDef",
    {
        "Events": List[str],
        "Type": TypeType,
    },
)

GetDiscoveredSchemaResponseTypeDef = TypedDict(
    "GetDiscoveredSchemaResponseTypeDef",
    {
        "Content": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
    total=False,
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDiscoverersRequestRequestTypeDef = TypedDict(
    "ListDiscoverersRequestRequestTypeDef",
    {
        "DiscovererIdPrefix": str,
        "Limit": int,
        "NextToken": str,
        "SourceArnPrefix": str,
    },
    total=False,
)

ListDiscoverersResponseTypeDef = TypedDict(
    "ListDiscoverersResponseTypeDef",
    {
        "Discoverers": List["DiscovererSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegistriesRequestRequestTypeDef = TypedDict(
    "ListRegistriesRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
        "RegistryNamePrefix": str,
        "Scope": str,
    },
    total=False,
)

ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {
        "NextToken": str,
        "Registries": List["RegistrySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemaVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListSchemaVersionsRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalListSchemaVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListSchemaVersionsRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class ListSchemaVersionsRequestRequestTypeDef(
    _RequiredListSchemaVersionsRequestRequestTypeDef,
    _OptionalListSchemaVersionsRequestRequestTypeDef,
):
    pass

ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {
        "NextToken": str,
        "SchemaVersions": List["SchemaVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSchemasRequestRequestTypeDef = TypedDict(
    "_RequiredListSchemasRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)
_OptionalListSchemasRequestRequestTypeDef = TypedDict(
    "_OptionalListSchemasRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
        "SchemaNamePrefix": str,
    },
    total=False,
)

class ListSchemasRequestRequestTypeDef(
    _RequiredListSchemasRequestRequestTypeDef, _OptionalListSchemasRequestRequestTypeDef
):
    pass

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List["SchemaSummaryTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPutCodeBindingRequestRequestTypeDef = TypedDict(
    "_RequiredPutCodeBindingRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalPutCodeBindingRequestRequestTypeDef = TypedDict(
    "_OptionalPutCodeBindingRequestRequestTypeDef",
    {
        "SchemaVersion": str,
    },
    total=False,
)

class PutCodeBindingRequestRequestTypeDef(
    _RequiredPutCodeBindingRequestRequestTypeDef, _OptionalPutCodeBindingRequestRequestTypeDef
):
    pass

PutCodeBindingResponseTypeDef = TypedDict(
    "PutCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": CodeGenerationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutResourcePolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutResourcePolicyRequestRequestTypeDef",
    {
        "Policy": str,
    },
)
_OptionalPutResourcePolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutResourcePolicyRequestRequestTypeDef",
    {
        "RegistryName": str,
        "RevisionId": str,
    },
    total=False,
)

class PutResourcePolicyRequestRequestTypeDef(
    _RequiredPutResourcePolicyRequestRequestTypeDef, _OptionalPutResourcePolicyRequestRequestTypeDef
):
    pass

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistrySummaryTypeDef = TypedDict(
    "RegistrySummaryTypeDef",
    {
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
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

SchemaSummaryTypeDef = TypedDict(
    "SchemaSummaryTypeDef",
    {
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "Tags": Dict[str, str],
        "VersionCount": int,
    },
    total=False,
)

SchemaVersionSummaryTypeDef = TypedDict(
    "SchemaVersionSummaryTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Type": TypeType,
    },
    total=False,
)

SearchSchemaSummaryTypeDef = TypedDict(
    "SearchSchemaSummaryTypeDef",
    {
        "RegistryName": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersions": List["SearchSchemaVersionSummaryTypeDef"],
    },
    total=False,
)

SearchSchemaVersionSummaryTypeDef = TypedDict(
    "SearchSchemaVersionSummaryTypeDef",
    {
        "CreatedDate": datetime,
        "SchemaVersion": str,
        "Type": TypeType,
    },
    total=False,
)

_RequiredSearchSchemasRequestRequestTypeDef = TypedDict(
    "_RequiredSearchSchemasRequestRequestTypeDef",
    {
        "Keywords": str,
        "RegistryName": str,
    },
)
_OptionalSearchSchemasRequestRequestTypeDef = TypedDict(
    "_OptionalSearchSchemasRequestRequestTypeDef",
    {
        "Limit": int,
        "NextToken": str,
    },
    total=False,
)

class SearchSchemasRequestRequestTypeDef(
    _RequiredSearchSchemasRequestRequestTypeDef, _OptionalSearchSchemasRequestRequestTypeDef
):
    pass

SearchSchemasResponseTypeDef = TypedDict(
    "SearchSchemasResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List["SearchSchemaSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDiscovererRequestRequestTypeDef = TypedDict(
    "StartDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

StartDiscovererResponseTypeDef = TypedDict(
    "StartDiscovererResponseTypeDef",
    {
        "DiscovererId": str,
        "State": DiscovererStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDiscovererRequestRequestTypeDef = TypedDict(
    "StopDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

StopDiscovererResponseTypeDef = TypedDict(
    "StopDiscovererResponseTypeDef",
    {
        "DiscovererId": str,
        "State": DiscovererStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredUpdateDiscovererRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)
_OptionalUpdateDiscovererRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDiscovererRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateDiscovererRequestRequestTypeDef(
    _RequiredUpdateDiscovererRequestRequestTypeDef, _OptionalUpdateDiscovererRequestRequestTypeDef
):
    pass

UpdateDiscovererResponseTypeDef = TypedDict(
    "UpdateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRegistryRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)
_OptionalUpdateRegistryRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRegistryRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateRegistryRequestRequestTypeDef(
    _RequiredUpdateRegistryRequestRequestTypeDef, _OptionalUpdateRegistryRequestRequestTypeDef
):
    pass

UpdateRegistryResponseTypeDef = TypedDict(
    "UpdateRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSchemaRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)
_OptionalUpdateSchemaRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSchemaRequestRequestTypeDef",
    {
        "ClientTokenId": str,
        "Content": str,
        "Description": str,
        "Type": TypeType,
    },
    total=False,
)

class UpdateSchemaRequestRequestTypeDef(
    _RequiredUpdateSchemaRequestRequestTypeDef, _OptionalUpdateSchemaRequestRequestTypeDef
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
