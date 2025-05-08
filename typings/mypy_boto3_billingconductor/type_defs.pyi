"""
Type annotations for billingconductor service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_billingconductor/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_billingconductor.type_defs import AccountAssociationsListElementTypeDef

    data: AccountAssociationsListElementTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountAssociationsListElementTypeDef",
    "AccountGroupingTypeDef",
    "AssociateAccountsInputTypeDef",
    "AssociateAccountsOutputTypeDef",
    "AssociatePricingRulesInputTypeDef",
    "AssociatePricingRulesOutputTypeDef",
    "AssociateResourceErrorTypeDef",
    "AssociateResourceResponseElementTypeDef",
    "AttributeTypeDef",
    "BatchAssociateResourcesToCustomLineItemInputTypeDef",
    "BatchAssociateResourcesToCustomLineItemOutputTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemInputTypeDef",
    "BatchDisassociateResourcesFromCustomLineItemOutputTypeDef",
    "BillingGroupCostReportElementTypeDef",
    "BillingGroupCostReportResultElementTypeDef",
    "BillingGroupListElementTypeDef",
    "BillingPeriodRangeTypeDef",
    "ComputationPreferenceTypeDef",
    "CreateBillingGroupInputTypeDef",
    "CreateBillingGroupOutputTypeDef",
    "CreateCustomLineItemInputTypeDef",
    "CreateCustomLineItemOutputTypeDef",
    "CreateFreeTierConfigTypeDef",
    "CreatePricingPlanInputTypeDef",
    "CreatePricingPlanOutputTypeDef",
    "CreatePricingRuleInputTypeDef",
    "CreatePricingRuleOutputTypeDef",
    "CreateTieringInputTypeDef",
    "CustomLineItemBillingPeriodRangeTypeDef",
    "CustomLineItemChargeDetailsTypeDef",
    "CustomLineItemFlatChargeDetailsTypeDef",
    "CustomLineItemListElementTypeDef",
    "CustomLineItemPercentageChargeDetailsTypeDef",
    "CustomLineItemVersionListElementTypeDef",
    "DeleteBillingGroupInputTypeDef",
    "DeleteBillingGroupOutputTypeDef",
    "DeleteCustomLineItemInputTypeDef",
    "DeleteCustomLineItemOutputTypeDef",
    "DeletePricingPlanInputTypeDef",
    "DeletePricingPlanOutputTypeDef",
    "DeletePricingRuleInputTypeDef",
    "DeletePricingRuleOutputTypeDef",
    "DisassociateAccountsInputTypeDef",
    "DisassociateAccountsOutputTypeDef",
    "DisassociatePricingRulesInputTypeDef",
    "DisassociatePricingRulesOutputTypeDef",
    "DisassociateResourceResponseElementTypeDef",
    "FreeTierConfigTypeDef",
    "GetBillingGroupCostReportInputTypeDef",
    "GetBillingGroupCostReportOutputTypeDef",
    "LineItemFilterOutputTypeDef",
    "LineItemFilterTypeDef",
    "LineItemFilterUnionTypeDef",
    "ListAccountAssociationsFilterTypeDef",
    "ListAccountAssociationsInputPaginateTypeDef",
    "ListAccountAssociationsInputTypeDef",
    "ListAccountAssociationsOutputTypeDef",
    "ListBillingGroupAccountGroupingTypeDef",
    "ListBillingGroupCostReportsFilterTypeDef",
    "ListBillingGroupCostReportsInputPaginateTypeDef",
    "ListBillingGroupCostReportsInputTypeDef",
    "ListBillingGroupCostReportsOutputTypeDef",
    "ListBillingGroupsFilterTypeDef",
    "ListBillingGroupsInputPaginateTypeDef",
    "ListBillingGroupsInputTypeDef",
    "ListBillingGroupsOutputTypeDef",
    "ListCustomLineItemChargeDetailsTypeDef",
    "ListCustomLineItemFlatChargeDetailsTypeDef",
    "ListCustomLineItemPercentageChargeDetailsTypeDef",
    "ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef",
    "ListCustomLineItemVersionsFilterTypeDef",
    "ListCustomLineItemVersionsInputPaginateTypeDef",
    "ListCustomLineItemVersionsInputTypeDef",
    "ListCustomLineItemVersionsOutputTypeDef",
    "ListCustomLineItemsFilterTypeDef",
    "ListCustomLineItemsInputPaginateTypeDef",
    "ListCustomLineItemsInputTypeDef",
    "ListCustomLineItemsOutputTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleInputTypeDef",
    "ListPricingPlansAssociatedWithPricingRuleOutputTypeDef",
    "ListPricingPlansFilterTypeDef",
    "ListPricingPlansInputPaginateTypeDef",
    "ListPricingPlansInputTypeDef",
    "ListPricingPlansOutputTypeDef",
    "ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef",
    "ListPricingRulesAssociatedToPricingPlanInputTypeDef",
    "ListPricingRulesAssociatedToPricingPlanOutputTypeDef",
    "ListPricingRulesFilterTypeDef",
    "ListPricingRulesInputPaginateTypeDef",
    "ListPricingRulesInputTypeDef",
    "ListPricingRulesOutputTypeDef",
    "ListResourcesAssociatedToCustomLineItemFilterTypeDef",
    "ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef",
    "ListResourcesAssociatedToCustomLineItemInputTypeDef",
    "ListResourcesAssociatedToCustomLineItemOutputTypeDef",
    "ListResourcesAssociatedToCustomLineItemResponseElementTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PricingPlanListElementTypeDef",
    "PricingRuleListElementTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TieringTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateBillingGroupAccountGroupingTypeDef",
    "UpdateBillingGroupInputTypeDef",
    "UpdateBillingGroupOutputTypeDef",
    "UpdateCustomLineItemChargeDetailsTypeDef",
    "UpdateCustomLineItemFlatChargeDetailsTypeDef",
    "UpdateCustomLineItemInputTypeDef",
    "UpdateCustomLineItemOutputTypeDef",
    "UpdateCustomLineItemPercentageChargeDetailsTypeDef",
    "UpdateFreeTierConfigTypeDef",
    "UpdatePricingPlanInputTypeDef",
    "UpdatePricingPlanOutputTypeDef",
    "UpdatePricingRuleInputTypeDef",
    "UpdatePricingRuleOutputTypeDef",
    "UpdateTieringInputTypeDef",
)

class AccountAssociationsListElementTypeDef(TypedDict):
    AccountId: NotRequired[str]
    BillingGroupArn: NotRequired[str]
    AccountName: NotRequired[str]
    AccountEmail: NotRequired[str]

class AccountGroupingTypeDef(TypedDict):
    LinkedAccountIds: Sequence[str]
    AutoAssociate: NotRequired[bool]

class AssociateAccountsInputTypeDef(TypedDict):
    Arn: str
    AccountIds: Sequence[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociatePricingRulesInputTypeDef(TypedDict):
    Arn: str
    PricingRuleArns: Sequence[str]

class AssociateResourceErrorTypeDef(TypedDict):
    Message: NotRequired[str]
    Reason: NotRequired[AssociateResourceErrorReasonType]

class AttributeTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class CustomLineItemBillingPeriodRangeTypeDef(TypedDict):
    InclusiveStartBillingPeriod: str
    ExclusiveEndBillingPeriod: NotRequired[str]

class BillingGroupCostReportElementTypeDef(TypedDict):
    Arn: NotRequired[str]
    AWSCost: NotRequired[str]
    ProformaCost: NotRequired[str]
    Margin: NotRequired[str]
    MarginPercentage: NotRequired[str]
    Currency: NotRequired[str]

class ComputationPreferenceTypeDef(TypedDict):
    PricingPlanArn: str

class ListBillingGroupAccountGroupingTypeDef(TypedDict):
    AutoAssociate: NotRequired[bool]

class BillingPeriodRangeTypeDef(TypedDict):
    InclusiveStartBillingPeriod: str
    ExclusiveEndBillingPeriod: str

class CreateFreeTierConfigTypeDef(TypedDict):
    Activated: bool

class CreatePricingPlanInputTypeDef(TypedDict):
    Name: str
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    PricingRuleArns: NotRequired[Sequence[str]]
    Tags: NotRequired[Mapping[str, str]]

class CustomLineItemFlatChargeDetailsTypeDef(TypedDict):
    ChargeValue: float

class CustomLineItemPercentageChargeDetailsTypeDef(TypedDict):
    PercentageValue: float
    AssociatedValues: NotRequired[Sequence[str]]

class DeleteBillingGroupInputTypeDef(TypedDict):
    Arn: str

class DeletePricingPlanInputTypeDef(TypedDict):
    Arn: str

class DeletePricingRuleInputTypeDef(TypedDict):
    Arn: str

class DisassociateAccountsInputTypeDef(TypedDict):
    Arn: str
    AccountIds: Sequence[str]

class DisassociatePricingRulesInputTypeDef(TypedDict):
    Arn: str
    PricingRuleArns: Sequence[str]

class FreeTierConfigTypeDef(TypedDict):
    Activated: bool

class LineItemFilterOutputTypeDef(TypedDict):
    Attribute: Literal["LINE_ITEM_TYPE"]
    MatchOption: Literal["NOT_EQUAL"]
    Values: List[Literal["SAVINGS_PLAN_NEGATION"]]

class LineItemFilterTypeDef(TypedDict):
    Attribute: Literal["LINE_ITEM_TYPE"]
    MatchOption: Literal["NOT_EQUAL"]
    Values: Sequence[Literal["SAVINGS_PLAN_NEGATION"]]

class ListAccountAssociationsFilterTypeDef(TypedDict):
    Association: NotRequired[str]
    AccountId: NotRequired[str]
    AccountIds: NotRequired[Sequence[str]]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListBillingGroupCostReportsFilterTypeDef(TypedDict):
    BillingGroupArns: NotRequired[Sequence[str]]

class ListBillingGroupsFilterTypeDef(TypedDict):
    Arns: NotRequired[Sequence[str]]
    PricingPlan: NotRequired[str]
    Statuses: NotRequired[Sequence[BillingGroupStatusType]]
    AutoAssociate: NotRequired[bool]

class ListCustomLineItemFlatChargeDetailsTypeDef(TypedDict):
    ChargeValue: float

class ListCustomLineItemPercentageChargeDetailsTypeDef(TypedDict):
    PercentageValue: float

class ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef(TypedDict):
    StartBillingPeriod: NotRequired[str]
    EndBillingPeriod: NotRequired[str]

class ListCustomLineItemsFilterTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    BillingGroups: NotRequired[Sequence[str]]
    Arns: NotRequired[Sequence[str]]
    AccountIds: NotRequired[Sequence[str]]

class ListPricingPlansAssociatedWithPricingRuleInputTypeDef(TypedDict):
    PricingRuleArn: str
    BillingPeriod: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListPricingPlansFilterTypeDef(TypedDict):
    Arns: NotRequired[Sequence[str]]

class PricingPlanListElementTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Description: NotRequired[str]
    Size: NotRequired[int]
    CreationTime: NotRequired[int]
    LastModifiedTime: NotRequired[int]

class ListPricingRulesAssociatedToPricingPlanInputTypeDef(TypedDict):
    PricingPlanArn: str
    BillingPeriod: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListPricingRulesFilterTypeDef(TypedDict):
    Arns: NotRequired[Sequence[str]]

class ListResourcesAssociatedToCustomLineItemFilterTypeDef(TypedDict):
    Relationship: NotRequired[CustomLineItemRelationshipType]

class ListResourcesAssociatedToCustomLineItemResponseElementTypeDef(TypedDict):
    Arn: NotRequired[str]
    Relationship: NotRequired[CustomLineItemRelationshipType]
    EndBillingPeriod: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateBillingGroupAccountGroupingTypeDef(TypedDict):
    AutoAssociate: NotRequired[bool]

class UpdateCustomLineItemFlatChargeDetailsTypeDef(TypedDict):
    ChargeValue: float

class UpdateCustomLineItemPercentageChargeDetailsTypeDef(TypedDict):
    PercentageValue: float

class UpdateFreeTierConfigTypeDef(TypedDict):
    Activated: bool

class UpdatePricingPlanInputTypeDef(TypedDict):
    Arn: str
    Name: NotRequired[str]
    Description: NotRequired[str]

class AssociateAccountsOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePricingRulesOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBillingGroupOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomLineItemOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePricingPlanOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePricingRuleOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBillingGroupOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCustomLineItemOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePricingPlanOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePricingRuleOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateAccountsOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePricingRulesOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountAssociationsOutputTypeDef(TypedDict):
    LinkedAccounts: List[AccountAssociationsListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPricingPlansAssociatedWithPricingRuleOutputTypeDef(TypedDict):
    BillingPeriod: str
    PricingRuleArn: str
    PricingPlanArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPricingRulesAssociatedToPricingPlanOutputTypeDef(TypedDict):
    BillingPeriod: str
    PricingPlanArn: str
    PricingRuleArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePricingPlanOutputTypeDef(TypedDict):
    Arn: str
    Name: str
    Description: str
    Size: int
    LastModifiedTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceResponseElementTypeDef(TypedDict):
    Arn: NotRequired[str]
    Error: NotRequired[AssociateResourceErrorTypeDef]

class DisassociateResourceResponseElementTypeDef(TypedDict):
    Arn: NotRequired[str]
    Error: NotRequired[AssociateResourceErrorTypeDef]

class BillingGroupCostReportResultElementTypeDef(TypedDict):
    Arn: NotRequired[str]
    AWSCost: NotRequired[str]
    ProformaCost: NotRequired[str]
    Margin: NotRequired[str]
    MarginPercentage: NotRequired[str]
    Currency: NotRequired[str]
    Attributes: NotRequired[List[AttributeTypeDef]]

class BatchAssociateResourcesToCustomLineItemInputTypeDef(TypedDict):
    TargetArn: str
    ResourceArns: Sequence[str]
    BillingPeriodRange: NotRequired[CustomLineItemBillingPeriodRangeTypeDef]

class BatchDisassociateResourcesFromCustomLineItemInputTypeDef(TypedDict):
    TargetArn: str
    ResourceArns: Sequence[str]
    BillingPeriodRange: NotRequired[CustomLineItemBillingPeriodRangeTypeDef]

class DeleteCustomLineItemInputTypeDef(TypedDict):
    Arn: str
    BillingPeriodRange: NotRequired[CustomLineItemBillingPeriodRangeTypeDef]

class ListBillingGroupCostReportsOutputTypeDef(TypedDict):
    BillingGroupCostReports: List[BillingGroupCostReportElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateBillingGroupInputTypeDef(TypedDict):
    Name: str
    AccountGrouping: AccountGroupingTypeDef
    ComputationPreference: ComputationPreferenceTypeDef
    ClientToken: NotRequired[str]
    PrimaryAccountId: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class BillingGroupListElementTypeDef(TypedDict):
    Name: NotRequired[str]
    Arn: NotRequired[str]
    Description: NotRequired[str]
    PrimaryAccountId: NotRequired[str]
    ComputationPreference: NotRequired[ComputationPreferenceTypeDef]
    Size: NotRequired[int]
    CreationTime: NotRequired[int]
    LastModifiedTime: NotRequired[int]
    Status: NotRequired[BillingGroupStatusType]
    StatusReason: NotRequired[str]
    AccountGrouping: NotRequired[ListBillingGroupAccountGroupingTypeDef]

class GetBillingGroupCostReportInputTypeDef(TypedDict):
    Arn: str
    BillingPeriodRange: NotRequired[BillingPeriodRangeTypeDef]
    GroupBy: NotRequired[Sequence[GroupByAttributeNameType]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class CreateTieringInputTypeDef(TypedDict):
    FreeTier: CreateFreeTierConfigTypeDef

class TieringTypeDef(TypedDict):
    FreeTier: FreeTierConfigTypeDef

LineItemFilterUnionTypeDef = Union[LineItemFilterTypeDef, LineItemFilterOutputTypeDef]

class ListAccountAssociationsInputTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListAccountAssociationsFilterTypeDef]
    NextToken: NotRequired[str]

class ListAccountAssociationsInputPaginateTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListAccountAssociationsFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPricingPlansAssociatedWithPricingRuleInputPaginateTypeDef(TypedDict):
    PricingRuleArn: str
    BillingPeriod: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPricingRulesAssociatedToPricingPlanInputPaginateTypeDef(TypedDict):
    PricingPlanArn: str
    BillingPeriod: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBillingGroupCostReportsInputPaginateTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListBillingGroupCostReportsFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBillingGroupCostReportsInputTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[ListBillingGroupCostReportsFilterTypeDef]

class ListBillingGroupsInputPaginateTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListBillingGroupsFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListBillingGroupsInputTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[ListBillingGroupsFilterTypeDef]

ListCustomLineItemChargeDetailsTypeDef = TypedDict(
    "ListCustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
        "Flat": NotRequired[ListCustomLineItemFlatChargeDetailsTypeDef],
        "Percentage": NotRequired[ListCustomLineItemPercentageChargeDetailsTypeDef],
        "LineItemFilters": NotRequired[List[LineItemFilterOutputTypeDef]],
    },
)

class ListCustomLineItemVersionsFilterTypeDef(TypedDict):
    BillingPeriodRange: NotRequired[ListCustomLineItemVersionsBillingPeriodRangeFilterTypeDef]

class ListCustomLineItemsInputPaginateTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListCustomLineItemsFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomLineItemsInputTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[ListCustomLineItemsFilterTypeDef]

class ListPricingPlansInputPaginateTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListPricingPlansFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPricingPlansInputTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListPricingPlansFilterTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListPricingPlansOutputTypeDef(TypedDict):
    BillingPeriod: str
    PricingPlans: List[PricingPlanListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListPricingRulesInputPaginateTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListPricingRulesFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPricingRulesInputTypeDef(TypedDict):
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListPricingRulesFilterTypeDef]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListResourcesAssociatedToCustomLineItemInputPaginateTypeDef(TypedDict):
    Arn: str
    BillingPeriod: NotRequired[str]
    Filters: NotRequired[ListResourcesAssociatedToCustomLineItemFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourcesAssociatedToCustomLineItemInputTypeDef(TypedDict):
    Arn: str
    BillingPeriod: NotRequired[str]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[ListResourcesAssociatedToCustomLineItemFilterTypeDef]

class ListResourcesAssociatedToCustomLineItemOutputTypeDef(TypedDict):
    Arn: str
    AssociatedResources: List[ListResourcesAssociatedToCustomLineItemResponseElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateBillingGroupInputTypeDef(TypedDict):
    Arn: str
    Name: NotRequired[str]
    Status: NotRequired[BillingGroupStatusType]
    ComputationPreference: NotRequired[ComputationPreferenceTypeDef]
    Description: NotRequired[str]
    AccountGrouping: NotRequired[UpdateBillingGroupAccountGroupingTypeDef]

class UpdateBillingGroupOutputTypeDef(TypedDict):
    Arn: str
    Name: str
    Description: str
    PrimaryAccountId: str
    PricingPlanArn: str
    Size: int
    LastModifiedTime: int
    Status: BillingGroupStatusType
    StatusReason: str
    AccountGrouping: UpdateBillingGroupAccountGroupingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTieringInputTypeDef(TypedDict):
    FreeTier: UpdateFreeTierConfigTypeDef

class BatchAssociateResourcesToCustomLineItemOutputTypeDef(TypedDict):
    SuccessfullyAssociatedResources: List[AssociateResourceResponseElementTypeDef]
    FailedAssociatedResources: List[AssociateResourceResponseElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateResourcesFromCustomLineItemOutputTypeDef(TypedDict):
    SuccessfullyDisassociatedResources: List[DisassociateResourceResponseElementTypeDef]
    FailedDisassociatedResources: List[DisassociateResourceResponseElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBillingGroupCostReportOutputTypeDef(TypedDict):
    BillingGroupCostReportResults: List[BillingGroupCostReportResultElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListBillingGroupsOutputTypeDef(TypedDict):
    BillingGroups: List[BillingGroupListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

CreatePricingRuleInputTypeDef = TypedDict(
    "CreatePricingRuleInputTypeDef",
    {
        "Name": str,
        "Scope": PricingRuleScopeType,
        "Type": PricingRuleTypeType,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "ModifierPercentage": NotRequired[float],
        "Service": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "BillingEntity": NotRequired[str],
        "Tiering": NotRequired[CreateTieringInputTypeDef],
        "UsageType": NotRequired[str],
        "Operation": NotRequired[str],
    },
)
PricingRuleListElementTypeDef = TypedDict(
    "PricingRuleListElementTypeDef",
    {
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "Scope": NotRequired[PricingRuleScopeType],
        "Type": NotRequired[PricingRuleTypeType],
        "ModifierPercentage": NotRequired[float],
        "Service": NotRequired[str],
        "AssociatedPricingPlanCount": NotRequired[int],
        "CreationTime": NotRequired[int],
        "LastModifiedTime": NotRequired[int],
        "BillingEntity": NotRequired[str],
        "Tiering": NotRequired[TieringTypeDef],
        "UsageType": NotRequired[str],
        "Operation": NotRequired[str],
    },
)
CustomLineItemChargeDetailsTypeDef = TypedDict(
    "CustomLineItemChargeDetailsTypeDef",
    {
        "Type": CustomLineItemTypeType,
        "Flat": NotRequired[CustomLineItemFlatChargeDetailsTypeDef],
        "Percentage": NotRequired[CustomLineItemPercentageChargeDetailsTypeDef],
        "LineItemFilters": NotRequired[Sequence[LineItemFilterUnionTypeDef]],
    },
)

class UpdateCustomLineItemChargeDetailsTypeDef(TypedDict):
    Flat: NotRequired[UpdateCustomLineItemFlatChargeDetailsTypeDef]
    Percentage: NotRequired[UpdateCustomLineItemPercentageChargeDetailsTypeDef]
    LineItemFilters: NotRequired[Sequence[LineItemFilterUnionTypeDef]]

class CustomLineItemListElementTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]
    ChargeDetails: NotRequired[ListCustomLineItemChargeDetailsTypeDef]
    CurrencyCode: NotRequired[CurrencyCodeType]
    Description: NotRequired[str]
    ProductCode: NotRequired[str]
    BillingGroupArn: NotRequired[str]
    CreationTime: NotRequired[int]
    LastModifiedTime: NotRequired[int]
    AssociationSize: NotRequired[int]
    AccountId: NotRequired[str]

class CustomLineItemVersionListElementTypeDef(TypedDict):
    Name: NotRequired[str]
    ChargeDetails: NotRequired[ListCustomLineItemChargeDetailsTypeDef]
    CurrencyCode: NotRequired[CurrencyCodeType]
    Description: NotRequired[str]
    ProductCode: NotRequired[str]
    BillingGroupArn: NotRequired[str]
    CreationTime: NotRequired[int]
    LastModifiedTime: NotRequired[int]
    AssociationSize: NotRequired[int]
    StartBillingPeriod: NotRequired[str]
    EndBillingPeriod: NotRequired[str]
    Arn: NotRequired[str]
    StartTime: NotRequired[int]
    AccountId: NotRequired[str]

class UpdateCustomLineItemOutputTypeDef(TypedDict):
    Arn: str
    BillingGroupArn: str
    Name: str
    Description: str
    ChargeDetails: ListCustomLineItemChargeDetailsTypeDef
    LastModifiedTime: int
    AssociationSize: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomLineItemVersionsInputPaginateTypeDef(TypedDict):
    Arn: str
    Filters: NotRequired[ListCustomLineItemVersionsFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCustomLineItemVersionsInputTypeDef(TypedDict):
    Arn: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[ListCustomLineItemVersionsFilterTypeDef]

UpdatePricingRuleInputTypeDef = TypedDict(
    "UpdatePricingRuleInputTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[PricingRuleTypeType],
        "ModifierPercentage": NotRequired[float],
        "Tiering": NotRequired[UpdateTieringInputTypeDef],
    },
)
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
        "Tiering": UpdateTieringInputTypeDef,
        "UsageType": str,
        "Operation": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListPricingRulesOutputTypeDef(TypedDict):
    BillingPeriod: str
    PricingRules: List[PricingRuleListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateCustomLineItemInputTypeDef(TypedDict):
    Name: str
    Description: str
    BillingGroupArn: str
    ChargeDetails: CustomLineItemChargeDetailsTypeDef
    ClientToken: NotRequired[str]
    BillingPeriodRange: NotRequired[CustomLineItemBillingPeriodRangeTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    AccountId: NotRequired[str]

class UpdateCustomLineItemInputTypeDef(TypedDict):
    Arn: str
    Name: NotRequired[str]
    Description: NotRequired[str]
    ChargeDetails: NotRequired[UpdateCustomLineItemChargeDetailsTypeDef]
    BillingPeriodRange: NotRequired[CustomLineItemBillingPeriodRangeTypeDef]

class ListCustomLineItemsOutputTypeDef(TypedDict):
    CustomLineItems: List[CustomLineItemListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListCustomLineItemVersionsOutputTypeDef(TypedDict):
    CustomLineItemVersions: List[CustomLineItemVersionListElementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
