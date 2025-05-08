"""
Main interface for savingsplans service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_savingsplans import (
        Client,
        SavingsPlansClient,
    )

    session = Session()
    client: SavingsPlansClient = session.client("savingsplans")
    ```
"""

from .client import SavingsPlansClient

Client = SavingsPlansClient

__all__ = ("Client", "SavingsPlansClient")
