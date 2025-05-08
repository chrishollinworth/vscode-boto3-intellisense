"""
Type annotations for forecast service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_forecast.client import ForecastServiceClient

    session = Session()
    client: ForecastServiceClient = session.client("forecast")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
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
from .type_defs import (
    CreateAutoPredictorRequestTypeDef,
    CreateAutoPredictorResponseTypeDef,
    CreateDatasetGroupRequestTypeDef,
    CreateDatasetGroupResponseTypeDef,
    CreateDatasetImportJobRequestTypeDef,
    CreateDatasetImportJobResponseTypeDef,
    CreateDatasetRequestTypeDef,
    CreateDatasetResponseTypeDef,
    CreateExplainabilityExportRequestTypeDef,
    CreateExplainabilityExportResponseTypeDef,
    CreateExplainabilityRequestTypeDef,
    CreateExplainabilityResponseTypeDef,
    CreateForecastExportJobRequestTypeDef,
    CreateForecastExportJobResponseTypeDef,
    CreateForecastRequestTypeDef,
    CreateForecastResponseTypeDef,
    CreateMonitorRequestTypeDef,
    CreateMonitorResponseTypeDef,
    CreatePredictorBacktestExportJobRequestTypeDef,
    CreatePredictorBacktestExportJobResponseTypeDef,
    CreatePredictorRequestTypeDef,
    CreatePredictorResponseTypeDef,
    CreateWhatIfAnalysisRequestTypeDef,
    CreateWhatIfAnalysisResponseTypeDef,
    CreateWhatIfForecastExportRequestTypeDef,
    CreateWhatIfForecastExportResponseTypeDef,
    CreateWhatIfForecastRequestTypeDef,
    CreateWhatIfForecastResponseTypeDef,
    DeleteDatasetGroupRequestTypeDef,
    DeleteDatasetImportJobRequestTypeDef,
    DeleteDatasetRequestTypeDef,
    DeleteExplainabilityExportRequestTypeDef,
    DeleteExplainabilityRequestTypeDef,
    DeleteForecastExportJobRequestTypeDef,
    DeleteForecastRequestTypeDef,
    DeleteMonitorRequestTypeDef,
    DeletePredictorBacktestExportJobRequestTypeDef,
    DeletePredictorRequestTypeDef,
    DeleteResourceTreeRequestTypeDef,
    DeleteWhatIfAnalysisRequestTypeDef,
    DeleteWhatIfForecastExportRequestTypeDef,
    DeleteWhatIfForecastRequestTypeDef,
    DescribeAutoPredictorRequestTypeDef,
    DescribeAutoPredictorResponseTypeDef,
    DescribeDatasetGroupRequestTypeDef,
    DescribeDatasetGroupResponseTypeDef,
    DescribeDatasetImportJobRequestTypeDef,
    DescribeDatasetImportJobResponseTypeDef,
    DescribeDatasetRequestTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeExplainabilityExportRequestTypeDef,
    DescribeExplainabilityExportResponseTypeDef,
    DescribeExplainabilityRequestTypeDef,
    DescribeExplainabilityResponseTypeDef,
    DescribeForecastExportJobRequestTypeDef,
    DescribeForecastExportJobResponseTypeDef,
    DescribeForecastRequestTypeDef,
    DescribeForecastResponseTypeDef,
    DescribeMonitorRequestTypeDef,
    DescribeMonitorResponseTypeDef,
    DescribePredictorBacktestExportJobRequestTypeDef,
    DescribePredictorBacktestExportJobResponseTypeDef,
    DescribePredictorRequestTypeDef,
    DescribePredictorResponseTypeDef,
    DescribeWhatIfAnalysisRequestTypeDef,
    DescribeWhatIfAnalysisResponseTypeDef,
    DescribeWhatIfForecastExportRequestTypeDef,
    DescribeWhatIfForecastExportResponseTypeDef,
    DescribeWhatIfForecastRequestTypeDef,
    DescribeWhatIfForecastResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetAccuracyMetricsRequestTypeDef,
    GetAccuracyMetricsResponseTypeDef,
    ListDatasetGroupsRequestTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsRequestTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsRequestTypeDef,
    ListDatasetsResponseTypeDef,
    ListExplainabilitiesRequestTypeDef,
    ListExplainabilitiesResponseTypeDef,
    ListExplainabilityExportsRequestTypeDef,
    ListExplainabilityExportsResponseTypeDef,
    ListForecastExportJobsRequestTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsRequestTypeDef,
    ListForecastsResponseTypeDef,
    ListMonitorEvaluationsRequestTypeDef,
    ListMonitorEvaluationsResponseTypeDef,
    ListMonitorsRequestTypeDef,
    ListMonitorsResponseTypeDef,
    ListPredictorBacktestExportJobsRequestTypeDef,
    ListPredictorBacktestExportJobsResponseTypeDef,
    ListPredictorsRequestTypeDef,
    ListPredictorsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWhatIfAnalysesRequestTypeDef,
    ListWhatIfAnalysesResponseTypeDef,
    ListWhatIfForecastExportsRequestTypeDef,
    ListWhatIfForecastExportsResponseTypeDef,
    ListWhatIfForecastsRequestTypeDef,
    ListWhatIfForecastsResponseTypeDef,
    ResumeResourceRequestTypeDef,
    StopResourceRequestTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateDatasetGroupRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("ForecastServiceClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]

class ForecastServiceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ForecastServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast.html#ForecastService.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#generate_presigned_url)
        """

    def create_auto_predictor(
        self, **kwargs: Unpack[CreateAutoPredictorRequestTypeDef]
    ) -> CreateAutoPredictorResponseTypeDef:
        """
        Creates an Amazon Forecast predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_auto_predictor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_auto_predictor)
        """

    def create_dataset(
        self, **kwargs: Unpack[CreateDatasetRequestTypeDef]
    ) -> CreateDatasetResponseTypeDef:
        """
        Creates an Amazon Forecast dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_dataset)
        """

    def create_dataset_group(
        self, **kwargs: Unpack[CreateDatasetGroupRequestTypeDef]
    ) -> CreateDatasetGroupResponseTypeDef:
        """
        Creates a dataset group, which holds a collection of related datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_dataset_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_dataset_group)
        """

    def create_dataset_import_job(
        self, **kwargs: Unpack[CreateDatasetImportJobRequestTypeDef]
    ) -> CreateDatasetImportJobResponseTypeDef:
        """
        Imports your training data to an Amazon Forecast dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_dataset_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_dataset_import_job)
        """

    def create_explainability(
        self, **kwargs: Unpack[CreateExplainabilityRequestTypeDef]
    ) -> CreateExplainabilityResponseTypeDef:
        """
        Explainability is only available for Forecasts and Predictors generated from an
        AutoPredictor (<a>CreateAutoPredictor</a>).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_explainability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_explainability)
        """

    def create_explainability_export(
        self, **kwargs: Unpack[CreateExplainabilityExportRequestTypeDef]
    ) -> CreateExplainabilityExportResponseTypeDef:
        """
        Exports an Explainability resource created by the <a>CreateExplainability</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_explainability_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_explainability_export)
        """

    def create_forecast(
        self, **kwargs: Unpack[CreateForecastRequestTypeDef]
    ) -> CreateForecastResponseTypeDef:
        """
        Creates a forecast for each item in the <code>TARGET_TIME_SERIES</code> dataset
        that was used to train the predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_forecast)
        """

    def create_forecast_export_job(
        self, **kwargs: Unpack[CreateForecastExportJobRequestTypeDef]
    ) -> CreateForecastExportJobResponseTypeDef:
        """
        Exports a forecast created by the <a>CreateForecast</a> operation to your
        Amazon Simple Storage Service (Amazon S3) bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_forecast_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_forecast_export_job)
        """

    def create_monitor(
        self, **kwargs: Unpack[CreateMonitorRequestTypeDef]
    ) -> CreateMonitorResponseTypeDef:
        """
        Creates a predictor monitor resource for an existing auto predictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_monitor)
        """

    def create_predictor(
        self, **kwargs: Unpack[CreatePredictorRequestTypeDef]
    ) -> CreatePredictorResponseTypeDef:
        """
        This operation creates a legacy predictor that does not include all the
        predictor functionalities provided by Amazon Forecast.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_predictor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_predictor)
        """

    def create_predictor_backtest_export_job(
        self, **kwargs: Unpack[CreatePredictorBacktestExportJobRequestTypeDef]
    ) -> CreatePredictorBacktestExportJobResponseTypeDef:
        """
        Exports backtest forecasts and accuracy metrics generated by the
        <a>CreateAutoPredictor</a> or <a>CreatePredictor</a> operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_predictor_backtest_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_predictor_backtest_export_job)
        """

    def create_what_if_analysis(
        self, **kwargs: Unpack[CreateWhatIfAnalysisRequestTypeDef]
    ) -> CreateWhatIfAnalysisResponseTypeDef:
        """
        What-if analysis is a scenario modeling technique where you make a hypothetical
        change to a time series and compare the forecasts generated by these changes
        against the baseline, unchanged time series.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_what_if_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_what_if_analysis)
        """

    def create_what_if_forecast(
        self, **kwargs: Unpack[CreateWhatIfForecastRequestTypeDef]
    ) -> CreateWhatIfForecastResponseTypeDef:
        """
        A what-if forecast is a forecast that is created from a modified version of the
        baseline forecast.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_what_if_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_what_if_forecast)
        """

    def create_what_if_forecast_export(
        self, **kwargs: Unpack[CreateWhatIfForecastExportRequestTypeDef]
    ) -> CreateWhatIfForecastExportResponseTypeDef:
        """
        Exports a forecast created by the <a>CreateWhatIfForecast</a> operation to your
        Amazon Simple Storage Service (Amazon S3) bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/create_what_if_forecast_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#create_what_if_forecast_export)
        """

    def delete_dataset(
        self, **kwargs: Unpack[DeleteDatasetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Amazon Forecast dataset that was created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_dataset)
        """

    def delete_dataset_group(
        self, **kwargs: Unpack[DeleteDatasetGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a dataset group created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_dataset_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_dataset_group)
        """

    def delete_dataset_import_job(
        self, **kwargs: Unpack[DeleteDatasetImportJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a dataset import job created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_dataset_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_dataset_import_job)
        """

    def delete_explainability(
        self, **kwargs: Unpack[DeleteExplainabilityRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Explainability resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_explainability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_explainability)
        """

    def delete_explainability_export(
        self, **kwargs: Unpack[DeleteExplainabilityExportRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an Explainability export.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_explainability_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_explainability_export)
        """

    def delete_forecast(
        self, **kwargs: Unpack[DeleteForecastRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a forecast created using the <a>CreateForecast</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_forecast)
        """

    def delete_forecast_export_job(
        self, **kwargs: Unpack[DeleteForecastExportJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a forecast export job created using the <a>CreateForecastExportJob</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_forecast_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_forecast_export_job)
        """

    def delete_monitor(
        self, **kwargs: Unpack[DeleteMonitorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_monitor)
        """

    def delete_predictor(
        self, **kwargs: Unpack[DeletePredictorRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a predictor created using the <a>DescribePredictor</a> or
        <a>CreatePredictor</a> operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_predictor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_predictor)
        """

    def delete_predictor_backtest_export_job(
        self, **kwargs: Unpack[DeletePredictorBacktestExportJobRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a predictor backtest export job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_predictor_backtest_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_predictor_backtest_export_job)
        """

    def delete_resource_tree(
        self, **kwargs: Unpack[DeleteResourceTreeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes an entire resource tree.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_resource_tree.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_resource_tree)
        """

    def delete_what_if_analysis(
        self, **kwargs: Unpack[DeleteWhatIfAnalysisRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a what-if analysis created using the <a>CreateWhatIfAnalysis</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_what_if_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_what_if_analysis)
        """

    def delete_what_if_forecast(
        self, **kwargs: Unpack[DeleteWhatIfForecastRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a what-if forecast created using the <a>CreateWhatIfForecast</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_what_if_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_what_if_forecast)
        """

    def delete_what_if_forecast_export(
        self, **kwargs: Unpack[DeleteWhatIfForecastExportRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a what-if forecast export created using the
        <a>CreateWhatIfForecastExport</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/delete_what_if_forecast_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#delete_what_if_forecast_export)
        """

    def describe_auto_predictor(
        self, **kwargs: Unpack[DescribeAutoPredictorRequestTypeDef]
    ) -> DescribeAutoPredictorResponseTypeDef:
        """
        Describes a predictor created using the CreateAutoPredictor operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_auto_predictor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_auto_predictor)
        """

    def describe_dataset(
        self, **kwargs: Unpack[DescribeDatasetRequestTypeDef]
    ) -> DescribeDatasetResponseTypeDef:
        """
        Describes an Amazon Forecast dataset created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_dataset)
        """

    def describe_dataset_group(
        self, **kwargs: Unpack[DescribeDatasetGroupRequestTypeDef]
    ) -> DescribeDatasetGroupResponseTypeDef:
        """
        Describes a dataset group created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_dataset_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_dataset_group)
        """

    def describe_dataset_import_job(
        self, **kwargs: Unpack[DescribeDatasetImportJobRequestTypeDef]
    ) -> DescribeDatasetImportJobResponseTypeDef:
        """
        Describes a dataset import job created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_dataset_import_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_dataset_import_job)
        """

    def describe_explainability(
        self, **kwargs: Unpack[DescribeExplainabilityRequestTypeDef]
    ) -> DescribeExplainabilityResponseTypeDef:
        """
        Describes an Explainability resource created using the
        <a>CreateExplainability</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_explainability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_explainability)
        """

    def describe_explainability_export(
        self, **kwargs: Unpack[DescribeExplainabilityExportRequestTypeDef]
    ) -> DescribeExplainabilityExportResponseTypeDef:
        """
        Describes an Explainability export created using the
        <a>CreateExplainabilityExport</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_explainability_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_explainability_export)
        """

    def describe_forecast(
        self, **kwargs: Unpack[DescribeForecastRequestTypeDef]
    ) -> DescribeForecastResponseTypeDef:
        """
        Describes a forecast created using the <a>CreateForecast</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_forecast)
        """

    def describe_forecast_export_job(
        self, **kwargs: Unpack[DescribeForecastExportJobRequestTypeDef]
    ) -> DescribeForecastExportJobResponseTypeDef:
        """
        Describes a forecast export job created using the
        <a>CreateForecastExportJob</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_forecast_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_forecast_export_job)
        """

    def describe_monitor(
        self, **kwargs: Unpack[DescribeMonitorRequestTypeDef]
    ) -> DescribeMonitorResponseTypeDef:
        """
        Describes a monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_monitor)
        """

    def describe_predictor(
        self, **kwargs: Unpack[DescribePredictorRequestTypeDef]
    ) -> DescribePredictorResponseTypeDef:
        """
        This operation is only valid for legacy predictors created with CreatePredictor.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_predictor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_predictor)
        """

    def describe_predictor_backtest_export_job(
        self, **kwargs: Unpack[DescribePredictorBacktestExportJobRequestTypeDef]
    ) -> DescribePredictorBacktestExportJobResponseTypeDef:
        """
        Describes a predictor backtest export job created using the
        <a>CreatePredictorBacktestExportJob</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_predictor_backtest_export_job.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_predictor_backtest_export_job)
        """

    def describe_what_if_analysis(
        self, **kwargs: Unpack[DescribeWhatIfAnalysisRequestTypeDef]
    ) -> DescribeWhatIfAnalysisResponseTypeDef:
        """
        Describes the what-if analysis created using the <a>CreateWhatIfAnalysis</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_what_if_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_what_if_analysis)
        """

    def describe_what_if_forecast(
        self, **kwargs: Unpack[DescribeWhatIfForecastRequestTypeDef]
    ) -> DescribeWhatIfForecastResponseTypeDef:
        """
        Describes the what-if forecast created using the <a>CreateWhatIfForecast</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_what_if_forecast.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_what_if_forecast)
        """

    def describe_what_if_forecast_export(
        self, **kwargs: Unpack[DescribeWhatIfForecastExportRequestTypeDef]
    ) -> DescribeWhatIfForecastExportResponseTypeDef:
        """
        Describes the what-if forecast export created using the
        <a>CreateWhatIfForecastExport</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/describe_what_if_forecast_export.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#describe_what_if_forecast_export)
        """

    def get_accuracy_metrics(
        self, **kwargs: Unpack[GetAccuracyMetricsRequestTypeDef]
    ) -> GetAccuracyMetricsResponseTypeDef:
        """
        Provides metrics on the accuracy of the models that were trained by the
        <a>CreatePredictor</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_accuracy_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_accuracy_metrics)
        """

    def list_dataset_groups(
        self, **kwargs: Unpack[ListDatasetGroupsRequestTypeDef]
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        Returns a list of dataset groups created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetGroup.html">CreateDatasetGroup</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_dataset_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_dataset_groups)
        """

    def list_dataset_import_jobs(
        self, **kwargs: Unpack[ListDatasetImportJobsRequestTypeDef]
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        Returns a list of dataset import jobs created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDatasetImportJob.html">CreateDatasetImportJob</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_dataset_import_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_dataset_import_jobs)
        """

    def list_datasets(
        self, **kwargs: Unpack[ListDatasetsRequestTypeDef]
    ) -> ListDatasetsResponseTypeDef:
        """
        Returns a list of datasets created using the <a
        href="https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html">CreateDataset</a>
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_datasets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_datasets)
        """

    def list_explainabilities(
        self, **kwargs: Unpack[ListExplainabilitiesRequestTypeDef]
    ) -> ListExplainabilitiesResponseTypeDef:
        """
        Returns a list of Explainability resources created using the
        <a>CreateExplainability</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_explainabilities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_explainabilities)
        """

    def list_explainability_exports(
        self, **kwargs: Unpack[ListExplainabilityExportsRequestTypeDef]
    ) -> ListExplainabilityExportsResponseTypeDef:
        """
        Returns a list of Explainability exports created using the
        <a>CreateExplainabilityExport</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_explainability_exports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_explainability_exports)
        """

    def list_forecast_export_jobs(
        self, **kwargs: Unpack[ListForecastExportJobsRequestTypeDef]
    ) -> ListForecastExportJobsResponseTypeDef:
        """
        Returns a list of forecast export jobs created using the
        <a>CreateForecastExportJob</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_forecast_export_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_forecast_export_jobs)
        """

    def list_forecasts(
        self, **kwargs: Unpack[ListForecastsRequestTypeDef]
    ) -> ListForecastsResponseTypeDef:
        """
        Returns a list of forecasts created using the <a>CreateForecast</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_forecasts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_forecasts)
        """

    def list_monitor_evaluations(
        self, **kwargs: Unpack[ListMonitorEvaluationsRequestTypeDef]
    ) -> ListMonitorEvaluationsResponseTypeDef:
        """
        Returns a list of the monitoring evaluation results and predictor events
        collected by the monitor resource during different windows of time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_monitor_evaluations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_monitor_evaluations)
        """

    def list_monitors(
        self, **kwargs: Unpack[ListMonitorsRequestTypeDef]
    ) -> ListMonitorsResponseTypeDef:
        """
        Returns a list of monitors created with the <a>CreateMonitor</a> operation and
        <a>CreateAutoPredictor</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_monitors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_monitors)
        """

    def list_predictor_backtest_export_jobs(
        self, **kwargs: Unpack[ListPredictorBacktestExportJobsRequestTypeDef]
    ) -> ListPredictorBacktestExportJobsResponseTypeDef:
        """
        Returns a list of predictor backtest export jobs created using the
        <a>CreatePredictorBacktestExportJob</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_predictor_backtest_export_jobs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_predictor_backtest_export_jobs)
        """

    def list_predictors(
        self, **kwargs: Unpack[ListPredictorsRequestTypeDef]
    ) -> ListPredictorsResponseTypeDef:
        """
        Returns a list of predictors created using the <a>CreateAutoPredictor</a> or
        <a>CreatePredictor</a> operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_predictors.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_predictors)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags for an Amazon Forecast resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_tags_for_resource)
        """

    def list_what_if_analyses(
        self, **kwargs: Unpack[ListWhatIfAnalysesRequestTypeDef]
    ) -> ListWhatIfAnalysesResponseTypeDef:
        """
        Returns a list of what-if analyses created using the
        <a>CreateWhatIfAnalysis</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_what_if_analyses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_what_if_analyses)
        """

    def list_what_if_forecast_exports(
        self, **kwargs: Unpack[ListWhatIfForecastExportsRequestTypeDef]
    ) -> ListWhatIfForecastExportsResponseTypeDef:
        """
        Returns a list of what-if forecast exports created using the
        <a>CreateWhatIfForecastExport</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_what_if_forecast_exports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_what_if_forecast_exports)
        """

    def list_what_if_forecasts(
        self, **kwargs: Unpack[ListWhatIfForecastsRequestTypeDef]
    ) -> ListWhatIfForecastsResponseTypeDef:
        """
        Returns a list of what-if forecasts created using the
        <a>CreateWhatIfForecast</a> operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/list_what_if_forecasts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#list_what_if_forecasts)
        """

    def resume_resource(
        self, **kwargs: Unpack[ResumeResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resumes a stopped monitor resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/resume_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#resume_resource)
        """

    def stop_resource(
        self, **kwargs: Unpack[StopResourceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Stops a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/stop_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#stop_resource)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified
        <code>resourceArn</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#untag_resource)
        """

    def update_dataset_group(
        self, **kwargs: Unpack[UpdateDatasetGroupRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Replaces the datasets in a dataset group with the specified datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/update_dataset_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#update_dataset_group)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_groups"]
    ) -> ListDatasetGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_import_jobs"]
    ) -> ListDatasetImportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_datasets"]
    ) -> ListDatasetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_explainabilities"]
    ) -> ListExplainabilitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_explainability_exports"]
    ) -> ListExplainabilityExportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_forecast_export_jobs"]
    ) -> ListForecastExportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_forecasts"]
    ) -> ListForecastsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_monitor_evaluations"]
    ) -> ListMonitorEvaluationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_monitors"]
    ) -> ListMonitorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_predictor_backtest_export_jobs"]
    ) -> ListPredictorBacktestExportJobsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_predictors"]
    ) -> ListPredictorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_what_if_analyses"]
    ) -> ListWhatIfAnalysesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_what_if_forecast_exports"]
    ) -> ListWhatIfForecastExportsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_what_if_forecasts"]
    ) -> ListWhatIfForecastsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/forecast/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/client/#get_paginator)
        """
