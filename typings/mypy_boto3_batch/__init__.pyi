"""
Main interface for batch service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_batch import (
        BatchClient,
        Client,
        DescribeComputeEnvironmentsPaginator,
        DescribeJobDefinitionsPaginator,
        DescribeJobQueuesPaginator,
        ListConsumableResourcesPaginator,
        ListJobsByConsumableResourcePaginator,
        ListJobsPaginator,
        ListSchedulingPoliciesPaginator,
    )

    session = Session()
    client: BatchClient = session.client("batch")

    describe_compute_environments_paginator: DescribeComputeEnvironmentsPaginator = client.get_paginator("describe_compute_environments")
    describe_job_definitions_paginator: DescribeJobDefinitionsPaginator = client.get_paginator("describe_job_definitions")
    describe_job_queues_paginator: DescribeJobQueuesPaginator = client.get_paginator("describe_job_queues")
    list_consumable_resources_paginator: ListConsumableResourcesPaginator = client.get_paginator("list_consumable_resources")
    list_jobs_by_consumable_resource_paginator: ListJobsByConsumableResourcePaginator = client.get_paginator("list_jobs_by_consumable_resource")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_scheduling_policies_paginator: ListSchedulingPoliciesPaginator = client.get_paginator("list_scheduling_policies")
    ```
"""

from .client import BatchClient
from .paginator import (
    DescribeComputeEnvironmentsPaginator,
    DescribeJobDefinitionsPaginator,
    DescribeJobQueuesPaginator,
    ListConsumableResourcesPaginator,
    ListJobsByConsumableResourcePaginator,
    ListJobsPaginator,
    ListSchedulingPoliciesPaginator,
)

Client = BatchClient

__all__ = (
    "BatchClient",
    "Client",
    "DescribeComputeEnvironmentsPaginator",
    "DescribeJobDefinitionsPaginator",
    "DescribeJobQueuesPaginator",
    "ListConsumableResourcesPaginator",
    "ListJobsByConsumableResourcePaginator",
    "ListJobsPaginator",
    "ListSchedulingPoliciesPaginator",
)
