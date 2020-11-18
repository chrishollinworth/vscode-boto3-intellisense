# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for robomaker service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_robomaker import RoboMakerClient
    from mypy_boto3_robomaker.paginator import (
        ListDeploymentJobsPaginator,
        ListFleetsPaginator,
        ListRobotApplicationsPaginator,
        ListRobotsPaginator,
        ListSimulationApplicationsPaginator,
        ListSimulationJobBatchesPaginator,
        ListSimulationJobsPaginator,
        ListWorldExportJobsPaginator,
        ListWorldGenerationJobsPaginator,
        ListWorldTemplatesPaginator,
        ListWorldsPaginator,
    )

    client: RoboMakerClient = boto3.client("robomaker")

    list_deployment_jobs_paginator: ListDeploymentJobsPaginator = client.get_paginator("list_deployment_jobs")
    list_fleets_paginator: ListFleetsPaginator = client.get_paginator("list_fleets")
    list_robot_applications_paginator: ListRobotApplicationsPaginator = client.get_paginator("list_robot_applications")
    list_robots_paginator: ListRobotsPaginator = client.get_paginator("list_robots")
    list_simulation_applications_paginator: ListSimulationApplicationsPaginator = client.get_paginator("list_simulation_applications")
    list_simulation_job_batches_paginator: ListSimulationJobBatchesPaginator = client.get_paginator("list_simulation_job_batches")
    list_simulation_jobs_paginator: ListSimulationJobsPaginator = client.get_paginator("list_simulation_jobs")
    list_world_export_jobs_paginator: ListWorldExportJobsPaginator = client.get_paginator("list_world_export_jobs")
    list_world_generation_jobs_paginator: ListWorldGenerationJobsPaginator = client.get_paginator("list_world_generation_jobs")
    list_world_templates_paginator: ListWorldTemplatesPaginator = client.get_paginator("list_world_templates")
    list_worlds_paginator: ListWorldsPaginator = client.get_paginator("list_worlds")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_robomaker.type_defs import (
    FilterTypeDef,
    ListDeploymentJobsResponseTypeDef,
    ListFleetsResponseTypeDef,
    ListRobotApplicationsResponseTypeDef,
    ListRobotsResponseTypeDef,
    ListSimulationApplicationsResponseTypeDef,
    ListSimulationJobBatchesResponseTypeDef,
    ListSimulationJobsResponseTypeDef,
    ListWorldExportJobsResponseTypeDef,
    ListWorldGenerationJobsResponseTypeDef,
    ListWorldsResponseTypeDef,
    ListWorldTemplatesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDeploymentJobsPaginator",
    "ListFleetsPaginator",
    "ListRobotApplicationsPaginator",
    "ListRobotsPaginator",
    "ListSimulationApplicationsPaginator",
    "ListSimulationJobBatchesPaginator",
    "ListSimulationJobsPaginator",
    "ListWorldExportJobsPaginator",
    "ListWorldGenerationJobsPaginator",
    "ListWorldTemplatesPaginator",
    "ListWorldsPaginator",
)


class ListDeploymentJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeploymentJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs)
    """

    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentJobsResponseTypeDef]:
        """
        [ListDeploymentJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListDeploymentJobs.paginate)
        """


class ListFleetsPaginator(Boto3Paginator):
    """
    [Paginator.ListFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets)
    """

    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListFleetsResponseTypeDef]:
        """
        [ListFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListFleets.paginate)
        """


class ListRobotApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListRobotApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications)
    """

    def paginate(
        self,
        versionQualifier: str = None,
        filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRobotApplicationsResponseTypeDef]:
        """
        [ListRobotApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListRobotApplications.paginate)
        """


class ListRobotsPaginator(Boto3Paginator):
    """
    [Paginator.ListRobots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots)
    """

    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRobotsResponseTypeDef]:
        """
        [ListRobots.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListRobots.paginate)
        """


class ListSimulationApplicationsPaginator(Boto3Paginator):
    """
    [Paginator.ListSimulationApplications documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications)
    """

    def paginate(
        self,
        versionQualifier: str = None,
        filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListSimulationApplicationsResponseTypeDef]:
        """
        [ListSimulationApplications.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationApplications.paginate)
        """


class ListSimulationJobBatchesPaginator(Boto3Paginator):
    """
    [Paginator.ListSimulationJobBatches documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobBatches)
    """

    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSimulationJobBatchesResponseTypeDef]:
        """
        [ListSimulationJobBatches.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobBatches.paginate)
        """


class ListSimulationJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListSimulationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs)
    """

    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSimulationJobsResponseTypeDef]:
        """
        [ListSimulationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListSimulationJobs.paginate)
        """


class ListWorldExportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListWorldExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldExportJobs)
    """

    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorldExportJobsResponseTypeDef]:
        """
        [ListWorldExportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldExportJobs.paginate)
        """


class ListWorldGenerationJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListWorldGenerationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldGenerationJobs)
    """

    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorldGenerationJobsResponseTypeDef]:
        """
        [ListWorldGenerationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldGenerationJobs.paginate)
        """


class ListWorldTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListWorldTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldTemplates)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorldTemplatesResponseTypeDef]:
        """
        [ListWorldTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorldTemplates.paginate)
        """


class ListWorldsPaginator(Boto3Paginator):
    """
    [Paginator.ListWorlds documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorlds)
    """

    def paginate(
        self, filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListWorldsResponseTypeDef]:
        """
        [ListWorlds.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/robomaker.html#RoboMaker.Paginator.ListWorlds.paginate)
        """
