"""
Type annotations for opensearch service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opensearch/literals.html)

Usage::

    ```python
    from mypy_boto3_opensearch.literals import ActionSeverityType

    data: ActionSeverityType = "HIGH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ActionSeverityType",
    "ActionStatusType",
    "ActionTypeType",
    "AutoTuneDesiredStateType",
    "AutoTuneStateType",
    "AutoTuneTypeType",
    "ConnectionModeType",
    "DeploymentStatusType",
    "DescribePackagesFilterNameType",
    "DomainHealthType",
    "DomainPackageStatusType",
    "DomainStateType",
    "DryRunModeType",
    "EngineTypeType",
    "IPAddressTypeType",
    "InboundConnectionStatusCodeType",
    "LogTypeType",
    "MaintenanceStatusType",
    "MaintenanceTypeType",
    "MasterNodeStatusType",
    "NodeStatusType",
    "NodeTypeType",
    "OpenSearchPartitionInstanceTypeType",
    "OpenSearchWarmPartitionInstanceTypeType",
    "OptionStateType",
    "OutboundConnectionStatusCodeType",
    "OverallChangeStatusType",
    "PackageStatusType",
    "PackageTypeType",
    "PrincipalTypeType",
    "ReservedInstancePaymentOptionType",
    "RollbackOnDisableType",
    "ScheduleAtType",
    "ScheduledAutoTuneActionTypeType",
    "ScheduledAutoTuneSeverityTypeType",
    "ScheduledByType",
    "SkipUnavailableStatusType",
    "TLSSecurityPolicyType",
    "TimeUnitType",
    "UpgradeStatusType",
    "UpgradeStepType",
    "VolumeTypeType",
    "VpcEndpointErrorCodeType",
    "VpcEndpointStatusType",
    "ZoneStatusType",
)

ActionSeverityType = Literal["HIGH", "LOW", "MEDIUM"]
ActionStatusType = Literal[
    "COMPLETED", "ELIGIBLE", "FAILED", "IN_PROGRESS", "NOT_ELIGIBLE", "PENDING_UPDATE"
]
ActionTypeType = Literal["JVM_HEAP_SIZE_TUNING", "JVM_YOUNG_GEN_TUNING", "SERVICE_SOFTWARE_UPDATE"]
AutoTuneDesiredStateType = Literal["DISABLED", "ENABLED"]
AutoTuneStateType = Literal[
    "DISABLED",
    "DISABLED_AND_ROLLBACK_COMPLETE",
    "DISABLED_AND_ROLLBACK_ERROR",
    "DISABLED_AND_ROLLBACK_IN_PROGRESS",
    "DISABLED_AND_ROLLBACK_SCHEDULED",
    "DISABLE_IN_PROGRESS",
    "ENABLED",
    "ENABLE_IN_PROGRESS",
    "ERROR",
]
AutoTuneTypeType = Literal["SCHEDULED_ACTION"]
ConnectionModeType = Literal["DIRECT", "VPC_ENDPOINT"]
DeploymentStatusType = Literal[
    "COMPLETED", "ELIGIBLE", "IN_PROGRESS", "NOT_ELIGIBLE", "PENDING_UPDATE"
]
DescribePackagesFilterNameType = Literal[
    "EngineVersion", "PackageID", "PackageName", "PackageStatus", "PackageType"
]
DomainHealthType = Literal["Green", "NotAvailable", "Red", "Yellow"]
DomainPackageStatusType = Literal[
    "ACTIVE", "ASSOCIATING", "ASSOCIATION_FAILED", "DISSOCIATING", "DISSOCIATION_FAILED"
]
DomainStateType = Literal["Active", "NotAvailable", "Processing"]
DryRunModeType = Literal["Basic", "Verbose"]
EngineTypeType = Literal["Elasticsearch", "OpenSearch"]
IPAddressTypeType = Literal["dualstack", "ipv4"]
InboundConnectionStatusCodeType = Literal[
    "ACTIVE",
    "APPROVED",
    "DELETED",
    "DELETING",
    "PENDING_ACCEPTANCE",
    "PROVISIONING",
    "REJECTED",
    "REJECTING",
]
LogTypeType = Literal["AUDIT_LOGS", "ES_APPLICATION_LOGS", "INDEX_SLOW_LOGS", "SEARCH_SLOW_LOGS"]
MaintenanceStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "PENDING", "TIMED_OUT"]
MaintenanceTypeType = Literal["REBOOT_NODE", "RESTART_DASHBOARD", "RESTART_SEARCH_PROCESS"]
MasterNodeStatusType = Literal["Available", "UnAvailable"]
NodeStatusType = Literal["Active", "NotAvailable", "StandBy"]
NodeTypeType = Literal["Data", "Master", "Ultrawarm"]
OpenSearchPartitionInstanceTypeType = Literal[
    "c4.2xlarge.search",
    "c4.4xlarge.search",
    "c4.8xlarge.search",
    "c4.large.search",
    "c4.xlarge.search",
    "c5.18xlarge.search",
    "c5.2xlarge.search",
    "c5.4xlarge.search",
    "c5.9xlarge.search",
    "c5.large.search",
    "c5.xlarge.search",
    "c6g.12xlarge.search",
    "c6g.2xlarge.search",
    "c6g.4xlarge.search",
    "c6g.8xlarge.search",
    "c6g.large.search",
    "c6g.xlarge.search",
    "d2.2xlarge.search",
    "d2.4xlarge.search",
    "d2.8xlarge.search",
    "d2.xlarge.search",
    "i2.2xlarge.search",
    "i2.xlarge.search",
    "i3.16xlarge.search",
    "i3.2xlarge.search",
    "i3.4xlarge.search",
    "i3.8xlarge.search",
    "i3.large.search",
    "i3.xlarge.search",
    "m3.2xlarge.search",
    "m3.large.search",
    "m3.medium.search",
    "m3.xlarge.search",
    "m4.10xlarge.search",
    "m4.2xlarge.search",
    "m4.4xlarge.search",
    "m4.large.search",
    "m4.xlarge.search",
    "m5.12xlarge.search",
    "m5.24xlarge.search",
    "m5.2xlarge.search",
    "m5.4xlarge.search",
    "m5.large.search",
    "m5.xlarge.search",
    "m6g.12xlarge.search",
    "m6g.2xlarge.search",
    "m6g.4xlarge.search",
    "m6g.8xlarge.search",
    "m6g.large.search",
    "m6g.xlarge.search",
    "r3.2xlarge.search",
    "r3.4xlarge.search",
    "r3.8xlarge.search",
    "r3.large.search",
    "r3.xlarge.search",
    "r4.16xlarge.search",
    "r4.2xlarge.search",
    "r4.4xlarge.search",
    "r4.8xlarge.search",
    "r4.large.search",
    "r4.xlarge.search",
    "r5.12xlarge.search",
    "r5.24xlarge.search",
    "r5.2xlarge.search",
    "r5.4xlarge.search",
    "r5.large.search",
    "r5.xlarge.search",
    "r6g.12xlarge.search",
    "r6g.2xlarge.search",
    "r6g.4xlarge.search",
    "r6g.8xlarge.search",
    "r6g.large.search",
    "r6g.xlarge.search",
    "r6gd.12xlarge.search",
    "r6gd.16xlarge.search",
    "r6gd.2xlarge.search",
    "r6gd.4xlarge.search",
    "r6gd.8xlarge.search",
    "r6gd.large.search",
    "r6gd.xlarge.search",
    "t2.medium.search",
    "t2.micro.search",
    "t2.small.search",
    "t3.2xlarge.search",
    "t3.large.search",
    "t3.medium.search",
    "t3.micro.search",
    "t3.nano.search",
    "t3.small.search",
    "t3.xlarge.search",
    "t4g.medium.search",
    "t4g.small.search",
    "ultrawarm1.large.search",
    "ultrawarm1.medium.search",
    "ultrawarm1.xlarge.search",
]
OpenSearchWarmPartitionInstanceTypeType = Literal[
    "ultrawarm1.large.search", "ultrawarm1.medium.search", "ultrawarm1.xlarge.search"
]
OptionStateType = Literal["Active", "Processing", "RequiresIndexDocuments"]
OutboundConnectionStatusCodeType = Literal[
    "ACTIVE",
    "APPROVED",
    "DELETED",
    "DELETING",
    "PENDING_ACCEPTANCE",
    "PROVISIONING",
    "REJECTED",
    "REJECTING",
    "VALIDATING",
    "VALIDATION_FAILED",
]
OverallChangeStatusType = Literal["COMPLETED", "FAILED", "PENDING", "PROCESSING"]
PackageStatusType = Literal[
    "AVAILABLE",
    "COPYING",
    "COPY_FAILED",
    "DELETED",
    "DELETE_FAILED",
    "DELETING",
    "VALIDATING",
    "VALIDATION_FAILED",
]
PackageTypeType = Literal["TXT-DICTIONARY", "ZIP-PLUGIN"]
PrincipalTypeType = Literal["AWS_ACCOUNT", "AWS_SERVICE"]
ReservedInstancePaymentOptionType = Literal["ALL_UPFRONT", "NO_UPFRONT", "PARTIAL_UPFRONT"]
RollbackOnDisableType = Literal["DEFAULT_ROLLBACK", "NO_ROLLBACK"]
ScheduleAtType = Literal["NOW", "OFF_PEAK_WINDOW", "TIMESTAMP"]
ScheduledAutoTuneActionTypeType = Literal["JVM_HEAP_SIZE_TUNING", "JVM_YOUNG_GEN_TUNING"]
ScheduledAutoTuneSeverityTypeType = Literal["HIGH", "LOW", "MEDIUM"]
ScheduledByType = Literal["CUSTOMER", "SYSTEM"]
SkipUnavailableStatusType = Literal["DISABLED", "ENABLED"]
TLSSecurityPolicyType = Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"]
TimeUnitType = Literal["HOURS"]
UpgradeStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES"]
UpgradeStepType = Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"]
VolumeTypeType = Literal["gp2", "gp3", "io1", "standard"]
VpcEndpointErrorCodeType = Literal["ENDPOINT_NOT_FOUND", "SERVER_ERROR"]
VpcEndpointStatusType = Literal[
    "ACTIVE", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
]
ZoneStatusType = Literal["Active", "NotAvailable", "StandBy"]
