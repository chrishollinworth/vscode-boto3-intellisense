"""
Type annotations for serverlessrepo service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_serverlessrepo.client import ServerlessApplicationRepositoryClient
    from mypy_boto3_serverlessrepo.paginator import (
        ListApplicationDependenciesPaginator,
        ListApplicationVersionsPaginator,
        ListApplicationsPaginator,
    )

    session = Session()
    client: ServerlessApplicationRepositoryClient = session.client("serverlessrepo")

    list_application_dependencies_paginator: ListApplicationDependenciesPaginator = client.get_paginator("list_application_dependencies")
    list_application_versions_paginator: ListApplicationVersionsPaginator = client.get_paginator("list_application_versions")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListApplicationDependenciesRequestPaginateTypeDef,
    ListApplicationDependenciesResponseTypeDef,
    ListApplicationsRequestPaginateTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsRequestPaginateTypeDef,
    ListApplicationVersionsResponseTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListApplicationDependenciesPaginator",
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
)

if TYPE_CHECKING:
    _ListApplicationDependenciesPaginatorBase = Paginator[
        ListApplicationDependenciesResponseTypeDef
    ]
else:
    _ListApplicationDependenciesPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationDependenciesPaginator(_ListApplicationDependenciesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/paginator/ListApplicationDependencies.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators/#listapplicationdependenciespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationDependenciesRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationDependenciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/paginator/ListApplicationDependencies.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators/#listapplicationdependenciespaginator)
        """

if TYPE_CHECKING:
    _ListApplicationVersionsPaginatorBase = Paginator[ListApplicationVersionsResponseTypeDef]
else:
    _ListApplicationVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationVersionsPaginator(_ListApplicationVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/paginator/ListApplicationVersions.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators/#listapplicationversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/paginator/ListApplicationVersions.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators/#listapplicationversionspaginator)
        """

if TYPE_CHECKING:
    _ListApplicationsPaginatorBase = Paginator[ListApplicationsResponseTypeDef]
else:
    _ListApplicationsPaginatorBase = Paginator  # type: ignore[assignment]

class ListApplicationsPaginator(_ListApplicationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/paginator/ListApplications.html#ServerlessApplicationRepository.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators/#listapplicationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListApplicationsRequestPaginateTypeDef]
    ) -> PageIterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/serverlessrepo/paginator/ListApplications.html#ServerlessApplicationRepository.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators/#listapplicationspaginator)
        """
