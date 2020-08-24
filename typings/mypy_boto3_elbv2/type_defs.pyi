"""
Main interface for elbv2 service type definitions.

Usage::

    ```python
    from mypy_boto3_elbv2.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateTypeDef",
    "CipherTypeDef",
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
    "PathPatternConditionConfigTypeDef",
    "QueryStringConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RedirectActionConfigTypeDef",
    "RuleConditionTypeDef",
    "RuleTypeDef",
    "SourceIpConditionConfigTypeDef",
    "SslPolicyTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TargetDescriptionTypeDef",
    "TargetGroupAttributeTypeDef",
    "TargetGroupStickinessConfigTypeDef",
    "TargetGroupTupleTypeDef",
    "TargetGroupTypeDef",
    "TargetHealthDescriptionTypeDef",
    "TargetHealthTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "CreateListenerOutputTypeDef",
    "CreateLoadBalancerOutputTypeDef",
    "CreateRuleOutputTypeDef",
    "CreateTargetGroupOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "DescribeListenersOutputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "DescribeRulesOutputTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeTargetGroupAttributesOutputTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "DescribeTargetHealthOutputTypeDef",
    "ModifyListenerOutputTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "ModifyRuleOutputTypeDef",
    "ModifyTargetGroupAttributesOutputTypeDef",
    "ModifyTargetGroupOutputTypeDef",
    "PaginatorConfigTypeDef",
    "RulePriorityPairTypeDef",
    "SetIpAddressTypeOutputTypeDef",
    "SetRulePrioritiesOutputTypeDef",
    "SetSecurityGroupsOutputTypeDef",
    "SetSubnetsOutputTypeDef",
    "SubnetMappingTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredActionTypeDef = TypedDict(
    "_RequiredActionTypeDef",
    {
        "Type": Literal[
            "forward", "authenticate-oidc", "authenticate-cognito", "redirect", "fixed-response"
        ]
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


_RequiredAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_RequiredAuthenticateCognitoActionConfigTypeDef",
    {"UserPoolArn": str, "UserPoolClientId": str, "UserPoolDomain": str},
)
_OptionalAuthenticateCognitoActionConfigTypeDef = TypedDict(
    "_OptionalAuthenticateCognitoActionConfigTypeDef",
    {
        "SessionCookieName": str,
        "Scope": str,
        "SessionTimeout": int,
        "AuthenticationRequestExtraParams": Dict[str, str],
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
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
        "OnUnauthenticatedRequest": Literal["deny", "allow", "authenticate"],
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
    {"ZoneName": str, "SubnetId": str, "LoadBalancerAddresses": List["LoadBalancerAddressTypeDef"]},
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef", {"CertificateArn": str, "IsDefault": bool}, total=False
)

CipherTypeDef = TypedDict("CipherTypeDef", {"Name": str, "Priority": int}, total=False)

_RequiredFixedResponseActionConfigTypeDef = TypedDict(
    "_RequiredFixedResponseActionConfigTypeDef", {"StatusCode": str}
)
_OptionalFixedResponseActionConfigTypeDef = TypedDict(
    "_OptionalFixedResponseActionConfigTypeDef",
    {"MessageBody": str, "ContentType": str},
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
    "HostHeaderConditionConfigTypeDef", {"Values": List[str]}, total=False
)

HttpHeaderConditionConfigTypeDef = TypedDict(
    "HttpHeaderConditionConfigTypeDef", {"HttpHeaderName": str, "Values": List[str]}, total=False
)

HttpRequestMethodConditionConfigTypeDef = TypedDict(
    "HttpRequestMethodConditionConfigTypeDef", {"Values": List[str]}, total=False
)

LimitTypeDef = TypedDict("LimitTypeDef", {"Name": str, "Max": str}, total=False)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Certificates": List["CertificateTypeDef"],
        "SslPolicy": str,
        "DefaultActions": List["ActionTypeDef"],
        "AlpnPolicy": List[str],
    },
    total=False,
)

LoadBalancerAddressTypeDef = TypedDict(
    "LoadBalancerAddressTypeDef",
    {"IpAddress": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)

LoadBalancerAttributeTypeDef = TypedDict(
    "LoadBalancerAttributeTypeDef", {"Key": str, "Value": str}, total=False
)

LoadBalancerStateTypeDef = TypedDict(
    "LoadBalancerStateTypeDef",
    {"Code": Literal["active", "provisioning", "active_impaired", "failed"], "Reason": str},
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
        "Scheme": Literal["internet-facing", "internal"],
        "VpcId": str,
        "State": "LoadBalancerStateTypeDef",
        "Type": Literal["application", "network"],
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "SecurityGroups": List[str],
        "IpAddressType": Literal["ipv4", "dualstack"],
    },
    total=False,
)

MatcherTypeDef = TypedDict("MatcherTypeDef", {"HttpCode": str})

PathPatternConditionConfigTypeDef = TypedDict(
    "PathPatternConditionConfigTypeDef", {"Values": List[str]}, total=False
)

QueryStringConditionConfigTypeDef = TypedDict(
    "QueryStringConditionConfigTypeDef",
    {"Values": List["QueryStringKeyValuePairTypeDef"]},
    total=False,
)

QueryStringKeyValuePairTypeDef = TypedDict(
    "QueryStringKeyValuePairTypeDef", {"Key": str, "Value": str}, total=False
)

_RequiredRedirectActionConfigTypeDef = TypedDict(
    "_RequiredRedirectActionConfigTypeDef", {"StatusCode": Literal["HTTP_301", "HTTP_302"]}
)
_OptionalRedirectActionConfigTypeDef = TypedDict(
    "_OptionalRedirectActionConfigTypeDef",
    {"Protocol": str, "Port": str, "Host": str, "Path": str, "Query": str},
    total=False,
)


class RedirectActionConfigTypeDef(
    _RequiredRedirectActionConfigTypeDef, _OptionalRedirectActionConfigTypeDef
):
    pass


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

SourceIpConditionConfigTypeDef = TypedDict(
    "SourceIpConditionConfigTypeDef", {"Values": List[str]}, total=False
)

SslPolicyTypeDef = TypedDict(
    "SslPolicyTypeDef",
    {"SslProtocols": List[str], "Ciphers": List["CipherTypeDef"], "Name": str},
    total=False,
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef", {"ResourceArn": str, "Tags": List["TagTypeDef"]}, total=False
)

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


_RequiredTargetDescriptionTypeDef = TypedDict("_RequiredTargetDescriptionTypeDef", {"Id": str})
_OptionalTargetDescriptionTypeDef = TypedDict(
    "_OptionalTargetDescriptionTypeDef", {"Port": int, "AvailabilityZone": str}, total=False
)


class TargetDescriptionTypeDef(
    _RequiredTargetDescriptionTypeDef, _OptionalTargetDescriptionTypeDef
):
    pass


TargetGroupAttributeTypeDef = TypedDict(
    "TargetGroupAttributeTypeDef", {"Key": str, "Value": str}, total=False
)

TargetGroupStickinessConfigTypeDef = TypedDict(
    "TargetGroupStickinessConfigTypeDef", {"Enabled": bool, "DurationSeconds": int}, total=False
)

TargetGroupTupleTypeDef = TypedDict(
    "TargetGroupTupleTypeDef", {"TargetGroupArn": str, "Weight": int}, total=False
)

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": Literal["HTTP", "HTTPS", "TCP", "TLS", "UDP", "TCP_UDP"],
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": "MatcherTypeDef",
        "LoadBalancerArns": List[str],
        "TargetType": Literal["instance", "ip", "lambda"],
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
        "State": Literal["initial", "healthy", "unhealthy", "unused", "draining", "unavailable"],
        "Reason": Literal[
            "Elb.RegistrationInProgress",
            "Elb.InitialHealthChecking",
            "Target.ResponseCodeMismatch",
            "Target.Timeout",
            "Target.FailedHealthChecks",
            "Target.NotRegistered",
            "Target.NotInUse",
            "Target.DeregistrationInProgress",
            "Target.InvalidState",
            "Target.IpUnusable",
            "Target.HealthCheckDisabled",
            "Elb.InternalError",
        ],
        "Description": str,
    },
    total=False,
)

AddListenerCertificatesOutputTypeDef = TypedDict(
    "AddListenerCertificatesOutputTypeDef",
    {"Certificates": List["CertificateTypeDef"]},
    total=False,
)

CreateListenerOutputTypeDef = TypedDict(
    "CreateListenerOutputTypeDef", {"Listeners": List["ListenerTypeDef"]}, total=False
)

CreateLoadBalancerOutputTypeDef = TypedDict(
    "CreateLoadBalancerOutputTypeDef", {"LoadBalancers": List["LoadBalancerTypeDef"]}, total=False
)

CreateRuleOutputTypeDef = TypedDict(
    "CreateRuleOutputTypeDef", {"Rules": List["RuleTypeDef"]}, total=False
)

CreateTargetGroupOutputTypeDef = TypedDict(
    "CreateTargetGroupOutputTypeDef", {"TargetGroups": List["TargetGroupTypeDef"]}, total=False
)

DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {"Limits": List["LimitTypeDef"], "NextMarker": str},
    total=False,
)

DescribeListenerCertificatesOutputTypeDef = TypedDict(
    "DescribeListenerCertificatesOutputTypeDef",
    {"Certificates": List["CertificateTypeDef"], "NextMarker": str},
    total=False,
)

DescribeListenersOutputTypeDef = TypedDict(
    "DescribeListenersOutputTypeDef",
    {"Listeners": List["ListenerTypeDef"], "NextMarker": str},
    total=False,
)

DescribeLoadBalancerAttributesOutputTypeDef = TypedDict(
    "DescribeLoadBalancerAttributesOutputTypeDef",
    {"Attributes": List["LoadBalancerAttributeTypeDef"]},
    total=False,
)

DescribeLoadBalancersOutputTypeDef = TypedDict(
    "DescribeLoadBalancersOutputTypeDef",
    {"LoadBalancers": List["LoadBalancerTypeDef"], "NextMarker": str},
    total=False,
)

DescribeRulesOutputTypeDef = TypedDict(
    "DescribeRulesOutputTypeDef", {"Rules": List["RuleTypeDef"], "NextMarker": str}, total=False
)

DescribeSSLPoliciesOutputTypeDef = TypedDict(
    "DescribeSSLPoliciesOutputTypeDef",
    {"SslPolicies": List["SslPolicyTypeDef"], "NextMarker": str},
    total=False,
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef", {"TagDescriptions": List["TagDescriptionTypeDef"]}, total=False
)

DescribeTargetGroupAttributesOutputTypeDef = TypedDict(
    "DescribeTargetGroupAttributesOutputTypeDef",
    {"Attributes": List["TargetGroupAttributeTypeDef"]},
    total=False,
)

DescribeTargetGroupsOutputTypeDef = TypedDict(
    "DescribeTargetGroupsOutputTypeDef",
    {"TargetGroups": List["TargetGroupTypeDef"], "NextMarker": str},
    total=False,
)

DescribeTargetHealthOutputTypeDef = TypedDict(
    "DescribeTargetHealthOutputTypeDef",
    {"TargetHealthDescriptions": List["TargetHealthDescriptionTypeDef"]},
    total=False,
)

ModifyListenerOutputTypeDef = TypedDict(
    "ModifyListenerOutputTypeDef", {"Listeners": List["ListenerTypeDef"]}, total=False
)

ModifyLoadBalancerAttributesOutputTypeDef = TypedDict(
    "ModifyLoadBalancerAttributesOutputTypeDef",
    {"Attributes": List["LoadBalancerAttributeTypeDef"]},
    total=False,
)

ModifyRuleOutputTypeDef = TypedDict(
    "ModifyRuleOutputTypeDef", {"Rules": List["RuleTypeDef"]}, total=False
)

ModifyTargetGroupAttributesOutputTypeDef = TypedDict(
    "ModifyTargetGroupAttributesOutputTypeDef",
    {"Attributes": List["TargetGroupAttributeTypeDef"]},
    total=False,
)

ModifyTargetGroupOutputTypeDef = TypedDict(
    "ModifyTargetGroupOutputTypeDef", {"TargetGroups": List["TargetGroupTypeDef"]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RulePriorityPairTypeDef = TypedDict(
    "RulePriorityPairTypeDef", {"RuleArn": str, "Priority": int}, total=False
)

SetIpAddressTypeOutputTypeDef = TypedDict(
    "SetIpAddressTypeOutputTypeDef", {"IpAddressType": Literal["ipv4", "dualstack"]}, total=False
)

SetRulePrioritiesOutputTypeDef = TypedDict(
    "SetRulePrioritiesOutputTypeDef", {"Rules": List["RuleTypeDef"]}, total=False
)

SetSecurityGroupsOutputTypeDef = TypedDict(
    "SetSecurityGroupsOutputTypeDef", {"SecurityGroupIds": List[str]}, total=False
)

SetSubnetsOutputTypeDef = TypedDict(
    "SetSubnetsOutputTypeDef", {"AvailabilityZones": List["AvailabilityZoneTypeDef"]}, total=False
)

SubnetMappingTypeDef = TypedDict(
    "SubnetMappingTypeDef",
    {"SubnetId": str, "AllocationId": str, "PrivateIPv4Address": str},
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
