"""
Type annotations for rtbfabric service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_rtbfabric/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_rtbfabric.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    FilterTypeType,
    LinkDirectionType,
    LinkStatusType,
    ProtocolType,
    RequesterGatewayStatusType,
    ResponderErrorMaskingActionType,
    ResponderErrorMaskingLoggingTypeType,
    ResponderGatewayStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AcceptLinkRequestTypeDef",
    "AcceptLinkResponseTypeDef",
    "ActionTypeDef",
    "AutoScalingGroupsConfigurationOutputTypeDef",
    "AutoScalingGroupsConfigurationTypeDef",
    "CreateInboundExternalLinkRequestTypeDef",
    "CreateInboundExternalLinkResponseTypeDef",
    "CreateLinkRequestTypeDef",
    "CreateLinkResponseTypeDef",
    "CreateOutboundExternalLinkRequestTypeDef",
    "CreateOutboundExternalLinkResponseTypeDef",
    "CreateRequesterGatewayRequestTypeDef",
    "CreateRequesterGatewayResponseTypeDef",
    "CreateResponderGatewayRequestTypeDef",
    "CreateResponderGatewayResponseTypeDef",
    "DeleteInboundExternalLinkRequestTypeDef",
    "DeleteInboundExternalLinkResponseTypeDef",
    "DeleteLinkRequestTypeDef",
    "DeleteLinkResponseTypeDef",
    "DeleteOutboundExternalLinkRequestTypeDef",
    "DeleteOutboundExternalLinkResponseTypeDef",
    "DeleteRequesterGatewayRequestTypeDef",
    "DeleteRequesterGatewayResponseTypeDef",
    "DeleteResponderGatewayRequestTypeDef",
    "DeleteResponderGatewayResponseTypeDef",
    "EksEndpointsConfigurationTypeDef",
    "FilterCriterionOutputTypeDef",
    "FilterCriterionTypeDef",
    "FilterCriterionUnionTypeDef",
    "FilterOutputTypeDef",
    "FilterTypeDef",
    "FilterUnionTypeDef",
    "GetInboundExternalLinkRequestTypeDef",
    "GetInboundExternalLinkRequestWaitTypeDef",
    "GetInboundExternalLinkResponseTypeDef",
    "GetLinkRequestTypeDef",
    "GetLinkRequestWaitExtraTypeDef",
    "GetLinkRequestWaitTypeDef",
    "GetLinkResponseTypeDef",
    "GetOutboundExternalLinkRequestTypeDef",
    "GetOutboundExternalLinkRequestWaitTypeDef",
    "GetOutboundExternalLinkResponseTypeDef",
    "GetRequesterGatewayRequestTypeDef",
    "GetRequesterGatewayRequestWaitExtraTypeDef",
    "GetRequesterGatewayRequestWaitTypeDef",
    "GetRequesterGatewayResponseTypeDef",
    "GetResponderGatewayRequestTypeDef",
    "GetResponderGatewayRequestWaitExtraTypeDef",
    "GetResponderGatewayRequestWaitTypeDef",
    "GetResponderGatewayResponseTypeDef",
    "HeaderTagActionTypeDef",
    "LinkApplicationLogConfigurationTypeDef",
    "LinkApplicationLogSamplingTypeDef",
    "LinkAttributesOutputTypeDef",
    "LinkAttributesTypeDef",
    "LinkAttributesUnionTypeDef",
    "LinkLogSettingsTypeDef",
    "ListLinksRequestPaginateTypeDef",
    "ListLinksRequestTypeDef",
    "ListLinksResponseStructureTypeDef",
    "ListLinksResponseTypeDef",
    "ListRequesterGatewaysRequestPaginateTypeDef",
    "ListRequesterGatewaysRequestTypeDef",
    "ListRequesterGatewaysResponseTypeDef",
    "ListResponderGatewaysRequestPaginateTypeDef",
    "ListResponderGatewaysRequestTypeDef",
    "ListResponderGatewaysResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManagedEndpointConfigurationOutputTypeDef",
    "ManagedEndpointConfigurationTypeDef",
    "ManagedEndpointConfigurationUnionTypeDef",
    "ModuleConfigurationOutputTypeDef",
    "ModuleConfigurationTypeDef",
    "ModuleConfigurationUnionTypeDef",
    "ModuleParametersOutputTypeDef",
    "ModuleParametersTypeDef",
    "ModuleParametersUnionTypeDef",
    "NoBidActionTypeDef",
    "NoBidModuleParametersTypeDef",
    "OpenRtbAttributeModuleParametersOutputTypeDef",
    "OpenRtbAttributeModuleParametersTypeDef",
    "OpenRtbAttributeModuleParametersUnionTypeDef",
    "PaginatorConfigTypeDef",
    "RateLimiterModuleParametersTypeDef",
    "RejectLinkRequestTypeDef",
    "RejectLinkResponseTypeDef",
    "ResponderErrorMaskingForHttpCodeOutputTypeDef",
    "ResponderErrorMaskingForHttpCodeTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TrustStoreConfigurationOutputTypeDef",
    "TrustStoreConfigurationTypeDef",
    "TrustStoreConfigurationUnionTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateLinkModuleFlowRequestTypeDef",
    "UpdateLinkModuleFlowResponseTypeDef",
    "UpdateLinkRequestTypeDef",
    "UpdateLinkResponseTypeDef",
    "UpdateRequesterGatewayRequestTypeDef",
    "UpdateRequesterGatewayResponseTypeDef",
    "UpdateResponderGatewayRequestTypeDef",
    "UpdateResponderGatewayResponseTypeDef",
    "WaiterConfigTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class HeaderTagActionTypeDef(TypedDict):
    name: str
    value: str

class NoBidActionTypeDef(TypedDict):
    noBidReasonCode: NotRequired[int]

class AutoScalingGroupsConfigurationOutputTypeDef(TypedDict):
    autoScalingGroupNames: List[str]
    roleArn: str

class AutoScalingGroupsConfigurationTypeDef(TypedDict):
    autoScalingGroupNames: Sequence[str]
    roleArn: str

class CreateRequesterGatewayRequestTypeDef(TypedDict):
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]
    clientToken: str
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class DeleteInboundExternalLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str

class DeleteLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str

class DeleteOutboundExternalLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str

class DeleteRequesterGatewayRequestTypeDef(TypedDict):
    gatewayId: str

class DeleteResponderGatewayRequestTypeDef(TypedDict):
    gatewayId: str

class EksEndpointsConfigurationTypeDef(TypedDict):
    endpointsResourceName: str
    endpointsResourceNamespace: str
    clusterApiServerEndpointUri: str
    clusterApiServerCaCertificateChain: str
    clusterName: str
    roleArn: str

class FilterCriterionOutputTypeDef(TypedDict):
    path: str
    values: List[str]

class FilterCriterionTypeDef(TypedDict):
    path: str
    values: Sequence[str]

class GetInboundExternalLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str

class GetOutboundExternalLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str

class GetRequesterGatewayRequestTypeDef(TypedDict):
    gatewayId: str

class GetResponderGatewayRequestTypeDef(TypedDict):
    gatewayId: str

class TrustStoreConfigurationOutputTypeDef(TypedDict):
    certificateAuthorityCertificates: List[str]

class LinkApplicationLogSamplingTypeDef(TypedDict):
    errorLog: float
    filterLog: float

class ResponderErrorMaskingForHttpCodeOutputTypeDef(TypedDict):
    httpCode: str
    action: ResponderErrorMaskingActionType
    loggingTypes: List[ResponderErrorMaskingLoggingTypeType]
    responseLoggingPercentage: NotRequired[float]

class ResponderErrorMaskingForHttpCodeTypeDef(TypedDict):
    httpCode: str
    action: ResponderErrorMaskingActionType
    loggingTypes: Sequence[ResponderErrorMaskingLoggingTypeType]
    responseLoggingPercentage: NotRequired[float]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListLinksRequestTypeDef(TypedDict):
    gatewayId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListRequesterGatewaysRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListResponderGatewaysRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class NoBidModuleParametersTypeDef(TypedDict):
    reason: NotRequired[str]
    reasonCode: NotRequired[int]
    passThroughPercentage: NotRequired[float]

class RateLimiterModuleParametersTypeDef(TypedDict):
    tps: NotRequired[float]

class RejectLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TrustStoreConfigurationTypeDef(TypedDict):
    certificateAuthorityCertificates: Sequence[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateRequesterGatewayRequestTypeDef(TypedDict):
    clientToken: str
    gatewayId: str
    description: NotRequired[str]

class CreateInboundExternalLinkResponseTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    status: LinkStatusType
    domainName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOutboundExternalLinkResponseTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    status: LinkStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRequesterGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    domainName: str
    status: RequesterGatewayStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResponderGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    status: ResponderGatewayStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInboundExternalLinkResponseTypeDef(TypedDict):
    linkId: str
    status: LinkStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLinkResponseTypeDef(TypedDict):
    linkId: str
    status: LinkStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteOutboundExternalLinkResponseTypeDef(TypedDict):
    linkId: str
    status: LinkStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRequesterGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    status: RequesterGatewayStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResponderGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    status: ResponderGatewayStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetRequesterGatewayResponseTypeDef(TypedDict):
    status: RequesterGatewayStatusType
    domainName: str
    description: str
    createdAt: datetime
    updatedAt: datetime
    vpcId: str
    subnetIds: List[str]
    securityGroupIds: List[str]
    gatewayId: str
    tags: Dict[str, str]
    activeLinksCount: int
    totalLinksCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListRequesterGatewaysResponseTypeDef(TypedDict):
    gatewayIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResponderGatewaysResponseTypeDef(TypedDict):
    gatewayIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLinkModuleFlowResponseTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    status: LinkStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLinkResponseTypeDef(TypedDict):
    linkId: str
    status: LinkStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRequesterGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    status: RequesterGatewayStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResponderGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    status: ResponderGatewayStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ActionTypeDef(TypedDict):
    noBid: NotRequired[NoBidActionTypeDef]
    headerTag: NotRequired[HeaderTagActionTypeDef]

class ManagedEndpointConfigurationOutputTypeDef(TypedDict):
    autoScalingGroups: NotRequired[AutoScalingGroupsConfigurationOutputTypeDef]
    eksEndpoints: NotRequired[EksEndpointsConfigurationTypeDef]

class ManagedEndpointConfigurationTypeDef(TypedDict):
    autoScalingGroups: NotRequired[AutoScalingGroupsConfigurationTypeDef]
    eksEndpoints: NotRequired[EksEndpointsConfigurationTypeDef]

class FilterOutputTypeDef(TypedDict):
    criteria: List[FilterCriterionOutputTypeDef]

FilterCriterionUnionTypeDef = Union[FilterCriterionTypeDef, FilterCriterionOutputTypeDef]

class GetInboundExternalLinkRequestWaitTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetLinkRequestWaitExtraTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetLinkRequestWaitTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetOutboundExternalLinkRequestWaitTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRequesterGatewayRequestWaitExtraTypeDef(TypedDict):
    gatewayId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetRequesterGatewayRequestWaitTypeDef(TypedDict):
    gatewayId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetResponderGatewayRequestWaitExtraTypeDef(TypedDict):
    gatewayId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetResponderGatewayRequestWaitTypeDef(TypedDict):
    gatewayId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class LinkApplicationLogConfigurationTypeDef(TypedDict):
    sampling: LinkApplicationLogSamplingTypeDef

class LinkAttributesOutputTypeDef(TypedDict):
    responderErrorMasking: NotRequired[List[ResponderErrorMaskingForHttpCodeOutputTypeDef]]
    customerProvidedId: NotRequired[str]

class LinkAttributesTypeDef(TypedDict):
    responderErrorMasking: NotRequired[Sequence[ResponderErrorMaskingForHttpCodeTypeDef]]
    customerProvidedId: NotRequired[str]

class ListLinksRequestPaginateTypeDef(TypedDict):
    gatewayId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRequesterGatewaysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResponderGatewaysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

TrustStoreConfigurationUnionTypeDef = Union[
    TrustStoreConfigurationTypeDef, TrustStoreConfigurationOutputTypeDef
]

class GetResponderGatewayResponseTypeDef(TypedDict):
    vpcId: str
    subnetIds: List[str]
    securityGroupIds: List[str]
    status: ResponderGatewayStatusType
    description: str
    createdAt: datetime
    updatedAt: datetime
    domainName: str
    port: int
    protocol: ProtocolType
    trustStoreConfiguration: TrustStoreConfigurationOutputTypeDef
    managedEndpointConfiguration: ManagedEndpointConfigurationOutputTypeDef
    gatewayId: str
    tags: Dict[str, str]
    activeLinksCount: int
    totalLinksCount: int
    inboundLinksCount: int
    ResponseMetadata: ResponseMetadataTypeDef

ManagedEndpointConfigurationUnionTypeDef = Union[
    ManagedEndpointConfigurationTypeDef, ManagedEndpointConfigurationOutputTypeDef
]

class OpenRtbAttributeModuleParametersOutputTypeDef(TypedDict):
    filterType: FilterTypeType
    filterConfiguration: List[FilterOutputTypeDef]
    action: ActionTypeDef
    holdbackPercentage: float

class FilterTypeDef(TypedDict):
    criteria: Sequence[FilterCriterionUnionTypeDef]

class LinkLogSettingsTypeDef(TypedDict):
    applicationLogs: LinkApplicationLogConfigurationTypeDef

LinkAttributesUnionTypeDef = Union[LinkAttributesTypeDef, LinkAttributesOutputTypeDef]

class CreateResponderGatewayRequestTypeDef(TypedDict):
    vpcId: str
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]
    port: int
    protocol: ProtocolType
    clientToken: str
    domainName: NotRequired[str]
    trustStoreConfiguration: NotRequired[TrustStoreConfigurationUnionTypeDef]
    managedEndpointConfiguration: NotRequired[ManagedEndpointConfigurationUnionTypeDef]
    description: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateResponderGatewayRequestTypeDef(TypedDict):
    port: int
    protocol: ProtocolType
    clientToken: str
    gatewayId: str
    domainName: NotRequired[str]
    trustStoreConfiguration: NotRequired[TrustStoreConfigurationUnionTypeDef]
    managedEndpointConfiguration: NotRequired[ManagedEndpointConfigurationUnionTypeDef]
    description: NotRequired[str]

class ModuleParametersOutputTypeDef(TypedDict):
    noBid: NotRequired[NoBidModuleParametersTypeDef]
    openRtbAttribute: NotRequired[OpenRtbAttributeModuleParametersOutputTypeDef]
    rateLimiter: NotRequired[RateLimiterModuleParametersTypeDef]

FilterUnionTypeDef = Union[FilterTypeDef, FilterOutputTypeDef]

class GetOutboundExternalLinkResponseTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    status: LinkStatusType
    publicEndpoint: str
    createdAt: datetime
    updatedAt: datetime
    tags: Dict[str, str]
    logSettings: LinkLogSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    logSettings: NotRequired[LinkLogSettingsTypeDef]

class AcceptLinkRequestTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    logSettings: LinkLogSettingsTypeDef
    attributes: NotRequired[LinkAttributesUnionTypeDef]

class CreateInboundExternalLinkRequestTypeDef(TypedDict):
    clientToken: str
    gatewayId: str
    logSettings: LinkLogSettingsTypeDef
    attributes: NotRequired[LinkAttributesUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]

class CreateLinkRequestTypeDef(TypedDict):
    gatewayId: str
    peerGatewayId: str
    logSettings: LinkLogSettingsTypeDef
    attributes: NotRequired[LinkAttributesUnionTypeDef]
    httpResponderAllowed: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]

class CreateOutboundExternalLinkRequestTypeDef(TypedDict):
    clientToken: str
    gatewayId: str
    publicEndpoint: str
    logSettings: LinkLogSettingsTypeDef
    attributes: NotRequired[LinkAttributesUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]

class ModuleConfigurationOutputTypeDef(TypedDict):
    name: str
    version: NotRequired[str]
    dependsOn: NotRequired[List[str]]
    moduleParameters: NotRequired[ModuleParametersOutputTypeDef]

class OpenRtbAttributeModuleParametersTypeDef(TypedDict):
    filterType: FilterTypeType
    filterConfiguration: Sequence[FilterUnionTypeDef]
    action: ActionTypeDef
    holdbackPercentage: float

class AcceptLinkResponseTypeDef(TypedDict):
    gatewayId: str
    peerGatewayId: str
    status: LinkStatusType
    createdAt: datetime
    updatedAt: datetime
    direction: LinkDirectionType
    flowModules: List[ModuleConfigurationOutputTypeDef]
    pendingFlowModules: List[ModuleConfigurationOutputTypeDef]
    attributes: LinkAttributesOutputTypeDef
    linkId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLinkResponseTypeDef(TypedDict):
    gatewayId: str
    peerGatewayId: str
    status: LinkStatusType
    createdAt: datetime
    updatedAt: datetime
    direction: LinkDirectionType
    flowModules: List[ModuleConfigurationOutputTypeDef]
    pendingFlowModules: List[ModuleConfigurationOutputTypeDef]
    attributes: LinkAttributesOutputTypeDef
    linkId: str
    customerProvidedId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInboundExternalLinkResponseTypeDef(TypedDict):
    gatewayId: str
    linkId: str
    status: LinkStatusType
    domainName: str
    flowModules: List[ModuleConfigurationOutputTypeDef]
    pendingFlowModules: List[ModuleConfigurationOutputTypeDef]
    attributes: LinkAttributesOutputTypeDef
    createdAt: datetime
    updatedAt: datetime
    tags: Dict[str, str]
    logSettings: LinkLogSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinkResponseTypeDef(TypedDict):
    gatewayId: str
    peerGatewayId: str
    status: LinkStatusType
    createdAt: datetime
    updatedAt: datetime
    direction: LinkDirectionType
    flowModules: List[ModuleConfigurationOutputTypeDef]
    pendingFlowModules: List[ModuleConfigurationOutputTypeDef]
    attributes: LinkAttributesOutputTypeDef
    linkId: str
    tags: Dict[str, str]
    logSettings: LinkLogSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLinksResponseStructureTypeDef(TypedDict):
    gatewayId: str
    peerGatewayId: str
    status: LinkStatusType
    createdAt: datetime
    updatedAt: datetime
    linkId: str
    direction: NotRequired[LinkDirectionType]
    flowModules: NotRequired[List[ModuleConfigurationOutputTypeDef]]
    pendingFlowModules: NotRequired[List[ModuleConfigurationOutputTypeDef]]
    attributes: NotRequired[LinkAttributesOutputTypeDef]
    tags: NotRequired[Dict[str, str]]

class RejectLinkResponseTypeDef(TypedDict):
    gatewayId: str
    peerGatewayId: str
    status: LinkStatusType
    createdAt: datetime
    updatedAt: datetime
    direction: LinkDirectionType
    flowModules: List[ModuleConfigurationOutputTypeDef]
    pendingFlowModules: List[ModuleConfigurationOutputTypeDef]
    attributes: LinkAttributesOutputTypeDef
    linkId: str
    ResponseMetadata: ResponseMetadataTypeDef

OpenRtbAttributeModuleParametersUnionTypeDef = Union[
    OpenRtbAttributeModuleParametersTypeDef, OpenRtbAttributeModuleParametersOutputTypeDef
]

class ListLinksResponseTypeDef(TypedDict):
    links: List[ListLinksResponseStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ModuleParametersTypeDef(TypedDict):
    noBid: NotRequired[NoBidModuleParametersTypeDef]
    openRtbAttribute: NotRequired[OpenRtbAttributeModuleParametersUnionTypeDef]
    rateLimiter: NotRequired[RateLimiterModuleParametersTypeDef]

ModuleParametersUnionTypeDef = Union[ModuleParametersTypeDef, ModuleParametersOutputTypeDef]

class ModuleConfigurationTypeDef(TypedDict):
    name: str
    version: NotRequired[str]
    dependsOn: NotRequired[Sequence[str]]
    moduleParameters: NotRequired[ModuleParametersUnionTypeDef]

ModuleConfigurationUnionTypeDef = Union[
    ModuleConfigurationTypeDef, ModuleConfigurationOutputTypeDef
]

class UpdateLinkModuleFlowRequestTypeDef(TypedDict):
    clientToken: str
    gatewayId: str
    linkId: str
    modules: Sequence[ModuleConfigurationUnionTypeDef]
