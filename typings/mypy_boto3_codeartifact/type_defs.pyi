"""
Type annotations for codeartifact service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_codeartifact.type_defs import AssetSummaryTypeDef

    data: AssetSummaryTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import IO, Any, Union

from botocore.response import StreamingBody

from .literals import (
    AllowPublishType,
    AllowUpstreamType,
    DomainStatusType,
    EndpointTypeType,
    HashAlgorithmType,
    PackageFormatType,
    PackageGroupAllowedRepositoryUpdateTypeType,
    PackageGroupAssociationTypeType,
    PackageGroupOriginRestrictionModeType,
    PackageGroupOriginRestrictionTypeType,
    PackageVersionErrorCodeType,
    PackageVersionOriginTypeType,
    PackageVersionStatusType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AssetSummaryTypeDef",
    "AssociateExternalConnectionRequestTypeDef",
    "AssociateExternalConnectionResultTypeDef",
    "AssociatedPackageTypeDef",
    "BlobTypeDef",
    "CopyPackageVersionsRequestTypeDef",
    "CopyPackageVersionsResultTypeDef",
    "CreateDomainRequestTypeDef",
    "CreateDomainResultTypeDef",
    "CreatePackageGroupRequestTypeDef",
    "CreatePackageGroupResultTypeDef",
    "CreateRepositoryRequestTypeDef",
    "CreateRepositoryResultTypeDef",
    "DeleteDomainPermissionsPolicyRequestTypeDef",
    "DeleteDomainPermissionsPolicyResultTypeDef",
    "DeleteDomainRequestTypeDef",
    "DeleteDomainResultTypeDef",
    "DeletePackageGroupRequestTypeDef",
    "DeletePackageGroupResultTypeDef",
    "DeletePackageRequestTypeDef",
    "DeletePackageResultTypeDef",
    "DeletePackageVersionsRequestTypeDef",
    "DeletePackageVersionsResultTypeDef",
    "DeleteRepositoryPermissionsPolicyRequestTypeDef",
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    "DeleteRepositoryRequestTypeDef",
    "DeleteRepositoryResultTypeDef",
    "DescribeDomainRequestTypeDef",
    "DescribeDomainResultTypeDef",
    "DescribePackageGroupRequestTypeDef",
    "DescribePackageGroupResultTypeDef",
    "DescribePackageRequestTypeDef",
    "DescribePackageResultTypeDef",
    "DescribePackageVersionRequestTypeDef",
    "DescribePackageVersionResultTypeDef",
    "DescribeRepositoryRequestTypeDef",
    "DescribeRepositoryResultTypeDef",
    "DisassociateExternalConnectionRequestTypeDef",
    "DisassociateExternalConnectionResultTypeDef",
    "DisposePackageVersionsRequestTypeDef",
    "DisposePackageVersionsResultTypeDef",
    "DomainDescriptionTypeDef",
    "DomainEntryPointTypeDef",
    "DomainSummaryTypeDef",
    "GetAssociatedPackageGroupRequestTypeDef",
    "GetAssociatedPackageGroupResultTypeDef",
    "GetAuthorizationTokenRequestTypeDef",
    "GetAuthorizationTokenResultTypeDef",
    "GetDomainPermissionsPolicyRequestTypeDef",
    "GetDomainPermissionsPolicyResultTypeDef",
    "GetPackageVersionAssetRequestTypeDef",
    "GetPackageVersionAssetResultTypeDef",
    "GetPackageVersionReadmeRequestTypeDef",
    "GetPackageVersionReadmeResultTypeDef",
    "GetRepositoryEndpointRequestTypeDef",
    "GetRepositoryEndpointResultTypeDef",
    "GetRepositoryPermissionsPolicyRequestTypeDef",
    "GetRepositoryPermissionsPolicyResultTypeDef",
    "LicenseInfoTypeDef",
    "ListAllowedRepositoriesForGroupRequestPaginateTypeDef",
    "ListAllowedRepositoriesForGroupRequestTypeDef",
    "ListAllowedRepositoriesForGroupResultTypeDef",
    "ListAssociatedPackagesRequestPaginateTypeDef",
    "ListAssociatedPackagesRequestTypeDef",
    "ListAssociatedPackagesResultTypeDef",
    "ListDomainsRequestPaginateTypeDef",
    "ListDomainsRequestTypeDef",
    "ListDomainsResultTypeDef",
    "ListPackageGroupsRequestPaginateTypeDef",
    "ListPackageGroupsRequestTypeDef",
    "ListPackageGroupsResultTypeDef",
    "ListPackageVersionAssetsRequestPaginateTypeDef",
    "ListPackageVersionAssetsRequestTypeDef",
    "ListPackageVersionAssetsResultTypeDef",
    "ListPackageVersionDependenciesRequestTypeDef",
    "ListPackageVersionDependenciesResultTypeDef",
    "ListPackageVersionsRequestPaginateTypeDef",
    "ListPackageVersionsRequestTypeDef",
    "ListPackageVersionsResultTypeDef",
    "ListPackagesRequestPaginateTypeDef",
    "ListPackagesRequestTypeDef",
    "ListPackagesResultTypeDef",
    "ListRepositoriesInDomainRequestPaginateTypeDef",
    "ListRepositoriesInDomainRequestTypeDef",
    "ListRepositoriesInDomainResultTypeDef",
    "ListRepositoriesRequestPaginateTypeDef",
    "ListRepositoriesRequestTypeDef",
    "ListRepositoriesResultTypeDef",
    "ListSubPackageGroupsRequestPaginateTypeDef",
    "ListSubPackageGroupsRequestTypeDef",
    "ListSubPackageGroupsResultTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PackageDependencyTypeDef",
    "PackageDescriptionTypeDef",
    "PackageGroupAllowedRepositoryTypeDef",
    "PackageGroupDescriptionTypeDef",
    "PackageGroupOriginConfigurationTypeDef",
    "PackageGroupOriginRestrictionTypeDef",
    "PackageGroupReferenceTypeDef",
    "PackageGroupSummaryTypeDef",
    "PackageOriginConfigurationTypeDef",
    "PackageOriginRestrictionsTypeDef",
    "PackageSummaryTypeDef",
    "PackageVersionDescriptionTypeDef",
    "PackageVersionErrorTypeDef",
    "PackageVersionOriginTypeDef",
    "PackageVersionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PublishPackageVersionRequestTypeDef",
    "PublishPackageVersionResultTypeDef",
    "PutDomainPermissionsPolicyRequestTypeDef",
    "PutDomainPermissionsPolicyResultTypeDef",
    "PutPackageOriginConfigurationRequestTypeDef",
    "PutPackageOriginConfigurationResultTypeDef",
    "PutRepositoryPermissionsPolicyRequestTypeDef",
    "PutRepositoryPermissionsPolicyResultTypeDef",
    "RepositoryDescriptionTypeDef",
    "RepositoryExternalConnectionInfoTypeDef",
    "RepositorySummaryTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "SuccessfulPackageVersionInfoTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdatePackageGroupOriginConfigurationRequestTypeDef",
    "UpdatePackageGroupOriginConfigurationResultTypeDef",
    "UpdatePackageGroupRequestTypeDef",
    "UpdatePackageGroupResultTypeDef",
    "UpdatePackageVersionsStatusRequestTypeDef",
    "UpdatePackageVersionsStatusResultTypeDef",
    "UpdateRepositoryRequestTypeDef",
    "UpdateRepositoryResultTypeDef",
    "UpstreamRepositoryInfoTypeDef",
    "UpstreamRepositoryTypeDef",
)

class AssetSummaryTypeDef(TypedDict):
    name: str
    size: NotRequired[int]
    hashes: NotRequired[Dict[HashAlgorithmType, str]]

class AssociateExternalConnectionRequestTypeDef(TypedDict):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

AssociatedPackageTypeDef = TypedDict(
    "AssociatedPackageTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "package": NotRequired[str],
        "associationType": NotRequired[PackageGroupAssociationTypeType],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CopyPackageVersionsRequestTypeDef = TypedDict(
    "CopyPackageVersionsRequestTypeDef",
    {
        "domain": str,
        "sourceRepository": str,
        "destinationRepository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versions": NotRequired[Sequence[str]],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "allowOverwrite": NotRequired[bool],
        "includeFromUpstream": NotRequired[bool],
    },
)

class PackageVersionErrorTypeDef(TypedDict):
    errorCode: NotRequired[PackageVersionErrorCodeType]
    errorMessage: NotRequired[str]

class SuccessfulPackageVersionInfoTypeDef(TypedDict):
    revision: NotRequired[str]
    status: NotRequired[PackageVersionStatusType]

class TagTypeDef(TypedDict):
    key: str
    value: str

class DomainDescriptionTypeDef(TypedDict):
    name: NotRequired[str]
    owner: NotRequired[str]
    arn: NotRequired[str]
    status: NotRequired[DomainStatusType]
    createdTime: NotRequired[datetime]
    encryptionKey: NotRequired[str]
    repositoryCount: NotRequired[int]
    assetSizeBytes: NotRequired[int]
    s3BucketArn: NotRequired[str]

class UpstreamRepositoryTypeDef(TypedDict):
    repositoryName: str

class DeleteDomainPermissionsPolicyRequestTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]
    policyRevision: NotRequired[str]

class ResourcePolicyTypeDef(TypedDict):
    resourceArn: NotRequired[str]
    revision: NotRequired[str]
    document: NotRequired[str]

class DeleteDomainRequestTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]

class DeletePackageGroupRequestTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]

DeletePackageRequestTypeDef = TypedDict(
    "DeletePackageRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)
DeletePackageVersionsRequestTypeDef = TypedDict(
    "DeletePackageVersionsRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)

class DeleteRepositoryPermissionsPolicyRequestTypeDef(TypedDict):
    domain: str
    repository: str
    domainOwner: NotRequired[str]
    policyRevision: NotRequired[str]

class DeleteRepositoryRequestTypeDef(TypedDict):
    domain: str
    repository: str
    domainOwner: NotRequired[str]

class DescribeDomainRequestTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]

class DescribePackageGroupRequestTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]

DescribePackageRequestTypeDef = TypedDict(
    "DescribePackageRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)
DescribePackageVersionRequestTypeDef = TypedDict(
    "DescribePackageVersionRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)

class DescribeRepositoryRequestTypeDef(TypedDict):
    domain: str
    repository: str
    domainOwner: NotRequired[str]

class DisassociateExternalConnectionRequestTypeDef(TypedDict):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: NotRequired[str]

DisposePackageVersionsRequestTypeDef = TypedDict(
    "DisposePackageVersionsRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)

class DomainEntryPointTypeDef(TypedDict):
    repositoryName: NotRequired[str]
    externalConnectionName: NotRequired[str]

class DomainSummaryTypeDef(TypedDict):
    name: NotRequired[str]
    owner: NotRequired[str]
    arn: NotRequired[str]
    status: NotRequired[DomainStatusType]
    createdTime: NotRequired[datetime]
    encryptionKey: NotRequired[str]

GetAssociatedPackageGroupRequestTypeDef = TypedDict(
    "GetAssociatedPackageGroupRequestTypeDef",
    {
        "domain": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)

class GetAuthorizationTokenRequestTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]
    durationSeconds: NotRequired[int]

class GetDomainPermissionsPolicyRequestTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]

GetPackageVersionAssetRequestTypeDef = TypedDict(
    "GetPackageVersionAssetRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "asset": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "packageVersionRevision": NotRequired[str],
    },
)
GetPackageVersionReadmeRequestTypeDef = TypedDict(
    "GetPackageVersionReadmeRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)
GetRepositoryEndpointRequestTypeDef = TypedDict(
    "GetRepositoryEndpointRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "domainOwner": NotRequired[str],
        "endpointType": NotRequired[EndpointTypeType],
    },
)

class GetRepositoryPermissionsPolicyRequestTypeDef(TypedDict):
    domain: str
    repository: str
    domainOwner: NotRequired[str]

class LicenseInfoTypeDef(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAllowedRepositoriesForGroupRequestTypeDef(TypedDict):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListAssociatedPackagesRequestTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    preview: NotRequired[bool]

class ListDomainsRequestTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListPackageGroupsRequestTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    prefix: NotRequired[str]

ListPackageVersionAssetsRequestTypeDef = TypedDict(
    "ListPackageVersionAssetsRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListPackageVersionDependenciesRequestTypeDef = TypedDict(
    "ListPackageVersionDependenciesRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

class PackageDependencyTypeDef(TypedDict):
    namespace: NotRequired[str]
    package: NotRequired[str]
    dependencyType: NotRequired[str]
    versionRequirement: NotRequired[str]

ListPackageVersionsRequestTypeDef = TypedDict(
    "ListPackageVersionsRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
        "sortBy": NotRequired[Literal["PUBLISHED_TIME"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "originType": NotRequired[PackageVersionOriginTypeType],
    },
)
ListPackagesRequestTypeDef = TypedDict(
    "ListPackagesRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "packagePrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "publish": NotRequired[AllowPublishType],
        "upstream": NotRequired[AllowUpstreamType],
    },
)

class ListRepositoriesInDomainRequestTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]
    administratorAccount: NotRequired[str]
    repositoryPrefix: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class RepositorySummaryTypeDef(TypedDict):
    name: NotRequired[str]
    administratorAccount: NotRequired[str]
    domainName: NotRequired[str]
    domainOwner: NotRequired[str]
    arn: NotRequired[str]
    description: NotRequired[str]
    createdTime: NotRequired[datetime]

class ListRepositoriesRequestTypeDef(TypedDict):
    repositoryPrefix: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListSubPackageGroupsRequestTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class PackageGroupAllowedRepositoryTypeDef(TypedDict):
    repositoryName: NotRequired[str]
    originRestrictionType: NotRequired[PackageGroupOriginRestrictionTypeType]

class PackageGroupReferenceTypeDef(TypedDict):
    arn: NotRequired[str]
    pattern: NotRequired[str]

class PackageOriginRestrictionsTypeDef(TypedDict):
    publish: AllowPublishType
    upstream: AllowUpstreamType

class PutDomainPermissionsPolicyRequestTypeDef(TypedDict):
    domain: str
    policyDocument: str
    domainOwner: NotRequired[str]
    policyRevision: NotRequired[str]

class PutRepositoryPermissionsPolicyRequestTypeDef(TypedDict):
    domain: str
    repository: str
    policyDocument: str
    domainOwner: NotRequired[str]
    policyRevision: NotRequired[str]

class RepositoryExternalConnectionInfoTypeDef(TypedDict):
    externalConnectionName: NotRequired[str]
    packageFormat: NotRequired[PackageFormatType]
    status: NotRequired[Literal["Available"]]

class UpstreamRepositoryInfoTypeDef(TypedDict):
    repositoryName: NotRequired[str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePackageGroupRequestTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]
    contactInfo: NotRequired[str]
    description: NotRequired[str]

UpdatePackageVersionsStatusRequestTypeDef = TypedDict(
    "UpdatePackageVersionsStatusRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "targetStatus": PackageVersionStatusType,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)

class GetAuthorizationTokenResultTypeDef(TypedDict):
    authorizationToken: str
    expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPackageVersionAssetResultTypeDef(TypedDict):
    asset: StreamingBody
    assetName: str
    packageVersion: str
    packageVersionRevision: str
    ResponseMetadata: ResponseMetadataTypeDef

GetPackageVersionReadmeResultTypeDef = TypedDict(
    "GetPackageVersionReadmeResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "readme": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class GetRepositoryEndpointResultTypeDef(TypedDict):
    repositoryEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAllowedRepositoriesForGroupResultTypeDef(TypedDict):
    allowedRepositories: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

ListPackageVersionAssetsResultTypeDef = TypedDict(
    "ListPackageVersionAssetsResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "assets": List[AssetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "nextToken": NotRequired[str],
    },
)
PublishPackageVersionResultTypeDef = TypedDict(
    "PublishPackageVersionResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "status": PackageVersionStatusType,
        "asset": AssetSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

class ListAssociatedPackagesResultTypeDef(TypedDict):
    packages: List[AssociatedPackageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

PublishPackageVersionRequestTypeDef = TypedDict(
    "PublishPackageVersionRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "assetContent": BlobTypeDef,
        "assetName": str,
        "assetSHA256": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "unfinished": NotRequired[bool],
    },
)

class CopyPackageVersionsResultTypeDef(TypedDict):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageVersionsResultTypeDef(TypedDict):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisposePackageVersionsResultTypeDef(TypedDict):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageVersionsStatusResultTypeDef(TypedDict):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainRequestTypeDef(TypedDict):
    domain: str
    encryptionKey: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class CreatePackageGroupRequestTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]
    contactInfo: NotRequired[str]
    description: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]

class ListTagsForResourceResultTypeDef(TypedDict):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateDomainResultTypeDef(TypedDict):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResultTypeDef(TypedDict):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainResultTypeDef(TypedDict):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryRequestTypeDef(TypedDict):
    domain: str
    repository: str
    domainOwner: NotRequired[str]
    description: NotRequired[str]
    upstreams: NotRequired[Sequence[UpstreamRepositoryTypeDef]]
    tags: NotRequired[Sequence[TagTypeDef]]

class UpdateRepositoryRequestTypeDef(TypedDict):
    domain: str
    repository: str
    domainOwner: NotRequired[str]
    description: NotRequired[str]
    upstreams: NotRequired[Sequence[UpstreamRepositoryTypeDef]]

class DeleteDomainPermissionsPolicyResultTypeDef(TypedDict):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryPermissionsPolicyResultTypeDef(TypedDict):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainPermissionsPolicyResultTypeDef(TypedDict):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryPermissionsPolicyResultTypeDef(TypedDict):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDomainPermissionsPolicyResultTypeDef(TypedDict):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRepositoryPermissionsPolicyResultTypeDef(TypedDict):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PackageVersionOriginTypeDef(TypedDict):
    domainEntryPoint: NotRequired[DomainEntryPointTypeDef]
    originType: NotRequired[PackageVersionOriginTypeType]

class ListDomainsResultTypeDef(TypedDict):
    domains: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAllowedRepositoriesForGroupRequestPaginateTypeDef(TypedDict):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListAssociatedPackagesRequestPaginateTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]
    preview: NotRequired[bool]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDomainsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListPackageGroupsRequestPaginateTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]
    prefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListPackageVersionAssetsRequestPaginateTypeDef = TypedDict(
    "ListPackageVersionAssetsRequestPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackageVersionsRequestPaginateTypeDef = TypedDict(
    "ListPackageVersionsRequestPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
        "sortBy": NotRequired[Literal["PUBLISHED_TIME"]],
        "originType": NotRequired[PackageVersionOriginTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPackagesRequestPaginateTypeDef = TypedDict(
    "ListPackagesRequestPaginateTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "packagePrefix": NotRequired[str],
        "publish": NotRequired[AllowPublishType],
        "upstream": NotRequired[AllowUpstreamType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)

class ListRepositoriesInDomainRequestPaginateTypeDef(TypedDict):
    domain: str
    domainOwner: NotRequired[str]
    administratorAccount: NotRequired[str]
    repositoryPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRepositoriesRequestPaginateTypeDef(TypedDict):
    repositoryPrefix: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSubPackageGroupsRequestPaginateTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

ListPackageVersionDependenciesResultTypeDef = TypedDict(
    "ListPackageVersionDependenciesResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "dependencies": List[PackageDependencyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "nextToken": NotRequired[str],
    },
)

class ListRepositoriesInDomainResultTypeDef(TypedDict):
    repositories: List[RepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListRepositoriesResultTypeDef(TypedDict):
    repositories: List[RepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class UpdatePackageGroupOriginConfigurationRequestTypeDef(TypedDict):
    domain: str
    packageGroup: str
    domainOwner: NotRequired[str]
    restrictions: NotRequired[
        Mapping[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionModeType]
    ]
    addAllowedRepositories: NotRequired[Sequence[PackageGroupAllowedRepositoryTypeDef]]
    removeAllowedRepositories: NotRequired[Sequence[PackageGroupAllowedRepositoryTypeDef]]

class PackageGroupOriginRestrictionTypeDef(TypedDict):
    mode: NotRequired[PackageGroupOriginRestrictionModeType]
    effectiveMode: NotRequired[PackageGroupOriginRestrictionModeType]
    inheritedFrom: NotRequired[PackageGroupReferenceTypeDef]
    repositoriesCount: NotRequired[int]

class PackageOriginConfigurationTypeDef(TypedDict):
    restrictions: NotRequired[PackageOriginRestrictionsTypeDef]

PutPackageOriginConfigurationRequestTypeDef = TypedDict(
    "PutPackageOriginConfigurationRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "restrictions": PackageOriginRestrictionsTypeDef,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)

class RepositoryDescriptionTypeDef(TypedDict):
    name: NotRequired[str]
    administratorAccount: NotRequired[str]
    domainName: NotRequired[str]
    domainOwner: NotRequired[str]
    arn: NotRequired[str]
    description: NotRequired[str]
    upstreams: NotRequired[List[UpstreamRepositoryInfoTypeDef]]
    externalConnections: NotRequired[List[RepositoryExternalConnectionInfoTypeDef]]
    createdTime: NotRequired[datetime]

PackageVersionDescriptionTypeDef = TypedDict(
    "PackageVersionDescriptionTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "packageName": NotRequired[str],
        "displayName": NotRequired[str],
        "version": NotRequired[str],
        "summary": NotRequired[str],
        "homePage": NotRequired[str],
        "sourceCodeRepository": NotRequired[str],
        "publishedTime": NotRequired[datetime],
        "licenses": NotRequired[List[LicenseInfoTypeDef]],
        "revision": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
        "origin": NotRequired[PackageVersionOriginTypeDef],
    },
)

class PackageVersionSummaryTypeDef(TypedDict):
    version: str
    status: PackageVersionStatusType
    revision: NotRequired[str]
    origin: NotRequired[PackageVersionOriginTypeDef]

class PackageGroupOriginConfigurationTypeDef(TypedDict):
    restrictions: NotRequired[
        Dict[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionTypeDef]
    ]

PackageDescriptionTypeDef = TypedDict(
    "PackageDescriptionTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "name": NotRequired[str],
        "originConfiguration": NotRequired[PackageOriginConfigurationTypeDef],
    },
)
PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "package": NotRequired[str],
        "originConfiguration": NotRequired[PackageOriginConfigurationTypeDef],
    },
)

class PutPackageOriginConfigurationResultTypeDef(TypedDict):
    originConfiguration: PackageOriginConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateExternalConnectionResultTypeDef(TypedDict):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryResultTypeDef(TypedDict):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryResultTypeDef(TypedDict):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRepositoryResultTypeDef(TypedDict):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateExternalConnectionResultTypeDef(TypedDict):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRepositoryResultTypeDef(TypedDict):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageVersionResultTypeDef(TypedDict):
    packageVersion: PackageVersionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

ListPackageVersionsResultTypeDef = TypedDict(
    "ListPackageVersionsResultTypeDef",
    {
        "defaultDisplayVersion": str,
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "versions": List[PackageVersionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "nextToken": NotRequired[str],
    },
)

class PackageGroupDescriptionTypeDef(TypedDict):
    arn: NotRequired[str]
    pattern: NotRequired[str]
    domainName: NotRequired[str]
    domainOwner: NotRequired[str]
    createdTime: NotRequired[datetime]
    contactInfo: NotRequired[str]
    description: NotRequired[str]
    originConfiguration: NotRequired[PackageGroupOriginConfigurationTypeDef]
    parent: NotRequired[PackageGroupReferenceTypeDef]

class PackageGroupSummaryTypeDef(TypedDict):
    arn: NotRequired[str]
    pattern: NotRequired[str]
    domainName: NotRequired[str]
    domainOwner: NotRequired[str]
    createdTime: NotRequired[datetime]
    contactInfo: NotRequired[str]
    description: NotRequired[str]
    originConfiguration: NotRequired[PackageGroupOriginConfigurationTypeDef]
    parent: NotRequired[PackageGroupReferenceTypeDef]

class DescribePackageResultTypeDef(TypedDict):
    package: PackageDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageResultTypeDef(TypedDict):
    deletedPackage: PackageSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagesResultTypeDef(TypedDict):
    packages: List[PackageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class CreatePackageGroupResultTypeDef(TypedDict):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageGroupResultTypeDef(TypedDict):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageGroupResultTypeDef(TypedDict):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedPackageGroupResultTypeDef(TypedDict):
    packageGroup: PackageGroupDescriptionTypeDef
    associationType: PackageGroupAssociationTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageGroupOriginConfigurationResultTypeDef(TypedDict):
    packageGroup: PackageGroupDescriptionTypeDef
    allowedRepositoryUpdates: Dict[
        PackageGroupOriginRestrictionTypeType,
        Dict[PackageGroupAllowedRepositoryUpdateTypeType, List[str]],
    ]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageGroupResultTypeDef(TypedDict):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageGroupsResultTypeDef(TypedDict):
    packageGroups: List[PackageGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSubPackageGroupsResultTypeDef(TypedDict):
    packageGroups: List[PackageGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]
