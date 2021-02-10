"""
Main interface for emr-containers service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_emr_containers import EMRContainersClient
    from mypy_boto3_emr_containers.paginator import (
        ListJobRunsPaginator,
        ListManagedEndpointsPaginator,
        ListVirtualClustersPaginator,
    )

    client: EMRContainersClient = boto3.client("emr-containers")

    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    list_managed_endpoints_paginator: ListManagedEndpointsPaginator = client.get_paginator("list_managed_endpoints")
    list_virtual_clusters_paginator: ListVirtualClustersPaginator = client.get_paginator("list_virtual_clusters")
    ```
"""
import sys
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_emr_containers.type_defs import (
    ListJobRunsResponseTypeDef,
    ListManagedEndpointsResponseTypeDef,
    ListVirtualClustersResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ListJobRunsPaginator", "ListManagedEndpointsPaginator", "ListVirtualClustersPaginator")


class ListJobRunsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns)
    """

    def paginate(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        name: str = None,
        states: List[
            Literal[
                "PENDING",
                "SUBMITTED",
                "RUNNING",
                "FAILED",
                "CANCELLED",
                "CANCEL_PENDING",
                "COMPLETED",
            ]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        """
        [ListJobRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns.paginate)
        """


class ListManagedEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListManagedEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints)
    """

    def paginate(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        types: List[str] = None,
        states: List[
            Literal["CREATING", "ACTIVE", "TERMINATING", "TERMINATED", "TERMINATED_WITH_ERRORS"]
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListManagedEndpointsResponseTypeDef]:
        """
        [ListManagedEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints.paginate)
        """


class ListVirtualClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters)
    """

    def paginate(
        self,
        containerProviderId: str = None,
        containerProviderType: Literal["EKS"] = None,
        createdAfter: datetime = None,
        createdBefore: datetime = None,
        states: List[Literal["RUNNING", "TERMINATING", "TERMINATED", "ARRESTED"]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListVirtualClustersResponseTypeDef]:
        """
        [ListVirtualClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters.paginate)
        """
