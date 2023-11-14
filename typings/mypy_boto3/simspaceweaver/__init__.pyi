"""
Main interface for simspaceweaver service.

Usage::

    ```python
    import boto3
    from mypy_boto3_simspaceweaver import (
        Client,
        SimSpaceWeaverClient,
    )

    session = boto3.Session()

    client: SimSpaceWeaverClient = boto3.client("simspaceweaver")
    session_client: SimSpaceWeaverClient = session.client("simspaceweaver")
    ```
"""
from .client import SimSpaceWeaverClient

Client = SimSpaceWeaverClient

__all__ = ("Client", "SimSpaceWeaverClient")
