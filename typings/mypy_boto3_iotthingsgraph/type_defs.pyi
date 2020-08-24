"""
Main interface for iotthingsgraph service type definitions.

Usage::

    ```python
    from mypy_boto3_iotthingsgraph.type_defs import DefinitionDocumentTypeDef

    data: DefinitionDocumentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DefinitionDocumentTypeDef",
    "DependencyRevisionTypeDef",
    "EntityDescriptionTypeDef",
    "FlowExecutionMessageTypeDef",
    "FlowExecutionSummaryTypeDef",
    "FlowTemplateDescriptionTypeDef",
    "FlowTemplateSummaryTypeDef",
    "MetricsConfigurationTypeDef",
    "SystemInstanceDescriptionTypeDef",
    "SystemInstanceSummaryTypeDef",
    "SystemTemplateDescriptionTypeDef",
    "SystemTemplateSummaryTypeDef",
    "TagTypeDef",
    "ThingTypeDef",
    "CreateFlowTemplateResponseTypeDef",
    "CreateSystemInstanceResponseTypeDef",
    "CreateSystemTemplateResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeploySystemInstanceResponseTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "EntityFilterTypeDef",
    "FlowTemplateFilterTypeDef",
    "GetEntitiesResponseTypeDef",
    "GetFlowTemplateResponseTypeDef",
    "GetFlowTemplateRevisionsResponseTypeDef",
    "GetNamespaceDeletionStatusResponseTypeDef",
    "GetSystemInstanceResponseTypeDef",
    "GetSystemTemplateResponseTypeDef",
    "GetSystemTemplateRevisionsResponseTypeDef",
    "GetUploadStatusResponseTypeDef",
    "ListFlowExecutionMessagesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "SearchEntitiesResponseTypeDef",
    "SearchFlowExecutionsResponseTypeDef",
    "SearchFlowTemplatesResponseTypeDef",
    "SearchSystemInstancesResponseTypeDef",
    "SearchSystemTemplatesResponseTypeDef",
    "SearchThingsResponseTypeDef",
    "SystemInstanceFilterTypeDef",
    "SystemTemplateFilterTypeDef",
    "UndeploySystemInstanceResponseTypeDef",
    "UpdateFlowTemplateResponseTypeDef",
    "UpdateSystemTemplateResponseTypeDef",
    "UploadEntityDefinitionsResponseTypeDef",
)

DefinitionDocumentTypeDef = TypedDict(
    "DefinitionDocumentTypeDef", {"language": Literal["GRAPHQL"], "text": str}
)

DependencyRevisionTypeDef = TypedDict(
    "DependencyRevisionTypeDef", {"id": str, "revisionNumber": int}, total=False
)

EntityDescriptionTypeDef = TypedDict(
    "EntityDescriptionTypeDef",
    {
        "id": str,
        "arn": str,
        "type": Literal[
            "DEVICE",
            "SERVICE",
            "DEVICE_MODEL",
            "CAPABILITY",
            "STATE",
            "ACTION",
            "EVENT",
            "PROPERTY",
            "MAPPING",
            "ENUM",
        ],
        "createdAt": datetime,
        "definition": "DefinitionDocumentTypeDef",
    },
    total=False,
)

FlowExecutionMessageTypeDef = TypedDict(
    "FlowExecutionMessageTypeDef",
    {
        "messageId": str,
        "eventType": Literal[
            "EXECUTION_STARTED",
            "EXECUTION_FAILED",
            "EXECUTION_ABORTED",
            "EXECUTION_SUCCEEDED",
            "STEP_STARTED",
            "STEP_FAILED",
            "STEP_SUCCEEDED",
            "ACTIVITY_SCHEDULED",
            "ACTIVITY_STARTED",
            "ACTIVITY_FAILED",
            "ACTIVITY_SUCCEEDED",
            "START_FLOW_EXECUTION_TASK",
            "SCHEDULE_NEXT_READY_STEPS_TASK",
            "THING_ACTION_TASK",
            "THING_ACTION_TASK_FAILED",
            "THING_ACTION_TASK_SUCCEEDED",
            "ACKNOWLEDGE_TASK_MESSAGE",
        ],
        "timestamp": datetime,
        "payload": str,
    },
    total=False,
)

FlowExecutionSummaryTypeDef = TypedDict(
    "FlowExecutionSummaryTypeDef",
    {
        "flowExecutionId": str,
        "status": Literal["RUNNING", "ABORTED", "SUCCEEDED", "FAILED"],
        "systemInstanceId": str,
        "flowTemplateId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

FlowTemplateDescriptionTypeDef = TypedDict(
    "FlowTemplateDescriptionTypeDef",
    {
        "summary": "FlowTemplateSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "validatedNamespaceVersion": int,
    },
    total=False,
)

FlowTemplateSummaryTypeDef = TypedDict(
    "FlowTemplateSummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

MetricsConfigurationTypeDef = TypedDict(
    "MetricsConfigurationTypeDef",
    {"cloudMetricEnabled": bool, "metricRuleRoleArn": str},
    total=False,
)

SystemInstanceDescriptionTypeDef = TypedDict(
    "SystemInstanceDescriptionTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "s3BucketName": str,
        "metricsConfiguration": "MetricsConfigurationTypeDef",
        "validatedNamespaceVersion": int,
        "validatedDependencyRevisions": List["DependencyRevisionTypeDef"],
        "flowActionsRoleArn": str,
    },
    total=False,
)

SystemInstanceSummaryTypeDef = TypedDict(
    "SystemInstanceSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": Literal[
            "NOT_DEPLOYED",
            "BOOTSTRAP",
            "DEPLOY_IN_PROGRESS",
            "DEPLOYED_IN_TARGET",
            "UNDEPLOY_IN_PROGRESS",
            "FAILED",
            "PENDING_DELETE",
            "DELETED_IN_TARGET",
        ],
        "target": Literal["GREENGRASS", "CLOUD"],
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)

SystemTemplateDescriptionTypeDef = TypedDict(
    "SystemTemplateDescriptionTypeDef",
    {
        "summary": "SystemTemplateSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "validatedNamespaceVersion": int,
    },
    total=False,
)

SystemTemplateSummaryTypeDef = TypedDict(
    "SystemTemplateSummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str})

ThingTypeDef = TypedDict("ThingTypeDef", {"thingArn": str, "thingName": str}, total=False)

CreateFlowTemplateResponseTypeDef = TypedDict(
    "CreateFlowTemplateResponseTypeDef", {"summary": "FlowTemplateSummaryTypeDef"}, total=False
)

CreateSystemInstanceResponseTypeDef = TypedDict(
    "CreateSystemInstanceResponseTypeDef", {"summary": "SystemInstanceSummaryTypeDef"}, total=False
)

CreateSystemTemplateResponseTypeDef = TypedDict(
    "CreateSystemTemplateResponseTypeDef", {"summary": "SystemTemplateSummaryTypeDef"}, total=False
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef", {"namespaceArn": str, "namespaceName": str}, total=False
)

_RequiredDeploySystemInstanceResponseTypeDef = TypedDict(
    "_RequiredDeploySystemInstanceResponseTypeDef", {"summary": "SystemInstanceSummaryTypeDef"}
)
_OptionalDeploySystemInstanceResponseTypeDef = TypedDict(
    "_OptionalDeploySystemInstanceResponseTypeDef", {"greengrassDeploymentId": str}, total=False
)


class DeploySystemInstanceResponseTypeDef(
    _RequiredDeploySystemInstanceResponseTypeDef, _OptionalDeploySystemInstanceResponseTypeDef
):
    pass


DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "trackingNamespaceName": str,
        "trackingNamespaceVersion": int,
        "namespaceVersion": int,
    },
    total=False,
)

EntityFilterTypeDef = TypedDict(
    "EntityFilterTypeDef",
    {
        "name": Literal["NAME", "NAMESPACE", "SEMANTIC_TYPE_PATH", "REFERENCED_ENTITY_ID"],
        "value": List[str],
    },
    total=False,
)

FlowTemplateFilterTypeDef = TypedDict(
    "FlowTemplateFilterTypeDef", {"name": Literal["DEVICE_MODEL_ID"], "value": List[str]}
)

GetEntitiesResponseTypeDef = TypedDict(
    "GetEntitiesResponseTypeDef", {"descriptions": List["EntityDescriptionTypeDef"]}, total=False
)

GetFlowTemplateResponseTypeDef = TypedDict(
    "GetFlowTemplateResponseTypeDef", {"description": "FlowTemplateDescriptionTypeDef"}, total=False
)

GetFlowTemplateRevisionsResponseTypeDef = TypedDict(
    "GetFlowTemplateRevisionsResponseTypeDef",
    {"summaries": List["FlowTemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

GetNamespaceDeletionStatusResponseTypeDef = TypedDict(
    "GetNamespaceDeletionStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "status": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "errorCode": Literal["VALIDATION_FAILED"],
        "errorMessage": str,
    },
    total=False,
)

GetSystemInstanceResponseTypeDef = TypedDict(
    "GetSystemInstanceResponseTypeDef",
    {"description": "SystemInstanceDescriptionTypeDef"},
    total=False,
)

GetSystemTemplateResponseTypeDef = TypedDict(
    "GetSystemTemplateResponseTypeDef",
    {"description": "SystemTemplateDescriptionTypeDef"},
    total=False,
)

GetSystemTemplateRevisionsResponseTypeDef = TypedDict(
    "GetSystemTemplateRevisionsResponseTypeDef",
    {"summaries": List["SystemTemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

_RequiredGetUploadStatusResponseTypeDef = TypedDict(
    "_RequiredGetUploadStatusResponseTypeDef",
    {
        "uploadId": str,
        "uploadStatus": Literal["IN_PROGRESS", "SUCCEEDED", "FAILED"],
        "createdDate": datetime,
    },
)
_OptionalGetUploadStatusResponseTypeDef = TypedDict(
    "_OptionalGetUploadStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "namespaceVersion": int,
        "failureReason": List[str],
    },
    total=False,
)


class GetUploadStatusResponseTypeDef(
    _RequiredGetUploadStatusResponseTypeDef, _OptionalGetUploadStatusResponseTypeDef
):
    pass


ListFlowExecutionMessagesResponseTypeDef = TypedDict(
    "ListFlowExecutionMessagesResponseTypeDef",
    {"messages": List["FlowExecutionMessageTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"tags": List["TagTypeDef"], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SearchEntitiesResponseTypeDef = TypedDict(
    "SearchEntitiesResponseTypeDef",
    {"descriptions": List["EntityDescriptionTypeDef"], "nextToken": str},
    total=False,
)

SearchFlowExecutionsResponseTypeDef = TypedDict(
    "SearchFlowExecutionsResponseTypeDef",
    {"summaries": List["FlowExecutionSummaryTypeDef"], "nextToken": str},
    total=False,
)

SearchFlowTemplatesResponseTypeDef = TypedDict(
    "SearchFlowTemplatesResponseTypeDef",
    {"summaries": List["FlowTemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

SearchSystemInstancesResponseTypeDef = TypedDict(
    "SearchSystemInstancesResponseTypeDef",
    {"summaries": List["SystemInstanceSummaryTypeDef"], "nextToken": str},
    total=False,
)

SearchSystemTemplatesResponseTypeDef = TypedDict(
    "SearchSystemTemplatesResponseTypeDef",
    {"summaries": List["SystemTemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

SearchThingsResponseTypeDef = TypedDict(
    "SearchThingsResponseTypeDef", {"things": List["ThingTypeDef"], "nextToken": str}, total=False
)

SystemInstanceFilterTypeDef = TypedDict(
    "SystemInstanceFilterTypeDef",
    {"name": Literal["SYSTEM_TEMPLATE_ID", "STATUS", "GREENGRASS_GROUP_NAME"], "value": List[str]},
    total=False,
)

SystemTemplateFilterTypeDef = TypedDict(
    "SystemTemplateFilterTypeDef", {"name": Literal["FLOW_TEMPLATE_ID"], "value": List[str]}
)

UndeploySystemInstanceResponseTypeDef = TypedDict(
    "UndeploySystemInstanceResponseTypeDef",
    {"summary": "SystemInstanceSummaryTypeDef"},
    total=False,
)

UpdateFlowTemplateResponseTypeDef = TypedDict(
    "UpdateFlowTemplateResponseTypeDef", {"summary": "FlowTemplateSummaryTypeDef"}, total=False
)

UpdateSystemTemplateResponseTypeDef = TypedDict(
    "UpdateSystemTemplateResponseTypeDef", {"summary": "SystemTemplateSummaryTypeDef"}, total=False
)

UploadEntityDefinitionsResponseTypeDef = TypedDict(
    "UploadEntityDefinitionsResponseTypeDef", {"uploadId": str}
)
