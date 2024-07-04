"""
Type annotations for billingconductor service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_billingconductor import BillingConductorClient
    from mypy_boto3_billingconductor.paginator import (
        ListAccountAssociationsPaginator,
        ListBillingGroupCostReportsPaginator,
        ListBillingGroupsPaginator,
        ListCustomLineItemVersionsPaginator,
        ListCustomLineItemsPaginator,
        ListPricingPlansPaginator,
        ListPricingPlansAssociatedWithPricingRulePaginator,
        ListPricingRulesPaginator,
        ListPricingRulesAssociatedToPricingPlanPaginator,
        ListResourcesAssociatedToCustomLineItemPaginator,
    )

    client: BillingConductorClient = boto3.client("billingconductor")

    list_account_associations_paginator: ListAccountAssociationsPaginator = client.get_paginator("list_account_associations")
    list_billing_group_cost_reports_paginator: ListBillingGroupCostReportsPaginator = client.get_paginator("list_billing_group_cost_reports")
    list_billing_groups_paginator: ListBillingGroupsPaginator = client.get_paginator("list_billing_groups")
    list_custom_line_item_versions_paginator: ListCustomLineItemVersionsPaginator = client.get_paginator("list_custom_line_item_versions")
    list_custom_line_items_paginator: ListCustomLineItemsPaginator = client.get_paginator("list_custom_line_items")
    list_pricing_plans_paginator: ListPricingPlansPaginator = client.get_paginator("list_pricing_plans")
    list_pricing_plans_associated_with_pricing_rule_paginator: ListPricingPlansAssociatedWithPricingRulePaginator = client.get_paginator("list_pricing_plans_associated_with_pricing_rule")
    list_pricing_rules_paginator: ListPricingRulesPaginator = client.get_paginator("list_pricing_rules")
    list_pricing_rules_associated_to_pricing_plan_paginator: ListPricingRulesAssociatedToPricingPlanPaginator = client.get_paginator("list_pricing_rules_associated_to_pricing_plan")
    list_resources_associated_to_custom_line_item_paginator: ListResourcesAssociatedToCustomLineItemPaginator = client.get_paginator("list_resources_associated_to_custom_line_item")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListAccountAssociationsFilterTypeDef,
    ListAccountAssociationsOutputTypeDef,
    ListBillingGroupCostReportsFilterTypeDef,
    ListBillingGroupCostReportsOutputTypeDef,
    ListBillingGroupsFilterTypeDef,
    ListBillingGroupsOutputTypeDef,
    ListCustomLineItemsFilterTypeDef,
    ListCustomLineItemsOutputTypeDef,
    ListCustomLineItemVersionsFilterTypeDef,
    ListCustomLineItemVersionsOutputTypeDef,
    ListPricingPlansAssociatedWithPricingRuleOutputTypeDef,
    ListPricingPlansFilterTypeDef,
    ListPricingPlansOutputTypeDef,
    ListPricingRulesAssociatedToPricingPlanOutputTypeDef,
    ListPricingRulesFilterTypeDef,
    ListPricingRulesOutputTypeDef,
    ListResourcesAssociatedToCustomLineItemFilterTypeDef,
    ListResourcesAssociatedToCustomLineItemOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListAccountAssociationsPaginator",
    "ListBillingGroupCostReportsPaginator",
    "ListBillingGroupsPaginator",
    "ListCustomLineItemVersionsPaginator",
    "ListCustomLineItemsPaginator",
    "ListPricingPlansPaginator",
    "ListPricingPlansAssociatedWithPricingRulePaginator",
    "ListPricingRulesPaginator",
    "ListPricingRulesAssociatedToPricingPlanPaginator",
    "ListResourcesAssociatedToCustomLineItemPaginator",
)

class ListAccountAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListAccountAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listaccountassociationspaginator)
    """

    def paginate(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListAccountAssociationsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAccountAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListAccountAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listaccountassociationspaginator)
        """

class ListBillingGroupCostReportsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListBillingGroupCostReports)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listbillinggroupcostreportspaginator)
    """

    def paginate(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListBillingGroupCostReportsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBillingGroupCostReportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListBillingGroupCostReports.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listbillinggroupcostreportspaginator)
        """

class ListBillingGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListBillingGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listbillinggroupspaginator)
    """

    def paginate(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListBillingGroupsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBillingGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListBillingGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listbillinggroupspaginator)
        """

class ListCustomLineItemVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListCustomLineItemVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listcustomlineitemversionspaginator)
    """

    def paginate(
        self,
        *,
        Arn: str,
        Filters: "ListCustomLineItemVersionsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomLineItemVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListCustomLineItemVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listcustomlineitemversionspaginator)
        """

class ListCustomLineItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListCustomLineItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listcustomlineitemspaginator)
    """

    def paginate(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListCustomLineItemsFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCustomLineItemsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListCustomLineItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listcustomlineitemspaginator)
        """

class ListPricingPlansPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingPlans)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingplanspaginator)
    """

    def paginate(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListPricingPlansFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPricingPlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingPlans.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingplanspaginator)
        """

class ListPricingPlansAssociatedWithPricingRulePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingPlansAssociatedWithPricingRule)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingplansassociatedwithpricingrulepaginator)
    """

    def paginate(
        self,
        *,
        PricingRuleArn: str,
        BillingPeriod: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPricingPlansAssociatedWithPricingRuleOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingPlansAssociatedWithPricingRule.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingplansassociatedwithpricingrulepaginator)
        """

class ListPricingRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingrulespaginator)
    """

    def paginate(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListPricingRulesFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPricingRulesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingrulespaginator)
        """

class ListPricingRulesAssociatedToPricingPlanPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingRulesAssociatedToPricingPlan)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingrulesassociatedtopricingplanpaginator)
    """

    def paginate(
        self,
        *,
        PricingPlanArn: str,
        BillingPeriod: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPricingRulesAssociatedToPricingPlanOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingRulesAssociatedToPricingPlan.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingrulesassociatedtopricingplanpaginator)
        """

class ListResourcesAssociatedToCustomLineItemPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListResourcesAssociatedToCustomLineItem)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listresourcesassociatedtocustomlineitempaginator)
    """

    def paginate(
        self,
        *,
        Arn: str,
        BillingPeriod: str = None,
        Filters: "ListResourcesAssociatedToCustomLineItemFilterTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourcesAssociatedToCustomLineItemOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/billingconductor.html#BillingConductor.Paginator.ListResourcesAssociatedToCustomLineItem.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listresourcesassociatedtocustomlineitempaginator)
        """
