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

from .literals import AWSServiceAccessStatusType, IndexStateType, IndexTypeType

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
    "CreateViewInputTypeDef",
    "CreateViewOutputTypeDef",
    "DeleteIndexInputTypeDef",
    "DeleteIndexOutputTypeDef",
    "DeleteViewInputTypeDef",
    "DeleteViewOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAccountLevelServiceConfigurationOutputTypeDef",
    "GetDefaultViewOutputTypeDef",
    "GetIndexOutputTypeDef",
    "GetManagedViewInputTypeDef",
    "GetManagedViewOutputTypeDef",
    "GetViewInputTypeDef",
    "GetViewOutputTypeDef",
    "IncludedPropertyTypeDef",
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
    "ResourceCountTypeDef",
    "ResourcePropertyTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "SearchFilterTypeDef",
    "SearchInputPaginateTypeDef",
    "SearchInputTypeDef",
    "SearchOutputTypeDef",
    "SupportedResourceTypeTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateIndexTypeInputTypeDef",
    "UpdateIndexTypeOutputTypeDef",
    "UpdateViewInputTypeDef",
    "UpdateViewOutputTypeDef",
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
    ErrorMessage: str
    ViewArn: str

class BatchGetViewInputTypeDef(TypedDict):
    ViewArns: NotRequired[Sequence[str]]

class CreateIndexInputTypeDef(TypedDict):
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class IncludedPropertyTypeDef(TypedDict):
    Name: str

class SearchFilterTypeDef(TypedDict):
    FilterString: str

class DeleteIndexInputTypeDef(TypedDict):
    Arn: str

class DeleteViewInputTypeDef(TypedDict):
    ViewArn: str

class OrgConfigurationTypeDef(TypedDict):
    AWSServiceAccessStatus: AWSServiceAccessStatusType
    ServiceLinkedRole: NotRequired[str]

class GetManagedViewInputTypeDef(TypedDict):
    ManagedViewArn: str

class GetViewInputTypeDef(TypedDict):
    ViewArn: str

IndexTypeDef = TypedDict(
    "IndexTypeDef",
    {
        "Arn": NotRequired[str],
        "Region": NotRequired[str],
        "Type": NotRequired[IndexTypeType],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListIndexesForMembersInputTypeDef(TypedDict):
    AccountIdList: Sequence[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

MemberIndexTypeDef = TypedDict(
    "MemberIndexTypeDef",
    {
        "AccountId": NotRequired[str],
        "Arn": NotRequired[str],
        "Region": NotRequired[str],
        "Type": NotRequired[IndexTypeType],
    },
)
ListIndexesInputTypeDef = TypedDict(
    "ListIndexesInputTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Regions": NotRequired[Sequence[str]],
        "Type": NotRequired[IndexTypeType],
    },
)

class ListManagedViewsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ServicePrincipal: NotRequired[str]

class ListSupportedResourceTypesInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class SupportedResourceTypeTypeDef(TypedDict):
    ResourceType: NotRequired[str]
    Service: NotRequired[str]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class ListViewsInputTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ResourceCountTypeDef(TypedDict):
    Complete: NotRequired[bool]
    TotalResources: NotRequired[int]

class ResourcePropertyTypeDef(TypedDict):
    Data: NotRequired[Dict[str, Any]]
    LastReportedAt: NotRequired[datetime]
    Name: NotRequired[str]

class SearchInputTypeDef(TypedDict):
    QueryString: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ViewArn: NotRequired[str]

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
    CreatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIndexOutputTypeDef(TypedDict):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
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
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "ReplicatingFrom": List[str],
        "ReplicatingTo": List[str],
        "State": IndexStateType,
        "Tags": Dict[str, str],
        "Type": IndexTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListManagedViewsOutputTypeDef(TypedDict):
    ManagedViews: List[str]
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
        "LastUpdatedAt": datetime,
        "State": IndexStateType,
        "Type": IndexTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateViewInputTypeDef(TypedDict):
    ViewName: str
    ClientToken: NotRequired[str]
    Filters: NotRequired[SearchFilterTypeDef]
    IncludedProperties: NotRequired[Sequence[IncludedPropertyTypeDef]]
    Scope: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ListResourcesInputTypeDef(TypedDict):
    Filters: NotRequired[SearchFilterTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ViewArn: NotRequired[str]

class ManagedViewTypeDef(TypedDict):
    Filters: NotRequired[SearchFilterTypeDef]
    IncludedProperties: NotRequired[List[IncludedPropertyTypeDef]]
    LastUpdatedAt: NotRequired[datetime]
    ManagedViewArn: NotRequired[str]
    ManagedViewName: NotRequired[str]
    Owner: NotRequired[str]
    ResourcePolicy: NotRequired[str]
    Scope: NotRequired[str]
    TrustedService: NotRequired[str]
    Version: NotRequired[str]

class UpdateViewInputTypeDef(TypedDict):
    ViewArn: str
    Filters: NotRequired[SearchFilterTypeDef]
    IncludedProperties: NotRequired[Sequence[IncludedPropertyTypeDef]]

class ViewTypeDef(TypedDict):
    Filters: NotRequired[SearchFilterTypeDef]
    IncludedProperties: NotRequired[List[IncludedPropertyTypeDef]]
    LastUpdatedAt: NotRequired[datetime]
    Owner: NotRequired[str]
    Scope: NotRequired[str]
    ViewArn: NotRequired[str]

class GetAccountLevelServiceConfigurationOutputTypeDef(TypedDict):
    OrgConfiguration: OrgConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexesOutputTypeDef(TypedDict):
    Indexes: List[IndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListIndexesForMembersInputPaginateTypeDef(TypedDict):
    AccountIdList: Sequence[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListIndexesInputPaginateTypeDef = TypedDict(
    "ListIndexesInputPaginateTypeDef",
    {
        "Regions": NotRequired[Sequence[str]],
        "Type": NotRequired[IndexTypeType],
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

class ListSupportedResourceTypesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListViewsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchInputPaginateTypeDef(TypedDict):
    QueryString: str
    ViewArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIndexesForMembersOutputTypeDef(TypedDict):
    Indexes: List[MemberIndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSupportedResourceTypesOutputTypeDef(TypedDict):
    ResourceTypes: List[SupportedResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResourceTypeDef(TypedDict):
    Arn: NotRequired[str]
    LastReportedAt: NotRequired[datetime]
    OwningAccountId: NotRequired[str]
    Properties: NotRequired[List[ResourcePropertyTypeDef]]
    Region: NotRequired[str]
    ResourceType: NotRequired[str]
    Service: NotRequired[str]

class GetManagedViewOutputTypeDef(TypedDict):
    ManagedView: ManagedViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetViewOutputTypeDef(TypedDict):
    Errors: List[BatchGetViewErrorTypeDef]
    Views: List[ViewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateViewOutputTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetViewOutputTypeDef(TypedDict):
    Tags: Dict[str, str]
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateViewOutputTypeDef(TypedDict):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesOutputTypeDef(TypedDict):
    Resources: List[ResourceTypeDef]
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchOutputTypeDef(TypedDict):
    Count: ResourceCountTypeDef
    Resources: List[ResourceTypeDef]
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
