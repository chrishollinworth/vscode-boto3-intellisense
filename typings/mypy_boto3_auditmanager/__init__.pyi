"""
Main interface for auditmanager service.

Usage::

    ```python
    import boto3
    from mypy_boto3_auditmanager import (
        AuditManagerClient,
        Client,
    )

    session = boto3.Session()

    client: AuditManagerClient = boto3.client("auditmanager")
    session_client: AuditManagerClient = session.client("auditmanager")
    ```
"""
from mypy_boto3_auditmanager.client import AuditManagerClient

Client = AuditManagerClient


__all__ = ("AuditManagerClient", "Client")
