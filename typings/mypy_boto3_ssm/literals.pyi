"""
Type annotations for ssm service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/literals.html)

Usage::

    ```python
    from mypy_boto3_ssm.literals import AssociationComplianceSeverityType

    data: AssociationComplianceSeverityType = "CRITICAL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssociationComplianceSeverityType",
    "AssociationExecutionFilterKeyType",
    "AssociationExecutionTargetsFilterKeyType",
    "AssociationFilterKeyType",
    "AssociationFilterOperatorTypeType",
    "AssociationStatusNameType",
    "AssociationSyncComplianceType",
    "AttachmentHashTypeType",
    "AttachmentsSourceKeyType",
    "AutomationExecutionFilterKeyType",
    "AutomationExecutionStatusType",
    "AutomationSubtypeType",
    "AutomationTypeType",
    "CalendarStateType",
    "CommandExecutedWaiterName",
    "CommandFilterKeyType",
    "CommandInvocationStatusType",
    "CommandPluginStatusType",
    "CommandStatusType",
    "ComplianceQueryOperatorTypeType",
    "ComplianceSeverityType",
    "ComplianceStatusType",
    "ComplianceUploadTypeType",
    "ConnectionStatusType",
    "DescribeActivationsFilterKeysType",
    "DescribeActivationsPaginatorName",
    "DescribeAssociationExecutionTargetsPaginatorName",
    "DescribeAssociationExecutionsPaginatorName",
    "DescribeAutomationExecutionsPaginatorName",
    "DescribeAutomationStepExecutionsPaginatorName",
    "DescribeAvailablePatchesPaginatorName",
    "DescribeEffectiveInstanceAssociationsPaginatorName",
    "DescribeEffectivePatchesForPatchBaselinePaginatorName",
    "DescribeInstanceAssociationsStatusPaginatorName",
    "DescribeInstanceInformationPaginatorName",
    "DescribeInstancePatchStatesForPatchGroupPaginatorName",
    "DescribeInstancePatchStatesPaginatorName",
    "DescribeInstancePatchesPaginatorName",
    "DescribeInventoryDeletionsPaginatorName",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName",
    "DescribeMaintenanceWindowExecutionTasksPaginatorName",
    "DescribeMaintenanceWindowExecutionsPaginatorName",
    "DescribeMaintenanceWindowSchedulePaginatorName",
    "DescribeMaintenanceWindowTargetsPaginatorName",
    "DescribeMaintenanceWindowTasksPaginatorName",
    "DescribeMaintenanceWindowsForTargetPaginatorName",
    "DescribeMaintenanceWindowsPaginatorName",
    "DescribeOpsItemsPaginatorName",
    "DescribeParametersPaginatorName",
    "DescribePatchBaselinesPaginatorName",
    "DescribePatchGroupsPaginatorName",
    "DescribePatchPropertiesPaginatorName",
    "DescribeSessionsPaginatorName",
    "DocumentFilterKeyType",
    "DocumentFormatType",
    "DocumentHashTypeType",
    "DocumentMetadataEnumType",
    "DocumentParameterTypeType",
    "DocumentPermissionTypeType",
    "DocumentReviewActionType",
    "DocumentReviewCommentTypeType",
    "DocumentStatusType",
    "DocumentTypeType",
    "ExecutionModeType",
    "FaultType",
    "GetInventoryPaginatorName",
    "GetInventorySchemaPaginatorName",
    "GetOpsSummaryPaginatorName",
    "GetParameterHistoryPaginatorName",
    "GetParametersByPathPaginatorName",
    "InstanceInformationFilterKeyType",
    "InstancePatchStateOperatorTypeType",
    "InventoryAttributeDataTypeType",
    "InventoryDeletionStatusType",
    "InventoryQueryOperatorTypeType",
    "InventorySchemaDeleteOptionType",
    "LastResourceDataSyncStatusType",
    "ListAssociationVersionsPaginatorName",
    "ListAssociationsPaginatorName",
    "ListCommandInvocationsPaginatorName",
    "ListCommandsPaginatorName",
    "ListComplianceItemsPaginatorName",
    "ListComplianceSummariesPaginatorName",
    "ListDocumentVersionsPaginatorName",
    "ListDocumentsPaginatorName",
    "ListOpsItemEventsPaginatorName",
    "ListOpsItemRelatedItemsPaginatorName",
    "ListOpsMetadataPaginatorName",
    "ListResourceComplianceSummariesPaginatorName",
    "ListResourceDataSyncPaginatorName",
    "MaintenanceWindowExecutionStatusType",
    "MaintenanceWindowResourceTypeType",
    "MaintenanceWindowTaskTypeType",
    "NotificationEventType",
    "NotificationTypeType",
    "OperatingSystemType",
    "OpsFilterOperatorTypeType",
    "OpsItemDataTypeType",
    "OpsItemEventFilterKeyType",
    "OpsItemEventFilterOperatorType",
    "OpsItemFilterKeyType",
    "OpsItemFilterOperatorType",
    "OpsItemRelatedItemsFilterKeyType",
    "OpsItemRelatedItemsFilterOperatorType",
    "OpsItemStatusType",
    "ParameterTierType",
    "ParameterTypeType",
    "ParametersFilterKeyType",
    "PatchActionType",
    "PatchComplianceDataStateType",
    "PatchComplianceLevelType",
    "PatchDeploymentStatusType",
    "PatchFilterKeyType",
    "PatchOperationTypeType",
    "PatchPropertyType",
    "PatchSetType",
    "PingStatusType",
    "PlatformTypeType",
    "RebootOptionType",
    "ResourceDataSyncS3FormatType",
    "ResourceTypeForTaggingType",
    "ResourceTypeType",
    "ReviewStatusType",
    "SessionFilterKeyType",
    "SessionStateType",
    "SessionStatusType",
    "SignalTypeType",
    "StepExecutionFilterKeyType",
    "StopTypeType",
)

AssociationComplianceSeverityType = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM", "UNSPECIFIED"]
AssociationExecutionFilterKeyType = Literal["CreatedTime", "ExecutionId", "Status"]
AssociationExecutionTargetsFilterKeyType = Literal["ResourceId", "ResourceType", "Status"]
AssociationFilterKeyType = Literal[
    "AssociationId",
    "AssociationName",
    "AssociationStatusName",
    "InstanceId",
    "LastExecutedAfter",
    "LastExecutedBefore",
    "Name",
    "ResourceGroupName",
]
AssociationFilterOperatorTypeType = Literal["EQUAL", "GREATER_THAN", "LESS_THAN"]
AssociationStatusNameType = Literal["Failed", "Pending", "Success"]
AssociationSyncComplianceType = Literal["AUTO", "MANUAL"]
AttachmentHashTypeType = Literal["Sha256"]
AttachmentsSourceKeyType = Literal["AttachmentReference", "S3FileUrl", "SourceUrl"]
AutomationExecutionFilterKeyType = Literal[
    "AutomationSubtype",
    "AutomationType",
    "CurrentAction",
    "DocumentNamePrefix",
    "ExecutionId",
    "ExecutionStatus",
    "OpsItemId",
    "ParentExecutionId",
    "StartTimeAfter",
    "StartTimeBefore",
    "TagKey",
    "TargetResourceGroup",
]
AutomationExecutionStatusType = Literal[
    "Approved",
    "Cancelled",
    "Cancelling",
    "ChangeCalendarOverrideApproved",
    "ChangeCalendarOverrideRejected",
    "CompletedWithFailure",
    "CompletedWithSuccess",
    "Failed",
    "InProgress",
    "Pending",
    "PendingApproval",
    "PendingChangeCalendarOverride",
    "Rejected",
    "RunbookInProgress",
    "Scheduled",
    "Success",
    "TimedOut",
    "Waiting",
]
AutomationSubtypeType = Literal["ChangeRequest"]
AutomationTypeType = Literal["CrossAccount", "Local"]
CalendarStateType = Literal["CLOSED", "OPEN"]
CommandExecutedWaiterName = Literal["command_executed"]
CommandFilterKeyType = Literal[
    "DocumentName", "ExecutionStage", "InvokedAfter", "InvokedBefore", "Status"
]
CommandInvocationStatusType = Literal[
    "Cancelled", "Cancelling", "Delayed", "Failed", "InProgress", "Pending", "Success", "TimedOut"
]
CommandPluginStatusType = Literal[
    "Cancelled", "Failed", "InProgress", "Pending", "Success", "TimedOut"
]
CommandStatusType = Literal[
    "Cancelled", "Cancelling", "Failed", "InProgress", "Pending", "Success", "TimedOut"
]
ComplianceQueryOperatorTypeType = Literal[
    "BEGIN_WITH", "EQUAL", "GREATER_THAN", "LESS_THAN", "NOT_EQUAL"
]
ComplianceSeverityType = Literal[
    "CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"
]
ComplianceStatusType = Literal["COMPLIANT", "NON_COMPLIANT"]
ComplianceUploadTypeType = Literal["COMPLETE", "PARTIAL"]
ConnectionStatusType = Literal["Connected", "NotConnected"]
DescribeActivationsFilterKeysType = Literal["ActivationIds", "DefaultInstanceName", "IamRole"]
DescribeActivationsPaginatorName = Literal["describe_activations"]
DescribeAssociationExecutionTargetsPaginatorName = Literal["describe_association_execution_targets"]
DescribeAssociationExecutionsPaginatorName = Literal["describe_association_executions"]
DescribeAutomationExecutionsPaginatorName = Literal["describe_automation_executions"]
DescribeAutomationStepExecutionsPaginatorName = Literal["describe_automation_step_executions"]
DescribeAvailablePatchesPaginatorName = Literal["describe_available_patches"]
DescribeEffectiveInstanceAssociationsPaginatorName = Literal[
    "describe_effective_instance_associations"
]
DescribeEffectivePatchesForPatchBaselinePaginatorName = Literal[
    "describe_effective_patches_for_patch_baseline"
]
DescribeInstanceAssociationsStatusPaginatorName = Literal["describe_instance_associations_status"]
DescribeInstanceInformationPaginatorName = Literal["describe_instance_information"]
DescribeInstancePatchStatesForPatchGroupPaginatorName = Literal[
    "describe_instance_patch_states_for_patch_group"
]
DescribeInstancePatchStatesPaginatorName = Literal["describe_instance_patch_states"]
DescribeInstancePatchesPaginatorName = Literal["describe_instance_patches"]
DescribeInventoryDeletionsPaginatorName = Literal["describe_inventory_deletions"]
DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName = Literal[
    "describe_maintenance_window_execution_task_invocations"
]
DescribeMaintenanceWindowExecutionTasksPaginatorName = Literal[
    "describe_maintenance_window_execution_tasks"
]
DescribeMaintenanceWindowExecutionsPaginatorName = Literal["describe_maintenance_window_executions"]
DescribeMaintenanceWindowSchedulePaginatorName = Literal["describe_maintenance_window_schedule"]
DescribeMaintenanceWindowTargetsPaginatorName = Literal["describe_maintenance_window_targets"]
DescribeMaintenanceWindowTasksPaginatorName = Literal["describe_maintenance_window_tasks"]
DescribeMaintenanceWindowsForTargetPaginatorName = Literal[
    "describe_maintenance_windows_for_target"
]
DescribeMaintenanceWindowsPaginatorName = Literal["describe_maintenance_windows"]
DescribeOpsItemsPaginatorName = Literal["describe_ops_items"]
DescribeParametersPaginatorName = Literal["describe_parameters"]
DescribePatchBaselinesPaginatorName = Literal["describe_patch_baselines"]
DescribePatchGroupsPaginatorName = Literal["describe_patch_groups"]
DescribePatchPropertiesPaginatorName = Literal["describe_patch_properties"]
DescribeSessionsPaginatorName = Literal["describe_sessions"]
DocumentFilterKeyType = Literal["DocumentType", "Name", "Owner", "PlatformTypes"]
DocumentFormatType = Literal["JSON", "TEXT", "YAML"]
DocumentHashTypeType = Literal["Sha1", "Sha256"]
DocumentMetadataEnumType = Literal["DocumentReviews"]
DocumentParameterTypeType = Literal["String", "StringList"]
DocumentPermissionTypeType = Literal["Share"]
DocumentReviewActionType = Literal["Approve", "Reject", "SendForReview", "UpdateReview"]
DocumentReviewCommentTypeType = Literal["Comment"]
DocumentStatusType = Literal["Active", "Creating", "Deleting", "Failed", "Updating"]
DocumentTypeType = Literal[
    "ApplicationConfiguration",
    "ApplicationConfigurationSchema",
    "Automation",
    "Automation.ChangeTemplate",
    "ChangeCalendar",
    "Command",
    "DeploymentStrategy",
    "Package",
    "Policy",
    "ProblemAnalysis",
    "ProblemAnalysisTemplate",
    "Session",
]
ExecutionModeType = Literal["Auto", "Interactive"]
FaultType = Literal["Client", "Server", "Unknown"]
GetInventoryPaginatorName = Literal["get_inventory"]
GetInventorySchemaPaginatorName = Literal["get_inventory_schema"]
GetOpsSummaryPaginatorName = Literal["get_ops_summary"]
GetParameterHistoryPaginatorName = Literal["get_parameter_history"]
GetParametersByPathPaginatorName = Literal["get_parameters_by_path"]
InstanceInformationFilterKeyType = Literal[
    "ActivationIds",
    "AgentVersion",
    "AssociationStatus",
    "IamRole",
    "InstanceIds",
    "PingStatus",
    "PlatformTypes",
    "ResourceType",
]
InstancePatchStateOperatorTypeType = Literal["Equal", "GreaterThan", "LessThan", "NotEqual"]
InventoryAttributeDataTypeType = Literal["number", "string"]
InventoryDeletionStatusType = Literal["Complete", "InProgress"]
InventoryQueryOperatorTypeType = Literal[
    "BeginWith", "Equal", "Exists", "GreaterThan", "LessThan", "NotEqual"
]
InventorySchemaDeleteOptionType = Literal["DeleteSchema", "DisableSchema"]
LastResourceDataSyncStatusType = Literal["Failed", "InProgress", "Successful"]
ListAssociationVersionsPaginatorName = Literal["list_association_versions"]
ListAssociationsPaginatorName = Literal["list_associations"]
ListCommandInvocationsPaginatorName = Literal["list_command_invocations"]
ListCommandsPaginatorName = Literal["list_commands"]
ListComplianceItemsPaginatorName = Literal["list_compliance_items"]
ListComplianceSummariesPaginatorName = Literal["list_compliance_summaries"]
ListDocumentVersionsPaginatorName = Literal["list_document_versions"]
ListDocumentsPaginatorName = Literal["list_documents"]
ListOpsItemEventsPaginatorName = Literal["list_ops_item_events"]
ListOpsItemRelatedItemsPaginatorName = Literal["list_ops_item_related_items"]
ListOpsMetadataPaginatorName = Literal["list_ops_metadata"]
ListResourceComplianceSummariesPaginatorName = Literal["list_resource_compliance_summaries"]
ListResourceDataSyncPaginatorName = Literal["list_resource_data_sync"]
MaintenanceWindowExecutionStatusType = Literal[
    "CANCELLED",
    "CANCELLING",
    "FAILED",
    "IN_PROGRESS",
    "PENDING",
    "SKIPPED_OVERLAPPING",
    "SUCCESS",
    "TIMED_OUT",
]
MaintenanceWindowResourceTypeType = Literal["INSTANCE", "RESOURCE_GROUP"]
MaintenanceWindowTaskTypeType = Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"]
NotificationEventType = Literal["All", "Cancelled", "Failed", "InProgress", "Success", "TimedOut"]
NotificationTypeType = Literal["Command", "Invocation"]
OperatingSystemType = Literal[
    "AMAZON_LINUX",
    "AMAZON_LINUX_2",
    "CENTOS",
    "DEBIAN",
    "MACOS",
    "ORACLE_LINUX",
    "REDHAT_ENTERPRISE_LINUX",
    "SUSE",
    "UBUNTU",
    "WINDOWS",
]
OpsFilterOperatorTypeType = Literal[
    "BeginWith", "Equal", "Exists", "GreaterThan", "LessThan", "NotEqual"
]
OpsItemDataTypeType = Literal["SearchableString", "String"]
OpsItemEventFilterKeyType = Literal["OpsItemId"]
OpsItemEventFilterOperatorType = Literal["Equal"]
OpsItemFilterKeyType = Literal[
    "ActualEndTime",
    "ActualStartTime",
    "AutomationId",
    "Category",
    "ChangeRequestByApproverArn",
    "ChangeRequestByApproverName",
    "ChangeRequestByRequesterArn",
    "ChangeRequestByRequesterName",
    "ChangeRequestByTargetsResourceGroup",
    "ChangeRequestByTemplate",
    "CreatedBy",
    "CreatedTime",
    "InsightByType",
    "LastModifiedTime",
    "OperationalData",
    "OperationalDataKey",
    "OperationalDataValue",
    "OpsItemId",
    "OpsItemType",
    "PlannedEndTime",
    "PlannedStartTime",
    "Priority",
    "ResourceId",
    "Severity",
    "Source",
    "Status",
    "Title",
]
OpsItemFilterOperatorType = Literal["Contains", "Equal", "GreaterThan", "LessThan"]
OpsItemRelatedItemsFilterKeyType = Literal["AssociationId", "ResourceType", "ResourceUri"]
OpsItemRelatedItemsFilterOperatorType = Literal["Equal"]
OpsItemStatusType = Literal[
    "Approved",
    "Cancelled",
    "Cancelling",
    "ChangeCalendarOverrideApproved",
    "ChangeCalendarOverrideRejected",
    "Closed",
    "CompletedWithFailure",
    "CompletedWithSuccess",
    "Failed",
    "InProgress",
    "Open",
    "Pending",
    "PendingApproval",
    "PendingChangeCalendarOverride",
    "Rejected",
    "Resolved",
    "RunbookInProgress",
    "Scheduled",
    "TimedOut",
]
ParameterTierType = Literal["Advanced", "Intelligent-Tiering", "Standard"]
ParameterTypeType = Literal["SecureString", "String", "StringList"]
ParametersFilterKeyType = Literal["KeyId", "Name", "Type"]
PatchActionType = Literal["ALLOW_AS_DEPENDENCY", "BLOCK"]
PatchComplianceDataStateType = Literal[
    "FAILED",
    "INSTALLED",
    "INSTALLED_OTHER",
    "INSTALLED_PENDING_REBOOT",
    "INSTALLED_REJECTED",
    "MISSING",
    "NOT_APPLICABLE",
]
PatchComplianceLevelType = Literal[
    "CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"
]
PatchDeploymentStatusType = Literal[
    "APPROVED", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED", "PENDING_APPROVAL"
]
PatchFilterKeyType = Literal[
    "ADVISORY_ID",
    "ARCH",
    "BUGZILLA_ID",
    "CLASSIFICATION",
    "CVE_ID",
    "EPOCH",
    "MSRC_SEVERITY",
    "NAME",
    "PATCH_ID",
    "PATCH_SET",
    "PRIORITY",
    "PRODUCT",
    "PRODUCT_FAMILY",
    "RELEASE",
    "REPOSITORY",
    "SECTION",
    "SECURITY",
    "SEVERITY",
    "VERSION",
]
PatchOperationTypeType = Literal["Install", "Scan"]
PatchPropertyType = Literal[
    "CLASSIFICATION", "MSRC_SEVERITY", "PRIORITY", "PRODUCT", "PRODUCT_FAMILY", "SEVERITY"
]
PatchSetType = Literal["APPLICATION", "OS"]
PingStatusType = Literal["ConnectionLost", "Inactive", "Online"]
PlatformTypeType = Literal["Linux", "Windows"]
RebootOptionType = Literal["NoReboot", "RebootIfNeeded"]
ResourceDataSyncS3FormatType = Literal["JsonSerDe"]
ResourceTypeForTaggingType = Literal[
    "Document",
    "MaintenanceWindow",
    "ManagedInstance",
    "OpsItem",
    "OpsMetadata",
    "Parameter",
    "PatchBaseline",
]
ResourceTypeType = Literal["Document", "EC2Instance", "ManagedInstance"]
ReviewStatusType = Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"]
SessionFilterKeyType = Literal[
    "InvokedAfter", "InvokedBefore", "Owner", "SessionId", "Status", "Target"
]
SessionStateType = Literal["Active", "History"]
SessionStatusType = Literal[
    "Connected", "Connecting", "Disconnected", "Failed", "Terminated", "Terminating"
]
SignalTypeType = Literal["Approve", "Reject", "Resume", "StartStep", "StopStep"]
StepExecutionFilterKeyType = Literal[
    "Action",
    "StartTimeAfter",
    "StartTimeBefore",
    "StepExecutionId",
    "StepExecutionStatus",
    "StepName",
]
StopTypeType = Literal["Cancel", "Complete"]
