"""
Type annotations for discovery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_discovery.type_defs import AgentConfigurationStatusTypeDef

    data: AgentConfigurationStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Union

from .literals import (
    AgentStatusType,
    BatchDeleteConfigurationTaskStatusType,
    BatchDeleteImportDataErrorCodeType,
    ConfigurationItemTypeType,
    ContinuousExportStatusType,
    DeleteAgentErrorCodeType,
    ExportStatusType,
    ImportStatusType,
    ImportTaskFilterNameType,
    OfferingClassType,
    PurchasingOptionType,
    TenancyType,
    TermLengthType,
    orderStringType,
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
    "AgentConfigurationStatusTypeDef",
    "AgentInfoTypeDef",
    "AgentNetworkInfoTypeDef",
    "AssociateConfigurationItemsToApplicationRequestRequestTypeDef",
    "BatchDeleteAgentErrorTypeDef",
    "BatchDeleteAgentsRequestRequestTypeDef",
    "BatchDeleteAgentsResponseTypeDef",
    "BatchDeleteConfigurationTaskTypeDef",
    "BatchDeleteImportDataErrorTypeDef",
    "BatchDeleteImportDataRequestRequestTypeDef",
    "BatchDeleteImportDataResponseTypeDef",
    "ConfigurationTagTypeDef",
    "ContinuousExportDescriptionTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CustomerAgentInfoTypeDef",
    "CustomerAgentlessCollectorInfoTypeDef",
    "CustomerConnectorInfoTypeDef",
    "CustomerMeCollectorInfoTypeDef",
    "DeleteAgentTypeDef",
    "DeleteApplicationsRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeletionWarningTypeDef",
    "DescribeAgentsRequestRequestTypeDef",
    "DescribeAgentsResponseTypeDef",
    "DescribeBatchDeleteConfigurationTaskRequestRequestTypeDef",
    "DescribeBatchDeleteConfigurationTaskResponseTypeDef",
    "DescribeConfigurationsRequestRequestTypeDef",
    "DescribeConfigurationsResponseTypeDef",
    "DescribeContinuousExportsRequestRequestTypeDef",
    "DescribeContinuousExportsResponseTypeDef",
    "DescribeExportConfigurationsRequestRequestTypeDef",
    "DescribeExportConfigurationsResponseTypeDef",
    "DescribeExportTasksRequestRequestTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeImportTasksRequestRequestTypeDef",
    "DescribeImportTasksResponseTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef",
    "Ec2RecommendationsExportPreferencesTypeDef",
    "ExportConfigurationsResponseTypeDef",
    "ExportFilterTypeDef",
    "ExportInfoTypeDef",
    "ExportPreferencesTypeDef",
    "FailedConfigurationTypeDef",
    "FilterTypeDef",
    "GetDiscoverySummaryResponseTypeDef",
    "ImportTaskFilterTypeDef",
    "ImportTaskTypeDef",
    "ListConfigurationsRequestRequestTypeDef",
    "ListConfigurationsResponseTypeDef",
    "ListServerNeighborsRequestRequestTypeDef",
    "ListServerNeighborsResponseTypeDef",
    "NeighborConnectionDetailTypeDef",
    "OrderByElementTypeDef",
    "PaginatorConfigTypeDef",
    "ReservedInstanceOptionsTypeDef",
    "ResponseMetadataTypeDef",
    "StartBatchDeleteConfigurationTaskRequestRequestTypeDef",
    "StartBatchDeleteConfigurationTaskResponseTypeDef",
    "StartContinuousExportResponseTypeDef",
    "StartDataCollectionByAgentIdsRequestRequestTypeDef",
    "StartDataCollectionByAgentIdsResponseTypeDef",
    "StartExportTaskRequestRequestTypeDef",
    "StartExportTaskResponseTypeDef",
    "StartImportTaskRequestRequestTypeDef",
    "StartImportTaskResponseTypeDef",
    "StopContinuousExportRequestRequestTypeDef",
    "StopContinuousExportResponseTypeDef",
    "StopDataCollectionByAgentIdsRequestRequestTypeDef",
    "StopDataCollectionByAgentIdsResponseTypeDef",
    "TagFilterTypeDef",
    "TagTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UsageMetricBasisTypeDef",
)

AgentConfigurationStatusTypeDef = TypedDict(
    "AgentConfigurationStatusTypeDef",
    {
        "agentId": str,
        "operationSucceeded": bool,
        "description": str,
    },
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
        "health": AgentStatusType,
        "lastHealthPingTime": str,
        "collectionStatus": str,
        "agentType": str,
        "registeredTime": str,
    },
    total=False,
)

AgentNetworkInfoTypeDef = TypedDict(
    "AgentNetworkInfoTypeDef",
    {
        "ipAddress": str,
        "macAddress": str,
    },
    total=False,
)

AssociateConfigurationItemsToApplicationRequestRequestTypeDef = TypedDict(
    "AssociateConfigurationItemsToApplicationRequestRequestTypeDef",
    {
        "applicationConfigurationId": str,
        "configurationIds": List[str],
    },
)

BatchDeleteAgentErrorTypeDef = TypedDict(
    "BatchDeleteAgentErrorTypeDef",
    {
        "agentId": str,
        "errorMessage": str,
        "errorCode": DeleteAgentErrorCodeType,
    },
)

BatchDeleteAgentsRequestRequestTypeDef = TypedDict(
    "BatchDeleteAgentsRequestRequestTypeDef",
    {
        "deleteAgents": List["DeleteAgentTypeDef"],
    },
)

BatchDeleteAgentsResponseTypeDef = TypedDict(
    "BatchDeleteAgentsResponseTypeDef",
    {
        "errors": List["BatchDeleteAgentErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteConfigurationTaskTypeDef = TypedDict(
    "BatchDeleteConfigurationTaskTypeDef",
    {
        "taskId": str,
        "status": BatchDeleteConfigurationTaskStatusType,
        "startTime": datetime,
        "endTime": datetime,
        "configurationType": Literal["SERVER"],
        "requestedConfigurations": List[str],
        "deletedConfigurations": List[str],
        "failedConfigurations": List["FailedConfigurationTypeDef"],
        "deletionWarnings": List["DeletionWarningTypeDef"],
    },
    total=False,
)

BatchDeleteImportDataErrorTypeDef = TypedDict(
    "BatchDeleteImportDataErrorTypeDef",
    {
        "importTaskId": str,
        "errorCode": BatchDeleteImportDataErrorCodeType,
        "errorDescription": str,
    },
    total=False,
)

_RequiredBatchDeleteImportDataRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteImportDataRequestRequestTypeDef",
    {
        "importTaskIds": List[str],
    },
)
_OptionalBatchDeleteImportDataRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteImportDataRequestRequestTypeDef",
    {
        "deleteHistory": bool,
    },
    total=False,
)

class BatchDeleteImportDataRequestRequestTypeDef(
    _RequiredBatchDeleteImportDataRequestRequestTypeDef,
    _OptionalBatchDeleteImportDataRequestRequestTypeDef,
):
    pass

BatchDeleteImportDataResponseTypeDef = TypedDict(
    "BatchDeleteImportDataResponseTypeDef",
    {
        "errors": List["BatchDeleteImportDataErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConfigurationTagTypeDef = TypedDict(
    "ConfigurationTagTypeDef",
    {
        "configurationType": ConfigurationItemTypeType,
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
        "status": ContinuousExportStatusType,
        "statusDetail": str,
        "s3Bucket": str,
        "startTime": datetime,
        "stopTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
    },
    total=False,
)

_RequiredCreateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateApplicationRequestRequestTypeDef",
    {
        "name": str,
    },
)
_OptionalCreateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateApplicationRequestRequestTypeDef",
    {
        "description": str,
    },
    total=False,
)

class CreateApplicationRequestRequestTypeDef(
    _RequiredCreateApplicationRequestRequestTypeDef, _OptionalCreateApplicationRequestRequestTypeDef
):
    pass

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "configurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "configurationIds": List[str],
        "tags": List["TagTypeDef"],
    },
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

CustomerAgentlessCollectorInfoTypeDef = TypedDict(
    "CustomerAgentlessCollectorInfoTypeDef",
    {
        "activeAgentlessCollectors": int,
        "healthyAgentlessCollectors": int,
        "denyListedAgentlessCollectors": int,
        "shutdownAgentlessCollectors": int,
        "unhealthyAgentlessCollectors": int,
        "totalAgentlessCollectors": int,
        "unknownAgentlessCollectors": int,
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

CustomerMeCollectorInfoTypeDef = TypedDict(
    "CustomerMeCollectorInfoTypeDef",
    {
        "activeMeCollectors": int,
        "healthyMeCollectors": int,
        "denyListedMeCollectors": int,
        "shutdownMeCollectors": int,
        "unhealthyMeCollectors": int,
        "totalMeCollectors": int,
        "unknownMeCollectors": int,
    },
)

_RequiredDeleteAgentTypeDef = TypedDict(
    "_RequiredDeleteAgentTypeDef",
    {
        "agentId": str,
    },
)
_OptionalDeleteAgentTypeDef = TypedDict(
    "_OptionalDeleteAgentTypeDef",
    {
        "force": bool,
    },
    total=False,
)

class DeleteAgentTypeDef(_RequiredDeleteAgentTypeDef, _OptionalDeleteAgentTypeDef):
    pass

DeleteApplicationsRequestRequestTypeDef = TypedDict(
    "DeleteApplicationsRequestRequestTypeDef",
    {
        "configurationIds": List[str],
    },
)

_RequiredDeleteTagsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTagsRequestRequestTypeDef",
    {
        "configurationIds": List[str],
    },
)
_OptionalDeleteTagsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTagsRequestRequestTypeDef",
    {
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class DeleteTagsRequestRequestTypeDef(
    _RequiredDeleteTagsRequestRequestTypeDef, _OptionalDeleteTagsRequestRequestTypeDef
):
    pass

DeletionWarningTypeDef = TypedDict(
    "DeletionWarningTypeDef",
    {
        "configurationId": str,
        "warningCode": int,
        "warningText": str,
    },
    total=False,
)

DescribeAgentsRequestRequestTypeDef = TypedDict(
    "DescribeAgentsRequestRequestTypeDef",
    {
        "agentIds": List[str],
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeAgentsResponseTypeDef = TypedDict(
    "DescribeAgentsResponseTypeDef",
    {
        "agentsInfo": List["AgentInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchDeleteConfigurationTaskRequestRequestTypeDef = TypedDict(
    "DescribeBatchDeleteConfigurationTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

DescribeBatchDeleteConfigurationTaskResponseTypeDef = TypedDict(
    "DescribeBatchDeleteConfigurationTaskResponseTypeDef",
    {
        "task": "BatchDeleteConfigurationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeConfigurationsRequestRequestTypeDef",
    {
        "configurationIds": List[str],
    },
)

DescribeConfigurationsResponseTypeDef = TypedDict(
    "DescribeConfigurationsResponseTypeDef",
    {
        "configurations": List[Dict[str, str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeContinuousExportsRequestRequestTypeDef = TypedDict(
    "DescribeContinuousExportsRequestRequestTypeDef",
    {
        "exportIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeContinuousExportsResponseTypeDef = TypedDict(
    "DescribeContinuousExportsResponseTypeDef",
    {
        "descriptions": List["ContinuousExportDescriptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeExportConfigurationsRequestRequestTypeDef",
    {
        "exportIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeExportConfigurationsResponseTypeDef = TypedDict(
    "DescribeExportConfigurationsResponseTypeDef",
    {
        "exportsInfo": List["ExportInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestRequestTypeDef",
    {
        "exportIds": List[str],
        "filters": List["ExportFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {
        "exportsInfo": List["ExportInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportTasksRequestRequestTypeDef",
    {
        "filters": List["ImportTaskFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeImportTasksResponseTypeDef = TypedDict(
    "DescribeImportTasksResponseTypeDef",
    {
        "nextToken": str,
        "tasks": List["ImportTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "filters": List["TagFilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeTagsResponseTypeDef = TypedDict(
    "DescribeTagsResponseTypeDef",
    {
        "tags": List["ConfigurationTagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef = TypedDict(
    "DisassociateConfigurationItemsFromApplicationRequestRequestTypeDef",
    {
        "applicationConfigurationId": str,
        "configurationIds": List[str],
    },
)

Ec2RecommendationsExportPreferencesTypeDef = TypedDict(
    "Ec2RecommendationsExportPreferencesTypeDef",
    {
        "enabled": bool,
        "cpuPerformanceMetricBasis": "UsageMetricBasisTypeDef",
        "ramPerformanceMetricBasis": "UsageMetricBasisTypeDef",
        "tenancy": TenancyType,
        "excludedInstanceTypes": List[str],
        "preferredRegion": str,
        "reservedInstanceOptions": "ReservedInstanceOptionsTypeDef",
    },
    total=False,
)

ExportConfigurationsResponseTypeDef = TypedDict(
    "ExportConfigurationsResponseTypeDef",
    {
        "exportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportFilterTypeDef = TypedDict(
    "ExportFilterTypeDef",
    {
        "name": str,
        "values": List[str],
        "condition": str,
    },
)

_RequiredExportInfoTypeDef = TypedDict(
    "_RequiredExportInfoTypeDef",
    {
        "exportId": str,
        "exportStatus": ExportStatusType,
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

ExportPreferencesTypeDef = TypedDict(
    "ExportPreferencesTypeDef",
    {
        "ec2RecommendationsPreferences": "Ec2RecommendationsExportPreferencesTypeDef",
    },
    total=False,
)

FailedConfigurationTypeDef = TypedDict(
    "FailedConfigurationTypeDef",
    {
        "configurationId": str,
        "errorStatusCode": int,
        "errorMessage": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "name": str,
        "values": List[str],
        "condition": str,
    },
)

GetDiscoverySummaryResponseTypeDef = TypedDict(
    "GetDiscoverySummaryResponseTypeDef",
    {
        "servers": int,
        "applications": int,
        "serversMappedToApplications": int,
        "serversMappedtoTags": int,
        "agentSummary": "CustomerAgentInfoTypeDef",
        "connectorSummary": "CustomerConnectorInfoTypeDef",
        "meCollectorSummary": "CustomerMeCollectorInfoTypeDef",
        "agentlessCollectorSummary": "CustomerAgentlessCollectorInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportTaskFilterTypeDef = TypedDict(
    "ImportTaskFilterTypeDef",
    {
        "name": ImportTaskFilterNameType,
        "values": List[str],
    },
    total=False,
)

ImportTaskTypeDef = TypedDict(
    "ImportTaskTypeDef",
    {
        "importTaskId": str,
        "clientRequestToken": str,
        "name": str,
        "importUrl": str,
        "status": ImportStatusType,
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

_RequiredListConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredListConfigurationsRequestRequestTypeDef",
    {
        "configurationType": ConfigurationItemTypeType,
    },
)
_OptionalListConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalListConfigurationsRequestRequestTypeDef",
    {
        "filters": List["FilterTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "orderBy": List["OrderByElementTypeDef"],
    },
    total=False,
)

class ListConfigurationsRequestRequestTypeDef(
    _RequiredListConfigurationsRequestRequestTypeDef,
    _OptionalListConfigurationsRequestRequestTypeDef,
):
    pass

ListConfigurationsResponseTypeDef = TypedDict(
    "ListConfigurationsResponseTypeDef",
    {
        "configurations": List[Dict[str, str]],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListServerNeighborsRequestRequestTypeDef = TypedDict(
    "_RequiredListServerNeighborsRequestRequestTypeDef",
    {
        "configurationId": str,
    },
)
_OptionalListServerNeighborsRequestRequestTypeDef = TypedDict(
    "_OptionalListServerNeighborsRequestRequestTypeDef",
    {
        "portInformationNeeded": bool,
        "neighborConfigurationIds": List[str],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListServerNeighborsRequestRequestTypeDef(
    _RequiredListServerNeighborsRequestRequestTypeDef,
    _OptionalListServerNeighborsRequestRequestTypeDef,
):
    pass

ListServerNeighborsResponseTypeDef = TypedDict(
    "ListServerNeighborsResponseTypeDef",
    {
        "neighbors": List["NeighborConnectionDetailTypeDef"],
        "nextToken": str,
        "knownDependencyCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredNeighborConnectionDetailTypeDef = TypedDict(
    "_RequiredNeighborConnectionDetailTypeDef",
    {
        "sourceServerId": str,
        "destinationServerId": str,
        "connectionsCount": int,
    },
)
_OptionalNeighborConnectionDetailTypeDef = TypedDict(
    "_OptionalNeighborConnectionDetailTypeDef",
    {
        "destinationPort": int,
        "transportProtocol": str,
    },
    total=False,
)

class NeighborConnectionDetailTypeDef(
    _RequiredNeighborConnectionDetailTypeDef, _OptionalNeighborConnectionDetailTypeDef
):
    pass

_RequiredOrderByElementTypeDef = TypedDict(
    "_RequiredOrderByElementTypeDef",
    {
        "fieldName": str,
    },
)
_OptionalOrderByElementTypeDef = TypedDict(
    "_OptionalOrderByElementTypeDef",
    {
        "sortOrder": orderStringType,
    },
    total=False,
)

class OrderByElementTypeDef(_RequiredOrderByElementTypeDef, _OptionalOrderByElementTypeDef):
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

ReservedInstanceOptionsTypeDef = TypedDict(
    "ReservedInstanceOptionsTypeDef",
    {
        "purchasingOption": PurchasingOptionType,
        "offeringClass": OfferingClassType,
        "termLength": TermLengthType,
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

StartBatchDeleteConfigurationTaskRequestRequestTypeDef = TypedDict(
    "StartBatchDeleteConfigurationTaskRequestRequestTypeDef",
    {
        "configurationType": Literal["SERVER"],
        "configurationIds": List[str],
    },
)

StartBatchDeleteConfigurationTaskResponseTypeDef = TypedDict(
    "StartBatchDeleteConfigurationTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartContinuousExportResponseTypeDef = TypedDict(
    "StartContinuousExportResponseTypeDef",
    {
        "exportId": str,
        "s3Bucket": str,
        "startTime": datetime,
        "dataSource": Literal["AGENT"],
        "schemaStorageConfig": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDataCollectionByAgentIdsRequestRequestTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsRequestRequestTypeDef",
    {
        "agentIds": List[str],
    },
)

StartDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "StartDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List["AgentConfigurationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartExportTaskRequestRequestTypeDef = TypedDict(
    "StartExportTaskRequestRequestTypeDef",
    {
        "exportDataFormat": List[Literal["CSV"]],
        "filters": List["ExportFilterTypeDef"],
        "startTime": Union[datetime, str],
        "endTime": Union[datetime, str],
        "preferences": "ExportPreferencesTypeDef",
    },
    total=False,
)

StartExportTaskResponseTypeDef = TypedDict(
    "StartExportTaskResponseTypeDef",
    {
        "exportId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartImportTaskRequestRequestTypeDef = TypedDict(
    "_RequiredStartImportTaskRequestRequestTypeDef",
    {
        "name": str,
        "importUrl": str,
    },
)
_OptionalStartImportTaskRequestRequestTypeDef = TypedDict(
    "_OptionalStartImportTaskRequestRequestTypeDef",
    {
        "clientRequestToken": str,
    },
    total=False,
)

class StartImportTaskRequestRequestTypeDef(
    _RequiredStartImportTaskRequestRequestTypeDef, _OptionalStartImportTaskRequestRequestTypeDef
):
    pass

StartImportTaskResponseTypeDef = TypedDict(
    "StartImportTaskResponseTypeDef",
    {
        "task": "ImportTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopContinuousExportRequestRequestTypeDef = TypedDict(
    "StopContinuousExportRequestRequestTypeDef",
    {
        "exportId": str,
    },
)

StopContinuousExportResponseTypeDef = TypedDict(
    "StopContinuousExportResponseTypeDef",
    {
        "startTime": datetime,
        "stopTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDataCollectionByAgentIdsRequestRequestTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsRequestRequestTypeDef",
    {
        "agentIds": List[str],
    },
)

StopDataCollectionByAgentIdsResponseTypeDef = TypedDict(
    "StopDataCollectionByAgentIdsResponseTypeDef",
    {
        "agentsConfigurationStatus": List["AgentConfigurationStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "name": str,
        "values": List[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

_RequiredUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateApplicationRequestRequestTypeDef",
    {
        "configurationId": str,
    },
)
_OptionalUpdateApplicationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)

class UpdateApplicationRequestRequestTypeDef(
    _RequiredUpdateApplicationRequestRequestTypeDef, _OptionalUpdateApplicationRequestRequestTypeDef
):
    pass

UsageMetricBasisTypeDef = TypedDict(
    "UsageMetricBasisTypeDef",
    {
        "name": str,
        "percentageAdjust": float,
    },
    total=False,
)
