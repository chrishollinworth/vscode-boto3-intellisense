"""
Type annotations for elastic-inference service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_elastic_inference import ElasticInferenceClient

    client: ElasticInferenceClient = boto3.client("elastic-inference")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import BaseClient, ClientMeta

from .literals import LocationTypeType
from .paginator import DescribeAcceleratorsPaginator
from .type_defs import (
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

class ElasticInferenceClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ElasticInferenceClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#close)
        """
    def describe_accelerator_offerings(
        self, *, locationType: LocationTypeType, acceleratorTypes: List[str] = None
    ) -> DescribeAcceleratorOfferingsResponseTypeDef:
        """
        Describes the locations in which a given accelerator type or set of types is
        present in a given region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerator_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#describe_accelerator_offerings)
        """
    def describe_accelerator_types(self) -> DescribeAcceleratorTypesResponseTypeDef:
        """
        Describes the accelerator types available in a given region, as well as their
        characteristics, such as memory and throughput.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerator_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#describe_accelerator_types)
        """
    def describe_accelerators(
        self,
        *,
        acceleratorIds: List[str] = None,
        filters: List["FilterTypeDef"] = None,
        maxResults: int = None,
        nextToken: str = None
    ) -> DescribeAcceleratorsResponseTypeDef:
        """
        Describes information over a provided set of accelerators belonging to an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.describe_accelerators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#describe_accelerators)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#generate_presigned_url)
        """
    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceResultTypeDef:
        """
        Returns all tags of an Elastic Inference Accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#list_tags_for_resource)
        """
    def tag_resource(self, *, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        Adds the specified tags to an Elastic Inference Accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#tag_resource)
        """
    def untag_resource(self, *, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from an Elastic Inference Accelerator.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/client.html#untag_resource)
        """
    def get_paginator(
        self, operation_name: Literal["describe_accelerators"]
    ) -> DescribeAcceleratorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.26.121/reference/services/elastic-inference.html#ElasticInference.Paginator.DescribeAccelerators)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/paginators.html#describeacceleratorspaginator)
        """
