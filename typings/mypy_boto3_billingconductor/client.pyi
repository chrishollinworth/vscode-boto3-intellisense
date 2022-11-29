"""
Type annotations for billingconductor service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_billingconductor import BillingConductorClient

    client: BillingConductorClient = boto3.client("billingconductor")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import BillingGroupStatusType, PricingRuleScopeType, PricingRuleTypeType
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
from .type_defs import (
    AccountGroupingTypeDef,
    AssociateAccountsOutputTypeDef,
    AssociatePricingRulesOutputTypeDef,
    BatchAssociateResourcesToCustomLineItemOutputTypeDef,
    BatchDisassociateResourcesFromCustomLineItemOutputTypeDef,
    ComputationPreferenceTypeDef,
    CreateBillingGroupOutputTypeDef,
    CreateCustomLineItemOutputTypeDef,
    CreatePricingPlanOutputTypeDef,
    CreatePricingRuleOutputTypeDef,
    CustomLineItemBillingPeriodRangeTypeDef,
    CustomLineItemChargeDetailsTypeDef,
    DeleteBillingGroupOutputTypeDef,
    DeleteCustomLineItemOutputTypeDef,
    DeletePricingPlanOutputTypeDef,
    DeletePricingRuleOutputTypeDef,
    DisassociateAccountsOutputTypeDef,
    DisassociatePricingRulesOutputTypeDef,
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
    ListTagsForResourceResponseTypeDef,
    UpdateBillingGroupOutputTypeDef,
    UpdateCustomLineItemChargeDetailsTypeDef,
    UpdateCustomLineItemOutputTypeDef,
    UpdatePricingPlanOutputTypeDef,
    UpdatePricingRuleOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("BillingConductorClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceLimitExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BillingConductorClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BillingConductorClient exceptions.
        """
    def associate_accounts(
        self, *, Arn: str, AccountIds: List[str]
    ) -> AssociateAccountsOutputTypeDef:
        """
        Connects an array of account IDs in a consolidated billing family to a
        predefined billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.associate_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#associate_accounts)
        """
    def associate_pricing_rules(
        self, *, Arn: str, PricingRuleArns: List[str]
    ) -> AssociatePricingRulesOutputTypeDef:
        """
        Connects an array of `PricingRuleArns` to a defined `PricingPlan`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.associate_pricing_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#associate_pricing_rules)
        """
    def batch_associate_resources_to_custom_line_item(
        self,
        *,
        TargetArn: str,
        ResourceArns: List[str],
        BillingPeriodRange: "CustomLineItemBillingPeriodRangeTypeDef" = None
    ) -> BatchAssociateResourcesToCustomLineItemOutputTypeDef:
        """
        Associates a batch of resources to a percentage custom line item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.batch_associate_resources_to_custom_line_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#batch_associate_resources_to_custom_line_item)
        """
    def batch_disassociate_resources_from_custom_line_item(
        self,
        *,
        TargetArn: str,
        ResourceArns: List[str],
        BillingPeriodRange: "CustomLineItemBillingPeriodRangeTypeDef" = None
    ) -> BatchDisassociateResourcesFromCustomLineItemOutputTypeDef:
        """
        Disassociates a batch of resources from a percentage custom line item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.batch_disassociate_resources_from_custom_line_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#batch_disassociate_resources_from_custom_line_item)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#close)
        """
    def create_billing_group(
        self,
        *,
        Name: str,
        AccountGrouping: "AccountGroupingTypeDef",
        ComputationPreference: "ComputationPreferenceTypeDef",
        ClientToken: str = None,
        PrimaryAccountId: str = None,
        Description: str = None,
        Tags: Dict[str, str] = None
    ) -> CreateBillingGroupOutputTypeDef:
        """
        Creates a billing group that resembles a consolidated billing family that Amazon
        Web Services charges, based off of the predefined pricing plan computation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.create_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#create_billing_group)
        """
    def create_custom_line_item(
        self,
        *,
        Name: str,
        Description: str,
        BillingGroupArn: str,
        ChargeDetails: "CustomLineItemChargeDetailsTypeDef",
        ClientToken: str = None,
        BillingPeriodRange: "CustomLineItemBillingPeriodRangeTypeDef" = None,
        Tags: Dict[str, str] = None
    ) -> CreateCustomLineItemOutputTypeDef:
        """
        Creates a custom line item that can be used to create a one-time fixed charge
        that can be applied to a single billing group for the current or previous
        billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.create_custom_line_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#create_custom_line_item)
        """
    def create_pricing_plan(
        self,
        *,
        Name: str,
        ClientToken: str = None,
        Description: str = None,
        PricingRuleArns: List[str] = None,
        Tags: Dict[str, str] = None
    ) -> CreatePricingPlanOutputTypeDef:
        """
        Creates a pricing plan that is used for computing Amazon Web Services charges
        for billing groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.create_pricing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#create_pricing_plan)
        """
    def create_pricing_rule(
        self,
        *,
        Name: str,
        Scope: PricingRuleScopeType,
        Type: PricingRuleTypeType,
        ModifierPercentage: float,
        ClientToken: str = None,
        Description: str = None,
        Service: str = None,
        Tags: Dict[str, str] = None,
        BillingEntity: str = None
    ) -> CreatePricingRuleOutputTypeDef:
        """
        Creates a pricing rule can be associated to a pricing plan, or a set of pricing
        plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.create_pricing_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#create_pricing_rule)
        """
    def delete_billing_group(self, *, Arn: str) -> DeleteBillingGroupOutputTypeDef:
        """
        Deletes a billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.delete_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#delete_billing_group)
        """
    def delete_custom_line_item(
        self, *, Arn: str, BillingPeriodRange: "CustomLineItemBillingPeriodRangeTypeDef" = None
    ) -> DeleteCustomLineItemOutputTypeDef:
        """
        Deletes the custom line item identified by the given ARN in the current, or
        previous billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.delete_custom_line_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#delete_custom_line_item)
        """
    def delete_pricing_plan(self, *, Arn: str) -> DeletePricingPlanOutputTypeDef:
        """
        Deletes a pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.delete_pricing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#delete_pricing_plan)
        """
    def delete_pricing_rule(self, *, Arn: str) -> DeletePricingRuleOutputTypeDef:
        """
        Deletes the pricing rule that's identified by the input Amazon Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.delete_pricing_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#delete_pricing_rule)
        """
    def disassociate_accounts(
        self, *, Arn: str, AccountIds: List[str]
    ) -> DisassociateAccountsOutputTypeDef:
        """
        Removes the specified list of account IDs from the given billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.disassociate_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#disassociate_accounts)
        """
    def disassociate_pricing_rules(
        self, *, Arn: str, PricingRuleArns: List[str]
    ) -> DisassociatePricingRulesOutputTypeDef:
        """
        Disassociates a list of pricing rules from a pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.disassociate_pricing_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#disassociate_pricing_rules)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#generate_presigned_url)
        """
    def list_account_associations(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListAccountAssociationsFilterTypeDef" = None,
        NextToken: str = None
    ) -> ListAccountAssociationsOutputTypeDef:
        """
        This is a paginated call to list linked accounts that are linked to the payer
        account for the specified time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_account_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_account_associations)
        """
    def list_billing_group_cost_reports(
        self,
        *,
        BillingPeriod: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: "ListBillingGroupCostReportsFilterTypeDef" = None
    ) -> ListBillingGroupCostReportsOutputTypeDef:
        """
        A paginated call to retrieve a summary report of actual Amazon Web Services
        charges and the calculated Amazon Web Services charges based on the associated
        pricing plan of a billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_billing_group_cost_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_billing_group_cost_reports)
        """
    def list_billing_groups(
        self,
        *,
        BillingPeriod: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: "ListBillingGroupsFilterTypeDef" = None
    ) -> ListBillingGroupsOutputTypeDef:
        """
        A paginated call to retrieve a list of billing groups for the given billing
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_billing_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_billing_groups)
        """
    def list_custom_line_item_versions(
        self,
        *,
        Arn: str,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: "ListCustomLineItemVersionsFilterTypeDef" = None
    ) -> ListCustomLineItemVersionsOutputTypeDef:
        """
        A paginated call to get a list of all custom line item versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_custom_line_item_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_custom_line_item_versions)
        """
    def list_custom_line_items(
        self,
        *,
        BillingPeriod: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: "ListCustomLineItemsFilterTypeDef" = None
    ) -> ListCustomLineItemsOutputTypeDef:
        """
        A paginated call to get a list of all custom line items (FFLIs) for the given
        billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_custom_line_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_custom_line_items)
        """
    def list_pricing_plans(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListPricingPlansFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPricingPlansOutputTypeDef:
        """
        A paginated call to get pricing plans for the given billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_pricing_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_pricing_plans)
        """
    def list_pricing_plans_associated_with_pricing_rule(
        self,
        *,
        PricingRuleArn: str,
        BillingPeriod: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPricingPlansAssociatedWithPricingRuleOutputTypeDef:
        """
        A list of the pricing plans that are associated with a pricing rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_pricing_plans_associated_with_pricing_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_pricing_plans_associated_with_pricing_rule)
        """
    def list_pricing_rules(
        self,
        *,
        BillingPeriod: str = None,
        Filters: "ListPricingRulesFilterTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPricingRulesOutputTypeDef:
        """
        Describes a pricing rule that can be associated to a pricing plan, or set of
        pricing plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_pricing_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_pricing_rules)
        """
    def list_pricing_rules_associated_to_pricing_plan(
        self,
        *,
        PricingPlanArn: str,
        BillingPeriod: str = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListPricingRulesAssociatedToPricingPlanOutputTypeDef:
        """
        Lists the pricing rules that are associated with a pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_pricing_rules_associated_to_pricing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_pricing_rules_associated_to_pricing_plan)
        """
    def list_resources_associated_to_custom_line_item(
        self,
        *,
        Arn: str,
        BillingPeriod: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: "ListResourcesAssociatedToCustomLineItemFilterTypeDef" = None
    ) -> ListResourcesAssociatedToCustomLineItemOutputTypeDef:
        """
        List the resources that are associated to a custom line item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_resources_associated_to_custom_line_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_resources_associated_to_custom_line_item)
        """
    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        A list the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified `resourceArn`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#tag_resource)
        """
    def untag_resource(self, *, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#untag_resource)
        """
    def update_billing_group(
        self,
        *,
        Arn: str,
        Name: str = None,
        Status: BillingGroupStatusType = None,
        ComputationPreference: "ComputationPreferenceTypeDef" = None,
        Description: str = None
    ) -> UpdateBillingGroupOutputTypeDef:
        """
        This updates an existing billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.update_billing_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#update_billing_group)
        """
    def update_custom_line_item(
        self,
        *,
        Arn: str,
        Name: str = None,
        Description: str = None,
        ChargeDetails: "UpdateCustomLineItemChargeDetailsTypeDef" = None,
        BillingPeriodRange: "CustomLineItemBillingPeriodRangeTypeDef" = None
    ) -> UpdateCustomLineItemOutputTypeDef:
        """
        Update an existing custom line item in the current or previous billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.update_custom_line_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#update_custom_line_item)
        """
    def update_pricing_plan(
        self, *, Arn: str, Name: str = None, Description: str = None
    ) -> UpdatePricingPlanOutputTypeDef:
        """
        This updates an existing pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.update_pricing_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#update_pricing_plan)
        """
    def update_pricing_rule(
        self,
        *,
        Arn: str,
        Name: str = None,
        Description: str = None,
        Type: PricingRuleTypeType = None,
        ModifierPercentage: float = None
    ) -> UpdatePricingRuleOutputTypeDef:
        """
        Updates an existing pricing rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Client.update_pricing_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client.html#update_pricing_rule)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_associations"]
    ) -> ListAccountAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListAccountAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listaccountassociationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_billing_group_cost_reports"]
    ) -> ListBillingGroupCostReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListBillingGroupCostReports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listbillinggroupcostreportspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_billing_groups"]
    ) -> ListBillingGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListBillingGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listbillinggroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_line_item_versions"]
    ) -> ListCustomLineItemVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListCustomLineItemVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listcustomlineitemversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_custom_line_items"]
    ) -> ListCustomLineItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListCustomLineItems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listcustomlineitemspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pricing_plans"]
    ) -> ListPricingPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingPlans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingplanspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pricing_plans_associated_with_pricing_rule"]
    ) -> ListPricingPlansAssociatedWithPricingRulePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingPlansAssociatedWithPricingRule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingplansassociatedwithpricingrulepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pricing_rules"]
    ) -> ListPricingRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingrulespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_pricing_rules_associated_to_pricing_plan"]
    ) -> ListPricingRulesAssociatedToPricingPlanPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListPricingRulesAssociatedToPricingPlan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listpricingrulesassociatedtopricingplanpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resources_associated_to_custom_line_item"]
    ) -> ListResourcesAssociatedToCustomLineItemPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.18/reference/services/billingconductor.html#BillingConductor.Paginator.ListResourcesAssociatedToCustomLineItem)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/paginators.html#listresourcesassociatedtocustomlineitempaginator)
        """
