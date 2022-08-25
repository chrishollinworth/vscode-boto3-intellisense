"""
Type annotations for ssm service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ssm import SSMClient

    client: SSMClient = boto3.client("ssm")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AssociationComplianceSeverityType,
    AssociationSyncComplianceType,
    ComplianceUploadTypeType,
    DocumentFormatType,
    DocumentHashTypeType,
    DocumentTypeType,
    ExecutionModeType,
    InventorySchemaDeleteOptionType,
    MaintenanceWindowResourceTypeType,
    MaintenanceWindowTaskCutoffBehaviorType,
    MaintenanceWindowTaskTypeType,
    OperatingSystemType,
    OpsItemStatusType,
    ParameterTierType,
    ParameterTypeType,
    PatchActionType,
    PatchComplianceLevelType,
    PatchPropertyType,
    PatchSetType,
    ResourceTypeForTaggingType,
    SessionStateType,
    SignalTypeType,
    StopTypeType,
)
from .paginator import (
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
    ListOpsItemEventsPaginator,
    ListOpsItemRelatedItemsPaginator,
    ListOpsMetadataPaginator,
    ListResourceComplianceSummariesPaginator,
    ListResourceDataSyncPaginator,
)
from .type_defs import (
    AssociateOpsItemRelatedItemResponseTypeDef,
    AssociationExecutionFilterTypeDef,
    AssociationExecutionTargetsFilterTypeDef,
    AssociationFilterTypeDef,
    AssociationStatusTypeDef,
    AttachmentsSourceTypeDef,
    AutomationExecutionFilterTypeDef,
    BaselineOverrideTypeDef,
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
    CreateOpsMetadataResultTypeDef,
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
    DocumentReviewsTypeDef,
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
    GetOpsMetadataResultTypeDef,
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
    InventoryAggregatorTypeDef,
    InventoryFilterTypeDef,
    InventoryItemTypeDef,
    LabelParameterVersionResultTypeDef,
    ListAssociationsResultTypeDef,
    ListAssociationVersionsResultTypeDef,
    ListCommandInvocationsResultTypeDef,
    ListCommandsResultTypeDef,
    ListComplianceItemsResultTypeDef,
    ListComplianceSummariesResultTypeDef,
    ListDocumentMetadataHistoryResponseTypeDef,
    ListDocumentsResultTypeDef,
    ListDocumentVersionsResultTypeDef,
    ListInventoryEntriesResultTypeDef,
    ListOpsItemEventsResponseTypeDef,
    ListOpsItemRelatedItemsResponseTypeDef,
    ListOpsMetadataResultTypeDef,
    ListResourceComplianceSummariesResultTypeDef,
    ListResourceDataSyncResultTypeDef,
    ListTagsForResourceResultTypeDef,
    LoggingInfoTypeDef,
    MaintenanceWindowFilterTypeDef,
    MaintenanceWindowTaskInvocationParametersTypeDef,
    MaintenanceWindowTaskParameterValueExpressionTypeDef,
    MetadataValueTypeDef,
    NotificationConfigTypeDef,
    OpsAggregatorTypeDef,
    OpsFilterTypeDef,
    OpsItemDataValueTypeDef,
    OpsItemEventFilterTypeDef,
    OpsItemFilterTypeDef,
    OpsItemNotificationTypeDef,
    OpsItemRelatedItemsFilterTypeDef,
    OpsMetadataFilterTypeDef,
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
    RegistrationMetadataItemTypeDef,
    RelatedOpsItemTypeDef,
    ResetServiceSettingResultTypeDef,
    ResourceDataSyncS3DestinationTypeDef,
    ResourceDataSyncSourceTypeDef,
    ResultAttributeTypeDef,
    ResumeSessionResponseTypeDef,
    RunbookTypeDef,
    SendCommandResultTypeDef,
    SessionFilterTypeDef,
    StartAutomationExecutionResultTypeDef,
    StartChangeRequestExecutionResultTypeDef,
    StartSessionResponseTypeDef,
    StepExecutionFilterTypeDef,
    TagTypeDef,
    TargetLocationTypeDef,
    TargetTypeDef,
    TerminateSessionResponseTypeDef,
    UnlabelParameterVersionResultTypeDef,
    UpdateAssociationResultTypeDef,
    UpdateAssociationStatusResultTypeDef,
    UpdateDocumentDefaultVersionResultTypeDef,
    UpdateDocumentResultTypeDef,
    UpdateMaintenanceWindowResultTypeDef,
    UpdateMaintenanceWindowTargetResultTypeDef,
    UpdateMaintenanceWindowTaskResultTypeDef,
    UpdateOpsMetadataResultTypeDef,
    UpdatePatchBaselineResultTypeDef,
)
from .waiter import CommandExecutedWaiter

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
    AutomationDefinitionNotApprovedException: Type[BotocoreClientError]
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
    InvalidTargetMaps: Type[BotocoreClientError]
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
    OpsItemRelatedItemAlreadyExistsException: Type[BotocoreClientError]
    OpsItemRelatedItemAssociationNotFoundException: Type[BotocoreClientError]
    OpsMetadataAlreadyExistsException: Type[BotocoreClientError]
    OpsMetadataInvalidArgumentException: Type[BotocoreClientError]
    OpsMetadataKeyLimitExceededException: Type[BotocoreClientError]
    OpsMetadataLimitExceededException: Type[BotocoreClientError]
    OpsMetadataNotFoundException: Type[BotocoreClientError]
    OpsMetadataTooManyUpdatesException: Type[BotocoreClientError]
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

class SSMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSMClient exceptions.
        """
    def add_tags_to_resource(
        self, *, ResourceType: ResourceTypeForTaggingType, ResourceId: str, Tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.add_tags_to_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#add_tags_to_resource)
        """
    def associate_ops_item_related_item(
        self, *, OpsItemId: str, AssociationType: str, ResourceType: str, ResourceUri: str
    ) -> AssociateOpsItemRelatedItemResponseTypeDef:
        """
        Associates a related item to a Systems Manager OpsCenter OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.associate_ops_item_related_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#associate_ops_item_related_item)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#can_paginate)
        """
    def cancel_command(self, *, CommandId: str, InstanceIds: List[str] = None) -> Dict[str, Any]:
        """
        Attempts to cancel the command specified by the Command ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.cancel_command)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#cancel_command)
        """
    def cancel_maintenance_window_execution(
        self, *, WindowExecutionId: str
    ) -> CancelMaintenanceWindowExecutionResultTypeDef:
        """
        Stops a maintenance window execution that is already in progress and cancels any
        tasks in the window that haven't already starting running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.cancel_maintenance_window_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#cancel_maintenance_window_execution)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#close)
        """
    def create_activation(
        self,
        *,
        IamRole: str,
        Description: str = None,
        DefaultInstanceName: str = None,
        RegistrationLimit: int = None,
        ExpirationDate: Union[datetime, str] = None,
        Tags: List["TagTypeDef"] = None,
        RegistrationMetadata: List["RegistrationMetadataItemTypeDef"] = None
    ) -> CreateActivationResultTypeDef:
        """
        Generates an activation code and activation ID you can use to register your on-
        premises servers, edge devices, or virtual machine (VM) with Amazon Web Services
        Systems Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_activation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_activation)
        """
    def create_association(
        self,
        *,
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
        ComplianceSeverity: AssociationComplianceSeverityType = None,
        SyncCompliance: AssociationSyncComplianceType = None,
        ApplyOnlyAtCronInterval: bool = None,
        CalendarNames: List[str] = None,
        TargetLocations: List["TargetLocationTypeDef"] = None,
        ScheduleOffset: int = None,
        TargetMaps: List[Dict[str, List[str]]] = None
    ) -> CreateAssociationResultTypeDef:
        """
        A State Manager association defines the state that you want to maintain on your
        managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_association)
        """
    def create_association_batch(
        self, *, Entries: List["CreateAssociationBatchRequestEntryTypeDef"]
    ) -> CreateAssociationBatchResultTypeDef:
        """
        Associates the specified Amazon Web Services Systems Manager document (SSM
        document) with the specified managed nodes or targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_association_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_association_batch)
        """
    def create_document(
        self,
        *,
        Content: str,
        Name: str,
        Requires: List["DocumentRequiresTypeDef"] = None,
        Attachments: List["AttachmentsSourceTypeDef"] = None,
        DisplayName: str = None,
        VersionName: str = None,
        DocumentType: DocumentTypeType = None,
        DocumentFormat: DocumentFormatType = None,
        TargetType: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateDocumentResultTypeDef:
        """
        Creates a Amazon Web Services Systems Manager (SSM document).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_document)
        """
    def create_maintenance_window(
        self,
        *,
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
        Tags: List["TagTypeDef"] = None
    ) -> CreateMaintenanceWindowResultTypeDef:
        """
        Creates a new maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_maintenance_window)
        """
    def create_ops_item(
        self,
        *,
        Description: str,
        Source: str,
        Title: str,
        OpsItemType: str = None,
        OperationalData: Dict[str, "OpsItemDataValueTypeDef"] = None,
        Notifications: List["OpsItemNotificationTypeDef"] = None,
        Priority: int = None,
        RelatedOpsItems: List["RelatedOpsItemTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        Category: str = None,
        Severity: str = None,
        ActualStartTime: Union[datetime, str] = None,
        ActualEndTime: Union[datetime, str] = None,
        PlannedStartTime: Union[datetime, str] = None,
        PlannedEndTime: Union[datetime, str] = None
    ) -> CreateOpsItemResponseTypeDef:
        """
        Creates a new OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_ops_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_ops_item)
        """
    def create_ops_metadata(
        self,
        *,
        ResourceId: str,
        Metadata: Dict[str, "MetadataValueTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreateOpsMetadataResultTypeDef:
        """
        If you create a new application in Application Manager, Amazon Web Services
        Systems Manager calls this API operation to specify information about the new
        application, including the application type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_ops_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_ops_metadata)
        """
    def create_patch_baseline(
        self,
        *,
        Name: str,
        OperatingSystem: OperatingSystemType = None,
        GlobalFilters: "PatchFilterGroupTypeDef" = None,
        ApprovalRules: "PatchRuleGroupTypeDef" = None,
        ApprovedPatches: List[str] = None,
        ApprovedPatchesComplianceLevel: PatchComplianceLevelType = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[str] = None,
        RejectedPatchesAction: PatchActionType = None,
        Description: str = None,
        Sources: List["PatchSourceTypeDef"] = None,
        ClientToken: str = None,
        Tags: List["TagTypeDef"] = None
    ) -> CreatePatchBaselineResultTypeDef:
        """
        Creates a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_patch_baseline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_patch_baseline)
        """
    def create_resource_data_sync(
        self,
        *,
        SyncName: str,
        S3Destination: "ResourceDataSyncS3DestinationTypeDef" = None,
        SyncType: str = None,
        SyncSource: "ResourceDataSyncSourceTypeDef" = None
    ) -> Dict[str, Any]:
        """
        A resource data sync helps you view data from multiple sources in a single
        location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.create_resource_data_sync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#create_resource_data_sync)
        """
    def delete_activation(self, *, ActivationId: str) -> Dict[str, Any]:
        """
        Deletes an activation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_activation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_activation)
        """
    def delete_association(
        self, *, Name: str = None, InstanceId: str = None, AssociationId: str = None
    ) -> Dict[str, Any]:
        """
        Disassociates the specified Amazon Web Services Systems Manager document (SSM
        document) from the specified managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_association)
        """
    def delete_document(
        self, *, Name: str, DocumentVersion: str = None, VersionName: str = None, Force: bool = None
    ) -> Dict[str, Any]:
        """
        Deletes the Amazon Web Services Systems Manager document (SSM document) and all
        managed node associations to the document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_document)
        """
    def delete_inventory(
        self,
        *,
        TypeName: str,
        SchemaDeleteOption: InventorySchemaDeleteOptionType = None,
        DryRun: bool = None,
        ClientToken: str = None
    ) -> DeleteInventoryResultTypeDef:
        """
        Delete a custom inventory type or the data associated with a custom Inventory
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_inventory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_inventory)
        """
    def delete_maintenance_window(self, *, WindowId: str) -> DeleteMaintenanceWindowResultTypeDef:
        """
        Deletes a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_maintenance_window)
        """
    def delete_ops_metadata(self, *, OpsMetadataArn: str) -> Dict[str, Any]:
        """
        Delete OpsMetadata related to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_ops_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_ops_metadata)
        """
    def delete_parameter(self, *, Name: str) -> Dict[str, Any]:
        """
        Delete a parameter from the system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_parameter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_parameter)
        """
    def delete_parameters(self, *, Names: List[str]) -> DeleteParametersResultTypeDef:
        """
        Delete a list of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_parameters)
        """
    def delete_patch_baseline(self, *, BaselineId: str) -> DeletePatchBaselineResultTypeDef:
        """
        Deletes a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_patch_baseline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_patch_baseline)
        """
    def delete_resource_data_sync(self, *, SyncName: str, SyncType: str = None) -> Dict[str, Any]:
        """
        Deletes a resource data sync configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.delete_resource_data_sync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#delete_resource_data_sync)
        """
    def deregister_managed_instance(self, *, InstanceId: str) -> Dict[str, Any]:
        """
        Removes the server or virtual machine from the list of registered servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.deregister_managed_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#deregister_managed_instance)
        """
    def deregister_patch_baseline_for_patch_group(
        self, *, BaselineId: str, PatchGroup: str
    ) -> DeregisterPatchBaselineForPatchGroupResultTypeDef:
        """
        Removes a patch group from a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.deregister_patch_baseline_for_patch_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#deregister_patch_baseline_for_patch_group)
        """
    def deregister_target_from_maintenance_window(
        self, *, WindowId: str, WindowTargetId: str, Safe: bool = None
    ) -> DeregisterTargetFromMaintenanceWindowResultTypeDef:
        """
        Removes a target from a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.deregister_target_from_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#deregister_target_from_maintenance_window)
        """
    def deregister_task_from_maintenance_window(
        self, *, WindowId: str, WindowTaskId: str
    ) -> DeregisterTaskFromMaintenanceWindowResultTypeDef:
        """
        Removes a task from a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.deregister_task_from_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#deregister_task_from_maintenance_window)
        """
    def describe_activations(
        self,
        *,
        Filters: List["DescribeActivationsFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeActivationsResultTypeDef:
        """
        Describes details about the activation, such as the date and time the activation
        was created, its expiration date, the Identity and Access Management (IAM) role
        assigned to the managed nodes in the activation, and the number of nodes
        registered by using this activation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_activations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_activations)
        """
    def describe_association(
        self,
        *,
        Name: str = None,
        InstanceId: str = None,
        AssociationId: str = None,
        AssociationVersion: str = None
    ) -> DescribeAssociationResultTypeDef:
        """
        Describes the association for the specified target or managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_association)
        """
    def describe_association_execution_targets(
        self,
        *,
        AssociationId: str,
        ExecutionId: str,
        Filters: List["AssociationExecutionTargetsFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeAssociationExecutionTargetsResultTypeDef:
        """
        Views information about a specific execution of a specific association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_association_execution_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_association_execution_targets)
        """
    def describe_association_executions(
        self,
        *,
        AssociationId: str,
        Filters: List["AssociationExecutionFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeAssociationExecutionsResultTypeDef:
        """
        Views all executions for a specific association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_association_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_association_executions)
        """
    def describe_automation_executions(
        self,
        *,
        Filters: List["AutomationExecutionFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeAutomationExecutionsResultTypeDef:
        """
        Provides details about all active and terminated Automation executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_automation_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_automation_executions)
        """
    def describe_automation_step_executions(
        self,
        *,
        AutomationExecutionId: str,
        Filters: List["StepExecutionFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        ReverseOrder: bool = None
    ) -> DescribeAutomationStepExecutionsResultTypeDef:
        """
        Information about all active and terminated step executions in an Automation
        workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_automation_step_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_automation_step_executions)
        """
    def describe_available_patches(
        self,
        *,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeAvailablePatchesResultTypeDef:
        """
        Lists all patches eligible to be included in a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_available_patches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_available_patches)
        """
    def describe_document(
        self, *, Name: str, DocumentVersion: str = None, VersionName: str = None
    ) -> DescribeDocumentResultTypeDef:
        """
        Describes the specified Amazon Web Services Systems Manager document (SSM
        document).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_document)
        """
    def describe_document_permission(
        self,
        *,
        Name: str,
        PermissionType: Literal["Share"],
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeDocumentPermissionResponseTypeDef:
        """
        Describes the permissions for a Amazon Web Services Systems Manager document
        (SSM document).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_document_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_document_permission)
        """
    def describe_effective_instance_associations(
        self, *, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeEffectiveInstanceAssociationsResultTypeDef:
        """
        All associations for the managed node(s).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_effective_instance_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_effective_instance_associations)
        """
    def describe_effective_patches_for_patch_baseline(
        self, *, BaselineId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeEffectivePatchesForPatchBaselineResultTypeDef:
        """
        Retrieves the current effective patches (the patch and the approval state) for
        the specified patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_effective_patches_for_patch_baseline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_effective_patches_for_patch_baseline)
        """
    def describe_instance_associations_status(
        self, *, InstanceId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeInstanceAssociationsStatusResultTypeDef:
        """
        The status of the associations for the managed node(s).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_instance_associations_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_instance_associations_status)
        """
    def describe_instance_information(
        self,
        *,
        InstanceInformationFilterList: List["InstanceInformationFilterTypeDef"] = None,
        Filters: List["InstanceInformationStringFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeInstanceInformationResultTypeDef:
        """
        Describes one or more of your managed nodes, including information about the
        operating system platform, the version of SSM Agent installed on the managed
        node, node status, and so on.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_instance_information)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_instance_information)
        """
    def describe_instance_patch_states(
        self, *, InstanceIds: List[str], NextToken: str = None, MaxResults: int = None
    ) -> DescribeInstancePatchStatesResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_instance_patch_states)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_instance_patch_states)
        """
    def describe_instance_patch_states_for_patch_group(
        self,
        *,
        PatchGroup: str,
        Filters: List["InstancePatchStateFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeInstancePatchStatesForPatchGroupResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_instance_patch_states_for_patch_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_instance_patch_states_for_patch_group)
        """
    def describe_instance_patches(
        self,
        *,
        InstanceId: str,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeInstancePatchesResultTypeDef:
        """
        Retrieves information about the patches on the specified managed node and their
        state relative to the patch baseline being used for the node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_instance_patches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_instance_patches)
        """
    def describe_inventory_deletions(
        self, *, DeletionId: str = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeInventoryDeletionsResultTypeDef:
        """
        Describes a specific delete inventory operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_inventory_deletions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_inventory_deletions)
        """
    def describe_maintenance_window_execution_task_invocations(
        self,
        *,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef:
        """
        Retrieves the individual task executions (one per target) for a particular task
        run as part of a maintenance window execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_task_invocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_maintenance_window_execution_task_invocations)
        """
    def describe_maintenance_window_execution_tasks(
        self,
        *,
        WindowExecutionId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMaintenanceWindowExecutionTasksResultTypeDef:
        """
        For a given maintenance window execution, lists the tasks that were run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_maintenance_window_execution_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_maintenance_window_execution_tasks)
        """
    def describe_maintenance_window_executions(
        self,
        *,
        WindowId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMaintenanceWindowExecutionsResultTypeDef:
        """
        Lists the executions of a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_maintenance_window_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_maintenance_window_executions)
        """
    def describe_maintenance_window_schedule(
        self,
        *,
        WindowId: str = None,
        Targets: List["TargetTypeDef"] = None,
        ResourceType: MaintenanceWindowResourceTypeType = None,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMaintenanceWindowScheduleResultTypeDef:
        """
        Retrieves information about upcoming executions of a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_maintenance_window_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_maintenance_window_schedule)
        """
    def describe_maintenance_window_targets(
        self,
        *,
        WindowId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMaintenanceWindowTargetsResultTypeDef:
        """
        Lists the targets registered with the maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_maintenance_window_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_maintenance_window_targets)
        """
    def describe_maintenance_window_tasks(
        self,
        *,
        WindowId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMaintenanceWindowTasksResultTypeDef:
        """
        Lists the tasks in a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_maintenance_window_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_maintenance_window_tasks)
        """
    def describe_maintenance_windows(
        self,
        *,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMaintenanceWindowsResultTypeDef:
        """
        Retrieves the maintenance windows in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_maintenance_windows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_maintenance_windows)
        """
    def describe_maintenance_windows_for_target(
        self,
        *,
        Targets: List["TargetTypeDef"],
        ResourceType: MaintenanceWindowResourceTypeType,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMaintenanceWindowsForTargetResultTypeDef:
        """
        Retrieves information about the maintenance window targets or tasks that a
        managed node is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_maintenance_windows_for_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_maintenance_windows_for_target)
        """
    def describe_ops_items(
        self,
        *,
        OpsItemFilters: List["OpsItemFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeOpsItemsResponseTypeDef:
        """
        Query a set of OpsItems.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_ops_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_ops_items)
        """
    def describe_parameters(
        self,
        *,
        Filters: List["ParametersFilterTypeDef"] = None,
        ParameterFilters: List["ParameterStringFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeParametersResultTypeDef:
        """
        Get information about a parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_parameters)
        """
    def describe_patch_baselines(
        self,
        *,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribePatchBaselinesResultTypeDef:
        """
        Lists the patch baselines in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_patch_baselines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_patch_baselines)
        """
    def describe_patch_group_state(
        self, *, PatchGroup: str
    ) -> DescribePatchGroupStateResultTypeDef:
        """
        Returns high-level aggregated patch compliance state information for a patch
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_patch_group_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_patch_group_state)
        """
    def describe_patch_groups(
        self,
        *,
        MaxResults: int = None,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        NextToken: str = None
    ) -> DescribePatchGroupsResultTypeDef:
        """
        Lists all patch groups that have been registered with patch baselines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_patch_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_patch_groups)
        """
    def describe_patch_properties(
        self,
        *,
        OperatingSystem: OperatingSystemType,
        Property: PatchPropertyType,
        PatchSet: PatchSetType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribePatchPropertiesResultTypeDef:
        """
        Lists the properties of available patches organized by product, product family,
        classification, severity, and other properties of available patches.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_patch_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_patch_properties)
        """
    def describe_sessions(
        self,
        *,
        State: SessionStateType,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["SessionFilterTypeDef"] = None
    ) -> DescribeSessionsResponseTypeDef:
        """
        Retrieves a list of all active sessions (both connected and disconnected) or
        terminated sessions from the past 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.describe_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#describe_sessions)
        """
    def disassociate_ops_item_related_item(
        self, *, OpsItemId: str, AssociationId: str
    ) -> Dict[str, Any]:
        """
        Deletes the association between an OpsItem and a related item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.disassociate_ops_item_related_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#disassociate_ops_item_related_item)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#generate_presigned_url)
        """
    def get_automation_execution(
        self, *, AutomationExecutionId: str
    ) -> GetAutomationExecutionResultTypeDef:
        """
        Get detailed information about a particular Automation execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_automation_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_automation_execution)
        """
    def get_calendar_state(
        self, *, CalendarNames: List[str], AtTime: str = None
    ) -> GetCalendarStateResponseTypeDef:
        """
        Gets the state of a Amazon Web Services Systems Manager change calendar at the
        current time or a specified time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_calendar_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_calendar_state)
        """
    def get_command_invocation(
        self, *, CommandId: str, InstanceId: str, PluginName: str = None
    ) -> GetCommandInvocationResultTypeDef:
        """
        Returns detailed information about command execution for an invocation or
        plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_command_invocation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_command_invocation)
        """
    def get_connection_status(self, *, Target: str) -> GetConnectionStatusResponseTypeDef:
        """
        Retrieves the Session Manager connection status for a managed node to determine
        whether it is running and ready to receive Session Manager connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_connection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_connection_status)
        """
    def get_default_patch_baseline(
        self, *, OperatingSystem: OperatingSystemType = None
    ) -> GetDefaultPatchBaselineResultTypeDef:
        """
        Retrieves the default patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_default_patch_baseline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_default_patch_baseline)
        """
    def get_deployable_patch_snapshot_for_instance(
        self,
        *,
        InstanceId: str,
        SnapshotId: str,
        BaselineOverride: "BaselineOverrideTypeDef" = None
    ) -> GetDeployablePatchSnapshotForInstanceResultTypeDef:
        """
        Retrieves the current snapshot for the patch baseline the managed node uses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_deployable_patch_snapshot_for_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_deployable_patch_snapshot_for_instance)
        """
    def get_document(
        self,
        *,
        Name: str,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: DocumentFormatType = None
    ) -> GetDocumentResultTypeDef:
        """
        Gets the contents of the specified Amazon Web Services Systems Manager document
        (SSM document).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_document)
        """
    def get_inventory(
        self,
        *,
        Filters: List["InventoryFilterTypeDef"] = None,
        Aggregators: List["InventoryAggregatorTypeDef"] = None,
        ResultAttributes: List["ResultAttributeTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetInventoryResultTypeDef:
        """
        Query inventory information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_inventory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_inventory)
        """
    def get_inventory_schema(
        self,
        *,
        TypeName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Aggregator: bool = None,
        SubType: bool = None
    ) -> GetInventorySchemaResultTypeDef:
        """
        Return a list of inventory type names for the account, or return a list of
        attribute names for a specific Inventory item type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_inventory_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_inventory_schema)
        """
    def get_maintenance_window(self, *, WindowId: str) -> GetMaintenanceWindowResultTypeDef:
        """
        Retrieves a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_maintenance_window)
        """
    def get_maintenance_window_execution(
        self, *, WindowExecutionId: str
    ) -> GetMaintenanceWindowExecutionResultTypeDef:
        """
        Retrieves details about a specific a maintenance window execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_maintenance_window_execution)
        """
    def get_maintenance_window_execution_task(
        self, *, WindowExecutionId: str, TaskId: str
    ) -> GetMaintenanceWindowExecutionTaskResultTypeDef:
        """
        Retrieves the details about a specific task run as part of a maintenance window
        execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_maintenance_window_execution_task)
        """
    def get_maintenance_window_execution_task_invocation(
        self, *, WindowExecutionId: str, TaskId: str, InvocationId: str
    ) -> GetMaintenanceWindowExecutionTaskInvocationResultTypeDef:
        """
        Retrieves information about a specific task running on a specific target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_maintenance_window_execution_task_invocation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_maintenance_window_execution_task_invocation)
        """
    def get_maintenance_window_task(
        self, *, WindowId: str, WindowTaskId: str
    ) -> GetMaintenanceWindowTaskResultTypeDef:
        """
        Retrieves the details of a maintenance window task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_maintenance_window_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_maintenance_window_task)
        """
    def get_ops_item(self, *, OpsItemId: str) -> GetOpsItemResponseTypeDef:
        """
        Get information about an OpsItem by using the ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_ops_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_ops_item)
        """
    def get_ops_metadata(
        self, *, OpsMetadataArn: str, MaxResults: int = None, NextToken: str = None
    ) -> GetOpsMetadataResultTypeDef:
        """
        View operational metadata related to an application in Application Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_ops_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_ops_metadata)
        """
    def get_ops_summary(
        self,
        *,
        SyncName: str = None,
        Filters: List["OpsFilterTypeDef"] = None,
        Aggregators: List["OpsAggregatorTypeDef"] = None,
        ResultAttributes: List["OpsResultAttributeTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetOpsSummaryResultTypeDef:
        """
        View a summary of operations metadata (OpsData) based on specified filters and
        aggregators.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_ops_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_ops_summary)
        """
    def get_parameter(self, *, Name: str, WithDecryption: bool = None) -> GetParameterResultTypeDef:
        """
        Get information about a single parameter by specifying the parameter name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_parameter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_parameter)
        """
    def get_parameter_history(
        self,
        *,
        Name: str,
        WithDecryption: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetParameterHistoryResultTypeDef:
        """
        Retrieves the history of all changes to a parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_parameter_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_parameter_history)
        """
    def get_parameters(
        self, *, Names: List[str], WithDecryption: bool = None
    ) -> GetParametersResultTypeDef:
        """
        Get information about one or more parameters by specifying multiple parameter
        names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_parameters)
        """
    def get_parameters_by_path(
        self,
        *,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List["ParameterStringFilterTypeDef"] = None,
        WithDecryption: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetParametersByPathResultTypeDef:
        """
        Retrieve information about one or more parameters in a specific hierarchy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_parameters_by_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_parameters_by_path)
        """
    def get_patch_baseline(self, *, BaselineId: str) -> GetPatchBaselineResultTypeDef:
        """
        Retrieves information about a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_patch_baseline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_patch_baseline)
        """
    def get_patch_baseline_for_patch_group(
        self, *, PatchGroup: str, OperatingSystem: OperatingSystemType = None
    ) -> GetPatchBaselineForPatchGroupResultTypeDef:
        """
        Retrieves the patch baseline that should be used for the specified patch group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_patch_baseline_for_patch_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_patch_baseline_for_patch_group)
        """
    def get_service_setting(self, *, SettingId: str) -> GetServiceSettingResultTypeDef:
        """
        `ServiceSetting` is an account-level setting for an Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.get_service_setting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#get_service_setting)
        """
    def label_parameter_version(
        self, *, Name: str, Labels: List[str], ParameterVersion: int = None
    ) -> LabelParameterVersionResultTypeDef:
        """
        A parameter label is a user-defined alias to help you manage different versions
        of a parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.label_parameter_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#label_parameter_version)
        """
    def list_association_versions(
        self, *, AssociationId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListAssociationVersionsResultTypeDef:
        """
        Retrieves all versions of an association for a specific association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_association_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_association_versions)
        """
    def list_associations(
        self,
        *,
        AssociationFilterList: List["AssociationFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListAssociationsResultTypeDef:
        """
        Returns all State Manager associations in the current Amazon Web Services
        account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_associations)
        """
    def list_command_invocations(
        self,
        *,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["CommandFilterTypeDef"] = None,
        Details: bool = None
    ) -> ListCommandInvocationsResultTypeDef:
        """
        An invocation is copy of a command sent to a specific managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_command_invocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_command_invocations)
        """
    def list_commands(
        self,
        *,
        CommandId: str = None,
        InstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["CommandFilterTypeDef"] = None
    ) -> ListCommandsResultTypeDef:
        """
        Lists the commands requested by users of the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_commands)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_commands)
        """
    def list_compliance_items(
        self,
        *,
        Filters: List["ComplianceStringFilterTypeDef"] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListComplianceItemsResultTypeDef:
        """
        For a specified resource ID, this API operation returns a list of compliance
        statuses for different resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_compliance_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_compliance_items)
        """
    def list_compliance_summaries(
        self,
        *,
        Filters: List["ComplianceStringFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListComplianceSummariesResultTypeDef:
        """
        Returns a summary count of compliant and non-compliant resources for a
        compliance type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_compliance_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_compliance_summaries)
        """
    def list_document_metadata_history(
        self,
        *,
        Name: str,
        Metadata: Literal["DocumentReviews"],
        DocumentVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListDocumentMetadataHistoryResponseTypeDef:
        """
        Information about approval reviews for a version of a change template in Change
        Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_document_metadata_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_document_metadata_history)
        """
    def list_document_versions(
        self, *, Name: str, MaxResults: int = None, NextToken: str = None
    ) -> ListDocumentVersionsResultTypeDef:
        """
        List all versions for a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_document_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_document_versions)
        """
    def list_documents(
        self,
        *,
        DocumentFilterList: List["DocumentFilterTypeDef"] = None,
        Filters: List["DocumentKeyValuesFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListDocumentsResultTypeDef:
        """
        Returns all Systems Manager (SSM) documents in the current Amazon Web Services
        account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_documents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_documents)
        """
    def list_inventory_entries(
        self,
        *,
        InstanceId: str,
        TypeName: str,
        Filters: List["InventoryFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListInventoryEntriesResultTypeDef:
        """
        A list of inventory items returned by the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_inventory_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_inventory_entries)
        """
    def list_ops_item_events(
        self,
        *,
        Filters: List["OpsItemEventFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListOpsItemEventsResponseTypeDef:
        """
        Returns a list of all OpsItem events in the current Amazon Web Services Region
        and Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_ops_item_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_ops_item_events)
        """
    def list_ops_item_related_items(
        self,
        *,
        OpsItemId: str = None,
        Filters: List["OpsItemRelatedItemsFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListOpsItemRelatedItemsResponseTypeDef:
        """
        Lists all related-item resources associated with a Systems Manager OpsCenter
        OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_ops_item_related_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_ops_item_related_items)
        """
    def list_ops_metadata(
        self,
        *,
        Filters: List["OpsMetadataFilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> ListOpsMetadataResultTypeDef:
        """
        Amazon Web Services Systems Manager calls this API operation when displaying all
        Application Manager OpsMetadata objects or blobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_ops_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_ops_metadata)
        """
    def list_resource_compliance_summaries(
        self,
        *,
        Filters: List["ComplianceStringFilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> ListResourceComplianceSummariesResultTypeDef:
        """
        Returns a resource-level summary count.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_resource_compliance_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_resource_compliance_summaries)
        """
    def list_resource_data_sync(
        self, *, SyncType: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListResourceDataSyncResultTypeDef:
        """
        Lists your resource data sync configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_resource_data_sync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_resource_data_sync)
        """
    def list_tags_for_resource(
        self, *, ResourceType: ResourceTypeForTaggingType, ResourceId: str
    ) -> ListTagsForResourceResultTypeDef:
        """
        Returns a list of the tags assigned to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#list_tags_for_resource)
        """
    def modify_document_permission(
        self,
        *,
        Name: str,
        PermissionType: Literal["Share"],
        AccountIdsToAdd: List[str] = None,
        AccountIdsToRemove: List[str] = None,
        SharedDocumentVersion: str = None
    ) -> Dict[str, Any]:
        """
        Shares a Amazon Web Services Systems Manager document (SSM document)publicly or
        privately.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.modify_document_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#modify_document_permission)
        """
    def put_compliance_items(
        self,
        *,
        ResourceId: str,
        ResourceType: str,
        ComplianceType: str,
        ExecutionSummary: "ComplianceExecutionSummaryTypeDef",
        Items: List["ComplianceItemEntryTypeDef"],
        ItemContentHash: str = None,
        UploadType: ComplianceUploadTypeType = None
    ) -> Dict[str, Any]:
        """
        Registers a compliance type and other compliance details on a designated
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.put_compliance_items)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#put_compliance_items)
        """
    def put_inventory(
        self, *, InstanceId: str, Items: List["InventoryItemTypeDef"]
    ) -> PutInventoryResultTypeDef:
        """
        Bulk update custom inventory items on one or more managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.put_inventory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#put_inventory)
        """
    def put_parameter(
        self,
        *,
        Name: str,
        Value: str,
        Description: str = None,
        Type: ParameterTypeType = None,
        KeyId: str = None,
        Overwrite: bool = None,
        AllowedPattern: str = None,
        Tags: List["TagTypeDef"] = None,
        Tier: ParameterTierType = None,
        Policies: str = None,
        DataType: str = None
    ) -> PutParameterResultTypeDef:
        """
        Add a parameter to the system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.put_parameter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#put_parameter)
        """
    def register_default_patch_baseline(
        self, *, BaselineId: str
    ) -> RegisterDefaultPatchBaselineResultTypeDef:
        """
        Defines the default patch baseline for the relevant operating system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.register_default_patch_baseline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#register_default_patch_baseline)
        """
    def register_patch_baseline_for_patch_group(
        self, *, BaselineId: str, PatchGroup: str
    ) -> RegisterPatchBaselineForPatchGroupResultTypeDef:
        """
        Registers a patch baseline for a patch group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.register_patch_baseline_for_patch_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#register_patch_baseline_for_patch_group)
        """
    def register_target_with_maintenance_window(
        self,
        *,
        WindowId: str,
        ResourceType: MaintenanceWindowResourceTypeType,
        Targets: List["TargetTypeDef"],
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None
    ) -> RegisterTargetWithMaintenanceWindowResultTypeDef:
        """
        Registers a target with a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.register_target_with_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#register_target_with_maintenance_window)
        """
    def register_task_with_maintenance_window(
        self,
        *,
        WindowId: str,
        TaskArn: str,
        TaskType: MaintenanceWindowTaskTypeType,
        Targets: List["TargetTypeDef"] = None,
        ServiceRoleArn: str = None,
        TaskParameters: Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"] = None,
        TaskInvocationParameters: "MaintenanceWindowTaskInvocationParametersTypeDef" = None,
        Priority: int = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        LoggingInfo: "LoggingInfoTypeDef" = None,
        Name: str = None,
        Description: str = None,
        ClientToken: str = None,
        CutoffBehavior: MaintenanceWindowTaskCutoffBehaviorType = None
    ) -> RegisterTaskWithMaintenanceWindowResultTypeDef:
        """
        Adds a new task to a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.register_task_with_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#register_task_with_maintenance_window)
        """
    def remove_tags_from_resource(
        self, *, ResourceType: ResourceTypeForTaggingType, ResourceId: str, TagKeys: List[str]
    ) -> Dict[str, Any]:
        """
        Removes tag keys from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.remove_tags_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#remove_tags_from_resource)
        """
    def reset_service_setting(self, *, SettingId: str) -> ResetServiceSettingResultTypeDef:
        """
        `ServiceSetting` is an account-level setting for an Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.reset_service_setting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#reset_service_setting)
        """
    def resume_session(self, *, SessionId: str) -> ResumeSessionResponseTypeDef:
        """
        Reconnects a session to a managed node after it has been disconnected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.resume_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#resume_session)
        """
    def send_automation_signal(
        self,
        *,
        AutomationExecutionId: str,
        SignalType: SignalTypeType,
        Payload: Dict[str, List[str]] = None
    ) -> Dict[str, Any]:
        """
        Sends a signal to an Automation execution to change the current behavior or
        status of the execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.send_automation_signal)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#send_automation_signal)
        """
    def send_command(
        self,
        *,
        DocumentName: str,
        InstanceIds: List[str] = None,
        Targets: List["TargetTypeDef"] = None,
        DocumentVersion: str = None,
        DocumentHash: str = None,
        DocumentHashType: DocumentHashTypeType = None,
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
        CloudWatchOutputConfig: "CloudWatchOutputConfigTypeDef" = None
    ) -> SendCommandResultTypeDef:
        """
        Runs commands on one or more managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.send_command)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#send_command)
        """
    def start_associations_once(self, *, AssociationIds: List[str]) -> Dict[str, Any]:
        """
        Runs an association immediately and only one time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.start_associations_once)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#start_associations_once)
        """
    def start_automation_execution(
        self,
        *,
        DocumentName: str,
        DocumentVersion: str = None,
        Parameters: Dict[str, List[str]] = None,
        ClientToken: str = None,
        Mode: ExecutionModeType = None,
        TargetParameterName: str = None,
        Targets: List["TargetTypeDef"] = None,
        TargetMaps: List[Dict[str, List[str]]] = None,
        MaxConcurrency: str = None,
        MaxErrors: str = None,
        TargetLocations: List["TargetLocationTypeDef"] = None,
        Tags: List["TagTypeDef"] = None
    ) -> StartAutomationExecutionResultTypeDef:
        """
        Initiates execution of an Automation runbook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.start_automation_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#start_automation_execution)
        """
    def start_change_request_execution(
        self,
        *,
        DocumentName: str,
        Runbooks: List["RunbookTypeDef"],
        ScheduledTime: Union[datetime, str] = None,
        DocumentVersion: str = None,
        Parameters: Dict[str, List[str]] = None,
        ChangeRequestName: str = None,
        ClientToken: str = None,
        AutoApprove: bool = None,
        Tags: List["TagTypeDef"] = None,
        ScheduledEndTime: Union[datetime, str] = None,
        ChangeDetails: str = None
    ) -> StartChangeRequestExecutionResultTypeDef:
        """
        Creates a change request for Change Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.start_change_request_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#start_change_request_execution)
        """
    def start_session(
        self,
        *,
        Target: str,
        DocumentName: str = None,
        Reason: str = None,
        Parameters: Dict[str, List[str]] = None
    ) -> StartSessionResponseTypeDef:
        """
        Initiates a connection to a target (for example, a managed node) for a Session
        Manager session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.start_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#start_session)
        """
    def stop_automation_execution(
        self, *, AutomationExecutionId: str, Type: StopTypeType = None
    ) -> Dict[str, Any]:
        """
        Stop an Automation that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.stop_automation_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#stop_automation_execution)
        """
    def terminate_session(self, *, SessionId: str) -> TerminateSessionResponseTypeDef:
        """
        Permanently ends a session and closes the data connection between the Session
        Manager client and SSM Agent on the managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.terminate_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#terminate_session)
        """
    def unlabel_parameter_version(
        self, *, Name: str, ParameterVersion: int, Labels: List[str]
    ) -> UnlabelParameterVersionResultTypeDef:
        """
        Remove a label or labels from a parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.unlabel_parameter_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#unlabel_parameter_version)
        """
    def update_association(
        self,
        *,
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
        ComplianceSeverity: AssociationComplianceSeverityType = None,
        SyncCompliance: AssociationSyncComplianceType = None,
        ApplyOnlyAtCronInterval: bool = None,
        CalendarNames: List[str] = None,
        TargetLocations: List["TargetLocationTypeDef"] = None,
        ScheduleOffset: int = None,
        TargetMaps: List[Dict[str, List[str]]] = None
    ) -> UpdateAssociationResultTypeDef:
        """
        Updates an association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_association)
        """
    def update_association_status(
        self, *, Name: str, InstanceId: str, AssociationStatus: "AssociationStatusTypeDef"
    ) -> UpdateAssociationStatusResultTypeDef:
        """
        Updates the status of the Amazon Web Services Systems Manager document (SSM
        document) associated with the specified managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_association_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_association_status)
        """
    def update_document(
        self,
        *,
        Content: str,
        Name: str,
        Attachments: List["AttachmentsSourceTypeDef"] = None,
        DisplayName: str = None,
        VersionName: str = None,
        DocumentVersion: str = None,
        DocumentFormat: DocumentFormatType = None,
        TargetType: str = None
    ) -> UpdateDocumentResultTypeDef:
        """
        Updates one or more values for an SSM document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_document)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_document)
        """
    def update_document_default_version(
        self, *, Name: str, DocumentVersion: str
    ) -> UpdateDocumentDefaultVersionResultTypeDef:
        """
        Set the default version of a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_document_default_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_document_default_version)
        """
    def update_document_metadata(
        self, *, Name: str, DocumentReviews: "DocumentReviewsTypeDef", DocumentVersion: str = None
    ) -> Dict[str, Any]:
        """
        Updates information related to approval reviews for a specific version of a
        change template in Change Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_document_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_document_metadata)
        """
    def update_maintenance_window(
        self,
        *,
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
        Replace: bool = None
    ) -> UpdateMaintenanceWindowResultTypeDef:
        """
        Updates an existing maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_maintenance_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_maintenance_window)
        """
    def update_maintenance_window_target(
        self,
        *,
        WindowId: str,
        WindowTargetId: str,
        Targets: List["TargetTypeDef"] = None,
        OwnerInformation: str = None,
        Name: str = None,
        Description: str = None,
        Replace: bool = None
    ) -> UpdateMaintenanceWindowTargetResultTypeDef:
        """
        Modifies the target of an existing maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_maintenance_window_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_maintenance_window_target)
        """
    def update_maintenance_window_task(
        self,
        *,
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
        CutoffBehavior: MaintenanceWindowTaskCutoffBehaviorType = None
    ) -> UpdateMaintenanceWindowTaskResultTypeDef:
        """
        Modifies a task assigned to a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_maintenance_window_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_maintenance_window_task)
        """
    def update_managed_instance_role(self, *, InstanceId: str, IamRole: str) -> Dict[str, Any]:
        """
        Changes the Identity and Access Management (IAM) role that is assigned to the
        on-premises server, edge device, or virtual machines (VM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_managed_instance_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_managed_instance_role)
        """
    def update_ops_item(
        self,
        *,
        OpsItemId: str,
        Description: str = None,
        OperationalData: Dict[str, "OpsItemDataValueTypeDef"] = None,
        OperationalDataToDelete: List[str] = None,
        Notifications: List["OpsItemNotificationTypeDef"] = None,
        Priority: int = None,
        RelatedOpsItems: List["RelatedOpsItemTypeDef"] = None,
        Status: OpsItemStatusType = None,
        Title: str = None,
        Category: str = None,
        Severity: str = None,
        ActualStartTime: Union[datetime, str] = None,
        ActualEndTime: Union[datetime, str] = None,
        PlannedStartTime: Union[datetime, str] = None,
        PlannedEndTime: Union[datetime, str] = None
    ) -> Dict[str, Any]:
        """
        Edit or change an OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_ops_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_ops_item)
        """
    def update_ops_metadata(
        self,
        *,
        OpsMetadataArn: str,
        MetadataToUpdate: Dict[str, "MetadataValueTypeDef"] = None,
        KeysToDelete: List[str] = None
    ) -> UpdateOpsMetadataResultTypeDef:
        """
        Amazon Web Services Systems Manager calls this API operation when you edit
        OpsMetadata in Application Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_ops_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_ops_metadata)
        """
    def update_patch_baseline(
        self,
        *,
        BaselineId: str,
        Name: str = None,
        GlobalFilters: "PatchFilterGroupTypeDef" = None,
        ApprovalRules: "PatchRuleGroupTypeDef" = None,
        ApprovedPatches: List[str] = None,
        ApprovedPatchesComplianceLevel: PatchComplianceLevelType = None,
        ApprovedPatchesEnableNonSecurity: bool = None,
        RejectedPatches: List[str] = None,
        RejectedPatchesAction: PatchActionType = None,
        Description: str = None,
        Sources: List["PatchSourceTypeDef"] = None,
        Replace: bool = None
    ) -> UpdatePatchBaselineResultTypeDef:
        """
        Modifies an existing patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_patch_baseline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_patch_baseline)
        """
    def update_resource_data_sync(
        self, *, SyncName: str, SyncType: str, SyncSource: "ResourceDataSyncSourceTypeDef"
    ) -> Dict[str, Any]:
        """
        Update a resource data sync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_resource_data_sync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_resource_data_sync)
        """
    def update_service_setting(self, *, SettingId: str, SettingValue: str) -> Dict[str, Any]:
        """
        `ServiceSetting` is an account-level setting for an Amazon Web Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Client.update_service_setting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/client.html#update_service_setting)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_activations"]
    ) -> DescribeActivationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeActivations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeactivationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_association_execution_targets"]
    ) -> DescribeAssociationExecutionTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeassociationexecutiontargetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_association_executions"]
    ) -> DescribeAssociationExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeassociationexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_automation_executions"]
    ) -> DescribeAutomationExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeautomationexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_automation_step_executions"]
    ) -> DescribeAutomationStepExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeautomationstepexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_available_patches"]
    ) -> DescribeAvailablePatchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeavailablepatchespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_effective_instance_associations"]
    ) -> DescribeEffectiveInstanceAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeeffectiveinstanceassociationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_effective_patches_for_patch_baseline"]
    ) -> DescribeEffectivePatchesForPatchBaselinePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeeffectivepatchesforpatchbaselinepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_associations_status"]
    ) -> DescribeInstanceAssociationsStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstanceassociationsstatuspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_information"]
    ) -> DescribeInstanceInformationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstanceinformationpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patch_states"]
    ) -> DescribeInstancePatchStatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchstatespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patch_states_for_patch_group"]
    ) -> DescribeInstancePatchStatesForPatchGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchstatesforpatchgrouppaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_patches"]
    ) -> DescribeInstancePatchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_inventory_deletions"]
    ) -> DescribeInventoryDeletionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinventorydeletionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_execution_task_invocations"]
    ) -> DescribeMaintenanceWindowExecutionTaskInvocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutiontaskinvocationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_execution_tasks"]
    ) -> DescribeMaintenanceWindowExecutionTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutiontaskspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_executions"]
    ) -> DescribeMaintenanceWindowExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_schedule"]
    ) -> DescribeMaintenanceWindowSchedulePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowschedulepaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_targets"]
    ) -> DescribeMaintenanceWindowTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowtargetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_window_tasks"]
    ) -> DescribeMaintenanceWindowTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowtaskspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_windows"]
    ) -> DescribeMaintenanceWindowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_maintenance_windows_for_target"]
    ) -> DescribeMaintenanceWindowsForTargetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowsfortargetpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ops_items"]
    ) -> DescribeOpsItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeOpsItems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeopsitemspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_parameters"]
    ) -> DescribeParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_patch_baselines"]
    ) -> DescribePatchBaselinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchbaselinespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_patch_groups"]
    ) -> DescribePatchGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchgroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_patch_properties"]
    ) -> DescribePatchPropertiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchProperties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchpropertiespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_sessions"]
    ) -> DescribeSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describesessionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_inventory"]) -> GetInventoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetInventory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getinventorypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_inventory_schema"]
    ) -> GetInventorySchemaPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getinventoryschemapaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_ops_summary"]) -> GetOpsSummaryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetOpsSummary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getopssummarypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_parameter_history"]
    ) -> GetParameterHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getparameterhistorypaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_parameters_by_path"]
    ) -> GetParametersByPathPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getparametersbypathpaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_association_versions"]
    ) -> ListAssociationVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listassociationversionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations"]
    ) -> ListAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listassociationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_command_invocations"]
    ) -> ListCommandInvocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcommandinvocationspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_commands"]) -> ListCommandsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListCommands)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcommandspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_items"]
    ) -> ListComplianceItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcomplianceitemspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_summaries"]
    ) -> ListComplianceSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcompliancesummariespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_document_versions"]
    ) -> ListDocumentVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listdocumentversionspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_documents"]) -> ListDocumentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListDocuments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listdocumentspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_ops_item_events"]
    ) -> ListOpsItemEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsItemEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsitemeventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_ops_item_related_items"]
    ) -> ListOpsItemRelatedItemsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsItemRelatedItems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsitemrelateditemspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_ops_metadata"]
    ) -> ListOpsMetadataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsMetadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsmetadatapaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_compliance_summaries"]
    ) -> ListResourceComplianceSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listresourcecompliancesummariespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_data_sync"]
    ) -> ListResourceDataSyncPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listresourcedatasyncpaginator)
        """
    def get_waiter(self, waiter_name: Literal["command_executed"]) -> CommandExecutedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Waiter.CommandExecuted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/waiters.html#commandexecutedwaiter)
        """
