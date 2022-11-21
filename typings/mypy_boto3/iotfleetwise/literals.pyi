"""
Type annotations for iotfleetwise service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleetwise/literals.html)

Usage::

    ```python
    from mypy_boto3_iotfleetwise.literals import CampaignStatusType

    data: CampaignStatusType = "CREATING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CampaignStatusType",
    "CompressionType",
    "DiagnosticsModeType",
    "GetVehicleStatusPaginatorName",
    "ListCampaignsPaginatorName",
    "ListDecoderManifestNetworkInterfacesPaginatorName",
    "ListDecoderManifestSignalsPaginatorName",
    "ListDecoderManifestsPaginatorName",
    "ListFleetsForVehiclePaginatorName",
    "ListFleetsPaginatorName",
    "ListModelManifestNodesPaginatorName",
    "ListModelManifestsPaginatorName",
    "ListSignalCatalogNodesPaginatorName",
    "ListSignalCatalogsPaginatorName",
    "ListVehiclesInFleetPaginatorName",
    "ListVehiclesPaginatorName",
    "LogTypeType",
    "ManifestStatusType",
    "NetworkInterfaceTypeType",
    "NodeDataTypeType",
    "RegistrationStatusType",
    "SignalDecoderTypeType",
    "SpoolingModeType",
    "TriggerModeType",
    "UpdateCampaignActionType",
    "UpdateModeType",
    "VehicleAssociationBehaviorType",
    "VehicleStateType",
)

CampaignStatusType = Literal["CREATING", "RUNNING", "SUSPENDED", "WAITING_FOR_APPROVAL"]
CompressionType = Literal["OFF", "SNAPPY"]
DiagnosticsModeType = Literal["OFF", "SEND_ACTIVE_DTCS"]
GetVehicleStatusPaginatorName = Literal["get_vehicle_status"]
ListCampaignsPaginatorName = Literal["list_campaigns"]
ListDecoderManifestNetworkInterfacesPaginatorName = Literal[
    "list_decoder_manifest_network_interfaces"
]
ListDecoderManifestSignalsPaginatorName = Literal["list_decoder_manifest_signals"]
ListDecoderManifestsPaginatorName = Literal["list_decoder_manifests"]
ListFleetsForVehiclePaginatorName = Literal["list_fleets_for_vehicle"]
ListFleetsPaginatorName = Literal["list_fleets"]
ListModelManifestNodesPaginatorName = Literal["list_model_manifest_nodes"]
ListModelManifestsPaginatorName = Literal["list_model_manifests"]
ListSignalCatalogNodesPaginatorName = Literal["list_signal_catalog_nodes"]
ListSignalCatalogsPaginatorName = Literal["list_signal_catalogs"]
ListVehiclesInFleetPaginatorName = Literal["list_vehicles_in_fleet"]
ListVehiclesPaginatorName = Literal["list_vehicles"]
LogTypeType = Literal["ERROR", "OFF"]
ManifestStatusType = Literal["ACTIVE", "DRAFT"]
NetworkInterfaceTypeType = Literal["CAN_INTERFACE", "OBD_INTERFACE"]
NodeDataTypeType = Literal[
    "BOOLEAN",
    "BOOLEAN_ARRAY",
    "DOUBLE",
    "DOUBLE_ARRAY",
    "FLOAT",
    "FLOAT_ARRAY",
    "INT16",
    "INT16_ARRAY",
    "INT32",
    "INT32_ARRAY",
    "INT64",
    "INT64_ARRAY",
    "INT8",
    "INT8_ARRAY",
    "STRING",
    "STRING_ARRAY",
    "UINT16",
    "UINT16_ARRAY",
    "UINT32",
    "UINT32_ARRAY",
    "UINT64",
    "UINT64_ARRAY",
    "UINT8",
    "UINT8_ARRAY",
    "UNIX_TIMESTAMP",
    "UNIX_TIMESTAMP_ARRAY",
    "UNKNOWN",
]
RegistrationStatusType = Literal[
    "REGISTRATION_FAILURE", "REGISTRATION_PENDING", "REGISTRATION_SUCCESS"
]
SignalDecoderTypeType = Literal["CAN_SIGNAL", "OBD_SIGNAL"]
SpoolingModeType = Literal["OFF", "TO_DISK"]
TriggerModeType = Literal["ALWAYS", "RISING_EDGE"]
UpdateCampaignActionType = Literal["APPROVE", "RESUME", "SUSPEND", "UPDATE"]
UpdateModeType = Literal["Merge", "Overwrite"]
VehicleAssociationBehaviorType = Literal["CreateIotThing", "ValidateIotThingExists"]
VehicleStateType = Literal["CREATED", "DELETING", "HEALTHY", "READY", "SUSPENDED"]