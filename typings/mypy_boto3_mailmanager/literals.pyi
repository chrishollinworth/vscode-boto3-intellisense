"""
Type annotations for mailmanager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mailmanager/literals.html)

Usage::

    ```python
    from mypy_boto3_mailmanager.literals import AcceptActionType

    data: AcceptActionType = "ALLOW"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AcceptActionType",
    "ActionFailurePolicyType",
    "ArchiveBooleanEmailAttributeType",
    "ArchiveBooleanOperatorType",
    "ArchiveStateType",
    "ArchiveStringEmailAttributeType",
    "ArchiveStringOperatorType",
    "ExportStateType",
    "IngressBooleanOperatorType",
    "IngressIpOperatorType",
    "IngressIpv4AttributeType",
    "IngressPointStatusToUpdateType",
    "IngressPointStatusType",
    "IngressPointTypeType",
    "IngressStringEmailAttributeType",
    "IngressStringOperatorType",
    "IngressTlsAttributeType",
    "IngressTlsProtocolAttributeType",
    "IngressTlsProtocolOperatorType",
    "ListAddonInstancesPaginatorName",
    "ListAddonSubscriptionsPaginatorName",
    "ListArchiveExportsPaginatorName",
    "ListArchiveSearchesPaginatorName",
    "ListArchivesPaginatorName",
    "ListIngressPointsPaginatorName",
    "ListRelaysPaginatorName",
    "ListRuleSetsPaginatorName",
    "ListTrafficPoliciesPaginatorName",
    "MailFromType",
    "RetentionPeriodType",
    "RuleBooleanEmailAttributeType",
    "RuleBooleanOperatorType",
    "RuleDmarcOperatorType",
    "RuleDmarcPolicyType",
    "RuleIpEmailAttributeType",
    "RuleIpOperatorType",
    "RuleNumberEmailAttributeType",
    "RuleNumberOperatorType",
    "RuleStringEmailAttributeType",
    "RuleStringOperatorType",
    "RuleVerdictAttributeType",
    "RuleVerdictOperatorType",
    "RuleVerdictType",
    "SearchStateType",
)

AcceptActionType = Literal["ALLOW", "DENY"]
ActionFailurePolicyType = Literal["CONTINUE", "DROP"]
ArchiveBooleanEmailAttributeType = Literal["HAS_ATTACHMENTS"]
ArchiveBooleanOperatorType = Literal["IS_FALSE", "IS_TRUE"]
ArchiveStateType = Literal["ACTIVE", "PENDING_DELETION"]
ArchiveStringEmailAttributeType = Literal["CC", "FROM", "SUBJECT", "TO"]
ArchiveStringOperatorType = Literal["CONTAINS"]
ExportStateType = Literal[
    "CANCELLED", "COMPLETED", "FAILED", "PREPROCESSING", "PROCESSING", "QUEUED"
]
IngressBooleanOperatorType = Literal["IS_FALSE", "IS_TRUE"]
IngressIpOperatorType = Literal["CIDR_MATCHES", "NOT_CIDR_MATCHES"]
IngressIpv4AttributeType = Literal["SENDER_IP"]
IngressPointStatusToUpdateType = Literal["ACTIVE", "CLOSED"]
IngressPointStatusType = Literal[
    "ACTIVE", "CLOSED", "DEPROVISIONING", "FAILED", "PROVISIONING", "UPDATING"
]
IngressPointTypeType = Literal["AUTH", "OPEN"]
IngressStringEmailAttributeType = Literal["RECIPIENT"]
IngressStringOperatorType = Literal["CONTAINS", "ENDS_WITH", "EQUALS", "NOT_EQUALS", "STARTS_WITH"]
IngressTlsAttributeType = Literal["TLS_PROTOCOL"]
IngressTlsProtocolAttributeType = Literal["TLS1_2", "TLS1_3"]
IngressTlsProtocolOperatorType = Literal["IS", "MINIMUM_TLS_VERSION"]
ListAddonInstancesPaginatorName = Literal["list_addon_instances"]
ListAddonSubscriptionsPaginatorName = Literal["list_addon_subscriptions"]
ListArchiveExportsPaginatorName = Literal["list_archive_exports"]
ListArchiveSearchesPaginatorName = Literal["list_archive_searches"]
ListArchivesPaginatorName = Literal["list_archives"]
ListIngressPointsPaginatorName = Literal["list_ingress_points"]
ListRelaysPaginatorName = Literal["list_relays"]
ListRuleSetsPaginatorName = Literal["list_rule_sets"]
ListTrafficPoliciesPaginatorName = Literal["list_traffic_policies"]
MailFromType = Literal["PRESERVE", "REPLACE"]
RetentionPeriodType = Literal[
    "EIGHTEEN_MONTHS",
    "EIGHT_YEARS",
    "FIVE_YEARS",
    "FOUR_YEARS",
    "NINE_MONTHS",
    "NINE_YEARS",
    "ONE_YEAR",
    "PERMANENT",
    "SEVEN_YEARS",
    "SIX_MONTHS",
    "SIX_YEARS",
    "TEN_YEARS",
    "THIRTY_MONTHS",
    "THREE_MONTHS",
    "THREE_YEARS",
    "TWO_YEARS",
]
RuleBooleanEmailAttributeType = Literal["READ_RECEIPT_REQUESTED", "TLS", "TLS_WRAPPED"]
RuleBooleanOperatorType = Literal["IS_FALSE", "IS_TRUE"]
RuleDmarcOperatorType = Literal["EQUALS", "NOT_EQUALS"]
RuleDmarcPolicyType = Literal["NONE", "QUARANTINE", "REJECT"]
RuleIpEmailAttributeType = Literal["SOURCE_IP"]
RuleIpOperatorType = Literal["CIDR_MATCHES", "NOT_CIDR_MATCHES"]
RuleNumberEmailAttributeType = Literal["MESSAGE_SIZE"]
RuleNumberOperatorType = Literal[
    "EQUALS",
    "GREATER_THAN",
    "GREATER_THAN_OR_EQUAL",
    "LESS_THAN",
    "LESS_THAN_OR_EQUAL",
    "NOT_EQUALS",
]
RuleStringEmailAttributeType = Literal[
    "CC", "FROM", "HELO", "MAIL_FROM", "RECIPIENT", "SENDER", "SUBJECT", "TO"
]
RuleStringOperatorType = Literal["CONTAINS", "ENDS_WITH", "EQUALS", "NOT_EQUALS", "STARTS_WITH"]
RuleVerdictAttributeType = Literal["DKIM", "SPF"]
RuleVerdictOperatorType = Literal["EQUALS", "NOT_EQUALS"]
RuleVerdictType = Literal["FAIL", "GRAY", "PASS", "PROCESSING_FAILED"]
SearchStateType = Literal["CANCELLED", "COMPLETED", "FAILED", "QUEUED", "RUNNING"]
