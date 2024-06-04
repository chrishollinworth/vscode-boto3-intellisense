"""
Main interface for emr-serverless service.

Usage::

    ```python
    import boto3
    from mypy_boto3_emr_serverless import (
        Client,
        EMRServerlessClient,
        ListApplicationsPaginator,
        ListJobRunAttemptsPaginator,
        ListJobRunsPaginator,
    )

    session = boto3.Session()

    client: EMRServerlessClient = boto3.client("emr-serverless")
    session_client: EMRServerlessClient = session.client("emr-serverless")

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
