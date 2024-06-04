"""
Main interface for freetier service.

Usage::

    ```python
    import boto3
    from mypy_boto3_freetier import (
        Client,
        FreeTierClient,
        GetFreeTierUsagePaginator,
    )

    session = boto3.Session()

    client: FreeTierClient = boto3.client("freetier")
    session_client: FreeTierClient = session.client("freetier")

    get_free_tier_usage_paginator: GetFreeTierUsagePaginator = client.get_paginator("get_free_tier_usage")
    ```
"""

from .client import FreeTierClient
from .paginator import GetFreeTierUsagePaginator

Client = FreeTierClient

__all__ = ("Client", "FreeTierClient", "GetFreeTierUsagePaginator")
