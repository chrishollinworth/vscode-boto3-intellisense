"""
Main interface for codeartifact service.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codeartifact import (
        Client,
        CodeArtifactClient,
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

from .client import CodeArtifactClient
from .paginator import (
    ListAllowedRepositoriesForGroupPaginator,
    ListAssociatedPackagesPaginator,
    ListDomainsPaginator,
    ListPackageGroupsPaginator,
    ListPackagesPaginator,
    ListPackageVersionAssetsPaginator,
    ListPackageVersionsPaginator,
    ListRepositoriesInDomainPaginator,
    ListRepositoriesPaginator,
    ListSubPackageGroupsPaginator,
)

Client = CodeArtifactClient

__all__ = (
    "Client",
    "CodeArtifactClient",
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
