"""
Main interface for wellarchitected service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_wellarchitected/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_wellarchitected import (
        Client,
        WellArchitectedClient,
    )

    session = Session()
    client: WellArchitectedClient = session.client("wellarchitected")
    ```
"""

from .client import WellArchitectedClient

Client = WellArchitectedClient

__all__ = ("Client", "WellArchitectedClient")
