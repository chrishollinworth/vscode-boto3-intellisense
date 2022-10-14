"""
Type annotations for serverlessrepo service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_serverlessrepo import ServerlessApplicationRepositoryClient
    from mypy_boto3_serverlessrepo.paginator import (
        ListApplicationDependenciesPaginator,
        ListApplicationVersionsPaginator,
        ListApplicationsPaginator,
    )

    client: ServerlessApplicationRepositoryClient = boto3.client("serverlessrepo")

    list_application_dependencies_paginator: ListApplicationDependenciesPaginator = client.get_paginator("list_application_dependencies")
    list_application_versions_paginator: ListApplicationVersionsPaginator = client.get_paginator("list_application_versions")
    list_applications_paginator: ListApplicationsPaginator = client.get_paginator("list_applications")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListApplicationDependenciesResponseTypeDef,
    ListApplicationsResponseTypeDef,
    ListApplicationVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListApplicationDependenciesPaginator",
    "ListApplicationVersionsPaginator",
    "ListApplicationsPaginator",
)

class ListApplicationDependenciesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators.html#listapplicationdependenciespaginator)
    """

    def paginate(
        self,
        *,
        ApplicationId: str,
        SemanticVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationDependenciesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationDependencies.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators.html#listapplicationdependenciespaginator)
        """

class ListApplicationVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators.html#listapplicationversionspaginator)
    """

    def paginate(
        self, *, ApplicationId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationVersionsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplicationVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators.html#listapplicationversionspaginator)
        """

class ListApplicationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators.html#listapplicationspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListApplicationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.24.89/reference/services/serverlessrepo.html#ServerlessApplicationRepository.Paginator.ListApplications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/paginators.html#listapplicationspaginator)
        """
