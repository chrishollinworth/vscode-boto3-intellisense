"""
Main interface for bedrock service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock import (
        BedrockClient,
        Client,
        ListCustomModelsPaginator,
        ListEvaluationJobsPaginator,
        ListGuardrailsPaginator,
        ListImportedModelsPaginator,
        ListInferenceProfilesPaginator,
        ListMarketplaceModelEndpointsPaginator,
        ListModelCopyJobsPaginator,
        ListModelCustomizationJobsPaginator,
        ListModelImportJobsPaginator,
        ListModelInvocationJobsPaginator,
        ListPromptRoutersPaginator,
        ListProvisionedModelThroughputsPaginator,
    )

    session = Session()
    client: BedrockClient = session.client("bedrock")

    list_custom_models_paginator: ListCustomModelsPaginator = client.get_paginator("list_custom_models")
    list_evaluation_jobs_paginator: ListEvaluationJobsPaginator = client.get_paginator("list_evaluation_jobs")
    list_guardrails_paginator: ListGuardrailsPaginator = client.get_paginator("list_guardrails")
    list_imported_models_paginator: ListImportedModelsPaginator = client.get_paginator("list_imported_models")
    list_inference_profiles_paginator: ListInferenceProfilesPaginator = client.get_paginator("list_inference_profiles")
    list_marketplace_model_endpoints_paginator: ListMarketplaceModelEndpointsPaginator = client.get_paginator("list_marketplace_model_endpoints")
    list_model_copy_jobs_paginator: ListModelCopyJobsPaginator = client.get_paginator("list_model_copy_jobs")
    list_model_customization_jobs_paginator: ListModelCustomizationJobsPaginator = client.get_paginator("list_model_customization_jobs")
    list_model_import_jobs_paginator: ListModelImportJobsPaginator = client.get_paginator("list_model_import_jobs")
    list_model_invocation_jobs_paginator: ListModelInvocationJobsPaginator = client.get_paginator("list_model_invocation_jobs")
    list_prompt_routers_paginator: ListPromptRoutersPaginator = client.get_paginator("list_prompt_routers")
    list_provisioned_model_throughputs_paginator: ListProvisionedModelThroughputsPaginator = client.get_paginator("list_provisioned_model_throughputs")
    ```
"""

from .client import BedrockClient
from .paginator import (
    ListCustomModelsPaginator,
    ListEvaluationJobsPaginator,
    ListGuardrailsPaginator,
    ListImportedModelsPaginator,
    ListInferenceProfilesPaginator,
    ListMarketplaceModelEndpointsPaginator,
    ListModelCopyJobsPaginator,
    ListModelCustomizationJobsPaginator,
    ListModelImportJobsPaginator,
    ListModelInvocationJobsPaginator,
    ListPromptRoutersPaginator,
    ListProvisionedModelThroughputsPaginator,
)

Client = BedrockClient

__all__ = (
    "BedrockClient",
    "Client",
    "ListCustomModelsPaginator",
    "ListEvaluationJobsPaginator",
    "ListGuardrailsPaginator",
    "ListImportedModelsPaginator",
    "ListInferenceProfilesPaginator",
    "ListMarketplaceModelEndpointsPaginator",
    "ListModelCopyJobsPaginator",
    "ListModelCustomizationJobsPaginator",
    "ListModelImportJobsPaginator",
    "ListModelInvocationJobsPaginator",
    "ListPromptRoutersPaginator",
    "ListProvisionedModelThroughputsPaginator",
)
