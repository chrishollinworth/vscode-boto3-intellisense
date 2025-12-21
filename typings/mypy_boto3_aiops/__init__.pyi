"""
Main interface for aiops service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_aiops/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_aiops import (
        AIOpsClient,
        Client,
        ListInvestigationGroupsPaginator,
    )

    session = Session()
    client: AIOpsClient = session.client("aiops")

    list_investigation_groups_paginator: ListInvestigationGroupsPaginator = client.get_paginator("list_investigation_groups")
    ```
"""

from .client import AIOpsClient
from .paginator import ListInvestigationGroupsPaginator

Client = AIOpsClient

__all__ = ("AIOpsClient", "Client", "ListInvestigationGroupsPaginator")
