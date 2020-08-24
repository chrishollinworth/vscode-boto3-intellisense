# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for iotanalytics service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotanalytics import IoTAnalyticsClient

    client: IoTAnalyticsClient = boto3.client("iotanalytics")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_iotanalytics.paginator import (
    ListChannelsPaginator,
    ListDatasetContentsPaginator,
    ListDatasetsPaginator,
    ListDatastoresPaginator,
    ListPipelinesPaginator,
)
from mypy_boto3_iotanalytics.type_defs import (
    BatchPutMessageResponseTypeDef,
    ChannelStorageTypeDef,
    CreateChannelResponseTypeDef,
    CreateDatasetContentResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateDatastoreResponseTypeDef,
    CreatePipelineResponseTypeDef,
    DatasetActionTypeDef,
    DatasetContentDeliveryRuleTypeDef,
    DatasetTriggerTypeDef,
    DatastoreStorageTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeDatastoreResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DescribePipelineResponseTypeDef,
    GetDatasetContentResponseTypeDef,
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


class Exceptions:
    ClientError: Type[Boto3ClientError]
    InternalFailureException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ResourceAlreadyExistsException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]


class IoTAnalyticsClient:
    """
    [IoTAnalytics.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client)
    """

    exceptions: Exceptions

    def batch_put_message(
        self, channelName: str, messages: List[MessageTypeDef]
    ) -> BatchPutMessageResponseTypeDef:
        """
        [Client.batch_put_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.batch_put_message)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.can_paginate)
        """

    def cancel_pipeline_reprocessing(
        self, pipelineName: str, reprocessingId: str
    ) -> Dict[str, Any]:
        """
        [Client.cancel_pipeline_reprocessing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.cancel_pipeline_reprocessing)
        """

    def create_channel(
        self,
        channelName: str,
        channelStorage: "ChannelStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateChannelResponseTypeDef:
        """
        [Client.create_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.create_channel)
        """

    def create_dataset(
        self,
        datasetName: str,
        actions: List["DatasetActionTypeDef"],
        triggers: List["DatasetTriggerTypeDef"] = None,
        contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"] = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        versioningConfiguration: "VersioningConfigurationTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDatasetResponseTypeDef:
        """
        [Client.create_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.create_dataset)
        """

    def create_dataset_content(self, datasetName: str) -> CreateDatasetContentResponseTypeDef:
        """
        [Client.create_dataset_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.create_dataset_content)
        """

    def create_datastore(
        self,
        datastoreName: str,
        datastoreStorage: "DatastoreStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDatastoreResponseTypeDef:
        """
        [Client.create_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.create_datastore)
        """

    def create_pipeline(
        self,
        pipelineName: str,
        pipelineActivities: List["PipelineActivityTypeDef"],
        tags: List["TagTypeDef"] = None,
    ) -> CreatePipelineResponseTypeDef:
        """
        [Client.create_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.create_pipeline)
        """

    def delete_channel(self, channelName: str) -> None:
        """
        [Client.delete_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_channel)
        """

    def delete_dataset(self, datasetName: str) -> None:
        """
        [Client.delete_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_dataset)
        """

    def delete_dataset_content(self, datasetName: str, versionId: str = None) -> None:
        """
        [Client.delete_dataset_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_dataset_content)
        """

    def delete_datastore(self, datastoreName: str) -> None:
        """
        [Client.delete_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_datastore)
        """

    def delete_pipeline(self, pipelineName: str) -> None:
        """
        [Client.delete_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_pipeline)
        """

    def describe_channel(
        self, channelName: str, includeStatistics: bool = None
    ) -> DescribeChannelResponseTypeDef:
        """
        [Client.describe_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_channel)
        """

    def describe_dataset(self, datasetName: str) -> DescribeDatasetResponseTypeDef:
        """
        [Client.describe_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_dataset)
        """

    def describe_datastore(
        self, datastoreName: str, includeStatistics: bool = None
    ) -> DescribeDatastoreResponseTypeDef:
        """
        [Client.describe_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_datastore)
        """

    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        [Client.describe_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_logging_options)
        """

    def describe_pipeline(self, pipelineName: str) -> DescribePipelineResponseTypeDef:
        """
        [Client.describe_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_pipeline)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.generate_presigned_url)
        """

    def get_dataset_content(
        self, datasetName: str, versionId: str = None
    ) -> GetDatasetContentResponseTypeDef:
        """
        [Client.get_dataset_content documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.get_dataset_content)
        """

    def list_channels(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListChannelsResponseTypeDef:
        """
        [Client.list_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.list_channels)
        """

    def list_dataset_contents(
        self,
        datasetName: str,
        nextToken: str = None,
        maxResults: int = None,
        scheduledOnOrAfter: datetime = None,
        scheduledBefore: datetime = None,
    ) -> ListDatasetContentsResponseTypeDef:
        """
        [Client.list_dataset_contents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.list_dataset_contents)
        """

    def list_datasets(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Client.list_datasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.list_datasets)
        """

    def list_datastores(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDatastoresResponseTypeDef:
        """
        [Client.list_datastores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.list_datastores)
        """

    def list_pipelines(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListPipelinesResponseTypeDef:
        """
        [Client.list_pipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.list_pipelines)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.list_tags_for_resource)
        """

    def put_logging_options(self, loggingOptions: "LoggingOptionsTypeDef") -> None:
        """
        [Client.put_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.put_logging_options)
        """

    def run_pipeline_activity(
        self, pipelineActivity: "PipelineActivityTypeDef", payloads: List[bytes]
    ) -> RunPipelineActivityResponseTypeDef:
        """
        [Client.run_pipeline_activity documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.run_pipeline_activity)
        """

    def sample_channel_data(
        self,
        channelName: str,
        maxMessages: int = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> SampleChannelDataResponseTypeDef:
        """
        [Client.sample_channel_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.sample_channel_data)
        """

    def start_pipeline_reprocessing(
        self, pipelineName: str, startTime: datetime = None, endTime: datetime = None
    ) -> StartPipelineReprocessingResponseTypeDef:
        """
        [Client.start_pipeline_reprocessing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.start_pipeline_reprocessing)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.untag_resource)
        """

    def update_channel(
        self,
        channelName: str,
        channelStorage: "ChannelStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
    ) -> None:
        """
        [Client.update_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.update_channel)
        """

    def update_dataset(
        self,
        datasetName: str,
        actions: List["DatasetActionTypeDef"],
        triggers: List["DatasetTriggerTypeDef"] = None,
        contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"] = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        versioningConfiguration: "VersioningConfigurationTypeDef" = None,
    ) -> None:
        """
        [Client.update_dataset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.update_dataset)
        """

    def update_datastore(
        self,
        datastoreName: str,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        datastoreStorage: "DatastoreStorageTypeDef" = None,
    ) -> None:
        """
        [Client.update_datastore documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.update_datastore)
        """

    def update_pipeline(
        self, pipelineName: str, pipelineActivities: List["PipelineActivityTypeDef"]
    ) -> None:
        """
        [Client.update_pipeline documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Client.update_pipeline)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListChannels)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_contents"]
    ) -> ListDatasetContentsPaginator:
        """
        [Paginator.ListDatasetContents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasetContents)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasets)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datastores"]) -> ListDatastoresPaginator:
        """
        [Paginator.ListDatastores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatastores)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListPipelines)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
