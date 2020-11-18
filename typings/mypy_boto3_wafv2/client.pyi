# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for wafv2 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_wafv2 import WAFV2Client

    client: WAFV2Client = boto3.client("wafv2")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_wafv2.type_defs import (
    CheckCapacityResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateRegexPatternSetResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    CreateWebACLResponseTypeDef,
    DefaultActionTypeDef,
    DeleteFirewallManagerRuleGroupsResponseTypeDef,
    DescribeManagedRuleGroupResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetPermissionPolicyResponseTypeDef,
    GetRateBasedStatementManagedKeysResponseTypeDef,
    GetRegexPatternSetResponseTypeDef,
    GetRuleGroupResponseTypeDef,
    GetSampledRequestsResponseTypeDef,
    GetWebACLForResourceResponseTypeDef,
    GetWebACLResponseTypeDef,
    ListAvailableManagedRuleGroupsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListResourcesForWebACLResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebACLsResponseTypeDef,
    LoggingConfigurationTypeDef,
    PutLoggingConfigurationResponseTypeDef,
    RegexTypeDef,
    RuleTypeDef,
    TagTypeDef,
    TimeWindowTypeDef,
    UpdateIPSetResponseTypeDef,
    UpdateRegexPatternSetResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateWebACLResponseTypeDef,
    VisibilityConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("WAFV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    WAFAssociatedItemException: Type[BotocoreClientError]
    WAFDuplicateItemException: Type[BotocoreClientError]
    WAFInternalErrorException: Type[BotocoreClientError]
    WAFInvalidOperationException: Type[BotocoreClientError]
    WAFInvalidParameterException: Type[BotocoreClientError]
    WAFInvalidPermissionPolicyException: Type[BotocoreClientError]
    WAFInvalidResourceException: Type[BotocoreClientError]
    WAFLimitsExceededException: Type[BotocoreClientError]
    WAFNonexistentItemException: Type[BotocoreClientError]
    WAFOptimisticLockException: Type[BotocoreClientError]
    WAFServiceLinkedRoleErrorException: Type[BotocoreClientError]
    WAFSubscriptionNotFoundException: Type[BotocoreClientError]
    WAFTagOperationException: Type[BotocoreClientError]
    WAFTagOperationInternalErrorException: Type[BotocoreClientError]
    WAFUnavailableEntityException: Type[BotocoreClientError]


class WAFV2Client:
    """
    [WAFV2.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_web_acl(self, WebACLArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.associate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.associate_web_acl)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.can_paginate)
        """

    def check_capacity(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], Rules: List["RuleTypeDef"]
    ) -> CheckCapacityResponseTypeDef:
        """
        [Client.check_capacity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.check_capacity)
        """

    def create_ip_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        IPAddressVersion: Literal["IPV4", "IPV6"],
        Addresses: List[str],
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateIPSetResponseTypeDef:
        """
        [Client.create_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.create_ip_set)
        """

    def create_regex_pattern_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        RegularExpressionList: List["RegexTypeDef"],
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateRegexPatternSetResponseTypeDef:
        """
        [Client.create_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.create_regex_pattern_set)
        """

    def create_rule_group(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Capacity: int,
        VisibilityConfig: "VisibilityConfigTypeDef",
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateRuleGroupResponseTypeDef:
        """
        [Client.create_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.create_rule_group)
        """

    def create_web_acl(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        DefaultAction: "DefaultActionTypeDef",
        VisibilityConfig: "VisibilityConfigTypeDef",
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateWebACLResponseTypeDef:
        """
        [Client.create_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.create_web_acl)
        """

    def delete_firewall_manager_rule_groups(
        self, WebACLArn: str, WebACLLockToken: str
    ) -> DeleteFirewallManagerRuleGroupsResponseTypeDef:
        """
        [Client.delete_firewall_manager_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.delete_firewall_manager_rule_groups)
        """

    def delete_ip_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.delete_ip_set)
        """

    def delete_logging_configuration(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.delete_logging_configuration)
        """

    def delete_permission_policy(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.delete_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.delete_permission_policy)
        """

    def delete_regex_pattern_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.delete_regex_pattern_set)
        """

    def delete_rule_group(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.delete_rule_group)
        """

    def delete_web_acl(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Client.delete_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.delete_web_acl)
        """

    def describe_managed_rule_group(
        self, VendorName: str, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"]
    ) -> DescribeManagedRuleGroupResponseTypeDef:
        """
        [Client.describe_managed_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.describe_managed_rule_group)
        """

    def disassociate_web_acl(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Client.disassociate_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.disassociate_web_acl)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.generate_presigned_url)
        """

    def get_ip_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> GetIPSetResponseTypeDef:
        """
        [Client.get_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_ip_set)
        """

    def get_logging_configuration(self, ResourceArn: str) -> GetLoggingConfigurationResponseTypeDef:
        """
        [Client.get_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_logging_configuration)
        """

    def get_permission_policy(self, ResourceArn: str) -> GetPermissionPolicyResponseTypeDef:
        """
        [Client.get_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_permission_policy)
        """

    def get_rate_based_statement_managed_keys(
        self,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        WebACLName: str,
        WebACLId: str,
        RuleName: str,
    ) -> GetRateBasedStatementManagedKeysResponseTypeDef:
        """
        [Client.get_rate_based_statement_managed_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_rate_based_statement_managed_keys)
        """

    def get_regex_pattern_set(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> GetRegexPatternSetResponseTypeDef:
        """
        [Client.get_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_regex_pattern_set)
        """

    def get_rule_group(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> GetRuleGroupResponseTypeDef:
        """
        [Client.get_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_rule_group)
        """

    def get_sampled_requests(
        self,
        WebAclArn: str,
        RuleMetricName: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        TimeWindow: "TimeWindowTypeDef",
        MaxItems: int,
    ) -> GetSampledRequestsResponseTypeDef:
        """
        [Client.get_sampled_requests documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_sampled_requests)
        """

    def get_web_acl(
        self, Name: str, Scope: Literal["CLOUDFRONT", "REGIONAL"], Id: str
    ) -> GetWebACLResponseTypeDef:
        """
        [Client.get_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_web_acl)
        """

    def get_web_acl_for_resource(self, ResourceArn: str) -> GetWebACLForResourceResponseTypeDef:
        """
        [Client.get_web_acl_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.get_web_acl_for_resource)
        """

    def list_available_managed_rule_groups(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListAvailableManagedRuleGroupsResponseTypeDef:
        """
        [Client.list_available_managed_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_groups)
        """

    def list_ip_sets(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListIPSetsResponseTypeDef:
        """
        [Client.list_ip_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.list_ip_sets)
        """

    def list_logging_configurations(
        self,
        Scope: Literal["CLOUDFRONT", "REGIONAL"] = None,
        NextMarker: str = None,
        Limit: int = None,
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        [Client.list_logging_configurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.list_logging_configurations)
        """

    def list_regex_pattern_sets(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListRegexPatternSetsResponseTypeDef:
        """
        [Client.list_regex_pattern_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.list_regex_pattern_sets)
        """

    def list_resources_for_web_acl(
        self,
        WebACLArn: str,
        ResourceType: Literal["APPLICATION_LOAD_BALANCER", "API_GATEWAY", "APPSYNC"] = None,
    ) -> ListResourcesForWebACLResponseTypeDef:
        """
        [Client.list_resources_for_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.list_resources_for_web_acl)
        """

    def list_rule_groups(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        [Client.list_rule_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.list_rule_groups)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.list_tags_for_resource)
        """

    def list_web_acls(
        self, Scope: Literal["CLOUDFRONT", "REGIONAL"], NextMarker: str = None, Limit: int = None
    ) -> ListWebACLsResponseTypeDef:
        """
        [Client.list_web_acls documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.list_web_acls)
        """

    def put_logging_configuration(
        self, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutLoggingConfigurationResponseTypeDef:
        """
        [Client.put_logging_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.put_logging_configuration)
        """

    def put_permission_policy(self, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        [Client.put_permission_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.put_permission_policy)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.tag_resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.untag_resource)
        """

    def update_ip_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        Addresses: List[str],
        LockToken: str,
        Description: str = None,
    ) -> UpdateIPSetResponseTypeDef:
        """
        [Client.update_ip_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.update_ip_set)
        """

    def update_regex_pattern_set(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        RegularExpressionList: List["RegexTypeDef"],
        LockToken: str,
        Description: str = None,
    ) -> UpdateRegexPatternSetResponseTypeDef:
        """
        [Client.update_regex_pattern_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.update_regex_pattern_set)
        """

    def update_rule_group(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        VisibilityConfig: "VisibilityConfigTypeDef",
        LockToken: str,
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        [Client.update_rule_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.update_rule_group)
        """

    def update_web_acl(
        self,
        Name: str,
        Scope: Literal["CLOUDFRONT", "REGIONAL"],
        Id: str,
        DefaultAction: "DefaultActionTypeDef",
        VisibilityConfig: "VisibilityConfigTypeDef",
        LockToken: str,
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
    ) -> UpdateWebACLResponseTypeDef:
        """
        [Client.update_web_acl documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/wafv2.html#WAFV2.Client.update_web_acl)
        """
