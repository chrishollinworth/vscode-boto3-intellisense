"""
Type annotations for emr-containers service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_emr_containers.client import EMRContainersClient
    from mypy_boto3_emr_containers.paginator import (
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

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListJobRunsRequestPaginateTypeDef,
    ListJobRunsResponsePaginatorTypeDef,
    ListJobRunsResponseTypeDef,
    ListJobTemplatesRequestPaginateTypeDef,
    ListJobTemplatesResponsePaginatorTypeDef,
    ListManagedEndpointsRequestPaginateTypeDef,
    ListManagedEndpointsResponsePaginatorTypeDef,
    ListSecurityConfigurationsRequestPaginateTypeDef,
    ListSecurityConfigurationsResponseTypeDef,
    ListVirtualClustersRequestPaginateTypeDef,
    ListVirtualClustersResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListJobRunsPaginator",
    "ListJobTemplatesPaginator",
    "ListManagedEndpointsPaginator",
    "ListSecurityConfigurationsPaginator",
    "ListVirtualClustersPaginator",
)

if TYPE_CHECKING:
    _ListJobRunsPaginatorBase = Paginator[ListJobRunsResponseTypeDef]
else:
    _ListJobRunsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobRunsPaginator(_ListJobRunsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListJobRuns.html#EMRContainers.Paginator.ListJobRuns)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listjobrunspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobRunsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobRunsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListJobRuns.html#EMRContainers.Paginator.ListJobRuns.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listjobrunspaginator)
        """

if TYPE_CHECKING:
    _ListJobTemplatesPaginatorBase = Paginator[ListJobTemplatesResponsePaginatorTypeDef]
else:
    _ListJobTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobTemplatesPaginator(_ListJobTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListJobTemplates.html#EMRContainers.Paginator.ListJobTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listjobtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[ListJobTemplatesResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListJobTemplates.html#EMRContainers.Paginator.ListJobTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listjobtemplatespaginator)
        """

if TYPE_CHECKING:
    _ListManagedEndpointsPaginatorBase = Paginator[ListManagedEndpointsResponsePaginatorTypeDef]
else:
    _ListManagedEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class ListManagedEndpointsPaginator(_ListManagedEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListManagedEndpoints.html#EMRContainers.Paginator.ListManagedEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listmanagedendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListManagedEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[ListManagedEndpointsResponsePaginatorTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListManagedEndpoints.html#EMRContainers.Paginator.ListManagedEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listmanagedendpointspaginator)
        """

if TYPE_CHECKING:
    _ListSecurityConfigurationsPaginatorBase = Paginator[ListSecurityConfigurationsResponseTypeDef]
else:
    _ListSecurityConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSecurityConfigurationsPaginator(_ListSecurityConfigurationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListSecurityConfigurations.html#EMRContainers.Paginator.ListSecurityConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listsecurityconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSecurityConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[ListSecurityConfigurationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListSecurityConfigurations.html#EMRContainers.Paginator.ListSecurityConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listsecurityconfigurationspaginator)
        """

if TYPE_CHECKING:
    _ListVirtualClustersPaginatorBase = Paginator[ListVirtualClustersResponseTypeDef]
else:
    _ListVirtualClustersPaginatorBase = Paginator  # type: ignore[assignment]

class ListVirtualClustersPaginator(_ListVirtualClustersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListVirtualClusters.html#EMRContainers.Paginator.ListVirtualClusters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listvirtualclusterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListVirtualClustersRequestPaginateTypeDef]
    ) -> PageIterator[ListVirtualClustersResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr-containers/paginator/ListVirtualClusters.html#EMRContainers.Paginator.ListVirtualClusters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators/#listvirtualclusterspaginator)
        """
