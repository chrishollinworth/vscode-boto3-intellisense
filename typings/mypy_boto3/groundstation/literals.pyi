"""
Type annotations for groundstation service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/literals.html)

Usage::

    ```python
    from mypy_boto3_groundstation.literals import AgentStatusType

    data: AgentStatusType = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AgentStatusType",
    "AngleUnitsType",
    "AuditResultsType",
    "BandwidthUnitsType",
    "CapabilityHealthReasonType",
    "CapabilityHealthType",
    "ConfigCapabilityTypeType",
    "ContactScheduledWaiterName",
    "ContactStatusType",
    "CriticalityType",
    "EirpUnitsType",
    "EndpointStatusType",
    "EphemerisInvalidReasonType",
    "EphemerisSourceType",
    "EphemerisStatusType",
    "FrequencyUnitsType",
    "ListConfigsPaginatorName",
    "ListContactsPaginatorName",
    "ListDataflowEndpointGroupsPaginatorName",
    "ListEphemeridesPaginatorName",
    "ListGroundStationsPaginatorName",
    "ListMissionProfilesPaginatorName",
    "ListSatellitesPaginatorName",
    "PolarizationType",
)

AgentStatusType = Literal["ACTIVE", "FAILED", "INACTIVE", "SUCCESS"]
AngleUnitsType = Literal["DEGREE_ANGLE", "RADIAN"]
AuditResultsType = Literal["HEALTHY", "UNHEALTHY"]
BandwidthUnitsType = Literal["GHz", "MHz", "kHz"]
CapabilityHealthReasonType = Literal[
    "DATAPLANE_FAILURE",
    "HEALTHY",
    "INITIALIZING_DATAPLANE",
    "INVALID_IP_OWNERSHIP",
    "NOT_AUTHORIZED_TO_CREATE_SLR",
    "NO_REGISTERED_AGENT",
    "UNVERIFIED_IP_OWNERSHIP",
]
CapabilityHealthType = Literal["HEALTHY", "UNHEALTHY"]
ConfigCapabilityTypeType = Literal[
    "antenna-downlink",
    "antenna-downlink-demod-decode",
    "antenna-uplink",
    "dataflow-endpoint",
    "s3-recording",
    "tracking",
    "uplink-echo",
]
ContactScheduledWaiterName = Literal["contact_scheduled"]
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
EphemerisInvalidReasonType = Literal[
    "KMS_KEY_INVALID",
    "METADATA_INVALID",
    "TIME_RANGE_INVALID",
    "TRAJECTORY_INVALID",
    "VALIDATION_ERROR",
]
EphemerisSourceType = Literal["CUSTOMER_PROVIDED", "SPACE_TRACK"]
EphemerisStatusType = Literal["DISABLED", "ENABLED", "ERROR", "EXPIRED", "INVALID", "VALIDATING"]
FrequencyUnitsType = Literal["GHz", "MHz", "kHz"]
ListConfigsPaginatorName = Literal["list_configs"]
ListContactsPaginatorName = Literal["list_contacts"]
ListDataflowEndpointGroupsPaginatorName = Literal["list_dataflow_endpoint_groups"]
ListEphemeridesPaginatorName = Literal["list_ephemerides"]
ListGroundStationsPaginatorName = Literal["list_ground_stations"]
ListMissionProfilesPaginatorName = Literal["list_mission_profiles"]
ListSatellitesPaginatorName = Literal["list_satellites"]
PolarizationType = Literal["LEFT_HAND", "NONE", "RIGHT_HAND"]
