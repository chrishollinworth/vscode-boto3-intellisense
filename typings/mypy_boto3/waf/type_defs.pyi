"""
Type annotations for waf service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_waf/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_waf.type_defs import ExcludedRuleTypeDef

    data: ExcludedRuleTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    ChangeActionType,
    ChangeTokenStatusType,
    ComparisonOperatorType,
    GeoMatchConstraintValueType,
    IPSetDescriptorTypeType,
    MatchFieldTypeType,
    PositionalConstraintType,
    PredicateTypeType,
    TextTransformationType,
    WafActionTypeType,
    WafOverrideActionTypeType,
    WafRuleTypeType,
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
    "ActivatedRuleOutputTypeDef",
    "ActivatedRuleTypeDef",
    "ActivatedRuleUnionTypeDef",
    "BlobTypeDef",
    "ByteMatchSetSummaryTypeDef",
    "ByteMatchSetTypeDef",
    "ByteMatchSetUpdateTypeDef",
    "ByteMatchTupleOutputTypeDef",
    "ByteMatchTupleTypeDef",
    "ByteMatchTupleUnionTypeDef",
    "CreateByteMatchSetRequestTypeDef",
    "CreateByteMatchSetResponseTypeDef",
    "CreateGeoMatchSetRequestTypeDef",
    "CreateGeoMatchSetResponseTypeDef",
    "CreateIPSetRequestTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRateBasedRuleRequestTypeDef",
    "CreateRateBasedRuleResponseTypeDef",
    "CreateRegexMatchSetRequestTypeDef",
    "CreateRegexMatchSetResponseTypeDef",
    "CreateRegexPatternSetRequestTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupRequestTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateRuleRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateSizeConstraintSetRequestTypeDef",
    "CreateSizeConstraintSetResponseTypeDef",
    "CreateSqlInjectionMatchSetRequestTypeDef",
    "CreateSqlInjectionMatchSetResponseTypeDef",
    "CreateWebACLMigrationStackRequestTypeDef",
    "CreateWebACLMigrationStackResponseTypeDef",
    "CreateWebACLRequestTypeDef",
    "CreateWebACLResponseTypeDef",
    "CreateXssMatchSetRequestTypeDef",
    "CreateXssMatchSetResponseTypeDef",
    "DeleteByteMatchSetRequestTypeDef",
    "DeleteByteMatchSetResponseTypeDef",
    "DeleteGeoMatchSetRequestTypeDef",
    "DeleteGeoMatchSetResponseTypeDef",
    "DeleteIPSetRequestTypeDef",
    "DeleteIPSetResponseTypeDef",
    "DeleteLoggingConfigurationRequestTypeDef",
    "DeletePermissionPolicyRequestTypeDef",
    "DeleteRateBasedRuleRequestTypeDef",
    "DeleteRateBasedRuleResponseTypeDef",
    "DeleteRegexMatchSetRequestTypeDef",
    "DeleteRegexMatchSetResponseTypeDef",
    "DeleteRegexPatternSetRequestTypeDef",
    "DeleteRegexPatternSetResponseTypeDef",
    "DeleteRuleGroupRequestTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DeleteRuleRequestTypeDef",
    "DeleteRuleResponseTypeDef",
    "DeleteSizeConstraintSetRequestTypeDef",
    "DeleteSizeConstraintSetResponseTypeDef",
    "DeleteSqlInjectionMatchSetRequestTypeDef",
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    "DeleteWebACLRequestTypeDef",
    "DeleteWebACLResponseTypeDef",
    "DeleteXssMatchSetRequestTypeDef",
    "DeleteXssMatchSetResponseTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "GeoMatchConstraintTypeDef",
    "GeoMatchSetSummaryTypeDef",
    "GeoMatchSetTypeDef",
    "GeoMatchSetUpdateTypeDef",
    "GetByteMatchSetRequestTypeDef",
    "GetByteMatchSetResponseTypeDef",
    "GetChangeTokenResponseTypeDef",
    "GetChangeTokenStatusRequestTypeDef",
    "GetChangeTokenStatusResponseTypeDef",
    "GetGeoMatchSetRequestTypeDef",
    "GetGeoMatchSetResponseTypeDef",
    "GetIPSetRequestTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationRequestTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetPermissionPolicyRequestTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedRuleManagedKeysRequestPaginateTypeDef",
    "GetRateBasedRuleManagedKeysRequestTypeDef",
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    "GetRateBasedRuleRequestTypeDef",
    "GetRateBasedRuleResponseTypeDef",
    "GetRegexMatchSetRequestTypeDef",
    "GetRegexMatchSetResponseTypeDef",
    "GetRegexPatternSetRequestTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupRequestTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetRuleRequestTypeDef",
    "GetRuleResponseTypeDef",
    "GetSampledRequestsRequestTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetSizeConstraintSetRequestTypeDef",
    "GetSizeConstraintSetResponseTypeDef",
    "GetSqlInjectionMatchSetRequestTypeDef",
    "GetSqlInjectionMatchSetResponseTypeDef",
    "GetWebACLRequestTypeDef",
    "GetWebACLResponseTypeDef",
    "GetXssMatchSetRequestTypeDef",
    "GetXssMatchSetResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetDescriptorTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "IPSetUpdateTypeDef",
    "ListActivatedRulesInRuleGroupRequestPaginateTypeDef",
    "ListActivatedRulesInRuleGroupRequestTypeDef",
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    "ListByteMatchSetsRequestPaginateTypeDef",
    "ListByteMatchSetsRequestTypeDef",
    "ListByteMatchSetsResponseTypeDef",
    "ListGeoMatchSetsRequestPaginateTypeDef",
    "ListGeoMatchSetsRequestTypeDef",
    "ListGeoMatchSetsResponseTypeDef",
    "ListIPSetsRequestPaginateTypeDef",
    "ListIPSetsRequestTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsRequestPaginateTypeDef",
    "ListLoggingConfigurationsRequestTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRateBasedRulesRequestPaginateTypeDef",
    "ListRateBasedRulesRequestTypeDef",
    "ListRateBasedRulesResponseTypeDef",
    "ListRegexMatchSetsRequestPaginateTypeDef",
    "ListRegexMatchSetsRequestTypeDef",
    "ListRegexMatchSetsResponseTypeDef",
    "ListRegexPatternSetsRequestPaginateTypeDef",
    "ListRegexPatternSetsRequestTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListRuleGroupsRequestPaginateTypeDef",
    "ListRuleGroupsRequestTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListRulesRequestPaginateTypeDef",
    "ListRulesRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListSizeConstraintSetsRequestPaginateTypeDef",
    "ListSizeConstraintSetsRequestTypeDef",
    "ListSizeConstraintSetsResponseTypeDef",
    "ListSqlInjectionMatchSetsRequestPaginateTypeDef",
    "ListSqlInjectionMatchSetsRequestTypeDef",
    "ListSqlInjectionMatchSetsResponseTypeDef",
    "ListSubscribedRuleGroupsRequestPaginateTypeDef",
    "ListSubscribedRuleGroupsRequestTypeDef",
    "ListSubscribedRuleGroupsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsRequestPaginateTypeDef",
    "ListWebACLsRequestTypeDef",
    "ListWebACLsResponseTypeDef",
    "ListXssMatchSetsRequestPaginateTypeDef",
    "ListXssMatchSetsRequestTypeDef",
    "ListXssMatchSetsResponseTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "LoggingConfigurationUnionTypeDef",
    "PaginatorConfigTypeDef",
    "PredicateTypeDef",
    "PutLoggingConfigurationRequestTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "PutPermissionPolicyRequestTypeDef",
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
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimeWindowOutputTypeDef",
    "TimeWindowTypeDef",
    "TimeWindowUnionTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateByteMatchSetRequestTypeDef",
    "UpdateByteMatchSetResponseTypeDef",
    "UpdateGeoMatchSetRequestTypeDef",
    "UpdateGeoMatchSetResponseTypeDef",
    "UpdateIPSetRequestTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRateBasedRuleRequestTypeDef",
    "UpdateRateBasedRuleResponseTypeDef",
    "UpdateRegexMatchSetRequestTypeDef",
    "UpdateRegexMatchSetResponseTypeDef",
    "UpdateRegexPatternSetRequestTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupRequestTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateRuleRequestTypeDef",
    "UpdateRuleResponseTypeDef",
    "UpdateSizeConstraintSetRequestTypeDef",
    "UpdateSizeConstraintSetResponseTypeDef",
    "UpdateSqlInjectionMatchSetRequestTypeDef",
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    "UpdateWebACLRequestTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UpdateXssMatchSetRequestTypeDef",
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

class ExcludedRuleTypeDef(TypedDict):
    RuleId: str

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
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class ByteMatchSetSummaryTypeDef(TypedDict):
    ByteMatchSetId: str
    Name: str

FieldToMatchTypeDef = TypedDict(
    "FieldToMatchTypeDef",
    {
        "Type": MatchFieldTypeType,
        "Data": NotRequired[str],
    },
)

class CreateByteMatchSetRequestTypeDef(TypedDict):
    Name: str
    ChangeToken: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateGeoMatchSetRequestTypeDef(TypedDict):
    Name: str
    ChangeToken: str

class CreateIPSetRequestTypeDef(TypedDict):
    Name: str
    ChangeToken: str

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class CreateRegexMatchSetRequestTypeDef(TypedDict):
    Name: str
    ChangeToken: str

class CreateRegexPatternSetRequestTypeDef(TypedDict):
    Name: str
    ChangeToken: str

class RegexPatternSetTypeDef(TypedDict):
    RegexPatternSetId: str
    RegexPatternStrings: List[str]
    Name: NotRequired[str]

class RuleGroupTypeDef(TypedDict):
    RuleGroupId: str
    Name: NotRequired[str]
    MetricName: NotRequired[str]

class CreateSizeConstraintSetRequestTypeDef(TypedDict):
    Name: str
    ChangeToken: str

class CreateSqlInjectionMatchSetRequestTypeDef(TypedDict):
    Name: str
    ChangeToken: str

class CreateWebACLMigrationStackRequestTypeDef(TypedDict):
    WebACLId: str
    S3BucketName: str
    IgnoreUnsupportedType: bool

class CreateXssMatchSetRequestTypeDef(TypedDict):
    Name: str
    ChangeToken: str

class DeleteByteMatchSetRequestTypeDef(TypedDict):
    ByteMatchSetId: str
    ChangeToken: str

class DeleteGeoMatchSetRequestTypeDef(TypedDict):
    GeoMatchSetId: str
    ChangeToken: str

class DeleteIPSetRequestTypeDef(TypedDict):
    IPSetId: str
    ChangeToken: str

class DeleteLoggingConfigurationRequestTypeDef(TypedDict):
    ResourceArn: str

class DeletePermissionPolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class DeleteRateBasedRuleRequestTypeDef(TypedDict):
    RuleId: str
    ChangeToken: str

class DeleteRegexMatchSetRequestTypeDef(TypedDict):
    RegexMatchSetId: str
    ChangeToken: str

class DeleteRegexPatternSetRequestTypeDef(TypedDict):
    RegexPatternSetId: str
    ChangeToken: str

class DeleteRuleGroupRequestTypeDef(TypedDict):
    RuleGroupId: str
    ChangeToken: str

class DeleteRuleRequestTypeDef(TypedDict):
    RuleId: str
    ChangeToken: str

class DeleteSizeConstraintSetRequestTypeDef(TypedDict):
    SizeConstraintSetId: str
    ChangeToken: str

class DeleteSqlInjectionMatchSetRequestTypeDef(TypedDict):
    SqlInjectionMatchSetId: str
    ChangeToken: str

class DeleteWebACLRequestTypeDef(TypedDict):
    WebACLId: str
    ChangeToken: str

class DeleteXssMatchSetRequestTypeDef(TypedDict):
    XssMatchSetId: str
    ChangeToken: str

GeoMatchConstraintTypeDef = TypedDict(
    "GeoMatchConstraintTypeDef",
    {
        "Type": Literal["Country"],
        "Value": GeoMatchConstraintValueType,
    },
)

class GeoMatchSetSummaryTypeDef(TypedDict):
    GeoMatchSetId: str
    Name: str

class GetByteMatchSetRequestTypeDef(TypedDict):
    ByteMatchSetId: str

class GetChangeTokenStatusRequestTypeDef(TypedDict):
    ChangeToken: str

class GetGeoMatchSetRequestTypeDef(TypedDict):
    GeoMatchSetId: str

class GetIPSetRequestTypeDef(TypedDict):
    IPSetId: str

class GetLoggingConfigurationRequestTypeDef(TypedDict):
    ResourceArn: str

class GetPermissionPolicyRequestTypeDef(TypedDict):
    ResourceArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetRateBasedRuleManagedKeysRequestTypeDef(TypedDict):
    RuleId: str
    NextMarker: NotRequired[str]

class GetRateBasedRuleRequestTypeDef(TypedDict):
    RuleId: str

class GetRegexMatchSetRequestTypeDef(TypedDict):
    RegexMatchSetId: str

class GetRegexPatternSetRequestTypeDef(TypedDict):
    RegexPatternSetId: str

class GetRuleGroupRequestTypeDef(TypedDict):
    RuleGroupId: str

class GetRuleRequestTypeDef(TypedDict):
    RuleId: str

class TimeWindowOutputTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime

class GetSizeConstraintSetRequestTypeDef(TypedDict):
    SizeConstraintSetId: str

class GetSqlInjectionMatchSetRequestTypeDef(TypedDict):
    SqlInjectionMatchSetId: str

class GetWebACLRequestTypeDef(TypedDict):
    WebACLId: str

class GetXssMatchSetRequestTypeDef(TypedDict):
    XssMatchSetId: str

class HTTPHeaderTypeDef(TypedDict):
    Name: NotRequired[str]
    Value: NotRequired[str]

IPSetDescriptorTypeDef = TypedDict(
    "IPSetDescriptorTypeDef",
    {
        "Type": IPSetDescriptorTypeType,
        "Value": str,
    },
)

class IPSetSummaryTypeDef(TypedDict):
    IPSetId: str
    Name: str

class ListActivatedRulesInRuleGroupRequestTypeDef(TypedDict):
    RuleGroupId: NotRequired[str]
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListByteMatchSetsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListGeoMatchSetsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListIPSetsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListLoggingConfigurationsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListRateBasedRulesRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class RuleSummaryTypeDef(TypedDict):
    RuleId: str
    Name: str

class ListRegexMatchSetsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class RegexMatchSetSummaryTypeDef(TypedDict):
    RegexMatchSetId: str
    Name: str

class ListRegexPatternSetsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class RegexPatternSetSummaryTypeDef(TypedDict):
    RegexPatternSetId: str
    Name: str

class ListRuleGroupsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class RuleGroupSummaryTypeDef(TypedDict):
    RuleGroupId: str
    Name: str

class ListRulesRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListSizeConstraintSetsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class SizeConstraintSetSummaryTypeDef(TypedDict):
    SizeConstraintSetId: str
    Name: str

class ListSqlInjectionMatchSetsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class SqlInjectionMatchSetSummaryTypeDef(TypedDict):
    SqlInjectionMatchSetId: str
    Name: str

class ListSubscribedRuleGroupsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class SubscribedRuleGroupSummaryTypeDef(TypedDict):
    RuleGroupId: str
    Name: str
    MetricName: str

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class ListWebACLsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class WebACLSummaryTypeDef(TypedDict):
    WebACLId: str
    Name: str

class ListXssMatchSetsRequestTypeDef(TypedDict):
    NextMarker: NotRequired[str]
    Limit: NotRequired[int]

class XssMatchSetSummaryTypeDef(TypedDict):
    XssMatchSetId: str
    Name: str

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Negated": bool,
        "Type": PredicateTypeType,
        "DataId": str,
    },
)

class PutPermissionPolicyRequestTypeDef(TypedDict):
    ResourceArn: str
    Policy: str

class RegexPatternSetUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    RegexPatternString: str

TimestampTypeDef = Union[datetime, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

ActivatedRuleOutputTypeDef = TypedDict(
    "ActivatedRuleOutputTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": NotRequired[WafActionTypeDef],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Type": NotRequired[WafRuleTypeType],
        "ExcludedRules": NotRequired[List[ExcludedRuleTypeDef]],
    },
)
ActivatedRuleTypeDef = TypedDict(
    "ActivatedRuleTypeDef",
    {
        "Priority": int,
        "RuleId": str,
        "Action": NotRequired[WafActionTypeDef],
        "OverrideAction": NotRequired[WafOverrideActionTypeDef],
        "Type": NotRequired[WafRuleTypeType],
        "ExcludedRules": NotRequired[Sequence[ExcludedRuleTypeDef]],
    },
)

class ByteMatchTupleOutputTypeDef(TypedDict):
    FieldToMatch: FieldToMatchTypeDef
    TargetString: bytes
    TextTransformation: TextTransformationType
    PositionalConstraint: PositionalConstraintType

class ByteMatchTupleTypeDef(TypedDict):
    FieldToMatch: FieldToMatchTypeDef
    TargetString: BlobTypeDef
    TextTransformation: TextTransformationType
    PositionalConstraint: PositionalConstraintType

class LoggingConfigurationOutputTypeDef(TypedDict):
    ResourceArn: str
    LogDestinationConfigs: List[str]
    RedactedFields: NotRequired[List[FieldToMatchTypeDef]]

class LoggingConfigurationTypeDef(TypedDict):
    ResourceArn: str
    LogDestinationConfigs: Sequence[str]
    RedactedFields: NotRequired[Sequence[FieldToMatchTypeDef]]

class RegexMatchTupleTypeDef(TypedDict):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType
    RegexPatternSetId: str

class SizeConstraintTypeDef(TypedDict):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType
    ComparisonOperator: ComparisonOperatorType
    Size: int

class SqlInjectionMatchTupleTypeDef(TypedDict):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType

class XssMatchTupleTypeDef(TypedDict):
    FieldToMatch: FieldToMatchTypeDef
    TextTransformation: TextTransformationType

class CreateWebACLMigrationStackResponseTypeDef(TypedDict):
    S3ObjectUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteByteMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGeoMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIPSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRateBasedRuleResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegexMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegexPatternSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleGroupResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSizeConstraintSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSqlInjectionMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWebACLResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteXssMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeTokenResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeTokenStatusResponseTypeDef(TypedDict):
    ChangeTokenStatus: ChangeTokenStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionPolicyResponseTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedRuleManagedKeysResponseTypeDef(TypedDict):
    ManagedKeys: List[str]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListByteMatchSetsResponseTypeDef(TypedDict):
    NextMarker: str
    ByteMatchSets: List[ByteMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateByteMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeoMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIPSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRateBasedRuleResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexPatternSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleGroupResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSizeConstraintSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSqlInjectionMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebACLResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateXssMatchSetResponseTypeDef(TypedDict):
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRateBasedRuleRequestTypeDef(TypedDict):
    Name: str
    MetricName: str
    RateKey: Literal["IP"]
    RateLimit: int
    ChangeToken: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateRuleGroupRequestTypeDef(TypedDict):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateRuleRequestTypeDef(TypedDict):
    Name: str
    MetricName: str
    ChangeToken: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateWebACLRequestTypeDef(TypedDict):
    Name: str
    MetricName: str
    DefaultAction: WafActionTypeDef
    ChangeToken: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagInfoForResourceTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    TagList: NotRequired[List[TagTypeDef]]

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateRegexPatternSetResponseTypeDef(TypedDict):
    RegexPatternSet: RegexPatternSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegexPatternSetResponseTypeDef(TypedDict):
    RegexPatternSet: RegexPatternSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleGroupResponseTypeDef(TypedDict):
    RuleGroup: RuleGroupTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleGroupResponseTypeDef(TypedDict):
    RuleGroup: RuleGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GeoMatchSetTypeDef(TypedDict):
    GeoMatchSetId: str
    GeoMatchConstraints: List[GeoMatchConstraintTypeDef]
    Name: NotRequired[str]

class GeoMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    GeoMatchConstraint: GeoMatchConstraintTypeDef

class ListGeoMatchSetsResponseTypeDef(TypedDict):
    NextMarker: str
    GeoMatchSets: List[GeoMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedRuleManagedKeysRequestPaginateTypeDef(TypedDict):
    RuleId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListActivatedRulesInRuleGroupRequestPaginateTypeDef(TypedDict):
    RuleGroupId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListByteMatchSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGeoMatchSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListIPSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLoggingConfigurationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRateBasedRulesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegexMatchSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegexPatternSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRuleGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRulesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSizeConstraintSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSqlInjectionMatchSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubscribedRuleGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWebACLsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListXssMatchSetsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class HTTPRequestTypeDef(TypedDict):
    ClientIP: NotRequired[str]
    Country: NotRequired[str]
    URI: NotRequired[str]
    Method: NotRequired[str]
    HTTPVersion: NotRequired[str]
    Headers: NotRequired[List[HTTPHeaderTypeDef]]

class IPSetTypeDef(TypedDict):
    IPSetId: str
    IPSetDescriptors: List[IPSetDescriptorTypeDef]
    Name: NotRequired[str]

class IPSetUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    IPSetDescriptor: IPSetDescriptorTypeDef

class ListIPSetsResponseTypeDef(TypedDict):
    NextMarker: str
    IPSets: List[IPSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRateBasedRulesResponseTypeDef(TypedDict):
    NextMarker: str
    Rules: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesResponseTypeDef(TypedDict):
    NextMarker: str
    Rules: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRegexMatchSetsResponseTypeDef(TypedDict):
    NextMarker: str
    RegexMatchSets: List[RegexMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRegexPatternSetsResponseTypeDef(TypedDict):
    NextMarker: str
    RegexPatternSets: List[RegexPatternSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRuleGroupsResponseTypeDef(TypedDict):
    NextMarker: str
    RuleGroups: List[RuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSizeConstraintSetsResponseTypeDef(TypedDict):
    NextMarker: str
    SizeConstraintSets: List[SizeConstraintSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSqlInjectionMatchSetsResponseTypeDef(TypedDict):
    NextMarker: str
    SqlInjectionMatchSets: List[SqlInjectionMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubscribedRuleGroupsResponseTypeDef(TypedDict):
    NextMarker: str
    RuleGroups: List[SubscribedRuleGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebACLsResponseTypeDef(TypedDict):
    NextMarker: str
    WebACLs: List[WebACLSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListXssMatchSetsResponseTypeDef(TypedDict):
    NextMarker: str
    XssMatchSets: List[XssMatchSetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RateBasedRuleTypeDef(TypedDict):
    RuleId: str
    MatchPredicates: List[PredicateTypeDef]
    RateKey: Literal["IP"]
    RateLimit: int
    Name: NotRequired[str]
    MetricName: NotRequired[str]

class RuleTypeDef(TypedDict):
    RuleId: str
    Predicates: List[PredicateTypeDef]
    Name: NotRequired[str]
    MetricName: NotRequired[str]

class RuleUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    Predicate: PredicateTypeDef

class UpdateRegexPatternSetRequestTypeDef(TypedDict):
    RegexPatternSetId: str
    Updates: Sequence[RegexPatternSetUpdateTypeDef]
    ChangeToken: str

class TimeWindowTypeDef(TypedDict):
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class ListActivatedRulesInRuleGroupResponseTypeDef(TypedDict):
    NextMarker: str
    ActivatedRules: List[ActivatedRuleOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class WebACLTypeDef(TypedDict):
    WebACLId: str
    DefaultAction: WafActionTypeDef
    Rules: List[ActivatedRuleOutputTypeDef]
    Name: NotRequired[str]
    MetricName: NotRequired[str]
    WebACLArn: NotRequired[str]

ActivatedRuleUnionTypeDef = Union[ActivatedRuleTypeDef, ActivatedRuleOutputTypeDef]

class ByteMatchSetTypeDef(TypedDict):
    ByteMatchSetId: str
    ByteMatchTuples: List[ByteMatchTupleOutputTypeDef]
    Name: NotRequired[str]

ByteMatchTupleUnionTypeDef = Union[ByteMatchTupleTypeDef, ByteMatchTupleOutputTypeDef]

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

LoggingConfigurationUnionTypeDef = Union[
    LoggingConfigurationTypeDef, LoggingConfigurationOutputTypeDef
]

class RegexMatchSetTypeDef(TypedDict):
    RegexMatchSetId: NotRequired[str]
    Name: NotRequired[str]
    RegexMatchTuples: NotRequired[List[RegexMatchTupleTypeDef]]

class RegexMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    RegexMatchTuple: RegexMatchTupleTypeDef

class SizeConstraintSetTypeDef(TypedDict):
    SizeConstraintSetId: str
    SizeConstraints: List[SizeConstraintTypeDef]
    Name: NotRequired[str]

class SizeConstraintSetUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    SizeConstraint: SizeConstraintTypeDef

class SqlInjectionMatchSetTypeDef(TypedDict):
    SqlInjectionMatchSetId: str
    SqlInjectionMatchTuples: List[SqlInjectionMatchTupleTypeDef]
    Name: NotRequired[str]

class SqlInjectionMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    SqlInjectionMatchTuple: SqlInjectionMatchTupleTypeDef

class XssMatchSetTypeDef(TypedDict):
    XssMatchSetId: str
    XssMatchTuples: List[XssMatchTupleTypeDef]
    Name: NotRequired[str]

class XssMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    XssMatchTuple: XssMatchTupleTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    NextMarker: str
    TagInfoForResource: TagInfoForResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGeoMatchSetResponseTypeDef(TypedDict):
    GeoMatchSet: GeoMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGeoMatchSetResponseTypeDef(TypedDict):
    GeoMatchSet: GeoMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGeoMatchSetRequestTypeDef(TypedDict):
    GeoMatchSetId: str
    ChangeToken: str
    Updates: Sequence[GeoMatchSetUpdateTypeDef]

class SampledHTTPRequestTypeDef(TypedDict):
    Request: HTTPRequestTypeDef
    Weight: int
    Timestamp: NotRequired[datetime]
    Action: NotRequired[str]
    RuleWithinRuleGroup: NotRequired[str]

class CreateIPSetResponseTypeDef(TypedDict):
    IPSet: IPSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIPSetResponseTypeDef(TypedDict):
    IPSet: IPSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIPSetRequestTypeDef(TypedDict):
    IPSetId: str
    ChangeToken: str
    Updates: Sequence[IPSetUpdateTypeDef]

class CreateRateBasedRuleResponseTypeDef(TypedDict):
    Rule: RateBasedRuleTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRateBasedRuleResponseTypeDef(TypedDict):
    Rule: RateBasedRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleResponseTypeDef(TypedDict):
    Rule: RuleTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleResponseTypeDef(TypedDict):
    Rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRateBasedRuleRequestTypeDef(TypedDict):
    RuleId: str
    ChangeToken: str
    Updates: Sequence[RuleUpdateTypeDef]
    RateLimit: int

class UpdateRuleRequestTypeDef(TypedDict):
    RuleId: str
    ChangeToken: str
    Updates: Sequence[RuleUpdateTypeDef]

TimeWindowUnionTypeDef = Union[TimeWindowTypeDef, TimeWindowOutputTypeDef]

class CreateWebACLResponseTypeDef(TypedDict):
    WebACL: WebACLTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWebACLResponseTypeDef(TypedDict):
    WebACL: WebACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RuleGroupUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleUnionTypeDef

class WebACLUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    ActivatedRule: ActivatedRuleUnionTypeDef

class CreateByteMatchSetResponseTypeDef(TypedDict):
    ByteMatchSet: ByteMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetByteMatchSetResponseTypeDef(TypedDict):
    ByteMatchSet: ByteMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ByteMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeActionType
    ByteMatchTuple: ByteMatchTupleUnionTypeDef

class PutLoggingConfigurationRequestTypeDef(TypedDict):
    LoggingConfiguration: LoggingConfigurationUnionTypeDef

class CreateRegexMatchSetResponseTypeDef(TypedDict):
    RegexMatchSet: RegexMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegexMatchSetResponseTypeDef(TypedDict):
    RegexMatchSet: RegexMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegexMatchSetRequestTypeDef(TypedDict):
    RegexMatchSetId: str
    Updates: Sequence[RegexMatchSetUpdateTypeDef]
    ChangeToken: str

class CreateSizeConstraintSetResponseTypeDef(TypedDict):
    SizeConstraintSet: SizeConstraintSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSizeConstraintSetResponseTypeDef(TypedDict):
    SizeConstraintSet: SizeConstraintSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSizeConstraintSetRequestTypeDef(TypedDict):
    SizeConstraintSetId: str
    ChangeToken: str
    Updates: Sequence[SizeConstraintSetUpdateTypeDef]

class CreateSqlInjectionMatchSetResponseTypeDef(TypedDict):
    SqlInjectionMatchSet: SqlInjectionMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSqlInjectionMatchSetResponseTypeDef(TypedDict):
    SqlInjectionMatchSet: SqlInjectionMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSqlInjectionMatchSetRequestTypeDef(TypedDict):
    SqlInjectionMatchSetId: str
    ChangeToken: str
    Updates: Sequence[SqlInjectionMatchSetUpdateTypeDef]

class CreateXssMatchSetResponseTypeDef(TypedDict):
    XssMatchSet: XssMatchSetTypeDef
    ChangeToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetXssMatchSetResponseTypeDef(TypedDict):
    XssMatchSet: XssMatchSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateXssMatchSetRequestTypeDef(TypedDict):
    XssMatchSetId: str
    ChangeToken: str
    Updates: Sequence[XssMatchSetUpdateTypeDef]

class GetSampledRequestsResponseTypeDef(TypedDict):
    SampledRequests: List[SampledHTTPRequestTypeDef]
    PopulationSize: int
    TimeWindow: TimeWindowOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSampledRequestsRequestTypeDef(TypedDict):
    WebAclId: str
    RuleId: str
    TimeWindow: TimeWindowUnionTypeDef
    MaxItems: int

class UpdateRuleGroupRequestTypeDef(TypedDict):
    RuleGroupId: str
    Updates: Sequence[RuleGroupUpdateTypeDef]
    ChangeToken: str

class UpdateWebACLRequestTypeDef(TypedDict):
    WebACLId: str
    ChangeToken: str
    Updates: NotRequired[Sequence[WebACLUpdateTypeDef]]
    DefaultAction: NotRequired[WafActionTypeDef]

class UpdateByteMatchSetRequestTypeDef(TypedDict):
    ByteMatchSetId: str
    ChangeToken: str
    Updates: Sequence[ByteMatchSetUpdateTypeDef]
