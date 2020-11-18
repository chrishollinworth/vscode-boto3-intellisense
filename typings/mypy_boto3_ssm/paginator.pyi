# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for ssm service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_ssm import SSMClient
    from mypy_boto3_ssm.paginator import (
        DescribeActivationsPaginator,
        DescribeAssociationExecutionTargetsPaginator,
        DescribeAssociationExecutionsPaginator,
        DescribeAutomationExecutionsPaginator,
        DescribeAutomationStepExecutionsPaginator,
        DescribeAvailablePatchesPaginator,
        DescribeEffectiveInstanceAssociationsPaginator,
        DescribeEffectivePatchesForPatchBaselinePaginator,
        DescribeInstanceAssociationsStatusPaginator,
        DescribeInstanceInformationPaginator,
        DescribeInstancePatchStatesPaginator,
        DescribeInstancePatchStatesForPatchGroupPaginator,
        DescribeInstancePatchesPaginator,
        DescribeInventoryDeletionsPaginator,
        DescribeMaintenanceWindowExecutionTaskInvocationsPaginator,
        DescribeMaintenanceWindowExecutionTasksPaginator,
        DescribeMaintenanceWindowExecutionsPaginator,
        DescribeMaintenanceWindowSchedulePaginator,
        DescribeMaintenanceWindowTargetsPaginator,
        DescribeMaintenanceWindowTasksPaginator,
        DescribeMaintenanceWindowsPaginator,
        DescribeMaintenanceWindowsForTargetPaginator,
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
        ListAssociationVersionsPaginator,
        ListAssociationsPaginator,
        ListCommandInvocationsPaginator,
        ListCommandsPaginator,
        ListComplianceItemsPaginator,
        ListComplianceSummariesPaginator,
        ListDocumentVersionsPaginator,
        ListDocumentsPaginator,
        ListResourceComplianceSummariesPaginator,
        ListResourceDataSyncPaginator,
    )

    client: SSMClient = boto3.client("ssm")

    describe_activations_paginator: DescribeActivationsPaginator = client.get_paginator("describe_activations")
    describe_association_execution_targets_paginator: DescribeAssociationExecutionTargetsPaginator = client.get_paginator("describe_association_execution_targets")
    describe_association_executions_paginator: DescribeAssociationExecutionsPaginator = client.get_paginator("describe_association_executions")
    describe_automation_executions_paginator: DescribeAutomationExecutionsPaginator = client.get_paginator("describe_automation_executions")
    describe_automation_step_executions_paginator: DescribeAutomationStepExecutionsPaginator = client.get_paginator("describe_automation_step_executions")
    describe_available_patches_paginator: DescribeAvailablePatchesPaginator = client.get_paginator("describe_available_patches")
    describe_effective_instance_associations_paginator: DescribeEffectiveInstanceAssociationsPaginator = client.get_paginator("describe_effective_instance_associations")
    describe_effective_patches_for_patch_baseline_paginator: DescribeEffectivePatchesForPatchBaselinePaginator = client.get_paginator("describe_effective_patches_for_patch_baseline")
    describe_instance_associations_status_paginator: DescribeInstanceAssociationsStatusPaginator = client.get_paginator("describe_instance_associations_status")
    describe_instance_information_paginator: DescribeInstanceInformationPaginator = client.get_paginator("describe_instance_information")
    describe_instance_patch_states_paginator: DescribeInstancePatchStatesPaginator = client.get_paginator("describe_instance_patch_states")
    describe_instance_patch_states_for_patch_group_paginator: DescribeInstancePatchStatesForPatchGroupPaginator = client.get_paginator("describe_instance_patch_states_for_patch_group")
    describe_instance_patches_paginator: DescribeInstancePatchesPaginator = client.get_paginator("describe_instance_patches")
    describe_inventory_deletions_paginator: DescribeInventoryDeletionsPaginator = client.get_paginator("describe_inventory_deletions")
    describe_maintenance_window_execution_task_invocations_paginator: DescribeMaintenanceWindowExecutionTaskInvocationsPaginator = client.get_paginator("describe_maintenance_window_execution_task_invocations")
    describe_maintenance_window_execution_tasks_paginator: DescribeMaintenanceWindowExecutionTasksPaginator = client.get_paginator("describe_maintenance_window_execution_tasks")
    describe_maintenance_window_executions_paginator: DescribeMaintenanceWindowExecutionsPaginator = client.get_paginator("describe_maintenance_window_executions")
    describe_maintenance_window_schedule_paginator: DescribeMaintenanceWindowSchedulePaginator = client.get_paginator("describe_maintenance_window_schedule")
    describe_maintenance_window_targets_paginator: DescribeMaintenanceWindowTargetsPaginator = client.get_paginator("describe_maintenance_window_targets")
    describe_maintenance_window_tasks_paginator: DescribeMaintenanceWindowTasksPaginator = client.get_paginator("describe_maintenance_window_tasks")
    describe_maintenance_windows_paginator: DescribeMaintenanceWindowsPaginator = client.get_paginator("describe_maintenance_windows")
    describe_maintenance_windows_for_target_paginator: DescribeMaintenanceWindowsForTargetPaginator = client.get_paginator("describe_maintenance_windows_for_target")
    describe_ops_items_paginator: DescribeOpsItemsPaginator = client.get_paginator("describe_ops_items")
    describe_parameters_paginator: DescribeParametersPaginator = client.get_paginator("describe_parameters")
    describe_patch_baselines_paginator: DescribePatchBaselinesPaginator = client.get_paginator("describe_patch_baselines")
    describe_patch_groups_paginator: DescribePatchGroupsPaginator = client.get_paginator("describe_patch_groups")
    describe_patch_properties_paginator: DescribePatchPropertiesPaginator = client.get_paginator("describe_patch_properties")
    describe_sessions_paginator: DescribeSessionsPaginator = client.get_paginator("describe_sessions")
    get_inventory_paginator: GetInventoryPaginator = client.get_paginator("get_inventory")
    get_inventory_schema_paginator: GetInventorySchemaPaginator = client.get_paginator("get_inventory_schema")
    get_ops_summary_paginator: GetOpsSummaryPaginator = client.get_paginator("get_ops_summary")
    get_parameter_history_paginator: GetParameterHistoryPaginator = client.get_paginator("get_parameter_history")
    get_parameters_by_path_paginator: GetParametersByPathPaginator = client.get_paginator("get_parameters_by_path")
    list_association_versions_paginator: ListAssociationVersionsPaginator = client.get_paginator("list_association_versions")
    list_associations_paginator: ListAssociationsPaginator = client.get_paginator("list_associations")
    list_command_invocations_paginator: ListCommandInvocationsPaginator = client.get_paginator("list_command_invocations")
    list_commands_paginator: ListCommandsPaginator = client.get_paginator("list_commands")
    list_compliance_items_paginator: ListComplianceItemsPaginator = client.get_paginator("list_compliance_items")
    list_compliance_summaries_paginator: ListComplianceSummariesPaginator = client.get_paginator("list_compliance_summaries")
    list_document_versions_paginator: ListDocumentVersionsPaginator = client.get_paginator("list_document_versions")
    list_documents_paginator: ListDocumentsPaginator = client.get_paginator("list_documents")
    list_resource_compliance_summaries_paginator: ListResourceComplianceSummariesPaginator = client.get_paginator("list_resource_compliance_summaries")
    list_resource_data_sync_paginator: ListResourceDataSyncPaginator = client.get_paginator("list_resource_data_sync")
    ```
"""
import sys
from typing import Any, Dict, Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_ssm.type_defs import (
    AssociationExecutionFilterTypeDef,
    AssociationExecutionTargetsFilterTypeDef,
    AssociationFilterTypeDef,
    AutomationExecutionFilterTypeDef,
    CommandFilterTypeDef,
    ComplianceStringFilterTypeDef,
    DescribeActivationsFilterTypeDef,
    DescribeActivationsResultTypeDef,
    DescribeAssociationExecutionsResultTypeDef,
    DescribeAssociationExecutionTargetsResultTypeDef,
    DescribeAutomationExecutionsResultTypeDef,
    DescribeAutomationStepExecutionsResultTypeDef,
    DescribeAvailablePatchesResultTypeDef,
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
    DescribePatchPropertiesResultTypeDef,
    DescribeSessionsResponseTypeDef,
    DocumentFilterTypeDef,
    DocumentKeyValuesFilterTypeDef,
    GetInventoryResultTypeDef,
    GetInventorySchemaResultTypeDef,
    GetOpsSummaryResultTypeDef,
    GetParameterHistoryResultTypeDef,
    GetParametersByPathResultTypeDef,
    InstanceInformationFilterTypeDef,
    InstanceInformationStringFilterTypeDef,
    InstancePatchStateFilterTypeDef,
    InventoryFilterTypeDef,
    ListAssociationsResultTypeDef,
    ListAssociationVersionsResultTypeDef,
    ListCommandInvocationsResultTypeDef,
    ListCommandsResultTypeDef,
    ListComplianceItemsResultTypeDef,
    ListComplianceSummariesResultTypeDef,
    ListDocumentsResultTypeDef,
    ListDocumentVersionsResultTypeDef,
    ListResourceComplianceSummariesResultTypeDef,
    ListResourceDataSyncResultTypeDef,
    MaintenanceWindowFilterTypeDef,
    OpsFilterTypeDef,
    OpsItemFilterTypeDef,
    OpsResultAttributeTypeDef,
    PaginatorConfigTypeDef,
    ParametersFilterTypeDef,
    ParameterStringFilterTypeDef,
    PatchOrchestratorFilterTypeDef,
    ResultAttributeTypeDef,
    SessionFilterTypeDef,
    StepExecutionFilterTypeDef,
    TargetTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeActivationsPaginator",
    "DescribeAssociationExecutionTargetsPaginator",
    "DescribeAssociationExecutionsPaginator",
    "DescribeAutomationExecutionsPaginator",
    "DescribeAutomationStepExecutionsPaginator",
    "DescribeAvailablePatchesPaginator",
    "DescribeEffectiveInstanceAssociationsPaginator",
    "DescribeEffectivePatchesForPatchBaselinePaginator",
    "DescribeInstanceAssociationsStatusPaginator",
    "DescribeInstanceInformationPaginator",
    "DescribeInstancePatchStatesPaginator",
    "DescribeInstancePatchStatesForPatchGroupPaginator",
    "DescribeInstancePatchesPaginator",
    "DescribeInventoryDeletionsPaginator",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginator",
    "DescribeMaintenanceWindowExecutionTasksPaginator",
    "DescribeMaintenanceWindowExecutionsPaginator",
    "DescribeMaintenanceWindowSchedulePaginator",
    "DescribeMaintenanceWindowTargetsPaginator",
    "DescribeMaintenanceWindowTasksPaginator",
    "DescribeMaintenanceWindowsPaginator",
    "DescribeMaintenanceWindowsForTargetPaginator",
    "DescribeOpsItemsPaginator",
    "DescribeParametersPaginator",
    "DescribePatchBaselinesPaginator",
    "DescribePatchGroupsPaginator",
    "DescribePatchPropertiesPaginator",
    "DescribeSessionsPaginator",
    "GetInventoryPaginator",
    "GetInventorySchemaPaginator",
    "GetOpsSummaryPaginator",
    "GetParameterHistoryPaginator",
    "GetParametersByPathPaginator",
    "ListAssociationVersionsPaginator",
    "ListAssociationsPaginator",
    "ListCommandInvocationsPaginator",
    "ListCommandsPaginator",
    "ListComplianceItemsPaginator",
    "ListComplianceSummariesPaginator",
    "ListDocumentVersionsPaginator",
    "ListDocumentsPaginator",
    "ListResourceComplianceSummariesPaginator",
    "ListResourceDataSyncPaginator",
)


class DescribeActivationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeActivations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeActivations)
    """

    def paginate(
        self,
        Filters: List[DescribeActivationsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeActivationsResultTypeDef]:
        """
        [DescribeActivations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeActivations.paginate)
        """


class DescribeAssociationExecutionTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAssociationExecutionTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)
    """

    def paginate(
        self,
        AssociationId: str,
        ExecutionId: str,
        Filters: List[AssociationExecutionTargetsFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeAssociationExecutionTargetsResultTypeDef]:
        """
        [DescribeAssociationExecutionTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets.paginate)
        """


class DescribeAssociationExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAssociationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)
    """

    def paginate(
        self,
        AssociationId: str,
        Filters: List[AssociationExecutionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeAssociationExecutionsResultTypeDef]:
        """
        [DescribeAssociationExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions.paginate)
        """


class DescribeAutomationExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAutomationExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)
    """

    def paginate(
        self,
        Filters: List[AutomationExecutionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeAutomationExecutionsResultTypeDef]:
        """
        [DescribeAutomationExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions.paginate)
        """


class DescribeAutomationStepExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAutomationStepExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)
    """

    def paginate(
        self,
        AutomationExecutionId: str,
        Filters: List[StepExecutionFilterTypeDef] = None,
        ReverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeAutomationStepExecutionsResultTypeDef]:
        """
        [DescribeAutomationStepExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions.paginate)
        """


class DescribeAvailablePatchesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAvailablePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)
    """

    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeAvailablePatchesResultTypeDef]:
        """
        [DescribeAvailablePatches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches.paginate)
        """


class DescribeEffectiveInstanceAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEffectiveInstanceAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)
    """

    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEffectiveInstanceAssociationsResultTypeDef]:
        """
        [DescribeEffectiveInstanceAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations.paginate)
        """


class DescribeEffectivePatchesForPatchBaselinePaginator(Boto3Paginator):
    """
    [Paginator.DescribeEffectivePatchesForPatchBaseline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)
    """

    def paginate(
        self, BaselineId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEffectivePatchesForPatchBaselineResultTypeDef]:
        """
        [DescribeEffectivePatchesForPatchBaseline.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline.paginate)
        """


class DescribeInstanceAssociationsStatusPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceAssociationsStatus documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)
    """

    def paginate(
        self, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceAssociationsStatusResultTypeDef]:
        """
        [DescribeInstanceAssociationsStatus.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus.paginate)
        """


class DescribeInstanceInformationPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstanceInformation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)
    """

    def paginate(
        self,
        InstanceInformationFilterList: List[InstanceInformationFilterTypeDef] = None,
        Filters: List[InstanceInformationStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInstanceInformationResultTypeDef]:
        """
        [DescribeInstanceInformation.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation.paginate)
        """


class DescribeInstancePatchStatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstancePatchStates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)
    """

    def paginate(
        self, InstanceIds: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancePatchStatesResultTypeDef]:
        """
        [DescribeInstancePatchStates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates.paginate)
        """


class DescribeInstancePatchStatesForPatchGroupPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstancePatchStatesForPatchGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)
    """

    def paginate(
        self,
        PatchGroup: str,
        Filters: List[InstancePatchStateFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInstancePatchStatesForPatchGroupResultTypeDef]:
        """
        [DescribeInstancePatchStatesForPatchGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup.paginate)
        """


class DescribeInstancePatchesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInstancePatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)
    """

    def paginate(
        self,
        InstanceId: str,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeInstancePatchesResultTypeDef]:
        """
        [DescribeInstancePatches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches.paginate)
        """


class DescribeInventoryDeletionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeInventoryDeletions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)
    """

    def paginate(
        self, DeletionId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInventoryDeletionsResultTypeDef]:
        """
        [DescribeInventoryDeletions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions.paginate)
        """


class DescribeMaintenanceWindowExecutionTaskInvocationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowExecutionTaskInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)
    """

    def paginate(
        self,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef]:
        """
        [DescribeMaintenanceWindowExecutionTaskInvocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations.paginate)
        """


class DescribeMaintenanceWindowExecutionTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowExecutionTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)
    """

    def paginate(
        self,
        WindowExecutionId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMaintenanceWindowExecutionTasksResultTypeDef]:
        """
        [DescribeMaintenanceWindowExecutionTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks.paginate)
        """


class DescribeMaintenanceWindowExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)
    """

    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMaintenanceWindowExecutionsResultTypeDef]:
        """
        [DescribeMaintenanceWindowExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions.paginate)
        """


class DescribeMaintenanceWindowSchedulePaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowSchedule documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)
    """

    def paginate(
        self,
        WindowId: str = None,
        Targets: List["TargetTypeDef"] = None,
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"] = None,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMaintenanceWindowScheduleResultTypeDef]:
        """
        [DescribeMaintenanceWindowSchedule.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule.paginate)
        """


class DescribeMaintenanceWindowTargetsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowTargets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)
    """

    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMaintenanceWindowTargetsResultTypeDef]:
        """
        [DescribeMaintenanceWindowTargets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets.paginate)
        """


class DescribeMaintenanceWindowTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)
    """

    def paginate(
        self,
        WindowId: str,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMaintenanceWindowTasksResultTypeDef]:
        """
        [DescribeMaintenanceWindowTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks.paginate)
        """


class DescribeMaintenanceWindowsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)
    """

    def paginate(
        self,
        Filters: List[MaintenanceWindowFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMaintenanceWindowsResultTypeDef]:
        """
        [DescribeMaintenanceWindows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows.paginate)
        """


class DescribeMaintenanceWindowsForTargetPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMaintenanceWindowsForTarget documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)
    """

    def paginate(
        self,
        Targets: List["TargetTypeDef"],
        ResourceType: Literal["INSTANCE", "RESOURCE_GROUP"],
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeMaintenanceWindowsForTargetResultTypeDef]:
        """
        [DescribeMaintenanceWindowsForTarget.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget.paginate)
        """


class DescribeOpsItemsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOpsItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeOpsItems)
    """

    def paginate(
        self,
        OpsItemFilters: List[OpsItemFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeOpsItemsResponseTypeDef]:
        """
        [DescribeOpsItems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeOpsItems.paginate)
        """


class DescribeParametersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeParameters)
    """

    def paginate(
        self,
        Filters: List[ParametersFilterTypeDef] = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeParametersResultTypeDef]:
        """
        [DescribeParameters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeParameters.paginate)
        """


class DescribePatchBaselinesPaginator(Boto3Paginator):
    """
    [Paginator.DescribePatchBaselines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)
    """

    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribePatchBaselinesResultTypeDef]:
        """
        [DescribePatchBaselines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines.paginate)
        """


class DescribePatchGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribePatchGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)
    """

    def paginate(
        self,
        Filters: List[PatchOrchestratorFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribePatchGroupsResultTypeDef]:
        """
        [DescribePatchGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups.paginate)
        """


class DescribePatchPropertiesPaginator(Boto3Paginator):
    """
    [Paginator.DescribePatchProperties documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchProperties)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribePatchPropertiesResultTypeDef]:
        """
        [DescribePatchProperties.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribePatchProperties.paginate)
        """


class DescribeSessionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeSessions)
    """

    def paginate(
        self,
        State: Literal["Active", "History"],
        Filters: List[SessionFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeSessionsResponseTypeDef]:
        """
        [DescribeSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.DescribeSessions.paginate)
        """


class GetInventoryPaginator(Boto3Paginator):
    """
    [Paginator.GetInventory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetInventory)
    """

    def paginate(
        self,
        Filters: List["InventoryFilterTypeDef"] = None,
        Aggregators: List[Dict[str, Any]] = None,
        ResultAttributes: List[ResultAttributeTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetInventoryResultTypeDef]:
        """
        [GetInventory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetInventory.paginate)
        """


class GetInventorySchemaPaginator(Boto3Paginator):
    """
    [Paginator.GetInventorySchema documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)
    """

    def paginate(
        self,
        TypeName: str = None,
        Aggregator: bool = None,
        SubType: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetInventorySchemaResultTypeDef]:
        """
        [GetInventorySchema.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetInventorySchema.paginate)
        """


class GetOpsSummaryPaginator(Boto3Paginator):
    """
    [Paginator.GetOpsSummary documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetOpsSummary)
    """

    def paginate(
        self,
        SyncName: str = None,
        Filters: List["OpsFilterTypeDef"] = None,
        Aggregators: List[Dict[str, Any]] = None,
        ResultAttributes: List[OpsResultAttributeTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetOpsSummaryResultTypeDef]:
        """
        [GetOpsSummary.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetOpsSummary.paginate)
        """


class GetParameterHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetParameterHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)
    """

    def paginate(
        self,
        Name: str,
        WithDecryption: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetParameterHistoryResultTypeDef]:
        """
        [GetParameterHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetParameterHistory.paginate)
        """


class GetParametersByPathPaginator(Boto3Paginator):
    """
    [Paginator.GetParametersByPath documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)
    """

    def paginate(
        self,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List[ParameterStringFilterTypeDef] = None,
        WithDecryption: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetParametersByPathResultTypeDef]:
        """
        [GetParametersByPath.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.GetParametersByPath.paginate)
        """


class ListAssociationVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)
    """

    def paginate(
        self, AssociationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociationVersionsResultTypeDef]:
        """
        [ListAssociationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions.paginate)
        """


class ListAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListAssociations)
    """

    def paginate(
        self,
        AssociationFilterList: List[AssociationFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAssociationsResultTypeDef]:
        """
        [ListAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListAssociations.paginate)
        """


class ListCommandInvocationsPaginator(Boto3Paginator):
    """
    [Paginator.ListCommandInvocations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)
    """

    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[CommandFilterTypeDef] = None,
        Details: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCommandInvocationsResultTypeDef]:
        """
        [ListCommandInvocations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations.paginate)
        """


class ListCommandsPaginator(Boto3Paginator):
    """
    [Paginator.ListCommands documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListCommands)
    """

    def paginate(
        self,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List[CommandFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCommandsResultTypeDef]:
        """
        [ListCommands.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListCommands.paginate)
        """


class ListComplianceItemsPaginator(Boto3Paginator):
    """
    [Paginator.ListComplianceItems documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)
    """

    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListComplianceItemsResultTypeDef]:
        """
        [ListComplianceItems.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListComplianceItems.paginate)
        """


class ListComplianceSummariesPaginator(Boto3Paginator):
    """
    [Paginator.ListComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)
    """

    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListComplianceSummariesResultTypeDef]:
        """
        [ListComplianceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries.paginate)
        """


class ListDocumentVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDocumentVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)
    """

    def paginate(
        self, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentVersionsResultTypeDef]:
        """
        [ListDocumentVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions.paginate)
        """


class ListDocumentsPaginator(Boto3Paginator):
    """
    [Paginator.ListDocuments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListDocuments)
    """

    def paginate(
        self,
        DocumentFilterList: List[DocumentFilterTypeDef] = None,
        Filters: List[DocumentKeyValuesFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDocumentsResultTypeDef]:
        """
        [ListDocuments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListDocuments.paginate)
        """


class ListResourceComplianceSummariesPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceComplianceSummaries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)
    """

    def paginate(
        self,
        Filters: List[ComplianceStringFilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListResourceComplianceSummariesResultTypeDef]:
        """
        [ListResourceComplianceSummaries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries.paginate)
        """


class ListResourceDataSyncPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceDataSync documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)
    """

    def paginate(
        self, SyncType: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDataSyncResultTypeDef]:
        """
        [ListResourceDataSync.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync.paginate)
        """
