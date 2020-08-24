"""
Main interface for batch service.

Usage::

    ```python
    import boto3
    from mypy_boto3_batch import (
        BatchClient,
        Client,
        DescribeComputeEnvironmentsPaginator,
        DescribeJobDefinitionsPaginator,
        DescribeJobQueuesPaginator,
        ListJobsPaginator,
    )

    session = boto3.Session()

    client: BatchClient = boto3.client("batch")
    session_client: BatchClient = session.client("batch")

    describe_compute_environments_paginator: DescribeComputeEnvironmentsPaginator = client.get_paginator("describe_compute_environments")
    describe_job_definitions_paginator: DescribeJobDefinitionsPaginator = client.get_paginator("describe_job_definitions")
    describe_job_queues_paginator: DescribeJobQueuesPaginator = client.get_paginator("describe_job_queues")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""
from mypy_boto3_batch.client import BatchClient
from mypy_boto3_batch.paginator import (
    DescribeComputeEnvironmentsPaginator,
    DescribeJobDefinitionsPaginator,
    DescribeJobQueuesPaginator,
    ListJobsPaginator,
)

Client = BatchClient


__all__ = (
    "BatchClient",
    "Client",
    "DescribeComputeEnvironmentsPaginator",
    "DescribeJobDefinitionsPaginator",
    "DescribeJobQueuesPaginator",
    "ListJobsPaginator",
)
