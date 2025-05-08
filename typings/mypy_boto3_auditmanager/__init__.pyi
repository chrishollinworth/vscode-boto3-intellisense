"""
Main interface for auditmanager service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_auditmanager import (
        AuditManagerClient,
        Client,
    )

    session = Session()
    client: AuditManagerClient = session.client("auditmanager")
    ```
"""

from .client import AuditManagerClient

Client = AuditManagerClient

__all__ = ("AuditManagerClient", "Client")
