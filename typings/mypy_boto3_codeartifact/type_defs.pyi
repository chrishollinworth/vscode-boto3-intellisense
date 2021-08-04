"""
Type annotations for codeartifact service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeartifact.type_defs import AssetSummaryTypeDef

    data: AssetSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from .literals import (
    DomainStatusType,
    HashAlgorithmType,
    PackageFormatType,
    PackageVersionErrorCodeType,
    PackageVersionStatusType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssetSummaryTypeDef",
    "AssociateExternalConnectionRequestRequestTypeDef",
    "AssociateExternalConnectionResultTypeDef",
    "CopyPackageVersionsRequestRequestTypeDef",
    "CopyPackageVersionsResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResultTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "CreateRepositoryResultTypeDef",
    "DeleteDomainPermissionsPolicyRequestRequestTypeDef",
    "DeleteDomainPermissionsPolicyResultTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResultTypeDef",
    "DeletePackageVersionsRequestRequestTypeDef",
    "DeletePackageVersionsResultTypeDef",
    "DeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DeleteRepositoryResultTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResultTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "DescribePackageVersionResultTypeDef",
    "DescribeRepositoryRequestRequestTypeDef",
    "DescribeRepositoryResultTypeDef",
    "DisassociateExternalConnectionRequestRequestTypeDef",
    "DisassociateExternalConnectionResultTypeDef",
    "DisposePackageVersionsRequestRequestTypeDef",
    "DisposePackageVersionsResultTypeDef",
    "DomainDescriptionTypeDef",
    "DomainSummaryTypeDef",
    "GetAuthorizationTokenRequestRequestTypeDef",
    "GetAuthorizationTokenResultTypeDef",
    "GetDomainPermissionsPolicyRequestRequestTypeDef",
    "GetDomainPermissionsPolicyResultTypeDef",
    "GetPackageVersionAssetRequestRequestTypeDef",
    "GetPackageVersionAssetResultTypeDef",
    "GetPackageVersionReadmeRequestRequestTypeDef",
    "GetPackageVersionReadmeResultTypeDef",
    "GetRepositoryEndpointRequestRequestTypeDef",
    "GetRepositoryEndpointResultTypeDef",
    "GetRepositoryPermissionsPolicyRequestRequestTypeDef",
    "GetRepositoryPermissionsPolicyResultTypeDef",
    "LicenseInfoTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResultTypeDef",
    "ListPackageVersionAssetsRequestRequestTypeDef",
    "ListPackageVersionAssetsResultTypeDef",
    "ListPackageVersionDependenciesRequestRequestTypeDef",
    "ListPackageVersionDependenciesResultTypeDef",
    "ListPackageVersionsRequestRequestTypeDef",
    "ListPackageVersionsResultTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "ListPackagesResultTypeDef",
    "ListRepositoriesInDomainRequestRequestTypeDef",
    "ListRepositoriesInDomainResultTypeDef",
    "ListRepositoriesRequestRequestTypeDef",
    "ListRepositoriesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PackageDependencyTypeDef",
    "PackageSummaryTypeDef",
    "PackageVersionDescriptionTypeDef",
    "PackageVersionErrorTypeDef",
    "PackageVersionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PutDomainPermissionsPolicyRequestRequestTypeDef",
    "PutDomainPermissionsPolicyResultTypeDef",
    "PutRepositoryPermissionsPolicyRequestRequestTypeDef",
    "PutRepositoryPermissionsPolicyResultTypeDef",
    "RepositoryDescriptionTypeDef",
    "RepositoryExternalConnectionInfoTypeDef",
    "RepositorySummaryTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "SuccessfulPackageVersionInfoTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePackageVersionsStatusRequestRequestTypeDef",
    "UpdatePackageVersionsStatusResultTypeDef",
    "UpdateRepositoryRequestRequestTypeDef",
    "UpdateRepositoryResultTypeDef",
    "UpstreamRepositoryInfoTypeDef",
    "UpstreamRepositoryTypeDef",
)

_RequiredAssetSummaryTypeDef = TypedDict(
    "_RequiredAssetSummaryTypeDef",
    {
        "name": str,
    },
)
_OptionalAssetSummaryTypeDef = TypedDict(
    "_OptionalAssetSummaryTypeDef",
    {
        "size": int,
        "hashes": Dict[HashAlgorithmType, str],
    },
    total=False,
)

class AssetSummaryTypeDef(_RequiredAssetSummaryTypeDef, _OptionalAssetSummaryTypeDef):
    pass

_RequiredAssociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateExternalConnectionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
    },
)
_OptionalAssociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateExternalConnectionRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class AssociateExternalConnectionRequestRequestTypeDef(
    _RequiredAssociateExternalConnectionRequestRequestTypeDef,
    _OptionalAssociateExternalConnectionRequestRequestTypeDef,
):
    pass

AssociateExternalConnectionResultTypeDef = TypedDict(
    "AssociateExternalConnectionResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyPackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredCopyPackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "sourceRepository": str,
        "destinationRepository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalCopyPackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalCopyPackageVersionsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versions": List[str],
        "versionRevisions": Dict[str, str],
        "allowOverwrite": bool,
        "includeFromUpstream": bool,
    },
    total=False,
)

class CopyPackageVersionsRequestRequestTypeDef(
    _RequiredCopyPackageVersionsRequestRequestTypeDef,
    _OptionalCopyPackageVersionsRequestRequestTypeDef,
):
    pass

CopyPackageVersionsResultTypeDef = TypedDict(
    "CopyPackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDomainRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalCreateDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDomainRequestRequestTypeDef",
    {
        "encryptionKey": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateDomainRequestRequestTypeDef(
    _RequiredCreateDomainRequestRequestTypeDef, _OptionalCreateDomainRequestRequestTypeDef
):
    pass

CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryRequestRequestTypeDef",
    {
        "domainOwner": str,
        "description": str,
        "upstreams": List["UpstreamRepositoryTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRepositoryRequestRequestTypeDef(
    _RequiredCreateRepositoryRequestRequestTypeDef, _OptionalCreateRepositoryRequestRequestTypeDef
):
    pass

CreateRepositoryResultTypeDef = TypedDict(
    "CreateRepositoryResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDeleteDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)

class DeleteDomainPermissionsPolicyRequestRequestTypeDef(
    _RequiredDeleteDomainPermissionsPolicyRequestRequestTypeDef,
    _OptionalDeleteDomainPermissionsPolicyRequestRequestTypeDef,
):
    pass

DeleteDomainPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteDomainPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteDomainRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDomainRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDeleteDomainRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDomainRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DeleteDomainRequestRequestTypeDef(
    _RequiredDeleteDomainRequestRequestTypeDef, _OptionalDeleteDomainRequestRequestTypeDef
):
    pass

DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": List[str],
    },
)
_OptionalDeletePackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageVersionsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)

class DeletePackageVersionsRequestRequestTypeDef(
    _RequiredDeletePackageVersionsRequestRequestTypeDef,
    _OptionalDeletePackageVersionsRequestRequestTypeDef,
):
    pass

DeletePackageVersionsResultTypeDef = TypedDict(
    "DeletePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDeleteRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)

class DeleteRepositoryPermissionsPolicyRequestRequestTypeDef(
    _RequiredDeleteRepositoryPermissionsPolicyRequestRequestTypeDef,
    _OptionalDeleteRepositoryPermissionsPolicyRequestRequestTypeDef,
):
    pass

DeleteRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DeleteRepositoryRequestRequestTypeDef(
    _RequiredDeleteRepositoryRequestRequestTypeDef, _OptionalDeleteRepositoryRequestRequestTypeDef
):
    pass

DeleteRepositoryResultTypeDef = TypedDict(
    "DeleteRepositoryResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeDomainRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeDomainRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalDescribeDomainRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeDomainRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DescribeDomainRequestRequestTypeDef(
    _RequiredDescribeDomainRequestRequestTypeDef, _OptionalDescribeDomainRequestRequestTypeDef
):
    pass

DescribeDomainResultTypeDef = TypedDict(
    "DescribeDomainResultTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePackageVersionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalDescribePackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePackageVersionRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class DescribePackageVersionRequestRequestTypeDef(
    _RequiredDescribePackageVersionRequestRequestTypeDef,
    _OptionalDescribePackageVersionRequestRequestTypeDef,
):
    pass

DescribePackageVersionResultTypeDef = TypedDict(
    "DescribePackageVersionResultTypeDef",
    {
        "packageVersion": "PackageVersionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalDescribeRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeRepositoryRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DescribeRepositoryRequestRequestTypeDef(
    _RequiredDescribeRepositoryRequestRequestTypeDef,
    _OptionalDescribeRepositoryRequestRequestTypeDef,
):
    pass

DescribeRepositoryResultTypeDef = TypedDict(
    "DescribeRepositoryResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateExternalConnectionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
    },
)
_OptionalDisassociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateExternalConnectionRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DisassociateExternalConnectionRequestRequestTypeDef(
    _RequiredDisassociateExternalConnectionRequestRequestTypeDef,
    _OptionalDisassociateExternalConnectionRequestRequestTypeDef,
):
    pass

DisassociateExternalConnectionResultTypeDef = TypedDict(
    "DisassociateExternalConnectionResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisposePackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredDisposePackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": List[str],
    },
)
_OptionalDisposePackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalDisposePackageVersionsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versionRevisions": Dict[str, str],
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)

class DisposePackageVersionsRequestRequestTypeDef(
    _RequiredDisposePackageVersionsRequestRequestTypeDef,
    _OptionalDisposePackageVersionsRequestRequestTypeDef,
):
    pass

DisposePackageVersionsResultTypeDef = TypedDict(
    "DisposePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainDescriptionTypeDef = TypedDict(
    "DomainDescriptionTypeDef",
    {
        "name": str,
        "owner": str,
        "arn": str,
        "status": DomainStatusType,
        "createdTime": datetime,
        "encryptionKey": str,
        "repositoryCount": int,
        "assetSizeBytes": int,
        "s3BucketArn": str,
    },
    total=False,
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "name": str,
        "owner": str,
        "arn": str,
        "status": DomainStatusType,
        "createdTime": datetime,
        "encryptionKey": str,
    },
    total=False,
)

_RequiredGetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "_RequiredGetAuthorizationTokenRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalGetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "_OptionalGetAuthorizationTokenRequestRequestTypeDef",
    {
        "domainOwner": str,
        "durationSeconds": int,
    },
    total=False,
)

class GetAuthorizationTokenRequestRequestTypeDef(
    _RequiredGetAuthorizationTokenRequestRequestTypeDef,
    _OptionalGetAuthorizationTokenRequestRequestTypeDef,
):
    pass

GetAuthorizationTokenResultTypeDef = TypedDict(
    "GetAuthorizationTokenResultTypeDef",
    {
        "authorizationToken": str,
        "expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalGetDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class GetDomainPermissionsPolicyRequestRequestTypeDef(
    _RequiredGetDomainPermissionsPolicyRequestRequestTypeDef,
    _OptionalGetDomainPermissionsPolicyRequestRequestTypeDef,
):
    pass

GetDomainPermissionsPolicyResultTypeDef = TypedDict(
    "GetDomainPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPackageVersionAssetRequestRequestTypeDef = TypedDict(
    "_RequiredGetPackageVersionAssetRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "asset": str,
    },
)
_OptionalGetPackageVersionAssetRequestRequestTypeDef = TypedDict(
    "_OptionalGetPackageVersionAssetRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "packageVersionRevision": str,
    },
    total=False,
)

class GetPackageVersionAssetRequestRequestTypeDef(
    _RequiredGetPackageVersionAssetRequestRequestTypeDef,
    _OptionalGetPackageVersionAssetRequestRequestTypeDef,
):
    pass

GetPackageVersionAssetResultTypeDef = TypedDict(
    "GetPackageVersionAssetResultTypeDef",
    {
        "asset": StreamingBody,
        "assetName": str,
        "packageVersion": str,
        "packageVersionRevision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetPackageVersionReadmeRequestRequestTypeDef = TypedDict(
    "_RequiredGetPackageVersionReadmeRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalGetPackageVersionReadmeRequestRequestTypeDef = TypedDict(
    "_OptionalGetPackageVersionReadmeRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class GetPackageVersionReadmeRequestRequestTypeDef(
    _RequiredGetPackageVersionReadmeRequestRequestTypeDef,
    _OptionalGetPackageVersionReadmeRequestRequestTypeDef,
):
    pass

GetPackageVersionReadmeResultTypeDef = TypedDict(
    "GetPackageVersionReadmeResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "readme": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryEndpointRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
    },
)
_OptionalGetRepositoryEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryEndpointRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class GetRepositoryEndpointRequestRequestTypeDef(
    _RequiredGetRepositoryEndpointRequestRequestTypeDef,
    _OptionalGetRepositoryEndpointRequestRequestTypeDef,
):
    pass

GetRepositoryEndpointResultTypeDef = TypedDict(
    "GetRepositoryEndpointResultTypeDef",
    {
        "repositoryEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalGetRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class GetRepositoryPermissionsPolicyRequestRequestTypeDef(
    _RequiredGetRepositoryPermissionsPolicyRequestRequestTypeDef,
    _OptionalGetRepositoryPermissionsPolicyRequestRequestTypeDef,
):
    pass

GetRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "GetRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LicenseInfoTypeDef = TypedDict(
    "LicenseInfoTypeDef",
    {
        "name": str,
        "url": str,
    },
    total=False,
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef",
    {
        "domains": List["DomainSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackageVersionAssetsRequestRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionAssetsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalListPackageVersionAssetsRequestRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionAssetsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListPackageVersionAssetsRequestRequestTypeDef(
    _RequiredListPackageVersionAssetsRequestRequestTypeDef,
    _OptionalListPackageVersionAssetsRequestRequestTypeDef,
):
    pass

ListPackageVersionAssetsResultTypeDef = TypedDict(
    "ListPackageVersionAssetsResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "assets": List["AssetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackageVersionDependenciesRequestRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionDependenciesRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
    },
)
_OptionalListPackageVersionDependenciesRequestRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionDependenciesRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "nextToken": str,
    },
    total=False,
)

class ListPackageVersionDependenciesRequestRequestTypeDef(
    _RequiredListPackageVersionDependenciesRequestRequestTypeDef,
    _OptionalListPackageVersionDependenciesRequestRequestTypeDef,
):
    pass

ListPackageVersionDependenciesResultTypeDef = TypedDict(
    "ListPackageVersionDependenciesResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "dependencies": List["PackageDependencyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackageVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredListPackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalListPackageVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalListPackageVersionsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "status": PackageVersionStatusType,
        "sortBy": Literal["PUBLISHED_TIME"],
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListPackageVersionsRequestRequestTypeDef(
    _RequiredListPackageVersionsRequestRequestTypeDef,
    _OptionalListPackageVersionsRequestRequestTypeDef,
):
    pass

ListPackageVersionsResultTypeDef = TypedDict(
    "ListPackageVersionsResultTypeDef",
    {
        "defaultDisplayVersion": str,
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "versions": List["PackageVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPackagesRequestRequestTypeDef = TypedDict(
    "_RequiredListPackagesRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalListPackagesRequestRequestTypeDef = TypedDict(
    "_OptionalListPackagesRequestRequestTypeDef",
    {
        "domainOwner": str,
        "format": PackageFormatType,
        "namespace": str,
        "packagePrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListPackagesRequestRequestTypeDef(
    _RequiredListPackagesRequestRequestTypeDef, _OptionalListPackagesRequestRequestTypeDef
):
    pass

ListPackagesResultTypeDef = TypedDict(
    "ListPackagesResultTypeDef",
    {
        "packages": List["PackageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListRepositoriesInDomainRequestRequestTypeDef = TypedDict(
    "_RequiredListRepositoriesInDomainRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalListRepositoriesInDomainRequestRequestTypeDef = TypedDict(
    "_OptionalListRepositoriesInDomainRequestRequestTypeDef",
    {
        "domainOwner": str,
        "administratorAccount": str,
        "repositoryPrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListRepositoriesInDomainRequestRequestTypeDef(
    _RequiredListRepositoriesInDomainRequestRequestTypeDef,
    _OptionalListRepositoriesInDomainRequestRequestTypeDef,
):
    pass

ListRepositoriesInDomainResultTypeDef = TypedDict(
    "ListRepositoriesInDomainResultTypeDef",
    {
        "repositories": List["RepositorySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesRequestRequestTypeDef = TypedDict(
    "ListRepositoriesRequestRequestTypeDef",
    {
        "repositoryPrefix": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListRepositoriesResultTypeDef = TypedDict(
    "ListRepositoriesResultTypeDef",
    {
        "repositories": List["RepositorySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PackageDependencyTypeDef = TypedDict(
    "PackageDependencyTypeDef",
    {
        "namespace": str,
        "package": str,
        "dependencyType": str,
        "versionRequirement": str,
    },
    total=False,
)

PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
    },
    total=False,
)

PackageVersionDescriptionTypeDef = TypedDict(
    "PackageVersionDescriptionTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "packageName": str,
        "displayName": str,
        "version": str,
        "summary": str,
        "homePage": str,
        "sourceCodeRepository": str,
        "publishedTime": datetime,
        "licenses": List["LicenseInfoTypeDef"],
        "revision": str,
        "status": PackageVersionStatusType,
    },
    total=False,
)

PackageVersionErrorTypeDef = TypedDict(
    "PackageVersionErrorTypeDef",
    {
        "errorCode": PackageVersionErrorCodeType,
        "errorMessage": str,
    },
    total=False,
)

_RequiredPackageVersionSummaryTypeDef = TypedDict(
    "_RequiredPackageVersionSummaryTypeDef",
    {
        "version": str,
        "status": PackageVersionStatusType,
    },
)
_OptionalPackageVersionSummaryTypeDef = TypedDict(
    "_OptionalPackageVersionSummaryTypeDef",
    {
        "revision": str,
    },
    total=False,
)

class PackageVersionSummaryTypeDef(
    _RequiredPackageVersionSummaryTypeDef, _OptionalPackageVersionSummaryTypeDef
):
    pass

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPutDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "policyDocument": str,
    },
)
_OptionalPutDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)

class PutDomainPermissionsPolicyRequestRequestTypeDef(
    _RequiredPutDomainPermissionsPolicyRequestRequestTypeDef,
    _OptionalPutDomainPermissionsPolicyRequestRequestTypeDef,
):
    pass

PutDomainPermissionsPolicyResultTypeDef = TypedDict(
    "PutDomainPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredPutRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "policyDocument": str,
    },
)
_OptionalPutRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalPutRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domainOwner": str,
        "policyRevision": str,
    },
    total=False,
)

class PutRepositoryPermissionsPolicyRequestRequestTypeDef(
    _RequiredPutRepositoryPermissionsPolicyRequestRequestTypeDef,
    _OptionalPutRepositoryPermissionsPolicyRequestRequestTypeDef,
):
    pass

PutRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "PutRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryDescriptionTypeDef = TypedDict(
    "RepositoryDescriptionTypeDef",
    {
        "name": str,
        "administratorAccount": str,
        "domainName": str,
        "domainOwner": str,
        "arn": str,
        "description": str,
        "upstreams": List["UpstreamRepositoryInfoTypeDef"],
        "externalConnections": List["RepositoryExternalConnectionInfoTypeDef"],
    },
    total=False,
)

RepositoryExternalConnectionInfoTypeDef = TypedDict(
    "RepositoryExternalConnectionInfoTypeDef",
    {
        "externalConnectionName": str,
        "packageFormat": PackageFormatType,
        "status": Literal["Available"],
    },
    total=False,
)

RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "name": str,
        "administratorAccount": str,
        "domainName": str,
        "domainOwner": str,
        "arn": str,
        "description": str,
    },
    total=False,
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "resourceArn": str,
        "revision": str,
        "document": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SuccessfulPackageVersionInfoTypeDef = TypedDict(
    "SuccessfulPackageVersionInfoTypeDef",
    {
        "revision": str,
        "status": PackageVersionStatusType,
    },
    total=False,
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": List["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdatePackageVersionsStatusRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageVersionsStatusRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": List[str],
        "targetStatus": PackageVersionStatusType,
    },
)
_OptionalUpdatePackageVersionsStatusRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageVersionsStatusRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "versionRevisions": Dict[str, str],
        "expectedStatus": PackageVersionStatusType,
    },
    total=False,
)

class UpdatePackageVersionsStatusRequestRequestTypeDef(
    _RequiredUpdatePackageVersionsStatusRequestRequestTypeDef,
    _OptionalUpdatePackageVersionsStatusRequestRequestTypeDef,
):
    pass

UpdatePackageVersionsStatusResultTypeDef = TypedDict(
    "UpdatePackageVersionsStatusResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
    },
)
_OptionalUpdateRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRepositoryRequestRequestTypeDef",
    {
        "domainOwner": str,
        "description": str,
        "upstreams": List["UpstreamRepositoryTypeDef"],
    },
    total=False,
)

class UpdateRepositoryRequestRequestTypeDef(
    _RequiredUpdateRepositoryRequestRequestTypeDef, _OptionalUpdateRepositoryRequestRequestTypeDef
):
    pass

UpdateRepositoryResultTypeDef = TypedDict(
    "UpdateRepositoryResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpstreamRepositoryInfoTypeDef = TypedDict(
    "UpstreamRepositoryInfoTypeDef",
    {
        "repositoryName": str,
    },
    total=False,
)

UpstreamRepositoryTypeDef = TypedDict(
    "UpstreamRepositoryTypeDef",
    {
        "repositoryName": str,
    },
)
