"""
Type annotations for logs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_logs.type_defs import AccountPolicyTypeDef

    data: AccountPolicyTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    AnomalyDetectorStatusType,
    DataProtectionStatusType,
    DeliveryDestinationTypeType,
    DistributionType,
    EvaluationFrequencyType,
    ExportTaskStatusCodeType,
    LogGroupClassType,
    OrderByType,
    OutputFormatType,
    QueryStatusType,
    StandardUnitType,
    StateType,
    SuppressionStateType,
    SuppressionTypeType,
    SuppressionUnitType,
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
    "AccountPolicyTypeDef",
    "AnomalyDetectorTypeDef",
    "AnomalyTypeDef",
    "AssociateKmsKeyRequestRequestTypeDef",
    "CancelExportTaskRequestRequestTypeDef",
    "CreateDeliveryRequestRequestTypeDef",
    "CreateDeliveryResponseTypeDef",
    "CreateExportTaskRequestRequestTypeDef",
    "CreateExportTaskResponseTypeDef",
    "CreateLogAnomalyDetectorRequestRequestTypeDef",
    "CreateLogAnomalyDetectorResponseTypeDef",
    "CreateLogGroupRequestRequestTypeDef",
    "CreateLogStreamRequestRequestTypeDef",
    "DeleteAccountPolicyRequestRequestTypeDef",
    "DeleteDataProtectionPolicyRequestRequestTypeDef",
    "DeleteDeliveryDestinationPolicyRequestRequestTypeDef",
    "DeleteDeliveryDestinationRequestRequestTypeDef",
    "DeleteDeliveryRequestRequestTypeDef",
    "DeleteDeliverySourceRequestRequestTypeDef",
    "DeleteDestinationRequestRequestTypeDef",
    "DeleteLogAnomalyDetectorRequestRequestTypeDef",
    "DeleteLogGroupRequestRequestTypeDef",
    "DeleteLogStreamRequestRequestTypeDef",
    "DeleteMetricFilterRequestRequestTypeDef",
    "DeleteQueryDefinitionRequestRequestTypeDef",
    "DeleteQueryDefinitionResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRetentionPolicyRequestRequestTypeDef",
    "DeleteSubscriptionFilterRequestRequestTypeDef",
    "DeliveryDestinationConfigurationTypeDef",
    "DeliveryDestinationTypeDef",
    "DeliverySourceTypeDef",
    "DeliveryTypeDef",
    "DescribeAccountPoliciesRequestRequestTypeDef",
    "DescribeAccountPoliciesResponseTypeDef",
    "DescribeDeliveriesRequestRequestTypeDef",
    "DescribeDeliveriesResponseTypeDef",
    "DescribeDeliveryDestinationsRequestRequestTypeDef",
    "DescribeDeliveryDestinationsResponseTypeDef",
    "DescribeDeliverySourcesRequestRequestTypeDef",
    "DescribeDeliverySourcesResponseTypeDef",
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
    "GetDataProtectionPolicyRequestRequestTypeDef",
    "GetDataProtectionPolicyResponseTypeDef",
    "GetDeliveryDestinationPolicyRequestRequestTypeDef",
    "GetDeliveryDestinationPolicyResponseTypeDef",
    "GetDeliveryDestinationRequestRequestTypeDef",
    "GetDeliveryDestinationResponseTypeDef",
    "GetDeliveryRequestRequestTypeDef",
    "GetDeliveryResponseTypeDef",
    "GetDeliverySourceRequestRequestTypeDef",
    "GetDeliverySourceResponseTypeDef",
    "GetLogAnomalyDetectorRequestRequestTypeDef",
    "GetLogAnomalyDetectorResponseTypeDef",
    "GetLogEventsRequestRequestTypeDef",
    "GetLogEventsResponseTypeDef",
    "GetLogGroupFieldsRequestRequestTypeDef",
    "GetLogGroupFieldsResponseTypeDef",
    "GetLogRecordRequestRequestTypeDef",
    "GetLogRecordResponseTypeDef",
    "GetQueryResultsRequestRequestTypeDef",
    "GetQueryResultsResponseTypeDef",
    "InputLogEventTypeDef",
    "ListAnomaliesRequestRequestTypeDef",
    "ListAnomaliesResponseTypeDef",
    "ListLogAnomalyDetectorsRequestRequestTypeDef",
    "ListLogAnomalyDetectorsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
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
    "PatternTokenTypeDef",
    "PolicyTypeDef",
    "PutAccountPolicyRequestRequestTypeDef",
    "PutAccountPolicyResponseTypeDef",
    "PutDataProtectionPolicyRequestRequestTypeDef",
    "PutDataProtectionPolicyResponseTypeDef",
    "PutDeliveryDestinationPolicyRequestRequestTypeDef",
    "PutDeliveryDestinationPolicyResponseTypeDef",
    "PutDeliveryDestinationRequestRequestTypeDef",
    "PutDeliveryDestinationResponseTypeDef",
    "PutDeliverySourceRequestRequestTypeDef",
    "PutDeliverySourceResponseTypeDef",
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
    "SuppressionPeriodTypeDef",
    "TagLogGroupRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestMetricFilterRequestRequestTypeDef",
    "TestMetricFilterResponseTypeDef",
    "UntagLogGroupRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAnomalyRequestRequestTypeDef",
    "UpdateLogAnomalyDetectorRequestRequestTypeDef",
)

AccountPolicyTypeDef = TypedDict(
    "AccountPolicyTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
        "lastUpdatedTime": int,
        "policyType": Literal["DATA_PROTECTION_POLICY"],
        "scope": Literal["ALL"],
        "accountId": str,
    },
    total=False,
)

AnomalyDetectorTypeDef = TypedDict(
    "AnomalyDetectorTypeDef",
    {
        "anomalyDetectorArn": str,
        "detectorName": str,
        "logGroupArnList": List[str],
        "evaluationFrequency": EvaluationFrequencyType,
        "filterPattern": str,
        "anomalyDetectorStatus": AnomalyDetectorStatusType,
        "kmsKeyId": str,
        "creationTimeStamp": int,
        "lastModifiedTimeStamp": int,
        "anomalyVisibilityTime": int,
    },
    total=False,
)

_RequiredAnomalyTypeDef = TypedDict(
    "_RequiredAnomalyTypeDef",
    {
        "anomalyId": str,
        "patternId": str,
        "anomalyDetectorArn": str,
        "patternString": str,
        "firstSeen": int,
        "lastSeen": int,
        "description": str,
        "active": bool,
        "state": StateType,
        "histogram": Dict[str, int],
        "logSamples": List[str],
        "patternTokens": List["PatternTokenTypeDef"],
        "logGroupArnList": List[str],
    },
)
_OptionalAnomalyTypeDef = TypedDict(
    "_OptionalAnomalyTypeDef",
    {
        "patternRegex": str,
        "priority": str,
        "suppressed": bool,
        "suppressedDate": int,
        "suppressedUntil": int,
        "isPatternLevelSuppression": bool,
    },
    total=False,
)

class AnomalyTypeDef(_RequiredAnomalyTypeDef, _OptionalAnomalyTypeDef):
    pass

_RequiredAssociateKmsKeyRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateKmsKeyRequestRequestTypeDef",
    {
        "kmsKeyId": str,
    },
)
_OptionalAssociateKmsKeyRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateKmsKeyRequestRequestTypeDef",
    {
        "logGroupName": str,
        "resourceIdentifier": str,
    },
    total=False,
)

class AssociateKmsKeyRequestRequestTypeDef(
    _RequiredAssociateKmsKeyRequestRequestTypeDef, _OptionalAssociateKmsKeyRequestRequestTypeDef
):
    pass

CancelExportTaskRequestRequestTypeDef = TypedDict(
    "CancelExportTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

_RequiredCreateDeliveryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDeliveryRequestRequestTypeDef",
    {
        "deliverySourceName": str,
        "deliveryDestinationArn": str,
    },
)
_OptionalCreateDeliveryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDeliveryRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateDeliveryRequestRequestTypeDef(
    _RequiredCreateDeliveryRequestRequestTypeDef, _OptionalCreateDeliveryRequestRequestTypeDef
):
    pass

CreateDeliveryResponseTypeDef = TypedDict(
    "CreateDeliveryResponseTypeDef",
    {
        "delivery": "DeliveryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredCreateLogAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLogAnomalyDetectorRequestRequestTypeDef",
    {
        "logGroupArnList": List[str],
    },
)
_OptionalCreateLogAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLogAnomalyDetectorRequestRequestTypeDef",
    {
        "detectorName": str,
        "evaluationFrequency": EvaluationFrequencyType,
        "filterPattern": str,
        "kmsKeyId": str,
        "anomalyVisibilityTime": int,
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateLogAnomalyDetectorRequestRequestTypeDef(
    _RequiredCreateLogAnomalyDetectorRequestRequestTypeDef,
    _OptionalCreateLogAnomalyDetectorRequestRequestTypeDef,
):
    pass

CreateLogAnomalyDetectorResponseTypeDef = TypedDict(
    "CreateLogAnomalyDetectorResponseTypeDef",
    {
        "anomalyDetectorArn": str,
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
        "logGroupClass": LogGroupClassType,
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

DeleteAccountPolicyRequestRequestTypeDef = TypedDict(
    "DeleteAccountPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "policyType": Literal["DATA_PROTECTION_POLICY"],
    },
)

DeleteDataProtectionPolicyRequestRequestTypeDef = TypedDict(
    "DeleteDataProtectionPolicyRequestRequestTypeDef",
    {
        "logGroupIdentifier": str,
    },
)

DeleteDeliveryDestinationPolicyRequestRequestTypeDef = TypedDict(
    "DeleteDeliveryDestinationPolicyRequestRequestTypeDef",
    {
        "deliveryDestinationName": str,
    },
)

DeleteDeliveryDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDeliveryDestinationRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteDeliveryRequestRequestTypeDef = TypedDict(
    "DeleteDeliveryRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteDeliverySourceRequestRequestTypeDef = TypedDict(
    "DeleteDeliverySourceRequestRequestTypeDef",
    {
        "name": str,
    },
)

DeleteDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDestinationRequestRequestTypeDef",
    {
        "destinationName": str,
    },
)

DeleteLogAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeleteLogAnomalyDetectorRequestRequestTypeDef",
    {
        "anomalyDetectorArn": str,
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

DeliveryDestinationConfigurationTypeDef = TypedDict(
    "DeliveryDestinationConfigurationTypeDef",
    {
        "destinationResourceArn": str,
    },
)

DeliveryDestinationTypeDef = TypedDict(
    "DeliveryDestinationTypeDef",
    {
        "name": str,
        "arn": str,
        "deliveryDestinationType": DeliveryDestinationTypeType,
        "outputFormat": OutputFormatType,
        "deliveryDestinationConfiguration": "DeliveryDestinationConfigurationTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

DeliverySourceTypeDef = TypedDict(
    "DeliverySourceTypeDef",
    {
        "name": str,
        "arn": str,
        "resourceArns": List[str],
        "service": str,
        "logType": str,
        "tags": Dict[str, str],
    },
    total=False,
)

DeliveryTypeDef = TypedDict(
    "DeliveryTypeDef",
    {
        "id": str,
        "arn": str,
        "deliverySourceName": str,
        "deliveryDestinationArn": str,
        "deliveryDestinationType": DeliveryDestinationTypeType,
        "tags": Dict[str, str],
    },
    total=False,
)

_RequiredDescribeAccountPoliciesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeAccountPoliciesRequestRequestTypeDef",
    {
        "policyType": Literal["DATA_PROTECTION_POLICY"],
    },
)
_OptionalDescribeAccountPoliciesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeAccountPoliciesRequestRequestTypeDef",
    {
        "policyName": str,
        "accountIdentifiers": List[str],
    },
    total=False,
)

class DescribeAccountPoliciesRequestRequestTypeDef(
    _RequiredDescribeAccountPoliciesRequestRequestTypeDef,
    _OptionalDescribeAccountPoliciesRequestRequestTypeDef,
):
    pass

DescribeAccountPoliciesResponseTypeDef = TypedDict(
    "DescribeAccountPoliciesResponseTypeDef",
    {
        "accountPolicies": List["AccountPolicyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliveriesRequestRequestTypeDef = TypedDict(
    "DescribeDeliveriesRequestRequestTypeDef",
    {
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeDeliveriesResponseTypeDef = TypedDict(
    "DescribeDeliveriesResponseTypeDef",
    {
        "deliveries": List["DeliveryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliveryDestinationsRequestRequestTypeDef = TypedDict(
    "DescribeDeliveryDestinationsRequestRequestTypeDef",
    {
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeDeliveryDestinationsResponseTypeDef = TypedDict(
    "DescribeDeliveryDestinationsResponseTypeDef",
    {
        "deliveryDestinations": List["DeliveryDestinationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeliverySourcesRequestRequestTypeDef = TypedDict(
    "DescribeDeliverySourcesRequestRequestTypeDef",
    {
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

DescribeDeliverySourcesResponseTypeDef = TypedDict(
    "DescribeDeliverySourcesResponseTypeDef",
    {
        "deliverySources": List["DeliverySourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "accountIdentifiers": List[str],
        "logGroupNamePrefix": str,
        "logGroupNamePattern": str,
        "nextToken": str,
        "limit": int,
        "includeLinkedAccounts": bool,
        "logGroupClass": LogGroupClassType,
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

DescribeLogStreamsRequestRequestTypeDef = TypedDict(
    "DescribeLogStreamsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logGroupIdentifier": str,
        "logStreamNamePrefix": str,
        "orderBy": OrderByType,
        "descending": bool,
        "nextToken": str,
        "limit": int,
    },
    total=False,
)

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
        "resourceIdentifier": str,
    },
    total=False,
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

FilterLogEventsRequestRequestTypeDef = TypedDict(
    "FilterLogEventsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logGroupIdentifier": str,
        "logStreamNames": List[str],
        "logStreamNamePrefix": str,
        "startTime": int,
        "endTime": int,
        "filterPattern": str,
        "nextToken": str,
        "limit": int,
        "interleaved": bool,
        "unmask": bool,
    },
    total=False,
)

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

GetDataProtectionPolicyRequestRequestTypeDef = TypedDict(
    "GetDataProtectionPolicyRequestRequestTypeDef",
    {
        "logGroupIdentifier": str,
    },
)

GetDataProtectionPolicyResponseTypeDef = TypedDict(
    "GetDataProtectionPolicyResponseTypeDef",
    {
        "logGroupIdentifier": str,
        "policyDocument": str,
        "lastUpdatedTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliveryDestinationPolicyRequestRequestTypeDef = TypedDict(
    "GetDeliveryDestinationPolicyRequestRequestTypeDef",
    {
        "deliveryDestinationName": str,
    },
)

GetDeliveryDestinationPolicyResponseTypeDef = TypedDict(
    "GetDeliveryDestinationPolicyResponseTypeDef",
    {
        "policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliveryDestinationRequestRequestTypeDef = TypedDict(
    "GetDeliveryDestinationRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetDeliveryDestinationResponseTypeDef = TypedDict(
    "GetDeliveryDestinationResponseTypeDef",
    {
        "deliveryDestination": "DeliveryDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliveryRequestRequestTypeDef = TypedDict(
    "GetDeliveryRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetDeliveryResponseTypeDef = TypedDict(
    "GetDeliveryResponseTypeDef",
    {
        "delivery": "DeliveryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeliverySourceRequestRequestTypeDef = TypedDict(
    "GetDeliverySourceRequestRequestTypeDef",
    {
        "name": str,
    },
)

GetDeliverySourceResponseTypeDef = TypedDict(
    "GetDeliverySourceResponseTypeDef",
    {
        "deliverySource": "DeliverySourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLogAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "GetLogAnomalyDetectorRequestRequestTypeDef",
    {
        "anomalyDetectorArn": str,
    },
)

GetLogAnomalyDetectorResponseTypeDef = TypedDict(
    "GetLogAnomalyDetectorResponseTypeDef",
    {
        "detectorName": str,
        "logGroupArnList": List[str],
        "evaluationFrequency": EvaluationFrequencyType,
        "filterPattern": str,
        "anomalyDetectorStatus": AnomalyDetectorStatusType,
        "kmsKeyId": str,
        "creationTimeStamp": int,
        "lastModifiedTimeStamp": int,
        "anomalyVisibilityTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLogEventsRequestRequestTypeDef = TypedDict(
    "_RequiredGetLogEventsRequestRequestTypeDef",
    {
        "logStreamName": str,
    },
)
_OptionalGetLogEventsRequestRequestTypeDef = TypedDict(
    "_OptionalGetLogEventsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logGroupIdentifier": str,
        "startTime": int,
        "endTime": int,
        "nextToken": str,
        "limit": int,
        "startFromHead": bool,
        "unmask": bool,
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

GetLogGroupFieldsRequestRequestTypeDef = TypedDict(
    "GetLogGroupFieldsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "time": int,
        "logGroupIdentifier": str,
    },
    total=False,
)

GetLogGroupFieldsResponseTypeDef = TypedDict(
    "GetLogGroupFieldsResponseTypeDef",
    {
        "logGroupFields": List["LogGroupFieldTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLogRecordRequestRequestTypeDef = TypedDict(
    "_RequiredGetLogRecordRequestRequestTypeDef",
    {
        "logRecordPointer": str,
    },
)
_OptionalGetLogRecordRequestRequestTypeDef = TypedDict(
    "_OptionalGetLogRecordRequestRequestTypeDef",
    {
        "unmask": bool,
    },
    total=False,
)

class GetLogRecordRequestRequestTypeDef(
    _RequiredGetLogRecordRequestRequestTypeDef, _OptionalGetLogRecordRequestRequestTypeDef
):
    pass

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
        "encryptionKey": str,
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

ListAnomaliesRequestRequestTypeDef = TypedDict(
    "ListAnomaliesRequestRequestTypeDef",
    {
        "anomalyDetectorArn": str,
        "suppressionState": SuppressionStateType,
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

ListAnomaliesResponseTypeDef = TypedDict(
    "ListAnomaliesResponseTypeDef",
    {
        "anomalies": List["AnomalyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLogAnomalyDetectorsRequestRequestTypeDef = TypedDict(
    "ListLogAnomalyDetectorsRequestRequestTypeDef",
    {
        "filterLogGroupArn": str,
        "limit": int,
        "nextToken": str,
    },
    total=False,
)

ListLogAnomalyDetectorsResponseTypeDef = TypedDict(
    "ListLogAnomalyDetectorsResponseTypeDef",
    {
        "anomalyDetectors": List["AnomalyDetectorTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "dataProtectionStatus": DataProtectionStatusType,
        "inheritedProperties": List[Literal["ACCOUNT_DATA_PROTECTION"]],
        "logGroupClass": LogGroupClassType,
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

PatternTokenTypeDef = TypedDict(
    "PatternTokenTypeDef",
    {
        "dynamicTokenPosition": int,
        "isDynamic": bool,
        "tokenString": str,
        "enumerations": Dict[str, int],
    },
    total=False,
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "deliveryDestinationPolicy": str,
    },
    total=False,
)

_RequiredPutAccountPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutAccountPolicyRequestRequestTypeDef",
    {
        "policyName": str,
        "policyDocument": str,
        "policyType": Literal["DATA_PROTECTION_POLICY"],
    },
)
_OptionalPutAccountPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutAccountPolicyRequestRequestTypeDef",
    {
        "scope": Literal["ALL"],
    },
    total=False,
)

class PutAccountPolicyRequestRequestTypeDef(
    _RequiredPutAccountPolicyRequestRequestTypeDef, _OptionalPutAccountPolicyRequestRequestTypeDef
):
    pass

PutAccountPolicyResponseTypeDef = TypedDict(
    "PutAccountPolicyResponseTypeDef",
    {
        "accountPolicy": "AccountPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutDataProtectionPolicyRequestRequestTypeDef = TypedDict(
    "PutDataProtectionPolicyRequestRequestTypeDef",
    {
        "logGroupIdentifier": str,
        "policyDocument": str,
    },
)

PutDataProtectionPolicyResponseTypeDef = TypedDict(
    "PutDataProtectionPolicyResponseTypeDef",
    {
        "logGroupIdentifier": str,
        "policyDocument": str,
        "lastUpdatedTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutDeliveryDestinationPolicyRequestRequestTypeDef = TypedDict(
    "PutDeliveryDestinationPolicyRequestRequestTypeDef",
    {
        "deliveryDestinationName": str,
        "deliveryDestinationPolicy": str,
    },
)

PutDeliveryDestinationPolicyResponseTypeDef = TypedDict(
    "PutDeliveryDestinationPolicyResponseTypeDef",
    {
        "policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutDeliveryDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredPutDeliveryDestinationRequestRequestTypeDef",
    {
        "name": str,
        "deliveryDestinationConfiguration": "DeliveryDestinationConfigurationTypeDef",
    },
)
_OptionalPutDeliveryDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalPutDeliveryDestinationRequestRequestTypeDef",
    {
        "outputFormat": OutputFormatType,
        "tags": Dict[str, str],
    },
    total=False,
)

class PutDeliveryDestinationRequestRequestTypeDef(
    _RequiredPutDeliveryDestinationRequestRequestTypeDef,
    _OptionalPutDeliveryDestinationRequestRequestTypeDef,
):
    pass

PutDeliveryDestinationResponseTypeDef = TypedDict(
    "PutDeliveryDestinationResponseTypeDef",
    {
        "deliveryDestination": "DeliveryDestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutDeliverySourceRequestRequestTypeDef = TypedDict(
    "_RequiredPutDeliverySourceRequestRequestTypeDef",
    {
        "name": str,
        "resourceArn": str,
        "logType": str,
    },
)
_OptionalPutDeliverySourceRequestRequestTypeDef = TypedDict(
    "_OptionalPutDeliverySourceRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class PutDeliverySourceRequestRequestTypeDef(
    _RequiredPutDeliverySourceRequestRequestTypeDef, _OptionalPutDeliverySourceRequestRequestTypeDef
):
    pass

PutDeliverySourceResponseTypeDef = TypedDict(
    "PutDeliverySourceResponseTypeDef",
    {
        "deliverySource": "DeliverySourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutDestinationPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutDestinationPolicyRequestRequestTypeDef",
    {
        "destinationName": str,
        "accessPolicy": str,
    },
)
_OptionalPutDestinationPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutDestinationPolicyRequestRequestTypeDef",
    {
        "forceUpdate": bool,
    },
    total=False,
)

class PutDestinationPolicyRequestRequestTypeDef(
    _RequiredPutDestinationPolicyRequestRequestTypeDef,
    _OptionalPutDestinationPolicyRequestRequestTypeDef,
):
    pass

_RequiredPutDestinationRequestRequestTypeDef = TypedDict(
    "_RequiredPutDestinationRequestRequestTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
    },
)
_OptionalPutDestinationRequestRequestTypeDef = TypedDict(
    "_OptionalPutDestinationRequestRequestTypeDef",
    {
        "tags": Dict[str, str],
    },
    total=False,
)

class PutDestinationRequestRequestTypeDef(
    _RequiredPutDestinationRequestRequestTypeDef, _OptionalPutDestinationRequestRequestTypeDef
):
    pass

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
        "clientToken": str,
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
        "logGroupIdentifiers": List[str],
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

SuppressionPeriodTypeDef = TypedDict(
    "SuppressionPeriodTypeDef",
    {
        "value": int,
        "suppressionUnit": SuppressionUnitType,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateAnomalyRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateAnomalyRequestRequestTypeDef",
    {
        "anomalyDetectorArn": str,
    },
)
_OptionalUpdateAnomalyRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateAnomalyRequestRequestTypeDef",
    {
        "anomalyId": str,
        "patternId": str,
        "suppressionType": SuppressionTypeType,
        "suppressionPeriod": "SuppressionPeriodTypeDef",
    },
    total=False,
)

class UpdateAnomalyRequestRequestTypeDef(
    _RequiredUpdateAnomalyRequestRequestTypeDef, _OptionalUpdateAnomalyRequestRequestTypeDef
):
    pass

_RequiredUpdateLogAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLogAnomalyDetectorRequestRequestTypeDef",
    {
        "anomalyDetectorArn": str,
        "enabled": bool,
    },
)
_OptionalUpdateLogAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLogAnomalyDetectorRequestRequestTypeDef",
    {
        "evaluationFrequency": EvaluationFrequencyType,
        "filterPattern": str,
        "anomalyVisibilityTime": int,
    },
    total=False,
)

class UpdateLogAnomalyDetectorRequestRequestTypeDef(
    _RequiredUpdateLogAnomalyDetectorRequestRequestTypeDef,
    _OptionalUpdateLogAnomalyDetectorRequestRequestTypeDef,
):
    pass
