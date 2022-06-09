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
    "AppStatusTypeType",
    "AssessmentInvokerType",
    "AssessmentStatusType",
    "ComplianceStatusType",
    "ConfigRecommendationOptimizationTypeType",
    "CostFrequencyType",
    "DataLocationConstraintType",
    "DisruptionTypeType",
    "EstimatedCostTierType",
    "HaArchitectureType",
    "PhysicalIdentifierTypeType",
    "RecommendationComplianceStatusType",
    "RecommendationTemplateStatusType",
    "RenderRecommendationTypeType",
    "ResiliencyPolicyTierType",
    "ResourceImportStatusTypeType",
    "ResourceMappingTypeType",
    "ResourceResolutionStatusTypeType",
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
AppStatusTypeType = Literal["Active", "Deleting"]
AssessmentInvokerType = Literal["System", "User"]
AssessmentStatusType = Literal["Failed", "InProgress", "Pending", "Success"]
ComplianceStatusType = Literal["PolicyBreached", "PolicyMet"]
ConfigRecommendationOptimizationTypeType = Literal[
    "BestAZRecovery", "BestAttainable", "LeastChange", "LeastCost", "LeastErrors"
]
CostFrequencyType = Literal["Daily", "Hourly", "Monthly", "Yearly"]
DataLocationConstraintType = Literal["AnyLocation", "SameContinent", "SameCountry"]
DisruptionTypeType = Literal["AZ", "Hardware", "Region", "Software"]
EstimatedCostTierType = Literal["L1", "L2", "L3", "L4"]
HaArchitectureType = Literal[
    "BackupAndRestore", "MultiSite", "NoRecoveryPlan", "PilotLight", "WarmStandby"
]
PhysicalIdentifierTypeType = Literal["Arn", "Native"]
RecommendationComplianceStatusType = Literal[
    "BreachedCanMeet", "BreachedUnattainable", "MetCanImprove"
]
RecommendationTemplateStatusType = Literal["Failed", "InProgress", "Pending", "Success"]
RenderRecommendationTypeType = Literal["Alarm", "Sop", "Test"]
ResiliencyPolicyTierType = Literal[
    "CoreServices", "Critical", "Important", "MissionCritical", "NonCritical"
]
ResourceImportStatusTypeType = Literal["Failed", "InProgress", "Pending", "Success"]
ResourceMappingTypeType = Literal[
    "AppRegistryApp", "CfnStack", "Resource", "ResourceGroup", "Terraform"
]
ResourceResolutionStatusTypeType = Literal["Failed", "InProgress", "Pending", "Success"]
SopServiceTypeType = Literal["SSM"]
TemplateFormatType = Literal["CfnJson", "CfnYaml"]
TestRiskType = Literal["High", "Medium", "Small"]
TestTypeType = Literal["AZ", "Hardware", "Region", "Software"]
