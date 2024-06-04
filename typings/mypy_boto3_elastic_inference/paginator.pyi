"""
Type annotations for elastic-inference service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_elastic_inference import ElasticInferenceClient
    from mypy_boto3_elastic_inference.paginator import (
        DescribeAcceleratorsPaginator,
    )

    client: ElasticInferenceClient = boto3.client("elastic-inference")

    describe_accelerators_paginator: DescribeAcceleratorsPaginator = client.get_paginator("describe_accelerators")
    ```
"""

from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import DescribeAcceleratorsResponseTypeDef, FilterTypeDef, PaginatorConfigTypeDef

__all__ = ("DescribeAcceleratorsPaginator",)

class DescribeAcceleratorsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/elastic-inference.html#ElasticInference.Paginator.DescribeAccelerators)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/paginators.html#describeacceleratorspaginator)
    """

    def paginate(
        self,
        *,
        acceleratorIds: List[str] = None,
        filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAcceleratorsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.119/reference/services/elastic-inference.html#ElasticInference.Paginator.DescribeAccelerators.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/paginators.html#describeacceleratorspaginator)
        """
