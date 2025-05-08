"""
Type annotations for forecast service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_forecast.client import ForecastServiceClient
    from mypy_boto3_forecast.paginator import (
        ListDatasetGroupsPaginator,
        ListDatasetImportJobsPaginator,
        ListDatasetsPaginator,
        ListExplainabilitiesPaginator,
        ListExplainabilityExportsPaginator,
        ListForecastExportJobsPaginator,
        ListForecastsPaginator,
        ListMonitorEvaluationsPaginator,
        ListMonitorsPaginator,
        ListPredictorBacktestExportJobsPaginator,
        ListPredictorsPaginator,
        ListWhatIfAnalysesPaginator,
        ListWhatIfForecastExportsPaginator,
        ListWhatIfForecastsPaginator,
    )

    session = Session()
    client: ForecastServiceClient = session.client("forecast")

    list_dataset_groups_paginator: ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
    list_dataset_import_jobs_paginator: ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_explainabilities_paginator: ListExplainabilitiesPaginator = client.get_paginator("list_explainabilities")
    list_explainability_exports_paginator: ListExplainabilityExportsPaginator = client.get_paginator("list_explainability_exports")
    list_forecast_export_jobs_paginator: ListForecastExportJobsPaginator = client.get_paginator("list_forecast_export_jobs")
    list_forecasts_paginator: ListForecastsPaginator = client.get_paginator("list_forecasts")
    list_monitor_evaluations_paginator: ListMonitorEvaluationsPaginator = client.get_paginator("list_monitor_evaluations")
    list_monitors_paginator: ListMonitorsPaginator = client.get_paginator("list_monitors")
    list_predictor_backtest_export_jobs_paginator: ListPredictorBacktestExportJobsPaginator = client.get_paginator("list_predictor_backtest_export_jobs")
    list_predictors_paginator: ListPredictorsPaginator = client.get_paginator("list_predictors")
    list_what_if_analyses_paginator: ListWhatIfAnalysesPaginator = client.get_paginator("list_what_if_analyses")
    list_what_if_forecast_exports_paginator: ListWhatIfForecastExportsPaginator = client.get_paginator("list_what_if_forecast_exports")
    list_what_if_forecasts_paginator: ListWhatIfForecastsPaginator = client.get_paginator("list_what_if_forecasts")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListDatasetGroupsRequestPaginateTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsRequestPaginateTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsRequestPaginateTypeDef,
    ListDatasetsResponseTypeDef,
    ListExplainabilitiesRequestPaginateTypeDef,
    ListExplainabilitiesResponseTypeDef,
    ListExplainabilityExportsRequestPaginateTypeDef,
    ListExplainabilityExportsResponseTypeDef,
    ListForecastExportJobsRequestPaginateTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsRequestPaginateTypeDef,
    ListForecastsResponseTypeDef,
    ListMonitorEvaluationsRequestPaginateTypeDef,
    ListMonitorEvaluationsResponseTypeDef,
    ListMonitorsRequestPaginateTypeDef,
    ListMonitorsResponseTypeDef,
    ListPredictorBacktestExportJobsRequestPaginateTypeDef,
    ListPredictorBacktestExportJobsResponseTypeDef,
    ListPredictorsRequestPaginateTypeDef,
    ListPredictorsResponseTypeDef,
    ListWhatIfAnalysesRequestPaginateTypeDef,
    ListWhatIfAnalysesResponseTypeDef,
    ListWhatIfForecastExportsRequestPaginateTypeDef,
    ListWhatIfForecastExportsResponseTypeDef,
    ListWhatIfForecastsRequestPaginateTypeDef,
    ListWhatIfForecastsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListExplainabilitiesPaginator",
    "ListExplainabilityExportsPaginator",
    "ListForecastExportJobsPaginator",
    "ListForecastsPaginator",
    "ListMonitorEvaluationsPaginator",
    "ListMonitorsPaginator",
    "ListPredictorBacktestExportJobsPaginator",
    "ListPredictorsPaginator",
    "ListWhatIfAnalysesPaginator",
    "ListWhatIfForecastExportsPaginator",
    "ListWhatIfForecastsPaginator",
)

if TYPE_CHECKING:
    _ListDatasetGroupsPaginatorBase = Paginator[ListDatasetGroupsResponseTypeDef]
else:
    _ListDatasetGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetGroupsPaginator(_ListDatasetGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListDatasetGroups.html#ForecastService.Paginator.ListDatasetGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listdatasetgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListDatasetGroups.html#ForecastService.Paginator.ListDatasetGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listdatasetgroupspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetImportJobsPaginatorBase = Paginator[ListDatasetImportJobsResponseTypeDef]
else:
    _ListDatasetImportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetImportJobsPaginator(_ListDatasetImportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListDatasetImportJobs.html#ForecastService.Paginator.ListDatasetImportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listdatasetimportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetImportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetImportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListDatasetImportJobs.html#ForecastService.Paginator.ListDatasetImportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listdatasetimportjobspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetsPaginatorBase = Paginator[ListDatasetsResponseTypeDef]
else:
    _ListDatasetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetsPaginator(_ListDatasetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListDatasets.html#ForecastService.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListDatasets.html#ForecastService.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listdatasetspaginator)
        """

if TYPE_CHECKING:
    _ListExplainabilitiesPaginatorBase = Paginator[ListExplainabilitiesResponseTypeDef]
else:
    _ListExplainabilitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListExplainabilitiesPaginator(_ListExplainabilitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListExplainabilities.html#ForecastService.Paginator.ListExplainabilities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listexplainabilitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExplainabilitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListExplainabilitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListExplainabilities.html#ForecastService.Paginator.ListExplainabilities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listexplainabilitiespaginator)
        """

if TYPE_CHECKING:
    _ListExplainabilityExportsPaginatorBase = Paginator[ListExplainabilityExportsResponseTypeDef]
else:
    _ListExplainabilityExportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListExplainabilityExportsPaginator(_ListExplainabilityExportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListExplainabilityExports.html#ForecastService.Paginator.ListExplainabilityExports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listexplainabilityexportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListExplainabilityExportsRequestPaginateTypeDef]
    ) -> PageIterator[ListExplainabilityExportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListExplainabilityExports.html#ForecastService.Paginator.ListExplainabilityExports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listexplainabilityexportspaginator)
        """

if TYPE_CHECKING:
    _ListForecastExportJobsPaginatorBase = Paginator[ListForecastExportJobsResponseTypeDef]
else:
    _ListForecastExportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListForecastExportJobsPaginator(_ListForecastExportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListForecastExportJobs.html#ForecastService.Paginator.ListForecastExportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listforecastexportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListForecastExportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListForecastExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListForecastExportJobs.html#ForecastService.Paginator.ListForecastExportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listforecastexportjobspaginator)
        """

if TYPE_CHECKING:
    _ListForecastsPaginatorBase = Paginator[ListForecastsResponseTypeDef]
else:
    _ListForecastsPaginatorBase = Paginator  # type: ignore[assignment]

class ListForecastsPaginator(_ListForecastsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListForecasts.html#ForecastService.Paginator.ListForecasts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listforecastspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListForecastsRequestPaginateTypeDef]
    ) -> PageIterator[ListForecastsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListForecasts.html#ForecastService.Paginator.ListForecasts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listforecastspaginator)
        """

if TYPE_CHECKING:
    _ListMonitorEvaluationsPaginatorBase = Paginator[ListMonitorEvaluationsResponseTypeDef]
else:
    _ListMonitorEvaluationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMonitorEvaluationsPaginator(_ListMonitorEvaluationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListMonitorEvaluations.html#ForecastService.Paginator.ListMonitorEvaluations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listmonitorevaluationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMonitorEvaluationsRequestPaginateTypeDef]
    ) -> PageIterator[ListMonitorEvaluationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListMonitorEvaluations.html#ForecastService.Paginator.ListMonitorEvaluations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listmonitorevaluationspaginator)
        """

if TYPE_CHECKING:
    _ListMonitorsPaginatorBase = Paginator[ListMonitorsResponseTypeDef]
else:
    _ListMonitorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMonitorsPaginator(_ListMonitorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListMonitors.html#ForecastService.Paginator.ListMonitors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listmonitorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMonitorsRequestPaginateTypeDef]
    ) -> PageIterator[ListMonitorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListMonitors.html#ForecastService.Paginator.ListMonitors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listmonitorspaginator)
        """

if TYPE_CHECKING:
    _ListPredictorBacktestExportJobsPaginatorBase = Paginator[
        ListPredictorBacktestExportJobsResponseTypeDef
    ]
else:
    _ListPredictorBacktestExportJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPredictorBacktestExportJobsPaginator(_ListPredictorBacktestExportJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListPredictorBacktestExportJobs.html#ForecastService.Paginator.ListPredictorBacktestExportJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listpredictorbacktestexportjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPredictorBacktestExportJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListPredictorBacktestExportJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListPredictorBacktestExportJobs.html#ForecastService.Paginator.ListPredictorBacktestExportJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listpredictorbacktestexportjobspaginator)
        """

if TYPE_CHECKING:
    _ListPredictorsPaginatorBase = Paginator[ListPredictorsResponseTypeDef]
else:
    _ListPredictorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPredictorsPaginator(_ListPredictorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListPredictors.html#ForecastService.Paginator.ListPredictors)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listpredictorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPredictorsRequestPaginateTypeDef]
    ) -> PageIterator[ListPredictorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListPredictors.html#ForecastService.Paginator.ListPredictors.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listpredictorspaginator)
        """

if TYPE_CHECKING:
    _ListWhatIfAnalysesPaginatorBase = Paginator[ListWhatIfAnalysesResponseTypeDef]
else:
    _ListWhatIfAnalysesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWhatIfAnalysesPaginator(_ListWhatIfAnalysesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListWhatIfAnalyses.html#ForecastService.Paginator.ListWhatIfAnalyses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listwhatifanalysespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWhatIfAnalysesRequestPaginateTypeDef]
    ) -> PageIterator[ListWhatIfAnalysesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListWhatIfAnalyses.html#ForecastService.Paginator.ListWhatIfAnalyses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listwhatifanalysespaginator)
        """

if TYPE_CHECKING:
    _ListWhatIfForecastExportsPaginatorBase = Paginator[ListWhatIfForecastExportsResponseTypeDef]
else:
    _ListWhatIfForecastExportsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWhatIfForecastExportsPaginator(_ListWhatIfForecastExportsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListWhatIfForecastExports.html#ForecastService.Paginator.ListWhatIfForecastExports)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listwhatifforecastexportspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWhatIfForecastExportsRequestPaginateTypeDef]
    ) -> PageIterator[ListWhatIfForecastExportsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListWhatIfForecastExports.html#ForecastService.Paginator.ListWhatIfForecastExports.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listwhatifforecastexportspaginator)
        """

if TYPE_CHECKING:
    _ListWhatIfForecastsPaginatorBase = Paginator[ListWhatIfForecastsResponseTypeDef]
else:
    _ListWhatIfForecastsPaginatorBase = Paginator  # type: ignore[assignment]

class ListWhatIfForecastsPaginator(_ListWhatIfForecastsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListWhatIfForecasts.html#ForecastService.Paginator.ListWhatIfForecasts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listwhatifforecastspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWhatIfForecastsRequestPaginateTypeDef]
    ) -> PageIterator[ListWhatIfForecastsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/paginator/ListWhatIfForecasts.html#ForecastService.Paginator.ListWhatIfForecasts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/paginators/#listwhatifforecastspaginator)
        """
