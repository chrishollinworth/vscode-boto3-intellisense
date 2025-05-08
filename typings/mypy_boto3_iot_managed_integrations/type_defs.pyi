"""
Type annotations for iot-managed-integrations service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iot_managed_integrations/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iot_managed_integrations.type_defs import AbortConfigCriteriaTypeDef

    data: AbortConfigCriteriaTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any, Union

from .literals import (
    AbortCriteriaFailureTypeType,
    AuthMaterialTypeType,
    ConfigurationStateType,
    DeviceDiscoveryStatusType,
    DisconnectReasonValueType,
    DiscoveryTypeType,
    EncryptionTypeType,
    EventTypeType,
    HubNetworkModeType,
    LogLevelType,
    OtaStatusType,
    OtaTaskExecutionStatusType,
    OtaTypeType,
    ProvisioningStatusType,
    ProvisioningTypeType,
    RetryCriteriaFailureTypeType,
    RoleType,
    SchedulingConfigEndBehaviorType,
    SchemaVersionFormatType,
    SchemaVersionTypeType,
    SchemaVersionVisibilityType,
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
    "AbortConfigCriteriaTypeDef",
    "CapabilityActionTypeDef",
    "CapabilityReportCapabilityOutputTypeDef",
    "CapabilityReportCapabilityTypeDef",
    "CapabilityReportEndpointOutputTypeDef",
    "CapabilityReportEndpointTypeDef",
    "CapabilityReportOutputTypeDef",
    "CapabilityReportTypeDef",
    "CapabilityReportUnionTypeDef",
    "CommandCapabilityTypeDef",
    "CommandEndpointTypeDef",
    "ConfigurationErrorTypeDef",
    "ConfigurationStatusTypeDef",
    "CreateCredentialLockerRequestTypeDef",
    "CreateCredentialLockerResponseTypeDef",
    "CreateDestinationRequestTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateEventLogConfigurationRequestTypeDef",
    "CreateEventLogConfigurationResponseTypeDef",
    "CreateManagedThingRequestTypeDef",
    "CreateManagedThingResponseTypeDef",
    "CreateNotificationConfigurationRequestTypeDef",
    "CreateNotificationConfigurationResponseTypeDef",
    "CreateOtaTaskConfigurationRequestTypeDef",
    "CreateOtaTaskConfigurationResponseTypeDef",
    "CreateOtaTaskRequestTypeDef",
    "CreateOtaTaskResponseTypeDef",
    "CreateProvisioningProfileRequestTypeDef",
    "CreateProvisioningProfileResponseTypeDef",
    "CredentialLockerSummaryTypeDef",
    "DeleteCredentialLockerRequestTypeDef",
    "DeleteDestinationRequestTypeDef",
    "DeleteEventLogConfigurationRequestTypeDef",
    "DeleteManagedThingRequestTypeDef",
    "DeleteNotificationConfigurationRequestTypeDef",
    "DeleteOtaTaskConfigurationRequestTypeDef",
    "DeleteOtaTaskRequestTypeDef",
    "DeleteProvisioningProfileRequestTypeDef",
    "DestinationSummaryTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EventLogConfigurationSummaryTypeDef",
    "ExponentialRolloutRateTypeDef",
    "GetCredentialLockerRequestTypeDef",
    "GetCredentialLockerResponseTypeDef",
    "GetCustomEndpointResponseTypeDef",
    "GetDefaultEncryptionConfigurationResponseTypeDef",
    "GetDestinationRequestTypeDef",
    "GetDestinationResponseTypeDef",
    "GetDeviceDiscoveryRequestTypeDef",
    "GetDeviceDiscoveryResponseTypeDef",
    "GetEventLogConfigurationRequestTypeDef",
    "GetEventLogConfigurationResponseTypeDef",
    "GetHubConfigurationResponseTypeDef",
    "GetManagedThingCapabilitiesRequestTypeDef",
    "GetManagedThingCapabilitiesResponseTypeDef",
    "GetManagedThingConnectivityDataRequestTypeDef",
    "GetManagedThingConnectivityDataResponseTypeDef",
    "GetManagedThingMetaDataRequestTypeDef",
    "GetManagedThingMetaDataResponseTypeDef",
    "GetManagedThingRequestTypeDef",
    "GetManagedThingResponseTypeDef",
    "GetManagedThingStateRequestTypeDef",
    "GetManagedThingStateResponseTypeDef",
    "GetNotificationConfigurationRequestTypeDef",
    "GetNotificationConfigurationResponseTypeDef",
    "GetOtaTaskConfigurationRequestTypeDef",
    "GetOtaTaskConfigurationResponseTypeDef",
    "GetOtaTaskRequestTypeDef",
    "GetOtaTaskResponseTypeDef",
    "GetProvisioningProfileRequestTypeDef",
    "GetProvisioningProfileResponseTypeDef",
    "GetRuntimeLogConfigurationRequestTypeDef",
    "GetRuntimeLogConfigurationResponseTypeDef",
    "GetSchemaVersionRequestTypeDef",
    "GetSchemaVersionResponseTypeDef",
    "ListCredentialLockersRequestPaginateTypeDef",
    "ListCredentialLockersRequestTypeDef",
    "ListCredentialLockersResponseTypeDef",
    "ListDestinationsRequestPaginateTypeDef",
    "ListDestinationsRequestTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListEventLogConfigurationsRequestPaginateTypeDef",
    "ListEventLogConfigurationsRequestTypeDef",
    "ListEventLogConfigurationsResponseTypeDef",
    "ListManagedThingSchemasRequestPaginateTypeDef",
    "ListManagedThingSchemasRequestTypeDef",
    "ListManagedThingSchemasResponseTypeDef",
    "ListManagedThingsRequestPaginateTypeDef",
    "ListManagedThingsRequestTypeDef",
    "ListManagedThingsResponseTypeDef",
    "ListNotificationConfigurationsRequestPaginateTypeDef",
    "ListNotificationConfigurationsRequestTypeDef",
    "ListNotificationConfigurationsResponseTypeDef",
    "ListOtaTaskConfigurationsRequestPaginateTypeDef",
    "ListOtaTaskConfigurationsRequestTypeDef",
    "ListOtaTaskConfigurationsResponseTypeDef",
    "ListOtaTaskExecutionsRequestPaginateTypeDef",
    "ListOtaTaskExecutionsRequestTypeDef",
    "ListOtaTaskExecutionsResponseTypeDef",
    "ListOtaTasksRequestPaginateTypeDef",
    "ListOtaTasksRequestTypeDef",
    "ListOtaTasksResponseTypeDef",
    "ListProvisioningProfilesRequestPaginateTypeDef",
    "ListProvisioningProfilesRequestTypeDef",
    "ListProvisioningProfilesResponseTypeDef",
    "ListSchemaVersionsRequestPaginateTypeDef",
    "ListSchemaVersionsRequestTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ManagedThingSchemaListItemTypeDef",
    "ManagedThingSummaryTypeDef",
    "NotificationConfigurationSummaryTypeDef",
    "OtaTaskAbortConfigOutputTypeDef",
    "OtaTaskAbortConfigTypeDef",
    "OtaTaskConfigurationSummaryTypeDef",
    "OtaTaskExecutionRetryConfigOutputTypeDef",
    "OtaTaskExecutionRetryConfigTypeDef",
    "OtaTaskExecutionRetryConfigUnionTypeDef",
    "OtaTaskExecutionRolloutConfigTypeDef",
    "OtaTaskExecutionSummariesTypeDef",
    "OtaTaskExecutionSummaryTypeDef",
    "OtaTaskSchedulingConfigOutputTypeDef",
    "OtaTaskSchedulingConfigTypeDef",
    "OtaTaskSchedulingConfigUnionTypeDef",
    "OtaTaskSummaryTypeDef",
    "OtaTaskTimeoutConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ProvisioningProfileSummaryTypeDef",
    "PushConfigOutputTypeDef",
    "PushConfigTypeDef",
    "PushConfigUnionTypeDef",
    "PutDefaultEncryptionConfigurationRequestTypeDef",
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    "PutHubConfigurationRequestTypeDef",
    "PutHubConfigurationResponseTypeDef",
    "PutRuntimeLogConfigurationRequestTypeDef",
    "RegisterCustomEndpointResponseTypeDef",
    "ResetRuntimeLogConfigurationRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RetryConfigCriteriaTypeDef",
    "RolloutRateIncreaseCriteriaTypeDef",
    "RuntimeLogConfigurationsTypeDef",
    "ScheduleMaintenanceWindowTypeDef",
    "SchemaVersionListItemTypeDef",
    "SendManagedThingCommandRequestTypeDef",
    "SendManagedThingCommandResponseTypeDef",
    "StartDeviceDiscoveryRequestTypeDef",
    "StartDeviceDiscoveryResponseTypeDef",
    "StateCapabilityTypeDef",
    "StateEndpointTypeDef",
    "TaskProcessingDetailsTypeDef",
    "UpdateDestinationRequestTypeDef",
    "UpdateEventLogConfigurationRequestTypeDef",
    "UpdateManagedThingRequestTypeDef",
    "UpdateNotificationConfigurationRequestTypeDef",
    "UpdateOtaTaskRequestTypeDef",
)

class AbortConfigCriteriaTypeDef(TypedDict):
    Action: NotRequired[Literal["CANCEL"]]
    FailureType: NotRequired[AbortCriteriaFailureTypeType]
    MinNumberOfExecutedThings: NotRequired[int]
    ThresholdPercentage: NotRequired[float]

class CapabilityActionTypeDef(TypedDict):
    name: str
    ref: NotRequired[str]
    actionTraceId: NotRequired[str]
    parameters: NotRequired[Mapping[str, Any]]

CapabilityReportCapabilityOutputTypeDef = TypedDict(
    "CapabilityReportCapabilityOutputTypeDef",
    {
        "id": str,
        "name": str,
        "version": str,
        "properties": List[str],
        "actions": List[str],
        "events": List[str],
    },
)
CapabilityReportCapabilityTypeDef = TypedDict(
    "CapabilityReportCapabilityTypeDef",
    {
        "id": str,
        "name": str,
        "version": str,
        "properties": Sequence[str],
        "actions": Sequence[str],
        "events": Sequence[str],
    },
)

class ConfigurationErrorTypeDef(TypedDict):
    code: NotRequired[str]
    message: NotRequired[str]

class CreateCredentialLockerRequestTypeDef(TypedDict):
    Name: NotRequired[str]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateDestinationRequestTypeDef(TypedDict):
    DeliveryDestinationArn: str
    DeliveryDestinationType: Literal["KINESIS"]
    Name: str
    RoleArn: str
    ClientToken: NotRequired[str]
    Description: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateEventLogConfigurationRequestTypeDef(TypedDict):
    ResourceType: str
    EventLogLevel: LogLevelType
    ResourceId: NotRequired[str]
    ClientToken: NotRequired[str]

class CreateNotificationConfigurationRequestTypeDef(TypedDict):
    EventType: EventTypeType
    DestinationName: str
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CreateProvisioningProfileRequestTypeDef(TypedDict):
    ProvisioningType: ProvisioningTypeType
    CaCertificate: NotRequired[str]
    Name: NotRequired[str]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

class CredentialLockerSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    Name: NotRequired[str]
    CreatedAt: NotRequired[datetime]

class DeleteCredentialLockerRequestTypeDef(TypedDict):
    Identifier: str

class DeleteDestinationRequestTypeDef(TypedDict):
    Name: str

class DeleteEventLogConfigurationRequestTypeDef(TypedDict):
    Id: str

class DeleteManagedThingRequestTypeDef(TypedDict):
    Identifier: str
    Force: NotRequired[bool]

class DeleteNotificationConfigurationRequestTypeDef(TypedDict):
    EventType: EventTypeType

class DeleteOtaTaskConfigurationRequestTypeDef(TypedDict):
    Identifier: str

class DeleteOtaTaskRequestTypeDef(TypedDict):
    Identifier: str

class DeleteProvisioningProfileRequestTypeDef(TypedDict):
    Identifier: str

class DestinationSummaryTypeDef(TypedDict):
    Description: NotRequired[str]
    DeliveryDestinationArn: NotRequired[str]
    DeliveryDestinationType: NotRequired[Literal["KINESIS"]]
    Name: NotRequired[str]
    RoleArn: NotRequired[str]

class EventLogConfigurationSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    ResourceType: NotRequired[str]
    ResourceId: NotRequired[str]
    EventLogLevel: NotRequired[LogLevelType]

class RolloutRateIncreaseCriteriaTypeDef(TypedDict):
    numberOfNotifiedThings: NotRequired[int]
    numberOfSucceededThings: NotRequired[int]

class GetCredentialLockerRequestTypeDef(TypedDict):
    Identifier: str

class GetDestinationRequestTypeDef(TypedDict):
    Name: str

class GetDeviceDiscoveryRequestTypeDef(TypedDict):
    Identifier: str

class GetEventLogConfigurationRequestTypeDef(TypedDict):
    Id: str

class GetManagedThingCapabilitiesRequestTypeDef(TypedDict):
    Identifier: str

class GetManagedThingConnectivityDataRequestTypeDef(TypedDict):
    Identifier: str

class GetManagedThingMetaDataRequestTypeDef(TypedDict):
    Identifier: str

class GetManagedThingRequestTypeDef(TypedDict):
    Identifier: str

class GetManagedThingStateRequestTypeDef(TypedDict):
    ManagedThingId: str

class GetNotificationConfigurationRequestTypeDef(TypedDict):
    EventType: EventTypeType

class GetOtaTaskConfigurationRequestTypeDef(TypedDict):
    Identifier: str

class GetOtaTaskRequestTypeDef(TypedDict):
    Identifier: str

class TaskProcessingDetailsTypeDef(TypedDict):
    NumberOfCanceledThings: NotRequired[int]
    NumberOfFailedThings: NotRequired[int]
    NumberOfInProgressThings: NotRequired[int]
    numberOfQueuedThings: NotRequired[int]
    numberOfRejectedThings: NotRequired[int]
    numberOfRemovedThings: NotRequired[int]
    numberOfSucceededThings: NotRequired[int]
    numberOfTimedOutThings: NotRequired[int]
    processingTargets: NotRequired[List[str]]

class GetProvisioningProfileRequestTypeDef(TypedDict):
    Identifier: str

class GetRuntimeLogConfigurationRequestTypeDef(TypedDict):
    ManagedThingId: str

class RuntimeLogConfigurationsTypeDef(TypedDict):
    LogLevel: NotRequired[LogLevelType]
    LogFlushLevel: NotRequired[LogLevelType]
    LocalStoreLocation: NotRequired[str]
    LocalStoreFileRotationMaxFiles: NotRequired[int]
    LocalStoreFileRotationMaxBytes: NotRequired[int]
    UploadLog: NotRequired[bool]
    UploadPeriodMinutes: NotRequired[int]
    DeleteLocalStoreAfterUpload: NotRequired[bool]

GetSchemaVersionRequestTypeDef = TypedDict(
    "GetSchemaVersionRequestTypeDef",
    {
        "Type": SchemaVersionTypeType,
        "SchemaVersionedId": str,
        "Format": NotRequired[SchemaVersionFormatType],
    },
)

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListCredentialLockersRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListDestinationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListEventLogConfigurationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListManagedThingSchemasRequestTypeDef(TypedDict):
    Identifier: str
    EndpointIdFilter: NotRequired[str]
    CapabilityIdFilter: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ManagedThingSchemaListItemTypeDef(TypedDict):
    EndpointId: NotRequired[str]
    CapabilityId: NotRequired[str]
    Schema: NotRequired[Dict[str, Any]]

class ListManagedThingsRequestTypeDef(TypedDict):
    OwnerFilter: NotRequired[str]
    CredentialLockerFilter: NotRequired[str]
    RoleFilter: NotRequired[RoleType]
    ParentControllerIdentifierFilter: NotRequired[str]
    ConnectorPolicyIdFilter: NotRequired[str]
    SerialNumberFilter: NotRequired[str]
    ProvisioningStatusFilter: NotRequired[ProvisioningStatusType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ManagedThingSummaryTypeDef(TypedDict):
    Id: NotRequired[str]
    Arn: NotRequired[str]
    AdvertisedProductId: NotRequired[str]
    Brand: NotRequired[str]
    Classification: NotRequired[str]
    ConnectorDeviceId: NotRequired[str]
    ConnectorPolicyId: NotRequired[str]
    Model: NotRequired[str]
    Name: NotRequired[str]
    Owner: NotRequired[str]
    CredentialLockerId: NotRequired[str]
    ParentControllerId: NotRequired[str]
    ProvisioningStatus: NotRequired[ProvisioningStatusType]
    Role: NotRequired[RoleType]
    SerialNumber: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    UpdatedAt: NotRequired[datetime]
    ActivatedAt: NotRequired[datetime]

class ListNotificationConfigurationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class NotificationConfigurationSummaryTypeDef(TypedDict):
    EventType: NotRequired[EventTypeType]
    DestinationName: NotRequired[str]

class ListOtaTaskConfigurationsRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class OtaTaskConfigurationSummaryTypeDef(TypedDict):
    TaskConfigurationId: NotRequired[str]
    Name: NotRequired[str]
    CreatedAt: NotRequired[datetime]

class ListOtaTaskExecutionsRequestTypeDef(TypedDict):
    Identifier: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListOtaTasksRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class OtaTaskSummaryTypeDef(TypedDict):
    TaskId: NotRequired[str]
    TaskArn: NotRequired[str]
    CreatedAt: NotRequired[datetime]
    LastUpdatedAt: NotRequired[datetime]
    TaskConfigurationId: NotRequired[str]
    Status: NotRequired[OtaStatusType]

class ListProvisioningProfilesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ProvisioningProfileSummaryTypeDef(TypedDict):
    Name: NotRequired[str]
    Id: NotRequired[str]
    Arn: NotRequired[str]
    ProvisioningType: NotRequired[ProvisioningTypeType]

ListSchemaVersionsRequestTypeDef = TypedDict(
    "ListSchemaVersionsRequestTypeDef",
    {
        "Type": SchemaVersionTypeType,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "SchemaId": NotRequired[str],
        "Namespace": NotRequired[str],
        "Visibility": NotRequired[SchemaVersionVisibilityType],
        "SemanticVersion": NotRequired[str],
    },
)
SchemaVersionListItemTypeDef = TypedDict(
    "SchemaVersionListItemTypeDef",
    {
        "SchemaId": NotRequired[str],
        "Type": NotRequired[SchemaVersionTypeType],
        "Description": NotRequired[str],
        "Namespace": NotRequired[str],
        "SemanticVersion": NotRequired[str],
        "Visibility": NotRequired[SchemaVersionVisibilityType],
    },
)

class RetryConfigCriteriaTypeDef(TypedDict):
    FailureType: NotRequired[RetryCriteriaFailureTypeType]
    MinNumberOfRetries: NotRequired[int]

class OtaTaskExecutionSummaryTypeDef(TypedDict):
    ExecutionNumber: NotRequired[int]
    LastUpdatedAt: NotRequired[datetime]
    QueuedAt: NotRequired[datetime]
    RetryAttempt: NotRequired[int]
    StartedAt: NotRequired[datetime]
    Status: NotRequired[OtaTaskExecutionStatusType]

class ScheduleMaintenanceWindowTypeDef(TypedDict):
    DurationInMinutes: NotRequired[int]
    StartTime: NotRequired[str]

class OtaTaskTimeoutConfigTypeDef(TypedDict):
    InProgressTimeoutInMinutes: NotRequired[int]

class PutDefaultEncryptionConfigurationRequestTypeDef(TypedDict):
    encryptionType: EncryptionTypeType
    kmsKeyArn: NotRequired[str]

class PutHubConfigurationRequestTypeDef(TypedDict):
    HubTokenTimerExpirySettingInSeconds: int

class ResetRuntimeLogConfigurationRequestTypeDef(TypedDict):
    ManagedThingId: str

class StartDeviceDiscoveryRequestTypeDef(TypedDict):
    DiscoveryType: DiscoveryTypeType
    ControllerIdentifier: NotRequired[str]
    ConnectorAssociationIdentifier: NotRequired[str]
    AuthenticationMaterial: NotRequired[str]
    AuthenticationMaterialType: NotRequired[Literal["ZWAVE_INSTALL_CODE"]]
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]

StateCapabilityTypeDef = TypedDict(
    "StateCapabilityTypeDef",
    {
        "id": str,
        "name": str,
        "version": str,
        "properties": NotRequired[Dict[str, Any]],
    },
)

class UpdateDestinationRequestTypeDef(TypedDict):
    Name: str
    DeliveryDestinationArn: NotRequired[str]
    DeliveryDestinationType: NotRequired[Literal["KINESIS"]]
    RoleArn: NotRequired[str]
    Description: NotRequired[str]

class UpdateEventLogConfigurationRequestTypeDef(TypedDict):
    Id: str
    EventLogLevel: LogLevelType

class UpdateNotificationConfigurationRequestTypeDef(TypedDict):
    EventType: EventTypeType
    DestinationName: str

class UpdateOtaTaskRequestTypeDef(TypedDict):
    Identifier: str
    Description: NotRequired[str]
    TaskConfigurationId: NotRequired[str]

class OtaTaskAbortConfigOutputTypeDef(TypedDict):
    AbortConfigCriteriaList: NotRequired[List[AbortConfigCriteriaTypeDef]]

class OtaTaskAbortConfigTypeDef(TypedDict):
    AbortConfigCriteriaList: NotRequired[Sequence[AbortConfigCriteriaTypeDef]]

CommandCapabilityTypeDef = TypedDict(
    "CommandCapabilityTypeDef",
    {
        "id": str,
        "name": str,
        "version": str,
        "actions": Sequence[CapabilityActionTypeDef],
    },
)
CapabilityReportEndpointOutputTypeDef = TypedDict(
    "CapabilityReportEndpointOutputTypeDef",
    {
        "id": str,
        "deviceTypes": List[str],
        "capabilities": List[CapabilityReportCapabilityOutputTypeDef],
    },
)
CapabilityReportEndpointTypeDef = TypedDict(
    "CapabilityReportEndpointTypeDef",
    {
        "id": str,
        "deviceTypes": Sequence[str],
        "capabilities": Sequence[CapabilityReportCapabilityTypeDef],
    },
)

class ConfigurationStatusTypeDef(TypedDict):
    state: ConfigurationStateType
    error: NotRequired[ConfigurationErrorTypeDef]

class CreateCredentialLockerResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDestinationResponseTypeDef(TypedDict):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventLogConfigurationResponseTypeDef(TypedDict):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateManagedThingResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNotificationConfigurationResponseTypeDef(TypedDict):
    EventType: EventTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOtaTaskConfigurationResponseTypeDef(TypedDict):
    TaskConfigurationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOtaTaskResponseTypeDef(TypedDict):
    TaskId: str
    TaskArn: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProvisioningProfileResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    ProvisioningType: ProvisioningTypeType
    Id: str
    ClaimCertificate: str
    ClaimCertificatePrivateKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetCredentialLockerResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    Name: str
    CreatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomEndpointResponseTypeDef(TypedDict):
    EndpointAddress: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDestinationResponseTypeDef(TypedDict):
    Description: str
    DeliveryDestinationArn: str
    DeliveryDestinationType: Literal["KINESIS"]
    Name: str
    RoleArn: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeviceDiscoveryResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    DiscoveryType: DiscoveryTypeType
    Status: DeviceDiscoveryStatusType
    StartedAt: datetime
    ControllerId: str
    ConnectorAssociationId: str
    FinishedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventLogConfigurationResponseTypeDef(TypedDict):
    Id: str
    ResourceType: str
    ResourceId: str
    EventLogLevel: LogLevelType
    ResponseMetadata: ResponseMetadataTypeDef

class GetHubConfigurationResponseTypeDef(TypedDict):
    HubTokenTimerExpirySettingInSeconds: int
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetManagedThingConnectivityDataResponseTypeDef(TypedDict):
    ManagedThingId: str
    Connected: bool
    Timestamp: datetime
    DisconnectReason: DisconnectReasonValueType
    ResponseMetadata: ResponseMetadataTypeDef

class GetManagedThingMetaDataResponseTypeDef(TypedDict):
    ManagedThingId: str
    MetaData: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetManagedThingResponseTypeDef(TypedDict):
    Id: str
    Arn: str
    Owner: str
    CredentialLockerId: str
    AdvertisedProductId: str
    Role: RoleType
    ProvisioningStatus: ProvisioningStatusType
    Name: str
    Model: str
    Brand: str
    SerialNumber: str
    UniversalProductCode: str
    InternationalArticleNumber: str
    ConnectorPolicyId: str
    ConnectorDeviceId: str
    DeviceSpecificKey: str
    MacAddress: str
    ParentControllerId: str
    Classification: str
    CreatedAt: datetime
    UpdatedAt: datetime
    ActivatedAt: datetime
    HubNetworkMode: HubNetworkModeType
    MetaData: Dict[str, str]
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetNotificationConfigurationResponseTypeDef(TypedDict):
    EventType: EventTypeType
    DestinationName: str
    CreatedAt: datetime
    UpdatedAt: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetProvisioningProfileResponseTypeDef(TypedDict):
    Arn: str
    Name: str
    ProvisioningType: ProvisioningTypeType
    Id: str
    ClaimCertificate: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

GetSchemaVersionResponseTypeDef = TypedDict(
    "GetSchemaVersionResponseTypeDef",
    {
        "SchemaId": str,
        "Type": SchemaVersionTypeType,
        "Description": str,
        "Namespace": str,
        "SemanticVersion": str,
        "Visibility": SchemaVersionVisibilityType,
        "Schema": Dict[str, Any],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class PutHubConfigurationResponseTypeDef(TypedDict):
    HubTokenTimerExpirySettingInSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCustomEndpointResponseTypeDef(TypedDict):
    EndpointAddress: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendManagedThingCommandResponseTypeDef(TypedDict):
    TraceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDeviceDiscoveryResponseTypeDef(TypedDict):
    Id: str
    StartedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListCredentialLockersResponseTypeDef(TypedDict):
    Items: List[CredentialLockerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListDestinationsResponseTypeDef(TypedDict):
    DestinationList: List[DestinationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListEventLogConfigurationsResponseTypeDef(TypedDict):
    EventLogConfigurationList: List[EventLogConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ExponentialRolloutRateTypeDef(TypedDict):
    BaseRatePerMinute: NotRequired[int]
    IncrementFactor: NotRequired[float]
    RateIncreaseCriteria: NotRequired[RolloutRateIncreaseCriteriaTypeDef]

class GetRuntimeLogConfigurationResponseTypeDef(TypedDict):
    ManagedThingId: str
    RuntimeLogConfigurations: RuntimeLogConfigurationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRuntimeLogConfigurationRequestTypeDef(TypedDict):
    ManagedThingId: str
    RuntimeLogConfigurations: RuntimeLogConfigurationsTypeDef

class ListCredentialLockersRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDestinationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEventLogConfigurationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedThingSchemasRequestPaginateTypeDef(TypedDict):
    Identifier: str
    EndpointIdFilter: NotRequired[str]
    CapabilityIdFilter: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListManagedThingsRequestPaginateTypeDef(TypedDict):
    OwnerFilter: NotRequired[str]
    CredentialLockerFilter: NotRequired[str]
    RoleFilter: NotRequired[RoleType]
    ParentControllerIdentifierFilter: NotRequired[str]
    ConnectorPolicyIdFilter: NotRequired[str]
    SerialNumberFilter: NotRequired[str]
    ProvisioningStatusFilter: NotRequired[ProvisioningStatusType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListNotificationConfigurationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOtaTaskConfigurationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOtaTaskExecutionsRequestPaginateTypeDef(TypedDict):
    Identifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOtaTasksRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProvisioningProfilesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListSchemaVersionsRequestPaginateTypeDef = TypedDict(
    "ListSchemaVersionsRequestPaginateTypeDef",
    {
        "Type": SchemaVersionTypeType,
        "SchemaId": NotRequired[str],
        "Namespace": NotRequired[str],
        "Visibility": NotRequired[SchemaVersionVisibilityType],
        "SemanticVersion": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListManagedThingSchemasResponseTypeDef(TypedDict):
    Items: List[ManagedThingSchemaListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListManagedThingsResponseTypeDef(TypedDict):
    Items: List[ManagedThingSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListNotificationConfigurationsResponseTypeDef(TypedDict):
    NotificationConfigurationList: List[NotificationConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListOtaTaskConfigurationsResponseTypeDef(TypedDict):
    Items: List[OtaTaskConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListOtaTasksResponseTypeDef(TypedDict):
    Tasks: List[OtaTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListProvisioningProfilesResponseTypeDef(TypedDict):
    Items: List[ProvisioningProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSchemaVersionsResponseTypeDef(TypedDict):
    Items: List[SchemaVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class OtaTaskExecutionRetryConfigOutputTypeDef(TypedDict):
    RetryConfigCriteria: NotRequired[List[RetryConfigCriteriaTypeDef]]

class OtaTaskExecutionRetryConfigTypeDef(TypedDict):
    RetryConfigCriteria: NotRequired[Sequence[RetryConfigCriteriaTypeDef]]

class OtaTaskExecutionSummariesTypeDef(TypedDict):
    TaskExecutionSummary: NotRequired[OtaTaskExecutionSummaryTypeDef]
    ManagedThingId: NotRequired[str]

class OtaTaskSchedulingConfigOutputTypeDef(TypedDict):
    EndBehavior: NotRequired[SchedulingConfigEndBehaviorType]
    EndTime: NotRequired[str]
    MaintenanceWindows: NotRequired[List[ScheduleMaintenanceWindowTypeDef]]
    StartTime: NotRequired[str]

class OtaTaskSchedulingConfigTypeDef(TypedDict):
    EndBehavior: NotRequired[SchedulingConfigEndBehaviorType]
    EndTime: NotRequired[str]
    MaintenanceWindows: NotRequired[Sequence[ScheduleMaintenanceWindowTypeDef]]
    StartTime: NotRequired[str]

class StateEndpointTypeDef(TypedDict):
    endpointId: str
    capabilities: List[StateCapabilityTypeDef]

class CommandEndpointTypeDef(TypedDict):
    endpointId: str
    capabilities: Sequence[CommandCapabilityTypeDef]

class CapabilityReportOutputTypeDef(TypedDict):
    version: str
    endpoints: List[CapabilityReportEndpointOutputTypeDef]
    nodeId: NotRequired[str]

class CapabilityReportTypeDef(TypedDict):
    version: str
    endpoints: Sequence[CapabilityReportEndpointTypeDef]
    nodeId: NotRequired[str]

class GetDefaultEncryptionConfigurationResponseTypeDef(TypedDict):
    configurationStatus: ConfigurationStatusTypeDef
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutDefaultEncryptionConfigurationResponseTypeDef(TypedDict):
    configurationStatus: ConfigurationStatusTypeDef
    encryptionType: EncryptionTypeType
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class OtaTaskExecutionRolloutConfigTypeDef(TypedDict):
    ExponentialRolloutRate: NotRequired[ExponentialRolloutRateTypeDef]
    MaximumPerMinute: NotRequired[int]

OtaTaskExecutionRetryConfigUnionTypeDef = Union[
    OtaTaskExecutionRetryConfigTypeDef, OtaTaskExecutionRetryConfigOutputTypeDef
]

class ListOtaTaskExecutionsResponseTypeDef(TypedDict):
    ExecutionSummaries: List[OtaTaskExecutionSummariesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

GetOtaTaskResponseTypeDef = TypedDict(
    "GetOtaTaskResponseTypeDef",
    {
        "TaskId": str,
        "TaskArn": str,
        "Description": str,
        "S3Url": str,
        "Protocol": Literal["HTTP"],
        "OtaType": OtaTypeType,
        "OtaTargetQueryString": str,
        "OtaMechanism": Literal["PUSH"],
        "Target": List[str],
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "TaskConfigurationId": str,
        "TaskProcessingDetails": TaskProcessingDetailsTypeDef,
        "OtaSchedulingConfig": OtaTaskSchedulingConfigOutputTypeDef,
        "OtaTaskExecutionRetryConfig": OtaTaskExecutionRetryConfigOutputTypeDef,
        "Status": OtaStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
OtaTaskSchedulingConfigUnionTypeDef = Union[
    OtaTaskSchedulingConfigTypeDef, OtaTaskSchedulingConfigOutputTypeDef
]

class GetManagedThingStateResponseTypeDef(TypedDict):
    Endpoints: List[StateEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SendManagedThingCommandRequestTypeDef(TypedDict):
    ManagedThingId: str
    Endpoints: Sequence[CommandEndpointTypeDef]
    ConnectorAssociationId: NotRequired[str]

class GetManagedThingCapabilitiesResponseTypeDef(TypedDict):
    ManagedThingId: str
    Capabilities: str
    CapabilityReport: CapabilityReportOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CapabilityReportUnionTypeDef = Union[CapabilityReportTypeDef, CapabilityReportOutputTypeDef]

class PushConfigOutputTypeDef(TypedDict):
    AbortConfig: NotRequired[OtaTaskAbortConfigOutputTypeDef]
    RolloutConfig: NotRequired[OtaTaskExecutionRolloutConfigTypeDef]
    TimeoutConfig: NotRequired[OtaTaskTimeoutConfigTypeDef]

class PushConfigTypeDef(TypedDict):
    AbortConfig: NotRequired[OtaTaskAbortConfigTypeDef]
    RolloutConfig: NotRequired[OtaTaskExecutionRolloutConfigTypeDef]
    TimeoutConfig: NotRequired[OtaTaskTimeoutConfigTypeDef]

CreateOtaTaskRequestTypeDef = TypedDict(
    "CreateOtaTaskRequestTypeDef",
    {
        "S3Url": str,
        "OtaType": OtaTypeType,
        "Description": NotRequired[str],
        "Protocol": NotRequired[Literal["HTTP"]],
        "Target": NotRequired[Sequence[str]],
        "TaskConfigurationId": NotRequired[str],
        "OtaMechanism": NotRequired[Literal["PUSH"]],
        "OtaTargetQueryString": NotRequired[str],
        "ClientToken": NotRequired[str],
        "OtaSchedulingConfig": NotRequired[OtaTaskSchedulingConfigUnionTypeDef],
        "OtaTaskExecutionRetryConfig": NotRequired[OtaTaskExecutionRetryConfigUnionTypeDef],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

class CreateManagedThingRequestTypeDef(TypedDict):
    Role: RoleType
    AuthenticationMaterial: str
    AuthenticationMaterialType: AuthMaterialTypeType
    Owner: NotRequired[str]
    CredentialLockerId: NotRequired[str]
    SerialNumber: NotRequired[str]
    Brand: NotRequired[str]
    Model: NotRequired[str]
    Name: NotRequired[str]
    CapabilityReport: NotRequired[CapabilityReportUnionTypeDef]
    Capabilities: NotRequired[str]
    ClientToken: NotRequired[str]
    Classification: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    MetaData: NotRequired[Mapping[str, str]]

class UpdateManagedThingRequestTypeDef(TypedDict):
    Identifier: str
    Owner: NotRequired[str]
    CredentialLockerId: NotRequired[str]
    SerialNumber: NotRequired[str]
    Brand: NotRequired[str]
    Model: NotRequired[str]
    Name: NotRequired[str]
    CapabilityReport: NotRequired[CapabilityReportUnionTypeDef]
    Capabilities: NotRequired[str]
    Classification: NotRequired[str]
    HubNetworkMode: NotRequired[HubNetworkModeType]
    MetaData: NotRequired[Mapping[str, str]]

class GetOtaTaskConfigurationResponseTypeDef(TypedDict):
    TaskConfigurationId: str
    Name: str
    PushConfig: PushConfigOutputTypeDef
    Description: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

PushConfigUnionTypeDef = Union[PushConfigTypeDef, PushConfigOutputTypeDef]

class CreateOtaTaskConfigurationRequestTypeDef(TypedDict):
    Description: NotRequired[str]
    Name: NotRequired[str]
    PushConfig: NotRequired[PushConfigUnionTypeDef]
    ClientToken: NotRequired[str]
