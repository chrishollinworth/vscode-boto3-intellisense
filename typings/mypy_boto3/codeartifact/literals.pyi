"""
Type annotations for codeartifact service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/literals.html)

Usage::

    ```python
    from mypy_boto3_codeartifact.literals import AllowPublishType

    data: AllowPublishType = "ALLOW"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AllowPublishType",
    "AllowUpstreamType",
    "DomainStatusType",
    "ExternalConnectionStatusType",
    "HashAlgorithmType",
    "ListAllowedRepositoriesForGroupPaginatorName",
    "ListAssociatedPackagesPaginatorName",
    "ListDomainsPaginatorName",
    "ListPackageGroupsPaginatorName",
    "ListPackageVersionAssetsPaginatorName",
    "ListPackageVersionsPaginatorName",
    "ListPackagesPaginatorName",
    "ListRepositoriesInDomainPaginatorName",
    "ListRepositoriesPaginatorName",
    "ListSubPackageGroupsPaginatorName",
    "PackageFormatType",
    "PackageGroupAllowedRepositoryUpdateTypeType",
    "PackageGroupAssociationTypeType",
    "PackageGroupOriginRestrictionModeType",
    "PackageGroupOriginRestrictionTypeType",
    "PackageVersionErrorCodeType",
    "PackageVersionOriginTypeType",
    "PackageVersionSortTypeType",
    "PackageVersionStatusType",
)

AllowPublishType = Literal["ALLOW", "BLOCK"]
AllowUpstreamType = Literal["ALLOW", "BLOCK"]
DomainStatusType = Literal["Active", "Deleted"]
ExternalConnectionStatusType = Literal["Available"]
HashAlgorithmType = Literal["MD5", "SHA-1", "SHA-256", "SHA-512"]
ListAllowedRepositoriesForGroupPaginatorName = Literal["list_allowed_repositories_for_group"]
ListAssociatedPackagesPaginatorName = Literal["list_associated_packages"]
ListDomainsPaginatorName = Literal["list_domains"]
ListPackageGroupsPaginatorName = Literal["list_package_groups"]
ListPackageVersionAssetsPaginatorName = Literal["list_package_version_assets"]
ListPackageVersionsPaginatorName = Literal["list_package_versions"]
ListPackagesPaginatorName = Literal["list_packages"]
ListRepositoriesInDomainPaginatorName = Literal["list_repositories_in_domain"]
ListRepositoriesPaginatorName = Literal["list_repositories"]
ListSubPackageGroupsPaginatorName = Literal["list_sub_package_groups"]
PackageFormatType = Literal["cargo", "generic", "maven", "npm", "nuget", "pypi", "ruby", "swift"]
PackageGroupAllowedRepositoryUpdateTypeType = Literal["ADDED", "REMOVED"]
PackageGroupAssociationTypeType = Literal["STRONG", "WEAK"]
PackageGroupOriginRestrictionModeType = Literal[
    "ALLOW", "ALLOW_SPECIFIC_REPOSITORIES", "BLOCK", "INHERIT"
]
PackageGroupOriginRestrictionTypeType = Literal["EXTERNAL_UPSTREAM", "INTERNAL_UPSTREAM", "PUBLISH"]
PackageVersionErrorCodeType = Literal[
    "ALREADY_EXISTS",
    "MISMATCHED_REVISION",
    "MISMATCHED_STATUS",
    "NOT_ALLOWED",
    "NOT_FOUND",
    "SKIPPED",
]
PackageVersionOriginTypeType = Literal["EXTERNAL", "INTERNAL", "UNKNOWN"]
PackageVersionSortTypeType = Literal["PUBLISHED_TIME"]
PackageVersionStatusType = Literal[
    "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
]
