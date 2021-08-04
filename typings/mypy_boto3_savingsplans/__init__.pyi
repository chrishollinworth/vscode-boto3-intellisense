"""
Main interface for savingsplans service.

Usage::

    ```python
    import boto3
    from mypy_boto3_savingsplans import (
        Client,
        SavingsPlansClient,
    )

    session = boto3.Session()

    client: SavingsPlansClient = boto3.client("savingsplans")
    session_client: SavingsPlansClient = session.client("savingsplans")
    ```
"""
from .client import SavingsPlansClient

Client = SavingsPlansClient

__all__ = ("Client", "SavingsPlansClient")
