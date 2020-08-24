"""
Main interface for ssm service type definitions.

Usage::

    ```python
    from mypy_boto3_ssm.type_defs import AccountSharingInfoTypeDef

    data: AccountSharingInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountSharingInfoTypeDef",
    "ActivationTypeDef",
    "AssociationDescriptionTypeDef",
    "AssociationExecutionTargetTypeDef",
    "AssociationExecutionTypeDef",
    "AssociationOverviewTypeDef",
    "AssociationStatusTypeDef",
    "AssociationTypeDef",
    "AssociationVersionInfoTypeDef",
    "AttachmentContentTypeDef",
    "AttachmentInformationTypeDef",
    "AutomationExecutionMetadataTypeDef",
    "AutomationExecutionTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CommandInvocationTypeDef",
    "CommandPluginTypeDef",
    "CommandTypeDef",
    "ComplianceExecutionSummaryTypeDef",
    "ComplianceItemTypeDef",
    "ComplianceSummaryItemTypeDef",
    "CompliantSummaryTypeDef",
    "CreateAssociationBatchRequestEntryTypeDef",
    "DocumentDefaultVersionDescriptionTypeDef",
    "DocumentDescriptionTypeDef",
    "DocumentIdentifierTypeDef",
    "DocumentParameterTypeDef",
    "DocumentRequiresTypeDef",
    "DocumentVersionInfoTypeDef",
    "EffectivePatchTypeDef",
    "FailedCreateAssociationTypeDef",
    "FailureDetailsTypeDef",
    "InstanceAggregatedAssociationOverviewTypeDef",
    "InstanceAssociationOutputLocationTypeDef",
    "InstanceAssociationOutputUrlTypeDef",
    "InstanceAssociationStatusInfoTypeDef",
    "InstanceAssociationTypeDef",
    "InstanceInformationTypeDef",
    "InstancePatchStateTypeDef",
    "InventoryDeletionStatusItemTypeDef",
    "InventoryDeletionSummaryItemTypeDef",
    "InventoryDeletionSummaryTypeDef",
    "InventoryFilterTypeDef",
    "InventoryGroupTypeDef",
    "InventoryItemAttributeTypeDef",
    "InventoryItemSchemaTypeDef",
    "InventoryResultEntityTypeDef",
    "InventoryResultItemTypeDef",
    "LoggingInfoTypeDef",
    "MaintenanceWindowAutomationParametersTypeDef",
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    "MaintenanceWindowExecutionTypeDef",
    "MaintenanceWindowIdentityForTargetTypeDef",
    "MaintenanceWindowIdentityTypeDef",
    "MaintenanceWindowLambdaParametersTypeDef",
    "MaintenanceWindowRunCommandParametersTypeDef",
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    "MaintenanceWindowTargetTypeDef",
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    "MaintenanceWindowTaskTypeDef",
    "NonCompliantSummaryTypeDef",
    "NotificationConfigTypeDef",
    "OpsEntityItemTypeDef",
    "OpsEntityTypeDef",
    "OpsFilterTypeDef",
    "OpsItemDataValueTypeDef",
    "OpsItemNotificationTypeDef",
    "OpsItemSummaryTypeDef",
    "OpsItemTypeDef",
    "OutputSourceTypeDef",
    "ParameterHistoryTypeDef",
    "ParameterInlinePolicyTypeDef",
    "ParameterMetadataTypeDef",
    "ParameterTypeDef",
    "PatchBaselineIdentityTypeDef",
    "PatchComplianceDataTypeDef",
    "PatchFilterGroupTypeDef",
    "PatchFilterTypeDef",
    "PatchGroupPatchBaselineMappingTypeDef",
    "PatchRuleGroupTypeDef",
    "PatchRuleTypeDef",
    "PatchSourceTypeDef",
    "PatchStatusTypeDef",
    "PatchTypeDef",
    "ProgressCountersTypeDef",
    "RelatedOpsItemTypeDef",
    "ResolvedTargetsTypeDef",
    "ResourceComplianceSummaryItemTypeDef",
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    "ResourceDataSyncDestinationDataSharingTypeDef",
    "ResourceDataSyncItemTypeDef",
    "ResourceDataSyncOrganizationalUnitTypeDef",
    "ResourceDataSyncS3DestinationTypeDef",
    "ResourceDataSyncSourceWithStateTypeDef",
    "S3OutputLocationTypeDef",
    "S3OutputUrlTypeDef",
    "ScheduledWindowExecutionTypeDef",
    "ServiceSettingTypeDef",
    "SessionManagerOutputUrlTypeDef",
    "SessionTypeDef",
    "SeveritySummaryTypeDef",
    "StepExecutionTypeDef",
    "TagTypeDef",
    "TargetLocationTypeDef",
    "TargetTypeDef",
    "AssociationExecutionFilterTypeDef",
    "AssociationExecutionTargetsFilterTypeDef",
    "AssociationFilterTypeDef",
    "AttachmentsSourceTypeDef",
    "AutomationExecutionFilterTypeDef",
    "CancelMaintenanceWindowExecutionResultTypeDef",
    "CommandFilterTypeDef",
    "ComplianceItemEntryTypeDef",
    "ComplianceStringFilterTypeDef",
    "CreateActivationResultTypeDef",
    "CreateAssociationBatchResultTypeDef",
    "CreateAssociationResultTypeDef",
    "CreateDocumentResultTypeDef",
    "CreateMaintenanceWindowResultTypeDef",
    "CreateOpsItemResponseTypeDef",
    "CreatePatchBaselineResultTypeDef",
    "DeleteInventoryResultTypeDef",
    "DeleteMaintenanceWindowResultTypeDef",
    "DeleteParametersResultTypeDef",
    "DeletePatchBaselineResultTypeDef",
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    "DescribeActivationsFilterTypeDef",
    "DescribeActivationsResultTypeDef",
    "DescribeAssociationExecutionTargetsResultTypeDef",
    "DescribeAssociationExecutionsResultTypeDef",
    "DescribeAssociationResultTypeDef",
    "DescribeAutomationExecutionsResultTypeDef",
    "DescribeAutomationStepExecutionsResultTypeDef",
    "DescribeAvailablePatchesResultTypeDef",
    "DescribeDocumentPermissionResponseTypeDef",
    "DescribeDocumentResultTypeDef",
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    "DescribeInstanceAssociationsStatusResultTypeDef",
    "DescribeInstanceInformationResultTypeDef",
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    "DescribeInstancePatchStatesResultTypeDef",
    "DescribeInstancePatchesResultTypeDef",
    "DescribeInventoryDeletionsResultTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    "DescribeMaintenanceWindowTasksResultTypeDef",
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    "DescribeMaintenanceWindowsResultTypeDef",
    "DescribeOpsItemsResponseTypeDef",
    "DescribeParametersResultTypeDef",
    "DescribePatchBaselinesResultTypeDef",
    "DescribePatchGroupStateResultTypeDef",
    "DescribePatchGroupsResultTypeDef",
    "DescribePatchPropertiesResultTypeDef",
    "DescribeSessionsResponseTypeDef",
    "InventoryAggregatorTypeDef",
    "OpsAggregatorTypeDef",
    "DocumentFilterTypeDef",
    "DocumentKeyValuesFilterTypeDef",
    "GetAutomationExecutionResultTypeDef",
    "GetCalendarStateResponseTypeDef",
    "GetCommandInvocationResultTypeDef",
    "GetConnectionStatusResponseTypeDef",
    "GetDefaultPatchBaselineResultTypeDef",
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    "GetDocumentResultTypeDef",
    "GetInventoryResultTypeDef",
    "GetInventorySchemaResultTypeDef",
    "GetMaintenanceWindowExecutionResultTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    "GetMaintenanceWindowResultTypeDef",
    "GetMaintenanceWindowTaskResultTypeDef",
    "GetOpsItemResponseTypeDef",
    "GetOpsSummaryResultTypeDef",
    "GetParameterHistoryResultTypeDef",
    "GetParameterResultTypeDef",
    "GetParametersByPathResultTypeDef",
    "GetParametersResultTypeDef",
    "GetPatchBaselineForPatchGroupResultTypeDef",
    "GetPatchBaselineResultTypeDef",
    "GetServiceSettingResultTypeDef",
    "InstanceInformationFilterTypeDef",
    "InstanceInformationStringFilterTypeDef",
    "InstancePatchStateFilterTypeDef",
    "InventoryItemTypeDef",
    "LabelParameterVersionResultTypeDef",
    "ListAssociationVersionsResultTypeDef",
    "ListAssociationsResultTypeDef",
    "ListCommandInvocationsResultTypeDef",
    "ListCommandsResultTypeDef",
    "ListComplianceItemsResultTypeDef",
    "ListComplianceSummariesResultTypeDef",
    "ListDocumentVersionsResultTypeDef",
    "ListDocumentsResultTypeDef",
    "ListInventoryEntriesResultTypeDef",
    "ListResourceComplianceSummariesResultTypeDef",
    "ListResourceDataSyncResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "MaintenanceWindowFilterTypeDef",
    "OpsItemFilterTypeDef",
    "OpsResultAttributeTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterStringFilterTypeDef",
    "ParametersFilterTypeDef",
    "PatchOrchestratorFilterTypeDef",
    "PutInventoryResultTypeDef",
    "PutParameterResultTypeDef",
    "RegisterDefaultPatchBaselineResultTypeDef",
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    "ResetServiceSettingResultTypeDef",
    "ResourceDataSyncSourceTypeDef",
    "ResultAttributeTypeDef",
    "ResumeSessionResponseTypeDef",
    "SendCommandResultTypeDef",
    "SessionFilterTypeDef",
    "StartAutomationExecutionResultTypeDef",
    "StartSessionResponseTypeDef",
    "StepExecutionFilterTypeDef",
    "TerminateSessionResponseTypeDef",
    "UpdateAssociationResultTypeDef",
    "UpdateAssociationStatusResultTypeDef",
    "UpdateDocumentDefaultVersionResultTypeDef",
    "UpdateDocumentResultTypeDef",
    "UpdateMaintenanceWindowResultTypeDef",
    "UpdateMaintenanceWindowTargetResultTypeDef",
    "UpdateMaintenanceWindowTaskResultTypeDef",
    "UpdatePatchBaselineResultTypeDef",
    "WaiterConfigTypeDef",
)

AccountSharingInfoTypeDef = TypedDict(
    "AccountSharingInfoTypeDef", {"AccountId": str, "SharedDocumentVersion": str}, total=False
)

ActivationTypeDef = TypedDict(
    "ActivationTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

AssociationDescriptionTypeDef = TypedDict(
    "AssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": "AssociationStatusTypeDef",
        "Overview": "AssociationOverviewTypeDef",
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
        "SyncCompliance": Literal["AUTO", "MANUAL"],
        "ApplyOnlyAtCronInterval": bool,
    },
    total=False,
)

AssociationExecutionTargetTypeDef = TypedDict(
    "AssociationExecutionTargetTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": "OutputSourceTypeDef",
    },
    total=False,
)

AssociationExecutionTypeDef = TypedDict(
    "AssociationExecutionTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)

AssociationOverviewTypeDef = TypedDict(
    "AssociationOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

_RequiredAssociationStatusTypeDef = TypedDict(
    "_RequiredAssociationStatusTypeDef",
    {"Date": datetime, "Name": Literal["Pending", "Success", "Failed"], "Message": str},
)
_OptionalAssociationStatusTypeDef = TypedDict(
    "_OptionalAssociationStatusTypeDef", {"AdditionalInfo": str}, total=False
)


class AssociationStatusTypeDef(
    _RequiredAssociationStatusTypeDef, _OptionalAssociationStatusTypeDef
):
    pass


AssociationTypeDef = TypedDict(
    "AssociationTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List["TargetTypeDef"],
        "LastExecutionDate": datetime,
        "Overview": "AssociationOverviewTypeDef",
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)

AssociationVersionInfoTypeDef = TypedDict(
    "AssociationVersionInfoTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
        "SyncCompliance": Literal["AUTO", "MANUAL"],
        "ApplyOnlyAtCronInterval": bool,
    },
    total=False,
)

AttachmentContentTypeDef = TypedDict(
    "AttachmentContentTypeDef",
    {"Name": str, "Size": int, "Hash": str, "HashType": Literal["Sha256"], "Url": str},
    total=False,
)

AttachmentInformationTypeDef = TypedDict("AttachmentInformationTypeDef", {"Name": str}, total=False)

AutomationExecutionMetadataTypeDef = TypedDict(
    "AutomationExecutionMetadataTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": "ResolvedTargetsTypeDef",
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": Literal["CrossAccount", "Local"],
    },
    total=False,
)

AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "AutomationExecutionStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "StepExecutions": List["StepExecutionTypeDef"],
        "StepExecutionsTruncated": bool,
        "Parameters": Dict[str, List[str]],
        "Outputs": Dict[str, List[str]],
        "FailureMessage": str,
        "Mode": Literal["Auto", "Interactive"],
        "ParentAutomationExecutionId": str,
        "ExecutedBy": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": "ResolvedTargetsTypeDef",
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "TargetLocations": List["TargetLocationTypeDef"],
        "ProgressCounters": "ProgressCountersTypeDef",
    },
    total=False,
)

CloudWatchOutputConfigTypeDef = TypedDict(
    "CloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

CommandInvocationTypeDef = TypedDict(
    "CommandInvocationTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List["CommandPluginTypeDef"],
        "ServiceRole": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
    },
    total=False,
)

CommandPluginTypeDef = TypedDict(
    "CommandPluginTypeDef",
    {
        "Name": str,
        "Status": Literal["Pending", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"],
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List["TargetTypeDef"],
        "RequestedDateTime": datetime,
        "Status": Literal[
            "Pending", "InProgress", "Success", "Cancelled", "Failed", "TimedOut", "Cancelling"
        ],
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "TimeoutSeconds": int,
    },
    total=False,
)

_RequiredComplianceExecutionSummaryTypeDef = TypedDict(
    "_RequiredComplianceExecutionSummaryTypeDef", {"ExecutionTime": datetime}
)
_OptionalComplianceExecutionSummaryTypeDef = TypedDict(
    "_OptionalComplianceExecutionSummaryTypeDef",
    {"ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ComplianceExecutionSummaryTypeDef(
    _RequiredComplianceExecutionSummaryTypeDef, _OptionalComplianceExecutionSummaryTypeDef
):
    pass


ComplianceItemTypeDef = TypedDict(
    "ComplianceItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "Details": Dict[str, str],
    },
    total=False,
)

ComplianceSummaryItemTypeDef = TypedDict(
    "ComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": "CompliantSummaryTypeDef",
        "NonCompliantSummary": "NonCompliantSummaryTypeDef",
    },
    total=False,
)

CompliantSummaryTypeDef = TypedDict(
    "CompliantSummaryTypeDef",
    {"CompliantCount": int, "SeveritySummary": "SeveritySummaryTypeDef"},
    total=False,
)

_RequiredCreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "_RequiredCreateAssociationBatchRequestEntryTypeDef", {"Name": str}
)
_OptionalCreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "_OptionalCreateAssociationBatchRequestEntryTypeDef",
    {
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"],
        "SyncCompliance": Literal["AUTO", "MANUAL"],
        "ApplyOnlyAtCronInterval": bool,
    },
    total=False,
)


class CreateAssociationBatchRequestEntryTypeDef(
    _RequiredCreateAssociationBatchRequestEntryTypeDef,
    _OptionalCreateAssociationBatchRequestEntryTypeDef,
):
    pass


DocumentDefaultVersionDescriptionTypeDef = TypedDict(
    "DocumentDefaultVersionDescriptionTypeDef",
    {"Name": str, "DefaultVersion": str, "DefaultVersionName": str},
    total=False,
)

DocumentDescriptionTypeDef = TypedDict(
    "DocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": Literal["Sha256", "Sha1"],
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List["DocumentParameterTypeDef"],
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "TargetType": str,
        "Tags": List["TagTypeDef"],
        "AttachmentsInformation": List["AttachmentInformationTypeDef"],
        "Requires": List["DocumentRequiresTypeDef"],
    },
    total=False,
)

DocumentIdentifierTypeDef = TypedDict(
    "DocumentIdentifierTypeDef",
    {
        "Name": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[Literal["Windows", "Linux"]],
        "DocumentVersion": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "SchemaVersion": str,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "TargetType": str,
        "Tags": List["TagTypeDef"],
        "Requires": List["DocumentRequiresTypeDef"],
    },
    total=False,
)

DocumentParameterTypeDef = TypedDict(
    "DocumentParameterTypeDef",
    {"Name": str, "Type": Literal["String", "StringList"], "Description": str, "DefaultValue": str},
    total=False,
)

_RequiredDocumentRequiresTypeDef = TypedDict("_RequiredDocumentRequiresTypeDef", {"Name": str})
_OptionalDocumentRequiresTypeDef = TypedDict(
    "_OptionalDocumentRequiresTypeDef", {"Version": str}, total=False
)


class DocumentRequiresTypeDef(_RequiredDocumentRequiresTypeDef, _OptionalDocumentRequiresTypeDef):
    pass


DocumentVersionInfoTypeDef = TypedDict(
    "DocumentVersionInfoTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
    },
    total=False,
)

EffectivePatchTypeDef = TypedDict(
    "EffectivePatchTypeDef",
    {"Patch": "PatchTypeDef", "PatchStatus": "PatchStatusTypeDef"},
    total=False,
)

FailedCreateAssociationTypeDef = TypedDict(
    "FailedCreateAssociationTypeDef",
    {
        "Entry": "CreateAssociationBatchRequestEntryTypeDef",
        "Message": str,
        "Fault": Literal["Client", "Server", "Unknown"],
    },
    total=False,
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)

InstanceAggregatedAssociationOverviewTypeDef = TypedDict(
    "InstanceAggregatedAssociationOverviewTypeDef",
    {"DetailedStatus": str, "InstanceAssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

InstanceAssociationOutputLocationTypeDef = TypedDict(
    "InstanceAssociationOutputLocationTypeDef",
    {"S3Location": "S3OutputLocationTypeDef"},
    total=False,
)

InstanceAssociationOutputUrlTypeDef = TypedDict(
    "InstanceAssociationOutputUrlTypeDef", {"S3OutputUrl": "S3OutputUrlTypeDef"}, total=False
)

InstanceAssociationStatusInfoTypeDef = TypedDict(
    "InstanceAssociationStatusInfoTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": "InstanceAssociationOutputUrlTypeDef",
        "AssociationName": str,
    },
    total=False,
)

InstanceAssociationTypeDef = TypedDict(
    "InstanceAssociationTypeDef",
    {"AssociationId": str, "InstanceId": str, "Content": str, "AssociationVersion": str},
    total=False,
)

InstanceInformationTypeDef = TypedDict(
    "InstanceInformationTypeDef",
    {
        "InstanceId": str,
        "PingStatus": Literal["Online", "ConnectionLost", "Inactive"],
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": Literal["Windows", "Linux"],
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": Literal["ManagedInstance", "Document", "EC2Instance"],
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": "InstanceAggregatedAssociationOverviewTypeDef",
    },
    total=False,
)

_RequiredInstancePatchStateTypeDef = TypedDict(
    "_RequiredInstancePatchStateTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": Literal["Scan", "Install"],
    },
)
_OptionalInstancePatchStateTypeDef = TypedDict(
    "_OptionalInstancePatchStateTypeDef",
    {
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": Literal["RebootIfNeeded", "NoReboot"],
    },
    total=False,
)


class InstancePatchStateTypeDef(
    _RequiredInstancePatchStateTypeDef, _OptionalInstancePatchStateTypeDef
):
    pass


InventoryDeletionStatusItemTypeDef = TypedDict(
    "InventoryDeletionStatusItemTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": Literal["InProgress", "Complete"],
        "LastStatusMessage": str,
        "DeletionSummary": "InventoryDeletionSummaryTypeDef",
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)

InventoryDeletionSummaryItemTypeDef = TypedDict(
    "InventoryDeletionSummaryItemTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)

InventoryDeletionSummaryTypeDef = TypedDict(
    "InventoryDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List["InventoryDeletionSummaryItemTypeDef"],
    },
    total=False,
)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef", {"Key": str, "Values": List[str]}
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef",
    {"Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"]},
    total=False,
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


InventoryGroupTypeDef = TypedDict(
    "InventoryGroupTypeDef", {"Name": str, "Filters": List["InventoryFilterTypeDef"]}
)

InventoryItemAttributeTypeDef = TypedDict(
    "InventoryItemAttributeTypeDef", {"Name": str, "DataType": Literal["string", "number"]}
)

_RequiredInventoryItemSchemaTypeDef = TypedDict(
    "_RequiredInventoryItemSchemaTypeDef",
    {"TypeName": str, "Attributes": List["InventoryItemAttributeTypeDef"]},
)
_OptionalInventoryItemSchemaTypeDef = TypedDict(
    "_OptionalInventoryItemSchemaTypeDef", {"Version": str, "DisplayName": str}, total=False
)


class InventoryItemSchemaTypeDef(
    _RequiredInventoryItemSchemaTypeDef, _OptionalInventoryItemSchemaTypeDef
):
    pass


InventoryResultEntityTypeDef = TypedDict(
    "InventoryResultEntityTypeDef",
    {"Id": str, "Data": Dict[str, "InventoryResultItemTypeDef"]},
    total=False,
)

_RequiredInventoryResultItemTypeDef = TypedDict(
    "_RequiredInventoryResultItemTypeDef",
    {"TypeName": str, "SchemaVersion": str, "Content": List[Dict[str, str]]},
)
_OptionalInventoryResultItemTypeDef = TypedDict(
    "_OptionalInventoryResultItemTypeDef", {"CaptureTime": str, "ContentHash": str}, total=False
)


class InventoryResultItemTypeDef(
    _RequiredInventoryResultItemTypeDef, _OptionalInventoryResultItemTypeDef
):
    pass


_RequiredLoggingInfoTypeDef = TypedDict(
    "_RequiredLoggingInfoTypeDef", {"S3BucketName": str, "S3Region": str}
)
_OptionalLoggingInfoTypeDef = TypedDict(
    "_OptionalLoggingInfoTypeDef", {"S3KeyPrefix": str}, total=False
)


class LoggingInfoTypeDef(_RequiredLoggingInfoTypeDef, _OptionalLoggingInfoTypeDef):
    pass


MaintenanceWindowAutomationParametersTypeDef = TypedDict(
    "MaintenanceWindowAutomationParametersTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

MaintenanceWindowExecutionTaskIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
    },
    total=False,
)

MaintenanceWindowExecutionTaskInvocationIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

MaintenanceWindowExecutionTypeDef = TypedDict(
    "MaintenanceWindowExecutionTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

MaintenanceWindowIdentityForTargetTypeDef = TypedDict(
    "MaintenanceWindowIdentityForTargetTypeDef", {"WindowId": str, "Name": str}, total=False
)

MaintenanceWindowIdentityTypeDef = TypedDict(
    "MaintenanceWindowIdentityTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)

MaintenanceWindowLambdaParametersTypeDef = TypedDict(
    "MaintenanceWindowLambdaParametersTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": bytes},
    total=False,
)

MaintenanceWindowRunCommandParametersTypeDef = TypedDict(
    "MaintenanceWindowRunCommandParametersTypeDef",
    {
        "Comment": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "DocumentHash": str,
        "DocumentHashType": Literal["Sha256", "Sha1"],
        "DocumentVersion": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

MaintenanceWindowStepFunctionsParametersTypeDef = TypedDict(
    "MaintenanceWindowStepFunctionsParametersTypeDef", {"Input": str, "Name": str}, total=False
)

MaintenanceWindowTargetTypeDef = TypedDict(
    "MaintenanceWindowTargetTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": Literal["INSTANCE", "RESOURCE_GROUP"],
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

MaintenanceWindowTaskInvocationParametersTypeDef = TypedDict(
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    {
        "RunCommand": "MaintenanceWindowRunCommandParametersTypeDef",
        "Automation": "MaintenanceWindowAutomationParametersTypeDef",
        "StepFunctions": "MaintenanceWindowStepFunctionsParametersTypeDef",
        "Lambda": "MaintenanceWindowLambdaParametersTypeDef",
    },
    total=False,
)

MaintenanceWindowTaskParameterValueExpressionTypeDef = TypedDict(
    "MaintenanceWindowTaskParameterValueExpressionTypeDef", {"Values": List[str]}, total=False
)

MaintenanceWindowTaskTypeDef = TypedDict(
    "MaintenanceWindowTaskTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Targets": List["TargetTypeDef"],
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "Priority": int,
        "LoggingInfo": "LoggingInfoTypeDef",
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

NonCompliantSummaryTypeDef = TypedDict(
    "NonCompliantSummaryTypeDef",
    {"NonCompliantCount": int, "SeveritySummary": "SeveritySummaryTypeDef"},
    total=False,
)

NotificationConfigTypeDef = TypedDict(
    "NotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[
            Literal["All", "InProgress", "Success", "TimedOut", "Cancelled", "Failed"]
        ],
        "NotificationType": Literal["Command", "Invocation"],
    },
    total=False,
)

OpsEntityItemTypeDef = TypedDict(
    "OpsEntityItemTypeDef", {"CaptureTime": str, "Content": List[Dict[str, str]]}, total=False
)

OpsEntityTypeDef = TypedDict(
    "OpsEntityTypeDef", {"Id": str, "Data": Dict[str, "OpsEntityItemTypeDef"]}, total=False
)

_RequiredOpsFilterTypeDef = TypedDict(
    "_RequiredOpsFilterTypeDef", {"Key": str, "Values": List[str]}
)
_OptionalOpsFilterTypeDef = TypedDict(
    "_OptionalOpsFilterTypeDef",
    {"Type": Literal["Equal", "NotEqual", "BeginWith", "LessThan", "GreaterThan", "Exists"]},
    total=False,
)


class OpsFilterTypeDef(_RequiredOpsFilterTypeDef, _OptionalOpsFilterTypeDef):
    pass


OpsItemDataValueTypeDef = TypedDict(
    "OpsItemDataValueTypeDef",
    {"Value": str, "Type": Literal["SearchableString", "String"]},
    total=False,
)

OpsItemNotificationTypeDef = TypedDict("OpsItemNotificationTypeDef", {"Arn": str}, total=False)

OpsItemSummaryTypeDef = TypedDict(
    "OpsItemSummaryTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Priority": int,
        "Source": str,
        "Status": Literal["Open", "InProgress", "Resolved"],
        "OpsItemId": str,
        "Title": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Category": str,
        "Severity": str,
    },
    total=False,
)

OpsItemTypeDef = TypedDict(
    "OpsItemTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "Description": str,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Notifications": List["OpsItemNotificationTypeDef"],
        "Priority": int,
        "RelatedOpsItems": List["RelatedOpsItemTypeDef"],
        "Status": Literal["Open", "InProgress", "Resolved"],
        "OpsItemId": str,
        "Version": str,
        "Title": str,
        "Source": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Category": str,
        "Severity": str,
    },
    total=False,
)

OutputSourceTypeDef = TypedDict(
    "OutputSourceTypeDef", {"OutputSourceId": str, "OutputSourceType": str}, total=False
)

ParameterHistoryTypeDef = TypedDict(
    "ParameterHistoryTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List["ParameterInlinePolicyTypeDef"],
        "DataType": str,
    },
    total=False,
)

ParameterInlinePolicyTypeDef = TypedDict(
    "ParameterInlinePolicyTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

ParameterMetadataTypeDef = TypedDict(
    "ParameterMetadataTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"],
        "Policies": List["ParameterInlinePolicyTypeDef"],
        "DataType": str,
    },
    total=False,
)

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Type": Literal["String", "StringList", "SecureString"],
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
        "DataType": str,
    },
    total=False,
)

PatchBaselineIdentityTypeDef = TypedDict(
    "PatchBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
            "ORACLE_LINUX",
            "DEBIAN",
        ],
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

PatchComplianceDataTypeDef = TypedDict(
    "PatchComplianceDataTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": Literal[
            "INSTALLED",
            "INSTALLED_OTHER",
            "INSTALLED_PENDING_REBOOT",
            "INSTALLED_REJECTED",
            "MISSING",
            "NOT_APPLICABLE",
            "FAILED",
        ],
        "InstalledTime": datetime,
    },
)

PatchFilterGroupTypeDef = TypedDict(
    "PatchFilterGroupTypeDef", {"PatchFilters": List["PatchFilterTypeDef"]}
)

PatchFilterTypeDef = TypedDict(
    "PatchFilterTypeDef",
    {
        "Key": Literal[
            "PATCH_SET",
            "PRODUCT",
            "PRODUCT_FAMILY",
            "CLASSIFICATION",
            "MSRC_SEVERITY",
            "PATCH_ID",
            "SECTION",
            "PRIORITY",
            "SEVERITY",
        ],
        "Values": List[str],
    },
)

PatchGroupPatchBaselineMappingTypeDef = TypedDict(
    "PatchGroupPatchBaselineMappingTypeDef",
    {"PatchGroup": str, "BaselineIdentity": "PatchBaselineIdentityTypeDef"},
    total=False,
)

PatchRuleGroupTypeDef = TypedDict("PatchRuleGroupTypeDef", {"PatchRules": List["PatchRuleTypeDef"]})

_RequiredPatchRuleTypeDef = TypedDict(
    "_RequiredPatchRuleTypeDef", {"PatchFilterGroup": "PatchFilterGroupTypeDef"}
)
_OptionalPatchRuleTypeDef = TypedDict(
    "_OptionalPatchRuleTypeDef",
    {
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApproveAfterDays": int,
        "ApproveUntilDate": str,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class PatchRuleTypeDef(_RequiredPatchRuleTypeDef, _OptionalPatchRuleTypeDef):
    pass


PatchSourceTypeDef = TypedDict(
    "PatchSourceTypeDef", {"Name": str, "Products": List[str], "Configuration": str}
)

PatchStatusTypeDef = TypedDict(
    "PatchStatusTypeDef",
    {
        "DeploymentStatus": Literal[
            "APPROVED", "PENDING_APPROVAL", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED"
        ],
        "ComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovalDate": datetime,
    },
    total=False,
)

PatchTypeDef = TypedDict(
    "PatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
    },
    total=False,
)

ProgressCountersTypeDef = TypedDict(
    "ProgressCountersTypeDef",
    {
        "TotalSteps": int,
        "SuccessSteps": int,
        "FailedSteps": int,
        "CancelledSteps": int,
        "TimedOutSteps": int,
    },
    total=False,
)

RelatedOpsItemTypeDef = TypedDict("RelatedOpsItemTypeDef", {"OpsItemId": str})

ResolvedTargetsTypeDef = TypedDict(
    "ResolvedTargetsTypeDef", {"ParameterValues": List[str], "Truncated": bool}, total=False
)

ResourceComplianceSummaryItemTypeDef = TypedDict(
    "ResourceComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
        "OverallSeverity": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "CompliantSummary": "CompliantSummaryTypeDef",
        "NonCompliantSummary": "NonCompliantSummaryTypeDef",
    },
    total=False,
)

_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef", {"OrganizationSourceType": str}
)
_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef",
    {"OrganizationalUnits": List["ResourceDataSyncOrganizationalUnitTypeDef"]},
    total=False,
)


class ResourceDataSyncAwsOrganizationsSourceTypeDef(
    _RequiredResourceDataSyncAwsOrganizationsSourceTypeDef,
    _OptionalResourceDataSyncAwsOrganizationsSourceTypeDef,
):
    pass


ResourceDataSyncDestinationDataSharingTypeDef = TypedDict(
    "ResourceDataSyncDestinationDataSharingTypeDef",
    {"DestinationDataSharingType": str},
    total=False,
)

ResourceDataSyncItemTypeDef = TypedDict(
    "ResourceDataSyncItemTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": "ResourceDataSyncSourceWithStateTypeDef",
        "S3Destination": "ResourceDataSyncS3DestinationTypeDef",
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": Literal["Successful", "Failed", "InProgress"],
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)

ResourceDataSyncOrganizationalUnitTypeDef = TypedDict(
    "ResourceDataSyncOrganizationalUnitTypeDef", {"OrganizationalUnitId": str}, total=False
)

_RequiredResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_RequiredResourceDataSyncS3DestinationTypeDef",
    {"BucketName": str, "SyncFormat": Literal["JsonSerDe"], "Region": str},
)
_OptionalResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_OptionalResourceDataSyncS3DestinationTypeDef",
    {
        "Prefix": str,
        "AWSKMSKeyARN": str,
        "DestinationDataSharing": "ResourceDataSyncDestinationDataSharingTypeDef",
    },
    total=False,
)


class ResourceDataSyncS3DestinationTypeDef(
    _RequiredResourceDataSyncS3DestinationTypeDef, _OptionalResourceDataSyncS3DestinationTypeDef
):
    pass


ResourceDataSyncSourceWithStateTypeDef = TypedDict(
    "ResourceDataSyncSourceWithStateTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": "ResourceDataSyncAwsOrganizationsSourceTypeDef",
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
    },
    total=False,
)

S3OutputLocationTypeDef = TypedDict(
    "S3OutputLocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

S3OutputUrlTypeDef = TypedDict("S3OutputUrlTypeDef", {"OutputUrl": str}, total=False)

ScheduledWindowExecutionTypeDef = TypedDict(
    "ScheduledWindowExecutionTypeDef",
    {"WindowId": str, "Name": str, "ExecutionTime": str},
    total=False,
)

ServiceSettingTypeDef = TypedDict(
    "ServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)

SessionManagerOutputUrlTypeDef = TypedDict(
    "SessionManagerOutputUrlTypeDef", {"S3OutputUrl": str, "CloudWatchOutputUrl": str}, total=False
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": Literal[
            "Connected", "Connecting", "Disconnected", "Terminated", "Terminating", "Failed"
        ],
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": "SessionManagerOutputUrlTypeDef",
    },
    total=False,
)

SeveritySummaryTypeDef = TypedDict(
    "SeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

StepExecutionTypeDef = TypedDict(
    "StepExecutionTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": Literal[
            "Pending",
            "InProgress",
            "Waiting",
            "Success",
            "TimedOut",
            "Cancelling",
            "Cancelled",
            "Failed",
        ],
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": "FailureDetailsTypeDef",
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List["TargetTypeDef"],
        "TargetLocation": "TargetLocationTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TargetLocationTypeDef = TypedDict(
    "TargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

TargetTypeDef = TypedDict("TargetTypeDef", {"Key": str, "Values": List[str]}, total=False)

AssociationExecutionFilterTypeDef = TypedDict(
    "AssociationExecutionFilterTypeDef",
    {
        "Key": Literal["ExecutionId", "Status", "CreatedTime"],
        "Value": str,
        "Type": Literal["EQUAL", "LESS_THAN", "GREATER_THAN"],
    },
)

AssociationExecutionTargetsFilterTypeDef = TypedDict(
    "AssociationExecutionTargetsFilterTypeDef",
    {"Key": Literal["Status", "ResourceId", "ResourceType"], "Value": str},
)

AssociationFilterTypeDef = TypedDict(
    "AssociationFilterTypeDef",
    {
        "key": Literal[
            "InstanceId",
            "Name",
            "AssociationId",
            "AssociationStatusName",
            "LastExecutedBefore",
            "LastExecutedAfter",
            "AssociationName",
            "ResourceGroupName",
        ],
        "value": str,
    },
)

AttachmentsSourceTypeDef = TypedDict(
    "AttachmentsSourceTypeDef",
    {
        "Key": Literal["SourceUrl", "S3FileUrl", "AttachmentReference"],
        "Values": List[str],
        "Name": str,
    },
    total=False,
)

AutomationExecutionFilterTypeDef = TypedDict(
    "AutomationExecutionFilterTypeDef",
    {
        "Key": Literal[
            "DocumentNamePrefix",
            "ExecutionStatus",
            "ExecutionId",
            "ParentExecutionId",
            "CurrentAction",
            "StartTimeBefore",
            "StartTimeAfter",
            "AutomationType",
            "TagKey",
        ],
        "Values": List[str],
    },
)

CancelMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionResultTypeDef", {"WindowExecutionId": str}, total=False
)

CommandFilterTypeDef = TypedDict(
    "CommandFilterTypeDef",
    {
        "key": Literal["InvokedAfter", "InvokedBefore", "Status", "ExecutionStage", "DocumentName"],
        "value": str,
    },
)

_RequiredComplianceItemEntryTypeDef = TypedDict(
    "_RequiredComplianceItemEntryTypeDef",
    {
        "Severity": Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"],
        "Status": Literal["COMPLIANT", "NON_COMPLIANT"],
    },
)
_OptionalComplianceItemEntryTypeDef = TypedDict(
    "_OptionalComplianceItemEntryTypeDef",
    {"Id": str, "Title": str, "Details": Dict[str, str]},
    total=False,
)


class ComplianceItemEntryTypeDef(
    _RequiredComplianceItemEntryTypeDef, _OptionalComplianceItemEntryTypeDef
):
    pass


ComplianceStringFilterTypeDef = TypedDict(
    "ComplianceStringFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["EQUAL", "NOT_EQUAL", "BEGIN_WITH", "LESS_THAN", "GREATER_THAN"],
    },
    total=False,
)

CreateActivationResultTypeDef = TypedDict(
    "CreateActivationResultTypeDef", {"ActivationId": str, "ActivationCode": str}, total=False
)

CreateAssociationBatchResultTypeDef = TypedDict(
    "CreateAssociationBatchResultTypeDef",
    {
        "Successful": List["AssociationDescriptionTypeDef"],
        "Failed": List["FailedCreateAssociationTypeDef"],
    },
    total=False,
)

CreateAssociationResultTypeDef = TypedDict(
    "CreateAssociationResultTypeDef",
    {"AssociationDescription": "AssociationDescriptionTypeDef"},
    total=False,
)

CreateDocumentResultTypeDef = TypedDict(
    "CreateDocumentResultTypeDef",
    {"DocumentDescription": "DocumentDescriptionTypeDef"},
    total=False,
)

CreateMaintenanceWindowResultTypeDef = TypedDict(
    "CreateMaintenanceWindowResultTypeDef", {"WindowId": str}, total=False
)

CreateOpsItemResponseTypeDef = TypedDict(
    "CreateOpsItemResponseTypeDef", {"OpsItemId": str}, total=False
)

CreatePatchBaselineResultTypeDef = TypedDict(
    "CreatePatchBaselineResultTypeDef", {"BaselineId": str}, total=False
)

DeleteInventoryResultTypeDef = TypedDict(
    "DeleteInventoryResultTypeDef",
    {"DeletionId": str, "TypeName": str, "DeletionSummary": "InventoryDeletionSummaryTypeDef"},
    total=False,
)

DeleteMaintenanceWindowResultTypeDef = TypedDict(
    "DeleteMaintenanceWindowResultTypeDef", {"WindowId": str}, total=False
)

DeleteParametersResultTypeDef = TypedDict(
    "DeleteParametersResultTypeDef",
    {"DeletedParameters": List[str], "InvalidParameters": List[str]},
    total=False,
)

DeletePatchBaselineResultTypeDef = TypedDict(
    "DeletePatchBaselineResultTypeDef", {"BaselineId": str}, total=False
)

DeregisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)

DeregisterTargetFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    {"WindowId": str, "WindowTargetId": str},
    total=False,
)

DeregisterTaskFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    {"WindowId": str, "WindowTaskId": str},
    total=False,
)

DescribeActivationsFilterTypeDef = TypedDict(
    "DescribeActivationsFilterTypeDef",
    {
        "FilterKey": Literal["ActivationIds", "DefaultInstanceName", "IamRole"],
        "FilterValues": List[str],
    },
    total=False,
)

DescribeActivationsResultTypeDef = TypedDict(
    "DescribeActivationsResultTypeDef",
    {"ActivationList": List["ActivationTypeDef"], "NextToken": str},
    total=False,
)

DescribeAssociationExecutionTargetsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsResultTypeDef",
    {"AssociationExecutionTargets": List["AssociationExecutionTargetTypeDef"], "NextToken": str},
    total=False,
)

DescribeAssociationExecutionsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionsResultTypeDef",
    {"AssociationExecutions": List["AssociationExecutionTypeDef"], "NextToken": str},
    total=False,
)

DescribeAssociationResultTypeDef = TypedDict(
    "DescribeAssociationResultTypeDef",
    {"AssociationDescription": "AssociationDescriptionTypeDef"},
    total=False,
)

DescribeAutomationExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationExecutionsResultTypeDef",
    {
        "AutomationExecutionMetadataList": List["AutomationExecutionMetadataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeAutomationStepExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsResultTypeDef",
    {"StepExecutions": List["StepExecutionTypeDef"], "NextToken": str},
    total=False,
)

DescribeAvailablePatchesResultTypeDef = TypedDict(
    "DescribeAvailablePatchesResultTypeDef",
    {"Patches": List["PatchTypeDef"], "NextToken": str},
    total=False,
)

DescribeDocumentPermissionResponseTypeDef = TypedDict(
    "DescribeDocumentPermissionResponseTypeDef",
    {"AccountIds": List[str], "AccountSharingInfoList": List["AccountSharingInfoTypeDef"]},
    total=False,
)

DescribeDocumentResultTypeDef = TypedDict(
    "DescribeDocumentResultTypeDef", {"Document": "DocumentDescriptionTypeDef"}, total=False
)

DescribeEffectiveInstanceAssociationsResultTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    {"Associations": List["InstanceAssociationTypeDef"], "NextToken": str},
    total=False,
)

DescribeEffectivePatchesForPatchBaselineResultTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    {"EffectivePatches": List["EffectivePatchTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstanceAssociationsStatusResultTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusResultTypeDef",
    {
        "InstanceAssociationStatusInfos": List["InstanceAssociationStatusInfoTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceInformationResultTypeDef = TypedDict(
    "DescribeInstanceInformationResultTypeDef",
    {"InstanceInformationList": List["InstanceInformationTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstancePatchStatesForPatchGroupResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    {"InstancePatchStates": List["InstancePatchStateTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstancePatchStatesResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesResultTypeDef",
    {"InstancePatchStates": List["InstancePatchStateTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstancePatchesResultTypeDef = TypedDict(
    "DescribeInstancePatchesResultTypeDef",
    {"Patches": List["PatchComplianceDataTypeDef"], "NextToken": str},
    total=False,
)

DescribeInventoryDeletionsResultTypeDef = TypedDict(
    "DescribeInventoryDeletionsResultTypeDef",
    {"InventoryDeletions": List["InventoryDeletionStatusItemTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeMaintenanceWindowExecutionTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    {
        "WindowExecutionTaskIdentities": List["MaintenanceWindowExecutionTaskIdentityTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeMaintenanceWindowExecutionsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    {"WindowExecutions": List["MaintenanceWindowExecutionTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowScheduleResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    {"ScheduledWindowExecutions": List["ScheduledWindowExecutionTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowTargetsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    {"Targets": List["MaintenanceWindowTargetTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksResultTypeDef",
    {"Tasks": List["MaintenanceWindowTaskTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowsForTargetResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    {"WindowIdentities": List["MaintenanceWindowIdentityForTargetTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsResultTypeDef",
    {"WindowIdentities": List["MaintenanceWindowIdentityTypeDef"], "NextToken": str},
    total=False,
)

DescribeOpsItemsResponseTypeDef = TypedDict(
    "DescribeOpsItemsResponseTypeDef",
    {"NextToken": str, "OpsItemSummaries": List["OpsItemSummaryTypeDef"]},
    total=False,
)

DescribeParametersResultTypeDef = TypedDict(
    "DescribeParametersResultTypeDef",
    {"Parameters": List["ParameterMetadataTypeDef"], "NextToken": str},
    total=False,
)

DescribePatchBaselinesResultTypeDef = TypedDict(
    "DescribePatchBaselinesResultTypeDef",
    {"BaselineIdentities": List["PatchBaselineIdentityTypeDef"], "NextToken": str},
    total=False,
)

DescribePatchGroupStateResultTypeDef = TypedDict(
    "DescribePatchGroupStateResultTypeDef",
    {
        "Instances": int,
        "InstancesWithInstalledPatches": int,
        "InstancesWithInstalledOtherPatches": int,
        "InstancesWithInstalledPendingRebootPatches": int,
        "InstancesWithInstalledRejectedPatches": int,
        "InstancesWithMissingPatches": int,
        "InstancesWithFailedPatches": int,
        "InstancesWithNotApplicablePatches": int,
        "InstancesWithUnreportedNotApplicablePatches": int,
    },
    total=False,
)

DescribePatchGroupsResultTypeDef = TypedDict(
    "DescribePatchGroupsResultTypeDef",
    {"Mappings": List["PatchGroupPatchBaselineMappingTypeDef"], "NextToken": str},
    total=False,
)

DescribePatchPropertiesResultTypeDef = TypedDict(
    "DescribePatchPropertiesResultTypeDef",
    {"Properties": List[Dict[str, str]], "NextToken": str},
    total=False,
)

DescribeSessionsResponseTypeDef = TypedDict(
    "DescribeSessionsResponseTypeDef",
    {"Sessions": List["SessionTypeDef"], "NextToken": str},
    total=False,
)

InventoryAggregatorTypeDef = TypedDict(
    "InventoryAggregatorTypeDef",
    {
        "Expression": str,
        "Aggregators": List[Dict[str, Any]],
        "Groups": List["InventoryGroupTypeDef"],
    },
    total=False,
)

OpsAggregatorTypeDef = TypedDict(
    "OpsAggregatorTypeDef",
    {
        "AggregatorType": str,
        "TypeName": str,
        "AttributeName": str,
        "Values": Dict[str, str],
        "Filters": List["OpsFilterTypeDef"],
        "Aggregators": List[Dict[str, Any]],
    },
    total=False,
)

DocumentFilterTypeDef = TypedDict(
    "DocumentFilterTypeDef",
    {"key": Literal["Name", "Owner", "PlatformTypes", "DocumentType"], "value": str},
)

DocumentKeyValuesFilterTypeDef = TypedDict(
    "DocumentKeyValuesFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

GetAutomationExecutionResultTypeDef = TypedDict(
    "GetAutomationExecutionResultTypeDef",
    {"AutomationExecution": "AutomationExecutionTypeDef"},
    total=False,
)

GetCalendarStateResponseTypeDef = TypedDict(
    "GetCalendarStateResponseTypeDef",
    {"State": Literal["OPEN", "CLOSED"], "AtTime": str, "NextTransitionTime": str},
    total=False,
)

GetCommandInvocationResultTypeDef = TypedDict(
    "GetCommandInvocationResultTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "PluginName": str,
        "ResponseCode": int,
        "ExecutionStartDateTime": str,
        "ExecutionElapsedTime": str,
        "ExecutionEndDateTime": str,
        "Status": Literal[
            "Pending",
            "InProgress",
            "Delayed",
            "Success",
            "Cancelled",
            "TimedOut",
            "Failed",
            "Cancelling",
        ],
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
    },
    total=False,
)

GetConnectionStatusResponseTypeDef = TypedDict(
    "GetConnectionStatusResponseTypeDef",
    {"Target": str, "Status": Literal["Connected", "NotConnected"]},
    total=False,
)

GetDefaultPatchBaselineResultTypeDef = TypedDict(
    "GetDefaultPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
            "ORACLE_LINUX",
            "DEBIAN",
        ],
    },
    total=False,
)

GetDeployablePatchSnapshotForInstanceResultTypeDef = TypedDict(
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    {"InstanceId": str, "SnapshotId": str, "SnapshotDownloadUrl": str, "Product": str},
    total=False,
)

GetDocumentResultTypeDef = TypedDict(
    "GetDocumentResultTypeDef",
    {
        "Name": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": Literal["Creating", "Active", "Updating", "Deleting", "Failed"],
        "StatusInformation": str,
        "Content": str,
        "DocumentType": Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ],
        "DocumentFormat": Literal["YAML", "JSON", "TEXT"],
        "Requires": List["DocumentRequiresTypeDef"],
        "AttachmentsContent": List["AttachmentContentTypeDef"],
    },
    total=False,
)

GetInventoryResultTypeDef = TypedDict(
    "GetInventoryResultTypeDef",
    {"Entities": List["InventoryResultEntityTypeDef"], "NextToken": str},
    total=False,
)

GetInventorySchemaResultTypeDef = TypedDict(
    "GetInventorySchemaResultTypeDef",
    {"Schemas": List["InventoryItemSchemaTypeDef"], "NextToken": str},
    total=False,
)

GetMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

GetMaintenanceWindowExecutionTaskInvocationResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "Parameters": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

GetMaintenanceWindowExecutionTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "TaskParameters": List[Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": Literal[
            "PENDING",
            "IN_PROGRESS",
            "SUCCESS",
            "FAILED",
            "TIMED_OUT",
            "CANCELLING",
            "CANCELLED",
            "SKIPPED_OVERLAPPING",
        ],
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

GetMaintenanceWindowResultTypeDef = TypedDict(
    "GetMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "NextExecutionTime": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
    },
    total=False,
)

GetMaintenanceWindowTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
    },
    total=False,
)

GetOpsItemResponseTypeDef = TypedDict(
    "GetOpsItemResponseTypeDef", {"OpsItem": "OpsItemTypeDef"}, total=False
)

GetOpsSummaryResultTypeDef = TypedDict(
    "GetOpsSummaryResultTypeDef",
    {"Entities": List["OpsEntityTypeDef"], "NextToken": str},
    total=False,
)

GetParameterHistoryResultTypeDef = TypedDict(
    "GetParameterHistoryResultTypeDef",
    {"Parameters": List["ParameterHistoryTypeDef"], "NextToken": str},
    total=False,
)

GetParameterResultTypeDef = TypedDict(
    "GetParameterResultTypeDef", {"Parameter": "ParameterTypeDef"}, total=False
)

GetParametersByPathResultTypeDef = TypedDict(
    "GetParametersByPathResultTypeDef",
    {"Parameters": List["ParameterTypeDef"], "NextToken": str},
    total=False,
)

GetParametersResultTypeDef = TypedDict(
    "GetParametersResultTypeDef",
    {"Parameters": List["ParameterTypeDef"], "InvalidParameters": List[str]},
    total=False,
)

GetPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "GetPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
            "ORACLE_LINUX",
            "DEBIAN",
        ],
    },
    total=False,
)

GetPatchBaselineResultTypeDef = TypedDict(
    "GetPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
            "ORACLE_LINUX",
            "DEBIAN",
        ],
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": Literal["ALLOW_AS_DEPENDENCY", "BLOCK"],
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
    },
    total=False,
)

GetServiceSettingResultTypeDef = TypedDict(
    "GetServiceSettingResultTypeDef", {"ServiceSetting": "ServiceSettingTypeDef"}, total=False
)

InstanceInformationFilterTypeDef = TypedDict(
    "InstanceInformationFilterTypeDef",
    {
        "key": Literal[
            "InstanceIds",
            "AgentVersion",
            "PingStatus",
            "PlatformTypes",
            "ActivationIds",
            "IamRole",
            "ResourceType",
            "AssociationStatus",
        ],
        "valueSet": List[str],
    },
)

InstanceInformationStringFilterTypeDef = TypedDict(
    "InstanceInformationStringFilterTypeDef", {"Key": str, "Values": List[str]}
)

InstancePatchStateFilterTypeDef = TypedDict(
    "InstancePatchStateFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": Literal["Equal", "NotEqual", "LessThan", "GreaterThan"],
    },
)

_RequiredInventoryItemTypeDef = TypedDict(
    "_RequiredInventoryItemTypeDef", {"TypeName": str, "SchemaVersion": str, "CaptureTime": str}
)
_OptionalInventoryItemTypeDef = TypedDict(
    "_OptionalInventoryItemTypeDef",
    {"ContentHash": str, "Content": List[Dict[str, str]], "Context": Dict[str, str]},
    total=False,
)


class InventoryItemTypeDef(_RequiredInventoryItemTypeDef, _OptionalInventoryItemTypeDef):
    pass


LabelParameterVersionResultTypeDef = TypedDict(
    "LabelParameterVersionResultTypeDef",
    {"InvalidLabels": List[str], "ParameterVersion": int},
    total=False,
)

ListAssociationVersionsResultTypeDef = TypedDict(
    "ListAssociationVersionsResultTypeDef",
    {"AssociationVersions": List["AssociationVersionInfoTypeDef"], "NextToken": str},
    total=False,
)

ListAssociationsResultTypeDef = TypedDict(
    "ListAssociationsResultTypeDef",
    {"Associations": List["AssociationTypeDef"], "NextToken": str},
    total=False,
)

ListCommandInvocationsResultTypeDef = TypedDict(
    "ListCommandInvocationsResultTypeDef",
    {"CommandInvocations": List["CommandInvocationTypeDef"], "NextToken": str},
    total=False,
)

ListCommandsResultTypeDef = TypedDict(
    "ListCommandsResultTypeDef", {"Commands": List["CommandTypeDef"], "NextToken": str}, total=False
)

ListComplianceItemsResultTypeDef = TypedDict(
    "ListComplianceItemsResultTypeDef",
    {"ComplianceItems": List["ComplianceItemTypeDef"], "NextToken": str},
    total=False,
)

ListComplianceSummariesResultTypeDef = TypedDict(
    "ListComplianceSummariesResultTypeDef",
    {"ComplianceSummaryItems": List["ComplianceSummaryItemTypeDef"], "NextToken": str},
    total=False,
)

ListDocumentVersionsResultTypeDef = TypedDict(
    "ListDocumentVersionsResultTypeDef",
    {"DocumentVersions": List["DocumentVersionInfoTypeDef"], "NextToken": str},
    total=False,
)

ListDocumentsResultTypeDef = TypedDict(
    "ListDocumentsResultTypeDef",
    {"DocumentIdentifiers": List["DocumentIdentifierTypeDef"], "NextToken": str},
    total=False,
)

ListInventoryEntriesResultTypeDef = TypedDict(
    "ListInventoryEntriesResultTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
    },
    total=False,
)

ListResourceComplianceSummariesResultTypeDef = TypedDict(
    "ListResourceComplianceSummariesResultTypeDef",
    {
        "ResourceComplianceSummaryItems": List["ResourceComplianceSummaryItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListResourceDataSyncResultTypeDef = TypedDict(
    "ListResourceDataSyncResultTypeDef",
    {"ResourceDataSyncItems": List["ResourceDataSyncItemTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

MaintenanceWindowFilterTypeDef = TypedDict(
    "MaintenanceWindowFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

OpsItemFilterTypeDef = TypedDict(
    "OpsItemFilterTypeDef",
    {
        "Key": Literal[
            "Status",
            "CreatedBy",
            "Source",
            "Priority",
            "Title",
            "OpsItemId",
            "CreatedTime",
            "LastModifiedTime",
            "OperationalData",
            "OperationalDataKey",
            "OperationalDataValue",
            "ResourceId",
            "AutomationId",
            "Category",
            "Severity",
        ],
        "Values": List[str],
        "Operator": Literal["Equal", "Contains", "GreaterThan", "LessThan"],
    },
)

OpsResultAttributeTypeDef = TypedDict("OpsResultAttributeTypeDef", {"TypeName": str})

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredParameterStringFilterTypeDef = TypedDict(
    "_RequiredParameterStringFilterTypeDef", {"Key": str}
)
_OptionalParameterStringFilterTypeDef = TypedDict(
    "_OptionalParameterStringFilterTypeDef", {"Option": str, "Values": List[str]}, total=False
)


class ParameterStringFilterTypeDef(
    _RequiredParameterStringFilterTypeDef, _OptionalParameterStringFilterTypeDef
):
    pass


ParametersFilterTypeDef = TypedDict(
    "ParametersFilterTypeDef", {"Key": Literal["Name", "Type", "KeyId"], "Values": List[str]}
)

PatchOrchestratorFilterTypeDef = TypedDict(
    "PatchOrchestratorFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

PutInventoryResultTypeDef = TypedDict("PutInventoryResultTypeDef", {"Message": str}, total=False)

PutParameterResultTypeDef = TypedDict(
    "PutParameterResultTypeDef",
    {"Version": int, "Tier": Literal["Standard", "Advanced", "Intelligent-Tiering"]},
    total=False,
)

RegisterDefaultPatchBaselineResultTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineResultTypeDef", {"BaselineId": str}, total=False
)

RegisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)

RegisterTargetWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTargetWithMaintenanceWindowResultTypeDef", {"WindowTargetId": str}, total=False
)

RegisterTaskWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTaskWithMaintenanceWindowResultTypeDef", {"WindowTaskId": str}, total=False
)

ResetServiceSettingResultTypeDef = TypedDict(
    "ResetServiceSettingResultTypeDef", {"ServiceSetting": "ServiceSettingTypeDef"}, total=False
)

_RequiredResourceDataSyncSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncSourceTypeDef", {"SourceType": str, "SourceRegions": List[str]}
)
_OptionalResourceDataSyncSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": "ResourceDataSyncAwsOrganizationsSourceTypeDef",
        "IncludeFutureRegions": bool,
    },
    total=False,
)


class ResourceDataSyncSourceTypeDef(
    _RequiredResourceDataSyncSourceTypeDef, _OptionalResourceDataSyncSourceTypeDef
):
    pass


ResultAttributeTypeDef = TypedDict("ResultAttributeTypeDef", {"TypeName": str})

ResumeSessionResponseTypeDef = TypedDict(
    "ResumeSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)

SendCommandResultTypeDef = TypedDict(
    "SendCommandResultTypeDef", {"Command": "CommandTypeDef"}, total=False
)

SessionFilterTypeDef = TypedDict(
    "SessionFilterTypeDef",
    {"key": Literal["InvokedAfter", "InvokedBefore", "Target", "Owner", "Status"], "value": str},
)

StartAutomationExecutionResultTypeDef = TypedDict(
    "StartAutomationExecutionResultTypeDef", {"AutomationExecutionId": str}, total=False
)

StartSessionResponseTypeDef = TypedDict(
    "StartSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)

StepExecutionFilterTypeDef = TypedDict(
    "StepExecutionFilterTypeDef",
    {
        "Key": Literal[
            "StartTimeBefore",
            "StartTimeAfter",
            "StepExecutionStatus",
            "StepExecutionId",
            "StepName",
            "Action",
        ],
        "Values": List[str],
    },
)

TerminateSessionResponseTypeDef = TypedDict(
    "TerminateSessionResponseTypeDef", {"SessionId": str}, total=False
)

UpdateAssociationResultTypeDef = TypedDict(
    "UpdateAssociationResultTypeDef",
    {"AssociationDescription": "AssociationDescriptionTypeDef"},
    total=False,
)

UpdateAssociationStatusResultTypeDef = TypedDict(
    "UpdateAssociationStatusResultTypeDef",
    {"AssociationDescription": "AssociationDescriptionTypeDef"},
    total=False,
)

UpdateDocumentDefaultVersionResultTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionResultTypeDef",
    {"Description": "DocumentDefaultVersionDescriptionTypeDef"},
    total=False,
)

UpdateDocumentResultTypeDef = TypedDict(
    "UpdateDocumentResultTypeDef",
    {"DocumentDescription": "DocumentDescriptionTypeDef"},
    total=False,
)

UpdateMaintenanceWindowResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
    },
    total=False,
)

UpdateMaintenanceWindowTargetResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTargetResultTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

UpdateMaintenanceWindowTaskResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
    },
    total=False,
)

UpdatePatchBaselineResultTypeDef = TypedDict(
    "UpdatePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
            "ORACLE_LINUX",
            "DEBIAN",
        ],
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ],
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": Literal["ALLOW_AS_DEPENDENCY", "BLOCK"],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
