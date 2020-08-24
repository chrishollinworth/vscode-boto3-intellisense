"""
Main interface for outposts service.

Usage::

    ```python
    import boto3
    from mypy_boto3_outposts import (
        Client,
        OutpostsClient,
    )

    session = boto3.Session()

    client: OutpostsClient = boto3.client("outposts")
    session_client: OutpostsClient = session.client("outposts")
    ```
"""
from mypy_boto3_outposts.client import OutpostsClient

Client = OutpostsClient


__all__ = ("Client", "OutpostsClient")
