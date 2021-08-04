"""
Type annotations for pinpoint-email service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint_email/literals.html)

Usage::

    ```python
    from mypy_boto3_pinpoint_email.literals import BehaviorOnMxFailureType

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
    "DeliverabilityDashboardAccountStatusType",
    "DeliverabilityTestStatusType",
    "DimensionValueSourceType",
    "DkimStatusType",
    "EventTypeType",
    "GetDedicatedIpsPaginatorName",
    "IdentityTypeType",
    "ListConfigurationSetsPaginatorName",
    "ListDedicatedIpPoolsPaginatorName",
    "ListDeliverabilityTestReportsPaginatorName",
    "ListEmailIdentitiesPaginatorName",
    "MailFromDomainStatusType",
    "TlsPolicyType",
    "WarmupStatusType",
)

BehaviorOnMxFailureType = Literal["REJECT_MESSAGE", "USE_DEFAULT_VALUE"]
DeliverabilityDashboardAccountStatusType = Literal["ACTIVE", "DISABLED", "PENDING_EXPIRATION"]
DeliverabilityTestStatusType = Literal["COMPLETED", "IN_PROGRESS"]
DimensionValueSourceType = Literal["EMAIL_HEADER", "LINK_TAG", "MESSAGE_TAG"]
DkimStatusType = Literal["FAILED", "NOT_STARTED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
EventTypeType = Literal[
    "BOUNCE", "CLICK", "COMPLAINT", "DELIVERY", "OPEN", "REJECT", "RENDERING_FAILURE", "SEND"
]
GetDedicatedIpsPaginatorName = Literal["get_dedicated_ips"]
IdentityTypeType = Literal["DOMAIN", "EMAIL_ADDRESS", "MANAGED_DOMAIN"]
ListConfigurationSetsPaginatorName = Literal["list_configuration_sets"]
ListDedicatedIpPoolsPaginatorName = Literal["list_dedicated_ip_pools"]
ListDeliverabilityTestReportsPaginatorName = Literal["list_deliverability_test_reports"]
ListEmailIdentitiesPaginatorName = Literal["list_email_identities"]
MailFromDomainStatusType = Literal["FAILED", "PENDING", "SUCCESS", "TEMPORARY_FAILURE"]
TlsPolicyType = Literal["OPTIONAL", "REQUIRE"]
WarmupStatusType = Literal["DONE", "IN_PROGRESS"]
