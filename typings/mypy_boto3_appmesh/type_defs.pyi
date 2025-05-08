"""
Type annotations for appmesh service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_appmesh/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_appmesh.type_defs import AwsCloudMapInstanceAttributeTypeDef

    data: AwsCloudMapInstanceAttributeTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    DefaultGatewayRouteRewriteType,
    DnsResponseTypeType,
    DurationUnitType,
    EgressFilterTypeType,
    GatewayRouteStatusCodeType,
    GrpcRetryPolicyEventType,
    HttpMethodType,
    HttpSchemeType,
    IpPreferenceType,
    ListenerTlsModeType,
    MeshStatusCodeType,
    PortProtocolType,
    RouteStatusCodeType,
    VirtualGatewayListenerTlsModeType,
    VirtualGatewayPortProtocolType,
    VirtualGatewayStatusCodeType,
    VirtualNodeStatusCodeType,
    VirtualRouterStatusCodeType,
    VirtualServiceStatusCodeType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessLogOutputTypeDef",
    "AccessLogTypeDef",
    "AwsCloudMapInstanceAttributeTypeDef",
    "AwsCloudMapServiceDiscoveryOutputTypeDef",
    "AwsCloudMapServiceDiscoveryTypeDef",
    "BackendDefaultsOutputTypeDef",
    "BackendDefaultsTypeDef",
    "BackendOutputTypeDef",
    "BackendTypeDef",
    "ClientPolicyOutputTypeDef",
    "ClientPolicyTlsOutputTypeDef",
    "ClientPolicyTlsTypeDef",
    "ClientPolicyTypeDef",
    "ClientTlsCertificateTypeDef",
    "CreateGatewayRouteInputTypeDef",
    "CreateGatewayRouteOutputTypeDef",
    "CreateMeshInputTypeDef",
    "CreateMeshOutputTypeDef",
    "CreateRouteInputTypeDef",
    "CreateRouteOutputTypeDef",
    "CreateVirtualGatewayInputTypeDef",
    "CreateVirtualGatewayOutputTypeDef",
    "CreateVirtualNodeInputTypeDef",
    "CreateVirtualNodeOutputTypeDef",
    "CreateVirtualRouterInputTypeDef",
    "CreateVirtualRouterOutputTypeDef",
    "CreateVirtualServiceInputTypeDef",
    "CreateVirtualServiceOutputTypeDef",
    "DeleteGatewayRouteInputTypeDef",
    "DeleteGatewayRouteOutputTypeDef",
    "DeleteMeshInputTypeDef",
    "DeleteMeshOutputTypeDef",
    "DeleteRouteInputTypeDef",
    "DeleteRouteOutputTypeDef",
    "DeleteVirtualGatewayInputTypeDef",
    "DeleteVirtualGatewayOutputTypeDef",
    "DeleteVirtualNodeInputTypeDef",
    "DeleteVirtualNodeOutputTypeDef",
    "DeleteVirtualRouterInputTypeDef",
    "DeleteVirtualRouterOutputTypeDef",
    "DeleteVirtualServiceInputTypeDef",
    "DeleteVirtualServiceOutputTypeDef",
    "DescribeGatewayRouteInputTypeDef",
    "DescribeGatewayRouteOutputTypeDef",
    "DescribeMeshInputTypeDef",
    "DescribeMeshOutputTypeDef",
    "DescribeRouteInputTypeDef",
    "DescribeRouteOutputTypeDef",
    "DescribeVirtualGatewayInputTypeDef",
    "DescribeVirtualGatewayOutputTypeDef",
    "DescribeVirtualNodeInputTypeDef",
    "DescribeVirtualNodeOutputTypeDef",
    "DescribeVirtualRouterInputTypeDef",
    "DescribeVirtualRouterOutputTypeDef",
    "DescribeVirtualServiceInputTypeDef",
    "DescribeVirtualServiceOutputTypeDef",
    "DnsServiceDiscoveryTypeDef",
    "DurationTypeDef",
    "EgressFilterTypeDef",
    "FileAccessLogOutputTypeDef",
    "FileAccessLogTypeDef",
    "GatewayRouteDataTypeDef",
    "GatewayRouteHostnameMatchTypeDef",
    "GatewayRouteHostnameRewriteTypeDef",
    "GatewayRouteRefTypeDef",
    "GatewayRouteSpecOutputTypeDef",
    "GatewayRouteSpecTypeDef",
    "GatewayRouteSpecUnionTypeDef",
    "GatewayRouteStatusTypeDef",
    "GatewayRouteTargetTypeDef",
    "GatewayRouteVirtualServiceTypeDef",
    "GrpcGatewayRouteActionTypeDef",
    "GrpcGatewayRouteMatchOutputTypeDef",
    "GrpcGatewayRouteMatchTypeDef",
    "GrpcGatewayRouteMetadataTypeDef",
    "GrpcGatewayRouteOutputTypeDef",
    "GrpcGatewayRouteRewriteTypeDef",
    "GrpcGatewayRouteTypeDef",
    "GrpcMetadataMatchMethodTypeDef",
    "GrpcRetryPolicyOutputTypeDef",
    "GrpcRetryPolicyTypeDef",
    "GrpcRouteActionOutputTypeDef",
    "GrpcRouteActionTypeDef",
    "GrpcRouteMatchOutputTypeDef",
    "GrpcRouteMatchTypeDef",
    "GrpcRouteMetadataMatchMethodTypeDef",
    "GrpcRouteMetadataTypeDef",
    "GrpcRouteOutputTypeDef",
    "GrpcRouteTypeDef",
    "GrpcTimeoutTypeDef",
    "HeaderMatchMethodTypeDef",
    "HealthCheckPolicyTypeDef",
    "HttpGatewayRouteActionTypeDef",
    "HttpGatewayRouteHeaderTypeDef",
    "HttpGatewayRouteMatchOutputTypeDef",
    "HttpGatewayRouteMatchTypeDef",
    "HttpGatewayRouteOutputTypeDef",
    "HttpGatewayRoutePathRewriteTypeDef",
    "HttpGatewayRoutePrefixRewriteTypeDef",
    "HttpGatewayRouteRewriteTypeDef",
    "HttpGatewayRouteTypeDef",
    "HttpPathMatchTypeDef",
    "HttpQueryParameterTypeDef",
    "HttpRetryPolicyOutputTypeDef",
    "HttpRetryPolicyTypeDef",
    "HttpRouteActionOutputTypeDef",
    "HttpRouteActionTypeDef",
    "HttpRouteHeaderTypeDef",
    "HttpRouteMatchOutputTypeDef",
    "HttpRouteMatchTypeDef",
    "HttpRouteOutputTypeDef",
    "HttpRouteTypeDef",
    "HttpTimeoutTypeDef",
    "JsonFormatRefTypeDef",
    "ListGatewayRoutesInputPaginateTypeDef",
    "ListGatewayRoutesInputTypeDef",
    "ListGatewayRoutesOutputTypeDef",
    "ListMeshesInputPaginateTypeDef",
    "ListMeshesInputTypeDef",
    "ListMeshesOutputTypeDef",
    "ListRoutesInputPaginateTypeDef",
    "ListRoutesInputTypeDef",
    "ListRoutesOutputTypeDef",
    "ListTagsForResourceInputPaginateTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVirtualGatewaysInputPaginateTypeDef",
    "ListVirtualGatewaysInputTypeDef",
    "ListVirtualGatewaysOutputTypeDef",
    "ListVirtualNodesInputPaginateTypeDef",
    "ListVirtualNodesInputTypeDef",
    "ListVirtualNodesOutputTypeDef",
    "ListVirtualRoutersInputPaginateTypeDef",
    "ListVirtualRoutersInputTypeDef",
    "ListVirtualRoutersOutputTypeDef",
    "ListVirtualServicesInputPaginateTypeDef",
    "ListVirtualServicesInputTypeDef",
    "ListVirtualServicesOutputTypeDef",
    "ListenerOutputTypeDef",
    "ListenerTimeoutTypeDef",
    "ListenerTlsAcmCertificateTypeDef",
    "ListenerTlsCertificateTypeDef",
    "ListenerTlsFileCertificateTypeDef",
    "ListenerTlsOutputTypeDef",
    "ListenerTlsSdsCertificateTypeDef",
    "ListenerTlsTypeDef",
    "ListenerTlsValidationContextOutputTypeDef",
    "ListenerTlsValidationContextTrustTypeDef",
    "ListenerTlsValidationContextTypeDef",
    "ListenerTypeDef",
    "LoggingFormatOutputTypeDef",
    "LoggingFormatTypeDef",
    "LoggingOutputTypeDef",
    "LoggingTypeDef",
    "MatchRangeTypeDef",
    "MeshDataTypeDef",
    "MeshRefTypeDef",
    "MeshServiceDiscoveryTypeDef",
    "MeshSpecTypeDef",
    "MeshStatusTypeDef",
    "OutlierDetectionTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "QueryParameterMatchTypeDef",
    "ResourceMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "RouteDataTypeDef",
    "RouteRefTypeDef",
    "RouteSpecOutputTypeDef",
    "RouteSpecTypeDef",
    "RouteSpecUnionTypeDef",
    "RouteStatusTypeDef",
    "ServiceDiscoveryOutputTypeDef",
    "ServiceDiscoveryTypeDef",
    "SubjectAlternativeNameMatchersOutputTypeDef",
    "SubjectAlternativeNameMatchersTypeDef",
    "SubjectAlternativeNamesOutputTypeDef",
    "SubjectAlternativeNamesTypeDef",
    "TagRefTypeDef",
    "TagResourceInputTypeDef",
    "TcpRouteActionOutputTypeDef",
    "TcpRouteActionTypeDef",
    "TcpRouteMatchTypeDef",
    "TcpRouteOutputTypeDef",
    "TcpRouteTypeDef",
    "TcpTimeoutTypeDef",
    "TlsValidationContextAcmTrustOutputTypeDef",
    "TlsValidationContextAcmTrustTypeDef",
    "TlsValidationContextFileTrustTypeDef",
    "TlsValidationContextOutputTypeDef",
    "TlsValidationContextSdsTrustTypeDef",
    "TlsValidationContextTrustOutputTypeDef",
    "TlsValidationContextTrustTypeDef",
    "TlsValidationContextTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateGatewayRouteInputTypeDef",
    "UpdateGatewayRouteOutputTypeDef",
    "UpdateMeshInputTypeDef",
    "UpdateMeshOutputTypeDef",
    "UpdateRouteInputTypeDef",
    "UpdateRouteOutputTypeDef",
    "UpdateVirtualGatewayInputTypeDef",
    "UpdateVirtualGatewayOutputTypeDef",
    "UpdateVirtualNodeInputTypeDef",
    "UpdateVirtualNodeOutputTypeDef",
    "UpdateVirtualRouterInputTypeDef",
    "UpdateVirtualRouterOutputTypeDef",
    "UpdateVirtualServiceInputTypeDef",
    "UpdateVirtualServiceOutputTypeDef",
    "VirtualGatewayAccessLogOutputTypeDef",
    "VirtualGatewayAccessLogTypeDef",
    "VirtualGatewayBackendDefaultsOutputTypeDef",
    "VirtualGatewayBackendDefaultsTypeDef",
    "VirtualGatewayClientPolicyOutputTypeDef",
    "VirtualGatewayClientPolicyTlsOutputTypeDef",
    "VirtualGatewayClientPolicyTlsTypeDef",
    "VirtualGatewayClientPolicyTypeDef",
    "VirtualGatewayClientTlsCertificateTypeDef",
    "VirtualGatewayConnectionPoolTypeDef",
    "VirtualGatewayDataTypeDef",
    "VirtualGatewayFileAccessLogOutputTypeDef",
    "VirtualGatewayFileAccessLogTypeDef",
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    "VirtualGatewayHealthCheckPolicyTypeDef",
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    "VirtualGatewayHttpConnectionPoolTypeDef",
    "VirtualGatewayListenerOutputTypeDef",
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    "VirtualGatewayListenerTlsCertificateTypeDef",
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    "VirtualGatewayListenerTlsOutputTypeDef",
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    "VirtualGatewayListenerTlsTypeDef",
    "VirtualGatewayListenerTlsValidationContextOutputTypeDef",
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    "VirtualGatewayListenerTypeDef",
    "VirtualGatewayLoggingOutputTypeDef",
    "VirtualGatewayLoggingTypeDef",
    "VirtualGatewayPortMappingTypeDef",
    "VirtualGatewayRefTypeDef",
    "VirtualGatewaySpecOutputTypeDef",
    "VirtualGatewaySpecTypeDef",
    "VirtualGatewaySpecUnionTypeDef",
    "VirtualGatewayStatusTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    "VirtualGatewayTlsValidationContextOutputTypeDef",
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    "VirtualGatewayTlsValidationContextTrustOutputTypeDef",
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    "VirtualGatewayTlsValidationContextTypeDef",
    "VirtualNodeConnectionPoolTypeDef",
    "VirtualNodeDataTypeDef",
    "VirtualNodeGrpcConnectionPoolTypeDef",
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    "VirtualNodeHttpConnectionPoolTypeDef",
    "VirtualNodeRefTypeDef",
    "VirtualNodeServiceProviderTypeDef",
    "VirtualNodeSpecOutputTypeDef",
    "VirtualNodeSpecTypeDef",
    "VirtualNodeSpecUnionTypeDef",
    "VirtualNodeStatusTypeDef",
    "VirtualNodeTcpConnectionPoolTypeDef",
    "VirtualRouterDataTypeDef",
    "VirtualRouterListenerTypeDef",
    "VirtualRouterRefTypeDef",
    "VirtualRouterServiceProviderTypeDef",
    "VirtualRouterSpecOutputTypeDef",
    "VirtualRouterSpecTypeDef",
    "VirtualRouterSpecUnionTypeDef",
    "VirtualRouterStatusTypeDef",
    "VirtualServiceBackendOutputTypeDef",
    "VirtualServiceBackendTypeDef",
    "VirtualServiceDataTypeDef",
    "VirtualServiceProviderTypeDef",
    "VirtualServiceRefTypeDef",
    "VirtualServiceSpecTypeDef",
    "VirtualServiceStatusTypeDef",
    "WeightedTargetTypeDef",
)

class AwsCloudMapInstanceAttributeTypeDef(TypedDict):
    key: str
    value: str

class ListenerTlsFileCertificateTypeDef(TypedDict):
    certificateChain: str
    privateKey: str

class ListenerTlsSdsCertificateTypeDef(TypedDict):
    secretName: str

class TagRefTypeDef(TypedDict):
    key: str
    value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteGatewayRouteInputTypeDef(TypedDict):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: NotRequired[str]

class DeleteMeshInputTypeDef(TypedDict):
    meshName: str

class DeleteRouteInputTypeDef(TypedDict):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: NotRequired[str]

class DeleteVirtualGatewayInputTypeDef(TypedDict):
    meshName: str
    virtualGatewayName: str
    meshOwner: NotRequired[str]

class DeleteVirtualNodeInputTypeDef(TypedDict):
    meshName: str
    virtualNodeName: str
    meshOwner: NotRequired[str]

class DeleteVirtualRouterInputTypeDef(TypedDict):
    meshName: str
    virtualRouterName: str
    meshOwner: NotRequired[str]

class DeleteVirtualServiceInputTypeDef(TypedDict):
    meshName: str
    virtualServiceName: str
    meshOwner: NotRequired[str]

class DescribeGatewayRouteInputTypeDef(TypedDict):
    gatewayRouteName: str
    meshName: str
    virtualGatewayName: str
    meshOwner: NotRequired[str]

class DescribeMeshInputTypeDef(TypedDict):
    meshName: str
    meshOwner: NotRequired[str]

class DescribeRouteInputTypeDef(TypedDict):
    meshName: str
    routeName: str
    virtualRouterName: str
    meshOwner: NotRequired[str]

class DescribeVirtualGatewayInputTypeDef(TypedDict):
    meshName: str
    virtualGatewayName: str
    meshOwner: NotRequired[str]

class DescribeVirtualNodeInputTypeDef(TypedDict):
    meshName: str
    virtualNodeName: str
    meshOwner: NotRequired[str]

class DescribeVirtualRouterInputTypeDef(TypedDict):
    meshName: str
    virtualRouterName: str
    meshOwner: NotRequired[str]

class DescribeVirtualServiceInputTypeDef(TypedDict):
    meshName: str
    virtualServiceName: str
    meshOwner: NotRequired[str]

class DnsServiceDiscoveryTypeDef(TypedDict):
    hostname: str
    ipPreference: NotRequired[IpPreferenceType]
    responseType: NotRequired[DnsResponseTypeType]

class DurationTypeDef(TypedDict):
    unit: NotRequired[DurationUnitType]
    value: NotRequired[int]

EgressFilterTypeDef = TypedDict(
    "EgressFilterTypeDef",
    {
        "type": EgressFilterTypeType,
    },
)

class GatewayRouteStatusTypeDef(TypedDict):
    status: GatewayRouteStatusCodeType

class ResourceMetadataTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshOwner: str
    resourceOwner: str
    uid: str
    version: int

class GatewayRouteHostnameMatchTypeDef(TypedDict):
    exact: NotRequired[str]
    suffix: NotRequired[str]

class GatewayRouteHostnameRewriteTypeDef(TypedDict):
    defaultTargetHostname: NotRequired[DefaultGatewayRouteRewriteType]

class GatewayRouteRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    gatewayRouteName: str
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str

class GatewayRouteVirtualServiceTypeDef(TypedDict):
    virtualServiceName: str

class MatchRangeTypeDef(TypedDict):
    end: int
    start: int

class WeightedTargetTypeDef(TypedDict):
    virtualNode: str
    weight: int
    port: NotRequired[int]

class HealthCheckPolicyTypeDef(TypedDict):
    healthyThreshold: int
    intervalMillis: int
    protocol: PortProtocolType
    timeoutMillis: int
    unhealthyThreshold: int
    path: NotRequired[str]
    port: NotRequired[int]

class HttpPathMatchTypeDef(TypedDict):
    exact: NotRequired[str]
    regex: NotRequired[str]

class HttpGatewayRoutePathRewriteTypeDef(TypedDict):
    exact: NotRequired[str]

class HttpGatewayRoutePrefixRewriteTypeDef(TypedDict):
    defaultPrefix: NotRequired[DefaultGatewayRouteRewriteType]
    value: NotRequired[str]

class QueryParameterMatchTypeDef(TypedDict):
    exact: NotRequired[str]

class JsonFormatRefTypeDef(TypedDict):
    key: str
    value: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListGatewayRoutesInputTypeDef(TypedDict):
    meshName: str
    virtualGatewayName: str
    limit: NotRequired[int]
    meshOwner: NotRequired[str]
    nextToken: NotRequired[str]

class ListMeshesInputTypeDef(TypedDict):
    limit: NotRequired[int]
    nextToken: NotRequired[str]

class MeshRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int

class ListRoutesInputTypeDef(TypedDict):
    meshName: str
    virtualRouterName: str
    limit: NotRequired[int]
    meshOwner: NotRequired[str]
    nextToken: NotRequired[str]

class RouteRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    routeName: str
    version: int
    virtualRouterName: str

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str
    limit: NotRequired[int]
    nextToken: NotRequired[str]

class ListVirtualGatewaysInputTypeDef(TypedDict):
    meshName: str
    limit: NotRequired[int]
    meshOwner: NotRequired[str]
    nextToken: NotRequired[str]

class VirtualGatewayRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualGatewayName: str

class ListVirtualNodesInputTypeDef(TypedDict):
    meshName: str
    limit: NotRequired[int]
    meshOwner: NotRequired[str]
    nextToken: NotRequired[str]

class VirtualNodeRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualNodeName: str

class ListVirtualRoutersInputTypeDef(TypedDict):
    meshName: str
    limit: NotRequired[int]
    meshOwner: NotRequired[str]
    nextToken: NotRequired[str]

class VirtualRouterRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualRouterName: str

class ListVirtualServicesInputTypeDef(TypedDict):
    meshName: str
    limit: NotRequired[int]
    meshOwner: NotRequired[str]
    nextToken: NotRequired[str]

class VirtualServiceRefTypeDef(TypedDict):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    meshName: str
    meshOwner: str
    resourceOwner: str
    version: int
    virtualServiceName: str

class PortMappingTypeDef(TypedDict):
    port: int
    protocol: PortProtocolType

class ListenerTlsAcmCertificateTypeDef(TypedDict):
    certificateArn: str

class TlsValidationContextFileTrustTypeDef(TypedDict):
    certificateChain: str

class TlsValidationContextSdsTrustTypeDef(TypedDict):
    secretName: str

class MeshStatusTypeDef(TypedDict):
    status: NotRequired[MeshStatusCodeType]

class MeshServiceDiscoveryTypeDef(TypedDict):
    ipPreference: NotRequired[IpPreferenceType]

class RouteStatusTypeDef(TypedDict):
    status: RouteStatusCodeType

class SubjectAlternativeNameMatchersOutputTypeDef(TypedDict):
    exact: List[str]

class SubjectAlternativeNameMatchersTypeDef(TypedDict):
    exact: Sequence[str]

class TcpRouteMatchTypeDef(TypedDict):
    port: NotRequired[int]

class TlsValidationContextAcmTrustOutputTypeDef(TypedDict):
    certificateAuthorityArns: List[str]

class TlsValidationContextAcmTrustTypeDef(TypedDict):
    certificateAuthorityArns: Sequence[str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class VirtualGatewayListenerTlsFileCertificateTypeDef(TypedDict):
    certificateChain: str
    privateKey: str

class VirtualGatewayListenerTlsSdsCertificateTypeDef(TypedDict):
    secretName: str

class VirtualGatewayGrpcConnectionPoolTypeDef(TypedDict):
    maxRequests: int

class VirtualGatewayHttp2ConnectionPoolTypeDef(TypedDict):
    maxRequests: int

class VirtualGatewayHttpConnectionPoolTypeDef(TypedDict):
    maxConnections: int
    maxPendingRequests: NotRequired[int]

class VirtualGatewayStatusTypeDef(TypedDict):
    status: VirtualGatewayStatusCodeType

class VirtualGatewayHealthCheckPolicyTypeDef(TypedDict):
    healthyThreshold: int
    intervalMillis: int
    protocol: VirtualGatewayPortProtocolType
    timeoutMillis: int
    unhealthyThreshold: int
    path: NotRequired[str]
    port: NotRequired[int]

class VirtualGatewayPortMappingTypeDef(TypedDict):
    port: int
    protocol: VirtualGatewayPortProtocolType

class VirtualGatewayListenerTlsAcmCertificateTypeDef(TypedDict):
    certificateArn: str

class VirtualGatewayTlsValidationContextFileTrustTypeDef(TypedDict):
    certificateChain: str

class VirtualGatewayTlsValidationContextSdsTrustTypeDef(TypedDict):
    secretName: str

class VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef(TypedDict):
    certificateAuthorityArns: List[str]

class VirtualGatewayTlsValidationContextAcmTrustTypeDef(TypedDict):
    certificateAuthorityArns: Sequence[str]

class VirtualNodeGrpcConnectionPoolTypeDef(TypedDict):
    maxRequests: int

class VirtualNodeHttp2ConnectionPoolTypeDef(TypedDict):
    maxRequests: int

class VirtualNodeHttpConnectionPoolTypeDef(TypedDict):
    maxConnections: int
    maxPendingRequests: NotRequired[int]

class VirtualNodeTcpConnectionPoolTypeDef(TypedDict):
    maxConnections: int

class VirtualNodeStatusTypeDef(TypedDict):
    status: VirtualNodeStatusCodeType

class VirtualNodeServiceProviderTypeDef(TypedDict):
    virtualNodeName: str

class VirtualRouterStatusTypeDef(TypedDict):
    status: VirtualRouterStatusCodeType

class VirtualRouterServiceProviderTypeDef(TypedDict):
    virtualRouterName: str

class VirtualServiceStatusTypeDef(TypedDict):
    status: VirtualServiceStatusCodeType

class AwsCloudMapServiceDiscoveryOutputTypeDef(TypedDict):
    namespaceName: str
    serviceName: str
    attributes: NotRequired[List[AwsCloudMapInstanceAttributeTypeDef]]
    ipPreference: NotRequired[IpPreferenceType]

class AwsCloudMapServiceDiscoveryTypeDef(TypedDict):
    namespaceName: str
    serviceName: str
    attributes: NotRequired[Sequence[AwsCloudMapInstanceAttributeTypeDef]]
    ipPreference: NotRequired[IpPreferenceType]

class ClientTlsCertificateTypeDef(TypedDict):
    file: NotRequired[ListenerTlsFileCertificateTypeDef]
    sds: NotRequired[ListenerTlsSdsCertificateTypeDef]

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagRefTypeDef]

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: List[TagRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GrpcRetryPolicyOutputTypeDef(TypedDict):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    grpcRetryEvents: NotRequired[List[GrpcRetryPolicyEventType]]
    httpRetryEvents: NotRequired[List[str]]
    tcpRetryEvents: NotRequired[List[Literal["connection-error"]]]

class GrpcRetryPolicyTypeDef(TypedDict):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    grpcRetryEvents: NotRequired[Sequence[GrpcRetryPolicyEventType]]
    httpRetryEvents: NotRequired[Sequence[str]]
    tcpRetryEvents: NotRequired[Sequence[Literal["connection-error"]]]

class GrpcTimeoutTypeDef(TypedDict):
    idle: NotRequired[DurationTypeDef]
    perRequest: NotRequired[DurationTypeDef]

class HttpRetryPolicyOutputTypeDef(TypedDict):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    httpRetryEvents: NotRequired[List[str]]
    tcpRetryEvents: NotRequired[List[Literal["connection-error"]]]

class HttpRetryPolicyTypeDef(TypedDict):
    maxRetries: int
    perRetryTimeout: DurationTypeDef
    httpRetryEvents: NotRequired[Sequence[str]]
    tcpRetryEvents: NotRequired[Sequence[Literal["connection-error"]]]

class HttpTimeoutTypeDef(TypedDict):
    idle: NotRequired[DurationTypeDef]
    perRequest: NotRequired[DurationTypeDef]

class OutlierDetectionTypeDef(TypedDict):
    baseEjectionDuration: DurationTypeDef
    interval: DurationTypeDef
    maxEjectionPercent: int
    maxServerErrors: int

class TcpTimeoutTypeDef(TypedDict):
    idle: NotRequired[DurationTypeDef]

class GrpcGatewayRouteRewriteTypeDef(TypedDict):
    hostname: NotRequired[GatewayRouteHostnameRewriteTypeDef]

class ListGatewayRoutesOutputTypeDef(TypedDict):
    gatewayRoutes: List[GatewayRouteRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GatewayRouteTargetTypeDef(TypedDict):
    virtualService: GatewayRouteVirtualServiceTypeDef
    port: NotRequired[int]

GrpcMetadataMatchMethodTypeDef = TypedDict(
    "GrpcMetadataMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired[MatchRangeTypeDef],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)
GrpcRouteMetadataMatchMethodTypeDef = TypedDict(
    "GrpcRouteMetadataMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired[MatchRangeTypeDef],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)
HeaderMatchMethodTypeDef = TypedDict(
    "HeaderMatchMethodTypeDef",
    {
        "exact": NotRequired[str],
        "prefix": NotRequired[str],
        "range": NotRequired[MatchRangeTypeDef],
        "regex": NotRequired[str],
        "suffix": NotRequired[str],
    },
)

class GrpcRouteActionOutputTypeDef(TypedDict):
    weightedTargets: List[WeightedTargetTypeDef]

class GrpcRouteActionTypeDef(TypedDict):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class HttpRouteActionOutputTypeDef(TypedDict):
    weightedTargets: List[WeightedTargetTypeDef]

class HttpRouteActionTypeDef(TypedDict):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class TcpRouteActionOutputTypeDef(TypedDict):
    weightedTargets: List[WeightedTargetTypeDef]

class TcpRouteActionTypeDef(TypedDict):
    weightedTargets: Sequence[WeightedTargetTypeDef]

class HttpGatewayRouteRewriteTypeDef(TypedDict):
    hostname: NotRequired[GatewayRouteHostnameRewriteTypeDef]
    path: NotRequired[HttpGatewayRoutePathRewriteTypeDef]
    prefix: NotRequired[HttpGatewayRoutePrefixRewriteTypeDef]

class HttpQueryParameterTypeDef(TypedDict):
    name: str
    match: NotRequired[QueryParameterMatchTypeDef]

class LoggingFormatOutputTypeDef(TypedDict):
    json: NotRequired[List[JsonFormatRefTypeDef]]
    text: NotRequired[str]

class LoggingFormatTypeDef(TypedDict):
    json: NotRequired[Sequence[JsonFormatRefTypeDef]]
    text: NotRequired[str]

class ListGatewayRoutesInputPaginateTypeDef(TypedDict):
    meshName: str
    virtualGatewayName: str
    meshOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMeshesInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRoutesInputPaginateTypeDef(TypedDict):
    meshName: str
    virtualRouterName: str
    meshOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceInputPaginateTypeDef(TypedDict):
    resourceArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVirtualGatewaysInputPaginateTypeDef(TypedDict):
    meshName: str
    meshOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVirtualNodesInputPaginateTypeDef(TypedDict):
    meshName: str
    meshOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVirtualRoutersInputPaginateTypeDef(TypedDict):
    meshName: str
    meshOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVirtualServicesInputPaginateTypeDef(TypedDict):
    meshName: str
    meshOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMeshesOutputTypeDef(TypedDict):
    meshes: List[MeshRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRoutesOutputTypeDef(TypedDict):
    routes: List[RouteRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListVirtualGatewaysOutputTypeDef(TypedDict):
    virtualGateways: List[VirtualGatewayRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListVirtualNodesOutputTypeDef(TypedDict):
    virtualNodes: List[VirtualNodeRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListVirtualRoutersOutputTypeDef(TypedDict):
    virtualRouters: List[VirtualRouterRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListVirtualServicesOutputTypeDef(TypedDict):
    virtualServices: List[VirtualServiceRefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class VirtualRouterListenerTypeDef(TypedDict):
    portMapping: PortMappingTypeDef

class ListenerTlsCertificateTypeDef(TypedDict):
    acm: NotRequired[ListenerTlsAcmCertificateTypeDef]
    file: NotRequired[ListenerTlsFileCertificateTypeDef]
    sds: NotRequired[ListenerTlsSdsCertificateTypeDef]

class ListenerTlsValidationContextTrustTypeDef(TypedDict):
    file: NotRequired[TlsValidationContextFileTrustTypeDef]
    sds: NotRequired[TlsValidationContextSdsTrustTypeDef]

class MeshSpecTypeDef(TypedDict):
    egressFilter: NotRequired[EgressFilterTypeDef]
    serviceDiscovery: NotRequired[MeshServiceDiscoveryTypeDef]

class SubjectAlternativeNamesOutputTypeDef(TypedDict):
    match: SubjectAlternativeNameMatchersOutputTypeDef

class SubjectAlternativeNamesTypeDef(TypedDict):
    match: SubjectAlternativeNameMatchersTypeDef

class TlsValidationContextTrustOutputTypeDef(TypedDict):
    acm: NotRequired[TlsValidationContextAcmTrustOutputTypeDef]
    file: NotRequired[TlsValidationContextFileTrustTypeDef]
    sds: NotRequired[TlsValidationContextSdsTrustTypeDef]

class TlsValidationContextTrustTypeDef(TypedDict):
    acm: NotRequired[TlsValidationContextAcmTrustTypeDef]
    file: NotRequired[TlsValidationContextFileTrustTypeDef]
    sds: NotRequired[TlsValidationContextSdsTrustTypeDef]

class VirtualGatewayClientTlsCertificateTypeDef(TypedDict):
    file: NotRequired[VirtualGatewayListenerTlsFileCertificateTypeDef]
    sds: NotRequired[VirtualGatewayListenerTlsSdsCertificateTypeDef]

class VirtualGatewayConnectionPoolTypeDef(TypedDict):
    grpc: NotRequired[VirtualGatewayGrpcConnectionPoolTypeDef]
    http: NotRequired[VirtualGatewayHttpConnectionPoolTypeDef]
    http2: NotRequired[VirtualGatewayHttp2ConnectionPoolTypeDef]

class VirtualGatewayListenerTlsCertificateTypeDef(TypedDict):
    acm: NotRequired[VirtualGatewayListenerTlsAcmCertificateTypeDef]
    file: NotRequired[VirtualGatewayListenerTlsFileCertificateTypeDef]
    sds: NotRequired[VirtualGatewayListenerTlsSdsCertificateTypeDef]

class VirtualGatewayListenerTlsValidationContextTrustTypeDef(TypedDict):
    file: NotRequired[VirtualGatewayTlsValidationContextFileTrustTypeDef]
    sds: NotRequired[VirtualGatewayTlsValidationContextSdsTrustTypeDef]

class VirtualGatewayTlsValidationContextTrustOutputTypeDef(TypedDict):
    acm: NotRequired[VirtualGatewayTlsValidationContextAcmTrustOutputTypeDef]
    file: NotRequired[VirtualGatewayTlsValidationContextFileTrustTypeDef]
    sds: NotRequired[VirtualGatewayTlsValidationContextSdsTrustTypeDef]

class VirtualGatewayTlsValidationContextTrustTypeDef(TypedDict):
    acm: NotRequired[VirtualGatewayTlsValidationContextAcmTrustTypeDef]
    file: NotRequired[VirtualGatewayTlsValidationContextFileTrustTypeDef]
    sds: NotRequired[VirtualGatewayTlsValidationContextSdsTrustTypeDef]

class VirtualNodeConnectionPoolTypeDef(TypedDict):
    grpc: NotRequired[VirtualNodeGrpcConnectionPoolTypeDef]
    http: NotRequired[VirtualNodeHttpConnectionPoolTypeDef]
    http2: NotRequired[VirtualNodeHttp2ConnectionPoolTypeDef]
    tcp: NotRequired[VirtualNodeTcpConnectionPoolTypeDef]

class VirtualServiceProviderTypeDef(TypedDict):
    virtualNode: NotRequired[VirtualNodeServiceProviderTypeDef]
    virtualRouter: NotRequired[VirtualRouterServiceProviderTypeDef]

class ServiceDiscoveryOutputTypeDef(TypedDict):
    awsCloudMap: NotRequired[AwsCloudMapServiceDiscoveryOutputTypeDef]
    dns: NotRequired[DnsServiceDiscoveryTypeDef]

class ServiceDiscoveryTypeDef(TypedDict):
    awsCloudMap: NotRequired[AwsCloudMapServiceDiscoveryTypeDef]
    dns: NotRequired[DnsServiceDiscoveryTypeDef]

class ListenerTimeoutTypeDef(TypedDict):
    grpc: NotRequired[GrpcTimeoutTypeDef]
    http: NotRequired[HttpTimeoutTypeDef]
    http2: NotRequired[HttpTimeoutTypeDef]
    tcp: NotRequired[TcpTimeoutTypeDef]

class GrpcGatewayRouteActionTypeDef(TypedDict):
    target: GatewayRouteTargetTypeDef
    rewrite: NotRequired[GrpcGatewayRouteRewriteTypeDef]

class GrpcGatewayRouteMetadataTypeDef(TypedDict):
    name: str
    invert: NotRequired[bool]
    match: NotRequired[GrpcMetadataMatchMethodTypeDef]

class GrpcRouteMetadataTypeDef(TypedDict):
    name: str
    invert: NotRequired[bool]
    match: NotRequired[GrpcRouteMetadataMatchMethodTypeDef]

class HttpGatewayRouteHeaderTypeDef(TypedDict):
    name: str
    invert: NotRequired[bool]
    match: NotRequired[HeaderMatchMethodTypeDef]

class HttpRouteHeaderTypeDef(TypedDict):
    name: str
    invert: NotRequired[bool]
    match: NotRequired[HeaderMatchMethodTypeDef]

class TcpRouteOutputTypeDef(TypedDict):
    action: TcpRouteActionOutputTypeDef
    match: NotRequired[TcpRouteMatchTypeDef]
    timeout: NotRequired[TcpTimeoutTypeDef]

class TcpRouteTypeDef(TypedDict):
    action: TcpRouteActionTypeDef
    match: NotRequired[TcpRouteMatchTypeDef]
    timeout: NotRequired[TcpTimeoutTypeDef]

class HttpGatewayRouteActionTypeDef(TypedDict):
    target: GatewayRouteTargetTypeDef
    rewrite: NotRequired[HttpGatewayRouteRewriteTypeDef]

FileAccessLogOutputTypeDef = TypedDict(
    "FileAccessLogOutputTypeDef",
    {
        "path": str,
        "format": NotRequired[LoggingFormatOutputTypeDef],
    },
)
VirtualGatewayFileAccessLogOutputTypeDef = TypedDict(
    "VirtualGatewayFileAccessLogOutputTypeDef",
    {
        "path": str,
        "format": NotRequired[LoggingFormatOutputTypeDef],
    },
)
FileAccessLogTypeDef = TypedDict(
    "FileAccessLogTypeDef",
    {
        "path": str,
        "format": NotRequired[LoggingFormatTypeDef],
    },
)
VirtualGatewayFileAccessLogTypeDef = TypedDict(
    "VirtualGatewayFileAccessLogTypeDef",
    {
        "path": str,
        "format": NotRequired[LoggingFormatTypeDef],
    },
)

class VirtualRouterSpecOutputTypeDef(TypedDict):
    listeners: NotRequired[List[VirtualRouterListenerTypeDef]]

class VirtualRouterSpecTypeDef(TypedDict):
    listeners: NotRequired[Sequence[VirtualRouterListenerTypeDef]]

class CreateMeshInputTypeDef(TypedDict):
    meshName: str
    clientToken: NotRequired[str]
    spec: NotRequired[MeshSpecTypeDef]
    tags: NotRequired[Sequence[TagRefTypeDef]]

class MeshDataTypeDef(TypedDict):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: MeshSpecTypeDef
    status: MeshStatusTypeDef

class UpdateMeshInputTypeDef(TypedDict):
    meshName: str
    clientToken: NotRequired[str]
    spec: NotRequired[MeshSpecTypeDef]

class ListenerTlsValidationContextOutputTypeDef(TypedDict):
    trust: ListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: NotRequired[SubjectAlternativeNamesOutputTypeDef]

class ListenerTlsValidationContextTypeDef(TypedDict):
    trust: ListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: NotRequired[SubjectAlternativeNamesTypeDef]

class TlsValidationContextOutputTypeDef(TypedDict):
    trust: TlsValidationContextTrustOutputTypeDef
    subjectAlternativeNames: NotRequired[SubjectAlternativeNamesOutputTypeDef]

class TlsValidationContextTypeDef(TypedDict):
    trust: TlsValidationContextTrustTypeDef
    subjectAlternativeNames: NotRequired[SubjectAlternativeNamesTypeDef]

class VirtualGatewayListenerTlsValidationContextOutputTypeDef(TypedDict):
    trust: VirtualGatewayListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: NotRequired[SubjectAlternativeNamesOutputTypeDef]

class VirtualGatewayListenerTlsValidationContextTypeDef(TypedDict):
    trust: VirtualGatewayListenerTlsValidationContextTrustTypeDef
    subjectAlternativeNames: NotRequired[SubjectAlternativeNamesTypeDef]

class VirtualGatewayTlsValidationContextOutputTypeDef(TypedDict):
    trust: VirtualGatewayTlsValidationContextTrustOutputTypeDef
    subjectAlternativeNames: NotRequired[SubjectAlternativeNamesOutputTypeDef]

class VirtualGatewayTlsValidationContextTypeDef(TypedDict):
    trust: VirtualGatewayTlsValidationContextTrustTypeDef
    subjectAlternativeNames: NotRequired[SubjectAlternativeNamesTypeDef]

class VirtualServiceSpecTypeDef(TypedDict):
    provider: NotRequired[VirtualServiceProviderTypeDef]

class GrpcGatewayRouteMatchOutputTypeDef(TypedDict):
    hostname: NotRequired[GatewayRouteHostnameMatchTypeDef]
    metadata: NotRequired[List[GrpcGatewayRouteMetadataTypeDef]]
    port: NotRequired[int]
    serviceName: NotRequired[str]

class GrpcGatewayRouteMatchTypeDef(TypedDict):
    hostname: NotRequired[GatewayRouteHostnameMatchTypeDef]
    metadata: NotRequired[Sequence[GrpcGatewayRouteMetadataTypeDef]]
    port: NotRequired[int]
    serviceName: NotRequired[str]

class GrpcRouteMatchOutputTypeDef(TypedDict):
    metadata: NotRequired[List[GrpcRouteMetadataTypeDef]]
    methodName: NotRequired[str]
    port: NotRequired[int]
    serviceName: NotRequired[str]

class GrpcRouteMatchTypeDef(TypedDict):
    metadata: NotRequired[Sequence[GrpcRouteMetadataTypeDef]]
    methodName: NotRequired[str]
    port: NotRequired[int]
    serviceName: NotRequired[str]

class HttpGatewayRouteMatchOutputTypeDef(TypedDict):
    headers: NotRequired[List[HttpGatewayRouteHeaderTypeDef]]
    hostname: NotRequired[GatewayRouteHostnameMatchTypeDef]
    method: NotRequired[HttpMethodType]
    path: NotRequired[HttpPathMatchTypeDef]
    port: NotRequired[int]
    prefix: NotRequired[str]
    queryParameters: NotRequired[List[HttpQueryParameterTypeDef]]

class HttpGatewayRouteMatchTypeDef(TypedDict):
    headers: NotRequired[Sequence[HttpGatewayRouteHeaderTypeDef]]
    hostname: NotRequired[GatewayRouteHostnameMatchTypeDef]
    method: NotRequired[HttpMethodType]
    path: NotRequired[HttpPathMatchTypeDef]
    port: NotRequired[int]
    prefix: NotRequired[str]
    queryParameters: NotRequired[Sequence[HttpQueryParameterTypeDef]]

class HttpRouteMatchOutputTypeDef(TypedDict):
    headers: NotRequired[List[HttpRouteHeaderTypeDef]]
    method: NotRequired[HttpMethodType]
    path: NotRequired[HttpPathMatchTypeDef]
    port: NotRequired[int]
    prefix: NotRequired[str]
    queryParameters: NotRequired[List[HttpQueryParameterTypeDef]]
    scheme: NotRequired[HttpSchemeType]

class HttpRouteMatchTypeDef(TypedDict):
    headers: NotRequired[Sequence[HttpRouteHeaderTypeDef]]
    method: NotRequired[HttpMethodType]
    path: NotRequired[HttpPathMatchTypeDef]
    port: NotRequired[int]
    prefix: NotRequired[str]
    queryParameters: NotRequired[Sequence[HttpQueryParameterTypeDef]]
    scheme: NotRequired[HttpSchemeType]

class AccessLogOutputTypeDef(TypedDict):
    file: NotRequired[FileAccessLogOutputTypeDef]

class VirtualGatewayAccessLogOutputTypeDef(TypedDict):
    file: NotRequired[VirtualGatewayFileAccessLogOutputTypeDef]

class AccessLogTypeDef(TypedDict):
    file: NotRequired[FileAccessLogTypeDef]

class VirtualGatewayAccessLogTypeDef(TypedDict):
    file: NotRequired[VirtualGatewayFileAccessLogTypeDef]

class VirtualRouterDataTypeDef(TypedDict):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualRouterSpecOutputTypeDef
    status: VirtualRouterStatusTypeDef
    virtualRouterName: str

VirtualRouterSpecUnionTypeDef = Union[VirtualRouterSpecTypeDef, VirtualRouterSpecOutputTypeDef]

class CreateMeshOutputTypeDef(TypedDict):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMeshOutputTypeDef(TypedDict):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMeshOutputTypeDef(TypedDict):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMeshOutputTypeDef(TypedDict):
    mesh: MeshDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListenerTlsOutputTypeDef(TypedDict):
    certificate: ListenerTlsCertificateTypeDef
    mode: ListenerTlsModeType
    validation: NotRequired[ListenerTlsValidationContextOutputTypeDef]

class ListenerTlsTypeDef(TypedDict):
    certificate: ListenerTlsCertificateTypeDef
    mode: ListenerTlsModeType
    validation: NotRequired[ListenerTlsValidationContextTypeDef]

class ClientPolicyTlsOutputTypeDef(TypedDict):
    validation: TlsValidationContextOutputTypeDef
    certificate: NotRequired[ClientTlsCertificateTypeDef]
    enforce: NotRequired[bool]
    ports: NotRequired[List[int]]

class ClientPolicyTlsTypeDef(TypedDict):
    validation: TlsValidationContextTypeDef
    certificate: NotRequired[ClientTlsCertificateTypeDef]
    enforce: NotRequired[bool]
    ports: NotRequired[Sequence[int]]

class VirtualGatewayListenerTlsOutputTypeDef(TypedDict):
    certificate: VirtualGatewayListenerTlsCertificateTypeDef
    mode: VirtualGatewayListenerTlsModeType
    validation: NotRequired[VirtualGatewayListenerTlsValidationContextOutputTypeDef]

class VirtualGatewayListenerTlsTypeDef(TypedDict):
    certificate: VirtualGatewayListenerTlsCertificateTypeDef
    mode: VirtualGatewayListenerTlsModeType
    validation: NotRequired[VirtualGatewayListenerTlsValidationContextTypeDef]

class VirtualGatewayClientPolicyTlsOutputTypeDef(TypedDict):
    validation: VirtualGatewayTlsValidationContextOutputTypeDef
    certificate: NotRequired[VirtualGatewayClientTlsCertificateTypeDef]
    enforce: NotRequired[bool]
    ports: NotRequired[List[int]]

class VirtualGatewayClientPolicyTlsTypeDef(TypedDict):
    validation: VirtualGatewayTlsValidationContextTypeDef
    certificate: NotRequired[VirtualGatewayClientTlsCertificateTypeDef]
    enforce: NotRequired[bool]
    ports: NotRequired[Sequence[int]]

class CreateVirtualServiceInputTypeDef(TypedDict):
    meshName: str
    spec: VirtualServiceSpecTypeDef
    virtualServiceName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]
    tags: NotRequired[Sequence[TagRefTypeDef]]

class UpdateVirtualServiceInputTypeDef(TypedDict):
    meshName: str
    spec: VirtualServiceSpecTypeDef
    virtualServiceName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]

class VirtualServiceDataTypeDef(TypedDict):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualServiceSpecTypeDef
    status: VirtualServiceStatusTypeDef
    virtualServiceName: str

class GrpcGatewayRouteOutputTypeDef(TypedDict):
    action: GrpcGatewayRouteActionTypeDef
    match: GrpcGatewayRouteMatchOutputTypeDef

class GrpcGatewayRouteTypeDef(TypedDict):
    action: GrpcGatewayRouteActionTypeDef
    match: GrpcGatewayRouteMatchTypeDef

class GrpcRouteOutputTypeDef(TypedDict):
    action: GrpcRouteActionOutputTypeDef
    match: GrpcRouteMatchOutputTypeDef
    retryPolicy: NotRequired[GrpcRetryPolicyOutputTypeDef]
    timeout: NotRequired[GrpcTimeoutTypeDef]

class GrpcRouteTypeDef(TypedDict):
    action: GrpcRouteActionTypeDef
    match: GrpcRouteMatchTypeDef
    retryPolicy: NotRequired[GrpcRetryPolicyTypeDef]
    timeout: NotRequired[GrpcTimeoutTypeDef]

class HttpGatewayRouteOutputTypeDef(TypedDict):
    action: HttpGatewayRouteActionTypeDef
    match: HttpGatewayRouteMatchOutputTypeDef

class HttpGatewayRouteTypeDef(TypedDict):
    action: HttpGatewayRouteActionTypeDef
    match: HttpGatewayRouteMatchTypeDef

class HttpRouteOutputTypeDef(TypedDict):
    action: HttpRouteActionOutputTypeDef
    match: HttpRouteMatchOutputTypeDef
    retryPolicy: NotRequired[HttpRetryPolicyOutputTypeDef]
    timeout: NotRequired[HttpTimeoutTypeDef]

class HttpRouteTypeDef(TypedDict):
    action: HttpRouteActionTypeDef
    match: HttpRouteMatchTypeDef
    retryPolicy: NotRequired[HttpRetryPolicyTypeDef]
    timeout: NotRequired[HttpTimeoutTypeDef]

class LoggingOutputTypeDef(TypedDict):
    accessLog: NotRequired[AccessLogOutputTypeDef]

class VirtualGatewayLoggingOutputTypeDef(TypedDict):
    accessLog: NotRequired[VirtualGatewayAccessLogOutputTypeDef]

class LoggingTypeDef(TypedDict):
    accessLog: NotRequired[AccessLogTypeDef]

class VirtualGatewayLoggingTypeDef(TypedDict):
    accessLog: NotRequired[VirtualGatewayAccessLogTypeDef]

class CreateVirtualRouterOutputTypeDef(TypedDict):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualRouterOutputTypeDef(TypedDict):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualRouterOutputTypeDef(TypedDict):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualRouterOutputTypeDef(TypedDict):
    virtualRouter: VirtualRouterDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualRouterInputTypeDef(TypedDict):
    meshName: str
    spec: VirtualRouterSpecUnionTypeDef
    virtualRouterName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]
    tags: NotRequired[Sequence[TagRefTypeDef]]

class UpdateVirtualRouterInputTypeDef(TypedDict):
    meshName: str
    spec: VirtualRouterSpecUnionTypeDef
    virtualRouterName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]

class ListenerOutputTypeDef(TypedDict):
    portMapping: PortMappingTypeDef
    connectionPool: NotRequired[VirtualNodeConnectionPoolTypeDef]
    healthCheck: NotRequired[HealthCheckPolicyTypeDef]
    outlierDetection: NotRequired[OutlierDetectionTypeDef]
    timeout: NotRequired[ListenerTimeoutTypeDef]
    tls: NotRequired[ListenerTlsOutputTypeDef]

class ListenerTypeDef(TypedDict):
    portMapping: PortMappingTypeDef
    connectionPool: NotRequired[VirtualNodeConnectionPoolTypeDef]
    healthCheck: NotRequired[HealthCheckPolicyTypeDef]
    outlierDetection: NotRequired[OutlierDetectionTypeDef]
    timeout: NotRequired[ListenerTimeoutTypeDef]
    tls: NotRequired[ListenerTlsTypeDef]

class ClientPolicyOutputTypeDef(TypedDict):
    tls: NotRequired[ClientPolicyTlsOutputTypeDef]

class ClientPolicyTypeDef(TypedDict):
    tls: NotRequired[ClientPolicyTlsTypeDef]

class VirtualGatewayListenerOutputTypeDef(TypedDict):
    portMapping: VirtualGatewayPortMappingTypeDef
    connectionPool: NotRequired[VirtualGatewayConnectionPoolTypeDef]
    healthCheck: NotRequired[VirtualGatewayHealthCheckPolicyTypeDef]
    tls: NotRequired[VirtualGatewayListenerTlsOutputTypeDef]

class VirtualGatewayListenerTypeDef(TypedDict):
    portMapping: VirtualGatewayPortMappingTypeDef
    connectionPool: NotRequired[VirtualGatewayConnectionPoolTypeDef]
    healthCheck: NotRequired[VirtualGatewayHealthCheckPolicyTypeDef]
    tls: NotRequired[VirtualGatewayListenerTlsTypeDef]

class VirtualGatewayClientPolicyOutputTypeDef(TypedDict):
    tls: NotRequired[VirtualGatewayClientPolicyTlsOutputTypeDef]

class VirtualGatewayClientPolicyTypeDef(TypedDict):
    tls: NotRequired[VirtualGatewayClientPolicyTlsTypeDef]

class CreateVirtualServiceOutputTypeDef(TypedDict):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualServiceOutputTypeDef(TypedDict):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualServiceOutputTypeDef(TypedDict):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualServiceOutputTypeDef(TypedDict):
    virtualService: VirtualServiceDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GatewayRouteSpecOutputTypeDef(TypedDict):
    grpcRoute: NotRequired[GrpcGatewayRouteOutputTypeDef]
    http2Route: NotRequired[HttpGatewayRouteOutputTypeDef]
    httpRoute: NotRequired[HttpGatewayRouteOutputTypeDef]
    priority: NotRequired[int]

class GatewayRouteSpecTypeDef(TypedDict):
    grpcRoute: NotRequired[GrpcGatewayRouteTypeDef]
    http2Route: NotRequired[HttpGatewayRouteTypeDef]
    httpRoute: NotRequired[HttpGatewayRouteTypeDef]
    priority: NotRequired[int]

class RouteSpecOutputTypeDef(TypedDict):
    grpcRoute: NotRequired[GrpcRouteOutputTypeDef]
    http2Route: NotRequired[HttpRouteOutputTypeDef]
    httpRoute: NotRequired[HttpRouteOutputTypeDef]
    priority: NotRequired[int]
    tcpRoute: NotRequired[TcpRouteOutputTypeDef]

class RouteSpecTypeDef(TypedDict):
    grpcRoute: NotRequired[GrpcRouteTypeDef]
    http2Route: NotRequired[HttpRouteTypeDef]
    httpRoute: NotRequired[HttpRouteTypeDef]
    priority: NotRequired[int]
    tcpRoute: NotRequired[TcpRouteTypeDef]

class BackendDefaultsOutputTypeDef(TypedDict):
    clientPolicy: NotRequired[ClientPolicyOutputTypeDef]

class VirtualServiceBackendOutputTypeDef(TypedDict):
    virtualServiceName: str
    clientPolicy: NotRequired[ClientPolicyOutputTypeDef]

class BackendDefaultsTypeDef(TypedDict):
    clientPolicy: NotRequired[ClientPolicyTypeDef]

class VirtualServiceBackendTypeDef(TypedDict):
    virtualServiceName: str
    clientPolicy: NotRequired[ClientPolicyTypeDef]

class VirtualGatewayBackendDefaultsOutputTypeDef(TypedDict):
    clientPolicy: NotRequired[VirtualGatewayClientPolicyOutputTypeDef]

class VirtualGatewayBackendDefaultsTypeDef(TypedDict):
    clientPolicy: NotRequired[VirtualGatewayClientPolicyTypeDef]

class GatewayRouteDataTypeDef(TypedDict):
    gatewayRouteName: str
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: GatewayRouteSpecOutputTypeDef
    status: GatewayRouteStatusTypeDef
    virtualGatewayName: str

GatewayRouteSpecUnionTypeDef = Union[GatewayRouteSpecTypeDef, GatewayRouteSpecOutputTypeDef]

class RouteDataTypeDef(TypedDict):
    meshName: str
    metadata: ResourceMetadataTypeDef
    routeName: str
    spec: RouteSpecOutputTypeDef
    status: RouteStatusTypeDef
    virtualRouterName: str

RouteSpecUnionTypeDef = Union[RouteSpecTypeDef, RouteSpecOutputTypeDef]

class BackendOutputTypeDef(TypedDict):
    virtualService: NotRequired[VirtualServiceBackendOutputTypeDef]

class BackendTypeDef(TypedDict):
    virtualService: NotRequired[VirtualServiceBackendTypeDef]

class VirtualGatewaySpecOutputTypeDef(TypedDict):
    listeners: List[VirtualGatewayListenerOutputTypeDef]
    backendDefaults: NotRequired[VirtualGatewayBackendDefaultsOutputTypeDef]
    logging: NotRequired[VirtualGatewayLoggingOutputTypeDef]

class VirtualGatewaySpecTypeDef(TypedDict):
    listeners: Sequence[VirtualGatewayListenerTypeDef]
    backendDefaults: NotRequired[VirtualGatewayBackendDefaultsTypeDef]
    logging: NotRequired[VirtualGatewayLoggingTypeDef]

class CreateGatewayRouteOutputTypeDef(TypedDict):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayRouteOutputTypeDef(TypedDict):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGatewayRouteOutputTypeDef(TypedDict):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayRouteOutputTypeDef(TypedDict):
    gatewayRoute: GatewayRouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGatewayRouteInputTypeDef(TypedDict):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecUnionTypeDef
    virtualGatewayName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]
    tags: NotRequired[Sequence[TagRefTypeDef]]

class UpdateGatewayRouteInputTypeDef(TypedDict):
    gatewayRouteName: str
    meshName: str
    spec: GatewayRouteSpecUnionTypeDef
    virtualGatewayName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]

class CreateRouteOutputTypeDef(TypedDict):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRouteOutputTypeDef(TypedDict):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRouteOutputTypeDef(TypedDict):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRouteOutputTypeDef(TypedDict):
    route: RouteDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteInputTypeDef(TypedDict):
    meshName: str
    routeName: str
    spec: RouteSpecUnionTypeDef
    virtualRouterName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]
    tags: NotRequired[Sequence[TagRefTypeDef]]

class UpdateRouteInputTypeDef(TypedDict):
    meshName: str
    routeName: str
    spec: RouteSpecUnionTypeDef
    virtualRouterName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]

class VirtualNodeSpecOutputTypeDef(TypedDict):
    backendDefaults: NotRequired[BackendDefaultsOutputTypeDef]
    backends: NotRequired[List[BackendOutputTypeDef]]
    listeners: NotRequired[List[ListenerOutputTypeDef]]
    logging: NotRequired[LoggingOutputTypeDef]
    serviceDiscovery: NotRequired[ServiceDiscoveryOutputTypeDef]

class VirtualNodeSpecTypeDef(TypedDict):
    backendDefaults: NotRequired[BackendDefaultsTypeDef]
    backends: NotRequired[Sequence[BackendTypeDef]]
    listeners: NotRequired[Sequence[ListenerTypeDef]]
    logging: NotRequired[LoggingTypeDef]
    serviceDiscovery: NotRequired[ServiceDiscoveryTypeDef]

class VirtualGatewayDataTypeDef(TypedDict):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualGatewaySpecOutputTypeDef
    status: VirtualGatewayStatusTypeDef
    virtualGatewayName: str

VirtualGatewaySpecUnionTypeDef = Union[VirtualGatewaySpecTypeDef, VirtualGatewaySpecOutputTypeDef]

class VirtualNodeDataTypeDef(TypedDict):
    meshName: str
    metadata: ResourceMetadataTypeDef
    spec: VirtualNodeSpecOutputTypeDef
    status: VirtualNodeStatusTypeDef
    virtualNodeName: str

VirtualNodeSpecUnionTypeDef = Union[VirtualNodeSpecTypeDef, VirtualNodeSpecOutputTypeDef]

class CreateVirtualGatewayOutputTypeDef(TypedDict):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualGatewayOutputTypeDef(TypedDict):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualGatewayOutputTypeDef(TypedDict):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualGatewayOutputTypeDef(TypedDict):
    virtualGateway: VirtualGatewayDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualGatewayInputTypeDef(TypedDict):
    meshName: str
    spec: VirtualGatewaySpecUnionTypeDef
    virtualGatewayName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]
    tags: NotRequired[Sequence[TagRefTypeDef]]

class UpdateVirtualGatewayInputTypeDef(TypedDict):
    meshName: str
    spec: VirtualGatewaySpecUnionTypeDef
    virtualGatewayName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]

class CreateVirtualNodeOutputTypeDef(TypedDict):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualNodeOutputTypeDef(TypedDict):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVirtualNodeOutputTypeDef(TypedDict):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVirtualNodeOutputTypeDef(TypedDict):
    virtualNode: VirtualNodeDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVirtualNodeInputTypeDef(TypedDict):
    meshName: str
    spec: VirtualNodeSpecUnionTypeDef
    virtualNodeName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]
    tags: NotRequired[Sequence[TagRefTypeDef]]

class UpdateVirtualNodeInputTypeDef(TypedDict):
    meshName: str
    spec: VirtualNodeSpecUnionTypeDef
    virtualNodeName: str
    clientToken: NotRequired[str]
    meshOwner: NotRequired[str]
