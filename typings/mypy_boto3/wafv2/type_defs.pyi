"""
Type annotations for wafv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wafv2.type_defs import APIKeySummaryTypeDef

    data: APIKeySummaryTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ActionValueType,
    AssociatedResourceTypeType,
    BodyParsingFallbackBehaviorType,
    ComparisonOperatorType,
    CountryCodeType,
    FailureReasonType,
    FallbackBehaviorType,
    FilterBehaviorType,
    FilterRequirementType,
    ForwardedIPPositionType,
    InspectionLevelType,
    IPAddressVersionType,
    JsonMatchScopeType,
    LabelMatchScopeType,
    LogScopeType,
    MapMatchScopeType,
    OversizeHandlingType,
    PayloadTypeType,
    PlatformType,
    PositionalConstraintType,
    RateBasedStatementAggregateKeyTypeType,
    ResourceTypeType,
    ResponseContentTypeType,
    ScopeType,
    SensitivityLevelType,
    SizeInspectionLimitType,
    TextTransformationTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "APIKeySummaryTypeDef",
    "AWSManagedRulesACFPRuleSetTypeDef",
    "AWSManagedRulesATPRuleSetTypeDef",
    "AWSManagedRulesBotControlRuleSetTypeDef",
    "ActionConditionTypeDef",
    "AddressFieldTypeDef",
    "AllowActionTypeDef",
    "AndStatementTypeDef",
    "AssociateWebACLRequestRequestTypeDef",
    "AssociationConfigTypeDef",
    "BlockActionTypeDef",
    "BodyTypeDef",
    "ByteMatchStatementTypeDef",
    "CaptchaActionTypeDef",
    "CaptchaConfigTypeDef",
    "CaptchaResponseTypeDef",
    "ChallengeActionTypeDef",
    "ChallengeConfigTypeDef",
    "ChallengeResponseTypeDef",
    "CheckCapacityRequestRequestTypeDef",
    "CheckCapacityResponseTypeDef",
    "ConditionTypeDef",
    "CookieMatchPatternTypeDef",
    "CookiesTypeDef",
    "CountActionTypeDef",
    "CreateAPIKeyRequestRequestTypeDef",
    "CreateAPIKeyResponseTypeDef",
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
    "DeleteAPIKeyRequestRequestTypeDef",
    "DeleteFirewallManagerRuleGroupsRequestRequestTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeletePermissionPolicyRequestRequestTypeDef",
    "DeleteRegexPatternSetRequestRequestTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteWebACLRequestRequestTypeDef",
    "DescribeAllManagedProductsRequestRequestTypeDef",
    "DescribeAllManagedProductsResponseTypeDef",
    "DescribeManagedProductsByVendorRequestRequestTypeDef",
    "DescribeManagedProductsByVendorResponseTypeDef",
    "DescribeManagedRuleGroupRequestRequestTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "DisassociateWebACLRequestRequestTypeDef",
    "EmailFieldTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "FilterTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "FirewallManagerStatementTypeDef",
    "ForwardedIPConfigTypeDef",
    "GenerateMobileSdkReleaseUrlRequestRequestTypeDef",
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    "GeoMatchStatementTypeDef",
    "GetDecryptedAPIKeyRequestRequestTypeDef",
    "GetDecryptedAPIKeyResponseTypeDef",
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
    "HeaderOrderTypeDef",
    "HeadersTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "IPSetReferenceStatementTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "ImmunityTimePropertyTypeDef",
    "JA3FingerprintTypeDef",
    "JsonBodyTypeDef",
    "JsonMatchPatternTypeDef",
    "LabelMatchStatementTypeDef",
    "LabelNameConditionTypeDef",
    "LabelSummaryTypeDef",
    "LabelTypeDef",
    "ListAPIKeysRequestRequestTypeDef",
    "ListAPIKeysResponseTypeDef",
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
    "ManagedProductDescriptorTypeDef",
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
    "PhoneNumberFieldTypeDef",
    "PutLoggingConfigurationRequestRequestTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutManagedRuleSetVersionsRequestRequestTypeDef",
    "PutManagedRuleSetVersionsResponseTypeDef",
    "PutPermissionPolicyRequestRequestTypeDef",
    "RateBasedStatementCustomKeyTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "RateBasedStatementTypeDef",
    "RateLimitCookieTypeDef",
    "RateLimitHeaderTypeDef",
    "RateLimitLabelNamespaceTypeDef",
    "RateLimitQueryArgumentTypeDef",
    "RateLimitQueryStringTypeDef",
    "RateLimitUriPathTypeDef",
    "RegexMatchStatementTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexTypeDef",
    "ReleaseSummaryTypeDef",
    "RequestBodyAssociatedResourceTypeConfigTypeDef",
    "RequestInspectionACFPTypeDef",
    "RequestInspectionTypeDef",
    "ResponseInspectionBodyContainsTypeDef",
    "ResponseInspectionHeaderTypeDef",
    "ResponseInspectionJsonTypeDef",
    "ResponseInspectionStatusCodeTypeDef",
    "ResponseInspectionTypeDef",
    "ResponseMetadataTypeDef",
    "RuleActionOverrideTypeDef",
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

APIKeySummaryTypeDef = TypedDict(
    "APIKeySummaryTypeDef",
    {
        "TokenDomains": List[str],
        "APIKey": str,
        "CreationTimestamp": datetime,
        "Version": int,
    },
    total=False,
)

_RequiredAWSManagedRulesACFPRuleSetTypeDef = TypedDict(
    "_RequiredAWSManagedRulesACFPRuleSetTypeDef",
    {
        "CreationPath": str,
        "RegistrationPagePath": str,
        "RequestInspection": "RequestInspectionACFPTypeDef",
    },
)
_OptionalAWSManagedRulesACFPRuleSetTypeDef = TypedDict(
    "_OptionalAWSManagedRulesACFPRuleSetTypeDef",
    {
        "ResponseInspection": "ResponseInspectionTypeDef",
        "EnableRegexInPath": bool,
    },
    total=False,
)

class AWSManagedRulesACFPRuleSetTypeDef(
    _RequiredAWSManagedRulesACFPRuleSetTypeDef, _OptionalAWSManagedRulesACFPRuleSetTypeDef
):
    pass

_RequiredAWSManagedRulesATPRuleSetTypeDef = TypedDict(
    "_RequiredAWSManagedRulesATPRuleSetTypeDef",
    {
        "LoginPath": str,
    },
)
_OptionalAWSManagedRulesATPRuleSetTypeDef = TypedDict(
    "_OptionalAWSManagedRulesATPRuleSetTypeDef",
    {
        "RequestInspection": "RequestInspectionTypeDef",
        "ResponseInspection": "ResponseInspectionTypeDef",
        "EnableRegexInPath": bool,
    },
    total=False,
)

class AWSManagedRulesATPRuleSetTypeDef(
    _RequiredAWSManagedRulesATPRuleSetTypeDef, _OptionalAWSManagedRulesATPRuleSetTypeDef
):
    pass

_RequiredAWSManagedRulesBotControlRuleSetTypeDef = TypedDict(
    "_RequiredAWSManagedRulesBotControlRuleSetTypeDef",
    {
        "InspectionLevel": InspectionLevelType,
    },
)
_OptionalAWSManagedRulesBotControlRuleSetTypeDef = TypedDict(
    "_OptionalAWSManagedRulesBotControlRuleSetTypeDef",
    {
        "EnableMachineLearning": bool,
    },
    total=False,
)

class AWSManagedRulesBotControlRuleSetTypeDef(
    _RequiredAWSManagedRulesBotControlRuleSetTypeDef,
    _OptionalAWSManagedRulesBotControlRuleSetTypeDef,
):
    pass

ActionConditionTypeDef = TypedDict(
    "ActionConditionTypeDef",
    {
        "Action": ActionValueType,
    },
)

AddressFieldTypeDef = TypedDict(
    "AddressFieldTypeDef",
    {
        "Identifier": str,
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

AssociationConfigTypeDef = TypedDict(
    "AssociationConfigTypeDef",
    {
        "RequestBody": Dict[
            AssociatedResourceTypeType, "RequestBodyAssociatedResourceTypeConfigTypeDef"
        ],
    },
    total=False,
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

ChallengeActionTypeDef = TypedDict(
    "ChallengeActionTypeDef",
    {
        "CustomRequestHandling": "CustomRequestHandlingTypeDef",
    },
    total=False,
)

ChallengeConfigTypeDef = TypedDict(
    "ChallengeConfigTypeDef",
    {
        "ImmunityTimeProperty": "ImmunityTimePropertyTypeDef",
    },
    total=False,
)

ChallengeResponseTypeDef = TypedDict(
    "ChallengeResponseTypeDef",
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

CreateAPIKeyRequestRequestTypeDef = TypedDict(
    "CreateAPIKeyRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "TokenDomains": List[str],
    },
)

CreateAPIKeyResponseTypeDef = TypedDict(
    "CreateAPIKeyResponseTypeDef",
    {
        "APIKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "ChallengeConfig": "ChallengeConfigTypeDef",
        "TokenDomains": List[str],
        "AssociationConfig": "AssociationConfigTypeDef",
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

DeleteAPIKeyRequestRequestTypeDef = TypedDict(
    "DeleteAPIKeyRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "APIKey": str,
    },
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

_RequiredDeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalDeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "LogType": Literal["WAF_LOGS"],
        "LogScope": LogScopeType,
    },
    total=False,
)

class DeleteLoggingConfigurationRequestRequestTypeDef(
    _RequiredDeleteLoggingConfigurationRequestRequestTypeDef,
    _OptionalDeleteLoggingConfigurationRequestRequestTypeDef,
):
    pass

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

DescribeAllManagedProductsRequestRequestTypeDef = TypedDict(
    "DescribeAllManagedProductsRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)

DescribeAllManagedProductsResponseTypeDef = TypedDict(
    "DescribeAllManagedProductsResponseTypeDef",
    {
        "ManagedProducts": List["ManagedProductDescriptorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeManagedProductsByVendorRequestRequestTypeDef = TypedDict(
    "DescribeManagedProductsByVendorRequestRequestTypeDef",
    {
        "VendorName": str,
        "Scope": ScopeType,
    },
)

DescribeManagedProductsByVendorResponseTypeDef = TypedDict(
    "DescribeManagedProductsByVendorResponseTypeDef",
    {
        "ManagedProducts": List["ManagedProductDescriptorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

EmailFieldTypeDef = TypedDict(
    "EmailFieldTypeDef",
    {
        "Identifier": str,
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
        "HeaderOrder": "HeaderOrderTypeDef",
        "JA3Fingerprint": "JA3FingerprintTypeDef",
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

GetDecryptedAPIKeyRequestRequestTypeDef = TypedDict(
    "GetDecryptedAPIKeyRequestRequestTypeDef",
    {
        "Scope": ScopeType,
        "APIKey": str,
    },
)

GetDecryptedAPIKeyResponseTypeDef = TypedDict(
    "GetDecryptedAPIKeyResponseTypeDef",
    {
        "TokenDomains": List[str],
        "CreationTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredGetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetLoggingConfigurationRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
_OptionalGetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetLoggingConfigurationRequestRequestTypeDef",
    {
        "LogType": Literal["WAF_LOGS"],
        "LogScope": LogScopeType,
    },
    total=False,
)

class GetLoggingConfigurationRequestRequestTypeDef(
    _RequiredGetLoggingConfigurationRequestRequestTypeDef,
    _OptionalGetLoggingConfigurationRequestRequestTypeDef,
):
    pass

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

HeaderOrderTypeDef = TypedDict(
    "HeaderOrderTypeDef",
    {
        "OversizeHandling": OversizeHandlingType,
    },
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

JA3FingerprintTypeDef = TypedDict(
    "JA3FingerprintTypeDef",
    {
        "FallbackBehavior": FallbackBehaviorType,
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

_RequiredListAPIKeysRequestRequestTypeDef = TypedDict(
    "_RequiredListAPIKeysRequestRequestTypeDef",
    {
        "Scope": ScopeType,
    },
)
_OptionalListAPIKeysRequestRequestTypeDef = TypedDict(
    "_OptionalListAPIKeysRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

class ListAPIKeysRequestRequestTypeDef(
    _RequiredListAPIKeysRequestRequestTypeDef, _OptionalListAPIKeysRequestRequestTypeDef
):
    pass

ListAPIKeysResponseTypeDef = TypedDict(
    "ListAPIKeysResponseTypeDef",
    {
        "NextMarker": str,
        "APIKeySummaries": List["APIKeySummaryTypeDef"],
        "ApplicationIntegrationURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "LogScope": LogScopeType,
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
        "LogType": Literal["WAF_LOGS"],
        "LogScope": LogScopeType,
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

ManagedProductDescriptorTypeDef = TypedDict(
    "ManagedProductDescriptorTypeDef",
    {
        "VendorName": str,
        "ManagedRuleSetName": str,
        "ProductId": str,
        "ProductLink": str,
        "ProductTitle": str,
        "ProductDescription": str,
        "SnsTopicArn": str,
        "IsVersioningSupported": bool,
        "IsAdvancedManagedRuleSet": bool,
    },
    total=False,
)

ManagedRuleGroupConfigTypeDef = TypedDict(
    "ManagedRuleGroupConfigTypeDef",
    {
        "LoginPath": str,
        "PayloadType": PayloadTypeType,
        "UsernameField": "UsernameFieldTypeDef",
        "PasswordField": "PasswordFieldTypeDef",
        "AWSManagedRulesBotControlRuleSet": "AWSManagedRulesBotControlRuleSetTypeDef",
        "AWSManagedRulesATPRuleSet": "AWSManagedRulesATPRuleSetTypeDef",
        "AWSManagedRulesACFPRuleSet": "AWSManagedRulesACFPRuleSetTypeDef",
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
        "RuleActionOverrides": List["RuleActionOverrideTypeDef"],
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

PhoneNumberFieldTypeDef = TypedDict(
    "PhoneNumberFieldTypeDef",
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

RateBasedStatementCustomKeyTypeDef = TypedDict(
    "RateBasedStatementCustomKeyTypeDef",
    {
        "Header": "RateLimitHeaderTypeDef",
        "Cookie": "RateLimitCookieTypeDef",
        "QueryArgument": "RateLimitQueryArgumentTypeDef",
        "QueryString": "RateLimitQueryStringTypeDef",
        "HTTPMethod": Dict[str, Any],
        "ForwardedIP": Dict[str, Any],
        "IP": Dict[str, Any],
        "LabelNamespace": "RateLimitLabelNamespaceTypeDef",
        "UriPath": "RateLimitUriPathTypeDef",
    },
    total=False,
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
        "EvaluationWindowSec": int,
        "ScopeDownStatement": "StatementTypeDef",
        "ForwardedIPConfig": "ForwardedIPConfigTypeDef",
        "CustomKeys": List["RateBasedStatementCustomKeyTypeDef"],
    },
    total=False,
)

class RateBasedStatementTypeDef(
    _RequiredRateBasedStatementTypeDef, _OptionalRateBasedStatementTypeDef
):
    pass

RateLimitCookieTypeDef = TypedDict(
    "RateLimitCookieTypeDef",
    {
        "Name": str,
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

RateLimitHeaderTypeDef = TypedDict(
    "RateLimitHeaderTypeDef",
    {
        "Name": str,
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

RateLimitLabelNamespaceTypeDef = TypedDict(
    "RateLimitLabelNamespaceTypeDef",
    {
        "Namespace": str,
    },
)

RateLimitQueryArgumentTypeDef = TypedDict(
    "RateLimitQueryArgumentTypeDef",
    {
        "Name": str,
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

RateLimitQueryStringTypeDef = TypedDict(
    "RateLimitQueryStringTypeDef",
    {
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

RateLimitUriPathTypeDef = TypedDict(
    "RateLimitUriPathTypeDef",
    {
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)

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

RequestBodyAssociatedResourceTypeConfigTypeDef = TypedDict(
    "RequestBodyAssociatedResourceTypeConfigTypeDef",
    {
        "DefaultSizeInspectionLimit": SizeInspectionLimitType,
    },
)

_RequiredRequestInspectionACFPTypeDef = TypedDict(
    "_RequiredRequestInspectionACFPTypeDef",
    {
        "PayloadType": PayloadTypeType,
    },
)
_OptionalRequestInspectionACFPTypeDef = TypedDict(
    "_OptionalRequestInspectionACFPTypeDef",
    {
        "UsernameField": "UsernameFieldTypeDef",
        "PasswordField": "PasswordFieldTypeDef",
        "EmailField": "EmailFieldTypeDef",
        "PhoneNumberFields": List["PhoneNumberFieldTypeDef"],
        "AddressFields": List["AddressFieldTypeDef"],
    },
    total=False,
)

class RequestInspectionACFPTypeDef(
    _RequiredRequestInspectionACFPTypeDef, _OptionalRequestInspectionACFPTypeDef
):
    pass

RequestInspectionTypeDef = TypedDict(
    "RequestInspectionTypeDef",
    {
        "PayloadType": PayloadTypeType,
        "UsernameField": "UsernameFieldTypeDef",
        "PasswordField": "PasswordFieldTypeDef",
    },
)

ResponseInspectionBodyContainsTypeDef = TypedDict(
    "ResponseInspectionBodyContainsTypeDef",
    {
        "SuccessStrings": List[str],
        "FailureStrings": List[str],
    },
)

ResponseInspectionHeaderTypeDef = TypedDict(
    "ResponseInspectionHeaderTypeDef",
    {
        "Name": str,
        "SuccessValues": List[str],
        "FailureValues": List[str],
    },
)

ResponseInspectionJsonTypeDef = TypedDict(
    "ResponseInspectionJsonTypeDef",
    {
        "Identifier": str,
        "SuccessValues": List[str],
        "FailureValues": List[str],
    },
)

ResponseInspectionStatusCodeTypeDef = TypedDict(
    "ResponseInspectionStatusCodeTypeDef",
    {
        "SuccessCodes": List[int],
        "FailureCodes": List[int],
    },
)

ResponseInspectionTypeDef = TypedDict(
    "ResponseInspectionTypeDef",
    {
        "StatusCode": "ResponseInspectionStatusCodeTypeDef",
        "Header": "ResponseInspectionHeaderTypeDef",
        "BodyContains": "ResponseInspectionBodyContainsTypeDef",
        "Json": "ResponseInspectionJsonTypeDef",
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

RuleActionOverrideTypeDef = TypedDict(
    "RuleActionOverrideTypeDef",
    {
        "Name": str,
        "ActionToUse": "RuleActionTypeDef",
    },
)

RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "Block": "BlockActionTypeDef",
        "Allow": "AllowActionTypeDef",
        "Count": "CountActionTypeDef",
        "Captcha": "CaptchaActionTypeDef",
        "Challenge": "ChallengeActionTypeDef",
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
        "RuleActionOverrides": List["RuleActionOverrideTypeDef"],
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
        "ChallengeConfig": "ChallengeConfigTypeDef",
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
        "ChallengeResponse": "ChallengeResponseTypeDef",
        "OverriddenAction": str,
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

_RequiredSqliMatchStatementTypeDef = TypedDict(
    "_RequiredSqliMatchStatementTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformations": List["TextTransformationTypeDef"],
    },
)
_OptionalSqliMatchStatementTypeDef = TypedDict(
    "_OptionalSqliMatchStatementTypeDef",
    {
        "SensitivityLevel": SensitivityLevelType,
    },
    total=False,
)

class SqliMatchStatementTypeDef(
    _RequiredSqliMatchStatementTypeDef, _OptionalSqliMatchStatementTypeDef
):
    pass

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
        "ChallengeConfig": "ChallengeConfigTypeDef",
        "TokenDomains": List[str],
        "AssociationConfig": "AssociationConfigTypeDef",
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
        "ChallengeConfig": "ChallengeConfigTypeDef",
        "TokenDomains": List[str],
        "AssociationConfig": "AssociationConfigTypeDef",
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
