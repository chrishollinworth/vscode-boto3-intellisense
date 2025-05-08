"""
Main interface for dax service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_dax/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
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

    session = Session()
    client: DAXClient = session.client("dax")

    describe_clusters_paginator: DescribeClustersPaginator = client.get_paginator("describe_clusters")
    describe_default_parameters_paginator: DescribeDefaultParametersPaginator = client.get_paginator("describe_default_parameters")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    describe_parameter_groups_paginator: DescribeParameterGroupsPaginator = client.get_paginator("describe_parameter_groups")
    describe_parameters_paginator: DescribeParametersPaginator = client.get_paginator("describe_parameters")
    describe_subnet_groups_paginator: DescribeSubnetGroupsPaginator = client.get_paginator("describe_subnet_groups")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    ```
"""

from .client import DAXClient
from .paginator import (
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
