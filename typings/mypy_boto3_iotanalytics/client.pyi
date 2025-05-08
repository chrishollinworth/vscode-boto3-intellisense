"""
Type annotations for iotanalytics service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotanalytics.client import IoTAnalyticsClient

    session = Session()
    client: IoTAnalyticsClient = session.client("iotanalytics")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    ListChannelsPaginator,
    ListDatasetContentsPaginator,
    ListDatasetsPaginator,
    ListDatastoresPaginator,
    ListPipelinesPaginator,
)
from .type_defs import (
    BatchPutMessageRequestTypeDef,
    BatchPutMessageResponseTypeDef,
    CancelPipelineReprocessingRequestTypeDef,
    CreateChannelRequestTypeDef,
    CreateChannelResponseTypeDef,
    CreateDatasetContentRequestTypeDef,
    CreateDatasetContentResponseTypeDef,
    CreateDatasetRequestTypeDef,
    CreateDatasetResponseTypeDef,
    CreateDatastoreRequestTypeDef,
    CreateDatastoreResponseTypeDef,
    CreatePipelineRequestTypeDef,
    CreatePipelineResponseTypeDef,
    DeleteChannelRequestTypeDef,
    DeleteDatasetContentRequestTypeDef,
    DeleteDatasetRequestTypeDef,
    DeleteDatastoreRequestTypeDef,
    DeletePipelineRequestTypeDef,
    DescribeChannelRequestTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeDatasetRequestTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeDatastoreRequestTypeDef,
    DescribeDatastoreResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DescribePipelineRequestTypeDef,
    DescribePipelineResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetDatasetContentRequestTypeDef,
    GetDatasetContentResponseTypeDef,
    ListChannelsRequestTypeDef,
    ListChannelsResponseTypeDef,
    ListDatasetContentsRequestTypeDef,
    ListDatasetContentsResponseTypeDef,
    ListDatasetsRequestTypeDef,
    ListDatasetsResponseTypeDef,
    ListDatastoresRequestTypeDef,
    ListDatastoresResponseTypeDef,
    ListPipelinesRequestTypeDef,
    ListPipelinesResponseTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutLoggingOptionsRequestTypeDef,
    RunPipelineActivityRequestTypeDef,
    RunPipelineActivityResponseTypeDef,
    SampleChannelDataRequestTypeDef,
    SampleChannelDataResponseTypeDef,
    StartPipelineReprocessingRequestTypeDef,
    StartPipelineReprocessingResponseTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdateChannelRequestTypeDef,
    UpdateDatasetRequestTypeDef,
    UpdateDatastoreRequestTypeDef,
    UpdatePipelineRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("IoTAnalyticsClient",)

class Exceptions(BaseClientExceptions):
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        IoTAnalyticsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics.html#IoTAnalytics.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#generate_presigned_url)
        """

    def batch_put_message(
        self, **kwargs: Unpack[BatchPutMessageRequestTypeDef]
    ) -> BatchPutMessageResponseTypeDef:
        """
        Sends messages to a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/batch_put_message.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#batch_put_message)
        """

    def cancel_pipeline_reprocessing(
        self, **kwargs: Unpack[CancelPipelineReprocessingRequestTypeDef]
    ) -> Dict[str, Any]:
        """
        Cancels the reprocessing of data through the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/cancel_pipeline_reprocessing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#cancel_pipeline_reprocessing)
        """

    def create_channel(
        self, **kwargs: Unpack[CreateChannelRequestTypeDef]
    ) -> CreateChannelResponseTypeDef:
        """
        Used to create a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/create_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#create_channel)
        """

    def create_dataset(
        self, **kwargs: Unpack[CreateDatasetRequestTypeDef]
    ) -> CreateDatasetResponseTypeDef:
        """
        Used to create a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/create_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#create_dataset)
        """

    def create_dataset_content(
        self, **kwargs: Unpack[CreateDatasetContentRequestTypeDef]
    ) -> CreateDatasetContentResponseTypeDef:
        """
        Creates the content of a dataset by applying a <code>queryAction</code> (a SQL
        query) or a <code>containerAction</code> (executing a containerized
        application).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/create_dataset_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#create_dataset_content)
        """

    def create_datastore(
        self, **kwargs: Unpack[CreateDatastoreRequestTypeDef]
    ) -> CreateDatastoreResponseTypeDef:
        """
        Creates a data store, which is a repository for messages.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/create_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#create_datastore)
        """

    def create_pipeline(
        self, **kwargs: Unpack[CreatePipelineRequestTypeDef]
    ) -> CreatePipelineResponseTypeDef:
        """
        Creates a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/create_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#create_pipeline)
        """

    def delete_channel(
        self, **kwargs: Unpack[DeleteChannelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/delete_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#delete_channel)
        """

    def delete_dataset(
        self, **kwargs: Unpack[DeleteDatasetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/delete_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#delete_dataset)
        """

    def delete_dataset_content(
        self, **kwargs: Unpack[DeleteDatasetContentRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the content of the specified dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/delete_dataset_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#delete_dataset_content)
        """

    def delete_datastore(
        self, **kwargs: Unpack[DeleteDatastoreRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/delete_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#delete_datastore)
        """

    def delete_pipeline(
        self, **kwargs: Unpack[DeletePipelineRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/delete_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#delete_pipeline)
        """

    def describe_channel(
        self, **kwargs: Unpack[DescribeChannelRequestTypeDef]
    ) -> DescribeChannelResponseTypeDef:
        """
        Retrieves information about a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/describe_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#describe_channel)
        """

    def describe_dataset(
        self, **kwargs: Unpack[DescribeDatasetRequestTypeDef]
    ) -> DescribeDatasetResponseTypeDef:
        """
        Retrieves information about a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/describe_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#describe_dataset)
        """

    def describe_datastore(
        self, **kwargs: Unpack[DescribeDatastoreRequestTypeDef]
    ) -> DescribeDatastoreResponseTypeDef:
        """
        Retrieves information about a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/describe_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#describe_datastore)
        """

    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        Retrieves the current settings of the IoT Analytics logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/describe_logging_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#describe_logging_options)
        """

    def describe_pipeline(
        self, **kwargs: Unpack[DescribePipelineRequestTypeDef]
    ) -> DescribePipelineResponseTypeDef:
        """
        Retrieves information about a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/describe_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#describe_pipeline)
        """

    def get_dataset_content(
        self, **kwargs: Unpack[GetDatasetContentRequestTypeDef]
    ) -> GetDatasetContentResponseTypeDef:
        """
        Retrieves the contents of a dataset as presigned URIs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/get_dataset_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#get_dataset_content)
        """

    def list_channels(
        self, **kwargs: Unpack[ListChannelsRequestTypeDef]
    ) -> ListChannelsResponseTypeDef:
        """
        Retrieves a list of channels.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/list_channels.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#list_channels)
        """

    def list_dataset_contents(
        self, **kwargs: Unpack[ListDatasetContentsRequestTypeDef]
    ) -> ListDatasetContentsResponseTypeDef:
        """
        Lists information about dataset contents that have been created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/list_dataset_contents.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#list_dataset_contents)
        """

    def list_datasets(
        self, **kwargs: Unpack[ListDatasetsRequestTypeDef]
    ) -> ListDatasetsResponseTypeDef:
        """
        Retrieves information about datasets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/list_datasets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#list_datasets)
        """

    def list_datastores(
        self, **kwargs: Unpack[ListDatastoresRequestTypeDef]
    ) -> ListDatastoresResponseTypeDef:
        """
        Retrieves a list of data stores.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/list_datastores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#list_datastores)
        """

    def list_pipelines(
        self, **kwargs: Unpack[ListPipelinesRequestTypeDef]
    ) -> ListPipelinesResponseTypeDef:
        """
        Retrieves a list of pipelines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/list_pipelines.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#list_pipelines)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists the tags (metadata) that you have assigned to the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#list_tags_for_resource)
        """

    def put_logging_options(
        self, **kwargs: Unpack[PutLoggingOptionsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sets or updates the IoT Analytics logging options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/put_logging_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#put_logging_options)
        """

    def run_pipeline_activity(
        self, **kwargs: Unpack[RunPipelineActivityRequestTypeDef]
    ) -> RunPipelineActivityResponseTypeDef:
        """
        Simulates the results of running a pipeline activity on a message payload.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/run_pipeline_activity.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#run_pipeline_activity)
        """

    def sample_channel_data(
        self, **kwargs: Unpack[SampleChannelDataRequestTypeDef]
    ) -> SampleChannelDataResponseTypeDef:
        """
        Retrieves a sample of messages from the specified channel ingested during the
        specified timeframe.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/sample_channel_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#sample_channel_data)
        """

    def start_pipeline_reprocessing(
        self, **kwargs: Unpack[StartPipelineReprocessingRequestTypeDef]
    ) -> StartPipelineReprocessingResponseTypeDef:
        """
        Starts the reprocessing of raw message data through the pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/start_pipeline_reprocessing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#start_pipeline_reprocessing)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds to or modifies the tags of the given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes the given tags (metadata) from the resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#untag_resource)
        """

    def update_channel(
        self, **kwargs: Unpack[UpdateChannelRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used to update the settings of a channel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/update_channel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#update_channel)
        """

    def update_dataset(
        self, **kwargs: Unpack[UpdateDatasetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the settings of a dataset.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/update_dataset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#update_dataset)
        """

    def update_datastore(
        self, **kwargs: Unpack[UpdateDatastoreRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Used to update the settings of a data store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/update_datastore.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#update_datastore)
        """

    def update_pipeline(
        self, **kwargs: Unpack[UpdatePipelineRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Updates the settings of a pipeline.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/update_pipeline.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#update_pipeline)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_channels"]
    ) -> ListChannelsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_dataset_contents"]
    ) -> ListDatasetContentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_datasets"]
    ) -> ListDatasetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_datastores"]
    ) -> ListDatastoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_pipelines"]
    ) -> ListPipelinesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client/#get_paginator)
        """
