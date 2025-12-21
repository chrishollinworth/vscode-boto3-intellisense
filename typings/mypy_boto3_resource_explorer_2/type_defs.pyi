"""
Type annotations for resource-explorer-2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resource_explorer_2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_resource_explorer_2.type_defs import AssociateDefaultViewInputTypeDef

    data: AssociateDefaultViewInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from .literals import AWSServiceAccessStatusType, IndexStateType, IndexTypeType, OperationStatusType

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
    "AssociateDefaultViewInputTypeDef",
    "AssociateDefaultViewOutputTypeDef",
    "BatchGetViewErrorTypeDef",
    "BatchGetViewInputTypeDef",
    "BatchGetViewOutputTypeDef",
    "CreateIndexInputTypeDef",
    "CreateIndexOutputTypeDef",
    "CreateResourceExplorerSetupInputTypeDef",
    "CreateResourceExplorerSetupOutputTypeDef",
    "CreateViewInputTypeDef",
    "CreateViewOutputTypeDef",
    "DeleteIndexInputTypeDef",
    "DeleteIndexOutputTypeDef",
    "DeleteResourceExplorerSetupInputTypeDef",
    "DeleteResourceExplorerSetupOutputTypeDef",
    "DeleteViewInputTypeDef",
    "DeleteViewOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ErrorDetailsTypeDef",
    "GetAccountLevelServiceConfigurationOutputTypeDef",
    "GetDefaultViewOutputTypeDef",
    "GetIndexOutputTypeDef",
    "GetManagedViewInputTypeDef",
    "GetManagedViewOutputTypeDef",
    "GetResourceExplorerSetupInputPaginateTypeDef",
    "GetResourceExplorerSetupInputTypeDef",
    "GetResourceExplorerSetupOutputTypeDef",
    "GetServiceIndexOutputTypeDef",
    "GetServiceViewInputTypeDef",
    "GetServiceViewOutputTypeDef",
    "GetViewInputTypeDef",
    "GetViewOutputTypeDef",
    "IncludedPropertyTypeDef",
    "IndexStatusTypeDef",
    "IndexTypeDef",
    "ListIndexesForMembersInputPaginateTypeDef",
    "ListIndexesForMembersInputTypeDef",
    "ListIndexesForMembersOutputTypeDef",
    "ListIndexesInputPaginateTypeDef",
    "ListIndexesInputTypeDef",
    "ListIndexesOutputTypeDef",
    "ListManagedViewsInputPaginateTypeDef",
    "ListManagedViewsInputTypeDef",
    "ListManagedViewsOutputTypeDef",
    "ListResourcesInputPaginateTypeDef",
    "ListResourcesInputTypeDef",
    "ListResourcesOutputTypeDef",
    "ListServiceIndexesInputPaginateTypeDef",
    "ListServiceIndexesInputTypeDef",
    "ListServiceIndexesOutputTypeDef",
    "ListServiceViewsInputPaginateTypeDef",
    "ListServiceViewsInputTypeDef",
    "ListServiceViewsOutputTypeDef",
    "ListStreamingAccessForServicesInputPaginateTypeDef",
    "ListStreamingAccessForServicesInputTypeDef",
    "ListStreamingAccessForServicesOutputTypeDef",
    "ListSupportedResourceTypesInputPaginateTypeDef",
    "ListSupportedResourceTypesInputTypeDef",
    "ListSupportedResourceTypesOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListViewsInputPaginateTypeDef",
    "ListViewsInputTypeDef",
    "ListViewsOutputTypeDef",
    "ManagedViewTypeDef",
    "MemberIndexTypeDef",
    "OrgConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "RegionStatusTypeDef",
    "ResourceCountTypeDef",
    "ResourcePropertyTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "SearchFilterTypeDef",
    "SearchInputPaginateTypeDef",
    "SearchInputTypeDef",
    "SearchOutputTypeDef",
    "ServiceViewTypeDef",
    "StreamingAccessDetailsTypeDef",
    "SupportedResourceTypeTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateIndexTypeInputTypeDef",
    "UpdateIndexTypeOutputTypeDef",
    "UpdateViewInputTypeDef",
    "UpdateViewOutputTypeDef",
    "ViewStatusTypeDef",
    "ViewTypeDef",
)

class AssociateDefaultViewInputTypeDef(TypedDict):
    ViewArn: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchGetViewErrorTypeDef(TypedDict):
    ViewArn: str
    ErrorMessage: str

class BatchGetViewInputTypeDef(TypedDict):
    ViewArns: NotRequired[Sequence[str]]

class CreateIndexInputTypeDef(TypedDict):
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateResourceExplorerSetupInputTypeDef(TypedDict):
    RegionList: Sequence[str]
    ViewName: str
    AggregatorRegions: NotRequired[Sequence[str]]

class IncludedPropertyTypeDef(TypedDict):
    Name: str

class SearchFilterTypeDef(TypedDict):
    FilterString: str

class DeleteIndexInputTypeDef(TypedDict):
    Arn: str

class DeleteResourceExplorerSetupInputTypeDef(TypedDict):
    RegionList: NotRequired[Sequence[str]]
    DeleteInAllRegions: NotRequired[bool]

class DeleteViewInputTypeDef(TypedDict):
    ViewArn: str

class ErrorDetailsTypeDef(TypedDict):
    Code: NotRequired[str]
    Message: NotRequired[str]

class OrgConfigurationTypeDef(TypedDict):
    AWSServiceAccessStatus: AWSServiceAccessStatusType
    ServiceLinkedRole: NotRequired[str]

class GetManagedViewInputTypeDef(TypedDict):
    ManagedViewArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetResourceExplorerSetupInputTypeDef(TypedDict):
    TaskId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GetServiceViewInputTypeDef(TypedDict):
    ServiceViewArn: str

class GetViewInputTypeDef(TypedDict):
    ViewArn: str

IndexTypeDef = TypedDict(
    "IndexTypeDef",
    {
        "Region": NotRequired[str],
        "Arn": NotRequired[str],
        "Type": NotRequired[IndexTypeType],
    },
)

class ListIndexesForMembersInputTypeDef(TypedDict):
    AccountIdList: Sequence[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

MemberIndexTypeDef = TypedDict(
    "MemberIndexTypeDef",
    {
        "AccountId": NotRequired[str],
        "Region": NotRequired[str],
        "Arn": NotRequired[str],
        "Type": NotRequired[IndexTypeType],
    },
)
ListIndexesInputTypeDef = TypedDict(
    "ListIndexesInputTypeDef",
    {
        "Type": NotRequired[IndexTypeType],
        "Regions": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

class ListManagedViewsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ServicePrincipal: NotRequired[str]

class ListServiceIndexesInputTypeDef(TypedDict):
    Regions: NotRequired[Sequence[str]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListServiceViewsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListStreamingAccessForServicesInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class StreamingAccessDetailsTypeDef(TypedDict):
    ServicePrincipal: str
    CreatedAt: datetime

class ListSupportedResourceTypesInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SupportedResourceTypeTypeDef(TypedDict):
    Service: NotRequired[str]
    ResourceType: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class ListViewsInputTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ResourceCountTypeDef(TypedDict):
    TotalResources: NotRequired[int]
    Complete: NotRequired[bool]

class ResourcePropertyTypeDef(TypedDict):
    Name: NotRequired[str]
    LastReportedAt: NotRequired[datetime]
    Data: NotRequired[Dict[str, Any]]

class SearchInputTypeDef(TypedDict):
    QueryString: str
    MaxResults: NotRequired[int]
    ViewArn: NotRequired[str]
    NextToken: NotRequired[str]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    Tags: NotRequired[Mapping[str, str]]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

UpdateIndexTypeInputTypeDef = TypedDict(
    "UpdateIndexTypeInputTypeDef",
    {
        "Arn": str,
        "Type": IndexTypeType,
    },
)

class AssociateDefaultViewOutputTypeDef(TypedDict):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIndexOutputTypeDef(TypedDict):
    Arn: str
    State: IndexStateType
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceExplorerSetupOutputTypeDef(TypedDict):
    TaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIndexOutputTypeDef(TypedDict):
    Arn: str
    State: IndexStateType
    LastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourceExplorerSetupOutputTypeDef(TypedDict):
    TaskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteViewOutputTypeDef(TypedDict):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDefaultViewOutputTypeDef(TypedDict):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

GetIndexOutputTypeDef = TypedDict(
    "GetIndexOutputTypeDef",
    {
        "Arn": str,
        "Type": IndexTypeType,
        "State": IndexStateType,
        "ReplicatingFrom": List[str],
        "ReplicatingTo": List[str],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceIndexOutputTypeDef = TypedDict(
    "GetServiceIndexOutputTypeDef",
    {
        "Arn": str,
        "Type": IndexTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListManagedViewsOutputTypeDef(TypedDict):
    ManagedViews: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListServiceViewsOutputTypeDef(TypedDict):
    ServiceViews: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListViewsOutputTypeDef(TypedDict):
    Views: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

UpdateIndexTypeOutputTypeDef = TypedDict(
    "UpdateIndexTypeOutputTypeDef",
    {
        "Arn": str,
        "Type": IndexTypeType,
        "State": IndexStateType,
        "LastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateViewInputTypeDef(TypedDict):
    ViewName: str
    ClientToken: NotRequired[str]
    IncludedProperties: NotRequired[Sequence[IncludedPropertyTypeDef]]
    Scope: NotRequired[str]
    Filters: NotRequired[SearchFilterTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class ListResourcesInputTypeDef(TypedDict):
    Filters: NotRequired[SearchFilterTypeDef]
    MaxResults: NotRequired[int]
    ViewArn: NotRequired[str]
    NextToken: NotRequired[str]

class ManagedViewTypeDef(TypedDict):
    ManagedViewArn: NotRequired[str]
    ManagedViewName: NotRequired[str]
    TrustedService: NotRequired[str]
    LastUpdatedAt: NotRequired[datetime]
    Owner: NotRequired[str]
    Scope: NotRequired[str]
    IncludedProperties: NotRequired[List[IncludedPropertyTypeDef]]
    Filters: NotRequired[SearchFilterTypeDef]
    ResourcePolicy: NotRequired[str]
    Version: NotRequired[str]

class ServiceViewTypeDef(TypedDict):
    ServiceViewArn: str
    Filters: NotRequired[SearchFilterTypeDef]
    IncludedProperties: NotRequired[List[IncludedPropertyTypeDef]]
    StreamingAccessForService: NotRequired[str]
    ScopeType: NotRequired[str]

class UpdateViewInputTypeDef(TypedDict):
    ViewArn: str
    IncludedProperties: NotRequired[Sequence[IncludedPropertyTypeDef]]
    Filters: NotRequired[SearchFilterTypeDef]

class ViewTypeDef(TypedDict):
    ViewArn: NotRequired[str]
    Owner: NotRequired[str]
    LastUpdatedAt: NotRequired[datetime]
    Scope: NotRequired[str]
    IncludedProperties: NotRequired[List[IncludedPropertyTypeDef]]
    Filters: NotRequired[SearchFilterTypeDef]

class GetAccountLevelServiceConfigurationOutputTypeDef(TypedDict):
    OrgConfiguration: OrgConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceExplorerSetupInputPaginateTypeDef(TypedDict):
    TaskId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIndexesForMembersInputPaginateTypeDef(TypedDict):
    AccountIdList: Sequence[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListIndexesInputPaginateTypeDef = TypedDict(
    "ListIndexesInputPaginateTypeDef",
    {
        "Type": NotRequired[IndexTypeType],
        "Regions": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListManagedViewsInputPaginateTypeDef(TypedDict):
    ServicePrincipal: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourcesInputPaginateTypeDef(TypedDict):
    Filters: NotRequired[SearchFilterTypeDef]
    ViewArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceIndexesInputPaginateTypeDef(TypedDict):
    Regions: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceViewsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStreamingAccessForServicesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSupportedResourceTypesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListViewsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchInputPaginateTypeDef(TypedDict):
    QueryString: str
    ViewArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class IndexStatusTypeDef(TypedDict):
    Status: NotRequired[OperationStatusType]
    Index: NotRequired[IndexTypeDef]
    ErrorDetails: NotRequired[ErrorDetailsTypeDef]

class ListIndexesOutputTypeDef(TypedDict):
    Indexes: List[IndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListServiceIndexesOutputTypeDef(TypedDict):
    Indexes: List[IndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListIndexesForMembersOutputTypeDef(TypedDict):
    Indexes: List[MemberIndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListStreamingAccessForServicesOutputTypeDef(TypedDict):
    StreamingAccessForServices: List[StreamingAccessDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSupportedResourceTypesOutputTypeDef(TypedDict):
    ResourceTypes: List[SupportedResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResourceTypeDef(TypedDict):
    Arn: NotRequired[str]
    OwningAccountId: NotRequired[str]
    Region: NotRequired[str]
    ResourceType: NotRequired[str]
    Service: NotRequired[str]
    LastReportedAt: NotRequired[datetime]
    Properties: NotRequired[List[ResourcePropertyTypeDef]]

class GetManagedViewOutputTypeDef(TypedDict):
    ManagedView: ManagedViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceViewOutputTypeDef(TypedDict):
    View: ServiceViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetViewOutputTypeDef(TypedDict):
    Views: List[ViewTypeDef]
    Errors: List[BatchGetViewErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateViewOutputTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetViewOutputTypeDef(TypedDict):
    View: ViewTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateViewOutputTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ViewStatusTypeDef(TypedDict):
    Status: NotRequired[OperationStatusType]
    View: NotRequired[ViewTypeDef]
    ErrorDetails: NotRequired[ErrorDetailsTypeDef]

class ListResourcesOutputTypeDef(TypedDict):
    Resources: List[ResourceTypeDef]
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchOutputTypeDef(TypedDict):
    Resources: List[ResourceTypeDef]
    ViewArn: str
    Count: ResourceCountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class RegionStatusTypeDef(TypedDict):
    Region: NotRequired[str]
    Index: NotRequired[IndexStatusTypeDef]
    View: NotRequired[ViewStatusTypeDef]

class GetResourceExplorerSetupOutputTypeDef(TypedDict):
    Regions: List[RegionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
