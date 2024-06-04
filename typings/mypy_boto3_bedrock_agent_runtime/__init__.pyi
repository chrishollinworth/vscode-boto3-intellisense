"""
Main interface for bedrock-agent-runtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_bedrock_agent_runtime import (
        AgentsforBedrockRuntimeClient,
        Client,
        RetrievePaginator,
    )

    session = boto3.Session()

    client: AgentsforBedrockRuntimeClient = boto3.client("bedrock-agent-runtime")
    session_client: AgentsforBedrockRuntimeClient = session.client("bedrock-agent-runtime")

    retrieve_paginator: RetrievePaginator = client.get_paginator("retrieve")
    ```
"""

from .client import AgentsforBedrockRuntimeClient
from .paginator import RetrievePaginator

Client = AgentsforBedrockRuntimeClient

__all__ = ("AgentsforBedrockRuntimeClient", "Client", "RetrievePaginator")
