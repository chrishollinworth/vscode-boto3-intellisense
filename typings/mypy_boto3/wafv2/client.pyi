"""
Type annotations for wafv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_wafv2 import WAFV2Client

    client: WAFV2Client = boto3.client("wafv2")
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union

from botocore.client import BaseClient, ClientMeta

from .literals import IPAddressVersionType, LogScopeType, PlatformType, ResourceTypeType, ScopeType
from .type_defs import (
    AssociationConfigTypeDef,
    CaptchaConfigTypeDef,
    ChallengeConfigTypeDef,
    CheckCapacityResponseTypeDef,
    CreateAPIKeyResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateRegexPatternSetResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    CreateWebACLResponseTypeDef,
    CustomResponseBodyTypeDef,
    DefaultActionTypeDef,
    DeleteFirewallManagerRuleGroupsResponseTypeDef,
    DescribeAllManagedProductsResponseTypeDef,
    DescribeManagedProductsByVendorResponseTypeDef,
    DescribeManagedRuleGroupResponseTypeDef,
    GenerateMobileSdkReleaseUrlResponseTypeDef,
    GetDecryptedAPIKeyResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetManagedRuleSetResponseTypeDef,
    GetMobileSdkReleaseResponseTypeDef,
    GetPermissionPolicyResponseTypeDef,
    GetRateBasedStatementManagedKeysResponseTypeDef,
    GetRegexPatternSetResponseTypeDef,
    GetRuleGroupResponseTypeDef,
    GetSampledRequestsResponseTypeDef,
    GetWebACLForResourceResponseTypeDef,
    GetWebACLResponseTypeDef,
    ListAPIKeysResponseTypeDef,
    ListAvailableManagedRuleGroupsResponseTypeDef,
    ListAvailableManagedRuleGroupVersionsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListManagedRuleSetsResponseTypeDef,
    ListMobileSdkReleasesResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListResourcesForWebACLResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebACLsResponseTypeDef,
    LoggingConfigurationTypeDef,
    PutLoggingConfigurationResponseTypeDef,
    PutManagedRuleSetVersionsResponseTypeDef,
    RegexTypeDef,
    RuleTypeDef,
    TagTypeDef,
    TimeWindowTypeDef,
    UpdateIPSetResponseTypeDef,
    UpdateManagedRuleSetVersionExpiryDateResponseTypeDef,
    UpdateRegexPatternSetResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateWebACLResponseTypeDef,
    VersionToPublishTypeDef,
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
    WAFConfigurationWarningException: Type[BotocoreClientError]
    WAFDuplicateItemException: Type[BotocoreClientError]
    WAFExpiredManagedRuleGroupVersionException: Type[BotocoreClientError]
    WAFInternalErrorException: Type[BotocoreClientError]
    WAFInvalidOperationException: Type[BotocoreClientError]
    WAFInvalidParameterException: Type[BotocoreClientError]
    WAFInvalidPermissionPolicyException: Type[BotocoreClientError]
    WAFInvalidResourceException: Type[BotocoreClientError]
    WAFLimitsExceededException: Type[BotocoreClientError]
    WAFLogDestinationPermissionIssueException: Type[BotocoreClientError]
    WAFNonexistentItemException: Type[BotocoreClientError]
    WAFOptimisticLockException: Type[BotocoreClientError]
    WAFServiceLinkedRoleErrorException: Type[BotocoreClientError]
    WAFSubscriptionNotFoundException: Type[BotocoreClientError]
    WAFTagOperationException: Type[BotocoreClientError]
    WAFTagOperationInternalErrorException: Type[BotocoreClientError]
    WAFUnavailableEntityException: Type[BotocoreClientError]
    WAFUnsupportedAggregateKeyTypeException: Type[BotocoreClientError]

class WAFV2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WAFV2Client exceptions.
        """

    def associate_web_acl(self, *, WebACLArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        Associates a web ACL with a regional application resource, to protect the
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.associate_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#associate_web_acl)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#can_paginate)
        """

    def check_capacity(
        self, *, Scope: ScopeType, Rules: List["RuleTypeDef"]
    ) -> CheckCapacityResponseTypeDef:
        """
        Returns the web ACL capacity unit (WCU) requirements for a specified scope and
        set of rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.check_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#check_capacity)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#close)
        """

    def create_api_key(
        self, *, Scope: ScopeType, TokenDomains: List[str]
    ) -> CreateAPIKeyResponseTypeDef:
        """
        Creates an API key that contains a set of token domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.create_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create_api_key)
        """

    def create_ip_set(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        IPAddressVersion: IPAddressVersionType,
        Addresses: List[str],
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateIPSetResponseTypeDef:
        """
        Creates an  IPSet, which you use to identify web requests that originate from
        specific IP addresses or ranges of IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.create_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create_ip_set)
        """

    def create_regex_pattern_set(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        RegularExpressionList: List["RegexTypeDef"],
        Description: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateRegexPatternSetResponseTypeDef:
        """
        Creates a  RegexPatternSet, which you reference in a
        RegexPatternSetReferenceStatement, to have WAF inspect a web request component
        for the specified patterns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.create_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create_regex_pattern_set)
        """

    def create_rule_group(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Capacity: int,
        VisibilityConfig: "VisibilityConfigTypeDef",
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None
    ) -> CreateRuleGroupResponseTypeDef:
        """
        Creates a  RuleGroup per the specifications provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.create_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create_rule_group)
        """

    def create_web_acl(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        DefaultAction: "DefaultActionTypeDef",
        VisibilityConfig: "VisibilityConfigTypeDef",
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None,
        CaptchaConfig: "CaptchaConfigTypeDef" = None,
        ChallengeConfig: "ChallengeConfigTypeDef" = None,
        TokenDomains: List[str] = None,
        AssociationConfig: "AssociationConfigTypeDef" = None
    ) -> CreateWebACLResponseTypeDef:
        """
        Creates a  WebACL per the specifications provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.create_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create_web_acl)
        """

    def delete_api_key(self, *, Scope: ScopeType, APIKey: str) -> Dict[str, Any]:
        """
        Deletes the specified API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.delete_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete_api_key)
        """

    def delete_firewall_manager_rule_groups(
        self, *, WebACLArn: str, WebACLLockToken: str
    ) -> DeleteFirewallManagerRuleGroupsResponseTypeDef:
        """
        Deletes all rule groups that are managed by Firewall Manager for the specified
        web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.delete_firewall_manager_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete_firewall_manager_rule_groups)
        """

    def delete_ip_set(
        self, *, Name: str, Scope: ScopeType, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified  IPSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.delete_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete_ip_set)
        """

    def delete_logging_configuration(
        self,
        *,
        ResourceArn: str,
        LogType: Literal["WAF_LOGS"] = None,
        LogScope: LogScopeType = None
    ) -> Dict[str, Any]:
        """
        Deletes the  LoggingConfiguration from the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.delete_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete_logging_configuration)
        """

    def delete_permission_policy(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Permanently deletes an IAM policy from the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.delete_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete_permission_policy)
        """

    def delete_regex_pattern_set(
        self, *, Name: str, Scope: ScopeType, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified  RegexPatternSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.delete_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete_regex_pattern_set)
        """

    def delete_rule_group(
        self, *, Name: str, Scope: ScopeType, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified  RuleGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.delete_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete_rule_group)
        """

    def delete_web_acl(
        self, *, Name: str, Scope: ScopeType, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        Deletes the specified  WebACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.delete_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete_web_acl)
        """

    def describe_all_managed_products(
        self, *, Scope: ScopeType
    ) -> DescribeAllManagedProductsResponseTypeDef:
        """
        Provides high-level information for the Amazon Web Services Managed Rules rule
        groups and Amazon Web Services Marketplace managed rule groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.describe_all_managed_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#describe_all_managed_products)
        """

    def describe_managed_products_by_vendor(
        self, *, VendorName: str, Scope: ScopeType
    ) -> DescribeManagedProductsByVendorResponseTypeDef:
        """
        Provides high-level information for the managed rule groups owned by a specific
        vendor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.describe_managed_products_by_vendor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#describe_managed_products_by_vendor)
        """

    def describe_managed_rule_group(
        self, *, VendorName: str, Name: str, Scope: ScopeType, VersionName: str = None
    ) -> DescribeManagedRuleGroupResponseTypeDef:
        """
        Provides high-level information for a managed rule group, including descriptions
        of the rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.describe_managed_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#describe_managed_rule_group)
        """

    def disassociate_web_acl(self, *, ResourceArn: str) -> Dict[str, Any]:
        """
        Disassociates the specified regional application resource from any existing web
        ACL association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.disassociate_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#disassociate_web_acl)
        """

    def generate_mobile_sdk_release_url(
        self, *, Platform: PlatformType, ReleaseVersion: str
    ) -> GenerateMobileSdkReleaseUrlResponseTypeDef:
        """
        Generates a presigned download URL for the specified release of the mobile SDK.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.generate_mobile_sdk_release_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#generate_mobile_sdk_release_url)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#generate_presigned_url)
        """

    def get_decrypted_api_key(
        self, *, Scope: ScopeType, APIKey: str
    ) -> GetDecryptedAPIKeyResponseTypeDef:
        """
        Returns your API key in decrypted form.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_decrypted_api_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_decrypted_api_key)
        """

    def get_ip_set(self, *, Name: str, Scope: ScopeType, Id: str) -> GetIPSetResponseTypeDef:
        """
        Retrieves the specified  IPSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_ip_set)
        """

    def get_logging_configuration(
        self,
        *,
        ResourceArn: str,
        LogType: Literal["WAF_LOGS"] = None,
        LogScope: LogScopeType = None
    ) -> GetLoggingConfigurationResponseTypeDef:
        """
        Returns the  LoggingConfiguration for the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_logging_configuration)
        """

    def get_managed_rule_set(
        self, *, Name: str, Scope: ScopeType, Id: str
    ) -> GetManagedRuleSetResponseTypeDef:
        """
        Retrieves the specified managed rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_managed_rule_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_managed_rule_set)
        """

    def get_mobile_sdk_release(
        self, *, Platform: PlatformType, ReleaseVersion: str
    ) -> GetMobileSdkReleaseResponseTypeDef:
        """
        Retrieves information for the specified mobile SDK release, including release
        notes and tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_mobile_sdk_release)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_mobile_sdk_release)
        """

    def get_permission_policy(self, *, ResourceArn: str) -> GetPermissionPolicyResponseTypeDef:
        """
        Returns the IAM policy that is attached to the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_permission_policy)
        """

    def get_rate_based_statement_managed_keys(
        self,
        *,
        Scope: ScopeType,
        WebACLName: str,
        WebACLId: str,
        RuleName: str,
        RuleGroupRuleName: str = None
    ) -> GetRateBasedStatementManagedKeysResponseTypeDef:
        """
        Retrieves the IP addresses that are currently blocked by a rate-based rule
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_rate_based_statement_managed_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_rate_based_statement_managed_keys)
        """

    def get_regex_pattern_set(
        self, *, Name: str, Scope: ScopeType, Id: str
    ) -> GetRegexPatternSetResponseTypeDef:
        """
        Retrieves the specified  RegexPatternSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_regex_pattern_set)
        """

    def get_rule_group(
        self, *, Name: str = None, Scope: ScopeType = None, Id: str = None, ARN: str = None
    ) -> GetRuleGroupResponseTypeDef:
        """
        Retrieves the specified  RuleGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_rule_group)
        """

    def get_sampled_requests(
        self,
        *,
        WebAclArn: str,
        RuleMetricName: str,
        Scope: ScopeType,
        TimeWindow: "TimeWindowTypeDef",
        MaxItems: int
    ) -> GetSampledRequestsResponseTypeDef:
        """
        Gets detailed information about a specified number of requests--a sample--that
        WAF randomly selects from among the first 5,000 requests that your Amazon Web
        Services resource received during a time range that you choose.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_sampled_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_sampled_requests)
        """

    def get_web_acl(self, *, Name: str, Scope: ScopeType, Id: str) -> GetWebACLResponseTypeDef:
        """
        Retrieves the specified  WebACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_web_acl)
        """

    def get_web_acl_for_resource(self, *, ResourceArn: str) -> GetWebACLForResourceResponseTypeDef:
        """
        Retrieves the  WebACL for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.get_web_acl_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get_web_acl_for_resource)
        """

    def list_api_keys(
        self, *, Scope: ScopeType, NextMarker: str = None, Limit: int = None
    ) -> ListAPIKeysResponseTypeDef:
        """
        Retrieves a list of the API keys that you've defined for the specified scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_api_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_api_keys)
        """

    def list_available_managed_rule_group_versions(
        self,
        *,
        VendorName: str,
        Name: str,
        Scope: ScopeType,
        NextMarker: str = None,
        Limit: int = None
    ) -> ListAvailableManagedRuleGroupVersionsResponseTypeDef:
        """
        Returns a list of the available versions for the specified managed rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_group_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_available_managed_rule_group_versions)
        """

    def list_available_managed_rule_groups(
        self, *, Scope: ScopeType, NextMarker: str = None, Limit: int = None
    ) -> ListAvailableManagedRuleGroupsResponseTypeDef:
        """
        Retrieves an array of managed rule groups that are available for you to use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_available_managed_rule_groups)
        """

    def list_ip_sets(
        self, *, Scope: ScopeType, NextMarker: str = None, Limit: int = None
    ) -> ListIPSetsResponseTypeDef:
        """
        Retrieves an array of  IPSetSummary objects for the IP sets that you manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_ip_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_ip_sets)
        """

    def list_logging_configurations(
        self,
        *,
        Scope: ScopeType,
        NextMarker: str = None,
        Limit: int = None,
        LogScope: LogScopeType = None
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        Retrieves an array of your  LoggingConfiguration objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_logging_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_logging_configurations)
        """

    def list_managed_rule_sets(
        self, *, Scope: ScopeType, NextMarker: str = None, Limit: int = None
    ) -> ListManagedRuleSetsResponseTypeDef:
        """
        Retrieves the managed rule sets that you own.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_managed_rule_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_managed_rule_sets)
        """

    def list_mobile_sdk_releases(
        self, *, Platform: PlatformType, NextMarker: str = None, Limit: int = None
    ) -> ListMobileSdkReleasesResponseTypeDef:
        """
        Retrieves a list of the available releases for the mobile SDK and the specified
        device platform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_mobile_sdk_releases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_mobile_sdk_releases)
        """

    def list_regex_pattern_sets(
        self, *, Scope: ScopeType, NextMarker: str = None, Limit: int = None
    ) -> ListRegexPatternSetsResponseTypeDef:
        """
        Retrieves an array of  RegexPatternSetSummary objects for the regex pattern sets
        that you manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_regex_pattern_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_regex_pattern_sets)
        """

    def list_resources_for_web_acl(
        self, *, WebACLArn: str, ResourceType: ResourceTypeType = None
    ) -> ListResourcesForWebACLResponseTypeDef:
        """
        Retrieves an array of the Amazon Resource Names (ARNs) for the regional
        resources that are associated with the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_resources_for_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_resources_for_web_acl)
        """

    def list_rule_groups(
        self, *, Scope: ScopeType, NextMarker: str = None, Limit: int = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        Retrieves an array of  RuleGroupSummary objects for the rule groups that you
        manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_rule_groups)
        """

    def list_tags_for_resource(
        self, *, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the  TagInfoForResource for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_tags_for_resource)
        """

    def list_web_acls(
        self, *, Scope: ScopeType, NextMarker: str = None, Limit: int = None
    ) -> ListWebACLsResponseTypeDef:
        """
        Retrieves an array of  WebACLSummary objects for the web ACLs that you manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.list_web_acls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list_web_acls)
        """

    def put_logging_configuration(
        self, *, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutLoggingConfigurationResponseTypeDef:
        """
        Enables the specified  LoggingConfiguration, to start logging from a web ACL,
        according to the configuration provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.put_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#put_logging_configuration)
        """

    def put_managed_rule_set_versions(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        LockToken: str,
        RecommendedVersion: str = None,
        VersionsToPublish: Dict[str, "VersionToPublishTypeDef"] = None
    ) -> PutManagedRuleSetVersionsResponseTypeDef:
        """
        Defines the versions of your managed rule set that you are offering to the
        customers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.put_managed_rule_set_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#put_managed_rule_set_versions)
        """

    def put_permission_policy(self, *, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        Attaches an IAM policy to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.put_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#put_permission_policy)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Associates tags with the specified Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Disassociates tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#untag_resource)
        """

    def update_ip_set(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        Addresses: List[str],
        LockToken: str,
        Description: str = None
    ) -> UpdateIPSetResponseTypeDef:
        """
        Updates the specified  IPSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.update_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update_ip_set)
        """

    def update_managed_rule_set_version_expiry_date(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        LockToken: str,
        VersionToExpire: str,
        ExpiryTimestamp: Union[datetime, str]
    ) -> UpdateManagedRuleSetVersionExpiryDateResponseTypeDef:
        """
        Updates the expiration information for your managed rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.update_managed_rule_set_version_expiry_date)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update_managed_rule_set_version_expiry_date)
        """

    def update_regex_pattern_set(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        RegularExpressionList: List["RegexTypeDef"],
        LockToken: str,
        Description: str = None
    ) -> UpdateRegexPatternSetResponseTypeDef:
        """
        Updates the specified  RegexPatternSet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.update_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update_regex_pattern_set)
        """

    def update_rule_group(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        VisibilityConfig: "VisibilityConfigTypeDef",
        LockToken: str,
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        Updates the specified  RuleGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.update_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update_rule_group)
        """

    def update_web_acl(
        self,
        *,
        Name: str,
        Scope: ScopeType,
        Id: str,
        DefaultAction: "DefaultActionTypeDef",
        VisibilityConfig: "VisibilityConfigTypeDef",
        LockToken: str,
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None,
        CaptchaConfig: "CaptchaConfigTypeDef" = None,
        ChallengeConfig: "ChallengeConfigTypeDef" = None,
        TokenDomains: List[str] = None,
        AssociationConfig: "AssociationConfigTypeDef" = None
    ) -> UpdateWebACLResponseTypeDef:
        """
        Updates the specified  WebACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/wafv2.html#WAFV2.Client.update_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update_web_acl)
        """
