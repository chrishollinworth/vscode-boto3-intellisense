"""
Type annotations for codeartifact service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_codeartifact import CodeArtifactClient
    from mypy_boto3_codeartifact.paginator import (
        ListAllowedRepositoriesForGroupPaginator,
        ListAssociatedPackagesPaginator,
        ListDomainsPaginator,
        ListPackageGroupsPaginator,
        ListPackageVersionAssetsPaginator,
        ListPackageVersionsPaginator,
        ListPackagesPaginator,
        ListRepositoriesPaginator,
        ListRepositoriesInDomainPaginator,
        ListSubPackageGroupsPaginator,
    )

    client: CodeArtifactClient = boto3.client("codeartifact")

    list_allowed_repositories_for_group_paginator: ListAllowedRepositoriesForGroupPaginator = client.get_paginator("list_allowed_repositories_for_group")
    list_associated_packages_paginator: ListAssociatedPackagesPaginator = client.get_paginator("list_associated_packages")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_package_groups_paginator: ListPackageGroupsPaginator = client.get_paginator("list_package_groups")
    list_package_version_assets_paginator: ListPackageVersionAssetsPaginator = client.get_paginator("list_package_version_assets")
    list_package_versions_paginator: ListPackageVersionsPaginator = client.get_paginator("list_package_versions")
    list_packages_paginator: ListPackagesPaginator = client.get_paginator("list_packages")
    list_repositories_paginator: ListRepositoriesPaginator = client.get_paginator("list_repositories")
    list_repositories_in_domain_paginator: ListRepositoriesInDomainPaginator = client.get_paginator("list_repositories_in_domain")
    list_sub_package_groups_paginator: ListSubPackageGroupsPaginator = client.get_paginator("list_sub_package_groups")
    ```
"""

import sys
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    AllowPublishType,
    AllowUpstreamType,
    PackageFormatType,
    PackageGroupOriginRestrictionTypeType,
    PackageVersionOriginTypeType,
    PackageVersionStatusType,
)
from .type_defs import (
    ListAllowedRepositoriesForGroupResultTypeDef,
    ListAssociatedPackagesResultTypeDef,
    ListDomainsResultTypeDef,
    ListPackageGroupsResultTypeDef,
    ListPackagesResultTypeDef,
    ListPackageVersionAssetsResultTypeDef,
    ListPackageVersionsResultTypeDef,
    ListRepositoriesInDomainResultTypeDef,
    ListRepositoriesResultTypeDef,
    ListSubPackageGroupsResultTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListAllowedRepositoriesForGroupPaginator",
    "ListAssociatedPackagesPaginator",
    "ListDomainsPaginator",
    "ListPackageGroupsPaginator",
    "ListPackageVersionAssetsPaginator",
    "ListPackageVersionsPaginator",
    "ListPackagesPaginator",
    "ListRepositoriesPaginator",
    "ListRepositoriesInDomainPaginator",
    "ListSubPackageGroupsPaginator",
)

class ListAllowedRepositoriesForGroupPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListAllowedRepositoriesForGroup)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listallowedrepositoriesforgrouppaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        packageGroup: str,
        originRestrictionType: PackageGroupOriginRestrictionTypeType,
        domainOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAllowedRepositoriesForGroupResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListAllowedRepositoriesForGroup.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listallowedrepositoriesforgrouppaginator)
        """

class ListAssociatedPackagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListAssociatedPackages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listassociatedpackagespaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str = None,
        preview: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListAssociatedPackagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListAssociatedPackages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listassociatedpackagespaginator)
        """

class ListDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listdomainspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listdomainspaginator)
        """

class ListPackageGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackagegroupspaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        domainOwner: str = None,
        prefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackageGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackagegroupspaginator)
        """

class ListPackageVersionAssetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersionAssets)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersionAssets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackageversionassetspaginator)
        """

class ListPackageVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersions)
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
        originType: PackageVersionOriginTypeType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackageVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackageversionspaginator)
        """

class ListPackagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackages)
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
        publish: AllowPublishType = None,
        upstream: AllowUpstreamType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPackagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listpackagespaginator)
        """

class ListRepositoriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositories)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listrepositoriespaginator)
    """

    def paginate(
        self, *, repositoryPrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListRepositoriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositories.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listrepositoriespaginator)
        """

class ListRepositoriesInDomainPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositoriesInDomain)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositoriesInDomain.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listrepositoriesindomainpaginator)
        """

class ListSubPackageGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListSubPackageGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listsubpackagegroupspaginator)
    """

    def paginate(
        self,
        *,
        domain: str,
        packageGroup: str,
        domainOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubPackageGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/codeartifact.html#CodeArtifact.Paginator.ListSubPackageGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/paginators.html#listsubpackagegroupspaginator)
        """
