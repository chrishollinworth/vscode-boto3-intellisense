"""
Type annotations for elbv2 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elbv2/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_elbv2.type_defs import AuthenticateCognitoActionConfigOutputTypeDef

    data: AuthenticateCognitoActionConfigOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActionTypeEnumType,
    AdvertiseTrustStoreCaNamesEnumType,
    AnomalyResultEnumType,
    AuthenticateCognitoActionConditionalBehaviorEnumType,
    AuthenticateOidcActionConditionalBehaviorEnumType,
    CapacityReservationStateEnumType,
    DescribeTargetHealthInputIncludeEnumType,
    EnablePrefixForIpv6SourceNatEnumType,
    EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType,
    IpAddressTypeType,
    LoadBalancerSchemeEnumType,
    LoadBalancerStateEnumType,
    LoadBalancerTypeEnumType,
    MitigationInEffectEnumType,
    ProtocolEnumType,
    RedirectActionStatusCodeEnumType,
    TargetAdministrativeOverrideReasonEnumType,
    TargetAdministrativeOverrideStateEnumType,
    TargetGroupIpAddressTypeEnumType,
    TargetHealthReasonEnumType,
    TargetHealthStateEnumType,
    TargetTypeEnumType,
    TrustStoreAssociationStatusEnumType,
    TrustStoreStatusType,
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
    "ActionOutputTypeDef",
    "ActionTypeDef",
    "ActionUnionTypeDef",
    "AddListenerCertificatesInputTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "AddTagsInputTypeDef",
    "AddTrustStoreRevocationsInputTypeDef",
    "AddTrustStoreRevocationsOutputTypeDef",
    "AdministrativeOverrideTypeDef",
    "AnomalyDetectionTypeDef",
    "AuthenticateCognitoActionConfigOutputTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateCognitoActionConfigUnionTypeDef",
    "AuthenticateOidcActionConfigOutputTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "AuthenticateOidcActionConfigUnionTypeDef",
    "AvailabilityZoneTypeDef",
    "CapacityReservationStatusTypeDef",
    "CertificateTypeDef",
    "CipherTypeDef",
    "CreateListenerInputTypeDef",
    "CreateListenerOutputTypeDef",
    "CreateLoadBalancerInputTypeDef",
    "CreateLoadBalancerOutputTypeDef",
    "CreateRuleInputTypeDef",
    "CreateRuleOutputTypeDef",
    "CreateTargetGroupInputTypeDef",
    "CreateTargetGroupOutputTypeDef",
    "CreateTrustStoreInputTypeDef",
    "CreateTrustStoreOutputTypeDef",
    "DeleteListenerInputTypeDef",
    "DeleteLoadBalancerInputTypeDef",
    "DeleteRuleInputTypeDef",
    "DeleteSharedTrustStoreAssociationInputTypeDef",
    "DeleteTargetGroupInputTypeDef",
    "DeleteTrustStoreInputTypeDef",
    "DeregisterTargetsInputTypeDef",
    "DescribeAccountLimitsInputPaginateTypeDef",
    "DescribeAccountLimitsInputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeCapacityReservationInputTypeDef",
    "DescribeCapacityReservationOutputTypeDef",
    "DescribeListenerAttributesInputTypeDef",
    "DescribeListenerAttributesOutputTypeDef",
    "DescribeListenerCertificatesInputPaginateTypeDef",
    "DescribeListenerCertificatesInputTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "DescribeListenersInputPaginateTypeDef",
    "DescribeListenersInputTypeDef",
    "DescribeListenersOutputTypeDef",
    "DescribeLoadBalancerAttributesInputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancersInputPaginateTypeDef",
    "DescribeLoadBalancersInputTypeDef",
    "DescribeLoadBalancersInputWaitExtraExtraTypeDef",
    "DescribeLoadBalancersInputWaitExtraTypeDef",
    "DescribeLoadBalancersInputWaitTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "DescribeRulesInputPaginateTypeDef",
    "DescribeRulesInputTypeDef",
    "DescribeRulesOutputTypeDef",
    "DescribeSSLPoliciesInputPaginateTypeDef",
    "DescribeSSLPoliciesInputTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "DescribeTagsInputTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeTargetGroupAttributesInputTypeDef",
    "DescribeTargetGroupAttributesOutputTypeDef",
    "DescribeTargetGroupsInputPaginateTypeDef",
    "DescribeTargetGroupsInputTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "DescribeTargetHealthInputTypeDef",
    "DescribeTargetHealthInputWaitExtraTypeDef",
    "DescribeTargetHealthInputWaitTypeDef",
    "DescribeTargetHealthOutputTypeDef",
    "DescribeTrustStoreAssociationsInputTypeDef",
    "DescribeTrustStoreAssociationsOutputTypeDef",
    "DescribeTrustStoreRevocationTypeDef",
    "DescribeTrustStoreRevocationsInputTypeDef",
    "DescribeTrustStoreRevocationsOutputTypeDef",
    "DescribeTrustStoresInputTypeDef",
    "DescribeTrustStoresOutputTypeDef",
    "FixedResponseActionConfigTypeDef",
    "ForwardActionConfigOutputTypeDef",
    "ForwardActionConfigTypeDef",
    "ForwardActionConfigUnionTypeDef",
    "GetResourcePolicyInputTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GetTrustStoreCaCertificatesBundleInputTypeDef",
    "GetTrustStoreCaCertificatesBundleOutputTypeDef",
    "GetTrustStoreRevocationContentInputTypeDef",
    "GetTrustStoreRevocationContentOutputTypeDef",
    "HostHeaderConditionConfigOutputTypeDef",
    "HostHeaderConditionConfigTypeDef",
    "HostHeaderConditionConfigUnionTypeDef",
    "HttpHeaderConditionConfigOutputTypeDef",
    "HttpHeaderConditionConfigTypeDef",
    "HttpHeaderConditionConfigUnionTypeDef",
    "HttpRequestMethodConditionConfigOutputTypeDef",
    "HttpRequestMethodConditionConfigTypeDef",
    "HttpRequestMethodConditionConfigUnionTypeDef",
    "IpamPoolsTypeDef",
    "LimitTypeDef",
    "ListenerAttributeTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAddressTypeDef",
    "LoadBalancerAttributeTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTypeDef",
    "MatcherTypeDef",
    "MinimumLoadBalancerCapacityTypeDef",
    "ModifyCapacityReservationInputTypeDef",
    "ModifyCapacityReservationOutputTypeDef",
    "ModifyIpPoolsInputTypeDef",
    "ModifyIpPoolsOutputTypeDef",
    "ModifyListenerAttributesInputTypeDef",
    "ModifyListenerAttributesOutputTypeDef",
    "ModifyListenerInputTypeDef",
    "ModifyListenerOutputTypeDef",
    "ModifyLoadBalancerAttributesInputTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "ModifyRuleInputTypeDef",
    "ModifyRuleOutputTypeDef",
    "ModifyTargetGroupAttributesInputTypeDef",
    "ModifyTargetGroupAttributesOutputTypeDef",
    "ModifyTargetGroupInputTypeDef",
    "ModifyTargetGroupOutputTypeDef",
    "ModifyTrustStoreInputTypeDef",
    "ModifyTrustStoreOutputTypeDef",
    "MutualAuthenticationAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "PathPatternConditionConfigOutputTypeDef",
    "PathPatternConditionConfigTypeDef",
    "PathPatternConditionConfigUnionTypeDef",
    "QueryStringConditionConfigOutputTypeDef",
    "QueryStringConditionConfigTypeDef",
    "QueryStringConditionConfigUnionTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RedirectActionConfigTypeDef",
    "RegisterTargetsInputTypeDef",
    "RemoveListenerCertificatesInputTypeDef",
    "RemoveTagsInputTypeDef",
    "RemoveTrustStoreRevocationsInputTypeDef",
    "ResponseMetadataTypeDef",
    "RevocationContentTypeDef",
    "RuleConditionOutputTypeDef",
    "RuleConditionTypeDef",
    "RuleConditionUnionTypeDef",
    "RulePriorityPairTypeDef",
    "RuleTypeDef",
    "SetIpAddressTypeInputTypeDef",
    "SetIpAddressTypeOutputTypeDef",
    "SetRulePrioritiesInputTypeDef",
    "SetRulePrioritiesOutputTypeDef",
    "SetSecurityGroupsInputTypeDef",
    "SetSecurityGroupsOutputTypeDef",
    "SetSubnetsInputTypeDef",
    "SetSubnetsOutputTypeDef",
    "SourceIpConditionConfigOutputTypeDef",
    "SourceIpConditionConfigTypeDef",
    "SourceIpConditionConfigUnionTypeDef",
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
    "ZonalCapacityReservationStateTypeDef",
)

class AuthenticateCognitoActionConfigOutputTypeDef(TypedDict):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: NotRequired[str]
    Scope: NotRequired[str]
    SessionTimeout: NotRequired[int]
    AuthenticationRequestExtraParams: NotRequired[Dict[str, str]]
    OnUnauthenticatedRequest: NotRequired[AuthenticateCognitoActionConditionalBehaviorEnumType]

class AuthenticateOidcActionConfigOutputTypeDef(TypedDict):
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    ClientId: str
    ClientSecret: NotRequired[str]
    SessionCookieName: NotRequired[str]
    Scope: NotRequired[str]
    SessionTimeout: NotRequired[int]
    AuthenticationRequestExtraParams: NotRequired[Dict[str, str]]
    OnUnauthenticatedRequest: NotRequired[AuthenticateOidcActionConditionalBehaviorEnumType]
    UseExistingClientSecret: NotRequired[bool]

class FixedResponseActionConfigTypeDef(TypedDict):
    StatusCode: str
    MessageBody: NotRequired[str]
    ContentType: NotRequired[str]

RedirectActionConfigTypeDef = TypedDict(
    "RedirectActionConfigTypeDef",
    {
        "StatusCode": RedirectActionStatusCodeEnumType,
        "Protocol": NotRequired[str],
        "Port": NotRequired[str],
        "Host": NotRequired[str],
        "Path": NotRequired[str],
        "Query": NotRequired[str],
    },
)

class CertificateTypeDef(TypedDict):
    CertificateArn: NotRequired[str]
    IsDefault: NotRequired[bool]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: NotRequired[str]

class RevocationContentTypeDef(TypedDict):
    S3Bucket: NotRequired[str]
    S3Key: NotRequired[str]
    S3ObjectVersion: NotRequired[str]
    RevocationType: NotRequired[Literal["CRL"]]

class TrustStoreRevocationTypeDef(TypedDict):
    TrustStoreArn: NotRequired[str]
    RevocationId: NotRequired[int]
    RevocationType: NotRequired[Literal["CRL"]]
    NumberOfRevokedEntries: NotRequired[int]

class AdministrativeOverrideTypeDef(TypedDict):
    State: NotRequired[TargetAdministrativeOverrideStateEnumType]
    Reason: NotRequired[TargetAdministrativeOverrideReasonEnumType]
    Description: NotRequired[str]

class AnomalyDetectionTypeDef(TypedDict):
    Result: NotRequired[AnomalyResultEnumType]
    MitigationInEffect: NotRequired[MitigationInEffectEnumType]

class AuthenticateCognitoActionConfigTypeDef(TypedDict):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str
    SessionCookieName: NotRequired[str]
    Scope: NotRequired[str]
    SessionTimeout: NotRequired[int]
    AuthenticationRequestExtraParams: NotRequired[Mapping[str, str]]
    OnUnauthenticatedRequest: NotRequired[AuthenticateCognitoActionConditionalBehaviorEnumType]

class AuthenticateOidcActionConfigTypeDef(TypedDict):
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    ClientId: str
    ClientSecret: NotRequired[str]
    SessionCookieName: NotRequired[str]
    Scope: NotRequired[str]
    SessionTimeout: NotRequired[int]
    AuthenticationRequestExtraParams: NotRequired[Mapping[str, str]]
    OnUnauthenticatedRequest: NotRequired[AuthenticateOidcActionConditionalBehaviorEnumType]
    UseExistingClientSecret: NotRequired[bool]

class LoadBalancerAddressTypeDef(TypedDict):
    IpAddress: NotRequired[str]
    AllocationId: NotRequired[str]
    PrivateIPv4Address: NotRequired[str]
    IPv6Address: NotRequired[str]

class CapacityReservationStatusTypeDef(TypedDict):
    Code: NotRequired[CapacityReservationStateEnumType]
    Reason: NotRequired[str]

class CipherTypeDef(TypedDict):
    Name: NotRequired[str]
    Priority: NotRequired[int]

class MutualAuthenticationAttributesTypeDef(TypedDict):
    Mode: NotRequired[str]
    TrustStoreArn: NotRequired[str]
    IgnoreClientCertificateExpiry: NotRequired[bool]
    TrustStoreAssociationStatus: NotRequired[TrustStoreAssociationStatusEnumType]
    AdvertiseTrustStoreCaNames: NotRequired[AdvertiseTrustStoreCaNamesEnumType]

class IpamPoolsTypeDef(TypedDict):
    Ipv4IpamPoolId: NotRequired[str]

class SubnetMappingTypeDef(TypedDict):
    SubnetId: NotRequired[str]
    AllocationId: NotRequired[str]
    PrivateIPv4Address: NotRequired[str]
    IPv6Address: NotRequired[str]
    SourceNatIpv6Prefix: NotRequired[str]

class MatcherTypeDef(TypedDict):
    HttpCode: NotRequired[str]
    GrpcCode: NotRequired[str]

class TrustStoreTypeDef(TypedDict):
    Name: NotRequired[str]
    TrustStoreArn: NotRequired[str]
    Status: NotRequired[TrustStoreStatusType]
    NumberOfCaCertificates: NotRequired[int]
    TotalRevokedEntries: NotRequired[int]

class DeleteListenerInputTypeDef(TypedDict):
    ListenerArn: str

class DeleteLoadBalancerInputTypeDef(TypedDict):
    LoadBalancerArn: str

class DeleteRuleInputTypeDef(TypedDict):
    RuleArn: str

class DeleteSharedTrustStoreAssociationInputTypeDef(TypedDict):
    TrustStoreArn: str
    ResourceArn: str

class DeleteTargetGroupInputTypeDef(TypedDict):
    TargetGroupArn: str

class DeleteTrustStoreInputTypeDef(TypedDict):
    TrustStoreArn: str

class TargetDescriptionTypeDef(TypedDict):
    Id: str
    Port: NotRequired[int]
    AvailabilityZone: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeAccountLimitsInputTypeDef(TypedDict):
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class LimitTypeDef(TypedDict):
    Name: NotRequired[str]
    Max: NotRequired[str]

class DescribeCapacityReservationInputTypeDef(TypedDict):
    LoadBalancerArn: str

class MinimumLoadBalancerCapacityTypeDef(TypedDict):
    CapacityUnits: NotRequired[int]

class DescribeListenerAttributesInputTypeDef(TypedDict):
    ListenerArn: str

class ListenerAttributeTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class DescribeListenerCertificatesInputTypeDef(TypedDict):
    ListenerArn: str
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class DescribeListenersInputTypeDef(TypedDict):
    LoadBalancerArn: NotRequired[str]
    ListenerArns: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class DescribeLoadBalancerAttributesInputTypeDef(TypedDict):
    LoadBalancerArn: str

class LoadBalancerAttributeTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class DescribeLoadBalancersInputTypeDef(TypedDict):
    LoadBalancerArns: NotRequired[Sequence[str]]
    Names: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeRulesInputTypeDef(TypedDict):
    ListenerArn: NotRequired[str]
    RuleArns: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class DescribeSSLPoliciesInputTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]
    LoadBalancerType: NotRequired[LoadBalancerTypeEnumType]

class DescribeTagsInputTypeDef(TypedDict):
    ResourceArns: Sequence[str]

class DescribeTargetGroupAttributesInputTypeDef(TypedDict):
    TargetGroupArn: str

class TargetGroupAttributeTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class DescribeTargetGroupsInputTypeDef(TypedDict):
    LoadBalancerArn: NotRequired[str]
    TargetGroupArns: NotRequired[Sequence[str]]
    Names: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class DescribeTrustStoreAssociationsInputTypeDef(TypedDict):
    TrustStoreArn: str
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class TrustStoreAssociationTypeDef(TypedDict):
    ResourceArn: NotRequired[str]

class DescribeTrustStoreRevocationTypeDef(TypedDict):
    TrustStoreArn: NotRequired[str]
    RevocationId: NotRequired[int]
    RevocationType: NotRequired[Literal["CRL"]]
    NumberOfRevokedEntries: NotRequired[int]

class DescribeTrustStoreRevocationsInputTypeDef(TypedDict):
    TrustStoreArn: str
    RevocationIds: NotRequired[Sequence[int]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class DescribeTrustStoresInputTypeDef(TypedDict):
    TrustStoreArns: NotRequired[Sequence[str]]
    Names: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]

class TargetGroupStickinessConfigTypeDef(TypedDict):
    Enabled: NotRequired[bool]
    DurationSeconds: NotRequired[int]

class TargetGroupTupleTypeDef(TypedDict):
    TargetGroupArn: NotRequired[str]
    Weight: NotRequired[int]

class GetResourcePolicyInputTypeDef(TypedDict):
    ResourceArn: str

class GetTrustStoreCaCertificatesBundleInputTypeDef(TypedDict):
    TrustStoreArn: str

class GetTrustStoreRevocationContentInputTypeDef(TypedDict):
    TrustStoreArn: str
    RevocationId: int

class HostHeaderConditionConfigOutputTypeDef(TypedDict):
    Values: NotRequired[List[str]]

class HostHeaderConditionConfigTypeDef(TypedDict):
    Values: NotRequired[Sequence[str]]

class HttpHeaderConditionConfigOutputTypeDef(TypedDict):
    HttpHeaderName: NotRequired[str]
    Values: NotRequired[List[str]]

class HttpHeaderConditionConfigTypeDef(TypedDict):
    HttpHeaderName: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class HttpRequestMethodConditionConfigOutputTypeDef(TypedDict):
    Values: NotRequired[List[str]]

class HttpRequestMethodConditionConfigTypeDef(TypedDict):
    Values: NotRequired[Sequence[str]]

class LoadBalancerStateTypeDef(TypedDict):
    Code: NotRequired[LoadBalancerStateEnumType]
    Reason: NotRequired[str]

class ModifyTrustStoreInputTypeDef(TypedDict):
    TrustStoreArn: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: NotRequired[str]

class PathPatternConditionConfigOutputTypeDef(TypedDict):
    Values: NotRequired[List[str]]

class PathPatternConditionConfigTypeDef(TypedDict):
    Values: NotRequired[Sequence[str]]

class QueryStringKeyValuePairTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class RemoveTagsInputTypeDef(TypedDict):
    ResourceArns: Sequence[str]
    TagKeys: Sequence[str]

class RemoveTrustStoreRevocationsInputTypeDef(TypedDict):
    TrustStoreArn: str
    RevocationIds: Sequence[int]

class SourceIpConditionConfigOutputTypeDef(TypedDict):
    Values: NotRequired[List[str]]

class RulePriorityPairTypeDef(TypedDict):
    RuleArn: NotRequired[str]
    Priority: NotRequired[int]

class SetIpAddressTypeInputTypeDef(TypedDict):
    LoadBalancerArn: str
    IpAddressType: IpAddressTypeType

class SetSecurityGroupsInputTypeDef(TypedDict):
    LoadBalancerArn: str
    SecurityGroups: Sequence[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: NotRequired[
        EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType
    ]

class SourceIpConditionConfigTypeDef(TypedDict):
    Values: NotRequired[Sequence[str]]

class TargetHealthTypeDef(TypedDict):
    State: NotRequired[TargetHealthStateEnumType]
    Reason: NotRequired[TargetHealthReasonEnumType]
    Description: NotRequired[str]

class AddListenerCertificatesInputTypeDef(TypedDict):
    ListenerArn: str
    Certificates: Sequence[CertificateTypeDef]

class RemoveListenerCertificatesInputTypeDef(TypedDict):
    ListenerArn: str
    Certificates: Sequence[CertificateTypeDef]

class AddListenerCertificatesOutputTypeDef(TypedDict):
    Certificates: List[CertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeListenerCertificatesOutputTypeDef(TypedDict):
    Certificates: List[CertificateTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyOutputTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreCaCertificatesBundleOutputTypeDef(TypedDict):
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrustStoreRevocationContentOutputTypeDef(TypedDict):
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetIpAddressTypeOutputTypeDef(TypedDict):
    IpAddressType: IpAddressTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class SetSecurityGroupsOutputTypeDef(TypedDict):
    SecurityGroupIds: List[str]
    EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic: (
        EnforceSecurityGroupInboundRulesOnPrivateLinkTrafficEnumType
    )
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsInputTypeDef(TypedDict):
    ResourceArns: Sequence[str]
    Tags: Sequence[TagTypeDef]

class CreateTrustStoreInputTypeDef(TypedDict):
    Name: str
    CaCertificatesBundleS3Bucket: str
    CaCertificatesBundleS3Key: str
    CaCertificatesBundleS3ObjectVersion: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class TagDescriptionTypeDef(TypedDict):
    ResourceArn: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class AddTrustStoreRevocationsInputTypeDef(TypedDict):
    TrustStoreArn: str
    RevocationContents: NotRequired[Sequence[RevocationContentTypeDef]]

class AddTrustStoreRevocationsOutputTypeDef(TypedDict):
    TrustStoreRevocations: List[TrustStoreRevocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

AuthenticateCognitoActionConfigUnionTypeDef = Union[
    AuthenticateCognitoActionConfigTypeDef, AuthenticateCognitoActionConfigOutputTypeDef
]
AuthenticateOidcActionConfigUnionTypeDef = Union[
    AuthenticateOidcActionConfigTypeDef, AuthenticateOidcActionConfigOutputTypeDef
]

class AvailabilityZoneTypeDef(TypedDict):
    ZoneName: NotRequired[str]
    SubnetId: NotRequired[str]
    OutpostId: NotRequired[str]
    LoadBalancerAddresses: NotRequired[List[LoadBalancerAddressTypeDef]]
    SourceNatIpv6Prefixes: NotRequired[List[str]]

class ZonalCapacityReservationStateTypeDef(TypedDict):
    State: NotRequired[CapacityReservationStatusTypeDef]
    AvailabilityZone: NotRequired[str]
    EffectiveCapacityUnits: NotRequired[float]

class SslPolicyTypeDef(TypedDict):
    SslProtocols: NotRequired[List[str]]
    Ciphers: NotRequired[List[CipherTypeDef]]
    Name: NotRequired[str]
    SupportedLoadBalancerTypes: NotRequired[List[str]]

class ModifyIpPoolsInputTypeDef(TypedDict):
    LoadBalancerArn: str
    IpamPools: NotRequired[IpamPoolsTypeDef]
    RemoveIpamPools: NotRequired[Sequence[Literal["ipv4"]]]

class ModifyIpPoolsOutputTypeDef(TypedDict):
    IpamPools: IpamPoolsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CreateLoadBalancerInputTypeDef = TypedDict(
    "CreateLoadBalancerInputTypeDef",
    {
        "Name": str,
        "Subnets": NotRequired[Sequence[str]],
        "SubnetMappings": NotRequired[Sequence[SubnetMappingTypeDef]],
        "SecurityGroups": NotRequired[Sequence[str]],
        "Scheme": NotRequired[LoadBalancerSchemeEnumType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "Type": NotRequired[LoadBalancerTypeEnumType],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "EnablePrefixForIpv6SourceNat": NotRequired[EnablePrefixForIpv6SourceNatEnumType],
        "IpamPools": NotRequired[IpamPoolsTypeDef],
    },
)

class SetSubnetsInputTypeDef(TypedDict):
    LoadBalancerArn: str
    Subnets: NotRequired[Sequence[str]]
    SubnetMappings: NotRequired[Sequence[SubnetMappingTypeDef]]
    IpAddressType: NotRequired[IpAddressTypeType]
    EnablePrefixForIpv6SourceNat: NotRequired[EnablePrefixForIpv6SourceNatEnumType]

CreateTargetGroupInputTypeDef = TypedDict(
    "CreateTargetGroupInputTypeDef",
    {
        "Name": str,
        "Protocol": NotRequired[ProtocolEnumType],
        "ProtocolVersion": NotRequired[str],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "HealthCheckProtocol": NotRequired[ProtocolEnumType],
        "HealthCheckPort": NotRequired[str],
        "HealthCheckEnabled": NotRequired[bool],
        "HealthCheckPath": NotRequired[str],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "HealthCheckTimeoutSeconds": NotRequired[int],
        "HealthyThresholdCount": NotRequired[int],
        "UnhealthyThresholdCount": NotRequired[int],
        "Matcher": NotRequired[MatcherTypeDef],
        "TargetType": NotRequired[TargetTypeEnumType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "IpAddressType": NotRequired[TargetGroupIpAddressTypeEnumType],
    },
)

class ModifyTargetGroupInputTypeDef(TypedDict):
    TargetGroupArn: str
    HealthCheckProtocol: NotRequired[ProtocolEnumType]
    HealthCheckPort: NotRequired[str]
    HealthCheckPath: NotRequired[str]
    HealthCheckEnabled: NotRequired[bool]
    HealthCheckIntervalSeconds: NotRequired[int]
    HealthCheckTimeoutSeconds: NotRequired[int]
    HealthyThresholdCount: NotRequired[int]
    UnhealthyThresholdCount: NotRequired[int]
    Matcher: NotRequired[MatcherTypeDef]

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": NotRequired[str],
        "TargetGroupName": NotRequired[str],
        "Protocol": NotRequired[ProtocolEnumType],
        "Port": NotRequired[int],
        "VpcId": NotRequired[str],
        "HealthCheckProtocol": NotRequired[ProtocolEnumType],
        "HealthCheckPort": NotRequired[str],
        "HealthCheckEnabled": NotRequired[bool],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "HealthCheckTimeoutSeconds": NotRequired[int],
        "HealthyThresholdCount": NotRequired[int],
        "UnhealthyThresholdCount": NotRequired[int],
        "HealthCheckPath": NotRequired[str],
        "Matcher": NotRequired[MatcherTypeDef],
        "LoadBalancerArns": NotRequired[List[str]],
        "TargetType": NotRequired[TargetTypeEnumType],
        "ProtocolVersion": NotRequired[str],
        "IpAddressType": NotRequired[TargetGroupIpAddressTypeEnumType],
    },
)

class CreateTrustStoreOutputTypeDef(TypedDict):
    TrustStores: List[TrustStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustStoresOutputTypeDef(TypedDict):
    TrustStores: List[TrustStoreTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTrustStoreOutputTypeDef(TypedDict):
    TrustStores: List[TrustStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTargetsInputTypeDef(TypedDict):
    TargetGroupArn: str
    Targets: Sequence[TargetDescriptionTypeDef]

class DescribeTargetHealthInputTypeDef(TypedDict):
    TargetGroupArn: str
    Targets: NotRequired[Sequence[TargetDescriptionTypeDef]]
    Include: NotRequired[Sequence[DescribeTargetHealthInputIncludeEnumType]]

class RegisterTargetsInputTypeDef(TypedDict):
    TargetGroupArn: str
    Targets: Sequence[TargetDescriptionTypeDef]

class DescribeAccountLimitsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeListenerCertificatesInputPaginateTypeDef(TypedDict):
    ListenerArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeListenersInputPaginateTypeDef(TypedDict):
    LoadBalancerArn: NotRequired[str]
    ListenerArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeLoadBalancersInputPaginateTypeDef(TypedDict):
    LoadBalancerArns: NotRequired[Sequence[str]]
    Names: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeRulesInputPaginateTypeDef(TypedDict):
    ListenerArn: NotRequired[str]
    RuleArns: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSSLPoliciesInputPaginateTypeDef(TypedDict):
    Names: NotRequired[Sequence[str]]
    LoadBalancerType: NotRequired[LoadBalancerTypeEnumType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTargetGroupsInputPaginateTypeDef(TypedDict):
    LoadBalancerArn: NotRequired[str]
    TargetGroupArns: NotRequired[Sequence[str]]
    Names: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAccountLimitsOutputTypeDef(TypedDict):
    Limits: List[LimitTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCapacityReservationInputTypeDef(TypedDict):
    LoadBalancerArn: str
    MinimumLoadBalancerCapacity: NotRequired[MinimumLoadBalancerCapacityTypeDef]
    ResetCapacityReservation: NotRequired[bool]

class DescribeListenerAttributesOutputTypeDef(TypedDict):
    Attributes: List[ListenerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyListenerAttributesInputTypeDef(TypedDict):
    ListenerArn: str
    Attributes: Sequence[ListenerAttributeTypeDef]

class ModifyListenerAttributesOutputTypeDef(TypedDict):
    Attributes: List[ListenerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancerAttributesOutputTypeDef(TypedDict):
    Attributes: List[LoadBalancerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLoadBalancerAttributesInputTypeDef(TypedDict):
    LoadBalancerArn: str
    Attributes: Sequence[LoadBalancerAttributeTypeDef]

class ModifyLoadBalancerAttributesOutputTypeDef(TypedDict):
    Attributes: List[LoadBalancerAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancersInputWaitExtraExtraTypeDef(TypedDict):
    LoadBalancerArns: NotRequired[Sequence[str]]
    Names: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeLoadBalancersInputWaitExtraTypeDef(TypedDict):
    LoadBalancerArns: NotRequired[Sequence[str]]
    Names: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeLoadBalancersInputWaitTypeDef(TypedDict):
    LoadBalancerArns: NotRequired[Sequence[str]]
    Names: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    PageSize: NotRequired[int]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeTargetHealthInputWaitExtraTypeDef(TypedDict):
    TargetGroupArn: str
    Targets: NotRequired[Sequence[TargetDescriptionTypeDef]]
    Include: NotRequired[Sequence[DescribeTargetHealthInputIncludeEnumType]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeTargetHealthInputWaitTypeDef(TypedDict):
    TargetGroupArn: str
    Targets: NotRequired[Sequence[TargetDescriptionTypeDef]]
    Include: NotRequired[Sequence[DescribeTargetHealthInputIncludeEnumType]]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class DescribeTargetGroupAttributesOutputTypeDef(TypedDict):
    Attributes: List[TargetGroupAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTargetGroupAttributesInputTypeDef(TypedDict):
    TargetGroupArn: str
    Attributes: Sequence[TargetGroupAttributeTypeDef]

class ModifyTargetGroupAttributesOutputTypeDef(TypedDict):
    Attributes: List[TargetGroupAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustStoreAssociationsOutputTypeDef(TypedDict):
    TrustStoreAssociations: List[TrustStoreAssociationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrustStoreRevocationsOutputTypeDef(TypedDict):
    TrustStoreRevocations: List[DescribeTrustStoreRevocationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ForwardActionConfigOutputTypeDef(TypedDict):
    TargetGroups: NotRequired[List[TargetGroupTupleTypeDef]]
    TargetGroupStickinessConfig: NotRequired[TargetGroupStickinessConfigTypeDef]

class ForwardActionConfigTypeDef(TypedDict):
    TargetGroups: NotRequired[Sequence[TargetGroupTupleTypeDef]]
    TargetGroupStickinessConfig: NotRequired[TargetGroupStickinessConfigTypeDef]

HostHeaderConditionConfigUnionTypeDef = Union[
    HostHeaderConditionConfigTypeDef, HostHeaderConditionConfigOutputTypeDef
]
HttpHeaderConditionConfigUnionTypeDef = Union[
    HttpHeaderConditionConfigTypeDef, HttpHeaderConditionConfigOutputTypeDef
]
HttpRequestMethodConditionConfigUnionTypeDef = Union[
    HttpRequestMethodConditionConfigTypeDef, HttpRequestMethodConditionConfigOutputTypeDef
]
PathPatternConditionConfigUnionTypeDef = Union[
    PathPatternConditionConfigTypeDef, PathPatternConditionConfigOutputTypeDef
]

class QueryStringConditionConfigOutputTypeDef(TypedDict):
    Values: NotRequired[List[QueryStringKeyValuePairTypeDef]]

class QueryStringConditionConfigTypeDef(TypedDict):
    Values: NotRequired[Sequence[QueryStringKeyValuePairTypeDef]]

class SetRulePrioritiesInputTypeDef(TypedDict):
    RulePriorities: Sequence[RulePriorityPairTypeDef]

SourceIpConditionConfigUnionTypeDef = Union[
    SourceIpConditionConfigTypeDef, SourceIpConditionConfigOutputTypeDef
]

class TargetHealthDescriptionTypeDef(TypedDict):
    Target: NotRequired[TargetDescriptionTypeDef]
    HealthCheckPort: NotRequired[str]
    TargetHealth: NotRequired[TargetHealthTypeDef]
    AnomalyDetection: NotRequired[AnomalyDetectionTypeDef]
    AdministrativeOverride: NotRequired[AdministrativeOverrideTypeDef]

class DescribeTagsOutputTypeDef(TypedDict):
    TagDescriptions: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "LoadBalancerArn": NotRequired[str],
        "DNSName": NotRequired[str],
        "CanonicalHostedZoneId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LoadBalancerName": NotRequired[str],
        "Scheme": NotRequired[LoadBalancerSchemeEnumType],
        "VpcId": NotRequired[str],
        "State": NotRequired[LoadBalancerStateTypeDef],
        "Type": NotRequired[LoadBalancerTypeEnumType],
        "AvailabilityZones": NotRequired[List[AvailabilityZoneTypeDef]],
        "SecurityGroups": NotRequired[List[str]],
        "IpAddressType": NotRequired[IpAddressTypeType],
        "CustomerOwnedIpv4Pool": NotRequired[str],
        "EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic": NotRequired[str],
        "EnablePrefixForIpv6SourceNat": NotRequired[EnablePrefixForIpv6SourceNatEnumType],
        "IpamPools": NotRequired[IpamPoolsTypeDef],
    },
)

class SetSubnetsOutputTypeDef(TypedDict):
    AvailabilityZones: List[AvailabilityZoneTypeDef]
    IpAddressType: IpAddressTypeType
    EnablePrefixForIpv6SourceNat: EnablePrefixForIpv6SourceNatEnumType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCapacityReservationOutputTypeDef(TypedDict):
    LastModifiedTime: datetime
    DecreaseRequestsRemaining: int
    MinimumLoadBalancerCapacity: MinimumLoadBalancerCapacityTypeDef
    CapacityReservationState: List[ZonalCapacityReservationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCapacityReservationOutputTypeDef(TypedDict):
    LastModifiedTime: datetime
    DecreaseRequestsRemaining: int
    MinimumLoadBalancerCapacity: MinimumLoadBalancerCapacityTypeDef
    CapacityReservationState: List[ZonalCapacityReservationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSSLPoliciesOutputTypeDef(TypedDict):
    SslPolicies: List[SslPolicyTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTargetGroupOutputTypeDef(TypedDict):
    TargetGroups: List[TargetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTargetGroupsOutputTypeDef(TypedDict):
    TargetGroups: List[TargetGroupTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyTargetGroupOutputTypeDef(TypedDict):
    TargetGroups: List[TargetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ActionOutputTypeDef = TypedDict(
    "ActionOutputTypeDef",
    {
        "Type": ActionTypeEnumType,
        "TargetGroupArn": NotRequired[str],
        "AuthenticateOidcConfig": NotRequired[AuthenticateOidcActionConfigOutputTypeDef],
        "AuthenticateCognitoConfig": NotRequired[AuthenticateCognitoActionConfigOutputTypeDef],
        "Order": NotRequired[int],
        "RedirectConfig": NotRequired[RedirectActionConfigTypeDef],
        "FixedResponseConfig": NotRequired[FixedResponseActionConfigTypeDef],
        "ForwardConfig": NotRequired[ForwardActionConfigOutputTypeDef],
    },
)
ForwardActionConfigUnionTypeDef = Union[
    ForwardActionConfigTypeDef, ForwardActionConfigOutputTypeDef
]

class RuleConditionOutputTypeDef(TypedDict):
    Field: NotRequired[str]
    Values: NotRequired[List[str]]
    HostHeaderConfig: NotRequired[HostHeaderConditionConfigOutputTypeDef]
    PathPatternConfig: NotRequired[PathPatternConditionConfigOutputTypeDef]
    HttpHeaderConfig: NotRequired[HttpHeaderConditionConfigOutputTypeDef]
    QueryStringConfig: NotRequired[QueryStringConditionConfigOutputTypeDef]
    HttpRequestMethodConfig: NotRequired[HttpRequestMethodConditionConfigOutputTypeDef]
    SourceIpConfig: NotRequired[SourceIpConditionConfigOutputTypeDef]

QueryStringConditionConfigUnionTypeDef = Union[
    QueryStringConditionConfigTypeDef, QueryStringConditionConfigOutputTypeDef
]

class DescribeTargetHealthOutputTypeDef(TypedDict):
    TargetHealthDescriptions: List[TargetHealthDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoadBalancerOutputTypeDef(TypedDict):
    LoadBalancers: List[LoadBalancerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLoadBalancersOutputTypeDef(TypedDict):
    LoadBalancers: List[LoadBalancerTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "LoadBalancerArn": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolEnumType],
        "Certificates": NotRequired[List[CertificateTypeDef]],
        "SslPolicy": NotRequired[str],
        "DefaultActions": NotRequired[List[ActionOutputTypeDef]],
        "AlpnPolicy": NotRequired[List[str]],
        "MutualAuthentication": NotRequired[MutualAuthenticationAttributesTypeDef],
    },
)
ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "Type": ActionTypeEnumType,
        "TargetGroupArn": NotRequired[str],
        "AuthenticateOidcConfig": NotRequired[AuthenticateOidcActionConfigUnionTypeDef],
        "AuthenticateCognitoConfig": NotRequired[AuthenticateCognitoActionConfigUnionTypeDef],
        "Order": NotRequired[int],
        "RedirectConfig": NotRequired[RedirectActionConfigTypeDef],
        "FixedResponseConfig": NotRequired[FixedResponseActionConfigTypeDef],
        "ForwardConfig": NotRequired[ForwardActionConfigUnionTypeDef],
    },
)

class RuleTypeDef(TypedDict):
    RuleArn: NotRequired[str]
    Priority: NotRequired[str]
    Conditions: NotRequired[List[RuleConditionOutputTypeDef]]
    Actions: NotRequired[List[ActionOutputTypeDef]]
    IsDefault: NotRequired[bool]

class RuleConditionTypeDef(TypedDict):
    Field: NotRequired[str]
    Values: NotRequired[Sequence[str]]
    HostHeaderConfig: NotRequired[HostHeaderConditionConfigUnionTypeDef]
    PathPatternConfig: NotRequired[PathPatternConditionConfigUnionTypeDef]
    HttpHeaderConfig: NotRequired[HttpHeaderConditionConfigUnionTypeDef]
    QueryStringConfig: NotRequired[QueryStringConditionConfigUnionTypeDef]
    HttpRequestMethodConfig: NotRequired[HttpRequestMethodConditionConfigUnionTypeDef]
    SourceIpConfig: NotRequired[SourceIpConditionConfigUnionTypeDef]

class CreateListenerOutputTypeDef(TypedDict):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeListenersOutputTypeDef(TypedDict):
    Listeners: List[ListenerTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyListenerOutputTypeDef(TypedDict):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

ActionUnionTypeDef = Union[ActionTypeDef, ActionOutputTypeDef]

class CreateRuleOutputTypeDef(TypedDict):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRulesOutputTypeDef(TypedDict):
    Rules: List[RuleTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyRuleOutputTypeDef(TypedDict):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetRulePrioritiesOutputTypeDef(TypedDict):
    Rules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

RuleConditionUnionTypeDef = Union[RuleConditionTypeDef, RuleConditionOutputTypeDef]
CreateListenerInputTypeDef = TypedDict(
    "CreateListenerInputTypeDef",
    {
        "LoadBalancerArn": str,
        "DefaultActions": Sequence[ActionUnionTypeDef],
        "Protocol": NotRequired[ProtocolEnumType],
        "Port": NotRequired[int],
        "SslPolicy": NotRequired[str],
        "Certificates": NotRequired[Sequence[CertificateTypeDef]],
        "AlpnPolicy": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "MutualAuthentication": NotRequired[MutualAuthenticationAttributesTypeDef],
    },
)
ModifyListenerInputTypeDef = TypedDict(
    "ModifyListenerInputTypeDef",
    {
        "ListenerArn": str,
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolEnumType],
        "SslPolicy": NotRequired[str],
        "Certificates": NotRequired[Sequence[CertificateTypeDef]],
        "DefaultActions": NotRequired[Sequence[ActionUnionTypeDef]],
        "AlpnPolicy": NotRequired[Sequence[str]],
        "MutualAuthentication": NotRequired[MutualAuthenticationAttributesTypeDef],
    },
)

class CreateRuleInputTypeDef(TypedDict):
    ListenerArn: str
    Conditions: Sequence[RuleConditionUnionTypeDef]
    Priority: int
    Actions: Sequence[ActionUnionTypeDef]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ModifyRuleInputTypeDef(TypedDict):
    RuleArn: str
    Conditions: NotRequired[Sequence[RuleConditionUnionTypeDef]]
    Actions: NotRequired[Sequence[ActionUnionTypeDef]]
