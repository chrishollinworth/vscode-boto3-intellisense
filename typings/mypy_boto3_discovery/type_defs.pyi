"""
Main interface for discovery service type definitions.

Usage::

    ```python
    from mypy_boto3_discovery.type_defs import AgentConfigurationStatusTypeDef

    data: AgentConfigurationStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AgentConfigurationStatusTypeDef",
    "AgentInfoTypeDef",
    "AgentNetworkInfoTypeDef",
    "BatchDeleteImportDataErrorTypeDef",
    "ConfigurationTagTypeDef",
    "ContinuousExportDescriptionTypeDef",
    "CustomerAgentInfoTypeDef",
    "CustomerConnectorInfoTypeDef",
    "ExportInfoTypeDef",
    "ImportTaskTypeDef",
    "NeighborConnectionDetailTypeDef",
    "BatchDeleteImportDataResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "DescribeAgentsResponseTypeDef",
    "DescribeConfigurationsResponseTypeDef",
    "DescribeContinuousExportsResponseTypeDef",
    "DescribeExportConfigurationsResponseTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeImportTasksResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "ExportConfigurationsResponseTypeDef",
    "ExportFilterTypeDef",
    "FilterTypeDef",
    "GetDiscoverySummaryResponseTypeDef",
    "ImportTaskFilterTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListServerNeighborsResponseTypeDef",
    "OrderByElementTypeDef",
    "PaginatorConfigTypeDef",
    "StartContinuousExportResponseTypeDef",
    "StartDataCollectionByAgentIdsResponseTypeDef",
    "StartExportTaskResponseTypeDef",
    "StartImportTaskResponseTypeDef",
    "StopContinuousExportResponseTypeDef",
    "StopDataCollectionByAgentIdsResponseTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
)

AgentConfigurationStatusTypeDef = TypedDict(
    "AgentConfigurationStatusTypeDef",
    {"agentId": str, "operationSucceeded": bool, "description": str},
    total=False,
)

AgentInfoTypeDef = TypedDict(
    "AgentInfoTypeDef",
    {
        "agentId": str,
        "hostName": str,
        "agentNetworkInfoList": List["AgentNetworkInfoTypeDef"],
        "connectorId": str,
        "version": str,
        "health": Literal["HEALTHY", "UNHEALTHY", "RUNNING", "UNKNOWN", "BLACKLISTED", "SHUTDOWN"],
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)

AgentNetworkInfoTypeDef = TypedDict(
    "AgentNetworkInfoTypeDef", {"ipAddress": str, "macAddress": str}, total=False
)

BatchDeleteImportDataErrorTypeDef = TypedDict(
    "BatchDeleteImportDataErrorTypeDef",
    {
        "importTaskId": str,
        "errorCode": Literal["NOT_FOUND", "INTERNAL_SERVER_ERROR", "OVER_LIMIT"],
        "errorDescription": str,
    },
    total=False,
)

ConfigurationTagTypeDef = TypedDict(
    "ConfigurationTagTypeDef",
    {
        "configurationType": Literal["SERVER", "PROCESS", "CONNECTION", "APPLICATION"],
        "configurationId": str,
        "key": str,
        "value": str,
        "timeOfCreation": datetime,
    },
    total=False,
)

ContinuousExportDescriptionTypeDef = TypedDict(
    "ContinuousExportDescriptionTypeDef",
    {
        "exportId": str,
        "status": Literal[
            "START_IN_PROGRESS",
            "START_FAILED",
            "ACTIVE",
            "ERROR",
            "STOP_IN_PROGRESS",
            "STOP_FAILED",
            "INACTIVE",
        ],
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

CustomerAgentInfoTypeDef = TypedDict(
    "CustomerAgentInfoTypeDef",
    {
        "activeAgents": int,
        "healthyAgents": int,
        "blackListedAgents": int,
        "shutdownAgents": int,
        "unhealthyAgents": int,
        "totalAgents": int,
        "unknownAgents": int,
    },
)

CustomerConnectorInfoTypeDef = TypedDict(
    "CustomerConnectorInfoTypeDef",
    {
        "activeConnectors": int,
        "healthyConnectors": int,
        "blackListedConnectors": int,
        "shutdownConnectors": int,
        "unhealthyConnectors": int,
        "totalConnectors": int,
        "unknownConnectors": int,
    },
)

_RequiredExportInfoTypeDef = TypedDict(
    "_RequiredExportInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": Literal["FAILED", "SUCCEEDED", "IN_PROGRESS"],
        "statusMessage": str,
        "exportRequestTime": datetime,
    },
)
_OptionalExportInfoTypeDef = TypedDict(
    "_OptionalExportInfoTypeDef",
    {
        "configurationsDownloadUrl": str,
        "isTruncated": bool,
        "requestedStartTime": datetime,
        "requestedEndTime": datetime,
    },
    total=False,
)


class ExportInfoTypeDef(_RequiredExportInfoTypeDef, _OptionalExportInfoTypeDef):
    pass


ImportTaskTypeDef = TypedDict(
    "ImportTaskTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": Literal[
            "IMPORT_IN_PROGRESS",
            "IMPORT_COMPLETE",
            "IMPORT_COMPLETE_WITH_ERRORS",
            "IMPORT_FAILED",
            "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
            "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
            "DELETE_IN_PROGRESS",
            "DELETE_COMPLETE",
            "DELETE_FAILED",
            "DELETE_FAILED_LIMIT_EXCEEDED",
            "INTERNAL_ERROR",
        ],
        "importRequestTime": datetime,
        "importCompletionTime": datetime,
        "importDeletedTime": datetime,
        "serverImportSuccess": int,
        "serverImportFailure": int,
        "applicationImportSuccess": int,
        "applicationImportFailure": int,
        "errorsAndFailedEntriesZip": str,
    },
    total=False,
)

_RequiredNeighborConnectionDetailTypeDef = TypedDict(
    "_RequiredNeighborConnectionDetailTypeDef",
    {"sourceServerId": str, "destinationServerId": str, "connectionsCount": int},
)
_OptionalNeighborConnectionDetailTypeDef = TypedDict(
    "_OptionalNeighborConnectionDetailTypeDef",
    {"destinationPort": int, "transportProtocol": str},
    total=False,
)


class NeighborConnectionDetailTypeDef(
    _RequiredNeighborConnectionDetailTypeDef, _OptionalNeighborConnectionDetailTypeDef
):
    pass


BatchDeleteImportDataResponseTypeDef = TypedDict(
    "BatchDeleteImportDataResponseTypeDef",
    {"errors": List["BatchDeleteImportDataErrorTypeDef"]},
    total=False,
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef", {"configurationId": str}, total=False
)

DescribeAgentsResponseTypeDef = TypedDict(
    "DescribeAgentsResponseTypeDef",
    {"agentsInfo": List["AgentInfoTypeDef"], "nextToken": str},
    total=False,
)

DescribeConfigurationsResponseTypeDef = TypedDict(
    "DescribeConfigurationsResponseTypeDef", {"configurations": List[Dict[str, str]]}, total=False
)

DescribeContinuousExportsResponseTypeDef = TypedDict(
    "DescribeContinuousExportsResponseTypeDef",
    {"descriptions": List["ContinuousExportDescriptionTypeDef"], "nextToken": str},
    total=False,
)

DescribeExportConfigurationsResponseTypeDef = TypedDict(
    "DescribeExportConfigurationsResponseTypeDef",
    {"exportsInfo": List["ExportInfoTypeDef"], "nextToken": str},
    total=False,
)

DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {"exportsInfo": List["ExportInfoTypeDef"], "nextToken": str},
    total=False,
)

DescribeImportTasksResponseTypeDef = TypedDict(
    "DescribeImportTasksResponseTypeDef",
    {"nextToken": str, "tasks": List["ImportTaskTypeDef"]},
    total=False,
)

DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {"tags": List["ConfigurationTagTypeDef"], "nextToken": str},
    total=False,
)

ExportConfigurationsResponseTypeDef = TypedDict(
    "ExportConfigurationsResponseTypeDef", {"exportId": str}, total=False
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef", {"name": str, "values": List[str], "condition": str}
)

FilterTypeDef = TypedDict("FilterTypeDef", {"name": str, "values": List[str], "condition": str})

GetDiscoverySummaryResponseTypeDef = TypedDict(
    "GetDiscoverySummaryResponseTypeDef",
    {
        "servers": int,
        "applications": int,
        "serversMappedToApplications": int,
        "serversMappedtoTags": int,
        "agentSummary": "CustomerAgentInfoTypeDef",
        "connectorSummary": "CustomerConnectorInfoTypeDef",
    },
    total=False,
)

ImportTaskFilterTypeDef = TypedDict(
    "ImportTaskFilterTypeDef",
    {"name": Literal["IMPORT_TASK_ID", "STATUS", "NAME"], "values": List[str]},
    total=False,
)

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {"configurations": List[Dict[str, str]], "nextToken": str},
    total=False,
)

_RequiredListServerNeighborsResponseTypeDef = TypedDict(
    "_RequiredListServerNeighborsResponseTypeDef",
    {"neighbors": List["NeighborConnectionDetailTypeDef"]},
)
_OptionalListServerNeighborsResponseTypeDef = TypedDict(
    "_OptionalListServerNeighborsResponseTypeDef",
    {"nextToken": str, "knownDependencyCount": int},
    total=False,
)


class ListServerNeighborsResponseTypeDef(
    _RequiredListServerNeighborsResponseTypeDef, _OptionalListServerNeighborsResponseTypeDef
):
    pass


_RequiredOrderByElementTypeDef = TypedDict("_RequiredOrderByElementTypeDef", {"fieldName": str})
_OptionalOrderByElementTypeDef = TypedDict(
    "_OptionalOrderByElementTypeDef", {"sortOrder": Literal["ASC", "DESC"]}, total=False
)


class OrderByElementTypeDef(_RequiredOrderByElementTypeDef, _OptionalOrderByElementTypeDef):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartContinuousExportResponseTypeDef = TypedDict(
    "StartContinuousExportResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

StartDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsResponseTypeDef",
    {"agentsConfigurationStatus": List["AgentConfigurationStatusTypeDef"]},
    total=False,
)

StartExportTaskResponseTypeDef = TypedDict(
    "StartExportTaskResponseTypeDef", {"exportId": str}, total=False
)

StartImportTaskResponseTypeDef = TypedDict(
    "StartImportTaskResponseTypeDef", {"task": "ImportTaskTypeDef"}, total=False
)

StopContinuousExportResponseTypeDef = TypedDict(
    "StopContinuousExportResponseTypeDef",
    {"startTime": datetime, "stopTime": datetime},
    total=False,
)

StopDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsResponseTypeDef",
    {"agentsConfigurationStatus": List["AgentConfigurationStatusTypeDef"]},
    total=False,
)

TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"name": str, "values": List[str]})

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str})
