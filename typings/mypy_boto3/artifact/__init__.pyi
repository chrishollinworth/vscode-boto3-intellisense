"""
Main interface for artifact service.

Usage::

    ```python
    import boto3
    from mypy_boto3_artifact import (
        ArtifactClient,
        Client,
        ListReportsPaginator,
    )

    session = boto3.Session()

    client: ArtifactClient = boto3.client("artifact")
    session_client: ArtifactClient = session.client("artifact")

    list_reports_paginator: ListReportsPaginator = client.get_paginator("list_reports")
    ```
"""

from .client import ArtifactClient
from .paginator import ListReportsPaginator

Client = ArtifactClient

__all__ = ("ArtifactClient", "Client", "ListReportsPaginator")
