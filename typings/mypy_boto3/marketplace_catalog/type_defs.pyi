"""
Type annotations for marketplace-catalog service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import AmiProductEntityIdFilterTypeDef

    data: AmiProductEntityIdFilterTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from .literals import (
    AmiProductSortByType,
    AmiProductVisibilityStringType,
    ChangeStatusType,
    ContainerProductSortByType,
    ContainerProductVisibilityStringType,
    DataProductSortByType,
    DataProductVisibilityStringType,
    FailureCodeType,
    IntentType,
    OfferSortByType,
    OfferStateStringType,
    OfferTargetingStringType,
    OwnershipTypeType,
    ResaleAuthorizationSortByType,
    ResaleAuthorizationStatusStringType,
    SaaSProductSortByType,
    SaaSProductVisibilityStringType,
    SortOrderType,
)

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
    "AmiProductEntityIdFilterTypeDef",
    "AmiProductFiltersTypeDef",
    "AmiProductLastModifiedDateFilterDateRangeTypeDef",
    "AmiProductLastModifiedDateFilterTypeDef",
    "AmiProductSortTypeDef",
    "AmiProductSummaryTypeDef",
    "AmiProductTitleFilterTypeDef",
    "AmiProductVisibilityFilterTypeDef",
    "BatchDescribeEntitiesRequestTypeDef",
    "BatchDescribeEntitiesResponseTypeDef",
    "BatchDescribeErrorDetailTypeDef",
    "CancelChangeSetRequestTypeDef",
    "CancelChangeSetResponseTypeDef",
    "ChangeSetSummaryListItemTypeDef",
    "ChangeSummaryTypeDef",
    "ChangeTypeDef",
    "ContainerProductEntityIdFilterTypeDef",
    "ContainerProductFiltersTypeDef",
    "ContainerProductLastModifiedDateFilterDateRangeTypeDef",
    "ContainerProductLastModifiedDateFilterTypeDef",
    "ContainerProductSortTypeDef",
    "ContainerProductSummaryTypeDef",
    "ContainerProductTitleFilterTypeDef",
    "ContainerProductVisibilityFilterTypeDef",
    "DataProductEntityIdFilterTypeDef",
    "DataProductFiltersTypeDef",
    "DataProductLastModifiedDateFilterDateRangeTypeDef",
    "DataProductLastModifiedDateFilterTypeDef",
    "DataProductSortTypeDef",
    "DataProductSummaryTypeDef",
    "DataProductTitleFilterTypeDef",
    "DataProductVisibilityFilterTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DescribeChangeSetRequestTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "DescribeEntityRequestTypeDef",
    "DescribeEntityResponseTypeDef",
    "EntityDetailTypeDef",
    "EntityRequestTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeDef",
    "EntityTypeFiltersTypeDef",
    "EntityTypeSortTypeDef",
    "ErrorDetailTypeDef",
    "FilterTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListChangeSetsRequestPaginateTypeDef",
    "ListChangeSetsRequestTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ListEntitiesRequestPaginateTypeDef",
    "ListEntitiesRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OfferAvailabilityEndDateFilterDateRangeTypeDef",
    "OfferAvailabilityEndDateFilterTypeDef",
    "OfferBuyerAccountsFilterTypeDef",
    "OfferEntityIdFilterTypeDef",
    "OfferFiltersTypeDef",
    "OfferLastModifiedDateFilterDateRangeTypeDef",
    "OfferLastModifiedDateFilterTypeDef",
    "OfferNameFilterTypeDef",
    "OfferProductIdFilterTypeDef",
    "OfferReleaseDateFilterDateRangeTypeDef",
    "OfferReleaseDateFilterTypeDef",
    "OfferResaleAuthorizationIdFilterTypeDef",
    "OfferSortTypeDef",
    "OfferStateFilterTypeDef",
    "OfferSummaryTypeDef",
    "OfferTargetingFilterTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef",
    "ResaleAuthorizationAvailabilityEndDateFilterTypeDef",
    "ResaleAuthorizationCreatedDateFilterDateRangeTypeDef",
    "ResaleAuthorizationCreatedDateFilterTypeDef",
    "ResaleAuthorizationEntityIdFilterTypeDef",
    "ResaleAuthorizationFiltersTypeDef",
    "ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef",
    "ResaleAuthorizationLastModifiedDateFilterTypeDef",
    "ResaleAuthorizationManufacturerAccountIdFilterTypeDef",
    "ResaleAuthorizationManufacturerLegalNameFilterTypeDef",
    "ResaleAuthorizationNameFilterTypeDef",
    "ResaleAuthorizationOfferExtendedStatusFilterTypeDef",
    "ResaleAuthorizationProductIdFilterTypeDef",
    "ResaleAuthorizationProductNameFilterTypeDef",
    "ResaleAuthorizationResellerAccountIDFilterTypeDef",
    "ResaleAuthorizationResellerLegalNameFilterTypeDef",
    "ResaleAuthorizationSortTypeDef",
    "ResaleAuthorizationStatusFilterTypeDef",
    "ResaleAuthorizationSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SaaSProductEntityIdFilterTypeDef",
    "SaaSProductFiltersTypeDef",
    "SaaSProductLastModifiedDateFilterDateRangeTypeDef",
    "SaaSProductLastModifiedDateFilterTypeDef",
    "SaaSProductSortTypeDef",
    "SaaSProductSummaryTypeDef",
    "SaaSProductTitleFilterTypeDef",
    "SaaSProductVisibilityFilterTypeDef",
    "SortTypeDef",
    "StartChangeSetRequestTypeDef",
    "StartChangeSetResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
)

class AmiProductEntityIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class AmiProductTitleFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class AmiProductVisibilityFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[AmiProductVisibilityStringType]]

class AmiProductLastModifiedDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class AmiProductSortTypeDef(TypedDict):
    SortBy: NotRequired[AmiProductSortByType]
    SortOrder: NotRequired[SortOrderType]

class AmiProductSummaryTypeDef(TypedDict):
    ProductTitle: NotRequired[str]
    Visibility: NotRequired[AmiProductVisibilityStringType]

class EntityRequestTypeDef(TypedDict):
    Catalog: str
    EntityId: str

class BatchDescribeErrorDetailTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class EntityDetailTypeDef(TypedDict):
    EntityType: NotRequired[str]
    EntityArn: NotRequired[str]
    EntityIdentifier: NotRequired[str]
    LastModifiedDate: NotRequired[str]
    DetailsDocument: NotRequired[Dict[str, Any]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CancelChangeSetRequestTypeDef(TypedDict):
    Catalog: str
    ChangeSetId: str

class ChangeSetSummaryListItemTypeDef(TypedDict):
    ChangeSetId: NotRequired[str]
    ChangeSetArn: NotRequired[str]
    ChangeSetName: NotRequired[str]
    StartTime: NotRequired[str]
    EndTime: NotRequired[str]
    Status: NotRequired[ChangeStatusType]
    EntityIdList: NotRequired[List[str]]
    FailureCode: NotRequired[FailureCodeType]

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Type": str,
        "Identifier": NotRequired[str],
    },
)

class ErrorDetailTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ContainerProductEntityIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class ContainerProductTitleFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class ContainerProductVisibilityFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[ContainerProductVisibilityStringType]]

class ContainerProductLastModifiedDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class ContainerProductSortTypeDef(TypedDict):
    SortBy: NotRequired[ContainerProductSortByType]
    SortOrder: NotRequired[SortOrderType]

class ContainerProductSummaryTypeDef(TypedDict):
    ProductTitle: NotRequired[str]
    Visibility: NotRequired[ContainerProductVisibilityStringType]

class DataProductEntityIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class DataProductTitleFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class DataProductVisibilityFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[DataProductVisibilityStringType]]

class DataProductLastModifiedDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class DataProductSortTypeDef(TypedDict):
    SortBy: NotRequired[DataProductSortByType]
    SortOrder: NotRequired[SortOrderType]

class DataProductSummaryTypeDef(TypedDict):
    ProductTitle: NotRequired[str]
    Visibility: NotRequired[DataProductVisibilityStringType]

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class DescribeChangeSetRequestTypeDef(TypedDict):
    Catalog: str
    ChangeSetId: str

class DescribeEntityRequestTypeDef(TypedDict):
    Catalog: str
    EntityId: str

class OfferSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    ProductId: NotRequired[str]
    ResaleAuthorizationId: NotRequired[str]
    ReleaseDate: NotRequired[str]
    AvailabilityEndDate: NotRequired[str]
    BuyerAccounts: NotRequired[List[str]]
    State: NotRequired[OfferStateStringType]
    Targeting: NotRequired[List[OfferTargetingStringType]]

class ResaleAuthorizationSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    ProductId: NotRequired[str]
    ProductName: NotRequired[str]
    ManufacturerAccountId: NotRequired[str]
    ManufacturerLegalName: NotRequired[str]
    ResellerAccountID: NotRequired[str]
    ResellerLegalName: NotRequired[str]
    Status: NotRequired[ResaleAuthorizationStatusStringType]
    OfferExtendedStatus: NotRequired[str]
    CreatedDate: NotRequired[str]
    AvailabilityEndDate: NotRequired[str]

class SaaSProductSummaryTypeDef(TypedDict):
    ProductTitle: NotRequired[str]
    Visibility: NotRequired[SaaSProductVisibilityStringType]

class OfferSortTypeDef(TypedDict):
    SortBy: NotRequired[OfferSortByType]
    SortOrder: NotRequired[SortOrderType]

class ResaleAuthorizationSortTypeDef(TypedDict):
    SortBy: NotRequired[ResaleAuthorizationSortByType]
    SortOrder: NotRequired[SortOrderType]

class SaaSProductSortTypeDef(TypedDict):
    SortBy: NotRequired[SaaSProductSortByType]
    SortOrder: NotRequired[SortOrderType]

class FilterTypeDef(TypedDict):
    Name: NotRequired[str]
    ValueList: NotRequired[Sequence[str]]

class GetResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class SortTypeDef(TypedDict):
    SortBy: NotRequired[str]
    SortOrder: NotRequired[SortOrderType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class OfferAvailabilityEndDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class OfferBuyerAccountsFilterTypeDef(TypedDict):
    WildCardValue: NotRequired[str]

class OfferEntityIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class OfferNameFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class OfferProductIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class OfferResaleAuthorizationIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class OfferStateFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[OfferStateStringType]]

class OfferTargetingFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[OfferTargetingStringType]]

class OfferLastModifiedDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class OfferReleaseDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    Policy: str

class ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class ResaleAuthorizationCreatedDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class ResaleAuthorizationEntityIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class ResaleAuthorizationManufacturerAccountIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class ResaleAuthorizationManufacturerLegalNameFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class ResaleAuthorizationNameFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class ResaleAuthorizationOfferExtendedStatusFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class ResaleAuthorizationProductIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class ResaleAuthorizationProductNameFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class ResaleAuthorizationResellerAccountIDFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class ResaleAuthorizationResellerLegalNameFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class ResaleAuthorizationStatusFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[ResaleAuthorizationStatusStringType]]

class ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class SaaSProductEntityIdFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]

class SaaSProductTitleFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[str]]
    WildCardValue: NotRequired[str]

class SaaSProductVisibilityFilterTypeDef(TypedDict):
    ValueList: NotRequired[Sequence[SaaSProductVisibilityStringType]]

class SaaSProductLastModifiedDateFilterDateRangeTypeDef(TypedDict):
    AfterValue: NotRequired[str]
    BeforeValue: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class AmiProductLastModifiedDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[AmiProductLastModifiedDateFilterDateRangeTypeDef]

class BatchDescribeEntitiesRequestTypeDef(TypedDict):
    EntityRequestList: Sequence[EntityRequestTypeDef]

class BatchDescribeEntitiesResponseTypeDef(TypedDict):
    EntityDetails: Dict[str, EntityDetailTypeDef]
    Errors: Dict[str, BatchDescribeErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelChangeSetResponseTypeDef(TypedDict):
    ChangeSetId: str
    ChangeSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntityResponseTypeDef(TypedDict):
    EntityType: str
    EntityIdentifier: str
    EntityArn: str
    LastModifiedDate: str
    Details: str
    DetailsDocument: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartChangeSetResponseTypeDef(TypedDict):
    ChangeSetId: str
    ChangeSetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListChangeSetsResponseTypeDef(TypedDict):
    ChangeSetSummaryList: List[ChangeSetSummaryListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ChangeSummaryTypeDef(TypedDict):
    ChangeType: NotRequired[str]
    Entity: NotRequired[EntityTypeDef]
    Details: NotRequired[str]
    DetailsDocument: NotRequired[Dict[str, Any]]
    ErrorDetailList: NotRequired[List[ErrorDetailTypeDef]]
    ChangeName: NotRequired[str]

class ChangeTypeDef(TypedDict):
    ChangeType: str
    Entity: EntityTypeDef
    EntityTags: NotRequired[Sequence[TagTypeDef]]
    Details: NotRequired[str]
    DetailsDocument: NotRequired[Mapping[str, Any]]
    ChangeName: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ContainerProductLastModifiedDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[ContainerProductLastModifiedDateFilterDateRangeTypeDef]

class DataProductLastModifiedDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[DataProductLastModifiedDateFilterDateRangeTypeDef]

class EntitySummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    EntityType: NotRequired[str]
    EntityId: NotRequired[str]
    EntityArn: NotRequired[str]
    LastModifiedDate: NotRequired[str]
    Visibility: NotRequired[str]
    AmiProductSummary: NotRequired[AmiProductSummaryTypeDef]
    ContainerProductSummary: NotRequired[ContainerProductSummaryTypeDef]
    DataProductSummary: NotRequired[DataProductSummaryTypeDef]
    SaaSProductSummary: NotRequired[SaaSProductSummaryTypeDef]
    OfferSummary: NotRequired[OfferSummaryTypeDef]
    ResaleAuthorizationSummary: NotRequired[ResaleAuthorizationSummaryTypeDef]

class EntityTypeSortTypeDef(TypedDict):
    DataProductSort: NotRequired[DataProductSortTypeDef]
    SaaSProductSort: NotRequired[SaaSProductSortTypeDef]
    AmiProductSort: NotRequired[AmiProductSortTypeDef]
    OfferSort: NotRequired[OfferSortTypeDef]
    ContainerProductSort: NotRequired[ContainerProductSortTypeDef]
    ResaleAuthorizationSort: NotRequired[ResaleAuthorizationSortTypeDef]

class ListChangeSetsRequestPaginateTypeDef(TypedDict):
    Catalog: str
    FilterList: NotRequired[Sequence[FilterTypeDef]]
    Sort: NotRequired[SortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListChangeSetsRequestTypeDef(TypedDict):
    Catalog: str
    FilterList: NotRequired[Sequence[FilterTypeDef]]
    Sort: NotRequired[SortTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class OfferAvailabilityEndDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[OfferAvailabilityEndDateFilterDateRangeTypeDef]

class OfferLastModifiedDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[OfferLastModifiedDateFilterDateRangeTypeDef]

class OfferReleaseDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[OfferReleaseDateFilterDateRangeTypeDef]

class ResaleAuthorizationAvailabilityEndDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef]
    ValueList: NotRequired[Sequence[str]]

class ResaleAuthorizationCreatedDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[ResaleAuthorizationCreatedDateFilterDateRangeTypeDef]
    ValueList: NotRequired[Sequence[str]]

class ResaleAuthorizationLastModifiedDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef]

class SaaSProductLastModifiedDateFilterTypeDef(TypedDict):
    DateRange: NotRequired[SaaSProductLastModifiedDateFilterDateRangeTypeDef]

class AmiProductFiltersTypeDef(TypedDict):
    EntityId: NotRequired[AmiProductEntityIdFilterTypeDef]
    LastModifiedDate: NotRequired[AmiProductLastModifiedDateFilterTypeDef]
    ProductTitle: NotRequired[AmiProductTitleFilterTypeDef]
    Visibility: NotRequired[AmiProductVisibilityFilterTypeDef]

class DescribeChangeSetResponseTypeDef(TypedDict):
    ChangeSetId: str
    ChangeSetArn: str
    ChangeSetName: str
    Intent: IntentType
    StartTime: str
    EndTime: str
    Status: ChangeStatusType
    FailureCode: FailureCodeType
    FailureDescription: str
    ChangeSet: List[ChangeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartChangeSetRequestTypeDef(TypedDict):
    Catalog: str
    ChangeSet: Sequence[ChangeTypeDef]
    ChangeSetName: NotRequired[str]
    ClientRequestToken: NotRequired[str]
    ChangeSetTags: NotRequired[Sequence[TagTypeDef]]
    Intent: NotRequired[IntentType]

class ContainerProductFiltersTypeDef(TypedDict):
    EntityId: NotRequired[ContainerProductEntityIdFilterTypeDef]
    LastModifiedDate: NotRequired[ContainerProductLastModifiedDateFilterTypeDef]
    ProductTitle: NotRequired[ContainerProductTitleFilterTypeDef]
    Visibility: NotRequired[ContainerProductVisibilityFilterTypeDef]

class DataProductFiltersTypeDef(TypedDict):
    EntityId: NotRequired[DataProductEntityIdFilterTypeDef]
    ProductTitle: NotRequired[DataProductTitleFilterTypeDef]
    Visibility: NotRequired[DataProductVisibilityFilterTypeDef]
    LastModifiedDate: NotRequired[DataProductLastModifiedDateFilterTypeDef]

class ListEntitiesResponseTypeDef(TypedDict):
    EntitySummaryList: List[EntitySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class OfferFiltersTypeDef(TypedDict):
    EntityId: NotRequired[OfferEntityIdFilterTypeDef]
    Name: NotRequired[OfferNameFilterTypeDef]
    ProductId: NotRequired[OfferProductIdFilterTypeDef]
    ResaleAuthorizationId: NotRequired[OfferResaleAuthorizationIdFilterTypeDef]
    ReleaseDate: NotRequired[OfferReleaseDateFilterTypeDef]
    AvailabilityEndDate: NotRequired[OfferAvailabilityEndDateFilterTypeDef]
    BuyerAccounts: NotRequired[OfferBuyerAccountsFilterTypeDef]
    State: NotRequired[OfferStateFilterTypeDef]
    Targeting: NotRequired[OfferTargetingFilterTypeDef]
    LastModifiedDate: NotRequired[OfferLastModifiedDateFilterTypeDef]

class ResaleAuthorizationFiltersTypeDef(TypedDict):
    EntityId: NotRequired[ResaleAuthorizationEntityIdFilterTypeDef]
    Name: NotRequired[ResaleAuthorizationNameFilterTypeDef]
    ProductId: NotRequired[ResaleAuthorizationProductIdFilterTypeDef]
    CreatedDate: NotRequired[ResaleAuthorizationCreatedDateFilterTypeDef]
    AvailabilityEndDate: NotRequired[ResaleAuthorizationAvailabilityEndDateFilterTypeDef]
    ManufacturerAccountId: NotRequired[ResaleAuthorizationManufacturerAccountIdFilterTypeDef]
    ProductName: NotRequired[ResaleAuthorizationProductNameFilterTypeDef]
    ManufacturerLegalName: NotRequired[ResaleAuthorizationManufacturerLegalNameFilterTypeDef]
    ResellerAccountID: NotRequired[ResaleAuthorizationResellerAccountIDFilterTypeDef]
    ResellerLegalName: NotRequired[ResaleAuthorizationResellerLegalNameFilterTypeDef]
    Status: NotRequired[ResaleAuthorizationStatusFilterTypeDef]
    OfferExtendedStatus: NotRequired[ResaleAuthorizationOfferExtendedStatusFilterTypeDef]
    LastModifiedDate: NotRequired[ResaleAuthorizationLastModifiedDateFilterTypeDef]

class SaaSProductFiltersTypeDef(TypedDict):
    EntityId: NotRequired[SaaSProductEntityIdFilterTypeDef]
    ProductTitle: NotRequired[SaaSProductTitleFilterTypeDef]
    Visibility: NotRequired[SaaSProductVisibilityFilterTypeDef]
    LastModifiedDate: NotRequired[SaaSProductLastModifiedDateFilterTypeDef]

class EntityTypeFiltersTypeDef(TypedDict):
    DataProductFilters: NotRequired[DataProductFiltersTypeDef]
    SaaSProductFilters: NotRequired[SaaSProductFiltersTypeDef]
    AmiProductFilters: NotRequired[AmiProductFiltersTypeDef]
    OfferFilters: NotRequired[OfferFiltersTypeDef]
    ContainerProductFilters: NotRequired[ContainerProductFiltersTypeDef]
    ResaleAuthorizationFilters: NotRequired[ResaleAuthorizationFiltersTypeDef]

class ListEntitiesRequestPaginateTypeDef(TypedDict):
    Catalog: str
    EntityType: str
    FilterList: NotRequired[Sequence[FilterTypeDef]]
    Sort: NotRequired[SortTypeDef]
    OwnershipType: NotRequired[OwnershipTypeType]
    EntityTypeFilters: NotRequired[EntityTypeFiltersTypeDef]
    EntityTypeSort: NotRequired[EntityTypeSortTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEntitiesRequestTypeDef(TypedDict):
    Catalog: str
    EntityType: str
    FilterList: NotRequired[Sequence[FilterTypeDef]]
    Sort: NotRequired[SortTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    OwnershipType: NotRequired[OwnershipTypeType]
    EntityTypeFilters: NotRequired[EntityTypeFiltersTypeDef]
    EntityTypeSort: NotRequired[EntityTypeSortTypeDef]
