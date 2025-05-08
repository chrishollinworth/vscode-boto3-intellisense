"""
Type annotations for sagemaker-featurestore-runtime service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sagemaker_featurestore_runtime.client import SageMakerFeatureStoreRuntimeClient

    session = Session()
    client: SageMakerFeatureStoreRuntimeClient = session.client("sagemaker-featurestore-runtime")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    BatchGetRecordRequestTypeDef,
    BatchGetRecordResponseTypeDef,
    DeleteRecordRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetRecordRequestTypeDef,
    GetRecordResponseTypeDef,
    PutRecordRequestTypeDef,
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

__all__ = ("SageMakerFeatureStoreRuntimeClient",)

class Exceptions(BaseClientExceptions):
    AccessForbidden: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalFailure: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ServiceUnavailable: Type[BotocoreClientError]
    ValidationError: Type[BotocoreClientError]

class SageMakerFeatureStoreRuntimeClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime.html#SageMakerFeatureStoreRuntime.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SageMakerFeatureStoreRuntimeClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime.html#SageMakerFeatureStoreRuntime.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/#generate_presigned_url)
        """

    def batch_get_record(
        self, **kwargs: Unpack[BatchGetRecordRequestTypeDef]
    ) -> BatchGetRecordResponseTypeDef:
        """
        Retrieves a batch of <code>Records</code> from a <code>FeatureGroup</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/batch_get_record.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/#batch_get_record)
        """

    def delete_record(
        self, **kwargs: Unpack[DeleteRecordRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a <code>Record</code> from a <code>FeatureGroup</code> in the
        <code>OnlineStore</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/delete_record.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/#delete_record)
        """

    def get_record(self, **kwargs: Unpack[GetRecordRequestTypeDef]) -> GetRecordResponseTypeDef:
        """
        Use for <code>OnlineStore</code> serving from a <code>FeatureStore</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/get_record.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/#get_record)
        """

    def put_record(self, **kwargs: Unpack[PutRecordRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        The <code>PutRecord</code> API is used to ingest a list of <code>Records</code>
        into your feature group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/put_record.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client/#put_record)
        """
