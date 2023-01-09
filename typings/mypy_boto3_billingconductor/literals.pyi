"""
Type annotations for billingconductor service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/literals.html)

Usage::

    ```python
    from mypy_boto3_billingconductor.literals import AssociateResourceErrorReasonType

    data: AssociateResourceErrorReasonType = "ILLEGAL_CUSTOMLINEITEM"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssociateResourceErrorReasonType",
    "BillingGroupStatusType",
    "CurrencyCodeType",
    "CustomLineItemRelationshipType",
    "CustomLineItemTypeType",
    "ListAccountAssociationsPaginatorName",
    "ListBillingGroupCostReportsPaginatorName",
    "ListBillingGroupsPaginatorName",
    "ListCustomLineItemVersionsPaginatorName",
    "ListCustomLineItemsPaginatorName",
    "ListPricingPlansAssociatedWithPricingRulePaginatorName",
    "ListPricingPlansPaginatorName",
    "ListPricingRulesAssociatedToPricingPlanPaginatorName",
    "ListPricingRulesPaginatorName",
    "ListResourcesAssociatedToCustomLineItemPaginatorName",
    "PricingRuleScopeType",
    "PricingRuleTypeType",
)

AssociateResourceErrorReasonType = Literal[
    "ILLEGAL_CUSTOMLINEITEM",
    "INTERNAL_SERVER_EXCEPTION",
    "INVALID_ARN",
    "INVALID_BILLING_PERIOD_RANGE",
    "SERVICE_LIMIT_EXCEEDED",
]
BillingGroupStatusType = Literal["ACTIVE", "PRIMARY_ACCOUNT_MISSING"]
CurrencyCodeType = Literal["CNY", "USD"]
CustomLineItemRelationshipType = Literal["CHILD", "PARENT"]
CustomLineItemTypeType = Literal["CREDIT", "FEE"]
ListAccountAssociationsPaginatorName = Literal["list_account_associations"]
ListBillingGroupCostReportsPaginatorName = Literal["list_billing_group_cost_reports"]
ListBillingGroupsPaginatorName = Literal["list_billing_groups"]
ListCustomLineItemVersionsPaginatorName = Literal["list_custom_line_item_versions"]
ListCustomLineItemsPaginatorName = Literal["list_custom_line_items"]
ListPricingPlansAssociatedWithPricingRulePaginatorName = Literal[
    "list_pricing_plans_associated_with_pricing_rule"
]
ListPricingPlansPaginatorName = Literal["list_pricing_plans"]
ListPricingRulesAssociatedToPricingPlanPaginatorName = Literal[
    "list_pricing_rules_associated_to_pricing_plan"
]
ListPricingRulesPaginatorName = Literal["list_pricing_rules"]
ListResourcesAssociatedToCustomLineItemPaginatorName = Literal[
    "list_resources_associated_to_custom_line_item"
]
PricingRuleScopeType = Literal["BILLING_ENTITY", "GLOBAL", "SERVICE"]
PricingRuleTypeType = Literal["DISCOUNT", "MARKUP", "TIERING"]
