"""
Main interface for shield service.

Usage::

    ```python
    import boto3
    from mypy_boto3_shield import (
        Client,
        ListAttacksPaginator,
        ListProtectionsPaginator,
        ShieldClient,
    )

    session = boto3.Session()

    client: ShieldClient = boto3.client("shield")
    session_client: ShieldClient = session.client("shield")

    list_attacks_paginator: ListAttacksPaginator = client.get_paginator("list_attacks")
    list_protections_paginator: ListProtectionsPaginator = client.get_paginator("list_protections")
    ```
"""
from mypy_boto3_shield.client import ShieldClient
from mypy_boto3_shield.paginator import ListAttacksPaginator, ListProtectionsPaginator

Client = ShieldClient


__all__ = ("Client", "ListAttacksPaginator", "ListProtectionsPaginator", "ShieldClient")
