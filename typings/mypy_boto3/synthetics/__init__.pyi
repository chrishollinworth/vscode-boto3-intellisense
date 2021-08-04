"""
Main interface for synthetics service.

Usage::

    ```python
    import boto3
    from mypy_boto3_synthetics import (
        Client,
        SyntheticsClient,
    )

    session = boto3.Session()

    client: SyntheticsClient = boto3.client("synthetics")
    session_client: SyntheticsClient = session.client("synthetics")
    ```
"""
from .client import SyntheticsClient

Client = SyntheticsClient

__all__ = ("Client", "SyntheticsClient")
