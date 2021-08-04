"""
Type annotations for waf-regional service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf_regional/type_defs.html)

Usage::

    ```python
    from mypy_boto3_waf_regional.type_defs import ActivatedRuleTypeDef

    data: ActivatedRuleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ChangeActionType,
    ChangeTokenStatusType,
    ComparisonOperatorType,
    GeoMatchConstraintValueType,
    IPSetDescriptorTypeType,
    MatchFieldTypeType,
    PositionalConstraintType,
    PredicateTypeType,
    ResourceTypeType,
    TextTransformationType,
    WafActionTypeType,
    WafOverrideActionTypeType,
    WafRuleTypeType,
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
    "ActivatedRuleTypeDef",
    "AssociateWebACLRequestRequestTypeDef",
    "ByteMatchSetSummaryTypeDef",
    "ByteMatchSetTypeDef",
    "ByteMatchSetUpdateTypeDef",
    "ByteMatchTupleTypeDef",
    "CreateByteMatchSetRequestRequestTypeDef",
    "CreateByteMatchSetResponseTypeDef",
    "CreateGeoMatchSetRequestRequestTypeDef",
    "CreateGeoMatchSetResponseTypeDef",
    "CreateIPSetRequestRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRateBasedRuleRequestRequestTypeDef",
    "CreateRateBasedRuleResponseTypeDef",
    "CreateRegexMatchSetRequestRequestTypeDef",
    "CreateRegexMatchSetResponseTypeDef",
    "CreateRegexPatternSetRequestRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupRequestRequestTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateSizeConstraintSetRequestRequestTypeDef",
    "CreateSizeConstraintSetResponseTypeDef",
    "CreateSqlInjectionMatchSetRequestRequestTypeDef",
    "CreateSqlInjectionMatchSetResponseTypeDef",
    "CreateWebACLMigrationStackRequestRequestTypeDef",
    "CreateWebACLMigrationStackResponseTypeDef",
    "CreateWebACLRequestRequestTypeDef",
    "CreateWebACLResponseTypeDef",
    "CreateXssMatchSetRequestRequestTypeDef",
    "CreateXssMatchSetResponseTypeDef",
    "DeleteByteMatchSetRequestRequestTypeDef",
    "DeleteByteMatchSetResponseTypeDef",
    "DeleteGeoMatchSetRequestRequestTypeDef",
    "DeleteGeoMatchSetResponseTypeDef",
    "DeleteIPSetRequestRequestTypeDef",
    "DeleteIPSetResponseTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeletePermissionPolicyRequestRequestTypeDef",
    "DeleteRateBasedRuleRequestRequestTypeDef",
    "DeleteRateBasedRuleResponseTypeDef",
    "DeleteRegexMatchSetRequestRequestTypeDef",
    "DeleteRegexMatchSetResponseTypeDef",
    "DeleteRegexPatternSetRequestRequestTypeDef",
    "DeleteRegexPatternSetResponseTypeDef",
    "DeleteRuleGroupRequestRequestTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DeleteRuleResponseTypeDef",
    "DeleteSizeConstraintSetRequestRequestTypeDef",
    "DeleteSizeConstraintSetResponseTypeDef",
    "DeleteSqlInjectionMatchSetRequestRequestTypeDef",
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    "DeleteWebACLRequestRequestTypeDef",
    "DeleteWebACLResponseTypeDef",
    "DeleteXssMatchSetRequestRequestTypeDef",
    "DeleteXssMatchSetResponseTypeDef",
    "DisassociateWebACLRequestRequestTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "GeoMatchConstraintTypeDef",
    "GeoMatchSetSummaryTypeDef",
    "GeoMatchSetTypeDef",
    "GeoMatchSetUpdateTypeDef",
    "GetByteMatchSetRequestRequestTypeDef",
    "GetByteMatchSetResponseTypeDef",
    "GetChangeTokenResponseTypeDef",
    "GetChangeTokenStatusRequestRequestTypeDef",
    "GetChangeTokenStatusResponseTypeDef",
    "GetGeoMatchSetRequestRequestTypeDef",
    "GetGeoMatchSetResponseTypeDef",
    "GetIPSetRequestRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetPermissionPolicyRequestRequestTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedRuleManagedKeysRequestRequestTypeDef",
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    "GetRateBasedRuleRequestRequestTypeDef",
    "GetRateBasedRuleResponseTypeDef",
    "GetRegexMatchSetRequestRequestTypeDef",
    "GetRegexMatchSetResponseTypeDef",
    "GetRegexPatternSetRequestRequestTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupRequestRequestTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetRuleRequestRequestTypeDef",
    "GetRuleResponseTypeDef",
    "GetSampledRequestsRequestRequestTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetSizeConstraintSetRequestRequestTypeDef",
    "GetSizeConstraintSetResponseTypeDef",
    "GetSqlInjectionMatchSetRequestRequestTypeDef",
    "GetSqlInjectionMatchSetResponseTypeDef",
    "GetWebACLForResourceRequestRequestTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLRequestRequestTypeDef",
    "GetWebACLResponseTypeDef",
    "GetXssMatchSetRequestRequestTypeDef",
    "GetXssMatchSetResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetDescriptorTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "IPSetUpdateTypeDef",
    "ListActivatedRulesInRuleGroupRequestRequestTypeDef",
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    "ListByteMatchSetsRequestRequestTypeDef",
    "ListByteMatchSetsResponseTypeDef",
    "ListGeoMatchSetsRequestRequestTypeDef",
    "ListGeoMatchSetsResponseTypeDef",
    "ListIPSetsRequestRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRateBasedRulesRequestRequestTypeDef",
    "ListRateBasedRulesResponseTypeDef",
    "ListRegexMatchSetsRequestRequestTypeDef",
    "ListRegexMatchSetsResponseTypeDef",
    "ListRegexPatternSetsRequestRequestTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListResourcesForWebACLRequestRequestTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "ListRuleGroupsRequestRequestTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListSizeConstraintSetsRequestRequestTypeDef",
    "ListSizeConstraintSetsResponseTypeDef",
    "ListSqlInjectionMatchSetsRequestRequestTypeDef",
    "ListSqlInjectionMatchSetsResponseTypeDef",
    "ListSubscribedRuleGroupsRequestRequestTypeDef",
    "ListSubscribedRuleGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsRequestRequestTypeDef",
    "ListWebACLsResponseTypeDef",
    "ListXssMatchSetsRequestRequestTypeDef",
    "ListXssMatchSetsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "PredicateTypeDef",
    "PutLoggingConfigurationRequestRequestTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutPermissionPolicyRequestRequestTypeDef",
    "RateBasedRuleTypeDef",
    "RegexMatchSetSummaryTypeDef",
    "RegexMatchSetTypeDef",
    "RegexMatchSetUpdateTypeDef",
    "RegexMatchTupleTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexPatternSetUpdateTypeDef",
    "ResponseMetadataTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleGroupUpdateTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "RuleUpdateTypeDef",
    "SampledHTTPRequestTypeDef",
    "SizeConstraintSetSummaryTypeDef",
    "SizeConstraintSetTypeDef",
    "SizeConstraintSetUpdateTypeDef",
    "SizeConstraintTypeDef",
    "SqlInjectionMatchSetSummaryTypeDef",
    "SqlInjectionMatchSetTypeDef",
    "SqlInjectionMatchSetUpdateTypeDef",
    "SqlInjectionMatchTupleTypeDef",
    "SubscribedRuleGroupSummaryTypeDef",
    "TagInfoForResourceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimeWindowTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateByteMatchSetRequestRequestTypeDef",
    "UpdateByteMatchSetResponseTypeDef",
    "UpdateGeoMatchSetRequestRequestTypeDef",
    "UpdateGeoMatchSetResponseTypeDef",
    "UpdateIPSetRequestRequestTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRateBasedRuleRequestRequestTypeDef",
    "UpdateRateBasedRuleResponseTypeDef",
    "UpdateRegexMatchSetRequestRequestTypeDef",
    "UpdateRegexMatchSetResponseTypeDef",
    "UpdateRegexPatternSetRequestRequestTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupRequestRequestTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "UpdateRuleResponseTypeDef",
    "UpdateSizeConstraintSetRequestRequestTypeDef",
    "UpdateSizeConstraintSetResponseTypeDef",
    "UpdateSqlInjectionMatchSetRequestRequestTypeDef",
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    "UpdateWebACLRequestRequestTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UpdateXssMatchSetRequestRequestTypeDef",
    "UpdateXssMatchSetResponseTypeDef",
    "WafActionTypeDef",
    "WafOverrideActionTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "WebACLUpdateTypeDef",
    "XssMatchSetSummaryTypeDef",
    "XssMatchSetTypeDef",
    "XssMatchSetUpdateTypeDef",
    "XssMatchTupleTypeDef",
)

_RequiredActivatedRuleTypeDef = TypedDict(
    "_RequiredActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
    },
)
_OptionalActivatedRuleTypeDef = TypedDict(
    "_OptionalActivatedRuleTypeDef",
    {
        "Action": "WafActionTypeDef",
        "OverrideAction": "WafOverrideActionTypeDef",
        "Type": WafRuleTypeType,
        "ExcludedRules": List["ExcludedRuleTypeDef"],
    },
    total=False,
)

class ActivatedRuleTypeDef(_RequiredActivatedRuleTypeDef, _OptionalActivatedRuleTypeDef):
    pass

AssociateWebACLRequestRequestTypeDef = TypedDict(
    "AssociateWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
        "ResourceArn": str,
    },
)

ByteMatchSetSummaryTypeDef = TypedDict(
    "ByteMatchSetSummaryTypeDef",
    {
        "ByteMatchSetId": str,
        "Name": str,
    },
)

_RequiredByteMatchSetTypeDef = TypedDict(
    "_RequiredByteMatchSetTypeDef",
    {
        "ByteMatchSetId": str,
        "ByteMatchTuples": List["ByteMatchTupleTypeDef"],
    },
)
_OptionalByteMatchSetTypeDef = TypedDict(
    "_OptionalByteMatchSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class ByteMatchSetTypeDef(_RequiredByteMatchSetTypeDef, _OptionalByteMatchSetTypeDef):
    pass

ByteMatchSetUpdateTypeDef = TypedDict(
    "ByteMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ByteMatchTuple": "ByteMatchTupleTypeDef",
    },
)

ByteMatchTupleTypeDef = TypedDict(
    "ByteMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TargetString": bytes,
        "TextTransformation": TextTransformationType,
        "PositionalConstraint": PositionalConstraintType,
    },
)

CreateByteMatchSetRequestRequestTypeDef = TypedDict(
    "CreateByteMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateByteMatchSetResponseTypeDef = TypedDict(
    "CreateByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": "ByteMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGeoMatchSetRequestRequestTypeDef = TypedDict(
    "CreateGeoMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateGeoMatchSetResponseTypeDef = TypedDict(
    "CreateGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": "GeoMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIPSetRequestRequestTypeDef = TypedDict(
    "CreateIPSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateIPSetResponseTypeDef = TypedDict(
    "CreateIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRateBasedRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRateBasedRuleRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "RateKey": Literal["IP"],
        "RateLimit": int,
        "ChangeToken": str,
    },
)
_OptionalCreateRateBasedRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRateBasedRuleRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRateBasedRuleRequestRequestTypeDef(
    _RequiredCreateRateBasedRuleRequestRequestTypeDef,
    _OptionalCreateRateBasedRuleRequestRequestTypeDef,
):
    pass

CreateRateBasedRuleResponseTypeDef = TypedDict(
    "CreateRateBasedRuleResponseTypeDef",
    {
        "Rule": "RateBasedRuleTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegexMatchSetRequestRequestTypeDef = TypedDict(
    "CreateRegexMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateRegexMatchSetResponseTypeDef = TypedDict(
    "CreateRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": "RegexMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "CreateRegexPatternSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateRegexPatternSetResponseTypeDef = TypedDict(
    "CreateRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleGroupRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "ChangeToken": str,
    },
)
_OptionalCreateRuleGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleGroupRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
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
        "RuleGroup": "RuleGroupTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "ChangeToken": str,
    },
)
_OptionalCreateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRuleRequestRequestTypeDef(
    _RequiredCreateRuleRequestRequestTypeDef, _OptionalCreateRuleRequestRequestTypeDef
):
    pass

CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "CreateSizeConstraintSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateSizeConstraintSetResponseTypeDef = TypedDict(
    "CreateSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": "SizeConstraintSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "CreateSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": "SqlInjectionMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWebACLMigrationStackRequestRequestTypeDef = TypedDict(
    "CreateWebACLMigrationStackRequestRequestTypeDef",
    {
        "WebACLId": str,
        "S3BucketName": str,
        "IgnoreUnsupportedType": bool,
    },
)

CreateWebACLMigrationStackResponseTypeDef = TypedDict(
    "CreateWebACLMigrationStackResponseTypeDef",
    {
        "S3ObjectUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateWebACLRequestRequestTypeDef = TypedDict(
    "_RequiredCreateWebACLRequestRequestTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "DefaultAction": "WafActionTypeDef",
        "ChangeToken": str,
    },
)
_OptionalCreateWebACLRequestRequestTypeDef = TypedDict(
    "_OptionalCreateWebACLRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
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
        "WebACL": "WebACLTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateXssMatchSetRequestRequestTypeDef = TypedDict(
    "CreateXssMatchSetRequestRequestTypeDef",
    {
        "Name": str,
        "ChangeToken": str,
    },
)

CreateXssMatchSetResponseTypeDef = TypedDict(
    "CreateXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": "XssMatchSetTypeDef",
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteByteMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteByteMatchSetResponseTypeDef = TypedDict(
    "DeleteByteMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGeoMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteGeoMatchSetResponseTypeDef = TypedDict(
    "DeleteGeoMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIPSetRequestRequestTypeDef = TypedDict(
    "DeleteIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
        "ChangeToken": str,
    },
)

DeleteIPSetResponseTypeDef = TypedDict(
    "DeleteIPSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

DeleteRateBasedRuleRequestRequestTypeDef = TypedDict(
    "DeleteRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
    },
)

DeleteRateBasedRuleResponseTypeDef = TypedDict(
    "DeleteRateBasedRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegexMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteRegexMatchSetResponseTypeDef = TypedDict(
    "DeleteRegexMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRegexPatternSetRequestRequestTypeDef = TypedDict(
    "DeleteRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
        "ChangeToken": str,
    },
)

DeleteRegexPatternSetResponseTypeDef = TypedDict(
    "DeleteRegexPatternSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleGroupRequestRequestTypeDef = TypedDict(
    "DeleteRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
        "ChangeToken": str,
    },
)

DeleteRuleGroupResponseTypeDef = TypedDict(
    "DeleteRuleGroupResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
    },
)

DeleteRuleResponseTypeDef = TypedDict(
    "DeleteRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "DeleteSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
        "ChangeToken": str,
    },
)

DeleteSizeConstraintSetResponseTypeDef = TypedDict(
    "DeleteSizeConstraintSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWebACLRequestRequestTypeDef = TypedDict(
    "DeleteWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
        "ChangeToken": str,
    },
)

DeleteWebACLResponseTypeDef = TypedDict(
    "DeleteWebACLResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteXssMatchSetRequestRequestTypeDef = TypedDict(
    "DeleteXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
        "ChangeToken": str,
    },
)

DeleteXssMatchSetResponseTypeDef = TypedDict(
    "DeleteXssMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
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
        "RuleId": str,
    },
)

_RequiredFieldToMatchTypeDef = TypedDict(
    "_RequiredFieldToMatchTypeDef",
    {
        "Type": MatchFieldTypeType,
    },
)
_OptionalFieldToMatchTypeDef = TypedDict(
    "_OptionalFieldToMatchTypeDef",
    {
        "Data": str,
    },
    total=False,
)

class FieldToMatchTypeDef(_RequiredFieldToMatchTypeDef, _OptionalFieldToMatchTypeDef):
    pass

GeoMatchConstraintTypeDef = TypedDict(
    "GeoMatchConstraintTypeDef",
    {
        "Type": Literal["Country"],
        "Value": GeoMatchConstraintValueType,
    },
)

GeoMatchSetSummaryTypeDef = TypedDict(
    "GeoMatchSetSummaryTypeDef",
    {
        "GeoMatchSetId": str,
        "Name": str,
    },
)

_RequiredGeoMatchSetTypeDef = TypedDict(
    "_RequiredGeoMatchSetTypeDef",
    {
        "GeoMatchSetId": str,
        "GeoMatchConstraints": List["GeoMatchConstraintTypeDef"],
    },
)
_OptionalGeoMatchSetTypeDef = TypedDict(
    "_OptionalGeoMatchSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class GeoMatchSetTypeDef(_RequiredGeoMatchSetTypeDef, _OptionalGeoMatchSetTypeDef):
    pass

GeoMatchSetUpdateTypeDef = TypedDict(
    "GeoMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "GeoMatchConstraint": "GeoMatchConstraintTypeDef",
    },
)

GetByteMatchSetRequestRequestTypeDef = TypedDict(
    "GetByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
    },
)

GetByteMatchSetResponseTypeDef = TypedDict(
    "GetByteMatchSetResponseTypeDef",
    {
        "ByteMatchSet": "ByteMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeTokenResponseTypeDef = TypedDict(
    "GetChangeTokenResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeTokenStatusRequestRequestTypeDef = TypedDict(
    "GetChangeTokenStatusRequestRequestTypeDef",
    {
        "ChangeToken": str,
    },
)

GetChangeTokenStatusResponseTypeDef = TypedDict(
    "GetChangeTokenStatusResponseTypeDef",
    {
        "ChangeTokenStatus": ChangeTokenStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeoMatchSetRequestRequestTypeDef = TypedDict(
    "GetGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
    },
)

GetGeoMatchSetResponseTypeDef = TypedDict(
    "GetGeoMatchSetResponseTypeDef",
    {
        "GeoMatchSet": "GeoMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIPSetRequestRequestTypeDef = TypedDict(
    "GetIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
    },
)

GetIPSetResponseTypeDef = TypedDict(
    "GetIPSetResponseTypeDef",
    {
        "IPSet": "IPSetTypeDef",
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

_RequiredGetRateBasedRuleManagedKeysRequestRequestTypeDef = TypedDict(
    "_RequiredGetRateBasedRuleManagedKeysRequestRequestTypeDef",
    {
        "RuleId": str,
    },
)
_OptionalGetRateBasedRuleManagedKeysRequestRequestTypeDef = TypedDict(
    "_OptionalGetRateBasedRuleManagedKeysRequestRequestTypeDef",
    {
        "NextMarker": str,
    },
    total=False,
)

class GetRateBasedRuleManagedKeysRequestRequestTypeDef(
    _RequiredGetRateBasedRuleManagedKeysRequestRequestTypeDef,
    _OptionalGetRateBasedRuleManagedKeysRequestRequestTypeDef,
):
    pass

GetRateBasedRuleManagedKeysResponseTypeDef = TypedDict(
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    {
        "ManagedKeys": List[str],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRateBasedRuleRequestRequestTypeDef = TypedDict(
    "GetRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
    },
)

GetRateBasedRuleResponseTypeDef = TypedDict(
    "GetRateBasedRuleResponseTypeDef",
    {
        "Rule": "RateBasedRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegexMatchSetRequestRequestTypeDef = TypedDict(
    "GetRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
    },
)

GetRegexMatchSetResponseTypeDef = TypedDict(
    "GetRegexMatchSetResponseTypeDef",
    {
        "RegexMatchSet": "RegexMatchSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegexPatternSetRequestRequestTypeDef = TypedDict(
    "GetRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
    },
)

GetRegexPatternSetResponseTypeDef = TypedDict(
    "GetRegexPatternSetResponseTypeDef",
    {
        "RegexPatternSet": "RegexPatternSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleGroupRequestRequestTypeDef = TypedDict(
    "GetRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
    },
)

GetRuleGroupResponseTypeDef = TypedDict(
    "GetRuleGroupResponseTypeDef",
    {
        "RuleGroup": "RuleGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "RuleId": str,
    },
)

GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "Rule": "RuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSampledRequestsRequestRequestTypeDef = TypedDict(
    "GetSampledRequestsRequestRequestTypeDef",
    {
        "WebAclId": str,
        "RuleId": str,
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

GetSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "GetSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
    },
)

GetSizeConstraintSetResponseTypeDef = TypedDict(
    "GetSizeConstraintSetResponseTypeDef",
    {
        "SizeConstraintSet": "SizeConstraintSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "GetSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
    },
)

GetSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "GetSqlInjectionMatchSetResponseTypeDef",
    {
        "SqlInjectionMatchSet": "SqlInjectionMatchSetTypeDef",
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
        "WebACLSummary": "WebACLSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWebACLRequestRequestTypeDef = TypedDict(
    "GetWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
    },
)

GetWebACLResponseTypeDef = TypedDict(
    "GetWebACLResponseTypeDef",
    {
        "WebACL": "WebACLTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetXssMatchSetRequestRequestTypeDef = TypedDict(
    "GetXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
    },
)

GetXssMatchSetResponseTypeDef = TypedDict(
    "GetXssMatchSetResponseTypeDef",
    {
        "XssMatchSet": "XssMatchSetTypeDef",
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

IPSetDescriptorTypeDef = TypedDict(
    "IPSetDescriptorTypeDef",
    {
        "Type": IPSetDescriptorTypeType,
        "Value": str,
    },
)

IPSetSummaryTypeDef = TypedDict(
    "IPSetSummaryTypeDef",
    {
        "IPSetId": str,
        "Name": str,
    },
)

_RequiredIPSetTypeDef = TypedDict(
    "_RequiredIPSetTypeDef",
    {
        "IPSetId": str,
        "IPSetDescriptors": List["IPSetDescriptorTypeDef"],
    },
)
_OptionalIPSetTypeDef = TypedDict(
    "_OptionalIPSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class IPSetTypeDef(_RequiredIPSetTypeDef, _OptionalIPSetTypeDef):
    pass

IPSetUpdateTypeDef = TypedDict(
    "IPSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "IPSetDescriptor": "IPSetDescriptorTypeDef",
    },
)

ListActivatedRulesInRuleGroupRequestRequestTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListActivatedRulesInRuleGroupResponseTypeDef = TypedDict(
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    {
        "NextMarker": str,
        "ActivatedRules": List["ActivatedRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListByteMatchSetsRequestRequestTypeDef = TypedDict(
    "ListByteMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListByteMatchSetsResponseTypeDef = TypedDict(
    "ListByteMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "ByteMatchSets": List["ByteMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeoMatchSetsRequestRequestTypeDef = TypedDict(
    "ListGeoMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListGeoMatchSetsResponseTypeDef = TypedDict(
    "ListGeoMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "GeoMatchSets": List["GeoMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIPSetsRequestRequestTypeDef = TypedDict(
    "ListIPSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListIPSetsResponseTypeDef = TypedDict(
    "ListIPSetsResponseTypeDef",
    {
        "NextMarker": str,
        "IPSets": List["IPSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "LoggingConfigurations": List["LoggingConfigurationTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRateBasedRulesRequestRequestTypeDef = TypedDict(
    "ListRateBasedRulesRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRateBasedRulesResponseTypeDef = TypedDict(
    "ListRateBasedRulesResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List["RuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegexMatchSetsRequestRequestTypeDef = TypedDict(
    "ListRegexMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRegexMatchSetsResponseTypeDef = TypedDict(
    "ListRegexMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "RegexMatchSets": List["RegexMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegexPatternSetsRequestRequestTypeDef = TypedDict(
    "ListRegexPatternSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

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
        "WebACLId": str,
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

ListRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRuleGroupsResponseTypeDef = TypedDict(
    "ListRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["RuleGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "NextMarker": str,
        "Rules": List["RuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSizeConstraintSetsRequestRequestTypeDef = TypedDict(
    "ListSizeConstraintSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListSizeConstraintSetsResponseTypeDef = TypedDict(
    "ListSizeConstraintSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SizeConstraintSets": List["SizeConstraintSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSqlInjectionMatchSetsRequestRequestTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListSqlInjectionMatchSetsResponseTypeDef = TypedDict(
    "ListSqlInjectionMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "SqlInjectionMatchSets": List["SqlInjectionMatchSetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSubscribedRuleGroupsRequestRequestTypeDef = TypedDict(
    "ListSubscribedRuleGroupsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListSubscribedRuleGroupsResponseTypeDef = TypedDict(
    "ListSubscribedRuleGroupsResponseTypeDef",
    {
        "NextMarker": str,
        "RuleGroups": List["SubscribedRuleGroupSummaryTypeDef"],
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

ListWebACLsRequestRequestTypeDef = TypedDict(
    "ListWebACLsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListWebACLsResponseTypeDef = TypedDict(
    "ListWebACLsResponseTypeDef",
    {
        "NextMarker": str,
        "WebACLs": List["WebACLSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListXssMatchSetsRequestRequestTypeDef = TypedDict(
    "ListXssMatchSetsRequestRequestTypeDef",
    {
        "NextMarker": str,
        "Limit": int,
    },
    total=False,
)

ListXssMatchSetsResponseTypeDef = TypedDict(
    "ListXssMatchSetsResponseTypeDef",
    {
        "NextMarker": str,
        "XssMatchSets": List["XssMatchSetSummaryTypeDef"],
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
    },
    total=False,
)

class LoggingConfigurationTypeDef(
    _RequiredLoggingConfigurationTypeDef, _OptionalLoggingConfigurationTypeDef
):
    pass

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Negated": bool,
        "Type": PredicateTypeType,
        "DataId": str,
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

PutPermissionPolicyRequestRequestTypeDef = TypedDict(
    "PutPermissionPolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
    },
)

_RequiredRateBasedRuleTypeDef = TypedDict(
    "_RequiredRateBasedRuleTypeDef",
    {
        "RuleId": str,
        "MatchPredicates": List["PredicateTypeDef"],
        "RateKey": Literal["IP"],
        "RateLimit": int,
    },
)
_OptionalRateBasedRuleTypeDef = TypedDict(
    "_OptionalRateBasedRuleTypeDef",
    {
        "Name": str,
        "MetricName": str,
    },
    total=False,
)

class RateBasedRuleTypeDef(_RequiredRateBasedRuleTypeDef, _OptionalRateBasedRuleTypeDef):
    pass

RegexMatchSetSummaryTypeDef = TypedDict(
    "RegexMatchSetSummaryTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
    },
)

RegexMatchSetTypeDef = TypedDict(
    "RegexMatchSetTypeDef",
    {
        "RegexMatchSetId": str,
        "Name": str,
        "RegexMatchTuples": List["RegexMatchTupleTypeDef"],
    },
    total=False,
)

RegexMatchSetUpdateTypeDef = TypedDict(
    "RegexMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "RegexMatchTuple": "RegexMatchTupleTypeDef",
    },
)

RegexMatchTupleTypeDef = TypedDict(
    "RegexMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
        "RegexPatternSetId": str,
    },
)

RegexPatternSetSummaryTypeDef = TypedDict(
    "RegexPatternSetSummaryTypeDef",
    {
        "RegexPatternSetId": str,
        "Name": str,
    },
)

_RequiredRegexPatternSetTypeDef = TypedDict(
    "_RequiredRegexPatternSetTypeDef",
    {
        "RegexPatternSetId": str,
        "RegexPatternStrings": List[str],
    },
)
_OptionalRegexPatternSetTypeDef = TypedDict(
    "_OptionalRegexPatternSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class RegexPatternSetTypeDef(_RequiredRegexPatternSetTypeDef, _OptionalRegexPatternSetTypeDef):
    pass

RegexPatternSetUpdateTypeDef = TypedDict(
    "RegexPatternSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "RegexPatternString": str,
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

RuleGroupSummaryTypeDef = TypedDict(
    "RuleGroupSummaryTypeDef",
    {
        "RuleGroupId": str,
        "Name": str,
    },
)

_RequiredRuleGroupTypeDef = TypedDict(
    "_RequiredRuleGroupTypeDef",
    {
        "RuleGroupId": str,
    },
)
_OptionalRuleGroupTypeDef = TypedDict(
    "_OptionalRuleGroupTypeDef",
    {
        "Name": str,
        "MetricName": str,
    },
    total=False,
)

class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, _OptionalRuleGroupTypeDef):
    pass

RuleGroupUpdateTypeDef = TypedDict(
    "RuleGroupUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ActivatedRule": "ActivatedRuleTypeDef",
    },
)

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "RuleId": str,
        "Name": str,
    },
)

_RequiredRuleTypeDef = TypedDict(
    "_RequiredRuleTypeDef",
    {
        "RuleId": str,
        "Predicates": List["PredicateTypeDef"],
    },
)
_OptionalRuleTypeDef = TypedDict(
    "_OptionalRuleTypeDef",
    {
        "Name": str,
        "MetricName": str,
    },
    total=False,
)

class RuleTypeDef(_RequiredRuleTypeDef, _OptionalRuleTypeDef):
    pass

RuleUpdateTypeDef = TypedDict(
    "RuleUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "Predicate": "PredicateTypeDef",
    },
)

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
        "RuleWithinRuleGroup": str,
    },
    total=False,
)

class SampledHTTPRequestTypeDef(
    _RequiredSampledHTTPRequestTypeDef, _OptionalSampledHTTPRequestTypeDef
):
    pass

SizeConstraintSetSummaryTypeDef = TypedDict(
    "SizeConstraintSetSummaryTypeDef",
    {
        "SizeConstraintSetId": str,
        "Name": str,
    },
)

_RequiredSizeConstraintSetTypeDef = TypedDict(
    "_RequiredSizeConstraintSetTypeDef",
    {
        "SizeConstraintSetId": str,
        "SizeConstraints": List["SizeConstraintTypeDef"],
    },
)
_OptionalSizeConstraintSetTypeDef = TypedDict(
    "_OptionalSizeConstraintSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class SizeConstraintSetTypeDef(
    _RequiredSizeConstraintSetTypeDef, _OptionalSizeConstraintSetTypeDef
):
    pass

SizeConstraintSetUpdateTypeDef = TypedDict(
    "SizeConstraintSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "SizeConstraint": "SizeConstraintTypeDef",
    },
)

SizeConstraintTypeDef = TypedDict(
    "SizeConstraintTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
        "ComparisonOperator": ComparisonOperatorType,
        "Size": int,
    },
)

SqlInjectionMatchSetSummaryTypeDef = TypedDict(
    "SqlInjectionMatchSetSummaryTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "Name": str,
    },
)

_RequiredSqlInjectionMatchSetTypeDef = TypedDict(
    "_RequiredSqlInjectionMatchSetTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "SqlInjectionMatchTuples": List["SqlInjectionMatchTupleTypeDef"],
    },
)
_OptionalSqlInjectionMatchSetTypeDef = TypedDict(
    "_OptionalSqlInjectionMatchSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class SqlInjectionMatchSetTypeDef(
    _RequiredSqlInjectionMatchSetTypeDef, _OptionalSqlInjectionMatchSetTypeDef
):
    pass

SqlInjectionMatchSetUpdateTypeDef = TypedDict(
    "SqlInjectionMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "SqlInjectionMatchTuple": "SqlInjectionMatchTupleTypeDef",
    },
)

SqlInjectionMatchTupleTypeDef = TypedDict(
    "SqlInjectionMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
    },
)

SubscribedRuleGroupSummaryTypeDef = TypedDict(
    "SubscribedRuleGroupSummaryTypeDef",
    {
        "RuleGroupId": str,
        "Name": str,
        "MetricName": str,
    },
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

UpdateByteMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateByteMatchSetRequestRequestTypeDef",
    {
        "ByteMatchSetId": str,
        "ChangeToken": str,
        "Updates": List["ByteMatchSetUpdateTypeDef"],
    },
)

UpdateByteMatchSetResponseTypeDef = TypedDict(
    "UpdateByteMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGeoMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateGeoMatchSetRequestRequestTypeDef",
    {
        "GeoMatchSetId": str,
        "ChangeToken": str,
        "Updates": List["GeoMatchSetUpdateTypeDef"],
    },
)

UpdateGeoMatchSetResponseTypeDef = TypedDict(
    "UpdateGeoMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIPSetRequestRequestTypeDef = TypedDict(
    "UpdateIPSetRequestRequestTypeDef",
    {
        "IPSetId": str,
        "ChangeToken": str,
        "Updates": List["IPSetUpdateTypeDef"],
    },
)

UpdateIPSetResponseTypeDef = TypedDict(
    "UpdateIPSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRateBasedRuleRequestRequestTypeDef = TypedDict(
    "UpdateRateBasedRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
        "Updates": List["RuleUpdateTypeDef"],
        "RateLimit": int,
    },
)

UpdateRateBasedRuleResponseTypeDef = TypedDict(
    "UpdateRateBasedRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegexMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateRegexMatchSetRequestRequestTypeDef",
    {
        "RegexMatchSetId": str,
        "Updates": List["RegexMatchSetUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRegexMatchSetResponseTypeDef = TypedDict(
    "UpdateRegexMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegexPatternSetRequestRequestTypeDef = TypedDict(
    "UpdateRegexPatternSetRequestRequestTypeDef",
    {
        "RegexPatternSetId": str,
        "Updates": List["RegexPatternSetUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRegexPatternSetResponseTypeDef = TypedDict(
    "UpdateRegexPatternSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleGroupRequestRequestTypeDef = TypedDict(
    "UpdateRuleGroupRequestRequestTypeDef",
    {
        "RuleGroupId": str,
        "Updates": List["RuleGroupUpdateTypeDef"],
        "ChangeToken": str,
    },
)

UpdateRuleGroupResponseTypeDef = TypedDict(
    "UpdateRuleGroupResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuleRequestRequestTypeDef = TypedDict(
    "UpdateRuleRequestRequestTypeDef",
    {
        "RuleId": str,
        "ChangeToken": str,
        "Updates": List["RuleUpdateTypeDef"],
    },
)

UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSizeConstraintSetRequestRequestTypeDef = TypedDict(
    "UpdateSizeConstraintSetRequestRequestTypeDef",
    {
        "SizeConstraintSetId": str,
        "ChangeToken": str,
        "Updates": List["SizeConstraintSetUpdateTypeDef"],
    },
)

UpdateSizeConstraintSetResponseTypeDef = TypedDict(
    "UpdateSizeConstraintSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSqlInjectionMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetRequestRequestTypeDef",
    {
        "SqlInjectionMatchSetId": str,
        "ChangeToken": str,
        "Updates": List["SqlInjectionMatchSetUpdateTypeDef"],
    },
)

UpdateSqlInjectionMatchSetResponseTypeDef = TypedDict(
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateWebACLRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateWebACLRequestRequestTypeDef",
    {
        "WebACLId": str,
        "ChangeToken": str,
    },
)
_OptionalUpdateWebACLRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateWebACLRequestRequestTypeDef",
    {
        "Updates": List["WebACLUpdateTypeDef"],
        "DefaultAction": "WafActionTypeDef",
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
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateXssMatchSetRequestRequestTypeDef = TypedDict(
    "UpdateXssMatchSetRequestRequestTypeDef",
    {
        "XssMatchSetId": str,
        "ChangeToken": str,
        "Updates": List["XssMatchSetUpdateTypeDef"],
    },
)

UpdateXssMatchSetResponseTypeDef = TypedDict(
    "UpdateXssMatchSetResponseTypeDef",
    {
        "ChangeToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WafActionTypeDef = TypedDict(
    "WafActionTypeDef",
    {
        "Type": WafActionTypeType,
    },
)

WafOverrideActionTypeDef = TypedDict(
    "WafOverrideActionTypeDef",
    {
        "Type": WafOverrideActionTypeType,
    },
)

WebACLSummaryTypeDef = TypedDict(
    "WebACLSummaryTypeDef",
    {
        "WebACLId": str,
        "Name": str,
    },
)

_RequiredWebACLTypeDef = TypedDict(
    "_RequiredWebACLTypeDef",
    {
        "WebACLId": str,
        "DefaultAction": "WafActionTypeDef",
        "Rules": List["ActivatedRuleTypeDef"],
    },
)
_OptionalWebACLTypeDef = TypedDict(
    "_OptionalWebACLTypeDef",
    {
        "Name": str,
        "MetricName": str,
        "WebACLArn": str,
    },
    total=False,
)

class WebACLTypeDef(_RequiredWebACLTypeDef, _OptionalWebACLTypeDef):
    pass

WebACLUpdateTypeDef = TypedDict(
    "WebACLUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "ActivatedRule": "ActivatedRuleTypeDef",
    },
)

XssMatchSetSummaryTypeDef = TypedDict(
    "XssMatchSetSummaryTypeDef",
    {
        "XssMatchSetId": str,
        "Name": str,
    },
)

_RequiredXssMatchSetTypeDef = TypedDict(
    "_RequiredXssMatchSetTypeDef",
    {
        "XssMatchSetId": str,
        "XssMatchTuples": List["XssMatchTupleTypeDef"],
    },
)
_OptionalXssMatchSetTypeDef = TypedDict(
    "_OptionalXssMatchSetTypeDef",
    {
        "Name": str,
    },
    total=False,
)

class XssMatchSetTypeDef(_RequiredXssMatchSetTypeDef, _OptionalXssMatchSetTypeDef):
    pass

XssMatchSetUpdateTypeDef = TypedDict(
    "XssMatchSetUpdateTypeDef",
    {
        "Action": ChangeActionType,
        "XssMatchTuple": "XssMatchTupleTypeDef",
    },
)

XssMatchTupleTypeDef = TypedDict(
    "XssMatchTupleTypeDef",
    {
        "FieldToMatch": "FieldToMatchTypeDef",
        "TextTransformation": TextTransformationType,
    },
)
