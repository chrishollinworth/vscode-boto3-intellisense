# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for batch service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_batch import BatchClient
    from mypy_boto3_batch.paginator import (
        DescribeComputeEnvironmentsPaginator,
        DescribeJobDefinitionsPaginator,
        DescribeJobQueuesPaginator,
        ListJobsPaginator,
    )

    client: BatchClient = boto3.client("batch")

    describe_compute_environments_paginator: DescribeComputeEnvironmentsPaginator = client.get_paginator("describe_compute_environments")
    describe_job_definitions_paginator: DescribeJobDefinitionsPaginator = client.get_paginator("describe_job_definitions")
    describe_job_queues_paginator: DescribeJobQueuesPaginator = client.get_paginator("describe_job_queues")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""
import sys
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_batch.type_defs import (
    DescribeComputeEnvironmentsResponseTypeDef,
    DescribeJobDefinitionsResponseTypeDef,
    DescribeJobQueuesResponseTypeDef,
    ListJobsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeComputeEnvironmentsPaginator",
    "DescribeJobDefinitionsPaginator",
    "DescribeJobQueuesPaginator",
    "ListJobsPaginator",
)


class DescribeComputeEnvironmentsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeComputeEnvironments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments)
    """

    def paginate(
        self, computeEnvironments: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeComputeEnvironmentsResponseTypeDef]:
        """
        [DescribeComputeEnvironments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeComputeEnvironments.paginate)
        """


class DescribeJobDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions)
    """

    def paginate(
        self,
        jobDefinitions: List[str] = None,
        jobDefinitionName: str = None,
        status: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeJobDefinitionsResponseTypeDef]:
        """
        [DescribeJobDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeJobDefinitions.paginate)
        """


class DescribeJobQueuesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeJobQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeJobQueues)
    """

    def paginate(
        self, jobQueues: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeJobQueuesResponseTypeDef]:
        """
        [DescribeJobQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.DescribeJobQueues.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.ListJobs)
    """

    def paginate(
        self,
        jobQueue: str = None,
        arrayJobId: str = None,
        multiNodeJobId: str = None,
        jobStatus: Literal[
            "SUBMITTED", "PENDING", "RUNNABLE", "STARTING", "RUNNING", "SUCCEEDED", "FAILED"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobsResponseTypeDef]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/batch.html#Batch.Paginator.ListJobs.paginate)
        """
