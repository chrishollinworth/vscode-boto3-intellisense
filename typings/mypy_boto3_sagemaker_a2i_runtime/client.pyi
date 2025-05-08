"""
Type annotations for sagemaker-a2i-runtime service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_a2i_runtime.client import AugmentedAIRuntimeClient

    session = Session()
    client: AugmentedAIRuntimeClient = session.client("sagemaker-a2i-runtime")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import ListHumanLoopsPaginator
from .type_defs import (
    DeleteHumanLoopRequestTypeDef,
    DescribeHumanLoopRequestTypeDef,
    DescribeHumanLoopResponseTypeDef,
    ListHumanLoopsRequestTypeDef,
    ListHumanLoopsResponseTypeDef,
    StartHumanLoopRequestTypeDef,
    StartHumanLoopResponseTypeDef,
    StopHumanLoopRequestTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("AugmentedAIRuntimeClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class AugmentedAIRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AugmentedAIRuntimeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#generate_presigned_url)
        """

    def delete_human_loop(self, **kwargs: Unpack[DeleteHumanLoopRequestTypeDef]) -> Dict[str, Any]:
        """
        Deletes the specified human loop for a flow definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/client/delete_human_loop.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#delete_human_loop)
        """

    def describe_human_loop(
        self, **kwargs: Unpack[DescribeHumanLoopRequestTypeDef]
    ) -> DescribeHumanLoopResponseTypeDef:
        """
        Returns information about the specified human loop.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/client/describe_human_loop.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#describe_human_loop)
        """

    def list_human_loops(
        self, **kwargs: Unpack[ListHumanLoopsRequestTypeDef]
    ) -> ListHumanLoopsResponseTypeDef:
        """
        Returns information about human loops, given the specified parameters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/client/list_human_loops.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#list_human_loops)
        """

    def start_human_loop(
        self, **kwargs: Unpack[StartHumanLoopRequestTypeDef]
    ) -> StartHumanLoopResponseTypeDef:
        """
        Starts a human loop, provided that at least one activation condition is met.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/client/start_human_loop.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#start_human_loop)
        """

    def stop_human_loop(self, **kwargs: Unpack[StopHumanLoopRequestTypeDef]) -> Dict[str, Any]:
        """
        Stops the specified human loop.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/client/stop_human_loop.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#stop_human_loop)
        """

    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_human_loops"]
    ) -> ListHumanLoopsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-a2i-runtime/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/client/#get_paginator)
        """
