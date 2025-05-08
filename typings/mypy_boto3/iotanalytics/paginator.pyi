"""
Type annotations for iotanalytics service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iotanalytics.client import IoTAnalyticsClient
    from mypy_boto3_iotanalytics.paginator import (
        ListChannelsPaginator,
        ListDatasetContentsPaginator,
        ListDatasetsPaginator,
        ListDatastoresPaginator,
        ListPipelinesPaginator,
    )

    session = Session()
    client: IoTAnalyticsClient = session.client("iotanalytics")

    list_channels_paginator: ListChannelsPaginator = client.get_paginator("list_channels")
    list_dataset_contents_paginator: ListDatasetContentsPaginator = client.get_paginator("list_dataset_contents")
    list_datasets_paginator: ListDatasetsPaginator = client.get_paginator("list_datasets")
    list_datastores_paginator: ListDatastoresPaginator = client.get_paginator("list_datastores")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListChannelsRequestPaginateTypeDef,
    ListChannelsResponseTypeDef,
    ListDatasetContentsRequestPaginateTypeDef,
    ListDatasetContentsResponseTypeDef,
    ListDatasetsRequestPaginateTypeDef,
    ListDatasetsResponseTypeDef,
    ListDatastoresRequestPaginateTypeDef,
    ListDatastoresResponseTypeDef,
    ListPipelinesRequestPaginateTypeDef,
    ListPipelinesResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListChannelsPaginator",
    "ListDatasetContentsPaginator",
    "ListDatasetsPaginator",
    "ListDatastoresPaginator",
    "ListPipelinesPaginator",
)

if TYPE_CHECKING:
    _ListChannelsPaginatorBase = Paginator[ListChannelsResponseTypeDef]
else:
    _ListChannelsPaginatorBase = Paginator  # type: ignore[assignment]

class ListChannelsPaginator(_ListChannelsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListChannels.html#IoTAnalytics.Paginator.ListChannels)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listchannelspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListChannelsRequestPaginateTypeDef]
    ) -> PageIterator[ListChannelsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListChannels.html#IoTAnalytics.Paginator.ListChannels.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listchannelspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetContentsPaginatorBase = Paginator[ListDatasetContentsResponseTypeDef]
else:
    _ListDatasetContentsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetContentsPaginator(_ListDatasetContentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListDatasetContents.html#IoTAnalytics.Paginator.ListDatasetContents)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listdatasetcontentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetContentsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetContentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListDatasetContents.html#IoTAnalytics.Paginator.ListDatasetContents.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listdatasetcontentspaginator)
        """

if TYPE_CHECKING:
    _ListDatasetsPaginatorBase = Paginator[ListDatasetsResponseTypeDef]
else:
    _ListDatasetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatasetsPaginator(_ListDatasetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListDatasets.html#IoTAnalytics.Paginator.ListDatasets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listdatasetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatasetsRequestPaginateTypeDef]
    ) -> PageIterator[ListDatasetsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListDatasets.html#IoTAnalytics.Paginator.ListDatasets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listdatasetspaginator)
        """

if TYPE_CHECKING:
    _ListDatastoresPaginatorBase = Paginator[ListDatastoresResponseTypeDef]
else:
    _ListDatastoresPaginatorBase = Paginator  # type: ignore[assignment]

class ListDatastoresPaginator(_ListDatastoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListDatastores.html#IoTAnalytics.Paginator.ListDatastores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listdatastorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDatastoresRequestPaginateTypeDef]
    ) -> PageIterator[ListDatastoresResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListDatastores.html#IoTAnalytics.Paginator.ListDatastores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listdatastorespaginator)
        """

if TYPE_CHECKING:
    _ListPipelinesPaginatorBase = Paginator[ListPipelinesResponseTypeDef]
else:
    _ListPipelinesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPipelinesPaginator(_ListPipelinesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListPipelines.html#IoTAnalytics.Paginator.ListPipelines)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listpipelinespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPipelinesRequestPaginateTypeDef]
    ) -> PageIterator[ListPipelinesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iotanalytics/paginator/ListPipelines.html#IoTAnalytics.Paginator.ListPipelines.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators/#listpipelinespaginator)
        """
