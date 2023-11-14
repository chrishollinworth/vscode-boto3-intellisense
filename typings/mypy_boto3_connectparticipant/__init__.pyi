"""
Main interface for connectparticipant service.

Usage::

    ```python
    import boto3
    from mypy_boto3_connectparticipant import (
        Client,
        ConnectParticipantClient,
    )

    session = boto3.Session()

    client: ConnectParticipantClient = boto3.client("connectparticipant")
    session_client: ConnectParticipantClient = session.client("connectparticipant")
    ```
"""
from .client import ConnectParticipantClient

Client = ConnectParticipantClient

__all__ = ("Client", "ConnectParticipantClient")
