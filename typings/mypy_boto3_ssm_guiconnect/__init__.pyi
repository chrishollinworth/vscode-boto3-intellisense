"""
Main interface for ssm-guiconnect service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ssm_guiconnect import (
        Client,
        SSMGUIConnectClient,
    )

    session = Session()
    client: SSMGUIConnectClient = session.client("ssm-guiconnect")
    ```
"""

from .client import SSMGUIConnectClient

Client = SSMGUIConnectClient

__all__ = ("Client", "SSMGUIConnectClient")
