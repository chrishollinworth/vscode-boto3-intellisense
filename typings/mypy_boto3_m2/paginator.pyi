"""
Type annotations for m2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_m2 import MainframeModernizationClient
    from mypy_boto3_m2.paginator import (
        ListApplicationVersionsPaginator,
        ListApplicationsPaginator,
        ListBatchJobDefinitionsPaginator,
        ListBatchJobExecutionsPaginator,
        ListDataSetImportHistoryPaginator,
        ListDataSetsPaginator,
        ListDeploymentsPaginator,
        ListEngineVersionsPaginator,
        ListEnvironmentsPaginator,
    )

    client: MainframeModernizationClient = boto3.client("m2")

    list_application_versions_paginator: ListApplicationVersionsPaginator = client.get_paginator("list_application_versions")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_batch_job_definitions_paginator: ListBatchJobDefinitionsPaginator = client.get_paginator("list_batch_job_definitions")
    list_batch_job_executions_paginator: ListBatchJobExecutionsPaginator = client.get_paginator("list_batch_job_executions")
    list_data_set_import_history_paginator: ListDataSetImportHistoryPaginator = client.get_paginator("list_data_set_import_history")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_engine_versions_paginator: ListEngineVersionsPaginator = client.get_paginator("list_engine_versions")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import BatchJobExecutionStatusType, EngineTypeType
from .type_defs import (
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListBatchJobDefinitionsResponseTypeDef,
    ListBatchJobExecutionsResponseTypeDef,
    ListDataSetImportHistoryResponseTypeDef,
    ListDataSetsResponseTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEngineVersionsResponseTypeDef,
    ListEnvironmentsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
    "ListBatchJobDefinitionsPaginator",
    "ListBatchJobExecutionsPaginator",
    "ListDataSetImportHistoryPaginator",
    "ListDataSetsPaginator",
    "ListDeploymentsPaginator",
    "ListEngineVersionsPaginator",
    "ListEnvironmentsPaginator",
)

class ListApplicationVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListApplicationVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listapplicationversionspaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListApplicationVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listapplicationversionspaginator)
        """

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self,
        *,
        environmentId: str = None,
        names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listapplicationspaginator)
        """

class ListBatchJobDefinitionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobDefinitions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listbatchjobdefinitionspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        prefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBatchJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobDefinitions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listbatchjobdefinitionspaginator)
        """

class ListBatchJobExecutionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobExecutions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listbatchjobexecutionspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        executionIds: List[str] = None,
        jobName: str = None,
        startedAfter: Union[datetime, str] = None,
        startedBefore: Union[datetime, str] = None,
        status: BatchJobExecutionStatusType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBatchJobExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListBatchJobExecutions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listbatchjobexecutionspaginator)
        """

class ListDataSetImportHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListDataSetImportHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdatasetimporthistorypaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSetImportHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListDataSetImportHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdatasetimporthistorypaginator)
        """

class ListDataSetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListDataSets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdatasetspaginator)
    """

    def paginate(
        self,
        *,
        applicationId: str,
        prefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListDataSets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdatasetspaginator)
        """

class ListDeploymentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdeploymentspaginator)
    """

    def paginate(
        self, *, applicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listdeploymentspaginator)
        """

class ListEngineVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListEngineVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listengineversionspaginator)
    """

    def paginate(
        self, *, engineType: EngineTypeType = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEngineVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListEngineVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listengineversionspaginator)
        """

class ListEnvironmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listenvironmentspaginator)
    """

    def paginate(
        self,
        *,
        engineType: EngineTypeType = None,
        names: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/m2.html#MainframeModernization.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators.html#listenvironmentspaginator)
        """
