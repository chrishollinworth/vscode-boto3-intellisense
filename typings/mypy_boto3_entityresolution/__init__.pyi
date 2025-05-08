"""
Main interface for entityresolution service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_entityresolution import (
        Client,
        EntityResolutionClient,
        ListIdMappingJobsPaginator,
        ListIdMappingWorkflowsPaginator,
        ListIdNamespacesPaginator,
        ListMatchingJobsPaginator,
        ListMatchingWorkflowsPaginator,
        ListProviderServicesPaginator,
        ListSchemaMappingsPaginator,
    )

    session = Session()
    client: EntityResolutionClient = session.client("entityresolution")

    list_id_mapping_jobs_paginator: ListIdMappingJobsPaginator = client.get_paginator("list_id_mapping_jobs")
    list_id_mapping_workflows_paginator: ListIdMappingWorkflowsPaginator = client.get_paginator("list_id_mapping_workflows")
    list_id_namespaces_paginator: ListIdNamespacesPaginator = client.get_paginator("list_id_namespaces")
    list_matching_jobs_paginator: ListMatchingJobsPaginator = client.get_paginator("list_matching_jobs")
    list_matching_workflows_paginator: ListMatchingWorkflowsPaginator = client.get_paginator("list_matching_workflows")
    list_provider_services_paginator: ListProviderServicesPaginator = client.get_paginator("list_provider_services")
    list_schema_mappings_paginator: ListSchemaMappingsPaginator = client.get_paginator("list_schema_mappings")
    ```
"""

from .client import EntityResolutionClient
from .paginator import (
    ListIdMappingJobsPaginator,
    ListIdMappingWorkflowsPaginator,
    ListIdNamespacesPaginator,
    ListMatchingJobsPaginator,
    ListMatchingWorkflowsPaginator,
    ListProviderServicesPaginator,
    ListSchemaMappingsPaginator,
)

Client = EntityResolutionClient

__all__ = (
    "Client",
    "EntityResolutionClient",
    "ListIdMappingJobsPaginator",
    "ListIdMappingWorkflowsPaginator",
    "ListIdNamespacesPaginator",
    "ListMatchingJobsPaginator",
    "ListMatchingWorkflowsPaginator",
    "ListProviderServicesPaginator",
    "ListSchemaMappingsPaginator",
)
