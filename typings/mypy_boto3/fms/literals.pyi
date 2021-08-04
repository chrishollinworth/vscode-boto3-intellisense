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
    "DependentServiceNameType",
    "DestinationTypeType",
    "ListAppsListsPaginatorName",
    "ListComplianceStatusPaginatorName",
    "ListMemberAccountsPaginatorName",
    "ListPoliciesPaginatorName",
    "ListProtocolsListsPaginatorName",
    "PolicyComplianceStatusTypeType",
    "RemediationActionTypeType",
    "SecurityServiceTypeType",
    "TargetTypeType",
    "ViolationReasonType",
)

AccountRoleStatusType = Literal["CREATING", "DELETED", "DELETING", "PENDING_DELETION", "READY"]
CustomerPolicyScopeIdTypeType = Literal["ACCOUNT", "ORG_UNIT"]
DependentServiceNameType = Literal["AWSCONFIG", "AWSSHIELD_ADVANCED", "AWSVPC", "AWSWAF"]
DestinationTypeType = Literal["IPV4", "IPV6", "PREFIX_LIST"]
ListAppsListsPaginatorName = Literal["list_apps_lists"]
ListComplianceStatusPaginatorName = Literal["list_compliance_status"]
ListMemberAccountsPaginatorName = Literal["list_member_accounts"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListProtocolsListsPaginatorName = Literal["list_protocols_lists"]
PolicyComplianceStatusTypeType = Literal["COMPLIANT", "NON_COMPLIANT"]
RemediationActionTypeType = Literal["MODIFY", "REMOVE"]
SecurityServiceTypeType = Literal[
    "DNS_FIREWALL",
    "NETWORK_FIREWALL",
    "SECURITY_GROUPS_COMMON",
    "SECURITY_GROUPS_CONTENT_AUDIT",
    "SECURITY_GROUPS_USAGE_AUDIT",
    "SHIELD_ADVANCED",
    "WAF",
    "WAFV2",
]
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
ViolationReasonType = Literal[
    "BLACK_HOLE_ROUTE_DETECTED",
    "BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET",
    "FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE",
    "FMS_CREATED_SECURITY_GROUP_EDITED",
    "INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE",
    "INTERNET_TRAFFIC_NOT_INSPECTED",
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
    "SECURITY_GROUP_REDUNDANT",
    "SECURITY_GROUP_UNUSED",
    "TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY",
    "UNEXPECTED_FIREWALL_ROUTES",
    "UNEXPECTED_TARGET_GATEWAY_ROUTES",
    "WEB_ACL_MISSING_RULE_GROUP",
]
