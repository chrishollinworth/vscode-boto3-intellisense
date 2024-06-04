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
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    AllowPublishType,
    AllowUpstreamType,
    DomainStatusType,
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
    "AssociatedPackageTypeDef",
    "CopyPackageVersionsRequestRequestTypeDef",
    "CopyPackageVersionsResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResultTypeDef",
    "CreatePackageGroupRequestRequestTypeDef",
    "CreatePackageGroupResultTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "CreateRepositoryResultTypeDef",
    "DeleteDomainPermissionsPolicyRequestRequestTypeDef",
    "DeleteDomainPermissionsPolicyResultTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResultTypeDef",
    "DeletePackageGroupRequestRequestTypeDef",
    "DeletePackageGroupResultTypeDef",
    "DeletePackageRequestRequestTypeDef",
    "DeletePackageResultTypeDef",
    "DeletePackageVersionsRequestRequestTypeDef",
    "DeletePackageVersionsResultTypeDef",
    "DeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DeleteRepositoryResultTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResultTypeDef",
    "DescribePackageGroupRequestRequestTypeDef",
    "DescribePackageGroupResultTypeDef",
    "DescribePackageRequestRequestTypeDef",
    "DescribePackageResultTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "DescribePackageVersionResultTypeDef",
    "DescribeRepositoryRequestRequestTypeDef",
    "DescribeRepositoryResultTypeDef",
    "DisassociateExternalConnectionRequestRequestTypeDef",
    "DisassociateExternalConnectionResultTypeDef",
    "DisposePackageVersionsRequestRequestTypeDef",
    "DisposePackageVersionsResultTypeDef",
    "DomainDescriptionTypeDef",
    "DomainEntryPointTypeDef",
    "DomainSummaryTypeDef",
    "GetAssociatedPackageGroupRequestRequestTypeDef",
    "GetAssociatedPackageGroupResultTypeDef",
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
    "ListAllowedRepositoriesForGroupRequestRequestTypeDef",
    "ListAllowedRepositoriesForGroupResultTypeDef",
    "ListAssociatedPackagesRequestRequestTypeDef",
    "ListAssociatedPackagesResultTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResultTypeDef",
    "ListPackageGroupsRequestRequestTypeDef",
    "ListPackageGroupsResultTypeDef",
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
    "ListSubPackageGroupsRequestRequestTypeDef",
    "ListSubPackageGroupsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
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
    "PublishPackageVersionRequestRequestTypeDef",
    "PublishPackageVersionResultTypeDef",
    "PutDomainPermissionsPolicyRequestRequestTypeDef",
    "PutDomainPermissionsPolicyResultTypeDef",
    "PutPackageOriginConfigurationRequestRequestTypeDef",
    "PutPackageOriginConfigurationResultTypeDef",
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
    "UpdatePackageGroupOriginConfigurationRequestRequestTypeDef",
    "UpdatePackageGroupOriginConfigurationResultTypeDef",
    "UpdatePackageGroupRequestRequestTypeDef",
    "UpdatePackageGroupResultTypeDef",
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

AssociatedPackageTypeDef = TypedDict(
    "AssociatedPackageTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "associationType": PackageGroupAssociationTypeType,
    },
    total=False,
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

_RequiredCreatePackageGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePackageGroupRequestRequestTypeDef",
    {
        "domain": str,
        "packageGroup": str,
    },
)
_OptionalCreatePackageGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePackageGroupRequestRequestTypeDef",
    {
        "domainOwner": str,
        "contactInfo": str,
        "description": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreatePackageGroupRequestRequestTypeDef(
    _RequiredCreatePackageGroupRequestRequestTypeDef,
    _OptionalCreatePackageGroupRequestRequestTypeDef,
):
    pass

CreatePackageGroupResultTypeDef = TypedDict(
    "CreatePackageGroupResultTypeDef",
    {
        "packageGroup": "PackageGroupDescriptionTypeDef",
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

_RequiredDeletePackageGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageGroupRequestRequestTypeDef",
    {
        "domain": str,
        "packageGroup": str,
    },
)
_OptionalDeletePackageGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageGroupRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DeletePackageGroupRequestRequestTypeDef(
    _RequiredDeletePackageGroupRequestRequestTypeDef,
    _OptionalDeletePackageGroupRequestRequestTypeDef,
):
    pass

DeletePackageGroupResultTypeDef = TypedDict(
    "DeletePackageGroupResultTypeDef",
    {
        "packageGroup": "PackageGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeletePackageRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePackageRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalDeletePackageRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePackageRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class DeletePackageRequestRequestTypeDef(
    _RequiredDeletePackageRequestRequestTypeDef, _OptionalDeletePackageRequestRequestTypeDef
):
    pass

DeletePackageResultTypeDef = TypedDict(
    "DeletePackageResultTypeDef",
    {
        "deletedPackage": "PackageSummaryTypeDef",
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

_RequiredDescribePackageGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePackageGroupRequestRequestTypeDef",
    {
        "domain": str,
        "packageGroup": str,
    },
)
_OptionalDescribePackageGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePackageGroupRequestRequestTypeDef",
    {
        "domainOwner": str,
    },
    total=False,
)

class DescribePackageGroupRequestRequestTypeDef(
    _RequiredDescribePackageGroupRequestRequestTypeDef,
    _OptionalDescribePackageGroupRequestRequestTypeDef,
):
    pass

DescribePackageGroupResultTypeDef = TypedDict(
    "DescribePackageGroupResultTypeDef",
    {
        "packageGroup": "PackageGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribePackageRequestRequestTypeDef = TypedDict(
    "_RequiredDescribePackageRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalDescribePackageRequestRequestTypeDef = TypedDict(
    "_OptionalDescribePackageRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class DescribePackageRequestRequestTypeDef(
    _RequiredDescribePackageRequestRequestTypeDef, _OptionalDescribePackageRequestRequestTypeDef
):
    pass

DescribePackageResultTypeDef = TypedDict(
    "DescribePackageResultTypeDef",
    {
        "package": "PackageDescriptionTypeDef",
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

DomainEntryPointTypeDef = TypedDict(
    "DomainEntryPointTypeDef",
    {
        "repositoryName": str,
        "externalConnectionName": str,
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

_RequiredGetAssociatedPackageGroupRequestRequestTypeDef = TypedDict(
    "_RequiredGetAssociatedPackageGroupRequestRequestTypeDef",
    {
        "domain": str,
        "format": PackageFormatType,
        "package": str,
    },
)
_OptionalGetAssociatedPackageGroupRequestRequestTypeDef = TypedDict(
    "_OptionalGetAssociatedPackageGroupRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class GetAssociatedPackageGroupRequestRequestTypeDef(
    _RequiredGetAssociatedPackageGroupRequestRequestTypeDef,
    _OptionalGetAssociatedPackageGroupRequestRequestTypeDef,
):
    pass

GetAssociatedPackageGroupResultTypeDef = TypedDict(
    "GetAssociatedPackageGroupResultTypeDef",
    {
        "packageGroup": "PackageGroupDescriptionTypeDef",
        "associationType": PackageGroupAssociationTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListAllowedRepositoriesForGroupRequestRequestTypeDef = TypedDict(
    "_RequiredListAllowedRepositoriesForGroupRequestRequestTypeDef",
    {
        "domain": str,
        "packageGroup": str,
        "originRestrictionType": PackageGroupOriginRestrictionTypeType,
    },
)
_OptionalListAllowedRepositoriesForGroupRequestRequestTypeDef = TypedDict(
    "_OptionalListAllowedRepositoriesForGroupRequestRequestTypeDef",
    {
        "domainOwner": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListAllowedRepositoriesForGroupRequestRequestTypeDef(
    _RequiredListAllowedRepositoriesForGroupRequestRequestTypeDef,
    _OptionalListAllowedRepositoriesForGroupRequestRequestTypeDef,
):
    pass

ListAllowedRepositoriesForGroupResultTypeDef = TypedDict(
    "ListAllowedRepositoriesForGroupResultTypeDef",
    {
        "allowedRepositories": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListAssociatedPackagesRequestRequestTypeDef = TypedDict(
    "_RequiredListAssociatedPackagesRequestRequestTypeDef",
    {
        "domain": str,
        "packageGroup": str,
    },
)
_OptionalListAssociatedPackagesRequestRequestTypeDef = TypedDict(
    "_OptionalListAssociatedPackagesRequestRequestTypeDef",
    {
        "domainOwner": str,
        "maxResults": int,
        "nextToken": str,
        "preview": bool,
    },
    total=False,
)

class ListAssociatedPackagesRequestRequestTypeDef(
    _RequiredListAssociatedPackagesRequestRequestTypeDef,
    _OptionalListAssociatedPackagesRequestRequestTypeDef,
):
    pass

ListAssociatedPackagesResultTypeDef = TypedDict(
    "ListAssociatedPackagesResultTypeDef",
    {
        "packages": List["AssociatedPackageTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredListPackageGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListPackageGroupsRequestRequestTypeDef",
    {
        "domain": str,
    },
)
_OptionalListPackageGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListPackageGroupsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "maxResults": int,
        "nextToken": str,
        "prefix": str,
    },
    total=False,
)

class ListPackageGroupsRequestRequestTypeDef(
    _RequiredListPackageGroupsRequestRequestTypeDef, _OptionalListPackageGroupsRequestRequestTypeDef
):
    pass

ListPackageGroupsResultTypeDef = TypedDict(
    "ListPackageGroupsResultTypeDef",
    {
        "packageGroups": List["PackageGroupSummaryTypeDef"],
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
        "originType": PackageVersionOriginTypeType,
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
        "publish": AllowPublishType,
        "upstream": AllowUpstreamType,
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

_RequiredListSubPackageGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListSubPackageGroupsRequestRequestTypeDef",
    {
        "domain": str,
        "packageGroup": str,
    },
)
_OptionalListSubPackageGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListSubPackageGroupsRequestRequestTypeDef",
    {
        "domainOwner": str,
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

class ListSubPackageGroupsRequestRequestTypeDef(
    _RequiredListSubPackageGroupsRequestRequestTypeDef,
    _OptionalListSubPackageGroupsRequestRequestTypeDef,
):
    pass

ListSubPackageGroupsResultTypeDef = TypedDict(
    "ListSubPackageGroupsResultTypeDef",
    {
        "packageGroups": List["PackageGroupSummaryTypeDef"],
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

PackageDescriptionTypeDef = TypedDict(
    "PackageDescriptionTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "name": str,
        "originConfiguration": "PackageOriginConfigurationTypeDef",
    },
    total=False,
)

PackageGroupAllowedRepositoryTypeDef = TypedDict(
    "PackageGroupAllowedRepositoryTypeDef",
    {
        "repositoryName": str,
        "originRestrictionType": PackageGroupOriginRestrictionTypeType,
    },
    total=False,
)

PackageGroupDescriptionTypeDef = TypedDict(
    "PackageGroupDescriptionTypeDef",
    {
        "arn": str,
        "pattern": str,
        "domainName": str,
        "domainOwner": str,
        "createdTime": datetime,
        "contactInfo": str,
        "description": str,
        "originConfiguration": "PackageGroupOriginConfigurationTypeDef",
        "parent": "PackageGroupReferenceTypeDef",
    },
    total=False,
)

PackageGroupOriginConfigurationTypeDef = TypedDict(
    "PackageGroupOriginConfigurationTypeDef",
    {
        "restrictions": Dict[
            PackageGroupOriginRestrictionTypeType, "PackageGroupOriginRestrictionTypeDef"
        ],
    },
    total=False,
)

PackageGroupOriginRestrictionTypeDef = TypedDict(
    "PackageGroupOriginRestrictionTypeDef",
    {
        "mode": PackageGroupOriginRestrictionModeType,
        "effectiveMode": PackageGroupOriginRestrictionModeType,
        "inheritedFrom": "PackageGroupReferenceTypeDef",
        "repositoriesCount": int,
    },
    total=False,
)

PackageGroupReferenceTypeDef = TypedDict(
    "PackageGroupReferenceTypeDef",
    {
        "arn": str,
        "pattern": str,
    },
    total=False,
)

PackageGroupSummaryTypeDef = TypedDict(
    "PackageGroupSummaryTypeDef",
    {
        "arn": str,
        "pattern": str,
        "domainName": str,
        "domainOwner": str,
        "createdTime": datetime,
        "contactInfo": str,
        "description": str,
        "originConfiguration": "PackageGroupOriginConfigurationTypeDef",
        "parent": "PackageGroupReferenceTypeDef",
    },
    total=False,
)

PackageOriginConfigurationTypeDef = TypedDict(
    "PackageOriginConfigurationTypeDef",
    {
        "restrictions": "PackageOriginRestrictionsTypeDef",
    },
    total=False,
)

PackageOriginRestrictionsTypeDef = TypedDict(
    "PackageOriginRestrictionsTypeDef",
    {
        "publish": AllowPublishType,
        "upstream": AllowUpstreamType,
    },
)

PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "originConfiguration": "PackageOriginConfigurationTypeDef",
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
        "origin": "PackageVersionOriginTypeDef",
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

PackageVersionOriginTypeDef = TypedDict(
    "PackageVersionOriginTypeDef",
    {
        "domainEntryPoint": "DomainEntryPointTypeDef",
        "originType": PackageVersionOriginTypeType,
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
        "origin": "PackageVersionOriginTypeDef",
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

_RequiredPublishPackageVersionRequestRequestTypeDef = TypedDict(
    "_RequiredPublishPackageVersionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "assetContent": Union[bytes, IO[bytes], StreamingBody],
        "assetName": str,
        "assetSHA256": str,
    },
)
_OptionalPublishPackageVersionRequestRequestTypeDef = TypedDict(
    "_OptionalPublishPackageVersionRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
        "unfinished": bool,
    },
    total=False,
)

class PublishPackageVersionRequestRequestTypeDef(
    _RequiredPublishPackageVersionRequestRequestTypeDef,
    _OptionalPublishPackageVersionRequestRequestTypeDef,
):
    pass

PublishPackageVersionResultTypeDef = TypedDict(
    "PublishPackageVersionResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "status": PackageVersionStatusType,
        "asset": "AssetSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

_RequiredPutPackageOriginConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredPutPackageOriginConfigurationRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "restrictions": "PackageOriginRestrictionsTypeDef",
    },
)
_OptionalPutPackageOriginConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalPutPackageOriginConfigurationRequestRequestTypeDef",
    {
        "domainOwner": str,
        "namespace": str,
    },
    total=False,
)

class PutPackageOriginConfigurationRequestRequestTypeDef(
    _RequiredPutPackageOriginConfigurationRequestRequestTypeDef,
    _OptionalPutPackageOriginConfigurationRequestRequestTypeDef,
):
    pass

PutPackageOriginConfigurationResultTypeDef = TypedDict(
    "PutPackageOriginConfigurationResultTypeDef",
    {
        "originConfiguration": "PackageOriginConfigurationTypeDef",
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
        "createdTime": datetime,
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
        "createdTime": datetime,
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

_RequiredUpdatePackageGroupOriginConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageGroupOriginConfigurationRequestRequestTypeDef",
    {
        "domain": str,
        "packageGroup": str,
    },
)
_OptionalUpdatePackageGroupOriginConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageGroupOriginConfigurationRequestRequestTypeDef",
    {
        "domainOwner": str,
        "restrictions": Dict[
            PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionModeType
        ],
        "addAllowedRepositories": List["PackageGroupAllowedRepositoryTypeDef"],
        "removeAllowedRepositories": List["PackageGroupAllowedRepositoryTypeDef"],
    },
    total=False,
)

class UpdatePackageGroupOriginConfigurationRequestRequestTypeDef(
    _RequiredUpdatePackageGroupOriginConfigurationRequestRequestTypeDef,
    _OptionalUpdatePackageGroupOriginConfigurationRequestRequestTypeDef,
):
    pass

UpdatePackageGroupOriginConfigurationResultTypeDef = TypedDict(
    "UpdatePackageGroupOriginConfigurationResultTypeDef",
    {
        "packageGroup": "PackageGroupDescriptionTypeDef",
        "allowedRepositoryUpdates": Dict[
            PackageGroupOriginRestrictionTypeType,
            Dict[PackageGroupAllowedRepositoryUpdateTypeType, List[str]],
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdatePackageGroupRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePackageGroupRequestRequestTypeDef",
    {
        "domain": str,
        "packageGroup": str,
    },
)
_OptionalUpdatePackageGroupRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePackageGroupRequestRequestTypeDef",
    {
        "domainOwner": str,
        "contactInfo": str,
        "description": str,
    },
    total=False,
)

class UpdatePackageGroupRequestRequestTypeDef(
    _RequiredUpdatePackageGroupRequestRequestTypeDef,
    _OptionalUpdatePackageGroupRequestRequestTypeDef,
):
    pass

UpdatePackageGroupResultTypeDef = TypedDict(
    "UpdatePackageGroupResultTypeDef",
    {
        "packageGroup": "PackageGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
