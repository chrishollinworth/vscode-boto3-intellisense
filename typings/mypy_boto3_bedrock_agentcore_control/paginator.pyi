"""
Type annotations for bedrock-agentcore-control service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_bedrock_agentcore_control.client import BedrockAgentCoreControlClient
    from mypy_boto3_bedrock_agentcore_control.paginator import (
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
    )

    session = Session()
    client: BedrockAgentCoreControlClient = session.client("bedrock-agentcore-control")

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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAgentRuntimeEndpointsRequestPaginateTypeDef,
    ListAgentRuntimeEndpointsResponseTypeDef,
    ListAgentRuntimesRequestPaginateTypeDef,
    ListAgentRuntimesResponseTypeDef,
    ListAgentRuntimeVersionsRequestPaginateTypeDef,
    ListAgentRuntimeVersionsResponseTypeDef,
    ListApiKeyCredentialProvidersRequestPaginateTypeDef,
    ListApiKeyCredentialProvidersResponseTypeDef,
    ListBrowsersRequestPaginateTypeDef,
    ListBrowsersResponseTypeDef,
    ListCodeInterpretersRequestPaginateTypeDef,
    ListCodeInterpretersResponseTypeDef,
    ListEvaluatorsRequestPaginateTypeDef,
    ListEvaluatorsResponseTypeDef,
    ListGatewaysRequestPaginateTypeDef,
    ListGatewaysResponseTypeDef,
    ListGatewayTargetsRequestPaginateTypeDef,
    ListGatewayTargetsResponseTypeDef,
    ListMemoriesInputPaginateTypeDef,
    ListMemoriesOutputTypeDef,
    ListOauth2CredentialProvidersRequestPaginateTypeDef,
    ListOauth2CredentialProvidersResponseTypeDef,
    ListOnlineEvaluationConfigsRequestPaginateTypeDef,
    ListOnlineEvaluationConfigsResponseTypeDef,
    ListPoliciesRequestPaginateTypeDef,
    ListPoliciesResponseTypeDef,
    ListPolicyEnginesRequestPaginateTypeDef,
    ListPolicyEnginesResponseTypeDef,
    ListPolicyGenerationAssetsRequestPaginateTypeDef,
    ListPolicyGenerationAssetsResponseTypeDef,
    ListPolicyGenerationsRequestPaginateTypeDef,
    ListPolicyGenerationsResponseTypeDef,
    ListWorkloadIdentitiesRequestPaginateTypeDef,
    ListWorkloadIdentitiesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
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
)

if TYPE_CHECKING:
    _ListAgentRuntimeEndpointsPaginatorBase = Paginator[ListAgentRuntimeEndpointsResponseTypeDef]
else:
    _ListAgentRuntimeEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentRuntimeEndpointsPaginator(_ListAgentRuntimeEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListAgentRuntimeEndpoints.html#BedrockAgentCoreControl.Paginator.ListAgentRuntimeEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listagentruntimeendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentRuntimeEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentRuntimeEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListAgentRuntimeEndpoints.html#BedrockAgentCoreControl.Paginator.ListAgentRuntimeEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listagentruntimeendpointspaginator)
        """

if TYPE_CHECKING:
    _ListAgentRuntimeVersionsPaginatorBase = Paginator[ListAgentRuntimeVersionsResponseTypeDef]
else:
    _ListAgentRuntimeVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentRuntimeVersionsPaginator(_ListAgentRuntimeVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListAgentRuntimeVersions.html#BedrockAgentCoreControl.Paginator.ListAgentRuntimeVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listagentruntimeversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentRuntimeVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentRuntimeVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListAgentRuntimeVersions.html#BedrockAgentCoreControl.Paginator.ListAgentRuntimeVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listagentruntimeversionspaginator)
        """

if TYPE_CHECKING:
    _ListAgentRuntimesPaginatorBase = Paginator[ListAgentRuntimesResponseTypeDef]
else:
    _ListAgentRuntimesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAgentRuntimesPaginator(_ListAgentRuntimesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListAgentRuntimes.html#BedrockAgentCoreControl.Paginator.ListAgentRuntimes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listagentruntimespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAgentRuntimesRequestPaginateTypeDef]
    ) -> PageIterator[ListAgentRuntimesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListAgentRuntimes.html#BedrockAgentCoreControl.Paginator.ListAgentRuntimes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listagentruntimespaginator)
        """

if TYPE_CHECKING:
    _ListApiKeyCredentialProvidersPaginatorBase = Paginator[
        ListApiKeyCredentialProvidersResponseTypeDef
    ]
else:
    _ListApiKeyCredentialProvidersPaginatorBase = Paginator  # type: ignore[assignment]

class ListApiKeyCredentialProvidersPaginator(_ListApiKeyCredentialProvidersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListApiKeyCredentialProviders.html#BedrockAgentCoreControl.Paginator.ListApiKeyCredentialProviders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listapikeycredentialproviderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApiKeyCredentialProvidersRequestPaginateTypeDef]
    ) -> PageIterator[ListApiKeyCredentialProvidersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListApiKeyCredentialProviders.html#BedrockAgentCoreControl.Paginator.ListApiKeyCredentialProviders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listapikeycredentialproviderspaginator)
        """

if TYPE_CHECKING:
    _ListBrowsersPaginatorBase = Paginator[ListBrowsersResponseTypeDef]
else:
    _ListBrowsersPaginatorBase = Paginator  # type: ignore[assignment]

class ListBrowsersPaginator(_ListBrowsersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListBrowsers.html#BedrockAgentCoreControl.Paginator.ListBrowsers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listbrowserspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBrowsersRequestPaginateTypeDef]
    ) -> PageIterator[ListBrowsersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListBrowsers.html#BedrockAgentCoreControl.Paginator.ListBrowsers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listbrowserspaginator)
        """

if TYPE_CHECKING:
    _ListCodeInterpretersPaginatorBase = Paginator[ListCodeInterpretersResponseTypeDef]
else:
    _ListCodeInterpretersPaginatorBase = Paginator  # type: ignore[assignment]

class ListCodeInterpretersPaginator(_ListCodeInterpretersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListCodeInterpreters.html#BedrockAgentCoreControl.Paginator.ListCodeInterpreters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listcodeinterpreterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListCodeInterpretersRequestPaginateTypeDef]
    ) -> PageIterator[ListCodeInterpretersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListCodeInterpreters.html#BedrockAgentCoreControl.Paginator.ListCodeInterpreters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listcodeinterpreterspaginator)
        """

if TYPE_CHECKING:
    _ListEvaluatorsPaginatorBase = Paginator[ListEvaluatorsResponseTypeDef]
else:
    _ListEvaluatorsPaginatorBase = Paginator  # type: ignore[assignment]

class ListEvaluatorsPaginator(_ListEvaluatorsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListEvaluators.html#BedrockAgentCoreControl.Paginator.ListEvaluators)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listevaluatorspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListEvaluatorsRequestPaginateTypeDef]
    ) -> PageIterator[ListEvaluatorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListEvaluators.html#BedrockAgentCoreControl.Paginator.ListEvaluators.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listevaluatorspaginator)
        """

if TYPE_CHECKING:
    _ListGatewayTargetsPaginatorBase = Paginator[ListGatewayTargetsResponseTypeDef]
else:
    _ListGatewayTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListGatewayTargetsPaginator(_ListGatewayTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListGatewayTargets.html#BedrockAgentCoreControl.Paginator.ListGatewayTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listgatewaytargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGatewayTargetsRequestPaginateTypeDef]
    ) -> PageIterator[ListGatewayTargetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListGatewayTargets.html#BedrockAgentCoreControl.Paginator.ListGatewayTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listgatewaytargetspaginator)
        """

if TYPE_CHECKING:
    _ListGatewaysPaginatorBase = Paginator[ListGatewaysResponseTypeDef]
else:
    _ListGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class ListGatewaysPaginator(_ListGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListGateways.html#BedrockAgentCoreControl.Paginator.ListGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[ListGatewaysResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListGateways.html#BedrockAgentCoreControl.Paginator.ListGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listgatewayspaginator)
        """

if TYPE_CHECKING:
    _ListMemoriesPaginatorBase = Paginator[ListMemoriesOutputTypeDef]
else:
    _ListMemoriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListMemoriesPaginator(_ListMemoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListMemories.html#BedrockAgentCoreControl.Paginator.ListMemories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listmemoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMemoriesInputPaginateTypeDef]
    ) -> PageIterator[ListMemoriesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListMemories.html#BedrockAgentCoreControl.Paginator.ListMemories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listmemoriespaginator)
        """

if TYPE_CHECKING:
    _ListOauth2CredentialProvidersPaginatorBase = Paginator[
        ListOauth2CredentialProvidersResponseTypeDef
    ]
else:
    _ListOauth2CredentialProvidersPaginatorBase = Paginator  # type: ignore[assignment]

class ListOauth2CredentialProvidersPaginator(_ListOauth2CredentialProvidersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListOauth2CredentialProviders.html#BedrockAgentCoreControl.Paginator.ListOauth2CredentialProviders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listoauth2credentialproviderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOauth2CredentialProvidersRequestPaginateTypeDef]
    ) -> PageIterator[ListOauth2CredentialProvidersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListOauth2CredentialProviders.html#BedrockAgentCoreControl.Paginator.ListOauth2CredentialProviders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listoauth2credentialproviderspaginator)
        """

if TYPE_CHECKING:
    _ListOnlineEvaluationConfigsPaginatorBase = Paginator[
        ListOnlineEvaluationConfigsResponseTypeDef
    ]
else:
    _ListOnlineEvaluationConfigsPaginatorBase = Paginator  # type: ignore[assignment]

class ListOnlineEvaluationConfigsPaginator(_ListOnlineEvaluationConfigsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListOnlineEvaluationConfigs.html#BedrockAgentCoreControl.Paginator.ListOnlineEvaluationConfigs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listonlineevaluationconfigspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListOnlineEvaluationConfigsRequestPaginateTypeDef]
    ) -> PageIterator[ListOnlineEvaluationConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListOnlineEvaluationConfigs.html#BedrockAgentCoreControl.Paginator.ListOnlineEvaluationConfigs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listonlineevaluationconfigspaginator)
        """

if TYPE_CHECKING:
    _ListPoliciesPaginatorBase = Paginator[ListPoliciesResponseTypeDef]
else:
    _ListPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPoliciesPaginator(_ListPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListPolicies.html#BedrockAgentCoreControl.Paginator.ListPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListPolicies.html#BedrockAgentCoreControl.Paginator.ListPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListPolicyEnginesPaginatorBase = Paginator[ListPolicyEnginesResponseTypeDef]
else:
    _ListPolicyEnginesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyEnginesPaginator(_ListPolicyEnginesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListPolicyEngines.html#BedrockAgentCoreControl.Paginator.ListPolicyEngines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listpolicyenginespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyEnginesRequestPaginateTypeDef]
    ) -> PageIterator[ListPolicyEnginesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListPolicyEngines.html#BedrockAgentCoreControl.Paginator.ListPolicyEngines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listpolicyenginespaginator)
        """

if TYPE_CHECKING:
    _ListPolicyGenerationAssetsPaginatorBase = Paginator[ListPolicyGenerationAssetsResponseTypeDef]
else:
    _ListPolicyGenerationAssetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyGenerationAssetsPaginator(_ListPolicyGenerationAssetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListPolicyGenerationAssets.html#BedrockAgentCoreControl.Paginator.ListPolicyGenerationAssets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listpolicygenerationassetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyGenerationAssetsRequestPaginateTypeDef]
    ) -> PageIterator[ListPolicyGenerationAssetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListPolicyGenerationAssets.html#BedrockAgentCoreControl.Paginator.ListPolicyGenerationAssets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listpolicygenerationassetspaginator)
        """

if TYPE_CHECKING:
    _ListPolicyGenerationsPaginatorBase = Paginator[ListPolicyGenerationsResponseTypeDef]
else:
    _ListPolicyGenerationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPolicyGenerationsPaginator(_ListPolicyGenerationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListPolicyGenerations.html#BedrockAgentCoreControl.Paginator.ListPolicyGenerations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listpolicygenerationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPolicyGenerationsRequestPaginateTypeDef]
    ) -> PageIterator[ListPolicyGenerationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListPolicyGenerations.html#BedrockAgentCoreControl.Paginator.ListPolicyGenerations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listpolicygenerationspaginator)
        """

if TYPE_CHECKING:
    _ListWorkloadIdentitiesPaginatorBase = Paginator[ListWorkloadIdentitiesResponseTypeDef]
else:
    _ListWorkloadIdentitiesPaginatorBase = Paginator  # type: ignore[assignment]

class ListWorkloadIdentitiesPaginator(_ListWorkloadIdentitiesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListWorkloadIdentities.html#BedrockAgentCoreControl.Paginator.ListWorkloadIdentities)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listworkloadidentitiespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListWorkloadIdentitiesRequestPaginateTypeDef]
    ) -> PageIterator[ListWorkloadIdentitiesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agentcore-control/paginator/ListWorkloadIdentities.html#BedrockAgentCoreControl.Paginator.ListWorkloadIdentities.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/paginators/#listworkloadidentitiespaginator)
        """
