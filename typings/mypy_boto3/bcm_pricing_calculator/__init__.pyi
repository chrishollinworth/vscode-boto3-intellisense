"""
Main interface for bcm-pricing-calculator service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bcm_pricing_calculator/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bcm_pricing_calculator import (
        BillingandCostManagementPricingCalculatorClient,
        Client,
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

from .client import BillingandCostManagementPricingCalculatorClient
from .paginator import (
    ListBillEstimateCommitmentsPaginator,
    ListBillEstimateInputCommitmentModificationsPaginator,
    ListBillEstimateInputUsageModificationsPaginator,
    ListBillEstimateLineItemsPaginator,
    ListBillEstimatesPaginator,
    ListBillScenarioCommitmentModificationsPaginator,
    ListBillScenariosPaginator,
    ListBillScenarioUsageModificationsPaginator,
    ListWorkloadEstimatesPaginator,
    ListWorkloadEstimateUsagePaginator,
)

Client = BillingandCostManagementPricingCalculatorClient

__all__ = (
    "BillingandCostManagementPricingCalculatorClient",
    "Client",
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
