"""
Main interface for eks-auth service.

Usage::

    ```python
    import boto3
    from mypy_boto3_eks_auth import (
        Client,
        EKSAuthClient,
    )

    session = boto3.Session()

    client: EKSAuthClient = boto3.client("eks-auth")
    session_client: EKSAuthClient = session.client("eks-auth")
    ```
"""

from .client import EKSAuthClient

Client = EKSAuthClient

__all__ = ("Client", "EKSAuthClient")
