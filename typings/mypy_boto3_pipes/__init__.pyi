"""
Main interface for pipes service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_pipes/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_pipes import (
        Client,
        EventBridgePipesClient,
        ListPipesPaginator,
    )

    session = Session()
    client: EventBridgePipesClient = session.client("pipes")

    list_pipes_paginator: ListPipesPaginator = client.get_paginator("list_pipes")
    ```
"""

from .client import EventBridgePipesClient
from .paginator import ListPipesPaginator

Client = EventBridgePipesClient

__all__ = ("Client", "EventBridgePipesClient", "ListPipesPaginator")
