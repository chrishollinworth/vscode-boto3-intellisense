"""
Main interface for schemas service type definitions.

Usage::

    ```python
    from mypy_boto3_schemas.type_defs import DiscovererSummaryTypeDef

    data: DiscovererSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
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
    "DiscovererSummaryTypeDef",
    "RegistrySummaryTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaVersionSummaryTypeDef",
    "SearchSchemaSummaryTypeDef",
    "SearchSchemaVersionSummaryTypeDef",
    "CreateDiscovererResponseTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "DescribeCodeBindingResponseTypeDef",
    "DescribeDiscovererResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeSchemaResponseTypeDef",
    "GetCodeBindingSourceResponseTypeDef",
    "GetDiscoveredSchemaResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListDiscoverersResponseTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutCodeBindingResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "SearchSchemasResponseTypeDef",
    "StartDiscovererResponseTypeDef",
    "StopDiscovererResponseTypeDef",
    "UpdateDiscovererResponseTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "WaiterConfigTypeDef",
)

DiscovererSummaryTypeDef = TypedDict(
    "DiscovererSummaryTypeDef",
    {
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

RegistrySummaryTypeDef = TypedDict(
    "RegistrySummaryTypeDef",
    {"RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
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
    {"SchemaArn": str, "SchemaName": str, "SchemaVersion": str},
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
    {"CreatedDate": datetime, "SchemaVersion": str},
    total=False,
)

CreateDiscovererResponseTypeDef = TypedDict(
    "CreateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateRegistryResponseTypeDef = TypedDict(
    "CreateRegistryResponseTypeDef",
    {"Description": str, "RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
)

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
    },
    total=False,
)

DescribeCodeBindingResponseTypeDef = TypedDict(
    "DescribeCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": Literal["CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"],
    },
    total=False,
)

DescribeDiscovererResponseTypeDef = TypedDict(
    "DescribeDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {"Description": str, "RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
)

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
    },
    total=False,
)

GetCodeBindingSourceResponseTypeDef = TypedDict(
    "GetCodeBindingSourceResponseTypeDef", {"Body": bytes}, total=False
)

GetDiscoveredSchemaResponseTypeDef = TypedDict(
    "GetDiscoveredSchemaResponseTypeDef", {"Content": str}, total=False
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)

ListDiscoverersResponseTypeDef = TypedDict(
    "ListDiscoverersResponseTypeDef",
    {"Discoverers": List["DiscovererSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {"NextToken": str, "Registries": List["RegistrySummaryTypeDef"]},
    total=False,
)

ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {"NextToken": str, "SchemaVersions": List["SchemaVersionSummaryTypeDef"]},
    total=False,
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {"NextToken": str, "Schemas": List["SchemaSummaryTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutCodeBindingResponseTypeDef = TypedDict(
    "PutCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": Literal["CREATE_IN_PROGRESS", "CREATE_COMPLETE", "CREATE_FAILED"],
    },
    total=False,
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef", {"Policy": str, "RevisionId": str}, total=False
)

SearchSchemasResponseTypeDef = TypedDict(
    "SearchSchemasResponseTypeDef",
    {"NextToken": str, "Schemas": List["SearchSchemaSummaryTypeDef"]},
    total=False,
)

StartDiscovererResponseTypeDef = TypedDict(
    "StartDiscovererResponseTypeDef",
    {"DiscovererId": str, "State": Literal["STARTED", "STOPPED"]},
    total=False,
)

StopDiscovererResponseTypeDef = TypedDict(
    "StopDiscovererResponseTypeDef",
    {"DiscovererId": str, "State": Literal["STARTED", "STOPPED"]},
    total=False,
)

UpdateDiscovererResponseTypeDef = TypedDict(
    "UpdateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": Literal["STARTED", "STOPPED"],
        "Tags": Dict[str, str],
    },
    total=False,
)

UpdateRegistryResponseTypeDef = TypedDict(
    "UpdateRegistryResponseTypeDef",
    {"Description": str, "RegistryArn": str, "RegistryName": str, "Tags": Dict[str, str]},
    total=False,
)

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
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
