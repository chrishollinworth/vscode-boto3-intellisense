"""
Main interface for bedrock-runtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_bedrock_runtime import (
        BedrockRuntimeClient,
        Client,
    )

    session = boto3.Session()

    client: BedrockRuntimeClient = boto3.client("bedrock-runtime")
    session_client: BedrockRuntimeClient = session.client("bedrock-runtime")
    ```
"""

from .client import BedrockRuntimeClient

Client = BedrockRuntimeClient

__all__ = ("BedrockRuntimeClient", "Client")
