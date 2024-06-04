"""
Type annotations for fms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/literals.html)

Usage::

    ```python
    from mypy_boto3_fms.literals import AccountRoleStatusType

    data: AccountRoleStatusType = "CREATING"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountRoleStatusType",
    "CustomerPolicyScopeIdTypeType",
    "CustomerPolicyStatusType",
    "DependentServiceNameType",
    "DestinationTypeType",
    "EntryTypeType",
    "EntryViolationReasonType",
    "FailedItemReasonType",
    "FirewallDeploymentModelType",
    "ListAdminAccountsForOrganizationPaginatorName",
    "ListAdminsManagingAccountPaginatorName",
    "ListAppsListsPaginatorName",
    "ListComplianceStatusPaginatorName",
    "ListMemberAccountsPaginatorName",
    "ListPoliciesPaginatorName",
    "ListProtocolsListsPaginatorName",
    "ListThirdPartyFirewallFirewallPoliciesPaginatorName",
    "MarketplaceSubscriptionOnboardingStatusType",
    "NetworkAclRuleActionType",
    "NetworkFirewallOverrideActionType",
    "OrganizationStatusType",
    "PolicyComplianceStatusTypeType",
    "RemediationActionTypeType",
    "ResourceSetStatusType",
    "RuleOrderType",
    "SecurityServiceTypeType",
    "StreamExceptionPolicyType",
    "TargetTypeType",
    "ThirdPartyFirewallAssociationStatusType",
    "ThirdPartyFirewallType",
    "ViolationReasonType",
)

AccountRoleStatusType = Literal["CREATING", "DELETED", "DELETING", "PENDING_DELETION", "READY"]
CustomerPolicyScopeIdTypeType = Literal["ACCOUNT", "ORG_UNIT"]
CustomerPolicyStatusType = Literal["ACTIVE", "OUT_OF_ADMIN_SCOPE"]
DependentServiceNameType = Literal["AWSCONFIG", "AWSSHIELD_ADVANCED", "AWSVPC", "AWSWAF"]
DestinationTypeType = Literal["IPV4", "IPV6", "PREFIX_LIST"]
EntryTypeType = Literal["CUSTOM_ENTRY", "FMS_MANAGED_FIRST_ENTRY", "FMS_MANAGED_LAST_ENTRY"]
EntryViolationReasonType = Literal[
    "ENTRY_CONFLICT", "INCORRECT_ENTRY_ORDER", "MISSING_EXPECTED_ENTRY"
]
FailedItemReasonType = Literal[
    "NOT_VALID_ACCOUNT_ID",
    "NOT_VALID_ARN",
    "NOT_VALID_PARTITION",
    "NOT_VALID_REGION",
    "NOT_VALID_RESOURCE_TYPE",
    "NOT_VALID_SERVICE",
]
FirewallDeploymentModelType = Literal["CENTRALIZED", "DISTRIBUTED"]
ListAdminAccountsForOrganizationPaginatorName = Literal["list_admin_accounts_for_organization"]
ListAdminsManagingAccountPaginatorName = Literal["list_admins_managing_account"]
ListAppsListsPaginatorName = Literal["list_apps_lists"]
ListComplianceStatusPaginatorName = Literal["list_compliance_status"]
ListMemberAccountsPaginatorName = Literal["list_member_accounts"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListProtocolsListsPaginatorName = Literal["list_protocols_lists"]
ListThirdPartyFirewallFirewallPoliciesPaginatorName = Literal[
    "list_third_party_firewall_firewall_policies"
]
MarketplaceSubscriptionOnboardingStatusType = Literal["COMPLETE", "NOT_COMPLETE", "NO_SUBSCRIPTION"]
NetworkAclRuleActionType = Literal["allow", "deny"]
NetworkFirewallOverrideActionType = Literal["DROP_TO_ALERT"]
OrganizationStatusType = Literal[
    "OFFBOARDING", "OFFBOARDING_COMPLETE", "ONBOARDING", "ONBOARDING_COMPLETE"
]
PolicyComplianceStatusTypeType = Literal["COMPLIANT", "NON_COMPLIANT"]
RemediationActionTypeType = Literal["MODIFY", "REMOVE"]
ResourceSetStatusType = Literal["ACTIVE", "OUT_OF_ADMIN_SCOPE"]
RuleOrderType = Literal["DEFAULT_ACTION_ORDER", "STRICT_ORDER"]
SecurityServiceTypeType = Literal[
    "DNS_FIREWALL",
    "IMPORT_NETWORK_FIREWALL",
    "NETWORK_ACL_COMMON",
    "NETWORK_FIREWALL",
    "SECURITY_GROUPS_COMMON",
    "SECURITY_GROUPS_CONTENT_AUDIT",
    "SECURITY_GROUPS_USAGE_AUDIT",
    "SHIELD_ADVANCED",
    "THIRD_PARTY_FIREWALL",
    "WAF",
    "WAFV2",
]
StreamExceptionPolicyType = Literal["CONTINUE", "DROP", "FMS_IGNORE", "REJECT"]
TargetTypeType = Literal[
    "CARRIER_GATEWAY",
    "EGRESS_ONLY_INTERNET_GATEWAY",
    "GATEWAY",
    "INSTANCE",
    "LOCAL_GATEWAY",
    "NAT_GATEWAY",
    "NETWORK_INTERFACE",
    "TRANSIT_GATEWAY",
    "VPC_ENDPOINT",
    "VPC_PEERING_CONNECTION",
]
ThirdPartyFirewallAssociationStatusType = Literal[
    "NOT_EXIST", "OFFBOARDING", "OFFBOARD_COMPLETE", "ONBOARDING", "ONBOARD_COMPLETE"
]
ThirdPartyFirewallType = Literal["FORTIGATE_CLOUD_NATIVE_FIREWALL", "PALO_ALTO_NETWORKS_CLOUD_NGFW"]
ViolationReasonType = Literal[
    "BLACK_HOLE_ROUTE_DETECTED",
    "BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET",
    "FIREWALL_SUBNET_IS_OUT_OF_SCOPE",
    "FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE",
    "FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT",
    "FMS_CREATED_SECURITY_GROUP_EDITED",
    "INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE",
    "INTERNET_TRAFFIC_NOT_INSPECTED",
    "INVALID_NETWORK_ACL_ENTRY",
    "INVALID_ROUTE_CONFIGURATION",
    "MISSING_EXPECTED_ROUTE_TABLE",
    "MISSING_FIREWALL",
    "MISSING_FIREWALL_SUBNET_IN_AZ",
    "MISSING_TARGET_GATEWAY",
    "NETWORK_FIREWALL_POLICY_MODIFIED",
    "RESOURCE_INCORRECT_WEB_ACL",
    "RESOURCE_MISSING_DNS_FIREWALL",
    "RESOURCE_MISSING_SECURITY_GROUP",
    "RESOURCE_MISSING_SHIELD_PROTECTION",
    "RESOURCE_MISSING_WEB_ACL",
    "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION",
    "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP",
    "ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT",
    "SECURITY_GROUP_REDUNDANT",
    "SECURITY_GROUP_UNUSED",
    "TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY",
    "UNEXPECTED_FIREWALL_ROUTES",
    "UNEXPECTED_TARGET_GATEWAY_ROUTES",
    "WEB_ACL_MISSING_RULE_GROUP",
]
