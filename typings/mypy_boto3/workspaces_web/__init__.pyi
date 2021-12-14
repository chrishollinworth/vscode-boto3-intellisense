"""
Main interface for workspaces-web service.

Usage::

    ```python
    import boto3
    from mypy_boto3_workspaces_web import (
        Client,
        WorkSpacesWebClient,
    )

    session = boto3.Session()

    client: WorkSpacesWebClient = boto3.client("workspaces-web")
    session_client: WorkSpacesWebClient = session.client("workspaces-web")
    ```
"""
from .client import WorkSpacesWebClient

Client = WorkSpacesWebClient

__all__ = ("Client", "WorkSpacesWebClient")
