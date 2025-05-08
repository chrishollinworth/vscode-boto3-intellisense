"""
Main interface for rds-data service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rds_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_rds_data import (
        Client,
        RDSDataServiceClient,
    )

    session = Session()
    client: RDSDataServiceClient = session.client("rds-data")
    ```
"""

from .client import RDSDataServiceClient

Client = RDSDataServiceClient

__all__ = ("Client", "RDSDataServiceClient")
