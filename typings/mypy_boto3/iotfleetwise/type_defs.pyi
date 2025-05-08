"""
Type annotations for iotfleetwise service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_iotfleetwise.type_defs import ActuatorOutputTypeDef

    data: ActuatorOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    CampaignStatusType,
    CompressionType,
    DataFormatType,
    DiagnosticsModeType,
    EncryptionStatusType,
    EncryptionTypeType,
    LogTypeType,
    ManifestStatusType,
    NetworkInterfaceTypeType,
    NodeDataEncodingType,
    NodeDataTypeType,
    RegistrationStatusType,
    ROS2PrimitiveTypeType,
    SignalDecoderTypeType,
    SignalNodeTypeType,
    SignalValueTypeType,
    SpoolingModeType,
    StorageCompressionFormatType,
    StorageMaximumSizeUnitType,
    StorageMinimumTimeToLiveUnitType,
    StructuredMessageListTypeType,
    TimeUnitType,
    TriggerModeType,
    UpdateCampaignActionType,
    UpdateModeType,
    VehicleAssociationBehaviorType,
    VehicleStateType,
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
    "ActuatorOutputTypeDef",
    "ActuatorTypeDef",
    "ActuatorUnionTypeDef",
    "AssociateVehicleFleetRequestTypeDef",
    "AttributeOutputTypeDef",
    "AttributeTypeDef",
    "AttributeUnionTypeDef",
    "BatchCreateVehicleRequestTypeDef",
    "BatchCreateVehicleResponseTypeDef",
    "BatchUpdateVehicleRequestTypeDef",
    "BatchUpdateVehicleResponseTypeDef",
    "BlobTypeDef",
    "BranchTypeDef",
    "CampaignSummaryTypeDef",
    "CanDbcDefinitionTypeDef",
    "CanInterfaceTypeDef",
    "CanSignalTypeDef",
    "CloudWatchLogDeliveryOptionsTypeDef",
    "CollectionSchemeTypeDef",
    "ConditionBasedCollectionSchemeTypeDef",
    "ConditionBasedSignalFetchConfigTypeDef",
    "CreateCampaignRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDecoderManifestRequestTypeDef",
    "CreateDecoderManifestResponseTypeDef",
    "CreateFleetRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateModelManifestRequestTypeDef",
    "CreateModelManifestResponseTypeDef",
    "CreateSignalCatalogRequestTypeDef",
    "CreateSignalCatalogResponseTypeDef",
    "CreateStateTemplateRequestTypeDef",
    "CreateStateTemplateResponseTypeDef",
    "CreateVehicleErrorTypeDef",
    "CreateVehicleRequestItemTypeDef",
    "CreateVehicleRequestTypeDef",
    "CreateVehicleResponseItemTypeDef",
    "CreateVehicleResponseTypeDef",
    "CustomDecodingInterfaceTypeDef",
    "CustomDecodingSignalTypeDef",
    "CustomPropertyTypeDef",
    "CustomStructTypeDef",
    "DataDestinationConfigTypeDef",
    "DataPartitionStorageOptionsTypeDef",
    "DataPartitionTypeDef",
    "DataPartitionUploadOptionsTypeDef",
    "DecoderManifestSummaryTypeDef",
    "DeleteCampaignRequestTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteDecoderManifestRequestTypeDef",
    "DeleteDecoderManifestResponseTypeDef",
    "DeleteFleetRequestTypeDef",
    "DeleteFleetResponseTypeDef",
    "DeleteModelManifestRequestTypeDef",
    "DeleteModelManifestResponseTypeDef",
    "DeleteSignalCatalogRequestTypeDef",
    "DeleteSignalCatalogResponseTypeDef",
    "DeleteStateTemplateRequestTypeDef",
    "DeleteStateTemplateResponseTypeDef",
    "DeleteVehicleRequestTypeDef",
    "DeleteVehicleResponseTypeDef",
    "DisassociateVehicleFleetRequestTypeDef",
    "FleetSummaryTypeDef",
    "FormattedVssTypeDef",
    "GetCampaignRequestTypeDef",
    "GetCampaignResponseTypeDef",
    "GetDecoderManifestRequestTypeDef",
    "GetDecoderManifestResponseTypeDef",
    "GetEncryptionConfigurationResponseTypeDef",
    "GetFleetRequestTypeDef",
    "GetFleetResponseTypeDef",
    "GetLoggingOptionsResponseTypeDef",
    "GetModelManifestRequestTypeDef",
    "GetModelManifestResponseTypeDef",
    "GetRegisterAccountStatusResponseTypeDef",
    "GetSignalCatalogRequestTypeDef",
    "GetSignalCatalogResponseTypeDef",
    "GetStateTemplateRequestTypeDef",
    "GetStateTemplateResponseTypeDef",
    "GetVehicleRequestTypeDef",
    "GetVehicleResponseTypeDef",
    "GetVehicleStatusRequestPaginateTypeDef",
    "GetVehicleStatusRequestTypeDef",
    "GetVehicleStatusResponseTypeDef",
    "IamRegistrationResponseTypeDef",
    "IamResourcesTypeDef",
    "ImportDecoderManifestRequestTypeDef",
    "ImportDecoderManifestResponseTypeDef",
    "ImportSignalCatalogRequestTypeDef",
    "ImportSignalCatalogResponseTypeDef",
    "ListCampaignsRequestPaginateTypeDef",
    "ListCampaignsRequestTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestPaginateTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestTypeDef",
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    "ListDecoderManifestSignalsRequestPaginateTypeDef",
    "ListDecoderManifestSignalsRequestTypeDef",
    "ListDecoderManifestSignalsResponsePaginatorTypeDef",
    "ListDecoderManifestSignalsResponseTypeDef",
    "ListDecoderManifestsRequestPaginateTypeDef",
    "ListDecoderManifestsRequestTypeDef",
    "ListDecoderManifestsResponseTypeDef",
    "ListFleetsForVehicleRequestPaginateTypeDef",
    "ListFleetsForVehicleRequestTypeDef",
    "ListFleetsForVehicleResponseTypeDef",
    "ListFleetsRequestPaginateTypeDef",
    "ListFleetsRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListModelManifestNodesRequestPaginateTypeDef",
    "ListModelManifestNodesRequestTypeDef",
    "ListModelManifestNodesResponseTypeDef",
    "ListModelManifestsRequestPaginateTypeDef",
    "ListModelManifestsRequestTypeDef",
    "ListModelManifestsResponseTypeDef",
    "ListSignalCatalogNodesRequestPaginateTypeDef",
    "ListSignalCatalogNodesRequestTypeDef",
    "ListSignalCatalogNodesResponseTypeDef",
    "ListSignalCatalogsRequestPaginateTypeDef",
    "ListSignalCatalogsRequestTypeDef",
    "ListSignalCatalogsResponseTypeDef",
    "ListStateTemplatesRequestPaginateTypeDef",
    "ListStateTemplatesRequestTypeDef",
    "ListStateTemplatesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVehiclesInFleetRequestPaginateTypeDef",
    "ListVehiclesInFleetRequestTypeDef",
    "ListVehiclesInFleetResponseTypeDef",
    "ListVehiclesRequestPaginateTypeDef",
    "ListVehiclesRequestTypeDef",
    "ListVehiclesResponseTypeDef",
    "MessageSignalOutputTypeDef",
    "MessageSignalPaginatorTypeDef",
    "MessageSignalTypeDef",
    "MessageSignalUnionTypeDef",
    "ModelManifestSummaryTypeDef",
    "MqttTopicConfigTypeDef",
    "NetworkFileDefinitionTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeCountsTypeDef",
    "NodeOutputTypeDef",
    "NodeTypeDef",
    "NodeUnionTypeDef",
    "ObdInterfaceTypeDef",
    "ObdSignalTypeDef",
    "PaginatorConfigTypeDef",
    "PeriodicStateTemplateUpdateStrategyTypeDef",
    "PrimitiveMessageDefinitionTypeDef",
    "PutEncryptionConfigurationRequestTypeDef",
    "PutEncryptionConfigurationResponseTypeDef",
    "PutLoggingOptionsRequestTypeDef",
    "ROS2PrimitiveMessageDefinitionTypeDef",
    "RegisterAccountRequestTypeDef",
    "RegisterAccountResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "SensorOutputTypeDef",
    "SensorTypeDef",
    "SensorUnionTypeDef",
    "SignalCatalogSummaryTypeDef",
    "SignalDecoderOutputTypeDef",
    "SignalDecoderPaginatorTypeDef",
    "SignalDecoderTypeDef",
    "SignalDecoderUnionTypeDef",
    "SignalFetchConfigTypeDef",
    "SignalFetchInformationOutputTypeDef",
    "SignalFetchInformationTypeDef",
    "SignalFetchInformationUnionTypeDef",
    "SignalInformationTypeDef",
    "StateTemplateAssociationOutputTypeDef",
    "StateTemplateAssociationTypeDef",
    "StateTemplateAssociationUnionTypeDef",
    "StateTemplateSummaryTypeDef",
    "StateTemplateUpdateStrategyOutputTypeDef",
    "StateTemplateUpdateStrategyTypeDef",
    "StateTemplateUpdateStrategyUnionTypeDef",
    "StorageMaximumSizeTypeDef",
    "StorageMinimumTimeToLiveTypeDef",
    "StructuredMessageFieldNameAndDataTypePairOutputTypeDef",
    "StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef",
    "StructuredMessageFieldNameAndDataTypePairTypeDef",
    "StructuredMessageFieldNameAndDataTypePairUnionTypeDef",
    "StructuredMessageListDefinitionOutputTypeDef",
    "StructuredMessageListDefinitionPaginatorTypeDef",
    "StructuredMessageListDefinitionTypeDef",
    "StructuredMessageListDefinitionUnionTypeDef",
    "StructuredMessageOutputTypeDef",
    "StructuredMessagePaginatorTypeDef",
    "StructuredMessageTypeDef",
    "StructuredMessageUnionTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "TimeBasedCollectionSchemeTypeDef",
    "TimeBasedSignalFetchConfigTypeDef",
    "TimePeriodTypeDef",
    "TimestampTypeDef",
    "TimestreamConfigTypeDef",
    "TimestreamRegistrationResponseTypeDef",
    "TimestreamResourcesTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCampaignRequestTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateDecoderManifestRequestTypeDef",
    "UpdateDecoderManifestResponseTypeDef",
    "UpdateFleetRequestTypeDef",
    "UpdateFleetResponseTypeDef",
    "UpdateModelManifestRequestTypeDef",
    "UpdateModelManifestResponseTypeDef",
    "UpdateSignalCatalogRequestTypeDef",
    "UpdateSignalCatalogResponseTypeDef",
    "UpdateStateTemplateRequestTypeDef",
    "UpdateStateTemplateResponseTypeDef",
    "UpdateVehicleErrorTypeDef",
    "UpdateVehicleRequestItemTypeDef",
    "UpdateVehicleRequestTypeDef",
    "UpdateVehicleResponseItemTypeDef",
    "UpdateVehicleResponseTypeDef",
    "VehicleMiddlewareTypeDef",
    "VehicleStatusTypeDef",
    "VehicleSummaryTypeDef",
)

ActuatorOutputTypeDef = TypedDict(
    "ActuatorOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[List[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "assignedValue": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)
ActuatorTypeDef = TypedDict(
    "ActuatorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[Sequence[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "assignedValue": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)

class AssociateVehicleFleetRequestTypeDef(TypedDict):
    vehicleName: str
    fleetId: str

AttributeOutputTypeDef = TypedDict(
    "AttributeOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[List[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "assignedValue": NotRequired[str],
        "defaultValue": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
    },
)
AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[Sequence[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "assignedValue": NotRequired[str],
        "defaultValue": NotRequired[str],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
    },
)

class CreateVehicleErrorTypeDef(TypedDict):
    vehicleName: NotRequired[str]
    code: NotRequired[str]
    message: NotRequired[str]

class CreateVehicleResponseItemTypeDef(TypedDict):
    vehicleName: NotRequired[str]
    arn: NotRequired[str]
    thingArn: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class UpdateVehicleErrorTypeDef(TypedDict):
    vehicleName: NotRequired[str]
    code: NotRequired[int]
    message: NotRequired[str]

class UpdateVehicleResponseItemTypeDef(TypedDict):
    vehicleName: NotRequired[str]
    arn: NotRequired[str]

BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]

class BranchTypeDef(TypedDict):
    fullyQualifiedName: str
    description: NotRequired[str]
    deprecationMessage: NotRequired[str]
    comment: NotRequired[str]

class CampaignSummaryTypeDef(TypedDict):
    creationTime: datetime
    lastModificationTime: datetime
    arn: NotRequired[str]
    name: NotRequired[str]
    description: NotRequired[str]
    signalCatalogArn: NotRequired[str]
    targetArn: NotRequired[str]
    status: NotRequired[CampaignStatusType]

class CanInterfaceTypeDef(TypedDict):
    name: str
    protocolName: NotRequired[str]
    protocolVersion: NotRequired[str]

class CanSignalTypeDef(TypedDict):
    messageId: int
    isBigEndian: bool
    isSigned: bool
    startBit: int
    offset: float
    factor: float
    length: int
    name: NotRequired[str]
    signalValueType: NotRequired[SignalValueTypeType]

class CloudWatchLogDeliveryOptionsTypeDef(TypedDict):
    logType: LogTypeType
    logGroupName: NotRequired[str]

class ConditionBasedCollectionSchemeTypeDef(TypedDict):
    expression: str
    minimumTriggerIntervalMs: NotRequired[int]
    triggerMode: NotRequired[TriggerModeType]
    conditionLanguageVersion: NotRequired[int]

class TimeBasedCollectionSchemeTypeDef(TypedDict):
    periodMs: int

class ConditionBasedSignalFetchConfigTypeDef(TypedDict):
    conditionExpression: str
    triggerMode: TriggerModeType

class SignalInformationTypeDef(TypedDict):
    name: str
    maxSampleCount: NotRequired[int]
    minimumSamplingIntervalMs: NotRequired[int]
    dataPartitionId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

TimestampTypeDef = Union[datetime, str]

class CustomDecodingInterfaceTypeDef(TypedDict):
    name: str

CustomDecodingSignalTypeDef = TypedDict(
    "CustomDecodingSignalTypeDef",
    {
        "id": str,
    },
)

class CustomPropertyTypeDef(TypedDict):
    fullyQualifiedName: str
    dataType: NodeDataTypeType
    dataEncoding: NotRequired[NodeDataEncodingType]
    description: NotRequired[str]
    deprecationMessage: NotRequired[str]
    comment: NotRequired[str]
    structFullyQualifiedName: NotRequired[str]

class CustomStructTypeDef(TypedDict):
    fullyQualifiedName: str
    description: NotRequired[str]
    deprecationMessage: NotRequired[str]
    comment: NotRequired[str]

class MqttTopicConfigTypeDef(TypedDict):
    mqttTopicArn: str
    executionRoleArn: str

class S3ConfigTypeDef(TypedDict):
    bucketArn: str
    dataFormat: NotRequired[DataFormatType]
    storageCompressionFormat: NotRequired[StorageCompressionFormatType]
    prefix: NotRequired[str]

class TimestreamConfigTypeDef(TypedDict):
    timestreamTableArn: str
    executionRoleArn: str

class StorageMaximumSizeTypeDef(TypedDict):
    unit: StorageMaximumSizeUnitType
    value: int

class StorageMinimumTimeToLiveTypeDef(TypedDict):
    unit: StorageMinimumTimeToLiveUnitType
    value: int

class DataPartitionUploadOptionsTypeDef(TypedDict):
    expression: str
    conditionLanguageVersion: NotRequired[int]

class DecoderManifestSummaryTypeDef(TypedDict):
    creationTime: datetime
    lastModificationTime: datetime
    name: NotRequired[str]
    arn: NotRequired[str]
    modelManifestArn: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[ManifestStatusType]
    message: NotRequired[str]

class DeleteCampaignRequestTypeDef(TypedDict):
    name: str

class DeleteDecoderManifestRequestTypeDef(TypedDict):
    name: str

class DeleteFleetRequestTypeDef(TypedDict):
    fleetId: str

class DeleteModelManifestRequestTypeDef(TypedDict):
    name: str

class DeleteSignalCatalogRequestTypeDef(TypedDict):
    name: str

class DeleteStateTemplateRequestTypeDef(TypedDict):
    identifier: str

class DeleteVehicleRequestTypeDef(TypedDict):
    vehicleName: str

class DisassociateVehicleFleetRequestTypeDef(TypedDict):
    vehicleName: str
    fleetId: str

FleetSummaryTypeDef = TypedDict(
    "FleetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
        "description": NotRequired[str],
        "lastModificationTime": NotRequired[datetime],
    },
)

class FormattedVssTypeDef(TypedDict):
    vssJson: NotRequired[str]

class GetCampaignRequestTypeDef(TypedDict):
    name: str

class GetDecoderManifestRequestTypeDef(TypedDict):
    name: str

class GetFleetRequestTypeDef(TypedDict):
    fleetId: str

class GetModelManifestRequestTypeDef(TypedDict):
    name: str

class IamRegistrationResponseTypeDef(TypedDict):
    roleArn: str
    registrationStatus: RegistrationStatusType
    errorMessage: NotRequired[str]

class TimestreamRegistrationResponseTypeDef(TypedDict):
    timestreamDatabaseName: str
    timestreamTableName: str
    registrationStatus: RegistrationStatusType
    timestreamDatabaseArn: NotRequired[str]
    timestreamTableArn: NotRequired[str]
    errorMessage: NotRequired[str]

class GetSignalCatalogRequestTypeDef(TypedDict):
    name: str

class NodeCountsTypeDef(TypedDict):
    totalNodes: NotRequired[int]
    totalBranches: NotRequired[int]
    totalSensors: NotRequired[int]
    totalAttributes: NotRequired[int]
    totalActuators: NotRequired[int]
    totalStructs: NotRequired[int]
    totalProperties: NotRequired[int]

class GetStateTemplateRequestTypeDef(TypedDict):
    identifier: str

class GetVehicleRequestTypeDef(TypedDict):
    vehicleName: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetVehicleStatusRequestTypeDef(TypedDict):
    vehicleName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class VehicleStatusTypeDef(TypedDict):
    campaignName: NotRequired[str]
    vehicleName: NotRequired[str]
    status: NotRequired[VehicleStateType]

class IamResourcesTypeDef(TypedDict):
    roleArn: str

class ListCampaignsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    status: NotRequired[str]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]

class ListDecoderManifestNetworkInterfacesRequestTypeDef(TypedDict):
    name: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDecoderManifestSignalsRequestTypeDef(TypedDict):
    name: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListDecoderManifestsRequestTypeDef(TypedDict):
    modelManifestArn: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]

class ListFleetsForVehicleRequestTypeDef(TypedDict):
    vehicleName: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListFleetsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]

class ListModelManifestNodesRequestTypeDef(TypedDict):
    name: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListModelManifestsRequestTypeDef(TypedDict):
    signalCatalogArn: NotRequired[str]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]

class ModelManifestSummaryTypeDef(TypedDict):
    creationTime: datetime
    lastModificationTime: datetime
    name: NotRequired[str]
    arn: NotRequired[str]
    signalCatalogArn: NotRequired[str]
    description: NotRequired[str]
    status: NotRequired[ManifestStatusType]

class ListSignalCatalogNodesRequestTypeDef(TypedDict):
    name: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    signalNodeType: NotRequired[SignalNodeTypeType]

class ListSignalCatalogsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class SignalCatalogSummaryTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    creationTime: NotRequired[datetime]
    lastModificationTime: NotRequired[datetime]

class ListStateTemplatesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]

StateTemplateSummaryTypeDef = TypedDict(
    "StateTemplateSummaryTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "signalCatalogArn": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastModificationTime": NotRequired[datetime],
        "id": NotRequired[str],
    },
)

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceARN: str

class ListVehiclesInFleetRequestTypeDef(TypedDict):
    fleetId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListVehiclesRequestTypeDef(TypedDict):
    modelManifestArn: NotRequired[str]
    attributeNames: NotRequired[Sequence[str]]
    attributeValues: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]

class VehicleSummaryTypeDef(TypedDict):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    creationTime: datetime
    lastModificationTime: datetime
    attributes: NotRequired[Dict[str, str]]

class ObdInterfaceTypeDef(TypedDict):
    name: str
    requestMessageId: int
    obdStandard: NotRequired[str]
    pidRequestIntervalSeconds: NotRequired[int]
    dtcRequestIntervalSeconds: NotRequired[int]
    useExtendedIds: NotRequired[bool]
    hasTransmissionEcu: NotRequired[bool]

class VehicleMiddlewareTypeDef(TypedDict):
    name: str
    protocolName: Literal["ROS_2"]

SensorOutputTypeDef = TypedDict(
    "SensorOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[List[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)

class ObdSignalTypeDef(TypedDict):
    pidResponseLength: int
    serviceMode: int
    pid: int
    scaling: float
    offset: float
    startByte: int
    byteLength: int
    bitRightShift: NotRequired[int]
    bitMaskLength: NotRequired[int]
    isSigned: NotRequired[bool]
    signalValueType: NotRequired[SignalValueTypeType]

class TimePeriodTypeDef(TypedDict):
    unit: TimeUnitType
    value: int

class ROS2PrimitiveMessageDefinitionTypeDef(TypedDict):
    primitiveType: ROS2PrimitiveTypeType
    offset: NotRequired[float]
    scaling: NotRequired[float]
    upperBound: NotRequired[int]

class PutEncryptionConfigurationRequestTypeDef(TypedDict):
    encryptionType: EncryptionTypeType
    kmsKeyId: NotRequired[str]

class TimestreamResourcesTypeDef(TypedDict):
    timestreamDatabaseName: str
    timestreamTableName: str

SensorTypeDef = TypedDict(
    "SensorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
        "description": NotRequired[str],
        "unit": NotRequired[str],
        "allowedValues": NotRequired[Sequence[str]],
        "min": NotRequired[float],
        "max": NotRequired[float],
        "deprecationMessage": NotRequired[str],
        "comment": NotRequired[str],
        "structFullyQualifiedName": NotRequired[str],
    },
)

class TimeBasedSignalFetchConfigTypeDef(TypedDict):
    executionFrequencyMs: int

class StructuredMessageFieldNameAndDataTypePairOutputTypeDef(TypedDict):
    fieldName: str
    dataType: Dict[str, Any]

class StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef(TypedDict):
    fieldName: str
    dataType: Dict[str, Any]

class StructuredMessageFieldNameAndDataTypePairTypeDef(TypedDict):
    fieldName: str
    dataType: Mapping[str, Any]

class StructuredMessageListDefinitionOutputTypeDef(TypedDict):
    name: str
    memberType: Dict[str, Any]
    listType: StructuredMessageListTypeType
    capacity: NotRequired[int]

class StructuredMessageListDefinitionPaginatorTypeDef(TypedDict):
    name: str
    memberType: Dict[str, Any]
    listType: StructuredMessageListTypeType
    capacity: NotRequired[int]

class StructuredMessageListDefinitionTypeDef(TypedDict):
    name: str
    memberType: Mapping[str, Any]
    listType: StructuredMessageListTypeType
    capacity: NotRequired[int]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateCampaignRequestTypeDef(TypedDict):
    name: str
    action: UpdateCampaignActionType
    description: NotRequired[str]
    dataExtraDimensions: NotRequired[Sequence[str]]

class UpdateFleetRequestTypeDef(TypedDict):
    fleetId: str
    description: NotRequired[str]

class UpdateModelManifestRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    nodesToAdd: NotRequired[Sequence[str]]
    nodesToRemove: NotRequired[Sequence[str]]
    status: NotRequired[ManifestStatusType]

class UpdateStateTemplateRequestTypeDef(TypedDict):
    identifier: str
    description: NotRequired[str]
    stateTemplatePropertiesToAdd: NotRequired[Sequence[str]]
    stateTemplatePropertiesToRemove: NotRequired[Sequence[str]]
    dataExtraDimensions: NotRequired[Sequence[str]]
    metadataExtraDimensions: NotRequired[Sequence[str]]

ActuatorUnionTypeDef = Union[ActuatorTypeDef, ActuatorOutputTypeDef]
AttributeUnionTypeDef = Union[AttributeTypeDef, AttributeOutputTypeDef]

class BatchCreateVehicleResponseTypeDef(TypedDict):
    vehicles: List[CreateVehicleResponseItemTypeDef]
    errors: List[CreateVehicleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCampaignResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDecoderManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateModelManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSignalCatalogResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateStateTemplateResponseTypeDef = TypedDict(
    "CreateStateTemplateResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class CreateVehicleResponseTypeDef(TypedDict):
    vehicleName: str
    arn: str
    thingArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCampaignResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDecoderManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

DeleteFleetResponseTypeDef = TypedDict(
    "DeleteFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeleteModelManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSignalCatalogResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

DeleteStateTemplateResponseTypeDef = TypedDict(
    "DeleteStateTemplateResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class DeleteVehicleResponseTypeDef(TypedDict):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDecoderManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    description: str
    modelManifestArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEncryptionConfigurationResponseTypeDef(TypedDict):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    errorMessage: str
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

GetFleetResponseTypeDef = TypedDict(
    "GetFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetModelManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    description: str
    signalCatalogArn: str
    status: ManifestStatusType
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

GetStateTemplateResponseTypeDef = TypedDict(
    "GetStateTemplateResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "stateTemplateProperties": List[str],
        "dataExtraDimensions": List[str],
        "metadataExtraDimensions": List[str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ImportDecoderManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSignalCatalogResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListFleetsForVehicleResponseTypeDef(TypedDict):
    fleets: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListVehiclesInFleetResponseTypeDef(TypedDict):
    vehicles: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutEncryptionConfigurationResponseTypeDef(TypedDict):
    kmsKeyId: str
    encryptionStatus: EncryptionStatusType
    encryptionType: EncryptionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCampaignResponseTypeDef(TypedDict):
    arn: str
    name: str
    status: CampaignStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDecoderManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

UpdateFleetResponseTypeDef = TypedDict(
    "UpdateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateModelManifestResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSignalCatalogResponseTypeDef(TypedDict):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

UpdateStateTemplateResponseTypeDef = TypedDict(
    "UpdateStateTemplateResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class UpdateVehicleResponseTypeDef(TypedDict):
    vehicleName: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateVehicleResponseTypeDef(TypedDict):
    vehicles: List[UpdateVehicleResponseItemTypeDef]
    errors: List[UpdateVehicleErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CanDbcDefinitionTypeDef(TypedDict):
    networkInterface: str
    canDbcFiles: Sequence[BlobTypeDef]
    signalsMap: NotRequired[Mapping[str, str]]

class ListCampaignsResponseTypeDef(TypedDict):
    campaignSummaries: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetLoggingOptionsResponseTypeDef(TypedDict):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutLoggingOptionsRequestTypeDef(TypedDict):
    cloudWatchLogDelivery: CloudWatchLogDeliveryOptionsTypeDef

class CollectionSchemeTypeDef(TypedDict):
    timeBasedCollectionScheme: NotRequired[TimeBasedCollectionSchemeTypeDef]
    conditionBasedCollectionScheme: NotRequired[ConditionBasedCollectionSchemeTypeDef]

class CreateFleetRequestTypeDef(TypedDict):
    fleetId: str
    signalCatalogArn: str
    description: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateModelManifestRequestTypeDef(TypedDict):
    name: str
    nodes: Sequence[str]
    signalCatalogArn: str
    description: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreateStateTemplateRequestTypeDef(TypedDict):
    name: str
    signalCatalogArn: str
    stateTemplateProperties: Sequence[str]
    description: NotRequired[str]
    dataExtraDimensions: NotRequired[Sequence[str]]
    metadataExtraDimensions: NotRequired[Sequence[str]]
    tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class DataDestinationConfigTypeDef(TypedDict):
    s3Config: NotRequired[S3ConfigTypeDef]
    timestreamConfig: NotRequired[TimestreamConfigTypeDef]
    mqttTopicConfig: NotRequired[MqttTopicConfigTypeDef]

class DataPartitionStorageOptionsTypeDef(TypedDict):
    maximumSize: StorageMaximumSizeTypeDef
    storageLocation: str
    minimumTimeToLive: StorageMinimumTimeToLiveTypeDef

class ListDecoderManifestsResponseTypeDef(TypedDict):
    summaries: List[DecoderManifestSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListFleetsResponseTypeDef(TypedDict):
    fleetSummaries: List[FleetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ImportSignalCatalogRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    vss: NotRequired[FormattedVssTypeDef]
    tags: NotRequired[Sequence[TagTypeDef]]

class GetRegisterAccountStatusResponseTypeDef(TypedDict):
    customerAccountId: str
    accountStatus: RegistrationStatusType
    timestreamRegistrationResponse: TimestreamRegistrationResponseTypeDef
    iamRegistrationResponse: IamRegistrationResponseTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSignalCatalogResponseTypeDef(TypedDict):
    name: str
    arn: str
    description: str
    nodeCounts: NodeCountsTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetVehicleStatusRequestPaginateTypeDef(TypedDict):
    vehicleName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCampaignsRequestPaginateTypeDef(TypedDict):
    status: NotRequired[str]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDecoderManifestNetworkInterfacesRequestPaginateTypeDef(TypedDict):
    name: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDecoderManifestSignalsRequestPaginateTypeDef(TypedDict):
    name: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDecoderManifestsRequestPaginateTypeDef(TypedDict):
    modelManifestArn: NotRequired[str]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFleetsForVehicleRequestPaginateTypeDef(TypedDict):
    vehicleName: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFleetsRequestPaginateTypeDef(TypedDict):
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListModelManifestNodesRequestPaginateTypeDef(TypedDict):
    name: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListModelManifestsRequestPaginateTypeDef(TypedDict):
    signalCatalogArn: NotRequired[str]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSignalCatalogNodesRequestPaginateTypeDef(TypedDict):
    name: str
    signalNodeType: NotRequired[SignalNodeTypeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSignalCatalogsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListStateTemplatesRequestPaginateTypeDef(TypedDict):
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVehiclesInFleetRequestPaginateTypeDef(TypedDict):
    fleetId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVehiclesRequestPaginateTypeDef(TypedDict):
    modelManifestArn: NotRequired[str]
    attributeNames: NotRequired[Sequence[str]]
    attributeValues: NotRequired[Sequence[str]]
    listResponseScope: NotRequired[Literal["METADATA_ONLY"]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetVehicleStatusResponseTypeDef(TypedDict):
    campaigns: List[VehicleStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListModelManifestsResponseTypeDef(TypedDict):
    summaries: List[ModelManifestSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSignalCatalogsResponseTypeDef(TypedDict):
    summaries: List[SignalCatalogSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListStateTemplatesResponseTypeDef(TypedDict):
    summaries: List[StateTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListVehiclesResponseTypeDef(TypedDict):
    vehicleSummaries: List[VehicleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "interfaceId": str,
        "type": NetworkInterfaceTypeType,
        "canInterface": NotRequired[CanInterfaceTypeDef],
        "obdInterface": NotRequired[ObdInterfaceTypeDef],
        "vehicleMiddleware": NotRequired[VehicleMiddlewareTypeDef],
        "customDecodingInterface": NotRequired[CustomDecodingInterfaceTypeDef],
    },
)
NodeOutputTypeDef = TypedDict(
    "NodeOutputTypeDef",
    {
        "branch": NotRequired[BranchTypeDef],
        "sensor": NotRequired[SensorOutputTypeDef],
        "actuator": NotRequired[ActuatorOutputTypeDef],
        "attribute": NotRequired[AttributeOutputTypeDef],
        "struct": NotRequired[CustomStructTypeDef],
        "property": NotRequired[CustomPropertyTypeDef],
    },
)

class PeriodicStateTemplateUpdateStrategyTypeDef(TypedDict):
    stateTemplateUpdateRate: TimePeriodTypeDef

class PrimitiveMessageDefinitionTypeDef(TypedDict):
    ros2PrimitiveMessageDefinition: NotRequired[ROS2PrimitiveMessageDefinitionTypeDef]

class RegisterAccountRequestTypeDef(TypedDict):
    timestreamResources: NotRequired[TimestreamResourcesTypeDef]
    iamResources: NotRequired[IamResourcesTypeDef]

class RegisterAccountResponseTypeDef(TypedDict):
    registerAccountStatus: RegistrationStatusType
    timestreamResources: TimestreamResourcesTypeDef
    iamResources: IamResourcesTypeDef
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

SensorUnionTypeDef = Union[SensorTypeDef, SensorOutputTypeDef]

class SignalFetchConfigTypeDef(TypedDict):
    timeBased: NotRequired[TimeBasedSignalFetchConfigTypeDef]
    conditionBased: NotRequired[ConditionBasedSignalFetchConfigTypeDef]

StructuredMessageFieldNameAndDataTypePairUnionTypeDef = Union[
    StructuredMessageFieldNameAndDataTypePairTypeDef,
    StructuredMessageFieldNameAndDataTypePairOutputTypeDef,
]
StructuredMessageListDefinitionUnionTypeDef = Union[
    StructuredMessageListDefinitionTypeDef, StructuredMessageListDefinitionOutputTypeDef
]

class NetworkFileDefinitionTypeDef(TypedDict):
    canDbc: NotRequired[CanDbcDefinitionTypeDef]

DataPartitionTypeDef = TypedDict(
    "DataPartitionTypeDef",
    {
        "id": str,
        "storageOptions": DataPartitionStorageOptionsTypeDef,
        "uploadOptions": NotRequired[DataPartitionUploadOptionsTypeDef],
    },
)

class ListDecoderManifestNetworkInterfacesResponseTypeDef(TypedDict):
    networkInterfaces: List[NetworkInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListModelManifestNodesResponseTypeDef(TypedDict):
    nodes: List[NodeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSignalCatalogNodesResponseTypeDef(TypedDict):
    nodes: List[NodeOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StateTemplateUpdateStrategyOutputTypeDef(TypedDict):
    periodic: NotRequired[PeriodicStateTemplateUpdateStrategyTypeDef]
    onChange: NotRequired[Dict[str, Any]]

class StateTemplateUpdateStrategyTypeDef(TypedDict):
    periodic: NotRequired[PeriodicStateTemplateUpdateStrategyTypeDef]
    onChange: NotRequired[Mapping[str, Any]]

class StructuredMessageOutputTypeDef(TypedDict):
    primitiveMessageDefinition: NotRequired[PrimitiveMessageDefinitionTypeDef]
    structuredMessageListDefinition: NotRequired[StructuredMessageListDefinitionOutputTypeDef]
    structuredMessageDefinition: NotRequired[
        List[StructuredMessageFieldNameAndDataTypePairOutputTypeDef]
    ]

class StructuredMessagePaginatorTypeDef(TypedDict):
    primitiveMessageDefinition: NotRequired[PrimitiveMessageDefinitionTypeDef]
    structuredMessageListDefinition: NotRequired[StructuredMessageListDefinitionPaginatorTypeDef]
    structuredMessageDefinition: NotRequired[
        List[StructuredMessageFieldNameAndDataTypePairPaginatorTypeDef]
    ]

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "branch": NotRequired[BranchTypeDef],
        "sensor": NotRequired[SensorUnionTypeDef],
        "actuator": NotRequired[ActuatorUnionTypeDef],
        "attribute": NotRequired[AttributeUnionTypeDef],
        "struct": NotRequired[CustomStructTypeDef],
        "property": NotRequired[CustomPropertyTypeDef],
    },
)

class SignalFetchInformationOutputTypeDef(TypedDict):
    fullyQualifiedName: str
    signalFetchConfig: SignalFetchConfigTypeDef
    actions: List[str]
    conditionLanguageVersion: NotRequired[int]

class SignalFetchInformationTypeDef(TypedDict):
    fullyQualifiedName: str
    signalFetchConfig: SignalFetchConfigTypeDef
    actions: Sequence[str]
    conditionLanguageVersion: NotRequired[int]

class StructuredMessageTypeDef(TypedDict):
    primitiveMessageDefinition: NotRequired[PrimitiveMessageDefinitionTypeDef]
    structuredMessageListDefinition: NotRequired[StructuredMessageListDefinitionUnionTypeDef]
    structuredMessageDefinition: NotRequired[
        Sequence[StructuredMessageFieldNameAndDataTypePairUnionTypeDef]
    ]

class ImportDecoderManifestRequestTypeDef(TypedDict):
    name: str
    networkFileDefinitions: Sequence[NetworkFileDefinitionTypeDef]

class StateTemplateAssociationOutputTypeDef(TypedDict):
    identifier: str
    stateTemplateUpdateStrategy: StateTemplateUpdateStrategyOutputTypeDef

StateTemplateUpdateStrategyUnionTypeDef = Union[
    StateTemplateUpdateStrategyTypeDef, StateTemplateUpdateStrategyOutputTypeDef
]

class MessageSignalOutputTypeDef(TypedDict):
    topicName: str
    structuredMessage: StructuredMessageOutputTypeDef

class MessageSignalPaginatorTypeDef(TypedDict):
    topicName: str
    structuredMessage: StructuredMessagePaginatorTypeDef

NodeUnionTypeDef = Union[NodeTypeDef, NodeOutputTypeDef]

class GetCampaignResponseTypeDef(TypedDict):
    name: str
    arn: str
    description: str
    signalCatalogArn: str
    targetArn: str
    status: CampaignStatusType
    startTime: datetime
    expiryTime: datetime
    postTriggerCollectionDuration: int
    diagnosticsMode: DiagnosticsModeType
    spoolingMode: SpoolingModeType
    compression: CompressionType
    priority: int
    signalsToCollect: List[SignalInformationTypeDef]
    collectionScheme: CollectionSchemeTypeDef
    dataExtraDimensions: List[str]
    creationTime: datetime
    lastModificationTime: datetime
    dataDestinationConfigs: List[DataDestinationConfigTypeDef]
    dataPartitions: List[DataPartitionTypeDef]
    signalsToFetch: List[SignalFetchInformationOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

SignalFetchInformationUnionTypeDef = Union[
    SignalFetchInformationTypeDef, SignalFetchInformationOutputTypeDef
]
StructuredMessageUnionTypeDef = Union[StructuredMessageTypeDef, StructuredMessageOutputTypeDef]

class GetVehicleResponseTypeDef(TypedDict):
    vehicleName: str
    arn: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: Dict[str, str]
    stateTemplates: List[StateTemplateAssociationOutputTypeDef]
    creationTime: datetime
    lastModificationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StateTemplateAssociationTypeDef(TypedDict):
    identifier: str
    stateTemplateUpdateStrategy: StateTemplateUpdateStrategyUnionTypeDef

SignalDecoderOutputTypeDef = TypedDict(
    "SignalDecoderOutputTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
        "canSignal": NotRequired[CanSignalTypeDef],
        "obdSignal": NotRequired[ObdSignalTypeDef],
        "messageSignal": NotRequired[MessageSignalOutputTypeDef],
        "customDecodingSignal": NotRequired[CustomDecodingSignalTypeDef],
    },
)
SignalDecoderPaginatorTypeDef = TypedDict(
    "SignalDecoderPaginatorTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
        "canSignal": NotRequired[CanSignalTypeDef],
        "obdSignal": NotRequired[ObdSignalTypeDef],
        "messageSignal": NotRequired[MessageSignalPaginatorTypeDef],
        "customDecodingSignal": NotRequired[CustomDecodingSignalTypeDef],
    },
)

class CreateSignalCatalogRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    nodes: NotRequired[Sequence[NodeUnionTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateSignalCatalogRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    nodesToAdd: NotRequired[Sequence[NodeUnionTypeDef]]
    nodesToUpdate: NotRequired[Sequence[NodeUnionTypeDef]]
    nodesToRemove: NotRequired[Sequence[str]]

class CreateCampaignRequestTypeDef(TypedDict):
    name: str
    signalCatalogArn: str
    targetArn: str
    collectionScheme: CollectionSchemeTypeDef
    description: NotRequired[str]
    startTime: NotRequired[TimestampTypeDef]
    expiryTime: NotRequired[TimestampTypeDef]
    postTriggerCollectionDuration: NotRequired[int]
    diagnosticsMode: NotRequired[DiagnosticsModeType]
    spoolingMode: NotRequired[SpoolingModeType]
    compression: NotRequired[CompressionType]
    priority: NotRequired[int]
    signalsToCollect: NotRequired[Sequence[SignalInformationTypeDef]]
    dataExtraDimensions: NotRequired[Sequence[str]]
    tags: NotRequired[Sequence[TagTypeDef]]
    dataDestinationConfigs: NotRequired[Sequence[DataDestinationConfigTypeDef]]
    dataPartitions: NotRequired[Sequence[DataPartitionTypeDef]]
    signalsToFetch: NotRequired[Sequence[SignalFetchInformationUnionTypeDef]]

class MessageSignalTypeDef(TypedDict):
    topicName: str
    structuredMessage: StructuredMessageUnionTypeDef

StateTemplateAssociationUnionTypeDef = Union[
    StateTemplateAssociationTypeDef, StateTemplateAssociationOutputTypeDef
]

class ListDecoderManifestSignalsResponseTypeDef(TypedDict):
    signalDecoders: List[SignalDecoderOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListDecoderManifestSignalsResponsePaginatorTypeDef(TypedDict):
    signalDecoders: List[SignalDecoderPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

MessageSignalUnionTypeDef = Union[MessageSignalTypeDef, MessageSignalOutputTypeDef]

class CreateVehicleRequestItemTypeDef(TypedDict):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: NotRequired[Mapping[str, str]]
    associationBehavior: NotRequired[VehicleAssociationBehaviorType]
    tags: NotRequired[Sequence[TagTypeDef]]
    stateTemplates: NotRequired[Sequence[StateTemplateAssociationUnionTypeDef]]

class CreateVehicleRequestTypeDef(TypedDict):
    vehicleName: str
    modelManifestArn: str
    decoderManifestArn: str
    attributes: NotRequired[Mapping[str, str]]
    associationBehavior: NotRequired[VehicleAssociationBehaviorType]
    tags: NotRequired[Sequence[TagTypeDef]]
    stateTemplates: NotRequired[Sequence[StateTemplateAssociationUnionTypeDef]]

class UpdateVehicleRequestItemTypeDef(TypedDict):
    vehicleName: str
    modelManifestArn: NotRequired[str]
    decoderManifestArn: NotRequired[str]
    attributes: NotRequired[Mapping[str, str]]
    attributeUpdateMode: NotRequired[UpdateModeType]
    stateTemplatesToAdd: NotRequired[Sequence[StateTemplateAssociationUnionTypeDef]]
    stateTemplatesToRemove: NotRequired[Sequence[str]]
    stateTemplatesToUpdate: NotRequired[Sequence[StateTemplateAssociationTypeDef]]

class UpdateVehicleRequestTypeDef(TypedDict):
    vehicleName: str
    modelManifestArn: NotRequired[str]
    decoderManifestArn: NotRequired[str]
    attributes: NotRequired[Mapping[str, str]]
    attributeUpdateMode: NotRequired[UpdateModeType]
    stateTemplatesToAdd: NotRequired[Sequence[StateTemplateAssociationUnionTypeDef]]
    stateTemplatesToRemove: NotRequired[Sequence[str]]
    stateTemplatesToUpdate: NotRequired[Sequence[StateTemplateAssociationUnionTypeDef]]

SignalDecoderTypeDef = TypedDict(
    "SignalDecoderTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
        "canSignal": NotRequired[CanSignalTypeDef],
        "obdSignal": NotRequired[ObdSignalTypeDef],
        "messageSignal": NotRequired[MessageSignalUnionTypeDef],
        "customDecodingSignal": NotRequired[CustomDecodingSignalTypeDef],
    },
)

class BatchCreateVehicleRequestTypeDef(TypedDict):
    vehicles: Sequence[CreateVehicleRequestItemTypeDef]

class BatchUpdateVehicleRequestTypeDef(TypedDict):
    vehicles: Sequence[UpdateVehicleRequestItemTypeDef]

SignalDecoderUnionTypeDef = Union[SignalDecoderTypeDef, SignalDecoderOutputTypeDef]

class CreateDecoderManifestRequestTypeDef(TypedDict):
    name: str
    modelManifestArn: str
    description: NotRequired[str]
    signalDecoders: NotRequired[Sequence[SignalDecoderUnionTypeDef]]
    networkInterfaces: NotRequired[Sequence[NetworkInterfaceTypeDef]]
    defaultForUnmappedSignals: NotRequired[Literal["CUSTOM_DECODING"]]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateDecoderManifestRequestTypeDef(TypedDict):
    name: str
    description: NotRequired[str]
    signalDecodersToAdd: NotRequired[Sequence[SignalDecoderUnionTypeDef]]
    signalDecodersToUpdate: NotRequired[Sequence[SignalDecoderUnionTypeDef]]
    signalDecodersToRemove: NotRequired[Sequence[str]]
    networkInterfacesToAdd: NotRequired[Sequence[NetworkInterfaceTypeDef]]
    networkInterfacesToUpdate: NotRequired[Sequence[NetworkInterfaceTypeDef]]
    networkInterfacesToRemove: NotRequired[Sequence[str]]
    status: NotRequired[ManifestStatusType]
    defaultForUnmappedSignals: NotRequired[Literal["CUSTOM_DECODING"]]
