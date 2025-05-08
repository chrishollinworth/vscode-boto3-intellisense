"""
Main interface for cloudtrail-data service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail_data/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_cloudtrail_data import (
        Client,
        CloudTrailDataServiceClient,
    )

    session = Session()
    client: CloudTrailDataServiceClient = session.client("cloudtrail-data")
    ```
"""

from .client import CloudTrailDataServiceClient

Client = CloudTrailDataServiceClient

__all__ = ("Client", "CloudTrailDataServiceClient")
