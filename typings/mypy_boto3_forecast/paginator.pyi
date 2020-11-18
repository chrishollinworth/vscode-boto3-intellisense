# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for forecast service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_forecast import ForecastServiceClient
    from mypy_boto3_forecast.paginator import (
        ListDatasetGroupsPaginator,
        ListDatasetImportJobsPaginator,
        ListDatasetsPaginator,
        ListForecastExportJobsPaginator,
        ListForecastsPaginator,
        ListPredictorsPaginator,
    )

    client: ForecastServiceClient = boto3.client("forecast")

    list_dataset_groups_paginator: ListDatasetGroupsPaginator = client.get_paginator("list_dataset_groups")
    list_dataset_import_jobs_paginator: ListDatasetImportJobsPaginator = client.get_paginator("list_dataset_import_jobs")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_forecast_export_jobs_paginator: ListForecastExportJobsPaginator = client.get_paginator("list_forecast_export_jobs")
    list_forecasts_paginator: ListForecastsPaginator = client.get_paginator("list_forecasts")
    list_predictors_paginator: ListPredictorsPaginator = client.get_paginator("list_predictors")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_forecast.type_defs import (
    FilterTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsResponseTypeDef,
    ListPredictorsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListForecastExportJobsPaginator",
    "ListForecastsPaginator",
    "ListPredictorsPaginator",
)


class ListDatasetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetGroupsResponseTypeDef]:
        """
        [ListDatasetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups.paginate)
        """


class ListDatasetImportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetImportJobsResponseTypeDef]:
        """
        [ListDatasetImportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs.paginate)
        """


class ListDatasetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListDatasets.paginate)
        """


class ListForecastExportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListForecastExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListForecastExportJobsResponseTypeDef]:
        """
        [ListForecastExportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs.paginate)
        """


class ListForecastsPaginator(Boto3Paginator):
    """
    [Paginator.ListForecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListForecastsResponseTypeDef]:
        """
        [ListForecasts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListForecasts.paginate)
        """


class ListPredictorsPaginator(Boto3Paginator):
    """
    [Paginator.ListPredictors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)
    """

    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPredictorsResponseTypeDef]:
        """
        [ListPredictors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/forecast.html#ForecastService.Paginator.ListPredictors.paginate)
        """
