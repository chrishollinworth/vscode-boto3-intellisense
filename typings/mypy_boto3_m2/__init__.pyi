"""
Main interface for m2 service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_m2/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_m2 import (
        Client,
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
        MainframeModernizationClient,
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

from .client import MainframeModernizationClient
from .paginator import (
    ListApplicationsPaginator,
    ListApplicationVersionsPaginator,
    ListBatchJobDefinitionsPaginator,
    ListBatchJobExecutionsPaginator,
    ListDataSetExportHistoryPaginator,
    ListDataSetImportHistoryPaginator,
    ListDataSetsPaginator,
    ListDeploymentsPaginator,
    ListEngineVersionsPaginator,
    ListEnvironmentsPaginator,
)

Client = MainframeModernizationClient

__all__ = (
    "Client",
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
    "MainframeModernizationClient",
)
