"""
Type annotations for amplify service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_amplify.client import AmplifyClient
    from mypy_boto3_amplify.paginator import (
        ListAppsPaginator,
        ListBranchesPaginator,
        ListDomainAssociationsPaginator,
        ListJobsPaginator,
    )

    session = Session()
    client: AmplifyClient = session.client("amplify")

    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    list_branches_paginator: ListBranchesPaginator = client.get_paginator("list_branches")
    list_domain_associations_paginator: ListDomainAssociationsPaginator = client.get_paginator("list_domain_associations")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAppsRequestPaginateTypeDef,
    ListAppsResultTypeDef,
    ListBranchesRequestPaginateTypeDef,
    ListBranchesResultTypeDef,
    ListDomainAssociationsRequestPaginateTypeDef,
    ListDomainAssociationsResultTypeDef,
    ListJobsRequestPaginateTypeDef,
    ListJobsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAppsPaginator",
    "ListBranchesPaginator",
    "ListDomainAssociationsPaginator",
    "ListJobsPaginator",
)

if TYPE_CHECKING:
    _ListAppsPaginatorBase = Paginator[ListAppsResultTypeDef]
else:
    _ListAppsPaginatorBase = Paginator  # type: ignore[assignment]

class ListAppsPaginator(_ListAppsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/paginator/ListApps.html#Amplify.Paginator.ListApps)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/#listappspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAppsRequestPaginateTypeDef]
    ) -> PageIterator[ListAppsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/paginator/ListApps.html#Amplify.Paginator.ListApps.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/#listappspaginator)
        """

if TYPE_CHECKING:
    _ListBranchesPaginatorBase = Paginator[ListBranchesResultTypeDef]
else:
    _ListBranchesPaginatorBase = Paginator  # type: ignore[assignment]

class ListBranchesPaginator(_ListBranchesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/paginator/ListBranches.html#Amplify.Paginator.ListBranches)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/#listbranchespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListBranchesRequestPaginateTypeDef]
    ) -> PageIterator[ListBranchesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/paginator/ListBranches.html#Amplify.Paginator.ListBranches.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/#listbranchespaginator)
        """

if TYPE_CHECKING:
    _ListDomainAssociationsPaginatorBase = Paginator[ListDomainAssociationsResultTypeDef]
else:
    _ListDomainAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainAssociationsPaginator(_ListDomainAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/paginator/ListDomainAssociations.html#Amplify.Paginator.ListDomainAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/#listdomainassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[ListDomainAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/paginator/ListDomainAssociations.html#Amplify.Paginator.ListDomainAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/#listdomainassociationspaginator)
        """

if TYPE_CHECKING:
    _ListJobsPaginatorBase = Paginator[ListJobsResultTypeDef]
else:
    _ListJobsPaginatorBase = Paginator  # type: ignore[assignment]

class ListJobsPaginator(_ListJobsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/paginator/ListJobs.html#Amplify.Paginator.ListJobs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/#listjobspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListJobsRequestPaginateTypeDef]
    ) -> PageIterator[ListJobsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/amplify/paginator/ListJobs.html#Amplify.Paginator.ListJobs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_amplify/paginators/#listjobspaginator)
        """
