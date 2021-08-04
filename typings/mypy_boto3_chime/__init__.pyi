"""
Main interface for chime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_chime import (
        ChimeClient,
        Client,
        ListAccountsPaginator,
        ListUsersPaginator,
    )

    session = boto3.Session()

    client: ChimeClient = boto3.client("chime")
    session_client: ChimeClient = session.client("chime")

    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""
from .client import ChimeClient
from .paginator import ListAccountsPaginator, ListUsersPaginator

Client = ChimeClient

__all__ = ("ChimeClient", "Client", "ListAccountsPaginator", "ListUsersPaginator")
