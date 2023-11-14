"""
Type annotations for migration-hub-refactor-spaces service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_migration_hub_refactor_spaces/type_defs.html)

Usage::

    ```python
    from mypy_boto3_migration_hub_refactor_spaces.type_defs import ApiGatewayProxyConfigTypeDef

    data: ApiGatewayProxyConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ApiGatewayEndpointTypeType,
    ApplicationStateType,
    EnvironmentStateType,
    ErrorCodeType,
    ErrorResourceTypeType,
    HttpMethodType,
    NetworkFabricTypeType,
    RouteActivationStateType,
    RouteStateType,
    RouteTypeType,
    ServiceEndpointTypeType,
    ServiceStateType,
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
    "ApiGatewayProxyConfigTypeDef",
    "ApiGatewayProxyInputTypeDef",
    "ApiGatewayProxySummaryTypeDef",
    "ApplicationSummaryTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateEnvironmentRequestRequestTypeDef",
    "CreateEnvironmentResponseTypeDef",
    "CreateRouteRequestRequestTypeDef",
    "CreateRouteResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "DefaultRouteInputTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteApplicationResponseTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DeleteEnvironmentResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRouteRequestRequestTypeDef",
    "DeleteRouteResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "EnvironmentSummaryTypeDef",
    "EnvironmentVpcTypeDef",
    "ErrorResponseTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetEnvironmentRequestRequestTypeDef",
    "GetEnvironmentResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetRouteRequestRequestTypeDef",
    "GetRouteResponseTypeDef",
    "GetServiceRequestRequestTypeDef",
    "GetServiceResponseTypeDef",
    "LambdaEndpointConfigTypeDef",
    "LambdaEndpointInputTypeDef",
    "LambdaEndpointSummaryTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListEnvironmentVpcsRequestRequestTypeDef",
    "ListEnvironmentVpcsResponseTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListEnvironmentsResponseTypeDef",
    "ListRoutesRequestRequestTypeDef",
    "ListRoutesResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RouteSummaryTypeDef",
    "ServiceSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRouteRequestRequestTypeDef",
    "UpdateRouteResponseTypeDef",
    "UriPathRouteInputTypeDef",
    "UrlEndpointConfigTypeDef",
    "UrlEndpointInputTypeDef",
    "UrlEndpointSummaryTypeDef",
)

ApiGatewayProxyConfigTypeDef = TypedDict(
    "ApiGatewayProxyConfigTypeDef",
    {
        "ApiGatewayId": str,
        "EndpointType": ApiGatewayEndpointTypeType,
        "NlbArn": str,
        "NlbName": str,
        "ProxyUrl": str,
        "StageName": str,
        "VpcLinkId": str,
    },
    total=False,
)

ApiGatewayProxyInputTypeDef = TypedDict(
    "ApiGatewayProxyInputTypeDef",
    {
        "EndpointType": ApiGatewayEndpointTypeType,
        "StageName": str,
    },
    total=False,
)

ApiGatewayProxySummaryTypeDef = TypedDict(
    "ApiGatewayProxySummaryTypeDef",
    {
        "ApiGatewayId": str,
        "EndpointType": ApiGatewayEndpointTypeType,
        "NlbArn": str,
        "NlbName": str,
        "ProxyUrl": str,
        "StageName": str,
        "VpcLinkId": str,
    },
    total=False,
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "ApiGatewayProxy": "ApiGatewayProxySummaryTypeDef",
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ProxyType": Literal["API_GATEWAY"],
        "State": ApplicationStateType,
        "Tags": Dict[str, str],
        "VpcId": str,
    },
    total=False,
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
        "Name": str,
        "ProxyType": Literal["API_GATEWAY"],
        "VpcId": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "ApiGatewayProxy": "ApiGatewayProxyInputTypeDef",
        "ClientToken": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApiGatewayProxy": "ApiGatewayProxyInputTypeDef",
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ProxyType": Literal["API_GATEWAY"],
        "State": ApplicationStateType,
        "Tags": Dict[str, str],
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentRequestRequestTypeDef",
    {
        "Name": str,
        "NetworkFabricType": NetworkFabricTypeType,
    },
)
_OptionalCreateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

class CreateEnvironmentRequestRequestTypeDef(
    _RequiredCreateEnvironmentRequestRequestTypeDef, _OptionalCreateEnvironmentRequestRequestTypeDef
):
    pass

CreateEnvironmentResponseTypeDef = TypedDict(
    "CreateEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "Description": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "NetworkFabricType": NetworkFabricTypeType,
        "OwnerAccountId": str,
        "State": EnvironmentStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteType": RouteTypeType,
        "ServiceIdentifier": str,
    },
)
_OptionalCreateRouteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRouteRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DefaultRoute": "DefaultRouteInputTypeDef",
        "Tags": Dict[str, str],
        "UriPathRoute": "UriPathRouteInputTypeDef",
    },
    total=False,
)

class CreateRouteRequestRequestTypeDef(
    _RequiredCreateRouteRequestRequestTypeDef, _OptionalCreateRouteRequestRequestTypeDef
):
    pass

CreateRouteResponseTypeDef = TypedDict(
    "CreateRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "OwnerAccountId": str,
        "RouteId": str,
        "RouteType": RouteTypeType,
        "ServiceId": str,
        "State": RouteStateType,
        "Tags": Dict[str, str],
        "UriPathRoute": "UriPathRouteInputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentIdentifier": str,
        "Name": str,
    },
)
_OptionalCreateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "LambdaEndpoint": "LambdaEndpointInputTypeDef",
        "Tags": Dict[str, str],
        "UrlEndpoint": "UrlEndpointInputTypeDef",
        "VpcId": str,
    },
    total=False,
)

class CreateServiceRequestRequestTypeDef(
    _RequiredCreateServiceRequestRequestTypeDef, _OptionalCreateServiceRequestRequestTypeDef
):
    pass

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "Description": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentId": str,
        "LambdaEndpoint": "LambdaEndpointInputTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "Tags": Dict[str, str],
        "UrlEndpoint": "UrlEndpointInputTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultRouteInputTypeDef = TypedDict(
    "DefaultRouteInputTypeDef",
    {
        "ActivationState": RouteActivationStateType,
    },
    total=False,
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
    },
)

DeleteApplicationResponseTypeDef = TypedDict(
    "DeleteApplicationResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "State": ApplicationStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
    },
)

DeleteEnvironmentResponseTypeDef = TypedDict(
    "DeleteEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "State": EnvironmentStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

DeleteRouteRequestRequestTypeDef = TypedDict(
    "DeleteRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteIdentifier": str,
    },
)

DeleteRouteResponseTypeDef = TypedDict(
    "DeleteRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "LastUpdatedTime": datetime,
        "RouteId": str,
        "ServiceId": str,
        "State": RouteStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "ServiceIdentifier": str,
    },
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "Name": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentSummaryTypeDef = TypedDict(
    "EnvironmentSummaryTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "Description": str,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "NetworkFabricType": NetworkFabricTypeType,
        "OwnerAccountId": str,
        "State": EnvironmentStateType,
        "Tags": Dict[str, str],
        "TransitGatewayId": str,
    },
    total=False,
)

EnvironmentVpcTypeDef = TypedDict(
    "EnvironmentVpcTypeDef",
    {
        "AccountId": str,
        "CidrBlocks": List[str],
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "LastUpdatedTime": datetime,
        "VpcId": str,
        "VpcName": str,
    },
    total=False,
)

ErrorResponseTypeDef = TypedDict(
    "ErrorResponseTypeDef",
    {
        "AccountId": str,
        "AdditionalDetails": Dict[str, str],
        "Code": ErrorCodeType,
        "Message": str,
        "ResourceIdentifier": str,
        "ResourceType": ErrorResourceTypeType,
    },
    total=False,
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
    },
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "ApiGatewayProxy": "ApiGatewayProxyConfigTypeDef",
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ProxyType": Literal["API_GATEWAY"],
        "State": ApplicationStateType,
        "Tags": Dict[str, str],
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEnvironmentRequestRequestTypeDef = TypedDict(
    "GetEnvironmentRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
    },
)

GetEnvironmentResponseTypeDef = TypedDict(
    "GetEnvironmentResponseTypeDef",
    {
        "Arn": str,
        "CreatedTime": datetime,
        "Description": str,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "NetworkFabricType": NetworkFabricTypeType,
        "OwnerAccountId": str,
        "State": EnvironmentStateType,
        "Tags": Dict[str, str],
        "TransitGatewayId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRouteRequestRequestTypeDef = TypedDict(
    "GetRouteRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteIdentifier": str,
    },
)

GetRouteResponseTypeDef = TypedDict(
    "GetRouteResponseTypeDef",
    {
        "AppendSourcePath": bool,
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "IncludeChildPaths": bool,
        "LastUpdatedTime": datetime,
        "Methods": List[HttpMethodType],
        "OwnerAccountId": str,
        "PathResourceToId": Dict[str, str],
        "RouteId": str,
        "RouteType": RouteTypeType,
        "ServiceId": str,
        "SourcePath": str,
        "State": RouteStateType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRequestRequestTypeDef = TypedDict(
    "GetServiceRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "ServiceIdentifier": str,
    },
)

GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "Description": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LambdaEndpoint": "LambdaEndpointConfigTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "Tags": Dict[str, str],
        "UrlEndpoint": "UrlEndpointConfigTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LambdaEndpointConfigTypeDef = TypedDict(
    "LambdaEndpointConfigTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

LambdaEndpointInputTypeDef = TypedDict(
    "LambdaEndpointInputTypeDef",
    {
        "Arn": str,
    },
)

LambdaEndpointSummaryTypeDef = TypedDict(
    "LambdaEndpointSummaryTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredListApplicationsRequestRequestTypeDef = TypedDict(
    "_RequiredListApplicationsRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
    },
)
_OptionalListApplicationsRequestRequestTypeDef = TypedDict(
    "_OptionalListApplicationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListApplicationsRequestRequestTypeDef(
    _RequiredListApplicationsRequestRequestTypeDef, _OptionalListApplicationsRequestRequestTypeDef
):
    pass

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationSummaryList": List["ApplicationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEnvironmentVpcsRequestRequestTypeDef = TypedDict(
    "_RequiredListEnvironmentVpcsRequestRequestTypeDef",
    {
        "EnvironmentIdentifier": str,
    },
)
_OptionalListEnvironmentVpcsRequestRequestTypeDef = TypedDict(
    "_OptionalListEnvironmentVpcsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListEnvironmentVpcsRequestRequestTypeDef(
    _RequiredListEnvironmentVpcsRequestRequestTypeDef,
    _OptionalListEnvironmentVpcsRequestRequestTypeDef,
):
    pass

ListEnvironmentVpcsResponseTypeDef = TypedDict(
    "ListEnvironmentVpcsResponseTypeDef",
    {
        "EnvironmentVpcList": List["EnvironmentVpcTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListEnvironmentsResponseTypeDef = TypedDict(
    "ListEnvironmentsResponseTypeDef",
    {
        "EnvironmentSummaryList": List["EnvironmentSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredListRoutesRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
    },
)
_OptionalListRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalListRoutesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListRoutesRequestRequestTypeDef(
    _RequiredListRoutesRequestRequestTypeDef, _OptionalListRoutesRequestRequestTypeDef
):
    pass

ListRoutesResponseTypeDef = TypedDict(
    "ListRoutesResponseTypeDef",
    {
        "NextToken": str,
        "RouteSummaryList": List["RouteSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServicesRequestRequestTypeDef = TypedDict(
    "_RequiredListServicesRequestRequestTypeDef",
    {
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
    },
)
_OptionalListServicesRequestRequestTypeDef = TypedDict(
    "_OptionalListServicesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListServicesRequestRequestTypeDef(
    _RequiredListServicesRequestRequestTypeDef, _OptionalListServicesRequestRequestTypeDef
):
    pass

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "NextToken": str,
        "ServiceSummaryList": List["ServiceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "Policy": str,
        "ResourceArn": str,
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

RouteSummaryTypeDef = TypedDict(
    "RouteSummaryTypeDef",
    {
        "AppendSourcePath": bool,
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "IncludeChildPaths": bool,
        "LastUpdatedTime": datetime,
        "Methods": List[HttpMethodType],
        "OwnerAccountId": str,
        "PathResourceToId": Dict[str, str],
        "RouteId": str,
        "RouteType": RouteTypeType,
        "ServiceId": str,
        "SourcePath": str,
        "State": RouteStateType,
        "Tags": Dict[str, str],
    },
    total=False,
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "CreatedByAccountId": str,
        "CreatedTime": datetime,
        "Description": str,
        "EndpointType": ServiceEndpointTypeType,
        "EnvironmentId": str,
        "Error": "ErrorResponseTypeDef",
        "LambdaEndpoint": "LambdaEndpointSummaryTypeDef",
        "LastUpdatedTime": datetime,
        "Name": str,
        "OwnerAccountId": str,
        "ServiceId": str,
        "State": ServiceStateType,
        "Tags": Dict[str, str],
        "UrlEndpoint": "UrlEndpointSummaryTypeDef",
        "VpcId": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

UpdateRouteRequestRequestTypeDef = TypedDict(
    "UpdateRouteRequestRequestTypeDef",
    {
        "ActivationState": RouteActivationStateType,
        "ApplicationIdentifier": str,
        "EnvironmentIdentifier": str,
        "RouteIdentifier": str,
    },
)

UpdateRouteResponseTypeDef = TypedDict(
    "UpdateRouteResponseTypeDef",
    {
        "ApplicationId": str,
        "Arn": str,
        "LastUpdatedTime": datetime,
        "RouteId": str,
        "ServiceId": str,
        "State": RouteStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUriPathRouteInputTypeDef = TypedDict(
    "_RequiredUriPathRouteInputTypeDef",
    {
        "ActivationState": RouteActivationStateType,
        "SourcePath": str,
    },
)
_OptionalUriPathRouteInputTypeDef = TypedDict(
    "_OptionalUriPathRouteInputTypeDef",
    {
        "AppendSourcePath": bool,
        "IncludeChildPaths": bool,
        "Methods": List[HttpMethodType],
    },
    total=False,
)

class UriPathRouteInputTypeDef(
    _RequiredUriPathRouteInputTypeDef, _OptionalUriPathRouteInputTypeDef
):
    pass

UrlEndpointConfigTypeDef = TypedDict(
    "UrlEndpointConfigTypeDef",
    {
        "HealthUrl": str,
        "Url": str,
    },
    total=False,
)

_RequiredUrlEndpointInputTypeDef = TypedDict(
    "_RequiredUrlEndpointInputTypeDef",
    {
        "Url": str,
    },
)
_OptionalUrlEndpointInputTypeDef = TypedDict(
    "_OptionalUrlEndpointInputTypeDef",
    {
        "HealthUrl": str,
    },
    total=False,
)

class UrlEndpointInputTypeDef(_RequiredUrlEndpointInputTypeDef, _OptionalUrlEndpointInputTypeDef):
    pass

UrlEndpointSummaryTypeDef = TypedDict(
    "UrlEndpointSummaryTypeDef",
    {
        "HealthUrl": str,
        "Url": str,
    },
    total=False,
)
