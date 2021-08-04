"""
Type annotations for codeartifact service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/literals.html)

Usage::

    ```python
    from mypy_boto3_codeartifact.literals import DomainStatusType

    data: DomainStatusType = "Active"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DomainStatusType",
    "ExternalConnectionStatusType",
    "HashAlgorithmType",
    "ListDomainsPaginatorName",
    "ListPackageVersionAssetsPaginatorName",
    "ListPackageVersionsPaginatorName",
    "ListPackagesPaginatorName",
    "ListRepositoriesInDomainPaginatorName",
    "ListRepositoriesPaginatorName",
    "PackageFormatType",
    "PackageVersionErrorCodeType",
    "PackageVersionSortTypeType",
    "PackageVersionStatusType",
)

DomainStatusType = Literal["Active", "Deleted"]
ExternalConnectionStatusType = Literal["Available"]
HashAlgorithmType = Literal["MD5", "SHA-1", "SHA-256", "SHA-512"]
ListDomainsPaginatorName = Literal["list_domains"]
ListPackageVersionAssetsPaginatorName = Literal["list_package_version_assets"]
ListPackageVersionsPaginatorName = Literal["list_package_versions"]
ListPackagesPaginatorName = Literal["list_packages"]
ListRepositoriesInDomainPaginatorName = Literal["list_repositories_in_domain"]
ListRepositoriesPaginatorName = Literal["list_repositories"]
PackageFormatType = Literal["maven", "npm", "nuget", "pypi"]
PackageVersionErrorCodeType = Literal[
    "ALREADY_EXISTS",
    "MISMATCHED_REVISION",
    "MISMATCHED_STATUS",
    "NOT_ALLOWED",
    "NOT_FOUND",
    "SKIPPED",
]
PackageVersionSortTypeType = Literal["PUBLISHED_TIME"]
PackageVersionStatusType = Literal[
    "Archived", "Deleted", "Disposed", "Published", "Unfinished", "Unlisted"
]
