"""
Main interface for route53 service type definitions.

Usage::

    ```python
    from mypy_boto3_route53.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

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
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "ChangeInfoTypeDef",
    "ChangeTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "DNSSECStatusTypeDef",
    "DelegationSetTypeDef",
    "DimensionTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
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
    "QueryLoggingConfigTypeDef",
    "ResourceRecordSetTypeDef",
    "ResourceRecordTypeDef",
    "ResourceTagSetTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "StatusReportTypeDef",
    "TagTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "TrafficPolicySummaryTypeDef",
    "TrafficPolicyTypeDef",
    "VPCTypeDef",
    "ActivateKeySigningKeyResponseTypeDef",
    "AssociateVPCWithHostedZoneResponseTypeDef",
    "ChangeBatchTypeDef",
    "ChangeResourceRecordSetsResponseTypeDef",
    "CreateHealthCheckResponseTypeDef",
    "CreateHostedZoneResponseTypeDef",
    "CreateKeySigningKeyResponseTypeDef",
    "CreateQueryLoggingConfigResponseTypeDef",
    "CreateReusableDelegationSetResponseTypeDef",
    "CreateTrafficPolicyInstanceResponseTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "CreateTrafficPolicyVersionResponseTypeDef",
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    "DeactivateKeySigningKeyResponseTypeDef",
    "DeleteHostedZoneResponseTypeDef",
    "DeleteKeySigningKeyResponseTypeDef",
    "DisableHostedZoneDNSSECResponseTypeDef",
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    "EnableHostedZoneDNSSECResponseTypeDef",
    "GetAccountLimitResponseTypeDef",
    "GetChangeResponseTypeDef",
    "GetCheckerIpRangesResponseTypeDef",
    "GetDNSSECResponseTypeDef",
    "GetGeoLocationResponseTypeDef",
    "GetHealthCheckCountResponseTypeDef",
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    "GetHealthCheckResponseTypeDef",
    "GetHealthCheckStatusResponseTypeDef",
    "GetHostedZoneCountResponseTypeDef",
    "GetHostedZoneLimitResponseTypeDef",
    "GetHostedZoneResponseTypeDef",
    "GetQueryLoggingConfigResponseTypeDef",
    "GetReusableDelegationSetLimitResponseTypeDef",
    "GetReusableDelegationSetResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    "GetTrafficPolicyInstanceResponseTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "ListGeoLocationsResponseTypeDef",
    "ListHealthChecksResponseTypeDef",
    "ListHostedZonesByNameResponseTypeDef",
    "ListHostedZonesByVPCResponseTypeDef",
    "ListHostedZonesResponseTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "ListReusableDelegationSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ListTrafficPolicyInstancesResponseTypeDef",
    "ListTrafficPolicyVersionsResponseTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "TestDNSAnswerResponseTypeDef",
    "UpdateHealthCheckResponseTypeDef",
    "UpdateHostedZoneCommentResponseTypeDef",
    "UpdateTrafficPolicyCommentResponseTypeDef",
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Type": Literal[
            "MAX_HEALTH_CHECKS_BY_OWNER",
            "MAX_HOSTED_ZONES_BY_OWNER",
            "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER",
            "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER",
            "MAX_TRAFFIC_POLICIES_BY_OWNER",
        ],
        "Value": int,
    },
)

AlarmIdentifierTypeDef = TypedDict(
    "AlarmIdentifierTypeDef",
    {
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-northwest-1",
            "cn-north-1",
            "af-south-1",
            "eu-south-1",
            "us-gov-west-1",
            "us-gov-east-1",
            "us-iso-east-1",
            "us-isob-east-1",
        ],
        "Name": str,
    },
)

AliasTargetTypeDef = TypedDict(
    "AliasTargetTypeDef", {"HostedZoneId": str, "DNSName": str, "EvaluateTargetHealth": bool}
)

_RequiredChangeInfoTypeDef = TypedDict(
    "_RequiredChangeInfoTypeDef",
    {"Id": str, "Status": Literal["PENDING", "INSYNC"], "SubmittedAt": datetime},
)
_OptionalChangeInfoTypeDef = TypedDict("_OptionalChangeInfoTypeDef", {"Comment": str}, total=False)


class ChangeInfoTypeDef(_RequiredChangeInfoTypeDef, _OptionalChangeInfoTypeDef):
    pass


ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Action": Literal["CREATE", "DELETE", "UPSERT"],
        "ResourceRecordSet": "ResourceRecordSetTypeDef",
    },
)

_RequiredCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_RequiredCloudWatchAlarmConfigurationTypeDef",
    {
        "EvaluationPeriods": int,
        "Threshold": float,
        "ComparisonOperator": Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        "Period": int,
        "MetricName": str,
        "Namespace": str,
        "Statistic": Literal["Average", "Sum", "SampleCount", "Maximum", "Minimum"],
    },
)
_OptionalCloudWatchAlarmConfigurationTypeDef = TypedDict(
    "_OptionalCloudWatchAlarmConfigurationTypeDef",
    {"Dimensions": List["DimensionTypeDef"]},
    total=False,
)


class CloudWatchAlarmConfigurationTypeDef(
    _RequiredCloudWatchAlarmConfigurationTypeDef, _OptionalCloudWatchAlarmConfigurationTypeDef
):
    pass


DNSSECStatusTypeDef = TypedDict(
    "DNSSECStatusTypeDef", {"ServeSignature": str, "StatusMessage": str}, total=False
)

_RequiredDelegationSetTypeDef = TypedDict(
    "_RequiredDelegationSetTypeDef", {"NameServers": List[str]}
)
_OptionalDelegationSetTypeDef = TypedDict(
    "_OptionalDelegationSetTypeDef", {"Id": str, "CallerReference": str}, total=False
)


class DelegationSetTypeDef(_RequiredDelegationSetTypeDef, _OptionalDelegationSetTypeDef):
    pass


DimensionTypeDef = TypedDict("DimensionTypeDef", {"Name": str, "Value": str})

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
    {"ContinentCode": str, "CountryCode": str, "SubdivisionCode": str},
    total=False,
)

_RequiredHealthCheckConfigTypeDef = TypedDict(
    "_RequiredHealthCheckConfigTypeDef",
    {
        "Type": Literal[
            "HTTP",
            "HTTPS",
            "HTTP_STR_MATCH",
            "HTTPS_STR_MATCH",
            "TCP",
            "CALCULATED",
            "CLOUDWATCH_METRIC",
        ]
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
        "Regions": List[
            Literal[
                "us-east-1",
                "us-west-1",
                "us-west-2",
                "eu-west-1",
                "ap-southeast-1",
                "ap-southeast-2",
                "ap-northeast-1",
                "sa-east-1",
            ]
        ],
        "AlarmIdentifier": "AlarmIdentifierTypeDef",
        "InsufficientDataHealthStatus": Literal["Healthy", "Unhealthy", "LastKnownStatus"],
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
        "Region": Literal[
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "sa-east-1",
        ],
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
    "HostedZoneConfigTypeDef", {"Comment": str, "PrivateZone": bool}, total=False
)

HostedZoneLimitTypeDef = TypedDict(
    "HostedZoneLimitTypeDef",
    {"Type": Literal["MAX_RRSETS_BY_ZONE", "MAX_VPCS_ASSOCIATED_BY_ZONE"], "Value": int},
)

HostedZoneOwnerTypeDef = TypedDict(
    "HostedZoneOwnerTypeDef", {"OwningAccount": str, "OwningService": str}, total=False
)

HostedZoneSummaryTypeDef = TypedDict(
    "HostedZoneSummaryTypeDef",
    {"HostedZoneId": str, "Name": str, "Owner": "HostedZoneOwnerTypeDef"},
)

_RequiredHostedZoneTypeDef = TypedDict(
    "_RequiredHostedZoneTypeDef", {"Id": str, "Name": str, "CallerReference": str}
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
    "LinkedServiceTypeDef", {"ServicePrincipal": str, "Description": str}, total=False
)

QueryLoggingConfigTypeDef = TypedDict(
    "QueryLoggingConfigTypeDef", {"Id": str, "HostedZoneId": str, "CloudWatchLogsLogGroupArn": str}
)

_RequiredResourceRecordSetTypeDef = TypedDict(
    "_RequiredResourceRecordSetTypeDef",
    {
        "Name": str,
        "Type": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
    },
)
_OptionalResourceRecordSetTypeDef = TypedDict(
    "_OptionalResourceRecordSetTypeDef",
    {
        "SetIdentifier": str,
        "Weight": int,
        "Region": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "ca-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "cn-north-1",
            "cn-northwest-1",
            "ap-east-1",
            "me-south-1",
            "ap-south-1",
            "af-south-1",
            "eu-south-1",
        ],
        "GeoLocation": "GeoLocationTypeDef",
        "Failover": Literal["PRIMARY", "SECONDARY"],
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


ResourceRecordTypeDef = TypedDict("ResourceRecordTypeDef", {"Value": str})

ResourceTagSetTypeDef = TypedDict(
    "ResourceTagSetTypeDef",
    {
        "ResourceType": Literal["healthcheck", "hostedzone"],
        "ResourceId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ReusableDelegationSetLimitTypeDef = TypedDict(
    "ReusableDelegationSetLimitTypeDef",
    {"Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"], "Value": int},
)

StatusReportTypeDef = TypedDict(
    "StatusReportTypeDef", {"Status": str, "CheckedTime": datetime}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str}, total=False)

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
        "TrafficPolicyType": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
    },
)

TrafficPolicySummaryTypeDef = TypedDict(
    "TrafficPolicySummaryTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
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
        "Type": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
        "Document": str,
    },
)
_OptionalTrafficPolicyTypeDef = TypedDict(
    "_OptionalTrafficPolicyTypeDef", {"Comment": str}, total=False
)


class TrafficPolicyTypeDef(_RequiredTrafficPolicyTypeDef, _OptionalTrafficPolicyTypeDef):
    pass


VPCTypeDef = TypedDict(
    "VPCTypeDef",
    {
        "VPCRegion": Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ap-east-1",
            "me-south-1",
            "us-gov-west-1",
            "us-gov-east-1",
            "us-iso-east-1",
            "us-isob-east-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-south-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "eu-north-1",
            "sa-east-1",
            "ca-central-1",
            "cn-north-1",
            "af-south-1",
            "eu-south-1",
        ],
        "VPCId": str,
    },
    total=False,
)

ActivateKeySigningKeyResponseTypeDef = TypedDict(
    "ActivateKeySigningKeyResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

AssociateVPCWithHostedZoneResponseTypeDef = TypedDict(
    "AssociateVPCWithHostedZoneResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

_RequiredChangeBatchTypeDef = TypedDict(
    "_RequiredChangeBatchTypeDef", {"Changes": List["ChangeTypeDef"]}
)
_OptionalChangeBatchTypeDef = TypedDict(
    "_OptionalChangeBatchTypeDef", {"Comment": str}, total=False
)


class ChangeBatchTypeDef(_RequiredChangeBatchTypeDef, _OptionalChangeBatchTypeDef):
    pass


ChangeResourceRecordSetsResponseTypeDef = TypedDict(
    "ChangeResourceRecordSetsResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

CreateHealthCheckResponseTypeDef = TypedDict(
    "CreateHealthCheckResponseTypeDef", {"HealthCheck": "HealthCheckTypeDef", "Location": str}
)

_RequiredCreateHostedZoneResponseTypeDef = TypedDict(
    "_RequiredCreateHostedZoneResponseTypeDef",
    {
        "HostedZone": "HostedZoneTypeDef",
        "ChangeInfo": "ChangeInfoTypeDef",
        "DelegationSet": "DelegationSetTypeDef",
        "Location": str,
    },
)
_OptionalCreateHostedZoneResponseTypeDef = TypedDict(
    "_OptionalCreateHostedZoneResponseTypeDef", {"VPC": "VPCTypeDef"}, total=False
)


class CreateHostedZoneResponseTypeDef(
    _RequiredCreateHostedZoneResponseTypeDef, _OptionalCreateHostedZoneResponseTypeDef
):
    pass


CreateKeySigningKeyResponseTypeDef = TypedDict(
    "CreateKeySigningKeyResponseTypeDef",
    {"ChangeInfo": "ChangeInfoTypeDef", "KeySigningKey": "KeySigningKeyTypeDef", "Location": str},
)

CreateQueryLoggingConfigResponseTypeDef = TypedDict(
    "CreateQueryLoggingConfigResponseTypeDef",
    {"QueryLoggingConfig": "QueryLoggingConfigTypeDef", "Location": str},
)

CreateReusableDelegationSetResponseTypeDef = TypedDict(
    "CreateReusableDelegationSetResponseTypeDef",
    {"DelegationSet": "DelegationSetTypeDef", "Location": str},
)

CreateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "CreateTrafficPolicyInstanceResponseTypeDef",
    {"TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef", "Location": str},
)

CreateTrafficPolicyResponseTypeDef = TypedDict(
    "CreateTrafficPolicyResponseTypeDef", {"TrafficPolicy": "TrafficPolicyTypeDef", "Location": str}
)

CreateTrafficPolicyVersionResponseTypeDef = TypedDict(
    "CreateTrafficPolicyVersionResponseTypeDef",
    {"TrafficPolicy": "TrafficPolicyTypeDef", "Location": str},
)

CreateVPCAssociationAuthorizationResponseTypeDef = TypedDict(
    "CreateVPCAssociationAuthorizationResponseTypeDef", {"HostedZoneId": str, "VPC": "VPCTypeDef"}
)

DeactivateKeySigningKeyResponseTypeDef = TypedDict(
    "DeactivateKeySigningKeyResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

DeleteHostedZoneResponseTypeDef = TypedDict(
    "DeleteHostedZoneResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

DeleteKeySigningKeyResponseTypeDef = TypedDict(
    "DeleteKeySigningKeyResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

DisableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "DisableHostedZoneDNSSECResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

DisassociateVPCFromHostedZoneResponseTypeDef = TypedDict(
    "DisassociateVPCFromHostedZoneResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

EnableHostedZoneDNSSECResponseTypeDef = TypedDict(
    "EnableHostedZoneDNSSECResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

GetAccountLimitResponseTypeDef = TypedDict(
    "GetAccountLimitResponseTypeDef", {"Limit": "AccountLimitTypeDef", "Count": int}
)

GetChangeResponseTypeDef = TypedDict(
    "GetChangeResponseTypeDef", {"ChangeInfo": "ChangeInfoTypeDef"}
)

GetCheckerIpRangesResponseTypeDef = TypedDict(
    "GetCheckerIpRangesResponseTypeDef", {"CheckerIpRanges": List[str]}
)

GetDNSSECResponseTypeDef = TypedDict(
    "GetDNSSECResponseTypeDef",
    {"Status": "DNSSECStatusTypeDef", "KeySigningKeys": List["KeySigningKeyTypeDef"]},
)

GetGeoLocationResponseTypeDef = TypedDict(
    "GetGeoLocationResponseTypeDef", {"GeoLocationDetails": "GeoLocationDetailsTypeDef"}
)

GetHealthCheckCountResponseTypeDef = TypedDict(
    "GetHealthCheckCountResponseTypeDef", {"HealthCheckCount": int}
)

GetHealthCheckLastFailureReasonResponseTypeDef = TypedDict(
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    {"HealthCheckObservations": List["HealthCheckObservationTypeDef"]},
)

GetHealthCheckResponseTypeDef = TypedDict(
    "GetHealthCheckResponseTypeDef", {"HealthCheck": "HealthCheckTypeDef"}
)

GetHealthCheckStatusResponseTypeDef = TypedDict(
    "GetHealthCheckStatusResponseTypeDef",
    {"HealthCheckObservations": List["HealthCheckObservationTypeDef"]},
)

GetHostedZoneCountResponseTypeDef = TypedDict(
    "GetHostedZoneCountResponseTypeDef", {"HostedZoneCount": int}
)

GetHostedZoneLimitResponseTypeDef = TypedDict(
    "GetHostedZoneLimitResponseTypeDef", {"Limit": "HostedZoneLimitTypeDef", "Count": int}
)

_RequiredGetHostedZoneResponseTypeDef = TypedDict(
    "_RequiredGetHostedZoneResponseTypeDef", {"HostedZone": "HostedZoneTypeDef"}
)
_OptionalGetHostedZoneResponseTypeDef = TypedDict(
    "_OptionalGetHostedZoneResponseTypeDef",
    {"DelegationSet": "DelegationSetTypeDef", "VPCs": List["VPCTypeDef"]},
    total=False,
)


class GetHostedZoneResponseTypeDef(
    _RequiredGetHostedZoneResponseTypeDef, _OptionalGetHostedZoneResponseTypeDef
):
    pass


GetQueryLoggingConfigResponseTypeDef = TypedDict(
    "GetQueryLoggingConfigResponseTypeDef", {"QueryLoggingConfig": "QueryLoggingConfigTypeDef"}
)

GetReusableDelegationSetLimitResponseTypeDef = TypedDict(
    "GetReusableDelegationSetLimitResponseTypeDef",
    {"Limit": "ReusableDelegationSetLimitTypeDef", "Count": int},
)

GetReusableDelegationSetResponseTypeDef = TypedDict(
    "GetReusableDelegationSetResponseTypeDef", {"DelegationSet": "DelegationSetTypeDef"}
)

GetTrafficPolicyInstanceCountResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceCountResponseTypeDef", {"TrafficPolicyInstanceCount": int}
)

GetTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "GetTrafficPolicyInstanceResponseTypeDef",
    {"TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef"},
)

GetTrafficPolicyResponseTypeDef = TypedDict(
    "GetTrafficPolicyResponseTypeDef", {"TrafficPolicy": "TrafficPolicyTypeDef"}
)

_RequiredListGeoLocationsResponseTypeDef = TypedDict(
    "_RequiredListGeoLocationsResponseTypeDef",
    {
        "GeoLocationDetailsList": List["GeoLocationDetailsTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListGeoLocationsResponseTypeDef = TypedDict(
    "_OptionalListGeoLocationsResponseTypeDef",
    {"NextContinentCode": str, "NextCountryCode": str, "NextSubdivisionCode": str},
    total=False,
)


class ListGeoLocationsResponseTypeDef(
    _RequiredListGeoLocationsResponseTypeDef, _OptionalListGeoLocationsResponseTypeDef
):
    pass


_RequiredListHealthChecksResponseTypeDef = TypedDict(
    "_RequiredListHealthChecksResponseTypeDef",
    {
        "HealthChecks": List["HealthCheckTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListHealthChecksResponseTypeDef = TypedDict(
    "_OptionalListHealthChecksResponseTypeDef", {"NextMarker": str}, total=False
)


class ListHealthChecksResponseTypeDef(
    _RequiredListHealthChecksResponseTypeDef, _OptionalListHealthChecksResponseTypeDef
):
    pass


_RequiredListHostedZonesByNameResponseTypeDef = TypedDict(
    "_RequiredListHostedZonesByNameResponseTypeDef",
    {"HostedZones": List["HostedZoneTypeDef"], "IsTruncated": bool, "MaxItems": str},
)
_OptionalListHostedZonesByNameResponseTypeDef = TypedDict(
    "_OptionalListHostedZonesByNameResponseTypeDef",
    {"DNSName": str, "HostedZoneId": str, "NextDNSName": str, "NextHostedZoneId": str},
    total=False,
)


class ListHostedZonesByNameResponseTypeDef(
    _RequiredListHostedZonesByNameResponseTypeDef, _OptionalListHostedZonesByNameResponseTypeDef
):
    pass


_RequiredListHostedZonesByVPCResponseTypeDef = TypedDict(
    "_RequiredListHostedZonesByVPCResponseTypeDef",
    {"HostedZoneSummaries": List["HostedZoneSummaryTypeDef"], "MaxItems": str},
)
_OptionalListHostedZonesByVPCResponseTypeDef = TypedDict(
    "_OptionalListHostedZonesByVPCResponseTypeDef", {"NextToken": str}, total=False
)


class ListHostedZonesByVPCResponseTypeDef(
    _RequiredListHostedZonesByVPCResponseTypeDef, _OptionalListHostedZonesByVPCResponseTypeDef
):
    pass


_RequiredListHostedZonesResponseTypeDef = TypedDict(
    "_RequiredListHostedZonesResponseTypeDef",
    {"HostedZones": List["HostedZoneTypeDef"], "Marker": str, "IsTruncated": bool, "MaxItems": str},
)
_OptionalListHostedZonesResponseTypeDef = TypedDict(
    "_OptionalListHostedZonesResponseTypeDef", {"NextMarker": str}, total=False
)


class ListHostedZonesResponseTypeDef(
    _RequiredListHostedZonesResponseTypeDef, _OptionalListHostedZonesResponseTypeDef
):
    pass


_RequiredListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "_RequiredListQueryLoggingConfigsResponseTypeDef",
    {"QueryLoggingConfigs": List["QueryLoggingConfigTypeDef"]},
)
_OptionalListQueryLoggingConfigsResponseTypeDef = TypedDict(
    "_OptionalListQueryLoggingConfigsResponseTypeDef", {"NextToken": str}, total=False
)


class ListQueryLoggingConfigsResponseTypeDef(
    _RequiredListQueryLoggingConfigsResponseTypeDef, _OptionalListQueryLoggingConfigsResponseTypeDef
):
    pass


_RequiredListResourceRecordSetsResponseTypeDef = TypedDict(
    "_RequiredListResourceRecordSetsResponseTypeDef",
    {"ResourceRecordSets": List["ResourceRecordSetTypeDef"], "IsTruncated": bool, "MaxItems": str},
)
_OptionalListResourceRecordSetsResponseTypeDef = TypedDict(
    "_OptionalListResourceRecordSetsResponseTypeDef",
    {
        "NextRecordName": str,
        "NextRecordType": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
        "NextRecordIdentifier": str,
    },
    total=False,
)


class ListResourceRecordSetsResponseTypeDef(
    _RequiredListResourceRecordSetsResponseTypeDef, _OptionalListResourceRecordSetsResponseTypeDef
):
    pass


_RequiredListReusableDelegationSetsResponseTypeDef = TypedDict(
    "_RequiredListReusableDelegationSetsResponseTypeDef",
    {
        "DelegationSets": List["DelegationSetTypeDef"],
        "Marker": str,
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListReusableDelegationSetsResponseTypeDef = TypedDict(
    "_OptionalListReusableDelegationSetsResponseTypeDef", {"NextMarker": str}, total=False
)


class ListReusableDelegationSetsResponseTypeDef(
    _RequiredListReusableDelegationSetsResponseTypeDef,
    _OptionalListReusableDelegationSetsResponseTypeDef,
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"ResourceTagSet": "ResourceTagSetTypeDef"}
)

ListTagsForResourcesResponseTypeDef = TypedDict(
    "ListTagsForResourcesResponseTypeDef", {"ResourceTagSets": List["ResourceTagSetTypeDef"]}
)

ListTrafficPoliciesResponseTypeDef = TypedDict(
    "ListTrafficPoliciesResponseTypeDef",
    {
        "TrafficPolicySummaries": List["TrafficPolicySummaryTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyIdMarker": str,
        "MaxItems": str,
    },
)

_RequiredListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListTrafficPolicyInstancesByHostedZoneResponseTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    {
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
    },
    total=False,
)


class ListTrafficPolicyInstancesByHostedZoneResponseTypeDef(
    _RequiredListTrafficPolicyInstancesByHostedZoneResponseTypeDef,
    _OptionalListTrafficPolicyInstancesByHostedZoneResponseTypeDef,
):
    pass


_RequiredListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListTrafficPolicyInstancesByPolicyResponseTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesByPolicyResponseTypeDef",
    {
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
    },
    total=False,
)


class ListTrafficPolicyInstancesByPolicyResponseTypeDef(
    _RequiredListTrafficPolicyInstancesByPolicyResponseTypeDef,
    _OptionalListTrafficPolicyInstancesByPolicyResponseTypeDef,
):
    pass


_RequiredListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "_RequiredListTrafficPolicyInstancesResponseTypeDef",
    {
        "TrafficPolicyInstances": List["TrafficPolicyInstanceTypeDef"],
        "IsTruncated": bool,
        "MaxItems": str,
    },
)
_OptionalListTrafficPolicyInstancesResponseTypeDef = TypedDict(
    "_OptionalListTrafficPolicyInstancesResponseTypeDef",
    {
        "HostedZoneIdMarker": str,
        "TrafficPolicyInstanceNameMarker": str,
        "TrafficPolicyInstanceTypeMarker": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
    },
    total=False,
)


class ListTrafficPolicyInstancesResponseTypeDef(
    _RequiredListTrafficPolicyInstancesResponseTypeDef,
    _OptionalListTrafficPolicyInstancesResponseTypeDef,
):
    pass


ListTrafficPolicyVersionsResponseTypeDef = TypedDict(
    "ListTrafficPolicyVersionsResponseTypeDef",
    {
        "TrafficPolicies": List["TrafficPolicyTypeDef"],
        "IsTruncated": bool,
        "TrafficPolicyVersionMarker": str,
        "MaxItems": str,
    },
)

_RequiredListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "_RequiredListVPCAssociationAuthorizationsResponseTypeDef",
    {"HostedZoneId": str, "VPCs": List["VPCTypeDef"]},
)
_OptionalListVPCAssociationAuthorizationsResponseTypeDef = TypedDict(
    "_OptionalListVPCAssociationAuthorizationsResponseTypeDef", {"NextToken": str}, total=False
)


class ListVPCAssociationAuthorizationsResponseTypeDef(
    _RequiredListVPCAssociationAuthorizationsResponseTypeDef,
    _OptionalListVPCAssociationAuthorizationsResponseTypeDef,
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TestDNSAnswerResponseTypeDef = TypedDict(
    "TestDNSAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": Literal[
            "SOA",
            "A",
            "TXT",
            "NS",
            "CNAME",
            "MX",
            "NAPTR",
            "PTR",
            "SRV",
            "SPF",
            "AAAA",
            "CAA",
            "DS",
        ],
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
    },
)

UpdateHealthCheckResponseTypeDef = TypedDict(
    "UpdateHealthCheckResponseTypeDef", {"HealthCheck": "HealthCheckTypeDef"}
)

UpdateHostedZoneCommentResponseTypeDef = TypedDict(
    "UpdateHostedZoneCommentResponseTypeDef", {"HostedZone": "HostedZoneTypeDef"}
)

UpdateTrafficPolicyCommentResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyCommentResponseTypeDef", {"TrafficPolicy": "TrafficPolicyTypeDef"}
)

UpdateTrafficPolicyInstanceResponseTypeDef = TypedDict(
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    {"TrafficPolicyInstance": "TrafficPolicyInstanceTypeDef"},
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
