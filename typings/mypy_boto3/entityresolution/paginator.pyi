"""
Type annotations for entityresolution service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_entityresolution.client import EntityResolutionClient
    from mypy_boto3_entityresolution.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListIdMappingJobsInputPaginateTypeDef,
    ListIdMappingJobsOutputTypeDef,
    ListIdMappingWorkflowsInputPaginateTypeDef,
    ListIdMappingWorkflowsOutputTypeDef,
    ListIdNamespacesInputPaginateTypeDef,
    ListIdNamespacesOutputTypeDef,
    ListMatchingJobsInputPaginateTypeDef,
    ListMatchingJobsOutputTypeDef,
    ListMatchingWorkflowsInputPaginateTypeDef,
    ListMatchingWorkflowsOutputTypeDef,
    ListProviderServicesInputPaginateTypeDef,
    ListProviderServicesOutputTypeDef,
    ListSchemaMappingsInputPaginateTypeDef,
    ListSchemaMappingsOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListIdMappingJobsPaginator",
    "ListIdMappingWorkflowsPaginator",
    "ListIdNamespacesPaginator",
    "ListMatchingJobsPaginator",
    "ListMatchingWorkflowsPaginator",
    "ListProviderServicesPaginator",
    "ListSchemaMappingsPaginator",
)

if TYPE_CHECKING:
    _ListIdMappingJobsPaginatorBase = Paginator[ListIdMappingJobsOutputTypeDef]
else:
    _ListIdMappingJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdMappingJobsPaginator(_ListIdMappingJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListIdMappingJobs.html#EntityResolution.Paginator.ListIdMappingJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listidmappingjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdMappingJobsInputPaginateTypeDef]
    ) -> PageIterator[ListIdMappingJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListIdMappingJobs.html#EntityResolution.Paginator.ListIdMappingJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listidmappingjobspaginator)
        """

if TYPE_CHECKING:
    _ListIdMappingWorkflowsPaginatorBase = Paginator[ListIdMappingWorkflowsOutputTypeDef]
else:
    _ListIdMappingWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdMappingWorkflowsPaginator(_ListIdMappingWorkflowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListIdMappingWorkflows.html#EntityResolution.Paginator.ListIdMappingWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listidmappingworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdMappingWorkflowsInputPaginateTypeDef]
    ) -> PageIterator[ListIdMappingWorkflowsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListIdMappingWorkflows.html#EntityResolution.Paginator.ListIdMappingWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listidmappingworkflowspaginator)
        """

if TYPE_CHECKING:
    _ListIdNamespacesPaginatorBase = Paginator[ListIdNamespacesOutputTypeDef]
else:
    _ListIdNamespacesPaginatorBase = Paginator  # type: ignore[assignment]

class ListIdNamespacesPaginator(_ListIdNamespacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListIdNamespaces.html#EntityResolution.Paginator.ListIdNamespaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listidnamespacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListIdNamespacesInputPaginateTypeDef]
    ) -> PageIterator[ListIdNamespacesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListIdNamespaces.html#EntityResolution.Paginator.ListIdNamespaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listidnamespacespaginator)
        """

if TYPE_CHECKING:
    _ListMatchingJobsPaginatorBase = Paginator[ListMatchingJobsOutputTypeDef]
else:
    _ListMatchingJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMatchingJobsPaginator(_ListMatchingJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListMatchingJobs.html#EntityResolution.Paginator.ListMatchingJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listmatchingjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMatchingJobsInputPaginateTypeDef]
    ) -> PageIterator[ListMatchingJobsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListMatchingJobs.html#EntityResolution.Paginator.ListMatchingJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listmatchingjobspaginator)
        """

if TYPE_CHECKING:
    _ListMatchingWorkflowsPaginatorBase = Paginator[ListMatchingWorkflowsOutputTypeDef]
else:
    _ListMatchingWorkflowsPaginatorBase = Paginator  # type: ignore[assignment]

class ListMatchingWorkflowsPaginator(_ListMatchingWorkflowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListMatchingWorkflows.html#EntityResolution.Paginator.ListMatchingWorkflows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listmatchingworkflowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListMatchingWorkflowsInputPaginateTypeDef]
    ) -> PageIterator[ListMatchingWorkflowsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListMatchingWorkflows.html#EntityResolution.Paginator.ListMatchingWorkflows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listmatchingworkflowspaginator)
        """

if TYPE_CHECKING:
    _ListProviderServicesPaginatorBase = Paginator[ListProviderServicesOutputTypeDef]
else:
    _ListProviderServicesPaginatorBase = Paginator  # type: ignore[assignment]

class ListProviderServicesPaginator(_ListProviderServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListProviderServices.html#EntityResolution.Paginator.ListProviderServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listproviderservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListProviderServicesInputPaginateTypeDef]
    ) -> PageIterator[ListProviderServicesOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListProviderServices.html#EntityResolution.Paginator.ListProviderServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listproviderservicespaginator)
        """

if TYPE_CHECKING:
    _ListSchemaMappingsPaginatorBase = Paginator[ListSchemaMappingsOutputTypeDef]
else:
    _ListSchemaMappingsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSchemaMappingsPaginator(_ListSchemaMappingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListSchemaMappings.html#EntityResolution.Paginator.ListSchemaMappings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listschemamappingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSchemaMappingsInputPaginateTypeDef]
    ) -> PageIterator[ListSchemaMappingsOutputTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/entityresolution/paginator/ListSchemaMappings.html#EntityResolution.Paginator.ListSchemaMappings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_entityresolution/paginators/#listschemamappingspaginator)
        """
