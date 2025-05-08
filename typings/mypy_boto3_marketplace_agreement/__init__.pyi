"""
Main interface for marketplace-agreement service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_marketplace_agreement/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_marketplace_agreement import (
        AgreementServiceClient,
        Client,
    )

    session = Session()
    client: AgreementServiceClient = session.client("marketplace-agreement")
    ```
"""

from .client import AgreementServiceClient

Client = AgreementServiceClient

__all__ = ("AgreementServiceClient", "Client")
