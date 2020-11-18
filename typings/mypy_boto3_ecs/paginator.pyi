# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for ecs service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_ecs import ECSClient
    from mypy_boto3_ecs.paginator import (
        ListAccountSettingsPaginator,
        ListAttributesPaginator,
        ListClustersPaginator,
        ListContainerInstancesPaginator,
        ListServicesPaginator,
        ListTaskDefinitionFamiliesPaginator,
        ListTaskDefinitionsPaginator,
        ListTasksPaginator,
    )

    client: ECSClient = boto3.client("ecs")

    list_account_settings_paginator: ListAccountSettingsPaginator = client.get_paginator("list_account_settings")
    list_attributes_paginator: ListAttributesPaginator = client.get_paginator("list_attributes")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_container_instances_paginator: ListContainerInstancesPaginator = client.get_paginator("list_container_instances")
    list_services_paginator: ListServicesPaginator = client.get_paginator("list_services")
    list_task_definition_families_paginator: ListTaskDefinitionFamiliesPaginator = client.get_paginator("list_task_definition_families")
    list_task_definitions_paginator: ListTaskDefinitionsPaginator = client.get_paginator("list_task_definitions")
    list_tasks_paginator: ListTasksPaginator = client.get_paginator("list_tasks")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_ecs.type_defs import (
    ListAccountSettingsResponseTypeDef,
    ListAttributesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListContainerInstancesResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTaskDefinitionFamiliesResponseTypeDef,
    ListTaskDefinitionsResponseTypeDef,
    ListTasksResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListAccountSettingsPaginator",
    "ListAttributesPaginator",
    "ListClustersPaginator",
    "ListContainerInstancesPaginator",
    "ListServicesPaginator",
    "ListTaskDefinitionFamiliesPaginator",
    "ListTaskDefinitionsPaginator",
    "ListTasksPaginator",
)


class ListAccountSettingsPaginator(Boto3Paginator):
    """
    [Paginator.ListAccountSettings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListAccountSettings)
    """

    def paginate(
        self,
        name: Literal[
            "serviceLongArnFormat",
            "taskLongArnFormat",
            "containerInstanceLongArnFormat",
            "awsvpcTrunking",
            "containerInsights",
        ] = None,
        value: str = None,
        principalArn: str = None,
        effectiveSettings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAccountSettingsResponseTypeDef]:
        """
        [ListAccountSettings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListAccountSettings.paginate)
        """


class ListAttributesPaginator(Boto3Paginator):
    """
    [Paginator.ListAttributes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListAttributes)
    """

    def paginate(
        self,
        targetType: Literal["container-instance"],
        cluster: str = None,
        attributeName: str = None,
        attributeValue: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAttributesResponseTypeDef]:
        """
        [ListAttributes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListAttributes.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListClusters)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListClustersResponseTypeDef]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListClusters.paginate)
        """


class ListContainerInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListContainerInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListContainerInstances)
    """

    def paginate(
        self,
        cluster: str = None,
        filter: str = None,
        status: Literal[
            "ACTIVE", "DRAINING", "REGISTERING", "DEREGISTERING", "REGISTRATION_FAILED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListContainerInstancesResponseTypeDef]:
        """
        [ListContainerInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListContainerInstances.paginate)
        """


class ListServicesPaginator(Boto3Paginator):
    """
    [Paginator.ListServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListServices)
    """

    def paginate(
        self,
        cluster: str = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        schedulingStrategy: Literal["REPLICA", "DAEMON"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListServicesResponseTypeDef]:
        """
        [ListServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListServices.paginate)
        """


class ListTaskDefinitionFamiliesPaginator(Boto3Paginator):
    """
    [Paginator.ListTaskDefinitionFamilies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies)
    """

    def paginate(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE", "ALL"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTaskDefinitionFamiliesResponseTypeDef]:
        """
        [ListTaskDefinitionFamilies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies.paginate)
        """


class ListTaskDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListTaskDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions)
    """

    def paginate(
        self,
        familyPrefix: str = None,
        status: Literal["ACTIVE", "INACTIVE"] = None,
        sort: Literal["ASC", "DESC"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTaskDefinitionsResponseTypeDef]:
        """
        [ListTaskDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions.paginate)
        """


class ListTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTasks)
    """

    def paginate(
        self,
        cluster: str = None,
        containerInstance: str = None,
        family: str = None,
        startedBy: str = None,
        serviceName: str = None,
        desiredStatus: Literal["RUNNING", "PENDING", "STOPPED"] = None,
        launchType: Literal["EC2", "FARGATE"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTasksResponseTypeDef]:
        """
        [ListTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ecs.html#ECS.Paginator.ListTasks.paginate)
        """
