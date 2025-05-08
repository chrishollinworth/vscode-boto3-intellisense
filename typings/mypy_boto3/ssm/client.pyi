"""
Type annotations for ssm service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ssm.client import SSMClient

    session = Session()
    client: SSMClient = session.client("ssm")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
    DescribeInstancePropertiesPaginator,
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
    GetResourcePoliciesPaginator,
    ListAssociationsPaginator,
    ListAssociationVersionsPaginator,
    ListCommandInvocationsPaginator,
    ListCommandsPaginator,
    ListComplianceItemsPaginator,
    ListComplianceSummariesPaginator,
    ListDocumentsPaginator,
    ListDocumentVersionsPaginator,
    ListNodesPaginator,
    ListNodesSummaryPaginator,
    ListOpsItemEventsPaginator,
    ListOpsItemRelatedItemsPaginator,
    ListOpsMetadataPaginator,
    ListResourceComplianceSummariesPaginator,
    ListResourceDataSyncPaginator,
)
from .type_defs import (
    AddTagsToResourceRequestTypeDef,
    AssociateOpsItemRelatedItemRequestTypeDef,
    AssociateOpsItemRelatedItemResponseTypeDef,
    CancelCommandRequestTypeDef,
    CancelMaintenanceWindowExecutionRequestTypeDef,
    CancelMaintenanceWindowExecutionResultTypeDef,
    CreateActivationRequestTypeDef,
    CreateActivationResultTypeDef,
    CreateAssociationBatchRequestTypeDef,
    CreateAssociationBatchResultTypeDef,
    CreateAssociationRequestTypeDef,
    CreateAssociationResultTypeDef,
    CreateDocumentRequestTypeDef,
    CreateDocumentResultTypeDef,
    CreateMaintenanceWindowRequestTypeDef,
    CreateMaintenanceWindowResultTypeDef,
    CreateOpsItemRequestTypeDef,
    CreateOpsItemResponseTypeDef,
    CreateOpsMetadataRequestTypeDef,
    CreateOpsMetadataResultTypeDef,
    CreatePatchBaselineRequestTypeDef,
    CreatePatchBaselineResultTypeDef,
    CreateResourceDataSyncRequestTypeDef,
    DeleteActivationRequestTypeDef,
    DeleteAssociationRequestTypeDef,
    DeleteDocumentRequestTypeDef,
    DeleteInventoryRequestTypeDef,
    DeleteInventoryResultTypeDef,
    DeleteMaintenanceWindowRequestTypeDef,
    DeleteMaintenanceWindowResultTypeDef,
    DeleteOpsItemRequestTypeDef,
    DeleteOpsMetadataRequestTypeDef,
    DeleteParameterRequestTypeDef,
    DeleteParametersRequestTypeDef,
    DeleteParametersResultTypeDef,
    DeletePatchBaselineRequestTypeDef,
    DeletePatchBaselineResultTypeDef,
    DeleteResourceDataSyncRequestTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeregisterManagedInstanceRequestTypeDef,
    DeregisterPatchBaselineForPatchGroupRequestTypeDef,
    DeregisterPatchBaselineForPatchGroupResultTypeDef,
    DeregisterTargetFromMaintenanceWindowRequestTypeDef,
    DeregisterTargetFromMaintenanceWindowResultTypeDef,
    DeregisterTaskFromMaintenanceWindowRequestTypeDef,
    DeregisterTaskFromMaintenanceWindowResultTypeDef,
    DescribeActivationsRequestTypeDef,
    DescribeActivationsResultTypeDef,
    DescribeAssociationExecutionsRequestTypeDef,
    DescribeAssociationExecutionsResultTypeDef,
    DescribeAssociationExecutionTargetsRequestTypeDef,
    DescribeAssociationExecutionTargetsResultTypeDef,
    DescribeAssociationRequestTypeDef,
    DescribeAssociationResultTypeDef,
    DescribeAutomationExecutionsRequestTypeDef,
    DescribeAutomationExecutionsResultTypeDef,
    DescribeAutomationStepExecutionsRequestTypeDef,
    DescribeAutomationStepExecutionsResultTypeDef,
    DescribeAvailablePatchesRequestTypeDef,
    DescribeAvailablePatchesResultTypeDef,
    DescribeDocumentPermissionRequestTypeDef,
    DescribeDocumentPermissionResponseTypeDef,
    DescribeDocumentRequestTypeDef,
    DescribeDocumentResultTypeDef,
    DescribeEffectiveInstanceAssociationsRequestTypeDef,
    DescribeEffectiveInstanceAssociationsResultTypeDef,
    DescribeEffectivePatchesForPatchBaselineRequestTypeDef,
    DescribeEffectivePatchesForPatchBaselineResultTypeDef,
    DescribeInstanceAssociationsStatusRequestTypeDef,
    DescribeInstanceAssociationsStatusResultTypeDef,
    DescribeInstanceInformationRequestTypeDef,
    DescribeInstanceInformationResultTypeDef,
    DescribeInstancePatchesRequestTypeDef,
    DescribeInstancePatchesResultTypeDef,
    DescribeInstancePatchStatesForPatchGroupRequestTypeDef,
    DescribeInstancePatchStatesForPatchGroupResultTypeDef,
    DescribeInstancePatchStatesRequestTypeDef,
    DescribeInstancePatchStatesResultTypeDef,
    DescribeInstancePropertiesRequestTypeDef,
    DescribeInstancePropertiesResultTypeDef,
    DescribeInventoryDeletionsRequestTypeDef,
    DescribeInventoryDeletionsResultTypeDef,
    DescribeMaintenanceWindowExecutionsRequestTypeDef,
    DescribeMaintenanceWindowExecutionsResultTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef,
    DescribeMaintenanceWindowExecutionTasksRequestTypeDef,
    DescribeMaintenanceWindowExecutionTasksResultTypeDef,
    DescribeMaintenanceWindowScheduleRequestTypeDef,
    DescribeMaintenanceWindowScheduleResultTypeDef,
    DescribeMaintenanceWindowsForTargetRequestTypeDef,
    DescribeMaintenanceWindowsForTargetResultTypeDef,
    DescribeMaintenanceWindowsRequestTypeDef,
    DescribeMaintenanceWindowsResultTypeDef,
    DescribeMaintenanceWindowTargetsRequestTypeDef,
    DescribeMaintenanceWindowTargetsResultTypeDef,
    DescribeMaintenanceWindowTasksRequestTypeDef,
    DescribeMaintenanceWindowTasksResultTypeDef,
    DescribeOpsItemsRequestTypeDef,
    DescribeOpsItemsResponseTypeDef,
    DescribeParametersRequestTypeDef,
    DescribeParametersResultTypeDef,
    DescribePatchBaselinesRequestTypeDef,
    DescribePatchBaselinesResultTypeDef,
    DescribePatchGroupsRequestTypeDef,
    DescribePatchGroupsResultTypeDef,
    DescribePatchGroupStateRequestTypeDef,
    DescribePatchGroupStateResultTypeDef,
    DescribePatchPropertiesRequestTypeDef,
    DescribePatchPropertiesResultTypeDef,
    DescribeSessionsRequestTypeDef,
    DescribeSessionsResponseTypeDef,
    DisassociateOpsItemRelatedItemRequestTypeDef,
    GetAccessTokenRequestTypeDef,
    GetAccessTokenResponseTypeDef,
    GetAutomationExecutionRequestTypeDef,
    GetAutomationExecutionResultTypeDef,
    GetCalendarStateRequestTypeDef,
    GetCalendarStateResponseTypeDef,
    GetCommandInvocationRequestTypeDef,
    GetCommandInvocationResultTypeDef,
    GetConnectionStatusRequestTypeDef,
    GetConnectionStatusResponseTypeDef,
    GetDefaultPatchBaselineRequestTypeDef,
    GetDefaultPatchBaselineResultTypeDef,
    GetDeployablePatchSnapshotForInstanceRequestTypeDef,
    GetDeployablePatchSnapshotForInstanceResultTypeDef,
    GetDocumentRequestTypeDef,
    GetDocumentResultTypeDef,
    GetExecutionPreviewRequestTypeDef,
    GetExecutionPreviewResponseTypeDef,
    GetInventoryRequestTypeDef,
    GetInventoryResultTypeDef,
    GetInventorySchemaRequestTypeDef,
    GetInventorySchemaResultTypeDef,
    GetMaintenanceWindowExecutionRequestTypeDef,
    GetMaintenanceWindowExecutionResultTypeDef,
    GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef,
    GetMaintenanceWindowExecutionTaskInvocationResultTypeDef,
    GetMaintenanceWindowExecutionTaskRequestTypeDef,
    GetMaintenanceWindowExecutionTaskResultTypeDef,
    GetMaintenanceWindowRequestTypeDef,
    GetMaintenanceWindowResultTypeDef,
    GetMaintenanceWindowTaskRequestTypeDef,
    GetMaintenanceWindowTaskResultTypeDef,
    GetOpsItemRequestTypeDef,
    GetOpsItemResponseTypeDef,
    GetOpsMetadataRequestTypeDef,
    GetOpsMetadataResultTypeDef,
    GetOpsSummaryRequestTypeDef,
    GetOpsSummaryResultTypeDef,
    GetParameterHistoryRequestTypeDef,
    GetParameterHistoryResultTypeDef,
    GetParameterRequestTypeDef,
    GetParameterResultTypeDef,
    GetParametersByPathRequestTypeDef,
    GetParametersByPathResultTypeDef,
    GetParametersRequestTypeDef,
    GetParametersResultTypeDef,
    GetPatchBaselineForPatchGroupRequestTypeDef,
    GetPatchBaselineForPatchGroupResultTypeDef,
    GetPatchBaselineRequestTypeDef,
    GetPatchBaselineResultTypeDef,
    GetResourcePoliciesRequestTypeDef,
    GetResourcePoliciesResponseTypeDef,
    GetServiceSettingRequestTypeDef,
    GetServiceSettingResultTypeDef,
    LabelParameterVersionRequestTypeDef,
    LabelParameterVersionResultTypeDef,
    ListAssociationsRequestTypeDef,
    ListAssociationsResultTypeDef,
    ListAssociationVersionsRequestTypeDef,
    ListAssociationVersionsResultTypeDef,
    ListCommandInvocationsRequestTypeDef,
    ListCommandInvocationsResultTypeDef,
    ListCommandsRequestTypeDef,
    ListCommandsResultTypeDef,
    ListComplianceItemsRequestTypeDef,
    ListComplianceItemsResultTypeDef,
    ListComplianceSummariesRequestTypeDef,
    ListComplianceSummariesResultTypeDef,
    ListDocumentMetadataHistoryRequestTypeDef,
    ListDocumentMetadataHistoryResponseTypeDef,
    ListDocumentsRequestTypeDef,
    ListDocumentsResultTypeDef,
    ListDocumentVersionsRequestTypeDef,
    ListDocumentVersionsResultTypeDef,
    ListInventoryEntriesRequestTypeDef,
    ListInventoryEntriesResultTypeDef,
    ListNodesRequestTypeDef,
    ListNodesResultTypeDef,
    ListNodesSummaryRequestTypeDef,
    ListNodesSummaryResultTypeDef,
    ListOpsItemEventsRequestTypeDef,
    ListOpsItemEventsResponseTypeDef,
    ListOpsItemRelatedItemsRequestTypeDef,
    ListOpsItemRelatedItemsResponseTypeDef,
    ListOpsMetadataRequestTypeDef,
    ListOpsMetadataResultTypeDef,
    ListResourceComplianceSummariesRequestTypeDef,
    ListResourceComplianceSummariesResultTypeDef,
    ListResourceDataSyncRequestTypeDef,
    ListResourceDataSyncResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    ModifyDocumentPermissionRequestTypeDef,
    PutComplianceItemsRequestTypeDef,
    PutInventoryRequestTypeDef,
    PutInventoryResultTypeDef,
    PutParameterRequestTypeDef,
    PutParameterResultTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    RegisterDefaultPatchBaselineRequestTypeDef,
    RegisterDefaultPatchBaselineResultTypeDef,
    RegisterPatchBaselineForPatchGroupRequestTypeDef,
    RegisterPatchBaselineForPatchGroupResultTypeDef,
    RegisterTargetWithMaintenanceWindowRequestTypeDef,
    RegisterTargetWithMaintenanceWindowResultTypeDef,
    RegisterTaskWithMaintenanceWindowRequestTypeDef,
    RegisterTaskWithMaintenanceWindowResultTypeDef,
    RemoveTagsFromResourceRequestTypeDef,
    ResetServiceSettingRequestTypeDef,
    ResetServiceSettingResultTypeDef,
    ResumeSessionRequestTypeDef,
    ResumeSessionResponseTypeDef,
    SendAutomationSignalRequestTypeDef,
    SendCommandRequestTypeDef,
    SendCommandResultTypeDef,
    StartAccessRequestRequestTypeDef,
    StartAccessRequestResponseTypeDef,
    StartAssociationsOnceRequestTypeDef,
    StartAutomationExecutionRequestTypeDef,
    StartAutomationExecutionResultTypeDef,
    StartChangeRequestExecutionRequestTypeDef,
    StartChangeRequestExecutionResultTypeDef,
    StartExecutionPreviewRequestTypeDef,
    StartExecutionPreviewResponseTypeDef,
    StartSessionRequestTypeDef,
    StartSessionResponseTypeDef,
    StopAutomationExecutionRequestTypeDef,
    TerminateSessionRequestTypeDef,
    TerminateSessionResponseTypeDef,
    UnlabelParameterVersionRequestTypeDef,
    UnlabelParameterVersionResultTypeDef,
    UpdateAssociationRequestTypeDef,
    UpdateAssociationResultTypeDef,
    UpdateAssociationStatusRequestTypeDef,
    UpdateAssociationStatusResultTypeDef,
    UpdateDocumentDefaultVersionRequestTypeDef,
    UpdateDocumentDefaultVersionResultTypeDef,
    UpdateDocumentMetadataRequestTypeDef,
    UpdateDocumentRequestTypeDef,
    UpdateDocumentResultTypeDef,
    UpdateMaintenanceWindowRequestTypeDef,
    UpdateMaintenanceWindowResultTypeDef,
    UpdateMaintenanceWindowTargetRequestTypeDef,
    UpdateMaintenanceWindowTargetResultTypeDef,
    UpdateMaintenanceWindowTaskRequestTypeDef,
    UpdateMaintenanceWindowTaskResultTypeDef,
    UpdateManagedInstanceRoleRequestTypeDef,
    UpdateOpsItemRequestTypeDef,
    UpdateOpsMetadataRequestTypeDef,
    UpdateOpsMetadataResultTypeDef,
    UpdatePatchBaselineRequestTypeDef,
    UpdatePatchBaselineResultTypeDef,
    UpdateResourceDataSyncRequestTypeDef,
    UpdateServiceSettingRequestTypeDef,
)
from .waiter import CommandExecutedWaiter

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("SSMClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
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
    InvalidInstancePropertyFilterValue: Type[BotocoreClientError]
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
    InvalidTag: Type[BotocoreClientError]
    InvalidTarget: Type[BotocoreClientError]
    InvalidTargetMaps: Type[BotocoreClientError]
    InvalidTypeNameException: Type[BotocoreClientError]
    InvalidUpdate: Type[BotocoreClientError]
    InvocationDoesNotExist: Type[BotocoreClientError]
    ItemContentMismatchException: Type[BotocoreClientError]
    ItemSizeLimitExceededException: Type[BotocoreClientError]
    MalformedResourcePolicyDocumentException: Type[BotocoreClientError]
    MaxDocumentSizeExceeded: Type[BotocoreClientError]
    OpsItemAccessDeniedException: Type[BotocoreClientError]
    OpsItemAlreadyExistsException: Type[BotocoreClientError]
    OpsItemConflictException: Type[BotocoreClientError]
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
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourcePolicyConflictException: Type[BotocoreClientError]
    ResourcePolicyInvalidParameterException: Type[BotocoreClientError]
    ResourcePolicyLimitExceededException: Type[BotocoreClientError]
    ResourcePolicyNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ServiceSettingNotFound: Type[BotocoreClientError]
    StatusUnchanged: Type[BotocoreClientError]
    SubTypeCountLimitExceededException: Type[BotocoreClientError]
    TargetInUseException: Type[BotocoreClientError]
    TargetNotConnected: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyTagsError: Type[BotocoreClientError]
    TooManyUpdates: Type[BotocoreClientError]
    TotalSizeLimitExceededException: Type[BotocoreClientError]
    UnsupportedCalendarException: Type[BotocoreClientError]
    UnsupportedFeatureRequiredException: Type[BotocoreClientError]
    UnsupportedInventoryItemContextException: Type[BotocoreClientError]
    UnsupportedInventorySchemaVersionException: Type[BotocoreClientError]
    UnsupportedOperatingSystem: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]
    UnsupportedParameterType: Type[BotocoreClientError]
    UnsupportedPlatformType: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SSMClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSMClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#generate_presigned_url)
        """

    def add_tags_to_resource(
        self, **kwargs: Unpack[AddTagsToResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds or overwrites one or more tags for the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/add_tags_to_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#add_tags_to_resource)
        """

    def associate_ops_item_related_item(
        self, **kwargs: Unpack[AssociateOpsItemRelatedItemRequestTypeDef]
    ) -> AssociateOpsItemRelatedItemResponseTypeDef:
        """
        Associates a related item to a Systems Manager OpsCenter OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/associate_ops_item_related_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#associate_ops_item_related_item)
        """

    def cancel_command(self, **kwargs: Unpack[CancelCommandRequestTypeDef]) -> Dict[str, Any]:
        """
        Attempts to cancel the command specified by the Command ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/cancel_command.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#cancel_command)
        """

    def cancel_maintenance_window_execution(
        self, **kwargs: Unpack[CancelMaintenanceWindowExecutionRequestTypeDef]
    ) -> CancelMaintenanceWindowExecutionResultTypeDef:
        """
        Stops a maintenance window execution that is already in progress and cancels
        any tasks in the window that haven't already starting running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/cancel_maintenance_window_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#cancel_maintenance_window_execution)
        """

    def create_activation(
        self, **kwargs: Unpack[CreateActivationRequestTypeDef]
    ) -> CreateActivationResultTypeDef:
        """
        Generates an activation code and activation ID you can use to register your
        on-premises servers, edge devices, or virtual machine (VM) with Amazon Web
        Services Systems Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_activation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_activation)
        """

    def create_association(
        self, **kwargs: Unpack[CreateAssociationRequestTypeDef]
    ) -> CreateAssociationResultTypeDef:
        """
        A State Manager association defines the state that you want to maintain on your
        managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_association)
        """

    def create_association_batch(
        self, **kwargs: Unpack[CreateAssociationBatchRequestTypeDef]
    ) -> CreateAssociationBatchResultTypeDef:
        """
        Associates the specified Amazon Web Services Systems Manager document (SSM
        document) with the specified managed nodes or targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_association_batch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_association_batch)
        """

    def create_document(
        self, **kwargs: Unpack[CreateDocumentRequestTypeDef]
    ) -> CreateDocumentResultTypeDef:
        """
        Creates a Amazon Web Services Systems Manager (SSM document).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_document)
        """

    def create_maintenance_window(
        self, **kwargs: Unpack[CreateMaintenanceWindowRequestTypeDef]
    ) -> CreateMaintenanceWindowResultTypeDef:
        """
        Creates a new maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_maintenance_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_maintenance_window)
        """

    def create_ops_item(
        self, **kwargs: Unpack[CreateOpsItemRequestTypeDef]
    ) -> CreateOpsItemResponseTypeDef:
        """
        Creates a new OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_ops_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_ops_item)
        """

    def create_ops_metadata(
        self, **kwargs: Unpack[CreateOpsMetadataRequestTypeDef]
    ) -> CreateOpsMetadataResultTypeDef:
        """
        If you create a new application in Application Manager, Amazon Web Services
        Systems Manager calls this API operation to specify information about the new
        application, including the application type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_ops_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_ops_metadata)
        """

    def create_patch_baseline(
        self, **kwargs: Unpack[CreatePatchBaselineRequestTypeDef]
    ) -> CreatePatchBaselineResultTypeDef:
        """
        Creates a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_patch_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_patch_baseline)
        """

    def create_resource_data_sync(
        self, **kwargs: Unpack[CreateResourceDataSyncRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        A resource data sync helps you view data from multiple sources in a single
        location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/create_resource_data_sync.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#create_resource_data_sync)
        """

    def delete_activation(self, **kwargs: Unpack[DeleteActivationRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes an activation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_activation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_activation)
        """

    def delete_association(
        self, **kwargs: Unpack[DeleteAssociationRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Disassociates the specified Amazon Web Services Systems Manager document (SSM
        document) from the specified managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_association)
        """

    def delete_document(self, **kwargs: Unpack[DeleteDocumentRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the Amazon Web Services Systems Manager document (SSM document) and all
        managed node associations to the document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_document)
        """

    def delete_inventory(
        self, **kwargs: Unpack[DeleteInventoryRequestTypeDef]
    ) -> DeleteInventoryResultTypeDef:
        """
        Delete a custom inventory type or the data associated with a custom Inventory
        type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_inventory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_inventory)
        """

    def delete_maintenance_window(
        self, **kwargs: Unpack[DeleteMaintenanceWindowRequestTypeDef]
    ) -> DeleteMaintenanceWindowResultTypeDef:
        """
        Deletes a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_maintenance_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_maintenance_window)
        """

    def delete_ops_item(self, **kwargs: Unpack[DeleteOpsItemRequestTypeDef]) -> Dict[str, Any]:
        """
        Delete an OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_ops_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_ops_item)
        """

    def delete_ops_metadata(
        self, **kwargs: Unpack[DeleteOpsMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Delete OpsMetadata related to an application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_ops_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_ops_metadata)
        """

    def delete_parameter(self, **kwargs: Unpack[DeleteParameterRequestTypeDef]) -> Dict[str, Any]:
        """
        Delete a parameter from the system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_parameter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_parameter)
        """

    def delete_parameters(
        self, **kwargs: Unpack[DeleteParametersRequestTypeDef]
    ) -> DeleteParametersResultTypeDef:
        """
        Delete a list of parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_parameters)
        """

    def delete_patch_baseline(
        self, **kwargs: Unpack[DeletePatchBaselineRequestTypeDef]
    ) -> DeletePatchBaselineResultTypeDef:
        """
        Deletes a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_patch_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_patch_baseline)
        """

    def delete_resource_data_sync(
        self, **kwargs: Unpack[DeleteResourceDataSyncRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a resource data sync configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_resource_data_sync.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_resource_data_sync)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a Systems Manager resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#delete_resource_policy)
        """

    def deregister_managed_instance(
        self, **kwargs: Unpack[DeregisterManagedInstanceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes the server or virtual machine from the list of registered servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/deregister_managed_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#deregister_managed_instance)
        """

    def deregister_patch_baseline_for_patch_group(
        self, **kwargs: Unpack[DeregisterPatchBaselineForPatchGroupRequestTypeDef]
    ) -> DeregisterPatchBaselineForPatchGroupResultTypeDef:
        """
        Removes a patch group from a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/deregister_patch_baseline_for_patch_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#deregister_patch_baseline_for_patch_group)
        """

    def deregister_target_from_maintenance_window(
        self, **kwargs: Unpack[DeregisterTargetFromMaintenanceWindowRequestTypeDef]
    ) -> DeregisterTargetFromMaintenanceWindowResultTypeDef:
        """
        Removes a target from a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/deregister_target_from_maintenance_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#deregister_target_from_maintenance_window)
        """

    def deregister_task_from_maintenance_window(
        self, **kwargs: Unpack[DeregisterTaskFromMaintenanceWindowRequestTypeDef]
    ) -> DeregisterTaskFromMaintenanceWindowResultTypeDef:
        """
        Removes a task from a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/deregister_task_from_maintenance_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#deregister_task_from_maintenance_window)
        """

    def describe_activations(
        self, **kwargs: Unpack[DescribeActivationsRequestTypeDef]
    ) -> DescribeActivationsResultTypeDef:
        """
        Describes details about the activation, such as the date and time the
        activation was created, its expiration date, the Identity and Access Management
        (IAM) role assigned to the managed nodes in the activation, and the number of
        nodes registered by using this activation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_activations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_activations)
        """

    def describe_association(
        self, **kwargs: Unpack[DescribeAssociationRequestTypeDef]
    ) -> DescribeAssociationResultTypeDef:
        """
        Describes the association for the specified target or managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_association)
        """

    def describe_association_execution_targets(
        self, **kwargs: Unpack[DescribeAssociationExecutionTargetsRequestTypeDef]
    ) -> DescribeAssociationExecutionTargetsResultTypeDef:
        """
        Views information about a specific execution of a specific association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_association_execution_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_association_execution_targets)
        """

    def describe_association_executions(
        self, **kwargs: Unpack[DescribeAssociationExecutionsRequestTypeDef]
    ) -> DescribeAssociationExecutionsResultTypeDef:
        """
        Views all executions for a specific association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_association_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_association_executions)
        """

    def describe_automation_executions(
        self, **kwargs: Unpack[DescribeAutomationExecutionsRequestTypeDef]
    ) -> DescribeAutomationExecutionsResultTypeDef:
        """
        Provides details about all active and terminated Automation executions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_automation_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_automation_executions)
        """

    def describe_automation_step_executions(
        self, **kwargs: Unpack[DescribeAutomationStepExecutionsRequestTypeDef]
    ) -> DescribeAutomationStepExecutionsResultTypeDef:
        """
        Information about all active and terminated step executions in an Automation
        workflow.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_automation_step_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_automation_step_executions)
        """

    def describe_available_patches(
        self, **kwargs: Unpack[DescribeAvailablePatchesRequestTypeDef]
    ) -> DescribeAvailablePatchesResultTypeDef:
        """
        Lists all patches eligible to be included in a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_available_patches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_available_patches)
        """

    def describe_document(
        self, **kwargs: Unpack[DescribeDocumentRequestTypeDef]
    ) -> DescribeDocumentResultTypeDef:
        """
        Describes the specified Amazon Web Services Systems Manager document (SSM
        document).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_document)
        """

    def describe_document_permission(
        self, **kwargs: Unpack[DescribeDocumentPermissionRequestTypeDef]
    ) -> DescribeDocumentPermissionResponseTypeDef:
        """
        Describes the permissions for a Amazon Web Services Systems Manager document
        (SSM document).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_document_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_document_permission)
        """

    def describe_effective_instance_associations(
        self, **kwargs: Unpack[DescribeEffectiveInstanceAssociationsRequestTypeDef]
    ) -> DescribeEffectiveInstanceAssociationsResultTypeDef:
        """
        All associations for the managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_effective_instance_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_effective_instance_associations)
        """

    def describe_effective_patches_for_patch_baseline(
        self, **kwargs: Unpack[DescribeEffectivePatchesForPatchBaselineRequestTypeDef]
    ) -> DescribeEffectivePatchesForPatchBaselineResultTypeDef:
        """
        Retrieves the current effective patches (the patch and the approval state) for
        the specified patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_effective_patches_for_patch_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_effective_patches_for_patch_baseline)
        """

    def describe_instance_associations_status(
        self, **kwargs: Unpack[DescribeInstanceAssociationsStatusRequestTypeDef]
    ) -> DescribeInstanceAssociationsStatusResultTypeDef:
        """
        The status of the associations for the managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_instance_associations_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_instance_associations_status)
        """

    def describe_instance_information(
        self, **kwargs: Unpack[DescribeInstanceInformationRequestTypeDef]
    ) -> DescribeInstanceInformationResultTypeDef:
        """
        Provides information about one or more of your managed nodes, including the
        operating system platform, SSM Agent version, association status, and IP
        address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_instance_information.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_instance_information)
        """

    def describe_instance_patch_states(
        self, **kwargs: Unpack[DescribeInstancePatchStatesRequestTypeDef]
    ) -> DescribeInstancePatchStatesResultTypeDef:
        """
        Retrieves the high-level patch state of one or more managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_instance_patch_states.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_instance_patch_states)
        """

    def describe_instance_patch_states_for_patch_group(
        self, **kwargs: Unpack[DescribeInstancePatchStatesForPatchGroupRequestTypeDef]
    ) -> DescribeInstancePatchStatesForPatchGroupResultTypeDef:
        """
        Retrieves the high-level patch state for the managed nodes in the specified
        patch group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_instance_patch_states_for_patch_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_instance_patch_states_for_patch_group)
        """

    def describe_instance_patches(
        self, **kwargs: Unpack[DescribeInstancePatchesRequestTypeDef]
    ) -> DescribeInstancePatchesResultTypeDef:
        """
        Retrieves information about the patches on the specified managed node and their
        state relative to the patch baseline being used for the node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_instance_patches.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_instance_patches)
        """

    def describe_instance_properties(
        self, **kwargs: Unpack[DescribeInstancePropertiesRequestTypeDef]
    ) -> DescribeInstancePropertiesResultTypeDef:
        """
        An API operation used by the Systems Manager console to display information
        about Systems Manager managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_instance_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_instance_properties)
        """

    def describe_inventory_deletions(
        self, **kwargs: Unpack[DescribeInventoryDeletionsRequestTypeDef]
    ) -> DescribeInventoryDeletionsResultTypeDef:
        """
        Describes a specific delete inventory operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_inventory_deletions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_inventory_deletions)
        """

    def describe_maintenance_window_execution_task_invocations(
        self, **kwargs: Unpack[DescribeMaintenanceWindowExecutionTaskInvocationsRequestTypeDef]
    ) -> DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef:
        """
        Retrieves the individual task executions (one per target) for a particular task
        run as part of a maintenance window execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_maintenance_window_execution_task_invocations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_maintenance_window_execution_task_invocations)
        """

    def describe_maintenance_window_execution_tasks(
        self, **kwargs: Unpack[DescribeMaintenanceWindowExecutionTasksRequestTypeDef]
    ) -> DescribeMaintenanceWindowExecutionTasksResultTypeDef:
        """
        For a given maintenance window execution, lists the tasks that were run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_maintenance_window_execution_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_maintenance_window_execution_tasks)
        """

    def describe_maintenance_window_executions(
        self, **kwargs: Unpack[DescribeMaintenanceWindowExecutionsRequestTypeDef]
    ) -> DescribeMaintenanceWindowExecutionsResultTypeDef:
        """
        Lists the executions of a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_maintenance_window_executions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_maintenance_window_executions)
        """

    def describe_maintenance_window_schedule(
        self, **kwargs: Unpack[DescribeMaintenanceWindowScheduleRequestTypeDef]
    ) -> DescribeMaintenanceWindowScheduleResultTypeDef:
        """
        Retrieves information about upcoming executions of a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_maintenance_window_schedule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_maintenance_window_schedule)
        """

    def describe_maintenance_window_targets(
        self, **kwargs: Unpack[DescribeMaintenanceWindowTargetsRequestTypeDef]
    ) -> DescribeMaintenanceWindowTargetsResultTypeDef:
        """
        Lists the targets registered with the maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_maintenance_window_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_maintenance_window_targets)
        """

    def describe_maintenance_window_tasks(
        self, **kwargs: Unpack[DescribeMaintenanceWindowTasksRequestTypeDef]
    ) -> DescribeMaintenanceWindowTasksResultTypeDef:
        """
        Lists the tasks in a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_maintenance_window_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_maintenance_window_tasks)
        """

    def describe_maintenance_windows(
        self, **kwargs: Unpack[DescribeMaintenanceWindowsRequestTypeDef]
    ) -> DescribeMaintenanceWindowsResultTypeDef:
        """
        Retrieves the maintenance windows in an Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_maintenance_windows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_maintenance_windows)
        """

    def describe_maintenance_windows_for_target(
        self, **kwargs: Unpack[DescribeMaintenanceWindowsForTargetRequestTypeDef]
    ) -> DescribeMaintenanceWindowsForTargetResultTypeDef:
        """
        Retrieves information about the maintenance window targets or tasks that a
        managed node is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_maintenance_windows_for_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_maintenance_windows_for_target)
        """

    def describe_ops_items(
        self, **kwargs: Unpack[DescribeOpsItemsRequestTypeDef]
    ) -> DescribeOpsItemsResponseTypeDef:
        """
        Query a set of OpsItems.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_ops_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_ops_items)
        """

    def describe_parameters(
        self, **kwargs: Unpack[DescribeParametersRequestTypeDef]
    ) -> DescribeParametersResultTypeDef:
        """
        Lists the parameters in your Amazon Web Services account or the parameters
        shared with you when you enable the <a
        href="https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html#systemsmanager-DescribeParameters-request-Shared">Shared</a>
        option.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_parameters)
        """

    def describe_patch_baselines(
        self, **kwargs: Unpack[DescribePatchBaselinesRequestTypeDef]
    ) -> DescribePatchBaselinesResultTypeDef:
        """
        Lists the patch baselines in your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_patch_baselines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_patch_baselines)
        """

    def describe_patch_group_state(
        self, **kwargs: Unpack[DescribePatchGroupStateRequestTypeDef]
    ) -> DescribePatchGroupStateResultTypeDef:
        """
        Returns high-level aggregated patch compliance state information for a patch
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_patch_group_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_patch_group_state)
        """

    def describe_patch_groups(
        self, **kwargs: Unpack[DescribePatchGroupsRequestTypeDef]
    ) -> DescribePatchGroupsResultTypeDef:
        """
        Lists all patch groups that have been registered with patch baselines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_patch_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_patch_groups)
        """

    def describe_patch_properties(
        self, **kwargs: Unpack[DescribePatchPropertiesRequestTypeDef]
    ) -> DescribePatchPropertiesResultTypeDef:
        """
        Lists the properties of available patches organized by product, product family,
        classification, severity, and other properties of available patches.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_patch_properties.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_patch_properties)
        """

    def describe_sessions(
        self, **kwargs: Unpack[DescribeSessionsRequestTypeDef]
    ) -> DescribeSessionsResponseTypeDef:
        """
        Retrieves a list of all active sessions (both connected and disconnected) or
        terminated sessions from the past 30 days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/describe_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#describe_sessions)
        """

    def disassociate_ops_item_related_item(
        self, **kwargs: Unpack[DisassociateOpsItemRelatedItemRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the association between an OpsItem and a related item.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/disassociate_ops_item_related_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#disassociate_ops_item_related_item)
        """

    def get_access_token(
        self, **kwargs: Unpack[GetAccessTokenRequestTypeDef]
    ) -> GetAccessTokenResponseTypeDef:
        """
        Returns a credentials set to be used with just-in-time node access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_access_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_access_token)
        """

    def get_automation_execution(
        self, **kwargs: Unpack[GetAutomationExecutionRequestTypeDef]
    ) -> GetAutomationExecutionResultTypeDef:
        """
        Get detailed information about a particular Automation execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_automation_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_automation_execution)
        """

    def get_calendar_state(
        self, **kwargs: Unpack[GetCalendarStateRequestTypeDef]
    ) -> GetCalendarStateResponseTypeDef:
        """
        Gets the state of a Amazon Web Services Systems Manager change calendar at the
        current time or a specified time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_calendar_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_calendar_state)
        """

    def get_command_invocation(
        self, **kwargs: Unpack[GetCommandInvocationRequestTypeDef]
    ) -> GetCommandInvocationResultTypeDef:
        """
        Returns detailed information about command execution for an invocation or
        plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_command_invocation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_command_invocation)
        """

    def get_connection_status(
        self, **kwargs: Unpack[GetConnectionStatusRequestTypeDef]
    ) -> GetConnectionStatusResponseTypeDef:
        """
        Retrieves the Session Manager connection status for a managed node to determine
        whether it is running and ready to receive Session Manager connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_connection_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_connection_status)
        """

    def get_default_patch_baseline(
        self, **kwargs: Unpack[GetDefaultPatchBaselineRequestTypeDef]
    ) -> GetDefaultPatchBaselineResultTypeDef:
        """
        Retrieves the default patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_default_patch_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_default_patch_baseline)
        """

    def get_deployable_patch_snapshot_for_instance(
        self, **kwargs: Unpack[GetDeployablePatchSnapshotForInstanceRequestTypeDef]
    ) -> GetDeployablePatchSnapshotForInstanceResultTypeDef:
        """
        Retrieves the current snapshot for the patch baseline the managed node uses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_deployable_patch_snapshot_for_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_deployable_patch_snapshot_for_instance)
        """

    def get_document(self, **kwargs: Unpack[GetDocumentRequestTypeDef]) -> GetDocumentResultTypeDef:
        """
        Gets the contents of the specified Amazon Web Services Systems Manager document
        (SSM document).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_document)
        """

    def get_execution_preview(
        self, **kwargs: Unpack[GetExecutionPreviewRequestTypeDef]
    ) -> GetExecutionPreviewResponseTypeDef:
        """
        Initiates the process of retrieving an existing preview that shows the effects
        that running a specified Automation runbook would have on the targeted
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_execution_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_execution_preview)
        """

    def get_inventory(
        self, **kwargs: Unpack[GetInventoryRequestTypeDef]
    ) -> GetInventoryResultTypeDef:
        """
        Query inventory information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_inventory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_inventory)
        """

    def get_inventory_schema(
        self, **kwargs: Unpack[GetInventorySchemaRequestTypeDef]
    ) -> GetInventorySchemaResultTypeDef:
        """
        Return a list of inventory type names for the account, or return a list of
        attribute names for a specific Inventory item type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_inventory_schema.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_inventory_schema)
        """

    def get_maintenance_window(
        self, **kwargs: Unpack[GetMaintenanceWindowRequestTypeDef]
    ) -> GetMaintenanceWindowResultTypeDef:
        """
        Retrieves a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_maintenance_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_maintenance_window)
        """

    def get_maintenance_window_execution(
        self, **kwargs: Unpack[GetMaintenanceWindowExecutionRequestTypeDef]
    ) -> GetMaintenanceWindowExecutionResultTypeDef:
        """
        Retrieves details about a specific a maintenance window execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_maintenance_window_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_maintenance_window_execution)
        """

    def get_maintenance_window_execution_task(
        self, **kwargs: Unpack[GetMaintenanceWindowExecutionTaskRequestTypeDef]
    ) -> GetMaintenanceWindowExecutionTaskResultTypeDef:
        """
        Retrieves the details about a specific task run as part of a maintenance window
        execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_maintenance_window_execution_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_maintenance_window_execution_task)
        """

    def get_maintenance_window_execution_task_invocation(
        self, **kwargs: Unpack[GetMaintenanceWindowExecutionTaskInvocationRequestTypeDef]
    ) -> GetMaintenanceWindowExecutionTaskInvocationResultTypeDef:
        """
        Retrieves information about a specific task running on a specific target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_maintenance_window_execution_task_invocation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_maintenance_window_execution_task_invocation)
        """

    def get_maintenance_window_task(
        self, **kwargs: Unpack[GetMaintenanceWindowTaskRequestTypeDef]
    ) -> GetMaintenanceWindowTaskResultTypeDef:
        """
        Retrieves the details of a maintenance window task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_maintenance_window_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_maintenance_window_task)
        """

    def get_ops_item(self, **kwargs: Unpack[GetOpsItemRequestTypeDef]) -> GetOpsItemResponseTypeDef:
        """
        Get information about an OpsItem by using the ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_ops_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_ops_item)
        """

    def get_ops_metadata(
        self, **kwargs: Unpack[GetOpsMetadataRequestTypeDef]
    ) -> GetOpsMetadataResultTypeDef:
        """
        View operational metadata related to an application in Application Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_ops_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_ops_metadata)
        """

    def get_ops_summary(
        self, **kwargs: Unpack[GetOpsSummaryRequestTypeDef]
    ) -> GetOpsSummaryResultTypeDef:
        """
        View a summary of operations metadata (OpsData) based on specified filters and
        aggregators.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_ops_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_ops_summary)
        """

    def get_parameter(
        self, **kwargs: Unpack[GetParameterRequestTypeDef]
    ) -> GetParameterResultTypeDef:
        """
        Get information about a single parameter by specifying the parameter name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_parameter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_parameter)
        """

    def get_parameter_history(
        self, **kwargs: Unpack[GetParameterHistoryRequestTypeDef]
    ) -> GetParameterHistoryResultTypeDef:
        """
        Retrieves the history of all changes to a parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_parameter_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_parameter_history)
        """

    def get_parameters(
        self, **kwargs: Unpack[GetParametersRequestTypeDef]
    ) -> GetParametersResultTypeDef:
        """
        Get information about one or more parameters by specifying multiple parameter
        names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_parameters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_parameters)
        """

    def get_parameters_by_path(
        self, **kwargs: Unpack[GetParametersByPathRequestTypeDef]
    ) -> GetParametersByPathResultTypeDef:
        """
        Retrieve information about one or more parameters under a specified level in a
        hierarchy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_parameters_by_path.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_parameters_by_path)
        """

    def get_patch_baseline(
        self, **kwargs: Unpack[GetPatchBaselineRequestTypeDef]
    ) -> GetPatchBaselineResultTypeDef:
        """
        Retrieves information about a patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_patch_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_patch_baseline)
        """

    def get_patch_baseline_for_patch_group(
        self, **kwargs: Unpack[GetPatchBaselineForPatchGroupRequestTypeDef]
    ) -> GetPatchBaselineForPatchGroupResultTypeDef:
        """
        Retrieves the patch baseline that should be used for the specified patch group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_patch_baseline_for_patch_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_patch_baseline_for_patch_group)
        """

    def get_resource_policies(
        self, **kwargs: Unpack[GetResourcePoliciesRequestTypeDef]
    ) -> GetResourcePoliciesResponseTypeDef:
        """
        Returns an array of the <code>Policy</code> object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_resource_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_resource_policies)
        """

    def get_service_setting(
        self, **kwargs: Unpack[GetServiceSettingRequestTypeDef]
    ) -> GetServiceSettingResultTypeDef:
        """
        <code>ServiceSetting</code> is an account-level setting for an Amazon Web
        Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_service_setting.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_service_setting)
        """

    def label_parameter_version(
        self, **kwargs: Unpack[LabelParameterVersionRequestTypeDef]
    ) -> LabelParameterVersionResultTypeDef:
        """
        A parameter label is a user-defined alias to help you manage different versions
        of a parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/label_parameter_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#label_parameter_version)
        """

    def list_association_versions(
        self, **kwargs: Unpack[ListAssociationVersionsRequestTypeDef]
    ) -> ListAssociationVersionsResultTypeDef:
        """
        Retrieves all versions of an association for a specific association ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_association_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_association_versions)
        """

    def list_associations(
        self, **kwargs: Unpack[ListAssociationsRequestTypeDef]
    ) -> ListAssociationsResultTypeDef:
        """
        Returns all State Manager associations in the current Amazon Web Services
        account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_associations)
        """

    def list_command_invocations(
        self, **kwargs: Unpack[ListCommandInvocationsRequestTypeDef]
    ) -> ListCommandInvocationsResultTypeDef:
        """
        An invocation is copy of a command sent to a specific managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_command_invocations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_command_invocations)
        """

    def list_commands(
        self, **kwargs: Unpack[ListCommandsRequestTypeDef]
    ) -> ListCommandsResultTypeDef:
        """
        Lists the commands requested by users of the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_commands.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_commands)
        """

    def list_compliance_items(
        self, **kwargs: Unpack[ListComplianceItemsRequestTypeDef]
    ) -> ListComplianceItemsResultTypeDef:
        """
        For a specified resource ID, this API operation returns a list of compliance
        statuses for different resource types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_compliance_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_compliance_items)
        """

    def list_compliance_summaries(
        self, **kwargs: Unpack[ListComplianceSummariesRequestTypeDef]
    ) -> ListComplianceSummariesResultTypeDef:
        """
        Returns a summary count of compliant and non-compliant resources for a
        compliance type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_compliance_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_compliance_summaries)
        """

    def list_document_metadata_history(
        self, **kwargs: Unpack[ListDocumentMetadataHistoryRequestTypeDef]
    ) -> ListDocumentMetadataHistoryResponseTypeDef:
        """
        Information about approval reviews for a version of a change template in Change
        Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_document_metadata_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_document_metadata_history)
        """

    def list_document_versions(
        self, **kwargs: Unpack[ListDocumentVersionsRequestTypeDef]
    ) -> ListDocumentVersionsResultTypeDef:
        """
        List all versions for a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_document_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_document_versions)
        """

    def list_documents(
        self, **kwargs: Unpack[ListDocumentsRequestTypeDef]
    ) -> ListDocumentsResultTypeDef:
        """
        Returns all Systems Manager (SSM) documents in the current Amazon Web Services
        account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_documents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_documents)
        """

    def list_inventory_entries(
        self, **kwargs: Unpack[ListInventoryEntriesRequestTypeDef]
    ) -> ListInventoryEntriesResultTypeDef:
        """
        A list of inventory items returned by the request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_inventory_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_inventory_entries)
        """

    def list_nodes(self, **kwargs: Unpack[ListNodesRequestTypeDef]) -> ListNodesResultTypeDef:
        """
        Takes in filters and returns a list of managed nodes matching the filter
        criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_nodes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_nodes)
        """

    def list_nodes_summary(
        self, **kwargs: Unpack[ListNodesSummaryRequestTypeDef]
    ) -> ListNodesSummaryResultTypeDef:
        """
        Generates a summary of managed instance/node metadata based on the filters and
        aggregators you specify.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_nodes_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_nodes_summary)
        """

    def list_ops_item_events(
        self, **kwargs: Unpack[ListOpsItemEventsRequestTypeDef]
    ) -> ListOpsItemEventsResponseTypeDef:
        """
        Returns a list of all OpsItem events in the current Amazon Web Services Region
        and Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_ops_item_events.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_ops_item_events)
        """

    def list_ops_item_related_items(
        self, **kwargs: Unpack[ListOpsItemRelatedItemsRequestTypeDef]
    ) -> ListOpsItemRelatedItemsResponseTypeDef:
        """
        Lists all related-item resources associated with a Systems Manager OpsCenter
        OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_ops_item_related_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_ops_item_related_items)
        """

    def list_ops_metadata(
        self, **kwargs: Unpack[ListOpsMetadataRequestTypeDef]
    ) -> ListOpsMetadataResultTypeDef:
        """
        Amazon Web Services Systems Manager calls this API operation when displaying
        all Application Manager OpsMetadata objects or blobs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_ops_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_ops_metadata)
        """

    def list_resource_compliance_summaries(
        self, **kwargs: Unpack[ListResourceComplianceSummariesRequestTypeDef]
    ) -> ListResourceComplianceSummariesResultTypeDef:
        """
        Returns a resource-level summary count.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_resource_compliance_summaries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_resource_compliance_summaries)
        """

    def list_resource_data_sync(
        self, **kwargs: Unpack[ListResourceDataSyncRequestTypeDef]
    ) -> ListResourceDataSyncResultTypeDef:
        """
        Lists your resource data sync configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_resource_data_sync.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_resource_data_sync)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        Returns a list of the tags assigned to the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#list_tags_for_resource)
        """

    def modify_document_permission(
        self, **kwargs: Unpack[ModifyDocumentPermissionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Shares a Amazon Web Services Systems Manager document (SSM document)publicly or
        privately.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/modify_document_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#modify_document_permission)
        """

    def put_compliance_items(
        self, **kwargs: Unpack[PutComplianceItemsRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Registers a compliance type and other compliance details on a designated
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/put_compliance_items.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#put_compliance_items)
        """

    def put_inventory(
        self, **kwargs: Unpack[PutInventoryRequestTypeDef]
    ) -> PutInventoryResultTypeDef:
        """
        Bulk update custom inventory items on one or more managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/put_inventory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#put_inventory)
        """

    def put_parameter(
        self, **kwargs: Unpack[PutParameterRequestTypeDef]
    ) -> PutParameterResultTypeDef:
        """
        Create or update a parameter in Parameter Store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/put_parameter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#put_parameter)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates a Systems Manager resource policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#put_resource_policy)
        """

    def register_default_patch_baseline(
        self, **kwargs: Unpack[RegisterDefaultPatchBaselineRequestTypeDef]
    ) -> RegisterDefaultPatchBaselineResultTypeDef:
        """
        Defines the default patch baseline for the relevant operating system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/register_default_patch_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#register_default_patch_baseline)
        """

    def register_patch_baseline_for_patch_group(
        self, **kwargs: Unpack[RegisterPatchBaselineForPatchGroupRequestTypeDef]
    ) -> RegisterPatchBaselineForPatchGroupResultTypeDef:
        """
        Registers a patch baseline for a patch group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/register_patch_baseline_for_patch_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#register_patch_baseline_for_patch_group)
        """

    def register_target_with_maintenance_window(
        self, **kwargs: Unpack[RegisterTargetWithMaintenanceWindowRequestTypeDef]
    ) -> RegisterTargetWithMaintenanceWindowResultTypeDef:
        """
        Registers a target with a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/register_target_with_maintenance_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#register_target_with_maintenance_window)
        """

    def register_task_with_maintenance_window(
        self, **kwargs: Unpack[RegisterTaskWithMaintenanceWindowRequestTypeDef]
    ) -> RegisterTaskWithMaintenanceWindowResultTypeDef:
        """
        Adds a new task to a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/register_task_with_maintenance_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#register_task_with_maintenance_window)
        """

    def remove_tags_from_resource(
        self, **kwargs: Unpack[RemoveTagsFromResourceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Removes tag keys from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/remove_tags_from_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#remove_tags_from_resource)
        """

    def reset_service_setting(
        self, **kwargs: Unpack[ResetServiceSettingRequestTypeDef]
    ) -> ResetServiceSettingResultTypeDef:
        """
        <code>ServiceSetting</code> is an account-level setting for an Amazon Web
        Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/reset_service_setting.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#reset_service_setting)
        """

    def resume_session(
        self, **kwargs: Unpack[ResumeSessionRequestTypeDef]
    ) -> ResumeSessionResponseTypeDef:
        """
        Reconnects a session to a managed node after it has been disconnected.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/resume_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#resume_session)
        """

    def send_automation_signal(
        self, **kwargs: Unpack[SendAutomationSignalRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Sends a signal to an Automation execution to change the current behavior or
        status of the execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/send_automation_signal.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#send_automation_signal)
        """

    def send_command(self, **kwargs: Unpack[SendCommandRequestTypeDef]) -> SendCommandResultTypeDef:
        """
        Runs commands on one or more managed nodes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/send_command.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#send_command)
        """

    def start_access_request(
        self, **kwargs: Unpack[StartAccessRequestRequestTypeDef]
    ) -> StartAccessRequestResponseTypeDef:
        """
        Starts the workflow for just-in-time node access sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/start_access_request.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#start_access_request)
        """

    def start_associations_once(
        self, **kwargs: Unpack[StartAssociationsOnceRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Runs an association immediately and only one time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/start_associations_once.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#start_associations_once)
        """

    def start_automation_execution(
        self, **kwargs: Unpack[StartAutomationExecutionRequestTypeDef]
    ) -> StartAutomationExecutionResultTypeDef:
        """
        Initiates execution of an Automation runbook.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/start_automation_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#start_automation_execution)
        """

    def start_change_request_execution(
        self, **kwargs: Unpack[StartChangeRequestExecutionRequestTypeDef]
    ) -> StartChangeRequestExecutionResultTypeDef:
        """
        Creates a change request for Change Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/start_change_request_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#start_change_request_execution)
        """

    def start_execution_preview(
        self, **kwargs: Unpack[StartExecutionPreviewRequestTypeDef]
    ) -> StartExecutionPreviewResponseTypeDef:
        """
        Initiates the process of creating a preview showing the effects that running a
        specified Automation runbook would have on the targeted resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/start_execution_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#start_execution_preview)
        """

    def start_session(
        self, **kwargs: Unpack[StartSessionRequestTypeDef]
    ) -> StartSessionResponseTypeDef:
        """
        Initiates a connection to a target (for example, a managed node) for a Session
        Manager session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/start_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#start_session)
        """

    def stop_automation_execution(
        self, **kwargs: Unpack[StopAutomationExecutionRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Stop an Automation that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/stop_automation_execution.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#stop_automation_execution)
        """

    def terminate_session(
        self, **kwargs: Unpack[TerminateSessionRequestTypeDef]
    ) -> TerminateSessionResponseTypeDef:
        """
        Permanently ends a session and closes the data connection between the Session
        Manager client and SSM Agent on the managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/terminate_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#terminate_session)
        """

    def unlabel_parameter_version(
        self, **kwargs: Unpack[UnlabelParameterVersionRequestTypeDef]
    ) -> UnlabelParameterVersionResultTypeDef:
        """
        Remove a label or labels from a parameter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/unlabel_parameter_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#unlabel_parameter_version)
        """

    def update_association(
        self, **kwargs: Unpack[UpdateAssociationRequestTypeDef]
    ) -> UpdateAssociationResultTypeDef:
        """
        Updates an association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_association)
        """

    def update_association_status(
        self, **kwargs: Unpack[UpdateAssociationStatusRequestTypeDef]
    ) -> UpdateAssociationStatusResultTypeDef:
        """
        Updates the status of the Amazon Web Services Systems Manager document (SSM
        document) associated with the specified managed node.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_association_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_association_status)
        """

    def update_document(
        self, **kwargs: Unpack[UpdateDocumentRequestTypeDef]
    ) -> UpdateDocumentResultTypeDef:
        """
        Updates one or more values for an SSM document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_document.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_document)
        """

    def update_document_default_version(
        self, **kwargs: Unpack[UpdateDocumentDefaultVersionRequestTypeDef]
    ) -> UpdateDocumentDefaultVersionResultTypeDef:
        """
        Set the default version of a document.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_document_default_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_document_default_version)
        """

    def update_document_metadata(
        self, **kwargs: Unpack[UpdateDocumentMetadataRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Updates information related to approval reviews for a specific version of a
        change template in Change Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_document_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_document_metadata)
        """

    def update_maintenance_window(
        self, **kwargs: Unpack[UpdateMaintenanceWindowRequestTypeDef]
    ) -> UpdateMaintenanceWindowResultTypeDef:
        """
        Updates an existing maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_maintenance_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_maintenance_window)
        """

    def update_maintenance_window_target(
        self, **kwargs: Unpack[UpdateMaintenanceWindowTargetRequestTypeDef]
    ) -> UpdateMaintenanceWindowTargetResultTypeDef:
        """
        Modifies the target of an existing maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_maintenance_window_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_maintenance_window_target)
        """

    def update_maintenance_window_task(
        self, **kwargs: Unpack[UpdateMaintenanceWindowTaskRequestTypeDef]
    ) -> UpdateMaintenanceWindowTaskResultTypeDef:
        """
        Modifies a task assigned to a maintenance window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_maintenance_window_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_maintenance_window_task)
        """

    def update_managed_instance_role(
        self, **kwargs: Unpack[UpdateManagedInstanceRoleRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Changes the Identity and Access Management (IAM) role that is assigned to the
        on-premises server, edge device, or virtual machines (VM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_managed_instance_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_managed_instance_role)
        """

    def update_ops_item(self, **kwargs: Unpack[UpdateOpsItemRequestTypeDef]) -> Dict[str, Any]:
        """
        Edit or change an OpsItem.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_ops_item.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_ops_item)
        """

    def update_ops_metadata(
        self, **kwargs: Unpack[UpdateOpsMetadataRequestTypeDef]
    ) -> UpdateOpsMetadataResultTypeDef:
        """
        Amazon Web Services Systems Manager calls this API operation when you edit
        OpsMetadata in Application Manager.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_ops_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_ops_metadata)
        """

    def update_patch_baseline(
        self, **kwargs: Unpack[UpdatePatchBaselineRequestTypeDef]
    ) -> UpdatePatchBaselineResultTypeDef:
        """
        Modifies an existing patch baseline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_patch_baseline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_patch_baseline)
        """

    def update_resource_data_sync(
        self, **kwargs: Unpack[UpdateResourceDataSyncRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Update a resource data sync.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_resource_data_sync.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_resource_data_sync)
        """

    def update_service_setting(
        self, **kwargs: Unpack[UpdateServiceSettingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        <code>ServiceSetting</code> is an account-level setting for an Amazon Web
        Services service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/update_service_setting.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#update_service_setting)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_activations"]
    ) -> DescribeActivationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_association_execution_targets"]
    ) -> DescribeAssociationExecutionTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_association_executions"]
    ) -> DescribeAssociationExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_automation_executions"]
    ) -> DescribeAutomationExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_automation_step_executions"]
    ) -> DescribeAutomationStepExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_available_patches"]
    ) -> DescribeAvailablePatchesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_effective_instance_associations"]
    ) -> DescribeEffectiveInstanceAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_effective_patches_for_patch_baseline"]
    ) -> DescribeEffectivePatchesForPatchBaselinePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_associations_status"]
    ) -> DescribeInstanceAssociationsStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_information"]
    ) -> DescribeInstanceInformationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_patch_states_for_patch_group"]
    ) -> DescribeInstancePatchStatesForPatchGroupPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_patch_states"]
    ) -> DescribeInstancePatchStatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_patches"]
    ) -> DescribeInstancePatchesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_properties"]
    ) -> DescribeInstancePropertiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_inventory_deletions"]
    ) -> DescribeInventoryDeletionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_maintenance_window_execution_task_invocations"]
    ) -> DescribeMaintenanceWindowExecutionTaskInvocationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_maintenance_window_execution_tasks"]
    ) -> DescribeMaintenanceWindowExecutionTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_maintenance_window_executions"]
    ) -> DescribeMaintenanceWindowExecutionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_maintenance_window_schedule"]
    ) -> DescribeMaintenanceWindowSchedulePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_maintenance_window_targets"]
    ) -> DescribeMaintenanceWindowTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_maintenance_window_tasks"]
    ) -> DescribeMaintenanceWindowTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_maintenance_windows_for_target"]
    ) -> DescribeMaintenanceWindowsForTargetPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_maintenance_windows"]
    ) -> DescribeMaintenanceWindowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ops_items"]
    ) -> DescribeOpsItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_parameters"]
    ) -> DescribeParametersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_patch_baselines"]
    ) -> DescribePatchBaselinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_patch_groups"]
    ) -> DescribePatchGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_patch_properties"]
    ) -> DescribePatchPropertiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_sessions"]
    ) -> DescribeSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_inventory"]
    ) -> GetInventoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_inventory_schema"]
    ) -> GetInventorySchemaPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_ops_summary"]
    ) -> GetOpsSummaryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_parameter_history"]
    ) -> GetParameterHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_parameters_by_path"]
    ) -> GetParametersByPathPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_resource_policies"]
    ) -> GetResourcePoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_association_versions"]
    ) -> ListAssociationVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associations"]
    ) -> ListAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_command_invocations"]
    ) -> ListCommandInvocationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_commands"]
    ) -> ListCommandsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_compliance_items"]
    ) -> ListComplianceItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_compliance_summaries"]
    ) -> ListComplianceSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_document_versions"]
    ) -> ListDocumentVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_documents"]
    ) -> ListDocumentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_nodes"]
    ) -> ListNodesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_nodes_summary"]
    ) -> ListNodesSummaryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ops_item_events"]
    ) -> ListOpsItemEventsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ops_item_related_items"]
    ) -> ListOpsItemRelatedItemsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_ops_metadata"]
    ) -> ListOpsMetadataPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_compliance_summaries"]
    ) -> ListResourceComplianceSummariesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_resource_data_sync"]
    ) -> ListResourceDataSyncPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_paginator)
        """

    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["command_executed"]
    ) -> CommandExecutedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/client/#get_waiter)
        """
