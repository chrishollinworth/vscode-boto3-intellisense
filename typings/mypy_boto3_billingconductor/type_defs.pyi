"""
Type annotations for billingconductor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_billingconductor.type_defs import AccountAssociationsListElementTypeDef

    data: AccountAssociationsListElementTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

from .literals import (
    AssociateResourceErrorReasonType,
    BillingGroupStatusType,
    CurrencyCodeType,
    CustomLineItemRelationshipType,
    CustomLineItemTypeType,
    GroupByAttributeNameType,
    PricingRuleScopeType,
    PricingRuleTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountAssociationsListElementTypeDef",
    "AccountGroupingTypeDef",
    "AssociateAccountsInputRequestTypeDef",
    "AssociateAccountsOutputTypeDef",
    "AssociatePricingRulesInputRequestTypeDef",
    "AssociatePricingRulesOutputTypeDef",
    "AssociateResourceErrorTypeDef",
    "AssociateResourceResponseElementTypeDef",
    "AttributeTypeDef",
    "BatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    "BillingGroupCostReportElementTypeDef",
    "BillingGroupCostReportResultElementTypeDef",
    "BillingGroupListElementTypeDef",
    "BillingPeriodRangeTypeDef",
    "ComputationPreferenceTypeDef",
    "CreateBillingGroupInputRequestTypeDef",
    "CreateBillingGroupOutputTypeDef",
    "CreateCustomLineItemInputRequestTypeDef",
    "CreateCustomLineItemOutputTypeDef",
    "CreateFreeTierConfigTypeDef",
    "CreatePricingPlanInputRequestTypeDef",
    "CreatePricingPlanOutputTypeDef",
    "CreatePricingRuleInputRequestTypeDef",
    "CreatePricingRuleOutputTypeDef",
    "CreateTieringInputTypeDef",
    "CustomLineItemBillingPeriodRangeTypeDef",
    "CustomLineItemChargeDetailsTypeDef",
    "CustomLineItemFlatChargeDetailsTypeDef",
    "CustomLineItemListElementTypeDef",
    "CustomLineItemPercentageChargeDetailsTypeDef",
    "CustomLineItemVersionListElementTypeDef",
    "DeleteBillingGroupInputRequestTypeDef",
    "DeleteBillingGroupOutputTypeDef",
    "DeleteCustomLineItemInputRequestTypeDef",
    "DeleteCustomLineItemOutputTypeDef",
    "DeletePricingPlanInputRequestTypeDef",
    "DeletePricingPlanOutputTypeDef",
    "DeletePricingRuleInputRequestTypeDef",
    "DeletePricingRuleOutputTypeDef",
    "DisassociateAccountsInputRequestTypeDef",
    "DisassociateAccountsOutputTypeDef",
    "DisassociatePricingRulesInputRequestTypeDef",
    "DisassociatePricingRulesOutputTypeDef",
    "DisassociateResourceResponseElementTypeDef",
    "FreeTierConfigTypeDef",
    "GetBillingGroupCostReportInputRequestTypeDef",
    "GetBillingGroupCostReportOutputTypeDef",
    "LineItemFilterTypeDef",
    "ListAccountAssociationsFilterTypeDef",
    "ListAccountAssociationsInputRequestTypeDef",
    "ListAccountAssociationsOutputTypeDef",
    "ListBillingGroupAccountGroupingTypeDef",
    "ListBillingGroupCostReportsFilterTypeDef",
    "ListBillingGroupCostReportsInputRequestTypeDef",
    "ListBillingGroupCostReportsOutputTypeDef",
    "ListBillingGroupsFilterTypeDef",
    "ListBillingGroupsInputRequestTypeDef",
    "ListBillingGroupsOutputTypeDef",
    "ListCustomLineItemChargeDetailsTypeDef",
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    "ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef",
    "ListCustomLineItemVersionsFilterTypeDef",
    "ListCustomLineItemVersionsInputRequestTypeDef",
    "ListCustomLineItemVersionsOutputTypeDef",
    "ListCustomLineItemsFilterTypeDef",
    "ListCustomLineItemsInputRequestTypeDef",
    "ListCustomLineItemsOutputTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    "ListPricingPlansFilterTypeDef",
    "ListPricingPlansInputRequestTypeDef",
    "ListPricingPlansOutputTypeDef",
    "ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    "ListPricingRulesFilterTypeDef",
    "ListPricingRulesInputRequestTypeDef",
    "ListPricingRulesOutputTypeDef",
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    "ListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PricingPlanListElementTypeDef",
    "PricingRuleListElementTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TieringTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBillingGroupAccountGroupingTypeDef",
    "UpdateBillingGroupInputRequestTypeDef",
    "UpdateBillingGroupOutputTypeDef",
    "UpdateCustomLineItemChargeDetailsTypeDef",
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    "UpdateCustomLineItemInputRequestTypeDef",
    "UpdateCustomLineItemOutputTypeDef",
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    "UpdateFreeTierConfigTypeDef",
    "UpdatePricingPlanInputRequestTypeDef",
    "UpdatePricingPlanOutputTypeDef",
    "UpdatePricingRuleInputRequestTypeDef",
    "UpdatePricingRuleOutputTypeDef",
    "UpdateTieringInputTypeDef",
)

AccountAssociationsListElementTypeDef = TypedDict(
    "AccountAssociationsListElementTypeDef",
    {
        "AccountId": str,
        "BillingGroupArn": str,
        "AccountName": str,
        "AccountEmail": str,
    },
    total=False,
)

_RequiredAccountGroupingTypeDef = TypedDict(
    "_RequiredAccountGroupingTypeDef",
    {
        "LinkedAccountIds": List[str],
    },
)
_OptionalAccountGroupingTypeDef = TypedDict(
    "_OptionalAccountGroupingTypeDef",
    {
        "AutoAssociate": bool,
    },
    total=False,
)

class AccountGroupingTypeDef(_RequiredAccountGroupingTypeDef, _OptionalAccountGroupingTypeDef):
    pass

AssociateAccountsInputRequestTypeDef = TypedDict(
    "AssociateAccountsInputRequestTypeDef",
    {
        "Arn": str,
        "AccountIds": List[str],
    },
)

AssociateAccountsOutputTypeDef = TypedDict(
    "AssociateAccountsOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatePricingRulesInputRequestTypeDef = TypedDict(
    "AssociatePricingRulesInputRequestTypeDef",
    {
        "Arn": str,
        "PricingRuleArns": List[str],
    },
)

AssociatePricingRulesOutputTypeDef = TypedDict(
    "AssociatePricingRulesOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResourceErrorTypeDef = TypedDict(
    "AssociateResourceErrorTypeDef",
    {
        "Message": str,
        "Reason": AssociateResourceErrorReasonType,
    },
    total=False,
)

AssociateResourceResponseElementTypeDef = TypedDict(
    "AssociateResourceResponseElementTypeDef",
    {
        "Arn": str,
        "Error": "AssociateResourceErrorTypeDef",
    },
    total=False,
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredBatchAssociateResourcesToCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    {
        "TargetArn": str,
        "ResourceArns": List[str],
    },
)
_OptionalBatchAssociateResourcesToCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchAssociateResourcesToCustomLineItemInputRequestTypeDef",
    {
        "BillingPeriodRange": "CustomLineItemBillingPeriodRangeTypeDef",
    },
    total=False,
)

class BatchAssociateResourcesToCustomLineItemInputRequestTypeDef(
    _RequiredBatchAssociateResourcesToCustomLineItemInputRequestTypeDef,
    _OptionalBatchAssociateResourcesToCustomLineItemInputRequestTypeDef,
):
    pass

BatchAssociateResourcesToCustomLineItemOutputTypeDef = TypedDict(
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    {
        "SuccessfullyAssociatedResources": List["AssociateResourceResponseElementTypeDef"],
        "FailedAssociatedResources": List["AssociateResourceResponseElementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    {
        "TargetArn": str,
        "ResourceArns": List[str],
    },
)
_OptionalBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef",
    {
        "BillingPeriodRange": "CustomLineItemBillingPeriodRangeTypeDef",
    },
    total=False,
)

class BatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef(
    _RequiredBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef,
    _OptionalBatchDisassociateResourcesFromCustomLineItemInputRequestTypeDef,
):
    pass

BatchDisassociateResourcesFromCustomLineItemOutputTypeDef = TypedDict(
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    {
        "SuccessfullyDisassociatedResources": List["DisassociateResourceResponseElementTypeDef"],
        "FailedDisassociatedResources": List["DisassociateResourceResponseElementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BillingGroupCostReportElementTypeDef = TypedDict(
    "BillingGroupCostReportElementTypeDef",
    {
        "Arn": str,
        "AWSCost": str,
        "ProformaCost": str,
        "Margin": str,
        "MarginPercentage": str,
        "Currency": str,
    },
    total=False,
)

BillingGroupCostReportResultElementTypeDef = TypedDict(
    "BillingGroupCostReportResultElementTypeDef",
    {
        "Arn": str,
        "AWSCost": str,
        "ProformaCost": str,
        "Margin": str,
        "MarginPercentage": str,
        "Currency": str,
        "Attributes": List["AttributeTypeDef"],
    },
    total=False,
)

BillingGroupListElementTypeDef = TypedDict(
    "BillingGroupListElementTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "PrimaryAccountId": str,
        "ComputationPreference": "ComputationPreferenceTypeDef",
        "Size": int,
        "CreationTime": int,
        "LastModifiedTime": int,
        "Status": BillingGroupStatusType,
        "StatusReason": str,
        "AccountGrouping": "ListBillingGroupAccountGroupingTypeDef",
    },
    total=False,
)

BillingPeriodRangeTypeDef = TypedDict(
    "BillingPeriodRangeTypeDef",
    {
        "InclusiveStartBillingPeriod": str,
        "ExclusiveEndBillingPeriod": str,
    },
)

ComputationPreferenceTypeDef = TypedDict(
    "ComputationPreferenceTypeDef",
    {
        "PricingPlanArn": str,
    },
)

_RequiredCreateBillingGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateBillingGroupInputRequestTypeDef",
    {
        "Name": str,
        "AccountGrouping": "AccountGroupingTypeDef",
        "ComputationPreference": "ComputationPreferenceTypeDef",
    },
)
_OptionalCreateBillingGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateBillingGroupInputRequestTypeDef",
    {
        "ClientToken": str,
        "PrimaryAccountId": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateBillingGroupInputRequestTypeDef(
    _RequiredCreateBillingGroupInputRequestTypeDef, _OptionalCreateBillingGroupInputRequestTypeDef
):
    pass

CreateBillingGroupOutputTypeDef = TypedDict(
    "CreateBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredCreateCustomLineItemInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "BillingGroupArn": str,
        "ChargeDetails": "CustomLineItemChargeDetailsTypeDef",
    },
)
_OptionalCreateCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalCreateCustomLineItemInputRequestTypeDef",
    {
        "ClientToken": str,
        "BillingPeriodRange": "CustomLineItemBillingPeriodRangeTypeDef",
        "Tags": Dict[str, str],
        "AccountId": str,
    },
    total=False,
)

class CreateCustomLineItemInputRequestTypeDef(
    _RequiredCreateCustomLineItemInputRequestTypeDef,
    _OptionalCreateCustomLineItemInputRequestTypeDef,
):
    pass

CreateCustomLineItemOutputTypeDef = TypedDict(
    "CreateCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFreeTierConfigTypeDef = TypedDict(
    "CreateFreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)

_RequiredCreatePricingPlanInputRequestTypeDef = TypedDict(
    "_RequiredCreatePricingPlanInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatePricingPlanInputRequestTypeDef = TypedDict(
    "_OptionalCreatePricingPlanInputRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "PricingRuleArns": List[str],
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreatePricingPlanInputRequestTypeDef(
    _RequiredCreatePricingPlanInputRequestTypeDef, _OptionalCreatePricingPlanInputRequestTypeDef
):
    pass

CreatePricingPlanOutputTypeDef = TypedDict(
    "CreatePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePricingRuleInputRequestTypeDef = TypedDict(
    "_RequiredCreatePricingRuleInputRequestTypeDef",
    {
        "Name": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
    },
)
_OptionalCreatePricingRuleInputRequestTypeDef = TypedDict(
    "_OptionalCreatePricingRuleInputRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "ModifierPercentage": float,
        "Service": str,
        "Tags": Dict[str, str],
        "BillingEntity": str,
        "Tiering": "CreateTieringInputTypeDef",
        "UsageType": str,
        "Operation": str,
    },
    total=False,
)

class CreatePricingRuleInputRequestTypeDef(
    _RequiredCreatePricingRuleInputRequestTypeDef, _OptionalCreatePricingRuleInputRequestTypeDef
):
    pass

CreatePricingRuleOutputTypeDef = TypedDict(
    "CreatePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTieringInputTypeDef = TypedDict(
    "CreateTieringInputTypeDef",
    {
        "FreeTier": "CreateFreeTierConfigTypeDef",
    },
)

_RequiredCustomLineItemBillingPeriodRangeTypeDef = TypedDict(
    "_RequiredCustomLineItemBillingPeriodRangeTypeDef",
    {
        "InclusiveStartBillingPeriod": str,
    },
)
_OptionalCustomLineItemBillingPeriodRangeTypeDef = TypedDict(
    "_OptionalCustomLineItemBillingPeriodRangeTypeDef",
    {
        "ExclusiveEndBillingPeriod": str,
    },
    total=False,
)

class CustomLineItemBillingPeriodRangeTypeDef(
    _RequiredCustomLineItemBillingPeriodRangeTypeDef,
    _OptionalCustomLineItemBillingPeriodRangeTypeDef,
):
    pass

_RequiredCustomLineItemChargeDetailsTypeDef = TypedDict(
    "_RequiredCustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
    },
)
_OptionalCustomLineItemChargeDetailsTypeDef = TypedDict(
    "_OptionalCustomLineItemChargeDetailsTypeDef",
    {
        "Flat": "CustomLineItemFlatChargeDetailsTypeDef",
        "Percentage": "CustomLineItemPercentageChargeDetailsTypeDef",
        "LineItemFilters": List["LineItemFilterTypeDef"],
    },
    total=False,
)

class CustomLineItemChargeDetailsTypeDef(
    _RequiredCustomLineItemChargeDetailsTypeDef, _OptionalCustomLineItemChargeDetailsTypeDef
):
    pass

CustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "CustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

CustomLineItemListElementTypeDef = TypedDict(
    "CustomLineItemListElementTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ChargeDetails": "ListCustomLineItemChargeDetailsTypeDef",
        "CurrencyCode": CurrencyCodeType,
        "Description": str,
        "ProductCode": str,
        "BillingGroupArn": str,
        "CreationTime": int,
        "LastModifiedTime": int,
        "AssociationSize": int,
        "AccountId": str,
    },
    total=False,
)

_RequiredCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "_RequiredCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)
_OptionalCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "_OptionalCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "AssociatedValues": List[str],
    },
    total=False,
)

class CustomLineItemPercentageChargeDetailsTypeDef(
    _RequiredCustomLineItemPercentageChargeDetailsTypeDef,
    _OptionalCustomLineItemPercentageChargeDetailsTypeDef,
):
    pass

CustomLineItemVersionListElementTypeDef = TypedDict(
    "CustomLineItemVersionListElementTypeDef",
    {
        "Name": str,
        "ChargeDetails": "ListCustomLineItemChargeDetailsTypeDef",
        "CurrencyCode": CurrencyCodeType,
        "Description": str,
        "ProductCode": str,
        "BillingGroupArn": str,
        "CreationTime": int,
        "LastModifiedTime": int,
        "AssociationSize": int,
        "StartBillingPeriod": str,
        "EndBillingPeriod": str,
        "Arn": str,
        "StartTime": int,
        "AccountId": str,
    },
    total=False,
)

DeleteBillingGroupInputRequestTypeDef = TypedDict(
    "DeleteBillingGroupInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteBillingGroupOutputTypeDef = TypedDict(
    "DeleteBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredDeleteCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalDeleteCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalDeleteCustomLineItemInputRequestTypeDef",
    {
        "BillingPeriodRange": "CustomLineItemBillingPeriodRangeTypeDef",
    },
    total=False,
)

class DeleteCustomLineItemInputRequestTypeDef(
    _RequiredDeleteCustomLineItemInputRequestTypeDef,
    _OptionalDeleteCustomLineItemInputRequestTypeDef,
):
    pass

DeleteCustomLineItemOutputTypeDef = TypedDict(
    "DeleteCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePricingPlanInputRequestTypeDef = TypedDict(
    "DeletePricingPlanInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeletePricingPlanOutputTypeDef = TypedDict(
    "DeletePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePricingRuleInputRequestTypeDef = TypedDict(
    "DeletePricingRuleInputRequestTypeDef",
    {
        "Arn": str,
    },
)

DeletePricingRuleOutputTypeDef = TypedDict(
    "DeletePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAccountsInputRequestTypeDef = TypedDict(
    "DisassociateAccountsInputRequestTypeDef",
    {
        "Arn": str,
        "AccountIds": List[str],
    },
)

DisassociateAccountsOutputTypeDef = TypedDict(
    "DisassociateAccountsOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePricingRulesInputRequestTypeDef = TypedDict(
    "DisassociatePricingRulesInputRequestTypeDef",
    {
        "Arn": str,
        "PricingRuleArns": List[str],
    },
)

DisassociatePricingRulesOutputTypeDef = TypedDict(
    "DisassociatePricingRulesOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResourceResponseElementTypeDef = TypedDict(
    "DisassociateResourceResponseElementTypeDef",
    {
        "Arn": str,
        "Error": "AssociateResourceErrorTypeDef",
    },
    total=False,
)

FreeTierConfigTypeDef = TypedDict(
    "FreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)

_RequiredGetBillingGroupCostReportInputRequestTypeDef = TypedDict(
    "_RequiredGetBillingGroupCostReportInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalGetBillingGroupCostReportInputRequestTypeDef = TypedDict(
    "_OptionalGetBillingGroupCostReportInputRequestTypeDef",
    {
        "BillingPeriodRange": "BillingPeriodRangeTypeDef",
        "GroupBy": List[GroupByAttributeNameType],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetBillingGroupCostReportInputRequestTypeDef(
    _RequiredGetBillingGroupCostReportInputRequestTypeDef,
    _OptionalGetBillingGroupCostReportInputRequestTypeDef,
):
    pass

GetBillingGroupCostReportOutputTypeDef = TypedDict(
    "GetBillingGroupCostReportOutputTypeDef",
    {
        "BillingGroupCostReportResults": List["BillingGroupCostReportResultElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LineItemFilterTypeDef = TypedDict(
    "LineItemFilterTypeDef",
    {
        "Attribute": Literal["LINE_ITEM_TYPE"],
        "MatchOption": Literal["NOT_EQUAL"],
        "Values": List[Literal["SAVINGS_PLAN_NEGATION"]],
    },
)

ListAccountAssociationsFilterTypeDef = TypedDict(
    "ListAccountAssociationsFilterTypeDef",
    {
        "Association": str,
        "AccountId": str,
        "AccountIds": List[str],
    },
    total=False,
)

ListAccountAssociationsInputRequestTypeDef = TypedDict(
    "ListAccountAssociationsInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "Filters": "ListAccountAssociationsFilterTypeDef",
        "NextToken": str,
    },
    total=False,
)

ListAccountAssociationsOutputTypeDef = TypedDict(
    "ListAccountAssociationsOutputTypeDef",
    {
        "LinkedAccounts": List["AccountAssociationsListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBillingGroupAccountGroupingTypeDef = TypedDict(
    "ListBillingGroupAccountGroupingTypeDef",
    {
        "AutoAssociate": bool,
    },
    total=False,
)

ListBillingGroupCostReportsFilterTypeDef = TypedDict(
    "ListBillingGroupCostReportsFilterTypeDef",
    {
        "BillingGroupArns": List[str],
    },
    total=False,
)

ListBillingGroupCostReportsInputRequestTypeDef = TypedDict(
    "ListBillingGroupCostReportsInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": "ListBillingGroupCostReportsFilterTypeDef",
    },
    total=False,
)

ListBillingGroupCostReportsOutputTypeDef = TypedDict(
    "ListBillingGroupCostReportsOutputTypeDef",
    {
        "BillingGroupCostReports": List["BillingGroupCostReportElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBillingGroupsFilterTypeDef = TypedDict(
    "ListBillingGroupsFilterTypeDef",
    {
        "Arns": List[str],
        "PricingPlan": str,
        "Statuses": List[BillingGroupStatusType],
        "AutoAssociate": bool,
    },
    total=False,
)

ListBillingGroupsInputRequestTypeDef = TypedDict(
    "ListBillingGroupsInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": "ListBillingGroupsFilterTypeDef",
    },
    total=False,
)

ListBillingGroupsOutputTypeDef = TypedDict(
    "ListBillingGroupsOutputTypeDef",
    {
        "BillingGroups": List["BillingGroupListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListCustomLineItemChargeDetailsTypeDef = TypedDict(
    "_RequiredListCustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
    },
)
_OptionalListCustomLineItemChargeDetailsTypeDef = TypedDict(
    "_OptionalListCustomLineItemChargeDetailsTypeDef",
    {
        "Flat": "ListCustomLineItemFlatChargeDetailsTypeDef",
        "Percentage": "ListCustomLineItemPercentageChargeDetailsTypeDef",
        "LineItemFilters": List["LineItemFilterTypeDef"],
    },
    total=False,
)

class ListCustomLineItemChargeDetailsTypeDef(
    _RequiredListCustomLineItemChargeDetailsTypeDef, _OptionalListCustomLineItemChargeDetailsTypeDef
):
    pass

ListCustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

ListCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)

ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef = TypedDict(
    "ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef",
    {
        "StartBillingPeriod": str,
        "EndBillingPeriod": str,
    },
    total=False,
)

ListCustomLineItemVersionsFilterTypeDef = TypedDict(
    "ListCustomLineItemVersionsFilterTypeDef",
    {
        "BillingPeriodRange": "ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef",
    },
    total=False,
)

_RequiredListCustomLineItemVersionsInputRequestTypeDef = TypedDict(
    "_RequiredListCustomLineItemVersionsInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListCustomLineItemVersionsInputRequestTypeDef = TypedDict(
    "_OptionalListCustomLineItemVersionsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": "ListCustomLineItemVersionsFilterTypeDef",
    },
    total=False,
)

class ListCustomLineItemVersionsInputRequestTypeDef(
    _RequiredListCustomLineItemVersionsInputRequestTypeDef,
    _OptionalListCustomLineItemVersionsInputRequestTypeDef,
):
    pass

ListCustomLineItemVersionsOutputTypeDef = TypedDict(
    "ListCustomLineItemVersionsOutputTypeDef",
    {
        "CustomLineItemVersions": List["CustomLineItemVersionListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomLineItemsFilterTypeDef = TypedDict(
    "ListCustomLineItemsFilterTypeDef",
    {
        "Names": List[str],
        "BillingGroups": List[str],
        "Arns": List[str],
        "AccountIds": List[str],
    },
    total=False,
)

ListCustomLineItemsInputRequestTypeDef = TypedDict(
    "ListCustomLineItemsInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": "ListCustomLineItemsFilterTypeDef",
    },
    total=False,
)

ListCustomLineItemsOutputTypeDef = TypedDict(
    "ListCustomLineItemsOutputTypeDef",
    {
        "CustomLineItems": List["CustomLineItemListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef = TypedDict(
    "_RequiredListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    {
        "PricingRuleArn": str,
    },
)
_OptionalListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef = TypedDict(
    "_OptionalListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef(
    _RequiredListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef,
    _OptionalListPricingPlansAssociatedWithPricingRuleInputRequestTypeDef,
):
    pass

ListPricingPlansAssociatedWithPricingRuleOutputTypeDef = TypedDict(
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingRuleArn": str,
        "PricingPlanArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPricingPlansFilterTypeDef = TypedDict(
    "ListPricingPlansFilterTypeDef",
    {
        "Arns": List[str],
    },
    total=False,
)

ListPricingPlansInputRequestTypeDef = TypedDict(
    "ListPricingPlansInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "Filters": "ListPricingPlansFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPricingPlansOutputTypeDef = TypedDict(
    "ListPricingPlansOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingPlans": List["PricingPlanListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPricingRulesAssociatedToPricingPlanInputRequestTypeDef = TypedDict(
    "_RequiredListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    {
        "PricingPlanArn": str,
    },
)
_OptionalListPricingRulesAssociatedToPricingPlanInputRequestTypeDef = TypedDict(
    "_OptionalListPricingRulesAssociatedToPricingPlanInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListPricingRulesAssociatedToPricingPlanInputRequestTypeDef(
    _RequiredListPricingRulesAssociatedToPricingPlanInputRequestTypeDef,
    _OptionalListPricingRulesAssociatedToPricingPlanInputRequestTypeDef,
):
    pass

ListPricingRulesAssociatedToPricingPlanOutputTypeDef = TypedDict(
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingPlanArn": str,
        "PricingRuleArns": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPricingRulesFilterTypeDef = TypedDict(
    "ListPricingRulesFilterTypeDef",
    {
        "Arns": List[str],
    },
    total=False,
)

ListPricingRulesInputRequestTypeDef = TypedDict(
    "ListPricingRulesInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "Filters": "ListPricingRulesFilterTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListPricingRulesOutputTypeDef = TypedDict(
    "ListPricingRulesOutputTypeDef",
    {
        "BillingPeriod": str,
        "PricingRules": List["PricingRuleListElementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesAssociatedToCustomLineItemFilterTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    {
        "Relationship": CustomLineItemRelationshipType,
    },
    total=False,
)

_RequiredListResourcesAssociatedToCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalListResourcesAssociatedToCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalListResourcesAssociatedToCustomLineItemInputRequestTypeDef",
    {
        "BillingPeriod": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    },
    total=False,
)

class ListResourcesAssociatedToCustomLineItemInputRequestTypeDef(
    _RequiredListResourcesAssociatedToCustomLineItemInputRequestTypeDef,
    _OptionalListResourcesAssociatedToCustomLineItemInputRequestTypeDef,
):
    pass

ListResourcesAssociatedToCustomLineItemOutputTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "AssociatedResources": List[
            "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesAssociatedToCustomLineItemResponseElementTypeDef = TypedDict(
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    {
        "Arn": str,
        "Relationship": CustomLineItemRelationshipType,
        "EndBillingPeriod": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PricingPlanListElementTypeDef = TypedDict(
    "PricingPlanListElementTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "Size": int,
        "CreationTime": int,
        "LastModifiedTime": int,
    },
    total=False,
)

PricingRuleListElementTypeDef = TypedDict(
    "PricingRuleListElementTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "Service": str,
        "AssociatedPricingPlanCount": int,
        "CreationTime": int,
        "LastModifiedTime": int,
        "BillingEntity": str,
        "Tiering": "TieringTypeDef",
        "UsageType": str,
        "Operation": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TieringTypeDef = TypedDict(
    "TieringTypeDef",
    {
        "FreeTier": "FreeTierConfigTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateBillingGroupAccountGroupingTypeDef = TypedDict(
    "UpdateBillingGroupAccountGroupingTypeDef",
    {
        "AutoAssociate": bool,
    },
    total=False,
)

_RequiredUpdateBillingGroupInputRequestTypeDef = TypedDict(
    "_RequiredUpdateBillingGroupInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdateBillingGroupInputRequestTypeDef = TypedDict(
    "_OptionalUpdateBillingGroupInputRequestTypeDef",
    {
        "Name": str,
        "Status": BillingGroupStatusType,
        "ComputationPreference": "ComputationPreferenceTypeDef",
        "Description": str,
        "AccountGrouping": "UpdateBillingGroupAccountGroupingTypeDef",
    },
    total=False,
)

class UpdateBillingGroupInputRequestTypeDef(
    _RequiredUpdateBillingGroupInputRequestTypeDef, _OptionalUpdateBillingGroupInputRequestTypeDef
):
    pass

UpdateBillingGroupOutputTypeDef = TypedDict(
    "UpdateBillingGroupOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "PrimaryAccountId": str,
        "PricingPlanArn": str,
        "Size": int,
        "LastModifiedTime": int,
        "Status": BillingGroupStatusType,
        "StatusReason": str,
        "AccountGrouping": "UpdateBillingGroupAccountGroupingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomLineItemChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemChargeDetailsTypeDef",
    {
        "Flat": "UpdateCustomLineItemFlatChargeDetailsTypeDef",
        "Percentage": "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
        "LineItemFilters": List["LineItemFilterTypeDef"],
    },
    total=False,
)

UpdateCustomLineItemFlatChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    {
        "ChargeValue": float,
    },
)

_RequiredUpdateCustomLineItemInputRequestTypeDef = TypedDict(
    "_RequiredUpdateCustomLineItemInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdateCustomLineItemInputRequestTypeDef = TypedDict(
    "_OptionalUpdateCustomLineItemInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "ChargeDetails": "UpdateCustomLineItemChargeDetailsTypeDef",
        "BillingPeriodRange": "CustomLineItemBillingPeriodRangeTypeDef",
    },
    total=False,
)

class UpdateCustomLineItemInputRequestTypeDef(
    _RequiredUpdateCustomLineItemInputRequestTypeDef,
    _OptionalUpdateCustomLineItemInputRequestTypeDef,
):
    pass

UpdateCustomLineItemOutputTypeDef = TypedDict(
    "UpdateCustomLineItemOutputTypeDef",
    {
        "Arn": str,
        "BillingGroupArn": str,
        "Name": str,
        "Description": str,
        "ChargeDetails": "ListCustomLineItemChargeDetailsTypeDef",
        "LastModifiedTime": int,
        "AssociationSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomLineItemPercentageChargeDetailsTypeDef = TypedDict(
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    {
        "PercentageValue": float,
    },
)

UpdateFreeTierConfigTypeDef = TypedDict(
    "UpdateFreeTierConfigTypeDef",
    {
        "Activated": bool,
    },
)

_RequiredUpdatePricingPlanInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePricingPlanInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdatePricingPlanInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePricingPlanInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
    },
    total=False,
)

class UpdatePricingPlanInputRequestTypeDef(
    _RequiredUpdatePricingPlanInputRequestTypeDef, _OptionalUpdatePricingPlanInputRequestTypeDef
):
    pass

UpdatePricingPlanOutputTypeDef = TypedDict(
    "UpdatePricingPlanOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Size": int,
        "LastModifiedTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePricingRuleInputRequestTypeDef = TypedDict(
    "_RequiredUpdatePricingRuleInputRequestTypeDef",
    {
        "Arn": str,
    },
)
_OptionalUpdatePricingRuleInputRequestTypeDef = TypedDict(
    "_OptionalUpdatePricingRuleInputRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "Tiering": "UpdateTieringInputTypeDef",
    },
    total=False,
)

class UpdatePricingRuleInputRequestTypeDef(
    _RequiredUpdatePricingRuleInputRequestTypeDef, _OptionalUpdatePricingRuleInputRequestTypeDef
):
    pass

UpdatePricingRuleOutputTypeDef = TypedDict(
    "UpdatePricingRuleOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Description": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ModifierPercentage": float,
        "Service": str,
        "AssociatedPricingPlanCount": int,
        "LastModifiedTime": int,
        "BillingEntity": str,
        "Tiering": "UpdateTieringInputTypeDef",
        "UsageType": str,
        "Operation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTieringInputTypeDef = TypedDict(
    "UpdateTieringInputTypeDef",
    {
        "FreeTier": "UpdateFreeTierConfigTypeDef",
    },
)
