"""
Type annotations for codeartifact service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_codeartifact.client import CodeArtifactClient
    from mypy_boto3_codeartifact.paginator import (
        ListAllowedRepositoriesForGroupPaginator,
        ListAssociatedPackagesPaginator,
        ListDomainsPaginator,
        ListPackageGroupsPaginator,
        ListPackageVersionAssetsPaginator,
        ListPackageVersionsPaginator,
        ListPackagesPaginator,
        ListRepositoriesInDomainPaginator,
        ListRepositoriesPaginator,
        ListSubPackageGroupsPaginator,
    )

    session = Session()
    client: CodeArtifactClient = session.client("codeartifact")

    list_allowed_repositories_for_group_paginator: ListAllowedRepositoriesForGroupPaginator = client.get_paginator("list_allowed_repositories_for_group")
    list_associated_packages_paginator: ListAssociatedPackagesPaginator = client.get_paginator("list_associated_packages")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_package_groups_paginator: ListPackageGroupsPaginator = client.get_paginator("list_package_groups")
    list_package_version_assets_paginator: ListPackageVersionAssetsPaginator = client.get_paginator("list_package_version_assets")
    list_package_versions_paginator: ListPackageVersionsPaginator = client.get_paginator("list_package_versions")
    list_packages_paginator: ListPackagesPaginator = client.get_paginator("list_packages")
    list_repositories_in_domain_paginator: ListRepositoriesInDomainPaginator = client.get_paginator("list_repositories_in_domain")
    list_repositories_paginator: ListRepositoriesPaginator = client.get_paginator("list_repositories")
    list_sub_package_groups_paginator: ListSubPackageGroupsPaginator = client.get_paginator("list_sub_package_groups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    ListAllowedRepositoriesForGroupRequestPaginateTypeDef,
    ListAllowedRepositoriesForGroupResultTypeDef,
    ListAssociatedPackagesRequestPaginateTypeDef,
    ListAssociatedPackagesResultTypeDef,
    ListDomainsRequestPaginateTypeDef,
    ListDomainsResultTypeDef,
    ListPackageGroupsRequestPaginateTypeDef,
    ListPackageGroupsResultTypeDef,
    ListPackagesRequestPaginateTypeDef,
    ListPackagesResultTypeDef,
    ListPackageVersionAssetsRequestPaginateTypeDef,
    ListPackageVersionAssetsResultTypeDef,
    ListPackageVersionsRequestPaginateTypeDef,
    ListPackageVersionsResultTypeDef,
    ListRepositoriesInDomainRequestPaginateTypeDef,
    ListRepositoriesInDomainResultTypeDef,
    ListRepositoriesRequestPaginateTypeDef,
    ListRepositoriesResultTypeDef,
    ListSubPackageGroupsRequestPaginateTypeDef,
    ListSubPackageGroupsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "ListAllowedRepositoriesForGroupPaginator",
    "ListAssociatedPackagesPaginator",
    "ListDomainsPaginator",
    "ListPackageGroupsPaginator",
    "ListPackageVersionAssetsPaginator",
    "ListPackageVersionsPaginator",
    "ListPackagesPaginator",
    "ListRepositoriesInDomainPaginator",
    "ListRepositoriesPaginator",
    "ListSubPackageGroupsPaginator",
)

if TYPE_CHECKING:
    _ListAllowedRepositoriesForGroupPaginatorBase = Paginator[
        ListAllowedRepositoriesForGroupResultTypeDef
    ]
else:
    _ListAllowedRepositoriesForGroupPaginatorBase = Paginator  # type: ignore[assignment]

class ListAllowedRepositoriesForGroupPaginator(_ListAllowedRepositoriesForGroupPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListAllowedRepositoriesForGroup.html#CodeArtifact.Paginator.ListAllowedRepositoriesForGroup)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listallowedrepositoriesforgrouppaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAllowedRepositoriesForGroupRequestPaginateTypeDef]
    ) -> PageIterator[ListAllowedRepositoriesForGroupResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListAllowedRepositoriesForGroup.html#CodeArtifact.Paginator.ListAllowedRepositoriesForGroup.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listallowedrepositoriesforgrouppaginator)
        """

if TYPE_CHECKING:
    _ListAssociatedPackagesPaginatorBase = Paginator[ListAssociatedPackagesResultTypeDef]
else:
    _ListAssociatedPackagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListAssociatedPackagesPaginator(_ListAssociatedPackagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListAssociatedPackages.html#CodeArtifact.Paginator.ListAssociatedPackages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listassociatedpackagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListAssociatedPackagesRequestPaginateTypeDef]
    ) -> PageIterator[ListAssociatedPackagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListAssociatedPackages.html#CodeArtifact.Paginator.ListAssociatedPackages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listassociatedpackagespaginator)
        """

if TYPE_CHECKING:
    _ListDomainsPaginatorBase = Paginator[ListDomainsResultTypeDef]
else:
    _ListDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class ListDomainsPaginator(_ListDomainsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListDomains.html#CodeArtifact.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListDomainsRequestPaginateTypeDef]
    ) -> PageIterator[ListDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListDomains.html#CodeArtifact.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listdomainspaginator)
        """

if TYPE_CHECKING:
    _ListPackageGroupsPaginatorBase = Paginator[ListPackageGroupsResultTypeDef]
else:
    _ListPackageGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPackageGroupsPaginator(_ListPackageGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListPackageGroups.html#CodeArtifact.Paginator.ListPackageGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listpackagegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPackageGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListPackageGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListPackageGroups.html#CodeArtifact.Paginator.ListPackageGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listpackagegroupspaginator)
        """

if TYPE_CHECKING:
    _ListPackageVersionAssetsPaginatorBase = Paginator[ListPackageVersionAssetsResultTypeDef]
else:
    _ListPackageVersionAssetsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPackageVersionAssetsPaginator(_ListPackageVersionAssetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListPackageVersionAssets.html#CodeArtifact.Paginator.ListPackageVersionAssets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listpackageversionassetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPackageVersionAssetsRequestPaginateTypeDef]
    ) -> PageIterator[ListPackageVersionAssetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListPackageVersionAssets.html#CodeArtifact.Paginator.ListPackageVersionAssets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listpackageversionassetspaginator)
        """

if TYPE_CHECKING:
    _ListPackageVersionsPaginatorBase = Paginator[ListPackageVersionsResultTypeDef]
else:
    _ListPackageVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class ListPackageVersionsPaginator(_ListPackageVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListPackageVersions.html#CodeArtifact.Paginator.ListPackageVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listpackageversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPackageVersionsRequestPaginateTypeDef]
    ) -> PageIterator[ListPackageVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListPackageVersions.html#CodeArtifact.Paginator.ListPackageVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listpackageversionspaginator)
        """

if TYPE_CHECKING:
    _ListPackagesPaginatorBase = Paginator[ListPackagesResultTypeDef]
else:
    _ListPackagesPaginatorBase = Paginator  # type: ignore[assignment]

class ListPackagesPaginator(_ListPackagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListPackages.html#CodeArtifact.Paginator.ListPackages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listpackagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListPackagesRequestPaginateTypeDef]
    ) -> PageIterator[ListPackagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListPackages.html#CodeArtifact.Paginator.ListPackages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listpackagespaginator)
        """

if TYPE_CHECKING:
    _ListRepositoriesInDomainPaginatorBase = Paginator[ListRepositoriesInDomainResultTypeDef]
else:
    _ListRepositoriesInDomainPaginatorBase = Paginator  # type: ignore[assignment]

class ListRepositoriesInDomainPaginator(_ListRepositoriesInDomainPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListRepositoriesInDomain.html#CodeArtifact.Paginator.ListRepositoriesInDomain)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listrepositoriesindomainpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRepositoriesInDomainRequestPaginateTypeDef]
    ) -> PageIterator[ListRepositoriesInDomainResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListRepositoriesInDomain.html#CodeArtifact.Paginator.ListRepositoriesInDomain.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listrepositoriesindomainpaginator)
        """

if TYPE_CHECKING:
    _ListRepositoriesPaginatorBase = Paginator[ListRepositoriesResultTypeDef]
else:
    _ListRepositoriesPaginatorBase = Paginator  # type: ignore[assignment]

class ListRepositoriesPaginator(_ListRepositoriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListRepositories.html#CodeArtifact.Paginator.ListRepositories)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listrepositoriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListRepositoriesRequestPaginateTypeDef]
    ) -> PageIterator[ListRepositoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListRepositories.html#CodeArtifact.Paginator.ListRepositories.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listrepositoriespaginator)
        """

if TYPE_CHECKING:
    _ListSubPackageGroupsPaginatorBase = Paginator[ListSubPackageGroupsResultTypeDef]
else:
    _ListSubPackageGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class ListSubPackageGroupsPaginator(_ListSubPackageGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListSubPackageGroups.html#CodeArtifact.Paginator.ListSubPackageGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listsubpackagegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSubPackageGroupsRequestPaginateTypeDef]
    ) -> PageIterator[ListSubPackageGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/paginator/ListSubPackageGroups.html#CodeArtifact.Paginator.ListSubPackageGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators/#listsubpackagegroupspaginator)
        """
