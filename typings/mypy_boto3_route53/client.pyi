"""
Type annotations for route53 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_route53 import Route53Client

    client: Route53Client = boto3.client("route53")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AccountLimitTypeType,
    HealthCheckRegionType,
    HostedZoneLimitTypeType,
    InsufficientDataHealthStatusType,
    ResettableElementNameType,
    RRTypeType,
    TagResourceTypeType,
    VPCRegionType,
)
from .paginator import (
    ListCidrBlocksPaginator,
    ListCidrCollectionsPaginator,
    ListCidrLocationsPaginator,
    ListHealthChecksPaginator,
    ListHostedZonesPaginator,
    ListQueryLoggingConfigsPaginator,
    ListResourceRecordSetsPaginator,
    ListVPCAssociationAuthorizationsPaginator,
)
from .type_defs import (
    ActivateKeySigningKeyResponseTypeDef,
    AlarmIdentifierTypeDef,
    AssociateVPCWithHostedZoneResponseTypeDef,
    ChangeBatchTypeDef,
    ChangeCidrCollectionResponseTypeDef,
    ChangeResourceRecordSetsResponseTypeDef,
    CidrCollectionChangeTypeDef,
    CreateCidrCollectionResponseTypeDef,
    CreateHealthCheckResponseTypeDef,
    CreateHostedZoneResponseTypeDef,
    CreateKeySigningKeyResponseTypeDef,
    CreateQueryLoggingConfigResponseTypeDef,
    CreateReusableDelegationSetResponseTypeDef,
    CreateTrafficPolicyInstanceResponseTypeDef,
    CreateTrafficPolicyResponseTypeDef,
    CreateTrafficPolicyVersionResponseTypeDef,
    CreateVPCAssociationAuthorizationResponseTypeDef,
    DeactivateKeySigningKeyResponseTypeDef,
    DeleteHostedZoneResponseTypeDef,
    DeleteKeySigningKeyResponseTypeDef,
    DisableHostedZoneDNSSECResponseTypeDef,
    DisassociateVPCFromHostedZoneResponseTypeDef,
    EnableHostedZoneDNSSECResponseTypeDef,
    GetAccountLimitResponseTypeDef,
    GetChangeResponseTypeDef,
    GetCheckerIpRangesResponseTypeDef,
    GetDNSSECResponseTypeDef,
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
    ListCidrBlocksResponseTypeDef,
    ListCidrCollectionsResponseTypeDef,
    ListCidrLocationsResponseTypeDef,
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
from .waiter import ResourceRecordSetsChangedWaiter

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
    CidrBlockInUseException: Type[BotocoreClientError]
    CidrCollectionAlreadyExistsException: Type[BotocoreClientError]
    CidrCollectionInUseException: Type[BotocoreClientError]
    CidrCollectionVersionMismatchException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModification: Type[BotocoreClientError]
    ConflictingDomainExists: Type[BotocoreClientError]
    ConflictingTypes: Type[BotocoreClientError]
    DNSSECNotFound: Type[BotocoreClientError]
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
    HostedZonePartiallyDelegated: Type[BotocoreClientError]
    IncompatibleVersion: Type[BotocoreClientError]
    InsufficientCloudWatchLogsResourcePolicy: Type[BotocoreClientError]
    InvalidArgument: Type[BotocoreClientError]
    InvalidChangeBatch: Type[BotocoreClientError]
    InvalidDomainName: Type[BotocoreClientError]
    InvalidInput: Type[BotocoreClientError]
    InvalidKMSArn: Type[BotocoreClientError]
    InvalidKeySigningKeyName: Type[BotocoreClientError]
    InvalidKeySigningKeyStatus: Type[BotocoreClientError]
    InvalidPaginationToken: Type[BotocoreClientError]
    InvalidSigningStatus: Type[BotocoreClientError]
    InvalidTrafficPolicyDocument: Type[BotocoreClientError]
    InvalidVPCId: Type[BotocoreClientError]
    KeySigningKeyAlreadyExists: Type[BotocoreClientError]
    KeySigningKeyInParentDSRecord: Type[BotocoreClientError]
    KeySigningKeyInUse: Type[BotocoreClientError]
    KeySigningKeyWithActiveStatusNotFound: Type[BotocoreClientError]
    LastVPCAssociation: Type[BotocoreClientError]
    LimitsExceeded: Type[BotocoreClientError]
    NoSuchChange: Type[BotocoreClientError]
    NoSuchCidrCollectionException: Type[BotocoreClientError]
    NoSuchCidrLocationException: Type[BotocoreClientError]
    NoSuchCloudWatchLogsLogGroup: Type[BotocoreClientError]
    NoSuchDelegationSet: Type[BotocoreClientError]
    NoSuchGeoLocation: Type[BotocoreClientError]
    NoSuchHealthCheck: Type[BotocoreClientError]
    NoSuchHostedZone: Type[BotocoreClientError]
    NoSuchKeySigningKey: Type[BotocoreClientError]
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
    TooManyKeySigningKeys: Type[BotocoreClientError]
    TooManyTrafficPolicies: Type[BotocoreClientError]
    TooManyTrafficPolicyInstances: Type[BotocoreClientError]
    TooManyTrafficPolicyVersionsForCurrentPolicy: Type[BotocoreClientError]
    TooManyVPCAssociationAuthorizations: Type[BotocoreClientError]
    TrafficPolicyAlreadyExists: Type[BotocoreClientError]
    TrafficPolicyInUse: Type[BotocoreClientError]
    TrafficPolicyInstanceAlreadyExists: Type[BotocoreClientError]
    VPCAssociationAuthorizationNotFound: Type[BotocoreClientError]
    VPCAssociationNotFound: Type[BotocoreClientError]

class Route53Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        Route53Client exceptions.
        """
    def activate_key_signing_key(
        self, *, HostedZoneId: str, Name: str
    ) -> ActivateKeySigningKeyResponseTypeDef:
        """
        Activates a key-signing key (KSK) so that it can be used for signing by DNSSEC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.activate_key_signing_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#activate_key_signing_key)
        """
    def associate_vpc_with_hosted_zone(
        self, *, HostedZoneId: str, VPC: "VPCTypeDef", Comment: str = None
    ) -> AssociateVPCWithHostedZoneResponseTypeDef:
        """
        Associates an Amazon VPC with a private hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.associate_vpc_with_hosted_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#associate_vpc_with_hosted_zone)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#can_paginate)
        """
    def change_cidr_collection(
        self,
        *,
        Id: str,
        Changes: List["CidrCollectionChangeTypeDef"],
        CollectionVersion: int = None
    ) -> ChangeCidrCollectionResponseTypeDef:
        """
        Creates, changes, or deletes CIDR blocks within a collection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.change_cidr_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#change_cidr_collection)
        """
    def change_resource_record_sets(
        self, *, HostedZoneId: str, ChangeBatch: "ChangeBatchTypeDef"
    ) -> ChangeResourceRecordSetsResponseTypeDef:
        """
        Creates, changes, or deletes a resource record set, which contains authoritative
        DNS information for a specified domain name or subdomain name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.change_resource_record_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#change_resource_record_sets)
        """
    def change_tags_for_resource(
        self,
        *,
        ResourceType: TagResourceTypeType,
        ResourceId: str,
        AddTags: List["TagTypeDef"] = None,
        RemoveTagKeys: List[str] = None
    ) -> Dict[str, Any]:
        """
        Adds, edits, or deletes tags for a health check or a hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.change_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#change_tags_for_resource)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#close)
        """
    def create_cidr_collection(
        self, *, Name: str, CallerReference: str
    ) -> CreateCidrCollectionResponseTypeDef:
        """
        Creates a CIDR collection in the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_cidr_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_cidr_collection)
        """
    def create_health_check(
        self, *, CallerReference: str, HealthCheckConfig: "HealthCheckConfigTypeDef"
    ) -> CreateHealthCheckResponseTypeDef:
        """
        Creates a new health check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_health_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_health_check)
        """
    def create_hosted_zone(
        self,
        *,
        Name: str,
        CallerReference: str,
        VPC: "VPCTypeDef" = None,
        HostedZoneConfig: "HostedZoneConfigTypeDef" = None,
        DelegationSetId: str = None
    ) -> CreateHostedZoneResponseTypeDef:
        """
        Creates a new public or private hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_hosted_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_hosted_zone)
        """
    def create_key_signing_key(
        self,
        *,
        CallerReference: str,
        HostedZoneId: str,
        KeyManagementServiceArn: str,
        Name: str,
        Status: str
    ) -> CreateKeySigningKeyResponseTypeDef:
        """
        Creates a new key-signing key (KSK) associated with a hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_key_signing_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_key_signing_key)
        """
    def create_query_logging_config(
        self, *, HostedZoneId: str, CloudWatchLogsLogGroupArn: str
    ) -> CreateQueryLoggingConfigResponseTypeDef:
        """
        Creates a configuration for DNS query logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_query_logging_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_query_logging_config)
        """
    def create_reusable_delegation_set(
        self, *, CallerReference: str, HostedZoneId: str = None
    ) -> CreateReusableDelegationSetResponseTypeDef:
        """
        Creates a delegation set (a group of four name servers) that can be reused by
        multiple hosted zones that were created by the same Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_reusable_delegation_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_reusable_delegation_set)
        """
    def create_traffic_policy(
        self, *, Name: str, Document: str, Comment: str = None
    ) -> CreateTrafficPolicyResponseTypeDef:
        """
        Creates a traffic policy, which you use to create multiple DNS resource record
        sets for one domain name (such as example.com) or one subdomain name (such as
        www.example.com).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_traffic_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_traffic_policy)
        """
    def create_traffic_policy_instance(
        self,
        *,
        HostedZoneId: str,
        Name: str,
        TTL: int,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int
    ) -> CreateTrafficPolicyInstanceResponseTypeDef:
        """
        Creates resource record sets in a specified hosted zone based on the settings in
        a specified traffic policy version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_traffic_policy_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_traffic_policy_instance)
        """
    def create_traffic_policy_version(
        self, *, Id: str, Document: str, Comment: str = None
    ) -> CreateTrafficPolicyVersionResponseTypeDef:
        """
        Creates a new version of an existing traffic policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_traffic_policy_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_traffic_policy_version)
        """
    def create_vpc_association_authorization(
        self, *, HostedZoneId: str, VPC: "VPCTypeDef"
    ) -> CreateVPCAssociationAuthorizationResponseTypeDef:
        """
        Authorizes the Amazon Web Services account that created a specified VPC to
        submit an `AssociateVPCWithHostedZone` request to associate the VPC with a
        specified hosted zone that was created by a different account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.create_vpc_association_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#create_vpc_association_authorization)
        """
    def deactivate_key_signing_key(
        self, *, HostedZoneId: str, Name: str
    ) -> DeactivateKeySigningKeyResponseTypeDef:
        """
        Deactivates a key-signing key (KSK) so that it will not be used for signing by
        DNSSEC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.deactivate_key_signing_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#deactivate_key_signing_key)
        """
    def delete_cidr_collection(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a CIDR collection in the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_cidr_collection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_cidr_collection)
        """
    def delete_health_check(self, *, HealthCheckId: str) -> Dict[str, Any]:
        """
        Deletes a health check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_health_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_health_check)
        """
    def delete_hosted_zone(self, *, Id: str) -> DeleteHostedZoneResponseTypeDef:
        """
        Deletes a hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_hosted_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_hosted_zone)
        """
    def delete_key_signing_key(
        self, *, HostedZoneId: str, Name: str
    ) -> DeleteKeySigningKeyResponseTypeDef:
        """
        Deletes a key-signing key (KSK).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_key_signing_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_key_signing_key)
        """
    def delete_query_logging_config(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a configuration for DNS query logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_query_logging_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_query_logging_config)
        """
    def delete_reusable_delegation_set(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a reusable delegation set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_reusable_delegation_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_reusable_delegation_set)
        """
    def delete_traffic_policy(self, *, Id: str, Version: int) -> Dict[str, Any]:
        """
        Deletes a traffic policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_traffic_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_traffic_policy)
        """
    def delete_traffic_policy_instance(self, *, Id: str) -> Dict[str, Any]:
        """
        Deletes a traffic policy instance and all of the resource record sets that
        Amazon Route 53 created when you created the instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_traffic_policy_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_traffic_policy_instance)
        """
    def delete_vpc_association_authorization(
        self, *, HostedZoneId: str, VPC: "VPCTypeDef"
    ) -> Dict[str, Any]:
        """
        Removes authorization to submit an `AssociateVPCWithHostedZone` request to
        associate a specified VPC with a hosted zone that was created by a different
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.delete_vpc_association_authorization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#delete_vpc_association_authorization)
        """
    def disable_hosted_zone_dnssec(
        self, *, HostedZoneId: str
    ) -> DisableHostedZoneDNSSECResponseTypeDef:
        """
        Disables DNSSEC signing in a specific hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.disable_hosted_zone_dnssec)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#disable_hosted_zone_dnssec)
        """
    def disassociate_vpc_from_hosted_zone(
        self, *, HostedZoneId: str, VPC: "VPCTypeDef", Comment: str = None
    ) -> DisassociateVPCFromHostedZoneResponseTypeDef:
        """
        Disassociates an Amazon Virtual Private Cloud (Amazon VPC) from an Amazon Route
        53 private hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.disassociate_vpc_from_hosted_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#disassociate_vpc_from_hosted_zone)
        """
    def enable_hosted_zone_dnssec(
        self, *, HostedZoneId: str
    ) -> EnableHostedZoneDNSSECResponseTypeDef:
        """
        Enables DNSSEC signing in a specific hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.enable_hosted_zone_dnssec)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#enable_hosted_zone_dnssec)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#generate_presigned_url)
        """
    def get_account_limit(self, *, Type: AccountLimitTypeType) -> GetAccountLimitResponseTypeDef:
        """
        Gets the specified limit for the current account, for example, the maximum
        number of health checks that you can create using the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_account_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_account_limit)
        """
    def get_change(self, *, Id: str) -> GetChangeResponseTypeDef:
        """
        Returns the current status of a change batch request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_change)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_change)
        """
    def get_checker_ip_ranges(self) -> GetCheckerIpRangesResponseTypeDef:
        """
        Route 53 does not perform authorization for this API because it retrieves
        information that is already available to the public.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_checker_ip_ranges)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_checker_ip_ranges)
        """
    def get_dnssec(self, *, HostedZoneId: str) -> GetDNSSECResponseTypeDef:
        """
        Returns information about DNSSEC for a specific hosted zone, including the key-
        signing keys (KSKs) in the hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_dnssec)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_dnssec)
        """
    def get_geo_location(
        self, *, ContinentCode: str = None, CountryCode: str = None, SubdivisionCode: str = None
    ) -> GetGeoLocationResponseTypeDef:
        """
        Gets information about whether a specified geographic location is supported for
        Amazon Route 53 geolocation resource record sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_geo_location)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_geo_location)
        """
    def get_health_check(self, *, HealthCheckId: str) -> GetHealthCheckResponseTypeDef:
        """
        Gets information about a specified health check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_health_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_health_check)
        """
    def get_health_check_count(self) -> GetHealthCheckCountResponseTypeDef:
        """
        Retrieves the number of health checks that are associated with the current
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_health_check_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_health_check_count)
        """
    def get_health_check_last_failure_reason(
        self, *, HealthCheckId: str
    ) -> GetHealthCheckLastFailureReasonResponseTypeDef:
        """
        Gets the reason that a specified health check failed most recently.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_health_check_last_failure_reason)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_health_check_last_failure_reason)
        """
    def get_health_check_status(self, *, HealthCheckId: str) -> GetHealthCheckStatusResponseTypeDef:
        """
        Gets status of a specified health check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_health_check_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_health_check_status)
        """
    def get_hosted_zone(self, *, Id: str) -> GetHostedZoneResponseTypeDef:
        """
        Gets information about a specified hosted zone including the four name servers
        assigned to the hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_hosted_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_hosted_zone)
        """
    def get_hosted_zone_count(self) -> GetHostedZoneCountResponseTypeDef:
        """
        Retrieves the number of hosted zones that are associated with the current Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_hosted_zone_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_hosted_zone_count)
        """
    def get_hosted_zone_limit(
        self, *, Type: HostedZoneLimitTypeType, HostedZoneId: str
    ) -> GetHostedZoneLimitResponseTypeDef:
        """
        Gets the specified limit for a specified hosted zone, for example, the maximum
        number of records that you can create in the hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_hosted_zone_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_hosted_zone_limit)
        """
    def get_query_logging_config(self, *, Id: str) -> GetQueryLoggingConfigResponseTypeDef:
        """
        Gets information about a specified configuration for DNS query logging.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_query_logging_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_query_logging_config)
        """
    def get_reusable_delegation_set(self, *, Id: str) -> GetReusableDelegationSetResponseTypeDef:
        """
        Retrieves information about a specified reusable delegation set, including the
        four name servers that are assigned to the delegation set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_reusable_delegation_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_reusable_delegation_set)
        """
    def get_reusable_delegation_set_limit(
        self, *, Type: Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"], DelegationSetId: str
    ) -> GetReusableDelegationSetLimitResponseTypeDef:
        """
        Gets the maximum number of hosted zones that you can associate with the
        specified reusable delegation set.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_reusable_delegation_set_limit)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_reusable_delegation_set_limit)
        """
    def get_traffic_policy(self, *, Id: str, Version: int) -> GetTrafficPolicyResponseTypeDef:
        """
        Gets information about a specific traffic policy version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_traffic_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_traffic_policy)
        """
    def get_traffic_policy_instance(self, *, Id: str) -> GetTrafficPolicyInstanceResponseTypeDef:
        """
        Gets information about a specified traffic policy instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_traffic_policy_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_traffic_policy_instance)
        """
    def get_traffic_policy_instance_count(self) -> GetTrafficPolicyInstanceCountResponseTypeDef:
        """
        Gets the number of traffic policy instances that are associated with the current
        Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.get_traffic_policy_instance_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#get_traffic_policy_instance_count)
        """
    def list_cidr_blocks(
        self,
        *,
        CollectionId: str,
        LocationName: str = None,
        NextToken: str = None,
        MaxResults: str = None
    ) -> ListCidrBlocksResponseTypeDef:
        """
        Returns a paginated list of location objects and their CIDR blocks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_cidr_blocks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_cidr_blocks)
        """
    def list_cidr_collections(
        self, *, NextToken: str = None, MaxResults: str = None
    ) -> ListCidrCollectionsResponseTypeDef:
        """
        Returns a paginated list of CIDR collections in the Amazon Web Services account
        (metadata only).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_cidr_collections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_cidr_collections)
        """
    def list_cidr_locations(
        self, *, CollectionId: str, NextToken: str = None, MaxResults: str = None
    ) -> ListCidrLocationsResponseTypeDef:
        """
        Returns a paginated list of CIDR locations for the given collection (metadata
        only, does not include CIDR blocks).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_cidr_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_cidr_locations)
        """
    def list_geo_locations(
        self,
        *,
        StartContinentCode: str = None,
        StartCountryCode: str = None,
        StartSubdivisionCode: str = None,
        MaxItems: str = None
    ) -> ListGeoLocationsResponseTypeDef:
        """
        Retrieves a list of supported geographic locations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_geo_locations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_geo_locations)
        """
    def list_health_checks(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListHealthChecksResponseTypeDef:
        """
        Retrieve a list of the health checks that are associated with the current Amazon
        Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_health_checks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_health_checks)
        """
    def list_hosted_zones(
        self,
        *,
        Marker: str = None,
        MaxItems: str = None,
        DelegationSetId: str = None,
        HostedZoneType: Literal["PrivateHostedZone"] = None
    ) -> ListHostedZonesResponseTypeDef:
        """
        Retrieves a list of the public and private hosted zones that are associated with
        the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_hosted_zones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_hosted_zones)
        """
    def list_hosted_zones_by_name(
        self, *, DNSName: str = None, HostedZoneId: str = None, MaxItems: str = None
    ) -> ListHostedZonesByNameResponseTypeDef:
        """
        Retrieves a list of your hosted zones in lexicographic order.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_hosted_zones_by_name)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_hosted_zones_by_name)
        """
    def list_hosted_zones_by_vpc(
        self, *, VPCId: str, VPCRegion: VPCRegionType, MaxItems: str = None, NextToken: str = None
    ) -> ListHostedZonesByVPCResponseTypeDef:
        """
        Lists all the private hosted zones that a specified VPC is associated with,
        regardless of which Amazon Web Services account or Amazon Web Services service
        owns the hosted zones.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_hosted_zones_by_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_hosted_zones_by_vpc)
        """
    def list_query_logging_configs(
        self, *, HostedZoneId: str = None, NextToken: str = None, MaxResults: str = None
    ) -> ListQueryLoggingConfigsResponseTypeDef:
        """
        Lists the configurations for DNS query logging that are associated with the
        current Amazon Web Services account or the configuration that is associated with
        a specified hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_query_logging_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_query_logging_configs)
        """
    def list_resource_record_sets(
        self,
        *,
        HostedZoneId: str,
        StartRecordName: str = None,
        StartRecordType: RRTypeType = None,
        StartRecordIdentifier: str = None,
        MaxItems: str = None
    ) -> ListResourceRecordSetsResponseTypeDef:
        """
        Lists the resource record sets in a specified hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_resource_record_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_resource_record_sets)
        """
    def list_reusable_delegation_sets(
        self, *, Marker: str = None, MaxItems: str = None
    ) -> ListReusableDelegationSetsResponseTypeDef:
        """
        Retrieves a list of the reusable delegation sets that are associated with the
        current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_reusable_delegation_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_reusable_delegation_sets)
        """
    def list_tags_for_resource(
        self, *, ResourceType: TagResourceTypeType, ResourceId: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists tags for one health check or hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_tags_for_resource)
        """
    def list_tags_for_resources(
        self, *, ResourceType: TagResourceTypeType, ResourceIds: List[str]
    ) -> ListTagsForResourcesResponseTypeDef:
        """
        Lists tags for up to 10 health checks or hosted zones.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_tags_for_resources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_tags_for_resources)
        """
    def list_traffic_policies(
        self, *, TrafficPolicyIdMarker: str = None, MaxItems: str = None
    ) -> ListTrafficPoliciesResponseTypeDef:
        """
        Gets information about the latest version for every traffic policy that is
        associated with the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_traffic_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_traffic_policies)
        """
    def list_traffic_policy_instances(
        self,
        *,
        HostedZoneIdMarker: str = None,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: RRTypeType = None,
        MaxItems: str = None
    ) -> ListTrafficPolicyInstancesResponseTypeDef:
        """
        Gets information about the traffic policy instances that you created by using
        the current Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_traffic_policy_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_traffic_policy_instances)
        """
    def list_traffic_policy_instances_by_hosted_zone(
        self,
        *,
        HostedZoneId: str,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: RRTypeType = None,
        MaxItems: str = None
    ) -> ListTrafficPolicyInstancesByHostedZoneResponseTypeDef:
        """
        Gets information about the traffic policy instances that you created in a
        specified hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_traffic_policy_instances_by_hosted_zone)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_traffic_policy_instances_by_hosted_zone)
        """
    def list_traffic_policy_instances_by_policy(
        self,
        *,
        TrafficPolicyId: str,
        TrafficPolicyVersion: int,
        HostedZoneIdMarker: str = None,
        TrafficPolicyInstanceNameMarker: str = None,
        TrafficPolicyInstanceTypeMarker: RRTypeType = None,
        MaxItems: str = None
    ) -> ListTrafficPolicyInstancesByPolicyResponseTypeDef:
        """
        Gets information about the traffic policy instances that you created by using a
        specify traffic policy version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_traffic_policy_instances_by_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_traffic_policy_instances_by_policy)
        """
    def list_traffic_policy_versions(
        self, *, Id: str, TrafficPolicyVersionMarker: str = None, MaxItems: str = None
    ) -> ListTrafficPolicyVersionsResponseTypeDef:
        """
        Gets information about all of the versions for a specified traffic policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_traffic_policy_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_traffic_policy_versions)
        """
    def list_vpc_association_authorizations(
        self, *, HostedZoneId: str, NextToken: str = None, MaxResults: str = None
    ) -> ListVPCAssociationAuthorizationsResponseTypeDef:
        """
        Gets a list of the VPCs that were created by other accounts and that can be
        associated with a specified hosted zone because you've submitted one or more
        `CreateVPCAssociationAuthorization` requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.list_vpc_association_authorizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#list_vpc_association_authorizations)
        """
    def test_dns_answer(
        self,
        *,
        HostedZoneId: str,
        RecordName: str,
        RecordType: RRTypeType,
        ResolverIP: str = None,
        EDNS0ClientSubnetIP: str = None,
        EDNS0ClientSubnetMask: str = None
    ) -> TestDNSAnswerResponseTypeDef:
        """
        Gets the value that Amazon Route 53 returns in response to a DNS request for a
        specified record name and type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.test_dns_answer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#test_dns_answer)
        """
    def update_health_check(
        self,
        *,
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
        Regions: List[HealthCheckRegionType] = None,
        AlarmIdentifier: "AlarmIdentifierTypeDef" = None,
        InsufficientDataHealthStatus: InsufficientDataHealthStatusType = None,
        ResetElements: List[ResettableElementNameType] = None
    ) -> UpdateHealthCheckResponseTypeDef:
        """
        Updates an existing health check.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.update_health_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#update_health_check)
        """
    def update_hosted_zone_comment(
        self, *, Id: str, Comment: str = None
    ) -> UpdateHostedZoneCommentResponseTypeDef:
        """
        Updates the comment for a specified hosted zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.update_hosted_zone_comment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#update_hosted_zone_comment)
        """
    def update_traffic_policy_comment(
        self, *, Id: str, Version: int, Comment: str
    ) -> UpdateTrafficPolicyCommentResponseTypeDef:
        """
        Updates the comment for a specified traffic policy version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.update_traffic_policy_comment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#update_traffic_policy_comment)
        """
    def update_traffic_policy_instance(
        self, *, Id: str, TTL: int, TrafficPolicyId: str, TrafficPolicyVersion: int
    ) -> UpdateTrafficPolicyInstanceResponseTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Client.update_traffic_policy_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/client.html#update_traffic_policy_instance)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_cidr_blocks"]) -> ListCidrBlocksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Paginator.ListCidrBlocks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrblockspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_cidr_collections"]
    ) -> ListCidrCollectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Paginator.ListCidrCollections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrcollectionspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_cidr_locations"]
    ) -> ListCidrLocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Paginator.ListCidrLocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listcidrlocationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_health_checks"]
    ) -> ListHealthChecksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Paginator.ListHealthChecks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listhealthcheckspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_hosted_zones"]
    ) -> ListHostedZonesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Paginator.ListHostedZones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listhostedzonespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_query_logging_configs"]
    ) -> ListQueryLoggingConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listqueryloggingconfigspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_record_sets"]
    ) -> ListResourceRecordSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listresourcerecordsetspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_vpc_association_authorizations"]
    ) -> ListVPCAssociationAuthorizationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/paginators.html#listvpcassociationauthorizationspaginator)
        """
    def get_waiter(
        self, waiter_name: Literal["resource_record_sets_changed"]
    ) -> ResourceRecordSetsChangedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/route53.html#Route53.Waiter.ResourceRecordSetsChanged)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/waiters.html#resourcerecordsetschangedwaiter)
        """
