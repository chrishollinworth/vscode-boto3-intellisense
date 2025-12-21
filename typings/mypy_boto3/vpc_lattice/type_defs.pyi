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
    PrivateDnsPreferenceType,
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
    VerificationStatusType,
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
    "DeleteDomainVerificationRequestTypeDef",
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
    "DnsOptionsOutputTypeDef",
    "DnsOptionsTypeDef",
    "DnsOptionsUnionTypeDef",
    "DnsResourceTypeDef",
    "DomainVerificationSummaryTypeDef",
    "FixedResponseActionTypeDef",
    "ForwardActionOutputTypeDef",
    "ForwardActionTypeDef",
    "ForwardActionUnionTypeDef",
    "GetAccessLogSubscriptionRequestTypeDef",
    "GetAccessLogSubscriptionResponseTypeDef",
    "GetAuthPolicyRequestTypeDef",
    "GetAuthPolicyResponseTypeDef",
    "GetDomainVerificationRequestTypeDef",
    "GetDomainVerificationResponseTypeDef",
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
    "ListDomainVerificationsRequestPaginateTypeDef",
    "ListDomainVerificationsRequestTypeDef",
    "ListDomainVerificationsResponseTypeDef",
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
    "StartDomainVerificationRequestTypeDef",
    "StartDomainVerificationResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TargetFailureTypeDef",
    "TargetGroupConfigTypeDef",
    "TargetGroupSummaryTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "TxtMethodConfigTypeDef",
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
        "id": str,
        "arn": str,
        "resourceId": str,
        "resourceArn": str,
        "destinationArn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
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
    ruleIdentifier: NotRequired[str]
    failureCode: NotRequired[str]
    failureMessage: NotRequired[str]

class CreateAccessLogSubscriptionRequestTypeDef(TypedDict):
    resourceIdentifier: str
    destinationArn: str
    clientToken: NotRequired[str]
    serviceNetworkLogType: NotRequired[ServiceNetworkLogTypeType]
    tags: NotRequired[Mapping[str, str]]

class CreateResourceGatewayRequestTypeDef(TypedDict):
    name: str
    clientToken: NotRequired[str]
    vpcIdentifier: NotRequired[str]
    subnetIds: NotRequired[Sequence[str]]
    securityGroupIds: NotRequired[Sequence[str]]
    ipAddressType: NotRequired[ResourceGatewayIpAddressTypeType]
    ipv4AddressesPerEni: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]

class SharingConfigTypeDef(TypedDict):
    enabled: NotRequired[bool]

class CreateServiceNetworkResourceAssociationRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: NotRequired[str]
    privateDnsEnabled: NotRequired[bool]
    tags: NotRequired[Mapping[str, str]]

class CreateServiceNetworkServiceAssociationRequestTypeDef(TypedDict):
    serviceIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class DnsEntryTypeDef(TypedDict):
    domainName: NotRequired[str]
    hostedZoneId: NotRequired[str]

class DnsOptionsOutputTypeDef(TypedDict):
    privateDnsPreference: NotRequired[PrivateDnsPreferenceType]
    privateDnsSpecifiedDomains: NotRequired[List[str]]

class CreateServiceRequestTypeDef(TypedDict):
    name: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    customDomainName: NotRequired[str]
    certificateArn: NotRequired[str]
    authType: NotRequired[AuthTypeType]

class DeleteAccessLogSubscriptionRequestTypeDef(TypedDict):
    accessLogSubscriptionIdentifier: str

class DeleteAuthPolicyRequestTypeDef(TypedDict):
    resourceIdentifier: str

class DeleteDomainVerificationRequestTypeDef(TypedDict):
    domainVerificationIdentifier: str

class DeleteListenerRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str

class DeleteResourceConfigurationRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str

class DeleteResourceEndpointAssociationRequestTypeDef(TypedDict):
    resourceEndpointAssociationIdentifier: str

class DeleteResourceGatewayRequestTypeDef(TypedDict):
    resourceGatewayIdentifier: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class DeleteRuleRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str
    ruleIdentifier: str

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
        "id": NotRequired[str],
        "port": NotRequired[int],
        "failureCode": NotRequired[str],
        "failureMessage": NotRequired[str],
    },
)

class DnsOptionsTypeDef(TypedDict):
    privateDnsPreference: NotRequired[PrivateDnsPreferenceType]
    privateDnsSpecifiedDomains: NotRequired[Sequence[str]]

class DnsResourceTypeDef(TypedDict):
    domainName: NotRequired[str]
    ipAddressType: NotRequired[ResourceConfigurationIpAddressTypeType]

class TxtMethodConfigTypeDef(TypedDict):
    value: str
    name: str

class FixedResponseActionTypeDef(TypedDict):
    statusCode: int

class WeightedTargetGroupTypeDef(TypedDict):
    targetGroupIdentifier: str
    weight: NotRequired[int]

class GetAccessLogSubscriptionRequestTypeDef(TypedDict):
    accessLogSubscriptionIdentifier: str

class GetAuthPolicyRequestTypeDef(TypedDict):
    resourceIdentifier: str

class GetDomainVerificationRequestTypeDef(TypedDict):
    domainVerificationIdentifier: str

class GetListenerRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str

class GetResourceConfigurationRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str

class GetResourceGatewayRequestTypeDef(TypedDict):
    resourceGatewayIdentifier: str

class GetResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str

class GetRuleRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str
    ruleIdentifier: str

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
    exact: NotRequired[str]
    prefix: NotRequired[str]
    contains: NotRequired[str]

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

class ListDomainVerificationsRequestTypeDef(TypedDict):
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
        "id": NotRequired[str],
        "name": NotRequired[str],
        "protocol": NotRequired[ListenerProtocolType],
        "port": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

class ListResourceConfigurationsRequestTypeDef(TypedDict):
    resourceGatewayIdentifier: NotRequired[str]
    resourceConfigurationGroupIdentifier: NotRequired[str]
    domainVerificationIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ResourceConfigurationSummaryTypeDef = TypedDict(
    "ResourceConfigurationSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "resourceGatewayId": NotRequired[str],
        "resourceConfigurationGroupId": NotRequired[str],
        "type": NotRequired[ResourceConfigurationTypeType],
        "status": NotRequired[ResourceConfigurationStatusType],
        "amazonManaged": NotRequired[bool],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "customDomainName": NotRequired[str],
        "domainVerificationId": NotRequired[str],
        "groupDomain": NotRequired[str],
    },
)

class ListResourceEndpointAssociationsRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str
    resourceEndpointAssociationIdentifier: NotRequired[str]
    vpcEndpointId: NotRequired[str]
    vpcEndpointOwner: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ResourceEndpointAssociationSummaryTypeDef = TypedDict(
    "ResourceEndpointAssociationSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "resourceConfigurationId": NotRequired[str],
        "resourceConfigurationArn": NotRequired[str],
        "resourceConfigurationName": NotRequired[str],
        "vpcEndpointId": NotRequired[str],
        "vpcEndpointOwner": NotRequired[str],
        "createdBy": NotRequired[str],
        "createdAt": NotRequired[datetime],
    },
)

class ListResourceGatewaysRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ResourceGatewaySummaryTypeDef = TypedDict(
    "ResourceGatewaySummaryTypeDef",
    {
        "name": NotRequired[str],
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[ResourceGatewayStatusType],
        "vpcIdentifier": NotRequired[str],
        "subnetIds": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
        "ipAddressType": NotRequired[ResourceGatewayIpAddressTypeType],
        "ipv4AddressesPerEni": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

class ListRulesRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "isDefault": NotRequired[bool],
        "priority": NotRequired[int],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
    },
)

class ListServiceNetworkResourceAssociationsRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: NotRequired[str]
    resourceConfigurationIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    includeChildren: NotRequired[bool]

class ListServiceNetworkServiceAssociationsRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: NotRequired[str]
    serviceIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListServiceNetworkVpcAssociationsRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: NotRequired[str]
    vpcIdentifier: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListServiceNetworkVpcEndpointAssociationsRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ServiceNetworkEndpointAssociationTypeDef = TypedDict(
    "ServiceNetworkEndpointAssociationTypeDef",
    {
        "vpcEndpointId": NotRequired[str],
        "vpcId": NotRequired[str],
        "vpcEndpointOwnerId": NotRequired[str],
        "id": NotRequired[str],
        "state": NotRequired[str],
        "serviceNetworkArn": NotRequired[str],
        "createdAt": NotRequired[datetime],
    },
)

class ListServiceNetworksRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

ServiceNetworkSummaryTypeDef = TypedDict(
    "ServiceNetworkSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "numberOfAssociatedVPCs": NotRequired[int],
        "numberOfAssociatedServices": NotRequired[int],
        "numberOfAssociatedResourceConfigurations": NotRequired[int],
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
    vpcIdentifier: NotRequired[str]
    targetGroupType: NotRequired[TargetGroupTypeType]

TargetGroupSummaryTypeDef = TypedDict(
    "TargetGroupSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[TargetGroupTypeType],
        "createdAt": NotRequired[datetime],
        "port": NotRequired[int],
        "protocol": NotRequired[TargetGroupProtocolType],
        "ipAddressType": NotRequired[IpAddressTypeType],
        "vpcIdentifier": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
        "status": NotRequired[TargetGroupStatusType],
        "serviceArns": NotRequired[List[str]],
        "lambdaEventStructureVersion": NotRequired[LambdaEventStructureVersionType],
    },
)
TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "id": NotRequired[str],
        "port": NotRequired[int],
        "status": NotRequired[TargetStatusType],
        "reasonCode": NotRequired[str],
    },
)

class PathMatchTypeTypeDef(TypedDict):
    exact: NotRequired[str]
    prefix: NotRequired[str]

class PutAuthPolicyRequestTypeDef(TypedDict):
    resourceIdentifier: str
    policy: str

class PutResourcePolicyRequestTypeDef(TypedDict):
    resourceArn: str
    policy: str

class StartDomainVerificationRequestTypeDef(TypedDict):
    domainName: str
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

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
    serviceNetworkIdentifier: str
    authType: AuthTypeType

class UpdateServiceNetworkVpcAssociationRequestTypeDef(TypedDict):
    serviceNetworkVpcAssociationIdentifier: str
    securityGroupIds: Sequence[str]

class UpdateServiceRequestTypeDef(TypedDict):
    serviceIdentifier: str
    certificateArn: NotRequired[str]
    authType: NotRequired[AuthTypeType]

CreateAccessLogSubscriptionResponseTypeDef = TypedDict(
    "CreateAccessLogSubscriptionResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "resourceId": str,
        "resourceArn": str,
        "serviceNetworkLogType": ServiceNetworkLogTypeType,
        "destinationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateResourceGatewayResponseTypeDef = TypedDict(
    "CreateResourceGatewayResponseTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "status": ResourceGatewayStatusType,
        "vpcIdentifier": str,
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "ipAddressType": ResourceGatewayIpAddressTypeType,
        "ipv4AddressesPerEni": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceNetworkResourceAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkResourceAssociationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": ServiceNetworkResourceAssociationStatusType,
        "createdBy": str,
        "privateDnsEnabled": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResourceEndpointAssociationResponseTypeDef = TypedDict(
    "DeleteResourceEndpointAssociationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "resourceConfigurationId": str,
        "resourceConfigurationArn": str,
        "vpcEndpointId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteResourceGatewayResponseTypeDef = TypedDict(
    "DeleteResourceGatewayResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "status": ResourceGatewayStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceNetworkResourceAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkResourceAssociationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": ServiceNetworkResourceAssociationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkServiceAssociationResponseTypeDef",
    {
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkVpcAssociationResponseTypeDef",
    {
        "id": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteTargetGroupResponseTypeDef = TypedDict(
    "DeleteTargetGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": TargetGroupStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessLogSubscriptionResponseTypeDef = TypedDict(
    "GetAccessLogSubscriptionResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "resourceId": str,
        "resourceArn": str,
        "destinationArn": str,
        "serviceNetworkLogType": ServiceNetworkLogTypeType,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetAuthPolicyResponseTypeDef(TypedDict):
    policy: str
    state: AuthPolicyStateType
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

GetResourceGatewayResponseTypeDef = TypedDict(
    "GetResourceGatewayResponseTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "status": ResourceGatewayStatusType,
        "vpcId": str,
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "ipAddressType": ResourceGatewayIpAddressTypeType,
        "ipv4AddressesPerEni": int,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetResourcePolicyResponseTypeDef(TypedDict):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

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
        "id": str,
        "arn": str,
        "resourceId": str,
        "resourceArn": str,
        "destinationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateResourceGatewayResponseTypeDef = TypedDict(
    "UpdateResourceGatewayResponseTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "status": ResourceGatewayStatusType,
        "vpcId": str,
        "subnetIds": List[str],
        "securityGroupIds": List[str],
        "ipAddressType": IpAddressTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceNetworkResponseTypeDef = TypedDict(
    "UpdateServiceNetworkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "authType": AuthTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "UpdateServiceNetworkVpcAssociationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "createdBy": str,
        "securityGroupIds": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "customDomainName": str,
        "certificateArn": str,
        "authType": AuthTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateServiceNetworkRequestTypeDef(TypedDict):
    name: str
    clientToken: NotRequired[str]
    authType: NotRequired[AuthTypeType]
    tags: NotRequired[Mapping[str, str]]
    sharingConfig: NotRequired[SharingConfigTypeDef]

CreateServiceNetworkResponseTypeDef = TypedDict(
    "CreateServiceNetworkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "sharingConfig": SharingConfigTypeDef,
        "authType": AuthTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkResponseTypeDef = TypedDict(
    "GetServiceNetworkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "arn": str,
        "authType": AuthTypeType,
        "sharingConfig": SharingConfigTypeDef,
        "numberOfAssociatedVPCs": int,
        "numberOfAssociatedServices": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkServiceAssociationResponseTypeDef",
    {
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "arn": str,
        "createdBy": str,
        "customDomainName": str,
        "dnsEntry": DnsEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "customDomainName": str,
        "certificateArn": str,
        "status": ServiceStatusType,
        "authType": AuthTypeType,
        "dnsEntry": DnsEntryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkResourceAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkResourceAssociationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "status": ServiceNetworkResourceAssociationStatusType,
        "createdBy": str,
        "createdAt": datetime,
        "resourceConfigurationId": str,
        "resourceConfigurationArn": str,
        "resourceConfigurationName": str,
        "serviceNetworkId": str,
        "serviceNetworkArn": str,
        "serviceNetworkName": str,
        "failureReason": str,
        "failureCode": str,
        "lastUpdatedAt": datetime,
        "privateDnsEntry": DnsEntryTypeDef,
        "privateDnsEnabled": bool,
        "dnsEntry": DnsEntryTypeDef,
        "isManagedAssociation": bool,
        "domainVerificationStatus": VerificationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkServiceAssociationResponseTypeDef",
    {
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "serviceId": str,
        "serviceName": str,
        "serviceArn": str,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "serviceNetworkArn": str,
        "dnsEntry": DnsEntryTypeDef,
        "customDomainName": str,
        "failureMessage": str,
        "failureCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceResponseTypeDef = TypedDict(
    "GetServiceResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "dnsEntry": DnsEntryTypeDef,
        "customDomainName": str,
        "certificateArn": str,
        "status": ServiceStatusType,
        "authType": AuthTypeType,
        "failureCode": str,
        "failureMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceNetworkResourceAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkResourceAssociationSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[ServiceNetworkResourceAssociationStatusType],
        "createdBy": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "resourceConfigurationId": NotRequired[str],
        "resourceConfigurationArn": NotRequired[str],
        "resourceConfigurationName": NotRequired[str],
        "serviceNetworkId": NotRequired[str],
        "serviceNetworkArn": NotRequired[str],
        "serviceNetworkName": NotRequired[str],
        "dnsEntry": NotRequired[DnsEntryTypeDef],
        "privateDnsEntry": NotRequired[DnsEntryTypeDef],
        "isManagedAssociation": NotRequired[bool],
        "failureCode": NotRequired[str],
        "privateDnsEnabled": NotRequired[bool],
    },
)
ServiceNetworkServiceAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkServiceAssociationSummaryTypeDef",
    {
        "id": NotRequired[str],
        "status": NotRequired[ServiceNetworkServiceAssociationStatusType],
        "arn": NotRequired[str],
        "createdBy": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "serviceId": NotRequired[str],
        "serviceName": NotRequired[str],
        "serviceArn": NotRequired[str],
        "serviceNetworkId": NotRequired[str],
        "serviceNetworkName": NotRequired[str],
        "serviceNetworkArn": NotRequired[str],
        "dnsEntry": NotRequired[DnsEntryTypeDef],
        "customDomainName": NotRequired[str],
    },
)
ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "lastUpdatedAt": NotRequired[datetime],
        "dnsEntry": NotRequired[DnsEntryTypeDef],
        "customDomainName": NotRequired[str],
        "status": NotRequired[ServiceStatusType],
    },
)
CreateServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkVpcAssociationResponseTypeDef",
    {
        "id": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "arn": str,
        "createdBy": str,
        "securityGroupIds": List[str],
        "privateDnsEnabled": bool,
        "dnsOptions": DnsOptionsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkVpcAssociationResponseTypeDef",
    {
        "id": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "arn": str,
        "createdBy": str,
        "createdAt": datetime,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "serviceNetworkArn": str,
        "vpcId": str,
        "securityGroupIds": List[str],
        "privateDnsEnabled": bool,
        "failureMessage": str,
        "failureCode": str,
        "lastUpdatedAt": datetime,
        "dnsOptions": DnsOptionsOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceNetworkVpcAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkVpcAssociationSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[ServiceNetworkVpcAssociationStatusType],
        "createdBy": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "serviceNetworkId": NotRequired[str],
        "serviceNetworkName": NotRequired[str],
        "serviceNetworkArn": NotRequired[str],
        "privateDnsEnabled": NotRequired[bool],
        "dnsOptions": NotRequired[DnsOptionsOutputTypeDef],
        "vpcId": NotRequired[str],
        "lastUpdatedAt": NotRequired[datetime],
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

DnsOptionsUnionTypeDef = Union[DnsOptionsTypeDef, DnsOptionsOutputTypeDef]
DomainVerificationSummaryTypeDef = TypedDict(
    "DomainVerificationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "domainName": str,
        "status": VerificationStatusType,
        "createdAt": datetime,
        "txtMethodConfig": NotRequired[TxtMethodConfigTypeDef],
        "lastVerifiedTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
GetDomainVerificationResponseTypeDef = TypedDict(
    "GetDomainVerificationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "domainName": str,
        "status": VerificationStatusType,
        "txtMethodConfig": TxtMethodConfigTypeDef,
        "createdAt": datetime,
        "lastVerifiedTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDomainVerificationResponseTypeDef = TypedDict(
    "StartDomainVerificationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "domainName": str,
        "status": VerificationStatusType,
        "txtMethodConfig": TxtMethodConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ForwardActionOutputTypeDef(TypedDict):
    targetGroups: List[WeightedTargetGroupTypeDef]

class ForwardActionTypeDef(TypedDict):
    targetGroups: Sequence[WeightedTargetGroupTypeDef]

class HeaderMatchTypeDef(TypedDict):
    name: str
    match: HeaderMatchTypeTypeDef
    caseSensitive: NotRequired[bool]

class HealthCheckConfigTypeDef(TypedDict):
    enabled: NotRequired[bool]
    protocol: NotRequired[TargetGroupProtocolType]
    protocolVersion: NotRequired[HealthCheckProtocolVersionType]
    port: NotRequired[int]
    path: NotRequired[str]
    healthCheckIntervalSeconds: NotRequired[int]
    healthCheckTimeoutSeconds: NotRequired[int]
    healthyThresholdCount: NotRequired[int]
    unhealthyThresholdCount: NotRequired[int]
    matcher: NotRequired[MatcherTypeDef]

class ResourceConfigurationDefinitionTypeDef(TypedDict):
    dnsResource: NotRequired[DnsResourceTypeDef]
    ipResource: NotRequired[IpResourceTypeDef]
    arnResource: NotRequired[ArnResourceTypeDef]

class ListAccessLogSubscriptionsRequestPaginateTypeDef(TypedDict):
    resourceIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainVerificationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListListenersRequestPaginateTypeDef(TypedDict):
    serviceIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceConfigurationsRequestPaginateTypeDef(TypedDict):
    resourceGatewayIdentifier: NotRequired[str]
    resourceConfigurationGroupIdentifier: NotRequired[str]
    domainVerificationIdentifier: NotRequired[str]
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
    serviceIdentifier: str
    listenerIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceNetworkResourceAssociationsRequestPaginateTypeDef(TypedDict):
    serviceNetworkIdentifier: NotRequired[str]
    resourceConfigurationIdentifier: NotRequired[str]
    includeChildren: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListServiceNetworkServiceAssociationsRequestPaginateTypeDef(TypedDict):
    serviceNetworkIdentifier: NotRequired[str]
    serviceIdentifier: NotRequired[str]
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
    vpcIdentifier: NotRequired[str]
    targetGroupType: NotRequired[TargetGroupTypeType]
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

class ListServiceNetworkVpcAssociationsResponseTypeDef(TypedDict):
    items: List[ServiceNetworkVpcAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreateServiceNetworkVpcAssociationRequestTypeDef(TypedDict):
    serviceNetworkIdentifier: str
    vpcIdentifier: str
    clientToken: NotRequired[str]
    privateDnsEnabled: NotRequired[bool]
    securityGroupIds: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]
    dnsOptions: NotRequired[DnsOptionsUnionTypeDef]

class ListDomainVerificationsResponseTypeDef(TypedDict):
    items: List[DomainVerificationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RuleActionOutputTypeDef(TypedDict):
    forward: NotRequired[ForwardActionOutputTypeDef]
    fixedResponse: NotRequired[FixedResponseActionTypeDef]

ForwardActionUnionTypeDef = Union[ForwardActionTypeDef, ForwardActionOutputTypeDef]

class TargetGroupConfigTypeDef(TypedDict):
    port: NotRequired[int]
    protocol: NotRequired[TargetGroupProtocolType]
    protocolVersion: NotRequired[TargetGroupProtocolVersionType]
    ipAddressType: NotRequired[IpAddressTypeType]
    vpcIdentifier: NotRequired[str]
    healthCheck: NotRequired[HealthCheckConfigTypeDef]
    lambdaEventStructureVersion: NotRequired[LambdaEventStructureVersionType]

class UpdateTargetGroupRequestTypeDef(TypedDict):
    targetGroupIdentifier: str
    healthCheck: HealthCheckConfigTypeDef

CreateResourceConfigurationRequestTypeDef = TypedDict(
    "CreateResourceConfigurationRequestTypeDef",
    {
        "name": str,
        "type": ResourceConfigurationTypeType,
        "portRanges": NotRequired[Sequence[str]],
        "protocol": NotRequired[Literal["TCP"]],
        "resourceGatewayIdentifier": NotRequired[str],
        "resourceConfigurationGroupIdentifier": NotRequired[str],
        "resourceConfigurationDefinition": NotRequired[ResourceConfigurationDefinitionTypeDef],
        "allowAssociationToShareableServiceNetwork": NotRequired[bool],
        "customDomainName": NotRequired[str],
        "groupDomain": NotRequired[str],
        "domainVerificationIdentifier": NotRequired[str],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateResourceConfigurationResponseTypeDef = TypedDict(
    "CreateResourceConfigurationResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "resourceGatewayId": str,
        "resourceConfigurationGroupId": str,
        "type": ResourceConfigurationTypeType,
        "portRanges": List[str],
        "protocol": Literal["TCP"],
        "status": ResourceConfigurationStatusType,
        "resourceConfigurationDefinition": ResourceConfigurationDefinitionTypeDef,
        "allowAssociationToShareableServiceNetwork": bool,
        "createdAt": datetime,
        "failureReason": str,
        "customDomainName": str,
        "domainVerificationId": str,
        "groupDomain": str,
        "domainVerificationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourceConfigurationResponseTypeDef = TypedDict(
    "GetResourceConfigurationResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "resourceGatewayId": str,
        "resourceConfigurationGroupId": str,
        "type": ResourceConfigurationTypeType,
        "allowAssociationToShareableServiceNetwork": bool,
        "portRanges": List[str],
        "protocol": Literal["TCP"],
        "customDomainName": str,
        "status": ResourceConfigurationStatusType,
        "resourceConfigurationDefinition": ResourceConfigurationDefinitionTypeDef,
        "createdAt": datetime,
        "amazonManaged": bool,
        "failureReason": str,
        "lastUpdatedAt": datetime,
        "domainVerificationId": str,
        "domainVerificationArn": str,
        "domainVerificationStatus": VerificationStatusType,
        "groupDomain": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateResourceConfigurationRequestTypeDef(TypedDict):
    resourceConfigurationIdentifier: str
    resourceConfigurationDefinition: NotRequired[ResourceConfigurationDefinitionTypeDef]
    allowAssociationToShareableServiceNetwork: NotRequired[bool]
    portRanges: NotRequired[Sequence[str]]

UpdateResourceConfigurationResponseTypeDef = TypedDict(
    "UpdateResourceConfigurationResponseTypeDef",
    {
        "id": str,
        "name": str,
        "arn": str,
        "resourceGatewayId": str,
        "resourceConfigurationGroupId": str,
        "type": ResourceConfigurationTypeType,
        "portRanges": List[str],
        "allowAssociationToShareableServiceNetwork": bool,
        "protocol": Literal["TCP"],
        "status": ResourceConfigurationStatusType,
        "resourceConfigurationDefinition": ResourceConfigurationDefinitionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class HttpMatchOutputTypeDef(TypedDict):
    method: NotRequired[str]
    pathMatch: NotRequired[PathMatchTypeDef]
    headerMatches: NotRequired[List[HeaderMatchTypeDef]]

class HttpMatchTypeDef(TypedDict):
    method: NotRequired[str]
    pathMatch: NotRequired[PathMatchTypeDef]
    headerMatches: NotRequired[Sequence[HeaderMatchTypeDef]]

CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "protocol": ListenerProtocolType,
        "port": int,
        "serviceArn": str,
        "serviceId": str,
        "defaultAction": RuleActionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetListenerResponseTypeDef = TypedDict(
    "GetListenerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "protocol": ListenerProtocolType,
        "port": int,
        "serviceArn": str,
        "serviceId": str,
        "defaultAction": RuleActionOutputTypeDef,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "protocol": ListenerProtocolType,
        "port": int,
        "serviceArn": str,
        "serviceId": str,
        "defaultAction": RuleActionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class RuleActionTypeDef(TypedDict):
    forward: NotRequired[ForwardActionUnionTypeDef]
    fixedResponse: NotRequired[FixedResponseActionTypeDef]

CreateTargetGroupRequestTypeDef = TypedDict(
    "CreateTargetGroupRequestTypeDef",
    {
        "name": str,
        "type": TargetGroupTypeType,
        "config": NotRequired[TargetGroupConfigTypeDef],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateTargetGroupResponseTypeDef = TypedDict(
    "CreateTargetGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "type": TargetGroupTypeType,
        "config": TargetGroupConfigTypeDef,
        "status": TargetGroupStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTargetGroupResponseTypeDef = TypedDict(
    "GetTargetGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "type": TargetGroupTypeType,
        "config": TargetGroupConfigTypeDef,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "status": TargetGroupStatusType,
        "serviceArns": List[str],
        "failureMessage": str,
        "failureCode": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTargetGroupResponseTypeDef = TypedDict(
    "UpdateTargetGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "type": TargetGroupTypeType,
        "config": TargetGroupConfigTypeDef,
        "status": TargetGroupStatusType,
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
        "arn": str,
        "id": str,
        "name": str,
        "match": RuleMatchOutputTypeDef,
        "priority": int,
        "action": RuleActionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "isDefault": bool,
        "match": RuleMatchOutputTypeDef,
        "priority": int,
        "action": RuleActionOutputTypeDef,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RuleUpdateSuccessTypeDef = TypedDict(
    "RuleUpdateSuccessTypeDef",
    {
        "arn": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "isDefault": NotRequired[bool],
        "match": NotRequired[RuleMatchOutputTypeDef],
        "priority": NotRequired[int],
        "action": NotRequired[RuleActionOutputTypeDef],
    },
)
UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "isDefault": bool,
        "match": RuleMatchOutputTypeDef,
        "priority": int,
        "action": RuleActionOutputTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class RuleMatchTypeDef(TypedDict):
    httpMatch: NotRequired[HttpMatchUnionTypeDef]

class CreateListenerRequestTypeDef(TypedDict):
    serviceIdentifier: str
    name: str
    protocol: ListenerProtocolType
    defaultAction: RuleActionUnionTypeDef
    port: NotRequired[int]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class UpdateListenerRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str
    defaultAction: RuleActionUnionTypeDef

class BatchUpdateRuleResponseTypeDef(TypedDict):
    successful: List[RuleUpdateSuccessTypeDef]
    unsuccessful: List[RuleUpdateFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

RuleMatchUnionTypeDef = Union[RuleMatchTypeDef, RuleMatchOutputTypeDef]

class CreateRuleRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str
    name: str
    match: RuleMatchUnionTypeDef
    priority: int
    action: RuleActionUnionTypeDef
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class RuleUpdateTypeDef(TypedDict):
    ruleIdentifier: str
    match: NotRequired[RuleMatchUnionTypeDef]
    priority: NotRequired[int]
    action: NotRequired[RuleActionUnionTypeDef]

class UpdateRuleRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str
    ruleIdentifier: str
    match: NotRequired[RuleMatchUnionTypeDef]
    priority: NotRequired[int]
    action: NotRequired[RuleActionUnionTypeDef]

class BatchUpdateRuleRequestTypeDef(TypedDict):
    serviceIdentifier: str
    listenerIdentifier: str
    rules: Sequence[RuleUpdateTypeDef]
