"""
Type annotations for lambda service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_lambda/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_lambda.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.eventstream import EventStream
from botocore.response import StreamingBody

from .literals import (
    ApplicationLogLevelType,
    ArchitectureType,
    CapacityProviderScalingModeType,
    CapacityProviderStateType,
    CodeSigningPolicyType,
    EventSourcePositionType,
    EventTypeType,
    ExecutionStatusType,
    FullDocumentType,
    FunctionUrlAuthTypeType,
    InvocationTypeType,
    InvokeModeType,
    KafkaSchemaRegistryAuthTypeType,
    KafkaSchemaValidationAttributeType,
    LastUpdateStatusReasonCodeType,
    LastUpdateStatusType,
    LogFormatType,
    LogTypeType,
    OperationActionType,
    OperationStatusType,
    OperationTypeType,
    PackageTypeType,
    ProvisionedConcurrencyStatusEnumType,
    RecursiveLoopType,
    ResponseStreamingInvocationTypeType,
    RuntimeType,
    SchemaRegistryEventRecordFormatType,
    SnapStartApplyOnType,
    SnapStartOptimizationStatusType,
    SourceAccessTypeType,
    StateReasonCodeType,
    StateType,
    SystemLogLevelType,
    TracingModeType,
    UpdateRuntimeOnType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccountLimitTypeDef",
    "AccountUsageTypeDef",
    "AddLayerVersionPermissionRequestTypeDef",
    "AddLayerVersionPermissionResponseTypeDef",
    "AddPermissionRequestTypeDef",
    "AddPermissionResponseTypeDef",
    "AliasConfigurationResponseTypeDef",
    "AliasConfigurationTypeDef",
    "AliasRoutingConfigurationOutputTypeDef",
    "AliasRoutingConfigurationTypeDef",
    "AliasRoutingConfigurationUnionTypeDef",
    "AllowedPublishersOutputTypeDef",
    "AllowedPublishersTypeDef",
    "AllowedPublishersUnionTypeDef",
    "AmazonManagedKafkaEventSourceConfigOutputTypeDef",
    "AmazonManagedKafkaEventSourceConfigTypeDef",
    "AmazonManagedKafkaEventSourceConfigUnionTypeDef",
    "BlobTypeDef",
    "CallbackDetailsTypeDef",
    "CallbackFailedDetailsTypeDef",
    "CallbackOptionsTypeDef",
    "CallbackStartedDetailsTypeDef",
    "CallbackSucceededDetailsTypeDef",
    "CallbackTimedOutDetailsTypeDef",
    "CapacityProviderConfigTypeDef",
    "CapacityProviderPermissionsConfigTypeDef",
    "CapacityProviderScalingConfigOutputTypeDef",
    "CapacityProviderScalingConfigTypeDef",
    "CapacityProviderScalingConfigUnionTypeDef",
    "CapacityProviderTypeDef",
    "CapacityProviderVpcConfigOutputTypeDef",
    "CapacityProviderVpcConfigTypeDef",
    "CapacityProviderVpcConfigUnionTypeDef",
    "ChainedInvokeDetailsTypeDef",
    "ChainedInvokeFailedDetailsTypeDef",
    "ChainedInvokeOptionsTypeDef",
    "ChainedInvokeStartedDetailsTypeDef",
    "ChainedInvokeStoppedDetailsTypeDef",
    "ChainedInvokeSucceededDetailsTypeDef",
    "ChainedInvokeTimedOutDetailsTypeDef",
    "CheckpointDurableExecutionRequestTypeDef",
    "CheckpointDurableExecutionResponseTypeDef",
    "CheckpointUpdatedExecutionStateTypeDef",
    "CodeSigningConfigTypeDef",
    "CodeSigningPoliciesTypeDef",
    "ConcurrencyResponseTypeDef",
    "ConcurrencyTypeDef",
    "ContextDetailsTypeDef",
    "ContextFailedDetailsTypeDef",
    "ContextOptionsTypeDef",
    "ContextSucceededDetailsTypeDef",
    "CorsOutputTypeDef",
    "CorsTypeDef",
    "CorsUnionTypeDef",
    "CreateAliasRequestTypeDef",
    "CreateCapacityProviderRequestTypeDef",
    "CreateCapacityProviderResponseTypeDef",
    "CreateCodeSigningConfigRequestTypeDef",
    "CreateCodeSigningConfigResponseTypeDef",
    "CreateEventSourceMappingRequestTypeDef",
    "CreateFunctionRequestTypeDef",
    "CreateFunctionUrlConfigRequestTypeDef",
    "CreateFunctionUrlConfigResponseTypeDef",
    "DeadLetterConfigTypeDef",
    "DeleteAliasRequestTypeDef",
    "DeleteCapacityProviderRequestTypeDef",
    "DeleteCapacityProviderResponseTypeDef",
    "DeleteCodeSigningConfigRequestTypeDef",
    "DeleteEventSourceMappingRequestTypeDef",
    "DeleteFunctionCodeSigningConfigRequestTypeDef",
    "DeleteFunctionConcurrencyRequestTypeDef",
    "DeleteFunctionEventInvokeConfigRequestTypeDef",
    "DeleteFunctionRequestTypeDef",
    "DeleteFunctionResponseTypeDef",
    "DeleteFunctionUrlConfigRequestTypeDef",
    "DeleteLayerVersionRequestTypeDef",
    "DeleteProvisionedConcurrencyConfigRequestTypeDef",
    "DestinationConfigTypeDef",
    "DocumentDBEventSourceConfigTypeDef",
    "DurableConfigTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnvironmentErrorTypeDef",
    "EnvironmentResponseTypeDef",
    "EnvironmentTypeDef",
    "EphemeralStorageTypeDef",
    "ErrorObjectOutputTypeDef",
    "ErrorObjectTypeDef",
    "ErrorObjectUnionTypeDef",
    "EventErrorTypeDef",
    "EventInputTypeDef",
    "EventResultTypeDef",
    "EventSourceMappingConfigurationResponseTypeDef",
    "EventSourceMappingConfigurationTypeDef",
    "EventSourceMappingMetricsConfigOutputTypeDef",
    "EventSourceMappingMetricsConfigTypeDef",
    "EventSourceMappingMetricsConfigUnionTypeDef",
    "EventTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionFailedDetailsTypeDef",
    "ExecutionStartedDetailsTypeDef",
    "ExecutionStoppedDetailsTypeDef",
    "ExecutionSucceededDetailsTypeDef",
    "ExecutionTimedOutDetailsTypeDef",
    "ExecutionTypeDef",
    "FileSystemConfigTypeDef",
    "FilterCriteriaErrorTypeDef",
    "FilterCriteriaOutputTypeDef",
    "FilterCriteriaTypeDef",
    "FilterCriteriaUnionTypeDef",
    "FilterTypeDef",
    "FunctionCodeLocationTypeDef",
    "FunctionCodeTypeDef",
    "FunctionConfigurationResponseTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionEventInvokeConfigResponseTypeDef",
    "FunctionEventInvokeConfigTypeDef",
    "FunctionScalingConfigTypeDef",
    "FunctionUrlConfigTypeDef",
    "FunctionVersionsByCapacityProviderListItemTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetAliasRequestTypeDef",
    "GetCapacityProviderRequestTypeDef",
    "GetCapacityProviderResponseTypeDef",
    "GetCodeSigningConfigRequestTypeDef",
    "GetCodeSigningConfigResponseTypeDef",
    "GetDurableExecutionHistoryRequestPaginateTypeDef",
    "GetDurableExecutionHistoryRequestTypeDef",
    "GetDurableExecutionHistoryResponseTypeDef",
    "GetDurableExecutionRequestTypeDef",
    "GetDurableExecutionResponseTypeDef",
    "GetDurableExecutionStateRequestPaginateTypeDef",
    "GetDurableExecutionStateRequestTypeDef",
    "GetDurableExecutionStateResponseTypeDef",
    "GetEventSourceMappingRequestTypeDef",
    "GetFunctionCodeSigningConfigRequestTypeDef",
    "GetFunctionCodeSigningConfigResponseTypeDef",
    "GetFunctionConcurrencyRequestTypeDef",
    "GetFunctionConcurrencyResponseTypeDef",
    "GetFunctionConfigurationRequestTypeDef",
    "GetFunctionConfigurationRequestWaitExtraExtraTypeDef",
    "GetFunctionConfigurationRequestWaitExtraTypeDef",
    "GetFunctionConfigurationRequestWaitTypeDef",
    "GetFunctionEventInvokeConfigRequestTypeDef",
    "GetFunctionRecursionConfigRequestTypeDef",
    "GetFunctionRecursionConfigResponseTypeDef",
    "GetFunctionRequestTypeDef",
    "GetFunctionRequestWaitExtraExtraTypeDef",
    "GetFunctionRequestWaitExtraTypeDef",
    "GetFunctionRequestWaitTypeDef",
    "GetFunctionResponseTypeDef",
    "GetFunctionScalingConfigRequestTypeDef",
    "GetFunctionScalingConfigResponseTypeDef",
    "GetFunctionUrlConfigRequestTypeDef",
    "GetFunctionUrlConfigResponseTypeDef",
    "GetLayerVersionByArnRequestTypeDef",
    "GetLayerVersionPolicyRequestTypeDef",
    "GetLayerVersionPolicyResponseTypeDef",
    "GetLayerVersionRequestTypeDef",
    "GetLayerVersionResponseTypeDef",
    "GetPolicyRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProvisionedConcurrencyConfigRequestTypeDef",
    "GetProvisionedConcurrencyConfigResponseTypeDef",
    "GetRuntimeManagementConfigRequestTypeDef",
    "GetRuntimeManagementConfigResponseTypeDef",
    "ImageConfigErrorTypeDef",
    "ImageConfigOutputTypeDef",
    "ImageConfigResponseTypeDef",
    "ImageConfigTypeDef",
    "ImageConfigUnionTypeDef",
    "InstanceRequirementsOutputTypeDef",
    "InstanceRequirementsTypeDef",
    "InstanceRequirementsUnionTypeDef",
    "InvocationCompletedDetailsTypeDef",
    "InvocationRequestTypeDef",
    "InvocationResponseTypeDef",
    "InvokeAsyncRequestTypeDef",
    "InvokeAsyncResponseTypeDef",
    "InvokeResponseStreamUpdateTypeDef",
    "InvokeWithResponseStreamCompleteEventTypeDef",
    "InvokeWithResponseStreamRequestTypeDef",
    "InvokeWithResponseStreamResponseEventTypeDef",
    "InvokeWithResponseStreamResponseTypeDef",
    "KafkaSchemaRegistryAccessConfigTypeDef",
    "KafkaSchemaRegistryConfigOutputTypeDef",
    "KafkaSchemaRegistryConfigTypeDef",
    "KafkaSchemaValidationConfigTypeDef",
    "LambdaManagedInstancesCapacityProviderConfigTypeDef",
    "LayerTypeDef",
    "LayerVersionContentInputTypeDef",
    "LayerVersionContentOutputTypeDef",
    "LayerVersionsListItemTypeDef",
    "LayersListItemTypeDef",
    "ListAliasesRequestPaginateTypeDef",
    "ListAliasesRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListCapacityProvidersRequestPaginateTypeDef",
    "ListCapacityProvidersRequestTypeDef",
    "ListCapacityProvidersResponseTypeDef",
    "ListCodeSigningConfigsRequestPaginateTypeDef",
    "ListCodeSigningConfigsRequestTypeDef",
    "ListCodeSigningConfigsResponseTypeDef",
    "ListDurableExecutionsByFunctionRequestPaginateTypeDef",
    "ListDurableExecutionsByFunctionRequestTypeDef",
    "ListDurableExecutionsByFunctionResponseTypeDef",
    "ListEventSourceMappingsRequestPaginateTypeDef",
    "ListEventSourceMappingsRequestTypeDef",
    "ListEventSourceMappingsResponseTypeDef",
    "ListFunctionEventInvokeConfigsRequestPaginateTypeDef",
    "ListFunctionEventInvokeConfigsRequestTypeDef",
    "ListFunctionEventInvokeConfigsResponseTypeDef",
    "ListFunctionUrlConfigsRequestPaginateTypeDef",
    "ListFunctionUrlConfigsRequestTypeDef",
    "ListFunctionUrlConfigsResponseTypeDef",
    "ListFunctionVersionsByCapacityProviderRequestPaginateTypeDef",
    "ListFunctionVersionsByCapacityProviderRequestTypeDef",
    "ListFunctionVersionsByCapacityProviderResponseTypeDef",
    "ListFunctionsByCodeSigningConfigRequestPaginateTypeDef",
    "ListFunctionsByCodeSigningConfigRequestTypeDef",
    "ListFunctionsByCodeSigningConfigResponseTypeDef",
    "ListFunctionsRequestPaginateTypeDef",
    "ListFunctionsRequestTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListLayerVersionsRequestPaginateTypeDef",
    "ListLayerVersionsRequestTypeDef",
    "ListLayerVersionsResponseTypeDef",
    "ListLayersRequestPaginateTypeDef",
    "ListLayersRequestTypeDef",
    "ListLayersResponseTypeDef",
    "ListProvisionedConcurrencyConfigsRequestPaginateTypeDef",
    "ListProvisionedConcurrencyConfigsRequestTypeDef",
    "ListProvisionedConcurrencyConfigsResponseTypeDef",
    "ListTagsRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListVersionsByFunctionRequestPaginateTypeDef",
    "ListVersionsByFunctionRequestTypeDef",
    "ListVersionsByFunctionResponseTypeDef",
    "LoggingConfigTypeDef",
    "OnFailureTypeDef",
    "OnSuccessTypeDef",
    "OperationTypeDef",
    "OperationUpdateTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedConcurrencyConfigListItemTypeDef",
    "ProvisionedPollerConfigTypeDef",
    "PublishLayerVersionRequestTypeDef",
    "PublishLayerVersionResponseTypeDef",
    "PublishVersionRequestTypeDef",
    "PutFunctionCodeSigningConfigRequestTypeDef",
    "PutFunctionCodeSigningConfigResponseTypeDef",
    "PutFunctionConcurrencyRequestTypeDef",
    "PutFunctionEventInvokeConfigRequestTypeDef",
    "PutFunctionRecursionConfigRequestTypeDef",
    "PutFunctionRecursionConfigResponseTypeDef",
    "PutFunctionScalingConfigRequestTypeDef",
    "PutFunctionScalingConfigResponseTypeDef",
    "PutProvisionedConcurrencyConfigRequestTypeDef",
    "PutProvisionedConcurrencyConfigResponseTypeDef",
    "PutRuntimeManagementConfigRequestTypeDef",
    "PutRuntimeManagementConfigResponseTypeDef",
    "RemoveLayerVersionPermissionRequestTypeDef",
    "RemovePermissionRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RetryDetailsTypeDef",
    "RuntimeVersionConfigTypeDef",
    "RuntimeVersionErrorTypeDef",
    "ScalingConfigTypeDef",
    "SelfManagedEventSourceOutputTypeDef",
    "SelfManagedEventSourceTypeDef",
    "SelfManagedEventSourceUnionTypeDef",
    "SelfManagedKafkaEventSourceConfigOutputTypeDef",
    "SelfManagedKafkaEventSourceConfigTypeDef",
    "SelfManagedKafkaEventSourceConfigUnionTypeDef",
    "SendDurableExecutionCallbackFailureRequestTypeDef",
    "SendDurableExecutionCallbackHeartbeatRequestTypeDef",
    "SendDurableExecutionCallbackSuccessRequestTypeDef",
    "SnapStartResponseTypeDef",
    "SnapStartTypeDef",
    "SourceAccessConfigurationTypeDef",
    "StepDetailsTypeDef",
    "StepFailedDetailsTypeDef",
    "StepOptionsTypeDef",
    "StepSucceededDetailsTypeDef",
    "StopDurableExecutionRequestTypeDef",
    "StopDurableExecutionResponseTypeDef",
    "TagResourceRequestTypeDef",
    "TagsErrorTypeDef",
    "TargetTrackingScalingPolicyTypeDef",
    "TenancyConfigTypeDef",
    "TimestampTypeDef",
    "TraceHeaderTypeDef",
    "TracingConfigResponseTypeDef",
    "TracingConfigTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAliasRequestTypeDef",
    "UpdateCapacityProviderRequestTypeDef",
    "UpdateCapacityProviderResponseTypeDef",
    "UpdateCodeSigningConfigRequestTypeDef",
    "UpdateCodeSigningConfigResponseTypeDef",
    "UpdateEventSourceMappingRequestTypeDef",
    "UpdateFunctionCodeRequestTypeDef",
    "UpdateFunctionConfigurationRequestTypeDef",
    "UpdateFunctionEventInvokeConfigRequestTypeDef",
    "UpdateFunctionUrlConfigRequestTypeDef",
    "UpdateFunctionUrlConfigResponseTypeDef",
    "VpcConfigResponseTypeDef",
    "VpcConfigTypeDef",
    "WaitCancelledDetailsTypeDef",
    "WaitDetailsTypeDef",
    "WaitOptionsTypeDef",
    "WaitStartedDetailsTypeDef",
    "WaitSucceededDetailsTypeDef",
    "WaiterConfigTypeDef",
)

class AccountLimitTypeDef(TypedDict):
    TotalCodeSize: NotRequired[int]
    CodeSizeUnzipped: NotRequired[int]
    CodeSizeZipped: NotRequired[int]
    ConcurrentExecutions: NotRequired[int]
    UnreservedConcurrentExecutions: NotRequired[int]

class AccountUsageTypeDef(TypedDict):
    TotalCodeSize: NotRequired[int]
    FunctionCount: NotRequired[int]

class AddLayerVersionPermissionRequestTypeDef(TypedDict):
    LayerName: str
    VersionNumber: int
    StatementId: str
    Action: str
    Principal: str
    OrganizationId: NotRequired[str]
    RevisionId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AddPermissionRequestTypeDef(TypedDict):
    FunctionName: str
    StatementId: str
    Action: str
    Principal: str
    SourceArn: NotRequired[str]
    SourceAccount: NotRequired[str]
    EventSourceToken: NotRequired[str]
    Qualifier: NotRequired[str]
    RevisionId: NotRequired[str]
    PrincipalOrgID: NotRequired[str]
    FunctionUrlAuthType: NotRequired[FunctionUrlAuthTypeType]
    InvokedViaFunctionUrl: NotRequired[bool]

class AliasRoutingConfigurationOutputTypeDef(TypedDict):
    AdditionalVersionWeights: NotRequired[Dict[str, float]]

class AliasRoutingConfigurationTypeDef(TypedDict):
    AdditionalVersionWeights: NotRequired[Mapping[str, float]]

class AllowedPublishersOutputTypeDef(TypedDict):
    SigningProfileVersionArns: List[str]

class AllowedPublishersTypeDef(TypedDict):
    SigningProfileVersionArns: Sequence[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class ErrorObjectOutputTypeDef(TypedDict):
    ErrorMessage: NotRequired[str]
    ErrorType: NotRequired[str]
    ErrorData: NotRequired[str]
    StackTrace: NotRequired[List[str]]

class CallbackOptionsTypeDef(TypedDict):
    TimeoutSeconds: NotRequired[int]
    HeartbeatTimeoutSeconds: NotRequired[int]

class CallbackStartedDetailsTypeDef(TypedDict):
    CallbackId: str
    HeartbeatTimeout: NotRequired[int]
    Timeout: NotRequired[int]

class EventResultTypeDef(TypedDict):
    Payload: NotRequired[str]
    Truncated: NotRequired[bool]

class LambdaManagedInstancesCapacityProviderConfigTypeDef(TypedDict):
    CapacityProviderArn: str
    PerExecutionEnvironmentMaxConcurrency: NotRequired[int]
    ExecutionEnvironmentMemoryGiBPerVCpu: NotRequired[float]

class CapacityProviderPermissionsConfigTypeDef(TypedDict):
    CapacityProviderOperatorRoleArn: str

class TargetTrackingScalingPolicyTypeDef(TypedDict):
    PredefinedMetricType: Literal["LambdaCapacityProviderAverageCPUUtilization"]
    TargetValue: float

class CapacityProviderVpcConfigOutputTypeDef(TypedDict):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]

class InstanceRequirementsOutputTypeDef(TypedDict):
    Architectures: NotRequired[List[ArchitectureType]]
    AllowedInstanceTypes: NotRequired[List[str]]
    ExcludedInstanceTypes: NotRequired[List[str]]

class CapacityProviderVpcConfigTypeDef(TypedDict):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Sequence[str]

class ChainedInvokeOptionsTypeDef(TypedDict):
    FunctionName: str
    TenantId: NotRequired[str]

class EventInputTypeDef(TypedDict):
    Payload: NotRequired[str]
    Truncated: NotRequired[bool]

class CodeSigningPoliciesTypeDef(TypedDict):
    UntrustedArtifactOnDeployment: NotRequired[CodeSigningPolicyType]

class ConcurrencyTypeDef(TypedDict):
    ReservedConcurrentExecutions: NotRequired[int]

class ContextOptionsTypeDef(TypedDict):
    ReplayChildren: NotRequired[bool]

class CorsOutputTypeDef(TypedDict):
    AllowCredentials: NotRequired[bool]
    AllowHeaders: NotRequired[List[str]]
    AllowMethods: NotRequired[List[str]]
    AllowOrigins: NotRequired[List[str]]
    ExposeHeaders: NotRequired[List[str]]
    MaxAge: NotRequired[int]

class CorsTypeDef(TypedDict):
    AllowCredentials: NotRequired[bool]
    AllowHeaders: NotRequired[Sequence[str]]
    AllowMethods: NotRequired[Sequence[str]]
    AllowOrigins: NotRequired[Sequence[str]]
    ExposeHeaders: NotRequired[Sequence[str]]
    MaxAge: NotRequired[int]

class DocumentDBEventSourceConfigTypeDef(TypedDict):
    DatabaseName: NotRequired[str]
    CollectionName: NotRequired[str]
    FullDocument: NotRequired[FullDocumentType]

class ProvisionedPollerConfigTypeDef(TypedDict):
    MinimumPollers: NotRequired[int]
    MaximumPollers: NotRequired[int]
    PollerGroupName: NotRequired[str]

class ScalingConfigTypeDef(TypedDict):
    MaximumConcurrency: NotRequired[int]

SourceAccessConfigurationTypeDef = TypedDict(
    "SourceAccessConfigurationTypeDef",
    {
        "Type": NotRequired[SourceAccessTypeType],
        "URI": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]

class DeadLetterConfigTypeDef(TypedDict):
    TargetArn: NotRequired[str]

class DurableConfigTypeDef(TypedDict):
    RetentionPeriodInDays: NotRequired[int]
    ExecutionTimeout: NotRequired[int]

class EnvironmentTypeDef(TypedDict):
    Variables: NotRequired[Mapping[str, str]]

class EphemeralStorageTypeDef(TypedDict):
    Size: int

class FileSystemConfigTypeDef(TypedDict):
    Arn: str
    LocalMountPath: str

class LoggingConfigTypeDef(TypedDict):
    LogFormat: NotRequired[LogFormatType]
    ApplicationLogLevel: NotRequired[ApplicationLogLevelType]
    SystemLogLevel: NotRequired[SystemLogLevelType]
    LogGroup: NotRequired[str]

class SnapStartTypeDef(TypedDict):
    ApplyOn: NotRequired[SnapStartApplyOnType]

class TenancyConfigTypeDef(TypedDict):
    TenantIsolationMode: Literal["PER_TENANT"]

class TracingConfigTypeDef(TypedDict):
    Mode: NotRequired[TracingModeType]

class VpcConfigTypeDef(TypedDict):
    SubnetIds: NotRequired[Sequence[str]]
    SecurityGroupIds: NotRequired[Sequence[str]]
    Ipv6AllowedForDualStack: NotRequired[bool]

class DeleteAliasRequestTypeDef(TypedDict):
    FunctionName: str
    Name: str

class DeleteCapacityProviderRequestTypeDef(TypedDict):
    CapacityProviderName: str

class DeleteCodeSigningConfigRequestTypeDef(TypedDict):
    CodeSigningConfigArn: str

class DeleteEventSourceMappingRequestTypeDef(TypedDict):
    UUID: str

class DeleteFunctionCodeSigningConfigRequestTypeDef(TypedDict):
    FunctionName: str

class DeleteFunctionConcurrencyRequestTypeDef(TypedDict):
    FunctionName: str

class DeleteFunctionEventInvokeConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class DeleteFunctionRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class DeleteFunctionUrlConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class DeleteLayerVersionRequestTypeDef(TypedDict):
    LayerName: str
    VersionNumber: int

class DeleteProvisionedConcurrencyConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: str

class OnFailureTypeDef(TypedDict):
    Destination: NotRequired[str]

class OnSuccessTypeDef(TypedDict):
    Destination: NotRequired[str]

class EnvironmentErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    Message: NotRequired[str]

class ErrorObjectTypeDef(TypedDict):
    ErrorMessage: NotRequired[str]
    ErrorType: NotRequired[str]
    ErrorData: NotRequired[str]
    StackTrace: NotRequired[Sequence[str]]

class EventSourceMappingMetricsConfigOutputTypeDef(TypedDict):
    Metrics: NotRequired[List[Literal["EventCount"]]]

class FilterCriteriaErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    Message: NotRequired[str]

class SelfManagedEventSourceOutputTypeDef(TypedDict):
    Endpoints: NotRequired[Dict[Literal["KAFKA_BOOTSTRAP_SERVERS"], List[str]]]

class EventSourceMappingMetricsConfigTypeDef(TypedDict):
    Metrics: NotRequired[Sequence[Literal["EventCount"]]]

class WaitStartedDetailsTypeDef(TypedDict):
    Duration: int
    ScheduledEndTimestamp: datetime

class WaitSucceededDetailsTypeDef(TypedDict):
    Duration: NotRequired[int]

class ExecutionDetailsTypeDef(TypedDict):
    InputPayload: NotRequired[str]

class ExecutionTypeDef(TypedDict):
    DurableExecutionArn: str
    DurableExecutionName: str
    FunctionArn: str
    Status: ExecutionStatusType
    StartTimestamp: datetime
    EndTimestamp: NotRequired[datetime]

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Pattern": NotRequired[str],
    },
)

class FunctionCodeLocationTypeDef(TypedDict):
    RepositoryType: NotRequired[str]
    Location: NotRequired[str]
    ImageUri: NotRequired[str]
    ResolvedImageUri: NotRequired[str]
    SourceKMSKeyArn: NotRequired[str]

class LayerTypeDef(TypedDict):
    Arn: NotRequired[str]
    CodeSize: NotRequired[int]
    SigningProfileVersionArn: NotRequired[str]
    SigningJobArn: NotRequired[str]

class SnapStartResponseTypeDef(TypedDict):
    ApplyOn: NotRequired[SnapStartApplyOnType]
    OptimizationStatus: NotRequired[SnapStartOptimizationStatusType]

class TracingConfigResponseTypeDef(TypedDict):
    Mode: NotRequired[TracingModeType]

class VpcConfigResponseTypeDef(TypedDict):
    SubnetIds: NotRequired[List[str]]
    SecurityGroupIds: NotRequired[List[str]]
    VpcId: NotRequired[str]
    Ipv6AllowedForDualStack: NotRequired[bool]

class FunctionScalingConfigTypeDef(TypedDict):
    MinExecutionEnvironments: NotRequired[int]
    MaxExecutionEnvironments: NotRequired[int]

class FunctionVersionsByCapacityProviderListItemTypeDef(TypedDict):
    FunctionArn: str
    State: StateType

class GetAliasRequestTypeDef(TypedDict):
    FunctionName: str
    Name: str

class GetCapacityProviderRequestTypeDef(TypedDict):
    CapacityProviderName: str

class GetCodeSigningConfigRequestTypeDef(TypedDict):
    CodeSigningConfigArn: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetDurableExecutionHistoryRequestTypeDef(TypedDict):
    DurableExecutionArn: str
    IncludeExecutionData: NotRequired[bool]
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]
    ReverseOrder: NotRequired[bool]

class GetDurableExecutionRequestTypeDef(TypedDict):
    DurableExecutionArn: str

class TraceHeaderTypeDef(TypedDict):
    XAmznTraceId: NotRequired[str]

class GetDurableExecutionStateRequestTypeDef(TypedDict):
    DurableExecutionArn: str
    CheckpointToken: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class GetEventSourceMappingRequestTypeDef(TypedDict):
    UUID: str

class GetFunctionCodeSigningConfigRequestTypeDef(TypedDict):
    FunctionName: str

class GetFunctionConcurrencyRequestTypeDef(TypedDict):
    FunctionName: str

class GetFunctionConfigurationRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class GetFunctionEventInvokeConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class GetFunctionRecursionConfigRequestTypeDef(TypedDict):
    FunctionName: str

class GetFunctionRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class TagsErrorTypeDef(TypedDict):
    ErrorCode: str
    Message: str

class GetFunctionScalingConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: str

class GetFunctionUrlConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class GetLayerVersionByArnRequestTypeDef(TypedDict):
    Arn: str

class GetLayerVersionPolicyRequestTypeDef(TypedDict):
    LayerName: str
    VersionNumber: int

class GetLayerVersionRequestTypeDef(TypedDict):
    LayerName: str
    VersionNumber: int

class LayerVersionContentOutputTypeDef(TypedDict):
    Location: NotRequired[str]
    CodeSha256: NotRequired[str]
    CodeSize: NotRequired[int]
    SigningProfileVersionArn: NotRequired[str]
    SigningJobArn: NotRequired[str]

class GetPolicyRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class GetProvisionedConcurrencyConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: str

class GetRuntimeManagementConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]

class ImageConfigErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    Message: NotRequired[str]

class ImageConfigOutputTypeDef(TypedDict):
    EntryPoint: NotRequired[List[str]]
    Command: NotRequired[List[str]]
    WorkingDirectory: NotRequired[str]

class ImageConfigTypeDef(TypedDict):
    EntryPoint: NotRequired[Sequence[str]]
    Command: NotRequired[Sequence[str]]
    WorkingDirectory: NotRequired[str]

class InstanceRequirementsTypeDef(TypedDict):
    Architectures: NotRequired[Sequence[ArchitectureType]]
    AllowedInstanceTypes: NotRequired[Sequence[str]]
    ExcludedInstanceTypes: NotRequired[Sequence[str]]

class InvokeResponseStreamUpdateTypeDef(TypedDict):
    Payload: NotRequired[bytes]

class InvokeWithResponseStreamCompleteEventTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorDetails: NotRequired[str]
    LogResult: NotRequired[str]

KafkaSchemaRegistryAccessConfigTypeDef = TypedDict(
    "KafkaSchemaRegistryAccessConfigTypeDef",
    {
        "Type": NotRequired[KafkaSchemaRegistryAuthTypeType],
        "URI": NotRequired[str],
    },
)

class KafkaSchemaValidationConfigTypeDef(TypedDict):
    Attribute: NotRequired[KafkaSchemaValidationAttributeType]

class LayerVersionsListItemTypeDef(TypedDict):
    LayerVersionArn: NotRequired[str]
    Version: NotRequired[int]
    Description: NotRequired[str]
    CreatedDate: NotRequired[str]
    CompatibleRuntimes: NotRequired[List[RuntimeType]]
    LicenseInfo: NotRequired[str]
    CompatibleArchitectures: NotRequired[List[ArchitectureType]]

class ListAliasesRequestTypeDef(TypedDict):
    FunctionName: str
    FunctionVersion: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListCapacityProvidersRequestTypeDef(TypedDict):
    State: NotRequired[CapacityProviderStateType]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListCodeSigningConfigsRequestTypeDef(TypedDict):
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListEventSourceMappingsRequestTypeDef(TypedDict):
    EventSourceArn: NotRequired[str]
    FunctionName: NotRequired[str]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListFunctionEventInvokeConfigsRequestTypeDef(TypedDict):
    FunctionName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListFunctionUrlConfigsRequestTypeDef(TypedDict):
    FunctionName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListFunctionVersionsByCapacityProviderRequestTypeDef(TypedDict):
    CapacityProviderName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListFunctionsByCodeSigningConfigRequestTypeDef(TypedDict):
    CodeSigningConfigArn: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListFunctionsRequestTypeDef(TypedDict):
    MasterRegion: NotRequired[str]
    FunctionVersion: NotRequired[Literal["ALL"]]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ListLayerVersionsRequestTypeDef(TypedDict):
    LayerName: str
    CompatibleRuntime: NotRequired[RuntimeType]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]
    CompatibleArchitecture: NotRequired[ArchitectureType]

class ListLayersRequestTypeDef(TypedDict):
    CompatibleRuntime: NotRequired[RuntimeType]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]
    CompatibleArchitecture: NotRequired[ArchitectureType]

class ListProvisionedConcurrencyConfigsRequestTypeDef(TypedDict):
    FunctionName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class ProvisionedConcurrencyConfigListItemTypeDef(TypedDict):
    FunctionArn: NotRequired[str]
    RequestedProvisionedConcurrentExecutions: NotRequired[int]
    AvailableProvisionedConcurrentExecutions: NotRequired[int]
    AllocatedProvisionedConcurrentExecutions: NotRequired[int]
    Status: NotRequired[ProvisionedConcurrencyStatusEnumType]
    StatusReason: NotRequired[str]
    LastModified: NotRequired[str]

class ListTagsRequestTypeDef(TypedDict):
    Resource: str

class ListVersionsByFunctionRequestTypeDef(TypedDict):
    FunctionName: str
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class WaitDetailsTypeDef(TypedDict):
    ScheduledEndTimestamp: NotRequired[datetime]

class StepOptionsTypeDef(TypedDict):
    NextAttemptDelaySeconds: NotRequired[int]

class WaitOptionsTypeDef(TypedDict):
    WaitSeconds: NotRequired[int]

class PublishVersionRequestTypeDef(TypedDict):
    FunctionName: str
    CodeSha256: NotRequired[str]
    Description: NotRequired[str]
    RevisionId: NotRequired[str]
    PublishTo: NotRequired[Literal["LATEST_PUBLISHED"]]

class PutFunctionCodeSigningConfigRequestTypeDef(TypedDict):
    CodeSigningConfigArn: str
    FunctionName: str

class PutFunctionConcurrencyRequestTypeDef(TypedDict):
    FunctionName: str
    ReservedConcurrentExecutions: int

class PutFunctionRecursionConfigRequestTypeDef(TypedDict):
    FunctionName: str
    RecursiveLoop: RecursiveLoopType

class PutProvisionedConcurrencyConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: str
    ProvisionedConcurrentExecutions: int

class PutRuntimeManagementConfigRequestTypeDef(TypedDict):
    FunctionName: str
    UpdateRuntimeOn: UpdateRuntimeOnType
    Qualifier: NotRequired[str]
    RuntimeVersionArn: NotRequired[str]

class RemoveLayerVersionPermissionRequestTypeDef(TypedDict):
    LayerName: str
    VersionNumber: int
    StatementId: str
    RevisionId: NotRequired[str]

class RemovePermissionRequestTypeDef(TypedDict):
    FunctionName: str
    StatementId: str
    Qualifier: NotRequired[str]
    RevisionId: NotRequired[str]

class RetryDetailsTypeDef(TypedDict):
    CurrentAttempt: NotRequired[int]
    NextAttemptDelaySeconds: NotRequired[int]

class RuntimeVersionErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    Message: NotRequired[str]

class SelfManagedEventSourceTypeDef(TypedDict):
    Endpoints: NotRequired[Mapping[Literal["KAFKA_BOOTSTRAP_SERVERS"], Sequence[str]]]

class SendDurableExecutionCallbackHeartbeatRequestTypeDef(TypedDict):
    CallbackId: str

class TagResourceRequestTypeDef(TypedDict):
    Resource: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    Resource: str
    TagKeys: Sequence[str]

class AddLayerVersionPermissionResponseTypeDef(TypedDict):
    Statement: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddPermissionResponseTypeDef(TypedDict):
    Statement: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConcurrencyResponseTypeDef(TypedDict):
    ReservedConcurrentExecutions: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFunctionResponseTypeDef(TypedDict):
    StatusCode: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsResponseTypeDef(TypedDict):
    AccountLimit: AccountLimitTypeDef
    AccountUsage: AccountUsageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfigArn: str
    FunctionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionConcurrencyResponseTypeDef(TypedDict):
    ReservedConcurrentExecutions: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionRecursionConfigResponseTypeDef(TypedDict):
    RecursiveLoop: RecursiveLoopType
    ResponseMetadata: ResponseMetadataTypeDef

class GetLayerVersionPolicyResponseTypeDef(TypedDict):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPolicyResponseTypeDef(TypedDict):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProvisionedConcurrencyConfigResponseTypeDef(TypedDict):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnumType
    StatusReason: str
    LastModified: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuntimeManagementConfigResponseTypeDef(TypedDict):
    UpdateRuntimeOn: UpdateRuntimeOnType
    RuntimeVersionArn: str
    FunctionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvocationResponseTypeDef(TypedDict):
    StatusCode: int
    FunctionError: str
    LogResult: str
    Payload: StreamingBody
    ExecutedVersion: str
    DurableExecutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class InvokeAsyncResponseTypeDef(TypedDict):
    Status: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsByCodeSigningConfigResponseTypeDef(TypedDict):
    NextMarker: str
    FunctionArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutFunctionCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfigArn: str
    FunctionName: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutFunctionRecursionConfigResponseTypeDef(TypedDict):
    RecursiveLoop: RecursiveLoopType
    ResponseMetadata: ResponseMetadataTypeDef

class PutFunctionScalingConfigResponseTypeDef(TypedDict):
    FunctionState: StateType
    ResponseMetadata: ResponseMetadataTypeDef

class PutProvisionedConcurrencyConfigResponseTypeDef(TypedDict):
    RequestedProvisionedConcurrentExecutions: int
    AvailableProvisionedConcurrentExecutions: int
    AllocatedProvisionedConcurrentExecutions: int
    Status: ProvisionedConcurrencyStatusEnumType
    StatusReason: str
    LastModified: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutRuntimeManagementConfigResponseTypeDef(TypedDict):
    UpdateRuntimeOn: UpdateRuntimeOnType
    FunctionArn: str
    RuntimeVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopDurableExecutionResponseTypeDef(TypedDict):
    StopTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class AliasConfigurationResponseTypeDef(TypedDict):
    AliasArn: str
    Name: str
    FunctionVersion: str
    Description: str
    RoutingConfig: AliasRoutingConfigurationOutputTypeDef
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AliasConfigurationTypeDef(TypedDict):
    AliasArn: NotRequired[str]
    Name: NotRequired[str]
    FunctionVersion: NotRequired[str]
    Description: NotRequired[str]
    RoutingConfig: NotRequired[AliasRoutingConfigurationOutputTypeDef]
    RevisionId: NotRequired[str]

AliasRoutingConfigurationUnionTypeDef = Union[
    AliasRoutingConfigurationTypeDef, AliasRoutingConfigurationOutputTypeDef
]
AllowedPublishersUnionTypeDef = Union[AllowedPublishersTypeDef, AllowedPublishersOutputTypeDef]

class FunctionCodeTypeDef(TypedDict):
    ZipFile: NotRequired[BlobTypeDef]
    S3Bucket: NotRequired[str]
    S3Key: NotRequired[str]
    S3ObjectVersion: NotRequired[str]
    ImageUri: NotRequired[str]
    SourceKMSKeyArn: NotRequired[str]

class InvocationRequestTypeDef(TypedDict):
    FunctionName: str
    InvocationType: NotRequired[InvocationTypeType]
    LogType: NotRequired[LogTypeType]
    ClientContext: NotRequired[str]
    DurableExecutionName: NotRequired[str]
    Payload: NotRequired[BlobTypeDef]
    Qualifier: NotRequired[str]
    TenantId: NotRequired[str]

class InvokeAsyncRequestTypeDef(TypedDict):
    FunctionName: str
    InvokeArgs: BlobTypeDef

class InvokeWithResponseStreamRequestTypeDef(TypedDict):
    FunctionName: str
    InvocationType: NotRequired[ResponseStreamingInvocationTypeType]
    LogType: NotRequired[LogTypeType]
    ClientContext: NotRequired[str]
    Qualifier: NotRequired[str]
    Payload: NotRequired[BlobTypeDef]
    TenantId: NotRequired[str]

class LayerVersionContentInputTypeDef(TypedDict):
    S3Bucket: NotRequired[str]
    S3Key: NotRequired[str]
    S3ObjectVersion: NotRequired[str]
    ZipFile: NotRequired[BlobTypeDef]

class SendDurableExecutionCallbackSuccessRequestTypeDef(TypedDict):
    CallbackId: str
    Result: NotRequired[BlobTypeDef]

class UpdateFunctionCodeRequestTypeDef(TypedDict):
    FunctionName: str
    ZipFile: NotRequired[BlobTypeDef]
    S3Bucket: NotRequired[str]
    S3Key: NotRequired[str]
    S3ObjectVersion: NotRequired[str]
    ImageUri: NotRequired[str]
    Publish: NotRequired[bool]
    DryRun: NotRequired[bool]
    RevisionId: NotRequired[str]
    Architectures: NotRequired[Sequence[ArchitectureType]]
    SourceKMSKeyArn: NotRequired[str]
    PublishTo: NotRequired[Literal["LATEST_PUBLISHED"]]

class CallbackDetailsTypeDef(TypedDict):
    CallbackId: NotRequired[str]
    Result: NotRequired[str]
    Error: NotRequired[ErrorObjectOutputTypeDef]

class ChainedInvokeDetailsTypeDef(TypedDict):
    Result: NotRequired[str]
    Error: NotRequired[ErrorObjectOutputTypeDef]

class ContextDetailsTypeDef(TypedDict):
    ReplayChildren: NotRequired[bool]
    Result: NotRequired[str]
    Error: NotRequired[ErrorObjectOutputTypeDef]

class EventErrorTypeDef(TypedDict):
    Payload: NotRequired[ErrorObjectOutputTypeDef]
    Truncated: NotRequired[bool]

class StepDetailsTypeDef(TypedDict):
    Attempt: NotRequired[int]
    NextAttemptTimestamp: NotRequired[datetime]
    Result: NotRequired[str]
    Error: NotRequired[ErrorObjectOutputTypeDef]

class CallbackSucceededDetailsTypeDef(TypedDict):
    Result: EventResultTypeDef

class ChainedInvokeSucceededDetailsTypeDef(TypedDict):
    Result: EventResultTypeDef

class ContextSucceededDetailsTypeDef(TypedDict):
    Result: EventResultTypeDef

class ExecutionSucceededDetailsTypeDef(TypedDict):
    Result: EventResultTypeDef

class CapacityProviderConfigTypeDef(TypedDict):
    LambdaManagedInstancesCapacityProviderConfig: (
        LambdaManagedInstancesCapacityProviderConfigTypeDef
    )

class CapacityProviderScalingConfigOutputTypeDef(TypedDict):
    MaxVCpuCount: NotRequired[int]
    ScalingMode: NotRequired[CapacityProviderScalingModeType]
    ScalingPolicies: NotRequired[List[TargetTrackingScalingPolicyTypeDef]]

class CapacityProviderScalingConfigTypeDef(TypedDict):
    MaxVCpuCount: NotRequired[int]
    ScalingMode: NotRequired[CapacityProviderScalingModeType]
    ScalingPolicies: NotRequired[Sequence[TargetTrackingScalingPolicyTypeDef]]

CapacityProviderVpcConfigUnionTypeDef = Union[
    CapacityProviderVpcConfigTypeDef, CapacityProviderVpcConfigOutputTypeDef
]

class ChainedInvokeStartedDetailsTypeDef(TypedDict):
    FunctionName: str
    TenantId: NotRequired[str]
    Input: NotRequired[EventInputTypeDef]
    ExecutedVersion: NotRequired[str]
    DurableExecutionArn: NotRequired[str]

class ExecutionStartedDetailsTypeDef(TypedDict):
    Input: EventInputTypeDef
    ExecutionTimeout: int

class CodeSigningConfigTypeDef(TypedDict):
    CodeSigningConfigId: str
    CodeSigningConfigArn: str
    AllowedPublishers: AllowedPublishersOutputTypeDef
    CodeSigningPolicies: CodeSigningPoliciesTypeDef
    LastModified: str
    Description: NotRequired[str]

class CreateFunctionUrlConfigResponseTypeDef(TypedDict):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutputTypeDef
    CreationTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionUrlConfigTypeDef(TypedDict):
    FunctionUrl: str
    FunctionArn: str
    CreationTime: str
    LastModifiedTime: str
    AuthType: FunctionUrlAuthTypeType
    Cors: NotRequired[CorsOutputTypeDef]
    InvokeMode: NotRequired[InvokeModeType]

class GetFunctionUrlConfigResponseTypeDef(TypedDict):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutputTypeDef
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFunctionUrlConfigResponseTypeDef(TypedDict):
    FunctionUrl: str
    FunctionArn: str
    AuthType: FunctionUrlAuthTypeType
    Cors: CorsOutputTypeDef
    CreationTime: str
    LastModifiedTime: str
    InvokeMode: InvokeModeType
    ResponseMetadata: ResponseMetadataTypeDef

CorsUnionTypeDef = Union[CorsTypeDef, CorsOutputTypeDef]

class ListDurableExecutionsByFunctionRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    DurableExecutionName: NotRequired[str]
    Statuses: NotRequired[Sequence[ExecutionStatusType]]
    StartedAfter: NotRequired[TimestampTypeDef]
    StartedBefore: NotRequired[TimestampTypeDef]
    ReverseOrder: NotRequired[bool]
    Marker: NotRequired[str]
    MaxItems: NotRequired[int]

class DestinationConfigTypeDef(TypedDict):
    OnSuccess: NotRequired[OnSuccessTypeDef]
    OnFailure: NotRequired[OnFailureTypeDef]

class EnvironmentResponseTypeDef(TypedDict):
    Variables: NotRequired[Dict[str, str]]
    Error: NotRequired[EnvironmentErrorTypeDef]

ErrorObjectUnionTypeDef = Union[ErrorObjectTypeDef, ErrorObjectOutputTypeDef]
EventSourceMappingMetricsConfigUnionTypeDef = Union[
    EventSourceMappingMetricsConfigTypeDef, EventSourceMappingMetricsConfigOutputTypeDef
]

class ListDurableExecutionsByFunctionResponseTypeDef(TypedDict):
    DurableExecutions: List[ExecutionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class FilterCriteriaOutputTypeDef(TypedDict):
    Filters: NotRequired[List[FilterTypeDef]]

class FilterCriteriaTypeDef(TypedDict):
    Filters: NotRequired[Sequence[FilterTypeDef]]

class GetFunctionScalingConfigResponseTypeDef(TypedDict):
    FunctionArn: str
    AppliedFunctionScalingConfig: FunctionScalingConfigTypeDef
    RequestedFunctionScalingConfig: FunctionScalingConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutFunctionScalingConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: str
    FunctionScalingConfig: NotRequired[FunctionScalingConfigTypeDef]

class ListFunctionVersionsByCapacityProviderResponseTypeDef(TypedDict):
    CapacityProviderArn: str
    FunctionVersions: List[FunctionVersionsByCapacityProviderListItemTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDurableExecutionHistoryRequestPaginateTypeDef(TypedDict):
    DurableExecutionArn: str
    IncludeExecutionData: NotRequired[bool]
    ReverseOrder: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDurableExecutionStateRequestPaginateTypeDef(TypedDict):
    DurableExecutionArn: str
    CheckpointToken: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAliasesRequestPaginateTypeDef(TypedDict):
    FunctionName: str
    FunctionVersion: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCapacityProvidersRequestPaginateTypeDef(TypedDict):
    State: NotRequired[CapacityProviderStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCodeSigningConfigsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDurableExecutionsByFunctionRequestPaginateTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    DurableExecutionName: NotRequired[str]
    Statuses: NotRequired[Sequence[ExecutionStatusType]]
    StartedAfter: NotRequired[TimestampTypeDef]
    StartedBefore: NotRequired[TimestampTypeDef]
    ReverseOrder: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventSourceMappingsRequestPaginateTypeDef(TypedDict):
    EventSourceArn: NotRequired[str]
    FunctionName: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFunctionEventInvokeConfigsRequestPaginateTypeDef(TypedDict):
    FunctionName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFunctionUrlConfigsRequestPaginateTypeDef(TypedDict):
    FunctionName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFunctionVersionsByCapacityProviderRequestPaginateTypeDef(TypedDict):
    CapacityProviderName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFunctionsByCodeSigningConfigRequestPaginateTypeDef(TypedDict):
    CodeSigningConfigArn: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFunctionsRequestPaginateTypeDef(TypedDict):
    MasterRegion: NotRequired[str]
    FunctionVersion: NotRequired[Literal["ALL"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLayerVersionsRequestPaginateTypeDef(TypedDict):
    LayerName: str
    CompatibleRuntime: NotRequired[RuntimeType]
    CompatibleArchitecture: NotRequired[ArchitectureType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLayersRequestPaginateTypeDef(TypedDict):
    CompatibleRuntime: NotRequired[RuntimeType]
    CompatibleArchitecture: NotRequired[ArchitectureType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProvisionedConcurrencyConfigsRequestPaginateTypeDef(TypedDict):
    FunctionName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVersionsByFunctionRequestPaginateTypeDef(TypedDict):
    FunctionName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetDurableExecutionResponseTypeDef(TypedDict):
    DurableExecutionArn: str
    DurableExecutionName: str
    FunctionArn: str
    InputPayload: str
    Result: str
    Error: ErrorObjectOutputTypeDef
    StartTimestamp: datetime
    Status: ExecutionStatusType
    EndTimestamp: datetime
    Version: str
    TraceHeader: TraceHeaderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFunctionConfigurationRequestWaitExtraExtraTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetFunctionConfigurationRequestWaitExtraTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetFunctionConfigurationRequestWaitTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetFunctionRequestWaitExtraExtraTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetFunctionRequestWaitExtraTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetFunctionRequestWaitTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetLayerVersionResponseTypeDef(TypedDict):
    Content: LayerVersionContentOutputTypeDef
    LayerArn: str
    LayerVersionArn: str
    Description: str
    CreatedDate: str
    Version: int
    CompatibleRuntimes: List[RuntimeType]
    LicenseInfo: str
    CompatibleArchitectures: List[ArchitectureType]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishLayerVersionResponseTypeDef(TypedDict):
    Content: LayerVersionContentOutputTypeDef
    LayerArn: str
    LayerVersionArn: str
    Description: str
    CreatedDate: str
    Version: int
    CompatibleRuntimes: List[RuntimeType]
    LicenseInfo: str
    CompatibleArchitectures: List[ArchitectureType]
    ResponseMetadata: ResponseMetadataTypeDef

class ImageConfigResponseTypeDef(TypedDict):
    ImageConfig: NotRequired[ImageConfigOutputTypeDef]
    Error: NotRequired[ImageConfigErrorTypeDef]

ImageConfigUnionTypeDef = Union[ImageConfigTypeDef, ImageConfigOutputTypeDef]
InstanceRequirementsUnionTypeDef = Union[
    InstanceRequirementsTypeDef, InstanceRequirementsOutputTypeDef
]

class InvokeWithResponseStreamResponseEventTypeDef(TypedDict):
    PayloadChunk: NotRequired[InvokeResponseStreamUpdateTypeDef]
    InvokeComplete: NotRequired[InvokeWithResponseStreamCompleteEventTypeDef]

class KafkaSchemaRegistryConfigOutputTypeDef(TypedDict):
    SchemaRegistryURI: NotRequired[str]
    EventRecordFormat: NotRequired[SchemaRegistryEventRecordFormatType]
    AccessConfigs: NotRequired[List[KafkaSchemaRegistryAccessConfigTypeDef]]
    SchemaValidationConfigs: NotRequired[List[KafkaSchemaValidationConfigTypeDef]]

class KafkaSchemaRegistryConfigTypeDef(TypedDict):
    SchemaRegistryURI: NotRequired[str]
    EventRecordFormat: NotRequired[SchemaRegistryEventRecordFormatType]
    AccessConfigs: NotRequired[Sequence[KafkaSchemaRegistryAccessConfigTypeDef]]
    SchemaValidationConfigs: NotRequired[Sequence[KafkaSchemaValidationConfigTypeDef]]

class LayersListItemTypeDef(TypedDict):
    LayerName: NotRequired[str]
    LayerArn: NotRequired[str]
    LatestMatchingVersion: NotRequired[LayerVersionsListItemTypeDef]

class ListLayerVersionsResponseTypeDef(TypedDict):
    NextMarker: str
    LayerVersions: List[LayerVersionsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisionedConcurrencyConfigsResponseTypeDef(TypedDict):
    ProvisionedConcurrencyConfigs: List[ProvisionedConcurrencyConfigListItemTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class StepSucceededDetailsTypeDef(TypedDict):
    Result: EventResultTypeDef
    RetryDetails: RetryDetailsTypeDef

class RuntimeVersionConfigTypeDef(TypedDict):
    RuntimeVersionArn: NotRequired[str]
    Error: NotRequired[RuntimeVersionErrorTypeDef]

SelfManagedEventSourceUnionTypeDef = Union[
    SelfManagedEventSourceTypeDef, SelfManagedEventSourceOutputTypeDef
]

class ListAliasesResponseTypeDef(TypedDict):
    NextMarker: str
    Aliases: List[AliasConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAliasRequestTypeDef(TypedDict):
    FunctionName: str
    Name: str
    FunctionVersion: str
    Description: NotRequired[str]
    RoutingConfig: NotRequired[AliasRoutingConfigurationUnionTypeDef]

class UpdateAliasRequestTypeDef(TypedDict):
    FunctionName: str
    Name: str
    FunctionVersion: NotRequired[str]
    Description: NotRequired[str]
    RoutingConfig: NotRequired[AliasRoutingConfigurationUnionTypeDef]
    RevisionId: NotRequired[str]

class CreateCodeSigningConfigRequestTypeDef(TypedDict):
    AllowedPublishers: AllowedPublishersUnionTypeDef
    Description: NotRequired[str]
    CodeSigningPolicies: NotRequired[CodeSigningPoliciesTypeDef]
    Tags: NotRequired[Mapping[str, str]]

class UpdateCodeSigningConfigRequestTypeDef(TypedDict):
    CodeSigningConfigArn: str
    Description: NotRequired[str]
    AllowedPublishers: NotRequired[AllowedPublishersUnionTypeDef]
    CodeSigningPolicies: NotRequired[CodeSigningPoliciesTypeDef]

class PublishLayerVersionRequestTypeDef(TypedDict):
    LayerName: str
    Content: LayerVersionContentInputTypeDef
    Description: NotRequired[str]
    CompatibleRuntimes: NotRequired[Sequence[RuntimeType]]
    LicenseInfo: NotRequired[str]
    CompatibleArchitectures: NotRequired[Sequence[ArchitectureType]]

class CallbackFailedDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef

class CallbackTimedOutDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef

class ChainedInvokeFailedDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef

class ChainedInvokeStoppedDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef

class ChainedInvokeTimedOutDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef

class ContextFailedDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef

class ExecutionFailedDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef

class ExecutionStoppedDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef

class ExecutionTimedOutDetailsTypeDef(TypedDict):
    Error: NotRequired[EventErrorTypeDef]

class InvocationCompletedDetailsTypeDef(TypedDict):
    StartTimestamp: datetime
    EndTimestamp: datetime
    RequestId: str
    Error: NotRequired[EventErrorTypeDef]

class StepFailedDetailsTypeDef(TypedDict):
    Error: EventErrorTypeDef
    RetryDetails: RetryDetailsTypeDef

class WaitCancelledDetailsTypeDef(TypedDict):
    Error: NotRequired[EventErrorTypeDef]

OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "Id": str,
        "Type": OperationTypeType,
        "StartTimestamp": datetime,
        "Status": OperationStatusType,
        "ParentId": NotRequired[str],
        "Name": NotRequired[str],
        "SubType": NotRequired[str],
        "EndTimestamp": NotRequired[datetime],
        "ExecutionDetails": NotRequired[ExecutionDetailsTypeDef],
        "ContextDetails": NotRequired[ContextDetailsTypeDef],
        "StepDetails": NotRequired[StepDetailsTypeDef],
        "WaitDetails": NotRequired[WaitDetailsTypeDef],
        "CallbackDetails": NotRequired[CallbackDetailsTypeDef],
        "ChainedInvokeDetails": NotRequired[ChainedInvokeDetailsTypeDef],
    },
)

class CapacityProviderTypeDef(TypedDict):
    CapacityProviderArn: str
    State: CapacityProviderStateType
    VpcConfig: CapacityProviderVpcConfigOutputTypeDef
    PermissionsConfig: CapacityProviderPermissionsConfigTypeDef
    InstanceRequirements: NotRequired[InstanceRequirementsOutputTypeDef]
    CapacityProviderScalingConfig: NotRequired[CapacityProviderScalingConfigOutputTypeDef]
    KmsKeyArn: NotRequired[str]
    LastModified: NotRequired[str]

CapacityProviderScalingConfigUnionTypeDef = Union[
    CapacityProviderScalingConfigTypeDef, CapacityProviderScalingConfigOutputTypeDef
]

class CreateCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCodeSigningConfigsResponseTypeDef(TypedDict):
    NextMarker: str
    CodeSigningConfigs: List[CodeSigningConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCodeSigningConfigResponseTypeDef(TypedDict):
    CodeSigningConfig: CodeSigningConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionUrlConfigsResponseTypeDef(TypedDict):
    FunctionUrlConfigs: List[FunctionUrlConfigTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFunctionUrlConfigRequestTypeDef(TypedDict):
    FunctionName: str
    AuthType: FunctionUrlAuthTypeType
    Qualifier: NotRequired[str]
    Cors: NotRequired[CorsUnionTypeDef]
    InvokeMode: NotRequired[InvokeModeType]

class UpdateFunctionUrlConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    AuthType: NotRequired[FunctionUrlAuthTypeType]
    Cors: NotRequired[CorsUnionTypeDef]
    InvokeMode: NotRequired[InvokeModeType]

class FunctionEventInvokeConfigResponseTypeDef(TypedDict):
    LastModified: datetime
    FunctionArn: str
    MaximumRetryAttempts: int
    MaximumEventAgeInSeconds: int
    DestinationConfig: DestinationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionEventInvokeConfigTypeDef(TypedDict):
    LastModified: NotRequired[datetime]
    FunctionArn: NotRequired[str]
    MaximumRetryAttempts: NotRequired[int]
    MaximumEventAgeInSeconds: NotRequired[int]
    DestinationConfig: NotRequired[DestinationConfigTypeDef]

class PutFunctionEventInvokeConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    MaximumRetryAttempts: NotRequired[int]
    MaximumEventAgeInSeconds: NotRequired[int]
    DestinationConfig: NotRequired[DestinationConfigTypeDef]

class UpdateFunctionEventInvokeConfigRequestTypeDef(TypedDict):
    FunctionName: str
    Qualifier: NotRequired[str]
    MaximumRetryAttempts: NotRequired[int]
    MaximumEventAgeInSeconds: NotRequired[int]
    DestinationConfig: NotRequired[DestinationConfigTypeDef]

OperationUpdateTypeDef = TypedDict(
    "OperationUpdateTypeDef",
    {
        "Id": str,
        "Type": OperationTypeType,
        "Action": OperationActionType,
        "ParentId": NotRequired[str],
        "Name": NotRequired[str],
        "SubType": NotRequired[str],
        "Payload": NotRequired[str],
        "Error": NotRequired[ErrorObjectUnionTypeDef],
        "ContextOptions": NotRequired[ContextOptionsTypeDef],
        "StepOptions": NotRequired[StepOptionsTypeDef],
        "WaitOptions": NotRequired[WaitOptionsTypeDef],
        "CallbackOptions": NotRequired[CallbackOptionsTypeDef],
        "ChainedInvokeOptions": NotRequired[ChainedInvokeOptionsTypeDef],
    },
)

class SendDurableExecutionCallbackFailureRequestTypeDef(TypedDict):
    CallbackId: str
    Error: NotRequired[ErrorObjectUnionTypeDef]

class StopDurableExecutionRequestTypeDef(TypedDict):
    DurableExecutionArn: str
    Error: NotRequired[ErrorObjectUnionTypeDef]

FilterCriteriaUnionTypeDef = Union[FilterCriteriaTypeDef, FilterCriteriaOutputTypeDef]

class CreateFunctionRequestTypeDef(TypedDict):
    FunctionName: str
    Role: str
    Code: FunctionCodeTypeDef
    Runtime: NotRequired[RuntimeType]
    Handler: NotRequired[str]
    Description: NotRequired[str]
    Timeout: NotRequired[int]
    MemorySize: NotRequired[int]
    Publish: NotRequired[bool]
    VpcConfig: NotRequired[VpcConfigTypeDef]
    PackageType: NotRequired[PackageTypeType]
    DeadLetterConfig: NotRequired[DeadLetterConfigTypeDef]
    Environment: NotRequired[EnvironmentTypeDef]
    KMSKeyArn: NotRequired[str]
    TracingConfig: NotRequired[TracingConfigTypeDef]
    Tags: NotRequired[Mapping[str, str]]
    Layers: NotRequired[Sequence[str]]
    FileSystemConfigs: NotRequired[Sequence[FileSystemConfigTypeDef]]
    ImageConfig: NotRequired[ImageConfigUnionTypeDef]
    CodeSigningConfigArn: NotRequired[str]
    Architectures: NotRequired[Sequence[ArchitectureType]]
    EphemeralStorage: NotRequired[EphemeralStorageTypeDef]
    SnapStart: NotRequired[SnapStartTypeDef]
    LoggingConfig: NotRequired[LoggingConfigTypeDef]
    CapacityProviderConfig: NotRequired[CapacityProviderConfigTypeDef]
    PublishTo: NotRequired[Literal["LATEST_PUBLISHED"]]
    DurableConfig: NotRequired[DurableConfigTypeDef]
    TenancyConfig: NotRequired[TenancyConfigTypeDef]

class UpdateFunctionConfigurationRequestTypeDef(TypedDict):
    FunctionName: str
    Role: NotRequired[str]
    Handler: NotRequired[str]
    Description: NotRequired[str]
    Timeout: NotRequired[int]
    MemorySize: NotRequired[int]
    VpcConfig: NotRequired[VpcConfigTypeDef]
    Environment: NotRequired[EnvironmentTypeDef]
    Runtime: NotRequired[RuntimeType]
    DeadLetterConfig: NotRequired[DeadLetterConfigTypeDef]
    KMSKeyArn: NotRequired[str]
    TracingConfig: NotRequired[TracingConfigTypeDef]
    RevisionId: NotRequired[str]
    Layers: NotRequired[Sequence[str]]
    FileSystemConfigs: NotRequired[Sequence[FileSystemConfigTypeDef]]
    ImageConfig: NotRequired[ImageConfigUnionTypeDef]
    EphemeralStorage: NotRequired[EphemeralStorageTypeDef]
    SnapStart: NotRequired[SnapStartTypeDef]
    LoggingConfig: NotRequired[LoggingConfigTypeDef]
    CapacityProviderConfig: NotRequired[CapacityProviderConfigTypeDef]
    DurableConfig: NotRequired[DurableConfigTypeDef]

class InvokeWithResponseStreamResponseTypeDef(TypedDict):
    StatusCode: int
    ExecutedVersion: str
    EventStream: EventStream[InvokeWithResponseStreamResponseEventTypeDef]
    ResponseStreamContentType: str
    ResponseMetadata: ResponseMetadataTypeDef

class AmazonManagedKafkaEventSourceConfigOutputTypeDef(TypedDict):
    ConsumerGroupId: NotRequired[str]
    SchemaRegistryConfig: NotRequired[KafkaSchemaRegistryConfigOutputTypeDef]

class SelfManagedKafkaEventSourceConfigOutputTypeDef(TypedDict):
    ConsumerGroupId: NotRequired[str]
    SchemaRegistryConfig: NotRequired[KafkaSchemaRegistryConfigOutputTypeDef]

class AmazonManagedKafkaEventSourceConfigTypeDef(TypedDict):
    ConsumerGroupId: NotRequired[str]
    SchemaRegistryConfig: NotRequired[KafkaSchemaRegistryConfigTypeDef]

class SelfManagedKafkaEventSourceConfigTypeDef(TypedDict):
    ConsumerGroupId: NotRequired[str]
    SchemaRegistryConfig: NotRequired[KafkaSchemaRegistryConfigTypeDef]

class ListLayersResponseTypeDef(TypedDict):
    NextMarker: str
    Layers: List[LayersListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionConfigurationResponseTypeDef(TypedDict):
    FunctionName: str
    FunctionArn: str
    Runtime: RuntimeType
    Role: str
    Handler: str
    CodeSize: int
    Description: str
    Timeout: int
    MemorySize: int
    LastModified: str
    CodeSha256: str
    Version: str
    VpcConfig: VpcConfigResponseTypeDef
    DeadLetterConfig: DeadLetterConfigTypeDef
    Environment: EnvironmentResponseTypeDef
    KMSKeyArn: str
    TracingConfig: TracingConfigResponseTypeDef
    MasterArn: str
    RevisionId: str
    Layers: List[LayerTypeDef]
    State: StateType
    StateReason: str
    StateReasonCode: StateReasonCodeType
    LastUpdateStatus: LastUpdateStatusType
    LastUpdateStatusReason: str
    LastUpdateStatusReasonCode: LastUpdateStatusReasonCodeType
    FileSystemConfigs: List[FileSystemConfigTypeDef]
    PackageType: PackageTypeType
    ImageConfigResponse: ImageConfigResponseTypeDef
    SigningProfileVersionArn: str
    SigningJobArn: str
    Architectures: List[ArchitectureType]
    EphemeralStorage: EphemeralStorageTypeDef
    SnapStart: SnapStartResponseTypeDef
    RuntimeVersionConfig: RuntimeVersionConfigTypeDef
    LoggingConfig: LoggingConfigTypeDef
    CapacityProviderConfig: CapacityProviderConfigTypeDef
    ConfigSha256: str
    DurableConfig: DurableConfigTypeDef
    TenancyConfig: TenancyConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FunctionConfigurationTypeDef(TypedDict):
    FunctionName: NotRequired[str]
    FunctionArn: NotRequired[str]
    Runtime: NotRequired[RuntimeType]
    Role: NotRequired[str]
    Handler: NotRequired[str]
    CodeSize: NotRequired[int]
    Description: NotRequired[str]
    Timeout: NotRequired[int]
    MemorySize: NotRequired[int]
    LastModified: NotRequired[str]
    CodeSha256: NotRequired[str]
    Version: NotRequired[str]
    VpcConfig: NotRequired[VpcConfigResponseTypeDef]
    DeadLetterConfig: NotRequired[DeadLetterConfigTypeDef]
    Environment: NotRequired[EnvironmentResponseTypeDef]
    KMSKeyArn: NotRequired[str]
    TracingConfig: NotRequired[TracingConfigResponseTypeDef]
    MasterArn: NotRequired[str]
    RevisionId: NotRequired[str]
    Layers: NotRequired[List[LayerTypeDef]]
    State: NotRequired[StateType]
    StateReason: NotRequired[str]
    StateReasonCode: NotRequired[StateReasonCodeType]
    LastUpdateStatus: NotRequired[LastUpdateStatusType]
    LastUpdateStatusReason: NotRequired[str]
    LastUpdateStatusReasonCode: NotRequired[LastUpdateStatusReasonCodeType]
    FileSystemConfigs: NotRequired[List[FileSystemConfigTypeDef]]
    PackageType: NotRequired[PackageTypeType]
    ImageConfigResponse: NotRequired[ImageConfigResponseTypeDef]
    SigningProfileVersionArn: NotRequired[str]
    SigningJobArn: NotRequired[str]
    Architectures: NotRequired[List[ArchitectureType]]
    EphemeralStorage: NotRequired[EphemeralStorageTypeDef]
    SnapStart: NotRequired[SnapStartResponseTypeDef]
    RuntimeVersionConfig: NotRequired[RuntimeVersionConfigTypeDef]
    LoggingConfig: NotRequired[LoggingConfigTypeDef]
    CapacityProviderConfig: NotRequired[CapacityProviderConfigTypeDef]
    ConfigSha256: NotRequired[str]
    DurableConfig: NotRequired[DurableConfigTypeDef]
    TenancyConfig: NotRequired[TenancyConfigTypeDef]

class EventTypeDef(TypedDict):
    EventType: NotRequired[EventTypeType]
    SubType: NotRequired[str]
    EventId: NotRequired[int]
    Id: NotRequired[str]
    Name: NotRequired[str]
    EventTimestamp: NotRequired[datetime]
    ParentId: NotRequired[str]
    ExecutionStartedDetails: NotRequired[ExecutionStartedDetailsTypeDef]
    ExecutionSucceededDetails: NotRequired[ExecutionSucceededDetailsTypeDef]
    ExecutionFailedDetails: NotRequired[ExecutionFailedDetailsTypeDef]
    ExecutionTimedOutDetails: NotRequired[ExecutionTimedOutDetailsTypeDef]
    ExecutionStoppedDetails: NotRequired[ExecutionStoppedDetailsTypeDef]
    ContextStartedDetails: NotRequired[Dict[str, Any]]
    ContextSucceededDetails: NotRequired[ContextSucceededDetailsTypeDef]
    ContextFailedDetails: NotRequired[ContextFailedDetailsTypeDef]
    WaitStartedDetails: NotRequired[WaitStartedDetailsTypeDef]
    WaitSucceededDetails: NotRequired[WaitSucceededDetailsTypeDef]
    WaitCancelledDetails: NotRequired[WaitCancelledDetailsTypeDef]
    StepStartedDetails: NotRequired[Dict[str, Any]]
    StepSucceededDetails: NotRequired[StepSucceededDetailsTypeDef]
    StepFailedDetails: NotRequired[StepFailedDetailsTypeDef]
    ChainedInvokeStartedDetails: NotRequired[ChainedInvokeStartedDetailsTypeDef]
    ChainedInvokeSucceededDetails: NotRequired[ChainedInvokeSucceededDetailsTypeDef]
    ChainedInvokeFailedDetails: NotRequired[ChainedInvokeFailedDetailsTypeDef]
    ChainedInvokeTimedOutDetails: NotRequired[ChainedInvokeTimedOutDetailsTypeDef]
    ChainedInvokeStoppedDetails: NotRequired[ChainedInvokeStoppedDetailsTypeDef]
    CallbackStartedDetails: NotRequired[CallbackStartedDetailsTypeDef]
    CallbackSucceededDetails: NotRequired[CallbackSucceededDetailsTypeDef]
    CallbackFailedDetails: NotRequired[CallbackFailedDetailsTypeDef]
    CallbackTimedOutDetails: NotRequired[CallbackTimedOutDetailsTypeDef]
    InvocationCompletedDetails: NotRequired[InvocationCompletedDetailsTypeDef]

class CheckpointUpdatedExecutionStateTypeDef(TypedDict):
    Operations: NotRequired[List[OperationTypeDef]]
    NextMarker: NotRequired[str]

class GetDurableExecutionStateResponseTypeDef(TypedDict):
    Operations: List[OperationTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCapacityProviderResponseTypeDef(TypedDict):
    CapacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCapacityProviderResponseTypeDef(TypedDict):
    CapacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCapacityProviderResponseTypeDef(TypedDict):
    CapacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCapacityProvidersResponseTypeDef(TypedDict):
    CapacityProviders: List[CapacityProviderTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCapacityProviderResponseTypeDef(TypedDict):
    CapacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCapacityProviderRequestTypeDef(TypedDict):
    CapacityProviderName: str
    VpcConfig: CapacityProviderVpcConfigUnionTypeDef
    PermissionsConfig: CapacityProviderPermissionsConfigTypeDef
    InstanceRequirements: NotRequired[InstanceRequirementsUnionTypeDef]
    CapacityProviderScalingConfig: NotRequired[CapacityProviderScalingConfigUnionTypeDef]
    KmsKeyArn: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class UpdateCapacityProviderRequestTypeDef(TypedDict):
    CapacityProviderName: str
    CapacityProviderScalingConfig: NotRequired[CapacityProviderScalingConfigUnionTypeDef]

class ListFunctionEventInvokeConfigsResponseTypeDef(TypedDict):
    FunctionEventInvokeConfigs: List[FunctionEventInvokeConfigTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckpointDurableExecutionRequestTypeDef(TypedDict):
    DurableExecutionArn: str
    CheckpointToken: str
    Updates: NotRequired[Sequence[OperationUpdateTypeDef]]
    ClientToken: NotRequired[str]

class EventSourceMappingConfigurationResponseTypeDef(TypedDict):
    UUID: str
    StartingPosition: EventSourcePositionType
    StartingPositionTimestamp: datetime
    BatchSize: int
    MaximumBatchingWindowInSeconds: int
    ParallelizationFactor: int
    EventSourceArn: str
    FilterCriteria: FilterCriteriaOutputTypeDef
    FunctionArn: str
    LastModified: datetime
    LastProcessingResult: str
    State: str
    StateTransitionReason: str
    DestinationConfig: DestinationConfigTypeDef
    Topics: List[str]
    Queues: List[str]
    SourceAccessConfigurations: List[SourceAccessConfigurationTypeDef]
    SelfManagedEventSource: SelfManagedEventSourceOutputTypeDef
    MaximumRecordAgeInSeconds: int
    BisectBatchOnFunctionError: bool
    MaximumRetryAttempts: int
    TumblingWindowInSeconds: int
    FunctionResponseTypes: List[Literal["ReportBatchItemFailures"]]
    AmazonManagedKafkaEventSourceConfig: AmazonManagedKafkaEventSourceConfigOutputTypeDef
    SelfManagedKafkaEventSourceConfig: SelfManagedKafkaEventSourceConfigOutputTypeDef
    ScalingConfig: ScalingConfigTypeDef
    DocumentDBEventSourceConfig: DocumentDBEventSourceConfigTypeDef
    KMSKeyArn: str
    FilterCriteriaError: FilterCriteriaErrorTypeDef
    EventSourceMappingArn: str
    MetricsConfig: EventSourceMappingMetricsConfigOutputTypeDef
    ProvisionedPollerConfig: ProvisionedPollerConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventSourceMappingConfigurationTypeDef(TypedDict):
    UUID: NotRequired[str]
    StartingPosition: NotRequired[EventSourcePositionType]
    StartingPositionTimestamp: NotRequired[datetime]
    BatchSize: NotRequired[int]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    ParallelizationFactor: NotRequired[int]
    EventSourceArn: NotRequired[str]
    FilterCriteria: NotRequired[FilterCriteriaOutputTypeDef]
    FunctionArn: NotRequired[str]
    LastModified: NotRequired[datetime]
    LastProcessingResult: NotRequired[str]
    State: NotRequired[str]
    StateTransitionReason: NotRequired[str]
    DestinationConfig: NotRequired[DestinationConfigTypeDef]
    Topics: NotRequired[List[str]]
    Queues: NotRequired[List[str]]
    SourceAccessConfigurations: NotRequired[List[SourceAccessConfigurationTypeDef]]
    SelfManagedEventSource: NotRequired[SelfManagedEventSourceOutputTypeDef]
    MaximumRecordAgeInSeconds: NotRequired[int]
    BisectBatchOnFunctionError: NotRequired[bool]
    MaximumRetryAttempts: NotRequired[int]
    TumblingWindowInSeconds: NotRequired[int]
    FunctionResponseTypes: NotRequired[List[Literal["ReportBatchItemFailures"]]]
    AmazonManagedKafkaEventSourceConfig: NotRequired[
        AmazonManagedKafkaEventSourceConfigOutputTypeDef
    ]
    SelfManagedKafkaEventSourceConfig: NotRequired[SelfManagedKafkaEventSourceConfigOutputTypeDef]
    ScalingConfig: NotRequired[ScalingConfigTypeDef]
    DocumentDBEventSourceConfig: NotRequired[DocumentDBEventSourceConfigTypeDef]
    KMSKeyArn: NotRequired[str]
    FilterCriteriaError: NotRequired[FilterCriteriaErrorTypeDef]
    EventSourceMappingArn: NotRequired[str]
    MetricsConfig: NotRequired[EventSourceMappingMetricsConfigOutputTypeDef]
    ProvisionedPollerConfig: NotRequired[ProvisionedPollerConfigTypeDef]

AmazonManagedKafkaEventSourceConfigUnionTypeDef = Union[
    AmazonManagedKafkaEventSourceConfigTypeDef, AmazonManagedKafkaEventSourceConfigOutputTypeDef
]
SelfManagedKafkaEventSourceConfigUnionTypeDef = Union[
    SelfManagedKafkaEventSourceConfigTypeDef, SelfManagedKafkaEventSourceConfigOutputTypeDef
]

class GetFunctionResponseTypeDef(TypedDict):
    Configuration: FunctionConfigurationTypeDef
    Code: FunctionCodeLocationTypeDef
    Tags: Dict[str, str]
    TagsError: TagsErrorTypeDef
    Concurrency: ConcurrencyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFunctionsResponseTypeDef(TypedDict):
    NextMarker: str
    Functions: List[FunctionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVersionsByFunctionResponseTypeDef(TypedDict):
    NextMarker: str
    Versions: List[FunctionConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDurableExecutionHistoryResponseTypeDef(TypedDict):
    Events: List[EventTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CheckpointDurableExecutionResponseTypeDef(TypedDict):
    CheckpointToken: str
    NewExecutionState: CheckpointUpdatedExecutionStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventSourceMappingsResponseTypeDef(TypedDict):
    NextMarker: str
    EventSourceMappings: List[EventSourceMappingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSourceMappingRequestTypeDef(TypedDict):
    FunctionName: str
    EventSourceArn: NotRequired[str]
    Enabled: NotRequired[bool]
    BatchSize: NotRequired[int]
    FilterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    ParallelizationFactor: NotRequired[int]
    StartingPosition: NotRequired[EventSourcePositionType]
    StartingPositionTimestamp: NotRequired[TimestampTypeDef]
    DestinationConfig: NotRequired[DestinationConfigTypeDef]
    MaximumRecordAgeInSeconds: NotRequired[int]
    BisectBatchOnFunctionError: NotRequired[bool]
    MaximumRetryAttempts: NotRequired[int]
    Tags: NotRequired[Mapping[str, str]]
    TumblingWindowInSeconds: NotRequired[int]
    Topics: NotRequired[Sequence[str]]
    Queues: NotRequired[Sequence[str]]
    SourceAccessConfigurations: NotRequired[Sequence[SourceAccessConfigurationTypeDef]]
    SelfManagedEventSource: NotRequired[SelfManagedEventSourceUnionTypeDef]
    FunctionResponseTypes: NotRequired[Sequence[Literal["ReportBatchItemFailures"]]]
    AmazonManagedKafkaEventSourceConfig: NotRequired[
        AmazonManagedKafkaEventSourceConfigUnionTypeDef
    ]
    SelfManagedKafkaEventSourceConfig: NotRequired[SelfManagedKafkaEventSourceConfigUnionTypeDef]
    ScalingConfig: NotRequired[ScalingConfigTypeDef]
    DocumentDBEventSourceConfig: NotRequired[DocumentDBEventSourceConfigTypeDef]
    KMSKeyArn: NotRequired[str]
    MetricsConfig: NotRequired[EventSourceMappingMetricsConfigUnionTypeDef]
    ProvisionedPollerConfig: NotRequired[ProvisionedPollerConfigTypeDef]

class UpdateEventSourceMappingRequestTypeDef(TypedDict):
    UUID: str
    FunctionName: NotRequired[str]
    Enabled: NotRequired[bool]
    BatchSize: NotRequired[int]
    FilterCriteria: NotRequired[FilterCriteriaUnionTypeDef]
    MaximumBatchingWindowInSeconds: NotRequired[int]
    DestinationConfig: NotRequired[DestinationConfigTypeDef]
    MaximumRecordAgeInSeconds: NotRequired[int]
    BisectBatchOnFunctionError: NotRequired[bool]
    MaximumRetryAttempts: NotRequired[int]
    ParallelizationFactor: NotRequired[int]
    SourceAccessConfigurations: NotRequired[Sequence[SourceAccessConfigurationTypeDef]]
    TumblingWindowInSeconds: NotRequired[int]
    FunctionResponseTypes: NotRequired[Sequence[Literal["ReportBatchItemFailures"]]]
    ScalingConfig: NotRequired[ScalingConfigTypeDef]
    AmazonManagedKafkaEventSourceConfig: NotRequired[
        AmazonManagedKafkaEventSourceConfigUnionTypeDef
    ]
    SelfManagedKafkaEventSourceConfig: NotRequired[SelfManagedKafkaEventSourceConfigUnionTypeDef]
    DocumentDBEventSourceConfig: NotRequired[DocumentDBEventSourceConfigTypeDef]
    KMSKeyArn: NotRequired[str]
    MetricsConfig: NotRequired[EventSourceMappingMetricsConfigUnionTypeDef]
    ProvisionedPollerConfig: NotRequired[ProvisionedPollerConfigTypeDef]
