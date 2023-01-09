"""
Main interface for pipes service.

Usage::

    ```python
    import boto3
    from mypy_boto3_pipes import (
        Client,
        EventBridgePipesClient,
        ListPipesPaginator,
    )

    session = boto3.Session()

    client: EventBridgePipesClient = boto3.client("pipes")
    session_client: EventBridgePipesClient = session.client("pipes")

    list_pipes_paginator: ListPipesPaginator = client.get_paginator("list_pipes")
    ```
"""
from .client import EventBridgePipesClient
from .paginator import ListPipesPaginator

Client = EventBridgePipesClient

__all__ = ("Client", "EventBridgePipesClient", "ListPipesPaginator")
