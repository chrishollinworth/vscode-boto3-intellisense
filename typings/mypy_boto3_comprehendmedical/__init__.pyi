"""
Main interface for comprehendmedical service.

Usage::

    ```python
    import boto3
    from mypy_boto3_comprehendmedical import (
        Client,
        ComprehendMedicalClient,
    )

    session = boto3.Session()

    client: ComprehendMedicalClient = boto3.client("comprehendmedical")
    session_client: ComprehendMedicalClient = session.client("comprehendmedical")
    ```
"""
from mypy_boto3_comprehendmedical.client import ComprehendMedicalClient

Client = ComprehendMedicalClient


__all__ = ("Client", "ComprehendMedicalClient")
