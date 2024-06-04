"""
Main interface for marketplace-agreement service.

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplace_agreement import (
        AgreementServiceClient,
        Client,
    )

    session = boto3.Session()

    client: AgreementServiceClient = boto3.client("marketplace-agreement")
    session_client: AgreementServiceClient = session.client("marketplace-agreement")
    ```
"""

from .client import AgreementServiceClient

Client = AgreementServiceClient

__all__ = ("AgreementServiceClient", "Client")
