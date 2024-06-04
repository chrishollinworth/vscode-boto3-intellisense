"""
Type annotations for network-firewall service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/literals.html)

Usage::

    ```python
    from mypy_boto3_network_firewall.literals import AttachmentStatusType

    data: AttachmentStatusType = "CREATING"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AttachmentStatusType",
    "ConfigurationSyncStateType",
    "EncryptionTypeType",
    "FirewallStatusValueType",
    "GeneratedRulesTypeType",
    "IPAddressTypeType",
    "IdentifiedTypeType",
    "ListFirewallPoliciesPaginatorName",
    "ListFirewallsPaginatorName",
    "ListRuleGroupsPaginatorName",
    "ListTLSInspectionConfigurationsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "LogDestinationTypeType",
    "LogTypeType",
    "OverrideActionType",
    "PerObjectSyncStatusType",
    "ResourceManagedStatusType",
    "ResourceManagedTypeType",
    "ResourceStatusType",
    "RevocationCheckActionType",
    "RuleGroupTypeType",
    "RuleOrderType",
    "StatefulActionType",
    "StatefulRuleDirectionType",
    "StatefulRuleProtocolType",
    "StreamExceptionPolicyType",
    "TCPFlagType",
    "TargetTypeType",
)

AttachmentStatusType = Literal["CREATING", "DELETING", "ERROR", "FAILED", "READY", "SCALING"]
ConfigurationSyncStateType = Literal["CAPACITY_CONSTRAINED", "IN_SYNC", "PENDING"]
EncryptionTypeType = Literal["AWS_OWNED_KMS_KEY", "CUSTOMER_KMS"]
FirewallStatusValueType = Literal["DELETING", "PROVISIONING", "READY"]
GeneratedRulesTypeType = Literal["ALLOWLIST", "DENYLIST"]
IPAddressTypeType = Literal["DUALSTACK", "IPV4", "IPV6"]
IdentifiedTypeType = Literal[
    "STATELESS_RULE_CONTAINS_TCP_FLAGS", "STATELESS_RULE_FORWARDING_ASYMMETRICALLY"
]
ListFirewallPoliciesPaginatorName = Literal["list_firewall_policies"]
ListFirewallsPaginatorName = Literal["list_firewalls"]
ListRuleGroupsPaginatorName = Literal["list_rule_groups"]
ListTLSInspectionConfigurationsPaginatorName = Literal["list_tls_inspection_configurations"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
LogDestinationTypeType = Literal["CloudWatchLogs", "KinesisDataFirehose", "S3"]
LogTypeType = Literal["ALERT", "FLOW"]
OverrideActionType = Literal["DROP_TO_ALERT"]
PerObjectSyncStatusType = Literal["CAPACITY_CONSTRAINED", "IN_SYNC", "PENDING"]
ResourceManagedStatusType = Literal["ACCOUNT", "MANAGED"]
ResourceManagedTypeType = Literal["AWS_MANAGED_DOMAIN_LISTS", "AWS_MANAGED_THREAT_SIGNATURES"]
ResourceStatusType = Literal["ACTIVE", "DELETING", "ERROR"]
RevocationCheckActionType = Literal["DROP", "PASS", "REJECT"]
RuleGroupTypeType = Literal["STATEFUL", "STATELESS"]
RuleOrderType = Literal["DEFAULT_ACTION_ORDER", "STRICT_ORDER"]
StatefulActionType = Literal["ALERT", "DROP", "PASS", "REJECT"]
StatefulRuleDirectionType = Literal["ANY", "FORWARD"]
StatefulRuleProtocolType = Literal[
    "DCERPC",
    "DHCP",
    "DNS",
    "FTP",
    "HTTP",
    "ICMP",
    "IKEV2",
    "IMAP",
    "IP",
    "KRB5",
    "MSN",
    "NTP",
    "SMB",
    "SMTP",
    "SSH",
    "TCP",
    "TFTP",
    "TLS",
    "UDP",
]
StreamExceptionPolicyType = Literal["CONTINUE", "DROP", "REJECT"]
TCPFlagType = Literal["ACK", "CWR", "ECE", "FIN", "PSH", "RST", "SYN", "URG"]
TargetTypeType = Literal["HTTP_HOST", "TLS_SNI"]
