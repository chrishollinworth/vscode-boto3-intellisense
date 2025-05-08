"""
Type annotations for logs service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_logs/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_logs.type_defs import AccountPolicyTypeDef

    data: AccountPolicyTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from botocore.eventstream import EventStream

from .literals import (
    AnomalyDetectorStatusType,
    DataProtectionStatusType,
    DeliveryDestinationTypeType,
    DistributionType,
    EntityRejectionErrorTypeType,
    EvaluationFrequencyType,
    ExportTaskStatusCodeType,
    FlattenedElementType,
    IndexSourceType,
    IntegrationStatusType,
    LogGroupClassType,
    OpenSearchResourceStatusTypeType,
    OrderByType,
    OutputFormatType,
    PolicyTypeType,
    QueryLanguageType,
    QueryStatusType,
    StandardUnitType,
    StateType,
    SuppressionStateType,
    SuppressionTypeType,
    SuppressionUnitType,
    TypeType,
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
    "AccountPolicyTypeDef",
    "AddKeyEntryTypeDef",
    "AddKeysOutputTypeDef",
    "AddKeysTypeDef",
    "AddKeysUnionTypeDef",
    "AnomalyDetectorTypeDef",
    "AnomalyTypeDef",
    "AssociateKmsKeyRequestTypeDef",
    "CSVOutputTypeDef",
    "CSVTypeDef",
    "CSVUnionTypeDef",
    "CancelExportTaskRequestTypeDef",
    "ConfigurationTemplateDeliveryConfigValuesTypeDef",
    "ConfigurationTemplateTypeDef",
    "CopyValueEntryTypeDef",
    "CopyValueOutputTypeDef",
    "CopyValueTypeDef",
    "CopyValueUnionTypeDef",
    "CreateDeliveryRequestTypeDef",
    "CreateDeliveryResponseTypeDef",
    "CreateExportTaskRequestTypeDef",
    "CreateExportTaskResponseTypeDef",
    "CreateLogAnomalyDetectorRequestTypeDef",
    "CreateLogAnomalyDetectorResponseTypeDef",
    "CreateLogGroupRequestTypeDef",
    "CreateLogStreamRequestTypeDef",
    "DateTimeConverterOutputTypeDef",
    "DateTimeConverterTypeDef",
    "DateTimeConverterUnionTypeDef",
    "DeleteAccountPolicyRequestTypeDef",
    "DeleteDataProtectionPolicyRequestTypeDef",
    "DeleteDeliveryDestinationPolicyRequestTypeDef",
    "DeleteDeliveryDestinationRequestTypeDef",
    "DeleteDeliveryRequestTypeDef",
    "DeleteDeliverySourceRequestTypeDef",
    "DeleteDestinationRequestTypeDef",
    "DeleteIndexPolicyRequestTypeDef",
    "DeleteIntegrationRequestTypeDef",
    "DeleteKeysOutputTypeDef",
    "DeleteKeysTypeDef",
    "DeleteKeysUnionTypeDef",
    "DeleteLogAnomalyDetectorRequestTypeDef",
    "DeleteLogGroupRequestTypeDef",
    "DeleteLogStreamRequestTypeDef",
    "DeleteMetricFilterRequestTypeDef",
    "DeleteQueryDefinitionRequestTypeDef",
    "DeleteQueryDefinitionResponseTypeDef",
    "DeleteResourcePolicyRequestTypeDef",
    "DeleteRetentionPolicyRequestTypeDef",
    "DeleteSubscriptionFilterRequestTypeDef",
    "DeleteTransformerRequestTypeDef",
    "DeliveryDestinationConfigurationTypeDef",
    "DeliveryDestinationTypeDef",
    "DeliverySourceTypeDef",
    "DeliveryTypeDef",
    "DescribeAccountPoliciesRequestTypeDef",
    "DescribeAccountPoliciesResponseTypeDef",
    "DescribeConfigurationTemplatesRequestPaginateTypeDef",
    "DescribeConfigurationTemplatesRequestTypeDef",
    "DescribeConfigurationTemplatesResponseTypeDef",
    "DescribeDeliveriesRequestPaginateTypeDef",
    "DescribeDeliveriesRequestTypeDef",
    "DescribeDeliveriesResponseTypeDef",
    "DescribeDeliveryDestinationsRequestPaginateTypeDef",
    "DescribeDeliveryDestinationsRequestTypeDef",
    "DescribeDeliveryDestinationsResponseTypeDef",
    "DescribeDeliverySourcesRequestPaginateTypeDef",
    "DescribeDeliverySourcesRequestTypeDef",
    "DescribeDeliverySourcesResponseTypeDef",
    "DescribeDestinationsRequestPaginateTypeDef",
    "DescribeDestinationsRequestTypeDef",
    "DescribeDestinationsResponseTypeDef",
    "DescribeExportTasksRequestPaginateTypeDef",
    "DescribeExportTasksRequestTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeFieldIndexesRequestTypeDef",
    "DescribeFieldIndexesResponseTypeDef",
    "DescribeIndexPoliciesRequestTypeDef",
    "DescribeIndexPoliciesResponseTypeDef",
    "DescribeLogGroupsRequestPaginateTypeDef",
    "DescribeLogGroupsRequestTypeDef",
    "DescribeLogGroupsResponseTypeDef",
    "DescribeLogStreamsRequestPaginateTypeDef",
    "DescribeLogStreamsRequestTypeDef",
    "DescribeLogStreamsResponseTypeDef",
    "DescribeMetricFiltersRequestPaginateTypeDef",
    "DescribeMetricFiltersRequestTypeDef",
    "DescribeMetricFiltersResponseTypeDef",
    "DescribeQueriesRequestPaginateTypeDef",
    "DescribeQueriesRequestTypeDef",
    "DescribeQueriesResponseTypeDef",
    "DescribeQueryDefinitionsRequestTypeDef",
    "DescribeQueryDefinitionsResponseTypeDef",
    "DescribeResourcePoliciesRequestPaginateTypeDef",
    "DescribeResourcePoliciesRequestTypeDef",
    "DescribeResourcePoliciesResponseTypeDef",
    "DescribeSubscriptionFiltersRequestPaginateTypeDef",
    "DescribeSubscriptionFiltersRequestTypeDef",
    "DescribeSubscriptionFiltersResponseTypeDef",
    "DestinationTypeDef",
    "DisassociateKmsKeyRequestTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EntityTypeDef",
    "ExportTaskExecutionInfoTypeDef",
    "ExportTaskStatusTypeDef",
    "ExportTaskTypeDef",
    "FieldIndexTypeDef",
    "FilterLogEventsRequestPaginateTypeDef",
    "FilterLogEventsRequestTypeDef",
    "FilterLogEventsResponseTypeDef",
    "FilteredLogEventTypeDef",
    "GetDataProtectionPolicyRequestTypeDef",
    "GetDataProtectionPolicyResponseTypeDef",
    "GetDeliveryDestinationPolicyRequestTypeDef",
    "GetDeliveryDestinationPolicyResponseTypeDef",
    "GetDeliveryDestinationRequestTypeDef",
    "GetDeliveryDestinationResponseTypeDef",
    "GetDeliveryRequestTypeDef",
    "GetDeliveryResponseTypeDef",
    "GetDeliverySourceRequestTypeDef",
    "GetDeliverySourceResponseTypeDef",
    "GetIntegrationRequestTypeDef",
    "GetIntegrationResponseTypeDef",
    "GetLogAnomalyDetectorRequestTypeDef",
    "GetLogAnomalyDetectorResponseTypeDef",
    "GetLogEventsRequestTypeDef",
    "GetLogEventsResponseTypeDef",
    "GetLogGroupFieldsRequestTypeDef",
    "GetLogGroupFieldsResponseTypeDef",
    "GetLogRecordRequestTypeDef",
    "GetLogRecordResponseTypeDef",
    "GetQueryResultsRequestTypeDef",
    "GetQueryResultsResponseTypeDef",
    "GetTransformerRequestTypeDef",
    "GetTransformerResponseTypeDef",
    "GrokTypeDef",
    "IndexPolicyTypeDef",
    "InputLogEventTypeDef",
    "IntegrationDetailsTypeDef",
    "IntegrationSummaryTypeDef",
    "ListAnomaliesRequestPaginateTypeDef",
    "ListAnomaliesRequestTypeDef",
    "ListAnomaliesResponseTypeDef",
    "ListIntegrationsRequestTypeDef",
    "ListIntegrationsResponseTypeDef",
    "ListLogAnomalyDetectorsRequestPaginateTypeDef",
    "ListLogAnomalyDetectorsRequestTypeDef",
    "ListLogAnomalyDetectorsResponseTypeDef",
    "ListLogGroupsForQueryRequestPaginateTypeDef",
    "ListLogGroupsForQueryRequestTypeDef",
    "ListLogGroupsForQueryResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsLogGroupRequestTypeDef",
    "ListTagsLogGroupResponseTypeDef",
    "ListToMapTypeDef",
    "LiveTailSessionLogEventTypeDef",
    "LiveTailSessionMetadataTypeDef",
    "LiveTailSessionStartTypeDef",
    "LiveTailSessionUpdateTypeDef",
    "LogEventTypeDef",
    "LogGroupFieldTypeDef",
    "LogGroupTypeDef",
    "LogStreamTypeDef",
    "LowerCaseStringOutputTypeDef",
    "LowerCaseStringTypeDef",
    "LowerCaseStringUnionTypeDef",
    "MetricFilterMatchRecordTypeDef",
    "MetricFilterTypeDef",
    "MetricTransformationOutputTypeDef",
    "MetricTransformationTypeDef",
    "MetricTransformationUnionTypeDef",
    "MoveKeyEntryTypeDef",
    "MoveKeysOutputTypeDef",
    "MoveKeysTypeDef",
    "MoveKeysUnionTypeDef",
    "OpenSearchApplicationTypeDef",
    "OpenSearchCollectionTypeDef",
    "OpenSearchDataAccessPolicyTypeDef",
    "OpenSearchDataSourceTypeDef",
    "OpenSearchEncryptionPolicyTypeDef",
    "OpenSearchIntegrationDetailsTypeDef",
    "OpenSearchLifecyclePolicyTypeDef",
    "OpenSearchNetworkPolicyTypeDef",
    "OpenSearchResourceConfigTypeDef",
    "OpenSearchResourceStatusTypeDef",
    "OpenSearchWorkspaceTypeDef",
    "OutputLogEventTypeDef",
    "PaginatorConfigTypeDef",
    "ParseCloudfrontTypeDef",
    "ParseJSONTypeDef",
    "ParseKeyValueTypeDef",
    "ParsePostgresTypeDef",
    "ParseRoute53TypeDef",
    "ParseVPCTypeDef",
    "ParseWAFTypeDef",
    "PatternTokenTypeDef",
    "PolicyTypeDef",
    "ProcessorOutputTypeDef",
    "ProcessorTypeDef",
    "ProcessorUnionTypeDef",
    "PutAccountPolicyRequestTypeDef",
    "PutAccountPolicyResponseTypeDef",
    "PutDataProtectionPolicyRequestTypeDef",
    "PutDataProtectionPolicyResponseTypeDef",
    "PutDeliveryDestinationPolicyRequestTypeDef",
    "PutDeliveryDestinationPolicyResponseTypeDef",
    "PutDeliveryDestinationRequestTypeDef",
    "PutDeliveryDestinationResponseTypeDef",
    "PutDeliverySourceRequestTypeDef",
    "PutDeliverySourceResponseTypeDef",
    "PutDestinationPolicyRequestTypeDef",
    "PutDestinationRequestTypeDef",
    "PutDestinationResponseTypeDef",
    "PutIndexPolicyRequestTypeDef",
    "PutIndexPolicyResponseTypeDef",
    "PutIntegrationRequestTypeDef",
    "PutIntegrationResponseTypeDef",
    "PutLogEventsRequestTypeDef",
    "PutLogEventsResponseTypeDef",
    "PutMetricFilterRequestTypeDef",
    "PutQueryDefinitionRequestTypeDef",
    "PutQueryDefinitionResponseTypeDef",
    "PutResourcePolicyRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutRetentionPolicyRequestTypeDef",
    "PutSubscriptionFilterRequestTypeDef",
    "PutTransformerRequestTypeDef",
    "QueryDefinitionTypeDef",
    "QueryInfoTypeDef",
    "QueryStatisticsTypeDef",
    "RecordFieldTypeDef",
    "RejectedEntityInfoTypeDef",
    "RejectedLogEventsInfoTypeDef",
    "RenameKeyEntryTypeDef",
    "RenameKeysOutputTypeDef",
    "RenameKeysTypeDef",
    "RenameKeysUnionTypeDef",
    "ResourceConfigTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResultFieldTypeDef",
    "S3DeliveryConfigurationTypeDef",
    "SearchedLogStreamTypeDef",
    "SessionStreamingExceptionTypeDef",
    "SessionTimeoutExceptionTypeDef",
    "SplitStringEntryTypeDef",
    "SplitStringOutputTypeDef",
    "SplitStringTypeDef",
    "SplitStringUnionTypeDef",
    "StartLiveTailRequestTypeDef",
    "StartLiveTailResponseStreamTypeDef",
    "StartLiveTailResponseTypeDef",
    "StartQueryRequestTypeDef",
    "StartQueryResponseTypeDef",
    "StopQueryRequestTypeDef",
    "StopQueryResponseTypeDef",
    "SubscriptionFilterTypeDef",
    "SubstituteStringEntryTypeDef",
    "SubstituteStringOutputTypeDef",
    "SubstituteStringTypeDef",
    "SubstituteStringUnionTypeDef",
    "SuppressionPeriodTypeDef",
    "TagLogGroupRequestTypeDef",
    "TagResourceRequestTypeDef",
    "TestMetricFilterRequestTypeDef",
    "TestMetricFilterResponseTypeDef",
    "TestTransformerRequestTypeDef",
    "TestTransformerResponseTypeDef",
    "TransformedLogRecordTypeDef",
    "TrimStringOutputTypeDef",
    "TrimStringTypeDef",
    "TrimStringUnionTypeDef",
    "TypeConverterEntryTypeDef",
    "TypeConverterOutputTypeDef",
    "TypeConverterTypeDef",
    "TypeConverterUnionTypeDef",
    "UntagLogGroupRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateAnomalyRequestTypeDef",
    "UpdateDeliveryConfigurationRequestTypeDef",
    "UpdateLogAnomalyDetectorRequestTypeDef",
    "UpperCaseStringOutputTypeDef",
    "UpperCaseStringTypeDef",
    "UpperCaseStringUnionTypeDef",
)

class AccountPolicyTypeDef(TypedDict):
    policyName: NotRequired[str]
    policyDocument: NotRequired[str]
    lastUpdatedTime: NotRequired[int]
    policyType: NotRequired[PolicyTypeType]
    scope: NotRequired[Literal["ALL"]]
    selectionCriteria: NotRequired[str]
    accountId: NotRequired[str]

class AddKeyEntryTypeDef(TypedDict):
    key: str
    value: str
    overwriteIfExists: NotRequired[bool]

class AnomalyDetectorTypeDef(TypedDict):
    anomalyDetectorArn: NotRequired[str]
    detectorName: NotRequired[str]
    logGroupArnList: NotRequired[List[str]]
    evaluationFrequency: NotRequired[EvaluationFrequencyType]
    filterPattern: NotRequired[str]
    anomalyDetectorStatus: NotRequired[AnomalyDetectorStatusType]
    kmsKeyId: NotRequired[str]
    creationTimeStamp: NotRequired[int]
    lastModifiedTimeStamp: NotRequired[int]
    anomalyVisibilityTime: NotRequired[int]

class LogEventTypeDef(TypedDict):
    timestamp: NotRequired[int]
    message: NotRequired[str]

class PatternTokenTypeDef(TypedDict):
    dynamicTokenPosition: NotRequired[int]
    isDynamic: NotRequired[bool]
    tokenString: NotRequired[str]
    enumerations: NotRequired[Dict[str, int]]
    inferredTokenName: NotRequired[str]

class AssociateKmsKeyRequestTypeDef(TypedDict):
    kmsKeyId: str
    logGroupName: NotRequired[str]
    resourceIdentifier: NotRequired[str]

class CSVOutputTypeDef(TypedDict):
    quoteCharacter: NotRequired[str]
    delimiter: NotRequired[str]
    columns: NotRequired[List[str]]
    source: NotRequired[str]

class CSVTypeDef(TypedDict):
    quoteCharacter: NotRequired[str]
    delimiter: NotRequired[str]
    columns: NotRequired[Sequence[str]]
    source: NotRequired[str]

class CancelExportTaskRequestTypeDef(TypedDict):
    taskId: str

class S3DeliveryConfigurationTypeDef(TypedDict):
    suffixPath: NotRequired[str]
    enableHiveCompatiblePath: NotRequired[bool]

class RecordFieldTypeDef(TypedDict):
    name: NotRequired[str]
    mandatory: NotRequired[bool]

class CopyValueEntryTypeDef(TypedDict):
    source: str
    target: str
    overwriteIfExists: NotRequired[bool]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateExportTaskRequestTypeDef(TypedDict):
    logGroupName: str
    fromTime: int
    to: int
    destination: str
    taskName: NotRequired[str]
    logStreamNamePrefix: NotRequired[str]
    destinationPrefix: NotRequired[str]

class CreateLogAnomalyDetectorRequestTypeDef(TypedDict):
    logGroupArnList: Sequence[str]
    detectorName: NotRequired[str]
    evaluationFrequency: NotRequired[EvaluationFrequencyType]
    filterPattern: NotRequired[str]
    kmsKeyId: NotRequired[str]
    anomalyVisibilityTime: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]

class CreateLogGroupRequestTypeDef(TypedDict):
    logGroupName: str
    kmsKeyId: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    logGroupClass: NotRequired[LogGroupClassType]

class CreateLogStreamRequestTypeDef(TypedDict):
    logGroupName: str
    logStreamName: str

class DateTimeConverterOutputTypeDef(TypedDict):
    source: str
    target: str
    matchPatterns: List[str]
    targetFormat: NotRequired[str]
    sourceTimezone: NotRequired[str]
    targetTimezone: NotRequired[str]
    locale: NotRequired[str]

class DateTimeConverterTypeDef(TypedDict):
    source: str
    target: str
    matchPatterns: Sequence[str]
    targetFormat: NotRequired[str]
    sourceTimezone: NotRequired[str]
    targetTimezone: NotRequired[str]
    locale: NotRequired[str]

class DeleteAccountPolicyRequestTypeDef(TypedDict):
    policyName: str
    policyType: PolicyTypeType

class DeleteDataProtectionPolicyRequestTypeDef(TypedDict):
    logGroupIdentifier: str

class DeleteDeliveryDestinationPolicyRequestTypeDef(TypedDict):
    deliveryDestinationName: str

class DeleteDeliveryDestinationRequestTypeDef(TypedDict):
    name: str

DeleteDeliveryRequestTypeDef = TypedDict(
    "DeleteDeliveryRequestTypeDef",
    {
        "id": str,
    },
)

class DeleteDeliverySourceRequestTypeDef(TypedDict):
    name: str

class DeleteDestinationRequestTypeDef(TypedDict):
    destinationName: str

class DeleteIndexPolicyRequestTypeDef(TypedDict):
    logGroupIdentifier: str

class DeleteIntegrationRequestTypeDef(TypedDict):
    integrationName: str
    force: NotRequired[bool]

class DeleteKeysOutputTypeDef(TypedDict):
    withKeys: List[str]

class DeleteKeysTypeDef(TypedDict):
    withKeys: Sequence[str]

class DeleteLogAnomalyDetectorRequestTypeDef(TypedDict):
    anomalyDetectorArn: str

class DeleteLogGroupRequestTypeDef(TypedDict):
    logGroupName: str

class DeleteLogStreamRequestTypeDef(TypedDict):
    logGroupName: str
    logStreamName: str

class DeleteMetricFilterRequestTypeDef(TypedDict):
    logGroupName: str
    filterName: str

class DeleteQueryDefinitionRequestTypeDef(TypedDict):
    queryDefinitionId: str

class DeleteResourcePolicyRequestTypeDef(TypedDict):
    policyName: NotRequired[str]

class DeleteRetentionPolicyRequestTypeDef(TypedDict):
    logGroupName: str

class DeleteSubscriptionFilterRequestTypeDef(TypedDict):
    logGroupName: str
    filterName: str

class DeleteTransformerRequestTypeDef(TypedDict):
    logGroupIdentifier: str

class DeliveryDestinationConfigurationTypeDef(TypedDict):
    destinationResourceArn: str

class DeliverySourceTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    resourceArns: NotRequired[List[str]]
    service: NotRequired[str]
    logType: NotRequired[str]
    tags: NotRequired[Dict[str, str]]

class DescribeAccountPoliciesRequestTypeDef(TypedDict):
    policyType: PolicyTypeType
    policyName: NotRequired[str]
    accountIdentifiers: NotRequired[Sequence[str]]
    nextToken: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeConfigurationTemplatesRequestTypeDef(TypedDict):
    service: NotRequired[str]
    logTypes: NotRequired[Sequence[str]]
    resourceTypes: NotRequired[Sequence[str]]
    deliveryDestinationTypes: NotRequired[Sequence[DeliveryDestinationTypeType]]
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class DescribeDeliveriesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class DescribeDeliveryDestinationsRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class DescribeDeliverySourcesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class DescribeDestinationsRequestTypeDef(TypedDict):
    DestinationNamePrefix: NotRequired[str]
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class DestinationTypeDef(TypedDict):
    destinationName: NotRequired[str]
    targetArn: NotRequired[str]
    roleArn: NotRequired[str]
    accessPolicy: NotRequired[str]
    arn: NotRequired[str]
    creationTime: NotRequired[int]

class DescribeExportTasksRequestTypeDef(TypedDict):
    taskId: NotRequired[str]
    statusCode: NotRequired[ExportTaskStatusCodeType]
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class DescribeFieldIndexesRequestTypeDef(TypedDict):
    logGroupIdentifiers: Sequence[str]
    nextToken: NotRequired[str]

class FieldIndexTypeDef(TypedDict):
    logGroupIdentifier: NotRequired[str]
    fieldIndexName: NotRequired[str]
    lastScanTime: NotRequired[int]
    firstEventTime: NotRequired[int]
    lastEventTime: NotRequired[int]

class DescribeIndexPoliciesRequestTypeDef(TypedDict):
    logGroupIdentifiers: Sequence[str]
    nextToken: NotRequired[str]

class IndexPolicyTypeDef(TypedDict):
    logGroupIdentifier: NotRequired[str]
    lastUpdateTime: NotRequired[int]
    policyDocument: NotRequired[str]
    policyName: NotRequired[str]
    source: NotRequired[IndexSourceType]

class DescribeLogGroupsRequestTypeDef(TypedDict):
    accountIdentifiers: NotRequired[Sequence[str]]
    logGroupNamePrefix: NotRequired[str]
    logGroupNamePattern: NotRequired[str]
    nextToken: NotRequired[str]
    limit: NotRequired[int]
    includeLinkedAccounts: NotRequired[bool]
    logGroupClass: NotRequired[LogGroupClassType]

class LogGroupTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    creationTime: NotRequired[int]
    retentionInDays: NotRequired[int]
    metricFilterCount: NotRequired[int]
    arn: NotRequired[str]
    storedBytes: NotRequired[int]
    kmsKeyId: NotRequired[str]
    dataProtectionStatus: NotRequired[DataProtectionStatusType]
    inheritedProperties: NotRequired[List[Literal["ACCOUNT_DATA_PROTECTION"]]]
    logGroupClass: NotRequired[LogGroupClassType]
    logGroupArn: NotRequired[str]

class DescribeLogStreamsRequestTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    logGroupIdentifier: NotRequired[str]
    logStreamNamePrefix: NotRequired[str]
    orderBy: NotRequired[OrderByType]
    descending: NotRequired[bool]
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class LogStreamTypeDef(TypedDict):
    logStreamName: NotRequired[str]
    creationTime: NotRequired[int]
    firstEventTimestamp: NotRequired[int]
    lastEventTimestamp: NotRequired[int]
    lastIngestionTime: NotRequired[int]
    uploadSequenceToken: NotRequired[str]
    arn: NotRequired[str]
    storedBytes: NotRequired[int]

class DescribeMetricFiltersRequestTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    filterNamePrefix: NotRequired[str]
    nextToken: NotRequired[str]
    limit: NotRequired[int]
    metricName: NotRequired[str]
    metricNamespace: NotRequired[str]

class DescribeQueriesRequestTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    status: NotRequired[QueryStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    queryLanguage: NotRequired[QueryLanguageType]

class QueryInfoTypeDef(TypedDict):
    queryLanguage: NotRequired[QueryLanguageType]
    queryId: NotRequired[str]
    queryString: NotRequired[str]
    status: NotRequired[QueryStatusType]
    createTime: NotRequired[int]
    logGroupName: NotRequired[str]

class DescribeQueryDefinitionsRequestTypeDef(TypedDict):
    queryLanguage: NotRequired[QueryLanguageType]
    queryDefinitionNamePrefix: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class QueryDefinitionTypeDef(TypedDict):
    queryLanguage: NotRequired[QueryLanguageType]
    queryDefinitionId: NotRequired[str]
    name: NotRequired[str]
    queryString: NotRequired[str]
    lastModified: NotRequired[int]
    logGroupNames: NotRequired[List[str]]

class DescribeResourcePoliciesRequestTypeDef(TypedDict):
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class ResourcePolicyTypeDef(TypedDict):
    policyName: NotRequired[str]
    policyDocument: NotRequired[str]
    lastUpdatedTime: NotRequired[int]

class DescribeSubscriptionFiltersRequestTypeDef(TypedDict):
    logGroupName: str
    filterNamePrefix: NotRequired[str]
    nextToken: NotRequired[str]
    limit: NotRequired[int]

class SubscriptionFilterTypeDef(TypedDict):
    filterName: NotRequired[str]
    logGroupName: NotRequired[str]
    filterPattern: NotRequired[str]
    destinationArn: NotRequired[str]
    roleArn: NotRequired[str]
    distribution: NotRequired[DistributionType]
    applyOnTransformedLogs: NotRequired[bool]
    creationTime: NotRequired[int]

class DisassociateKmsKeyRequestTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    resourceIdentifier: NotRequired[str]

class EntityTypeDef(TypedDict):
    keyAttributes: NotRequired[Mapping[str, str]]
    attributes: NotRequired[Mapping[str, str]]

class ExportTaskExecutionInfoTypeDef(TypedDict):
    creationTime: NotRequired[int]
    completionTime: NotRequired[int]

class ExportTaskStatusTypeDef(TypedDict):
    code: NotRequired[ExportTaskStatusCodeType]
    message: NotRequired[str]

class FilterLogEventsRequestTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    logGroupIdentifier: NotRequired[str]
    logStreamNames: NotRequired[Sequence[str]]
    logStreamNamePrefix: NotRequired[str]
    startTime: NotRequired[int]
    endTime: NotRequired[int]
    filterPattern: NotRequired[str]
    nextToken: NotRequired[str]
    limit: NotRequired[int]
    interleaved: NotRequired[bool]
    unmask: NotRequired[bool]

class FilteredLogEventTypeDef(TypedDict):
    logStreamName: NotRequired[str]
    timestamp: NotRequired[int]
    message: NotRequired[str]
    ingestionTime: NotRequired[int]
    eventId: NotRequired[str]

class SearchedLogStreamTypeDef(TypedDict):
    logStreamName: NotRequired[str]
    searchedCompletely: NotRequired[bool]

class GetDataProtectionPolicyRequestTypeDef(TypedDict):
    logGroupIdentifier: str

class GetDeliveryDestinationPolicyRequestTypeDef(TypedDict):
    deliveryDestinationName: str

class PolicyTypeDef(TypedDict):
    deliveryDestinationPolicy: NotRequired[str]

class GetDeliveryDestinationRequestTypeDef(TypedDict):
    name: str

GetDeliveryRequestTypeDef = TypedDict(
    "GetDeliveryRequestTypeDef",
    {
        "id": str,
    },
)

class GetDeliverySourceRequestTypeDef(TypedDict):
    name: str

class GetIntegrationRequestTypeDef(TypedDict):
    integrationName: str

class GetLogAnomalyDetectorRequestTypeDef(TypedDict):
    anomalyDetectorArn: str

class GetLogEventsRequestTypeDef(TypedDict):
    logStreamName: str
    logGroupName: NotRequired[str]
    logGroupIdentifier: NotRequired[str]
    startTime: NotRequired[int]
    endTime: NotRequired[int]
    nextToken: NotRequired[str]
    limit: NotRequired[int]
    startFromHead: NotRequired[bool]
    unmask: NotRequired[bool]

class OutputLogEventTypeDef(TypedDict):
    timestamp: NotRequired[int]
    message: NotRequired[str]
    ingestionTime: NotRequired[int]

class GetLogGroupFieldsRequestTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    time: NotRequired[int]
    logGroupIdentifier: NotRequired[str]

class LogGroupFieldTypeDef(TypedDict):
    name: NotRequired[str]
    percent: NotRequired[int]

class GetLogRecordRequestTypeDef(TypedDict):
    logRecordPointer: str
    unmask: NotRequired[bool]

class GetQueryResultsRequestTypeDef(TypedDict):
    queryId: str

class QueryStatisticsTypeDef(TypedDict):
    recordsMatched: NotRequired[float]
    recordsScanned: NotRequired[float]
    estimatedRecordsSkipped: NotRequired[float]
    bytesScanned: NotRequired[float]
    estimatedBytesSkipped: NotRequired[float]
    logGroupsScanned: NotRequired[float]

class ResultFieldTypeDef(TypedDict):
    field: NotRequired[str]
    value: NotRequired[str]

class GetTransformerRequestTypeDef(TypedDict):
    logGroupIdentifier: str

class GrokTypeDef(TypedDict):
    match: str
    source: NotRequired[str]

class InputLogEventTypeDef(TypedDict):
    timestamp: int
    message: str

class IntegrationSummaryTypeDef(TypedDict):
    integrationName: NotRequired[str]
    integrationType: NotRequired[Literal["OPENSEARCH"]]
    integrationStatus: NotRequired[IntegrationStatusType]

class ListAnomaliesRequestTypeDef(TypedDict):
    anomalyDetectorArn: NotRequired[str]
    suppressionState: NotRequired[SuppressionStateType]
    limit: NotRequired[int]
    nextToken: NotRequired[str]

class ListIntegrationsRequestTypeDef(TypedDict):
    integrationNamePrefix: NotRequired[str]
    integrationType: NotRequired[Literal["OPENSEARCH"]]
    integrationStatus: NotRequired[IntegrationStatusType]

class ListLogAnomalyDetectorsRequestTypeDef(TypedDict):
    filterLogGroupArn: NotRequired[str]
    limit: NotRequired[int]
    nextToken: NotRequired[str]

class ListLogGroupsForQueryRequestTypeDef(TypedDict):
    queryId: str
    nextToken: NotRequired[str]
    maxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class ListTagsLogGroupRequestTypeDef(TypedDict):
    logGroupName: str

class ListToMapTypeDef(TypedDict):
    source: str
    key: str
    valueKey: NotRequired[str]
    target: NotRequired[str]
    flatten: NotRequired[bool]
    flattenedElement: NotRequired[FlattenedElementType]

class LiveTailSessionLogEventTypeDef(TypedDict):
    logStreamName: NotRequired[str]
    logGroupIdentifier: NotRequired[str]
    message: NotRequired[str]
    timestamp: NotRequired[int]
    ingestionTime: NotRequired[int]

class LiveTailSessionMetadataTypeDef(TypedDict):
    sampled: NotRequired[bool]

class LiveTailSessionStartTypeDef(TypedDict):
    requestId: NotRequired[str]
    sessionId: NotRequired[str]
    logGroupIdentifiers: NotRequired[List[str]]
    logStreamNames: NotRequired[List[str]]
    logStreamNamePrefixes: NotRequired[List[str]]
    logEventFilterPattern: NotRequired[str]

class LowerCaseStringOutputTypeDef(TypedDict):
    withKeys: List[str]

class LowerCaseStringTypeDef(TypedDict):
    withKeys: Sequence[str]

class MetricFilterMatchRecordTypeDef(TypedDict):
    eventNumber: NotRequired[int]
    eventMessage: NotRequired[str]
    extractedValues: NotRequired[Dict[str, str]]

class MetricTransformationOutputTypeDef(TypedDict):
    metricName: str
    metricNamespace: str
    metricValue: str
    defaultValue: NotRequired[float]
    dimensions: NotRequired[Dict[str, str]]
    unit: NotRequired[StandardUnitType]

class MetricTransformationTypeDef(TypedDict):
    metricName: str
    metricNamespace: str
    metricValue: str
    defaultValue: NotRequired[float]
    dimensions: NotRequired[Mapping[str, str]]
    unit: NotRequired[StandardUnitType]

class MoveKeyEntryTypeDef(TypedDict):
    source: str
    target: str
    overwriteIfExists: NotRequired[bool]

class OpenSearchResourceStatusTypeDef(TypedDict):
    status: NotRequired[OpenSearchResourceStatusTypeType]
    statusMessage: NotRequired[str]

class OpenSearchResourceConfigTypeDef(TypedDict):
    dataSourceRoleArn: str
    dashboardViewerPrincipals: Sequence[str]
    retentionDays: int
    kmsKeyArn: NotRequired[str]
    applicationArn: NotRequired[str]

class ParseCloudfrontTypeDef(TypedDict):
    source: NotRequired[str]

class ParseJSONTypeDef(TypedDict):
    source: NotRequired[str]
    destination: NotRequired[str]

class ParseKeyValueTypeDef(TypedDict):
    source: NotRequired[str]
    destination: NotRequired[str]
    fieldDelimiter: NotRequired[str]
    keyValueDelimiter: NotRequired[str]
    keyPrefix: NotRequired[str]
    nonMatchValue: NotRequired[str]
    overwriteIfExists: NotRequired[bool]

class ParsePostgresTypeDef(TypedDict):
    source: NotRequired[str]

class ParseRoute53TypeDef(TypedDict):
    source: NotRequired[str]

class ParseVPCTypeDef(TypedDict):
    source: NotRequired[str]

class ParseWAFTypeDef(TypedDict):
    source: NotRequired[str]

class TrimStringOutputTypeDef(TypedDict):
    withKeys: List[str]

class UpperCaseStringOutputTypeDef(TypedDict):
    withKeys: List[str]

class PutAccountPolicyRequestTypeDef(TypedDict):
    policyName: str
    policyDocument: str
    policyType: PolicyTypeType
    scope: NotRequired[Literal["ALL"]]
    selectionCriteria: NotRequired[str]

class PutDataProtectionPolicyRequestTypeDef(TypedDict):
    logGroupIdentifier: str
    policyDocument: str

class PutDeliveryDestinationPolicyRequestTypeDef(TypedDict):
    deliveryDestinationName: str
    deliveryDestinationPolicy: str

class PutDeliverySourceRequestTypeDef(TypedDict):
    name: str
    resourceArn: str
    logType: str
    tags: NotRequired[Mapping[str, str]]

class PutDestinationPolicyRequestTypeDef(TypedDict):
    destinationName: str
    accessPolicy: str
    forceUpdate: NotRequired[bool]

class PutDestinationRequestTypeDef(TypedDict):
    destinationName: str
    targetArn: str
    roleArn: str
    tags: NotRequired[Mapping[str, str]]

class PutIndexPolicyRequestTypeDef(TypedDict):
    logGroupIdentifier: str
    policyDocument: str

class RejectedEntityInfoTypeDef(TypedDict):
    errorType: EntityRejectionErrorTypeType

class RejectedLogEventsInfoTypeDef(TypedDict):
    tooNewLogEventStartIndex: NotRequired[int]
    tooOldLogEventEndIndex: NotRequired[int]
    expiredLogEventEndIndex: NotRequired[int]

class PutQueryDefinitionRequestTypeDef(TypedDict):
    name: str
    queryString: str
    queryLanguage: NotRequired[QueryLanguageType]
    queryDefinitionId: NotRequired[str]
    logGroupNames: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]

class PutResourcePolicyRequestTypeDef(TypedDict):
    policyName: NotRequired[str]
    policyDocument: NotRequired[str]

class PutRetentionPolicyRequestTypeDef(TypedDict):
    logGroupName: str
    retentionInDays: int

class PutSubscriptionFilterRequestTypeDef(TypedDict):
    logGroupName: str
    filterName: str
    filterPattern: str
    destinationArn: str
    roleArn: NotRequired[str]
    distribution: NotRequired[DistributionType]
    applyOnTransformedLogs: NotRequired[bool]

class RenameKeyEntryTypeDef(TypedDict):
    key: str
    renameTo: str
    overwriteIfExists: NotRequired[bool]

class SessionStreamingExceptionTypeDef(TypedDict):
    message: NotRequired[str]

class SessionTimeoutExceptionTypeDef(TypedDict):
    message: NotRequired[str]

class SplitStringEntryTypeDef(TypedDict):
    source: str
    delimiter: str

class StartLiveTailRequestTypeDef(TypedDict):
    logGroupIdentifiers: Sequence[str]
    logStreamNames: NotRequired[Sequence[str]]
    logStreamNamePrefixes: NotRequired[Sequence[str]]
    logEventFilterPattern: NotRequired[str]

class StartQueryRequestTypeDef(TypedDict):
    startTime: int
    endTime: int
    queryString: str
    queryLanguage: NotRequired[QueryLanguageType]
    logGroupName: NotRequired[str]
    logGroupNames: NotRequired[Sequence[str]]
    logGroupIdentifiers: NotRequired[Sequence[str]]
    limit: NotRequired[int]

class StopQueryRequestTypeDef(TypedDict):
    queryId: str

SubstituteStringEntryTypeDef = TypedDict(
    "SubstituteStringEntryTypeDef",
    {
        "source": str,
        "from": str,
        "to": str,
    },
)

class SuppressionPeriodTypeDef(TypedDict):
    value: NotRequired[int]
    suppressionUnit: NotRequired[SuppressionUnitType]

class TagLogGroupRequestTypeDef(TypedDict):
    logGroupName: str
    tags: Mapping[str, str]

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class TestMetricFilterRequestTypeDef(TypedDict):
    filterPattern: str
    logEventMessages: Sequence[str]

class TransformedLogRecordTypeDef(TypedDict):
    eventNumber: NotRequired[int]
    eventMessage: NotRequired[str]
    transformedEventMessage: NotRequired[str]

class TrimStringTypeDef(TypedDict):
    withKeys: Sequence[str]

TypeConverterEntryTypeDef = TypedDict(
    "TypeConverterEntryTypeDef",
    {
        "key": str,
        "type": TypeType,
    },
)

class UntagLogGroupRequestTypeDef(TypedDict):
    logGroupName: str
    tags: Sequence[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLogAnomalyDetectorRequestTypeDef(TypedDict):
    anomalyDetectorArn: str
    enabled: bool
    evaluationFrequency: NotRequired[EvaluationFrequencyType]
    filterPattern: NotRequired[str]
    anomalyVisibilityTime: NotRequired[int]

class UpperCaseStringTypeDef(TypedDict):
    withKeys: Sequence[str]

class AddKeysOutputTypeDef(TypedDict):
    entries: List[AddKeyEntryTypeDef]

class AddKeysTypeDef(TypedDict):
    entries: Sequence[AddKeyEntryTypeDef]

class AnomalyTypeDef(TypedDict):
    anomalyId: str
    patternId: str
    anomalyDetectorArn: str
    patternString: str
    firstSeen: int
    lastSeen: int
    description: str
    active: bool
    state: StateType
    histogram: Dict[str, int]
    logSamples: List[LogEventTypeDef]
    patternTokens: List[PatternTokenTypeDef]
    logGroupArnList: List[str]
    patternRegex: NotRequired[str]
    priority: NotRequired[str]
    suppressed: NotRequired[bool]
    suppressedDate: NotRequired[int]
    suppressedUntil: NotRequired[int]
    isPatternLevelSuppression: NotRequired[bool]

CSVUnionTypeDef = Union[CSVTypeDef, CSVOutputTypeDef]

class ConfigurationTemplateDeliveryConfigValuesTypeDef(TypedDict):
    recordFields: NotRequired[List[str]]
    fieldDelimiter: NotRequired[str]
    s3DeliveryConfiguration: NotRequired[S3DeliveryConfigurationTypeDef]

class CreateDeliveryRequestTypeDef(TypedDict):
    deliverySourceName: str
    deliveryDestinationArn: str
    recordFields: NotRequired[Sequence[str]]
    fieldDelimiter: NotRequired[str]
    s3DeliveryConfiguration: NotRequired[S3DeliveryConfigurationTypeDef]
    tags: NotRequired[Mapping[str, str]]

DeliveryTypeDef = TypedDict(
    "DeliveryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "deliverySourceName": NotRequired[str],
        "deliveryDestinationArn": NotRequired[str],
        "deliveryDestinationType": NotRequired[DeliveryDestinationTypeType],
        "recordFields": NotRequired[List[str]],
        "fieldDelimiter": NotRequired[str],
        "s3DeliveryConfiguration": NotRequired[S3DeliveryConfigurationTypeDef],
        "tags": NotRequired[Dict[str, str]],
    },
)
UpdateDeliveryConfigurationRequestTypeDef = TypedDict(
    "UpdateDeliveryConfigurationRequestTypeDef",
    {
        "id": str,
        "recordFields": NotRequired[Sequence[str]],
        "fieldDelimiter": NotRequired[str],
        "s3DeliveryConfiguration": NotRequired[S3DeliveryConfigurationTypeDef],
    },
)

class CopyValueOutputTypeDef(TypedDict):
    entries: List[CopyValueEntryTypeDef]

class CopyValueTypeDef(TypedDict):
    entries: Sequence[CopyValueEntryTypeDef]

class CreateExportTaskResponseTypeDef(TypedDict):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLogAnomalyDetectorResponseTypeDef(TypedDict):
    anomalyDetectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteQueryDefinitionResponseTypeDef(TypedDict):
    success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountPoliciesResponseTypeDef(TypedDict):
    accountPolicies: List[AccountPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataProtectionPolicyResponseTypeDef(TypedDict):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetLogAnomalyDetectorResponseTypeDef(TypedDict):
    detectorName: str
    logGroupArnList: List[str]
    evaluationFrequency: EvaluationFrequencyType
    filterPattern: str
    anomalyDetectorStatus: AnomalyDetectorStatusType
    kmsKeyId: str
    creationTimeStamp: int
    lastModifiedTimeStamp: int
    anomalyVisibilityTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetLogRecordResponseTypeDef(TypedDict):
    logRecord: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLogAnomalyDetectorsResponseTypeDef(TypedDict):
    anomalyDetectors: List[AnomalyDetectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListLogGroupsForQueryResponseTypeDef(TypedDict):
    logGroupIdentifiers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsLogGroupResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountPolicyResponseTypeDef(TypedDict):
    accountPolicy: AccountPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataProtectionPolicyResponseTypeDef(TypedDict):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutIntegrationResponseTypeDef(TypedDict):
    integrationName: str
    integrationStatus: IntegrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PutQueryDefinitionResponseTypeDef(TypedDict):
    queryDefinitionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryResponseTypeDef(TypedDict):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopQueryResponseTypeDef(TypedDict):
    success: bool
    ResponseMetadata: ResponseMetadataTypeDef

DateTimeConverterUnionTypeDef = Union[DateTimeConverterTypeDef, DateTimeConverterOutputTypeDef]
DeleteKeysUnionTypeDef = Union[DeleteKeysTypeDef, DeleteKeysOutputTypeDef]

class DeliveryDestinationTypeDef(TypedDict):
    name: NotRequired[str]
    arn: NotRequired[str]
    deliveryDestinationType: NotRequired[DeliveryDestinationTypeType]
    outputFormat: NotRequired[OutputFormatType]
    deliveryDestinationConfiguration: NotRequired[DeliveryDestinationConfigurationTypeDef]
    tags: NotRequired[Dict[str, str]]

class PutDeliveryDestinationRequestTypeDef(TypedDict):
    name: str
    deliveryDestinationConfiguration: DeliveryDestinationConfigurationTypeDef
    outputFormat: NotRequired[OutputFormatType]
    tags: NotRequired[Mapping[str, str]]

class DescribeDeliverySourcesResponseTypeDef(TypedDict):
    deliverySources: List[DeliverySourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetDeliverySourceResponseTypeDef(TypedDict):
    deliverySource: DeliverySourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliverySourceResponseTypeDef(TypedDict):
    deliverySource: DeliverySourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationTemplatesRequestPaginateTypeDef(TypedDict):
    service: NotRequired[str]
    logTypes: NotRequired[Sequence[str]]
    resourceTypes: NotRequired[Sequence[str]]
    deliveryDestinationTypes: NotRequired[Sequence[DeliveryDestinationTypeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDeliveriesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDeliveryDestinationsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDeliverySourcesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDestinationsRequestPaginateTypeDef(TypedDict):
    DestinationNamePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeExportTasksRequestPaginateTypeDef(TypedDict):
    taskId: NotRequired[str]
    statusCode: NotRequired[ExportTaskStatusCodeType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeLogGroupsRequestPaginateTypeDef(TypedDict):
    accountIdentifiers: NotRequired[Sequence[str]]
    logGroupNamePrefix: NotRequired[str]
    logGroupNamePattern: NotRequired[str]
    includeLinkedAccounts: NotRequired[bool]
    logGroupClass: NotRequired[LogGroupClassType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeLogStreamsRequestPaginateTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    logGroupIdentifier: NotRequired[str]
    logStreamNamePrefix: NotRequired[str]
    orderBy: NotRequired[OrderByType]
    descending: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeMetricFiltersRequestPaginateTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    filterNamePrefix: NotRequired[str]
    metricName: NotRequired[str]
    metricNamespace: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeQueriesRequestPaginateTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    status: NotRequired[QueryStatusType]
    queryLanguage: NotRequired[QueryLanguageType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeResourcePoliciesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeSubscriptionFiltersRequestPaginateTypeDef(TypedDict):
    logGroupName: str
    filterNamePrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class FilterLogEventsRequestPaginateTypeDef(TypedDict):
    logGroupName: NotRequired[str]
    logGroupIdentifier: NotRequired[str]
    logStreamNames: NotRequired[Sequence[str]]
    logStreamNamePrefix: NotRequired[str]
    startTime: NotRequired[int]
    endTime: NotRequired[int]
    filterPattern: NotRequired[str]
    interleaved: NotRequired[bool]
    unmask: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAnomaliesRequestPaginateTypeDef(TypedDict):
    anomalyDetectorArn: NotRequired[str]
    suppressionState: NotRequired[SuppressionStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLogAnomalyDetectorsRequestPaginateTypeDef(TypedDict):
    filterLogGroupArn: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListLogGroupsForQueryRequestPaginateTypeDef(TypedDict):
    queryId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeDestinationsResponseTypeDef(TypedDict):
    destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutDestinationResponseTypeDef(TypedDict):
    destination: DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFieldIndexesResponseTypeDef(TypedDict):
    fieldIndexes: List[FieldIndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeIndexPoliciesResponseTypeDef(TypedDict):
    indexPolicies: List[IndexPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutIndexPolicyResponseTypeDef(TypedDict):
    indexPolicy: IndexPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLogGroupsResponseTypeDef(TypedDict):
    logGroups: List[LogGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeLogStreamsResponseTypeDef(TypedDict):
    logStreams: List[LogStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeQueriesResponseTypeDef(TypedDict):
    queries: List[QueryInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeQueryDefinitionsResponseTypeDef(TypedDict):
    queryDefinitions: List[QueryDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class DescribeResourcePoliciesResponseTypeDef(TypedDict):
    resourcePolicies: List[ResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutResourcePolicyResponseTypeDef(TypedDict):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubscriptionFiltersResponseTypeDef(TypedDict):
    subscriptionFilters: List[SubscriptionFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "taskId": NotRequired[str],
        "taskName": NotRequired[str],
        "logGroupName": NotRequired[str],
        "from": NotRequired[int],
        "to": NotRequired[int],
        "destination": NotRequired[str],
        "destinationPrefix": NotRequired[str],
        "status": NotRequired[ExportTaskStatusTypeDef],
        "executionInfo": NotRequired[ExportTaskExecutionInfoTypeDef],
    },
)

class FilterLogEventsResponseTypeDef(TypedDict):
    events: List[FilteredLogEventTypeDef]
    searchedLogStreams: List[SearchedLogStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetDeliveryDestinationPolicyResponseTypeDef(TypedDict):
    policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliveryDestinationPolicyResponseTypeDef(TypedDict):
    policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLogEventsResponseTypeDef(TypedDict):
    events: List[OutputLogEventTypeDef]
    nextForwardToken: str
    nextBackwardToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLogGroupFieldsResponseTypeDef(TypedDict):
    logGroupFields: List[LogGroupFieldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryResultsResponseTypeDef(TypedDict):
    queryLanguage: QueryLanguageType
    results: List[List[ResultFieldTypeDef]]
    statistics: QueryStatisticsTypeDef
    status: QueryStatusType
    encryptionKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutLogEventsRequestTypeDef(TypedDict):
    logGroupName: str
    logStreamName: str
    logEvents: Sequence[InputLogEventTypeDef]
    sequenceToken: NotRequired[str]
    entity: NotRequired[EntityTypeDef]

class ListIntegrationsResponseTypeDef(TypedDict):
    integrationSummaries: List[IntegrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LiveTailSessionUpdateTypeDef(TypedDict):
    sessionMetadata: NotRequired[LiveTailSessionMetadataTypeDef]
    sessionResults: NotRequired[List[LiveTailSessionLogEventTypeDef]]

LowerCaseStringUnionTypeDef = Union[LowerCaseStringTypeDef, LowerCaseStringOutputTypeDef]

class TestMetricFilterResponseTypeDef(TypedDict):
    matches: List[MetricFilterMatchRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricFilterTypeDef(TypedDict):
    filterName: NotRequired[str]
    filterPattern: NotRequired[str]
    metricTransformations: NotRequired[List[MetricTransformationOutputTypeDef]]
    creationTime: NotRequired[int]
    logGroupName: NotRequired[str]
    applyOnTransformedLogs: NotRequired[bool]

MetricTransformationUnionTypeDef = Union[
    MetricTransformationTypeDef, MetricTransformationOutputTypeDef
]

class MoveKeysOutputTypeDef(TypedDict):
    entries: List[MoveKeyEntryTypeDef]

class MoveKeysTypeDef(TypedDict):
    entries: Sequence[MoveKeyEntryTypeDef]

class OpenSearchApplicationTypeDef(TypedDict):
    applicationEndpoint: NotRequired[str]
    applicationArn: NotRequired[str]
    applicationId: NotRequired[str]
    status: NotRequired[OpenSearchResourceStatusTypeDef]

class OpenSearchCollectionTypeDef(TypedDict):
    collectionEndpoint: NotRequired[str]
    collectionArn: NotRequired[str]
    status: NotRequired[OpenSearchResourceStatusTypeDef]

class OpenSearchDataAccessPolicyTypeDef(TypedDict):
    policyName: NotRequired[str]
    status: NotRequired[OpenSearchResourceStatusTypeDef]

class OpenSearchDataSourceTypeDef(TypedDict):
    dataSourceName: NotRequired[str]
    status: NotRequired[OpenSearchResourceStatusTypeDef]

class OpenSearchEncryptionPolicyTypeDef(TypedDict):
    policyName: NotRequired[str]
    status: NotRequired[OpenSearchResourceStatusTypeDef]

class OpenSearchLifecyclePolicyTypeDef(TypedDict):
    policyName: NotRequired[str]
    status: NotRequired[OpenSearchResourceStatusTypeDef]

class OpenSearchNetworkPolicyTypeDef(TypedDict):
    policyName: NotRequired[str]
    status: NotRequired[OpenSearchResourceStatusTypeDef]

class OpenSearchWorkspaceTypeDef(TypedDict):
    workspaceId: NotRequired[str]
    status: NotRequired[OpenSearchResourceStatusTypeDef]

class ResourceConfigTypeDef(TypedDict):
    openSearchResourceConfig: NotRequired[OpenSearchResourceConfigTypeDef]

class PutLogEventsResponseTypeDef(TypedDict):
    nextSequenceToken: str
    rejectedLogEventsInfo: RejectedLogEventsInfoTypeDef
    rejectedEntityInfo: RejectedEntityInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RenameKeysOutputTypeDef(TypedDict):
    entries: List[RenameKeyEntryTypeDef]

class RenameKeysTypeDef(TypedDict):
    entries: Sequence[RenameKeyEntryTypeDef]

class SplitStringOutputTypeDef(TypedDict):
    entries: List[SplitStringEntryTypeDef]

class SplitStringTypeDef(TypedDict):
    entries: Sequence[SplitStringEntryTypeDef]

class SubstituteStringOutputTypeDef(TypedDict):
    entries: List[SubstituteStringEntryTypeDef]

class SubstituteStringTypeDef(TypedDict):
    entries: Sequence[SubstituteStringEntryTypeDef]

class UpdateAnomalyRequestTypeDef(TypedDict):
    anomalyDetectorArn: str
    anomalyId: NotRequired[str]
    patternId: NotRequired[str]
    suppressionType: NotRequired[SuppressionTypeType]
    suppressionPeriod: NotRequired[SuppressionPeriodTypeDef]
    baseline: NotRequired[bool]

class TestTransformerResponseTypeDef(TypedDict):
    transformedLogs: List[TransformedLogRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

TrimStringUnionTypeDef = Union[TrimStringTypeDef, TrimStringOutputTypeDef]

class TypeConverterOutputTypeDef(TypedDict):
    entries: List[TypeConverterEntryTypeDef]

class TypeConverterTypeDef(TypedDict):
    entries: Sequence[TypeConverterEntryTypeDef]

UpperCaseStringUnionTypeDef = Union[UpperCaseStringTypeDef, UpperCaseStringOutputTypeDef]
AddKeysUnionTypeDef = Union[AddKeysTypeDef, AddKeysOutputTypeDef]

class ListAnomaliesResponseTypeDef(TypedDict):
    anomalies: List[AnomalyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ConfigurationTemplateTypeDef(TypedDict):
    service: NotRequired[str]
    logType: NotRequired[str]
    resourceType: NotRequired[str]
    deliveryDestinationType: NotRequired[DeliveryDestinationTypeType]
    defaultDeliveryConfigValues: NotRequired[ConfigurationTemplateDeliveryConfigValuesTypeDef]
    allowedFields: NotRequired[List[RecordFieldTypeDef]]
    allowedOutputFormats: NotRequired[List[OutputFormatType]]
    allowedActionForAllowVendedLogsDeliveryForResource: NotRequired[str]
    allowedFieldDelimiters: NotRequired[List[str]]
    allowedSuffixPathFields: NotRequired[List[str]]

class CreateDeliveryResponseTypeDef(TypedDict):
    delivery: DeliveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeliveriesResponseTypeDef(TypedDict):
    deliveries: List[DeliveryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetDeliveryResponseTypeDef(TypedDict):
    delivery: DeliveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

CopyValueUnionTypeDef = Union[CopyValueTypeDef, CopyValueOutputTypeDef]

class DescribeDeliveryDestinationsResponseTypeDef(TypedDict):
    deliveryDestinations: List[DeliveryDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetDeliveryDestinationResponseTypeDef(TypedDict):
    deliveryDestination: DeliveryDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliveryDestinationResponseTypeDef(TypedDict):
    deliveryDestination: DeliveryDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportTasksResponseTypeDef(TypedDict):
    exportTasks: List[ExportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartLiveTailResponseStreamTypeDef(TypedDict):
    sessionStart: NotRequired[LiveTailSessionStartTypeDef]
    sessionUpdate: NotRequired[LiveTailSessionUpdateTypeDef]
    SessionTimeoutException: NotRequired[SessionTimeoutExceptionTypeDef]
    SessionStreamingException: NotRequired[SessionStreamingExceptionTypeDef]

class DescribeMetricFiltersResponseTypeDef(TypedDict):
    metricFilters: List[MetricFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class PutMetricFilterRequestTypeDef(TypedDict):
    logGroupName: str
    filterName: str
    filterPattern: str
    metricTransformations: Sequence[MetricTransformationUnionTypeDef]
    applyOnTransformedLogs: NotRequired[bool]

MoveKeysUnionTypeDef = Union[MoveKeysTypeDef, MoveKeysOutputTypeDef]

class OpenSearchIntegrationDetailsTypeDef(TypedDict):
    dataSource: NotRequired[OpenSearchDataSourceTypeDef]
    application: NotRequired[OpenSearchApplicationTypeDef]
    collection: NotRequired[OpenSearchCollectionTypeDef]
    workspace: NotRequired[OpenSearchWorkspaceTypeDef]
    encryptionPolicy: NotRequired[OpenSearchEncryptionPolicyTypeDef]
    networkPolicy: NotRequired[OpenSearchNetworkPolicyTypeDef]
    accessPolicy: NotRequired[OpenSearchDataAccessPolicyTypeDef]
    lifecyclePolicy: NotRequired[OpenSearchLifecyclePolicyTypeDef]

class PutIntegrationRequestTypeDef(TypedDict):
    integrationName: str
    resourceConfig: ResourceConfigTypeDef
    integrationType: Literal["OPENSEARCH"]

RenameKeysUnionTypeDef = Union[RenameKeysTypeDef, RenameKeysOutputTypeDef]
SplitStringUnionTypeDef = Union[SplitStringTypeDef, SplitStringOutputTypeDef]
SubstituteStringUnionTypeDef = Union[SubstituteStringTypeDef, SubstituteStringOutputTypeDef]

class ProcessorOutputTypeDef(TypedDict):
    addKeys: NotRequired[AddKeysOutputTypeDef]
    copyValue: NotRequired[CopyValueOutputTypeDef]
    csv: NotRequired[CSVOutputTypeDef]
    dateTimeConverter: NotRequired[DateTimeConverterOutputTypeDef]
    deleteKeys: NotRequired[DeleteKeysOutputTypeDef]
    grok: NotRequired[GrokTypeDef]
    listToMap: NotRequired[ListToMapTypeDef]
    lowerCaseString: NotRequired[LowerCaseStringOutputTypeDef]
    moveKeys: NotRequired[MoveKeysOutputTypeDef]
    parseCloudfront: NotRequired[ParseCloudfrontTypeDef]
    parseJSON: NotRequired[ParseJSONTypeDef]
    parseKeyValue: NotRequired[ParseKeyValueTypeDef]
    parseRoute53: NotRequired[ParseRoute53TypeDef]
    parsePostgres: NotRequired[ParsePostgresTypeDef]
    parseVPC: NotRequired[ParseVPCTypeDef]
    parseWAF: NotRequired[ParseWAFTypeDef]
    renameKeys: NotRequired[RenameKeysOutputTypeDef]
    splitString: NotRequired[SplitStringOutputTypeDef]
    substituteString: NotRequired[SubstituteStringOutputTypeDef]
    trimString: NotRequired[TrimStringOutputTypeDef]
    typeConverter: NotRequired[TypeConverterOutputTypeDef]
    upperCaseString: NotRequired[UpperCaseStringOutputTypeDef]

TypeConverterUnionTypeDef = Union[TypeConverterTypeDef, TypeConverterOutputTypeDef]

class DescribeConfigurationTemplatesResponseTypeDef(TypedDict):
    configurationTemplates: List[ConfigurationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class StartLiveTailResponseTypeDef(TypedDict):
    responseStream: EventStream[StartLiveTailResponseStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationDetailsTypeDef(TypedDict):
    openSearchIntegrationDetails: NotRequired[OpenSearchIntegrationDetailsTypeDef]

class GetTransformerResponseTypeDef(TypedDict):
    logGroupIdentifier: str
    creationTime: int
    lastModifiedTime: int
    transformerConfig: List[ProcessorOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ProcessorTypeDef(TypedDict):
    addKeys: NotRequired[AddKeysUnionTypeDef]
    copyValue: NotRequired[CopyValueUnionTypeDef]
    csv: NotRequired[CSVUnionTypeDef]
    dateTimeConverter: NotRequired[DateTimeConverterUnionTypeDef]
    deleteKeys: NotRequired[DeleteKeysUnionTypeDef]
    grok: NotRequired[GrokTypeDef]
    listToMap: NotRequired[ListToMapTypeDef]
    lowerCaseString: NotRequired[LowerCaseStringUnionTypeDef]
    moveKeys: NotRequired[MoveKeysUnionTypeDef]
    parseCloudfront: NotRequired[ParseCloudfrontTypeDef]
    parseJSON: NotRequired[ParseJSONTypeDef]
    parseKeyValue: NotRequired[ParseKeyValueTypeDef]
    parseRoute53: NotRequired[ParseRoute53TypeDef]
    parsePostgres: NotRequired[ParsePostgresTypeDef]
    parseVPC: NotRequired[ParseVPCTypeDef]
    parseWAF: NotRequired[ParseWAFTypeDef]
    renameKeys: NotRequired[RenameKeysUnionTypeDef]
    splitString: NotRequired[SplitStringUnionTypeDef]
    substituteString: NotRequired[SubstituteStringUnionTypeDef]
    trimString: NotRequired[TrimStringUnionTypeDef]
    typeConverter: NotRequired[TypeConverterUnionTypeDef]
    upperCaseString: NotRequired[UpperCaseStringUnionTypeDef]

class GetIntegrationResponseTypeDef(TypedDict):
    integrationName: str
    integrationType: Literal["OPENSEARCH"]
    integrationStatus: IntegrationStatusType
    integrationDetails: IntegrationDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ProcessorUnionTypeDef = Union[ProcessorTypeDef, ProcessorOutputTypeDef]

class PutTransformerRequestTypeDef(TypedDict):
    logGroupIdentifier: str
    transformerConfig: Sequence[ProcessorUnionTypeDef]

class TestTransformerRequestTypeDef(TypedDict):
    transformerConfig: Sequence[ProcessorUnionTypeDef]
    logEventMessages: Sequence[str]
