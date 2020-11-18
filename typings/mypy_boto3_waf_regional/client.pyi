# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for waf-regional service client

Usage::

    ```python
    import boto3
    from mypy_boto3_waf_regional import WAFRegionalClient

    client: WAFRegionalClient = boto3.client("waf-regional")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_waf_regional.type_defs import (
    ByteMatchSetUpdateTypeDef,
    CreateByteMatchSetResponseTypeDef,
    CreateGeoMatchSetResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateRateBasedRuleResponseTypeDef,
    CreateRegexMatchSetResponseTypeDef,
    CreateRegexPatternSetResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    CreateRuleResponseTypeDef,
    CreateSizeConstraintSetResponseTypeDef,
    CreateSqlInjectionMatchSetResponseTypeDef,
    CreateWebACLMigrationStackResponseTypeDef,
    CreateWebACLResponseTypeDef,
    CreateXssMatchSetResponseTypeDef,
    DeleteByteMatchSetResponseTypeDef,
    DeleteGeoMatchSetResponseTypeDef,
    DeleteIPSetResponseTypeDef,
    DeleteRateBasedRuleResponseTypeDef,
    DeleteRegexMatchSetResponseTypeDef,
    DeleteRegexPatternSetResponseTypeDef,
    DeleteRuleGroupResponseTypeDef,
    DeleteRuleResponseTypeDef,
    DeleteSizeConstraintSetResponseTypeDef,
    DeleteSqlInjectionMatchSetResponseTypeDef,
    DeleteWebACLResponseTypeDef,
    DeleteXssMatchSetResponseTypeDef,
    GeoMatchSetUpdateTypeDef,
    GetByteMatchSetResponseTypeDef,
    GetChangeTokenResponseTypeDef,
    GetChangeTokenStatusResponseTypeDef,
    GetGeoMatchSetResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetPermissionPolicyResponseTypeDef,
    GetRateBasedRuleManagedKeysResponseTypeDef,
    GetRateBasedRuleResponseTypeDef,
    GetRegexMatchSetResponseTypeDef,
    GetRegexPatternSetResponseTypeDef,
    GetRuleGroupResponseTypeDef,
    GetRuleResponseTypeDef,
    GetSampledRequestsResponseTypeDef,
    GetSizeConstraintSetResponseTypeDef,
    GetSqlInjectionMatchSetResponseTypeDef,
    GetWebACLForResourceResponseTypeDef,
    GetWebACLResponseTypeDef,
    GetXssMatchSetResponseTypeDef,
    IPSetUpdateTypeDef,
    ListActivatedRulesInRuleGroupResponseTypeDef,
    ListByteMatchSetsResponseTypeDef,
    ListGeoMatchSetsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRateBasedRulesResponseTypeDef,
    ListRegexMatchSetsResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListResourcesForWebACLResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListRulesResponseTypeDef,
    ListSizeConstraintSetsResponseTypeDef,
    ListSqlInjectionMatchSetsResponseTypeDef,
    ListSubscribedRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebACLsResponseTypeDef,
    ListXssMatchSetsResponseTypeDef,
    LoggingConfigurationTypeDef,
    PutLoggingConfigurationResponseTypeDef,
    RegexMatchSetUpdateTypeDef,
    RegexPatternSetUpdateTypeDef,
    RuleGroupUpdateTypeDef,
    RuleUpdateTypeDef,
    SizeConstraintSetUpdateTypeDef,
    SqlInjectionMatchSetUpdateTypeDef,
    TagTypeDef,
    TimeWindowTypeDef,
    UpdateByteMatchSetResponseTypeDef,
    UpdateGeoMatchSetResponseTypeDef,
    UpdateIPSetResponseTypeDef,
    UpdateRateBasedRuleResponseTypeDef,
    UpdateRegexMatchSetResponseTypeDef,
    UpdateRegexPatternSetResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateRuleResponseTypeDef,
    UpdateSizeConstraintSetResponseTypeDef,
    UpdateSqlInjectionMatchSetResponseTypeDef,
    UpdateWebACLResponseTypeDef,
    UpdateXssMatchSetResponseTypeDef,
    WafActionTypeDef,
    WebACLUpdateTypeDef,
    XssMatchSetUpdateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WAFRegionalClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    WAFBadRequestException: Type[BotocoreClientError]
    WAFDisallowedNameException: Type[BotocoreClientError]
    WAFEntityMigrationException: Type[BotocoreClientError]
    WAFInternalErrorException: Type[BotocoreClientError]
    WAFInvalidAccountException: Type[BotocoreClientError]
    WAFInvalidOperationException: Type[BotocoreClientError]
    WAFInvalidParameterException: Type[BotocoreClientError]
    WAFInvalidPermissionPolicyException: Type[BotocoreClientError]
    WAFInvalidRegexPatternException: Type[BotocoreClientError]
    WAFLimitsExceededException: Type[BotocoreClientError]
    WAFNonEmptyEntityException: Type[BotocoreClientError]
    WAFNonexistentContainerException: Type[BotocoreClientError]
    WAFNonexistentItemException: Type[BotocoreClientError]
    WAFReferencedItemException: Type[BotocoreClientError]
    WAFServiceLinkedRoleErrorException: Type[BotocoreClientError]
    WAFStaleDataException: Type[BotocoreClientError]
    WAFSubscriptionNotFoundException: Type[BotocoreClientError]
    WAFTagOperationException: Type[BotocoreClientError]
    WAFTagOperationInternalErrorException: Type[BotocoreClientError]
    WAFUnavailableEntityException: Type[BotocoreClientError]


class WAFRegionalClient:
    """
    [WAFRegional.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_web_acl(self, WebACLId: str, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.associate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.associate_web_acl)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.can_paginate)
        """

    def create_byte_match_set(
        self, Name: str, ChangeToken: str
    ) -> CreateByteMatchSetResponseTypeDef:
        """
        [Client.create_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_byte_match_set)
        """

    def create_geo_match_set(self, Name: str, ChangeToken: str) -> CreateGeoMatchSetResponseTypeDef:
        """
        [Client.create_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_geo_match_set)
        """

    def create_ip_set(self, Name: str, ChangeToken: str) -> CreateIPSetResponseTypeDef:
        """
        [Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_ip_set)
        """

    def create_rate_based_rule(
        self,
        Name: str,
        MetricName: str,
        RateKey: Literal["IP"],
        RateLimit: int,
        ChangeToken: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateRateBasedRuleResponseTypeDef:
        """
        [Client.create_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_rate_based_rule)
        """

    def create_regex_match_set(
        self, Name: str, ChangeToken: str
    ) -> CreateRegexMatchSetResponseTypeDef:
        """
        [Client.create_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_regex_match_set)
        """

    def create_regex_pattern_set(
        self, Name: str, ChangeToken: str
    ) -> CreateRegexPatternSetResponseTypeDef:
        """
        [Client.create_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_regex_pattern_set)
        """

    def create_rule(
        self, Name: str, MetricName: str, ChangeToken: str, Tags: List["TagTypeDef"] = None
    ) -> CreateRuleResponseTypeDef:
        """
        [Client.create_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_rule)
        """

    def create_rule_group(
        self, Name: str, MetricName: str, ChangeToken: str, Tags: List["TagTypeDef"] = None
    ) -> CreateRuleGroupResponseTypeDef:
        """
        [Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_rule_group)
        """

    def create_size_constraint_set(
        self, Name: str, ChangeToken: str
    ) -> CreateSizeConstraintSetResponseTypeDef:
        """
        [Client.create_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_size_constraint_set)
        """

    def create_sql_injection_match_set(
        self, Name: str, ChangeToken: str
    ) -> CreateSqlInjectionMatchSetResponseTypeDef:
        """
        [Client.create_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_sql_injection_match_set)
        """

    def create_web_acl(
        self,
        Name: str,
        MetricName: str,
        DefaultAction: "WafActionTypeDef",
        ChangeToken: str,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateWebACLResponseTypeDef:
        """
        [Client.create_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_web_acl)
        """

    def create_web_acl_migration_stack(
        self, WebACLId: str, S3BucketName: str, IgnoreUnsupportedType: bool
    ) -> CreateWebACLMigrationStackResponseTypeDef:
        """
        [Client.create_web_acl_migration_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_web_acl_migration_stack)
        """

    def create_xss_match_set(self, Name: str, ChangeToken: str) -> CreateXssMatchSetResponseTypeDef:
        """
        [Client.create_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.create_xss_match_set)
        """

    def delete_byte_match_set(
        self, ByteMatchSetId: str, ChangeToken: str
    ) -> DeleteByteMatchSetResponseTypeDef:
        """
        [Client.delete_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_byte_match_set)
        """

    def delete_geo_match_set(
        self, GeoMatchSetId: str, ChangeToken: str
    ) -> DeleteGeoMatchSetResponseTypeDef:
        """
        [Client.delete_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_geo_match_set)
        """

    def delete_ip_set(self, IPSetId: str, ChangeToken: str) -> DeleteIPSetResponseTypeDef:
        """
        [Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_ip_set)
        """

    def delete_logging_configuration(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_logging_configuration)
        """

    def delete_permission_policy(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_permission_policy)
        """

    def delete_rate_based_rule(
        self, RuleId: str, ChangeToken: str
    ) -> DeleteRateBasedRuleResponseTypeDef:
        """
        [Client.delete_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_rate_based_rule)
        """

    def delete_regex_match_set(
        self, RegexMatchSetId: str, ChangeToken: str
    ) -> DeleteRegexMatchSetResponseTypeDef:
        """
        [Client.delete_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_regex_match_set)
        """

    def delete_regex_pattern_set(
        self, RegexPatternSetId: str, ChangeToken: str
    ) -> DeleteRegexPatternSetResponseTypeDef:
        """
        [Client.delete_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_regex_pattern_set)
        """

    def delete_rule(self, RuleId: str, ChangeToken: str) -> DeleteRuleResponseTypeDef:
        """
        [Client.delete_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_rule)
        """

    def delete_rule_group(
        self, RuleGroupId: str, ChangeToken: str
    ) -> DeleteRuleGroupResponseTypeDef:
        """
        [Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_rule_group)
        """

    def delete_size_constraint_set(
        self, SizeConstraintSetId: str, ChangeToken: str
    ) -> DeleteSizeConstraintSetResponseTypeDef:
        """
        [Client.delete_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_size_constraint_set)
        """

    def delete_sql_injection_match_set(
        self, SqlInjectionMatchSetId: str, ChangeToken: str
    ) -> DeleteSqlInjectionMatchSetResponseTypeDef:
        """
        [Client.delete_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_sql_injection_match_set)
        """

    def delete_web_acl(self, WebACLId: str, ChangeToken: str) -> DeleteWebACLResponseTypeDef:
        """
        [Client.delete_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_web_acl)
        """

    def delete_xss_match_set(
        self, XssMatchSetId: str, ChangeToken: str
    ) -> DeleteXssMatchSetResponseTypeDef:
        """
        [Client.delete_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.delete_xss_match_set)
        """

    def disassociate_web_acl(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.disassociate_web_acl)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.generate_presigned_url)
        """

    def get_byte_match_set(self, ByteMatchSetId: str) -> GetByteMatchSetResponseTypeDef:
        """
        [Client.get_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_byte_match_set)
        """

    def get_change_token(self) -> GetChangeTokenResponseTypeDef:
        """
        [Client.get_change_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_change_token)
        """

    def get_change_token_status(self, ChangeToken: str) -> GetChangeTokenStatusResponseTypeDef:
        """
        [Client.get_change_token_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_change_token_status)
        """

    def get_geo_match_set(self, GeoMatchSetId: str) -> GetGeoMatchSetResponseTypeDef:
        """
        [Client.get_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_geo_match_set)
        """

    def get_ip_set(self, IPSetId: str) -> GetIPSetResponseTypeDef:
        """
        [Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_ip_set)
        """

    def get_logging_configuration(self, ResourceArn: str) -> GetLoggingConfigurationResponseTypeDef:
        """
        [Client.get_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_logging_configuration)
        """

    def get_permission_policy(self, ResourceArn: str) -> GetPermissionPolicyResponseTypeDef:
        """
        [Client.get_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_permission_policy)
        """

    def get_rate_based_rule(self, RuleId: str) -> GetRateBasedRuleResponseTypeDef:
        """
        [Client.get_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_rate_based_rule)
        """

    def get_rate_based_rule_managed_keys(
        self, RuleId: str, NextMarker: str = None
    ) -> GetRateBasedRuleManagedKeysResponseTypeDef:
        """
        [Client.get_rate_based_rule_managed_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_rate_based_rule_managed_keys)
        """

    def get_regex_match_set(self, RegexMatchSetId: str) -> GetRegexMatchSetResponseTypeDef:
        """
        [Client.get_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_regex_match_set)
        """

    def get_regex_pattern_set(self, RegexPatternSetId: str) -> GetRegexPatternSetResponseTypeDef:
        """
        [Client.get_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_regex_pattern_set)
        """

    def get_rule(self, RuleId: str) -> GetRuleResponseTypeDef:
        """
        [Client.get_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_rule)
        """

    def get_rule_group(self, RuleGroupId: str) -> GetRuleGroupResponseTypeDef:
        """
        [Client.get_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_rule_group)
        """

    def get_sampled_requests(
        self, WebAclId: str, RuleId: str, TimeWindow: "TimeWindowTypeDef", MaxItems: int
    ) -> GetSampledRequestsResponseTypeDef:
        """
        [Client.get_sampled_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_sampled_requests)
        """

    def get_size_constraint_set(
        self, SizeConstraintSetId: str
    ) -> GetSizeConstraintSetResponseTypeDef:
        """
        [Client.get_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_size_constraint_set)
        """

    def get_sql_injection_match_set(
        self, SqlInjectionMatchSetId: str
    ) -> GetSqlInjectionMatchSetResponseTypeDef:
        """
        [Client.get_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_sql_injection_match_set)
        """

    def get_web_acl(self, WebACLId: str) -> GetWebACLResponseTypeDef:
        """
        [Client.get_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_web_acl)
        """

    def get_web_acl_for_resource(self, ResourceArn: str) -> GetWebACLForResourceResponseTypeDef:
        """
        [Client.get_web_acl_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_web_acl_for_resource)
        """

    def get_xss_match_set(self, XssMatchSetId: str) -> GetXssMatchSetResponseTypeDef:
        """
        [Client.get_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.get_xss_match_set)
        """

    def list_activated_rules_in_rule_group(
        self, RuleGroupId: str = None, NextMarker: str = None, Limit: int = None
    ) -> ListActivatedRulesInRuleGroupResponseTypeDef:
        """
        [Client.list_activated_rules_in_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_activated_rules_in_rule_group)
        """

    def list_byte_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListByteMatchSetsResponseTypeDef:
        """
        [Client.list_byte_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_byte_match_sets)
        """

    def list_geo_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListGeoMatchSetsResponseTypeDef:
        """
        [Client.list_geo_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_geo_match_sets)
        """

    def list_ip_sets(self, NextMarker: str = None, Limit: int = None) -> ListIPSetsResponseTypeDef:
        """
        [Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_ip_sets)
        """

    def list_logging_configurations(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        [Client.list_logging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_logging_configurations)
        """

    def list_rate_based_rules(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListRateBasedRulesResponseTypeDef:
        """
        [Client.list_rate_based_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_rate_based_rules)
        """

    def list_regex_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListRegexMatchSetsResponseTypeDef:
        """
        [Client.list_regex_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_regex_match_sets)
        """

    def list_regex_pattern_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListRegexPatternSetsResponseTypeDef:
        """
        [Client.list_regex_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_regex_pattern_sets)
        """

    def list_resources_for_web_acl(
        self,
        WebACLId: str,
        ResourceType: Literal["APPLICATION_LOAD_BALANCER", "API_GATEWAY"] = None,
    ) -> ListResourcesForWebACLResponseTypeDef:
        """
        [Client.list_resources_for_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_resources_for_web_acl)
        """

    def list_rule_groups(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        [Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_rule_groups)
        """

    def list_rules(self, NextMarker: str = None, Limit: int = None) -> ListRulesResponseTypeDef:
        """
        [Client.list_rules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_rules)
        """

    def list_size_constraint_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListSizeConstraintSetsResponseTypeDef:
        """
        [Client.list_size_constraint_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_size_constraint_sets)
        """

    def list_sql_injection_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListSqlInjectionMatchSetsResponseTypeDef:
        """
        [Client.list_sql_injection_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_sql_injection_match_sets)
        """

    def list_subscribed_rule_groups(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListSubscribedRuleGroupsResponseTypeDef:
        """
        [Client.list_subscribed_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_subscribed_rule_groups)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_tags_for_resource)
        """

    def list_web_acls(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListWebACLsResponseTypeDef:
        """
        [Client.list_web_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_web_acls)
        """

    def list_xss_match_sets(
        self, NextMarker: str = None, Limit: int = None
    ) -> ListXssMatchSetsResponseTypeDef:
        """
        [Client.list_xss_match_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.list_xss_match_sets)
        """

    def put_logging_configuration(
        self, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutLoggingConfigurationResponseTypeDef:
        """
        [Client.put_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.put_logging_configuration)
        """

    def put_permission_policy(self, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        [Client.put_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.put_permission_policy)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.untag_resource)
        """

    def update_byte_match_set(
        self, ByteMatchSetId: str, ChangeToken: str, Updates: List[ByteMatchSetUpdateTypeDef]
    ) -> UpdateByteMatchSetResponseTypeDef:
        """
        [Client.update_byte_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_byte_match_set)
        """

    def update_geo_match_set(
        self, GeoMatchSetId: str, ChangeToken: str, Updates: List[GeoMatchSetUpdateTypeDef]
    ) -> UpdateGeoMatchSetResponseTypeDef:
        """
        [Client.update_geo_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_geo_match_set)
        """

    def update_ip_set(
        self, IPSetId: str, ChangeToken: str, Updates: List[IPSetUpdateTypeDef]
    ) -> UpdateIPSetResponseTypeDef:
        """
        [Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_ip_set)
        """

    def update_rate_based_rule(
        self, RuleId: str, ChangeToken: str, Updates: List[RuleUpdateTypeDef], RateLimit: int
    ) -> UpdateRateBasedRuleResponseTypeDef:
        """
        [Client.update_rate_based_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_rate_based_rule)
        """

    def update_regex_match_set(
        self, RegexMatchSetId: str, Updates: List[RegexMatchSetUpdateTypeDef], ChangeToken: str
    ) -> UpdateRegexMatchSetResponseTypeDef:
        """
        [Client.update_regex_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_regex_match_set)
        """

    def update_regex_pattern_set(
        self, RegexPatternSetId: str, Updates: List[RegexPatternSetUpdateTypeDef], ChangeToken: str
    ) -> UpdateRegexPatternSetResponseTypeDef:
        """
        [Client.update_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_regex_pattern_set)
        """

    def update_rule(
        self, RuleId: str, ChangeToken: str, Updates: List[RuleUpdateTypeDef]
    ) -> UpdateRuleResponseTypeDef:
        """
        [Client.update_rule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_rule)
        """

    def update_rule_group(
        self, RuleGroupId: str, Updates: List[RuleGroupUpdateTypeDef], ChangeToken: str
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        [Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_rule_group)
        """

    def update_size_constraint_set(
        self,
        SizeConstraintSetId: str,
        ChangeToken: str,
        Updates: List[SizeConstraintSetUpdateTypeDef],
    ) -> UpdateSizeConstraintSetResponseTypeDef:
        """
        [Client.update_size_constraint_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_size_constraint_set)
        """

    def update_sql_injection_match_set(
        self,
        SqlInjectionMatchSetId: str,
        ChangeToken: str,
        Updates: List[SqlInjectionMatchSetUpdateTypeDef],
    ) -> UpdateSqlInjectionMatchSetResponseTypeDef:
        """
        [Client.update_sql_injection_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_sql_injection_match_set)
        """

    def update_web_acl(
        self,
        WebACLId: str,
        ChangeToken: str,
        Updates: List[WebACLUpdateTypeDef] = None,
        DefaultAction: "WafActionTypeDef" = None,
    ) -> UpdateWebACLResponseTypeDef:
        """
        [Client.update_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_web_acl)
        """

    def update_xss_match_set(
        self, XssMatchSetId: str, ChangeToken: str, Updates: List[XssMatchSetUpdateTypeDef]
    ) -> UpdateXssMatchSetResponseTypeDef:
        """
        [Client.update_xss_match_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/waf-regional.html#WAFRegional.Client.update_xss_match_set)
        """
