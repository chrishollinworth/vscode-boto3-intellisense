"""
Type annotations for invoicing service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_invoicing/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_invoicing.type_defs import BatchGetInvoiceProfileRequestTypeDef

    data: BatchGetInvoiceProfileRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ConnectionTestingMethodType,
    EinvoiceDeliveryAttachmentTypeType,
    EinvoiceDeliveryDocumentTypeType,
    InvoiceTypeType,
    ListInvoiceSummariesResourceTypeType,
    ProcurementPortalNameType,
    ProcurementPortalPreferenceStatusType,
    PurchaseOrderDataSourceTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AmountBreakdownTypeDef",
    "BatchGetInvoiceProfileRequestTypeDef",
    "BatchGetInvoiceProfileResponseTypeDef",
    "BillingPeriodTypeDef",
    "ContactTypeDef",
    "CreateInvoiceUnitRequestTypeDef",
    "CreateInvoiceUnitResponseTypeDef",
    "CreateProcurementPortalPreferenceRequestTypeDef",
    "CreateProcurementPortalPreferenceResponseTypeDef",
    "CurrencyExchangeDetailsTypeDef",
    "DateIntervalTypeDef",
    "DeleteInvoiceUnitRequestTypeDef",
    "DeleteInvoiceUnitResponseTypeDef",
    "DeleteProcurementPortalPreferenceRequestTypeDef",
    "DeleteProcurementPortalPreferenceResponseTypeDef",
    "DiscountsBreakdownAmountTypeDef",
    "DiscountsBreakdownTypeDef",
    "EinvoiceDeliveryPreferenceOutputTypeDef",
    "EinvoiceDeliveryPreferenceTypeDef",
    "EinvoiceDeliveryPreferenceUnionTypeDef",
    "EntityTypeDef",
    "FeesBreakdownAmountTypeDef",
    "FeesBreakdownTypeDef",
    "FiltersTypeDef",
    "GetInvoicePDFRequestTypeDef",
    "GetInvoicePDFResponseTypeDef",
    "GetInvoiceUnitRequestTypeDef",
    "GetInvoiceUnitResponseTypeDef",
    "GetProcurementPortalPreferenceRequestTypeDef",
    "GetProcurementPortalPreferenceResponseTypeDef",
    "InvoiceCurrencyAmountTypeDef",
    "InvoicePDFTypeDef",
    "InvoiceProfileTypeDef",
    "InvoiceSummariesFilterTypeDef",
    "InvoiceSummariesSelectorTypeDef",
    "InvoiceSummaryTypeDef",
    "InvoiceUnitRuleOutputTypeDef",
    "InvoiceUnitRuleTypeDef",
    "InvoiceUnitRuleUnionTypeDef",
    "InvoiceUnitTypeDef",
    "ListInvoiceSummariesRequestPaginateTypeDef",
    "ListInvoiceSummariesRequestTypeDef",
    "ListInvoiceSummariesResponseTypeDef",
    "ListInvoiceUnitsRequestPaginateTypeDef",
    "ListInvoiceUnitsRequestTypeDef",
    "ListInvoiceUnitsResponseTypeDef",
    "ListProcurementPortalPreferencesRequestPaginateTypeDef",
    "ListProcurementPortalPreferencesRequestTypeDef",
    "ListProcurementPortalPreferencesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProcurementPortalPreferenceSelectorOutputTypeDef",
    "ProcurementPortalPreferenceSelectorTypeDef",
    "ProcurementPortalPreferenceSelectorUnionTypeDef",
    "ProcurementPortalPreferenceSummaryTypeDef",
    "ProcurementPortalPreferenceTypeDef",
    "PurchaseOrderDataSourceTypeDef",
    "PutProcurementPortalPreferenceRequestTypeDef",
    "PutProcurementPortalPreferenceResponseTypeDef",
    "ReceiverAddressTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadataTypeDef",
    "SupplementalDocumentTypeDef",
    "TagResourceRequestTypeDef",
    "TaxesBreakdownAmountTypeDef",
    "TaxesBreakdownTypeDef",
    "TestEnvPreferenceInputTypeDef",
    "TestEnvPreferenceTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateInvoiceUnitRequestTypeDef",
    "UpdateInvoiceUnitResponseTypeDef",
    "UpdateProcurementPortalPreferenceStatusRequestTypeDef",
    "UpdateProcurementPortalPreferenceStatusResponseTypeDef",
)

class BatchGetInvoiceProfileRequestTypeDef(TypedDict):
    AccountIds: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BillingPeriodTypeDef(TypedDict):
    Month: int
    Year: int

class ContactTypeDef(TypedDict):
    Name: NotRequired[str]
    Email: NotRequired[str]

class ResourceTagTypeDef(TypedDict):
    Key: str
    Value: str

class TestEnvPreferenceInputTypeDef(TypedDict):
    BuyerDomain: Literal["NetworkID"]
    BuyerIdentifier: str
    SupplierDomain: Literal["NetworkID"]
    SupplierIdentifier: str
    ProcurementPortalSharedSecret: NotRequired[str]
    ProcurementPortalInstanceEndpoint: NotRequired[str]

class CurrencyExchangeDetailsTypeDef(TypedDict):
    SourceCurrencyCode: NotRequired[str]
    TargetCurrencyCode: NotRequired[str]
    Rate: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class DeleteInvoiceUnitRequestTypeDef(TypedDict):
    InvoiceUnitArn: str

class DeleteProcurementPortalPreferenceRequestTypeDef(TypedDict):
    ProcurementPortalPreferenceArn: str

class DiscountsBreakdownAmountTypeDef(TypedDict):
    Description: NotRequired[str]
    Amount: NotRequired[str]
    Rate: NotRequired[str]

class PurchaseOrderDataSourceTypeDef(TypedDict):
    EinvoiceDeliveryDocumentType: NotRequired[EinvoiceDeliveryDocumentTypeType]
    PurchaseOrderDataSourceType: NotRequired[PurchaseOrderDataSourceTypeType]

class EntityTypeDef(TypedDict):
    InvoicingEntity: NotRequired[str]

class FeesBreakdownAmountTypeDef(TypedDict):
    Description: NotRequired[str]
    Amount: NotRequired[str]
    Rate: NotRequired[str]

class FiltersTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    InvoiceReceivers: NotRequired[Sequence[str]]
    Accounts: NotRequired[Sequence[str]]
    BillSourceAccounts: NotRequired[Sequence[str]]

class GetInvoicePDFRequestTypeDef(TypedDict):
    InvoiceId: str

class InvoiceUnitRuleOutputTypeDef(TypedDict):
    LinkedAccounts: NotRequired[List[str]]
    BillSourceAccounts: NotRequired[List[str]]

class GetProcurementPortalPreferenceRequestTypeDef(TypedDict):
    ProcurementPortalPreferenceArn: str

class SupplementalDocumentTypeDef(TypedDict):
    DocumentUrl: NotRequired[str]
    DocumentUrlExpirationDate: NotRequired[datetime]

class ReceiverAddressTypeDef(TypedDict):
    AddressLine1: NotRequired[str]
    AddressLine2: NotRequired[str]
    AddressLine3: NotRequired[str]
    DistrictOrCounty: NotRequired[str]
    City: NotRequired[str]
    StateOrRegion: NotRequired[str]
    CountryCode: NotRequired[str]
    CompanyName: NotRequired[str]
    PostalCode: NotRequired[str]

class InvoiceSummariesSelectorTypeDef(TypedDict):
    ResourceType: ListInvoiceSummariesResourceTypeType
    Value: str

class InvoiceUnitRuleTypeDef(TypedDict):
    LinkedAccounts: NotRequired[Sequence[str]]
    BillSourceAccounts: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListProcurementPortalPreferencesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class ProcurementPortalPreferenceSelectorOutputTypeDef(TypedDict):
    InvoiceUnitArns: NotRequired[List[str]]
    SellerOfRecords: NotRequired[List[str]]

class ProcurementPortalPreferenceSelectorTypeDef(TypedDict):
    InvoiceUnitArns: NotRequired[Sequence[str]]
    SellerOfRecords: NotRequired[Sequence[str]]

class TestEnvPreferenceTypeDef(TypedDict):
    BuyerDomain: Literal["NetworkID"]
    BuyerIdentifier: str
    SupplierDomain: Literal["NetworkID"]
    SupplierIdentifier: str
    ProcurementPortalSharedSecret: NotRequired[str]
    ProcurementPortalInstanceEndpoint: NotRequired[str]
    PurchaseOrderRetrievalEndpoint: NotRequired[str]

class TaxesBreakdownAmountTypeDef(TypedDict):
    Description: NotRequired[str]
    Amount: NotRequired[str]
    Rate: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]

class UpdateProcurementPortalPreferenceStatusRequestTypeDef(TypedDict):
    ProcurementPortalPreferenceArn: str
    EinvoiceDeliveryPreferenceStatus: NotRequired[ProcurementPortalPreferenceStatusType]
    EinvoiceDeliveryPreferenceStatusReason: NotRequired[str]
    PurchaseOrderRetrievalPreferenceStatus: NotRequired[ProcurementPortalPreferenceStatusType]
    PurchaseOrderRetrievalPreferenceStatusReason: NotRequired[str]

class CreateInvoiceUnitResponseTypeDef(TypedDict):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProcurementPortalPreferenceResponseTypeDef(TypedDict):
    ProcurementPortalPreferenceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInvoiceUnitResponseTypeDef(TypedDict):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProcurementPortalPreferenceResponseTypeDef(TypedDict):
    ProcurementPortalPreferenceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutProcurementPortalPreferenceResponseTypeDef(TypedDict):
    ProcurementPortalPreferenceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInvoiceUnitResponseTypeDef(TypedDict):
    InvoiceUnitArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProcurementPortalPreferenceStatusResponseTypeDef(TypedDict):
    ProcurementPortalPreferenceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class DateIntervalTypeDef(TypedDict):
    StartDate: TimestampTypeDef
    EndDate: TimestampTypeDef

class GetInvoiceUnitRequestTypeDef(TypedDict):
    InvoiceUnitArn: str
    AsOf: NotRequired[TimestampTypeDef]

class DiscountsBreakdownTypeDef(TypedDict):
    Breakdown: NotRequired[List[DiscountsBreakdownAmountTypeDef]]
    TotalAmount: NotRequired[str]

EinvoiceDeliveryPreferenceOutputTypeDef = TypedDict(
    "EinvoiceDeliveryPreferenceOutputTypeDef",
    {
        "EinvoiceDeliveryDocumentTypes": List[EinvoiceDeliveryDocumentTypeType],
        "Protocol": Literal["CXML"],
        "PurchaseOrderDataSources": List[PurchaseOrderDataSourceTypeDef],
        "ConnectionTestingMethod": ConnectionTestingMethodType,
        "EinvoiceDeliveryActivationDate": datetime,
        "EinvoiceDeliveryAttachmentTypes": NotRequired[List[EinvoiceDeliveryAttachmentTypeType]],
    },
)
EinvoiceDeliveryPreferenceTypeDef = TypedDict(
    "EinvoiceDeliveryPreferenceTypeDef",
    {
        "EinvoiceDeliveryDocumentTypes": Sequence[EinvoiceDeliveryDocumentTypeType],
        "Protocol": Literal["CXML"],
        "PurchaseOrderDataSources": Sequence[PurchaseOrderDataSourceTypeDef],
        "ConnectionTestingMethod": ConnectionTestingMethodType,
        "EinvoiceDeliveryActivationDate": TimestampTypeDef,
        "EinvoiceDeliveryAttachmentTypes": NotRequired[
            Sequence[EinvoiceDeliveryAttachmentTypeType]
        ],
    },
)

class FeesBreakdownTypeDef(TypedDict):
    Breakdown: NotRequired[List[FeesBreakdownAmountTypeDef]]
    TotalAmount: NotRequired[str]

class ListInvoiceUnitsRequestTypeDef(TypedDict):
    Filters: NotRequired[FiltersTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]
    AsOf: NotRequired[TimestampTypeDef]

class GetInvoiceUnitResponseTypeDef(TypedDict):
    InvoiceUnitArn: str
    InvoiceReceiver: str
    Name: str
    Description: str
    TaxInheritanceDisabled: bool
    Rule: InvoiceUnitRuleOutputTypeDef
    LastModified: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class InvoiceUnitTypeDef(TypedDict):
    InvoiceUnitArn: NotRequired[str]
    InvoiceReceiver: NotRequired[str]
    Name: NotRequired[str]
    Description: NotRequired[str]
    TaxInheritanceDisabled: NotRequired[bool]
    Rule: NotRequired[InvoiceUnitRuleOutputTypeDef]
    LastModified: NotRequired[datetime]

class InvoicePDFTypeDef(TypedDict):
    InvoiceId: NotRequired[str]
    DocumentUrl: NotRequired[str]
    DocumentUrlExpirationDate: NotRequired[datetime]
    SupplementalDocuments: NotRequired[List[SupplementalDocumentTypeDef]]

class InvoiceProfileTypeDef(TypedDict):
    AccountId: NotRequired[str]
    ReceiverName: NotRequired[str]
    ReceiverAddress: NotRequired[ReceiverAddressTypeDef]
    ReceiverEmail: NotRequired[str]
    Issuer: NotRequired[str]
    TaxRegistrationNumber: NotRequired[str]

InvoiceUnitRuleUnionTypeDef = Union[InvoiceUnitRuleTypeDef, InvoiceUnitRuleOutputTypeDef]

class ListInvoiceUnitsRequestPaginateTypeDef(TypedDict):
    Filters: NotRequired[FiltersTypeDef]
    AsOf: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProcurementPortalPreferencesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ProcurementPortalPreferenceSummaryTypeDef(TypedDict):
    AwsAccountId: str
    ProcurementPortalPreferenceArn: str
    ProcurementPortalName: ProcurementPortalNameType
    BuyerDomain: Literal["NetworkID"]
    BuyerIdentifier: str
    SupplierDomain: Literal["NetworkID"]
    SupplierIdentifier: str
    EinvoiceDeliveryEnabled: bool
    PurchaseOrderRetrievalEnabled: bool
    Version: int
    CreateDate: datetime
    LastUpdateDate: datetime
    Selector: NotRequired[ProcurementPortalPreferenceSelectorOutputTypeDef]
    EinvoiceDeliveryPreferenceStatus: NotRequired[ProcurementPortalPreferenceStatusType]
    EinvoiceDeliveryPreferenceStatusReason: NotRequired[str]
    PurchaseOrderRetrievalPreferenceStatus: NotRequired[ProcurementPortalPreferenceStatusType]
    PurchaseOrderRetrievalPreferenceStatusReason: NotRequired[str]

ProcurementPortalPreferenceSelectorUnionTypeDef = Union[
    ProcurementPortalPreferenceSelectorTypeDef, ProcurementPortalPreferenceSelectorOutputTypeDef
]

class TaxesBreakdownTypeDef(TypedDict):
    Breakdown: NotRequired[List[TaxesBreakdownAmountTypeDef]]
    TotalAmount: NotRequired[str]

class InvoiceSummariesFilterTypeDef(TypedDict):
    TimeInterval: NotRequired[DateIntervalTypeDef]
    BillingPeriod: NotRequired[BillingPeriodTypeDef]
    InvoicingEntity: NotRequired[str]

class ProcurementPortalPreferenceTypeDef(TypedDict):
    AwsAccountId: str
    ProcurementPortalPreferenceArn: str
    ProcurementPortalName: ProcurementPortalNameType
    BuyerDomain: Literal["NetworkID"]
    BuyerIdentifier: str
    SupplierDomain: Literal["NetworkID"]
    SupplierIdentifier: str
    EinvoiceDeliveryEnabled: bool
    PurchaseOrderRetrievalEnabled: bool
    Version: int
    CreateDate: datetime
    LastUpdateDate: datetime
    Selector: NotRequired[ProcurementPortalPreferenceSelectorOutputTypeDef]
    ProcurementPortalSharedSecret: NotRequired[str]
    ProcurementPortalInstanceEndpoint: NotRequired[str]
    PurchaseOrderRetrievalEndpoint: NotRequired[str]
    TestEnvPreference: NotRequired[TestEnvPreferenceTypeDef]
    EinvoiceDeliveryPreference: NotRequired[EinvoiceDeliveryPreferenceOutputTypeDef]
    Contacts: NotRequired[List[ContactTypeDef]]
    EinvoiceDeliveryPreferenceStatus: NotRequired[ProcurementPortalPreferenceStatusType]
    EinvoiceDeliveryPreferenceStatusReason: NotRequired[str]
    PurchaseOrderRetrievalPreferenceStatus: NotRequired[ProcurementPortalPreferenceStatusType]
    PurchaseOrderRetrievalPreferenceStatusReason: NotRequired[str]

EinvoiceDeliveryPreferenceUnionTypeDef = Union[
    EinvoiceDeliveryPreferenceTypeDef, EinvoiceDeliveryPreferenceOutputTypeDef
]

class ListInvoiceUnitsResponseTypeDef(TypedDict):
    InvoiceUnits: List[InvoiceUnitTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetInvoicePDFResponseTypeDef(TypedDict):
    InvoicePDF: InvoicePDFTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetInvoiceProfileResponseTypeDef(TypedDict):
    Profiles: List[InvoiceProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInvoiceUnitRequestTypeDef(TypedDict):
    Name: str
    InvoiceReceiver: str
    Rule: InvoiceUnitRuleUnionTypeDef
    Description: NotRequired[str]
    TaxInheritanceDisabled: NotRequired[bool]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]

class UpdateInvoiceUnitRequestTypeDef(TypedDict):
    InvoiceUnitArn: str
    Description: NotRequired[str]
    TaxInheritanceDisabled: NotRequired[bool]
    Rule: NotRequired[InvoiceUnitRuleUnionTypeDef]

class ListProcurementPortalPreferencesResponseTypeDef(TypedDict):
    ProcurementPortalPreferences: List[ProcurementPortalPreferenceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class AmountBreakdownTypeDef(TypedDict):
    SubTotalAmount: NotRequired[str]
    Discounts: NotRequired[DiscountsBreakdownTypeDef]
    Taxes: NotRequired[TaxesBreakdownTypeDef]
    Fees: NotRequired[FeesBreakdownTypeDef]

class ListInvoiceSummariesRequestPaginateTypeDef(TypedDict):
    Selector: InvoiceSummariesSelectorTypeDef
    Filter: NotRequired[InvoiceSummariesFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListInvoiceSummariesRequestTypeDef(TypedDict):
    Selector: InvoiceSummariesSelectorTypeDef
    Filter: NotRequired[InvoiceSummariesFilterTypeDef]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class GetProcurementPortalPreferenceResponseTypeDef(TypedDict):
    ProcurementPortalPreference: ProcurementPortalPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProcurementPortalPreferenceRequestTypeDef(TypedDict):
    ProcurementPortalName: ProcurementPortalNameType
    BuyerDomain: Literal["NetworkID"]
    BuyerIdentifier: str
    SupplierDomain: Literal["NetworkID"]
    SupplierIdentifier: str
    EinvoiceDeliveryEnabled: bool
    PurchaseOrderRetrievalEnabled: bool
    Contacts: Sequence[ContactTypeDef]
    Selector: NotRequired[ProcurementPortalPreferenceSelectorUnionTypeDef]
    ProcurementPortalSharedSecret: NotRequired[str]
    ProcurementPortalInstanceEndpoint: NotRequired[str]
    TestEnvPreference: NotRequired[TestEnvPreferenceInputTypeDef]
    EinvoiceDeliveryPreference: NotRequired[EinvoiceDeliveryPreferenceUnionTypeDef]
    ResourceTags: NotRequired[Sequence[ResourceTagTypeDef]]
    ClientToken: NotRequired[str]

class PutProcurementPortalPreferenceRequestTypeDef(TypedDict):
    ProcurementPortalPreferenceArn: str
    EinvoiceDeliveryEnabled: bool
    PurchaseOrderRetrievalEnabled: bool
    Contacts: Sequence[ContactTypeDef]
    Selector: NotRequired[ProcurementPortalPreferenceSelectorUnionTypeDef]
    ProcurementPortalSharedSecret: NotRequired[str]
    ProcurementPortalInstanceEndpoint: NotRequired[str]
    TestEnvPreference: NotRequired[TestEnvPreferenceInputTypeDef]
    EinvoiceDeliveryPreference: NotRequired[EinvoiceDeliveryPreferenceUnionTypeDef]

class InvoiceCurrencyAmountTypeDef(TypedDict):
    TotalAmount: NotRequired[str]
    TotalAmountBeforeTax: NotRequired[str]
    CurrencyCode: NotRequired[str]
    AmountBreakdown: NotRequired[AmountBreakdownTypeDef]
    CurrencyExchangeDetails: NotRequired[CurrencyExchangeDetailsTypeDef]

class InvoiceSummaryTypeDef(TypedDict):
    AccountId: NotRequired[str]
    InvoiceId: NotRequired[str]
    IssuedDate: NotRequired[datetime]
    DueDate: NotRequired[datetime]
    Entity: NotRequired[EntityTypeDef]
    BillingPeriod: NotRequired[BillingPeriodTypeDef]
    InvoiceType: NotRequired[InvoiceTypeType]
    OriginalInvoiceId: NotRequired[str]
    PurchaseOrderNumber: NotRequired[str]
    BaseCurrencyAmount: NotRequired[InvoiceCurrencyAmountTypeDef]
    TaxCurrencyAmount: NotRequired[InvoiceCurrencyAmountTypeDef]
    PaymentCurrencyAmount: NotRequired[InvoiceCurrencyAmountTypeDef]

class ListInvoiceSummariesResponseTypeDef(TypedDict):
    InvoiceSummaries: List[InvoiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
