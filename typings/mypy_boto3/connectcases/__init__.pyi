"""
Main interface for connectcases service.

Usage::

    ```python
    import boto3
    from mypy_boto3_connectcases import (
        Client,
        ConnectCasesClient,
        SearchCasesPaginator,
        SearchRelatedItemsPaginator,
    )

    session = boto3.Session()

    client: ConnectCasesClient = boto3.client("connectcases")
    session_client: ConnectCasesClient = session.client("connectcases")

    search_cases_paginator: SearchCasesPaginator = client.get_paginator("search_cases")
    search_related_items_paginator: SearchRelatedItemsPaginator = client.get_paginator("search_related_items")
    ```
"""
from .client import ConnectCasesClient
from .paginator import SearchCasesPaginator, SearchRelatedItemsPaginator

Client = ConnectCasesClient

__all__ = ("Client", "ConnectCasesClient", "SearchCasesPaginator", "SearchRelatedItemsPaginator")
