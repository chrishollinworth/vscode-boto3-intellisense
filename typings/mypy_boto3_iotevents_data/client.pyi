# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for iotevents-data service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotevents_data import IoTEventsDataClient

    client: IoTEventsDataClient = boto3.client("iotevents-data")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_iotevents_data.type_defs import (
    BatchPutMessageResponseTypeDef,
    BatchUpdateDetectorResponseTypeDef,
    DescribeDetectorResponseTypeDef,
    ListDetectorsResponseTypeDef,
    MessageTypeDef,
    UpdateDetectorRequestTypeDef,
)

__all__ = ("IoTEventsDataClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class IoTEventsDataClient:
    """
    [IoTEventsData.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents-data.html#IoTEventsData.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_put_message(self, messages: List[MessageTypeDef]) -> BatchPutMessageResponseTypeDef:
        """
        [Client.batch_put_message documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents-data.html#IoTEventsData.Client.batch_put_message)
        """

    def batch_update_detector(
        self, detectors: List[UpdateDetectorRequestTypeDef]
    ) -> BatchUpdateDetectorResponseTypeDef:
        """
        [Client.batch_update_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents-data.html#IoTEventsData.Client.batch_update_detector)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents-data.html#IoTEventsData.Client.can_paginate)
        """

    def describe_detector(
        self, detectorModelName: str, keyValue: str = None
    ) -> DescribeDetectorResponseTypeDef:
        """
        [Client.describe_detector documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents-data.html#IoTEventsData.Client.describe_detector)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents-data.html#IoTEventsData.Client.generate_presigned_url)
        """

    def list_detectors(
        self,
        detectorModelName: str,
        stateName: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListDetectorsResponseTypeDef:
        """
        [Client.list_detectors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents-data.html#IoTEventsData.Client.list_detectors)
        """
