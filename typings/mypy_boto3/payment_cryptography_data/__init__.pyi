"""
Main interface for payment-cryptography-data service.

Usage::

    ```python
    import boto3
    from mypy_boto3_payment_cryptography_data import (
        Client,
        PaymentCryptographyDataPlaneClient,
    )

    session = boto3.Session()

    client: PaymentCryptographyDataPlaneClient = boto3.client("payment-cryptography-data")
    session_client: PaymentCryptographyDataPlaneClient = session.client("payment-cryptography-data")
    ```
"""

from .client import PaymentCryptographyDataPlaneClient

Client = PaymentCryptographyDataPlaneClient

__all__ = ("Client", "PaymentCryptographyDataPlaneClient")
