"""
Main interface for sso-oidc service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sso_oidc import (
        Client,
        SSOOIDCClient,
    )

    session = boto3.Session()

    client: SSOOIDCClient = boto3.client("sso-oidc")
    session_client: SSOOIDCClient = session.client("sso-oidc")
    ```
"""
from .client import SSOOIDCClient

Client = SSOOIDCClient

__all__ = ("Client", "SSOOIDCClient")
