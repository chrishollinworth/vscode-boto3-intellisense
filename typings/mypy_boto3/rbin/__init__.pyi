"""
Main interface for rbin service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rbin/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rbin import (
        Client,
        ListRulesPaginator,
        RecycleBinClient,
    )

    session = Session()
    client: RecycleBinClient = session.client("rbin")

    list_rules_paginator: ListRulesPaginator = client.get_paginator("list_rules")
    ```
"""

from .client import RecycleBinClient
from .paginator import ListRulesPaginator

Client = RecycleBinClient

__all__ = ("Client", "ListRulesPaginator", "RecycleBinClient")
