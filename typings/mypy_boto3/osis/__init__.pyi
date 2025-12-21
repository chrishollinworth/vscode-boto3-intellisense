"""
Main interface for osis service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_osis/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_osis import (
        Client,
        ListPipelineEndpointConnectionsPaginator,
        ListPipelineEndpointsPaginator,
        OpenSearchIngestionClient,
    )

    session = Session()
    client: OpenSearchIngestionClient = session.client("osis")

    list_pipeline_endpoint_connections_paginator: ListPipelineEndpointConnectionsPaginator = client.get_paginator("list_pipeline_endpoint_connections")
    list_pipeline_endpoints_paginator: ListPipelineEndpointsPaginator = client.get_paginator("list_pipeline_endpoints")
    ```
"""

from .client import OpenSearchIngestionClient
from .paginator import ListPipelineEndpointConnectionsPaginator, ListPipelineEndpointsPaginator

Client = OpenSearchIngestionClient

__all__ = (
    "Client",
    "ListPipelineEndpointConnectionsPaginator",
    "ListPipelineEndpointsPaginator",
    "OpenSearchIngestionClient",
)
