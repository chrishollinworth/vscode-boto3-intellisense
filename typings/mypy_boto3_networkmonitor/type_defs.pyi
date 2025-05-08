"""
Type annotations for networkmonitor service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_networkmonitor.type_defs import CreateMonitorProbeInputTypeDef

    data: CreateMonitorProbeInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import AddressFamilyType, MonitorStateType, ProbeStateType, ProtocolType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "CreateMonitorInputTypeDef",
    "CreateMonitorOutputTypeDef",
    "CreateMonitorProbeInputTypeDef",
    "CreateProbeInputTypeDef",
    "CreateProbeOutputTypeDef",
    "DeleteMonitorInputTypeDef",
    "DeleteProbeInputTypeDef",
    "GetMonitorInputTypeDef",
    "GetMonitorOutputTypeDef",
    "GetProbeInputTypeDef",
    "GetProbeOutputTypeDef",
    "ListMonitorsInputPaginateTypeDef",
    "ListMonitorsInputTypeDef",
    "ListMonitorsOutputTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MonitorSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ProbeInputTypeDef",
    "ProbeTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputTypeDef",
    "UntagResourceInputTypeDef",
    "UpdateMonitorInputTypeDef",
    "UpdateMonitorOutputTypeDef",
    "UpdateProbeInputTypeDef",
    "UpdateProbeOutputTypeDef",
)

class CreateMonitorProbeInputTypeDef(TypedDict):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    destinationPort: NotRequired[int]
    packetSize: NotRequired[int]
    probeTags: NotRequired[Mapping[str, str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class ProbeInputTypeDef(TypedDict):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    destinationPort: NotRequired[int]
    packetSize: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]

class DeleteMonitorInputTypeDef(TypedDict):
    monitorName: str

class DeleteProbeInputTypeDef(TypedDict):
    monitorName: str
    probeId: str

class GetMonitorInputTypeDef(TypedDict):
    monitorName: str

class ProbeTypeDef(TypedDict):
    sourceArn: str
    destination: str
    protocol: ProtocolType
    probeId: NotRequired[str]
    probeArn: NotRequired[str]
    destinationPort: NotRequired[int]
    packetSize: NotRequired[int]
    addressFamily: NotRequired[AddressFamilyType]
    vpcId: NotRequired[str]
    state: NotRequired[ProbeStateType]
    createdAt: NotRequired[datetime]
    modifiedAt: NotRequired[datetime]
    tags: NotRequired[Dict[str, str]]

class GetProbeInputTypeDef(TypedDict):
    monitorName: str
    probeId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListMonitorsInputTypeDef(TypedDict):
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]
    state: NotRequired[str]

class MonitorSummaryTypeDef(TypedDict):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: NotRequired[int]
    tags: NotRequired[Dict[str, str]]

class ListTagsForResourceInputTypeDef(TypedDict):
    resourceArn: str

class TagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceInputTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateMonitorInputTypeDef(TypedDict):
    monitorName: str
    aggregationPeriod: int

class UpdateProbeInputTypeDef(TypedDict):
    monitorName: str
    probeId: str
    state: NotRequired[ProbeStateType]
    destination: NotRequired[str]
    destinationPort: NotRequired[int]
    protocol: NotRequired[ProtocolType]
    packetSize: NotRequired[int]

class CreateMonitorInputTypeDef(TypedDict):
    monitorName: str
    probes: NotRequired[Sequence[CreateMonitorProbeInputTypeDef]]
    aggregationPeriod: NotRequired[int]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CreateMonitorOutputTypeDef(TypedDict):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProbeOutputTypeDef(TypedDict):
    probeId: str
    probeArn: str
    sourceArn: str
    destination: str
    destinationPort: int
    protocol: ProtocolType
    packetSize: int
    addressFamily: AddressFamilyType
    vpcId: str
    state: ProbeStateType
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetProbeOutputTypeDef(TypedDict):
    probeId: str
    probeArn: str
    sourceArn: str
    destination: str
    destinationPort: int
    protocol: ProtocolType
    packetSize: int
    addressFamily: AddressFamilyType
    vpcId: str
    state: ProbeStateType
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMonitorOutputTypeDef(TypedDict):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProbeOutputTypeDef(TypedDict):
    probeId: str
    probeArn: str
    sourceArn: str
    destination: str
    destinationPort: int
    protocol: ProtocolType
    packetSize: int
    addressFamily: AddressFamilyType
    vpcId: str
    state: ProbeStateType
    createdAt: datetime
    modifiedAt: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProbeInputTypeDef(TypedDict):
    monitorName: str
    probe: ProbeInputTypeDef
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class GetMonitorOutputTypeDef(TypedDict):
    monitorArn: str
    monitorName: str
    state: MonitorStateType
    aggregationPeriod: int
    tags: Dict[str, str]
    probes: List[ProbeTypeDef]
    createdAt: datetime
    modifiedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListMonitorsInputPaginateTypeDef(TypedDict):
    state: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListMonitorsOutputTypeDef(TypedDict):
    monitors: List[MonitorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
