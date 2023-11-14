"""
Type annotations for resiliencehub service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resiliencehub/literals.html)

Usage::

    ```python
    from mypy_boto3_resiliencehub.literals import AlarmTypeType

    data: AlarmTypeType = "Canary"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AlarmTypeType",
    "AppAssessmentScheduleTypeType",
    "AppComplianceStatusTypeType",
    "AppDriftStatusTypeType",
    "AppStatusTypeType",
    "AssessmentInvokerType",
    "AssessmentStatusType",
    "ComplianceStatusType",
    "ConfigRecommendationOptimizationTypeType",
    "CostFrequencyType",
    "DataLocationConstraintType",
    "DifferenceTypeType",
    "DisruptionTypeType",
    "DriftStatusType",
    "DriftTypeType",
    "EstimatedCostTierType",
    "EventTypeType",
    "ExcludeRecommendationReasonType",
    "HaArchitectureType",
    "PermissionModelTypeType",
    "PhysicalIdentifierTypeType",
    "RecommendationComplianceStatusType",
    "RecommendationStatusType",
    "RecommendationTemplateStatusType",
    "RenderRecommendationTypeType",
    "ResiliencyPolicyTierType",
    "ResiliencyScoreTypeType",
    "ResourceImportStatusTypeType",
    "ResourceImportStrategyTypeType",
    "ResourceMappingTypeType",
    "ResourceResolutionStatusTypeType",
    "ResourceSourceTypeType",
    "SopServiceTypeType",
    "TemplateFormatType",
    "TestRiskType",
    "TestTypeType",
)

AlarmTypeType = Literal["Canary", "Composite", "Event", "Logs", "Metric"]
AppAssessmentScheduleTypeType = Literal["Daily", "Disabled"]
AppComplianceStatusTypeType = Literal[
    "ChangesDetected", "NotAssessed", "PolicyBreached", "PolicyMet"
]
AppDriftStatusTypeType = Literal["Detected", "NotChecked", "NotDetected"]
AppStatusTypeType = Literal["Active", "Deleting"]
AssessmentInvokerType = Literal["System", "User"]
AssessmentStatusType = Literal["Failed", "InProgress", "Pending", "Success"]
ComplianceStatusType = Literal["PolicyBreached", "PolicyMet"]
ConfigRecommendationOptimizationTypeType = Literal[
    "BestAZRecovery",
    "BestAttainable",
    "BestRegionRecovery",
    "LeastChange",
    "LeastCost",
    "LeastErrors",
]
CostFrequencyType = Literal["Daily", "Hourly", "Monthly", "Yearly"]
DataLocationConstraintType = Literal["AnyLocation", "SameContinent", "SameCountry"]
DifferenceTypeType = Literal["NotEqual"]
DisruptionTypeType = Literal["AZ", "Hardware", "Region", "Software"]
DriftStatusType = Literal["Detected", "NotChecked", "NotDetected"]
DriftTypeType = Literal["ApplicationCompliance"]
EstimatedCostTierType = Literal["L1", "L2", "L3", "L4"]
EventTypeType = Literal["DriftDetected", "ScheduledAssessmentFailure"]
ExcludeRecommendationReasonType = Literal[
    "AlreadyImplemented", "ComplexityOfImplementation", "NotRelevant"
]
HaArchitectureType = Literal[
    "BackupAndRestore", "MultiSite", "NoRecoveryPlan", "PilotLight", "WarmStandby"
]
PermissionModelTypeType = Literal["LegacyIAMUser", "RoleBased"]
PhysicalIdentifierTypeType = Literal["Arn", "Native"]
RecommendationComplianceStatusType = Literal[
    "BreachedCanMeet", "BreachedUnattainable", "MetCanImprove"
]
RecommendationStatusType = Literal["Excluded", "Implemented", "Inactive", "NotImplemented"]
RecommendationTemplateStatusType = Literal["Failed", "InProgress", "Pending", "Success"]
RenderRecommendationTypeType = Literal["Alarm", "Sop", "Test"]
ResiliencyPolicyTierType = Literal[
    "CoreServices", "Critical", "Important", "MissionCritical", "NonCritical", "NotApplicable"
]
ResiliencyScoreTypeType = Literal["Alarm", "Compliance", "Sop", "Test"]
ResourceImportStatusTypeType = Literal["Failed", "InProgress", "Pending", "Success"]
ResourceImportStrategyTypeType = Literal["AddOnly", "ReplaceAll"]
ResourceMappingTypeType = Literal[
    "AppRegistryApp", "CfnStack", "EKS", "Resource", "ResourceGroup", "Terraform"
]
ResourceResolutionStatusTypeType = Literal["Failed", "InProgress", "Pending", "Success"]
ResourceSourceTypeType = Literal["AppTemplate", "Discovered"]
SopServiceTypeType = Literal["SSM"]
TemplateFormatType = Literal["CfnJson", "CfnYaml"]
TestRiskType = Literal["High", "Medium", "Small"]
TestTypeType = Literal["AZ", "Hardware", "Region", "Software"]
