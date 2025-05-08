"""
Type annotations for sagemaker-metrics service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_metrics.client import SageMakerMetricsClient

    session = Session()
    client: SageMakerMetricsClient = session.client("sagemaker-metrics")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    BatchGetMetricsRequestTypeDef,
    BatchGetMetricsResponseTypeDef,
    BatchPutMetricsRequestTypeDef,
    BatchPutMetricsResponseTypeDef,
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

__all__ = ("SageMakerMetricsClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]

class SageMakerMetricsClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SageMakerMetricsClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics.html#SageMakerMetrics.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/client/#generate_presigned_url)
        """

    def batch_get_metrics(
        self, **kwargs: Unpack[BatchGetMetricsRequestTypeDef]
    ) -> BatchGetMetricsResponseTypeDef:
        """
        Used to retrieve training metrics from SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics/client/batch_get_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/client/#batch_get_metrics)
        """

    def batch_put_metrics(
        self, **kwargs: Unpack[BatchPutMetricsRequestTypeDef]
    ) -> BatchPutMetricsResponseTypeDef:
        """
        Used to ingest training metrics into SageMaker.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-metrics/client/batch_put_metrics.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_metrics/client/#batch_put_metrics)
        """
