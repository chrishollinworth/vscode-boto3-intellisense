"""
Type annotations for elbv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elbv2.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ActionTypeEnumType,
    AuthenticateCognitoActionConditionalBehaviorEnumType,
    AuthenticateOidcActionConditionalBehaviorEnumType,
    IpAddressTypeType,
    LoadBalancerSchemeEnumType,
    LoadBalancerStateEnumType,
    LoadBalancerTypeEnumType,
    ProtocolEnumType,
    RedirectActionStatusCodeEnumType,
    TargetHealthReasonEnumType,
    TargetHealthStateEnumType,
    TargetTypeEnumType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActionTypeDef",
    "AddListenerCertificatesInputRequestTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateTypeDef",
    "CipherTypeDef",
    "CreateListenerInputRequestTypeDef",
    "CreateListenerOutputTypeDef",
    "CreateLoadBalancerInputRequestTypeDef",
    "CreateLoadBalancerOutputTypeDef",
    "CreateRuleInputRequestTypeDef",
    "CreateRuleOutputTypeDef",
    "CreateTargetGroupInputRequestTypeDef",
    "CreateTargetGroupOutputTypeDef",
    "DeleteListenerInputRequestTypeDef",
    "DeleteLoadBalancerInputRequestTypeDef",
    "DeleteRuleInputRequestTypeDef",
    "DeleteTargetGroupInputRequestTypeDef",
    "DeregisterTargetsInputRequestTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeListenerCertificatesInputRequestTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "DescribeListenersInputRequestTypeDef",
    "DescribeListenersOutputTypeDef",
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancersInputRequestTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "DescribeRulesInputRequestTypeDef",
    "DescribeRulesOutputTypeDef",
    "DescribeSSLPoliciesInputRequestTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeTargetGroupAttributesInputRequestTypeDef",
    "DescribeTargetGroupAttributesOutputTypeDef",
    "DescribeTargetGroupsInputRequestTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "DescribeTargetHealthInputRequestTypeDef",
    "DescribeTargetHealthOutputTypeDef",
    "FixedResponseActionConfigTypeDef",
    "ForwardActionConfigTypeDef",
    "HostHeaderConditionConfigTypeDef",
    "HttpHeaderConditionConfigTypeDef",
    "HttpRequestMethodConditionConfigTypeDef",
    "LimitTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAddressTypeDef",
    "LoadBalancerAttributeTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTypeDef",
    "MatcherTypeDef",
    "ModifyListenerInputRequestTypeDef",
    "ModifyListenerOutputTypeDef",
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "ModifyRuleInputRequestTypeDef",
    "ModifyRuleOutputTypeDef",
    "ModifyTargetGroupAttributesInputRequestTypeDef",
    "ModifyTargetGroupAttributesOutputTypeDef",
    "ModifyTargetGroupInputRequestTypeDef",
    "ModifyTargetGroupOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RedirectActionConfigTypeDef",
    "RegisterTargetsInputRequestTypeDef",
    "RemoveListenerCertificatesInputRequestTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuleConditionTypeDef",
    "RulePriorityPairTypeDef",
    "RuleTypeDef",
    "SetIpAddressTypeInputRequestTypeDef",
    "SetIpAddressTypeOutputTypeDef",
    "SetRulePrioritiesInputRequestTypeDef",
    "SetRulePrioritiesOutputTypeDef",
    "SetSecurityGroupsInputRequestTypeDef",
    "SetSecurityGroupsOutputTypeDef",
    "SetSubnetsInputRequestTypeDef",
    "SetSubnetsOutputTypeDef",
    "SourceIpConditionConfigTypeDef",
    "SslPolicyTypeDef",
    "SubnetMappingTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TargetDescriptionTypeDef",
    "TargetGroupAttributeTypeDef",
    "TargetGroupStickinessConfigTypeDef",
    "TargetGroupTupleTypeDef",
    "TargetGroupTypeDef",
    "TargetHealthDescriptionTypeDef",
    "TargetHealthTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredActionTypeDef = TypedDict(
    "_RequiredActionTypeDef",
    {
        "Type": ActionTypeEnumType,
    },
)
_OptionalActionTypeDef = TypedDict(
    "_OptionalActionTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": "AuthenticateOidcActionConfigTypeDef",
        "AuthenticateCognitoConfig": "AuthenticateCognitoActionConfigTypeDef",
        "Order": int,
        "RedirectConfig": "RedirectActionConfigTypeDef",
        "FixedResponseConfig": "FixedResponseActionConfigTypeDef",
        "ForwardConfig": "ForwardActionConfigTypeDef",
    },
    total=False,
)

class ActionTypeDef(_RequiredActionTypeDef, _OptionalActionTypeDef):
    pass

AddListenerCertificatesInputRequestTypeDef = TypedDict(
    "AddListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Certificates": List["CertificateTypeDef"],
    },
)

AddListenerCertificatesOutputTypeDef = TypedDict(
    "AddListenerCertificatesOutputTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "ResourceArns": List[str],
        "Tags": List["TagTypeDef"],
    },
)

_RequiredAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateCognitoActionConfigTypeDef",
    {
        "UserPoolArn": str,
        "UserPoolClientId": str,
        "UserPoolDomain": str,
    },
)
_OptionalAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateCognitoActionConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": AuthenticateCognitoActionConditionalBehaviorEnumType,
    },
    total=False,
)

class AuthenticateCognitoActionConfigTypeDef(
    _RequiredAuthenticateCognitoActionConfigTypeDef, _OptionalAuthenticateCognitoActionConfigTypeDef
):
    pass

_RequiredAuthenticateOidcActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateOidcActionConfigTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
    },
)
_OptionalAuthenticateOidcActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateOidcActionConfigTypeDef",
    {
        "ClientSecret": str,
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": AuthenticateOidcActionConditionalBehaviorEnumType,
        "UseExistingClientSecret": bool,
    },
    total=False,
)

class AuthenticateOidcActionConfigTypeDef(
    _RequiredAuthenticateOidcActionConfigTypeDef, _OptionalAuthenticateOidcActionConfigTypeDef
):
    pass

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "ZoneName": str,
        "SubnetId": str,
        "OutpostId": str,
        "LoadBalancerAddresses": List["LoadBalancerAddressTypeDef"],
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateArn": str,
        "IsDefault": bool,
    },
    total=False,
)

CipherTypeDef = TypedDict(
    "CipherTypeDef",
    {
        "Name": str,
        "Priority": int,
    },
    total=False,
)

_RequiredCreateListenerInputRequestTypeDef = TypedDict(
    "_RequiredCreateListenerInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "DefaultActions": List["ActionTypeDef"],
    },
)
_OptionalCreateListenerInputRequestTypeDef = TypedDict(
    "_OptionalCreateListenerInputRequestTypeDef",
    {
        "Protocol": ProtocolEnumType,
        "Port": int,
        "SslPolicy": str,
        "Certificates": List["CertificateTypeDef"],
        "AlpnPolicy": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateListenerInputRequestTypeDef(
    _RequiredCreateListenerInputRequestTypeDef, _OptionalCreateListenerInputRequestTypeDef
):
    pass

CreateListenerOutputTypeDef = TypedDict(
    "CreateListenerOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoadBalancerInputRequestTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateLoadBalancerInputRequestTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerInputRequestTypeDef",
    {
        "Subnets": List[str],
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "SecurityGroups": List[str],
        "Scheme": LoadBalancerSchemeEnumType,
        "Tags": List["TagTypeDef"],
        "Type": LoadBalancerTypeEnumType,
        "IpAddressType": IpAddressTypeType,
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)

class CreateLoadBalancerInputRequestTypeDef(
    _RequiredCreateLoadBalancerInputRequestTypeDef, _OptionalCreateLoadBalancerInputRequestTypeDef
):
    pass

CreateLoadBalancerOutputTypeDef = TypedDict(
    "CreateLoadBalancerOutputTypeDef",
    {
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRuleInputRequestTypeDef = TypedDict(
    "_RequiredCreateRuleInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Conditions": List["RuleConditionTypeDef"],
        "Priority": int,
        "Actions": List["ActionTypeDef"],
    },
)
_OptionalCreateRuleInputRequestTypeDef = TypedDict(
    "_OptionalCreateRuleInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRuleInputRequestTypeDef(
    _RequiredCreateRuleInputRequestTypeDef, _OptionalCreateRuleInputRequestTypeDef
):
    pass

CreateRuleOutputTypeDef = TypedDict(
    "CreateRuleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTargetGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateTargetGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateTargetGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateTargetGroupInputRequestTypeDef",
    {
        "Protocol": ProtocolEnumType,
        "ProtocolVersion": str,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckPath": str,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "Matcher": "MatcherTypeDef",
        "TargetType": TargetTypeEnumType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTargetGroupInputRequestTypeDef(
    _RequiredCreateTargetGroupInputRequestTypeDef, _OptionalCreateTargetGroupInputRequestTypeDef
):
    pass

CreateTargetGroupOutputTypeDef = TypedDict(
    "CreateTargetGroupOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteListenerInputRequestTypeDef = TypedDict(
    "DeleteListenerInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DeleteLoadBalancerInputRequestTypeDef = TypedDict(
    "DeleteLoadBalancerInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)

DeleteRuleInputRequestTypeDef = TypedDict(
    "DeleteRuleInputRequestTypeDef",
    {
        "RuleArn": str,
    },
)

DeleteTargetGroupInputRequestTypeDef = TypedDict(
    "DeleteTargetGroupInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)

DeregisterTargetsInputRequestTypeDef = TypedDict(
    "DeregisterTargetsInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": List["TargetDescriptionTypeDef"],
    },
)

DescribeAccountLimitsInputRequestTypeDef = TypedDict(
    "DescribeAccountLimitsInputRequestTypeDef",
    {
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "Limits": List["LimitTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeListenerCertificatesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalDescribeListenerCertificatesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeListenerCertificatesInputRequestTypeDef",
    {
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

class DescribeListenerCertificatesInputRequestTypeDef(
    _RequiredDescribeListenerCertificatesInputRequestTypeDef,
    _OptionalDescribeListenerCertificatesInputRequestTypeDef,
):
    pass

DescribeListenerCertificatesOutputTypeDef = TypedDict(
    "DescribeListenerCertificatesOutputTypeDef",
    {
        "Certificates": List["CertificateTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenersInputRequestTypeDef = TypedDict(
    "DescribeListenersInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "ListenerArns": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeListenersOutputTypeDef = TypedDict(
    "DescribeListenersOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)

DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List["LoadBalancerAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLoadBalancersInputRequestTypeDef = TypedDict(
    "DescribeLoadBalancersInputRequestTypeDef",
    {
        "LoadBalancerArns": List[str],
        "Names": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeLoadBalancersOutputTypeDef = TypedDict(
    "DescribeLoadBalancersOutputTypeDef",
    {
        "LoadBalancers": List["LoadBalancerTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRulesInputRequestTypeDef = TypedDict(
    "DescribeRulesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "RuleArns": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeRulesOutputTypeDef = TypedDict(
    "DescribeRulesOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSSLPoliciesInputRequestTypeDef = TypedDict(
    "DescribeSSLPoliciesInputRequestTypeDef",
    {
        "Names": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeSSLPoliciesOutputTypeDef = TypedDict(
    "DescribeSSLPoliciesOutputTypeDef",
    {
        "SslPolicies": List["SslPolicyTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "ResourceArns": List[str],
    },
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "TagDescriptions": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetGroupAttributesInputRequestTypeDef = TypedDict(
    "DescribeTargetGroupAttributesInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)

DescribeTargetGroupAttributesOutputTypeDef = TypedDict(
    "DescribeTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List["TargetGroupAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTargetGroupsInputRequestTypeDef = TypedDict(
    "DescribeTargetGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "TargetGroupArns": List[str],
        "Names": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeTargetGroupsOutputTypeDef = TypedDict(
    "DescribeTargetGroupsOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTargetHealthInputRequestTypeDef = TypedDict(
    "_RequiredDescribeTargetHealthInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)
_OptionalDescribeTargetHealthInputRequestTypeDef = TypedDict(
    "_OptionalDescribeTargetHealthInputRequestTypeDef",
    {
        "Targets": List["TargetDescriptionTypeDef"],
    },
    total=False,
)

class DescribeTargetHealthInputRequestTypeDef(
    _RequiredDescribeTargetHealthInputRequestTypeDef,
    _OptionalDescribeTargetHealthInputRequestTypeDef,
):
    pass

DescribeTargetHealthOutputTypeDef = TypedDict(
    "DescribeTargetHealthOutputTypeDef",
    {
        "TargetHealthDescriptions": List["TargetHealthDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredFixedResponseActionConfigTypeDef = TypedDict(
    "_RequiredFixedResponseActionConfigTypeDef",
    {
        "StatusCode": str,
    },
)
_OptionalFixedResponseActionConfigTypeDef = TypedDict(
    "_OptionalFixedResponseActionConfigTypeDef",
    {
        "MessageBody": str,
        "ContentType": str,
    },
    total=False,
)

class FixedResponseActionConfigTypeDef(
    _RequiredFixedResponseActionConfigTypeDef, _OptionalFixedResponseActionConfigTypeDef
):
    pass

ForwardActionConfigTypeDef = TypedDict(
    "ForwardActionConfigTypeDef",
    {
        "TargetGroups": List["TargetGroupTupleTypeDef"],
        "TargetGroupStickinessConfig": "TargetGroupStickinessConfigTypeDef",
    },
    total=False,
)

HostHeaderConditionConfigTypeDef = TypedDict(
    "HostHeaderConditionConfigTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

HttpHeaderConditionConfigTypeDef = TypedDict(
    "HttpHeaderConditionConfigTypeDef",
    {
        "HttpHeaderName": str,
        "Values": List[str],
    },
    total=False,
)

HttpRequestMethodConditionConfigTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

LimitTypeDef = TypedDict(
    "LimitTypeDef",
    {
        "Name": str,
        "Max": str,
    },
    total=False,
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": ProtocolEnumType,
        "Certificates": List["CertificateTypeDef"],
        "SslPolicy": str,
        "DefaultActions": List["ActionTypeDef"],
        "AlpnPolicy": List[str],
    },
    total=False,
)

LoadBalancerAddressTypeDef = TypedDict(
    "LoadBalancerAddressTypeDef",
    {
        "IpAddress": str,
        "AllocationId": str,
        "PrivateIPv4Address": str,
        "IPv6Address": str,
    },
    total=False,
)

LoadBalancerAttributeTypeDef = TypedDict(
    "LoadBalancerAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {
        "Code": LoadBalancerStateEnumType,
        "Reason": str,
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": LoadBalancerSchemeEnumType,
        "VpcId": str,
        "State": "LoadBalancerStateTypeDef",
        "Type": LoadBalancerTypeEnumType,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "SecurityGroups": List[str],
        "IpAddressType": IpAddressTypeType,
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)

MatcherTypeDef = TypedDict(
    "MatcherTypeDef",
    {
        "HttpCode": str,
        "GrpcCode": str,
    },
    total=False,
)

_RequiredModifyListenerInputRequestTypeDef = TypedDict(
    "_RequiredModifyListenerInputRequestTypeDef",
    {
        "ListenerArn": str,
    },
)
_OptionalModifyListenerInputRequestTypeDef = TypedDict(
    "_OptionalModifyListenerInputRequestTypeDef",
    {
        "Port": int,
        "Protocol": ProtocolEnumType,
        "SslPolicy": str,
        "Certificates": List["CertificateTypeDef"],
        "DefaultActions": List["ActionTypeDef"],
        "AlpnPolicy": List[str],
    },
    total=False,
)

class ModifyListenerInputRequestTypeDef(
    _RequiredModifyListenerInputRequestTypeDef, _OptionalModifyListenerInputRequestTypeDef
):
    pass

ModifyListenerOutputTypeDef = TypedDict(
    "ModifyListenerOutputTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLoadBalancerAttributesInputRequestTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "Attributes": List["LoadBalancerAttributeTypeDef"],
    },
)

ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {
        "Attributes": List["LoadBalancerAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyRuleInputRequestTypeDef = TypedDict(
    "_RequiredModifyRuleInputRequestTypeDef",
    {
        "RuleArn": str,
    },
)
_OptionalModifyRuleInputRequestTypeDef = TypedDict(
    "_OptionalModifyRuleInputRequestTypeDef",
    {
        "Conditions": List["RuleConditionTypeDef"],
        "Actions": List["ActionTypeDef"],
    },
    total=False,
)

class ModifyRuleInputRequestTypeDef(
    _RequiredModifyRuleInputRequestTypeDef, _OptionalModifyRuleInputRequestTypeDef
):
    pass

ModifyRuleOutputTypeDef = TypedDict(
    "ModifyRuleOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTargetGroupAttributesInputRequestTypeDef = TypedDict(
    "ModifyTargetGroupAttributesInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Attributes": List["TargetGroupAttributeTypeDef"],
    },
)

ModifyTargetGroupAttributesOutputTypeDef = TypedDict(
    "ModifyTargetGroupAttributesOutputTypeDef",
    {
        "Attributes": List["TargetGroupAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTargetGroupInputRequestTypeDef = TypedDict(
    "_RequiredModifyTargetGroupInputRequestTypeDef",
    {
        "TargetGroupArn": str,
    },
)
_OptionalModifyTargetGroupInputRequestTypeDef = TypedDict(
    "_OptionalModifyTargetGroupInputRequestTypeDef",
    {
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckPath": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "Matcher": "MatcherTypeDef",
    },
    total=False,
)

class ModifyTargetGroupInputRequestTypeDef(
    _RequiredModifyTargetGroupInputRequestTypeDef, _OptionalModifyTargetGroupInputRequestTypeDef
):
    pass

ModifyTargetGroupOutputTypeDef = TypedDict(
    "ModifyTargetGroupOutputTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
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

PathPatternConditionConfigTypeDef = TypedDict(
    "PathPatternConditionConfigTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

QueryStringConditionConfigTypeDef = TypedDict(
    "QueryStringConditionConfigTypeDef",
    {
        "Values": List["QueryStringKeyValuePairTypeDef"],
    },
    total=False,
)

QueryStringKeyValuePairTypeDef = TypedDict(
    "QueryStringKeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredRedirectActionConfigTypeDef = TypedDict(
    "_RequiredRedirectActionConfigTypeDef",
    {
        "StatusCode": RedirectActionStatusCodeEnumType,
    },
)
_OptionalRedirectActionConfigTypeDef = TypedDict(
    "_OptionalRedirectActionConfigTypeDef",
    {
        "Protocol": str,
        "Port": str,
        "Host": str,
        "Path": str,
        "Query": str,
    },
    total=False,
)

class RedirectActionConfigTypeDef(
    _RequiredRedirectActionConfigTypeDef, _OptionalRedirectActionConfigTypeDef
):
    pass

RegisterTargetsInputRequestTypeDef = TypedDict(
    "RegisterTargetsInputRequestTypeDef",
    {
        "TargetGroupArn": str,
        "Targets": List["TargetDescriptionTypeDef"],
    },
)

RemoveListenerCertificatesInputRequestTypeDef = TypedDict(
    "RemoveListenerCertificatesInputRequestTypeDef",
    {
        "ListenerArn": str,
        "Certificates": List["CertificateTypeDef"],
    },
)

RemoveTagsInputRequestTypeDef = TypedDict(
    "RemoveTagsInputRequestTypeDef",
    {
        "ResourceArns": List[str],
        "TagKeys": List[str],
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

RuleConditionTypeDef = TypedDict(
    "RuleConditionTypeDef",
    {
        "Field": str,
        "Values": List[str],
        "HostHeaderConfig": "HostHeaderConditionConfigTypeDef",
        "PathPatternConfig": "PathPatternConditionConfigTypeDef",
        "HttpHeaderConfig": "HttpHeaderConditionConfigTypeDef",
        "QueryStringConfig": "QueryStringConditionConfigTypeDef",
        "HttpRequestMethodConfig": "HttpRequestMethodConditionConfigTypeDef",
        "SourceIpConfig": "SourceIpConditionConfigTypeDef",
    },
    total=False,
)

RulePriorityPairTypeDef = TypedDict(
    "RulePriorityPairTypeDef",
    {
        "RuleArn": str,
        "Priority": int,
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "RuleArn": str,
        "Priority": str,
        "Conditions": List["RuleConditionTypeDef"],
        "Actions": List["ActionTypeDef"],
        "IsDefault": bool,
    },
    total=False,
)

SetIpAddressTypeInputRequestTypeDef = TypedDict(
    "SetIpAddressTypeInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "IpAddressType": IpAddressTypeType,
    },
)

SetIpAddressTypeOutputTypeDef = TypedDict(
    "SetIpAddressTypeOutputTypeDef",
    {
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetRulePrioritiesInputRequestTypeDef = TypedDict(
    "SetRulePrioritiesInputRequestTypeDef",
    {
        "RulePriorities": List["RulePriorityPairTypeDef"],
    },
)

SetRulePrioritiesOutputTypeDef = TypedDict(
    "SetRulePrioritiesOutputTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSecurityGroupsInputRequestTypeDef = TypedDict(
    "SetSecurityGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "SecurityGroups": List[str],
    },
)

SetSecurityGroupsOutputTypeDef = TypedDict(
    "SetSecurityGroupsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSetSubnetsInputRequestTypeDef = TypedDict(
    "_RequiredSetSubnetsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
    },
)
_OptionalSetSubnetsInputRequestTypeDef = TypedDict(
    "_OptionalSetSubnetsInputRequestTypeDef",
    {
        "Subnets": List[str],
        "SubnetMappings": List["SubnetMappingTypeDef"],
        "IpAddressType": IpAddressTypeType,
    },
    total=False,
)

class SetSubnetsInputRequestTypeDef(
    _RequiredSetSubnetsInputRequestTypeDef, _OptionalSetSubnetsInputRequestTypeDef
):
    pass

SetSubnetsOutputTypeDef = TypedDict(
    "SetSubnetsOutputTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "IpAddressType": IpAddressTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SourceIpConditionConfigTypeDef = TypedDict(
    "SourceIpConditionConfigTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

SslPolicyTypeDef = TypedDict(
    "SslPolicyTypeDef",
    {
        "SslProtocols": List[str],
        "Ciphers": List["CipherTypeDef"],
        "Name": str,
    },
    total=False,
)

SubnetMappingTypeDef = TypedDict(
    "SubnetMappingTypeDef",
    {
        "SubnetId": str,
        "AllocationId": str,
        "PrivateIPv4Address": str,
        "IPv6Address": str,
    },
    total=False,
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

_RequiredTargetDescriptionTypeDef = TypedDict(
    "_RequiredTargetDescriptionTypeDef",
    {
        "Id": str,
    },
)
_OptionalTargetDescriptionTypeDef = TypedDict(
    "_OptionalTargetDescriptionTypeDef",
    {
        "Port": int,
        "AvailabilityZone": str,
    },
    total=False,
)

class TargetDescriptionTypeDef(
    _RequiredTargetDescriptionTypeDef, _OptionalTargetDescriptionTypeDef
):
    pass

TargetGroupAttributeTypeDef = TypedDict(
    "TargetGroupAttributeTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

TargetGroupStickinessConfigTypeDef = TypedDict(
    "TargetGroupStickinessConfigTypeDef",
    {
        "Enabled": bool,
        "DurationSeconds": int,
    },
    total=False,
)

TargetGroupTupleTypeDef = TypedDict(
    "TargetGroupTupleTypeDef",
    {
        "TargetGroupArn": str,
        "Weight": int,
    },
    total=False,
)

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": ProtocolEnumType,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": ProtocolEnumType,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": "MatcherTypeDef",
        "LoadBalancerArns": List[str],
        "TargetType": TargetTypeEnumType,
        "ProtocolVersion": str,
    },
    total=False,
)

TargetHealthDescriptionTypeDef = TypedDict(
    "TargetHealthDescriptionTypeDef",
    {
        "Target": "TargetDescriptionTypeDef",
        "HealthCheckPort": str,
        "TargetHealth": "TargetHealthTypeDef",
    },
    total=False,
)

TargetHealthTypeDef = TypedDict(
    "TargetHealthTypeDef",
    {
        "State": TargetHealthStateEnumType,
        "Reason": TargetHealthReasonEnumType,
        "Description": str,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
