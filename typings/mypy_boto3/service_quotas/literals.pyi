"""
Type annotations for service-quotas service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/literals.html)

Usage::

    ```python
    from mypy_boto3_service_quotas.literals import ErrorCodeType

    data: ErrorCodeType = "DEPENDENCY_ACCESS_DENIED_ERROR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ErrorCodeType",
    "ListAWSDefaultServiceQuotasPaginatorName",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorName",
    "ListRequestedServiceQuotaChangeHistoryPaginatorName",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginatorName",
    "ListServiceQuotasPaginatorName",
    "ListServicesPaginatorName",
    "PeriodUnitType",
    "RequestStatusType",
    "ServiceQuotaTemplateAssociationStatusType",
)

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
RequestStatusType = Literal["APPROVED", "CASE_CLOSED", "CASE_OPENED", "DENIED", "PENDING"]
ServiceQuotaTemplateAssociationStatusType = Literal["ASSOCIATED", "DISASSOCIATED"]
