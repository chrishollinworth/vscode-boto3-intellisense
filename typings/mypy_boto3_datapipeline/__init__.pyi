"""
Main interface for datapipeline service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_datapipeline import (
        Client,
        DataPipelineClient,
        DescribeObjectsPaginator,
        ListPipelinesPaginator,
        QueryObjectsPaginator,
    )

    session = Session()
    client: DataPipelineClient = session.client("datapipeline")

    describe_objects_paginator: DescribeObjectsPaginator = client.get_paginator("describe_objects")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    query_objects_paginator: QueryObjectsPaginator = client.get_paginator("query_objects")
    ```
"""

from .client import DataPipelineClient
from .paginator import DescribeObjectsPaginator, ListPipelinesPaginator, QueryObjectsPaginator

Client = DataPipelineClient

__all__ = (
    "Client",
    "DataPipelineClient",
    "DescribeObjectsPaginator",
    "ListPipelinesPaginator",
    "QueryObjectsPaginator",
)
