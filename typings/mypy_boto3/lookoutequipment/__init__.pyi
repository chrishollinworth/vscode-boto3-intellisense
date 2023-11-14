"""
Main interface for lookoutequipment service.

Usage::

    ```python
    import boto3
    from mypy_boto3_lookoutequipment import (
        Client,
        LookoutEquipmentClient,
    )

    session = boto3.Session()

    client: LookoutEquipmentClient = boto3.client("lookoutequipment")
    session_client: LookoutEquipmentClient = session.client("lookoutequipment")
    ```
"""
from .client import LookoutEquipmentClient

Client = LookoutEquipmentClient

__all__ = ("Client", "LookoutEquipmentClient")
