"""
Type annotations for migrationhuborchestrator service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migrationhuborchestrator/literals.html)

Usage::

    ```python
    from mypy_boto3_migrationhuborchestrator.literals import DataTypeType

    data: DataTypeType = "INTEGER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DataTypeType",
    "ListPluginsPaginatorName",
    "ListTemplateStepGroupsPaginatorName",
    "ListTemplateStepsPaginatorName",
    "ListTemplatesPaginatorName",
    "ListWorkflowStepGroupsPaginatorName",
    "ListWorkflowStepsPaginatorName",
    "ListWorkflowsPaginatorName",
    "MigrationWorkflowStatusEnumType",
    "OwnerType",
    "PluginHealthType",
    "RunEnvironmentType",
    "StepActionTypeType",
    "StepGroupStatusType",
    "StepStatusType",
    "TargetTypeType",
    "TemplateStatusType",
)

DataTypeType = Literal["INTEGER", "STRING", "STRINGLIST", "STRINGMAP"]
ListPluginsPaginatorName = Literal["list_plugins"]
ListTemplateStepGroupsPaginatorName = Literal["list_template_step_groups"]
ListTemplateStepsPaginatorName = Literal["list_template_steps"]
ListTemplatesPaginatorName = Literal["list_templates"]
ListWorkflowStepGroupsPaginatorName = Literal["list_workflow_step_groups"]
ListWorkflowStepsPaginatorName = Literal["list_workflow_steps"]
ListWorkflowsPaginatorName = Literal["list_workflows"]
MigrationWorkflowStatusEnumType = Literal[
    "COMPLETED",
    "CREATING",
    "CREATION_FAILED",
    "DELETED",
    "DELETING",
    "DELETION_FAILED",
    "IN_PROGRESS",
    "NOT_STARTED",
    "PAUSED",
    "PAUSING",
    "PAUSING_FAILED",
    "STARTING",
    "USER_ATTENTION_REQUIRED",
    "WORKFLOW_FAILED",
]
OwnerType = Literal["AWS_MANAGED", "CUSTOM"]
PluginHealthType = Literal["HEALTHY", "UNHEALTHY"]
RunEnvironmentType = Literal["AWS", "ONPREMISE"]
StepActionTypeType = Literal["AUTOMATED", "MANUAL"]
StepGroupStatusType = Literal[
    "AWAITING_DEPENDENCIES",
    "COMPLETED",
    "FAILED",
    "IN_PROGRESS",
    "PAUSED",
    "PAUSING",
    "READY",
    "USER_ATTENTION_REQUIRED",
]
StepStatusType = Literal[
    "AWAITING_DEPENDENCIES",
    "COMPLETED",
    "FAILED",
    "IN_PROGRESS",
    "PAUSED",
    "READY",
    "USER_ATTENTION_REQUIRED",
]
TargetTypeType = Literal["ALL", "NONE", "SINGLE"]
TemplateStatusType = Literal["CREATED"]
