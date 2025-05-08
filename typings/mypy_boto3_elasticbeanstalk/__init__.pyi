"""
Main interface for elasticbeanstalk service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_elasticbeanstalk import (
        Client,
        DescribeApplicationVersionsPaginator,
        DescribeEnvironmentManagedActionHistoryPaginator,
        DescribeEnvironmentsPaginator,
        DescribeEventsPaginator,
        ElasticBeanstalkClient,
        EnvironmentExistsWaiter,
        EnvironmentTerminatedWaiter,
        EnvironmentUpdatedWaiter,
        ListPlatformVersionsPaginator,
    )

    session = Session()
    client: ElasticBeanstalkClient = session.client("elasticbeanstalk")

    environment_exists_waiter: EnvironmentExistsWaiter = client.get_waiter("environment_exists")
    environment_terminated_waiter: EnvironmentTerminatedWaiter = client.get_waiter("environment_terminated")
    environment_updated_waiter: EnvironmentUpdatedWaiter = client.get_waiter("environment_updated")

    describe_application_versions_paginator: DescribeApplicationVersionsPaginator = client.get_paginator("describe_application_versions")
    describe_environment_managed_action_history_paginator: DescribeEnvironmentManagedActionHistoryPaginator = client.get_paginator("describe_environment_managed_action_history")
    describe_environments_paginator: DescribeEnvironmentsPaginator = client.get_paginator("describe_environments")
    describe_events_paginator: DescribeEventsPaginator = client.get_paginator("describe_events")
    list_platform_versions_paginator: ListPlatformVersionsPaginator = client.get_paginator("list_platform_versions")
    ```
"""

from .client import ElasticBeanstalkClient
from .paginator import (
    DescribeApplicationVersionsPaginator,
    DescribeEnvironmentManagedActionHistoryPaginator,
    DescribeEnvironmentsPaginator,
    DescribeEventsPaginator,
    ListPlatformVersionsPaginator,
)
from .waiter import EnvironmentExistsWaiter, EnvironmentTerminatedWaiter, EnvironmentUpdatedWaiter

Client = ElasticBeanstalkClient

__all__ = (
    "Client",
    "DescribeApplicationVersionsPaginator",
    "DescribeEnvironmentManagedActionHistoryPaginator",
    "DescribeEnvironmentsPaginator",
    "DescribeEventsPaginator",
    "ElasticBeanstalkClient",
    "EnvironmentExistsWaiter",
    "EnvironmentTerminatedWaiter",
    "EnvironmentUpdatedWaiter",
    "ListPlatformVersionsPaginator",
)
