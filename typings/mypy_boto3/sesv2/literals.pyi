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
    "BounceTypeType",
    "BulkEmailStatusType",
    "ContactLanguageType",
    "ContactListImportActionType",
    "DataFormatType",
    "DeliverabilityDashboardAccountStatusType",
    "DeliverabilityTestStatusType",
    "DeliveryEventTypeType",
    "DimensionValueSourceType",
    "DkimSigningAttributesOriginType",
    "DkimSigningKeyLengthType",
    "DkimStatusType",
    "EngagementEventTypeType",
    "EventTypeType",
    "ExportSourceTypeType",
    "FeatureStatusType",
    "IdentityTypeType",
    "ImportDestinationTypeType",
    "JobStatusType",
    "ListRecommendationsFilterKeyType",
    "MailFromDomainStatusType",
    "MailTypeType",
    "MetricAggregationType",
    "MetricDimensionNameType",
    "MetricNamespaceType",
    "MetricType",
    "QueryErrorCodeType",
    "RecommendationImpactType",
    "RecommendationStatusType",
    "RecommendationTypeType",
    "ReviewStatusType",
    "ScalingModeType",
    "SubscriptionStatusType",
    "SuppressionListImportActionType",
    "SuppressionListReasonType",
    "TlsPolicyType",
    "VerificationErrorType",
    "VerificationStatusType",
    "WarmupStatusType",
)

BehaviorOnMxFailureType = Literal["REJECT_MESSAGE", "USE_DEFAULT_VALUE"]
BounceTypeType = Literal["PERMANENT", "TRANSIENT", "UNDETERMINED"]
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
DeliveryEventTypeType = Literal[
    "COMPLAINT", "DELIVERY", "PERMANENT_BOUNCE", "SEND", "TRANSIENT_BOUNCE", "UNDETERMINED_BOUNCE"
]
DimensionValueSourceType = Literal["EMAIL_HEADER", "LINK_TAG", "MESSAGE_TAG"]
DkimSigningAttributesOriginType = Literal["AWS_SES", "EXTERNAL"]
DkimSigningKeyLengthType = Literal["RSA_1024_BIT", "RSA_2048_BIT"]
DkimStatusType = Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
EngagementEventTypeType = Literal["CLICK", "OPEN"]
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
ExportSourceTypeType = Literal["MESSAGE_INSIGHTS", "METRICS_DATA"]
FeatureStatusType = Literal["DISABLED", "ENABLED"]
IdentityTypeType = Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"]
ImportDestinationTypeType = Literal["CONTACT_LIST", "SUPPRESSION_LIST"]
JobStatusType = Literal["CANCELLED", "COMPLETED", "CREATED", "FAILED", "PROCESSING"]
ListRecommendationsFilterKeyType = Literal["IMPACT", "RESOURCE_ARN", "STATUS", "TYPE"]
MailFromDomainStatusType = Literal["FAILED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
MailTypeType = Literal["MARKETING", "TRANSACTIONAL"]
MetricAggregationType = Literal["RATE", "VOLUME"]
MetricDimensionNameType = Literal["CONFIGURATION_SET", "EMAIL_IDENTITY", "ISP"]
MetricNamespaceType = Literal["VDM"]
MetricType = Literal[
    "CLICK",
    "COMPLAINT",
    "DELIVERY",
    "DELIVERY_CLICK",
    "DELIVERY_COMPLAINT",
    "DELIVERY_OPEN",
    "OPEN",
    "PERMANENT_BOUNCE",
    "SEND",
    "TRANSIENT_BOUNCE",
]
QueryErrorCodeType = Literal["ACCESS_DENIED", "INTERNAL_FAILURE"]
RecommendationImpactType = Literal["HIGH", "LOW"]
RecommendationStatusType = Literal["FIXED", "OPEN"]
RecommendationTypeType = Literal["BIMI", "DKIM", "DMARC", "SPF"]
ReviewStatusType = Literal["DENIED", "FAILED", "GRANTED", "PENDING"]
ScalingModeType = Literal["MANAGED", "STANDARD"]
SubscriptionStatusType = Literal["OPT_IN", "OPT_OUT"]
SuppressionListImportActionType = Literal["DELETE", "PUT"]
SuppressionListReasonType = Literal["BOUNCE", "COMPLAINT"]
TlsPolicyType = Literal["OPTIONAL", "REQUIRE"]
VerificationErrorType = Literal[
    "DNS_SERVER_ERROR", "HOST_NOT_FOUND", "INVALID_VALUE", "SERVICE_ERROR", "TYPE_NOT_FOUND"
]
VerificationStatusType = Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
WarmupStatusType = Literal["DONE", "IN_PROGRESS"]
