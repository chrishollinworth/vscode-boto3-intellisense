"""
Main interface for wellarchitected service.

Usage::

    ```python
    import boto3
    from mypy_boto3_wellarchitected import (
        Client,
        WellArchitectedClient,
    )

    session = boto3.Session()

    client: WellArchitectedClient = boto3.client("wellarchitected")
    session_client: WellArchitectedClient = session.client("wellarchitected")
    ```
"""
from .client import WellArchitectedClient

Client = WellArchitectedClient

__all__ = ("Client", "WellArchitectedClient")
