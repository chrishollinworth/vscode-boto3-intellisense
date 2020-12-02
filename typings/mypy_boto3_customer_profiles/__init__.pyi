"""
Main interface for customer-profiles service.

Usage::

    ```python
    import boto3
    from mypy_boto3_customer_profiles import (
        Client,
        CustomerProfilesClient,
    )

    session = boto3.Session()

    client: CustomerProfilesClient = boto3.client("customer-profiles")
    session_client: CustomerProfilesClient = session.client("customer-profiles")
    ```
"""
from mypy_boto3_customer_profiles.client import CustomerProfilesClient

Client = CustomerProfilesClient


__all__ = ("Client", "CustomerProfilesClient")
