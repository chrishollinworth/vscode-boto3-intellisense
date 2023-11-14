"""
Main interface for kendra-ranking service.

Usage::

    ```python
    import boto3
    from mypy_boto3_kendra_ranking import (
        Client,
        KendraRankingClient,
    )

    session = boto3.Session()

    client: KendraRankingClient = boto3.client("kendra-ranking")
    session_client: KendraRankingClient = session.client("kendra-ranking")
    ```
"""
from .client import KendraRankingClient

Client = KendraRankingClient

__all__ = ("Client", "KendraRankingClient")
