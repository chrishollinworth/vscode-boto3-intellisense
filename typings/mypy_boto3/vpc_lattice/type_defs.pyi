"""
Type annotations for vpc-lattice service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_vpc_lattice.type_defs import AccessLogSubscriptionSummaryTypeDef

    data: AccessLogSubscriptionSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AuthPolicyStateType,
    AuthTypeType,
    HealthCheckProtocolVersionType,
    IpAddressTypeType,
    LambdaEventStructureVersionType,
    ListenerProtocolType,
    ResourceConfigurationIpAddressTypeType,
    ResourceConfigurationStatusType,
    ResourceConfigurationTypeType,
    ResourceGatewayIpAddressTypeType,
    ResourceGatewayStatusType,
    ServiceNetworkLogTypeType,
    ServiceNetworkResourceAssociationStatusType,
    ServiceNetworkServiceAssociationStatusType,
    ServiceNetworkVpcAssociationStatusType,
    ServiceStatusType,
    TargetGroupProtocolType,
    TargetGroupProtocolVersionType,
    TargetGroupStatusType,
    TargetGroupTypeType,
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
    "AccessLogSubscriptionSummaryTypeDef",
    "ArnResourceTypeDef",
    "BatchUpdateRuleRequestTypeDef",
    "BatchUpdateRuleResponseTypeDef",
    "CreateAccessLogSubscriptionRequestTypeDef",
    "CreateAccessLogSubscriptionResponseTypeDef",
    "CreateListenerRequestTypeDef",
    "CreateListenerResponseTypeDef",
    "CreateResourceConfigurationRequestTypeDef",
    "CreateResourceConfigurationResponseTypeDef",
    "CreateResourceGatewayRequestTypeDef",
    "CreateResourceGatewayResponseTypeDef",
    "CreateRuleRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateServiceNetworkRequestTypeDef",
    "CreateServiceNetworkResourceAssociationRequestTypeDef",
    "CreateServiceNetworkResourceAssociationResponseTypeDef",
    "CreateServiceNetworkResponseTypeDef",
    "CreateServiceNetworkServiceAssociationRequestTypeDef",
    "CreateServiceNetworkServiceAssociationResponseTypeDef",
    "CreateServiceNetworkVpcAssociationRequestTypeDef",
    "CreateServiceNetworkVpcAssociationResponseTypeDef",
    "CreateServiceRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateTargetGroupRequestTypeDef",
    "CreateTargetGroupResponseTypeDef",
    "DeleteAccessLogSubscriptionRequestTypeDef",
    "DeleteAuthPolicyRequestTypeDef",
    "DeleteListenerRequestTypeDef",
    "DeleteResourceConfigurationRequestTypeDef",
    "DeleteResourceEndpointAssociationRequestTypeDef",
    "DeleteResourceEndpointAssociationResponseTypeDef",
    "DeleteResourceGatewayRequestTypeDef",
    "DeleteResourceGatewayResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteRuleRequestTypeDef",
    "DeleteServiceNetworkRequestTypeDef",
    "DeleteServiceNetworkResourceAssociationRequestTypeDef",
    "DeleteServiceNetworkResourceAssociationResponseTypeDef",
    "DeleteServiceNetworkServiceAssociationRequestTypeDef",
    "DeleteServiceNetworkServiceAssociationResponseTypeDef",
    "DeleteServiceNetworkVpcAssociationRequestTypeDef",
    "DeleteServiceNetworkVpcAssociationResponseTypeDef",
    "DeleteServiceRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteTargetGroupRequestTypeDef",
    "DeleteTargetGroupResponseTypeDef",
    "DeregisterTargetsRequestTypeDef",
    "DeregisterTargetsResponseTypeDef",
    "DnsEntryTypeDef",
    "DnsResourceTypeDef",
    "FixedResponseActionTypeDef",
    "ForwardActionOutputTypeDef",
    "ForwardActionTypeDef",
    "ForwardActionUnionTypeDef",
    "GetAccessLogSubscriptionRequestTypeDef",
    "GetAccessLogSubscriptionResponseTypeDef",
    "GetAuthPolicyRequestTypeDef",
    "GetAuthPolicyResponseTypeDef",
    "GetListenerRequestTypeDef",
    "GetListenerResponseTypeDef",
    "GetResourceConfigurationRequestTypeDef",
    "GetResourceConfigurationResponseTypeDef",
    "GetResourceGatewayRequestTypeDef",
    "GetResourceGatewayResponseTypeDef",
    "GetResourcePolicyRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetRuleRequestTypeDef",
    "GetRuleResponseTypeDef",
    "GetServiceNetworkRequestTypeDef",
    "GetServiceNetworkResourceAssociationRequestTypeDef",
    "GetServiceNetworkResourceAssociationResponseTypeDef",
    "GetServiceNetworkResponseTypeDef",
    "GetServiceNetworkServiceAssociationRequestTypeDef",
    "GetServiceNetworkServiceAssociationResponseTypeDef",
    "GetServiceNetworkVpcAssociationRequestTypeDef",
    "GetServiceNetworkVpcAssociationResponseTypeDef",
    "GetServiceRequestTypeDef",
    "GetServiceResponseTypeDef",
    "GetTargetGroupRequestTypeDef",
    "GetTargetGroupResponseTypeDef",
    "HeaderMatchTypeDef",
    "HeaderMatchTypeTypeDef",
    "HealthCheckConfigTypeDef",
    "HttpMatchOutputTypeDef",
    "HttpMatchTypeDef",
    "HttpMatchUnionTypeDef",
    "IpResourceTypeDef",
    "ListAccessLogSubscriptionsRequestPaginateTypeDef",
    "ListAccessLogSubscriptionsRequestTypeDef",
    "ListAccessLogSubscriptionsResponseTypeDef",
    "ListListenersRequestPaginateTypeDef",
    "ListListenersRequestTypeDef",
    "ListListenersResponseTypeDef",
    "ListResourceConfigurationsRequestPaginateTypeDef",
    "ListResourceConfigurationsRequestTypeDef",
    "ListResourceConfigurationsResponseTypeDef",
    "ListResourceEndpointAssociationsRequestPaginateTypeDef",
    "ListResourceEndpointAssociationsRequestTypeDef",
    "ListResourceEndpointAssociationsResponseTypeDef",
    "ListResourceGatewaysRequestPaginateTypeDef",
    "ListResourceGatewaysRequestTypeDef",
    "ListResourceGatewaysResponseTypeDef",
    "ListRulesRequestPaginateTypeDef",
    "ListRulesRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListServiceNetworkResourceAssociationsRequestPaginateTypeDef",
    "ListServiceNetworkResourceAssociationsRequestTypeDef",
    "ListServiceNetworkResourceAssociationsResponseTypeDef",
    "ListServiceNetworkServiceAssociationsRequestPaginateTypeDef",
    "ListServiceNetworkServiceAssociationsRequestTypeDef",
    "ListServiceNetworkServiceAssociationsResponseTypeDef",
    "ListServiceNetworkVpcAssociationsRequestPaginateTypeDef",
    "ListServiceNetworkVpcAssociationsRequestTypeDef",
    "ListServiceNetworkVpcAssociationsResponseTypeDef",
    "ListServiceNetworkVpcEndpointAssociationsRequestPaginateTypeDef",
    "ListServiceNetworkVpcEndpointAssociationsRequestTypeDef",
    "ListServiceNetworkVpcEndpointAssociationsResponseTypeDef",
    "ListServiceNetworksRequestPaginateTypeDef",
    "ListServiceNetworksRequestTypeDef",
    "ListServiceNetworksResponseTypeDef",
    "ListServicesRequestPaginateTypeDef",
    "ListServicesRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetGroupsRequestPaginateTypeDef",
    "ListTargetGroupsRequestTypeDef",
    "ListTargetGroupsResponseTypeDef",
    "ListTargetsRequestPaginateTypeDef",
    "ListTargetsRequestTypeDef",
    "ListTargetsResponseTypeDef",
    "ListenerSummaryTypeDef",
    "MatcherTypeDef",
    "PaginatorConfigTypeDef",
    "PathMatchTypeDef",
    "PathMatchTypeTypeDef",
    "PutAuthPolicyRequestTypeDef",
    "PutAuthPolicyResponseTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "RegisterTargetsRequestTypeDef",
    "RegisterTargetsResponseTypeDef",
    "ResourceConfigurationDefinitionTypeDef",
    "ResourceConfigurationSummaryTypeDef",
    "ResourceEndpointAssociationSummaryTypeDef",
    "ResourceGatewaySummaryTypeDef",
    "ResponseMetadataTypeDef",
    "RuleActionOutputTypeDef",
    "RuleActionTypeDef",
    "RuleActionUnionTypeDef",
    "RuleMatchOutputTypeDef",
    "RuleMatchTypeDef",
    "RuleMatchUnionTypeDef",
    "RuleSummaryTypeDef",
    "RuleUpdateFailureTypeDef",
    "RuleUpdateSuccessTypeDef",
    "RuleUpdateTypeDef",
    "ServiceNetworkEndpointAssociationTypeDef",
    "ServiceNetworkResourceAssociationSummaryTypeDef",
    "ServiceNetworkServiceAssociationSummaryTypeDef",
    "ServiceNetworkSummaryTypeDef",
    "ServiceNetworkVpcAssociationSummaryTypeDef",
    "ServiceSummaryTypeDef",
    "SharingConfigTypeDef",
    "TagResourceRequestTypeDef",
    "TargetFailureTypeDef",
    "TargetGroupConfigTypeDef",
    "TargetGroupSummaryTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAccessLogSubscriptionRequestTypeDef",
    "UpdateAccessLogSubscriptionResponseTypeDef",
    "UpdateListenerRequestTypeDef",
    "UpdateListenerResponseTypeDef",
    "UpdateResourceConfigurationRequestTypeDef",
    "UpdateResourceConfigurationResponseTypeDef",
    "UpdateResourceGatewayRequestTypeDef",
    "UpdateResourceGatewayResponseTypeDef",
    "UpdateRuleRequestTypeDef",
    "UpdateRuleResponseTypeDef",
    "UpdateServiceNetworkRequestTypeDef",
    "UpdateServiceNetworkResponseTypeDef",
    "UpdateServiceNetworkVpcAssociationRequestTypeDef",
    "UpdateServiceNetworkVpcAssociationResponseTypeDef",
    "UpdateServiceRequestTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateTargetGroupRequestTypeDef",
    "UpdateTargetGroupResponseTypeDef",
    "WeightedTargetGroupTypeDef",
)

AccessLogSubscriptionSummaryTypeDef = TypedDict(
    "AccessLogSubscriptionSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "destinationArn": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "resourceArn": str,
        "resourceId": str,
        "serviceNetworkLogType": NotRequired[ServiceNetworkLogTypeType],
    },
)

class ArnResourceTypeDef(TypedDict):
    arn: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class RuleUpdateFailureTypeDef(TypedDict):
    failureCode: NotRequired[str]
    failureMessage: NotRequired[str]
    ruleIdentifier: NotRequired[str]

class CreateAccessLogSubscriptionRequestTypeDef(TypedDict):
    destinationArn: str
    resourceIdentifier: str
    clientToken: NotRequired[str]
    serviceNetworkLogType: NotRequired[ServiceNetworkLogTypeType]
    tags: NotRequired[Mapping[str, str]]

class CreateResourceGatewayRequestTypeDef(TypedDict):
    name: str
    subnetIds: Sequence[str]
    vpcIdentifier: str
    clientToken: NotRequired[str]
    ipAddressType: NotRequired[ResourceGatewayIpAddressTypeType]
    securityGroupIds: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]

class SharingConfigTypeDef(TypedDict):
    enabled: NotRequired[bool]

class CreateServiceNetworkResourceAssociationRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateServiceNetworkServiceAssociationRequestTypeDef(TypedDict):
    serviceIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class DnsEntryTypeDef(TypedDict):
    domainName: NotRequired[str]
    hostedZoneId: NotRequired[str]

class CreateServiceNetworkVpcAssociationRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: str
    vpcIdentifier: str
    clientToken: NotRequired[str]
    securityGroupIds: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]

class CreateServiceRequestTypeDef(TypedDict):
    name: str
    authType: NotRequired[AuthTypeType]
    certificateArn: NotRequired[str]
    clientToken: NotRequired[str]
    customDomainName: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class DeleteAccessLogSubscriptionRequestTypeDef(TypedDict):
    accessLogSubscriptionIdentifier: str

class DeleteAuthPolicyRequestTypeDef(TypedDict):
    resourceIdentifier: str

class DeleteListenerRequestTypeDef(TypedDict):
    listenerIdentifier: str
    serviceIdentifier: str

class DeleteResourceConfigurationRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str

class DeleteResourceEndpointAssociationRequestTypeDef(TypedDict):
    resourceEndpointAssociationIdentifier: str

class DeleteResourceGatewayRequestTypeDef(TypedDict):
    resourceGatewayIdentifier: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class DeleteRuleRequestTypeDef(TypedDict):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str

class DeleteServiceNetworkRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: str

class DeleteServiceNetworkResourceAssociationRequestTypeDef(TypedDict):
    serviceNetworkResourceAssociationIdentifier: str

class DeleteServiceNetworkServiceAssociationRequestTypeDef(TypedDict):
    serviceNetworkServiceAssociationIdentifier: str

class DeleteServiceNetworkVpcAssociationRequestTypeDef(TypedDict):
    serviceNetworkVpcAssociationIdentifier: str

class DeleteServiceRequestTypeDef(TypedDict):
    serviceIdentifier: str

class DeleteTargetGroupRequestTypeDef(TypedDict):
    targetGroupIdentifier: str

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "id": str,
        "port": NotRequired[int],
    },
)
TargetFailureTypeDef = TypedDict(
    "TargetFailureTypeDef",
    {
        "failureCode": NotRequired[str],
        "failureMessage": NotRequired[str],
        "id": NotRequired[str],
        "port": NotRequired[int],
    },
)

class DnsResourceTypeDef(TypedDict):
    domainName: NotRequired[str]
    ipAddressType: NotRequired[ResourceConfigurationIpAddressTypeType]

class FixedResponseActionTypeDef(TypedDict):
    statusCode: int

class WeightedTargetGroupTypeDef(TypedDict):
    targetGroupIdentifier: str
    weight: NotRequired[int]

class GetAccessLogSubscriptionRequestTypeDef(TypedDict):
    accessLogSubscriptionIdentifier: str

class GetAuthPolicyRequestTypeDef(TypedDict):
    resourceIdentifier: str

class GetListenerRequestTypeDef(TypedDict):
    listenerIdentifier: str
    serviceIdentifier: str

class GetResourceConfigurationRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str

class GetResourceGatewayRequestTypeDef(TypedDict):
    resourceGatewayIdentifier: str

class GetResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class GetRuleRequestTypeDef(TypedDict):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str

class GetServiceNetworkRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: str

class GetServiceNetworkResourceAssociationRequestTypeDef(TypedDict):
    serviceNetworkResourceAssociationIdentifier: str

class GetServiceNetworkServiceAssociationRequestTypeDef(TypedDict):
    serviceNetworkServiceAssociationIdentifier: str

class GetServiceNetworkVpcAssociationRequestTypeDef(TypedDict):
    serviceNetworkVpcAssociationIdentifier: str

class GetServiceRequestTypeDef(TypedDict):
    serviceIdentifier: str

class GetTargetGroupRequestTypeDef(TypedDict):
    targetGroupIdentifier: str

class HeaderMatchTypeTypeDef(TypedDict):
    contains: NotRequired[str]
    exact: NotRequired[str]
    prefix: NotRequired[str]

class MatcherTypeDef(TypedDict):
    httpCode: NotRequired[str]

class IpResourceTypeDef(TypedDict):
    ipAddress: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAccessLogSubscriptionsRequestTypeDef(TypedDict):
    resourceIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListListenersRequestTypeDef(TypedDict):
    serviceIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ListenerSummaryTypeDef = TypedDict(
    "ListenerSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "port": NotRequired[int],
        "protocol": NotRequired[ListenerProtocolType],
    },
)

class ListResourceConfigurationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    resourceConfigurationGroupIdentifier: NotRequired[str]
    resourceGatewayIdentifier: NotRequired[str]

ResourceConfigurationSummaryTypeDef = TypedDict(
    "ResourceConfigurationSummaryTypeDef",
    {
        "amazonManaged": NotRequired[bool],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "resourceConfigurationGroupId": NotRequired[str],
        "resourceGatewayId": NotRequired[str],
        "status": NotRequired[ResourceConfigurationStatusType],
        "type": NotRequired[ResourceConfigurationTypeType],
    },
)

class ListResourceEndpointAssociationsRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    resourceEndpointAssociationIdentifier: NotRequired[str]
    vpcEndpointId: NotRequired[str]
    vpcEndpointOwner: NotRequired[str]

ResourceEndpointAssociationSummaryTypeDef = TypedDict(
    "ResourceEndpointAssociationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "id": NotRequired[str],
        "resourceConfigurationArn": NotRequired[str],
        "resourceConfigurationId": NotRequired[str],
        "resourceConfigurationName": NotRequired[str],
        "vpcEndpointId": NotRequired[str],
        "vpcEndpointOwner": NotRequired[str],
    },
)

class ListResourceGatewaysRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ResourceGatewaySummaryTypeDef = TypedDict(
    "ResourceGatewaySummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "ipAddressType": NotRequired[ResourceGatewayIpAddressTypeType],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "securityGroupIds": NotRequired[List[str]],
        "status": NotRequired[ResourceGatewayStatusType],
        "subnetIds": NotRequired[List[str]],
        "vpcIdentifier": NotRequired[str],
    },
)

class ListRulesRequestTypeDef(TypedDict):
    listenerIdentifier: str
    serviceIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "isDefault": NotRequired[bool],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "priority": NotRequired[int],
    },
)

class ListServiceNetworkResourceAssociationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    resourceConfigurationIdentifier: NotRequired[str]
    serviceNetworkIdentifier: NotRequired[str]

class ListServiceNetworkServiceAssociationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    serviceIdentifier: NotRequired[str]
    serviceNetworkIdentifier: NotRequired[str]

class ListServiceNetworkVpcAssociationsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    serviceNetworkIdentifier: NotRequired[str]
    vpcIdentifier: NotRequired[str]

ServiceNetworkVpcAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkVpcAssociationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "serviceNetworkArn": NotRequired[str],
        "serviceNetworkId": NotRequired[str],
        "serviceNetworkName": NotRequired[str],
        "status": NotRequired[ServiceNetworkVpcAssociationStatusType],
        "vpcId": NotRequired[str],
    },
)

class ListServiceNetworkVpcEndpointAssociationsRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ServiceNetworkEndpointAssociationTypeDef = TypedDict(
    "ServiceNetworkEndpointAssociationTypeDef",
    {
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "serviceNetworkArn": NotRequired[str],
        "state": NotRequired[str],
        "vpcEndpointId": NotRequired[str],
        "vpcEndpointOwnerId": NotRequired[str],
        "vpcId": NotRequired[str],
    },
)

class ListServiceNetworksRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ServiceNetworkSummaryTypeDef = TypedDict(
    "ServiceNetworkSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "numberOfAssociatedResourceConfigurations": NotRequired[int],
        "numberOfAssociatedServices": NotRequired[int],
        "numberOfAssociatedVPCs": NotRequired[int],
    },
)

class ListServicesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTargetGroupsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    targetGroupType: NotRequired[TargetGroupTypeType]
    vpcIdentifier: NotRequired[str]

TargetGroupSummaryTypeDef = TypedDict(
    "TargetGroupSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "id": NotRequired[str],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "lambdaEventStructureVersion": NotRequired[LambdaEventStructureVersionType],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "port": NotRequired[int],
        "protocol": NotRequired[TargetGroupProtocolType],
        "serviceArns": NotRequired[List[str]],
        "status": NotRequired[TargetGroupStatusType],
        "type": NotRequired[TargetGroupTypeType],
        "vpcIdentifier": NotRequired[str],
    },
)
TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "id": NotRequired[str],
        "port": NotRequired[int],
        "reasonCode": NotRequired[str],
        "status": NotRequired[TargetStatusType],
    },
)

class PathMatchTypeTypeDef(TypedDict):
    exact: NotRequired[str]
    prefix: NotRequired[str]

class PutAuthPolicyRequestTypeDef(TypedDict):
    policy: str
    resourceIdentifier: str

class PutResourcePolicyRequestTypeDef(TypedDict):
    policy: str
    resourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessLogSubscriptionRequestTypeDef(TypedDict):
    accessLogSubscriptionIdentifier: str
    destinationArn: str

class UpdateResourceGatewayRequestTypeDef(TypedDict):
    resourceGatewayIdentifier: str
    securityGroupIds: NotRequired[Sequence[str]]

class UpdateServiceNetworkRequestTypeDef(TypedDict):
    authType: AuthTypeType
    serviceNetworkIdentifier: str

class UpdateServiceNetworkVpcAssociationRequestTypeDef(TypedDict):
    securityGroupIds: Sequence[str]
    serviceNetworkVpcAssociationIdentifier: str

class UpdateServiceRequestTypeDef(TypedDict):
    serviceIdentifier: str
    authType: NotRequired[AuthTypeType]
    certificateArn: NotRequired[str]

CreateAccessLogSubscriptionResponseTypeDef = TypedDict(
    "CreateAccessLogSubscriptionResponseTypeDef",
    {
        "arn": str,
        "destinationArn": str,
        "id": str,
        "resourceArn": str,
        "resourceId": str,
        "serviceNetworkLogType": ServiceNetworkLogTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceGatewayResponseTypeDef = TypedDict(
    "CreateResourceGatewayResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ipAddressType": ResourceGatewayIpAddressTypeType,
        "name": str,
        "securityGroupIds": List[str],
        "status": ResourceGatewayStatusType,
        "subnetIds": List[str],
        "vpcIdentifier": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceNetworkResourceAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkResourceAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "id": str,
        "status": ServiceNetworkResourceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "id": str,
        "securityGroupIds": List[str],
        "status": ServiceNetworkVpcAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResourceEndpointAssociationResponseTypeDef = TypedDict(
    "DeleteResourceEndpointAssociationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "resourceConfigurationArn": str,
        "resourceConfigurationId": str,
        "vpcEndpointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResourceGatewayResponseTypeDef = TypedDict(
    "DeleteResourceGatewayResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "status": ResourceGatewayStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceNetworkResourceAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkResourceAssociationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": ServiceNetworkResourceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTargetGroupResponseTypeDef = TypedDict(
    "DeleteTargetGroupResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": TargetGroupStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessLogSubscriptionResponseTypeDef = TypedDict(
    "GetAccessLogSubscriptionResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "destinationArn": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "resourceArn": str,
        "resourceId": str,
        "serviceNetworkLogType": ServiceNetworkLogTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetAuthPolicyResponseTypeDef(TypedDict):
    createdAt: datetime
    lastUpdatedAt: datetime
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadataTypeDef

GetResourceGatewayResponseTypeDef = TypedDict(
    "GetResourceGatewayResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "ipAddressType": ResourceGatewayIpAddressTypeType,
        "lastUpdatedAt": datetime,
        "name": str,
        "securityGroupIds": List[str],
        "status": ResourceGatewayStatusType,
        "subnetIds": List[str],
        "vpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetResourcePolicyResponseTypeDef(TypedDict):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

GetServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "securityGroupIds": List[str],
        "serviceNetworkArn": str,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "vpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListAccessLogSubscriptionsResponseTypeDef(TypedDict):
    items: List[AccessLogSubscriptionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAuthPolicyResponseTypeDef(TypedDict):
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadataTypeDef

UpdateAccessLogSubscriptionResponseTypeDef = TypedDict(
    "UpdateAccessLogSubscriptionResponseTypeDef",
    {
        "arn": str,
        "destinationArn": str,
        "id": str,
        "resourceArn": str,
        "resourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateResourceGatewayResponseTypeDef = TypedDict(
    "UpdateResourceGatewayResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "ipAddressType": IpAddressTypeType,
        "name": str,
        "securityGroupIds": List[str],
        "status": ResourceGatewayStatusType,
        "subnetIds": List[str],
        "vpcId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceNetworkResponseTypeDef = TypedDict(
    "UpdateServiceNetworkResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "id": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "UpdateServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "id": str,
        "securityGroupIds": List[str],
        "status": ServiceNetworkVpcAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "certificateArn": str,
        "customDomainName": str,
        "id": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateServiceNetworkRequestTypeDef(TypedDict):
    name: str
    authType: NotRequired[AuthTypeType]
    clientToken: NotRequired[str]
    sharingConfig: NotRequired[SharingConfigTypeDef]
    tags: NotRequired[Mapping[str, str]]

CreateServiceNetworkResponseTypeDef = TypedDict(
    "CreateServiceNetworkResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "id": str,
        "name": str,
        "sharingConfig": SharingConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkResponseTypeDef = TypedDict(
    "GetServiceNetworkResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "createdAt": datetime,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "numberOfAssociatedServices": int,
        "numberOfAssociatedVPCs": int,
        "sharingConfig": SharingConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "certificateArn": str,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "id": str,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkResourceAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkResourceAssociationResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "dnsEntry": DnsEntryTypeDef,
        "failureCode": str,
        "failureReason": str,
        "id": str,
        "isManagedAssociation": bool,
        "lastUpdatedAt": datetime,
        "privateDnsEntry": DnsEntryTypeDef,
        "resourceConfigurationArn": str,
        "resourceConfigurationId": str,
        "resourceConfigurationName": str,
        "serviceNetworkArn": str,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "status": ServiceNetworkResourceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "serviceArn": str,
        "serviceId": str,
        "serviceName": str,
        "serviceNetworkArn": str,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "certificateArn": str,
        "createdAt": datetime,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceNetworkResourceAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkResourceAssociationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "dnsEntry": NotRequired[DnsEntryTypeDef],
        "failureCode": NotRequired[str],
        "id": NotRequired[str],
        "isManagedAssociation": NotRequired[bool],
        "privateDnsEntry": NotRequired[DnsEntryTypeDef],
        "resourceConfigurationArn": NotRequired[str],
        "resourceConfigurationId": NotRequired[str],
        "resourceConfigurationName": NotRequired[str],
        "serviceNetworkArn": NotRequired[str],
        "serviceNetworkId": NotRequired[str],
        "serviceNetworkName": NotRequired[str],
        "status": NotRequired[ServiceNetworkResourceAssociationStatusType],
    },
)
ServiceNetworkServiceAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkServiceAssociationSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "createdBy": NotRequired[str],
        "customDomainName": NotRequired[str],
        "dnsEntry": NotRequired[DnsEntryTypeDef],
        "id": NotRequired[str],
        "serviceArn": NotRequired[str],
        "serviceId": NotRequired[str],
        "serviceName": NotRequired[str],
        "serviceNetworkArn": NotRequired[str],
        "serviceNetworkId": NotRequired[str],
        "serviceNetworkName": NotRequired[str],
        "status": NotRequired[ServiceNetworkServiceAssociationStatusType],
    },
)
ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "customDomainName": NotRequired[str],
        "dnsEntry": NotRequired[DnsEntryTypeDef],
        "id": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "name": NotRequired[str],
        "status": NotRequired[ServiceStatusType],
    },
)

class DeregisterTargetsRequestTypeDef(TypedDict):
    targetGroupIdentifier: str
    targets: Sequence[TargetTypeDef]

class ListTargetsRequestTypeDef(TypedDict):
    targetGroupIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    targets: NotRequired[Sequence[TargetTypeDef]]

class RegisterTargetsRequestTypeDef(TypedDict):
    targetGroupIdentifier: str
    targets: Sequence[TargetTypeDef]

class DeregisterTargetsResponseTypeDef(TypedDict):
    successful: List[TargetTypeDef]
    unsuccessful: List[TargetFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTargetsResponseTypeDef(TypedDict):
    successful: List[TargetTypeDef]
    unsuccessful: List[TargetFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ForwardActionOutputTypeDef(TypedDict):
    targetGroups: List[WeightedTargetGroupTypeDef]

class ForwardActionTypeDef(TypedDict):
    targetGroups: Sequence[WeightedTargetGroupTypeDef]

class HeaderMatchTypeDef(TypedDict):
    match: HeaderMatchTypeTypeDef
    name: str
    caseSensitive: NotRequired[bool]

class HealthCheckConfigTypeDef(TypedDict):
    enabled: NotRequired[bool]
    healthCheckIntervalSeconds: NotRequired[int]
    healthCheckTimeoutSeconds: NotRequired[int]
    healthyThresholdCount: NotRequired[int]
    matcher: NotRequired[MatcherTypeDef]
    path: NotRequired[str]
    port: NotRequired[int]
    protocol: NotRequired[TargetGroupProtocolType]
    protocolVersion: NotRequired[HealthCheckProtocolVersionType]
    unhealthyThresholdCount: NotRequired[int]

class ResourceConfigurationDefinitionTypeDef(TypedDict):
    arnResource: NotRequired[ArnResourceTypeDef]
    dnsResource: NotRequired[DnsResourceTypeDef]
    ipResource: NotRequired[IpResourceTypeDef]

class ListAccessLogSubscriptionsRequestPaginateTypeDef(TypedDict):
    resourceIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListListenersRequestPaginateTypeDef(TypedDict):
    serviceIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceConfigurationsRequestPaginateTypeDef(TypedDict):
    resourceConfigurationGroupIdentifier: NotRequired[str]
    resourceGatewayIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceEndpointAssociationsRequestPaginateTypeDef(TypedDict):
    resourceConfigurationIdentifier: str
    resourceEndpointAssociationIdentifier: NotRequired[str]
    vpcEndpointId: NotRequired[str]
    vpcEndpointOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceGatewaysRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRulesRequestPaginateTypeDef(TypedDict):
    listenerIdentifier: str
    serviceIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceNetworkResourceAssociationsRequestPaginateTypeDef(TypedDict):
    resourceConfigurationIdentifier: NotRequired[str]
    serviceNetworkIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceNetworkServiceAssociationsRequestPaginateTypeDef(TypedDict):
    serviceIdentifier: NotRequired[str]
    serviceNetworkIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceNetworkVpcAssociationsRequestPaginateTypeDef(TypedDict):
    serviceNetworkIdentifier: NotRequired[str]
    vpcIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceNetworkVpcEndpointAssociationsRequestPaginateTypeDef(TypedDict):
    serviceNetworkIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceNetworksRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServicesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTargetGroupsRequestPaginateTypeDef(TypedDict):
    targetGroupType: NotRequired[TargetGroupTypeType]
    vpcIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTargetsRequestPaginateTypeDef(TypedDict):
    targetGroupIdentifier: str
    targets: NotRequired[Sequence[TargetTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListListenersResponseTypeDef(TypedDict):
    items: List[ListenerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResourceConfigurationsResponseTypeDef(TypedDict):
    items: List[ResourceConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResourceEndpointAssociationsResponseTypeDef(TypedDict):
    items: List[ResourceEndpointAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListResourceGatewaysResponseTypeDef(TypedDict):
    items: List[ResourceGatewaySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRulesResponseTypeDef(TypedDict):
    items: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceNetworkVpcAssociationsResponseTypeDef(TypedDict):
    items: List[ServiceNetworkVpcAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceNetworkVpcEndpointAssociationsResponseTypeDef(TypedDict):
    items: List[ServiceNetworkEndpointAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceNetworksResponseTypeDef(TypedDict):
    items: List[ServiceNetworkSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTargetGroupsResponseTypeDef(TypedDict):
    items: List[TargetGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTargetsResponseTypeDef(TypedDict):
    items: List[TargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PathMatchTypeDef(TypedDict):
    match: PathMatchTypeTypeDef
    caseSensitive: NotRequired[bool]

class ListServiceNetworkResourceAssociationsResponseTypeDef(TypedDict):
    items: List[ServiceNetworkResourceAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServiceNetworkServiceAssociationsResponseTypeDef(TypedDict):
    items: List[ServiceNetworkServiceAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListServicesResponseTypeDef(TypedDict):
    items: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RuleActionOutputTypeDef(TypedDict):
    fixedResponse: NotRequired[FixedResponseActionTypeDef]
    forward: NotRequired[ForwardActionOutputTypeDef]

ForwardActionUnionTypeDef = Union[ForwardActionTypeDef, ForwardActionOutputTypeDef]

class TargetGroupConfigTypeDef(TypedDict):
    healthCheck: NotRequired[HealthCheckConfigTypeDef]
    ipAddressType: NotRequired[IpAddressTypeType]
    lambdaEventStructureVersion: NotRequired[LambdaEventStructureVersionType]
    port: NotRequired[int]
    protocol: NotRequired[TargetGroupProtocolType]
    protocolVersion: NotRequired[TargetGroupProtocolVersionType]
    vpcIdentifier: NotRequired[str]

class UpdateTargetGroupRequestTypeDef(TypedDict):
    healthCheck: HealthCheckConfigTypeDef
    targetGroupIdentifier: str

CreateResourceConfigurationRequestTypeDef = TypedDict(
    "CreateResourceConfigurationRequestTypeDef",
    {
        "name": str,
        "type": ResourceConfigurationTypeType,
        "allowAssociationToShareableServiceNetwork": NotRequired[bool],
        "clientToken": NotRequired[str],
        "portRanges": NotRequired[Sequence[str]],
        "protocol": NotRequired[Literal["TCP"]],
        "resourceConfigurationDefinition": NotRequired[ResourceConfigurationDefinitionTypeDef],
        "resourceConfigurationGroupIdentifier": NotRequired[str],
        "resourceGatewayIdentifier": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateResourceConfigurationResponseTypeDef = TypedDict(
    "CreateResourceConfigurationResponseTypeDef",
    {
        "allowAssociationToShareableServiceNetwork": bool,
        "arn": str,
        "createdAt": datetime,
        "failureReason": str,
        "id": str,
        "name": str,
        "portRanges": List[str],
        "protocol": Literal["TCP"],
        "resourceConfigurationDefinition": ResourceConfigurationDefinitionTypeDef,
        "resourceConfigurationGroupId": str,
        "resourceGatewayId": str,
        "status": ResourceConfigurationStatusType,
        "type": ResourceConfigurationTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceConfigurationResponseTypeDef = TypedDict(
    "GetResourceConfigurationResponseTypeDef",
    {
        "allowAssociationToShareableServiceNetwork": bool,
        "amazonManaged": bool,
        "arn": str,
        "createdAt": datetime,
        "customDomainName": str,
        "failureReason": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "portRanges": List[str],
        "protocol": Literal["TCP"],
        "resourceConfigurationDefinition": ResourceConfigurationDefinitionTypeDef,
        "resourceConfigurationGroupId": str,
        "resourceGatewayId": str,
        "status": ResourceConfigurationStatusType,
        "type": ResourceConfigurationTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateResourceConfigurationRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str
    allowAssociationToShareableServiceNetwork: NotRequired[bool]
    portRanges: NotRequired[Sequence[str]]
    resourceConfigurationDefinition: NotRequired[ResourceConfigurationDefinitionTypeDef]

UpdateResourceConfigurationResponseTypeDef = TypedDict(
    "UpdateResourceConfigurationResponseTypeDef",
    {
        "allowAssociationToShareableServiceNetwork": bool,
        "arn": str,
        "id": str,
        "name": str,
        "portRanges": List[str],
        "protocol": Literal["TCP"],
        "resourceConfigurationDefinition": ResourceConfigurationDefinitionTypeDef,
        "resourceConfigurationGroupId": str,
        "resourceGatewayId": str,
        "status": ResourceConfigurationStatusType,
        "type": ResourceConfigurationTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class HttpMatchOutputTypeDef(TypedDict):
    headerMatches: NotRequired[List[HeaderMatchTypeDef]]
    method: NotRequired[str]
    pathMatch: NotRequired[PathMatchTypeDef]

class HttpMatchTypeDef(TypedDict):
    headerMatches: NotRequired[Sequence[HeaderMatchTypeDef]]
    method: NotRequired[str]
    pathMatch: NotRequired[PathMatchTypeDef]

CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef",
    {
        "arn": str,
        "defaultAction": RuleActionOutputTypeDef,
        "id": str,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetListenerResponseTypeDef = TypedDict(
    "GetListenerResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "defaultAction": RuleActionOutputTypeDef,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef",
    {
        "arn": str,
        "defaultAction": RuleActionOutputTypeDef,
        "id": str,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class RuleActionTypeDef(TypedDict):
    fixedResponse: NotRequired[FixedResponseActionTypeDef]
    forward: NotRequired[ForwardActionUnionTypeDef]

CreateTargetGroupRequestTypeDef = TypedDict(
    "CreateTargetGroupRequestTypeDef",
    {
        "name": str,
        "type": TargetGroupTypeType,
        "clientToken": NotRequired[str],
        "config": NotRequired[TargetGroupConfigTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateTargetGroupResponseTypeDef = TypedDict(
    "CreateTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": TargetGroupConfigTypeDef,
        "id": str,
        "name": str,
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTargetGroupResponseTypeDef = TypedDict(
    "GetTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": TargetGroupConfigTypeDef,
        "createdAt": datetime,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "serviceArns": List[str],
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTargetGroupResponseTypeDef = TypedDict(
    "UpdateTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": TargetGroupConfigTypeDef,
        "id": str,
        "name": str,
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class RuleMatchOutputTypeDef(TypedDict):
    httpMatch: NotRequired[HttpMatchOutputTypeDef]

HttpMatchUnionTypeDef = Union[HttpMatchTypeDef, HttpMatchOutputTypeDef]
RuleActionUnionTypeDef = Union[RuleActionTypeDef, RuleActionOutputTypeDef]
CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "action": RuleActionOutputTypeDef,
        "arn": str,
        "id": str,
        "match": RuleMatchOutputTypeDef,
        "name": str,
        "priority": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "action": RuleActionOutputTypeDef,
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "isDefault": bool,
        "lastUpdatedAt": datetime,
        "match": RuleMatchOutputTypeDef,
        "name": str,
        "priority": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleUpdateSuccessTypeDef = TypedDict(
    "RuleUpdateSuccessTypeDef",
    {
        "action": NotRequired[RuleActionOutputTypeDef],
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "isDefault": NotRequired[bool],
        "match": NotRequired[RuleMatchOutputTypeDef],
        "name": NotRequired[str],
        "priority": NotRequired[int],
    },
)
UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "action": RuleActionOutputTypeDef,
        "arn": str,
        "id": str,
        "isDefault": bool,
        "match": RuleMatchOutputTypeDef,
        "name": str,
        "priority": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class RuleMatchTypeDef(TypedDict):
    httpMatch: NotRequired[HttpMatchUnionTypeDef]

class CreateListenerRequestTypeDef(TypedDict):
    defaultAction: RuleActionUnionTypeDef
    name: str
    protocol: ListenerProtocolType
    serviceIdentifier: str
    clientToken: NotRequired[str]
    port: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]

class UpdateListenerRequestTypeDef(TypedDict):
    defaultAction: RuleActionUnionTypeDef
    listenerIdentifier: str
    serviceIdentifier: str

class BatchUpdateRuleResponseTypeDef(TypedDict):
    successful: List[RuleUpdateSuccessTypeDef]
    unsuccessful: List[RuleUpdateFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

RuleMatchUnionTypeDef = Union[RuleMatchTypeDef, RuleMatchOutputTypeDef]

class CreateRuleRequestTypeDef(TypedDict):
    action: RuleActionUnionTypeDef
    listenerIdentifier: str
    match: RuleMatchUnionTypeDef
    name: str
    priority: int
    serviceIdentifier: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class RuleUpdateTypeDef(TypedDict):
    ruleIdentifier: str
    action: NotRequired[RuleActionUnionTypeDef]
    match: NotRequired[RuleMatchUnionTypeDef]
    priority: NotRequired[int]

class UpdateRuleRequestTypeDef(TypedDict):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str
    action: NotRequired[RuleActionUnionTypeDef]
    match: NotRequired[RuleMatchUnionTypeDef]
    priority: NotRequired[int]

class BatchUpdateRuleRequestTypeDef(TypedDict):
    listenerIdentifier: str
    rules: Sequence[RuleUpdateTypeDef]
    serviceIdentifier: str
