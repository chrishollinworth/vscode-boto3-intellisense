"""
Type annotations for emr-containers service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html)

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
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import EndpointStateType, JobRunStateType, VirtualClusterStateType
from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listjobrunspaginator)
    """

    def paginate(
        self,
        *,
        virtualClusterId: str,
        createdBefore: Union[datetime, str] = None,
        createdAfter: Union[datetime, str] = None,
        name: str = None,
        states: List[JobRunStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listjobrunspaginator)
        """

class ListManagedEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listmanagedendpointspaginator)
    """

    def paginate(
        self,
        *,
        virtualClusterId: str,
        createdBefore: Union[datetime, str] = None,
        createdAfter: Union[datetime, str] = None,
        types: List[str] = None,
        states: List[EndpointStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListManagedEndpointsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listmanagedendpointspaginator)
        """

class ListVirtualClustersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listvirtualclusterspaginator)
    """

    def paginate(
        self,
        *,
        containerProviderId: str = None,
        containerProviderType: Literal["EKS"] = None,
        createdAfter: Union[datetime, str] = None,
        createdBefore: Union[datetime, str] = None,
        states: List[VirtualClusterStateType] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListVirtualClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.13/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listvirtualclusterspaginator)
        """
