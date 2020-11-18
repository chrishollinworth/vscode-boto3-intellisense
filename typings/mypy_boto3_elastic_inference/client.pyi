# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for elastic-inference service client

Usage::

    ```python
    import boto3
    from mypy_boto3_elastic_inference import ElasticInferenceClient

    client: ElasticInferenceClient = boto3.client("elastic-inference")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_elastic_inference.paginator import DescribeAcceleratorsPaginator
from mypy_boto3_elastic_inference.type_defs import (
    DescribeAcceleratorOfferingsResponseTypeDef,
    DescribeAcceleratorsResponseTypeDef,
    DescribeAcceleratorTypesResponseTypeDef,
    FilterTypeDef,
    ListTagsForResourceResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ElasticInferenceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class ElasticInferenceClient:
    """
    [ElasticInference.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client.can_paginate)
        """

    def describe_accelerator_offerings(
        self,
        locationType: Literal["region", "availability-zone", "availability-zone-id"],
        acceleratorTypes: List[str] = None,
    ) -> DescribeAcceleratorOfferingsResponseTypeDef:
        """
        [Client.describe_accelerator_offerings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerator_offerings)
        """

    def describe_accelerator_types(self) -> DescribeAcceleratorTypesResponseTypeDef:
        """
        [Client.describe_accelerator_types documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerator_types)
        """

    def describe_accelerators(
        self,
        acceleratorIds: List[str] = None,
        filters: List[FilterTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeAcceleratorsResponseTypeDef:
        """
        [Client.describe_accelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerators)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client.generate_presigned_url)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client.list_tags_for_resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Client.untag_resource)
        """

    def get_paginator(
        self, operation_name: Literal["describe_accelerators"]
    ) -> DescribeAcceleratorsPaginator:
        """
        [Paginator.DescribeAccelerators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/elastic-inference.html#ElasticInference.Paginator.DescribeAccelerators)
        """
