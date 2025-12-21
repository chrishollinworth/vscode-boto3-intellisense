"""
Type annotations for groundstation service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_groundstation.type_defs import ComponentVersionTypeDef

    data: ComponentVersionTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AgentStatusType,
    AngleUnitsType,
    AuditResultsType,
    BandwidthUnitsType,
    CapabilityHealthReasonType,
    CapabilityHealthType,
    ConfigCapabilityTypeType,
    ContactStatusType,
    CriticalityType,
    EndpointStatusType,
    EphemerisErrorCodeType,
    EphemerisInvalidReasonType,
    EphemerisSourceType,
    EphemerisStatusType,
    EphemerisTypeType,
    FrequencyUnitsType,
    PolarizationType,
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
    "AgentDetailsTypeDef",
    "AggregateStatusTypeDef",
    "AntennaDemodDecodeDetailsTypeDef",
    "AntennaDownlinkConfigTypeDef",
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    "AntennaUplinkConfigTypeDef",
    "AwsGroundStationAgentEndpointTypeDef",
    "AzElEphemerisFilterTypeDef",
    "AzElEphemerisTypeDef",
    "AzElProgramTrackSettingsTypeDef",
    "AzElSegmentTypeDef",
    "AzElSegmentsDataTypeDef",
    "AzElSegmentsTypeDef",
    "CancelContactRequestTypeDef",
    "ComponentStatusDataTypeDef",
    "ComponentVersionTypeDef",
    "ConfigDetailsTypeDef",
    "ConfigIdResponseTypeDef",
    "ConfigListItemTypeDef",
    "ConfigTypeDataTypeDef",
    "ConnectionDetailsTypeDef",
    "ContactDataTypeDef",
    "ContactIdResponseTypeDef",
    "CreateConfigRequestTypeDef",
    "CreateDataflowEndpointGroupRequestTypeDef",
    "CreateDataflowEndpointGroupV2RequestTypeDef",
    "CreateDataflowEndpointGroupV2ResponseTypeDef",
    "CreateEndpointDetailsTypeDef",
    "CreateEphemerisRequestTypeDef",
    "CreateMissionProfileRequestTypeDef",
    "DataflowDetailTypeDef",
    "DataflowEndpointConfigTypeDef",
    "DataflowEndpointGroupIdResponseTypeDef",
    "DataflowEndpointListItemTypeDef",
    "DataflowEndpointTypeDef",
    "DecodeConfigTypeDef",
    "DeleteConfigRequestTypeDef",
    "DeleteDataflowEndpointGroupRequestTypeDef",
    "DeleteEphemerisRequestTypeDef",
    "DeleteMissionProfileRequestTypeDef",
    "DemodulationConfigTypeDef",
    "DescribeContactRequestTypeDef",
    "DescribeContactRequestWaitTypeDef",
    "DescribeContactResponseTypeDef",
    "DescribeEphemerisRequestTypeDef",
    "DescribeEphemerisResponseTypeDef",
    "DestinationTypeDef",
    "DiscoveryDataTypeDef",
    "DownlinkAwsGroundStationAgentEndpointDetailsTypeDef",
    "DownlinkAwsGroundStationAgentEndpointTypeDef",
    "DownlinkConnectionDetailsTypeDef",
    "DownlinkDataflowDetailsTypeDef",
    "EirpTypeDef",
    "ElevationTypeDef",
    "EndpointDetailsOutputTypeDef",
    "EndpointDetailsTypeDef",
    "EndpointDetailsUnionTypeDef",
    "EphemerisDataTypeDef",
    "EphemerisDescriptionTypeDef",
    "EphemerisErrorReasonTypeDef",
    "EphemerisFilterTypeDef",
    "EphemerisIdResponseTypeDef",
    "EphemerisItemTypeDef",
    "EphemerisMetaDataTypeDef",
    "EphemerisResponseDataTypeDef",
    "EphemerisTypeDescriptionTypeDef",
    "FrequencyBandwidthTypeDef",
    "FrequencyTypeDef",
    "GetAgentConfigurationRequestTypeDef",
    "GetAgentConfigurationResponseTypeDef",
    "GetAgentTaskResponseUrlRequestTypeDef",
    "GetAgentTaskResponseUrlResponseTypeDef",
    "GetConfigRequestTypeDef",
    "GetConfigResponseTypeDef",
    "GetDataflowEndpointGroupRequestTypeDef",
    "GetDataflowEndpointGroupResponseTypeDef",
    "GetMinuteUsageRequestTypeDef",
    "GetMinuteUsageResponseTypeDef",
    "GetMissionProfileRequestTypeDef",
    "GetMissionProfileResponseTypeDef",
    "GetSatelliteRequestTypeDef",
    "GetSatelliteResponseTypeDef",
    "GroundStationDataTypeDef",
    "ISO8601TimeRangeTypeDef",
    "IntegerRangeTypeDef",
    "KmsKeyTypeDef",
    "ListConfigsRequestPaginateTypeDef",
    "ListConfigsRequestTypeDef",
    "ListConfigsResponseTypeDef",
    "ListContactsRequestPaginateTypeDef",
    "ListContactsRequestTypeDef",
    "ListContactsResponseTypeDef",
    "ListDataflowEndpointGroupsRequestPaginateTypeDef",
    "ListDataflowEndpointGroupsRequestTypeDef",
    "ListDataflowEndpointGroupsResponseTypeDef",
    "ListEphemeridesRequestPaginateTypeDef",
    "ListEphemeridesRequestTypeDef",
    "ListEphemeridesResponseTypeDef",
    "ListGroundStationsRequestPaginateTypeDef",
    "ListGroundStationsRequestTypeDef",
    "ListGroundStationsResponseTypeDef",
    "ListMissionProfilesRequestPaginateTypeDef",
    "ListMissionProfilesRequestTypeDef",
    "ListMissionProfilesResponseTypeDef",
    "ListSatellitesRequestPaginateTypeDef",
    "ListSatellitesRequestTypeDef",
    "ListSatellitesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MissionProfileIdResponseTypeDef",
    "MissionProfileListItemTypeDef",
    "OEMEphemerisTypeDef",
    "PaginatorConfigTypeDef",
    "ProgramTrackSettingsTypeDef",
    "RangedConnectionDetailsTypeDef",
    "RangedSocketAddressTypeDef",
    "RegisterAgentRequestTypeDef",
    "RegisterAgentResponseTypeDef",
    "ReserveContactRequestTypeDef",
    "ResponseMetadataTypeDef",
    "S3ObjectTypeDef",
    "S3RecordingConfigTypeDef",
    "S3RecordingDetailsTypeDef",
    "SatelliteListItemTypeDef",
    "SecurityDetailsOutputTypeDef",
    "SecurityDetailsTypeDef",
    "SecurityDetailsUnionTypeDef",
    "SocketAddressTypeDef",
    "SourceTypeDef",
    "SpectrumConfigTypeDef",
    "TLEDataTypeDef",
    "TLEEphemerisTypeDef",
    "TagResourceRequestTypeDef",
    "TimeAzElTypeDef",
    "TimeRangeTypeDef",
    "TimestampTypeDef",
    "TrackingConfigTypeDef",
    "TrackingOverridesTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAgentStatusRequestTypeDef",
    "UpdateAgentStatusResponseTypeDef",
    "UpdateConfigRequestTypeDef",
    "UpdateEphemerisRequestTypeDef",
    "UpdateMissionProfileRequestTypeDef",
    "UplinkAwsGroundStationAgentEndpointDetailsTypeDef",
    "UplinkAwsGroundStationAgentEndpointTypeDef",
    "UplinkConnectionDetailsTypeDef",
    "UplinkDataflowDetailsTypeDef",
    "UplinkEchoConfigTypeDef",
    "UplinkSpectrumConfigTypeDef",
    "WaiterConfigTypeDef",
)

class ComponentVersionTypeDef(TypedDict):
    componentType: str
    versions: Sequence[str]

class AggregateStatusTypeDef(TypedDict):
    status: AgentStatusType
    signatureMap: NotRequired[Mapping[str, bool]]

class AntennaDemodDecodeDetailsTypeDef(TypedDict):
    outputNode: NotRequired[str]

class DecodeConfigTypeDef(TypedDict):
    unvalidatedJSON: str

class DemodulationConfigTypeDef(TypedDict):
    unvalidatedJSON: str

class EirpTypeDef(TypedDict):
    value: float
    units: Literal["dBW"]

AzElEphemerisFilterTypeDef = TypedDict(
    "AzElEphemerisFilterTypeDef",
    {
        "id": str,
    },
)

class AzElProgramTrackSettingsTypeDef(TypedDict):
    ephemerisId: str

class TimeAzElTypeDef(TypedDict):
    dt: float
    az: float
    el: float

TimestampTypeDef = Union[datetime, str]

class S3ObjectTypeDef(TypedDict):
    bucket: NotRequired[str]
    key: NotRequired[str]
    version: NotRequired[str]

class CancelContactRequestTypeDef(TypedDict):
    contactId: str

class ComponentStatusDataTypeDef(TypedDict):
    componentType: str
    capabilityArn: str
    status: AgentStatusType
    dataflowId: str
    bytesSent: NotRequired[int]
    bytesReceived: NotRequired[int]
    packetsDropped: NotRequired[int]

class S3RecordingDetailsTypeDef(TypedDict):
    bucketArn: NotRequired[str]
    keyTemplate: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ConfigListItemTypeDef(TypedDict):
    configId: NotRequired[str]
    configType: NotRequired[ConfigCapabilityTypeType]
    configArn: NotRequired[str]
    name: NotRequired[str]

class DataflowEndpointConfigTypeDef(TypedDict):
    dataflowEndpointName: str
    dataflowEndpointRegion: NotRequired[str]

class S3RecordingConfigTypeDef(TypedDict):
    bucketArn: str
    roleArn: str
    prefix: NotRequired[str]

class TrackingConfigTypeDef(TypedDict):
    autotrack: CriticalityType

class UplinkEchoConfigTypeDef(TypedDict):
    enabled: bool
    antennaUplinkConfigArn: str

class SocketAddressTypeDef(TypedDict):
    name: str
    port: int

class ElevationTypeDef(TypedDict):
    value: float
    unit: AngleUnitsType

class EphemerisResponseDataTypeDef(TypedDict):
    ephemerisType: EphemerisTypeType
    ephemerisId: NotRequired[str]

class KmsKeyTypeDef(TypedDict):
    kmsKeyArn: NotRequired[str]
    kmsAliasArn: NotRequired[str]
    kmsAliasName: NotRequired[str]

class DataflowEndpointListItemTypeDef(TypedDict):
    dataflowEndpointGroupId: NotRequired[str]
    dataflowEndpointGroupArn: NotRequired[str]

class DeleteConfigRequestTypeDef(TypedDict):
    configId: str
    configType: ConfigCapabilityTypeType

class DeleteDataflowEndpointGroupRequestTypeDef(TypedDict):
    dataflowEndpointGroupId: str

class DeleteEphemerisRequestTypeDef(TypedDict):
    ephemerisId: str

class DeleteMissionProfileRequestTypeDef(TypedDict):
    missionProfileId: str

class DescribeContactRequestTypeDef(TypedDict):
    contactId: str

class WaiterConfigTypeDef(TypedDict):
    Delay: NotRequired[int]
    MaxAttempts: NotRequired[int]

class DescribeEphemerisRequestTypeDef(TypedDict):
    ephemerisId: str

class EphemerisErrorReasonTypeDef(TypedDict):
    errorCode: EphemerisErrorCodeType
    errorMessage: str

class DiscoveryDataTypeDef(TypedDict):
    publicIpAddresses: Sequence[str]
    privateIpAddresses: Sequence[str]
    capabilityArns: Sequence[str]

class SecurityDetailsOutputTypeDef(TypedDict):
    subnetIds: List[str]
    securityGroupIds: List[str]
    roleArn: str

class EphemerisMetaDataTypeDef(TypedDict):
    source: EphemerisSourceType
    ephemerisId: NotRequired[str]
    epoch: NotRequired[datetime]
    name: NotRequired[str]

class FrequencyBandwidthTypeDef(TypedDict):
    value: float
    units: BandwidthUnitsType

class FrequencyTypeDef(TypedDict):
    value: float
    units: FrequencyUnitsType

class GetAgentConfigurationRequestTypeDef(TypedDict):
    agentId: str

class GetAgentTaskResponseUrlRequestTypeDef(TypedDict):
    agentId: str
    taskId: str

class GetConfigRequestTypeDef(TypedDict):
    configId: str
    configType: ConfigCapabilityTypeType

class GetDataflowEndpointGroupRequestTypeDef(TypedDict):
    dataflowEndpointGroupId: str

class GetMinuteUsageRequestTypeDef(TypedDict):
    month: int
    year: int

class GetMissionProfileRequestTypeDef(TypedDict):
    missionProfileId: str

class GetSatelliteRequestTypeDef(TypedDict):
    satelliteId: str

class GroundStationDataTypeDef(TypedDict):
    groundStationId: NotRequired[str]
    groundStationName: NotRequired[str]
    region: NotRequired[str]

class IntegerRangeTypeDef(TypedDict):
    minimum: int
    maximum: int

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListConfigsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDataflowEndpointGroupsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListGroundStationsRequestTypeDef(TypedDict):
    satelliteId: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListMissionProfilesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class MissionProfileListItemTypeDef(TypedDict):
    missionProfileId: NotRequired[str]
    missionProfileArn: NotRequired[str]
    region: NotRequired[str]
    name: NotRequired[str]

class ListSatellitesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class SecurityDetailsTypeDef(TypedDict):
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]
    roleArn: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateEphemerisRequestTypeDef(TypedDict):
    ephemerisId: str
    enabled: bool
    name: NotRequired[str]
    priority: NotRequired[int]

class AgentDetailsTypeDef(TypedDict):
    agentVersion: str
    instanceId: str
    instanceType: str
    componentVersions: Sequence[ComponentVersionTypeDef]
    reservedCpuCores: NotRequired[Sequence[int]]
    agentCpuCores: NotRequired[Sequence[int]]

class EphemerisFilterTypeDef(TypedDict):
    azEl: NotRequired[AzElEphemerisFilterTypeDef]

class ProgramTrackSettingsTypeDef(TypedDict):
    azEl: NotRequired[AzElProgramTrackSettingsTypeDef]

class ISO8601TimeRangeTypeDef(TypedDict):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef

class ListEphemeridesRequestTypeDef(TypedDict):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    satelliteId: NotRequired[str]
    ephemerisType: NotRequired[EphemerisTypeType]
    statusList: NotRequired[Sequence[EphemerisStatusType]]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class TimeRangeTypeDef(TypedDict):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef

class EphemerisDescriptionTypeDef(TypedDict):
    sourceS3Object: NotRequired[S3ObjectTypeDef]
    ephemerisData: NotRequired[str]

class EphemerisItemTypeDef(TypedDict):
    ephemerisId: NotRequired[str]
    ephemerisType: NotRequired[EphemerisTypeType]
    status: NotRequired[EphemerisStatusType]
    priority: NotRequired[int]
    enabled: NotRequired[bool]
    creationTime: NotRequired[datetime]
    name: NotRequired[str]
    sourceS3Object: NotRequired[S3ObjectTypeDef]

class OEMEphemerisTypeDef(TypedDict):
    s3Object: NotRequired[S3ObjectTypeDef]
    oemData: NotRequired[str]

class UpdateAgentStatusRequestTypeDef(TypedDict):
    agentId: str
    taskId: str
    aggregateStatus: AggregateStatusTypeDef
    componentStatuses: Sequence[ComponentStatusDataTypeDef]

class ConfigIdResponseTypeDef(TypedDict):
    configId: str
    configType: ConfigCapabilityTypeType
    configArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContactIdResponseTypeDef(TypedDict):
    contactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataflowEndpointGroupV2ResponseTypeDef(TypedDict):
    dataflowEndpointGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataflowEndpointGroupIdResponseTypeDef(TypedDict):
    dataflowEndpointGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EphemerisIdResponseTypeDef(TypedDict):
    ephemerisId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentConfigurationResponseTypeDef(TypedDict):
    agentId: str
    taskingDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgentTaskResponseUrlResponseTypeDef(TypedDict):
    agentId: str
    taskId: str
    presignedLogUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetMinuteUsageResponseTypeDef(TypedDict):
    isReservedMinutesCustomer: bool
    totalReservedMinuteAllocation: int
    upcomingMinutesScheduled: int
    totalScheduledMinutes: int
    estimatedMinutesRemaining: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MissionProfileIdResponseTypeDef(TypedDict):
    missionProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterAgentResponseTypeDef(TypedDict):
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgentStatusResponseTypeDef(TypedDict):
    agentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListConfigsResponseTypeDef(TypedDict):
    configList: List[ConfigListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ConnectionDetailsTypeDef(TypedDict):
    socketAddress: SocketAddressTypeDef
    mtu: NotRequired[int]

class DataflowEndpointTypeDef(TypedDict):
    name: NotRequired[str]
    address: NotRequired[SocketAddressTypeDef]
    status: NotRequired[EndpointStatusType]
    mtu: NotRequired[int]

class ContactDataTypeDef(TypedDict):
    contactId: NotRequired[str]
    missionProfileArn: NotRequired[str]
    satelliteArn: NotRequired[str]
    startTime: NotRequired[datetime]
    endTime: NotRequired[datetime]
    prePassStartTime: NotRequired[datetime]
    postPassEndTime: NotRequired[datetime]
    groundStation: NotRequired[str]
    contactStatus: NotRequired[ContactStatusType]
    errorMessage: NotRequired[str]
    maximumElevation: NotRequired[ElevationTypeDef]
    region: NotRequired[str]
    tags: NotRequired[Dict[str, str]]
    visibilityStartTime: NotRequired[datetime]
    visibilityEndTime: NotRequired[datetime]
    ephemeris: NotRequired[EphemerisResponseDataTypeDef]

class CreateMissionProfileRequestTypeDef(TypedDict):
    name: str
    minimumViableContactDurationSeconds: int
    dataflowEdges: Sequence[Sequence[str]]
    trackingConfigArn: str
    contactPrePassDurationSeconds: NotRequired[int]
    contactPostPassDurationSeconds: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]
    streamsKmsKey: NotRequired[KmsKeyTypeDef]
    streamsKmsRole: NotRequired[str]

class GetMissionProfileResponseTypeDef(TypedDict):
    missionProfileId: str
    missionProfileArn: str
    name: str
    region: str
    contactPrePassDurationSeconds: int
    contactPostPassDurationSeconds: int
    minimumViableContactDurationSeconds: int
    dataflowEdges: List[List[str]]
    trackingConfigArn: str
    tags: Dict[str, str]
    streamsKmsKey: KmsKeyTypeDef
    streamsKmsRole: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMissionProfileRequestTypeDef(TypedDict):
    missionProfileId: str
    name: NotRequired[str]
    contactPrePassDurationSeconds: NotRequired[int]
    contactPostPassDurationSeconds: NotRequired[int]
    minimumViableContactDurationSeconds: NotRequired[int]
    dataflowEdges: NotRequired[Sequence[Sequence[str]]]
    trackingConfigArn: NotRequired[str]
    streamsKmsKey: NotRequired[KmsKeyTypeDef]
    streamsKmsRole: NotRequired[str]

class ListDataflowEndpointGroupsResponseTypeDef(TypedDict):
    dataflowEndpointGroupList: List[DataflowEndpointListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeContactRequestWaitTypeDef(TypedDict):
    contactId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class GetSatelliteResponseTypeDef(TypedDict):
    satelliteId: str
    satelliteArn: str
    noradSatelliteID: int
    groundStations: List[str]
    currentEphemeris: EphemerisMetaDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SatelliteListItemTypeDef(TypedDict):
    satelliteId: NotRequired[str]
    satelliteArn: NotRequired[str]
    noradSatelliteID: NotRequired[int]
    groundStations: NotRequired[List[str]]
    currentEphemeris: NotRequired[EphemerisMetaDataTypeDef]

class SpectrumConfigTypeDef(TypedDict):
    centerFrequency: FrequencyTypeDef
    bandwidth: FrequencyBandwidthTypeDef
    polarization: NotRequired[PolarizationType]

class UplinkSpectrumConfigTypeDef(TypedDict):
    centerFrequency: FrequencyTypeDef
    polarization: NotRequired[PolarizationType]

class ListGroundStationsResponseTypeDef(TypedDict):
    groundStationList: List[GroundStationDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class RangedSocketAddressTypeDef(TypedDict):
    name: str
    portRange: IntegerRangeTypeDef

class ListConfigsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataflowEndpointGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEphemeridesRequestPaginateTypeDef(TypedDict):
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    satelliteId: NotRequired[str]
    ephemerisType: NotRequired[EphemerisTypeType]
    statusList: NotRequired[Sequence[EphemerisStatusType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroundStationsRequestPaginateTypeDef(TypedDict):
    satelliteId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMissionProfilesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSatellitesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMissionProfilesResponseTypeDef(TypedDict):
    missionProfileList: List[MissionProfileListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

SecurityDetailsUnionTypeDef = Union[SecurityDetailsTypeDef, SecurityDetailsOutputTypeDef]

class RegisterAgentRequestTypeDef(TypedDict):
    discoveryData: DiscoveryDataTypeDef
    agentDetails: AgentDetailsTypeDef
    tags: NotRequired[Mapping[str, str]]

class ListContactsRequestPaginateTypeDef(TypedDict):
    statusList: Sequence[ContactStatusType]
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    groundStation: NotRequired[str]
    satelliteArn: NotRequired[str]
    missionProfileArn: NotRequired[str]
    ephemeris: NotRequired[EphemerisFilterTypeDef]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListContactsRequestTypeDef(TypedDict):
    statusList: Sequence[ContactStatusType]
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    groundStation: NotRequired[str]
    satelliteArn: NotRequired[str]
    missionProfileArn: NotRequired[str]
    ephemeris: NotRequired[EphemerisFilterTypeDef]

class TrackingOverridesTypeDef(TypedDict):
    programTrackSettings: ProgramTrackSettingsTypeDef

class AzElSegmentTypeDef(TypedDict):
    referenceEpoch: TimestampTypeDef
    validTimeRange: ISO8601TimeRangeTypeDef
    azElList: Sequence[TimeAzElTypeDef]

class TLEDataTypeDef(TypedDict):
    tleLine1: str
    tleLine2: str
    validTimeRange: TimeRangeTypeDef

class EphemerisTypeDescriptionTypeDef(TypedDict):
    tle: NotRequired[EphemerisDescriptionTypeDef]
    oem: NotRequired[EphemerisDescriptionTypeDef]
    azEl: NotRequired[EphemerisDescriptionTypeDef]

class ListEphemeridesResponseTypeDef(TypedDict):
    ephemerides: List[EphemerisItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListContactsResponseTypeDef(TypedDict):
    contactList: List[ContactDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSatellitesResponseTypeDef(TypedDict):
    satellites: List[SatelliteListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AntennaDownlinkConfigTypeDef(TypedDict):
    spectrumConfig: SpectrumConfigTypeDef

class AntennaDownlinkDemodDecodeConfigTypeDef(TypedDict):
    spectrumConfig: SpectrumConfigTypeDef
    demodulationConfig: DemodulationConfigTypeDef
    decodeConfig: DecodeConfigTypeDef

class AntennaUplinkConfigTypeDef(TypedDict):
    spectrumConfig: UplinkSpectrumConfigTypeDef
    targetEirp: EirpTypeDef
    transmitDisabled: NotRequired[bool]

class RangedConnectionDetailsTypeDef(TypedDict):
    socketAddress: RangedSocketAddressTypeDef
    mtu: NotRequired[int]

class ReserveContactRequestTypeDef(TypedDict):
    missionProfileArn: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    groundStation: str
    satelliteArn: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    trackingOverrides: NotRequired[TrackingOverridesTypeDef]

class AzElSegmentsTypeDef(TypedDict):
    angleUnit: AngleUnitsType
    azElSegmentList: Sequence[AzElSegmentTypeDef]

class TLEEphemerisTypeDef(TypedDict):
    s3Object: NotRequired[S3ObjectTypeDef]
    tleData: NotRequired[Sequence[TLEDataTypeDef]]

class DescribeEphemerisResponseTypeDef(TypedDict):
    ephemerisId: str
    satelliteId: str
    status: EphemerisStatusType
    priority: int
    creationTime: datetime
    enabled: bool
    name: str
    tags: Dict[str, str]
    suppliedData: EphemerisTypeDescriptionTypeDef
    invalidReason: EphemerisInvalidReasonType
    errorReasons: List[EphemerisErrorReasonTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigTypeDataTypeDef(TypedDict):
    antennaDownlinkConfig: NotRequired[AntennaDownlinkConfigTypeDef]
    trackingConfig: NotRequired[TrackingConfigTypeDef]
    dataflowEndpointConfig: NotRequired[DataflowEndpointConfigTypeDef]
    antennaDownlinkDemodDecodeConfig: NotRequired[AntennaDownlinkDemodDecodeConfigTypeDef]
    antennaUplinkConfig: NotRequired[AntennaUplinkConfigTypeDef]
    uplinkEchoConfig: NotRequired[UplinkEchoConfigTypeDef]
    s3RecordingConfig: NotRequired[S3RecordingConfigTypeDef]

class AwsGroundStationAgentEndpointTypeDef(TypedDict):
    name: str
    egressAddress: ConnectionDetailsTypeDef
    ingressAddress: RangedConnectionDetailsTypeDef
    agentStatus: NotRequired[AgentStatusType]
    auditResults: NotRequired[AuditResultsType]

class DownlinkConnectionDetailsTypeDef(TypedDict):
    agentIpAndPortAddress: RangedConnectionDetailsTypeDef
    egressAddressAndPort: ConnectionDetailsTypeDef

class UplinkConnectionDetailsTypeDef(TypedDict):
    ingressAddressAndPort: ConnectionDetailsTypeDef
    agentIpAndPortAddress: RangedConnectionDetailsTypeDef

class AzElSegmentsDataTypeDef(TypedDict):
    s3Object: NotRequired[S3ObjectTypeDef]
    azElData: NotRequired[AzElSegmentsTypeDef]

class CreateConfigRequestTypeDef(TypedDict):
    name: str
    configData: ConfigTypeDataTypeDef
    tags: NotRequired[Mapping[str, str]]

class GetConfigResponseTypeDef(TypedDict):
    configId: str
    configArn: str
    name: str
    configType: ConfigCapabilityTypeType
    configData: ConfigTypeDataTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfigRequestTypeDef(TypedDict):
    configId: str
    name: str
    configType: ConfigCapabilityTypeType
    configData: ConfigTypeDataTypeDef

class DownlinkDataflowDetailsTypeDef(TypedDict):
    agentConnectionDetails: NotRequired[DownlinkConnectionDetailsTypeDef]

class UplinkDataflowDetailsTypeDef(TypedDict):
    agentConnectionDetails: NotRequired[UplinkConnectionDetailsTypeDef]

class AzElEphemerisTypeDef(TypedDict):
    groundStation: str
    data: AzElSegmentsDataTypeDef

class DownlinkAwsGroundStationAgentEndpointDetailsTypeDef(TypedDict):
    name: str
    dataflowDetails: DownlinkDataflowDetailsTypeDef
    agentStatus: NotRequired[AgentStatusType]
    auditResults: NotRequired[AuditResultsType]

class DownlinkAwsGroundStationAgentEndpointTypeDef(TypedDict):
    name: str
    dataflowDetails: DownlinkDataflowDetailsTypeDef

class UplinkAwsGroundStationAgentEndpointDetailsTypeDef(TypedDict):
    name: str
    dataflowDetails: UplinkDataflowDetailsTypeDef
    agentStatus: NotRequired[AgentStatusType]
    auditResults: NotRequired[AuditResultsType]

class UplinkAwsGroundStationAgentEndpointTypeDef(TypedDict):
    name: str
    dataflowDetails: UplinkDataflowDetailsTypeDef

class EphemerisDataTypeDef(TypedDict):
    tle: NotRequired[TLEEphemerisTypeDef]
    oem: NotRequired[OEMEphemerisTypeDef]
    azEl: NotRequired[AzElEphemerisTypeDef]

class EndpointDetailsOutputTypeDef(TypedDict):
    securityDetails: NotRequired[SecurityDetailsOutputTypeDef]
    endpoint: NotRequired[DataflowEndpointTypeDef]
    awsGroundStationAgentEndpoint: NotRequired[AwsGroundStationAgentEndpointTypeDef]
    uplinkAwsGroundStationAgentEndpoint: NotRequired[
        UplinkAwsGroundStationAgentEndpointDetailsTypeDef
    ]
    downlinkAwsGroundStationAgentEndpoint: NotRequired[
        DownlinkAwsGroundStationAgentEndpointDetailsTypeDef
    ]
    healthStatus: NotRequired[CapabilityHealthType]
    healthReasons: NotRequired[List[CapabilityHealthReasonType]]

class EndpointDetailsTypeDef(TypedDict):
    securityDetails: NotRequired[SecurityDetailsUnionTypeDef]
    endpoint: NotRequired[DataflowEndpointTypeDef]
    awsGroundStationAgentEndpoint: NotRequired[AwsGroundStationAgentEndpointTypeDef]
    uplinkAwsGroundStationAgentEndpoint: NotRequired[
        UplinkAwsGroundStationAgentEndpointDetailsTypeDef
    ]
    downlinkAwsGroundStationAgentEndpoint: NotRequired[
        DownlinkAwsGroundStationAgentEndpointDetailsTypeDef
    ]
    healthStatus: NotRequired[CapabilityHealthType]
    healthReasons: NotRequired[Sequence[CapabilityHealthReasonType]]

class CreateEndpointDetailsTypeDef(TypedDict):
    uplinkAwsGroundStationAgentEndpoint: NotRequired[UplinkAwsGroundStationAgentEndpointTypeDef]
    downlinkAwsGroundStationAgentEndpoint: NotRequired[DownlinkAwsGroundStationAgentEndpointTypeDef]

class CreateEphemerisRequestTypeDef(TypedDict):
    name: str
    satelliteId: NotRequired[str]
    enabled: NotRequired[bool]
    priority: NotRequired[int]
    expirationTime: NotRequired[TimestampTypeDef]
    kmsKeyArn: NotRequired[str]
    ephemeris: NotRequired[EphemerisDataTypeDef]
    tags: NotRequired[Mapping[str, str]]

class ConfigDetailsTypeDef(TypedDict):
    endpointDetails: NotRequired[EndpointDetailsOutputTypeDef]
    antennaDemodDecodeDetails: NotRequired[AntennaDemodDecodeDetailsTypeDef]
    s3RecordingDetails: NotRequired[S3RecordingDetailsTypeDef]

class GetDataflowEndpointGroupResponseTypeDef(TypedDict):
    dataflowEndpointGroupId: str
    dataflowEndpointGroupArn: str
    endpointsDetails: List[EndpointDetailsOutputTypeDef]
    tags: Dict[str, str]
    contactPrePassDurationSeconds: int
    contactPostPassDurationSeconds: int
    ResponseMetadata: ResponseMetadataTypeDef

EndpointDetailsUnionTypeDef = Union[EndpointDetailsTypeDef, EndpointDetailsOutputTypeDef]

class CreateDataflowEndpointGroupV2RequestTypeDef(TypedDict):
    endpoints: Sequence[CreateEndpointDetailsTypeDef]
    contactPrePassDurationSeconds: NotRequired[int]
    contactPostPassDurationSeconds: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]

class DestinationTypeDef(TypedDict):
    configType: NotRequired[ConfigCapabilityTypeType]
    configId: NotRequired[str]
    configDetails: NotRequired[ConfigDetailsTypeDef]
    dataflowDestinationRegion: NotRequired[str]

class SourceTypeDef(TypedDict):
    configType: NotRequired[ConfigCapabilityTypeType]
    configId: NotRequired[str]
    configDetails: NotRequired[ConfigDetailsTypeDef]
    dataflowSourceRegion: NotRequired[str]

class CreateDataflowEndpointGroupRequestTypeDef(TypedDict):
    endpointDetails: Sequence[EndpointDetailsUnionTypeDef]
    tags: NotRequired[Mapping[str, str]]
    contactPrePassDurationSeconds: NotRequired[int]
    contactPostPassDurationSeconds: NotRequired[int]

class DataflowDetailTypeDef(TypedDict):
    source: NotRequired[SourceTypeDef]
    destination: NotRequired[DestinationTypeDef]
    errorMessage: NotRequired[str]

class DescribeContactResponseTypeDef(TypedDict):
    contactId: str
    missionProfileArn: str
    satelliteArn: str
    startTime: datetime
    endTime: datetime
    prePassStartTime: datetime
    postPassEndTime: datetime
    groundStation: str
    contactStatus: ContactStatusType
    errorMessage: str
    maximumElevation: ElevationTypeDef
    tags: Dict[str, str]
    region: str
    dataflowList: List[DataflowDetailTypeDef]
    visibilityStartTime: datetime
    visibilityEndTime: datetime
    trackingOverrides: TrackingOverridesTypeDef
    ephemeris: EphemerisResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
