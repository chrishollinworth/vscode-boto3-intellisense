"""
Main interface for chime service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_chime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_chime import (
        ChimeClient,
        Client,
        ListAccountsPaginator,
        ListUsersPaginator,
    )

    session = Session()
    client: ChimeClient = session.client("chime")

    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    list_users_paginator: ListUsersPaginator = client.get_paginator("list_users")
    ```
"""

from .client import ChimeClient
from .paginator import ListAccountsPaginator, ListUsersPaginator

Client = ChimeClient

__all__ = ("ChimeClient", "Client", "ListAccountsPaginator", "ListUsersPaginator")
