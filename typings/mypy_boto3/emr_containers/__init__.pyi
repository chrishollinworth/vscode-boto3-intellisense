"""
Main interface for emr-containers service.

Usage::

    ```python
    import boto3
    from mypy_boto3_emr_containers import (
        Client,
        EMRContainersClient,
        ListJobRunsPaginator,
        ListManagedEndpointsPaginator,
        ListVirtualClustersPaginator,
    )

    session = boto3.Session()

    client: EMRContainersClient = boto3.client("emr-containers")
    session_client: EMRContainersClient = session.client("emr-containers")

    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    list_managed_endpoints_paginator: ListManagedEndpointsPaginator = client.get_paginator("list_managed_endpoints")
    list_virtual_clusters_paginator: ListVirtualClustersPaginator = client.get_paginator("list_virtual_clusters")
    ```
"""
from .client import EMRContainersClient
from .paginator import (
    ListJobRunsPaginator,
    ListManagedEndpointsPaginator,
    ListVirtualClustersPaginator,
)

Client = EMRContainersClient

__all__ = (
    "Client",
    "EMRContainersClient",
    "ListJobRunsPaginator",
    "ListManagedEndpointsPaginator",
    "ListVirtualClustersPaginator",
)
