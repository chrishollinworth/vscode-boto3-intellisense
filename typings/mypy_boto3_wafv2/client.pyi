"""
Type annotations for wafv2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_wafv2.client import WAFV2Client

    session = Session()
    client: WAFV2Client = session.client("wafv2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    AssociateWebACLRequestTypeDef,
    CheckCapacityRequestTypeDef,
    CheckCapacityResponseTypeDef,
    CreateAPIKeyRequestTypeDef,
    CreateAPIKeyResponseTypeDef,
    CreateIPSetRequestTypeDef,
    CreateIPSetResponseTypeDef,
    CreateRegexPatternSetRequestTypeDef,
    CreateRegexPatternSetResponseTypeDef,
    CreateRuleGroupRequestTypeDef,
    CreateRuleGroupResponseTypeDef,
    CreateWebACLRequestTypeDef,
    CreateWebACLResponseTypeDef,
    DeleteAPIKeyRequestTypeDef,
    DeleteFirewallManagerRuleGroupsRequestTypeDef,
    DeleteFirewallManagerRuleGroupsResponseTypeDef,
    DeleteIPSetRequestTypeDef,
    DeleteLoggingConfigurationRequestTypeDef,
    DeletePermissionPolicyRequestTypeDef,
    DeleteRegexPatternSetRequestTypeDef,
    DeleteRuleGroupRequestTypeDef,
    DeleteWebACLRequestTypeDef,
    DescribeAllManagedProductsRequestTypeDef,
    DescribeAllManagedProductsResponseTypeDef,
    DescribeManagedProductsByVendorRequestTypeDef,
    DescribeManagedProductsByVendorResponseTypeDef,
    DescribeManagedRuleGroupRequestTypeDef,
    DescribeManagedRuleGroupResponseTypeDef,
    DisassociateWebACLRequestTypeDef,
    GenerateMobileSdkReleaseUrlRequestTypeDef,
    GenerateMobileSdkReleaseUrlResponseTypeDef,
    GetDecryptedAPIKeyRequestTypeDef,
    GetDecryptedAPIKeyResponseTypeDef,
    GetIPSetRequestTypeDef,
    GetIPSetResponseTypeDef,
    GetLoggingConfigurationRequestTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetManagedRuleSetRequestTypeDef,
    GetManagedRuleSetResponseTypeDef,
    GetMobileSdkReleaseRequestTypeDef,
    GetMobileSdkReleaseResponseTypeDef,
    GetPermissionPolicyRequestTypeDef,
    GetPermissionPolicyResponseTypeDef,
    GetRateBasedStatementManagedKeysRequestTypeDef,
    GetRateBasedStatementManagedKeysResponseTypeDef,
    GetRegexPatternSetRequestTypeDef,
    GetRegexPatternSetResponseTypeDef,
    GetRuleGroupRequestTypeDef,
    GetRuleGroupResponseTypeDef,
    GetSampledRequestsRequestTypeDef,
    GetSampledRequestsResponseTypeDef,
    GetWebACLForResourceRequestTypeDef,
    GetWebACLForResourceResponseTypeDef,
    GetWebACLRequestTypeDef,
    GetWebACLResponseTypeDef,
    ListAPIKeysRequestTypeDef,
    ListAPIKeysResponseTypeDef,
    ListAvailableManagedRuleGroupsRequestTypeDef,
    ListAvailableManagedRuleGroupsResponseTypeDef,
    ListAvailableManagedRuleGroupVersionsRequestTypeDef,
    ListAvailableManagedRuleGroupVersionsResponseTypeDef,
    ListIPSetsRequestTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsRequestTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListManagedRuleSetsRequestTypeDef,
    ListManagedRuleSetsResponseTypeDef,
    ListMobileSdkReleasesRequestTypeDef,
    ListMobileSdkReleasesResponseTypeDef,
    ListRegexPatternSetsRequestTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListResourcesForWebACLRequestTypeDef,
    ListResourcesForWebACLResponseTypeDef,
    ListRuleGroupsRequestTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebACLsRequestTypeDef,
    ListWebACLsResponseTypeDef,
    PutLoggingConfigurationRequestTypeDef,
    PutLoggingConfigurationResponseTypeDef,
    PutManagedRuleSetVersionsRequestTypeDef,
    PutManagedRuleSetVersionsResponseTypeDef,
    PutPermissionPolicyRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateIPSetRequestTypeDef,
    UpdateIPSetResponseTypeDef,
    UpdateManagedRuleSetVersionExpiryDateRequestTypeDef,
    UpdateManagedRuleSetVersionExpiryDateResponseTypeDef,
    UpdateRegexPatternSetRequestTypeDef,
    UpdateRegexPatternSetResponseTypeDef,
    UpdateRuleGroupRequestTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateWebACLRequestTypeDef,
    UpdateWebACLResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("WAFV2Client",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        WAFV2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2.html#WAFV2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#generate_presigned_url)
        """

    def associate_web_acl(self, **kwargs: Unpack[AssociateWebACLRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates a web ACL with a resource, to protect the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/associate_web_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#associate_web_acl)
        """

    def check_capacity(
        self, **kwargs: Unpack[CheckCapacityRequestTypeDef]
    ) -> CheckCapacityResponseTypeDef:
        """
        Returns the web ACL capacity unit (WCU) requirements for a specified scope and
        set of rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/check_capacity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#check_capacity)
        """

    def create_api_key(
        self, **kwargs: Unpack[CreateAPIKeyRequestTypeDef]
    ) -> CreateAPIKeyResponseTypeDef:
        """
        Creates an API key that contains a set of token domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/create_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#create_api_key)
        """

    def create_ip_set(
        self, **kwargs: Unpack[CreateIPSetRequestTypeDef]
    ) -> CreateIPSetResponseTypeDef:
        """
        Creates an <a>IPSet</a>, which you use to identify web requests that originate
        from specific IP addresses or ranges of IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/create_ip_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#create_ip_set)
        """

    def create_regex_pattern_set(
        self, **kwargs: Unpack[CreateRegexPatternSetRequestTypeDef]
    ) -> CreateRegexPatternSetResponseTypeDef:
        """
        Creates a <a>RegexPatternSet</a>, which you reference in a
        <a>RegexPatternSetReferenceStatement</a>, to have WAF inspect a web request
        component for the specified patterns.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/create_regex_pattern_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#create_regex_pattern_set)
        """

    def create_rule_group(
        self, **kwargs: Unpack[CreateRuleGroupRequestTypeDef]
    ) -> CreateRuleGroupResponseTypeDef:
        """
        Creates a <a>RuleGroup</a> per the specifications provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/create_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#create_rule_group)
        """

    def create_web_acl(
        self, **kwargs: Unpack[CreateWebACLRequestTypeDef]
    ) -> CreateWebACLResponseTypeDef:
        """
        Creates a <a>WebACL</a> per the specifications provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/create_web_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#create_web_acl)
        """

    def delete_api_key(self, **kwargs: Unpack[DeleteAPIKeyRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified API key.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/delete_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#delete_api_key)
        """

    def delete_firewall_manager_rule_groups(
        self, **kwargs: Unpack[DeleteFirewallManagerRuleGroupsRequestTypeDef]
    ) -> DeleteFirewallManagerRuleGroupsResponseTypeDef:
        """
        Deletes all rule groups that are managed by Firewall Manager from the specified
        <a>WebACL</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/delete_firewall_manager_rule_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#delete_firewall_manager_rule_groups)
        """

    def delete_ip_set(self, **kwargs: Unpack[DeleteIPSetRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified <a>IPSet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/delete_ip_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#delete_ip_set)
        """

    def delete_logging_configuration(
        self, **kwargs: Unpack[DeleteLoggingConfigurationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the <a>LoggingConfiguration</a> from the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/delete_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#delete_logging_configuration)
        """

    def delete_permission_policy(
        self, **kwargs: Unpack[DeletePermissionPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Permanently deletes an IAM policy from the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/delete_permission_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#delete_permission_policy)
        """

    def delete_regex_pattern_set(
        self, **kwargs: Unpack[DeleteRegexPatternSetRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the specified <a>RegexPatternSet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/delete_regex_pattern_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#delete_regex_pattern_set)
        """

    def delete_rule_group(self, **kwargs: Unpack[DeleteRuleGroupRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified <a>RuleGroup</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/delete_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#delete_rule_group)
        """

    def delete_web_acl(self, **kwargs: Unpack[DeleteWebACLRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified <a>WebACL</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/delete_web_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#delete_web_acl)
        """

    def describe_all_managed_products(
        self, **kwargs: Unpack[DescribeAllManagedProductsRequestTypeDef]
    ) -> DescribeAllManagedProductsResponseTypeDef:
        """
        Provides high-level information for the Amazon Web Services Managed Rules rule
        groups and Amazon Web Services Marketplace managed rule groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/describe_all_managed_products.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#describe_all_managed_products)
        """

    def describe_managed_products_by_vendor(
        self, **kwargs: Unpack[DescribeManagedProductsByVendorRequestTypeDef]
    ) -> DescribeManagedProductsByVendorResponseTypeDef:
        """
        Provides high-level information for the managed rule groups owned by a specific
        vendor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/describe_managed_products_by_vendor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#describe_managed_products_by_vendor)
        """

    def describe_managed_rule_group(
        self, **kwargs: Unpack[DescribeManagedRuleGroupRequestTypeDef]
    ) -> DescribeManagedRuleGroupResponseTypeDef:
        """
        Provides high-level information for a managed rule group, including
        descriptions of the rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/describe_managed_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#describe_managed_rule_group)
        """

    def disassociate_web_acl(
        self, **kwargs: Unpack[DisassociateWebACLRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified resource from its web ACL association, if it has
        one.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/disassociate_web_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#disassociate_web_acl)
        """

    def generate_mobile_sdk_release_url(
        self, **kwargs: Unpack[GenerateMobileSdkReleaseUrlRequestTypeDef]
    ) -> GenerateMobileSdkReleaseUrlResponseTypeDef:
        """
        Generates a presigned download URL for the specified release of the mobile SDK.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/generate_mobile_sdk_release_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#generate_mobile_sdk_release_url)
        """

    def get_decrypted_api_key(
        self, **kwargs: Unpack[GetDecryptedAPIKeyRequestTypeDef]
    ) -> GetDecryptedAPIKeyResponseTypeDef:
        """
        Returns your API key in decrypted form.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_decrypted_api_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_decrypted_api_key)
        """

    def get_ip_set(self, **kwargs: Unpack[GetIPSetRequestTypeDef]) -> GetIPSetResponseTypeDef:
        """
        Retrieves the specified <a>IPSet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_ip_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_ip_set)
        """

    def get_logging_configuration(
        self, **kwargs: Unpack[GetLoggingConfigurationRequestTypeDef]
    ) -> GetLoggingConfigurationResponseTypeDef:
        """
        Returns the <a>LoggingConfiguration</a> for the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_logging_configuration)
        """

    def get_managed_rule_set(
        self, **kwargs: Unpack[GetManagedRuleSetRequestTypeDef]
    ) -> GetManagedRuleSetResponseTypeDef:
        """
        Retrieves the specified managed rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_managed_rule_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_managed_rule_set)
        """

    def get_mobile_sdk_release(
        self, **kwargs: Unpack[GetMobileSdkReleaseRequestTypeDef]
    ) -> GetMobileSdkReleaseResponseTypeDef:
        """
        Retrieves information for the specified mobile SDK release, including release
        notes and tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_mobile_sdk_release.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_mobile_sdk_release)
        """

    def get_permission_policy(
        self, **kwargs: Unpack[GetPermissionPolicyRequestTypeDef]
    ) -> GetPermissionPolicyResponseTypeDef:
        """
        Returns the IAM policy that is attached to the specified rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_permission_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_permission_policy)
        """

    def get_rate_based_statement_managed_keys(
        self, **kwargs: Unpack[GetRateBasedStatementManagedKeysRequestTypeDef]
    ) -> GetRateBasedStatementManagedKeysResponseTypeDef:
        """
        Retrieves the IP addresses that are currently blocked by a rate-based rule
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_rate_based_statement_managed_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_rate_based_statement_managed_keys)
        """

    def get_regex_pattern_set(
        self, **kwargs: Unpack[GetRegexPatternSetRequestTypeDef]
    ) -> GetRegexPatternSetResponseTypeDef:
        """
        Retrieves the specified <a>RegexPatternSet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_regex_pattern_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_regex_pattern_set)
        """

    def get_rule_group(
        self, **kwargs: Unpack[GetRuleGroupRequestTypeDef]
    ) -> GetRuleGroupResponseTypeDef:
        """
        Retrieves the specified <a>RuleGroup</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_rule_group)
        """

    def get_sampled_requests(
        self, **kwargs: Unpack[GetSampledRequestsRequestTypeDef]
    ) -> GetSampledRequestsResponseTypeDef:
        """
        Gets detailed information about a specified number of requests--a sample--that
        WAF randomly selects from among the first 5,000 requests that your Amazon Web
        Services resource received during a time range that you choose.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_sampled_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_sampled_requests)
        """

    def get_web_acl(self, **kwargs: Unpack[GetWebACLRequestTypeDef]) -> GetWebACLResponseTypeDef:
        """
        Retrieves the specified <a>WebACL</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_web_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_web_acl)
        """

    def get_web_acl_for_resource(
        self, **kwargs: Unpack[GetWebACLForResourceRequestTypeDef]
    ) -> GetWebACLForResourceResponseTypeDef:
        """
        Retrieves the <a>WebACL</a> for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/get_web_acl_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#get_web_acl_for_resource)
        """

    def list_api_keys(
        self, **kwargs: Unpack[ListAPIKeysRequestTypeDef]
    ) -> ListAPIKeysResponseTypeDef:
        """
        Retrieves a list of the API keys that you've defined for the specified scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_api_keys.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_api_keys)
        """

    def list_available_managed_rule_group_versions(
        self, **kwargs: Unpack[ListAvailableManagedRuleGroupVersionsRequestTypeDef]
    ) -> ListAvailableManagedRuleGroupVersionsResponseTypeDef:
        """
        Returns a list of the available versions for the specified managed rule group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_available_managed_rule_group_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_available_managed_rule_group_versions)
        """

    def list_available_managed_rule_groups(
        self, **kwargs: Unpack[ListAvailableManagedRuleGroupsRequestTypeDef]
    ) -> ListAvailableManagedRuleGroupsResponseTypeDef:
        """
        Retrieves an array of managed rule groups that are available for you to use.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_available_managed_rule_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_available_managed_rule_groups)
        """

    def list_ip_sets(self, **kwargs: Unpack[ListIPSetsRequestTypeDef]) -> ListIPSetsResponseTypeDef:
        """
        Retrieves an array of <a>IPSetSummary</a> objects for the IP sets that you
        manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_ip_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_ip_sets)
        """

    def list_logging_configurations(
        self, **kwargs: Unpack[ListLoggingConfigurationsRequestTypeDef]
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        Retrieves an array of your <a>LoggingConfiguration</a> objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_logging_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_logging_configurations)
        """

    def list_managed_rule_sets(
        self, **kwargs: Unpack[ListManagedRuleSetsRequestTypeDef]
    ) -> ListManagedRuleSetsResponseTypeDef:
        """
        Retrieves the managed rule sets that you own.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_managed_rule_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_managed_rule_sets)
        """

    def list_mobile_sdk_releases(
        self, **kwargs: Unpack[ListMobileSdkReleasesRequestTypeDef]
    ) -> ListMobileSdkReleasesResponseTypeDef:
        """
        Retrieves a list of the available releases for the mobile SDK and the specified
        device platform.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_mobile_sdk_releases.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_mobile_sdk_releases)
        """

    def list_regex_pattern_sets(
        self, **kwargs: Unpack[ListRegexPatternSetsRequestTypeDef]
    ) -> ListRegexPatternSetsResponseTypeDef:
        """
        Retrieves an array of <a>RegexPatternSetSummary</a> objects for the regex
        pattern sets that you manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_regex_pattern_sets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_regex_pattern_sets)
        """

    def list_resources_for_web_acl(
        self, **kwargs: Unpack[ListResourcesForWebACLRequestTypeDef]
    ) -> ListResourcesForWebACLResponseTypeDef:
        """
        Retrieves an array of the Amazon Resource Names (ARNs) for the resources that
        are associated with the specified web ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_resources_for_web_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_resources_for_web_acl)
        """

    def list_rule_groups(
        self, **kwargs: Unpack[ListRuleGroupsRequestTypeDef]
    ) -> ListRuleGroupsResponseTypeDef:
        """
        Retrieves an array of <a>RuleGroupSummary</a> objects for the rule groups that
        you manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_rule_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_rule_groups)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Retrieves the <a>TagInfoForResource</a> for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_tags_for_resource)
        """

    def list_web_acls(
        self, **kwargs: Unpack[ListWebACLsRequestTypeDef]
    ) -> ListWebACLsResponseTypeDef:
        """
        Retrieves an array of <a>WebACLSummary</a> objects for the web ACLs that you
        manage.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/list_web_acls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#list_web_acls)
        """

    def put_logging_configuration(
        self, **kwargs: Unpack[PutLoggingConfigurationRequestTypeDef]
    ) -> PutLoggingConfigurationResponseTypeDef:
        """
        Enables the specified <a>LoggingConfiguration</a>, to start logging from a web
        ACL, according to the configuration provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/put_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#put_logging_configuration)
        """

    def put_managed_rule_set_versions(
        self, **kwargs: Unpack[PutManagedRuleSetVersionsRequestTypeDef]
    ) -> PutManagedRuleSetVersionsResponseTypeDef:
        """
        Defines the versions of your managed rule set that you are offering to the
        customers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/put_managed_rule_set_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#put_managed_rule_set_versions)
        """

    def put_permission_policy(
        self, **kwargs: Unpack[PutPermissionPolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Use this to share a rule group with other accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/put_permission_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#put_permission_policy)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates tags with the specified Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Disassociates tags from an Amazon Web Services resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#untag_resource)
        """

    def update_ip_set(
        self, **kwargs: Unpack[UpdateIPSetRequestTypeDef]
    ) -> UpdateIPSetResponseTypeDef:
        """
        Updates the specified <a>IPSet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/update_ip_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#update_ip_set)
        """

    def update_managed_rule_set_version_expiry_date(
        self, **kwargs: Unpack[UpdateManagedRuleSetVersionExpiryDateRequestTypeDef]
    ) -> UpdateManagedRuleSetVersionExpiryDateResponseTypeDef:
        """
        Updates the expiration information for your managed rule set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/update_managed_rule_set_version_expiry_date.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#update_managed_rule_set_version_expiry_date)
        """

    def update_regex_pattern_set(
        self, **kwargs: Unpack[UpdateRegexPatternSetRequestTypeDef]
    ) -> UpdateRegexPatternSetResponseTypeDef:
        """
        Updates the specified <a>RegexPatternSet</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/update_regex_pattern_set.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#update_regex_pattern_set)
        """

    def update_rule_group(
        self, **kwargs: Unpack[UpdateRuleGroupRequestTypeDef]
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        Updates the specified <a>RuleGroup</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/update_rule_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#update_rule_group)
        """

    def update_web_acl(
        self, **kwargs: Unpack[UpdateWebACLRequestTypeDef]
    ) -> UpdateWebACLResponseTypeDef:
        """
        Updates the specified <a>WebACL</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/wafv2/client/update_web_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client/#update_web_acl)
        """
