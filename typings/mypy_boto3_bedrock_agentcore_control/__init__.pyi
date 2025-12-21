"""
Main interface for bedrock-agentcore-control service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_agentcore_control import (
        BedrockAgentCoreControlClient,
        Client,
        ListAgentRuntimeEndpointsPaginator,
        ListAgentRuntimeVersionsPaginator,
        ListAgentRuntimesPaginator,
        ListApiKeyCredentialProvidersPaginator,
        ListBrowsersPaginator,
        ListCodeInterpretersPaginator,
        ListEvaluatorsPaginator,
        ListGatewayTargetsPaginator,
        ListGatewaysPaginator,
        ListMemoriesPaginator,
        ListOauth2CredentialProvidersPaginator,
        ListOnlineEvaluationConfigsPaginator,
        ListPoliciesPaginator,
        ListPolicyEnginesPaginator,
        ListPolicyGenerationAssetsPaginator,
        ListPolicyGenerationsPaginator,
        ListWorkloadIdentitiesPaginator,
        MemoryCreatedWaiter,
        PolicyActiveWaiter,
        PolicyDeletedWaiter,
        PolicyEngineActiveWaiter,
        PolicyEngineDeletedWaiter,
        PolicyGenerationCompletedWaiter,
    )

    session = Session()
    client: BedrockAgentCoreControlClient = session.client("bedrock-agentcore-control")

    memory_created_waiter: MemoryCreatedWaiter = client.get_waiter("memory_created")
    policy_active_waiter: PolicyActiveWaiter = client.get_waiter("policy_active")
    policy_deleted_waiter: PolicyDeletedWaiter = client.get_waiter("policy_deleted")
    policy_engine_active_waiter: PolicyEngineActiveWaiter = client.get_waiter("policy_engine_active")
    policy_engine_deleted_waiter: PolicyEngineDeletedWaiter = client.get_waiter("policy_engine_deleted")
    policy_generation_completed_waiter: PolicyGenerationCompletedWaiter = client.get_waiter("policy_generation_completed")

    list_agent_runtime_endpoints_paginator: ListAgentRuntimeEndpointsPaginator = client.get_paginator("list_agent_runtime_endpoints")
    list_agent_runtime_versions_paginator: ListAgentRuntimeVersionsPaginator = client.get_paginator("list_agent_runtime_versions")
    list_agent_runtimes_paginator: ListAgentRuntimesPaginator = client.get_paginator("list_agent_runtimes")
    list_api_key_credential_providers_paginator: ListApiKeyCredentialProvidersPaginator = client.get_paginator("list_api_key_credential_providers")
    list_browsers_paginator: ListBrowsersPaginator = client.get_paginator("list_browsers")
    list_code_interpreters_paginator: ListCodeInterpretersPaginator = client.get_paginator("list_code_interpreters")
    list_evaluators_paginator: ListEvaluatorsPaginator = client.get_paginator("list_evaluators")
    list_gateway_targets_paginator: ListGatewayTargetsPaginator = client.get_paginator("list_gateway_targets")
    list_gateways_paginator: ListGatewaysPaginator = client.get_paginator("list_gateways")
    list_memories_paginator: ListMemoriesPaginator = client.get_paginator("list_memories")
    list_oauth2_credential_providers_paginator: ListOauth2CredentialProvidersPaginator = client.get_paginator("list_oauth2_credential_providers")
    list_online_evaluation_configs_paginator: ListOnlineEvaluationConfigsPaginator = client.get_paginator("list_online_evaluation_configs")
    list_policies_paginator: ListPoliciesPaginator = client.get_paginator("list_policies")
    list_policy_engines_paginator: ListPolicyEnginesPaginator = client.get_paginator("list_policy_engines")
    list_policy_generation_assets_paginator: ListPolicyGenerationAssetsPaginator = client.get_paginator("list_policy_generation_assets")
    list_policy_generations_paginator: ListPolicyGenerationsPaginator = client.get_paginator("list_policy_generations")
    list_workload_identities_paginator: ListWorkloadIdentitiesPaginator = client.get_paginator("list_workload_identities")
    ```
"""

from .client import BedrockAgentCoreControlClient
from .paginator import (
    ListAgentRuntimeEndpointsPaginator,
    ListAgentRuntimesPaginator,
    ListAgentRuntimeVersionsPaginator,
    ListApiKeyCredentialProvidersPaginator,
    ListBrowsersPaginator,
    ListCodeInterpretersPaginator,
    ListEvaluatorsPaginator,
    ListGatewaysPaginator,
    ListGatewayTargetsPaginator,
    ListMemoriesPaginator,
    ListOauth2CredentialProvidersPaginator,
    ListOnlineEvaluationConfigsPaginator,
    ListPoliciesPaginator,
    ListPolicyEnginesPaginator,
    ListPolicyGenerationAssetsPaginator,
    ListPolicyGenerationsPaginator,
    ListWorkloadIdentitiesPaginator,
)
from .waiter import (
    MemoryCreatedWaiter,
    PolicyActiveWaiter,
    PolicyDeletedWaiter,
    PolicyEngineActiveWaiter,
    PolicyEngineDeletedWaiter,
    PolicyGenerationCompletedWaiter,
)

Client = BedrockAgentCoreControlClient

__all__ = (
    "BedrockAgentCoreControlClient",
    "Client",
    "ListAgentRuntimeEndpointsPaginator",
    "ListAgentRuntimeVersionsPaginator",
    "ListAgentRuntimesPaginator",
    "ListApiKeyCredentialProvidersPaginator",
    "ListBrowsersPaginator",
    "ListCodeInterpretersPaginator",
    "ListEvaluatorsPaginator",
    "ListGatewayTargetsPaginator",
    "ListGatewaysPaginator",
    "ListMemoriesPaginator",
    "ListOauth2CredentialProvidersPaginator",
    "ListOnlineEvaluationConfigsPaginator",
    "ListPoliciesPaginator",
    "ListPolicyEnginesPaginator",
    "ListPolicyGenerationAssetsPaginator",
    "ListPolicyGenerationsPaginator",
    "ListWorkloadIdentitiesPaginator",
    "MemoryCreatedWaiter",
    "PolicyActiveWaiter",
    "PolicyDeletedWaiter",
    "PolicyEngineActiveWaiter",
    "PolicyEngineDeletedWaiter",
    "PolicyGenerationCompletedWaiter",
)
