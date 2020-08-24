"""
Main interface for wafv2 service type definitions.

Usage::

    ```python
    from mypy_boto3_wafv2.type_defs import AndStatementTypeDef

    data: AndStatementTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AndStatementTypeDef",
    "ByteMatchStatementTypeDef",
    "DefaultActionTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "FirewallManagerStatementTypeDef",
    "ForwardedIPConfigTypeDef",
    "GeoMatchStatementTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "IPSetReferenceStatementTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "LoggingConfigurationTypeDef",
    "ManagedRuleGroupStatementTypeDef",
    "ManagedRuleGroupSummaryTypeDef",
    "NotStatementTypeDef",
    "OrStatementTypeDef",
    "OverrideActionTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "RateBasedStatementTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexTypeDef",
    "RuleActionTypeDef",
    "RuleGroupReferenceStatementTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "SampledHTTPRequestTypeDef",
    "SingleHeaderTypeDef",
    "SingleQueryArgumentTypeDef",
    "SizeConstraintStatementTypeDef",
    "SqliMatchStatementTypeDef",
    "TagInfoForResourceTypeDef",
    "TagTypeDef",
    "TextTransformationTypeDef",
    "TimeWindowTypeDef",
    "VisibilityConfigTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "XssMatchStatementTypeDef",
    "CheckCapacityResponseTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateWebACLResponseTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "StatementTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLResponseTypeDef",
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsResponseTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateWebACLResponseTypeDef",
)

AndStatementTypeDef = TypedDict("AndStatementTypeDef", {"Statements": List[Dict[str, Any]]})

ByteMatchStatementTypeDef = TypedDict(
    "ByteMatchStatementTypeDef",
    {
        "SearchString": bytes,
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
        "PositionalConstraint": Literal[
            "EXACTLY", "STARTS_WITH", "ENDS_WITH", "CONTAINS", "CONTAINS_WORD"
        ],
    },
)

DefaultActionTypeDef = TypedDict(
    "DefaultActionTypeDef", {"Block": Dict[str, Any], "Allow": Dict[str, Any]}, total=False
)

ExcludedRuleTypeDef = TypedDict("ExcludedRuleTypeDef", {"Name": str})

FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "SingleHeader": "SingleHeaderTypeDef",
        "SingleQueryArgument": "SingleQueryArgumentTypeDef",
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": Dict[str, Any],
        "Method": Dict[str, Any],
    },
    total=False,
)

FirewallManagerRuleGroupTypeDef = TypedDict(
    "FirewallManagerRuleGroupTypeDef",
    {
        "Name": str,
        "Priority": int,
        "FirewallManagerStatement": "FirewallManagerStatementTypeDef",
        "OverrideAction": "OverrideActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)

FirewallManagerStatementTypeDef = TypedDict(
    "FirewallManagerStatementTypeDef",
    {
        "ManagedRuleGroupStatement": "ManagedRuleGroupStatementTypeDef",
        "RuleGroupReferenceStatement": "RuleGroupReferenceStatementTypeDef",
    },
    total=False,
)

ForwardedIPConfigTypeDef = TypedDict(
    "ForwardedIPConfigTypeDef",
    {"HeaderName": str, "FallbackBehavior": Literal["MATCH", "NO_MATCH"]},
)

GeoMatchStatementTypeDef = TypedDict(
    "GeoMatchStatementTypeDef",
    {
        "CountryCodes": List[
            Literal[
                "AF",
                "AX",
                "AL",
                "DZ",
                "AS",
                "AD",
                "AO",
                "AI",
                "AQ",
                "AG",
                "AR",
                "AM",
                "AW",
                "AU",
                "AT",
                "AZ",
                "BS",
                "BH",
                "BD",
                "BB",
                "BY",
                "BE",
                "BZ",
                "BJ",
                "BM",
                "BT",
                "BO",
                "BQ",
                "BA",
                "BW",
                "BV",
                "BR",
                "IO",
                "BN",
                "BG",
                "BF",
                "BI",
                "KH",
                "CM",
                "CA",
                "CV",
                "KY",
                "CF",
                "TD",
                "CL",
                "CN",
                "CX",
                "CC",
                "CO",
                "KM",
                "CG",
                "CD",
                "CK",
                "CR",
                "CI",
                "HR",
                "CU",
                "CW",
                "CY",
                "CZ",
                "DK",
                "DJ",
                "DM",
                "DO",
                "EC",
                "EG",
                "SV",
                "GQ",
                "ER",
                "EE",
                "ET",
                "FK",
                "FO",
                "FJ",
                "FI",
                "FR",
                "GF",
                "PF",
                "TF",
                "GA",
                "GM",
                "GE",
                "DE",
                "GH",
                "GI",
                "GR",
                "GL",
                "GD",
                "GP",
                "GU",
                "GT",
                "GG",
                "GN",
                "GW",
                "GY",
                "HT",
                "HM",
                "VA",
                "HN",
                "HK",
                "HU",
                "IS",
                "IN",
                "ID",
                "IR",
                "IQ",
                "IE",
                "IM",
                "IL",
                "IT",
                "JM",
                "JP",
                "JE",
                "JO",
                "KZ",
                "KE",
                "KI",
                "KP",
                "KR",
                "KW",
                "KG",
                "LA",
                "LV",
                "LB",
                "LS",
                "LR",
                "LY",
                "LI",
                "LT",
                "LU",
                "MO",
                "MK",
                "MG",
                "MW",
                "MY",
                "MV",
                "ML",
                "MT",
                "MH",
                "MQ",
                "MR",
                "MU",
                "YT",
                "MX",
                "FM",
                "MD",
                "MC",
                "MN",
                "ME",
                "MS",
                "MA",
                "MZ",
                "MM",
                "NA",
                "NR",
                "NP",
                "NL",
                "NC",
                "NZ",
                "NI",
                "NE",
                "NG",
                "NU",
                "NF",
                "MP",
                "NO",
                "OM",
                "PK",
                "PW",
                "PS",
                "PA",
                "PG",
                "PY",
                "PE",
                "PH",
                "PN",
                "PL",
                "PT",
                "PR",
                "QA",
                "RE",
                "RO",
                "RU",
                "RW",
                "BL",
                "SH",
                "KN",
                "LC",
                "MF",
                "PM",
                "VC",
                "WS",
                "SM",
                "ST",
                "SA",
                "SN",
                "RS",
                "SC",
                "SL",
                "SG",
                "SX",
                "SK",
                "SI",
                "SB",
                "SO",
                "ZA",
                "GS",
                "SS",
                "ES",
                "LK",
                "SD",
                "SR",
                "SJ",
                "SZ",
                "SE",
                "CH",
                "SY",
                "TW",
                "TJ",
                "TZ",
                "TH",
                "TL",
                "TG",
                "TK",
                "TO",
                "TT",
                "TN",
                "TR",
                "TM",
                "TC",
                "TV",
                "UG",
                "UA",
                "AE",
                "GB",
                "US",
                "UM",
                "UY",
                "UZ",
                "VU",
                "VE",
                "VN",
                "VG",
                "VI",
                "WF",
                "EH",
                "YE",
                "ZM",
                "ZW",
            ]
        ],
        "ForwardedIPConfig": "ForwardedIPConfigTypeDef",
    },
    total=False,
)

HTTPHeaderTypeDef = TypedDict("HTTPHeaderTypeDef", {"Name": str, "Value": str}, total=False)

HTTPRequestTypeDef = TypedDict(
    "HTTPRequestTypeDef",
    {
        "ClientIP": str,
        "Country": str,
        "URI": str,
        "Method": str,
        "HTTPVersion": str,
        "Headers": List["HTTPHeaderTypeDef"],
    },
    total=False,
)

IPSetForwardedIPConfigTypeDef = TypedDict(
    "IPSetForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": Literal["MATCH", "NO_MATCH"],
        "Position": Literal["FIRST", "LAST", "ANY"],
    },
)

_RequiredIPSetReferenceStatementTypeDef = TypedDict(
    "_RequiredIPSetReferenceStatementTypeDef", {"ARN": str}
)
_OptionalIPSetReferenceStatementTypeDef = TypedDict(
    "_OptionalIPSetReferenceStatementTypeDef",
    {"IPSetForwardedIPConfig": "IPSetForwardedIPConfigTypeDef"},
    total=False,
)


class IPSetReferenceStatementTypeDef(
    _RequiredIPSetReferenceStatementTypeDef, _OptionalIPSetReferenceStatementTypeDef
):
    pass


IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

_RequiredIPSetTypeDef = TypedDict(
    "_RequiredIPSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "IPAddressVersion": Literal["IPV4", "IPV6"],
        "Addresses": List[str],
    },
)
_OptionalIPSetTypeDef = TypedDict("_OptionalIPSetTypeDef", {"Description": str}, total=False)


class IPSetTypeDef(_RequiredIPSetTypeDef, _OptionalIPSetTypeDef):
    pass


_RequiredLoggingConfigurationTypeDef = TypedDict(
    "_RequiredLoggingConfigurationTypeDef", {"ResourceArn": str, "LogDestinationConfigs": List[str]}
)
_OptionalLoggingConfigurationTypeDef = TypedDict(
    "_OptionalLoggingConfigurationTypeDef",
    {"RedactedFields": List["FieldToMatchTypeDef"], "ManagedByFirewallManager": bool},
    total=False,
)


class LoggingConfigurationTypeDef(
    _RequiredLoggingConfigurationTypeDef, _OptionalLoggingConfigurationTypeDef
):
    pass


_RequiredManagedRuleGroupStatementTypeDef = TypedDict(
    "_RequiredManagedRuleGroupStatementTypeDef", {"VendorName": str, "Name": str}
)
_OptionalManagedRuleGroupStatementTypeDef = TypedDict(
    "_OptionalManagedRuleGroupStatementTypeDef",
    {"ExcludedRules": List["ExcludedRuleTypeDef"]},
    total=False,
)


class ManagedRuleGroupStatementTypeDef(
    _RequiredManagedRuleGroupStatementTypeDef, _OptionalManagedRuleGroupStatementTypeDef
):
    pass


ManagedRuleGroupSummaryTypeDef = TypedDict(
    "ManagedRuleGroupSummaryTypeDef",
    {"VendorName": str, "Name": str, "Description": str},
    total=False,
)

NotStatementTypeDef = TypedDict("NotStatementTypeDef", {"Statement": Dict[str, Any]})

OrStatementTypeDef = TypedDict("OrStatementTypeDef", {"Statements": List[Dict[str, Any]]})

OverrideActionTypeDef = TypedDict(
    "OverrideActionTypeDef", {"Count": Dict[str, Any], "None": Dict[str, Any]}, total=False
)

RateBasedStatementManagedKeysIPSetTypeDef = TypedDict(
    "RateBasedStatementManagedKeysIPSetTypeDef",
    {"IPAddressVersion": Literal["IPV4", "IPV6"], "Addresses": List[str]},
    total=False,
)

_RequiredRateBasedStatementTypeDef = TypedDict(
    "_RequiredRateBasedStatementTypeDef",
    {"Limit": int, "AggregateKeyType": Literal["IP", "FORWARDED_IP"]},
)
_OptionalRateBasedStatementTypeDef = TypedDict(
    "_OptionalRateBasedStatementTypeDef",
    {"ScopeDownStatement": Dict[str, Any], "ForwardedIPConfig": "ForwardedIPConfigTypeDef"},
    total=False,
)


class RateBasedStatementTypeDef(
    _RequiredRateBasedStatementTypeDef, _OptionalRateBasedStatementTypeDef
):
    pass


RegexPatternSetReferenceStatementTypeDef = TypedDict(
    "RegexPatternSetReferenceStatementTypeDef",
    {
        "ARN": str,
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

RegexPatternSetTypeDef = TypedDict(
    "RegexPatternSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "Description": str,
        "RegularExpressionList": List["RegexTypeDef"],
    },
    total=False,
)

RegexTypeDef = TypedDict("RegexTypeDef", {"RegexString": str}, total=False)

RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {"Block": Dict[str, Any], "Allow": Dict[str, Any], "Count": Dict[str, Any]},
    total=False,
)

_RequiredRuleGroupReferenceStatementTypeDef = TypedDict(
    "_RequiredRuleGroupReferenceStatementTypeDef", {"ARN": str}
)
_OptionalRuleGroupReferenceStatementTypeDef = TypedDict(
    "_OptionalRuleGroupReferenceStatementTypeDef",
    {"ExcludedRules": List["ExcludedRuleTypeDef"]},
    total=False,
)


class RuleGroupReferenceStatementTypeDef(
    _RequiredRuleGroupReferenceStatementTypeDef, _OptionalRuleGroupReferenceStatementTypeDef
):
    pass


RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef",
    {
        "Name": str,
        "Id": str,
        "Capacity": int,
        "ARN": str,
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef", {"Description": str, "Rules": List["RuleTypeDef"]}, total=False
)


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass


RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef", {"Name": str, "Action": "RuleActionTypeDef"}, total=False
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": Dict[str, Any],
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {"Action": "RuleActionTypeDef", "OverrideAction": "OverrideActionTypeDef"},
    total=False,
)


class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass


_RequiredSampledHTTPRequestTypeDef = TypedDict(
    "_RequiredSampledHTTPRequestTypeDef", {"Request": "HTTPRequestTypeDef", "Weight": int}
)
_OptionalSampledHTTPRequestTypeDef = TypedDict(
    "_OptionalSampledHTTPRequestTypeDef",
    {"Timestamp": datetime, "Action": str, "RuleNameWithinRuleGroup": str},
    total=False,
)


class SampledHTTPRequestTypeDef(
    _RequiredSampledHTTPRequestTypeDef, _OptionalSampledHTTPRequestTypeDef
):
    pass


SingleHeaderTypeDef = TypedDict("SingleHeaderTypeDef", {"Name": str})

SingleQueryArgumentTypeDef = TypedDict("SingleQueryArgumentTypeDef", {"Name": str})

SizeConstraintStatementTypeDef = TypedDict(
    "SizeConstraintStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "ComparisonOperator": Literal["EQ", "NE", "LE", "LT", "GE", "GT"],
        "Size": int,
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

SqliMatchStatementTypeDef = TypedDict(
    "SqliMatchStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

TagInfoForResourceTypeDef = TypedDict(
    "TagInfoForResourceTypeDef", {"ResourceARN": str, "TagList": List["TagTypeDef"]}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TextTransformationTypeDef = TypedDict(
    "TextTransformationTypeDef",
    {
        "Priority": int,
        "Type": Literal[
            "NONE",
            "COMPRESS_WHITE_SPACE",
            "HTML_ENTITY_DECODE",
            "LOWERCASE",
            "CMD_LINE",
            "URL_DECODE",
        ],
    },
)

TimeWindowTypeDef = TypedDict("TimeWindowTypeDef", {"StartTime": datetime, "EndTime": datetime})

VisibilityConfigTypeDef = TypedDict(
    "VisibilityConfigTypeDef",
    {"SampledRequestsEnabled": bool, "CloudWatchMetricsEnabled": bool, "MetricName": str},
)

WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {"Name": str, "Id": str, "Description": str, "LockToken": str, "ARN": str},
    total=False,
)

_RequiredWebACLTypeDef = TypedDict(
    "_RequiredWebACLTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "DefaultAction": "DefaultActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalWebACLTypeDef = TypedDict(
    "_OptionalWebACLTypeDef",
    {
        "Description": str,
        "Rules": List["RuleTypeDef"],
        "Capacity": int,
        "PreProcessFirewallManagerRuleGroups": List["FirewallManagerRuleGroupTypeDef"],
        "PostProcessFirewallManagerRuleGroups": List["FirewallManagerRuleGroupTypeDef"],
        "ManagedByFirewallManager": bool,
    },
    total=False,
)


class WebACLTypeDef(_RequiredWebACLTypeDef, _OptionalWebACLTypeDef):
    pass


XssMatchStatementTypeDef = TypedDict(
    "XssMatchStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

CheckCapacityResponseTypeDef = TypedDict(
    "CheckCapacityResponseTypeDef", {"Capacity": int}, total=False
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef", {"Summary": "IPSetSummaryTypeDef"}, total=False
)

CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {"Summary": "RegexPatternSetSummaryTypeDef"},
    total=False,
)

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef", {"Summary": "RuleGroupSummaryTypeDef"}, total=False
)

CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef", {"Summary": "WebACLSummaryTypeDef"}, total=False
)

DeleteFirewallManagerRuleGroupsResponseTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsResponseTypeDef", {"NextWebACLLockToken": str}, total=False
)

DescribeManagedRuleGroupResponseTypeDef = TypedDict(
    "DescribeManagedRuleGroupResponseTypeDef",
    {"Capacity": int, "Rules": List["RuleSummaryTypeDef"]},
    total=False,
)

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "ByteMatchStatement": "ByteMatchStatementTypeDef",
        "SqliMatchStatement": "SqliMatchStatementTypeDef",
        "XssMatchStatement": "XssMatchStatementTypeDef",
        "SizeConstraintStatement": "SizeConstraintStatementTypeDef",
        "GeoMatchStatement": "GeoMatchStatementTypeDef",
        "RuleGroupReferenceStatement": "RuleGroupReferenceStatementTypeDef",
        "IPSetReferenceStatement": "IPSetReferenceStatementTypeDef",
        "RegexPatternSetReferenceStatement": "RegexPatternSetReferenceStatementTypeDef",
        "RateBasedStatement": "RateBasedStatementTypeDef",
        "AndStatement": "AndStatementTypeDef",
        "OrStatement": "OrStatementTypeDef",
        "NotStatement": "NotStatementTypeDef",
        "ManagedRuleGroupStatement": "ManagedRuleGroupStatementTypeDef",
    },
    total=False,
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef", {"IPSet": "IPSetTypeDef", "LockToken": str}, total=False
)

GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {"LoggingConfiguration": "LoggingConfigurationTypeDef"},
    total=False,
)

GetPermissionPolicyResponseTypeDef = TypedDict(
    "GetPermissionPolicyResponseTypeDef", {"Policy": str}, total=False
)

GetRateBasedStatementManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    {
        "ManagedKeysIPV4": "RateBasedStatementManagedKeysIPSetTypeDef",
        "ManagedKeysIPV6": "RateBasedStatementManagedKeysIPSetTypeDef",
    },
    total=False,
)

GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {"RegexPatternSet": "RegexPatternSetTypeDef", "LockToken": str},
    total=False,
)

GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef", {"RuleGroup": "RuleGroupTypeDef", "LockToken": str}, total=False
)

GetSampledRequestsResponseTypeDef = TypedDict(
    "GetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List["SampledHTTPRequestTypeDef"],
        "PopulationSize": int,
        "TimeWindow": "TimeWindowTypeDef",
    },
    total=False,
)

GetWebACLForResourceResponseTypeDef = TypedDict(
    "GetWebACLForResourceResponseTypeDef", {"WebACL": "WebACLTypeDef"}, total=False
)

GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef", {"WebACL": "WebACLTypeDef", "LockToken": str}, total=False
)

ListAvailableManagedRuleGroupsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    {"NextMarker": str, "ManagedRuleGroups": List["ManagedRuleGroupSummaryTypeDef"]},
    total=False,
)

ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {"NextMarker": str, "IPSets": List["IPSetSummaryTypeDef"]},
    total=False,
)

ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {"LoggingConfigurations": List["LoggingConfigurationTypeDef"], "NextMarker": str},
    total=False,
)

ListRegexPatternSetsResponseTypeDef = TypedDict(
    "ListRegexPatternSetsResponseTypeDef",
    {"NextMarker": str, "RegexPatternSets": List["RegexPatternSetSummaryTypeDef"]},
    total=False,
)

ListResourcesForWebACLResponseTypeDef = TypedDict(
    "ListResourcesForWebACLResponseTypeDef", {"ResourceArns": List[str]}, total=False
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {"NextMarker": str, "RuleGroups": List["RuleGroupSummaryTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"NextMarker": str, "TagInfoForResource": "TagInfoForResourceTypeDef"},
    total=False,
)

ListWebACLsResponseTypeDef = TypedDict(
    "ListWebACLsResponseTypeDef",
    {"NextMarker": str, "WebACLs": List["WebACLSummaryTypeDef"]},
    total=False,
)

PutLoggingConfigurationResponseTypeDef = TypedDict(
    "PutLoggingConfigurationResponseTypeDef",
    {"LoggingConfiguration": "LoggingConfigurationTypeDef"},
    total=False,
)

UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef", {"NextLockToken": str}, total=False
)

UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef", {"NextLockToken": str}, total=False
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef", {"NextLockToken": str}, total=False
)

UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef", {"NextLockToken": str}, total=False
)
