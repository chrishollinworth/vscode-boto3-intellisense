"""
Main interface for ebs service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ebs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ebs import (
        Client,
        EBSClient,
    )

    session = Session()
    client: EBSClient = session.client("ebs")
    ```
"""

from .client import EBSClient

Client = EBSClient

__all__ = ("Client", "EBSClient")
