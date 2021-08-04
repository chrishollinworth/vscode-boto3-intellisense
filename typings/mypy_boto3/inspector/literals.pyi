"""
Type annotations for inspector service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector/literals.html)

Usage::

    ```python
    from mypy_boto3_inspector.literals import AgentHealthCodeType

    data: AgentHealthCodeType = "IDLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AgentHealthCodeType",
    "AgentHealthType",
    "AssessmentRunNotificationSnsStatusCodeType",
    "AssessmentRunStateType",
    "AssetTypeType",
    "FailedItemErrorCodeType",
    "InspectorEventType",
    "ListAssessmentRunAgentsPaginatorName",
    "ListAssessmentRunsPaginatorName",
    "ListAssessmentTargetsPaginatorName",
    "ListAssessmentTemplatesPaginatorName",
    "ListEventSubscriptionsPaginatorName",
    "ListExclusionsPaginatorName",
    "ListFindingsPaginatorName",
    "ListRulesPackagesPaginatorName",
    "LocaleType",
    "PreviewAgentsPaginatorName",
    "PreviewStatusType",
    "ReportFileFormatType",
    "ReportStatusType",
    "ReportTypeType",
    "ScopeTypeType",
    "SeverityType",
    "StopActionType",
)

AgentHealthCodeType = Literal["IDLE", "RUNNING", "SHUTDOWN", "THROTTLED", "UNHEALTHY", "UNKNOWN"]
AgentHealthType = Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
AssessmentRunNotificationSnsStatusCodeType = Literal[
    "ACCESS_DENIED", "INTERNAL_ERROR", "SUCCESS", "TOPIC_DOES_NOT_EXIST"
]
AssessmentRunStateType = Literal[
    "CANCELED",
    "COLLECTING_DATA",
    "COMPLETED",
    "COMPLETED_WITH_ERRORS",
    "CREATED",
    "DATA_COLLECTED",
    "ERROR",
    "EVALUATING_RULES",
    "FAILED",
    "START_DATA_COLLECTION_IN_PROGRESS",
    "START_DATA_COLLECTION_PENDING",
    "START_EVALUATING_RULES_PENDING",
    "STOP_DATA_COLLECTION_PENDING",
]
AssetTypeType = Literal["ec2-instance"]
FailedItemErrorCodeType = Literal[
    "ACCESS_DENIED",
    "DUPLICATE_ARN",
    "INTERNAL_ERROR",
    "INVALID_ARN",
    "ITEM_DOES_NOT_EXIST",
    "LIMIT_EXCEEDED",
]
InspectorEventType = Literal[
    "ASSESSMENT_RUN_COMPLETED",
    "ASSESSMENT_RUN_STARTED",
    "ASSESSMENT_RUN_STATE_CHANGED",
    "FINDING_REPORTED",
    "OTHER",
]
ListAssessmentRunAgentsPaginatorName = Literal["list_assessment_run_agents"]
ListAssessmentRunsPaginatorName = Literal["list_assessment_runs"]
ListAssessmentTargetsPaginatorName = Literal["list_assessment_targets"]
ListAssessmentTemplatesPaginatorName = Literal["list_assessment_templates"]
ListEventSubscriptionsPaginatorName = Literal["list_event_subscriptions"]
ListExclusionsPaginatorName = Literal["list_exclusions"]
ListFindingsPaginatorName = Literal["list_findings"]
ListRulesPackagesPaginatorName = Literal["list_rules_packages"]
LocaleType = Literal["EN_US"]
PreviewAgentsPaginatorName = Literal["preview_agents"]
PreviewStatusType = Literal["COMPLETED", "WORK_IN_PROGRESS"]
ReportFileFormatType = Literal["HTML", "PDF"]
ReportStatusType = Literal["COMPLETED", "FAILED", "WORK_IN_PROGRESS"]
ReportTypeType = Literal["FINDING", "FULL"]
ScopeTypeType = Literal["INSTANCE_ID", "RULES_PACKAGE_ARN"]
SeverityType = Literal["High", "Informational", "Low", "Medium", "Undefined"]
StopActionType = Literal["SKIP_EVALUATION", "START_EVALUATION"]
