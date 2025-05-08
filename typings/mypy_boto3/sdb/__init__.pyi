"""
Main interface for sdb service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sdb/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sdb import (
        Client,
        ListDomainsPaginator,
        SelectPaginator,
        SimpleDBClient,
    )

    session = Session()
    client: SimpleDBClient = session.client("sdb")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    select_paginator: SelectPaginator = client.get_paginator("select")
    ```
"""

from .client import SimpleDBClient
from .paginator import ListDomainsPaginator, SelectPaginator

Client = SimpleDBClient

__all__ = ("Client", "ListDomainsPaginator", "SelectPaginator", "SimpleDBClient")
