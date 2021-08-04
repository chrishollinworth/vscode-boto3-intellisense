"""
Main interface for iotthingsgraph service.

Usage::

    ```python
    import boto3
    from mypy_boto3_iotthingsgraph import (
        Client,
        GetFlowTemplateRevisionsPaginator,
        GetSystemTemplateRevisionsPaginator,
        IoTThingsGraphClient,
        ListFlowExecutionMessagesPaginator,
        ListTagsForResourcePaginator,
        SearchEntitiesPaginator,
        SearchFlowExecutionsPaginator,
        SearchFlowTemplatesPaginator,
        SearchSystemInstancesPaginator,
        SearchSystemTemplatesPaginator,
        SearchThingsPaginator,
    )

    session = boto3.Session()

    client: IoTThingsGraphClient = boto3.client("iotthingsgraph")
    session_client: IoTThingsGraphClient = session.client("iotthingsgraph")

    get_flow_template_revisions_paginator: GetFlowTemplateRevisionsPaginator = client.get_paginator("get_flow_template_revisions")
    get_system_template_revisions_paginator: GetSystemTemplateRevisionsPaginator = client.get_paginator("get_system_template_revisions")
    list_flow_execution_messages_paginator: ListFlowExecutionMessagesPaginator = client.get_paginator("list_flow_execution_messages")
    list_tags_for_resource_paginator: ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
    search_entities_paginator: SearchEntitiesPaginator = client.get_paginator("search_entities")
    search_flow_executions_paginator: SearchFlowExecutionsPaginator = client.get_paginator("search_flow_executions")
    search_flow_templates_paginator: SearchFlowTemplatesPaginator = client.get_paginator("search_flow_templates")
    search_system_instances_paginator: SearchSystemInstancesPaginator = client.get_paginator("search_system_instances")
    search_system_templates_paginator: SearchSystemTemplatesPaginator = client.get_paginator("search_system_templates")
    search_things_paginator: SearchThingsPaginator = client.get_paginator("search_things")
    ```
"""
from .client import IoTThingsGraphClient
from .paginator import (
    GetFlowTemplateRevisionsPaginator,
    GetSystemTemplateRevisionsPaginator,
    ListFlowExecutionMessagesPaginator,
    ListTagsForResourcePaginator,
    SearchEntitiesPaginator,
    SearchFlowExecutionsPaginator,
    SearchFlowTemplatesPaginator,
    SearchSystemInstancesPaginator,
    SearchSystemTemplatesPaginator,
    SearchThingsPaginator,
)

Client = IoTThingsGraphClient

__all__ = (
    "Client",
    "GetFlowTemplateRevisionsPaginator",
    "GetSystemTemplateRevisionsPaginator",
    "IoTThingsGraphClient",
    "ListFlowExecutionMessagesPaginator",
    "ListTagsForResourcePaginator",
    "SearchEntitiesPaginator",
    "SearchFlowExecutionsPaginator",
    "SearchFlowTemplatesPaginator",
    "SearchSystemInstancesPaginator",
    "SearchSystemTemplatesPaginator",
    "SearchThingsPaginator",
)
