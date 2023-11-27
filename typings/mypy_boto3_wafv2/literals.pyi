"""
Type annotations for wafv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/literals.html)

Usage::

    ```python
    from mypy_boto3_wafv2.literals import ActionValueType

    data: ActionValueType = "ALLOW"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionValueType",
    "AssociatedResourceTypeType",
    "BodyParsingFallbackBehaviorType",
    "ComparisonOperatorType",
    "CountryCodeType",
    "FailureReasonType",
    "FallbackBehaviorType",
    "FilterBehaviorType",
    "FilterRequirementType",
    "ForwardedIPPositionType",
    "IPAddressVersionType",
    "InspectionLevelType",
    "JsonMatchScopeType",
    "LabelMatchScopeType",
    "MapMatchScopeType",
    "OversizeHandlingType",
    "PayloadTypeType",
    "PlatformType",
    "PositionalConstraintType",
    "RateBasedStatementAggregateKeyTypeType",
    "ResourceTypeType",
    "ResponseContentTypeType",
    "ScopeType",
    "SensitivityLevelType",
    "SizeInspectionLimitType",
    "TextTransformationTypeType",
)

ActionValueType = Literal["ALLOW", "BLOCK", "CAPTCHA", "CHALLENGE", "COUNT", "EXCLUDED_AS_COUNT"]
AssociatedResourceTypeType = Literal["CLOUDFRONT"]
BodyParsingFallbackBehaviorType = Literal["EVALUATE_AS_STRING", "MATCH", "NO_MATCH"]
ComparisonOperatorType = Literal["EQ", "GE", "GT", "LE", "LT", "NE"]
CountryCodeType = Literal[
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
    "XK",
    "YE",
    "YT",
    "ZA",
    "ZM",
    "ZW",
]
FailureReasonType = Literal[
    "TOKEN_DOMAIN_MISMATCH", "TOKEN_EXPIRED", "TOKEN_INVALID", "TOKEN_MISSING"
]
FallbackBehaviorType = Literal["MATCH", "NO_MATCH"]
FilterBehaviorType = Literal["DROP", "KEEP"]
FilterRequirementType = Literal["MEETS_ALL", "MEETS_ANY"]
ForwardedIPPositionType = Literal["ANY", "FIRST", "LAST"]
IPAddressVersionType = Literal["IPV4", "IPV6"]
InspectionLevelType = Literal["COMMON", "TARGETED"]
JsonMatchScopeType = Literal["ALL", "KEY", "VALUE"]
LabelMatchScopeType = Literal["LABEL", "NAMESPACE"]
MapMatchScopeType = Literal["ALL", "KEY", "VALUE"]
OversizeHandlingType = Literal["CONTINUE", "MATCH", "NO_MATCH"]
PayloadTypeType = Literal["FORM_ENCODED", "JSON"]
PlatformType = Literal["ANDROID", "IOS"]
PositionalConstraintType = Literal[
    "CONTAINS", "CONTAINS_WORD", "ENDS_WITH", "EXACTLY", "STARTS_WITH"
]
RateBasedStatementAggregateKeyTypeType = Literal["CONSTANT", "CUSTOM_KEYS", "FORWARDED_IP", "IP"]
ResourceTypeType = Literal[
    "API_GATEWAY",
    "APPLICATION_LOAD_BALANCER",
    "APPSYNC",
    "APP_RUNNER_SERVICE",
    "COGNITO_USER_POOL",
    "VERIFIED_ACCESS_INSTANCE",
]
ResponseContentTypeType = Literal["APPLICATION_JSON", "TEXT_HTML", "TEXT_PLAIN"]
ScopeType = Literal["CLOUDFRONT", "REGIONAL"]
SensitivityLevelType = Literal["HIGH", "LOW"]
SizeInspectionLimitType = Literal["KB_16", "KB_32", "KB_48", "KB_64"]
TextTransformationTypeType = Literal[
    "BASE64_DECODE",
    "BASE64_DECODE_EXT",
    "CMD_LINE",
    "COMPRESS_WHITE_SPACE",
    "CSS_DECODE",
    "ESCAPE_SEQ_DECODE",
    "HEX_DECODE",
    "HTML_ENTITY_DECODE",
    "JS_DECODE",
    "LOWERCASE",
    "MD5",
    "NONE",
    "NORMALIZE_PATH",
    "NORMALIZE_PATH_WIN",
    "REMOVE_NULLS",
    "REPLACE_COMMENTS",
    "REPLACE_NULLS",
    "SQL_HEX_DECODE",
    "URL_DECODE",
    "URL_DECODE_UNI",
    "UTF8_TO_UNICODE",
]