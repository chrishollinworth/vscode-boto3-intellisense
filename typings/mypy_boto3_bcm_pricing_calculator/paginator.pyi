"""
Type annotations for bcm-pricing-calculator service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bcm_pricing_calculator.client import BillingandCostManagementPricingCalculatorClient
    from mypy_boto3_bcm_pricing_calculator.paginator import (
        ListBillEstimateCommitmentsPaginator,
        ListBillEstimateInputCommitmentModificationsPaginator,
        ListBillEstimateInputUsageModificationsPaginator,
        ListBillEstimateLineItemsPaginator,
        ListBillEstimatesPaginator,
        ListBillScenarioCommitmentModificationsPaginator,
        ListBillScenarioUsageModificationsPaginator,
        ListBillScenariosPaginator,
        ListWorkloadEstimateUsagePaginator,
        ListWorkloadEstimatesPaginator,
    )

    session = Session()
    client: BillingandCostManagementPricingCalculatorClient = session.client("bcm-pricing-calculator")

    list_bill_estimate_commitments_paginator: ListBillEstimateCommitmentsPaginator = client.get_paginator("list_bill_estimate_commitments")
    list_bill_estimate_input_commitment_modifications_paginator: ListBillEstimateInputCommitmentModificationsPaginator = client.get_paginator("list_bill_estimate_input_commitment_modifications")
    list_bill_estimate_input_usage_modifications_paginator: ListBillEstimateInputUsageModificationsPaginator = client.get_paginator("list_bill_estimate_input_usage_modifications")
    list_bill_estimate_line_items_paginator: ListBillEstimateLineItemsPaginator = client.get_paginator("list_bill_estimate_line_items")
    list_bill_estimates_paginator: ListBillEstimatesPaginator = client.get_paginator("list_bill_estimates")
    list_bill_scenario_commitment_modifications_paginator: ListBillScenarioCommitmentModificationsPaginator = client.get_paginator("list_bill_scenario_commitment_modifications")
    list_bill_scenario_usage_modifications_paginator: ListBillScenarioUsageModificationsPaginator = client.get_paginator("list_bill_scenario_usage_modifications")
    list_bill_scenarios_paginator: ListBillScenariosPaginator = client.get_paginator("list_bill_scenarios")
    list_workload_estimate_usage_paginator: ListWorkloadEstimateUsagePaginator = client.get_paginator("list_workload_estimate_usage")
    list_workload_estimates_paginator: ListWorkloadEstimatesPaginator = client.get_paginator("list_workload_estimates")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListBillEstimateCommitmentsRequestPaginateTypeDef,
    ListBillEstimateCommitmentsResponseTypeDef,
    ListBillEstimateInputCommitmentModificationsRequestPaginateTypeDef,
    ListBillEstimateInputCommitmentModificationsResponseTypeDef,
    ListBillEstimateInputUsageModificationsRequestPaginateTypeDef,
    ListBillEstimateInputUsageModificationsResponsePaginatorTypeDef,
    ListBillEstimateLineItemsRequestPaginateTypeDef,
    ListBillEstimateLineItemsResponseTypeDef,
    ListBillEstimatesRequestPaginateTypeDef,
    ListBillEstimatesResponseTypeDef,
    ListBillScenarioCommitmentModificationsRequestPaginateTypeDef,
    ListBillScenarioCommitmentModificationsResponseTypeDef,
    ListBillScenariosRequestPaginateTypeDef,
    ListBillScenariosResponseTypeDef,
    ListBillScenarioUsageModificationsRequestPaginateTypeDef,
    ListBillScenarioUsageModificationsResponsePaginatorTypeDef,
    ListWorkloadEstimatesRequestPaginateTypeDef,
    ListWorkloadEstimatesResponseTypeDef,
    ListWorkloadEstimateUsageRequestPaginateTypeDef,
    ListWorkloadEstimateUsageResponsePaginatorTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListBillEstimateCommitmentsPaginator",
    "ListBillEstimateInputCommitmentModificationsPaginator",
    "ListBillEstimateInputUsageModificationsPaginator",
    "ListBillEstimateLineItemsPaginator",
    "ListBillEstimatesPaginator",
    "ListBillScenarioCommitmentModificationsPaginator",
    "ListBillScenarioUsageModificationsPaginator",
    "ListBillScenariosPaginator",
    "ListWorkloadEstimateUsagePaginator",
    "ListWorkloadEstimatesPaginator",
)

if TYPE_CHECKING:
    _ListBillEstimateCommitmentsPaginatorBase = Paginator[
        ListBillEstimateCommitmentsResponseTypeDef
    ]
else:
    _ListBillEstimateCommitmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillEstimateCommitmentsPaginator(_ListBillEstimateCommitmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimateCommitments.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimateCommitments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimatecommitmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillEstimateCommitmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListBillEstimateCommitmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimateCommitments.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimateCommitments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimatecommitmentspaginator)
        """

if TYPE_CHECKING:
    _ListBillEstimateInputCommitmentModificationsPaginatorBase = Paginator[
        ListBillEstimateInputCommitmentModificationsResponseTypeDef
    ]
else:
    _ListBillEstimateInputCommitmentModificationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillEstimateInputCommitmentModificationsPaginator(
    _ListBillEstimateInputCommitmentModificationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimateInputCommitmentModifications.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimateInputCommitmentModifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimateinputcommitmentmodificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillEstimateInputCommitmentModificationsRequestPaginateTypeDef]
    ) -> PageIterator[ListBillEstimateInputCommitmentModificationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimateInputCommitmentModifications.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimateInputCommitmentModifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimateinputcommitmentmodificationspaginator)
        """

if TYPE_CHECKING:
    _ListBillEstimateInputUsageModificationsPaginatorBase = Paginator[
        ListBillEstimateInputUsageModificationsResponsePaginatorTypeDef
    ]
else:
    _ListBillEstimateInputUsageModificationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillEstimateInputUsageModificationsPaginator(
    _ListBillEstimateInputUsageModificationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimateInputUsageModifications.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimateInputUsageModifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimateinputusagemodificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillEstimateInputUsageModificationsRequestPaginateTypeDef]
    ) -> PageIterator[ListBillEstimateInputUsageModificationsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimateInputUsageModifications.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimateInputUsageModifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimateinputusagemodificationspaginator)
        """

if TYPE_CHECKING:
    _ListBillEstimateLineItemsPaginatorBase = Paginator[ListBillEstimateLineItemsResponseTypeDef]
else:
    _ListBillEstimateLineItemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillEstimateLineItemsPaginator(_ListBillEstimateLineItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimateLineItems.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimateLineItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimatelineitemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillEstimateLineItemsRequestPaginateTypeDef]
    ) -> PageIterator[ListBillEstimateLineItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimateLineItems.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimateLineItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimatelineitemspaginator)
        """

if TYPE_CHECKING:
    _ListBillEstimatesPaginatorBase = Paginator[ListBillEstimatesResponseTypeDef]
else:
    _ListBillEstimatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillEstimatesPaginator(_ListBillEstimatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimates.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillEstimatesRequestPaginateTypeDef]
    ) -> PageIterator[ListBillEstimatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillEstimates.html#BillingandCostManagementPricingCalculator.Paginator.ListBillEstimates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillestimatespaginator)
        """

if TYPE_CHECKING:
    _ListBillScenarioCommitmentModificationsPaginatorBase = Paginator[
        ListBillScenarioCommitmentModificationsResponseTypeDef
    ]
else:
    _ListBillScenarioCommitmentModificationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillScenarioCommitmentModificationsPaginator(
    _ListBillScenarioCommitmentModificationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillScenarioCommitmentModifications.html#BillingandCostManagementPricingCalculator.Paginator.ListBillScenarioCommitmentModifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillscenariocommitmentmodificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillScenarioCommitmentModificationsRequestPaginateTypeDef]
    ) -> PageIterator[ListBillScenarioCommitmentModificationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillScenarioCommitmentModifications.html#BillingandCostManagementPricingCalculator.Paginator.ListBillScenarioCommitmentModifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillscenariocommitmentmodificationspaginator)
        """

if TYPE_CHECKING:
    _ListBillScenarioUsageModificationsPaginatorBase = Paginator[
        ListBillScenarioUsageModificationsResponsePaginatorTypeDef
    ]
else:
    _ListBillScenarioUsageModificationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillScenarioUsageModificationsPaginator(_ListBillScenarioUsageModificationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillScenarioUsageModifications.html#BillingandCostManagementPricingCalculator.Paginator.ListBillScenarioUsageModifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillscenariousagemodificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillScenarioUsageModificationsRequestPaginateTypeDef]
    ) -> PageIterator[ListBillScenarioUsageModificationsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillScenarioUsageModifications.html#BillingandCostManagementPricingCalculator.Paginator.ListBillScenarioUsageModifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillscenariousagemodificationspaginator)
        """

if TYPE_CHECKING:
    _ListBillScenariosPaginatorBase = Paginator[ListBillScenariosResponseTypeDef]
else:
    _ListBillScenariosPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillScenariosPaginator(_ListBillScenariosPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillScenarios.html#BillingandCostManagementPricingCalculator.Paginator.ListBillScenarios)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillscenariospaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillScenariosRequestPaginateTypeDef]
    ) -> PageIterator[ListBillScenariosResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListBillScenarios.html#BillingandCostManagementPricingCalculator.Paginator.ListBillScenarios.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listbillscenariospaginator)
        """

if TYPE_CHECKING:
    _ListWorkloadEstimateUsagePaginatorBase = Paginator[
        ListWorkloadEstimateUsageResponsePaginatorTypeDef
    ]
else:
    _ListWorkloadEstimateUsagePaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkloadEstimateUsagePaginator(_ListWorkloadEstimateUsagePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListWorkloadEstimateUsage.html#BillingandCostManagementPricingCalculator.Paginator.ListWorkloadEstimateUsage)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listworkloadestimateusagepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkloadEstimateUsageRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkloadEstimateUsageResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListWorkloadEstimateUsage.html#BillingandCostManagementPricingCalculator.Paginator.ListWorkloadEstimateUsage.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listworkloadestimateusagepaginator)
        """

if TYPE_CHECKING:
    _ListWorkloadEstimatesPaginatorBase = Paginator[ListWorkloadEstimatesResponseTypeDef]
else:
    _ListWorkloadEstimatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkloadEstimatesPaginator(_ListWorkloadEstimatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListWorkloadEstimates.html#BillingandCostManagementPricingCalculator.Paginator.ListWorkloadEstimates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listworkloadestimatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkloadEstimatesRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkloadEstimatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bcm-pricing-calculator/paginator/ListWorkloadEstimates.html#BillingandCostManagementPricingCalculator.Paginator.ListWorkloadEstimates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/paginators/#listworkloadestimatespaginator)
        """
