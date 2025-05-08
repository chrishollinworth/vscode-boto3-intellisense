"""
Main interface for ssm service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ssm import (
        Client,
        CommandExecutedWaiter,
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
        DescribeInstancePatchStatesForPatchGroupPaginator,
        DescribeInstancePatchStatesPaginator,
        DescribeInstancePatchesPaginator,
        DescribeInstancePropertiesPaginator,
        DescribeInventoryDeletionsPaginator,
        DescribeMaintenanceWindowExecutionTaskInvocationsPaginator,
        DescribeMaintenanceWindowExecutionTasksPaginator,
        DescribeMaintenanceWindowExecutionsPaginator,
        DescribeMaintenanceWindowSchedulePaginator,
        DescribeMaintenanceWindowTargetsPaginator,
        DescribeMaintenanceWindowTasksPaginator,
        DescribeMaintenanceWindowsForTargetPaginator,
        DescribeMaintenanceWindowsPaginator,
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
        ListAssociationVersionsPaginator,
        ListAssociationsPaginator,
        ListCommandInvocationsPaginator,
        ListCommandsPaginator,
        ListComplianceItemsPaginator,
        ListComplianceSummariesPaginator,
        ListDocumentVersionsPaginator,
        ListDocumentsPaginator,
        ListNodesPaginator,
        ListNodesSummaryPaginator,
        ListOpsItemEventsPaginator,
        ListOpsItemRelatedItemsPaginator,
        ListOpsMetadataPaginator,
        ListResourceComplianceSummariesPaginator,
        ListResourceDataSyncPaginator,
        SSMClient,
    )

    session = Session()
    client: SSMClient = session.client("ssm")

    command_executed_waiter: CommandExecutedWaiter = client.get_waiter("command_executed")

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
    describe_instance_patch_states_for_patch_group_paginator: DescribeInstancePatchStatesForPatchGroupPaginator = client.get_paginator("describe_instance_patch_states_for_patch_group")
    describe_instance_patch_states_paginator: DescribeInstancePatchStatesPaginator = client.get_paginator("describe_instance_patch_states")
    describe_instance_patches_paginator: DescribeInstancePatchesPaginator = client.get_paginator("describe_instance_patches")
    describe_instance_properties_paginator: DescribeInstancePropertiesPaginator = client.get_paginator("describe_instance_properties")
    describe_inventory_deletions_paginator: DescribeInventoryDeletionsPaginator = client.get_paginator("describe_inventory_deletions")
    describe_maintenance_window_execution_task_invocations_paginator: DescribeMaintenanceWindowExecutionTaskInvocationsPaginator = client.get_paginator("describe_maintenance_window_execution_task_invocations")
    describe_maintenance_window_execution_tasks_paginator: DescribeMaintenanceWindowExecutionTasksPaginator = client.get_paginator("describe_maintenance_window_execution_tasks")
    describe_maintenance_window_executions_paginator: DescribeMaintenanceWindowExecutionsPaginator = client.get_paginator("describe_maintenance_window_executions")
    describe_maintenance_window_schedule_paginator: DescribeMaintenanceWindowSchedulePaginator = client.get_paginator("describe_maintenance_window_schedule")
    describe_maintenance_window_targets_paginator: DescribeMaintenanceWindowTargetsPaginator = client.get_paginator("describe_maintenance_window_targets")
    describe_maintenance_window_tasks_paginator: DescribeMaintenanceWindowTasksPaginator = client.get_paginator("describe_maintenance_window_tasks")
    describe_maintenance_windows_for_target_paginator: DescribeMaintenanceWindowsForTargetPaginator = client.get_paginator("describe_maintenance_windows_for_target")
    describe_maintenance_windows_paginator: DescribeMaintenanceWindowsPaginator = client.get_paginator("describe_maintenance_windows")
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
    get_resource_policies_paginator: GetResourcePoliciesPaginator = client.get_paginator("get_resource_policies")
    list_association_versions_paginator: ListAssociationVersionsPaginator = client.get_paginator("list_association_versions")
    list_associations_paginator: ListAssociationsPaginator = client.get_paginator("list_associations")
    list_command_invocations_paginator: ListCommandInvocationsPaginator = client.get_paginator("list_command_invocations")
    list_commands_paginator: ListCommandsPaginator = client.get_paginator("list_commands")
    list_compliance_items_paginator: ListComplianceItemsPaginator = client.get_paginator("list_compliance_items")
    list_compliance_summaries_paginator: ListComplianceSummariesPaginator = client.get_paginator("list_compliance_summaries")
    list_document_versions_paginator: ListDocumentVersionsPaginator = client.get_paginator("list_document_versions")
    list_documents_paginator: ListDocumentsPaginator = client.get_paginator("list_documents")
    list_nodes_paginator: ListNodesPaginator = client.get_paginator("list_nodes")
    list_nodes_summary_paginator: ListNodesSummaryPaginator = client.get_paginator("list_nodes_summary")
    list_ops_item_events_paginator: ListOpsItemEventsPaginator = client.get_paginator("list_ops_item_events")
    list_ops_item_related_items_paginator: ListOpsItemRelatedItemsPaginator = client.get_paginator("list_ops_item_related_items")
    list_ops_metadata_paginator: ListOpsMetadataPaginator = client.get_paginator("list_ops_metadata")
    list_resource_compliance_summaries_paginator: ListResourceComplianceSummariesPaginator = client.get_paginator("list_resource_compliance_summaries")
    list_resource_data_sync_paginator: ListResourceDataSyncPaginator = client.get_paginator("list_resource_data_sync")
    ```
"""

from .client import SSMClient
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
from .waiter import CommandExecutedWaiter

Client = SSMClient

__all__ = (
    "Client",
    "CommandExecutedWaiter",
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
    "DescribeInstancePatchStatesForPatchGroupPaginator",
    "DescribeInstancePatchStatesPaginator",
    "DescribeInstancePatchesPaginator",
    "DescribeInstancePropertiesPaginator",
    "DescribeInventoryDeletionsPaginator",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginator",
    "DescribeMaintenanceWindowExecutionTasksPaginator",
    "DescribeMaintenanceWindowExecutionsPaginator",
    "DescribeMaintenanceWindowSchedulePaginator",
    "DescribeMaintenanceWindowTargetsPaginator",
    "DescribeMaintenanceWindowTasksPaginator",
    "DescribeMaintenanceWindowsForTargetPaginator",
    "DescribeMaintenanceWindowsPaginator",
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
    "GetResourcePoliciesPaginator",
    "ListAssociationVersionsPaginator",
    "ListAssociationsPaginator",
    "ListCommandInvocationsPaginator",
    "ListCommandsPaginator",
    "ListComplianceItemsPaginator",
    "ListComplianceSummariesPaginator",
    "ListDocumentVersionsPaginator",
    "ListDocumentsPaginator",
    "ListNodesPaginator",
    "ListNodesSummaryPaginator",
    "ListOpsItemEventsPaginator",
    "ListOpsItemRelatedItemsPaginator",
    "ListOpsMetadataPaginator",
    "ListResourceComplianceSummariesPaginator",
    "ListResourceDataSyncPaginator",
    "SSMClient",
)
