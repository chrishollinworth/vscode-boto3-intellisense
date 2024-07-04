"""
Type annotations for iotfleetwise service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotfleetwise.type_defs import ActuatorTypeDef

    data: ActuatorTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

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
    SpoolingModeType,
    StorageCompressionFormatType,
    StructuredMessageListTypeType,
    TriggerModeType,
    UpdateCampaignActionType,
    UpdateModeType,
    VehicleAssociationBehaviorType,
    VehicleStateType,
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
    "ActuatorTypeDef",
    "AssociateVehicleFleetRequestRequestTypeDef",
    "AttributeTypeDef",
    "BatchCreateVehicleRequestRequestTypeDef",
    "BatchCreateVehicleResponseTypeDef",
    "BatchUpdateVehicleRequestRequestTypeDef",
    "BatchUpdateVehicleResponseTypeDef",
    "BranchTypeDef",
    "CampaignSummaryTypeDef",
    "CanDbcDefinitionTypeDef",
    "CanInterfaceTypeDef",
    "CanSignalTypeDef",
    "CloudWatchLogDeliveryOptionsTypeDef",
    "CollectionSchemeTypeDef",
    "ConditionBasedCollectionSchemeTypeDef",
    "CreateCampaignRequestRequestTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDecoderManifestRequestRequestTypeDef",
    "CreateDecoderManifestResponseTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateModelManifestRequestRequestTypeDef",
    "CreateModelManifestResponseTypeDef",
    "CreateSignalCatalogRequestRequestTypeDef",
    "CreateSignalCatalogResponseTypeDef",
    "CreateVehicleErrorTypeDef",
    "CreateVehicleRequestItemTypeDef",
    "CreateVehicleRequestRequestTypeDef",
    "CreateVehicleResponseItemTypeDef",
    "CreateVehicleResponseTypeDef",
    "CustomPropertyTypeDef",
    "CustomStructTypeDef",
    "DataDestinationConfigTypeDef",
    "DecoderManifestSummaryTypeDef",
    "DeleteCampaignRequestRequestTypeDef",
    "DeleteCampaignResponseTypeDef",
    "DeleteDecoderManifestRequestRequestTypeDef",
    "DeleteDecoderManifestResponseTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DeleteFleetResponseTypeDef",
    "DeleteModelManifestRequestRequestTypeDef",
    "DeleteModelManifestResponseTypeDef",
    "DeleteSignalCatalogRequestRequestTypeDef",
    "DeleteSignalCatalogResponseTypeDef",
    "DeleteVehicleRequestRequestTypeDef",
    "DeleteVehicleResponseTypeDef",
    "DisassociateVehicleFleetRequestRequestTypeDef",
    "FleetSummaryTypeDef",
    "FormattedVssTypeDef",
    "GetCampaignRequestRequestTypeDef",
    "GetCampaignResponseTypeDef",
    "GetDecoderManifestRequestRequestTypeDef",
    "GetDecoderManifestResponseTypeDef",
    "GetEncryptionConfigurationResponseTypeDef",
    "GetFleetRequestRequestTypeDef",
    "GetFleetResponseTypeDef",
    "GetLoggingOptionsResponseTypeDef",
    "GetModelManifestRequestRequestTypeDef",
    "GetModelManifestResponseTypeDef",
    "GetRegisterAccountStatusResponseTypeDef",
    "GetSignalCatalogRequestRequestTypeDef",
    "GetSignalCatalogResponseTypeDef",
    "GetVehicleRequestRequestTypeDef",
    "GetVehicleResponseTypeDef",
    "GetVehicleStatusRequestRequestTypeDef",
    "GetVehicleStatusResponseTypeDef",
    "IamRegistrationResponseTypeDef",
    "IamResourcesTypeDef",
    "ImportDecoderManifestRequestRequestTypeDef",
    "ImportDecoderManifestResponseTypeDef",
    "ImportSignalCatalogRequestRequestTypeDef",
    "ImportSignalCatalogResponseTypeDef",
    "ListCampaignsRequestRequestTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    "ListDecoderManifestSignalsRequestRequestTypeDef",
    "ListDecoderManifestSignalsResponseTypeDef",
    "ListDecoderManifestsRequestRequestTypeDef",
    "ListDecoderManifestsResponseTypeDef",
    "ListFleetsForVehicleRequestRequestTypeDef",
    "ListFleetsForVehicleResponseTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListModelManifestNodesRequestRequestTypeDef",
    "ListModelManifestNodesResponseTypeDef",
    "ListModelManifestsRequestRequestTypeDef",
    "ListModelManifestsResponseTypeDef",
    "ListSignalCatalogNodesRequestRequestTypeDef",
    "ListSignalCatalogNodesResponseTypeDef",
    "ListSignalCatalogsRequestRequestTypeDef",
    "ListSignalCatalogsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVehiclesInFleetRequestRequestTypeDef",
    "ListVehiclesInFleetResponseTypeDef",
    "ListVehiclesRequestRequestTypeDef",
    "ListVehiclesResponseTypeDef",
    "MessageSignalTypeDef",
    "ModelManifestSummaryTypeDef",
    "NetworkFileDefinitionTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeCountsTypeDef",
    "NodeTypeDef",
    "ObdInterfaceTypeDef",
    "ObdSignalTypeDef",
    "PaginatorConfigTypeDef",
    "PrimitiveMessageDefinitionTypeDef",
    "PutEncryptionConfigurationRequestRequestTypeDef",
    "PutEncryptionConfigurationResponseTypeDef",
    "PutLoggingOptionsRequestRequestTypeDef",
    "ROS2PrimitiveMessageDefinitionTypeDef",
    "RegisterAccountRequestRequestTypeDef",
    "RegisterAccountResponseTypeDef",
    "ResponseMetadataTypeDef",
    "S3ConfigTypeDef",
    "SensorTypeDef",
    "SignalCatalogSummaryTypeDef",
    "SignalDecoderTypeDef",
    "SignalInformationTypeDef",
    "StructuredMessageFieldNameAndDataTypePairTypeDef",
    "StructuredMessageListDefinitionTypeDef",
    "StructuredMessageTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimeBasedCollectionSchemeTypeDef",
    "TimestreamConfigTypeDef",
    "TimestreamRegistrationResponseTypeDef",
    "TimestreamResourcesTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCampaignRequestRequestTypeDef",
    "UpdateCampaignResponseTypeDef",
    "UpdateDecoderManifestRequestRequestTypeDef",
    "UpdateDecoderManifestResponseTypeDef",
    "UpdateFleetRequestRequestTypeDef",
    "UpdateFleetResponseTypeDef",
    "UpdateModelManifestRequestRequestTypeDef",
    "UpdateModelManifestResponseTypeDef",
    "UpdateSignalCatalogRequestRequestTypeDef",
    "UpdateSignalCatalogResponseTypeDef",
    "UpdateVehicleErrorTypeDef",
    "UpdateVehicleRequestItemTypeDef",
    "UpdateVehicleRequestRequestTypeDef",
    "UpdateVehicleResponseItemTypeDef",
    "UpdateVehicleResponseTypeDef",
    "VehicleMiddlewareTypeDef",
    "VehicleStatusTypeDef",
    "VehicleSummaryTypeDef",
)

_RequiredActuatorTypeDef = TypedDict(
    "_RequiredActuatorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalActuatorTypeDef = TypedDict(
    "_OptionalActuatorTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": List[str],
        "min": float,
        "max": float,
        "assignedValue": str,
        "deprecationMessage": str,
        "comment": str,
        "structFullyQualifiedName": str,
    },
    total=False,
)

class ActuatorTypeDef(_RequiredActuatorTypeDef, _OptionalActuatorTypeDef):
    pass

AssociateVehicleFleetRequestRequestTypeDef = TypedDict(
    "AssociateVehicleFleetRequestRequestTypeDef",
    {
        "vehicleName": str,
        "fleetId": str,
    },
)

_RequiredAttributeTypeDef = TypedDict(
    "_RequiredAttributeTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": List[str],
        "min": float,
        "max": float,
        "assignedValue": str,
        "defaultValue": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass

BatchCreateVehicleRequestRequestTypeDef = TypedDict(
    "BatchCreateVehicleRequestRequestTypeDef",
    {
        "vehicles": List["CreateVehicleRequestItemTypeDef"],
    },
)

BatchCreateVehicleResponseTypeDef = TypedDict(
    "BatchCreateVehicleResponseTypeDef",
    {
        "vehicles": List["CreateVehicleResponseItemTypeDef"],
        "errors": List["CreateVehicleErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateVehicleRequestRequestTypeDef = TypedDict(
    "BatchUpdateVehicleRequestRequestTypeDef",
    {
        "vehicles": List["UpdateVehicleRequestItemTypeDef"],
    },
)

BatchUpdateVehicleResponseTypeDef = TypedDict(
    "BatchUpdateVehicleResponseTypeDef",
    {
        "vehicles": List["UpdateVehicleResponseItemTypeDef"],
        "errors": List["UpdateVehicleErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBranchTypeDef = TypedDict(
    "_RequiredBranchTypeDef",
    {
        "fullyQualifiedName": str,
    },
)
_OptionalBranchTypeDef = TypedDict(
    "_OptionalBranchTypeDef",
    {
        "description": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class BranchTypeDef(_RequiredBranchTypeDef, _OptionalBranchTypeDef):
    pass

_RequiredCampaignSummaryTypeDef = TypedDict(
    "_RequiredCampaignSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalCampaignSummaryTypeDef = TypedDict(
    "_OptionalCampaignSummaryTypeDef",
    {
        "arn": str,
        "name": str,
        "description": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "status": CampaignStatusType,
    },
    total=False,
)

class CampaignSummaryTypeDef(_RequiredCampaignSummaryTypeDef, _OptionalCampaignSummaryTypeDef):
    pass

_RequiredCanDbcDefinitionTypeDef = TypedDict(
    "_RequiredCanDbcDefinitionTypeDef",
    {
        "networkInterface": str,
        "canDbcFiles": List[Union[bytes, IO[bytes], StreamingBody]],
    },
)
_OptionalCanDbcDefinitionTypeDef = TypedDict(
    "_OptionalCanDbcDefinitionTypeDef",
    {
        "signalsMap": Dict[str, str],
    },
    total=False,
)

class CanDbcDefinitionTypeDef(_RequiredCanDbcDefinitionTypeDef, _OptionalCanDbcDefinitionTypeDef):
    pass

_RequiredCanInterfaceTypeDef = TypedDict(
    "_RequiredCanInterfaceTypeDef",
    {
        "name": str,
    },
)
_OptionalCanInterfaceTypeDef = TypedDict(
    "_OptionalCanInterfaceTypeDef",
    {
        "protocolName": str,
        "protocolVersion": str,
    },
    total=False,
)

class CanInterfaceTypeDef(_RequiredCanInterfaceTypeDef, _OptionalCanInterfaceTypeDef):
    pass

_RequiredCanSignalTypeDef = TypedDict(
    "_RequiredCanSignalTypeDef",
    {
        "messageId": int,
        "isBigEndian": bool,
        "isSigned": bool,
        "startBit": int,
        "offset": float,
        "factor": float,
        "length": int,
    },
)
_OptionalCanSignalTypeDef = TypedDict(
    "_OptionalCanSignalTypeDef",
    {
        "name": str,
    },
    total=False,
)

class CanSignalTypeDef(_RequiredCanSignalTypeDef, _OptionalCanSignalTypeDef):
    pass

_RequiredCloudWatchLogDeliveryOptionsTypeDef = TypedDict(
    "_RequiredCloudWatchLogDeliveryOptionsTypeDef",
    {
        "logType": LogTypeType,
    },
)
_OptionalCloudWatchLogDeliveryOptionsTypeDef = TypedDict(
    "_OptionalCloudWatchLogDeliveryOptionsTypeDef",
    {
        "logGroupName": str,
    },
    total=False,
)

class CloudWatchLogDeliveryOptionsTypeDef(
    _RequiredCloudWatchLogDeliveryOptionsTypeDef, _OptionalCloudWatchLogDeliveryOptionsTypeDef
):
    pass

CollectionSchemeTypeDef = TypedDict(
    "CollectionSchemeTypeDef",
    {
        "timeBasedCollectionScheme": "TimeBasedCollectionSchemeTypeDef",
        "conditionBasedCollectionScheme": "ConditionBasedCollectionSchemeTypeDef",
    },
    total=False,
)

_RequiredConditionBasedCollectionSchemeTypeDef = TypedDict(
    "_RequiredConditionBasedCollectionSchemeTypeDef",
    {
        "expression": str,
    },
)
_OptionalConditionBasedCollectionSchemeTypeDef = TypedDict(
    "_OptionalConditionBasedCollectionSchemeTypeDef",
    {
        "minimumTriggerIntervalMs": int,
        "triggerMode": TriggerModeType,
        "conditionLanguageVersion": int,
    },
    total=False,
)

class ConditionBasedCollectionSchemeTypeDef(
    _RequiredConditionBasedCollectionSchemeTypeDef, _OptionalConditionBasedCollectionSchemeTypeDef
):
    pass

_RequiredCreateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "collectionScheme": "CollectionSchemeTypeDef",
    },
)
_OptionalCreateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCampaignRequestRequestTypeDef",
    {
        "description": str,
        "startTime": Union[datetime, str],
        "expiryTime": Union[datetime, str],
        "postTriggerCollectionDuration": int,
        "diagnosticsMode": DiagnosticsModeType,
        "spoolingMode": SpoolingModeType,
        "compression": CompressionType,
        "priority": int,
        "signalsToCollect": List["SignalInformationTypeDef"],
        "dataExtraDimensions": List[str],
        "tags": List["TagTypeDef"],
        "dataDestinationConfigs": List["DataDestinationConfigTypeDef"],
    },
    total=False,
)

class CreateCampaignRequestRequestTypeDef(
    _RequiredCreateCampaignRequestRequestTypeDef, _OptionalCreateCampaignRequestRequestTypeDef
):
    pass

CreateCampaignResponseTypeDef = TypedDict(
    "CreateCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "modelManifestArn": str,
    },
)
_OptionalCreateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDecoderManifestRequestRequestTypeDef",
    {
        "description": str,
        "signalDecoders": List["SignalDecoderTypeDef"],
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDecoderManifestRequestRequestTypeDef(
    _RequiredCreateDecoderManifestRequestRequestTypeDef,
    _OptionalCreateDecoderManifestRequestRequestTypeDef,
):
    pass

CreateDecoderManifestResponseTypeDef = TypedDict(
    "CreateDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestRequestTypeDef",
    {
        "fleetId": str,
        "signalCatalogArn": str,
    },
)
_OptionalCreateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateFleetRequestRequestTypeDef(
    _RequiredCreateFleetRequestRequestTypeDef, _OptionalCreateFleetRequestRequestTypeDef
):
    pass

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateModelManifestRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelManifestRequestRequestTypeDef",
    {
        "name": str,
        "nodes": List[str],
        "signalCatalogArn": str,
    },
)
_OptionalCreateModelManifestRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelManifestRequestRequestTypeDef",
    {
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateModelManifestRequestRequestTypeDef(
    _RequiredCreateModelManifestRequestRequestTypeDef,
    _OptionalCreateModelManifestRequestRequestTypeDef,
):
    pass

CreateModelManifestResponseTypeDef = TypedDict(
    "CreateModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "nodes": List["NodeTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSignalCatalogRequestRequestTypeDef(
    _RequiredCreateSignalCatalogRequestRequestTypeDef,
    _OptionalCreateSignalCatalogRequestRequestTypeDef,
):
    pass

CreateSignalCatalogResponseTypeDef = TypedDict(
    "CreateSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVehicleErrorTypeDef = TypedDict(
    "CreateVehicleErrorTypeDef",
    {
        "vehicleName": str,
        "code": str,
        "message": str,
    },
    total=False,
)

_RequiredCreateVehicleRequestItemTypeDef = TypedDict(
    "_RequiredCreateVehicleRequestItemTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
    },
)
_OptionalCreateVehicleRequestItemTypeDef = TypedDict(
    "_OptionalCreateVehicleRequestItemTypeDef",
    {
        "attributes": Dict[str, str],
        "associationBehavior": VehicleAssociationBehaviorType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateVehicleRequestItemTypeDef(
    _RequiredCreateVehicleRequestItemTypeDef, _OptionalCreateVehicleRequestItemTypeDef
):
    pass

_RequiredCreateVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
    },
)
_OptionalCreateVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVehicleRequestRequestTypeDef",
    {
        "attributes": Dict[str, str],
        "associationBehavior": VehicleAssociationBehaviorType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateVehicleRequestRequestTypeDef(
    _RequiredCreateVehicleRequestRequestTypeDef, _OptionalCreateVehicleRequestRequestTypeDef
):
    pass

CreateVehicleResponseItemTypeDef = TypedDict(
    "CreateVehicleResponseItemTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "thingArn": str,
    },
    total=False,
)

CreateVehicleResponseTypeDef = TypedDict(
    "CreateVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "thingArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCustomPropertyTypeDef = TypedDict(
    "_RequiredCustomPropertyTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalCustomPropertyTypeDef = TypedDict(
    "_OptionalCustomPropertyTypeDef",
    {
        "dataEncoding": NodeDataEncodingType,
        "description": str,
        "deprecationMessage": str,
        "comment": str,
        "structFullyQualifiedName": str,
    },
    total=False,
)

class CustomPropertyTypeDef(_RequiredCustomPropertyTypeDef, _OptionalCustomPropertyTypeDef):
    pass

_RequiredCustomStructTypeDef = TypedDict(
    "_RequiredCustomStructTypeDef",
    {
        "fullyQualifiedName": str,
    },
)
_OptionalCustomStructTypeDef = TypedDict(
    "_OptionalCustomStructTypeDef",
    {
        "description": str,
        "deprecationMessage": str,
        "comment": str,
    },
    total=False,
)

class CustomStructTypeDef(_RequiredCustomStructTypeDef, _OptionalCustomStructTypeDef):
    pass

DataDestinationConfigTypeDef = TypedDict(
    "DataDestinationConfigTypeDef",
    {
        "s3Config": "S3ConfigTypeDef",
        "timestreamConfig": "TimestreamConfigTypeDef",
    },
    total=False,
)

_RequiredDecoderManifestSummaryTypeDef = TypedDict(
    "_RequiredDecoderManifestSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalDecoderManifestSummaryTypeDef = TypedDict(
    "_OptionalDecoderManifestSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "modelManifestArn": str,
        "description": str,
        "status": ManifestStatusType,
        "message": str,
    },
    total=False,
)

class DecoderManifestSummaryTypeDef(
    _RequiredDecoderManifestSummaryTypeDef, _OptionalDecoderManifestSummaryTypeDef
):
    pass

DeleteCampaignRequestRequestTypeDef = TypedDict(
    "DeleteCampaignRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteCampaignResponseTypeDef = TypedDict(
    "DeleteCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDecoderManifestRequestRequestTypeDef = TypedDict(
    "DeleteDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteDecoderManifestResponseTypeDef = TypedDict(
    "DeleteDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)

DeleteFleetResponseTypeDef = TypedDict(
    "DeleteFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteModelManifestRequestRequestTypeDef = TypedDict(
    "DeleteModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteModelManifestResponseTypeDef = TypedDict(
    "DeleteModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSignalCatalogRequestRequestTypeDef = TypedDict(
    "DeleteSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteSignalCatalogResponseTypeDef = TypedDict(
    "DeleteSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVehicleRequestRequestTypeDef = TypedDict(
    "DeleteVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)

DeleteVehicleResponseTypeDef = TypedDict(
    "DeleteVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateVehicleFleetRequestRequestTypeDef = TypedDict(
    "DisassociateVehicleFleetRequestRequestTypeDef",
    {
        "vehicleName": str,
        "fleetId": str,
    },
)

_RequiredFleetSummaryTypeDef = TypedDict(
    "_RequiredFleetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
    },
)
_OptionalFleetSummaryTypeDef = TypedDict(
    "_OptionalFleetSummaryTypeDef",
    {
        "description": str,
        "lastModificationTime": datetime,
    },
    total=False,
)

class FleetSummaryTypeDef(_RequiredFleetSummaryTypeDef, _OptionalFleetSummaryTypeDef):
    pass

FormattedVssTypeDef = TypedDict(
    "FormattedVssTypeDef",
    {
        "vssJson": str,
    },
    total=False,
)

GetCampaignRequestRequestTypeDef = TypedDict(
    "GetCampaignRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetCampaignResponseTypeDef = TypedDict(
    "GetCampaignResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "targetArn": str,
        "status": CampaignStatusType,
        "startTime": datetime,
        "expiryTime": datetime,
        "postTriggerCollectionDuration": int,
        "diagnosticsMode": DiagnosticsModeType,
        "spoolingMode": SpoolingModeType,
        "compression": CompressionType,
        "priority": int,
        "signalsToCollect": List["SignalInformationTypeDef"],
        "collectionScheme": "CollectionSchemeTypeDef",
        "dataExtraDimensions": List[str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "dataDestinationConfigs": List["DataDestinationConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDecoderManifestRequestRequestTypeDef = TypedDict(
    "GetDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetDecoderManifestResponseTypeDef = TypedDict(
    "GetDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "modelManifestArn": str,
        "status": ManifestStatusType,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEncryptionConfigurationResponseTypeDef = TypedDict(
    "GetEncryptionConfigurationResponseTypeDef",
    {
        "kmsKeyId": str,
        "encryptionStatus": EncryptionStatusType,
        "encryptionType": EncryptionTypeType,
        "errorMessage": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFleetRequestRequestTypeDef = TypedDict(
    "GetFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)

GetFleetResponseTypeDef = TypedDict(
    "GetFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoggingOptionsResponseTypeDef = TypedDict(
    "GetLoggingOptionsResponseTypeDef",
    {
        "cloudWatchLogDelivery": "CloudWatchLogDeliveryOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetModelManifestRequestRequestTypeDef = TypedDict(
    "GetModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetModelManifestResponseTypeDef = TypedDict(
    "GetModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "signalCatalogArn": str,
        "status": ManifestStatusType,
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegisterAccountStatusResponseTypeDef = TypedDict(
    "GetRegisterAccountStatusResponseTypeDef",
    {
        "customerAccountId": str,
        "accountStatus": RegistrationStatusType,
        "timestreamRegistrationResponse": "TimestreamRegistrationResponseTypeDef",
        "iamRegistrationResponse": "IamRegistrationResponseTypeDef",
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSignalCatalogRequestRequestTypeDef = TypedDict(
    "GetSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetSignalCatalogResponseTypeDef = TypedDict(
    "GetSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "nodeCounts": "NodeCountsTypeDef",
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVehicleRequestRequestTypeDef = TypedDict(
    "GetVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)

GetVehicleResponseTypeDef = TypedDict(
    "GetVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Dict[str, str],
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetVehicleStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetVehicleStatusRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalGetVehicleStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetVehicleStatusRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class GetVehicleStatusRequestRequestTypeDef(
    _RequiredGetVehicleStatusRequestRequestTypeDef, _OptionalGetVehicleStatusRequestRequestTypeDef
):
    pass

GetVehicleStatusResponseTypeDef = TypedDict(
    "GetVehicleStatusResponseTypeDef",
    {
        "campaigns": List["VehicleStatusTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredIamRegistrationResponseTypeDef = TypedDict(
    "_RequiredIamRegistrationResponseTypeDef",
    {
        "roleArn": str,
        "registrationStatus": RegistrationStatusType,
    },
)
_OptionalIamRegistrationResponseTypeDef = TypedDict(
    "_OptionalIamRegistrationResponseTypeDef",
    {
        "errorMessage": str,
    },
    total=False,
)

class IamRegistrationResponseTypeDef(
    _RequiredIamRegistrationResponseTypeDef, _OptionalIamRegistrationResponseTypeDef
):
    pass

IamResourcesTypeDef = TypedDict(
    "IamResourcesTypeDef",
    {
        "roleArn": str,
    },
)

ImportDecoderManifestRequestRequestTypeDef = TypedDict(
    "ImportDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
        "networkFileDefinitions": List["NetworkFileDefinitionTypeDef"],
    },
)

ImportDecoderManifestResponseTypeDef = TypedDict(
    "ImportDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredImportSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredImportSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalImportSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalImportSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "vss": "FormattedVssTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class ImportSignalCatalogRequestRequestTypeDef(
    _RequiredImportSignalCatalogRequestRequestTypeDef,
    _OptionalImportSignalCatalogRequestRequestTypeDef,
):
    pass

ImportSignalCatalogResponseTypeDef = TypedDict(
    "ImportSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCampaignsRequestRequestTypeDef = TypedDict(
    "ListCampaignsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "status": str,
    },
    total=False,
)

ListCampaignsResponseTypeDef = TypedDict(
    "ListCampaignsResponseTypeDef",
    {
        "campaignSummaries": List["CampaignSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "_RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "_OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDecoderManifestNetworkInterfacesRequestRequestTypeDef(
    _RequiredListDecoderManifestNetworkInterfacesRequestRequestTypeDef,
    _OptionalListDecoderManifestNetworkInterfacesRequestRequestTypeDef,
):
    pass

ListDecoderManifestNetworkInterfacesResponseTypeDef = TypedDict(
    "ListDecoderManifestNetworkInterfacesResponseTypeDef",
    {
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListDecoderManifestSignalsRequestRequestTypeDef = TypedDict(
    "_RequiredListDecoderManifestSignalsRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListDecoderManifestSignalsRequestRequestTypeDef = TypedDict(
    "_OptionalListDecoderManifestSignalsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListDecoderManifestSignalsRequestRequestTypeDef(
    _RequiredListDecoderManifestSignalsRequestRequestTypeDef,
    _OptionalListDecoderManifestSignalsRequestRequestTypeDef,
):
    pass

ListDecoderManifestSignalsResponseTypeDef = TypedDict(
    "ListDecoderManifestSignalsResponseTypeDef",
    {
        "signalDecoders": List["SignalDecoderTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDecoderManifestsRequestRequestTypeDef = TypedDict(
    "ListDecoderManifestsRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListDecoderManifestsResponseTypeDef = TypedDict(
    "ListDecoderManifestsResponseTypeDef",
    {
        "summaries": List["DecoderManifestSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListFleetsForVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredListFleetsForVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalListFleetsForVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalListFleetsForVehicleRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListFleetsForVehicleRequestRequestTypeDef(
    _RequiredListFleetsForVehicleRequestRequestTypeDef,
    _OptionalListFleetsForVehicleRequestRequestTypeDef,
):
    pass

ListFleetsForVehicleResponseTypeDef = TypedDict(
    "ListFleetsForVehicleResponseTypeDef",
    {
        "fleets": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "fleetSummaries": List["FleetSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListModelManifestNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListModelManifestNodesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListModelManifestNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListModelManifestNodesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListModelManifestNodesRequestRequestTypeDef(
    _RequiredListModelManifestNodesRequestRequestTypeDef,
    _OptionalListModelManifestNodesRequestRequestTypeDef,
):
    pass

ListModelManifestNodesResponseTypeDef = TypedDict(
    "ListModelManifestNodesResponseTypeDef",
    {
        "nodes": List["NodeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelManifestsRequestRequestTypeDef = TypedDict(
    "ListModelManifestsRequestRequestTypeDef",
    {
        "signalCatalogArn": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListModelManifestsResponseTypeDef = TypedDict(
    "ListModelManifestsResponseTypeDef",
    {
        "summaries": List["ModelManifestSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListSignalCatalogNodesRequestRequestTypeDef = TypedDict(
    "_RequiredListSignalCatalogNodesRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalListSignalCatalogNodesRequestRequestTypeDef = TypedDict(
    "_OptionalListSignalCatalogNodesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "signalNodeType": SignalNodeTypeType,
    },
    total=False,
)

class ListSignalCatalogNodesRequestRequestTypeDef(
    _RequiredListSignalCatalogNodesRequestRequestTypeDef,
    _OptionalListSignalCatalogNodesRequestRequestTypeDef,
):
    pass

ListSignalCatalogNodesResponseTypeDef = TypedDict(
    "ListSignalCatalogNodesResponseTypeDef",
    {
        "nodes": List["NodeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSignalCatalogsRequestRequestTypeDef = TypedDict(
    "ListSignalCatalogsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListSignalCatalogsResponseTypeDef = TypedDict(
    "ListSignalCatalogsResponseTypeDef",
    {
        "summaries": List["SignalCatalogSummaryTypeDef"],
        "nextToken": str,
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

_RequiredListVehiclesInFleetRequestRequestTypeDef = TypedDict(
    "_RequiredListVehiclesInFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)
_OptionalListVehiclesInFleetRequestRequestTypeDef = TypedDict(
    "_OptionalListVehiclesInFleetRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListVehiclesInFleetRequestRequestTypeDef(
    _RequiredListVehiclesInFleetRequestRequestTypeDef,
    _OptionalListVehiclesInFleetRequestRequestTypeDef,
):
    pass

ListVehiclesInFleetResponseTypeDef = TypedDict(
    "ListVehiclesInFleetResponseTypeDef",
    {
        "vehicles": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVehiclesRequestRequestTypeDef = TypedDict(
    "ListVehiclesRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "attributeNames": List[str],
        "attributeValues": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListVehiclesResponseTypeDef = TypedDict(
    "ListVehiclesResponseTypeDef",
    {
        "vehicleSummaries": List["VehicleSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageSignalTypeDef = TypedDict(
    "MessageSignalTypeDef",
    {
        "topicName": str,
        "structuredMessage": "StructuredMessageTypeDef",
    },
)

_RequiredModelManifestSummaryTypeDef = TypedDict(
    "_RequiredModelManifestSummaryTypeDef",
    {
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalModelManifestSummaryTypeDef = TypedDict(
    "_OptionalModelManifestSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "signalCatalogArn": str,
        "description": str,
        "status": ManifestStatusType,
    },
    total=False,
)

class ModelManifestSummaryTypeDef(
    _RequiredModelManifestSummaryTypeDef, _OptionalModelManifestSummaryTypeDef
):
    pass

NetworkFileDefinitionTypeDef = TypedDict(
    "NetworkFileDefinitionTypeDef",
    {
        "canDbc": "CanDbcDefinitionTypeDef",
    },
    total=False,
)

_RequiredNetworkInterfaceTypeDef = TypedDict(
    "_RequiredNetworkInterfaceTypeDef",
    {
        "interfaceId": str,
        "type": NetworkInterfaceTypeType,
    },
)
_OptionalNetworkInterfaceTypeDef = TypedDict(
    "_OptionalNetworkInterfaceTypeDef",
    {
        "canInterface": "CanInterfaceTypeDef",
        "obdInterface": "ObdInterfaceTypeDef",
        "vehicleMiddleware": "VehicleMiddlewareTypeDef",
    },
    total=False,
)

class NetworkInterfaceTypeDef(_RequiredNetworkInterfaceTypeDef, _OptionalNetworkInterfaceTypeDef):
    pass

NodeCountsTypeDef = TypedDict(
    "NodeCountsTypeDef",
    {
        "totalNodes": int,
        "totalBranches": int,
        "totalSensors": int,
        "totalAttributes": int,
        "totalActuators": int,
        "totalStructs": int,
        "totalProperties": int,
    },
    total=False,
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "branch": "BranchTypeDef",
        "sensor": "SensorTypeDef",
        "actuator": "ActuatorTypeDef",
        "attribute": "AttributeTypeDef",
        "struct": "CustomStructTypeDef",
        "property": "CustomPropertyTypeDef",
    },
    total=False,
)

_RequiredObdInterfaceTypeDef = TypedDict(
    "_RequiredObdInterfaceTypeDef",
    {
        "name": str,
        "requestMessageId": int,
    },
)
_OptionalObdInterfaceTypeDef = TypedDict(
    "_OptionalObdInterfaceTypeDef",
    {
        "obdStandard": str,
        "pidRequestIntervalSeconds": int,
        "dtcRequestIntervalSeconds": int,
        "useExtendedIds": bool,
        "hasTransmissionEcu": bool,
    },
    total=False,
)

class ObdInterfaceTypeDef(_RequiredObdInterfaceTypeDef, _OptionalObdInterfaceTypeDef):
    pass

_RequiredObdSignalTypeDef = TypedDict(
    "_RequiredObdSignalTypeDef",
    {
        "pidResponseLength": int,
        "serviceMode": int,
        "pid": int,
        "scaling": float,
        "offset": float,
        "startByte": int,
        "byteLength": int,
    },
)
_OptionalObdSignalTypeDef = TypedDict(
    "_OptionalObdSignalTypeDef",
    {
        "bitRightShift": int,
        "bitMaskLength": int,
    },
    total=False,
)

class ObdSignalTypeDef(_RequiredObdSignalTypeDef, _OptionalObdSignalTypeDef):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PrimitiveMessageDefinitionTypeDef = TypedDict(
    "PrimitiveMessageDefinitionTypeDef",
    {
        "ros2PrimitiveMessageDefinition": "ROS2PrimitiveMessageDefinitionTypeDef",
    },
    total=False,
)

_RequiredPutEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutEncryptionConfigurationRequestRequestTypeDef",
    {
        "encryptionType": EncryptionTypeType,
    },
)
_OptionalPutEncryptionConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutEncryptionConfigurationRequestRequestTypeDef",
    {
        "kmsKeyId": str,
    },
    total=False,
)

class PutEncryptionConfigurationRequestRequestTypeDef(
    _RequiredPutEncryptionConfigurationRequestRequestTypeDef,
    _OptionalPutEncryptionConfigurationRequestRequestTypeDef,
):
    pass

PutEncryptionConfigurationResponseTypeDef = TypedDict(
    "PutEncryptionConfigurationResponseTypeDef",
    {
        "kmsKeyId": str,
        "encryptionStatus": EncryptionStatusType,
        "encryptionType": EncryptionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLoggingOptionsRequestRequestTypeDef = TypedDict(
    "PutLoggingOptionsRequestRequestTypeDef",
    {
        "cloudWatchLogDelivery": "CloudWatchLogDeliveryOptionsTypeDef",
    },
)

_RequiredROS2PrimitiveMessageDefinitionTypeDef = TypedDict(
    "_RequiredROS2PrimitiveMessageDefinitionTypeDef",
    {
        "primitiveType": ROS2PrimitiveTypeType,
    },
)
_OptionalROS2PrimitiveMessageDefinitionTypeDef = TypedDict(
    "_OptionalROS2PrimitiveMessageDefinitionTypeDef",
    {
        "offset": float,
        "scaling": float,
        "upperBound": int,
    },
    total=False,
)

class ROS2PrimitiveMessageDefinitionTypeDef(
    _RequiredROS2PrimitiveMessageDefinitionTypeDef, _OptionalROS2PrimitiveMessageDefinitionTypeDef
):
    pass

RegisterAccountRequestRequestTypeDef = TypedDict(
    "RegisterAccountRequestRequestTypeDef",
    {
        "timestreamResources": "TimestreamResourcesTypeDef",
        "iamResources": "IamResourcesTypeDef",
    },
    total=False,
)

RegisterAccountResponseTypeDef = TypedDict(
    "RegisterAccountResponseTypeDef",
    {
        "registerAccountStatus": RegistrationStatusType,
        "timestreamResources": "TimestreamResourcesTypeDef",
        "iamResources": "IamResourcesTypeDef",
        "creationTime": datetime,
        "lastModificationTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef",
    {
        "bucketArn": str,
    },
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef",
    {
        "dataFormat": DataFormatType,
        "storageCompressionFormat": StorageCompressionFormatType,
        "prefix": str,
    },
    total=False,
)

class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass

_RequiredSensorTypeDef = TypedDict(
    "_RequiredSensorTypeDef",
    {
        "fullyQualifiedName": str,
        "dataType": NodeDataTypeType,
    },
)
_OptionalSensorTypeDef = TypedDict(
    "_OptionalSensorTypeDef",
    {
        "description": str,
        "unit": str,
        "allowedValues": List[str],
        "min": float,
        "max": float,
        "deprecationMessage": str,
        "comment": str,
        "structFullyQualifiedName": str,
    },
    total=False,
)

class SensorTypeDef(_RequiredSensorTypeDef, _OptionalSensorTypeDef):
    pass

SignalCatalogSummaryTypeDef = TypedDict(
    "SignalCatalogSummaryTypeDef",
    {
        "name": str,
        "arn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
    total=False,
)

_RequiredSignalDecoderTypeDef = TypedDict(
    "_RequiredSignalDecoderTypeDef",
    {
        "fullyQualifiedName": str,
        "type": SignalDecoderTypeType,
        "interfaceId": str,
    },
)
_OptionalSignalDecoderTypeDef = TypedDict(
    "_OptionalSignalDecoderTypeDef",
    {
        "canSignal": "CanSignalTypeDef",
        "obdSignal": "ObdSignalTypeDef",
        "messageSignal": "MessageSignalTypeDef",
    },
    total=False,
)

class SignalDecoderTypeDef(_RequiredSignalDecoderTypeDef, _OptionalSignalDecoderTypeDef):
    pass

_RequiredSignalInformationTypeDef = TypedDict(
    "_RequiredSignalInformationTypeDef",
    {
        "name": str,
    },
)
_OptionalSignalInformationTypeDef = TypedDict(
    "_OptionalSignalInformationTypeDef",
    {
        "maxSampleCount": int,
        "minimumSamplingIntervalMs": int,
    },
    total=False,
)

class SignalInformationTypeDef(
    _RequiredSignalInformationTypeDef, _OptionalSignalInformationTypeDef
):
    pass

StructuredMessageFieldNameAndDataTypePairTypeDef = TypedDict(
    "StructuredMessageFieldNameAndDataTypePairTypeDef",
    {
        "fieldName": str,
        "dataType": "StructuredMessageTypeDef",
    },
)

_RequiredStructuredMessageListDefinitionTypeDef = TypedDict(
    "_RequiredStructuredMessageListDefinitionTypeDef",
    {
        "name": str,
        "memberType": Dict[str, Any],
        "listType": StructuredMessageListTypeType,
    },
)
_OptionalStructuredMessageListDefinitionTypeDef = TypedDict(
    "_OptionalStructuredMessageListDefinitionTypeDef",
    {
        "capacity": int,
    },
    total=False,
)

class StructuredMessageListDefinitionTypeDef(
    _RequiredStructuredMessageListDefinitionTypeDef, _OptionalStructuredMessageListDefinitionTypeDef
):
    pass

StructuredMessageTypeDef = TypedDict(
    "StructuredMessageTypeDef",
    {
        "primitiveMessageDefinition": "PrimitiveMessageDefinitionTypeDef",
        "structuredMessageListDefinition": Dict[str, Any],
        "structuredMessageDefinition": List[Dict[str, Any]],
    },
    total=False,
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

TimeBasedCollectionSchemeTypeDef = TypedDict(
    "TimeBasedCollectionSchemeTypeDef",
    {
        "periodMs": int,
    },
)

TimestreamConfigTypeDef = TypedDict(
    "TimestreamConfigTypeDef",
    {
        "timestreamTableArn": str,
        "executionRoleArn": str,
    },
)

_RequiredTimestreamRegistrationResponseTypeDef = TypedDict(
    "_RequiredTimestreamRegistrationResponseTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
        "registrationStatus": RegistrationStatusType,
    },
)
_OptionalTimestreamRegistrationResponseTypeDef = TypedDict(
    "_OptionalTimestreamRegistrationResponseTypeDef",
    {
        "timestreamDatabaseArn": str,
        "timestreamTableArn": str,
        "errorMessage": str,
    },
    total=False,
)

class TimestreamRegistrationResponseTypeDef(
    _RequiredTimestreamRegistrationResponseTypeDef, _OptionalTimestreamRegistrationResponseTypeDef
):
    pass

TimestreamResourcesTypeDef = TypedDict(
    "TimestreamResourcesTypeDef",
    {
        "timestreamDatabaseName": str,
        "timestreamTableName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateCampaignRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateCampaignRequestRequestTypeDef",
    {
        "name": str,
        "action": UpdateCampaignActionType,
    },
)
_OptionalUpdateCampaignRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateCampaignRequestRequestTypeDef",
    {
        "description": str,
        "dataExtraDimensions": List[str],
    },
    total=False,
)

class UpdateCampaignRequestRequestTypeDef(
    _RequiredUpdateCampaignRequestRequestTypeDef, _OptionalUpdateCampaignRequestRequestTypeDef
):
    pass

UpdateCampaignResponseTypeDef = TypedDict(
    "UpdateCampaignResponseTypeDef",
    {
        "arn": str,
        "name": str,
        "status": CampaignStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateDecoderManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateDecoderManifestRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateDecoderManifestRequestRequestTypeDef",
    {
        "description": str,
        "signalDecodersToAdd": List["SignalDecoderTypeDef"],
        "signalDecodersToUpdate": List["SignalDecoderTypeDef"],
        "signalDecodersToRemove": List[str],
        "networkInterfacesToAdd": List["NetworkInterfaceTypeDef"],
        "networkInterfacesToUpdate": List["NetworkInterfaceTypeDef"],
        "networkInterfacesToRemove": List[str],
        "status": ManifestStatusType,
    },
    total=False,
)

class UpdateDecoderManifestRequestRequestTypeDef(
    _RequiredUpdateDecoderManifestRequestRequestTypeDef,
    _OptionalUpdateDecoderManifestRequestRequestTypeDef,
):
    pass

UpdateDecoderManifestResponseTypeDef = TypedDict(
    "UpdateDecoderManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateFleetRequestRequestTypeDef",
    {
        "fleetId": str,
    },
)
_OptionalUpdateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateFleetRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class UpdateFleetRequestRequestTypeDef(
    _RequiredUpdateFleetRequestRequestTypeDef, _OptionalUpdateFleetRequestRequestTypeDef
):
    pass

UpdateFleetResponseTypeDef = TypedDict(
    "UpdateFleetResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateModelManifestRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateModelManifestRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateModelManifestRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateModelManifestRequestRequestTypeDef",
    {
        "description": str,
        "nodesToAdd": List[str],
        "nodesToRemove": List[str],
        "status": ManifestStatusType,
    },
    total=False,
)

class UpdateModelManifestRequestRequestTypeDef(
    _RequiredUpdateModelManifestRequestRequestTypeDef,
    _OptionalUpdateModelManifestRequestRequestTypeDef,
):
    pass

UpdateModelManifestResponseTypeDef = TypedDict(
    "UpdateModelManifestResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateSignalCatalogRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalUpdateSignalCatalogRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateSignalCatalogRequestRequestTypeDef",
    {
        "description": str,
        "nodesToAdd": List["NodeTypeDef"],
        "nodesToUpdate": List["NodeTypeDef"],
        "nodesToRemove": List[str],
    },
    total=False,
)

class UpdateSignalCatalogRequestRequestTypeDef(
    _RequiredUpdateSignalCatalogRequestRequestTypeDef,
    _OptionalUpdateSignalCatalogRequestRequestTypeDef,
):
    pass

UpdateSignalCatalogResponseTypeDef = TypedDict(
    "UpdateSignalCatalogResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVehicleErrorTypeDef = TypedDict(
    "UpdateVehicleErrorTypeDef",
    {
        "vehicleName": str,
        "code": int,
        "message": str,
    },
    total=False,
)

_RequiredUpdateVehicleRequestItemTypeDef = TypedDict(
    "_RequiredUpdateVehicleRequestItemTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalUpdateVehicleRequestItemTypeDef = TypedDict(
    "_OptionalUpdateVehicleRequestItemTypeDef",
    {
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Dict[str, str],
        "attributeUpdateMode": UpdateModeType,
    },
    total=False,
)

class UpdateVehicleRequestItemTypeDef(
    _RequiredUpdateVehicleRequestItemTypeDef, _OptionalUpdateVehicleRequestItemTypeDef
):
    pass

_RequiredUpdateVehicleRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateVehicleRequestRequestTypeDef",
    {
        "vehicleName": str,
    },
)
_OptionalUpdateVehicleRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateVehicleRequestRequestTypeDef",
    {
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "attributes": Dict[str, str],
        "attributeUpdateMode": UpdateModeType,
    },
    total=False,
)

class UpdateVehicleRequestRequestTypeDef(
    _RequiredUpdateVehicleRequestRequestTypeDef, _OptionalUpdateVehicleRequestRequestTypeDef
):
    pass

UpdateVehicleResponseItemTypeDef = TypedDict(
    "UpdateVehicleResponseItemTypeDef",
    {
        "vehicleName": str,
        "arn": str,
    },
    total=False,
)

UpdateVehicleResponseTypeDef = TypedDict(
    "UpdateVehicleResponseTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VehicleMiddlewareTypeDef = TypedDict(
    "VehicleMiddlewareTypeDef",
    {
        "name": str,
        "protocolName": Literal["ROS_2"],
    },
)

VehicleStatusTypeDef = TypedDict(
    "VehicleStatusTypeDef",
    {
        "campaignName": str,
        "vehicleName": str,
        "status": VehicleStateType,
    },
    total=False,
)

_RequiredVehicleSummaryTypeDef = TypedDict(
    "_RequiredVehicleSummaryTypeDef",
    {
        "vehicleName": str,
        "arn": str,
        "modelManifestArn": str,
        "decoderManifestArn": str,
        "creationTime": datetime,
        "lastModificationTime": datetime,
    },
)
_OptionalVehicleSummaryTypeDef = TypedDict(
    "_OptionalVehicleSummaryTypeDef",
    {
        "attributes": Dict[str, str],
    },
    total=False,
)

class VehicleSummaryTypeDef(_RequiredVehicleSummaryTypeDef, _OptionalVehicleSummaryTypeDef):
    pass
