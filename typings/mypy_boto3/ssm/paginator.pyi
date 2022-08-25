"""
Type annotations for ssm service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html)

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
        ListOpsItemEventsPaginator,
        ListOpsItemRelatedItemsPaginator,
        ListOpsMetadataPaginator,
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
    list_ops_item_events_paginator: ListOpsItemEventsPaginator = client.get_paginator("list_ops_item_events")
    list_ops_item_related_items_paginator: ListOpsItemRelatedItemsPaginator = client.get_paginator("list_ops_item_related_items")
    list_ops_metadata_paginator: ListOpsMetadataPaginator = client.get_paginator("list_ops_metadata")
    list_resource_compliance_summaries_paginator: ListResourceComplianceSummariesPaginator = client.get_paginator("list_resource_compliance_summaries")
    list_resource_data_sync_paginator: ListResourceDataSyncPaginator = client.get_paginator("list_resource_data_sync")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    MaintenanceWindowResourceTypeType,
    OperatingSystemType,
    PatchPropertyType,
    PatchSetType,
    SessionStateType,
)
from .type_defs import (
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
    InventoryAggregatorTypeDef,
    InventoryFilterTypeDef,
    ListAssociationsResultTypeDef,
    ListAssociationVersionsResultTypeDef,
    ListCommandInvocationsResultTypeDef,
    ListCommandsResultTypeDef,
    ListComplianceItemsResultTypeDef,
    ListComplianceSummariesResultTypeDef,
    ListDocumentsResultTypeDef,
    ListDocumentVersionsResultTypeDef,
    ListOpsItemEventsResponseTypeDef,
    ListOpsItemRelatedItemsResponseTypeDef,
    ListOpsMetadataResultTypeDef,
    ListResourceComplianceSummariesResultTypeDef,
    ListResourceDataSyncResultTypeDef,
    MaintenanceWindowFilterTypeDef,
    OpsAggregatorTypeDef,
    OpsFilterTypeDef,
    OpsItemEventFilterTypeDef,
    OpsItemFilterTypeDef,
    OpsItemRelatedItemsFilterTypeDef,
    OpsMetadataFilterTypeDef,
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
    "ListOpsItemEventsPaginator",
    "ListOpsItemRelatedItemsPaginator",
    "ListOpsMetadataPaginator",
    "ListResourceComplianceSummariesPaginator",
    "ListResourceDataSyncPaginator",
)

class DescribeActivationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeActivations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeactivationspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["DescribeActivationsFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeActivationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeActivations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeactivationspaginator)
        """

class DescribeAssociationExecutionTargetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeassociationexecutiontargetspaginator)
    """

    def paginate(
        self,
        *,
        AssociationId: str,
        ExecutionId: str,
        Filters: List["AssociationExecutionTargetsFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAssociationExecutionTargetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutionTargets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeassociationexecutiontargetspaginator)
        """

class DescribeAssociationExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeassociationexecutionspaginator)
    """

    def paginate(
        self,
        *,
        AssociationId: str,
        Filters: List["AssociationExecutionFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAssociationExecutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAssociationExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeassociationexecutionspaginator)
        """

class DescribeAutomationExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeautomationexecutionspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["AutomationExecutionFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAutomationExecutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAutomationExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeautomationexecutionspaginator)
        """

class DescribeAutomationStepExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeautomationstepexecutionspaginator)
    """

    def paginate(
        self,
        *,
        AutomationExecutionId: str,
        Filters: List["StepExecutionFilterTypeDef"] = None,
        ReverseOrder: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAutomationStepExecutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAutomationStepExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeautomationstepexecutionspaginator)
        """

class DescribeAvailablePatchesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeavailablepatchespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAvailablePatchesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeAvailablePatches.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeavailablepatchespaginator)
        """

class DescribeEffectiveInstanceAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeeffectiveinstanceassociationspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEffectiveInstanceAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeEffectiveInstanceAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeeffectiveinstanceassociationspaginator)
        """

class DescribeEffectivePatchesForPatchBaselinePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeeffectivepatchesforpatchbaselinepaginator)
    """

    def paginate(
        self, *, BaselineId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEffectivePatchesForPatchBaselineResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeeffectivepatchesforpatchbaselinepaginator)
        """

class DescribeInstanceAssociationsStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstanceassociationsstatuspaginator)
    """

    def paginate(
        self, *, InstanceId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceAssociationsStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstanceAssociationsStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstanceassociationsstatuspaginator)
        """

class DescribeInstanceInformationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstanceinformationpaginator)
    """

    def paginate(
        self,
        *,
        InstanceInformationFilterList: List["InstanceInformationFilterTypeDef"] = None,
        Filters: List["InstanceInformationStringFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceInformationResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstanceInformation.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstanceinformationpaginator)
        """

class DescribeInstancePatchStatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchstatespaginator)
    """

    def paginate(
        self, *, InstanceIds: List[str], PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancePatchStatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchstatespaginator)
        """

class DescribeInstancePatchStatesForPatchGroupPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchstatesforpatchgrouppaginator)
    """

    def paginate(
        self,
        *,
        PatchGroup: str,
        Filters: List["InstancePatchStateFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancePatchStatesForPatchGroupResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchstatesforpatchgrouppaginator)
        """

class DescribeInstancePatchesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchespaginator)
    """

    def paginate(
        self,
        *,
        InstanceId: str,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancePatchesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInstancePatches.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinstancepatchespaginator)
        """

class DescribeInventoryDeletionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinventorydeletionspaginator)
    """

    def paginate(
        self, *, DeletionId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInventoryDeletionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeInventoryDeletions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeinventorydeletionspaginator)
        """

class DescribeMaintenanceWindowExecutionTaskInvocationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutiontaskinvocationspaginator)
    """

    def paginate(
        self,
        *,
        WindowExecutionId: str,
        TaskId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutiontaskinvocationspaginator)
        """

class DescribeMaintenanceWindowExecutionTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutiontaskspaginator)
    """

    def paginate(
        self,
        *,
        WindowExecutionId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowExecutionTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutiontaskspaginator)
        """

class DescribeMaintenanceWindowExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutionspaginator)
    """

    def paginate(
        self,
        *,
        WindowId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowExecutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowexecutionspaginator)
        """

class DescribeMaintenanceWindowSchedulePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowschedulepaginator)
    """

    def paginate(
        self,
        *,
        WindowId: str = None,
        Targets: List["TargetTypeDef"] = None,
        ResourceType: MaintenanceWindowResourceTypeType = None,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowScheduleResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowSchedule.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowschedulepaginator)
        """

class DescribeMaintenanceWindowTargetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowtargetspaginator)
    """

    def paginate(
        self,
        *,
        WindowId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowTargetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTargets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowtargetspaginator)
        """

class DescribeMaintenanceWindowTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowtaskspaginator)
    """

    def paginate(
        self,
        *,
        WindowId: str,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowtaskspaginator)
        """

class DescribeMaintenanceWindowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["MaintenanceWindowFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowspaginator)
        """

class DescribeMaintenanceWindowsForTargetPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowsfortargetpaginator)
    """

    def paginate(
        self,
        *,
        Targets: List["TargetTypeDef"],
        ResourceType: MaintenanceWindowResourceTypeType,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMaintenanceWindowsForTargetResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describemaintenancewindowsfortargetpaginator)
        """

class DescribeOpsItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeOpsItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeopsitemspaginator)
    """

    def paginate(
        self,
        *,
        OpsItemFilters: List["OpsItemFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeOpsItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeOpsItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeopsitemspaginator)
        """

class DescribeParametersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeParameters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeparameterspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["ParametersFilterTypeDef"] = None,
        ParameterFilters: List["ParameterStringFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeParameters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describeparameterspaginator)
        """

class DescribePatchBaselinesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchbaselinespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePatchBaselinesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchBaselines.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchbaselinespaginator)
        """

class DescribePatchGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchgroupspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["PatchOrchestratorFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePatchGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchgroupspaginator)
        """

class DescribePatchPropertiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchProperties)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchpropertiespaginator)
    """

    def paginate(
        self,
        *,
        OperatingSystem: OperatingSystemType,
        Property: PatchPropertyType,
        PatchSet: PatchSetType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePatchPropertiesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribePatchProperties.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describepatchpropertiespaginator)
        """

class DescribeSessionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeSessions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describesessionspaginator)
    """

    def paginate(
        self,
        *,
        State: SessionStateType,
        Filters: List["SessionFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.DescribeSessions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#describesessionspaginator)
        """

class GetInventoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetInventory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getinventorypaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["InventoryFilterTypeDef"] = None,
        Aggregators: List["InventoryAggregatorTypeDef"] = None,
        ResultAttributes: List["ResultAttributeTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInventoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetInventory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getinventorypaginator)
        """

class GetInventorySchemaPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetInventorySchema)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getinventoryschemapaginator)
    """

    def paginate(
        self,
        *,
        TypeName: str = None,
        Aggregator: bool = None,
        SubType: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInventorySchemaResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetInventorySchema.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getinventoryschemapaginator)
        """

class GetOpsSummaryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetOpsSummary)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getopssummarypaginator)
    """

    def paginate(
        self,
        *,
        SyncName: str = None,
        Filters: List["OpsFilterTypeDef"] = None,
        Aggregators: List["OpsAggregatorTypeDef"] = None,
        ResultAttributes: List["OpsResultAttributeTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetOpsSummaryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetOpsSummary.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getopssummarypaginator)
        """

class GetParameterHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetParameterHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getparameterhistorypaginator)
    """

    def paginate(
        self,
        *,
        Name: str,
        WithDecryption: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetParameterHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetParameterHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getparameterhistorypaginator)
        """

class GetParametersByPathPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetParametersByPath)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getparametersbypathpaginator)
    """

    def paginate(
        self,
        *,
        Path: str,
        Recursive: bool = None,
        ParameterFilters: List["ParameterStringFilterTypeDef"] = None,
        WithDecryption: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetParametersByPathResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.GetParametersByPath.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#getparametersbypathpaginator)
        """

class ListAssociationVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listassociationversionspaginator)
    """

    def paginate(
        self, *, AssociationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociationVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListAssociationVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listassociationversionspaginator)
        """

class ListAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listassociationspaginator)
    """

    def paginate(
        self,
        *,
        AssociationFilterList: List["AssociationFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listassociationspaginator)
        """

class ListCommandInvocationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcommandinvocationspaginator)
    """

    def paginate(
        self,
        *,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List["CommandFilterTypeDef"] = None,
        Details: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCommandInvocationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListCommandInvocations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcommandinvocationspaginator)
        """

class ListCommandsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListCommands)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcommandspaginator)
    """

    def paginate(
        self,
        *,
        CommandId: str = None,
        InstanceId: str = None,
        Filters: List["CommandFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListCommandsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListCommands.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcommandspaginator)
        """

class ListComplianceItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListComplianceItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcomplianceitemspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["ComplianceStringFilterTypeDef"] = None,
        ResourceIds: List[str] = None,
        ResourceTypes: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComplianceItemsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListComplianceItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcomplianceitemspaginator)
        """

class ListComplianceSummariesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcompliancesummariespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["ComplianceStringFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListComplianceSummariesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListComplianceSummaries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listcompliancesummariespaginator)
        """

class ListDocumentVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listdocumentversionspaginator)
    """

    def paginate(
        self, *, Name: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListDocumentVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listdocumentversionspaginator)
        """

class ListDocumentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListDocuments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listdocumentspaginator)
    """

    def paginate(
        self,
        *,
        DocumentFilterList: List["DocumentFilterTypeDef"] = None,
        Filters: List["DocumentKeyValuesFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDocumentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListDocuments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listdocumentspaginator)
        """

class ListOpsItemEventsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsItemEvents)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsitemeventspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["OpsItemEventFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOpsItemEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsItemEvents.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsitemeventspaginator)
        """

class ListOpsItemRelatedItemsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsItemRelatedItems)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsitemrelateditemspaginator)
    """

    def paginate(
        self,
        *,
        OpsItemId: str = None,
        Filters: List["OpsItemRelatedItemsFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOpsItemRelatedItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsItemRelatedItems.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsitemrelateditemspaginator)
        """

class ListOpsMetadataPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsMetadata)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsmetadatapaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["OpsMetadataFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListOpsMetadataResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListOpsMetadata.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listopsmetadatapaginator)
        """

class ListResourceComplianceSummariesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listresourcecompliancesummariespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["ComplianceStringFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceComplianceSummariesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListResourceComplianceSummaries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listresourcecompliancesummariespaginator)
        """

class ListResourceDataSyncPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listresourcedatasyncpaginator)
    """

    def paginate(
        self, *, SyncType: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListResourceDataSyncResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.58/reference/services/ssm.html#SSM.Paginator.ListResourceDataSync.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators.html#listresourcedatasyncpaginator)
        """
