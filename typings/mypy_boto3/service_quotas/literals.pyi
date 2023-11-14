"""
Type annotations for service-quotas service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/literals.html)

Usage::

    ```python
    from mypy_boto3_service_quotas.literals import AppliedLevelEnumType

    data: AppliedLevelEnumType = "ACCOUNT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AppliedLevelEnumType",
    "ErrorCodeType",
    "ListAWSDefaultServiceQuotasPaginatorName",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorName",
    "ListRequestedServiceQuotaChangeHistoryPaginatorName",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginatorName",
    "ListServiceQuotasPaginatorName",
    "ListServicesPaginatorName",
    "PeriodUnitType",
    "QuotaContextScopeType",
    "RequestStatusType",
    "ServiceQuotaTemplateAssociationStatusType",
)

AppliedLevelEnumType = Literal["ACCOUNT", "ALL", "RESOURCE"]
ErrorCodeType = Literal[
    "DEPENDENCY_ACCESS_DENIED_ERROR",
    "DEPENDENCY_SERVICE_ERROR",
    "DEPENDENCY_THROTTLING_ERROR",
    "SERVICE_QUOTA_NOT_AVAILABLE_ERROR",
]
ListAWSDefaultServiceQuotasPaginatorName = Literal["list_aws_default_service_quotas"]
ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorName = Literal[
    "list_requested_service_quota_change_history_by_quota"
]
ListRequestedServiceQuotaChangeHistoryPaginatorName = Literal[
    "list_requested_service_quota_change_history"
]
ListServiceQuotaIncreaseRequestsInTemplatePaginatorName = Literal[
    "list_service_quota_increase_requests_in_template"
]
ListServiceQuotasPaginatorName = Literal["list_service_quotas"]
ListServicesPaginatorName = Literal["list_services"]
PeriodUnitType = Literal["DAY", "HOUR", "MICROSECOND", "MILLISECOND", "MINUTE", "SECOND", "WEEK"]
QuotaContextScopeType = Literal["ACCOUNT", "RESOURCE"]
RequestStatusType = Literal[
    "APPROVED", "CASE_CLOSED", "CASE_OPENED", "DENIED", "INVALID_REQUEST", "NOT_APPROVED", "PENDING"
]
ServiceQuotaTemplateAssociationStatusType = Literal["ASSOCIATED", "DISASSOCIATED"]
