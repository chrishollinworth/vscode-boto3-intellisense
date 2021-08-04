"""
Type annotations for logs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_logs.type_defs import AssociateKmsKeyRequestRequestTypeDef

    data: AssociateKmsKeyRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    DistributionType,
    ExportTaskStatusCodeType,
    OrderByType,
    QueryStatusType,
    StandardUnitType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateKmsKeyRequestRequestTypeDef",
    "CancelExportTaskRequestRequestTypeDef",
    "CreateExportTaskRequestRequestTypeDef",
    "CreateExportTaskResponseTypeDef",
    "CreateLogGroupRequestRequestTypeDef",
    "CreateLogStreamRequestRequestTypeDef",
    "DeleteDestinationRequestRequestTypeDef",
    "DeleteLogGroupRequestRequestTypeDef",
    "DeleteLogStreamRequestRequestTypeDef",
    "DeleteMetricFilterRequestRequestTypeDef",
    "DeleteQueryDefinitionRequestRequestTypeDef",
    "DeleteQueryDefinitionResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRetentionPolicyRequestRequestTypeDef",
    "DeleteSubscriptionFilterRequestRequestTypeDef",
    "DescribeDestinationsRequestRequestTypeDef",
    "DescribeDestinationsResponseTypeDef",
    "DescribeExportTasksRequestRequestTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeLogGroupsRequestRequestTypeDef",
    "DescribeLogGroupsResponseTypeDef",
    "DescribeLogStreamsRequestRequestTypeDef",
    "DescribeLogStreamsResponseTypeDef",
    "DescribeMetricFiltersRequestRequestTypeDef",
    "DescribeMetricFiltersResponseTypeDef",
    "DescribeQueriesRequestRequestTypeDef",
    "DescribeQueriesResponseTypeDef",
    "DescribeQueryDefinitionsRequestRequestTypeDef",
    "DescribeQueryDefinitionsResponseTypeDef",
    "DescribeResourcePoliciesRequestRequestTypeDef",
    "DescribeResourcePoliciesResponseTypeDef",
    "DescribeSubscriptionFiltersRequestRequestTypeDef",
    "DescribeSubscriptionFiltersResponseTypeDef",
    "DestinationTypeDef",
    "DisassociateKmsKeyRequestRequestTypeDef",
    "ExportTaskExecutionInfoTypeDef",
    "ExportTaskStatusTypeDef",
    "ExportTaskTypeDef",
    "FilterLogEventsRequestRequestTypeDef",
    "FilterLogEventsResponseTypeDef",
    "FilteredLogEventTypeDef",
    "GetLogEventsRequestRequestTypeDef",
    "GetLogEventsResponseTypeDef",
    "GetLogGroupFieldsRequestRequestTypeDef",
    "GetLogGroupFieldsResponseTypeDef",
    "GetLogRecordRequestRequestTypeDef",
    "GetLogRecordResponseTypeDef",
    "GetQueryResultsRequestRequestTypeDef",
    "GetQueryResultsResponseTypeDef",
    "InputLogEventTypeDef",
    "ListTagsLogGroupRequestRequestTypeDef",
    "ListTagsLogGroupResponseTypeDef",
    "LogGroupFieldTypeDef",
    "LogGroupTypeDef",
    "LogStreamTypeDef",
    "MetricFilterMatchRecordTypeDef",
    "MetricFilterTypeDef",
    "MetricTransformationTypeDef",
    "OutputLogEventTypeDef",
    "PaginatorConfigTypeDef",
    "PutDestinationPolicyRequestRequestTypeDef",
    "PutDestinationRequestRequestTypeDef",
    "PutDestinationResponseTypeDef",
    "PutLogEventsRequestRequestTypeDef",
    "PutLogEventsResponseTypeDef",
    "PutMetricFilterRequestRequestTypeDef",
    "PutQueryDefinitionRequestRequestTypeDef",
    "PutQueryDefinitionResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutRetentionPolicyRequestRequestTypeDef",
    "PutSubscriptionFilterRequestRequestTypeDef",
    "QueryDefinitionTypeDef",
    "QueryInfoTypeDef",
    "QueryStatisticsTypeDef",
    "RejectedLogEventsInfoTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResultFieldTypeDef",
    "SearchedLogStreamTypeDef",
    "StartQueryRequestRequestTypeDef",
    "StartQueryResponseTypeDef",
    "StopQueryRequestRequestTypeDef",
    "StopQueryResponseTypeDef",
    "SubscriptionFilterTypeDef",
    "TagLogGroupRequestRequestTypeDef",
    "TestMetricFilterRequestRequestTypeDef",
    "TestMetricFilterResponseTypeDef",
    "UntagLogGroupRequestRequestTypeDef",
)

AssociateKmsKeyRequestRequestTypeDef = TypedDict(
    "AssociateKmsKeyRequestRequestTypeDef",
    {
        "logGroupName": str,
        "kmsKeyId": str,
    },
)

CancelExportTaskRequestRequestTypeDef = TypedDict(
    "CancelExportTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

_RequiredCreateExportTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateExportTaskRequestRequestTypeDef",
    {
        "logGroupName": str,
        "fromTime": int,
        "to": int,
        "destination": str,
    },
)
_OptionalCreateExportTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateExportTaskRequestRequestTypeDef",
    {
        "taskName": str,
        "logStreamNamePrefix": str,
        "destinationPrefix": str,
    },
    total=False,
)

class CreateExportTaskRequestRequestTypeDef(
    _RequiredCreateExportTaskRequestRequestTypeDef, _OptionalCreateExportTaskRequestRequestTypeDef
):
    pass

CreateExportTaskResponseTypeDef = TypedDict(
    "CreateExportTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLogGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalCreateLogGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLogGroupRequestRequestTypeDef",
    {
        "kmsKeyId": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateLogGroupRequestRequestTypeDef(
    _RequiredCreateLogGroupRequestRequestTypeDef, _OptionalCreateLogGroupRequestRequestTypeDef
):
    pass

CreateLogStreamRequestRequestTypeDef = TypedDict(
    "CreateLogStreamRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
    },
)

DeleteDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDestinationRequestRequestTypeDef",
    {
        "destinationName": str,
    },
)

DeleteLogGroupRequestRequestTypeDef = TypedDict(
    "DeleteLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)

DeleteLogStreamRequestRequestTypeDef = TypedDict(
    "DeleteLogStreamRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
    },
)

DeleteMetricFilterRequestRequestTypeDef = TypedDict(
    "DeleteMetricFilterRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
    },
)

DeleteQueryDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteQueryDefinitionRequestRequestTypeDef",
    {
        "queryDefinitionId": str,
    },
)

DeleteQueryDefinitionResponseTypeDef = TypedDict(
    "DeleteQueryDefinitionResponseTypeDef",
    {
        "success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "policyName": str,
    },
    total=False,
)

DeleteRetentionPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRetentionPolicyRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)

DeleteSubscriptionFilterRequestRequestTypeDef = TypedDict(
    "DeleteSubscriptionFilterRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
    },
)

DescribeDestinationsRequestRequestTypeDef = TypedDict(
    "DescribeDestinationsRequestRequestTypeDef",
    {
        "DestinationNamePrefix": str,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeDestinationsResponseTypeDef = TypedDict(
    "DescribeDestinationsResponseTypeDef",
    {
        "destinations": List["DestinationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestRequestTypeDef",
    {
        "taskId": str,
        "statusCode": ExportTaskStatusCodeType,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {
        "exportTasks": List["ExportTaskTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLogGroupsRequestRequestTypeDef = TypedDict(
    "DescribeLogGroupsRequestRequestTypeDef",
    {
        "logGroupNamePrefix": str,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeLogGroupsResponseTypeDef = TypedDict(
    "DescribeLogGroupsResponseTypeDef",
    {
        "logGroups": List["LogGroupTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeLogStreamsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeLogStreamsRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalDescribeLogStreamsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeLogStreamsRequestRequestTypeDef",
    {
        "logStreamNamePrefix": str,
        "orderBy": OrderByType,
        "descending": bool,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

class DescribeLogStreamsRequestRequestTypeDef(
    _RequiredDescribeLogStreamsRequestRequestTypeDef,
    _OptionalDescribeLogStreamsRequestRequestTypeDef,
):
    pass

DescribeLogStreamsResponseTypeDef = TypedDict(
    "DescribeLogStreamsResponseTypeDef",
    {
        "logStreams": List["LogStreamTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricFiltersRequestRequestTypeDef = TypedDict(
    "DescribeMetricFiltersRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterNamePrefix": str,
        "nextToken": str,
        "limit": int,
        "metricName": str,
        "metricNamespace": str,
    },
    total=False,
)

DescribeMetricFiltersResponseTypeDef = TypedDict(
    "DescribeMetricFiltersResponseTypeDef",
    {
        "metricFilters": List["MetricFilterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueriesRequestRequestTypeDef = TypedDict(
    "DescribeQueriesRequestRequestTypeDef",
    {
        "logGroupName": str,
        "status": QueryStatusType,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeQueriesResponseTypeDef = TypedDict(
    "DescribeQueriesResponseTypeDef",
    {
        "queries": List["QueryInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueryDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeQueryDefinitionsRequestRequestTypeDef",
    {
        "queryDefinitionNamePrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

DescribeQueryDefinitionsResponseTypeDef = TypedDict(
    "DescribeQueryDefinitionsResponseTypeDef",
    {
        "queryDefinitions": List["QueryDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePoliciesRequestRequestTypeDef = TypedDict(
    "DescribeResourcePoliciesRequestRequestTypeDef",
    {
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeResourcePoliciesResponseTypeDef = TypedDict(
    "DescribeResourcePoliciesResponseTypeDef",
    {
        "resourcePolicies": List["ResourcePolicyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSubscriptionFiltersRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSubscriptionFiltersRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalDescribeSubscriptionFiltersRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSubscriptionFiltersRequestRequestTypeDef",
    {
        "filterNamePrefix": str,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

class DescribeSubscriptionFiltersRequestRequestTypeDef(
    _RequiredDescribeSubscriptionFiltersRequestRequestTypeDef,
    _OptionalDescribeSubscriptionFiltersRequestRequestTypeDef,
):
    pass

DescribeSubscriptionFiltersResponseTypeDef = TypedDict(
    "DescribeSubscriptionFiltersResponseTypeDef",
    {
        "subscriptionFilters": List["SubscriptionFilterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
        "accessPolicy": str,
        "arn": str,
        "creationTime": int,
    },
    total=False,
)

DisassociateKmsKeyRequestRequestTypeDef = TypedDict(
    "DisassociateKmsKeyRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)

ExportTaskExecutionInfoTypeDef = TypedDict(
    "ExportTaskExecutionInfoTypeDef",
    {
        "creationTime": int,
        "completionTime": int,
    },
    total=False,
)

ExportTaskStatusTypeDef = TypedDict(
    "ExportTaskStatusTypeDef",
    {
        "code": ExportTaskStatusCodeType,
        "message": str,
    },
    total=False,
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": "ExportTaskStatusTypeDef",
        "executionInfo": "ExportTaskExecutionInfoTypeDef",
    },
    total=False,
)

_RequiredFilterLogEventsRequestRequestTypeDef = TypedDict(
    "_RequiredFilterLogEventsRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalFilterLogEventsRequestRequestTypeDef = TypedDict(
    "_OptionalFilterLogEventsRequestRequestTypeDef",
    {
        "logStreamNames": List[str],
        "logStreamNamePrefix": str,
        "startTime": int,
        "endTime": int,
        "filterPattern": str,
        "nextToken": str,
        "limit": int,
        "interleaved": bool,
    },
    total=False,
)

class FilterLogEventsRequestRequestTypeDef(
    _RequiredFilterLogEventsRequestRequestTypeDef, _OptionalFilterLogEventsRequestRequestTypeDef
):
    pass

FilterLogEventsResponseTypeDef = TypedDict(
    "FilterLogEventsResponseTypeDef",
    {
        "events": List["FilteredLogEventTypeDef"],
        "searchedLogStreams": List["SearchedLogStreamTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilteredLogEventTypeDef = TypedDict(
    "FilteredLogEventTypeDef",
    {
        "logStreamName": str,
        "timestamp": int,
        "message": str,
        "ingestionTime": int,
        "eventId": str,
    },
    total=False,
)

_RequiredGetLogEventsRequestRequestTypeDef = TypedDict(
    "_RequiredGetLogEventsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
    },
)
_OptionalGetLogEventsRequestRequestTypeDef = TypedDict(
    "_OptionalGetLogEventsRequestRequestTypeDef",
    {
        "startTime": int,
        "endTime": int,
        "nextToken": str,
        "limit": int,
        "startFromHead": bool,
    },
    total=False,
)

class GetLogEventsRequestRequestTypeDef(
    _RequiredGetLogEventsRequestRequestTypeDef, _OptionalGetLogEventsRequestRequestTypeDef
):
    pass

GetLogEventsResponseTypeDef = TypedDict(
    "GetLogEventsResponseTypeDef",
    {
        "events": List["OutputLogEventTypeDef"],
        "nextForwardToken": str,
        "nextBackwardToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLogGroupFieldsRequestRequestTypeDef = TypedDict(
    "_RequiredGetLogGroupFieldsRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)
_OptionalGetLogGroupFieldsRequestRequestTypeDef = TypedDict(
    "_OptionalGetLogGroupFieldsRequestRequestTypeDef",
    {
        "time": int,
    },
    total=False,
)

class GetLogGroupFieldsRequestRequestTypeDef(
    _RequiredGetLogGroupFieldsRequestRequestTypeDef, _OptionalGetLogGroupFieldsRequestRequestTypeDef
):
    pass

GetLogGroupFieldsResponseTypeDef = TypedDict(
    "GetLogGroupFieldsResponseTypeDef",
    {
        "logGroupFields": List["LogGroupFieldTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLogRecordRequestRequestTypeDef = TypedDict(
    "GetLogRecordRequestRequestTypeDef",
    {
        "logRecordPointer": str,
    },
)

GetLogRecordResponseTypeDef = TypedDict(
    "GetLogRecordResponseTypeDef",
    {
        "logRecord": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryResultsRequestRequestTypeDef = TypedDict(
    "GetQueryResultsRequestRequestTypeDef",
    {
        "queryId": str,
    },
)

GetQueryResultsResponseTypeDef = TypedDict(
    "GetQueryResultsResponseTypeDef",
    {
        "results": List[List["ResultFieldTypeDef"]],
        "statistics": "QueryStatisticsTypeDef",
        "status": QueryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputLogEventTypeDef = TypedDict(
    "InputLogEventTypeDef",
    {
        "timestamp": int,
        "message": str,
    },
)

ListTagsLogGroupRequestRequestTypeDef = TypedDict(
    "ListTagsLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)

ListTagsLogGroupResponseTypeDef = TypedDict(
    "ListTagsLogGroupResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogGroupFieldTypeDef = TypedDict(
    "LogGroupFieldTypeDef",
    {
        "name": str,
        "percent": int,
    },
    total=False,
)

LogGroupTypeDef = TypedDict(
    "LogGroupTypeDef",
    {
        "logGroupName": str,
        "creationTime": int,
        "retentionInDays": int,
        "metricFilterCount": int,
        "arn": str,
        "storedBytes": int,
        "kmsKeyId": str,
    },
    total=False,
)

LogStreamTypeDef = TypedDict(
    "LogStreamTypeDef",
    {
        "logStreamName": str,
        "creationTime": int,
        "firstEventTimestamp": int,
        "lastEventTimestamp": int,
        "lastIngestionTime": int,
        "uploadSequenceToken": str,
        "arn": str,
        "storedBytes": int,
    },
    total=False,
)

MetricFilterMatchRecordTypeDef = TypedDict(
    "MetricFilterMatchRecordTypeDef",
    {
        "eventNumber": int,
        "eventMessage": str,
        "extractedValues": Dict[str, str],
    },
    total=False,
)

MetricFilterTypeDef = TypedDict(
    "MetricFilterTypeDef",
    {
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List["MetricTransformationTypeDef"],
        "creationTime": int,
        "logGroupName": str,
    },
    total=False,
)

_RequiredMetricTransformationTypeDef = TypedDict(
    "_RequiredMetricTransformationTypeDef",
    {
        "metricName": str,
        "metricNamespace": str,
        "metricValue": str,
    },
)
_OptionalMetricTransformationTypeDef = TypedDict(
    "_OptionalMetricTransformationTypeDef",
    {
        "defaultValue": float,
        "dimensions": Dict[str, str],
        "unit": StandardUnitType,
    },
    total=False,
)

class MetricTransformationTypeDef(
    _RequiredMetricTransformationTypeDef, _OptionalMetricTransformationTypeDef
):
    pass

OutputLogEventTypeDef = TypedDict(
    "OutputLogEventTypeDef",
    {
        "timestamp": int,
        "message": str,
        "ingestionTime": int,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PutDestinationPolicyRequestRequestTypeDef = TypedDict(
    "PutDestinationPolicyRequestRequestTypeDef",
    {
        "destinationName": str,
        "accessPolicy": str,
    },
)

PutDestinationRequestRequestTypeDef = TypedDict(
    "PutDestinationRequestRequestTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
    },
)

PutDestinationResponseTypeDef = TypedDict(
    "PutDestinationResponseTypeDef",
    {
        "destination": "DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutLogEventsRequestRequestTypeDef = TypedDict(
    "_RequiredPutLogEventsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
        "logEvents": List["InputLogEventTypeDef"],
    },
)
_OptionalPutLogEventsRequestRequestTypeDef = TypedDict(
    "_OptionalPutLogEventsRequestRequestTypeDef",
    {
        "sequenceToken": str,
    },
    total=False,
)

class PutLogEventsRequestRequestTypeDef(
    _RequiredPutLogEventsRequestRequestTypeDef, _OptionalPutLogEventsRequestRequestTypeDef
):
    pass

PutLogEventsResponseTypeDef = TypedDict(
    "PutLogEventsResponseTypeDef",
    {
        "nextSequenceToken": str,
        "rejectedLogEventsInfo": "RejectedLogEventsInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutMetricFilterRequestRequestTypeDef = TypedDict(
    "PutMetricFilterRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": List["MetricTransformationTypeDef"],
    },
)

_RequiredPutQueryDefinitionRequestRequestTypeDef = TypedDict(
    "_RequiredPutQueryDefinitionRequestRequestTypeDef",
    {
        "name": str,
        "queryString": str,
    },
)
_OptionalPutQueryDefinitionRequestRequestTypeDef = TypedDict(
    "_OptionalPutQueryDefinitionRequestRequestTypeDef",
    {
        "queryDefinitionId": str,
        "logGroupNames": List[str],
    },
    total=False,
)

class PutQueryDefinitionRequestRequestTypeDef(
    _RequiredPutQueryDefinitionRequestRequestTypeDef,
    _OptionalPutQueryDefinitionRequestRequestTypeDef,
):
    pass

PutQueryDefinitionResponseTypeDef = TypedDict(
    "PutQueryDefinitionResponseTypeDef",
    {
        "queryDefinitionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
    },
    total=False,
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "resourcePolicy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRetentionPolicyRequestRequestTypeDef = TypedDict(
    "PutRetentionPolicyRequestRequestTypeDef",
    {
        "logGroupName": str,
        "retentionInDays": int,
    },
)

_RequiredPutSubscriptionFilterRequestRequestTypeDef = TypedDict(
    "_RequiredPutSubscriptionFilterRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
        "filterPattern": str,
        "destinationArn": str,
    },
)
_OptionalPutSubscriptionFilterRequestRequestTypeDef = TypedDict(
    "_OptionalPutSubscriptionFilterRequestRequestTypeDef",
    {
        "roleArn": str,
        "distribution": DistributionType,
    },
    total=False,
)

class PutSubscriptionFilterRequestRequestTypeDef(
    _RequiredPutSubscriptionFilterRequestRequestTypeDef,
    _OptionalPutSubscriptionFilterRequestRequestTypeDef,
):
    pass

QueryDefinitionTypeDef = TypedDict(
    "QueryDefinitionTypeDef",
    {
        "queryDefinitionId": str,
        "name": str,
        "queryString": str,
        "lastModified": int,
        "logGroupNames": List[str],
    },
    total=False,
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "queryId": str,
        "queryString": str,
        "status": QueryStatusType,
        "createTime": int,
        "logGroupName": str,
    },
    total=False,
)

QueryStatisticsTypeDef = TypedDict(
    "QueryStatisticsTypeDef",
    {
        "recordsMatched": float,
        "recordsScanned": float,
        "bytesScanned": float,
    },
    total=False,
)

RejectedLogEventsInfoTypeDef = TypedDict(
    "RejectedLogEventsInfoTypeDef",
    {
        "tooNewLogEventStartIndex": int,
        "tooOldLogEventEndIndex": int,
        "expiredLogEventEndIndex": int,
    },
    total=False,
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
        "lastUpdatedTime": int,
    },
    total=False,
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

ResultFieldTypeDef = TypedDict(
    "ResultFieldTypeDef",
    {
        "field": str,
        "value": str,
    },
    total=False,
)

SearchedLogStreamTypeDef = TypedDict(
    "SearchedLogStreamTypeDef",
    {
        "logStreamName": str,
        "searchedCompletely": bool,
    },
    total=False,
)

_RequiredStartQueryRequestRequestTypeDef = TypedDict(
    "_RequiredStartQueryRequestRequestTypeDef",
    {
        "startTime": int,
        "endTime": int,
        "queryString": str,
    },
)
_OptionalStartQueryRequestRequestTypeDef = TypedDict(
    "_OptionalStartQueryRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logGroupNames": List[str],
        "limit": int,
    },
    total=False,
)

class StartQueryRequestRequestTypeDef(
    _RequiredStartQueryRequestRequestTypeDef, _OptionalStartQueryRequestRequestTypeDef
):
    pass

StartQueryResponseTypeDef = TypedDict(
    "StartQueryResponseTypeDef",
    {
        "queryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopQueryRequestRequestTypeDef = TypedDict(
    "StopQueryRequestRequestTypeDef",
    {
        "queryId": str,
    },
)

StopQueryResponseTypeDef = TypedDict(
    "StopQueryResponseTypeDef",
    {
        "success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscriptionFilterTypeDef = TypedDict(
    "SubscriptionFilterTypeDef",
    {
        "filterName": str,
        "logGroupName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": str,
        "distribution": DistributionType,
        "creationTime": int,
    },
    total=False,
)

TagLogGroupRequestRequestTypeDef = TypedDict(
    "TagLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
        "tags": Dict[str, str],
    },
)

TestMetricFilterRequestRequestTypeDef = TypedDict(
    "TestMetricFilterRequestRequestTypeDef",
    {
        "filterPattern": str,
        "logEventMessages": List[str],
    },
)

TestMetricFilterResponseTypeDef = TypedDict(
    "TestMetricFilterResponseTypeDef",
    {
        "matches": List["MetricFilterMatchRecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagLogGroupRequestRequestTypeDef = TypedDict(
    "UntagLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
        "tags": List[str],
    },
)
