"""
Type annotations for robomaker service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_robomaker.client import RoboMakerClient
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

    session = Session()
    client: RoboMakerClient = session.client("robomaker")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDeploymentJobsRequestPaginateTypeDef,
    ListDeploymentJobsResponseTypeDef,
    ListFleetsRequestPaginateTypeDef,
    ListFleetsResponseTypeDef,
    ListRobotApplicationsRequestPaginateTypeDef,
    ListRobotApplicationsResponseTypeDef,
    ListRobotsRequestPaginateTypeDef,
    ListRobotsResponseTypeDef,
    ListSimulationApplicationsRequestPaginateTypeDef,
    ListSimulationApplicationsResponseTypeDef,
    ListSimulationJobBatchesRequestPaginateTypeDef,
    ListSimulationJobBatchesResponseTypeDef,
    ListSimulationJobsRequestPaginateTypeDef,
    ListSimulationJobsResponseTypeDef,
    ListWorldExportJobsRequestPaginateTypeDef,
    ListWorldExportJobsResponseTypeDef,
    ListWorldGenerationJobsRequestPaginateTypeDef,
    ListWorldGenerationJobsResponseTypeDef,
    ListWorldsRequestPaginateTypeDef,
    ListWorldsResponseTypeDef,
    ListWorldTemplatesRequestPaginateTypeDef,
    ListWorldTemplatesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

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

if TYPE_CHECKING:
    _ListDeploymentJobsPaginatorBase = Paginator[ListDeploymentJobsResponseTypeDef]
else:
    _ListDeploymentJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentJobsPaginator(_ListDeploymentJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListDeploymentJobs.html#RoboMaker.Paginator.ListDeploymentJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listdeploymentjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDeploymentJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListDeploymentJobs.html#RoboMaker.Paginator.ListDeploymentJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listdeploymentjobspaginator)
        """

if TYPE_CHECKING:
    _ListFleetsPaginatorBase = Paginator[ListFleetsResponseTypeDef]
else:
    _ListFleetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListFleetsPaginator(_ListFleetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListFleets.html#RoboMaker.Paginator.ListFleets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listfleetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListFleetsRequestPaginateTypeDef]
    ) -> PageIterator[ListFleetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListFleets.html#RoboMaker.Paginator.ListFleets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listfleetspaginator)
        """

if TYPE_CHECKING:
    _ListRobotApplicationsPaginatorBase = Paginator[ListRobotApplicationsResponseTypeDef]
else:
    _ListRobotApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRobotApplicationsPaginator(_ListRobotApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListRobotApplications.html#RoboMaker.Paginator.ListRobotApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listrobotapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRobotApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListRobotApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListRobotApplications.html#RoboMaker.Paginator.ListRobotApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listrobotapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListRobotsPaginatorBase = Paginator[ListRobotsResponseTypeDef]
else:
    _ListRobotsPaginatorBase = Paginator  # type: ignore[assignment]

class ListRobotsPaginator(_ListRobotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListRobots.html#RoboMaker.Paginator.ListRobots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listrobotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRobotsRequestPaginateTypeDef]
    ) -> PageIterator[ListRobotsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListRobots.html#RoboMaker.Paginator.ListRobots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listrobotspaginator)
        """

if TYPE_CHECKING:
    _ListSimulationApplicationsPaginatorBase = Paginator[ListSimulationApplicationsResponseTypeDef]
else:
    _ListSimulationApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSimulationApplicationsPaginator(_ListSimulationApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListSimulationApplications.html#RoboMaker.Paginator.ListSimulationApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listsimulationapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSimulationApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListSimulationApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListSimulationApplications.html#RoboMaker.Paginator.ListSimulationApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listsimulationapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListSimulationJobBatchesPaginatorBase = Paginator[ListSimulationJobBatchesResponseTypeDef]
else:
    _ListSimulationJobBatchesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSimulationJobBatchesPaginator(_ListSimulationJobBatchesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListSimulationJobBatches.html#RoboMaker.Paginator.ListSimulationJobBatches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listsimulationjobbatchespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSimulationJobBatchesRequestPaginateTypeDef]
    ) -> PageIterator[ListSimulationJobBatchesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListSimulationJobBatches.html#RoboMaker.Paginator.ListSimulationJobBatches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listsimulationjobbatchespaginator)
        """

if TYPE_CHECKING:
    _ListSimulationJobsPaginatorBase = Paginator[ListSimulationJobsResponseTypeDef]
else:
    _ListSimulationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSimulationJobsPaginator(_ListSimulationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListSimulationJobs.html#RoboMaker.Paginator.ListSimulationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listsimulationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSimulationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListSimulationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListSimulationJobs.html#RoboMaker.Paginator.ListSimulationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listsimulationjobspaginator)
        """

if TYPE_CHECKING:
    _ListWorldExportJobsPaginatorBase = Paginator[ListWorldExportJobsResponseTypeDef]
else:
    _ListWorldExportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorldExportJobsPaginator(_ListWorldExportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListWorldExportJobs.html#RoboMaker.Paginator.ListWorldExportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listworldexportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorldExportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorldExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListWorldExportJobs.html#RoboMaker.Paginator.ListWorldExportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listworldexportjobspaginator)
        """

if TYPE_CHECKING:
    _ListWorldGenerationJobsPaginatorBase = Paginator[ListWorldGenerationJobsResponseTypeDef]
else:
    _ListWorldGenerationJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorldGenerationJobsPaginator(_ListWorldGenerationJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListWorldGenerationJobs.html#RoboMaker.Paginator.ListWorldGenerationJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listworldgenerationjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorldGenerationJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorldGenerationJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListWorldGenerationJobs.html#RoboMaker.Paginator.ListWorldGenerationJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listworldgenerationjobspaginator)
        """

if TYPE_CHECKING:
    _ListWorldTemplatesPaginatorBase = Paginator[ListWorldTemplatesResponseTypeDef]
else:
    _ListWorldTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorldTemplatesPaginator(_ListWorldTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListWorldTemplates.html#RoboMaker.Paginator.ListWorldTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listworldtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorldTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListWorldTemplatesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListWorldTemplates.html#RoboMaker.Paginator.ListWorldTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listworldtemplatespaginator)
        """

if TYPE_CHECKING:
    _ListWorldsPaginatorBase = Paginator[ListWorldsResponseTypeDef]
else:
    _ListWorldsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorldsPaginator(_ListWorldsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListWorlds.html#RoboMaker.Paginator.ListWorlds)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listworldspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorldsRequestPaginateTypeDef]
    ) -> PageIterator[ListWorldsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/robomaker/paginator/ListWorlds.html#RoboMaker.Paginator.ListWorlds.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_robomaker/paginators/#listworldspaginator)
        """
