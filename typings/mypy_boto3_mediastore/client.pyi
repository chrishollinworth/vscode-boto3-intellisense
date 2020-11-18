# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for mediastore service client

Usage::

    ```python
    import boto3
    from mypy_boto3_mediastore import MediaStoreClient

    client: MediaStoreClient = boto3.client("mediastore")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_mediastore.paginator import ListContainersPaginator
from mypy_boto3_mediastore.type_defs import (
    CorsRuleTypeDef,
    CreateContainerOutputTypeDef,
    DescribeContainerOutputTypeDef,
    GetContainerPolicyOutputTypeDef,
    GetCorsPolicyOutputTypeDef,
    GetLifecyclePolicyOutputTypeDef,
    GetMetricPolicyOutputTypeDef,
    ListContainersOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    MetricPolicyTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaStoreClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ContainerInUseException: Type[BotocoreClientError]
    ContainerNotFoundException: Type[BotocoreClientError]
    CorsPolicyNotFoundException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PolicyNotFoundException: Type[BotocoreClientError]


class MediaStoreClient:
    """
    [MediaStore.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.can_paginate)
        """

    def create_container(
        self, ContainerName: str, Tags: List["TagTypeDef"] = None
    ) -> CreateContainerOutputTypeDef:
        """
        [Client.create_container documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.create_container)
        """

    def delete_container(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Client.delete_container documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.delete_container)
        """

    def delete_container_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Client.delete_container_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.delete_container_policy)
        """

    def delete_cors_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Client.delete_cors_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.delete_cors_policy)
        """

    def delete_lifecycle_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Client.delete_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.delete_lifecycle_policy)
        """

    def delete_metric_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Client.delete_metric_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.delete_metric_policy)
        """

    def describe_container(self, ContainerName: str = None) -> DescribeContainerOutputTypeDef:
        """
        [Client.describe_container documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.describe_container)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.generate_presigned_url)
        """

    def get_container_policy(self, ContainerName: str) -> GetContainerPolicyOutputTypeDef:
        """
        [Client.get_container_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.get_container_policy)
        """

    def get_cors_policy(self, ContainerName: str) -> GetCorsPolicyOutputTypeDef:
        """
        [Client.get_cors_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.get_cors_policy)
        """

    def get_lifecycle_policy(self, ContainerName: str) -> GetLifecyclePolicyOutputTypeDef:
        """
        [Client.get_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.get_lifecycle_policy)
        """

    def get_metric_policy(self, ContainerName: str) -> GetMetricPolicyOutputTypeDef:
        """
        [Client.get_metric_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.get_metric_policy)
        """

    def list_containers(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListContainersOutputTypeDef:
        """
        [Client.list_containers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.list_containers)
        """

    def list_tags_for_resource(self, Resource: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.list_tags_for_resource)
        """

    def put_container_policy(self, ContainerName: str, Policy: str) -> Dict[str, Any]:
        """
        [Client.put_container_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.put_container_policy)
        """

    def put_cors_policy(
        self, ContainerName: str, CorsPolicy: List["CorsRuleTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Client.put_cors_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.put_cors_policy)
        """

    def put_lifecycle_policy(self, ContainerName: str, LifecyclePolicy: str) -> Dict[str, Any]:
        """
        [Client.put_lifecycle_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.put_lifecycle_policy)
        """

    def put_metric_policy(
        self, ContainerName: str, MetricPolicy: "MetricPolicyTypeDef"
    ) -> Dict[str, Any]:
        """
        [Client.put_metric_policy documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.put_metric_policy)
        """

    def start_access_logging(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Client.start_access_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.start_access_logging)
        """

    def stop_access_logging(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Client.stop_access_logging documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.stop_access_logging)
        """

    def tag_resource(self, Resource: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.tag_resource)
        """

    def untag_resource(self, Resource: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Client.untag_resource)
        """

    def get_paginator(self, operation_name: Literal["list_containers"]) -> ListContainersPaginator:
        """
        [Paginator.ListContainers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/mediastore.html#MediaStore.Paginator.ListContainers)
        """
