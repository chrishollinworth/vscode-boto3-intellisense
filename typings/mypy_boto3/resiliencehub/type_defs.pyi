"""
Type annotations for resiliencehub service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/type_defs.html)

Usage::

    ```python
    from mypy_boto3_resiliencehub.type_defs import AddDraftAppVersionResourceMappingsRequestRequestTypeDef

    data: AddDraftAppVersionResourceMappingsRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AlarmTypeType,
    AppAssessmentScheduleTypeType,
    AppComplianceStatusTypeType,
    AppDriftStatusTypeType,
    AppStatusTypeType,
    AssessmentInvokerType,
    AssessmentStatusType,
    ComplianceStatusType,
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
    HaArchitectureType,
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
    ResourceSourceTypeType,
    TemplateFormatType,
    TestRiskType,
    TestTypeType,
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
    "AddDraftAppVersionResourceMappingsRequestRequestTypeDef",
    "AddDraftAppVersionResourceMappingsResponseTypeDef",
    "AlarmRecommendationTypeDef",
    "AppAssessmentSummaryTypeDef",
    "AppAssessmentTypeDef",
    "AppComponentComplianceTypeDef",
    "AppComponentTypeDef",
    "AppInputSourceTypeDef",
    "AppSummaryTypeDef",
    "AppTypeDef",
    "AppVersionSummaryTypeDef",
    "BatchUpdateRecommendationStatusFailedEntryTypeDef",
    "BatchUpdateRecommendationStatusRequestRequestTypeDef",
    "BatchUpdateRecommendationStatusResponseTypeDef",
    "BatchUpdateRecommendationStatusSuccessfulEntryTypeDef",
    "ComplianceDriftTypeDef",
    "ComponentRecommendationTypeDef",
    "ConfigRecommendationTypeDef",
    "CostTypeDef",
    "CreateAppRequestRequestTypeDef",
    "CreateAppResponseTypeDef",
    "CreateAppVersionAppComponentRequestRequestTypeDef",
    "CreateAppVersionAppComponentResponseTypeDef",
    "CreateAppVersionResourceRequestRequestTypeDef",
    "CreateAppVersionResourceResponseTypeDef",
    "CreateRecommendationTemplateRequestRequestTypeDef",
    "CreateRecommendationTemplateResponseTypeDef",
    "CreateResiliencyPolicyRequestRequestTypeDef",
    "CreateResiliencyPolicyResponseTypeDef",
    "DeleteAppAssessmentRequestRequestTypeDef",
    "DeleteAppAssessmentResponseTypeDef",
    "DeleteAppInputSourceRequestRequestTypeDef",
    "DeleteAppInputSourceResponseTypeDef",
    "DeleteAppRequestRequestTypeDef",
    "DeleteAppResponseTypeDef",
    "DeleteAppVersionAppComponentRequestRequestTypeDef",
    "DeleteAppVersionAppComponentResponseTypeDef",
    "DeleteAppVersionResourceRequestRequestTypeDef",
    "DeleteAppVersionResourceResponseTypeDef",
    "DeleteRecommendationTemplateRequestRequestTypeDef",
    "DeleteRecommendationTemplateResponseTypeDef",
    "DeleteResiliencyPolicyRequestRequestTypeDef",
    "DeleteResiliencyPolicyResponseTypeDef",
    "DescribeAppAssessmentRequestRequestTypeDef",
    "DescribeAppAssessmentResponseTypeDef",
    "DescribeAppRequestRequestTypeDef",
    "DescribeAppResponseTypeDef",
    "DescribeAppVersionAppComponentRequestRequestTypeDef",
    "DescribeAppVersionAppComponentResponseTypeDef",
    "DescribeAppVersionRequestRequestTypeDef",
    "DescribeAppVersionResourceRequestRequestTypeDef",
    "DescribeAppVersionResourceResponseTypeDef",
    "DescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef",
    "DescribeAppVersionResourcesResolutionStatusResponseTypeDef",
    "DescribeAppVersionResponseTypeDef",
    "DescribeAppVersionTemplateRequestRequestTypeDef",
    "DescribeAppVersionTemplateResponseTypeDef",
    "DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef",
    "DescribeDraftAppVersionResourcesImportStatusResponseTypeDef",
    "DescribeResiliencyPolicyRequestRequestTypeDef",
    "DescribeResiliencyPolicyResponseTypeDef",
    "DisruptionComplianceTypeDef",
    "EksSourceClusterNamespaceTypeDef",
    "EksSourceTypeDef",
    "EventSubscriptionTypeDef",
    "FailurePolicyTypeDef",
    "ImportResourcesToDraftAppVersionRequestRequestTypeDef",
    "ImportResourcesToDraftAppVersionResponseTypeDef",
    "ListAlarmRecommendationsRequestRequestTypeDef",
    "ListAlarmRecommendationsResponseTypeDef",
    "ListAppAssessmentComplianceDriftsRequestRequestTypeDef",
    "ListAppAssessmentComplianceDriftsResponseTypeDef",
    "ListAppAssessmentResourceDriftsRequestRequestTypeDef",
    "ListAppAssessmentResourceDriftsResponseTypeDef",
    "ListAppAssessmentsRequestRequestTypeDef",
    "ListAppAssessmentsResponseTypeDef",
    "ListAppComponentCompliancesRequestRequestTypeDef",
    "ListAppComponentCompliancesResponseTypeDef",
    "ListAppComponentRecommendationsRequestRequestTypeDef",
    "ListAppComponentRecommendationsResponseTypeDef",
    "ListAppInputSourcesRequestRequestTypeDef",
    "ListAppInputSourcesResponseTypeDef",
    "ListAppVersionAppComponentsRequestRequestTypeDef",
    "ListAppVersionAppComponentsResponseTypeDef",
    "ListAppVersionResourceMappingsRequestRequestTypeDef",
    "ListAppVersionResourceMappingsResponseTypeDef",
    "ListAppVersionResourcesRequestRequestTypeDef",
    "ListAppVersionResourcesResponseTypeDef",
    "ListAppVersionsRequestRequestTypeDef",
    "ListAppVersionsResponseTypeDef",
    "ListAppsRequestRequestTypeDef",
    "ListAppsResponseTypeDef",
    "ListRecommendationTemplatesRequestRequestTypeDef",
    "ListRecommendationTemplatesResponseTypeDef",
    "ListResiliencyPoliciesRequestRequestTypeDef",
    "ListResiliencyPoliciesResponseTypeDef",
    "ListSopRecommendationsRequestRequestTypeDef",
    "ListSopRecommendationsResponseTypeDef",
    "ListSuggestedResiliencyPoliciesRequestRequestTypeDef",
    "ListSuggestedResiliencyPoliciesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestRecommendationsRequestRequestTypeDef",
    "ListTestRecommendationsResponseTypeDef",
    "ListUnsupportedAppVersionResourcesRequestRequestTypeDef",
    "ListUnsupportedAppVersionResourcesResponseTypeDef",
    "LogicalResourceIdTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionModelTypeDef",
    "PhysicalResourceIdTypeDef",
    "PhysicalResourceTypeDef",
    "PublishAppVersionRequestRequestTypeDef",
    "PublishAppVersionResponseTypeDef",
    "PutDraftAppVersionTemplateRequestRequestTypeDef",
    "PutDraftAppVersionTemplateResponseTypeDef",
    "RecommendationDisruptionComplianceTypeDef",
    "RecommendationItemTypeDef",
    "RecommendationTemplateTypeDef",
    "RemoveDraftAppVersionResourceMappingsRequestRequestTypeDef",
    "RemoveDraftAppVersionResourceMappingsResponseTypeDef",
    "ResiliencyPolicyTypeDef",
    "ResiliencyScoreTypeDef",
    "ResolveAppVersionResourcesRequestRequestTypeDef",
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
    "StartAppAssessmentRequestRequestTypeDef",
    "StartAppAssessmentResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TerraformSourceTypeDef",
    "TestRecommendationTypeDef",
    "UnsupportedResourceTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAppRequestRequestTypeDef",
    "UpdateAppResponseTypeDef",
    "UpdateAppVersionAppComponentRequestRequestTypeDef",
    "UpdateAppVersionAppComponentResponseTypeDef",
    "UpdateAppVersionRequestRequestTypeDef",
    "UpdateAppVersionResourceRequestRequestTypeDef",
    "UpdateAppVersionResourceResponseTypeDef",
    "UpdateAppVersionResponseTypeDef",
    "UpdateRecommendationStatusItemTypeDef",
    "UpdateRecommendationStatusRequestEntryTypeDef",
    "UpdateResiliencyPolicyRequestRequestTypeDef",
    "UpdateResiliencyPolicyResponseTypeDef",
)

AddDraftAppVersionResourceMappingsRequestRequestTypeDef = TypedDict(
    "AddDraftAppVersionResourceMappingsRequestRequestTypeDef",
    {
        "appArn": str,
        "resourceMappings": List["ResourceMappingTypeDef"],
    },
)

AddDraftAppVersionResourceMappingsResponseTypeDef = TypedDict(
    "AddDraftAppVersionResourceMappingsResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "resourceMappings": List["ResourceMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAlarmRecommendationTypeDef = TypedDict(
    "_RequiredAlarmRecommendationTypeDef",
    {
        "name": str,
        "recommendationId": str,
        "referenceId": str,
        "type": AlarmTypeType,
    },
)
_OptionalAlarmRecommendationTypeDef = TypedDict(
    "_OptionalAlarmRecommendationTypeDef",
    {
        "appComponentName": str,
        "appComponentNames": List[str],
        "description": str,
        "items": List["RecommendationItemTypeDef"],
        "prerequisite": str,
        "recommendationStatus": RecommendationStatusType,
    },
    total=False,
)

class AlarmRecommendationTypeDef(
    _RequiredAlarmRecommendationTypeDef, _OptionalAlarmRecommendationTypeDef
):
    pass

_RequiredAppAssessmentSummaryTypeDef = TypedDict(
    "_RequiredAppAssessmentSummaryTypeDef",
    {
        "assessmentArn": str,
        "assessmentStatus": AssessmentStatusType,
    },
)
_OptionalAppAssessmentSummaryTypeDef = TypedDict(
    "_OptionalAppAssessmentSummaryTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "assessmentName": str,
        "complianceStatus": ComplianceStatusType,
        "cost": "CostTypeDef",
        "driftStatus": DriftStatusType,
        "endTime": datetime,
        "invoker": AssessmentInvokerType,
        "message": str,
        "resiliencyScore": float,
        "startTime": datetime,
        "versionName": str,
    },
    total=False,
)

class AppAssessmentSummaryTypeDef(
    _RequiredAppAssessmentSummaryTypeDef, _OptionalAppAssessmentSummaryTypeDef
):
    pass

_RequiredAppAssessmentTypeDef = TypedDict(
    "_RequiredAppAssessmentTypeDef",
    {
        "assessmentArn": str,
        "assessmentStatus": AssessmentStatusType,
        "invoker": AssessmentInvokerType,
    },
)
_OptionalAppAssessmentTypeDef = TypedDict(
    "_OptionalAppAssessmentTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "assessmentName": str,
        "compliance": Dict[DisruptionTypeType, "DisruptionComplianceTypeDef"],
        "complianceStatus": ComplianceStatusType,
        "cost": "CostTypeDef",
        "driftStatus": DriftStatusType,
        "endTime": datetime,
        "message": str,
        "policy": "ResiliencyPolicyTypeDef",
        "resiliencyScore": "ResiliencyScoreTypeDef",
        "resourceErrorsDetails": "ResourceErrorsDetailsTypeDef",
        "startTime": datetime,
        "tags": Dict[str, str],
        "versionName": str,
    },
    total=False,
)

class AppAssessmentTypeDef(_RequiredAppAssessmentTypeDef, _OptionalAppAssessmentTypeDef):
    pass

AppComponentComplianceTypeDef = TypedDict(
    "AppComponentComplianceTypeDef",
    {
        "appComponentName": str,
        "compliance": Dict[DisruptionTypeType, "DisruptionComplianceTypeDef"],
        "cost": "CostTypeDef",
        "message": str,
        "resiliencyScore": "ResiliencyScoreTypeDef",
        "status": ComplianceStatusType,
    },
    total=False,
)

_RequiredAppComponentTypeDef = TypedDict(
    "_RequiredAppComponentTypeDef",
    {
        "name": str,
        "type": str,
    },
)
_OptionalAppComponentTypeDef = TypedDict(
    "_OptionalAppComponentTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
        "id": str,
    },
    total=False,
)

class AppComponentTypeDef(_RequiredAppComponentTypeDef, _OptionalAppComponentTypeDef):
    pass

_RequiredAppInputSourceTypeDef = TypedDict(
    "_RequiredAppInputSourceTypeDef",
    {
        "importType": ResourceMappingTypeType,
    },
)
_OptionalAppInputSourceTypeDef = TypedDict(
    "_OptionalAppInputSourceTypeDef",
    {
        "eksSourceClusterNamespace": "EksSourceClusterNamespaceTypeDef",
        "resourceCount": int,
        "sourceArn": str,
        "sourceName": str,
        "terraformSource": "TerraformSourceTypeDef",
    },
    total=False,
)

class AppInputSourceTypeDef(_RequiredAppInputSourceTypeDef, _OptionalAppInputSourceTypeDef):
    pass

_RequiredAppSummaryTypeDef = TypedDict(
    "_RequiredAppSummaryTypeDef",
    {
        "appArn": str,
        "creationTime": datetime,
        "name": str,
    },
)
_OptionalAppSummaryTypeDef = TypedDict(
    "_OptionalAppSummaryTypeDef",
    {
        "assessmentSchedule": AppAssessmentScheduleTypeType,
        "complianceStatus": AppComplianceStatusTypeType,
        "description": str,
        "driftStatus": AppDriftStatusTypeType,
        "lastAppComplianceEvaluationTime": datetime,
        "resiliencyScore": float,
        "rpoInSecs": int,
        "rtoInSecs": int,
        "status": AppStatusTypeType,
    },
    total=False,
)

class AppSummaryTypeDef(_RequiredAppSummaryTypeDef, _OptionalAppSummaryTypeDef):
    pass

_RequiredAppTypeDef = TypedDict(
    "_RequiredAppTypeDef",
    {
        "appArn": str,
        "creationTime": datetime,
        "name": str,
    },
)
_OptionalAppTypeDef = TypedDict(
    "_OptionalAppTypeDef",
    {
        "assessmentSchedule": AppAssessmentScheduleTypeType,
        "complianceStatus": AppComplianceStatusTypeType,
        "description": str,
        "driftStatus": AppDriftStatusTypeType,
        "eventSubscriptions": List["EventSubscriptionTypeDef"],
        "lastAppComplianceEvaluationTime": datetime,
        "lastDriftEvaluationTime": datetime,
        "lastResiliencyScoreEvaluationTime": datetime,
        "permissionModel": "PermissionModelTypeDef",
        "policyArn": str,
        "resiliencyScore": float,
        "rpoInSecs": int,
        "rtoInSecs": int,
        "status": AppStatusTypeType,
        "tags": Dict[str, str],
    },
    total=False,
)

class AppTypeDef(_RequiredAppTypeDef, _OptionalAppTypeDef):
    pass

_RequiredAppVersionSummaryTypeDef = TypedDict(
    "_RequiredAppVersionSummaryTypeDef",
    {
        "appVersion": str,
    },
)
_OptionalAppVersionSummaryTypeDef = TypedDict(
    "_OptionalAppVersionSummaryTypeDef",
    {
        "creationTime": datetime,
        "identifier": int,
        "versionName": str,
    },
    total=False,
)

class AppVersionSummaryTypeDef(
    _RequiredAppVersionSummaryTypeDef, _OptionalAppVersionSummaryTypeDef
):
    pass

BatchUpdateRecommendationStatusFailedEntryTypeDef = TypedDict(
    "BatchUpdateRecommendationStatusFailedEntryTypeDef",
    {
        "entryId": str,
        "errorMessage": str,
    },
)

BatchUpdateRecommendationStatusRequestRequestTypeDef = TypedDict(
    "BatchUpdateRecommendationStatusRequestRequestTypeDef",
    {
        "appArn": str,
        "requestEntries": List["UpdateRecommendationStatusRequestEntryTypeDef"],
    },
)

BatchUpdateRecommendationStatusResponseTypeDef = TypedDict(
    "BatchUpdateRecommendationStatusResponseTypeDef",
    {
        "appArn": str,
        "failedEntries": List["BatchUpdateRecommendationStatusFailedEntryTypeDef"],
        "successfulEntries": List["BatchUpdateRecommendationStatusSuccessfulEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchUpdateRecommendationStatusSuccessfulEntryTypeDef = TypedDict(
    "_RequiredBatchUpdateRecommendationStatusSuccessfulEntryTypeDef",
    {
        "entryId": str,
        "excluded": bool,
        "item": "UpdateRecommendationStatusItemTypeDef",
        "referenceId": str,
    },
)
_OptionalBatchUpdateRecommendationStatusSuccessfulEntryTypeDef = TypedDict(
    "_OptionalBatchUpdateRecommendationStatusSuccessfulEntryTypeDef",
    {
        "excludeReason": ExcludeRecommendationReasonType,
    },
    total=False,
)

class BatchUpdateRecommendationStatusSuccessfulEntryTypeDef(
    _RequiredBatchUpdateRecommendationStatusSuccessfulEntryTypeDef,
    _OptionalBatchUpdateRecommendationStatusSuccessfulEntryTypeDef,
):
    pass

ComplianceDriftTypeDef = TypedDict(
    "ComplianceDriftTypeDef",
    {
        "actualReferenceId": str,
        "actualValue": Dict[DisruptionTypeType, "DisruptionComplianceTypeDef"],
        "appId": str,
        "appVersion": str,
        "diffType": DifferenceTypeType,
        "driftType": DriftTypeType,
        "entityId": str,
        "entityType": str,
        "expectedReferenceId": str,
        "expectedValue": Dict[DisruptionTypeType, "DisruptionComplianceTypeDef"],
    },
    total=False,
)

ComponentRecommendationTypeDef = TypedDict(
    "ComponentRecommendationTypeDef",
    {
        "appComponentName": str,
        "configRecommendations": List["ConfigRecommendationTypeDef"],
        "recommendationStatus": RecommendationComplianceStatusType,
    },
)

_RequiredConfigRecommendationTypeDef = TypedDict(
    "_RequiredConfigRecommendationTypeDef",
    {
        "name": str,
        "optimizationType": ConfigRecommendationOptimizationTypeType,
        "referenceId": str,
    },
)
_OptionalConfigRecommendationTypeDef = TypedDict(
    "_OptionalConfigRecommendationTypeDef",
    {
        "appComponentName": str,
        "compliance": Dict[DisruptionTypeType, "DisruptionComplianceTypeDef"],
        "cost": "CostTypeDef",
        "description": str,
        "haArchitecture": HaArchitectureType,
        "recommendationCompliance": Dict[
            DisruptionTypeType, "RecommendationDisruptionComplianceTypeDef"
        ],
        "suggestedChanges": List[str],
    },
    total=False,
)

class ConfigRecommendationTypeDef(
    _RequiredConfigRecommendationTypeDef, _OptionalConfigRecommendationTypeDef
):
    pass

CostTypeDef = TypedDict(
    "CostTypeDef",
    {
        "amount": float,
        "currency": str,
        "frequency": CostFrequencyType,
    },
)

_RequiredCreateAppRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateAppRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppRequestRequestTypeDef",
    {
        "assessmentSchedule": AppAssessmentScheduleTypeType,
        "clientToken": str,
        "description": str,
        "eventSubscriptions": List["EventSubscriptionTypeDef"],
        "permissionModel": "PermissionModelTypeDef",
        "policyArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAppRequestRequestTypeDef(
    _RequiredCreateAppRequestRequestTypeDef, _OptionalCreateAppRequestRequestTypeDef
):
    pass

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppVersionAppComponentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppVersionAppComponentRequestRequestTypeDef",
    {
        "appArn": str,
        "name": str,
        "type": str,
    },
)
_OptionalCreateAppVersionAppComponentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppVersionAppComponentRequestRequestTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
        "clientToken": str,
        "id": str,
    },
    total=False,
)

class CreateAppVersionAppComponentRequestRequestTypeDef(
    _RequiredCreateAppVersionAppComponentRequestRequestTypeDef,
    _OptionalCreateAppVersionAppComponentRequestRequestTypeDef,
):
    pass

CreateAppVersionAppComponentResponseTypeDef = TypedDict(
    "CreateAppVersionAppComponentResponseTypeDef",
    {
        "appArn": str,
        "appComponent": "AppComponentTypeDef",
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAppVersionResourceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAppVersionResourceRequestRequestTypeDef",
    {
        "appArn": str,
        "appComponents": List[str],
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "physicalResourceId": str,
        "resourceType": str,
    },
)
_OptionalCreateAppVersionResourceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAppVersionResourceRequestRequestTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
        "awsAccountId": str,
        "awsRegion": str,
        "clientToken": str,
        "resourceName": str,
    },
    total=False,
)

class CreateAppVersionResourceRequestRequestTypeDef(
    _RequiredCreateAppVersionResourceRequestRequestTypeDef,
    _OptionalCreateAppVersionResourceRequestRequestTypeDef,
):
    pass

CreateAppVersionResourceResponseTypeDef = TypedDict(
    "CreateAppVersionResourceResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "physicalResource": "PhysicalResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRecommendationTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRecommendationTemplateRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "name": str,
    },
)
_OptionalCreateRecommendationTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRecommendationTemplateRequestRequestTypeDef",
    {
        "bucketName": str,
        "clientToken": str,
        "format": TemplateFormatType,
        "recommendationIds": List[str],
        "recommendationTypes": List[RenderRecommendationTypeType],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateRecommendationTemplateRequestRequestTypeDef(
    _RequiredCreateRecommendationTemplateRequestRequestTypeDef,
    _OptionalCreateRecommendationTemplateRequestRequestTypeDef,
):
    pass

CreateRecommendationTemplateResponseTypeDef = TypedDict(
    "CreateRecommendationTemplateResponseTypeDef",
    {
        "recommendationTemplate": "RecommendationTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResiliencyPolicyRequestRequestTypeDef",
    {
        "policy": Dict[DisruptionTypeType, "FailurePolicyTypeDef"],
        "policyName": str,
        "tier": ResiliencyPolicyTierType,
    },
)
_OptionalCreateResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResiliencyPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
        "dataLocationConstraint": DataLocationConstraintType,
        "policyDescription": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateResiliencyPolicyRequestRequestTypeDef(
    _RequiredCreateResiliencyPolicyRequestRequestTypeDef,
    _OptionalCreateResiliencyPolicyRequestRequestTypeDef,
):
    pass

CreateResiliencyPolicyResponseTypeDef = TypedDict(
    "CreateResiliencyPolicyResponseTypeDef",
    {
        "policy": "ResiliencyPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAppAssessmentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAppAssessmentRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)
_OptionalDeleteAppAssessmentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAppAssessmentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAppAssessmentRequestRequestTypeDef(
    _RequiredDeleteAppAssessmentRequestRequestTypeDef,
    _OptionalDeleteAppAssessmentRequestRequestTypeDef,
):
    pass

DeleteAppAssessmentResponseTypeDef = TypedDict(
    "DeleteAppAssessmentResponseTypeDef",
    {
        "assessmentArn": str,
        "assessmentStatus": AssessmentStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAppInputSourceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAppInputSourceRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalDeleteAppInputSourceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAppInputSourceRequestRequestTypeDef",
    {
        "clientToken": str,
        "eksSourceClusterNamespace": "EksSourceClusterNamespaceTypeDef",
        "sourceArn": str,
        "terraformSource": "TerraformSourceTypeDef",
    },
    total=False,
)

class DeleteAppInputSourceRequestRequestTypeDef(
    _RequiredDeleteAppInputSourceRequestRequestTypeDef,
    _OptionalDeleteAppInputSourceRequestRequestTypeDef,
):
    pass

DeleteAppInputSourceResponseTypeDef = TypedDict(
    "DeleteAppInputSourceResponseTypeDef",
    {
        "appArn": str,
        "appInputSource": "AppInputSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAppRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAppRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalDeleteAppRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAppRequestRequestTypeDef",
    {
        "clientToken": str,
        "forceDelete": bool,
    },
    total=False,
)

class DeleteAppRequestRequestTypeDef(
    _RequiredDeleteAppRequestRequestTypeDef, _OptionalDeleteAppRequestRequestTypeDef
):
    pass

DeleteAppResponseTypeDef = TypedDict(
    "DeleteAppResponseTypeDef",
    {
        "appArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAppVersionAppComponentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAppVersionAppComponentRequestRequestTypeDef",
    {
        "appArn": str,
        "id": str,
    },
)
_OptionalDeleteAppVersionAppComponentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAppVersionAppComponentRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteAppVersionAppComponentRequestRequestTypeDef(
    _RequiredDeleteAppVersionAppComponentRequestRequestTypeDef,
    _OptionalDeleteAppVersionAppComponentRequestRequestTypeDef,
):
    pass

DeleteAppVersionAppComponentResponseTypeDef = TypedDict(
    "DeleteAppVersionAppComponentResponseTypeDef",
    {
        "appArn": str,
        "appComponent": "AppComponentTypeDef",
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteAppVersionResourceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteAppVersionResourceRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalDeleteAppVersionResourceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteAppVersionResourceRequestRequestTypeDef",
    {
        "awsAccountId": str,
        "awsRegion": str,
        "clientToken": str,
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "physicalResourceId": str,
        "resourceName": str,
    },
    total=False,
)

class DeleteAppVersionResourceRequestRequestTypeDef(
    _RequiredDeleteAppVersionResourceRequestRequestTypeDef,
    _OptionalDeleteAppVersionResourceRequestRequestTypeDef,
):
    pass

DeleteAppVersionResourceResponseTypeDef = TypedDict(
    "DeleteAppVersionResourceResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "physicalResource": "PhysicalResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRecommendationTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRecommendationTemplateRequestRequestTypeDef",
    {
        "recommendationTemplateArn": str,
    },
)
_OptionalDeleteRecommendationTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRecommendationTemplateRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteRecommendationTemplateRequestRequestTypeDef(
    _RequiredDeleteRecommendationTemplateRequestRequestTypeDef,
    _OptionalDeleteRecommendationTemplateRequestRequestTypeDef,
):
    pass

DeleteRecommendationTemplateResponseTypeDef = TypedDict(
    "DeleteRecommendationTemplateResponseTypeDef",
    {
        "recommendationTemplateArn": str,
        "status": RecommendationTemplateStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResiliencyPolicyRequestRequestTypeDef",
    {
        "policyArn": str,
    },
)
_OptionalDeleteResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResiliencyPolicyRequestRequestTypeDef",
    {
        "clientToken": str,
    },
    total=False,
)

class DeleteResiliencyPolicyRequestRequestTypeDef(
    _RequiredDeleteResiliencyPolicyRequestRequestTypeDef,
    _OptionalDeleteResiliencyPolicyRequestRequestTypeDef,
):
    pass

DeleteResiliencyPolicyResponseTypeDef = TypedDict(
    "DeleteResiliencyPolicyResponseTypeDef",
    {
        "policyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppAssessmentRequestRequestTypeDef = TypedDict(
    "DescribeAppAssessmentRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)

DescribeAppAssessmentResponseTypeDef = TypedDict(
    "DescribeAppAssessmentResponseTypeDef",
    {
        "assessment": "AppAssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppRequestRequestTypeDef = TypedDict(
    "DescribeAppRequestRequestTypeDef",
    {
        "appArn": str,
    },
)

DescribeAppResponseTypeDef = TypedDict(
    "DescribeAppResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppVersionAppComponentRequestRequestTypeDef = TypedDict(
    "DescribeAppVersionAppComponentRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "id": str,
    },
)

DescribeAppVersionAppComponentResponseTypeDef = TypedDict(
    "DescribeAppVersionAppComponentResponseTypeDef",
    {
        "appArn": str,
        "appComponent": "AppComponentTypeDef",
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppVersionRequestRequestTypeDef = TypedDict(
    "DescribeAppVersionRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)

_RequiredDescribeAppVersionResourceRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAppVersionResourceRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)
_OptionalDescribeAppVersionResourceRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAppVersionResourceRequestRequestTypeDef",
    {
        "awsAccountId": str,
        "awsRegion": str,
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "physicalResourceId": str,
        "resourceName": str,
    },
    total=False,
)

class DescribeAppVersionResourceRequestRequestTypeDef(
    _RequiredDescribeAppVersionResourceRequestRequestTypeDef,
    _OptionalDescribeAppVersionResourceRequestRequestTypeDef,
):
    pass

DescribeAppVersionResourceResponseTypeDef = TypedDict(
    "DescribeAppVersionResourceResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "physicalResource": "PhysicalResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)
_OptionalDescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef",
    {
        "resolutionId": str,
    },
    total=False,
)

class DescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef(
    _RequiredDescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef,
    _OptionalDescribeAppVersionResourcesResolutionStatusRequestRequestTypeDef,
):
    pass

DescribeAppVersionResourcesResolutionStatusResponseTypeDef = TypedDict(
    "DescribeAppVersionResourcesResolutionStatusResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "errorMessage": str,
        "resolutionId": str,
        "status": ResourceResolutionStatusTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppVersionResponseTypeDef = TypedDict(
    "DescribeAppVersionResponseTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
        "appArn": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppVersionTemplateRequestRequestTypeDef = TypedDict(
    "DescribeAppVersionTemplateRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)

DescribeAppVersionTemplateResponseTypeDef = TypedDict(
    "DescribeAppVersionTemplateResponseTypeDef",
    {
        "appArn": str,
        "appTemplateBody": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef = TypedDict(
    "DescribeDraftAppVersionResourcesImportStatusRequestRequestTypeDef",
    {
        "appArn": str,
    },
)

DescribeDraftAppVersionResourcesImportStatusResponseTypeDef = TypedDict(
    "DescribeDraftAppVersionResourcesImportStatusResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "errorMessage": str,
        "status": ResourceImportStatusTypeType,
        "statusChangeTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "DescribeResiliencyPolicyRequestRequestTypeDef",
    {
        "policyArn": str,
    },
)

DescribeResiliencyPolicyResponseTypeDef = TypedDict(
    "DescribeResiliencyPolicyResponseTypeDef",
    {
        "policy": "ResiliencyPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisruptionComplianceTypeDef = TypedDict(
    "_RequiredDisruptionComplianceTypeDef",
    {
        "complianceStatus": ComplianceStatusType,
    },
)
_OptionalDisruptionComplianceTypeDef = TypedDict(
    "_OptionalDisruptionComplianceTypeDef",
    {
        "achievableRpoInSecs": int,
        "achievableRtoInSecs": int,
        "currentRpoInSecs": int,
        "currentRtoInSecs": int,
        "message": str,
        "rpoDescription": str,
        "rpoReferenceId": str,
        "rtoDescription": str,
        "rtoReferenceId": str,
    },
    total=False,
)

class DisruptionComplianceTypeDef(
    _RequiredDisruptionComplianceTypeDef, _OptionalDisruptionComplianceTypeDef
):
    pass

EksSourceClusterNamespaceTypeDef = TypedDict(
    "EksSourceClusterNamespaceTypeDef",
    {
        "eksClusterArn": str,
        "namespace": str,
    },
)

EksSourceTypeDef = TypedDict(
    "EksSourceTypeDef",
    {
        "eksClusterArn": str,
        "namespaces": List[str],
    },
)

_RequiredEventSubscriptionTypeDef = TypedDict(
    "_RequiredEventSubscriptionTypeDef",
    {
        "eventType": EventTypeType,
        "name": str,
    },
)
_OptionalEventSubscriptionTypeDef = TypedDict(
    "_OptionalEventSubscriptionTypeDef",
    {
        "snsTopicArn": str,
    },
    total=False,
)

class EventSubscriptionTypeDef(
    _RequiredEventSubscriptionTypeDef, _OptionalEventSubscriptionTypeDef
):
    pass

FailurePolicyTypeDef = TypedDict(
    "FailurePolicyTypeDef",
    {
        "rpoInSecs": int,
        "rtoInSecs": int,
    },
)

_RequiredImportResourcesToDraftAppVersionRequestRequestTypeDef = TypedDict(
    "_RequiredImportResourcesToDraftAppVersionRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalImportResourcesToDraftAppVersionRequestRequestTypeDef = TypedDict(
    "_OptionalImportResourcesToDraftAppVersionRequestRequestTypeDef",
    {
        "eksSources": List["EksSourceTypeDef"],
        "importStrategy": ResourceImportStrategyTypeType,
        "sourceArns": List[str],
        "terraformSources": List["TerraformSourceTypeDef"],
    },
    total=False,
)

class ImportResourcesToDraftAppVersionRequestRequestTypeDef(
    _RequiredImportResourcesToDraftAppVersionRequestRequestTypeDef,
    _OptionalImportResourcesToDraftAppVersionRequestRequestTypeDef,
):
    pass

ImportResourcesToDraftAppVersionResponseTypeDef = TypedDict(
    "ImportResourcesToDraftAppVersionResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "eksSources": List["EksSourceTypeDef"],
        "sourceArns": List[str],
        "status": ResourceImportStatusTypeType,
        "terraformSources": List["TerraformSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAlarmRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAlarmRecommendationsRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)
_OptionalListAlarmRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAlarmRecommendationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAlarmRecommendationsRequestRequestTypeDef(
    _RequiredListAlarmRecommendationsRequestRequestTypeDef,
    _OptionalListAlarmRecommendationsRequestRequestTypeDef,
):
    pass

ListAlarmRecommendationsResponseTypeDef = TypedDict(
    "ListAlarmRecommendationsResponseTypeDef",
    {
        "alarmRecommendations": List["AlarmRecommendationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppAssessmentComplianceDriftsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppAssessmentComplianceDriftsRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)
_OptionalListAppAssessmentComplianceDriftsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppAssessmentComplianceDriftsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAppAssessmentComplianceDriftsRequestRequestTypeDef(
    _RequiredListAppAssessmentComplianceDriftsRequestRequestTypeDef,
    _OptionalListAppAssessmentComplianceDriftsRequestRequestTypeDef,
):
    pass

ListAppAssessmentComplianceDriftsResponseTypeDef = TypedDict(
    "ListAppAssessmentComplianceDriftsResponseTypeDef",
    {
        "complianceDrifts": List["ComplianceDriftTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppAssessmentResourceDriftsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppAssessmentResourceDriftsRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)
_OptionalListAppAssessmentResourceDriftsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppAssessmentResourceDriftsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAppAssessmentResourceDriftsRequestRequestTypeDef(
    _RequiredListAppAssessmentResourceDriftsRequestRequestTypeDef,
    _OptionalListAppAssessmentResourceDriftsRequestRequestTypeDef,
):
    pass

ListAppAssessmentResourceDriftsResponseTypeDef = TypedDict(
    "ListAppAssessmentResourceDriftsResponseTypeDef",
    {
        "nextToken": str,
        "resourceDrifts": List["ResourceDriftTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppAssessmentsRequestRequestTypeDef = TypedDict(
    "ListAppAssessmentsRequestRequestTypeDef",
    {
        "appArn": str,
        "assessmentName": str,
        "assessmentStatus": List[AssessmentStatusType],
        "complianceStatus": ComplianceStatusType,
        "invoker": AssessmentInvokerType,
        "maxResults": int,
        "nextToken": str,
        "reverseOrder": bool,
    },
    total=False,
)

ListAppAssessmentsResponseTypeDef = TypedDict(
    "ListAppAssessmentsResponseTypeDef",
    {
        "assessmentSummaries": List["AppAssessmentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppComponentCompliancesRequestRequestTypeDef = TypedDict(
    "_RequiredListAppComponentCompliancesRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)
_OptionalListAppComponentCompliancesRequestRequestTypeDef = TypedDict(
    "_OptionalListAppComponentCompliancesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAppComponentCompliancesRequestRequestTypeDef(
    _RequiredListAppComponentCompliancesRequestRequestTypeDef,
    _OptionalListAppComponentCompliancesRequestRequestTypeDef,
):
    pass

ListAppComponentCompliancesResponseTypeDef = TypedDict(
    "ListAppComponentCompliancesResponseTypeDef",
    {
        "componentCompliances": List["AppComponentComplianceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppComponentRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppComponentRecommendationsRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)
_OptionalListAppComponentRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppComponentRecommendationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAppComponentRecommendationsRequestRequestTypeDef(
    _RequiredListAppComponentRecommendationsRequestRequestTypeDef,
    _OptionalListAppComponentRecommendationsRequestRequestTypeDef,
):
    pass

ListAppComponentRecommendationsResponseTypeDef = TypedDict(
    "ListAppComponentRecommendationsResponseTypeDef",
    {
        "componentRecommendations": List["ComponentRecommendationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppInputSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListAppInputSourcesRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)
_OptionalListAppInputSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListAppInputSourcesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAppInputSourcesRequestRequestTypeDef(
    _RequiredListAppInputSourcesRequestRequestTypeDef,
    _OptionalListAppInputSourcesRequestRequestTypeDef,
):
    pass

ListAppInputSourcesResponseTypeDef = TypedDict(
    "ListAppInputSourcesResponseTypeDef",
    {
        "appInputSources": List["AppInputSourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppVersionAppComponentsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppVersionAppComponentsRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)
_OptionalListAppVersionAppComponentsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppVersionAppComponentsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAppVersionAppComponentsRequestRequestTypeDef(
    _RequiredListAppVersionAppComponentsRequestRequestTypeDef,
    _OptionalListAppVersionAppComponentsRequestRequestTypeDef,
):
    pass

ListAppVersionAppComponentsResponseTypeDef = TypedDict(
    "ListAppVersionAppComponentsResponseTypeDef",
    {
        "appArn": str,
        "appComponents": List["AppComponentTypeDef"],
        "appVersion": str,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppVersionResourceMappingsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppVersionResourceMappingsRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)
_OptionalListAppVersionResourceMappingsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppVersionResourceMappingsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAppVersionResourceMappingsRequestRequestTypeDef(
    _RequiredListAppVersionResourceMappingsRequestRequestTypeDef,
    _OptionalListAppVersionResourceMappingsRequestRequestTypeDef,
):
    pass

ListAppVersionResourceMappingsResponseTypeDef = TypedDict(
    "ListAppVersionResourceMappingsResponseTypeDef",
    {
        "nextToken": str,
        "resourceMappings": List["ResourceMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppVersionResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListAppVersionResourcesRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)
_OptionalListAppVersionResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListAppVersionResourcesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resolutionId": str,
    },
    total=False,
)

class ListAppVersionResourcesRequestRequestTypeDef(
    _RequiredListAppVersionResourcesRequestRequestTypeDef,
    _OptionalListAppVersionResourcesRequestRequestTypeDef,
):
    pass

ListAppVersionResourcesResponseTypeDef = TypedDict(
    "ListAppVersionResourcesResponseTypeDef",
    {
        "nextToken": str,
        "physicalResources": List["PhysicalResourceTypeDef"],
        "resolutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAppVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAppVersionsRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalListAppVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAppVersionsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "maxResults": int,
        "nextToken": str,
        "startTime": Union[datetime, str],
    },
    total=False,
)

class ListAppVersionsRequestRequestTypeDef(
    _RequiredListAppVersionsRequestRequestTypeDef, _OptionalListAppVersionsRequestRequestTypeDef
):
    pass

ListAppVersionsResponseTypeDef = TypedDict(
    "ListAppVersionsResponseTypeDef",
    {
        "appVersions": List["AppVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppsRequestRequestTypeDef = TypedDict(
    "ListAppsRequestRequestTypeDef",
    {
        "appArn": str,
        "fromLastAssessmentTime": Union[datetime, str],
        "maxResults": int,
        "name": str,
        "nextToken": str,
        "reverseOrder": bool,
        "toLastAssessmentTime": Union[datetime, str],
    },
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef",
    {
        "appSummaries": List["AppSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendationTemplatesRequestRequestTypeDef = TypedDict(
    "ListRecommendationTemplatesRequestRequestTypeDef",
    {
        "assessmentArn": str,
        "maxResults": int,
        "name": str,
        "nextToken": str,
        "recommendationTemplateArn": str,
        "reverseOrder": bool,
        "status": List[RecommendationTemplateStatusType],
    },
    total=False,
)

ListRecommendationTemplatesResponseTypeDef = TypedDict(
    "ListRecommendationTemplatesResponseTypeDef",
    {
        "nextToken": str,
        "recommendationTemplates": List["RecommendationTemplateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResiliencyPoliciesRequestRequestTypeDef = TypedDict(
    "ListResiliencyPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "policyName": str,
    },
    total=False,
)

ListResiliencyPoliciesResponseTypeDef = TypedDict(
    "ListResiliencyPoliciesResponseTypeDef",
    {
        "nextToken": str,
        "resiliencyPolicies": List["ResiliencyPolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSopRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredListSopRecommendationsRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)
_OptionalListSopRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalListSopRecommendationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSopRecommendationsRequestRequestTypeDef(
    _RequiredListSopRecommendationsRequestRequestTypeDef,
    _OptionalListSopRecommendationsRequestRequestTypeDef,
):
    pass

ListSopRecommendationsResponseTypeDef = TypedDict(
    "ListSopRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "sopRecommendations": List["SopRecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSuggestedResiliencyPoliciesRequestRequestTypeDef = TypedDict(
    "ListSuggestedResiliencyPoliciesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSuggestedResiliencyPoliciesResponseTypeDef = TypedDict(
    "ListSuggestedResiliencyPoliciesResponseTypeDef",
    {
        "nextToken": str,
        "resiliencyPolicies": List["ResiliencyPolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTestRecommendationsRequestRequestTypeDef = TypedDict(
    "_RequiredListTestRecommendationsRequestRequestTypeDef",
    {
        "assessmentArn": str,
    },
)
_OptionalListTestRecommendationsRequestRequestTypeDef = TypedDict(
    "_OptionalListTestRecommendationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListTestRecommendationsRequestRequestTypeDef(
    _RequiredListTestRecommendationsRequestRequestTypeDef,
    _OptionalListTestRecommendationsRequestRequestTypeDef,
):
    pass

ListTestRecommendationsResponseTypeDef = TypedDict(
    "ListTestRecommendationsResponseTypeDef",
    {
        "nextToken": str,
        "testRecommendations": List["TestRecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUnsupportedAppVersionResourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListUnsupportedAppVersionResourcesRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)
_OptionalListUnsupportedAppVersionResourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListUnsupportedAppVersionResourcesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "resolutionId": str,
    },
    total=False,
)

class ListUnsupportedAppVersionResourcesRequestRequestTypeDef(
    _RequiredListUnsupportedAppVersionResourcesRequestRequestTypeDef,
    _OptionalListUnsupportedAppVersionResourcesRequestRequestTypeDef,
):
    pass

ListUnsupportedAppVersionResourcesResponseTypeDef = TypedDict(
    "ListUnsupportedAppVersionResourcesResponseTypeDef",
    {
        "nextToken": str,
        "resolutionId": str,
        "unsupportedResources": List["UnsupportedResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLogicalResourceIdTypeDef = TypedDict(
    "_RequiredLogicalResourceIdTypeDef",
    {
        "identifier": str,
    },
)
_OptionalLogicalResourceIdTypeDef = TypedDict(
    "_OptionalLogicalResourceIdTypeDef",
    {
        "eksSourceName": str,
        "logicalStackName": str,
        "resourceGroupName": str,
        "terraformSourceName": str,
    },
    total=False,
)

class LogicalResourceIdTypeDef(
    _RequiredLogicalResourceIdTypeDef, _OptionalLogicalResourceIdTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPermissionModelTypeDef = TypedDict(
    "_RequiredPermissionModelTypeDef",
    {
        "type": PermissionModelTypeType,
    },
)
_OptionalPermissionModelTypeDef = TypedDict(
    "_OptionalPermissionModelTypeDef",
    {
        "crossAccountRoleArns": List[str],
        "invokerRoleName": str,
    },
    total=False,
)

class PermissionModelTypeDef(_RequiredPermissionModelTypeDef, _OptionalPermissionModelTypeDef):
    pass

_RequiredPhysicalResourceIdTypeDef = TypedDict(
    "_RequiredPhysicalResourceIdTypeDef",
    {
        "identifier": str,
        "type": PhysicalIdentifierTypeType,
    },
)
_OptionalPhysicalResourceIdTypeDef = TypedDict(
    "_OptionalPhysicalResourceIdTypeDef",
    {
        "awsAccountId": str,
        "awsRegion": str,
    },
    total=False,
)

class PhysicalResourceIdTypeDef(
    _RequiredPhysicalResourceIdTypeDef, _OptionalPhysicalResourceIdTypeDef
):
    pass

_RequiredPhysicalResourceTypeDef = TypedDict(
    "_RequiredPhysicalResourceTypeDef",
    {
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "physicalResourceId": "PhysicalResourceIdTypeDef",
        "resourceType": str,
    },
)
_OptionalPhysicalResourceTypeDef = TypedDict(
    "_OptionalPhysicalResourceTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
        "appComponents": List["AppComponentTypeDef"],
        "excluded": bool,
        "parentResourceName": str,
        "resourceName": str,
        "sourceType": ResourceSourceTypeType,
    },
    total=False,
)

class PhysicalResourceTypeDef(_RequiredPhysicalResourceTypeDef, _OptionalPhysicalResourceTypeDef):
    pass

_RequiredPublishAppVersionRequestRequestTypeDef = TypedDict(
    "_RequiredPublishAppVersionRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalPublishAppVersionRequestRequestTypeDef = TypedDict(
    "_OptionalPublishAppVersionRequestRequestTypeDef",
    {
        "versionName": str,
    },
    total=False,
)

class PublishAppVersionRequestRequestTypeDef(
    _RequiredPublishAppVersionRequestRequestTypeDef, _OptionalPublishAppVersionRequestRequestTypeDef
):
    pass

PublishAppVersionResponseTypeDef = TypedDict(
    "PublishAppVersionResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "identifier": int,
        "versionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutDraftAppVersionTemplateRequestRequestTypeDef = TypedDict(
    "PutDraftAppVersionTemplateRequestRequestTypeDef",
    {
        "appArn": str,
        "appTemplateBody": str,
    },
)

PutDraftAppVersionTemplateResponseTypeDef = TypedDict(
    "PutDraftAppVersionTemplateResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRecommendationDisruptionComplianceTypeDef = TypedDict(
    "_RequiredRecommendationDisruptionComplianceTypeDef",
    {
        "expectedComplianceStatus": ComplianceStatusType,
    },
)
_OptionalRecommendationDisruptionComplianceTypeDef = TypedDict(
    "_OptionalRecommendationDisruptionComplianceTypeDef",
    {
        "expectedRpoDescription": str,
        "expectedRpoInSecs": int,
        "expectedRtoDescription": str,
        "expectedRtoInSecs": int,
    },
    total=False,
)

class RecommendationDisruptionComplianceTypeDef(
    _RequiredRecommendationDisruptionComplianceTypeDef,
    _OptionalRecommendationDisruptionComplianceTypeDef,
):
    pass

RecommendationItemTypeDef = TypedDict(
    "RecommendationItemTypeDef",
    {
        "alreadyImplemented": bool,
        "excludeReason": ExcludeRecommendationReasonType,
        "excluded": bool,
        "resourceId": str,
        "targetAccountId": str,
        "targetRegion": str,
    },
    total=False,
)

_RequiredRecommendationTemplateTypeDef = TypedDict(
    "_RequiredRecommendationTemplateTypeDef",
    {
        "assessmentArn": str,
        "format": TemplateFormatType,
        "name": str,
        "recommendationTemplateArn": str,
        "recommendationTypes": List[RenderRecommendationTypeType],
        "status": RecommendationTemplateStatusType,
    },
)
_OptionalRecommendationTemplateTypeDef = TypedDict(
    "_OptionalRecommendationTemplateTypeDef",
    {
        "appArn": str,
        "endTime": datetime,
        "message": str,
        "needsReplacements": bool,
        "recommendationIds": List[str],
        "startTime": datetime,
        "tags": Dict[str, str],
        "templatesLocation": "S3LocationTypeDef",
    },
    total=False,
)

class RecommendationTemplateTypeDef(
    _RequiredRecommendationTemplateTypeDef, _OptionalRecommendationTemplateTypeDef
):
    pass

_RequiredRemoveDraftAppVersionResourceMappingsRequestRequestTypeDef = TypedDict(
    "_RequiredRemoveDraftAppVersionResourceMappingsRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalRemoveDraftAppVersionResourceMappingsRequestRequestTypeDef = TypedDict(
    "_OptionalRemoveDraftAppVersionResourceMappingsRequestRequestTypeDef",
    {
        "appRegistryAppNames": List[str],
        "eksSourceNames": List[str],
        "logicalStackNames": List[str],
        "resourceGroupNames": List[str],
        "resourceNames": List[str],
        "terraformSourceNames": List[str],
    },
    total=False,
)

class RemoveDraftAppVersionResourceMappingsRequestRequestTypeDef(
    _RequiredRemoveDraftAppVersionResourceMappingsRequestRequestTypeDef,
    _OptionalRemoveDraftAppVersionResourceMappingsRequestRequestTypeDef,
):
    pass

RemoveDraftAppVersionResourceMappingsResponseTypeDef = TypedDict(
    "RemoveDraftAppVersionResourceMappingsResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResiliencyPolicyTypeDef = TypedDict(
    "ResiliencyPolicyTypeDef",
    {
        "creationTime": datetime,
        "dataLocationConstraint": DataLocationConstraintType,
        "estimatedCostTier": EstimatedCostTierType,
        "policy": Dict[DisruptionTypeType, "FailurePolicyTypeDef"],
        "policyArn": str,
        "policyDescription": str,
        "policyName": str,
        "tags": Dict[str, str],
        "tier": ResiliencyPolicyTierType,
    },
    total=False,
)

_RequiredResiliencyScoreTypeDef = TypedDict(
    "_RequiredResiliencyScoreTypeDef",
    {
        "disruptionScore": Dict[DisruptionTypeType, float],
        "score": float,
    },
)
_OptionalResiliencyScoreTypeDef = TypedDict(
    "_OptionalResiliencyScoreTypeDef",
    {
        "componentScore": Dict[ResiliencyScoreTypeType, "ScoringComponentResiliencyScoreTypeDef"],
    },
    total=False,
)

class ResiliencyScoreTypeDef(_RequiredResiliencyScoreTypeDef, _OptionalResiliencyScoreTypeDef):
    pass

ResolveAppVersionResourcesRequestRequestTypeDef = TypedDict(
    "ResolveAppVersionResourcesRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
    },
)

ResolveAppVersionResourcesResponseTypeDef = TypedDict(
    "ResolveAppVersionResourcesResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "resolutionId": str,
        "status": ResourceResolutionStatusTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceDriftTypeDef = TypedDict(
    "ResourceDriftTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "diffType": DifferenceTypeType,
        "referenceId": str,
        "resourceIdentifier": "ResourceIdentifierTypeDef",
    },
    total=False,
)

ResourceErrorTypeDef = TypedDict(
    "ResourceErrorTypeDef",
    {
        "logicalResourceId": str,
        "physicalResourceId": str,
        "reason": str,
    },
    total=False,
)

ResourceErrorsDetailsTypeDef = TypedDict(
    "ResourceErrorsDetailsTypeDef",
    {
        "hasMoreErrors": bool,
        "resourceErrors": List["ResourceErrorTypeDef"],
    },
    total=False,
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "resourceType": str,
    },
    total=False,
)

_RequiredResourceMappingTypeDef = TypedDict(
    "_RequiredResourceMappingTypeDef",
    {
        "mappingType": ResourceMappingTypeType,
        "physicalResourceId": "PhysicalResourceIdTypeDef",
    },
)
_OptionalResourceMappingTypeDef = TypedDict(
    "_OptionalResourceMappingTypeDef",
    {
        "appRegistryAppName": str,
        "eksSourceName": str,
        "logicalStackName": str,
        "resourceGroupName": str,
        "resourceName": str,
        "terraformSourceName": str,
    },
    total=False,
)

class ResourceMappingTypeDef(_RequiredResourceMappingTypeDef, _OptionalResourceMappingTypeDef):
    pass

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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucket": str,
        "prefix": str,
    },
    total=False,
)

ScoringComponentResiliencyScoreTypeDef = TypedDict(
    "ScoringComponentResiliencyScoreTypeDef",
    {
        "excludedCount": int,
        "outstandingCount": int,
        "possibleScore": float,
        "score": float,
    },
    total=False,
)

_RequiredSopRecommendationTypeDef = TypedDict(
    "_RequiredSopRecommendationTypeDef",
    {
        "recommendationId": str,
        "referenceId": str,
        "serviceType": Literal["SSM"],
    },
)
_OptionalSopRecommendationTypeDef = TypedDict(
    "_OptionalSopRecommendationTypeDef",
    {
        "appComponentName": str,
        "description": str,
        "items": List["RecommendationItemTypeDef"],
        "name": str,
        "prerequisite": str,
        "recommendationStatus": RecommendationStatusType,
    },
    total=False,
)

class SopRecommendationTypeDef(
    _RequiredSopRecommendationTypeDef, _OptionalSopRecommendationTypeDef
):
    pass

_RequiredStartAppAssessmentRequestRequestTypeDef = TypedDict(
    "_RequiredStartAppAssessmentRequestRequestTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "assessmentName": str,
    },
)
_OptionalStartAppAssessmentRequestRequestTypeDef = TypedDict(
    "_OptionalStartAppAssessmentRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class StartAppAssessmentRequestRequestTypeDef(
    _RequiredStartAppAssessmentRequestRequestTypeDef,
    _OptionalStartAppAssessmentRequestRequestTypeDef,
):
    pass

StartAppAssessmentResponseTypeDef = TypedDict(
    "StartAppAssessmentResponseTypeDef",
    {
        "assessment": "AppAssessmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TerraformSourceTypeDef = TypedDict(
    "TerraformSourceTypeDef",
    {
        "s3StateFileUrl": str,
    },
)

_RequiredTestRecommendationTypeDef = TypedDict(
    "_RequiredTestRecommendationTypeDef",
    {
        "referenceId": str,
    },
)
_OptionalTestRecommendationTypeDef = TypedDict(
    "_OptionalTestRecommendationTypeDef",
    {
        "appComponentName": str,
        "dependsOnAlarms": List[str],
        "description": str,
        "intent": str,
        "items": List["RecommendationItemTypeDef"],
        "name": str,
        "prerequisite": str,
        "recommendationId": str,
        "recommendationStatus": RecommendationStatusType,
        "risk": TestRiskType,
        "type": TestTypeType,
    },
    total=False,
)

class TestRecommendationTypeDef(
    _RequiredTestRecommendationTypeDef, _OptionalTestRecommendationTypeDef
):
    pass

_RequiredUnsupportedResourceTypeDef = TypedDict(
    "_RequiredUnsupportedResourceTypeDef",
    {
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "physicalResourceId": "PhysicalResourceIdTypeDef",
        "resourceType": str,
    },
)
_OptionalUnsupportedResourceTypeDef = TypedDict(
    "_OptionalUnsupportedResourceTypeDef",
    {
        "unsupportedResourceStatus": str,
    },
    total=False,
)

class UnsupportedResourceTypeDef(
    _RequiredUnsupportedResourceTypeDef, _OptionalUnsupportedResourceTypeDef
):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAppRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalUpdateAppRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppRequestRequestTypeDef",
    {
        "assessmentSchedule": AppAssessmentScheduleTypeType,
        "clearResiliencyPolicyArn": bool,
        "description": str,
        "eventSubscriptions": List["EventSubscriptionTypeDef"],
        "permissionModel": "PermissionModelTypeDef",
        "policyArn": str,
    },
    total=False,
)

class UpdateAppRequestRequestTypeDef(
    _RequiredUpdateAppRequestRequestTypeDef, _OptionalUpdateAppRequestRequestTypeDef
):
    pass

UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "app": "AppTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAppVersionAppComponentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppVersionAppComponentRequestRequestTypeDef",
    {
        "appArn": str,
        "id": str,
    },
)
_OptionalUpdateAppVersionAppComponentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppVersionAppComponentRequestRequestTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
        "name": str,
        "type": str,
    },
    total=False,
)

class UpdateAppVersionAppComponentRequestRequestTypeDef(
    _RequiredUpdateAppVersionAppComponentRequestRequestTypeDef,
    _OptionalUpdateAppVersionAppComponentRequestRequestTypeDef,
):
    pass

UpdateAppVersionAppComponentResponseTypeDef = TypedDict(
    "UpdateAppVersionAppComponentResponseTypeDef",
    {
        "appArn": str,
        "appComponent": "AppComponentTypeDef",
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAppVersionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppVersionRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalUpdateAppVersionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppVersionRequestRequestTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
    },
    total=False,
)

class UpdateAppVersionRequestRequestTypeDef(
    _RequiredUpdateAppVersionRequestRequestTypeDef, _OptionalUpdateAppVersionRequestRequestTypeDef
):
    pass

_RequiredUpdateAppVersionResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAppVersionResourceRequestRequestTypeDef",
    {
        "appArn": str,
    },
)
_OptionalUpdateAppVersionResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAppVersionResourceRequestRequestTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
        "appComponents": List[str],
        "awsAccountId": str,
        "awsRegion": str,
        "excluded": bool,
        "logicalResourceId": "LogicalResourceIdTypeDef",
        "physicalResourceId": str,
        "resourceName": str,
        "resourceType": str,
    },
    total=False,
)

class UpdateAppVersionResourceRequestRequestTypeDef(
    _RequiredUpdateAppVersionResourceRequestRequestTypeDef,
    _OptionalUpdateAppVersionResourceRequestRequestTypeDef,
):
    pass

UpdateAppVersionResourceResponseTypeDef = TypedDict(
    "UpdateAppVersionResourceResponseTypeDef",
    {
        "appArn": str,
        "appVersion": str,
        "physicalResource": "PhysicalResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppVersionResponseTypeDef = TypedDict(
    "UpdateAppVersionResponseTypeDef",
    {
        "additionalInfo": Dict[str, List[str]],
        "appArn": str,
        "appVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecommendationStatusItemTypeDef = TypedDict(
    "UpdateRecommendationStatusItemTypeDef",
    {
        "resourceId": str,
        "targetAccountId": str,
        "targetRegion": str,
    },
    total=False,
)

_RequiredUpdateRecommendationStatusRequestEntryTypeDef = TypedDict(
    "_RequiredUpdateRecommendationStatusRequestEntryTypeDef",
    {
        "entryId": str,
        "excluded": bool,
        "item": "UpdateRecommendationStatusItemTypeDef",
        "referenceId": str,
    },
)
_OptionalUpdateRecommendationStatusRequestEntryTypeDef = TypedDict(
    "_OptionalUpdateRecommendationStatusRequestEntryTypeDef",
    {
        "excludeReason": ExcludeRecommendationReasonType,
    },
    total=False,
)

class UpdateRecommendationStatusRequestEntryTypeDef(
    _RequiredUpdateRecommendationStatusRequestEntryTypeDef,
    _OptionalUpdateRecommendationStatusRequestEntryTypeDef,
):
    pass

_RequiredUpdateResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateResiliencyPolicyRequestRequestTypeDef",
    {
        "policyArn": str,
    },
)
_OptionalUpdateResiliencyPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateResiliencyPolicyRequestRequestTypeDef",
    {
        "dataLocationConstraint": DataLocationConstraintType,
        "policy": Dict[DisruptionTypeType, "FailurePolicyTypeDef"],
        "policyDescription": str,
        "policyName": str,
        "tier": ResiliencyPolicyTierType,
    },
    total=False,
)

class UpdateResiliencyPolicyRequestRequestTypeDef(
    _RequiredUpdateResiliencyPolicyRequestRequestTypeDef,
    _OptionalUpdateResiliencyPolicyRequestRequestTypeDef,
):
    pass

UpdateResiliencyPolicyResponseTypeDef = TypedDict(
    "UpdateResiliencyPolicyResponseTypeDef",
    {
        "policy": "ResiliencyPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
