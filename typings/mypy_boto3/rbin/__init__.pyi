"""
Main interface for rbin service.

Usage::

    ```python
    import boto3
    from mypy_boto3_rbin import (
        Client,
        ListRulesPaginator,
        RecycleBinClient,
    )

    session = boto3.Session()

    client: RecycleBinClient = boto3.client("rbin")
    session_client: RecycleBinClient = session.client("rbin")

    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    ```
"""
from .client import RecycleBinClient
from .paginator import ListRulesPaginator

Client = RecycleBinClient

__all__ = ("Client", "ListRulesPaginator", "RecycleBinClient")
