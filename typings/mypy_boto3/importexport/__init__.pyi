"""
Main interface for importexport service.

Usage::

    ```python
    import boto3
    from mypy_boto3_importexport import (
        Client,
        ImportExportClient,
        ListJobsPaginator,
    )

    session = boto3.Session()

    client: ImportExportClient = boto3.client("importexport")
    session_client: ImportExportClient = session.client("importexport")

    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""
from .client import ImportExportClient
from .paginator import ListJobsPaginator

Client = ImportExportClient

__all__ = ("Client", "ImportExportClient", "ListJobsPaginator")
