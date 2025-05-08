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
    EphemerisInvalidReasonType,
    EphemerisSourceType,
    EphemerisStatusType,
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
    "EirpTypeDef",
    "ElevationTypeDef",
    "EndpointDetailsOutputTypeDef",
    "EndpointDetailsTypeDef",
    "EndpointDetailsUnionTypeDef",
    "EphemerisDataTypeDef",
    "EphemerisDescriptionTypeDef",
    "EphemerisIdResponseTypeDef",
    "EphemerisItemTypeDef",
    "EphemerisMetaDataTypeDef",
    "EphemerisTypeDescriptionTypeDef",
    "FrequencyBandwidthTypeDef",
    "FrequencyTypeDef",
    "GetAgentConfigurationRequestTypeDef",
    "GetAgentConfigurationResponseTypeDef",
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
    "TimeRangeTypeDef",
    "TimestampTypeDef",
    "TrackingConfigTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAgentStatusRequestTypeDef",
    "UpdateAgentStatusResponseTypeDef",
    "UpdateConfigRequestTypeDef",
    "UpdateEphemerisRequestTypeDef",
    "UpdateMissionProfileRequestTypeDef",
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
    units: Literal["dBW"]
    value: float

class CancelContactRequestTypeDef(TypedDict):
    contactId: str

class ComponentStatusDataTypeDef(TypedDict):
    capabilityArn: str
    componentType: str
    dataflowId: str
    status: AgentStatusType
    bytesReceived: NotRequired[int]
    bytesSent: NotRequired[int]
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
    configArn: NotRequired[str]
    configId: NotRequired[str]
    configType: NotRequired[ConfigCapabilityTypeType]
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
    antennaUplinkConfigArn: str
    enabled: bool

class SocketAddressTypeDef(TypedDict):
    name: str
    port: int

class ElevationTypeDef(TypedDict):
    unit: AngleUnitsType
    value: float

TimestampTypeDef = Union[datetime, str]

class KmsKeyTypeDef(TypedDict):
    kmsAliasArn: NotRequired[str]
    kmsAliasName: NotRequired[str]
    kmsKeyArn: NotRequired[str]

class DataflowEndpointListItemTypeDef(TypedDict):
    dataflowEndpointGroupArn: NotRequired[str]
    dataflowEndpointGroupId: NotRequired[str]

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

class DiscoveryDataTypeDef(TypedDict):
    capabilityArns: Sequence[str]
    privateIpAddresses: Sequence[str]
    publicIpAddresses: Sequence[str]

class SecurityDetailsOutputTypeDef(TypedDict):
    roleArn: str
    securityGroupIds: List[str]
    subnetIds: List[str]

class S3ObjectTypeDef(TypedDict):
    bucket: NotRequired[str]
    key: NotRequired[str]
    version: NotRequired[str]

class EphemerisMetaDataTypeDef(TypedDict):
    source: EphemerisSourceType
    ephemerisId: NotRequired[str]
    epoch: NotRequired[datetime]
    name: NotRequired[str]

class FrequencyBandwidthTypeDef(TypedDict):
    units: BandwidthUnitsType
    value: float

class FrequencyTypeDef(TypedDict):
    units: FrequencyUnitsType
    value: float

class GetAgentConfigurationRequestTypeDef(TypedDict):
    agentId: str

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
    maximum: int
    minimum: int

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
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    satelliteId: NotRequired[str]

class ListMissionProfilesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class MissionProfileListItemTypeDef(TypedDict):
    missionProfileArn: NotRequired[str]
    missionProfileId: NotRequired[str]
    name: NotRequired[str]
    region: NotRequired[str]

class ListSatellitesRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class SecurityDetailsTypeDef(TypedDict):
    roleArn: str
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateEphemerisRequestTypeDef(TypedDict):
    enabled: bool
    ephemerisId: str
    name: NotRequired[str]
    priority: NotRequired[int]

class AgentDetailsTypeDef(TypedDict):
    agentVersion: str
    componentVersions: Sequence[ComponentVersionTypeDef]
    instanceId: str
    instanceType: str
    agentCpuCores: NotRequired[Sequence[int]]
    reservedCpuCores: NotRequired[Sequence[int]]

class UpdateAgentStatusRequestTypeDef(TypedDict):
    agentId: str
    aggregateStatus: AggregateStatusTypeDef
    componentStatuses: Sequence[ComponentStatusDataTypeDef]
    taskId: str

class ConfigIdResponseTypeDef(TypedDict):
    configArn: str
    configId: str
    configType: ConfigCapabilityTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ContactIdResponseTypeDef(TypedDict):
    contactId: str
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

class GetMinuteUsageResponseTypeDef(TypedDict):
    estimatedMinutesRemaining: int
    isReservedMinutesCustomer: bool
    totalReservedMinuteAllocation: int
    totalScheduledMinutes: int
    upcomingMinutesScheduled: int
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
    address: NotRequired[SocketAddressTypeDef]
    mtu: NotRequired[int]
    name: NotRequired[str]
    status: NotRequired[EndpointStatusType]

class ContactDataTypeDef(TypedDict):
    contactId: NotRequired[str]
    contactStatus: NotRequired[ContactStatusType]
    endTime: NotRequired[datetime]
    errorMessage: NotRequired[str]
    groundStation: NotRequired[str]
    maximumElevation: NotRequired[ElevationTypeDef]
    missionProfileArn: NotRequired[str]
    postPassEndTime: NotRequired[datetime]
    prePassStartTime: NotRequired[datetime]
    region: NotRequired[str]
    satelliteArn: NotRequired[str]
    startTime: NotRequired[datetime]
    tags: NotRequired[Dict[str, str]]
    visibilityEndTime: NotRequired[datetime]
    visibilityStartTime: NotRequired[datetime]

class ListContactsRequestTypeDef(TypedDict):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef
    statusList: Sequence[ContactStatusType]
    groundStation: NotRequired[str]
    maxResults: NotRequired[int]
    missionProfileArn: NotRequired[str]
    nextToken: NotRequired[str]
    satelliteArn: NotRequired[str]

class ListEphemeridesRequestTypeDef(TypedDict):
    endTime: TimestampTypeDef
    satelliteId: str
    startTime: TimestampTypeDef
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    statusList: NotRequired[Sequence[EphemerisStatusType]]

class ReserveContactRequestTypeDef(TypedDict):
    endTime: TimestampTypeDef
    groundStation: str
    missionProfileArn: str
    satelliteArn: str
    startTime: TimestampTypeDef
    tags: NotRequired[Mapping[str, str]]

class TimeRangeTypeDef(TypedDict):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef

class CreateMissionProfileRequestTypeDef(TypedDict):
    dataflowEdges: Sequence[Sequence[str]]
    minimumViableContactDurationSeconds: int
    name: str
    trackingConfigArn: str
    contactPostPassDurationSeconds: NotRequired[int]
    contactPrePassDurationSeconds: NotRequired[int]
    streamsKmsKey: NotRequired[KmsKeyTypeDef]
    streamsKmsRole: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class GetMissionProfileResponseTypeDef(TypedDict):
    contactPostPassDurationSeconds: int
    contactPrePassDurationSeconds: int
    dataflowEdges: List[List[str]]
    minimumViableContactDurationSeconds: int
    missionProfileArn: str
    missionProfileId: str
    name: str
    region: str
    streamsKmsKey: KmsKeyTypeDef
    streamsKmsRole: str
    tags: Dict[str, str]
    trackingConfigArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMissionProfileRequestTypeDef(TypedDict):
    missionProfileId: str
    contactPostPassDurationSeconds: NotRequired[int]
    contactPrePassDurationSeconds: NotRequired[int]
    dataflowEdges: NotRequired[Sequence[Sequence[str]]]
    minimumViableContactDurationSeconds: NotRequired[int]
    name: NotRequired[str]
    streamsKmsKey: NotRequired[KmsKeyTypeDef]
    streamsKmsRole: NotRequired[str]
    trackingConfigArn: NotRequired[str]

class ListDataflowEndpointGroupsResponseTypeDef(TypedDict):
    dataflowEndpointGroupList: List[DataflowEndpointListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeContactRequestWaitTypeDef(TypedDict):
    contactId: str
    WaiterConfig: NotRequired[WaiterConfigTypeDef]

class EphemerisDescriptionTypeDef(TypedDict):
    ephemerisData: NotRequired[str]
    sourceS3Object: NotRequired[S3ObjectTypeDef]

class EphemerisItemTypeDef(TypedDict):
    creationTime: NotRequired[datetime]
    enabled: NotRequired[bool]
    ephemerisId: NotRequired[str]
    name: NotRequired[str]
    priority: NotRequired[int]
    sourceS3Object: NotRequired[S3ObjectTypeDef]
    status: NotRequired[EphemerisStatusType]

class OEMEphemerisTypeDef(TypedDict):
    oemData: NotRequired[str]
    s3Object: NotRequired[S3ObjectTypeDef]

class GetSatelliteResponseTypeDef(TypedDict):
    currentEphemeris: EphemerisMetaDataTypeDef
    groundStations: List[str]
    noradSatelliteID: int
    satelliteArn: str
    satelliteId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SatelliteListItemTypeDef(TypedDict):
    currentEphemeris: NotRequired[EphemerisMetaDataTypeDef]
    groundStations: NotRequired[List[str]]
    noradSatelliteID: NotRequired[int]
    satelliteArn: NotRequired[str]
    satelliteId: NotRequired[str]

class SpectrumConfigTypeDef(TypedDict):
    bandwidth: FrequencyBandwidthTypeDef
    centerFrequency: FrequencyTypeDef
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

class ListContactsRequestPaginateTypeDef(TypedDict):
    endTime: TimestampTypeDef
    startTime: TimestampTypeDef
    statusList: Sequence[ContactStatusType]
    groundStation: NotRequired[str]
    missionProfileArn: NotRequired[str]
    satelliteArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDataflowEndpointGroupsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListEphemeridesRequestPaginateTypeDef(TypedDict):
    endTime: TimestampTypeDef
    satelliteId: str
    startTime: TimestampTypeDef
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
    agentDetails: AgentDetailsTypeDef
    discoveryData: DiscoveryDataTypeDef
    tags: NotRequired[Mapping[str, str]]

class ListContactsResponseTypeDef(TypedDict):
    contactList: List[ContactDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class TLEDataTypeDef(TypedDict):
    tleLine1: str
    tleLine2: str
    validTimeRange: TimeRangeTypeDef

class EphemerisTypeDescriptionTypeDef(TypedDict):
    oem: NotRequired[EphemerisDescriptionTypeDef]
    tle: NotRequired[EphemerisDescriptionTypeDef]

class ListEphemeridesResponseTypeDef(TypedDict):
    ephemerides: List[EphemerisItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSatellitesResponseTypeDef(TypedDict):
    satellites: List[SatelliteListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class AntennaDownlinkConfigTypeDef(TypedDict):
    spectrumConfig: SpectrumConfigTypeDef

class AntennaDownlinkDemodDecodeConfigTypeDef(TypedDict):
    decodeConfig: DecodeConfigTypeDef
    demodulationConfig: DemodulationConfigTypeDef
    spectrumConfig: SpectrumConfigTypeDef

class AntennaUplinkConfigTypeDef(TypedDict):
    spectrumConfig: UplinkSpectrumConfigTypeDef
    targetEirp: EirpTypeDef
    transmitDisabled: NotRequired[bool]

class RangedConnectionDetailsTypeDef(TypedDict):
    socketAddress: RangedSocketAddressTypeDef
    mtu: NotRequired[int]

class TLEEphemerisTypeDef(TypedDict):
    s3Object: NotRequired[S3ObjectTypeDef]
    tleData: NotRequired[Sequence[TLEDataTypeDef]]

class DescribeEphemerisResponseTypeDef(TypedDict):
    creationTime: datetime
    enabled: bool
    ephemerisId: str
    invalidReason: EphemerisInvalidReasonType
    name: str
    priority: int
    satelliteId: str
    status: EphemerisStatusType
    suppliedData: EphemerisTypeDescriptionTypeDef
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfigTypeDataTypeDef(TypedDict):
    antennaDownlinkConfig: NotRequired[AntennaDownlinkConfigTypeDef]
    antennaDownlinkDemodDecodeConfig: NotRequired[AntennaDownlinkDemodDecodeConfigTypeDef]
    antennaUplinkConfig: NotRequired[AntennaUplinkConfigTypeDef]
    dataflowEndpointConfig: NotRequired[DataflowEndpointConfigTypeDef]
    s3RecordingConfig: NotRequired[S3RecordingConfigTypeDef]
    trackingConfig: NotRequired[TrackingConfigTypeDef]
    uplinkEchoConfig: NotRequired[UplinkEchoConfigTypeDef]

class AwsGroundStationAgentEndpointTypeDef(TypedDict):
    egressAddress: ConnectionDetailsTypeDef
    ingressAddress: RangedConnectionDetailsTypeDef
    name: str
    agentStatus: NotRequired[AgentStatusType]
    auditResults: NotRequired[AuditResultsType]

class EphemerisDataTypeDef(TypedDict):
    oem: NotRequired[OEMEphemerisTypeDef]
    tle: NotRequired[TLEEphemerisTypeDef]

class CreateConfigRequestTypeDef(TypedDict):
    configData: ConfigTypeDataTypeDef
    name: str
    tags: NotRequired[Mapping[str, str]]

class GetConfigResponseTypeDef(TypedDict):
    configArn: str
    configData: ConfigTypeDataTypeDef
    configId: str
    configType: ConfigCapabilityTypeType
    name: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfigRequestTypeDef(TypedDict):
    configData: ConfigTypeDataTypeDef
    configId: str
    configType: ConfigCapabilityTypeType
    name: str

class EndpointDetailsOutputTypeDef(TypedDict):
    awsGroundStationAgentEndpoint: NotRequired[AwsGroundStationAgentEndpointTypeDef]
    endpoint: NotRequired[DataflowEndpointTypeDef]
    healthReasons: NotRequired[List[CapabilityHealthReasonType]]
    healthStatus: NotRequired[CapabilityHealthType]
    securityDetails: NotRequired[SecurityDetailsOutputTypeDef]

class EndpointDetailsTypeDef(TypedDict):
    awsGroundStationAgentEndpoint: NotRequired[AwsGroundStationAgentEndpointTypeDef]
    endpoint: NotRequired[DataflowEndpointTypeDef]
    healthReasons: NotRequired[Sequence[CapabilityHealthReasonType]]
    healthStatus: NotRequired[CapabilityHealthType]
    securityDetails: NotRequired[SecurityDetailsUnionTypeDef]

class CreateEphemerisRequestTypeDef(TypedDict):
    name: str
    satelliteId: str
    enabled: NotRequired[bool]
    ephemeris: NotRequired[EphemerisDataTypeDef]
    expirationTime: NotRequired[TimestampTypeDef]
    kmsKeyArn: NotRequired[str]
    priority: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]

class ConfigDetailsTypeDef(TypedDict):
    antennaDemodDecodeDetails: NotRequired[AntennaDemodDecodeDetailsTypeDef]
    endpointDetails: NotRequired[EndpointDetailsOutputTypeDef]
    s3RecordingDetails: NotRequired[S3RecordingDetailsTypeDef]

class GetDataflowEndpointGroupResponseTypeDef(TypedDict):
    contactPostPassDurationSeconds: int
    contactPrePassDurationSeconds: int
    dataflowEndpointGroupArn: str
    dataflowEndpointGroupId: str
    endpointsDetails: List[EndpointDetailsOutputTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

EndpointDetailsUnionTypeDef = Union[EndpointDetailsTypeDef, EndpointDetailsOutputTypeDef]

class DestinationTypeDef(TypedDict):
    configDetails: NotRequired[ConfigDetailsTypeDef]
    configId: NotRequired[str]
    configType: NotRequired[ConfigCapabilityTypeType]
    dataflowDestinationRegion: NotRequired[str]

class SourceTypeDef(TypedDict):
    configDetails: NotRequired[ConfigDetailsTypeDef]
    configId: NotRequired[str]
    configType: NotRequired[ConfigCapabilityTypeType]
    dataflowSourceRegion: NotRequired[str]

class CreateDataflowEndpointGroupRequestTypeDef(TypedDict):
    endpointDetails: Sequence[EndpointDetailsUnionTypeDef]
    contactPostPassDurationSeconds: NotRequired[int]
    contactPrePassDurationSeconds: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]

class DataflowDetailTypeDef(TypedDict):
    destination: NotRequired[DestinationTypeDef]
    errorMessage: NotRequired[str]
    source: NotRequired[SourceTypeDef]

class DescribeContactResponseTypeDef(TypedDict):
    contactId: str
    contactStatus: ContactStatusType
    dataflowList: List[DataflowDetailTypeDef]
    endTime: datetime
    errorMessage: str
    groundStation: str
    maximumElevation: ElevationTypeDef
    missionProfileArn: str
    postPassEndTime: datetime
    prePassStartTime: datetime
    region: str
    satelliteArn: str
    startTime: datetime
    tags: Dict[str, str]
    visibilityEndTime: datetime
    visibilityStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
