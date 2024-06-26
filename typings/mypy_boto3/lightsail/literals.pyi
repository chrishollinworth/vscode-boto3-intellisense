"""
Type annotations for lightsail service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/literals.html)

Usage::

    ```python
    from mypy_boto3_lightsail.literals import AccessDirectionType

    data: AccessDirectionType = "inbound"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccessDirectionType",
    "AccessTypeType",
    "AccountLevelBpaSyncStatusType",
    "AddOnTypeType",
    "AlarmStateType",
    "AppCategoryType",
    "AutoMountStatusType",
    "AutoSnapshotStatusType",
    "BPAStatusMessageType",
    "BehaviorEnumType",
    "BlueprintTypeType",
    "BucketMetricNameType",
    "CertificateDomainValidationStatusType",
    "CertificateProviderType",
    "CertificateStatusType",
    "CloudFormationStackRecordSourceTypeType",
    "ComparisonOperatorType",
    "ContactMethodStatusType",
    "ContactMethodVerificationProtocolType",
    "ContactProtocolType",
    "ContainerServiceDeploymentStateType",
    "ContainerServiceMetricNameType",
    "ContainerServicePowerNameType",
    "ContainerServiceProtocolType",
    "ContainerServiceStateDetailCodeType",
    "ContainerServiceStateType",
    "CurrencyType",
    "DiskSnapshotStateType",
    "DiskStateType",
    "DistributionMetricNameType",
    "DnsRecordCreationStateCodeType",
    "ExportSnapshotRecordSourceTypeType",
    "ForwardValuesType",
    "GetActiveNamesPaginatorName",
    "GetBlueprintsPaginatorName",
    "GetBundlesPaginatorName",
    "GetCloudFormationStackRecordsPaginatorName",
    "GetDiskSnapshotsPaginatorName",
    "GetDisksPaginatorName",
    "GetDomainsPaginatorName",
    "GetExportSnapshotRecordsPaginatorName",
    "GetInstanceSnapshotsPaginatorName",
    "GetInstancesPaginatorName",
    "GetKeyPairsPaginatorName",
    "GetLoadBalancersPaginatorName",
    "GetOperationsPaginatorName",
    "GetRelationalDatabaseBlueprintsPaginatorName",
    "GetRelationalDatabaseBundlesPaginatorName",
    "GetRelationalDatabaseEventsPaginatorName",
    "GetRelationalDatabaseParametersPaginatorName",
    "GetRelationalDatabaseSnapshotsPaginatorName",
    "GetRelationalDatabasesPaginatorName",
    "GetStaticIpsPaginatorName",
    "HeaderEnumType",
    "HttpEndpointType",
    "HttpProtocolIpv6Type",
    "HttpTokensType",
    "InstanceAccessProtocolType",
    "InstanceHealthReasonType",
    "InstanceHealthStateType",
    "InstanceMetadataStateType",
    "InstanceMetricNameType",
    "InstancePlatformType",
    "InstanceSnapshotStateType",
    "IpAddressTypeType",
    "LoadBalancerAttributeNameType",
    "LoadBalancerMetricNameType",
    "LoadBalancerProtocolType",
    "LoadBalancerStateType",
    "LoadBalancerTlsCertificateDnsRecordCreationStateCodeType",
    "LoadBalancerTlsCertificateDomainStatusType",
    "LoadBalancerTlsCertificateFailureReasonType",
    "LoadBalancerTlsCertificateRenewalStatusType",
    "LoadBalancerTlsCertificateRevocationReasonType",
    "LoadBalancerTlsCertificateStatusType",
    "MetricNameType",
    "MetricStatisticType",
    "MetricUnitType",
    "NameServersUpdateStateCodeType",
    "NetworkProtocolType",
    "OperationStatusType",
    "OperationTypeType",
    "OriginProtocolPolicyEnumType",
    "PortAccessTypeType",
    "PortInfoSourceTypeType",
    "PortStateType",
    "PricingUnitType",
    "R53HostedZoneDeletionStateCodeType",
    "RecordStateType",
    "RegionNameType",
    "RelationalDatabaseEngineType",
    "RelationalDatabaseMetricNameType",
    "RelationalDatabasePasswordVersionType",
    "RenewalStatusType",
    "ResourceBucketAccessType",
    "ResourceTypeType",
    "SetupStatusType",
    "StatusType",
    "StatusTypeType",
    "TreatMissingDataType",
    "ViewerMinimumTlsProtocolVersionEnumType",
)

AccessDirectionType = Literal["inbound", "outbound"]
AccessTypeType = Literal["private", "public"]
AccountLevelBpaSyncStatusType = Literal["Defaulted", "Failed", "InSync", "NeverSynced"]
AddOnTypeType = Literal["AutoSnapshot", "StopInstanceOnIdle"]
AlarmStateType = Literal["ALARM", "INSUFFICIENT_DATA", "OK"]
AppCategoryType = Literal["LfR"]
AutoMountStatusType = Literal["Failed", "Mounted", "NotMounted", "Pending"]
AutoSnapshotStatusType = Literal["Failed", "InProgress", "NotFound", "Success"]
BPAStatusMessageType = Literal[
    "DEFAULTED_FOR_SLR_MISSING", "DEFAULTED_FOR_SLR_MISSING_ON_HOLD", "SYNC_ON_HOLD", "Unknown"
]
BehaviorEnumType = Literal["cache", "dont-cache"]
BlueprintTypeType = Literal["app", "os"]
BucketMetricNameType = Literal["BucketSizeBytes", "NumberOfObjects"]
CertificateDomainValidationStatusType = Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
CertificateProviderType = Literal["LetsEncrypt"]
CertificateStatusType = Literal[
    "EXPIRED",
    "FAILED",
    "INACTIVE",
    "ISSUED",
    "PENDING_VALIDATION",
    "REVOKED",
    "VALIDATION_TIMED_OUT",
]
CloudFormationStackRecordSourceTypeType = Literal["ExportSnapshotRecord"]
ComparisonOperatorType = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",
]
ContactMethodStatusType = Literal["Invalid", "PendingVerification", "Valid"]
ContactMethodVerificationProtocolType = Literal["Email"]
ContactProtocolType = Literal["Email", "SMS"]
ContainerServiceDeploymentStateType = Literal["ACTIVATING", "ACTIVE", "FAILED", "INACTIVE"]
ContainerServiceMetricNameType = Literal["CPUUtilization", "MemoryUtilization"]
ContainerServicePowerNameType = Literal["large", "medium", "micro", "nano", "small", "xlarge"]
ContainerServiceProtocolType = Literal["HTTP", "HTTPS", "TCP", "UDP"]
ContainerServiceStateDetailCodeType = Literal[
    "ACTIVATING_DEPLOYMENT",
    "CERTIFICATE_LIMIT_EXCEEDED",
    "CREATING_DEPLOYMENT",
    "CREATING_NETWORK_INFRASTRUCTURE",
    "CREATING_SYSTEM_RESOURCES",
    "EVALUATING_HEALTH_CHECK",
    "PROVISIONING_CERTIFICATE",
    "PROVISIONING_SERVICE",
    "UNKNOWN_ERROR",
]
ContainerServiceStateType = Literal[
    "DELETING", "DEPLOYING", "DISABLED", "PENDING", "READY", "RUNNING", "UPDATING"
]
CurrencyType = Literal["USD"]
DiskSnapshotStateType = Literal["completed", "error", "pending", "unknown"]
DiskStateType = Literal["available", "error", "in-use", "pending", "unknown"]
DistributionMetricNameType = Literal[
    "BytesDownloaded",
    "BytesUploaded",
    "Http4xxErrorRate",
    "Http5xxErrorRate",
    "Requests",
    "TotalErrorRate",
]
DnsRecordCreationStateCodeType = Literal["FAILED", "STARTED", "SUCCEEDED"]
ExportSnapshotRecordSourceTypeType = Literal["DiskSnapshot", "InstanceSnapshot"]
ForwardValuesType = Literal["all", "allow-list", "none"]
GetActiveNamesPaginatorName = Literal["get_active_names"]
GetBlueprintsPaginatorName = Literal["get_blueprints"]
GetBundlesPaginatorName = Literal["get_bundles"]
GetCloudFormationStackRecordsPaginatorName = Literal["get_cloud_formation_stack_records"]
GetDiskSnapshotsPaginatorName = Literal["get_disk_snapshots"]
GetDisksPaginatorName = Literal["get_disks"]
GetDomainsPaginatorName = Literal["get_domains"]
GetExportSnapshotRecordsPaginatorName = Literal["get_export_snapshot_records"]
GetInstanceSnapshotsPaginatorName = Literal["get_instance_snapshots"]
GetInstancesPaginatorName = Literal["get_instances"]
GetKeyPairsPaginatorName = Literal["get_key_pairs"]
GetLoadBalancersPaginatorName = Literal["get_load_balancers"]
GetOperationsPaginatorName = Literal["get_operations"]
GetRelationalDatabaseBlueprintsPaginatorName = Literal["get_relational_database_blueprints"]
GetRelationalDatabaseBundlesPaginatorName = Literal["get_relational_database_bundles"]
GetRelationalDatabaseEventsPaginatorName = Literal["get_relational_database_events"]
GetRelationalDatabaseParametersPaginatorName = Literal["get_relational_database_parameters"]
GetRelationalDatabaseSnapshotsPaginatorName = Literal["get_relational_database_snapshots"]
GetRelationalDatabasesPaginatorName = Literal["get_relational_databases"]
GetStaticIpsPaginatorName = Literal["get_static_ips"]
HeaderEnumType = Literal[
    "Accept",
    "Accept-Charset",
    "Accept-Datetime",
    "Accept-Encoding",
    "Accept-Language",
    "Authorization",
    "CloudFront-Forwarded-Proto",
    "CloudFront-Is-Desktop-Viewer",
    "CloudFront-Is-Mobile-Viewer",
    "CloudFront-Is-SmartTV-Viewer",
    "CloudFront-Is-Tablet-Viewer",
    "CloudFront-Viewer-Country",
    "Host",
    "Origin",
    "Referer",
]
HttpEndpointType = Literal["disabled", "enabled"]
HttpProtocolIpv6Type = Literal["disabled", "enabled"]
HttpTokensType = Literal["optional", "required"]
InstanceAccessProtocolType = Literal["rdp", "ssh"]
InstanceHealthReasonType = Literal[
    "Instance.DeregistrationInProgress",
    "Instance.FailedHealthChecks",
    "Instance.InvalidState",
    "Instance.IpUnusable",
    "Instance.NotInUse",
    "Instance.NotRegistered",
    "Instance.ResponseCodeMismatch",
    "Instance.Timeout",
    "Lb.InitialHealthChecking",
    "Lb.InternalError",
    "Lb.RegistrationInProgress",
]
InstanceHealthStateType = Literal[
    "draining", "healthy", "initial", "unavailable", "unhealthy", "unused"
]
InstanceMetadataStateType = Literal["applied", "pending"]
InstanceMetricNameType = Literal[
    "BurstCapacityPercentage",
    "BurstCapacityTime",
    "CPUUtilization",
    "MetadataNoToken",
    "NetworkIn",
    "NetworkOut",
    "StatusCheckFailed",
    "StatusCheckFailed_Instance",
    "StatusCheckFailed_System",
]
InstancePlatformType = Literal["LINUX_UNIX", "WINDOWS"]
InstanceSnapshotStateType = Literal["available", "error", "pending"]
IpAddressTypeType = Literal["dualstack", "ipv4", "ipv6"]
LoadBalancerAttributeNameType = Literal[
    "HealthCheckPath",
    "HttpsRedirectionEnabled",
    "SessionStickinessEnabled",
    "SessionStickiness_LB_CookieDurationSeconds",
    "TlsPolicyName",
]
LoadBalancerMetricNameType = Literal[
    "ClientTLSNegotiationErrorCount",
    "HTTPCode_Instance_2XX_Count",
    "HTTPCode_Instance_3XX_Count",
    "HTTPCode_Instance_4XX_Count",
    "HTTPCode_Instance_5XX_Count",
    "HTTPCode_LB_4XX_Count",
    "HTTPCode_LB_5XX_Count",
    "HealthyHostCount",
    "InstanceResponseTime",
    "RejectedConnectionCount",
    "RequestCount",
    "UnhealthyHostCount",
]
LoadBalancerProtocolType = Literal["HTTP", "HTTP_HTTPS"]
LoadBalancerStateType = Literal["active", "active_impaired", "failed", "provisioning", "unknown"]
LoadBalancerTlsCertificateDnsRecordCreationStateCodeType = Literal["FAILED", "STARTED", "SUCCEEDED"]
LoadBalancerTlsCertificateDomainStatusType = Literal["FAILED", "PENDING_VALIDATION", "SUCCESS"]
LoadBalancerTlsCertificateFailureReasonType = Literal[
    "ADDITIONAL_VERIFICATION_REQUIRED",
    "DOMAIN_NOT_ALLOWED",
    "INVALID_PUBLIC_DOMAIN",
    "NO_AVAILABLE_CONTACTS",
    "OTHER",
]
LoadBalancerTlsCertificateRenewalStatusType = Literal[
    "FAILED", "PENDING_AUTO_RENEWAL", "PENDING_VALIDATION", "SUCCESS"
]
LoadBalancerTlsCertificateRevocationReasonType = Literal[
    "AFFILIATION_CHANGED",
    "A_A_COMPROMISE",
    "CA_COMPROMISE",
    "CERTIFICATE_HOLD",
    "CESSATION_OF_OPERATION",
    "KEY_COMPROMISE",
    "PRIVILEGE_WITHDRAWN",
    "REMOVE_FROM_CRL",
    "SUPERCEDED",
    "UNSPECIFIED",
]
LoadBalancerTlsCertificateStatusType = Literal[
    "EXPIRED",
    "FAILED",
    "INACTIVE",
    "ISSUED",
    "PENDING_VALIDATION",
    "REVOKED",
    "UNKNOWN",
    "VALIDATION_TIMED_OUT",
]
MetricNameType = Literal[
    "BurstCapacityPercentage",
    "BurstCapacityTime",
    "CPUUtilization",
    "ClientTLSNegotiationErrorCount",
    "DatabaseConnections",
    "DiskQueueDepth",
    "FreeStorageSpace",
    "HTTPCode_Instance_2XX_Count",
    "HTTPCode_Instance_3XX_Count",
    "HTTPCode_Instance_4XX_Count",
    "HTTPCode_Instance_5XX_Count",
    "HTTPCode_LB_4XX_Count",
    "HTTPCode_LB_5XX_Count",
    "HealthyHostCount",
    "InstanceResponseTime",
    "NetworkIn",
    "NetworkOut",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
    "RejectedConnectionCount",
    "RequestCount",
    "StatusCheckFailed",
    "StatusCheckFailed_Instance",
    "StatusCheckFailed_System",
    "UnhealthyHostCount",
]
MetricStatisticType = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
MetricUnitType = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
NameServersUpdateStateCodeType = Literal["FAILED", "PENDING", "STARTED", "SUCCEEDED"]
NetworkProtocolType = Literal["all", "icmp", "icmpv6", "tcp", "udp"]
OperationStatusType = Literal["Completed", "Failed", "NotStarted", "Started", "Succeeded"]
OperationTypeType = Literal[
    "AllocateStaticIp",
    "AttachCertificateToDistribution",
    "AttachDisk",
    "AttachInstancesToLoadBalancer",
    "AttachLoadBalancerTlsCertificate",
    "AttachStaticIp",
    "CloseInstancePublicPorts",
    "CreateBucket",
    "CreateBucketAccessKey",
    "CreateCertificate",
    "CreateContactMethod",
    "CreateContainerService",
    "CreateContainerServiceDeployment",
    "CreateContainerServiceRegistryLogin",
    "CreateDisk",
    "CreateDiskFromSnapshot",
    "CreateDiskSnapshot",
    "CreateDistribution",
    "CreateDomain",
    "CreateInstance",
    "CreateInstanceSnapshot",
    "CreateInstancesFromSnapshot",
    "CreateLoadBalancer",
    "CreateLoadBalancerTlsCertificate",
    "CreateRelationalDatabase",
    "CreateRelationalDatabaseFromSnapshot",
    "CreateRelationalDatabaseSnapshot",
    "DeleteAlarm",
    "DeleteBucket",
    "DeleteBucketAccessKey",
    "DeleteCertificate",
    "DeleteContactMethod",
    "DeleteContainerImage",
    "DeleteContainerService",
    "DeleteDisk",
    "DeleteDiskSnapshot",
    "DeleteDistribution",
    "DeleteDomain",
    "DeleteDomainEntry",
    "DeleteInstance",
    "DeleteInstanceSnapshot",
    "DeleteKnownHostKeys",
    "DeleteLoadBalancer",
    "DeleteLoadBalancerTlsCertificate",
    "DeleteRelationalDatabase",
    "DeleteRelationalDatabaseSnapshot",
    "DetachCertificateFromDistribution",
    "DetachDisk",
    "DetachInstancesFromLoadBalancer",
    "DetachStaticIp",
    "DisableAddOn",
    "EnableAddOn",
    "GetAlarms",
    "GetContactMethods",
    "OpenInstancePublicPorts",
    "PutAlarm",
    "PutInstancePublicPorts",
    "RebootInstance",
    "RebootRelationalDatabase",
    "RegisterContainerImage",
    "ReleaseStaticIp",
    "ResetDistributionCache",
    "SendContactMethodVerification",
    "SetIpAddressType",
    "SetResourceAccessForBucket",
    "SetupInstanceHttps",
    "StartGUISession",
    "StartInstance",
    "StartRelationalDatabase",
    "StopGUISession",
    "StopInstance",
    "StopRelationalDatabase",
    "TestAlarm",
    "UpdateBucket",
    "UpdateBucketBundle",
    "UpdateContainerService",
    "UpdateDistribution",
    "UpdateDistributionBundle",
    "UpdateDomainEntry",
    "UpdateInstanceMetadataOptions",
    "UpdateLoadBalancerAttribute",
    "UpdateRelationalDatabase",
    "UpdateRelationalDatabaseParameters",
]
OriginProtocolPolicyEnumType = Literal["http-only", "https-only"]
PortAccessTypeType = Literal["Private", "Public"]
PortInfoSourceTypeType = Literal["CLOSED", "DEFAULT", "INSTANCE", "NONE"]
PortStateType = Literal["closed", "open"]
PricingUnitType = Literal["Bundles", "GB", "GB-Mo", "Hrs", "Queries"]
R53HostedZoneDeletionStateCodeType = Literal["FAILED", "PENDING", "STARTED", "SUCCEEDED"]
RecordStateType = Literal["Failed", "Started", "Succeeded"]
RegionNameType = Literal[
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
RelationalDatabaseEngineType = Literal["mysql"]
RelationalDatabaseMetricNameType = Literal[
    "CPUUtilization",
    "DatabaseConnections",
    "DiskQueueDepth",
    "FreeStorageSpace",
    "NetworkReceiveThroughput",
    "NetworkTransmitThroughput",
]
RelationalDatabasePasswordVersionType = Literal["CURRENT", "PENDING", "PREVIOUS"]
RenewalStatusType = Literal["Failed", "PendingAutoRenewal", "PendingValidation", "Success"]
ResourceBucketAccessType = Literal["allow", "deny"]
ResourceTypeType = Literal[
    "Alarm",
    "Bucket",
    "Certificate",
    "CloudFormationStackRecord",
    "ContactMethod",
    "ContainerService",
    "Disk",
    "DiskSnapshot",
    "Distribution",
    "Domain",
    "ExportSnapshotRecord",
    "Instance",
    "InstanceSnapshot",
    "KeyPair",
    "LoadBalancer",
    "LoadBalancerTlsCertificate",
    "PeeredVpc",
    "RelationalDatabase",
    "RelationalDatabaseSnapshot",
    "StaticIp",
]
SetupStatusType = Literal["failed", "inProgress", "succeeded"]
StatusType = Literal[
    "failedInstanceCreation",
    "failedStartingGUISession",
    "failedStoppingGUISession",
    "notStarted",
    "settingUpInstance",
    "startExpired",
    "started",
    "starting",
    "stopped",
    "stopping",
]
StatusTypeType = Literal["Active", "Inactive"]
TreatMissingDataType = Literal["breaching", "ignore", "missing", "notBreaching"]
ViewerMinimumTlsProtocolVersionEnumType = Literal[
    "TLSv1.1_2016", "TLSv1.2_2018", "TLSv1.2_2019", "TLSv1.2_2021"
]
