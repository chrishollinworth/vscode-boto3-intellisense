"""
Type annotations for ses service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ses/literals.html)

Usage::

    ```python
    from mypy_boto3_ses.literals import BehaviorOnMXFailureType

    data: BehaviorOnMXFailureType = "RejectMessage"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BehaviorOnMXFailureType",
    "BounceTypeType",
    "BulkEmailStatusType",
    "ConfigurationSetAttributeType",
    "CustomMailFromStatusType",
    "DimensionValueSourceType",
    "DsnActionType",
    "EventTypeType",
    "IdentityExistsWaiterName",
    "IdentityTypeType",
    "InvocationTypeType",
    "ListConfigurationSetsPaginatorName",
    "ListCustomVerificationEmailTemplatesPaginatorName",
    "ListIdentitiesPaginatorName",
    "ListReceiptRuleSetsPaginatorName",
    "ListTemplatesPaginatorName",
    "NotificationTypeType",
    "ReceiptFilterPolicyType",
    "SNSActionEncodingType",
    "StopScopeType",
    "TlsPolicyType",
    "VerificationStatusType",
)

BehaviorOnMXFailureType = Literal["RejectMessage", "UseDefaultValue"]
BounceTypeType = Literal[
    "ContentRejected",
    "DoesNotExist",
    "ExceededQuota",
    "MessageTooLarge",
    "TemporaryFailure",
    "Undefined",
]
BulkEmailStatusType = Literal[
    "AccountDailyQuotaExceeded",
    "AccountSendingPaused",
    "AccountSuspended",
    "AccountThrottled",
    "ConfigurationSetDoesNotExist",
    "ConfigurationSetSendingPaused",
    "Failed",
    "InvalidParameterValue",
    "InvalidSendingPoolName",
    "MailFromDomainNotVerified",
    "MessageRejected",
    "Success",
    "TemplateDoesNotExist",
    "TransientFailure",
]
ConfigurationSetAttributeType = Literal[
    "deliveryOptions", "eventDestinations", "reputationOptions", "trackingOptions"
]
CustomMailFromStatusType = Literal["Failed", "Pending", "Success", "TemporaryFailure"]
DimensionValueSourceType = Literal["emailHeader", "linkTag", "messageTag"]
DsnActionType = Literal["delayed", "delivered", "expanded", "failed", "relayed"]
EventTypeType = Literal[
    "bounce", "click", "complaint", "delivery", "open", "reject", "renderingFailure", "send"
]
IdentityExistsWaiterName = Literal["identity_exists"]
IdentityTypeType = Literal["Domain", "EmailAddress"]
InvocationTypeType = Literal["Event", "RequestResponse"]
ListConfigurationSetsPaginatorName = Literal["list_configuration_sets"]
ListCustomVerificationEmailTemplatesPaginatorName = Literal[
    "list_custom_verification_email_templates"
]
ListIdentitiesPaginatorName = Literal["list_identities"]
ListReceiptRuleSetsPaginatorName = Literal["list_receipt_rule_sets"]
ListTemplatesPaginatorName = Literal["list_templates"]
NotificationTypeType = Literal["Bounce", "Complaint", "Delivery"]
ReceiptFilterPolicyType = Literal["Allow", "Block"]
SNSActionEncodingType = Literal["Base64", "UTF-8"]
StopScopeType = Literal["RuleSet"]
TlsPolicyType = Literal["Optional", "Require"]
VerificationStatusType = Literal["Failed", "NotStarted", "Pending", "Success", "TemporaryFailure"]
