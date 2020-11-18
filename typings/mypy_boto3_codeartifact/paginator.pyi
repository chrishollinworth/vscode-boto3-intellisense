# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,unused-import
"""
Main interface for codeartifact service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_codeartifact import CodeArtifactClient
    from mypy_boto3_codeartifact.paginator import (
        ListDomainsPaginator,
        ListPackageVersionAssetsPaginator,
        ListPackageVersionsPaginator,
        ListPackagesPaginator,
        ListRepositoriesPaginator,
        ListRepositoriesInDomainPaginator,
    )

    client: CodeArtifactClient = boto3.client("codeartifact")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_package_version_assets_paginator: ListPackageVersionAssetsPaginator = client.get_paginator("list_package_version_assets")
    list_package_versions_paginator: ListPackageVersionsPaginator = client.get_paginator("list_package_versions")
    list_packages_paginator: ListPackagesPaginator = client.get_paginator("list_packages")
    list_repositories_paginator: ListRepositoriesPaginator = client.get_paginator("list_repositories")
    list_repositories_in_domain_paginator: ListRepositoriesInDomainPaginator = client.get_paginator("list_repositories_in_domain")
    ```
"""
import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codeartifact.type_defs import (
    ListDomainsResultTypeDef,
    ListPackagesResultTypeDef,
    ListPackageVersionAssetsResultTypeDef,
    ListPackageVersionsResultTypeDef,
    ListRepositoriesInDomainResultTypeDef,
    ListRepositoriesResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ListDomainsPaginator",
    "ListPackageVersionAssetsPaginator",
    "ListPackageVersionsPaginator",
    "ListPackagesPaginator",
    "ListRepositoriesPaginator",
    "ListRepositoriesInDomainPaginator",
)


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListDomains)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResultTypeDef]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListDomains.paginate)
        """


class ListPackageVersionAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListPackageVersionAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersionAssets)
    """

    def paginate(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        packageVersion: str,
        domainOwner: str = None,
        namespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPackageVersionAssetsResultTypeDef]:
        """
        [ListPackageVersionAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersionAssets.paginate)
        """


class ListPackageVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPackageVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersions)
    """

    def paginate(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        domainOwner: str = None,
        namespace: str = None,
        status: Literal[
            "Published", "Unfinished", "Unlisted", "Archived", "Disposed", "Deleted"
        ] = None,
        sortBy: Literal["PUBLISHED_TIME"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPackageVersionsResultTypeDef]:
        """
        [ListPackageVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersions.paginate)
        """


class ListPackagesPaginator(Boto3Paginator):
    """
    [Paginator.ListPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackages)
    """

    def paginate(
        self,
        domain: str,
        repository: str,
        domainOwner: str = None,
        format: Literal["npm", "pypi", "maven"] = None,
        namespace: str = None,
        packagePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPackagesResultTypeDef]:
        """
        [ListPackages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackages.paginate)
        """


class ListRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositories)
    """

    def paginate(
        self, repositoryPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesResultTypeDef]:
        """
        [ListRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositories.paginate)
        """


class ListRepositoriesInDomainPaginator(Boto3Paginator):
    """
    [Paginator.ListRepositoriesInDomain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositoriesInDomain)
    """

    def paginate(
        self,
        domain: str,
        domainOwner: str = None,
        administratorAccount: str = None,
        repositoryPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRepositoriesInDomainResultTypeDef]:
        """
        [ListRepositoriesInDomain.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositoriesInDomain.paginate)
        """
