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
    "IncludeExecutionDataOptionType",
    "KinesisStreamStartPositionType",
    "LaunchTypeType",
    "ListPipesPaginatorName",
    "LogLevelType",
    "MSKStartPositionType",
    "OnPartialBatchItemFailureStreamsType",
    "PipeStateType",
    "PipeTargetInvocationTypeType",
    "PlacementConstraintTypeType",
    "PlacementStrategyTypeType",
    "PropagateTagsType",
    "RequestedPipeStateDescribeResponseType",
    "RequestedPipeStateType",
    "S3OutputFormatType",
    "SelfManagedKafkaStartPositionType",
)

AssignPublicIpType = Literal["DISABLED", "ENABLED"]
BatchJobDependencyTypeType = Literal["N_TO_N", "SEQUENTIAL"]
BatchResourceRequirementTypeType = Literal["GPU", "MEMORY", "VCPU"]
DynamoDBStreamStartPositionType = Literal["LATEST", "TRIM_HORIZON"]
EcsEnvironmentFileTypeType = Literal["s3"]
EcsResourceRequirementTypeType = Literal["GPU", "InferenceAccelerator"]
IncludeExecutionDataOptionType = Literal["ALL"]
KinesisStreamStartPositionType = Literal["AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"]
LaunchTypeType = Literal["EC2", "EXTERNAL", "FARGATE"]
ListPipesPaginatorName = Literal["list_pipes"]
LogLevelType = Literal["ERROR", "INFO", "OFF", "TRACE"]
MSKStartPositionType = Literal["LATEST", "TRIM_HORIZON"]
OnPartialBatchItemFailureStreamsType = Literal["AUTOMATIC_BISECT"]
PipeStateType = Literal[
    "CREATE_FAILED",
    "CREATE_ROLLBACK_FAILED",
    "CREATING",
    "DELETE_FAILED",
    "DELETE_ROLLBACK_FAILED",
    "DELETING",
    "RUNNING",
    "STARTING",
    "START_FAILED",
    "STOPPED",
    "STOPPING",
    "STOP_FAILED",
    "UPDATE_FAILED",
    "UPDATE_ROLLBACK_FAILED",
    "UPDATING",
]
PipeTargetInvocationTypeType = Literal["FIRE_AND_FORGET", "REQUEST_RESPONSE"]
PlacementConstraintTypeType = Literal["distinctInstance", "memberOf"]
PlacementStrategyTypeType = Literal["binpack", "random", "spread"]
PropagateTagsType = Literal["TASK_DEFINITION"]
RequestedPipeStateDescribeResponseType = Literal["DELETED", "RUNNING", "STOPPED"]
RequestedPipeStateType = Literal["RUNNING", "STOPPED"]
S3OutputFormatType = Literal["json", "plain", "w3c"]
SelfManagedKafkaStartPositionType = Literal["LATEST", "TRIM_HORIZON"]
