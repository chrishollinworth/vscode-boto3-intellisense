"""
Main interface for sdb service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sdb import (
        Client,
        ListDomainsPaginator,
        SelectPaginator,
        SimpleDBClient,
    )

    session = boto3.Session()

    client: SimpleDBClient = boto3.client("sdb")
    session_client: SimpleDBClient = session.client("sdb")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    select_paginator: SelectPaginator = client.get_paginator("select")
    ```
"""
from mypy_boto3_sdb.client import SimpleDBClient
from mypy_boto3_sdb.paginator import ListDomainsPaginator, SelectPaginator

Client = SimpleDBClient


__all__ = ("Client", "ListDomainsPaginator", "SelectPaginator", "SimpleDBClient")
