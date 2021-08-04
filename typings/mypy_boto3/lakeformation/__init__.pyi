"""
Main interface for lakeformation service.

Usage::

    ```python
    import boto3
    from mypy_boto3_lakeformation import (
        Client,
        LakeFormationClient,
    )

    session = boto3.Session()

    client: LakeFormationClient = boto3.client("lakeformation")
    session_client: LakeFormationClient = session.client("lakeformation")
    ```
"""
from .client import LakeFormationClient

Client = LakeFormationClient

__all__ = ("Client", "LakeFormationClient")
