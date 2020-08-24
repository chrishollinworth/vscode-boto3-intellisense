# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for sagemaker-a2i-runtime service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_a2i_runtime import AugmentedAIRuntimeClient

    client: AugmentedAIRuntimeClient = boto3.client("sagemaker-a2i-runtime")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, Type

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_sagemaker_a2i_runtime.paginator import ListHumanLoopsPaginator
from mypy_boto3_sagemaker_a2i_runtime.type_defs import (
    DescribeHumanLoopResponseTypeDef,
    HumanLoopDataAttributesTypeDef,
    HumanLoopInputTypeDef,
    ListHumanLoopsResponseTypeDef,
    StartHumanLoopResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("AugmentedAIRuntimeClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    InternalServerException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceQuotaExceededException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    ValidationException: Type[Boto3ClientError]


class AugmentedAIRuntimeClient:
    """
    [AugmentedAIRuntime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.can_paginate)
        """

    def delete_human_loop(self, HumanLoopName: str) -> Dict[str, Any]:
        """
        [Client.delete_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.delete_human_loop)
        """

    def describe_human_loop(self, HumanLoopName: str) -> DescribeHumanLoopResponseTypeDef:
        """
        [Client.describe_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.describe_human_loop)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.generate_presigned_url)
        """

    def list_human_loops(
        self,
        FlowDefinitionArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: Literal["Ascending", "Descending"] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListHumanLoopsResponseTypeDef:
        """
        [Client.list_human_loops documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.list_human_loops)
        """

    def start_human_loop(
        self,
        HumanLoopName: str,
        FlowDefinitionArn: str,
        HumanLoopInput: HumanLoopInputTypeDef,
        DataAttributes: HumanLoopDataAttributesTypeDef = None,
    ) -> StartHumanLoopResponseTypeDef:
        """
        [Client.start_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.start_human_loop)
        """

    def stop_human_loop(self, HumanLoopName: str) -> Dict[str, Any]:
        """
        [Client.stop_human_loop documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client.stop_human_loop)
        """

    def get_paginator(self, operation_name: Literal["list_human_loops"]) -> ListHumanLoopsPaginator:
        """
        [Paginator.ListHumanLoops documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops)
        """
