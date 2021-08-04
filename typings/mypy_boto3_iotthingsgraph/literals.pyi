"""
Type annotations for iotthingsgraph service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/literals.html)

Usage::

    ```python
    from mypy_boto3_iotthingsgraph.literals import DefinitionLanguageType

    data: DefinitionLanguageType = "GRAPHQL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DefinitionLanguageType",
    "DeploymentTargetType",
    "EntityFilterNameType",
    "EntityTypeType",
    "FlowExecutionEventTypeType",
    "FlowExecutionStatusType",
    "FlowTemplateFilterNameType",
    "GetFlowTemplateRevisionsPaginatorName",
    "GetSystemTemplateRevisionsPaginatorName",
    "ListFlowExecutionMessagesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "NamespaceDeletionStatusErrorCodesType",
    "NamespaceDeletionStatusType",
    "SearchEntitiesPaginatorName",
    "SearchFlowExecutionsPaginatorName",
    "SearchFlowTemplatesPaginatorName",
    "SearchSystemInstancesPaginatorName",
    "SearchSystemTemplatesPaginatorName",
    "SearchThingsPaginatorName",
    "SystemInstanceDeploymentStatusType",
    "SystemInstanceFilterNameType",
    "SystemTemplateFilterNameType",
    "UploadStatusType",
)

DefinitionLanguageType = Literal["GRAPHQL"]
DeploymentTargetType = Literal["CLOUD", "GREENGRASS"]
EntityFilterNameType = Literal["NAME", "NAMESPACE", "REFERENCED_ENTITY_ID", "SEMANTIC_TYPE_PATH"]
EntityTypeType = Literal[
    "ACTION",
    "CAPABILITY",
    "DEVICE",
    "DEVICE_MODEL",
    "ENUM",
    "EVENT",
    "MAPPING",
    "PROPERTY",
    "SERVICE",
    "STATE",
]
FlowExecutionEventTypeType = Literal[
    "ACKNOWLEDGE_TASK_MESSAGE",
    "ACTIVITY_FAILED",
    "ACTIVITY_SCHEDULED",
    "ACTIVITY_STARTED",
    "ACTIVITY_SUCCEEDED",
    "EXECUTION_ABORTED",
    "EXECUTION_FAILED",
    "EXECUTION_STARTED",
    "EXECUTION_SUCCEEDED",
    "SCHEDULE_NEXT_READY_STEPS_TASK",
    "START_FLOW_EXECUTION_TASK",
    "STEP_FAILED",
    "STEP_STARTED",
    "STEP_SUCCEEDED",
    "THING_ACTION_TASK",
    "THING_ACTION_TASK_FAILED",
    "THING_ACTION_TASK_SUCCEEDED",
]
FlowExecutionStatusType = Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED"]
FlowTemplateFilterNameType = Literal["DEVICE_MODEL_ID"]
GetFlowTemplateRevisionsPaginatorName = Literal["get_flow_template_revisions"]
GetSystemTemplateRevisionsPaginatorName = Literal["get_system_template_revisions"]
ListFlowExecutionMessagesPaginatorName = Literal["list_flow_execution_messages"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
NamespaceDeletionStatusErrorCodesType = Literal["VALIDATION_FAILED"]
NamespaceDeletionStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
SearchEntitiesPaginatorName = Literal["search_entities"]
SearchFlowExecutionsPaginatorName = Literal["search_flow_executions"]
SearchFlowTemplatesPaginatorName = Literal["search_flow_templates"]
SearchSystemInstancesPaginatorName = Literal["search_system_instances"]
SearchSystemTemplatesPaginatorName = Literal["search_system_templates"]
SearchThingsPaginatorName = Literal["search_things"]
SystemInstanceDeploymentStatusType = Literal[
    "BOOTSTRAP",
    "DELETED_IN_TARGET",
    "DEPLOYED_IN_TARGET",
    "DEPLOY_IN_PROGRESS",
    "FAILED",
    "NOT_DEPLOYED",
    "PENDING_DELETE",
    "UNDEPLOY_IN_PROGRESS",
]
SystemInstanceFilterNameType = Literal["GREENGRASS_GROUP_NAME", "STATUS", "SYSTEM_TEMPLATE_ID"]
SystemTemplateFilterNameType = Literal["FLOW_TEMPLATE_ID"]
UploadStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
