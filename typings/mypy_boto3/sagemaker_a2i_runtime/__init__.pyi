"""
Main interface for sagemaker-a2i-runtime service.

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_a2i_runtime import (
        AugmentedAIRuntimeClient,
        Client,
        ListHumanLoopsPaginator,
    )

    session = boto3.Session()

    client: AugmentedAIRuntimeClient = boto3.client("sagemaker-a2i-runtime")
    session_client: AugmentedAIRuntimeClient = session.client("sagemaker-a2i-runtime")

    list_human_loops_paginator: ListHumanLoopsPaginator = client.get_paginator("list_human_loops")
    ```
"""
from .client import AugmentedAIRuntimeClient
from .paginator import ListHumanLoopsPaginator

Client = AugmentedAIRuntimeClient

__all__ = ("AugmentedAIRuntimeClient", "Client", "ListHumanLoopsPaginator")
