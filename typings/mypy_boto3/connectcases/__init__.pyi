"""
Main interface for connectcases service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectcases/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_connectcases import (
        Client,
        ConnectCasesClient,
        ListCaseRulesPaginator,
        SearchAllRelatedItemsPaginator,
        SearchCasesPaginator,
        SearchRelatedItemsPaginator,
    )

    session = Session()
    client: ConnectCasesClient = session.client("connectcases")

    list_case_rules_paginator: ListCaseRulesPaginator = client.get_paginator("list_case_rules")
    search_all_related_items_paginator: SearchAllRelatedItemsPaginator = client.get_paginator("search_all_related_items")
    search_cases_paginator: SearchCasesPaginator = client.get_paginator("search_cases")
    search_related_items_paginator: SearchRelatedItemsPaginator = client.get_paginator("search_related_items")
    ```
"""

from .client import ConnectCasesClient
from .paginator import (
    ListCaseRulesPaginator,
    SearchAllRelatedItemsPaginator,
    SearchCasesPaginator,
    SearchRelatedItemsPaginator,
)

Client = ConnectCasesClient

__all__ = (
    "Client",
    "ConnectCasesClient",
    "ListCaseRulesPaginator",
    "SearchAllRelatedItemsPaginator",
    "SearchCasesPaginator",
    "SearchRelatedItemsPaginator",
)
