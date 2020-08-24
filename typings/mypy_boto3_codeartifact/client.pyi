# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for codeartifact service client

Usage::

    ```python
    import boto3
    from mypy_boto3_codeartifact import CodeArtifactClient

    client: CodeArtifactClient = boto3.client("codeartifact")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codeartifact.paginator import (
    ListDomainsPaginator,
    ListPackagesPaginator,
    ListPackageVersionAssetsPaginator,
    ListPackageVersionsPaginator,
    ListRepositoriesInDomainPaginator,
    ListRepositoriesPaginator,
)
from mypy_boto3_codeartifact.type_defs import (
    AssociateExternalConnectionResultTypeDef,
    CopyPackageVersionsResultTypeDef,
    CreateDomainResultTypeDef,
    CreateRepositoryResultTypeDef,
    DeleteDomainPermissionsPolicyResultTypeDef,
    DeleteDomainResultTypeDef,
    DeletePackageVersionsResultTypeDef,
    DeleteRepositoryPermissionsPolicyResultTypeDef,
    DeleteRepositoryResultTypeDef,
    DescribeDomainResultTypeDef,
    DescribePackageVersionResultTypeDef,
    DescribeRepositoryResultTypeDef,
    DisassociateExternalConnectionResultTypeDef,
    DisposePackageVersionsResultTypeDef,
    GetAuthorizationTokenResultTypeDef,
    GetDomainPermissionsPolicyResultTypeDef,
    GetPackageVersionAssetResultTypeDef,
    GetPackageVersionReadmeResultTypeDef,
    GetRepositoryEndpointResultTypeDef,
    GetRepositoryPermissionsPolicyResultTypeDef,
    ListDomainsResultTypeDef,
    ListPackagesResultTypeDef,
    ListPackageVersionAssetsResultTypeDef,
    ListPackageVersionDependenciesResultTypeDef,
    ListPackageVersionsResultTypeDef,
    ListRepositoriesInDomainResultTypeDef,
    ListRepositoriesResultTypeDef,
    PutDomainPermissionsPolicyResultTypeDef,
    PutRepositoryPermissionsPolicyResultTypeDef,
    UpdatePackageVersionsStatusResultTypeDef,
    UpdateRepositoryResultTypeDef,
    UpstreamRepositoryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeArtifactClient",)


class Exceptions:
    AccessDeniedException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceQuotaExceededException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class CodeArtifactClient:
    """
    [CodeArtifact.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client)
    """

    exceptions: Exceptions

    def associate_external_connection(
        self, domain: str, repository: str, externalConnection: str, domainOwner: str = None
    ) -> AssociateExternalConnectionResultTypeDef:
        """
        [Client.associate_external_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.associate_external_connection)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.can_paginate)
        """

    def copy_package_versions(
        self,
        domain: str,
        sourceRepository: str,
        destinationRepository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        domainOwner: str = None,
        namespace: str = None,
        versions: List[str] = None,
        versionRevisions: Dict[str, str] = None,
        allowOverwrite: bool = None,
        includeFromUpstream: bool = None,
    ) -> CopyPackageVersionsResultTypeDef:
        """
        [Client.copy_package_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.copy_package_versions)
        """

    def create_domain(self, domain: str, encryptionKey: str = None) -> CreateDomainResultTypeDef:
        """
        [Client.create_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.create_domain)
        """

    def create_repository(
        self,
        domain: str,
        repository: str,
        domainOwner: str = None,
        description: str = None,
        upstreams: List[UpstreamRepositoryTypeDef] = None,
    ) -> CreateRepositoryResultTypeDef:
        """
        [Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.create_repository)
        """

    def delete_domain(self, domain: str, domainOwner: str = None) -> DeleteDomainResultTypeDef:
        """
        [Client.delete_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.delete_domain)
        """

    def delete_domain_permissions_policy(
        self, domain: str, domainOwner: str = None, policyRevision: str = None
    ) -> DeleteDomainPermissionsPolicyResultTypeDef:
        """
        [Client.delete_domain_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.delete_domain_permissions_policy)
        """

    def delete_package_versions(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        versions: List[str],
        domainOwner: str = None,
        namespace: str = None,
        expectedStatus: Literal[
            "Published", "Unfinished", "Unlisted", "Archived", "Disposed", "Deleted"
        ] = None,
    ) -> DeletePackageVersionsResultTypeDef:
        """
        [Client.delete_package_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.delete_package_versions)
        """

    def delete_repository(
        self, domain: str, repository: str, domainOwner: str = None
    ) -> DeleteRepositoryResultTypeDef:
        """
        [Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.delete_repository)
        """

    def delete_repository_permissions_policy(
        self, domain: str, repository: str, domainOwner: str = None, policyRevision: str = None
    ) -> DeleteRepositoryPermissionsPolicyResultTypeDef:
        """
        [Client.delete_repository_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.delete_repository_permissions_policy)
        """

    def describe_domain(self, domain: str, domainOwner: str = None) -> DescribeDomainResultTypeDef:
        """
        [Client.describe_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.describe_domain)
        """

    def describe_package_version(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        packageVersion: str,
        domainOwner: str = None,
        namespace: str = None,
    ) -> DescribePackageVersionResultTypeDef:
        """
        [Client.describe_package_version documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.describe_package_version)
        """

    def describe_repository(
        self, domain: str, repository: str, domainOwner: str = None
    ) -> DescribeRepositoryResultTypeDef:
        """
        [Client.describe_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.describe_repository)
        """

    def disassociate_external_connection(
        self, domain: str, repository: str, externalConnection: str, domainOwner: str = None
    ) -> DisassociateExternalConnectionResultTypeDef:
        """
        [Client.disassociate_external_connection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.disassociate_external_connection)
        """

    def dispose_package_versions(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        versions: List[str],
        domainOwner: str = None,
        namespace: str = None,
        versionRevisions: Dict[str, str] = None,
        expectedStatus: Literal[
            "Published", "Unfinished", "Unlisted", "Archived", "Disposed", "Deleted"
        ] = None,
    ) -> DisposePackageVersionsResultTypeDef:
        """
        [Client.dispose_package_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.dispose_package_versions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.generate_presigned_url)
        """

    def get_authorization_token(
        self, domain: str, domainOwner: str = None, durationSeconds: int = None
    ) -> GetAuthorizationTokenResultTypeDef:
        """
        [Client.get_authorization_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.get_authorization_token)
        """

    def get_domain_permissions_policy(
        self, domain: str, domainOwner: str = None
    ) -> GetDomainPermissionsPolicyResultTypeDef:
        """
        [Client.get_domain_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.get_domain_permissions_policy)
        """

    def get_package_version_asset(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        packageVersion: str,
        asset: str,
        domainOwner: str = None,
        namespace: str = None,
        packageVersionRevision: str = None,
    ) -> GetPackageVersionAssetResultTypeDef:
        """
        [Client.get_package_version_asset documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.get_package_version_asset)
        """

    def get_package_version_readme(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        packageVersion: str,
        domainOwner: str = None,
        namespace: str = None,
    ) -> GetPackageVersionReadmeResultTypeDef:
        """
        [Client.get_package_version_readme documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.get_package_version_readme)
        """

    def get_repository_endpoint(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        domainOwner: str = None,
    ) -> GetRepositoryEndpointResultTypeDef:
        """
        [Client.get_repository_endpoint documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.get_repository_endpoint)
        """

    def get_repository_permissions_policy(
        self, domain: str, repository: str, domainOwner: str = None
    ) -> GetRepositoryPermissionsPolicyResultTypeDef:
        """
        [Client.get_repository_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.get_repository_permissions_policy)
        """

    def list_domains(
        self, maxResults: int = None, nextToken: str = None
    ) -> ListDomainsResultTypeDef:
        """
        [Client.list_domains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.list_domains)
        """

    def list_package_version_assets(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        packageVersion: str,
        domainOwner: str = None,
        namespace: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListPackageVersionAssetsResultTypeDef:
        """
        [Client.list_package_version_assets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.list_package_version_assets)
        """

    def list_package_version_dependencies(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        packageVersion: str,
        domainOwner: str = None,
        namespace: str = None,
        nextToken: str = None,
    ) -> ListPackageVersionDependenciesResultTypeDef:
        """
        [Client.list_package_version_dependencies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.list_package_version_dependencies)
        """

    def list_package_versions(
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
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListPackageVersionsResultTypeDef:
        """
        [Client.list_package_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.list_package_versions)
        """

    def list_packages(
        self,
        domain: str,
        repository: str,
        domainOwner: str = None,
        format: Literal["npm", "pypi", "maven"] = None,
        namespace: str = None,
        packagePrefix: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListPackagesResultTypeDef:
        """
        [Client.list_packages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.list_packages)
        """

    def list_repositories(
        self, repositoryPrefix: str = None, maxResults: int = None, nextToken: str = None
    ) -> ListRepositoriesResultTypeDef:
        """
        [Client.list_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.list_repositories)
        """

    def list_repositories_in_domain(
        self,
        domain: str,
        domainOwner: str = None,
        administratorAccount: str = None,
        repositoryPrefix: str = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListRepositoriesInDomainResultTypeDef:
        """
        [Client.list_repositories_in_domain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.list_repositories_in_domain)
        """

    def put_domain_permissions_policy(
        self, domain: str, policyDocument: str, domainOwner: str = None, policyRevision: str = None
    ) -> PutDomainPermissionsPolicyResultTypeDef:
        """
        [Client.put_domain_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.put_domain_permissions_policy)
        """

    def put_repository_permissions_policy(
        self,
        domain: str,
        repository: str,
        policyDocument: str,
        domainOwner: str = None,
        policyRevision: str = None,
    ) -> PutRepositoryPermissionsPolicyResultTypeDef:
        """
        [Client.put_repository_permissions_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.put_repository_permissions_policy)
        """

    def update_package_versions_status(
        self,
        domain: str,
        repository: str,
        format: Literal["npm", "pypi", "maven"],
        package: str,
        versions: List[str],
        targetStatus: Literal[
            "Published", "Unfinished", "Unlisted", "Archived", "Disposed", "Deleted"
        ],
        domainOwner: str = None,
        namespace: str = None,
        versionRevisions: Dict[str, str] = None,
        expectedStatus: Literal[
            "Published", "Unfinished", "Unlisted", "Archived", "Disposed", "Deleted"
        ] = None,
    ) -> UpdatePackageVersionsStatusResultTypeDef:
        """
        [Client.update_package_versions_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.update_package_versions_status)
        """

    def update_repository(
        self,
        domain: str,
        repository: str,
        domainOwner: str = None,
        description: str = None,
        upstreams: List[UpstreamRepositoryTypeDef] = None,
    ) -> UpdateRepositoryResultTypeDef:
        """
        [Client.update_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Client.update_repository)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Paginator.ListDomains)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_package_version_assets"]
    ) -> ListPackageVersionAssetsPaginator:
        """
        [Paginator.ListPackageVersionAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersionAssets)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_package_versions"]
    ) -> ListPackageVersionsPaginator:
        """
        [Paginator.ListPackageVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackageVersions)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_packages"]) -> ListPackagesPaginator:
        """
        [Paginator.ListPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Paginator.ListPackages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_repositories"]
    ) -> ListRepositoriesPaginator:
        """
        [Paginator.ListRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_repositories_in_domain"]
    ) -> ListRepositoriesInDomainPaginator:
        """
        [Paginator.ListRepositoriesInDomain documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/codeartifact.html#CodeArtifact.Paginator.ListRepositoriesInDomain)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass
