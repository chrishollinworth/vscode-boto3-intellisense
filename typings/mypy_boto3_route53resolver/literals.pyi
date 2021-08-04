"""
Type annotations for route53resolver service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/literals.html)

Usage::

    ```python
    from mypy_boto3_route53resolver.literals import ActionType

    data: ActionType = "ALERT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionType",
    "BlockOverrideDnsTypeType",
    "BlockResponseType",
    "FirewallDomainImportOperationType",
    "FirewallDomainListStatusType",
    "FirewallDomainUpdateOperationType",
    "FirewallFailOpenStatusType",
    "FirewallRuleGroupAssociationStatusType",
    "FirewallRuleGroupStatusType",
    "IpAddressStatusType",
    "ListFirewallConfigsPaginatorName",
    "ListFirewallDomainListsPaginatorName",
    "ListFirewallDomainsPaginatorName",
    "ListFirewallRuleGroupAssociationsPaginatorName",
    "ListFirewallRuleGroupsPaginatorName",
    "ListFirewallRulesPaginatorName",
    "ListResolverDnssecConfigsPaginatorName",
    "ListResolverEndpointIpAddressesPaginatorName",
    "ListResolverEndpointsPaginatorName",
    "ListResolverQueryLogConfigAssociationsPaginatorName",
    "ListResolverQueryLogConfigsPaginatorName",
    "ListResolverRuleAssociationsPaginatorName",
    "ListResolverRulesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "MutationProtectionStatusType",
    "ResolverDNSSECValidationStatusType",
    "ResolverEndpointDirectionType",
    "ResolverEndpointStatusType",
    "ResolverQueryLogConfigAssociationErrorType",
    "ResolverQueryLogConfigAssociationStatusType",
    "ResolverQueryLogConfigStatusType",
    "ResolverRuleAssociationStatusType",
    "ResolverRuleStatusType",
    "RuleTypeOptionType",
    "ShareStatusType",
    "SortOrderType",
    "ValidationType",
)

ActionType = Literal["ALERT", "ALLOW", "BLOCK"]
BlockOverrideDnsTypeType = Literal["CNAME"]
BlockResponseType = Literal["NODATA", "NXDOMAIN", "OVERRIDE"]
FirewallDomainImportOperationType = Literal["REPLACE"]
FirewallDomainListStatusType = Literal[
    "COMPLETE", "COMPLETE_IMPORT_FAILED", "DELETING", "IMPORTING", "UPDATING"
]
FirewallDomainUpdateOperationType = Literal["ADD", "REMOVE", "REPLACE"]
FirewallFailOpenStatusType = Literal["DISABLED", "ENABLED"]
FirewallRuleGroupAssociationStatusType = Literal["COMPLETE", "DELETING", "UPDATING"]
FirewallRuleGroupStatusType = Literal["COMPLETE", "DELETING", "UPDATING"]
IpAddressStatusType = Literal[
    "ATTACHED",
    "ATTACHING",
    "CREATING",
    "DELETE_FAILED_FAS_EXPIRED",
    "DELETING",
    "DETACHING",
    "FAILED_CREATION",
    "FAILED_RESOURCE_GONE",
    "REMAP_ATTACHING",
    "REMAP_DETACHING",
]
ListFirewallConfigsPaginatorName = Literal["list_firewall_configs"]
ListFirewallDomainListsPaginatorName = Literal["list_firewall_domain_lists"]
ListFirewallDomainsPaginatorName = Literal["list_firewall_domains"]
ListFirewallRuleGroupAssociationsPaginatorName = Literal["list_firewall_rule_group_associations"]
ListFirewallRuleGroupsPaginatorName = Literal["list_firewall_rule_groups"]
ListFirewallRulesPaginatorName = Literal["list_firewall_rules"]
ListResolverDnssecConfigsPaginatorName = Literal["list_resolver_dnssec_configs"]
ListResolverEndpointIpAddressesPaginatorName = Literal["list_resolver_endpoint_ip_addresses"]
ListResolverEndpointsPaginatorName = Literal["list_resolver_endpoints"]
ListResolverQueryLogConfigAssociationsPaginatorName = Literal[
    "list_resolver_query_log_config_associations"
]
ListResolverQueryLogConfigsPaginatorName = Literal["list_resolver_query_log_configs"]
ListResolverRuleAssociationsPaginatorName = Literal["list_resolver_rule_associations"]
ListResolverRulesPaginatorName = Literal["list_resolver_rules"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
MutationProtectionStatusType = Literal["DISABLED", "ENABLED"]
ResolverDNSSECValidationStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
ResolverEndpointDirectionType = Literal["INBOUND", "OUTBOUND"]
ResolverEndpointStatusType = Literal[
    "ACTION_NEEDED", "AUTO_RECOVERING", "CREATING", "DELETING", "OPERATIONAL", "UPDATING"
]
ResolverQueryLogConfigAssociationErrorType = Literal[
    "ACCESS_DENIED", "DESTINATION_NOT_FOUND", "INTERNAL_SERVICE_ERROR", "NONE"
]
ResolverQueryLogConfigAssociationStatusType = Literal[
    "ACTION_NEEDED", "ACTIVE", "CREATING", "DELETING", "FAILED"
]
ResolverQueryLogConfigStatusType = Literal["CREATED", "CREATING", "DELETING", "FAILED"]
ResolverRuleAssociationStatusType = Literal[
    "COMPLETE", "CREATING", "DELETING", "FAILED", "OVERRIDDEN"
]
ResolverRuleStatusType = Literal["COMPLETE", "DELETING", "FAILED", "UPDATING"]
RuleTypeOptionType = Literal["FORWARD", "RECURSIVE", "SYSTEM"]
ShareStatusType = Literal["NOT_SHARED", "SHARED_BY_ME", "SHARED_WITH_ME"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
ValidationType = Literal["DISABLE", "ENABLE"]
