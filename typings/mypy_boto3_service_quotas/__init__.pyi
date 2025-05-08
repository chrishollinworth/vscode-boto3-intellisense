"""
Main interface for service-quotas service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
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

    session = Session()
    client: ServiceQuotasClient = session.client("service-quotas")

    list_aws_default_service_quotas_paginator: ListAWSDefaultServiceQuotasPaginator = client.get_paginator("list_aws_default_service_quotas")
    list_requested_service_quota_change_history_by_quota_paginator: ListRequestedServiceQuotaChangeHistoryByQuotaPaginator = client.get_paginator("list_requested_service_quota_change_history_by_quota")
    list_requested_service_quota_change_history_paginator: ListRequestedServiceQuotaChangeHistoryPaginator = client.get_paginator("list_requested_service_quota_change_history")
    list_service_quota_increase_requests_in_template_paginator: ListServiceQuotaIncreaseRequestsInTemplatePaginator = client.get_paginator("list_service_quota_increase_requests_in_template")
    list_service_quotas_paginator: ListServiceQuotasPaginator = client.get_paginator("list_service_quotas")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""

from .client import ServiceQuotasClient
from .paginator import (
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
