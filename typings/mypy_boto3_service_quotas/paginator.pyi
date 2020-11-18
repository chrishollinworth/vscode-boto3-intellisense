# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for service-quotas service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_service_quotas import ServiceQuotasClient
    from mypy_boto3_service_quotas.paginator import (
        ListAWSDefaultServiceQuotasPaginator,
        ListRequestedServiceQuotaChangeHistoryPaginator,
        ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
        ListServiceQuotaIncreaseRequestsInTemplatePaginator,
        ListServiceQuotasPaginator,
        ListServicesPaginator,
    )

    client: ServiceQuotasClient = boto3.client("service-quotas")

    list_aws_default_service_quotas_paginator: ListAWSDefaultServiceQuotasPaginator = client.get_paginator("list_aws_default_service_quotas")
    list_requested_service_quota_change_history_paginator: ListRequestedServiceQuotaChangeHistoryPaginator = client.get_paginator("list_requested_service_quota_change_history")
    list_requested_service_quota_change_history_by_quota_paginator: ListRequestedServiceQuotaChangeHistoryByQuotaPaginator = client.get_paginator("list_requested_service_quota_change_history_by_quota")
    list_service_quota_increase_requests_in_template_paginator: ListServiceQuotaIncreaseRequestsInTemplatePaginator = client.get_paginator("list_service_quota_increase_requests_in_template")
    list_service_quotas_paginator: ListServiceQuotasPaginator = client.get_paginator("list_service_quotas")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_service_quotas.type_defs import (
    ListAWSDefaultServiceQuotasResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ListServiceQuotasResponseTypeDef,
    ListServicesResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAWSDefaultServiceQuotasPaginator",
    "ListRequestedServiceQuotaChangeHistoryPaginator",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginator",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginator",
    "ListServiceQuotasPaginator",
    "ListServicesPaginator",
)


class ListAWSDefaultServiceQuotasPaginator(Boto3Paginator):
    """
    [Paginator.ListAWSDefaultServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas)
    """

    def paginate(
        self, ServiceCode: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAWSDefaultServiceQuotasResponseTypeDef]:
        """
        [ListAWSDefaultServiceQuotas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas.paginate)
        """


class ListRequestedServiceQuotaChangeHistoryPaginator(Boto3Paginator):
    """
    [Paginator.ListRequestedServiceQuotaChangeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory)
    """

    def paginate(
        self,
        ServiceCode: str = None,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRequestedServiceQuotaChangeHistoryResponseTypeDef]:
        """
        [ListRequestedServiceQuotaChangeHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory.paginate)
        """


class ListRequestedServiceQuotaChangeHistoryByQuotaPaginator(Boto3Paginator):
    """
    [Paginator.ListRequestedServiceQuotaChangeHistoryByQuota documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota)
    """

    def paginate(
        self,
        ServiceCode: str,
        QuotaCode: str,
        Status: Literal["PENDING", "CASE_OPENED", "APPROVED", "DENIED", "CASE_CLOSED"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef]:
        """
        [ListRequestedServiceQuotaChangeHistoryByQuota.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota.paginate)
        """


class ListServiceQuotaIncreaseRequestsInTemplatePaginator(Boto3Paginator):
    """
    [Paginator.ListServiceQuotaIncreaseRequestsInTemplate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate)
    """

    def paginate(
        self,
        ServiceCode: str = None,
        AwsRegion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef]:
        """
        [ListServiceQuotaIncreaseRequestsInTemplate.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate.paginate)
        """


class ListServiceQuotasPaginator(Boto3Paginator):
    """
    [Paginator.ListServiceQuotas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas)
    """

    def paginate(
        self, ServiceCode: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceQuotasResponseTypeDef]:
        """
        [ListServiceQuotas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesResponseTypeDef]:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices.paginate)
        """
