"""
Type annotations for codeartifact service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html)

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

from .literals import PackageFormatType, PackageVersionStatusType
from .type_defs import (
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listdomainspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listdomainspaginator)
        """

class ListPackageVersionAssetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersionAssets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackageversionassetspaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        repository: str,
        format: PackageFormatType,
        package: str,
        packageVersion: str,
        domainOwner: str = None,
        namespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackageVersionAssetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersionAssets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackageversionassetspaginator)
        """

class ListPackageVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackageversionspaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        repository: str,
        format: PackageFormatType,
        package: str,
        domainOwner: str = None,
        namespace: str = None,
        status: PackageVersionStatusType = None,
        sortBy: Literal["PUBLISHED_TIME"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackageVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackageversionspaginator)
        """

class ListPackagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackagespaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        repository: str,
        domainOwner: str = None,
        format: PackageFormatType = None,
        namespace: str = None,
        packagePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackagespaginator)
        """

class ListRepositoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listrepositoriespaginator)
    """

    def paginate(
        self, *, repositoryPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listrepositoriespaginator)
        """

class ListRepositoriesInDomainPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositoriesInDomain)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listrepositoriesindomainpaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        domainOwner: str = None,
        administratorAccount: str = None,
        repositoryPrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesInDomainResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.20.24/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositoriesInDomain.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listrepositoriesindomainpaginator)
        """
