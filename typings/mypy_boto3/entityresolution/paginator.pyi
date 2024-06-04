"""
Type annotations for entityresolution service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_entityresolution import EntityResolutionClient
    from mypy_boto3_entityresolution.paginator import (
        ListIdMappingJobsPaginator,
        ListIdMappingWorkflowsPaginator,
        ListIdNamespacesPaginator,
        ListMatchingJobsPaginator,
        ListMatchingWorkflowsPaginator,
        ListProviderServicesPaginator,
        ListSchemaMappingsPaginator,
    )

    client: EntityResolutionClient = boto3.client("entityresolution")

    list_id_mapping_jobs_paginator: ListIdMappingJobsPaginator = client.get_paginator("list_id_mapping_jobs")
    list_id_mapping_workflows_paginator: ListIdMappingWorkflowsPaginator = client.get_paginator("list_id_mapping_workflows")
    list_id_namespaces_paginator: ListIdNamespacesPaginator = client.get_paginator("list_id_namespaces")
    list_matching_jobs_paginator: ListMatchingJobsPaginator = client.get_paginator("list_matching_jobs")
    list_matching_workflows_paginator: ListMatchingWorkflowsPaginator = client.get_paginator("list_matching_workflows")
    list_provider_services_paginator: ListProviderServicesPaginator = client.get_paginator("list_provider_services")
    list_schema_mappings_paginator: ListSchemaMappingsPaginator = client.get_paginator("list_schema_mappings")
    ```
"""

from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListIdMappingJobsOutputTypeDef,
    ListIdMappingWorkflowsOutputTypeDef,
    ListIdNamespacesOutputTypeDef,
    ListMatchingJobsOutputTypeDef,
    ListMatchingWorkflowsOutputTypeDef,
    ListProviderServicesOutputTypeDef,
    ListSchemaMappingsOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListIdMappingJobsPaginator",
    "ListIdMappingWorkflowsPaginator",
    "ListIdNamespacesPaginator",
    "ListMatchingJobsPaginator",
    "ListMatchingWorkflowsPaginator",
    "ListProviderServicesPaginator",
    "ListSchemaMappingsPaginator",
)

class ListIdMappingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListIdMappingJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listidmappingjobspaginator)
    """

    def paginate(
        self, *, workflowName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdMappingJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListIdMappingJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listidmappingjobspaginator)
        """

class ListIdMappingWorkflowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListIdMappingWorkflows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listidmappingworkflowspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdMappingWorkflowsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListIdMappingWorkflows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listidmappingworkflowspaginator)
        """

class ListIdNamespacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListIdNamespaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listidnamespacespaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListIdNamespacesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListIdNamespaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listidnamespacespaginator)
        """

class ListMatchingJobsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListMatchingJobs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listmatchingjobspaginator)
    """

    def paginate(
        self, *, workflowName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMatchingJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListMatchingJobs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listmatchingjobspaginator)
        """

class ListMatchingWorkflowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListMatchingWorkflows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listmatchingworkflowspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMatchingWorkflowsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListMatchingWorkflows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listmatchingworkflowspaginator)
        """

class ListProviderServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListProviderServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listproviderservicespaginator)
    """

    def paginate(
        self, *, providerName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListProviderServicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListProviderServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listproviderservicespaginator)
        """

class ListSchemaMappingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListSchemaMappings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listschemamappingspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSchemaMappingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/entityresolution.html#EntityResolution.Paginator.ListSchemaMappings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators.html#listschemamappingspaginator)
        """
