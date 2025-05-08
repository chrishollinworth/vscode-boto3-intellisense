"""
Main interface for discovery service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_discovery/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_discovery import (
        ApplicationDiscoveryServiceClient,
        Client,
        DescribeAgentsPaginator,
        DescribeContinuousExportsPaginator,
        DescribeExportConfigurationsPaginator,
        DescribeExportTasksPaginator,
        DescribeImportTasksPaginator,
        DescribeTagsPaginator,
        ListConfigurationsPaginator,
    )

    session = Session()
    client: ApplicationDiscoveryServiceClient = session.client("discovery")

    describe_agents_paginator: DescribeAgentsPaginator = client.get_paginator("describe_agents")
    describe_continuous_exports_paginator: DescribeContinuousExportsPaginator = client.get_paginator("describe_continuous_exports")
    describe_export_configurations_paginator: DescribeExportConfigurationsPaginator = client.get_paginator("describe_export_configurations")
    describe_export_tasks_paginator: DescribeExportTasksPaginator = client.get_paginator("describe_export_tasks")
    describe_import_tasks_paginator: DescribeImportTasksPaginator = client.get_paginator("describe_import_tasks")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    list_configurations_paginator: ListConfigurationsPaginator = client.get_paginator("list_configurations")
    ```
"""

from .client import ApplicationDiscoveryServiceClient
from .paginator import (
    DescribeAgentsPaginator,
    DescribeContinuousExportsPaginator,
    DescribeExportConfigurationsPaginator,
    DescribeExportTasksPaginator,
    DescribeImportTasksPaginator,
    DescribeTagsPaginator,
    ListConfigurationsPaginator,
)

Client = ApplicationDiscoveryServiceClient

__all__ = (
    "ApplicationDiscoveryServiceClient",
    "Client",
    "DescribeAgentsPaginator",
    "DescribeContinuousExportsPaginator",
    "DescribeExportConfigurationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeImportTasksPaginator",
    "DescribeTagsPaginator",
    "ListConfigurationsPaginator",
)
