"""
Type annotations for lightsail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lightsail.type_defs import AccessKeyTypeDef

    data: AccessKeyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AccessDirectionType,
    AccessTypeType,
    AlarmStateType,
    AutoSnapshotStatusType,
    BehaviorEnumType,
    BlueprintTypeType,
    BucketMetricNameType,
    CertificateStatusType,
    ComparisonOperatorType,
    ContactMethodStatusType,
    ContactProtocolType,
    ContainerServiceDeploymentStateType,
    ContainerServiceMetricNameType,
    ContainerServicePowerNameType,
    ContainerServiceProtocolType,
    ContainerServiceStateDetailCodeType,
    ContainerServiceStateType,
    DiskSnapshotStateType,
    DiskStateType,
    DistributionMetricNameType,
    ExportSnapshotRecordSourceTypeType,
    ForwardValuesType,
    HeaderEnumType,
    InstanceAccessProtocolType,
    InstanceHealthReasonType,
    InstanceHealthStateType,
    InstanceMetricNameType,
    InstancePlatformType,
    InstanceSnapshotStateType,
    IpAddressTypeType,
    LoadBalancerAttributeNameType,
    LoadBalancerMetricNameType,
    LoadBalancerProtocolType,
    LoadBalancerStateType,
    LoadBalancerTlsCertificateDomainStatusType,
    LoadBalancerTlsCertificateFailureReasonType,
    LoadBalancerTlsCertificateRenewalStatusType,
    LoadBalancerTlsCertificateRevocationReasonType,
    LoadBalancerTlsCertificateStatusType,
    MetricNameType,
    MetricStatisticType,
    MetricUnitType,
    NetworkProtocolType,
    OperationStatusType,
    OperationTypeType,
    OriginProtocolPolicyEnumType,
    PortAccessTypeType,
    PortInfoSourceTypeType,
    PortStateType,
    RecordStateType,
    RegionNameType,
    RelationalDatabaseMetricNameType,
    RelationalDatabasePasswordVersionType,
    RenewalStatusType,
    ResourceBucketAccessType,
    ResourceTypeType,
    StatusTypeType,
    TreatMissingDataType,
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
    "AccessKeyTypeDef",
    "AccessRulesTypeDef",
    "AddOnRequestTypeDef",
    "AddOnTypeDef",
    "AlarmTypeDef",
    "AllocateStaticIpRequestRequestTypeDef",
    "AllocateStaticIpResultTypeDef",
    "AttachCertificateToDistributionRequestRequestTypeDef",
    "AttachCertificateToDistributionResultTypeDef",
    "AttachDiskRequestRequestTypeDef",
    "AttachDiskResultTypeDef",
    "AttachInstancesToLoadBalancerRequestRequestTypeDef",
    "AttachInstancesToLoadBalancerResultTypeDef",
    "AttachLoadBalancerTlsCertificateRequestRequestTypeDef",
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    "AttachStaticIpRequestRequestTypeDef",
    "AttachStaticIpResultTypeDef",
    "AttachedDiskTypeDef",
    "AutoSnapshotAddOnRequestTypeDef",
    "AutoSnapshotDetailsTypeDef",
    "AvailabilityZoneTypeDef",
    "BlueprintTypeDef",
    "BucketBundleTypeDef",
    "BucketStateTypeDef",
    "BucketTypeDef",
    "BundleTypeDef",
    "CacheBehaviorPerPathTypeDef",
    "CacheBehaviorTypeDef",
    "CacheSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CloseInstancePublicPortsRequestRequestTypeDef",
    "CloseInstancePublicPortsResultTypeDef",
    "CloudFormationStackRecordSourceInfoTypeDef",
    "CloudFormationStackRecordTypeDef",
    "ContactMethodTypeDef",
    "ContainerImageTypeDef",
    "ContainerServiceDeploymentRequestTypeDef",
    "ContainerServiceDeploymentTypeDef",
    "ContainerServiceEndpointTypeDef",
    "ContainerServiceHealthCheckConfigTypeDef",
    "ContainerServiceLogEventTypeDef",
    "ContainerServicePowerTypeDef",
    "ContainerServiceRegistryLoginTypeDef",
    "ContainerServiceStateDetailTypeDef",
    "ContainerServiceTypeDef",
    "ContainerServicesListResultTypeDef",
    "ContainerTypeDef",
    "CookieObjectTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateBucketAccessKeyRequestRequestTypeDef",
    "CreateBucketAccessKeyResultTypeDef",
    "CreateBucketRequestRequestTypeDef",
    "CreateBucketResultTypeDef",
    "CreateCertificateRequestRequestTypeDef",
    "CreateCertificateResultTypeDef",
    "CreateCloudFormationStackRequestRequestTypeDef",
    "CreateCloudFormationStackResultTypeDef",
    "CreateContactMethodRequestRequestTypeDef",
    "CreateContactMethodResultTypeDef",
    "CreateContainerServiceDeploymentRequestRequestTypeDef",
    "CreateContainerServiceDeploymentResultTypeDef",
    "CreateContainerServiceRegistryLoginResultTypeDef",
    "CreateContainerServiceRequestRequestTypeDef",
    "CreateContainerServiceResultTypeDef",
    "CreateDiskFromSnapshotRequestRequestTypeDef",
    "CreateDiskFromSnapshotResultTypeDef",
    "CreateDiskRequestRequestTypeDef",
    "CreateDiskResultTypeDef",
    "CreateDiskSnapshotRequestRequestTypeDef",
    "CreateDiskSnapshotResultTypeDef",
    "CreateDistributionRequestRequestTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDomainEntryRequestRequestTypeDef",
    "CreateDomainEntryResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResultTypeDef",
    "CreateInstanceSnapshotRequestRequestTypeDef",
    "CreateInstanceSnapshotResultTypeDef",
    "CreateInstancesFromSnapshotRequestRequestTypeDef",
    "CreateInstancesFromSnapshotResultTypeDef",
    "CreateInstancesRequestRequestTypeDef",
    "CreateInstancesResultTypeDef",
    "CreateKeyPairRequestRequestTypeDef",
    "CreateKeyPairResultTypeDef",
    "CreateLoadBalancerRequestRequestTypeDef",
    "CreateLoadBalancerResultTypeDef",
    "CreateLoadBalancerTlsCertificateRequestRequestTypeDef",
    "CreateLoadBalancerTlsCertificateResultTypeDef",
    "CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef",
    "CreateRelationalDatabaseFromSnapshotResultTypeDef",
    "CreateRelationalDatabaseRequestRequestTypeDef",
    "CreateRelationalDatabaseResultTypeDef",
    "CreateRelationalDatabaseSnapshotRequestRequestTypeDef",
    "CreateRelationalDatabaseSnapshotResultTypeDef",
    "DeleteAlarmRequestRequestTypeDef",
    "DeleteAlarmResultTypeDef",
    "DeleteAutoSnapshotRequestRequestTypeDef",
    "DeleteAutoSnapshotResultTypeDef",
    "DeleteBucketAccessKeyRequestRequestTypeDef",
    "DeleteBucketAccessKeyResultTypeDef",
    "DeleteBucketRequestRequestTypeDef",
    "DeleteBucketResultTypeDef",
    "DeleteCertificateRequestRequestTypeDef",
    "DeleteCertificateResultTypeDef",
    "DeleteContactMethodRequestRequestTypeDef",
    "DeleteContactMethodResultTypeDef",
    "DeleteContainerImageRequestRequestTypeDef",
    "DeleteContainerServiceRequestRequestTypeDef",
    "DeleteDiskRequestRequestTypeDef",
    "DeleteDiskResultTypeDef",
    "DeleteDiskSnapshotRequestRequestTypeDef",
    "DeleteDiskSnapshotResultTypeDef",
    "DeleteDistributionRequestRequestTypeDef",
    "DeleteDistributionResultTypeDef",
    "DeleteDomainEntryRequestRequestTypeDef",
    "DeleteDomainEntryResultTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResultTypeDef",
    "DeleteInstanceRequestRequestTypeDef",
    "DeleteInstanceResultTypeDef",
    "DeleteInstanceSnapshotRequestRequestTypeDef",
    "DeleteInstanceSnapshotResultTypeDef",
    "DeleteKeyPairRequestRequestTypeDef",
    "DeleteKeyPairResultTypeDef",
    "DeleteKnownHostKeysRequestRequestTypeDef",
    "DeleteKnownHostKeysResultTypeDef",
    "DeleteLoadBalancerRequestRequestTypeDef",
    "DeleteLoadBalancerResultTypeDef",
    "DeleteLoadBalancerTlsCertificateRequestRequestTypeDef",
    "DeleteLoadBalancerTlsCertificateResultTypeDef",
    "DeleteRelationalDatabaseRequestRequestTypeDef",
    "DeleteRelationalDatabaseResultTypeDef",
    "DeleteRelationalDatabaseSnapshotRequestRequestTypeDef",
    "DeleteRelationalDatabaseSnapshotResultTypeDef",
    "DestinationInfoTypeDef",
    "DetachCertificateFromDistributionRequestRequestTypeDef",
    "DetachCertificateFromDistributionResultTypeDef",
    "DetachDiskRequestRequestTypeDef",
    "DetachDiskResultTypeDef",
    "DetachInstancesFromLoadBalancerRequestRequestTypeDef",
    "DetachInstancesFromLoadBalancerResultTypeDef",
    "DetachStaticIpRequestRequestTypeDef",
    "DetachStaticIpResultTypeDef",
    "DisableAddOnRequestRequestTypeDef",
    "DisableAddOnResultTypeDef",
    "DiskInfoTypeDef",
    "DiskMapTypeDef",
    "DiskSnapshotInfoTypeDef",
    "DiskSnapshotTypeDef",
    "DiskTypeDef",
    "DistributionBundleTypeDef",
    "DomainEntryTypeDef",
    "DomainTypeDef",
    "DomainValidationRecordTypeDef",
    "DownloadDefaultKeyPairResultTypeDef",
    "EnableAddOnRequestRequestTypeDef",
    "EnableAddOnResultTypeDef",
    "EndpointRequestTypeDef",
    "ExportSnapshotRecordSourceInfoTypeDef",
    "ExportSnapshotRecordTypeDef",
    "ExportSnapshotRequestRequestTypeDef",
    "ExportSnapshotResultTypeDef",
    "GetActiveNamesRequestRequestTypeDef",
    "GetActiveNamesResultTypeDef",
    "GetAlarmsRequestRequestTypeDef",
    "GetAlarmsResultTypeDef",
    "GetAutoSnapshotsRequestRequestTypeDef",
    "GetAutoSnapshotsResultTypeDef",
    "GetBlueprintsRequestRequestTypeDef",
    "GetBlueprintsResultTypeDef",
    "GetBucketAccessKeysRequestRequestTypeDef",
    "GetBucketAccessKeysResultTypeDef",
    "GetBucketBundlesRequestRequestTypeDef",
    "GetBucketBundlesResultTypeDef",
    "GetBucketMetricDataRequestRequestTypeDef",
    "GetBucketMetricDataResultTypeDef",
    "GetBucketsRequestRequestTypeDef",
    "GetBucketsResultTypeDef",
    "GetBundlesRequestRequestTypeDef",
    "GetBundlesResultTypeDef",
    "GetCertificatesRequestRequestTypeDef",
    "GetCertificatesResultTypeDef",
    "GetCloudFormationStackRecordsRequestRequestTypeDef",
    "GetCloudFormationStackRecordsResultTypeDef",
    "GetContactMethodsRequestRequestTypeDef",
    "GetContactMethodsResultTypeDef",
    "GetContainerAPIMetadataResultTypeDef",
    "GetContainerImagesRequestRequestTypeDef",
    "GetContainerImagesResultTypeDef",
    "GetContainerLogRequestRequestTypeDef",
    "GetContainerLogResultTypeDef",
    "GetContainerServiceDeploymentsRequestRequestTypeDef",
    "GetContainerServiceDeploymentsResultTypeDef",
    "GetContainerServiceMetricDataRequestRequestTypeDef",
    "GetContainerServiceMetricDataResultTypeDef",
    "GetContainerServicePowersResultTypeDef",
    "GetContainerServicesRequestRequestTypeDef",
    "GetDiskRequestRequestTypeDef",
    "GetDiskResultTypeDef",
    "GetDiskSnapshotRequestRequestTypeDef",
    "GetDiskSnapshotResultTypeDef",
    "GetDiskSnapshotsRequestRequestTypeDef",
    "GetDiskSnapshotsResultTypeDef",
    "GetDisksRequestRequestTypeDef",
    "GetDisksResultTypeDef",
    "GetDistributionBundlesResultTypeDef",
    "GetDistributionLatestCacheResetRequestRequestTypeDef",
    "GetDistributionLatestCacheResetResultTypeDef",
    "GetDistributionMetricDataRequestRequestTypeDef",
    "GetDistributionMetricDataResultTypeDef",
    "GetDistributionsRequestRequestTypeDef",
    "GetDistributionsResultTypeDef",
    "GetDomainRequestRequestTypeDef",
    "GetDomainResultTypeDef",
    "GetDomainsRequestRequestTypeDef",
    "GetDomainsResultTypeDef",
    "GetExportSnapshotRecordsRequestRequestTypeDef",
    "GetExportSnapshotRecordsResultTypeDef",
    "GetInstanceAccessDetailsRequestRequestTypeDef",
    "GetInstanceAccessDetailsResultTypeDef",
    "GetInstanceMetricDataRequestRequestTypeDef",
    "GetInstanceMetricDataResultTypeDef",
    "GetInstancePortStatesRequestRequestTypeDef",
    "GetInstancePortStatesResultTypeDef",
    "GetInstanceRequestRequestTypeDef",
    "GetInstanceResultTypeDef",
    "GetInstanceSnapshotRequestRequestTypeDef",
    "GetInstanceSnapshotResultTypeDef",
    "GetInstanceSnapshotsRequestRequestTypeDef",
    "GetInstanceSnapshotsResultTypeDef",
    "GetInstanceStateRequestRequestTypeDef",
    "GetInstanceStateResultTypeDef",
    "GetInstancesRequestRequestTypeDef",
    "GetInstancesResultTypeDef",
    "GetKeyPairRequestRequestTypeDef",
    "GetKeyPairResultTypeDef",
    "GetKeyPairsRequestRequestTypeDef",
    "GetKeyPairsResultTypeDef",
    "GetLoadBalancerMetricDataRequestRequestTypeDef",
    "GetLoadBalancerMetricDataResultTypeDef",
    "GetLoadBalancerRequestRequestTypeDef",
    "GetLoadBalancerResultTypeDef",
    "GetLoadBalancerTlsCertificatesRequestRequestTypeDef",
    "GetLoadBalancerTlsCertificatesResultTypeDef",
    "GetLoadBalancersRequestRequestTypeDef",
    "GetLoadBalancersResultTypeDef",
    "GetOperationRequestRequestTypeDef",
    "GetOperationResultTypeDef",
    "GetOperationsForResourceRequestRequestTypeDef",
    "GetOperationsForResourceResultTypeDef",
    "GetOperationsRequestRequestTypeDef",
    "GetOperationsResultTypeDef",
    "GetRegionsRequestRequestTypeDef",
    "GetRegionsResultTypeDef",
    "GetRelationalDatabaseBlueprintsRequestRequestTypeDef",
    "GetRelationalDatabaseBlueprintsResultTypeDef",
    "GetRelationalDatabaseBundlesRequestRequestTypeDef",
    "GetRelationalDatabaseBundlesResultTypeDef",
    "GetRelationalDatabaseEventsRequestRequestTypeDef",
    "GetRelationalDatabaseEventsResultTypeDef",
    "GetRelationalDatabaseLogEventsRequestRequestTypeDef",
    "GetRelationalDatabaseLogEventsResultTypeDef",
    "GetRelationalDatabaseLogStreamsRequestRequestTypeDef",
    "GetRelationalDatabaseLogStreamsResultTypeDef",
    "GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef",
    "GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    "GetRelationalDatabaseMetricDataRequestRequestTypeDef",
    "GetRelationalDatabaseMetricDataResultTypeDef",
    "GetRelationalDatabaseParametersRequestRequestTypeDef",
    "GetRelationalDatabaseParametersResultTypeDef",
    "GetRelationalDatabaseRequestRequestTypeDef",
    "GetRelationalDatabaseResultTypeDef",
    "GetRelationalDatabaseSnapshotRequestRequestTypeDef",
    "GetRelationalDatabaseSnapshotResultTypeDef",
    "GetRelationalDatabaseSnapshotsRequestRequestTypeDef",
    "GetRelationalDatabaseSnapshotsResultTypeDef",
    "GetRelationalDatabasesRequestRequestTypeDef",
    "GetRelationalDatabasesResultTypeDef",
    "GetStaticIpRequestRequestTypeDef",
    "GetStaticIpResultTypeDef",
    "GetStaticIpsRequestRequestTypeDef",
    "GetStaticIpsResultTypeDef",
    "HeaderObjectTypeDef",
    "HostKeyAttributesTypeDef",
    "ImportKeyPairRequestRequestTypeDef",
    "ImportKeyPairResultTypeDef",
    "InputOriginTypeDef",
    "InstanceAccessDetailsTypeDef",
    "InstanceEntryTypeDef",
    "InstanceHardwareTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceNetworkingTypeDef",
    "InstancePortInfoTypeDef",
    "InstancePortStateTypeDef",
    "InstanceSnapshotInfoTypeDef",
    "InstanceSnapshotTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
    "IsVpcPeeredResultTypeDef",
    "KeyPairTypeDef",
    "LightsailDistributionTypeDef",
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    "LoadBalancerTlsCertificateSummaryTypeDef",
    "LoadBalancerTlsCertificateTypeDef",
    "LoadBalancerTypeDef",
    "LogEventTypeDef",
    "MetricDatapointTypeDef",
    "MonitoredResourceInfoTypeDef",
    "MonthlyTransferTypeDef",
    "OpenInstancePublicPortsRequestRequestTypeDef",
    "OpenInstancePublicPortsResultTypeDef",
    "OperationTypeDef",
    "OriginTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordDataTypeDef",
    "PeerVpcResultTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    "PortInfoTypeDef",
    "PutAlarmRequestRequestTypeDef",
    "PutAlarmResultTypeDef",
    "PutInstancePublicPortsRequestRequestTypeDef",
    "PutInstancePublicPortsResultTypeDef",
    "QueryStringObjectTypeDef",
    "RebootInstanceRequestRequestTypeDef",
    "RebootInstanceResultTypeDef",
    "RebootRelationalDatabaseRequestRequestTypeDef",
    "RebootRelationalDatabaseResultTypeDef",
    "RegionTypeDef",
    "RegisterContainerImageRequestRequestTypeDef",
    "RegisterContainerImageResultTypeDef",
    "RelationalDatabaseBlueprintTypeDef",
    "RelationalDatabaseBundleTypeDef",
    "RelationalDatabaseEndpointTypeDef",
    "RelationalDatabaseEventTypeDef",
    "RelationalDatabaseHardwareTypeDef",
    "RelationalDatabaseParameterTypeDef",
    "RelationalDatabaseSnapshotTypeDef",
    "RelationalDatabaseTypeDef",
    "ReleaseStaticIpRequestRequestTypeDef",
    "ReleaseStaticIpResultTypeDef",
    "RenewalSummaryTypeDef",
    "ResetDistributionCacheRequestRequestTypeDef",
    "ResetDistributionCacheResultTypeDef",
    "ResourceLocationTypeDef",
    "ResourceReceivingAccessTypeDef",
    "ResourceRecordTypeDef",
    "ResponseMetadataTypeDef",
    "SendContactMethodVerificationRequestRequestTypeDef",
    "SendContactMethodVerificationResultTypeDef",
    "SetIpAddressTypeRequestRequestTypeDef",
    "SetIpAddressTypeResultTypeDef",
    "SetResourceAccessForBucketRequestRequestTypeDef",
    "SetResourceAccessForBucketResultTypeDef",
    "StartInstanceRequestRequestTypeDef",
    "StartInstanceResultTypeDef",
    "StartRelationalDatabaseRequestRequestTypeDef",
    "StartRelationalDatabaseResultTypeDef",
    "StaticIpTypeDef",
    "StopInstanceRequestRequestTypeDef",
    "StopInstanceResultTypeDef",
    "StopRelationalDatabaseRequestRequestTypeDef",
    "StopRelationalDatabaseResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResultTypeDef",
    "TagTypeDef",
    "TestAlarmRequestRequestTypeDef",
    "TestAlarmResultTypeDef",
    "UnpeerVpcResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UntagResourceResultTypeDef",
    "UpdateBucketBundleRequestRequestTypeDef",
    "UpdateBucketBundleResultTypeDef",
    "UpdateBucketRequestRequestTypeDef",
    "UpdateBucketResultTypeDef",
    "UpdateContainerServiceRequestRequestTypeDef",
    "UpdateContainerServiceResultTypeDef",
    "UpdateDistributionBundleRequestRequestTypeDef",
    "UpdateDistributionBundleResultTypeDef",
    "UpdateDistributionRequestRequestTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateDomainEntryRequestRequestTypeDef",
    "UpdateDomainEntryResultTypeDef",
    "UpdateLoadBalancerAttributeRequestRequestTypeDef",
    "UpdateLoadBalancerAttributeResultTypeDef",
    "UpdateRelationalDatabaseParametersRequestRequestTypeDef",
    "UpdateRelationalDatabaseParametersResultTypeDef",
    "UpdateRelationalDatabaseRequestRequestTypeDef",
    "UpdateRelationalDatabaseResultTypeDef",
)

AccessKeyTypeDef = TypedDict(
    "AccessKeyTypeDef",
    {
        "accessKeyId": str,
        "secretAccessKey": str,
        "status": StatusTypeType,
        "createdAt": datetime,
    },
    total=False,
)

AccessRulesTypeDef = TypedDict(
    "AccessRulesTypeDef",
    {
        "getObject": AccessTypeType,
        "allowPublicOverrides": bool,
    },
    total=False,
)

_RequiredAddOnRequestTypeDef = TypedDict(
    "_RequiredAddOnRequestTypeDef",
    {
        "addOnType": Literal["AutoSnapshot"],
    },
)
_OptionalAddOnRequestTypeDef = TypedDict(
    "_OptionalAddOnRequestTypeDef",
    {
        "autoSnapshotAddOnRequest": "AutoSnapshotAddOnRequestTypeDef",
    },
    total=False,
)

class AddOnRequestTypeDef(_RequiredAddOnRequestTypeDef, _OptionalAddOnRequestTypeDef):
    pass

AddOnTypeDef = TypedDict(
    "AddOnTypeDef",
    {
        "name": str,
        "status": str,
        "snapshotTimeOfDay": str,
        "nextSnapshotTimeOfDay": str,
    },
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "supportCode": str,
        "monitoredResourceInfo": "MonitoredResourceInfoTypeDef",
        "comparisonOperator": ComparisonOperatorType,
        "evaluationPeriods": int,
        "period": int,
        "threshold": float,
        "datapointsToAlarm": int,
        "treatMissingData": TreatMissingDataType,
        "statistic": MetricStatisticType,
        "metricName": MetricNameType,
        "state": AlarmStateType,
        "unit": MetricUnitType,
        "contactProtocols": List[ContactProtocolType],
        "notificationTriggers": List[AlarmStateType],
        "notificationEnabled": bool,
    },
    total=False,
)

AllocateStaticIpRequestRequestTypeDef = TypedDict(
    "AllocateStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)

AllocateStaticIpResultTypeDef = TypedDict(
    "AllocateStaticIpResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachCertificateToDistributionRequestRequestTypeDef = TypedDict(
    "AttachCertificateToDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
        "certificateName": str,
    },
)

AttachCertificateToDistributionResultTypeDef = TypedDict(
    "AttachCertificateToDistributionResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachDiskRequestRequestTypeDef = TypedDict(
    "AttachDiskRequestRequestTypeDef",
    {
        "diskName": str,
        "instanceName": str,
        "diskPath": str,
    },
)

AttachDiskResultTypeDef = TypedDict(
    "AttachDiskResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachInstancesToLoadBalancerRequestRequestTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instanceNames": List[str],
    },
)

AttachInstancesToLoadBalancerResultTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
    },
)

AttachLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachStaticIpRequestRequestTypeDef = TypedDict(
    "AttachStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
        "instanceName": str,
    },
)

AttachStaticIpResultTypeDef = TypedDict(
    "AttachStaticIpResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachedDiskTypeDef = TypedDict(
    "AttachedDiskTypeDef",
    {
        "path": str,
        "sizeInGb": int,
    },
    total=False,
)

AutoSnapshotAddOnRequestTypeDef = TypedDict(
    "AutoSnapshotAddOnRequestTypeDef",
    {
        "snapshotTimeOfDay": str,
    },
    total=False,
)

AutoSnapshotDetailsTypeDef = TypedDict(
    "AutoSnapshotDetailsTypeDef",
    {
        "date": str,
        "createdAt": datetime,
        "status": AutoSnapshotStatusType,
        "fromAttachedDisks": List["AttachedDiskTypeDef"],
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "zoneName": str,
        "state": str,
    },
    total=False,
)

BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "blueprintId": str,
        "name": str,
        "group": str,
        "type": BlueprintTypeType,
        "description": str,
        "isActive": bool,
        "minPower": int,
        "version": str,
        "versionCode": str,
        "productUrl": str,
        "licenseUrl": str,
        "platform": InstancePlatformType,
    },
    total=False,
)

BucketBundleTypeDef = TypedDict(
    "BucketBundleTypeDef",
    {
        "bundleId": str,
        "name": str,
        "price": float,
        "storagePerMonthInGb": int,
        "transferPerMonthInGb": int,
        "isActive": bool,
    },
    total=False,
)

BucketStateTypeDef = TypedDict(
    "BucketStateTypeDef",
    {
        "code": str,
        "message": str,
    },
    total=False,
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "resourceType": str,
        "accessRules": "AccessRulesTypeDef",
        "arn": str,
        "bundleId": str,
        "createdAt": datetime,
        "url": str,
        "location": "ResourceLocationTypeDef",
        "name": str,
        "supportCode": str,
        "tags": List["TagTypeDef"],
        "objectVersioning": str,
        "ableToUpdateBundle": bool,
        "readonlyAccessAccounts": List[str],
        "resourcesReceivingAccess": List["ResourceReceivingAccessTypeDef"],
        "state": "BucketStateTypeDef",
    },
    total=False,
)

BundleTypeDef = TypedDict(
    "BundleTypeDef",
    {
        "price": float,
        "cpuCount": int,
        "diskSizeInGb": int,
        "bundleId": str,
        "instanceType": str,
        "isActive": bool,
        "name": str,
        "power": int,
        "ramSizeInGb": float,
        "transferPerMonthInGb": int,
        "supportedPlatforms": List[InstancePlatformType],
    },
    total=False,
)

CacheBehaviorPerPathTypeDef = TypedDict(
    "CacheBehaviorPerPathTypeDef",
    {
        "path": str,
        "behavior": BehaviorEnumType,
    },
    total=False,
)

CacheBehaviorTypeDef = TypedDict(
    "CacheBehaviorTypeDef",
    {
        "behavior": BehaviorEnumType,
    },
    total=False,
)

CacheSettingsTypeDef = TypedDict(
    "CacheSettingsTypeDef",
    {
        "defaultTTL": int,
        "minimumTTL": int,
        "maximumTTL": int,
        "allowedHTTPMethods": str,
        "cachedHTTPMethods": str,
        "forwardedCookies": "CookieObjectTypeDef",
        "forwardedHeaders": "HeaderObjectTypeDef",
        "forwardedQueryStrings": "QueryStringObjectTypeDef",
    },
    total=False,
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "certificateArn": str,
        "certificateName": str,
        "domainName": str,
        "certificateDetail": "CertificateTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "arn": str,
        "name": str,
        "domainName": str,
        "status": CertificateStatusType,
        "serialNumber": str,
        "subjectAlternativeNames": List[str],
        "domainValidationRecords": List["DomainValidationRecordTypeDef"],
        "requestFailureReason": str,
        "inUseResourceCount": int,
        "keyAlgorithm": str,
        "createdAt": datetime,
        "issuedAt": datetime,
        "issuerCA": str,
        "notBefore": datetime,
        "notAfter": datetime,
        "eligibleToRenew": str,
        "renewalSummary": "RenewalSummaryTypeDef",
        "revokedAt": datetime,
        "revocationReason": str,
        "tags": List["TagTypeDef"],
        "supportCode": str,
    },
    total=False,
)

CloseInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "CloseInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfo": "PortInfoTypeDef",
        "instanceName": str,
    },
)

CloseInstancePublicPortsResultTypeDef = TypedDict(
    "CloseInstancePublicPortsResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CloudFormationStackRecordSourceInfoTypeDef = TypedDict(
    "CloudFormationStackRecordSourceInfoTypeDef",
    {
        "resourceType": Literal["ExportSnapshotRecord"],
        "name": str,
        "arn": str,
    },
    total=False,
)

CloudFormationStackRecordTypeDef = TypedDict(
    "CloudFormationStackRecordTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "state": RecordStateType,
        "sourceInfo": List["CloudFormationStackRecordSourceInfoTypeDef"],
        "destinationInfo": "DestinationInfoTypeDef",
    },
    total=False,
)

ContactMethodTypeDef = TypedDict(
    "ContactMethodTypeDef",
    {
        "contactEndpoint": str,
        "status": ContactMethodStatusType,
        "protocol": ContactProtocolType,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "supportCode": str,
    },
    total=False,
)

ContainerImageTypeDef = TypedDict(
    "ContainerImageTypeDef",
    {
        "image": str,
        "digest": str,
        "createdAt": datetime,
    },
    total=False,
)

ContainerServiceDeploymentRequestTypeDef = TypedDict(
    "ContainerServiceDeploymentRequestTypeDef",
    {
        "containers": Dict[str, "ContainerTypeDef"],
        "publicEndpoint": "EndpointRequestTypeDef",
    },
    total=False,
)

ContainerServiceDeploymentTypeDef = TypedDict(
    "ContainerServiceDeploymentTypeDef",
    {
        "version": int,
        "state": ContainerServiceDeploymentStateType,
        "containers": Dict[str, "ContainerTypeDef"],
        "publicEndpoint": "ContainerServiceEndpointTypeDef",
        "createdAt": datetime,
    },
    total=False,
)

ContainerServiceEndpointTypeDef = TypedDict(
    "ContainerServiceEndpointTypeDef",
    {
        "containerName": str,
        "containerPort": int,
        "healthCheck": "ContainerServiceHealthCheckConfigTypeDef",
    },
    total=False,
)

ContainerServiceHealthCheckConfigTypeDef = TypedDict(
    "ContainerServiceHealthCheckConfigTypeDef",
    {
        "healthyThreshold": int,
        "unhealthyThreshold": int,
        "timeoutSeconds": int,
        "intervalSeconds": int,
        "path": str,
        "successCodes": str,
    },
    total=False,
)

ContainerServiceLogEventTypeDef = TypedDict(
    "ContainerServiceLogEventTypeDef",
    {
        "createdAt": datetime,
        "message": str,
    },
    total=False,
)

ContainerServicePowerTypeDef = TypedDict(
    "ContainerServicePowerTypeDef",
    {
        "powerId": str,
        "price": float,
        "cpuCount": float,
        "ramSizeInGb": float,
        "name": str,
        "isActive": bool,
    },
    total=False,
)

ContainerServiceRegistryLoginTypeDef = TypedDict(
    "ContainerServiceRegistryLoginTypeDef",
    {
        "username": str,
        "password": str,
        "expiresAt": datetime,
        "registry": str,
    },
    total=False,
)

ContainerServiceStateDetailTypeDef = TypedDict(
    "ContainerServiceStateDetailTypeDef",
    {
        "code": ContainerServiceStateDetailCodeType,
        "message": str,
    },
    total=False,
)

ContainerServiceTypeDef = TypedDict(
    "ContainerServiceTypeDef",
    {
        "containerServiceName": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "power": ContainerServicePowerNameType,
        "powerId": str,
        "state": ContainerServiceStateType,
        "stateDetail": "ContainerServiceStateDetailTypeDef",
        "scale": int,
        "currentDeployment": "ContainerServiceDeploymentTypeDef",
        "nextDeployment": "ContainerServiceDeploymentTypeDef",
        "isDisabled": bool,
        "principalArn": str,
        "privateDomainName": str,
        "publicDomainNames": Dict[str, List[str]],
        "url": str,
    },
    total=False,
)

ContainerServicesListResultTypeDef = TypedDict(
    "ContainerServicesListResultTypeDef",
    {
        "containerServices": List["ContainerServiceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "image": str,
        "command": List[str],
        "environment": Dict[str, str],
        "ports": Dict[str, ContainerServiceProtocolType],
    },
    total=False,
)

CookieObjectTypeDef = TypedDict(
    "CookieObjectTypeDef",
    {
        "option": ForwardValuesType,
        "cookiesAllowList": List[str],
    },
    total=False,
)

_RequiredCopySnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCopySnapshotRequestRequestTypeDef",
    {
        "targetSnapshotName": str,
        "sourceRegion": RegionNameType,
    },
)
_OptionalCopySnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCopySnapshotRequestRequestTypeDef",
    {
        "sourceSnapshotName": str,
        "sourceResourceName": str,
        "restoreDate": str,
        "useLatestRestorableAutoSnapshot": bool,
    },
    total=False,
)

class CopySnapshotRequestRequestTypeDef(
    _RequiredCopySnapshotRequestRequestTypeDef, _OptionalCopySnapshotRequestRequestTypeDef
):
    pass

CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBucketAccessKeyRequestRequestTypeDef = TypedDict(
    "CreateBucketAccessKeyRequestRequestTypeDef",
    {
        "bucketName": str,
    },
)

CreateBucketAccessKeyResultTypeDef = TypedDict(
    "CreateBucketAccessKeyResultTypeDef",
    {
        "accessKey": "AccessKeyTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateBucketRequestRequestTypeDef = TypedDict(
    "_RequiredCreateBucketRequestRequestTypeDef",
    {
        "bucketName": str,
        "bundleId": str,
    },
)
_OptionalCreateBucketRequestRequestTypeDef = TypedDict(
    "_OptionalCreateBucketRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "enableObjectVersioning": bool,
    },
    total=False,
)

class CreateBucketRequestRequestTypeDef(
    _RequiredCreateBucketRequestRequestTypeDef, _OptionalCreateBucketRequestRequestTypeDef
):
    pass

CreateBucketResultTypeDef = TypedDict(
    "CreateBucketResultTypeDef",
    {
        "bucket": "BucketTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCertificateRequestRequestTypeDef",
    {
        "certificateName": str,
        "domainName": str,
    },
)
_OptionalCreateCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCertificateRequestRequestTypeDef",
    {
        "subjectAlternativeNames": List[str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCertificateRequestRequestTypeDef(
    _RequiredCreateCertificateRequestRequestTypeDef, _OptionalCreateCertificateRequestRequestTypeDef
):
    pass

CreateCertificateResultTypeDef = TypedDict(
    "CreateCertificateResultTypeDef",
    {
        "certificate": "CertificateSummaryTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCloudFormationStackRequestRequestTypeDef = TypedDict(
    "CreateCloudFormationStackRequestRequestTypeDef",
    {
        "instances": List["InstanceEntryTypeDef"],
    },
)

CreateCloudFormationStackResultTypeDef = TypedDict(
    "CreateCloudFormationStackResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContactMethodRequestRequestTypeDef = TypedDict(
    "CreateContactMethodRequestRequestTypeDef",
    {
        "protocol": ContactProtocolType,
        "contactEndpoint": str,
    },
)

CreateContactMethodResultTypeDef = TypedDict(
    "CreateContactMethodResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContainerServiceDeploymentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContainerServiceDeploymentRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalCreateContainerServiceDeploymentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContainerServiceDeploymentRequestRequestTypeDef",
    {
        "containers": Dict[str, "ContainerTypeDef"],
        "publicEndpoint": "EndpointRequestTypeDef",
    },
    total=False,
)

class CreateContainerServiceDeploymentRequestRequestTypeDef(
    _RequiredCreateContainerServiceDeploymentRequestRequestTypeDef,
    _OptionalCreateContainerServiceDeploymentRequestRequestTypeDef,
):
    pass

CreateContainerServiceDeploymentResultTypeDef = TypedDict(
    "CreateContainerServiceDeploymentResultTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContainerServiceRegistryLoginResultTypeDef = TypedDict(
    "CreateContainerServiceRegistryLoginResultTypeDef",
    {
        "registryLogin": "ContainerServiceRegistryLoginTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateContainerServiceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
        "power": ContainerServicePowerNameType,
        "scale": int,
    },
)
_OptionalCreateContainerServiceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateContainerServiceRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "publicDomainNames": Dict[str, List[str]],
        "deployment": "ContainerServiceDeploymentRequestTypeDef",
    },
    total=False,
)

class CreateContainerServiceRequestRequestTypeDef(
    _RequiredCreateContainerServiceRequestRequestTypeDef,
    _OptionalCreateContainerServiceRequestRequestTypeDef,
):
    pass

CreateContainerServiceResultTypeDef = TypedDict(
    "CreateContainerServiceResultTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDiskFromSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDiskFromSnapshotRequestRequestTypeDef",
    {
        "diskName": str,
        "availabilityZone": str,
        "sizeInGb": int,
    },
)
_OptionalCreateDiskFromSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDiskFromSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnRequestTypeDef"],
        "sourceDiskName": str,
        "restoreDate": str,
        "useLatestRestorableAutoSnapshot": bool,
    },
    total=False,
)

class CreateDiskFromSnapshotRequestRequestTypeDef(
    _RequiredCreateDiskFromSnapshotRequestRequestTypeDef,
    _OptionalCreateDiskFromSnapshotRequestRequestTypeDef,
):
    pass

CreateDiskFromSnapshotResultTypeDef = TypedDict(
    "CreateDiskFromSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDiskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDiskRequestRequestTypeDef",
    {
        "diskName": str,
        "availabilityZone": str,
        "sizeInGb": int,
    },
)
_OptionalCreateDiskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDiskRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnRequestTypeDef"],
    },
    total=False,
)

class CreateDiskRequestRequestTypeDef(
    _RequiredCreateDiskRequestRequestTypeDef, _OptionalCreateDiskRequestRequestTypeDef
):
    pass

CreateDiskResultTypeDef = TypedDict(
    "CreateDiskResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDiskSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)
_OptionalCreateDiskSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDiskSnapshotRequestRequestTypeDef",
    {
        "diskName": str,
        "instanceName": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDiskSnapshotRequestRequestTypeDef(
    _RequiredCreateDiskSnapshotRequestRequestTypeDef,
    _OptionalCreateDiskSnapshotRequestRequestTypeDef,
):
    pass

CreateDiskSnapshotResultTypeDef = TypedDict(
    "CreateDiskSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDistributionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
        "origin": "InputOriginTypeDef",
        "defaultCacheBehavior": "CacheBehaviorTypeDef",
        "bundleId": str,
    },
)
_OptionalCreateDistributionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDistributionRequestRequestTypeDef",
    {
        "cacheBehaviorSettings": "CacheSettingsTypeDef",
        "cacheBehaviors": List["CacheBehaviorPerPathTypeDef"],
        "ipAddressType": IpAddressTypeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDistributionRequestRequestTypeDef(
    _RequiredCreateDistributionRequestRequestTypeDef,
    _OptionalCreateDistributionRequestRequestTypeDef,
):
    pass

CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {
        "distribution": "LightsailDistributionTypeDef",
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainEntryRequestRequestTypeDef = TypedDict(
    "CreateDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

CreateDomainEntryResultTypeDef = TypedDict(
    "CreateDomainEntryResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
_OptionalCreateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDomainRequestRequestTypeDef(
    _RequiredCreateDomainRequestRequestTypeDef, _OptionalCreateDomainRequestRequestTypeDef
):
    pass

CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
        "instanceName": str,
    },
)
_OptionalCreateInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceSnapshotRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateInstanceSnapshotRequestRequestTypeDef(
    _RequiredCreateInstanceSnapshotRequestRequestTypeDef,
    _OptionalCreateInstanceSnapshotRequestRequestTypeDef,
):
    pass

CreateInstanceSnapshotResultTypeDef = TypedDict(
    "CreateInstanceSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstancesFromSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstancesFromSnapshotRequestRequestTypeDef",
    {
        "instanceNames": List[str],
        "availabilityZone": str,
        "bundleId": str,
    },
)
_OptionalCreateInstancesFromSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstancesFromSnapshotRequestRequestTypeDef",
    {
        "attachedDiskMapping": Dict[str, List["DiskMapTypeDef"]],
        "instanceSnapshotName": str,
        "userData": str,
        "keyPairName": str,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnRequestTypeDef"],
        "ipAddressType": IpAddressTypeType,
        "sourceInstanceName": str,
        "restoreDate": str,
        "useLatestRestorableAutoSnapshot": bool,
    },
    total=False,
)

class CreateInstancesFromSnapshotRequestRequestTypeDef(
    _RequiredCreateInstancesFromSnapshotRequestRequestTypeDef,
    _OptionalCreateInstancesFromSnapshotRequestRequestTypeDef,
):
    pass

CreateInstancesFromSnapshotResultTypeDef = TypedDict(
    "CreateInstancesFromSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstancesRequestRequestTypeDef",
    {
        "instanceNames": List[str],
        "availabilityZone": str,
        "blueprintId": str,
        "bundleId": str,
    },
)
_OptionalCreateInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstancesRequestRequestTypeDef",
    {
        "customImageName": str,
        "userData": str,
        "keyPairName": str,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnRequestTypeDef"],
        "ipAddressType": IpAddressTypeType,
    },
    total=False,
)

class CreateInstancesRequestRequestTypeDef(
    _RequiredCreateInstancesRequestRequestTypeDef, _OptionalCreateInstancesRequestRequestTypeDef
):
    pass

CreateInstancesResultTypeDef = TypedDict(
    "CreateInstancesResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKeyPairRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
    },
)
_OptionalCreateKeyPairRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKeyPairRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateKeyPairRequestRequestTypeDef(
    _RequiredCreateKeyPairRequestRequestTypeDef, _OptionalCreateKeyPairRequestRequestTypeDef
):
    pass

CreateKeyPairResultTypeDef = TypedDict(
    "CreateKeyPairResultTypeDef",
    {
        "keyPair": "KeyPairTypeDef",
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoadBalancerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instancePort": int,
    },
)
_OptionalCreateLoadBalancerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerRequestRequestTypeDef",
    {
        "healthCheckPath": str,
        "certificateName": str,
        "certificateDomainName": str,
        "certificateAlternativeNames": List[str],
        "tags": List["TagTypeDef"],
        "ipAddressType": IpAddressTypeType,
    },
    total=False,
)

class CreateLoadBalancerRequestRequestTypeDef(
    _RequiredCreateLoadBalancerRequestRequestTypeDef,
    _OptionalCreateLoadBalancerRequestRequestTypeDef,
):
    pass

CreateLoadBalancerResultTypeDef = TypedDict(
    "CreateLoadBalancerResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
        "certificateDomainName": str,
    },
)
_OptionalCreateLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "certificateAlternativeNames": List[str],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateLoadBalancerTlsCertificateRequestRequestTypeDef(
    _RequiredCreateLoadBalancerTlsCertificateRequestRequestTypeDef,
    _OptionalCreateLoadBalancerTlsCertificateRequestRequestTypeDef,
):
    pass

CreateLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "CreateLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRelationalDatabaseFromSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRelationalDatabaseFromSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalCreateRelationalDatabaseFromSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRelationalDatabaseFromSnapshotRequestRequestTypeDef",
    {
        "availabilityZone": str,
        "publiclyAccessible": bool,
        "relationalDatabaseSnapshotName": str,
        "relationalDatabaseBundleId": str,
        "sourceRelationalDatabaseName": str,
        "restoreTime": Union[datetime, str],
        "useLatestRestorableTime": bool,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef(
    _RequiredCreateRelationalDatabaseFromSnapshotRequestRequestTypeDef,
    _OptionalCreateRelationalDatabaseFromSnapshotRequestRequestTypeDef,
):
    pass

CreateRelationalDatabaseFromSnapshotResultTypeDef = TypedDict(
    "CreateRelationalDatabaseFromSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "masterUsername": str,
    },
)
_OptionalCreateRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRelationalDatabaseRequestRequestTypeDef",
    {
        "availabilityZone": str,
        "masterUserPassword": str,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRelationalDatabaseRequestRequestTypeDef(
    _RequiredCreateRelationalDatabaseRequestRequestTypeDef,
    _OptionalCreateRelationalDatabaseRequestRequestTypeDef,
):
    pass

CreateRelationalDatabaseResultTypeDef = TypedDict(
    "CreateRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "relationalDatabaseSnapshotName": str,
    },
)
_OptionalCreateRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRelationalDatabaseSnapshotRequestRequestTypeDef(
    _RequiredCreateRelationalDatabaseSnapshotRequestRequestTypeDef,
    _OptionalCreateRelationalDatabaseSnapshotRequestRequestTypeDef,
):
    pass

CreateRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "CreateRelationalDatabaseSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAlarmRequestRequestTypeDef = TypedDict(
    "DeleteAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
    },
)

DeleteAlarmResultTypeDef = TypedDict(
    "DeleteAlarmResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAutoSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteAutoSnapshotRequestRequestTypeDef",
    {
        "resourceName": str,
        "date": str,
    },
)

DeleteAutoSnapshotResultTypeDef = TypedDict(
    "DeleteAutoSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBucketAccessKeyRequestRequestTypeDef = TypedDict(
    "DeleteBucketAccessKeyRequestRequestTypeDef",
    {
        "bucketName": str,
        "accessKeyId": str,
    },
)

DeleteBucketAccessKeyResultTypeDef = TypedDict(
    "DeleteBucketAccessKeyResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteBucketRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteBucketRequestRequestTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalDeleteBucketRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteBucketRequestRequestTypeDef",
    {
        "forceDelete": bool,
    },
    total=False,
)

class DeleteBucketRequestRequestTypeDef(
    _RequiredDeleteBucketRequestRequestTypeDef, _OptionalDeleteBucketRequestRequestTypeDef
):
    pass

DeleteBucketResultTypeDef = TypedDict(
    "DeleteBucketResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCertificateRequestRequestTypeDef = TypedDict(
    "DeleteCertificateRequestRequestTypeDef",
    {
        "certificateName": str,
    },
)

DeleteCertificateResultTypeDef = TypedDict(
    "DeleteCertificateResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContactMethodRequestRequestTypeDef = TypedDict(
    "DeleteContactMethodRequestRequestTypeDef",
    {
        "protocol": ContactProtocolType,
    },
)

DeleteContactMethodResultTypeDef = TypedDict(
    "DeleteContactMethodResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteContainerImageRequestRequestTypeDef = TypedDict(
    "DeleteContainerImageRequestRequestTypeDef",
    {
        "serviceName": str,
        "image": str,
    },
)

DeleteContainerServiceRequestRequestTypeDef = TypedDict(
    "DeleteContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)

_RequiredDeleteDiskRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDiskRequestRequestTypeDef",
    {
        "diskName": str,
    },
)
_OptionalDeleteDiskRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDiskRequestRequestTypeDef",
    {
        "forceDeleteAddOns": bool,
    },
    total=False,
)

class DeleteDiskRequestRequestTypeDef(
    _RequiredDeleteDiskRequestRequestTypeDef, _OptionalDeleteDiskRequestRequestTypeDef
):
    pass

DeleteDiskResultTypeDef = TypedDict(
    "DeleteDiskResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDiskSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)

DeleteDiskSnapshotResultTypeDef = TypedDict(
    "DeleteDiskSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDistributionRequestRequestTypeDef = TypedDict(
    "DeleteDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
    },
    total=False,
)

DeleteDistributionResultTypeDef = TypedDict(
    "DeleteDistributionResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainEntryRequestRequestTypeDef = TypedDict(
    "DeleteDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

DeleteDomainEntryResultTypeDef = TypedDict(
    "DeleteDomainEntryResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
_OptionalDeleteInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteInstanceRequestRequestTypeDef",
    {
        "forceDeleteAddOns": bool,
    },
    total=False,
)

class DeleteInstanceRequestRequestTypeDef(
    _RequiredDeleteInstanceRequestRequestTypeDef, _OptionalDeleteInstanceRequestRequestTypeDef
):
    pass

DeleteInstanceResultTypeDef = TypedDict(
    "DeleteInstanceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
    },
)

DeleteInstanceSnapshotResultTypeDef = TypedDict(
    "DeleteInstanceSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeyPairRequestRequestTypeDef = TypedDict(
    "DeleteKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
    },
)

DeleteKeyPairResultTypeDef = TypedDict(
    "DeleteKeyPairResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKnownHostKeysRequestRequestTypeDef = TypedDict(
    "DeleteKnownHostKeysRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

DeleteKnownHostKeysResultTypeDef = TypedDict(
    "DeleteKnownHostKeysResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLoadBalancerRequestRequestTypeDef = TypedDict(
    "DeleteLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

DeleteLoadBalancerResultTypeDef = TypedDict(
    "DeleteLoadBalancerResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "certificateName": str,
    },
)
_OptionalDeleteLoadBalancerTlsCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLoadBalancerTlsCertificateRequestRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)

class DeleteLoadBalancerTlsCertificateRequestRequestTypeDef(
    _RequiredDeleteLoadBalancerTlsCertificateRequestRequestTypeDef,
    _OptionalDeleteLoadBalancerTlsCertificateRequestRequestTypeDef,
):
    pass

DeleteLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "DeleteLoadBalancerTlsCertificateResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalDeleteRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRelationalDatabaseRequestRequestTypeDef",
    {
        "skipFinalSnapshot": bool,
        "finalRelationalDatabaseSnapshotName": str,
    },
    total=False,
)

class DeleteRelationalDatabaseRequestRequestTypeDef(
    _RequiredDeleteRelationalDatabaseRequestRequestTypeDef,
    _OptionalDeleteRelationalDatabaseRequestRequestTypeDef,
):
    pass

DeleteRelationalDatabaseResultTypeDef = TypedDict(
    "DeleteRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
)

DeleteRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationInfoTypeDef = TypedDict(
    "DestinationInfoTypeDef",
    {
        "id": str,
        "service": str,
    },
    total=False,
)

DetachCertificateFromDistributionRequestRequestTypeDef = TypedDict(
    "DetachCertificateFromDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
    },
)

DetachCertificateFromDistributionResultTypeDef = TypedDict(
    "DetachCertificateFromDistributionResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachDiskRequestRequestTypeDef = TypedDict(
    "DetachDiskRequestRequestTypeDef",
    {
        "diskName": str,
    },
)

DetachDiskResultTypeDef = TypedDict(
    "DetachDiskResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachInstancesFromLoadBalancerRequestRequestTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "instanceNames": List[str],
    },
)

DetachInstancesFromLoadBalancerResultTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachStaticIpRequestRequestTypeDef = TypedDict(
    "DetachStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)

DetachStaticIpResultTypeDef = TypedDict(
    "DetachStaticIpResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableAddOnRequestRequestTypeDef = TypedDict(
    "DisableAddOnRequestRequestTypeDef",
    {
        "addOnType": Literal["AutoSnapshot"],
        "resourceName": str,
    },
)

DisableAddOnResultTypeDef = TypedDict(
    "DisableAddOnResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {
        "name": str,
        "path": str,
        "sizeInGb": int,
        "isSystemDisk": bool,
    },
    total=False,
)

DiskMapTypeDef = TypedDict(
    "DiskMapTypeDef",
    {
        "originalDiskPath": str,
        "newDiskName": str,
    },
    total=False,
)

DiskSnapshotInfoTypeDef = TypedDict(
    "DiskSnapshotInfoTypeDef",
    {
        "sizeInGb": int,
    },
    total=False,
)

DiskSnapshotTypeDef = TypedDict(
    "DiskSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "sizeInGb": int,
        "state": DiskSnapshotStateType,
        "progress": str,
        "fromDiskName": str,
        "fromDiskArn": str,
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "isFromAutoSnapshot": bool,
    },
    total=False,
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnTypeDef"],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": DiskStateType,
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)

DistributionBundleTypeDef = TypedDict(
    "DistributionBundleTypeDef",
    {
        "bundleId": str,
        "name": str,
        "price": float,
        "transferPerMonthInGb": int,
        "isActive": bool,
    },
    total=False,
)

DomainEntryTypeDef = TypedDict(
    "DomainEntryTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "domainEntries": List["DomainEntryTypeDef"],
    },
    total=False,
)

DomainValidationRecordTypeDef = TypedDict(
    "DomainValidationRecordTypeDef",
    {
        "domainName": str,
        "resourceRecord": "ResourceRecordTypeDef",
    },
    total=False,
)

DownloadDefaultKeyPairResultTypeDef = TypedDict(
    "DownloadDefaultKeyPairResultTypeDef",
    {
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableAddOnRequestRequestTypeDef = TypedDict(
    "EnableAddOnRequestRequestTypeDef",
    {
        "resourceName": str,
        "addOnRequest": "AddOnRequestTypeDef",
    },
)

EnableAddOnResultTypeDef = TypedDict(
    "EnableAddOnResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEndpointRequestTypeDef = TypedDict(
    "_RequiredEndpointRequestTypeDef",
    {
        "containerName": str,
        "containerPort": int,
    },
)
_OptionalEndpointRequestTypeDef = TypedDict(
    "_OptionalEndpointRequestTypeDef",
    {
        "healthCheck": "ContainerServiceHealthCheckConfigTypeDef",
    },
    total=False,
)

class EndpointRequestTypeDef(_RequiredEndpointRequestTypeDef, _OptionalEndpointRequestTypeDef):
    pass

ExportSnapshotRecordSourceInfoTypeDef = TypedDict(
    "ExportSnapshotRecordSourceInfoTypeDef",
    {
        "resourceType": ExportSnapshotRecordSourceTypeType,
        "createdAt": datetime,
        "name": str,
        "arn": str,
        "fromResourceName": str,
        "fromResourceArn": str,
        "instanceSnapshotInfo": "InstanceSnapshotInfoTypeDef",
        "diskSnapshotInfo": "DiskSnapshotInfoTypeDef",
    },
    total=False,
)

ExportSnapshotRecordTypeDef = TypedDict(
    "ExportSnapshotRecordTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "state": RecordStateType,
        "sourceInfo": "ExportSnapshotRecordSourceInfoTypeDef",
        "destinationInfo": "DestinationInfoTypeDef",
    },
    total=False,
)

ExportSnapshotRequestRequestTypeDef = TypedDict(
    "ExportSnapshotRequestRequestTypeDef",
    {
        "sourceSnapshotName": str,
    },
)

ExportSnapshotResultTypeDef = TypedDict(
    "ExportSnapshotResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetActiveNamesRequestRequestTypeDef = TypedDict(
    "GetActiveNamesRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetActiveNamesResultTypeDef = TypedDict(
    "GetActiveNamesResultTypeDef",
    {
        "activeNames": List[str],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAlarmsRequestRequestTypeDef = TypedDict(
    "GetAlarmsRequestRequestTypeDef",
    {
        "alarmName": str,
        "pageToken": str,
        "monitoredResourceName": str,
    },
    total=False,
)

GetAlarmsResultTypeDef = TypedDict(
    "GetAlarmsResultTypeDef",
    {
        "alarms": List["AlarmTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAutoSnapshotsRequestRequestTypeDef = TypedDict(
    "GetAutoSnapshotsRequestRequestTypeDef",
    {
        "resourceName": str,
    },
)

GetAutoSnapshotsResultTypeDef = TypedDict(
    "GetAutoSnapshotsResultTypeDef",
    {
        "resourceName": str,
        "resourceType": ResourceTypeType,
        "autoSnapshots": List["AutoSnapshotDetailsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlueprintsRequestRequestTypeDef = TypedDict(
    "GetBlueprintsRequestRequestTypeDef",
    {
        "includeInactive": bool,
        "pageToken": str,
    },
    total=False,
)

GetBlueprintsResultTypeDef = TypedDict(
    "GetBlueprintsResultTypeDef",
    {
        "blueprints": List["BlueprintTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketAccessKeysRequestRequestTypeDef = TypedDict(
    "GetBucketAccessKeysRequestRequestTypeDef",
    {
        "bucketName": str,
    },
)

GetBucketAccessKeysResultTypeDef = TypedDict(
    "GetBucketAccessKeysResultTypeDef",
    {
        "accessKeys": List["AccessKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketBundlesRequestRequestTypeDef = TypedDict(
    "GetBucketBundlesRequestRequestTypeDef",
    {
        "includeInactive": bool,
    },
    total=False,
)

GetBucketBundlesResultTypeDef = TypedDict(
    "GetBucketBundlesResultTypeDef",
    {
        "bundles": List["BucketBundleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketMetricDataRequestRequestTypeDef = TypedDict(
    "GetBucketMetricDataRequestRequestTypeDef",
    {
        "bucketName": str,
        "metricName": BucketMetricNameType,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "period": int,
        "statistics": List[MetricStatisticType],
        "unit": MetricUnitType,
    },
)

GetBucketMetricDataResultTypeDef = TypedDict(
    "GetBucketMetricDataResultTypeDef",
    {
        "metricName": BucketMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBucketsRequestRequestTypeDef = TypedDict(
    "GetBucketsRequestRequestTypeDef",
    {
        "bucketName": str,
        "pageToken": str,
        "includeConnectedResources": bool,
    },
    total=False,
)

GetBucketsResultTypeDef = TypedDict(
    "GetBucketsResultTypeDef",
    {
        "buckets": List["BucketTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBundlesRequestRequestTypeDef = TypedDict(
    "GetBundlesRequestRequestTypeDef",
    {
        "includeInactive": bool,
        "pageToken": str,
    },
    total=False,
)

GetBundlesResultTypeDef = TypedDict(
    "GetBundlesResultTypeDef",
    {
        "bundles": List["BundleTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCertificatesRequestRequestTypeDef = TypedDict(
    "GetCertificatesRequestRequestTypeDef",
    {
        "certificateStatuses": List[CertificateStatusType],
        "includeCertificateDetails": bool,
        "certificateName": str,
    },
    total=False,
)

GetCertificatesResultTypeDef = TypedDict(
    "GetCertificatesResultTypeDef",
    {
        "certificates": List["CertificateSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCloudFormationStackRecordsRequestRequestTypeDef = TypedDict(
    "GetCloudFormationStackRecordsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetCloudFormationStackRecordsResultTypeDef = TypedDict(
    "GetCloudFormationStackRecordsResultTypeDef",
    {
        "cloudFormationStackRecords": List["CloudFormationStackRecordTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactMethodsRequestRequestTypeDef = TypedDict(
    "GetContactMethodsRequestRequestTypeDef",
    {
        "protocols": List[ContactProtocolType],
    },
    total=False,
)

GetContactMethodsResultTypeDef = TypedDict(
    "GetContactMethodsResultTypeDef",
    {
        "contactMethods": List["ContactMethodTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerAPIMetadataResultTypeDef = TypedDict(
    "GetContainerAPIMetadataResultTypeDef",
    {
        "metadata": List[Dict[str, str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerImagesRequestRequestTypeDef = TypedDict(
    "GetContainerImagesRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)

GetContainerImagesResultTypeDef = TypedDict(
    "GetContainerImagesResultTypeDef",
    {
        "containerImages": List["ContainerImageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetContainerLogRequestRequestTypeDef = TypedDict(
    "_RequiredGetContainerLogRequestRequestTypeDef",
    {
        "serviceName": str,
        "containerName": str,
    },
)
_OptionalGetContainerLogRequestRequestTypeDef = TypedDict(
    "_OptionalGetContainerLogRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "filterPattern": str,
        "pageToken": str,
    },
    total=False,
)

class GetContainerLogRequestRequestTypeDef(
    _RequiredGetContainerLogRequestRequestTypeDef, _OptionalGetContainerLogRequestRequestTypeDef
):
    pass

GetContainerLogResultTypeDef = TypedDict(
    "GetContainerLogResultTypeDef",
    {
        "logEvents": List["ContainerServiceLogEventTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServiceDeploymentsRequestRequestTypeDef = TypedDict(
    "GetContainerServiceDeploymentsRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)

GetContainerServiceDeploymentsResultTypeDef = TypedDict(
    "GetContainerServiceDeploymentsResultTypeDef",
    {
        "deployments": List["ContainerServiceDeploymentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServiceMetricDataRequestRequestTypeDef = TypedDict(
    "GetContainerServiceMetricDataRequestRequestTypeDef",
    {
        "serviceName": str,
        "metricName": ContainerServiceMetricNameType,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "period": int,
        "statistics": List[MetricStatisticType],
    },
)

GetContainerServiceMetricDataResultTypeDef = TypedDict(
    "GetContainerServiceMetricDataResultTypeDef",
    {
        "metricName": ContainerServiceMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServicePowersResultTypeDef = TypedDict(
    "GetContainerServicePowersResultTypeDef",
    {
        "powers": List["ContainerServicePowerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContainerServicesRequestRequestTypeDef = TypedDict(
    "GetContainerServicesRequestRequestTypeDef",
    {
        "serviceName": str,
    },
    total=False,
)

GetDiskRequestRequestTypeDef = TypedDict(
    "GetDiskRequestRequestTypeDef",
    {
        "diskName": str,
    },
)

GetDiskResultTypeDef = TypedDict(
    "GetDiskResultTypeDef",
    {
        "disk": "DiskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiskSnapshotRequestRequestTypeDef = TypedDict(
    "GetDiskSnapshotRequestRequestTypeDef",
    {
        "diskSnapshotName": str,
    },
)

GetDiskSnapshotResultTypeDef = TypedDict(
    "GetDiskSnapshotResultTypeDef",
    {
        "diskSnapshot": "DiskSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiskSnapshotsRequestRequestTypeDef = TypedDict(
    "GetDiskSnapshotsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetDiskSnapshotsResultTypeDef = TypedDict(
    "GetDiskSnapshotsResultTypeDef",
    {
        "diskSnapshots": List["DiskSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDisksRequestRequestTypeDef = TypedDict(
    "GetDisksRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetDisksResultTypeDef = TypedDict(
    "GetDisksResultTypeDef",
    {
        "disks": List["DiskTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionBundlesResultTypeDef = TypedDict(
    "GetDistributionBundlesResultTypeDef",
    {
        "bundles": List["DistributionBundleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionLatestCacheResetRequestRequestTypeDef = TypedDict(
    "GetDistributionLatestCacheResetRequestRequestTypeDef",
    {
        "distributionName": str,
    },
    total=False,
)

GetDistributionLatestCacheResetResultTypeDef = TypedDict(
    "GetDistributionLatestCacheResetResultTypeDef",
    {
        "status": str,
        "createTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionMetricDataRequestRequestTypeDef = TypedDict(
    "GetDistributionMetricDataRequestRequestTypeDef",
    {
        "distributionName": str,
        "metricName": DistributionMetricNameType,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "period": int,
        "unit": MetricUnitType,
        "statistics": List[MetricStatisticType],
    },
)

GetDistributionMetricDataResultTypeDef = TypedDict(
    "GetDistributionMetricDataResultTypeDef",
    {
        "metricName": DistributionMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDistributionsRequestRequestTypeDef = TypedDict(
    "GetDistributionsRequestRequestTypeDef",
    {
        "distributionName": str,
        "pageToken": str,
    },
    total=False,
)

GetDistributionsResultTypeDef = TypedDict(
    "GetDistributionsResultTypeDef",
    {
        "distributions": List["LightsailDistributionTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainRequestRequestTypeDef = TypedDict(
    "GetDomainRequestRequestTypeDef",
    {
        "domainName": str,
    },
)

GetDomainResultTypeDef = TypedDict(
    "GetDomainResultTypeDef",
    {
        "domain": "DomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainsRequestRequestTypeDef = TypedDict(
    "GetDomainsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetDomainsResultTypeDef = TypedDict(
    "GetDomainsResultTypeDef",
    {
        "domains": List["DomainTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExportSnapshotRecordsRequestRequestTypeDef = TypedDict(
    "GetExportSnapshotRecordsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetExportSnapshotRecordsResultTypeDef = TypedDict(
    "GetExportSnapshotRecordsResultTypeDef",
    {
        "exportSnapshotRecords": List["ExportSnapshotRecordTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInstanceAccessDetailsRequestRequestTypeDef = TypedDict(
    "_RequiredGetInstanceAccessDetailsRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
_OptionalGetInstanceAccessDetailsRequestRequestTypeDef = TypedDict(
    "_OptionalGetInstanceAccessDetailsRequestRequestTypeDef",
    {
        "protocol": InstanceAccessProtocolType,
    },
    total=False,
)

class GetInstanceAccessDetailsRequestRequestTypeDef(
    _RequiredGetInstanceAccessDetailsRequestRequestTypeDef,
    _OptionalGetInstanceAccessDetailsRequestRequestTypeDef,
):
    pass

GetInstanceAccessDetailsResultTypeDef = TypedDict(
    "GetInstanceAccessDetailsResultTypeDef",
    {
        "accessDetails": "InstanceAccessDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceMetricDataRequestRequestTypeDef = TypedDict(
    "GetInstanceMetricDataRequestRequestTypeDef",
    {
        "instanceName": str,
        "metricName": InstanceMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": List[MetricStatisticType],
    },
)

GetInstanceMetricDataResultTypeDef = TypedDict(
    "GetInstanceMetricDataResultTypeDef",
    {
        "metricName": InstanceMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstancePortStatesRequestRequestTypeDef = TypedDict(
    "GetInstancePortStatesRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstancePortStatesResultTypeDef = TypedDict(
    "GetInstancePortStatesResultTypeDef",
    {
        "portStates": List["InstancePortStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceRequestRequestTypeDef = TypedDict(
    "GetInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstanceResultTypeDef = TypedDict(
    "GetInstanceResultTypeDef",
    {
        "instance": "InstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceSnapshotRequestRequestTypeDef = TypedDict(
    "GetInstanceSnapshotRequestRequestTypeDef",
    {
        "instanceSnapshotName": str,
    },
)

GetInstanceSnapshotResultTypeDef = TypedDict(
    "GetInstanceSnapshotResultTypeDef",
    {
        "instanceSnapshot": "InstanceSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceSnapshotsRequestRequestTypeDef = TypedDict(
    "GetInstanceSnapshotsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetInstanceSnapshotsResultTypeDef = TypedDict(
    "GetInstanceSnapshotsResultTypeDef",
    {
        "instanceSnapshots": List["InstanceSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceStateRequestRequestTypeDef = TypedDict(
    "GetInstanceStateRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

GetInstanceStateResultTypeDef = TypedDict(
    "GetInstanceStateResultTypeDef",
    {
        "state": "InstanceStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstancesRequestRequestTypeDef = TypedDict(
    "GetInstancesRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetInstancesResultTypeDef = TypedDict(
    "GetInstancesResultTypeDef",
    {
        "instances": List["InstanceTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPairRequestRequestTypeDef = TypedDict(
    "GetKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
    },
)

GetKeyPairResultTypeDef = TypedDict(
    "GetKeyPairResultTypeDef",
    {
        "keyPair": "KeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKeyPairsRequestRequestTypeDef = TypedDict(
    "GetKeyPairsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetKeyPairsResultTypeDef = TypedDict(
    "GetKeyPairsResultTypeDef",
    {
        "keyPairs": List["KeyPairTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerMetricDataRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerMetricDataRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "metricName": LoadBalancerMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": List[MetricStatisticType],
    },
)

GetLoadBalancerMetricDataResultTypeDef = TypedDict(
    "GetLoadBalancerMetricDataResultTypeDef",
    {
        "metricName": LoadBalancerMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

GetLoadBalancerResultTypeDef = TypedDict(
    "GetLoadBalancerResultTypeDef",
    {
        "loadBalancer": "LoadBalancerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancerTlsCertificatesRequestRequestTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesRequestRequestTypeDef",
    {
        "loadBalancerName": str,
    },
)

GetLoadBalancerTlsCertificatesResultTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesResultTypeDef",
    {
        "tlsCertificates": List["LoadBalancerTlsCertificateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoadBalancersRequestRequestTypeDef = TypedDict(
    "GetLoadBalancersRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetLoadBalancersResultTypeDef = TypedDict(
    "GetLoadBalancersResultTypeDef",
    {
        "loadBalancers": List["LoadBalancerTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationRequestRequestTypeDef = TypedDict(
    "GetOperationRequestRequestTypeDef",
    {
        "operationId": str,
    },
)

GetOperationResultTypeDef = TypedDict(
    "GetOperationResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetOperationsForResourceRequestRequestTypeDef = TypedDict(
    "_RequiredGetOperationsForResourceRequestRequestTypeDef",
    {
        "resourceName": str,
    },
)
_OptionalGetOperationsForResourceRequestRequestTypeDef = TypedDict(
    "_OptionalGetOperationsForResourceRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

class GetOperationsForResourceRequestRequestTypeDef(
    _RequiredGetOperationsForResourceRequestRequestTypeDef,
    _OptionalGetOperationsForResourceRequestRequestTypeDef,
):
    pass

GetOperationsForResourceResultTypeDef = TypedDict(
    "GetOperationsForResourceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "nextPageCount": str,
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOperationsRequestRequestTypeDef = TypedDict(
    "GetOperationsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetOperationsResultTypeDef = TypedDict(
    "GetOperationsResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegionsRequestRequestTypeDef = TypedDict(
    "GetRegionsRequestRequestTypeDef",
    {
        "includeAvailabilityZones": bool,
        "includeRelationalDatabaseAvailabilityZones": bool,
    },
    total=False,
)

GetRegionsResultTypeDef = TypedDict(
    "GetRegionsResultTypeDef",
    {
        "regions": List["RegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseBlueprintsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetRelationalDatabaseBlueprintsResultTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsResultTypeDef",
    {
        "blueprints": List["RelationalDatabaseBlueprintTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseBundlesRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetRelationalDatabaseBundlesResultTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesResultTypeDef",
    {
        "bundles": List["RelationalDatabaseBundleTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRelationalDatabaseEventsRequestRequestTypeDef = TypedDict(
    "_RequiredGetRelationalDatabaseEventsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalGetRelationalDatabaseEventsRequestRequestTypeDef = TypedDict(
    "_OptionalGetRelationalDatabaseEventsRequestRequestTypeDef",
    {
        "durationInMinutes": int,
        "pageToken": str,
    },
    total=False,
)

class GetRelationalDatabaseEventsRequestRequestTypeDef(
    _RequiredGetRelationalDatabaseEventsRequestRequestTypeDef,
    _OptionalGetRelationalDatabaseEventsRequestRequestTypeDef,
):
    pass

GetRelationalDatabaseEventsResultTypeDef = TypedDict(
    "GetRelationalDatabaseEventsResultTypeDef",
    {
        "relationalDatabaseEvents": List["RelationalDatabaseEventTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRelationalDatabaseLogEventsRequestRequestTypeDef = TypedDict(
    "_RequiredGetRelationalDatabaseLogEventsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "logStreamName": str,
    },
)
_OptionalGetRelationalDatabaseLogEventsRequestRequestTypeDef = TypedDict(
    "_OptionalGetRelationalDatabaseLogEventsRequestRequestTypeDef",
    {
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "startFromHead": bool,
        "pageToken": str,
    },
    total=False,
)

class GetRelationalDatabaseLogEventsRequestRequestTypeDef(
    _RequiredGetRelationalDatabaseLogEventsRequestRequestTypeDef,
    _OptionalGetRelationalDatabaseLogEventsRequestRequestTypeDef,
):
    pass

GetRelationalDatabaseLogEventsResultTypeDef = TypedDict(
    "GetRelationalDatabaseLogEventsResultTypeDef",
    {
        "resourceLogEvents": List["LogEventTypeDef"],
        "nextBackwardToken": str,
        "nextForwardToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseLogStreamsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

GetRelationalDatabaseLogStreamsResultTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsResultTypeDef",
    {
        "logStreams": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef = TypedDict(
    "_RequiredGetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalGetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef = TypedDict(
    "_OptionalGetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef",
    {
        "passwordVersion": RelationalDatabasePasswordVersionType,
    },
    total=False,
)

class GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef(
    _RequiredGetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef,
    _OptionalGetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef,
):
    pass

GetRelationalDatabaseMasterUserPasswordResultTypeDef = TypedDict(
    "GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    {
        "masterUserPassword": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseMetricDataRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "metricName": RelationalDatabaseMetricNameType,
        "period": int,
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "unit": MetricUnitType,
        "statistics": List[MetricStatisticType],
    },
)

GetRelationalDatabaseMetricDataResultTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataResultTypeDef",
    {
        "metricName": RelationalDatabaseMetricNameType,
        "metricData": List["MetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRelationalDatabaseParametersRequestRequestTypeDef = TypedDict(
    "_RequiredGetRelationalDatabaseParametersRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalGetRelationalDatabaseParametersRequestRequestTypeDef = TypedDict(
    "_OptionalGetRelationalDatabaseParametersRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

class GetRelationalDatabaseParametersRequestRequestTypeDef(
    _RequiredGetRelationalDatabaseParametersRequestRequestTypeDef,
    _OptionalGetRelationalDatabaseParametersRequestRequestTypeDef,
):
    pass

GetRelationalDatabaseParametersResultTypeDef = TypedDict(
    "GetRelationalDatabaseParametersResultTypeDef",
    {
        "parameters": List["RelationalDatabaseParameterTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

GetRelationalDatabaseResultTypeDef = TypedDict(
    "GetRelationalDatabaseResultTypeDef",
    {
        "relationalDatabase": "RelationalDatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseSnapshotRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotRequestRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
)

GetRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotResultTypeDef",
    {
        "relationalDatabaseSnapshot": "RelationalDatabaseSnapshotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabaseSnapshotsRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetRelationalDatabaseSnapshotsResultTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsResultTypeDef",
    {
        "relationalDatabaseSnapshots": List["RelationalDatabaseSnapshotTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRelationalDatabasesRequestRequestTypeDef = TypedDict(
    "GetRelationalDatabasesRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetRelationalDatabasesResultTypeDef = TypedDict(
    "GetRelationalDatabasesResultTypeDef",
    {
        "relationalDatabases": List["RelationalDatabaseTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStaticIpRequestRequestTypeDef = TypedDict(
    "GetStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)

GetStaticIpResultTypeDef = TypedDict(
    "GetStaticIpResultTypeDef",
    {
        "staticIp": "StaticIpTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStaticIpsRequestRequestTypeDef = TypedDict(
    "GetStaticIpsRequestRequestTypeDef",
    {
        "pageToken": str,
    },
    total=False,
)

GetStaticIpsResultTypeDef = TypedDict(
    "GetStaticIpsResultTypeDef",
    {
        "staticIps": List["StaticIpTypeDef"],
        "nextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HeaderObjectTypeDef = TypedDict(
    "HeaderObjectTypeDef",
    {
        "option": ForwardValuesType,
        "headersAllowList": List[HeaderEnumType],
    },
    total=False,
)

HostKeyAttributesTypeDef = TypedDict(
    "HostKeyAttributesTypeDef",
    {
        "algorithm": str,
        "publicKey": str,
        "witnessedAt": datetime,
        "fingerprintSHA1": str,
        "fingerprintSHA256": str,
        "notValidBefore": datetime,
        "notValidAfter": datetime,
    },
    total=False,
)

ImportKeyPairRequestRequestTypeDef = TypedDict(
    "ImportKeyPairRequestRequestTypeDef",
    {
        "keyPairName": str,
        "publicKeyBase64": str,
    },
)

ImportKeyPairResultTypeDef = TypedDict(
    "ImportKeyPairResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputOriginTypeDef = TypedDict(
    "InputOriginTypeDef",
    {
        "name": str,
        "regionName": RegionNameType,
        "protocolPolicy": OriginProtocolPolicyEnumType,
    },
    total=False,
)

InstanceAccessDetailsTypeDef = TypedDict(
    "InstanceAccessDetailsTypeDef",
    {
        "certKey": str,
        "expiresAt": datetime,
        "ipAddress": str,
        "password": str,
        "passwordData": "PasswordDataTypeDef",
        "privateKey": str,
        "protocol": InstanceAccessProtocolType,
        "instanceName": str,
        "username": str,
        "hostKeys": List["HostKeyAttributesTypeDef"],
    },
    total=False,
)

_RequiredInstanceEntryTypeDef = TypedDict(
    "_RequiredInstanceEntryTypeDef",
    {
        "sourceName": str,
        "instanceType": str,
        "portInfoSource": PortInfoSourceTypeType,
        "availabilityZone": str,
    },
)
_OptionalInstanceEntryTypeDef = TypedDict(
    "_OptionalInstanceEntryTypeDef",
    {
        "userData": str,
    },
    total=False,
)

class InstanceEntryTypeDef(_RequiredInstanceEntryTypeDef, _OptionalInstanceEntryTypeDef):
    pass

InstanceHardwareTypeDef = TypedDict(
    "InstanceHardwareTypeDef",
    {
        "cpuCount": int,
        "disks": List["DiskTypeDef"],
        "ramSizeInGb": float,
    },
    total=False,
)

InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "instanceName": str,
        "instanceHealth": InstanceHealthStateType,
        "instanceHealthReason": InstanceHealthReasonType,
    },
    total=False,
)

InstanceNetworkingTypeDef = TypedDict(
    "InstanceNetworkingTypeDef",
    {
        "monthlyTransfer": "MonthlyTransferTypeDef",
        "ports": List["InstancePortInfoTypeDef"],
    },
    total=False,
)

InstancePortInfoTypeDef = TypedDict(
    "InstancePortInfoTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocolType,
        "accessFrom": str,
        "accessType": PortAccessTypeType,
        "commonName": str,
        "accessDirection": AccessDirectionType,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

InstancePortStateTypeDef = TypedDict(
    "InstancePortStateTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocolType,
        "state": PortStateType,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

InstanceSnapshotInfoTypeDef = TypedDict(
    "InstanceSnapshotInfoTypeDef",
    {
        "fromBundleId": str,
        "fromBlueprintId": str,
        "fromDiskInfo": List["DiskInfoTypeDef"],
    },
    total=False,
)

InstanceSnapshotTypeDef = TypedDict(
    "InstanceSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "state": InstanceSnapshotStateType,
        "progress": str,
        "fromAttachedDisks": List["DiskTypeDef"],
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "fromBlueprintId": str,
        "fromBundleId": str,
        "isFromAutoSnapshot": bool,
        "sizeInGb": int,
    },
    total=False,
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "code": int,
        "name": str,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "blueprintId": str,
        "blueprintName": str,
        "bundleId": str,
        "addOns": List["AddOnTypeDef"],
        "isStaticIp": bool,
        "privateIpAddress": str,
        "publicIpAddress": str,
        "ipv6Addresses": List[str],
        "ipAddressType": IpAddressTypeType,
        "hardware": "InstanceHardwareTypeDef",
        "networking": "InstanceNetworkingTypeDef",
        "state": "InstanceStateTypeDef",
        "username": str,
        "sshKeyName": str,
    },
    total=False,
)

IsVpcPeeredResultTypeDef = TypedDict(
    "IsVpcPeeredResultTypeDef",
    {
        "isPeered": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "fingerprint": str,
    },
    total=False,
)

LightsailDistributionTypeDef = TypedDict(
    "LightsailDistributionTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "alternativeDomainNames": List[str],
        "status": str,
        "isEnabled": bool,
        "domainName": str,
        "bundleId": str,
        "certificateName": str,
        "origin": "OriginTypeDef",
        "originPublicDNS": str,
        "defaultCacheBehavior": "CacheBehaviorTypeDef",
        "cacheBehaviorSettings": "CacheSettingsTypeDef",
        "cacheBehaviors": List["CacheBehaviorPerPathTypeDef"],
        "ableToUpdateBundle": bool,
        "ipAddressType": IpAddressTypeType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

LoadBalancerTlsCertificateDomainValidationOptionTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    {
        "domainName": str,
        "validationStatus": LoadBalancerTlsCertificateDomainStatusType,
    },
    total=False,
)

LoadBalancerTlsCertificateDomainValidationRecordTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
        "validationStatus": LoadBalancerTlsCertificateDomainStatusType,
        "domainName": str,
    },
    total=False,
)

LoadBalancerTlsCertificateRenewalSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    {
        "renewalStatus": LoadBalancerTlsCertificateRenewalStatusType,
        "domainValidationOptions": List["LoadBalancerTlsCertificateDomainValidationOptionTypeDef"],
    },
    total=False,
)

LoadBalancerTlsCertificateSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateSummaryTypeDef",
    {
        "name": str,
        "isAttached": bool,
    },
    total=False,
)

LoadBalancerTlsCertificateTypeDef = TypedDict(
    "LoadBalancerTlsCertificateTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "loadBalancerName": str,
        "isAttached": bool,
        "status": LoadBalancerTlsCertificateStatusType,
        "domainName": str,
        "domainValidationRecords": List["LoadBalancerTlsCertificateDomainValidationRecordTypeDef"],
        "failureReason": LoadBalancerTlsCertificateFailureReasonType,
        "issuedAt": datetime,
        "issuer": str,
        "keyAlgorithm": str,
        "notAfter": datetime,
        "notBefore": datetime,
        "renewalSummary": "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
        "revocationReason": LoadBalancerTlsCertificateRevocationReasonType,
        "revokedAt": datetime,
        "serial": str,
        "signatureAlgorithm": str,
        "subject": str,
        "subjectAlternativeNames": List[str],
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "dnsName": str,
        "state": LoadBalancerStateType,
        "protocol": LoadBalancerProtocolType,
        "publicPorts": List[int],
        "healthCheckPath": str,
        "instancePort": int,
        "instanceHealthSummary": List["InstanceHealthSummaryTypeDef"],
        "tlsCertificateSummaries": List["LoadBalancerTlsCertificateSummaryTypeDef"],
        "configurationOptions": Dict[LoadBalancerAttributeNameType, str],
        "ipAddressType": IpAddressTypeType,
    },
    total=False,
)

LogEventTypeDef = TypedDict(
    "LogEventTypeDef",
    {
        "createdAt": datetime,
        "message": str,
    },
    total=False,
)

MetricDatapointTypeDef = TypedDict(
    "MetricDatapointTypeDef",
    {
        "average": float,
        "maximum": float,
        "minimum": float,
        "sampleCount": float,
        "sum": float,
        "timestamp": datetime,
        "unit": MetricUnitType,
    },
    total=False,
)

MonitoredResourceInfoTypeDef = TypedDict(
    "MonitoredResourceInfoTypeDef",
    {
        "arn": str,
        "name": str,
        "resourceType": ResourceTypeType,
    },
    total=False,
)

MonthlyTransferTypeDef = TypedDict(
    "MonthlyTransferTypeDef",
    {
        "gbPerMonthAllocated": int,
    },
    total=False,
)

OpenInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "OpenInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfo": "PortInfoTypeDef",
        "instanceName": str,
    },
)

OpenInstancePublicPortsResultTypeDef = TypedDict(
    "OpenInstancePublicPortsResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": ResourceTypeType,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": OperationTypeType,
        "status": OperationStatusType,
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)

OriginTypeDef = TypedDict(
    "OriginTypeDef",
    {
        "name": str,
        "resourceType": ResourceTypeType,
        "regionName": RegionNameType,
        "protocolPolicy": OriginProtocolPolicyEnumType,
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

PasswordDataTypeDef = TypedDict(
    "PasswordDataTypeDef",
    {
        "ciphertext": str,
        "keyPairName": str,
    },
    total=False,
)

PeerVpcResultTypeDef = TypedDict(
    "PeerVpcResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {
        "action": str,
        "description": str,
        "currentApplyDate": datetime,
    },
    total=False,
)

PendingModifiedRelationalDatabaseValuesTypeDef = TypedDict(
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    {
        "masterUserPassword": str,
        "engineVersion": str,
        "backupRetentionEnabled": bool,
    },
    total=False,
)

PortInfoTypeDef = TypedDict(
    "PortInfoTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocolType,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

_RequiredPutAlarmRequestRequestTypeDef = TypedDict(
    "_RequiredPutAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
        "metricName": MetricNameType,
        "monitoredResourceName": str,
        "comparisonOperator": ComparisonOperatorType,
        "threshold": float,
        "evaluationPeriods": int,
    },
)
_OptionalPutAlarmRequestRequestTypeDef = TypedDict(
    "_OptionalPutAlarmRequestRequestTypeDef",
    {
        "datapointsToAlarm": int,
        "treatMissingData": TreatMissingDataType,
        "contactProtocols": List[ContactProtocolType],
        "notificationTriggers": List[AlarmStateType],
        "notificationEnabled": bool,
    },
    total=False,
)

class PutAlarmRequestRequestTypeDef(
    _RequiredPutAlarmRequestRequestTypeDef, _OptionalPutAlarmRequestRequestTypeDef
):
    pass

PutAlarmResultTypeDef = TypedDict(
    "PutAlarmResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInstancePublicPortsRequestRequestTypeDef = TypedDict(
    "PutInstancePublicPortsRequestRequestTypeDef",
    {
        "portInfos": List["PortInfoTypeDef"],
        "instanceName": str,
    },
)

PutInstancePublicPortsResultTypeDef = TypedDict(
    "PutInstancePublicPortsResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryStringObjectTypeDef = TypedDict(
    "QueryStringObjectTypeDef",
    {
        "option": bool,
        "queryStringsAllowList": List[str],
    },
    total=False,
)

RebootInstanceRequestRequestTypeDef = TypedDict(
    "RebootInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

RebootInstanceResultTypeDef = TypedDict(
    "RebootInstanceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebootRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "RebootRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

RebootRelationalDatabaseResultTypeDef = TypedDict(
    "RebootRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "continentCode": str,
        "description": str,
        "displayName": str,
        "name": RegionNameType,
        "availabilityZones": List["AvailabilityZoneTypeDef"],
        "relationalDatabaseAvailabilityZones": List["AvailabilityZoneTypeDef"],
    },
    total=False,
)

RegisterContainerImageRequestRequestTypeDef = TypedDict(
    "RegisterContainerImageRequestRequestTypeDef",
    {
        "serviceName": str,
        "label": str,
        "digest": str,
    },
)

RegisterContainerImageResultTypeDef = TypedDict(
    "RegisterContainerImageResultTypeDef",
    {
        "containerImage": "ContainerImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelationalDatabaseBlueprintTypeDef = TypedDict(
    "RelationalDatabaseBlueprintTypeDef",
    {
        "blueprintId": str,
        "engine": Literal["mysql"],
        "engineVersion": str,
        "engineDescription": str,
        "engineVersionDescription": str,
        "isEngineDefault": bool,
    },
    total=False,
)

RelationalDatabaseBundleTypeDef = TypedDict(
    "RelationalDatabaseBundleTypeDef",
    {
        "bundleId": str,
        "name": str,
        "price": float,
        "ramSizeInGb": float,
        "diskSizeInGb": int,
        "transferPerMonthInGb": int,
        "cpuCount": int,
        "isEncrypted": bool,
        "isActive": bool,
    },
    total=False,
)

RelationalDatabaseEndpointTypeDef = TypedDict(
    "RelationalDatabaseEndpointTypeDef",
    {
        "port": int,
        "address": str,
    },
    total=False,
)

RelationalDatabaseEventTypeDef = TypedDict(
    "RelationalDatabaseEventTypeDef",
    {
        "resource": str,
        "createdAt": datetime,
        "message": str,
        "eventCategories": List[str],
    },
    total=False,
)

RelationalDatabaseHardwareTypeDef = TypedDict(
    "RelationalDatabaseHardwareTypeDef",
    {
        "cpuCount": int,
        "diskSizeInGb": int,
        "ramSizeInGb": float,
    },
    total=False,
)

RelationalDatabaseParameterTypeDef = TypedDict(
    "RelationalDatabaseParameterTypeDef",
    {
        "allowedValues": str,
        "applyMethod": str,
        "applyType": str,
        "dataType": str,
        "description": str,
        "isModifiable": bool,
        "parameterName": str,
        "parameterValue": str,
    },
    total=False,
)

RelationalDatabaseSnapshotTypeDef = TypedDict(
    "RelationalDatabaseSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "engine": str,
        "engineVersion": str,
        "sizeInGb": int,
        "state": str,
        "fromRelationalDatabaseName": str,
        "fromRelationalDatabaseArn": str,
        "fromRelationalDatabaseBundleId": str,
        "fromRelationalDatabaseBlueprintId": str,
    },
    total=False,
)

RelationalDatabaseTypeDef = TypedDict(
    "RelationalDatabaseTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "tags": List["TagTypeDef"],
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "hardware": "RelationalDatabaseHardwareTypeDef",
        "state": str,
        "secondaryAvailabilityZone": str,
        "backupRetentionEnabled": bool,
        "pendingModifiedValues": "PendingModifiedRelationalDatabaseValuesTypeDef",
        "engine": str,
        "engineVersion": str,
        "latestRestorableTime": datetime,
        "masterUsername": str,
        "parameterApplyStatus": str,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "masterEndpoint": "RelationalDatabaseEndpointTypeDef",
        "pendingMaintenanceActions": List["PendingMaintenanceActionTypeDef"],
        "caCertificateIdentifier": str,
    },
    total=False,
)

ReleaseStaticIpRequestRequestTypeDef = TypedDict(
    "ReleaseStaticIpRequestRequestTypeDef",
    {
        "staticIpName": str,
    },
)

ReleaseStaticIpResultTypeDef = TypedDict(
    "ReleaseStaticIpResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RenewalSummaryTypeDef = TypedDict(
    "RenewalSummaryTypeDef",
    {
        "domainValidationRecords": List["DomainValidationRecordTypeDef"],
        "renewalStatus": RenewalStatusType,
        "renewalStatusReason": str,
        "updatedAt": datetime,
    },
    total=False,
)

ResetDistributionCacheRequestRequestTypeDef = TypedDict(
    "ResetDistributionCacheRequestRequestTypeDef",
    {
        "distributionName": str,
    },
    total=False,
)

ResetDistributionCacheResultTypeDef = TypedDict(
    "ResetDistributionCacheResultTypeDef",
    {
        "status": str,
        "createTime": datetime,
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceLocationTypeDef = TypedDict(
    "ResourceLocationTypeDef",
    {
        "availabilityZone": str,
        "regionName": RegionNameType,
    },
    total=False,
)

ResourceReceivingAccessTypeDef = TypedDict(
    "ResourceReceivingAccessTypeDef",
    {
        "name": str,
        "resourceType": str,
    },
    total=False,
)

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
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

SendContactMethodVerificationRequestRequestTypeDef = TypedDict(
    "SendContactMethodVerificationRequestRequestTypeDef",
    {
        "protocol": Literal["Email"],
    },
)

SendContactMethodVerificationResultTypeDef = TypedDict(
    "SendContactMethodVerificationResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetIpAddressTypeRequestRequestTypeDef = TypedDict(
    "SetIpAddressTypeRequestRequestTypeDef",
    {
        "resourceType": ResourceTypeType,
        "resourceName": str,
        "ipAddressType": IpAddressTypeType,
    },
)

SetIpAddressTypeResultTypeDef = TypedDict(
    "SetIpAddressTypeResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetResourceAccessForBucketRequestRequestTypeDef = TypedDict(
    "SetResourceAccessForBucketRequestRequestTypeDef",
    {
        "resourceName": str,
        "bucketName": str,
        "access": ResourceBucketAccessType,
    },
)

SetResourceAccessForBucketResultTypeDef = TypedDict(
    "SetResourceAccessForBucketResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartInstanceRequestRequestTypeDef = TypedDict(
    "StartInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)

StartInstanceResultTypeDef = TypedDict(
    "StartInstanceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "StartRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)

StartRelationalDatabaseResultTypeDef = TypedDict(
    "StartRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StaticIpTypeDef = TypedDict(
    "StaticIpTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceTypeType,
        "ipAddress": str,
        "attachedTo": str,
        "isAttached": bool,
    },
    total=False,
)

_RequiredStopInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredStopInstanceRequestRequestTypeDef",
    {
        "instanceName": str,
    },
)
_OptionalStopInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalStopInstanceRequestRequestTypeDef",
    {
        "force": bool,
    },
    total=False,
)

class StopInstanceRequestRequestTypeDef(
    _RequiredStopInstanceRequestRequestTypeDef, _OptionalStopInstanceRequestRequestTypeDef
):
    pass

StopInstanceResultTypeDef = TypedDict(
    "StopInstanceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStopRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredStopRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalStopRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalStopRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseSnapshotName": str,
    },
    total=False,
)

class StopRelationalDatabaseRequestRequestTypeDef(
    _RequiredStopRelationalDatabaseRequestRequestTypeDef,
    _OptionalStopRelationalDatabaseRequestRequestTypeDef,
):
    pass

StopRelationalDatabaseResultTypeDef = TypedDict(
    "StopRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredTagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredTagResourceRequestRequestTypeDef",
    {
        "resourceName": str,
        "tags": List["TagTypeDef"],
    },
)
_OptionalTagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalTagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
    total=False,
)

class TagResourceRequestRequestTypeDef(
    _RequiredTagResourceRequestRequestTypeDef, _OptionalTagResourceRequestRequestTypeDef
):
    pass

TagResourceResultTypeDef = TypedDict(
    "TagResourceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
    total=False,
)

TestAlarmRequestRequestTypeDef = TypedDict(
    "TestAlarmRequestRequestTypeDef",
    {
        "alarmName": str,
        "state": AlarmStateType,
    },
)

TestAlarmResultTypeDef = TypedDict(
    "TestAlarmResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnpeerVpcResultTypeDef = TypedDict(
    "UnpeerVpcResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUntagResourceRequestRequestTypeDef = TypedDict(
    "_RequiredUntagResourceRequestRequestTypeDef",
    {
        "resourceName": str,
        "tagKeys": List[str],
    },
)
_OptionalUntagResourceRequestRequestTypeDef = TypedDict(
    "_OptionalUntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
    total=False,
)

class UntagResourceRequestRequestTypeDef(
    _RequiredUntagResourceRequestRequestTypeDef, _OptionalUntagResourceRequestRequestTypeDef
):
    pass

UntagResourceResultTypeDef = TypedDict(
    "UntagResourceResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBucketBundleRequestRequestTypeDef = TypedDict(
    "UpdateBucketBundleRequestRequestTypeDef",
    {
        "bucketName": str,
        "bundleId": str,
    },
)

UpdateBucketBundleResultTypeDef = TypedDict(
    "UpdateBucketBundleResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBucketRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateBucketRequestRequestTypeDef",
    {
        "bucketName": str,
    },
)
_OptionalUpdateBucketRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateBucketRequestRequestTypeDef",
    {
        "accessRules": "AccessRulesTypeDef",
        "versioning": str,
        "readonlyAccessAccounts": List[str],
    },
    total=False,
)

class UpdateBucketRequestRequestTypeDef(
    _RequiredUpdateBucketRequestRequestTypeDef, _OptionalUpdateBucketRequestRequestTypeDef
):
    pass

UpdateBucketResultTypeDef = TypedDict(
    "UpdateBucketResultTypeDef",
    {
        "bucket": "BucketTypeDef",
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateContainerServiceRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateContainerServiceRequestRequestTypeDef",
    {
        "serviceName": str,
    },
)
_OptionalUpdateContainerServiceRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateContainerServiceRequestRequestTypeDef",
    {
        "power": ContainerServicePowerNameType,
        "scale": int,
        "isDisabled": bool,
        "publicDomainNames": Dict[str, List[str]],
    },
    total=False,
)

class UpdateContainerServiceRequestRequestTypeDef(
    _RequiredUpdateContainerServiceRequestRequestTypeDef,
    _OptionalUpdateContainerServiceRequestRequestTypeDef,
):
    pass

UpdateContainerServiceResultTypeDef = TypedDict(
    "UpdateContainerServiceResultTypeDef",
    {
        "containerService": "ContainerServiceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDistributionBundleRequestRequestTypeDef = TypedDict(
    "UpdateDistributionBundleRequestRequestTypeDef",
    {
        "distributionName": str,
        "bundleId": str,
    },
    total=False,
)

UpdateDistributionBundleResultTypeDef = TypedDict(
    "UpdateDistributionBundleResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDistributionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDistributionRequestRequestTypeDef",
    {
        "distributionName": str,
    },
)
_OptionalUpdateDistributionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDistributionRequestRequestTypeDef",
    {
        "origin": "InputOriginTypeDef",
        "defaultCacheBehavior": "CacheBehaviorTypeDef",
        "cacheBehaviorSettings": "CacheSettingsTypeDef",
        "cacheBehaviors": List["CacheBehaviorPerPathTypeDef"],
        "isEnabled": bool,
    },
    total=False,
)

class UpdateDistributionRequestRequestTypeDef(
    _RequiredUpdateDistributionRequestRequestTypeDef,
    _OptionalUpdateDistributionRequestRequestTypeDef,
):
    pass

UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef",
    {
        "operation": "OperationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDomainEntryRequestRequestTypeDef = TypedDict(
    "UpdateDomainEntryRequestRequestTypeDef",
    {
        "domainName": str,
        "domainEntry": "DomainEntryTypeDef",
    },
)

UpdateDomainEntryResultTypeDef = TypedDict(
    "UpdateDomainEntryResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLoadBalancerAttributeRequestRequestTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeRequestRequestTypeDef",
    {
        "loadBalancerName": str,
        "attributeName": LoadBalancerAttributeNameType,
        "attributeValue": str,
    },
)

UpdateLoadBalancerAttributeResultTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRelationalDatabaseParametersRequestRequestTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
        "parameters": List["RelationalDatabaseParameterTypeDef"],
    },
)

UpdateRelationalDatabaseParametersResultTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRelationalDatabaseRequestRequestTypeDef",
    {
        "relationalDatabaseName": str,
    },
)
_OptionalUpdateRelationalDatabaseRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRelationalDatabaseRequestRequestTypeDef",
    {
        "masterUserPassword": str,
        "rotateMasterUserPassword": bool,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "enableBackupRetention": bool,
        "disableBackupRetention": bool,
        "publiclyAccessible": bool,
        "applyImmediately": bool,
        "caCertificateIdentifier": str,
    },
    total=False,
)

class UpdateRelationalDatabaseRequestRequestTypeDef(
    _RequiredUpdateRelationalDatabaseRequestRequestTypeDef,
    _OptionalUpdateRelationalDatabaseRequestRequestTypeDef,
):
    pass

UpdateRelationalDatabaseResultTypeDef = TypedDict(
    "UpdateRelationalDatabaseResultTypeDef",
    {
        "operations": List["OperationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
