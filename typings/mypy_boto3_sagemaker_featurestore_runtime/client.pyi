"""
Main interface for sagemaker-featurestore-runtime service client

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_featurestore_runtime import SagemakerFeatureStoreRuntimeClient

    client: SagemakerFeatureStoreRuntimeClient = boto3.client("sagemaker-featurestore-runtime")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_sagemaker_featurestore_runtime.type_defs import (
    FeatureValueTypeDef,
    GetRecordResponseTypeDef,
)

__all__ = ("SagemakerFeatureStoreRuntimeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessForbidden: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalFailure: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ServiceUnavailable: Type[BotocoreClientError]
    ValidationError: Type[BotocoreClientError]


class SagemakerFeatureStoreRuntimeClient:
    """
    [SagemakerFeatureStoreRuntime.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.can_paginate)
        """

    def delete_record(
        self, FeatureGroupName: str, RecordIdentifierValueAsString: str, EventTime: str
    ) -> None:
        """
        [Client.delete_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.delete_record)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.generate_presigned_url)
        """

    def get_record(
        self,
        FeatureGroupName: str,
        RecordIdentifierValueAsString: str,
        FeatureNames: List[str] = None,
    ) -> GetRecordResponseTypeDef:
        """
        [Client.get_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.get_record)
        """

    def put_record(self, FeatureGroupName: str, Record: List["FeatureValueTypeDef"]) -> None:
        """
        [Client.put_record documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.5/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.put_record)
        """
