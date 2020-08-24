"""
Main interface for cloud9 service.

Usage::

    ```python
    import boto3
    from mypy_boto3_cloud9 import (
        Client,
        Cloud9Client,
        DescribeEnvironmentMembershipsPaginator,
        ListEnvironmentsPaginator,
    )

    session = boto3.Session()

    client: Cloud9Client = boto3.client("cloud9")
    session_client: Cloud9Client = session.client("cloud9")

    describe_environment_memberships_paginator: DescribeEnvironmentMembershipsPaginator = client.get_paginator("describe_environment_memberships")
    list_environments_paginator: ListEnvironmentsPaginator = client.get_paginator("list_environments")
    ```
"""
from mypy_boto3_cloud9.client import Cloud9Client
from mypy_boto3_cloud9.paginator import (
    DescribeEnvironmentMembershipsPaginator,
    ListEnvironmentsPaginator,
)

Client = Cloud9Client


__all__ = (
    "Client",
    "Cloud9Client",
    "DescribeEnvironmentMembershipsPaginator",
    "ListEnvironmentsPaginator",
)
