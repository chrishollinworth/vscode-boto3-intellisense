"""
Main interface for service-quotas service.

Usage::

    ```python
    import boto3
    from mypy_boto3_service_quotas import (
        Client,
        ListAWSDefaultServiceQuotasPaginator,
        ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
        ListRequestedServiceQuotaChangeHistoryPaginator,
        ListServiceQuotaIncreaseRequestsInTemplatePaginator,
        ListServiceQuotasPaginator,
        ListServicesPaginator,
        ServiceQuotasClient,
    )

    session = boto3.Session()

    client: ServiceQuotasClient = boto3.client("service-quotas")
    session_client: ServiceQuotasClient = session.client("service-quotas")

    list_aws_default_service_quotas_paginator: ListAWSDefaultServiceQuotasPaginator = client.get_paginator("list_aws_default_service_quotas")
    list_requested_service_quota_change_history_paginator: ListRequestedServiceQuotaChangeHistoryPaginator = client.get_paginator("list_requested_service_quota_change_history")
    list_requested_service_quota_change_history_by_quota_paginator: ListRequestedServiceQuotaChangeHistoryByQuotaPaginator = client.get_paginator("list_requested_service_quota_change_history_by_quota")
    list_service_quota_increase_requests_in_template_paginator: ListServiceQuotaIncreaseRequestsInTemplatePaginator = client.get_paginator("list_service_quota_increase_requests_in_template")
    list_service_quotas_paginator: ListServiceQuotasPaginator = client.get_paginator("list_service_quotas")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""
from mypy_boto3_service_quotas.client import ServiceQuotasClient
from mypy_boto3_service_quotas.paginator import (
    ListAWSDefaultServiceQuotasPaginator,
    ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
    ListRequestedServiceQuotaChangeHistoryPaginator,
    ListServiceQuotaIncreaseRequestsInTemplatePaginator,
    ListServiceQuotasPaginator,
    ListServicesPaginator,
)

Client = ServiceQuotasClient


__all__ = (
    "Client",
    "ListAWSDefaultServiceQuotasPaginator",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginator",
    "ListRequestedServiceQuotaChangeHistoryPaginator",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginator",
    "ListServiceQuotasPaginator",
    "ListServicesPaginator",
    "ServiceQuotasClient",
)
