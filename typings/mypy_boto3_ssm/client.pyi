# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for ssm service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm import SSMClient

    client: SSMClient = boto3.client("ssm")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_ssm.paginator import (
    DescribeActivationsPaginator,
    DescribeAssociationExecutionsPaginator,
    DescribeAssociationExecutionTargetsPaginator,
    DescribeAutomationExecutionsPaginator,
    DescribeAutomationStepExecutionsPaginator,
    DescribeAvailablePatchesPaginator,
    DescribeEffectiveInstanceAssociationsPaginator,
    DescribeEffectivePatchesForPatchBaselinePaginator,
    DescribeInstanceAssociationsStatusPaginator,
    DescribeInstanceInformationPaginator,
    DescribeInstancePatchesPaginator,
    DescribeInstancePatchStatesForPatchGroupPaginator,
    DescribeInstancePatchStatesPaginator,
    DescribeInventoryDeletionsPaginator,
    DescribeMaintenanceWindowExecutionsPaginator,
    DescribeMaintenanceWindowExecutionTaskInvocationsPaginator,
    DescribeMaintenanceWindowExecutionTasksPaginator,
    DescribeMaintenanceWindowSchedulePaginator,
    DescribeMaintenanceWindowsForTargetPaginator,
    DescribeMaintenanceWindowsPaginator,
    DescribeMaintenanceWindowTargetsPaginator,
    DescribeMaintenanceWindowTasksPaginator,
    DescribeOpsItemsPaginator,
    DescribeParametersPaginator,
    DescribePatchBaselinesPaginator,
    DescribePatchGroupsPaginator,
    DescribePatchPropertiesPaginator,
    DescribeSessionsPaginator,
    GetInventoryPaginator,
    GetInventorySchemaPaginator,
    GetOpsSummaryPaginator,
    GetParameterHistoryPaginator,
    GetParametersByPathPaginator,
    ListAssociationsPaginator,
    ListAssociationVersionsPaginator,
    ListCommandInvocationsPaginator,
    ListCommandsPaginator,
    ListComplianceItemsPaginator,
    ListComplianceSummariesPaginator,
    ListDocumentsPaginator,
    ListDocumentVersionsPaginator,
    ListResourceComplianceSummariesPaginator,
    ListResourceDataSyncPaginator,
)
from mypy_boto3_ssm.type_defs import (
    AssociationExecutionFilterTypeDef,
    AssociationExecutionTargetsFilterTypeDef,
    AssociationFilterTypeDef,
    AssociationStatusTypeDef,
    AttachmentsSourceTypeDef,
    AutomationExecutionFilterTypeDef,
    CancelMaintenanceWindowExecutionResultTypeDef,
    CloudWatchOutputConfigTypeDef,
    CommandFilterTypeDef,
    ComplianceExecutionSummaryTypeDef,
    ComplianceItemEntryTypeDef,
    ComplianceStringFilterTypeDef,
    CreateActivationResultTypeDef,
    CreateAssociationBatchRequestEntryTypeDef,
    CreateAssociationBatchResultTypeDef,
    CreateAssociationResultTypeDef,
    CreateDocumentResultTypeDef,
    CreateMaintenanceWindowResultTypeDef,
    CreateOpsItemResponseTypeDef,
    CreatePatchBaselineResultTypeDef,
    DeleteInventoryResultTypeDef,
    DeleteMaintenanceWindowResultTypeDef,
    DeleteParametersResultTypeDef,
    DeletePatchBaselineResultTypeDef,
    DeregisterPatchBaselineForPatchGroupResultTypeDef,
    DeregisterTargetFromMaintenanceWindowResultTypeDef,
    DeregisterTaskFromMaintenanceWindowResultTypeDef,
    DescribeActivationsFilterTypeDef,
    DescribeActivationsResultTypeDef,
    DescribeAssociationExecutionsResultTypeDef,
    DescribeAssociationExecutionTargetsResultTypeDef,
    DescribeAssociationResultTypeDef,
    DescribeAutomationExecutionsResultTypeDef,
    DescribeAutomationStepExecutionsResultTypeDef,
    DescribeAvailablePatchesResultTypeDef,
    DescribeDocumentPermissionResponseTypeDef,
    DescribeDocumentResultTypeDef,
    DescribeEffectiveInstanceAssociationsResultTypeDef,
    DescribeEffectivePatchesForPatchBaselineResultTypeDef,
    DescribeInstanceAssociationsStatusResultTypeDef,
    DescribeInstanceInformationResultTypeDef,
    DescribeInstancePatchesResultTypeDef,
    DescribeInstancePatchStatesForPatchGroupResultTypeDef,
    DescribeInstancePatchStatesResultTypeDef,
    DescribeInventoryDeletionsResultTypeDef,
    DescribeMaintenanceWindowExecutionsResultTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef,
    DescribeMaintenanceWindowExecutionTasksResultTypeDef,
    DescribeMaintenanceWindowScheduleResultTypeDef,
    DescribeMaintenanceWindowsForTargetResultTypeDef,
    DescribeMaintenanceWindowsResultTypeDef,
    DescribeMaintenanceWindowTargetsResultTypeDef,
    DescribeMaintenanceWindowTasksResultTypeDef,
    DescribeOpsItemsResponseTypeDef,
    DescribeParametersResultTypeDef,
    DescribePatchBaselinesResultTypeDef,
    DescribePatchGroupsResultTypeDef,
    DescribePatchGroupStateResultTypeDef,
    DescribePatchPropertiesResultTypeDef,
    DescribeSessionsResponseTypeDef,
    DocumentFilterTypeDef,
    DocumentKeyValuesFilterTypeDef,
    DocumentRequiresTypeDef,
    GetAutomationExecutionResultTypeDef,
    GetCalendarStateResponseTypeDef,
    GetCommandInvocationResultTypeDef,
    GetConnectionStatusResponseTypeDef,
    GetDefaultPatchBaselineResultTypeDef,
    GetDeployablePatchSnapshotForInstanceResultTypeDef,
    GetDocumentResultTypeDef,
    GetInventoryResultTypeDef,
    GetInventorySchemaResultTypeDef,
    GetMaintenanceWindowExecutionResultTypeDef,
    GetMaintenanceWindowExecutionTaskInvocationResultTypeDef,
    GetMaintenanceWindowExecutionTaskResultTypeDef,
    GetMaintenanceWindowResultTypeDef,
    GetMaintenanceWindowTaskResultTypeDef,
    GetOpsItemResponseTypeDef,
    GetOpsSummaryResultTypeDef,
    GetParameterHistoryResultTypeDef,
    GetParameterResultTypeDef,
    GetParametersByPathResultTypeDef,
    GetParametersResultTypeDef,
    GetPatchBaselineForPatchGroupResultTypeDef,
    GetPatchBaselineResultTypeDef,
    GetServiceSettingResultTypeDef,
    InstanceAssociationOutputLocationTypeDef,
    InstanceInformationFilterTypeDef,
    InstanceInformationStringFilterTypeDef,
    InstancePatchStateFilterTypeDef,
    InventoryFilterTypeDef,
    InventoryItemTypeDef,
    LabelParameterVersionResultTypeDef,
    ListAssociationsResultTypeDef,
    ListAssociationVersionsResultTypeDef,
    ListCommandInvocationsResultTypeDef,
    ListCommandsResultTypeDef,
    ListComplianceItemsResultTypeDef,
    ListComplianceSummariesResultTypeDef,
    ListDocumentsResultTypeDef,
    ListDocumentVersionsResultTypeDef,
    ListInventoryEntriesResultTypeDef,
    ListResourceComplianceSummariesResultTypeDef,
    ListResourceDataSyncResultTypeDef,
    ListTagsForResourceResultTypeDef,
    LoggingInfoTypeDef,
    MaintenanceWindowFilterTypeDef,
    MaintenanceWindowTaskInvocationParametersTypeDef,
    MaintenanceWindowTaskParameterValueExpressionTypeDef,
    NotificationConfigTypeDef,
    OpsFilterTypeDef,
    OpsItemDataValueTypeDef,
    OpsItemFilterTypeDef,
    OpsItemNotificationTypeDef,
    OpsResultAttributeTypeDef,
    ParametersFilterTypeDef,
    ParameterStringFilterTypeDef,
    PatchFilterGroupTypeDef,
    PatchOrchestratorFilterTypeDef,
    PatchRuleGroupTypeDef,
    PatchSourceTypeDef,
    PutInventoryResultTypeDef,
    PutParameterResultTypeDef,
    RegisterDefaultPatchBaselineResultTypeDef,
    RegisterPatchBaselineForPatchGroupResultTypeDef,
    RegisterTargetWithMaintenanceWindowResultTypeDef,
    RegisterTaskWithMaintenanceWindowResultTypeDef,
    RelatedOpsItemTypeDef,
    ResetServiceSettingResultTypeDef,
    ResourceDataSyncS3DestinationTypeDef,
    ResourceDataSyncSourceTypeDef,
    ResultAttributeTypeDef,
    ResumeSessionResponseTypeDef,
    SendCommandResultTypeDef,
    SessionFilterTypeDef,
    StartAutomationExecutionResultTypeDef,
    StartSessionResponseTypeDef,
    StepExecutionFilterTypeDef,
    TagTypeDef,
    TargetLocationTypeDef,
    TargetTypeDef,
    TerminateSessionResponseTypeDef,
    UpdateAssociationResultTypeDef,
    UpdateAssociationStatusResultTypeDef,
    UpdateDocumentDefaultVersionResultTypeDef,
    UpdateDocumentResultTypeDef,
    UpdateMaintenanceWindowResultTypeDef,
    UpdateMaintenanceWindowTargetResultTypeDef,
    UpdateMaintenanceWindowTaskResultTypeDef,
    UpdatePatchBaselineResultTypeDef,
)
from mypy_boto3_ssm.waiter import CommandExecutedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SSMClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    AssociatedInstances: Type[BotocoreClientError]
    AssociationAlreadyExists: Type[BotocoreClientError]
    AssociationDoesNotExist: Type[BotocoreClientError]
    AssociationExecutionDoesNotExist: Type[BotocoreClientError]
    AssociationLimitExceeded: Type[BotocoreClientError]
    AssociationVersionLimitExceeded: Type[BotocoreClientError]
    AutomationDefinitionNotFoundException: Type[BotocoreClientError]
    AutomationDefinitionVersionNotFoundException: Type[BotocoreClientError]
    AutomationExecutionLimitExceededException: Type[BotocoreClientError]
    AutomationExecutionNotFoundException: Type[BotocoreClientError]
    AutomationStepNotFoundException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ComplianceTypeCountLimitExceededException: Type[BotocoreClientError]
    CustomSchemaCountLimitExceededException: Type[BotocoreClientError]
    DocumentAlreadyExists: Type[BotocoreClientError]
    DocumentLimitExceeded: Type[BotocoreClientError]
    DocumentPermissionLimit: Type[BotocoreClientError]
    DocumentVersionLimitExceeded: Type[BotocoreClientError]
    DoesNotExistException: Type[BotocoreClientError]
    DuplicateDocumentContent: Type[BotocoreClientError]
    DuplicateDocumentVersionName: Type[BotocoreClientError]
    DuplicateInstanceId: Type[BotocoreClientError]
    FeatureNotAvailableException: Type[BotocoreClientError]
    HierarchyLevelLimitExceededException: Type[BotocoreClientError]
    HierarchyTypeMismatchException: Type[BotocoreClientError]
    IdempotentParameterMismatch: Type[BotocoreClientError]
    IncompatiblePolicyException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InvalidActivation: Type[BotocoreClientError]
    InvalidActivationId: Type[BotocoreClientError]
    InvalidAggregatorException: Type[BotocoreClientError]
    InvalidAllowedPatternException: Type[BotocoreClientError]
    InvalidAssociation: Type[BotocoreClientError]
    InvalidAssociationVersion: Type[BotocoreClientError]
    InvalidAutomationExecutionParametersException: Type[BotocoreClientError]
    InvalidAutomationSignalException: Type[BotocoreClientError]
    InvalidAutomationStatusUpdateException: Type[BotocoreClientError]
    InvalidCommandId: Type[BotocoreClientError]
    InvalidDeleteInventoryParametersException: Type[BotocoreClientError]
    InvalidDeletionIdException: Type[BotocoreClientError]
    InvalidDocument: Type[BotocoreClientError]
    InvalidDocumentContent: Type[BotocoreClientError]
    InvalidDocumentOperation: Type[BotocoreClientError]
    InvalidDocumentSchemaVersion: Type[BotocoreClientError]
    InvalidDocumentType: Type[BotocoreClientError]
    InvalidDocumentVersion: Type[BotocoreClientError]
    InvalidFilter: Type[BotocoreClientError]
    InvalidFilterKey: Type[BotocoreClientError]
    InvalidFilterOption: Type[BotocoreClientError]
    InvalidFilterValue: Type[BotocoreClientError]
    InvalidInstanceId: Type[BotocoreClientError]
    InvalidInstanceInformationFilterValue: Type[BotocoreClientError]
    InvalidInventoryGroupException: Type[BotocoreClientError]
    InvalidInventoryItemContextException: Type[BotocoreClientError]
    InvalidInventoryRequestException: Type[BotocoreClientError]
    InvalidItemContentException: Type[BotocoreClientError]
    InvalidKeyId: Type[BotocoreClientError]
    InvalidNextToken: Type[BotocoreClientError]
    InvalidNotificationConfig: Type[BotocoreClientError]
    InvalidOptionException: Type[BotocoreClientError]
    InvalidOutputFolder: Type[BotocoreClientError]
    InvalidOutputLocation: Type[BotocoreClientError]
    InvalidParameters: Type[BotocoreClientError]
    InvalidPermissionType: Type[BotocoreClientError]
    InvalidPluginName: Type[BotocoreClientError]
    InvalidPolicyAttributeException: Type[BotocoreClientError]
    InvalidPolicyTypeException: Type[BotocoreClientError]
    InvalidResourceId: Type[BotocoreClientError]
    InvalidResourceType: Type[BotocoreClientError]
    InvalidResultAttributeException: Type[BotocoreClientError]
    InvalidRole: Type[BotocoreClientError]
    InvalidSchedule: Type[BotocoreClientError]
    InvalidTarget: Type[BotocoreClientError]
    InvalidTypeNameException: Type[BotocoreClientError]
    InvalidUpdate: Type[BotocoreClientError]
    InvocationDoesNotExist: Type[BotocoreClientError]
    ItemContentMismatchException: Type[BotocoreClientError]
    ItemSizeLimitExceededException: Type[BotocoreClientError]
    MaxDocumentSizeExceeded: Type[BotocoreClientError]
    OpsItemAlreadyExistsException: Type[BotocoreClientError]
    OpsItemInvalidParameterException: Type[BotocoreClientError]
    OpsItemLimitExceededException: Type[BotocoreClientError]
    OpsItemNotFoundException: Type[BotocoreClientError]
    ParameterAlreadyExists: Type[BotocoreClientError]
    ParameterLimitExceeded: Type[BotocoreClientError]
    ParameterMaxVersionLimitExceeded: Type[BotocoreClientError]
    ParameterNotFound: Type[BotocoreClientError]
    ParameterPatternMismatchException: Type[BotocoreClientError]
    ParameterVersionLabelLimitExceeded: Type[BotocoreClientError]
    ParameterVersionNotFound: Type[BotocoreClientError]
    PoliciesLimitExceededException: Type[BotocoreClientError]
    ResourceDataSyncAlreadyExistsException: Type[BotocoreClientError]
    ResourceDataSyncConflictException: Type[BotocoreClientError]
    ResourceDataSyncCountExceededException: Type[BotocoreClientError]
    ResourceDataSyncInvalidConfigurationException: Type[BotocoreClientError]
    ResourceDataSyncNotFoundException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ServiceSettingNotFound: Type[BotocoreClientError]
    StatusUnchanged: Type[BotocoreClientError]
    SubTypeCountLimitExceededException: Type[BotocoreClientError]
    TargetInUseException: Type[BotocoreClientError]
    TargetNotConnected: Type[BotocoreClientError]
    TooManyTagsError: Type[BotocoreClientError]
    TooManyUpdates: Type[BotocoreClientError]
    TotalSizeLimitExceededException: Type[BotocoreClientError]
    UnsupportedCalendarException: Type[BotocoreClientError]
    UnsupportedFeatureRequiredException: Type[BotocoreClientError]
    UnsupportedInventoryItemContextException: Type[BotocoreClientError]
    UnsupportedInventorySchemaVersionException: Type[BotocoreClientError]
    UnsupportedOperatingSystem: Type[BotocoreClientError]
    UnsupportedParameterType: Type[BotocoreClientError]
    UnsupportedPlatformType: Type[BotocoreClientError]


class SSMClient:
    """
    [SSM.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_tags_to_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
        Tags: List["TagTypeDef"],
    ) -> Dict[str, Any]:
        """
        [Client.add_tags_to_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.add_tags_to_resource)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.can_paginate)
        """

    def cancel_command(self, CommandId: str, InstanceIds: List[str] = None) -> Dict[str, Any]:
        """
        [Client.cancel_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.cancel_command)
        """

    def cancel_maintenance_window_execution(
        self, WindowExecutionId: str
    ) -> CancelMaintenanceWindowExecutionResultTypeDef:
        """
        [Client.cancel_maintenance_window_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.cancel_maintenance_window_execution)
        """

    def create_activation(
        self,
        IamRole: str,
        Description: str = None,
        DefaultInstanceName: str = None,
        RegistrationLimit: int = None,
        ExpirationDate: datetime = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateActivationResultTypeDef:
        """
        [Client.create_activation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.create_activation)
        """

    def create_association(
        self,
        Name: str,
        DocumentVersion: str = None,
        InstanceId: str = None,
        Parameters: Dict[str, List[str]] = None,
        Targets: List["TargetTypeDef"] = None,
        ScheduleExpression: str = None,
        OutputLocation: "InstanceAssociationOutputLocationTypeDef" = None,
        AssociationName: str = None,
        AutomationTargetParameterName: str = None,
        MaxErrors: str = None,
        MaxConcurrency: str = None,
        ComplianceSeverity: Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"] = None,
        SyncCompliance: Literal["AUTO", "MANUAL"] = None,
        ApplyOnlyAtCronInterval: bool = None,
    ) -> CreateAssociationResultTypeDef:
        """
        [Client.create_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.create_association)
        """

    def create_association_batch(
        self, Entries: List["CreateAssociationBatchRequestEntryTypeDef"]
    ) -> CreateAssociationBatchResultTypeDef:
        """
        [Client.create_association_batch documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.create_association_batch)
        """

    def create_document(
        self,
        Content: str,
        Name: str,
        Requires: List["DocumentRequiresTypeDef"] = None,
        Attachments: List[AttachmentsSourceTypeDef] = None,
        VersionName: str = None,
        DocumentType: Literal[
            "Command",
            "Policy",
            "Automation",
            "Session",
            "Package",
            "ApplicationConfiguration",
            "ApplicationConfigurationSchema",
            "DeploymentStrategy",
            "ChangeCalendar",
        ] = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
        TargetType: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDocumentResultTypeDef:
        """
        [Client.create_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.create_document)
        """

    def create_maintenance_window(
        self,
        Name: str,
        Schedule: str,
        Duration: int,
        Cutoff: int,
        AllowUnassociatedTargets: bool,
        Description: str = None,
        StartDate: str = None,
        EndDate: str = None,
        ScheduleTimezone: str = None,
        ScheduleOffset: int = None,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateMaintenanceWindowResultTypeDef:
        """
        [Client.create_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.create_maintenance_window)
        """

    def create_ops_item(
        self,
        Description: str,
        Source: str,
        Title: str,
        OperationalData: Dict[str, "OpsItemDataValueTypeDef"] = None,
        Notifications: List["OpsItemNotificationTypeDef"] = None,
        Priority: int = None,
        RelatedOpsItems: List["RelatedOpsItemTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        Category: str = None,
        Severity: str = None,
    ) -> CreateOpsItemResponseTypeDef:
        """
        [Client.create_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.create_ops_item)
        """

    def create_patch_baseline(
        self,
        Name: str,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
            "ORACLE_LINUX",
            "DEBIAN",
        ] = None,
        GlobalFilters: "PatchFilterGroupTypeDef" = None,
        ApprovalRules: "PatchRuleGroupTypeDef" = None,
        ApprovedPatches: List[str] = None,
        ApprovedPatchesComplianceLevel: Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ] = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[str] = None,
        RejectedPatchesAction: Literal["ALLOW_AS_DEPENDENCY", "BLOCK"] = None,
        Description: str = None,
        Sources: List["PatchSourceTypeDef"] = None,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreatePatchBaselineResultTypeDef:
        """
        [Client.create_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.create_patch_baseline)
        """

    def create_resource_data_sync(
        self,
        SyncName: str,
        S3Destination: "ResourceDataSyncS3DestinationTypeDef" = None,
        SyncType: str = None,
        SyncSource: ResourceDataSyncSourceTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Client.create_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.create_resource_data_sync)
        """

    def delete_activation(self, ActivationId: str) -> Dict[str, Any]:
        """
        [Client.delete_activation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_activation)
        """

    def delete_association(
        self, Name: str = None, InstanceId: str = None, AssociationId: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_association)
        """

    def delete_document(
        self, Name: str, DocumentVersion: str = None, VersionName: str = None, Force: bool = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_document)
        """

    def delete_inventory(
        self,
        TypeName: str,
        SchemaDeleteOption: Literal["DisableSchema", "DeleteSchema"] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> DeleteInventoryResultTypeDef:
        """
        [Client.delete_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_inventory)
        """

    def delete_maintenance_window(self, WindowId: str) -> DeleteMaintenanceWindowResultTypeDef:
        """
        [Client.delete_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_maintenance_window)
        """

    def delete_parameter(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_parameter)
        """

    def delete_parameters(self, Names: List[str]) -> DeleteParametersResultTypeDef:
        """
        [Client.delete_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_parameters)
        """

    def delete_patch_baseline(self, BaselineId: str) -> DeletePatchBaselineResultTypeDef:
        """
        [Client.delete_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_patch_baseline)
        """

    def delete_resource_data_sync(self, SyncName: str, SyncType: str = None) -> Dict[str, Any]:
        """
        [Client.delete_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.delete_resource_data_sync)
        """

    def deregister_managed_instance(self, InstanceId: str) -> Dict[str, Any]:
        """
        [Client.deregister_managed_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.deregister_managed_instance)
        """

    def deregister_patch_baseline_for_patch_group(
        self, BaselineId: str, PatchGroup: str
    ) -> DeregisterPatchBaselineForPatchGroupResultTypeDef:
        """
        [Client.deregister_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.deregister_patch_baseline_for_patch_group)
        """

    def deregister_target_from_maintenance_window(
        self, WindowId: str, WindowTargetId: str, Safe: bool = None
    ) -> DeregisterTargetFromMaintenanceWindowResultTypeDef:
        """
        [Client.deregister_target_from_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.deregister_target_from_maintenance_window)
        """

    def deregister_task_from_maintenance_window(
        self, WindowId: str, WindowTaskId: str
    ) -> DeregisterTaskFromMaintenanceWindowResultTypeDef:
        """
        [Client.deregister_task_from_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.deregister_task_from_maintenance_window)
        """

    def describe_activations(
        self,
        Filters: List[DescribeActivationsFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeActivationsResultTypeDef:
        """
        [Client.describe_activations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_activations)
        """

    def describe_association(
        self,
        Name: str = None,
        InstanceId: str = None,
        AssociationId: str = None,
        AssociationVersion: str = None,
    ) -> DescribeAssociationResultTypeDef:
        """
        [Client.describe_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_association)
        """

    def describe_association_execution_targets(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[AssociationExecutionTargetsFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAssociationExecutionTargetsResultTypeDef:
        """
        [Client.describe_association_execution_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_association_execution_targets)
        """

    def describe_association_executions(
        self,
        AssociationId: str,
        Filters: List[AssociationExecutionFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAssociationExecutionsResultTypeDef:
        """
        [Client.describe_association_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_association_executions)
        """

    def describe_automation_executions(
        self,
        Filters: List[AutomationExecutionFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAutomationExecutionsResultTypeDef:
        """
        [Client.describe_automation_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_automation_executions)
        """

    def describe_automation_step_executions(
        self,
        AutomationExecutionId: str,
        Filters: List[StepExecutionFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
        ReverseOrder: bool = None,
    ) -> DescribeAutomationStepExecutionsResultTypeDef:
        """
        [Client.describe_automation_step_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_automation_step_executions)
        """

    def describe_available_patches(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAvailablePatchesResultTypeDef:
        """
        [Client.describe_available_patches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_available_patches)
        """

    def describe_document(
        self, Name: str, DocumentVersion: str = None, VersionName: str = None
    ) -> DescribeDocumentResultTypeDef:
        """
        [Client.describe_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_document)
        """

    def describe_document_permission(
        self, Name: str, PermissionType: Literal["Share"]
    ) -> DescribeDocumentPermissionResponseTypeDef:
        """
        [Client.describe_document_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_document_permission)
        """

    def describe_effective_instance_associations(
        self, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeEffectiveInstanceAssociationsResultTypeDef:
        """
        [Client.describe_effective_instance_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_effective_instance_associations)
        """

    def describe_effective_patches_for_patch_baseline(
        self, BaselineId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeEffectivePatchesForPatchBaselineResultTypeDef:
        """
        [Client.describe_effective_patches_for_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_effective_patches_for_patch_baseline)
        """

    def describe_instance_associations_status(
        self, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeInstanceAssociationsStatusResultTypeDef:
        """
        [Client.describe_instance_associations_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_instance_associations_status)
        """

    def describe_instance_information(
        self,
        InstanceInformationFilterList: List[InstanceInformationFilterTypeDef] = None,
        Filters: List[InstanceInformationStringFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstanceInformationResultTypeDef:
        """
        [Client.describe_instance_information documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_instance_information)
        """

    def describe_instance_patch_states(
        self, InstanceIds: List[str], NextToken: str = None, MaxResults: int = None
    ) -> DescribeInstancePatchStatesResultTypeDef:
        """
        [Client.describe_instance_patch_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_instance_patch_states)
        """

    def describe_instance_patch_states_for_patch_group(
        self,
        PatchGroup: str,
        Filters: List[InstancePatchStateFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeInstancePatchStatesForPatchGroupResultTypeDef:
        """
        [Client.describe_instance_patch_states_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_instance_patch_states_for_patch_group)
        """

    def describe_instance_patches(
        self,
        InstanceId: str,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeInstancePatchesResultTypeDef:
        """
        [Client.describe_instance_patches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_instance_patches)
        """

    def describe_inventory_deletions(
        self, DeletionId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeInventoryDeletionsResultTypeDef:
        """
        [Client.describe_inventory_deletions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_inventory_deletions)
        """

    def describe_maintenance_window_execution_task_invocations(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef:
        """
        [Client.describe_maintenance_window_execution_task_invocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_task_invocations)
        """

    def describe_maintenance_window_execution_tasks(
        self,
        WindowExecutionId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowExecutionTasksResultTypeDef:
        """
        [Client.describe_maintenance_window_execution_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_tasks)
        """

    def describe_maintenance_window_executions(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowExecutionsResultTypeDef:
        """
        [Client.describe_maintenance_window_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_maintenance_window_executions)
        """

    def describe_maintenance_window_schedule(
        self,
        WindowId: str = None,
        Targets: List["TargetTypeDef"] = None,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"] = None,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowScheduleResultTypeDef:
        """
        [Client.describe_maintenance_window_schedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_maintenance_window_schedule)
        """

    def describe_maintenance_window_targets(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowTargetsResultTypeDef:
        """
        [Client.describe_maintenance_window_targets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_maintenance_window_targets)
        """

    def describe_maintenance_window_tasks(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowTasksResultTypeDef:
        """
        [Client.describe_maintenance_window_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_maintenance_window_tasks)
        """

    def describe_maintenance_windows(
        self,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowsResultTypeDef:
        """
        [Client.describe_maintenance_windows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_maintenance_windows)
        """

    def describe_maintenance_windows_for_target(
        self,
        Targets: List["TargetTypeDef"],
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeMaintenanceWindowsForTargetResultTypeDef:
        """
        [Client.describe_maintenance_windows_for_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_maintenance_windows_for_target)
        """

    def describe_ops_items(
        self,
        OpsItemFilters: List[OpsItemFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeOpsItemsResponseTypeDef:
        """
        [Client.describe_ops_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_ops_items)
        """

    def describe_parameters(
        self,
        Filters: List[ParametersFilterTypeDef] = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeParametersResultTypeDef:
        """
        [Client.describe_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_parameters)
        """

    def describe_patch_baselines(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribePatchBaselinesResultTypeDef:
        """
        [Client.describe_patch_baselines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_patch_baselines)
        """

    def describe_patch_group_state(self, PatchGroup: str) -> DescribePatchGroupStateResultTypeDef:
        """
        [Client.describe_patch_group_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_patch_group_state)
        """

    def describe_patch_groups(
        self,
        MaxResults: int = None,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        NextToken: str = None,
    ) -> DescribePatchGroupsResultTypeDef:
        """
        [Client.describe_patch_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_patch_groups)
        """

    def describe_patch_properties(
        self,
        OperatingSystem: Literal[
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
        Property: Literal[
            "PRODUCT", "PRODUCT_FAMILY", "CLASSIFICATION", "MSRC_SEVERITY", "PRIORITY", "SEVERITY"
        ],
        PatchSet: Literal["OS", "APPLICATION"] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribePatchPropertiesResultTypeDef:
        """
        [Client.describe_patch_properties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_patch_properties)
        """

    def describe_sessions(
        self,
        State: Literal["Active", "History"],
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[SessionFilterTypeDef] = None,
    ) -> DescribeSessionsResponseTypeDef:
        """
        [Client.describe_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.describe_sessions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.generate_presigned_url)
        """

    def get_automation_execution(
        self, AutomationExecutionId: str
    ) -> GetAutomationExecutionResultTypeDef:
        """
        [Client.get_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_automation_execution)
        """

    def get_calendar_state(
        self, CalendarNames: List[str], AtTime: str = None
    ) -> GetCalendarStateResponseTypeDef:
        """
        [Client.get_calendar_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_calendar_state)
        """

    def get_command_invocation(
        self, CommandId: str, InstanceId: str, PluginName: str = None
    ) -> GetCommandInvocationResultTypeDef:
        """
        [Client.get_command_invocation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_command_invocation)
        """

    def get_connection_status(self, Target: str) -> GetConnectionStatusResponseTypeDef:
        """
        [Client.get_connection_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_connection_status)
        """

    def get_default_patch_baseline(
        self,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
            "ORACLE_LINUX",
            "DEBIAN",
        ] = None,
    ) -> GetDefaultPatchBaselineResultTypeDef:
        """
        [Client.get_default_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_default_patch_baseline)
        """

    def get_deployable_patch_snapshot_for_instance(
        self, InstanceId: str, SnapshotId: str
    ) -> GetDeployablePatchSnapshotForInstanceResultTypeDef:
        """
        [Client.get_deployable_patch_snapshot_for_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_deployable_patch_snapshot_for_instance)
        """

    def get_document(
        self,
        Name: str,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
    ) -> GetDocumentResultTypeDef:
        """
        [Client.get_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_document)
        """

    def get_inventory(
        self,
        Filters: List["InventoryFilterTypeDef"] = None,
        Aggregators: List[Dict[str, Any]] = None,
        ResultAttributes: List[ResultAttributeTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetInventoryResultTypeDef:
        """
        [Client.get_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_inventory)
        """

    def get_inventory_schema(
        self,
        TypeName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Aggregator: bool = None,
        SubType: bool = None,
    ) -> GetInventorySchemaResultTypeDef:
        """
        [Client.get_inventory_schema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_inventory_schema)
        """

    def get_maintenance_window(self, WindowId: str) -> GetMaintenanceWindowResultTypeDef:
        """
        [Client.get_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_maintenance_window)
        """

    def get_maintenance_window_execution(
        self, WindowExecutionId: str
    ) -> GetMaintenanceWindowExecutionResultTypeDef:
        """
        [Client.get_maintenance_window_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution)
        """

    def get_maintenance_window_execution_task(
        self, WindowExecutionId: str, TaskId: str
    ) -> GetMaintenanceWindowExecutionTaskResultTypeDef:
        """
        [Client.get_maintenance_window_execution_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task)
        """

    def get_maintenance_window_execution_task_invocation(
        self, WindowExecutionId: str, TaskId: str, InvocationId: str
    ) -> GetMaintenanceWindowExecutionTaskInvocationResultTypeDef:
        """
        [Client.get_maintenance_window_execution_task_invocation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task_invocation)
        """

    def get_maintenance_window_task(
        self, WindowId: str, WindowTaskId: str
    ) -> GetMaintenanceWindowTaskResultTypeDef:
        """
        [Client.get_maintenance_window_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_maintenance_window_task)
        """

    def get_ops_item(self, OpsItemId: str) -> GetOpsItemResponseTypeDef:
        """
        [Client.get_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_ops_item)
        """

    def get_ops_summary(
        self,
        SyncName: str = None,
        Filters: List["OpsFilterTypeDef"] = None,
        Aggregators: List[Dict[str, Any]] = None,
        ResultAttributes: List[OpsResultAttributeTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetOpsSummaryResultTypeDef:
        """
        [Client.get_ops_summary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_ops_summary)
        """

    def get_parameter(self, Name: str, WithDecryption: bool = None) -> GetParameterResultTypeDef:
        """
        [Client.get_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_parameter)
        """

    def get_parameter_history(
        self, Name: str, WithDecryption: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> GetParameterHistoryResultTypeDef:
        """
        [Client.get_parameter_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_parameter_history)
        """

    def get_parameters(
        self, Names: List[str], WithDecryption: bool = None
    ) -> GetParametersResultTypeDef:
        """
        [Client.get_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_parameters)
        """

    def get_parameters_by_path(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        WithDecryption: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetParametersByPathResultTypeDef:
        """
        [Client.get_parameters_by_path documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_parameters_by_path)
        """

    def get_patch_baseline(self, BaselineId: str) -> GetPatchBaselineResultTypeDef:
        """
        [Client.get_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_patch_baseline)
        """

    def get_patch_baseline_for_patch_group(
        self,
        PatchGroup: str,
        OperatingSystem: Literal[
            "WINDOWS",
            "AMAZON_LINUX",
            "AMAZON_LINUX_2",
            "UBUNTU",
            "REDHAT_ENTERPRISE_LINUX",
            "SUSE",
            "CENTOS",
            "ORACLE_LINUX",
            "DEBIAN",
        ] = None,
    ) -> GetPatchBaselineForPatchGroupResultTypeDef:
        """
        [Client.get_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_patch_baseline_for_patch_group)
        """

    def get_service_setting(self, SettingId: str) -> GetServiceSettingResultTypeDef:
        """
        [Client.get_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.get_service_setting)
        """

    def label_parameter_version(
        self, Name: str, Labels: List[str], ParameterVersion: int = None
    ) -> LabelParameterVersionResultTypeDef:
        """
        [Client.label_parameter_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.label_parameter_version)
        """

    def list_association_versions(
        self, AssociationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociationVersionsResultTypeDef:
        """
        [Client.list_association_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_association_versions)
        """

    def list_associations(
        self,
        AssociationFilterList: List[AssociationFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAssociationsResultTypeDef:
        """
        [Client.list_associations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_associations)
        """

    def list_command_invocations(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[CommandFilterTypeDef] = None,
        Details: bool = None,
    ) -> ListCommandInvocationsResultTypeDef:
        """
        [Client.list_command_invocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_command_invocations)
        """

    def list_commands(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[CommandFilterTypeDef] = None,
    ) -> ListCommandsResultTypeDef:
        """
        [Client.list_commands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_commands)
        """

    def list_compliance_items(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListComplianceItemsResultTypeDef:
        """
        [Client.list_compliance_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_compliance_items)
        """

    def list_compliance_summaries(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListComplianceSummariesResultTypeDef:
        """
        [Client.list_compliance_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_compliance_summaries)
        """

    def list_document_versions(
        self, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDocumentVersionsResultTypeDef:
        """
        [Client.list_document_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_document_versions)
        """

    def list_documents(
        self,
        DocumentFilterList: List[DocumentFilterTypeDef] = None,
        Filters: List[DocumentKeyValuesFilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListDocumentsResultTypeDef:
        """
        [Client.list_documents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_documents)
        """

    def list_inventory_entries(
        self,
        InstanceId: str,
        TypeName: str,
        Filters: List["InventoryFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListInventoryEntriesResultTypeDef:
        """
        [Client.list_inventory_entries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_inventory_entries)
        """

    def list_resource_compliance_summaries(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListResourceComplianceSummariesResultTypeDef:
        """
        [Client.list_resource_compliance_summaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_resource_compliance_summaries)
        """

    def list_resource_data_sync(
        self, SyncType: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListResourceDataSyncResultTypeDef:
        """
        [Client.list_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_resource_data_sync)
        """

    def list_tags_for_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
    ) -> ListTagsForResourceResultTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.list_tags_for_resource)
        """

    def modify_document_permission(
        self,
        Name: str,
        PermissionType: Literal["Share"],
        AccountIdsToAdd: List[str] = None,
        AccountIdsToRemove: List[str] = None,
        SharedDocumentVersion: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.modify_document_permission documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.modify_document_permission)
        """

    def put_compliance_items(
        self,
        ResourceId: str,
        ResourceType: str,
        ComplianceType: str,
        ExecutionSummary: "ComplianceExecutionSummaryTypeDef",
        Items: List[ComplianceItemEntryTypeDef],
        ItemContentHash: str = None,
        UploadType: Literal["COMPLETE", "PARTIAL"] = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_compliance_items documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.put_compliance_items)
        """

    def put_inventory(
        self, InstanceId: str, Items: List[InventoryItemTypeDef]
    ) -> PutInventoryResultTypeDef:
        """
        [Client.put_inventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.put_inventory)
        """

    def put_parameter(
        self,
        Name: str,
        Value: str,
        Description: str = None,
        Type: Literal["String", "StringList", "SecureString"] = None,
        KeyId: str = None,
        Overwrite: bool = None,
        AllowedPattern: str = None,
        Tags: List["TagTypeDef"] = None,
        Tier: Literal["Standard", "Advanced", "Intelligent-Tiering"] = None,
        Policies: str = None,
        DataType: str = None,
    ) -> PutParameterResultTypeDef:
        """
        [Client.put_parameter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.put_parameter)
        """

    def register_default_patch_baseline(
        self, BaselineId: str
    ) -> RegisterDefaultPatchBaselineResultTypeDef:
        """
        [Client.register_default_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.register_default_patch_baseline)
        """

    def register_patch_baseline_for_patch_group(
        self, BaselineId: str, PatchGroup: str
    ) -> RegisterPatchBaselineForPatchGroupResultTypeDef:
        """
        [Client.register_patch_baseline_for_patch_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.register_patch_baseline_for_patch_group)
        """

    def register_target_with_maintenance_window(
        self,
        WindowId: str,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        Targets: List["TargetTypeDef"],
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> RegisterTargetWithMaintenanceWindowResultTypeDef:
        """
        [Client.register_target_with_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.register_target_with_maintenance_window)
        """

    def register_task_with_maintenance_window(
        self,
        WindowId: str,
        Targets: List["TargetTypeDef"],
        TaskArn: str,
        TaskType: Literal["RUN_COMMAND", "AUTOMATION", "STEP_FUNCTIONS", "LAMBDA"],
        MaxConcurrency: str,
        MaxErrors: str,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"] = None,
        TaskInvocationParameters: "MaintenanceWindowTaskInvocationParametersTypeDef" = None,
        Priority: int = None,
        LoggingInfo: "LoggingInfoTypeDef" = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
    ) -> RegisterTaskWithMaintenanceWindowResultTypeDef:
        """
        [Client.register_task_with_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.register_task_with_maintenance_window)
        """

    def remove_tags_from_resource(
        self,
        ResourceType: Literal[
            "Document",
            "ManagedInstance",
            "MaintenanceWindow",
            "Parameter",
            "PatchBaseline",
            "OpsItem",
        ],
        ResourceId: str,
        TagKeys: List[str],
    ) -> Dict[str, Any]:
        """
        [Client.remove_tags_from_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.remove_tags_from_resource)
        """

    def reset_service_setting(self, SettingId: str) -> ResetServiceSettingResultTypeDef:
        """
        [Client.reset_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.reset_service_setting)
        """

    def resume_session(self, SessionId: str) -> ResumeSessionResponseTypeDef:
        """
        [Client.resume_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.resume_session)
        """

    def send_automation_signal(
        self,
        AutomationExecutionId: str,
        SignalType: Literal["Approve", "Reject", "StartStep", "StopStep", "Resume"],
        Payload: Dict[str, List[str]] = None,
    ) -> Dict[str, Any]:
        """
        [Client.send_automation_signal documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.send_automation_signal)
        """

    def send_command(
        self,
        DocumentName: str,
        InstanceIds: List[str] = None,
        Targets: List["TargetTypeDef"] = None,
        DocumentVersion: str = None,
        DocumentHash: str = None,
        DocumentHashType: Literal["Sha256", "Sha1"] = None,
        TimeoutSeconds: int = None,
        Comment: str = None,
        Parameters: Dict[str, List[str]] = None,
        OutputS3Region: str = None,
        OutputS3BucketName: str = None,
        OutputS3KeyPrefix: str = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        ServiceRoleArn: str = None,
        NotificationConfig: "NotificationConfigTypeDef" = None,
        CloudWatchOutputConfig: "CloudWatchOutputConfigTypeDef" = None,
    ) -> SendCommandResultTypeDef:
        """
        [Client.send_command documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.send_command)
        """

    def start_associations_once(self, AssociationIds: List[str]) -> Dict[str, Any]:
        """
        [Client.start_associations_once documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.start_associations_once)
        """

    def start_automation_execution(
        self,
        DocumentName: str,
        DocumentVersion: str = None,
        Parameters: Dict[str, List[str]] = None,
        ClientToken: str = None,
        Mode: Literal["Auto", "Interactive"] = None,
        TargetParameterName: str = None,
        Targets: List["TargetTypeDef"] = None,
        TargetMaps: List[Dict[str, List[str]]] = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        TargetLocations: List["TargetLocationTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> StartAutomationExecutionResultTypeDef:
        """
        [Client.start_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.start_automation_execution)
        """

    def start_session(
        self, Target: str, DocumentName: str = None, Parameters: Dict[str, List[str]] = None
    ) -> StartSessionResponseTypeDef:
        """
        [Client.start_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.start_session)
        """

    def stop_automation_execution(
        self, AutomationExecutionId: str, Type: Literal["Complete", "Cancel"] = None
    ) -> Dict[str, Any]:
        """
        [Client.stop_automation_execution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.stop_automation_execution)
        """

    def terminate_session(self, SessionId: str) -> TerminateSessionResponseTypeDef:
        """
        [Client.terminate_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.terminate_session)
        """

    def update_association(
        self,
        AssociationId: str,
        Parameters: Dict[str, List[str]] = None,
        DocumentVersion: str = None,
        ScheduleExpression: str = None,
        OutputLocation: "InstanceAssociationOutputLocationTypeDef" = None,
        Name: str = None,
        Targets: List["TargetTypeDef"] = None,
        AssociationName: str = None,
        AssociationVersion: str = None,
        AutomationTargetParameterName: str = None,
        MaxErrors: str = None,
        MaxConcurrency: str = None,
        ComplianceSeverity: Literal["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNSPECIFIED"] = None,
        SyncCompliance: Literal["AUTO", "MANUAL"] = None,
        ApplyOnlyAtCronInterval: bool = None,
    ) -> UpdateAssociationResultTypeDef:
        """
        [Client.update_association documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_association)
        """

    def update_association_status(
        self, Name: str, InstanceId: str, AssociationStatus: "AssociationStatusTypeDef"
    ) -> UpdateAssociationStatusResultTypeDef:
        """
        [Client.update_association_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_association_status)
        """

    def update_document(
        self,
        Content: str,
        Name: str,
        Attachments: List[AttachmentsSourceTypeDef] = None,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: Literal["YAML", "JSON", "TEXT"] = None,
        TargetType: str = None,
    ) -> UpdateDocumentResultTypeDef:
        """
        [Client.update_document documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_document)
        """

    def update_document_default_version(
        self, Name: str, DocumentVersion: str
    ) -> UpdateDocumentDefaultVersionResultTypeDef:
        """
        [Client.update_document_default_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_document_default_version)
        """

    def update_maintenance_window(
        self,
        WindowId: str,
        Name: str = None,
        Description: str = None,
        StartDate: str = None,
        EndDate: str = None,
        Schedule: str = None,
        ScheduleTimezone: str = None,
        ScheduleOffset: int = None,
        Duration: int = None,
        Cutoff: int = None,
        AllowUnassociatedTargets: bool = None,
        Enabled: bool = None,
        Replace: bool = None,
    ) -> UpdateMaintenanceWindowResultTypeDef:
        """
        [Client.update_maintenance_window documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_maintenance_window)
        """

    def update_maintenance_window_target(
        self,
        WindowId: str,
        WindowTargetId: str,
        Targets: List["TargetTypeDef"] = None,
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None,
    ) -> UpdateMaintenanceWindowTargetResultTypeDef:
        """
        [Client.update_maintenance_window_target documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_maintenance_window_target)
        """

    def update_maintenance_window_task(
        self,
        WindowId: str,
        WindowTaskId: str,
        Targets: List["TargetTypeDef"] = None,
        TaskArn: str = None,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"] = None,
        TaskInvocationParameters: "MaintenanceWindowTaskInvocationParametersTypeDef" = None,
        Priority: int = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        LoggingInfo: "LoggingInfoTypeDef" = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None,
    ) -> UpdateMaintenanceWindowTaskResultTypeDef:
        """
        [Client.update_maintenance_window_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_maintenance_window_task)
        """

    def update_managed_instance_role(self, InstanceId: str, IamRole: str) -> Dict[str, Any]:
        """
        [Client.update_managed_instance_role documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_managed_instance_role)
        """

    def update_ops_item(
        self,
        OpsItemId: str,
        Description: str = None,
        OperationalData: Dict[str, "OpsItemDataValueTypeDef"] = None,
        OperationalDataToDelete: List[str] = None,
        Notifications: List["OpsItemNotificationTypeDef"] = None,
        Priority: int = None,
        RelatedOpsItems: List["RelatedOpsItemTypeDef"] = None,
        Status: Literal["Open", "InProgress", "Resolved"] = None,
        Title: str = None,
        Category: str = None,
        Severity: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.update_ops_item documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_ops_item)
        """

    def update_patch_baseline(
        self,
        BaselineId: str,
        Name: str = None,
        GlobalFilters: "PatchFilterGroupTypeDef" = None,
        ApprovalRules: "PatchRuleGroupTypeDef" = None,
        ApprovedPatches: List[str] = None,
        ApprovedPatchesComplianceLevel: Literal[
            "CRITICAL", "HIGH", "MEDIUM", "LOW", "INFORMATIONAL", "UNSPECIFIED"
        ] = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[str] = None,
        RejectedPatchesAction: Literal["ALLOW_AS_DEPENDENCY", "BLOCK"] = None,
        Description: str = None,
        Sources: List["PatchSourceTypeDef"] = None,
        Replace: bool = None,
    ) -> UpdatePatchBaselineResultTypeDef:
        """
        [Client.update_patch_baseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_patch_baseline)
        """

    def update_resource_data_sync(
        self, SyncName: str, SyncType: str, SyncSource: ResourceDataSyncSourceTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_resource_data_sync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_resource_data_sync)
        """

    def update_service_setting(self, SettingId: str, SettingValue: str) -> Dict[str, Any]:
        """
        [Client.update_service_setting documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Client.update_service_setting)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_activations"]
    ) -> DescribeActivationsPaginator:
        """
        [Paginator.DescribeActivations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeActivations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_association_execution_targets"]
    ) -> DescribeAssociationExecutionTargetsPaginator:
        """
        [Paginator.DescribeAssociationExecutionTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_association_executions"]
    ) -> DescribeAssociationExecutionsPaginator:
        """
        [Paginator.DescribeAssociationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_automation_executions"]
    ) -> DescribeAutomationExecutionsPaginator:
        """
        [Paginator.DescribeAutomationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_automation_step_executions"]
    ) -> DescribeAutomationStepExecutionsPaginator:
        """
        [Paginator.DescribeAutomationStepExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_available_patches"]
    ) -> DescribeAvailablePatchesPaginator:
        """
        [Paginator.DescribeAvailablePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_effective_instance_associations"]
    ) -> DescribeEffectiveInstanceAssociationsPaginator:
        """
        [Paginator.DescribeEffectiveInstanceAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_effective_patches_for_patch_baseline"]
    ) -> DescribeEffectivePatchesForPatchBaselinePaginator:
        """
        [Paginator.DescribeEffectivePatchesForPatchBaseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_associations_status"]
    ) -> DescribeInstanceAssociationsStatusPaginator:
        """
        [Paginator.DescribeInstanceAssociationsStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_information"]
    ) -> DescribeInstanceInformationPaginator:
        """
        [Paginator.DescribeInstanceInformation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patch_states"]
    ) -> DescribeInstancePatchStatesPaginator:
        """
        [Paginator.DescribeInstancePatchStates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patch_states_for_patch_group"]
    ) -> DescribeInstancePatchStatesForPatchGroupPaginator:
        """
        [Paginator.DescribeInstancePatchStatesForPatchGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patches"]
    ) -> DescribeInstancePatchesPaginator:
        """
        [Paginator.DescribeInstancePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_inventory_deletions"]
    ) -> DescribeInventoryDeletionsPaginator:
        """
        [Paginator.DescribeInventoryDeletions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_execution_task_invocations"]
    ) -> DescribeMaintenanceWindowExecutionTaskInvocationsPaginator:
        """
        [Paginator.DescribeMaintenanceWindowExecutionTaskInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_execution_tasks"]
    ) -> DescribeMaintenanceWindowExecutionTasksPaginator:
        """
        [Paginator.DescribeMaintenanceWindowExecutionTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_executions"]
    ) -> DescribeMaintenanceWindowExecutionsPaginator:
        """
        [Paginator.DescribeMaintenanceWindowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_schedule"]
    ) -> DescribeMaintenanceWindowSchedulePaginator:
        """
        [Paginator.DescribeMaintenanceWindowSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_targets"]
    ) -> DescribeMaintenanceWindowTargetsPaginator:
        """
        [Paginator.DescribeMaintenanceWindowTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_tasks"]
    ) -> DescribeMaintenanceWindowTasksPaginator:
        """
        [Paginator.DescribeMaintenanceWindowTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_windows"]
    ) -> DescribeMaintenanceWindowsPaginator:
        """
        [Paginator.DescribeMaintenanceWindows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_windows_for_target"]
    ) -> DescribeMaintenanceWindowsForTargetPaginator:
        """
        [Paginator.DescribeMaintenanceWindowsForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ops_items"]
    ) -> DescribeOpsItemsPaginator:
        """
        [Paginator.DescribeOpsItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeOpsItems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameters"]
    ) -> DescribeParametersPaginator:
        """
        [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_patch_baselines"]
    ) -> DescribePatchBaselinesPaginator:
        """
        [Paginator.DescribePatchBaselines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_patch_groups"]
    ) -> DescribePatchGroupsPaginator:
        """
        [Paginator.DescribePatchGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_patch_properties"]
    ) -> DescribePatchPropertiesPaginator:
        """
        [Paginator.DescribePatchProperties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchProperties)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> DescribeSessionsPaginator:
        """
        [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeSessions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_inventory"]) -> GetInventoryPaginator:
        """
        [Paginator.GetInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetInventory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_inventory_schema"]
    ) -> GetInventorySchemaPaginator:
        """
        [Paginator.GetInventorySchema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_ops_summary"]) -> GetOpsSummaryPaginator:
        """
        [Paginator.GetOpsSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetOpsSummary)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_parameter_history"]
    ) -> GetParameterHistoryPaginator:
        """
        [Paginator.GetParameterHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_parameters_by_path"]
    ) -> GetParametersByPathPaginator:
        """
        [Paginator.GetParametersByPath documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_association_versions"]
    ) -> ListAssociationVersionsPaginator:
        """
        [Paginator.ListAssociationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations"]
    ) -> ListAssociationsPaginator:
        """
        [Paginator.ListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListAssociations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_command_invocations"]
    ) -> ListCommandInvocationsPaginator:
        """
        [Paginator.ListCommandInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_commands"]) -> ListCommandsPaginator:
        """
        [Paginator.ListCommands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListCommands)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_items"]
    ) -> ListComplianceItemsPaginator:
        """
        [Paginator.ListComplianceItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_summaries"]
    ) -> ListComplianceSummariesPaginator:
        """
        [Paginator.ListComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_versions"]
    ) -> ListDocumentVersionsPaginator:
        """
        [Paginator.ListDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_documents"]) -> ListDocumentsPaginator:
        """
        [Paginator.ListDocuments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListDocuments)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_compliance_summaries"]
    ) -> ListResourceComplianceSummariesPaginator:
        """
        [Paginator.ListResourceComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_data_sync"]
    ) -> ListResourceDataSyncPaginator:
        """
        [Paginator.ListResourceDataSync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)
        """

    def get_waiter(self, waiter_name: Literal["command_executed"]) -> CommandExecutedWaiter:
        """
        [Waiter.CommandExecuted documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Waiter.CommandExecuted)
        """
