"""
Type annotations for bedrock-agentcore-control service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_bedrock_agentcore_control.client import BedrockAgentCoreControlClient

    session = Session()
    client: BedrockAgentCoreControlClient = session.client("bedrock-agentcore-control")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
from .type_defs import (
    CreateAgentRuntimeEndpointRequestTypeDef,
    CreateAgentRuntimeEndpointResponseTypeDef,
    CreateAgentRuntimeRequestTypeDef,
    CreateAgentRuntimeResponseTypeDef,
    CreateApiKeyCredentialProviderRequestTypeDef,
    CreateApiKeyCredentialProviderResponseTypeDef,
    CreateBrowserRequestTypeDef,
    CreateBrowserResponseTypeDef,
    CreateCodeInterpreterRequestTypeDef,
    CreateCodeInterpreterResponseTypeDef,
    CreateEvaluatorRequestTypeDef,
    CreateEvaluatorResponseTypeDef,
    CreateGatewayRequestTypeDef,
    CreateGatewayResponseTypeDef,
    CreateGatewayTargetRequestTypeDef,
    CreateGatewayTargetResponseTypeDef,
    CreateMemoryInputTypeDef,
    CreateMemoryOutputTypeDef,
    CreateOauth2CredentialProviderRequestTypeDef,
    CreateOauth2CredentialProviderResponseTypeDef,
    CreateOnlineEvaluationConfigRequestTypeDef,
    CreateOnlineEvaluationConfigResponseTypeDef,
    CreatePolicyEngineRequestTypeDef,
    CreatePolicyEngineResponseTypeDef,
    CreatePolicyRequestTypeDef,
    CreatePolicyResponseTypeDef,
    CreateWorkloadIdentityRequestTypeDef,
    CreateWorkloadIdentityResponseTypeDef,
    DeleteAgentRuntimeEndpointRequestTypeDef,
    DeleteAgentRuntimeEndpointResponseTypeDef,
    DeleteAgentRuntimeRequestTypeDef,
    DeleteAgentRuntimeResponseTypeDef,
    DeleteApiKeyCredentialProviderRequestTypeDef,
    DeleteBrowserRequestTypeDef,
    DeleteBrowserResponseTypeDef,
    DeleteCodeInterpreterRequestTypeDef,
    DeleteCodeInterpreterResponseTypeDef,
    DeleteEvaluatorRequestTypeDef,
    DeleteEvaluatorResponseTypeDef,
    DeleteGatewayRequestTypeDef,
    DeleteGatewayResponseTypeDef,
    DeleteGatewayTargetRequestTypeDef,
    DeleteGatewayTargetResponseTypeDef,
    DeleteMemoryInputTypeDef,
    DeleteMemoryOutputTypeDef,
    DeleteOauth2CredentialProviderRequestTypeDef,
    DeleteOnlineEvaluationConfigRequestTypeDef,
    DeleteOnlineEvaluationConfigResponseTypeDef,
    DeletePolicyEngineRequestTypeDef,
    DeletePolicyEngineResponseTypeDef,
    DeletePolicyRequestTypeDef,
    DeletePolicyResponseTypeDef,
    DeleteResourcePolicyRequestTypeDef,
    DeleteWorkloadIdentityRequestTypeDef,
    GetAgentRuntimeEndpointRequestTypeDef,
    GetAgentRuntimeEndpointResponseTypeDef,
    GetAgentRuntimeRequestTypeDef,
    GetAgentRuntimeResponseTypeDef,
    GetApiKeyCredentialProviderRequestTypeDef,
    GetApiKeyCredentialProviderResponseTypeDef,
    GetBrowserRequestTypeDef,
    GetBrowserResponseTypeDef,
    GetCodeInterpreterRequestTypeDef,
    GetCodeInterpreterResponseTypeDef,
    GetEvaluatorRequestTypeDef,
    GetEvaluatorResponseTypeDef,
    GetGatewayRequestTypeDef,
    GetGatewayResponseTypeDef,
    GetGatewayTargetRequestTypeDef,
    GetGatewayTargetResponseTypeDef,
    GetMemoryInputTypeDef,
    GetMemoryOutputTypeDef,
    GetOauth2CredentialProviderRequestTypeDef,
    GetOauth2CredentialProviderResponseTypeDef,
    GetOnlineEvaluationConfigRequestTypeDef,
    GetOnlineEvaluationConfigResponseTypeDef,
    GetPolicyEngineRequestTypeDef,
    GetPolicyEngineResponseTypeDef,
    GetPolicyGenerationRequestTypeDef,
    GetPolicyGenerationResponseTypeDef,
    GetPolicyRequestTypeDef,
    GetPolicyResponseTypeDef,
    GetResourcePolicyRequestTypeDef,
    GetResourcePolicyResponseTypeDef,
    GetTokenVaultRequestTypeDef,
    GetTokenVaultResponseTypeDef,
    GetWorkloadIdentityRequestTypeDef,
    GetWorkloadIdentityResponseTypeDef,
    ListAgentRuntimeEndpointsRequestTypeDef,
    ListAgentRuntimeEndpointsResponseTypeDef,
    ListAgentRuntimesRequestTypeDef,
    ListAgentRuntimesResponseTypeDef,
    ListAgentRuntimeVersionsRequestTypeDef,
    ListAgentRuntimeVersionsResponseTypeDef,
    ListApiKeyCredentialProvidersRequestTypeDef,
    ListApiKeyCredentialProvidersResponseTypeDef,
    ListBrowsersRequestTypeDef,
    ListBrowsersResponseTypeDef,
    ListCodeInterpretersRequestTypeDef,
    ListCodeInterpretersResponseTypeDef,
    ListEvaluatorsRequestTypeDef,
    ListEvaluatorsResponseTypeDef,
    ListGatewaysRequestTypeDef,
    ListGatewaysResponseTypeDef,
    ListGatewayTargetsRequestTypeDef,
    ListGatewayTargetsResponseTypeDef,
    ListMemoriesInputTypeDef,
    ListMemoriesOutputTypeDef,
    ListOauth2CredentialProvidersRequestTypeDef,
    ListOauth2CredentialProvidersResponseTypeDef,
    ListOnlineEvaluationConfigsRequestTypeDef,
    ListOnlineEvaluationConfigsResponseTypeDef,
    ListPoliciesRequestTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyEnginesRequestTypeDef,
    ListPolicyEnginesResponseTypeDef,
    ListPolicyGenerationAssetsRequestTypeDef,
    ListPolicyGenerationAssetsResponseTypeDef,
    ListPolicyGenerationsRequestTypeDef,
    ListPolicyGenerationsResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWorkloadIdentitiesRequestTypeDef,
    ListWorkloadIdentitiesResponseTypeDef,
    PutResourcePolicyRequestTypeDef,
    PutResourcePolicyResponseTypeDef,
    SetTokenVaultCMKRequestTypeDef,
    SetTokenVaultCMKResponseTypeDef,
    StartPolicyGenerationRequestTypeDef,
    StartPolicyGenerationResponseTypeDef,
    SynchronizeGatewayTargetsRequestTypeDef,
    SynchronizeGatewayTargetsResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateAgentRuntimeEndpointRequestTypeDef,
    UpdateAgentRuntimeEndpointResponseTypeDef,
    UpdateAgentRuntimeRequestTypeDef,
    UpdateAgentRuntimeResponseTypeDef,
    UpdateApiKeyCredentialProviderRequestTypeDef,
    UpdateApiKeyCredentialProviderResponseTypeDef,
    UpdateEvaluatorRequestTypeDef,
    UpdateEvaluatorResponseTypeDef,
    UpdateGatewayRequestTypeDef,
    UpdateGatewayResponseTypeDef,
    UpdateGatewayTargetRequestTypeDef,
    UpdateGatewayTargetResponseTypeDef,
    UpdateMemoryInputTypeDef,
    UpdateMemoryOutputTypeDef,
    UpdateOauth2CredentialProviderRequestTypeDef,
    UpdateOauth2CredentialProviderResponseTypeDef,
    UpdateOnlineEvaluationConfigRequestTypeDef,
    UpdateOnlineEvaluationConfigResponseTypeDef,
    UpdatePolicyEngineRequestTypeDef,
    UpdatePolicyEngineResponseTypeDef,
    UpdatePolicyRequestTypeDef,
    UpdatePolicyResponseTypeDef,
    UpdateWorkloadIdentityRequestTypeDef,
    UpdateWorkloadIdentityResponseTypeDef,
)
from .waiter import (
    MemoryCreatedWaiter,
    PolicyActiveWaiter,
    PolicyDeletedWaiter,
    PolicyEngineActiveWaiter,
    PolicyEngineDeletedWaiter,
    PolicyGenerationCompletedWaiter,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("BedrockAgentCoreControlClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    DecryptionFailure: Type[BotocoreClientError]
    EncryptionFailure: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class BedrockAgentCoreControlClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control.html#BedrockAgentCoreControl.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        BedrockAgentCoreControlClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control.html#BedrockAgentCoreControl.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#generate_presigned_url)
        """

    def create_agent_runtime(
        self, **kwargs: Unpack[CreateAgentRuntimeRequestTypeDef]
    ) -> CreateAgentRuntimeResponseTypeDef:
        """
        Creates an Amazon Bedrock AgentCore Runtime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_agent_runtime.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_agent_runtime)
        """

    def create_agent_runtime_endpoint(
        self, **kwargs: Unpack[CreateAgentRuntimeEndpointRequestTypeDef]
    ) -> CreateAgentRuntimeEndpointResponseTypeDef:
        """
        Creates an AgentCore Runtime endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_agent_runtime_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_agent_runtime_endpoint)
        """

    def create_api_key_credential_provider(
        self, **kwargs: Unpack[CreateApiKeyCredentialProviderRequestTypeDef]
    ) -> CreateApiKeyCredentialProviderResponseTypeDef:
        """
        Creates a new API key credential provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_api_key_credential_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_api_key_credential_provider)
        """

    def create_browser(
        self, **kwargs: Unpack[CreateBrowserRequestTypeDef]
    ) -> CreateBrowserResponseTypeDef:
        """
        Creates a custom browser.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_browser.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_browser)
        """

    def create_code_interpreter(
        self, **kwargs: Unpack[CreateCodeInterpreterRequestTypeDef]
    ) -> CreateCodeInterpreterResponseTypeDef:
        """
        Creates a custom code interpreter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_code_interpreter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_code_interpreter)
        """

    def create_evaluator(
        self, **kwargs: Unpack[CreateEvaluatorRequestTypeDef]
    ) -> CreateEvaluatorResponseTypeDef:
        """
        Creates a custom evaluator for agent quality assessment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_evaluator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_evaluator)
        """

    def create_gateway(
        self, **kwargs: Unpack[CreateGatewayRequestTypeDef]
    ) -> CreateGatewayResponseTypeDef:
        """
        Creates a gateway for Amazon Bedrock Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_gateway)
        """

    def create_gateway_target(
        self, **kwargs: Unpack[CreateGatewayTargetRequestTypeDef]
    ) -> CreateGatewayTargetResponseTypeDef:
        """
        Creates a target for a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_gateway_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_gateway_target)
        """

    def create_memory(
        self, **kwargs: Unpack[CreateMemoryInputTypeDef]
    ) -> CreateMemoryOutputTypeDef:
        """
        Creates a new Amazon Bedrock AgentCore Memory resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_memory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_memory)
        """

    def create_oauth2_credential_provider(
        self, **kwargs: Unpack[CreateOauth2CredentialProviderRequestTypeDef]
    ) -> CreateOauth2CredentialProviderResponseTypeDef:
        """
        Creates a new OAuth2 credential provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_oauth2_credential_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_oauth2_credential_provider)
        """

    def create_online_evaluation_config(
        self, **kwargs: Unpack[CreateOnlineEvaluationConfigRequestTypeDef]
    ) -> CreateOnlineEvaluationConfigResponseTypeDef:
        """
        Creates an online evaluation configuration for continuous monitoring of agent
        performance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_online_evaluation_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_online_evaluation_config)
        """

    def create_policy(
        self, **kwargs: Unpack[CreatePolicyRequestTypeDef]
    ) -> CreatePolicyResponseTypeDef:
        """
        Creates a policy within the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_policy)
        """

    def create_policy_engine(
        self, **kwargs: Unpack[CreatePolicyEngineRequestTypeDef]
    ) -> CreatePolicyEngineResponseTypeDef:
        """
        Creates a new policy engine within the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_policy_engine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_policy_engine)
        """

    def create_workload_identity(
        self, **kwargs: Unpack[CreateWorkloadIdentityRequestTypeDef]
    ) -> CreateWorkloadIdentityResponseTypeDef:
        """
        Creates a new workload identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/create_workload_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#create_workload_identity)
        """

    def delete_agent_runtime(
        self, **kwargs: Unpack[DeleteAgentRuntimeRequestTypeDef]
    ) -> DeleteAgentRuntimeResponseTypeDef:
        """
        Deletes an Amazon Bedrock AgentCore Runtime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_agent_runtime.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_agent_runtime)
        """

    def delete_agent_runtime_endpoint(
        self, **kwargs: Unpack[DeleteAgentRuntimeEndpointRequestTypeDef]
    ) -> DeleteAgentRuntimeEndpointResponseTypeDef:
        """
        Deletes an AAgentCore Runtime endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_agent_runtime_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_agent_runtime_endpoint)
        """

    def delete_api_key_credential_provider(
        self, **kwargs: Unpack[DeleteApiKeyCredentialProviderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an API key credential provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_api_key_credential_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_api_key_credential_provider)
        """

    def delete_browser(
        self, **kwargs: Unpack[DeleteBrowserRequestTypeDef]
    ) -> DeleteBrowserResponseTypeDef:
        """
        Deletes a custom browser.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_browser.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_browser)
        """

    def delete_code_interpreter(
        self, **kwargs: Unpack[DeleteCodeInterpreterRequestTypeDef]
    ) -> DeleteCodeInterpreterResponseTypeDef:
        """
        Deletes a custom code interpreter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_code_interpreter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_code_interpreter)
        """

    def delete_evaluator(
        self, **kwargs: Unpack[DeleteEvaluatorRequestTypeDef]
    ) -> DeleteEvaluatorResponseTypeDef:
        """
        Deletes a custom evaluator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_evaluator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_evaluator)
        """

    def delete_gateway(
        self, **kwargs: Unpack[DeleteGatewayRequestTypeDef]
    ) -> DeleteGatewayResponseTypeDef:
        """
        Deletes a gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_gateway)
        """

    def delete_gateway_target(
        self, **kwargs: Unpack[DeleteGatewayTargetRequestTypeDef]
    ) -> DeleteGatewayTargetResponseTypeDef:
        """
        Deletes a gateway target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_gateway_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_gateway_target)
        """

    def delete_memory(
        self, **kwargs: Unpack[DeleteMemoryInputTypeDef]
    ) -> DeleteMemoryOutputTypeDef:
        """
        Deletes an Amazon Bedrock AgentCore Memory resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_memory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_memory)
        """

    def delete_oauth2_credential_provider(
        self, **kwargs: Unpack[DeleteOauth2CredentialProviderRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes an OAuth2 credential provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_oauth2_credential_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_oauth2_credential_provider)
        """

    def delete_online_evaluation_config(
        self, **kwargs: Unpack[DeleteOnlineEvaluationConfigRequestTypeDef]
    ) -> DeleteOnlineEvaluationConfigResponseTypeDef:
        """
        Deletes an online evaluation configuration and stops any ongoing evaluation
        processes associated with it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_online_evaluation_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_online_evaluation_config)
        """

    def delete_policy(
        self, **kwargs: Unpack[DeletePolicyRequestTypeDef]
    ) -> DeletePolicyResponseTypeDef:
        """
        Deletes an existing policy from the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_policy)
        """

    def delete_policy_engine(
        self, **kwargs: Unpack[DeletePolicyEngineRequestTypeDef]
    ) -> DeletePolicyEngineResponseTypeDef:
        """
        Deletes an existing policy engine from the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_policy_engine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_policy_engine)
        """

    def delete_resource_policy(
        self, **kwargs: Unpack[DeleteResourcePolicyRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes the resource-based policy for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_resource_policy)
        """

    def delete_workload_identity(
        self, **kwargs: Unpack[DeleteWorkloadIdentityRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Deletes a workload identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/delete_workload_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#delete_workload_identity)
        """

    def get_agent_runtime(
        self, **kwargs: Unpack[GetAgentRuntimeRequestTypeDef]
    ) -> GetAgentRuntimeResponseTypeDef:
        """
        Gets an Amazon Bedrock AgentCore Runtime.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_agent_runtime.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_agent_runtime)
        """

    def get_agent_runtime_endpoint(
        self, **kwargs: Unpack[GetAgentRuntimeEndpointRequestTypeDef]
    ) -> GetAgentRuntimeEndpointResponseTypeDef:
        """
        Gets information about an Amazon Secure AgentEndpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_agent_runtime_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_agent_runtime_endpoint)
        """

    def get_api_key_credential_provider(
        self, **kwargs: Unpack[GetApiKeyCredentialProviderRequestTypeDef]
    ) -> GetApiKeyCredentialProviderResponseTypeDef:
        """
        Retrieves information about an API key credential provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_api_key_credential_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_api_key_credential_provider)
        """

    def get_browser(self, **kwargs: Unpack[GetBrowserRequestTypeDef]) -> GetBrowserResponseTypeDef:
        """
        Gets information about a custom browser.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_browser.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_browser)
        """

    def get_code_interpreter(
        self, **kwargs: Unpack[GetCodeInterpreterRequestTypeDef]
    ) -> GetCodeInterpreterResponseTypeDef:
        """
        Gets information about a custom code interpreter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_code_interpreter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_code_interpreter)
        """

    def get_evaluator(
        self, **kwargs: Unpack[GetEvaluatorRequestTypeDef]
    ) -> GetEvaluatorResponseTypeDef:
        """
        Retrieves detailed information about an evaluator, including its configuration,
        status, and metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_evaluator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_evaluator)
        """

    def get_gateway(self, **kwargs: Unpack[GetGatewayRequestTypeDef]) -> GetGatewayResponseTypeDef:
        """
        Retrieves information about a specific Gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_gateway)
        """

    def get_gateway_target(
        self, **kwargs: Unpack[GetGatewayTargetRequestTypeDef]
    ) -> GetGatewayTargetResponseTypeDef:
        """
        Retrieves information about a specific gateway target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_gateway_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_gateway_target)
        """

    def get_memory(self, **kwargs: Unpack[GetMemoryInputTypeDef]) -> GetMemoryOutputTypeDef:
        """
        Retrieve an existing Amazon Bedrock AgentCore Memory resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_memory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_memory)
        """

    def get_oauth2_credential_provider(
        self, **kwargs: Unpack[GetOauth2CredentialProviderRequestTypeDef]
    ) -> GetOauth2CredentialProviderResponseTypeDef:
        """
        Retrieves information about an OAuth2 credential provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_oauth2_credential_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_oauth2_credential_provider)
        """

    def get_online_evaluation_config(
        self, **kwargs: Unpack[GetOnlineEvaluationConfigRequestTypeDef]
    ) -> GetOnlineEvaluationConfigResponseTypeDef:
        """
        Retrieves detailed information about an online evaluation configuration,
        including its rules, data sources, evaluators, and execution status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_online_evaluation_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_online_evaluation_config)
        """

    def get_policy(self, **kwargs: Unpack[GetPolicyRequestTypeDef]) -> GetPolicyResponseTypeDef:
        """
        Retrieves detailed information about a specific policy within the AgentCore
        Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_policy)
        """

    def get_policy_engine(
        self, **kwargs: Unpack[GetPolicyEngineRequestTypeDef]
    ) -> GetPolicyEngineResponseTypeDef:
        """
        Retrieves detailed information about a specific policy engine within the
        AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_policy_engine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_policy_engine)
        """

    def get_policy_generation(
        self, **kwargs: Unpack[GetPolicyGenerationRequestTypeDef]
    ) -> GetPolicyGenerationResponseTypeDef:
        """
        Retrieves information about a policy generation request within the AgentCore
        Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_policy_generation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_policy_generation)
        """

    def get_resource_policy(
        self, **kwargs: Unpack[GetResourcePolicyRequestTypeDef]
    ) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves the resource-based policy for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_resource_policy)
        """

    def get_token_vault(
        self, **kwargs: Unpack[GetTokenVaultRequestTypeDef]
    ) -> GetTokenVaultResponseTypeDef:
        """
        Retrieves information about a token vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_token_vault.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_token_vault)
        """

    def get_workload_identity(
        self, **kwargs: Unpack[GetWorkloadIdentityRequestTypeDef]
    ) -> GetWorkloadIdentityResponseTypeDef:
        """
        Retrieves information about a workload identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_workload_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_workload_identity)
        """

    def list_agent_runtime_endpoints(
        self, **kwargs: Unpack[ListAgentRuntimeEndpointsRequestTypeDef]
    ) -> ListAgentRuntimeEndpointsResponseTypeDef:
        """
        Lists all endpoints for a specific Amazon Secure Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_agent_runtime_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_agent_runtime_endpoints)
        """

    def list_agent_runtime_versions(
        self, **kwargs: Unpack[ListAgentRuntimeVersionsRequestTypeDef]
    ) -> ListAgentRuntimeVersionsResponseTypeDef:
        """
        Lists all versions of a specific Amazon Secure Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_agent_runtime_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_agent_runtime_versions)
        """

    def list_agent_runtimes(
        self, **kwargs: Unpack[ListAgentRuntimesRequestTypeDef]
    ) -> ListAgentRuntimesResponseTypeDef:
        """
        Lists all Amazon Secure Agents in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_agent_runtimes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_agent_runtimes)
        """

    def list_api_key_credential_providers(
        self, **kwargs: Unpack[ListApiKeyCredentialProvidersRequestTypeDef]
    ) -> ListApiKeyCredentialProvidersResponseTypeDef:
        """
        Lists all API key credential providers in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_api_key_credential_providers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_api_key_credential_providers)
        """

    def list_browsers(
        self, **kwargs: Unpack[ListBrowsersRequestTypeDef]
    ) -> ListBrowsersResponseTypeDef:
        """
        Lists all custom browsers in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_browsers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_browsers)
        """

    def list_code_interpreters(
        self, **kwargs: Unpack[ListCodeInterpretersRequestTypeDef]
    ) -> ListCodeInterpretersResponseTypeDef:
        """
        Lists all custom code interpreters in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_code_interpreters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_code_interpreters)
        """

    def list_evaluators(
        self, **kwargs: Unpack[ListEvaluatorsRequestTypeDef]
    ) -> ListEvaluatorsResponseTypeDef:
        """
        Lists all available evaluators, including both builtin evaluators provided by
        the service and custom evaluators created by the user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_evaluators.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_evaluators)
        """

    def list_gateway_targets(
        self, **kwargs: Unpack[ListGatewayTargetsRequestTypeDef]
    ) -> ListGatewayTargetsResponseTypeDef:
        """
        Lists all targets for a specific gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_gateway_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_gateway_targets)
        """

    def list_gateways(
        self, **kwargs: Unpack[ListGatewaysRequestTypeDef]
    ) -> ListGatewaysResponseTypeDef:
        """
        Lists all gateways in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_gateways)
        """

    def list_memories(
        self, **kwargs: Unpack[ListMemoriesInputTypeDef]
    ) -> ListMemoriesOutputTypeDef:
        """
        Lists the available Amazon Bedrock AgentCore Memory resources in the current
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_memories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_memories)
        """

    def list_oauth2_credential_providers(
        self, **kwargs: Unpack[ListOauth2CredentialProvidersRequestTypeDef]
    ) -> ListOauth2CredentialProvidersResponseTypeDef:
        """
        Lists all OAuth2 credential providers in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_oauth2_credential_providers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_oauth2_credential_providers)
        """

    def list_online_evaluation_configs(
        self, **kwargs: Unpack[ListOnlineEvaluationConfigsRequestTypeDef]
    ) -> ListOnlineEvaluationConfigsResponseTypeDef:
        """
        Lists all online evaluation configurations in the account, providing summary
        information about each configuration's status and settings.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_online_evaluation_configs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_online_evaluation_configs)
        """

    def list_policies(
        self, **kwargs: Unpack[ListPoliciesRequestTypeDef]
    ) -> ListPoliciesResponseTypeDef:
        """
        Retrieves a list of policies within the AgentCore Policy engine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_policies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_policies)
        """

    def list_policy_engines(
        self, **kwargs: Unpack[ListPolicyEnginesRequestTypeDef]
    ) -> ListPolicyEnginesResponseTypeDef:
        """
        Retrieves a list of policy engines within the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_policy_engines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_policy_engines)
        """

    def list_policy_generation_assets(
        self, **kwargs: Unpack[ListPolicyGenerationAssetsRequestTypeDef]
    ) -> ListPolicyGenerationAssetsResponseTypeDef:
        """
        Retrieves a list of generated policy assets from a policy generation request
        within the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_policy_generation_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_policy_generation_assets)
        """

    def list_policy_generations(
        self, **kwargs: Unpack[ListPolicyGenerationsRequestTypeDef]
    ) -> ListPolicyGenerationsResponseTypeDef:
        """
        Retrieves a list of policy generation requests within the AgentCore Policy
        system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_policy_generations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_policy_generations)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags associated with the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_tags_for_resource)
        """

    def list_workload_identities(
        self, **kwargs: Unpack[ListWorkloadIdentitiesRequestTypeDef]
    ) -> ListWorkloadIdentitiesResponseTypeDef:
        """
        Lists all workload identities in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/list_workload_identities.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#list_workload_identities)
        """

    def put_resource_policy(
        self, **kwargs: Unpack[PutResourcePolicyRequestTypeDef]
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates a resource-based policy for a resource with the specified
        resourceArn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/put_resource_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#put_resource_policy)
        """

    def set_token_vault_cmk(
        self, **kwargs: Unpack[SetTokenVaultCMKRequestTypeDef]
    ) -> SetTokenVaultCMKResponseTypeDef:
        """
        Sets the customer master key (CMK) for a token vault.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/set_token_vault_cmk.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#set_token_vault_cmk)
        """

    def start_policy_generation(
        self, **kwargs: Unpack[StartPolicyGenerationRequestTypeDef]
    ) -> StartPolicyGenerationResponseTypeDef:
        """
        Initiates the AI-powered generation of Cedar policies from natural language
        descriptions within the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/start_policy_generation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#start_policy_generation)
        """

    def synchronize_gateway_targets(
        self, **kwargs: Unpack[SynchronizeGatewayTargetsRequestTypeDef]
    ) -> SynchronizeGatewayTargetsResponseTypeDef:
        """
        The gateway targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/synchronize_gateway_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#synchronize_gateway_targets)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Associates the specified tags to a resource with the specified resourceArn.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#untag_resource)
        """

    def update_agent_runtime(
        self, **kwargs: Unpack[UpdateAgentRuntimeRequestTypeDef]
    ) -> UpdateAgentRuntimeResponseTypeDef:
        """
        Updates an existing Amazon Secure Agent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_agent_runtime.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_agent_runtime)
        """

    def update_agent_runtime_endpoint(
        self, **kwargs: Unpack[UpdateAgentRuntimeEndpointRequestTypeDef]
    ) -> UpdateAgentRuntimeEndpointResponseTypeDef:
        """
        Updates an existing Amazon Bedrock AgentCore Runtime endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_agent_runtime_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_agent_runtime_endpoint)
        """

    def update_api_key_credential_provider(
        self, **kwargs: Unpack[UpdateApiKeyCredentialProviderRequestTypeDef]
    ) -> UpdateApiKeyCredentialProviderResponseTypeDef:
        """
        Updates an existing API key credential provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_api_key_credential_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_api_key_credential_provider)
        """

    def update_evaluator(
        self, **kwargs: Unpack[UpdateEvaluatorRequestTypeDef]
    ) -> UpdateEvaluatorResponseTypeDef:
        """
        Updates a custom evaluator's configuration, description, or evaluation level.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_evaluator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_evaluator)
        """

    def update_gateway(
        self, **kwargs: Unpack[UpdateGatewayRequestTypeDef]
    ) -> UpdateGatewayResponseTypeDef:
        """
        Updates an existing gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_gateway)
        """

    def update_gateway_target(
        self, **kwargs: Unpack[UpdateGatewayTargetRequestTypeDef]
    ) -> UpdateGatewayTargetResponseTypeDef:
        """
        Updates an existing gateway target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_gateway_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_gateway_target)
        """

    def update_memory(
        self, **kwargs: Unpack[UpdateMemoryInputTypeDef]
    ) -> UpdateMemoryOutputTypeDef:
        """
        Update an Amazon Bedrock AgentCore Memory resource memory.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_memory.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_memory)
        """

    def update_oauth2_credential_provider(
        self, **kwargs: Unpack[UpdateOauth2CredentialProviderRequestTypeDef]
    ) -> UpdateOauth2CredentialProviderResponseTypeDef:
        """
        Updates an existing OAuth2 credential provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_oauth2_credential_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_oauth2_credential_provider)
        """

    def update_online_evaluation_config(
        self, **kwargs: Unpack[UpdateOnlineEvaluationConfigRequestTypeDef]
    ) -> UpdateOnlineEvaluationConfigResponseTypeDef:
        """
        Updates an online evaluation configuration's settings, including rules, data
        sources, evaluators, and execution status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_online_evaluation_config.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_online_evaluation_config)
        """

    def update_policy(
        self, **kwargs: Unpack[UpdatePolicyRequestTypeDef]
    ) -> UpdatePolicyResponseTypeDef:
        """
        Updates an existing policy within the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_policy)
        """

    def update_policy_engine(
        self, **kwargs: Unpack[UpdatePolicyEngineRequestTypeDef]
    ) -> UpdatePolicyEngineResponseTypeDef:
        """
        Updates an existing policy engine within the AgentCore Policy system.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_policy_engine.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_policy_engine)
        """

    def update_workload_identity(
        self, **kwargs: Unpack[UpdateWorkloadIdentityRequestTypeDef]
    ) -> UpdateWorkloadIdentityResponseTypeDef:
        """
        Updates an existing workload identity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/update_workload_identity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#update_workload_identity)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_runtime_endpoints"]
    ) -> ListAgentRuntimeEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_runtime_versions"]
    ) -> ListAgentRuntimeVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_agent_runtimes"]
    ) -> ListAgentRuntimesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_api_key_credential_providers"]
    ) -> ListApiKeyCredentialProvidersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_browsers"]
    ) -> ListBrowsersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_code_interpreters"]
    ) -> ListCodeInterpretersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_evaluators"]
    ) -> ListEvaluatorsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_gateway_targets"]
    ) -> ListGatewayTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_gateways"]
    ) -> ListGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_memories"]
    ) -> ListMemoriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_oauth2_credential_providers"]
    ) -> ListOauth2CredentialProvidersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_online_evaluation_configs"]
    ) -> ListOnlineEvaluationConfigsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policies"]
    ) -> ListPoliciesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_engines"]
    ) -> ListPolicyEnginesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_generation_assets"]
    ) -> ListPolicyGenerationAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_policy_generations"]
    ) -> ListPolicyGenerationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_workload_identities"]
    ) -> ListWorkloadIdentitiesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["memory_created"]
    ) -> MemoryCreatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["policy_active"]
    ) -> PolicyActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["policy_deleted"]
    ) -> PolicyDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["policy_engine_active"]
    ) -> PolicyEngineActiveWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["policy_engine_deleted"]
    ) -> PolicyEngineDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["policy_generation_completed"]
    ) -> PolicyGenerationCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/client/#get_waiter)
        """
