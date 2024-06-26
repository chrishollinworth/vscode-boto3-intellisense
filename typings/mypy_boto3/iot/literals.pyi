"""
Type annotations for iot service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/literals.html)

Usage::

    ```python
    from mypy_boto3_iot.literals import AbortActionType

    data: AbortActionType = "CANCEL"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AbortActionType",
    "ActionTypeType",
    "AggregationTypeNameType",
    "AlertTargetTypeType",
    "AuditCheckRunStatusType",
    "AuditFindingSeverityType",
    "AuditFrequencyType",
    "AuditMitigationActionsExecutionStatusType",
    "AuditMitigationActionsTaskStatusType",
    "AuditNotificationTypeType",
    "AuditTaskStatusType",
    "AuditTaskTypeType",
    "AuthDecisionType",
    "AuthorizerStatusType",
    "AutoRegistrationStatusType",
    "AwsJobAbortCriteriaAbortActionType",
    "AwsJobAbortCriteriaFailureTypeType",
    "BehaviorCriteriaTypeType",
    "CACertificateStatusType",
    "CACertificateUpdateActionType",
    "CannedAccessControlListType",
    "CertificateModeType",
    "CertificateProviderOperationType",
    "CertificateStatusType",
    "ComparisonOperatorType",
    "ConfidenceLevelType",
    "CustomMetricTypeType",
    "DayOfWeekType",
    "DetectMitigationActionExecutionStatusType",
    "DetectMitigationActionsTaskStatusType",
    "DeviceCertificateUpdateActionType",
    "DeviceDefenderIndexingModeType",
    "DimensionTypeType",
    "DimensionValueOperatorType",
    "DomainConfigurationStatusType",
    "DomainTypeType",
    "DynamicGroupStatusType",
    "DynamoKeyTypeType",
    "EventTypeType",
    "FieldTypeType",
    "FleetMetricUnitType",
    "GetBehaviorModelTrainingSummariesPaginatorName",
    "IndexStatusType",
    "JobEndBehaviorType",
    "JobExecutionFailureTypeType",
    "JobExecutionStatusType",
    "JobStatusType",
    "ListActiveViolationsPaginatorName",
    "ListAttachedPoliciesPaginatorName",
    "ListAuditFindingsPaginatorName",
    "ListAuditMitigationActionsExecutionsPaginatorName",
    "ListAuditMitigationActionsTasksPaginatorName",
    "ListAuditSuppressionsPaginatorName",
    "ListAuditTasksPaginatorName",
    "ListAuthorizersPaginatorName",
    "ListBillingGroupsPaginatorName",
    "ListCACertificatesPaginatorName",
    "ListCertificatesByCAPaginatorName",
    "ListCertificatesPaginatorName",
    "ListCustomMetricsPaginatorName",
    "ListDetectMitigationActionsExecutionsPaginatorName",
    "ListDetectMitigationActionsTasksPaginatorName",
    "ListDimensionsPaginatorName",
    "ListDomainConfigurationsPaginatorName",
    "ListFleetMetricsPaginatorName",
    "ListIndicesPaginatorName",
    "ListJobExecutionsForJobPaginatorName",
    "ListJobExecutionsForThingPaginatorName",
    "ListJobTemplatesPaginatorName",
    "ListJobsPaginatorName",
    "ListManagedJobTemplatesPaginatorName",
    "ListMetricValuesPaginatorName",
    "ListMitigationActionsPaginatorName",
    "ListOTAUpdatesPaginatorName",
    "ListOutgoingCertificatesPaginatorName",
    "ListPackageVersionsPaginatorName",
    "ListPackagesPaginatorName",
    "ListPoliciesPaginatorName",
    "ListPolicyPrincipalsPaginatorName",
    "ListPrincipalPoliciesPaginatorName",
    "ListPrincipalThingsPaginatorName",
    "ListProvisioningTemplateVersionsPaginatorName",
    "ListProvisioningTemplatesPaginatorName",
    "ListRelatedResourcesForAuditFindingPaginatorName",
    "ListRoleAliasesPaginatorName",
    "ListScheduledAuditsPaginatorName",
    "ListSecurityProfilesForTargetPaginatorName",
    "ListSecurityProfilesPaginatorName",
    "ListStreamsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTargetsForPolicyPaginatorName",
    "ListTargetsForSecurityProfilePaginatorName",
    "ListThingGroupsForThingPaginatorName",
    "ListThingGroupsPaginatorName",
    "ListThingPrincipalsPaginatorName",
    "ListThingRegistrationTaskReportsPaginatorName",
    "ListThingRegistrationTasksPaginatorName",
    "ListThingTypesPaginatorName",
    "ListThingsInBillingGroupPaginatorName",
    "ListThingsInThingGroupPaginatorName",
    "ListThingsPaginatorName",
    "ListTopicRuleDestinationsPaginatorName",
    "ListTopicRulesPaginatorName",
    "ListV2LoggingLevelsPaginatorName",
    "ListViolationEventsPaginatorName",
    "LogLevelType",
    "LogTargetTypeType",
    "MessageFormatType",
    "MitigationActionTypeType",
    "ModelStatusType",
    "NamedShadowIndexingModeType",
    "OTAUpdateStatusType",
    "PackageVersionActionType",
    "PackageVersionStatusType",
    "PolicyTemplateNameType",
    "ProtocolType",
    "ReportTypeType",
    "ResourceTypeType",
    "RetryableFailureTypeType",
    "ServerCertificateStatusType",
    "ServiceTypeType",
    "StatusType",
    "TargetFieldOrderType",
    "TargetSelectionType",
    "TemplateTypeType",
    "ThingConnectivityIndexingModeType",
    "ThingGroupIndexingModeType",
    "ThingIndexingModeType",
    "TopicRuleDestinationStatusType",
    "VerificationStateType",
    "ViolationEventTypeType",
)

AbortActionType = Literal["CANCEL"]
ActionTypeType = Literal["CONNECT", "PUBLISH", "RECEIVE", "SUBSCRIBE"]
AggregationTypeNameType = Literal["Cardinality", "Percentiles", "Statistics"]
AlertTargetTypeType = Literal["SNS"]
AuditCheckRunStatusType = Literal[
    "CANCELED",
    "COMPLETED_COMPLIANT",
    "COMPLETED_NON_COMPLIANT",
    "FAILED",
    "IN_PROGRESS",
    "WAITING_FOR_DATA_COLLECTION",
]
AuditFindingSeverityType = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM"]
AuditFrequencyType = Literal["BIWEEKLY", "DAILY", "MONTHLY", "WEEKLY"]
AuditMitigationActionsExecutionStatusType = Literal[
    "CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "SKIPPED"
]
AuditMitigationActionsTaskStatusType = Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
AuditNotificationTypeType = Literal["SNS"]
AuditTaskStatusType = Literal["CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS"]
AuditTaskTypeType = Literal["ON_DEMAND_AUDIT_TASK", "SCHEDULED_AUDIT_TASK"]
AuthDecisionType = Literal["ALLOWED", "EXPLICIT_DENY", "IMPLICIT_DENY"]
AuthorizerStatusType = Literal["ACTIVE", "INACTIVE"]
AutoRegistrationStatusType = Literal["DISABLE", "ENABLE"]
AwsJobAbortCriteriaAbortActionType = Literal["CANCEL"]
AwsJobAbortCriteriaFailureTypeType = Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"]
BehaviorCriteriaTypeType = Literal["MACHINE_LEARNING", "STATIC", "STATISTICAL"]
CACertificateStatusType = Literal["ACTIVE", "INACTIVE"]
CACertificateUpdateActionType = Literal["DEACTIVATE"]
CannedAccessControlListType = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "log-delivery-write",
    "private",
    "public-read",
    "public-read-write",
]
CertificateModeType = Literal["DEFAULT", "SNI_ONLY"]
CertificateProviderOperationType = Literal["CreateCertificateFromCsr"]
CertificateStatusType = Literal[
    "ACTIVE", "INACTIVE", "PENDING_ACTIVATION", "PENDING_TRANSFER", "REGISTER_INACTIVE", "REVOKED"
]
ComparisonOperatorType = Literal[
    "greater-than",
    "greater-than-equals",
    "in-cidr-set",
    "in-port-set",
    "in-set",
    "less-than",
    "less-than-equals",
    "not-in-cidr-set",
    "not-in-port-set",
    "not-in-set",
]
ConfidenceLevelType = Literal["HIGH", "LOW", "MEDIUM"]
CustomMetricTypeType = Literal["ip-address-list", "number", "number-list", "string-list"]
DayOfWeekType = Literal["FRI", "MON", "SAT", "SUN", "THU", "TUE", "WED"]
DetectMitigationActionExecutionStatusType = Literal[
    "FAILED", "IN_PROGRESS", "SKIPPED", "SUCCESSFUL"
]
DetectMitigationActionsTaskStatusType = Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCESSFUL"]
DeviceCertificateUpdateActionType = Literal["DEACTIVATE"]
DeviceDefenderIndexingModeType = Literal["OFF", "VIOLATIONS"]
DimensionTypeType = Literal["TOPIC_FILTER"]
DimensionValueOperatorType = Literal["IN", "NOT_IN"]
DomainConfigurationStatusType = Literal["DISABLED", "ENABLED"]
DomainTypeType = Literal["AWS_MANAGED", "CUSTOMER_MANAGED", "ENDPOINT"]
DynamicGroupStatusType = Literal["ACTIVE", "BUILDING", "REBUILDING"]
DynamoKeyTypeType = Literal["NUMBER", "STRING"]
EventTypeType = Literal[
    "CA_CERTIFICATE",
    "CERTIFICATE",
    "JOB",
    "JOB_EXECUTION",
    "POLICY",
    "THING",
    "THING_GROUP",
    "THING_GROUP_HIERARCHY",
    "THING_GROUP_MEMBERSHIP",
    "THING_TYPE",
    "THING_TYPE_ASSOCIATION",
]
FieldTypeType = Literal["Boolean", "Number", "String"]
FleetMetricUnitType = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
GetBehaviorModelTrainingSummariesPaginatorName = Literal["get_behavior_model_training_summaries"]
IndexStatusType = Literal["ACTIVE", "BUILDING", "REBUILDING"]
JobEndBehaviorType = Literal["CANCEL", "FORCE_CANCEL", "STOP_ROLLOUT"]
JobExecutionFailureTypeType = Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"]
JobExecutionStatusType = Literal[
    "CANCELED", "FAILED", "IN_PROGRESS", "QUEUED", "REJECTED", "REMOVED", "SUCCEEDED", "TIMED_OUT"
]
JobStatusType = Literal["CANCELED", "COMPLETED", "DELETION_IN_PROGRESS", "IN_PROGRESS", "SCHEDULED"]
ListActiveViolationsPaginatorName = Literal["list_active_violations"]
ListAttachedPoliciesPaginatorName = Literal["list_attached_policies"]
ListAuditFindingsPaginatorName = Literal["list_audit_findings"]
ListAuditMitigationActionsExecutionsPaginatorName = Literal[
    "list_audit_mitigation_actions_executions"
]
ListAuditMitigationActionsTasksPaginatorName = Literal["list_audit_mitigation_actions_tasks"]
ListAuditSuppressionsPaginatorName = Literal["list_audit_suppressions"]
ListAuditTasksPaginatorName = Literal["list_audit_tasks"]
ListAuthorizersPaginatorName = Literal["list_authorizers"]
ListBillingGroupsPaginatorName = Literal["list_billing_groups"]
ListCACertificatesPaginatorName = Literal["list_ca_certificates"]
ListCertificatesByCAPaginatorName = Literal["list_certificates_by_ca"]
ListCertificatesPaginatorName = Literal["list_certificates"]
ListCustomMetricsPaginatorName = Literal["list_custom_metrics"]
ListDetectMitigationActionsExecutionsPaginatorName = Literal[
    "list_detect_mitigation_actions_executions"
]
ListDetectMitigationActionsTasksPaginatorName = Literal["list_detect_mitigation_actions_tasks"]
ListDimensionsPaginatorName = Literal["list_dimensions"]
ListDomainConfigurationsPaginatorName = Literal["list_domain_configurations"]
ListFleetMetricsPaginatorName = Literal["list_fleet_metrics"]
ListIndicesPaginatorName = Literal["list_indices"]
ListJobExecutionsForJobPaginatorName = Literal["list_job_executions_for_job"]
ListJobExecutionsForThingPaginatorName = Literal["list_job_executions_for_thing"]
ListJobTemplatesPaginatorName = Literal["list_job_templates"]
ListJobsPaginatorName = Literal["list_jobs"]
ListManagedJobTemplatesPaginatorName = Literal["list_managed_job_templates"]
ListMetricValuesPaginatorName = Literal["list_metric_values"]
ListMitigationActionsPaginatorName = Literal["list_mitigation_actions"]
ListOTAUpdatesPaginatorName = Literal["list_ota_updates"]
ListOutgoingCertificatesPaginatorName = Literal["list_outgoing_certificates"]
ListPackageVersionsPaginatorName = Literal["list_package_versions"]
ListPackagesPaginatorName = Literal["list_packages"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListPolicyPrincipalsPaginatorName = Literal["list_policy_principals"]
ListPrincipalPoliciesPaginatorName = Literal["list_principal_policies"]
ListPrincipalThingsPaginatorName = Literal["list_principal_things"]
ListProvisioningTemplateVersionsPaginatorName = Literal["list_provisioning_template_versions"]
ListProvisioningTemplatesPaginatorName = Literal["list_provisioning_templates"]
ListRelatedResourcesForAuditFindingPaginatorName = Literal[
    "list_related_resources_for_audit_finding"
]
ListRoleAliasesPaginatorName = Literal["list_role_aliases"]
ListScheduledAuditsPaginatorName = Literal["list_scheduled_audits"]
ListSecurityProfilesForTargetPaginatorName = Literal["list_security_profiles_for_target"]
ListSecurityProfilesPaginatorName = Literal["list_security_profiles"]
ListStreamsPaginatorName = Literal["list_streams"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTargetsForPolicyPaginatorName = Literal["list_targets_for_policy"]
ListTargetsForSecurityProfilePaginatorName = Literal["list_targets_for_security_profile"]
ListThingGroupsForThingPaginatorName = Literal["list_thing_groups_for_thing"]
ListThingGroupsPaginatorName = Literal["list_thing_groups"]
ListThingPrincipalsPaginatorName = Literal["list_thing_principals"]
ListThingRegistrationTaskReportsPaginatorName = Literal["list_thing_registration_task_reports"]
ListThingRegistrationTasksPaginatorName = Literal["list_thing_registration_tasks"]
ListThingTypesPaginatorName = Literal["list_thing_types"]
ListThingsInBillingGroupPaginatorName = Literal["list_things_in_billing_group"]
ListThingsInThingGroupPaginatorName = Literal["list_things_in_thing_group"]
ListThingsPaginatorName = Literal["list_things"]
ListTopicRuleDestinationsPaginatorName = Literal["list_topic_rule_destinations"]
ListTopicRulesPaginatorName = Literal["list_topic_rules"]
ListV2LoggingLevelsPaginatorName = Literal["list_v2_logging_levels"]
ListViolationEventsPaginatorName = Literal["list_violation_events"]
LogLevelType = Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARN"]
LogTargetTypeType = Literal["CLIENT_ID", "DEFAULT", "PRINCIPAL_ID", "SOURCE_IP", "THING_GROUP"]
MessageFormatType = Literal["JSON", "RAW"]
MitigationActionTypeType = Literal[
    "ADD_THINGS_TO_THING_GROUP",
    "ENABLE_IOT_LOGGING",
    "PUBLISH_FINDING_TO_SNS",
    "REPLACE_DEFAULT_POLICY_VERSION",
    "UPDATE_CA_CERTIFICATE",
    "UPDATE_DEVICE_CERTIFICATE",
]
ModelStatusType = Literal["ACTIVE", "EXPIRED", "PENDING_BUILD"]
NamedShadowIndexingModeType = Literal["OFF", "ON"]
OTAUpdateStatusType = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_PENDING",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
]
PackageVersionActionType = Literal["DEPRECATE", "PUBLISH"]
PackageVersionStatusType = Literal["DEPRECATED", "DRAFT", "PUBLISHED"]
PolicyTemplateNameType = Literal["BLANK_POLICY"]
ProtocolType = Literal["HTTP", "MQTT"]
ReportTypeType = Literal["ERRORS", "RESULTS"]
ResourceTypeType = Literal[
    "ACCOUNT_SETTINGS",
    "CA_CERTIFICATE",
    "CLIENT_ID",
    "COGNITO_IDENTITY_POOL",
    "DEVICE_CERTIFICATE",
    "IAM_ROLE",
    "IOT_POLICY",
    "ISSUER_CERTIFICATE",
    "ROLE_ALIAS",
]
RetryableFailureTypeType = Literal["ALL", "FAILED", "TIMED_OUT"]
ServerCertificateStatusType = Literal["INVALID", "VALID"]
ServiceTypeType = Literal["CREDENTIAL_PROVIDER", "DATA", "JOBS"]
StatusType = Literal["Cancelled", "Cancelling", "Completed", "Failed", "InProgress"]
TargetFieldOrderType = Literal["LatLon", "LonLat"]
TargetSelectionType = Literal["CONTINUOUS", "SNAPSHOT"]
TemplateTypeType = Literal["FLEET_PROVISIONING", "JITP"]
ThingConnectivityIndexingModeType = Literal["OFF", "STATUS"]
ThingGroupIndexingModeType = Literal["OFF", "ON"]
ThingIndexingModeType = Literal["OFF", "REGISTRY", "REGISTRY_AND_SHADOW"]
TopicRuleDestinationStatusType = Literal["DELETING", "DISABLED", "ENABLED", "ERROR", "IN_PROGRESS"]
VerificationStateType = Literal["BENIGN_POSITIVE", "FALSE_POSITIVE", "TRUE_POSITIVE", "UNKNOWN"]
ViolationEventTypeType = Literal["alarm-cleared", "alarm-invalidated", "in-alarm"]
