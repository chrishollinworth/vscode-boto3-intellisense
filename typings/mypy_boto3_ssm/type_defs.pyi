"""
Type annotations for ssm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm.type_defs import AccountSharingInfoTypeDef

    data: AccountSharingInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AssociationComplianceSeverityType,
    AssociationExecutionFilterKeyType,
    AssociationExecutionTargetsFilterKeyType,
    AssociationFilterKeyType,
    AssociationFilterOperatorTypeType,
    AssociationStatusNameType,
    AssociationSyncComplianceType,
    AttachmentsSourceKeyType,
    AutomationExecutionFilterKeyType,
    AutomationExecutionStatusType,
    AutomationTypeType,
    CalendarStateType,
    CommandFilterKeyType,
    CommandInvocationStatusType,
    CommandPluginStatusType,
    CommandStatusType,
    ComplianceQueryOperatorTypeType,
    ComplianceSeverityType,
    ComplianceStatusType,
    ComplianceUploadTypeType,
    ConnectionStatusType,
    DescribeActivationsFilterKeysType,
    DocumentFilterKeyType,
    DocumentFormatType,
    DocumentHashTypeType,
    DocumentParameterTypeType,
    DocumentReviewActionType,
    DocumentStatusType,
    DocumentTypeType,
    ExecutionModeType,
    FaultType,
    InstanceInformationFilterKeyType,
    InstancePatchStateOperatorTypeType,
    InventoryAttributeDataTypeType,
    InventoryDeletionStatusType,
    InventoryQueryOperatorTypeType,
    InventorySchemaDeleteOptionType,
    LastResourceDataSyncStatusType,
    MaintenanceWindowExecutionStatusType,
    MaintenanceWindowResourceTypeType,
    MaintenanceWindowTaskTypeType,
    NotificationEventType,
    NotificationTypeType,
    OperatingSystemType,
    OpsFilterOperatorTypeType,
    OpsItemDataTypeType,
    OpsItemFilterKeyType,
    OpsItemFilterOperatorType,
    OpsItemRelatedItemsFilterKeyType,
    OpsItemStatusType,
    ParametersFilterKeyType,
    ParameterTierType,
    ParameterTypeType,
    PatchActionType,
    PatchComplianceDataStateType,
    PatchComplianceLevelType,
    PatchDeploymentStatusType,
    PatchFilterKeyType,
    PatchOperationTypeType,
    PatchPropertyType,
    PatchSetType,
    PingStatusType,
    PlatformTypeType,
    RebootOptionType,
    ResourceTypeForTaggingType,
    ResourceTypeType,
    ReviewStatusType,
    SessionFilterKeyType,
    SessionStateType,
    SessionStatusType,
    SignalTypeType,
    StepExecutionFilterKeyType,
    StopTypeType,
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
    "AccountSharingInfoTypeDef",
    "ActivationTypeDef",
    "AddTagsToResourceRequestRequestTypeDef",
    "AssociateOpsItemRelatedItemRequestRequestTypeDef",
    "AssociateOpsItemRelatedItemResponseTypeDef",
    "AssociationDescriptionTypeDef",
    "AssociationExecutionFilterTypeDef",
    "AssociationExecutionTargetTypeDef",
    "AssociationExecutionTargetsFilterTypeDef",
    "AssociationExecutionTypeDef",
    "AssociationFilterTypeDef",
    "AssociationOverviewTypeDef",
    "AssociationStatusTypeDef",
    "AssociationTypeDef",
    "AssociationVersionInfoTypeDef",
    "AttachmentContentTypeDef",
    "AttachmentInformationTypeDef",
    "AttachmentsSourceTypeDef",
    "AutomationExecutionFilterTypeDef",
    "AutomationExecutionMetadataTypeDef",
    "AutomationExecutionTypeDef",
    "BaselineOverrideTypeDef",
    "CancelCommandRequestRequestTypeDef",
    "CancelMaintenanceWindowExecutionRequestRequestTypeDef",
    "CancelMaintenanceWindowExecutionResultTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CommandFilterTypeDef",
    "CommandInvocationTypeDef",
    "CommandPluginTypeDef",
    "CommandTypeDef",
    "ComplianceExecutionSummaryTypeDef",
    "ComplianceItemEntryTypeDef",
    "ComplianceItemTypeDef",
    "ComplianceStringFilterTypeDef",
    "ComplianceSummaryItemTypeDef",
    "CompliantSummaryTypeDef",
    "CreateActivationRequestRequestTypeDef",
    "CreateActivationResultTypeDef",
    "CreateAssociationBatchRequestEntryTypeDef",
    "CreateAssociationBatchRequestRequestTypeDef",
    "CreateAssociationBatchResultTypeDef",
    "CreateAssociationRequestRequestTypeDef",
    "CreateAssociationResultTypeDef",
    "CreateDocumentRequestRequestTypeDef",
    "CreateDocumentResultTypeDef",
    "CreateMaintenanceWindowRequestRequestTypeDef",
    "CreateMaintenanceWindowResultTypeDef",
    "CreateOpsItemRequestRequestTypeDef",
    "CreateOpsItemResponseTypeDef",
    "CreateOpsMetadataRequestRequestTypeDef",
    "CreateOpsMetadataResultTypeDef",
    "CreatePatchBaselineRequestRequestTypeDef",
    "CreatePatchBaselineResultTypeDef",
    "CreateResourceDataSyncRequestRequestTypeDef",
    "DeleteActivationRequestRequestTypeDef",
    "DeleteAssociationRequestRequestTypeDef",
    "DeleteDocumentRequestRequestTypeDef",
    "DeleteInventoryRequestRequestTypeDef",
    "DeleteInventoryResultTypeDef",
    "DeleteMaintenanceWindowRequestRequestTypeDef",
    "DeleteMaintenanceWindowResultTypeDef",
    "DeleteOpsMetadataRequestRequestTypeDef",
    "DeleteParameterRequestRequestTypeDef",
    "DeleteParametersRequestRequestTypeDef",
    "DeleteParametersResultTypeDef",
    "DeletePatchBaselineRequestRequestTypeDef",
    "DeletePatchBaselineResultTypeDef",
    "DeleteResourceDataSyncRequestRequestTypeDef",
    "DeregisterManagedInstanceRequestRequestTypeDef",
    "DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    "DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef",
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    "DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef",
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    "DescribeActivationsFilterTypeDef",
    "DescribeActivationsRequestRequestTypeDef",
    "DescribeActivationsResultTypeDef",
    "DescribeAssociationExecutionTargetsRequestRequestTypeDef",
    "DescribeAssociationExecutionTargetsResultTypeDef",
    "DescribeAssociationExecutionsRequestRequestTypeDef",
    "DescribeAssociationExecutionsResultTypeDef",
    "DescribeAssociationRequestRequestTypeDef",
    "DescribeAssociationResultTypeDef",
    "DescribeAutomationExecutionsRequestRequestTypeDef",
    "DescribeAutomationExecutionsResultTypeDef",
    "DescribeAutomationStepExecutionsRequestRequestTypeDef",
    "DescribeAutomationStepExecutionsResultTypeDef",
    "DescribeAvailablePatchesRequestRequestTypeDef",
    "DescribeAvailablePatchesResultTypeDef",
    "DescribeDocumentPermissionRequestRequestTypeDef",
    "DescribeDocumentPermissionResponseTypeDef",
    "DescribeDocumentRequestRequestTypeDef",
    "DescribeDocumentResultTypeDef",
    "DescribeEffectiveInstanceAssociationsRequestRequestTypeDef",
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    "DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef",
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    "DescribeInstanceAssociationsStatusRequestRequestTypeDef",
    "DescribeInstanceAssociationsStatusResultTypeDef",
    "DescribeInstanceInformationRequestRequestTypeDef",
    "DescribeInstanceInformationResultTypeDef",
    "DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef",
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    "DescribeInstancePatchStatesRequestRequestTypeDef",
    "DescribeInstancePatchStatesResultTypeDef",
    "DescribeInstancePatchesRequestRequestTypeDef",
    "DescribeInstancePatchesResultTypeDef",
    "DescribeInventoryDeletionsRequestRequestTypeDef",
    "DescribeInventoryDeletionsResultTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    "DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    "DescribeMaintenanceWindowExecutionsRequestRequestTypeDef",
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    "DescribeMaintenanceWindowScheduleRequestRequestTypeDef",
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    "DescribeMaintenanceWindowTargetsRequestRequestTypeDef",
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    "DescribeMaintenanceWindowTasksRequestRequestTypeDef",
    "DescribeMaintenanceWindowTasksResultTypeDef",
    "DescribeMaintenanceWindowsForTargetRequestRequestTypeDef",
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    "DescribeMaintenanceWindowsRequestRequestTypeDef",
    "DescribeMaintenanceWindowsResultTypeDef",
    "DescribeOpsItemsRequestRequestTypeDef",
    "DescribeOpsItemsResponseTypeDef",
    "DescribeParametersRequestRequestTypeDef",
    "DescribeParametersResultTypeDef",
    "DescribePatchBaselinesRequestRequestTypeDef",
    "DescribePatchBaselinesResultTypeDef",
    "DescribePatchGroupStateRequestRequestTypeDef",
    "DescribePatchGroupStateResultTypeDef",
    "DescribePatchGroupsRequestRequestTypeDef",
    "DescribePatchGroupsResultTypeDef",
    "DescribePatchPropertiesRequestRequestTypeDef",
    "DescribePatchPropertiesResultTypeDef",
    "DescribeSessionsRequestRequestTypeDef",
    "DescribeSessionsResponseTypeDef",
    "DisassociateOpsItemRelatedItemRequestRequestTypeDef",
    "DocumentDefaultVersionDescriptionTypeDef",
    "DocumentDescriptionTypeDef",
    "DocumentFilterTypeDef",
    "DocumentIdentifierTypeDef",
    "DocumentKeyValuesFilterTypeDef",
    "DocumentMetadataResponseInfoTypeDef",
    "DocumentParameterTypeDef",
    "DocumentRequiresTypeDef",
    "DocumentReviewCommentSourceTypeDef",
    "DocumentReviewerResponseSourceTypeDef",
    "DocumentReviewsTypeDef",
    "DocumentVersionInfoTypeDef",
    "EffectivePatchTypeDef",
    "FailedCreateAssociationTypeDef",
    "FailureDetailsTypeDef",
    "GetAutomationExecutionRequestRequestTypeDef",
    "GetAutomationExecutionResultTypeDef",
    "GetCalendarStateRequestRequestTypeDef",
    "GetCalendarStateResponseTypeDef",
    "GetCommandInvocationRequestRequestTypeDef",
    "GetCommandInvocationResultTypeDef",
    "GetConnectionStatusRequestRequestTypeDef",
    "GetConnectionStatusResponseTypeDef",
    "GetDefaultPatchBaselineRequestRequestTypeDef",
    "GetDefaultPatchBaselineResultTypeDef",
    "GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef",
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    "GetDocumentRequestRequestTypeDef",
    "GetDocumentResultTypeDef",
    "GetInventoryRequestRequestTypeDef",
    "GetInventoryResultTypeDef",
    "GetInventorySchemaRequestRequestTypeDef",
    "GetInventorySchemaResultTypeDef",
    "GetMaintenanceWindowExecutionRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionResultTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    "GetMaintenanceWindowExecutionTaskRequestRequestTypeDef",
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    "GetMaintenanceWindowRequestRequestTypeDef",
    "GetMaintenanceWindowResultTypeDef",
    "GetMaintenanceWindowTaskRequestRequestTypeDef",
    "GetMaintenanceWindowTaskResultTypeDef",
    "GetOpsItemRequestRequestTypeDef",
    "GetOpsItemResponseTypeDef",
    "GetOpsMetadataRequestRequestTypeDef",
    "GetOpsMetadataResultTypeDef",
    "GetOpsSummaryRequestRequestTypeDef",
    "GetOpsSummaryResultTypeDef",
    "GetParameterHistoryRequestRequestTypeDef",
    "GetParameterHistoryResultTypeDef",
    "GetParameterRequestRequestTypeDef",
    "GetParameterResultTypeDef",
    "GetParametersByPathRequestRequestTypeDef",
    "GetParametersByPathResultTypeDef",
    "GetParametersRequestRequestTypeDef",
    "GetParametersResultTypeDef",
    "GetPatchBaselineForPatchGroupRequestRequestTypeDef",
    "GetPatchBaselineForPatchGroupResultTypeDef",
    "GetPatchBaselineRequestRequestTypeDef",
    "GetPatchBaselineResultTypeDef",
    "GetServiceSettingRequestRequestTypeDef",
    "GetServiceSettingResultTypeDef",
    "InstanceAggregatedAssociationOverviewTypeDef",
    "InstanceAssociationOutputLocationTypeDef",
    "InstanceAssociationOutputUrlTypeDef",
    "InstanceAssociationStatusInfoTypeDef",
    "InstanceAssociationTypeDef",
    "InstanceInformationFilterTypeDef",
    "InstanceInformationStringFilterTypeDef",
    "InstanceInformationTypeDef",
    "InstancePatchStateFilterTypeDef",
    "InstancePatchStateTypeDef",
    "InventoryAggregatorTypeDef",
    "InventoryDeletionStatusItemTypeDef",
    "InventoryDeletionSummaryItemTypeDef",
    "InventoryDeletionSummaryTypeDef",
    "InventoryFilterTypeDef",
    "InventoryGroupTypeDef",
    "InventoryItemAttributeTypeDef",
    "InventoryItemSchemaTypeDef",
    "InventoryItemTypeDef",
    "InventoryResultEntityTypeDef",
    "InventoryResultItemTypeDef",
    "LabelParameterVersionRequestRequestTypeDef",
    "LabelParameterVersionResultTypeDef",
    "ListAssociationVersionsRequestRequestTypeDef",
    "ListAssociationVersionsResultTypeDef",
    "ListAssociationsRequestRequestTypeDef",
    "ListAssociationsResultTypeDef",
    "ListCommandInvocationsRequestRequestTypeDef",
    "ListCommandInvocationsResultTypeDef",
    "ListCommandsRequestRequestTypeDef",
    "ListCommandsResultTypeDef",
    "ListComplianceItemsRequestRequestTypeDef",
    "ListComplianceItemsResultTypeDef",
    "ListComplianceSummariesRequestRequestTypeDef",
    "ListComplianceSummariesResultTypeDef",
    "ListDocumentMetadataHistoryRequestRequestTypeDef",
    "ListDocumentMetadataHistoryResponseTypeDef",
    "ListDocumentVersionsRequestRequestTypeDef",
    "ListDocumentVersionsResultTypeDef",
    "ListDocumentsRequestRequestTypeDef",
    "ListDocumentsResultTypeDef",
    "ListInventoryEntriesRequestRequestTypeDef",
    "ListInventoryEntriesResultTypeDef",
    "ListOpsItemEventsRequestRequestTypeDef",
    "ListOpsItemEventsResponseTypeDef",
    "ListOpsItemRelatedItemsRequestRequestTypeDef",
    "ListOpsItemRelatedItemsResponseTypeDef",
    "ListOpsMetadataRequestRequestTypeDef",
    "ListOpsMetadataResultTypeDef",
    "ListResourceComplianceSummariesRequestRequestTypeDef",
    "ListResourceComplianceSummariesResultTypeDef",
    "ListResourceDataSyncRequestRequestTypeDef",
    "ListResourceDataSyncResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LoggingInfoTypeDef",
    "MaintenanceWindowAutomationParametersTypeDef",
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    "MaintenanceWindowExecutionTypeDef",
    "MaintenanceWindowFilterTypeDef",
    "MaintenanceWindowIdentityForTargetTypeDef",
    "MaintenanceWindowIdentityTypeDef",
    "MaintenanceWindowLambdaParametersTypeDef",
    "MaintenanceWindowRunCommandParametersTypeDef",
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    "MaintenanceWindowTargetTypeDef",
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    "MaintenanceWindowTaskTypeDef",
    "MetadataValueTypeDef",
    "ModifyDocumentPermissionRequestRequestTypeDef",
    "NonCompliantSummaryTypeDef",
    "NotificationConfigTypeDef",
    "OpsAggregatorTypeDef",
    "OpsEntityItemTypeDef",
    "OpsEntityTypeDef",
    "OpsFilterTypeDef",
    "OpsItemDataValueTypeDef",
    "OpsItemEventFilterTypeDef",
    "OpsItemEventSummaryTypeDef",
    "OpsItemFilterTypeDef",
    "OpsItemIdentityTypeDef",
    "OpsItemNotificationTypeDef",
    "OpsItemRelatedItemSummaryTypeDef",
    "OpsItemRelatedItemsFilterTypeDef",
    "OpsItemSummaryTypeDef",
    "OpsItemTypeDef",
    "OpsMetadataFilterTypeDef",
    "OpsMetadataTypeDef",
    "OpsResultAttributeTypeDef",
    "OutputSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterHistoryTypeDef",
    "ParameterInlinePolicyTypeDef",
    "ParameterMetadataTypeDef",
    "ParameterStringFilterTypeDef",
    "ParameterTypeDef",
    "ParametersFilterTypeDef",
    "PatchBaselineIdentityTypeDef",
    "PatchComplianceDataTypeDef",
    "PatchFilterGroupTypeDef",
    "PatchFilterTypeDef",
    "PatchGroupPatchBaselineMappingTypeDef",
    "PatchOrchestratorFilterTypeDef",
    "PatchRuleGroupTypeDef",
    "PatchRuleTypeDef",
    "PatchSourceTypeDef",
    "PatchStatusTypeDef",
    "PatchTypeDef",
    "ProgressCountersTypeDef",
    "PutComplianceItemsRequestRequestTypeDef",
    "PutInventoryRequestRequestTypeDef",
    "PutInventoryResultTypeDef",
    "PutParameterRequestRequestTypeDef",
    "PutParameterResultTypeDef",
    "RegisterDefaultPatchBaselineRequestRequestTypeDef",
    "RegisterDefaultPatchBaselineResultTypeDef",
    "RegisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    "RegisterTargetWithMaintenanceWindowRequestRequestTypeDef",
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    "RegisterTaskWithMaintenanceWindowRequestRequestTypeDef",
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    "RelatedOpsItemTypeDef",
    "RemoveTagsFromResourceRequestRequestTypeDef",
    "ResetServiceSettingRequestRequestTypeDef",
    "ResetServiceSettingResultTypeDef",
    "ResolvedTargetsTypeDef",
    "ResourceComplianceSummaryItemTypeDef",
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    "ResourceDataSyncDestinationDataSharingTypeDef",
    "ResourceDataSyncItemTypeDef",
    "ResourceDataSyncOrganizationalUnitTypeDef",
    "ResourceDataSyncS3DestinationTypeDef",
    "ResourceDataSyncSourceTypeDef",
    "ResourceDataSyncSourceWithStateTypeDef",
    "ResponseMetadataTypeDef",
    "ResultAttributeTypeDef",
    "ResumeSessionRequestRequestTypeDef",
    "ResumeSessionResponseTypeDef",
    "ReviewInformationTypeDef",
    "RunbookTypeDef",
    "S3OutputLocationTypeDef",
    "S3OutputUrlTypeDef",
    "ScheduledWindowExecutionTypeDef",
    "SendAutomationSignalRequestRequestTypeDef",
    "SendCommandRequestRequestTypeDef",
    "SendCommandResultTypeDef",
    "ServiceSettingTypeDef",
    "SessionFilterTypeDef",
    "SessionManagerOutputUrlTypeDef",
    "SessionTypeDef",
    "SeveritySummaryTypeDef",
    "StartAssociationsOnceRequestRequestTypeDef",
    "StartAutomationExecutionRequestRequestTypeDef",
    "StartAutomationExecutionResultTypeDef",
    "StartChangeRequestExecutionRequestRequestTypeDef",
    "StartChangeRequestExecutionResultTypeDef",
    "StartSessionRequestRequestTypeDef",
    "StartSessionResponseTypeDef",
    "StepExecutionFilterTypeDef",
    "StepExecutionTypeDef",
    "StopAutomationExecutionRequestRequestTypeDef",
    "TagTypeDef",
    "TargetLocationTypeDef",
    "TargetTypeDef",
    "TerminateSessionRequestRequestTypeDef",
    "TerminateSessionResponseTypeDef",
    "UnlabelParameterVersionRequestRequestTypeDef",
    "UnlabelParameterVersionResultTypeDef",
    "UpdateAssociationRequestRequestTypeDef",
    "UpdateAssociationResultTypeDef",
    "UpdateAssociationStatusRequestRequestTypeDef",
    "UpdateAssociationStatusResultTypeDef",
    "UpdateDocumentDefaultVersionRequestRequestTypeDef",
    "UpdateDocumentDefaultVersionResultTypeDef",
    "UpdateDocumentMetadataRequestRequestTypeDef",
    "UpdateDocumentRequestRequestTypeDef",
    "UpdateDocumentResultTypeDef",
    "UpdateMaintenanceWindowRequestRequestTypeDef",
    "UpdateMaintenanceWindowResultTypeDef",
    "UpdateMaintenanceWindowTargetRequestRequestTypeDef",
    "UpdateMaintenanceWindowTargetResultTypeDef",
    "UpdateMaintenanceWindowTaskRequestRequestTypeDef",
    "UpdateMaintenanceWindowTaskResultTypeDef",
    "UpdateManagedInstanceRoleRequestRequestTypeDef",
    "UpdateOpsItemRequestRequestTypeDef",
    "UpdateOpsMetadataRequestRequestTypeDef",
    "UpdateOpsMetadataResultTypeDef",
    "UpdatePatchBaselineRequestRequestTypeDef",
    "UpdatePatchBaselineResultTypeDef",
    "UpdateResourceDataSyncRequestRequestTypeDef",
    "UpdateServiceSettingRequestRequestTypeDef",
    "WaiterConfigTypeDef",
)

AccountSharingInfoTypeDef = TypedDict(
    "AccountSharingInfoTypeDef",
    {
        "AccountId": str,
        "SharedDocumentVersion": str,
    },
    total=False,
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

AddTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddTagsToResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
)

AssociateOpsItemRelatedItemRequestRequestTypeDef = TypedDict(
    "AssociateOpsItemRelatedItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "AssociationType": str,
        "ResourceType": str,
        "ResourceUri": str,
    },
)

AssociateOpsItemRelatedItemResponseTypeDef = TypedDict(
    "AssociateOpsItemRelatedItemResponseTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

AssociationExecutionFilterTypeDef = TypedDict(
    "AssociationExecutionFilterTypeDef",
    {
        "Key": AssociationExecutionFilterKeyType,
        "Value": str,
        "Type": AssociationFilterOperatorTypeType,
    },
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

AssociationExecutionTargetsFilterTypeDef = TypedDict(
    "AssociationExecutionTargetsFilterTypeDef",
    {
        "Key": AssociationExecutionTargetsFilterKeyType,
        "Value": str,
    },
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

AssociationFilterTypeDef = TypedDict(
    "AssociationFilterTypeDef",
    {
        "key": AssociationFilterKeyType,
        "value": str,
    },
)

AssociationOverviewTypeDef = TypedDict(
    "AssociationOverviewTypeDef",
    {
        "Status": str,
        "DetailedStatus": str,
        "AssociationStatusAggregatedCount": Dict[str, int],
    },
    total=False,
)

_RequiredAssociationStatusTypeDef = TypedDict(
    "_RequiredAssociationStatusTypeDef",
    {
        "Date": datetime,
        "Name": AssociationStatusNameType,
        "Message": str,
    },
)
_OptionalAssociationStatusTypeDef = TypedDict(
    "_OptionalAssociationStatusTypeDef",
    {
        "AdditionalInfo": str,
    },
    total=False,
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
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

AttachmentContentTypeDef = TypedDict(
    "AttachmentContentTypeDef",
    {
        "Name": str,
        "Size": int,
        "Hash": str,
        "HashType": Literal["Sha256"],
        "Url": str,
    },
    total=False,
)

AttachmentInformationTypeDef = TypedDict(
    "AttachmentInformationTypeDef",
    {
        "Name": str,
    },
    total=False,
)

AttachmentsSourceTypeDef = TypedDict(
    "AttachmentsSourceTypeDef",
    {
        "Key": AttachmentsSourceKeyType,
        "Values": List[str],
        "Name": str,
    },
    total=False,
)

AutomationExecutionFilterTypeDef = TypedDict(
    "AutomationExecutionFilterTypeDef",
    {
        "Key": AutomationExecutionFilterKeyType,
        "Values": List[str],
    },
)

AutomationExecutionMetadataTypeDef = TypedDict(
    "AutomationExecutionMetadataTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": AutomationExecutionStatusType,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": ExecutionModeType,
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
        "AutomationType": AutomationTypeType,
        "AutomationSubtype": Literal["ChangeRequest"],
        "ScheduledTime": datetime,
        "Runbooks": List["RunbookTypeDef"],
        "OpsItemId": str,
        "AssociationId": str,
        "ChangeRequestName": str,
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
        "AutomationExecutionStatus": AutomationExecutionStatusType,
        "StepExecutions": List["StepExecutionTypeDef"],
        "StepExecutionsTruncated": bool,
        "Parameters": Dict[str, List[str]],
        "Outputs": Dict[str, List[str]],
        "FailureMessage": str,
        "Mode": ExecutionModeType,
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
        "AutomationSubtype": Literal["ChangeRequest"],
        "ScheduledTime": datetime,
        "Runbooks": List["RunbookTypeDef"],
        "OpsItemId": str,
        "AssociationId": str,
        "ChangeRequestName": str,
    },
    total=False,
)

BaselineOverrideTypeDef = TypedDict(
    "BaselineOverrideTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "Sources": List["PatchSourceTypeDef"],
    },
    total=False,
)

_RequiredCancelCommandRequestRequestTypeDef = TypedDict(
    "_RequiredCancelCommandRequestRequestTypeDef",
    {
        "CommandId": str,
    },
)
_OptionalCancelCommandRequestRequestTypeDef = TypedDict(
    "_OptionalCancelCommandRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
    total=False,
)

class CancelCommandRequestRequestTypeDef(
    _RequiredCancelCommandRequestRequestTypeDef, _OptionalCancelCommandRequestRequestTypeDef
):
    pass

CancelMaintenanceWindowExecutionRequestRequestTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)

CancelMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionResultTypeDef",
    {
        "WindowExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudWatchOutputConfigTypeDef = TypedDict(
    "CloudWatchOutputConfigTypeDef",
    {
        "CloudWatchLogGroupName": str,
        "CloudWatchOutputEnabled": bool,
    },
    total=False,
)

CommandFilterTypeDef = TypedDict(
    "CommandFilterTypeDef",
    {
        "key": CommandFilterKeyType,
        "value": str,
    },
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
        "Status": CommandInvocationStatusType,
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
        "Status": CommandPluginStatusType,
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
        "Status": CommandStatusType,
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
    "_RequiredComplianceExecutionSummaryTypeDef",
    {
        "ExecutionTime": datetime,
    },
)
_OptionalComplianceExecutionSummaryTypeDef = TypedDict(
    "_OptionalComplianceExecutionSummaryTypeDef",
    {
        "ExecutionId": str,
        "ExecutionType": str,
    },
    total=False,
)

class ComplianceExecutionSummaryTypeDef(
    _RequiredComplianceExecutionSummaryTypeDef, _OptionalComplianceExecutionSummaryTypeDef
):
    pass

_RequiredComplianceItemEntryTypeDef = TypedDict(
    "_RequiredComplianceItemEntryTypeDef",
    {
        "Severity": ComplianceSeverityType,
        "Status": ComplianceStatusType,
    },
)
_OptionalComplianceItemEntryTypeDef = TypedDict(
    "_OptionalComplianceItemEntryTypeDef",
    {
        "Id": str,
        "Title": str,
        "Details": Dict[str, str],
    },
    total=False,
)

class ComplianceItemEntryTypeDef(
    _RequiredComplianceItemEntryTypeDef, _OptionalComplianceItemEntryTypeDef
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
        "Status": ComplianceStatusType,
        "Severity": ComplianceSeverityType,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "Details": Dict[str, str],
    },
    total=False,
)

ComplianceStringFilterTypeDef = TypedDict(
    "ComplianceStringFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": ComplianceQueryOperatorTypeType,
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
    {
        "CompliantCount": int,
        "SeveritySummary": "SeveritySummaryTypeDef",
    },
    total=False,
)

_RequiredCreateActivationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateActivationRequestRequestTypeDef",
    {
        "IamRole": str,
    },
)
_OptionalCreateActivationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateActivationRequestRequestTypeDef",
    {
        "Description": str,
        "DefaultInstanceName": str,
        "RegistrationLimit": int,
        "ExpirationDate": Union[datetime, str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateActivationRequestRequestTypeDef(
    _RequiredCreateActivationRequestRequestTypeDef, _OptionalCreateActivationRequestRequestTypeDef
):
    pass

CreateActivationResultTypeDef = TypedDict(
    "CreateActivationResultTypeDef",
    {
        "ActivationId": str,
        "ActivationCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "_RequiredCreateAssociationBatchRequestEntryTypeDef",
    {
        "Name": str,
    },
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
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

class CreateAssociationBatchRequestEntryTypeDef(
    _RequiredCreateAssociationBatchRequestEntryTypeDef,
    _OptionalCreateAssociationBatchRequestEntryTypeDef,
):
    pass

CreateAssociationBatchRequestRequestTypeDef = TypedDict(
    "CreateAssociationBatchRequestRequestTypeDef",
    {
        "Entries": List["CreateAssociationBatchRequestEntryTypeDef"],
    },
)

CreateAssociationBatchResultTypeDef = TypedDict(
    "CreateAssociationBatchResultTypeDef",
    {
        "Successful": List["AssociationDescriptionTypeDef"],
        "Failed": List["FailedCreateAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAssociationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAssociationRequestRequestTypeDef",
    {
        "DocumentVersion": str,
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "AssociationName": str,
        "AutomationTargetParameterName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

class CreateAssociationRequestRequestTypeDef(
    _RequiredCreateAssociationRequestRequestTypeDef, _OptionalCreateAssociationRequestRequestTypeDef
):
    pass

CreateAssociationResultTypeDef = TypedDict(
    "CreateAssociationResultTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDocumentRequestRequestTypeDef",
    {
        "Content": str,
        "Name": str,
    },
)
_OptionalCreateDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDocumentRequestRequestTypeDef",
    {
        "Requires": List["DocumentRequiresTypeDef"],
        "Attachments": List["AttachmentsSourceTypeDef"],
        "DisplayName": str,
        "VersionName": str,
        "DocumentType": DocumentTypeType,
        "DocumentFormat": DocumentFormatType,
        "TargetType": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDocumentRequestRequestTypeDef(
    _RequiredCreateDocumentRequestRequestTypeDef, _OptionalCreateDocumentRequestRequestTypeDef
):
    pass

CreateDocumentResultTypeDef = TypedDict(
    "CreateDocumentResultTypeDef",
    {
        "DocumentDescription": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMaintenanceWindowRequestRequestTypeDef",
    {
        "Name": str,
        "Schedule": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
    },
)
_OptionalCreateMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMaintenanceWindowRequestRequestTypeDef",
    {
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateMaintenanceWindowRequestRequestTypeDef(
    _RequiredCreateMaintenanceWindowRequestRequestTypeDef,
    _OptionalCreateMaintenanceWindowRequestRequestTypeDef,
):
    pass

CreateMaintenanceWindowResultTypeDef = TypedDict(
    "CreateMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOpsItemRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOpsItemRequestRequestTypeDef",
    {
        "Description": str,
        "Source": str,
        "Title": str,
    },
)
_OptionalCreateOpsItemRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOpsItemRequestRequestTypeDef",
    {
        "OpsItemType": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Notifications": List["OpsItemNotificationTypeDef"],
        "Priority": int,
        "RelatedOpsItems": List["RelatedOpsItemTypeDef"],
        "Tags": List["TagTypeDef"],
        "Category": str,
        "Severity": str,
        "ActualStartTime": Union[datetime, str],
        "ActualEndTime": Union[datetime, str],
        "PlannedStartTime": Union[datetime, str],
        "PlannedEndTime": Union[datetime, str],
    },
    total=False,
)

class CreateOpsItemRequestRequestTypeDef(
    _RequiredCreateOpsItemRequestRequestTypeDef, _OptionalCreateOpsItemRequestRequestTypeDef
):
    pass

CreateOpsItemResponseTypeDef = TypedDict(
    "CreateOpsItemResponseTypeDef",
    {
        "OpsItemId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateOpsMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredCreateOpsMetadataRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)
_OptionalCreateOpsMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalCreateOpsMetadataRequestRequestTypeDef",
    {
        "Metadata": Dict[str, "MetadataValueTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateOpsMetadataRequestRequestTypeDef(
    _RequiredCreateOpsMetadataRequestRequestTypeDef, _OptionalCreateOpsMetadataRequestRequestTypeDef
):
    pass

CreateOpsMetadataResultTypeDef = TypedDict(
    "CreateOpsMetadataResultTypeDef",
    {
        "OpsMetadataArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreatePatchBaselineRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePatchBaselineRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreatePatchBaselineRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePatchBaselineRequestRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePatchBaselineRequestRequestTypeDef(
    _RequiredCreatePatchBaselineRequestRequestTypeDef,
    _OptionalCreatePatchBaselineRequestRequestTypeDef,
):
    pass

CreatePatchBaselineResultTypeDef = TypedDict(
    "CreatePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateResourceDataSyncRequestRequestTypeDef = TypedDict(
    "_RequiredCreateResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
    },
)
_OptionalCreateResourceDataSyncRequestRequestTypeDef = TypedDict(
    "_OptionalCreateResourceDataSyncRequestRequestTypeDef",
    {
        "S3Destination": "ResourceDataSyncS3DestinationTypeDef",
        "SyncType": str,
        "SyncSource": "ResourceDataSyncSourceTypeDef",
    },
    total=False,
)

class CreateResourceDataSyncRequestRequestTypeDef(
    _RequiredCreateResourceDataSyncRequestRequestTypeDef,
    _OptionalCreateResourceDataSyncRequestRequestTypeDef,
):
    pass

DeleteActivationRequestRequestTypeDef = TypedDict(
    "DeleteActivationRequestRequestTypeDef",
    {
        "ActivationId": str,
    },
)

DeleteAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssociationRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
    },
    total=False,
)

_RequiredDeleteDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDocumentRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDocumentRequestRequestTypeDef",
    {
        "DocumentVersion": str,
        "VersionName": str,
        "Force": bool,
    },
    total=False,
)

class DeleteDocumentRequestRequestTypeDef(
    _RequiredDeleteDocumentRequestRequestTypeDef, _OptionalDeleteDocumentRequestRequestTypeDef
):
    pass

_RequiredDeleteInventoryRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteInventoryRequestRequestTypeDef",
    {
        "TypeName": str,
    },
)
_OptionalDeleteInventoryRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteInventoryRequestRequestTypeDef",
    {
        "SchemaDeleteOption": InventorySchemaDeleteOptionType,
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class DeleteInventoryRequestRequestTypeDef(
    _RequiredDeleteInventoryRequestRequestTypeDef, _OptionalDeleteInventoryRequestRequestTypeDef
):
    pass

DeleteInventoryResultTypeDef = TypedDict(
    "DeleteInventoryResultTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionSummary": "InventoryDeletionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "DeleteMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)

DeleteMaintenanceWindowResultTypeDef = TypedDict(
    "DeleteMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteOpsMetadataRequestRequestTypeDef = TypedDict(
    "DeleteOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
    },
)

DeleteParameterRequestRequestTypeDef = TypedDict(
    "DeleteParameterRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteParametersRequestRequestTypeDef = TypedDict(
    "DeleteParametersRequestRequestTypeDef",
    {
        "Names": List[str],
    },
)

DeleteParametersResultTypeDef = TypedDict(
    "DeleteParametersResultTypeDef",
    {
        "DeletedParameters": List[str],
        "InvalidParameters": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePatchBaselineRequestRequestTypeDef = TypedDict(
    "DeletePatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)

DeletePatchBaselineResultTypeDef = TypedDict(
    "DeletePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteResourceDataSyncRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
    },
)
_OptionalDeleteResourceDataSyncRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteResourceDataSyncRequestRequestTypeDef",
    {
        "SyncType": str,
    },
    total=False,
)

class DeleteResourceDataSyncRequestRequestTypeDef(
    _RequiredDeleteResourceDataSyncRequestRequestTypeDef,
    _OptionalDeleteResourceDataSyncRequestRequestTypeDef,
):
    pass

DeregisterManagedInstanceRequestRequestTypeDef = TypedDict(
    "DeregisterManagedInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)

DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
    },
)

DeregisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeregisterTargetFromMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterTargetFromMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
    },
)
_OptionalDeregisterTargetFromMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterTargetFromMaintenanceWindowRequestRequestTypeDef",
    {
        "Safe": bool,
    },
    total=False,
)

class DeregisterTargetFromMaintenanceWindowRequestRequestTypeDef(
    _RequiredDeregisterTargetFromMaintenanceWindowRequestRequestTypeDef,
    _OptionalDeregisterTargetFromMaintenanceWindowRequestRequestTypeDef,
):
    pass

DeregisterTargetFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)

DeregisterTaskFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeActivationsFilterTypeDef = TypedDict(
    "DescribeActivationsFilterTypeDef",
    {
        "FilterKey": DescribeActivationsFilterKeysType,
        "FilterValues": List[str],
    },
    total=False,
)

DescribeActivationsRequestRequestTypeDef = TypedDict(
    "DescribeActivationsRequestRequestTypeDef",
    {
        "Filters": List["DescribeActivationsFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeActivationsResultTypeDef = TypedDict(
    "DescribeActivationsResultTypeDef",
    {
        "ActivationList": List["ActivationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAssociationExecutionTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAssociationExecutionTargetsRequestRequestTypeDef",
    {
        "AssociationId": str,
        "ExecutionId": str,
    },
)
_OptionalDescribeAssociationExecutionTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAssociationExecutionTargetsRequestRequestTypeDef",
    {
        "Filters": List["AssociationExecutionTargetsFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeAssociationExecutionTargetsRequestRequestTypeDef(
    _RequiredDescribeAssociationExecutionTargetsRequestRequestTypeDef,
    _OptionalDescribeAssociationExecutionTargetsRequestRequestTypeDef,
):
    pass

DescribeAssociationExecutionTargetsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsResultTypeDef",
    {
        "AssociationExecutionTargets": List["AssociationExecutionTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAssociationExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAssociationExecutionsRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDescribeAssociationExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAssociationExecutionsRequestRequestTypeDef",
    {
        "Filters": List["AssociationExecutionFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeAssociationExecutionsRequestRequestTypeDef(
    _RequiredDescribeAssociationExecutionsRequestRequestTypeDef,
    _OptionalDescribeAssociationExecutionsRequestRequestTypeDef,
):
    pass

DescribeAssociationExecutionsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionsResultTypeDef",
    {
        "AssociationExecutions": List["AssociationExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAssociationRequestRequestTypeDef = TypedDict(
    "DescribeAssociationRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
    },
    total=False,
)

DescribeAssociationResultTypeDef = TypedDict(
    "DescribeAssociationResultTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAutomationExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAutomationExecutionsRequestRequestTypeDef",
    {
        "Filters": List["AutomationExecutionFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAutomationExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationExecutionsResultTypeDef",
    {
        "AutomationExecutionMetadataList": List["AutomationExecutionMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeAutomationStepExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAutomationStepExecutionsRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
    },
)
_OptionalDescribeAutomationStepExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAutomationStepExecutionsRequestRequestTypeDef",
    {
        "Filters": List["StepExecutionFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
        "ReverseOrder": bool,
    },
    total=False,
)

class DescribeAutomationStepExecutionsRequestRequestTypeDef(
    _RequiredDescribeAutomationStepExecutionsRequestRequestTypeDef,
    _OptionalDescribeAutomationStepExecutionsRequestRequestTypeDef,
):
    pass

DescribeAutomationStepExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsResultTypeDef",
    {
        "StepExecutions": List["StepExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailablePatchesRequestRequestTypeDef = TypedDict(
    "DescribeAvailablePatchesRequestRequestTypeDef",
    {
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeAvailablePatchesResultTypeDef = TypedDict(
    "DescribeAvailablePatchesResultTypeDef",
    {
        "Patches": List["PatchTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDocumentPermissionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDocumentPermissionRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionType": Literal["Share"],
    },
)
_OptionalDescribeDocumentPermissionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDocumentPermissionRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeDocumentPermissionRequestRequestTypeDef(
    _RequiredDescribeDocumentPermissionRequestRequestTypeDef,
    _OptionalDescribeDocumentPermissionRequestRequestTypeDef,
):
    pass

DescribeDocumentPermissionResponseTypeDef = TypedDict(
    "DescribeDocumentPermissionResponseTypeDef",
    {
        "AccountIds": List[str],
        "AccountSharingInfoList": List["AccountSharingInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDocumentRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDocumentRequestRequestTypeDef",
    {
        "DocumentVersion": str,
        "VersionName": str,
    },
    total=False,
)

class DescribeDocumentRequestRequestTypeDef(
    _RequiredDescribeDocumentRequestRequestTypeDef, _OptionalDescribeDocumentRequestRequestTypeDef
):
    pass

DescribeDocumentResultTypeDef = TypedDict(
    "DescribeDocumentResultTypeDef",
    {
        "Document": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEffectiveInstanceAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEffectiveInstanceAssociationsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDescribeEffectiveInstanceAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEffectiveInstanceAssociationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeEffectiveInstanceAssociationsRequestRequestTypeDef(
    _RequiredDescribeEffectiveInstanceAssociationsRequestRequestTypeDef,
    _OptionalDescribeEffectiveInstanceAssociationsRequestRequestTypeDef,
):
    pass

DescribeEffectiveInstanceAssociationsResultTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    {
        "Associations": List["InstanceAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)
_OptionalDescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef(
    _RequiredDescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef,
    _OptionalDescribeEffectivePatchesForPatchBaselineRequestRequestTypeDef,
):
    pass

DescribeEffectivePatchesForPatchBaselineResultTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    {
        "EffectivePatches": List["EffectivePatchTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstanceAssociationsStatusRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeInstanceAssociationsStatusRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDescribeInstanceAssociationsStatusRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeInstanceAssociationsStatusRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeInstanceAssociationsStatusRequestRequestTypeDef(
    _RequiredDescribeInstanceAssociationsStatusRequestRequestTypeDef,
    _OptionalDescribeInstanceAssociationsStatusRequestRequestTypeDef,
):
    pass

DescribeInstanceAssociationsStatusResultTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusResultTypeDef",
    {
        "InstanceAssociationStatusInfos": List["InstanceAssociationStatusInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceInformationRequestRequestTypeDef = TypedDict(
    "DescribeInstanceInformationRequestRequestTypeDef",
    {
        "InstanceInformationFilterList": List["InstanceInformationFilterTypeDef"],
        "Filters": List["InstanceInformationStringFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceInformationResultTypeDef = TypedDict(
    "DescribeInstanceInformationResultTypeDef",
    {
        "InstanceInformationList": List["InstanceInformationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef",
    {
        "PatchGroup": str,
    },
)
_OptionalDescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef",
    {
        "Filters": List["InstancePatchStateFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef(
    _RequiredDescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef,
    _OptionalDescribeInstancePatchStatesForPatchGroupRequestRequestTypeDef,
):
    pass

DescribeInstancePatchStatesForPatchGroupResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    {
        "InstancePatchStates": List["InstancePatchStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstancePatchStatesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeInstancePatchStatesRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalDescribeInstancePatchStatesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeInstancePatchStatesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeInstancePatchStatesRequestRequestTypeDef(
    _RequiredDescribeInstancePatchStatesRequestRequestTypeDef,
    _OptionalDescribeInstancePatchStatesRequestRequestTypeDef,
):
    pass

DescribeInstancePatchStatesResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesResultTypeDef",
    {
        "InstancePatchStates": List["InstancePatchStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstancePatchesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeInstancePatchesRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDescribeInstancePatchesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeInstancePatchesRequestRequestTypeDef",
    {
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeInstancePatchesRequestRequestTypeDef(
    _RequiredDescribeInstancePatchesRequestRequestTypeDef,
    _OptionalDescribeInstancePatchesRequestRequestTypeDef,
):
    pass

DescribeInstancePatchesResultTypeDef = TypedDict(
    "DescribeInstancePatchesResultTypeDef",
    {
        "Patches": List["PatchComplianceDataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInventoryDeletionsRequestRequestTypeDef = TypedDict(
    "DescribeInventoryDeletionsRequestRequestTypeDef",
    {
        "DeletionId": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeInventoryDeletionsResultTypeDef = TypedDict(
    "DescribeInventoryDeletionsResultTypeDef",
    {
        "InventoryDeletions": List["InventoryDeletionStatusItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
    },
)
_OptionalDescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef(
    _RequiredDescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef,
    _OptionalDescribeMaintenanceWindowExecutionTaskInvocationsRequestRequestTypeDef,
):
    pass

DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)
_OptionalDescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef(
    _RequiredDescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef,
    _OptionalDescribeMaintenanceWindowExecutionTasksRequestRequestTypeDef,
):
    pass

DescribeMaintenanceWindowExecutionTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    {
        "WindowExecutionTaskIdentities": List["MaintenanceWindowExecutionTaskIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowExecutionsRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)
_OptionalDescribeMaintenanceWindowExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowExecutionsRequestRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeMaintenanceWindowExecutionsRequestRequestTypeDef(
    _RequiredDescribeMaintenanceWindowExecutionsRequestRequestTypeDef,
    _OptionalDescribeMaintenanceWindowExecutionsRequestRequestTypeDef,
):
    pass

DescribeMaintenanceWindowExecutionsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    {
        "WindowExecutions": List["MaintenanceWindowExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowScheduleRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleRequestRequestTypeDef",
    {
        "WindowId": str,
        "Targets": List["TargetTypeDef"],
        "ResourceType": MaintenanceWindowResourceTypeType,
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMaintenanceWindowScheduleResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    {
        "ScheduledWindowExecutions": List["ScheduledWindowExecutionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowTargetsRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)
_OptionalDescribeMaintenanceWindowTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowTargetsRequestRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeMaintenanceWindowTargetsRequestRequestTypeDef(
    _RequiredDescribeMaintenanceWindowTargetsRequestRequestTypeDef,
    _OptionalDescribeMaintenanceWindowTargetsRequestRequestTypeDef,
):
    pass

DescribeMaintenanceWindowTargetsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    {
        "Targets": List["MaintenanceWindowTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowTasksRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowTasksRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)
_OptionalDescribeMaintenanceWindowTasksRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowTasksRequestRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeMaintenanceWindowTasksRequestRequestTypeDef(
    _RequiredDescribeMaintenanceWindowTasksRequestRequestTypeDef,
    _OptionalDescribeMaintenanceWindowTasksRequestRequestTypeDef,
):
    pass

DescribeMaintenanceWindowTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksResultTypeDef",
    {
        "Tasks": List["MaintenanceWindowTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMaintenanceWindowsForTargetRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeMaintenanceWindowsForTargetRequestRequestTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "ResourceType": MaintenanceWindowResourceTypeType,
    },
)
_OptionalDescribeMaintenanceWindowsForTargetRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeMaintenanceWindowsForTargetRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeMaintenanceWindowsForTargetRequestRequestTypeDef(
    _RequiredDescribeMaintenanceWindowsForTargetRequestRequestTypeDef,
    _OptionalDescribeMaintenanceWindowsForTargetRequestRequestTypeDef,
):
    pass

DescribeMaintenanceWindowsForTargetResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    {
        "WindowIdentities": List["MaintenanceWindowIdentityForTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceWindowsRequestRequestTypeDef = TypedDict(
    "DescribeMaintenanceWindowsRequestRequestTypeDef",
    {
        "Filters": List["MaintenanceWindowFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeMaintenanceWindowsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsResultTypeDef",
    {
        "WindowIdentities": List["MaintenanceWindowIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOpsItemsRequestRequestTypeDef = TypedDict(
    "DescribeOpsItemsRequestRequestTypeDef",
    {
        "OpsItemFilters": List["OpsItemFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeOpsItemsResponseTypeDef = TypedDict(
    "DescribeOpsItemsResponseTypeDef",
    {
        "NextToken": str,
        "OpsItemSummaries": List["OpsItemSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeParametersRequestRequestTypeDef = TypedDict(
    "DescribeParametersRequestRequestTypeDef",
    {
        "Filters": List["ParametersFilterTypeDef"],
        "ParameterFilters": List["ParameterStringFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeParametersResultTypeDef = TypedDict(
    "DescribeParametersResultTypeDef",
    {
        "Parameters": List["ParameterMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchBaselinesRequestRequestTypeDef = TypedDict(
    "DescribePatchBaselinesRequestRequestTypeDef",
    {
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribePatchBaselinesResultTypeDef = TypedDict(
    "DescribePatchBaselinesResultTypeDef",
    {
        "BaselineIdentities": List["PatchBaselineIdentityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchGroupStateRequestRequestTypeDef = TypedDict(
    "DescribePatchGroupStateRequestRequestTypeDef",
    {
        "PatchGroup": str,
    },
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
        "InstancesWithCriticalNonCompliantPatches": int,
        "InstancesWithSecurityNonCompliantPatches": int,
        "InstancesWithOtherNonCompliantPatches": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePatchGroupsRequestRequestTypeDef = TypedDict(
    "DescribePatchGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "Filters": List["PatchOrchestratorFilterTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribePatchGroupsResultTypeDef = TypedDict(
    "DescribePatchGroupsResultTypeDef",
    {
        "Mappings": List["PatchGroupPatchBaselineMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePatchPropertiesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePatchPropertiesRequestRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
        "Property": PatchPropertyType,
    },
)
_OptionalDescribePatchPropertiesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePatchPropertiesRequestRequestTypeDef",
    {
        "PatchSet": PatchSetType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribePatchPropertiesRequestRequestTypeDef(
    _RequiredDescribePatchPropertiesRequestRequestTypeDef,
    _OptionalDescribePatchPropertiesRequestRequestTypeDef,
):
    pass

DescribePatchPropertiesResultTypeDef = TypedDict(
    "DescribePatchPropertiesResultTypeDef",
    {
        "Properties": List[Dict[str, str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSessionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSessionsRequestRequestTypeDef",
    {
        "State": SessionStateType,
    },
)
_OptionalDescribeSessionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSessionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["SessionFilterTypeDef"],
    },
    total=False,
)

class DescribeSessionsRequestRequestTypeDef(
    _RequiredDescribeSessionsRequestRequestTypeDef, _OptionalDescribeSessionsRequestRequestTypeDef
):
    pass

DescribeSessionsResponseTypeDef = TypedDict(
    "DescribeSessionsResponseTypeDef",
    {
        "Sessions": List["SessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateOpsItemRelatedItemRequestRequestTypeDef = TypedDict(
    "DisassociateOpsItemRelatedItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "AssociationId": str,
    },
)

DocumentDefaultVersionDescriptionTypeDef = TypedDict(
    "DocumentDefaultVersionDescriptionTypeDef",
    {
        "Name": str,
        "DefaultVersion": str,
        "DefaultVersionName": str,
    },
    total=False,
)

DocumentDescriptionTypeDef = TypedDict(
    "DocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": DocumentHashTypeType,
        "Name": str,
        "DisplayName": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": DocumentStatusType,
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List["DocumentParameterTypeDef"],
        "PlatformTypes": List[PlatformTypeType],
        "DocumentType": DocumentTypeType,
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": DocumentFormatType,
        "TargetType": str,
        "Tags": List["TagTypeDef"],
        "AttachmentsInformation": List["AttachmentInformationTypeDef"],
        "Requires": List["DocumentRequiresTypeDef"],
        "Author": str,
        "ReviewInformation": List["ReviewInformationTypeDef"],
        "ApprovedVersion": str,
        "PendingReviewVersion": str,
        "ReviewStatus": ReviewStatusType,
    },
    total=False,
)

DocumentFilterTypeDef = TypedDict(
    "DocumentFilterTypeDef",
    {
        "key": DocumentFilterKeyType,
        "value": str,
    },
)

DocumentIdentifierTypeDef = TypedDict(
    "DocumentIdentifierTypeDef",
    {
        "Name": str,
        "CreatedDate": datetime,
        "DisplayName": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[PlatformTypeType],
        "DocumentVersion": str,
        "DocumentType": DocumentTypeType,
        "SchemaVersion": str,
        "DocumentFormat": DocumentFormatType,
        "TargetType": str,
        "Tags": List["TagTypeDef"],
        "Requires": List["DocumentRequiresTypeDef"],
        "ReviewStatus": ReviewStatusType,
        "Author": str,
    },
    total=False,
)

DocumentKeyValuesFilterTypeDef = TypedDict(
    "DocumentKeyValuesFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

DocumentMetadataResponseInfoTypeDef = TypedDict(
    "DocumentMetadataResponseInfoTypeDef",
    {
        "ReviewerResponse": List["DocumentReviewerResponseSourceTypeDef"],
    },
    total=False,
)

DocumentParameterTypeDef = TypedDict(
    "DocumentParameterTypeDef",
    {
        "Name": str,
        "Type": DocumentParameterTypeType,
        "Description": str,
        "DefaultValue": str,
    },
    total=False,
)

_RequiredDocumentRequiresTypeDef = TypedDict(
    "_RequiredDocumentRequiresTypeDef",
    {
        "Name": str,
    },
)
_OptionalDocumentRequiresTypeDef = TypedDict(
    "_OptionalDocumentRequiresTypeDef",
    {
        "Version": str,
    },
    total=False,
)

class DocumentRequiresTypeDef(_RequiredDocumentRequiresTypeDef, _OptionalDocumentRequiresTypeDef):
    pass

DocumentReviewCommentSourceTypeDef = TypedDict(
    "DocumentReviewCommentSourceTypeDef",
    {
        "Type": Literal["Comment"],
        "Content": str,
    },
    total=False,
)

DocumentReviewerResponseSourceTypeDef = TypedDict(
    "DocumentReviewerResponseSourceTypeDef",
    {
        "CreateTime": datetime,
        "UpdatedTime": datetime,
        "ReviewStatus": ReviewStatusType,
        "Comment": List["DocumentReviewCommentSourceTypeDef"],
        "Reviewer": str,
    },
    total=False,
)

_RequiredDocumentReviewsTypeDef = TypedDict(
    "_RequiredDocumentReviewsTypeDef",
    {
        "Action": DocumentReviewActionType,
    },
)
_OptionalDocumentReviewsTypeDef = TypedDict(
    "_OptionalDocumentReviewsTypeDef",
    {
        "Comment": List["DocumentReviewCommentSourceTypeDef"],
    },
    total=False,
)

class DocumentReviewsTypeDef(_RequiredDocumentReviewsTypeDef, _OptionalDocumentReviewsTypeDef):
    pass

DocumentVersionInfoTypeDef = TypedDict(
    "DocumentVersionInfoTypeDef",
    {
        "Name": str,
        "DisplayName": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": DocumentFormatType,
        "Status": DocumentStatusType,
        "StatusInformation": str,
        "ReviewStatus": ReviewStatusType,
    },
    total=False,
)

EffectivePatchTypeDef = TypedDict(
    "EffectivePatchTypeDef",
    {
        "Patch": "PatchTypeDef",
        "PatchStatus": "PatchStatusTypeDef",
    },
    total=False,
)

FailedCreateAssociationTypeDef = TypedDict(
    "FailedCreateAssociationTypeDef",
    {
        "Entry": "CreateAssociationBatchRequestEntryTypeDef",
        "Message": str,
        "Fault": FaultType,
    },
    total=False,
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {
        "FailureStage": str,
        "FailureType": str,
        "Details": Dict[str, List[str]],
    },
    total=False,
)

GetAutomationExecutionRequestRequestTypeDef = TypedDict(
    "GetAutomationExecutionRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
    },
)

GetAutomationExecutionResultTypeDef = TypedDict(
    "GetAutomationExecutionResultTypeDef",
    {
        "AutomationExecution": "AutomationExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCalendarStateRequestRequestTypeDef = TypedDict(
    "_RequiredGetCalendarStateRequestRequestTypeDef",
    {
        "CalendarNames": List[str],
    },
)
_OptionalGetCalendarStateRequestRequestTypeDef = TypedDict(
    "_OptionalGetCalendarStateRequestRequestTypeDef",
    {
        "AtTime": str,
    },
    total=False,
)

class GetCalendarStateRequestRequestTypeDef(
    _RequiredGetCalendarStateRequestRequestTypeDef, _OptionalGetCalendarStateRequestRequestTypeDef
):
    pass

GetCalendarStateResponseTypeDef = TypedDict(
    "GetCalendarStateResponseTypeDef",
    {
        "State": CalendarStateType,
        "AtTime": str,
        "NextTransitionTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCommandInvocationRequestRequestTypeDef = TypedDict(
    "_RequiredGetCommandInvocationRequestRequestTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
    },
)
_OptionalGetCommandInvocationRequestRequestTypeDef = TypedDict(
    "_OptionalGetCommandInvocationRequestRequestTypeDef",
    {
        "PluginName": str,
    },
    total=False,
)

class GetCommandInvocationRequestRequestTypeDef(
    _RequiredGetCommandInvocationRequestRequestTypeDef,
    _OptionalGetCommandInvocationRequestRequestTypeDef,
):
    pass

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
        "Status": CommandInvocationStatusType,
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionStatusRequestRequestTypeDef = TypedDict(
    "GetConnectionStatusRequestRequestTypeDef",
    {
        "Target": str,
    },
)

GetConnectionStatusResponseTypeDef = TypedDict(
    "GetConnectionStatusResponseTypeDef",
    {
        "Target": str,
        "Status": ConnectionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDefaultPatchBaselineRequestRequestTypeDef = TypedDict(
    "GetDefaultPatchBaselineRequestRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
    },
    total=False,
)

GetDefaultPatchBaselineResultTypeDef = TypedDict(
    "GetDefaultPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "OperatingSystem": OperatingSystemType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDeployablePatchSnapshotForInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredGetDeployablePatchSnapshotForInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": str,
    },
)
_OptionalGetDeployablePatchSnapshotForInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalGetDeployablePatchSnapshotForInstanceRequestRequestTypeDef",
    {
        "BaselineOverride": "BaselineOverrideTypeDef",
    },
    total=False,
)

class GetDeployablePatchSnapshotForInstanceRequestRequestTypeDef(
    _RequiredGetDeployablePatchSnapshotForInstanceRequestRequestTypeDef,
    _OptionalGetDeployablePatchSnapshotForInstanceRequestRequestTypeDef,
):
    pass

GetDeployablePatchSnapshotForInstanceResultTypeDef = TypedDict(
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    {
        "InstanceId": str,
        "SnapshotId": str,
        "SnapshotDownloadUrl": str,
        "Product": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredGetDocumentRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalGetDocumentRequestRequestTypeDef",
    {
        "VersionName": str,
        "DocumentVersion": str,
        "DocumentFormat": DocumentFormatType,
    },
    total=False,
)

class GetDocumentRequestRequestTypeDef(
    _RequiredGetDocumentRequestRequestTypeDef, _OptionalGetDocumentRequestRequestTypeDef
):
    pass

GetDocumentResultTypeDef = TypedDict(
    "GetDocumentResultTypeDef",
    {
        "Name": str,
        "CreatedDate": datetime,
        "DisplayName": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": DocumentStatusType,
        "StatusInformation": str,
        "Content": str,
        "DocumentType": DocumentTypeType,
        "DocumentFormat": DocumentFormatType,
        "Requires": List["DocumentRequiresTypeDef"],
        "AttachmentsContent": List["AttachmentContentTypeDef"],
        "ReviewStatus": ReviewStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInventoryRequestRequestTypeDef = TypedDict(
    "GetInventoryRequestRequestTypeDef",
    {
        "Filters": List["InventoryFilterTypeDef"],
        "Aggregators": List["InventoryAggregatorTypeDef"],
        "ResultAttributes": List["ResultAttributeTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetInventoryResultTypeDef = TypedDict(
    "GetInventoryResultTypeDef",
    {
        "Entities": List["InventoryResultEntityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInventorySchemaRequestRequestTypeDef = TypedDict(
    "GetInventorySchemaRequestRequestTypeDef",
    {
        "TypeName": str,
        "NextToken": str,
        "MaxResults": int,
        "Aggregator": bool,
        "SubType": bool,
    },
    total=False,
)

GetInventorySchemaResultTypeDef = TypedDict(
    "GetInventorySchemaResultTypeDef",
    {
        "Schemas": List["InventoryItemSchemaTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
    },
)

GetMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
        "InvocationId": str,
    },
)

GetMaintenanceWindowExecutionTaskInvocationResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "Parameters": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowExecutionTaskRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskRequestRequestTypeDef",
    {
        "WindowExecutionId": str,
        "TaskId": str,
    },
)

GetMaintenanceWindowExecutionTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": MaintenanceWindowTaskTypeType,
        "TaskParameters": List[Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
    },
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMaintenanceWindowTaskRequestRequestTypeDef = TypedDict(
    "GetMaintenanceWindowTaskRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)

GetMaintenanceWindowTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpsItemRequestRequestTypeDef = TypedDict(
    "GetOpsItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
    },
)

GetOpsItemResponseTypeDef = TypedDict(
    "GetOpsItemResponseTypeDef",
    {
        "OpsItem": "OpsItemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOpsMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredGetOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
    },
)
_OptionalGetOpsMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalGetOpsMetadataRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetOpsMetadataRequestRequestTypeDef(
    _RequiredGetOpsMetadataRequestRequestTypeDef, _OptionalGetOpsMetadataRequestRequestTypeDef
):
    pass

GetOpsMetadataResultTypeDef = TypedDict(
    "GetOpsMetadataResultTypeDef",
    {
        "ResourceId": str,
        "Metadata": Dict[str, "MetadataValueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpsSummaryRequestRequestTypeDef = TypedDict(
    "GetOpsSummaryRequestRequestTypeDef",
    {
        "SyncName": str,
        "Filters": List["OpsFilterTypeDef"],
        "Aggregators": List["OpsAggregatorTypeDef"],
        "ResultAttributes": List["OpsResultAttributeTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

GetOpsSummaryResultTypeDef = TypedDict(
    "GetOpsSummaryResultTypeDef",
    {
        "Entities": List["OpsEntityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetParameterHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetParameterHistoryRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetParameterHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetParameterHistoryRequestRequestTypeDef",
    {
        "WithDecryption": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetParameterHistoryRequestRequestTypeDef(
    _RequiredGetParameterHistoryRequestRequestTypeDef,
    _OptionalGetParameterHistoryRequestRequestTypeDef,
):
    pass

GetParameterHistoryResultTypeDef = TypedDict(
    "GetParameterHistoryResultTypeDef",
    {
        "Parameters": List["ParameterHistoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetParameterRequestRequestTypeDef = TypedDict(
    "_RequiredGetParameterRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetParameterRequestRequestTypeDef = TypedDict(
    "_OptionalGetParameterRequestRequestTypeDef",
    {
        "WithDecryption": bool,
    },
    total=False,
)

class GetParameterRequestRequestTypeDef(
    _RequiredGetParameterRequestRequestTypeDef, _OptionalGetParameterRequestRequestTypeDef
):
    pass

GetParameterResultTypeDef = TypedDict(
    "GetParameterResultTypeDef",
    {
        "Parameter": "ParameterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetParametersByPathRequestRequestTypeDef = TypedDict(
    "_RequiredGetParametersByPathRequestRequestTypeDef",
    {
        "Path": str,
    },
)
_OptionalGetParametersByPathRequestRequestTypeDef = TypedDict(
    "_OptionalGetParametersByPathRequestRequestTypeDef",
    {
        "Recursive": bool,
        "ParameterFilters": List["ParameterStringFilterTypeDef"],
        "WithDecryption": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetParametersByPathRequestRequestTypeDef(
    _RequiredGetParametersByPathRequestRequestTypeDef,
    _OptionalGetParametersByPathRequestRequestTypeDef,
):
    pass

GetParametersByPathResultTypeDef = TypedDict(
    "GetParametersByPathResultTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetParametersRequestRequestTypeDef = TypedDict(
    "_RequiredGetParametersRequestRequestTypeDef",
    {
        "Names": List[str],
    },
)
_OptionalGetParametersRequestRequestTypeDef = TypedDict(
    "_OptionalGetParametersRequestRequestTypeDef",
    {
        "WithDecryption": bool,
    },
    total=False,
)

class GetParametersRequestRequestTypeDef(
    _RequiredGetParametersRequestRequestTypeDef, _OptionalGetParametersRequestRequestTypeDef
):
    pass

GetParametersResultTypeDef = TypedDict(
    "GetParametersResultTypeDef",
    {
        "Parameters": List["ParameterTypeDef"],
        "InvalidParameters": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "_RequiredGetPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "PatchGroup": str,
    },
)
_OptionalGetPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "_OptionalGetPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "OperatingSystem": OperatingSystemType,
    },
    total=False,
)

class GetPatchBaselineForPatchGroupRequestRequestTypeDef(
    _RequiredGetPatchBaselineForPatchGroupRequestRequestTypeDef,
    _OptionalGetPatchBaselineForPatchGroupRequestRequestTypeDef,
):
    pass

GetPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "GetPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "OperatingSystem": OperatingSystemType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPatchBaselineRequestRequestTypeDef = TypedDict(
    "GetPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)

GetPatchBaselineResultTypeDef = TypedDict(
    "GetPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceSettingRequestRequestTypeDef = TypedDict(
    "GetServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
    },
)

GetServiceSettingResultTypeDef = TypedDict(
    "GetServiceSettingResultTypeDef",
    {
        "ServiceSetting": "ServiceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAggregatedAssociationOverviewTypeDef = TypedDict(
    "InstanceAggregatedAssociationOverviewTypeDef",
    {
        "DetailedStatus": str,
        "InstanceAssociationStatusAggregatedCount": Dict[str, int],
    },
    total=False,
)

InstanceAssociationOutputLocationTypeDef = TypedDict(
    "InstanceAssociationOutputLocationTypeDef",
    {
        "S3Location": "S3OutputLocationTypeDef",
    },
    total=False,
)

InstanceAssociationOutputUrlTypeDef = TypedDict(
    "InstanceAssociationOutputUrlTypeDef",
    {
        "S3OutputUrl": "S3OutputUrlTypeDef",
    },
    total=False,
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
    {
        "AssociationId": str,
        "InstanceId": str,
        "Content": str,
        "AssociationVersion": str,
    },
    total=False,
)

InstanceInformationFilterTypeDef = TypedDict(
    "InstanceInformationFilterTypeDef",
    {
        "key": InstanceInformationFilterKeyType,
        "valueSet": List[str],
    },
)

InstanceInformationStringFilterTypeDef = TypedDict(
    "InstanceInformationStringFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)

InstanceInformationTypeDef = TypedDict(
    "InstanceInformationTypeDef",
    {
        "InstanceId": str,
        "PingStatus": PingStatusType,
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": PlatformTypeType,
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": ResourceTypeType,
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

InstancePatchStateFilterTypeDef = TypedDict(
    "InstancePatchStateFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
        "Type": InstancePatchStateOperatorTypeType,
    },
)

_RequiredInstancePatchStateTypeDef = TypedDict(
    "_RequiredInstancePatchStateTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": PatchOperationTypeType,
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
        "RebootOption": RebootOptionType,
        "CriticalNonCompliantCount": int,
        "SecurityNonCompliantCount": int,
        "OtherNonCompliantCount": int,
    },
    total=False,
)

class InstancePatchStateTypeDef(
    _RequiredInstancePatchStateTypeDef, _OptionalInstancePatchStateTypeDef
):
    pass

InventoryAggregatorTypeDef = TypedDict(
    "InventoryAggregatorTypeDef",
    {
        "Expression": str,
        "Aggregators": List[Dict[str, Any]],
        "Groups": List["InventoryGroupTypeDef"],
    },
    total=False,
)

InventoryDeletionStatusItemTypeDef = TypedDict(
    "InventoryDeletionStatusItemTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": InventoryDeletionStatusType,
        "LastStatusMessage": str,
        "DeletionSummary": "InventoryDeletionSummaryTypeDef",
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)

InventoryDeletionSummaryItemTypeDef = TypedDict(
    "InventoryDeletionSummaryItemTypeDef",
    {
        "Version": str,
        "Count": int,
        "RemainingCount": int,
    },
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
    "_RequiredInventoryFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef",
    {
        "Type": InventoryQueryOperatorTypeType,
    },
    total=False,
)

class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass

InventoryGroupTypeDef = TypedDict(
    "InventoryGroupTypeDef",
    {
        "Name": str,
        "Filters": List["InventoryFilterTypeDef"],
    },
)

InventoryItemAttributeTypeDef = TypedDict(
    "InventoryItemAttributeTypeDef",
    {
        "Name": str,
        "DataType": InventoryAttributeDataTypeType,
    },
)

_RequiredInventoryItemSchemaTypeDef = TypedDict(
    "_RequiredInventoryItemSchemaTypeDef",
    {
        "TypeName": str,
        "Attributes": List["InventoryItemAttributeTypeDef"],
    },
)
_OptionalInventoryItemSchemaTypeDef = TypedDict(
    "_OptionalInventoryItemSchemaTypeDef",
    {
        "Version": str,
        "DisplayName": str,
    },
    total=False,
)

class InventoryItemSchemaTypeDef(
    _RequiredInventoryItemSchemaTypeDef, _OptionalInventoryItemSchemaTypeDef
):
    pass

_RequiredInventoryItemTypeDef = TypedDict(
    "_RequiredInventoryItemTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "CaptureTime": str,
    },
)
_OptionalInventoryItemTypeDef = TypedDict(
    "_OptionalInventoryItemTypeDef",
    {
        "ContentHash": str,
        "Content": List[Dict[str, str]],
        "Context": Dict[str, str],
    },
    total=False,
)

class InventoryItemTypeDef(_RequiredInventoryItemTypeDef, _OptionalInventoryItemTypeDef):
    pass

InventoryResultEntityTypeDef = TypedDict(
    "InventoryResultEntityTypeDef",
    {
        "Id": str,
        "Data": Dict[str, "InventoryResultItemTypeDef"],
    },
    total=False,
)

_RequiredInventoryResultItemTypeDef = TypedDict(
    "_RequiredInventoryResultItemTypeDef",
    {
        "TypeName": str,
        "SchemaVersion": str,
        "Content": List[Dict[str, str]],
    },
)
_OptionalInventoryResultItemTypeDef = TypedDict(
    "_OptionalInventoryResultItemTypeDef",
    {
        "CaptureTime": str,
        "ContentHash": str,
    },
    total=False,
)

class InventoryResultItemTypeDef(
    _RequiredInventoryResultItemTypeDef, _OptionalInventoryResultItemTypeDef
):
    pass

_RequiredLabelParameterVersionRequestRequestTypeDef = TypedDict(
    "_RequiredLabelParameterVersionRequestRequestTypeDef",
    {
        "Name": str,
        "Labels": List[str],
    },
)
_OptionalLabelParameterVersionRequestRequestTypeDef = TypedDict(
    "_OptionalLabelParameterVersionRequestRequestTypeDef",
    {
        "ParameterVersion": int,
    },
    total=False,
)

class LabelParameterVersionRequestRequestTypeDef(
    _RequiredLabelParameterVersionRequestRequestTypeDef,
    _OptionalLabelParameterVersionRequestRequestTypeDef,
):
    pass

LabelParameterVersionResultTypeDef = TypedDict(
    "LabelParameterVersionResultTypeDef",
    {
        "InvalidLabels": List[str],
        "ParameterVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociationVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociationVersionsRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalListAssociationVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociationVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListAssociationVersionsRequestRequestTypeDef(
    _RequiredListAssociationVersionsRequestRequestTypeDef,
    _OptionalListAssociationVersionsRequestRequestTypeDef,
):
    pass

ListAssociationVersionsResultTypeDef = TypedDict(
    "ListAssociationVersionsResultTypeDef",
    {
        "AssociationVersions": List["AssociationVersionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociationsRequestRequestTypeDef = TypedDict(
    "ListAssociationsRequestRequestTypeDef",
    {
        "AssociationFilterList": List["AssociationFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListAssociationsResultTypeDef = TypedDict(
    "ListAssociationsResultTypeDef",
    {
        "Associations": List["AssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCommandInvocationsRequestRequestTypeDef = TypedDict(
    "ListCommandInvocationsRequestRequestTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["CommandFilterTypeDef"],
        "Details": bool,
    },
    total=False,
)

ListCommandInvocationsResultTypeDef = TypedDict(
    "ListCommandInvocationsResultTypeDef",
    {
        "CommandInvocations": List["CommandInvocationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCommandsRequestRequestTypeDef = TypedDict(
    "ListCommandsRequestRequestTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["CommandFilterTypeDef"],
    },
    total=False,
)

ListCommandsResultTypeDef = TypedDict(
    "ListCommandsResultTypeDef",
    {
        "Commands": List["CommandTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComplianceItemsRequestRequestTypeDef = TypedDict(
    "ListComplianceItemsRequestRequestTypeDef",
    {
        "Filters": List["ComplianceStringFilterTypeDef"],
        "ResourceIds": List[str],
        "ResourceTypes": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListComplianceItemsResultTypeDef = TypedDict(
    "ListComplianceItemsResultTypeDef",
    {
        "ComplianceItems": List["ComplianceItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComplianceSummariesRequestRequestTypeDef = TypedDict(
    "ListComplianceSummariesRequestRequestTypeDef",
    {
        "Filters": List["ComplianceStringFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListComplianceSummariesResultTypeDef = TypedDict(
    "ListComplianceSummariesResultTypeDef",
    {
        "ComplianceSummaryItems": List["ComplianceSummaryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDocumentMetadataHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredListDocumentMetadataHistoryRequestRequestTypeDef",
    {
        "Name": str,
        "Metadata": Literal["DocumentReviews"],
    },
)
_OptionalListDocumentMetadataHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalListDocumentMetadataHistoryRequestRequestTypeDef",
    {
        "DocumentVersion": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListDocumentMetadataHistoryRequestRequestTypeDef(
    _RequiredListDocumentMetadataHistoryRequestRequestTypeDef,
    _OptionalListDocumentMetadataHistoryRequestRequestTypeDef,
):
    pass

ListDocumentMetadataHistoryResponseTypeDef = TypedDict(
    "ListDocumentMetadataHistoryResponseTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "Author": str,
        "Metadata": "DocumentMetadataResponseInfoTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDocumentVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListDocumentVersionsRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalListDocumentVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListDocumentVersionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListDocumentVersionsRequestRequestTypeDef(
    _RequiredListDocumentVersionsRequestRequestTypeDef,
    _OptionalListDocumentVersionsRequestRequestTypeDef,
):
    pass

ListDocumentVersionsResultTypeDef = TypedDict(
    "ListDocumentVersionsResultTypeDef",
    {
        "DocumentVersions": List["DocumentVersionInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDocumentsRequestRequestTypeDef = TypedDict(
    "ListDocumentsRequestRequestTypeDef",
    {
        "DocumentFilterList": List["DocumentFilterTypeDef"],
        "Filters": List["DocumentKeyValuesFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListDocumentsResultTypeDef = TypedDict(
    "ListDocumentsResultTypeDef",
    {
        "DocumentIdentifiers": List["DocumentIdentifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListInventoryEntriesRequestRequestTypeDef = TypedDict(
    "_RequiredListInventoryEntriesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "TypeName": str,
    },
)
_OptionalListInventoryEntriesRequestRequestTypeDef = TypedDict(
    "_OptionalListInventoryEntriesRequestRequestTypeDef",
    {
        "Filters": List["InventoryFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListInventoryEntriesRequestRequestTypeDef(
    _RequiredListInventoryEntriesRequestRequestTypeDef,
    _OptionalListInventoryEntriesRequestRequestTypeDef,
):
    pass

ListInventoryEntriesResultTypeDef = TypedDict(
    "ListInventoryEntriesResultTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsItemEventsRequestRequestTypeDef = TypedDict(
    "ListOpsItemEventsRequestRequestTypeDef",
    {
        "Filters": List["OpsItemEventFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOpsItemEventsResponseTypeDef = TypedDict(
    "ListOpsItemEventsResponseTypeDef",
    {
        "NextToken": str,
        "Summaries": List["OpsItemEventSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsItemRelatedItemsRequestRequestTypeDef = TypedDict(
    "ListOpsItemRelatedItemsRequestRequestTypeDef",
    {
        "OpsItemId": str,
        "Filters": List["OpsItemRelatedItemsFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOpsItemRelatedItemsResponseTypeDef = TypedDict(
    "ListOpsItemRelatedItemsResponseTypeDef",
    {
        "NextToken": str,
        "Summaries": List["OpsItemRelatedItemSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpsMetadataRequestRequestTypeDef = TypedDict(
    "ListOpsMetadataRequestRequestTypeDef",
    {
        "Filters": List["OpsMetadataFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListOpsMetadataResultTypeDef = TypedDict(
    "ListOpsMetadataResultTypeDef",
    {
        "OpsMetadataList": List["OpsMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceComplianceSummariesRequestRequestTypeDef = TypedDict(
    "ListResourceComplianceSummariesRequestRequestTypeDef",
    {
        "Filters": List["ComplianceStringFilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListResourceComplianceSummariesResultTypeDef = TypedDict(
    "ListResourceComplianceSummariesResultTypeDef",
    {
        "ResourceComplianceSummaryItems": List["ResourceComplianceSummaryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceDataSyncRequestRequestTypeDef = TypedDict(
    "ListResourceDataSyncRequestRequestTypeDef",
    {
        "SyncType": str,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListResourceDataSyncResultTypeDef = TypedDict(
    "ListResourceDataSyncResultTypeDef",
    {
        "ResourceDataSyncItems": List["ResourceDataSyncItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredLoggingInfoTypeDef = TypedDict(
    "_RequiredLoggingInfoTypeDef",
    {
        "S3BucketName": str,
        "S3Region": str,
    },
)
_OptionalLoggingInfoTypeDef = TypedDict(
    "_OptionalLoggingInfoTypeDef",
    {
        "S3KeyPrefix": str,
    },
    total=False,
)

class LoggingInfoTypeDef(_RequiredLoggingInfoTypeDef, _OptionalLoggingInfoTypeDef):
    pass

MaintenanceWindowAutomationParametersTypeDef = TypedDict(
    "MaintenanceWindowAutomationParametersTypeDef",
    {
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
    },
    total=False,
)

MaintenanceWindowExecutionTaskIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
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
        "TaskType": MaintenanceWindowTaskTypeType,
        "Parameters": str,
        "Status": MaintenanceWindowExecutionStatusType,
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
        "Status": MaintenanceWindowExecutionStatusType,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

MaintenanceWindowFilterTypeDef = TypedDict(
    "MaintenanceWindowFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

MaintenanceWindowIdentityForTargetTypeDef = TypedDict(
    "MaintenanceWindowIdentityForTargetTypeDef",
    {
        "WindowId": str,
        "Name": str,
    },
    total=False,
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
    {
        "ClientContext": str,
        "Qualifier": str,
        "Payload": bytes,
    },
    total=False,
)

MaintenanceWindowRunCommandParametersTypeDef = TypedDict(
    "MaintenanceWindowRunCommandParametersTypeDef",
    {
        "Comment": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "DocumentHash": str,
        "DocumentHashType": DocumentHashTypeType,
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
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    {
        "Input": str,
        "Name": str,
    },
    total=False,
)

MaintenanceWindowTargetTypeDef = TypedDict(
    "MaintenanceWindowTargetTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": MaintenanceWindowResourceTypeType,
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
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

MaintenanceWindowTaskTypeDef = TypedDict(
    "MaintenanceWindowTaskTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": MaintenanceWindowTaskTypeType,
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

MetadataValueTypeDef = TypedDict(
    "MetadataValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

_RequiredModifyDocumentPermissionRequestRequestTypeDef = TypedDict(
    "_RequiredModifyDocumentPermissionRequestRequestTypeDef",
    {
        "Name": str,
        "PermissionType": Literal["Share"],
    },
)
_OptionalModifyDocumentPermissionRequestRequestTypeDef = TypedDict(
    "_OptionalModifyDocumentPermissionRequestRequestTypeDef",
    {
        "AccountIdsToAdd": List[str],
        "AccountIdsToRemove": List[str],
        "SharedDocumentVersion": str,
    },
    total=False,
)

class ModifyDocumentPermissionRequestRequestTypeDef(
    _RequiredModifyDocumentPermissionRequestRequestTypeDef,
    _OptionalModifyDocumentPermissionRequestRequestTypeDef,
):
    pass

NonCompliantSummaryTypeDef = TypedDict(
    "NonCompliantSummaryTypeDef",
    {
        "NonCompliantCount": int,
        "SeveritySummary": "SeveritySummaryTypeDef",
    },
    total=False,
)

NotificationConfigTypeDef = TypedDict(
    "NotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[NotificationEventType],
        "NotificationType": NotificationTypeType,
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

OpsEntityItemTypeDef = TypedDict(
    "OpsEntityItemTypeDef",
    {
        "CaptureTime": str,
        "Content": List[Dict[str, str]],
    },
    total=False,
)

OpsEntityTypeDef = TypedDict(
    "OpsEntityTypeDef",
    {
        "Id": str,
        "Data": Dict[str, "OpsEntityItemTypeDef"],
    },
    total=False,
)

_RequiredOpsFilterTypeDef = TypedDict(
    "_RequiredOpsFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)
_OptionalOpsFilterTypeDef = TypedDict(
    "_OptionalOpsFilterTypeDef",
    {
        "Type": OpsFilterOperatorTypeType,
    },
    total=False,
)

class OpsFilterTypeDef(_RequiredOpsFilterTypeDef, _OptionalOpsFilterTypeDef):
    pass

OpsItemDataValueTypeDef = TypedDict(
    "OpsItemDataValueTypeDef",
    {
        "Value": str,
        "Type": OpsItemDataTypeType,
    },
    total=False,
)

OpsItemEventFilterTypeDef = TypedDict(
    "OpsItemEventFilterTypeDef",
    {
        "Key": Literal["OpsItemId"],
        "Values": List[str],
        "Operator": Literal["Equal"],
    },
)

OpsItemEventSummaryTypeDef = TypedDict(
    "OpsItemEventSummaryTypeDef",
    {
        "OpsItemId": str,
        "EventId": str,
        "Source": str,
        "DetailType": str,
        "Detail": str,
        "CreatedBy": "OpsItemIdentityTypeDef",
        "CreatedTime": datetime,
    },
    total=False,
)

OpsItemFilterTypeDef = TypedDict(
    "OpsItemFilterTypeDef",
    {
        "Key": OpsItemFilterKeyType,
        "Values": List[str],
        "Operator": OpsItemFilterOperatorType,
    },
)

OpsItemIdentityTypeDef = TypedDict(
    "OpsItemIdentityTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

OpsItemNotificationTypeDef = TypedDict(
    "OpsItemNotificationTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

OpsItemRelatedItemSummaryTypeDef = TypedDict(
    "OpsItemRelatedItemSummaryTypeDef",
    {
        "OpsItemId": str,
        "AssociationId": str,
        "ResourceType": str,
        "AssociationType": str,
        "ResourceUri": str,
        "CreatedBy": "OpsItemIdentityTypeDef",
        "CreatedTime": datetime,
        "LastModifiedBy": "OpsItemIdentityTypeDef",
        "LastModifiedTime": datetime,
    },
    total=False,
)

OpsItemRelatedItemsFilterTypeDef = TypedDict(
    "OpsItemRelatedItemsFilterTypeDef",
    {
        "Key": OpsItemRelatedItemsFilterKeyType,
        "Values": List[str],
        "Operator": Literal["Equal"],
    },
)

OpsItemSummaryTypeDef = TypedDict(
    "OpsItemSummaryTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Priority": int,
        "Source": str,
        "Status": OpsItemStatusType,
        "OpsItemId": str,
        "Title": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Category": str,
        "Severity": str,
        "OpsItemType": str,
        "ActualStartTime": datetime,
        "ActualEndTime": datetime,
        "PlannedStartTime": datetime,
        "PlannedEndTime": datetime,
    },
    total=False,
)

OpsItemTypeDef = TypedDict(
    "OpsItemTypeDef",
    {
        "CreatedBy": str,
        "OpsItemType": str,
        "CreatedTime": datetime,
        "Description": str,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Notifications": List["OpsItemNotificationTypeDef"],
        "Priority": int,
        "RelatedOpsItems": List["RelatedOpsItemTypeDef"],
        "Status": OpsItemStatusType,
        "OpsItemId": str,
        "Version": str,
        "Title": str,
        "Source": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Category": str,
        "Severity": str,
        "ActualStartTime": datetime,
        "ActualEndTime": datetime,
        "PlannedStartTime": datetime,
        "PlannedEndTime": datetime,
    },
    total=False,
)

OpsMetadataFilterTypeDef = TypedDict(
    "OpsMetadataFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
)

OpsMetadataTypeDef = TypedDict(
    "OpsMetadataTypeDef",
    {
        "ResourceId": str,
        "OpsMetadataArn": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "CreationDate": datetime,
    },
    total=False,
)

OpsResultAttributeTypeDef = TypedDict(
    "OpsResultAttributeTypeDef",
    {
        "TypeName": str,
    },
)

OutputSourceTypeDef = TypedDict(
    "OutputSourceTypeDef",
    {
        "OutputSourceId": str,
        "OutputSourceType": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ParameterHistoryTypeDef = TypedDict(
    "ParameterHistoryTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": ParameterTierType,
        "Policies": List["ParameterInlinePolicyTypeDef"],
        "DataType": str,
    },
    total=False,
)

ParameterInlinePolicyTypeDef = TypedDict(
    "ParameterInlinePolicyTypeDef",
    {
        "PolicyText": str,
        "PolicyType": str,
        "PolicyStatus": str,
    },
    total=False,
)

ParameterMetadataTypeDef = TypedDict(
    "ParameterMetadataTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": ParameterTierType,
        "Policies": List["ParameterInlinePolicyTypeDef"],
        "DataType": str,
    },
    total=False,
)

_RequiredParameterStringFilterTypeDef = TypedDict(
    "_RequiredParameterStringFilterTypeDef",
    {
        "Key": str,
    },
)
_OptionalParameterStringFilterTypeDef = TypedDict(
    "_OptionalParameterStringFilterTypeDef",
    {
        "Option": str,
        "Values": List[str],
    },
    total=False,
)

class ParameterStringFilterTypeDef(
    _RequiredParameterStringFilterTypeDef, _OptionalParameterStringFilterTypeDef
):
    pass

ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
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

ParametersFilterTypeDef = TypedDict(
    "ParametersFilterTypeDef",
    {
        "Key": ParametersFilterKeyType,
        "Values": List[str],
    },
)

PatchBaselineIdentityTypeDef = TypedDict(
    "PatchBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": OperatingSystemType,
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

_RequiredPatchComplianceDataTypeDef = TypedDict(
    "_RequiredPatchComplianceDataTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": PatchComplianceDataStateType,
        "InstalledTime": datetime,
    },
)
_OptionalPatchComplianceDataTypeDef = TypedDict(
    "_OptionalPatchComplianceDataTypeDef",
    {
        "CVEIds": str,
    },
    total=False,
)

class PatchComplianceDataTypeDef(
    _RequiredPatchComplianceDataTypeDef, _OptionalPatchComplianceDataTypeDef
):
    pass

PatchFilterGroupTypeDef = TypedDict(
    "PatchFilterGroupTypeDef",
    {
        "PatchFilters": List["PatchFilterTypeDef"],
    },
)

PatchFilterTypeDef = TypedDict(
    "PatchFilterTypeDef",
    {
        "Key": PatchFilterKeyType,
        "Values": List[str],
    },
)

PatchGroupPatchBaselineMappingTypeDef = TypedDict(
    "PatchGroupPatchBaselineMappingTypeDef",
    {
        "PatchGroup": str,
        "BaselineIdentity": "PatchBaselineIdentityTypeDef",
    },
    total=False,
)

PatchOrchestratorFilterTypeDef = TypedDict(
    "PatchOrchestratorFilterTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

PatchRuleGroupTypeDef = TypedDict(
    "PatchRuleGroupTypeDef",
    {
        "PatchRules": List["PatchRuleTypeDef"],
    },
)

_RequiredPatchRuleTypeDef = TypedDict(
    "_RequiredPatchRuleTypeDef",
    {
        "PatchFilterGroup": "PatchFilterGroupTypeDef",
    },
)
_OptionalPatchRuleTypeDef = TypedDict(
    "_OptionalPatchRuleTypeDef",
    {
        "ComplianceLevel": PatchComplianceLevelType,
        "ApproveAfterDays": int,
        "ApproveUntilDate": str,
        "EnableNonSecurity": bool,
    },
    total=False,
)

class PatchRuleTypeDef(_RequiredPatchRuleTypeDef, _OptionalPatchRuleTypeDef):
    pass

PatchSourceTypeDef = TypedDict(
    "PatchSourceTypeDef",
    {
        "Name": str,
        "Products": List[str],
        "Configuration": str,
    },
)

PatchStatusTypeDef = TypedDict(
    "PatchStatusTypeDef",
    {
        "DeploymentStatus": PatchDeploymentStatusType,
        "ComplianceLevel": PatchComplianceLevelType,
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
        "AdvisoryIds": List[str],
        "BugzillaIds": List[str],
        "CVEIds": List[str],
        "Name": str,
        "Epoch": int,
        "Version": str,
        "Release": str,
        "Arch": str,
        "Severity": str,
        "Repository": str,
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

_RequiredPutComplianceItemsRequestRequestTypeDef = TypedDict(
    "_RequiredPutComplianceItemsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceType": str,
        "ComplianceType": str,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "Items": List["ComplianceItemEntryTypeDef"],
    },
)
_OptionalPutComplianceItemsRequestRequestTypeDef = TypedDict(
    "_OptionalPutComplianceItemsRequestRequestTypeDef",
    {
        "ItemContentHash": str,
        "UploadType": ComplianceUploadTypeType,
    },
    total=False,
)

class PutComplianceItemsRequestRequestTypeDef(
    _RequiredPutComplianceItemsRequestRequestTypeDef,
    _OptionalPutComplianceItemsRequestRequestTypeDef,
):
    pass

PutInventoryRequestRequestTypeDef = TypedDict(
    "PutInventoryRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Items": List["InventoryItemTypeDef"],
    },
)

PutInventoryResultTypeDef = TypedDict(
    "PutInventoryResultTypeDef",
    {
        "Message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutParameterRequestRequestTypeDef = TypedDict(
    "_RequiredPutParameterRequestRequestTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)
_OptionalPutParameterRequestRequestTypeDef = TypedDict(
    "_OptionalPutParameterRequestRequestTypeDef",
    {
        "Description": str,
        "Type": ParameterTypeType,
        "KeyId": str,
        "Overwrite": bool,
        "AllowedPattern": str,
        "Tags": List["TagTypeDef"],
        "Tier": ParameterTierType,
        "Policies": str,
        "DataType": str,
    },
    total=False,
)

class PutParameterRequestRequestTypeDef(
    _RequiredPutParameterRequestRequestTypeDef, _OptionalPutParameterRequestRequestTypeDef
):
    pass

PutParameterResultTypeDef = TypedDict(
    "PutParameterResultTypeDef",
    {
        "Version": int,
        "Tier": ParameterTierType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterDefaultPatchBaselineRequestRequestTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)

RegisterDefaultPatchBaselineResultTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterPatchBaselineForPatchGroupRequestRequestTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupRequestRequestTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
    },
)

RegisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    {
        "BaselineId": str,
        "PatchGroup": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTargetWithMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterTargetWithMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "ResourceType": MaintenanceWindowResourceTypeType,
        "Targets": List["TargetTypeDef"],
    },
)
_OptionalRegisterTargetWithMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterTargetWithMaintenanceWindowRequestRequestTypeDef",
    {
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
        "ClientToken": str,
    },
    total=False,
)

class RegisterTargetWithMaintenanceWindowRequestRequestTypeDef(
    _RequiredRegisterTargetWithMaintenanceWindowRequestRequestTypeDef,
    _OptionalRegisterTargetWithMaintenanceWindowRequestRequestTypeDef,
):
    pass

RegisterTargetWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    {
        "WindowTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTaskWithMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterTaskWithMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
        "TaskArn": str,
        "TaskType": MaintenanceWindowTaskTypeType,
    },
)
_OptionalRegisterTaskWithMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterTaskWithMaintenanceWindowRequestRequestTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
        "ClientToken": str,
    },
    total=False,
)

class RegisterTaskWithMaintenanceWindowRequestRequestTypeDef(
    _RequiredRegisterTaskWithMaintenanceWindowRequestRequestTypeDef,
    _OptionalRegisterTaskWithMaintenanceWindowRequestRequestTypeDef,
):
    pass

RegisterTaskWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    {
        "WindowTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelatedOpsItemTypeDef = TypedDict(
    "RelatedOpsItemTypeDef",
    {
        "OpsItemId": str,
    },
)

RemoveTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceRequestRequestTypeDef",
    {
        "ResourceType": ResourceTypeForTaggingType,
        "ResourceId": str,
        "TagKeys": List[str],
    },
)

ResetServiceSettingRequestRequestTypeDef = TypedDict(
    "ResetServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
    },
)

ResetServiceSettingResultTypeDef = TypedDict(
    "ResetServiceSettingResultTypeDef",
    {
        "ServiceSetting": "ServiceSettingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolvedTargetsTypeDef = TypedDict(
    "ResolvedTargetsTypeDef",
    {
        "ParameterValues": List[str],
        "Truncated": bool,
    },
    total=False,
)

ResourceComplianceSummaryItemTypeDef = TypedDict(
    "ResourceComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": ComplianceStatusType,
        "OverallSeverity": ComplianceSeverityType,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "CompliantSummary": "CompliantSummaryTypeDef",
        "NonCompliantSummary": "NonCompliantSummaryTypeDef",
    },
    total=False,
)

_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef",
    {
        "OrganizationSourceType": str,
    },
)
_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef",
    {
        "OrganizationalUnits": List["ResourceDataSyncOrganizationalUnitTypeDef"],
    },
    total=False,
)

class ResourceDataSyncAwsOrganizationsSourceTypeDef(
    _RequiredResourceDataSyncAwsOrganizationsSourceTypeDef,
    _OptionalResourceDataSyncAwsOrganizationsSourceTypeDef,
):
    pass

ResourceDataSyncDestinationDataSharingTypeDef = TypedDict(
    "ResourceDataSyncDestinationDataSharingTypeDef",
    {
        "DestinationDataSharingType": str,
    },
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
        "LastStatus": LastResourceDataSyncStatusType,
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)

ResourceDataSyncOrganizationalUnitTypeDef = TypedDict(
    "ResourceDataSyncOrganizationalUnitTypeDef",
    {
        "OrganizationalUnitId": str,
    },
    total=False,
)

_RequiredResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_RequiredResourceDataSyncS3DestinationTypeDef",
    {
        "BucketName": str,
        "SyncFormat": Literal["JsonSerDe"],
        "Region": str,
    },
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

_RequiredResourceDataSyncSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncSourceTypeDef",
    {
        "SourceType": str,
        "SourceRegions": List[str],
    },
)
_OptionalResourceDataSyncSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": "ResourceDataSyncAwsOrganizationsSourceTypeDef",
        "IncludeFutureRegions": bool,
        "EnableAllOpsDataSources": bool,
    },
    total=False,
)

class ResourceDataSyncSourceTypeDef(
    _RequiredResourceDataSyncSourceTypeDef, _OptionalResourceDataSyncSourceTypeDef
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
        "EnableAllOpsDataSources": bool,
    },
    total=False,
)

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

ResultAttributeTypeDef = TypedDict(
    "ResultAttributeTypeDef",
    {
        "TypeName": str,
    },
)

ResumeSessionRequestRequestTypeDef = TypedDict(
    "ResumeSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

ResumeSessionResponseTypeDef = TypedDict(
    "ResumeSessionResponseTypeDef",
    {
        "SessionId": str,
        "TokenValue": str,
        "StreamUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReviewInformationTypeDef = TypedDict(
    "ReviewInformationTypeDef",
    {
        "ReviewedTime": datetime,
        "Status": ReviewStatusType,
        "Reviewer": str,
    },
    total=False,
)

_RequiredRunbookTypeDef = TypedDict(
    "_RequiredRunbookTypeDef",
    {
        "DocumentName": str,
    },
)
_OptionalRunbookTypeDef = TypedDict(
    "_OptionalRunbookTypeDef",
    {
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

class RunbookTypeDef(_RequiredRunbookTypeDef, _OptionalRunbookTypeDef):
    pass

S3OutputLocationTypeDef = TypedDict(
    "S3OutputLocationTypeDef",
    {
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

S3OutputUrlTypeDef = TypedDict(
    "S3OutputUrlTypeDef",
    {
        "OutputUrl": str,
    },
    total=False,
)

ScheduledWindowExecutionTypeDef = TypedDict(
    "ScheduledWindowExecutionTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "ExecutionTime": str,
    },
    total=False,
)

_RequiredSendAutomationSignalRequestRequestTypeDef = TypedDict(
    "_RequiredSendAutomationSignalRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
        "SignalType": SignalTypeType,
    },
)
_OptionalSendAutomationSignalRequestRequestTypeDef = TypedDict(
    "_OptionalSendAutomationSignalRequestRequestTypeDef",
    {
        "Payload": Dict[str, List[str]],
    },
    total=False,
)

class SendAutomationSignalRequestRequestTypeDef(
    _RequiredSendAutomationSignalRequestRequestTypeDef,
    _OptionalSendAutomationSignalRequestRequestTypeDef,
):
    pass

_RequiredSendCommandRequestRequestTypeDef = TypedDict(
    "_RequiredSendCommandRequestRequestTypeDef",
    {
        "DocumentName": str,
    },
)
_OptionalSendCommandRequestRequestTypeDef = TypedDict(
    "_OptionalSendCommandRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
        "Targets": List["TargetTypeDef"],
        "DocumentVersion": str,
        "DocumentHash": str,
        "DocumentHashType": DocumentHashTypeType,
        "TimeoutSeconds": int,
        "Comment": str,
        "Parameters": Dict[str, List[str]],
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "ServiceRoleArn": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
    },
    total=False,
)

class SendCommandRequestRequestTypeDef(
    _RequiredSendCommandRequestRequestTypeDef, _OptionalSendCommandRequestRequestTypeDef
):
    pass

SendCommandResultTypeDef = TypedDict(
    "SendCommandResultTypeDef",
    {
        "Command": "CommandTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

SessionFilterTypeDef = TypedDict(
    "SessionFilterTypeDef",
    {
        "key": SessionFilterKeyType,
        "value": str,
    },
)

SessionManagerOutputUrlTypeDef = TypedDict(
    "SessionManagerOutputUrlTypeDef",
    {
        "S3OutputUrl": str,
        "CloudWatchOutputUrl": str,
    },
    total=False,
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": SessionStatusType,
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

StartAssociationsOnceRequestRequestTypeDef = TypedDict(
    "StartAssociationsOnceRequestRequestTypeDef",
    {
        "AssociationIds": List[str],
    },
)

_RequiredStartAutomationExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartAutomationExecutionRequestRequestTypeDef",
    {
        "DocumentName": str,
    },
)
_OptionalStartAutomationExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartAutomationExecutionRequestRequestTypeDef",
    {
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "ClientToken": str,
        "Mode": ExecutionModeType,
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "TargetMaps": List[Dict[str, List[str]]],
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetLocations": List["TargetLocationTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class StartAutomationExecutionRequestRequestTypeDef(
    _RequiredStartAutomationExecutionRequestRequestTypeDef,
    _OptionalStartAutomationExecutionRequestRequestTypeDef,
):
    pass

StartAutomationExecutionResultTypeDef = TypedDict(
    "StartAutomationExecutionResultTypeDef",
    {
        "AutomationExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartChangeRequestExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStartChangeRequestExecutionRequestRequestTypeDef",
    {
        "DocumentName": str,
        "Runbooks": List["RunbookTypeDef"],
    },
)
_OptionalStartChangeRequestExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStartChangeRequestExecutionRequestRequestTypeDef",
    {
        "ScheduledTime": Union[datetime, str],
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "ChangeRequestName": str,
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
        "ScheduledEndTime": Union[datetime, str],
        "ChangeDetails": str,
    },
    total=False,
)

class StartChangeRequestExecutionRequestRequestTypeDef(
    _RequiredStartChangeRequestExecutionRequestRequestTypeDef,
    _OptionalStartChangeRequestExecutionRequestRequestTypeDef,
):
    pass

StartChangeRequestExecutionResultTypeDef = TypedDict(
    "StartChangeRequestExecutionResultTypeDef",
    {
        "AutomationExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartSessionRequestRequestTypeDef = TypedDict(
    "_RequiredStartSessionRequestRequestTypeDef",
    {
        "Target": str,
    },
)
_OptionalStartSessionRequestRequestTypeDef = TypedDict(
    "_OptionalStartSessionRequestRequestTypeDef",
    {
        "DocumentName": str,
        "Parameters": Dict[str, List[str]],
    },
    total=False,
)

class StartSessionRequestRequestTypeDef(
    _RequiredStartSessionRequestRequestTypeDef, _OptionalStartSessionRequestRequestTypeDef
):
    pass

StartSessionResponseTypeDef = TypedDict(
    "StartSessionResponseTypeDef",
    {
        "SessionId": str,
        "TokenValue": str,
        "StreamUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StepExecutionFilterTypeDef = TypedDict(
    "StepExecutionFilterTypeDef",
    {
        "Key": StepExecutionFilterKeyType,
        "Values": List[str],
    },
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
        "StepStatus": AutomationExecutionStatusType,
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

_RequiredStopAutomationExecutionRequestRequestTypeDef = TypedDict(
    "_RequiredStopAutomationExecutionRequestRequestTypeDef",
    {
        "AutomationExecutionId": str,
    },
)
_OptionalStopAutomationExecutionRequestRequestTypeDef = TypedDict(
    "_OptionalStopAutomationExecutionRequestRequestTypeDef",
    {
        "Type": StopTypeType,
    },
    total=False,
)

class StopAutomationExecutionRequestRequestTypeDef(
    _RequiredStopAutomationExecutionRequestRequestTypeDef,
    _OptionalStopAutomationExecutionRequestRequestTypeDef,
):
    pass

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

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

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

TerminateSessionRequestRequestTypeDef = TypedDict(
    "TerminateSessionRequestRequestTypeDef",
    {
        "SessionId": str,
    },
)

TerminateSessionResponseTypeDef = TypedDict(
    "TerminateSessionResponseTypeDef",
    {
        "SessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnlabelParameterVersionRequestRequestTypeDef = TypedDict(
    "UnlabelParameterVersionRequestRequestTypeDef",
    {
        "Name": str,
        "ParameterVersion": int,
        "Labels": List[str],
    },
)

UnlabelParameterVersionResultTypeDef = TypedDict(
    "UnlabelParameterVersionResultTypeDef",
    {
        "RemovedLabels": List[str],
        "InvalidLabels": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalUpdateAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAssociationRequestRequestTypeDef",
    {
        "Parameters": Dict[str, List[str]],
        "DocumentVersion": str,
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "Name": str,
        "Targets": List["TargetTypeDef"],
        "AssociationName": str,
        "AssociationVersion": str,
        "AutomationTargetParameterName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverityType,
        "SyncCompliance": AssociationSyncComplianceType,
        "ApplyOnlyAtCronInterval": bool,
        "CalendarNames": List[str],
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

class UpdateAssociationRequestRequestTypeDef(
    _RequiredUpdateAssociationRequestRequestTypeDef, _OptionalUpdateAssociationRequestRequestTypeDef
):
    pass

UpdateAssociationResultTypeDef = TypedDict(
    "UpdateAssociationResultTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAssociationStatusRequestRequestTypeDef = TypedDict(
    "UpdateAssociationStatusRequestRequestTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationStatus": "AssociationStatusTypeDef",
    },
)

UpdateAssociationStatusResultTypeDef = TypedDict(
    "UpdateAssociationStatusResultTypeDef",
    {
        "AssociationDescription": "AssociationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDocumentDefaultVersionRequestRequestTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
    },
)

UpdateDocumentDefaultVersionResultTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionResultTypeDef",
    {
        "Description": "DocumentDefaultVersionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDocumentMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentMetadataRequestRequestTypeDef",
    {
        "Name": str,
        "DocumentReviews": "DocumentReviewsTypeDef",
    },
)
_OptionalUpdateDocumentMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentMetadataRequestRequestTypeDef",
    {
        "DocumentVersion": str,
    },
    total=False,
)

class UpdateDocumentMetadataRequestRequestTypeDef(
    _RequiredUpdateDocumentMetadataRequestRequestTypeDef,
    _OptionalUpdateDocumentMetadataRequestRequestTypeDef,
):
    pass

_RequiredUpdateDocumentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDocumentRequestRequestTypeDef",
    {
        "Content": str,
        "Name": str,
    },
)
_OptionalUpdateDocumentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDocumentRequestRequestTypeDef",
    {
        "Attachments": List["AttachmentsSourceTypeDef"],
        "DisplayName": str,
        "VersionName": str,
        "DocumentVersion": str,
        "DocumentFormat": DocumentFormatType,
        "TargetType": str,
    },
    total=False,
)

class UpdateDocumentRequestRequestTypeDef(
    _RequiredUpdateDocumentRequestRequestTypeDef, _OptionalUpdateDocumentRequestRequestTypeDef
):
    pass

UpdateDocumentResultTypeDef = TypedDict(
    "UpdateDocumentResultTypeDef",
    {
        "DocumentDescription": "DocumentDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMaintenanceWindowRequestRequestTypeDef",
    {
        "WindowId": str,
    },
)
_OptionalUpdateMaintenanceWindowRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMaintenanceWindowRequestRequestTypeDef",
    {
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
        "Replace": bool,
    },
    total=False,
)

class UpdateMaintenanceWindowRequestRequestTypeDef(
    _RequiredUpdateMaintenanceWindowRequestRequestTypeDef,
    _OptionalUpdateMaintenanceWindowRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMaintenanceWindowTargetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMaintenanceWindowTargetRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
    },
)
_OptionalUpdateMaintenanceWindowTargetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMaintenanceWindowTargetRequestRequestTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
        "Replace": bool,
    },
    total=False,
)

class UpdateMaintenanceWindowTargetRequestRequestTypeDef(
    _RequiredUpdateMaintenanceWindowTargetRequestRequestTypeDef,
    _OptionalUpdateMaintenanceWindowTargetRequestRequestTypeDef,
):
    pass

UpdateMaintenanceWindowTargetResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTargetResultTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMaintenanceWindowTaskRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMaintenanceWindowTaskRequestRequestTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
    },
)
_OptionalUpdateMaintenanceWindowTaskRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMaintenanceWindowTaskRequestRequestTypeDef",
    {
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
        "Replace": bool,
    },
    total=False,
)

class UpdateMaintenanceWindowTaskRequestRequestTypeDef(
    _RequiredUpdateMaintenanceWindowTaskRequestRequestTypeDef,
    _OptionalUpdateMaintenanceWindowTaskRequestRequestTypeDef,
):
    pass

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateManagedInstanceRoleRequestRequestTypeDef = TypedDict(
    "UpdateManagedInstanceRoleRequestRequestTypeDef",
    {
        "InstanceId": str,
        "IamRole": str,
    },
)

_RequiredUpdateOpsItemRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOpsItemRequestRequestTypeDef",
    {
        "OpsItemId": str,
    },
)
_OptionalUpdateOpsItemRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOpsItemRequestRequestTypeDef",
    {
        "Description": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "OperationalDataToDelete": List[str],
        "Notifications": List["OpsItemNotificationTypeDef"],
        "Priority": int,
        "RelatedOpsItems": List["RelatedOpsItemTypeDef"],
        "Status": OpsItemStatusType,
        "Title": str,
        "Category": str,
        "Severity": str,
        "ActualStartTime": Union[datetime, str],
        "ActualEndTime": Union[datetime, str],
        "PlannedStartTime": Union[datetime, str],
        "PlannedEndTime": Union[datetime, str],
    },
    total=False,
)

class UpdateOpsItemRequestRequestTypeDef(
    _RequiredUpdateOpsItemRequestRequestTypeDef, _OptionalUpdateOpsItemRequestRequestTypeDef
):
    pass

_RequiredUpdateOpsMetadataRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateOpsMetadataRequestRequestTypeDef",
    {
        "OpsMetadataArn": str,
    },
)
_OptionalUpdateOpsMetadataRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateOpsMetadataRequestRequestTypeDef",
    {
        "MetadataToUpdate": Dict[str, "MetadataValueTypeDef"],
        "KeysToDelete": List[str],
    },
    total=False,
)

class UpdateOpsMetadataRequestRequestTypeDef(
    _RequiredUpdateOpsMetadataRequestRequestTypeDef, _OptionalUpdateOpsMetadataRequestRequestTypeDef
):
    pass

UpdateOpsMetadataResultTypeDef = TypedDict(
    "UpdateOpsMetadataResultTypeDef",
    {
        "OpsMetadataArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePatchBaselineRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePatchBaselineRequestRequestTypeDef",
    {
        "BaselineId": str,
    },
)
_OptionalUpdatePatchBaselineRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePatchBaselineRequestRequestTypeDef",
    {
        "Name": str,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "Replace": bool,
    },
    total=False,
)

class UpdatePatchBaselineRequestRequestTypeDef(
    _RequiredUpdatePatchBaselineRequestRequestTypeDef,
    _OptionalUpdatePatchBaselineRequestRequestTypeDef,
):
    pass

UpdatePatchBaselineResultTypeDef = TypedDict(
    "UpdatePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystemType,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevelType,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchActionType,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateResourceDataSyncRequestRequestTypeDef = TypedDict(
    "UpdateResourceDataSyncRequestRequestTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": "ResourceDataSyncSourceTypeDef",
    },
)

UpdateServiceSettingRequestRequestTypeDef = TypedDict(
    "UpdateServiceSettingRequestRequestTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
