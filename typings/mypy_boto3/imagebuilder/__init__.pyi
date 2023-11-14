"""
Main interface for imagebuilder service.

Usage::

    ```python
    import boto3
    from mypy_boto3_imagebuilder import (
        Client,
        imagebuilderClient,
    )

    session = boto3.Session()

    client: imagebuilderClient = boto3.client("imagebuilder")
    session_client: imagebuilderClient = session.client("imagebuilder")
    ```
"""
from .client import imagebuilderClient

Client = imagebuilderClient

__all__ = ("Client", "imagebuilderClient")
