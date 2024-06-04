"""
Type annotations for scheduler service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_scheduler/type_defs.html)

Usage::

    ```python
    from mypy_boto3_scheduler.type_defs import AwsVpcConfigurationTypeDef

    data: AwsVpcConfigurationTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ActionAfterCompletionType,
    AssignPublicIpType,
    FlexibleTimeWindowModeType,
    LaunchTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    ScheduleGroupStateType,
    ScheduleStateType,
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
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CreateScheduleGroupInputRequestTypeDef",
    "CreateScheduleGroupOutputTypeDef",
    "CreateScheduleInputRequestTypeDef",
    "CreateScheduleOutputTypeDef",
    "DeadLetterConfigTypeDef",
    "DeleteScheduleGroupInputRequestTypeDef",
    "DeleteScheduleInputRequestTypeDef",
    "EcsParametersTypeDef",
    "EventBridgeParametersTypeDef",
    "FlexibleTimeWindowTypeDef",
    "GetScheduleGroupInputRequestTypeDef",
    "GetScheduleGroupOutputTypeDef",
    "GetScheduleInputRequestTypeDef",
    "GetScheduleOutputTypeDef",
    "KinesisParametersTypeDef",
    "ListScheduleGroupsInputRequestTypeDef",
    "ListScheduleGroupsOutputTypeDef",
    "ListSchedulesInputRequestTypeDef",
    "ListSchedulesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "ResponseMetadataTypeDef",
    "RetryPolicyTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "ScheduleGroupSummaryTypeDef",
    "ScheduleSummaryTypeDef",
    "SqsParametersTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateScheduleInputRequestTypeDef",
    "UpdateScheduleOutputTypeDef",
)

_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef",
    {
        "Subnets": List[str],
    },
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {
        "AssignPublicIp": AssignPublicIpType,
        "SecurityGroups": List[str],
    },
    total=False,
)

class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass

_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "base": int,
        "weight": int,
    },
    total=False,
)

class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass

_RequiredCreateScheduleGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateScheduleGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateScheduleGroupInputRequestTypeDef",
    {
        "ClientToken": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateScheduleGroupInputRequestTypeDef(
    _RequiredCreateScheduleGroupInputRequestTypeDef, _OptionalCreateScheduleGroupInputRequestTypeDef
):
    pass

CreateScheduleGroupOutputTypeDef = TypedDict(
    "CreateScheduleGroupOutputTypeDef",
    {
        "ScheduleGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateScheduleInputRequestTypeDef = TypedDict(
    "_RequiredCreateScheduleInputRequestTypeDef",
    {
        "FlexibleTimeWindow": "FlexibleTimeWindowTypeDef",
        "Name": str,
        "ScheduleExpression": str,
        "Target": "TargetTypeDef",
    },
)
_OptionalCreateScheduleInputRequestTypeDef = TypedDict(
    "_OptionalCreateScheduleInputRequestTypeDef",
    {
        "ActionAfterCompletion": ActionAfterCompletionType,
        "ClientToken": str,
        "Description": str,
        "EndDate": Union[datetime, str],
        "GroupName": str,
        "KmsKeyArn": str,
        "ScheduleExpressionTimezone": str,
        "StartDate": Union[datetime, str],
        "State": ScheduleStateType,
    },
    total=False,
)

class CreateScheduleInputRequestTypeDef(
    _RequiredCreateScheduleInputRequestTypeDef, _OptionalCreateScheduleInputRequestTypeDef
):
    pass

CreateScheduleOutputTypeDef = TypedDict(
    "CreateScheduleOutputTypeDef",
    {
        "ScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

_RequiredDeleteScheduleGroupInputRequestTypeDef = TypedDict(
    "_RequiredDeleteScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteScheduleGroupInputRequestTypeDef = TypedDict(
    "_OptionalDeleteScheduleGroupInputRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class DeleteScheduleGroupInputRequestTypeDef(
    _RequiredDeleteScheduleGroupInputRequestTypeDef, _OptionalDeleteScheduleGroupInputRequestTypeDef
):
    pass

_RequiredDeleteScheduleInputRequestTypeDef = TypedDict(
    "_RequiredDeleteScheduleInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteScheduleInputRequestTypeDef = TypedDict(
    "_OptionalDeleteScheduleInputRequestTypeDef",
    {
        "ClientToken": str,
        "GroupName": str,
    },
    total=False,
)

class DeleteScheduleInputRequestTypeDef(
    _RequiredDeleteScheduleInputRequestTypeDef, _OptionalDeleteScheduleInputRequestTypeDef
):
    pass

_RequiredEcsParametersTypeDef = TypedDict(
    "_RequiredEcsParametersTypeDef",
    {
        "TaskDefinitionArn": str,
    },
)
_OptionalEcsParametersTypeDef = TypedDict(
    "_OptionalEcsParametersTypeDef",
    {
        "CapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "Group": str,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "PlacementConstraints": List["PlacementConstraintTypeDef"],
        "PlacementStrategy": List["PlacementStrategyTypeDef"],
        "PlatformVersion": str,
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": List[Dict[str, str]],
        "TaskCount": int,
    },
    total=False,
)

class EcsParametersTypeDef(_RequiredEcsParametersTypeDef, _OptionalEcsParametersTypeDef):
    pass

EventBridgeParametersTypeDef = TypedDict(
    "EventBridgeParametersTypeDef",
    {
        "DetailType": str,
        "Source": str,
    },
)

_RequiredFlexibleTimeWindowTypeDef = TypedDict(
    "_RequiredFlexibleTimeWindowTypeDef",
    {
        "Mode": FlexibleTimeWindowModeType,
    },
)
_OptionalFlexibleTimeWindowTypeDef = TypedDict(
    "_OptionalFlexibleTimeWindowTypeDef",
    {
        "MaximumWindowInMinutes": int,
    },
    total=False,
)

class FlexibleTimeWindowTypeDef(
    _RequiredFlexibleTimeWindowTypeDef, _OptionalFlexibleTimeWindowTypeDef
):
    pass

GetScheduleGroupInputRequestTypeDef = TypedDict(
    "GetScheduleGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetScheduleGroupOutputTypeDef = TypedDict(
    "GetScheduleGroupOutputTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "LastModificationDate": datetime,
        "Name": str,
        "State": ScheduleGroupStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetScheduleInputRequestTypeDef = TypedDict(
    "_RequiredGetScheduleInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalGetScheduleInputRequestTypeDef = TypedDict(
    "_OptionalGetScheduleInputRequestTypeDef",
    {
        "GroupName": str,
    },
    total=False,
)

class GetScheduleInputRequestTypeDef(
    _RequiredGetScheduleInputRequestTypeDef, _OptionalGetScheduleInputRequestTypeDef
):
    pass

GetScheduleOutputTypeDef = TypedDict(
    "GetScheduleOutputTypeDef",
    {
        "ActionAfterCompletion": ActionAfterCompletionType,
        "Arn": str,
        "CreationDate": datetime,
        "Description": str,
        "EndDate": datetime,
        "FlexibleTimeWindow": "FlexibleTimeWindowTypeDef",
        "GroupName": str,
        "KmsKeyArn": str,
        "LastModificationDate": datetime,
        "Name": str,
        "ScheduleExpression": str,
        "ScheduleExpressionTimezone": str,
        "StartDate": datetime,
        "State": ScheduleStateType,
        "Target": "TargetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KinesisParametersTypeDef = TypedDict(
    "KinesisParametersTypeDef",
    {
        "PartitionKey": str,
    },
)

ListScheduleGroupsInputRequestTypeDef = TypedDict(
    "ListScheduleGroupsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NamePrefix": str,
        "NextToken": str,
    },
    total=False,
)

ListScheduleGroupsOutputTypeDef = TypedDict(
    "ListScheduleGroupsOutputTypeDef",
    {
        "NextToken": str,
        "ScheduleGroups": List["ScheduleGroupSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchedulesInputRequestTypeDef = TypedDict(
    "ListSchedulesInputRequestTypeDef",
    {
        "GroupName": str,
        "MaxResults": int,
        "NamePrefix": str,
        "NextToken": str,
        "State": ScheduleStateType,
    },
    total=False,
)

ListSchedulesOutputTypeDef = TypedDict(
    "ListSchedulesOutputTypeDef",
    {
        "NextToken": str,
        "Schedules": List["ScheduleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {
        "awsvpcConfiguration": "AwsVpcConfigurationTypeDef",
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

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "expression": str,
        "type": PlacementConstraintTypeType,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "field": str,
        "type": PlacementStrategyTypeType,
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

RetryPolicyTypeDef = TypedDict(
    "RetryPolicyTypeDef",
    {
        "MaximumEventAgeInSeconds": int,
        "MaximumRetryAttempts": int,
    },
    total=False,
)

SageMakerPipelineParameterTypeDef = TypedDict(
    "SageMakerPipelineParameterTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

SageMakerPipelineParametersTypeDef = TypedDict(
    "SageMakerPipelineParametersTypeDef",
    {
        "PipelineParameterList": List["SageMakerPipelineParameterTypeDef"],
    },
    total=False,
)

ScheduleGroupSummaryTypeDef = TypedDict(
    "ScheduleGroupSummaryTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "LastModificationDate": datetime,
        "Name": str,
        "State": ScheduleGroupStateType,
    },
    total=False,
)

ScheduleSummaryTypeDef = TypedDict(
    "ScheduleSummaryTypeDef",
    {
        "Arn": str,
        "CreationDate": datetime,
        "GroupName": str,
        "LastModificationDate": datetime,
        "Name": str,
        "State": ScheduleStateType,
        "Target": "TargetSummaryTypeDef",
    },
    total=False,
)

SqsParametersTypeDef = TypedDict(
    "SqsParametersTypeDef",
    {
        "MessageGroupId": str,
    },
    total=False,
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "Arn": str,
    },
)

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "Arn": str,
        "RoleArn": str,
    },
)
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "EcsParameters": "EcsParametersTypeDef",
        "EventBridgeParameters": "EventBridgeParametersTypeDef",
        "Input": str,
        "KinesisParameters": "KinesisParametersTypeDef",
        "RetryPolicy": "RetryPolicyTypeDef",
        "SageMakerPipelineParameters": "SageMakerPipelineParametersTypeDef",
        "SqsParameters": "SqsParametersTypeDef",
    },
    total=False,
)

class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateScheduleInputRequestTypeDef = TypedDict(
    "_RequiredUpdateScheduleInputRequestTypeDef",
    {
        "FlexibleTimeWindow": "FlexibleTimeWindowTypeDef",
        "Name": str,
        "ScheduleExpression": str,
        "Target": "TargetTypeDef",
    },
)
_OptionalUpdateScheduleInputRequestTypeDef = TypedDict(
    "_OptionalUpdateScheduleInputRequestTypeDef",
    {
        "ActionAfterCompletion": ActionAfterCompletionType,
        "ClientToken": str,
        "Description": str,
        "EndDate": Union[datetime, str],
        "GroupName": str,
        "KmsKeyArn": str,
        "ScheduleExpressionTimezone": str,
        "StartDate": Union[datetime, str],
        "State": ScheduleStateType,
    },
    total=False,
)

class UpdateScheduleInputRequestTypeDef(
    _RequiredUpdateScheduleInputRequestTypeDef, _OptionalUpdateScheduleInputRequestTypeDef
):
    pass

UpdateScheduleOutputTypeDef = TypedDict(
    "UpdateScheduleOutputTypeDef",
    {
        "ScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
