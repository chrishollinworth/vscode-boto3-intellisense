"""
Main interface for panorama service.

Usage::

    ```python
    import boto3
    from mypy_boto3_panorama import (
        Client,
        PanoramaClient,
    )

    session = boto3.Session()

    client: PanoramaClient = boto3.client("panorama")
    session_client: PanoramaClient = session.client("panorama")
    ```
"""
from .client import PanoramaClient

Client = PanoramaClient

__all__ = ("Client", "PanoramaClient")
