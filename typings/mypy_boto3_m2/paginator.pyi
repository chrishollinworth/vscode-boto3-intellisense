"""
Type annotations for m2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_m2.client import MainframeModernizationClient
    from mypy_boto3_m2.paginator import (
        ListApplicationVersionsPaginator,
        ListApplicationsPaginator,
        ListBatchJobDefinitionsPaginator,
        ListBatchJobExecutionsPaginator,
        ListDataSetExportHistoryPaginator,
        ListDataSetImportHistoryPaginator,
        ListDataSetsPaginator,
        ListDeploymentsPaginator,
        ListEngineVersionsPaginator,
        ListEnvironmentsPaginator,
    )

    session = Session()
    client: MainframeModernizationClient = session.client("m2")

    list_application_versions_paginator: ListApplicationVersionsPaginator = client.get_paginator("list_application_versions")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_batch_job_definitions_paginator: ListBatchJobDefinitionsPaginator = client.get_paginator("list_batch_job_definitions")
    list_batch_job_executions_paginator: ListBatchJobExecutionsPaginator = client.get_paginator("list_batch_job_executions")
    list_data_set_export_history_paginator: ListDataSetExportHistoryPaginator = client.get_paginator("list_data_set_export_history")
    list_data_set_import_history_paginator: ListDataSetImportHistoryPaginator = client.get_paginator("list_data_set_import_history")
    list_data_sets_paginator: ListDataSetsPaginator = client.get_paginator("list_data_sets")
    list_deployments_paginator: ListDeploymentsPaginator = client.get_paginator("list_deployments")
    list_engine_versions_paginator: ListEngineVersionsPaginator = client.get_paginator("list_engine_versions")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationsRequestPaginateTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsRequestPaginateTypeDef,
    ListApplicationVersionsResponseTypeDef,
    ListBatchJobDefinitionsRequestPaginateTypeDef,
    ListBatchJobDefinitionsResponseTypeDef,
    ListBatchJobExecutionsRequestPaginateTypeDef,
    ListBatchJobExecutionsResponseTypeDef,
    ListDataSetExportHistoryRequestPaginateTypeDef,
    ListDataSetExportHistoryResponseTypeDef,
    ListDataSetImportHistoryRequestPaginateTypeDef,
    ListDataSetImportHistoryResponseTypeDef,
    ListDataSetsRequestPaginateTypeDef,
    ListDataSetsResponseTypeDef,
    ListDeploymentsRequestPaginateTypeDef,
    ListDeploymentsResponseTypeDef,
    ListEngineVersionsRequestPaginateTypeDef,
    ListEngineVersionsResponseTypeDef,
    ListEnvironmentsRequestPaginateTypeDef,
    ListEnvironmentsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
    "ListBatchJobDefinitionsPaginator",
    "ListBatchJobExecutionsPaginator",
    "ListDataSetExportHistoryPaginator",
    "ListDataSetImportHistoryPaginator",
    "ListDataSetsPaginator",
    "ListDeploymentsPaginator",
    "ListEngineVersionsPaginator",
    "ListEnvironmentsPaginator",
)

if TYPE_CHECKING:
    _ListApplicationVersionsPaginatorBase = Paginator[ListApplicationVersionsResponseTypeDef]
else:
    _ListApplicationVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationVersionsPaginator(_ListApplicationVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListApplicationVersions.html#MainframeModernization.Paginator.ListApplicationVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listapplicationversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListApplicationVersions.html#MainframeModernization.Paginator.ListApplicationVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listapplicationversionspaginator)
        """

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListApplications.html#MainframeModernization.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListApplications.html#MainframeModernization.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listapplicationspaginator)
        """

if TYPE_CHECKING:
    _ListBatchJobDefinitionsPaginatorBase = Paginator[ListBatchJobDefinitionsResponseTypeDef]
else:
    _ListBatchJobDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBatchJobDefinitionsPaginator(_ListBatchJobDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListBatchJobDefinitions.html#MainframeModernization.Paginator.ListBatchJobDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listbatchjobdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBatchJobDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[ListBatchJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListBatchJobDefinitions.html#MainframeModernization.Paginator.ListBatchJobDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listbatchjobdefinitionspaginator)
        """

if TYPE_CHECKING:
    _ListBatchJobExecutionsPaginatorBase = Paginator[ListBatchJobExecutionsResponseTypeDef]
else:
    _ListBatchJobExecutionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListBatchJobExecutionsPaginator(_ListBatchJobExecutionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListBatchJobExecutions.html#MainframeModernization.Paginator.ListBatchJobExecutions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listbatchjobexecutionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBatchJobExecutionsRequestPaginateTypeDef]
    ) -> PageIterator[ListBatchJobExecutionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListBatchJobExecutions.html#MainframeModernization.Paginator.ListBatchJobExecutions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listbatchjobexecutionspaginator)
        """

if TYPE_CHECKING:
    _ListDataSetExportHistoryPaginatorBase = Paginator[ListDataSetExportHistoryResponseTypeDef]
else:
    _ListDataSetExportHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSetExportHistoryPaginator(_ListDataSetExportHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListDataSetExportHistory.html#MainframeModernization.Paginator.ListDataSetExportHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listdatasetexporthistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSetExportHistoryRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSetExportHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListDataSetExportHistory.html#MainframeModernization.Paginator.ListDataSetExportHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listdatasetexporthistorypaginator)
        """

if TYPE_CHECKING:
    _ListDataSetImportHistoryPaginatorBase = Paginator[ListDataSetImportHistoryResponseTypeDef]
else:
    _ListDataSetImportHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSetImportHistoryPaginator(_ListDataSetImportHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListDataSetImportHistory.html#MainframeModernization.Paginator.ListDataSetImportHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listdatasetimporthistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSetImportHistoryRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSetImportHistoryResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListDataSetImportHistory.html#MainframeModernization.Paginator.ListDataSetImportHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listdatasetimporthistorypaginator)
        """

if TYPE_CHECKING:
    _ListDataSetsPaginatorBase = Paginator[ListDataSetsResponseTypeDef]
else:
    _ListDataSetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDataSetsPaginator(_ListDataSetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListDataSets.html#MainframeModernization.Paginator.ListDataSets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDataSetsRequestPaginateTypeDef]
    ) -> PageIterator[ListDataSetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListDataSets.html#MainframeModernization.Paginator.ListDataSets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listdatasetspaginator)
        """

if TYPE_CHECKING:
    _ListDeploymentsPaginatorBase = Paginator[ListDeploymentsResponseTypeDef]
else:
    _ListDeploymentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDeploymentsPaginator(_ListDeploymentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListDeployments.html#MainframeModernization.Paginator.ListDeployments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listdeploymentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDeploymentsRequestPaginateTypeDef]
    ) -> PageIterator[ListDeploymentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListDeployments.html#MainframeModernization.Paginator.ListDeployments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listdeploymentspaginator)
        """

if TYPE_CHECKING:
    _ListEngineVersionsPaginatorBase = Paginator[ListEngineVersionsResponseTypeDef]
else:
    _ListEngineVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEngineVersionsPaginator(_ListEngineVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListEngineVersions.html#MainframeModernization.Paginator.ListEngineVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listengineversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEngineVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListEngineVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListEngineVersions.html#MainframeModernization.Paginator.ListEngineVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listengineversionspaginator)
        """

if TYPE_CHECKING:
    _ListEnvironmentsPaginatorBase = Paginator[ListEnvironmentsResponseTypeDef]
else:
    _ListEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEnvironmentsPaginator(_ListEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListEnvironments.html#MainframeModernization.Paginator.ListEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[ListEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/m2/paginator/ListEnvironments.html#MainframeModernization.Paginator.ListEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/paginators/#listenvironmentspaginator)
        """
