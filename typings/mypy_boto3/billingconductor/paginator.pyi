"""
Type annotations for billingconductor service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_billingconductor.client import BillingConductorClient
    from mypy_boto3_billingconductor.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccountAssociationsInputPaginateTypeDef,
    ListAccountAssociationsOutputTypeDef,
    ListBillingGroupCostReportsInputPaginateTypeDef,
    ListBillingGroupCostReportsOutputTypeDef,
    ListBillingGroupsInputPaginateTypeDef,
    ListBillingGroupsOutputTypeDef,
    ListCustomLineItemsInputPaginateTypeDef,
    ListCustomLineItemsOutputTypeDef,
    ListCustomLineItemVersionsInputPaginateTypeDef,
    ListCustomLineItemVersionsOutputTypeDef,
    ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef,
    ListPricingPlansAssociatedWithPricingRuleOutputTypeDef,
    ListPricingPlansInputPaginateTypeDef,
    ListPricingPlansOutputTypeDef,
    ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef,
    ListPricingRulesAssociatedToPricingPlanOutputTypeDef,
    ListPricingRulesInputPaginateTypeDef,
    ListPricingRulesOutputTypeDef,
    ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef,
    ListResourcesAssociatedToCustomLineItemOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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

if TYPE_CHECKING:
    _ListAccountAssociationsPaginatorBase = Paginator[ListAccountAssociationsOutputTypeDef]
else:
    _ListAccountAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountAssociationsPaginator(_ListAccountAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListAccountAssociations.html#BillingConductor.Paginator.ListAccountAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listaccountassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountAssociationsInputPaginateTypeDef]
    ) -> PageIterator[ListAccountAssociationsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListAccountAssociations.html#BillingConductor.Paginator.ListAccountAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listaccountassociationspaginator)
        """

if TYPE_CHECKING:
    _ListBillingGroupCostReportsPaginatorBase = Paginator[ListBillingGroupCostReportsOutputTypeDef]
else:
    _ListBillingGroupCostReportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillingGroupCostReportsPaginator(_ListBillingGroupCostReportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListBillingGroupCostReports.html#BillingConductor.Paginator.ListBillingGroupCostReports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listbillinggroupcostreportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillingGroupCostReportsInputPaginateTypeDef]
    ) -> PageIterator[ListBillingGroupCostReportsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListBillingGroupCostReports.html#BillingConductor.Paginator.ListBillingGroupCostReports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listbillinggroupcostreportspaginator)
        """

if TYPE_CHECKING:
    _ListBillingGroupsPaginatorBase = Paginator[ListBillingGroupsOutputTypeDef]
else:
    _ListBillingGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBillingGroupsPaginator(_ListBillingGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListBillingGroups.html#BillingConductor.Paginator.ListBillingGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listbillinggroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBillingGroupsInputPaginateTypeDef]
    ) -> PageIterator[ListBillingGroupsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListBillingGroups.html#BillingConductor.Paginator.ListBillingGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listbillinggroupspaginator)
        """

if TYPE_CHECKING:
    _ListCustomLineItemVersionsPaginatorBase = Paginator[ListCustomLineItemVersionsOutputTypeDef]
else:
    _ListCustomLineItemVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomLineItemVersionsPaginator(_ListCustomLineItemVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListCustomLineItemVersions.html#BillingConductor.Paginator.ListCustomLineItemVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listcustomlineitemversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomLineItemVersionsInputPaginateTypeDef]
    ) -> PageIterator[ListCustomLineItemVersionsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListCustomLineItemVersions.html#BillingConductor.Paginator.ListCustomLineItemVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listcustomlineitemversionspaginator)
        """

if TYPE_CHECKING:
    _ListCustomLineItemsPaginatorBase = Paginator[ListCustomLineItemsOutputTypeDef]
else:
    _ListCustomLineItemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCustomLineItemsPaginator(_ListCustomLineItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListCustomLineItems.html#BillingConductor.Paginator.ListCustomLineItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listcustomlineitemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCustomLineItemsInputPaginateTypeDef]
    ) -> PageIterator[ListCustomLineItemsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListCustomLineItems.html#BillingConductor.Paginator.ListCustomLineItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listcustomlineitemspaginator)
        """

if TYPE_CHECKING:
    _ListPricingPlansAssociatedWithPricingRulePaginatorBase = Paginator[
        ListPricingPlansAssociatedWithPricingRuleOutputTypeDef
    ]
else:
    _ListPricingPlansAssociatedWithPricingRulePaginatorBase = Paginator  # type: ignore[assignment]

class ListPricingPlansAssociatedWithPricingRulePaginator(
    _ListPricingPlansAssociatedWithPricingRulePaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListPricingPlansAssociatedWithPricingRule.html#BillingConductor.Paginator.ListPricingPlansAssociatedWithPricingRule)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listpricingplansassociatedwithpricingrulepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef]
    ) -> PageIterator[ListPricingPlansAssociatedWithPricingRuleOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListPricingPlansAssociatedWithPricingRule.html#BillingConductor.Paginator.ListPricingPlansAssociatedWithPricingRule.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listpricingplansassociatedwithpricingrulepaginator)
        """

if TYPE_CHECKING:
    _ListPricingPlansPaginatorBase = Paginator[ListPricingPlansOutputTypeDef]
else:
    _ListPricingPlansPaginatorBase = Paginator  # type: ignore[assignment]

class ListPricingPlansPaginator(_ListPricingPlansPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListPricingPlans.html#BillingConductor.Paginator.ListPricingPlans)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listpricingplanspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPricingPlansInputPaginateTypeDef]
    ) -> PageIterator[ListPricingPlansOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListPricingPlans.html#BillingConductor.Paginator.ListPricingPlans.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listpricingplanspaginator)
        """

if TYPE_CHECKING:
    _ListPricingRulesAssociatedToPricingPlanPaginatorBase = Paginator[
        ListPricingRulesAssociatedToPricingPlanOutputTypeDef
    ]
else:
    _ListPricingRulesAssociatedToPricingPlanPaginatorBase = Paginator  # type: ignore[assignment]

class ListPricingRulesAssociatedToPricingPlanPaginator(
    _ListPricingRulesAssociatedToPricingPlanPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListPricingRulesAssociatedToPricingPlan.html#BillingConductor.Paginator.ListPricingRulesAssociatedToPricingPlan)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listpricingrulesassociatedtopricingplanpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef]
    ) -> PageIterator[ListPricingRulesAssociatedToPricingPlanOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListPricingRulesAssociatedToPricingPlan.html#BillingConductor.Paginator.ListPricingRulesAssociatedToPricingPlan.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listpricingrulesassociatedtopricingplanpaginator)
        """

if TYPE_CHECKING:
    _ListPricingRulesPaginatorBase = Paginator[ListPricingRulesOutputTypeDef]
else:
    _ListPricingRulesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPricingRulesPaginator(_ListPricingRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListPricingRules.html#BillingConductor.Paginator.ListPricingRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listpricingrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPricingRulesInputPaginateTypeDef]
    ) -> PageIterator[ListPricingRulesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListPricingRules.html#BillingConductor.Paginator.ListPricingRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listpricingrulespaginator)
        """

if TYPE_CHECKING:
    _ListResourcesAssociatedToCustomLineItemPaginatorBase = Paginator[
        ListResourcesAssociatedToCustomLineItemOutputTypeDef
    ]
else:
    _ListResourcesAssociatedToCustomLineItemPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourcesAssociatedToCustomLineItemPaginator(
    _ListResourcesAssociatedToCustomLineItemPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListResourcesAssociatedToCustomLineItem.html#BillingConductor.Paginator.ListResourcesAssociatedToCustomLineItem)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listresourcesassociatedtocustomlineitempaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef]
    ) -> PageIterator[ListResourcesAssociatedToCustomLineItemOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/paginator/ListResourcesAssociatedToCustomLineItem.html#BillingConductor.Paginator.ListResourcesAssociatedToCustomLineItem.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators/#listresourcesassociatedtocustomlineitempaginator)
        """
