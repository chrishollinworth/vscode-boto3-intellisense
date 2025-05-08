"""
Main interface for connect-contact-lens service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_connect_contact_lens import (
        Client,
        ConnectContactLensClient,
    )

    session = Session()
    client: ConnectContactLensClient = session.client("connect-contact-lens")
    ```
"""

from .client import ConnectContactLensClient

Client = ConnectContactLensClient

__all__ = ("Client", "ConnectContactLensClient")
