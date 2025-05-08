"""
Main interface for forecast service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_forecast/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_forecast import (
        Client,
        ForecastServiceClient,
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

from .client import ForecastServiceClient
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

Client = ForecastServiceClient

__all__ = (
    "Client",
    "ForecastServiceClient",
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
