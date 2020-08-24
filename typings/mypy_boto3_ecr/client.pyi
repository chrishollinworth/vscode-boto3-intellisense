# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for ecr service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ecr import ECRClient

    client: ECRClient = boto3.client("ecr")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter

from mypy_boto3_ecr.paginator import (
    DescribeImageScanFindingsPaginator,
    DescribeImagesPaginator,
    DescribeRepositoriesPaginator,
    GetLifecyclePolicyPreviewPaginator,
    ListImagesPaginator,
)
from mypy_boto3_ecr.type_defs import (
    BatchCheckLayerAvailabilityResponseTypeDef,
    BatchDeleteImageResponseTypeDef,
    BatchGetImageResponseTypeDef,
    CompleteLayerUploadResponseTypeDef,
    CreateRepositoryResponseTypeDef,
    DeleteLifecyclePolicyResponseTypeDef,
    DeleteRepositoryPolicyResponseTypeDef,
    DeleteRepositoryResponseTypeDef,
    DescribeImageScanFindingsResponseTypeDef,
    DescribeImagesFilterTypeDef,
    DescribeImagesResponseTypeDef,
    DescribeRepositoriesResponseTypeDef,
    EncryptionConfigurationTypeDef,
    GetAuthorizationTokenResponseTypeDef,
    GetDownloadUrlForLayerResponseTypeDef,
    GetLifecyclePolicyPreviewResponseTypeDef,
    GetLifecyclePolicyResponseTypeDef,
    GetRepositoryPolicyResponseTypeDef,
    ImageIdentifierTypeDef,
    ImageScanningConfigurationTypeDef,
    InitiateLayerUploadResponseTypeDef,
    LifecyclePolicyPreviewFilterTypeDef,
    ListImagesFilterTypeDef,
    ListImagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutImageResponseTypeDef,
    PutImageScanningConfigurationResponseTypeDef,
    PutImageTagMutabilityResponseTypeDef,
    PutLifecyclePolicyResponseTypeDef,
    SetRepositoryPolicyResponseTypeDef,
    StartImageScanResponseTypeDef,
    StartLifecyclePolicyPreviewResponseTypeDef,
    TagTypeDef,
    UploadLayerPartResponseTypeDef,
)
from mypy_boto3_ecr.waiter import ImageScanCompleteWaiter, LifecyclePolicyPreviewCompleteWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ECRClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    EmptyUploadException: Type[Boto3ClientError]
    ImageAlreadyExistsException: Type[Boto3ClientError]
    ImageDigestDoesNotMatchException: Type[Boto3ClientError]
    ImageNotFoundException: Type[Boto3ClientError]
    ImageTagAlreadyExistsException: Type[Boto3ClientError]
    InvalidLayerException: Type[Boto3ClientError]
    InvalidLayerPartException: Type[Boto3ClientError]
    InvalidParameterException: Type[Boto3ClientError]
    InvalidTagParameterException: Type[Boto3ClientError]
    KmsException: Type[Boto3ClientError]
    LayerAlreadyExistsException: Type[Boto3ClientError]
    LayerInaccessibleException: Type[Boto3ClientError]
    LayerPartTooSmallException: Type[Boto3ClientError]
    LayersNotFoundException: Type[Boto3ClientError]
    LifecyclePolicyNotFoundException: Type[Boto3ClientError]
    LifecyclePolicyPreviewInProgressException: Type[Boto3ClientError]
    LifecyclePolicyPreviewNotFoundException: Type[Boto3ClientError]
    LimitExceededException: Type[Boto3ClientError]
    ReferencedImagesNotFoundException: Type[Boto3ClientError]
    RepositoryAlreadyExistsException: Type[Boto3ClientError]
    RepositoryNotEmptyException: Type[Boto3ClientError]
    RepositoryNotFoundException: Type[Boto3ClientError]
    RepositoryPolicyNotFoundException: Type[Boto3ClientError]
    ScanNotFoundException: Type[Boto3ClientError]
    ServerException: Type[Boto3ClientError]
    TooManyTagsException: Type[Boto3ClientError]
    UnsupportedImageTypeException: Type[Boto3ClientError]
    UploadNotFoundException: Type[Boto3ClientError]


class ECRClient:
    """
    [ECR.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client)
    """

    exceptions: Exceptions

    def batch_check_layer_availability(
        self, repositoryName: str, layerDigests: List[str], registryId: str = None
    ) -> BatchCheckLayerAvailabilityResponseTypeDef:
        """
        [Client.batch_check_layer_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.batch_check_layer_availability)
        """

    def batch_delete_image(
        self, repositoryName: str, imageIds: List["ImageIdentifierTypeDef"], registryId: str = None
    ) -> BatchDeleteImageResponseTypeDef:
        """
        [Client.batch_delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.batch_delete_image)
        """

    def batch_get_image(
        self,
        repositoryName: str,
        imageIds: List["ImageIdentifierTypeDef"],
        registryId: str = None,
        acceptedMediaTypes: List[str] = None,
    ) -> BatchGetImageResponseTypeDef:
        """
        [Client.batch_get_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.batch_get_image)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.can_paginate)
        """

    def complete_layer_upload(
        self, repositoryName: str, uploadId: str, layerDigests: List[str], registryId: str = None
    ) -> CompleteLayerUploadResponseTypeDef:
        """
        [Client.complete_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.complete_layer_upload)
        """

    def create_repository(
        self,
        repositoryName: str,
        tags: List["TagTypeDef"] = None,
        imageTagMutability: Literal["MUTABLE", "IMMUTABLE"] = None,
        imageScanningConfiguration: "ImageScanningConfigurationTypeDef" = None,
        encryptionConfiguration: "EncryptionConfigurationTypeDef" = None,
    ) -> CreateRepositoryResponseTypeDef:
        """
        [Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.create_repository)
        """

    def delete_lifecycle_policy(
        self, repositoryName: str, registryId: str = None
    ) -> DeleteLifecyclePolicyResponseTypeDef:
        """
        [Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.delete_lifecycle_policy)
        """

    def delete_repository(
        self, repositoryName: str, registryId: str = None, force: bool = None
    ) -> DeleteRepositoryResponseTypeDef:
        """
        [Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.delete_repository)
        """

    def delete_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> DeleteRepositoryPolicyResponseTypeDef:
        """
        [Client.delete_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.delete_repository_policy)
        """

    def describe_image_scan_findings(
        self,
        repositoryName: str,
        imageId: "ImageIdentifierTypeDef",
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeImageScanFindingsResponseTypeDef:
        """
        [Client.describe_image_scan_findings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.describe_image_scan_findings)
        """

    def describe_images(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: DescribeImagesFilterTypeDef = None,
    ) -> DescribeImagesResponseTypeDef:
        """
        [Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.describe_images)
        """

    def describe_repositories(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeRepositoriesResponseTypeDef:
        """
        [Client.describe_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.describe_repositories)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.generate_presigned_url)
        """

    def get_authorization_token(
        self, registryIds: List[str] = None
    ) -> GetAuthorizationTokenResponseTypeDef:
        """
        [Client.get_authorization_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.get_authorization_token)
        """

    def get_download_url_for_layer(
        self, repositoryName: str, layerDigest: str, registryId: str = None
    ) -> GetDownloadUrlForLayerResponseTypeDef:
        """
        [Client.get_download_url_for_layer documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.get_download_url_for_layer)
        """

    def get_lifecycle_policy(
        self, repositoryName: str, registryId: str = None
    ) -> GetLifecyclePolicyResponseTypeDef:
        """
        [Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.get_lifecycle_policy)
        """

    def get_lifecycle_policy_preview(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: LifecyclePolicyPreviewFilterTypeDef = None,
    ) -> GetLifecyclePolicyPreviewResponseTypeDef:
        """
        [Client.get_lifecycle_policy_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.get_lifecycle_policy_preview)
        """

    def get_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> GetRepositoryPolicyResponseTypeDef:
        """
        [Client.get_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.get_repository_policy)
        """

    def initiate_layer_upload(
        self, repositoryName: str, registryId: str = None
    ) -> InitiateLayerUploadResponseTypeDef:
        """
        [Client.initiate_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.initiate_layer_upload)
        """

    def list_images(
        self,
        repositoryName: str,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ListImagesFilterTypeDef = None,
    ) -> ListImagesResponseTypeDef:
        """
        [Client.list_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.list_images)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.list_tags_for_resource)
        """

    def put_image(
        self,
        repositoryName: str,
        imageManifest: str,
        registryId: str = None,
        imageManifestMediaType: str = None,
        imageTag: str = None,
        imageDigest: str = None,
    ) -> PutImageResponseTypeDef:
        """
        [Client.put_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.put_image)
        """

    def put_image_scanning_configuration(
        self,
        repositoryName: str,
        imageScanningConfiguration: "ImageScanningConfigurationTypeDef",
        registryId: str = None,
    ) -> PutImageScanningConfigurationResponseTypeDef:
        """
        [Client.put_image_scanning_configuration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.put_image_scanning_configuration)
        """

    def put_image_tag_mutability(
        self,
        repositoryName: str,
        imageTagMutability: Literal["MUTABLE", "IMMUTABLE"],
        registryId: str = None,
    ) -> PutImageTagMutabilityResponseTypeDef:
        """
        [Client.put_image_tag_mutability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.put_image_tag_mutability)
        """

    def put_lifecycle_policy(
        self, repositoryName: str, lifecyclePolicyText: str, registryId: str = None
    ) -> PutLifecyclePolicyResponseTypeDef:
        """
        [Client.put_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.put_lifecycle_policy)
        """

    def set_repository_policy(
        self, repositoryName: str, policyText: str, registryId: str = None, force: bool = None
    ) -> SetRepositoryPolicyResponseTypeDef:
        """
        [Client.set_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.set_repository_policy)
        """

    def start_image_scan(
        self, repositoryName: str, imageId: "ImageIdentifierTypeDef", registryId: str = None
    ) -> StartImageScanResponseTypeDef:
        """
        [Client.start_image_scan documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.start_image_scan)
        """

    def start_lifecycle_policy_preview(
        self, repositoryName: str, registryId: str = None, lifecyclePolicyText: str = None
    ) -> StartLifecyclePolicyPreviewResponseTypeDef:
        """
        [Client.start_lifecycle_policy_preview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.start_lifecycle_policy_preview)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.untag_resource)
        """

    def upload_layer_part(
        self,
        repositoryName: str,
        uploadId: str,
        partFirstByte: int,
        partLastByte: int,
        layerPartBlob: Union[bytes, IO[bytes]],
        registryId: str = None,
    ) -> UploadLayerPartResponseTypeDef:
        """
        [Client.upload_layer_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Client.upload_layer_part)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_scan_findings"]
    ) -> DescribeImageScanFindingsPaginator:
        """
        [Paginator.DescribeImageScanFindings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeImageScanFindings)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_repositories"]
    ) -> DescribeRepositoriesPaginator:
        """
        [Paginator.DescribeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.DescribeRepositories)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_lifecycle_policy_preview"]
    ) -> GetLifecyclePolicyPreviewPaginator:
        """
        [Paginator.GetLifecyclePolicyPreview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.GetLifecyclePolicyPreview)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_images"]) -> ListImagesPaginator:
        """
        [Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Paginator.ListImages)
        """

    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        pass

    @overload
    def get_waiter(self, waiter_name: Literal["image_scan_complete"]) -> ImageScanCompleteWaiter:
        """
        [Waiter.ImageScanComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Waiter.ImageScanComplete)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["lifecycle_policy_preview_complete"]
    ) -> LifecyclePolicyPreviewCompleteWaiter:
        """
        [Waiter.LifecyclePolicyPreviewComplete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete)
        """

    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        pass
