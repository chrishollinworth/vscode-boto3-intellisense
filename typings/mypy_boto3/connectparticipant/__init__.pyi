"""
Main interface for connectparticipant service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_connectparticipant import (
        Client,
        ConnectParticipantClient,
    )

    session = Session()
    client: ConnectParticipantClient = session.client("connectparticipant")
    ```
"""

from .client import ConnectParticipantClient

Client = ConnectParticipantClient

__all__ = ("Client", "ConnectParticipantClient")
