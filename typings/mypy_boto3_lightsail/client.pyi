# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for lightsail service client

Usage::

    ```python
    import boto3
    from mypy_boto3_lightsail import LightsailClient

    client: LightsailClient = boto3.client("lightsail")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_lightsail.paginator import (
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
from mypy_boto3_lightsail.type_defs import (
    AddOnRequestTypeDef,
    AllocateStaticIpResultTypeDef,
    AttachCertificateToDistributionResultTypeDef,
    AttachDiskResultTypeDef,
    AttachInstancesToLoadBalancerResultTypeDef,
    AttachLoadBalancerTlsCertificateResultTypeDef,
    AttachStaticIpResultTypeDef,
    CacheBehaviorPerPathTypeDef,
    CacheBehaviorTypeDef,
    CacheSettingsTypeDef,
    CloseInstancePublicPortsResultTypeDef,
    ContainerServiceDeploymentRequestTypeDef,
    ContainerServicesListResultTypeDef,
    ContainerTypeDef,
    CopySnapshotResultTypeDef,
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
    PutAlarmResultTypeDef,
    PutInstancePublicPortsResultTypeDef,
    RebootInstanceResultTypeDef,
    RebootRelationalDatabaseResultTypeDef,
    RegisterContainerImageResultTypeDef,
    RelationalDatabaseParameterTypeDef,
    ReleaseStaticIpResultTypeDef,
    ResetDistributionCacheResultTypeDef,
    SendContactMethodVerificationResultTypeDef,
    StartInstanceResultTypeDef,
    StartRelationalDatabaseResultTypeDef,
    StopInstanceResultTypeDef,
    StopRelationalDatabaseResultTypeDef,
    TagResourceResultTypeDef,
    TagTypeDef,
    TestAlarmResultTypeDef,
    UnpeerVpcResultTypeDef,
    UntagResourceResultTypeDef,
    UpdateContainerServiceResultTypeDef,
    UpdateDistributionBundleResultTypeDef,
    UpdateDistributionResultTypeDef,
    UpdateDomainEntryResultTypeDef,
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


class LightsailClient:
    """
    [Lightsail.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def allocate_static_ip(self, staticIpName: str) -> AllocateStaticIpResultTypeDef:
        """
        [Client.allocate_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.allocate_static_ip)
        """

    def attach_certificate_to_distribution(
        self, distributionName: str, certificateName: str
    ) -> AttachCertificateToDistributionResultTypeDef:
        """
        [Client.attach_certificate_to_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.attach_certificate_to_distribution)
        """

    def attach_disk(
        self, diskName: str, instanceName: str, diskPath: str
    ) -> AttachDiskResultTypeDef:
        """
        [Client.attach_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.attach_disk)
        """

    def attach_instances_to_load_balancer(
        self, loadBalancerName: str, instanceNames: List[str]
    ) -> AttachInstancesToLoadBalancerResultTypeDef:
        """
        [Client.attach_instances_to_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.attach_instances_to_load_balancer)
        """

    def attach_load_balancer_tls_certificate(
        self, loadBalancerName: str, certificateName: str
    ) -> AttachLoadBalancerTlsCertificateResultTypeDef:
        """
        [Client.attach_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.attach_load_balancer_tls_certificate)
        """

    def attach_static_ip(self, staticIpName: str, instanceName: str) -> AttachStaticIpResultTypeDef:
        """
        [Client.attach_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.attach_static_ip)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.can_paginate)
        """

    def close_instance_public_ports(
        self, portInfo: PortInfoTypeDef, instanceName: str
    ) -> CloseInstancePublicPortsResultTypeDef:
        """
        [Client.close_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.close_instance_public_ports)
        """

    def copy_snapshot(
        self,
        targetSnapshotName: str,
        sourceRegion: Literal[
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-central-1",
            "ca-central-1",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ap-northeast-2",
        ],
        sourceSnapshotName: str = None,
        sourceResourceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> CopySnapshotResultTypeDef:
        """
        [Client.copy_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.copy_snapshot)
        """

    def create_certificate(
        self,
        certificateName: str,
        domainName: str,
        subjectAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateCertificateResultTypeDef:
        """
        [Client.create_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_certificate)
        """

    def create_cloud_formation_stack(
        self, instances: List[InstanceEntryTypeDef]
    ) -> CreateCloudFormationStackResultTypeDef:
        """
        [Client.create_cloud_formation_stack documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_cloud_formation_stack)
        """

    def create_contact_method(
        self, protocol: Literal["Email", "SMS"], contactEndpoint: str
    ) -> CreateContactMethodResultTypeDef:
        """
        [Client.create_contact_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_contact_method)
        """

    def create_container_service(
        self,
        serviceName: str,
        power: Literal["nano", "micro", "small", "medium", "large", "xlarge"],
        scale: int,
        tags: List["TagTypeDef"] = None,
        publicDomainNames: Dict[str, List[str]] = None,
        deployment: ContainerServiceDeploymentRequestTypeDef = None,
    ) -> CreateContainerServiceResultTypeDef:
        """
        [Client.create_container_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_container_service)
        """

    def create_container_service_deployment(
        self,
        serviceName: str,
        containers: Dict[str, "ContainerTypeDef"] = None,
        publicEndpoint: "EndpointRequestTypeDef" = None,
    ) -> CreateContainerServiceDeploymentResultTypeDef:
        """
        [Client.create_container_service_deployment documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_container_service_deployment)
        """

    def create_container_service_registry_login(
        self,
    ) -> CreateContainerServiceRegistryLoginResultTypeDef:
        """
        [Client.create_container_service_registry_login documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_container_service_registry_login)
        """

    def create_disk(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        tags: List["TagTypeDef"] = None,
        addOns: List[AddOnRequestTypeDef] = None,
    ) -> CreateDiskResultTypeDef:
        """
        [Client.create_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_disk)
        """

    def create_disk_from_snapshot(
        self,
        diskName: str,
        availabilityZone: str,
        sizeInGb: int,
        diskSnapshotName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List[AddOnRequestTypeDef] = None,
        sourceDiskName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> CreateDiskFromSnapshotResultTypeDef:
        """
        [Client.create_disk_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_disk_from_snapshot)
        """

    def create_disk_snapshot(
        self,
        diskSnapshotName: str,
        diskName: str = None,
        instanceName: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDiskSnapshotResultTypeDef:
        """
        [Client.create_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_disk_snapshot)
        """

    def create_distribution(
        self,
        distributionName: str,
        origin: InputOriginTypeDef,
        defaultCacheBehavior: "CacheBehaviorTypeDef",
        bundleId: str,
        cacheBehaviorSettings: "CacheSettingsTypeDef" = None,
        cacheBehaviors: List["CacheBehaviorPerPathTypeDef"] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDistributionResultTypeDef:
        """
        [Client.create_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_distribution)
        """

    def create_domain(
        self, domainName: str, tags: List["TagTypeDef"] = None
    ) -> CreateDomainResultTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_domain)
        """

    def create_domain_entry(
        self, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> CreateDomainEntryResultTypeDef:
        """
        [Client.create_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_domain_entry)
        """

    def create_instance_snapshot(
        self, instanceSnapshotName: str, instanceName: str, tags: List["TagTypeDef"] = None
    ) -> CreateInstanceSnapshotResultTypeDef:
        """
        [Client.create_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_instance_snapshot)
        """

    def create_instances(
        self,
        instanceNames: List[str],
        availabilityZone: str,
        blueprintId: str,
        bundleId: str,
        customImageName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List[AddOnRequestTypeDef] = None,
    ) -> CreateInstancesResultTypeDef:
        """
        [Client.create_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_instances)
        """

    def create_instances_from_snapshot(
        self,
        instanceNames: List[str],
        availabilityZone: str,
        bundleId: str,
        attachedDiskMapping: Dict[str, List[DiskMapTypeDef]] = None,
        instanceSnapshotName: str = None,
        userData: str = None,
        keyPairName: str = None,
        tags: List["TagTypeDef"] = None,
        addOns: List[AddOnRequestTypeDef] = None,
        sourceInstanceName: str = None,
        restoreDate: str = None,
        useLatestRestorableAutoSnapshot: bool = None,
    ) -> CreateInstancesFromSnapshotResultTypeDef:
        """
        [Client.create_instances_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_instances_from_snapshot)
        """

    def create_key_pair(
        self, keyPairName: str, tags: List["TagTypeDef"] = None
    ) -> CreateKeyPairResultTypeDef:
        """
        [Client.create_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_key_pair)
        """

    def create_load_balancer(
        self,
        loadBalancerName: str,
        instancePort: int,
        healthCheckPath: str = None,
        certificateName: str = None,
        certificateDomainName: str = None,
        certificateAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateLoadBalancerResultTypeDef:
        """
        [Client.create_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_load_balancer)
        """

    def create_load_balancer_tls_certificate(
        self,
        loadBalancerName: str,
        certificateName: str,
        certificateDomainName: str,
        certificateAlternativeNames: List[str] = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateLoadBalancerTlsCertificateResultTypeDef:
        """
        [Client.create_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_load_balancer_tls_certificate)
        """

    def create_relational_database(
        self,
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
        tags: List["TagTypeDef"] = None,
    ) -> CreateRelationalDatabaseResultTypeDef:
        """
        [Client.create_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_relational_database)
        """

    def create_relational_database_from_snapshot(
        self,
        relationalDatabaseName: str,
        availabilityZone: str = None,
        publiclyAccessible: bool = None,
        relationalDatabaseSnapshotName: str = None,
        relationalDatabaseBundleId: str = None,
        sourceRelationalDatabaseName: str = None,
        restoreTime: datetime = None,
        useLatestRestorableTime: bool = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateRelationalDatabaseFromSnapshotResultTypeDef:
        """
        [Client.create_relational_database_from_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_relational_database_from_snapshot)
        """

    def create_relational_database_snapshot(
        self,
        relationalDatabaseName: str,
        relationalDatabaseSnapshotName: str,
        tags: List["TagTypeDef"] = None,
    ) -> CreateRelationalDatabaseSnapshotResultTypeDef:
        """
        [Client.create_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.create_relational_database_snapshot)
        """

    def delete_alarm(self, alarmName: str) -> DeleteAlarmResultTypeDef:
        """
        [Client.delete_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_alarm)
        """

    def delete_auto_snapshot(self, resourceName: str, date: str) -> DeleteAutoSnapshotResultTypeDef:
        """
        [Client.delete_auto_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_auto_snapshot)
        """

    def delete_certificate(self, certificateName: str) -> DeleteCertificateResultTypeDef:
        """
        [Client.delete_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_certificate)
        """

    def delete_contact_method(
        self, protocol: Literal["Email", "SMS"]
    ) -> DeleteContactMethodResultTypeDef:
        """
        [Client.delete_contact_method documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_contact_method)
        """

    def delete_container_image(self, serviceName: str, image: str) -> Dict[str, Any]:
        """
        [Client.delete_container_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_container_image)
        """

    def delete_container_service(self, serviceName: str) -> Dict[str, Any]:
        """
        [Client.delete_container_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_container_service)
        """

    def delete_disk(self, diskName: str, forceDeleteAddOns: bool = None) -> DeleteDiskResultTypeDef:
        """
        [Client.delete_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_disk)
        """

    def delete_disk_snapshot(self, diskSnapshotName: str) -> DeleteDiskSnapshotResultTypeDef:
        """
        [Client.delete_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_disk_snapshot)
        """

    def delete_distribution(self, distributionName: str = None) -> DeleteDistributionResultTypeDef:
        """
        [Client.delete_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_distribution)
        """

    def delete_domain(self, domainName: str) -> DeleteDomainResultTypeDef:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_domain)
        """

    def delete_domain_entry(
        self, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> DeleteDomainEntryResultTypeDef:
        """
        [Client.delete_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_domain_entry)
        """

    def delete_instance(
        self, instanceName: str, forceDeleteAddOns: bool = None
    ) -> DeleteInstanceResultTypeDef:
        """
        [Client.delete_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_instance)
        """

    def delete_instance_snapshot(
        self, instanceSnapshotName: str
    ) -> DeleteInstanceSnapshotResultTypeDef:
        """
        [Client.delete_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_instance_snapshot)
        """

    def delete_key_pair(self, keyPairName: str) -> DeleteKeyPairResultTypeDef:
        """
        [Client.delete_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_key_pair)
        """

    def delete_known_host_keys(self, instanceName: str) -> DeleteKnownHostKeysResultTypeDef:
        """
        [Client.delete_known_host_keys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_known_host_keys)
        """

    def delete_load_balancer(self, loadBalancerName: str) -> DeleteLoadBalancerResultTypeDef:
        """
        [Client.delete_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer)
        """

    def delete_load_balancer_tls_certificate(
        self, loadBalancerName: str, certificateName: str, force: bool = None
    ) -> DeleteLoadBalancerTlsCertificateResultTypeDef:
        """
        [Client.delete_load_balancer_tls_certificate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_load_balancer_tls_certificate)
        """

    def delete_relational_database(
        self,
        relationalDatabaseName: str,
        skipFinalSnapshot: bool = None,
        finalRelationalDatabaseSnapshotName: str = None,
    ) -> DeleteRelationalDatabaseResultTypeDef:
        """
        [Client.delete_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_relational_database)
        """

    def delete_relational_database_snapshot(
        self, relationalDatabaseSnapshotName: str
    ) -> DeleteRelationalDatabaseSnapshotResultTypeDef:
        """
        [Client.delete_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.delete_relational_database_snapshot)
        """

    def detach_certificate_from_distribution(
        self, distributionName: str
    ) -> DetachCertificateFromDistributionResultTypeDef:
        """
        [Client.detach_certificate_from_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.detach_certificate_from_distribution)
        """

    def detach_disk(self, diskName: str) -> DetachDiskResultTypeDef:
        """
        [Client.detach_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.detach_disk)
        """

    def detach_instances_from_load_balancer(
        self, loadBalancerName: str, instanceNames: List[str]
    ) -> DetachInstancesFromLoadBalancerResultTypeDef:
        """
        [Client.detach_instances_from_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.detach_instances_from_load_balancer)
        """

    def detach_static_ip(self, staticIpName: str) -> DetachStaticIpResultTypeDef:
        """
        [Client.detach_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.detach_static_ip)
        """

    def disable_add_on(
        self, addOnType: Literal["AutoSnapshot"], resourceName: str
    ) -> DisableAddOnResultTypeDef:
        """
        [Client.disable_add_on documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.disable_add_on)
        """

    def download_default_key_pair(self) -> DownloadDefaultKeyPairResultTypeDef:
        """
        [Client.download_default_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.download_default_key_pair)
        """

    def enable_add_on(
        self, resourceName: str, addOnRequest: AddOnRequestTypeDef
    ) -> EnableAddOnResultTypeDef:
        """
        [Client.enable_add_on documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.enable_add_on)
        """

    def export_snapshot(self, sourceSnapshotName: str) -> ExportSnapshotResultTypeDef:
        """
        [Client.export_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.export_snapshot)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.generate_presigned_url)
        """

    def get_active_names(self, pageToken: str = None) -> GetActiveNamesResultTypeDef:
        """
        [Client.get_active_names documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_active_names)
        """

    def get_alarms(
        self, alarmName: str = None, pageToken: str = None, monitoredResourceName: str = None
    ) -> GetAlarmsResultTypeDef:
        """
        [Client.get_alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_alarms)
        """

    def get_auto_snapshots(self, resourceName: str) -> GetAutoSnapshotsResultTypeDef:
        """
        [Client.get_auto_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_auto_snapshots)
        """

    def get_blueprints(
        self, includeInactive: bool = None, pageToken: str = None
    ) -> GetBlueprintsResultTypeDef:
        """
        [Client.get_blueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_blueprints)
        """

    def get_bundles(
        self, includeInactive: bool = None, pageToken: str = None
    ) -> GetBundlesResultTypeDef:
        """
        [Client.get_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_bundles)
        """

    def get_certificates(
        self,
        certificateStatuses: List[
            Literal[
                "PENDING_VALIDATION",
                "ISSUED",
                "INACTIVE",
                "EXPIRED",
                "VALIDATION_TIMED_OUT",
                "REVOKED",
                "FAILED",
            ]
        ] = None,
        includeCertificateDetails: bool = None,
        certificateName: str = None,
    ) -> GetCertificatesResultTypeDef:
        """
        [Client.get_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_certificates)
        """

    def get_cloud_formation_stack_records(
        self, pageToken: str = None
    ) -> GetCloudFormationStackRecordsResultTypeDef:
        """
        [Client.get_cloud_formation_stack_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_cloud_formation_stack_records)
        """

    def get_contact_methods(
        self, protocols: List[Literal["Email", "SMS"]] = None
    ) -> GetContactMethodsResultTypeDef:
        """
        [Client.get_contact_methods documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_contact_methods)
        """

    def get_container_api_metadata(self) -> GetContainerAPIMetadataResultTypeDef:
        """
        [Client.get_container_api_metadata documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_container_api_metadata)
        """

    def get_container_images(self, serviceName: str) -> GetContainerImagesResultTypeDef:
        """
        [Client.get_container_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_container_images)
        """

    def get_container_log(
        self,
        serviceName: str,
        containerName: str,
        startTime: datetime = None,
        endTime: datetime = None,
        filterPattern: str = None,
        pageToken: str = None,
    ) -> GetContainerLogResultTypeDef:
        """
        [Client.get_container_log documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_container_log)
        """

    def get_container_service_deployments(
        self, serviceName: str
    ) -> GetContainerServiceDeploymentsResultTypeDef:
        """
        [Client.get_container_service_deployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_container_service_deployments)
        """

    def get_container_service_metric_data(
        self,
        serviceName: str,
        metricName: Literal["CPUUtilization", "MemoryUtilization"],
        startTime: datetime,
        endTime: datetime,
        period: int,
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> GetContainerServiceMetricDataResultTypeDef:
        """
        [Client.get_container_service_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_container_service_metric_data)
        """

    def get_container_service_powers(self) -> GetContainerServicePowersResultTypeDef:
        """
        [Client.get_container_service_powers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_container_service_powers)
        """

    def get_container_services(self, serviceName: str = None) -> ContainerServicesListResultTypeDef:
        """
        [Client.get_container_services documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_container_services)
        """

    def get_disk(self, diskName: str) -> GetDiskResultTypeDef:
        """
        [Client.get_disk documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_disk)
        """

    def get_disk_snapshot(self, diskSnapshotName: str) -> GetDiskSnapshotResultTypeDef:
        """
        [Client.get_disk_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshot)
        """

    def get_disk_snapshots(self, pageToken: str = None) -> GetDiskSnapshotsResultTypeDef:
        """
        [Client.get_disk_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_disk_snapshots)
        """

    def get_disks(self, pageToken: str = None) -> GetDisksResultTypeDef:
        """
        [Client.get_disks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_disks)
        """

    def get_distribution_bundles(self) -> GetDistributionBundlesResultTypeDef:
        """
        [Client.get_distribution_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_distribution_bundles)
        """

    def get_distribution_latest_cache_reset(
        self, distributionName: str = None
    ) -> GetDistributionLatestCacheResetResultTypeDef:
        """
        [Client.get_distribution_latest_cache_reset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_distribution_latest_cache_reset)
        """

    def get_distribution_metric_data(
        self,
        distributionName: str,
        metricName: Literal[
            "Requests",
            "BytesDownloaded",
            "BytesUploaded",
            "TotalErrorRate",
            "Http4xxErrorRate",
            "Http5xxErrorRate",
        ],
        startTime: datetime,
        endTime: datetime,
        period: int,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> GetDistributionMetricDataResultTypeDef:
        """
        [Client.get_distribution_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_distribution_metric_data)
        """

    def get_distributions(
        self, distributionName: str = None, pageToken: str = None
    ) -> GetDistributionsResultTypeDef:
        """
        [Client.get_distributions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_distributions)
        """

    def get_domain(self, domainName: str) -> GetDomainResultTypeDef:
        """
        [Client.get_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_domain)
        """

    def get_domains(self, pageToken: str = None) -> GetDomainsResultTypeDef:
        """
        [Client.get_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_domains)
        """

    def get_export_snapshot_records(
        self, pageToken: str = None
    ) -> GetExportSnapshotRecordsResultTypeDef:
        """
        [Client.get_export_snapshot_records documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_export_snapshot_records)
        """

    def get_instance(self, instanceName: str) -> GetInstanceResultTypeDef:
        """
        [Client.get_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_instance)
        """

    def get_instance_access_details(
        self, instanceName: str, protocol: Literal["ssh", "rdp"] = None
    ) -> GetInstanceAccessDetailsResultTypeDef:
        """
        [Client.get_instance_access_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_instance_access_details)
        """

    def get_instance_metric_data(
        self,
        instanceName: str,
        metricName: Literal[
            "CPUUtilization",
            "NetworkIn",
            "NetworkOut",
            "StatusCheckFailed",
            "StatusCheckFailed_Instance",
            "StatusCheckFailed_System",
            "BurstCapacityTime",
            "BurstCapacityPercentage",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> GetInstanceMetricDataResultTypeDef:
        """
        [Client.get_instance_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_instance_metric_data)
        """

    def get_instance_port_states(self, instanceName: str) -> GetInstancePortStatesResultTypeDef:
        """
        [Client.get_instance_port_states documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_instance_port_states)
        """

    def get_instance_snapshot(self, instanceSnapshotName: str) -> GetInstanceSnapshotResultTypeDef:
        """
        [Client.get_instance_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshot)
        """

    def get_instance_snapshots(self, pageToken: str = None) -> GetInstanceSnapshotsResultTypeDef:
        """
        [Client.get_instance_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_instance_snapshots)
        """

    def get_instance_state(self, instanceName: str) -> GetInstanceStateResultTypeDef:
        """
        [Client.get_instance_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_instance_state)
        """

    def get_instances(self, pageToken: str = None) -> GetInstancesResultTypeDef:
        """
        [Client.get_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_instances)
        """

    def get_key_pair(self, keyPairName: str) -> GetKeyPairResultTypeDef:
        """
        [Client.get_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_key_pair)
        """

    def get_key_pairs(self, pageToken: str = None) -> GetKeyPairsResultTypeDef:
        """
        [Client.get_key_pairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_key_pairs)
        """

    def get_load_balancer(self, loadBalancerName: str) -> GetLoadBalancerResultTypeDef:
        """
        [Client.get_load_balancer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_load_balancer)
        """

    def get_load_balancer_metric_data(
        self,
        loadBalancerName: str,
        metricName: Literal[
            "ClientTLSNegotiationErrorCount",
            "HealthyHostCount",
            "UnhealthyHostCount",
            "HTTPCode_LB_4XX_Count",
            "HTTPCode_LB_5XX_Count",
            "HTTPCode_Instance_2XX_Count",
            "HTTPCode_Instance_3XX_Count",
            "HTTPCode_Instance_4XX_Count",
            "HTTPCode_Instance_5XX_Count",
            "InstanceResponseTime",
            "RejectedConnectionCount",
            "RequestCount",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> GetLoadBalancerMetricDataResultTypeDef:
        """
        [Client.get_load_balancer_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_metric_data)
        """

    def get_load_balancer_tls_certificates(
        self, loadBalancerName: str
    ) -> GetLoadBalancerTlsCertificatesResultTypeDef:
        """
        [Client.get_load_balancer_tls_certificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_load_balancer_tls_certificates)
        """

    def get_load_balancers(self, pageToken: str = None) -> GetLoadBalancersResultTypeDef:
        """
        [Client.get_load_balancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_load_balancers)
        """

    def get_operation(self, operationId: str) -> GetOperationResultTypeDef:
        """
        [Client.get_operation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_operation)
        """

    def get_operations(self, pageToken: str = None) -> GetOperationsResultTypeDef:
        """
        [Client.get_operations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_operations)
        """

    def get_operations_for_resource(
        self, resourceName: str, pageToken: str = None
    ) -> GetOperationsForResourceResultTypeDef:
        """
        [Client.get_operations_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_operations_for_resource)
        """

    def get_regions(
        self,
        includeAvailabilityZones: bool = None,
        includeRelationalDatabaseAvailabilityZones: bool = None,
    ) -> GetRegionsResultTypeDef:
        """
        [Client.get_regions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_regions)
        """

    def get_relational_database(
        self, relationalDatabaseName: str
    ) -> GetRelationalDatabaseResultTypeDef:
        """
        [Client.get_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database)
        """

    def get_relational_database_blueprints(
        self, pageToken: str = None
    ) -> GetRelationalDatabaseBlueprintsResultTypeDef:
        """
        [Client.get_relational_database_blueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_blueprints)
        """

    def get_relational_database_bundles(
        self, pageToken: str = None
    ) -> GetRelationalDatabaseBundlesResultTypeDef:
        """
        [Client.get_relational_database_bundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_bundles)
        """

    def get_relational_database_events(
        self, relationalDatabaseName: str, durationInMinutes: int = None, pageToken: str = None
    ) -> GetRelationalDatabaseEventsResultTypeDef:
        """
        [Client.get_relational_database_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_events)
        """

    def get_relational_database_log_events(
        self,
        relationalDatabaseName: str,
        logStreamName: str,
        startTime: datetime = None,
        endTime: datetime = None,
        startFromHead: bool = None,
        pageToken: str = None,
    ) -> GetRelationalDatabaseLogEventsResultTypeDef:
        """
        [Client.get_relational_database_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_events)
        """

    def get_relational_database_log_streams(
        self, relationalDatabaseName: str
    ) -> GetRelationalDatabaseLogStreamsResultTypeDef:
        """
        [Client.get_relational_database_log_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_log_streams)
        """

    def get_relational_database_master_user_password(
        self,
        relationalDatabaseName: str,
        passwordVersion: Literal["CURRENT", "PREVIOUS", "PENDING"] = None,
    ) -> GetRelationalDatabaseMasterUserPasswordResultTypeDef:
        """
        [Client.get_relational_database_master_user_password documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_master_user_password)
        """

    def get_relational_database_metric_data(
        self,
        relationalDatabaseName: str,
        metricName: Literal[
            "CPUUtilization",
            "DatabaseConnections",
            "DiskQueueDepth",
            "FreeStorageSpace",
            "NetworkReceiveThroughput",
            "NetworkTransmitThroughput",
        ],
        period: int,
        startTime: datetime,
        endTime: datetime,
        unit: Literal[
            "Seconds",
            "Microseconds",
            "Milliseconds",
            "Bytes",
            "Kilobytes",
            "Megabytes",
            "Gigabytes",
            "Terabytes",
            "Bits",
            "Kilobits",
            "Megabits",
            "Gigabits",
            "Terabits",
            "Percent",
            "Count",
            "Bytes/Second",
            "Kilobytes/Second",
            "Megabytes/Second",
            "Gigabytes/Second",
            "Terabytes/Second",
            "Bits/Second",
            "Kilobits/Second",
            "Megabits/Second",
            "Gigabits/Second",
            "Terabits/Second",
            "Count/Second",
            "None",
        ],
        statistics: List[Literal["Minimum", "Maximum", "Sum", "Average", "SampleCount"]],
    ) -> GetRelationalDatabaseMetricDataResultTypeDef:
        """
        [Client.get_relational_database_metric_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_metric_data)
        """

    def get_relational_database_parameters(
        self, relationalDatabaseName: str, pageToken: str = None
    ) -> GetRelationalDatabaseParametersResultTypeDef:
        """
        [Client.get_relational_database_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_parameters)
        """

    def get_relational_database_snapshot(
        self, relationalDatabaseSnapshotName: str
    ) -> GetRelationalDatabaseSnapshotResultTypeDef:
        """
        [Client.get_relational_database_snapshot documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshot)
        """

    def get_relational_database_snapshots(
        self, pageToken: str = None
    ) -> GetRelationalDatabaseSnapshotsResultTypeDef:
        """
        [Client.get_relational_database_snapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_database_snapshots)
        """

    def get_relational_databases(
        self, pageToken: str = None
    ) -> GetRelationalDatabasesResultTypeDef:
        """
        [Client.get_relational_databases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_relational_databases)
        """

    def get_static_ip(self, staticIpName: str) -> GetStaticIpResultTypeDef:
        """
        [Client.get_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_static_ip)
        """

    def get_static_ips(self, pageToken: str = None) -> GetStaticIpsResultTypeDef:
        """
        [Client.get_static_ips documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.get_static_ips)
        """

    def import_key_pair(self, keyPairName: str, publicKeyBase64: str) -> ImportKeyPairResultTypeDef:
        """
        [Client.import_key_pair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.import_key_pair)
        """

    def is_vpc_peered(self) -> IsVpcPeeredResultTypeDef:
        """
        [Client.is_vpc_peered documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.is_vpc_peered)
        """

    def open_instance_public_ports(
        self, portInfo: PortInfoTypeDef, instanceName: str
    ) -> OpenInstancePublicPortsResultTypeDef:
        """
        [Client.open_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.open_instance_public_ports)
        """

    def peer_vpc(self) -> PeerVpcResultTypeDef:
        """
        [Client.peer_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.peer_vpc)
        """

    def put_alarm(
        self,
        alarmName: str,
        metricName: Literal[
            "CPUUtilization",
            "NetworkIn",
            "NetworkOut",
            "StatusCheckFailed",
            "StatusCheckFailed_Instance",
            "StatusCheckFailed_System",
            "ClientTLSNegotiationErrorCount",
            "HealthyHostCount",
            "UnhealthyHostCount",
            "HTTPCode_LB_4XX_Count",
            "HTTPCode_LB_5XX_Count",
            "HTTPCode_Instance_2XX_Count",
            "HTTPCode_Instance_3XX_Count",
            "HTTPCode_Instance_4XX_Count",
            "HTTPCode_Instance_5XX_Count",
            "InstanceResponseTime",
            "RejectedConnectionCount",
            "RequestCount",
            "DatabaseConnections",
            "DiskQueueDepth",
            "FreeStorageSpace",
            "NetworkReceiveThroughput",
            "NetworkTransmitThroughput",
            "BurstCapacityTime",
            "BurstCapacityPercentage",
        ],
        monitoredResourceName: str,
        comparisonOperator: Literal[
            "GreaterThanOrEqualToThreshold",
            "GreaterThanThreshold",
            "LessThanThreshold",
            "LessThanOrEqualToThreshold",
        ],
        threshold: float,
        evaluationPeriods: int,
        datapointsToAlarm: int = None,
        treatMissingData: Literal["breaching", "notBreaching", "ignore", "missing"] = None,
        contactProtocols: List[Literal["Email", "SMS"]] = None,
        notificationTriggers: List[Literal["OK", "ALARM", "INSUFFICIENT_DATA"]] = None,
        notificationEnabled: bool = None,
    ) -> PutAlarmResultTypeDef:
        """
        [Client.put_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.put_alarm)
        """

    def put_instance_public_ports(
        self, portInfos: List[PortInfoTypeDef], instanceName: str
    ) -> PutInstancePublicPortsResultTypeDef:
        """
        [Client.put_instance_public_ports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.put_instance_public_ports)
        """

    def reboot_instance(self, instanceName: str) -> RebootInstanceResultTypeDef:
        """
        [Client.reboot_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.reboot_instance)
        """

    def reboot_relational_database(
        self, relationalDatabaseName: str
    ) -> RebootRelationalDatabaseResultTypeDef:
        """
        [Client.reboot_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.reboot_relational_database)
        """

    def register_container_image(
        self, serviceName: str, label: str, digest: str
    ) -> RegisterContainerImageResultTypeDef:
        """
        [Client.register_container_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.register_container_image)
        """

    def release_static_ip(self, staticIpName: str) -> ReleaseStaticIpResultTypeDef:
        """
        [Client.release_static_ip documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.release_static_ip)
        """

    def reset_distribution_cache(
        self, distributionName: str = None
    ) -> ResetDistributionCacheResultTypeDef:
        """
        [Client.reset_distribution_cache documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.reset_distribution_cache)
        """

    def send_contact_method_verification(
        self, protocol: Literal["Email"]
    ) -> SendContactMethodVerificationResultTypeDef:
        """
        [Client.send_contact_method_verification documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.send_contact_method_verification)
        """

    def start_instance(self, instanceName: str) -> StartInstanceResultTypeDef:
        """
        [Client.start_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.start_instance)
        """

    def start_relational_database(
        self, relationalDatabaseName: str
    ) -> StartRelationalDatabaseResultTypeDef:
        """
        [Client.start_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.start_relational_database)
        """

    def stop_instance(self, instanceName: str, force: bool = None) -> StopInstanceResultTypeDef:
        """
        [Client.stop_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.stop_instance)
        """

    def stop_relational_database(
        self, relationalDatabaseName: str, relationalDatabaseSnapshotName: str = None
    ) -> StopRelationalDatabaseResultTypeDef:
        """
        [Client.stop_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.stop_relational_database)
        """

    def tag_resource(
        self, resourceName: str, tags: List["TagTypeDef"], resourceArn: str = None
    ) -> TagResourceResultTypeDef:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.tag_resource)
        """

    def test_alarm(
        self, alarmName: str, state: Literal["OK", "ALARM", "INSUFFICIENT_DATA"]
    ) -> TestAlarmResultTypeDef:
        """
        [Client.test_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.test_alarm)
        """

    def unpeer_vpc(self) -> UnpeerVpcResultTypeDef:
        """
        [Client.unpeer_vpc documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.unpeer_vpc)
        """

    def untag_resource(
        self, resourceName: str, tagKeys: List[str], resourceArn: str = None
    ) -> UntagResourceResultTypeDef:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.untag_resource)
        """

    def update_container_service(
        self,
        serviceName: str,
        power: Literal["nano", "micro", "small", "medium", "large", "xlarge"] = None,
        scale: int = None,
        isDisabled: bool = None,
        publicDomainNames: Dict[str, List[str]] = None,
    ) -> UpdateContainerServiceResultTypeDef:
        """
        [Client.update_container_service documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.update_container_service)
        """

    def update_distribution(
        self,
        distributionName: str,
        origin: InputOriginTypeDef = None,
        defaultCacheBehavior: "CacheBehaviorTypeDef" = None,
        cacheBehaviorSettings: "CacheSettingsTypeDef" = None,
        cacheBehaviors: List["CacheBehaviorPerPathTypeDef"] = None,
        isEnabled: bool = None,
    ) -> UpdateDistributionResultTypeDef:
        """
        [Client.update_distribution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.update_distribution)
        """

    def update_distribution_bundle(
        self, distributionName: str = None, bundleId: str = None
    ) -> UpdateDistributionBundleResultTypeDef:
        """
        [Client.update_distribution_bundle documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.update_distribution_bundle)
        """

    def update_domain_entry(
        self, domainName: str, domainEntry: "DomainEntryTypeDef"
    ) -> UpdateDomainEntryResultTypeDef:
        """
        [Client.update_domain_entry documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.update_domain_entry)
        """

    def update_load_balancer_attribute(
        self,
        loadBalancerName: str,
        attributeName: Literal[
            "HealthCheckPath",
            "SessionStickinessEnabled",
            "SessionStickiness_LB_CookieDurationSeconds",
        ],
        attributeValue: str,
    ) -> UpdateLoadBalancerAttributeResultTypeDef:
        """
        [Client.update_load_balancer_attribute documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.update_load_balancer_attribute)
        """

    def update_relational_database(
        self,
        relationalDatabaseName: str,
        masterUserPassword: str = None,
        rotateMasterUserPassword: bool = None,
        preferredBackupWindow: str = None,
        preferredMaintenanceWindow: str = None,
        enableBackupRetention: bool = None,
        disableBackupRetention: bool = None,
        publiclyAccessible: bool = None,
        applyImmediately: bool = None,
        caCertificateIdentifier: str = None,
    ) -> UpdateRelationalDatabaseResultTypeDef:
        """
        [Client.update_relational_database documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.update_relational_database)
        """

    def update_relational_database_parameters(
        self, relationalDatabaseName: str, parameters: List["RelationalDatabaseParameterTypeDef"]
    ) -> UpdateRelationalDatabaseParametersResultTypeDef:
        """
        [Client.update_relational_database_parameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Client.update_relational_database_parameters)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_active_names"]) -> GetActiveNamesPaginator:
        """
        [Paginator.GetActiveNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetActiveNames)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_blueprints"]) -> GetBlueprintsPaginator:
        """
        [Paginator.GetBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetBlueprints)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_bundles"]) -> GetBundlesPaginator:
        """
        [Paginator.GetBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetBundles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_cloud_formation_stack_records"]
    ) -> GetCloudFormationStackRecordsPaginator:
        """
        [Paginator.GetCloudFormationStackRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetCloudFormationStackRecords)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_disk_snapshots"]
    ) -> GetDiskSnapshotsPaginator:
        """
        [Paginator.GetDiskSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDiskSnapshots)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_disks"]) -> GetDisksPaginator:
        """
        [Paginator.GetDisks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDisks)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_domains"]) -> GetDomainsPaginator:
        """
        [Paginator.GetDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetDomains)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_export_snapshot_records"]
    ) -> GetExportSnapshotRecordsPaginator:
        """
        [Paginator.GetExportSnapshotRecords documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetExportSnapshotRecords)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_instance_snapshots"]
    ) -> GetInstanceSnapshotsPaginator:
        """
        [Paginator.GetInstanceSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetInstanceSnapshots)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_instances"]) -> GetInstancesPaginator:
        """
        [Paginator.GetInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetInstances)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_key_pairs"]) -> GetKeyPairsPaginator:
        """
        [Paginator.GetKeyPairs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetKeyPairs)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_load_balancers"]
    ) -> GetLoadBalancersPaginator:
        """
        [Paginator.GetLoadBalancers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetLoadBalancers)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_operations"]) -> GetOperationsPaginator:
        """
        [Paginator.GetOperations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetOperations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_blueprints"]
    ) -> GetRelationalDatabaseBlueprintsPaginator:
        """
        [Paginator.GetRelationalDatabaseBlueprints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBlueprints)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_bundles"]
    ) -> GetRelationalDatabaseBundlesPaginator:
        """
        [Paginator.GetRelationalDatabaseBundles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseBundles)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_events"]
    ) -> GetRelationalDatabaseEventsPaginator:
        """
        [Paginator.GetRelationalDatabaseEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseEvents)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_parameters"]
    ) -> GetRelationalDatabaseParametersPaginator:
        """
        [Paginator.GetRelationalDatabaseParameters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseParameters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_database_snapshots"]
    ) -> GetRelationalDatabaseSnapshotsPaginator:
        """
        [Paginator.GetRelationalDatabaseSnapshots documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabaseSnapshots)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_relational_databases"]
    ) -> GetRelationalDatabasesPaginator:
        """
        [Paginator.GetRelationalDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetRelationalDatabases)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_static_ips"]) -> GetStaticIpsPaginator:
        """
        [Paginator.GetStaticIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/lightsail.html#Lightsail.Paginator.GetStaticIps)
        """
