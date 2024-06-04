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
    AnomalyResultEnumType,
    AuthenticateCognitoActionConditionalBehaviorEnumType,
    AuthenticateOidcActionConditionalBehaviorEnumType,
    DescribeTargetHealthInputIncludeEnumType,
    EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType,
    IpAddressTypeType,
    LoadBalancerSchemeEnumType,
    LoadBalancerStateEnumType,
    LoadBalancerTypeEnumType,
    MitigationInEffectEnumType,
    ProtocolEnumType,
    RedirectActionStatusCodeEnumType,
    TargetGroupIpAddressTypeEnumType,
    TargetHealthReasonEnumType,
    TargetHealthStateEnumType,
    TargetTypeEnumType,
    TrustStoreStatusType,
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
    "ActionTypeDef",
    "AddListenerCertificatesInputRequestTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "AddTagsInputRequestTypeDef",
    "AddTrustStoreRevocationsInputRequestTypeDef",
    "AddTrustStoreRevocationsOutputTypeDef",
    "AnomalyDetectionTypeDef",
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
    "CreateTrustStoreInputRequestTypeDef",
    "CreateTrustStoreOutputTypeDef",
    "DeleteListenerInputRequestTypeDef",
    "DeleteLoadBalancerInputRequestTypeDef",
    "DeleteRuleInputRequestTypeDef",
    "DeleteTargetGroupInputRequestTypeDef",
    "DeleteTrustStoreInputRequestTypeDef",
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
    "DescribeTrustStoreAssociationsInputRequestTypeDef",
    "DescribeTrustStoreAssociationsOutputTypeDef",
    "DescribeTrustStoreRevocationTypeDef",
    "DescribeTrustStoreRevocationsInputRequestTypeDef",
    "DescribeTrustStoreRevocationsOutputTypeDef",
    "DescribeTrustStoresInputRequestTypeDef",
    "DescribeTrustStoresOutputTypeDef",
    "FixedResponseActionConfigTypeDef",
    "ForwardActionConfigTypeDef",
    "GetTrustStoreCaCertificatesBundleInputRequestTypeDef",
    "GetTrustStoreCaCertificatesBundleOutputTypeDef",
    "GetTrustStoreRevocationContentInputRequestTypeDef",
    "GetTrustStoreRevocationContentOutputTypeDef",
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
    "ModifyTrustStoreInputRequestTypeDef",
    "ModifyTrustStoreOutputTypeDef",
    "MutualAuthenticationAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RedirectActionConfigTypeDef",
    "RegisterTargetsInputRequestTypeDef",
    "RemoveListenerCertificatesInputRequestTypeDef",
    "RemoveTagsInputRequestTypeDef",
    "RemoveTrustStoreRevocationsInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RevocationContentTypeDef",
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
    "TrustStoreAssociationTypeDef",
    "TrustStoreRevocationTypeDef",
    "TrustStoreTypeDef",
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

_RequiredAddTrustStoreRevocationsInputRequestTypeDef = TypedDict(
    "_RequiredAddTrustStoreRevocationsInputRequestTypeDef",
    {
        "TrustStoreArn": str,
    },
)
_OptionalAddTrustStoreRevocationsInputRequestTypeDef = TypedDict(
    "_OptionalAddTrustStoreRevocationsInputRequestTypeDef",
    {
        "RevocationContents": List["RevocationContentTypeDef"],
    },
    total=False,
)

class AddTrustStoreRevocationsInputRequestTypeDef(
    _RequiredAddTrustStoreRevocationsInputRequestTypeDef,
    _OptionalAddTrustStoreRevocationsInputRequestTypeDef,
):
    pass

AddTrustStoreRevocationsOutputTypeDef = TypedDict(
    "AddTrustStoreRevocationsOutputTypeDef",
    {
        "TrustStoreRevocations": List["TrustStoreRevocationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AnomalyDetectionTypeDef = TypedDict(
    "AnomalyDetectionTypeDef",
    {
        "Result": AnomalyResultEnumType,
        "MitigationInEffect": MitigationInEffectEnumType,
    },
    total=False,
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
        "MutualAuthentication": "MutualAuthenticationAttributesTypeDef",
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
        "IpAddressType": TargetGroupIpAddressTypeEnumType,
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

_RequiredCreateTrustStoreInputRequestTypeDef = TypedDict(
    "_RequiredCreateTrustStoreInputRequestTypeDef",
    {
        "Name": str,
        "CaCertificatesBundleS3Bucket": str,
        "CaCertificatesBundleS3Key": str,
    },
)
_OptionalCreateTrustStoreInputRequestTypeDef = TypedDict(
    "_OptionalCreateTrustStoreInputRequestTypeDef",
    {
        "CaCertificatesBundleS3ObjectVersion": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTrustStoreInputRequestTypeDef(
    _RequiredCreateTrustStoreInputRequestTypeDef, _OptionalCreateTrustStoreInputRequestTypeDef
):
    pass

CreateTrustStoreOutputTypeDef = TypedDict(
    "CreateTrustStoreOutputTypeDef",
    {
        "TrustStores": List["TrustStoreTypeDef"],
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

DeleteTrustStoreInputRequestTypeDef = TypedDict(
    "DeleteTrustStoreInputRequestTypeDef",
    {
        "TrustStoreArn": str,
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
        "LoadBalancerType": LoadBalancerTypeEnumType,
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
        "Include": List[DescribeTargetHealthInputIncludeEnumType],
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

_RequiredDescribeTrustStoreAssociationsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeTrustStoreAssociationsInputRequestTypeDef",
    {
        "TrustStoreArn": str,
    },
)
_OptionalDescribeTrustStoreAssociationsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeTrustStoreAssociationsInputRequestTypeDef",
    {
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

class DescribeTrustStoreAssociationsInputRequestTypeDef(
    _RequiredDescribeTrustStoreAssociationsInputRequestTypeDef,
    _OptionalDescribeTrustStoreAssociationsInputRequestTypeDef,
):
    pass

DescribeTrustStoreAssociationsOutputTypeDef = TypedDict(
    "DescribeTrustStoreAssociationsOutputTypeDef",
    {
        "TrustStoreAssociations": List["TrustStoreAssociationTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustStoreRevocationTypeDef = TypedDict(
    "DescribeTrustStoreRevocationTypeDef",
    {
        "TrustStoreArn": str,
        "RevocationId": int,
        "RevocationType": Literal["CRL"],
        "NumberOfRevokedEntries": int,
    },
    total=False,
)

_RequiredDescribeTrustStoreRevocationsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeTrustStoreRevocationsInputRequestTypeDef",
    {
        "TrustStoreArn": str,
    },
)
_OptionalDescribeTrustStoreRevocationsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeTrustStoreRevocationsInputRequestTypeDef",
    {
        "RevocationIds": List[int],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

class DescribeTrustStoreRevocationsInputRequestTypeDef(
    _RequiredDescribeTrustStoreRevocationsInputRequestTypeDef,
    _OptionalDescribeTrustStoreRevocationsInputRequestTypeDef,
):
    pass

DescribeTrustStoreRevocationsOutputTypeDef = TypedDict(
    "DescribeTrustStoreRevocationsOutputTypeDef",
    {
        "TrustStoreRevocations": List["DescribeTrustStoreRevocationTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrustStoresInputRequestTypeDef = TypedDict(
    "DescribeTrustStoresInputRequestTypeDef",
    {
        "TrustStoreArns": List[str],
        "Names": List[str],
        "Marker": str,
        "PageSize": int,
    },
    total=False,
)

DescribeTrustStoresOutputTypeDef = TypedDict(
    "DescribeTrustStoresOutputTypeDef",
    {
        "TrustStores": List["TrustStoreTypeDef"],
        "NextMarker": str,
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

GetTrustStoreCaCertificatesBundleInputRequestTypeDef = TypedDict(
    "GetTrustStoreCaCertificatesBundleInputRequestTypeDef",
    {
        "TrustStoreArn": str,
    },
)

GetTrustStoreCaCertificatesBundleOutputTypeDef = TypedDict(
    "GetTrustStoreCaCertificatesBundleOutputTypeDef",
    {
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrustStoreRevocationContentInputRequestTypeDef = TypedDict(
    "GetTrustStoreRevocationContentInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "RevocationId": int,
    },
)

GetTrustStoreRevocationContentOutputTypeDef = TypedDict(
    "GetTrustStoreRevocationContentOutputTypeDef",
    {
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "MutualAuthentication": "MutualAuthenticationAttributesTypeDef",
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
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic": str,
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
        "MutualAuthentication": "MutualAuthenticationAttributesTypeDef",
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

_RequiredModifyTrustStoreInputRequestTypeDef = TypedDict(
    "_RequiredModifyTrustStoreInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "CaCertificatesBundleS3Bucket": str,
        "CaCertificatesBundleS3Key": str,
    },
)
_OptionalModifyTrustStoreInputRequestTypeDef = TypedDict(
    "_OptionalModifyTrustStoreInputRequestTypeDef",
    {
        "CaCertificatesBundleS3ObjectVersion": str,
    },
    total=False,
)

class ModifyTrustStoreInputRequestTypeDef(
    _RequiredModifyTrustStoreInputRequestTypeDef, _OptionalModifyTrustStoreInputRequestTypeDef
):
    pass

ModifyTrustStoreOutputTypeDef = TypedDict(
    "ModifyTrustStoreOutputTypeDef",
    {
        "TrustStores": List["TrustStoreTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MutualAuthenticationAttributesTypeDef = TypedDict(
    "MutualAuthenticationAttributesTypeDef",
    {
        "Mode": str,
        "TrustStoreArn": str,
        "IgnoreClientCertificateExpiry": bool,
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

RemoveTrustStoreRevocationsInputRequestTypeDef = TypedDict(
    "RemoveTrustStoreRevocationsInputRequestTypeDef",
    {
        "TrustStoreArn": str,
        "RevocationIds": List[int],
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

RevocationContentTypeDef = TypedDict(
    "RevocationContentTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "RevocationType": Literal["CRL"],
    },
    total=False,
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

_RequiredSetSecurityGroupsInputRequestTypeDef = TypedDict(
    "_RequiredSetSecurityGroupsInputRequestTypeDef",
    {
        "LoadBalancerArn": str,
        "SecurityGroups": List[str],
    },
)
_OptionalSetSecurityGroupsInputRequestTypeDef = TypedDict(
    "_OptionalSetSecurityGroupsInputRequestTypeDef",
    {
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic": EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType,
    },
    total=False,
)

class SetSecurityGroupsInputRequestTypeDef(
    _RequiredSetSecurityGroupsInputRequestTypeDef, _OptionalSetSecurityGroupsInputRequestTypeDef
):
    pass

SetSecurityGroupsOutputTypeDef = TypedDict(
    "SetSecurityGroupsOutputTypeDef",
    {
        "SecurityGroupIds": List[str],
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic": EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType,
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
        "SupportedLoadBalancerTypes": List[str],
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
        "IpAddressType": TargetGroupIpAddressTypeEnumType,
    },
    total=False,
)

TargetHealthDescriptionTypeDef = TypedDict(
    "TargetHealthDescriptionTypeDef",
    {
        "Target": "TargetDescriptionTypeDef",
        "HealthCheckPort": str,
        "TargetHealth": "TargetHealthTypeDef",
        "AnomalyDetection": "AnomalyDetectionTypeDef",
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

TrustStoreAssociationTypeDef = TypedDict(
    "TrustStoreAssociationTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

TrustStoreRevocationTypeDef = TypedDict(
    "TrustStoreRevocationTypeDef",
    {
        "TrustStoreArn": str,
        "RevocationId": int,
        "RevocationType": Literal["CRL"],
        "NumberOfRevokedEntries": int,
    },
    total=False,
)

TrustStoreTypeDef = TypedDict(
    "TrustStoreTypeDef",
    {
        "Name": str,
        "TrustStoreArn": str,
        "Status": TrustStoreStatusType,
        "NumberOfCaCertificates": int,
        "TotalRevokedEntries": int,
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
