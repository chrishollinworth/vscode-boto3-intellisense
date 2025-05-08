"""
Type annotations for taxsettings service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_taxsettings/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_taxsettings.type_defs import TaxInheritanceDetailsTypeDef

    data: TaxInheritanceDetailsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AddressRoleTypeType,
    EntityExemptionAccountStatusType,
    HeritageStatusType,
    IndonesiaTaxRegistrationNumberTypeType,
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
    UzbekistanTaxRegistrationNumberTypeType,
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
    "AccountDetailsTypeDef",
    "AccountMetaDataTypeDef",
    "AdditionalInfoRequestTypeDef",
    "AdditionalInfoResponseTypeDef",
    "AddressTypeDef",
    "AuthorityTypeDef",
    "BatchDeleteTaxRegistrationErrorTypeDef",
    "BatchDeleteTaxRegistrationRequestTypeDef",
    "BatchDeleteTaxRegistrationResponseTypeDef",
    "BatchGetTaxExemptionsRequestTypeDef",
    "BatchGetTaxExemptionsResponseTypeDef",
    "BatchPutTaxRegistrationErrorTypeDef",
    "BatchPutTaxRegistrationRequestTypeDef",
    "BatchPutTaxRegistrationResponseTypeDef",
    "BlobTypeDef",
    "BrazilAdditionalInfoTypeDef",
    "CanadaAdditionalInfoTypeDef",
    "DeleteSupplementalTaxRegistrationRequestTypeDef",
    "DeleteTaxRegistrationRequestTypeDef",
    "DestinationS3LocationTypeDef",
    "EgyptAdditionalInfoTypeDef",
    "EstoniaAdditionalInfoTypeDef",
    "ExemptionCertificateTypeDef",
    "GeorgiaAdditionalInfoTypeDef",
    "GetTaxExemptionTypesResponseTypeDef",
    "GetTaxInheritanceResponseTypeDef",
    "GetTaxRegistrationDocumentRequestTypeDef",
    "GetTaxRegistrationDocumentResponseTypeDef",
    "GetTaxRegistrationRequestTypeDef",
    "GetTaxRegistrationResponseTypeDef",
    "GreeceAdditionalInfoTypeDef",
    "IndiaAdditionalInfoTypeDef",
    "IndonesiaAdditionalInfoTypeDef",
    "IsraelAdditionalInfoTypeDef",
    "ItalyAdditionalInfoTypeDef",
    "JurisdictionTypeDef",
    "KenyaAdditionalInfoTypeDef",
    "ListSupplementalTaxRegistrationsRequestPaginateTypeDef",
    "ListSupplementalTaxRegistrationsRequestTypeDef",
    "ListSupplementalTaxRegistrationsResponseTypeDef",
    "ListTaxExemptionsRequestPaginateTypeDef",
    "ListTaxExemptionsRequestTypeDef",
    "ListTaxExemptionsResponseTypeDef",
    "ListTaxRegistrationsRequestPaginateTypeDef",
    "ListTaxRegistrationsRequestTypeDef",
    "ListTaxRegistrationsResponseTypeDef",
    "MalaysiaAdditionalInfoOutputTypeDef",
    "MalaysiaAdditionalInfoTypeDef",
    "MalaysiaAdditionalInfoUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PolandAdditionalInfoTypeDef",
    "PutSupplementalTaxRegistrationRequestTypeDef",
    "PutSupplementalTaxRegistrationResponseTypeDef",
    "PutTaxExemptionRequestTypeDef",
    "PutTaxExemptionResponseTypeDef",
    "PutTaxInheritanceRequestTypeDef",
    "PutTaxRegistrationRequestTypeDef",
    "PutTaxRegistrationResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RomaniaAdditionalInfoTypeDef",
    "SaudiArabiaAdditionalInfoTypeDef",
    "SourceS3LocationTypeDef",
    "SouthKoreaAdditionalInfoTypeDef",
    "SpainAdditionalInfoTypeDef",
    "SupplementalTaxRegistrationEntryTypeDef",
    "SupplementalTaxRegistrationTypeDef",
    "TaxDocumentMetadataTypeDef",
    "TaxExemptionDetailsTypeDef",
    "TaxExemptionTypeDef",
    "TaxExemptionTypeTypeDef",
    "TaxInheritanceDetailsTypeDef",
    "TaxRegistrationDocFileTypeDef",
    "TaxRegistrationDocumentTypeDef",
    "TaxRegistrationEntryTypeDef",
    "TaxRegistrationTypeDef",
    "TaxRegistrationWithJurisdictionTypeDef",
    "TurkeyAdditionalInfoTypeDef",
    "UkraineAdditionalInfoTypeDef",
    "UzbekistanAdditionalInfoTypeDef",
    "VerificationDetailsTypeDef",
    "VietnamAdditionalInfoTypeDef",
)

class TaxInheritanceDetailsTypeDef(TypedDict):
    inheritanceObtainedReason: NotRequired[str]
    parentEntityId: NotRequired[str]

class AddressTypeDef(TypedDict):
    addressLine1: str
    city: str
    countryCode: str
    postalCode: str
    addressLine2: NotRequired[str]
    addressLine3: NotRequired[str]
    districtOrCounty: NotRequired[str]
    stateOrRegion: NotRequired[str]

class JurisdictionTypeDef(TypedDict):
    countryCode: str
    stateOrRegion: NotRequired[str]

class CanadaAdditionalInfoTypeDef(TypedDict):
    canadaQuebecSalesTaxNumber: NotRequired[str]
    canadaRetailSalesTaxNumber: NotRequired[str]
    isResellerAccount: NotRequired[bool]
    provincialSalesTaxId: NotRequired[str]

class EgyptAdditionalInfoTypeDef(TypedDict):
    uniqueIdentificationNumber: NotRequired[str]
    uniqueIdentificationNumberExpirationDate: NotRequired[str]

class EstoniaAdditionalInfoTypeDef(TypedDict):
    registryCommercialCode: str

class GeorgiaAdditionalInfoTypeDef(TypedDict):
    personType: PersonTypeType

class GreeceAdditionalInfoTypeDef(TypedDict):
    contractingAuthorityCode: NotRequired[str]

class IndonesiaAdditionalInfoTypeDef(TypedDict):
    decisionNumber: NotRequired[str]
    ppnExceptionDesignationCode: NotRequired[str]
    taxRegistrationNumberType: NotRequired[IndonesiaTaxRegistrationNumberTypeType]

class IsraelAdditionalInfoTypeDef(TypedDict):
    customerType: IsraelCustomerTypeType
    dealerType: IsraelDealerTypeType

class ItalyAdditionalInfoTypeDef(TypedDict):
    cigNumber: NotRequired[str]
    cupNumber: NotRequired[str]
    sdiAccountId: NotRequired[str]
    taxCode: NotRequired[str]

class KenyaAdditionalInfoTypeDef(TypedDict):
    personType: PersonTypeType

class PolandAdditionalInfoTypeDef(TypedDict):
    individualRegistrationNumber: NotRequired[str]
    isGroupVatEnabled: NotRequired[bool]

class RomaniaAdditionalInfoTypeDef(TypedDict):
    taxRegistrationNumberType: TaxRegistrationNumberTypeType

class SaudiArabiaAdditionalInfoTypeDef(TypedDict):
    taxRegistrationNumberType: NotRequired[SaudiArabiaTaxRegistrationNumberTypeType]

class SouthKoreaAdditionalInfoTypeDef(TypedDict):
    businessRepresentativeName: str
    itemOfBusiness: str
    lineOfBusiness: str

class SpainAdditionalInfoTypeDef(TypedDict):
    registrationType: RegistrationTypeType

class TurkeyAdditionalInfoTypeDef(TypedDict):
    industries: NotRequired[IndustriesType]
    kepEmailId: NotRequired[str]
    secondaryTaxId: NotRequired[str]
    taxOffice: NotRequired[str]

class UkraineAdditionalInfoTypeDef(TypedDict):
    ukraineTrnType: UkraineTrnTypeType

class UzbekistanAdditionalInfoTypeDef(TypedDict):
    taxRegistrationNumberType: NotRequired[UzbekistanTaxRegistrationNumberTypeType]
    vatRegistrationNumber: NotRequired[str]

class VietnamAdditionalInfoTypeDef(TypedDict):
    electronicTransactionCodeNumber: NotRequired[str]
    enterpriseIdentificationNumber: NotRequired[str]
    paymentVoucherNumber: NotRequired[str]
    paymentVoucherNumberDate: NotRequired[str]

class BrazilAdditionalInfoTypeDef(TypedDict):
    ccmCode: NotRequired[str]
    legalNatureCode: NotRequired[str]

class IndiaAdditionalInfoTypeDef(TypedDict):
    pan: NotRequired[str]

class MalaysiaAdditionalInfoOutputTypeDef(TypedDict):
    businessRegistrationNumber: NotRequired[str]
    serviceTaxCodes: NotRequired[List[MalaysiaServiceTaxCodeType]]
    taxInformationNumber: NotRequired[str]

class AuthorityTypeDef(TypedDict):
    country: str
    state: NotRequired[str]

class BatchDeleteTaxRegistrationErrorTypeDef(TypedDict):
    accountId: str
    message: str
    code: NotRequired[str]

class BatchDeleteTaxRegistrationRequestTypeDef(TypedDict):
    accountIds: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class BatchGetTaxExemptionsRequestTypeDef(TypedDict):
    accountIds: Sequence[str]

class BatchPutTaxRegistrationErrorTypeDef(TypedDict):
    accountId: str
    message: str
    code: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class DeleteSupplementalTaxRegistrationRequestTypeDef(TypedDict):
    authorityId: str

class DeleteTaxRegistrationRequestTypeDef(TypedDict):
    accountId: NotRequired[str]

class DestinationS3LocationTypeDef(TypedDict):
    bucket: str
    prefix: NotRequired[str]

class TaxDocumentMetadataTypeDef(TypedDict):
    taxDocumentAccessToken: str
    taxDocumentName: str

class GetTaxRegistrationRequestTypeDef(TypedDict):
    accountId: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListSupplementalTaxRegistrationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTaxExemptionsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTaxRegistrationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class MalaysiaAdditionalInfoTypeDef(TypedDict):
    businessRegistrationNumber: NotRequired[str]
    serviceTaxCodes: NotRequired[Sequence[MalaysiaServiceTaxCodeType]]
    taxInformationNumber: NotRequired[str]

class PutTaxInheritanceRequestTypeDef(TypedDict):
    heritageStatus: NotRequired[HeritageStatusType]

class SourceS3LocationTypeDef(TypedDict):
    bucket: str
    key: str

class SupplementalTaxRegistrationEntryTypeDef(TypedDict):
    address: AddressTypeDef
    legalName: str
    registrationId: str
    registrationType: Literal["VAT"]

class SupplementalTaxRegistrationTypeDef(TypedDict):
    address: AddressTypeDef
    authorityId: str
    legalName: str
    registrationId: str
    registrationType: Literal["VAT"]
    status: TaxRegistrationStatusType

class AccountMetaDataTypeDef(TypedDict):
    accountName: NotRequired[str]
    address: NotRequired[AddressTypeDef]
    addressRoleMap: NotRequired[Dict[AddressRoleTypeType, JurisdictionTypeDef]]
    addressType: NotRequired[AddressRoleTypeType]
    seller: NotRequired[str]

class AdditionalInfoResponseTypeDef(TypedDict):
    brazilAdditionalInfo: NotRequired[BrazilAdditionalInfoTypeDef]
    canadaAdditionalInfo: NotRequired[CanadaAdditionalInfoTypeDef]
    egyptAdditionalInfo: NotRequired[EgyptAdditionalInfoTypeDef]
    estoniaAdditionalInfo: NotRequired[EstoniaAdditionalInfoTypeDef]
    georgiaAdditionalInfo: NotRequired[GeorgiaAdditionalInfoTypeDef]
    greeceAdditionalInfo: NotRequired[GreeceAdditionalInfoTypeDef]
    indiaAdditionalInfo: NotRequired[IndiaAdditionalInfoTypeDef]
    indonesiaAdditionalInfo: NotRequired[IndonesiaAdditionalInfoTypeDef]
    israelAdditionalInfo: NotRequired[IsraelAdditionalInfoTypeDef]
    italyAdditionalInfo: NotRequired[ItalyAdditionalInfoTypeDef]
    kenyaAdditionalInfo: NotRequired[KenyaAdditionalInfoTypeDef]
    malaysiaAdditionalInfo: NotRequired[MalaysiaAdditionalInfoOutputTypeDef]
    polandAdditionalInfo: NotRequired[PolandAdditionalInfoTypeDef]
    romaniaAdditionalInfo: NotRequired[RomaniaAdditionalInfoTypeDef]
    saudiArabiaAdditionalInfo: NotRequired[SaudiArabiaAdditionalInfoTypeDef]
    southKoreaAdditionalInfo: NotRequired[SouthKoreaAdditionalInfoTypeDef]
    spainAdditionalInfo: NotRequired[SpainAdditionalInfoTypeDef]
    turkeyAdditionalInfo: NotRequired[TurkeyAdditionalInfoTypeDef]
    ukraineAdditionalInfo: NotRequired[UkraineAdditionalInfoTypeDef]
    uzbekistanAdditionalInfo: NotRequired[UzbekistanAdditionalInfoTypeDef]
    vietnamAdditionalInfo: NotRequired[VietnamAdditionalInfoTypeDef]

class TaxExemptionTypeTypeDef(TypedDict):
    applicableJurisdictions: NotRequired[List[AuthorityTypeDef]]
    description: NotRequired[str]
    displayName: NotRequired[str]

class BatchDeleteTaxRegistrationResponseTypeDef(TypedDict):
    errors: List[BatchDeleteTaxRegistrationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaxInheritanceResponseTypeDef(TypedDict):
    heritageStatus: HeritageStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaxRegistrationDocumentResponseTypeDef(TypedDict):
    destinationFilePath: str
    presignedS3Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSupplementalTaxRegistrationResponseTypeDef(TypedDict):
    authorityId: str
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PutTaxExemptionResponseTypeDef(TypedDict):
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutTaxRegistrationResponseTypeDef(TypedDict):
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutTaxRegistrationResponseTypeDef(TypedDict):
    errors: List[BatchPutTaxRegistrationErrorTypeDef]
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ExemptionCertificateTypeDef(TypedDict):
    documentFile: BlobTypeDef
    documentName: str

class TaxRegistrationDocFileTypeDef(TypedDict):
    fileContent: BlobTypeDef
    fileName: str

class GetTaxRegistrationDocumentRequestTypeDef(TypedDict):
    taxDocumentMetadata: TaxDocumentMetadataTypeDef
    destinationS3Location: NotRequired[DestinationS3LocationTypeDef]

class ListSupplementalTaxRegistrationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTaxExemptionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTaxRegistrationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

MalaysiaAdditionalInfoUnionTypeDef = Union[
    MalaysiaAdditionalInfoTypeDef, MalaysiaAdditionalInfoOutputTypeDef
]

class PutSupplementalTaxRegistrationRequestTypeDef(TypedDict):
    taxRegistrationEntry: SupplementalTaxRegistrationEntryTypeDef

class ListSupplementalTaxRegistrationsResponseTypeDef(TypedDict):
    taxRegistrations: List[SupplementalTaxRegistrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TaxRegistrationTypeDef(TypedDict):
    legalAddress: AddressTypeDef
    legalName: str
    registrationId: str
    registrationType: TaxRegistrationTypeType
    status: TaxRegistrationStatusType
    additionalTaxInformation: NotRequired[AdditionalInfoResponseTypeDef]
    certifiedEmailId: NotRequired[str]
    sector: NotRequired[SectorType]
    taxDocumentMetadatas: NotRequired[List[TaxDocumentMetadataTypeDef]]

class TaxRegistrationWithJurisdictionTypeDef(TypedDict):
    jurisdiction: JurisdictionTypeDef
    legalName: str
    registrationId: str
    registrationType: TaxRegistrationTypeType
    status: TaxRegistrationStatusType
    additionalTaxInformation: NotRequired[AdditionalInfoResponseTypeDef]
    certifiedEmailId: NotRequired[str]
    sector: NotRequired[SectorType]
    taxDocumentMetadatas: NotRequired[List[TaxDocumentMetadataTypeDef]]

class GetTaxExemptionTypesResponseTypeDef(TypedDict):
    taxExemptionTypes: List[TaxExemptionTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TaxExemptionTypeDef(TypedDict):
    authority: AuthorityTypeDef
    taxExemptionType: TaxExemptionTypeTypeDef
    effectiveDate: NotRequired[datetime]
    expirationDate: NotRequired[datetime]
    status: NotRequired[EntityExemptionAccountStatusType]
    systemEffectiveDate: NotRequired[datetime]

class PutTaxExemptionRequestTypeDef(TypedDict):
    accountIds: Sequence[str]
    authority: AuthorityTypeDef
    exemptionCertificate: ExemptionCertificateTypeDef
    exemptionType: str

class TaxRegistrationDocumentTypeDef(TypedDict):
    file: NotRequired[TaxRegistrationDocFileTypeDef]
    s3Location: NotRequired[SourceS3LocationTypeDef]

class AdditionalInfoRequestTypeDef(TypedDict):
    canadaAdditionalInfo: NotRequired[CanadaAdditionalInfoTypeDef]
    egyptAdditionalInfo: NotRequired[EgyptAdditionalInfoTypeDef]
    estoniaAdditionalInfo: NotRequired[EstoniaAdditionalInfoTypeDef]
    georgiaAdditionalInfo: NotRequired[GeorgiaAdditionalInfoTypeDef]
    greeceAdditionalInfo: NotRequired[GreeceAdditionalInfoTypeDef]
    indonesiaAdditionalInfo: NotRequired[IndonesiaAdditionalInfoTypeDef]
    israelAdditionalInfo: NotRequired[IsraelAdditionalInfoTypeDef]
    italyAdditionalInfo: NotRequired[ItalyAdditionalInfoTypeDef]
    kenyaAdditionalInfo: NotRequired[KenyaAdditionalInfoTypeDef]
    malaysiaAdditionalInfo: NotRequired[MalaysiaAdditionalInfoUnionTypeDef]
    polandAdditionalInfo: NotRequired[PolandAdditionalInfoTypeDef]
    romaniaAdditionalInfo: NotRequired[RomaniaAdditionalInfoTypeDef]
    saudiArabiaAdditionalInfo: NotRequired[SaudiArabiaAdditionalInfoTypeDef]
    southKoreaAdditionalInfo: NotRequired[SouthKoreaAdditionalInfoTypeDef]
    spainAdditionalInfo: NotRequired[SpainAdditionalInfoTypeDef]
    turkeyAdditionalInfo: NotRequired[TurkeyAdditionalInfoTypeDef]
    ukraineAdditionalInfo: NotRequired[UkraineAdditionalInfoTypeDef]
    uzbekistanAdditionalInfo: NotRequired[UzbekistanAdditionalInfoTypeDef]
    vietnamAdditionalInfo: NotRequired[VietnamAdditionalInfoTypeDef]

class GetTaxRegistrationResponseTypeDef(TypedDict):
    taxRegistration: TaxRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccountDetailsTypeDef(TypedDict):
    accountId: NotRequired[str]
    accountMetaData: NotRequired[AccountMetaDataTypeDef]
    taxInheritanceDetails: NotRequired[TaxInheritanceDetailsTypeDef]
    taxRegistration: NotRequired[TaxRegistrationWithJurisdictionTypeDef]

class TaxExemptionDetailsTypeDef(TypedDict):
    heritageObtainedDetails: NotRequired[bool]
    heritageObtainedParentEntity: NotRequired[str]
    heritageObtainedReason: NotRequired[str]
    taxExemptions: NotRequired[List[TaxExemptionTypeDef]]

class VerificationDetailsTypeDef(TypedDict):
    dateOfBirth: NotRequired[str]
    taxRegistrationDocuments: NotRequired[Sequence[TaxRegistrationDocumentTypeDef]]

class ListTaxRegistrationsResponseTypeDef(TypedDict):
    accountDetails: List[AccountDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class BatchGetTaxExemptionsResponseTypeDef(TypedDict):
    failedAccounts: List[str]
    taxExemptionDetailsMap: Dict[str, TaxExemptionDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTaxExemptionsResponseTypeDef(TypedDict):
    taxExemptionDetailsMap: Dict[str, TaxExemptionDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TaxRegistrationEntryTypeDef(TypedDict):
    registrationId: str
    registrationType: TaxRegistrationTypeType
    additionalTaxInformation: NotRequired[AdditionalInfoRequestTypeDef]
    certifiedEmailId: NotRequired[str]
    legalAddress: NotRequired[AddressTypeDef]
    legalName: NotRequired[str]
    sector: NotRequired[SectorType]
    verificationDetails: NotRequired[VerificationDetailsTypeDef]

class BatchPutTaxRegistrationRequestTypeDef(TypedDict):
    accountIds: Sequence[str]
    taxRegistrationEntry: TaxRegistrationEntryTypeDef

class PutTaxRegistrationRequestTypeDef(TypedDict):
    taxRegistrationEntry: TaxRegistrationEntryTypeDef
    accountId: NotRequired[str]
