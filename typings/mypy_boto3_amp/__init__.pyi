"""
Main interface for amp service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amp/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_amp import (
        Client,
        ListRuleGroupsNamespacesPaginator,
        ListScrapersPaginator,
        ListWorkspacesPaginator,
        PrometheusServiceClient,
        ScraperActiveWaiter,
        ScraperDeletedWaiter,
        WorkspaceActiveWaiter,
        WorkspaceDeletedWaiter,
    )

    session = Session()
    client: PrometheusServiceClient = session.client("amp")

    scraper_active_waiter: ScraperActiveWaiter = client.get_waiter("scraper_active")
    scraper_deleted_waiter: ScraperDeletedWaiter = client.get_waiter("scraper_deleted")
    workspace_active_waiter: WorkspaceActiveWaiter = client.get_waiter("workspace_active")
    workspace_deleted_waiter: WorkspaceDeletedWaiter = client.get_waiter("workspace_deleted")

    list_rule_groups_namespaces_paginator: ListRuleGroupsNamespacesPaginator = client.get_paginator("list_rule_groups_namespaces")
    list_scrapers_paginator: ListScrapersPaginator = client.get_paginator("list_scrapers")
    list_workspaces_paginator: ListWorkspacesPaginator = client.get_paginator("list_workspaces")
    ```
"""

from .client import PrometheusServiceClient
from .paginator import (
    ListRuleGroupsNamespacesPaginator,
    ListScrapersPaginator,
    ListWorkspacesPaginator,
)
from .waiter import (
    ScraperActiveWaiter,
    ScraperDeletedWaiter,
    WorkspaceActiveWaiter,
    WorkspaceDeletedWaiter,
)

Client = PrometheusServiceClient

__all__ = (
    "Client",
    "ListRuleGroupsNamespacesPaginator",
    "ListScrapersPaginator",
    "ListWorkspacesPaginator",
    "PrometheusServiceClient",
    "ScraperActiveWaiter",
    "ScraperDeletedWaiter",
    "WorkspaceActiveWaiter",
    "WorkspaceDeletedWaiter",
)
