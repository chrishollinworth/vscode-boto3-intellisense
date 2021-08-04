"""
Type annotations for ecr-public service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecr_public.type_defs import AuthorizationDataTypeDef

    data: AuthorizationDataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from .literals import (
    ImageFailureCodeType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    RegistryAliasStatusType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AuthorizationDataTypeDef",
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageRequestRequestTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "CompleteLayerUploadRequestRequestTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageTagsRequestRequestTypeDef",
    "DescribeImageTagsResponseTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribeRegistriesRequestRequestTypeDef",
    "DescribeRegistriesResponseTypeDef",
    "DescribeRepositoriesRequestRequestTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetRegistryCatalogDataResponseTypeDef",
    "GetRepositoryCatalogDataRequestRequestTypeDef",
    "GetRepositoryCatalogDataResponseTypeDef",
    "GetRepositoryPolicyRequestRequestTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageTagDetailTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadRequestRequestTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageRequestRequestTypeDef",
    "PutImageResponseTypeDef",
    "PutRegistryCatalogDataRequestRequestTypeDef",
    "PutRegistryCatalogDataResponseTypeDef",
    "PutRepositoryCatalogDataRequestRequestTypeDef",
    "PutRepositoryCatalogDataResponseTypeDef",
    "ReferencedImageDetailTypeDef",
    "RegistryAliasTypeDef",
    "RegistryCatalogDataTypeDef",
    "RegistryTypeDef",
    "RepositoryCatalogDataInputTypeDef",
    "RepositoryCatalogDataTypeDef",
    "RepositoryTypeDef",
    "ResponseMetadataTypeDef",
    "SetRepositoryPolicyRequestRequestTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UploadLayerPartRequestRequestTypeDef",
    "UploadLayerPartResponseTypeDef",
)

AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": str,
        "expiresAt": datetime,
    },
    total=False,
)

_RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "_RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigests": List[str],
    },
)
_OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "_OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class BatchCheckLayerAvailabilityRequestRequestTypeDef(
    _RequiredBatchCheckLayerAvailabilityRequestRequestTypeDef,
    _OptionalBatchCheckLayerAvailabilityRequestRequestTypeDef,
):
    pass

BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List["LayerTypeDef"],
        "failures": List["LayerFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredBatchDeleteImageRequestRequestTypeDef = TypedDict(
    "_RequiredBatchDeleteImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": List["ImageIdentifierTypeDef"],
    },
)
_OptionalBatchDeleteImageRequestRequestTypeDef = TypedDict(
    "_OptionalBatchDeleteImageRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class BatchDeleteImageRequestRequestTypeDef(
    _RequiredBatchDeleteImageRequestRequestTypeDef, _OptionalBatchDeleteImageRequestRequestTypeDef
):
    pass

BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "failures": List["ImageFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "_RequiredCompleteLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "layerDigests": List[str],
    },
)
_OptionalCompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "_OptionalCompleteLayerUploadRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class CompleteLayerUploadRequestRequestTypeDef(
    _RequiredCompleteLayerUploadRequestRequestTypeDef,
    _OptionalCompleteLayerUploadRequestRequestTypeDef,
):
    pass

CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalCreateRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRepositoryRequestRequestTypeDef",
    {
        "catalogData": "RepositoryCatalogDataInputTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateRepositoryRequestRequestTypeDef(
    _RequiredCreateRepositoryRequestRequestTypeDef, _OptionalCreateRepositoryRequestRequestTypeDef
):
    pass

CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "catalogData": "RepositoryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class DeleteRepositoryPolicyRequestRequestTypeDef(
    _RequiredDeleteRepositoryPolicyRequestRequestTypeDef,
    _OptionalDeleteRepositoryPolicyRequestRequestTypeDef,
):
    pass

DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDeleteRepositoryRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRepositoryRequestRequestTypeDef",
    {
        "registryId": str,
        "force": bool,
    },
    total=False,
)

class DeleteRepositoryRequestRequestTypeDef(
    _RequiredDeleteRepositoryRequestRequestTypeDef, _OptionalDeleteRepositoryRequestRequestTypeDef
):
    pass

DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageTagsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImageTagsRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDescribeImageTagsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImageTagsRequestRequestTypeDef",
    {
        "registryId": str,
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeImageTagsRequestRequestTypeDef(
    _RequiredDescribeImageTagsRequestRequestTypeDef, _OptionalDescribeImageTagsRequestRequestTypeDef
):
    pass

DescribeImageTagsResponseTypeDef = TypedDict(
    "DescribeImageTagsResponseTypeDef",
    {
        "imageTagDetails": List["ImageTagDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImagesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalDescribeImagesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImagesRequestRequestTypeDef",
    {
        "registryId": str,
        "imageIds": List["ImageIdentifierTypeDef"],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class DescribeImagesRequestRequestTypeDef(
    _RequiredDescribeImagesRequestRequestTypeDef, _OptionalDescribeImagesRequestRequestTypeDef
):
    pass

DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {
        "imageDetails": List["ImageDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistriesRequestRequestTypeDef = TypedDict(
    "DescribeRegistriesRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeRegistriesResponseTypeDef = TypedDict(
    "DescribeRegistriesResponseTypeDef",
    {
        "registries": List["RegistryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoriesRequestRequestTypeDef = TypedDict(
    "DescribeRepositoriesRequestRequestTypeDef",
    {
        "registryId": str,
        "repositoryNames": List[str],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List["RepositoryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": "AuthorizationDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryCatalogDataResponseTypeDef = TypedDict(
    "GetRegistryCatalogDataResponseTypeDef",
    {
        "registryCatalogData": "RegistryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryCatalogDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryCatalogDataRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetRepositoryCatalogDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryCatalogDataRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class GetRepositoryCatalogDataRequestRequestTypeDef(
    _RequiredGetRepositoryCatalogDataRequestRequestTypeDef,
    _OptionalGetRepositoryCatalogDataRequestRequestTypeDef,
):
    pass

GetRepositoryCatalogDataResponseTypeDef = TypedDict(
    "GetRepositoryCatalogDataResponseTypeDef",
    {
        "catalogData": "RepositoryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalGetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class GetRepositoryPolicyRequestRequestTypeDef(
    _RequiredGetRepositoryPolicyRequestRequestTypeDef,
    _OptionalGetRepositoryPolicyRequestRequestTypeDef,
):
    pass

GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageDigest": str,
        "imageTags": List[str],
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageManifestMediaType": str,
        "artifactMediaType": str,
    },
    total=False,
)

ImageFailureTypeDef = TypedDict(
    "ImageFailureTypeDef",
    {
        "imageId": "ImageIdentifierTypeDef",
        "failureCode": ImageFailureCodeType,
        "failureReason": str,
    },
    total=False,
)

ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef",
    {
        "imageDigest": str,
        "imageTag": str,
    },
    total=False,
)

ImageTagDetailTypeDef = TypedDict(
    "ImageTagDetailTypeDef",
    {
        "imageTag": str,
        "createdAt": datetime,
        "imageDetail": "ReferencedImageDetailTypeDef",
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "imageId": "ImageIdentifierTypeDef",
        "imageManifest": str,
        "imageManifestMediaType": str,
    },
    total=False,
)

_RequiredInitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "_RequiredInitiateLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
    },
)
_OptionalInitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "_OptionalInitiateLayerUploadRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class InitiateLayerUploadRequestRequestTypeDef(
    _RequiredInitiateLayerUploadRequestRequestTypeDef,
    _OptionalInitiateLayerUploadRequestRequestTypeDef,
):
    pass

InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": str,
        "failureCode": LayerFailureCodeType,
        "failureReason": str,
    },
    total=False,
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": str,
        "layerAvailability": LayerAvailabilityType,
        "layerSize": int,
        "mediaType": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

_RequiredPutImageRequestRequestTypeDef = TypedDict(
    "_RequiredPutImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageManifest": str,
    },
)
_OptionalPutImageRequestRequestTypeDef = TypedDict(
    "_OptionalPutImageRequestRequestTypeDef",
    {
        "registryId": str,
        "imageManifestMediaType": str,
        "imageTag": str,
        "imageDigest": str,
    },
    total=False,
)

class PutImageRequestRequestTypeDef(
    _RequiredPutImageRequestRequestTypeDef, _OptionalPutImageRequestRequestTypeDef
):
    pass

PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef",
    {
        "image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryCatalogDataRequestRequestTypeDef = TypedDict(
    "PutRegistryCatalogDataRequestRequestTypeDef",
    {
        "displayName": str,
    },
    total=False,
)

PutRegistryCatalogDataResponseTypeDef = TypedDict(
    "PutRegistryCatalogDataResponseTypeDef",
    {
        "registryCatalogData": "RegistryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPutRepositoryCatalogDataRequestRequestTypeDef = TypedDict(
    "_RequiredPutRepositoryCatalogDataRequestRequestTypeDef",
    {
        "repositoryName": str,
        "catalogData": "RepositoryCatalogDataInputTypeDef",
    },
)
_OptionalPutRepositoryCatalogDataRequestRequestTypeDef = TypedDict(
    "_OptionalPutRepositoryCatalogDataRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class PutRepositoryCatalogDataRequestRequestTypeDef(
    _RequiredPutRepositoryCatalogDataRequestRequestTypeDef,
    _OptionalPutRepositoryCatalogDataRequestRequestTypeDef,
):
    pass

PutRepositoryCatalogDataResponseTypeDef = TypedDict(
    "PutRepositoryCatalogDataResponseTypeDef",
    {
        "catalogData": "RepositoryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReferencedImageDetailTypeDef = TypedDict(
    "ReferencedImageDetailTypeDef",
    {
        "imageDigest": str,
        "imageSizeInBytes": int,
        "imagePushedAt": datetime,
        "imageManifestMediaType": str,
        "artifactMediaType": str,
    },
    total=False,
)

RegistryAliasTypeDef = TypedDict(
    "RegistryAliasTypeDef",
    {
        "name": str,
        "status": RegistryAliasStatusType,
        "primaryRegistryAlias": bool,
        "defaultRegistryAlias": bool,
    },
)

RegistryCatalogDataTypeDef = TypedDict(
    "RegistryCatalogDataTypeDef",
    {
        "displayName": str,
    },
    total=False,
)

RegistryTypeDef = TypedDict(
    "RegistryTypeDef",
    {
        "registryId": str,
        "registryArn": str,
        "registryUri": str,
        "verified": bool,
        "aliases": List["RegistryAliasTypeDef"],
    },
)

RepositoryCatalogDataInputTypeDef = TypedDict(
    "RepositoryCatalogDataInputTypeDef",
    {
        "description": str,
        "architectures": List[str],
        "operatingSystems": List[str],
        "logoImageBlob": Union[bytes, IO[bytes], StreamingBody],
        "aboutText": str,
        "usageText": str,
    },
    total=False,
)

RepositoryCatalogDataTypeDef = TypedDict(
    "RepositoryCatalogDataTypeDef",
    {
        "description": str,
        "architectures": List[str],
        "operatingSystems": List[str],
        "logoUrl": str,
        "aboutText": str,
        "usageText": str,
        "marketplaceCertified": bool,
    },
    total=False,
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": str,
        "registryId": str,
        "repositoryName": str,
        "repositoryUri": str,
        "createdAt": datetime,
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

_RequiredSetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredSetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "policyText": str,
    },
)
_OptionalSetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalSetRepositoryPolicyRequestRequestTypeDef",
    {
        "registryId": str,
        "force": bool,
    },
    total=False,
)

class SetRepositoryPolicyRequestRequestTypeDef(
    _RequiredSetRepositoryPolicyRequestRequestTypeDef,
    _OptionalSetRepositoryPolicyRequestRequestTypeDef,
):
    pass

SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "Key": str,
        "Value": str,
    },
    total=False,
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUploadLayerPartRequestRequestTypeDef = TypedDict(
    "_RequiredUploadLayerPartRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "partFirstByte": int,
        "partLastByte": int,
        "layerPartBlob": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalUploadLayerPartRequestRequestTypeDef = TypedDict(
    "_OptionalUploadLayerPartRequestRequestTypeDef",
    {
        "registryId": str,
    },
    total=False,
)

class UploadLayerPartRequestRequestTypeDef(
    _RequiredUploadLayerPartRequestRequestTypeDef, _OptionalUploadLayerPartRequestRequestTypeDef
):
    pass

UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
