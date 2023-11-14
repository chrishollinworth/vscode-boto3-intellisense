"""
Main interface for customer-profiles service.

Usage::

    ```python
    import boto3
    from mypy_boto3_customer_profiles import (
        Client,
        CustomerProfilesClient,
        ListEventStreamsPaginator,
    )

    session = boto3.Session()

    client: CustomerProfilesClient = boto3.client("customer-profiles")
    session_client: CustomerProfilesClient = session.client("customer-profiles")

    list_event_streams_paginator: ListEventStreamsPaginator = client.get_paginator("list_event_streams")
    ```
"""
from .client import CustomerProfilesClient
from .paginator import ListEventStreamsPaginator

Client = CustomerProfilesClient

__all__ = ("Client", "CustomerProfilesClient", "ListEventStreamsPaginator")
