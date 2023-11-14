"""
Type annotations for lightsail service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lightsail import LightsailClient

    client: LightsailClient = boto3.client("lightsail")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    AddOnTypeType,
    AlarmStateType,
    BucketMetricNameType,
    CertificateStatusType,
    ComparisonOperatorType,
    ContactProtocolType,
    ContainerServiceMetricNameType,
    ContainerServicePowerNameType,
    DistributionMetricNameType,
    HttpEndpointType,
    HttpProtocolIpv6Type,
    HttpTokensType,
    InstanceAccessProtocolType,
    InstanceMetricNameType,
    IpAddressTypeType,
    LoadBalancerAttributeNameType,
    LoadBalancerMetricNameType,
    MetricNameType,
    MetricStatisticType,
    MetricUnitType,
    RegionNameType,
    RelationalDatabaseMetricNameType,
    RelationalDatabasePasswordVersionType,
    ResourceBucketAccessType,
    ResourceTypeType,
    TreatMissingDataType,
)
from .paginator import (
    GetActiveNamesPaginator,
    GetBlueprintsPaginator,
    GetBundlesPaginator,
    GetCloudFormationStackRecordsPaginator,
    GetDiskSnapshotsPaginator,
    GetDisksPaginator,
    GetDomainsPaginator,
    GetExportSnapshotRecordsPaginator,
    GetInstanceSnapshotsPaginator,
    GetInstancesPaginator,
    GetKeyPairsPaginator,
    GetLoadBalancersPaginator,
    GetOperationsPaginator,
    GetRelationalDatabaseBlueprintsPaginator,
    GetRelationalDatabaseBundlesPaginator,
    GetRelationalDatabaseEventsPaginator,
    GetRelationalDatabaseParametersPaginator,
    GetRelationalDatabaseSnapshotsPaginator,
    GetRelationalDatabasesPaginator,
    GetStaticIpsPaginator,
)
from .type_defs import (
    AccessRulesTypeDef,
    AddOnRequestTypeDef,
    AllocateStaticIpResultTypeDef,
    AttachCertificateToDistributionResultTypeDef,
    AttachDiskResultTypeDef,
    AttachInstancesToLoadBalancerResultTypeDef,
    AttachLoadBalancerTlsCertificateResultTypeDef,
    AttachStaticIpResultTypeDef,
    BucketAccessLogConfigTypeDef,
    CacheBehaviorPerPathTypeDef,
    CacheBehaviorTypeDef,
    CacheSettingsTypeDef,
    CloseInstancePublicPortsResultTypeDef,
    ContainerServiceDeploymentRequestTypeDef,
    ContainerServicesListResultTypeDef,
    ContainerTypeDef,
    CopySnapshotResultTypeDef,
    CreateBucketAccessKeyResultTypeDef,
    CreateBucketResultTypeDef,
    CreateCertificateResultTypeDef,
    CreateCloudFormationStackResultTypeDef,
    CreateContactMethodResultTypeDef,
    CreateContainerServiceDeploymentResultTypeDef,
    CreateContainerServiceRegistryLoginResultTypeDef,
    CreateContainerServiceResultTypeDef,
    CreateDiskFromSnapshotResultTypeDef,
    CreateDiskResultTypeDef,
    CreateDiskSnapshotResultTypeDef,
    CreateDistributionResultTypeDef,
    CreateDomainEntryResultTypeDef,
    CreateDomainResultTypeDef,
    CreateGUISessionAccessDetailsResultTypeDef,
    CreateInstancesFromSnapshotResultTypeDef,
    CreateInstanceSnapshotResultTypeDef,
    CreateInstancesResultTypeDef,
    CreateKeyPairResultTypeDef,
    CreateLoadBalancerResultTypeDef,
    CreateLoadBalancerTlsCertificateResultTypeDef,
    CreateRelationalDatabaseFromSnapshotResultTypeDef,
    CreateRelationalDatabaseResultTypeDef,
    CreateRelationalDatabaseSnapshotResultTypeDef,
    DeleteAlarmResultTypeDef,
    DeleteAutoSnapshotResultTypeDef,
    DeleteBucketAccessKeyResultTypeDef,
    DeleteBucketResultTypeDef,
    DeleteCertificateResultTypeDef,
    DeleteContactMethodResultTypeDef,
    DeleteDiskResultTypeDef,
    DeleteDiskSnapshotResultTypeDef,
    DeleteDistributionResultTypeDef,
    DeleteDomainEntryResultTypeDef,
    DeleteDomainResultTypeDef,
    DeleteInstanceResultTypeDef,
    DeleteInstanceSnapshotResultTypeDef,
    DeleteKeyPairResultTypeDef,
    DeleteKnownHostKeysResultTypeDef,
    DeleteLoadBalancerResultTypeDef,
    DeleteLoadBalancerTlsCertificateResultTypeDef,
    DeleteRelationalDatabaseResultTypeDef,
    DeleteRelationalDatabaseSnapshotResultTypeDef,
    DetachCertificateFromDistributionResultTypeDef,
    DetachDiskResultTypeDef,
    DetachInstancesFromLoadBalancerResultTypeDef,
    DetachStaticIpResultTypeDef,
    DisableAddOnResultTypeDef,
    DiskMapTypeDef,
    DomainEntryTypeDef,
    DownloadDefaultKeyPairResultTypeDef,
    EnableAddOnResultTypeDef,
    EndpointRequestTypeDef,
    ExportSnapshotResultTypeDef,
    GetActiveNamesResultTypeDef,
    GetAlarmsResultTypeDef,
    GetAutoSnapshotsResultTypeDef,
    GetBlueprintsResultTypeDef,
    GetBucketAccessKeysResultTypeDef,
    GetBucketBundlesResultTypeDef,
    GetBucketMetricDataResultTypeDef,
    GetBucketsResultTypeDef,
    GetBundlesResultTypeDef,
    GetCertificatesResultTypeDef,
    GetCloudFormationStackRecordsResultTypeDef,
    GetContactMethodsResultTypeDef,
    GetContainerAPIMetadataResultTypeDef,
    GetContainerImagesResultTypeDef,
    GetContainerLogResultTypeDef,
    GetContainerServiceDeploymentsResultTypeDef,
    GetContainerServiceMetricDataResultTypeDef,
    GetContainerServicePowersResultTypeDef,
    GetCostEstimateResultTypeDef,
    GetDiskResultTypeDef,
    GetDiskSnapshotResultTypeDef,
    GetDiskSnapshotsResultTypeDef,
    GetDisksResultTypeDef,
    GetDistributionBundlesResultTypeDef,
    GetDistributionLatestCacheResetResultTypeDef,
    GetDistributionMetricDataResultTypeDef,
    GetDistributionsResultTypeDef,
    GetDomainResultTypeDef,
    GetDomainsResultTypeDef,
    GetExportSnapshotRecordsResultTypeDef,
    GetInstanceAccessDetailsResultTypeDef,
    GetInstanceMetricDataResultTypeDef,
    GetInstancePortStatesResultTypeDef,
    GetInstanceResultTypeDef,
    GetInstanceSnapshotResultTypeDef,
    GetInstanceSnapshotsResultTypeDef,
    GetInstancesResultTypeDef,
    GetInstanceStateResultTypeDef,
    GetKeyPairResultTypeDef,
    GetKeyPairsResultTypeDef,
    GetLoadBalancerMetricDataResultTypeDef,
    GetLoadBalancerResultTypeDef,
    GetLoadBalancersResultTypeDef,
    GetLoadBalancerTlsCertificatesResultTypeDef,
    GetLoadBalancerTlsPoliciesResultTypeDef,
    GetOperationResultTypeDef,
    GetOperationsForResourceResultTypeDef,
    GetOperationsResultTypeDef,
    GetRegionsResultTypeDef,
    GetRelationalDatabaseBlueprintsResultTypeDef,
    GetRelationalDatabaseBundlesResultTypeDef,
    GetRelationalDatabaseEventsResultTypeDef,
    GetRelationalDatabaseLogEventsResultTypeDef,
    GetRelationalDatabaseLogStreamsResultTypeDef,
    GetRelationalDatabaseMasterUserPasswordResultTypeDef,
    GetRelationalDatabaseMetricDataResultTypeDef,
    GetRelationalDatabaseParametersResultTypeDef,
    GetRelationalDatabaseResultTypeDef,
    GetRelationalDatabaseSnapshotResultTypeDef,
    GetRelationalDatabaseSnapshotsResultTypeDef,
    GetRelationalDatabasesResultTypeDef,
    GetStaticIpResultTypeDef,
    GetStaticIpsResultTypeDef,
    ImportKeyPairResultTypeDef,
    InputOriginTypeDef,
    InstanceEntryTypeDef,
    IsVpcPeeredResultTypeDef,
    OpenInstancePublicPortsResultTypeDef,
    PeerVpcResultTypeDef,
    PortInfoTypeDef,
    PrivateRegistryAccessRequestTypeDef,
    PutAlarmResultTypeDef,
    PutInstancePublicPortsResultTypeDef,
    RebootInstanceResultTypeDef,
    RebootRelationalDatabaseResultTypeDef,
    RegisterContainerImageResultTypeDef,
    RelationalDatabaseParameterTypeDef,
    ReleaseStaticIpResultTypeDef,
    ResetDistributionCacheResultTypeDef,
    SendContactMethodVerificationResultTypeDef,
    SetIpAddressTypeResultTypeDef,
    SetResourceAccessForBucketResultTypeDef,
    StartGUISessionResultTypeDef,
    StartInstanceResultTypeDef,
    StartRelationalDatabaseResultTypeDef,
    StopGUISessionResultTypeDef,
    StopInstanceResultTypeDef,
    StopRelationalDatabaseResultTypeDef,
    TagResourceResultTypeDef,
    TagTypeDef,
    TestAlarmResultTypeDef,
    UnpeerVpcResultTypeDef,
    UntagResourceResultTypeDef,
    UpdateBucketBundleResultTypeDef,
    UpdateBucketResultTypeDef,
    UpdateContainerServiceResultTypeDef,
    UpdateDistributionBundleResultTypeDef,
    UpdateDistributionResultTypeDef,
    UpdateDomainEntryResultTypeDef,
    UpdateInstanceMetadataOptionsResultTypeDef,
    UpdateLoadBalancerAttributeResultTypeDef,
    UpdateRelationalDatabaseParametersResultTypeDef,
    UpdateRelationalDatabaseResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("LightsailClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AccountSetupInProgressException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    OperationFailureException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    UnauthenticatedException: Type[BotocoreClientError]

class LightsailClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        LightsailClient exceptions.
        """
    def allocate_static_ip(self, *, staticIpName: str) -> AllocateStaticIpResultTypeDef:
        """
        Allocates a static IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.allocate_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#allocate_static_ip)
        """
    def attach_certificate_to_distribution(
        self, *, distributionName: str, certificateName: str
    ) -> AttachCertificateToDistributionResultTypeDef:
        """
        Attaches an SSL/TLS certificate to your Amazon Lightsail content delivery
        network (CDN) distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.attach_certificate_to_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_certificate_to_distribution)
        """
    def attach_disk(
        self, *, diskName: str, instanceName: str, diskPath: str, autoMounting: bool = None
    ) -> AttachDiskResultTypeDef:
        """
        Attaches a block storage disk to a running or stopped Lightsail instance and
        exposes it to the instance with the specified disk name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.attach_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_disk)
        """
    def attach_instances_to_load_balancer(
        self, *, loadBalancerName: str, instanceNames: List[str]
    ) -> AttachInstancesToLoadBalancerResultTypeDef:
        """
        Attaches one or more Lightsail instances to a load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.attach_instances_to_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_instances_to_load_balancer)
        """
    def attach_load_balancer_tls_certificate(
        self, *, loadBalancerName: str, certificateName: str
    ) -> AttachLoadBalancerTlsCertificateResultTypeDef:
        """
        Attaches a Transport Layer Security (TLS) certificate to your load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.attach_load_balancer_tls_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_load_balancer_tls_certificate)
        """
    def attach_static_ip(
        self, *, staticIpName: str, instanceName: str
    ) -> AttachStaticIpResultTypeDef:
        """
        Attaches a static IP address to a specific Amazon Lightsail instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.attach_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#attach_static_ip)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#close)
        """
    def close_instance_public_ports(
        self, *, portInfo: "PortInfoTypeDef", instanceName: str
    ) -> CloseInstancePublicPortsResultTypeDef:
        """
        Closes ports for a specific Amazon Lightsail instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.close_instance_public_ports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#close_instance_public_ports)
        """
    def copy_snapshot(
        self,
        *,
        targetSnapshotName: str,
        sourceRegion: RegionNameType,
        sourceSnapshotName: str = None,
        sourceResourceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None
    ) -> CopySnapshotResultTypeDef:
        """
        Copies a manual snapshot of an instance or disk as another manual snapshot, or
        copies an automatic snapshot of an instance or disk as a manual snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.copy_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#copy_snapshot)
        """
    def create_bucket(
        self,
        *,
        bucketName: str,
        bundleId: str,
        tags: List["TagTypeDef"] = None,
        enableObjectVersioning: bool = None
    ) -> CreateBucketResultTypeDef:
        """
        Creates an Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_bucket)
        """
    def create_bucket_access_key(self, *, bucketName: str) -> CreateBucketAccessKeyResultTypeDef:
        """
        Creates a new access key for the specified Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_bucket_access_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_bucket_access_key)
        """
    def create_certificate(
        self,
        *,
        certificateName: str,
        domainName: str,
        subjectAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateCertificateResultTypeDef:
        """
        Creates an SSL/TLS certificate for an Amazon Lightsail content delivery network
        (CDN) distribution and a container service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_certificate)
        """
    def create_cloud_formation_stack(
        self, *, instances: List["InstanceEntryTypeDef"]
    ) -> CreateCloudFormationStackResultTypeDef:
        """
        Creates an AWS CloudFormation stack, which creates a new Amazon EC2 instance
        from an exported Amazon Lightsail snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_cloud_formation_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_cloud_formation_stack)
        """
    def create_contact_method(
        self, *, protocol: ContactProtocolType, contactEndpoint: str
    ) -> CreateContactMethodResultTypeDef:
        """
        Creates an email or SMS text message contact method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_contact_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_contact_method)
        """
    def create_container_service(
        self,
        *,
        serviceName: str,
        power: ContainerServicePowerNameType,
        scale: int,
        tags: List["TagTypeDef"] = None,
        publicDomainNames: Dict[str, List[str]] = None,
        deployment: "ContainerServiceDeploymentRequestTypeDef" = None,
        privateRegistryAccess: "PrivateRegistryAccessRequestTypeDef" = None
    ) -> CreateContainerServiceResultTypeDef:
        """
        Creates an Amazon Lightsail container service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_container_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_container_service)
        """
    def create_container_service_deployment(
        self,
        *,
        serviceName: str,
        containers: Dict[str, "ContainerTypeDef"] = None,
        publicEndpoint: "EndpointRequestTypeDef" = None
    ) -> CreateContainerServiceDeploymentResultTypeDef:
        """
        Creates a deployment for your Amazon Lightsail container service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_container_service_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_container_service_deployment)
        """
    def create_container_service_registry_login(
        self,
    ) -> CreateContainerServiceRegistryLoginResultTypeDef:
        """
        Creates a temporary set of log in credentials that you can use to log in to the
        Docker process on your local machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_container_service_registry_login)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_container_service_registry_login)
        """
    def create_disk(
        self,
        *,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        tags: List["TagTypeDef"] = None,
        addOns: List["AddOnRequestTypeDef"] = None
    ) -> CreateDiskResultTypeDef:
        """
        Creates a block storage disk that can be attached to an Amazon Lightsail
        instance in the same Availability Zone (e.g., `us-east-2a`).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_disk)
        """
    def create_disk_from_snapshot(
        self,
        *,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        diskSnapshotName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List["AddOnRequestTypeDef"] = None,
        sourceDiskName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None
    ) -> CreateDiskFromSnapshotResultTypeDef:
        """
        Creates a block storage disk from a manual or automatic snapshot of a disk.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_disk_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_disk_from_snapshot)
        """
    def create_disk_snapshot(
        self,
        *,
        diskSnapshotName: str,
        diskName: str = None,
        instanceName: str = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDiskSnapshotResultTypeDef:
        """
        Creates a snapshot of a block storage disk.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_disk_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_disk_snapshot)
        """
    def create_distribution(
        self,
        *,
        distributionName: str,
        origin: "InputOriginTypeDef",
        defaultCacheBehavior: "CacheBehaviorTypeDef",
        bundleId: str,
        cacheBehaviorSettings: "CacheSettingsTypeDef" = None,
        cacheBehaviors: List["CacheBehaviorPerPathTypeDef"] = None,
        ipAddressType: IpAddressTypeType = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateDistributionResultTypeDef:
        """
        Creates an Amazon Lightsail content delivery network (CDN) distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_distribution)
        """
    def create_domain(
        self, *, domainName: str, tags: List["TagTypeDef"] = None
    ) -> CreateDomainResultTypeDef:
        """
        Creates a domain resource for the specified domain (e.g., example.com).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_domain)
        """
    def create_domain_entry(
        self, *, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> CreateDomainEntryResultTypeDef:
        """
        Creates one of the following domain name system (DNS) records in a domain DNS
        zone: Address (A), canonical name (CNAME), mail exchanger (MX), name server
        (NS), start of authority (SOA), service locator (SRV), or text (TXT).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_domain_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_domain_entry)
        """
    def create_gui_session_access_details(
        self, *, resourceName: str
    ) -> CreateGUISessionAccessDetailsResultTypeDef:
        """
        Creates two URLs that are used to access a virtual computer’s graphical user
        interface (GUI) session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_gui_session_access_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_gui_session_access_details)
        """
    def create_instance_snapshot(
        self, *, instanceSnapshotName: str, instanceName: str, tags: List["TagTypeDef"] = None
    ) -> CreateInstanceSnapshotResultTypeDef:
        """
        Creates a snapshot of a specific virtual private server, or *instance*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_instance_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_instance_snapshot)
        """
    def create_instances(
        self,
        *,
        instanceNames: List[str],
        availabilityZone: str,
        blueprintId: str,
        bundleId: str,
        customImageName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List["AddOnRequestTypeDef"] = None,
        ipAddressType: IpAddressTypeType = None
    ) -> CreateInstancesResultTypeDef:
        """
        Creates one or more Amazon Lightsail instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_instances)
        """
    def create_instances_from_snapshot(
        self,
        *,
        instanceNames: List[str],
        availabilityZone: str,
        bundleId: str,
        attachedDiskMapping: Dict[str, List["DiskMapTypeDef"]] = None,
        instanceSnapshotName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List["AddOnRequestTypeDef"] = None,
        ipAddressType: IpAddressTypeType = None,
        sourceInstanceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None
    ) -> CreateInstancesFromSnapshotResultTypeDef:
        """
        Creates one or more new instances from a manual or automatic snapshot of an
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_instances_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_instances_from_snapshot)
        """
    def create_key_pair(
        self, *, keyPairName: str, tags: List["TagTypeDef"] = None
    ) -> CreateKeyPairResultTypeDef:
        """
        Creates a custom SSH key pair that you can use with an Amazon Lightsail
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_key_pair)
        """
    def create_load_balancer(
        self,
        *,
        loadBalancerName: str,
        instancePort: int,
        healthCheckPath: str = None,
        certificateName: str = None,
        certificateDomainName: str = None,
        certificateAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None,
        ipAddressType: IpAddressTypeType = None,
        tlsPolicyName: str = None
    ) -> CreateLoadBalancerResultTypeDef:
        """
        Creates a Lightsail load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_load_balancer)
        """
    def create_load_balancer_tls_certificate(
        self,
        *,
        loadBalancerName: str,
        certificateName: str,
        certificateDomainName: str,
        certificateAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateLoadBalancerTlsCertificateResultTypeDef:
        """
        Creates an SSL/TLS certificate for an Amazon Lightsail load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_load_balancer_tls_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_load_balancer_tls_certificate)
        """
    def create_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        relationalDatabaseBlueprintId: str,
        relationalDatabaseBundleId: str,
        masterDatabaseName: str,
        masterUsername: str,
        availabilityZone: str = None,
        masterUserPassword: str = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        publiclyAccessible: bool = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRelationalDatabaseResultTypeDef:
        """
        Creates a new database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_relational_database)
        """
    def create_relational_database_from_snapshot(
        self,
        *,
        relationalDatabaseName: str,
        availabilityZone: str = None,
        publiclyAccessible: bool = None,
        relationalDatabaseSnapshotName: str = None,
        relationalDatabaseBundleId: str = None,
        sourceRelationalDatabaseName: str = None,
        restoreTime: Union[datetime, str] = None,
        useLatestRestorableTime: bool = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateRelationalDatabaseFromSnapshotResultTypeDef:
        """
        Creates a new database from an existing database snapshot in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_relational_database_from_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_relational_database_from_snapshot)
        """
    def create_relational_database_snapshot(
        self,
        *,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str,
        tags: List["TagTypeDef"] = None
    ) -> CreateRelationalDatabaseSnapshotResultTypeDef:
        """
        Creates a snapshot of your database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.create_relational_database_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#create_relational_database_snapshot)
        """
    def delete_alarm(self, *, alarmName: str) -> DeleteAlarmResultTypeDef:
        """
        Deletes an alarm.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_alarm)
        """
    def delete_auto_snapshot(
        self, *, resourceName: str, date: str
    ) -> DeleteAutoSnapshotResultTypeDef:
        """
        Deletes an automatic snapshot of an instance or disk.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_auto_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_auto_snapshot)
        """
    def delete_bucket(
        self, *, bucketName: str, forceDelete: bool = None
    ) -> DeleteBucketResultTypeDef:
        """
        Deletes a Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_bucket)
        """
    def delete_bucket_access_key(
        self, *, bucketName: str, accessKeyId: str
    ) -> DeleteBucketAccessKeyResultTypeDef:
        """
        Deletes an access key for the specified Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_bucket_access_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_bucket_access_key)
        """
    def delete_certificate(self, *, certificateName: str) -> DeleteCertificateResultTypeDef:
        """
        Deletes an SSL/TLS certificate for your Amazon Lightsail content delivery
        network (CDN) distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_certificate)
        """
    def delete_contact_method(
        self, *, protocol: ContactProtocolType
    ) -> DeleteContactMethodResultTypeDef:
        """
        Deletes a contact method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_contact_method)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_contact_method)
        """
    def delete_container_image(self, *, serviceName: str, image: str) -> Dict[str, Any]:
        """
        Deletes a container image that is registered to your Amazon Lightsail container
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_container_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_container_image)
        """
    def delete_container_service(self, *, serviceName: str) -> Dict[str, Any]:
        """
        Deletes your Amazon Lightsail container service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_container_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_container_service)
        """
    def delete_disk(
        self, *, diskName: str, forceDeleteAddOns: bool = None
    ) -> DeleteDiskResultTypeDef:
        """
        Deletes the specified block storage disk.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_disk)
        """
    def delete_disk_snapshot(self, *, diskSnapshotName: str) -> DeleteDiskSnapshotResultTypeDef:
        """
        Deletes the specified disk snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_disk_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_disk_snapshot)
        """
    def delete_distribution(
        self, *, distributionName: str = None
    ) -> DeleteDistributionResultTypeDef:
        """
        Deletes your Amazon Lightsail content delivery network (CDN) distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_distribution)
        """
    def delete_domain(self, *, domainName: str) -> DeleteDomainResultTypeDef:
        """
        Deletes the specified domain recordset and all of its domain records.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_domain)
        """
    def delete_domain_entry(
        self, *, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> DeleteDomainEntryResultTypeDef:
        """
        Deletes a specific domain entry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_domain_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_domain_entry)
        """
    def delete_instance(
        self, *, instanceName: str, forceDeleteAddOns: bool = None
    ) -> DeleteInstanceResultTypeDef:
        """
        Deletes an Amazon Lightsail instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_instance)
        """
    def delete_instance_snapshot(
        self, *, instanceSnapshotName: str
    ) -> DeleteInstanceSnapshotResultTypeDef:
        """
        Deletes a specific snapshot of a virtual private server (or *instance*).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_instance_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_instance_snapshot)
        """
    def delete_key_pair(
        self, *, keyPairName: str, expectedFingerprint: str = None
    ) -> DeleteKeyPairResultTypeDef:
        """
        Deletes the specified key pair by removing the public key from Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_key_pair)
        """
    def delete_known_host_keys(self, *, instanceName: str) -> DeleteKnownHostKeysResultTypeDef:
        """
        Deletes the known host key or certificate used by the Amazon Lightsail browser-
        based SSH or RDP clients to authenticate an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_known_host_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_known_host_keys)
        """
    def delete_load_balancer(self, *, loadBalancerName: str) -> DeleteLoadBalancerResultTypeDef:
        """
        Deletes a Lightsail load balancer and all its associated SSL/TLS certificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_load_balancer)
        """
    def delete_load_balancer_tls_certificate(
        self, *, loadBalancerName: str, certificateName: str, force: bool = None
    ) -> DeleteLoadBalancerTlsCertificateResultTypeDef:
        """
        Deletes an SSL/TLS certificate associated with a Lightsail load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer_tls_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_load_balancer_tls_certificate)
        """
    def delete_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        skipFinalSnapshot: bool = None,
        finalRelationalDatabaseSnapshotName: str = None
    ) -> DeleteRelationalDatabaseResultTypeDef:
        """
        Deletes a database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_relational_database)
        """
    def delete_relational_database_snapshot(
        self, *, relationalDatabaseSnapshotName: str
    ) -> DeleteRelationalDatabaseSnapshotResultTypeDef:
        """
        Deletes a database snapshot in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.delete_relational_database_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#delete_relational_database_snapshot)
        """
    def detach_certificate_from_distribution(
        self, *, distributionName: str
    ) -> DetachCertificateFromDistributionResultTypeDef:
        """
        Detaches an SSL/TLS certificate from your Amazon Lightsail content delivery
        network (CDN) distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.detach_certificate_from_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#detach_certificate_from_distribution)
        """
    def detach_disk(self, *, diskName: str) -> DetachDiskResultTypeDef:
        """
        Detaches a stopped block storage disk from a Lightsail instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.detach_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#detach_disk)
        """
    def detach_instances_from_load_balancer(
        self, *, loadBalancerName: str, instanceNames: List[str]
    ) -> DetachInstancesFromLoadBalancerResultTypeDef:
        """
        Detaches the specified instances from a Lightsail load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.detach_instances_from_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#detach_instances_from_load_balancer)
        """
    def detach_static_ip(self, *, staticIpName: str) -> DetachStaticIpResultTypeDef:
        """
        Detaches a static IP from the Amazon Lightsail instance to which it is attached.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.detach_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#detach_static_ip)
        """
    def disable_add_on(
        self, *, addOnType: AddOnTypeType, resourceName: str
    ) -> DisableAddOnResultTypeDef:
        """
        Disables an add-on for an Amazon Lightsail resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.disable_add_on)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#disable_add_on)
        """
    def download_default_key_pair(self) -> DownloadDefaultKeyPairResultTypeDef:
        """
        Downloads the regional Amazon Lightsail default key pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.download_default_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#download_default_key_pair)
        """
    def enable_add_on(
        self, *, resourceName: str, addOnRequest: "AddOnRequestTypeDef"
    ) -> EnableAddOnResultTypeDef:
        """
        Enables or modifies an add-on for an Amazon Lightsail resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.enable_add_on)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#enable_add_on)
        """
    def export_snapshot(self, *, sourceSnapshotName: str) -> ExportSnapshotResultTypeDef:
        """
        Exports an Amazon Lightsail instance or block storage disk snapshot to Amazon
        Elastic Compute Cloud (Amazon EC2).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.export_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#export_snapshot)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#generate_presigned_url)
        """
    def get_active_names(self, *, pageToken: str = None) -> GetActiveNamesResultTypeDef:
        """
        Returns the names of all active (not deleted) resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_active_names)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_active_names)
        """
    def get_alarms(
        self, *, alarmName: str = None, pageToken: str = None, monitoredResourceName: str = None
    ) -> GetAlarmsResultTypeDef:
        """
        Returns information about the configured alarms.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_alarms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_alarms)
        """
    def get_auto_snapshots(self, *, resourceName: str) -> GetAutoSnapshotsResultTypeDef:
        """
        Returns the available automatic snapshots for an instance or disk.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_auto_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_auto_snapshots)
        """
    def get_blueprints(
        self,
        *,
        includeInactive: bool = None,
        pageToken: str = None,
        appCategory: Literal["LfR"] = None
    ) -> GetBlueprintsResultTypeDef:
        """
        Returns the list of available instance images, or *blueprints*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_blueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_blueprints)
        """
    def get_bucket_access_keys(self, *, bucketName: str) -> GetBucketAccessKeysResultTypeDef:
        """
        Returns the existing access key IDs for the specified Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_bucket_access_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_bucket_access_keys)
        """
    def get_bucket_bundles(self, *, includeInactive: bool = None) -> GetBucketBundlesResultTypeDef:
        """
        Returns the bundles that you can apply to a Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_bucket_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_bucket_bundles)
        """
    def get_bucket_metric_data(
        self,
        *,
        bucketName: str,
        metricName: BucketMetricNameType,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        period: int,
        statistics: List[MetricStatisticType],
        unit: MetricUnitType
    ) -> GetBucketMetricDataResultTypeDef:
        """
        Returns the data points of a specific metric for an Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_bucket_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_bucket_metric_data)
        """
    def get_buckets(
        self,
        *,
        bucketName: str = None,
        pageToken: str = None,
        includeConnectedResources: bool = None
    ) -> GetBucketsResultTypeDef:
        """
        Returns information about one or more Amazon Lightsail buckets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_buckets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_buckets)
        """
    def get_bundles(
        self,
        *,
        includeInactive: bool = None,
        pageToken: str = None,
        appCategory: Literal["LfR"] = None
    ) -> GetBundlesResultTypeDef:
        """
        Returns the bundles that you can apply to an Amazon Lightsail instance when you
        create it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_bundles)
        """
    def get_certificates(
        self,
        *,
        certificateStatuses: List[CertificateStatusType] = None,
        includeCertificateDetails: bool = None,
        certificateName: str = None,
        pageToken: str = None
    ) -> GetCertificatesResultTypeDef:
        """
        Returns information about one or more Amazon Lightsail SSL/TLS certificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_certificates)
        """
    def get_cloud_formation_stack_records(
        self, *, pageToken: str = None
    ) -> GetCloudFormationStackRecordsResultTypeDef:
        """
        Returns the CloudFormation stack record created as a result of the `create cloud
        formation stack` operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_cloud_formation_stack_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_cloud_formation_stack_records)
        """
    def get_contact_methods(
        self, *, protocols: List[ContactProtocolType] = None
    ) -> GetContactMethodsResultTypeDef:
        """
        Returns information about the configured contact methods.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_contact_methods)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_contact_methods)
        """
    def get_container_api_metadata(self) -> GetContainerAPIMetadataResultTypeDef:
        """
        Returns information about Amazon Lightsail containers, such as the current
        version of the Lightsail Control (lightsailctl) plugin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_container_api_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_api_metadata)
        """
    def get_container_images(self, *, serviceName: str) -> GetContainerImagesResultTypeDef:
        """
        Returns the container images that are registered to your Amazon Lightsail
        container service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_container_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_images)
        """
    def get_container_log(
        self,
        *,
        serviceName: str,
        containerName: str,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        filterPattern: str = None,
        pageToken: str = None
    ) -> GetContainerLogResultTypeDef:
        """
        Returns the log events of a container of your Amazon Lightsail container
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_container_log)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_log)
        """
    def get_container_service_deployments(
        self, *, serviceName: str
    ) -> GetContainerServiceDeploymentsResultTypeDef:
        """
        Returns the deployments for your Amazon Lightsail container service A deployment
        specifies the settings, such as the ports and launch command, of containers that
        are deployed to your container service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_container_service_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_service_deployments)
        """
    def get_container_service_metric_data(
        self,
        *,
        serviceName: str,
        metricName: ContainerServiceMetricNameType,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        period: int,
        statistics: List[MetricStatisticType]
    ) -> GetContainerServiceMetricDataResultTypeDef:
        """
        Returns the data points of a specific metric of your Amazon Lightsail container
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_container_service_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_service_metric_data)
        """
    def get_container_service_powers(self) -> GetContainerServicePowersResultTypeDef:
        """
        Returns the list of powers that can be specified for your Amazon Lightsail
        container services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_container_service_powers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_service_powers)
        """
    def get_container_services(
        self, *, serviceName: str = None
    ) -> ContainerServicesListResultTypeDef:
        """
        Returns information about one or more of your Amazon Lightsail container
        services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_container_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_container_services)
        """
    def get_cost_estimate(
        self, *, resourceName: str, startTime: Union[datetime, str], endTime: Union[datetime, str]
    ) -> GetCostEstimateResultTypeDef:
        """
        Retrieves information about the cost estimate for a specified resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_cost_estimate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_cost_estimate)
        """
    def get_disk(self, *, diskName: str) -> GetDiskResultTypeDef:
        """
        Returns information about a specific block storage disk.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_disk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_disk)
        """
    def get_disk_snapshot(self, *, diskSnapshotName: str) -> GetDiskSnapshotResultTypeDef:
        """
        Returns information about a specific block storage disk snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_disk_snapshot)
        """
    def get_disk_snapshots(self, *, pageToken: str = None) -> GetDiskSnapshotsResultTypeDef:
        """
        Returns information about all block storage disk snapshots in your AWS account
        and region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_disk_snapshots)
        """
    def get_disks(self, *, pageToken: str = None) -> GetDisksResultTypeDef:
        """
        Returns information about all block storage disks in your AWS account and
        region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_disks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_disks)
        """
    def get_distribution_bundles(self) -> GetDistributionBundlesResultTypeDef:
        """
        Returns the bundles that can be applied to your Amazon Lightsail content
        delivery network (CDN) distributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_distribution_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_distribution_bundles)
        """
    def get_distribution_latest_cache_reset(
        self, *, distributionName: str = None
    ) -> GetDistributionLatestCacheResetResultTypeDef:
        """
        Returns the timestamp and status of the last cache reset of a specific Amazon
        Lightsail content delivery network (CDN) distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_distribution_latest_cache_reset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_distribution_latest_cache_reset)
        """
    def get_distribution_metric_data(
        self,
        *,
        distributionName: str,
        metricName: DistributionMetricNameType,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        period: int,
        unit: MetricUnitType,
        statistics: List[MetricStatisticType]
    ) -> GetDistributionMetricDataResultTypeDef:
        """
        Returns the data points of a specific metric for an Amazon Lightsail content
        delivery network (CDN) distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_distribution_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_distribution_metric_data)
        """
    def get_distributions(
        self, *, distributionName: str = None, pageToken: str = None
    ) -> GetDistributionsResultTypeDef:
        """
        Returns information about one or more of your Amazon Lightsail content delivery
        network (CDN) distributions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_distributions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_distributions)
        """
    def get_domain(self, *, domainName: str) -> GetDomainResultTypeDef:
        """
        Returns information about a specific domain recordset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_domain)
        """
    def get_domains(self, *, pageToken: str = None) -> GetDomainsResultTypeDef:
        """
        Returns a list of all domains in the user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_domains)
        """
    def get_export_snapshot_records(
        self, *, pageToken: str = None
    ) -> GetExportSnapshotRecordsResultTypeDef:
        """
        Returns all export snapshot records created as a result of the `export snapshot`
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_export_snapshot_records)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_export_snapshot_records)
        """
    def get_instance(self, *, instanceName: str) -> GetInstanceResultTypeDef:
        """
        Returns information about a specific Amazon Lightsail instance, which is a
        virtual private server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance)
        """
    def get_instance_access_details(
        self, *, instanceName: str, protocol: InstanceAccessProtocolType = None
    ) -> GetInstanceAccessDetailsResultTypeDef:
        """
        Returns temporary SSH keys you can use to connect to a specific virtual private
        server, or *instance*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_instance_access_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_access_details)
        """
    def get_instance_metric_data(
        self,
        *,
        instanceName: str,
        metricName: InstanceMetricNameType,
        period: int,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        unit: MetricUnitType,
        statistics: List[MetricStatisticType]
    ) -> GetInstanceMetricDataResultTypeDef:
        """
        Returns the data points for the specified Amazon Lightsail instance metric,
        given an instance name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_instance_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_metric_data)
        """
    def get_instance_port_states(self, *, instanceName: str) -> GetInstancePortStatesResultTypeDef:
        """
        Returns the firewall port states for a specific Amazon Lightsail instance, the
        IP addresses allowed to connect to the instance through the ports, and the
        protocol.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_instance_port_states)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_port_states)
        """
    def get_instance_snapshot(
        self, *, instanceSnapshotName: str
    ) -> GetInstanceSnapshotResultTypeDef:
        """
        Returns information about a specific instance snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_snapshot)
        """
    def get_instance_snapshots(self, *, pageToken: str = None) -> GetInstanceSnapshotsResultTypeDef:
        """
        Returns all instance snapshots for the user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_snapshots)
        """
    def get_instance_state(self, *, instanceName: str) -> GetInstanceStateResultTypeDef:
        """
        Returns the state of a specific instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_instance_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instance_state)
        """
    def get_instances(self, *, pageToken: str = None) -> GetInstancesResultTypeDef:
        """
        Returns information about all Amazon Lightsail virtual private servers, or
        *instances*.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_instances)
        """
    def get_key_pair(self, *, keyPairName: str) -> GetKeyPairResultTypeDef:
        """
        Returns information about a specific key pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_key_pair)
        """
    def get_key_pairs(
        self, *, pageToken: str = None, includeDefaultKeyPair: bool = None
    ) -> GetKeyPairsResultTypeDef:
        """
        Returns information about all key pairs in the user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_key_pairs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_key_pairs)
        """
    def get_load_balancer(self, *, loadBalancerName: str) -> GetLoadBalancerResultTypeDef:
        """
        Returns information about the specified Lightsail load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancer)
        """
    def get_load_balancer_metric_data(
        self,
        *,
        loadBalancerName: str,
        metricName: LoadBalancerMetricNameType,
        period: int,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        unit: MetricUnitType,
        statistics: List[MetricStatisticType]
    ) -> GetLoadBalancerMetricDataResultTypeDef:
        """
        Returns information about health metrics for your Lightsail load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancer_metric_data)
        """
    def get_load_balancer_tls_certificates(
        self, *, loadBalancerName: str
    ) -> GetLoadBalancerTlsCertificatesResultTypeDef:
        """
        Returns information about the TLS certificates that are associated with the
        specified Lightsail load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_tls_certificates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancer_tls_certificates)
        """
    def get_load_balancer_tls_policies(
        self, *, pageToken: str = None
    ) -> GetLoadBalancerTlsPoliciesResultTypeDef:
        """
        Returns a list of TLS security policies that you can apply to Lightsail load
        balancers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_tls_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancer_tls_policies)
        """
    def get_load_balancers(self, *, pageToken: str = None) -> GetLoadBalancersResultTypeDef:
        """
        Returns information about all load balancers in an account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_load_balancers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_load_balancers)
        """
    def get_operation(self, *, operationId: str) -> GetOperationResultTypeDef:
        """
        Returns information about a specific operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_operation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_operation)
        """
    def get_operations(self, *, pageToken: str = None) -> GetOperationsResultTypeDef:
        """
        Returns information about all operations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_operations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_operations)
        """
    def get_operations_for_resource(
        self, *, resourceName: str, pageToken: str = None
    ) -> GetOperationsForResourceResultTypeDef:
        """
        Gets operations for a specific resource (e.g., an instance or a static IP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_operations_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_operations_for_resource)
        """
    def get_regions(
        self,
        *,
        includeAvailabilityZones: bool = None,
        includeRelationalDatabaseAvailabilityZones: bool = None
    ) -> GetRegionsResultTypeDef:
        """
        Returns a list of all valid regions for Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_regions)
        """
    def get_relational_database(
        self, *, relationalDatabaseName: str
    ) -> GetRelationalDatabaseResultTypeDef:
        """
        Returns information about a specific database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database)
        """
    def get_relational_database_blueprints(
        self, *, pageToken: str = None
    ) -> GetRelationalDatabaseBlueprintsResultTypeDef:
        """
        Returns a list of available database blueprints in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_blueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_blueprints)
        """
    def get_relational_database_bundles(
        self, *, pageToken: str = None, includeInactive: bool = None
    ) -> GetRelationalDatabaseBundlesResultTypeDef:
        """
        Returns the list of bundles that are available in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_bundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_bundles)
        """
    def get_relational_database_events(
        self, *, relationalDatabaseName: str, durationInMinutes: int = None, pageToken: str = None
    ) -> GetRelationalDatabaseEventsResultTypeDef:
        """
        Returns a list of events for a specific database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_events)
        """
    def get_relational_database_log_events(
        self,
        *,
        relationalDatabaseName: str,
        logStreamName: str,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        startFromHead: bool = None,
        pageToken: str = None
    ) -> GetRelationalDatabaseLogEventsResultTypeDef:
        """
        Returns a list of log events for a database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_log_events)
        """
    def get_relational_database_log_streams(
        self, *, relationalDatabaseName: str
    ) -> GetRelationalDatabaseLogStreamsResultTypeDef:
        """
        Returns a list of available log streams for a specific database in Amazon
        Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_log_streams)
        """
    def get_relational_database_master_user_password(
        self,
        *,
        relationalDatabaseName: str,
        passwordVersion: RelationalDatabasePasswordVersionType = None
    ) -> GetRelationalDatabaseMasterUserPasswordResultTypeDef:
        """
        Returns the current, previous, or pending versions of the master user password
        for a Lightsail database.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_master_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_master_user_password)
        """
    def get_relational_database_metric_data(
        self,
        *,
        relationalDatabaseName: str,
        metricName: RelationalDatabaseMetricNameType,
        period: int,
        startTime: Union[datetime, str],
        endTime: Union[datetime, str],
        unit: MetricUnitType,
        statistics: List[MetricStatisticType]
    ) -> GetRelationalDatabaseMetricDataResultTypeDef:
        """
        Returns the data points of the specified metric for a database in Amazon
        Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_metric_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_metric_data)
        """
    def get_relational_database_parameters(
        self, *, relationalDatabaseName: str, pageToken: str = None
    ) -> GetRelationalDatabaseParametersResultTypeDef:
        """
        Returns all of the runtime parameters offered by the underlying database
        software, or engine, for a specific database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_parameters)
        """
    def get_relational_database_snapshot(
        self, *, relationalDatabaseSnapshotName: str
    ) -> GetRelationalDatabaseSnapshotResultTypeDef:
        """
        Returns information about a specific database snapshot in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_snapshot)
        """
    def get_relational_database_snapshots(
        self, *, pageToken: str = None
    ) -> GetRelationalDatabaseSnapshotsResultTypeDef:
        """
        Returns information about all of your database snapshots in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_database_snapshots)
        """
    def get_relational_databases(
        self, *, pageToken: str = None
    ) -> GetRelationalDatabasesResultTypeDef:
        """
        Returns information about all of your databases in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_relational_databases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_relational_databases)
        """
    def get_static_ip(self, *, staticIpName: str) -> GetStaticIpResultTypeDef:
        """
        Returns information about an Amazon Lightsail static IP.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_static_ip)
        """
    def get_static_ips(self, *, pageToken: str = None) -> GetStaticIpsResultTypeDef:
        """
        Returns information about all static IPs in the user's account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.get_static_ips)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#get_static_ips)
        """
    def import_key_pair(
        self, *, keyPairName: str, publicKeyBase64: str
    ) -> ImportKeyPairResultTypeDef:
        """
        Imports a public SSH key from a specific key pair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.import_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#import_key_pair)
        """
    def is_vpc_peered(self) -> IsVpcPeeredResultTypeDef:
        """
        Returns a Boolean value indicating whether your Lightsail VPC is peered.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.is_vpc_peered)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#is_vpc_peered)
        """
    def open_instance_public_ports(
        self, *, portInfo: "PortInfoTypeDef", instanceName: str
    ) -> OpenInstancePublicPortsResultTypeDef:
        """
        Opens ports for a specific Amazon Lightsail instance, and specifies the IP
        addresses allowed to connect to the instance through the ports, and the
        protocol.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.open_instance_public_ports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#open_instance_public_ports)
        """
    def peer_vpc(self) -> PeerVpcResultTypeDef:
        """
        Peers the Lightsail VPC with the user's default VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.peer_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#peer_vpc)
        """
    def put_alarm(
        self,
        *,
        alarmName: str,
        metricName: MetricNameType,
        monitoredResourceName: str,
        comparisonOperator: ComparisonOperatorType,
        threshold: float,
        evaluationPeriods: int,
        datapointsToAlarm: int = None,
        treatMissingData: TreatMissingDataType = None,
        contactProtocols: List[ContactProtocolType] = None,
        notificationTriggers: List[AlarmStateType] = None,
        notificationEnabled: bool = None
    ) -> PutAlarmResultTypeDef:
        """
        Creates or updates an alarm, and associates it with the specified metric.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.put_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#put_alarm)
        """
    def put_instance_public_ports(
        self, *, portInfos: List["PortInfoTypeDef"], instanceName: str
    ) -> PutInstancePublicPortsResultTypeDef:
        """
        Opens ports for a specific Amazon Lightsail instance, and specifies the IP
        addresses allowed to connect to the instance through the ports, and the
        protocol.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.put_instance_public_ports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#put_instance_public_ports)
        """
    def reboot_instance(self, *, instanceName: str) -> RebootInstanceResultTypeDef:
        """
        Restarts a specific instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.reboot_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#reboot_instance)
        """
    def reboot_relational_database(
        self, *, relationalDatabaseName: str
    ) -> RebootRelationalDatabaseResultTypeDef:
        """
        Restarts a specific database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.reboot_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#reboot_relational_database)
        """
    def register_container_image(
        self, *, serviceName: str, label: str, digest: str
    ) -> RegisterContainerImageResultTypeDef:
        """
        Registers a container image to your Amazon Lightsail container service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.register_container_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#register_container_image)
        """
    def release_static_ip(self, *, staticIpName: str) -> ReleaseStaticIpResultTypeDef:
        """
        Deletes a specific static IP from your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.release_static_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#release_static_ip)
        """
    def reset_distribution_cache(
        self, *, distributionName: str = None
    ) -> ResetDistributionCacheResultTypeDef:
        """
        Deletes currently cached content from your Amazon Lightsail content delivery
        network (CDN) distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.reset_distribution_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#reset_distribution_cache)
        """
    def send_contact_method_verification(
        self, *, protocol: Literal["Email"]
    ) -> SendContactMethodVerificationResultTypeDef:
        """
        Sends a verification request to an email contact method to ensure it's owned by
        the requester.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.send_contact_method_verification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#send_contact_method_verification)
        """
    def set_ip_address_type(
        self, *, resourceType: ResourceTypeType, resourceName: str, ipAddressType: IpAddressTypeType
    ) -> SetIpAddressTypeResultTypeDef:
        """
        Sets the IP address type for an Amazon Lightsail resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.set_ip_address_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#set_ip_address_type)
        """
    def set_resource_access_for_bucket(
        self, *, resourceName: str, bucketName: str, access: ResourceBucketAccessType
    ) -> SetResourceAccessForBucketResultTypeDef:
        """
        Sets the Amazon Lightsail resources that can access the specified Lightsail
        bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.set_resource_access_for_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#set_resource_access_for_bucket)
        """
    def start_gui_session(self, *, resourceName: str) -> StartGUISessionResultTypeDef:
        """
        Initiates a graphical user interface (GUI) session that’s used to access a
        virtual computer’s operating system and application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.start_gui_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#start_gui_session)
        """
    def start_instance(self, *, instanceName: str) -> StartInstanceResultTypeDef:
        """
        Starts a specific Amazon Lightsail instance from a stopped state.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.start_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#start_instance)
        """
    def start_relational_database(
        self, *, relationalDatabaseName: str
    ) -> StartRelationalDatabaseResultTypeDef:
        """
        Starts a specific database from a stopped state in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.start_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#start_relational_database)
        """
    def stop_gui_session(self, *, resourceName: str) -> StopGUISessionResultTypeDef:
        """
        Terminates a web-based NICE DCV session that’s used to access a virtual
        computer’s operating system or application.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.stop_gui_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#stop_gui_session)
        """
    def stop_instance(self, *, instanceName: str, force: bool = None) -> StopInstanceResultTypeDef:
        """
        Stops a specific Amazon Lightsail instance that is currently running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.stop_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#stop_instance)
        """
    def stop_relational_database(
        self, *, relationalDatabaseName: str, relationalDatabaseSnapshotName: str = None
    ) -> StopRelationalDatabaseResultTypeDef:
        """
        Stops a specific database that is currently running in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.stop_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#stop_relational_database)
        """
    def tag_resource(
        self, *, resourceName: str, tags: List["TagTypeDef"], resourceArn: str = None
    ) -> TagResourceResultTypeDef:
        """
        Adds one or more tags to the specified Amazon Lightsail resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#tag_resource)
        """
    def test_alarm(self, *, alarmName: str, state: AlarmStateType) -> TestAlarmResultTypeDef:
        """
        Tests an alarm by displaying a banner on the Amazon Lightsail console.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.test_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#test_alarm)
        """
    def unpeer_vpc(self) -> UnpeerVpcResultTypeDef:
        """
        Unpeers the Lightsail VPC from the user's default VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.unpeer_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#unpeer_vpc)
        """
    def untag_resource(
        self, *, resourceName: str, tagKeys: List[str], resourceArn: str = None
    ) -> UntagResourceResultTypeDef:
        """
        Deletes the specified set of tag keys and their values from the specified Amazon
        Lightsail resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#untag_resource)
        """
    def update_bucket(
        self,
        *,
        bucketName: str,
        accessRules: "AccessRulesTypeDef" = None,
        versioning: str = None,
        readonlyAccessAccounts: List[str] = None,
        accessLogConfig: "BucketAccessLogConfigTypeDef" = None
    ) -> UpdateBucketResultTypeDef:
        """
        Updates an existing Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_bucket)
        """
    def update_bucket_bundle(
        self, *, bucketName: str, bundleId: str
    ) -> UpdateBucketBundleResultTypeDef:
        """
        Updates the bundle, or storage plan, of an existing Amazon Lightsail bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_bucket_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_bucket_bundle)
        """
    def update_container_service(
        self,
        *,
        serviceName: str,
        power: ContainerServicePowerNameType = None,
        scale: int = None,
        isDisabled: bool = None,
        publicDomainNames: Dict[str, List[str]] = None,
        privateRegistryAccess: "PrivateRegistryAccessRequestTypeDef" = None
    ) -> UpdateContainerServiceResultTypeDef:
        """
        Updates the configuration of your Amazon Lightsail container service, such as
        its power, scale, and public domain names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_container_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_container_service)
        """
    def update_distribution(
        self,
        *,
        distributionName: str,
        origin: "InputOriginTypeDef" = None,
        defaultCacheBehavior: "CacheBehaviorTypeDef" = None,
        cacheBehaviorSettings: "CacheSettingsTypeDef" = None,
        cacheBehaviors: List["CacheBehaviorPerPathTypeDef"] = None,
        isEnabled: bool = None
    ) -> UpdateDistributionResultTypeDef:
        """
        Updates an existing Amazon Lightsail content delivery network (CDN)
        distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_distribution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_distribution)
        """
    def update_distribution_bundle(
        self, *, distributionName: str = None, bundleId: str = None
    ) -> UpdateDistributionBundleResultTypeDef:
        """
        Updates the bundle of your Amazon Lightsail content delivery network (CDN)
        distribution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_distribution_bundle)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_distribution_bundle)
        """
    def update_domain_entry(
        self, *, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> UpdateDomainEntryResultTypeDef:
        """
        Updates a domain recordset after it is created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_domain_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_domain_entry)
        """
    def update_instance_metadata_options(
        self,
        *,
        instanceName: str,
        httpTokens: HttpTokensType = None,
        httpEndpoint: HttpEndpointType = None,
        httpPutResponseHopLimit: int = None,
        httpProtocolIpv6: HttpProtocolIpv6Type = None
    ) -> UpdateInstanceMetadataOptionsResultTypeDef:
        """
        Modifies the Amazon Lightsail instance metadata parameters on a running or
        stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_instance_metadata_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_instance_metadata_options)
        """
    def update_load_balancer_attribute(
        self,
        *,
        loadBalancerName: str,
        attributeName: LoadBalancerAttributeNameType,
        attributeValue: str
    ) -> UpdateLoadBalancerAttributeResultTypeDef:
        """
        Updates the specified attribute for a load balancer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_load_balancer_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_load_balancer_attribute)
        """
    def update_relational_database(
        self,
        *,
        relationalDatabaseName: str,
        masterUserPassword: str = None,
        rotateMasterUserPassword: bool = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        enableBackupRetention: bool = None,
        disableBackupRetention: bool = None,
        publiclyAccessible: bool = None,
        applyImmediately: bool = None,
        caCertificateIdentifier: str = None
    ) -> UpdateRelationalDatabaseResultTypeDef:
        """
        Allows the update of one or more attributes of a database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_relational_database)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_relational_database)
        """
    def update_relational_database_parameters(
        self, *, relationalDatabaseName: str, parameters: List["RelationalDatabaseParameterTypeDef"]
    ) -> UpdateRelationalDatabaseParametersResultTypeDef:
        """
        Allows the update of one or more parameters of a database in Amazon Lightsail.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Client.update_relational_database_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/client.html#update_relational_database_parameters)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_active_names"]) -> GetActiveNamesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getactivenamespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_blueprints"]) -> GetBlueprintsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getblueprintspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_bundles"]) -> GetBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getbundlespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_cloud_formation_stack_records"]
    ) -> GetCloudFormationStackRecordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getcloudformationstackrecordspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_disk_snapshots"]
    ) -> GetDiskSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdisksnapshotspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_disks"]) -> GetDisksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdiskspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_domains"]) -> GetDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getdomainspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_export_snapshot_records"]
    ) -> GetExportSnapshotRecordsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getexportsnapshotrecordspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_instance_snapshots"]
    ) -> GetInstanceSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getinstancesnapshotspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_instances"]) -> GetInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getinstancespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_key_pairs"]) -> GetKeyPairsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getkeypairspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_load_balancers"]
    ) -> GetLoadBalancersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getloadbalancerspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_operations"]) -> GetOperationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getoperationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_blueprints"]
    ) -> GetRelationalDatabaseBlueprintsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseblueprintspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_bundles"]
    ) -> GetRelationalDatabaseBundlesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasebundlespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_events"]
    ) -> GetRelationalDatabaseEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseeventspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_parameters"]
    ) -> GetRelationalDatabaseParametersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabaseparameterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_snapshots"]
    ) -> GetRelationalDatabaseSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasesnapshotspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_databases"]
    ) -> GetRelationalDatabasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getrelationaldatabasespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["get_static_ips"]) -> GetStaticIpsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/paginators.html#getstaticipspaginator)
        """
