"""
Main interface for bedrock service.

Usage::

    ```python
    import boto3
    from mypy_boto3_bedrock import (
        BedrockClient,
        Client,
        ListCustomModelsPaginator,
        ListEvaluationJobsPaginator,
        ListGuardrailsPaginator,
        ListModelCustomizationJobsPaginator,
        ListProvisionedModelThroughputsPaginator,
    )

    session = boto3.Session()

    client: BedrockClient = boto3.client("bedrock")
    session_client: BedrockClient = session.client("bedrock")

    list_custom_models_paginator: ListCustomModelsPaginator = client.get_paginator("list_custom_models")
    list_evaluation_jobs_paginator: ListEvaluationJobsPaginator = client.get_paginator("list_evaluation_jobs")
    list_guardrails_paginator: ListGuardrailsPaginator = client.get_paginator("list_guardrails")
    list_model_customization_jobs_paginator: ListModelCustomizationJobsPaginator = client.get_paginator("list_model_customization_jobs")
    list_provisioned_model_throughputs_paginator: ListProvisionedModelThroughputsPaginator = client.get_paginator("list_provisioned_model_throughputs")
    ```
"""

from .client import BedrockClient
from .paginator import (
    ListCustomModelsPaginator,
    ListEvaluationJobsPaginator,
    ListGuardrailsPaginator,
    ListModelCustomizationJobsPaginator,
    ListProvisionedModelThroughputsPaginator,
)

Client = BedrockClient

__all__ = (
    "BedrockClient",
    "Client",
    "ListCustomModelsPaginator",
    "ListEvaluationJobsPaginator",
    "ListGuardrailsPaginator",
    "ListModelCustomizationJobsPaginator",
    "ListProvisionedModelThroughputsPaginator",
)
