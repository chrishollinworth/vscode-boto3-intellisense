"""
Type annotations for marketplace-catalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import AmiProductEntityIdFilterTypeDef

    data: AmiProductEntityIdFilterTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

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

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AmiProductEntityIdFilterTypeDef",
    "AmiProductFiltersTypeDef",
    "AmiProductLastModifiedDateFilterDateRangeTypeDef",
    "AmiProductLastModifiedDateFilterTypeDef",
    "AmiProductSortTypeDef",
    "AmiProductSummaryTypeDef",
    "AmiProductTitleFilterTypeDef",
    "AmiProductVisibilityFilterTypeDef",
    "BatchDescribeEntitiesRequestRequestTypeDef",
    "BatchDescribeEntitiesResponseTypeDef",
    "BatchDescribeErrorDetailTypeDef",
    "CancelChangeSetRequestRequestTypeDef",
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
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DescribeChangeSetRequestRequestTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "DescribeEntityRequestRequestTypeDef",
    "DescribeEntityResponseTypeDef",
    "EntityDetailTypeDef",
    "EntityRequestTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeDef",
    "EntityTypeFiltersTypeDef",
    "EntityTypeSortTypeDef",
    "ErrorDetailTypeDef",
    "FilterTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListChangeSetsRequestRequestTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ListEntitiesRequestRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
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
    "PutResourcePolicyRequestRequestTypeDef",
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
    "StartChangeSetRequestRequestTypeDef",
    "StartChangeSetResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

AmiProductEntityIdFilterTypeDef = TypedDict(
    "AmiProductEntityIdFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

AmiProductFiltersTypeDef = TypedDict(
    "AmiProductFiltersTypeDef",
    {
        "EntityId": "AmiProductEntityIdFilterTypeDef",
        "LastModifiedDate": "AmiProductLastModifiedDateFilterTypeDef",
        "ProductTitle": "AmiProductTitleFilterTypeDef",
        "Visibility": "AmiProductVisibilityFilterTypeDef",
    },
    total=False,
)

AmiProductLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "AmiProductLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

AmiProductLastModifiedDateFilterTypeDef = TypedDict(
    "AmiProductLastModifiedDateFilterTypeDef",
    {
        "DateRange": "AmiProductLastModifiedDateFilterDateRangeTypeDef",
    },
    total=False,
)

AmiProductSortTypeDef = TypedDict(
    "AmiProductSortTypeDef",
    {
        "SortBy": AmiProductSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

AmiProductSummaryTypeDef = TypedDict(
    "AmiProductSummaryTypeDef",
    {
        "ProductTitle": str,
        "Visibility": AmiProductVisibilityStringType,
    },
    total=False,
)

AmiProductTitleFilterTypeDef = TypedDict(
    "AmiProductTitleFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

AmiProductVisibilityFilterTypeDef = TypedDict(
    "AmiProductVisibilityFilterTypeDef",
    {
        "ValueList": List[AmiProductVisibilityStringType],
    },
    total=False,
)

BatchDescribeEntitiesRequestRequestTypeDef = TypedDict(
    "BatchDescribeEntitiesRequestRequestTypeDef",
    {
        "EntityRequestList": List["EntityRequestTypeDef"],
    },
)

BatchDescribeEntitiesResponseTypeDef = TypedDict(
    "BatchDescribeEntitiesResponseTypeDef",
    {
        "EntityDetails": Dict[str, "EntityDetailTypeDef"],
        "Errors": Dict[str, "BatchDescribeErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDescribeErrorDetailTypeDef = TypedDict(
    "BatchDescribeErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

CancelChangeSetRequestRequestTypeDef = TypedDict(
    "CancelChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

CancelChangeSetResponseTypeDef = TypedDict(
    "CancelChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeSetSummaryListItemTypeDef = TypedDict(
    "ChangeSetSummaryListItemTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "EntityIdList": List[str],
        "FailureCode": FailureCodeType,
    },
    total=False,
)

ChangeSummaryTypeDef = TypedDict(
    "ChangeSummaryTypeDef",
    {
        "ChangeType": str,
        "Entity": "EntityTypeDef",
        "Details": str,
        "DetailsDocument": Dict[str, Any],
        "ErrorDetailList": List["ErrorDetailTypeDef"],
        "ChangeName": str,
    },
    total=False,
)

_RequiredChangeTypeDef = TypedDict(
    "_RequiredChangeTypeDef",
    {
        "ChangeType": str,
        "Entity": "EntityTypeDef",
    },
)
_OptionalChangeTypeDef = TypedDict(
    "_OptionalChangeTypeDef",
    {
        "EntityTags": List["TagTypeDef"],
        "Details": str,
        "DetailsDocument": Dict[str, Any],
        "ChangeName": str,
    },
    total=False,
)

class ChangeTypeDef(_RequiredChangeTypeDef, _OptionalChangeTypeDef):
    pass

ContainerProductEntityIdFilterTypeDef = TypedDict(
    "ContainerProductEntityIdFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

ContainerProductFiltersTypeDef = TypedDict(
    "ContainerProductFiltersTypeDef",
    {
        "EntityId": "ContainerProductEntityIdFilterTypeDef",
        "LastModifiedDate": "ContainerProductLastModifiedDateFilterTypeDef",
        "ProductTitle": "ContainerProductTitleFilterTypeDef",
        "Visibility": "ContainerProductVisibilityFilterTypeDef",
    },
    total=False,
)

ContainerProductLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "ContainerProductLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

ContainerProductLastModifiedDateFilterTypeDef = TypedDict(
    "ContainerProductLastModifiedDateFilterTypeDef",
    {
        "DateRange": "ContainerProductLastModifiedDateFilterDateRangeTypeDef",
    },
    total=False,
)

ContainerProductSortTypeDef = TypedDict(
    "ContainerProductSortTypeDef",
    {
        "SortBy": ContainerProductSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ContainerProductSummaryTypeDef = TypedDict(
    "ContainerProductSummaryTypeDef",
    {
        "ProductTitle": str,
        "Visibility": ContainerProductVisibilityStringType,
    },
    total=False,
)

ContainerProductTitleFilterTypeDef = TypedDict(
    "ContainerProductTitleFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

ContainerProductVisibilityFilterTypeDef = TypedDict(
    "ContainerProductVisibilityFilterTypeDef",
    {
        "ValueList": List[ContainerProductVisibilityStringType],
    },
    total=False,
)

DataProductEntityIdFilterTypeDef = TypedDict(
    "DataProductEntityIdFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

DataProductFiltersTypeDef = TypedDict(
    "DataProductFiltersTypeDef",
    {
        "EntityId": "DataProductEntityIdFilterTypeDef",
        "ProductTitle": "DataProductTitleFilterTypeDef",
        "Visibility": "DataProductVisibilityFilterTypeDef",
        "LastModifiedDate": "DataProductLastModifiedDateFilterTypeDef",
    },
    total=False,
)

DataProductLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "DataProductLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

DataProductLastModifiedDateFilterTypeDef = TypedDict(
    "DataProductLastModifiedDateFilterTypeDef",
    {
        "DateRange": "DataProductLastModifiedDateFilterDateRangeTypeDef",
    },
    total=False,
)

DataProductSortTypeDef = TypedDict(
    "DataProductSortTypeDef",
    {
        "SortBy": DataProductSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

DataProductSummaryTypeDef = TypedDict(
    "DataProductSummaryTypeDef",
    {
        "ProductTitle": str,
        "Visibility": DataProductVisibilityStringType,
    },
    total=False,
)

DataProductTitleFilterTypeDef = TypedDict(
    "DataProductTitleFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

DataProductVisibilityFilterTypeDef = TypedDict(
    "DataProductVisibilityFilterTypeDef",
    {
        "ValueList": List[DataProductVisibilityStringType],
    },
    total=False,
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeChangeSetRequestRequestTypeDef = TypedDict(
    "DescribeChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

DescribeChangeSetResponseTypeDef = TypedDict(
    "DescribeChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "Intent": IntentType,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "FailureCode": FailureCodeType,
        "FailureDescription": str,
        "ChangeSet": List["ChangeSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityRequestRequestTypeDef = TypedDict(
    "DescribeEntityRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityId": str,
    },
)

DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
        "DetailsDocument": Dict[str, Any],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntityDetailTypeDef = TypedDict(
    "EntityDetailTypeDef",
    {
        "EntityType": str,
        "EntityArn": str,
        "EntityIdentifier": str,
        "LastModifiedDate": str,
        "DetailsDocument": Dict[str, Any],
    },
    total=False,
)

EntityRequestTypeDef = TypedDict(
    "EntityRequestTypeDef",
    {
        "Catalog": str,
        "EntityId": str,
    },
)

EntitySummaryTypeDef = TypedDict(
    "EntitySummaryTypeDef",
    {
        "Name": str,
        "EntityType": str,
        "EntityId": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Visibility": str,
        "AmiProductSummary": "AmiProductSummaryTypeDef",
        "ContainerProductSummary": "ContainerProductSummaryTypeDef",
        "DataProductSummary": "DataProductSummaryTypeDef",
        "SaaSProductSummary": "SaaSProductSummaryTypeDef",
        "OfferSummary": "OfferSummaryTypeDef",
        "ResaleAuthorizationSummary": "ResaleAuthorizationSummaryTypeDef",
    },
    total=False,
)

_RequiredEntityTypeDef = TypedDict(
    "_RequiredEntityTypeDef",
    {
        "Type": str,
    },
)
_OptionalEntityTypeDef = TypedDict(
    "_OptionalEntityTypeDef",
    {
        "Identifier": str,
    },
    total=False,
)

class EntityTypeDef(_RequiredEntityTypeDef, _OptionalEntityTypeDef):
    pass

EntityTypeFiltersTypeDef = TypedDict(
    "EntityTypeFiltersTypeDef",
    {
        "DataProductFilters": "DataProductFiltersTypeDef",
        "SaaSProductFilters": "SaaSProductFiltersTypeDef",
        "AmiProductFilters": "AmiProductFiltersTypeDef",
        "OfferFilters": "OfferFiltersTypeDef",
        "ContainerProductFilters": "ContainerProductFiltersTypeDef",
        "ResaleAuthorizationFilters": "ResaleAuthorizationFiltersTypeDef",
    },
    total=False,
)

EntityTypeSortTypeDef = TypedDict(
    "EntityTypeSortTypeDef",
    {
        "DataProductSort": "DataProductSortTypeDef",
        "SaaSProductSort": "SaaSProductSortTypeDef",
        "AmiProductSort": "AmiProductSortTypeDef",
        "OfferSort": "OfferSortTypeDef",
        "ContainerProductSort": "ContainerProductSortTypeDef",
        "ResaleAuthorizationSort": "ResaleAuthorizationSortTypeDef",
    },
    total=False,
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "ValueList": List[str],
    },
    total=False,
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChangeSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListChangeSetsRequestRequestTypeDef",
    {
        "Catalog": str,
    },
)
_OptionalListChangeSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListChangeSetsRequestRequestTypeDef",
    {
        "FilterList": List["FilterTypeDef"],
        "Sort": "SortTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChangeSetsRequestRequestTypeDef(
    _RequiredListChangeSetsRequestRequestTypeDef, _OptionalListChangeSetsRequestRequestTypeDef
):
    pass

ListChangeSetsResponseTypeDef = TypedDict(
    "ListChangeSetsResponseTypeDef",
    {
        "ChangeSetSummaryList": List["ChangeSetSummaryListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredListEntitiesRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityType": str,
    },
)
_OptionalListEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalListEntitiesRequestRequestTypeDef",
    {
        "FilterList": List["FilterTypeDef"],
        "Sort": "SortTypeDef",
        "NextToken": str,
        "MaxResults": int,
        "OwnershipType": OwnershipTypeType,
        "EntityTypeFilters": "EntityTypeFiltersTypeDef",
        "EntityTypeSort": "EntityTypeSortTypeDef",
    },
    total=False,
)

class ListEntitiesRequestRequestTypeDef(
    _RequiredListEntitiesRequestRequestTypeDef, _OptionalListEntitiesRequestRequestTypeDef
):
    pass

ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "EntitySummaryList": List["EntitySummaryTypeDef"],
        "NextToken": str,
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
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OfferAvailabilityEndDateFilterDateRangeTypeDef = TypedDict(
    "OfferAvailabilityEndDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

OfferAvailabilityEndDateFilterTypeDef = TypedDict(
    "OfferAvailabilityEndDateFilterTypeDef",
    {
        "DateRange": "OfferAvailabilityEndDateFilterDateRangeTypeDef",
    },
    total=False,
)

OfferBuyerAccountsFilterTypeDef = TypedDict(
    "OfferBuyerAccountsFilterTypeDef",
    {
        "WildCardValue": str,
    },
    total=False,
)

OfferEntityIdFilterTypeDef = TypedDict(
    "OfferEntityIdFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

OfferFiltersTypeDef = TypedDict(
    "OfferFiltersTypeDef",
    {
        "EntityId": "OfferEntityIdFilterTypeDef",
        "Name": "OfferNameFilterTypeDef",
        "ProductId": "OfferProductIdFilterTypeDef",
        "ResaleAuthorizationId": "OfferResaleAuthorizationIdFilterTypeDef",
        "ReleaseDate": "OfferReleaseDateFilterTypeDef",
        "AvailabilityEndDate": "OfferAvailabilityEndDateFilterTypeDef",
        "BuyerAccounts": "OfferBuyerAccountsFilterTypeDef",
        "State": "OfferStateFilterTypeDef",
        "Targeting": "OfferTargetingFilterTypeDef",
        "LastModifiedDate": "OfferLastModifiedDateFilterTypeDef",
    },
    total=False,
)

OfferLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "OfferLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

OfferLastModifiedDateFilterTypeDef = TypedDict(
    "OfferLastModifiedDateFilterTypeDef",
    {
        "DateRange": "OfferLastModifiedDateFilterDateRangeTypeDef",
    },
    total=False,
)

OfferNameFilterTypeDef = TypedDict(
    "OfferNameFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

OfferProductIdFilterTypeDef = TypedDict(
    "OfferProductIdFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

OfferReleaseDateFilterDateRangeTypeDef = TypedDict(
    "OfferReleaseDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

OfferReleaseDateFilterTypeDef = TypedDict(
    "OfferReleaseDateFilterTypeDef",
    {
        "DateRange": "OfferReleaseDateFilterDateRangeTypeDef",
    },
    total=False,
)

OfferResaleAuthorizationIdFilterTypeDef = TypedDict(
    "OfferResaleAuthorizationIdFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

OfferSortTypeDef = TypedDict(
    "OfferSortTypeDef",
    {
        "SortBy": OfferSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

OfferStateFilterTypeDef = TypedDict(
    "OfferStateFilterTypeDef",
    {
        "ValueList": List[OfferStateStringType],
    },
    total=False,
)

OfferSummaryTypeDef = TypedDict(
    "OfferSummaryTypeDef",
    {
        "Name": str,
        "ProductId": str,
        "ResaleAuthorizationId": str,
        "ReleaseDate": str,
        "AvailabilityEndDate": str,
        "BuyerAccounts": List[str],
        "State": OfferStateStringType,
        "Targeting": List[OfferTargetingStringType],
    },
    total=False,
)

OfferTargetingFilterTypeDef = TypedDict(
    "OfferTargetingFilterTypeDef",
    {
        "ValueList": List[OfferTargetingStringType],
    },
    total=False,
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

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef = TypedDict(
    "ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

ResaleAuthorizationAvailabilityEndDateFilterTypeDef = TypedDict(
    "ResaleAuthorizationAvailabilityEndDateFilterTypeDef",
    {
        "DateRange": "ResaleAuthorizationAvailabilityEndDateFilterDateRangeTypeDef",
        "ValueList": List[str],
    },
    total=False,
)

ResaleAuthorizationCreatedDateFilterDateRangeTypeDef = TypedDict(
    "ResaleAuthorizationCreatedDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

ResaleAuthorizationCreatedDateFilterTypeDef = TypedDict(
    "ResaleAuthorizationCreatedDateFilterTypeDef",
    {
        "DateRange": "ResaleAuthorizationCreatedDateFilterDateRangeTypeDef",
        "ValueList": List[str],
    },
    total=False,
)

ResaleAuthorizationEntityIdFilterTypeDef = TypedDict(
    "ResaleAuthorizationEntityIdFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

ResaleAuthorizationFiltersTypeDef = TypedDict(
    "ResaleAuthorizationFiltersTypeDef",
    {
        "EntityId": "ResaleAuthorizationEntityIdFilterTypeDef",
        "Name": "ResaleAuthorizationNameFilterTypeDef",
        "ProductId": "ResaleAuthorizationProductIdFilterTypeDef",
        "CreatedDate": "ResaleAuthorizationCreatedDateFilterTypeDef",
        "AvailabilityEndDate": "ResaleAuthorizationAvailabilityEndDateFilterTypeDef",
        "ManufacturerAccountId": "ResaleAuthorizationManufacturerAccountIdFilterTypeDef",
        "ProductName": "ResaleAuthorizationProductNameFilterTypeDef",
        "ManufacturerLegalName": "ResaleAuthorizationManufacturerLegalNameFilterTypeDef",
        "ResellerAccountID": "ResaleAuthorizationResellerAccountIDFilterTypeDef",
        "ResellerLegalName": "ResaleAuthorizationResellerLegalNameFilterTypeDef",
        "Status": "ResaleAuthorizationStatusFilterTypeDef",
        "OfferExtendedStatus": "ResaleAuthorizationOfferExtendedStatusFilterTypeDef",
        "LastModifiedDate": "ResaleAuthorizationLastModifiedDateFilterTypeDef",
    },
    total=False,
)

ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

ResaleAuthorizationLastModifiedDateFilterTypeDef = TypedDict(
    "ResaleAuthorizationLastModifiedDateFilterTypeDef",
    {
        "DateRange": "ResaleAuthorizationLastModifiedDateFilterDateRangeTypeDef",
    },
    total=False,
)

ResaleAuthorizationManufacturerAccountIdFilterTypeDef = TypedDict(
    "ResaleAuthorizationManufacturerAccountIdFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

ResaleAuthorizationManufacturerLegalNameFilterTypeDef = TypedDict(
    "ResaleAuthorizationManufacturerLegalNameFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

ResaleAuthorizationNameFilterTypeDef = TypedDict(
    "ResaleAuthorizationNameFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

ResaleAuthorizationOfferExtendedStatusFilterTypeDef = TypedDict(
    "ResaleAuthorizationOfferExtendedStatusFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

ResaleAuthorizationProductIdFilterTypeDef = TypedDict(
    "ResaleAuthorizationProductIdFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

ResaleAuthorizationProductNameFilterTypeDef = TypedDict(
    "ResaleAuthorizationProductNameFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

ResaleAuthorizationResellerAccountIDFilterTypeDef = TypedDict(
    "ResaleAuthorizationResellerAccountIDFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

ResaleAuthorizationResellerLegalNameFilterTypeDef = TypedDict(
    "ResaleAuthorizationResellerLegalNameFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

ResaleAuthorizationSortTypeDef = TypedDict(
    "ResaleAuthorizationSortTypeDef",
    {
        "SortBy": ResaleAuthorizationSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

ResaleAuthorizationStatusFilterTypeDef = TypedDict(
    "ResaleAuthorizationStatusFilterTypeDef",
    {
        "ValueList": List[ResaleAuthorizationStatusStringType],
    },
    total=False,
)

ResaleAuthorizationSummaryTypeDef = TypedDict(
    "ResaleAuthorizationSummaryTypeDef",
    {
        "Name": str,
        "ProductId": str,
        "ProductName": str,
        "ManufacturerAccountId": str,
        "ManufacturerLegalName": str,
        "ResellerAccountID": str,
        "ResellerLegalName": str,
        "Status": ResaleAuthorizationStatusStringType,
        "OfferExtendedStatus": str,
        "CreatedDate": str,
        "AvailabilityEndDate": str,
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

SaaSProductEntityIdFilterTypeDef = TypedDict(
    "SaaSProductEntityIdFilterTypeDef",
    {
        "ValueList": List[str],
    },
    total=False,
)

SaaSProductFiltersTypeDef = TypedDict(
    "SaaSProductFiltersTypeDef",
    {
        "EntityId": "SaaSProductEntityIdFilterTypeDef",
        "ProductTitle": "SaaSProductTitleFilterTypeDef",
        "Visibility": "SaaSProductVisibilityFilterTypeDef",
        "LastModifiedDate": "SaaSProductLastModifiedDateFilterTypeDef",
    },
    total=False,
)

SaaSProductLastModifiedDateFilterDateRangeTypeDef = TypedDict(
    "SaaSProductLastModifiedDateFilterDateRangeTypeDef",
    {
        "AfterValue": str,
        "BeforeValue": str,
    },
    total=False,
)

SaaSProductLastModifiedDateFilterTypeDef = TypedDict(
    "SaaSProductLastModifiedDateFilterTypeDef",
    {
        "DateRange": "SaaSProductLastModifiedDateFilterDateRangeTypeDef",
    },
    total=False,
)

SaaSProductSortTypeDef = TypedDict(
    "SaaSProductSortTypeDef",
    {
        "SortBy": SaaSProductSortByType,
        "SortOrder": SortOrderType,
    },
    total=False,
)

SaaSProductSummaryTypeDef = TypedDict(
    "SaaSProductSummaryTypeDef",
    {
        "ProductTitle": str,
        "Visibility": SaaSProductVisibilityStringType,
    },
    total=False,
)

SaaSProductTitleFilterTypeDef = TypedDict(
    "SaaSProductTitleFilterTypeDef",
    {
        "ValueList": List[str],
        "WildCardValue": str,
    },
    total=False,
)

SaaSProductVisibilityFilterTypeDef = TypedDict(
    "SaaSProductVisibilityFilterTypeDef",
    {
        "ValueList": List[SaaSProductVisibilityStringType],
    },
    total=False,
)

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "SortBy": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

_RequiredStartChangeSetRequestRequestTypeDef = TypedDict(
    "_RequiredStartChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSet": List["ChangeTypeDef"],
    },
)
_OptionalStartChangeSetRequestRequestTypeDef = TypedDict(
    "_OptionalStartChangeSetRequestRequestTypeDef",
    {
        "ChangeSetName": str,
        "ClientRequestToken": str,
        "ChangeSetTags": List["TagTypeDef"],
        "Intent": IntentType,
    },
    total=False,
)

class StartChangeSetRequestRequestTypeDef(
    _RequiredStartChangeSetRequestRequestTypeDef, _OptionalStartChangeSetRequestRequestTypeDef
):
    pass

StartChangeSetResponseTypeDef = TypedDict(
    "StartChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
