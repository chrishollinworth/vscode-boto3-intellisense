"""
Type annotations for service-quotas service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html)

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
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import RequestStatusType
from .type_defs import (
    ListAWSDefaultServiceQuotasResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ListServiceQuotasResponseTypeDef,
    ListServicesResponseTypeDef,
    PaginatorConfigTypeDef,
)

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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listawsdefaultservicequotaspaginator)
    """

    def paginate(
        self, *, ServiceCode: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAWSDefaultServiceQuotasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listawsdefaultservicequotaspaginator)
        """

class ListRequestedServiceQuotaChangeHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listrequestedservicequotachangehistorypaginator)
    """

    def paginate(
        self,
        *,
        ServiceCode: str = None,
        Status: RequestStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRequestedServiceQuotaChangeHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listrequestedservicequotachangehistorypaginator)
        """

class ListRequestedServiceQuotaChangeHistoryByQuotaPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listrequestedservicequotachangehistorybyquotapaginator)
    """

    def paginate(
        self,
        *,
        ServiceCode: str,
        QuotaCode: str,
        Status: RequestStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listrequestedservicequotachangehistorybyquotapaginator)
        """

class ListServiceQuotaIncreaseRequestsInTemplatePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listservicequotaincreaserequestsintemplatepaginator)
    """

    def paginate(
        self,
        *,
        ServiceCode: str = None,
        AwsRegion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listservicequotaincreaserequestsintemplatepaginator)
        """

class ListServiceQuotasPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listservicequotaspaginator)
    """

    def paginate(
        self, *, ServiceCode: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServiceQuotasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServiceQuotas.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listservicequotaspaginator)
        """

class ListServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listservicespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/service-quotas.html#ServiceQuotas.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators.html#listservicespaginator)
        """
