"""
Type annotations for codeartifact service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_codeartifact.client import CodeArtifactClient

    session = Session()
    client: CodeArtifactClient = session.client("codeartifact")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

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
from .type_defs import (
    AssociateExternalConnectionRequestTypeDef,
    AssociateExternalConnectionResultTypeDef,
    CopyPackageVersionsRequestTypeDef,
    CopyPackageVersionsResultTypeDef,
    CreateDomainRequestTypeDef,
    CreateDomainResultTypeDef,
    CreatePackageGroupRequestTypeDef,
    CreatePackageGroupResultTypeDef,
    CreateRepositoryRequestTypeDef,
    CreateRepositoryResultTypeDef,
    DeleteDomainPermissionsPolicyRequestTypeDef,
    DeleteDomainPermissionsPolicyResultTypeDef,
    DeleteDomainRequestTypeDef,
    DeleteDomainResultTypeDef,
    DeletePackageGroupRequestTypeDef,
    DeletePackageGroupResultTypeDef,
    DeletePackageRequestTypeDef,
    DeletePackageResultTypeDef,
    DeletePackageVersionsRequestTypeDef,
    DeletePackageVersionsResultTypeDef,
    DeleteRepositoryPermissionsPolicyRequestTypeDef,
    DeleteRepositoryPermissionsPolicyResultTypeDef,
    DeleteRepositoryRequestTypeDef,
    DeleteRepositoryResultTypeDef,
    DescribeDomainRequestTypeDef,
    DescribeDomainResultTypeDef,
    DescribePackageGroupRequestTypeDef,
    DescribePackageGroupResultTypeDef,
    DescribePackageRequestTypeDef,
    DescribePackageResultTypeDef,
    DescribePackageVersionRequestTypeDef,
    DescribePackageVersionResultTypeDef,
    DescribeRepositoryRequestTypeDef,
    DescribeRepositoryResultTypeDef,
    DisassociateExternalConnectionRequestTypeDef,
    DisassociateExternalConnectionResultTypeDef,
    DisposePackageVersionsRequestTypeDef,
    DisposePackageVersionsResultTypeDef,
    GetAssociatedPackageGroupRequestTypeDef,
    GetAssociatedPackageGroupResultTypeDef,
    GetAuthorizationTokenRequestTypeDef,
    GetAuthorizationTokenResultTypeDef,
    GetDomainPermissionsPolicyRequestTypeDef,
    GetDomainPermissionsPolicyResultTypeDef,
    GetPackageVersionAssetRequestTypeDef,
    GetPackageVersionAssetResultTypeDef,
    GetPackageVersionReadmeRequestTypeDef,
    GetPackageVersionReadmeResultTypeDef,
    GetRepositoryEndpointRequestTypeDef,
    GetRepositoryEndpointResultTypeDef,
    GetRepositoryPermissionsPolicyRequestTypeDef,
    GetRepositoryPermissionsPolicyResultTypeDef,
    ListAllowedRepositoriesForGroupRequestTypeDef,
    ListAllowedRepositoriesForGroupResultTypeDef,
    ListAssociatedPackagesRequestTypeDef,
    ListAssociatedPackagesResultTypeDef,
    ListDomainsRequestTypeDef,
    ListDomainsResultTypeDef,
    ListPackageGroupsRequestTypeDef,
    ListPackageGroupsResultTypeDef,
    ListPackagesRequestTypeDef,
    ListPackagesResultTypeDef,
    ListPackageVersionAssetsRequestTypeDef,
    ListPackageVersionAssetsResultTypeDef,
    ListPackageVersionDependenciesRequestTypeDef,
    ListPackageVersionDependenciesResultTypeDef,
    ListPackageVersionsRequestTypeDef,
    ListPackageVersionsResultTypeDef,
    ListRepositoriesInDomainRequestTypeDef,
    ListRepositoriesInDomainResultTypeDef,
    ListRepositoriesRequestTypeDef,
    ListRepositoriesResultTypeDef,
    ListSubPackageGroupsRequestTypeDef,
    ListSubPackageGroupsResultTypeDef,
    ListTagsForResourceRequestTypeDef,
    ListTagsForResourceResultTypeDef,
    PublishPackageVersionRequestTypeDef,
    PublishPackageVersionResultTypeDef,
    PutDomainPermissionsPolicyRequestTypeDef,
    PutDomainPermissionsPolicyResultTypeDef,
    PutPackageOriginConfigurationRequestTypeDef,
    PutPackageOriginConfigurationResultTypeDef,
    PutRepositoryPermissionsPolicyRequestTypeDef,
    PutRepositoryPermissionsPolicyResultTypeDef,
    TagResourceRequestTypeDef,
    UntagResourceRequestTypeDef,
    UpdatePackageGroupOriginConfigurationRequestTypeDef,
    UpdatePackageGroupOriginConfigurationResultTypeDef,
    UpdatePackageGroupRequestTypeDef,
    UpdatePackageGroupResultTypeDef,
    UpdatePackageVersionsStatusRequestTypeDef,
    UpdatePackageVersionsStatusResultTypeDef,
    UpdateRepositoryRequestTypeDef,
    UpdateRepositoryResultTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("CodeArtifactClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class CodeArtifactClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        CodeArtifactClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact.html#CodeArtifact.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#generate_presigned_url)
        """

    def associate_external_connection(
        self, **kwargs: Unpack[AssociateExternalConnectionRequestTypeDef]
    ) -> AssociateExternalConnectionResultTypeDef:
        """
        Adds an existing external connection to a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/associate_external_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#associate_external_connection)
        """

    def copy_package_versions(
        self, **kwargs: Unpack[CopyPackageVersionsRequestTypeDef]
    ) -> CopyPackageVersionsResultTypeDef:
        """
        Copies package versions from one repository to another repository in the same
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/copy_package_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#copy_package_versions)
        """

    def create_domain(
        self, **kwargs: Unpack[CreateDomainRequestTypeDef]
    ) -> CreateDomainResultTypeDef:
        """
        Creates a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/create_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#create_domain)
        """

    def create_package_group(
        self, **kwargs: Unpack[CreatePackageGroupRequestTypeDef]
    ) -> CreatePackageGroupResultTypeDef:
        """
        Creates a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/create_package_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#create_package_group)
        """

    def create_repository(
        self, **kwargs: Unpack[CreateRepositoryRequestTypeDef]
    ) -> CreateRepositoryResultTypeDef:
        """
        Creates a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/create_repository.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#create_repository)
        """

    def delete_domain(
        self, **kwargs: Unpack[DeleteDomainRequestTypeDef]
    ) -> DeleteDomainResultTypeDef:
        """
        Deletes a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#delete_domain)
        """

    def delete_domain_permissions_policy(
        self, **kwargs: Unpack[DeleteDomainPermissionsPolicyRequestTypeDef]
    ) -> DeleteDomainPermissionsPolicyResultTypeDef:
        """
        Deletes the resource policy set on a domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_domain_permissions_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#delete_domain_permissions_policy)
        """

    def delete_package(
        self, **kwargs: Unpack[DeletePackageRequestTypeDef]
    ) -> DeletePackageResultTypeDef:
        """
        Deletes a package and all associated package versions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#delete_package)
        """

    def delete_package_group(
        self, **kwargs: Unpack[DeletePackageGroupRequestTypeDef]
    ) -> DeletePackageGroupResultTypeDef:
        """
        Deletes a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_package_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#delete_package_group)
        """

    def delete_package_versions(
        self, **kwargs: Unpack[DeletePackageVersionsRequestTypeDef]
    ) -> DeletePackageVersionsResultTypeDef:
        """
        Deletes one or more versions of a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_package_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#delete_package_versions)
        """

    def delete_repository(
        self, **kwargs: Unpack[DeleteRepositoryRequestTypeDef]
    ) -> DeleteRepositoryResultTypeDef:
        """
        Deletes a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_repository.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#delete_repository)
        """

    def delete_repository_permissions_policy(
        self, **kwargs: Unpack[DeleteRepositoryPermissionsPolicyRequestTypeDef]
    ) -> DeleteRepositoryPermissionsPolicyResultTypeDef:
        """
        Deletes the resource policy that is set on a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/delete_repository_permissions_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#delete_repository_permissions_policy)
        """

    def describe_domain(
        self, **kwargs: Unpack[DescribeDomainRequestTypeDef]
    ) -> DescribeDomainResultTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainDescription.html">DomainDescription</a>
        object that contains information about the requested domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#describe_domain)
        """

    def describe_package(
        self, **kwargs: Unpack[DescribePackageRequestTypeDef]
    ) -> DescribePackageResultTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDescription.html">PackageDescription</a>
        object that contains information about the requested package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_package.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#describe_package)
        """

    def describe_package_group(
        self, **kwargs: Unpack[DescribePackageGroupRequestTypeDef]
    ) -> DescribePackageGroupResultTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageGroupDescription.html">PackageGroupDescription</a>
        object that contains information about the requested package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_package_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#describe_package_group)
        """

    def describe_package_version(
        self, **kwargs: Unpack[DescribePackageVersionRequestTypeDef]
    ) -> DescribePackageVersionResultTypeDef:
        """
        Returns a <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html">PackageVersionDescription</a>
        object that contains information about the requested package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_package_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#describe_package_version)
        """

    def describe_repository(
        self, **kwargs: Unpack[DescribeRepositoryRequestTypeDef]
    ) -> DescribeRepositoryResultTypeDef:
        """
        Returns a <code>RepositoryDescription</code> object that contains detailed
        information about the requested repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/describe_repository.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#describe_repository)
        """

    def disassociate_external_connection(
        self, **kwargs: Unpack[DisassociateExternalConnectionRequestTypeDef]
    ) -> DisassociateExternalConnectionResultTypeDef:
        """
        Removes an existing external connection from a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/disassociate_external_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#disassociate_external_connection)
        """

    def dispose_package_versions(
        self, **kwargs: Unpack[DisposePackageVersionsRequestTypeDef]
    ) -> DisposePackageVersionsResultTypeDef:
        """
        Deletes the assets in package versions and sets the package versions' status to
        <code>Disposed</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/dispose_package_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#dispose_package_versions)
        """

    def get_associated_package_group(
        self, **kwargs: Unpack[GetAssociatedPackageGroupRequestTypeDef]
    ) -> GetAssociatedPackageGroupResultTypeDef:
        """
        Returns the most closely associated package group to the specified package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_associated_package_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_associated_package_group)
        """

    def get_authorization_token(
        self, **kwargs: Unpack[GetAuthorizationTokenRequestTypeDef]
    ) -> GetAuthorizationTokenResultTypeDef:
        """
        Generates a temporary authorization token for accessing repositories in the
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_authorization_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_authorization_token)
        """

    def get_domain_permissions_policy(
        self, **kwargs: Unpack[GetDomainPermissionsPolicyRequestTypeDef]
    ) -> GetDomainPermissionsPolicyResultTypeDef:
        """
        Returns the resource policy attached to the specified domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_domain_permissions_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_domain_permissions_policy)
        """

    def get_package_version_asset(
        self, **kwargs: Unpack[GetPackageVersionAssetRequestTypeDef]
    ) -> GetPackageVersionAssetResultTypeDef:
        """
        Returns an asset (or file) that is in a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_package_version_asset.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_package_version_asset)
        """

    def get_package_version_readme(
        self, **kwargs: Unpack[GetPackageVersionReadmeRequestTypeDef]
    ) -> GetPackageVersionReadmeResultTypeDef:
        """
        Gets the readme file or descriptive text for a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_package_version_readme.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_package_version_readme)
        """

    def get_repository_endpoint(
        self, **kwargs: Unpack[GetRepositoryEndpointRequestTypeDef]
    ) -> GetRepositoryEndpointResultTypeDef:
        """
        Returns the endpoint of a repository for a specific package format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_repository_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_repository_endpoint)
        """

    def get_repository_permissions_policy(
        self, **kwargs: Unpack[GetRepositoryPermissionsPolicyRequestTypeDef]
    ) -> GetRepositoryPermissionsPolicyResultTypeDef:
        """
        Returns the resource policy that is set on a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_repository_permissions_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_repository_permissions_policy)
        """

    def list_allowed_repositories_for_group(
        self, **kwargs: Unpack[ListAllowedRepositoriesForGroupRequestTypeDef]
    ) -> ListAllowedRepositoriesForGroupResultTypeDef:
        """
        Lists the repositories in the added repositories list of the specified
        restriction type for a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_allowed_repositories_for_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_allowed_repositories_for_group)
        """

    def list_associated_packages(
        self, **kwargs: Unpack[ListAssociatedPackagesRequestTypeDef]
    ) -> ListAssociatedPackagesResultTypeDef:
        """
        Returns a list of packages associated with the requested package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_associated_packages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_associated_packages)
        """

    def list_domains(self, **kwargs: Unpack[ListDomainsRequestTypeDef]) -> ListDomainsResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html">DomainSummary</a>
        objects for all domains owned by the Amazon Web Services account that makes
        this call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_domains)
        """

    def list_package_groups(
        self, **kwargs: Unpack[ListPackageGroupsRequestTypeDef]
    ) -> ListPackageGroupsResultTypeDef:
        """
        Returns a list of package groups in the requested domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_package_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_package_groups)
        """

    def list_package_version_assets(
        self, **kwargs: Unpack[ListPackageVersionAssetsRequestTypeDef]
    ) -> ListPackageVersionAssetsResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html">AssetSummary</a>
        objects for assets in a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_package_version_assets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_package_version_assets)
        """

    def list_package_version_dependencies(
        self, **kwargs: Unpack[ListPackageVersionDependenciesRequestTypeDef]
    ) -> ListPackageVersionDependenciesResultTypeDef:
        """
        Returns the direct dependencies for a package version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_package_version_dependencies.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_package_version_dependencies)
        """

    def list_package_versions(
        self, **kwargs: Unpack[ListPackageVersionsRequestTypeDef]
    ) -> ListPackageVersionsResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionSummary.html">PackageVersionSummary</a>
        objects for package versions in a repository that match the request parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_package_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_package_versions)
        """

    def list_packages(
        self, **kwargs: Unpack[ListPackagesRequestTypeDef]
    ) -> ListPackagesResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html">PackageSummary</a>
        objects for packages in a repository that match the request parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_packages.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_packages)
        """

    def list_repositories(
        self, **kwargs: Unpack[ListRepositoriesRequestTypeDef]
    ) -> ListRepositoriesResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html">RepositorySummary</a>
        objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_repositories.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_repositories)
        """

    def list_repositories_in_domain(
        self, **kwargs: Unpack[ListRepositoriesInDomainRequestTypeDef]
    ) -> ListRepositoriesInDomainResultTypeDef:
        """
        Returns a list of <a
        href="https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_RepositorySummary.html">RepositorySummary</a>
        objects.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_repositories_in_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_repositories_in_domain)
        """

    def list_sub_package_groups(
        self, **kwargs: Unpack[ListSubPackageGroupsRequestTypeDef]
    ) -> ListSubPackageGroupsResultTypeDef:
        """
        Returns a list of direct children of the specified package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_sub_package_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_sub_package_groups)
        """

    def list_tags_for_resource(
        self, **kwargs: Unpack[ListTagsForResourceRequestTypeDef]
    ) -> ListTagsForResourceResultTypeDef:
        """
        Gets information about Amazon Web Services tags for a specified Amazon Resource
        Name (ARN) in CodeArtifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/list_tags_for_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#list_tags_for_resource)
        """

    def publish_package_version(
        self, **kwargs: Unpack[PublishPackageVersionRequestTypeDef]
    ) -> PublishPackageVersionResultTypeDef:
        """
        Creates a new package version containing one or more assets (or files).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/publish_package_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#publish_package_version)
        """

    def put_domain_permissions_policy(
        self, **kwargs: Unpack[PutDomainPermissionsPolicyRequestTypeDef]
    ) -> PutDomainPermissionsPolicyResultTypeDef:
        """
        Sets a resource policy on a domain that specifies permissions to access it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/put_domain_permissions_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#put_domain_permissions_policy)
        """

    def put_package_origin_configuration(
        self, **kwargs: Unpack[PutPackageOriginConfigurationRequestTypeDef]
    ) -> PutPackageOriginConfigurationResultTypeDef:
        """
        Sets the package origin configuration for a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/put_package_origin_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#put_package_origin_configuration)
        """

    def put_repository_permissions_policy(
        self, **kwargs: Unpack[PutRepositoryPermissionsPolicyRequestTypeDef]
    ) -> PutRepositoryPermissionsPolicyResultTypeDef:
        """
        Sets the resource policy on a repository that specifies permissions to access
        it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/put_repository_permissions_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#put_repository_permissions_policy)
        """

    def tag_resource(self, **kwargs: Unpack[TagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Adds or updates tags for a resource in CodeArtifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/tag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#tag_resource)
        """

    def untag_resource(self, **kwargs: Unpack[UntagResourceRequestTypeDef]) -> Dict[str, Any]:
        """
        Removes tags from a resource in CodeArtifact.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/untag_resource.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#untag_resource)
        """

    def update_package_group(
        self, **kwargs: Unpack[UpdatePackageGroupRequestTypeDef]
    ) -> UpdatePackageGroupResultTypeDef:
        """
        Updates a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/update_package_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#update_package_group)
        """

    def update_package_group_origin_configuration(
        self, **kwargs: Unpack[UpdatePackageGroupOriginConfigurationRequestTypeDef]
    ) -> UpdatePackageGroupOriginConfigurationResultTypeDef:
        """
        Updates the package origin configuration for a package group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/update_package_group_origin_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#update_package_group_origin_configuration)
        """

    def update_package_versions_status(
        self, **kwargs: Unpack[UpdatePackageVersionsStatusRequestTypeDef]
    ) -> UpdatePackageVersionsStatusResultTypeDef:
        """
        Updates the status of one or more versions of a package.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/update_package_versions_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#update_package_versions_status)
        """

    def update_repository(
        self, **kwargs: Unpack[UpdateRepositoryRequestTypeDef]
    ) -> UpdateRepositoryResultTypeDef:
        """
        Update the properties of a repository.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/update_repository.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#update_repository)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_allowed_repositories_for_group"]
    ) -> ListAllowedRepositoriesForGroupPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_associated_packages"]
    ) -> ListAssociatedPackagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_domains"]
    ) -> ListDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_package_groups"]
    ) -> ListPackageGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_package_version_assets"]
    ) -> ListPackageVersionAssetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_package_versions"]
    ) -> ListPackageVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_packages"]
    ) -> ListPackagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_repositories_in_domain"]
    ) -> ListRepositoriesInDomainPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_repositories"]
    ) -> ListRepositoriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_sub_package_groups"]
    ) -> ListSubPackageGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codeartifact/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/client/#get_paginator)
        """
