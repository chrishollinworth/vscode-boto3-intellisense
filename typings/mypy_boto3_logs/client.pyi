# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for logs service client

Usage::

    ```python
    import boto3
    from mypy_boto3_logs import CloudWatchLogsClient

    client: CloudWatchLogsClient = boto3.client("logs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_logs.paginator import (
    DescribeDestinationsPaginator,
    DescribeExportTasksPaginator,
    DescribeLogGroupsPaginator,
    DescribeLogStreamsPaginator,
    DescribeMetricFiltersPaginator,
    DescribeQueriesPaginator,
    DescribeResourcePoliciesPaginator,
    DescribeSubscriptionFiltersPaginator,
    FilterLogEventsPaginator,
)
from mypy_boto3_logs.type_defs import (
    CreateExportTaskResponseTypeDef,
    DeleteQueryDefinitionResponseTypeDef,
    DescribeDestinationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeLogGroupsResponseTypeDef,
    DescribeLogStreamsResponseTypeDef,
    DescribeMetricFiltersResponseTypeDef,
    DescribeQueriesResponseTypeDef,
    DescribeQueryDefinitionsResponseTypeDef,
    DescribeResourcePoliciesResponseTypeDef,
    DescribeSubscriptionFiltersResponseTypeDef,
    FilterLogEventsResponseTypeDef,
    GetLogEventsResponseTypeDef,
    GetLogGroupFieldsResponseTypeDef,
    GetLogRecordResponseTypeDef,
    GetQueryResultsResponseTypeDef,
    InputLogEventTypeDef,
    ListTagsLogGroupResponseTypeDef,
    MetricTransformationTypeDef,
    PutDestinationResponseTypeDef,
    PutLogEventsResponseTypeDef,
    PutQueryDefinitionResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    StartQueryResponseTypeDef,
    StopQueryResponseTypeDef,
    TestMetricFilterResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CloudWatchLogsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DataAlreadyAcceptedException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidSequenceTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MalformedQueryException: Type[BotocoreClientError]
    OperationAbortedException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    UnrecognizedClientException: Type[BotocoreClientError]


class CloudWatchLogsClient:
    """
    [CloudWatchLogs.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_kms_key(self, logGroupName: str, kmsKeyId: str) -> None:
        """
        [Client.associate_kms_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.associate_kms_key)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.can_paginate)
        """

    def cancel_export_task(self, taskId: str) -> None:
        """
        [Client.cancel_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.cancel_export_task)
        """

    def create_export_task(
        self,
        logGroupName: str,
        fromTime: int,
        to: int,
        destination: str,
        taskName: str = None,
        logStreamNamePrefix: str = None,
        destinationPrefix: str = None,
    ) -> CreateExportTaskResponseTypeDef:
        """
        [Client.create_export_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.create_export_task)
        """

    def create_log_group(
        self, logGroupName: str, kmsKeyId: str = None, tags: Dict[str, str] = None
    ) -> None:
        """
        [Client.create_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.create_log_group)
        """

    def create_log_stream(self, logGroupName: str, logStreamName: str) -> None:
        """
        [Client.create_log_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.create_log_stream)
        """

    def delete_destination(self, destinationName: str) -> None:
        """
        [Client.delete_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.delete_destination)
        """

    def delete_log_group(self, logGroupName: str) -> None:
        """
        [Client.delete_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.delete_log_group)
        """

    def delete_log_stream(self, logGroupName: str, logStreamName: str) -> None:
        """
        [Client.delete_log_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.delete_log_stream)
        """

    def delete_metric_filter(self, logGroupName: str, filterName: str) -> None:
        """
        [Client.delete_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.delete_metric_filter)
        """

    def delete_query_definition(
        self, queryDefinitionId: str
    ) -> DeleteQueryDefinitionResponseTypeDef:
        """
        [Client.delete_query_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.delete_query_definition)
        """

    def delete_resource_policy(self, policyName: str = None) -> None:
        """
        [Client.delete_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.delete_resource_policy)
        """

    def delete_retention_policy(self, logGroupName: str) -> None:
        """
        [Client.delete_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.delete_retention_policy)
        """

    def delete_subscription_filter(self, logGroupName: str, filterName: str) -> None:
        """
        [Client.delete_subscription_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.delete_subscription_filter)
        """

    def describe_destinations(
        self, DestinationNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> DescribeDestinationsResponseTypeDef:
        """
        [Client.describe_destinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_destinations)
        """

    def describe_export_tasks(
        self,
        taskId: str = None,
        statusCode: Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ] = None,
        nextToken: str = None,
        limit: int = None,
    ) -> DescribeExportTasksResponseTypeDef:
        """
        [Client.describe_export_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_export_tasks)
        """

    def describe_log_groups(
        self, logGroupNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> DescribeLogGroupsResponseTypeDef:
        """
        [Client.describe_log_groups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_log_groups)
        """

    def describe_log_streams(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: Literal["LogStreamName", "LastEventTime"] = None,
        descending: bool = None,
        nextToken: str = None,
        limit: int = None,
    ) -> DescribeLogStreamsResponseTypeDef:
        """
        [Client.describe_log_streams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_log_streams)
        """

    def describe_metric_filters(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
        metricName: str = None,
        metricNamespace: str = None,
    ) -> DescribeMetricFiltersResponseTypeDef:
        """
        [Client.describe_metric_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_metric_filters)
        """

    def describe_queries(
        self,
        logGroupName: str = None,
        status: Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeQueriesResponseTypeDef:
        """
        [Client.describe_queries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_queries)
        """

    def describe_query_definitions(
        self, queryDefinitionNamePrefix: str = None, maxResults: int = None, nextToken: str = None
    ) -> DescribeQueryDefinitionsResponseTypeDef:
        """
        [Client.describe_query_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_query_definitions)
        """

    def describe_resource_policies(
        self, nextToken: str = None, limit: int = None
    ) -> DescribeResourcePoliciesResponseTypeDef:
        """
        [Client.describe_resource_policies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_resource_policies)
        """

    def describe_subscription_filters(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
    ) -> DescribeSubscriptionFiltersResponseTypeDef:
        """
        [Client.describe_subscription_filters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.describe_subscription_filters)
        """

    def disassociate_kms_key(self, logGroupName: str) -> None:
        """
        [Client.disassociate_kms_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.disassociate_kms_key)
        """

    def filter_log_events(
        self,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        nextToken: str = None,
        limit: int = None,
        interleaved: bool = None,
    ) -> FilterLogEventsResponseTypeDef:
        """
        [Client.filter_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.filter_log_events)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.generate_presigned_url)
        """

    def get_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        startTime: int = None,
        endTime: int = None,
        nextToken: str = None,
        limit: int = None,
        startFromHead: bool = None,
    ) -> GetLogEventsResponseTypeDef:
        """
        [Client.get_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.get_log_events)
        """

    def get_log_group_fields(
        self, logGroupName: str, time: int = None
    ) -> GetLogGroupFieldsResponseTypeDef:
        """
        [Client.get_log_group_fields documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.get_log_group_fields)
        """

    def get_log_record(self, logRecordPointer: str) -> GetLogRecordResponseTypeDef:
        """
        [Client.get_log_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.get_log_record)
        """

    def get_query_results(self, queryId: str) -> GetQueryResultsResponseTypeDef:
        """
        [Client.get_query_results documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.get_query_results)
        """

    def list_tags_log_group(self, logGroupName: str) -> ListTagsLogGroupResponseTypeDef:
        """
        [Client.list_tags_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.list_tags_log_group)
        """

    def put_destination(
        self, destinationName: str, targetArn: str, roleArn: str
    ) -> PutDestinationResponseTypeDef:
        """
        [Client.put_destination documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.put_destination)
        """

    def put_destination_policy(self, destinationName: str, accessPolicy: str) -> None:
        """
        [Client.put_destination_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.put_destination_policy)
        """

    def put_log_events(
        self,
        logGroupName: str,
        logStreamName: str,
        logEvents: List[InputLogEventTypeDef],
        sequenceToken: str = None,
    ) -> PutLogEventsResponseTypeDef:
        """
        [Client.put_log_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.put_log_events)
        """

    def put_metric_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        metricTransformations: List["MetricTransformationTypeDef"],
    ) -> None:
        """
        [Client.put_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.put_metric_filter)
        """

    def put_query_definition(
        self,
        name: str,
        queryString: str,
        queryDefinitionId: str = None,
        logGroupNames: List[str] = None,
    ) -> PutQueryDefinitionResponseTypeDef:
        """
        [Client.put_query_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.put_query_definition)
        """

    def put_resource_policy(
        self, policyName: str = None, policyDocument: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        [Client.put_resource_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.put_resource_policy)
        """

    def put_retention_policy(self, logGroupName: str, retentionInDays: int) -> None:
        """
        [Client.put_retention_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.put_retention_policy)
        """

    def put_subscription_filter(
        self,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        destinationArn: str,
        roleArn: str = None,
        distribution: Literal["Random", "ByLogStream"] = None,
    ) -> None:
        """
        [Client.put_subscription_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.put_subscription_filter)
        """

    def start_query(
        self,
        startTime: int,
        endTime: int,
        queryString: str,
        logGroupName: str = None,
        logGroupNames: List[str] = None,
        limit: int = None,
    ) -> StartQueryResponseTypeDef:
        """
        [Client.start_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.start_query)
        """

    def stop_query(self, queryId: str) -> StopQueryResponseTypeDef:
        """
        [Client.stop_query documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.stop_query)
        """

    def tag_log_group(self, logGroupName: str, tags: Dict[str, str]) -> None:
        """
        [Client.tag_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.tag_log_group)
        """

    def test_metric_filter(
        self, filterPattern: str, logEventMessages: List[str]
    ) -> TestMetricFilterResponseTypeDef:
        """
        [Client.test_metric_filter documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.test_metric_filter)
        """

    def untag_log_group(self, logGroupName: str, tags: List[str]) -> None:
        """
        [Client.untag_log_group documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Client.untag_log_group)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_destinations"]
    ) -> DescribeDestinationsPaginator:
        """
        [Paginator.DescribeDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_log_groups"]
    ) -> DescribeLogGroupsPaginator:
        """
        [Paginator.DescribeLogGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_log_streams"]
    ) -> DescribeLogStreamsPaginator:
        """
        [Paginator.DescribeLogStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_metric_filters"]
    ) -> DescribeMetricFiltersPaginator:
        """
        [Paginator.DescribeMetricFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_queries"]
    ) -> DescribeQueriesPaginator:
        """
        [Paginator.DescribeQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_policies"]
    ) -> DescribeResourcePoliciesPaginator:
        """
        [Paginator.DescribeResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscription_filters"]
    ) -> DescribeSubscriptionFiltersPaginator:
        """
        [Paginator.DescribeSubscriptionFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["filter_log_events"]
    ) -> FilterLogEventsPaginator:
        """
        [Paginator.FilterLogEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)
        """
