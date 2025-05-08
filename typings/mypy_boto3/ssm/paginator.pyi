"""
Type annotations for ssm service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ssm.client import SSMClient
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
    )

    session = Session()
    client: SSMClient = session.client("ssm")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeActivationsRequestPaginateTypeDef,
    DescribeActivationsResultTypeDef,
    DescribeAssociationExecutionsRequestPaginateTypeDef,
    DescribeAssociationExecutionsResultTypeDef,
    DescribeAssociationExecutionTargetsRequestPaginateTypeDef,
    DescribeAssociationExecutionTargetsResultTypeDef,
    DescribeAutomationExecutionsRequestPaginateTypeDef,
    DescribeAutomationExecutionsResultTypeDef,
    DescribeAutomationStepExecutionsRequestPaginateTypeDef,
    DescribeAutomationStepExecutionsResultTypeDef,
    DescribeAvailablePatchesRequestPaginateTypeDef,
    DescribeAvailablePatchesResultTypeDef,
    DescribeEffectiveInstanceAssociationsRequestPaginateTypeDef,
    DescribeEffectiveInstanceAssociationsResultTypeDef,
    DescribeEffectivePatchesForPatchBaselineRequestPaginateTypeDef,
    DescribeEffectivePatchesForPatchBaselineResultTypeDef,
    DescribeInstanceAssociationsStatusRequestPaginateTypeDef,
    DescribeInstanceAssociationsStatusResultTypeDef,
    DescribeInstanceInformationRequestPaginateTypeDef,
    DescribeInstanceInformationResultTypeDef,
    DescribeInstancePatchesRequestPaginateTypeDef,
    DescribeInstancePatchesResultTypeDef,
    DescribeInstancePatchStatesForPatchGroupRequestPaginateTypeDef,
    DescribeInstancePatchStatesForPatchGroupResultTypeDef,
    DescribeInstancePatchStatesRequestPaginateTypeDef,
    DescribeInstancePatchStatesResultTypeDef,
    DescribeInstancePropertiesRequestPaginateTypeDef,
    DescribeInstancePropertiesResultTypeDef,
    DescribeInventoryDeletionsRequestPaginateTypeDef,
    DescribeInventoryDeletionsResultTypeDef,
    DescribeMaintenanceWindowExecutionsRequestPaginateTypeDef,
    DescribeMaintenanceWindowExecutionsResultTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginateTypeDef,
    DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef,
    DescribeMaintenanceWindowExecutionTasksRequestPaginateTypeDef,
    DescribeMaintenanceWindowExecutionTasksResultTypeDef,
    DescribeMaintenanceWindowScheduleRequestPaginateTypeDef,
    DescribeMaintenanceWindowScheduleResultTypeDef,
    DescribeMaintenanceWindowsForTargetRequestPaginateTypeDef,
    DescribeMaintenanceWindowsForTargetResultTypeDef,
    DescribeMaintenanceWindowsRequestPaginateTypeDef,
    DescribeMaintenanceWindowsResultTypeDef,
    DescribeMaintenanceWindowTargetsRequestPaginateTypeDef,
    DescribeMaintenanceWindowTargetsResultTypeDef,
    DescribeMaintenanceWindowTasksRequestPaginateTypeDef,
    DescribeMaintenanceWindowTasksResultTypeDef,
    DescribeOpsItemsRequestPaginateTypeDef,
    DescribeOpsItemsResponseTypeDef,
    DescribeParametersRequestPaginateTypeDef,
    DescribeParametersResultTypeDef,
    DescribePatchBaselinesRequestPaginateTypeDef,
    DescribePatchBaselinesResultTypeDef,
    DescribePatchGroupsRequestPaginateTypeDef,
    DescribePatchGroupsResultTypeDef,
    DescribePatchPropertiesRequestPaginateTypeDef,
    DescribePatchPropertiesResultTypeDef,
    DescribeSessionsRequestPaginateTypeDef,
    DescribeSessionsResponseTypeDef,
    GetInventoryRequestPaginateTypeDef,
    GetInventoryResultTypeDef,
    GetInventorySchemaRequestPaginateTypeDef,
    GetInventorySchemaResultTypeDef,
    GetOpsSummaryRequestPaginateTypeDef,
    GetOpsSummaryResultTypeDef,
    GetParameterHistoryRequestPaginateTypeDef,
    GetParameterHistoryResultTypeDef,
    GetParametersByPathRequestPaginateTypeDef,
    GetParametersByPathResultTypeDef,
    GetResourcePoliciesRequestPaginateTypeDef,
    GetResourcePoliciesResponseTypeDef,
    ListAssociationsRequestPaginateTypeDef,
    ListAssociationsResultTypeDef,
    ListAssociationVersionsRequestPaginateTypeDef,
    ListAssociationVersionsResultTypeDef,
    ListCommandInvocationsRequestPaginateTypeDef,
    ListCommandInvocationsResultTypeDef,
    ListCommandsRequestPaginateTypeDef,
    ListCommandsResultTypeDef,
    ListComplianceItemsRequestPaginateTypeDef,
    ListComplianceItemsResultTypeDef,
    ListComplianceSummariesRequestPaginateTypeDef,
    ListComplianceSummariesResultTypeDef,
    ListDocumentsRequestPaginateTypeDef,
    ListDocumentsResultTypeDef,
    ListDocumentVersionsRequestPaginateTypeDef,
    ListDocumentVersionsResultTypeDef,
    ListNodesRequestPaginateTypeDef,
    ListNodesResultTypeDef,
    ListNodesSummaryRequestPaginateTypeDef,
    ListNodesSummaryResultTypeDef,
    ListOpsItemEventsRequestPaginateTypeDef,
    ListOpsItemEventsResponseTypeDef,
    ListOpsItemRelatedItemsRequestPaginateTypeDef,
    ListOpsItemRelatedItemsResponseTypeDef,
    ListOpsMetadataRequestPaginateTypeDef,
    ListOpsMetadataResultTypeDef,
    ListResourceComplianceSummariesRequestPaginateTypeDef,
    ListResourceComplianceSummariesResultTypeDef,
    ListResourceDataSyncRequestPaginateTypeDef,
    ListResourceDataSyncResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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
)

if TYPE_CHECKING:
    _DescribeActivationsPaginatorBase = Paginator[DescribeActivationsResultTypeDef]
else:
    _DescribeActivationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeActivationsPaginator(_DescribeActivationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeActivations.html#SSM.Paginator.DescribeActivations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeactivationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeActivationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeActivationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeActivations.html#SSM.Paginator.DescribeActivations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeactivationspaginator)
        """

if TYPE_CHECKING:
    _DescribeAssociationExecutionTargetsPaginatorBase = Paginator[
        DescribeAssociationExecutionTargetsResultTypeDef
    ]
else:
    _DescribeAssociationExecutionTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAssociationExecutionTargetsPaginator(
    _DescribeAssociationExecutionTargetsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAssociationExecutionTargets.html#SSM.Paginator.DescribeAssociationExecutionTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeassociationexecutiontargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAssociationExecutionTargetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAssociationExecutionTargetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAssociationExecutionTargets.html#SSM.Paginator.DescribeAssociationExecutionTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeassociationexecutiontargetspaginator)
        """

if TYPE_CHECKING:
    _DescribeAssociationExecutionsPaginatorBase = Paginator[
        DescribeAssociationExecutionsResultTypeDef
    ]
else:
    _DescribeAssociationExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAssociationExecutionsPaginator(_DescribeAssociationExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAssociationExecutions.html#SSM.Paginator.DescribeAssociationExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeassociationexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAssociationExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAssociationExecutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAssociationExecutions.html#SSM.Paginator.DescribeAssociationExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeassociationexecutionspaginator)
        """

if TYPE_CHECKING:
    _DescribeAutomationExecutionsPaginatorBase = Paginator[
        DescribeAutomationExecutionsResultTypeDef
    ]
else:
    _DescribeAutomationExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAutomationExecutionsPaginator(_DescribeAutomationExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAutomationExecutions.html#SSM.Paginator.DescribeAutomationExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeautomationexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAutomationExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAutomationExecutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAutomationExecutions.html#SSM.Paginator.DescribeAutomationExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeautomationexecutionspaginator)
        """

if TYPE_CHECKING:
    _DescribeAutomationStepExecutionsPaginatorBase = Paginator[
        DescribeAutomationStepExecutionsResultTypeDef
    ]
else:
    _DescribeAutomationStepExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAutomationStepExecutionsPaginator(_DescribeAutomationStepExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAutomationStepExecutions.html#SSM.Paginator.DescribeAutomationStepExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeautomationstepexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAutomationStepExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAutomationStepExecutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAutomationStepExecutions.html#SSM.Paginator.DescribeAutomationStepExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeautomationstepexecutionspaginator)
        """

if TYPE_CHECKING:
    _DescribeAvailablePatchesPaginatorBase = Paginator[DescribeAvailablePatchesResultTypeDef]
else:
    _DescribeAvailablePatchesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAvailablePatchesPaginator(_DescribeAvailablePatchesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAvailablePatches.html#SSM.Paginator.DescribeAvailablePatches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeavailablepatchespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAvailablePatchesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAvailablePatchesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeAvailablePatches.html#SSM.Paginator.DescribeAvailablePatches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeavailablepatchespaginator)
        """

if TYPE_CHECKING:
    _DescribeEffectiveInstanceAssociationsPaginatorBase = Paginator[
        DescribeEffectiveInstanceAssociationsResultTypeDef
    ]
else:
    _DescribeEffectiveInstanceAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEffectiveInstanceAssociationsPaginator(
    _DescribeEffectiveInstanceAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeEffectiveInstanceAssociations.html#SSM.Paginator.DescribeEffectiveInstanceAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeeffectiveinstanceassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEffectiveInstanceAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEffectiveInstanceAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeEffectiveInstanceAssociations.html#SSM.Paginator.DescribeEffectiveInstanceAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeeffectiveinstanceassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeEffectivePatchesForPatchBaselinePaginatorBase = Paginator[
        DescribeEffectivePatchesForPatchBaselineResultTypeDef
    ]
else:
    _DescribeEffectivePatchesForPatchBaselinePaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEffectivePatchesForPatchBaselinePaginator(
    _DescribeEffectivePatchesForPatchBaselinePaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeEffectivePatchesForPatchBaseline.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeeffectivepatchesforpatchbaselinepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEffectivePatchesForPatchBaselineRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEffectivePatchesForPatchBaselineResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeEffectivePatchesForPatchBaseline.html#SSM.Paginator.DescribeEffectivePatchesForPatchBaseline.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeeffectivepatchesforpatchbaselinepaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceAssociationsStatusPaginatorBase = Paginator[
        DescribeInstanceAssociationsStatusResultTypeDef
    ]
else:
    _DescribeInstanceAssociationsStatusPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceAssociationsStatusPaginator(_DescribeInstanceAssociationsStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstanceAssociationsStatus.html#SSM.Paginator.DescribeInstanceAssociationsStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstanceassociationsstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceAssociationsStatusRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceAssociationsStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstanceAssociationsStatus.html#SSM.Paginator.DescribeInstanceAssociationsStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstanceassociationsstatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceInformationPaginatorBase = Paginator[DescribeInstanceInformationResultTypeDef]
else:
    _DescribeInstanceInformationPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceInformationPaginator(_DescribeInstanceInformationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstanceInformation.html#SSM.Paginator.DescribeInstanceInformation)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstanceinformationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceInformationRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceInformationResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstanceInformation.html#SSM.Paginator.DescribeInstanceInformation.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstanceinformationpaginator)
        """

if TYPE_CHECKING:
    _DescribeInstancePatchStatesForPatchGroupPaginatorBase = Paginator[
        DescribeInstancePatchStatesForPatchGroupResultTypeDef
    ]
else:
    _DescribeInstancePatchStatesForPatchGroupPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstancePatchStatesForPatchGroupPaginator(
    _DescribeInstancePatchStatesForPatchGroupPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstancePatchStatesForPatchGroup.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstancepatchstatesforpatchgrouppaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancePatchStatesForPatchGroupRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstancePatchStatesForPatchGroupResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstancePatchStatesForPatchGroup.html#SSM.Paginator.DescribeInstancePatchStatesForPatchGroup.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstancepatchstatesforpatchgrouppaginator)
        """

if TYPE_CHECKING:
    _DescribeInstancePatchStatesPaginatorBase = Paginator[DescribeInstancePatchStatesResultTypeDef]
else:
    _DescribeInstancePatchStatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstancePatchStatesPaginator(_DescribeInstancePatchStatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstancePatchStates.html#SSM.Paginator.DescribeInstancePatchStates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstancepatchstatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancePatchStatesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstancePatchStatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstancePatchStates.html#SSM.Paginator.DescribeInstancePatchStates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstancepatchstatespaginator)
        """

if TYPE_CHECKING:
    _DescribeInstancePatchesPaginatorBase = Paginator[DescribeInstancePatchesResultTypeDef]
else:
    _DescribeInstancePatchesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstancePatchesPaginator(_DescribeInstancePatchesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstancePatches.html#SSM.Paginator.DescribeInstancePatches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstancepatchespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancePatchesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstancePatchesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstancePatches.html#SSM.Paginator.DescribeInstancePatches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstancepatchespaginator)
        """

if TYPE_CHECKING:
    _DescribeInstancePropertiesPaginatorBase = Paginator[DescribeInstancePropertiesResultTypeDef]
else:
    _DescribeInstancePropertiesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstancePropertiesPaginator(_DescribeInstancePropertiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstanceProperties.html#SSM.Paginator.DescribeInstanceProperties)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstancepropertiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancePropertiesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstancePropertiesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInstanceProperties.html#SSM.Paginator.DescribeInstanceProperties.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinstancepropertiespaginator)
        """

if TYPE_CHECKING:
    _DescribeInventoryDeletionsPaginatorBase = Paginator[DescribeInventoryDeletionsResultTypeDef]
else:
    _DescribeInventoryDeletionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInventoryDeletionsPaginator(_DescribeInventoryDeletionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInventoryDeletions.html#SSM.Paginator.DescribeInventoryDeletions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinventorydeletionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInventoryDeletionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInventoryDeletionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeInventoryDeletions.html#SSM.Paginator.DescribeInventoryDeletions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeinventorydeletionspaginator)
        """

if TYPE_CHECKING:
    _DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorBase = Paginator[
        DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef
    ]
else:
    _DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMaintenanceWindowExecutionTaskInvocationsPaginator(
    _DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowExecutionTaskInvocations.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowexecutiontaskinvocationspaginator)
    """
    def paginate(  # type: ignore[override]
        self,
        **kwargs: Unpack[DescribeMaintenanceWindowExecutionTaskInvocationsRequestPaginateTypeDef],
    ) -> PageIterator[DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowExecutionTaskInvocations.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTaskInvocations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowexecutiontaskinvocationspaginator)
        """

if TYPE_CHECKING:
    _DescribeMaintenanceWindowExecutionTasksPaginatorBase = Paginator[
        DescribeMaintenanceWindowExecutionTasksResultTypeDef
    ]
else:
    _DescribeMaintenanceWindowExecutionTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMaintenanceWindowExecutionTasksPaginator(
    _DescribeMaintenanceWindowExecutionTasksPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowExecutionTasks.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowexecutiontaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMaintenanceWindowExecutionTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMaintenanceWindowExecutionTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowExecutionTasks.html#SSM.Paginator.DescribeMaintenanceWindowExecutionTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowexecutiontaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeMaintenanceWindowExecutionsPaginatorBase = Paginator[
        DescribeMaintenanceWindowExecutionsResultTypeDef
    ]
else:
    _DescribeMaintenanceWindowExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMaintenanceWindowExecutionsPaginator(
    _DescribeMaintenanceWindowExecutionsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowExecutions.html#SSM.Paginator.DescribeMaintenanceWindowExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMaintenanceWindowExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMaintenanceWindowExecutionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowExecutions.html#SSM.Paginator.DescribeMaintenanceWindowExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowexecutionspaginator)
        """

if TYPE_CHECKING:
    _DescribeMaintenanceWindowSchedulePaginatorBase = Paginator[
        DescribeMaintenanceWindowScheduleResultTypeDef
    ]
else:
    _DescribeMaintenanceWindowSchedulePaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMaintenanceWindowSchedulePaginator(_DescribeMaintenanceWindowSchedulePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowSchedule.html#SSM.Paginator.DescribeMaintenanceWindowSchedule)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowschedulepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMaintenanceWindowScheduleRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMaintenanceWindowScheduleResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowSchedule.html#SSM.Paginator.DescribeMaintenanceWindowSchedule.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowschedulepaginator)
        """

if TYPE_CHECKING:
    _DescribeMaintenanceWindowTargetsPaginatorBase = Paginator[
        DescribeMaintenanceWindowTargetsResultTypeDef
    ]
else:
    _DescribeMaintenanceWindowTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMaintenanceWindowTargetsPaginator(_DescribeMaintenanceWindowTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowTargets.html#SSM.Paginator.DescribeMaintenanceWindowTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowtargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMaintenanceWindowTargetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMaintenanceWindowTargetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowTargets.html#SSM.Paginator.DescribeMaintenanceWindowTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowtargetspaginator)
        """

if TYPE_CHECKING:
    _DescribeMaintenanceWindowTasksPaginatorBase = Paginator[
        DescribeMaintenanceWindowTasksResultTypeDef
    ]
else:
    _DescribeMaintenanceWindowTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMaintenanceWindowTasksPaginator(_DescribeMaintenanceWindowTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowTasks.html#SSM.Paginator.DescribeMaintenanceWindowTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowtaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMaintenanceWindowTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMaintenanceWindowTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowTasks.html#SSM.Paginator.DescribeMaintenanceWindowTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowtaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeMaintenanceWindowsForTargetPaginatorBase = Paginator[
        DescribeMaintenanceWindowsForTargetResultTypeDef
    ]
else:
    _DescribeMaintenanceWindowsForTargetPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMaintenanceWindowsForTargetPaginator(
    _DescribeMaintenanceWindowsForTargetPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowsForTarget.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowsfortargetpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMaintenanceWindowsForTargetRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMaintenanceWindowsForTargetResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindowsForTarget.html#SSM.Paginator.DescribeMaintenanceWindowsForTarget.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowsfortargetpaginator)
        """

if TYPE_CHECKING:
    _DescribeMaintenanceWindowsPaginatorBase = Paginator[DescribeMaintenanceWindowsResultTypeDef]
else:
    _DescribeMaintenanceWindowsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMaintenanceWindowsPaginator(_DescribeMaintenanceWindowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindows.html#SSM.Paginator.DescribeMaintenanceWindows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMaintenanceWindowsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMaintenanceWindowsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeMaintenanceWindows.html#SSM.Paginator.DescribeMaintenanceWindows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describemaintenancewindowspaginator)
        """

if TYPE_CHECKING:
    _DescribeOpsItemsPaginatorBase = Paginator[DescribeOpsItemsResponseTypeDef]
else:
    _DescribeOpsItemsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeOpsItemsPaginator(_DescribeOpsItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeOpsItems.html#SSM.Paginator.DescribeOpsItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeopsitemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeOpsItemsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeOpsItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeOpsItems.html#SSM.Paginator.DescribeOpsItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeopsitemspaginator)
        """

if TYPE_CHECKING:
    _DescribeParametersPaginatorBase = Paginator[DescribeParametersResultTypeDef]
else:
    _DescribeParametersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeParametersPaginator(_DescribeParametersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeParameters.html#SSM.Paginator.DescribeParameters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeparameterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeParametersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeParametersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeParameters.html#SSM.Paginator.DescribeParameters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describeparameterspaginator)
        """

if TYPE_CHECKING:
    _DescribePatchBaselinesPaginatorBase = Paginator[DescribePatchBaselinesResultTypeDef]
else:
    _DescribePatchBaselinesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePatchBaselinesPaginator(_DescribePatchBaselinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribePatchBaselines.html#SSM.Paginator.DescribePatchBaselines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describepatchbaselinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePatchBaselinesRequestPaginateTypeDef]
    ) -> PageIterator[DescribePatchBaselinesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribePatchBaselines.html#SSM.Paginator.DescribePatchBaselines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describepatchbaselinespaginator)
        """

if TYPE_CHECKING:
    _DescribePatchGroupsPaginatorBase = Paginator[DescribePatchGroupsResultTypeDef]
else:
    _DescribePatchGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePatchGroupsPaginator(_DescribePatchGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribePatchGroups.html#SSM.Paginator.DescribePatchGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describepatchgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePatchGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribePatchGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribePatchGroups.html#SSM.Paginator.DescribePatchGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describepatchgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribePatchPropertiesPaginatorBase = Paginator[DescribePatchPropertiesResultTypeDef]
else:
    _DescribePatchPropertiesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePatchPropertiesPaginator(_DescribePatchPropertiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribePatchProperties.html#SSM.Paginator.DescribePatchProperties)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describepatchpropertiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePatchPropertiesRequestPaginateTypeDef]
    ) -> PageIterator[DescribePatchPropertiesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribePatchProperties.html#SSM.Paginator.DescribePatchProperties.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describepatchpropertiespaginator)
        """

if TYPE_CHECKING:
    _DescribeSessionsPaginatorBase = Paginator[DescribeSessionsResponseTypeDef]
else:
    _DescribeSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSessionsPaginator(_DescribeSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeSessions.html#SSM.Paginator.DescribeSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describesessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSessionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSessionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/DescribeSessions.html#SSM.Paginator.DescribeSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#describesessionspaginator)
        """

if TYPE_CHECKING:
    _GetInventoryPaginatorBase = Paginator[GetInventoryResultTypeDef]
else:
    _GetInventoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetInventoryPaginator(_GetInventoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetInventory.html#SSM.Paginator.GetInventory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getinventorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetInventoryRequestPaginateTypeDef]
    ) -> PageIterator[GetInventoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetInventory.html#SSM.Paginator.GetInventory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getinventorypaginator)
        """

if TYPE_CHECKING:
    _GetInventorySchemaPaginatorBase = Paginator[GetInventorySchemaResultTypeDef]
else:
    _GetInventorySchemaPaginatorBase = Paginator  # type: ignore[assignment]

class GetInventorySchemaPaginator(_GetInventorySchemaPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetInventorySchema.html#SSM.Paginator.GetInventorySchema)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getinventoryschemapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetInventorySchemaRequestPaginateTypeDef]
    ) -> PageIterator[GetInventorySchemaResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetInventorySchema.html#SSM.Paginator.GetInventorySchema.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getinventoryschemapaginator)
        """

if TYPE_CHECKING:
    _GetOpsSummaryPaginatorBase = Paginator[GetOpsSummaryResultTypeDef]
else:
    _GetOpsSummaryPaginatorBase = Paginator  # type: ignore[assignment]

class GetOpsSummaryPaginator(_GetOpsSummaryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetOpsSummary.html#SSM.Paginator.GetOpsSummary)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getopssummarypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetOpsSummaryRequestPaginateTypeDef]
    ) -> PageIterator[GetOpsSummaryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetOpsSummary.html#SSM.Paginator.GetOpsSummary.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getopssummarypaginator)
        """

if TYPE_CHECKING:
    _GetParameterHistoryPaginatorBase = Paginator[GetParameterHistoryResultTypeDef]
else:
    _GetParameterHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetParameterHistoryPaginator(_GetParameterHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetParameterHistory.html#SSM.Paginator.GetParameterHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getparameterhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetParameterHistoryRequestPaginateTypeDef]
    ) -> PageIterator[GetParameterHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetParameterHistory.html#SSM.Paginator.GetParameterHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getparameterhistorypaginator)
        """

if TYPE_CHECKING:
    _GetParametersByPathPaginatorBase = Paginator[GetParametersByPathResultTypeDef]
else:
    _GetParametersByPathPaginatorBase = Paginator  # type: ignore[assignment]

class GetParametersByPathPaginator(_GetParametersByPathPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetParametersByPath.html#SSM.Paginator.GetParametersByPath)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getparametersbypathpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetParametersByPathRequestPaginateTypeDef]
    ) -> PageIterator[GetParametersByPathResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetParametersByPath.html#SSM.Paginator.GetParametersByPath.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getparametersbypathpaginator)
        """

if TYPE_CHECKING:
    _GetResourcePoliciesPaginatorBase = Paginator[GetResourcePoliciesResponseTypeDef]
else:
    _GetResourcePoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class GetResourcePoliciesPaginator(_GetResourcePoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetResourcePolicies.html#SSM.Paginator.GetResourcePolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getresourcepoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetResourcePoliciesRequestPaginateTypeDef]
    ) -> PageIterator[GetResourcePoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/GetResourcePolicies.html#SSM.Paginator.GetResourcePolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#getresourcepoliciespaginator)
        """

if TYPE_CHECKING:
    _ListAssociationVersionsPaginatorBase = Paginator[ListAssociationVersionsResultTypeDef]
else:
    _ListAssociationVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociationVersionsPaginator(_ListAssociationVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListAssociationVersions.html#SSM.Paginator.ListAssociationVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listassociationversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociationVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociationVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListAssociationVersions.html#SSM.Paginator.ListAssociationVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listassociationversionspaginator)
        """

if TYPE_CHECKING:
    _ListAssociationsPaginatorBase = Paginator[ListAssociationsResultTypeDef]
else:
    _ListAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociationsPaginator(_ListAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListAssociations.html#SSM.Paginator.ListAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListAssociations.html#SSM.Paginator.ListAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listassociationspaginator)
        """

if TYPE_CHECKING:
    _ListCommandInvocationsPaginatorBase = Paginator[ListCommandInvocationsResultTypeDef]
else:
    _ListCommandInvocationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCommandInvocationsPaginator(_ListCommandInvocationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListCommandInvocations.html#SSM.Paginator.ListCommandInvocations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listcommandinvocationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCommandInvocationsRequestPaginateTypeDef]
    ) -> PageIterator[ListCommandInvocationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListCommandInvocations.html#SSM.Paginator.ListCommandInvocations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listcommandinvocationspaginator)
        """

if TYPE_CHECKING:
    _ListCommandsPaginatorBase = Paginator[ListCommandsResultTypeDef]
else:
    _ListCommandsPaginatorBase = Paginator  # type: ignore[assignment]

class ListCommandsPaginator(_ListCommandsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListCommands.html#SSM.Paginator.ListCommands)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listcommandspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCommandsRequestPaginateTypeDef]
    ) -> PageIterator[ListCommandsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListCommands.html#SSM.Paginator.ListCommands.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listcommandspaginator)
        """

if TYPE_CHECKING:
    _ListComplianceItemsPaginatorBase = Paginator[ListComplianceItemsResultTypeDef]
else:
    _ListComplianceItemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListComplianceItemsPaginator(_ListComplianceItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListComplianceItems.html#SSM.Paginator.ListComplianceItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listcomplianceitemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComplianceItemsRequestPaginateTypeDef]
    ) -> PageIterator[ListComplianceItemsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListComplianceItems.html#SSM.Paginator.ListComplianceItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listcomplianceitemspaginator)
        """

if TYPE_CHECKING:
    _ListComplianceSummariesPaginatorBase = Paginator[ListComplianceSummariesResultTypeDef]
else:
    _ListComplianceSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListComplianceSummariesPaginator(_ListComplianceSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListComplianceSummaries.html#SSM.Paginator.ListComplianceSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listcompliancesummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListComplianceSummariesRequestPaginateTypeDef]
    ) -> PageIterator[ListComplianceSummariesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListComplianceSummaries.html#SSM.Paginator.ListComplianceSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listcompliancesummariespaginator)
        """

if TYPE_CHECKING:
    _ListDocumentVersionsPaginatorBase = Paginator[ListDocumentVersionsResultTypeDef]
else:
    _ListDocumentVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDocumentVersionsPaginator(_ListDocumentVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListDocumentVersions.html#SSM.Paginator.ListDocumentVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listdocumentversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDocumentVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListDocumentVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListDocumentVersions.html#SSM.Paginator.ListDocumentVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listdocumentversionspaginator)
        """

if TYPE_CHECKING:
    _ListDocumentsPaginatorBase = Paginator[ListDocumentsResultTypeDef]
else:
    _ListDocumentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDocumentsPaginator(_ListDocumentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListDocuments.html#SSM.Paginator.ListDocuments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listdocumentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDocumentsRequestPaginateTypeDef]
    ) -> PageIterator[ListDocumentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListDocuments.html#SSM.Paginator.ListDocuments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listdocumentspaginator)
        """

if TYPE_CHECKING:
    _ListNodesPaginatorBase = Paginator[ListNodesResultTypeDef]
else:
    _ListNodesPaginatorBase = Paginator  # type: ignore[assignment]

class ListNodesPaginator(_ListNodesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListNodes.html#SSM.Paginator.ListNodes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listnodespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNodesRequestPaginateTypeDef]
    ) -> PageIterator[ListNodesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListNodes.html#SSM.Paginator.ListNodes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listnodespaginator)
        """

if TYPE_CHECKING:
    _ListNodesSummaryPaginatorBase = Paginator[ListNodesSummaryResultTypeDef]
else:
    _ListNodesSummaryPaginatorBase = Paginator  # type: ignore[assignment]

class ListNodesSummaryPaginator(_ListNodesSummaryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListNodesSummary.html#SSM.Paginator.ListNodesSummary)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listnodessummarypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListNodesSummaryRequestPaginateTypeDef]
    ) -> PageIterator[ListNodesSummaryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListNodesSummary.html#SSM.Paginator.ListNodesSummary.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listnodessummarypaginator)
        """

if TYPE_CHECKING:
    _ListOpsItemEventsPaginatorBase = Paginator[ListOpsItemEventsResponseTypeDef]
else:
    _ListOpsItemEventsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOpsItemEventsPaginator(_ListOpsItemEventsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListOpsItemEvents.html#SSM.Paginator.ListOpsItemEvents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listopsitemeventspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOpsItemEventsRequestPaginateTypeDef]
    ) -> PageIterator[ListOpsItemEventsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListOpsItemEvents.html#SSM.Paginator.ListOpsItemEvents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listopsitemeventspaginator)
        """

if TYPE_CHECKING:
    _ListOpsItemRelatedItemsPaginatorBase = Paginator[ListOpsItemRelatedItemsResponseTypeDef]
else:
    _ListOpsItemRelatedItemsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOpsItemRelatedItemsPaginator(_ListOpsItemRelatedItemsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListOpsItemRelatedItems.html#SSM.Paginator.ListOpsItemRelatedItems)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listopsitemrelateditemspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOpsItemRelatedItemsRequestPaginateTypeDef]
    ) -> PageIterator[ListOpsItemRelatedItemsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListOpsItemRelatedItems.html#SSM.Paginator.ListOpsItemRelatedItems.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listopsitemrelateditemspaginator)
        """

if TYPE_CHECKING:
    _ListOpsMetadataPaginatorBase = Paginator[ListOpsMetadataResultTypeDef]
else:
    _ListOpsMetadataPaginatorBase = Paginator  # type: ignore[assignment]

class ListOpsMetadataPaginator(_ListOpsMetadataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListOpsMetadata.html#SSM.Paginator.ListOpsMetadata)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listopsmetadatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOpsMetadataRequestPaginateTypeDef]
    ) -> PageIterator[ListOpsMetadataResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListOpsMetadata.html#SSM.Paginator.ListOpsMetadata.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listopsmetadatapaginator)
        """

if TYPE_CHECKING:
    _ListResourceComplianceSummariesPaginatorBase = Paginator[
        ListResourceComplianceSummariesResultTypeDef
    ]
else:
    _ListResourceComplianceSummariesPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceComplianceSummariesPaginator(_ListResourceComplianceSummariesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListResourceComplianceSummaries.html#SSM.Paginator.ListResourceComplianceSummaries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listresourcecompliancesummariespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceComplianceSummariesRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceComplianceSummariesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListResourceComplianceSummaries.html#SSM.Paginator.ListResourceComplianceSummaries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listresourcecompliancesummariespaginator)
        """

if TYPE_CHECKING:
    _ListResourceDataSyncPaginatorBase = Paginator[ListResourceDataSyncResultTypeDef]
else:
    _ListResourceDataSyncPaginatorBase = Paginator  # type: ignore[assignment]

class ListResourceDataSyncPaginator(_ListResourceDataSyncPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListResourceDataSync.html#SSM.Paginator.ListResourceDataSync)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listresourcedatasyncpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListResourceDataSyncRequestPaginateTypeDef]
    ) -> PageIterator[ListResourceDataSyncResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/paginator/ListResourceDataSync.html#SSM.Paginator.ListResourceDataSync.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm/paginators/#listresourcedatasyncpaginator)
        """
