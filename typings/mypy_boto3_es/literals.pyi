"""
Type annotations for es service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/literals.html)

Usage::

    ```python
    from mypy_boto3_es.literals import AutoTuneDesiredStateType

    data: AutoTuneDesiredStateType = "DISABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AutoTuneDesiredStateType",
    "AutoTuneStateType",
    "AutoTuneTypeType",
    "DeploymentStatusType",
    "DescribePackagesFilterNameType",
    "DescribeReservedElasticsearchInstanceOfferingsPaginatorName",
    "DescribeReservedElasticsearchInstancesPaginatorName",
    "DomainPackageStatusType",
    "ESPartitionInstanceTypeType",
    "ESWarmPartitionInstanceTypeType",
    "GetUpgradeHistoryPaginatorName",
    "InboundCrossClusterSearchConnectionStatusCodeType",
    "ListElasticsearchInstanceTypesPaginatorName",
    "ListElasticsearchVersionsPaginatorName",
    "LogTypeType",
    "OptionStateType",
    "OutboundCrossClusterSearchConnectionStatusCodeType",
    "PackageStatusType",
    "PackageTypeType",
    "ReservedElasticsearchInstancePaymentOptionType",
    "RollbackOnDisableType",
    "ScheduledAutoTuneActionTypeType",
    "ScheduledAutoTuneSeverityTypeType",
    "TLSSecurityPolicyType",
    "TimeUnitType",
    "UpgradeStatusType",
    "UpgradeStepType",
    "VolumeTypeType",
)

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
DeploymentStatusType = Literal[
    "COMPLETED", "ELIGIBLE", "IN_PROGRESS", "NOT_ELIGIBLE", "PENDING_UPDATE"
]
DescribePackagesFilterNameType = Literal["PackageID", "PackageName", "PackageStatus"]
DescribeReservedElasticsearchInstanceOfferingsPaginatorName = Literal[
    "describe_reserved_elasticsearch_instance_offerings"
]
DescribeReservedElasticsearchInstancesPaginatorName = Literal[
    "describe_reserved_elasticsearch_instances"
]
DomainPackageStatusType = Literal[
    "ACTIVE", "ASSOCIATING", "ASSOCIATION_FAILED", "DISSOCIATING", "DISSOCIATION_FAILED"
]
ESPartitionInstanceTypeType = Literal[
    "c4.2xlarge.elasticsearch",
    "c4.4xlarge.elasticsearch",
    "c4.8xlarge.elasticsearch",
    "c4.large.elasticsearch",
    "c4.xlarge.elasticsearch",
    "c5.18xlarge.elasticsearch",
    "c5.2xlarge.elasticsearch",
    "c5.4xlarge.elasticsearch",
    "c5.9xlarge.elasticsearch",
    "c5.large.elasticsearch",
    "c5.xlarge.elasticsearch",
    "d2.2xlarge.elasticsearch",
    "d2.4xlarge.elasticsearch",
    "d2.8xlarge.elasticsearch",
    "d2.xlarge.elasticsearch",
    "i2.2xlarge.elasticsearch",
    "i2.xlarge.elasticsearch",
    "i3.16xlarge.elasticsearch",
    "i3.2xlarge.elasticsearch",
    "i3.4xlarge.elasticsearch",
    "i3.8xlarge.elasticsearch",
    "i3.large.elasticsearch",
    "i3.xlarge.elasticsearch",
    "m3.2xlarge.elasticsearch",
    "m3.large.elasticsearch",
    "m3.medium.elasticsearch",
    "m3.xlarge.elasticsearch",
    "m4.10xlarge.elasticsearch",
    "m4.2xlarge.elasticsearch",
    "m4.4xlarge.elasticsearch",
    "m4.large.elasticsearch",
    "m4.xlarge.elasticsearch",
    "m5.12xlarge.elasticsearch",
    "m5.2xlarge.elasticsearch",
    "m5.4xlarge.elasticsearch",
    "m5.large.elasticsearch",
    "m5.xlarge.elasticsearch",
    "r3.2xlarge.elasticsearch",
    "r3.4xlarge.elasticsearch",
    "r3.8xlarge.elasticsearch",
    "r3.large.elasticsearch",
    "r3.xlarge.elasticsearch",
    "r4.16xlarge.elasticsearch",
    "r4.2xlarge.elasticsearch",
    "r4.4xlarge.elasticsearch",
    "r4.8xlarge.elasticsearch",
    "r4.large.elasticsearch",
    "r4.xlarge.elasticsearch",
    "r5.12xlarge.elasticsearch",
    "r5.2xlarge.elasticsearch",
    "r5.4xlarge.elasticsearch",
    "r5.large.elasticsearch",
    "r5.xlarge.elasticsearch",
    "t2.medium.elasticsearch",
    "t2.micro.elasticsearch",
    "t2.small.elasticsearch",
    "ultrawarm1.large.elasticsearch",
    "ultrawarm1.medium.elasticsearch",
]
ESWarmPartitionInstanceTypeType = Literal[
    "ultrawarm1.large.elasticsearch", "ultrawarm1.medium.elasticsearch"
]
GetUpgradeHistoryPaginatorName = Literal["get_upgrade_history"]
InboundCrossClusterSearchConnectionStatusCodeType = Literal[
    "APPROVED", "DELETED", "DELETING", "PENDING_ACCEPTANCE", "REJECTED", "REJECTING"
]
ListElasticsearchInstanceTypesPaginatorName = Literal["list_elasticsearch_instance_types"]
ListElasticsearchVersionsPaginatorName = Literal["list_elasticsearch_versions"]
LogTypeType = Literal["AUDIT_LOGS", "ES_APPLICATION_LOGS", "INDEX_SLOW_LOGS", "SEARCH_SLOW_LOGS"]
OptionStateType = Literal["Active", "Processing", "RequiresIndexDocuments"]
OutboundCrossClusterSearchConnectionStatusCodeType = Literal[
    "ACTIVE",
    "DELETED",
    "DELETING",
    "PENDING_ACCEPTANCE",
    "PROVISIONING",
    "REJECTED",
    "VALIDATING",
    "VALIDATION_FAILED",
]
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
PackageTypeType = Literal["TXT-DICTIONARY"]
ReservedElasticsearchInstancePaymentOptionType = Literal[
    "ALL_UPFRONT", "NO_UPFRONT", "PARTIAL_UPFRONT"
]
RollbackOnDisableType = Literal["DEFAULT_ROLLBACK", "NO_ROLLBACK"]
ScheduledAutoTuneActionTypeType = Literal["JVM_HEAP_SIZE_TUNING", "JVM_YOUNG_GEN_TUNING"]
ScheduledAutoTuneSeverityTypeType = Literal["HIGH", "LOW", "MEDIUM"]
TLSSecurityPolicyType = Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"]
TimeUnitType = Literal["HOURS"]
UpgradeStatusType = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED", "SUCCEEDED_WITH_ISSUES"]
UpgradeStepType = Literal["PRE_UPGRADE_CHECK", "SNAPSHOT", "UPGRADE"]
VolumeTypeType = Literal["gp2", "io1", "standard"]
