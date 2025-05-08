"""
Main interface for sagemaker-a2i-runtime service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_a2i_runtime import (
        AugmentedAIRuntimeClient,
        Client,
        ListHumanLoopsPaginator,
    )

    session = Session()
    client: AugmentedAIRuntimeClient = session.client("sagemaker-a2i-runtime")

    list_human_loops_paginator: ListHumanLoopsPaginator = client.get_paginator("list_human_loops")
    ```
"""

from .client import AugmentedAIRuntimeClient
from .paginator import ListHumanLoopsPaginator

Client = AugmentedAIRuntimeClient

__all__ = ("AugmentedAIRuntimeClient", "Client", "ListHumanLoopsPaginator")
