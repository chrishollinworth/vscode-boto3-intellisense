"""
Main interface for supplychain service.

Usage::

    ```python
    import boto3
    from mypy_boto3_supplychain import (
        Client,
        SupplyChainClient,
    )

    session = boto3.Session()

    client: SupplyChainClient = boto3.client("supplychain")
    session_client: SupplyChainClient = session.client("supplychain")
    ```
"""

from .client import SupplyChainClient

Client = SupplyChainClient

__all__ = ("Client", "SupplyChainClient")
