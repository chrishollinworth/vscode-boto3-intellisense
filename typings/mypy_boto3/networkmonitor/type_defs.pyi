"""
Type annotations for networkmonitor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmonitor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_networkmonitor.type_defs import CreateMonitorInputRequestTypeDef

    data: CreateMonitorInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import AddressFamilyType, MonitorStateType, ProbeStateType, ProtocolType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateMonitorInputRequestTypeDef",
    "CreateMonitorOutputTypeDef",
    "CreateMonitorProbeInputTypeDef",
    "CreateProbeInputRequestTypeDef",
    "CreateProbeOutputTypeDef",
    "DeleteMonitorInputRequestTypeDef",
    "DeleteProbeInputRequestTypeDef",
    "GetMonitorInputRequestTypeDef",
    "GetMonitorOutputTypeDef",
    "GetProbeInputRequestTypeDef",
    "GetProbeOutputTypeDef",
    "ListMonitorsInputRequestTypeDef",
    "ListMonitorsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MonitorSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ProbeInputTypeDef",
    "ProbeTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateMonitorInputRequestTypeDef",
    "UpdateMonitorOutputTypeDef",
    "UpdateProbeInputRequestTypeDef",
    "UpdateProbeOutputTypeDef",
)

_RequiredCreateMonitorInputRequestTypeDef = TypedDict(
    "_RequiredCreateMonitorInputRequestTypeDef",
    {
        "monitorName": str,
    },
)
_OptionalCreateMonitorInputRequestTypeDef = TypedDict(
    "_OptionalCreateMonitorInputRequestTypeDef",
    {
        "probes": List["CreateMonitorProbeInputTypeDef"],
        "aggregationPeriod": int,
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateMonitorInputRequestTypeDef(
    _RequiredCreateMonitorInputRequestTypeDef, _OptionalCreateMonitorInputRequestTypeDef
):
    pass

CreateMonitorOutputTypeDef = TypedDict(
    "CreateMonitorOutputTypeDef",
    {
        "monitorArn": str,
        "monitorName": str,
        "state": MonitorStateType,
        "aggregationPeriod": int,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateMonitorProbeInputTypeDef = TypedDict(
    "_RequiredCreateMonitorProbeInputTypeDef",
    {
        "sourceArn": str,
        "destination": str,
        "protocol": ProtocolType,
    },
)
_OptionalCreateMonitorProbeInputTypeDef = TypedDict(
    "_OptionalCreateMonitorProbeInputTypeDef",
    {
        "destinationPort": int,
        "packetSize": int,
        "probeTags": Dict[str, str],
    },
    total=False,
)

class CreateMonitorProbeInputTypeDef(
    _RequiredCreateMonitorProbeInputTypeDef, _OptionalCreateMonitorProbeInputTypeDef
):
    pass

_RequiredCreateProbeInputRequestTypeDef = TypedDict(
    "_RequiredCreateProbeInputRequestTypeDef",
    {
        "monitorName": str,
        "probe": "ProbeInputTypeDef",
    },
)
_OptionalCreateProbeInputRequestTypeDef = TypedDict(
    "_OptionalCreateProbeInputRequestTypeDef",
    {
        "clientToken": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateProbeInputRequestTypeDef(
    _RequiredCreateProbeInputRequestTypeDef, _OptionalCreateProbeInputRequestTypeDef
):
    pass

CreateProbeOutputTypeDef = TypedDict(
    "CreateProbeOutputTypeDef",
    {
        "probeId": str,
        "probeArn": str,
        "sourceArn": str,
        "destination": str,
        "destinationPort": int,
        "protocol": ProtocolType,
        "packetSize": int,
        "addressFamily": AddressFamilyType,
        "vpcId": str,
        "state": ProbeStateType,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMonitorInputRequestTypeDef = TypedDict(
    "DeleteMonitorInputRequestTypeDef",
    {
        "monitorName": str,
    },
)

DeleteProbeInputRequestTypeDef = TypedDict(
    "DeleteProbeInputRequestTypeDef",
    {
        "monitorName": str,
        "probeId": str,
    },
)

GetMonitorInputRequestTypeDef = TypedDict(
    "GetMonitorInputRequestTypeDef",
    {
        "monitorName": str,
    },
)

GetMonitorOutputTypeDef = TypedDict(
    "GetMonitorOutputTypeDef",
    {
        "monitorArn": str,
        "monitorName": str,
        "state": MonitorStateType,
        "aggregationPeriod": int,
        "tags": Dict[str, str],
        "probes": List["ProbeTypeDef"],
        "createdAt": datetime,
        "modifiedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProbeInputRequestTypeDef = TypedDict(
    "GetProbeInputRequestTypeDef",
    {
        "monitorName": str,
        "probeId": str,
    },
)

GetProbeOutputTypeDef = TypedDict(
    "GetProbeOutputTypeDef",
    {
        "probeId": str,
        "probeArn": str,
        "sourceArn": str,
        "destination": str,
        "destinationPort": int,
        "protocol": ProtocolType,
        "packetSize": int,
        "addressFamily": AddressFamilyType,
        "vpcId": str,
        "state": ProbeStateType,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMonitorsInputRequestTypeDef = TypedDict(
    "ListMonitorsInputRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
        "state": str,
    },
    total=False,
)

ListMonitorsOutputTypeDef = TypedDict(
    "ListMonitorsOutputTypeDef",
    {
        "monitors": List["MonitorSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMonitorSummaryTypeDef = TypedDict(
    "_RequiredMonitorSummaryTypeDef",
    {
        "monitorArn": str,
        "monitorName": str,
        "state": MonitorStateType,
    },
)
_OptionalMonitorSummaryTypeDef = TypedDict(
    "_OptionalMonitorSummaryTypeDef",
    {
        "aggregationPeriod": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class MonitorSummaryTypeDef(_RequiredMonitorSummaryTypeDef, _OptionalMonitorSummaryTypeDef):
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

_RequiredProbeInputTypeDef = TypedDict(
    "_RequiredProbeInputTypeDef",
    {
        "sourceArn": str,
        "destination": str,
        "protocol": ProtocolType,
    },
)
_OptionalProbeInputTypeDef = TypedDict(
    "_OptionalProbeInputTypeDef",
    {
        "destinationPort": int,
        "packetSize": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class ProbeInputTypeDef(_RequiredProbeInputTypeDef, _OptionalProbeInputTypeDef):
    pass

_RequiredProbeTypeDef = TypedDict(
    "_RequiredProbeTypeDef",
    {
        "sourceArn": str,
        "destination": str,
        "protocol": ProtocolType,
    },
)
_OptionalProbeTypeDef = TypedDict(
    "_OptionalProbeTypeDef",
    {
        "probeId": str,
        "probeArn": str,
        "destinationPort": int,
        "packetSize": int,
        "addressFamily": AddressFamilyType,
        "vpcId": str,
        "state": ProbeStateType,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

class ProbeTypeDef(_RequiredProbeTypeDef, _OptionalProbeTypeDef):
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

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

UpdateMonitorInputRequestTypeDef = TypedDict(
    "UpdateMonitorInputRequestTypeDef",
    {
        "monitorName": str,
        "aggregationPeriod": int,
    },
)

UpdateMonitorOutputTypeDef = TypedDict(
    "UpdateMonitorOutputTypeDef",
    {
        "monitorArn": str,
        "monitorName": str,
        "state": MonitorStateType,
        "aggregationPeriod": int,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateProbeInputRequestTypeDef = TypedDict(
    "_RequiredUpdateProbeInputRequestTypeDef",
    {
        "monitorName": str,
        "probeId": str,
    },
)
_OptionalUpdateProbeInputRequestTypeDef = TypedDict(
    "_OptionalUpdateProbeInputRequestTypeDef",
    {
        "state": ProbeStateType,
        "destination": str,
        "destinationPort": int,
        "protocol": ProtocolType,
        "packetSize": int,
    },
    total=False,
)

class UpdateProbeInputRequestTypeDef(
    _RequiredUpdateProbeInputRequestTypeDef, _OptionalUpdateProbeInputRequestTypeDef
):
    pass

UpdateProbeOutputTypeDef = TypedDict(
    "UpdateProbeOutputTypeDef",
    {
        "probeId": str,
        "probeArn": str,
        "sourceArn": str,
        "destination": str,
        "destinationPort": int,
        "protocol": ProtocolType,
        "packetSize": int,
        "addressFamily": AddressFamilyType,
        "vpcId": str,
        "state": ProbeStateType,
        "createdAt": datetime,
        "modifiedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
