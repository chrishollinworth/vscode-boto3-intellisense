"""
Type annotations for taxsettings service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/type_defs.html)

Usage::

    ```python
    from mypy_boto3_taxsettings.type_defs import AccountDetailsTypeDef

    data: AccountDetailsTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

from .literals import (
    AddressRoleTypeType,
    IndustriesType,
    IsraelCustomerTypeType,
    IsraelDealerTypeType,
    MalaysiaServiceTaxCodeType,
    PersonTypeType,
    RegistrationTypeType,
    SaudiArabiaTaxRegistrationNumberTypeType,
    SectorType,
    TaxRegistrationNumberTypeType,
    TaxRegistrationStatusType,
    TaxRegistrationTypeType,
    UkraineTrnTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountDetailsTypeDef",
    "AccountMetaDataTypeDef",
    "AdditionalInfoRequestTypeDef",
    "AdditionalInfoResponseTypeDef",
    "AddressTypeDef",
    "BatchDeleteTaxRegistrationErrorTypeDef",
    "BatchDeleteTaxRegistrationRequestRequestTypeDef",
    "BatchDeleteTaxRegistrationResponseTypeDef",
    "BatchPutTaxRegistrationErrorTypeDef",
    "BatchPutTaxRegistrationRequestRequestTypeDef",
    "BatchPutTaxRegistrationResponseTypeDef",
    "BrazilAdditionalInfoTypeDef",
    "CanadaAdditionalInfoTypeDef",
    "DeleteTaxRegistrationRequestRequestTypeDef",
    "DestinationS3LocationTypeDef",
    "EstoniaAdditionalInfoTypeDef",
    "GeorgiaAdditionalInfoTypeDef",
    "GetTaxRegistrationDocumentRequestRequestTypeDef",
    "GetTaxRegistrationDocumentResponseTypeDef",
    "GetTaxRegistrationRequestRequestTypeDef",
    "GetTaxRegistrationResponseTypeDef",
    "IndiaAdditionalInfoTypeDef",
    "IsraelAdditionalInfoTypeDef",
    "ItalyAdditionalInfoTypeDef",
    "JurisdictionTypeDef",
    "KenyaAdditionalInfoTypeDef",
    "ListTaxRegistrationsRequestRequestTypeDef",
    "ListTaxRegistrationsResponseTypeDef",
    "MalaysiaAdditionalInfoTypeDef",
    "PaginatorConfigTypeDef",
    "PolandAdditionalInfoTypeDef",
    "PutTaxRegistrationRequestRequestTypeDef",
    "PutTaxRegistrationResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RomaniaAdditionalInfoTypeDef",
    "SaudiArabiaAdditionalInfoTypeDef",
    "SourceS3LocationTypeDef",
    "SouthKoreaAdditionalInfoTypeDef",
    "SpainAdditionalInfoTypeDef",
    "TaxDocumentMetadataTypeDef",
    "TaxInheritanceDetailsTypeDef",
    "TaxRegistrationDocumentTypeDef",
    "TaxRegistrationEntryTypeDef",
    "TaxRegistrationTypeDef",
    "TaxRegistrationWithJurisdictionTypeDef",
    "TurkeyAdditionalInfoTypeDef",
    "UkraineAdditionalInfoTypeDef",
    "VerificationDetailsTypeDef",
)

AccountDetailsTypeDef = TypedDict(
    "AccountDetailsTypeDef",
    {
        "accountId": str,
        "accountMetaData": "AccountMetaDataTypeDef",
        "taxInheritanceDetails": "TaxInheritanceDetailsTypeDef",
        "taxRegistration": "TaxRegistrationWithJurisdictionTypeDef",
    },
    total=False,
)

AccountMetaDataTypeDef = TypedDict(
    "AccountMetaDataTypeDef",
    {
        "accountName": str,
        "address": "AddressTypeDef",
        "addressRoleMap": Dict[AddressRoleTypeType, "JurisdictionTypeDef"],
        "addressType": AddressRoleTypeType,
        "seller": str,
    },
    total=False,
)

AdditionalInfoRequestTypeDef = TypedDict(
    "AdditionalInfoRequestTypeDef",
    {
        "canadaAdditionalInfo": "CanadaAdditionalInfoTypeDef",
        "estoniaAdditionalInfo": "EstoniaAdditionalInfoTypeDef",
        "georgiaAdditionalInfo": "GeorgiaAdditionalInfoTypeDef",
        "israelAdditionalInfo": "IsraelAdditionalInfoTypeDef",
        "italyAdditionalInfo": "ItalyAdditionalInfoTypeDef",
        "kenyaAdditionalInfo": "KenyaAdditionalInfoTypeDef",
        "malaysiaAdditionalInfo": "MalaysiaAdditionalInfoTypeDef",
        "polandAdditionalInfo": "PolandAdditionalInfoTypeDef",
        "romaniaAdditionalInfo": "RomaniaAdditionalInfoTypeDef",
        "saudiArabiaAdditionalInfo": "SaudiArabiaAdditionalInfoTypeDef",
        "southKoreaAdditionalInfo": "SouthKoreaAdditionalInfoTypeDef",
        "spainAdditionalInfo": "SpainAdditionalInfoTypeDef",
        "turkeyAdditionalInfo": "TurkeyAdditionalInfoTypeDef",
        "ukraineAdditionalInfo": "UkraineAdditionalInfoTypeDef",
    },
    total=False,
)

AdditionalInfoResponseTypeDef = TypedDict(
    "AdditionalInfoResponseTypeDef",
    {
        "brazilAdditionalInfo": "BrazilAdditionalInfoTypeDef",
        "canadaAdditionalInfo": "CanadaAdditionalInfoTypeDef",
        "estoniaAdditionalInfo": "EstoniaAdditionalInfoTypeDef",
        "georgiaAdditionalInfo": "GeorgiaAdditionalInfoTypeDef",
        "indiaAdditionalInfo": "IndiaAdditionalInfoTypeDef",
        "israelAdditionalInfo": "IsraelAdditionalInfoTypeDef",
        "italyAdditionalInfo": "ItalyAdditionalInfoTypeDef",
        "kenyaAdditionalInfo": "KenyaAdditionalInfoTypeDef",
        "malaysiaAdditionalInfo": "MalaysiaAdditionalInfoTypeDef",
        "polandAdditionalInfo": "PolandAdditionalInfoTypeDef",
        "romaniaAdditionalInfo": "RomaniaAdditionalInfoTypeDef",
        "saudiArabiaAdditionalInfo": "SaudiArabiaAdditionalInfoTypeDef",
        "southKoreaAdditionalInfo": "SouthKoreaAdditionalInfoTypeDef",
        "spainAdditionalInfo": "SpainAdditionalInfoTypeDef",
        "turkeyAdditionalInfo": "TurkeyAdditionalInfoTypeDef",
        "ukraineAdditionalInfo": "UkraineAdditionalInfoTypeDef",
    },
    total=False,
)

_RequiredAddressTypeDef = TypedDict(
    "_RequiredAddressTypeDef",
    {
        "addressLine1": str,
        "city": str,
        "countryCode": str,
        "postalCode": str,
    },
)
_OptionalAddressTypeDef = TypedDict(
    "_OptionalAddressTypeDef",
    {
        "addressLine2": str,
        "addressLine3": str,
        "districtOrCounty": str,
        "stateOrRegion": str,
    },
    total=False,
)

class AddressTypeDef(_RequiredAddressTypeDef, _OptionalAddressTypeDef):
    pass

_RequiredBatchDeleteTaxRegistrationErrorTypeDef = TypedDict(
    "_RequiredBatchDeleteTaxRegistrationErrorTypeDef",
    {
        "accountId": str,
        "message": str,
    },
)
_OptionalBatchDeleteTaxRegistrationErrorTypeDef = TypedDict(
    "_OptionalBatchDeleteTaxRegistrationErrorTypeDef",
    {
        "code": str,
    },
    total=False,
)

class BatchDeleteTaxRegistrationErrorTypeDef(
    _RequiredBatchDeleteTaxRegistrationErrorTypeDef, _OptionalBatchDeleteTaxRegistrationErrorTypeDef
):
    pass

BatchDeleteTaxRegistrationRequestRequestTypeDef = TypedDict(
    "BatchDeleteTaxRegistrationRequestRequestTypeDef",
    {
        "accountIds": List[str],
    },
)

BatchDeleteTaxRegistrationResponseTypeDef = TypedDict(
    "BatchDeleteTaxRegistrationResponseTypeDef",
    {
        "errors": List["BatchDeleteTaxRegistrationErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchPutTaxRegistrationErrorTypeDef = TypedDict(
    "_RequiredBatchPutTaxRegistrationErrorTypeDef",
    {
        "accountId": str,
        "message": str,
    },
)
_OptionalBatchPutTaxRegistrationErrorTypeDef = TypedDict(
    "_OptionalBatchPutTaxRegistrationErrorTypeDef",
    {
        "code": str,
    },
    total=False,
)

class BatchPutTaxRegistrationErrorTypeDef(
    _RequiredBatchPutTaxRegistrationErrorTypeDef, _OptionalBatchPutTaxRegistrationErrorTypeDef
):
    pass

BatchPutTaxRegistrationRequestRequestTypeDef = TypedDict(
    "BatchPutTaxRegistrationRequestRequestTypeDef",
    {
        "accountIds": List[str],
        "taxRegistrationEntry": "TaxRegistrationEntryTypeDef",
    },
)

BatchPutTaxRegistrationResponseTypeDef = TypedDict(
    "BatchPutTaxRegistrationResponseTypeDef",
    {
        "errors": List["BatchPutTaxRegistrationErrorTypeDef"],
        "status": TaxRegistrationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BrazilAdditionalInfoTypeDef = TypedDict(
    "BrazilAdditionalInfoTypeDef",
    {
        "ccmCode": str,
        "legalNatureCode": str,
    },
    total=False,
)

CanadaAdditionalInfoTypeDef = TypedDict(
    "CanadaAdditionalInfoTypeDef",
    {
        "canadaQuebecSalesTaxNumber": str,
        "canadaRetailSalesTaxNumber": str,
        "isResellerAccount": bool,
        "provincialSalesTaxId": str,
    },
    total=False,
)

DeleteTaxRegistrationRequestRequestTypeDef = TypedDict(
    "DeleteTaxRegistrationRequestRequestTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

_RequiredDestinationS3LocationTypeDef = TypedDict(
    "_RequiredDestinationS3LocationTypeDef",
    {
        "bucket": str,
    },
)
_OptionalDestinationS3LocationTypeDef = TypedDict(
    "_OptionalDestinationS3LocationTypeDef",
    {
        "prefix": str,
    },
    total=False,
)

class DestinationS3LocationTypeDef(
    _RequiredDestinationS3LocationTypeDef, _OptionalDestinationS3LocationTypeDef
):
    pass

EstoniaAdditionalInfoTypeDef = TypedDict(
    "EstoniaAdditionalInfoTypeDef",
    {
        "registryCommercialCode": str,
    },
)

GeorgiaAdditionalInfoTypeDef = TypedDict(
    "GeorgiaAdditionalInfoTypeDef",
    {
        "personType": PersonTypeType,
    },
)

GetTaxRegistrationDocumentRequestRequestTypeDef = TypedDict(
    "GetTaxRegistrationDocumentRequestRequestTypeDef",
    {
        "destinationS3Location": "DestinationS3LocationTypeDef",
        "taxDocumentMetadata": "TaxDocumentMetadataTypeDef",
    },
)

GetTaxRegistrationDocumentResponseTypeDef = TypedDict(
    "GetTaxRegistrationDocumentResponseTypeDef",
    {
        "destinationFilePath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTaxRegistrationRequestRequestTypeDef = TypedDict(
    "GetTaxRegistrationRequestRequestTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

GetTaxRegistrationResponseTypeDef = TypedDict(
    "GetTaxRegistrationResponseTypeDef",
    {
        "taxRegistration": "TaxRegistrationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IndiaAdditionalInfoTypeDef = TypedDict(
    "IndiaAdditionalInfoTypeDef",
    {
        "pan": str,
    },
    total=False,
)

IsraelAdditionalInfoTypeDef = TypedDict(
    "IsraelAdditionalInfoTypeDef",
    {
        "customerType": IsraelCustomerTypeType,
        "dealerType": IsraelDealerTypeType,
    },
)

ItalyAdditionalInfoTypeDef = TypedDict(
    "ItalyAdditionalInfoTypeDef",
    {
        "cigNumber": str,
        "cupNumber": str,
        "sdiAccountId": str,
        "taxCode": str,
    },
    total=False,
)

_RequiredJurisdictionTypeDef = TypedDict(
    "_RequiredJurisdictionTypeDef",
    {
        "countryCode": str,
    },
)
_OptionalJurisdictionTypeDef = TypedDict(
    "_OptionalJurisdictionTypeDef",
    {
        "stateOrRegion": str,
    },
    total=False,
)

class JurisdictionTypeDef(_RequiredJurisdictionTypeDef, _OptionalJurisdictionTypeDef):
    pass

KenyaAdditionalInfoTypeDef = TypedDict(
    "KenyaAdditionalInfoTypeDef",
    {
        "personType": PersonTypeType,
    },
)

ListTaxRegistrationsRequestRequestTypeDef = TypedDict(
    "ListTaxRegistrationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTaxRegistrationsResponseTypeDef = TypedDict(
    "ListTaxRegistrationsResponseTypeDef",
    {
        "accountDetails": List["AccountDetailsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MalaysiaAdditionalInfoTypeDef = TypedDict(
    "MalaysiaAdditionalInfoTypeDef",
    {
        "serviceTaxCodes": List[MalaysiaServiceTaxCodeType],
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

PolandAdditionalInfoTypeDef = TypedDict(
    "PolandAdditionalInfoTypeDef",
    {
        "individualRegistrationNumber": str,
        "isGroupVatEnabled": bool,
    },
    total=False,
)

_RequiredPutTaxRegistrationRequestRequestTypeDef = TypedDict(
    "_RequiredPutTaxRegistrationRequestRequestTypeDef",
    {
        "taxRegistrationEntry": "TaxRegistrationEntryTypeDef",
    },
)
_OptionalPutTaxRegistrationRequestRequestTypeDef = TypedDict(
    "_OptionalPutTaxRegistrationRequestRequestTypeDef",
    {
        "accountId": str,
    },
    total=False,
)

class PutTaxRegistrationRequestRequestTypeDef(
    _RequiredPutTaxRegistrationRequestRequestTypeDef,
    _OptionalPutTaxRegistrationRequestRequestTypeDef,
):
    pass

PutTaxRegistrationResponseTypeDef = TypedDict(
    "PutTaxRegistrationResponseTypeDef",
    {
        "status": TaxRegistrationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RomaniaAdditionalInfoTypeDef = TypedDict(
    "RomaniaAdditionalInfoTypeDef",
    {
        "taxRegistrationNumberType": TaxRegistrationNumberTypeType,
    },
)

SaudiArabiaAdditionalInfoTypeDef = TypedDict(
    "SaudiArabiaAdditionalInfoTypeDef",
    {
        "taxRegistrationNumberType": SaudiArabiaTaxRegistrationNumberTypeType,
    },
    total=False,
)

SourceS3LocationTypeDef = TypedDict(
    "SourceS3LocationTypeDef",
    {
        "bucket": str,
        "key": str,
    },
)

SouthKoreaAdditionalInfoTypeDef = TypedDict(
    "SouthKoreaAdditionalInfoTypeDef",
    {
        "businessRepresentativeName": str,
        "itemOfBusiness": str,
        "lineOfBusiness": str,
    },
)

SpainAdditionalInfoTypeDef = TypedDict(
    "SpainAdditionalInfoTypeDef",
    {
        "registrationType": RegistrationTypeType,
    },
)

TaxDocumentMetadataTypeDef = TypedDict(
    "TaxDocumentMetadataTypeDef",
    {
        "taxDocumentAccessToken": str,
        "taxDocumentName": str,
    },
)

TaxInheritanceDetailsTypeDef = TypedDict(
    "TaxInheritanceDetailsTypeDef",
    {
        "inheritanceObtainedReason": str,
        "parentEntityId": str,
    },
    total=False,
)

TaxRegistrationDocumentTypeDef = TypedDict(
    "TaxRegistrationDocumentTypeDef",
    {
        "s3Location": "SourceS3LocationTypeDef",
    },
)

_RequiredTaxRegistrationEntryTypeDef = TypedDict(
    "_RequiredTaxRegistrationEntryTypeDef",
    {
        "registrationId": str,
        "registrationType": TaxRegistrationTypeType,
    },
)
_OptionalTaxRegistrationEntryTypeDef = TypedDict(
    "_OptionalTaxRegistrationEntryTypeDef",
    {
        "additionalTaxInformation": "AdditionalInfoRequestTypeDef",
        "certifiedEmailId": str,
        "legalAddress": "AddressTypeDef",
        "legalName": str,
        "sector": SectorType,
        "verificationDetails": "VerificationDetailsTypeDef",
    },
    total=False,
)

class TaxRegistrationEntryTypeDef(
    _RequiredTaxRegistrationEntryTypeDef, _OptionalTaxRegistrationEntryTypeDef
):
    pass

_RequiredTaxRegistrationTypeDef = TypedDict(
    "_RequiredTaxRegistrationTypeDef",
    {
        "legalAddress": "AddressTypeDef",
        "legalName": str,
        "registrationId": str,
        "registrationType": TaxRegistrationTypeType,
        "status": TaxRegistrationStatusType,
    },
)
_OptionalTaxRegistrationTypeDef = TypedDict(
    "_OptionalTaxRegistrationTypeDef",
    {
        "additionalTaxInformation": "AdditionalInfoResponseTypeDef",
        "certifiedEmailId": str,
        "sector": SectorType,
        "taxDocumentMetadatas": List["TaxDocumentMetadataTypeDef"],
    },
    total=False,
)

class TaxRegistrationTypeDef(_RequiredTaxRegistrationTypeDef, _OptionalTaxRegistrationTypeDef):
    pass

_RequiredTaxRegistrationWithJurisdictionTypeDef = TypedDict(
    "_RequiredTaxRegistrationWithJurisdictionTypeDef",
    {
        "jurisdiction": "JurisdictionTypeDef",
        "legalName": str,
        "registrationId": str,
        "registrationType": TaxRegistrationTypeType,
        "status": TaxRegistrationStatusType,
    },
)
_OptionalTaxRegistrationWithJurisdictionTypeDef = TypedDict(
    "_OptionalTaxRegistrationWithJurisdictionTypeDef",
    {
        "additionalTaxInformation": "AdditionalInfoResponseTypeDef",
        "certifiedEmailId": str,
        "sector": SectorType,
        "taxDocumentMetadatas": List["TaxDocumentMetadataTypeDef"],
    },
    total=False,
)

class TaxRegistrationWithJurisdictionTypeDef(
    _RequiredTaxRegistrationWithJurisdictionTypeDef, _OptionalTaxRegistrationWithJurisdictionTypeDef
):
    pass

TurkeyAdditionalInfoTypeDef = TypedDict(
    "TurkeyAdditionalInfoTypeDef",
    {
        "industries": IndustriesType,
        "kepEmailId": str,
        "secondaryTaxId": str,
        "taxOffice": str,
    },
    total=False,
)

UkraineAdditionalInfoTypeDef = TypedDict(
    "UkraineAdditionalInfoTypeDef",
    {
        "ukraineTrnType": UkraineTrnTypeType,
    },
)

VerificationDetailsTypeDef = TypedDict(
    "VerificationDetailsTypeDef",
    {
        "dateOfBirth": str,
        "taxRegistrationDocuments": List["TaxRegistrationDocumentTypeDef"],
    },
    total=False,
)
