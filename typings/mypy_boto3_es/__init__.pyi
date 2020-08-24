"""
Main interface for es service.

Usage::

    ```python
    import boto3
    from mypy_boto3_es import (
        Client,
        DescribeReservedElasticsearchInstanceOfferingsPaginator,
        DescribeReservedElasticsearchInstancesPaginator,
        ElasticsearchServiceClient,
        GetUpgradeHistoryPaginator,
        ListElasticsearchInstanceTypesPaginator,
        ListElasticsearchVersionsPaginator,
    )

    session = boto3.Session()

    client: ElasticsearchServiceClient = boto3.client("es")
    session_client: ElasticsearchServiceClient = session.client("es")

    describe_reserved_elasticsearch_instance_offerings_paginator: DescribeReservedElasticsearchInstanceOfferingsPaginator = client.get_paginator("describe_reserved_elasticsearch_instance_offerings")
    describe_reserved_elasticsearch_instances_paginator: DescribeReservedElasticsearchInstancesPaginator = client.get_paginator("describe_reserved_elasticsearch_instances")
    get_upgrade_history_paginator: GetUpgradeHistoryPaginator = client.get_paginator("get_upgrade_history")
    list_elasticsearch_instance_types_paginator: ListElasticsearchInstanceTypesPaginator = client.get_paginator("list_elasticsearch_instance_types")
    list_elasticsearch_versions_paginator: ListElasticsearchVersionsPaginator = client.get_paginator("list_elasticsearch_versions")
    ```
"""
from mypy_boto3_es.client import ElasticsearchServiceClient
from mypy_boto3_es.paginator import (
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
