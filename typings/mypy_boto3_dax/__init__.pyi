"""
Main interface for dax service.

Usage::

    ```python
    import boto3
    from mypy_boto3_dax import (
        Client,
        DAXClient,
        DescribeClustersPaginator,
        DescribeDefaultParametersPaginator,
        DescribeEventsPaginator,
        DescribeParameterGroupsPaginator,
        DescribeParametersPaginator,
        DescribeSubnetGroupsPaginator,
        ListTagsPaginator,
    )

    session = boto3.Session()

    client: DAXClient = boto3.client("dax")
    session_client: DAXClient = session.client("dax")

    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_default_parameters_paginator: DescribeDefaultParametersPaginator = client.get_paginator("describe_default_parameters")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_parameter_groups_paginator: DescribeParameterGroupsPaginator = client.get_paginator("describe_parameter_groups")
    describe_parameters_paginator: DescribeParametersPaginator = client.get_paginator("describe_parameters")
    describe_subnet_groups_paginator: DescribeSubnetGroupsPaginator = client.get_paginator("describe_subnet_groups")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""
from mypy_boto3_dax.client import DAXClient
from mypy_boto3_dax.paginator import (
    DescribeClustersPaginator,
    DescribeDefaultParametersPaginator,
    DescribeEventsPaginator,
    DescribeParameterGroupsPaginator,
    DescribeParametersPaginator,
    DescribeSubnetGroupsPaginator,
    ListTagsPaginator,
)

Client = DAXClient


__all__ = (
    "Client",
    "DAXClient",
    "DescribeClustersPaginator",
    "DescribeDefaultParametersPaginator",
    "DescribeEventsPaginator",
    "DescribeParameterGroupsPaginator",
    "DescribeParametersPaginator",
    "DescribeSubnetGroupsPaginator",
    "ListTagsPaginator",
)
