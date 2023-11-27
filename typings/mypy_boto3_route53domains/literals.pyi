"""
Type annotations for route53domains service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/literals.html)

Usage::

    ```python
    from mypy_boto3_route53domains.literals import ContactTypeType

    data: ContactTypeType = "ASSOCIATION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ContactTypeType",
    "CountryCodeType",
    "DomainAvailabilityType",
    "ExtraParamNameType",
    "ListDomainsAttributeNameType",
    "ListDomainsPaginatorName",
    "ListOperationsPaginatorName",
    "ListOperationsSortAttributeNameType",
    "ListPricesPaginatorName",
    "OperationStatusType",
    "OperationTypeType",
    "OperatorType",
    "ReachabilityStatusType",
    "SortOrderType",
    "StatusFlagType",
    "TransferableType",
    "ViewBillingPaginatorName",
)

ContactTypeType = Literal["ASSOCIATION", "COMPANY", "PERSON", "PUBLIC_BODY", "RESELLER"]
CountryCodeType = Literal[
    "AC",
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
    "AX",
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
    "BQ",
    "BR",
    "BS",
    "BT",
    "BV",
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
    "CW",
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
    "EH",
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
    "GF",
    "GG",
    "GH",
    "GI",
    "GL",
    "GM",
    "GN",
    "GP",
    "GQ",
    "GR",
    "GS",
    "GT",
    "GU",
    "GW",
    "GY",
    "HK",
    "HM",
    "HN",
    "HR",
    "HT",
    "HU",
    "ID",
    "IE",
    "IL",
    "IM",
    "IN",
    "IO",
    "IQ",
    "IR",
    "IS",
    "IT",
    "JE",
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
    "MQ",
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
    "NF",
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
    "PS",
    "PT",
    "PW",
    "PY",
    "QA",
    "RE",
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
    "SJ",
    "SK",
    "SL",
    "SM",
    "SN",
    "SO",
    "SR",
    "SS",
    "ST",
    "SV",
    "SX",
    "SY",
    "SZ",
    "TC",
    "TD",
    "TF",
    "TG",
    "TH",
    "TJ",
    "TK",
    "TL",
    "TM",
    "TN",
    "TO",
    "TP",
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
]
DomainAvailabilityType = Literal[
    "AVAILABLE",
    "AVAILABLE_PREORDER",
    "AVAILABLE_RESERVED",
    "DONT_KNOW",
    "RESERVED",
    "UNAVAILABLE",
    "UNAVAILABLE_PREMIUM",
    "UNAVAILABLE_RESTRICTED",
]
ExtraParamNameType = Literal[
    "AU_ID_NUMBER",
    "AU_ID_TYPE",
    "AU_PRIORITY_TOKEN",
    "BIRTH_CITY",
    "BIRTH_COUNTRY",
    "BIRTH_DATE_IN_YYYY_MM_DD",
    "BIRTH_DEPARTMENT",
    "BRAND_NUMBER",
    "CA_BUSINESS_ENTITY_TYPE",
    "CA_LEGAL_REPRESENTATIVE",
    "CA_LEGAL_REPRESENTATIVE_CAPACITY",
    "CA_LEGAL_TYPE",
    "DOCUMENT_NUMBER",
    "DUNS_NUMBER",
    "ES_IDENTIFICATION",
    "ES_IDENTIFICATION_TYPE",
    "ES_LEGAL_FORM",
    "EU_COUNTRY_OF_CITIZENSHIP",
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
    "UK_COMPANY_NUMBER",
    "UK_CONTACT_TYPE",
    "VAT_NUMBER",
]
ListDomainsAttributeNameType = Literal["DomainName", "Expiry"]
ListDomainsPaginatorName = Literal["list_domains"]
ListOperationsPaginatorName = Literal["list_operations"]
ListOperationsSortAttributeNameType = Literal["SubmittedDate"]
ListPricesPaginatorName = Literal["list_prices"]
OperationStatusType = Literal["ERROR", "FAILED", "IN_PROGRESS", "SUBMITTED", "SUCCESSFUL"]
OperationTypeType = Literal[
    "ADD_DNSSEC",
    "CHANGE_DOMAIN_OWNER",
    "CHANGE_PRIVACY_PROTECTION",
    "DELETE_DOMAIN",
    "DISABLE_AUTORENEW",
    "DOMAIN_LOCK",
    "ENABLE_AUTORENEW",
    "EXPIRE_DOMAIN",
    "INTERNAL_TRANSFER_IN_DOMAIN",
    "INTERNAL_TRANSFER_OUT_DOMAIN",
    "PUSH_DOMAIN",
    "REGISTER_DOMAIN",
    "REMOVE_DNSSEC",
    "RENEW_DOMAIN",
    "TRANSFER_IN_DOMAIN",
    "TRANSFER_OUT_DOMAIN",
    "UPDATE_DOMAIN_CONTACT",
    "UPDATE_NAMESERVER",
]
OperatorType = Literal["BEGINS_WITH", "GE", "LE"]
ReachabilityStatusType = Literal["DONE", "EXPIRED", "PENDING"]
SortOrderType = Literal["ASC", "DESC"]
StatusFlagType = Literal[
    "PENDING_ACCEPTANCE",
    "PENDING_AUTHORIZATION",
    "PENDING_CUSTOMER_ACTION",
    "PENDING_PAYMENT_VERIFICATION",
    "PENDING_SUPPORT_CASE",
]
TransferableType = Literal[
    "DOMAIN_IN_ANOTHER_ACCOUNT",
    "DOMAIN_IN_OWN_ACCOUNT",
    "DONT_KNOW",
    "PREMIUM_DOMAIN",
    "TRANSFERABLE",
    "UNTRANSFERABLE",
]
ViewBillingPaginatorName = Literal["view_billing"]