"""
Main interface for dynamodbstreams service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_dynamodbstreams import (
        Client,
        DynamoDBStreamsClient,
    )

    session = Session()
    client: DynamoDBStreamsClient = session.client("dynamodbstreams")
    ```
"""

from .client import DynamoDBStreamsClient

Client = DynamoDBStreamsClient

__all__ = ("Client", "DynamoDBStreamsClient")
