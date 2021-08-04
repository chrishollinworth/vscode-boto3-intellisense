"""
Main interface for rds-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_rds_data import (
        Client,
        RDSDataServiceClient,
    )

    session = boto3.Session()

    client: RDSDataServiceClient = boto3.client("rds-data")
    session_client: RDSDataServiceClient = session.client("rds-data")
    ```
"""
from .client import RDSDataServiceClient

Client = RDSDataServiceClient

__all__ = ("Client", "RDSDataServiceClient")
