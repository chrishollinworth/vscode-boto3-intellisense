"""
Main interface for emr-serverless service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_serverless/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_emr_serverless import (
        Client,
        EMRServerlessClient,
        ListApplicationsPaginator,
        ListJobRunAttemptsPaginator,
        ListJobRunsPaginator,
    )

    session = Session()
    client: EMRServerlessClient = session.client("emr-serverless")

    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    list_job_run_attempts_paginator: ListJobRunAttemptsPaginator = client.get_paginator("list_job_run_attempts")
    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    ```
"""

from .client import EMRServerlessClient
from .paginator import ListApplicationsPaginator, ListJobRunAttemptsPaginator, ListJobRunsPaginator

Client = EMRServerlessClient

__all__ = (
    "Client",
    "EMRServerlessClient",
    "ListApplicationsPaginator",
    "ListJobRunAttemptsPaginator",
    "ListJobRunsPaginator",
)
