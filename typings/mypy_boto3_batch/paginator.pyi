"""
Type annotations for batch service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_batch.client import BatchClient
    from mypy_boto3_batch.paginator import (
        DescribeComputeEnvironmentsPaginator,
        DescribeJobDefinitionsPaginator,
        DescribeJobQueuesPaginator,
        DescribeServiceEnvironmentsPaginator,
        ListConsumableResourcesPaginator,
        ListJobsByConsumableResourcePaginator,
        ListJobsPaginator,
        ListSchedulingPoliciesPaginator,
        ListServiceJobsPaginator,
    )

    session = Session()
    client: BatchClient = session.client("batch")

    describe_compute_environments_paginator: DescribeComputeEnvironmentsPaginator = client.get_paginator("describe_compute_environments")
    describe_job_definitions_paginator: DescribeJobDefinitionsPaginator = client.get_paginator("describe_job_definitions")
    describe_job_queues_paginator: DescribeJobQueuesPaginator = client.get_paginator("describe_job_queues")
    describe_service_environments_paginator: DescribeServiceEnvironmentsPaginator = client.get_paginator("describe_service_environments")
    list_consumable_resources_paginator: ListConsumableResourcesPaginator = client.get_paginator("list_consumable_resources")
    list_jobs_by_consumable_resource_paginator: ListJobsByConsumableResourcePaginator = client.get_paginator("list_jobs_by_consumable_resource")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_scheduling_policies_paginator: ListSchedulingPoliciesPaginator = client.get_paginator("list_scheduling_policies")
    list_service_jobs_paginator: ListServiceJobsPaginator = client.get_paginator("list_service_jobs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeComputeEnvironmentsRequestPaginateTypeDef,
    DescribeComputeEnvironmentsResponseTypeDef,
    DescribeJobDefinitionsRequestPaginateTypeDef,
    DescribeJobDefinitionsResponseTypeDef,
    DescribeJobQueuesRequestPaginateTypeDef,
    DescribeJobQueuesResponseTypeDef,
    DescribeServiceEnvironmentsRequestPaginateTypeDef,
    DescribeServiceEnvironmentsResponseTypeDef,
    ListConsumableResourcesRequestPaginateTypeDef,
    ListConsumableResourcesResponseTypeDef,
    ListJobsByConsumableResourceRequestPaginateTypeDef,
    ListJobsByConsumableResourceResponseTypeDef,
    ListJobsRequestPaginateTypeDef,
    ListJobsResponseTypeDef,
    ListSchedulingPoliciesRequestPaginateTypeDef,
    ListSchedulingPoliciesResponseTypeDef,
    ListServiceJobsRequestPaginateTypeDef,
    ListServiceJobsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeComputeEnvironmentsPaginator",
    "DescribeJobDefinitionsPaginator",
    "DescribeJobQueuesPaginator",
    "DescribeServiceEnvironmentsPaginator",
    "ListConsumableResourcesPaginator",
    "ListJobsByConsumableResourcePaginator",
    "ListJobsPaginator",
    "ListSchedulingPoliciesPaginator",
    "ListServiceJobsPaginator",
)

if TYPE_CHECKING:
    _DescribeComputeEnvironmentsPaginatorBase = Paginator[
        DescribeComputeEnvironmentsResponseTypeDef
    ]
else:
    _DescribeComputeEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeComputeEnvironmentsPaginator(_DescribeComputeEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/DescribeComputeEnvironments.html#Batch.Paginator.DescribeComputeEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#describecomputeenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeComputeEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeComputeEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/DescribeComputeEnvironments.html#Batch.Paginator.DescribeComputeEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#describecomputeenvironmentspaginator)
        """

if TYPE_CHECKING:
    _DescribeJobDefinitionsPaginatorBase = Paginator[DescribeJobDefinitionsResponseTypeDef]
else:
    _DescribeJobDefinitionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeJobDefinitionsPaginator(_DescribeJobDefinitionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/DescribeJobDefinitions.html#Batch.Paginator.DescribeJobDefinitions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#describejobdefinitionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeJobDefinitionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeJobDefinitionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/DescribeJobDefinitions.html#Batch.Paginator.DescribeJobDefinitions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#describejobdefinitionspaginator)
        """

if TYPE_CHECKING:
    _DescribeJobQueuesPaginatorBase = Paginator[DescribeJobQueuesResponseTypeDef]
else:
    _DescribeJobQueuesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeJobQueuesPaginator(_DescribeJobQueuesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/DescribeJobQueues.html#Batch.Paginator.DescribeJobQueues)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#describejobqueuespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeJobQueuesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeJobQueuesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/DescribeJobQueues.html#Batch.Paginator.DescribeJobQueues.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#describejobqueuespaginator)
        """

if TYPE_CHECKING:
    _DescribeServiceEnvironmentsPaginatorBase = Paginator[
        DescribeServiceEnvironmentsResponseTypeDef
    ]
else:
    _DescribeServiceEnvironmentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeServiceEnvironmentsPaginator(_DescribeServiceEnvironmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/DescribeServiceEnvironments.html#Batch.Paginator.DescribeServiceEnvironments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#describeserviceenvironmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeServiceEnvironmentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeServiceEnvironmentsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/DescribeServiceEnvironments.html#Batch.Paginator.DescribeServiceEnvironments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#describeserviceenvironmentspaginator)
        """

if TYPE_CHECKING:
    _ListConsumableResourcesPaginatorBase = Paginator[ListConsumableResourcesResponseTypeDef]
else:
    _ListConsumableResourcesPaginatorBase = Paginator  # type: ignore[assignment]

class ListConsumableResourcesPaginator(_ListConsumableResourcesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListConsumableResources.html#Batch.Paginator.ListConsumableResources)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listconsumableresourcespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListConsumableResourcesRequestPaginateTypeDef]
    ) -> PageIterator[ListConsumableResourcesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListConsumableResources.html#Batch.Paginator.ListConsumableResources.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listconsumableresourcespaginator)
        """

if TYPE_CHECKING:
    _ListJobsByConsumableResourcePaginatorBase = Paginator[
        ListJobsByConsumableResourceResponseTypeDef
    ]
else:
    _ListJobsByConsumableResourcePaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsByConsumableResourcePaginator(_ListJobsByConsumableResourcePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListJobsByConsumableResource.html#Batch.Paginator.ListJobsByConsumableResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listjobsbyconsumableresourcepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsByConsumableResourceRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsByConsumableResourceResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListJobsByConsumableResource.html#Batch.Paginator.ListJobsByConsumableResource.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listjobsbyconsumableresourcepaginator)
        """

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsResponseTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListJobs.html#Batch.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListJobs.html#Batch.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listjobspaginator)
        """

if TYPE_CHECKING:
    _ListSchedulingPoliciesPaginatorBase = Paginator[ListSchedulingPoliciesResponseTypeDef]
else:
    _ListSchedulingPoliciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchedulingPoliciesPaginator(_ListSchedulingPoliciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListSchedulingPolicies.html#Batch.Paginator.ListSchedulingPolicies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listschedulingpoliciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchedulingPoliciesRequestPaginateTypeDef]
    ) -> PageIterator[ListSchedulingPoliciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListSchedulingPolicies.html#Batch.Paginator.ListSchedulingPolicies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listschedulingpoliciespaginator)
        """

if TYPE_CHECKING:
    _ListServiceJobsPaginatorBase = Paginator[ListServiceJobsResponseTypeDef]
else:
    _ListServiceJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListServiceJobsPaginator(_ListServiceJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListServiceJobs.html#Batch.Paginator.ListServiceJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listservicejobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListServiceJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListServiceJobsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch/paginator/ListServiceJobs.html#Batch.Paginator.ListServiceJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_batch/paginators/#listservicejobspaginator)
        """
