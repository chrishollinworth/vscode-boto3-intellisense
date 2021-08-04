"""
Type annotations for sesv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sesv2/literals.html)

Usage::

    ```python
    from mypy_boto3_sesv2.literals import BehaviorOnMxFailureType

    data: BehaviorOnMxFailureType = "REJECT_MESSAGE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BehaviorOnMxFailureType",
    "BulkEmailStatusType",
    "ContactLanguageType",
    "ContactListImportActionType",
    "DataFormatType",
    "DeliverabilityDashboardAccountStatusType",
    "DeliverabilityTestStatusType",
    "DimensionValueSourceType",
    "DkimSigningAttributesOriginType",
    "DkimStatusType",
    "EventTypeType",
    "IdentityTypeType",
    "ImportDestinationTypeType",
    "JobStatusType",
    "MailFromDomainStatusType",
    "MailTypeType",
    "ReviewStatusType",
    "SubscriptionStatusType",
    "SuppressionListImportActionType",
    "SuppressionListReasonType",
    "TlsPolicyType",
    "WarmupStatusType",
)

BehaviorOnMxFailureType = Literal["REJECT_MESSAGE", "USE_DEFAULT_VALUE"]
BulkEmailStatusType = Literal[
    "ACCOUNT_DAILY_QUOTA_EXCEEDED",
    "ACCOUNT_SENDING_PAUSED",
    "ACCOUNT_SUSPENDED",
    "ACCOUNT_THROTTLED",
    "CONFIGURATION_SET_NOT_FOUND",
    "CONFIGURATION_SET_SENDING_PAUSED",
    "FAILED",
    "INVALID_PARAMETER",
    "INVALID_SENDING_POOL_NAME",
    "MAIL_FROM_DOMAIN_NOT_VERIFIED",
    "MESSAGE_REJECTED",
    "SUCCESS",
    "TEMPLATE_NOT_FOUND",
    "TRANSIENT_FAILURE",
]
ContactLanguageType = Literal["EN", "JA"]
ContactListImportActionType = Literal["DELETE", "PUT"]
DataFormatType = Literal["CSV", "JSON"]
DeliverabilityDashboardAccountStatusType = Literal["ACTIVE", "DISABLED", "PENDING_EXPIRATION"]
DeliverabilityTestStatusType = Literal["COMPLETED", "IN_PROGRESS"]
DimensionValueSourceType = Literal["EMAIL_HEADER", "LINK_TAG", "MESSAGE_TAG"]
DkimSigningAttributesOriginType = Literal["AWS_SES", "EXTERNAL"]
DkimStatusType = Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
EventTypeType = Literal[
    "BOUNCE",
    "CLICK",
    "COMPLAINT",
    "DELIVERY",
    "DELIVERY_DELAY",
    "OPEN",
    "REJECT",
    "RENDERING_FAILURE",
    "SEND",
    "SUBSCRIPTION",
]
IdentityTypeType = Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"]
ImportDestinationTypeType = Literal["CONTACT_LIST", "SUPPRESSION_LIST"]
JobStatusType = Literal["COMPLETED", "CREATED", "FAILED", "PROCESSING"]
MailFromDomainStatusType = Literal["FAILED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
MailTypeType = Literal["MARKETING", "TRANSACTIONAL"]
ReviewStatusType = Literal["DENIED", "FAILED", "GRANTED", "PENDING"]
SubscriptionStatusType = Literal["OPT_IN", "OPT_OUT"]
SuppressionListImportActionType = Literal["DELETE", "PUT"]
SuppressionListReasonType = Literal["BOUNCE", "COMPLAINT"]
TlsPolicyType = Literal["OPTIONAL", "REQUIRE"]
WarmupStatusType = Literal["DONE", "IN_PROGRESS"]
