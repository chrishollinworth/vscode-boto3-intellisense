"""
Type annotations for lambda service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lambda/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lambda.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ApplicationLogLevelType,
    ArchitectureType,
    CodeSigningPolicyType,
    EventSourcePositionType,
    FullDocumentType,
    FunctionUrlAuthTypeType,
    InvocationTypeType,
    InvokeModeType,
    LastUpdateStatusReasonCodeType,
    LastUpdateStatusType,
    LogFormatType,
    LogTypeType,
    PackageTypeType,
    ProvisionedConcurrencyStatusEnumType,
    ResponseStreamingInvocationTypeType,
    RuntimeType,
    SnapStartApplyOnType,
    SnapStartOptimizationStatusType,
    SourceAccessTypeType,
    StateReasonCodeType,
    StateType,
    SystemLogLevelType,
    TracingModeType,
    UpdateRuntimeOnType,
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
    "AccountLimitTypeDef",
    "AccountUsageTypeDef",
    "AddLayerVersionPermissionRequestRequestTypeDef",
    "AddLayerVersionPermissionResponseTypeDef",
    "AddPermissionRequestRequestTypeDef",
    "AddPermissionResponseTypeDef",
    "AliasConfigurationResponseMetadataTypeDef",
    "AliasConfigurationTypeDef",
    "AliasRoutingConfigurationTypeDef",
    "AllowedPublishersTypeDef",
    "AmazonManagedKafkaEventSourceConfigTypeDef",
    "CodeSigningConfigTypeDef",
    "CodeSigningPoliciesTypeDef",
    "ConcurrencyResponseMetadataTypeDef",
    "ConcurrencyTypeDef",
    "CorsTypeDef",
    "CreateAliasRequestRequestTypeDef",
    "CreateCodeSigningConfigRequestRequestTypeDef",
    "CreateCodeSigningConfigResponseTypeDef",
    "CreateEventSourceMappingRequestRequestTypeDef",
    "CreateFunctionRequestRequestTypeDef",
    "CreateFunctionUrlConfigRequestRequestTypeDef",
    "CreateFunctionUrlConfigResponseTypeDef",
    "DeadLetterConfigTypeDef",
    "DeleteAliasRequestRequestTypeDef",
    "DeleteCodeSigningConfigRequestRequestTypeDef",
    "DeleteEventSourceMappingRequestRequestTypeDef",
    "DeleteFunctionCodeSigningConfigRequestRequestTypeDef",
    "DeleteFunctionConcurrencyRequestRequestTypeDef",
    "DeleteFunctionEventInvokeConfigRequestRequestTypeDef",
    "DeleteFunctionRequestRequestTypeDef",
    "DeleteFunctionUrlConfigRequestRequestTypeDef",
    "DeleteLayerVersionRequestRequestTypeDef",
    "DeleteProvisionedConcurrencyConfigRequestRequestTypeDef",
    "DestinationConfigTypeDef",
    "DocumentDBEventSourceConfigTypeDef",
    "EnvironmentErrorTypeDef",
    "EnvironmentResponseTypeDef",
    "EnvironmentTypeDef",
    "EphemeralStorageTypeDef",
    "EventSourceMappingConfigurationResponseMetadataTypeDef",
    "EventSourceMappingConfigurationTypeDef",
    "FileSystemConfigTypeDef",
    "FilterCriteriaTypeDef",
    "FilterTypeDef",
    "FunctionCodeLocationTypeDef",
    "FunctionCodeTypeDef",
    "FunctionConfigurationResponseMetadataTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionEventInvokeConfigResponseMetadataTypeDef",
    "FunctionEventInvokeConfigTypeDef",
    "FunctionUrlConfigTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetAliasRequestRequestTypeDef",
    "GetCodeSigningConfigRequestRequestTypeDef",
    "GetCodeSigningConfigResponseTypeDef",
    "GetEventSourceMappingRequestRequestTypeDef",
    "GetFunctionCodeSigningConfigRequestRequestTypeDef",
    "GetFunctionCodeSigningConfigResponseTypeDef",
    "GetFunctionConcurrencyRequestRequestTypeDef",
    "GetFunctionConcurrencyResponseTypeDef",
    "GetFunctionConfigurationRequestRequestTypeDef",
    "GetFunctionEventInvokeConfigRequestRequestTypeDef",
    "GetFunctionRequestRequestTypeDef",
    "GetFunctionResponseTypeDef",
    "GetFunctionUrlConfigRequestRequestTypeDef",
    "GetFunctionUrlConfigResponseTypeDef",
    "GetLayerVersionByArnRequestRequestTypeDef",
    "GetLayerVersionPolicyRequestRequestTypeDef",
    "GetLayerVersionPolicyResponseTypeDef",
    "GetLayerVersionRequestRequestTypeDef",
    "GetLayerVersionResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProvisionedConcurrencyConfigRequestRequestTypeDef",
    "GetProvisionedConcurrencyConfigResponseTypeDef",
    "GetRuntimeManagementConfigRequestRequestTypeDef",
    "GetRuntimeManagementConfigResponseTypeDef",
    "ImageConfigErrorTypeDef",
    "ImageConfigResponseTypeDef",
    "ImageConfigTypeDef",
    "InvocationRequestRequestTypeDef",
    "InvocationResponseTypeDef",
    "InvokeAsyncRequestRequestTypeDef",
    "InvokeAsyncResponseTypeDef",
    "InvokeResponseStreamUpdateTypeDef",
    "InvokeWithResponseStreamCompleteEventTypeDef",
    "InvokeWithResponseStreamRequestRequestTypeDef",
    "InvokeWithResponseStreamResponseEventTypeDef",
    "InvokeWithResponseStreamResponseTypeDef",
    "LayerTypeDef",
    "LayerVersionContentInputTypeDef",
    "LayerVersionContentOutputTypeDef",
    "LayerVersionsListItemTypeDef",
    "LayersListItemTypeDef",
    "ListAliasesRequestRequestTypeDef",
    "ListAliasesResponseTypeDef",
    "ListCodeSigningConfigsRequestRequestTypeDef",
    "ListCodeSigningConfigsResponseTypeDef",
    "ListEventSourceMappingsRequestRequestTypeDef",
    "ListEventSourceMappingsResponseTypeDef",
    "ListFunctionEventInvokeConfigsRequestRequestTypeDef",
    "ListFunctionEventInvokeConfigsResponseTypeDef",
    "ListFunctionUrlConfigsRequestRequestTypeDef",
    "ListFunctionUrlConfigsResponseTypeDef",
    "ListFunctionsByCodeSigningConfigRequestRequestTypeDef",
    "ListFunctionsByCodeSigningConfigResponseTypeDef",
    "ListFunctionsRequestRequestTypeDef",
    "ListFunctionsResponseTypeDef",
    "ListLayerVersionsRequestRequestTypeDef",
    "ListLayerVersionsResponseTypeDef",
    "ListLayersRequestRequestTypeDef",
    "ListLayersResponseTypeDef",
    "ListProvisionedConcurrencyConfigsRequestRequestTypeDef",
    "ListProvisionedConcurrencyConfigsResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListVersionsByFunctionRequestRequestTypeDef",
    "ListVersionsByFunctionResponseTypeDef",
    "LoggingConfigTypeDef",
    "OnFailureTypeDef",
    "OnSuccessTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisionedConcurrencyConfigListItemTypeDef",
    "PublishLayerVersionRequestRequestTypeDef",
    "PublishLayerVersionResponseTypeDef",
    "PublishVersionRequestRequestTypeDef",
    "PutFunctionCodeSigningConfigRequestRequestTypeDef",
    "PutFunctionCodeSigningConfigResponseTypeDef",
    "PutFunctionConcurrencyRequestRequestTypeDef",
    "PutFunctionEventInvokeConfigRequestRequestTypeDef",
    "PutProvisionedConcurrencyConfigRequestRequestTypeDef",
    "PutProvisionedConcurrencyConfigResponseTypeDef",
    "PutRuntimeManagementConfigRequestRequestTypeDef",
    "PutRuntimeManagementConfigResponseTypeDef",
    "RemoveLayerVersionPermissionRequestRequestTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeVersionConfigTypeDef",
    "RuntimeVersionErrorTypeDef",
    "ScalingConfigTypeDef",
    "SelfManagedEventSourceTypeDef",
    "SelfManagedKafkaEventSourceConfigTypeDef",
    "SnapStartResponseTypeDef",
    "SnapStartTypeDef",
    "SourceAccessConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TracingConfigResponseTypeDef",
    "TracingConfigTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAliasRequestRequestTypeDef",
    "UpdateCodeSigningConfigRequestRequestTypeDef",
    "UpdateCodeSigningConfigResponseTypeDef",
    "UpdateEventSourceMappingRequestRequestTypeDef",
    "UpdateFunctionCodeRequestRequestTypeDef",
    "UpdateFunctionConfigurationRequestRequestTypeDef",
    "UpdateFunctionEventInvokeConfigRequestRequestTypeDef",
    "UpdateFunctionUrlConfigRequestRequestTypeDef",
    "UpdateFunctionUrlConfigResponseTypeDef",
    "VpcConfigResponseTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "TotalCodeSize": int,
        "CodeSizeUnzipped": int,
        "CodeSizeZipped": int,
        "ConcurrentExecutions": int,
        "UnreservedConcurrentExecutions": int,
    },
    total=False,
)

AccountUsageTypeDef = TypedDict(
    "AccountUsageTypeDef",
    {
        "TotalCodeSize": int,
        "FunctionCount": int,
    },
    total=False,
)

_RequiredAddLayerVersionPermissionRequestRequestTypeDef = TypedDict(
    "_RequiredAddLayerVersionPermissionRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
        "StatementId": str,
        "Action": str,
        "Principal": str,
    },
)
_OptionalAddLayerVersionPermissionRequestRequestTypeDef = TypedDict(
    "_OptionalAddLayerVersionPermissionRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "RevisionId": str,
    },
    total=False,
)

class AddLayerVersionPermissionRequestRequestTypeDef(
    _RequiredAddLayerVersionPermissionRequestRequestTypeDef,
    _OptionalAddLayerVersionPermissionRequestRequestTypeDef,
):
    pass

AddLayerVersionPermissionResponseTypeDef = TypedDict(
    "AddLayerVersionPermissionResponseTypeDef",
    {
        "Statement": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAddPermissionRequestRequestTypeDef = TypedDict(
    "_RequiredAddPermissionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "StatementId": str,
        "Action": str,
        "Principal": str,
    },
)
_OptionalAddPermissionRequestRequestTypeDef = TypedDict(
    "_OptionalAddPermissionRequestRequestTypeDef",
    {
        "SourceArn": str,
        "SourceAccount": str,
        "EventSourceToken": str,
        "Qualifier": str,
        "RevisionId": str,
        "PrincipalOrgID": str,
        "FunctionUrlAuthType": FunctionUrlAuthTypeType,
    },
    total=False,
)

class AddPermissionRequestRequestTypeDef(
    _RequiredAddPermissionRequestRequestTypeDef, _OptionalAddPermissionRequestRequestTypeDef
):
    pass

AddPermissionResponseTypeDef = TypedDict(
    "AddPermissionResponseTypeDef",
    {
        "Statement": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AliasConfigurationResponseMetadataTypeDef = TypedDict(
    "AliasConfigurationResponseMetadataTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AliasConfigurationTypeDef = TypedDict(
    "AliasConfigurationTypeDef",
    {
        "AliasArn": str,
        "Name": str,
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
        "RevisionId": str,
    },
    total=False,
)

AliasRoutingConfigurationTypeDef = TypedDict(
    "AliasRoutingConfigurationTypeDef",
    {
        "AdditionalVersionWeights": Dict[str, float],
    },
    total=False,
)

AllowedPublishersTypeDef = TypedDict(
    "AllowedPublishersTypeDef",
    {
        "SigningProfileVersionArns": List[str],
    },
)

AmazonManagedKafkaEventSourceConfigTypeDef = TypedDict(
    "AmazonManagedKafkaEventSourceConfigTypeDef",
    {
        "ConsumerGroupId": str,
    },
    total=False,
)

_RequiredCodeSigningConfigTypeDef = TypedDict(
    "_RequiredCodeSigningConfigTypeDef",
    {
        "CodeSigningConfigId": str,
        "CodeSigningConfigArn": str,
        "AllowedPublishers": "AllowedPublishersTypeDef",
        "CodeSigningPolicies": "CodeSigningPoliciesTypeDef",
        "LastModified": str,
    },
)
_OptionalCodeSigningConfigTypeDef = TypedDict(
    "_OptionalCodeSigningConfigTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class CodeSigningConfigTypeDef(
    _RequiredCodeSigningConfigTypeDef, _OptionalCodeSigningConfigTypeDef
):
    pass

CodeSigningPoliciesTypeDef = TypedDict(
    "CodeSigningPoliciesTypeDef",
    {
        "UntrustedArtifactOnDeployment": CodeSigningPolicyType,
    },
    total=False,
)

ConcurrencyResponseMetadataTypeDef = TypedDict(
    "ConcurrencyResponseMetadataTypeDef",
    {
        "ReservedConcurrentExecutions": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConcurrencyTypeDef = TypedDict(
    "ConcurrencyTypeDef",
    {
        "ReservedConcurrentExecutions": int,
    },
    total=False,
)

CorsTypeDef = TypedDict(
    "CorsTypeDef",
    {
        "AllowCredentials": bool,
        "AllowHeaders": List[str],
        "AllowMethods": List[str],
        "AllowOrigins": List[str],
        "ExposeHeaders": List[str],
        "MaxAge": int,
    },
    total=False,
)

_RequiredCreateAliasRequestRequestTypeDef = TypedDict(
    "_RequiredCreateAliasRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
        "FunctionVersion": str,
    },
)
_OptionalCreateAliasRequestRequestTypeDef = TypedDict(
    "_OptionalCreateAliasRequestRequestTypeDef",
    {
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
    },
    total=False,
)

class CreateAliasRequestRequestTypeDef(
    _RequiredCreateAliasRequestRequestTypeDef, _OptionalCreateAliasRequestRequestTypeDef
):
    pass

_RequiredCreateCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCodeSigningConfigRequestRequestTypeDef",
    {
        "AllowedPublishers": "AllowedPublishersTypeDef",
    },
)
_OptionalCreateCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCodeSigningConfigRequestRequestTypeDef",
    {
        "Description": str,
        "CodeSigningPolicies": "CodeSigningPoliciesTypeDef",
    },
    total=False,
)

class CreateCodeSigningConfigRequestRequestTypeDef(
    _RequiredCreateCodeSigningConfigRequestRequestTypeDef,
    _OptionalCreateCodeSigningConfigRequestRequestTypeDef,
):
    pass

CreateCodeSigningConfigResponseTypeDef = TypedDict(
    "CreateCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEventSourceMappingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEventSourceMappingRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalCreateEventSourceMappingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEventSourceMappingRequestRequestTypeDef",
    {
        "EventSourceArn": str,
        "Enabled": bool,
        "BatchSize": int,
        "FilterCriteria": "FilterCriteriaTypeDef",
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "StartingPosition": EventSourcePositionType,
        "StartingPositionTimestamp": Union[datetime, str],
        "DestinationConfig": "DestinationConfigTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "TumblingWindowInSeconds": int,
        "Topics": List[str],
        "Queues": List[str],
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "SelfManagedEventSource": "SelfManagedEventSourceTypeDef",
        "FunctionResponseTypes": List[Literal["ReportBatchItemFailures"]],
        "AmazonManagedKafkaEventSourceConfig": "AmazonManagedKafkaEventSourceConfigTypeDef",
        "SelfManagedKafkaEventSourceConfig": "SelfManagedKafkaEventSourceConfigTypeDef",
        "ScalingConfig": "ScalingConfigTypeDef",
        "DocumentDBEventSourceConfig": "DocumentDBEventSourceConfigTypeDef",
    },
    total=False,
)

class CreateEventSourceMappingRequestRequestTypeDef(
    _RequiredCreateEventSourceMappingRequestRequestTypeDef,
    _OptionalCreateEventSourceMappingRequestRequestTypeDef,
):
    pass

_RequiredCreateFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Role": str,
        "Code": "FunctionCodeTypeDef",
    },
)
_OptionalCreateFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionRequestRequestTypeDef",
    {
        "Runtime": RuntimeType,
        "Handler": str,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "Publish": bool,
        "VpcConfig": "VpcConfigTypeDef",
        "PackageType": PackageTypeType,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "Environment": "EnvironmentTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigTypeDef",
        "Tags": Dict[str, str],
        "Layers": List[str],
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "ImageConfig": "ImageConfigTypeDef",
        "CodeSigningConfigArn": str,
        "Architectures": List[ArchitectureType],
        "EphemeralStorage": "EphemeralStorageTypeDef",
        "SnapStart": "SnapStartTypeDef",
        "LoggingConfig": "LoggingConfigTypeDef",
    },
    total=False,
)

class CreateFunctionRequestRequestTypeDef(
    _RequiredCreateFunctionRequestRequestTypeDef, _OptionalCreateFunctionRequestRequestTypeDef
):
    pass

_RequiredCreateFunctionUrlConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFunctionUrlConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "AuthType": FunctionUrlAuthTypeType,
    },
)
_OptionalCreateFunctionUrlConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFunctionUrlConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
        "Cors": "CorsTypeDef",
        "InvokeMode": InvokeModeType,
    },
    total=False,
)

class CreateFunctionUrlConfigRequestRequestTypeDef(
    _RequiredCreateFunctionUrlConfigRequestRequestTypeDef,
    _OptionalCreateFunctionUrlConfigRequestRequestTypeDef,
):
    pass

CreateFunctionUrlConfigResponseTypeDef = TypedDict(
    "CreateFunctionUrlConfigResponseTypeDef",
    {
        "FunctionUrl": str,
        "FunctionArn": str,
        "AuthType": FunctionUrlAuthTypeType,
        "Cors": "CorsTypeDef",
        "CreationTime": str,
        "InvokeMode": InvokeModeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeadLetterConfigTypeDef = TypedDict(
    "DeadLetterConfigTypeDef",
    {
        "TargetArn": str,
    },
    total=False,
)

DeleteAliasRequestRequestTypeDef = TypedDict(
    "DeleteAliasRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
    },
)

DeleteCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "DeleteCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)

DeleteEventSourceMappingRequestRequestTypeDef = TypedDict(
    "DeleteEventSourceMappingRequestRequestTypeDef",
    {
        "UUID": str,
    },
)

DeleteFunctionCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "DeleteFunctionCodeSigningConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)

DeleteFunctionConcurrencyRequestRequestTypeDef = TypedDict(
    "DeleteFunctionConcurrencyRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)

_RequiredDeleteFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalDeleteFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class DeleteFunctionEventInvokeConfigRequestRequestTypeDef(
    _RequiredDeleteFunctionEventInvokeConfigRequestRequestTypeDef,
    _OptionalDeleteFunctionEventInvokeConfigRequestRequestTypeDef,
):
    pass

_RequiredDeleteFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFunctionRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalDeleteFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFunctionRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class DeleteFunctionRequestRequestTypeDef(
    _RequiredDeleteFunctionRequestRequestTypeDef, _OptionalDeleteFunctionRequestRequestTypeDef
):
    pass

_RequiredDeleteFunctionUrlConfigRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFunctionUrlConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalDeleteFunctionUrlConfigRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFunctionUrlConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class DeleteFunctionUrlConfigRequestRequestTypeDef(
    _RequiredDeleteFunctionUrlConfigRequestRequestTypeDef,
    _OptionalDeleteFunctionUrlConfigRequestRequestTypeDef,
):
    pass

DeleteLayerVersionRequestRequestTypeDef = TypedDict(
    "DeleteLayerVersionRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

DeleteProvisionedConcurrencyConfigRequestRequestTypeDef = TypedDict(
    "DeleteProvisionedConcurrencyConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
    },
)

DestinationConfigTypeDef = TypedDict(
    "DestinationConfigTypeDef",
    {
        "OnSuccess": "OnSuccessTypeDef",
        "OnFailure": "OnFailureTypeDef",
    },
    total=False,
)

DocumentDBEventSourceConfigTypeDef = TypedDict(
    "DocumentDBEventSourceConfigTypeDef",
    {
        "DatabaseName": str,
        "CollectionName": str,
        "FullDocument": FullDocumentType,
    },
    total=False,
)

EnvironmentErrorTypeDef = TypedDict(
    "EnvironmentErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

EnvironmentResponseTypeDef = TypedDict(
    "EnvironmentResponseTypeDef",
    {
        "Variables": Dict[str, str],
        "Error": "EnvironmentErrorTypeDef",
    },
    total=False,
)

EnvironmentTypeDef = TypedDict(
    "EnvironmentTypeDef",
    {
        "Variables": Dict[str, str],
    },
    total=False,
)

EphemeralStorageTypeDef = TypedDict(
    "EphemeralStorageTypeDef",
    {
        "Size": int,
    },
)

EventSourceMappingConfigurationResponseMetadataTypeDef = TypedDict(
    "EventSourceMappingConfigurationResponseMetadataTypeDef",
    {
        "UUID": str,
        "StartingPosition": EventSourcePositionType,
        "StartingPositionTimestamp": datetime,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FilterCriteria": "FilterCriteriaTypeDef",
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": "DestinationConfigTypeDef",
        "Topics": List[str],
        "Queues": List[str],
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "SelfManagedEventSource": "SelfManagedEventSourceTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "TumblingWindowInSeconds": int,
        "FunctionResponseTypes": List[Literal["ReportBatchItemFailures"]],
        "AmazonManagedKafkaEventSourceConfig": "AmazonManagedKafkaEventSourceConfigTypeDef",
        "SelfManagedKafkaEventSourceConfig": "SelfManagedKafkaEventSourceConfigTypeDef",
        "ScalingConfig": "ScalingConfigTypeDef",
        "DocumentDBEventSourceConfig": "DocumentDBEventSourceConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventSourceMappingConfigurationTypeDef = TypedDict(
    "EventSourceMappingConfigurationTypeDef",
    {
        "UUID": str,
        "StartingPosition": EventSourcePositionType,
        "StartingPositionTimestamp": datetime,
        "BatchSize": int,
        "MaximumBatchingWindowInSeconds": int,
        "ParallelizationFactor": int,
        "EventSourceArn": str,
        "FilterCriteria": "FilterCriteriaTypeDef",
        "FunctionArn": str,
        "LastModified": datetime,
        "LastProcessingResult": str,
        "State": str,
        "StateTransitionReason": str,
        "DestinationConfig": "DestinationConfigTypeDef",
        "Topics": List[str],
        "Queues": List[str],
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "SelfManagedEventSource": "SelfManagedEventSourceTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "TumblingWindowInSeconds": int,
        "FunctionResponseTypes": List[Literal["ReportBatchItemFailures"]],
        "AmazonManagedKafkaEventSourceConfig": "AmazonManagedKafkaEventSourceConfigTypeDef",
        "SelfManagedKafkaEventSourceConfig": "SelfManagedKafkaEventSourceConfigTypeDef",
        "ScalingConfig": "ScalingConfigTypeDef",
        "DocumentDBEventSourceConfig": "DocumentDBEventSourceConfigTypeDef",
    },
    total=False,
)

FileSystemConfigTypeDef = TypedDict(
    "FileSystemConfigTypeDef",
    {
        "Arn": str,
        "LocalMountPath": str,
    },
)

FilterCriteriaTypeDef = TypedDict(
    "FilterCriteriaTypeDef",
    {
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Pattern": str,
    },
    total=False,
)

FunctionCodeLocationTypeDef = TypedDict(
    "FunctionCodeLocationTypeDef",
    {
        "RepositoryType": str,
        "Location": str,
        "ImageUri": str,
        "ResolvedImageUri": str,
    },
    total=False,
)

FunctionCodeTypeDef = TypedDict(
    "FunctionCodeTypeDef",
    {
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ImageUri": str,
    },
    total=False,
)

FunctionConfigurationResponseMetadataTypeDef = TypedDict(
    "FunctionConfigurationResponseMetadataTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": RuntimeType,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": "VpcConfigResponseTypeDef",
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "Environment": "EnvironmentResponseTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigResponseTypeDef",
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List["LayerTypeDef"],
        "State": StateType,
        "StateReason": str,
        "StateReasonCode": StateReasonCodeType,
        "LastUpdateStatus": LastUpdateStatusType,
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": LastUpdateStatusReasonCodeType,
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "PackageType": PackageTypeType,
        "ImageConfigResponse": "ImageConfigResponseTypeDef",
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
        "Architectures": List[ArchitectureType],
        "EphemeralStorage": "EphemeralStorageTypeDef",
        "SnapStart": "SnapStartResponseTypeDef",
        "RuntimeVersionConfig": "RuntimeVersionConfigTypeDef",
        "LoggingConfig": "LoggingConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FunctionConfigurationTypeDef = TypedDict(
    "FunctionConfigurationTypeDef",
    {
        "FunctionName": str,
        "FunctionArn": str,
        "Runtime": RuntimeType,
        "Role": str,
        "Handler": str,
        "CodeSize": int,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "LastModified": str,
        "CodeSha256": str,
        "Version": str,
        "VpcConfig": "VpcConfigResponseTypeDef",
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "Environment": "EnvironmentResponseTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigResponseTypeDef",
        "MasterArn": str,
        "RevisionId": str,
        "Layers": List["LayerTypeDef"],
        "State": StateType,
        "StateReason": str,
        "StateReasonCode": StateReasonCodeType,
        "LastUpdateStatus": LastUpdateStatusType,
        "LastUpdateStatusReason": str,
        "LastUpdateStatusReasonCode": LastUpdateStatusReasonCodeType,
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "PackageType": PackageTypeType,
        "ImageConfigResponse": "ImageConfigResponseTypeDef",
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
        "Architectures": List[ArchitectureType],
        "EphemeralStorage": "EphemeralStorageTypeDef",
        "SnapStart": "SnapStartResponseTypeDef",
        "RuntimeVersionConfig": "RuntimeVersionConfigTypeDef",
        "LoggingConfig": "LoggingConfigTypeDef",
    },
    total=False,
)

FunctionEventInvokeConfigResponseMetadataTypeDef = TypedDict(
    "FunctionEventInvokeConfigResponseMetadataTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FunctionEventInvokeConfigTypeDef = TypedDict(
    "FunctionEventInvokeConfigTypeDef",
    {
        "LastModified": datetime,
        "FunctionArn": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
    },
    total=False,
)

_RequiredFunctionUrlConfigTypeDef = TypedDict(
    "_RequiredFunctionUrlConfigTypeDef",
    {
        "FunctionUrl": str,
        "FunctionArn": str,
        "CreationTime": str,
        "LastModifiedTime": str,
        "AuthType": FunctionUrlAuthTypeType,
    },
)
_OptionalFunctionUrlConfigTypeDef = TypedDict(
    "_OptionalFunctionUrlConfigTypeDef",
    {
        "Cors": "CorsTypeDef",
        "InvokeMode": InvokeModeType,
    },
    total=False,
)

class FunctionUrlConfigTypeDef(
    _RequiredFunctionUrlConfigTypeDef, _OptionalFunctionUrlConfigTypeDef
):
    pass

GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {
        "AccountLimit": "AccountLimitTypeDef",
        "AccountUsage": "AccountUsageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAliasRequestRequestTypeDef = TypedDict(
    "GetAliasRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
    },
)

GetCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "GetCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)

GetCodeSigningConfigResponseTypeDef = TypedDict(
    "GetCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventSourceMappingRequestRequestTypeDef = TypedDict(
    "GetEventSourceMappingRequestRequestTypeDef",
    {
        "UUID": str,
    },
)

GetFunctionCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "GetFunctionCodeSigningConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)

GetFunctionCodeSigningConfigResponseTypeDef = TypedDict(
    "GetFunctionCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFunctionConcurrencyRequestRequestTypeDef = TypedDict(
    "GetFunctionConcurrencyRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)

GetFunctionConcurrencyResponseTypeDef = TypedDict(
    "GetFunctionConcurrencyResponseTypeDef",
    {
        "ReservedConcurrentExecutions": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFunctionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetFunctionConfigurationRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetFunctionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetFunctionConfigurationRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class GetFunctionConfigurationRequestRequestTypeDef(
    _RequiredGetFunctionConfigurationRequestRequestTypeDef,
    _OptionalGetFunctionConfigurationRequestRequestTypeDef,
):
    pass

_RequiredGetFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "_RequiredGetFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "_OptionalGetFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class GetFunctionEventInvokeConfigRequestRequestTypeDef(
    _RequiredGetFunctionEventInvokeConfigRequestRequestTypeDef,
    _OptionalGetFunctionEventInvokeConfigRequestRequestTypeDef,
):
    pass

_RequiredGetFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredGetFunctionRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalGetFunctionRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class GetFunctionRequestRequestTypeDef(
    _RequiredGetFunctionRequestRequestTypeDef, _OptionalGetFunctionRequestRequestTypeDef
):
    pass

GetFunctionResponseTypeDef = TypedDict(
    "GetFunctionResponseTypeDef",
    {
        "Configuration": "FunctionConfigurationTypeDef",
        "Code": "FunctionCodeLocationTypeDef",
        "Tags": Dict[str, str],
        "Concurrency": "ConcurrencyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFunctionUrlConfigRequestRequestTypeDef = TypedDict(
    "_RequiredGetFunctionUrlConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetFunctionUrlConfigRequestRequestTypeDef = TypedDict(
    "_OptionalGetFunctionUrlConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class GetFunctionUrlConfigRequestRequestTypeDef(
    _RequiredGetFunctionUrlConfigRequestRequestTypeDef,
    _OptionalGetFunctionUrlConfigRequestRequestTypeDef,
):
    pass

GetFunctionUrlConfigResponseTypeDef = TypedDict(
    "GetFunctionUrlConfigResponseTypeDef",
    {
        "FunctionUrl": str,
        "FunctionArn": str,
        "AuthType": FunctionUrlAuthTypeType,
        "Cors": "CorsTypeDef",
        "CreationTime": str,
        "LastModifiedTime": str,
        "InvokeMode": InvokeModeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLayerVersionByArnRequestRequestTypeDef = TypedDict(
    "GetLayerVersionByArnRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

GetLayerVersionPolicyRequestRequestTypeDef = TypedDict(
    "GetLayerVersionPolicyRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

GetLayerVersionPolicyResponseTypeDef = TypedDict(
    "GetLayerVersionPolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLayerVersionRequestRequestTypeDef = TypedDict(
    "GetLayerVersionRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
    },
)

GetLayerVersionResponseTypeDef = TypedDict(
    "GetLayerVersionResponseTypeDef",
    {
        "Content": "LayerVersionContentOutputTypeDef",
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
        "CompatibleArchitectures": List[ArchitectureType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetPolicyRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetPolicyRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class GetPolicyRequestRequestTypeDef(
    _RequiredGetPolicyRequestRequestTypeDef, _OptionalGetPolicyRequestRequestTypeDef
):
    pass

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProvisionedConcurrencyConfigRequestRequestTypeDef = TypedDict(
    "GetProvisionedConcurrencyConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
    },
)

GetProvisionedConcurrencyConfigResponseTypeDef = TypedDict(
    "GetProvisionedConcurrencyConfigResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnumType,
        "StatusReason": str,
        "LastModified": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRuntimeManagementConfigRequestRequestTypeDef = TypedDict(
    "_RequiredGetRuntimeManagementConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalGetRuntimeManagementConfigRequestRequestTypeDef = TypedDict(
    "_OptionalGetRuntimeManagementConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
    },
    total=False,
)

class GetRuntimeManagementConfigRequestRequestTypeDef(
    _RequiredGetRuntimeManagementConfigRequestRequestTypeDef,
    _OptionalGetRuntimeManagementConfigRequestRequestTypeDef,
):
    pass

GetRuntimeManagementConfigResponseTypeDef = TypedDict(
    "GetRuntimeManagementConfigResponseTypeDef",
    {
        "UpdateRuntimeOn": UpdateRuntimeOnType,
        "RuntimeVersionArn": str,
        "FunctionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageConfigErrorTypeDef = TypedDict(
    "ImageConfigErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

ImageConfigResponseTypeDef = TypedDict(
    "ImageConfigResponseTypeDef",
    {
        "ImageConfig": "ImageConfigTypeDef",
        "Error": "ImageConfigErrorTypeDef",
    },
    total=False,
)

ImageConfigTypeDef = TypedDict(
    "ImageConfigTypeDef",
    {
        "EntryPoint": List[str],
        "Command": List[str],
        "WorkingDirectory": str,
    },
    total=False,
)

_RequiredInvocationRequestRequestTypeDef = TypedDict(
    "_RequiredInvocationRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalInvocationRequestRequestTypeDef = TypedDict(
    "_OptionalInvocationRequestRequestTypeDef",
    {
        "InvocationType": InvocationTypeType,
        "LogType": LogTypeType,
        "ClientContext": str,
        "Payload": Union[bytes, IO[bytes], StreamingBody],
        "Qualifier": str,
    },
    total=False,
)

class InvocationRequestRequestTypeDef(
    _RequiredInvocationRequestRequestTypeDef, _OptionalInvocationRequestRequestTypeDef
):
    pass

InvocationResponseTypeDef = TypedDict(
    "InvocationResponseTypeDef",
    {
        "StatusCode": int,
        "FunctionError": str,
        "LogResult": str,
        "Payload": IO[bytes],
        "ExecutedVersion": str,
    },
    total=False,
)

InvokeAsyncRequestRequestTypeDef = TypedDict(
    "InvokeAsyncRequestRequestTypeDef",
    {
        "FunctionName": str,
        "InvokeArgs": Union[bytes, IO[bytes], StreamingBody],
    },
)

InvokeAsyncResponseTypeDef = TypedDict(
    "InvokeAsyncResponseTypeDef",
    {
        "Status": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvokeResponseStreamUpdateTypeDef = TypedDict(
    "InvokeResponseStreamUpdateTypeDef",
    {
        "Payload": bytes,
    },
    total=False,
)

InvokeWithResponseStreamCompleteEventTypeDef = TypedDict(
    "InvokeWithResponseStreamCompleteEventTypeDef",
    {
        "ErrorCode": str,
        "ErrorDetails": str,
        "LogResult": str,
    },
    total=False,
)

_RequiredInvokeWithResponseStreamRequestRequestTypeDef = TypedDict(
    "_RequiredInvokeWithResponseStreamRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalInvokeWithResponseStreamRequestRequestTypeDef = TypedDict(
    "_OptionalInvokeWithResponseStreamRequestRequestTypeDef",
    {
        "InvocationType": ResponseStreamingInvocationTypeType,
        "LogType": LogTypeType,
        "ClientContext": str,
        "Qualifier": str,
        "Payload": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

class InvokeWithResponseStreamRequestRequestTypeDef(
    _RequiredInvokeWithResponseStreamRequestRequestTypeDef,
    _OptionalInvokeWithResponseStreamRequestRequestTypeDef,
):
    pass

InvokeWithResponseStreamResponseEventTypeDef = TypedDict(
    "InvokeWithResponseStreamResponseEventTypeDef",
    {
        "PayloadChunk": "InvokeResponseStreamUpdateTypeDef",
        "InvokeComplete": "InvokeWithResponseStreamCompleteEventTypeDef",
    },
    total=False,
)

InvokeWithResponseStreamResponseTypeDef = TypedDict(
    "InvokeWithResponseStreamResponseTypeDef",
    {
        "StatusCode": int,
        "ExecutedVersion": str,
        "EventStream": "InvokeWithResponseStreamResponseEventTypeDef",
        "ResponseStreamContentType": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": str,
        "CodeSize": int,
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
    },
    total=False,
)

LayerVersionContentInputTypeDef = TypedDict(
    "LayerVersionContentInputTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

LayerVersionContentOutputTypeDef = TypedDict(
    "LayerVersionContentOutputTypeDef",
    {
        "Location": str,
        "CodeSha256": str,
        "CodeSize": int,
        "SigningProfileVersionArn": str,
        "SigningJobArn": str,
    },
    total=False,
)

LayerVersionsListItemTypeDef = TypedDict(
    "LayerVersionsListItemTypeDef",
    {
        "LayerVersionArn": str,
        "Version": int,
        "Description": str,
        "CreatedDate": str,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
        "CompatibleArchitectures": List[ArchitectureType],
    },
    total=False,
)

LayersListItemTypeDef = TypedDict(
    "LayersListItemTypeDef",
    {
        "LayerName": str,
        "LayerArn": str,
        "LatestMatchingVersion": "LayerVersionsListItemTypeDef",
    },
    total=False,
)

_RequiredListAliasesRequestRequestTypeDef = TypedDict(
    "_RequiredListAliasesRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListAliasesRequestRequestTypeDef = TypedDict(
    "_OptionalListAliasesRequestRequestTypeDef",
    {
        "FunctionVersion": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListAliasesRequestRequestTypeDef(
    _RequiredListAliasesRequestRequestTypeDef, _OptionalListAliasesRequestRequestTypeDef
):
    pass

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {
        "NextMarker": str,
        "Aliases": List["AliasConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCodeSigningConfigsRequestRequestTypeDef = TypedDict(
    "ListCodeSigningConfigsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListCodeSigningConfigsResponseTypeDef = TypedDict(
    "ListCodeSigningConfigsResponseTypeDef",
    {
        "NextMarker": str,
        "CodeSigningConfigs": List["CodeSigningConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventSourceMappingsRequestRequestTypeDef = TypedDict(
    "ListEventSourceMappingsRequestRequestTypeDef",
    {
        "EventSourceArn": str,
        "FunctionName": str,
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListEventSourceMappingsResponseTypeDef = TypedDict(
    "ListEventSourceMappingsResponseTypeDef",
    {
        "NextMarker": str,
        "EventSourceMappings": List["EventSourceMappingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionEventInvokeConfigsRequestRequestTypeDef = TypedDict(
    "_RequiredListFunctionEventInvokeConfigsRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListFunctionEventInvokeConfigsRequestRequestTypeDef = TypedDict(
    "_OptionalListFunctionEventInvokeConfigsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListFunctionEventInvokeConfigsRequestRequestTypeDef(
    _RequiredListFunctionEventInvokeConfigsRequestRequestTypeDef,
    _OptionalListFunctionEventInvokeConfigsRequestRequestTypeDef,
):
    pass

ListFunctionEventInvokeConfigsResponseTypeDef = TypedDict(
    "ListFunctionEventInvokeConfigsResponseTypeDef",
    {
        "FunctionEventInvokeConfigs": List["FunctionEventInvokeConfigTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionUrlConfigsRequestRequestTypeDef = TypedDict(
    "_RequiredListFunctionUrlConfigsRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListFunctionUrlConfigsRequestRequestTypeDef = TypedDict(
    "_OptionalListFunctionUrlConfigsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListFunctionUrlConfigsRequestRequestTypeDef(
    _RequiredListFunctionUrlConfigsRequestRequestTypeDef,
    _OptionalListFunctionUrlConfigsRequestRequestTypeDef,
):
    pass

ListFunctionUrlConfigsResponseTypeDef = TypedDict(
    "ListFunctionUrlConfigsResponseTypeDef",
    {
        "FunctionUrlConfigs": List["FunctionUrlConfigTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFunctionsByCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "_RequiredListFunctionsByCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)
_OptionalListFunctionsByCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "_OptionalListFunctionsByCodeSigningConfigRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListFunctionsByCodeSigningConfigRequestRequestTypeDef(
    _RequiredListFunctionsByCodeSigningConfigRequestRequestTypeDef,
    _OptionalListFunctionsByCodeSigningConfigRequestRequestTypeDef,
):
    pass

ListFunctionsByCodeSigningConfigResponseTypeDef = TypedDict(
    "ListFunctionsByCodeSigningConfigResponseTypeDef",
    {
        "NextMarker": str,
        "FunctionArns": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFunctionsRequestRequestTypeDef = TypedDict(
    "ListFunctionsRequestRequestTypeDef",
    {
        "MasterRegion": str,
        "FunctionVersion": Literal["ALL"],
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

ListFunctionsResponseTypeDef = TypedDict(
    "ListFunctionsResponseTypeDef",
    {
        "NextMarker": str,
        "Functions": List["FunctionConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListLayerVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListLayerVersionsRequestRequestTypeDef",
    {
        "LayerName": str,
    },
)
_OptionalListLayerVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListLayerVersionsRequestRequestTypeDef",
    {
        "CompatibleRuntime": RuntimeType,
        "Marker": str,
        "MaxItems": int,
        "CompatibleArchitecture": ArchitectureType,
    },
    total=False,
)

class ListLayerVersionsRequestRequestTypeDef(
    _RequiredListLayerVersionsRequestRequestTypeDef, _OptionalListLayerVersionsRequestRequestTypeDef
):
    pass

ListLayerVersionsResponseTypeDef = TypedDict(
    "ListLayerVersionsResponseTypeDef",
    {
        "NextMarker": str,
        "LayerVersions": List["LayerVersionsListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLayersRequestRequestTypeDef = TypedDict(
    "ListLayersRequestRequestTypeDef",
    {
        "CompatibleRuntime": RuntimeType,
        "Marker": str,
        "MaxItems": int,
        "CompatibleArchitecture": ArchitectureType,
    },
    total=False,
)

ListLayersResponseTypeDef = TypedDict(
    "ListLayersResponseTypeDef",
    {
        "NextMarker": str,
        "Layers": List["LayersListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProvisionedConcurrencyConfigsRequestRequestTypeDef = TypedDict(
    "_RequiredListProvisionedConcurrencyConfigsRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListProvisionedConcurrencyConfigsRequestRequestTypeDef = TypedDict(
    "_OptionalListProvisionedConcurrencyConfigsRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListProvisionedConcurrencyConfigsRequestRequestTypeDef(
    _RequiredListProvisionedConcurrencyConfigsRequestRequestTypeDef,
    _OptionalListProvisionedConcurrencyConfigsRequestRequestTypeDef,
):
    pass

ListProvisionedConcurrencyConfigsResponseTypeDef = TypedDict(
    "ListProvisionedConcurrencyConfigsResponseTypeDef",
    {
        "ProvisionedConcurrencyConfigs": List["ProvisionedConcurrencyConfigListItemTypeDef"],
        "NextMarker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "Resource": str,
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListVersionsByFunctionRequestRequestTypeDef = TypedDict(
    "_RequiredListVersionsByFunctionRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalListVersionsByFunctionRequestRequestTypeDef = TypedDict(
    "_OptionalListVersionsByFunctionRequestRequestTypeDef",
    {
        "Marker": str,
        "MaxItems": int,
    },
    total=False,
)

class ListVersionsByFunctionRequestRequestTypeDef(
    _RequiredListVersionsByFunctionRequestRequestTypeDef,
    _OptionalListVersionsByFunctionRequestRequestTypeDef,
):
    pass

ListVersionsByFunctionResponseTypeDef = TypedDict(
    "ListVersionsByFunctionResponseTypeDef",
    {
        "NextMarker": str,
        "Versions": List["FunctionConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "LogFormat": LogFormatType,
        "ApplicationLogLevel": ApplicationLogLevelType,
        "SystemLogLevel": SystemLogLevelType,
        "LogGroup": str,
    },
    total=False,
)

OnFailureTypeDef = TypedDict(
    "OnFailureTypeDef",
    {
        "Destination": str,
    },
    total=False,
)

OnSuccessTypeDef = TypedDict(
    "OnSuccessTypeDef",
    {
        "Destination": str,
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

ProvisionedConcurrencyConfigListItemTypeDef = TypedDict(
    "ProvisionedConcurrencyConfigListItemTypeDef",
    {
        "FunctionArn": str,
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnumType,
        "StatusReason": str,
        "LastModified": str,
    },
    total=False,
)

_RequiredPublishLayerVersionRequestRequestTypeDef = TypedDict(
    "_RequiredPublishLayerVersionRequestRequestTypeDef",
    {
        "LayerName": str,
        "Content": "LayerVersionContentInputTypeDef",
    },
)
_OptionalPublishLayerVersionRequestRequestTypeDef = TypedDict(
    "_OptionalPublishLayerVersionRequestRequestTypeDef",
    {
        "Description": str,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
        "CompatibleArchitectures": List[ArchitectureType],
    },
    total=False,
)

class PublishLayerVersionRequestRequestTypeDef(
    _RequiredPublishLayerVersionRequestRequestTypeDef,
    _OptionalPublishLayerVersionRequestRequestTypeDef,
):
    pass

PublishLayerVersionResponseTypeDef = TypedDict(
    "PublishLayerVersionResponseTypeDef",
    {
        "Content": "LayerVersionContentOutputTypeDef",
        "LayerArn": str,
        "LayerVersionArn": str,
        "Description": str,
        "CreatedDate": str,
        "Version": int,
        "CompatibleRuntimes": List[RuntimeType],
        "LicenseInfo": str,
        "CompatibleArchitectures": List[ArchitectureType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPublishVersionRequestRequestTypeDef = TypedDict(
    "_RequiredPublishVersionRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalPublishVersionRequestRequestTypeDef = TypedDict(
    "_OptionalPublishVersionRequestRequestTypeDef",
    {
        "CodeSha256": str,
        "Description": str,
        "RevisionId": str,
    },
    total=False,
)

class PublishVersionRequestRequestTypeDef(
    _RequiredPublishVersionRequestRequestTypeDef, _OptionalPublishVersionRequestRequestTypeDef
):
    pass

PutFunctionCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "PutFunctionCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
    },
)

PutFunctionCodeSigningConfigResponseTypeDef = TypedDict(
    "PutFunctionCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfigArn": str,
        "FunctionName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutFunctionConcurrencyRequestRequestTypeDef = TypedDict(
    "PutFunctionConcurrencyRequestRequestTypeDef",
    {
        "FunctionName": str,
        "ReservedConcurrentExecutions": int,
    },
)

_RequiredPutFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "_RequiredPutFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalPutFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "_OptionalPutFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
    },
    total=False,
)

class PutFunctionEventInvokeConfigRequestRequestTypeDef(
    _RequiredPutFunctionEventInvokeConfigRequestRequestTypeDef,
    _OptionalPutFunctionEventInvokeConfigRequestRequestTypeDef,
):
    pass

PutProvisionedConcurrencyConfigRequestRequestTypeDef = TypedDict(
    "PutProvisionedConcurrencyConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Qualifier": str,
        "ProvisionedConcurrentExecutions": int,
    },
)

PutProvisionedConcurrencyConfigResponseTypeDef = TypedDict(
    "PutProvisionedConcurrencyConfigResponseTypeDef",
    {
        "RequestedProvisionedConcurrentExecutions": int,
        "AvailableProvisionedConcurrentExecutions": int,
        "AllocatedProvisionedConcurrentExecutions": int,
        "Status": ProvisionedConcurrencyStatusEnumType,
        "StatusReason": str,
        "LastModified": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRuntimeManagementConfigRequestRequestTypeDef = TypedDict(
    "_RequiredPutRuntimeManagementConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
        "UpdateRuntimeOn": UpdateRuntimeOnType,
    },
)
_OptionalPutRuntimeManagementConfigRequestRequestTypeDef = TypedDict(
    "_OptionalPutRuntimeManagementConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
        "RuntimeVersionArn": str,
    },
    total=False,
)

class PutRuntimeManagementConfigRequestRequestTypeDef(
    _RequiredPutRuntimeManagementConfigRequestRequestTypeDef,
    _OptionalPutRuntimeManagementConfigRequestRequestTypeDef,
):
    pass

PutRuntimeManagementConfigResponseTypeDef = TypedDict(
    "PutRuntimeManagementConfigResponseTypeDef",
    {
        "UpdateRuntimeOn": UpdateRuntimeOnType,
        "FunctionArn": str,
        "RuntimeVersionArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRemoveLayerVersionPermissionRequestRequestTypeDef = TypedDict(
    "_RequiredRemoveLayerVersionPermissionRequestRequestTypeDef",
    {
        "LayerName": str,
        "VersionNumber": int,
        "StatementId": str,
    },
)
_OptionalRemoveLayerVersionPermissionRequestRequestTypeDef = TypedDict(
    "_OptionalRemoveLayerVersionPermissionRequestRequestTypeDef",
    {
        "RevisionId": str,
    },
    total=False,
)

class RemoveLayerVersionPermissionRequestRequestTypeDef(
    _RequiredRemoveLayerVersionPermissionRequestRequestTypeDef,
    _OptionalRemoveLayerVersionPermissionRequestRequestTypeDef,
):
    pass

_RequiredRemovePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredRemovePermissionRequestRequestTypeDef",
    {
        "FunctionName": str,
        "StatementId": str,
    },
)
_OptionalRemovePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalRemovePermissionRequestRequestTypeDef",
    {
        "Qualifier": str,
        "RevisionId": str,
    },
    total=False,
)

class RemovePermissionRequestRequestTypeDef(
    _RequiredRemovePermissionRequestRequestTypeDef, _OptionalRemovePermissionRequestRequestTypeDef
):
    pass

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

RuntimeVersionConfigTypeDef = TypedDict(
    "RuntimeVersionConfigTypeDef",
    {
        "RuntimeVersionArn": str,
        "Error": "RuntimeVersionErrorTypeDef",
    },
    total=False,
)

RuntimeVersionErrorTypeDef = TypedDict(
    "RuntimeVersionErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
    },
    total=False,
)

ScalingConfigTypeDef = TypedDict(
    "ScalingConfigTypeDef",
    {
        "MaximumConcurrency": int,
    },
    total=False,
)

SelfManagedEventSourceTypeDef = TypedDict(
    "SelfManagedEventSourceTypeDef",
    {
        "Endpoints": Dict[Literal["KAFKA_BOOTSTRAP_SERVERS"], List[str]],
    },
    total=False,
)

SelfManagedKafkaEventSourceConfigTypeDef = TypedDict(
    "SelfManagedKafkaEventSourceConfigTypeDef",
    {
        "ConsumerGroupId": str,
    },
    total=False,
)

SnapStartResponseTypeDef = TypedDict(
    "SnapStartResponseTypeDef",
    {
        "ApplyOn": SnapStartApplyOnType,
        "OptimizationStatus": SnapStartOptimizationStatusType,
    },
    total=False,
)

SnapStartTypeDef = TypedDict(
    "SnapStartTypeDef",
    {
        "ApplyOn": SnapStartApplyOnType,
    },
    total=False,
)

SourceAccessConfigurationTypeDef = TypedDict(
    "SourceAccessConfigurationTypeDef",
    {
        "Type": SourceAccessTypeType,
        "URI": str,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "Tags": Dict[str, str],
    },
)

TracingConfigResponseTypeDef = TypedDict(
    "TracingConfigResponseTypeDef",
    {
        "Mode": TracingModeType,
    },
    total=False,
)

TracingConfigTypeDef = TypedDict(
    "TracingConfigTypeDef",
    {
        "Mode": TracingModeType,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Resource": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateAliasRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAliasRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Name": str,
    },
)
_OptionalUpdateAliasRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAliasRequestRequestTypeDef",
    {
        "FunctionVersion": str,
        "Description": str,
        "RoutingConfig": "AliasRoutingConfigurationTypeDef",
        "RevisionId": str,
    },
    total=False,
)

class UpdateAliasRequestRequestTypeDef(
    _RequiredUpdateAliasRequestRequestTypeDef, _OptionalUpdateAliasRequestRequestTypeDef
):
    pass

_RequiredUpdateCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCodeSigningConfigRequestRequestTypeDef",
    {
        "CodeSigningConfigArn": str,
    },
)
_OptionalUpdateCodeSigningConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCodeSigningConfigRequestRequestTypeDef",
    {
        "Description": str,
        "AllowedPublishers": "AllowedPublishersTypeDef",
        "CodeSigningPolicies": "CodeSigningPoliciesTypeDef",
    },
    total=False,
)

class UpdateCodeSigningConfigRequestRequestTypeDef(
    _RequiredUpdateCodeSigningConfigRequestRequestTypeDef,
    _OptionalUpdateCodeSigningConfigRequestRequestTypeDef,
):
    pass

UpdateCodeSigningConfigResponseTypeDef = TypedDict(
    "UpdateCodeSigningConfigResponseTypeDef",
    {
        "CodeSigningConfig": "CodeSigningConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEventSourceMappingRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEventSourceMappingRequestRequestTypeDef",
    {
        "UUID": str,
    },
)
_OptionalUpdateEventSourceMappingRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEventSourceMappingRequestRequestTypeDef",
    {
        "FunctionName": str,
        "Enabled": bool,
        "BatchSize": int,
        "FilterCriteria": "FilterCriteriaTypeDef",
        "MaximumBatchingWindowInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
        "MaximumRecordAgeInSeconds": int,
        "BisectBatchOnFunctionError": bool,
        "MaximumRetryAttempts": int,
        "ParallelizationFactor": int,
        "SourceAccessConfigurations": List["SourceAccessConfigurationTypeDef"],
        "TumblingWindowInSeconds": int,
        "FunctionResponseTypes": List[Literal["ReportBatchItemFailures"]],
        "ScalingConfig": "ScalingConfigTypeDef",
        "DocumentDBEventSourceConfig": "DocumentDBEventSourceConfigTypeDef",
    },
    total=False,
)

class UpdateEventSourceMappingRequestRequestTypeDef(
    _RequiredUpdateEventSourceMappingRequestRequestTypeDef,
    _OptionalUpdateEventSourceMappingRequestRequestTypeDef,
):
    pass

_RequiredUpdateFunctionCodeRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionCodeRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalUpdateFunctionCodeRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionCodeRequestRequestTypeDef",
    {
        "ZipFile": Union[bytes, IO[bytes], StreamingBody],
        "S3Bucket": str,
        "S3Key": str,
        "S3ObjectVersion": str,
        "ImageUri": str,
        "Publish": bool,
        "DryRun": bool,
        "RevisionId": str,
        "Architectures": List[ArchitectureType],
    },
    total=False,
)

class UpdateFunctionCodeRequestRequestTypeDef(
    _RequiredUpdateFunctionCodeRequestRequestTypeDef,
    _OptionalUpdateFunctionCodeRequestRequestTypeDef,
):
    pass

_RequiredUpdateFunctionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionConfigurationRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalUpdateFunctionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionConfigurationRequestRequestTypeDef",
    {
        "Role": str,
        "Handler": str,
        "Description": str,
        "Timeout": int,
        "MemorySize": int,
        "VpcConfig": "VpcConfigTypeDef",
        "Environment": "EnvironmentTypeDef",
        "Runtime": RuntimeType,
        "DeadLetterConfig": "DeadLetterConfigTypeDef",
        "KMSKeyArn": str,
        "TracingConfig": "TracingConfigTypeDef",
        "RevisionId": str,
        "Layers": List[str],
        "FileSystemConfigs": List["FileSystemConfigTypeDef"],
        "ImageConfig": "ImageConfigTypeDef",
        "EphemeralStorage": "EphemeralStorageTypeDef",
        "SnapStart": "SnapStartTypeDef",
        "LoggingConfig": "LoggingConfigTypeDef",
    },
    total=False,
)

class UpdateFunctionConfigurationRequestRequestTypeDef(
    _RequiredUpdateFunctionConfigurationRequestRequestTypeDef,
    _OptionalUpdateFunctionConfigurationRequestRequestTypeDef,
):
    pass

_RequiredUpdateFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalUpdateFunctionEventInvokeConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionEventInvokeConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
        "MaximumRetryAttempts": int,
        "MaximumEventAgeInSeconds": int,
        "DestinationConfig": "DestinationConfigTypeDef",
    },
    total=False,
)

class UpdateFunctionEventInvokeConfigRequestRequestTypeDef(
    _RequiredUpdateFunctionEventInvokeConfigRequestRequestTypeDef,
    _OptionalUpdateFunctionEventInvokeConfigRequestRequestTypeDef,
):
    pass

_RequiredUpdateFunctionUrlConfigRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFunctionUrlConfigRequestRequestTypeDef",
    {
        "FunctionName": str,
    },
)
_OptionalUpdateFunctionUrlConfigRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFunctionUrlConfigRequestRequestTypeDef",
    {
        "Qualifier": str,
        "AuthType": FunctionUrlAuthTypeType,
        "Cors": "CorsTypeDef",
        "InvokeMode": InvokeModeType,
    },
    total=False,
)

class UpdateFunctionUrlConfigRequestRequestTypeDef(
    _RequiredUpdateFunctionUrlConfigRequestRequestTypeDef,
    _OptionalUpdateFunctionUrlConfigRequestRequestTypeDef,
):
    pass

UpdateFunctionUrlConfigResponseTypeDef = TypedDict(
    "UpdateFunctionUrlConfigResponseTypeDef",
    {
        "FunctionUrl": str,
        "FunctionArn": str,
        "AuthType": FunctionUrlAuthTypeType,
        "Cors": "CorsTypeDef",
        "CreationTime": str,
        "LastModifiedTime": str,
        "InvokeMode": InvokeModeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigResponseTypeDef = TypedDict(
    "VpcConfigResponseTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "VpcId": str,
        "Ipv6AllowedForDualStack": bool,
    },
    total=False,
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "Ipv6AllowedForDualStack": bool,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)
