"""
Main interface for amplifybackend service.

Usage::

    ```python
    import boto3
    from mypy_boto3_amplifybackend import (
        AmplifyBackendClient,
        Client,
        ListBackendJobsPaginator,
    )

    session = boto3.Session()

    client: AmplifyBackendClient = boto3.client("amplifybackend")
    session_client: AmplifyBackendClient = session.client("amplifybackend")

    list_backend_jobs_paginator: ListBackendJobsPaginator = client.get_paginator("list_backend_jobs")
    ```
"""
from .client import AmplifyBackendClient
from .paginator import ListBackendJobsPaginator

Client = AmplifyBackendClient

__all__ = ("AmplifyBackendClient", "Client", "ListBackendJobsPaginator")
