# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for route53 service client

Usage::

    ```python
    import boto3
    from mypy_boto3_route53 import Route53Client

    client: Route53Client = boto3.client("route53")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_route53.paginator import (
    ListHealthChecksPaginator,
    ListHostedZonesPaginator,
    ListQueryLoggingConfigsPaginator,
    ListResourceRecordSetsPaginator,
    ListVPCAssociationAuthorizationsPaginator,
)
from mypy_boto3_route53.type_defs import (
    AlarmIdentifierTypeDef,
    AssociateVPCWithHostedZoneResponseTypeDef,
    ChangeBatchTypeDef,
    ChangeResourceRecordSetsResponseTypeDef,
    CreateHealthCheckResponseTypeDef,
    CreateHostedZoneResponseTypeDef,
    CreateQueryLoggingConfigResponseTypeDef,
    CreateReusableDelegationSetResponseTypeDef,
    CreateTrafficPolicyInstanceResponseTypeDef,
    CreateTrafficPolicyResponseTypeDef,
    CreateTrafficPolicyVersionResponseTypeDef,
    CreateVPCAssociationAuthorizationResponseTypeDef,
    DeleteHostedZoneResponseTypeDef,
    DisassociateVPCFromHostedZoneResponseTypeDef,
    GetAccountLimitResponseTypeDef,
    GetChangeResponseTypeDef,
    GetCheckerIpRangesResponseTypeDef,
    GetGeoLocationResponseTypeDef,
    GetHealthCheckCountResponseTypeDef,
    GetHealthCheckLastFailureReasonResponseTypeDef,
    GetHealthCheckResponseTypeDef,
    GetHealthCheckStatusResponseTypeDef,
    GetHostedZoneCountResponseTypeDef,
    GetHostedZoneLimitResponseTypeDef,
    GetHostedZoneResponseTypeDef,
    GetQueryLoggingConfigResponseTypeDef,
    GetReusableDelegationSetLimitResponseTypeDef,
    GetReusableDelegationSetResponseTypeDef,
    GetTrafficPolicyInstanceCountResponseTypeDef,
    GetTrafficPolicyInstanceResponseTypeDef,
    GetTrafficPolicyResponseTypeDef,
    HealthCheckConfigTypeDef,
    HostedZoneConfigTypeDef,
    ListGeoLocationsResponseTypeDef,
    ListHealthChecksResponseTypeDef,
    ListHostedZonesByNameResponseTypeDef,
    ListHostedZonesByVPCResponseTypeDef,
    ListHostedZonesResponseTypeDef,
    ListQueryLoggingConfigsResponseTypeDef,
    ListResourceRecordSetsResponseTypeDef,
    ListReusableDelegationSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTagsForResourcesResponseTypeDef,
    ListTrafficPoliciesResponseTypeDef,
    ListTrafficPolicyInstancesByHostedZoneResponseTypeDef,
    ListTrafficPolicyInstancesByPolicyResponseTypeDef,
    ListTrafficPolicyInstancesResponseTypeDef,
    ListTrafficPolicyVersionsResponseTypeDef,
    ListVPCAssociationAuthorizationsResponseTypeDef,
    TagTypeDef,
    TestDNSAnswerResponseTypeDef,
    UpdateHealthCheckResponseTypeDef,
    UpdateHostedZoneCommentResponseTypeDef,
    UpdateTrafficPolicyCommentResponseTypeDef,
    UpdateTrafficPolicyInstanceResponseTypeDef,
    VPCTypeDef,
)
from mypy_boto3_route53.waiter import ResourceRecordSetsChangedWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Route53Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModification: Type[BotocoreClientError]
    ConflictingDomainExists: Type[BotocoreClientError]
    ConflictingTypes: Type[BotocoreClientError]
    DelegationSetAlreadyCreated: Type[BotocoreClientError]
    DelegationSetAlreadyReusable: Type[BotocoreClientError]
    DelegationSetInUse: Type[BotocoreClientError]
    DelegationSetNotAvailable: Type[BotocoreClientError]
    DelegationSetNotReusable: Type[BotocoreClientError]
    HealthCheckAlreadyExists: Type[BotocoreClientError]
    HealthCheckInUse: Type[BotocoreClientError]
    HealthCheckVersionMismatch: Type[BotocoreClientError]
    HostedZoneAlreadyExists: Type[BotocoreClientError]
    HostedZoneNotEmpty: Type[BotocoreClientError]
    HostedZoneNotFound: Type[BotocoreClientError]
    HostedZoneNotPrivate: Type[BotocoreClientError]
    IncompatibleVersion: Type[BotocoreClientError]
    InsufficientCloudWatchLogsResourcePolicy: Type[BotocoreClientError]
    InvalidArgument: Type[BotocoreClientError]
    InvalidChangeBatch: Type[BotocoreClientError]
    InvalidDomainName: Type[BotocoreClientError]
    InvalidInput: Type[BotocoreClientError]
    InvalidPaginationToken: Type[BotocoreClientError]
    InvalidTrafficPolicyDocument: Type[BotocoreClientError]
    InvalidVPCId: Type[BotocoreClientError]
    LastVPCAssociation: Type[BotocoreClientError]
    LimitsExceeded: Type[BotocoreClientError]
    NoSuchChange: Type[BotocoreClientError]
    NoSuchCloudWatchLogsLogGroup: Type[BotocoreClientError]
    NoSuchDelegationSet: Type[BotocoreClientError]
    NoSuchGeoLocation: Type[BotocoreClientError]
    NoSuchHealthCheck: Type[BotocoreClientError]
    NoSuchHostedZone: Type[BotocoreClientError]
    NoSuchQueryLoggingConfig: Type[BotocoreClientError]
    NoSuchTrafficPolicy: Type[BotocoreClientError]
    NoSuchTrafficPolicyInstance: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    PriorRequestNotComplete: Type[BotocoreClientError]
    PublicZoneVPCAssociation: Type[BotocoreClientError]
    QueryLoggingConfigAlreadyExists: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    TooManyHealthChecks: Type[BotocoreClientError]
    TooManyHostedZones: Type[BotocoreClientError]
    TooManyTrafficPolicies: Type[BotocoreClientError]
    TooManyTrafficPolicyInstances: Type[BotocoreClientError]
    TooManyTrafficPolicyVersionsForCurrentPolicy: Type[BotocoreClientError]
    TooManyVPCAssociationAuthorizations: Type[BotocoreClientError]
    TrafficPolicyAlreadyExists: Type[BotocoreClientError]
    TrafficPolicyInUse: Type[BotocoreClientError]
    TrafficPolicyInstanceAlreadyExists: Type[BotocoreClientError]
    VPCAssociationAuthorizationNotFound: Type[BotocoreClientError]
    VPCAssociationNotFound: Type[BotocoreClientError]


class Route53Client:
    """
    [Route53.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_vpc_with_hosted_zone(
        self, HostedZoneId: str, VPC: "VPCTypeDef", Comment: str = None
    ) -> AssociateVPCWithHostedZoneResponseTypeDef:
        """
        [Client.associate_vpc_with_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.associate_vpc_with_hosted_zone)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.can_paginate)
        """

    def change_resource_record_sets(
        self, HostedZoneId: str, ChangeBatch: ChangeBatchTypeDef
    ) -> ChangeResourceRecordSetsResponseTypeDef:
        """
        [Client.change_resource_record_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.change_resource_record_sets)
        """

    def change_tags_for_resource(
        self,
        ResourceType: Literal["healthcheck", "hostedzone"],
        ResourceId: str,
        AddTags: List["TagTypeDef"] = None,
        RemoveTagKeys: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Client.change_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.change_tags_for_resource)
        """

    def create_health_check(
        self, CallerReference: str, HealthCheckConfig: "HealthCheckConfigTypeDef"
    ) -> CreateHealthCheckResponseTypeDef:
        """
        [Client.create_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.create_health_check)
        """

    def create_hosted_zone(
        self,
        Name: str,
        CallerReference: str,
        VPC: "VPCTypeDef" = None,
        HostedZoneConfig: "HostedZoneConfigTypeDef" = None,
        DelegationSetId: str = None,
    ) -> CreateHostedZoneResponseTypeDef:
        """
        [Client.create_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.create_hosted_zone)
        """

    def create_query_logging_config(
        self, HostedZoneId: str, CloudWatchLogsLogGroupArn: str
    ) -> CreateQueryLoggingConfigResponseTypeDef:
        """
        [Client.create_query_logging_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.create_query_logging_config)
        """

    def create_reusable_delegation_set(
        self, CallerReference: str, HostedZoneId: str = None
    ) -> CreateReusableDelegationSetResponseTypeDef:
        """
        [Client.create_reusable_delegation_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.create_reusable_delegation_set)
        """

    def create_traffic_policy(
        self, Name: str, Document: str, Comment: str = None
    ) -> CreateTrafficPolicyResponseTypeDef:
        """
        [Client.create_traffic_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.create_traffic_policy)
        """

    def create_traffic_policy_instance(
        self,
        HostedZoneId: str,
        Name: str,
        TTL: int,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
    ) -> CreateTrafficPolicyInstanceResponseTypeDef:
        """
        [Client.create_traffic_policy_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.create_traffic_policy_instance)
        """

    def create_traffic_policy_version(
        self, Id: str, Document: str, Comment: str = None
    ) -> CreateTrafficPolicyVersionResponseTypeDef:
        """
        [Client.create_traffic_policy_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.create_traffic_policy_version)
        """

    def create_vpc_association_authorization(
        self, HostedZoneId: str, VPC: "VPCTypeDef"
    ) -> CreateVPCAssociationAuthorizationResponseTypeDef:
        """
        [Client.create_vpc_association_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.create_vpc_association_authorization)
        """

    def delete_health_check(self, HealthCheckId: str) -> Dict[str, Any]:
        """
        [Client.delete_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.delete_health_check)
        """

    def delete_hosted_zone(self, Id: str) -> DeleteHostedZoneResponseTypeDef:
        """
        [Client.delete_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.delete_hosted_zone)
        """

    def delete_query_logging_config(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_query_logging_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.delete_query_logging_config)
        """

    def delete_reusable_delegation_set(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_reusable_delegation_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.delete_reusable_delegation_set)
        """

    def delete_traffic_policy(self, Id: str, Version: int) -> Dict[str, Any]:
        """
        [Client.delete_traffic_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.delete_traffic_policy)
        """

    def delete_traffic_policy_instance(self, Id: str) -> Dict[str, Any]:
        """
        [Client.delete_traffic_policy_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.delete_traffic_policy_instance)
        """

    def delete_vpc_association_authorization(
        self, HostedZoneId: str, VPC: "VPCTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.delete_vpc_association_authorization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.delete_vpc_association_authorization)
        """

    def disassociate_vpc_from_hosted_zone(
        self, HostedZoneId: str, VPC: "VPCTypeDef", Comment: str = None
    ) -> DisassociateVPCFromHostedZoneResponseTypeDef:
        """
        [Client.disassociate_vpc_from_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.disassociate_vpc_from_hosted_zone)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.generate_presigned_url)
        """

    def get_account_limit(
        self,
        Type: Literal[
            "MAX_HEALTH_CHECKS_BY_OWNER",
            "MAX_HOSTED_ZONES_BY_OWNER",
            "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER",
            "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER",
            "MAX_TRAFFIC_POLICIES_BY_OWNER",
        ],
    ) -> GetAccountLimitResponseTypeDef:
        """
        [Client.get_account_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_account_limit)
        """

    def get_change(self, Id: str) -> GetChangeResponseTypeDef:
        """
        [Client.get_change documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_change)
        """

    def get_checker_ip_ranges(self) -> GetCheckerIpRangesResponseTypeDef:
        """
        [Client.get_checker_ip_ranges documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_checker_ip_ranges)
        """

    def get_geo_location(
        self, ContinentCode: str = None, CountryCode: str = None, SubdivisionCode: str = None
    ) -> GetGeoLocationResponseTypeDef:
        """
        [Client.get_geo_location documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_geo_location)
        """

    def get_health_check(self, HealthCheckId: str) -> GetHealthCheckResponseTypeDef:
        """
        [Client.get_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_health_check)
        """

    def get_health_check_count(self) -> GetHealthCheckCountResponseTypeDef:
        """
        [Client.get_health_check_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_health_check_count)
        """

    def get_health_check_last_failure_reason(
        self, HealthCheckId: str
    ) -> GetHealthCheckLastFailureReasonResponseTypeDef:
        """
        [Client.get_health_check_last_failure_reason documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_health_check_last_failure_reason)
        """

    def get_health_check_status(self, HealthCheckId: str) -> GetHealthCheckStatusResponseTypeDef:
        """
        [Client.get_health_check_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_health_check_status)
        """

    def get_hosted_zone(self, Id: str) -> GetHostedZoneResponseTypeDef:
        """
        [Client.get_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_hosted_zone)
        """

    def get_hosted_zone_count(self) -> GetHostedZoneCountResponseTypeDef:
        """
        [Client.get_hosted_zone_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_hosted_zone_count)
        """

    def get_hosted_zone_limit(
        self, Type: Literal["MAX_RRSETS_BY_ZONE", "MAX_VPCS_ASSOCIATED_BY_ZONE"], HostedZoneId: str
    ) -> GetHostedZoneLimitResponseTypeDef:
        """
        [Client.get_hosted_zone_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_hosted_zone_limit)
        """

    def get_query_logging_config(self, Id: str) -> GetQueryLoggingConfigResponseTypeDef:
        """
        [Client.get_query_logging_config documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_query_logging_config)
        """

    def get_reusable_delegation_set(self, Id: str) -> GetReusableDelegationSetResponseTypeDef:
        """
        [Client.get_reusable_delegation_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_reusable_delegation_set)
        """

    def get_reusable_delegation_set_limit(
        self, Type: Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"], DelegationSetId: str
    ) -> GetReusableDelegationSetLimitResponseTypeDef:
        """
        [Client.get_reusable_delegation_set_limit documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_reusable_delegation_set_limit)
        """

    def get_traffic_policy(self, Id: str, Version: int) -> GetTrafficPolicyResponseTypeDef:
        """
        [Client.get_traffic_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_traffic_policy)
        """

    def get_traffic_policy_instance(self, Id: str) -> GetTrafficPolicyInstanceResponseTypeDef:
        """
        [Client.get_traffic_policy_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_traffic_policy_instance)
        """

    def get_traffic_policy_instance_count(self) -> GetTrafficPolicyInstanceCountResponseTypeDef:
        """
        [Client.get_traffic_policy_instance_count documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.get_traffic_policy_instance_count)
        """

    def list_geo_locations(
        self,
        StartContinentCode: str = None,
        StartCountryCode: str = None,
        StartSubdivisionCode: str = None,
        MaxItems: str = None,
    ) -> ListGeoLocationsResponseTypeDef:
        """
        [Client.list_geo_locations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_geo_locations)
        """

    def list_health_checks(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListHealthChecksResponseTypeDef:
        """
        [Client.list_health_checks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_health_checks)
        """

    def list_hosted_zones(
        self, Marker: str = None, MaxItems: str = None, DelegationSetId: str = None
    ) -> ListHostedZonesResponseTypeDef:
        """
        [Client.list_hosted_zones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_hosted_zones)
        """

    def list_hosted_zones_by_name(
        self, DNSName: str = None, HostedZoneId: str = None, MaxItems: str = None
    ) -> ListHostedZonesByNameResponseTypeDef:
        """
        [Client.list_hosted_zones_by_name documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_hosted_zones_by_name)
        """

    def list_hosted_zones_by_vpc(
        self,
        VPCId: str,
        VPCRegion: Literal[
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
        MaxItems: str = None,
        NextToken: str = None,
    ) -> ListHostedZonesByVPCResponseTypeDef:
        """
        [Client.list_hosted_zones_by_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_hosted_zones_by_vpc)
        """

    def list_query_logging_configs(
        self, HostedZoneId: str = None, NextToken: str = None, MaxResults: str = None
    ) -> ListQueryLoggingConfigsResponseTypeDef:
        """
        [Client.list_query_logging_configs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_query_logging_configs)
        """

    def list_resource_record_sets(
        self,
        HostedZoneId: str,
        StartRecordName: str = None,
        StartRecordType: Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ] = None,
        StartRecordIdentifier: str = None,
        MaxItems: str = None,
    ) -> ListResourceRecordSetsResponseTypeDef:
        """
        [Client.list_resource_record_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_resource_record_sets)
        """

    def list_reusable_delegation_sets(
        self, Marker: str = None, MaxItems: str = None
    ) -> ListReusableDelegationSetsResponseTypeDef:
        """
        [Client.list_reusable_delegation_sets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_reusable_delegation_sets)
        """

    def list_tags_for_resource(
        self, ResourceType: Literal["healthcheck", "hostedzone"], ResourceId: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_tags_for_resource)
        """

    def list_tags_for_resources(
        self, ResourceType: Literal["healthcheck", "hostedzone"], ResourceIds: List[str]
    ) -> ListTagsForResourcesResponseTypeDef:
        """
        [Client.list_tags_for_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_tags_for_resources)
        """

    def list_traffic_policies(
        self, TrafficPolicyIdMarker: str = None, MaxItems: str = None
    ) -> ListTrafficPoliciesResponseTypeDef:
        """
        [Client.list_traffic_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_traffic_policies)
        """

    def list_traffic_policy_instances(
        self,
        HostedZoneIdMarker: str = None,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ] = None,
        MaxItems: str = None,
    ) -> ListTrafficPolicyInstancesResponseTypeDef:
        """
        [Client.list_traffic_policy_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_traffic_policy_instances)
        """

    def list_traffic_policy_instances_by_hosted_zone(
        self,
        HostedZoneId: str,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ] = None,
        MaxItems: str = None,
    ) -> ListTrafficPolicyInstancesByHostedZoneResponseTypeDef:
        """
        [Client.list_traffic_policy_instances_by_hosted_zone documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_traffic_policy_instances_by_hosted_zone)
        """

    def list_traffic_policy_instances_by_policy(
        self,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
        HostedZoneIdMarker: str = None,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ] = None,
        MaxItems: str = None,
    ) -> ListTrafficPolicyInstancesByPolicyResponseTypeDef:
        """
        [Client.list_traffic_policy_instances_by_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_traffic_policy_instances_by_policy)
        """

    def list_traffic_policy_versions(
        self, Id: str, TrafficPolicyVersionMarker: str = None, MaxItems: str = None
    ) -> ListTrafficPolicyVersionsResponseTypeDef:
        """
        [Client.list_traffic_policy_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_traffic_policy_versions)
        """

    def list_vpc_association_authorizations(
        self, HostedZoneId: str, NextToken: str = None, MaxResults: str = None
    ) -> ListVPCAssociationAuthorizationsResponseTypeDef:
        """
        [Client.list_vpc_association_authorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.list_vpc_association_authorizations)
        """

    def test_dns_answer(
        self,
        HostedZoneId: str,
        RecordName: str,
        RecordType: Literal[
            "SOA", "A", "TXT", "NS", "CNAME", "MX", "NAPTR", "PTR", "SRV", "SPF", "AAAA", "CAA"
        ],
        ResolverIP: str = None,
        EDNS0ClientSubnetIP: str = None,
        EDNS0ClientSubnetMask: str = None,
    ) -> TestDNSAnswerResponseTypeDef:
        """
        [Client.test_dns_answer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.test_dns_answer)
        """

    def update_health_check(
        self,
        HealthCheckId: str,
        HealthCheckVersion: int = None,
        IPAddress: str = None,
        Port: int = None,
        ResourcePath: str = None,
        FullyQualifiedDomainName: str = None,
        SearchString: str = None,
        FailureThreshold: int = None,
        Inverted: bool = None,
        Disabled: bool = None,
        HealthThreshold: int = None,
        ChildHealthChecks: List[str] = None,
        EnableSNI: bool = None,
        Regions: List[
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
        ] = None,
        AlarmIdentifier: "AlarmIdentifierTypeDef" = None,
        InsufficientDataHealthStatus: Literal["Healthy", "Unhealthy", "LastKnownStatus"] = None,
        ResetElements: List[
            Literal["FullyQualifiedDomainName", "Regions", "ResourcePath", "ChildHealthChecks"]
        ] = None,
    ) -> UpdateHealthCheckResponseTypeDef:
        """
        [Client.update_health_check documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.update_health_check)
        """

    def update_hosted_zone_comment(
        self, Id: str, Comment: str = None
    ) -> UpdateHostedZoneCommentResponseTypeDef:
        """
        [Client.update_hosted_zone_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.update_hosted_zone_comment)
        """

    def update_traffic_policy_comment(
        self, Id: str, Version: int, Comment: str
    ) -> UpdateTrafficPolicyCommentResponseTypeDef:
        """
        [Client.update_traffic_policy_comment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.update_traffic_policy_comment)
        """

    def update_traffic_policy_instance(
        self, Id: str, TTL: int, TrafficPolicyId: str, TrafficPolicyVersion: int
    ) -> UpdateTrafficPolicyInstanceResponseTypeDef:
        """
        [Client.update_traffic_policy_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Client.update_traffic_policy_instance)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_health_checks"]
    ) -> ListHealthChecksPaginator:
        """
        [Paginator.ListHealthChecks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListHealthChecks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hosted_zones"]
    ) -> ListHostedZonesPaginator:
        """
        [Paginator.ListHostedZones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListHostedZones)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_query_logging_configs"]
    ) -> ListQueryLoggingConfigsPaginator:
        """
        [Paginator.ListQueryLoggingConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_record_sets"]
    ) -> ListResourceRecordSetsPaginator:
        """
        [Paginator.ListResourceRecordSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_vpc_association_authorizations"]
    ) -> ListVPCAssociationAuthorizationsPaginator:
        """
        [Paginator.ListVPCAssociationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations)
        """

    def get_waiter(
        self, waiter_name: Literal["resource_record_sets_changed"]
    ) -> ResourceRecordSetsChangedWaiter:
        """
        [Waiter.ResourceRecordSetsChanged documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged)
        """
