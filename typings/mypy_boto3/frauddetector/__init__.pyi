"""
Main interface for frauddetector service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_frauddetector import (
        Client,
        FraudDetectorClient,
    )

    session = Session()
    client: FraudDetectorClient = session.client("frauddetector")
    ```
"""

from .client import FraudDetectorClient

Client = FraudDetectorClient

__all__ = ("Client", "FraudDetectorClient")
