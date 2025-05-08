"""
Type annotations for sagemaker-runtime service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_runtime.client import SageMakerRuntimeClient

    session = Session()
    client: SageMakerRuntimeClient = session.client("sagemaker-runtime")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    InvokeEndpointAsyncInputTypeDef,
    InvokeEndpointAsyncOutputTypeDef,
    InvokeEndpointInputTypeDef,
    InvokeEndpointOutputTypeDef,
    InvokeEndpointWithResponseStreamInputTypeDef,
    InvokeEndpointWithResponseStreamOutputTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = ("SageMakerRuntimeClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    InternalDependencyException: Type[BotocoreClientError]
    InternalFailure: Type[BotocoreClientError]
    InternalStreamFailure: Type[BotocoreClientError]
    ModelError: Type[BotocoreClientError]
    ModelNotReadyException: Type[BotocoreClientError]
    ModelStreamError: Type[BotocoreClientError]
    ServiceUnavailable: Type[BotocoreClientError]
    ValidationError: Type[BotocoreClientError]

class SageMakerRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SageMakerRuntimeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime.html#SageMakerRuntime.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client/#generate_presigned_url)
        """

    def invoke_endpoint(
        self, **kwargs: Unpack[InvokeEndpointInputTypeDef]
    ) -> InvokeEndpointOutputTypeDef:
        """
        After you deploy a model into production using Amazon SageMaker hosting
        services, your client applications use this API to get inferences from the
        model hosted at the specified endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/invoke_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client/#invoke_endpoint)
        """

    def invoke_endpoint_async(
        self, **kwargs: Unpack[InvokeEndpointAsyncInputTypeDef]
    ) -> InvokeEndpointAsyncOutputTypeDef:
        """
        After you deploy a model into production using Amazon SageMaker hosting
        services, your client applications use this API to get inferences from the
        model hosted at the specified endpoint in an asynchronous manner.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/invoke_endpoint_async.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client/#invoke_endpoint_async)
        """

    def invoke_endpoint_with_response_stream(
        self, **kwargs: Unpack[InvokeEndpointWithResponseStreamInputTypeDef]
    ) -> InvokeEndpointWithResponseStreamOutputTypeDef:
        """
        Invokes a model at the specified endpoint to return the inference response as a
        stream.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-runtime/client/invoke_endpoint_with_response_stream.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_runtime/client/#invoke_endpoint_with_response_stream)
        """
