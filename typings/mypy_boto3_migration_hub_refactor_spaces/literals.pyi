"""
Type annotations for migration-hub-refactor-spaces service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/literals.html)

Usage::

    ```python
    from mypy_boto3_migration_hub_refactor_spaces.literals import ApiGatewayEndpointTypeType

    data: ApiGatewayEndpointTypeType = "PRIVATE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ApiGatewayEndpointTypeType",
    "ApplicationStateType",
    "EnvironmentStateType",
    "ErrorCodeType",
    "ErrorResourceTypeType",
    "HttpMethodType",
    "ListApplicationsPaginatorName",
    "ListEnvironmentVpcsPaginatorName",
    "ListEnvironmentsPaginatorName",
    "ListRoutesPaginatorName",
    "ListServicesPaginatorName",
    "NetworkFabricTypeType",
    "ProxyTypeType",
    "RouteActivationStateType",
    "RouteStateType",
    "RouteTypeType",
    "ServiceEndpointTypeType",
    "ServiceStateType",
)

ApiGatewayEndpointTypeType = Literal["PRIVATE", "REGIONAL"]
ApplicationStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
EnvironmentStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
ErrorCodeType = Literal[
    "INVALID_RESOURCE_STATE",
    "NOT_AUTHORIZED",
    "REQUEST_LIMIT_EXCEEDED",
    "RESOURCE_CREATION_FAILURE",
    "RESOURCE_DELETION_FAILURE",
    "RESOURCE_IN_USE",
    "RESOURCE_LIMIT_EXCEEDED",
    "RESOURCE_NOT_FOUND",
    "RESOURCE_RETRIEVAL_FAILURE",
    "RESOURCE_UPDATE_FAILURE",
    "SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE",
    "STATE_TRANSITION_FAILURE",
]
ErrorResourceTypeType = Literal[
    "API_GATEWAY",
    "APPLICATION",
    "ENVIRONMENT",
    "IAM_ROLE",
    "LAMBDA",
    "LOAD_BALANCER_LISTENER",
    "NLB",
    "RESOURCE_SHARE",
    "ROUTE",
    "ROUTE_TABLE",
    "SECURITY_GROUP",
    "SERVICE",
    "SUBNET",
    "TARGET_GROUP",
    "TRANSIT_GATEWAY",
    "TRANSIT_GATEWAY_ATTACHMENT",
    "VPC",
    "VPC_ENDPOINT_SERVICE_CONFIGURATION",
    "VPC_LINK",
]
HttpMethodType = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListEnvironmentVpcsPaginatorName = Literal["list_environment_vpcs"]
ListEnvironmentsPaginatorName = Literal["list_environments"]
ListRoutesPaginatorName = Literal["list_routes"]
ListServicesPaginatorName = Literal["list_services"]
NetworkFabricTypeType = Literal["NONE", "TRANSIT_GATEWAY"]
ProxyTypeType = Literal["API_GATEWAY"]
RouteActivationStateType = Literal["ACTIVE", "INACTIVE"]
RouteStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "INACTIVE", "UPDATING"]
RouteTypeType = Literal["DEFAULT", "URI_PATH"]
ServiceEndpointTypeType = Literal["LAMBDA", "URL"]
ServiceStateType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
