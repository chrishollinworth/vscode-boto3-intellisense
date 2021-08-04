"""
Type annotations for logs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_logs import CloudWatchLogsClient

    client: CloudWatchLogsClient = boto3.client("logs")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import DistributionType, ExportTaskStatusCodeType, OrderByType, QueryStatusType
from .paginator import (
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
from .type_defs import (
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

class CloudWatchLogsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        CloudWatchLogsClient exceptions.
        """
    def associate_kms_key(self, *, logGroupName: str, kmsKeyId: str) -> None:
        """
        Associates the specified AWS Key Management Service (AWS KMS) customer master
        key (CMK) with the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.associate_kms_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#associate_kms_key)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#can_paginate)
        """
    def cancel_export_task(self, *, taskId: str) -> None:
        """
        Cancels the specified export task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.cancel_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#cancel_export_task)
        """
    def create_export_task(
        self,
        *,
        logGroupName: str,
        fromTime: int,
        to: int,
        destination: str,
        taskName: str = None,
        logStreamNamePrefix: str = None,
        destinationPrefix: str = None
    ) -> CreateExportTaskResponseTypeDef:
        """
        Creates an export task, which allows you to efficiently export data from a log
        group to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.create_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#create_export_task)
        """
    def create_log_group(
        self, *, logGroupName: str, kmsKeyId: str = None, tags: Dict[str, str] = None
    ) -> None:
        """
        Creates a log group with the specified name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.create_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#create_log_group)
        """
    def create_log_stream(self, *, logGroupName: str, logStreamName: str) -> None:
        """
        Creates a log stream for the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.create_log_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#create_log_stream)
        """
    def delete_destination(self, *, destinationName: str) -> None:
        """
        Deletes the specified destination, and eventually disables all the subscription
        filters that publish to it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.delete_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_destination)
        """
    def delete_log_group(self, *, logGroupName: str) -> None:
        """
        Deletes the specified log group and permanently deletes all the archived log
        events associated with the log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.delete_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_log_group)
        """
    def delete_log_stream(self, *, logGroupName: str, logStreamName: str) -> None:
        """
        Deletes the specified log stream and permanently deletes all the archived log
        events associated with the log stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.delete_log_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_log_stream)
        """
    def delete_metric_filter(self, *, logGroupName: str, filterName: str) -> None:
        """
        Deletes the specified metric filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.delete_metric_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_metric_filter)
        """
    def delete_query_definition(
        self, *, queryDefinitionId: str
    ) -> DeleteQueryDefinitionResponseTypeDef:
        """
        Deletes a saved CloudWatch Logs Insights query definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.delete_query_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_query_definition)
        """
    def delete_resource_policy(self, *, policyName: str = None) -> None:
        """
        Deletes a resource policy from this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_resource_policy)
        """
    def delete_retention_policy(self, *, logGroupName: str) -> None:
        """
        Deletes the specified retention policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.delete_retention_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_retention_policy)
        """
    def delete_subscription_filter(self, *, logGroupName: str, filterName: str) -> None:
        """
        Deletes the specified subscription filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.delete_subscription_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#delete_subscription_filter)
        """
    def describe_destinations(
        self, *, DestinationNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> DescribeDestinationsResponseTypeDef:
        """
        Lists all your destinations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_destinations)
        """
    def describe_export_tasks(
        self,
        *,
        taskId: str = None,
        statusCode: ExportTaskStatusCodeType = None,
        nextToken: str = None,
        limit: int = None
    ) -> DescribeExportTasksResponseTypeDef:
        """
        Lists the specified export tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_export_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_export_tasks)
        """
    def describe_log_groups(
        self, *, logGroupNamePrefix: str = None, nextToken: str = None, limit: int = None
    ) -> DescribeLogGroupsResponseTypeDef:
        """
        Lists the specified log groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_log_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_log_groups)
        """
    def describe_log_streams(
        self,
        *,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: OrderByType = None,
        descending: bool = None,
        nextToken: str = None,
        limit: int = None
    ) -> DescribeLogStreamsResponseTypeDef:
        """
        Lists the log streams for the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_log_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_log_streams)
        """
    def describe_metric_filters(
        self,
        *,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None,
        metricName: str = None,
        metricNamespace: str = None
    ) -> DescribeMetricFiltersResponseTypeDef:
        """
        Lists the specified metric filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_metric_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_metric_filters)
        """
    def describe_queries(
        self,
        *,
        logGroupName: str = None,
        status: QueryStatusType = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeQueriesResponseTypeDef:
        """
        Returns a list of CloudWatch Logs Insights queries that are scheduled,
        executing, or have been executed recently in this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_queries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_queries)
        """
    def describe_query_definitions(
        self,
        *,
        queryDefinitionNamePrefix: str = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeQueryDefinitionsResponseTypeDef:
        """
        This operation returns a paginated list of your saved CloudWatch Logs Insights
        query definitions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_query_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_query_definitions)
        """
    def describe_resource_policies(
        self, *, nextToken: str = None, limit: int = None
    ) -> DescribeResourcePoliciesResponseTypeDef:
        """
        Lists the resource policies in this account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_resource_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_resource_policies)
        """
    def describe_subscription_filters(
        self,
        *,
        logGroupName: str,
        filterNamePrefix: str = None,
        nextToken: str = None,
        limit: int = None
    ) -> DescribeSubscriptionFiltersResponseTypeDef:
        """
        Lists the subscription filters for the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.describe_subscription_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#describe_subscription_filters)
        """
    def disassociate_kms_key(self, *, logGroupName: str) -> None:
        """
        Disassociates the associated AWS Key Management Service (AWS KMS) customer
        master key (CMK) from the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.disassociate_kms_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#disassociate_kms_key)
        """
    def filter_log_events(
        self,
        *,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        nextToken: str = None,
        limit: int = None,
        interleaved: bool = None
    ) -> FilterLogEventsResponseTypeDef:
        """
        Lists log events from the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.filter_log_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#filter_log_events)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#generate_presigned_url)
        """
    def get_log_events(
        self,
        *,
        logGroupName: str,
        logStreamName: str,
        startTime: int = None,
        endTime: int = None,
        nextToken: str = None,
        limit: int = None,
        startFromHead: bool = None
    ) -> GetLogEventsResponseTypeDef:
        """
        Lists log events from the specified log stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.get_log_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#get_log_events)
        """
    def get_log_group_fields(
        self, *, logGroupName: str, time: int = None
    ) -> GetLogGroupFieldsResponseTypeDef:
        """
        Returns a list of the fields that are included in log events in the specified
        log group, along with the percentage of log events that contain each field.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.get_log_group_fields)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#get_log_group_fields)
        """
    def get_log_record(self, *, logRecordPointer: str) -> GetLogRecordResponseTypeDef:
        """
        Retrieves all of the fields and values of a single log event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.get_log_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#get_log_record)
        """
    def get_query_results(self, *, queryId: str) -> GetQueryResultsResponseTypeDef:
        """
        Returns the results from the specified query.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.get_query_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#get_query_results)
        """
    def list_tags_log_group(self, *, logGroupName: str) -> ListTagsLogGroupResponseTypeDef:
        """
        Lists the tags for the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.list_tags_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#list_tags_log_group)
        """
    def put_destination(
        self, *, destinationName: str, targetArn: str, roleArn: str
    ) -> PutDestinationResponseTypeDef:
        """
        Creates or updates a destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.put_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_destination)
        """
    def put_destination_policy(self, *, destinationName: str, accessPolicy: str) -> None:
        """
        Creates or updates an access policy associated with an existing destination.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.put_destination_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_destination_policy)
        """
    def put_log_events(
        self,
        *,
        logGroupName: str,
        logStreamName: str,
        logEvents: List["InputLogEventTypeDef"],
        sequenceToken: str = None
    ) -> PutLogEventsResponseTypeDef:
        """
        Uploads a batch of log events to the specified log stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.put_log_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_log_events)
        """
    def put_metric_filter(
        self,
        *,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        metricTransformations: List["MetricTransformationTypeDef"]
    ) -> None:
        """
        Creates or updates a metric filter and associates it with the specified log
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.put_metric_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_metric_filter)
        """
    def put_query_definition(
        self,
        *,
        name: str,
        queryString: str,
        queryDefinitionId: str = None,
        logGroupNames: List[str] = None
    ) -> PutQueryDefinitionResponseTypeDef:
        """
        Creates or updates a query definition for CloudWatch Logs Insights.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.put_query_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_query_definition)
        """
    def put_resource_policy(
        self, *, policyName: str = None, policyDocument: str = None
    ) -> PutResourcePolicyResponseTypeDef:
        """
        Creates or updates a resource policy allowing other AWS services to put log
        events to this account, such as Amazon Route 53.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_resource_policy)
        """
    def put_retention_policy(self, *, logGroupName: str, retentionInDays: int) -> None:
        """
        Sets the retention of the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.put_retention_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_retention_policy)
        """
    def put_subscription_filter(
        self,
        *,
        logGroupName: str,
        filterName: str,
        filterPattern: str,
        destinationArn: str,
        roleArn: str = None,
        distribution: DistributionType = None
    ) -> None:
        """
        Creates or updates a subscription filter and associates it with the specified
        log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.put_subscription_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#put_subscription_filter)
        """
    def start_query(
        self,
        *,
        startTime: int,
        endTime: int,
        queryString: str,
        logGroupName: str = None,
        logGroupNames: List[str] = None,
        limit: int = None
    ) -> StartQueryResponseTypeDef:
        """
        Schedules a query of a log group using CloudWatch Logs Insights.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.start_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#start_query)
        """
    def stop_query(self, *, queryId: str) -> StopQueryResponseTypeDef:
        """
        Stops a CloudWatch Logs Insights query that is in progress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.stop_query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#stop_query)
        """
    def tag_log_group(self, *, logGroupName: str, tags: Dict[str, str]) -> None:
        """
        Adds or updates the specified tags for the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.tag_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#tag_log_group)
        """
    def test_metric_filter(
        self, *, filterPattern: str, logEventMessages: List[str]
    ) -> TestMetricFilterResponseTypeDef:
        """
        Tests the filter pattern of a metric filter against a sample of log event
        messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.test_metric_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#test_metric_filter)
        """
    def untag_log_group(self, *, logGroupName: str, tags: List[str]) -> None:
        """
        Removes the specified tags from the specified log group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Client.untag_log_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/client.html#untag_log_group)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_destinations"]
    ) -> DescribeDestinationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describedestinationspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_tasks"]
    ) -> DescribeExportTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeexporttaskspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_log_groups"]
    ) -> DescribeLogGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeloggroupspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_log_streams"]
    ) -> DescribeLogStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describelogstreamspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_metric_filters"]
    ) -> DescribeMetricFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describemetricfilterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_queries"]
    ) -> DescribeQueriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describequeriespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_resource_policies"]
    ) -> DescribeResourcePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describeresourcepoliciespaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscription_filters"]
    ) -> DescribeSubscriptionFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#describesubscriptionfilterspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["filter_log_events"]
    ) -> FilterLogEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/paginators.html#filterlogeventspaginator)
        """
