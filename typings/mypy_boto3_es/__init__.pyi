"""
Main interface for es service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_es/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_es import (
        Client,
        DescribeReservedElasticsearchInstanceOfferingsPaginator,
        DescribeReservedElasticsearchInstancesPaginator,
        ElasticsearchServiceClient,
        GetUpgradeHistoryPaginator,
        ListElasticsearchInstanceTypesPaginator,
        ListElasticsearchVersionsPaginator,
    )

    session = Session()
    client: ElasticsearchServiceClient = session.client("es")

    describe_reserved_elasticsearch_instance_offerings_paginator: DescribeReservedElasticsearchInstanceOfferingsPaginator = client.get_paginator("describe_reserved_elasticsearch_instance_offerings")
    describe_reserved_elasticsearch_instances_paginator: DescribeReservedElasticsearchInstancesPaginator = client.get_paginator("describe_reserved_elasticsearch_instances")
    get_upgrade_history_paginator: GetUpgradeHistoryPaginator = client.get_paginator("get_upgrade_history")
    list_elasticsearch_instance_types_paginator: ListElasticsearchInstanceTypesPaginator = client.get_paginator("list_elasticsearch_instance_types")
    list_elasticsearch_versions_paginator: ListElasticsearchVersionsPaginator = client.get_paginator("list_elasticsearch_versions")
    ```
"""

from .client import ElasticsearchServiceClient
from .paginator import (
    DescribeReservedElasticsearchInstanceOfferingsPaginator,
    DescribeReservedElasticsearchInstancesPaginator,
    GetUpgradeHistoryPaginator,
    ListElasticsearchInstanceTypesPaginator,
    ListElasticsearchVersionsPaginator,
)

Client = ElasticsearchServiceClient

__all__ = (
    "Client",
    "DescribeReservedElasticsearchInstanceOfferingsPaginator",
    "DescribeReservedElasticsearchInstancesPaginator",
    "ElasticsearchServiceClient",
    "GetUpgradeHistoryPaginator",
    "ListElasticsearchInstanceTypesPaginator",
    "ListElasticsearchVersionsPaginator",
)
