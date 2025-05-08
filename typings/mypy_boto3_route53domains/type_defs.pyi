"""
Type annotations for route53domains service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53domains/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_route53domains.type_defs import AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef

    data: AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ContactTypeType,
    CountryCodeType,
    DomainAvailabilityType,
    ExtraParamNameType,
    ListDomainsAttributeNameType,
    OperationStatusType,
    OperationTypeType,
    OperatorType,
    ReachabilityStatusType,
    SortOrderType,
    StatusFlagType,
    TransferableType,
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
    "AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef",
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "AssociateDelegationSignerToDomainRequestTypeDef",
    "AssociateDelegationSignerToDomainResponseTypeDef",
    "BillingRecordTypeDef",
    "CancelDomainTransferToAnotherAwsAccountRequestTypeDef",
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    "CheckDomainAvailabilityRequestTypeDef",
    "CheckDomainAvailabilityResponseTypeDef",
    "CheckDomainTransferabilityRequestTypeDef",
    "CheckDomainTransferabilityResponseTypeDef",
    "ConsentTypeDef",
    "ContactDetailOutputTypeDef",
    "ContactDetailTypeDef",
    "ContactDetailUnionTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteTagsForDomainRequestTypeDef",
    "DisableDomainAutoRenewRequestTypeDef",
    "DisableDomainTransferLockRequestTypeDef",
    "DisableDomainTransferLockResponseTypeDef",
    "DisassociateDelegationSignerFromDomainRequestTypeDef",
    "DisassociateDelegationSignerFromDomainResponseTypeDef",
    "DnssecKeyTypeDef",
    "DnssecSigningAttributesTypeDef",
    "DomainPriceTypeDef",
    "DomainSuggestionTypeDef",
    "DomainSummaryTypeDef",
    "DomainTransferabilityTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnableDomainAutoRenewRequestTypeDef",
    "EnableDomainTransferLockRequestTypeDef",
    "EnableDomainTransferLockResponseTypeDef",
    "ExtraParamTypeDef",
    "FilterConditionTypeDef",
    "GetContactReachabilityStatusRequestTypeDef",
    "GetContactReachabilityStatusResponseTypeDef",
    "GetDomainDetailRequestTypeDef",
    "GetDomainDetailResponseTypeDef",
    "GetDomainSuggestionsRequestTypeDef",
    "GetDomainSuggestionsResponseTypeDef",
    "GetOperationDetailRequestTypeDef",
    "GetOperationDetailResponseTypeDef",
    "ListDomainsRequestPaginateTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListOperationsRequestPaginateTypeDef",
    "ListOperationsRequestTypeDef",
    "ListOperationsResponseTypeDef",
    "ListPricesRequestPaginateTypeDef",
    "ListPricesRequestTypeDef",
    "ListPricesResponseTypeDef",
    "ListTagsForDomainRequestTypeDef",
    "ListTagsForDomainResponseTypeDef",
    "NameserverOutputTypeDef",
    "NameserverTypeDef",
    "NameserverUnionTypeDef",
    "OperationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PriceWithCurrencyTypeDef",
    "PushDomainRequestTypeDef",
    "RegisterDomainRequestTypeDef",
    "RegisterDomainResponseTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountRequestTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "RenewDomainRequestTypeDef",
    "RenewDomainResponseTypeDef",
    "ResendContactReachabilityEmailRequestTypeDef",
    "ResendContactReachabilityEmailResponseTypeDef",
    "ResendOperationAuthorizationRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveDomainAuthCodeRequestTypeDef",
    "RetrieveDomainAuthCodeResponseTypeDef",
    "SortConditionTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "TransferDomainRequestTypeDef",
    "TransferDomainResponseTypeDef",
    "TransferDomainToAnotherAwsAccountRequestTypeDef",
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    "UpdateDomainContactPrivacyRequestTypeDef",
    "UpdateDomainContactPrivacyResponseTypeDef",
    "UpdateDomainContactRequestTypeDef",
    "UpdateDomainContactResponseTypeDef",
    "UpdateDomainNameserversRequestTypeDef",
    "UpdateDomainNameserversResponseTypeDef",
    "UpdateTagsForDomainRequestTypeDef",
    "ViewBillingRequestPaginateTypeDef",
    "ViewBillingRequestTypeDef",
    "ViewBillingResponseTypeDef",
)

class AcceptDomainTransferFromAnotherAwsAccountRequestTypeDef(TypedDict):
    DomainName: str
    Password: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DnssecSigningAttributesTypeDef(TypedDict):
    Algorithm: NotRequired[int]
    Flags: NotRequired[int]
    PublicKey: NotRequired[str]

class BillingRecordTypeDef(TypedDict):
    DomainName: NotRequired[str]
    Operation: NotRequired[OperationTypeType]
    InvoiceId: NotRequired[str]
    BillDate: NotRequired[datetime]
    Price: NotRequired[float]

class CancelDomainTransferToAnotherAwsAccountRequestTypeDef(TypedDict):
    DomainName: str

class CheckDomainAvailabilityRequestTypeDef(TypedDict):
    DomainName: str
    IdnLangCode: NotRequired[str]

class CheckDomainTransferabilityRequestTypeDef(TypedDict):
    DomainName: str
    AuthCode: NotRequired[str]

class DomainTransferabilityTypeDef(TypedDict):
    Transferable: NotRequired[TransferableType]

class ConsentTypeDef(TypedDict):
    MaxPrice: float
    Currency: str

class ExtraParamTypeDef(TypedDict):
    Name: ExtraParamNameType
    Value: str

class DeleteDomainRequestTypeDef(TypedDict):
    DomainName: str

class DeleteTagsForDomainRequestTypeDef(TypedDict):
    DomainName: str
    TagsToDelete: Sequence[str]

class DisableDomainAutoRenewRequestTypeDef(TypedDict):
    DomainName: str

class DisableDomainTransferLockRequestTypeDef(TypedDict):
    DomainName: str

class DisassociateDelegationSignerFromDomainRequestTypeDef(TypedDict):
    DomainName: str
    Id: str

class DnssecKeyTypeDef(TypedDict):
    Algorithm: NotRequired[int]
    Flags: NotRequired[int]
    PublicKey: NotRequired[str]
    DigestType: NotRequired[int]
    Digest: NotRequired[str]
    KeyTag: NotRequired[int]
    Id: NotRequired[str]

class PriceWithCurrencyTypeDef(TypedDict):
    Price: float
    Currency: str

class DomainSuggestionTypeDef(TypedDict):
    DomainName: NotRequired[str]
    Availability: NotRequired[str]

class DomainSummaryTypeDef(TypedDict):
    DomainName: NotRequired[str]
    AutoRenew: NotRequired[bool]
    TransferLock: NotRequired[bool]
    Expiry: NotRequired[datetime]

class EnableDomainAutoRenewRequestTypeDef(TypedDict):
    DomainName: str

class EnableDomainTransferLockRequestTypeDef(TypedDict):
    DomainName: str

class FilterConditionTypeDef(TypedDict):
    Name: ListDomainsAttributeNameType
    Operator: OperatorType
    Values: Sequence[str]

class GetContactReachabilityStatusRequestTypeDef(TypedDict):
    domainName: NotRequired[str]

class GetDomainDetailRequestTypeDef(TypedDict):
    DomainName: str

class NameserverOutputTypeDef(TypedDict):
    Name: str
    GlueIps: NotRequired[List[str]]

class GetDomainSuggestionsRequestTypeDef(TypedDict):
    DomainName: str
    SuggestionCount: int
    OnlyAvailable: bool

class GetOperationDetailRequestTypeDef(TypedDict):
    OperationId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class SortConditionTypeDef(TypedDict):
    Name: ListDomainsAttributeNameType
    SortOrder: SortOrderType

TimestampTypeDef = Union[datetime, str]
OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "OperationId": NotRequired[str],
        "Status": NotRequired[OperationStatusType],
        "Type": NotRequired[OperationTypeType],
        "SubmittedDate": NotRequired[datetime],
        "DomainName": NotRequired[str],
        "Message": NotRequired[str],
        "StatusFlag": NotRequired[StatusFlagType],
        "LastUpdatedDate": NotRequired[datetime],
    },
)

class ListPricesRequestTypeDef(TypedDict):
    Tld: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListTagsForDomainRequestTypeDef(TypedDict):
    DomainName: str

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class NameserverTypeDef(TypedDict):
    Name: str
    GlueIps: NotRequired[Sequence[str]]

class PushDomainRequestTypeDef(TypedDict):
    DomainName: str
    Target: str

class RejectDomainTransferFromAnotherAwsAccountRequestTypeDef(TypedDict):
    DomainName: str

class RenewDomainRequestTypeDef(TypedDict):
    DomainName: str
    CurrentExpiryYear: int
    DurationInYears: NotRequired[int]

class ResendContactReachabilityEmailRequestTypeDef(TypedDict):
    domainName: NotRequired[str]

class ResendOperationAuthorizationRequestTypeDef(TypedDict):
    OperationId: str

class RetrieveDomainAuthCodeRequestTypeDef(TypedDict):
    DomainName: str

class TransferDomainToAnotherAwsAccountRequestTypeDef(TypedDict):
    DomainName: str
    AccountId: str

class UpdateDomainContactPrivacyRequestTypeDef(TypedDict):
    DomainName: str
    AdminPrivacy: NotRequired[bool]
    RegistrantPrivacy: NotRequired[bool]
    TechPrivacy: NotRequired[bool]
    BillingPrivacy: NotRequired[bool]

class AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDelegationSignerToDomainResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelDomainTransferToAnotherAwsAccountResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckDomainAvailabilityResponseTypeDef(TypedDict):
    Availability: DomainAvailabilityType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableDomainTransferLockResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateDelegationSignerFromDomainResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableDomainTransferLockResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactReachabilityStatusResponseTypeDef(TypedDict):
    domainName: str
    status: ReachabilityStatusType
    ResponseMetadata: ResponseMetadataTypeDef

GetOperationDetailResponseTypeDef = TypedDict(
    "GetOperationDetailResponseTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatusType,
        "Message": str,
        "DomainName": str,
        "Type": OperationTypeType,
        "SubmittedDate": datetime,
        "LastUpdatedDate": datetime,
        "StatusFlag": StatusFlagType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class RegisterDomainResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectDomainTransferFromAnotherAwsAccountResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RenewDomainResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResendContactReachabilityEmailResponseTypeDef(TypedDict):
    domainName: str
    emailAddress: str
    isAlreadyVerified: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RetrieveDomainAuthCodeResponseTypeDef(TypedDict):
    AuthCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferDomainResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferDomainToAnotherAwsAccountResponseTypeDef(TypedDict):
    OperationId: str
    Password: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainContactPrivacyResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainContactResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameserversResponseTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateDelegationSignerToDomainRequestTypeDef(TypedDict):
    DomainName: str
    SigningAttributes: DnssecSigningAttributesTypeDef

class ViewBillingResponseTypeDef(TypedDict):
    NextPageMarker: str
    BillingRecords: List[BillingRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CheckDomainTransferabilityResponseTypeDef(TypedDict):
    Transferability: DomainTransferabilityTypeDef
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContactDetailOutputTypeDef(TypedDict):
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    ContactType: NotRequired[ContactTypeType]
    OrganizationName: NotRequired[str]
    AddressLine1: NotRequired[str]
    AddressLine2: NotRequired[str]
    City: NotRequired[str]
    State: NotRequired[str]
    CountryCode: NotRequired[CountryCodeType]
    ZipCode: NotRequired[str]
    PhoneNumber: NotRequired[str]
    Email: NotRequired[str]
    Fax: NotRequired[str]
    ExtraParams: NotRequired[List[ExtraParamTypeDef]]

class ContactDetailTypeDef(TypedDict):
    FirstName: NotRequired[str]
    LastName: NotRequired[str]
    ContactType: NotRequired[ContactTypeType]
    OrganizationName: NotRequired[str]
    AddressLine1: NotRequired[str]
    AddressLine2: NotRequired[str]
    City: NotRequired[str]
    State: NotRequired[str]
    CountryCode: NotRequired[CountryCodeType]
    ZipCode: NotRequired[str]
    PhoneNumber: NotRequired[str]
    Email: NotRequired[str]
    Fax: NotRequired[str]
    ExtraParams: NotRequired[Sequence[ExtraParamTypeDef]]

class DomainPriceTypeDef(TypedDict):
    Name: NotRequired[str]
    RegistrationPrice: NotRequired[PriceWithCurrencyTypeDef]
    TransferPrice: NotRequired[PriceWithCurrencyTypeDef]
    RenewalPrice: NotRequired[PriceWithCurrencyTypeDef]
    ChangeOwnershipPrice: NotRequired[PriceWithCurrencyTypeDef]
    RestorationPrice: NotRequired[PriceWithCurrencyTypeDef]

class GetDomainSuggestionsResponseTypeDef(TypedDict):
    SuggestionsList: List[DomainSuggestionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResponseTypeDef(TypedDict):
    Domains: List[DomainSummaryTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPricesRequestPaginateTypeDef(TypedDict):
    Tld: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainsRequestPaginateTypeDef(TypedDict):
    FilterConditions: NotRequired[Sequence[FilterConditionTypeDef]]
    SortCondition: NotRequired[SortConditionTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainsRequestTypeDef(TypedDict):
    FilterConditions: NotRequired[Sequence[FilterConditionTypeDef]]
    SortCondition: NotRequired[SortConditionTypeDef]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

ListOperationsRequestPaginateTypeDef = TypedDict(
    "ListOperationsRequestPaginateTypeDef",
    {
        "SubmittedSince": NotRequired[TimestampTypeDef],
        "Status": NotRequired[Sequence[OperationStatusType]],
        "Type": NotRequired[Sequence[OperationTypeType]],
        "SortBy": NotRequired[Literal["SubmittedDate"]],
        "SortOrder": NotRequired[SortOrderType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOperationsRequestTypeDef = TypedDict(
    "ListOperationsRequestTypeDef",
    {
        "SubmittedSince": NotRequired[TimestampTypeDef],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
        "Status": NotRequired[Sequence[OperationStatusType]],
        "Type": NotRequired[Sequence[OperationTypeType]],
        "SortBy": NotRequired[Literal["SubmittedDate"]],
        "SortOrder": NotRequired[SortOrderType],
    },
)

class ViewBillingRequestPaginateTypeDef(TypedDict):
    Start: NotRequired[TimestampTypeDef]
    End: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ViewBillingRequestTypeDef(TypedDict):
    Start: NotRequired[TimestampTypeDef]
    End: NotRequired[TimestampTypeDef]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListOperationsResponseTypeDef(TypedDict):
    Operations: List[OperationSummaryTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForDomainResponseTypeDef(TypedDict):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTagsForDomainRequestTypeDef(TypedDict):
    DomainName: str
    TagsToUpdate: NotRequired[Sequence[TagTypeDef]]

NameserverUnionTypeDef = Union[NameserverTypeDef, NameserverOutputTypeDef]

class GetDomainDetailResponseTypeDef(TypedDict):
    DomainName: str
    Nameservers: List[NameserverOutputTypeDef]
    AutoRenew: bool
    AdminContact: ContactDetailOutputTypeDef
    RegistrantContact: ContactDetailOutputTypeDef
    TechContact: ContactDetailOutputTypeDef
    AdminPrivacy: bool
    RegistrantPrivacy: bool
    TechPrivacy: bool
    RegistrarName: str
    WhoIsServer: str
    RegistrarUrl: str
    AbuseContactEmail: str
    AbuseContactPhone: str
    RegistryDomainId: str
    CreationDate: datetime
    UpdatedDate: datetime
    ExpirationDate: datetime
    Reseller: str
    DnsSec: str
    StatusList: List[str]
    DnssecKeys: List[DnssecKeyTypeDef]
    BillingContact: ContactDetailOutputTypeDef
    BillingPrivacy: bool
    ResponseMetadata: ResponseMetadataTypeDef

ContactDetailUnionTypeDef = Union[ContactDetailTypeDef, ContactDetailOutputTypeDef]

class ListPricesResponseTypeDef(TypedDict):
    Prices: List[DomainPriceTypeDef]
    NextPageMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainNameserversRequestTypeDef(TypedDict):
    DomainName: str
    Nameservers: Sequence[NameserverUnionTypeDef]
    FIAuthKey: NotRequired[str]

class RegisterDomainRequestTypeDef(TypedDict):
    DomainName: str
    DurationInYears: int
    AdminContact: ContactDetailUnionTypeDef
    RegistrantContact: ContactDetailUnionTypeDef
    TechContact: ContactDetailUnionTypeDef
    IdnLangCode: NotRequired[str]
    AutoRenew: NotRequired[bool]
    PrivacyProtectAdminContact: NotRequired[bool]
    PrivacyProtectRegistrantContact: NotRequired[bool]
    PrivacyProtectTechContact: NotRequired[bool]
    BillingContact: NotRequired[ContactDetailUnionTypeDef]
    PrivacyProtectBillingContact: NotRequired[bool]

class TransferDomainRequestTypeDef(TypedDict):
    DomainName: str
    DurationInYears: int
    AdminContact: ContactDetailUnionTypeDef
    RegistrantContact: ContactDetailUnionTypeDef
    TechContact: ContactDetailUnionTypeDef
    IdnLangCode: NotRequired[str]
    Nameservers: NotRequired[Sequence[NameserverUnionTypeDef]]
    AuthCode: NotRequired[str]
    AutoRenew: NotRequired[bool]
    PrivacyProtectAdminContact: NotRequired[bool]
    PrivacyProtectRegistrantContact: NotRequired[bool]
    PrivacyProtectTechContact: NotRequired[bool]
    BillingContact: NotRequired[ContactDetailUnionTypeDef]
    PrivacyProtectBillingContact: NotRequired[bool]

class UpdateDomainContactRequestTypeDef(TypedDict):
    DomainName: str
    AdminContact: NotRequired[ContactDetailUnionTypeDef]
    RegistrantContact: NotRequired[ContactDetailUnionTypeDef]
    TechContact: NotRequired[ContactDetailUnionTypeDef]
    Consent: NotRequired[ConsentTypeDef]
    BillingContact: NotRequired[ContactDetailUnionTypeDef]
