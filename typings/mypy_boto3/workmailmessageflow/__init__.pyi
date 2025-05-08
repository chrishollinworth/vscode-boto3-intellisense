"""
Main interface for workmailmessageflow service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workmailmessageflow/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_workmailmessageflow import (
        Client,
        WorkMailMessageFlowClient,
    )

    session = Session()
    client: WorkMailMessageFlowClient = session.client("workmailmessageflow")
    ```
"""

from .client import WorkMailMessageFlowClient

Client = WorkMailMessageFlowClient

__all__ = ("Client", "WorkMailMessageFlowClient")
