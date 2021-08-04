"""
Type annotations for groundstation service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/literals.html)

Usage::

    ```python
    from mypy_boto3_groundstation.literals import AngleUnitsType

    data: AngleUnitsType = "DEGREE_ANGLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AngleUnitsType",
    "BandwidthUnitsType",
    "ConfigCapabilityTypeType",
    "ContactStatusType",
    "CriticalityType",
    "EirpUnitsType",
    "EndpointStatusType",
    "FrequencyUnitsType",
    "ListConfigsPaginatorName",
    "ListContactsPaginatorName",
    "ListDataflowEndpointGroupsPaginatorName",
    "ListGroundStationsPaginatorName",
    "ListMissionProfilesPaginatorName",
    "ListSatellitesPaginatorName",
    "PolarizationType",
)

AngleUnitsType = Literal["DEGREE_ANGLE", "RADIAN"]
BandwidthUnitsType = Literal["GHz", "MHz", "kHz"]
ConfigCapabilityTypeType = Literal[
    "antenna-downlink",
    "antenna-downlink-demod-decode",
    "antenna-uplink",
    "dataflow-endpoint",
    "s3-recording",
    "tracking",
    "uplink-echo",
]
ContactStatusType = Literal[
    "AVAILABLE",
    "AWS_CANCELLED",
    "AWS_FAILED",
    "CANCELLED",
    "CANCELLING",
    "COMPLETED",
    "FAILED",
    "FAILED_TO_SCHEDULE",
    "PASS",
    "POSTPASS",
    "PREPASS",
    "SCHEDULED",
    "SCHEDULING",
]
CriticalityType = Literal["PREFERRED", "REMOVED", "REQUIRED"]
EirpUnitsType = Literal["dBW"]
EndpointStatusType = Literal["created", "creating", "deleted", "deleting", "failed"]
FrequencyUnitsType = Literal["GHz", "MHz", "kHz"]
ListConfigsPaginatorName = Literal["list_configs"]
ListContactsPaginatorName = Literal["list_contacts"]
ListDataflowEndpointGroupsPaginatorName = Literal["list_dataflow_endpoint_groups"]
ListGroundStationsPaginatorName = Literal["list_ground_stations"]
ListMissionProfilesPaginatorName = Literal["list_mission_profiles"]
ListSatellitesPaginatorName = Literal["list_satellites"]
PolarizationType = Literal["LEFT_HAND", "NONE", "RIGHT_HAND"]
