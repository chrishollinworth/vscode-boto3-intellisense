"""
Type annotations for service-quotas service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_service_quotas.client import ServiceQuotasClient
    from mypy_boto3_service_quotas.paginator import (
        ListAWSDefaultServiceQuotasPaginator,
        ListRequestedServiceQuotaChangeHistoryByQuotaPaginator,
        ListRequestedServiceQuotaChangeHistoryPaginator,
        ListServiceQuotaIncreaseRequestsInTemplatePaginator,
        ListServiceQuotasPaginator,
        ListServicesPaginator,
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAWSDefaultServiceQuotasRequestPaginateTypeDef,
    ListAWSDefaultServiceQuotasResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef,
    ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef,
    ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef,
    ListRequestedServiceQuotaChangeHistoryResponseTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef,
    ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef,
    ListServiceQuotasRequestPaginateTypeDef,
    ListServiceQuotasResponseTypeDef,
    ListServicesRequestPaginateTypeDef,
    ListServicesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAWSDefaultServiceQuotasPaginator",
    "ListRequestedServiceQuotaChangeHistoryByQuotaPaginator",
    "ListRequestedServiceQuotaChangeHistoryPaginator",
    "ListServiceQuotaIncreaseRequestsInTemplatePaginator",
    "ListServiceQuotasPaginator",
    "ListServicesPaginator",
)

if TYPE_CHECKING:
    _ListAWSDefaultServiceQuotasPaginatorBase = Paginator[
        ListAWSDefaultServiceQuotasResponseTypeDef
    ]
else:
    _ListAWSDefaultServiceQuotasPaginatorBase = Paginator  # type: ignore[assignment]

class ListAWSDefaultServiceQuotasPaginator(_ListAWSDefaultServiceQuotasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListAWSDefaultServiceQuotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listawsdefaultservicequotaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAWSDefaultServiceQuotasRequestPaginateTypeDef]
    ) -> PageIterator[ListAWSDefaultServiceQuotasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListAWSDefaultServiceQuotas.html#ServiceQuotas.Paginator.ListAWSDefaultServiceQuotas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listawsdefaultservicequotaspaginator)
        """

if TYPE_CHECKING:
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorBase = Paginator[
        ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef
    ]
else:
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorBase = Paginator  # type: ignore[assignment]

class ListRequestedServiceQuotaChangeHistoryByQuotaPaginator(
    _ListRequestedServiceQuotaChangeHistoryByQuotaPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListRequestedServiceQuotaChangeHistoryByQuota.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listrequestedservicequotachangehistorybyquotapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRequestedServiceQuotaChangeHistoryByQuotaRequestPaginateTypeDef]
    ) -> PageIterator[ListRequestedServiceQuotaChangeHistoryByQuotaResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListRequestedServiceQuotaChangeHistoryByQuota.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistoryByQuota.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listrequestedservicequotachangehistorybyquotapaginator)
        """

if TYPE_CHECKING:
    _ListRequestedServiceQuotaChangeHistoryPaginatorBase = Paginator[
        ListRequestedServiceQuotaChangeHistoryResponseTypeDef
    ]
else:
    _ListRequestedServiceQuotaChangeHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class ListRequestedServiceQuotaChangeHistoryPaginator(
    _ListRequestedServiceQuotaChangeHistoryPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListRequestedServiceQuotaChangeHistory.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listrequestedservicequotachangehistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRequestedServiceQuotaChangeHistoryRequestPaginateTypeDef]
    ) -> PageIterator[ListRequestedServiceQuotaChangeHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListRequestedServiceQuotaChangeHistory.html#ServiceQuotas.Paginator.ListRequestedServiceQuotaChangeHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listrequestedservicequotachangehistorypaginator)
        """

if TYPE_CHECKING:
    _ListServiceQuotaIncreaseRequestsInTemplatePaginatorBase = Paginator[
        ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef
    ]
else:
    _ListServiceQuotaIncreaseRequestsInTemplatePaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceQuotaIncreaseRequestsInTemplatePaginator(
    _ListServiceQuotaIncreaseRequestsInTemplatePaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListServiceQuotaIncreaseRequestsInTemplate.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listservicequotaincreaserequestsintemplatepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceQuotaIncreaseRequestsInTemplateRequestPaginateTypeDef]
    ) -> PageIterator[ListServiceQuotaIncreaseRequestsInTemplateResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListServiceQuotaIncreaseRequestsInTemplate.html#ServiceQuotas.Paginator.ListServiceQuotaIncreaseRequestsInTemplate.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listservicequotaincreaserequestsintemplatepaginator)
        """

if TYPE_CHECKING:
    _ListServiceQuotasPaginatorBase = Paginator[ListServiceQuotasResponseTypeDef]
else:
    _ListServiceQuotasPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceQuotasPaginator(_ListServiceQuotasPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListServiceQuotas.html#ServiceQuotas.Paginator.ListServiceQuotas)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listservicequotaspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceQuotasRequestPaginateTypeDef]
    ) -> PageIterator[ListServiceQuotasResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListServiceQuotas.html#ServiceQuotas.Paginator.ListServiceQuotas.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listservicequotaspaginator)
        """

if TYPE_CHECKING:
    _ListServicesPaginatorBase = Paginator[ListServicesResponseTypeDef]
else:
    _ListServicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServicesPaginator(_ListServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListServices.html#ServiceQuotas.Paginator.ListServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicesRequestPaginateTypeDef]
    ) -> PageIterator[ListServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/service-quotas/paginator/ListServices.html#ServiceQuotas.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_service_quotas/paginators/#listservicespaginator)
        """
