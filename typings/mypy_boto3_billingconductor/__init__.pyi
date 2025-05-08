"""
Main interface for billingconductor service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_billingconductor import (
        BillingConductorClient,
        Client,
        ListAccountAssociationsPaginator,
        ListBillingGroupCostReportsPaginator,
        ListBillingGroupsPaginator,
        ListCustomLineItemVersionsPaginator,
        ListCustomLineItemsPaginator,
        ListPricingPlansAssociatedWithPricingRulePaginator,
        ListPricingPlansPaginator,
        ListPricingRulesAssociatedToPricingPlanPaginator,
        ListPricingRulesPaginator,
        ListResourcesAssociatedToCustomLineItemPaginator,
    )

    session = Session()
    client: BillingConductorClient = session.client("billingconductor")

    list_account_associations_paginator: ListAccountAssociationsPaginator = client.get_paginator("list_account_associations")
    list_billing_group_cost_reports_paginator: ListBillingGroupCostReportsPaginator = client.get_paginator("list_billing_group_cost_reports")
    list_billing_groups_paginator: ListBillingGroupsPaginator = client.get_paginator("list_billing_groups")
    list_custom_line_item_versions_paginator: ListCustomLineItemVersionsPaginator = client.get_paginator("list_custom_line_item_versions")
    list_custom_line_items_paginator: ListCustomLineItemsPaginator = client.get_paginator("list_custom_line_items")
    list_pricing_plans_associated_with_pricing_rule_paginator: ListPricingPlansAssociatedWithPricingRulePaginator = client.get_paginator("list_pricing_plans_associated_with_pricing_rule")
    list_pricing_plans_paginator: ListPricingPlansPaginator = client.get_paginator("list_pricing_plans")
    list_pricing_rules_associated_to_pricing_plan_paginator: ListPricingRulesAssociatedToPricingPlanPaginator = client.get_paginator("list_pricing_rules_associated_to_pricing_plan")
    list_pricing_rules_paginator: ListPricingRulesPaginator = client.get_paginator("list_pricing_rules")
    list_resources_associated_to_custom_line_item_paginator: ListResourcesAssociatedToCustomLineItemPaginator = client.get_paginator("list_resources_associated_to_custom_line_item")
    ```
"""

from .client import BillingConductorClient
from .paginator import (
    ListAccountAssociationsPaginator,
    ListBillingGroupCostReportsPaginator,
    ListBillingGroupsPaginator,
    ListCustomLineItemsPaginator,
    ListCustomLineItemVersionsPaginator,
    ListPricingPlansAssociatedWithPricingRulePaginator,
    ListPricingPlansPaginator,
    ListPricingRulesAssociatedToPricingPlanPaginator,
    ListPricingRulesPaginator,
    ListResourcesAssociatedToCustomLineItemPaginator,
)

Client = BillingConductorClient

__all__ = (
    "BillingConductorClient",
    "Client",
    "ListAccountAssociationsPaginator",
    "ListBillingGroupCostReportsPaginator",
    "ListBillingGroupsPaginator",
    "ListCustomLineItemVersionsPaginator",
    "ListCustomLineItemsPaginator",
    "ListPricingPlansAssociatedWithPricingRulePaginator",
    "ListPricingPlansPaginator",
    "ListPricingRulesAssociatedToPricingPlanPaginator",
    "ListPricingRulesPaginator",
    "ListResourcesAssociatedToCustomLineItemPaginator",
)
