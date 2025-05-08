"""
Type annotations for resiliencehub service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_resiliencehub.type_defs import AcceptGroupingRecommendationEntryTypeDef

    data: AcceptGroupingRecommendationEntryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AlarmTypeType,
    AppAssessmentScheduleTypeType,
    AppComplianceStatusTypeType,
    AppDriftStatusTypeType,
    AppStatusTypeType,
    AssessmentInvokerType,
    AssessmentStatusType,
    ComplianceStatusType,
    ConditionOperatorTypeType,
    ConfigRecommendationOptimizationTypeType,
    CostFrequencyType,
    DataLocationConstraintType,
    DifferenceTypeType,
    DisruptionTypeType,
    DriftStatusType,
    DriftTypeType,
    EstimatedCostTierType,
    EventTypeType,
    ExcludeRecommendationReasonType,
    FieldAggregationTypeType,
    GroupingRecommendationConfidenceLevelType,
    GroupingRecommendationRejectionReasonType,
    GroupingRecommendationStatusTypeType,
    HaArchitectureType,
    MetricsExportStatusTypeType,
    PermissionModelTypeType,
    PhysicalIdentifierTypeType,
    RecommendationComplianceStatusType,
    RecommendationStatusType,
    RecommendationTemplateStatusType,
    RenderRecommendationTypeType,
    ResiliencyPolicyTierType,
    ResiliencyScoreTypeType,
    ResourceImportStatusTypeType,
    ResourceImportStrategyTypeType,
    ResourceMappingTypeType,
    ResourceResolutionStatusTypeType,
    ResourcesGroupingRecGenStatusTypeType,
    ResourceSourceTypeType,
    TemplateFormatType,
    TestRiskType,
    TestTypeType,
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
    "AcceptGroupingRecommendationEntryTypeDef",
    "AcceptResourceGroupingRecommendationsRequestTypeDef",
    "AcceptResourceGroupingRecommendationsResponseTypeDef",
    "AddDraftAppVersionResourceMappingsRequestTypeDef",
    "AddDraftAppVersionResourceMappingsResponseTypeDef",
    "AlarmRecommendationTypeDef",
    "AlarmTypeDef",
    "AppAssessmentSummaryTypeDef",
    "AppAssessmentTypeDef",
    "AppComponentComplianceTypeDef",
    "AppComponentTypeDef",
    "AppInputSourceTypeDef",
    "AppSummaryTypeDef",
    "AppTypeDef",
    "AppVersionSummaryTypeDef",
    "AssessmentRiskRecommendationTypeDef",
    "AssessmentSummaryTypeDef",
    "BatchUpdateRecommendationStatusFailedEntryTypeDef",
    "BatchUpdateRecommendationStatusRequestTypeDef",
    "BatchUpdateRecommendationStatusResponseTypeDef",
    "BatchUpdateRecommendationStatusSuccessfulEntryTypeDef",
    "ComplianceDriftTypeDef",
    "ComponentRecommendationTypeDef",
    "ConditionTypeDef",
    "ConfigRecommendationTypeDef",
    "CostTypeDef",
    "CreateAppRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateAppVersionAppComponentRequestTypeDef",
    "CreateAppVersionAppComponentResponseTypeDef",
    "CreateAppVersionResourceRequestTypeDef",
    "CreateAppVersionResourceResponseTypeDef",
    "CreateRecommendationTemplateRequestTypeDef",
    "CreateRecommendationTemplateResponseTypeDef",
    "CreateResiliencyPolicyRequestTypeDef",
    "CreateResiliencyPolicyResponseTypeDef",
    "DeleteAppAssessmentRequestTypeDef",
    "DeleteAppAssessmentResponseTypeDef",
    "DeleteAppInputSourceRequestTypeDef",
    "DeleteAppInputSourceResponseTypeDef",
    "DeleteAppRequestTypeDef",
    "DeleteAppResponseTypeDef",
    "DeleteAppVersionAppComponentRequestTypeDef",
    "DeleteAppVersionAppComponentResponseTypeDef",
    "DeleteAppVersionResourceRequestTypeDef",
    "DeleteAppVersionResourceResponseTypeDef",
    "DeleteRecommendationTemplateRequestTypeDef",
    "DeleteRecommendationTemplateResponseTypeDef",
    "DeleteResiliencyPolicyRequestTypeDef",
    "DeleteResiliencyPolicyResponseTypeDef",
    "DescribeAppAssessmentRequestTypeDef",
    "DescribeAppAssessmentResponseTypeDef",
    "DescribeAppRequestTypeDef",
    "DescribeAppResponseTypeDef",
    "DescribeAppVersionAppComponentRequestTypeDef",
    "DescribeAppVersionAppComponentResponseTypeDef",
    "DescribeAppVersionRequestTypeDef",
    "DescribeAppVersionResourceRequestTypeDef",
    "DescribeAppVersionResourceResponseTypeDef",
    "DescribeAppVersionResourcesResolutionStatusRequestTypeDef",
    "DescribeAppVersionResourcesResolutionStatusResponseTypeDef",
    "DescribeAppVersionResponseTypeDef",
    "DescribeAppVersionTemplateRequestTypeDef",
    "DescribeAppVersionTemplateResponseTypeDef",
    "DescribeDraftAppVersionResourcesImportStatusRequestTypeDef",
    "DescribeDraftAppVersionResourcesImportStatusResponseTypeDef",
    "DescribeMetricsExportRequestTypeDef",
    "DescribeMetricsExportResponseTypeDef",
    "DescribeResiliencyPolicyRequestTypeDef",
    "DescribeResiliencyPolicyResponseTypeDef",
    "DescribeResourceGroupingRecommendationTaskRequestTypeDef",
    "DescribeResourceGroupingRecommendationTaskResponseTypeDef",
    "DisruptionComplianceTypeDef",
    "EksSourceClusterNamespaceTypeDef",
    "EksSourceOutputTypeDef",
    "EksSourceTypeDef",
    "EksSourceUnionTypeDef",
    "ErrorDetailTypeDef",
    "EventSubscriptionTypeDef",
    "ExperimentTypeDef",
    "FailedGroupingRecommendationEntryTypeDef",
    "FailurePolicyTypeDef",
    "FieldTypeDef",
    "GroupingAppComponentTypeDef",
    "GroupingRecommendationTypeDef",
    "GroupingResourceTypeDef",
    "ImportResourcesToDraftAppVersionRequestTypeDef",
    "ImportResourcesToDraftAppVersionResponseTypeDef",
    "ListAlarmRecommendationsRequestTypeDef",
    "ListAlarmRecommendationsResponseTypeDef",
    "ListAppAssessmentComplianceDriftsRequestTypeDef",
    "ListAppAssessmentComplianceDriftsResponseTypeDef",
    "ListAppAssessmentResourceDriftsRequestPaginateTypeDef",
    "ListAppAssessmentResourceDriftsRequestTypeDef",
    "ListAppAssessmentResourceDriftsResponseTypeDef",
    "ListAppAssessmentsRequestTypeDef",
    "ListAppAssessmentsResponseTypeDef",
    "ListAppComponentCompliancesRequestTypeDef",
    "ListAppComponentCompliancesResponseTypeDef",
    "ListAppComponentRecommendationsRequestTypeDef",
    "ListAppComponentRecommendationsResponseTypeDef",
    "ListAppInputSourcesRequestTypeDef",
    "ListAppInputSourcesResponseTypeDef",
    "ListAppVersionAppComponentsRequestTypeDef",
    "ListAppVersionAppComponentsResponseTypeDef",
    "ListAppVersionResourceMappingsRequestTypeDef",
    "ListAppVersionResourceMappingsResponseTypeDef",
    "ListAppVersionResourcesRequestTypeDef",
    "ListAppVersionResourcesResponseTypeDef",
    "ListAppVersionsRequestTypeDef",
    "ListAppVersionsResponseTypeDef",
    "ListAppsRequestTypeDef",
    "ListAppsResponseTypeDef",
    "ListMetricsRequestPaginateTypeDef",
    "ListMetricsRequestTypeDef",
    "ListMetricsResponseTypeDef",
    "ListRecommendationTemplatesRequestTypeDef",
    "ListRecommendationTemplatesResponseTypeDef",
    "ListResiliencyPoliciesRequestTypeDef",
    "ListResiliencyPoliciesResponseTypeDef",
    "ListResourceGroupingRecommendationsRequestPaginateTypeDef",
    "ListResourceGroupingRecommendationsRequestTypeDef",
    "ListResourceGroupingRecommendationsResponseTypeDef",
    "ListSopRecommendationsRequestTypeDef",
    "ListSopRecommendationsResponseTypeDef",
    "ListSuggestedResiliencyPoliciesRequestTypeDef",
    "ListSuggestedResiliencyPoliciesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestRecommendationsRequestTypeDef",
    "ListTestRecommendationsResponseTypeDef",
    "ListUnsupportedAppVersionResourcesRequestTypeDef",
    "ListUnsupportedAppVersionResourcesResponseTypeDef",
    "LogicalResourceIdTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionModelOutputTypeDef",
    "PermissionModelTypeDef",
    "PermissionModelUnionTypeDef",
    "PhysicalResourceIdTypeDef",
    "PhysicalResourceTypeDef",
    "PublishAppVersionRequestTypeDef",
    "PublishAppVersionResponseTypeDef",
    "PutDraftAppVersionTemplateRequestTypeDef",
    "PutDraftAppVersionTemplateResponseTypeDef",
    "RecommendationDisruptionComplianceTypeDef",
    "RecommendationItemTypeDef",
    "RecommendationTemplateTypeDef",
    "RejectGroupingRecommendationEntryTypeDef",
    "RejectResourceGroupingRecommendationsRequestTypeDef",
    "RejectResourceGroupingRecommendationsResponseTypeDef",
    "RemoveDraftAppVersionResourceMappingsRequestTypeDef",
    "RemoveDraftAppVersionResourceMappingsResponseTypeDef",
    "ResiliencyPolicyTypeDef",
    "ResiliencyScoreTypeDef",
    "ResolveAppVersionResourcesRequestTypeDef",
    "ResolveAppVersionResourcesResponseTypeDef",
    "ResourceDriftTypeDef",
    "ResourceErrorTypeDef",
    "ResourceErrorsDetailsTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceMappingTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "ScoringComponentResiliencyScoreTypeDef",
    "SopRecommendationTypeDef",
    "SortTypeDef",
    "StartAppAssessmentRequestTypeDef",
    "StartAppAssessmentResponseTypeDef",
    "StartMetricsExportRequestTypeDef",
    "StartMetricsExportResponseTypeDef",
    "StartResourceGroupingRecommendationTaskRequestTypeDef",
    "StartResourceGroupingRecommendationTaskResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TerraformSourceTypeDef",
    "TestRecommendationTypeDef",
    "TimestampTypeDef",
    "UnsupportedResourceTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAppRequestTypeDef",
    "UpdateAppResponseTypeDef",
    "UpdateAppVersionAppComponentRequestTypeDef",
    "UpdateAppVersionAppComponentResponseTypeDef",
    "UpdateAppVersionRequestTypeDef",
    "UpdateAppVersionResourceRequestTypeDef",
    "UpdateAppVersionResourceResponseTypeDef",
    "UpdateAppVersionResponseTypeDef",
    "UpdateRecommendationStatusItemTypeDef",
    "UpdateRecommendationStatusRequestEntryTypeDef",
    "UpdateResiliencyPolicyRequestTypeDef",
    "UpdateResiliencyPolicyResponseTypeDef",
)

class AcceptGroupingRecommendationEntryTypeDef(TypedDict):
    groupingRecommendationId: str

class FailedGroupingRecommendationEntryTypeDef(TypedDict):
    errorMessage: str
    groupingRecommendationId: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AlarmTypeDef(TypedDict):
    alarmArn: NotRequired[str]
    source: NotRequired[str]

class CostTypeDef(TypedDict):
    amount: float
    currency: str
    frequency: CostFrequencyType

class DisruptionComplianceTypeDef(TypedDict):
    complianceStatus: ComplianceStatusType
    achievableRpoInSecs: NotRequired[int]
    achievableRtoInSecs: NotRequired[int]
    currentRpoInSecs: NotRequired[int]
    currentRtoInSecs: NotRequired[int]
    message: NotRequired[str]
    rpoDescription: NotRequired[str]
    rpoReferenceId: NotRequired[str]
    rtoDescription: NotRequired[str]
    rtoReferenceId: NotRequired[str]

AppComponentTypeDef = TypedDict(
    "AppComponentTypeDef",
    {
        "name": str,
        "type": str,
        "additionalInfo": NotRequired[Dict[str, List[str]]],
        "id": NotRequired[str],
    },
)

class EksSourceClusterNamespaceTypeDef(TypedDict):
    eksClusterArn: str
    namespace: str

class TerraformSourceTypeDef(TypedDict):
    s3StateFileUrl: str

class AppSummaryTypeDef(TypedDict):
    appArn: str
    creationTime: datetime
    name: str
    assessmentSchedule: NotRequired[AppAssessmentScheduleTypeType]
    awsApplicationArn: NotRequired[str]
    complianceStatus: NotRequired[AppComplianceStatusTypeType]
    description: NotRequired[str]
    driftStatus: NotRequired[AppDriftStatusTypeType]
    lastAppComplianceEvaluationTime: NotRequired[datetime]
    resiliencyScore: NotRequired[float]
    rpoInSecs: NotRequired[int]
    rtoInSecs: NotRequired[int]
    status: NotRequired[AppStatusTypeType]

class EventSubscriptionTypeDef(TypedDict):
    eventType: EventTypeType
    name: str
    snsTopicArn: NotRequired[str]

PermissionModelOutputTypeDef = TypedDict(
    "PermissionModelOutputTypeDef",
    {
        "type": PermissionModelTypeType,
        "crossAccountRoleArns": NotRequired[List[str]],
        "invokerRoleName": NotRequired[str],
    },
)

class AppVersionSummaryTypeDef(TypedDict):
    appVersion: str
    creationTime: NotRequired[datetime]
    identifier: NotRequired[int]
    versionName: NotRequired[str]

class AssessmentRiskRecommendationTypeDef(TypedDict):
    appComponents: NotRequired[List[str]]
    recommendation: NotRequired[str]
    risk: NotRequired[str]

class BatchUpdateRecommendationStatusFailedEntryTypeDef(TypedDict):
    entryId: str
    errorMessage: str

class UpdateRecommendationStatusItemTypeDef(TypedDict):
    resourceId: NotRequired[str]
    targetAccountId: NotRequired[str]
    targetRegion: NotRequired[str]

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "field": str,
        "operator": ConditionOperatorTypeType,
        "value": NotRequired[str],
    },
)

class RecommendationDisruptionComplianceTypeDef(TypedDict):
    expectedComplianceStatus: ComplianceStatusType
    expectedRpoDescription: NotRequired[str]
    expectedRpoInSecs: NotRequired[int]
    expectedRtoDescription: NotRequired[str]
    expectedRtoInSecs: NotRequired[int]

CreateAppVersionAppComponentRequestTypeDef = TypedDict(
    "CreateAppVersionAppComponentRequestTypeDef",
    {
        "appArn": str,
        "name": str,
        "type": str,
        "additionalInfo": NotRequired[Mapping[str, Sequence[str]]],
        "clientToken": NotRequired[str],
        "id": NotRequired[str],
    },
)

class LogicalResourceIdTypeDef(TypedDict):
    identifier: str
    eksSourceName: NotRequired[str]
    logicalStackName: NotRequired[str]
    resourceGroupName: NotRequired[str]
    terraformSourceName: NotRequired[str]

CreateRecommendationTemplateRequestTypeDef = TypedDict(
    "CreateRecommendationTemplateRequestTypeDef",
    {
        "assessmentArn": str,
        "name": str,
        "bucketName": NotRequired[str],
        "clientToken": NotRequired[str],
        "format": NotRequired[TemplateFormatType],
        "recommendationIds": NotRequired[Sequence[str]],
        "recommendationTypes": NotRequired[Sequence[RenderRecommendationTypeType]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

class FailurePolicyTypeDef(TypedDict):
    rpoInSecs: int
    rtoInSecs: int

class DeleteAppAssessmentRequestTypeDef(TypedDict):
    assessmentArn: str
    clientToken: NotRequired[str]

class DeleteAppRequestTypeDef(TypedDict):
    appArn: str
    clientToken: NotRequired[str]
    forceDelete: NotRequired[bool]

DeleteAppVersionAppComponentRequestTypeDef = TypedDict(
    "DeleteAppVersionAppComponentRequestTypeDef",
    {
        "appArn": str,
        "id": str,
        "clientToken": NotRequired[str],
    },
)

class DeleteRecommendationTemplateRequestTypeDef(TypedDict):
    recommendationTemplateArn: str
    clientToken: NotRequired[str]

class DeleteResiliencyPolicyRequestTypeDef(TypedDict):
    policyArn: str
    clientToken: NotRequired[str]

class DescribeAppAssessmentRequestTypeDef(TypedDict):
    assessmentArn: str

class DescribeAppRequestTypeDef(TypedDict):
    appArn: str

DescribeAppVersionAppComponentRequestTypeDef = TypedDict(
    "DescribeAppVersionAppComponentRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "id": str,
    },
)

class DescribeAppVersionRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str

class DescribeAppVersionResourcesResolutionStatusRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str
    resolutionId: NotRequired[str]

class DescribeAppVersionTemplateRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str

class DescribeDraftAppVersionResourcesImportStatusRequestTypeDef(TypedDict):
    appArn: str

class ErrorDetailTypeDef(TypedDict):
    errorMessage: NotRequired[str]

class DescribeMetricsExportRequestTypeDef(TypedDict):
    metricsExportId: str

class S3LocationTypeDef(TypedDict):
    bucket: NotRequired[str]
    prefix: NotRequired[str]

class DescribeResiliencyPolicyRequestTypeDef(TypedDict):
    policyArn: str

class DescribeResourceGroupingRecommendationTaskRequestTypeDef(TypedDict):
    appArn: str
    groupingId: NotRequired[str]

class EksSourceOutputTypeDef(TypedDict):
    eksClusterArn: str
    namespaces: List[str]

class EksSourceTypeDef(TypedDict):
    eksClusterArn: str
    namespaces: Sequence[str]

class ExperimentTypeDef(TypedDict):
    experimentArn: NotRequired[str]
    experimentTemplateId: NotRequired[str]

class FieldTypeDef(TypedDict):
    name: str
    aggregation: NotRequired[FieldAggregationTypeType]

class GroupingAppComponentTypeDef(TypedDict):
    appComponentId: str
    appComponentName: str
    appComponentType: str

PhysicalResourceIdTypeDef = TypedDict(
    "PhysicalResourceIdTypeDef",
    {
        "identifier": str,
        "type": PhysicalIdentifierTypeType,
        "awsAccountId": NotRequired[str],
        "awsRegion": NotRequired[str],
    },
)

class ListAlarmRecommendationsRequestTypeDef(TypedDict):
    assessmentArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAppAssessmentComplianceDriftsRequestTypeDef(TypedDict):
    assessmentArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAppAssessmentResourceDriftsRequestTypeDef(TypedDict):
    assessmentArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAppAssessmentsRequestTypeDef(TypedDict):
    appArn: NotRequired[str]
    assessmentName: NotRequired[str]
    assessmentStatus: NotRequired[Sequence[AssessmentStatusType]]
    complianceStatus: NotRequired[ComplianceStatusType]
    invoker: NotRequired[AssessmentInvokerType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    reverseOrder: NotRequired[bool]

class ListAppComponentCompliancesRequestTypeDef(TypedDict):
    assessmentArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAppComponentRecommendationsRequestTypeDef(TypedDict):
    assessmentArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAppInputSourcesRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAppVersionAppComponentsRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAppVersionResourceMappingsRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAppVersionResourcesRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    resolutionId: NotRequired[str]

TimestampTypeDef = Union[datetime, str]

class SortTypeDef(TypedDict):
    field: str
    ascending: NotRequired[bool]

class ListRecommendationTemplatesRequestTypeDef(TypedDict):
    assessmentArn: NotRequired[str]
    maxResults: NotRequired[int]
    name: NotRequired[str]
    nextToken: NotRequired[str]
    recommendationTemplateArn: NotRequired[str]
    reverseOrder: NotRequired[bool]
    status: NotRequired[Sequence[RecommendationTemplateStatusType]]

class ListResiliencyPoliciesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    policyName: NotRequired[str]

class ListResourceGroupingRecommendationsRequestTypeDef(TypedDict):
    appArn: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSopRecommendationsRequestTypeDef(TypedDict):
    assessmentArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSuggestedResiliencyPoliciesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTestRecommendationsRequestTypeDef(TypedDict):
    assessmentArn: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListUnsupportedAppVersionResourcesRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    resolutionId: NotRequired[str]

PermissionModelTypeDef = TypedDict(
    "PermissionModelTypeDef",
    {
        "type": PermissionModelTypeType,
        "crossAccountRoleArns": NotRequired[Sequence[str]],
        "invokerRoleName": NotRequired[str],
    },
)

class PublishAppVersionRequestTypeDef(TypedDict):
    appArn: str
    versionName: NotRequired[str]

class PutDraftAppVersionTemplateRequestTypeDef(TypedDict):
    appArn: str
    appTemplateBody: str

class RejectGroupingRecommendationEntryTypeDef(TypedDict):
    groupingRecommendationId: str
    rejectionReason: NotRequired[GroupingRecommendationRejectionReasonType]

class RemoveDraftAppVersionResourceMappingsRequestTypeDef(TypedDict):
    appArn: str
    appRegistryAppNames: NotRequired[Sequence[str]]
    eksSourceNames: NotRequired[Sequence[str]]
    logicalStackNames: NotRequired[Sequence[str]]
    resourceGroupNames: NotRequired[Sequence[str]]
    resourceNames: NotRequired[Sequence[str]]
    terraformSourceNames: NotRequired[Sequence[str]]

class ScoringComponentResiliencyScoreTypeDef(TypedDict):
    excludedCount: NotRequired[int]
    outstandingCount: NotRequired[int]
    possibleScore: NotRequired[float]
    score: NotRequired[float]

class ResolveAppVersionResourcesRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str

class ResourceErrorTypeDef(TypedDict):
    logicalResourceId: NotRequired[str]
    physicalResourceId: NotRequired[str]
    reason: NotRequired[str]

class StartAppAssessmentRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str
    assessmentName: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class StartMetricsExportRequestTypeDef(TypedDict):
    bucketName: NotRequired[str]
    clientToken: NotRequired[str]

class StartResourceGroupingRecommendationTaskRequestTypeDef(TypedDict):
    appArn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

UpdateAppVersionAppComponentRequestTypeDef = TypedDict(
    "UpdateAppVersionAppComponentRequestTypeDef",
    {
        "appArn": str,
        "id": str,
        "additionalInfo": NotRequired[Mapping[str, Sequence[str]]],
        "name": NotRequired[str],
        "type": NotRequired[str],
    },
)

class UpdateAppVersionRequestTypeDef(TypedDict):
    appArn: str
    additionalInfo: NotRequired[Mapping[str, Sequence[str]]]

class AcceptResourceGroupingRecommendationsRequestTypeDef(TypedDict):
    appArn: str
    entries: Sequence[AcceptGroupingRecommendationEntryTypeDef]

class AcceptResourceGroupingRecommendationsResponseTypeDef(TypedDict):
    appArn: str
    failedEntries: List[FailedGroupingRecommendationEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppAssessmentResponseTypeDef(TypedDict):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppResponseTypeDef(TypedDict):
    appArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRecommendationTemplateResponseTypeDef(TypedDict):
    recommendationTemplateArn: str
    status: RecommendationTemplateStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResiliencyPolicyResponseTypeDef(TypedDict):
    policyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionResourcesResolutionStatusResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    errorMessage: str
    resolutionId: str
    status: ResourceResolutionStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionResponseTypeDef(TypedDict):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionTemplateResponseTypeDef(TypedDict):
    appArn: str
    appTemplateBody: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourceGroupingRecommendationTaskResponseTypeDef(TypedDict):
    errorMessage: str
    groupingId: str
    status: ResourcesGroupingRecGenStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ListMetricsResponseTypeDef(TypedDict):
    rows: List[List[str]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishAppVersionResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    identifier: int
    versionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutDraftAppVersionTemplateResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectResourceGroupingRecommendationsResponseTypeDef(TypedDict):
    appArn: str
    failedEntries: List[FailedGroupingRecommendationEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveDraftAppVersionResourceMappingsResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveAppVersionResourcesResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    resolutionId: str
    status: ResourceResolutionStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class StartMetricsExportResponseTypeDef(TypedDict):
    metricsExportId: str
    status: MetricsExportStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceGroupingRecommendationTaskResponseTypeDef(TypedDict):
    appArn: str
    errorMessage: str
    groupingId: str
    status: ResourcesGroupingRecGenStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppVersionResponseTypeDef(TypedDict):
    additionalInfo: Dict[str, List[str]]
    appArn: str
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppAssessmentSummaryTypeDef(TypedDict):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    appArn: NotRequired[str]
    appVersion: NotRequired[str]
    assessmentName: NotRequired[str]
    complianceStatus: NotRequired[ComplianceStatusType]
    cost: NotRequired[CostTypeDef]
    driftStatus: NotRequired[DriftStatusType]
    endTime: NotRequired[datetime]
    invoker: NotRequired[AssessmentInvokerType]
    message: NotRequired[str]
    resiliencyScore: NotRequired[float]
    startTime: NotRequired[datetime]
    versionName: NotRequired[str]

class ComplianceDriftTypeDef(TypedDict):
    actualReferenceId: NotRequired[str]
    actualValue: NotRequired[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]]
    appId: NotRequired[str]
    appVersion: NotRequired[str]
    diffType: NotRequired[DifferenceTypeType]
    driftType: NotRequired[DriftTypeType]
    entityId: NotRequired[str]
    entityType: NotRequired[str]
    expectedReferenceId: NotRequired[str]
    expectedValue: NotRequired[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]]

class CreateAppVersionAppComponentResponseTypeDef(TypedDict):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppVersionAppComponentResponseTypeDef(TypedDict):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionAppComponentResponseTypeDef(TypedDict):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppVersionAppComponentsResponseTypeDef(TypedDict):
    appArn: str
    appComponents: List[AppComponentTypeDef]
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateAppVersionAppComponentResponseTypeDef(TypedDict):
    appArn: str
    appComponent: AppComponentTypeDef
    appVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class AppInputSourceTypeDef(TypedDict):
    importType: ResourceMappingTypeType
    eksSourceClusterNamespace: NotRequired[EksSourceClusterNamespaceTypeDef]
    resourceCount: NotRequired[int]
    sourceArn: NotRequired[str]
    sourceName: NotRequired[str]
    terraformSource: NotRequired[TerraformSourceTypeDef]

class DeleteAppInputSourceRequestTypeDef(TypedDict):
    appArn: str
    clientToken: NotRequired[str]
    eksSourceClusterNamespace: NotRequired[EksSourceClusterNamespaceTypeDef]
    sourceArn: NotRequired[str]
    terraformSource: NotRequired[TerraformSourceTypeDef]

class ListAppsResponseTypeDef(TypedDict):
    appSummaries: List[AppSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AppTypeDef(TypedDict):
    appArn: str
    creationTime: datetime
    name: str
    assessmentSchedule: NotRequired[AppAssessmentScheduleTypeType]
    awsApplicationArn: NotRequired[str]
    complianceStatus: NotRequired[AppComplianceStatusTypeType]
    description: NotRequired[str]
    driftStatus: NotRequired[AppDriftStatusTypeType]
    eventSubscriptions: NotRequired[List[EventSubscriptionTypeDef]]
    lastAppComplianceEvaluationTime: NotRequired[datetime]
    lastDriftEvaluationTime: NotRequired[datetime]
    lastResiliencyScoreEvaluationTime: NotRequired[datetime]
    permissionModel: NotRequired[PermissionModelOutputTypeDef]
    policyArn: NotRequired[str]
    resiliencyScore: NotRequired[float]
    rpoInSecs: NotRequired[int]
    rtoInSecs: NotRequired[int]
    status: NotRequired[AppStatusTypeType]
    tags: NotRequired[Dict[str, str]]

class ListAppVersionsResponseTypeDef(TypedDict):
    appVersions: List[AppVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AssessmentSummaryTypeDef(TypedDict):
    riskRecommendations: NotRequired[List[AssessmentRiskRecommendationTypeDef]]
    summary: NotRequired[str]

class BatchUpdateRecommendationStatusSuccessfulEntryTypeDef(TypedDict):
    entryId: str
    excluded: bool
    referenceId: str
    appComponentId: NotRequired[str]
    excludeReason: NotRequired[ExcludeRecommendationReasonType]
    item: NotRequired[UpdateRecommendationStatusItemTypeDef]

class UpdateRecommendationStatusRequestEntryTypeDef(TypedDict):
    entryId: str
    excluded: bool
    referenceId: str
    appComponentId: NotRequired[str]
    excludeReason: NotRequired[ExcludeRecommendationReasonType]
    item: NotRequired[UpdateRecommendationStatusItemTypeDef]

class ConfigRecommendationTypeDef(TypedDict):
    name: str
    optimizationType: ConfigRecommendationOptimizationTypeType
    referenceId: str
    appComponentName: NotRequired[str]
    compliance: NotRequired[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]]
    cost: NotRequired[CostTypeDef]
    description: NotRequired[str]
    haArchitecture: NotRequired[HaArchitectureType]
    recommendationCompliance: NotRequired[
        Dict[DisruptionTypeType, RecommendationDisruptionComplianceTypeDef]
    ]
    suggestedChanges: NotRequired[List[str]]

class CreateAppVersionResourceRequestTypeDef(TypedDict):
    appArn: str
    appComponents: Sequence[str]
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: str
    resourceType: str
    additionalInfo: NotRequired[Mapping[str, Sequence[str]]]
    awsAccountId: NotRequired[str]
    awsRegion: NotRequired[str]
    clientToken: NotRequired[str]
    resourceName: NotRequired[str]

class DeleteAppVersionResourceRequestTypeDef(TypedDict):
    appArn: str
    awsAccountId: NotRequired[str]
    awsRegion: NotRequired[str]
    clientToken: NotRequired[str]
    logicalResourceId: NotRequired[LogicalResourceIdTypeDef]
    physicalResourceId: NotRequired[str]
    resourceName: NotRequired[str]

class DescribeAppVersionResourceRequestTypeDef(TypedDict):
    appArn: str
    appVersion: str
    awsAccountId: NotRequired[str]
    awsRegion: NotRequired[str]
    logicalResourceId: NotRequired[LogicalResourceIdTypeDef]
    physicalResourceId: NotRequired[str]
    resourceName: NotRequired[str]

class ResourceIdentifierTypeDef(TypedDict):
    logicalResourceId: NotRequired[LogicalResourceIdTypeDef]
    resourceType: NotRequired[str]

class UpdateAppVersionResourceRequestTypeDef(TypedDict):
    appArn: str
    additionalInfo: NotRequired[Mapping[str, Sequence[str]]]
    appComponents: NotRequired[Sequence[str]]
    awsAccountId: NotRequired[str]
    awsRegion: NotRequired[str]
    excluded: NotRequired[bool]
    logicalResourceId: NotRequired[LogicalResourceIdTypeDef]
    physicalResourceId: NotRequired[str]
    resourceName: NotRequired[str]
    resourceType: NotRequired[str]

class CreateResiliencyPolicyRequestTypeDef(TypedDict):
    policy: Mapping[DisruptionTypeType, FailurePolicyTypeDef]
    policyName: str
    tier: ResiliencyPolicyTierType
    clientToken: NotRequired[str]
    dataLocationConstraint: NotRequired[DataLocationConstraintType]
    policyDescription: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class ResiliencyPolicyTypeDef(TypedDict):
    creationTime: NotRequired[datetime]
    dataLocationConstraint: NotRequired[DataLocationConstraintType]
    estimatedCostTier: NotRequired[EstimatedCostTierType]
    policy: NotRequired[Dict[DisruptionTypeType, FailurePolicyTypeDef]]
    policyArn: NotRequired[str]
    policyDescription: NotRequired[str]
    policyName: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    tier: NotRequired[ResiliencyPolicyTierType]

class UpdateResiliencyPolicyRequestTypeDef(TypedDict):
    policyArn: str
    dataLocationConstraint: NotRequired[DataLocationConstraintType]
    policy: NotRequired[Mapping[DisruptionTypeType, FailurePolicyTypeDef]]
    policyDescription: NotRequired[str]
    policyName: NotRequired[str]
    tier: NotRequired[ResiliencyPolicyTierType]

class DescribeDraftAppVersionResourcesImportStatusResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    errorDetails: List[ErrorDetailTypeDef]
    errorMessage: str
    status: ResourceImportStatusTypeType
    statusChangeTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetricsExportResponseTypeDef(TypedDict):
    errorMessage: str
    exportLocation: S3LocationTypeDef
    metricsExportId: str
    status: MetricsExportStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

RecommendationTemplateTypeDef = TypedDict(
    "RecommendationTemplateTypeDef",
    {
        "assessmentArn": str,
        "format": TemplateFormatType,
        "name": str,
        "recommendationTemplateArn": str,
        "recommendationTypes": List[RenderRecommendationTypeType],
        "status": RecommendationTemplateStatusType,
        "appArn": NotRequired[str],
        "endTime": NotRequired[datetime],
        "message": NotRequired[str],
        "needsReplacements": NotRequired[bool],
        "recommendationIds": NotRequired[List[str]],
        "startTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
        "templatesLocation": NotRequired[S3LocationTypeDef],
    },
)

class ImportResourcesToDraftAppVersionResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    eksSources: List[EksSourceOutputTypeDef]
    sourceArns: List[str]
    status: ResourceImportStatusTypeType
    terraformSources: List[TerraformSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

EksSourceUnionTypeDef = Union[EksSourceTypeDef, EksSourceOutputTypeDef]

class RecommendationItemTypeDef(TypedDict):
    alreadyImplemented: NotRequired[bool]
    discoveredAlarm: NotRequired[AlarmTypeDef]
    excludeReason: NotRequired[ExcludeRecommendationReasonType]
    excluded: NotRequired[bool]
    latestDiscoveredExperiment: NotRequired[ExperimentTypeDef]
    resourceId: NotRequired[str]
    targetAccountId: NotRequired[str]
    targetRegion: NotRequired[str]

class GroupingResourceTypeDef(TypedDict):
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: PhysicalResourceIdTypeDef
    resourceName: str
    resourceType: str
    sourceAppComponentIds: List[str]

class PhysicalResourceTypeDef(TypedDict):
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: PhysicalResourceIdTypeDef
    resourceType: str
    additionalInfo: NotRequired[Dict[str, List[str]]]
    appComponents: NotRequired[List[AppComponentTypeDef]]
    excluded: NotRequired[bool]
    parentResourceName: NotRequired[str]
    resourceName: NotRequired[str]
    sourceType: NotRequired[ResourceSourceTypeType]

class ResourceMappingTypeDef(TypedDict):
    mappingType: ResourceMappingTypeType
    physicalResourceId: PhysicalResourceIdTypeDef
    appRegistryAppName: NotRequired[str]
    eksSourceName: NotRequired[str]
    logicalStackName: NotRequired[str]
    resourceGroupName: NotRequired[str]
    resourceName: NotRequired[str]
    terraformSourceName: NotRequired[str]

class UnsupportedResourceTypeDef(TypedDict):
    logicalResourceId: LogicalResourceIdTypeDef
    physicalResourceId: PhysicalResourceIdTypeDef
    resourceType: str
    unsupportedResourceStatus: NotRequired[str]

class ListAppAssessmentResourceDriftsRequestPaginateTypeDef(TypedDict):
    assessmentArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceGroupingRecommendationsRequestPaginateTypeDef(TypedDict):
    appArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAppVersionsRequestTypeDef(TypedDict):
    appArn: str
    endTime: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]

class ListAppsRequestTypeDef(TypedDict):
    appArn: NotRequired[str]
    awsApplicationArn: NotRequired[str]
    fromLastAssessmentTime: NotRequired[TimestampTypeDef]
    maxResults: NotRequired[int]
    name: NotRequired[str]
    nextToken: NotRequired[str]
    reverseOrder: NotRequired[bool]
    toLastAssessmentTime: NotRequired[TimestampTypeDef]

class ListMetricsRequestPaginateTypeDef(TypedDict):
    conditions: NotRequired[Sequence[ConditionTypeDef]]
    dataSource: NotRequired[str]
    fields: NotRequired[Sequence[FieldTypeDef]]
    sorts: NotRequired[Sequence[SortTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMetricsRequestTypeDef(TypedDict):
    conditions: NotRequired[Sequence[ConditionTypeDef]]
    dataSource: NotRequired[str]
    fields: NotRequired[Sequence[FieldTypeDef]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sorts: NotRequired[Sequence[SortTypeDef]]

PermissionModelUnionTypeDef = Union[PermissionModelTypeDef, PermissionModelOutputTypeDef]

class RejectResourceGroupingRecommendationsRequestTypeDef(TypedDict):
    appArn: str
    entries: Sequence[RejectGroupingRecommendationEntryTypeDef]

class ResiliencyScoreTypeDef(TypedDict):
    disruptionScore: Dict[DisruptionTypeType, float]
    score: float
    componentScore: NotRequired[
        Dict[ResiliencyScoreTypeType, ScoringComponentResiliencyScoreTypeDef]
    ]

class ResourceErrorsDetailsTypeDef(TypedDict):
    hasMoreErrors: NotRequired[bool]
    resourceErrors: NotRequired[List[ResourceErrorTypeDef]]

class ListAppAssessmentsResponseTypeDef(TypedDict):
    assessmentSummaries: List[AppAssessmentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAppAssessmentComplianceDriftsResponseTypeDef(TypedDict):
    complianceDrifts: List[ComplianceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DeleteAppInputSourceResponseTypeDef(TypedDict):
    appArn: str
    appInputSource: AppInputSourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInputSourcesResponseTypeDef(TypedDict):
    appInputSources: List[AppInputSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateAppResponseTypeDef(TypedDict):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppResponseTypeDef(TypedDict):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppResponseTypeDef(TypedDict):
    app: AppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRecommendationStatusResponseTypeDef(TypedDict):
    appArn: str
    failedEntries: List[BatchUpdateRecommendationStatusFailedEntryTypeDef]
    successfulEntries: List[BatchUpdateRecommendationStatusSuccessfulEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRecommendationStatusRequestTypeDef(TypedDict):
    appArn: str
    requestEntries: Sequence[UpdateRecommendationStatusRequestEntryTypeDef]

class ComponentRecommendationTypeDef(TypedDict):
    appComponentName: str
    configRecommendations: List[ConfigRecommendationTypeDef]
    recommendationStatus: RecommendationComplianceStatusType

class ResourceDriftTypeDef(TypedDict):
    appArn: NotRequired[str]
    appVersion: NotRequired[str]
    diffType: NotRequired[DifferenceTypeType]
    referenceId: NotRequired[str]
    resourceIdentifier: NotRequired[ResourceIdentifierTypeDef]

class CreateResiliencyPolicyResponseTypeDef(TypedDict):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResiliencyPolicyResponseTypeDef(TypedDict):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResiliencyPoliciesResponseTypeDef(TypedDict):
    resiliencyPolicies: List[ResiliencyPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSuggestedResiliencyPoliciesResponseTypeDef(TypedDict):
    resiliencyPolicies: List[ResiliencyPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateResiliencyPolicyResponseTypeDef(TypedDict):
    policy: ResiliencyPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecommendationTemplateResponseTypeDef(TypedDict):
    recommendationTemplate: RecommendationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecommendationTemplatesResponseTypeDef(TypedDict):
    recommendationTemplates: List[RecommendationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ImportResourcesToDraftAppVersionRequestTypeDef(TypedDict):
    appArn: str
    eksSources: NotRequired[Sequence[EksSourceUnionTypeDef]]
    importStrategy: NotRequired[ResourceImportStrategyTypeType]
    sourceArns: NotRequired[Sequence[str]]
    terraformSources: NotRequired[Sequence[TerraformSourceTypeDef]]

AlarmRecommendationTypeDef = TypedDict(
    "AlarmRecommendationTypeDef",
    {
        "name": str,
        "recommendationId": str,
        "referenceId": str,
        "type": AlarmTypeType,
        "appComponentName": NotRequired[str],
        "appComponentNames": NotRequired[List[str]],
        "description": NotRequired[str],
        "items": NotRequired[List[RecommendationItemTypeDef]],
        "prerequisite": NotRequired[str],
        "recommendationStatus": NotRequired[RecommendationStatusType],
    },
)

class SopRecommendationTypeDef(TypedDict):
    recommendationId: str
    referenceId: str
    serviceType: Literal["SSM"]
    appComponentName: NotRequired[str]
    description: NotRequired[str]
    items: NotRequired[List[RecommendationItemTypeDef]]
    name: NotRequired[str]
    prerequisite: NotRequired[str]
    recommendationStatus: NotRequired[RecommendationStatusType]

TestRecommendationTypeDef = TypedDict(
    "TestRecommendationTypeDef",
    {
        "referenceId": str,
        "appComponentId": NotRequired[str],
        "appComponentName": NotRequired[str],
        "dependsOnAlarms": NotRequired[List[str]],
        "description": NotRequired[str],
        "intent": NotRequired[str],
        "items": NotRequired[List[RecommendationItemTypeDef]],
        "name": NotRequired[str],
        "prerequisite": NotRequired[str],
        "recommendationId": NotRequired[str],
        "recommendationStatus": NotRequired[RecommendationStatusType],
        "risk": NotRequired[TestRiskType],
        "type": NotRequired[TestTypeType],
    },
)

class GroupingRecommendationTypeDef(TypedDict):
    confidenceLevel: GroupingRecommendationConfidenceLevelType
    creationTime: datetime
    groupingAppComponent: GroupingAppComponentTypeDef
    groupingRecommendationId: str
    recommendationReasons: List[str]
    resources: List[GroupingResourceTypeDef]
    score: float
    status: GroupingRecommendationStatusTypeType
    rejectionReason: NotRequired[GroupingRecommendationRejectionReasonType]

class CreateAppVersionResourceResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAppVersionResourceResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppVersionResourceResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppVersionResourcesResponseTypeDef(TypedDict):
    physicalResources: List[PhysicalResourceTypeDef]
    resolutionId: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdateAppVersionResourceResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    physicalResource: PhysicalResourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddDraftAppVersionResourceMappingsRequestTypeDef(TypedDict):
    appArn: str
    resourceMappings: Sequence[ResourceMappingTypeDef]

class AddDraftAppVersionResourceMappingsResponseTypeDef(TypedDict):
    appArn: str
    appVersion: str
    resourceMappings: List[ResourceMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppVersionResourceMappingsResponseTypeDef(TypedDict):
    resourceMappings: List[ResourceMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListUnsupportedAppVersionResourcesResponseTypeDef(TypedDict):
    resolutionId: str
    unsupportedResources: List[UnsupportedResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateAppRequestTypeDef(TypedDict):
    name: str
    assessmentSchedule: NotRequired[AppAssessmentScheduleTypeType]
    awsApplicationArn: NotRequired[str]
    clientToken: NotRequired[str]
    description: NotRequired[str]
    eventSubscriptions: NotRequired[Sequence[EventSubscriptionTypeDef]]
    permissionModel: NotRequired[PermissionModelUnionTypeDef]
    policyArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateAppRequestTypeDef(TypedDict):
    appArn: str
    assessmentSchedule: NotRequired[AppAssessmentScheduleTypeType]
    clearResiliencyPolicyArn: NotRequired[bool]
    description: NotRequired[str]
    eventSubscriptions: NotRequired[Sequence[EventSubscriptionTypeDef]]
    permissionModel: NotRequired[PermissionModelUnionTypeDef]
    policyArn: NotRequired[str]

class AppComponentComplianceTypeDef(TypedDict):
    appComponentName: NotRequired[str]
    compliance: NotRequired[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]]
    cost: NotRequired[CostTypeDef]
    message: NotRequired[str]
    resiliencyScore: NotRequired[ResiliencyScoreTypeDef]
    status: NotRequired[ComplianceStatusType]

class AppAssessmentTypeDef(TypedDict):
    assessmentArn: str
    assessmentStatus: AssessmentStatusType
    invoker: AssessmentInvokerType
    appArn: NotRequired[str]
    appVersion: NotRequired[str]
    assessmentName: NotRequired[str]
    compliance: NotRequired[Dict[DisruptionTypeType, DisruptionComplianceTypeDef]]
    complianceStatus: NotRequired[ComplianceStatusType]
    cost: NotRequired[CostTypeDef]
    driftStatus: NotRequired[DriftStatusType]
    endTime: NotRequired[datetime]
    message: NotRequired[str]
    policy: NotRequired[ResiliencyPolicyTypeDef]
    resiliencyScore: NotRequired[ResiliencyScoreTypeDef]
    resourceErrorsDetails: NotRequired[ResourceErrorsDetailsTypeDef]
    startTime: NotRequired[datetime]
    summary: NotRequired[AssessmentSummaryTypeDef]
    tags: NotRequired[Dict[str, str]]
    versionName: NotRequired[str]

class ListAppComponentRecommendationsResponseTypeDef(TypedDict):
    componentRecommendations: List[ComponentRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAppAssessmentResourceDriftsResponseTypeDef(TypedDict):
    resourceDrifts: List[ResourceDriftTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAlarmRecommendationsResponseTypeDef(TypedDict):
    alarmRecommendations: List[AlarmRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSopRecommendationsResponseTypeDef(TypedDict):
    sopRecommendations: List[SopRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTestRecommendationsResponseTypeDef(TypedDict):
    testRecommendations: List[TestRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResourceGroupingRecommendationsResponseTypeDef(TypedDict):
    groupingRecommendations: List[GroupingRecommendationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAppComponentCompliancesResponseTypeDef(TypedDict):
    componentCompliances: List[AppComponentComplianceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeAppAssessmentResponseTypeDef(TypedDict):
    assessment: AppAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartAppAssessmentResponseTypeDef(TypedDict):
    assessment: AppAssessmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
