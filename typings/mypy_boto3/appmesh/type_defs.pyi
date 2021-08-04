"""
Type annotations for appmesh service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appmesh/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appmesh.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    DefaultGatewayRouteRewriteType,
    DnsResponseTypeType,
    DurationUnitType,
    EgressFilterTypeType,
    GatewayRouteStatusCodeType,
    GrpcRetryPolicyEventType,
    HttpMethodType,
    HttpSchemeType,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessLogTypeDef",
    "AwsCloudMapInstanceAttributeTypeDef",
    "AwsCloudMapServiceDiscoveryTypeDef",
    "BackendDefaultsTypeDef",
    "BackendTypeDef",
    "ClientPolicyTlsTypeDef",
    "ClientPolicyTypeDef",
    "ClientTlsCertificateTypeDef",
    "CreateGatewayRouteInputRequestTypeDef",
    "CreateGatewayRouteOutputTypeDef",
    "CreateMeshInputRequestTypeDef",
    "CreateMeshOutputTypeDef",
    "CreateRouteInputRequestTypeDef",
    "CreateRouteOutputTypeDef",
    "CreateVirtualGatewayInputRequestTypeDef",
    "CreateVirtualGatewayOutputTypeDef",
    "CreateVirtualNodeInputRequestTypeDef",
    "CreateVirtualNodeOutputTypeDef",
    "CreateVirtualRouterInputRequestTypeDef",
    "CreateVirtualRouterOutputTypeDef",
    "CreateVirtualServiceInputRequestTypeDef",
    "CreateVirtualServiceOutputTypeDef",
    "DeleteGatewayRouteInputRequestTypeDef",
    "DeleteGatewayRouteOutputTypeDef",
    "DeleteMeshInputRequestTypeDef",
    "DeleteMeshOutputTypeDef",
    "DeleteRouteInputRequestTypeDef",
    "DeleteRouteOutputTypeDef",
    "DeleteVirtualGatewayInputRequestTypeDef",
    "DeleteVirtualGatewayOutputTypeDef",
    "DeleteVirtualNodeInputRequestTypeDef",
    "DeleteVirtualNodeOutputTypeDef",
    "DeleteVirtualRouterInputRequestTypeDef",
    "DeleteVirtualRouterOutputTypeDef",
    "DeleteVirtualServiceInputRequestTypeDef",
    "DeleteVirtualServiceOutputTypeDef",
    "DescribeGatewayRouteInputRequestTypeDef",
    "DescribeGatewayRouteOutputTypeDef",
    "DescribeMeshInputRequestTypeDef",
    "DescribeMeshOutputTypeDef",
    "DescribeRouteInputRequestTypeDef",
    "DescribeRouteOutputTypeDef",
    "DescribeVirtualGatewayInputRequestTypeDef",
    "DescribeVirtualGatewayOutputTypeDef",
    "DescribeVirtualNodeInputRequestTypeDef",
    "DescribeVirtualNodeOutputTypeDef",
    "DescribeVirtualRouterInputRequestTypeDef",
    "DescribeVirtualRouterOutputTypeDef",
    "DescribeVirtualServiceInputRequestTypeDef",
    "DescribeVirtualServiceOutputTypeDef",
    "DnsServiceDiscoveryTypeDef",
    "DurationTypeDef",
    "EgressFilterTypeDef",
    "FileAccessLogTypeDef",
    "GatewayRouteDataTypeDef",
    "GatewayRouteHostnameMatchTypeDef",
    "GatewayRouteHostnameRewriteTypeDef",
    "GatewayRouteRefTypeDef",
    "GatewayRouteSpecTypeDef",
    "GatewayRouteStatusTypeDef",
    "GatewayRouteTargetTypeDef",
    "GatewayRouteVirtualServiceTypeDef",
    "GrpcGatewayRouteActionTypeDef",
    "GrpcGatewayRouteMatchTypeDef",
    "GrpcGatewayRouteMetadataTypeDef",
    "GrpcGatewayRouteRewriteTypeDef",
    "GrpcGatewayRouteTypeDef",
    "GrpcMetadataMatchMethodTypeDef",
    "GrpcRetryPolicyTypeDef",
    "GrpcRouteActionTypeDef",
    "GrpcRouteMatchTypeDef",
    "GrpcRouteMetadataMatchMethodTypeDef",
    "GrpcRouteMetadataTypeDef",
    "GrpcRouteTypeDef",
    "GrpcTimeoutTypeDef",
    "HeaderMatchMethodTypeDef",
    "HealthCheckPolicyTypeDef",
    "HttpGatewayRouteActionTypeDef",
    "HttpGatewayRouteHeaderTypeDef",
    "HttpGatewayRouteMatchTypeDef",
    "HttpGatewayRoutePathRewriteTypeDef",
    "HttpGatewayRoutePrefixRewriteTypeDef",
    "HttpGatewayRouteRewriteTypeDef",
    "HttpGatewayRouteTypeDef",
    "HttpPathMatchTypeDef",
    "HttpQueryParameterTypeDef",
    "HttpRetryPolicyTypeDef",
    "HttpRouteActionTypeDef",
    "HttpRouteHeaderTypeDef",
    "HttpRouteMatchTypeDef",
    "HttpRouteTypeDef",
    "HttpTimeoutTypeDef",
    "ListGatewayRoutesInputRequestTypeDef",
    "ListGatewayRoutesOutputTypeDef",
    "ListMeshesInputRequestTypeDef",
    "ListMeshesOutputTypeDef",
    "ListRoutesInputRequestTypeDef",
    "ListRoutesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVirtualGatewaysInputRequestTypeDef",
    "ListVirtualGatewaysOutputTypeDef",
    "ListVirtualNodesInputRequestTypeDef",
    "ListVirtualNodesOutputTypeDef",
    "ListVirtualRoutersInputRequestTypeDef",
    "ListVirtualRoutersOutputTypeDef",
    "ListVirtualServicesInputRequestTypeDef",
    "ListVirtualServicesOutputTypeDef",
    "ListenerTimeoutTypeDef",
    "ListenerTlsAcmCertificateTypeDef",
    "ListenerTlsCertificateTypeDef",
    "ListenerTlsFileCertificateTypeDef",
    "ListenerTlsSdsCertificateTypeDef",
    "ListenerTlsTypeDef",
    "ListenerTlsValidationContextTrustTypeDef",
    "ListenerTlsValidationContextTypeDef",
    "ListenerTypeDef",
    "LoggingTypeDef",
    "MatchRangeTypeDef",
    "MeshDataTypeDef",
    "MeshRefTypeDef",
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
    "RouteSpecTypeDef",
    "RouteStatusTypeDef",
    "ServiceDiscoveryTypeDef",
    "SubjectAlternativeNameMatchersTypeDef",
    "SubjectAlternativeNamesTypeDef",
    "TagRefTypeDef",
    "TagResourceInputRequestTypeDef",
    "TcpRouteActionTypeDef",
    "TcpRouteTypeDef",
    "TcpTimeoutTypeDef",
    "TlsValidationContextAcmTrustTypeDef",
    "TlsValidationContextFileTrustTypeDef",
    "TlsValidationContextSdsTrustTypeDef",
    "TlsValidationContextTrustTypeDef",
    "TlsValidationContextTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateGatewayRouteInputRequestTypeDef",
    "UpdateGatewayRouteOutputTypeDef",
    "UpdateMeshInputRequestTypeDef",
    "UpdateMeshOutputTypeDef",
    "UpdateRouteInputRequestTypeDef",
    "UpdateRouteOutputTypeDef",
    "UpdateVirtualGatewayInputRequestTypeDef",
    "UpdateVirtualGatewayOutputTypeDef",
    "UpdateVirtualNodeInputRequestTypeDef",
    "UpdateVirtualNodeOutputTypeDef",
    "UpdateVirtualRouterInputRequestTypeDef",
    "UpdateVirtualRouterOutputTypeDef",
    "UpdateVirtualServiceInputRequestTypeDef",
    "UpdateVirtualServiceOutputTypeDef",
    "VirtualGatewayAccessLogTypeDef",
    "VirtualGatewayBackendDefaultsTypeDef",
    "VirtualGatewayClientPolicyTlsTypeDef",
    "VirtualGatewayClientPolicyTypeDef",
    "VirtualGatewayClientTlsCertificateTypeDef",
    "VirtualGatewayConnectionPoolTypeDef",
    "VirtualGatewayDataTypeDef",
    "VirtualGatewayFileAccessLogTypeDef",
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    "VirtualGatewayHealthCheckPolicyTypeDef",
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    "VirtualGatewayHttpConnectionPoolTypeDef",
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    "VirtualGatewayListenerTlsCertificateTypeDef",
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    "VirtualGatewayListenerTlsTypeDef",
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    "VirtualGatewayListenerTlsValidationContextTypeDef",
    "VirtualGatewayListenerTypeDef",
    "VirtualGatewayLoggingTypeDef",
    "VirtualGatewayPortMappingTypeDef",
    "VirtualGatewayRefTypeDef",
    "VirtualGatewaySpecTypeDef",
    "VirtualGatewayStatusTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    "VirtualGatewayTlsValidationContextTypeDef",
    "VirtualNodeConnectionPoolTypeDef",
    "VirtualNodeDataTypeDef",
    "VirtualNodeGrpcConnectionPoolTypeDef",
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    "VirtualNodeHttpConnectionPoolTypeDef",
    "VirtualNodeRefTypeDef",
    "VirtualNodeServiceProviderTypeDef",
    "VirtualNodeSpecTypeDef",
    "VirtualNodeStatusTypeDef",
    "VirtualNodeTcpConnectionPoolTypeDef",
    "VirtualRouterDataTypeDef",
    "VirtualRouterListenerTypeDef",
    "VirtualRouterRefTypeDef",
    "VirtualRouterServiceProviderTypeDef",
    "VirtualRouterSpecTypeDef",
    "VirtualRouterStatusTypeDef",
    "VirtualServiceBackendTypeDef",
    "VirtualServiceDataTypeDef",
    "VirtualServiceProviderTypeDef",
    "VirtualServiceRefTypeDef",
    "VirtualServiceSpecTypeDef",
    "VirtualServiceStatusTypeDef",
    "WeightedTargetTypeDef",
)

AccessLogTypeDef = TypedDict(
    "AccessLogTypeDef",
    {
        "file": "FileAccessLogTypeDef",
    },
    total=False,
)

AwsCloudMapInstanceAttributeTypeDef = TypedDict(
    "AwsCloudMapInstanceAttributeTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredAwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "_RequiredAwsCloudMapServiceDiscoveryTypeDef",
    {
        "namespaceName": str,
        "serviceName": str,
    },
)
_OptionalAwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "_OptionalAwsCloudMapServiceDiscoveryTypeDef",
    {
        "attributes": List["AwsCloudMapInstanceAttributeTypeDef"],
    },
    total=False,
)

class AwsCloudMapServiceDiscoveryTypeDef(
    _RequiredAwsCloudMapServiceDiscoveryTypeDef, _OptionalAwsCloudMapServiceDiscoveryTypeDef
):
    pass

BackendDefaultsTypeDef = TypedDict(
    "BackendDefaultsTypeDef",
    {
        "clientPolicy": "ClientPolicyTypeDef",
    },
    total=False,
)

BackendTypeDef = TypedDict(
    "BackendTypeDef",
    {
        "virtualService": "VirtualServiceBackendTypeDef",
    },
    total=False,
)

_RequiredClientPolicyTlsTypeDef = TypedDict(
    "_RequiredClientPolicyTlsTypeDef",
    {
        "validation": "TlsValidationContextTypeDef",
    },
)
_OptionalClientPolicyTlsTypeDef = TypedDict(
    "_OptionalClientPolicyTlsTypeDef",
    {
        "certificate": "ClientTlsCertificateTypeDef",
        "enforce": bool,
        "ports": List[int],
    },
    total=False,
)

class ClientPolicyTlsTypeDef(_RequiredClientPolicyTlsTypeDef, _OptionalClientPolicyTlsTypeDef):
    pass

ClientPolicyTypeDef = TypedDict(
    "ClientPolicyTypeDef",
    {
        "tls": "ClientPolicyTlsTypeDef",
    },
    total=False,
)

ClientTlsCertificateTypeDef = TypedDict(
    "ClientTlsCertificateTypeDef",
    {
        "file": "ListenerTlsFileCertificateTypeDef",
        "sds": "ListenerTlsSdsCertificateTypeDef",
    },
    total=False,
)

_RequiredCreateGatewayRouteInputRequestTypeDef = TypedDict(
    "_RequiredCreateGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": "GatewayRouteSpecTypeDef",
        "virtualGatewayName": str,
    },
)
_OptionalCreateGatewayRouteInputRequestTypeDef = TypedDict(
    "_OptionalCreateGatewayRouteInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)

class CreateGatewayRouteInputRequestTypeDef(
    _RequiredCreateGatewayRouteInputRequestTypeDef, _OptionalCreateGatewayRouteInputRequestTypeDef
):
    pass

CreateGatewayRouteOutputTypeDef = TypedDict(
    "CreateGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMeshInputRequestTypeDef = TypedDict(
    "_RequiredCreateMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalCreateMeshInputRequestTypeDef = TypedDict(
    "_OptionalCreateMeshInputRequestTypeDef",
    {
        "clientToken": str,
        "spec": "MeshSpecTypeDef",
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)

class CreateMeshInputRequestTypeDef(
    _RequiredCreateMeshInputRequestTypeDef, _OptionalCreateMeshInputRequestTypeDef
):
    pass

CreateMeshOutputTypeDef = TypedDict(
    "CreateMeshOutputTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteInputRequestTypeDef = TypedDict(
    "_RequiredCreateRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "virtualRouterName": str,
    },
)
_OptionalCreateRouteInputRequestTypeDef = TypedDict(
    "_OptionalCreateRouteInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)

class CreateRouteInputRequestTypeDef(
    _RequiredCreateRouteInputRequestTypeDef, _OptionalCreateRouteInputRequestTypeDef
):
    pass

CreateRouteOutputTypeDef = TypedDict(
    "CreateRouteOutputTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualGatewayInputRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualGatewaySpecTypeDef",
        "virtualGatewayName": str,
    },
)
_OptionalCreateVirtualGatewayInputRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualGatewayInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)

class CreateVirtualGatewayInputRequestTypeDef(
    _RequiredCreateVirtualGatewayInputRequestTypeDef,
    _OptionalCreateVirtualGatewayInputRequestTypeDef,
):
    pass

CreateVirtualGatewayOutputTypeDef = TypedDict(
    "CreateVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualNodeInputRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualNodeSpecTypeDef",
        "virtualNodeName": str,
    },
)
_OptionalCreateVirtualNodeInputRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualNodeInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)

class CreateVirtualNodeInputRequestTypeDef(
    _RequiredCreateVirtualNodeInputRequestTypeDef, _OptionalCreateVirtualNodeInputRequestTypeDef
):
    pass

CreateVirtualNodeOutputTypeDef = TypedDict(
    "CreateVirtualNodeOutputTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualRouterInputRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualRouterSpecTypeDef",
        "virtualRouterName": str,
    },
)
_OptionalCreateVirtualRouterInputRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualRouterInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)

class CreateVirtualRouterInputRequestTypeDef(
    _RequiredCreateVirtualRouterInputRequestTypeDef, _OptionalCreateVirtualRouterInputRequestTypeDef
):
    pass

CreateVirtualRouterOutputTypeDef = TypedDict(
    "CreateVirtualRouterOutputTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVirtualServiceInputRequestTypeDef = TypedDict(
    "_RequiredCreateVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualServiceSpecTypeDef",
        "virtualServiceName": str,
    },
)
_OptionalCreateVirtualServiceInputRequestTypeDef = TypedDict(
    "_OptionalCreateVirtualServiceInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
        "tags": List["TagRefTypeDef"],
    },
    total=False,
)

class CreateVirtualServiceInputRequestTypeDef(
    _RequiredCreateVirtualServiceInputRequestTypeDef,
    _OptionalCreateVirtualServiceInputRequestTypeDef,
):
    pass

CreateVirtualServiceOutputTypeDef = TypedDict(
    "CreateVirtualServiceOutputTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteGatewayRouteInputRequestTypeDef = TypedDict(
    "_RequiredDeleteGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDeleteGatewayRouteInputRequestTypeDef = TypedDict(
    "_OptionalDeleteGatewayRouteInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteGatewayRouteInputRequestTypeDef(
    _RequiredDeleteGatewayRouteInputRequestTypeDef, _OptionalDeleteGatewayRouteInputRequestTypeDef
):
    pass

DeleteGatewayRouteOutputTypeDef = TypedDict(
    "DeleteGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMeshInputRequestTypeDef = TypedDict(
    "DeleteMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)

DeleteMeshOutputTypeDef = TypedDict(
    "DeleteMeshOutputTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRouteInputRequestTypeDef = TypedDict(
    "_RequiredDeleteRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
    },
)
_OptionalDeleteRouteInputRequestTypeDef = TypedDict(
    "_OptionalDeleteRouteInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteRouteInputRequestTypeDef(
    _RequiredDeleteRouteInputRequestTypeDef, _OptionalDeleteRouteInputRequestTypeDef
):
    pass

DeleteRouteOutputTypeDef = TypedDict(
    "DeleteRouteOutputTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVirtualGatewayInputRequestTypeDef = TypedDict(
    "_RequiredDeleteVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDeleteVirtualGatewayInputRequestTypeDef = TypedDict(
    "_OptionalDeleteVirtualGatewayInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteVirtualGatewayInputRequestTypeDef(
    _RequiredDeleteVirtualGatewayInputRequestTypeDef,
    _OptionalDeleteVirtualGatewayInputRequestTypeDef,
):
    pass

DeleteVirtualGatewayOutputTypeDef = TypedDict(
    "DeleteVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVirtualNodeInputRequestTypeDef = TypedDict(
    "_RequiredDeleteVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
    },
)
_OptionalDeleteVirtualNodeInputRequestTypeDef = TypedDict(
    "_OptionalDeleteVirtualNodeInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteVirtualNodeInputRequestTypeDef(
    _RequiredDeleteVirtualNodeInputRequestTypeDef, _OptionalDeleteVirtualNodeInputRequestTypeDef
):
    pass

DeleteVirtualNodeOutputTypeDef = TypedDict(
    "DeleteVirtualNodeOutputTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVirtualRouterInputRequestTypeDef = TypedDict(
    "_RequiredDeleteVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalDeleteVirtualRouterInputRequestTypeDef = TypedDict(
    "_OptionalDeleteVirtualRouterInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteVirtualRouterInputRequestTypeDef(
    _RequiredDeleteVirtualRouterInputRequestTypeDef, _OptionalDeleteVirtualRouterInputRequestTypeDef
):
    pass

DeleteVirtualRouterOutputTypeDef = TypedDict(
    "DeleteVirtualRouterOutputTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVirtualServiceInputRequestTypeDef = TypedDict(
    "_RequiredDeleteVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
    },
)
_OptionalDeleteVirtualServiceInputRequestTypeDef = TypedDict(
    "_OptionalDeleteVirtualServiceInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DeleteVirtualServiceInputRequestTypeDef(
    _RequiredDeleteVirtualServiceInputRequestTypeDef,
    _OptionalDeleteVirtualServiceInputRequestTypeDef,
):
    pass

DeleteVirtualServiceOutputTypeDef = TypedDict(
    "DeleteVirtualServiceOutputTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeGatewayRouteInputRequestTypeDef = TypedDict(
    "_RequiredDescribeGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDescribeGatewayRouteInputRequestTypeDef = TypedDict(
    "_OptionalDescribeGatewayRouteInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeGatewayRouteInputRequestTypeDef(
    _RequiredDescribeGatewayRouteInputRequestTypeDef,
    _OptionalDescribeGatewayRouteInputRequestTypeDef,
):
    pass

DescribeGatewayRouteOutputTypeDef = TypedDict(
    "DescribeGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeMeshInputRequestTypeDef = TypedDict(
    "_RequiredDescribeMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalDescribeMeshInputRequestTypeDef = TypedDict(
    "_OptionalDescribeMeshInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeMeshInputRequestTypeDef(
    _RequiredDescribeMeshInputRequestTypeDef, _OptionalDescribeMeshInputRequestTypeDef
):
    pass

DescribeMeshOutputTypeDef = TypedDict(
    "DescribeMeshOutputTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRouteInputRequestTypeDef = TypedDict(
    "_RequiredDescribeRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "virtualRouterName": str,
    },
)
_OptionalDescribeRouteInputRequestTypeDef = TypedDict(
    "_OptionalDescribeRouteInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeRouteInputRequestTypeDef(
    _RequiredDescribeRouteInputRequestTypeDef, _OptionalDescribeRouteInputRequestTypeDef
):
    pass

DescribeRouteOutputTypeDef = TypedDict(
    "DescribeRouteOutputTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVirtualGatewayInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalDescribeVirtualGatewayInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVirtualGatewayInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeVirtualGatewayInputRequestTypeDef(
    _RequiredDescribeVirtualGatewayInputRequestTypeDef,
    _OptionalDescribeVirtualGatewayInputRequestTypeDef,
):
    pass

DescribeVirtualGatewayOutputTypeDef = TypedDict(
    "DescribeVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVirtualNodeInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "virtualNodeName": str,
    },
)
_OptionalDescribeVirtualNodeInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVirtualNodeInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeVirtualNodeInputRequestTypeDef(
    _RequiredDescribeVirtualNodeInputRequestTypeDef, _OptionalDescribeVirtualNodeInputRequestTypeDef
):
    pass

DescribeVirtualNodeOutputTypeDef = TypedDict(
    "DescribeVirtualNodeOutputTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVirtualRouterInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalDescribeVirtualRouterInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVirtualRouterInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeVirtualRouterInputRequestTypeDef(
    _RequiredDescribeVirtualRouterInputRequestTypeDef,
    _OptionalDescribeVirtualRouterInputRequestTypeDef,
):
    pass

DescribeVirtualRouterOutputTypeDef = TypedDict(
    "DescribeVirtualRouterOutputTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVirtualServiceInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "virtualServiceName": str,
    },
)
_OptionalDescribeVirtualServiceInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVirtualServiceInputRequestTypeDef",
    {
        "meshOwner": str,
    },
    total=False,
)

class DescribeVirtualServiceInputRequestTypeDef(
    _RequiredDescribeVirtualServiceInputRequestTypeDef,
    _OptionalDescribeVirtualServiceInputRequestTypeDef,
):
    pass

DescribeVirtualServiceOutputTypeDef = TypedDict(
    "DescribeVirtualServiceOutputTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDnsServiceDiscoveryTypeDef = TypedDict(
    "_RequiredDnsServiceDiscoveryTypeDef",
    {
        "hostname": str,
    },
)
_OptionalDnsServiceDiscoveryTypeDef = TypedDict(
    "_OptionalDnsServiceDiscoveryTypeDef",
    {
        "responseType": DnsResponseTypeType,
    },
    total=False,
)

class DnsServiceDiscoveryTypeDef(
    _RequiredDnsServiceDiscoveryTypeDef, _OptionalDnsServiceDiscoveryTypeDef
):
    pass

DurationTypeDef = TypedDict(
    "DurationTypeDef",
    {
        "unit": DurationUnitType,
        "value": int,
    },
    total=False,
)

EgressFilterTypeDef = TypedDict(
    "EgressFilterTypeDef",
    {
        "type": EgressFilterTypeType,
    },
)

FileAccessLogTypeDef = TypedDict(
    "FileAccessLogTypeDef",
    {
        "path": str,
    },
)

GatewayRouteDataTypeDef = TypedDict(
    "GatewayRouteDataTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "GatewayRouteSpecTypeDef",
        "status": "GatewayRouteStatusTypeDef",
        "virtualGatewayName": str,
    },
)

GatewayRouteHostnameMatchTypeDef = TypedDict(
    "GatewayRouteHostnameMatchTypeDef",
    {
        "exact": str,
        "suffix": str,
    },
    total=False,
)

GatewayRouteHostnameRewriteTypeDef = TypedDict(
    "GatewayRouteHostnameRewriteTypeDef",
    {
        "defaultTargetHostname": DefaultGatewayRouteRewriteType,
    },
    total=False,
)

GatewayRouteRefTypeDef = TypedDict(
    "GatewayRouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "gatewayRouteName": str,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)

GatewayRouteSpecTypeDef = TypedDict(
    "GatewayRouteSpecTypeDef",
    {
        "grpcRoute": "GrpcGatewayRouteTypeDef",
        "http2Route": "HttpGatewayRouteTypeDef",
        "httpRoute": "HttpGatewayRouteTypeDef",
        "priority": int,
    },
    total=False,
)

GatewayRouteStatusTypeDef = TypedDict(
    "GatewayRouteStatusTypeDef",
    {
        "status": GatewayRouteStatusCodeType,
    },
)

GatewayRouteTargetTypeDef = TypedDict(
    "GatewayRouteTargetTypeDef",
    {
        "virtualService": "GatewayRouteVirtualServiceTypeDef",
    },
)

GatewayRouteVirtualServiceTypeDef = TypedDict(
    "GatewayRouteVirtualServiceTypeDef",
    {
        "virtualServiceName": str,
    },
)

_RequiredGrpcGatewayRouteActionTypeDef = TypedDict(
    "_RequiredGrpcGatewayRouteActionTypeDef",
    {
        "target": "GatewayRouteTargetTypeDef",
    },
)
_OptionalGrpcGatewayRouteActionTypeDef = TypedDict(
    "_OptionalGrpcGatewayRouteActionTypeDef",
    {
        "rewrite": "GrpcGatewayRouteRewriteTypeDef",
    },
    total=False,
)

class GrpcGatewayRouteActionTypeDef(
    _RequiredGrpcGatewayRouteActionTypeDef, _OptionalGrpcGatewayRouteActionTypeDef
):
    pass

GrpcGatewayRouteMatchTypeDef = TypedDict(
    "GrpcGatewayRouteMatchTypeDef",
    {
        "hostname": "GatewayRouteHostnameMatchTypeDef",
        "metadata": List["GrpcGatewayRouteMetadataTypeDef"],
        "serviceName": str,
    },
    total=False,
)

_RequiredGrpcGatewayRouteMetadataTypeDef = TypedDict(
    "_RequiredGrpcGatewayRouteMetadataTypeDef",
    {
        "name": str,
    },
)
_OptionalGrpcGatewayRouteMetadataTypeDef = TypedDict(
    "_OptionalGrpcGatewayRouteMetadataTypeDef",
    {
        "invert": bool,
        "match": "GrpcMetadataMatchMethodTypeDef",
    },
    total=False,
)

class GrpcGatewayRouteMetadataTypeDef(
    _RequiredGrpcGatewayRouteMetadataTypeDef, _OptionalGrpcGatewayRouteMetadataTypeDef
):
    pass

GrpcGatewayRouteRewriteTypeDef = TypedDict(
    "GrpcGatewayRouteRewriteTypeDef",
    {
        "hostname": "GatewayRouteHostnameRewriteTypeDef",
    },
    total=False,
)

GrpcGatewayRouteTypeDef = TypedDict(
    "GrpcGatewayRouteTypeDef",
    {
        "action": "GrpcGatewayRouteActionTypeDef",
        "match": "GrpcGatewayRouteMatchTypeDef",
    },
)

GrpcMetadataMatchMethodTypeDef = TypedDict(
    "GrpcMetadataMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": "MatchRangeTypeDef",
        "regex": str,
        "suffix": str,
    },
    total=False,
)

_RequiredGrpcRetryPolicyTypeDef = TypedDict(
    "_RequiredGrpcRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": "DurationTypeDef",
    },
)
_OptionalGrpcRetryPolicyTypeDef = TypedDict(
    "_OptionalGrpcRetryPolicyTypeDef",
    {
        "grpcRetryEvents": List[GrpcRetryPolicyEventType],
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[Literal["connection-error"]],
    },
    total=False,
)

class GrpcRetryPolicyTypeDef(_RequiredGrpcRetryPolicyTypeDef, _OptionalGrpcRetryPolicyTypeDef):
    pass

GrpcRouteActionTypeDef = TypedDict(
    "GrpcRouteActionTypeDef",
    {
        "weightedTargets": List["WeightedTargetTypeDef"],
    },
)

GrpcRouteMatchTypeDef = TypedDict(
    "GrpcRouteMatchTypeDef",
    {
        "metadata": List["GrpcRouteMetadataTypeDef"],
        "methodName": str,
        "serviceName": str,
    },
    total=False,
)

GrpcRouteMetadataMatchMethodTypeDef = TypedDict(
    "GrpcRouteMetadataMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": "MatchRangeTypeDef",
        "regex": str,
        "suffix": str,
    },
    total=False,
)

_RequiredGrpcRouteMetadataTypeDef = TypedDict(
    "_RequiredGrpcRouteMetadataTypeDef",
    {
        "name": str,
    },
)
_OptionalGrpcRouteMetadataTypeDef = TypedDict(
    "_OptionalGrpcRouteMetadataTypeDef",
    {
        "invert": bool,
        "match": "GrpcRouteMetadataMatchMethodTypeDef",
    },
    total=False,
)

class GrpcRouteMetadataTypeDef(
    _RequiredGrpcRouteMetadataTypeDef, _OptionalGrpcRouteMetadataTypeDef
):
    pass

_RequiredGrpcRouteTypeDef = TypedDict(
    "_RequiredGrpcRouteTypeDef",
    {
        "action": "GrpcRouteActionTypeDef",
        "match": "GrpcRouteMatchTypeDef",
    },
)
_OptionalGrpcRouteTypeDef = TypedDict(
    "_OptionalGrpcRouteTypeDef",
    {
        "retryPolicy": "GrpcRetryPolicyTypeDef",
        "timeout": "GrpcTimeoutTypeDef",
    },
    total=False,
)

class GrpcRouteTypeDef(_RequiredGrpcRouteTypeDef, _OptionalGrpcRouteTypeDef):
    pass

GrpcTimeoutTypeDef = TypedDict(
    "GrpcTimeoutTypeDef",
    {
        "idle": "DurationTypeDef",
        "perRequest": "DurationTypeDef",
    },
    total=False,
)

HeaderMatchMethodTypeDef = TypedDict(
    "HeaderMatchMethodTypeDef",
    {
        "exact": str,
        "prefix": str,
        "range": "MatchRangeTypeDef",
        "regex": str,
        "suffix": str,
    },
    total=False,
)

_RequiredHealthCheckPolicyTypeDef = TypedDict(
    "_RequiredHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": PortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalHealthCheckPolicyTypeDef = TypedDict(
    "_OptionalHealthCheckPolicyTypeDef",
    {
        "path": str,
        "port": int,
    },
    total=False,
)

class HealthCheckPolicyTypeDef(
    _RequiredHealthCheckPolicyTypeDef, _OptionalHealthCheckPolicyTypeDef
):
    pass

_RequiredHttpGatewayRouteActionTypeDef = TypedDict(
    "_RequiredHttpGatewayRouteActionTypeDef",
    {
        "target": "GatewayRouteTargetTypeDef",
    },
)
_OptionalHttpGatewayRouteActionTypeDef = TypedDict(
    "_OptionalHttpGatewayRouteActionTypeDef",
    {
        "rewrite": "HttpGatewayRouteRewriteTypeDef",
    },
    total=False,
)

class HttpGatewayRouteActionTypeDef(
    _RequiredHttpGatewayRouteActionTypeDef, _OptionalHttpGatewayRouteActionTypeDef
):
    pass

_RequiredHttpGatewayRouteHeaderTypeDef = TypedDict(
    "_RequiredHttpGatewayRouteHeaderTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpGatewayRouteHeaderTypeDef = TypedDict(
    "_OptionalHttpGatewayRouteHeaderTypeDef",
    {
        "invert": bool,
        "match": "HeaderMatchMethodTypeDef",
    },
    total=False,
)

class HttpGatewayRouteHeaderTypeDef(
    _RequiredHttpGatewayRouteHeaderTypeDef, _OptionalHttpGatewayRouteHeaderTypeDef
):
    pass

HttpGatewayRouteMatchTypeDef = TypedDict(
    "HttpGatewayRouteMatchTypeDef",
    {
        "headers": List["HttpGatewayRouteHeaderTypeDef"],
        "hostname": "GatewayRouteHostnameMatchTypeDef",
        "method": HttpMethodType,
        "path": "HttpPathMatchTypeDef",
        "prefix": str,
        "queryParameters": List["HttpQueryParameterTypeDef"],
    },
    total=False,
)

HttpGatewayRoutePathRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePathRewriteTypeDef",
    {
        "exact": str,
    },
    total=False,
)

HttpGatewayRoutePrefixRewriteTypeDef = TypedDict(
    "HttpGatewayRoutePrefixRewriteTypeDef",
    {
        "defaultPrefix": DefaultGatewayRouteRewriteType,
        "value": str,
    },
    total=False,
)

HttpGatewayRouteRewriteTypeDef = TypedDict(
    "HttpGatewayRouteRewriteTypeDef",
    {
        "hostname": "GatewayRouteHostnameRewriteTypeDef",
        "path": "HttpGatewayRoutePathRewriteTypeDef",
        "prefix": "HttpGatewayRoutePrefixRewriteTypeDef",
    },
    total=False,
)

HttpGatewayRouteTypeDef = TypedDict(
    "HttpGatewayRouteTypeDef",
    {
        "action": "HttpGatewayRouteActionTypeDef",
        "match": "HttpGatewayRouteMatchTypeDef",
    },
)

HttpPathMatchTypeDef = TypedDict(
    "HttpPathMatchTypeDef",
    {
        "exact": str,
        "regex": str,
    },
    total=False,
)

_RequiredHttpQueryParameterTypeDef = TypedDict(
    "_RequiredHttpQueryParameterTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpQueryParameterTypeDef = TypedDict(
    "_OptionalHttpQueryParameterTypeDef",
    {
        "match": "QueryParameterMatchTypeDef",
    },
    total=False,
)

class HttpQueryParameterTypeDef(
    _RequiredHttpQueryParameterTypeDef, _OptionalHttpQueryParameterTypeDef
):
    pass

_RequiredHttpRetryPolicyTypeDef = TypedDict(
    "_RequiredHttpRetryPolicyTypeDef",
    {
        "maxRetries": int,
        "perRetryTimeout": "DurationTypeDef",
    },
)
_OptionalHttpRetryPolicyTypeDef = TypedDict(
    "_OptionalHttpRetryPolicyTypeDef",
    {
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[Literal["connection-error"]],
    },
    total=False,
)

class HttpRetryPolicyTypeDef(_RequiredHttpRetryPolicyTypeDef, _OptionalHttpRetryPolicyTypeDef):
    pass

HttpRouteActionTypeDef = TypedDict(
    "HttpRouteActionTypeDef",
    {
        "weightedTargets": List["WeightedTargetTypeDef"],
    },
)

_RequiredHttpRouteHeaderTypeDef = TypedDict(
    "_RequiredHttpRouteHeaderTypeDef",
    {
        "name": str,
    },
)
_OptionalHttpRouteHeaderTypeDef = TypedDict(
    "_OptionalHttpRouteHeaderTypeDef",
    {
        "invert": bool,
        "match": "HeaderMatchMethodTypeDef",
    },
    total=False,
)

class HttpRouteHeaderTypeDef(_RequiredHttpRouteHeaderTypeDef, _OptionalHttpRouteHeaderTypeDef):
    pass

HttpRouteMatchTypeDef = TypedDict(
    "HttpRouteMatchTypeDef",
    {
        "headers": List["HttpRouteHeaderTypeDef"],
        "method": HttpMethodType,
        "path": "HttpPathMatchTypeDef",
        "prefix": str,
        "queryParameters": List["HttpQueryParameterTypeDef"],
        "scheme": HttpSchemeType,
    },
    total=False,
)

_RequiredHttpRouteTypeDef = TypedDict(
    "_RequiredHttpRouteTypeDef",
    {
        "action": "HttpRouteActionTypeDef",
        "match": "HttpRouteMatchTypeDef",
    },
)
_OptionalHttpRouteTypeDef = TypedDict(
    "_OptionalHttpRouteTypeDef",
    {
        "retryPolicy": "HttpRetryPolicyTypeDef",
        "timeout": "HttpTimeoutTypeDef",
    },
    total=False,
)

class HttpRouteTypeDef(_RequiredHttpRouteTypeDef, _OptionalHttpRouteTypeDef):
    pass

HttpTimeoutTypeDef = TypedDict(
    "HttpTimeoutTypeDef",
    {
        "idle": "DurationTypeDef",
        "perRequest": "DurationTypeDef",
    },
    total=False,
)

_RequiredListGatewayRoutesInputRequestTypeDef = TypedDict(
    "_RequiredListGatewayRoutesInputRequestTypeDef",
    {
        "meshName": str,
        "virtualGatewayName": str,
    },
)
_OptionalListGatewayRoutesInputRequestTypeDef = TypedDict(
    "_OptionalListGatewayRoutesInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListGatewayRoutesInputRequestTypeDef(
    _RequiredListGatewayRoutesInputRequestTypeDef, _OptionalListGatewayRoutesInputRequestTypeDef
):
    pass

ListGatewayRoutesOutputTypeDef = TypedDict(
    "ListGatewayRoutesOutputTypeDef",
    {
        "gatewayRoutes": List["GatewayRouteRefTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeshesInputRequestTypeDef = TypedDict(
    "ListMeshesInputRequestTypeDef",
    {
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

ListMeshesOutputTypeDef = TypedDict(
    "ListMeshesOutputTypeDef",
    {
        "meshes": List["MeshRefTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutesInputRequestTypeDef = TypedDict(
    "_RequiredListRoutesInputRequestTypeDef",
    {
        "meshName": str,
        "virtualRouterName": str,
    },
)
_OptionalListRoutesInputRequestTypeDef = TypedDict(
    "_OptionalListRoutesInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListRoutesInputRequestTypeDef(
    _RequiredListRoutesInputRequestTypeDef, _OptionalListRoutesInputRequestTypeDef
):
    pass

ListRoutesOutputTypeDef = TypedDict(
    "ListRoutesOutputTypeDef",
    {
        "nextToken": str,
        "routes": List["RouteRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "nextToken": str,
        "tags": List["TagRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVirtualGatewaysInputRequestTypeDef = TypedDict(
    "_RequiredListVirtualGatewaysInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualGatewaysInputRequestTypeDef = TypedDict(
    "_OptionalListVirtualGatewaysInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListVirtualGatewaysInputRequestTypeDef(
    _RequiredListVirtualGatewaysInputRequestTypeDef, _OptionalListVirtualGatewaysInputRequestTypeDef
):
    pass

ListVirtualGatewaysOutputTypeDef = TypedDict(
    "ListVirtualGatewaysOutputTypeDef",
    {
        "nextToken": str,
        "virtualGateways": List["VirtualGatewayRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVirtualNodesInputRequestTypeDef = TypedDict(
    "_RequiredListVirtualNodesInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualNodesInputRequestTypeDef = TypedDict(
    "_OptionalListVirtualNodesInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListVirtualNodesInputRequestTypeDef(
    _RequiredListVirtualNodesInputRequestTypeDef, _OptionalListVirtualNodesInputRequestTypeDef
):
    pass

ListVirtualNodesOutputTypeDef = TypedDict(
    "ListVirtualNodesOutputTypeDef",
    {
        "nextToken": str,
        "virtualNodes": List["VirtualNodeRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVirtualRoutersInputRequestTypeDef = TypedDict(
    "_RequiredListVirtualRoutersInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualRoutersInputRequestTypeDef = TypedDict(
    "_OptionalListVirtualRoutersInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListVirtualRoutersInputRequestTypeDef(
    _RequiredListVirtualRoutersInputRequestTypeDef, _OptionalListVirtualRoutersInputRequestTypeDef
):
    pass

ListVirtualRoutersOutputTypeDef = TypedDict(
    "ListVirtualRoutersOutputTypeDef",
    {
        "nextToken": str,
        "virtualRouters": List["VirtualRouterRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVirtualServicesInputRequestTypeDef = TypedDict(
    "_RequiredListVirtualServicesInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalListVirtualServicesInputRequestTypeDef = TypedDict(
    "_OptionalListVirtualServicesInputRequestTypeDef",
    {
        "limit": int,
        "meshOwner": str,
        "nextToken": str,
    },
    total=False,
)

class ListVirtualServicesInputRequestTypeDef(
    _RequiredListVirtualServicesInputRequestTypeDef, _OptionalListVirtualServicesInputRequestTypeDef
):
    pass

ListVirtualServicesOutputTypeDef = TypedDict(
    "ListVirtualServicesOutputTypeDef",
    {
        "nextToken": str,
        "virtualServices": List["VirtualServiceRefTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListenerTimeoutTypeDef = TypedDict(
    "ListenerTimeoutTypeDef",
    {
        "grpc": "GrpcTimeoutTypeDef",
        "http": "HttpTimeoutTypeDef",
        "http2": "HttpTimeoutTypeDef",
        "tcp": "TcpTimeoutTypeDef",
    },
    total=False,
)

ListenerTlsAcmCertificateTypeDef = TypedDict(
    "ListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)

ListenerTlsCertificateTypeDef = TypedDict(
    "ListenerTlsCertificateTypeDef",
    {
        "acm": "ListenerTlsAcmCertificateTypeDef",
        "file": "ListenerTlsFileCertificateTypeDef",
        "sds": "ListenerTlsSdsCertificateTypeDef",
    },
    total=False,
)

ListenerTlsFileCertificateTypeDef = TypedDict(
    "ListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)

ListenerTlsSdsCertificateTypeDef = TypedDict(
    "ListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)

_RequiredListenerTlsTypeDef = TypedDict(
    "_RequiredListenerTlsTypeDef",
    {
        "certificate": "ListenerTlsCertificateTypeDef",
        "mode": ListenerTlsModeType,
    },
)
_OptionalListenerTlsTypeDef = TypedDict(
    "_OptionalListenerTlsTypeDef",
    {
        "validation": "ListenerTlsValidationContextTypeDef",
    },
    total=False,
)

class ListenerTlsTypeDef(_RequiredListenerTlsTypeDef, _OptionalListenerTlsTypeDef):
    pass

ListenerTlsValidationContextTrustTypeDef = TypedDict(
    "ListenerTlsValidationContextTrustTypeDef",
    {
        "file": "TlsValidationContextFileTrustTypeDef",
        "sds": "TlsValidationContextSdsTrustTypeDef",
    },
    total=False,
)

_RequiredListenerTlsValidationContextTypeDef = TypedDict(
    "_RequiredListenerTlsValidationContextTypeDef",
    {
        "trust": "ListenerTlsValidationContextTrustTypeDef",
    },
)
_OptionalListenerTlsValidationContextTypeDef = TypedDict(
    "_OptionalListenerTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": "SubjectAlternativeNamesTypeDef",
    },
    total=False,
)

class ListenerTlsValidationContextTypeDef(
    _RequiredListenerTlsValidationContextTypeDef, _OptionalListenerTlsValidationContextTypeDef
):
    pass

_RequiredListenerTypeDef = TypedDict(
    "_RequiredListenerTypeDef",
    {
        "portMapping": "PortMappingTypeDef",
    },
)
_OptionalListenerTypeDef = TypedDict(
    "_OptionalListenerTypeDef",
    {
        "connectionPool": "VirtualNodeConnectionPoolTypeDef",
        "healthCheck": "HealthCheckPolicyTypeDef",
        "outlierDetection": "OutlierDetectionTypeDef",
        "timeout": "ListenerTimeoutTypeDef",
        "tls": "ListenerTlsTypeDef",
    },
    total=False,
)

class ListenerTypeDef(_RequiredListenerTypeDef, _OptionalListenerTypeDef):
    pass

LoggingTypeDef = TypedDict(
    "LoggingTypeDef",
    {
        "accessLog": "AccessLogTypeDef",
    },
    total=False,
)

MatchRangeTypeDef = TypedDict(
    "MatchRangeTypeDef",
    {
        "end": int,
        "start": int,
    },
)

MeshDataTypeDef = TypedDict(
    "MeshDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "MeshSpecTypeDef",
        "status": "MeshStatusTypeDef",
    },
)

MeshRefTypeDef = TypedDict(
    "MeshRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
    },
)

MeshSpecTypeDef = TypedDict(
    "MeshSpecTypeDef",
    {
        "egressFilter": "EgressFilterTypeDef",
    },
    total=False,
)

MeshStatusTypeDef = TypedDict(
    "MeshStatusTypeDef",
    {
        "status": MeshStatusCodeType,
    },
    total=False,
)

OutlierDetectionTypeDef = TypedDict(
    "OutlierDetectionTypeDef",
    {
        "baseEjectionDuration": "DurationTypeDef",
        "interval": "DurationTypeDef",
        "maxEjectionPercent": int,
        "maxServerErrors": int,
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "port": int,
        "protocol": PortProtocolType,
    },
)

QueryParameterMatchTypeDef = TypedDict(
    "QueryParameterMatchTypeDef",
    {
        "exact": str,
    },
    total=False,
)

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshOwner": str,
        "resourceOwner": str,
        "uid": str,
        "version": int,
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RouteDataTypeDef = TypedDict(
    "RouteDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "status": "RouteStatusTypeDef",
        "virtualRouterName": str,
    },
)

RouteRefTypeDef = TypedDict(
    "RouteRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "routeName": str,
        "version": int,
        "virtualRouterName": str,
    },
)

RouteSpecTypeDef = TypedDict(
    "RouteSpecTypeDef",
    {
        "grpcRoute": "GrpcRouteTypeDef",
        "http2Route": "HttpRouteTypeDef",
        "httpRoute": "HttpRouteTypeDef",
        "priority": int,
        "tcpRoute": "TcpRouteTypeDef",
    },
    total=False,
)

RouteStatusTypeDef = TypedDict(
    "RouteStatusTypeDef",
    {
        "status": RouteStatusCodeType,
    },
)

ServiceDiscoveryTypeDef = TypedDict(
    "ServiceDiscoveryTypeDef",
    {
        "awsCloudMap": "AwsCloudMapServiceDiscoveryTypeDef",
        "dns": "DnsServiceDiscoveryTypeDef",
    },
    total=False,
)

SubjectAlternativeNameMatchersTypeDef = TypedDict(
    "SubjectAlternativeNameMatchersTypeDef",
    {
        "exact": List[str],
    },
)

SubjectAlternativeNamesTypeDef = TypedDict(
    "SubjectAlternativeNamesTypeDef",
    {
        "match": "SubjectAlternativeNameMatchersTypeDef",
    },
)

TagRefTypeDef = TypedDict(
    "TagRefTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagRefTypeDef"],
    },
)

TcpRouteActionTypeDef = TypedDict(
    "TcpRouteActionTypeDef",
    {
        "weightedTargets": List["WeightedTargetTypeDef"],
    },
)

_RequiredTcpRouteTypeDef = TypedDict(
    "_RequiredTcpRouteTypeDef",
    {
        "action": "TcpRouteActionTypeDef",
    },
)
_OptionalTcpRouteTypeDef = TypedDict(
    "_OptionalTcpRouteTypeDef",
    {
        "timeout": "TcpTimeoutTypeDef",
    },
    total=False,
)

class TcpRouteTypeDef(_RequiredTcpRouteTypeDef, _OptionalTcpRouteTypeDef):
    pass

TcpTimeoutTypeDef = TypedDict(
    "TcpTimeoutTypeDef",
    {
        "idle": "DurationTypeDef",
    },
    total=False,
)

TlsValidationContextAcmTrustTypeDef = TypedDict(
    "TlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": List[str],
    },
)

TlsValidationContextFileTrustTypeDef = TypedDict(
    "TlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)

TlsValidationContextSdsTrustTypeDef = TypedDict(
    "TlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)

TlsValidationContextTrustTypeDef = TypedDict(
    "TlsValidationContextTrustTypeDef",
    {
        "acm": "TlsValidationContextAcmTrustTypeDef",
        "file": "TlsValidationContextFileTrustTypeDef",
        "sds": "TlsValidationContextSdsTrustTypeDef",
    },
    total=False,
)

_RequiredTlsValidationContextTypeDef = TypedDict(
    "_RequiredTlsValidationContextTypeDef",
    {
        "trust": "TlsValidationContextTrustTypeDef",
    },
)
_OptionalTlsValidationContextTypeDef = TypedDict(
    "_OptionalTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": "SubjectAlternativeNamesTypeDef",
    },
    total=False,
)

class TlsValidationContextTypeDef(
    _RequiredTlsValidationContextTypeDef, _OptionalTlsValidationContextTypeDef
):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateGatewayRouteInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayRouteInputRequestTypeDef",
    {
        "gatewayRouteName": str,
        "meshName": str,
        "spec": "GatewayRouteSpecTypeDef",
        "virtualGatewayName": str,
    },
)
_OptionalUpdateGatewayRouteInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayRouteInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateGatewayRouteInputRequestTypeDef(
    _RequiredUpdateGatewayRouteInputRequestTypeDef, _OptionalUpdateGatewayRouteInputRequestTypeDef
):
    pass

UpdateGatewayRouteOutputTypeDef = TypedDict(
    "UpdateGatewayRouteOutputTypeDef",
    {
        "gatewayRoute": "GatewayRouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMeshInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMeshInputRequestTypeDef",
    {
        "meshName": str,
    },
)
_OptionalUpdateMeshInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMeshInputRequestTypeDef",
    {
        "clientToken": str,
        "spec": "MeshSpecTypeDef",
    },
    total=False,
)

class UpdateMeshInputRequestTypeDef(
    _RequiredUpdateMeshInputRequestTypeDef, _OptionalUpdateMeshInputRequestTypeDef
):
    pass

UpdateMeshOutputTypeDef = TypedDict(
    "UpdateMeshOutputTypeDef",
    {
        "mesh": "MeshDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRouteInputRequestTypeDef = TypedDict(
    "_RequiredUpdateRouteInputRequestTypeDef",
    {
        "meshName": str,
        "routeName": str,
        "spec": "RouteSpecTypeDef",
        "virtualRouterName": str,
    },
)
_OptionalUpdateRouteInputRequestTypeDef = TypedDict(
    "_OptionalUpdateRouteInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateRouteInputRequestTypeDef(
    _RequiredUpdateRouteInputRequestTypeDef, _OptionalUpdateRouteInputRequestTypeDef
):
    pass

UpdateRouteOutputTypeDef = TypedDict(
    "UpdateRouteOutputTypeDef",
    {
        "route": "RouteDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVirtualGatewayInputRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualGatewayInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualGatewaySpecTypeDef",
        "virtualGatewayName": str,
    },
)
_OptionalUpdateVirtualGatewayInputRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualGatewayInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateVirtualGatewayInputRequestTypeDef(
    _RequiredUpdateVirtualGatewayInputRequestTypeDef,
    _OptionalUpdateVirtualGatewayInputRequestTypeDef,
):
    pass

UpdateVirtualGatewayOutputTypeDef = TypedDict(
    "UpdateVirtualGatewayOutputTypeDef",
    {
        "virtualGateway": "VirtualGatewayDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVirtualNodeInputRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualNodeInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualNodeSpecTypeDef",
        "virtualNodeName": str,
    },
)
_OptionalUpdateVirtualNodeInputRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualNodeInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateVirtualNodeInputRequestTypeDef(
    _RequiredUpdateVirtualNodeInputRequestTypeDef, _OptionalUpdateVirtualNodeInputRequestTypeDef
):
    pass

UpdateVirtualNodeOutputTypeDef = TypedDict(
    "UpdateVirtualNodeOutputTypeDef",
    {
        "virtualNode": "VirtualNodeDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVirtualRouterInputRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualRouterInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualRouterSpecTypeDef",
        "virtualRouterName": str,
    },
)
_OptionalUpdateVirtualRouterInputRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualRouterInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateVirtualRouterInputRequestTypeDef(
    _RequiredUpdateVirtualRouterInputRequestTypeDef, _OptionalUpdateVirtualRouterInputRequestTypeDef
):
    pass

UpdateVirtualRouterOutputTypeDef = TypedDict(
    "UpdateVirtualRouterOutputTypeDef",
    {
        "virtualRouter": "VirtualRouterDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateVirtualServiceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateVirtualServiceInputRequestTypeDef",
    {
        "meshName": str,
        "spec": "VirtualServiceSpecTypeDef",
        "virtualServiceName": str,
    },
)
_OptionalUpdateVirtualServiceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateVirtualServiceInputRequestTypeDef",
    {
        "clientToken": str,
        "meshOwner": str,
    },
    total=False,
)

class UpdateVirtualServiceInputRequestTypeDef(
    _RequiredUpdateVirtualServiceInputRequestTypeDef,
    _OptionalUpdateVirtualServiceInputRequestTypeDef,
):
    pass

UpdateVirtualServiceOutputTypeDef = TypedDict(
    "UpdateVirtualServiceOutputTypeDef",
    {
        "virtualService": "VirtualServiceDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualGatewayAccessLogTypeDef = TypedDict(
    "VirtualGatewayAccessLogTypeDef",
    {
        "file": "VirtualGatewayFileAccessLogTypeDef",
    },
    total=False,
)

VirtualGatewayBackendDefaultsTypeDef = TypedDict(
    "VirtualGatewayBackendDefaultsTypeDef",
    {
        "clientPolicy": "VirtualGatewayClientPolicyTypeDef",
    },
    total=False,
)

_RequiredVirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "_RequiredVirtualGatewayClientPolicyTlsTypeDef",
    {
        "validation": "VirtualGatewayTlsValidationContextTypeDef",
    },
)
_OptionalVirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "_OptionalVirtualGatewayClientPolicyTlsTypeDef",
    {
        "certificate": "VirtualGatewayClientTlsCertificateTypeDef",
        "enforce": bool,
        "ports": List[int],
    },
    total=False,
)

class VirtualGatewayClientPolicyTlsTypeDef(
    _RequiredVirtualGatewayClientPolicyTlsTypeDef, _OptionalVirtualGatewayClientPolicyTlsTypeDef
):
    pass

VirtualGatewayClientPolicyTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTypeDef",
    {
        "tls": "VirtualGatewayClientPolicyTlsTypeDef",
    },
    total=False,
)

VirtualGatewayClientTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayClientTlsCertificateTypeDef",
    {
        "file": "VirtualGatewayListenerTlsFileCertificateTypeDef",
        "sds": "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    },
    total=False,
)

VirtualGatewayConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayConnectionPoolTypeDef",
    {
        "grpc": "VirtualGatewayGrpcConnectionPoolTypeDef",
        "http": "VirtualGatewayHttpConnectionPoolTypeDef",
        "http2": "VirtualGatewayHttp2ConnectionPoolTypeDef",
    },
    total=False,
)

VirtualGatewayDataTypeDef = TypedDict(
    "VirtualGatewayDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualGatewaySpecTypeDef",
        "status": "VirtualGatewayStatusTypeDef",
        "virtualGatewayName": str,
    },
)

VirtualGatewayFileAccessLogTypeDef = TypedDict(
    "VirtualGatewayFileAccessLogTypeDef",
    {
        "path": str,
    },
)

VirtualGatewayGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

_RequiredVirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "_RequiredVirtualGatewayHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": VirtualGatewayPortProtocolType,
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalVirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "_OptionalVirtualGatewayHealthCheckPolicyTypeDef",
    {
        "path": str,
        "port": int,
    },
    total=False,
)

class VirtualGatewayHealthCheckPolicyTypeDef(
    _RequiredVirtualGatewayHealthCheckPolicyTypeDef, _OptionalVirtualGatewayHealthCheckPolicyTypeDef
):
    pass

VirtualGatewayHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

_RequiredVirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "_RequiredVirtualGatewayHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)
_OptionalVirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "_OptionalVirtualGatewayHttpConnectionPoolTypeDef",
    {
        "maxPendingRequests": int,
    },
    total=False,
)

class VirtualGatewayHttpConnectionPoolTypeDef(
    _RequiredVirtualGatewayHttpConnectionPoolTypeDef,
    _OptionalVirtualGatewayHttpConnectionPoolTypeDef,
):
    pass

VirtualGatewayListenerTlsAcmCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsAcmCertificateTypeDef",
    {
        "certificateArn": str,
    },
)

VirtualGatewayListenerTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsCertificateTypeDef",
    {
        "acm": "VirtualGatewayListenerTlsAcmCertificateTypeDef",
        "file": "VirtualGatewayListenerTlsFileCertificateTypeDef",
        "sds": "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    },
    total=False,
)

VirtualGatewayListenerTlsFileCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsFileCertificateTypeDef",
    {
        "certificateChain": str,
        "privateKey": str,
    },
)

VirtualGatewayListenerTlsSdsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsSdsCertificateTypeDef",
    {
        "secretName": str,
    },
)

_RequiredVirtualGatewayListenerTlsTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTlsTypeDef",
    {
        "certificate": "VirtualGatewayListenerTlsCertificateTypeDef",
        "mode": VirtualGatewayListenerTlsModeType,
    },
)
_OptionalVirtualGatewayListenerTlsTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTlsTypeDef",
    {
        "validation": "VirtualGatewayListenerTlsValidationContextTypeDef",
    },
    total=False,
)

class VirtualGatewayListenerTlsTypeDef(
    _RequiredVirtualGatewayListenerTlsTypeDef, _OptionalVirtualGatewayListenerTlsTypeDef
):
    pass

VirtualGatewayListenerTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    {
        "file": "VirtualGatewayTlsValidationContextFileTrustTypeDef",
        "sds": "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    },
    total=False,
)

_RequiredVirtualGatewayListenerTlsValidationContextTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTlsValidationContextTypeDef",
    {
        "trust": "VirtualGatewayListenerTlsValidationContextTrustTypeDef",
    },
)
_OptionalVirtualGatewayListenerTlsValidationContextTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": "SubjectAlternativeNamesTypeDef",
    },
    total=False,
)

class VirtualGatewayListenerTlsValidationContextTypeDef(
    _RequiredVirtualGatewayListenerTlsValidationContextTypeDef,
    _OptionalVirtualGatewayListenerTlsValidationContextTypeDef,
):
    pass

_RequiredVirtualGatewayListenerTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTypeDef",
    {
        "portMapping": "VirtualGatewayPortMappingTypeDef",
    },
)
_OptionalVirtualGatewayListenerTypeDef = TypedDict(
    "_OptionalVirtualGatewayListenerTypeDef",
    {
        "connectionPool": "VirtualGatewayConnectionPoolTypeDef",
        "healthCheck": "VirtualGatewayHealthCheckPolicyTypeDef",
        "tls": "VirtualGatewayListenerTlsTypeDef",
    },
    total=False,
)

class VirtualGatewayListenerTypeDef(
    _RequiredVirtualGatewayListenerTypeDef, _OptionalVirtualGatewayListenerTypeDef
):
    pass

VirtualGatewayLoggingTypeDef = TypedDict(
    "VirtualGatewayLoggingTypeDef",
    {
        "accessLog": "VirtualGatewayAccessLogTypeDef",
    },
    total=False,
)

VirtualGatewayPortMappingTypeDef = TypedDict(
    "VirtualGatewayPortMappingTypeDef",
    {
        "port": int,
        "protocol": VirtualGatewayPortProtocolType,
    },
)

VirtualGatewayRefTypeDef = TypedDict(
    "VirtualGatewayRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualGatewayName": str,
    },
)

_RequiredVirtualGatewaySpecTypeDef = TypedDict(
    "_RequiredVirtualGatewaySpecTypeDef",
    {
        "listeners": List["VirtualGatewayListenerTypeDef"],
    },
)
_OptionalVirtualGatewaySpecTypeDef = TypedDict(
    "_OptionalVirtualGatewaySpecTypeDef",
    {
        "backendDefaults": "VirtualGatewayBackendDefaultsTypeDef",
        "logging": "VirtualGatewayLoggingTypeDef",
    },
    total=False,
)

class VirtualGatewaySpecTypeDef(
    _RequiredVirtualGatewaySpecTypeDef, _OptionalVirtualGatewaySpecTypeDef
):
    pass

VirtualGatewayStatusTypeDef = TypedDict(
    "VirtualGatewayStatusTypeDef",
    {
        "status": VirtualGatewayStatusCodeType,
    },
)

VirtualGatewayTlsValidationContextAcmTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    {
        "certificateAuthorityArns": List[str],
    },
)

VirtualGatewayTlsValidationContextFileTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    {
        "certificateChain": str,
    },
)

VirtualGatewayTlsValidationContextSdsTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    {
        "secretName": str,
    },
)

VirtualGatewayTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    {
        "acm": "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
        "file": "VirtualGatewayTlsValidationContextFileTrustTypeDef",
        "sds": "VirtualGatewayTlsValidationContextSdsTrustTypeDef",
    },
    total=False,
)

_RequiredVirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "_RequiredVirtualGatewayTlsValidationContextTypeDef",
    {
        "trust": "VirtualGatewayTlsValidationContextTrustTypeDef",
    },
)
_OptionalVirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "_OptionalVirtualGatewayTlsValidationContextTypeDef",
    {
        "subjectAlternativeNames": "SubjectAlternativeNamesTypeDef",
    },
    total=False,
)

class VirtualGatewayTlsValidationContextTypeDef(
    _RequiredVirtualGatewayTlsValidationContextTypeDef,
    _OptionalVirtualGatewayTlsValidationContextTypeDef,
):
    pass

VirtualNodeConnectionPoolTypeDef = TypedDict(
    "VirtualNodeConnectionPoolTypeDef",
    {
        "grpc": "VirtualNodeGrpcConnectionPoolTypeDef",
        "http": "VirtualNodeHttpConnectionPoolTypeDef",
        "http2": "VirtualNodeHttp2ConnectionPoolTypeDef",
        "tcp": "VirtualNodeTcpConnectionPoolTypeDef",
    },
    total=False,
)

VirtualNodeDataTypeDef = TypedDict(
    "VirtualNodeDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualNodeSpecTypeDef",
        "status": "VirtualNodeStatusTypeDef",
        "virtualNodeName": str,
    },
)

VirtualNodeGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualNodeGrpcConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

VirtualNodeHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualNodeHttp2ConnectionPoolTypeDef",
    {
        "maxRequests": int,
    },
)

_RequiredVirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "_RequiredVirtualNodeHttpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)
_OptionalVirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "_OptionalVirtualNodeHttpConnectionPoolTypeDef",
    {
        "maxPendingRequests": int,
    },
    total=False,
)

class VirtualNodeHttpConnectionPoolTypeDef(
    _RequiredVirtualNodeHttpConnectionPoolTypeDef, _OptionalVirtualNodeHttpConnectionPoolTypeDef
):
    pass

VirtualNodeRefTypeDef = TypedDict(
    "VirtualNodeRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualNodeName": str,
    },
)

VirtualNodeServiceProviderTypeDef = TypedDict(
    "VirtualNodeServiceProviderTypeDef",
    {
        "virtualNodeName": str,
    },
)

VirtualNodeSpecTypeDef = TypedDict(
    "VirtualNodeSpecTypeDef",
    {
        "backendDefaults": "BackendDefaultsTypeDef",
        "backends": List["BackendTypeDef"],
        "listeners": List["ListenerTypeDef"],
        "logging": "LoggingTypeDef",
        "serviceDiscovery": "ServiceDiscoveryTypeDef",
    },
    total=False,
)

VirtualNodeStatusTypeDef = TypedDict(
    "VirtualNodeStatusTypeDef",
    {
        "status": VirtualNodeStatusCodeType,
    },
)

VirtualNodeTcpConnectionPoolTypeDef = TypedDict(
    "VirtualNodeTcpConnectionPoolTypeDef",
    {
        "maxConnections": int,
    },
)

VirtualRouterDataTypeDef = TypedDict(
    "VirtualRouterDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualRouterSpecTypeDef",
        "status": "VirtualRouterStatusTypeDef",
        "virtualRouterName": str,
    },
)

VirtualRouterListenerTypeDef = TypedDict(
    "VirtualRouterListenerTypeDef",
    {
        "portMapping": "PortMappingTypeDef",
    },
)

VirtualRouterRefTypeDef = TypedDict(
    "VirtualRouterRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualRouterName": str,
    },
)

VirtualRouterServiceProviderTypeDef = TypedDict(
    "VirtualRouterServiceProviderTypeDef",
    {
        "virtualRouterName": str,
    },
)

VirtualRouterSpecTypeDef = TypedDict(
    "VirtualRouterSpecTypeDef",
    {
        "listeners": List["VirtualRouterListenerTypeDef"],
    },
    total=False,
)

VirtualRouterStatusTypeDef = TypedDict(
    "VirtualRouterStatusTypeDef",
    {
        "status": VirtualRouterStatusCodeType,
    },
)

_RequiredVirtualServiceBackendTypeDef = TypedDict(
    "_RequiredVirtualServiceBackendTypeDef",
    {
        "virtualServiceName": str,
    },
)
_OptionalVirtualServiceBackendTypeDef = TypedDict(
    "_OptionalVirtualServiceBackendTypeDef",
    {
        "clientPolicy": "ClientPolicyTypeDef",
    },
    total=False,
)

class VirtualServiceBackendTypeDef(
    _RequiredVirtualServiceBackendTypeDef, _OptionalVirtualServiceBackendTypeDef
):
    pass

VirtualServiceDataTypeDef = TypedDict(
    "VirtualServiceDataTypeDef",
    {
        "meshName": str,
        "metadata": "ResourceMetadataTypeDef",
        "spec": "VirtualServiceSpecTypeDef",
        "status": "VirtualServiceStatusTypeDef",
        "virtualServiceName": str,
    },
)

VirtualServiceProviderTypeDef = TypedDict(
    "VirtualServiceProviderTypeDef",
    {
        "virtualNode": "VirtualNodeServiceProviderTypeDef",
        "virtualRouter": "VirtualRouterServiceProviderTypeDef",
    },
    total=False,
)

VirtualServiceRefTypeDef = TypedDict(
    "VirtualServiceRefTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "meshName": str,
        "meshOwner": str,
        "resourceOwner": str,
        "version": int,
        "virtualServiceName": str,
    },
)

VirtualServiceSpecTypeDef = TypedDict(
    "VirtualServiceSpecTypeDef",
    {
        "provider": "VirtualServiceProviderTypeDef",
    },
    total=False,
)

VirtualServiceStatusTypeDef = TypedDict(
    "VirtualServiceStatusTypeDef",
    {
        "status": VirtualServiceStatusCodeType,
    },
)

WeightedTargetTypeDef = TypedDict(
    "WeightedTargetTypeDef",
    {
        "virtualNode": str,
        "weight": int,
    },
)
