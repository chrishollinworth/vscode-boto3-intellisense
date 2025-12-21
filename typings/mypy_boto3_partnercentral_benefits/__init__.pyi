"""
Main interface for partnercentral-benefits service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_partnercentral_benefits/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_partnercentral_benefits import (
        Client,
        ListBenefitAllocationsPaginator,
        ListBenefitApplicationsPaginator,
        ListBenefitsPaginator,
        PartnerCentralBenefitsClient,
    )

    session = Session()
    client: PartnerCentralBenefitsClient = session.client("partnercentral-benefits")

    list_benefit_allocations_paginator: ListBenefitAllocationsPaginator = client.get_paginator("list_benefit_allocations")
    list_benefit_applications_paginator: ListBenefitApplicationsPaginator = client.get_paginator("list_benefit_applications")
    list_benefits_paginator: ListBenefitsPaginator = client.get_paginator("list_benefits")
    ```
"""

from .client import PartnerCentralBenefitsClient
from .paginator import (
    ListBenefitAllocationsPaginator,
    ListBenefitApplicationsPaginator,
    ListBenefitsPaginator,
)

Client = PartnerCentralBenefitsClient

__all__ = (
    "Client",
    "ListBenefitAllocationsPaginator",
    "ListBenefitApplicationsPaginator",
    "ListBenefitsPaginator",
    "PartnerCentralBenefitsClient",
)
