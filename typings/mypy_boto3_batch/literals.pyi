"""
Type annotations for batch service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/literals.html)

Usage::

    ```python
    from mypy_boto3_batch.literals import ArrayJobDependencyType

    data: ArrayJobDependencyType = "N_TO_N"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ArrayJobDependencyType",
    "AssignPublicIpType",
    "CEStateType",
    "CEStatusType",
    "CETypeType",
    "CRAllocationStrategyType",
    "CRTypeType",
    "DescribeComputeEnvironmentsPaginatorName",
    "DescribeJobDefinitionsPaginatorName",
    "DescribeJobQueuesPaginatorName",
    "DeviceCgroupPermissionType",
    "EFSAuthorizationConfigIAMType",
    "EFSTransitEncryptionType",
    "JQStateType",
    "JQStatusType",
    "JobDefinitionTypeType",
    "JobStatusType",
    "ListJobsPaginatorName",
    "LogDriverType",
    "PlatformCapabilityType",
    "ResourceTypeType",
    "RetryActionType",
)

ArrayJobDependencyType = Literal["N_TO_N", "SEQUENTIAL"]
AssignPublicIpType = Literal["DISABLED", "ENABLED"]
CEStateType = Literal["DISABLED", "ENABLED"]
CEStatusType = Literal["CREATING", "DELETED", "DELETING", "INVALID", "UPDATING", "VALID"]
CETypeType = Literal["MANAGED", "UNMANAGED"]
CRAllocationStrategyType = Literal["BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"]
CRTypeType = Literal["EC2", "FARGATE", "FARGATE_SPOT", "SPOT"]
DescribeComputeEnvironmentsPaginatorName = Literal["describe_compute_environments"]
DescribeJobDefinitionsPaginatorName = Literal["describe_job_definitions"]
DescribeJobQueuesPaginatorName = Literal["describe_job_queues"]
DeviceCgroupPermissionType = Literal["MKNOD", "READ", "WRITE"]
EFSAuthorizationConfigIAMType = Literal["DISABLED", "ENABLED"]
EFSTransitEncryptionType = Literal["DISABLED", "ENABLED"]
JQStateType = Literal["DISABLED", "ENABLED"]
JQStatusType = Literal["CREATING", "DELETED", "DELETING", "INVALID", "UPDATING", "VALID"]
JobDefinitionTypeType = Literal["container", "multinode"]
JobStatusType = Literal[
    "FAILED", "PENDING", "RUNNABLE", "RUNNING", "STARTING", "SUBMITTED", "SUCCEEDED"
]
ListJobsPaginatorName = Literal["list_jobs"]
LogDriverType = Literal["awslogs", "fluentd", "gelf", "journald", "json-file", "splunk", "syslog"]
PlatformCapabilityType = Literal["EC2", "FARGATE"]
ResourceTypeType = Literal["GPU", "MEMORY", "VCPU"]
RetryActionType = Literal["EXIT", "RETRY"]
