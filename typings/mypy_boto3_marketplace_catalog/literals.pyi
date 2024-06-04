"""
Type annotations for marketplace-catalog service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/literals.html)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.literals import AmiProductSortByType

    data: AmiProductSortByType = "EntityId"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AmiProductSortByType",
    "AmiProductVisibilityStringType",
    "ChangeStatusType",
    "ContainerProductSortByType",
    "ContainerProductVisibilityStringType",
    "DataProductSortByType",
    "DataProductVisibilityStringType",
    "FailureCodeType",
    "IntentType",
    "ListChangeSetsPaginatorName",
    "ListEntitiesPaginatorName",
    "OfferSortByType",
    "OfferStateStringType",
    "OfferTargetingStringType",
    "OwnershipTypeType",
    "ResaleAuthorizationSortByType",
    "ResaleAuthorizationStatusStringType",
    "SaaSProductSortByType",
    "SaaSProductVisibilityStringType",
    "SortOrderType",
)

AmiProductSortByType = Literal["EntityId", "LastModifiedDate", "ProductTitle", "Visibility"]
AmiProductVisibilityStringType = Literal["Draft", "Limited", "Public", "Restricted"]
ChangeStatusType = Literal["APPLYING", "CANCELLED", "FAILED", "PREPARING", "SUCCEEDED"]
ContainerProductSortByType = Literal["EntityId", "LastModifiedDate", "ProductTitle", "Visibility"]
ContainerProductVisibilityStringType = Literal["Draft", "Limited", "Public", "Restricted"]
DataProductSortByType = Literal["EntityId", "LastModifiedDate", "ProductTitle", "Visibility"]
DataProductVisibilityStringType = Literal["Draft", "Limited", "Public", "Restricted", "Unavailable"]
FailureCodeType = Literal["CLIENT_ERROR", "SERVER_FAULT"]
IntentType = Literal["APPLY", "VALIDATE"]
ListChangeSetsPaginatorName = Literal["list_change_sets"]
ListEntitiesPaginatorName = Literal["list_entities"]
OfferSortByType = Literal[
    "AvailabilityEndDate",
    "BuyerAccounts",
    "EntityId",
    "LastModifiedDate",
    "Name",
    "ProductId",
    "ReleaseDate",
    "ResaleAuthorizationId",
    "State",
    "Targeting",
]
OfferStateStringType = Literal["Draft", "Released"]
OfferTargetingStringType = Literal["BuyerAccounts", "CountryCodes", "None", "ParticipatingPrograms"]
OwnershipTypeType = Literal["SELF", "SHARED"]
ResaleAuthorizationSortByType = Literal[
    "AvailabilityEndDate",
    "CreatedDate",
    "EntityId",
    "LastModifiedDate",
    "ManufacturerAccountId",
    "ManufacturerLegalName",
    "Name",
    "OfferExtendedStatus",
    "ProductId",
    "ProductName",
    "ResellerAccountID",
    "ResellerLegalName",
    "Status",
]
ResaleAuthorizationStatusStringType = Literal["Active", "Draft", "Restricted"]
SaaSProductSortByType = Literal["EntityId", "LastModifiedDate", "ProductTitle", "Visibility"]
SaaSProductVisibilityStringType = Literal["Draft", "Limited", "Public", "Restricted"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
