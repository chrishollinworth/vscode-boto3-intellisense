"""
Type annotations for compute-optimizer-automation service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer_automation/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_compute_optimizer_automation.type_defs import AccountInfoTypeDef

    data: AccountInfoTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AutomationEventFilterNameType,
    AutomationRuleFilterNameType,
    ComparisonOperatorType,
    EnrollmentStatusType,
    EventStatusType,
    EventTypeType,
    OrganizationRuleModeType,
    RecommendedActionFilterNameType,
    RecommendedActionTypeType,
    RuleApplyOrderType,
    RuleStatusType,
    RuleTypeType,
    SavingsEstimationModeType,
    StepStatusType,
    StepTypeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountInfoTypeDef",
    "AssociateAccountsRequestTypeDef",
    "AssociateAccountsResponseTypeDef",
    "AutomationEventFilterTypeDef",
    "AutomationEventStepTypeDef",
    "AutomationEventSummaryTypeDef",
    "AutomationEventTypeDef",
    "AutomationRuleTypeDef",
    "CreateAutomationRuleRequestTypeDef",
    "CreateAutomationRuleResponseTypeDef",
    "CriteriaOutputTypeDef",
    "CriteriaTypeDef",
    "CriteriaUnionTypeDef",
    "DeleteAutomationRuleRequestTypeDef",
    "DisassociateAccountsRequestTypeDef",
    "DisassociateAccountsResponseTypeDef",
    "DoubleCriteriaConditionOutputTypeDef",
    "DoubleCriteriaConditionTypeDef",
    "EbsVolumeConfigurationTypeDef",
    "EbsVolumeTypeDef",
    "EstimatedMonthlySavingsTypeDef",
    "FilterTypeDef",
    "GetAutomationEventRequestTypeDef",
    "GetAutomationEventResponseTypeDef",
    "GetAutomationRuleRequestTypeDef",
    "GetAutomationRuleResponseTypeDef",
    "GetEnrollmentConfigurationResponseTypeDef",
    "IntegerCriteriaConditionOutputTypeDef",
    "IntegerCriteriaConditionTypeDef",
    "ListAccountsRequestPaginateTypeDef",
    "ListAccountsRequestTypeDef",
    "ListAccountsResponseTypeDef",
    "ListAutomationEventStepsRequestPaginateTypeDef",
    "ListAutomationEventStepsRequestTypeDef",
    "ListAutomationEventStepsResponseTypeDef",
    "ListAutomationEventSummariesRequestPaginateTypeDef",
    "ListAutomationEventSummariesRequestTypeDef",
    "ListAutomationEventSummariesResponseTypeDef",
    "ListAutomationEventsRequestPaginateTypeDef",
    "ListAutomationEventsRequestTypeDef",
    "ListAutomationEventsResponseTypeDef",
    "ListAutomationRulePreviewRequestPaginateTypeDef",
    "ListAutomationRulePreviewRequestTypeDef",
    "ListAutomationRulePreviewResponseTypeDef",
    "ListAutomationRulePreviewSummariesRequestPaginateTypeDef",
    "ListAutomationRulePreviewSummariesRequestTypeDef",
    "ListAutomationRulePreviewSummariesResponseTypeDef",
    "ListAutomationRulesRequestPaginateTypeDef",
    "ListAutomationRulesRequestTypeDef",
    "ListAutomationRulesResponseTypeDef",
    "ListRecommendedActionSummariesRequestPaginateTypeDef",
    "ListRecommendedActionSummariesRequestTypeDef",
    "ListRecommendedActionSummariesResponseTypeDef",
    "ListRecommendedActionsRequestPaginateTypeDef",
    "ListRecommendedActionsRequestTypeDef",
    "ListRecommendedActionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OrganizationConfigurationOutputTypeDef",
    "OrganizationConfigurationTypeDef",
    "OrganizationConfigurationUnionTypeDef",
    "OrganizationScopeTypeDef",
    "PaginatorConfigTypeDef",
    "PreviewResultSummaryTypeDef",
    "PreviewResultTypeDef",
    "RecommendedActionFilterTypeDef",
    "RecommendedActionSummaryTypeDef",
    "RecommendedActionTotalTypeDef",
    "RecommendedActionTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTagsCriteriaConditionOutputTypeDef",
    "ResourceTagsCriteriaConditionTypeDef",
    "ResponseMetadataTypeDef",
    "RollbackAutomationEventRequestTypeDef",
    "RollbackAutomationEventResponseTypeDef",
    "RulePreviewTotalTypeDef",
    "ScheduleTypeDef",
    "StartAutomationEventRequestTypeDef",
    "StartAutomationEventResponseTypeDef",
    "StringCriteriaConditionOutputTypeDef",
    "StringCriteriaConditionTypeDef",
    "SummaryDimensionTypeDef",
    "SummaryTotalsTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimePeriodTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAutomationRuleRequestTypeDef",
    "UpdateAutomationRuleResponseTypeDef",
    "UpdateEnrollmentConfigurationRequestTypeDef",
    "UpdateEnrollmentConfigurationResponseTypeDef",
)

class AccountInfoTypeDef(TypedDict):
    accountId: str
    status: EnrollmentStatusType
    organizationRuleMode: OrganizationRuleModeType
    lastUpdatedTimestamp: datetime
    statusReason: NotRequired[str]

class AssociateAccountsRequestTypeDef(TypedDict):
    accountIds: Sequence[str]
    clientToken: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AutomationEventFilterTypeDef(TypedDict):
    name: AutomationEventFilterNameType
    values: Sequence[str]

class EstimatedMonthlySavingsTypeDef(TypedDict):
    currency: str
    beforeDiscountSavings: float
    afterDiscountSavings: float
    savingsEstimationMode: SavingsEstimationModeType

class SummaryDimensionTypeDef(TypedDict):
    key: Literal["EventStatus"]
    value: str

class TimePeriodTypeDef(TypedDict):
    startTimeInclusive: NotRequired[datetime]
    endTimeExclusive: NotRequired[datetime]

class OrganizationConfigurationOutputTypeDef(TypedDict):
    ruleApplyOrder: NotRequired[RuleApplyOrderType]
    accountIds: NotRequired[List[str]]

class ScheduleTypeDef(TypedDict):
    scheduleExpression: NotRequired[str]
    scheduleExpressionTimezone: NotRequired[str]
    executionWindowInMinutes: NotRequired[int]

class TagTypeDef(TypedDict):
    key: str
    value: str

class DoubleCriteriaConditionOutputTypeDef(TypedDict):
    comparison: NotRequired[ComparisonOperatorType]
    values: NotRequired[List[float]]

class IntegerCriteriaConditionOutputTypeDef(TypedDict):
    comparison: NotRequired[ComparisonOperatorType]
    values: NotRequired[List[int]]

class ResourceTagsCriteriaConditionOutputTypeDef(TypedDict):
    comparison: NotRequired[ComparisonOperatorType]
    key: NotRequired[str]
    values: NotRequired[List[str]]

class StringCriteriaConditionOutputTypeDef(TypedDict):
    comparison: NotRequired[ComparisonOperatorType]
    values: NotRequired[List[str]]

class DoubleCriteriaConditionTypeDef(TypedDict):
    comparison: NotRequired[ComparisonOperatorType]
    values: NotRequired[Sequence[float]]

class IntegerCriteriaConditionTypeDef(TypedDict):
    comparison: NotRequired[ComparisonOperatorType]
    values: NotRequired[Sequence[int]]

class ResourceTagsCriteriaConditionTypeDef(TypedDict):
    comparison: NotRequired[ComparisonOperatorType]
    key: NotRequired[str]
    values: NotRequired[Sequence[str]]

class StringCriteriaConditionTypeDef(TypedDict):
    comparison: NotRequired[ComparisonOperatorType]
    values: NotRequired[Sequence[str]]

class DeleteAutomationRuleRequestTypeDef(TypedDict):
    ruleArn: str
    ruleRevision: int
    clientToken: NotRequired[str]

class DisassociateAccountsRequestTypeDef(TypedDict):
    accountIds: Sequence[str]
    clientToken: NotRequired[str]

EbsVolumeConfigurationTypeDef = TypedDict(
    "EbsVolumeConfigurationTypeDef",
    {
        "type": NotRequired[str],
        "sizeInGib": NotRequired[int],
        "iops": NotRequired[int],
        "throughput": NotRequired[int],
    },
)

class FilterTypeDef(TypedDict):
    name: AutomationRuleFilterNameType
    values: Sequence[str]

class GetAutomationEventRequestTypeDef(TypedDict):
    eventId: str

class GetAutomationRuleRequestTypeDef(TypedDict):
    ruleArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccountsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAutomationEventStepsRequestTypeDef(TypedDict):
    eventId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class OrganizationScopeTypeDef(TypedDict):
    accountIds: NotRequired[Sequence[str]]

class RecommendedActionFilterTypeDef(TypedDict):
    name: RecommendedActionFilterNameType
    values: Sequence[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class OrganizationConfigurationTypeDef(TypedDict):
    ruleApplyOrder: NotRequired[RuleApplyOrderType]
    accountIds: NotRequired[Sequence[str]]

class RollbackAutomationEventRequestTypeDef(TypedDict):
    eventId: str
    clientToken: NotRequired[str]

class StartAutomationEventRequestTypeDef(TypedDict):
    recommendedActionId: str
    clientToken: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    ruleRevision: int
    tagKeys: Sequence[str]
    clientToken: NotRequired[str]

class UpdateEnrollmentConfigurationRequestTypeDef(TypedDict):
    status: EnrollmentStatusType
    clientToken: NotRequired[str]

class AssociateAccountsResponseTypeDef(TypedDict):
    accountIds: List[str]
    errors: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateAccountsResponseTypeDef(TypedDict):
    accountIds: List[str]
    errors: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnrollmentConfigurationResponseTypeDef(TypedDict):
    status: EnrollmentStatusType
    statusReason: str
    organizationRuleMode: OrganizationRuleModeType
    lastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsResponseTypeDef(TypedDict):
    accounts: List[AccountInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RollbackAutomationEventResponseTypeDef(TypedDict):
    eventId: str
    eventStatus: EventStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StartAutomationEventResponseTypeDef(TypedDict):
    recommendedActionId: str
    eventId: str
    eventStatus: EventStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEnrollmentConfigurationResponseTypeDef(TypedDict):
    status: EnrollmentStatusType
    statusReason: str
    lastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutomationEventSummariesRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[AutomationEventFilterTypeDef]]
    startDateInclusive: NotRequired[str]
    endDateExclusive: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class AutomationEventStepTypeDef(TypedDict):
    eventId: NotRequired[str]
    stepId: NotRequired[str]
    stepType: NotRequired[StepTypeType]
    stepStatus: NotRequired[StepStatusType]
    resourceId: NotRequired[str]
    startTimestamp: NotRequired[datetime]
    completedTimestamp: NotRequired[datetime]
    estimatedMonthlySavings: NotRequired[EstimatedMonthlySavingsTypeDef]

class AutomationEventTypeDef(TypedDict):
    eventId: NotRequired[str]
    eventDescription: NotRequired[str]
    eventType: NotRequired[EventTypeType]
    eventStatus: NotRequired[EventStatusType]
    eventStatusReason: NotRequired[str]
    resourceArn: NotRequired[str]
    resourceId: NotRequired[str]
    recommendedActionId: NotRequired[str]
    accountId: NotRequired[str]
    region: NotRequired[str]
    ruleId: NotRequired[str]
    resourceType: NotRequired[Literal["EbsVolume"]]
    createdTimestamp: NotRequired[datetime]
    completedTimestamp: NotRequired[datetime]
    estimatedMonthlySavings: NotRequired[EstimatedMonthlySavingsTypeDef]

class GetAutomationEventResponseTypeDef(TypedDict):
    eventId: str
    eventDescription: str
    eventType: EventTypeType
    eventStatus: EventStatusType
    eventStatusReason: str
    resourceArn: str
    resourceId: str
    recommendedActionId: str
    accountId: str
    region: str
    ruleId: str
    resourceType: Literal["EbsVolume"]
    createdTimestamp: datetime
    completedTimestamp: datetime
    estimatedMonthlySavings: EstimatedMonthlySavingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendedActionTotalTypeDef(TypedDict):
    recommendedActionCount: int
    estimatedMonthlySavings: EstimatedMonthlySavingsTypeDef

class RulePreviewTotalTypeDef(TypedDict):
    recommendedActionCount: int
    estimatedMonthlySavings: EstimatedMonthlySavingsTypeDef

class SummaryTotalsTypeDef(TypedDict):
    automationEventCount: NotRequired[int]
    estimatedMonthlySavings: NotRequired[EstimatedMonthlySavingsTypeDef]

class AutomationRuleTypeDef(TypedDict):
    ruleArn: NotRequired[str]
    ruleId: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    ruleType: NotRequired[RuleTypeType]
    ruleRevision: NotRequired[int]
    accountId: NotRequired[str]
    organizationConfiguration: NotRequired[OrganizationConfigurationOutputTypeDef]
    priority: NotRequired[str]
    recommendedActionTypes: NotRequired[List[RecommendedActionTypeType]]
    schedule: NotRequired[ScheduleTypeDef]
    status: NotRequired[RuleStatusType]
    createdTimestamp: NotRequired[datetime]
    lastUpdatedTimestamp: NotRequired[datetime]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    ruleRevision: int
    tags: Sequence[TagTypeDef]
    clientToken: NotRequired[str]

class CriteriaOutputTypeDef(TypedDict):
    region: NotRequired[List[StringCriteriaConditionOutputTypeDef]]
    resourceArn: NotRequired[List[StringCriteriaConditionOutputTypeDef]]
    ebsVolumeType: NotRequired[List[StringCriteriaConditionOutputTypeDef]]
    ebsVolumeSizeInGib: NotRequired[List[IntegerCriteriaConditionOutputTypeDef]]
    estimatedMonthlySavings: NotRequired[List[DoubleCriteriaConditionOutputTypeDef]]
    resourceTag: NotRequired[List[ResourceTagsCriteriaConditionOutputTypeDef]]
    lookBackPeriodInDays: NotRequired[List[IntegerCriteriaConditionOutputTypeDef]]
    restartNeeded: NotRequired[List[StringCriteriaConditionOutputTypeDef]]

class CriteriaTypeDef(TypedDict):
    region: NotRequired[Sequence[StringCriteriaConditionTypeDef]]
    resourceArn: NotRequired[Sequence[StringCriteriaConditionTypeDef]]
    ebsVolumeType: NotRequired[Sequence[StringCriteriaConditionTypeDef]]
    ebsVolumeSizeInGib: NotRequired[Sequence[IntegerCriteriaConditionTypeDef]]
    estimatedMonthlySavings: NotRequired[Sequence[DoubleCriteriaConditionTypeDef]]
    resourceTag: NotRequired[Sequence[ResourceTagsCriteriaConditionTypeDef]]
    lookBackPeriodInDays: NotRequired[Sequence[IntegerCriteriaConditionTypeDef]]
    restartNeeded: NotRequired[Sequence[StringCriteriaConditionTypeDef]]

class EbsVolumeTypeDef(TypedDict):
    configuration: NotRequired[EbsVolumeConfigurationTypeDef]

class ListAutomationRulesRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAccountsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAutomationEventStepsRequestPaginateTypeDef(TypedDict):
    eventId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAutomationEventSummariesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[AutomationEventFilterTypeDef]]
    startDateInclusive: NotRequired[str]
    endDateExclusive: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAutomationRulesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAutomationEventsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[AutomationEventFilterTypeDef]]
    startTimeInclusive: NotRequired[TimestampTypeDef]
    endTimeExclusive: NotRequired[TimestampTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAutomationEventsRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[AutomationEventFilterTypeDef]]
    startTimeInclusive: NotRequired[TimestampTypeDef]
    endTimeExclusive: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListRecommendedActionSummariesRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[RecommendedActionFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecommendedActionSummariesRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[RecommendedActionFilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListRecommendedActionsRequestPaginateTypeDef(TypedDict):
    filters: NotRequired[Sequence[RecommendedActionFilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRecommendedActionsRequestTypeDef(TypedDict):
    filters: NotRequired[Sequence[RecommendedActionFilterTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

OrganizationConfigurationUnionTypeDef = Union[
    OrganizationConfigurationTypeDef, OrganizationConfigurationOutputTypeDef
]

class ListAutomationEventStepsResponseTypeDef(TypedDict):
    automationEventSteps: List[AutomationEventStepTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAutomationEventsResponseTypeDef(TypedDict):
    automationEvents: List[AutomationEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RecommendedActionSummaryTypeDef(TypedDict):
    key: str
    total: RecommendedActionTotalTypeDef

class PreviewResultSummaryTypeDef(TypedDict):
    key: str
    total: RulePreviewTotalTypeDef

class AutomationEventSummaryTypeDef(TypedDict):
    key: NotRequired[str]
    dimensions: NotRequired[List[SummaryDimensionTypeDef]]
    timePeriod: NotRequired[TimePeriodTypeDef]
    total: NotRequired[SummaryTotalsTypeDef]

class ListAutomationRulesResponseTypeDef(TypedDict):
    automationRules: List[AutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateAutomationRuleResponseTypeDef(TypedDict):
    ruleArn: str
    ruleId: str
    name: str
    description: str
    ruleType: RuleTypeType
    ruleRevision: int
    organizationConfiguration: OrganizationConfigurationOutputTypeDef
    priority: str
    recommendedActionTypes: List[RecommendedActionTypeType]
    criteria: CriteriaOutputTypeDef
    schedule: ScheduleTypeDef
    status: RuleStatusType
    tags: List[TagTypeDef]
    createdTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetAutomationRuleResponseTypeDef(TypedDict):
    ruleArn: str
    ruleId: str
    name: str
    description: str
    ruleType: RuleTypeType
    ruleRevision: int
    accountId: str
    organizationConfiguration: OrganizationConfigurationOutputTypeDef
    priority: str
    recommendedActionTypes: List[RecommendedActionTypeType]
    criteria: CriteriaOutputTypeDef
    schedule: ScheduleTypeDef
    status: RuleStatusType
    tags: List[TagTypeDef]
    createdTimestamp: datetime
    lastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAutomationRuleResponseTypeDef(TypedDict):
    ruleArn: str
    ruleRevision: int
    name: str
    description: str
    ruleType: RuleTypeType
    organizationConfiguration: OrganizationConfigurationOutputTypeDef
    priority: str
    recommendedActionTypes: List[RecommendedActionTypeType]
    criteria: CriteriaOutputTypeDef
    schedule: ScheduleTypeDef
    status: RuleStatusType
    createdTimestamp: datetime
    lastUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

CriteriaUnionTypeDef = Union[CriteriaTypeDef, CriteriaOutputTypeDef]

class ResourceDetailsTypeDef(TypedDict):
    ebsVolume: NotRequired[EbsVolumeTypeDef]

class ListRecommendedActionSummariesResponseTypeDef(TypedDict):
    recommendedActionSummaries: List[RecommendedActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAutomationRulePreviewSummariesResponseTypeDef(TypedDict):
    previewResultSummaries: List[PreviewResultSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAutomationEventSummariesResponseTypeDef(TypedDict):
    automationEventSummaries: List[AutomationEventSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateAutomationRuleRequestTypeDef(TypedDict):
    name: str
    ruleType: RuleTypeType
    recommendedActionTypes: Sequence[RecommendedActionTypeType]
    schedule: ScheduleTypeDef
    status: RuleStatusType
    description: NotRequired[str]
    organizationConfiguration: NotRequired[OrganizationConfigurationUnionTypeDef]
    priority: NotRequired[str]
    criteria: NotRequired[CriteriaUnionTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]
    clientToken: NotRequired[str]

class ListAutomationRulePreviewRequestPaginateTypeDef(TypedDict):
    ruleType: RuleTypeType
    recommendedActionTypes: Sequence[RecommendedActionTypeType]
    organizationScope: NotRequired[OrganizationScopeTypeDef]
    criteria: NotRequired[CriteriaUnionTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAutomationRulePreviewRequestTypeDef(TypedDict):
    ruleType: RuleTypeType
    recommendedActionTypes: Sequence[RecommendedActionTypeType]
    organizationScope: NotRequired[OrganizationScopeTypeDef]
    criteria: NotRequired[CriteriaUnionTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAutomationRulePreviewSummariesRequestPaginateTypeDef(TypedDict):
    ruleType: RuleTypeType
    recommendedActionTypes: Sequence[RecommendedActionTypeType]
    organizationScope: NotRequired[OrganizationScopeTypeDef]
    criteria: NotRequired[CriteriaUnionTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAutomationRulePreviewSummariesRequestTypeDef(TypedDict):
    ruleType: RuleTypeType
    recommendedActionTypes: Sequence[RecommendedActionTypeType]
    organizationScope: NotRequired[OrganizationScopeTypeDef]
    criteria: NotRequired[CriteriaUnionTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class UpdateAutomationRuleRequestTypeDef(TypedDict):
    ruleArn: str
    ruleRevision: int
    name: NotRequired[str]
    description: NotRequired[str]
    ruleType: NotRequired[RuleTypeType]
    organizationConfiguration: NotRequired[OrganizationConfigurationUnionTypeDef]
    priority: NotRequired[str]
    recommendedActionTypes: NotRequired[Sequence[RecommendedActionTypeType]]
    criteria: NotRequired[CriteriaUnionTypeDef]
    schedule: NotRequired[ScheduleTypeDef]
    status: NotRequired[RuleStatusType]
    clientToken: NotRequired[str]

class PreviewResultTypeDef(TypedDict):
    recommendedActionId: NotRequired[str]
    resourceArn: NotRequired[str]
    resourceId: NotRequired[str]
    accountId: NotRequired[str]
    region: NotRequired[str]
    resourceType: NotRequired[Literal["EbsVolume"]]
    lookBackPeriodInDays: NotRequired[int]
    recommendedActionType: NotRequired[RecommendedActionTypeType]
    currentResourceSummary: NotRequired[str]
    currentResourceDetails: NotRequired[ResourceDetailsTypeDef]
    recommendedResourceSummary: NotRequired[str]
    recommendedResourceDetails: NotRequired[ResourceDetailsTypeDef]
    restartNeeded: NotRequired[bool]
    estimatedMonthlySavings: NotRequired[EstimatedMonthlySavingsTypeDef]
    resourceTags: NotRequired[List[TagTypeDef]]

class RecommendedActionTypeDef(TypedDict):
    recommendedActionId: NotRequired[str]
    resourceArn: NotRequired[str]
    resourceId: NotRequired[str]
    accountId: NotRequired[str]
    region: NotRequired[str]
    resourceType: NotRequired[Literal["EbsVolume"]]
    lookBackPeriodInDays: NotRequired[int]
    recommendedActionType: NotRequired[RecommendedActionTypeType]
    currentResourceSummary: NotRequired[str]
    currentResourceDetails: NotRequired[ResourceDetailsTypeDef]
    recommendedResourceSummary: NotRequired[str]
    recommendedResourceDetails: NotRequired[ResourceDetailsTypeDef]
    restartNeeded: NotRequired[bool]
    estimatedMonthlySavings: NotRequired[EstimatedMonthlySavingsTypeDef]
    resourceTags: NotRequired[List[TagTypeDef]]

class ListAutomationRulePreviewResponseTypeDef(TypedDict):
    previewResults: List[PreviewResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRecommendedActionsResponseTypeDef(TypedDict):
    recommendedActions: List[RecommendedActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
