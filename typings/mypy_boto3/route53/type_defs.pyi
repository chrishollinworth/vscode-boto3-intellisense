"""
Type annotations for route53 service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_route53.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccountLimitTypeType,
    ChangeActionType,
    ChangeStatusType,
    CidrCollectionChangeActionType,
    CloudWatchRegionType,
    ComparisonOperatorType,
    HealthCheckRegionType,
    HealthCheckTypeType,
    HostedZoneLimitTypeType,
    InsufficientDataHealthStatusType,
    ResettableElementNameType,
    ResourceRecordSetFailoverType,
    ResourceRecordSetRegionType,
    RRTypeType,
    StatisticType,
    TagResourceTypeType,
    VPCRegionType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountLimitTypeDef",
    "ActivateKeySigningKeyRequestTypeDef",
    "ActivateKeySigningKeyResponseTypeDef",
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "AssociateVPCWithHostedZoneRequestTypeDef",
    "AssociateVPCWithHostedZoneResponseTypeDef",
    "ChangeBatchTypeDef",
    "ChangeCidrCollectionRequestTypeDef",
    "ChangeCidrCollectionResponseTypeDef",
    "ChangeInfoTypeDef",
    "ChangeResourceRecordSetsRequestTypeDef",
    "ChangeResourceRecordSetsResponseTypeDef",
    "ChangeTagsForResourceRequestTypeDef",
    "ChangeTypeDef",
    "CidrBlockSummaryTypeDef",
    "CidrCollectionChangeTypeDef",
    "CidrCollectionTypeDef",
    "CidrRoutingConfigTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "CollectionSummaryTypeDef",
    "CoordinatesTypeDef",
    "CreateCidrCollectionRequestTypeDef",
    "CreateCidrCollectionResponseTypeDef",
    "CreateHealthCheckRequestTypeDef",
    "CreateHealthCheckResponseTypeDef",
    "CreateHostedZoneRequestTypeDef",
    "CreateHostedZoneResponseTypeDef",
    "CreateKeySigningKeyRequestTypeDef",
    "CreateKeySigningKeyResponseTypeDef",
    "CreateQueryLoggingConfigRequestTypeDef",
    "CreateQueryLoggingConfigResponseTypeDef",
    "CreateReusableDelegationSetRequestTypeDef",
    "CreateReusableDelegationSetResponseTypeDef",
    "CreateTrafficPolicyInstanceRequestTypeDef",
    "CreateTrafficPolicyInstanceResponseTypeDef",
    "CreateTrafficPolicyRequestTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "CreateTrafficPolicyVersionRequestTypeDef",
    "CreateTrafficPolicyVersionResponseTypeDef",
    "CreateVPCAssociationAuthorizationRequestTypeDef",
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    "DNSSECStatusTypeDef",
    "DeactivateKeySigningKeyRequestTypeDef",
    "DeactivateKeySigningKeyResponseTypeDef",
    "DelegationSetTypeDef",
    "DeleteCidrCollectionRequestTypeDef",
    "DeleteHealthCheckRequestTypeDef",
    "DeleteHostedZoneRequestTypeDef",
    "DeleteHostedZoneResponseTypeDef",
    "DeleteKeySigningKeyRequestTypeDef",
    "DeleteKeySigningKeyResponseTypeDef",
    "DeleteQueryLoggingConfigRequestTypeDef",
    "DeleteReusableDelegationSetRequestTypeDef",
    "DeleteTrafficPolicyInstanceRequestTypeDef",
    "DeleteTrafficPolicyRequestTypeDef",
    "DeleteVPCAssociationAuthorizationRequestTypeDef",
    "DimensionTypeDef",
    "DisableHostedZoneDNSSECRequestTypeDef",
    "DisableHostedZoneDNSSECResponseTypeDef",
    "DisassociateVPCFromHostedZoneRequestTypeDef",
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    "EnableHostedZoneDNSSECRequestTypeDef",
    "EnableHostedZoneDNSSECResponseTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
    "GeoProximityLocationTypeDef",
    "GetAccountLimitRequestTypeDef",
    "GetAccountLimitResponseTypeDef",
    "GetChangeRequestTypeDef",
    "GetChangeRequestWaitTypeDef",
    "GetChangeResponseTypeDef",
    "GetCheckerIpRangesResponseTypeDef",
    "GetDNSSECRequestTypeDef",
    "GetDNSSECResponseTypeDef",
    "GetGeoLocationRequestTypeDef",
    "GetGeoLocationResponseTypeDef",
    "GetHealthCheckCountResponseTypeDef",
    "GetHealthCheckLastFailureReasonRequestTypeDef",
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    "GetHealthCheckRequestTypeDef",
    "GetHealthCheckResponseTypeDef",
    "GetHealthCheckStatusRequestTypeDef",
    "GetHealthCheckStatusResponseTypeDef",
    "GetHostedZoneCountResponseTypeDef",
    "GetHostedZoneLimitRequestTypeDef",
    "GetHostedZoneLimitResponseTypeDef",
    "GetHostedZoneRequestTypeDef",
    "GetHostedZoneResponseTypeDef",
    "GetQueryLoggingConfigRequestTypeDef",
    "GetQueryLoggingConfigResponseTypeDef",
    "GetReusableDelegationSetLimitRequestTypeDef",
    "GetReusableDelegationSetLimitResponseTypeDef",
    "GetReusableDelegationSetRequestTypeDef",
    "GetReusableDelegationSetResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    "GetTrafficPolicyInstanceRequestTypeDef",
    "GetTrafficPolicyInstanceResponseTypeDef",
    "GetTrafficPolicyRequestTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "HealthCheckConfigOutputTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckConfigUnionTypeDef",
    "HealthCheckObservationTypeDef",
    "HealthCheckTypeDef",
    "HostedZoneConfigTypeDef",
    "HostedZoneLimitTypeDef",
    "HostedZoneOwnerTypeDef",
    "HostedZoneSummaryTypeDef",
    "HostedZoneTypeDef",
    "KeySigningKeyTypeDef",
    "LinkedServiceTypeDef",
    "ListCidrBlocksRequestPaginateTypeDef",
    "ListCidrBlocksRequestTypeDef",
    "ListCidrBlocksResponseTypeDef",
    "ListCidrCollectionsRequestPaginateTypeDef",
    "ListCidrCollectionsRequestTypeDef",
    "ListCidrCollectionsResponseTypeDef",
    "ListCidrLocationsRequestPaginateTypeDef",
    "ListCidrLocationsRequestTypeDef",
    "ListCidrLocationsResponseTypeDef",
    "ListGeoLocationsRequestTypeDef",
    "ListGeoLocationsResponseTypeDef",
    "ListHealthChecksRequestPaginateTypeDef",
    "ListHealthChecksRequestTypeDef",
    "ListHealthChecksResponseTypeDef",
    "ListHostedZonesByNameRequestTypeDef",
    "ListHostedZonesByNameResponseTypeDef",
    "ListHostedZonesByVPCRequestTypeDef",
    "ListHostedZonesByVPCResponseTypeDef",
    "ListHostedZonesRequestPaginateTypeDef",
    "ListHostedZonesRequestTypeDef",
    "ListHostedZonesResponseTypeDef",
    "ListQueryLoggingConfigsRequestPaginateTypeDef",
    "ListQueryLoggingConfigsRequestTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "ListResourceRecordSetsRequestPaginateTypeDef",
    "ListResourceRecordSetsRequestTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "ListReusableDelegationSetsRequestTypeDef",
    "ListReusableDelegationSetsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsForResourcesRequestTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "ListTrafficPoliciesRequestTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneRequestTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyRequestTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ListTrafficPolicyInstancesRequestTypeDef",
    "ListTrafficPolicyInstancesResponseTypeDef",
    "ListTrafficPolicyVersionsRequestTypeDef",
    "ListTrafficPolicyVersionsResponseTypeDef",
    "ListVPCAssociationAuthorizationsRequestPaginateTypeDef",
    "ListVPCAssociationAuthorizationsRequestTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "LocationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "QueryLoggingConfigTypeDef",
    "ResourceRecordSetOutputTypeDef",
    "ResourceRecordSetTypeDef",
    "ResourceRecordSetUnionTypeDef",
    "ResourceRecordTypeDef",
    "ResourceTagSetTypeDef",
    "ResponseMetadataTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "StatusReportTypeDef",
    "TagTypeDef",
    "TestDNSAnswerRequestTypeDef",
    "TestDNSAnswerResponseTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "TrafficPolicySummaryTypeDef",
    "TrafficPolicyTypeDef",
    "UpdateHealthCheckRequestTypeDef",
    "UpdateHealthCheckResponseTypeDef",
    "UpdateHostedZoneCommentRequestTypeDef",
    "UpdateHostedZoneCommentResponseTypeDef",
    "UpdateTrafficPolicyCommentRequestTypeDef",
    "UpdateTrafficPolicyCommentResponseTypeDef",
    "UpdateTrafficPolicyInstanceRequestTypeDef",
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    "VPCTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Type": AccountLimitTypeType,
        "Value": int,
    },
)

class ActivateKeySigningKeyRequestTypeDef(TypedDict):
    HostedZoneId: str
    Name: str

class ChangeInfoTypeDef(TypedDict):
    Id: str
    Status: ChangeStatusType
    SubmittedAt: datetime
    Comment: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AlarmIdentifierTypeDef(TypedDict):
    Region: CloudWatchRegionType
    Name: str

class AliasTargetTypeDef(TypedDict):
    HostedZoneId: str
    DNSName: str
    EvaluateTargetHealth: bool

class VPCTypeDef(TypedDict):
    VPCRegion: NotRequired[VPCRegionType]
    VPCId: NotRequired[str]

class CidrCollectionChangeTypeDef(TypedDict):
    LocationName: str
    Action: CidrCollectionChangeActionType
    CidrList: Sequence[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class CidrBlockSummaryTypeDef(TypedDict):
    CidrBlock: NotRequired[str]
    LocationName: NotRequired[str]

class CidrCollectionTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Version: NotRequired[int]

class CidrRoutingConfigTypeDef(TypedDict):
    CollectionId: str
    LocationName: str

class DimensionTypeDef(TypedDict):
    Name: str
    Value: str

class CollectionSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    Version: NotRequired[int]

class CoordinatesTypeDef(TypedDict):
    Latitude: str
    Longitude: str

class CreateCidrCollectionRequestTypeDef(TypedDict):
    Name: str
    CallerReference: str

class HostedZoneConfigTypeDef(TypedDict):
    Comment: NotRequired[str]
    PrivateZone: NotRequired[bool]

class DelegationSetTypeDef(TypedDict):
    NameServers: List[str]
    Id: NotRequired[str]
    CallerReference: NotRequired[str]

class CreateKeySigningKeyRequestTypeDef(TypedDict):
    CallerReference: str
    HostedZoneId: str
    KeyManagementServiceArn: str
    Name: str
    Status: str

class KeySigningKeyTypeDef(TypedDict):
    Name: NotRequired[str]
    KmsArn: NotRequired[str]
    Flag: NotRequired[int]
    SigningAlgorithmMnemonic: NotRequired[str]
    SigningAlgorithmType: NotRequired[int]
    DigestAlgorithmMnemonic: NotRequired[str]
    DigestAlgorithmType: NotRequired[int]
    KeyTag: NotRequired[int]
    DigestValue: NotRequired[str]
    PublicKey: NotRequired[str]
    DSRecord: NotRequired[str]
    DNSKEYRecord: NotRequired[str]
    Status: NotRequired[str]
    StatusMessage: NotRequired[str]
    CreatedDate: NotRequired[datetime]
    LastModifiedDate: NotRequired[datetime]

class CreateQueryLoggingConfigRequestTypeDef(TypedDict):
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str

class QueryLoggingConfigTypeDef(TypedDict):
    Id: str
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str

class CreateReusableDelegationSetRequestTypeDef(TypedDict):
    CallerReference: str
    HostedZoneId: NotRequired[str]

class CreateTrafficPolicyInstanceRequestTypeDef(TypedDict):
    HostedZoneId: str
    Name: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int

class TrafficPolicyInstanceTypeDef(TypedDict):
    Id: str
    HostedZoneId: str
    Name: str
    TTL: int
    State: str
    Message: str
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    TrafficPolicyType: RRTypeType

class CreateTrafficPolicyRequestTypeDef(TypedDict):
    Name: str
    Document: str
    Comment: NotRequired[str]

TrafficPolicyTypeDef = TypedDict(
    "TrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": RRTypeType,
        "Document": str,
        "Comment": NotRequired[str],
    },
)

class CreateTrafficPolicyVersionRequestTypeDef(TypedDict):
    Id: str
    Document: str
    Comment: NotRequired[str]

class DNSSECStatusTypeDef(TypedDict):
    ServeSignature: NotRequired[str]
    StatusMessage: NotRequired[str]

class DeactivateKeySigningKeyRequestTypeDef(TypedDict):
    HostedZoneId: str
    Name: str

class DeleteCidrCollectionRequestTypeDef(TypedDict):
    Id: str

class DeleteHealthCheckRequestTypeDef(TypedDict):
    HealthCheckId: str

class DeleteHostedZoneRequestTypeDef(TypedDict):
    Id: str

class DeleteKeySigningKeyRequestTypeDef(TypedDict):
    HostedZoneId: str
    Name: str

class DeleteQueryLoggingConfigRequestTypeDef(TypedDict):
    Id: str

class DeleteReusableDelegationSetRequestTypeDef(TypedDict):
    Id: str

class DeleteTrafficPolicyInstanceRequestTypeDef(TypedDict):
    Id: str

class DeleteTrafficPolicyRequestTypeDef(TypedDict):
    Id: str
    Version: int

class DisableHostedZoneDNSSECRequestTypeDef(TypedDict):
    HostedZoneId: str

class EnableHostedZoneDNSSECRequestTypeDef(TypedDict):
    HostedZoneId: str

class GeoLocationDetailsTypeDef(TypedDict):
    ContinentCode: NotRequired[str]
    ContinentName: NotRequired[str]
    CountryCode: NotRequired[str]
    CountryName: NotRequired[str]
    SubdivisionCode: NotRequired[str]
    SubdivisionName: NotRequired[str]

class GeoLocationTypeDef(TypedDict):
    ContinentCode: NotRequired[str]
    CountryCode: NotRequired[str]
    SubdivisionCode: NotRequired[str]

GetAccountLimitRequestTypeDef = TypedDict(
    "GetAccountLimitRequestTypeDef",
    {
        "Type": AccountLimitTypeType,
    },
)

class GetChangeRequestTypeDef(TypedDict):
    Id: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetDNSSECRequestTypeDef(TypedDict):
    HostedZoneId: str

class GetGeoLocationRequestTypeDef(TypedDict):
    ContinentCode: NotRequired[str]
    CountryCode: NotRequired[str]
    SubdivisionCode: NotRequired[str]

class GetHealthCheckLastFailureReasonRequestTypeDef(TypedDict):
    HealthCheckId: str

class GetHealthCheckRequestTypeDef(TypedDict):
    HealthCheckId: str

class GetHealthCheckStatusRequestTypeDef(TypedDict):
    HealthCheckId: str

GetHostedZoneLimitRequestTypeDef = TypedDict(
    "GetHostedZoneLimitRequestTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "HostedZoneId": str,
    },
)
HostedZoneLimitTypeDef = TypedDict(
    "HostedZoneLimitTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "Value": int,
    },
)

class GetHostedZoneRequestTypeDef(TypedDict):
    Id: str

class GetQueryLoggingConfigRequestTypeDef(TypedDict):
    Id: str

GetReusableDelegationSetLimitRequestTypeDef = TypedDict(
    "GetReusableDelegationSetLimitRequestTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "DelegationSetId": str,
    },
)
ReusableDelegationSetLimitTypeDef = TypedDict(
    "ReusableDelegationSetLimitTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "Value": int,
    },
)

class GetReusableDelegationSetRequestTypeDef(TypedDict):
    Id: str

class GetTrafficPolicyInstanceRequestTypeDef(TypedDict):
    Id: str

class GetTrafficPolicyRequestTypeDef(TypedDict):
    Id: str
    Version: int

class StatusReportTypeDef(TypedDict):
    Status: NotRequired[str]
    CheckedTime: NotRequired[datetime]

class LinkedServiceTypeDef(TypedDict):
    ServicePrincipal: NotRequired[str]
    Description: NotRequired[str]

class HostedZoneOwnerTypeDef(TypedDict):
    OwningAccount: NotRequired[str]
    OwningService: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCidrBlocksRequestTypeDef(TypedDict):
    CollectionId: str
    LocationName: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[str]

class ListCidrCollectionsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[str]

class ListCidrLocationsRequestTypeDef(TypedDict):
    CollectionId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[str]

class LocationSummaryTypeDef(TypedDict):
    LocationName: NotRequired[str]

class ListGeoLocationsRequestTypeDef(TypedDict):
    StartContinentCode: NotRequired[str]
    StartCountryCode: NotRequired[str]
    StartSubdivisionCode: NotRequired[str]
    MaxItems: NotRequired[str]

class ListHealthChecksRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListHostedZonesByNameRequestTypeDef(TypedDict):
    DNSName: NotRequired[str]
    HostedZoneId: NotRequired[str]
    MaxItems: NotRequired[str]

class ListHostedZonesByVPCRequestTypeDef(TypedDict):
    VPCId: str
    VPCRegion: VPCRegionType
    MaxItems: NotRequired[str]
    NextToken: NotRequired[str]

class ListHostedZonesRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]
    DelegationSetId: NotRequired[str]
    HostedZoneType: NotRequired[Literal["PrivateHostedZone"]]

class ListQueryLoggingConfigsRequestTypeDef(TypedDict):
    HostedZoneId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[str]

class ListResourceRecordSetsRequestTypeDef(TypedDict):
    HostedZoneId: str
    StartRecordName: NotRequired[str]
    StartRecordType: NotRequired[RRTypeType]
    StartRecordIdentifier: NotRequired[str]
    MaxItems: NotRequired[str]

class ListReusableDelegationSetsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceType: TagResourceTypeType
    ResourceId: str

class ListTagsForResourcesRequestTypeDef(TypedDict):
    ResourceType: TagResourceTypeType
    ResourceIds: Sequence[str]

class ListTrafficPoliciesRequestTypeDef(TypedDict):
    TrafficPolicyIdMarker: NotRequired[str]
    MaxItems: NotRequired[str]

TrafficPolicySummaryTypeDef = TypedDict(
    "TrafficPolicySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": RRTypeType,
        "LatestVersion": int,
        "TrafficPolicyCount": int,
    },
)

class ListTrafficPolicyInstancesByHostedZoneRequestTypeDef(TypedDict):
    HostedZoneId: str
    TrafficPolicyInstanceNameMarker: NotRequired[str]
    TrafficPolicyInstanceTypeMarker: NotRequired[RRTypeType]
    MaxItems: NotRequired[str]

class ListTrafficPolicyInstancesByPolicyRequestTypeDef(TypedDict):
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    HostedZoneIdMarker: NotRequired[str]
    TrafficPolicyInstanceNameMarker: NotRequired[str]
    TrafficPolicyInstanceTypeMarker: NotRequired[RRTypeType]
    MaxItems: NotRequired[str]

class ListTrafficPolicyInstancesRequestTypeDef(TypedDict):
    HostedZoneIdMarker: NotRequired[str]
    TrafficPolicyInstanceNameMarker: NotRequired[str]
    TrafficPolicyInstanceTypeMarker: NotRequired[RRTypeType]
    MaxItems: NotRequired[str]

class ListTrafficPolicyVersionsRequestTypeDef(TypedDict):
    Id: str
    TrafficPolicyVersionMarker: NotRequired[str]
    MaxItems: NotRequired[str]

class ListVPCAssociationAuthorizationsRequestTypeDef(TypedDict):
    HostedZoneId: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[str]

class ResourceRecordTypeDef(TypedDict):
    Value: str

class TestDNSAnswerRequestTypeDef(TypedDict):
    HostedZoneId: str
    RecordName: str
    RecordType: RRTypeType
    ResolverIP: NotRequired[str]
    EDNS0ClientSubnetIP: NotRequired[str]
    EDNS0ClientSubnetMask: NotRequired[str]

class UpdateHostedZoneCommentRequestTypeDef(TypedDict):
    Id: str
    Comment: NotRequired[str]

class UpdateTrafficPolicyCommentRequestTypeDef(TypedDict):
    Id: str
    Version: int
    Comment: str

class UpdateTrafficPolicyInstanceRequestTypeDef(TypedDict):
    Id: str
    TTL: int
    TrafficPolicyId: str
    TrafficPolicyVersion: int

class ActivateKeySigningKeyResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateVPCWithHostedZoneResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeCidrCollectionResponseTypeDef(TypedDict):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChangeResourceRecordSetsResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateKeySigningKeyResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteHostedZoneResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeySigningKeyResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisableHostedZoneDNSSECResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateVPCFromHostedZoneResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableHostedZoneDNSSECResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountLimitResponseTypeDef(TypedDict):
    Limit: AccountLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCheckerIpRangesResponseTypeDef(TypedDict):
    CheckerIpRanges: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetHealthCheckCountResponseTypeDef(TypedDict):
    HealthCheckCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostedZoneCountResponseTypeDef(TypedDict):
    HostedZoneCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrafficPolicyInstanceCountResponseTypeDef(TypedDict):
    TrafficPolicyInstanceCount: int
    ResponseMetadata: ResponseMetadataTypeDef

TestDNSAnswerResponseTypeDef = TypedDict(
    "TestDNSAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": RRTypeType,
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HealthCheckConfigOutputTypeDef = TypedDict(
    "HealthCheckConfigOutputTypeDef",
    {
        "Type": HealthCheckTypeType,
        "IPAddress": NotRequired[str],
        "Port": NotRequired[int],
        "ResourcePath": NotRequired[str],
        "FullyQualifiedDomainName": NotRequired[str],
        "SearchString": NotRequired[str],
        "RequestInterval": NotRequired[int],
        "FailureThreshold": NotRequired[int],
        "MeasureLatency": NotRequired[bool],
        "Inverted": NotRequired[bool],
        "Disabled": NotRequired[bool],
        "HealthThreshold": NotRequired[int],
        "ChildHealthChecks": NotRequired[List[str]],
        "EnableSNI": NotRequired[bool],
        "Regions": NotRequired[List[HealthCheckRegionType]],
        "AlarmIdentifier": NotRequired[AlarmIdentifierTypeDef],
        "InsufficientDataHealthStatus": NotRequired[InsufficientDataHealthStatusType],
        "RoutingControlArn": NotRequired[str],
    },
)
HealthCheckConfigTypeDef = TypedDict(
    "HealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
        "IPAddress": NotRequired[str],
        "Port": NotRequired[int],
        "ResourcePath": NotRequired[str],
        "FullyQualifiedDomainName": NotRequired[str],
        "SearchString": NotRequired[str],
        "RequestInterval": NotRequired[int],
        "FailureThreshold": NotRequired[int],
        "MeasureLatency": NotRequired[bool],
        "Inverted": NotRequired[bool],
        "Disabled": NotRequired[bool],
        "HealthThreshold": NotRequired[int],
        "ChildHealthChecks": NotRequired[Sequence[str]],
        "EnableSNI": NotRequired[bool],
        "Regions": NotRequired[Sequence[HealthCheckRegionType]],
        "AlarmIdentifier": NotRequired[AlarmIdentifierTypeDef],
        "InsufficientDataHealthStatus": NotRequired[InsufficientDataHealthStatusType],
        "RoutingControlArn": NotRequired[str],
    },
)

class UpdateHealthCheckRequestTypeDef(TypedDict):
    HealthCheckId: str
    HealthCheckVersion: NotRequired[int]
    IPAddress: NotRequired[str]
    Port: NotRequired[int]
    ResourcePath: NotRequired[str]
    FullyQualifiedDomainName: NotRequired[str]
    SearchString: NotRequired[str]
    FailureThreshold: NotRequired[int]
    Inverted: NotRequired[bool]
    Disabled: NotRequired[bool]
    HealthThreshold: NotRequired[int]
    ChildHealthChecks: NotRequired[Sequence[str]]
    EnableSNI: NotRequired[bool]
    Regions: NotRequired[Sequence[HealthCheckRegionType]]
    AlarmIdentifier: NotRequired[AlarmIdentifierTypeDef]
    InsufficientDataHealthStatus: NotRequired[InsufficientDataHealthStatusType]
    ResetElements: NotRequired[Sequence[ResettableElementNameType]]

class AssociateVPCWithHostedZoneRequestTypeDef(TypedDict):
    HostedZoneId: str
    VPC: VPCTypeDef
    Comment: NotRequired[str]

class CreateVPCAssociationAuthorizationRequestTypeDef(TypedDict):
    HostedZoneId: str
    VPC: VPCTypeDef

class CreateVPCAssociationAuthorizationResponseTypeDef(TypedDict):
    HostedZoneId: str
    VPC: VPCTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVPCAssociationAuthorizationRequestTypeDef(TypedDict):
    HostedZoneId: str
    VPC: VPCTypeDef

class DisassociateVPCFromHostedZoneRequestTypeDef(TypedDict):
    HostedZoneId: str
    VPC: VPCTypeDef
    Comment: NotRequired[str]

class ListVPCAssociationAuthorizationsResponseTypeDef(TypedDict):
    HostedZoneId: str
    VPCs: List[VPCTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ChangeCidrCollectionRequestTypeDef(TypedDict):
    Id: str
    Changes: Sequence[CidrCollectionChangeTypeDef]
    CollectionVersion: NotRequired[int]

class ChangeTagsForResourceRequestTypeDef(TypedDict):
    ResourceType: TagResourceTypeType
    ResourceId: str
    AddTags: NotRequired[Sequence[TagTypeDef]]
    RemoveTagKeys: NotRequired[Sequence[str]]

class ResourceTagSetTypeDef(TypedDict):
    ResourceType: NotRequired[TagResourceTypeType]
    ResourceId: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

class ListCidrBlocksResponseTypeDef(TypedDict):
    CidrBlocks: List[CidrBlockSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

CreateCidrCollectionResponseTypeDef = TypedDict(
    "CreateCidrCollectionResponseTypeDef",
    {
        "Collection": CidrCollectionTypeDef,
        "Location": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CloudWatchAlarmConfigurationTypeDef(TypedDict):
    EvaluationPeriods: int
    Threshold: float
    ComparisonOperator: ComparisonOperatorType
    Period: int
    MetricName: str
    Namespace: str
    Statistic: StatisticType
    Dimensions: NotRequired[List[DimensionTypeDef]]

class ListCidrCollectionsResponseTypeDef(TypedDict):
    CidrCollections: List[CollectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GeoProximityLocationTypeDef(TypedDict):
    AWSRegion: NotRequired[str]
    LocalZoneGroup: NotRequired[str]
    Coordinates: NotRequired[CoordinatesTypeDef]
    Bias: NotRequired[int]

class CreateHostedZoneRequestTypeDef(TypedDict):
    Name: str
    CallerReference: str
    VPC: NotRequired[VPCTypeDef]
    HostedZoneConfig: NotRequired[HostedZoneConfigTypeDef]
    DelegationSetId: NotRequired[str]

class CreateReusableDelegationSetResponseTypeDef(TypedDict):
    DelegationSet: DelegationSetTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReusableDelegationSetResponseTypeDef(TypedDict):
    DelegationSet: DelegationSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListReusableDelegationSetsResponseTypeDef(TypedDict):
    DelegationSets: List[DelegationSetTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKeySigningKeyResponseTypeDef(TypedDict):
    ChangeInfo: ChangeInfoTypeDef
    KeySigningKey: KeySigningKeyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueryLoggingConfigResponseTypeDef(TypedDict):
    QueryLoggingConfig: QueryLoggingConfigTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryLoggingConfigResponseTypeDef(TypedDict):
    QueryLoggingConfig: QueryLoggingConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListQueryLoggingConfigsResponseTypeDef(TypedDict):
    QueryLoggingConfigs: List[QueryLoggingConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateTrafficPolicyInstanceResponseTypeDef(TypedDict):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrafficPolicyInstanceResponseTypeDef(TypedDict):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPolicyInstancesByHostedZoneResponseTypeDef(TypedDict):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPolicyInstancesByPolicyResponseTypeDef(TypedDict):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPolicyInstancesResponseTypeDef(TypedDict):
    TrafficPolicyInstances: List[TrafficPolicyInstanceTypeDef]
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRTypeType
    IsTruncated: bool
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrafficPolicyInstanceResponseTypeDef(TypedDict):
    TrafficPolicyInstance: TrafficPolicyInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficPolicyResponseTypeDef(TypedDict):
    TrafficPolicy: TrafficPolicyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficPolicyVersionResponseTypeDef(TypedDict):
    TrafficPolicy: TrafficPolicyTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrafficPolicyResponseTypeDef(TypedDict):
    TrafficPolicy: TrafficPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTrafficPolicyVersionsResponseTypeDef(TypedDict):
    TrafficPolicies: List[TrafficPolicyTypeDef]
    IsTruncated: bool
    TrafficPolicyVersionMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrafficPolicyCommentResponseTypeDef(TypedDict):
    TrafficPolicy: TrafficPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDNSSECResponseTypeDef(TypedDict):
    Status: DNSSECStatusTypeDef
    KeySigningKeys: List[KeySigningKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGeoLocationResponseTypeDef(TypedDict):
    GeoLocationDetails: GeoLocationDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGeoLocationsResponseTypeDef(TypedDict):
    GeoLocationDetailsList: List[GeoLocationDetailsTypeDef]
    IsTruncated: bool
    NextContinentCode: str
    NextCountryCode: str
    NextSubdivisionCode: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChangeRequestWaitTypeDef(TypedDict):
    Id: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetHostedZoneLimitResponseTypeDef(TypedDict):
    Limit: HostedZoneLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetReusableDelegationSetLimitResponseTypeDef(TypedDict):
    Limit: ReusableDelegationSetLimitTypeDef
    Count: int
    ResponseMetadata: ResponseMetadataTypeDef

class HealthCheckObservationTypeDef(TypedDict):
    Region: NotRequired[HealthCheckRegionType]
    IPAddress: NotRequired[str]
    StatusReport: NotRequired[StatusReportTypeDef]

class HostedZoneTypeDef(TypedDict):
    Id: str
    Name: str
    CallerReference: str
    Config: NotRequired[HostedZoneConfigTypeDef]
    ResourceRecordSetCount: NotRequired[int]
    LinkedService: NotRequired[LinkedServiceTypeDef]

class HostedZoneSummaryTypeDef(TypedDict):
    HostedZoneId: str
    Name: str
    Owner: HostedZoneOwnerTypeDef

class ListCidrBlocksRequestPaginateTypeDef(TypedDict):
    CollectionId: str
    LocationName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCidrCollectionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCidrLocationsRequestPaginateTypeDef(TypedDict):
    CollectionId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHealthChecksRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListHostedZonesRequestPaginateTypeDef(TypedDict):
    DelegationSetId: NotRequired[str]
    HostedZoneType: NotRequired[Literal["PrivateHostedZone"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListQueryLoggingConfigsRequestPaginateTypeDef(TypedDict):
    HostedZoneId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListResourceRecordSetsRequestPaginateTypeDef(TypedDict):
    HostedZoneId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVPCAssociationAuthorizationsRequestPaginateTypeDef(TypedDict):
    HostedZoneId: str
    MaxResults: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCidrLocationsResponseTypeDef(TypedDict):
    CidrLocations: List[LocationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTrafficPoliciesResponseTypeDef(TypedDict):
    TrafficPolicySummaries: List[TrafficPolicySummaryTypeDef]
    IsTruncated: bool
    TrafficPolicyIdMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

HealthCheckConfigUnionTypeDef = Union[HealthCheckConfigTypeDef, HealthCheckConfigOutputTypeDef]

class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceTagSet: ResourceTagSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourcesResponseTypeDef(TypedDict):
    ResourceTagSets: List[ResourceTagSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class HealthCheckTypeDef(TypedDict):
    Id: str
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigOutputTypeDef
    HealthCheckVersion: int
    LinkedService: NotRequired[LinkedServiceTypeDef]
    CloudWatchAlarmConfiguration: NotRequired[CloudWatchAlarmConfigurationTypeDef]

ResourceRecordSetOutputTypeDef = TypedDict(
    "ResourceRecordSetOutputTypeDef",
    {
        "Name": str,
        "Type": RRTypeType,
        "SetIdentifier": NotRequired[str],
        "Weight": NotRequired[int],
        "Region": NotRequired[ResourceRecordSetRegionType],
        "GeoLocation": NotRequired[GeoLocationTypeDef],
        "Failover": NotRequired[ResourceRecordSetFailoverType],
        "MultiValueAnswer": NotRequired[bool],
        "TTL": NotRequired[int],
        "ResourceRecords": NotRequired[List[ResourceRecordTypeDef]],
        "AliasTarget": NotRequired[AliasTargetTypeDef],
        "HealthCheckId": NotRequired[str],
        "TrafficPolicyInstanceId": NotRequired[str],
        "CidrRoutingConfig": NotRequired[CidrRoutingConfigTypeDef],
        "GeoProximityLocation": NotRequired[GeoProximityLocationTypeDef],
    },
)
ResourceRecordSetTypeDef = TypedDict(
    "ResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": RRTypeType,
        "SetIdentifier": NotRequired[str],
        "Weight": NotRequired[int],
        "Region": NotRequired[ResourceRecordSetRegionType],
        "GeoLocation": NotRequired[GeoLocationTypeDef],
        "Failover": NotRequired[ResourceRecordSetFailoverType],
        "MultiValueAnswer": NotRequired[bool],
        "TTL": NotRequired[int],
        "ResourceRecords": NotRequired[Sequence[ResourceRecordTypeDef]],
        "AliasTarget": NotRequired[AliasTargetTypeDef],
        "HealthCheckId": NotRequired[str],
        "TrafficPolicyInstanceId": NotRequired[str],
        "CidrRoutingConfig": NotRequired[CidrRoutingConfigTypeDef],
        "GeoProximityLocation": NotRequired[GeoProximityLocationTypeDef],
    },
)

class GetHealthCheckLastFailureReasonResponseTypeDef(TypedDict):
    HealthCheckObservations: List[HealthCheckObservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetHealthCheckStatusResponseTypeDef(TypedDict):
    HealthCheckObservations: List[HealthCheckObservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHostedZoneResponseTypeDef(TypedDict):
    HostedZone: HostedZoneTypeDef
    ChangeInfo: ChangeInfoTypeDef
    DelegationSet: DelegationSetTypeDef
    VPC: VPCTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostedZoneResponseTypeDef(TypedDict):
    HostedZone: HostedZoneTypeDef
    DelegationSet: DelegationSetTypeDef
    VPCs: List[VPCTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListHostedZonesByNameResponseTypeDef(TypedDict):
    HostedZones: List[HostedZoneTypeDef]
    DNSName: str
    HostedZoneId: str
    IsTruncated: bool
    NextDNSName: str
    NextHostedZoneId: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListHostedZonesResponseTypeDef(TypedDict):
    HostedZones: List[HostedZoneTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHostedZoneCommentResponseTypeDef(TypedDict):
    HostedZone: HostedZoneTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHostedZonesByVPCResponseTypeDef(TypedDict):
    HostedZoneSummaries: List[HostedZoneSummaryTypeDef]
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateHealthCheckRequestTypeDef(TypedDict):
    CallerReference: str
    HealthCheckConfig: HealthCheckConfigUnionTypeDef

class CreateHealthCheckResponseTypeDef(TypedDict):
    HealthCheck: HealthCheckTypeDef
    Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetHealthCheckResponseTypeDef(TypedDict):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListHealthChecksResponseTypeDef(TypedDict):
    HealthChecks: List[HealthCheckTypeDef]
    Marker: str
    IsTruncated: bool
    NextMarker: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHealthCheckResponseTypeDef(TypedDict):
    HealthCheck: HealthCheckTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceRecordSetsResponseTypeDef(TypedDict):
    ResourceRecordSets: List[ResourceRecordSetOutputTypeDef]
    IsTruncated: bool
    NextRecordName: str
    NextRecordType: RRTypeType
    NextRecordIdentifier: str
    MaxItems: str
    ResponseMetadata: ResponseMetadataTypeDef

ResourceRecordSetUnionTypeDef = Union[ResourceRecordSetTypeDef, ResourceRecordSetOutputTypeDef]

class ChangeTypeDef(TypedDict):
    Action: ChangeActionType
    ResourceRecordSet: ResourceRecordSetUnionTypeDef

class ChangeBatchTypeDef(TypedDict):
    Changes: Sequence[ChangeTypeDef]
    Comment: NotRequired[str]

class ChangeResourceRecordSetsRequestTypeDef(TypedDict):
    HostedZoneId: str
    ChangeBatch: ChangeBatchTypeDef
