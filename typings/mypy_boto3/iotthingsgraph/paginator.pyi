"""
Type annotations for iotthingsgraph service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iotthingsgraph import IoTThingsGraphClient
    from mypy_boto3_iotthingsgraph.paginator import (
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

    client: IoTThingsGraphClient = boto3.client("iotthingsgraph")

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
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import EntityTypeType
from .type_defs import (
    EntityFilterTypeDef,
    FlowTemplateFilterTypeDef,
    GetFlowTemplateRevisionsResponseTypeDef,
    GetSystemTemplateRevisionsResponseTypeDef,
    ListFlowExecutionMessagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PaginatorConfigTypeDef,
    SearchEntitiesResponseTypeDef,
    SearchFlowExecutionsResponseTypeDef,
    SearchFlowTemplatesResponseTypeDef,
    SearchSystemInstancesResponseTypeDef,
    SearchSystemTemplatesResponseTypeDef,
    SearchThingsResponseTypeDef,
    SystemInstanceFilterTypeDef,
    SystemTemplateFilterTypeDef,
)

__all__ = (
    "GetFlowTemplateRevisionsPaginator",
    "GetSystemTemplateRevisionsPaginator",
    "ListFlowExecutionMessagesPaginator",
    "ListTagsForResourcePaginator",
    "SearchEntitiesPaginator",
    "SearchFlowExecutionsPaginator",
    "SearchFlowTemplatesPaginator",
    "SearchSystemInstancesPaginator",
    "SearchSystemTemplatesPaginator",
    "SearchThingsPaginator",
)

class GetFlowTemplateRevisionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#getflowtemplaterevisionspaginator)
    """

    def paginate(
        self, *, id: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetFlowTemplateRevisionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#getflowtemplaterevisionspaginator)
        """

class GetSystemTemplateRevisionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#getsystemtemplaterevisionspaginator)
    """

    def paginate(
        self, *, id: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSystemTemplateRevisionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#getsystemtemplaterevisionspaginator)
        """

class ListFlowExecutionMessagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#listflowexecutionmessagespaginator)
    """

    def paginate(
        self, *, flowExecutionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFlowExecutionMessagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#listflowexecutionmessagespaginator)
        """

class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#listtagsforresourcepaginator)
    """

    def paginate(
        self, *, resourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#listtagsforresourcepaginator)
        """

class SearchEntitiesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchentitiespaginator)
    """

    def paginate(
        self,
        *,
        entityTypes: List[EntityTypeType],
        filters: List["EntityFilterTypeDef"] = None,
        namespaceVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchEntitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchentitiespaginator)
        """

class SearchFlowExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchflowexecutionspaginator)
    """

    def paginate(
        self,
        *,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchFlowExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchflowexecutionspaginator)
        """

class SearchFlowTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchflowtemplatespaginator)
    """

    def paginate(
        self,
        *,
        filters: List["FlowTemplateFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchFlowTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchflowtemplatespaginator)
        """

class SearchSystemInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchsysteminstancespaginator)
    """

    def paginate(
        self,
        *,
        filters: List["SystemInstanceFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchSystemInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchsysteminstancespaginator)
        """

class SearchSystemTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchsystemtemplatespaginator)
    """

    def paginate(
        self,
        *,
        filters: List["SystemTemplateFilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchSystemTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchsystemtemplatespaginator)
        """

class SearchThingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchthingspaginator)
    """

    def paginate(
        self,
        *,
        entityId: str,
        namespaceVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchThingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators.html#searchthingspaginator)
        """
