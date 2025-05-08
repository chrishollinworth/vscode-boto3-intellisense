"""
Type annotations for ecs service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ecs.client import ECSClient
    from mypy_boto3_ecs.paginator import (
        ListAccountSettingsPaginator,
        ListAttributesPaginator,
        ListClustersPaginator,
        ListContainerInstancesPaginator,
        ListServicesByNamespacePaginator,
        ListServicesPaginator,
        ListTaskDefinitionFamiliesPaginator,
        ListTaskDefinitionsPaginator,
        ListTasksPaginator,
    )

    session = Session()
    client: ECSClient = session.client("ecs")

    list_account_settings_paginator: ListAccountSettingsPaginator = client.get_paginator("list_account_settings")
    list_attributes_paginator: ListAttributesPaginator = client.get_paginator("list_attributes")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_container_instances_paginator: ListContainerInstancesPaginator = client.get_paginator("list_container_instances")
    list_services_by_namespace_paginator: ListServicesByNamespacePaginator = client.get_paginator("list_services_by_namespace")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    list_task_definition_families_paginator: ListTaskDefinitionFamiliesPaginator = client.get_paginator("list_task_definition_families")
    list_task_definitions_paginator: ListTaskDefinitionsPaginator = client.get_paginator("list_task_definitions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAccountSettingsRequestPaginateTypeDef,
    ListAccountSettingsResponseTypeDef,
    ListAttributesRequestPaginateTypeDef,
    ListAttributesResponseTypeDef,
    ListClustersRequestPaginateTypeDef,
    ListClustersResponseTypeDef,
    ListContainerInstancesRequestPaginateTypeDef,
    ListContainerInstancesResponseTypeDef,
    ListServicesByNamespaceRequestPaginateTypeDef,
    ListServicesByNamespaceResponseTypeDef,
    ListServicesRequestPaginateTypeDef,
    ListServicesResponseTypeDef,
    ListTaskDefinitionFamiliesRequestPaginateTypeDef,
    ListTaskDefinitionFamiliesResponseTypeDef,
    ListTaskDefinitionsRequestPaginateTypeDef,
    ListTaskDefinitionsResponseTypeDef,
    ListTasksRequestPaginateTypeDef,
    ListTasksResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAccountSettingsPaginator",
    "ListAttributesPaginator",
    "ListClustersPaginator",
    "ListContainerInstancesPaginator",
    "ListServicesByNamespacePaginator",
    "ListServicesPaginator",
    "ListTaskDefinitionFamiliesPaginator",
    "ListTaskDefinitionsPaginator",
    "ListTasksPaginator",
)

if TYPE_CHECKING:
    _ListAccountSettingsPaginatorBase = Paginator[ListAccountSettingsResponseTypeDef]
else:
    _ListAccountSettingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAccountSettingsPaginator(_ListAccountSettingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListAccountSettings.html#ECS.Paginator.ListAccountSettings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listaccountsettingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAccountSettingsRequestPaginateTypeDef]
    ) -> PageIterator[ListAccountSettingsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListAccountSettings.html#ECS.Paginator.ListAccountSettings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listaccountsettingspaginator)
        """

if TYPE_CHECKING:
    _ListAttributesPaginatorBase = Paginator[ListAttributesResponseTypeDef]
else:
    _ListAttributesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAttributesPaginator(_ListAttributesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListAttributes.html#ECS.Paginator.ListAttributes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listattributespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAttributesRequestPaginateTypeDef]
    ) -> PageIterator[ListAttributesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListAttributes.html#ECS.Paginator.ListAttributes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listattributespaginator)
        """

if TYPE_CHECKING:
    _ListClustersPaginatorBase = Paginator[ListClustersResponseTypeDef]
else:
    _ListClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListClustersPaginator(_ListClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListClusters.html#ECS.Paginator.ListClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListClustersRequestPaginateTypeDef]
    ) -> PageIterator[ListClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListClusters.html#ECS.Paginator.ListClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listclusterspaginator)
        """

if TYPE_CHECKING:
    _ListContainerInstancesPaginatorBase = Paginator[ListContainerInstancesResponseTypeDef]
else:
    _ListContainerInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class ListContainerInstancesPaginator(_ListContainerInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListContainerInstances.html#ECS.Paginator.ListContainerInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listcontainerinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListContainerInstancesRequestPaginateTypeDef]
    ) -> PageIterator[ListContainerInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListContainerInstances.html#ECS.Paginator.ListContainerInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listcontainerinstancespaginator)
        """

if TYPE_CHECKING:
    _ListServicesByNamespacePaginatorBase = Paginator[ListServicesByNamespaceResponseTypeDef]
else:
    _ListServicesByNamespacePaginatorBase = Paginator  # type: ignore[assignment]

class ListServicesByNamespacePaginator(_ListServicesByNamespacePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListServicesByNamespace.html#ECS.Paginator.ListServicesByNamespace)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listservicesbynamespacepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicesByNamespaceRequestPaginateTypeDef]
    ) -> PageIterator[ListServicesByNamespaceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListServicesByNamespace.html#ECS.Paginator.ListServicesByNamespace.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listservicesbynamespacepaginator)
        """

if TYPE_CHECKING:
    _ListServicesPaginatorBase = Paginator[ListServicesResponseTypeDef]
else:
    _ListServicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListServicesPaginator(_ListServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListServices.html#ECS.Paginator.ListServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServicesRequestPaginateTypeDef]
    ) -> PageIterator[ListServicesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListServices.html#ECS.Paginator.ListServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listservicespaginator)
        """

if TYPE_CHECKING:
    _ListTaskDefinitionFamiliesPaginatorBase = Paginator[ListTaskDefinitionFamiliesResponseTypeDef]
else:
    _ListTaskDefinitionFamiliesPaginatorBase = Paginator  # type: ignore[assignment]

class ListTaskDefinitionFamiliesPaginator(_ListTaskDefinitionFamiliesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListTaskDefinitionFamilies.html#ECS.Paginator.ListTaskDefinitionFamilies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listtaskdefinitionfamiliespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTaskDefinitionFamiliesRequestPaginateTypeDef]
    ) -> PageIterator[ListTaskDefinitionFamiliesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListTaskDefinitionFamilies.html#ECS.Paginator.ListTaskDefinitionFamilies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listtaskdefinitionfamiliespaginator)
        """

if TYPE_CHECKING:
    _ListTaskDefinitionsPaginatorBase = Paginator[ListTaskDefinitionsResponseTypeDef]
else:
    _ListTaskDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListTaskDefinitionsPaginator(_ListTaskDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListTaskDefinitions.html#ECS.Paginator.ListTaskDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listtaskdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTaskDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListTaskDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListTaskDefinitions.html#ECS.Paginator.ListTaskDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listtaskdefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListTasksPaginatorBase = Paginator[ListTasksResponseTypeDef]
else:
    _ListTasksPaginatorBase = Paginator  # type: ignore[assignment]

class ListTasksPaginator(_ListTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListTasks.html#ECS.Paginator.ListTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listtaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListTasksRequestPaginateTypeDef]
    ) -> PageIterator[ListTasksResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs/paginator/ListTasks.html#ECS.Paginator.ListTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators/#listtaskspaginator)
        """
