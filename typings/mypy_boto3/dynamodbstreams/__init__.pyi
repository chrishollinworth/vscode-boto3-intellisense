"""
Main interface for dynamodbstreams service.

Usage::

    ```python
    import boto3
    from mypy_boto3_dynamodbstreams import (
        Client,
        DynamoDBStreamsClient,
    )

    session = boto3.Session()

    client: DynamoDBStreamsClient = boto3.client("dynamodbstreams")
    session_client: DynamoDBStreamsClient = session.client("dynamodbstreams")
    ```
"""
from .client import DynamoDBStreamsClient

Client = DynamoDBStreamsClient

__all__ = ("Client", "DynamoDBStreamsClient")
