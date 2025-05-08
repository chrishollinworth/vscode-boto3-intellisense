"""
Type annotations for iotthingsgraph service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iotthingsgraph.client import IoTThingsGraphClient
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

    session = Session()
    client: IoTThingsGraphClient = session.client("iotthingsgraph")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    GetFlowTemplateRevisionsRequestPaginateTypeDef,
    GetFlowTemplateRevisionsResponseTypeDef,
    GetSystemTemplateRevisionsRequestPaginateTypeDef,
    GetSystemTemplateRevisionsResponseTypeDef,
    ListFlowExecutionMessagesRequestPaginateTypeDef,
    ListFlowExecutionMessagesResponseTypeDef,
    ListTagsForResourceRequestPaginateTypeDef,
    ListTagsForResourceResponseTypeDef,
    SearchEntitiesRequestPaginateTypeDef,
    SearchEntitiesResponseTypeDef,
    SearchFlowExecutionsRequestPaginateTypeDef,
    SearchFlowExecutionsResponseTypeDef,
    SearchFlowTemplatesRequestPaginateTypeDef,
    SearchFlowTemplatesResponseTypeDef,
    SearchSystemInstancesRequestPaginateTypeDef,
    SearchSystemInstancesResponseTypeDef,
    SearchSystemTemplatesRequestPaginateTypeDef,
    SearchSystemTemplatesResponseTypeDef,
    SearchThingsRequestPaginateTypeDef,
    SearchThingsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _GetFlowTemplateRevisionsPaginatorBase = Paginator[GetFlowTemplateRevisionsResponseTypeDef]
else:
    _GetFlowTemplateRevisionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetFlowTemplateRevisionsPaginator(_GetFlowTemplateRevisionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/GetFlowTemplateRevisions.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#getflowtemplaterevisionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetFlowTemplateRevisionsRequestPaginateTypeDef]
    ) -> PageIterator[GetFlowTemplateRevisionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/GetFlowTemplateRevisions.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#getflowtemplaterevisionspaginator)
        """

if TYPE_CHECKING:
    _GetSystemTemplateRevisionsPaginatorBase = Paginator[GetSystemTemplateRevisionsResponseTypeDef]
else:
    _GetSystemTemplateRevisionsPaginatorBase = Paginator  # type: ignore[assignment]

class GetSystemTemplateRevisionsPaginator(_GetSystemTemplateRevisionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/GetSystemTemplateRevisions.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#getsystemtemplaterevisionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSystemTemplateRevisionsRequestPaginateTypeDef]
    ) -> PageIterator[GetSystemTemplateRevisionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/GetSystemTemplateRevisions.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#getsystemtemplaterevisionspaginator)
        """

if TYPE_CHECKING:
    _ListFlowExecutionMessagesPaginatorBase = Paginator[ListFlowExecutionMessagesResponseTypeDef]
else:
    _ListFlowExecutionMessagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListFlowExecutionMessagesPaginator(_ListFlowExecutionMessagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/ListFlowExecutionMessages.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#listflowexecutionmessagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFlowExecutionMessagesRequestPaginateTypeDef]
    ) -> PageIterator[ListFlowExecutionMessagesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/ListFlowExecutionMessages.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#listflowexecutionmessagespaginator)
        """

if TYPE_CHECKING:
    _ListTagsForResourcePaginatorBase = Paginator[ListTagsForResourceResponseTypeDef]
else:
    _ListTagsForResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListTagsForResourcePaginator(_ListTagsForResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/ListTagsForResource.html#IoTThingsGraph.Paginator.ListTagsForResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#listtagsforresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTagsForResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListTagsForResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/ListTagsForResource.html#IoTThingsGraph.Paginator.ListTagsForResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#listtagsforresourcepaginator)
        """

if TYPE_CHECKING:
    _SearchEntitiesPaginatorBase = Paginator[SearchEntitiesResponseTypeDef]
else:
    _SearchEntitiesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchEntitiesPaginator(_SearchEntitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchEntities.html#IoTThingsGraph.Paginator.SearchEntities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchEntitiesRequestPaginateTypeDef]
    ) -> PageIterator[SearchEntitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchEntities.html#IoTThingsGraph.Paginator.SearchEntities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchentitiespaginator)
        """

if TYPE_CHECKING:
    _SearchFlowExecutionsPaginatorBase = Paginator[SearchFlowExecutionsResponseTypeDef]
else:
    _SearchFlowExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchFlowExecutionsPaginator(_SearchFlowExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchFlowExecutions.html#IoTThingsGraph.Paginator.SearchFlowExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchflowexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchFlowExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[SearchFlowExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchFlowExecutions.html#IoTThingsGraph.Paginator.SearchFlowExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchflowexecutionspaginator)
        """

if TYPE_CHECKING:
    _SearchFlowTemplatesPaginatorBase = Paginator[SearchFlowTemplatesResponseTypeDef]
else:
    _SearchFlowTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchFlowTemplatesPaginator(_SearchFlowTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchFlowTemplates.html#IoTThingsGraph.Paginator.SearchFlowTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchflowtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchFlowTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[SearchFlowTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchFlowTemplates.html#IoTThingsGraph.Paginator.SearchFlowTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchflowtemplatespaginator)
        """

if TYPE_CHECKING:
    _SearchSystemInstancesPaginatorBase = Paginator[SearchSystemInstancesResponseTypeDef]
else:
    _SearchSystemInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchSystemInstancesPaginator(_SearchSystemInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchSystemInstances.html#IoTThingsGraph.Paginator.SearchSystemInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchsysteminstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchSystemInstancesRequestPaginateTypeDef]
    ) -> PageIterator[SearchSystemInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchSystemInstances.html#IoTThingsGraph.Paginator.SearchSystemInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchsysteminstancespaginator)
        """

if TYPE_CHECKING:
    _SearchSystemTemplatesPaginatorBase = Paginator[SearchSystemTemplatesResponseTypeDef]
else:
    _SearchSystemTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchSystemTemplatesPaginator(_SearchSystemTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchSystemTemplates.html#IoTThingsGraph.Paginator.SearchSystemTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchsystemtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchSystemTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[SearchSystemTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchSystemTemplates.html#IoTThingsGraph.Paginator.SearchSystemTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchsystemtemplatespaginator)
        """

if TYPE_CHECKING:
    _SearchThingsPaginatorBase = Paginator[SearchThingsResponseTypeDef]
else:
    _SearchThingsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchThingsPaginator(_SearchThingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchThings.html#IoTThingsGraph.Paginator.SearchThings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchthingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchThingsRequestPaginateTypeDef]
    ) -> PageIterator[SearchThingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotthingsgraph/paginator/SearchThings.html#IoTThingsGraph.Paginator.SearchThings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/paginators/#searchthingspaginator)
        """
