"""
Main interface for route53domains service type definitions.

Usage::

    ```python
    from mypy_boto3_route53domains.type_defs import BillingRecordTypeDef

    data: BillingRecordTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BillingRecordTypeDef",
    "ContactDetailTypeDef",
    "DomainSuggestionTypeDef",
    "DomainSummaryTypeDef",
    "DomainTransferabilityTypeDef",
    "ExtraParamTypeDef",
    "NameserverTypeDef",
    "OperationSummaryTypeDef",
    "TagTypeDef",
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    "CheckDomainAvailabilityResponseTypeDef",
    "CheckDomainTransferabilityResponseTypeDef",
    "DisableDomainTransferLockResponseTypeDef",
    "EnableDomainTransferLockResponseTypeDef",
    "GetContactReachabilityStatusResponseTypeDef",
    "GetDomainDetailResponseTypeDef",
    "GetDomainSuggestionsResponseTypeDef",
    "GetOperationDetailResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListTagsForDomainResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterDomainResponseTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "RenewDomainResponseTypeDef",
    "ResendContactReachabilityEmailResponseTypeDef",
    "RetrieveDomainAuthCodeResponseTypeDef",
    "TransferDomainResponseTypeDef",
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    "UpdateDomainContactPrivacyResponseTypeDef",
    "UpdateDomainContactResponseTypeDef",
    "UpdateDomainNameserversResponseTypeDef",
    "ViewBillingResponseTypeDef",
)

BillingRecordTypeDef = TypedDict(
    "BillingRecordTypeDef",
    {
        "DomainName": str,
        "Operation": Literal[
            "REGISTER_DOMAIN",
            "DELETE_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
            "CHANGE_PRIVACY_PROTECTION",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "DISABLE_AUTORENEW",
            "ADD_DNSSEC",
            "REMOVE_DNSSEC",
            "EXPIRE_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "CHANGE_DOMAIN_OWNER",
            "RENEW_DOMAIN",
            "PUSH_DOMAIN",
            "INTERNAL_TRANSFER_OUT_DOMAIN",
            "INTERNAL_TRANSFER_IN_DOMAIN",
        ],
        "InvoiceId": str,
        "BillDate": datetime,
        "Price": float,
    },
    total=False,
)

ContactDetailTypeDef = TypedDict(
    "ContactDetailTypeDef",
    {
        "FirstName": str,
        "LastName": str,
        "ContactType": Literal["PERSON", "COMPANY", "ASSOCIATION", "PUBLIC_BODY", "RESELLER"],
        "OrganizationName": str,
        "AddressLine1": str,
        "AddressLine2": str,
        "City": str,
        "State": str,
        "CountryCode": Literal[
            "AD",
            "AE",
            "AF",
            "AG",
            "AI",
            "AL",
            "AM",
            "AN",
            "AO",
            "AQ",
            "AR",
            "AS",
            "AT",
            "AU",
            "AW",
            "AZ",
            "BA",
            "BB",
            "BD",
            "BE",
            "BF",
            "BG",
            "BH",
            "BI",
            "BJ",
            "BL",
            "BM",
            "BN",
            "BO",
            "BR",
            "BS",
            "BT",
            "BW",
            "BY",
            "BZ",
            "CA",
            "CC",
            "CD",
            "CF",
            "CG",
            "CH",
            "CI",
            "CK",
            "CL",
            "CM",
            "CN",
            "CO",
            "CR",
            "CU",
            "CV",
            "CX",
            "CY",
            "CZ",
            "DE",
            "DJ",
            "DK",
            "DM",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ER",
            "ES",
            "ET",
            "FI",
            "FJ",
            "FK",
            "FM",
            "FO",
            "FR",
            "GA",
            "GB",
            "GD",
            "GE",
            "GH",
            "GI",
            "GL",
            "GM",
            "GN",
            "GQ",
            "GR",
            "GT",
            "GU",
            "GW",
            "GY",
            "HK",
            "HN",
            "HR",
            "HT",
            "HU",
            "ID",
            "IE",
            "IL",
            "IM",
            "IN",
            "IQ",
            "IR",
            "IS",
            "IT",
            "JM",
            "JO",
            "JP",
            "KE",
            "KG",
            "KH",
            "KI",
            "KM",
            "KN",
            "KP",
            "KR",
            "KW",
            "KY",
            "KZ",
            "LA",
            "LB",
            "LC",
            "LI",
            "LK",
            "LR",
            "LS",
            "LT",
            "LU",
            "LV",
            "LY",
            "MA",
            "MC",
            "MD",
            "ME",
            "MF",
            "MG",
            "MH",
            "MK",
            "ML",
            "MM",
            "MN",
            "MO",
            "MP",
            "MR",
            "MS",
            "MT",
            "MU",
            "MV",
            "MW",
            "MX",
            "MY",
            "MZ",
            "NA",
            "NC",
            "NE",
            "NG",
            "NI",
            "NL",
            "NO",
            "NP",
            "NR",
            "NU",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PF",
            "PG",
            "PH",
            "PK",
            "PL",
            "PM",
            "PN",
            "PR",
            "PT",
            "PW",
            "PY",
            "QA",
            "RO",
            "RS",
            "RU",
            "RW",
            "SA",
            "SB",
            "SC",
            "SD",
            "SE",
            "SG",
            "SH",
            "SI",
            "SK",
            "SL",
            "SM",
            "SN",
            "SO",
            "SR",
            "ST",
            "SV",
            "SY",
            "SZ",
            "TC",
            "TD",
            "TG",
            "TH",
            "TJ",
            "TK",
            "TL",
            "TM",
            "TN",
            "TO",
            "TR",
            "TT",
            "TV",
            "TW",
            "TZ",
            "UA",
            "UG",
            "US",
            "UY",
            "UZ",
            "VA",
            "VC",
            "VE",
            "VG",
            "VI",
            "VN",
            "VU",
            "WF",
            "WS",
            "YE",
            "YT",
            "ZA",
            "ZM",
            "ZW",
        ],
        "ZipCode": str,
        "PhoneNumber": str,
        "Email": str,
        "Fax": str,
        "ExtraParams": List["ExtraParamTypeDef"],
    },
    total=False,
)

DomainSuggestionTypeDef = TypedDict(
    "DomainSuggestionTypeDef", {"DomainName": str, "Availability": str}, total=False
)

_RequiredDomainSummaryTypeDef = TypedDict("_RequiredDomainSummaryTypeDef", {"DomainName": str})
_OptionalDomainSummaryTypeDef = TypedDict(
    "_OptionalDomainSummaryTypeDef",
    {"AutoRenew": bool, "TransferLock": bool, "Expiry": datetime},
    total=False,
)


class DomainSummaryTypeDef(_RequiredDomainSummaryTypeDef, _OptionalDomainSummaryTypeDef):
    pass


DomainTransferabilityTypeDef = TypedDict(
    "DomainTransferabilityTypeDef",
    {"Transferable": Literal["TRANSFERABLE", "UNTRANSFERABLE", "DONT_KNOW"]},
    total=False,
)

ExtraParamTypeDef = TypedDict(
    "ExtraParamTypeDef",
    {
        "Name": Literal[
            "DUNS_NUMBER",
            "BRAND_NUMBER",
            "BIRTH_DEPARTMENT",
            "BIRTH_DATE_IN_YYYY_MM_DD",
            "BIRTH_COUNTRY",
            "BIRTH_CITY",
            "DOCUMENT_NUMBER",
            "AU_ID_NUMBER",
            "AU_ID_TYPE",
            "CA_LEGAL_TYPE",
            "CA_BUSINESS_ENTITY_TYPE",
            "CA_LEGAL_REPRESENTATIVE",
            "CA_LEGAL_REPRESENTATIVE_CAPACITY",
            "ES_IDENTIFICATION",
            "ES_IDENTIFICATION_TYPE",
            "ES_LEGAL_FORM",
            "FI_BUSINESS_NUMBER",
            "FI_ID_NUMBER",
            "FI_NATIONALITY",
            "FI_ORGANIZATION_TYPE",
            "IT_NATIONALITY",
            "IT_PIN",
            "IT_REGISTRANT_ENTITY_TYPE",
            "RU_PASSPORT_DATA",
            "SE_ID_NUMBER",
            "SG_ID_NUMBER",
            "VAT_NUMBER",
            "UK_CONTACT_TYPE",
            "UK_COMPANY_NUMBER",
        ],
        "Value": str,
    },
)

_RequiredNameserverTypeDef = TypedDict("_RequiredNameserverTypeDef", {"Name": str})
_OptionalNameserverTypeDef = TypedDict(
    "_OptionalNameserverTypeDef", {"GlueIps": List[str]}, total=False
)


class NameserverTypeDef(_RequiredNameserverTypeDef, _OptionalNameserverTypeDef):
    pass


OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "OperationId": str,
        "Status": Literal["SUBMITTED", "IN_PROGRESS", "ERROR", "SUCCESSFUL", "FAILED"],
        "Type": Literal[
            "REGISTER_DOMAIN",
            "DELETE_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
            "CHANGE_PRIVACY_PROTECTION",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "DISABLE_AUTORENEW",
            "ADD_DNSSEC",
            "REMOVE_DNSSEC",
            "EXPIRE_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "CHANGE_DOMAIN_OWNER",
            "RENEW_DOMAIN",
            "PUSH_DOMAIN",
            "INTERNAL_TRANSFER_OUT_DOMAIN",
            "INTERNAL_TRANSFER_IN_DOMAIN",
        ],
        "SubmittedDate": datetime,
    },
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef = TypedDict(
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef", {"OperationId": str}, total=False
)

CancelDomainTransferToAnotherAwsAccountResponseTypeDef = TypedDict(
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef", {"OperationId": str}, total=False
)

CheckDomainAvailabilityResponseTypeDef = TypedDict(
    "CheckDomainAvailabilityResponseTypeDef",
    {
        "Availability": Literal[
            "AVAILABLE",
            "AVAILABLE_RESERVED",
            "AVAILABLE_PREORDER",
            "UNAVAILABLE",
            "UNAVAILABLE_PREMIUM",
            "UNAVAILABLE_RESTRICTED",
            "RESERVED",
            "DONT_KNOW",
        ]
    },
)

CheckDomainTransferabilityResponseTypeDef = TypedDict(
    "CheckDomainTransferabilityResponseTypeDef", {"Transferability": "DomainTransferabilityTypeDef"}
)

DisableDomainTransferLockResponseTypeDef = TypedDict(
    "DisableDomainTransferLockResponseTypeDef", {"OperationId": str}
)

EnableDomainTransferLockResponseTypeDef = TypedDict(
    "EnableDomainTransferLockResponseTypeDef", {"OperationId": str}
)

GetContactReachabilityStatusResponseTypeDef = TypedDict(
    "GetContactReachabilityStatusResponseTypeDef",
    {"domainName": str, "status": Literal["PENDING", "DONE", "EXPIRED"]},
    total=False,
)

_RequiredGetDomainDetailResponseTypeDef = TypedDict(
    "_RequiredGetDomainDetailResponseTypeDef",
    {
        "DomainName": str,
        "Nameservers": List["NameserverTypeDef"],
        "AdminContact": "ContactDetailTypeDef",
        "RegistrantContact": "ContactDetailTypeDef",
        "TechContact": "ContactDetailTypeDef",
    },
)
_OptionalGetDomainDetailResponseTypeDef = TypedDict(
    "_OptionalGetDomainDetailResponseTypeDef",
    {
        "AutoRenew": bool,
        "AdminPrivacy": bool,
        "RegistrantPrivacy": bool,
        "TechPrivacy": bool,
        "RegistrarName": str,
        "WhoIsServer": str,
        "RegistrarUrl": str,
        "AbuseContactEmail": str,
        "AbuseContactPhone": str,
        "RegistryDomainId": str,
        "CreationDate": datetime,
        "UpdatedDate": datetime,
        "ExpirationDate": datetime,
        "Reseller": str,
        "DnsSec": str,
        "StatusList": List[str],
    },
    total=False,
)


class GetDomainDetailResponseTypeDef(
    _RequiredGetDomainDetailResponseTypeDef, _OptionalGetDomainDetailResponseTypeDef
):
    pass


GetDomainSuggestionsResponseTypeDef = TypedDict(
    "GetDomainSuggestionsResponseTypeDef",
    {"SuggestionsList": List["DomainSuggestionTypeDef"]},
    total=False,
)

GetOperationDetailResponseTypeDef = TypedDict(
    "GetOperationDetailResponseTypeDef",
    {
        "OperationId": str,
        "Status": Literal["SUBMITTED", "IN_PROGRESS", "ERROR", "SUCCESSFUL", "FAILED"],
        "Message": str,
        "DomainName": str,
        "Type": Literal[
            "REGISTER_DOMAIN",
            "DELETE_DOMAIN",
            "TRANSFER_IN_DOMAIN",
            "UPDATE_DOMAIN_CONTACT",
            "UPDATE_NAMESERVER",
            "CHANGE_PRIVACY_PROTECTION",
            "DOMAIN_LOCK",
            "ENABLE_AUTORENEW",
            "DISABLE_AUTORENEW",
            "ADD_DNSSEC",
            "REMOVE_DNSSEC",
            "EXPIRE_DOMAIN",
            "TRANSFER_OUT_DOMAIN",
            "CHANGE_DOMAIN_OWNER",
            "RENEW_DOMAIN",
            "PUSH_DOMAIN",
            "INTERNAL_TRANSFER_OUT_DOMAIN",
            "INTERNAL_TRANSFER_IN_DOMAIN",
        ],
        "SubmittedDate": datetime,
    },
    total=False,
)

_RequiredListDomainsResponseTypeDef = TypedDict(
    "_RequiredListDomainsResponseTypeDef", {"Domains": List["DomainSummaryTypeDef"]}
)
_OptionalListDomainsResponseTypeDef = TypedDict(
    "_OptionalListDomainsResponseTypeDef", {"NextPageMarker": str}, total=False
)


class ListDomainsResponseTypeDef(
    _RequiredListDomainsResponseTypeDef, _OptionalListDomainsResponseTypeDef
):
    pass


_RequiredListOperationsResponseTypeDef = TypedDict(
    "_RequiredListOperationsResponseTypeDef", {"Operations": List["OperationSummaryTypeDef"]}
)
_OptionalListOperationsResponseTypeDef = TypedDict(
    "_OptionalListOperationsResponseTypeDef", {"NextPageMarker": str}, total=False
)


class ListOperationsResponseTypeDef(
    _RequiredListOperationsResponseTypeDef, _OptionalListOperationsResponseTypeDef
):
    pass


ListTagsForDomainResponseTypeDef = TypedDict(
    "ListTagsForDomainResponseTypeDef", {"TagList": List["TagTypeDef"]}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterDomainResponseTypeDef = TypedDict("RegisterDomainResponseTypeDef", {"OperationId": str})

RejectDomainTransferFromAnotherAwsAccountResponseTypeDef = TypedDict(
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef", {"OperationId": str}, total=False
)

RenewDomainResponseTypeDef = TypedDict("RenewDomainResponseTypeDef", {"OperationId": str})

ResendContactReachabilityEmailResponseTypeDef = TypedDict(
    "ResendContactReachabilityEmailResponseTypeDef",
    {"domainName": str, "emailAddress": str, "isAlreadyVerified": bool},
    total=False,
)

RetrieveDomainAuthCodeResponseTypeDef = TypedDict(
    "RetrieveDomainAuthCodeResponseTypeDef", {"AuthCode": str}
)

TransferDomainResponseTypeDef = TypedDict("TransferDomainResponseTypeDef", {"OperationId": str})

TransferDomainToAnotherAwsAccountResponseTypeDef = TypedDict(
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    {"OperationId": str, "Password": str},
    total=False,
)

UpdateDomainContactPrivacyResponseTypeDef = TypedDict(
    "UpdateDomainContactPrivacyResponseTypeDef", {"OperationId": str}
)

UpdateDomainContactResponseTypeDef = TypedDict(
    "UpdateDomainContactResponseTypeDef", {"OperationId": str}
)

UpdateDomainNameserversResponseTypeDef = TypedDict(
    "UpdateDomainNameserversResponseTypeDef", {"OperationId": str}
)

ViewBillingResponseTypeDef = TypedDict(
    "ViewBillingResponseTypeDef",
    {"NextPageMarker": str, "BillingRecords": List["BillingRecordTypeDef"]},
    total=False,
)
