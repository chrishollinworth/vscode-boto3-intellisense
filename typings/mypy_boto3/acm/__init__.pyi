"""
Main interface for acm service.

Usage::

    ```python
    import boto3
    from mypy_boto3_acm import (
        ACMClient,
        CertificateValidatedWaiter,
        Client,
        ListCertificatesPaginator,
    )

    session = boto3.Session()

    client: ACMClient = boto3.client("acm")
    session_client: ACMClient = session.client("acm")

    certificate_validated_waiter: CertificateValidatedWaiter = client.get_waiter("certificate_validated")

    list_certificates_paginator: ListCertificatesPaginator = client.get_paginator("list_certificates")
    ```
"""
from .client import ACMClient
from .paginator import ListCertificatesPaginator
from .waiter import CertificateValidatedWaiter

Client = ACMClient

__all__ = ("ACMClient", "CertificateValidatedWaiter", "Client", "ListCertificatesPaginator")
