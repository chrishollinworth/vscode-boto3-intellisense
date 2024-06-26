"""
Type annotations for waf-regional service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf_regional/literals.html)

Usage::

    ```python
    from mypy_boto3_waf_regional.literals import ChangeActionType

    data: ChangeActionType = "DELETE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ChangeActionType",
    "ChangeTokenStatusType",
    "ComparisonOperatorType",
    "GeoMatchConstraintTypeType",
    "GeoMatchConstraintValueType",
    "IPSetDescriptorTypeType",
    "MatchFieldTypeType",
    "PositionalConstraintType",
    "PredicateTypeType",
    "RateKeyType",
    "ResourceTypeType",
    "TextTransformationType",
    "WafActionTypeType",
    "WafOverrideActionTypeType",
    "WafRuleTypeType",
)

ChangeActionType = Literal["DELETE", "INSERT"]
ChangeTokenStatusType = Literal["INSYNC", "PENDING", "PROVISIONED"]
ComparisonOperatorType = Literal["EQ", "GE", "GT", "LE", "LT", "NE"]
GeoMatchConstraintTypeType = Literal["Country"]
GeoMatchConstraintValueType = Literal[
    "AD",
    "AE",
    "AF",
    "AG",
    "AI",
    "AL",
    "AM",
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
    "TR",
    "TT",
    "TV",
    "TW",
    "TZ",
    "UA",
    "UG",
    "UM",
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
IPSetDescriptorTypeType = Literal["IPV4", "IPV6"]
MatchFieldTypeType = Literal[
    "ALL_QUERY_ARGS", "BODY", "HEADER", "METHOD", "QUERY_STRING", "SINGLE_QUERY_ARG", "URI"
]
PositionalConstraintType = Literal[
    "CONTAINS", "CONTAINS_WORD", "ENDS_WITH", "EXACTLY", "STARTS_WITH"
]
PredicateTypeType = Literal[
    "ByteMatch",
    "GeoMatch",
    "IPMatch",
    "RegexMatch",
    "SizeConstraint",
    "SqlInjectionMatch",
    "XssMatch",
]
RateKeyType = Literal["IP"]
ResourceTypeType = Literal["API_GATEWAY", "APPLICATION_LOAD_BALANCER"]
TextTransformationType = Literal[
    "CMD_LINE", "COMPRESS_WHITE_SPACE", "HTML_ENTITY_DECODE", "LOWERCASE", "NONE", "URL_DECODE"
]
WafActionTypeType = Literal["ALLOW", "BLOCK", "COUNT"]
WafOverrideActionTypeType = Literal["COUNT", "NONE"]
WafRuleTypeType = Literal["GROUP", "RATE_BASED", "REGULAR"]
