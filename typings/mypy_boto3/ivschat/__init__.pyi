"""
Main interface for ivschat service.

Usage::

    ```python
    import boto3
    from mypy_boto3_ivschat import (
        Client,
        ivschatClient,
    )

    session = boto3.Session()

    client: ivschatClient = boto3.client("ivschat")
    session_client: ivschatClient = session.client("ivschat")
    ```
"""

from .client import ivschatClient

Client = ivschatClient

__all__ = ("Client", "ivschatClient")
