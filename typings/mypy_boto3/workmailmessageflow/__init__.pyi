"""
Main interface for workmailmessageflow service.

Usage::

    ```python
    import boto3
    from mypy_boto3_workmailmessageflow import (
        Client,
        WorkMailMessageFlowClient,
    )

    session = boto3.Session()

    client: WorkMailMessageFlowClient = boto3.client("workmailmessageflow")
    session_client: WorkMailMessageFlowClient = session.client("workmailmessageflow")
    ```
"""
from .client import WorkMailMessageFlowClient

Client = WorkMailMessageFlowClient

__all__ = ("Client", "WorkMailMessageFlowClient")
