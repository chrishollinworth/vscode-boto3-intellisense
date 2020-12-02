"""
Main interface for connect-contact-lens service.

Usage::

    ```python
    import boto3
    from mypy_boto3_connect_contact_lens import (
        Client,
        ConnectContactLensClient,
    )

    session = boto3.Session()

    client: ConnectContactLensClient = boto3.client("connect-contact-lens")
    session_client: ConnectContactLensClient = session.client("connect-contact-lens")
    ```
"""
from mypy_boto3_connect_contact_lens.client import ConnectContactLensClient

Client = ConnectContactLensClient


__all__ = ("Client", "ConnectContactLensClient")
