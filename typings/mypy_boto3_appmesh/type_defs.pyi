"""
Main interface for appmesh service type definitions.

Usage::

    ```python
    from mypy_boto3_appmesh.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

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
    "DnsServiceDiscoveryTypeDef",
    "DurationTypeDef",
    "EgressFilterTypeDef",
    "FileAccessLogTypeDef",
    "GatewayRouteDataTypeDef",
    "GatewayRouteRefTypeDef",
    "GatewayRouteSpecTypeDef",
    "GatewayRouteStatusTypeDef",
    "GatewayRouteTargetTypeDef",
    "GatewayRouteVirtualServiceTypeDef",
    "GrpcGatewayRouteActionTypeDef",
    "GrpcGatewayRouteMatchTypeDef",
    "GrpcGatewayRouteTypeDef",
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
    "HttpGatewayRouteMatchTypeDef",
    "HttpGatewayRouteTypeDef",
    "HttpRetryPolicyTypeDef",
    "HttpRouteActionTypeDef",
    "HttpRouteHeaderTypeDef",
    "HttpRouteMatchTypeDef",
    "HttpRouteTypeDef",
    "HttpTimeoutTypeDef",
    "ListenerTimeoutTypeDef",
    "ListenerTlsAcmCertificateTypeDef",
    "ListenerTlsCertificateTypeDef",
    "ListenerTlsFileCertificateTypeDef",
    "ListenerTlsTypeDef",
    "ListenerTypeDef",
    "LoggingTypeDef",
    "MatchRangeTypeDef",
    "MeshDataTypeDef",
    "MeshRefTypeDef",
    "MeshSpecTypeDef",
    "MeshStatusTypeDef",
    "OutlierDetectionTypeDef",
    "PortMappingTypeDef",
    "ResourceMetadataTypeDef",
    "ResponseMetadata",
    "RouteDataTypeDef",
    "RouteRefTypeDef",
    "RouteSpecTypeDef",
    "RouteStatusTypeDef",
    "ServiceDiscoveryTypeDef",
    "TagRefTypeDef",
    "TcpRouteActionTypeDef",
    "TcpRouteTypeDef",
    "TcpTimeoutTypeDef",
    "TlsValidationContextAcmTrustTypeDef",
    "TlsValidationContextFileTrustTypeDef",
    "TlsValidationContextTrustTypeDef",
    "TlsValidationContextTypeDef",
    "VirtualGatewayAccessLogTypeDef",
    "VirtualGatewayBackendDefaultsTypeDef",
    "VirtualGatewayClientPolicyTlsTypeDef",
    "VirtualGatewayClientPolicyTypeDef",
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
    "VirtualGatewayListenerTlsTypeDef",
    "VirtualGatewayListenerTypeDef",
    "VirtualGatewayLoggingTypeDef",
    "VirtualGatewayPortMappingTypeDef",
    "VirtualGatewayRefTypeDef",
    "VirtualGatewaySpecTypeDef",
    "VirtualGatewayStatusTypeDef",
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
    "VirtualGatewayTlsValidationContextFileTrustTypeDef",
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
    "CreateGatewayRouteOutputTypeDef",
    "CreateMeshOutputTypeDef",
    "CreateRouteOutputTypeDef",
    "CreateVirtualGatewayOutputTypeDef",
    "CreateVirtualNodeOutputTypeDef",
    "CreateVirtualRouterOutputTypeDef",
    "CreateVirtualServiceOutputTypeDef",
    "DeleteGatewayRouteOutputTypeDef",
    "DeleteMeshOutputTypeDef",
    "DeleteRouteOutputTypeDef",
    "DeleteVirtualGatewayOutputTypeDef",
    "DeleteVirtualNodeOutputTypeDef",
    "DeleteVirtualRouterOutputTypeDef",
    "DeleteVirtualServiceOutputTypeDef",
    "DescribeGatewayRouteOutputTypeDef",
    "DescribeMeshOutputTypeDef",
    "DescribeRouteOutputTypeDef",
    "DescribeVirtualGatewayOutputTypeDef",
    "DescribeVirtualNodeOutputTypeDef",
    "DescribeVirtualRouterOutputTypeDef",
    "DescribeVirtualServiceOutputTypeDef",
    "ListGatewayRoutesOutputTypeDef",
    "ListMeshesOutputTypeDef",
    "ListRoutesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListVirtualGatewaysOutputTypeDef",
    "ListVirtualNodesOutputTypeDef",
    "ListVirtualRoutersOutputTypeDef",
    "ListVirtualServicesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "UpdateGatewayRouteOutputTypeDef",
    "UpdateMeshOutputTypeDef",
    "UpdateRouteOutputTypeDef",
    "UpdateVirtualGatewayOutputTypeDef",
    "UpdateVirtualNodeOutputTypeDef",
    "UpdateVirtualRouterOutputTypeDef",
    "UpdateVirtualServiceOutputTypeDef",
)

AccessLogTypeDef = TypedDict("AccessLogTypeDef", {"file": "FileAccessLogTypeDef"}, total=False)

AwsCloudMapInstanceAttributeTypeDef = TypedDict(
    "AwsCloudMapInstanceAttributeTypeDef", {"key": str, "value": str}
)

_RequiredAwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "_RequiredAwsCloudMapServiceDiscoveryTypeDef", {"namespaceName": str, "serviceName": str}
)
_OptionalAwsCloudMapServiceDiscoveryTypeDef = TypedDict(
    "_OptionalAwsCloudMapServiceDiscoveryTypeDef",
    {"attributes": List["AwsCloudMapInstanceAttributeTypeDef"]},
    total=False,
)


class AwsCloudMapServiceDiscoveryTypeDef(
    _RequiredAwsCloudMapServiceDiscoveryTypeDef, _OptionalAwsCloudMapServiceDiscoveryTypeDef
):
    pass


BackendDefaultsTypeDef = TypedDict(
    "BackendDefaultsTypeDef", {"clientPolicy": "ClientPolicyTypeDef"}, total=False
)

BackendTypeDef = TypedDict(
    "BackendTypeDef", {"virtualService": "VirtualServiceBackendTypeDef"}, total=False
)

_RequiredClientPolicyTlsTypeDef = TypedDict(
    "_RequiredClientPolicyTlsTypeDef", {"validation": "TlsValidationContextTypeDef"}
)
_OptionalClientPolicyTlsTypeDef = TypedDict(
    "_OptionalClientPolicyTlsTypeDef", {"enforce": bool, "ports": List[int]}, total=False
)


class ClientPolicyTlsTypeDef(_RequiredClientPolicyTlsTypeDef, _OptionalClientPolicyTlsTypeDef):
    pass


ClientPolicyTypeDef = TypedDict(
    "ClientPolicyTypeDef", {"tls": "ClientPolicyTlsTypeDef"}, total=False
)

DnsServiceDiscoveryTypeDef = TypedDict("DnsServiceDiscoveryTypeDef", {"hostname": str})

DurationTypeDef = TypedDict(
    "DurationTypeDef", {"unit": Literal["s", "ms"], "value": int}, total=False
)

EgressFilterTypeDef = TypedDict("EgressFilterTypeDef", {"type": Literal["ALLOW_ALL", "DROP_ALL"]})

FileAccessLogTypeDef = TypedDict("FileAccessLogTypeDef", {"path": str})

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
    },
    total=False,
)

GatewayRouteStatusTypeDef = TypedDict(
    "GatewayRouteStatusTypeDef", {"status": Literal["ACTIVE", "INACTIVE", "DELETED"]}
)

GatewayRouteTargetTypeDef = TypedDict(
    "GatewayRouteTargetTypeDef", {"virtualService": "GatewayRouteVirtualServiceTypeDef"}
)

GatewayRouteVirtualServiceTypeDef = TypedDict(
    "GatewayRouteVirtualServiceTypeDef", {"virtualServiceName": str}
)

GrpcGatewayRouteActionTypeDef = TypedDict(
    "GrpcGatewayRouteActionTypeDef", {"target": "GatewayRouteTargetTypeDef"}
)

GrpcGatewayRouteMatchTypeDef = TypedDict(
    "GrpcGatewayRouteMatchTypeDef", {"serviceName": str}, total=False
)

GrpcGatewayRouteTypeDef = TypedDict(
    "GrpcGatewayRouteTypeDef",
    {"action": "GrpcGatewayRouteActionTypeDef", "match": "GrpcGatewayRouteMatchTypeDef"},
)

_RequiredGrpcRetryPolicyTypeDef = TypedDict(
    "_RequiredGrpcRetryPolicyTypeDef", {"maxRetries": int, "perRetryTimeout": "DurationTypeDef"}
)
_OptionalGrpcRetryPolicyTypeDef = TypedDict(
    "_OptionalGrpcRetryPolicyTypeDef",
    {
        "grpcRetryEvents": List[
            Literal[
                "cancelled", "deadline-exceeded", "internal", "resource-exhausted", "unavailable"
            ]
        ],
        "httpRetryEvents": List[str],
        "tcpRetryEvents": List[Literal["connection-error"]],
    },
    total=False,
)


class GrpcRetryPolicyTypeDef(_RequiredGrpcRetryPolicyTypeDef, _OptionalGrpcRetryPolicyTypeDef):
    pass


GrpcRouteActionTypeDef = TypedDict(
    "GrpcRouteActionTypeDef", {"weightedTargets": List["WeightedTargetTypeDef"]}
)

GrpcRouteMatchTypeDef = TypedDict(
    "GrpcRouteMatchTypeDef",
    {"metadata": List["GrpcRouteMetadataTypeDef"], "methodName": str, "serviceName": str},
    total=False,
)

GrpcRouteMetadataMatchMethodTypeDef = TypedDict(
    "GrpcRouteMetadataMatchMethodTypeDef",
    {"exact": str, "prefix": str, "range": "MatchRangeTypeDef", "regex": str, "suffix": str},
    total=False,
)

_RequiredGrpcRouteMetadataTypeDef = TypedDict("_RequiredGrpcRouteMetadataTypeDef", {"name": str})
_OptionalGrpcRouteMetadataTypeDef = TypedDict(
    "_OptionalGrpcRouteMetadataTypeDef",
    {"invert": bool, "match": "GrpcRouteMetadataMatchMethodTypeDef"},
    total=False,
)


class GrpcRouteMetadataTypeDef(
    _RequiredGrpcRouteMetadataTypeDef, _OptionalGrpcRouteMetadataTypeDef
):
    pass


_RequiredGrpcRouteTypeDef = TypedDict(
    "_RequiredGrpcRouteTypeDef",
    {"action": "GrpcRouteActionTypeDef", "match": "GrpcRouteMatchTypeDef"},
)
_OptionalGrpcRouteTypeDef = TypedDict(
    "_OptionalGrpcRouteTypeDef",
    {"retryPolicy": "GrpcRetryPolicyTypeDef", "timeout": "GrpcTimeoutTypeDef"},
    total=False,
)


class GrpcRouteTypeDef(_RequiredGrpcRouteTypeDef, _OptionalGrpcRouteTypeDef):
    pass


GrpcTimeoutTypeDef = TypedDict(
    "GrpcTimeoutTypeDef", {"idle": "DurationTypeDef", "perRequest": "DurationTypeDef"}, total=False
)

HeaderMatchMethodTypeDef = TypedDict(
    "HeaderMatchMethodTypeDef",
    {"exact": str, "prefix": str, "range": "MatchRangeTypeDef", "regex": str, "suffix": str},
    total=False,
)

_RequiredHealthCheckPolicyTypeDef = TypedDict(
    "_RequiredHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": Literal["http", "tcp", "http2", "grpc"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalHealthCheckPolicyTypeDef = TypedDict(
    "_OptionalHealthCheckPolicyTypeDef", {"path": str, "port": int}, total=False
)


class HealthCheckPolicyTypeDef(
    _RequiredHealthCheckPolicyTypeDef, _OptionalHealthCheckPolicyTypeDef
):
    pass


HttpGatewayRouteActionTypeDef = TypedDict(
    "HttpGatewayRouteActionTypeDef", {"target": "GatewayRouteTargetTypeDef"}
)

HttpGatewayRouteMatchTypeDef = TypedDict("HttpGatewayRouteMatchTypeDef", {"prefix": str})

HttpGatewayRouteTypeDef = TypedDict(
    "HttpGatewayRouteTypeDef",
    {"action": "HttpGatewayRouteActionTypeDef", "match": "HttpGatewayRouteMatchTypeDef"},
)

_RequiredHttpRetryPolicyTypeDef = TypedDict(
    "_RequiredHttpRetryPolicyTypeDef", {"maxRetries": int, "perRetryTimeout": "DurationTypeDef"}
)
_OptionalHttpRetryPolicyTypeDef = TypedDict(
    "_OptionalHttpRetryPolicyTypeDef",
    {"httpRetryEvents": List[str], "tcpRetryEvents": List[Literal["connection-error"]]},
    total=False,
)


class HttpRetryPolicyTypeDef(_RequiredHttpRetryPolicyTypeDef, _OptionalHttpRetryPolicyTypeDef):
    pass


HttpRouteActionTypeDef = TypedDict(
    "HttpRouteActionTypeDef", {"weightedTargets": List["WeightedTargetTypeDef"]}
)

_RequiredHttpRouteHeaderTypeDef = TypedDict("_RequiredHttpRouteHeaderTypeDef", {"name": str})
_OptionalHttpRouteHeaderTypeDef = TypedDict(
    "_OptionalHttpRouteHeaderTypeDef",
    {"invert": bool, "match": "HeaderMatchMethodTypeDef"},
    total=False,
)


class HttpRouteHeaderTypeDef(_RequiredHttpRouteHeaderTypeDef, _OptionalHttpRouteHeaderTypeDef):
    pass


_RequiredHttpRouteMatchTypeDef = TypedDict("_RequiredHttpRouteMatchTypeDef", {"prefix": str})
_OptionalHttpRouteMatchTypeDef = TypedDict(
    "_OptionalHttpRouteMatchTypeDef",
    {
        "headers": List["HttpRouteHeaderTypeDef"],
        "method": Literal[
            "GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"
        ],
        "scheme": Literal["http", "https"],
    },
    total=False,
)


class HttpRouteMatchTypeDef(_RequiredHttpRouteMatchTypeDef, _OptionalHttpRouteMatchTypeDef):
    pass


_RequiredHttpRouteTypeDef = TypedDict(
    "_RequiredHttpRouteTypeDef",
    {"action": "HttpRouteActionTypeDef", "match": "HttpRouteMatchTypeDef"},
)
_OptionalHttpRouteTypeDef = TypedDict(
    "_OptionalHttpRouteTypeDef",
    {"retryPolicy": "HttpRetryPolicyTypeDef", "timeout": "HttpTimeoutTypeDef"},
    total=False,
)


class HttpRouteTypeDef(_RequiredHttpRouteTypeDef, _OptionalHttpRouteTypeDef):
    pass


HttpTimeoutTypeDef = TypedDict(
    "HttpTimeoutTypeDef", {"idle": "DurationTypeDef", "perRequest": "DurationTypeDef"}, total=False
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
    "ListenerTlsAcmCertificateTypeDef", {"certificateArn": str}
)

ListenerTlsCertificateTypeDef = TypedDict(
    "ListenerTlsCertificateTypeDef",
    {"acm": "ListenerTlsAcmCertificateTypeDef", "file": "ListenerTlsFileCertificateTypeDef"},
    total=False,
)

ListenerTlsFileCertificateTypeDef = TypedDict(
    "ListenerTlsFileCertificateTypeDef", {"certificateChain": str, "privateKey": str}
)

ListenerTlsTypeDef = TypedDict(
    "ListenerTlsTypeDef",
    {
        "certificate": "ListenerTlsCertificateTypeDef",
        "mode": Literal["STRICT", "PERMISSIVE", "DISABLED"],
    },
)

_RequiredListenerTypeDef = TypedDict(
    "_RequiredListenerTypeDef", {"portMapping": "PortMappingTypeDef"}
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


LoggingTypeDef = TypedDict("LoggingTypeDef", {"accessLog": "AccessLogTypeDef"}, total=False)

MatchRangeTypeDef = TypedDict("MatchRangeTypeDef", {"end": int, "start": int})

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

MeshSpecTypeDef = TypedDict("MeshSpecTypeDef", {"egressFilter": "EgressFilterTypeDef"}, total=False)

MeshStatusTypeDef = TypedDict(
    "MeshStatusTypeDef", {"status": Literal["ACTIVE", "INACTIVE", "DELETED"]}, total=False
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

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef", {"port": int, "protocol": Literal["http", "tcp", "http2", "grpc"]}
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

ResponseMetadata = TypedDict(
    "ResponseMetadata",
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
    "RouteStatusTypeDef", {"status": Literal["ACTIVE", "INACTIVE", "DELETED"]}
)

ServiceDiscoveryTypeDef = TypedDict(
    "ServiceDiscoveryTypeDef",
    {"awsCloudMap": "AwsCloudMapServiceDiscoveryTypeDef", "dns": "DnsServiceDiscoveryTypeDef"},
    total=False,
)

TagRefTypeDef = TypedDict("TagRefTypeDef", {"key": str, "value": str})

TcpRouteActionTypeDef = TypedDict(
    "TcpRouteActionTypeDef", {"weightedTargets": List["WeightedTargetTypeDef"]}
)

_RequiredTcpRouteTypeDef = TypedDict(
    "_RequiredTcpRouteTypeDef", {"action": "TcpRouteActionTypeDef"}
)
_OptionalTcpRouteTypeDef = TypedDict(
    "_OptionalTcpRouteTypeDef", {"timeout": "TcpTimeoutTypeDef"}, total=False
)


class TcpRouteTypeDef(_RequiredTcpRouteTypeDef, _OptionalTcpRouteTypeDef):
    pass


TcpTimeoutTypeDef = TypedDict("TcpTimeoutTypeDef", {"idle": "DurationTypeDef"}, total=False)

TlsValidationContextAcmTrustTypeDef = TypedDict(
    "TlsValidationContextAcmTrustTypeDef", {"certificateAuthorityArns": List[str]}
)

TlsValidationContextFileTrustTypeDef = TypedDict(
    "TlsValidationContextFileTrustTypeDef", {"certificateChain": str}
)

TlsValidationContextTrustTypeDef = TypedDict(
    "TlsValidationContextTrustTypeDef",
    {"acm": "TlsValidationContextAcmTrustTypeDef", "file": "TlsValidationContextFileTrustTypeDef"},
    total=False,
)

TlsValidationContextTypeDef = TypedDict(
    "TlsValidationContextTypeDef", {"trust": "TlsValidationContextTrustTypeDef"}
)

VirtualGatewayAccessLogTypeDef = TypedDict(
    "VirtualGatewayAccessLogTypeDef", {"file": "VirtualGatewayFileAccessLogTypeDef"}, total=False
)

VirtualGatewayBackendDefaultsTypeDef = TypedDict(
    "VirtualGatewayBackendDefaultsTypeDef",
    {"clientPolicy": "VirtualGatewayClientPolicyTypeDef"},
    total=False,
)

_RequiredVirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "_RequiredVirtualGatewayClientPolicyTlsTypeDef",
    {"validation": "VirtualGatewayTlsValidationContextTypeDef"},
)
_OptionalVirtualGatewayClientPolicyTlsTypeDef = TypedDict(
    "_OptionalVirtualGatewayClientPolicyTlsTypeDef",
    {"enforce": bool, "ports": List[int]},
    total=False,
)


class VirtualGatewayClientPolicyTlsTypeDef(
    _RequiredVirtualGatewayClientPolicyTlsTypeDef, _OptionalVirtualGatewayClientPolicyTlsTypeDef
):
    pass


VirtualGatewayClientPolicyTypeDef = TypedDict(
    "VirtualGatewayClientPolicyTypeDef",
    {"tls": "VirtualGatewayClientPolicyTlsTypeDef"},
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

VirtualGatewayFileAccessLogTypeDef = TypedDict("VirtualGatewayFileAccessLogTypeDef", {"path": str})

VirtualGatewayGrpcConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayGrpcConnectionPoolTypeDef", {"maxRequests": int}
)

_RequiredVirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "_RequiredVirtualGatewayHealthCheckPolicyTypeDef",
    {
        "healthyThreshold": int,
        "intervalMillis": int,
        "protocol": Literal["http", "http2", "grpc"],
        "timeoutMillis": int,
        "unhealthyThreshold": int,
    },
)
_OptionalVirtualGatewayHealthCheckPolicyTypeDef = TypedDict(
    "_OptionalVirtualGatewayHealthCheckPolicyTypeDef", {"path": str, "port": int}, total=False
)


class VirtualGatewayHealthCheckPolicyTypeDef(
    _RequiredVirtualGatewayHealthCheckPolicyTypeDef, _OptionalVirtualGatewayHealthCheckPolicyTypeDef
):
    pass


VirtualGatewayHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualGatewayHttp2ConnectionPoolTypeDef", {"maxRequests": int}
)

_RequiredVirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "_RequiredVirtualGatewayHttpConnectionPoolTypeDef", {"maxConnections": int}
)
_OptionalVirtualGatewayHttpConnectionPoolTypeDef = TypedDict(
    "_OptionalVirtualGatewayHttpConnectionPoolTypeDef", {"maxPendingRequests": int}, total=False
)


class VirtualGatewayHttpConnectionPoolTypeDef(
    _RequiredVirtualGatewayHttpConnectionPoolTypeDef,
    _OptionalVirtualGatewayHttpConnectionPoolTypeDef,
):
    pass


VirtualGatewayListenerTlsAcmCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsAcmCertificateTypeDef", {"certificateArn": str}
)

VirtualGatewayListenerTlsCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsCertificateTypeDef",
    {
        "acm": "VirtualGatewayListenerTlsAcmCertificateTypeDef",
        "file": "VirtualGatewayListenerTlsFileCertificateTypeDef",
    },
    total=False,
)

VirtualGatewayListenerTlsFileCertificateTypeDef = TypedDict(
    "VirtualGatewayListenerTlsFileCertificateTypeDef", {"certificateChain": str, "privateKey": str}
)

VirtualGatewayListenerTlsTypeDef = TypedDict(
    "VirtualGatewayListenerTlsTypeDef",
    {
        "certificate": "VirtualGatewayListenerTlsCertificateTypeDef",
        "mode": Literal["STRICT", "PERMISSIVE", "DISABLED"],
    },
)

_RequiredVirtualGatewayListenerTypeDef = TypedDict(
    "_RequiredVirtualGatewayListenerTypeDef", {"portMapping": "VirtualGatewayPortMappingTypeDef"}
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
    "VirtualGatewayLoggingTypeDef", {"accessLog": "VirtualGatewayAccessLogTypeDef"}, total=False
)

VirtualGatewayPortMappingTypeDef = TypedDict(
    "VirtualGatewayPortMappingTypeDef", {"port": int, "protocol": Literal["http", "http2", "grpc"]}
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
    "_RequiredVirtualGatewaySpecTypeDef", {"listeners": List["VirtualGatewayListenerTypeDef"]}
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
    "VirtualGatewayStatusTypeDef", {"status": Literal["ACTIVE", "INACTIVE", "DELETED"]}
)

VirtualGatewayTlsValidationContextAcmTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextAcmTrustTypeDef", {"certificateAuthorityArns": List[str]}
)

VirtualGatewayTlsValidationContextFileTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextFileTrustTypeDef", {"certificateChain": str}
)

VirtualGatewayTlsValidationContextTrustTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTrustTypeDef",
    {
        "acm": "VirtualGatewayTlsValidationContextAcmTrustTypeDef",
        "file": "VirtualGatewayTlsValidationContextFileTrustTypeDef",
    },
    total=False,
)

VirtualGatewayTlsValidationContextTypeDef = TypedDict(
    "VirtualGatewayTlsValidationContextTypeDef",
    {"trust": "VirtualGatewayTlsValidationContextTrustTypeDef"},
)

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
    "VirtualNodeGrpcConnectionPoolTypeDef", {"maxRequests": int}
)

VirtualNodeHttp2ConnectionPoolTypeDef = TypedDict(
    "VirtualNodeHttp2ConnectionPoolTypeDef", {"maxRequests": int}
)

_RequiredVirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "_RequiredVirtualNodeHttpConnectionPoolTypeDef", {"maxConnections": int}
)
_OptionalVirtualNodeHttpConnectionPoolTypeDef = TypedDict(
    "_OptionalVirtualNodeHttpConnectionPoolTypeDef", {"maxPendingRequests": int}, total=False
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
    "VirtualNodeServiceProviderTypeDef", {"virtualNodeName": str}
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
    "VirtualNodeStatusTypeDef", {"status": Literal["ACTIVE", "INACTIVE", "DELETED"]}
)

VirtualNodeTcpConnectionPoolTypeDef = TypedDict(
    "VirtualNodeTcpConnectionPoolTypeDef", {"maxConnections": int}
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
    "VirtualRouterListenerTypeDef", {"portMapping": "PortMappingTypeDef"}
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
    "VirtualRouterServiceProviderTypeDef", {"virtualRouterName": str}
)

VirtualRouterSpecTypeDef = TypedDict(
    "VirtualRouterSpecTypeDef", {"listeners": List["VirtualRouterListenerTypeDef"]}, total=False
)

VirtualRouterStatusTypeDef = TypedDict(
    "VirtualRouterStatusTypeDef", {"status": Literal["ACTIVE", "INACTIVE", "DELETED"]}
)

_RequiredVirtualServiceBackendTypeDef = TypedDict(
    "_RequiredVirtualServiceBackendTypeDef", {"virtualServiceName": str}
)
_OptionalVirtualServiceBackendTypeDef = TypedDict(
    "_OptionalVirtualServiceBackendTypeDef", {"clientPolicy": "ClientPolicyTypeDef"}, total=False
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
    "VirtualServiceSpecTypeDef", {"provider": "VirtualServiceProviderTypeDef"}, total=False
)

VirtualServiceStatusTypeDef = TypedDict(
    "VirtualServiceStatusTypeDef", {"status": Literal["ACTIVE", "INACTIVE", "DELETED"]}
)

WeightedTargetTypeDef = TypedDict("WeightedTargetTypeDef", {"virtualNode": str, "weight": int})

_RequiredCreateGatewayRouteOutputTypeDef = TypedDict(
    "_RequiredCreateGatewayRouteOutputTypeDef", {"gatewayRoute": "GatewayRouteDataTypeDef"}
)
_OptionalCreateGatewayRouteOutputTypeDef = TypedDict(
    "_OptionalCreateGatewayRouteOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateGatewayRouteOutputTypeDef(
    _RequiredCreateGatewayRouteOutputTypeDef, _OptionalCreateGatewayRouteOutputTypeDef
):
    pass


_RequiredCreateMeshOutputTypeDef = TypedDict(
    "_RequiredCreateMeshOutputTypeDef", {"mesh": "MeshDataTypeDef"}
)
_OptionalCreateMeshOutputTypeDef = TypedDict(
    "_OptionalCreateMeshOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreateMeshOutputTypeDef(_RequiredCreateMeshOutputTypeDef, _OptionalCreateMeshOutputTypeDef):
    pass


_RequiredCreateRouteOutputTypeDef = TypedDict(
    "_RequiredCreateRouteOutputTypeDef", {"route": "RouteDataTypeDef"}
)
_OptionalCreateRouteOutputTypeDef = TypedDict(
    "_OptionalCreateRouteOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreateRouteOutputTypeDef(
    _RequiredCreateRouteOutputTypeDef, _OptionalCreateRouteOutputTypeDef
):
    pass


_RequiredCreateVirtualGatewayOutputTypeDef = TypedDict(
    "_RequiredCreateVirtualGatewayOutputTypeDef", {"virtualGateway": "VirtualGatewayDataTypeDef"}
)
_OptionalCreateVirtualGatewayOutputTypeDef = TypedDict(
    "_OptionalCreateVirtualGatewayOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateVirtualGatewayOutputTypeDef(
    _RequiredCreateVirtualGatewayOutputTypeDef, _OptionalCreateVirtualGatewayOutputTypeDef
):
    pass


_RequiredCreateVirtualNodeOutputTypeDef = TypedDict(
    "_RequiredCreateVirtualNodeOutputTypeDef", {"virtualNode": "VirtualNodeDataTypeDef"}
)
_OptionalCreateVirtualNodeOutputTypeDef = TypedDict(
    "_OptionalCreateVirtualNodeOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class CreateVirtualNodeOutputTypeDef(
    _RequiredCreateVirtualNodeOutputTypeDef, _OptionalCreateVirtualNodeOutputTypeDef
):
    pass


_RequiredCreateVirtualRouterOutputTypeDef = TypedDict(
    "_RequiredCreateVirtualRouterOutputTypeDef", {"virtualRouter": "VirtualRouterDataTypeDef"}
)
_OptionalCreateVirtualRouterOutputTypeDef = TypedDict(
    "_OptionalCreateVirtualRouterOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateVirtualRouterOutputTypeDef(
    _RequiredCreateVirtualRouterOutputTypeDef, _OptionalCreateVirtualRouterOutputTypeDef
):
    pass


_RequiredCreateVirtualServiceOutputTypeDef = TypedDict(
    "_RequiredCreateVirtualServiceOutputTypeDef", {"virtualService": "VirtualServiceDataTypeDef"}
)
_OptionalCreateVirtualServiceOutputTypeDef = TypedDict(
    "_OptionalCreateVirtualServiceOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class CreateVirtualServiceOutputTypeDef(
    _RequiredCreateVirtualServiceOutputTypeDef, _OptionalCreateVirtualServiceOutputTypeDef
):
    pass


_RequiredDeleteGatewayRouteOutputTypeDef = TypedDict(
    "_RequiredDeleteGatewayRouteOutputTypeDef", {"gatewayRoute": "GatewayRouteDataTypeDef"}
)
_OptionalDeleteGatewayRouteOutputTypeDef = TypedDict(
    "_OptionalDeleteGatewayRouteOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DeleteGatewayRouteOutputTypeDef(
    _RequiredDeleteGatewayRouteOutputTypeDef, _OptionalDeleteGatewayRouteOutputTypeDef
):
    pass


_RequiredDeleteMeshOutputTypeDef = TypedDict(
    "_RequiredDeleteMeshOutputTypeDef", {"mesh": "MeshDataTypeDef"}
)
_OptionalDeleteMeshOutputTypeDef = TypedDict(
    "_OptionalDeleteMeshOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DeleteMeshOutputTypeDef(_RequiredDeleteMeshOutputTypeDef, _OptionalDeleteMeshOutputTypeDef):
    pass


_RequiredDeleteRouteOutputTypeDef = TypedDict(
    "_RequiredDeleteRouteOutputTypeDef", {"route": "RouteDataTypeDef"}
)
_OptionalDeleteRouteOutputTypeDef = TypedDict(
    "_OptionalDeleteRouteOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DeleteRouteOutputTypeDef(
    _RequiredDeleteRouteOutputTypeDef, _OptionalDeleteRouteOutputTypeDef
):
    pass


_RequiredDeleteVirtualGatewayOutputTypeDef = TypedDict(
    "_RequiredDeleteVirtualGatewayOutputTypeDef", {"virtualGateway": "VirtualGatewayDataTypeDef"}
)
_OptionalDeleteVirtualGatewayOutputTypeDef = TypedDict(
    "_OptionalDeleteVirtualGatewayOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DeleteVirtualGatewayOutputTypeDef(
    _RequiredDeleteVirtualGatewayOutputTypeDef, _OptionalDeleteVirtualGatewayOutputTypeDef
):
    pass


_RequiredDeleteVirtualNodeOutputTypeDef = TypedDict(
    "_RequiredDeleteVirtualNodeOutputTypeDef", {"virtualNode": "VirtualNodeDataTypeDef"}
)
_OptionalDeleteVirtualNodeOutputTypeDef = TypedDict(
    "_OptionalDeleteVirtualNodeOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DeleteVirtualNodeOutputTypeDef(
    _RequiredDeleteVirtualNodeOutputTypeDef, _OptionalDeleteVirtualNodeOutputTypeDef
):
    pass


_RequiredDeleteVirtualRouterOutputTypeDef = TypedDict(
    "_RequiredDeleteVirtualRouterOutputTypeDef", {"virtualRouter": "VirtualRouterDataTypeDef"}
)
_OptionalDeleteVirtualRouterOutputTypeDef = TypedDict(
    "_OptionalDeleteVirtualRouterOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DeleteVirtualRouterOutputTypeDef(
    _RequiredDeleteVirtualRouterOutputTypeDef, _OptionalDeleteVirtualRouterOutputTypeDef
):
    pass


_RequiredDeleteVirtualServiceOutputTypeDef = TypedDict(
    "_RequiredDeleteVirtualServiceOutputTypeDef", {"virtualService": "VirtualServiceDataTypeDef"}
)
_OptionalDeleteVirtualServiceOutputTypeDef = TypedDict(
    "_OptionalDeleteVirtualServiceOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DeleteVirtualServiceOutputTypeDef(
    _RequiredDeleteVirtualServiceOutputTypeDef, _OptionalDeleteVirtualServiceOutputTypeDef
):
    pass


_RequiredDescribeGatewayRouteOutputTypeDef = TypedDict(
    "_RequiredDescribeGatewayRouteOutputTypeDef", {"gatewayRoute": "GatewayRouteDataTypeDef"}
)
_OptionalDescribeGatewayRouteOutputTypeDef = TypedDict(
    "_OptionalDescribeGatewayRouteOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeGatewayRouteOutputTypeDef(
    _RequiredDescribeGatewayRouteOutputTypeDef, _OptionalDescribeGatewayRouteOutputTypeDef
):
    pass


_RequiredDescribeMeshOutputTypeDef = TypedDict(
    "_RequiredDescribeMeshOutputTypeDef", {"mesh": "MeshDataTypeDef"}
)
_OptionalDescribeMeshOutputTypeDef = TypedDict(
    "_OptionalDescribeMeshOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DescribeMeshOutputTypeDef(
    _RequiredDescribeMeshOutputTypeDef, _OptionalDescribeMeshOutputTypeDef
):
    pass


_RequiredDescribeRouteOutputTypeDef = TypedDict(
    "_RequiredDescribeRouteOutputTypeDef", {"route": "RouteDataTypeDef"}
)
_OptionalDescribeRouteOutputTypeDef = TypedDict(
    "_OptionalDescribeRouteOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class DescribeRouteOutputTypeDef(
    _RequiredDescribeRouteOutputTypeDef, _OptionalDescribeRouteOutputTypeDef
):
    pass


_RequiredDescribeVirtualGatewayOutputTypeDef = TypedDict(
    "_RequiredDescribeVirtualGatewayOutputTypeDef", {"virtualGateway": "VirtualGatewayDataTypeDef"}
)
_OptionalDescribeVirtualGatewayOutputTypeDef = TypedDict(
    "_OptionalDescribeVirtualGatewayOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeVirtualGatewayOutputTypeDef(
    _RequiredDescribeVirtualGatewayOutputTypeDef, _OptionalDescribeVirtualGatewayOutputTypeDef
):
    pass


_RequiredDescribeVirtualNodeOutputTypeDef = TypedDict(
    "_RequiredDescribeVirtualNodeOutputTypeDef", {"virtualNode": "VirtualNodeDataTypeDef"}
)
_OptionalDescribeVirtualNodeOutputTypeDef = TypedDict(
    "_OptionalDescribeVirtualNodeOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeVirtualNodeOutputTypeDef(
    _RequiredDescribeVirtualNodeOutputTypeDef, _OptionalDescribeVirtualNodeOutputTypeDef
):
    pass


_RequiredDescribeVirtualRouterOutputTypeDef = TypedDict(
    "_RequiredDescribeVirtualRouterOutputTypeDef", {"virtualRouter": "VirtualRouterDataTypeDef"}
)
_OptionalDescribeVirtualRouterOutputTypeDef = TypedDict(
    "_OptionalDescribeVirtualRouterOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeVirtualRouterOutputTypeDef(
    _RequiredDescribeVirtualRouterOutputTypeDef, _OptionalDescribeVirtualRouterOutputTypeDef
):
    pass


_RequiredDescribeVirtualServiceOutputTypeDef = TypedDict(
    "_RequiredDescribeVirtualServiceOutputTypeDef", {"virtualService": "VirtualServiceDataTypeDef"}
)
_OptionalDescribeVirtualServiceOutputTypeDef = TypedDict(
    "_OptionalDescribeVirtualServiceOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class DescribeVirtualServiceOutputTypeDef(
    _RequiredDescribeVirtualServiceOutputTypeDef, _OptionalDescribeVirtualServiceOutputTypeDef
):
    pass


_RequiredListGatewayRoutesOutputTypeDef = TypedDict(
    "_RequiredListGatewayRoutesOutputTypeDef", {"gatewayRoutes": List["GatewayRouteRefTypeDef"]}
)
_OptionalListGatewayRoutesOutputTypeDef = TypedDict(
    "_OptionalListGatewayRoutesOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListGatewayRoutesOutputTypeDef(
    _RequiredListGatewayRoutesOutputTypeDef, _OptionalListGatewayRoutesOutputTypeDef
):
    pass


_RequiredListMeshesOutputTypeDef = TypedDict(
    "_RequiredListMeshesOutputTypeDef", {"meshes": List["MeshRefTypeDef"]}
)
_OptionalListMeshesOutputTypeDef = TypedDict(
    "_OptionalListMeshesOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListMeshesOutputTypeDef(_RequiredListMeshesOutputTypeDef, _OptionalListMeshesOutputTypeDef):
    pass


_RequiredListRoutesOutputTypeDef = TypedDict(
    "_RequiredListRoutesOutputTypeDef", {"routes": List["RouteRefTypeDef"]}
)
_OptionalListRoutesOutputTypeDef = TypedDict(
    "_OptionalListRoutesOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListRoutesOutputTypeDef(_RequiredListRoutesOutputTypeDef, _OptionalListRoutesOutputTypeDef):
    pass


_RequiredListTagsForResourceOutputTypeDef = TypedDict(
    "_RequiredListTagsForResourceOutputTypeDef", {"tags": List["TagRefTypeDef"]}
)
_OptionalListTagsForResourceOutputTypeDef = TypedDict(
    "_OptionalListTagsForResourceOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListTagsForResourceOutputTypeDef(
    _RequiredListTagsForResourceOutputTypeDef, _OptionalListTagsForResourceOutputTypeDef
):
    pass


_RequiredListVirtualGatewaysOutputTypeDef = TypedDict(
    "_RequiredListVirtualGatewaysOutputTypeDef",
    {"virtualGateways": List["VirtualGatewayRefTypeDef"]},
)
_OptionalListVirtualGatewaysOutputTypeDef = TypedDict(
    "_OptionalListVirtualGatewaysOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListVirtualGatewaysOutputTypeDef(
    _RequiredListVirtualGatewaysOutputTypeDef, _OptionalListVirtualGatewaysOutputTypeDef
):
    pass


_RequiredListVirtualNodesOutputTypeDef = TypedDict(
    "_RequiredListVirtualNodesOutputTypeDef", {"virtualNodes": List["VirtualNodeRefTypeDef"]}
)
_OptionalListVirtualNodesOutputTypeDef = TypedDict(
    "_OptionalListVirtualNodesOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListVirtualNodesOutputTypeDef(
    _RequiredListVirtualNodesOutputTypeDef, _OptionalListVirtualNodesOutputTypeDef
):
    pass


_RequiredListVirtualRoutersOutputTypeDef = TypedDict(
    "_RequiredListVirtualRoutersOutputTypeDef", {"virtualRouters": List["VirtualRouterRefTypeDef"]}
)
_OptionalListVirtualRoutersOutputTypeDef = TypedDict(
    "_OptionalListVirtualRoutersOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListVirtualRoutersOutputTypeDef(
    _RequiredListVirtualRoutersOutputTypeDef, _OptionalListVirtualRoutersOutputTypeDef
):
    pass


_RequiredListVirtualServicesOutputTypeDef = TypedDict(
    "_RequiredListVirtualServicesOutputTypeDef",
    {"virtualServices": List["VirtualServiceRefTypeDef"]},
)
_OptionalListVirtualServicesOutputTypeDef = TypedDict(
    "_OptionalListVirtualServicesOutputTypeDef",
    {"nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class ListVirtualServicesOutputTypeDef(
    _RequiredListVirtualServicesOutputTypeDef, _OptionalListVirtualServicesOutputTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredUpdateGatewayRouteOutputTypeDef = TypedDict(
    "_RequiredUpdateGatewayRouteOutputTypeDef", {"gatewayRoute": "GatewayRouteDataTypeDef"}
)
_OptionalUpdateGatewayRouteOutputTypeDef = TypedDict(
    "_OptionalUpdateGatewayRouteOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateGatewayRouteOutputTypeDef(
    _RequiredUpdateGatewayRouteOutputTypeDef, _OptionalUpdateGatewayRouteOutputTypeDef
):
    pass


_RequiredUpdateMeshOutputTypeDef = TypedDict(
    "_RequiredUpdateMeshOutputTypeDef", {"mesh": "MeshDataTypeDef"}
)
_OptionalUpdateMeshOutputTypeDef = TypedDict(
    "_OptionalUpdateMeshOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class UpdateMeshOutputTypeDef(_RequiredUpdateMeshOutputTypeDef, _OptionalUpdateMeshOutputTypeDef):
    pass


_RequiredUpdateRouteOutputTypeDef = TypedDict(
    "_RequiredUpdateRouteOutputTypeDef", {"route": "RouteDataTypeDef"}
)
_OptionalUpdateRouteOutputTypeDef = TypedDict(
    "_OptionalUpdateRouteOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class UpdateRouteOutputTypeDef(
    _RequiredUpdateRouteOutputTypeDef, _OptionalUpdateRouteOutputTypeDef
):
    pass


_RequiredUpdateVirtualGatewayOutputTypeDef = TypedDict(
    "_RequiredUpdateVirtualGatewayOutputTypeDef", {"virtualGateway": "VirtualGatewayDataTypeDef"}
)
_OptionalUpdateVirtualGatewayOutputTypeDef = TypedDict(
    "_OptionalUpdateVirtualGatewayOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateVirtualGatewayOutputTypeDef(
    _RequiredUpdateVirtualGatewayOutputTypeDef, _OptionalUpdateVirtualGatewayOutputTypeDef
):
    pass


_RequiredUpdateVirtualNodeOutputTypeDef = TypedDict(
    "_RequiredUpdateVirtualNodeOutputTypeDef", {"virtualNode": "VirtualNodeDataTypeDef"}
)
_OptionalUpdateVirtualNodeOutputTypeDef = TypedDict(
    "_OptionalUpdateVirtualNodeOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class UpdateVirtualNodeOutputTypeDef(
    _RequiredUpdateVirtualNodeOutputTypeDef, _OptionalUpdateVirtualNodeOutputTypeDef
):
    pass


_RequiredUpdateVirtualRouterOutputTypeDef = TypedDict(
    "_RequiredUpdateVirtualRouterOutputTypeDef", {"virtualRouter": "VirtualRouterDataTypeDef"}
)
_OptionalUpdateVirtualRouterOutputTypeDef = TypedDict(
    "_OptionalUpdateVirtualRouterOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateVirtualRouterOutputTypeDef(
    _RequiredUpdateVirtualRouterOutputTypeDef, _OptionalUpdateVirtualRouterOutputTypeDef
):
    pass


_RequiredUpdateVirtualServiceOutputTypeDef = TypedDict(
    "_RequiredUpdateVirtualServiceOutputTypeDef", {"virtualService": "VirtualServiceDataTypeDef"}
)
_OptionalUpdateVirtualServiceOutputTypeDef = TypedDict(
    "_OptionalUpdateVirtualServiceOutputTypeDef",
    {"ResponseMetadata": "ResponseMetadata"},
    total=False,
)


class UpdateVirtualServiceOutputTypeDef(
    _RequiredUpdateVirtualServiceOutputTypeDef, _OptionalUpdateVirtualServiceOutputTypeDef
):
    pass
