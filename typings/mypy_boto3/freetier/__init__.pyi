"""
Main interface for freetier service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_freetier/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_freetier import (
        Client,
        FreeTierClient,
        GetFreeTierUsagePaginator,
    )

    session = Session()
    client: FreeTierClient = session.client("freetier")

    get_free_tier_usage_paginator: GetFreeTierUsagePaginator = client.get_paginator("get_free_tier_usage")
    ```
"""

from .client import FreeTierClient
from .paginator import GetFreeTierUsagePaginator

Client = FreeTierClient

__all__ = ("Client", "FreeTierClient", "GetFreeTierUsagePaginator")
