"""
Type annotations for vpc-lattice service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_vpc_lattice/type_defs.html)

Usage::

    ```python
    from mypy_boto3_vpc_lattice.type_defs import AccessLogSubscriptionSummaryTypeDef

    data: AccessLogSubscriptionSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AuthPolicyStateType,
    AuthTypeType,
    HealthCheckProtocolVersionType,
    IpAddressTypeType,
    LambdaEventStructureVersionType,
    ListenerProtocolType,
    ServiceNetworkServiceAssociationStatusType,
    ServiceNetworkVpcAssociationStatusType,
    ServiceStatusType,
    TargetGroupProtocolType,
    TargetGroupProtocolVersionType,
    TargetGroupStatusType,
    TargetGroupTypeType,
    TargetStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccessLogSubscriptionSummaryTypeDef",
    "BatchUpdateRuleRequestRequestTypeDef",
    "BatchUpdateRuleResponseTypeDef",
    "CreateAccessLogSubscriptionRequestRequestTypeDef",
    "CreateAccessLogSubscriptionResponseTypeDef",
    "CreateListenerRequestRequestTypeDef",
    "CreateListenerResponseTypeDef",
    "CreateRuleRequestRequestTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateServiceNetworkRequestRequestTypeDef",
    "CreateServiceNetworkResponseTypeDef",
    "CreateServiceNetworkServiceAssociationRequestRequestTypeDef",
    "CreateServiceNetworkServiceAssociationResponseTypeDef",
    "CreateServiceNetworkVpcAssociationRequestRequestTypeDef",
    "CreateServiceNetworkVpcAssociationResponseTypeDef",
    "CreateServiceRequestRequestTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateTargetGroupRequestRequestTypeDef",
    "CreateTargetGroupResponseTypeDef",
    "DeleteAccessLogSubscriptionRequestRequestTypeDef",
    "DeleteAuthPolicyRequestRequestTypeDef",
    "DeleteListenerRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DeleteServiceNetworkRequestRequestTypeDef",
    "DeleteServiceNetworkServiceAssociationRequestRequestTypeDef",
    "DeleteServiceNetworkServiceAssociationResponseTypeDef",
    "DeleteServiceNetworkVpcAssociationRequestRequestTypeDef",
    "DeleteServiceNetworkVpcAssociationResponseTypeDef",
    "DeleteServiceRequestRequestTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteTargetGroupRequestRequestTypeDef",
    "DeleteTargetGroupResponseTypeDef",
    "DeregisterTargetsRequestRequestTypeDef",
    "DeregisterTargetsResponseTypeDef",
    "DnsEntryTypeDef",
    "FixedResponseActionTypeDef",
    "ForwardActionTypeDef",
    "GetAccessLogSubscriptionRequestRequestTypeDef",
    "GetAccessLogSubscriptionResponseTypeDef",
    "GetAuthPolicyRequestRequestTypeDef",
    "GetAuthPolicyResponseTypeDef",
    "GetListenerRequestRequestTypeDef",
    "GetListenerResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetRuleRequestRequestTypeDef",
    "GetRuleResponseTypeDef",
    "GetServiceNetworkRequestRequestTypeDef",
    "GetServiceNetworkResponseTypeDef",
    "GetServiceNetworkServiceAssociationRequestRequestTypeDef",
    "GetServiceNetworkServiceAssociationResponseTypeDef",
    "GetServiceNetworkVpcAssociationRequestRequestTypeDef",
    "GetServiceNetworkVpcAssociationResponseTypeDef",
    "GetServiceRequestRequestTypeDef",
    "GetServiceResponseTypeDef",
    "GetTargetGroupRequestRequestTypeDef",
    "GetTargetGroupResponseTypeDef",
    "HeaderMatchTypeDef",
    "HeaderMatchTypeTypeDef",
    "HealthCheckConfigTypeDef",
    "HttpMatchTypeDef",
    "ListAccessLogSubscriptionsRequestRequestTypeDef",
    "ListAccessLogSubscriptionsResponseTypeDef",
    "ListListenersRequestRequestTypeDef",
    "ListListenersResponseTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListServiceNetworkServiceAssociationsRequestRequestTypeDef",
    "ListServiceNetworkServiceAssociationsResponseTypeDef",
    "ListServiceNetworkVpcAssociationsRequestRequestTypeDef",
    "ListServiceNetworkVpcAssociationsResponseTypeDef",
    "ListServiceNetworksRequestRequestTypeDef",
    "ListServiceNetworksResponseTypeDef",
    "ListServicesRequestRequestTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetGroupsRequestRequestTypeDef",
    "ListTargetGroupsResponseTypeDef",
    "ListTargetsRequestRequestTypeDef",
    "ListTargetsResponseTypeDef",
    "ListenerSummaryTypeDef",
    "MatcherTypeDef",
    "PaginatorConfigTypeDef",
    "PathMatchTypeDef",
    "PathMatchTypeTypeDef",
    "PutAuthPolicyRequestRequestTypeDef",
    "PutAuthPolicyResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RegisterTargetsRequestRequestTypeDef",
    "RegisterTargetsResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuleActionTypeDef",
    "RuleMatchTypeDef",
    "RuleSummaryTypeDef",
    "RuleUpdateFailureTypeDef",
    "RuleUpdateSuccessTypeDef",
    "RuleUpdateTypeDef",
    "ServiceNetworkServiceAssociationSummaryTypeDef",
    "ServiceNetworkSummaryTypeDef",
    "ServiceNetworkVpcAssociationSummaryTypeDef",
    "ServiceSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TargetFailureTypeDef",
    "TargetGroupConfigTypeDef",
    "TargetGroupSummaryTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccessLogSubscriptionRequestRequestTypeDef",
    "UpdateAccessLogSubscriptionResponseTypeDef",
    "UpdateListenerRequestRequestTypeDef",
    "UpdateListenerResponseTypeDef",
    "UpdateRuleRequestRequestTypeDef",
    "UpdateRuleResponseTypeDef",
    "UpdateServiceNetworkRequestRequestTypeDef",
    "UpdateServiceNetworkResponseTypeDef",
    "UpdateServiceNetworkVpcAssociationRequestRequestTypeDef",
    "UpdateServiceNetworkVpcAssociationResponseTypeDef",
    "UpdateServiceRequestRequestTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateTargetGroupRequestRequestTypeDef",
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
    },
)

BatchUpdateRuleRequestRequestTypeDef = TypedDict(
    "BatchUpdateRuleRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "rules": List["RuleUpdateTypeDef"],
        "serviceIdentifier": str,
    },
)

BatchUpdateRuleResponseTypeDef = TypedDict(
    "BatchUpdateRuleResponseTypeDef",
    {
        "successful": List["RuleUpdateSuccessTypeDef"],
        "unsuccessful": List["RuleUpdateFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAccessLogSubscriptionRequestRequestTypeDef",
    {
        "destinationArn": str,
        "resourceIdentifier": str,
    },
)
_OptionalCreateAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAccessLogSubscriptionRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateAccessLogSubscriptionRequestRequestTypeDef(
    _RequiredCreateAccessLogSubscriptionRequestRequestTypeDef,
    _OptionalCreateAccessLogSubscriptionRequestRequestTypeDef,
):
    pass

CreateAccessLogSubscriptionResponseTypeDef = TypedDict(
    "CreateAccessLogSubscriptionResponseTypeDef",
    {
        "arn": str,
        "destinationArn": str,
        "id": str,
        "resourceArn": str,
        "resourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateListenerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateListenerRequestRequestTypeDef",
    {
        "defaultAction": "RuleActionTypeDef",
        "name": str,
        "protocol": ListenerProtocolType,
        "serviceIdentifier": str,
    },
)
_OptionalCreateListenerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateListenerRequestRequestTypeDef",
    {
        "clientToken": str,
        "port": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateListenerRequestRequestTypeDef(
    _RequiredCreateListenerRequestRequestTypeDef, _OptionalCreateListenerRequestRequestTypeDef
):
    pass

CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef",
    {
        "arn": str,
        "defaultAction": "RuleActionTypeDef",
        "id": str,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRuleRequestRequestTypeDef",
    {
        "action": "RuleActionTypeDef",
        "listenerIdentifier": str,
        "match": "RuleMatchTypeDef",
        "name": str,
        "priority": int,
        "serviceIdentifier": str,
    },
)
_OptionalCreateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRuleRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateRuleRequestRequestTypeDef(
    _RequiredCreateRuleRequestRequestTypeDef, _OptionalCreateRuleRequestRequestTypeDef
):
    pass

CreateRuleResponseTypeDef = TypedDict(
    "CreateRuleResponseTypeDef",
    {
        "action": "RuleActionTypeDef",
        "arn": str,
        "id": str,
        "match": "RuleMatchTypeDef",
        "name": str,
        "priority": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceNetworkRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateServiceNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceNetworkRequestRequestTypeDef",
    {
        "authType": AuthTypeType,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateServiceNetworkRequestRequestTypeDef(
    _RequiredCreateServiceNetworkRequestRequestTypeDef,
    _OptionalCreateServiceNetworkRequestRequestTypeDef,
):
    pass

CreateServiceNetworkResponseTypeDef = TypedDict(
    "CreateServiceNetworkResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "id": str,
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceNetworkServiceAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceNetworkServiceAssociationRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
        "serviceNetworkIdentifier": str,
    },
)
_OptionalCreateServiceNetworkServiceAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceNetworkServiceAssociationRequestRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateServiceNetworkServiceAssociationRequestRequestTypeDef(
    _RequiredCreateServiceNetworkServiceAssociationRequestRequestTypeDef,
    _OptionalCreateServiceNetworkServiceAssociationRequestRequestTypeDef,
):
    pass

CreateServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "customDomainName": str,
        "dnsEntry": "DnsEntryTypeDef",
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "serviceNetworkIdentifier": str,
        "vpcIdentifier": str,
    },
)
_OptionalCreateServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "clientToken": str,
        "securityGroupIds": List[str],
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateServiceNetworkVpcAssociationRequestRequestTypeDef(
    _RequiredCreateServiceNetworkVpcAssociationRequestRequestTypeDef,
    _OptionalCreateServiceNetworkVpcAssociationRequestRequestTypeDef,
):
    pass

CreateServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "CreateServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "createdBy": str,
        "id": str,
        "securityGroupIds": List[str],
        "status": ServiceNetworkVpcAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateServiceRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateServiceRequestRequestTypeDef",
    {
        "authType": AuthTypeType,
        "certificateArn": str,
        "clientToken": str,
        "customDomainName": str,
        "tags": Dict[str, str],
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
        "arn": str,
        "authType": AuthTypeType,
        "certificateArn": str,
        "customDomainName": str,
        "dnsEntry": "DnsEntryTypeDef",
        "id": str,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTargetGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTargetGroupRequestRequestTypeDef",
    {
        "name": str,
        "type": TargetGroupTypeType,
    },
)
_OptionalCreateTargetGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTargetGroupRequestRequestTypeDef",
    {
        "clientToken": str,
        "config": "TargetGroupConfigTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateTargetGroupRequestRequestTypeDef(
    _RequiredCreateTargetGroupRequestRequestTypeDef, _OptionalCreateTargetGroupRequestRequestTypeDef
):
    pass

CreateTargetGroupResponseTypeDef = TypedDict(
    "CreateTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": "TargetGroupConfigTypeDef",
        "id": str,
        "name": str,
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteAccessLogSubscriptionRequestRequestTypeDef",
    {
        "accessLogSubscriptionIdentifier": str,
    },
)

DeleteAuthPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAuthPolicyRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)

DeleteListenerRequestRequestTypeDef = TypedDict(
    "DeleteListenerRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "serviceIdentifier": str,
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

DeleteRuleRequestRequestTypeDef = TypedDict(
    "DeleteRuleRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "ruleIdentifier": str,
        "serviceIdentifier": str,
    },
)

DeleteServiceNetworkRequestRequestTypeDef = TypedDict(
    "DeleteServiceNetworkRequestRequestTypeDef",
    {
        "serviceNetworkIdentifier": str,
    },
)

DeleteServiceNetworkServiceAssociationRequestRequestTypeDef = TypedDict(
    "DeleteServiceNetworkServiceAssociationRequestRequestTypeDef",
    {
        "serviceNetworkServiceAssociationIdentifier": str,
    },
)

DeleteServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": ServiceNetworkServiceAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "DeleteServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "serviceNetworkVpcAssociationIdentifier": str,
    },
)

DeleteServiceNetworkVpcAssociationResponseTypeDef = TypedDict(
    "DeleteServiceNetworkVpcAssociationResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceRequestRequestTypeDef = TypedDict(
    "DeleteServiceRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
    },
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTargetGroupRequestRequestTypeDef = TypedDict(
    "DeleteTargetGroupRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
    },
)

DeleteTargetGroupResponseTypeDef = TypedDict(
    "DeleteTargetGroupResponseTypeDef",
    {
        "arn": str,
        "id": str,
        "status": TargetGroupStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTargetsRequestRequestTypeDef = TypedDict(
    "DeregisterTargetsRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
        "targets": List["TargetTypeDef"],
    },
)

DeregisterTargetsResponseTypeDef = TypedDict(
    "DeregisterTargetsResponseTypeDef",
    {
        "successful": List["TargetTypeDef"],
        "unsuccessful": List["TargetFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DnsEntryTypeDef = TypedDict(
    "DnsEntryTypeDef",
    {
        "domainName": str,
        "hostedZoneId": str,
    },
    total=False,
)

FixedResponseActionTypeDef = TypedDict(
    "FixedResponseActionTypeDef",
    {
        "statusCode": int,
    },
)

ForwardActionTypeDef = TypedDict(
    "ForwardActionTypeDef",
    {
        "targetGroups": List["WeightedTargetGroupTypeDef"],
    },
)

GetAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "GetAccessLogSubscriptionRequestRequestTypeDef",
    {
        "accessLogSubscriptionIdentifier": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAuthPolicyRequestRequestTypeDef = TypedDict(
    "GetAuthPolicyRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)

GetAuthPolicyResponseTypeDef = TypedDict(
    "GetAuthPolicyResponseTypeDef",
    {
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "policy": str,
        "state": AuthPolicyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetListenerRequestRequestTypeDef = TypedDict(
    "GetListenerRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "serviceIdentifier": str,
    },
)

GetListenerResponseTypeDef = TypedDict(
    "GetListenerResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "defaultAction": "RuleActionTypeDef",
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRuleRequestRequestTypeDef = TypedDict(
    "GetRuleRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "ruleIdentifier": str,
        "serviceIdentifier": str,
    },
)

GetRuleResponseTypeDef = TypedDict(
    "GetRuleResponseTypeDef",
    {
        "action": "RuleActionTypeDef",
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "isDefault": bool,
        "lastUpdatedAt": datetime,
        "match": "RuleMatchTypeDef",
        "name": str,
        "priority": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceNetworkRequestRequestTypeDef = TypedDict(
    "GetServiceNetworkRequestRequestTypeDef",
    {
        "serviceNetworkIdentifier": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceNetworkServiceAssociationRequestRequestTypeDef = TypedDict(
    "GetServiceNetworkServiceAssociationRequestRequestTypeDef",
    {
        "serviceNetworkServiceAssociationIdentifier": str,
    },
)

GetServiceNetworkServiceAssociationResponseTypeDef = TypedDict(
    "GetServiceNetworkServiceAssociationResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "customDomainName": str,
        "dnsEntry": "DnsEntryTypeDef",
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "GetServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "serviceNetworkVpcAssociationIdentifier": str,
    },
)

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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceRequestRequestTypeDef = TypedDict(
    "GetServiceRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
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
        "dnsEntry": "DnsEntryTypeDef",
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": ServiceStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTargetGroupRequestRequestTypeDef = TypedDict(
    "GetTargetGroupRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
    },
)

GetTargetGroupResponseTypeDef = TypedDict(
    "GetTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": "TargetGroupConfigTypeDef",
        "createdAt": datetime,
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "serviceArns": List[str],
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHeaderMatchTypeDef = TypedDict(
    "_RequiredHeaderMatchTypeDef",
    {
        "match": "HeaderMatchTypeTypeDef",
        "name": str,
    },
)
_OptionalHeaderMatchTypeDef = TypedDict(
    "_OptionalHeaderMatchTypeDef",
    {
        "caseSensitive": bool,
    },
    total=False,
)

class HeaderMatchTypeDef(_RequiredHeaderMatchTypeDef, _OptionalHeaderMatchTypeDef):
    pass

HeaderMatchTypeTypeDef = TypedDict(
    "HeaderMatchTypeTypeDef",
    {
        "contains": str,
        "exact": str,
        "prefix": str,
    },
    total=False,
)

HealthCheckConfigTypeDef = TypedDict(
    "HealthCheckConfigTypeDef",
    {
        "enabled": bool,
        "healthCheckIntervalSeconds": int,
        "healthCheckTimeoutSeconds": int,
        "healthyThresholdCount": int,
        "matcher": "MatcherTypeDef",
        "path": str,
        "port": int,
        "protocol": TargetGroupProtocolType,
        "protocolVersion": HealthCheckProtocolVersionType,
        "unhealthyThresholdCount": int,
    },
    total=False,
)

HttpMatchTypeDef = TypedDict(
    "HttpMatchTypeDef",
    {
        "headerMatches": List["HeaderMatchTypeDef"],
        "method": str,
        "pathMatch": "PathMatchTypeDef",
    },
    total=False,
)

_RequiredListAccessLogSubscriptionsRequestRequestTypeDef = TypedDict(
    "_RequiredListAccessLogSubscriptionsRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)
_OptionalListAccessLogSubscriptionsRequestRequestTypeDef = TypedDict(
    "_OptionalListAccessLogSubscriptionsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAccessLogSubscriptionsRequestRequestTypeDef(
    _RequiredListAccessLogSubscriptionsRequestRequestTypeDef,
    _OptionalListAccessLogSubscriptionsRequestRequestTypeDef,
):
    pass

ListAccessLogSubscriptionsResponseTypeDef = TypedDict(
    "ListAccessLogSubscriptionsResponseTypeDef",
    {
        "items": List["AccessLogSubscriptionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListListenersRequestRequestTypeDef = TypedDict(
    "_RequiredListListenersRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
    },
)
_OptionalListListenersRequestRequestTypeDef = TypedDict(
    "_OptionalListListenersRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListListenersRequestRequestTypeDef(
    _RequiredListListenersRequestRequestTypeDef, _OptionalListListenersRequestRequestTypeDef
):
    pass

ListListenersResponseTypeDef = TypedDict(
    "ListListenersResponseTypeDef",
    {
        "items": List["ListenerSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRulesRequestRequestTypeDef = TypedDict(
    "_RequiredListRulesRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "serviceIdentifier": str,
    },
)
_OptionalListRulesRequestRequestTypeDef = TypedDict(
    "_OptionalListRulesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListRulesRequestRequestTypeDef(
    _RequiredListRulesRequestRequestTypeDef, _OptionalListRulesRequestRequestTypeDef
):
    pass

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "items": List["RuleSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceNetworkServiceAssociationsRequestRequestTypeDef = TypedDict(
    "ListServiceNetworkServiceAssociationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "serviceIdentifier": str,
        "serviceNetworkIdentifier": str,
    },
    total=False,
)

ListServiceNetworkServiceAssociationsResponseTypeDef = TypedDict(
    "ListServiceNetworkServiceAssociationsResponseTypeDef",
    {
        "items": List["ServiceNetworkServiceAssociationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceNetworkVpcAssociationsRequestRequestTypeDef = TypedDict(
    "ListServiceNetworkVpcAssociationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "serviceNetworkIdentifier": str,
        "vpcIdentifier": str,
    },
    total=False,
)

ListServiceNetworkVpcAssociationsResponseTypeDef = TypedDict(
    "ListServiceNetworkVpcAssociationsResponseTypeDef",
    {
        "items": List["ServiceNetworkVpcAssociationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceNetworksRequestRequestTypeDef = TypedDict(
    "ListServiceNetworksRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListServiceNetworksResponseTypeDef = TypedDict(
    "ListServiceNetworksResponseTypeDef",
    {
        "items": List["ServiceNetworkSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServicesRequestRequestTypeDef = TypedDict(
    "ListServicesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef",
    {
        "items": List["ServiceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetGroupsRequestRequestTypeDef = TypedDict(
    "ListTargetGroupsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "targetGroupType": TargetGroupTypeType,
        "vpcIdentifier": str,
    },
    total=False,
)

ListTargetGroupsResponseTypeDef = TypedDict(
    "ListTargetGroupsResponseTypeDef",
    {
        "items": List["TargetGroupSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredListTargetsRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
    },
)
_OptionalListTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalListTargetsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "targets": List["TargetTypeDef"],
    },
    total=False,
)

class ListTargetsRequestRequestTypeDef(
    _RequiredListTargetsRequestRequestTypeDef, _OptionalListTargetsRequestRequestTypeDef
):
    pass

ListTargetsResponseTypeDef = TypedDict(
    "ListTargetsResponseTypeDef",
    {
        "items": List["TargetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListenerSummaryTypeDef = TypedDict(
    "ListenerSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
    },
    total=False,
)

MatcherTypeDef = TypedDict(
    "MatcherTypeDef",
    {
        "httpCode": str,
    },
    total=False,
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

_RequiredPathMatchTypeDef = TypedDict(
    "_RequiredPathMatchTypeDef",
    {
        "match": "PathMatchTypeTypeDef",
    },
)
_OptionalPathMatchTypeDef = TypedDict(
    "_OptionalPathMatchTypeDef",
    {
        "caseSensitive": bool,
    },
    total=False,
)

class PathMatchTypeDef(_RequiredPathMatchTypeDef, _OptionalPathMatchTypeDef):
    pass

PathMatchTypeTypeDef = TypedDict(
    "PathMatchTypeTypeDef",
    {
        "exact": str,
        "prefix": str,
    },
    total=False,
)

PutAuthPolicyRequestRequestTypeDef = TypedDict(
    "PutAuthPolicyRequestRequestTypeDef",
    {
        "policy": str,
        "resourceIdentifier": str,
    },
)

PutAuthPolicyResponseTypeDef = TypedDict(
    "PutAuthPolicyResponseTypeDef",
    {
        "policy": str,
        "state": AuthPolicyStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "policy": str,
        "resourceArn": str,
    },
)

RegisterTargetsRequestRequestTypeDef = TypedDict(
    "RegisterTargetsRequestRequestTypeDef",
    {
        "targetGroupIdentifier": str,
        "targets": List["TargetTypeDef"],
    },
)

RegisterTargetsResponseTypeDef = TypedDict(
    "RegisterTargetsResponseTypeDef",
    {
        "successful": List["TargetTypeDef"],
        "unsuccessful": List["TargetFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RuleActionTypeDef = TypedDict(
    "RuleActionTypeDef",
    {
        "fixedResponse": "FixedResponseActionTypeDef",
        "forward": "ForwardActionTypeDef",
    },
    total=False,
)

RuleMatchTypeDef = TypedDict(
    "RuleMatchTypeDef",
    {
        "httpMatch": "HttpMatchTypeDef",
    },
    total=False,
)

RuleSummaryTypeDef = TypedDict(
    "RuleSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "isDefault": bool,
        "lastUpdatedAt": datetime,
        "name": str,
        "priority": int,
    },
    total=False,
)

RuleUpdateFailureTypeDef = TypedDict(
    "RuleUpdateFailureTypeDef",
    {
        "failureCode": str,
        "failureMessage": str,
        "ruleIdentifier": str,
    },
    total=False,
)

RuleUpdateSuccessTypeDef = TypedDict(
    "RuleUpdateSuccessTypeDef",
    {
        "action": "RuleActionTypeDef",
        "arn": str,
        "id": str,
        "isDefault": bool,
        "match": "RuleMatchTypeDef",
        "name": str,
        "priority": int,
    },
    total=False,
)

_RequiredRuleUpdateTypeDef = TypedDict(
    "_RequiredRuleUpdateTypeDef",
    {
        "ruleIdentifier": str,
    },
)
_OptionalRuleUpdateTypeDef = TypedDict(
    "_OptionalRuleUpdateTypeDef",
    {
        "action": "RuleActionTypeDef",
        "match": "RuleMatchTypeDef",
        "priority": int,
    },
    total=False,
)

class RuleUpdateTypeDef(_RequiredRuleUpdateTypeDef, _OptionalRuleUpdateTypeDef):
    pass

ServiceNetworkServiceAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkServiceAssociationSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "customDomainName": str,
        "dnsEntry": "DnsEntryTypeDef",
        "id": str,
        "serviceArn": str,
        "serviceId": str,
        "serviceName": str,
        "serviceNetworkArn": str,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "status": ServiceNetworkServiceAssociationStatusType,
    },
    total=False,
)

ServiceNetworkSummaryTypeDef = TypedDict(
    "ServiceNetworkSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "numberOfAssociatedServices": int,
        "numberOfAssociatedVPCs": int,
    },
    total=False,
)

ServiceNetworkVpcAssociationSummaryTypeDef = TypedDict(
    "ServiceNetworkVpcAssociationSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "createdBy": str,
        "id": str,
        "lastUpdatedAt": datetime,
        "serviceNetworkArn": str,
        "serviceNetworkId": str,
        "serviceNetworkName": str,
        "status": ServiceNetworkVpcAssociationStatusType,
        "vpcId": str,
    },
    total=False,
)

ServiceSummaryTypeDef = TypedDict(
    "ServiceSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "customDomainName": str,
        "dnsEntry": "DnsEntryTypeDef",
        "id": str,
        "lastUpdatedAt": datetime,
        "name": str,
        "status": ServiceStatusType,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

TargetFailureTypeDef = TypedDict(
    "TargetFailureTypeDef",
    {
        "failureCode": str,
        "failureMessage": str,
        "id": str,
        "port": int,
    },
    total=False,
)

TargetGroupConfigTypeDef = TypedDict(
    "TargetGroupConfigTypeDef",
    {
        "healthCheck": "HealthCheckConfigTypeDef",
        "ipAddressType": IpAddressTypeType,
        "lambdaEventStructureVersion": LambdaEventStructureVersionType,
        "port": int,
        "protocol": TargetGroupProtocolType,
        "protocolVersion": TargetGroupProtocolVersionType,
        "vpcIdentifier": str,
    },
    total=False,
)

TargetGroupSummaryTypeDef = TypedDict(
    "TargetGroupSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "id": str,
        "ipAddressType": IpAddressTypeType,
        "lambdaEventStructureVersion": LambdaEventStructureVersionType,
        "lastUpdatedAt": datetime,
        "name": str,
        "port": int,
        "protocol": TargetGroupProtocolType,
        "serviceArns": List[str],
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "vpcIdentifier": str,
    },
    total=False,
)

TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "id": str,
        "port": int,
        "reasonCode": str,
        "status": TargetStatusType,
    },
    total=False,
)

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "id": str,
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "port": int,
    },
    total=False,
)

class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateAccessLogSubscriptionRequestRequestTypeDef = TypedDict(
    "UpdateAccessLogSubscriptionRequestRequestTypeDef",
    {
        "accessLogSubscriptionIdentifier": str,
        "destinationArn": str,
    },
)

UpdateAccessLogSubscriptionResponseTypeDef = TypedDict(
    "UpdateAccessLogSubscriptionResponseTypeDef",
    {
        "arn": str,
        "destinationArn": str,
        "id": str,
        "resourceArn": str,
        "resourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateListenerRequestRequestTypeDef = TypedDict(
    "UpdateListenerRequestRequestTypeDef",
    {
        "defaultAction": "RuleActionTypeDef",
        "listenerIdentifier": str,
        "serviceIdentifier": str,
    },
)

UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef",
    {
        "arn": str,
        "defaultAction": "RuleActionTypeDef",
        "id": str,
        "name": str,
        "port": int,
        "protocol": ListenerProtocolType,
        "serviceArn": str,
        "serviceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRuleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRuleRequestRequestTypeDef",
    {
        "listenerIdentifier": str,
        "ruleIdentifier": str,
        "serviceIdentifier": str,
    },
)
_OptionalUpdateRuleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRuleRequestRequestTypeDef",
    {
        "action": "RuleActionTypeDef",
        "match": "RuleMatchTypeDef",
        "priority": int,
    },
    total=False,
)

class UpdateRuleRequestRequestTypeDef(
    _RequiredUpdateRuleRequestRequestTypeDef, _OptionalUpdateRuleRequestRequestTypeDef
):
    pass

UpdateRuleResponseTypeDef = TypedDict(
    "UpdateRuleResponseTypeDef",
    {
        "action": "RuleActionTypeDef",
        "arn": str,
        "id": str,
        "isDefault": bool,
        "match": "RuleMatchTypeDef",
        "name": str,
        "priority": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceNetworkRequestRequestTypeDef = TypedDict(
    "UpdateServiceNetworkRequestRequestTypeDef",
    {
        "authType": AuthTypeType,
        "serviceNetworkIdentifier": str,
    },
)

UpdateServiceNetworkResponseTypeDef = TypedDict(
    "UpdateServiceNetworkResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "id": str,
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateServiceNetworkVpcAssociationRequestRequestTypeDef = TypedDict(
    "UpdateServiceNetworkVpcAssociationRequestRequestTypeDef",
    {
        "securityGroupIds": List[str],
        "serviceNetworkVpcAssociationIdentifier": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateServiceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateServiceRequestRequestTypeDef",
    {
        "serviceIdentifier": str,
    },
)
_OptionalUpdateServiceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateServiceRequestRequestTypeDef",
    {
        "authType": AuthTypeType,
        "certificateArn": str,
    },
    total=False,
)

class UpdateServiceRequestRequestTypeDef(
    _RequiredUpdateServiceRequestRequestTypeDef, _OptionalUpdateServiceRequestRequestTypeDef
):
    pass

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef",
    {
        "arn": str,
        "authType": AuthTypeType,
        "certificateArn": str,
        "customDomainName": str,
        "id": str,
        "name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTargetGroupRequestRequestTypeDef = TypedDict(
    "UpdateTargetGroupRequestRequestTypeDef",
    {
        "healthCheck": "HealthCheckConfigTypeDef",
        "targetGroupIdentifier": str,
    },
)

UpdateTargetGroupResponseTypeDef = TypedDict(
    "UpdateTargetGroupResponseTypeDef",
    {
        "arn": str,
        "config": "TargetGroupConfigTypeDef",
        "id": str,
        "name": str,
        "status": TargetGroupStatusType,
        "type": TargetGroupTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredWeightedTargetGroupTypeDef = TypedDict(
    "_RequiredWeightedTargetGroupTypeDef",
    {
        "targetGroupIdentifier": str,
    },
)
_OptionalWeightedTargetGroupTypeDef = TypedDict(
    "_OptionalWeightedTargetGroupTypeDef",
    {
        "weight": int,
    },
    total=False,
)

class WeightedTargetGroupTypeDef(
    _RequiredWeightedTargetGroupTypeDef, _OptionalWeightedTargetGroupTypeDef
):
    pass
