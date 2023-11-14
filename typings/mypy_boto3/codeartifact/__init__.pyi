"""
Main interface for codeartifact service.

Usage::

    ```python
    import boto3
    from mypy_boto3_codeartifact import (
        Client,
        CodeArtifactClient,
        ListDomainsPaginator,
        ListPackageVersionAssetsPaginator,
        ListPackageVersionsPaginator,
        ListPackagesPaginator,
        ListRepositoriesInDomainPaginator,
        ListRepositoriesPaginator,
    )

    session = boto3.Session()

    client: CodeArtifactClient = boto3.client("codeartifact")
    session_client: CodeArtifactClient = session.client("codeartifact")

    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_package_version_assets_paginator: ListPackageVersionAssetsPaginator = client.get_paginator("list_package_version_assets")
    list_package_versions_paginator: ListPackageVersionsPaginator = client.get_paginator("list_package_versions")
    list_packages_paginator: ListPackagesPaginator = client.get_paginator("list_packages")
    list_repositories_paginator: ListRepositoriesPaginator = client.get_paginator("list_repositories")
    list_repositories_in_domain_paginator: ListRepositoriesInDomainPaginator = client.get_paginator("list_repositories_in_domain")
    ```
"""
from .client import CodeArtifactClient
from .paginator import (
    ListDomainsPaginator,
    ListPackagesPaginator,
    ListPackageVersionAssetsPaginator,
    ListPackageVersionsPaginator,
    ListRepositoriesInDomainPaginator,
    ListRepositoriesPaginator,
)

Client = CodeArtifactClient

__all__ = (
    "Client",
    "CodeArtifactClient",
    "ListDomainsPaginator",
    "ListPackageVersionAssetsPaginator",
    "ListPackageVersionsPaginator",
    "ListPackagesPaginator",
    "ListRepositoriesInDomainPaginator",
    "ListRepositoriesPaginator",
)
