"""
Main interface for mq service.

Usage::

    ```python
    import boto3
    from mypy_boto3_mq import (
        Client,
        ListBrokersPaginator,
        MQClient,
    )

    session = boto3.Session()

    client: MQClient = boto3.client("mq")
    session_client: MQClient = session.client("mq")

    list_brokers_paginator: ListBrokersPaginator = client.get_paginator("list_brokers")
    ```
"""
from .client import MQClient
from .paginator import ListBrokersPaginator

Client = MQClient

__all__ = ("Client", "ListBrokersPaginator", "MQClient")
