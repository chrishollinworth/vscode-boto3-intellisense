# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for iotanalytics service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_iotanalytics import IoTAnalyticsClient
    from mypy_boto3_iotanalytics.paginator import (
        ListChannelsPaginator,
        ListDatasetContentsPaginator,
        ListDatasetsPaginator,
        ListDatastoresPaginator,
        ListPipelinesPaginator,
    )

    client: IoTAnalyticsClient = boto3.client("iotanalytics")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_dataset_contents_paginator: ListDatasetContentsPaginator = client.get_paginator("list_dataset_contents")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_datastores_paginator: ListDatastoresPaginator = client.get_paginator("list_datastores")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    ```
"""
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_iotanalytics.type_defs import (
    ListChannelsResponseTypeDef,
    ListDatasetContentsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListDatastoresResponseTypeDef,
    ListPipelinesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListChannelsPaginator",
    "ListDatasetContentsPaginator",
    "ListDatasetsPaginator",
    "ListDatastoresPaginator",
    "ListPipelinesPaginator",
)


class ListChannelsPaginator(Boto3Paginator):
    """
    [Paginator.ListChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListChannels)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListChannelsResponseTypeDef]:
        """
        [ListChannels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListChannels.paginate)
        """


class ListDatasetContentsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetContents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasetContents)
    """

    def paginate(
        self,
        datasetName: str,
        scheduledOnOrAfter: datetime = None,
        scheduledBefore: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDatasetContentsResponseTypeDef]:
        """
        [ListDatasetContents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasetContents.paginate)
        """


class ListDatasetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasets)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatasetsResponseTypeDef]:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasets.paginate)
        """


class ListDatastoresPaginator(Boto3Paginator):
    """
    [Paginator.ListDatastores documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatastores)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDatastoresResponseTypeDef]:
        """
        [ListDatastores.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatastores.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListPipelines)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelinesResponseTypeDef]:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListPipelines.paginate)
        """
