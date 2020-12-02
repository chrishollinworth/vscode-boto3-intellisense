"""
Main interface for events service type definitions.

Usage::

    ```python
    from mypy_boto3_events.type_defs import ArchiveTypeDef

    data: ArchiveTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArchiveTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchParametersTypeDef",
    "BatchRetryStrategyTypeDef",
    "DeadLetterConfigTypeDef",
    "EcsParametersTypeDef",
    "EventBusTypeDef",
    "EventSourceTypeDef",
    "HttpParametersTypeDef",
    "InputTransformerTypeDef",
    "KinesisParametersTypeDef",
    "NetworkConfigurationTypeDef",
    "PartnerEventSourceAccountTypeDef",
    "PartnerEventSourceTypeDef",
    "PutEventsResultEntryTypeDef",
    "PutPartnerEventsResultEntryTypeDef",
    "PutTargetsResultEntryTypeDef",
    "RedshiftDataParametersTypeDef",
    "RemoveTargetsResultEntryTypeDef",
    "ReplayDestinationTypeDef",
    "ReplayTypeDef",
    "RetryPolicyTypeDef",
    "RuleTypeDef",
    "RunCommandParametersTypeDef",
    "RunCommandTargetTypeDef",
    "SqsParametersTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "CancelReplayResponseTypeDef",
    "ConditionTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateEventBusResponseTypeDef",
    "CreatePartnerEventSourceResponseTypeDef",
    "DescribeArchiveResponseTypeDef",
    "DescribeEventBusResponseTypeDef",
    "DescribeEventSourceResponseTypeDef",
    "DescribePartnerEventSourceResponseTypeDef",
    "DescribeReplayResponseTypeDef",
    "DescribeRuleResponseTypeDef",
    "ListArchivesResponseTypeDef",
    "ListEventBusesResponseTypeDef",
    "ListEventSourcesResponseTypeDef",
    "ListPartnerEventSourceAccountsResponseTypeDef",
    "ListPartnerEventSourcesResponseTypeDef",
    "ListReplaysResponseTypeDef",
    "ListRuleNamesByTargetResponseTypeDef",
    "ListRulesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsByRuleResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutEventsRequestEntryTypeDef",
    "PutEventsResponseTypeDef",
    "PutPartnerEventsRequestEntryTypeDef",
    "PutPartnerEventsResponseTypeDef",
    "PutRuleResponseTypeDef",
    "PutTargetsResponseTypeDef",
    "RemoveTargetsResponseTypeDef",
    "StartReplayResponseTypeDef",
    "TestEventPatternResponseTypeDef",
    "UpdateArchiveResponseTypeDef",
)

ArchiveTypeDef = TypedDict(
    "ArchiveTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
        "State": Literal[
            "ENABLED", "DISABLED", "CREATING", "UPDATING", "CREATE_FAILED", "UPDATE_FAILED"
        ],
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
    },
    total=False,
)

_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef", {"Subnets": List[str]}
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {"SecurityGroups": List[str], "AssignPublicIp": Literal["ENABLED", "DISABLED"]},
    total=False,
)


class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass


BatchArrayPropertiesTypeDef = TypedDict("BatchArrayPropertiesTypeDef", {"Size": int}, total=False)

_RequiredBatchParametersTypeDef = TypedDict(
    "_RequiredBatchParametersTypeDef", {"JobDefinition": str, "JobName": str}
)
_OptionalBatchParametersTypeDef = TypedDict(
    "_OptionalBatchParametersTypeDef",
    {
        "ArrayProperties": "BatchArrayPropertiesTypeDef",
        "RetryStrategy": "BatchRetryStrategyTypeDef",
    },
    total=False,
)


class BatchParametersTypeDef(_RequiredBatchParametersTypeDef, _OptionalBatchParametersTypeDef):
    pass


BatchRetryStrategyTypeDef = TypedDict("BatchRetryStrategyTypeDef", {"Attempts": int}, total=False)

DeadLetterConfigTypeDef = TypedDict("DeadLetterConfigTypeDef", {"Arn": str}, total=False)

_RequiredEcsParametersTypeDef = TypedDict(
    "_RequiredEcsParametersTypeDef", {"TaskDefinitionArn": str}
)
_OptionalEcsParametersTypeDef = TypedDict(
    "_OptionalEcsParametersTypeDef",
    {
        "TaskCount": int,
        "LaunchType": Literal["EC2", "FARGATE"],
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "PlatformVersion": str,
        "Group": str,
    },
    total=False,
)


class EcsParametersTypeDef(_RequiredEcsParametersTypeDef, _OptionalEcsParametersTypeDef):
    pass


EventBusTypeDef = TypedDict(
    "EventBusTypeDef", {"Name": str, "Arn": str, "Policy": str}, total=False
)

EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

HttpParametersTypeDef = TypedDict(
    "HttpParametersTypeDef",
    {
        "PathParameterValues": List[str],
        "HeaderParameters": Dict[str, str],
        "QueryStringParameters": Dict[str, str],
    },
    total=False,
)

_RequiredInputTransformerTypeDef = TypedDict(
    "_RequiredInputTransformerTypeDef", {"InputTemplate": str}
)
_OptionalInputTransformerTypeDef = TypedDict(
    "_OptionalInputTransformerTypeDef", {"InputPathsMap": Dict[str, str]}, total=False
)


class InputTransformerTypeDef(_RequiredInputTransformerTypeDef, _OptionalInputTransformerTypeDef):
    pass


KinesisParametersTypeDef = TypedDict("KinesisParametersTypeDef", {"PartitionKeyPath": str})

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {"awsvpcConfiguration": "AwsVpcConfigurationTypeDef"},
    total=False,
)

PartnerEventSourceAccountTypeDef = TypedDict(
    "PartnerEventSourceAccountTypeDef",
    {
        "Account": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

PartnerEventSourceTypeDef = TypedDict(
    "PartnerEventSourceTypeDef", {"Arn": str, "Name": str}, total=False
)

PutEventsResultEntryTypeDef = TypedDict(
    "PutEventsResultEntryTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

PutPartnerEventsResultEntryTypeDef = TypedDict(
    "PutPartnerEventsResultEntryTypeDef",
    {"EventId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

PutTargetsResultEntryTypeDef = TypedDict(
    "PutTargetsResultEntryTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

_RequiredRedshiftDataParametersTypeDef = TypedDict(
    "_RequiredRedshiftDataParametersTypeDef", {"Database": str, "Sql": str}
)
_OptionalRedshiftDataParametersTypeDef = TypedDict(
    "_OptionalRedshiftDataParametersTypeDef",
    {"SecretManagerArn": str, "DbUser": str, "StatementName": str, "WithEvent": bool},
    total=False,
)


class RedshiftDataParametersTypeDef(
    _RequiredRedshiftDataParametersTypeDef, _OptionalRedshiftDataParametersTypeDef
):
    pass


RemoveTargetsResultEntryTypeDef = TypedDict(
    "RemoveTargetsResultEntryTypeDef",
    {"TargetId": str, "ErrorCode": str, "ErrorMessage": str},
    total=False,
)

_RequiredReplayDestinationTypeDef = TypedDict("_RequiredReplayDestinationTypeDef", {"Arn": str})
_OptionalReplayDestinationTypeDef = TypedDict(
    "_OptionalReplayDestinationTypeDef", {"FilterArns": List[str]}, total=False
)


class ReplayDestinationTypeDef(
    _RequiredReplayDestinationTypeDef, _OptionalReplayDestinationTypeDef
):
    pass


ReplayTypeDef = TypedDict(
    "ReplayTypeDef",
    {
        "ReplayName": str,
        "EventSourceArn": str,
        "State": Literal["STARTING", "RUNNING", "CANCELLING", "COMPLETED", "CANCELLED", "FAILED"],
        "StateReason": str,
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
    },
    total=False,
)

RetryPolicyTypeDef = TypedDict(
    "RetryPolicyTypeDef",
    {"MaximumRetryAttempts": int, "MaximumEventAgeInSeconds": int},
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

RunCommandParametersTypeDef = TypedDict(
    "RunCommandParametersTypeDef", {"RunCommandTargets": List["RunCommandTargetTypeDef"]}
)

RunCommandTargetTypeDef = TypedDict("RunCommandTargetTypeDef", {"Key": str, "Values": List[str]})

SqsParametersTypeDef = TypedDict("SqsParametersTypeDef", {"MessageGroupId": str}, total=False)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

_RequiredTargetTypeDef = TypedDict("_RequiredTargetTypeDef", {"Id": str, "Arn": str})
_OptionalTargetTypeDef = TypedDict(
    "_OptionalTargetTypeDef",
    {
        "RoleArn": str,
        "Input": str,
        "InputPath": str,
        "InputTransformer": "InputTransformerTypeDef",
        "KinesisParameters": "KinesisParametersTypeDef",
        "RunCommandParameters": "RunCommandParametersTypeDef",
        "EcsParameters": "EcsParametersTypeDef",
        "BatchParameters": "BatchParametersTypeDef",
        "SqsParameters": "SqsParametersTypeDef",
        "HttpParameters": "HttpParametersTypeDef",
        "RedshiftDataParameters": "RedshiftDataParametersTypeDef",
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "RetryPolicy": "RetryPolicyTypeDef",
    },
    total=False,
)


class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass


CancelReplayResponseTypeDef = TypedDict(
    "CancelReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": Literal["STARTING", "RUNNING", "CANCELLING", "COMPLETED", "CANCELLED", "FAILED"],
        "StateReason": str,
    },
    total=False,
)

ConditionTypeDef = TypedDict("ConditionTypeDef", {"Type": str, "Key": str, "Value": str})

CreateArchiveResponseTypeDef = TypedDict(
    "CreateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": Literal[
            "ENABLED", "DISABLED", "CREATING", "UPDATING", "CREATE_FAILED", "UPDATE_FAILED"
        ],
        "StateReason": str,
        "CreationTime": datetime,
    },
    total=False,
)

CreateEventBusResponseTypeDef = TypedDict(
    "CreateEventBusResponseTypeDef", {"EventBusArn": str}, total=False
)

CreatePartnerEventSourceResponseTypeDef = TypedDict(
    "CreatePartnerEventSourceResponseTypeDef", {"EventSourceArn": str}, total=False
)

DescribeArchiveResponseTypeDef = TypedDict(
    "DescribeArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "ArchiveName": str,
        "EventSourceArn": str,
        "Description": str,
        "EventPattern": str,
        "State": Literal[
            "ENABLED", "DISABLED", "CREATING", "UPDATING", "CREATE_FAILED", "UPDATE_FAILED"
        ],
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
    },
    total=False,
)

DescribeEventBusResponseTypeDef = TypedDict(
    "DescribeEventBusResponseTypeDef", {"Name": str, "Arn": str, "Policy": str}, total=False
)

DescribeEventSourceResponseTypeDef = TypedDict(
    "DescribeEventSourceResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": Literal["PENDING", "ACTIVE", "DELETED"],
    },
    total=False,
)

DescribePartnerEventSourceResponseTypeDef = TypedDict(
    "DescribePartnerEventSourceResponseTypeDef", {"Arn": str, "Name": str}, total=False
)

DescribeReplayResponseTypeDef = TypedDict(
    "DescribeReplayResponseTypeDef",
    {
        "ReplayName": str,
        "ReplayArn": str,
        "Description": str,
        "State": Literal["STARTING", "RUNNING", "CANCELLING", "COMPLETED", "CANCELLED", "FAILED"],
        "StateReason": str,
        "EventSourceArn": str,
        "Destination": "ReplayDestinationTypeDef",
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
    },
    total=False,
)

DescribeRuleResponseTypeDef = TypedDict(
    "DescribeRuleResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": Literal["ENABLED", "DISABLED"],
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
        "CreatedBy": str,
    },
    total=False,
)

ListArchivesResponseTypeDef = TypedDict(
    "ListArchivesResponseTypeDef",
    {"Archives": List["ArchiveTypeDef"], "NextToken": str},
    total=False,
)

ListEventBusesResponseTypeDef = TypedDict(
    "ListEventBusesResponseTypeDef",
    {"EventBuses": List["EventBusTypeDef"], "NextToken": str},
    total=False,
)

ListEventSourcesResponseTypeDef = TypedDict(
    "ListEventSourcesResponseTypeDef",
    {"EventSources": List["EventSourceTypeDef"], "NextToken": str},
    total=False,
)

ListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "ListPartnerEventSourceAccountsResponseTypeDef",
    {"PartnerEventSourceAccounts": List["PartnerEventSourceAccountTypeDef"], "NextToken": str},
    total=False,
)

ListPartnerEventSourcesResponseTypeDef = TypedDict(
    "ListPartnerEventSourcesResponseTypeDef",
    {"PartnerEventSources": List["PartnerEventSourceTypeDef"], "NextToken": str},
    total=False,
)

ListReplaysResponseTypeDef = TypedDict(
    "ListReplaysResponseTypeDef", {"Replays": List["ReplayTypeDef"], "NextToken": str}, total=False
)

ListRuleNamesByTargetResponseTypeDef = TypedDict(
    "ListRuleNamesByTargetResponseTypeDef", {"RuleNames": List[str], "NextToken": str}, total=False
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef", {"Rules": List["RuleTypeDef"], "NextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

ListTargetsByRuleResponseTypeDef = TypedDict(
    "ListTargetsByRuleResponseTypeDef",
    {"Targets": List["TargetTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutEventsRequestEntryTypeDef = TypedDict(
    "PutEventsRequestEntryTypeDef",
    {
        "Time": datetime,
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
        "EventBusName": str,
    },
    total=False,
)

PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List["PutEventsResultEntryTypeDef"]},
    total=False,
)

PutPartnerEventsRequestEntryTypeDef = TypedDict(
    "PutPartnerEventsRequestEntryTypeDef",
    {"Time": datetime, "Source": str, "Resources": List[str], "DetailType": str, "Detail": str},
    total=False,
)

PutPartnerEventsResponseTypeDef = TypedDict(
    "PutPartnerEventsResponseTypeDef",
    {"FailedEntryCount": int, "Entries": List["PutPartnerEventsResultEntryTypeDef"]},
    total=False,
)

PutRuleResponseTypeDef = TypedDict("PutRuleResponseTypeDef", {"RuleArn": str}, total=False)

PutTargetsResponseTypeDef = TypedDict(
    "PutTargetsResponseTypeDef",
    {"FailedEntryCount": int, "FailedEntries": List["PutTargetsResultEntryTypeDef"]},
    total=False,
)

RemoveTargetsResponseTypeDef = TypedDict(
    "RemoveTargetsResponseTypeDef",
    {"FailedEntryCount": int, "FailedEntries": List["RemoveTargetsResultEntryTypeDef"]},
    total=False,
)

StartReplayResponseTypeDef = TypedDict(
    "StartReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": Literal["STARTING", "RUNNING", "CANCELLING", "COMPLETED", "CANCELLED", "FAILED"],
        "StateReason": str,
        "ReplayStartTime": datetime,
    },
    total=False,
)

TestEventPatternResponseTypeDef = TypedDict(
    "TestEventPatternResponseTypeDef", {"Result": bool}, total=False
)

UpdateArchiveResponseTypeDef = TypedDict(
    "UpdateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": Literal[
            "ENABLED", "DISABLED", "CREATING", "UPDATING", "CREATE_FAILED", "UPDATE_FAILED"
        ],
        "StateReason": str,
        "CreationTime": datetime,
    },
    total=False,
)
