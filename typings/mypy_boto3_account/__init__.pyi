"""
Main interface for account service.

Usage::

    ```python
    import boto3
    from mypy_boto3_account import (
        AccountClient,
        Client,
        ListRegionsPaginator,
    )

    session = boto3.Session()

    client: AccountClient = boto3.client("account")
    session_client: AccountClient = session.client("account")

    list_regions_paginator: ListRegionsPaginator = client.get_paginator("list_regions")
    ```
"""

from .client import AccountClient
from .paginator import ListRegionsPaginator

Client = AccountClient

__all__ = ("AccountClient", "Client", "ListRegionsPaginator")
