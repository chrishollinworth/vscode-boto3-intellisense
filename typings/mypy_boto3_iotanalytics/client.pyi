"""
Type annotations for iotanalytics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotanalytics import IoTAnalyticsClient

    client: IoTAnalyticsClient = boto3.client("iotanalytics")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .paginator import (
    ListChannelsPaginator,
    ListDatasetContentsPaginator,
    ListDatasetsPaginator,
    ListDatastoresPaginator,
    ListPipelinesPaginator,
)
from .type_defs import (
    BatchPutMessageResponseTypeDef,
    ChannelMessagesTypeDef,
    ChannelStorageTypeDef,
    CreateChannelResponseTypeDef,
    CreateDatasetContentResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateDatastoreResponseTypeDef,
    CreatePipelineResponseTypeDef,
    DatasetActionTypeDef,
    DatasetContentDeliveryRuleTypeDef,
    DatasetTriggerTypeDef,
    DatastorePartitionsTypeDef,
    DatastoreStorageTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeDatastoreResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DescribePipelineResponseTypeDef,
    FileFormatConfigurationTypeDef,
    GetDatasetContentResponseTypeDef,
    LateDataRuleTypeDef,
    ListChannelsResponseTypeDef,
    ListDatasetContentsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListDatastoresResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingOptionsTypeDef,
    MessageTypeDef,
    PipelineActivityTypeDef,
    RetentionPeriodTypeDef,
    RunPipelineActivityResponseTypeDef,
    SampleChannelDataResponseTypeDef,
    StartPipelineReprocessingResponseTypeDef,
    TagTypeDef,
    VersioningConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("IoTAnalyticsClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class IoTAnalyticsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html)
    """

    meta: ClientMeta
    @property
    def exceptions(self) -> Exceptions:
        """
        IoTAnalyticsClient exceptions.
        """
    def batch_put_message(
        self, *, channelName: str, messages: List["MessageTypeDef"]
    ) -> BatchPutMessageResponseTypeDef:
        """
        Sends messages to a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.batch_put_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#batch_put_message)
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#can_paginate)
        """
    def cancel_pipeline_reprocessing(
        self, *, pipelineName: str, reprocessingId: str
    ) -> Dict[str, Any]:
        """
        Cancels the reprocessing of data through the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.cancel_pipeline_reprocessing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#cancel_pipeline_reprocessing)
        """
    def create_channel(
        self,
        *,
        channelName: str,
        channelStorage: "ChannelStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        tags: List["TagTypeDef"] = None
    ) -> CreateChannelResponseTypeDef:
        """
        Used to create a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create_channel)
        """
    def create_dataset(
        self,
        *,
        datasetName: str,
        actions: List["DatasetActionTypeDef"],
        triggers: List["DatasetTriggerTypeDef"] = None,
        contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"] = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        versioningConfiguration: "VersioningConfigurationTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        lateDataRules: List["LateDataRuleTypeDef"] = None
    ) -> CreateDatasetResponseTypeDef:
        """
        Used to create a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create_dataset)
        """
    def create_dataset_content(
        self, *, datasetName: str, versionId: str = None
    ) -> CreateDatasetContentResponseTypeDef:
        """
        Creates the content of a dataset by applying a `queryAction` (a SQL query) or a
        `containerAction` (executing a containerized application).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.create_dataset_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create_dataset_content)
        """
    def create_datastore(
        self,
        *,
        datastoreName: str,
        datastoreStorage: "DatastoreStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        fileFormatConfiguration: "FileFormatConfigurationTypeDef" = None,
        datastorePartitions: "DatastorePartitionsTypeDef" = None
    ) -> CreateDatastoreResponseTypeDef:
        """
        Creates a data store, which is a repository for messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.create_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create_datastore)
        """
    def create_pipeline(
        self,
        *,
        pipelineName: str,
        pipelineActivities: List["PipelineActivityTypeDef"],
        tags: List["TagTypeDef"] = None
    ) -> CreatePipelineResponseTypeDef:
        """
        Creates a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.create_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create_pipeline)
        """
    def delete_channel(self, *, channelName: str) -> None:
        """
        Deletes the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete_channel)
        """
    def delete_dataset(self, *, datasetName: str) -> None:
        """
        Deletes the specified dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete_dataset)
        """
    def delete_dataset_content(self, *, datasetName: str, versionId: str = None) -> None:
        """
        Deletes the content of the specified dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_dataset_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete_dataset_content)
        """
    def delete_datastore(self, *, datastoreName: str) -> None:
        """
        Deletes the specified data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete_datastore)
        """
    def delete_pipeline(self, *, pipelineName: str) -> None:
        """
        Deletes the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete_pipeline)
        """
    def describe_channel(
        self, *, channelName: str, includeStatistics: bool = None
    ) -> DescribeChannelResponseTypeDef:
        """
        Retrieves information about a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe_channel)
        """
    def describe_dataset(self, *, datasetName: str) -> DescribeDatasetResponseTypeDef:
        """
        Retrieves information about a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe_dataset)
        """
    def describe_datastore(
        self, *, datastoreName: str, includeStatistics: bool = None
    ) -> DescribeDatastoreResponseTypeDef:
        """
        Retrieves information about a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe_datastore)
        """
    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        Retrieves the current settings of the IoT Analytics logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe_logging_options)
        """
    def describe_pipeline(self, *, pipelineName: str) -> DescribePipelineResponseTypeDef:
        """
        Retrieves information about a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe_pipeline)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#generate_presigned_url)
        """
    def get_dataset_content(
        self, *, datasetName: str, versionId: str = None
    ) -> GetDatasetContentResponseTypeDef:
        """
        Retrieves the contents of a dataset as presigned URIs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.get_dataset_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#get_dataset_content)
        """
    def list_channels(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListChannelsResponseTypeDef:
        """
        Retrieves a list of channels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list_channels)
        """
    def list_dataset_contents(
        self,
        *,
        datasetName: str,
        nextToken: str = None,
        maxResults: int = None,
        scheduledOnOrAfter: Union[datetime, str] = None,
        scheduledBefore: Union[datetime, str] = None
    ) -> ListDatasetContentsResponseTypeDef:
        """
        Lists information about dataset contents that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.list_dataset_contents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list_dataset_contents)
        """
    def list_datasets(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        Retrieves information about datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list_datasets)
        """
    def list_datastores(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListDatastoresResponseTypeDef:
        """
        Retrieves a list of data stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.list_datastores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list_datastores)
        """
    def list_pipelines(
        self, *, nextToken: str = None, maxResults: int = None
    ) -> ListPipelinesResponseTypeDef:
        """
        Retrieves a list of pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.list_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list_pipelines)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) that you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list_tags_for_resource)
        """
    def put_logging_options(self, *, loggingOptions: "LoggingOptionsTypeDef") -> None:
        """
        Sets or updates the IoT Analytics logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.put_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#put_logging_options)
        """
    def run_pipeline_activity(
        self,
        *,
        pipelineActivity: "PipelineActivityTypeDef",
        payloads: List[Union[bytes, IO[bytes], StreamingBody]]
    ) -> RunPipelineActivityResponseTypeDef:
        """
        Simulates the results of running a pipeline activity on a message payload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.run_pipeline_activity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#run_pipeline_activity)
        """
    def sample_channel_data(
        self,
        *,
        channelName: str,
        maxMessages: int = None,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None
    ) -> SampleChannelDataResponseTypeDef:
        """
        Retrieves a sample of messages from the specified channel ingested during the
        specified timeframe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.sample_channel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#sample_channel_data)
        """
    def start_pipeline_reprocessing(
        self,
        *,
        pipelineName: str,
        startTime: Union[datetime, str] = None,
        endTime: Union[datetime, str] = None,
        channelMessages: "ChannelMessagesTypeDef" = None
    ) -> StartPipelineReprocessingResponseTypeDef:
        """
        Starts the reprocessing of raw message data through the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.start_pipeline_reprocessing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#start_pipeline_reprocessing)
        """
    def tag_resource(self, *, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the given tags (metadata) from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#untag_resource)
        """
    def update_channel(
        self,
        *,
        channelName: str,
        channelStorage: "ChannelStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None
    ) -> None:
        """
        Used to update the settings of a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#update_channel)
        """
    def update_dataset(
        self,
        *,
        datasetName: str,
        actions: List["DatasetActionTypeDef"],
        triggers: List["DatasetTriggerTypeDef"] = None,
        contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"] = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        versioningConfiguration: "VersioningConfigurationTypeDef" = None,
        lateDataRules: List["LateDataRuleTypeDef"] = None
    ) -> None:
        """
        Updates the settings of a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.update_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#update_dataset)
        """
    def update_datastore(
        self,
        *,
        datastoreName: str,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        datastoreStorage: "DatastoreStorageTypeDef" = None,
        fileFormatConfiguration: "FileFormatConfigurationTypeDef" = None
    ) -> None:
        """
        Used to update the settings of a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.update_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#update_datastore)
        """
    def update_pipeline(
        self, *, pipelineName: str, pipelineActivities: List["PipelineActivityTypeDef"]
    ) -> None:
        """
        Updates the settings of a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Client.update_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#update_pipeline)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListChannels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listchannelspaginator)
        """
    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_contents"]
    ) -> ListDatasetContentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasetContents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listdatasetcontentspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listdatasetspaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_datastores"]) -> ListDatastoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatastores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listdatastorespaginator)
        """
    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListPipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listpipelinespaginator)
        """
