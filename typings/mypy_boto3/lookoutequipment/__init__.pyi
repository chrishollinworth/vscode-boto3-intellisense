"""
Main interface for lookoutequipment service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_lookoutequipment import (
        Client,
        LookoutEquipmentClient,
    )

    session = Session()
    client: LookoutEquipmentClient = session.client("lookoutequipment")
    ```
"""

from .client import LookoutEquipmentClient

Client = LookoutEquipmentClient

__all__ = ("Client", "LookoutEquipmentClient")
