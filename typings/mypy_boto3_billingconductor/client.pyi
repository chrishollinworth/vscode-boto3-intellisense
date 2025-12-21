"""
Type annotations for billingconductor service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_billingconductor.client import BillingConductorClient

    session = Session()
    client: BillingConductorClient = session.client("billingconductor")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    AssociateAccountsInputTypeDef,
    AssociateAccountsOutputTypeDef,
    AssociatePricingRulesInputTypeDef,
    AssociatePricingRulesOutputTypeDef,
    BatchAssociateResourcesToCustomLineItemInputTypeDef,
    BatchAssociateResourcesToCustomLineItemOutputTypeDef,
    BatchDisassociateResourcesFromCustomLineItemInputTypeDef,
    BatchDisassociateResourcesFromCustomLineItemOutputTypeDef,
    CreateBillingGroupInputTypeDef,
    CreateBillingGroupOutputTypeDef,
    CreateCustomLineItemInputTypeDef,
    CreateCustomLineItemOutputTypeDef,
    CreatePricingPlanInputTypeDef,
    CreatePricingPlanOutputTypeDef,
    CreatePricingRuleInputTypeDef,
    CreatePricingRuleOutputTypeDef,
    DeleteBillingGroupInputTypeDef,
    DeleteBillingGroupOutputTypeDef,
    DeleteCustomLineItemInputTypeDef,
    DeleteCustomLineItemOutputTypeDef,
    DeletePricingPlanInputTypeDef,
    DeletePricingPlanOutputTypeDef,
    DeletePricingRuleInputTypeDef,
    DeletePricingRuleOutputTypeDef,
    DisassociateAccountsInputTypeDef,
    DisassociateAccountsOutputTypeDef,
    DisassociatePricingRulesInputTypeDef,
    DisassociatePricingRulesOutputTypeDef,
    GetBillingGroupCostReportInputTypeDef,
    GetBillingGroupCostReportOutputTypeDef,
    ListAccountAssociationsInputTypeDef,
    ListAccountAssociationsOutputTypeDef,
    ListBillingGroupCostReportsInputTypeDef,
    ListBillingGroupCostReportsOutputTypeDef,
    ListBillingGroupsInputTypeDef,
    ListBillingGroupsOutputTypeDef,
    ListCustomLineItemsInputTypeDef,
    ListCustomLineItemsOutputTypeDef,
    ListCustomLineItemVersionsInputTypeDef,
    ListCustomLineItemVersionsOutputTypeDef,
    ListPricingPlansAssociatedWithPricingRuleInputTypeDef,
    ListPricingPlansAssociatedWithPricingRuleOutputTypeDef,
    ListPricingPlansInputTypeDef,
    ListPricingPlansOutputTypeDef,
    ListPricingRulesAssociatedToPricingPlanInputTypeDef,
    ListPricingRulesAssociatedToPricingPlanOutputTypeDef,
    ListPricingRulesInputTypeDef,
    ListPricingRulesOutputTypeDef,
    ListResourcesAssociatedToCustomLineItemInputTypeDef,
    ListResourcesAssociatedToCustomLineItemOutputTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateBillingGroupInputTypeDef,
    UpdateBillingGroupOutputTypeDef,
    UpdateCustomLineItemInputTypeDef,
    UpdateCustomLineItemOutputTypeDef,
    UpdatePricingPlanInputTypeDef,
    UpdatePricingPlanOutputTypeDef,
    UpdatePricingRuleInputTypeDef,
    UpdatePricingRuleOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("BillingConductorClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor.html#BillingConductor.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BillingConductorClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor.html#BillingConductor.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#generate_presigned_url)
        """

    def associate_accounts(
        self, **kwargs: Unpack[AssociateAccountsInputTypeDef]
    ) -> AssociateAccountsOutputTypeDef:
        """
        Connects an array of account IDs in a consolidated billing family to a
        predefined billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/associate_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#associate_accounts)
        """

    def associate_pricing_rules(
        self, **kwargs: Unpack[AssociatePricingRulesInputTypeDef]
    ) -> AssociatePricingRulesOutputTypeDef:
        """
        Connects an array of <code>PricingRuleArns</code> to a defined
        <code>PricingPlan</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/associate_pricing_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#associate_pricing_rules)
        """

    def batch_associate_resources_to_custom_line_item(
        self, **kwargs: Unpack[BatchAssociateResourcesToCustomLineItemInputTypeDef]
    ) -> BatchAssociateResourcesToCustomLineItemOutputTypeDef:
        """
        Associates a batch of resources to a percentage custom line item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/batch_associate_resources_to_custom_line_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#batch_associate_resources_to_custom_line_item)
        """

    def batch_disassociate_resources_from_custom_line_item(
        self, **kwargs: Unpack[BatchDisassociateResourcesFromCustomLineItemInputTypeDef]
    ) -> BatchDisassociateResourcesFromCustomLineItemOutputTypeDef:
        """
        Disassociates a batch of resources from a percentage custom line item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/batch_disassociate_resources_from_custom_line_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#batch_disassociate_resources_from_custom_line_item)
        """

    def create_billing_group(
        self, **kwargs: Unpack[CreateBillingGroupInputTypeDef]
    ) -> CreateBillingGroupOutputTypeDef:
        """
        Creates a billing group that resembles a consolidated billing family that
        Amazon Web Services charges, based off of the predefined pricing plan
        computation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/create_billing_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#create_billing_group)
        """

    def create_custom_line_item(
        self, **kwargs: Unpack[CreateCustomLineItemInputTypeDef]
    ) -> CreateCustomLineItemOutputTypeDef:
        """
        Creates a custom line item that can be used to create a one-time fixed charge
        that can be applied to a single billing group for the current or previous
        billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/create_custom_line_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#create_custom_line_item)
        """

    def create_pricing_plan(
        self, **kwargs: Unpack[CreatePricingPlanInputTypeDef]
    ) -> CreatePricingPlanOutputTypeDef:
        """
        Creates a pricing plan that is used for computing Amazon Web Services charges
        for billing groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/create_pricing_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#create_pricing_plan)
        """

    def create_pricing_rule(
        self, **kwargs: Unpack[CreatePricingRuleInputTypeDef]
    ) -> CreatePricingRuleOutputTypeDef:
        """
        Creates a pricing rule can be associated to a pricing plan, or a set of pricing
        plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/create_pricing_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#create_pricing_rule)
        """

    def delete_billing_group(
        self, **kwargs: Unpack[DeleteBillingGroupInputTypeDef]
    ) -> DeleteBillingGroupOutputTypeDef:
        """
        Deletes a billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/delete_billing_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#delete_billing_group)
        """

    def delete_custom_line_item(
        self, **kwargs: Unpack[DeleteCustomLineItemInputTypeDef]
    ) -> DeleteCustomLineItemOutputTypeDef:
        """
        Deletes the custom line item identified by the given ARN in the current, or
        previous billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/delete_custom_line_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#delete_custom_line_item)
        """

    def delete_pricing_plan(
        self, **kwargs: Unpack[DeletePricingPlanInputTypeDef]
    ) -> DeletePricingPlanOutputTypeDef:
        """
        Deletes a pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/delete_pricing_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#delete_pricing_plan)
        """

    def delete_pricing_rule(
        self, **kwargs: Unpack[DeletePricingRuleInputTypeDef]
    ) -> DeletePricingRuleOutputTypeDef:
        """
        Deletes the pricing rule that's identified by the input Amazon Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/delete_pricing_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#delete_pricing_rule)
        """

    def disassociate_accounts(
        self, **kwargs: Unpack[DisassociateAccountsInputTypeDef]
    ) -> DisassociateAccountsOutputTypeDef:
        """
        Removes the specified list of account IDs from the given billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/disassociate_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#disassociate_accounts)
        """

    def disassociate_pricing_rules(
        self, **kwargs: Unpack[DisassociatePricingRulesInputTypeDef]
    ) -> DisassociatePricingRulesOutputTypeDef:
        """
        Disassociates a list of pricing rules from a pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/disassociate_pricing_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#disassociate_pricing_rules)
        """

    def get_billing_group_cost_report(
        self, **kwargs: Unpack[GetBillingGroupCostReportInputTypeDef]
    ) -> GetBillingGroupCostReportOutputTypeDef:
        """
        Retrieves the margin summary report, which includes the Amazon Web Services
        cost and charged amount (pro forma cost) by Amazon Web Services service for a
        specific billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_billing_group_cost_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_billing_group_cost_report)
        """

    def list_account_associations(
        self, **kwargs: Unpack[ListAccountAssociationsInputTypeDef]
    ) -> ListAccountAssociationsOutputTypeDef:
        """
        This is a paginated call to list linked accounts that are linked to the payer
        account for the specified time period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_account_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_account_associations)
        """

    def list_billing_group_cost_reports(
        self, **kwargs: Unpack[ListBillingGroupCostReportsInputTypeDef]
    ) -> ListBillingGroupCostReportsOutputTypeDef:
        """
        A paginated call to retrieve a summary report of actual Amazon Web Services
        charges and the calculated Amazon Web Services charges based on the associated
        pricing plan of a billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_billing_group_cost_reports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_billing_group_cost_reports)
        """

    def list_billing_groups(
        self, **kwargs: Unpack[ListBillingGroupsInputTypeDef]
    ) -> ListBillingGroupsOutputTypeDef:
        """
        A paginated call to retrieve a list of billing groups for the given billing
        period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_billing_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_billing_groups)
        """

    def list_custom_line_item_versions(
        self, **kwargs: Unpack[ListCustomLineItemVersionsInputTypeDef]
    ) -> ListCustomLineItemVersionsOutputTypeDef:
        """
        A paginated call to get a list of all custom line item versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_custom_line_item_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_custom_line_item_versions)
        """

    def list_custom_line_items(
        self, **kwargs: Unpack[ListCustomLineItemsInputTypeDef]
    ) -> ListCustomLineItemsOutputTypeDef:
        """
        A paginated call to get a list of all custom line items (FFLIs) for the given
        billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_custom_line_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_custom_line_items)
        """

    def list_pricing_plans(
        self, **kwargs: Unpack[ListPricingPlansInputTypeDef]
    ) -> ListPricingPlansOutputTypeDef:
        """
        A paginated call to get pricing plans for the given billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_pricing_plans.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_pricing_plans)
        """

    def list_pricing_plans_associated_with_pricing_rule(
        self, **kwargs: Unpack[ListPricingPlansAssociatedWithPricingRuleInputTypeDef]
    ) -> ListPricingPlansAssociatedWithPricingRuleOutputTypeDef:
        """
        A list of the pricing plans that are associated with a pricing rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_pricing_plans_associated_with_pricing_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_pricing_plans_associated_with_pricing_rule)
        """

    def list_pricing_rules(
        self, **kwargs: Unpack[ListPricingRulesInputTypeDef]
    ) -> ListPricingRulesOutputTypeDef:
        """
        Describes a pricing rule that can be associated to a pricing plan, or set of
        pricing plans.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_pricing_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_pricing_rules)
        """

    def list_pricing_rules_associated_to_pricing_plan(
        self, **kwargs: Unpack[ListPricingRulesAssociatedToPricingPlanInputTypeDef]
    ) -> ListPricingRulesAssociatedToPricingPlanOutputTypeDef:
        """
        Lists the pricing rules that are associated with a pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_pricing_rules_associated_to_pricing_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_pricing_rules_associated_to_pricing_plan)
        """

    def list_resources_associated_to_custom_line_item(
        self, **kwargs: Unpack[ListResourcesAssociatedToCustomLineItemInputTypeDef]
    ) -> ListResourcesAssociatedToCustomLineItemOutputTypeDef:
        """
        List the resources that are associated to a custom line item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_resources_associated_to_custom_line_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_resources_associated_to_custom_line_item)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        A list the tags for a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#list_tags_for_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified
        <code>resourceArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#untag_resource)
        """

    def update_billing_group(
        self, **kwargs: Unpack[UpdateBillingGroupInputTypeDef]
    ) -> UpdateBillingGroupOutputTypeDef:
        """
        This updates an existing billing group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/update_billing_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#update_billing_group)
        """

    def update_custom_line_item(
        self, **kwargs: Unpack[UpdateCustomLineItemInputTypeDef]
    ) -> UpdateCustomLineItemOutputTypeDef:
        """
        Update an existing custom line item in the current or previous billing period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/update_custom_line_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#update_custom_line_item)
        """

    def update_pricing_plan(
        self, **kwargs: Unpack[UpdatePricingPlanInputTypeDef]
    ) -> UpdatePricingPlanOutputTypeDef:
        """
        This updates an existing pricing plan.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/update_pricing_plan.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#update_pricing_plan)
        """

    def update_pricing_rule(
        self, **kwargs: Unpack[UpdatePricingRuleInputTypeDef]
    ) -> UpdatePricingRuleOutputTypeDef:
        """
        Updates an existing pricing rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/update_pricing_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#update_pricing_rule)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_account_associations"]
    ) -> ListAccountAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_billing_group_cost_reports"]
    ) -> ListBillingGroupCostReportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_billing_groups"]
    ) -> ListBillingGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_custom_line_item_versions"]
    ) -> ListCustomLineItemVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_custom_line_items"]
    ) -> ListCustomLineItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pricing_plans_associated_with_pricing_rule"]
    ) -> ListPricingPlansAssociatedWithPricingRulePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pricing_plans"]
    ) -> ListPricingPlansPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pricing_rules_associated_to_pricing_plan"]
    ) -> ListPricingRulesAssociatedToPricingPlanPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pricing_rules"]
    ) -> ListPricingRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resources_associated_to_custom_line_item"]
    ) -> ListResourcesAssociatedToCustomLineItemPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/billingconductor/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/client/#get_paginator)
        """
