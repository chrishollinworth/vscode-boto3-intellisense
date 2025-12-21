"""
Type annotations for bedrock-agentcore-control service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_agentcore_control/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bedrock_agentcore_control.type_defs import ContainerConfigurationTypeDef

    data: ContainerConfigurationTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AgentManagedRuntimeTypeType,
    AgentRuntimeEndpointStatusType,
    AgentRuntimeStatusType,
    ApiKeyCredentialLocationType,
    AuthorizerTypeType,
    BrowserNetworkModeType,
    BrowserStatusType,
    ClaimMatchOperatorTypeType,
    CodeInterpreterNetworkModeType,
    CodeInterpreterStatusType,
    CredentialProviderTypeType,
    CredentialProviderVendorTypeType,
    EvaluatorLevelType,
    EvaluatorStatusType,
    EvaluatorTypeType,
    FilterOperatorType,
    FindingTypeType,
    GatewayInterceptionPointType,
    GatewayPolicyEngineModeType,
    GatewayStatusType,
    InboundTokenClaimValueTypeType,
    KeyTypeType,
    MemoryStatusType,
    MemoryStrategyStatusType,
    MemoryStrategyTypeType,
    NetworkModeType,
    OAuthGrantTypeType,
    OnlineEvaluationConfigStatusType,
    OnlineEvaluationExecutionStatusType,
    OverrideTypeType,
    PolicyEngineStatusType,
    PolicyGenerationStatusType,
    PolicyStatusType,
    PolicyValidationModeType,
    ResourceTypeType,
    RestApiMethodType,
    SchemaTypeType,
    ServerProtocolType,
    TargetStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AgentRuntimeArtifactOutputTypeDef",
    "AgentRuntimeArtifactTypeDef",
    "AgentRuntimeArtifactUnionTypeDef",
    "AgentRuntimeEndpointTypeDef",
    "AgentRuntimeTypeDef",
    "ApiGatewayTargetConfigurationOutputTypeDef",
    "ApiGatewayTargetConfigurationTypeDef",
    "ApiGatewayToolConfigurationOutputTypeDef",
    "ApiGatewayToolConfigurationTypeDef",
    "ApiGatewayToolFilterOutputTypeDef",
    "ApiGatewayToolFilterTypeDef",
    "ApiGatewayToolOverrideTypeDef",
    "ApiKeyCredentialProviderItemTypeDef",
    "ApiKeyCredentialProviderTypeDef",
    "ApiSchemaConfigurationTypeDef",
    "AtlassianOauth2ProviderConfigInputTypeDef",
    "AtlassianOauth2ProviderConfigOutputTypeDef",
    "AuthorizerConfigurationOutputTypeDef",
    "AuthorizerConfigurationTypeDef",
    "AuthorizerConfigurationUnionTypeDef",
    "AuthorizingClaimMatchValueTypeOutputTypeDef",
    "AuthorizingClaimMatchValueTypeTypeDef",
    "BedrockEvaluatorModelConfigOutputTypeDef",
    "BedrockEvaluatorModelConfigTypeDef",
    "BrowserNetworkConfigurationOutputTypeDef",
    "BrowserNetworkConfigurationTypeDef",
    "BrowserNetworkConfigurationUnionTypeDef",
    "BrowserSigningConfigInputTypeDef",
    "BrowserSigningConfigOutputTypeDef",
    "BrowserSummaryTypeDef",
    "CategoricalScaleDefinitionTypeDef",
    "CedarPolicyTypeDef",
    "ClaimMatchValueTypeOutputTypeDef",
    "ClaimMatchValueTypeTypeDef",
    "CloudWatchLogsInputConfigOutputTypeDef",
    "CloudWatchLogsInputConfigTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CodeConfigurationOutputTypeDef",
    "CodeConfigurationTypeDef",
    "CodeInterpreterNetworkConfigurationOutputTypeDef",
    "CodeInterpreterNetworkConfigurationTypeDef",
    "CodeInterpreterNetworkConfigurationUnionTypeDef",
    "CodeInterpreterSummaryTypeDef",
    "CodeTypeDef",
    "ConsolidationConfigurationTypeDef",
    "ContainerConfigurationTypeDef",
    "ContentTypeDef",
    "CreateAgentRuntimeEndpointRequestTypeDef",
    "CreateAgentRuntimeEndpointResponseTypeDef",
    "CreateAgentRuntimeRequestTypeDef",
    "CreateAgentRuntimeResponseTypeDef",
    "CreateApiKeyCredentialProviderRequestTypeDef",
    "CreateApiKeyCredentialProviderResponseTypeDef",
    "CreateBrowserRequestTypeDef",
    "CreateBrowserResponseTypeDef",
    "CreateCodeInterpreterRequestTypeDef",
    "CreateCodeInterpreterResponseTypeDef",
    "CreateEvaluatorRequestTypeDef",
    "CreateEvaluatorResponseTypeDef",
    "CreateGatewayRequestTypeDef",
    "CreateGatewayResponseTypeDef",
    "CreateGatewayTargetRequestTypeDef",
    "CreateGatewayTargetResponseTypeDef",
    "CreateMemoryInputTypeDef",
    "CreateMemoryOutputTypeDef",
    "CreateOauth2CredentialProviderRequestTypeDef",
    "CreateOauth2CredentialProviderResponseTypeDef",
    "CreateOnlineEvaluationConfigRequestTypeDef",
    "CreateOnlineEvaluationConfigResponseTypeDef",
    "CreatePolicyEngineRequestTypeDef",
    "CreatePolicyEngineResponseTypeDef",
    "CreatePolicyRequestTypeDef",
    "CreatePolicyResponseTypeDef",
    "CreateWorkloadIdentityRequestTypeDef",
    "CreateWorkloadIdentityResponseTypeDef",
    "CredentialProviderConfigurationOutputTypeDef",
    "CredentialProviderConfigurationTypeDef",
    "CredentialProviderConfigurationUnionTypeDef",
    "CredentialProviderOutputTypeDef",
    "CredentialProviderTypeDef",
    "CredentialProviderUnionTypeDef",
    "CustomClaimValidationTypeOutputTypeDef",
    "CustomClaimValidationTypeTypeDef",
    "CustomConfigurationInputTypeDef",
    "CustomConsolidationConfigurationInputTypeDef",
    "CustomConsolidationConfigurationTypeDef",
    "CustomExtractionConfigurationInputTypeDef",
    "CustomExtractionConfigurationTypeDef",
    "CustomJWTAuthorizerConfigurationOutputTypeDef",
    "CustomJWTAuthorizerConfigurationTypeDef",
    "CustomMemoryStrategyInputTypeDef",
    "CustomOauth2ProviderConfigInputTypeDef",
    "CustomOauth2ProviderConfigOutputTypeDef",
    "CustomReflectionConfigurationInputTypeDef",
    "CustomReflectionConfigurationTypeDef",
    "DataSourceConfigOutputTypeDef",
    "DataSourceConfigTypeDef",
    "DataSourceConfigUnionTypeDef",
    "DeleteAgentRuntimeEndpointRequestTypeDef",
    "DeleteAgentRuntimeEndpointResponseTypeDef",
    "DeleteAgentRuntimeRequestTypeDef",
    "DeleteAgentRuntimeResponseTypeDef",
    "DeleteApiKeyCredentialProviderRequestTypeDef",
    "DeleteBrowserRequestTypeDef",
    "DeleteBrowserResponseTypeDef",
    "DeleteCodeInterpreterRequestTypeDef",
    "DeleteCodeInterpreterResponseTypeDef",
    "DeleteEvaluatorRequestTypeDef",
    "DeleteEvaluatorResponseTypeDef",
    "DeleteGatewayRequestTypeDef",
    "DeleteGatewayResponseTypeDef",
    "DeleteGatewayTargetRequestTypeDef",
    "DeleteGatewayTargetResponseTypeDef",
    "DeleteMemoryInputTypeDef",
    "DeleteMemoryOutputTypeDef",
    "DeleteMemoryStrategyInputTypeDef",
    "DeleteOauth2CredentialProviderRequestTypeDef",
    "DeleteOnlineEvaluationConfigRequestTypeDef",
    "DeleteOnlineEvaluationConfigResponseTypeDef",
    "DeletePolicyEngineRequestTypeDef",
    "DeletePolicyEngineResponseTypeDef",
    "DeletePolicyRequestTypeDef",
    "DeletePolicyResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteWorkloadIdentityRequestTypeDef",
    "EpisodicConsolidationOverrideTypeDef",
    "EpisodicExtractionOverrideTypeDef",
    "EpisodicMemoryStrategyInputTypeDef",
    "EpisodicOverrideConfigurationInputTypeDef",
    "EpisodicOverrideConsolidationConfigurationInputTypeDef",
    "EpisodicOverrideExtractionConfigurationInputTypeDef",
    "EpisodicOverrideReflectionConfigurationInputTypeDef",
    "EpisodicReflectionConfigurationInputTypeDef",
    "EpisodicReflectionConfigurationTypeDef",
    "EpisodicReflectionOverrideTypeDef",
    "EvaluatorConfigOutputTypeDef",
    "EvaluatorConfigTypeDef",
    "EvaluatorConfigUnionTypeDef",
    "EvaluatorModelConfigOutputTypeDef",
    "EvaluatorModelConfigTypeDef",
    "EvaluatorReferenceTypeDef",
    "EvaluatorSummaryTypeDef",
    "ExtractionConfigurationTypeDef",
    "FilterTypeDef",
    "FilterValueTypeDef",
    "FindingTypeDef",
    "GatewayInterceptorConfigurationOutputTypeDef",
    "GatewayInterceptorConfigurationTypeDef",
    "GatewayInterceptorConfigurationUnionTypeDef",
    "GatewayPolicyEngineConfigurationTypeDef",
    "GatewayProtocolConfigurationOutputTypeDef",
    "GatewayProtocolConfigurationTypeDef",
    "GatewayProtocolConfigurationUnionTypeDef",
    "GatewaySummaryTypeDef",
    "GatewayTargetTypeDef",
    "GetAgentRuntimeEndpointRequestTypeDef",
    "GetAgentRuntimeEndpointResponseTypeDef",
    "GetAgentRuntimeRequestTypeDef",
    "GetAgentRuntimeResponseTypeDef",
    "GetApiKeyCredentialProviderRequestTypeDef",
    "GetApiKeyCredentialProviderResponseTypeDef",
    "GetBrowserRequestTypeDef",
    "GetBrowserResponseTypeDef",
    "GetCodeInterpreterRequestTypeDef",
    "GetCodeInterpreterResponseTypeDef",
    "GetEvaluatorRequestTypeDef",
    "GetEvaluatorResponseTypeDef",
    "GetGatewayRequestTypeDef",
    "GetGatewayResponseTypeDef",
    "GetGatewayTargetRequestTypeDef",
    "GetGatewayTargetResponseTypeDef",
    "GetMemoryInputTypeDef",
    "GetMemoryInputWaitTypeDef",
    "GetMemoryOutputTypeDef",
    "GetOauth2CredentialProviderRequestTypeDef",
    "GetOauth2CredentialProviderResponseTypeDef",
    "GetOnlineEvaluationConfigRequestTypeDef",
    "GetOnlineEvaluationConfigResponseTypeDef",
    "GetPolicyEngineRequestTypeDef",
    "GetPolicyEngineRequestWaitExtraTypeDef",
    "GetPolicyEngineRequestWaitTypeDef",
    "GetPolicyEngineResponseTypeDef",
    "GetPolicyGenerationRequestTypeDef",
    "GetPolicyGenerationRequestWaitTypeDef",
    "GetPolicyGenerationResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyRequestWaitExtraTypeDef",
    "GetPolicyRequestWaitTypeDef",
    "GetPolicyResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetTokenVaultRequestTypeDef",
    "GetTokenVaultResponseTypeDef",
    "GetWorkloadIdentityRequestTypeDef",
    "GetWorkloadIdentityResponseTypeDef",
    "GithubOauth2ProviderConfigInputTypeDef",
    "GithubOauth2ProviderConfigOutputTypeDef",
    "GoogleOauth2ProviderConfigInputTypeDef",
    "GoogleOauth2ProviderConfigOutputTypeDef",
    "IncludedOauth2ProviderConfigInputTypeDef",
    "IncludedOauth2ProviderConfigOutputTypeDef",
    "InferenceConfigurationOutputTypeDef",
    "InferenceConfigurationTypeDef",
    "InterceptorConfigurationTypeDef",
    "InterceptorInputConfigurationTypeDef",
    "InvocationConfigurationInputTypeDef",
    "InvocationConfigurationTypeDef",
    "KmsConfigurationTypeDef",
    "LambdaInterceptorConfigurationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LinkedinOauth2ProviderConfigInputTypeDef",
    "LinkedinOauth2ProviderConfigOutputTypeDef",
    "ListAgentRuntimeEndpointsRequestPaginateTypeDef",
    "ListAgentRuntimeEndpointsRequestTypeDef",
    "ListAgentRuntimeEndpointsResponseTypeDef",
    "ListAgentRuntimeVersionsRequestPaginateTypeDef",
    "ListAgentRuntimeVersionsRequestTypeDef",
    "ListAgentRuntimeVersionsResponseTypeDef",
    "ListAgentRuntimesRequestPaginateTypeDef",
    "ListAgentRuntimesRequestTypeDef",
    "ListAgentRuntimesResponseTypeDef",
    "ListApiKeyCredentialProvidersRequestPaginateTypeDef",
    "ListApiKeyCredentialProvidersRequestTypeDef",
    "ListApiKeyCredentialProvidersResponseTypeDef",
    "ListBrowsersRequestPaginateTypeDef",
    "ListBrowsersRequestTypeDef",
    "ListBrowsersResponseTypeDef",
    "ListCodeInterpretersRequestPaginateTypeDef",
    "ListCodeInterpretersRequestTypeDef",
    "ListCodeInterpretersResponseTypeDef",
    "ListEvaluatorsRequestPaginateTypeDef",
    "ListEvaluatorsRequestTypeDef",
    "ListEvaluatorsResponseTypeDef",
    "ListGatewayTargetsRequestPaginateTypeDef",
    "ListGatewayTargetsRequestTypeDef",
    "ListGatewayTargetsResponseTypeDef",
    "ListGatewaysRequestPaginateTypeDef",
    "ListGatewaysRequestTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListMemoriesInputPaginateTypeDef",
    "ListMemoriesInputTypeDef",
    "ListMemoriesOutputTypeDef",
    "ListOauth2CredentialProvidersRequestPaginateTypeDef",
    "ListOauth2CredentialProvidersRequestTypeDef",
    "ListOauth2CredentialProvidersResponseTypeDef",
    "ListOnlineEvaluationConfigsRequestPaginateTypeDef",
    "ListOnlineEvaluationConfigsRequestTypeDef",
    "ListOnlineEvaluationConfigsResponseTypeDef",
    "ListPoliciesRequestPaginateTypeDef",
    "ListPoliciesRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyEnginesRequestPaginateTypeDef",
    "ListPolicyEnginesRequestTypeDef",
    "ListPolicyEnginesResponseTypeDef",
    "ListPolicyGenerationAssetsRequestPaginateTypeDef",
    "ListPolicyGenerationAssetsRequestTypeDef",
    "ListPolicyGenerationAssetsResponseTypeDef",
    "ListPolicyGenerationsRequestPaginateTypeDef",
    "ListPolicyGenerationsRequestTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkloadIdentitiesRequestPaginateTypeDef",
    "ListWorkloadIdentitiesRequestTypeDef",
    "ListWorkloadIdentitiesResponseTypeDef",
    "LlmAsAJudgeEvaluatorConfigOutputTypeDef",
    "LlmAsAJudgeEvaluatorConfigTypeDef",
    "MCPGatewayConfigurationOutputTypeDef",
    "MCPGatewayConfigurationTypeDef",
    "McpLambdaTargetConfigurationOutputTypeDef",
    "McpLambdaTargetConfigurationTypeDef",
    "McpServerTargetConfigurationTypeDef",
    "McpTargetConfigurationOutputTypeDef",
    "McpTargetConfigurationTypeDef",
    "MemoryStrategyInputTypeDef",
    "MemoryStrategyTypeDef",
    "MemorySummaryTypeDef",
    "MemoryTypeDef",
    "MessageBasedTriggerInputTypeDef",
    "MessageBasedTriggerTypeDef",
    "MetadataConfigurationOutputTypeDef",
    "MetadataConfigurationTypeDef",
    "MetadataConfigurationUnionTypeDef",
    "MicrosoftOauth2ProviderConfigInputTypeDef",
    "MicrosoftOauth2ProviderConfigOutputTypeDef",
    "ModifyConsolidationConfigurationTypeDef",
    "ModifyExtractionConfigurationTypeDef",
    "ModifyInvocationConfigurationInputTypeDef",
    "ModifyMemoryStrategiesTypeDef",
    "ModifyMemoryStrategyInputTypeDef",
    "ModifyReflectionConfigurationTypeDef",
    "ModifySelfManagedConfigurationTypeDef",
    "ModifyStrategyConfigurationTypeDef",
    "NetworkConfigurationOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkConfigurationUnionTypeDef",
    "NumericalScaleDefinitionTypeDef",
    "OAuthCredentialProviderOutputTypeDef",
    "OAuthCredentialProviderTypeDef",
    "OAuthCredentialProviderUnionTypeDef",
    "Oauth2AuthorizationServerMetadataOutputTypeDef",
    "Oauth2AuthorizationServerMetadataTypeDef",
    "Oauth2AuthorizationServerMetadataUnionTypeDef",
    "Oauth2CredentialProviderItemTypeDef",
    "Oauth2DiscoveryOutputTypeDef",
    "Oauth2DiscoveryTypeDef",
    "Oauth2DiscoveryUnionTypeDef",
    "Oauth2ProviderConfigInputTypeDef",
    "Oauth2ProviderConfigOutputTypeDef",
    "OnlineEvaluationConfigSummaryTypeDef",
    "OutputConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyDefinitionTypeDef",
    "PolicyEngineTypeDef",
    "PolicyGenerationAssetTypeDef",
    "PolicyGenerationTypeDef",
    "PolicyTypeDef",
    "ProtocolConfigurationTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RatingScaleOutputTypeDef",
    "RatingScaleTypeDef",
    "RecordingConfigTypeDef",
    "ReflectionConfigurationTypeDef",
    "RequestHeaderConfigurationOutputTypeDef",
    "RequestHeaderConfigurationTypeDef",
    "RequestHeaderConfigurationUnionTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RuleOutputTypeDef",
    "RuleTypeDef",
    "RuleUnionTypeDef",
    "S3ConfigurationTypeDef",
    "S3LocationTypeDef",
    "SalesforceOauth2ProviderConfigInputTypeDef",
    "SalesforceOauth2ProviderConfigOutputTypeDef",
    "SamplingConfigTypeDef",
    "SchemaDefinitionOutputTypeDef",
    "SchemaDefinitionTypeDef",
    "SecretTypeDef",
    "SelfManagedConfigurationInputTypeDef",
    "SelfManagedConfigurationTypeDef",
    "SemanticConsolidationOverrideTypeDef",
    "SemanticExtractionOverrideTypeDef",
    "SemanticMemoryStrategyInputTypeDef",
    "SemanticOverrideConfigurationInputTypeDef",
    "SemanticOverrideConsolidationConfigurationInputTypeDef",
    "SemanticOverrideExtractionConfigurationInputTypeDef",
    "SessionConfigTypeDef",
    "SetTokenVaultCMKRequestTypeDef",
    "SetTokenVaultCMKResponseTypeDef",
    "SlackOauth2ProviderConfigInputTypeDef",
    "SlackOauth2ProviderConfigOutputTypeDef",
    "StartPolicyGenerationRequestTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "StrategyConfigurationTypeDef",
    "SummaryConsolidationOverrideTypeDef",
    "SummaryMemoryStrategyInputTypeDef",
    "SummaryOverrideConfigurationInputTypeDef",
    "SummaryOverrideConsolidationConfigurationInputTypeDef",
    "SynchronizeGatewayTargetsRequestTypeDef",
    "SynchronizeGatewayTargetsResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TargetConfigurationOutputTypeDef",
    "TargetConfigurationTypeDef",
    "TargetConfigurationUnionTypeDef",
    "TargetSummaryTypeDef",
    "TimeBasedTriggerInputTypeDef",
    "TimeBasedTriggerTypeDef",
    "TokenBasedTriggerInputTypeDef",
    "TokenBasedTriggerTypeDef",
    "ToolDefinitionOutputTypeDef",
    "ToolDefinitionTypeDef",
    "ToolSchemaOutputTypeDef",
    "ToolSchemaTypeDef",
    "TriggerConditionInputTypeDef",
    "TriggerConditionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAgentRuntimeEndpointRequestTypeDef",
    "UpdateAgentRuntimeEndpointResponseTypeDef",
    "UpdateAgentRuntimeRequestTypeDef",
    "UpdateAgentRuntimeResponseTypeDef",
    "UpdateApiKeyCredentialProviderRequestTypeDef",
    "UpdateApiKeyCredentialProviderResponseTypeDef",
    "UpdateEvaluatorRequestTypeDef",
    "UpdateEvaluatorResponseTypeDef",
    "UpdateGatewayRequestTypeDef",
    "UpdateGatewayResponseTypeDef",
    "UpdateGatewayTargetRequestTypeDef",
    "UpdateGatewayTargetResponseTypeDef",
    "UpdateMemoryInputTypeDef",
    "UpdateMemoryOutputTypeDef",
    "UpdateOauth2CredentialProviderRequestTypeDef",
    "UpdateOauth2CredentialProviderResponseTypeDef",
    "UpdateOnlineEvaluationConfigRequestTypeDef",
    "UpdateOnlineEvaluationConfigResponseTypeDef",
    "UpdatePolicyEngineRequestTypeDef",
    "UpdatePolicyEngineResponseTypeDef",
    "UpdatePolicyRequestTypeDef",
    "UpdatePolicyResponseTypeDef",
    "UpdateWorkloadIdentityRequestTypeDef",
    "UpdateWorkloadIdentityResponseTypeDef",
    "UserPreferenceConsolidationOverrideTypeDef",
    "UserPreferenceExtractionOverrideTypeDef",
    "UserPreferenceMemoryStrategyInputTypeDef",
    "UserPreferenceOverrideConfigurationInputTypeDef",
    "UserPreferenceOverrideConsolidationConfigurationInputTypeDef",
    "UserPreferenceOverrideExtractionConfigurationInputTypeDef",
    "VpcConfigOutputTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
    "WorkloadIdentityDetailsTypeDef",
    "WorkloadIdentityTypeTypeDef",
)

class ContainerConfigurationTypeDef(TypedDict):
    containerUri: str

AgentRuntimeEndpointTypeDef = TypedDict(
    "AgentRuntimeEndpointTypeDef",
    {
        "name": str,
        "agentRuntimeEndpointArn": str,
        "agentRuntimeArn": str,
        "status": AgentRuntimeEndpointStatusType,
        "id": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "liveVersion": NotRequired[str],
        "targetVersion": NotRequired[str],
        "description": NotRequired[str],
    },
)

class AgentRuntimeTypeDef(TypedDict):
    agentRuntimeArn: str
    agentRuntimeId: str
    agentRuntimeVersion: str
    agentRuntimeName: str
    description: str
    lastUpdatedAt: datetime
    status: AgentRuntimeStatusType

class ApiGatewayToolFilterOutputTypeDef(TypedDict):
    filterPath: str
    methods: List[RestApiMethodType]

class ApiGatewayToolOverrideTypeDef(TypedDict):
    name: str
    path: str
    method: RestApiMethodType
    description: NotRequired[str]

class ApiGatewayToolFilterTypeDef(TypedDict):
    filterPath: str
    methods: Sequence[RestApiMethodType]

class ApiKeyCredentialProviderItemTypeDef(TypedDict):
    name: str
    credentialProviderArn: str
    createdTime: datetime
    lastUpdatedTime: datetime

class ApiKeyCredentialProviderTypeDef(TypedDict):
    providerArn: str
    credentialParameterName: NotRequired[str]
    credentialPrefix: NotRequired[str]
    credentialLocation: NotRequired[ApiKeyCredentialLocationType]

class S3ConfigurationTypeDef(TypedDict):
    uri: NotRequired[str]
    bucketOwnerAccountId: NotRequired[str]

class AtlassianOauth2ProviderConfigInputTypeDef(TypedDict):
    clientId: str
    clientSecret: str

class ClaimMatchValueTypeOutputTypeDef(TypedDict):
    matchValueString: NotRequired[str]
    matchValueStringList: NotRequired[List[str]]

class ClaimMatchValueTypeTypeDef(TypedDict):
    matchValueString: NotRequired[str]
    matchValueStringList: NotRequired[Sequence[str]]

class InferenceConfigurationOutputTypeDef(TypedDict):
    maxTokens: NotRequired[int]
    temperature: NotRequired[float]
    topP: NotRequired[float]
    stopSequences: NotRequired[List[str]]

class InferenceConfigurationTypeDef(TypedDict):
    maxTokens: NotRequired[int]
    temperature: NotRequired[float]
    topP: NotRequired[float]
    stopSequences: NotRequired[Sequence[str]]

class VpcConfigOutputTypeDef(TypedDict):
    securityGroups: List[str]
    subnets: List[str]

class VpcConfigTypeDef(TypedDict):
    securityGroups: Sequence[str]
    subnets: Sequence[str]

class BrowserSigningConfigInputTypeDef(TypedDict):
    enabled: bool

class BrowserSigningConfigOutputTypeDef(TypedDict):
    enabled: bool

class BrowserSummaryTypeDef(TypedDict):
    browserId: str
    browserArn: str
    status: BrowserStatusType
    createdAt: datetime
    name: NotRequired[str]
    description: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]

class CategoricalScaleDefinitionTypeDef(TypedDict):
    definition: str
    label: str

class CedarPolicyTypeDef(TypedDict):
    statement: str

class CloudWatchLogsInputConfigOutputTypeDef(TypedDict):
    logGroupNames: List[str]
    serviceNames: List[str]

class CloudWatchLogsInputConfigTypeDef(TypedDict):
    logGroupNames: Sequence[str]
    serviceNames: Sequence[str]

class CloudWatchOutputConfigTypeDef(TypedDict):
    logGroupName: str

class CodeInterpreterSummaryTypeDef(TypedDict):
    codeInterpreterId: str
    codeInterpreterArn: str
    status: CodeInterpreterStatusType
    createdAt: datetime
    name: NotRequired[str]
    description: NotRequired[str]
    lastUpdatedAt: NotRequired[datetime]

class S3LocationTypeDef(TypedDict):
    bucket: str
    prefix: str
    versionId: NotRequired[str]

class ContentTypeDef(TypedDict):
    rawText: NotRequired[str]

class CreateAgentRuntimeEndpointRequestTypeDef(TypedDict):
    agentRuntimeId: str
    name: str
    agentRuntimeVersion: NotRequired[str]
    description: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class LifecycleConfigurationTypeDef(TypedDict):
    idleRuntimeSessionTimeout: NotRequired[int]
    maxLifetime: NotRequired[int]

class ProtocolConfigurationTypeDef(TypedDict):
    serverProtocol: ServerProtocolType

class WorkloadIdentityDetailsTypeDef(TypedDict):
    workloadIdentityArn: str

class CreateApiKeyCredentialProviderRequestTypeDef(TypedDict):
    name: str
    apiKey: str
    tags: NotRequired[Mapping[str, str]]

class SecretTypeDef(TypedDict):
    secretArn: str

class GatewayPolicyEngineConfigurationTypeDef(TypedDict):
    arn: str
    mode: GatewayPolicyEngineModeType

class MetadataConfigurationOutputTypeDef(TypedDict):
    allowedRequestHeaders: NotRequired[List[str]]
    allowedQueryParameters: NotRequired[List[str]]
    allowedResponseHeaders: NotRequired[List[str]]

class EvaluatorReferenceTypeDef(TypedDict):
    evaluatorId: NotRequired[str]

class CreatePolicyEngineRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    clientToken: NotRequired[str]

class CreateWorkloadIdentityRequestTypeDef(TypedDict):
    name: str
    allowedResourceOauth2ReturnUrls: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]

class OAuthCredentialProviderOutputTypeDef(TypedDict):
    providerArn: str
    scopes: List[str]
    customParameters: NotRequired[Dict[str, str]]
    grantType: NotRequired[OAuthGrantTypeType]
    defaultReturnUrl: NotRequired[str]

class EpisodicOverrideConsolidationConfigurationInputTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class SemanticOverrideConsolidationConfigurationInputTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class SummaryOverrideConsolidationConfigurationInputTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class UserPreferenceOverrideConsolidationConfigurationInputTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class EpisodicConsolidationOverrideTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class SemanticConsolidationOverrideTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class SummaryConsolidationOverrideTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class UserPreferenceConsolidationOverrideTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class EpisodicOverrideExtractionConfigurationInputTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class SemanticOverrideExtractionConfigurationInputTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class UserPreferenceOverrideExtractionConfigurationInputTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class EpisodicExtractionOverrideTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class SemanticExtractionOverrideTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class UserPreferenceExtractionOverrideTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str

class EpisodicOverrideReflectionConfigurationInputTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str
    namespaces: NotRequired[Sequence[str]]

class EpisodicReflectionOverrideTypeDef(TypedDict):
    appendToPrompt: str
    modelId: str
    namespaces: NotRequired[List[str]]

class DeleteAgentRuntimeEndpointRequestTypeDef(TypedDict):
    agentRuntimeId: str
    endpointName: str
    clientToken: NotRequired[str]

class DeleteAgentRuntimeRequestTypeDef(TypedDict):
    agentRuntimeId: str
    clientToken: NotRequired[str]

class DeleteApiKeyCredentialProviderRequestTypeDef(TypedDict):
    name: str

class DeleteBrowserRequestTypeDef(TypedDict):
    browserId: str
    clientToken: NotRequired[str]

class DeleteCodeInterpreterRequestTypeDef(TypedDict):
    codeInterpreterId: str
    clientToken: NotRequired[str]

class DeleteEvaluatorRequestTypeDef(TypedDict):
    evaluatorId: str

class DeleteGatewayRequestTypeDef(TypedDict):
    gatewayIdentifier: str

class DeleteGatewayTargetRequestTypeDef(TypedDict):
    gatewayIdentifier: str
    targetId: str

class DeleteMemoryInputTypeDef(TypedDict):
    memoryId: str
    clientToken: NotRequired[str]

class DeleteMemoryStrategyInputTypeDef(TypedDict):
    memoryStrategyId: str

class DeleteOauth2CredentialProviderRequestTypeDef(TypedDict):
    name: str

class DeleteOnlineEvaluationConfigRequestTypeDef(TypedDict):
    onlineEvaluationConfigId: str

class DeletePolicyEngineRequestTypeDef(TypedDict):
    policyEngineId: str

class DeletePolicyRequestTypeDef(TypedDict):
    policyEngineId: str
    policyId: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class DeleteWorkloadIdentityRequestTypeDef(TypedDict):
    name: str

class EpisodicReflectionConfigurationInputTypeDef(TypedDict):
    namespaces: Sequence[str]

class EpisodicReflectionConfigurationTypeDef(TypedDict):
    namespaces: List[str]

class EvaluatorSummaryTypeDef(TypedDict):
    evaluatorArn: str
    evaluatorId: str
    evaluatorName: str
    evaluatorType: EvaluatorTypeType
    status: EvaluatorStatusType
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    level: NotRequired[EvaluatorLevelType]
    lockedForModification: NotRequired[bool]

class FilterValueTypeDef(TypedDict):
    stringValue: NotRequired[str]
    doubleValue: NotRequired[float]
    booleanValue: NotRequired[bool]

FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "type": NotRequired[FindingTypeType],
        "description": NotRequired[str],
    },
)

class InterceptorInputConfigurationTypeDef(TypedDict):
    passRequestHeaders: bool

class MCPGatewayConfigurationOutputTypeDef(TypedDict):
    supportedVersions: NotRequired[List[str]]
    instructions: NotRequired[str]
    searchType: NotRequired[Literal["SEMANTIC"]]

class MCPGatewayConfigurationTypeDef(TypedDict):
    supportedVersions: NotRequired[Sequence[str]]
    instructions: NotRequired[str]
    searchType: NotRequired[Literal["SEMANTIC"]]

class GatewaySummaryTypeDef(TypedDict):
    gatewayId: str
    name: str
    status: GatewayStatusType
    createdAt: datetime
    updatedAt: datetime
    authorizerType: AuthorizerTypeType
    protocolType: Literal["MCP"]
    description: NotRequired[str]

class GetAgentRuntimeEndpointRequestTypeDef(TypedDict):
    agentRuntimeId: str
    endpointName: str

class GetAgentRuntimeRequestTypeDef(TypedDict):
    agentRuntimeId: str
    agentRuntimeVersion: NotRequired[str]

class RequestHeaderConfigurationOutputTypeDef(TypedDict):
    requestHeaderAllowlist: NotRequired[List[str]]

class GetApiKeyCredentialProviderRequestTypeDef(TypedDict):
    name: str

class GetBrowserRequestTypeDef(TypedDict):
    browserId: str

class GetCodeInterpreterRequestTypeDef(TypedDict):
    codeInterpreterId: str

class GetEvaluatorRequestTypeDef(TypedDict):
    evaluatorId: str

class GetGatewayRequestTypeDef(TypedDict):
    gatewayIdentifier: str

class GetGatewayTargetRequestTypeDef(TypedDict):
    gatewayIdentifier: str
    targetId: str

class GetMemoryInputTypeDef(TypedDict):
    memoryId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetOauth2CredentialProviderRequestTypeDef(TypedDict):
    name: str

class GetOnlineEvaluationConfigRequestTypeDef(TypedDict):
    onlineEvaluationConfigId: str

class GetPolicyEngineRequestTypeDef(TypedDict):
    policyEngineId: str

class GetPolicyGenerationRequestTypeDef(TypedDict):
    policyGenerationId: str
    policyEngineId: str

class ResourceTypeDef(TypedDict):
    arn: NotRequired[str]

class GetPolicyRequestTypeDef(TypedDict):
    policyEngineId: str
    policyId: str

class GetResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class GetTokenVaultRequestTypeDef(TypedDict):
    tokenVaultId: NotRequired[str]

class KmsConfigurationTypeDef(TypedDict):
    keyType: KeyTypeType
    kmsKeyArn: NotRequired[str]

class GetWorkloadIdentityRequestTypeDef(TypedDict):
    name: str

class GithubOauth2ProviderConfigInputTypeDef(TypedDict):
    clientId: str
    clientSecret: str

class GoogleOauth2ProviderConfigInputTypeDef(TypedDict):
    clientId: str
    clientSecret: str

class IncludedOauth2ProviderConfigInputTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    issuer: NotRequired[str]
    authorizationEndpoint: NotRequired[str]
    tokenEndpoint: NotRequired[str]

class LambdaInterceptorConfigurationTypeDef(TypedDict):
    arn: str

class InvocationConfigurationInputTypeDef(TypedDict):
    topicArn: str
    payloadDeliveryBucketName: str

class InvocationConfigurationTypeDef(TypedDict):
    topicArn: str
    payloadDeliveryBucketName: str

class LinkedinOauth2ProviderConfigInputTypeDef(TypedDict):
    clientId: str
    clientSecret: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAgentRuntimeEndpointsRequestTypeDef(TypedDict):
    agentRuntimeId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAgentRuntimeVersionsRequestTypeDef(TypedDict):
    agentRuntimeId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAgentRuntimesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListApiKeyCredentialProvidersRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

ListBrowsersRequestTypeDef = TypedDict(
    "ListBrowsersRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "type": NotRequired[ResourceTypeType],
    },
)
ListCodeInterpretersRequestTypeDef = TypedDict(
    "ListCodeInterpretersRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "type": NotRequired[ResourceTypeType],
    },
)

class ListEvaluatorsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListGatewayTargetsRequestTypeDef(TypedDict):
    gatewayIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class TargetSummaryTypeDef(TypedDict):
    targetId: str
    name: str
    status: TargetStatusType
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]

class ListGatewaysRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListMemoriesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

MemorySummaryTypeDef = TypedDict(
    "MemorySummaryTypeDef",
    {
        "createdAt": datetime,
        "updatedAt": datetime,
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "status": NotRequired[MemoryStatusType],
    },
)

class ListOauth2CredentialProvidersRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class Oauth2CredentialProviderItemTypeDef(TypedDict):
    name: str
    credentialProviderVendor: CredentialProviderVendorTypeType
    credentialProviderArn: str
    createdTime: datetime
    lastUpdatedTime: datetime

class ListOnlineEvaluationConfigsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class OnlineEvaluationConfigSummaryTypeDef(TypedDict):
    onlineEvaluationConfigArn: str
    onlineEvaluationConfigId: str
    onlineEvaluationConfigName: str
    status: OnlineEvaluationConfigStatusType
    executionStatus: OnlineEvaluationExecutionStatusType
    createdAt: datetime
    updatedAt: datetime
    description: NotRequired[str]
    failureReason: NotRequired[str]

class ListPoliciesRequestTypeDef(TypedDict):
    policyEngineId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    targetResourceScope: NotRequired[str]

class ListPolicyEnginesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class PolicyEngineTypeDef(TypedDict):
    policyEngineId: str
    name: str
    createdAt: datetime
    updatedAt: datetime
    policyEngineArn: str
    status: PolicyEngineStatusType
    statusReasons: List[str]
    description: NotRequired[str]

class ListPolicyGenerationAssetsRequestTypeDef(TypedDict):
    policyGenerationId: str
    policyEngineId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListPolicyGenerationsRequestTypeDef(TypedDict):
    policyEngineId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListWorkloadIdentitiesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class WorkloadIdentityTypeTypeDef(TypedDict):
    name: str
    workloadIdentityArn: str

class McpServerTargetConfigurationTypeDef(TypedDict):
    endpoint: str

class SemanticMemoryStrategyInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    namespaces: NotRequired[Sequence[str]]

class SummaryMemoryStrategyInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    namespaces: NotRequired[Sequence[str]]

class UserPreferenceMemoryStrategyInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    namespaces: NotRequired[Sequence[str]]

class MessageBasedTriggerInputTypeDef(TypedDict):
    messageCount: NotRequired[int]

class MessageBasedTriggerTypeDef(TypedDict):
    messageCount: NotRequired[int]

class MetadataConfigurationTypeDef(TypedDict):
    allowedRequestHeaders: NotRequired[Sequence[str]]
    allowedQueryParameters: NotRequired[Sequence[str]]
    allowedResponseHeaders: NotRequired[Sequence[str]]

class MicrosoftOauth2ProviderConfigInputTypeDef(TypedDict):
    clientId: str
    clientSecret: str
    tenantId: NotRequired[str]

class ModifyInvocationConfigurationInputTypeDef(TypedDict):
    topicArn: NotRequired[str]
    payloadDeliveryBucketName: NotRequired[str]

class NumericalScaleDefinitionTypeDef(TypedDict):
    definition: str
    value: float
    label: str

class OAuthCredentialProviderTypeDef(TypedDict):
    providerArn: str
    scopes: Sequence[str]
    customParameters: NotRequired[Mapping[str, str]]
    grantType: NotRequired[OAuthGrantTypeType]
    defaultReturnUrl: NotRequired[str]

class Oauth2AuthorizationServerMetadataOutputTypeDef(TypedDict):
    issuer: str
    authorizationEndpoint: str
    tokenEndpoint: str
    responseTypes: NotRequired[List[str]]
    tokenEndpointAuthMethods: NotRequired[List[str]]

class Oauth2AuthorizationServerMetadataTypeDef(TypedDict):
    issuer: str
    authorizationEndpoint: str
    tokenEndpoint: str
    responseTypes: NotRequired[Sequence[str]]
    tokenEndpointAuthMethods: NotRequired[Sequence[str]]

class SalesforceOauth2ProviderConfigInputTypeDef(TypedDict):
    clientId: str
    clientSecret: str

class SlackOauth2ProviderConfigInputTypeDef(TypedDict):
    clientId: str
    clientSecret: str

class PutResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str
    policy: str

class RequestHeaderConfigurationTypeDef(TypedDict):
    requestHeaderAllowlist: NotRequired[Sequence[str]]

class SamplingConfigTypeDef(TypedDict):
    samplingPercentage: float

class SessionConfigTypeDef(TypedDict):
    sessionTimeoutMinutes: int

SchemaDefinitionOutputTypeDef = TypedDict(
    "SchemaDefinitionOutputTypeDef",
    {
        "type": SchemaTypeType,
        "properties": NotRequired[Dict[str, Dict[str, Any]]],
        "required": NotRequired[List[str]],
        "items": NotRequired[Dict[str, Any]],
        "description": NotRequired[str],
    },
)
SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "type": SchemaTypeType,
        "properties": NotRequired[Mapping[str, Mapping[str, Any]]],
        "required": NotRequired[Sequence[str]],
        "items": NotRequired[Mapping[str, Any]],
        "description": NotRequired[str],
    },
)

class SynchronizeGatewayTargetsRequestTypeDef(TypedDict):
    gatewayIdentifier: str
    targetIdList: Sequence[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TimeBasedTriggerInputTypeDef(TypedDict):
    idleSessionTimeout: NotRequired[int]

class TimeBasedTriggerTypeDef(TypedDict):
    idleSessionTimeout: NotRequired[int]

class TokenBasedTriggerInputTypeDef(TypedDict):
    tokenCount: NotRequired[int]

class TokenBasedTriggerTypeDef(TypedDict):
    tokenCount: NotRequired[int]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAgentRuntimeEndpointRequestTypeDef(TypedDict):
    agentRuntimeId: str
    endpointName: str
    agentRuntimeVersion: NotRequired[str]
    description: NotRequired[str]
    clientToken: NotRequired[str]

class UpdateApiKeyCredentialProviderRequestTypeDef(TypedDict):
    name: str
    apiKey: str

class UpdatePolicyEngineRequestTypeDef(TypedDict):
    policyEngineId: str
    description: NotRequired[str]

class UpdateWorkloadIdentityRequestTypeDef(TypedDict):
    name: str
    allowedResourceOauth2ReturnUrls: NotRequired[Sequence[str]]

class ApiGatewayToolConfigurationOutputTypeDef(TypedDict):
    toolFilters: List[ApiGatewayToolFilterOutputTypeDef]
    toolOverrides: NotRequired[List[ApiGatewayToolOverrideTypeDef]]

class ApiGatewayToolConfigurationTypeDef(TypedDict):
    toolFilters: Sequence[ApiGatewayToolFilterTypeDef]
    toolOverrides: NotRequired[Sequence[ApiGatewayToolOverrideTypeDef]]

class ApiSchemaConfigurationTypeDef(TypedDict):
    s3: NotRequired[S3ConfigurationTypeDef]
    inlinePayload: NotRequired[str]

class AuthorizingClaimMatchValueTypeOutputTypeDef(TypedDict):
    claimMatchValue: ClaimMatchValueTypeOutputTypeDef
    claimMatchOperator: ClaimMatchOperatorTypeType

class AuthorizingClaimMatchValueTypeTypeDef(TypedDict):
    claimMatchValue: ClaimMatchValueTypeTypeDef
    claimMatchOperator: ClaimMatchOperatorTypeType

class BedrockEvaluatorModelConfigOutputTypeDef(TypedDict):
    modelId: str
    inferenceConfig: NotRequired[InferenceConfigurationOutputTypeDef]
    additionalModelRequestFields: NotRequired[Dict[str, Any]]

class BedrockEvaluatorModelConfigTypeDef(TypedDict):
    modelId: str
    inferenceConfig: NotRequired[InferenceConfigurationTypeDef]
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]

class BrowserNetworkConfigurationOutputTypeDef(TypedDict):
    networkMode: BrowserNetworkModeType
    vpcConfig: NotRequired[VpcConfigOutputTypeDef]

class CodeInterpreterNetworkConfigurationOutputTypeDef(TypedDict):
    networkMode: CodeInterpreterNetworkModeType
    vpcConfig: NotRequired[VpcConfigOutputTypeDef]

class NetworkConfigurationOutputTypeDef(TypedDict):
    networkMode: NetworkModeType
    networkModeConfig: NotRequired[VpcConfigOutputTypeDef]

class BrowserNetworkConfigurationTypeDef(TypedDict):
    networkMode: BrowserNetworkModeType
    vpcConfig: NotRequired[VpcConfigTypeDef]

class CodeInterpreterNetworkConfigurationTypeDef(TypedDict):
    networkMode: CodeInterpreterNetworkModeType
    vpcConfig: NotRequired[VpcConfigTypeDef]

class NetworkConfigurationTypeDef(TypedDict):
    networkMode: NetworkModeType
    networkModeConfig: NotRequired[VpcConfigTypeDef]

class PolicyDefinitionTypeDef(TypedDict):
    cedar: NotRequired[CedarPolicyTypeDef]

class DataSourceConfigOutputTypeDef(TypedDict):
    cloudWatchLogs: NotRequired[CloudWatchLogsInputConfigOutputTypeDef]

class DataSourceConfigTypeDef(TypedDict):
    cloudWatchLogs: NotRequired[CloudWatchLogsInputConfigTypeDef]

class OutputConfigTypeDef(TypedDict):
    cloudWatchConfig: CloudWatchOutputConfigTypeDef

class CodeTypeDef(TypedDict):
    s3: NotRequired[S3LocationTypeDef]

class RecordingConfigTypeDef(TypedDict):
    enabled: NotRequired[bool]
    s3Location: NotRequired[S3LocationTypeDef]

class CreateAgentRuntimeEndpointResponseTypeDef(TypedDict):
    targetVersion: str
    agentRuntimeEndpointArn: str
    agentRuntimeArn: str
    agentRuntimeId: str
    endpointName: str
    status: AgentRuntimeEndpointStatusType
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBrowserResponseTypeDef(TypedDict):
    browserId: str
    browserArn: str
    createdAt: datetime
    status: BrowserStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCodeInterpreterResponseTypeDef(TypedDict):
    codeInterpreterId: str
    codeInterpreterArn: str
    createdAt: datetime
    status: CodeInterpreterStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEvaluatorResponseTypeDef(TypedDict):
    evaluatorArn: str
    evaluatorId: str
    createdAt: datetime
    status: EvaluatorStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePolicyEngineResponseTypeDef(TypedDict):
    policyEngineId: str
    name: str
    description: str
    createdAt: datetime
    updatedAt: datetime
    policyEngineArn: str
    status: PolicyEngineStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkloadIdentityResponseTypeDef(TypedDict):
    name: str
    workloadIdentityArn: str
    allowedResourceOauth2ReturnUrls: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentRuntimeEndpointResponseTypeDef(TypedDict):
    status: AgentRuntimeEndpointStatusType
    agentRuntimeId: str
    endpointName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAgentRuntimeResponseTypeDef(TypedDict):
    status: AgentRuntimeStatusType
    agentRuntimeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBrowserResponseTypeDef(TypedDict):
    browserId: str
    status: BrowserStatusType
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCodeInterpreterResponseTypeDef(TypedDict):
    codeInterpreterId: str
    status: CodeInterpreterStatusType
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEvaluatorResponseTypeDef(TypedDict):
    evaluatorArn: str
    evaluatorId: str
    status: EvaluatorStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    status: GatewayStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayTargetResponseTypeDef(TypedDict):
    gatewayArn: str
    targetId: str
    status: TargetStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMemoryOutputTypeDef(TypedDict):
    memoryId: str
    status: MemoryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOnlineEvaluationConfigResponseTypeDef(TypedDict):
    onlineEvaluationConfigArn: str
    onlineEvaluationConfigId: str
    status: OnlineEvaluationConfigStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePolicyEngineResponseTypeDef(TypedDict):
    policyEngineId: str
    name: str
    description: str
    createdAt: datetime
    updatedAt: datetime
    policyEngineArn: str
    status: PolicyEngineStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

GetAgentRuntimeEndpointResponseTypeDef = TypedDict(
    "GetAgentRuntimeEndpointResponseTypeDef",
    {
        "liveVersion": str,
        "targetVersion": str,
        "agentRuntimeEndpointArn": str,
        "agentRuntimeArn": str,
        "description": str,
        "status": AgentRuntimeEndpointStatusType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "failureReason": str,
        "name": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetPolicyEngineResponseTypeDef(TypedDict):
    policyEngineId: str
    name: str
    description: str
    createdAt: datetime
    updatedAt: datetime
    policyEngineArn: str
    status: PolicyEngineStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(TypedDict):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkloadIdentityResponseTypeDef(TypedDict):
    name: str
    workloadIdentityArn: str
    allowedResourceOauth2ReturnUrls: List[str]
    createdTime: datetime
    lastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAgentRuntimeEndpointsResponseTypeDef(TypedDict):
    runtimeEndpoints: List[AgentRuntimeEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAgentRuntimeVersionsResponseTypeDef(TypedDict):
    agentRuntimes: List[AgentRuntimeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAgentRuntimesResponseTypeDef(TypedDict):
    agentRuntimes: List[AgentRuntimeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListApiKeyCredentialProvidersResponseTypeDef(TypedDict):
    credentialProviders: List[ApiKeyCredentialProviderItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListBrowsersResponseTypeDef(TypedDict):
    browserSummaries: List[BrowserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListCodeInterpretersResponseTypeDef(TypedDict):
    codeInterpreterSummaries: List[CodeInterpreterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(TypedDict):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentRuntimeEndpointResponseTypeDef(TypedDict):
    liveVersion: str
    targetVersion: str
    agentRuntimeEndpointArn: str
    agentRuntimeArn: str
    status: AgentRuntimeEndpointStatusType
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEvaluatorResponseTypeDef(TypedDict):
    evaluatorArn: str
    evaluatorId: str
    updatedAt: datetime
    status: EvaluatorStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOnlineEvaluationConfigResponseTypeDef(TypedDict):
    onlineEvaluationConfigArn: str
    onlineEvaluationConfigId: str
    updatedAt: datetime
    status: OnlineEvaluationConfigStatusType
    executionStatus: OnlineEvaluationExecutionStatusType
    failureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePolicyEngineResponseTypeDef(TypedDict):
    policyEngineId: str
    name: str
    description: str
    createdAt: datetime
    updatedAt: datetime
    policyEngineArn: str
    status: PolicyEngineStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkloadIdentityResponseTypeDef(TypedDict):
    name: str
    workloadIdentityArn: str
    allowedResourceOauth2ReturnUrls: List[str]
    createdTime: datetime
    lastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentRuntimeResponseTypeDef(TypedDict):
    agentRuntimeArn: str
    workloadIdentityDetails: WorkloadIdentityDetailsTypeDef
    agentRuntimeId: str
    agentRuntimeVersion: str
    createdAt: datetime
    status: AgentRuntimeStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentRuntimeResponseTypeDef(TypedDict):
    agentRuntimeArn: str
    agentRuntimeId: str
    workloadIdentityDetails: WorkloadIdentityDetailsTypeDef
    agentRuntimeVersion: str
    createdAt: datetime
    lastUpdatedAt: datetime
    status: AgentRuntimeStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApiKeyCredentialProviderResponseTypeDef(TypedDict):
    apiKeySecretArn: SecretTypeDef
    name: str
    credentialProviderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApiKeyCredentialProviderResponseTypeDef(TypedDict):
    apiKeySecretArn: SecretTypeDef
    name: str
    credentialProviderArn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApiKeyCredentialProviderResponseTypeDef(TypedDict):
    apiKeySecretArn: SecretTypeDef
    name: str
    credentialProviderArn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CredentialProviderOutputTypeDef(TypedDict):
    oauthCredentialProvider: NotRequired[OAuthCredentialProviderOutputTypeDef]
    apiKeyCredentialProvider: NotRequired[ApiKeyCredentialProviderTypeDef]

class SummaryOverrideConfigurationInputTypeDef(TypedDict):
    consolidation: NotRequired[SummaryOverrideConsolidationConfigurationInputTypeDef]

class CustomConsolidationConfigurationInputTypeDef(TypedDict):
    semanticConsolidationOverride: NotRequired[
        SemanticOverrideConsolidationConfigurationInputTypeDef
    ]
    summaryConsolidationOverride: NotRequired[SummaryOverrideConsolidationConfigurationInputTypeDef]
    userPreferenceConsolidationOverride: NotRequired[
        UserPreferenceOverrideConsolidationConfigurationInputTypeDef
    ]
    episodicConsolidationOverride: NotRequired[
        EpisodicOverrideConsolidationConfigurationInputTypeDef
    ]

class CustomConsolidationConfigurationTypeDef(TypedDict):
    semanticConsolidationOverride: NotRequired[SemanticConsolidationOverrideTypeDef]
    summaryConsolidationOverride: NotRequired[SummaryConsolidationOverrideTypeDef]
    userPreferenceConsolidationOverride: NotRequired[UserPreferenceConsolidationOverrideTypeDef]
    episodicConsolidationOverride: NotRequired[EpisodicConsolidationOverrideTypeDef]

class SemanticOverrideConfigurationInputTypeDef(TypedDict):
    extraction: NotRequired[SemanticOverrideExtractionConfigurationInputTypeDef]
    consolidation: NotRequired[SemanticOverrideConsolidationConfigurationInputTypeDef]

class CustomExtractionConfigurationInputTypeDef(TypedDict):
    semanticExtractionOverride: NotRequired[SemanticOverrideExtractionConfigurationInputTypeDef]
    userPreferenceExtractionOverride: NotRequired[
        UserPreferenceOverrideExtractionConfigurationInputTypeDef
    ]
    episodicExtractionOverride: NotRequired[EpisodicOverrideExtractionConfigurationInputTypeDef]

class UserPreferenceOverrideConfigurationInputTypeDef(TypedDict):
    extraction: NotRequired[UserPreferenceOverrideExtractionConfigurationInputTypeDef]
    consolidation: NotRequired[UserPreferenceOverrideConsolidationConfigurationInputTypeDef]

class CustomExtractionConfigurationTypeDef(TypedDict):
    semanticExtractionOverride: NotRequired[SemanticExtractionOverrideTypeDef]
    userPreferenceExtractionOverride: NotRequired[UserPreferenceExtractionOverrideTypeDef]
    episodicExtractionOverride: NotRequired[EpisodicExtractionOverrideTypeDef]

class CustomReflectionConfigurationInputTypeDef(TypedDict):
    episodicReflectionOverride: NotRequired[EpisodicOverrideReflectionConfigurationInputTypeDef]

class EpisodicOverrideConfigurationInputTypeDef(TypedDict):
    extraction: NotRequired[EpisodicOverrideExtractionConfigurationInputTypeDef]
    consolidation: NotRequired[EpisodicOverrideConsolidationConfigurationInputTypeDef]
    reflection: NotRequired[EpisodicOverrideReflectionConfigurationInputTypeDef]

class CustomReflectionConfigurationTypeDef(TypedDict):
    episodicReflectionOverride: NotRequired[EpisodicReflectionOverrideTypeDef]

class EpisodicMemoryStrategyInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    namespaces: NotRequired[Sequence[str]]
    reflectionConfiguration: NotRequired[EpisodicReflectionConfigurationInputTypeDef]

class ListEvaluatorsResponseTypeDef(TypedDict):
    evaluators: List[EvaluatorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "key": str,
        "operator": FilterOperatorType,
        "value": FilterValueTypeDef,
    },
)

class GatewayProtocolConfigurationOutputTypeDef(TypedDict):
    mcp: NotRequired[MCPGatewayConfigurationOutputTypeDef]

class GatewayProtocolConfigurationTypeDef(TypedDict):
    mcp: NotRequired[MCPGatewayConfigurationTypeDef]

class ListGatewaysResponseTypeDef(TypedDict):
    items: List[GatewaySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetMemoryInputWaitTypeDef(TypedDict):
    memoryId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPolicyEngineRequestWaitExtraTypeDef(TypedDict):
    policyEngineId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPolicyEngineRequestWaitTypeDef(TypedDict):
    policyEngineId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPolicyGenerationRequestWaitTypeDef(TypedDict):
    policyGenerationId: str
    policyEngineId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPolicyRequestWaitExtraTypeDef(TypedDict):
    policyEngineId: str
    policyId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPolicyRequestWaitTypeDef(TypedDict):
    policyEngineId: str
    policyId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetPolicyGenerationResponseTypeDef(TypedDict):
    policyEngineId: str
    policyGenerationId: str
    name: str
    policyGenerationArn: str
    resource: ResourceTypeDef
    createdAt: datetime
    updatedAt: datetime
    status: PolicyGenerationStatusType
    statusReasons: List[str]
    findings: str
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyGenerationTypeDef(TypedDict):
    policyEngineId: str
    policyGenerationId: str
    name: str
    policyGenerationArn: str
    resource: ResourceTypeDef
    createdAt: datetime
    updatedAt: datetime
    status: PolicyGenerationStatusType
    statusReasons: List[str]
    findings: NotRequired[str]

class StartPolicyGenerationRequestTypeDef(TypedDict):
    policyEngineId: str
    resource: ResourceTypeDef
    content: ContentTypeDef
    name: str
    clientToken: NotRequired[str]

class StartPolicyGenerationResponseTypeDef(TypedDict):
    policyEngineId: str
    policyGenerationId: str
    name: str
    policyGenerationArn: str
    resource: ResourceTypeDef
    createdAt: datetime
    updatedAt: datetime
    status: PolicyGenerationStatusType
    statusReasons: List[str]
    findings: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTokenVaultResponseTypeDef(TypedDict):
    tokenVaultId: str
    kmsConfiguration: KmsConfigurationTypeDef
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class SetTokenVaultCMKRequestTypeDef(TypedDict):
    kmsConfiguration: KmsConfigurationTypeDef
    tokenVaultId: NotRequired[str]

class SetTokenVaultCMKResponseTypeDef(TypedDict):
    tokenVaultId: str
    kmsConfiguration: KmsConfigurationTypeDef
    lastModifiedDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

InterceptorConfigurationTypeDef = TypedDict(
    "InterceptorConfigurationTypeDef",
    {
        "lambda": NotRequired[LambdaInterceptorConfigurationTypeDef],
    },
)

class ListAgentRuntimeEndpointsRequestPaginateTypeDef(TypedDict):
    agentRuntimeId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAgentRuntimeVersionsRequestPaginateTypeDef(TypedDict):
    agentRuntimeId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAgentRuntimesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListApiKeyCredentialProvidersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListBrowsersRequestPaginateTypeDef = TypedDict(
    "ListBrowsersRequestPaginateTypeDef",
    {
        "type": NotRequired[ResourceTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListCodeInterpretersRequestPaginateTypeDef = TypedDict(
    "ListCodeInterpretersRequestPaginateTypeDef",
    {
        "type": NotRequired[ResourceTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListEvaluatorsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGatewayTargetsRequestPaginateTypeDef(TypedDict):
    gatewayIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGatewaysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMemoriesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOauth2CredentialProvidersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOnlineEvaluationConfigsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPoliciesRequestPaginateTypeDef(TypedDict):
    policyEngineId: str
    targetResourceScope: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyEnginesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyGenerationAssetsRequestPaginateTypeDef(TypedDict):
    policyGenerationId: str
    policyEngineId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPolicyGenerationsRequestPaginateTypeDef(TypedDict):
    policyEngineId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkloadIdentitiesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGatewayTargetsResponseTypeDef(TypedDict):
    items: List[TargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListMemoriesOutputTypeDef(TypedDict):
    memories: List[MemorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListOauth2CredentialProvidersResponseTypeDef(TypedDict):
    credentialProviders: List[Oauth2CredentialProviderItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListOnlineEvaluationConfigsResponseTypeDef(TypedDict):
    onlineEvaluationConfigs: List[OnlineEvaluationConfigSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPolicyEnginesResponseTypeDef(TypedDict):
    policyEngines: List[PolicyEngineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListWorkloadIdentitiesResponseTypeDef(TypedDict):
    workloadIdentities: List[WorkloadIdentityTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

MetadataConfigurationUnionTypeDef = Union[
    MetadataConfigurationTypeDef, MetadataConfigurationOutputTypeDef
]

class RatingScaleOutputTypeDef(TypedDict):
    numerical: NotRequired[List[NumericalScaleDefinitionTypeDef]]
    categorical: NotRequired[List[CategoricalScaleDefinitionTypeDef]]

class RatingScaleTypeDef(TypedDict):
    numerical: NotRequired[Sequence[NumericalScaleDefinitionTypeDef]]
    categorical: NotRequired[Sequence[CategoricalScaleDefinitionTypeDef]]

OAuthCredentialProviderUnionTypeDef = Union[
    OAuthCredentialProviderTypeDef, OAuthCredentialProviderOutputTypeDef
]

class Oauth2DiscoveryOutputTypeDef(TypedDict):
    discoveryUrl: NotRequired[str]
    authorizationServerMetadata: NotRequired[Oauth2AuthorizationServerMetadataOutputTypeDef]

Oauth2AuthorizationServerMetadataUnionTypeDef = Union[
    Oauth2AuthorizationServerMetadataTypeDef, Oauth2AuthorizationServerMetadataOutputTypeDef
]
RequestHeaderConfigurationUnionTypeDef = Union[
    RequestHeaderConfigurationTypeDef, RequestHeaderConfigurationOutputTypeDef
]

class ToolDefinitionOutputTypeDef(TypedDict):
    name: str
    description: str
    inputSchema: SchemaDefinitionOutputTypeDef
    outputSchema: NotRequired[SchemaDefinitionOutputTypeDef]

class ToolDefinitionTypeDef(TypedDict):
    name: str
    description: str
    inputSchema: SchemaDefinitionTypeDef
    outputSchema: NotRequired[SchemaDefinitionTypeDef]

class TriggerConditionInputTypeDef(TypedDict):
    messageBasedTrigger: NotRequired[MessageBasedTriggerInputTypeDef]
    tokenBasedTrigger: NotRequired[TokenBasedTriggerInputTypeDef]
    timeBasedTrigger: NotRequired[TimeBasedTriggerInputTypeDef]

class TriggerConditionTypeDef(TypedDict):
    messageBasedTrigger: NotRequired[MessageBasedTriggerTypeDef]
    tokenBasedTrigger: NotRequired[TokenBasedTriggerTypeDef]
    timeBasedTrigger: NotRequired[TimeBasedTriggerTypeDef]

class ApiGatewayTargetConfigurationOutputTypeDef(TypedDict):
    restApiId: str
    stage: str
    apiGatewayToolConfiguration: ApiGatewayToolConfigurationOutputTypeDef

class ApiGatewayTargetConfigurationTypeDef(TypedDict):
    restApiId: str
    stage: str
    apiGatewayToolConfiguration: ApiGatewayToolConfigurationTypeDef

class CustomClaimValidationTypeOutputTypeDef(TypedDict):
    inboundTokenClaimName: str
    inboundTokenClaimValueType: InboundTokenClaimValueTypeType
    authorizingClaimMatchValue: AuthorizingClaimMatchValueTypeOutputTypeDef

class CustomClaimValidationTypeTypeDef(TypedDict):
    inboundTokenClaimName: str
    inboundTokenClaimValueType: InboundTokenClaimValueTypeType
    authorizingClaimMatchValue: AuthorizingClaimMatchValueTypeTypeDef

class EvaluatorModelConfigOutputTypeDef(TypedDict):
    bedrockEvaluatorModelConfig: NotRequired[BedrockEvaluatorModelConfigOutputTypeDef]

class EvaluatorModelConfigTypeDef(TypedDict):
    bedrockEvaluatorModelConfig: NotRequired[BedrockEvaluatorModelConfigTypeDef]

class GetCodeInterpreterResponseTypeDef(TypedDict):
    codeInterpreterId: str
    codeInterpreterArn: str
    name: str
    description: str
    executionRoleArn: str
    networkConfiguration: CodeInterpreterNetworkConfigurationOutputTypeDef
    status: CodeInterpreterStatusType
    failureReason: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

BrowserNetworkConfigurationUnionTypeDef = Union[
    BrowserNetworkConfigurationTypeDef, BrowserNetworkConfigurationOutputTypeDef
]
CodeInterpreterNetworkConfigurationUnionTypeDef = Union[
    CodeInterpreterNetworkConfigurationTypeDef, CodeInterpreterNetworkConfigurationOutputTypeDef
]
NetworkConfigurationUnionTypeDef = Union[
    NetworkConfigurationTypeDef, NetworkConfigurationOutputTypeDef
]

class CreatePolicyRequestTypeDef(TypedDict):
    name: str
    definition: PolicyDefinitionTypeDef
    policyEngineId: str
    description: NotRequired[str]
    validationMode: NotRequired[PolicyValidationModeType]
    clientToken: NotRequired[str]

class CreatePolicyResponseTypeDef(TypedDict):
    policyId: str
    name: str
    policyEngineId: str
    definition: PolicyDefinitionTypeDef
    description: str
    createdAt: datetime
    updatedAt: datetime
    policyArn: str
    status: PolicyStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePolicyResponseTypeDef(TypedDict):
    policyId: str
    name: str
    policyEngineId: str
    definition: PolicyDefinitionTypeDef
    description: str
    createdAt: datetime
    updatedAt: datetime
    policyArn: str
    status: PolicyStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(TypedDict):
    policyId: str
    name: str
    policyEngineId: str
    definition: PolicyDefinitionTypeDef
    description: str
    createdAt: datetime
    updatedAt: datetime
    policyArn: str
    status: PolicyStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class PolicyGenerationAssetTypeDef(TypedDict):
    policyGenerationAssetId: str
    rawTextFragment: str
    findings: List[FindingTypeDef]
    definition: NotRequired[PolicyDefinitionTypeDef]

class PolicyTypeDef(TypedDict):
    policyId: str
    name: str
    policyEngineId: str
    definition: PolicyDefinitionTypeDef
    createdAt: datetime
    updatedAt: datetime
    policyArn: str
    status: PolicyStatusType
    statusReasons: List[str]
    description: NotRequired[str]

class UpdatePolicyRequestTypeDef(TypedDict):
    policyEngineId: str
    policyId: str
    definition: PolicyDefinitionTypeDef
    description: NotRequired[str]
    validationMode: NotRequired[PolicyValidationModeType]

class UpdatePolicyResponseTypeDef(TypedDict):
    policyId: str
    name: str
    policyEngineId: str
    definition: PolicyDefinitionTypeDef
    description: str
    createdAt: datetime
    updatedAt: datetime
    policyArn: str
    status: PolicyStatusType
    statusReasons: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

DataSourceConfigUnionTypeDef = Union[DataSourceConfigTypeDef, DataSourceConfigOutputTypeDef]

class CreateOnlineEvaluationConfigResponseTypeDef(TypedDict):
    onlineEvaluationConfigArn: str
    onlineEvaluationConfigId: str
    createdAt: datetime
    outputConfig: OutputConfigTypeDef
    status: OnlineEvaluationConfigStatusType
    executionStatus: OnlineEvaluationExecutionStatusType
    failureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CodeConfigurationOutputTypeDef(TypedDict):
    code: CodeTypeDef
    runtime: AgentManagedRuntimeTypeType
    entryPoint: List[str]

class CodeConfigurationTypeDef(TypedDict):
    code: CodeTypeDef
    runtime: AgentManagedRuntimeTypeType
    entryPoint: Sequence[str]

class GetBrowserResponseTypeDef(TypedDict):
    browserId: str
    browserArn: str
    name: str
    description: str
    executionRoleArn: str
    networkConfiguration: BrowserNetworkConfigurationOutputTypeDef
    recording: RecordingConfigTypeDef
    browserSigning: BrowserSigningConfigOutputTypeDef
    status: BrowserStatusType
    failureReason: str
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CredentialProviderConfigurationOutputTypeDef(TypedDict):
    credentialProviderType: CredentialProviderTypeType
    credentialProvider: NotRequired[CredentialProviderOutputTypeDef]

class ModifyConsolidationConfigurationTypeDef(TypedDict):
    customConsolidationConfiguration: NotRequired[CustomConsolidationConfigurationInputTypeDef]

class ConsolidationConfigurationTypeDef(TypedDict):
    customConsolidationConfiguration: NotRequired[CustomConsolidationConfigurationTypeDef]

class ModifyExtractionConfigurationTypeDef(TypedDict):
    customExtractionConfiguration: NotRequired[CustomExtractionConfigurationInputTypeDef]

class ExtractionConfigurationTypeDef(TypedDict):
    customExtractionConfiguration: NotRequired[CustomExtractionConfigurationTypeDef]

class ModifyReflectionConfigurationTypeDef(TypedDict):
    episodicReflectionConfiguration: NotRequired[EpisodicReflectionConfigurationInputTypeDef]
    customReflectionConfiguration: NotRequired[CustomReflectionConfigurationInputTypeDef]

class ReflectionConfigurationTypeDef(TypedDict):
    customReflectionConfiguration: NotRequired[CustomReflectionConfigurationTypeDef]
    episodicReflectionConfiguration: NotRequired[EpisodicReflectionConfigurationTypeDef]

class RuleOutputTypeDef(TypedDict):
    samplingConfig: SamplingConfigTypeDef
    filters: NotRequired[List[FilterTypeDef]]
    sessionConfig: NotRequired[SessionConfigTypeDef]

class RuleTypeDef(TypedDict):
    samplingConfig: SamplingConfigTypeDef
    filters: NotRequired[Sequence[FilterTypeDef]]
    sessionConfig: NotRequired[SessionConfigTypeDef]

GatewayProtocolConfigurationUnionTypeDef = Union[
    GatewayProtocolConfigurationTypeDef, GatewayProtocolConfigurationOutputTypeDef
]

class ListPolicyGenerationsResponseTypeDef(TypedDict):
    policyGenerations: List[PolicyGenerationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GatewayInterceptorConfigurationOutputTypeDef(TypedDict):
    interceptor: InterceptorConfigurationTypeDef
    interceptionPoints: List[GatewayInterceptionPointType]
    inputConfiguration: NotRequired[InterceptorInputConfigurationTypeDef]

class GatewayInterceptorConfigurationTypeDef(TypedDict):
    interceptor: InterceptorConfigurationTypeDef
    interceptionPoints: Sequence[GatewayInterceptionPointType]
    inputConfiguration: NotRequired[InterceptorInputConfigurationTypeDef]

class CredentialProviderTypeDef(TypedDict):
    oauthCredentialProvider: NotRequired[OAuthCredentialProviderUnionTypeDef]
    apiKeyCredentialProvider: NotRequired[ApiKeyCredentialProviderTypeDef]

class AtlassianOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class CustomOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class GithubOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class GoogleOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class IncludedOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class LinkedinOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class MicrosoftOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class SalesforceOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class SlackOauth2ProviderConfigOutputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryOutputTypeDef
    clientId: NotRequired[str]

class Oauth2DiscoveryTypeDef(TypedDict):
    discoveryUrl: NotRequired[str]
    authorizationServerMetadata: NotRequired[Oauth2AuthorizationServerMetadataUnionTypeDef]

class ToolSchemaOutputTypeDef(TypedDict):
    s3: NotRequired[S3ConfigurationTypeDef]
    inlinePayload: NotRequired[List[ToolDefinitionOutputTypeDef]]

class ToolSchemaTypeDef(TypedDict):
    s3: NotRequired[S3ConfigurationTypeDef]
    inlinePayload: NotRequired[Sequence[ToolDefinitionTypeDef]]

class ModifySelfManagedConfigurationTypeDef(TypedDict):
    triggerConditions: NotRequired[Sequence[TriggerConditionInputTypeDef]]
    invocationConfiguration: NotRequired[ModifyInvocationConfigurationInputTypeDef]
    historicalContextWindowSize: NotRequired[int]

class SelfManagedConfigurationInputTypeDef(TypedDict):
    invocationConfiguration: InvocationConfigurationInputTypeDef
    triggerConditions: NotRequired[Sequence[TriggerConditionInputTypeDef]]
    historicalContextWindowSize: NotRequired[int]

class SelfManagedConfigurationTypeDef(TypedDict):
    triggerConditions: List[TriggerConditionTypeDef]
    invocationConfiguration: InvocationConfigurationTypeDef
    historicalContextWindowSize: int

class CustomJWTAuthorizerConfigurationOutputTypeDef(TypedDict):
    discoveryUrl: str
    allowedAudience: NotRequired[List[str]]
    allowedClients: NotRequired[List[str]]
    allowedScopes: NotRequired[List[str]]
    customClaims: NotRequired[List[CustomClaimValidationTypeOutputTypeDef]]

class CustomJWTAuthorizerConfigurationTypeDef(TypedDict):
    discoveryUrl: str
    allowedAudience: NotRequired[Sequence[str]]
    allowedClients: NotRequired[Sequence[str]]
    allowedScopes: NotRequired[Sequence[str]]
    customClaims: NotRequired[Sequence[CustomClaimValidationTypeTypeDef]]

class LlmAsAJudgeEvaluatorConfigOutputTypeDef(TypedDict):
    instructions: str
    ratingScale: RatingScaleOutputTypeDef
    modelConfig: EvaluatorModelConfigOutputTypeDef

class LlmAsAJudgeEvaluatorConfigTypeDef(TypedDict):
    instructions: str
    ratingScale: RatingScaleTypeDef
    modelConfig: EvaluatorModelConfigTypeDef

class CreateBrowserRequestTypeDef(TypedDict):
    name: str
    networkConfiguration: BrowserNetworkConfigurationUnionTypeDef
    description: NotRequired[str]
    executionRoleArn: NotRequired[str]
    recording: NotRequired[RecordingConfigTypeDef]
    browserSigning: NotRequired[BrowserSigningConfigInputTypeDef]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateCodeInterpreterRequestTypeDef(TypedDict):
    name: str
    networkConfiguration: CodeInterpreterNetworkConfigurationUnionTypeDef
    description: NotRequired[str]
    executionRoleArn: NotRequired[str]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class ListPolicyGenerationAssetsResponseTypeDef(TypedDict):
    policyGenerationAssets: List[PolicyGenerationAssetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListPoliciesResponseTypeDef(TypedDict):
    policies: List[PolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AgentRuntimeArtifactOutputTypeDef(TypedDict):
    containerConfiguration: NotRequired[ContainerConfigurationTypeDef]
    codeConfiguration: NotRequired[CodeConfigurationOutputTypeDef]

class AgentRuntimeArtifactTypeDef(TypedDict):
    containerConfiguration: NotRequired[ContainerConfigurationTypeDef]
    codeConfiguration: NotRequired[CodeConfigurationTypeDef]

class GetOnlineEvaluationConfigResponseTypeDef(TypedDict):
    onlineEvaluationConfigArn: str
    onlineEvaluationConfigId: str
    onlineEvaluationConfigName: str
    description: str
    rule: RuleOutputTypeDef
    dataSourceConfig: DataSourceConfigOutputTypeDef
    evaluators: List[EvaluatorReferenceTypeDef]
    outputConfig: OutputConfigTypeDef
    evaluationExecutionRoleArn: str
    status: OnlineEvaluationConfigStatusType
    executionStatus: OnlineEvaluationExecutionStatusType
    createdAt: datetime
    updatedAt: datetime
    failureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

RuleUnionTypeDef = Union[RuleTypeDef, RuleOutputTypeDef]
GatewayInterceptorConfigurationUnionTypeDef = Union[
    GatewayInterceptorConfigurationTypeDef, GatewayInterceptorConfigurationOutputTypeDef
]
CredentialProviderUnionTypeDef = Union[CredentialProviderTypeDef, CredentialProviderOutputTypeDef]

class Oauth2ProviderConfigOutputTypeDef(TypedDict):
    customOauth2ProviderConfig: NotRequired[CustomOauth2ProviderConfigOutputTypeDef]
    googleOauth2ProviderConfig: NotRequired[GoogleOauth2ProviderConfigOutputTypeDef]
    githubOauth2ProviderConfig: NotRequired[GithubOauth2ProviderConfigOutputTypeDef]
    slackOauth2ProviderConfig: NotRequired[SlackOauth2ProviderConfigOutputTypeDef]
    salesforceOauth2ProviderConfig: NotRequired[SalesforceOauth2ProviderConfigOutputTypeDef]
    microsoftOauth2ProviderConfig: NotRequired[MicrosoftOauth2ProviderConfigOutputTypeDef]
    atlassianOauth2ProviderConfig: NotRequired[AtlassianOauth2ProviderConfigOutputTypeDef]
    linkedinOauth2ProviderConfig: NotRequired[LinkedinOauth2ProviderConfigOutputTypeDef]
    includedOauth2ProviderConfig: NotRequired[IncludedOauth2ProviderConfigOutputTypeDef]

Oauth2DiscoveryUnionTypeDef = Union[Oauth2DiscoveryTypeDef, Oauth2DiscoveryOutputTypeDef]

class McpLambdaTargetConfigurationOutputTypeDef(TypedDict):
    lambdaArn: str
    toolSchema: ToolSchemaOutputTypeDef

class McpLambdaTargetConfigurationTypeDef(TypedDict):
    lambdaArn: str
    toolSchema: ToolSchemaTypeDef

class ModifyStrategyConfigurationTypeDef(TypedDict):
    extraction: NotRequired[ModifyExtractionConfigurationTypeDef]
    consolidation: NotRequired[ModifyConsolidationConfigurationTypeDef]
    reflection: NotRequired[ModifyReflectionConfigurationTypeDef]
    selfManagedConfiguration: NotRequired[ModifySelfManagedConfigurationTypeDef]

class CustomConfigurationInputTypeDef(TypedDict):
    semanticOverride: NotRequired[SemanticOverrideConfigurationInputTypeDef]
    summaryOverride: NotRequired[SummaryOverrideConfigurationInputTypeDef]
    userPreferenceOverride: NotRequired[UserPreferenceOverrideConfigurationInputTypeDef]
    episodicOverride: NotRequired[EpisodicOverrideConfigurationInputTypeDef]
    selfManagedConfiguration: NotRequired[SelfManagedConfigurationInputTypeDef]

StrategyConfigurationTypeDef = TypedDict(
    "StrategyConfigurationTypeDef",
    {
        "type": NotRequired[OverrideTypeType],
        "extraction": NotRequired[ExtractionConfigurationTypeDef],
        "consolidation": NotRequired[ConsolidationConfigurationTypeDef],
        "reflection": NotRequired[ReflectionConfigurationTypeDef],
        "selfManagedConfiguration": NotRequired[SelfManagedConfigurationTypeDef],
    },
)

class AuthorizerConfigurationOutputTypeDef(TypedDict):
    customJWTAuthorizer: NotRequired[CustomJWTAuthorizerConfigurationOutputTypeDef]

class AuthorizerConfigurationTypeDef(TypedDict):
    customJWTAuthorizer: NotRequired[CustomJWTAuthorizerConfigurationTypeDef]

class EvaluatorConfigOutputTypeDef(TypedDict):
    llmAsAJudge: NotRequired[LlmAsAJudgeEvaluatorConfigOutputTypeDef]

class EvaluatorConfigTypeDef(TypedDict):
    llmAsAJudge: NotRequired[LlmAsAJudgeEvaluatorConfigTypeDef]

AgentRuntimeArtifactUnionTypeDef = Union[
    AgentRuntimeArtifactTypeDef, AgentRuntimeArtifactOutputTypeDef
]

class CreateOnlineEvaluationConfigRequestTypeDef(TypedDict):
    onlineEvaluationConfigName: str
    rule: RuleUnionTypeDef
    dataSourceConfig: DataSourceConfigUnionTypeDef
    evaluators: Sequence[EvaluatorReferenceTypeDef]
    evaluationExecutionRoleArn: str
    enableOnCreate: bool
    clientToken: NotRequired[str]
    description: NotRequired[str]

class UpdateOnlineEvaluationConfigRequestTypeDef(TypedDict):
    onlineEvaluationConfigId: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    rule: NotRequired[RuleUnionTypeDef]
    dataSourceConfig: NotRequired[DataSourceConfigUnionTypeDef]
    evaluators: NotRequired[Sequence[EvaluatorReferenceTypeDef]]
    evaluationExecutionRoleArn: NotRequired[str]
    executionStatus: NotRequired[OnlineEvaluationExecutionStatusType]

class CredentialProviderConfigurationTypeDef(TypedDict):
    credentialProviderType: CredentialProviderTypeType
    credentialProvider: NotRequired[CredentialProviderUnionTypeDef]

class CreateOauth2CredentialProviderResponseTypeDef(TypedDict):
    clientSecretArn: SecretTypeDef
    name: str
    credentialProviderArn: str
    callbackUrl: str
    oauth2ProviderConfigOutput: Oauth2ProviderConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOauth2CredentialProviderResponseTypeDef(TypedDict):
    clientSecretArn: SecretTypeDef
    name: str
    credentialProviderArn: str
    credentialProviderVendor: CredentialProviderVendorTypeType
    callbackUrl: str
    oauth2ProviderConfigOutput: Oauth2ProviderConfigOutputTypeDef
    createdTime: datetime
    lastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOauth2CredentialProviderResponseTypeDef(TypedDict):
    clientSecretArn: SecretTypeDef
    name: str
    credentialProviderVendor: CredentialProviderVendorTypeType
    credentialProviderArn: str
    callbackUrl: str
    oauth2ProviderConfigOutput: Oauth2ProviderConfigOutputTypeDef
    createdTime: datetime
    lastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CustomOauth2ProviderConfigInputTypeDef(TypedDict):
    oauthDiscovery: Oauth2DiscoveryUnionTypeDef
    clientId: str
    clientSecret: str

McpTargetConfigurationOutputTypeDef = TypedDict(
    "McpTargetConfigurationOutputTypeDef",
    {
        "openApiSchema": NotRequired[ApiSchemaConfigurationTypeDef],
        "smithyModel": NotRequired[ApiSchemaConfigurationTypeDef],
        "lambda": NotRequired[McpLambdaTargetConfigurationOutputTypeDef],
        "mcpServer": NotRequired[McpServerTargetConfigurationTypeDef],
        "apiGateway": NotRequired[ApiGatewayTargetConfigurationOutputTypeDef],
    },
)
McpTargetConfigurationTypeDef = TypedDict(
    "McpTargetConfigurationTypeDef",
    {
        "openApiSchema": NotRequired[ApiSchemaConfigurationTypeDef],
        "smithyModel": NotRequired[ApiSchemaConfigurationTypeDef],
        "lambda": NotRequired[McpLambdaTargetConfigurationTypeDef],
        "mcpServer": NotRequired[McpServerTargetConfigurationTypeDef],
        "apiGateway": NotRequired[ApiGatewayTargetConfigurationTypeDef],
    },
)

class ModifyMemoryStrategyInputTypeDef(TypedDict):
    memoryStrategyId: str
    description: NotRequired[str]
    namespaces: NotRequired[Sequence[str]]
    configuration: NotRequired[ModifyStrategyConfigurationTypeDef]

class CustomMemoryStrategyInputTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    namespaces: NotRequired[Sequence[str]]
    configuration: NotRequired[CustomConfigurationInputTypeDef]

MemoryStrategyTypeDef = TypedDict(
    "MemoryStrategyTypeDef",
    {
        "strategyId": str,
        "name": str,
        "type": MemoryStrategyTypeType,
        "namespaces": List[str],
        "description": NotRequired[str],
        "configuration": NotRequired[StrategyConfigurationTypeDef],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "status": NotRequired[MemoryStrategyStatusType],
    },
)

class CreateGatewayResponseTypeDef(TypedDict):
    gatewayArn: str
    gatewayId: str
    gatewayUrl: str
    createdAt: datetime
    updatedAt: datetime
    status: GatewayStatusType
    statusReasons: List[str]
    name: str
    description: str
    roleArn: str
    protocolType: Literal["MCP"]
    protocolConfiguration: GatewayProtocolConfigurationOutputTypeDef
    authorizerType: AuthorizerTypeType
    authorizerConfiguration: AuthorizerConfigurationOutputTypeDef
    kmsKeyArn: str
    interceptorConfigurations: List[GatewayInterceptorConfigurationOutputTypeDef]
    policyEngineConfiguration: GatewayPolicyEngineConfigurationTypeDef
    workloadIdentityDetails: WorkloadIdentityDetailsTypeDef
    exceptionLevel: Literal["DEBUG"]
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentRuntimeResponseTypeDef(TypedDict):
    agentRuntimeArn: str
    agentRuntimeName: str
    agentRuntimeId: str
    agentRuntimeVersion: str
    createdAt: datetime
    lastUpdatedAt: datetime
    roleArn: str
    networkConfiguration: NetworkConfigurationOutputTypeDef
    status: AgentRuntimeStatusType
    lifecycleConfiguration: LifecycleConfigurationTypeDef
    failureReason: str
    description: str
    workloadIdentityDetails: WorkloadIdentityDetailsTypeDef
    agentRuntimeArtifact: AgentRuntimeArtifactOutputTypeDef
    protocolConfiguration: ProtocolConfigurationTypeDef
    environmentVariables: Dict[str, str]
    authorizerConfiguration: AuthorizerConfigurationOutputTypeDef
    requestHeaderConfiguration: RequestHeaderConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGatewayResponseTypeDef(TypedDict):
    gatewayArn: str
    gatewayId: str
    gatewayUrl: str
    createdAt: datetime
    updatedAt: datetime
    status: GatewayStatusType
    statusReasons: List[str]
    name: str
    description: str
    roleArn: str
    protocolType: Literal["MCP"]
    protocolConfiguration: GatewayProtocolConfigurationOutputTypeDef
    authorizerType: AuthorizerTypeType
    authorizerConfiguration: AuthorizerConfigurationOutputTypeDef
    kmsKeyArn: str
    interceptorConfigurations: List[GatewayInterceptorConfigurationOutputTypeDef]
    policyEngineConfiguration: GatewayPolicyEngineConfigurationTypeDef
    workloadIdentityDetails: WorkloadIdentityDetailsTypeDef
    exceptionLevel: Literal["DEBUG"]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayResponseTypeDef(TypedDict):
    gatewayArn: str
    gatewayId: str
    gatewayUrl: str
    createdAt: datetime
    updatedAt: datetime
    status: GatewayStatusType
    statusReasons: List[str]
    name: str
    description: str
    roleArn: str
    protocolType: Literal["MCP"]
    protocolConfiguration: GatewayProtocolConfigurationOutputTypeDef
    authorizerType: AuthorizerTypeType
    authorizerConfiguration: AuthorizerConfigurationOutputTypeDef
    kmsKeyArn: str
    interceptorConfigurations: List[GatewayInterceptorConfigurationOutputTypeDef]
    policyEngineConfiguration: GatewayPolicyEngineConfigurationTypeDef
    workloadIdentityDetails: WorkloadIdentityDetailsTypeDef
    exceptionLevel: Literal["DEBUG"]
    ResponseMetadata: ResponseMetadataTypeDef

AuthorizerConfigurationUnionTypeDef = Union[
    AuthorizerConfigurationTypeDef, AuthorizerConfigurationOutputTypeDef
]

class GetEvaluatorResponseTypeDef(TypedDict):
    evaluatorArn: str
    evaluatorId: str
    evaluatorName: str
    description: str
    evaluatorConfig: EvaluatorConfigOutputTypeDef
    level: EvaluatorLevelType
    status: EvaluatorStatusType
    createdAt: datetime
    updatedAt: datetime
    lockedForModification: bool
    ResponseMetadata: ResponseMetadataTypeDef

EvaluatorConfigUnionTypeDef = Union[EvaluatorConfigTypeDef, EvaluatorConfigOutputTypeDef]
CredentialProviderConfigurationUnionTypeDef = Union[
    CredentialProviderConfigurationTypeDef, CredentialProviderConfigurationOutputTypeDef
]

class Oauth2ProviderConfigInputTypeDef(TypedDict):
    customOauth2ProviderConfig: NotRequired[CustomOauth2ProviderConfigInputTypeDef]
    googleOauth2ProviderConfig: NotRequired[GoogleOauth2ProviderConfigInputTypeDef]
    githubOauth2ProviderConfig: NotRequired[GithubOauth2ProviderConfigInputTypeDef]
    slackOauth2ProviderConfig: NotRequired[SlackOauth2ProviderConfigInputTypeDef]
    salesforceOauth2ProviderConfig: NotRequired[SalesforceOauth2ProviderConfigInputTypeDef]
    microsoftOauth2ProviderConfig: NotRequired[MicrosoftOauth2ProviderConfigInputTypeDef]
    atlassianOauth2ProviderConfig: NotRequired[AtlassianOauth2ProviderConfigInputTypeDef]
    linkedinOauth2ProviderConfig: NotRequired[LinkedinOauth2ProviderConfigInputTypeDef]
    includedOauth2ProviderConfig: NotRequired[IncludedOauth2ProviderConfigInputTypeDef]

class TargetConfigurationOutputTypeDef(TypedDict):
    mcp: NotRequired[McpTargetConfigurationOutputTypeDef]

class TargetConfigurationTypeDef(TypedDict):
    mcp: NotRequired[McpTargetConfigurationTypeDef]

class MemoryStrategyInputTypeDef(TypedDict):
    semanticMemoryStrategy: NotRequired[SemanticMemoryStrategyInputTypeDef]
    summaryMemoryStrategy: NotRequired[SummaryMemoryStrategyInputTypeDef]
    userPreferenceMemoryStrategy: NotRequired[UserPreferenceMemoryStrategyInputTypeDef]
    customMemoryStrategy: NotRequired[CustomMemoryStrategyInputTypeDef]
    episodicMemoryStrategy: NotRequired[EpisodicMemoryStrategyInputTypeDef]

MemoryTypeDef = TypedDict(
    "MemoryTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "eventExpiryDuration": int,
        "status": MemoryStatusType,
        "createdAt": datetime,
        "updatedAt": datetime,
        "description": NotRequired[str],
        "encryptionKeyArn": NotRequired[str],
        "memoryExecutionRoleArn": NotRequired[str],
        "failureReason": NotRequired[str],
        "strategies": NotRequired[List[MemoryStrategyTypeDef]],
    },
)

class CreateAgentRuntimeRequestTypeDef(TypedDict):
    agentRuntimeName: str
    agentRuntimeArtifact: AgentRuntimeArtifactUnionTypeDef
    roleArn: str
    networkConfiguration: NetworkConfigurationUnionTypeDef
    clientToken: NotRequired[str]
    description: NotRequired[str]
    authorizerConfiguration: NotRequired[AuthorizerConfigurationUnionTypeDef]
    requestHeaderConfiguration: NotRequired[RequestHeaderConfigurationUnionTypeDef]
    protocolConfiguration: NotRequired[ProtocolConfigurationTypeDef]
    lifecycleConfiguration: NotRequired[LifecycleConfigurationTypeDef]
    environmentVariables: NotRequired[Mapping[str, str]]
    tags: NotRequired[Mapping[str, str]]

class CreateGatewayRequestTypeDef(TypedDict):
    name: str
    roleArn: str
    protocolType: Literal["MCP"]
    authorizerType: AuthorizerTypeType
    description: NotRequired[str]
    clientToken: NotRequired[str]
    protocolConfiguration: NotRequired[GatewayProtocolConfigurationUnionTypeDef]
    authorizerConfiguration: NotRequired[AuthorizerConfigurationUnionTypeDef]
    kmsKeyArn: NotRequired[str]
    interceptorConfigurations: NotRequired[Sequence[GatewayInterceptorConfigurationUnionTypeDef]]
    policyEngineConfiguration: NotRequired[GatewayPolicyEngineConfigurationTypeDef]
    exceptionLevel: NotRequired[Literal["DEBUG"]]
    tags: NotRequired[Mapping[str, str]]

class UpdateAgentRuntimeRequestTypeDef(TypedDict):
    agentRuntimeId: str
    agentRuntimeArtifact: AgentRuntimeArtifactUnionTypeDef
    roleArn: str
    networkConfiguration: NetworkConfigurationUnionTypeDef
    description: NotRequired[str]
    authorizerConfiguration: NotRequired[AuthorizerConfigurationUnionTypeDef]
    requestHeaderConfiguration: NotRequired[RequestHeaderConfigurationUnionTypeDef]
    protocolConfiguration: NotRequired[ProtocolConfigurationTypeDef]
    lifecycleConfiguration: NotRequired[LifecycleConfigurationTypeDef]
    environmentVariables: NotRequired[Mapping[str, str]]
    clientToken: NotRequired[str]

class UpdateGatewayRequestTypeDef(TypedDict):
    gatewayIdentifier: str
    name: str
    roleArn: str
    protocolType: Literal["MCP"]
    authorizerType: AuthorizerTypeType
    description: NotRequired[str]
    protocolConfiguration: NotRequired[GatewayProtocolConfigurationUnionTypeDef]
    authorizerConfiguration: NotRequired[AuthorizerConfigurationUnionTypeDef]
    kmsKeyArn: NotRequired[str]
    interceptorConfigurations: NotRequired[Sequence[GatewayInterceptorConfigurationUnionTypeDef]]
    policyEngineConfiguration: NotRequired[GatewayPolicyEngineConfigurationTypeDef]
    exceptionLevel: NotRequired[Literal["DEBUG"]]

class CreateEvaluatorRequestTypeDef(TypedDict):
    evaluatorName: str
    evaluatorConfig: EvaluatorConfigUnionTypeDef
    level: EvaluatorLevelType
    clientToken: NotRequired[str]
    description: NotRequired[str]

class UpdateEvaluatorRequestTypeDef(TypedDict):
    evaluatorId: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    evaluatorConfig: NotRequired[EvaluatorConfigUnionTypeDef]
    level: NotRequired[EvaluatorLevelType]

class CreateOauth2CredentialProviderRequestTypeDef(TypedDict):
    name: str
    credentialProviderVendor: CredentialProviderVendorTypeType
    oauth2ProviderConfigInput: Oauth2ProviderConfigInputTypeDef
    tags: NotRequired[Mapping[str, str]]

class UpdateOauth2CredentialProviderRequestTypeDef(TypedDict):
    name: str
    credentialProviderVendor: CredentialProviderVendorTypeType
    oauth2ProviderConfigInput: Oauth2ProviderConfigInputTypeDef

class CreateGatewayTargetResponseTypeDef(TypedDict):
    gatewayArn: str
    targetId: str
    createdAt: datetime
    updatedAt: datetime
    status: TargetStatusType
    statusReasons: List[str]
    name: str
    description: str
    targetConfiguration: TargetConfigurationOutputTypeDef
    credentialProviderConfigurations: List[CredentialProviderConfigurationOutputTypeDef]
    lastSynchronizedAt: datetime
    metadataConfiguration: MetadataConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayTargetTypeDef(TypedDict):
    gatewayArn: str
    targetId: str
    createdAt: datetime
    updatedAt: datetime
    status: TargetStatusType
    name: str
    targetConfiguration: TargetConfigurationOutputTypeDef
    credentialProviderConfigurations: List[CredentialProviderConfigurationOutputTypeDef]
    statusReasons: NotRequired[List[str]]
    description: NotRequired[str]
    lastSynchronizedAt: NotRequired[datetime]
    metadataConfiguration: NotRequired[MetadataConfigurationOutputTypeDef]

class GetGatewayTargetResponseTypeDef(TypedDict):
    gatewayArn: str
    targetId: str
    createdAt: datetime
    updatedAt: datetime
    status: TargetStatusType
    statusReasons: List[str]
    name: str
    description: str
    targetConfiguration: TargetConfigurationOutputTypeDef
    credentialProviderConfigurations: List[CredentialProviderConfigurationOutputTypeDef]
    lastSynchronizedAt: datetime
    metadataConfiguration: MetadataConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayTargetResponseTypeDef(TypedDict):
    gatewayArn: str
    targetId: str
    createdAt: datetime
    updatedAt: datetime
    status: TargetStatusType
    statusReasons: List[str]
    name: str
    description: str
    targetConfiguration: TargetConfigurationOutputTypeDef
    credentialProviderConfigurations: List[CredentialProviderConfigurationOutputTypeDef]
    lastSynchronizedAt: datetime
    metadataConfiguration: MetadataConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

TargetConfigurationUnionTypeDef = Union[
    TargetConfigurationTypeDef, TargetConfigurationOutputTypeDef
]

class CreateMemoryInputTypeDef(TypedDict):
    name: str
    eventExpiryDuration: int
    clientToken: NotRequired[str]
    description: NotRequired[str]
    encryptionKeyArn: NotRequired[str]
    memoryExecutionRoleArn: NotRequired[str]
    memoryStrategies: NotRequired[Sequence[MemoryStrategyInputTypeDef]]
    tags: NotRequired[Mapping[str, str]]

class ModifyMemoryStrategiesTypeDef(TypedDict):
    addMemoryStrategies: NotRequired[Sequence[MemoryStrategyInputTypeDef]]
    modifyMemoryStrategies: NotRequired[Sequence[ModifyMemoryStrategyInputTypeDef]]
    deleteMemoryStrategies: NotRequired[Sequence[DeleteMemoryStrategyInputTypeDef]]

class CreateMemoryOutputTypeDef(TypedDict):
    memory: MemoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMemoryOutputTypeDef(TypedDict):
    memory: MemoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMemoryOutputTypeDef(TypedDict):
    memory: MemoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SynchronizeGatewayTargetsResponseTypeDef(TypedDict):
    targets: List[GatewayTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGatewayTargetRequestTypeDef(TypedDict):
    gatewayIdentifier: str
    name: str
    targetConfiguration: TargetConfigurationUnionTypeDef
    description: NotRequired[str]
    clientToken: NotRequired[str]
    credentialProviderConfigurations: NotRequired[
        Sequence[CredentialProviderConfigurationUnionTypeDef]
    ]
    metadataConfiguration: NotRequired[MetadataConfigurationUnionTypeDef]

class UpdateGatewayTargetRequestTypeDef(TypedDict):
    gatewayIdentifier: str
    targetId: str
    name: str
    targetConfiguration: TargetConfigurationUnionTypeDef
    description: NotRequired[str]
    credentialProviderConfigurations: NotRequired[
        Sequence[CredentialProviderConfigurationUnionTypeDef]
    ]
    metadataConfiguration: NotRequired[MetadataConfigurationUnionTypeDef]

class UpdateMemoryInputTypeDef(TypedDict):
    memoryId: str
    clientToken: NotRequired[str]
    description: NotRequired[str]
    eventExpiryDuration: NotRequired[int]
    memoryExecutionRoleArn: NotRequired[str]
    memoryStrategies: NotRequired[ModifyMemoryStrategiesTypeDef]
