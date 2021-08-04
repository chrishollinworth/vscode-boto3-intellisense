"""
Type annotations for events service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_events/type_defs.html)

Usage::

    ```python
    from mypy_boto3_events.type_defs import ActivateEventSourceRequestRequestTypeDef

    data: ActivateEventSourceRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    ApiDestinationHttpMethodType,
    ApiDestinationStateType,
    ArchiveStateType,
    AssignPublicIpType,
    ConnectionAuthorizationTypeType,
    ConnectionOAuthHttpMethodType,
    ConnectionStateType,
    EventSourceStateType,
    LaunchTypeType,
    PlacementConstraintTypeType,
    PlacementStrategyTypeType,
    ReplayStateType,
    RuleStateType,
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
    "ActivateEventSourceRequestRequestTypeDef",
    "ApiDestinationTypeDef",
    "ArchiveTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchParametersTypeDef",
    "BatchRetryStrategyTypeDef",
    "CancelReplayRequestRequestTypeDef",
    "CancelReplayResponseTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "ConditionTypeDef",
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    "ConnectionAuthResponseParametersTypeDef",
    "ConnectionBasicAuthResponseParametersTypeDef",
    "ConnectionBodyParameterTypeDef",
    "ConnectionHeaderParameterTypeDef",
    "ConnectionHttpParametersTypeDef",
    "ConnectionOAuthClientResponseParametersTypeDef",
    "ConnectionOAuthResponseParametersTypeDef",
    "ConnectionQueryStringParameterTypeDef",
    "ConnectionTypeDef",
    "CreateApiDestinationRequestRequestTypeDef",
    "CreateApiDestinationResponseTypeDef",
    "CreateArchiveRequestRequestTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    "CreateConnectionAuthRequestParametersTypeDef",
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    "CreateConnectionOAuthRequestParametersTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateEventBusRequestRequestTypeDef",
    "CreateEventBusResponseTypeDef",
    "CreatePartnerEventSourceRequestRequestTypeDef",
    "CreatePartnerEventSourceResponseTypeDef",
    "DeactivateEventSourceRequestRequestTypeDef",
    "DeadLetterConfigTypeDef",
    "DeauthorizeConnectionRequestRequestTypeDef",
    "DeauthorizeConnectionResponseTypeDef",
    "DeleteApiDestinationRequestRequestTypeDef",
    "DeleteArchiveRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteEventBusRequestRequestTypeDef",
    "DeletePartnerEventSourceRequestRequestTypeDef",
    "DeleteRuleRequestRequestTypeDef",
    "DescribeApiDestinationRequestRequestTypeDef",
    "DescribeApiDestinationResponseTypeDef",
    "DescribeArchiveRequestRequestTypeDef",
    "DescribeArchiveResponseTypeDef",
    "DescribeConnectionRequestRequestTypeDef",
    "DescribeConnectionResponseTypeDef",
    "DescribeEventBusRequestRequestTypeDef",
    "DescribeEventBusResponseTypeDef",
    "DescribeEventSourceRequestRequestTypeDef",
    "DescribeEventSourceResponseTypeDef",
    "DescribePartnerEventSourceRequestRequestTypeDef",
    "DescribePartnerEventSourceResponseTypeDef",
    "DescribeReplayRequestRequestTypeDef",
    "DescribeReplayResponseTypeDef",
    "DescribeRuleRequestRequestTypeDef",
    "DescribeRuleResponseTypeDef",
    "DisableRuleRequestRequestTypeDef",
    "EcsParametersTypeDef",
    "EnableRuleRequestRequestTypeDef",
    "EventBusTypeDef",
    "EventSourceTypeDef",
    "HttpParametersTypeDef",
    "InputTransformerTypeDef",
    "KinesisParametersTypeDef",
    "ListApiDestinationsRequestRequestTypeDef",
    "ListApiDestinationsResponseTypeDef",
    "ListArchivesRequestRequestTypeDef",
    "ListArchivesResponseTypeDef",
    "ListConnectionsRequestRequestTypeDef",
    "ListConnectionsResponseTypeDef",
    "ListEventBusesRequestRequestTypeDef",
    "ListEventBusesResponseTypeDef",
    "ListEventSourcesRequestRequestTypeDef",
    "ListEventSourcesResponseTypeDef",
    "ListPartnerEventSourceAccountsRequestRequestTypeDef",
    "ListPartnerEventSourceAccountsResponseTypeDef",
    "ListPartnerEventSourcesRequestRequestTypeDef",
    "ListPartnerEventSourcesResponseTypeDef",
    "ListReplaysRequestRequestTypeDef",
    "ListReplaysResponseTypeDef",
    "ListRuleNamesByTargetRequestRequestTypeDef",
    "ListRuleNamesByTargetResponseTypeDef",
    "ListRulesRequestRequestTypeDef",
    "ListRulesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsByRuleRequestRequestTypeDef",
    "ListTargetsByRuleResponseTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PartnerEventSourceAccountTypeDef",
    "PartnerEventSourceTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PutEventsRequestEntryTypeDef",
    "PutEventsRequestRequestTypeDef",
    "PutEventsResponseTypeDef",
    "PutEventsResultEntryTypeDef",
    "PutPartnerEventsRequestEntryTypeDef",
    "PutPartnerEventsRequestRequestTypeDef",
    "PutPartnerEventsResponseTypeDef",
    "PutPartnerEventsResultEntryTypeDef",
    "PutPermissionRequestRequestTypeDef",
    "PutRuleRequestRequestTypeDef",
    "PutRuleResponseTypeDef",
    "PutTargetsRequestRequestTypeDef",
    "PutTargetsResponseTypeDef",
    "PutTargetsResultEntryTypeDef",
    "RedshiftDataParametersTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "RemoveTargetsRequestRequestTypeDef",
    "RemoveTargetsResponseTypeDef",
    "RemoveTargetsResultEntryTypeDef",
    "ReplayDestinationTypeDef",
    "ReplayTypeDef",
    "ResponseMetadataTypeDef",
    "RetryPolicyTypeDef",
    "RuleTypeDef",
    "RunCommandParametersTypeDef",
    "RunCommandTargetTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "SqsParametersTypeDef",
    "StartReplayRequestRequestTypeDef",
    "StartReplayResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TestEventPatternRequestRequestTypeDef",
    "TestEventPatternResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApiDestinationRequestRequestTypeDef",
    "UpdateApiDestinationResponseTypeDef",
    "UpdateArchiveRequestRequestTypeDef",
    "UpdateArchiveResponseTypeDef",
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    "UpdateConnectionAuthRequestParametersTypeDef",
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    "UpdateConnectionOAuthRequestParametersTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateConnectionResponseTypeDef",
)

ActivateEventSourceRequestRequestTypeDef = TypedDict(
    "ActivateEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

ApiDestinationTypeDef = TypedDict(
    "ApiDestinationTypeDef",
    {
        "ApiDestinationArn": str,
        "Name": str,
        "ApiDestinationState": ApiDestinationStateType,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
    },
    total=False,
)

ArchiveTypeDef = TypedDict(
    "ArchiveTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
    },
    total=False,
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
        "SecurityGroups": List[str],
        "AssignPublicIp": AssignPublicIpType,
    },
    total=False,
)

class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass

BatchArrayPropertiesTypeDef = TypedDict(
    "BatchArrayPropertiesTypeDef",
    {
        "Size": int,
    },
    total=False,
)

_RequiredBatchParametersTypeDef = TypedDict(
    "_RequiredBatchParametersTypeDef",
    {
        "JobDefinition": str,
        "JobName": str,
    },
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

BatchRetryStrategyTypeDef = TypedDict(
    "BatchRetryStrategyTypeDef",
    {
        "Attempts": int,
    },
    total=False,
)

CancelReplayRequestRequestTypeDef = TypedDict(
    "CancelReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
    },
)

CancelReplayResponseTypeDef = TypedDict(
    "CancelReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef",
    {
        "capacityProvider": str,
    },
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef",
    {
        "weight": int,
        "base": int,
    },
    total=False,
)

class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "Type": str,
        "Key": str,
        "Value": str,
    },
)

ConnectionApiKeyAuthResponseParametersTypeDef = TypedDict(
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    {
        "ApiKeyName": str,
    },
    total=False,
)

ConnectionAuthResponseParametersTypeDef = TypedDict(
    "ConnectionAuthResponseParametersTypeDef",
    {
        "BasicAuthParameters": "ConnectionBasicAuthResponseParametersTypeDef",
        "OAuthParameters": "ConnectionOAuthResponseParametersTypeDef",
        "ApiKeyAuthParameters": "ConnectionApiKeyAuthResponseParametersTypeDef",
        "InvocationHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

ConnectionBasicAuthResponseParametersTypeDef = TypedDict(
    "ConnectionBasicAuthResponseParametersTypeDef",
    {
        "Username": str,
    },
    total=False,
)

ConnectionBodyParameterTypeDef = TypedDict(
    "ConnectionBodyParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionHeaderParameterTypeDef = TypedDict(
    "ConnectionHeaderParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionHttpParametersTypeDef = TypedDict(
    "ConnectionHttpParametersTypeDef",
    {
        "HeaderParameters": List["ConnectionHeaderParameterTypeDef"],
        "QueryStringParameters": List["ConnectionQueryStringParameterTypeDef"],
        "BodyParameters": List["ConnectionBodyParameterTypeDef"],
    },
    total=False,
)

ConnectionOAuthClientResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthClientResponseParametersTypeDef",
    {
        "ClientID": str,
    },
    total=False,
)

ConnectionOAuthResponseParametersTypeDef = TypedDict(
    "ConnectionOAuthResponseParametersTypeDef",
    {
        "ClientParameters": "ConnectionOAuthClientResponseParametersTypeDef",
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
        "OAuthHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

ConnectionQueryStringParameterTypeDef = TypedDict(
    "ConnectionQueryStringParameterTypeDef",
    {
        "Key": str,
        "Value": str,
        "IsValueSecret": bool,
    },
    total=False,
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionArn": str,
        "Name": str,
        "ConnectionState": ConnectionStateType,
        "StateReason": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
    },
    total=False,
)

_RequiredCreateApiDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
    },
)
_OptionalCreateApiDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApiDestinationRequestRequestTypeDef",
    {
        "Description": str,
        "InvocationRateLimitPerSecond": int,
    },
    total=False,
)

class CreateApiDestinationRequestRequestTypeDef(
    _RequiredCreateApiDestinationRequestRequestTypeDef,
    _OptionalCreateApiDestinationRequestRequestTypeDef,
):
    pass

CreateApiDestinationResponseTypeDef = TypedDict(
    "CreateApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateArchiveRequestRequestTypeDef = TypedDict(
    "_RequiredCreateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
        "EventSourceArn": str,
    },
)
_OptionalCreateArchiveRequestRequestTypeDef = TypedDict(
    "_OptionalCreateArchiveRequestRequestTypeDef",
    {
        "Description": str,
        "EventPattern": str,
        "RetentionDays": int,
    },
    total=False,
)

class CreateArchiveRequestRequestTypeDef(
    _RequiredCreateArchiveRequestRequestTypeDef, _OptionalCreateArchiveRequestRequestTypeDef
):
    pass

CreateArchiveResponseTypeDef = TypedDict(
    "CreateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": str,
        "ApiKeyValue": str,
    },
)

CreateConnectionAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": "CreateConnectionBasicAuthRequestParametersTypeDef",
        "OAuthParameters": "CreateConnectionOAuthRequestParametersTypeDef",
        "ApiKeyAuthParameters": "CreateConnectionApiKeyAuthRequestParametersTypeDef",
        "InvocationHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

CreateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

CreateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": str,
        "ClientSecret": str,
    },
)

_RequiredCreateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "_RequiredCreateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": "CreateConnectionOAuthClientRequestParametersTypeDef",
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
    },
)
_OptionalCreateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "_OptionalCreateConnectionOAuthRequestParametersTypeDef",
    {
        "OAuthHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

class CreateConnectionOAuthRequestParametersTypeDef(
    _RequiredCreateConnectionOAuthRequestParametersTypeDef,
    _OptionalCreateConnectionOAuthRequestParametersTypeDef,
):
    pass

_RequiredCreateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "AuthParameters": "CreateConnectionAuthRequestParametersTypeDef",
    },
)
_OptionalCreateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConnectionRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class CreateConnectionRequestRequestTypeDef(
    _RequiredCreateConnectionRequestRequestTypeDef, _OptionalCreateConnectionRequestRequestTypeDef
):
    pass

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventBusRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventBusRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateEventBusRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventBusRequestRequestTypeDef",
    {
        "EventSourceName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateEventBusRequestRequestTypeDef(
    _RequiredCreateEventBusRequestRequestTypeDef, _OptionalCreateEventBusRequestRequestTypeDef
):
    pass

CreateEventBusResponseTypeDef = TypedDict(
    "CreateEventBusResponseTypeDef",
    {
        "EventBusArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "CreatePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)

CreatePartnerEventSourceResponseTypeDef = TypedDict(
    "CreatePartnerEventSourceResponseTypeDef",
    {
        "EventSourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateEventSourceRequestRequestTypeDef = TypedDict(
    "DeactivateEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

DeauthorizeConnectionRequestRequestTypeDef = TypedDict(
    "DeauthorizeConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeauthorizeConnectionResponseTypeDef = TypedDict(
    "DeauthorizeConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApiDestinationRequestRequestTypeDef = TypedDict(
    "DeleteApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteArchiveRequestRequestTypeDef = TypedDict(
    "DeleteArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEventBusRequestRequestTypeDef = TypedDict(
    "DeleteEventBusRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeletePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "DeletePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
        "Account": str,
    },
)

_RequiredDeleteRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDeleteRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
        "Force": bool,
    },
    total=False,
)

class DeleteRuleRequestRequestTypeDef(
    _RequiredDeleteRuleRequestRequestTypeDef, _OptionalDeleteRuleRequestRequestTypeDef
):
    pass

DescribeApiDestinationRequestRequestTypeDef = TypedDict(
    "DescribeApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeApiDestinationResponseTypeDef = TypedDict(
    "DescribeApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "Name": str,
        "Description": str,
        "ApiDestinationState": ApiDestinationStateType,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeArchiveRequestRequestTypeDef = TypedDict(
    "DescribeArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)

DescribeArchiveResponseTypeDef = TypedDict(
    "DescribeArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "ArchiveName": str,
        "EventSourceArn": str,
        "Description": str,
        "EventPattern": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "RetentionDays": int,
        "SizeBytes": int,
        "EventCount": int,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionRequestRequestTypeDef = TypedDict(
    "DescribeConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeConnectionResponseTypeDef = TypedDict(
    "DescribeConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "Name": str,
        "Description": str,
        "ConnectionState": ConnectionStateType,
        "StateReason": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "SecretArn": str,
        "AuthParameters": "ConnectionAuthResponseParametersTypeDef",
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventBusRequestRequestTypeDef = TypedDict(
    "DescribeEventBusRequestRequestTypeDef",
    {
        "Name": str,
    },
    total=False,
)

DescribeEventBusResponseTypeDef = TypedDict(
    "DescribeEventBusResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSourceRequestRequestTypeDef = TypedDict(
    "DescribeEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeEventSourceResponseTypeDef = TypedDict(
    "DescribeEventSourceResponseTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": EventSourceStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePartnerEventSourceRequestRequestTypeDef = TypedDict(
    "DescribePartnerEventSourceRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribePartnerEventSourceResponseTypeDef = TypedDict(
    "DescribePartnerEventSourceResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplayRequestRequestTypeDef = TypedDict(
    "DescribeReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
    },
)

DescribeReplayResponseTypeDef = TypedDict(
    "DescribeReplayResponseTypeDef",
    {
        "ReplayName": str,
        "ReplayArn": str,
        "Description": str,
        "State": ReplayStateType,
        "StateReason": str,
        "EventSourceArn": str,
        "Destination": "ReplayDestinationTypeDef",
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDescribeRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)

class DescribeRuleRequestRequestTypeDef(
    _RequiredDescribeRuleRequestRequestTypeDef, _OptionalDescribeRuleRequestRequestTypeDef
):
    pass

DescribeRuleResponseTypeDef = TypedDict(
    "DescribeRuleResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "ScheduleExpression": str,
        "State": RuleStateType,
        "Description": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
        "CreatedBy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDisableRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalDisableRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDisableRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)

class DisableRuleRequestRequestTypeDef(
    _RequiredDisableRuleRequestRequestTypeDef, _OptionalDisableRuleRequestRequestTypeDef
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
        "TaskCount": int,
        "LaunchType": LaunchTypeType,
        "NetworkConfiguration": "NetworkConfigurationTypeDef",
        "PlatformVersion": str,
        "Group": str,
        "CapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "EnableECSManagedTags": bool,
        "EnableExecuteCommand": bool,
        "PlacementConstraints": List["PlacementConstraintTypeDef"],
        "PlacementStrategy": List["PlacementStrategyTypeDef"],
        "PropagateTags": Literal["TASK_DEFINITION"],
        "ReferenceId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class EcsParametersTypeDef(_RequiredEcsParametersTypeDef, _OptionalEcsParametersTypeDef):
    pass

_RequiredEnableRuleRequestRequestTypeDef = TypedDict(
    "_RequiredEnableRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalEnableRuleRequestRequestTypeDef = TypedDict(
    "_OptionalEnableRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)

class EnableRuleRequestRequestTypeDef(
    _RequiredEnableRuleRequestRequestTypeDef, _OptionalEnableRuleRequestRequestTypeDef
):
    pass

EventBusTypeDef = TypedDict(
    "EventBusTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Policy": str,
    },
    total=False,
)

EventSourceTypeDef = TypedDict(
    "EventSourceTypeDef",
    {
        "Arn": str,
        "CreatedBy": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "Name": str,
        "State": EventSourceStateType,
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
    "_RequiredInputTransformerTypeDef",
    {
        "InputTemplate": str,
    },
)
_OptionalInputTransformerTypeDef = TypedDict(
    "_OptionalInputTransformerTypeDef",
    {
        "InputPathsMap": Dict[str, str],
    },
    total=False,
)

class InputTransformerTypeDef(_RequiredInputTransformerTypeDef, _OptionalInputTransformerTypeDef):
    pass

KinesisParametersTypeDef = TypedDict(
    "KinesisParametersTypeDef",
    {
        "PartitionKeyPath": str,
    },
)

ListApiDestinationsRequestRequestTypeDef = TypedDict(
    "ListApiDestinationsRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "ConnectionArn": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListApiDestinationsResponseTypeDef = TypedDict(
    "ListApiDestinationsResponseTypeDef",
    {
        "ApiDestinations": List["ApiDestinationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListArchivesRequestRequestTypeDef = TypedDict(
    "ListArchivesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "EventSourceArn": str,
        "State": ArchiveStateType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListArchivesResponseTypeDef = TypedDict(
    "ListArchivesResponseTypeDef",
    {
        "Archives": List["ArchiveTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectionsRequestRequestTypeDef = TypedDict(
    "ListConnectionsRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "ConnectionState": ConnectionStateType,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListConnectionsResponseTypeDef = TypedDict(
    "ListConnectionsResponseTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventBusesRequestRequestTypeDef = TypedDict(
    "ListEventBusesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListEventBusesResponseTypeDef = TypedDict(
    "ListEventBusesResponseTypeDef",
    {
        "EventBuses": List["EventBusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSourcesRequestRequestTypeDef = TypedDict(
    "ListEventSourcesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListEventSourcesResponseTypeDef = TypedDict(
    "ListEventSourcesResponseTypeDef",
    {
        "EventSources": List["EventSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPartnerEventSourceAccountsRequestRequestTypeDef = TypedDict(
    "_RequiredListPartnerEventSourceAccountsRequestRequestTypeDef",
    {
        "EventSourceName": str,
    },
)
_OptionalListPartnerEventSourceAccountsRequestRequestTypeDef = TypedDict(
    "_OptionalListPartnerEventSourceAccountsRequestRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class ListPartnerEventSourceAccountsRequestRequestTypeDef(
    _RequiredListPartnerEventSourceAccountsRequestRequestTypeDef,
    _OptionalListPartnerEventSourceAccountsRequestRequestTypeDef,
):
    pass

ListPartnerEventSourceAccountsResponseTypeDef = TypedDict(
    "ListPartnerEventSourceAccountsResponseTypeDef",
    {
        "PartnerEventSourceAccounts": List["PartnerEventSourceAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPartnerEventSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredListPartnerEventSourcesRequestRequestTypeDef",
    {
        "NamePrefix": str,
    },
)
_OptionalListPartnerEventSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalListPartnerEventSourcesRequestRequestTypeDef",
    {
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class ListPartnerEventSourcesRequestRequestTypeDef(
    _RequiredListPartnerEventSourcesRequestRequestTypeDef,
    _OptionalListPartnerEventSourcesRequestRequestTypeDef,
):
    pass

ListPartnerEventSourcesResponseTypeDef = TypedDict(
    "ListPartnerEventSourcesResponseTypeDef",
    {
        "PartnerEventSources": List["PartnerEventSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReplaysRequestRequestTypeDef = TypedDict(
    "ListReplaysRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "State": ReplayStateType,
        "EventSourceArn": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListReplaysResponseTypeDef = TypedDict(
    "ListReplaysResponseTypeDef",
    {
        "Replays": List["ReplayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRuleNamesByTargetRequestRequestTypeDef = TypedDict(
    "_RequiredListRuleNamesByTargetRequestRequestTypeDef",
    {
        "TargetArn": str,
    },
)
_OptionalListRuleNamesByTargetRequestRequestTypeDef = TypedDict(
    "_OptionalListRuleNamesByTargetRequestRequestTypeDef",
    {
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class ListRuleNamesByTargetRequestRequestTypeDef(
    _RequiredListRuleNamesByTargetRequestRequestTypeDef,
    _OptionalListRuleNamesByTargetRequestRequestTypeDef,
):
    pass

ListRuleNamesByTargetResponseTypeDef = TypedDict(
    "ListRuleNamesByTargetResponseTypeDef",
    {
        "RuleNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesRequestRequestTypeDef = TypedDict(
    "ListRulesRequestRequestTypeDef",
    {
        "NamePrefix": str,
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

ListRulesResponseTypeDef = TypedDict(
    "ListRulesResponseTypeDef",
    {
        "Rules": List["RuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTargetsByRuleRequestRequestTypeDef = TypedDict(
    "_RequiredListTargetsByRuleRequestRequestTypeDef",
    {
        "Rule": str,
    },
)
_OptionalListTargetsByRuleRequestRequestTypeDef = TypedDict(
    "_OptionalListTargetsByRuleRequestRequestTypeDef",
    {
        "EventBusName": str,
        "NextToken": str,
        "Limit": int,
    },
    total=False,
)

class ListTargetsByRuleRequestRequestTypeDef(
    _RequiredListTargetsByRuleRequestRequestTypeDef, _OptionalListTargetsByRuleRequestRequestTypeDef
):
    pass

ListTargetsByRuleResponseTypeDef = TypedDict(
    "ListTargetsByRuleResponseTypeDef",
    {
        "Targets": List["TargetTypeDef"],
        "NextToken": str,
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

PartnerEventSourceAccountTypeDef = TypedDict(
    "PartnerEventSourceAccountTypeDef",
    {
        "Account": str,
        "CreationTime": datetime,
        "ExpirationTime": datetime,
        "State": EventSourceStateType,
    },
    total=False,
)

PartnerEventSourceTypeDef = TypedDict(
    "PartnerEventSourceTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef",
    {
        "type": PlacementConstraintTypeType,
        "expression": str,
    },
    total=False,
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef",
    {
        "type": PlacementStrategyTypeType,
        "field": str,
    },
    total=False,
)

PutEventsRequestEntryTypeDef = TypedDict(
    "PutEventsRequestEntryTypeDef",
    {
        "Time": Union[datetime, str],
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
        "EventBusName": str,
        "TraceHeader": str,
    },
    total=False,
)

PutEventsRequestRequestTypeDef = TypedDict(
    "PutEventsRequestRequestTypeDef",
    {
        "Entries": List["PutEventsRequestEntryTypeDef"],
    },
)

PutEventsResponseTypeDef = TypedDict(
    "PutEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List["PutEventsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEventsResultEntryTypeDef = TypedDict(
    "PutEventsResultEntryTypeDef",
    {
        "EventId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutPartnerEventsRequestEntryTypeDef = TypedDict(
    "PutPartnerEventsRequestEntryTypeDef",
    {
        "Time": Union[datetime, str],
        "Source": str,
        "Resources": List[str],
        "DetailType": str,
        "Detail": str,
    },
    total=False,
)

PutPartnerEventsRequestRequestTypeDef = TypedDict(
    "PutPartnerEventsRequestRequestTypeDef",
    {
        "Entries": List["PutPartnerEventsRequestEntryTypeDef"],
    },
)

PutPartnerEventsResponseTypeDef = TypedDict(
    "PutPartnerEventsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "Entries": List["PutPartnerEventsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutPartnerEventsResultEntryTypeDef = TypedDict(
    "PutPartnerEventsResultEntryTypeDef",
    {
        "EventId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

PutPermissionRequestRequestTypeDef = TypedDict(
    "PutPermissionRequestRequestTypeDef",
    {
        "EventBusName": str,
        "Action": str,
        "Principal": str,
        "StatementId": str,
        "Condition": "ConditionTypeDef",
        "Policy": str,
    },
    total=False,
)

_RequiredPutRuleRequestRequestTypeDef = TypedDict(
    "_RequiredPutRuleRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalPutRuleRequestRequestTypeDef = TypedDict(
    "_OptionalPutRuleRequestRequestTypeDef",
    {
        "ScheduleExpression": str,
        "EventPattern": str,
        "State": RuleStateType,
        "Description": str,
        "RoleArn": str,
        "Tags": List["TagTypeDef"],
        "EventBusName": str,
    },
    total=False,
)

class PutRuleRequestRequestTypeDef(
    _RequiredPutRuleRequestRequestTypeDef, _OptionalPutRuleRequestRequestTypeDef
):
    pass

PutRuleResponseTypeDef = TypedDict(
    "PutRuleResponseTypeDef",
    {
        "RuleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredPutTargetsRequestRequestTypeDef",
    {
        "Rule": str,
        "Targets": List["TargetTypeDef"],
    },
)
_OptionalPutTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalPutTargetsRequestRequestTypeDef",
    {
        "EventBusName": str,
    },
    total=False,
)

class PutTargetsRequestRequestTypeDef(
    _RequiredPutTargetsRequestRequestTypeDef, _OptionalPutTargetsRequestRequestTypeDef
):
    pass

PutTargetsResponseTypeDef = TypedDict(
    "PutTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List["PutTargetsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutTargetsResultEntryTypeDef = TypedDict(
    "PutTargetsResultEntryTypeDef",
    {
        "TargetId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredRedshiftDataParametersTypeDef = TypedDict(
    "_RequiredRedshiftDataParametersTypeDef",
    {
        "Database": str,
        "Sql": str,
    },
)
_OptionalRedshiftDataParametersTypeDef = TypedDict(
    "_OptionalRedshiftDataParametersTypeDef",
    {
        "SecretManagerArn": str,
        "DbUser": str,
        "StatementName": str,
        "WithEvent": bool,
    },
    total=False,
)

class RedshiftDataParametersTypeDef(
    _RequiredRedshiftDataParametersTypeDef, _OptionalRedshiftDataParametersTypeDef
):
    pass

RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "StatementId": str,
        "RemoveAllPermissions": bool,
        "EventBusName": str,
    },
    total=False,
)

_RequiredRemoveTargetsRequestRequestTypeDef = TypedDict(
    "_RequiredRemoveTargetsRequestRequestTypeDef",
    {
        "Rule": str,
        "Ids": List[str],
    },
)
_OptionalRemoveTargetsRequestRequestTypeDef = TypedDict(
    "_OptionalRemoveTargetsRequestRequestTypeDef",
    {
        "EventBusName": str,
        "Force": bool,
    },
    total=False,
)

class RemoveTargetsRequestRequestTypeDef(
    _RequiredRemoveTargetsRequestRequestTypeDef, _OptionalRemoveTargetsRequestRequestTypeDef
):
    pass

RemoveTargetsResponseTypeDef = TypedDict(
    "RemoveTargetsResponseTypeDef",
    {
        "FailedEntryCount": int,
        "FailedEntries": List["RemoveTargetsResultEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTargetsResultEntryTypeDef = TypedDict(
    "RemoveTargetsResultEntryTypeDef",
    {
        "TargetId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredReplayDestinationTypeDef = TypedDict(
    "_RequiredReplayDestinationTypeDef",
    {
        "Arn": str,
    },
)
_OptionalReplayDestinationTypeDef = TypedDict(
    "_OptionalReplayDestinationTypeDef",
    {
        "FilterArns": List[str],
    },
    total=False,
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
        "State": ReplayStateType,
        "StateReason": str,
        "EventStartTime": datetime,
        "EventEndTime": datetime,
        "EventLastReplayedTime": datetime,
        "ReplayStartTime": datetime,
        "ReplayEndTime": datetime,
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
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
    },
    total=False,
)

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "Arn": str,
        "EventPattern": str,
        "State": RuleStateType,
        "Description": str,
        "ScheduleExpression": str,
        "RoleArn": str,
        "ManagedBy": str,
        "EventBusName": str,
    },
    total=False,
)

RunCommandParametersTypeDef = TypedDict(
    "RunCommandParametersTypeDef",
    {
        "RunCommandTargets": List["RunCommandTargetTypeDef"],
    },
)

RunCommandTargetTypeDef = TypedDict(
    "RunCommandTargetTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
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

SqsParametersTypeDef = TypedDict(
    "SqsParametersTypeDef",
    {
        "MessageGroupId": str,
    },
    total=False,
)

_RequiredStartReplayRequestRequestTypeDef = TypedDict(
    "_RequiredStartReplayRequestRequestTypeDef",
    {
        "ReplayName": str,
        "EventSourceArn": str,
        "EventStartTime": Union[datetime, str],
        "EventEndTime": Union[datetime, str],
        "Destination": "ReplayDestinationTypeDef",
    },
)
_OptionalStartReplayRequestRequestTypeDef = TypedDict(
    "_OptionalStartReplayRequestRequestTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class StartReplayRequestRequestTypeDef(
    _RequiredStartReplayRequestRequestTypeDef, _OptionalStartReplayRequestRequestTypeDef
):
    pass

StartReplayResponseTypeDef = TypedDict(
    "StartReplayResponseTypeDef",
    {
        "ReplayArn": str,
        "State": ReplayStateType,
        "StateReason": str,
        "ReplayStartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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

_RequiredTargetTypeDef = TypedDict(
    "_RequiredTargetTypeDef",
    {
        "Id": str,
        "Arn": str,
    },
)
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
        "SageMakerPipelineParameters": "SageMakerPipelineParametersTypeDef",
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "RetryPolicy": "RetryPolicyTypeDef",
    },
    total=False,
)

class TargetTypeDef(_RequiredTargetTypeDef, _OptionalTargetTypeDef):
    pass

TestEventPatternRequestRequestTypeDef = TypedDict(
    "TestEventPatternRequestRequestTypeDef",
    {
        "EventPattern": str,
        "Event": str,
    },
)

TestEventPatternResponseTypeDef = TypedDict(
    "TestEventPatternResponseTypeDef",
    {
        "Result": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateApiDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApiDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateApiDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApiDestinationRequestRequestTypeDef",
    {
        "Description": str,
        "ConnectionArn": str,
        "InvocationEndpoint": str,
        "HttpMethod": ApiDestinationHttpMethodType,
        "InvocationRateLimitPerSecond": int,
    },
    total=False,
)

class UpdateApiDestinationRequestRequestTypeDef(
    _RequiredUpdateApiDestinationRequestRequestTypeDef,
    _OptionalUpdateApiDestinationRequestRequestTypeDef,
):
    pass

UpdateApiDestinationResponseTypeDef = TypedDict(
    "UpdateApiDestinationResponseTypeDef",
    {
        "ApiDestinationArn": str,
        "ApiDestinationState": ApiDestinationStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateArchiveRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateArchiveRequestRequestTypeDef",
    {
        "ArchiveName": str,
    },
)
_OptionalUpdateArchiveRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateArchiveRequestRequestTypeDef",
    {
        "Description": str,
        "EventPattern": str,
        "RetentionDays": int,
    },
    total=False,
)

class UpdateArchiveRequestRequestTypeDef(
    _RequiredUpdateArchiveRequestRequestTypeDef, _OptionalUpdateArchiveRequestRequestTypeDef
):
    pass

UpdateArchiveResponseTypeDef = TypedDict(
    "UpdateArchiveResponseTypeDef",
    {
        "ArchiveArn": str,
        "State": ArchiveStateType,
        "StateReason": str,
        "CreationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectionApiKeyAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    {
        "ApiKeyName": str,
        "ApiKeyValue": str,
    },
    total=False,
)

UpdateConnectionAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionAuthRequestParametersTypeDef",
    {
        "BasicAuthParameters": "UpdateConnectionBasicAuthRequestParametersTypeDef",
        "OAuthParameters": "UpdateConnectionOAuthRequestParametersTypeDef",
        "ApiKeyAuthParameters": "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
        "InvocationHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

UpdateConnectionBasicAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    {
        "Username": str,
        "Password": str,
    },
    total=False,
)

UpdateConnectionOAuthClientRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    {
        "ClientID": str,
        "ClientSecret": str,
    },
    total=False,
)

UpdateConnectionOAuthRequestParametersTypeDef = TypedDict(
    "UpdateConnectionOAuthRequestParametersTypeDef",
    {
        "ClientParameters": "UpdateConnectionOAuthClientRequestParametersTypeDef",
        "AuthorizationEndpoint": str,
        "HttpMethod": ConnectionOAuthHttpMethodType,
        "OAuthHttpParameters": "ConnectionHttpParametersTypeDef",
    },
    total=False,
)

_RequiredUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateConnectionRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalUpdateConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateConnectionRequestRequestTypeDef",
    {
        "Description": str,
        "AuthorizationType": ConnectionAuthorizationTypeType,
        "AuthParameters": "UpdateConnectionAuthRequestParametersTypeDef",
    },
    total=False,
)

class UpdateConnectionRequestRequestTypeDef(
    _RequiredUpdateConnectionRequestRequestTypeDef, _OptionalUpdateConnectionRequestRequestTypeDef
):
    pass

UpdateConnectionResponseTypeDef = TypedDict(
    "UpdateConnectionResponseTypeDef",
    {
        "ConnectionArn": str,
        "ConnectionState": ConnectionStateType,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "LastAuthorizedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
