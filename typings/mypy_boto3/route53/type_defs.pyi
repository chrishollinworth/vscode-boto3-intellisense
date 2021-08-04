"""
Type annotations for route53 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    AccountLimitTypeType,
    ChangeActionType,
    ChangeStatusType,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AccountLimitTypeDef",
    "ActivateKeySigningKeyRequestRequestTypeDef",
    "ActivateKeySigningKeyResponseTypeDef",
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "AssociateVPCWithHostedZoneRequestRequestTypeDef",
    "AssociateVPCWithHostedZoneResponseTypeDef",
    "ChangeBatchTypeDef",
    "ChangeInfoTypeDef",
    "ChangeResourceRecordSetsRequestRequestTypeDef",
    "ChangeResourceRecordSetsResponseTypeDef",
    "ChangeTagsForResourceRequestRequestTypeDef",
    "ChangeTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "CreateHealthCheckRequestRequestTypeDef",
    "CreateHealthCheckResponseTypeDef",
    "CreateHostedZoneRequestRequestTypeDef",
    "CreateHostedZoneResponseTypeDef",
    "CreateKeySigningKeyRequestRequestTypeDef",
    "CreateKeySigningKeyResponseTypeDef",
    "CreateQueryLoggingConfigRequestRequestTypeDef",
    "CreateQueryLoggingConfigResponseTypeDef",
    "CreateReusableDelegationSetRequestRequestTypeDef",
    "CreateReusableDelegationSetResponseTypeDef",
    "CreateTrafficPolicyInstanceRequestRequestTypeDef",
    "CreateTrafficPolicyInstanceResponseTypeDef",
    "CreateTrafficPolicyRequestRequestTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "CreateTrafficPolicyVersionRequestRequestTypeDef",
    "CreateTrafficPolicyVersionResponseTypeDef",
    "CreateVPCAssociationAuthorizationRequestRequestTypeDef",
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    "DNSSECStatusTypeDef",
    "DeactivateKeySigningKeyRequestRequestTypeDef",
    "DeactivateKeySigningKeyResponseTypeDef",
    "DelegationSetTypeDef",
    "DeleteHealthCheckRequestRequestTypeDef",
    "DeleteHostedZoneRequestRequestTypeDef",
    "DeleteHostedZoneResponseTypeDef",
    "DeleteKeySigningKeyRequestRequestTypeDef",
    "DeleteKeySigningKeyResponseTypeDef",
    "DeleteQueryLoggingConfigRequestRequestTypeDef",
    "DeleteReusableDelegationSetRequestRequestTypeDef",
    "DeleteTrafficPolicyInstanceRequestRequestTypeDef",
    "DeleteTrafficPolicyRequestRequestTypeDef",
    "DeleteVPCAssociationAuthorizationRequestRequestTypeDef",
    "DimensionTypeDef",
    "DisableHostedZoneDNSSECRequestRequestTypeDef",
    "DisableHostedZoneDNSSECResponseTypeDef",
    "DisassociateVPCFromHostedZoneRequestRequestTypeDef",
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    "EnableHostedZoneDNSSECRequestRequestTypeDef",
    "EnableHostedZoneDNSSECResponseTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
    "GetAccountLimitRequestRequestTypeDef",
    "GetAccountLimitResponseTypeDef",
    "GetChangeRequestRequestTypeDef",
    "GetChangeResponseTypeDef",
    "GetCheckerIpRangesResponseTypeDef",
    "GetDNSSECRequestRequestTypeDef",
    "GetDNSSECResponseTypeDef",
    "GetGeoLocationRequestRequestTypeDef",
    "GetGeoLocationResponseTypeDef",
    "GetHealthCheckCountResponseTypeDef",
    "GetHealthCheckLastFailureReasonRequestRequestTypeDef",
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    "GetHealthCheckRequestRequestTypeDef",
    "GetHealthCheckResponseTypeDef",
    "GetHealthCheckStatusRequestRequestTypeDef",
    "GetHealthCheckStatusResponseTypeDef",
    "GetHostedZoneCountResponseTypeDef",
    "GetHostedZoneLimitRequestRequestTypeDef",
    "GetHostedZoneLimitResponseTypeDef",
    "GetHostedZoneRequestRequestTypeDef",
    "GetHostedZoneResponseTypeDef",
    "GetQueryLoggingConfigRequestRequestTypeDef",
    "GetQueryLoggingConfigResponseTypeDef",
    "GetReusableDelegationSetLimitRequestRequestTypeDef",
    "GetReusableDelegationSetLimitResponseTypeDef",
    "GetReusableDelegationSetRequestRequestTypeDef",
    "GetReusableDelegationSetResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    "GetTrafficPolicyInstanceRequestRequestTypeDef",
    "GetTrafficPolicyInstanceResponseTypeDef",
    "GetTrafficPolicyRequestRequestTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckObservationTypeDef",
    "HealthCheckTypeDef",
    "HostedZoneConfigTypeDef",
    "HostedZoneLimitTypeDef",
    "HostedZoneOwnerTypeDef",
    "HostedZoneSummaryTypeDef",
    "HostedZoneTypeDef",
    "KeySigningKeyTypeDef",
    "LinkedServiceTypeDef",
    "ListGeoLocationsRequestRequestTypeDef",
    "ListGeoLocationsResponseTypeDef",
    "ListHealthChecksRequestRequestTypeDef",
    "ListHealthChecksResponseTypeDef",
    "ListHostedZonesByNameRequestRequestTypeDef",
    "ListHostedZonesByNameResponseTypeDef",
    "ListHostedZonesByVPCRequestRequestTypeDef",
    "ListHostedZonesByVPCResponseTypeDef",
    "ListHostedZonesRequestRequestTypeDef",
    "ListHostedZonesResponseTypeDef",
    "ListQueryLoggingConfigsRequestRequestTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "ListResourceRecordSetsRequestRequestTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "ListReusableDelegationSetsRequestRequestTypeDef",
    "ListReusableDelegationSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsForResourcesRequestRequestTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "ListTrafficPoliciesRequestRequestTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ListTrafficPolicyInstancesRequestRequestTypeDef",
    "ListTrafficPolicyInstancesResponseTypeDef",
    "ListTrafficPolicyVersionsRequestRequestTypeDef",
    "ListTrafficPolicyVersionsResponseTypeDef",
    "ListVPCAssociationAuthorizationsRequestRequestTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryLoggingConfigTypeDef",
    "ResourceRecordSetTypeDef",
    "ResourceRecordTypeDef",
    "ResourceTagSetTypeDef",
    "ResponseMetadataTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "StatusReportTypeDef",
    "TagTypeDef",
    "TestDNSAnswerRequestRequestTypeDef",
    "TestDNSAnswerResponseTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "TrafficPolicySummaryTypeDef",
    "TrafficPolicyTypeDef",
    "UpdateHealthCheckRequestRequestTypeDef",
    "UpdateHealthCheckResponseTypeDef",
    "UpdateHostedZoneCommentRequestRequestTypeDef",
    "UpdateHostedZoneCommentResponseTypeDef",
    "UpdateTrafficPolicyCommentRequestRequestTypeDef",
    "UpdateTrafficPolicyCommentResponseTypeDef",
    "UpdateTrafficPolicyInstanceRequestRequestTypeDef",
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

ActivateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "ActivateKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

ActivateKeySigningKeyResponseTypeDef = TypedDict(
    "ActivateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AlarmIdentifierTypeDef = TypedDict(
    "AlarmIdentifierTypeDef",
    {
        "Region": CloudWatchRegionType,
        "Name": str,
    },
)

AliasTargetTypeDef = TypedDict(
    "AliasTargetTypeDef",
    {
        "HostedZoneId": str,
        "DNSName": str,
        "EvaluateTargetHealth": bool,
    },
)

_RequiredAssociateVPCWithHostedZoneRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateVPCWithHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)
_OptionalAssociateVPCWithHostedZoneRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateVPCWithHostedZoneRequestRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class AssociateVPCWithHostedZoneRequestRequestTypeDef(
    _RequiredAssociateVPCWithHostedZoneRequestRequestTypeDef,
    _OptionalAssociateVPCWithHostedZoneRequestRequestTypeDef,
):
    pass

AssociateVPCWithHostedZoneResponseTypeDef = TypedDict(
    "AssociateVPCWithHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredChangeBatchTypeDef = TypedDict(
    "_RequiredChangeBatchTypeDef",
    {
        "Changes": List["ChangeTypeDef"],
    },
)
_OptionalChangeBatchTypeDef = TypedDict(
    "_OptionalChangeBatchTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class ChangeBatchTypeDef(_RequiredChangeBatchTypeDef, _OptionalChangeBatchTypeDef):
    pass

_RequiredChangeInfoTypeDef = TypedDict(
    "_RequiredChangeInfoTypeDef",
    {
        "Id": str,
        "Status": ChangeStatusType,
        "SubmittedAt": datetime,
    },
)
_OptionalChangeInfoTypeDef = TypedDict(
    "_OptionalChangeInfoTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class ChangeInfoTypeDef(_RequiredChangeInfoTypeDef, _OptionalChangeInfoTypeDef):
    pass

ChangeResourceRecordSetsRequestRequestTypeDef = TypedDict(
    "ChangeResourceRecordSetsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "ChangeBatch": "ChangeBatchTypeDef",
    },
)

ChangeResourceRecordSetsResponseTypeDef = TypedDict(
    "ChangeResourceRecordSetsResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredChangeTagsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredChangeTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
    },
)
_OptionalChangeTagsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalChangeTagsForResourceRequestRequestTypeDef",
    {
        "AddTags": List["TagTypeDef"],
        "RemoveTagKeys": List[str],
    },
    total=False,
)

class ChangeTagsForResourceRequestRequestTypeDef(
    _RequiredChangeTagsForResourceRequestRequestTypeDef,
    _OptionalChangeTagsForResourceRequestRequestTypeDef,
):
    pass

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Action": ChangeActionType,
        "ResourceRecordSet": "ResourceRecordSetTypeDef",
    },
)

_RequiredCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": ComparisonOperatorType,
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": StatisticType,
    },
)
_OptionalCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmConfigurationTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
    },
    total=False,
)

class CloudWatchAlarmConfigurationTypeDef(
    _RequiredCloudWatchAlarmConfigurationTypeDef, _OptionalCloudWatchAlarmConfigurationTypeDef
):
    pass

CreateHealthCheckRequestRequestTypeDef = TypedDict(
    "CreateHealthCheckRequestRequestTypeDef",
    {
        "CallerReference": str,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
    },
)

CreateHealthCheckResponseTypeDef = TypedDict(
    "CreateHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateHostedZoneRequestRequestTypeDef = TypedDict(
    "_RequiredCreateHostedZoneRequestRequestTypeDef",
    {
        "Name": str,
        "CallerReference": str,
    },
)
_OptionalCreateHostedZoneRequestRequestTypeDef = TypedDict(
    "_OptionalCreateHostedZoneRequestRequestTypeDef",
    {
        "VPC": "VPCTypeDef",
        "HostedZoneConfig": "HostedZoneConfigTypeDef",
        "DelegationSetId": str,
    },
    total=False,
)

class CreateHostedZoneRequestRequestTypeDef(
    _RequiredCreateHostedZoneRequestRequestTypeDef, _OptionalCreateHostedZoneRequestRequestTypeDef
):
    pass

CreateHostedZoneResponseTypeDef = TypedDict(
    "CreateHostedZoneResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "ChangeInfo": "ChangeInfoTypeDef",
        "DelegationSet": "DelegationSetTypeDef",
        "VPC": "VPCTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "CreateKeySigningKeyRequestRequestTypeDef",
    {
        "CallerReference": str,
        "HostedZoneId": str,
        "KeyManagementServiceArn": str,
        "Name": str,
        "Status": str,
    },
)

CreateKeySigningKeyResponseTypeDef = TypedDict(
    "CreateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "KeySigningKey": "KeySigningKeyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "CreateQueryLoggingConfigRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "CloudWatchLogsLogGroupArn": str,
    },
)

CreateQueryLoggingConfigResponseTypeDef = TypedDict(
    "CreateQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": "QueryLoggingConfigTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReusableDelegationSetRequestRequestTypeDef",
    {
        "CallerReference": str,
    },
)
_OptionalCreateReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReusableDelegationSetRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
    total=False,
)

class CreateReusableDelegationSetRequestRequestTypeDef(
    _RequiredCreateReusableDelegationSetRequestRequestTypeDef,
    _OptionalCreateReusableDelegationSetRequestRequestTypeDef,
):
    pass

CreateReusableDelegationSetResponseTypeDef = TypedDict(
    "CreateReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)

CreateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficPolicyRequestRequestTypeDef",
    {
        "Name": str,
        "Document": str,
    },
)
_OptionalCreateTrafficPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficPolicyRequestRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class CreateTrafficPolicyRequestRequestTypeDef(
    _RequiredCreateTrafficPolicyRequestRequestTypeDef,
    _OptionalCreateTrafficPolicyRequestRequestTypeDef,
):
    pass

CreateTrafficPolicyResponseTypeDef = TypedDict(
    "CreateTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficPolicyVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficPolicyVersionRequestRequestTypeDef",
    {
        "Id": str,
        "Document": str,
    },
)
_OptionalCreateTrafficPolicyVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficPolicyVersionRequestRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class CreateTrafficPolicyVersionRequestRequestTypeDef(
    _RequiredCreateTrafficPolicyVersionRequestRequestTypeDef,
    _OptionalCreateTrafficPolicyVersionRequestRequestTypeDef,
):
    pass

CreateTrafficPolicyVersionResponseTypeDef = TypedDict(
    "CreateTrafficPolicyVersionResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVPCAssociationAuthorizationRequestRequestTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)

CreateVPCAssociationAuthorizationResponseTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DNSSECStatusTypeDef = TypedDict(
    "DNSSECStatusTypeDef",
    {
        "ServeSignature": str,
        "StatusMessage": str,
    },
    total=False,
)

DeactivateKeySigningKeyRequestRequestTypeDef = TypedDict(
    "DeactivateKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

DeactivateKeySigningKeyResponseTypeDef = TypedDict(
    "DeactivateKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDelegationSetTypeDef = TypedDict(
    "_RequiredDelegationSetTypeDef",
    {
        "NameServers": List[str],
    },
)
_OptionalDelegationSetTypeDef = TypedDict(
    "_OptionalDelegationSetTypeDef",
    {
        "Id": str,
        "CallerReference": str,
    },
    total=False,
)

class DelegationSetTypeDef(_RequiredDelegationSetTypeDef, _OptionalDelegationSetTypeDef):
    pass

DeleteHealthCheckRequestRequestTypeDef = TypedDict(
    "DeleteHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

DeleteHostedZoneRequestRequestTypeDef = TypedDict(
    "DeleteHostedZoneRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteHostedZoneResponseTypeDef = TypedDict(
    "DeleteHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeySigningKeyRequestRequestTypeDef = TypedDict(
    "DeleteKeySigningKeyRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
    },
)

DeleteKeySigningKeyResponseTypeDef = TypedDict(
    "DeleteKeySigningKeyResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "DeleteQueryLoggingConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "DeleteReusableDelegationSetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteTrafficPolicyRequestRequestTypeDef = TypedDict(
    "DeleteTrafficPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
    },
)

DeleteVPCAssociationAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteVPCAssociationAuthorizationRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DisableHostedZoneDNSSECRequestRequestTypeDef = TypedDict(
    "DisableHostedZoneDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

DisableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "DisableHostedZoneDNSSECResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateVPCFromHostedZoneRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateVPCFromHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "VPC": "VPCTypeDef",
    },
)
_OptionalDisassociateVPCFromHostedZoneRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateVPCFromHostedZoneRequestRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class DisassociateVPCFromHostedZoneRequestRequestTypeDef(
    _RequiredDisassociateVPCFromHostedZoneRequestRequestTypeDef,
    _OptionalDisassociateVPCFromHostedZoneRequestRequestTypeDef,
):
    pass

DisassociateVPCFromHostedZoneResponseTypeDef = TypedDict(
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableHostedZoneDNSSECRequestRequestTypeDef = TypedDict(
    "EnableHostedZoneDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

EnableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "EnableHostedZoneDNSSECResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GeoLocationDetailsTypeDef = TypedDict(
    "GeoLocationDetailsTypeDef",
    {
        "ContinentCode": str,
        "ContinentName": str,
        "CountryCode": str,
        "CountryName": str,
        "SubdivisionCode": str,
        "SubdivisionName": str,
    },
    total=False,
)

GeoLocationTypeDef = TypedDict(
    "GeoLocationTypeDef",
    {
        "ContinentCode": str,
        "CountryCode": str,
        "SubdivisionCode": str,
    },
    total=False,
)

GetAccountLimitRequestRequestTypeDef = TypedDict(
    "GetAccountLimitRequestRequestTypeDef",
    {
        "Type": AccountLimitTypeType,
    },
)

GetAccountLimitResponseTypeDef = TypedDict(
    "GetAccountLimitResponseTypeDef",
    {
        "Limit": "AccountLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChangeRequestRequestTypeDef = TypedDict(
    "GetChangeRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetChangeResponseTypeDef = TypedDict(
    "GetChangeResponseTypeDef",
    {
        "ChangeInfo": "ChangeInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCheckerIpRangesResponseTypeDef = TypedDict(
    "GetCheckerIpRangesResponseTypeDef",
    {
        "CheckerIpRanges": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDNSSECRequestRequestTypeDef = TypedDict(
    "GetDNSSECRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)

GetDNSSECResponseTypeDef = TypedDict(
    "GetDNSSECResponseTypeDef",
    {
        "Status": "DNSSECStatusTypeDef",
        "KeySigningKeys": List["KeySigningKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeoLocationRequestRequestTypeDef = TypedDict(
    "GetGeoLocationRequestRequestTypeDef",
    {
        "ContinentCode": str,
        "CountryCode": str,
        "SubdivisionCode": str,
    },
    total=False,
)

GetGeoLocationResponseTypeDef = TypedDict(
    "GetGeoLocationResponseTypeDef",
    {
        "GeoLocationDetails": "GeoLocationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckCountResponseTypeDef = TypedDict(
    "GetHealthCheckCountResponseTypeDef",
    {
        "HealthCheckCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckLastFailureReasonRequestRequestTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckLastFailureReasonResponseTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    {
        "HealthCheckObservations": List["HealthCheckObservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckRequestRequestTypeDef = TypedDict(
    "GetHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckResponseTypeDef = TypedDict(
    "GetHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHealthCheckStatusRequestRequestTypeDef = TypedDict(
    "GetHealthCheckStatusRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)

GetHealthCheckStatusResponseTypeDef = TypedDict(
    "GetHealthCheckStatusResponseTypeDef",
    {
        "HealthCheckObservations": List["HealthCheckObservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneCountResponseTypeDef = TypedDict(
    "GetHostedZoneCountResponseTypeDef",
    {
        "HostedZoneCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneLimitRequestRequestTypeDef = TypedDict(
    "GetHostedZoneLimitRequestRequestTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "HostedZoneId": str,
    },
)

GetHostedZoneLimitResponseTypeDef = TypedDict(
    "GetHostedZoneLimitResponseTypeDef",
    {
        "Limit": "HostedZoneLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostedZoneRequestRequestTypeDef = TypedDict(
    "GetHostedZoneRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetHostedZoneResponseTypeDef = TypedDict(
    "GetHostedZoneResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "DelegationSet": "DelegationSetTypeDef",
        "VPCs": List["VPCTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryLoggingConfigRequestRequestTypeDef = TypedDict(
    "GetQueryLoggingConfigRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetQueryLoggingConfigResponseTypeDef = TypedDict(
    "GetQueryLoggingConfigResponseTypeDef",
    {
        "QueryLoggingConfig": "QueryLoggingConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReusableDelegationSetLimitRequestRequestTypeDef = TypedDict(
    "GetReusableDelegationSetLimitRequestRequestTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "DelegationSetId": str,
    },
)

GetReusableDelegationSetLimitResponseTypeDef = TypedDict(
    "GetReusableDelegationSetLimitResponseTypeDef",
    {
        "Limit": "ReusableDelegationSetLimitTypeDef",
        "Count": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetReusableDelegationSetRequestRequestTypeDef = TypedDict(
    "GetReusableDelegationSetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetReusableDelegationSetResponseTypeDef = TypedDict(
    "GetReusableDelegationSetResponseTypeDef",
    {
        "DelegationSet": "DelegationSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyInstanceCountResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    {
        "TrafficPolicyInstanceCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "GetTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrafficPolicyRequestRequestTypeDef = TypedDict(
    "GetTrafficPolicyRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
    },
)

GetTrafficPolicyResponseTypeDef = TypedDict(
    "GetTrafficPolicyResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredHealthCheckConfigTypeDef = TypedDict(
    "_RequiredHealthCheckConfigTypeDef",
    {
        "Type": HealthCheckTypeType,
    },
)
_OptionalHealthCheckConfigTypeDef = TypedDict(
    "_OptionalHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[HealthCheckRegionType],
        "AlarmIdentifier": "AlarmIdentifierTypeDef",
        "InsufficientDataHealthStatus": InsufficientDataHealthStatusType,
        "RoutingControlArn": str,
    },
    total=False,
)

class HealthCheckConfigTypeDef(
    _RequiredHealthCheckConfigTypeDef, _OptionalHealthCheckConfigTypeDef
):
    pass

HealthCheckObservationTypeDef = TypedDict(
    "HealthCheckObservationTypeDef",
    {
        "Region": HealthCheckRegionType,
        "IPAddress": str,
        "StatusReport": "StatusReportTypeDef",
    },
    total=False,
)

_RequiredHealthCheckTypeDef = TypedDict(
    "_RequiredHealthCheckTypeDef",
    {
        "Id": str,
        "CallerReference": str,
        "HealthCheckConfig": "HealthCheckConfigTypeDef",
        "HealthCheckVersion": int,
    },
)
_OptionalHealthCheckTypeDef = TypedDict(
    "_OptionalHealthCheckTypeDef",
    {
        "LinkedService": "LinkedServiceTypeDef",
        "CloudWatchAlarmConfiguration": "CloudWatchAlarmConfigurationTypeDef",
    },
    total=False,
)

class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, _OptionalHealthCheckTypeDef):
    pass

HostedZoneConfigTypeDef = TypedDict(
    "HostedZoneConfigTypeDef",
    {
        "Comment": str,
        "PrivateZone": bool,
    },
    total=False,
)

HostedZoneLimitTypeDef = TypedDict(
    "HostedZoneLimitTypeDef",
    {
        "Type": HostedZoneLimitTypeType,
        "Value": int,
    },
)

HostedZoneOwnerTypeDef = TypedDict(
    "HostedZoneOwnerTypeDef",
    {
        "OwningAccount": str,
        "OwningService": str,
    },
    total=False,
)

HostedZoneSummaryTypeDef = TypedDict(
    "HostedZoneSummaryTypeDef",
    {
        "HostedZoneId": str,
        "Name": str,
        "Owner": "HostedZoneOwnerTypeDef",
    },
)

_RequiredHostedZoneTypeDef = TypedDict(
    "_RequiredHostedZoneTypeDef",
    {
        "Id": str,
        "Name": str,
        "CallerReference": str,
    },
)
_OptionalHostedZoneTypeDef = TypedDict(
    "_OptionalHostedZoneTypeDef",
    {
        "Config": "HostedZoneConfigTypeDef",
        "ResourceRecordSetCount": int,
        "LinkedService": "LinkedServiceTypeDef",
    },
    total=False,
)

class HostedZoneTypeDef(_RequiredHostedZoneTypeDef, _OptionalHostedZoneTypeDef):
    pass

KeySigningKeyTypeDef = TypedDict(
    "KeySigningKeyTypeDef",
    {
        "Name": str,
        "KmsArn": str,
        "Flag": int,
        "SigningAlgorithmMnemonic": str,
        "SigningAlgorithmType": int,
        "DigestAlgorithmMnemonic": str,
        "DigestAlgorithmType": int,
        "KeyTag": int,
        "DigestValue": str,
        "PublicKey": str,
        "DSRecord": str,
        "DNSKEYRecord": str,
        "Status": str,
        "StatusMessage": str,
        "CreatedDate": datetime,
        "LastModifiedDate": datetime,
    },
    total=False,
)

LinkedServiceTypeDef = TypedDict(
    "LinkedServiceTypeDef",
    {
        "ServicePrincipal": str,
        "Description": str,
    },
    total=False,
)

ListGeoLocationsRequestRequestTypeDef = TypedDict(
    "ListGeoLocationsRequestRequestTypeDef",
    {
        "StartContinentCode": str,
        "StartCountryCode": str,
        "StartSubdivisionCode": str,
        "MaxItems": str,
    },
    total=False,
)

ListGeoLocationsResponseTypeDef = TypedDict(
    "ListGeoLocationsResponseTypeDef",
    {
        "GeoLocationDetailsList": List["GeoLocationDetailsTypeDef"],
        "IsTruncated": bool,
        "NextContinentCode": str,
        "NextCountryCode": str,
        "NextSubdivisionCode": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHealthChecksRequestRequestTypeDef = TypedDict(
    "ListHealthChecksRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListHealthChecksResponseTypeDef = TypedDict(
    "ListHealthChecksResponseTypeDef",
    {
        "HealthChecks": List["HealthCheckTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostedZonesByNameRequestRequestTypeDef = TypedDict(
    "ListHostedZonesByNameRequestRequestTypeDef",
    {
        "DNSName": str,
        "HostedZoneId": str,
        "MaxItems": str,
    },
    total=False,
)

ListHostedZonesByNameResponseTypeDef = TypedDict(
    "ListHostedZonesByNameResponseTypeDef",
    {
        "HostedZones": List["HostedZoneTypeDef"],
        "DNSName": str,
        "HostedZoneId": str,
        "IsTruncated": bool,
        "NextDNSName": str,
        "NextHostedZoneId": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListHostedZonesByVPCRequestRequestTypeDef = TypedDict(
    "_RequiredListHostedZonesByVPCRequestRequestTypeDef",
    {
        "VPCId": str,
        "VPCRegion": VPCRegionType,
    },
)
_OptionalListHostedZonesByVPCRequestRequestTypeDef = TypedDict(
    "_OptionalListHostedZonesByVPCRequestRequestTypeDef",
    {
        "MaxItems": str,
        "NextToken": str,
    },
    total=False,
)

class ListHostedZonesByVPCRequestRequestTypeDef(
    _RequiredListHostedZonesByVPCRequestRequestTypeDef,
    _OptionalListHostedZonesByVPCRequestRequestTypeDef,
):
    pass

ListHostedZonesByVPCResponseTypeDef = TypedDict(
    "ListHostedZonesByVPCResponseTypeDef",
    {
        "HostedZoneSummaries": List["HostedZoneSummaryTypeDef"],
        "MaxItems": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHostedZonesRequestRequestTypeDef = TypedDict(
    "ListHostedZonesRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
        "DelegationSetId": str,
    },
    total=False,
)

ListHostedZonesResponseTypeDef = TypedDict(
    "ListHostedZonesResponseTypeDef",
    {
        "HostedZones": List["HostedZoneTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueryLoggingConfigsRequestRequestTypeDef = TypedDict(
    "ListQueryLoggingConfigsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": str,
        "MaxResults": str,
    },
    total=False,
)

ListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "ListQueryLoggingConfigsResponseTypeDef",
    {
        "QueryLoggingConfigs": List["QueryLoggingConfigTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListResourceRecordSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListResourceRecordSetsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
_OptionalListResourceRecordSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListResourceRecordSetsRequestRequestTypeDef",
    {
        "StartRecordName": str,
        "StartRecordType": RRTypeType,
        "StartRecordIdentifier": str,
        "MaxItems": str,
    },
    total=False,
)

class ListResourceRecordSetsRequestRequestTypeDef(
    _RequiredListResourceRecordSetsRequestRequestTypeDef,
    _OptionalListResourceRecordSetsRequestRequestTypeDef,
):
    pass

ListResourceRecordSetsResponseTypeDef = TypedDict(
    "ListResourceRecordSetsResponseTypeDef",
    {
        "ResourceRecordSets": List["ResourceRecordSetTypeDef"],
        "IsTruncated": bool,
        "NextRecordName": str,
        "NextRecordType": RRTypeType,
        "NextRecordIdentifier": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReusableDelegationSetsRequestRequestTypeDef = TypedDict(
    "ListReusableDelegationSetsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": str,
    },
    total=False,
)

ListReusableDelegationSetsResponseTypeDef = TypedDict(
    "ListReusableDelegationSetsResponseTypeDef",
    {
        "DelegationSets": List["DelegationSetTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "NextMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "ResourceTagSet": "ResourceTagSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourcesRequestRequestTypeDef = TypedDict(
    "ListTagsForResourcesRequestRequestTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceIds": List[str],
    },
)

ListTagsForResourcesResponseTypeDef = TypedDict(
    "ListTagsForResourcesResponseTypeDef",
    {
        "ResourceTagSets": List["ResourceTagSetTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPoliciesRequestRequestTypeDef = TypedDict(
    "ListTrafficPoliciesRequestRequestTypeDef",
    {
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
    },
    total=False,
)

ListTrafficPoliciesResponseTypeDef = TypedDict(
    "ListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicySummaries": List["TrafficPolicySummaryTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
_OptionalListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef",
    {
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "MaxItems": str,
    },
    total=False,
)

class ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef(
    _RequiredListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef,
    _OptionalListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef,
):
    pass

ListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrafficPolicyInstancesByPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesByPolicyRequestRequestTypeDef",
    {
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)
_OptionalListTrafficPolicyInstancesByPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesByPolicyRequestRequestTypeDef",
    {
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "MaxItems": str,
    },
    total=False,
)

class ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef(
    _RequiredListTrafficPolicyInstancesByPolicyRequestRequestTypeDef,
    _OptionalListTrafficPolicyInstancesByPolicyRequestRequestTypeDef,
):
    pass

ListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrafficPolicyInstancesRequestRequestTypeDef = TypedDict(
    "ListTrafficPolicyInstancesRequestRequestTypeDef",
    {
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "MaxItems": str,
    },
    total=False,
)

ListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "ListTrafficPolicyInstancesResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": RRTypeType,
        "IsTruncated": bool,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTrafficPolicyVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListTrafficPolicyVersionsRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalListTrafficPolicyVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListTrafficPolicyVersionsRequestRequestTypeDef",
    {
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
    },
    total=False,
)

class ListTrafficPolicyVersionsRequestRequestTypeDef(
    _RequiredListTrafficPolicyVersionsRequestRequestTypeDef,
    _OptionalListTrafficPolicyVersionsRequestRequestTypeDef,
):
    pass

ListTrafficPolicyVersionsResponseTypeDef = TypedDict(
    "ListTrafficPolicyVersionsResponseTypeDef",
    {
        "TrafficPolicies": List["TrafficPolicyTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVPCAssociationAuthorizationsRequestRequestTypeDef = TypedDict(
    "_RequiredListVPCAssociationAuthorizationsRequestRequestTypeDef",
    {
        "HostedZoneId": str,
    },
)
_OptionalListVPCAssociationAuthorizationsRequestRequestTypeDef = TypedDict(
    "_OptionalListVPCAssociationAuthorizationsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": str,
    },
    total=False,
)

class ListVPCAssociationAuthorizationsRequestRequestTypeDef(
    _RequiredListVPCAssociationAuthorizationsRequestRequestTypeDef,
    _OptionalListVPCAssociationAuthorizationsRequestRequestTypeDef,
):
    pass

ListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    {
        "HostedZoneId": str,
        "NextToken": str,
        "VPCs": List["VPCTypeDef"],
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

QueryLoggingConfigTypeDef = TypedDict(
    "QueryLoggingConfigTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "CloudWatchLogsLogGroupArn": str,
    },
)

_RequiredResourceRecordSetTypeDef = TypedDict(
    "_RequiredResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": RRTypeType,
    },
)
_OptionalResourceRecordSetTypeDef = TypedDict(
    "_OptionalResourceRecordSetTypeDef",
    {
        "SetIdentifier": str,
        "Weight": int,
        "Region": ResourceRecordSetRegionType,
        "GeoLocation": "GeoLocationTypeDef",
        "Failover": ResourceRecordSetFailoverType,
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List["ResourceRecordTypeDef"],
        "AliasTarget": "AliasTargetTypeDef",
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)

class ResourceRecordSetTypeDef(
    _RequiredResourceRecordSetTypeDef, _OptionalResourceRecordSetTypeDef
):
    pass

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "Value": str,
    },
)

ResourceTagSetTypeDef = TypedDict(
    "ResourceTagSetTypeDef",
    {
        "ResourceType": TagResourceTypeType,
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
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

ReusableDelegationSetLimitTypeDef = TypedDict(
    "ReusableDelegationSetLimitTypeDef",
    {
        "Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"],
        "Value": int,
    },
)

StatusReportTypeDef = TypedDict(
    "StatusReportTypeDef",
    {
        "Status": str,
        "CheckedTime": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

_RequiredTestDNSAnswerRequestRequestTypeDef = TypedDict(
    "_RequiredTestDNSAnswerRequestRequestTypeDef",
    {
        "HostedZoneId": str,
        "RecordName": str,
        "RecordType": RRTypeType,
    },
)
_OptionalTestDNSAnswerRequestRequestTypeDef = TypedDict(
    "_OptionalTestDNSAnswerRequestRequestTypeDef",
    {
        "ResolverIP": str,
        "EDNS0ClientSubnetIP": str,
        "EDNS0ClientSubnetMask": str,
    },
    total=False,
)

class TestDNSAnswerRequestRequestTypeDef(
    _RequiredTestDNSAnswerRequestRequestTypeDef, _OptionalTestDNSAnswerRequestRequestTypeDef
):
    pass

TestDNSAnswerResponseTypeDef = TypedDict(
    "TestDNSAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": RRTypeType,
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TrafficPolicyInstanceTypeDef = TypedDict(
    "TrafficPolicyInstanceTypeDef",
    {
        "Id": str,
        "HostedZoneId": str,
        "Name": str,
        "TTL": int,
        "State": str,
        "Message": str,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
        "TrafficPolicyType": RRTypeType,
    },
)

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

_RequiredTrafficPolicyTypeDef = TypedDict(
    "_RequiredTrafficPolicyTypeDef",
    {
        "Id": str,
        "Version": int,
        "Name": str,
        "Type": RRTypeType,
        "Document": str,
    },
)
_OptionalTrafficPolicyTypeDef = TypedDict(
    "_OptionalTrafficPolicyTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class TrafficPolicyTypeDef(_RequiredTrafficPolicyTypeDef, _OptionalTrafficPolicyTypeDef):
    pass

_RequiredUpdateHealthCheckRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckId": str,
    },
)
_OptionalUpdateHealthCheckRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateHealthCheckRequestRequestTypeDef",
    {
        "HealthCheckVersion": int,
        "IPAddress": str,
        "Port": int,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "FailureThreshold": int,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[HealthCheckRegionType],
        "AlarmIdentifier": "AlarmIdentifierTypeDef",
        "InsufficientDataHealthStatus": InsufficientDataHealthStatusType,
        "ResetElements": List[ResettableElementNameType],
    },
    total=False,
)

class UpdateHealthCheckRequestRequestTypeDef(
    _RequiredUpdateHealthCheckRequestRequestTypeDef, _OptionalUpdateHealthCheckRequestRequestTypeDef
):
    pass

UpdateHealthCheckResponseTypeDef = TypedDict(
    "UpdateHealthCheckResponseTypeDef",
    {
        "HealthCheck": "HealthCheckTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateHostedZoneCommentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateHostedZoneCommentRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateHostedZoneCommentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateHostedZoneCommentRequestRequestTypeDef",
    {
        "Comment": str,
    },
    total=False,
)

class UpdateHostedZoneCommentRequestRequestTypeDef(
    _RequiredUpdateHostedZoneCommentRequestRequestTypeDef,
    _OptionalUpdateHostedZoneCommentRequestRequestTypeDef,
):
    pass

UpdateHostedZoneCommentResponseTypeDef = TypedDict(
    "UpdateHostedZoneCommentResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrafficPolicyCommentRequestRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentRequestRequestTypeDef",
    {
        "Id": str,
        "Version": int,
        "Comment": str,
    },
)

UpdateTrafficPolicyCommentResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentResponseTypeDef",
    {
        "TrafficPolicy": "TrafficPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrafficPolicyInstanceRequestRequestTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceRequestRequestTypeDef",
    {
        "Id": str,
        "TTL": int,
        "TrafficPolicyId": str,
        "TrafficPolicyVersion": int,
    },
)

UpdateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    {
        "TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VPCTypeDef = TypedDict(
    "VPCTypeDef",
    {
        "VPCRegion": VPCRegionType,
        "VPCId": str,
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
