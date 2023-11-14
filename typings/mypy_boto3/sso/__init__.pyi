"""
Main interface for sso service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sso import (
        Client,
        ListAccountRolesPaginator,
        ListAccountsPaginator,
        SSOClient,
    )

    session = boto3.Session()

    client: SSOClient = boto3.client("sso")
    session_client: SSOClient = session.client("sso")

    list_account_roles_paginator: ListAccountRolesPaginator = client.get_paginator("list_account_roles")
    list_accounts_paginator: ListAccountsPaginator = client.get_paginator("list_accounts")
    ```
"""
from .client import SSOClient
from .paginator import ListAccountRolesPaginator, ListAccountsPaginator

Client = SSOClient

__all__ = ("Client", "ListAccountRolesPaginator", "ListAccountsPaginator", "SSOClient")
