"""
Main interface for importexport service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_importexport/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_importexport import (
        Client,
        ImportExportClient,
        ListJobsPaginator,
    )

    session = Session()
    client: ImportExportClient = session.client("importexport")

    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""

from .client import ImportExportClient
from .paginator import ListJobsPaginator

Client = ImportExportClient

__all__ = ("Client", "ImportExportClient", "ListJobsPaginator")
