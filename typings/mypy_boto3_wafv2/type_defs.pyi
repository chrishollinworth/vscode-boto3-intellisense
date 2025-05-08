"""
Type annotations for wafv2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_wafv2.type_defs import APIKeySummaryTypeDef

    data: APIKeySummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    ActionValueType,
    AssociatedResourceTypeType,
    BodyParsingFallbackBehaviorType,
    ComparisonOperatorType,
    CountryCodeType,
    DataProtectionActionType,
    FailureReasonType,
    FallbackBehaviorType,
    FieldToProtectTypeType,
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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "APIKeySummaryTypeDef",
    "AWSManagedRulesACFPRuleSetOutputTypeDef",
    "AWSManagedRulesACFPRuleSetTypeDef",
    "AWSManagedRulesACFPRuleSetUnionTypeDef",
    "AWSManagedRulesATPRuleSetOutputTypeDef",
    "AWSManagedRulesATPRuleSetTypeDef",
    "AWSManagedRulesATPRuleSetUnionTypeDef",
    "AWSManagedRulesBotControlRuleSetTypeDef",
    "ActionConditionTypeDef",
    "AddressFieldTypeDef",
    "AllowActionOutputTypeDef",
    "AllowActionTypeDef",
    "AllowActionUnionTypeDef",
    "AndStatementOutputTypeDef",
    "AndStatementTypeDef",
    "AndStatementUnionTypeDef",
    "AssociateWebACLRequestTypeDef",
    "AssociationConfigOutputTypeDef",
    "AssociationConfigTypeDef",
    "AssociationConfigUnionTypeDef",
    "BlobTypeDef",
    "BlockActionOutputTypeDef",
    "BlockActionTypeDef",
    "BlockActionUnionTypeDef",
    "BodyTypeDef",
    "ByteMatchStatementOutputTypeDef",
    "ByteMatchStatementTypeDef",
    "ByteMatchStatementUnionTypeDef",
    "CaptchaActionOutputTypeDef",
    "CaptchaActionTypeDef",
    "CaptchaActionUnionTypeDef",
    "CaptchaConfigTypeDef",
    "CaptchaResponseTypeDef",
    "ChallengeActionOutputTypeDef",
    "ChallengeActionTypeDef",
    "ChallengeActionUnionTypeDef",
    "ChallengeConfigTypeDef",
    "ChallengeResponseTypeDef",
    "CheckCapacityRequestTypeDef",
    "CheckCapacityResponseTypeDef",
    "ConditionTypeDef",
    "CookieMatchPatternOutputTypeDef",
    "CookieMatchPatternTypeDef",
    "CookieMatchPatternUnionTypeDef",
    "CookiesOutputTypeDef",
    "CookiesTypeDef",
    "CookiesUnionTypeDef",
    "CountActionOutputTypeDef",
    "CountActionTypeDef",
    "CountActionUnionTypeDef",
    "CreateAPIKeyRequestTypeDef",
    "CreateAPIKeyResponseTypeDef",
    "CreateIPSetRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRegexPatternSetRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupRequestTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateWebACLRequestTypeDef",
    "CreateWebACLResponseTypeDef",
    "CustomHTTPHeaderTypeDef",
    "CustomRequestHandlingOutputTypeDef",
    "CustomRequestHandlingTypeDef",
    "CustomRequestHandlingUnionTypeDef",
    "CustomResponseBodyTypeDef",
    "CustomResponseOutputTypeDef",
    "CustomResponseTypeDef",
    "CustomResponseUnionTypeDef",
    "DataProtectionConfigOutputTypeDef",
    "DataProtectionConfigTypeDef",
    "DataProtectionConfigUnionTypeDef",
    "DataProtectionOutputTypeDef",
    "DataProtectionTypeDef",
    "DefaultActionOutputTypeDef",
    "DefaultActionTypeDef",
    "DefaultActionUnionTypeDef",
    "DeleteAPIKeyRequestTypeDef",
    "DeleteFirewallManagerRuleGroupsRequestTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "DeleteIPSetRequestTypeDef",
    "DeleteLoggingConfigurationRequestTypeDef",
    "DeletePermissionPolicyRequestTypeDef",
    "DeleteRegexPatternSetRequestTypeDef",
    "DeleteRuleGroupRequestTypeDef",
    "DeleteWebACLRequestTypeDef",
    "DescribeAllManagedProductsRequestTypeDef",
    "DescribeAllManagedProductsResponseTypeDef",
    "DescribeManagedProductsByVendorRequestTypeDef",
    "DescribeManagedProductsByVendorResponseTypeDef",
    "DescribeManagedRuleGroupRequestTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "DisassociateWebACLRequestTypeDef",
    "EmailFieldTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchOutputTypeDef",
    "FieldToMatchTypeDef",
    "FieldToMatchUnionTypeDef",
    "FieldToProtectOutputTypeDef",
    "FieldToProtectTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "FirewallManagerStatementTypeDef",
    "ForwardedIPConfigTypeDef",
    "GenerateMobileSdkReleaseUrlRequestTypeDef",
    "GenerateMobileSdkReleaseUrlResponseTypeDef",
    "GeoMatchStatementOutputTypeDef",
    "GeoMatchStatementTypeDef",
    "GeoMatchStatementUnionTypeDef",
    "GetDecryptedAPIKeyRequestTypeDef",
    "GetDecryptedAPIKeyResponseTypeDef",
    "GetIPSetRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationRequestTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetManagedRuleSetRequestTypeDef",
    "GetManagedRuleSetResponseTypeDef",
    "GetMobileSdkReleaseRequestTypeDef",
    "GetMobileSdkReleaseResponseTypeDef",
    "GetPermissionPolicyRequestTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedStatementManagedKeysRequestTypeDef",
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    "GetRegexPatternSetRequestTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupRequestTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetSampledRequestsRequestTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetWebACLForResourceRequestTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLRequestTypeDef",
    "GetWebACLResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "HeaderMatchPatternOutputTypeDef",
    "HeaderMatchPatternTypeDef",
    "HeaderMatchPatternUnionTypeDef",
    "HeaderOrderTypeDef",
    "HeadersOutputTypeDef",
    "HeadersTypeDef",
    "HeadersUnionTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "IPSetReferenceStatementTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "ImmunityTimePropertyTypeDef",
    "JA3FingerprintTypeDef",
    "JA4FingerprintTypeDef",
    "JsonBodyOutputTypeDef",
    "JsonBodyTypeDef",
    "JsonBodyUnionTypeDef",
    "JsonMatchPatternOutputTypeDef",
    "JsonMatchPatternTypeDef",
    "JsonMatchPatternUnionTypeDef",
    "LabelMatchStatementTypeDef",
    "LabelNameConditionTypeDef",
    "LabelSummaryTypeDef",
    "LabelTypeDef",
    "ListAPIKeysRequestTypeDef",
    "ListAPIKeysResponseTypeDef",
    "ListAvailableManagedRuleGroupVersionsRequestTypeDef",
    "ListAvailableManagedRuleGroupVersionsResponseTypeDef",
    "ListAvailableManagedRuleGroupsRequestTypeDef",
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    "ListIPSetsRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsRequestTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListManagedRuleSetsRequestTypeDef",
    "ListManagedRuleSetsResponseTypeDef",
    "ListMobileSdkReleasesRequestTypeDef",
    "ListMobileSdkReleasesResponseTypeDef",
    "ListRegexPatternSetsRequestTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListResourcesForWebACLRequestTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "ListRuleGroupsRequestTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsRequestTypeDef",
    "ListWebACLsResponseTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "LoggingConfigurationUnionTypeDef",
    "LoggingFilterOutputTypeDef",
    "LoggingFilterTypeDef",
    "ManagedProductDescriptorTypeDef",
    "ManagedRuleGroupConfigOutputTypeDef",
    "ManagedRuleGroupConfigTypeDef",
    "ManagedRuleGroupConfigUnionTypeDef",
    "ManagedRuleGroupStatementOutputTypeDef",
    "ManagedRuleGroupStatementTypeDef",
    "ManagedRuleGroupStatementUnionTypeDef",
    "ManagedRuleGroupSummaryTypeDef",
    "ManagedRuleGroupVersionTypeDef",
    "ManagedRuleSetSummaryTypeDef",
    "ManagedRuleSetTypeDef",
    "ManagedRuleSetVersionTypeDef",
    "MobileSdkReleaseTypeDef",
    "NotStatementOutputTypeDef",
    "NotStatementTypeDef",
    "NotStatementUnionTypeDef",
    "OrStatementOutputTypeDef",
    "OrStatementTypeDef",
    "OrStatementUnionTypeDef",
    "OverrideActionOutputTypeDef",
    "OverrideActionTypeDef",
    "OverrideActionUnionTypeDef",
    "PasswordFieldTypeDef",
    "PhoneNumberFieldTypeDef",
    "PutLoggingConfigurationRequestTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutManagedRuleSetVersionsRequestTypeDef",
    "PutManagedRuleSetVersionsResponseTypeDef",
    "PutPermissionPolicyRequestTypeDef",
    "RateBasedStatementCustomKeyOutputTypeDef",
    "RateBasedStatementCustomKeyTypeDef",
    "RateBasedStatementCustomKeyUnionTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "RateBasedStatementOutputTypeDef",
    "RateBasedStatementTypeDef",
    "RateBasedStatementUnionTypeDef",
    "RateLimitCookieOutputTypeDef",
    "RateLimitCookieTypeDef",
    "RateLimitCookieUnionTypeDef",
    "RateLimitHeaderOutputTypeDef",
    "RateLimitHeaderTypeDef",
    "RateLimitHeaderUnionTypeDef",
    "RateLimitJA3FingerprintTypeDef",
    "RateLimitJA4FingerprintTypeDef",
    "RateLimitLabelNamespaceTypeDef",
    "RateLimitQueryArgumentOutputTypeDef",
    "RateLimitQueryArgumentTypeDef",
    "RateLimitQueryArgumentUnionTypeDef",
    "RateLimitQueryStringOutputTypeDef",
    "RateLimitQueryStringTypeDef",
    "RateLimitQueryStringUnionTypeDef",
    "RateLimitUriPathOutputTypeDef",
    "RateLimitUriPathTypeDef",
    "RateLimitUriPathUnionTypeDef",
    "RegexMatchStatementOutputTypeDef",
    "RegexMatchStatementTypeDef",
    "RegexMatchStatementUnionTypeDef",
    "RegexPatternSetReferenceStatementOutputTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "RegexPatternSetReferenceStatementUnionTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexTypeDef",
    "ReleaseSummaryTypeDef",
    "RequestBodyAssociatedResourceTypeConfigTypeDef",
    "RequestInspectionACFPOutputTypeDef",
    "RequestInspectionACFPTypeDef",
    "RequestInspectionACFPUnionTypeDef",
    "RequestInspectionTypeDef",
    "ResponseInspectionBodyContainsOutputTypeDef",
    "ResponseInspectionBodyContainsTypeDef",
    "ResponseInspectionBodyContainsUnionTypeDef",
    "ResponseInspectionHeaderOutputTypeDef",
    "ResponseInspectionHeaderTypeDef",
    "ResponseInspectionHeaderUnionTypeDef",
    "ResponseInspectionJsonOutputTypeDef",
    "ResponseInspectionJsonTypeDef",
    "ResponseInspectionJsonUnionTypeDef",
    "ResponseInspectionOutputTypeDef",
    "ResponseInspectionStatusCodeOutputTypeDef",
    "ResponseInspectionStatusCodeTypeDef",
    "ResponseInspectionStatusCodeUnionTypeDef",
    "ResponseInspectionTypeDef",
    "ResponseInspectionUnionTypeDef",
    "ResponseMetadataTypeDef",
    "RuleActionOutputTypeDef",
    "RuleActionOverrideOutputTypeDef",
    "RuleActionOverrideTypeDef",
    "RuleActionOverrideUnionTypeDef",
    "RuleActionTypeDef",
    "RuleActionUnionTypeDef",
    "RuleGroupReferenceStatementOutputTypeDef",
    "RuleGroupReferenceStatementTypeDef",
    "RuleGroupReferenceStatementUnionTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleOutputTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "RuleUnionTypeDef",
    "SampledHTTPRequestTypeDef",
    "SingleHeaderTypeDef",
    "SingleQueryArgumentTypeDef",
    "SizeConstraintStatementOutputTypeDef",
    "SizeConstraintStatementTypeDef",
    "SizeConstraintStatementUnionTypeDef",
    "SqliMatchStatementOutputTypeDef",
    "SqliMatchStatementTypeDef",
    "SqliMatchStatementUnionTypeDef",
    "StatementOutputTypeDef",
    "StatementTypeDef",
    "StatementUnionTypeDef",
    "TagInfoForResourceTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TextTransformationTypeDef",
    "TimeWindowOutputTypeDef",
    "TimeWindowTypeDef",
    "TimeWindowUnionTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateIPSetRequestTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateRequestTypeDef",
    "UpdateManagedRuleSetVersionExpiryDateResponseTypeDef",
    "UpdateRegexPatternSetRequestTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupRequestTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateWebACLRequestTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UriFragmentTypeDef",
    "UsernameFieldTypeDef",
    "VersionToPublishTypeDef",
    "VisibilityConfigTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "XssMatchStatementOutputTypeDef",
    "XssMatchStatementTypeDef",
    "XssMatchStatementUnionTypeDef",
)

class APIKeySummaryTypeDef(TypedDict):
    TokenDomains: NotRequired[List[str]]
    APIKey: NotRequired[str]
    CreationTimestamp: NotRequired[datetime]
    Version: NotRequired[int]

class AWSManagedRulesBotControlRuleSetTypeDef(TypedDict):
    InspectionLevel: InspectionLevelType
    EnableMachineLearning: NotRequired[bool]

class ActionConditionTypeDef(TypedDict):
    Action: ActionValueType

class AddressFieldTypeDef(TypedDict):
    Identifier: str

class AndStatementOutputTypeDef(TypedDict):
    Statements: List[Dict[str, Any]]

class AndStatementTypeDef(TypedDict):
    Statements: Sequence[Mapping[str, Any]]

class AssociateWebACLRequestTypeDef(TypedDict):
    WebACLArn: str
    ResourceArn: str

class RequestBodyAssociatedResourceTypeConfigTypeDef(TypedDict):
    DefaultSizeInspectionLimit: SizeInspectionLimitType

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BodyTypeDef(TypedDict):
    OversizeHandling: NotRequired[OversizeHandlingType]

TextTransformationTypeDef = TypedDict(
    "TextTransformationTypeDef",
    {
        "Priority": int,
        "Type": TextTransformationTypeType,
    },
)

class ImmunityTimePropertyTypeDef(TypedDict):
    ImmunityTime: int

class CaptchaResponseTypeDef(TypedDict):
    ResponseCode: NotRequired[int]
    SolveTimestamp: NotRequired[int]
    FailureReason: NotRequired[FailureReasonType]

class ChallengeResponseTypeDef(TypedDict):
    ResponseCode: NotRequired[int]
    SolveTimestamp: NotRequired[int]
    FailureReason: NotRequired[FailureReasonType]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class LabelNameConditionTypeDef(TypedDict):
    LabelName: str

class CookieMatchPatternOutputTypeDef(TypedDict):
    All: NotRequired[Dict[str, Any]]
    IncludedCookies: NotRequired[List[str]]
    ExcludedCookies: NotRequired[List[str]]

class CookieMatchPatternTypeDef(TypedDict):
    All: NotRequired[Mapping[str, Any]]
    IncludedCookies: NotRequired[Sequence[str]]
    ExcludedCookies: NotRequired[Sequence[str]]

class CreateAPIKeyRequestTypeDef(TypedDict):
    Scope: ScopeType
    TokenDomains: Sequence[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class IPSetSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    Description: NotRequired[str]
    LockToken: NotRequired[str]
    ARN: NotRequired[str]

class RegexTypeDef(TypedDict):
    RegexString: NotRequired[str]

class RegexPatternSetSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    Description: NotRequired[str]
    LockToken: NotRequired[str]
    ARN: NotRequired[str]

class CustomResponseBodyTypeDef(TypedDict):
    ContentType: ResponseContentTypeType
    Content: str

class VisibilityConfigTypeDef(TypedDict):
    SampledRequestsEnabled: bool
    CloudWatchMetricsEnabled: bool
    MetricName: str

class RuleGroupSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    Description: NotRequired[str]
    LockToken: NotRequired[str]
    ARN: NotRequired[str]

class WebACLSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    Description: NotRequired[str]
    LockToken: NotRequired[str]
    ARN: NotRequired[str]

class CustomHTTPHeaderTypeDef(TypedDict):
    Name: str
    Value: str

class FieldToProtectOutputTypeDef(TypedDict):
    FieldType: FieldToProtectTypeType
    FieldKeys: NotRequired[List[str]]

class FieldToProtectTypeDef(TypedDict):
    FieldType: FieldToProtectTypeType
    FieldKeys: NotRequired[Sequence[str]]

class DeleteAPIKeyRequestTypeDef(TypedDict):
    Scope: ScopeType
    APIKey: str

class DeleteFirewallManagerRuleGroupsRequestTypeDef(TypedDict):
    WebACLArn: str
    WebACLLockToken: str

class DeleteIPSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str

class DeleteLoggingConfigurationRequestTypeDef(TypedDict):
    ResourceArn: str
    LogType: NotRequired[Literal["WAF_LOGS"]]
    LogScope: NotRequired[LogScopeType]

class DeletePermissionPolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class DeleteRegexPatternSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str

class DeleteRuleGroupRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str

class DeleteWebACLRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str

class DescribeAllManagedProductsRequestTypeDef(TypedDict):
    Scope: ScopeType

class ManagedProductDescriptorTypeDef(TypedDict):
    VendorName: NotRequired[str]
    ManagedRuleSetName: NotRequired[str]
    ProductId: NotRequired[str]
    ProductLink: NotRequired[str]
    ProductTitle: NotRequired[str]
    ProductDescription: NotRequired[str]
    SnsTopicArn: NotRequired[str]
    IsVersioningSupported: NotRequired[bool]
    IsAdvancedManagedRuleSet: NotRequired[bool]

class DescribeManagedProductsByVendorRequestTypeDef(TypedDict):
    VendorName: str
    Scope: ScopeType

class DescribeManagedRuleGroupRequestTypeDef(TypedDict):
    VendorName: str
    Name: str
    Scope: ScopeType
    VersionName: NotRequired[str]

class LabelSummaryTypeDef(TypedDict):
    Name: NotRequired[str]

class DisassociateWebACLRequestTypeDef(TypedDict):
    ResourceArn: str

class EmailFieldTypeDef(TypedDict):
    Identifier: str

class ExcludedRuleTypeDef(TypedDict):
    Name: str

class HeaderOrderTypeDef(TypedDict):
    OversizeHandling: OversizeHandlingType

class JA3FingerprintTypeDef(TypedDict):
    FallbackBehavior: FallbackBehaviorType

class JA4FingerprintTypeDef(TypedDict):
    FallbackBehavior: FallbackBehaviorType

class SingleHeaderTypeDef(TypedDict):
    Name: str

class SingleQueryArgumentTypeDef(TypedDict):
    Name: str

class UriFragmentTypeDef(TypedDict):
    FallbackBehavior: NotRequired[FallbackBehaviorType]

class ForwardedIPConfigTypeDef(TypedDict):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType

class GenerateMobileSdkReleaseUrlRequestTypeDef(TypedDict):
    Platform: PlatformType
    ReleaseVersion: str

class GetDecryptedAPIKeyRequestTypeDef(TypedDict):
    Scope: ScopeType
    APIKey: str

class GetIPSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str

class IPSetTypeDef(TypedDict):
    Name: str
    Id: str
    ARN: str
    IPAddressVersion: IPAddressVersionType
    Addresses: List[str]
    Description: NotRequired[str]

class GetLoggingConfigurationRequestTypeDef(TypedDict):
    ResourceArn: str
    LogType: NotRequired[Literal["WAF_LOGS"]]
    LogScope: NotRequired[LogScopeType]

class GetManagedRuleSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str

class GetMobileSdkReleaseRequestTypeDef(TypedDict):
    Platform: PlatformType
    ReleaseVersion: str

class GetPermissionPolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class GetRateBasedStatementManagedKeysRequestTypeDef(TypedDict):
    Scope: ScopeType
    WebACLName: str
    WebACLId: str
    RuleName: str
    RuleGroupRuleName: NotRequired[str]

class RateBasedStatementManagedKeysIPSetTypeDef(TypedDict):
    IPAddressVersion: NotRequired[IPAddressVersionType]
    Addresses: NotRequired[List[str]]

class GetRegexPatternSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str

class GetRuleGroupRequestTypeDef(TypedDict):
    Name: NotRequired[str]
    Scope: NotRequired[ScopeType]
    Id: NotRequired[str]
    ARN: NotRequired[str]

class TimeWindowOutputTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime

class GetWebACLForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class GetWebACLRequestTypeDef(TypedDict):
    Name: NotRequired[str]
    Scope: NotRequired[ScopeType]
    Id: NotRequired[str]
    ARN: NotRequired[str]

class HTTPHeaderTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

class HeaderMatchPatternOutputTypeDef(TypedDict):
    All: NotRequired[Dict[str, Any]]
    IncludedHeaders: NotRequired[List[str]]
    ExcludedHeaders: NotRequired[List[str]]

class HeaderMatchPatternTypeDef(TypedDict):
    All: NotRequired[Mapping[str, Any]]
    IncludedHeaders: NotRequired[Sequence[str]]
    ExcludedHeaders: NotRequired[Sequence[str]]

class IPSetForwardedIPConfigTypeDef(TypedDict):
    HeaderName: str
    FallbackBehavior: FallbackBehaviorType
    Position: ForwardedIPPositionType

class JsonMatchPatternOutputTypeDef(TypedDict):
    All: NotRequired[Dict[str, Any]]
    IncludedPaths: NotRequired[List[str]]

class JsonMatchPatternTypeDef(TypedDict):
    All: NotRequired[Mapping[str, Any]]
    IncludedPaths: NotRequired[Sequence[str]]

class LabelMatchStatementTypeDef(TypedDict):
    Scope: LabelMatchScopeType
    Key: str

class LabelTypeDef(TypedDict):
    Name: str

class ListAPIKeysRequestTypeDef(TypedDict):
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListAvailableManagedRuleGroupVersionsRequestTypeDef(TypedDict):
    VendorName: str
    Name: str
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ManagedRuleGroupVersionTypeDef(TypedDict):
    Name: NotRequired[str]
    LastUpdateTimestamp: NotRequired[datetime]

class ListAvailableManagedRuleGroupsRequestTypeDef(TypedDict):
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ManagedRuleGroupSummaryTypeDef(TypedDict):
    VendorName: NotRequired[str]
    Name: NotRequired[str]
    VersioningSupported: NotRequired[bool]
    Description: NotRequired[str]

class ListIPSetsRequestTypeDef(TypedDict):
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListLoggingConfigurationsRequestTypeDef(TypedDict):
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]
    LogScope: NotRequired[LogScopeType]

class ListManagedRuleSetsRequestTypeDef(TypedDict):
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ManagedRuleSetSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    Description: NotRequired[str]
    LockToken: NotRequired[str]
    ARN: NotRequired[str]
    LabelNamespace: NotRequired[str]

class ListMobileSdkReleasesRequestTypeDef(TypedDict):
    Platform: PlatformType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ReleaseSummaryTypeDef(TypedDict):
    ReleaseVersion: NotRequired[str]
    Timestamp: NotRequired[datetime]

class ListRegexPatternSetsRequestTypeDef(TypedDict):
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListResourcesForWebACLRequestTypeDef(TypedDict):
    WebACLArn: str
    ResourceType: NotRequired[ResourceTypeType]

class ListRuleGroupsRequestTypeDef(TypedDict):
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListWebACLsRequestTypeDef(TypedDict):
    Scope: ScopeType
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class PasswordFieldTypeDef(TypedDict):
    Identifier: str

class UsernameFieldTypeDef(TypedDict):
    Identifier: str

class ManagedRuleSetVersionTypeDef(TypedDict):
    AssociatedRuleGroupArn: NotRequired[str]
    Capacity: NotRequired[int]
    ForecastedLifetime: NotRequired[int]
    PublishTimestamp: NotRequired[datetime]
    LastUpdateTimestamp: NotRequired[datetime]
    ExpiryTimestamp: NotRequired[datetime]

class NotStatementOutputTypeDef(TypedDict):
    Statement: Dict[str, Any]

class NotStatementTypeDef(TypedDict):
    Statement: Mapping[str, Any]

class OrStatementOutputTypeDef(TypedDict):
    Statements: List[Dict[str, Any]]

class OrStatementTypeDef(TypedDict):
    Statements: Sequence[Mapping[str, Any]]

class PhoneNumberFieldTypeDef(TypedDict):
    Identifier: str

class VersionToPublishTypeDef(TypedDict):
    AssociatedRuleGroupArn: NotRequired[str]
    ForecastedLifetime: NotRequired[int]

class PutPermissionPolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    Policy: str

class RateLimitJA3FingerprintTypeDef(TypedDict):
    FallbackBehavior: FallbackBehaviorType

class RateLimitJA4FingerprintTypeDef(TypedDict):
    FallbackBehavior: FallbackBehaviorType

class RateLimitLabelNamespaceTypeDef(TypedDict):
    Namespace: str

class ResponseInspectionBodyContainsOutputTypeDef(TypedDict):
    SuccessStrings: List[str]
    FailureStrings: List[str]

class ResponseInspectionBodyContainsTypeDef(TypedDict):
    SuccessStrings: Sequence[str]
    FailureStrings: Sequence[str]

class ResponseInspectionHeaderOutputTypeDef(TypedDict):
    Name: str
    SuccessValues: List[str]
    FailureValues: List[str]

class ResponseInspectionHeaderTypeDef(TypedDict):
    Name: str
    SuccessValues: Sequence[str]
    FailureValues: Sequence[str]

class ResponseInspectionJsonOutputTypeDef(TypedDict):
    Identifier: str
    SuccessValues: List[str]
    FailureValues: List[str]

class ResponseInspectionJsonTypeDef(TypedDict):
    Identifier: str
    SuccessValues: Sequence[str]
    FailureValues: Sequence[str]

class ResponseInspectionStatusCodeOutputTypeDef(TypedDict):
    SuccessCodes: List[int]
    FailureCodes: List[int]

class ResponseInspectionStatusCodeTypeDef(TypedDict):
    SuccessCodes: Sequence[int]
    FailureCodes: Sequence[int]

TimestampTypeDef = Union[datetime, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateIPSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    Addresses: Sequence[str]
    LockToken: str
    Description: NotRequired[str]

AndStatementUnionTypeDef = Union[AndStatementTypeDef, AndStatementOutputTypeDef]

class AssociationConfigOutputTypeDef(TypedDict):
    RequestBody: NotRequired[
        Dict[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfigTypeDef]
    ]

class AssociationConfigTypeDef(TypedDict):
    RequestBody: NotRequired[
        Mapping[AssociatedResourceTypeType, RequestBodyAssociatedResourceTypeConfigTypeDef]
    ]

class RateLimitCookieOutputTypeDef(TypedDict):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitCookieTypeDef(TypedDict):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]

class RateLimitHeaderOutputTypeDef(TypedDict):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitHeaderTypeDef(TypedDict):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]

class RateLimitQueryArgumentOutputTypeDef(TypedDict):
    Name: str
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitQueryArgumentTypeDef(TypedDict):
    Name: str
    TextTransformations: Sequence[TextTransformationTypeDef]

class RateLimitQueryStringOutputTypeDef(TypedDict):
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitQueryStringTypeDef(TypedDict):
    TextTransformations: Sequence[TextTransformationTypeDef]

class RateLimitUriPathOutputTypeDef(TypedDict):
    TextTransformations: List[TextTransformationTypeDef]

class RateLimitUriPathTypeDef(TypedDict):
    TextTransformations: Sequence[TextTransformationTypeDef]

class CaptchaConfigTypeDef(TypedDict):
    ImmunityTimeProperty: NotRequired[ImmunityTimePropertyTypeDef]

class ChallengeConfigTypeDef(TypedDict):
    ImmunityTimeProperty: NotRequired[ImmunityTimePropertyTypeDef]

class CheckCapacityResponseTypeDef(TypedDict):
    Capacity: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAPIKeyResponseTypeDef(TypedDict):
    APIKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFirewallManagerRuleGroupsResponseTypeDef(TypedDict):
    NextWebACLLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMobileSdkReleaseUrlResponseTypeDef(TypedDict):
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDecryptedAPIKeyResponseTypeDef(TypedDict):
    TokenDomains: List[str]
    CreationTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionPolicyResponseTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAPIKeysResponseTypeDef(TypedDict):
    NextMarker: str
    APIKeySummaries: List[APIKeySummaryTypeDef]
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesForWebACLResponseTypeDef(TypedDict):
    ResourceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutManagedRuleSetVersionsResponseTypeDef(TypedDict):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIPSetResponseTypeDef(TypedDict):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateManagedRuleSetVersionExpiryDateResponseTypeDef(TypedDict):
    ExpiringVersion: str
    ExpiryTimestamp: datetime
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexPatternSetResponseTypeDef(TypedDict):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupResponseTypeDef(TypedDict):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebACLResponseTypeDef(TypedDict):
    NextLockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConditionTypeDef(TypedDict):
    ActionCondition: NotRequired[ActionConditionTypeDef]
    LabelNameCondition: NotRequired[LabelNameConditionTypeDef]

class CookiesOutputTypeDef(TypedDict):
    MatchPattern: CookieMatchPatternOutputTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

CookieMatchPatternUnionTypeDef = Union[CookieMatchPatternTypeDef, CookieMatchPatternOutputTypeDef]

class CreateIPSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    IPAddressVersion: IPAddressVersionType
    Addresses: Sequence[str]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class MobileSdkReleaseTypeDef(TypedDict):
    ReleaseVersion: NotRequired[str]
    Timestamp: NotRequired[datetime]
    ReleaseNotes: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class TagInfoForResourceTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    TagList: NotRequired[List[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateIPSetResponseTypeDef(TypedDict):
    Summary: IPSetSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIPSetsResponseTypeDef(TypedDict):
    NextMarker: str
    IPSets: List[IPSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegexPatternSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    RegularExpressionList: Sequence[RegexTypeDef]
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class RegexPatternSetTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    ARN: NotRequired[str]
    Description: NotRequired[str]
    RegularExpressionList: NotRequired[List[RegexTypeDef]]

class UpdateRegexPatternSetRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    RegularExpressionList: Sequence[RegexTypeDef]
    LockToken: str
    Description: NotRequired[str]

class CreateRegexPatternSetResponseTypeDef(TypedDict):
    Summary: RegexPatternSetSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRegexPatternSetsResponseTypeDef(TypedDict):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupResponseTypeDef(TypedDict):
    Summary: RuleGroupSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRuleGroupsResponseTypeDef(TypedDict):
    NextMarker: str
    RuleGroups: List[RuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWebACLResponseTypeDef(TypedDict):
    Summary: WebACLSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebACLsResponseTypeDef(TypedDict):
    NextMarker: str
    WebACLs: List[WebACLSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomRequestHandlingOutputTypeDef(TypedDict):
    InsertHeaders: List[CustomHTTPHeaderTypeDef]

class CustomRequestHandlingTypeDef(TypedDict):
    InsertHeaders: Sequence[CustomHTTPHeaderTypeDef]

class CustomResponseOutputTypeDef(TypedDict):
    ResponseCode: int
    CustomResponseBodyKey: NotRequired[str]
    ResponseHeaders: NotRequired[List[CustomHTTPHeaderTypeDef]]

class CustomResponseTypeDef(TypedDict):
    ResponseCode: int
    CustomResponseBodyKey: NotRequired[str]
    ResponseHeaders: NotRequired[Sequence[CustomHTTPHeaderTypeDef]]

class DataProtectionOutputTypeDef(TypedDict):
    Field: FieldToProtectOutputTypeDef
    Action: DataProtectionActionType
    ExcludeRuleMatchDetails: NotRequired[bool]
    ExcludeRateBasedDetails: NotRequired[bool]

class DataProtectionTypeDef(TypedDict):
    Field: FieldToProtectTypeDef
    Action: DataProtectionActionType
    ExcludeRuleMatchDetails: NotRequired[bool]
    ExcludeRateBasedDetails: NotRequired[bool]

class DescribeAllManagedProductsResponseTypeDef(TypedDict):
    ManagedProducts: List[ManagedProductDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeManagedProductsByVendorResponseTypeDef(TypedDict):
    ManagedProducts: List[ManagedProductDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GeoMatchStatementOutputTypeDef(TypedDict):
    CountryCodes: NotRequired[List[CountryCodeType]]
    ForwardedIPConfig: NotRequired[ForwardedIPConfigTypeDef]

class GeoMatchStatementTypeDef(TypedDict):
    CountryCodes: NotRequired[Sequence[CountryCodeType]]
    ForwardedIPConfig: NotRequired[ForwardedIPConfigTypeDef]

class GetIPSetResponseTypeDef(TypedDict):
    IPSet: IPSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedStatementManagedKeysResponseTypeDef(TypedDict):
    ManagedKeysIPV4: RateBasedStatementManagedKeysIPSetTypeDef
    ManagedKeysIPV6: RateBasedStatementManagedKeysIPSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HTTPRequestTypeDef(TypedDict):
    ClientIP: NotRequired[str]
    Country: NotRequired[str]
    URI: NotRequired[str]
    Method: NotRequired[str]
    HTTPVersion: NotRequired[str]
    Headers: NotRequired[List[HTTPHeaderTypeDef]]

class HeadersOutputTypeDef(TypedDict):
    MatchPattern: HeaderMatchPatternOutputTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

HeaderMatchPatternUnionTypeDef = Union[HeaderMatchPatternTypeDef, HeaderMatchPatternOutputTypeDef]

class IPSetReferenceStatementTypeDef(TypedDict):
    ARN: str
    IPSetForwardedIPConfig: NotRequired[IPSetForwardedIPConfigTypeDef]

class JsonBodyOutputTypeDef(TypedDict):
    MatchPattern: JsonMatchPatternOutputTypeDef
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: NotRequired[BodyParsingFallbackBehaviorType]
    OversizeHandling: NotRequired[OversizeHandlingType]

JsonMatchPatternUnionTypeDef = Union[JsonMatchPatternTypeDef, JsonMatchPatternOutputTypeDef]

class ListAvailableManagedRuleGroupVersionsResponseTypeDef(TypedDict):
    NextMarker: str
    Versions: List[ManagedRuleGroupVersionTypeDef]
    CurrentDefaultVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAvailableManagedRuleGroupsResponseTypeDef(TypedDict):
    NextMarker: str
    ManagedRuleGroups: List[ManagedRuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListManagedRuleSetsResponseTypeDef(TypedDict):
    NextMarker: str
    ManagedRuleSets: List[ManagedRuleSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMobileSdkReleasesResponseTypeDef(TypedDict):
    ReleaseSummaries: List[ReleaseSummaryTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RequestInspectionTypeDef(TypedDict):
    PayloadType: PayloadTypeType
    UsernameField: UsernameFieldTypeDef
    PasswordField: PasswordFieldTypeDef

class ManagedRuleSetTypeDef(TypedDict):
    Name: str
    Id: str
    ARN: str
    Description: NotRequired[str]
    PublishedVersions: NotRequired[Dict[str, ManagedRuleSetVersionTypeDef]]
    RecommendedVersion: NotRequired[str]
    LabelNamespace: NotRequired[str]

NotStatementUnionTypeDef = Union[NotStatementTypeDef, NotStatementOutputTypeDef]
OrStatementUnionTypeDef = Union[OrStatementTypeDef, OrStatementOutputTypeDef]

class RequestInspectionACFPOutputTypeDef(TypedDict):
    PayloadType: PayloadTypeType
    UsernameField: NotRequired[UsernameFieldTypeDef]
    PasswordField: NotRequired[PasswordFieldTypeDef]
    EmailField: NotRequired[EmailFieldTypeDef]
    PhoneNumberFields: NotRequired[List[PhoneNumberFieldTypeDef]]
    AddressFields: NotRequired[List[AddressFieldTypeDef]]

class RequestInspectionACFPTypeDef(TypedDict):
    PayloadType: PayloadTypeType
    UsernameField: NotRequired[UsernameFieldTypeDef]
    PasswordField: NotRequired[PasswordFieldTypeDef]
    EmailField: NotRequired[EmailFieldTypeDef]
    PhoneNumberFields: NotRequired[Sequence[PhoneNumberFieldTypeDef]]
    AddressFields: NotRequired[Sequence[AddressFieldTypeDef]]

class PutManagedRuleSetVersionsRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    RecommendedVersion: NotRequired[str]
    VersionsToPublish: NotRequired[Mapping[str, VersionToPublishTypeDef]]

ResponseInspectionBodyContainsUnionTypeDef = Union[
    ResponseInspectionBodyContainsTypeDef, ResponseInspectionBodyContainsOutputTypeDef
]
ResponseInspectionHeaderUnionTypeDef = Union[
    ResponseInspectionHeaderTypeDef, ResponseInspectionHeaderOutputTypeDef
]
ResponseInspectionJsonUnionTypeDef = Union[
    ResponseInspectionJsonTypeDef, ResponseInspectionJsonOutputTypeDef
]

class ResponseInspectionOutputTypeDef(TypedDict):
    StatusCode: NotRequired[ResponseInspectionStatusCodeOutputTypeDef]
    Header: NotRequired[ResponseInspectionHeaderOutputTypeDef]
    BodyContains: NotRequired[ResponseInspectionBodyContainsOutputTypeDef]
    Json: NotRequired[ResponseInspectionJsonOutputTypeDef]

ResponseInspectionStatusCodeUnionTypeDef = Union[
    ResponseInspectionStatusCodeTypeDef, ResponseInspectionStatusCodeOutputTypeDef
]

class TimeWindowTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class UpdateManagedRuleSetVersionExpiryDateRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    LockToken: str
    VersionToExpire: str
    ExpiryTimestamp: TimestampTypeDef

AssociationConfigUnionTypeDef = Union[AssociationConfigTypeDef, AssociationConfigOutputTypeDef]
RateLimitCookieUnionTypeDef = Union[RateLimitCookieTypeDef, RateLimitCookieOutputTypeDef]
RateLimitHeaderUnionTypeDef = Union[RateLimitHeaderTypeDef, RateLimitHeaderOutputTypeDef]
RateLimitQueryArgumentUnionTypeDef = Union[
    RateLimitQueryArgumentTypeDef, RateLimitQueryArgumentOutputTypeDef
]
RateLimitQueryStringUnionTypeDef = Union[
    RateLimitQueryStringTypeDef, RateLimitQueryStringOutputTypeDef
]

class RateBasedStatementCustomKeyOutputTypeDef(TypedDict):
    Header: NotRequired[RateLimitHeaderOutputTypeDef]
    Cookie: NotRequired[RateLimitCookieOutputTypeDef]
    QueryArgument: NotRequired[RateLimitQueryArgumentOutputTypeDef]
    QueryString: NotRequired[RateLimitQueryStringOutputTypeDef]
    HTTPMethod: NotRequired[Dict[str, Any]]
    ForwardedIP: NotRequired[Dict[str, Any]]
    IP: NotRequired[Dict[str, Any]]
    LabelNamespace: NotRequired[RateLimitLabelNamespaceTypeDef]
    UriPath: NotRequired[RateLimitUriPathOutputTypeDef]
    JA3Fingerprint: NotRequired[RateLimitJA3FingerprintTypeDef]
    JA4Fingerprint: NotRequired[RateLimitJA4FingerprintTypeDef]

RateLimitUriPathUnionTypeDef = Union[RateLimitUriPathTypeDef, RateLimitUriPathOutputTypeDef]

class FilterOutputTypeDef(TypedDict):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: List[ConditionTypeDef]

class FilterTypeDef(TypedDict):
    Behavior: FilterBehaviorType
    Requirement: FilterRequirementType
    Conditions: Sequence[ConditionTypeDef]

class CookiesTypeDef(TypedDict):
    MatchPattern: CookieMatchPatternUnionTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

class GetMobileSdkReleaseResponseTypeDef(TypedDict):
    MobileSdkRelease: MobileSdkReleaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    NextMarker: str
    TagInfoForResource: TagInfoForResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegexPatternSetResponseTypeDef(TypedDict):
    RegexPatternSet: RegexPatternSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AllowActionOutputTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[CustomRequestHandlingOutputTypeDef]

class CaptchaActionOutputTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[CustomRequestHandlingOutputTypeDef]

class ChallengeActionOutputTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[CustomRequestHandlingOutputTypeDef]

class CountActionOutputTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[CustomRequestHandlingOutputTypeDef]

CustomRequestHandlingUnionTypeDef = Union[
    CustomRequestHandlingTypeDef, CustomRequestHandlingOutputTypeDef
]

class BlockActionOutputTypeDef(TypedDict):
    CustomResponse: NotRequired[CustomResponseOutputTypeDef]

CustomResponseUnionTypeDef = Union[CustomResponseTypeDef, CustomResponseOutputTypeDef]

class DataProtectionConfigOutputTypeDef(TypedDict):
    DataProtections: List[DataProtectionOutputTypeDef]

class DataProtectionConfigTypeDef(TypedDict):
    DataProtections: Sequence[DataProtectionTypeDef]

GeoMatchStatementUnionTypeDef = Union[GeoMatchStatementTypeDef, GeoMatchStatementOutputTypeDef]

class SampledHTTPRequestTypeDef(TypedDict):
    Request: HTTPRequestTypeDef
    Weight: int
    Timestamp: NotRequired[datetime]
    Action: NotRequired[str]
    RuleNameWithinRuleGroup: NotRequired[str]
    RequestHeadersInserted: NotRequired[List[HTTPHeaderTypeDef]]
    ResponseCodeSent: NotRequired[int]
    Labels: NotRequired[List[LabelTypeDef]]
    CaptchaResponse: NotRequired[CaptchaResponseTypeDef]
    ChallengeResponse: NotRequired[ChallengeResponseTypeDef]
    OverriddenAction: NotRequired[str]

class HeadersTypeDef(TypedDict):
    MatchPattern: HeaderMatchPatternUnionTypeDef
    MatchScope: MapMatchScopeType
    OversizeHandling: OversizeHandlingType

class FieldToMatchOutputTypeDef(TypedDict):
    SingleHeader: NotRequired[SingleHeaderTypeDef]
    SingleQueryArgument: NotRequired[SingleQueryArgumentTypeDef]
    AllQueryArguments: NotRequired[Dict[str, Any]]
    UriPath: NotRequired[Dict[str, Any]]
    QueryString: NotRequired[Dict[str, Any]]
    Body: NotRequired[BodyTypeDef]
    Method: NotRequired[Dict[str, Any]]
    JsonBody: NotRequired[JsonBodyOutputTypeDef]
    Headers: NotRequired[HeadersOutputTypeDef]
    Cookies: NotRequired[CookiesOutputTypeDef]
    HeaderOrder: NotRequired[HeaderOrderTypeDef]
    JA3Fingerprint: NotRequired[JA3FingerprintTypeDef]
    JA4Fingerprint: NotRequired[JA4FingerprintTypeDef]
    UriFragment: NotRequired[UriFragmentTypeDef]

class JsonBodyTypeDef(TypedDict):
    MatchPattern: JsonMatchPatternUnionTypeDef
    MatchScope: JsonMatchScopeType
    InvalidFallbackBehavior: NotRequired[BodyParsingFallbackBehaviorType]
    OversizeHandling: NotRequired[OversizeHandlingType]

class GetManagedRuleSetResponseTypeDef(TypedDict):
    ManagedRuleSet: ManagedRuleSetTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

RequestInspectionACFPUnionTypeDef = Union[
    RequestInspectionACFPTypeDef, RequestInspectionACFPOutputTypeDef
]

class AWSManagedRulesACFPRuleSetOutputTypeDef(TypedDict):
    CreationPath: str
    RegistrationPagePath: str
    RequestInspection: RequestInspectionACFPOutputTypeDef
    ResponseInspection: NotRequired[ResponseInspectionOutputTypeDef]
    EnableRegexInPath: NotRequired[bool]

class AWSManagedRulesATPRuleSetOutputTypeDef(TypedDict):
    LoginPath: str
    RequestInspection: NotRequired[RequestInspectionTypeDef]
    ResponseInspection: NotRequired[ResponseInspectionOutputTypeDef]
    EnableRegexInPath: NotRequired[bool]

class ResponseInspectionTypeDef(TypedDict):
    StatusCode: NotRequired[ResponseInspectionStatusCodeUnionTypeDef]
    Header: NotRequired[ResponseInspectionHeaderUnionTypeDef]
    BodyContains: NotRequired[ResponseInspectionBodyContainsUnionTypeDef]
    Json: NotRequired[ResponseInspectionJsonUnionTypeDef]

TimeWindowUnionTypeDef = Union[TimeWindowTypeDef, TimeWindowOutputTypeDef]

class RateBasedStatementOutputTypeDef(TypedDict):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: NotRequired[int]
    ScopeDownStatement: NotRequired[Dict[str, Any]]
    ForwardedIPConfig: NotRequired[ForwardedIPConfigTypeDef]
    CustomKeys: NotRequired[List[RateBasedStatementCustomKeyOutputTypeDef]]

class RateBasedStatementCustomKeyTypeDef(TypedDict):
    Header: NotRequired[RateLimitHeaderUnionTypeDef]
    Cookie: NotRequired[RateLimitCookieUnionTypeDef]
    QueryArgument: NotRequired[RateLimitQueryArgumentUnionTypeDef]
    QueryString: NotRequired[RateLimitQueryStringUnionTypeDef]
    HTTPMethod: NotRequired[Mapping[str, Any]]
    ForwardedIP: NotRequired[Mapping[str, Any]]
    IP: NotRequired[Mapping[str, Any]]
    LabelNamespace: NotRequired[RateLimitLabelNamespaceTypeDef]
    UriPath: NotRequired[RateLimitUriPathUnionTypeDef]
    JA3Fingerprint: NotRequired[RateLimitJA3FingerprintTypeDef]
    JA4Fingerprint: NotRequired[RateLimitJA4FingerprintTypeDef]

class LoggingFilterOutputTypeDef(TypedDict):
    Filters: List[FilterOutputTypeDef]
    DefaultBehavior: FilterBehaviorType

class LoggingFilterTypeDef(TypedDict):
    Filters: Sequence[FilterTypeDef]
    DefaultBehavior: FilterBehaviorType

CookiesUnionTypeDef = Union[CookiesTypeDef, CookiesOutputTypeDef]
OverrideActionOutputTypeDef = TypedDict(
    "OverrideActionOutputTypeDef",
    {
        "Count": NotRequired[CountActionOutputTypeDef],
        "None": NotRequired[Dict[str, Any]],
    },
)

class AllowActionTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[CustomRequestHandlingUnionTypeDef]

class CaptchaActionTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[CustomRequestHandlingUnionTypeDef]

class ChallengeActionTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[CustomRequestHandlingUnionTypeDef]

class CountActionTypeDef(TypedDict):
    CustomRequestHandling: NotRequired[CustomRequestHandlingUnionTypeDef]

class DefaultActionOutputTypeDef(TypedDict):
    Block: NotRequired[BlockActionOutputTypeDef]
    Allow: NotRequired[AllowActionOutputTypeDef]

class RuleActionOutputTypeDef(TypedDict):
    Block: NotRequired[BlockActionOutputTypeDef]
    Allow: NotRequired[AllowActionOutputTypeDef]
    Count: NotRequired[CountActionOutputTypeDef]
    Captcha: NotRequired[CaptchaActionOutputTypeDef]
    Challenge: NotRequired[ChallengeActionOutputTypeDef]

class BlockActionTypeDef(TypedDict):
    CustomResponse: NotRequired[CustomResponseUnionTypeDef]

DataProtectionConfigUnionTypeDef = Union[
    DataProtectionConfigTypeDef, DataProtectionConfigOutputTypeDef
]

class GetSampledRequestsResponseTypeDef(TypedDict):
    SampledRequests: List[SampledHTTPRequestTypeDef]
    PopulationSize: int
    TimeWindow: TimeWindowOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

HeadersUnionTypeDef = Union[HeadersTypeDef, HeadersOutputTypeDef]

class ByteMatchStatementOutputTypeDef(TypedDict):
    SearchString: bytes
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]
    PositionalConstraint: PositionalConstraintType

class RegexMatchStatementOutputTypeDef(TypedDict):
    RegexString: str
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]

class RegexPatternSetReferenceStatementOutputTypeDef(TypedDict):
    ARN: str
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]

class SizeConstraintStatementOutputTypeDef(TypedDict):
    FieldToMatch: FieldToMatchOutputTypeDef
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: List[TextTransformationTypeDef]

class SqliMatchStatementOutputTypeDef(TypedDict):
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]
    SensitivityLevel: NotRequired[SensitivityLevelType]

class XssMatchStatementOutputTypeDef(TypedDict):
    FieldToMatch: FieldToMatchOutputTypeDef
    TextTransformations: List[TextTransformationTypeDef]

JsonBodyUnionTypeDef = Union[JsonBodyTypeDef, JsonBodyOutputTypeDef]

class ManagedRuleGroupConfigOutputTypeDef(TypedDict):
    LoginPath: NotRequired[str]
    PayloadType: NotRequired[PayloadTypeType]
    UsernameField: NotRequired[UsernameFieldTypeDef]
    PasswordField: NotRequired[PasswordFieldTypeDef]
    AWSManagedRulesBotControlRuleSet: NotRequired[AWSManagedRulesBotControlRuleSetTypeDef]
    AWSManagedRulesATPRuleSet: NotRequired[AWSManagedRulesATPRuleSetOutputTypeDef]
    AWSManagedRulesACFPRuleSet: NotRequired[AWSManagedRulesACFPRuleSetOutputTypeDef]

ResponseInspectionUnionTypeDef = Union[ResponseInspectionTypeDef, ResponseInspectionOutputTypeDef]

class GetSampledRequestsRequestTypeDef(TypedDict):
    WebAclArn: str
    RuleMetricName: str
    Scope: ScopeType
    TimeWindow: TimeWindowUnionTypeDef
    MaxItems: int

RateBasedStatementCustomKeyUnionTypeDef = Union[
    RateBasedStatementCustomKeyTypeDef, RateBasedStatementCustomKeyOutputTypeDef
]

class LoggingConfigurationOutputTypeDef(TypedDict):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: NotRequired[List[FieldToMatchOutputTypeDef]]
    ManagedByFirewallManager: NotRequired[bool]
    LoggingFilter: NotRequired[LoggingFilterOutputTypeDef]
    LogType: NotRequired[Literal["WAF_LOGS"]]
    LogScope: NotRequired[LogScopeType]

AllowActionUnionTypeDef = Union[AllowActionTypeDef, AllowActionOutputTypeDef]
CaptchaActionUnionTypeDef = Union[CaptchaActionTypeDef, CaptchaActionOutputTypeDef]
ChallengeActionUnionTypeDef = Union[ChallengeActionTypeDef, ChallengeActionOutputTypeDef]
CountActionUnionTypeDef = Union[CountActionTypeDef, CountActionOutputTypeDef]

class RuleActionOverrideOutputTypeDef(TypedDict):
    Name: str
    ActionToUse: RuleActionOutputTypeDef

class RuleSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Action: NotRequired[RuleActionOutputTypeDef]

BlockActionUnionTypeDef = Union[BlockActionTypeDef, BlockActionOutputTypeDef]

class DefaultActionTypeDef(TypedDict):
    Block: NotRequired[BlockActionTypeDef]
    Allow: NotRequired[AllowActionTypeDef]

class FieldToMatchTypeDef(TypedDict):
    SingleHeader: NotRequired[SingleHeaderTypeDef]
    SingleQueryArgument: NotRequired[SingleQueryArgumentTypeDef]
    AllQueryArguments: NotRequired[Mapping[str, Any]]
    UriPath: NotRequired[Mapping[str, Any]]
    QueryString: NotRequired[Mapping[str, Any]]
    Body: NotRequired[BodyTypeDef]
    Method: NotRequired[Mapping[str, Any]]
    JsonBody: NotRequired[JsonBodyUnionTypeDef]
    Headers: NotRequired[HeadersUnionTypeDef]
    Cookies: NotRequired[CookiesUnionTypeDef]
    HeaderOrder: NotRequired[HeaderOrderTypeDef]
    JA3Fingerprint: NotRequired[JA3FingerprintTypeDef]
    JA4Fingerprint: NotRequired[JA4FingerprintTypeDef]
    UriFragment: NotRequired[UriFragmentTypeDef]

class AWSManagedRulesACFPRuleSetTypeDef(TypedDict):
    CreationPath: str
    RegistrationPagePath: str
    RequestInspection: RequestInspectionACFPUnionTypeDef
    ResponseInspection: NotRequired[ResponseInspectionUnionTypeDef]
    EnableRegexInPath: NotRequired[bool]

class AWSManagedRulesATPRuleSetTypeDef(TypedDict):
    LoginPath: str
    RequestInspection: NotRequired[RequestInspectionTypeDef]
    ResponseInspection: NotRequired[ResponseInspectionUnionTypeDef]
    EnableRegexInPath: NotRequired[bool]

class RateBasedStatementTypeDef(TypedDict):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyTypeType
    EvaluationWindowSec: NotRequired[int]
    ScopeDownStatement: NotRequired[Mapping[str, Any]]
    ForwardedIPConfig: NotRequired[ForwardedIPConfigTypeDef]
    CustomKeys: NotRequired[Sequence[RateBasedStatementCustomKeyUnionTypeDef]]

class GetLoggingConfigurationResponseTypeDef(TypedDict):
    LoggingConfiguration: LoggingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLoggingConfigurationsResponseTypeDef(TypedDict):
    LoggingConfigurations: List[LoggingConfigurationOutputTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingConfigurationResponseTypeDef(TypedDict):
    LoggingConfiguration: LoggingConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

OverrideActionTypeDef = TypedDict(
    "OverrideActionTypeDef",
    {
        "Count": NotRequired[CountActionUnionTypeDef],
        "None": NotRequired[Mapping[str, Any]],
    },
)

class ManagedRuleGroupStatementOutputTypeDef(TypedDict):
    VendorName: str
    Name: str
    Version: NotRequired[str]
    ExcludedRules: NotRequired[List[ExcludedRuleTypeDef]]
    ScopeDownStatement: NotRequired[Dict[str, Any]]
    ManagedRuleGroupConfigs: NotRequired[List[ManagedRuleGroupConfigOutputTypeDef]]
    RuleActionOverrides: NotRequired[List[RuleActionOverrideOutputTypeDef]]

class RuleGroupReferenceStatementOutputTypeDef(TypedDict):
    ARN: str
    ExcludedRules: NotRequired[List[ExcludedRuleTypeDef]]
    RuleActionOverrides: NotRequired[List[RuleActionOverrideOutputTypeDef]]

class DescribeManagedRuleGroupResponseTypeDef(TypedDict):
    VersionName: str
    SnsTopicArn: str
    Capacity: int
    Rules: List[RuleSummaryTypeDef]
    LabelNamespace: str
    AvailableLabels: List[LabelSummaryTypeDef]
    ConsumedLabels: List[LabelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RuleActionTypeDef(TypedDict):
    Block: NotRequired[BlockActionUnionTypeDef]
    Allow: NotRequired[AllowActionUnionTypeDef]
    Count: NotRequired[CountActionUnionTypeDef]
    Captcha: NotRequired[CaptchaActionUnionTypeDef]
    Challenge: NotRequired[ChallengeActionUnionTypeDef]

DefaultActionUnionTypeDef = Union[DefaultActionTypeDef, DefaultActionOutputTypeDef]
FieldToMatchUnionTypeDef = Union[FieldToMatchTypeDef, FieldToMatchOutputTypeDef]

class LoggingConfigurationTypeDef(TypedDict):
    ResourceArn: str
    LogDestinationConfigs: Sequence[str]
    RedactedFields: NotRequired[Sequence[FieldToMatchTypeDef]]
    ManagedByFirewallManager: NotRequired[bool]
    LoggingFilter: NotRequired[LoggingFilterTypeDef]
    LogType: NotRequired[Literal["WAF_LOGS"]]
    LogScope: NotRequired[LogScopeType]

AWSManagedRulesACFPRuleSetUnionTypeDef = Union[
    AWSManagedRulesACFPRuleSetTypeDef, AWSManagedRulesACFPRuleSetOutputTypeDef
]
AWSManagedRulesATPRuleSetUnionTypeDef = Union[
    AWSManagedRulesATPRuleSetTypeDef, AWSManagedRulesATPRuleSetOutputTypeDef
]
RateBasedStatementUnionTypeDef = Union[RateBasedStatementTypeDef, RateBasedStatementOutputTypeDef]
OverrideActionUnionTypeDef = Union[OverrideActionTypeDef, OverrideActionOutputTypeDef]

class FirewallManagerStatementTypeDef(TypedDict):
    ManagedRuleGroupStatement: NotRequired[ManagedRuleGroupStatementOutputTypeDef]
    RuleGroupReferenceStatement: NotRequired[RuleGroupReferenceStatementOutputTypeDef]

class StatementOutputTypeDef(TypedDict):
    ByteMatchStatement: NotRequired[ByteMatchStatementOutputTypeDef]
    SqliMatchStatement: NotRequired[SqliMatchStatementOutputTypeDef]
    XssMatchStatement: NotRequired[XssMatchStatementOutputTypeDef]
    SizeConstraintStatement: NotRequired[SizeConstraintStatementOutputTypeDef]
    GeoMatchStatement: NotRequired[GeoMatchStatementOutputTypeDef]
    RuleGroupReferenceStatement: NotRequired[RuleGroupReferenceStatementOutputTypeDef]
    IPSetReferenceStatement: NotRequired[IPSetReferenceStatementTypeDef]
    RegexPatternSetReferenceStatement: NotRequired[RegexPatternSetReferenceStatementOutputTypeDef]
    RateBasedStatement: NotRequired[RateBasedStatementOutputTypeDef]
    AndStatement: NotRequired[AndStatementOutputTypeDef]
    OrStatement: NotRequired[OrStatementOutputTypeDef]
    NotStatement: NotRequired[NotStatementOutputTypeDef]
    ManagedRuleGroupStatement: NotRequired[ManagedRuleGroupStatementOutputTypeDef]
    LabelMatchStatement: NotRequired[LabelMatchStatementTypeDef]
    RegexMatchStatement: NotRequired[RegexMatchStatementOutputTypeDef]

RuleActionUnionTypeDef = Union[RuleActionTypeDef, RuleActionOutputTypeDef]

class ByteMatchStatementTypeDef(TypedDict):
    SearchString: BlobTypeDef
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]
    PositionalConstraint: PositionalConstraintType

class RegexMatchStatementTypeDef(TypedDict):
    RegexString: str
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]

class RegexPatternSetReferenceStatementTypeDef(TypedDict):
    ARN: str
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]

class SizeConstraintStatementTypeDef(TypedDict):
    FieldToMatch: FieldToMatchUnionTypeDef
    ComparisonOperator: ComparisonOperatorType
    Size: int
    TextTransformations: Sequence[TextTransformationTypeDef]

class SqliMatchStatementTypeDef(TypedDict):
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]
    SensitivityLevel: NotRequired[SensitivityLevelType]

class XssMatchStatementTypeDef(TypedDict):
    FieldToMatch: FieldToMatchUnionTypeDef
    TextTransformations: Sequence[TextTransformationTypeDef]

LoggingConfigurationUnionTypeDef = Union[
    LoggingConfigurationTypeDef, LoggingConfigurationOutputTypeDef
]

class ManagedRuleGroupConfigTypeDef(TypedDict):
    LoginPath: NotRequired[str]
    PayloadType: NotRequired[PayloadTypeType]
    UsernameField: NotRequired[UsernameFieldTypeDef]
    PasswordField: NotRequired[PasswordFieldTypeDef]
    AWSManagedRulesBotControlRuleSet: NotRequired[AWSManagedRulesBotControlRuleSetTypeDef]
    AWSManagedRulesATPRuleSet: NotRequired[AWSManagedRulesATPRuleSetUnionTypeDef]
    AWSManagedRulesACFPRuleSet: NotRequired[AWSManagedRulesACFPRuleSetUnionTypeDef]

class FirewallManagerRuleGroupTypeDef(TypedDict):
    Name: str
    Priority: int
    FirewallManagerStatement: FirewallManagerStatementTypeDef
    OverrideAction: OverrideActionOutputTypeDef
    VisibilityConfig: VisibilityConfigTypeDef

class RuleOutputTypeDef(TypedDict):
    Name: str
    Priority: int
    Statement: StatementOutputTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Action: NotRequired[RuleActionOutputTypeDef]
    OverrideAction: NotRequired[OverrideActionOutputTypeDef]
    RuleLabels: NotRequired[List[LabelTypeDef]]
    CaptchaConfig: NotRequired[CaptchaConfigTypeDef]
    ChallengeConfig: NotRequired[ChallengeConfigTypeDef]

class RuleActionOverrideTypeDef(TypedDict):
    Name: str
    ActionToUse: RuleActionUnionTypeDef

ByteMatchStatementUnionTypeDef = Union[ByteMatchStatementTypeDef, ByteMatchStatementOutputTypeDef]
RegexMatchStatementUnionTypeDef = Union[
    RegexMatchStatementTypeDef, RegexMatchStatementOutputTypeDef
]
RegexPatternSetReferenceStatementUnionTypeDef = Union[
    RegexPatternSetReferenceStatementTypeDef, RegexPatternSetReferenceStatementOutputTypeDef
]
SizeConstraintStatementUnionTypeDef = Union[
    SizeConstraintStatementTypeDef, SizeConstraintStatementOutputTypeDef
]
SqliMatchStatementUnionTypeDef = Union[SqliMatchStatementTypeDef, SqliMatchStatementOutputTypeDef]
XssMatchStatementUnionTypeDef = Union[XssMatchStatementTypeDef, XssMatchStatementOutputTypeDef]

class PutLoggingConfigurationRequestTypeDef(TypedDict):
    LoggingConfiguration: LoggingConfigurationUnionTypeDef

ManagedRuleGroupConfigUnionTypeDef = Union[
    ManagedRuleGroupConfigTypeDef, ManagedRuleGroupConfigOutputTypeDef
]

class RuleGroupTypeDef(TypedDict):
    Name: str
    Id: str
    Capacity: int
    ARN: str
    VisibilityConfig: VisibilityConfigTypeDef
    Description: NotRequired[str]
    Rules: NotRequired[List[RuleOutputTypeDef]]
    LabelNamespace: NotRequired[str]
    CustomResponseBodies: NotRequired[Dict[str, CustomResponseBodyTypeDef]]
    AvailableLabels: NotRequired[List[LabelSummaryTypeDef]]
    ConsumedLabels: NotRequired[List[LabelSummaryTypeDef]]

class WebACLTypeDef(TypedDict):
    Name: str
    Id: str
    ARN: str
    DefaultAction: DefaultActionOutputTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Description: NotRequired[str]
    Rules: NotRequired[List[RuleOutputTypeDef]]
    DataProtectionConfig: NotRequired[DataProtectionConfigOutputTypeDef]
    Capacity: NotRequired[int]
    PreProcessFirewallManagerRuleGroups: NotRequired[List[FirewallManagerRuleGroupTypeDef]]
    PostProcessFirewallManagerRuleGroups: NotRequired[List[FirewallManagerRuleGroupTypeDef]]
    ManagedByFirewallManager: NotRequired[bool]
    LabelNamespace: NotRequired[str]
    CustomResponseBodies: NotRequired[Dict[str, CustomResponseBodyTypeDef]]
    CaptchaConfig: NotRequired[CaptchaConfigTypeDef]
    ChallengeConfig: NotRequired[ChallengeConfigTypeDef]
    TokenDomains: NotRequired[List[str]]
    AssociationConfig: NotRequired[AssociationConfigOutputTypeDef]
    RetrofittedByFirewallManager: NotRequired[bool]

RuleActionOverrideUnionTypeDef = Union[RuleActionOverrideTypeDef, RuleActionOverrideOutputTypeDef]

class GetRuleGroupResponseTypeDef(TypedDict):
    RuleGroup: RuleGroupTypeDef
    LockToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebACLForResourceResponseTypeDef(TypedDict):
    WebACL: WebACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebACLResponseTypeDef(TypedDict):
    WebACL: WebACLTypeDef
    LockToken: str
    ApplicationIntegrationURL: str
    ResponseMetadata: ResponseMetadataTypeDef

class ManagedRuleGroupStatementTypeDef(TypedDict):
    VendorName: str
    Name: str
    Version: NotRequired[str]
    ExcludedRules: NotRequired[Sequence[ExcludedRuleTypeDef]]
    ScopeDownStatement: NotRequired[Mapping[str, Any]]
    ManagedRuleGroupConfigs: NotRequired[Sequence[ManagedRuleGroupConfigUnionTypeDef]]
    RuleActionOverrides: NotRequired[Sequence[RuleActionOverrideUnionTypeDef]]

class RuleGroupReferenceStatementTypeDef(TypedDict):
    ARN: str
    ExcludedRules: NotRequired[Sequence[ExcludedRuleTypeDef]]
    RuleActionOverrides: NotRequired[Sequence[RuleActionOverrideUnionTypeDef]]

ManagedRuleGroupStatementUnionTypeDef = Union[
    ManagedRuleGroupStatementTypeDef, ManagedRuleGroupStatementOutputTypeDef
]
RuleGroupReferenceStatementUnionTypeDef = Union[
    RuleGroupReferenceStatementTypeDef, RuleGroupReferenceStatementOutputTypeDef
]

class StatementTypeDef(TypedDict):
    ByteMatchStatement: NotRequired[ByteMatchStatementUnionTypeDef]
    SqliMatchStatement: NotRequired[SqliMatchStatementUnionTypeDef]
    XssMatchStatement: NotRequired[XssMatchStatementUnionTypeDef]
    SizeConstraintStatement: NotRequired[SizeConstraintStatementUnionTypeDef]
    GeoMatchStatement: NotRequired[GeoMatchStatementUnionTypeDef]
    RuleGroupReferenceStatement: NotRequired[RuleGroupReferenceStatementUnionTypeDef]
    IPSetReferenceStatement: NotRequired[IPSetReferenceStatementTypeDef]
    RegexPatternSetReferenceStatement: NotRequired[RegexPatternSetReferenceStatementUnionTypeDef]
    RateBasedStatement: NotRequired[RateBasedStatementUnionTypeDef]
    AndStatement: NotRequired[AndStatementUnionTypeDef]
    OrStatement: NotRequired[OrStatementUnionTypeDef]
    NotStatement: NotRequired[NotStatementUnionTypeDef]
    ManagedRuleGroupStatement: NotRequired[ManagedRuleGroupStatementUnionTypeDef]
    LabelMatchStatement: NotRequired[LabelMatchStatementTypeDef]
    RegexMatchStatement: NotRequired[RegexMatchStatementUnionTypeDef]

StatementUnionTypeDef = Union[StatementTypeDef, StatementOutputTypeDef]

class RuleTypeDef(TypedDict):
    Name: str
    Priority: int
    Statement: StatementUnionTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Action: NotRequired[RuleActionUnionTypeDef]
    OverrideAction: NotRequired[OverrideActionUnionTypeDef]
    RuleLabels: NotRequired[Sequence[LabelTypeDef]]
    CaptchaConfig: NotRequired[CaptchaConfigTypeDef]
    ChallengeConfig: NotRequired[ChallengeConfigTypeDef]

RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]

class CheckCapacityRequestTypeDef(TypedDict):
    Scope: ScopeType
    Rules: Sequence[RuleUnionTypeDef]

class CreateRuleGroupRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Capacity: int
    VisibilityConfig: VisibilityConfigTypeDef
    Description: NotRequired[str]
    Rules: NotRequired[Sequence[RuleUnionTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]
    CustomResponseBodies: NotRequired[Mapping[str, CustomResponseBodyTypeDef]]

class CreateWebACLRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    DefaultAction: DefaultActionUnionTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    Description: NotRequired[str]
    Rules: NotRequired[Sequence[RuleUnionTypeDef]]
    DataProtectionConfig: NotRequired[DataProtectionConfigUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]
    CustomResponseBodies: NotRequired[Mapping[str, CustomResponseBodyTypeDef]]
    CaptchaConfig: NotRequired[CaptchaConfigTypeDef]
    ChallengeConfig: NotRequired[ChallengeConfigTypeDef]
    TokenDomains: NotRequired[Sequence[str]]
    AssociationConfig: NotRequired[AssociationConfigUnionTypeDef]

class UpdateRuleGroupRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    VisibilityConfig: VisibilityConfigTypeDef
    LockToken: str
    Description: NotRequired[str]
    Rules: NotRequired[Sequence[RuleUnionTypeDef]]
    CustomResponseBodies: NotRequired[Mapping[str, CustomResponseBodyTypeDef]]

class UpdateWebACLRequestTypeDef(TypedDict):
    Name: str
    Scope: ScopeType
    Id: str
    DefaultAction: DefaultActionUnionTypeDef
    VisibilityConfig: VisibilityConfigTypeDef
    LockToken: str
    Description: NotRequired[str]
    Rules: NotRequired[Sequence[RuleUnionTypeDef]]
    DataProtectionConfig: NotRequired[DataProtectionConfigUnionTypeDef]
    CustomResponseBodies: NotRequired[Mapping[str, CustomResponseBodyTypeDef]]
    CaptchaConfig: NotRequired[CaptchaConfigTypeDef]
    ChallengeConfig: NotRequired[ChallengeConfigTypeDef]
    TokenDomains: NotRequired[Sequence[str]]
    AssociationConfig: NotRequired[AssociationConfigUnionTypeDef]
