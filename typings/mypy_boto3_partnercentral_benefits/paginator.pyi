"""
Type annotations for partnercentral-benefits service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_partnercentral_benefits.client import PartnerCentralBenefitsClient
    from mypy_boto3_partnercentral_benefits.paginator import (
        ListBenefitAllocationsPaginator,
        ListBenefitApplicationsPaginator,
        ListBenefitsPaginator,
    )

    session = Session()
    client: PartnerCentralBenefitsClient = session.client("partnercentral-benefits")

    list_benefit_allocations_paginator: ListBenefitAllocationsPaginator = client.get_paginator("list_benefit_allocations")
    list_benefit_applications_paginator: ListBenefitApplicationsPaginator = client.get_paginator("list_benefit_applications")
    list_benefits_paginator: ListBenefitsPaginator = client.get_paginator("list_benefits")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListBenefitAllocationsInputPaginateTypeDef,
    ListBenefitAllocationsOutputTypeDef,
    ListBenefitApplicationsInputPaginateTypeDef,
    ListBenefitApplicationsOutputTypeDef,
    ListBenefitsInputPaginateTypeDef,
    ListBenefitsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListBenefitAllocationsPaginator",
    "ListBenefitApplicationsPaginator",
    "ListBenefitsPaginator",
)

if TYPE_CHECKING:
    _ListBenefitAllocationsPaginatorBase = Paginator[ListBenefitAllocationsOutputTypeDef]
else:
    _ListBenefitAllocationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBenefitAllocationsPaginator(_ListBenefitAllocationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/paginator/ListBenefitAllocations.html#PartnerCentralBenefits.Paginator.ListBenefitAllocations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/paginators/#listbenefitallocationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBenefitAllocationsInputPaginateTypeDef]
    ) -> PageIterator[ListBenefitAllocationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/paginator/ListBenefitAllocations.html#PartnerCentralBenefits.Paginator.ListBenefitAllocations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/paginators/#listbenefitallocationspaginator)
        """

if TYPE_CHECKING:
    _ListBenefitApplicationsPaginatorBase = Paginator[ListBenefitApplicationsOutputTypeDef]
else:
    _ListBenefitApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBenefitApplicationsPaginator(_ListBenefitApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/paginator/ListBenefitApplications.html#PartnerCentralBenefits.Paginator.ListBenefitApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/paginators/#listbenefitapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBenefitApplicationsInputPaginateTypeDef]
    ) -> PageIterator[ListBenefitApplicationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/paginator/ListBenefitApplications.html#PartnerCentralBenefits.Paginator.ListBenefitApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/paginators/#listbenefitapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListBenefitsPaginatorBase = Paginator[ListBenefitsOutputTypeDef]
else:
    _ListBenefitsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBenefitsPaginator(_ListBenefitsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/paginator/ListBenefits.html#PartnerCentralBenefits.Paginator.ListBenefits)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/paginators/#listbenefitspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBenefitsInputPaginateTypeDef]
    ) -> PageIterator[ListBenefitsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/partnercentral-benefits/paginator/ListBenefits.html#PartnerCentralBenefits.Paginator.ListBenefits.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/paginators/#listbenefitspaginator)
        """
