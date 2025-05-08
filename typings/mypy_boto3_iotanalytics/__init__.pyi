"""
Main interface for iotanalytics service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_iotanalytics import (
        Client,
        IoTAnalyticsClient,
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

from .client import IoTAnalyticsClient
from .paginator import (
    ListChannelsPaginator,
    ListDatasetContentsPaginator,
    ListDatasetsPaginator,
    ListDatastoresPaginator,
    ListPipelinesPaginator,
)

Client = IoTAnalyticsClient

__all__ = (
    "Client",
    "IoTAnalyticsClient",
    "ListChannelsPaginator",
    "ListDatasetContentsPaginator",
    "ListDatasetsPaginator",
    "ListDatastoresPaginator",
    "ListPipelinesPaginator",
)
