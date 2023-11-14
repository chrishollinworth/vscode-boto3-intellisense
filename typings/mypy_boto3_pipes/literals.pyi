"""
Type annotations for pipes service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pipes/literals.html)

Usage::

    ```python
    from mypy_boto3_pipes.literals import AssignPublicIpType

    data: AssignPublicIpType = "DISABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AssignPublicIpType",
    "BatchJobDependencyTypeType",
    "BatchResourceRequirementTypeType",
    "DynamoDBStreamStartPositionType",
    "EcsEnvironmentFileTypeType",
    "EcsResourceRequirementTypeType",
    "KinesisStreamStartPositionType",
    "LaunchTypeType",
    "ListPipesPaginatorName",
    "MSKStartPositionType",
    "OnPartialBatchItemFailureStreamsType",
    "PipeStateType",
    "PipeTargetInvocationTypeType",
    "PlacementConstraintTypeType",
    "PlacementStrategyTypeType",
    "PropagateTagsType",
    "RequestedPipeStateDescribeResponseType",
    "RequestedPipeStateType",
    "SelfManagedKafkaStartPositionType",
)

AssignPublicIpType = Literal["DISABLED", "ENABLED"]
BatchJobDependencyTypeType = Literal["N_TO_N", "SEQUENTIAL"]
BatchResourceRequirementTypeType = Literal["GPU", "MEMORY", "VCPU"]
DynamoDBStreamStartPositionType = Literal["LATEST", "TRIM_HORIZON"]
EcsEnvironmentFileTypeType = Literal["s3"]
EcsResourceRequirementTypeType = Literal["GPU", "InferenceAccelerator"]
KinesisStreamStartPositionType = Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"]
LaunchTypeType = Literal["EC2", "EXTERNAL", "FARGATE"]
ListPipesPaginatorName = Literal["list_pipes"]
MSKStartPositionType = Literal["LATEST", "TRIM_HORIZON"]
OnPartialBatchItemFailureStreamsType = Literal["AUTOMATIC_BISECT"]
PipeStateType = Literal[
    "CREATE_FAILED",
    "CREATING",
    "DELETING",
    "RUNNING",
    "STARTING",
    "START_FAILED",
    "STOPPED",
    "STOPPING",
    "STOP_FAILED",
    "UPDATE_FAILED",
    "UPDATING",
]
PipeTargetInvocationTypeType = Literal["FIRE_AND_FORGET", "REQUEST_RESPONSE"]
PlacementConstraintTypeType = Literal["distinctInstance", "memberOf"]
PlacementStrategyTypeType = Literal["binpack", "random", "spread"]
PropagateTagsType = Literal["TASK_DEFINITION"]
RequestedPipeStateDescribeResponseType = Literal["DELETED", "RUNNING", "STOPPED"]
RequestedPipeStateType = Literal["RUNNING", "STOPPED"]
SelfManagedKafkaStartPositionType = Literal["LATEST", "TRIM_HORIZON"]
