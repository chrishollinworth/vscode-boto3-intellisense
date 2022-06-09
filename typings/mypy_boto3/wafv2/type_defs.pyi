"""
Type annotations for wafv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wafv2.type_defs import ActionConditionTypeDef

    data: ActionConditionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionValueType,
    BodyParsingFallbackBehaviorType,
    ComparisonOperatorType,
    CountryCodeType,
    FailureReasonType,
    FallbackBehaviorType,
    FilterBehaviorType,
    FilterRequirementType,
    ForwardedIPPositionType,
    IPAddressVersionType,
    JsonMatchScopeType,
    LabelMatchScopeType,
    MapMatchScopeType,
    OversizeHandlingType,
    PayloadTypeType,
    PlatformType,
    PositionalConstraintType,
    RateBasedStatementAggregateKeyTypeType,
    ResourceTypeType,
    ResponseContentTypeType,
    ScopeType,
    TextTransformationTypeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActionConditionTypeDef",
    "AllowActionTypeDef",
    "AndStatementTypeDef",
    "AssociateWebACLRequestRequestTypeDef",
    "BlockActionTypeDef",
    "BodyTypeDef",
    "ByteMatchStatementTypeDef",
    "CaptchaActionTypeDef",
    "CaptchaConfigTypeDef",
    "CaptchaResponseTypeDef",
    "CheckCapacityRequestRequestTypeDef",
    "CheckCapacityResponseTypeDef",
    "ConditionTypeDef",
    "CookieMatchPatternTypeDef",
    "CookiesTypeDef",
    "CountActionTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRegexPatternSetRequestRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateWebACLRequestRequestTypeDef",
    "CreateWebACLResponseTypeDef",
    "CustomHTTPHeaderTypeDef",
    "CustomRequestHandlingTypeDef",
    "CustomResponseBodyTypeDef",
    "CustomResponseTypeDef",
    "DefaultActionTypeDef",
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeletePermissionPolicyRequestRequestTypeDef",
    "DeleteRegexPatternSetRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteWebACLRequestRequestTypeDef",
    "DescribeManagedRuleGroupRequestRequestTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "DisassociateWebACLRequestRequestTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "FilterTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "FirewallManagerStatementTypeDef",
    "ForwardedIPConfigTypeDef",
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    "GeoMatchStatementTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetManagedRuleSetRequestRequestTypeDef",
    "GetManagedRuleSetResponseTypeDef",
    "GetMobileSdkReleaseRequestRequestTypeDef",
    "GetMobileSdkReleaseResponseTypeDef",
    "GetPermissionPolicyRequestRequestTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedStatementManagedKeysRequestRequestTypeDef",
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    "GetRegexPatternSetRequestRequestTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupRequestRequestTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetSampledRequestsRequestRequestTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetWebACLForResourceRequestRequestTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLRequestRequestTypeDef",
    "GetWebACLResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "HeaderMatchPatternTypeDef",
    "HeadersTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "IPSetReferenceStatementTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "ImmunityTimePropertyTypeDef",
    "JsonBodyTypeDef",
    "JsonMatchPatternTypeDef",
    "LabelMatchStatementTypeDef",
    "LabelNameConditionTypeDef",
    "LabelSummaryTypeDef",
    "LabelTypeDef",
    "ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    "ListAvailableManagedRuleGroupsRequestRequestTypeDef",
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListManagedRuleSetsRequestRequestTypeDef",
    "ListManagedRuleSetsResponseTypeDef",
    "ListMobileSdkReleasesRequestRequestTypeDef",
    "ListMobileSdkReleasesResponseTypeDef",
    "ListRegexPatternSetsRequestRequestTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListResourcesForWebACLRequestRequestTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsRequestRequestTypeDef",
    "ListWebACLsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "LoggingFilterTypeDef",
    "ManagedRuleGroupConfigTypeDef",
    "ManagedRuleGroupStatementTypeDef",
    "ManagedRuleGroupSummaryTypeDef",
    "ManagedRuleGroupVersionTypeDef",
    "ManagedRuleSetSummaryTypeDef",
    "ManagedRuleSetTypeDef",
    "ManagedRuleSetVersionTypeDef",
    "MobileSdkReleaseTypeDef",
    "NotStatementTypeDef",
    "OrStatementTypeDef",
    "OverrideActionTypeDef",
    "PasswordFieldTypeDef",
    "PutLoggingConfigurationRequestRequestTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutManagedRuleSetVersionsRequestRequestTypeDef",
    "PutManagedRuleSetVersionsResponseTypeDef",
    "PutPermissionPolicyRequestRequestTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "RateBasedStatementTypeDef",
    "RegexMatchStatementTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexTypeDef",
    "ReleaseSummaryTypeDef",
    "ResponseMetadataTypeDef",
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
    "StatementTypeDef",
    "TagInfoForResourceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TextTransformationTypeDef",
    "TimeWindowTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    "UpdateRegexPatternSetRequestRequestTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateWebACLRequestRequestTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UsernameFieldTypeDef",
    "VersionToPublishTypeDef",
    "VisibilityConfigTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "XssMatchStatementTypeDef",
)

ActionConditionTypeDef = TypedDict(
    "ActionConditionTypeDef",
    {
        "Action": ActionValueType,
    },
)

AllowActionTypeDef = TypedDict(
    "AllowActionTypeDef",
    {
        "CustomRequestHandling": "CustomRequestHandlingTypeDef",
    },
    total=False,
)

AndStatementTypeDef = TypedDict(
    "AndStatementTypeDef",
    {
        "Statements": List[Dict[str, Any]],
    },
)

AssociateWebACLRequestRequestTypeDef = TypedDict(
    "AssociateWebACLRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "ResourceArn": str,
    },
)

BlockActionTypeDef = TypedDict(
    "BlockActionTypeDef",
    {
        "CustomResponse": "CustomResponseTypeDef",
    },
    total=False,
)

BodyTypeDef = TypedDict(
    "BodyTypeDef",
    {
        "OversizeHandling": OversizeHandlingType,
    },
    total=False,
)

ByteMatchStatementTypeDef = TypedDict(
    "ByteMatchStatementTypeDef",
    {
        "SearchString": Union[bytes, IO[bytes], StreamingBody],
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
        "PositionalConstraint": PositionalConstraintType,
    },
)

CaptchaActionTypeDef = TypedDict(
    "CaptchaActionTypeDef",
    {
        "CustomRequestHandling": "CustomRequestHandlingTypeDef",
    },
    total=False,
)

CaptchaConfigTypeDef = TypedDict(
    "CaptchaConfigTypeDef",
    {
        "ImmunityTimeProperty": "ImmunityTimePropertyTypeDef",
    },
    total=False,
)

CaptchaResponseTypeDef = TypedDict(
    "CaptchaResponseTypeDef",
    {
        "ResponseCode": int,
        "SolveTimestamp": int,
        "FailureReason": FailureReasonType,
    },
    total=False,
)

CheckCapacityRequestRequestTypeDef = TypedDict(
    "CheckCapacityRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "Rules": List["RuleTypeDef"],
    },
)

CheckCapacityResponseTypeDef = TypedDict(
    "CheckCapacityResponseTypeDef",
    {
        "Capacity": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "ActionCondition": "ActionConditionTypeDef",
        "LabelNameCondition": "LabelNameConditionTypeDef",
    },
    total=False,
)

CookieMatchPatternTypeDef = TypedDict(
    "CookieMatchPatternTypeDef",
    {
        "All": Dict[str, Any],
        "IncludedCookies": List[str],
        "ExcludedCookies": List[str],
    },
    total=False,
)

CookiesTypeDef = TypedDict(
    "CookiesTypeDef",
    {
        "MatchPattern": "CookieMatchPatternTypeDef",
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)

CountActionTypeDef = TypedDict(
    "CountActionTypeDef",
    {
        "CustomRequestHandling": "CustomRequestHandlingTypeDef",
    },
    total=False,
)

_RequiredCreateIPSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
    },
)
_OptionalCreateIPSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIPSetRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateIPSetRequestRequestTypeDef(
    _RequiredCreateIPSetRequestRequestTypeDef, _OptionalCreateIPSetRequestRequestTypeDef
):
    pass

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "Summary": "IPSetSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "RegularExpressionList": List["RegexTypeDef"],
    },
)
_OptionalCreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRegexPatternSetRequestRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRegexPatternSetRequestRequestTypeDef(
    _RequiredCreateRegexPatternSetRequestRequestTypeDef,
    _OptionalCreateRegexPatternSetRequestRequestTypeDef,
):
    pass

CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "Summary": "RegexPatternSetSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Capacity": int,
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleGroupRequestRequestTypeDef",
    {
        "Description": str,
        "Rules": List["RuleTypeDef"],
        "Tags": List["TagTypeDef"],
        "CustomResponseBodies": Dict[str, "CustomResponseBodyTypeDef"],
    },
    total=False,
)

class CreateRuleGroupRequestRequestTypeDef(
    _RequiredCreateRuleGroupRequestRequestTypeDef, _OptionalCreateRuleGroupRequestRequestTypeDef
):
    pass

CreateRuleGroupResponseTypeDef = TypedDict(
    "CreateRuleGroupResponseTypeDef",
    {
        "Summary": "RuleGroupSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWebACLRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "DefaultAction": "DefaultActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalCreateWebACLRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWebACLRequestRequestTypeDef",
    {
        "Description": str,
        "Rules": List["RuleTypeDef"],
        "Tags": List["TagTypeDef"],
        "CustomResponseBodies": Dict[str, "CustomResponseBodyTypeDef"],
        "CaptchaConfig": "CaptchaConfigTypeDef",
    },
    total=False,
)

class CreateWebACLRequestRequestTypeDef(
    _RequiredCreateWebACLRequestRequestTypeDef, _OptionalCreateWebACLRequestRequestTypeDef
):
    pass

CreateWebACLResponseTypeDef = TypedDict(
    "CreateWebACLResponseTypeDef",
    {
        "Summary": "WebACLSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomHTTPHeaderTypeDef = TypedDict(
    "CustomHTTPHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

CustomRequestHandlingTypeDef = TypedDict(
    "CustomRequestHandlingTypeDef",
    {
        "InsertHeaders": List["CustomHTTPHeaderTypeDef"],
    },
)

CustomResponseBodyTypeDef = TypedDict(
    "CustomResponseBodyTypeDef",
    {
        "ContentType": ResponseContentTypeType,
        "Content": str,
    },
)

_RequiredCustomResponseTypeDef = TypedDict(
    "_RequiredCustomResponseTypeDef",
    {
        "ResponseCode": int,
    },
)
_OptionalCustomResponseTypeDef = TypedDict(
    "_OptionalCustomResponseTypeDef",
    {
        "CustomResponseBodyKey": str,
        "ResponseHeaders": List["CustomHTTPHeaderTypeDef"],
    },
    total=False,
)

class CustomResponseTypeDef(_RequiredCustomResponseTypeDef, _OptionalCustomResponseTypeDef):
    pass

DefaultActionTypeDef = TypedDict(
    "DefaultActionTypeDef",
    {
        "Block": "BlockActionTypeDef",
        "Allow": "AllowActionTypeDef",
    },
    total=False,
)

DeleteFirewallManagerRuleGroupsRequestRequestTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    {
        "WebACLArn": str,
        "WebACLLockToken": str,
    },
)

DeleteFirewallManagerRuleGroupsResponseTypeDef = TypedDict(
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    {
        "NextWebACLLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeletePermissionPolicyRequestRequestTypeDef = TypedDict(
    "DeletePermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteRegexPatternSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

DeleteWebACLRequestRequestTypeDef = TypedDict(
    "DeleteWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)

_RequiredDescribeManagedRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeManagedRuleGroupRequestRequestTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Scope": ScopeType,
    },
)
_OptionalDescribeManagedRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeManagedRuleGroupRequestRequestTypeDef",
    {
        "VersionName": str,
    },
    total=False,
)

class DescribeManagedRuleGroupRequestRequestTypeDef(
    _RequiredDescribeManagedRuleGroupRequestRequestTypeDef,
    _OptionalDescribeManagedRuleGroupRequestRequestTypeDef,
):
    pass

DescribeManagedRuleGroupResponseTypeDef = TypedDict(
    "DescribeManagedRuleGroupResponseTypeDef",
    {
        "VersionName": str,
        "SnsTopicArn": str,
        "Capacity": int,
        "Rules": List["RuleSummaryTypeDef"],
        "LabelNamespace": str,
        "AvailableLabels": List["LabelSummaryTypeDef"],
        "ConsumedLabels": List["LabelSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateWebACLRequestRequestTypeDef = TypedDict(
    "DisassociateWebACLRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ExcludedRuleTypeDef = TypedDict(
    "ExcludedRuleTypeDef",
    {
        "Name": str,
    },
)

FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "SingleHeader": "SingleHeaderTypeDef",
        "SingleQueryArgument": "SingleQueryArgumentTypeDef",
        "AllQueryArguments": Dict[str, Any],
        "UriPath": Dict[str, Any],
        "QueryString": Dict[str, Any],
        "Body": "BodyTypeDef",
        "Method": Dict[str, Any],
        "JsonBody": "JsonBodyTypeDef",
        "Headers": "HeadersTypeDef",
        "Cookies": "CookiesTypeDef",
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Behavior": FilterBehaviorType,
        "Requirement": FilterRequirementType,
        "Conditions": List["ConditionTypeDef"],
    },
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
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
    },
)

GenerateMobileSdkReleaseUrlRequestRequestTypeDef = TypedDict(
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "ReleaseVersion": str,
    },
)

GenerateMobileSdkReleaseUrlResponseTypeDef = TypedDict(
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    {
        "Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GeoMatchStatementTypeDef = TypedDict(
    "GeoMatchStatementTypeDef",
    {
        "CountryCodes": List[CountryCodeType],
        "ForwardedIPConfig": "ForwardedIPConfigTypeDef",
    },
    total=False,
)

GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
        "LockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetManagedRuleSetRequestRequestTypeDef = TypedDict(
    "GetManagedRuleSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetManagedRuleSetResponseTypeDef = TypedDict(
    "GetManagedRuleSetResponseTypeDef",
    {
        "ManagedRuleSet": "ManagedRuleSetTypeDef",
        "LockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMobileSdkReleaseRequestRequestTypeDef = TypedDict(
    "GetMobileSdkReleaseRequestRequestTypeDef",
    {
        "Platform": PlatformType,
        "ReleaseVersion": str,
    },
)

GetMobileSdkReleaseResponseTypeDef = TypedDict(
    "GetMobileSdkReleaseResponseTypeDef",
    {
        "MobileSdkRelease": "MobileSdkReleaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPermissionPolicyRequestRequestTypeDef = TypedDict(
    "GetPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetPermissionPolicyResponseTypeDef = TypedDict(
    "GetPermissionPolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRateBasedStatementManagedKeysRequestRequestTypeDef = TypedDict(
    "_RequiredGetRateBasedStatementManagedKeysRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "WebACLName": str,
        "WebACLId": str,
        "RuleName": str,
    },
)
_OptionalGetRateBasedStatementManagedKeysRequestRequestTypeDef = TypedDict(
    "_OptionalGetRateBasedStatementManagedKeysRequestRequestTypeDef",
    {
        "RuleGroupRuleName": str,
    },
    total=False,
)

class GetRateBasedStatementManagedKeysRequestRequestTypeDef(
    _RequiredGetRateBasedStatementManagedKeysRequestRequestTypeDef,
    _OptionalGetRateBasedStatementManagedKeysRequestRequestTypeDef,
):
    pass

GetRateBasedStatementManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    {
        "ManagedKeysIPV4": "RateBasedStatementManagedKeysIPSetTypeDef",
        "ManagedKeysIPV6": "RateBasedStatementManagedKeysIPSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegexPatternSetRequestRequestTypeDef = TypedDict(
    "GetRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "LockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleGroupRequestRequestTypeDef = TypedDict(
    "GetRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "ARN": str,
    },
    total=False,
)

GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "LockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSampledRequestsRequestRequestTypeDef = TypedDict(
    "GetSampledRequestsRequestRequestTypeDef",
    {
        "WebAclArn": str,
        "RuleMetricName": str,
        "Scope": ScopeType,
        "TimeWindow": "TimeWindowTypeDef",
        "MaxItems": int,
    },
)

GetSampledRequestsResponseTypeDef = TypedDict(
    "GetSampledRequestsResponseTypeDef",
    {
        "SampledRequests": List["SampledHTTPRequestTypeDef"],
        "PopulationSize": int,
        "TimeWindow": "TimeWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebACLForResourceRequestRequestTypeDef = TypedDict(
    "GetWebACLForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetWebACLForResourceResponseTypeDef = TypedDict(
    "GetWebACLForResourceResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebACLRequestRequestTypeDef = TypedDict(
    "GetWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
    },
)

GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "LockToken": str,
        "ApplicationIntegrationURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HTTPHeaderTypeDef = TypedDict(
    "HTTPHeaderTypeDef",
    {
        "Name": str,
        "Value": str,
    },
    total=False,
)

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

HeaderMatchPatternTypeDef = TypedDict(
    "HeaderMatchPatternTypeDef",
    {
        "All": Dict[str, Any],
        "IncludedHeaders": List[str],
        "ExcludedHeaders": List[str],
    },
    total=False,
)

HeadersTypeDef = TypedDict(
    "HeadersTypeDef",
    {
        "MatchPattern": "HeaderMatchPatternTypeDef",
        "MatchScope": MapMatchScopeType,
        "OversizeHandling": OversizeHandlingType,
    },
)

IPSetForwardedIPConfigTypeDef = TypedDict(
    "IPSetForwardedIPConfigTypeDef",
    {
        "HeaderName": str,
        "FallbackBehavior": FallbackBehaviorType,
        "Position": ForwardedIPPositionType,
    },
)

_RequiredIPSetReferenceStatementTypeDef = TypedDict(
    "_RequiredIPSetReferenceStatementTypeDef",
    {
        "ARN": str,
    },
)
_OptionalIPSetReferenceStatementTypeDef = TypedDict(
    "_OptionalIPSetReferenceStatementTypeDef",
    {
        "IPSetForwardedIPConfig": "IPSetForwardedIPConfigTypeDef",
    },
    total=False,
)

class IPSetReferenceStatementTypeDef(
    _RequiredIPSetReferenceStatementTypeDef, _OptionalIPSetReferenceStatementTypeDef
):
    pass

IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
    total=False,
)

_RequiredIPSetTypeDef = TypedDict(
    "_RequiredIPSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
    },
)
_OptionalIPSetTypeDef = TypedDict(
    "_OptionalIPSetTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class IPSetTypeDef(_RequiredIPSetTypeDef, _OptionalIPSetTypeDef):
    pass

ImmunityTimePropertyTypeDef = TypedDict(
    "ImmunityTimePropertyTypeDef",
    {
        "ImmunityTime": int,
    },
)

_RequiredJsonBodyTypeDef = TypedDict(
    "_RequiredJsonBodyTypeDef",
    {
        "MatchPattern": "JsonMatchPatternTypeDef",
        "MatchScope": JsonMatchScopeType,
    },
)
_OptionalJsonBodyTypeDef = TypedDict(
    "_OptionalJsonBodyTypeDef",
    {
        "InvalidFallbackBehavior": BodyParsingFallbackBehaviorType,
        "OversizeHandling": OversizeHandlingType,
    },
    total=False,
)

class JsonBodyTypeDef(_RequiredJsonBodyTypeDef, _OptionalJsonBodyTypeDef):
    pass

JsonMatchPatternTypeDef = TypedDict(
    "JsonMatchPatternTypeDef",
    {
        "All": Dict[str, Any],
        "IncludedPaths": List[str],
    },
    total=False,
)

LabelMatchStatementTypeDef = TypedDict(
    "LabelMatchStatementTypeDef",
    {
        "Scope": LabelMatchScopeType,
        "Key": str,
    },
)

LabelNameConditionTypeDef = TypedDict(
    "LabelNameConditionTypeDef",
    {
        "LabelName": str,
    },
)

LabelSummaryTypeDef = TypedDict(
    "LabelSummaryTypeDef",
    {
        "Name": str,
    },
    total=False,
)

LabelTypeDef = TypedDict(
    "LabelTypeDef",
    {
        "Name": str,
    },
)

_RequiredListAvailableManagedRuleGroupVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "Scope": ScopeType,
    },
)
_OptionalListAvailableManagedRuleGroupVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAvailableManagedRuleGroupVersionsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListAvailableManagedRuleGroupVersionsRequestRequestTypeDef(
    _RequiredListAvailableManagedRuleGroupVersionsRequestRequestTypeDef,
    _OptionalListAvailableManagedRuleGroupVersionsRequestRequestTypeDef,
):
    pass

ListAvailableManagedRuleGroupVersionsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    {
        "NextMarker": str,
        "Versions": List["ManagedRuleGroupVersionTypeDef"],
        "CurrentDefaultVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAvailableManagedRuleGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListAvailableManagedRuleGroupsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListAvailableManagedRuleGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListAvailableManagedRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListAvailableManagedRuleGroupsRequestRequestTypeDef(
    _RequiredListAvailableManagedRuleGroupsRequestRequestTypeDef,
    _OptionalListAvailableManagedRuleGroupsRequestRequestTypeDef,
):
    pass

ListAvailableManagedRuleGroupsResponseTypeDef = TypedDict(
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleGroups": List["ManagedRuleGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListIPSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListIPSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListIPSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListIPSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListIPSetsRequestRequestTypeDef(
    _RequiredListIPSetsRequestRequestTypeDef, _OptionalListIPSetsRequestRequestTypeDef
):
    pass

ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "NextMarker": str,
        "IPSets": List["IPSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListLoggingConfigurationsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListLoggingConfigurationsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListLoggingConfigurationsRequestRequestTypeDef(
    _RequiredListLoggingConfigurationsRequestRequestTypeDef,
    _OptionalListLoggingConfigurationsRequestRequestTypeDef,
):
    pass

ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List["LoggingConfigurationTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListManagedRuleSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListManagedRuleSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListManagedRuleSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListManagedRuleSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListManagedRuleSetsRequestRequestTypeDef(
    _RequiredListManagedRuleSetsRequestRequestTypeDef,
    _OptionalListManagedRuleSetsRequestRequestTypeDef,
):
    pass

ListManagedRuleSetsResponseTypeDef = TypedDict(
    "ListManagedRuleSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ManagedRuleSets": List["ManagedRuleSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListMobileSdkReleasesRequestRequestTypeDef = TypedDict(
    "_RequiredListMobileSdkReleasesRequestRequestTypeDef",
    {
        "Platform": PlatformType,
    },
)
_OptionalListMobileSdkReleasesRequestRequestTypeDef = TypedDict(
    "_OptionalListMobileSdkReleasesRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListMobileSdkReleasesRequestRequestTypeDef(
    _RequiredListMobileSdkReleasesRequestRequestTypeDef,
    _OptionalListMobileSdkReleasesRequestRequestTypeDef,
):
    pass

ListMobileSdkReleasesResponseTypeDef = TypedDict(
    "ListMobileSdkReleasesResponseTypeDef",
    {
        "ReleaseSummaries": List["ReleaseSummaryTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListRegexPatternSetsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListRegexPatternSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListRegexPatternSetsRequestRequestTypeDef(
    _RequiredListRegexPatternSetsRequestRequestTypeDef,
    _OptionalListRegexPatternSetsRequestRequestTypeDef,
):
    pass

ListRegexPatternSetsResponseTypeDef = TypedDict(
    "ListRegexPatternSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexPatternSets": List["RegexPatternSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourcesForWebACLRequestRequestTypeDef = TypedDict(
    "_RequiredListResourcesForWebACLRequestRequestTypeDef",
    {
        "WebACLArn": str,
    },
)
_OptionalListResourcesForWebACLRequestRequestTypeDef = TypedDict(
    "_OptionalListResourcesForWebACLRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeType,
    },
    total=False,
)

class ListResourcesForWebACLRequestRequestTypeDef(
    _RequiredListResourcesForWebACLRequestRequestTypeDef,
    _OptionalListResourcesForWebACLRequestRequestTypeDef,
):
    pass

ListResourcesForWebACLResponseTypeDef = TypedDict(
    "ListResourcesForWebACLResponseTypeDef",
    {
        "ResourceArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRuleGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListRuleGroupsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListRuleGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListRuleGroupsRequestRequestTypeDef(
    _RequiredListRuleGroupsRequestRequestTypeDef, _OptionalListRuleGroupsRequestRequestTypeDef
):
    pass

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["RuleGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListTagsForResourceRequestRequestTypeDef(
    _RequiredListTagsForResourceRequestRequestTypeDef,
    _OptionalListTagsForResourceRequestRequestTypeDef,
):
    pass

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "NextMarker": str,
        "TagInfoForResource": "TagInfoForResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListWebACLsRequestRequestTypeDef = TypedDict(
    "_RequiredListWebACLsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListWebACLsRequestRequestTypeDef = TypedDict(
    "_OptionalListWebACLsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListWebACLsRequestRequestTypeDef(
    _RequiredListWebACLsRequestRequestTypeDef, _OptionalListWebACLsRequestRequestTypeDef
):
    pass

ListWebACLsResponseTypeDef = TypedDict(
    "ListWebACLsResponseTypeDef",
    {
        "NextMarker": str,
        "WebACLs": List["WebACLSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLoggingConfigurationTypeDef = TypedDict(
    "_RequiredLoggingConfigurationTypeDef",
    {
        "ResourceArn": str,
        "LogDestinationConfigs": List[str],
    },
)
_OptionalLoggingConfigurationTypeDef = TypedDict(
    "_OptionalLoggingConfigurationTypeDef",
    {
        "RedactedFields": List["FieldToMatchTypeDef"],
        "ManagedByFirewallManager": bool,
        "LoggingFilter": "LoggingFilterTypeDef",
    },
    total=False,
)

class LoggingConfigurationTypeDef(
    _RequiredLoggingConfigurationTypeDef, _OptionalLoggingConfigurationTypeDef
):
    pass

LoggingFilterTypeDef = TypedDict(
    "LoggingFilterTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DefaultBehavior": FilterBehaviorType,
    },
)

ManagedRuleGroupConfigTypeDef = TypedDict(
    "ManagedRuleGroupConfigTypeDef",
    {
        "LoginPath": str,
        "PayloadType": PayloadTypeType,
        "UsernameField": "UsernameFieldTypeDef",
        "PasswordField": "PasswordFieldTypeDef",
    },
    total=False,
)

_RequiredManagedRuleGroupStatementTypeDef = TypedDict(
    "_RequiredManagedRuleGroupStatementTypeDef",
    {
        "VendorName": str,
        "Name": str,
    },
)
_OptionalManagedRuleGroupStatementTypeDef = TypedDict(
    "_OptionalManagedRuleGroupStatementTypeDef",
    {
        "Version": str,
        "ExcludedRules": List["ExcludedRuleTypeDef"],
        "ScopeDownStatement": "StatementTypeDef",
        "ManagedRuleGroupConfigs": List["ManagedRuleGroupConfigTypeDef"],
    },
    total=False,
)

class ManagedRuleGroupStatementTypeDef(
    _RequiredManagedRuleGroupStatementTypeDef, _OptionalManagedRuleGroupStatementTypeDef
):
    pass

ManagedRuleGroupSummaryTypeDef = TypedDict(
    "ManagedRuleGroupSummaryTypeDef",
    {
        "VendorName": str,
        "Name": str,
        "VersioningSupported": bool,
        "Description": str,
    },
    total=False,
)

ManagedRuleGroupVersionTypeDef = TypedDict(
    "ManagedRuleGroupVersionTypeDef",
    {
        "Name": str,
        "LastUpdateTimestamp": datetime,
    },
    total=False,
)

ManagedRuleSetSummaryTypeDef = TypedDict(
    "ManagedRuleSetSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
        "LabelNamespace": str,
    },
    total=False,
)

_RequiredManagedRuleSetTypeDef = TypedDict(
    "_RequiredManagedRuleSetTypeDef",
    {
        "Name": str,
        "Id": str,
        "ARN": str,
    },
)
_OptionalManagedRuleSetTypeDef = TypedDict(
    "_OptionalManagedRuleSetTypeDef",
    {
        "Description": str,
        "PublishedVersions": Dict[str, "ManagedRuleSetVersionTypeDef"],
        "RecommendedVersion": str,
        "LabelNamespace": str,
    },
    total=False,
)

class ManagedRuleSetTypeDef(_RequiredManagedRuleSetTypeDef, _OptionalManagedRuleSetTypeDef):
    pass

ManagedRuleSetVersionTypeDef = TypedDict(
    "ManagedRuleSetVersionTypeDef",
    {
        "AssociatedRuleGroupArn": str,
        "Capacity": int,
        "ForecastedLifetime": int,
        "PublishTimestamp": datetime,
        "LastUpdateTimestamp": datetime,
        "ExpiryTimestamp": datetime,
    },
    total=False,
)

MobileSdkReleaseTypeDef = TypedDict(
    "MobileSdkReleaseTypeDef",
    {
        "ReleaseVersion": str,
        "Timestamp": datetime,
        "ReleaseNotes": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

NotStatementTypeDef = TypedDict(
    "NotStatementTypeDef",
    {
        "Statement": "StatementTypeDef",
    },
)

OrStatementTypeDef = TypedDict(
    "OrStatementTypeDef",
    {
        "Statements": List["StatementTypeDef"],
    },
)

OverrideActionTypeDef = TypedDict(
    "OverrideActionTypeDef",
    {
        "Count": "CountActionTypeDef",
        "None": Dict[str, Any],
    },
    total=False,
)

PasswordFieldTypeDef = TypedDict(
    "PasswordFieldTypeDef",
    {
        "Identifier": str,
    },
)

PutLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutLoggingConfigurationRequestRequestTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
)

PutLoggingConfigurationResponseTypeDef = TypedDict(
    "PutLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutManagedRuleSetVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredPutManagedRuleSetVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
    },
)
_OptionalPutManagedRuleSetVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalPutManagedRuleSetVersionsRequestRequestTypeDef",
    {
        "RecommendedVersion": str,
        "VersionsToPublish": Dict[str, "VersionToPublishTypeDef"],
    },
    total=False,
)

class PutManagedRuleSetVersionsRequestRequestTypeDef(
    _RequiredPutManagedRuleSetVersionsRequestRequestTypeDef,
    _OptionalPutManagedRuleSetVersionsRequestRequestTypeDef,
):
    pass

PutManagedRuleSetVersionsResponseTypeDef = TypedDict(
    "PutManagedRuleSetVersionsResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPermissionPolicyRequestRequestTypeDef = TypedDict(
    "PutPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

RateBasedStatementManagedKeysIPSetTypeDef = TypedDict(
    "RateBasedStatementManagedKeysIPSetTypeDef",
    {
        "IPAddressVersion": IPAddressVersionType,
        "Addresses": List[str],
    },
    total=False,
)

_RequiredRateBasedStatementTypeDef = TypedDict(
    "_RequiredRateBasedStatementTypeDef",
    {
        "Limit": int,
        "AggregateKeyType": RateBasedStatementAggregateKeyTypeType,
    },
)
_OptionalRateBasedStatementTypeDef = TypedDict(
    "_OptionalRateBasedStatementTypeDef",
    {
        "ScopeDownStatement": "StatementTypeDef",
        "ForwardedIPConfig": "ForwardedIPConfigTypeDef",
    },
    total=False,
)

class RateBasedStatementTypeDef(
    _RequiredRateBasedStatementTypeDef, _OptionalRateBasedStatementTypeDef
):
    pass

RegexMatchStatementTypeDef = TypedDict(
    "RegexMatchStatementTypeDef",
    {
        "RegexString": str,
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

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
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
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

RegexTypeDef = TypedDict(
    "RegexTypeDef",
    {
        "RegexString": str,
    },
    total=False,
)

ReleaseSummaryTypeDef = TypedDict(
    "ReleaseSummaryTypeDef",
    {
        "ReleaseVersion": str,
        "Timestamp": datetime,
    },
    total=False,
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

RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "Block": "BlockActionTypeDef",
        "Allow": "AllowActionTypeDef",
        "Count": "CountActionTypeDef",
        "Captcha": "CaptchaActionTypeDef",
    },
    total=False,
)

_RequiredRuleGroupReferenceStatementTypeDef = TypedDict(
    "_RequiredRuleGroupReferenceStatementTypeDef",
    {
        "ARN": str,
    },
)
_OptionalRuleGroupReferenceStatementTypeDef = TypedDict(
    "_OptionalRuleGroupReferenceStatementTypeDef",
    {
        "ExcludedRules": List["ExcludedRuleTypeDef"],
    },
    total=False,
)

class RuleGroupReferenceStatementTypeDef(
    _RequiredRuleGroupReferenceStatementTypeDef, _OptionalRuleGroupReferenceStatementTypeDef
):
    pass

RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
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
    "_OptionalRuleGroupTypeDef",
    {
        "Description": str,
        "Rules": List["RuleTypeDef"],
        "LabelNamespace": str,
        "CustomResponseBodies": Dict[str, "CustomResponseBodyTypeDef"],
        "AvailableLabels": List["LabelSummaryTypeDef"],
        "ConsumedLabels": List["LabelSummaryTypeDef"],
    },
    total=False,
)

class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "Name": str,
        "Action": "RuleActionTypeDef",
    },
    total=False,
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "Name": str,
        "Priority": int,
        "Statement": "StatementTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Action": "RuleActionTypeDef",
        "OverrideAction": "OverrideActionTypeDef",
        "RuleLabels": List["LabelTypeDef"],
        "CaptchaConfig": "CaptchaConfigTypeDef",
    },
    total=False,
)

class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass

_RequiredSampledHTTPRequestTypeDef = TypedDict(
    "_RequiredSampledHTTPRequestTypeDef",
    {
        "Request": "HTTPRequestTypeDef",
        "Weight": int,
    },
)
_OptionalSampledHTTPRequestTypeDef = TypedDict(
    "_OptionalSampledHTTPRequestTypeDef",
    {
        "Timestamp": datetime,
        "Action": str,
        "RuleNameWithinRuleGroup": str,
        "RequestHeadersInserted": List["HTTPHeaderTypeDef"],
        "ResponseCodeSent": int,
        "Labels": List["LabelTypeDef"],
        "CaptchaResponse": "CaptchaResponseTypeDef",
    },
    total=False,
)

class SampledHTTPRequestTypeDef(
    _RequiredSampledHTTPRequestTypeDef, _OptionalSampledHTTPRequestTypeDef
):
    pass

SingleHeaderTypeDef = TypedDict(
    "SingleHeaderTypeDef",
    {
        "Name": str,
    },
)

SingleQueryArgumentTypeDef = TypedDict(
    "SingleQueryArgumentTypeDef",
    {
        "Name": str,
    },
)

SizeConstraintStatementTypeDef = TypedDict(
    "SizeConstraintStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "ComparisonOperator": ComparisonOperatorType,
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
        "RateBasedStatement": Dict[str, Any],
        "AndStatement": Dict[str, Any],
        "OrStatement": Dict[str, Any],
        "NotStatement": Dict[str, Any],
        "ManagedRuleGroupStatement": Dict[str, Any],
        "LabelMatchStatement": "LabelMatchStatementTypeDef",
        "RegexMatchStatement": "RegexMatchStatementTypeDef",
    },
    total=False,
)

TagInfoForResourceTypeDef = TypedDict(
    "TagInfoForResourceTypeDef",
    {
        "ResourceARN": str,
        "TagList": List["TagTypeDef"],
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TextTransformationTypeDef = TypedDict(
    "TextTransformationTypeDef",
    {
        "Priority": int,
        "Type": TextTransformationTypeType,
    },
)

TimeWindowTypeDef = TypedDict(
    "TimeWindowTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateIPSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "Addresses": List[str],
        "LockToken": str,
    },
)
_OptionalUpdateIPSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateIPSetRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateIPSetRequestRequestTypeDef(
    _RequiredUpdateIPSetRequestRequestTypeDef, _OptionalUpdateIPSetRequestRequestTypeDef
):
    pass

UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef = TypedDict(
    "UpdateManagedRuleSetVersionExpiryDateRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "LockToken": str,
        "VersionToExpire": str,
        "ExpiryTimestamp": Union[datetime, str],
    },
)

UpdateManagedRuleSetVersionExpiryDateResponseTypeDef = TypedDict(
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    {
        "ExpiringVersion": str,
        "ExpiryTimestamp": datetime,
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "RegularExpressionList": List["RegexTypeDef"],
        "LockToken": str,
    },
)
_OptionalUpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRegexPatternSetRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class UpdateRegexPatternSetRequestRequestTypeDef(
    _RequiredUpdateRegexPatternSetRequestRequestTypeDef,
    _OptionalUpdateRegexPatternSetRequestRequestTypeDef,
):
    pass

UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "LockToken": str,
    },
)
_OptionalUpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleGroupRequestRequestTypeDef",
    {
        "Description": str,
        "Rules": List["RuleTypeDef"],
        "CustomResponseBodies": Dict[str, "CustomResponseBodyTypeDef"],
    },
    total=False,
)

class UpdateRuleGroupRequestRequestTypeDef(
    _RequiredUpdateRuleGroupRequestRequestTypeDef, _OptionalUpdateRuleGroupRequestRequestTypeDef
):
    pass

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWebACLRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "Scope": ScopeType,
        "Id": str,
        "DefaultAction": "DefaultActionTypeDef",
        "VisibilityConfig": "VisibilityConfigTypeDef",
        "LockToken": str,
    },
)
_OptionalUpdateWebACLRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWebACLRequestRequestTypeDef",
    {
        "Description": str,
        "Rules": List["RuleTypeDef"],
        "CustomResponseBodies": Dict[str, "CustomResponseBodyTypeDef"],
        "CaptchaConfig": "CaptchaConfigTypeDef",
    },
    total=False,
)

class UpdateWebACLRequestRequestTypeDef(
    _RequiredUpdateWebACLRequestRequestTypeDef, _OptionalUpdateWebACLRequestRequestTypeDef
):
    pass

UpdateWebACLResponseTypeDef = TypedDict(
    "UpdateWebACLResponseTypeDef",
    {
        "NextLockToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UsernameFieldTypeDef = TypedDict(
    "UsernameFieldTypeDef",
    {
        "Identifier": str,
    },
)

VersionToPublishTypeDef = TypedDict(
    "VersionToPublishTypeDef",
    {
        "AssociatedRuleGroupArn": str,
        "ForecastedLifetime": int,
    },
    total=False,
)

VisibilityConfigTypeDef = TypedDict(
    "VisibilityConfigTypeDef",
    {
        "SampledRequestsEnabled": bool,
        "CloudWatchMetricsEnabled": bool,
        "MetricName": str,
    },
)

WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LockToken": str,
        "ARN": str,
    },
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
        "LabelNamespace": str,
        "CustomResponseBodies": Dict[str, "CustomResponseBodyTypeDef"],
        "CaptchaConfig": "CaptchaConfigTypeDef",
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
