"""
Main interface for mwaa service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mwaa import (
        Client,
        ListEnvironmentsPaginator,
        MWAAClient,
    )

    session = boto3.Session()

    client: MWAAClient = boto3.client("mwaa")
    session_client: MWAAClient = session.client("mwaa")

    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""
from .client import MWAAClient
from .paginator import ListEnvironmentsPaginator

Client = MWAAClient

__all__ = ("Client", "ListEnvironmentsPaginator", "MWAAClient")
