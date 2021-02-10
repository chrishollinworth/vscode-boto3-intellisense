"""
Main interface for ecr-public service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ecr_public import ECRPublicClient

    client: ECRPublicClient = boto3.client("ecr-public")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_ecr_public.paginator import (
    DescribeImagesPaginator,
    DescribeImageTagsPaginator,
    DescribeRegistriesPaginator,
    DescribeRepositoriesPaginator,
)
from mypy_boto3_ecr_public.type_defs import (
    BatchCheckLayerAvailabilityResponseTypeDef,
    BatchDeleteImageResponseTypeDef,
    CompleteLayerUploadResponseTypeDef,
    CreateRepositoryResponseTypeDef,
    DeleteRepositoryPolicyResponseTypeDef,
    DeleteRepositoryResponseTypeDef,
    DescribeImagesResponseTypeDef,
    DescribeImageTagsResponseTypeDef,
    DescribeRegistriesResponseTypeDef,
    DescribeRepositoriesResponseTypeDef,
    GetAuthorizationTokenResponseTypeDef,
    GetRegistryCatalogDataResponseTypeDef,
    GetRepositoryCatalogDataResponseTypeDef,
    GetRepositoryPolicyResponseTypeDef,
    ImageIdentifierTypeDef,
    InitiateLayerUploadResponseTypeDef,
    PutImageResponseTypeDef,
    PutRegistryCatalogDataResponseTypeDef,
    PutRepositoryCatalogDataResponseTypeDef,
    RepositoryCatalogDataInputTypeDef,
    SetRepositoryPolicyResponseTypeDef,
    UploadLayerPartResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ECRPublicClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    EmptyUploadException: Type[BotocoreClientError]
    ImageAlreadyExistsException: Type[BotocoreClientError]
    ImageDigestDoesNotMatchException: Type[BotocoreClientError]
    ImageNotFoundException: Type[BotocoreClientError]
    ImageTagAlreadyExistsException: Type[BotocoreClientError]
    InvalidLayerException: Type[BotocoreClientError]
    InvalidLayerPartException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LayerAlreadyExistsException: Type[BotocoreClientError]
    LayerPartTooSmallException: Type[BotocoreClientError]
    LayersNotFoundException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ReferencedImagesNotFoundException: Type[BotocoreClientError]
    RegistryNotFoundException: Type[BotocoreClientError]
    RepositoryAlreadyExistsException: Type[BotocoreClientError]
    RepositoryNotEmptyException: Type[BotocoreClientError]
    RepositoryNotFoundException: Type[BotocoreClientError]
    RepositoryPolicyNotFoundException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    UnsupportedCommandException: Type[BotocoreClientError]
    UploadNotFoundException: Type[BotocoreClientError]


class ECRPublicClient:
    """
    [ECRPublic.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_check_layer_availability(
        self, repositoryName: str, layerDigests: List[str], registryId: str = None
    ) -> BatchCheckLayerAvailabilityResponseTypeDef:
        """
        [Client.batch_check_layer_availability documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.batch_check_layer_availability)
        """

    def batch_delete_image(
        self, repositoryName: str, imageIds: List["ImageIdentifierTypeDef"], registryId: str = None
    ) -> BatchDeleteImageResponseTypeDef:
        """
        [Client.batch_delete_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.batch_delete_image)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.can_paginate)
        """

    def complete_layer_upload(
        self, repositoryName: str, uploadId: str, layerDigests: List[str], registryId: str = None
    ) -> CompleteLayerUploadResponseTypeDef:
        """
        [Client.complete_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.complete_layer_upload)
        """

    def create_repository(
        self, repositoryName: str, catalogData: RepositoryCatalogDataInputTypeDef = None
    ) -> CreateRepositoryResponseTypeDef:
        """
        [Client.create_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.create_repository)
        """

    def delete_repository(
        self, repositoryName: str, registryId: str = None, force: bool = None
    ) -> DeleteRepositoryResponseTypeDef:
        """
        [Client.delete_repository documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.delete_repository)
        """

    def delete_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> DeleteRepositoryPolicyResponseTypeDef:
        """
        [Client.delete_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.delete_repository_policy)
        """

    def describe_image_tags(
        self,
        repositoryName: str,
        registryId: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeImageTagsResponseTypeDef:
        """
        [Client.describe_image_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.describe_image_tags)
        """

    def describe_images(
        self,
        repositoryName: str,
        registryId: str = None,
        imageIds: List["ImageIdentifierTypeDef"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeImagesResponseTypeDef:
        """
        [Client.describe_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.describe_images)
        """

    def describe_registries(
        self, nextToken: str = None, maxResults: int = None
    ) -> DescribeRegistriesResponseTypeDef:
        """
        [Client.describe_registries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.describe_registries)
        """

    def describe_repositories(
        self,
        registryId: str = None,
        repositoryNames: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeRepositoriesResponseTypeDef:
        """
        [Client.describe_repositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.describe_repositories)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.generate_presigned_url)
        """

    def get_authorization_token(self) -> GetAuthorizationTokenResponseTypeDef:
        """
        [Client.get_authorization_token documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.get_authorization_token)
        """

    def get_registry_catalog_data(self) -> GetRegistryCatalogDataResponseTypeDef:
        """
        [Client.get_registry_catalog_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.get_registry_catalog_data)
        """

    def get_repository_catalog_data(
        self, repositoryName: str, registryId: str = None
    ) -> GetRepositoryCatalogDataResponseTypeDef:
        """
        [Client.get_repository_catalog_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.get_repository_catalog_data)
        """

    def get_repository_policy(
        self, repositoryName: str, registryId: str = None
    ) -> GetRepositoryPolicyResponseTypeDef:
        """
        [Client.get_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.get_repository_policy)
        """

    def initiate_layer_upload(
        self, repositoryName: str, registryId: str = None
    ) -> InitiateLayerUploadResponseTypeDef:
        """
        [Client.initiate_layer_upload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.initiate_layer_upload)
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
        [Client.put_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.put_image)
        """

    def put_registry_catalog_data(
        self, displayName: str = None
    ) -> PutRegistryCatalogDataResponseTypeDef:
        """
        [Client.put_registry_catalog_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.put_registry_catalog_data)
        """

    def put_repository_catalog_data(
        self,
        repositoryName: str,
        catalogData: RepositoryCatalogDataInputTypeDef,
        registryId: str = None,
    ) -> PutRepositoryCatalogDataResponseTypeDef:
        """
        [Client.put_repository_catalog_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.put_repository_catalog_data)
        """

    def set_repository_policy(
        self, repositoryName: str, policyText: str, registryId: str = None, force: bool = None
    ) -> SetRepositoryPolicyResponseTypeDef:
        """
        [Client.set_repository_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.set_repository_policy)
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
        [Client.upload_layer_part documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Client.upload_layer_part)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_image_tags"]
    ) -> DescribeImageTagsPaginator:
        """
        [Paginator.DescribeImageTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeImageTags)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Paginator.DescribeImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeImages)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_registries"]
    ) -> DescribeRegistriesPaginator:
        """
        [Paginator.DescribeRegistries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeRegistries)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_repositories"]
    ) -> DescribeRepositoriesPaginator:
        """
        [Paginator.DescribeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/ecr-public.html#ECRPublic.Paginator.DescribeRepositories)
        """
