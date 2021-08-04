"""
Type annotations for apigatewayv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_apigatewayv2/literals.html)

Usage::

    ```python
    from mypy_boto3_apigatewayv2.literals import AuthorizationTypeType

    data: AuthorizationTypeType = "AWS_IAM"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AuthorizationTypeType",
    "AuthorizerTypeType",
    "ConnectionTypeType",
    "ContentHandlingStrategyType",
    "DeploymentStatusType",
    "DomainNameStatusType",
    "EndpointTypeType",
    "GetApisPaginatorName",
    "GetAuthorizersPaginatorName",
    "GetDeploymentsPaginatorName",
    "GetDomainNamesPaginatorName",
    "GetIntegrationResponsesPaginatorName",
    "GetIntegrationsPaginatorName",
    "GetModelsPaginatorName",
    "GetRouteResponsesPaginatorName",
    "GetRoutesPaginatorName",
    "GetStagesPaginatorName",
    "IntegrationTypeType",
    "JSONYAMLType",
    "LoggingLevelType",
    "OAS30Type",
    "PassthroughBehaviorType",
    "ProtocolTypeType",
    "SecurityPolicyType",
    "VpcLinkStatusType",
    "VpcLinkVersionType",
)

AuthorizationTypeType = Literal["AWS_IAM", "CUSTOM", "JWT", "NONE"]
AuthorizerTypeType = Literal["JWT", "REQUEST"]
ConnectionTypeType = Literal["INTERNET", "VPC_LINK"]
ContentHandlingStrategyType = Literal["CONVERT_TO_BINARY", "CONVERT_TO_TEXT"]
DeploymentStatusType = Literal["DEPLOYED", "FAILED", "PENDING"]
DomainNameStatusType = Literal["AVAILABLE", "UPDATING"]
EndpointTypeType = Literal["EDGE", "REGIONAL"]
GetApisPaginatorName = Literal["get_apis"]
GetAuthorizersPaginatorName = Literal["get_authorizers"]
GetDeploymentsPaginatorName = Literal["get_deployments"]
GetDomainNamesPaginatorName = Literal["get_domain_names"]
GetIntegrationResponsesPaginatorName = Literal["get_integration_responses"]
GetIntegrationsPaginatorName = Literal["get_integrations"]
GetModelsPaginatorName = Literal["get_models"]
GetRouteResponsesPaginatorName = Literal["get_route_responses"]
GetRoutesPaginatorName = Literal["get_routes"]
GetStagesPaginatorName = Literal["get_stages"]
IntegrationTypeType = Literal["AWS", "AWS_PROXY", "HTTP", "HTTP_PROXY", "MOCK"]
JSONYAMLType = Literal["JSON", "YAML"]
LoggingLevelType = Literal["ERROR", "INFO", "OFF"]
OAS30Type = Literal["OAS30"]
PassthroughBehaviorType = Literal["NEVER", "WHEN_NO_MATCH", "WHEN_NO_TEMPLATES"]
ProtocolTypeType = Literal["HTTP", "WEBSOCKET"]
SecurityPolicyType = Literal["TLS_1_0", "TLS_1_2"]
VpcLinkStatusType = Literal["AVAILABLE", "DELETING", "FAILED", "INACTIVE", "PENDING"]
VpcLinkVersionType = Literal["V2"]
