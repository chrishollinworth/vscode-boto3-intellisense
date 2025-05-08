"""
Main interface for emr-containers service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_emr_containers import (
        Client,
        EMRContainersClient,
        ListJobRunsPaginator,
        ListJobTemplatesPaginator,
        ListManagedEndpointsPaginator,
        ListSecurityConfigurationsPaginator,
        ListVirtualClustersPaginator,
    )

    session = Session()
    client: EMRContainersClient = session.client("emr-containers")

    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    list_job_templates_paginator: ListJobTemplatesPaginator = client.get_paginator("list_job_templates")
    list_managed_endpoints_paginator: ListManagedEndpointsPaginator = client.get_paginator("list_managed_endpoints")
    list_security_configurations_paginator: ListSecurityConfigurationsPaginator = client.get_paginator("list_security_configurations")
    list_virtual_clusters_paginator: ListVirtualClustersPaginator = client.get_paginator("list_virtual_clusters")
    ```
"""

from .client import EMRContainersClient
from .paginator import (
    ListJobRunsPaginator,
    ListJobTemplatesPaginator,
    ListManagedEndpointsPaginator,
    ListSecurityConfigurationsPaginator,
    ListVirtualClustersPaginator,
)

Client = EMRContainersClient

__all__ = (
    "Client",
    "EMRContainersClient",
    "ListJobRunsPaginator",
    "ListJobTemplatesPaginator",
    "ListManagedEndpointsPaginator",
    "ListSecurityConfigurationsPaginator",
    "ListVirtualClustersPaginator",
)
