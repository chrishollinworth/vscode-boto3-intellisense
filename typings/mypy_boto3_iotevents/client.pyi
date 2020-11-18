# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for iotevents service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotevents import IoTEventsClient

    client: IoTEventsClient = boto3.client("iotevents")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_iotevents.type_defs import (
    CreateDetectorModelResponseTypeDef,
    CreateInputResponseTypeDef,
    DescribeDetectorModelResponseTypeDef,
    DescribeInputResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DetectorModelDefinitionTypeDef,
    InputDefinitionTypeDef,
    ListDetectorModelsResponseTypeDef,
    ListDetectorModelVersionsResponseTypeDef,
    ListInputsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingOptionsTypeDef,
    TagTypeDef,
    UpdateDetectorModelResponseTypeDef,
    UpdateInputResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTEventsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class IoTEventsClient:
    """
    [IoTEvents.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.can_paginate)
        """

    def create_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: "DetectorModelDefinitionTypeDef",
        roleArn: str,
        detectorModelDescription: str = None,
        key: str = None,
        tags: List["TagTypeDef"] = None,
        evaluationMethod: Literal["BATCH", "SERIAL"] = None,
    ) -> CreateDetectorModelResponseTypeDef:
        """
        [Client.create_detector_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.create_detector_model)
        """

    def create_input(
        self,
        inputName: str,
        inputDefinition: "InputDefinitionTypeDef",
        inputDescription: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateInputResponseTypeDef:
        """
        [Client.create_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.create_input)
        """

    def delete_detector_model(self, detectorModelName: str) -> Dict[str, Any]:
        """
        [Client.delete_detector_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.delete_detector_model)
        """

    def delete_input(self, inputName: str) -> Dict[str, Any]:
        """
        [Client.delete_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.delete_input)
        """

    def describe_detector_model(
        self, detectorModelName: str, detectorModelVersion: str = None
    ) -> DescribeDetectorModelResponseTypeDef:
        """
        [Client.describe_detector_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.describe_detector_model)
        """

    def describe_input(self, inputName: str) -> DescribeInputResponseTypeDef:
        """
        [Client.describe_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.describe_input)
        """

    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        [Client.describe_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.describe_logging_options)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.generate_presigned_url)
        """

    def list_detector_model_versions(
        self, detectorModelName: str, nextToken: str = None, maxResults: int = None
    ) -> ListDetectorModelVersionsResponseTypeDef:
        """
        [Client.list_detector_model_versions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.list_detector_model_versions)
        """

    def list_detector_models(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDetectorModelsResponseTypeDef:
        """
        [Client.list_detector_models documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.list_detector_models)
        """

    def list_inputs(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListInputsResponseTypeDef:
        """
        [Client.list_inputs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.list_inputs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.list_tags_for_resource)
        """

    def put_logging_options(self, loggingOptions: "LoggingOptionsTypeDef") -> None:
        """
        [Client.put_logging_options documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.put_logging_options)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.untag_resource)
        """

    def update_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: "DetectorModelDefinitionTypeDef",
        roleArn: str,
        detectorModelDescription: str = None,
        evaluationMethod: Literal["BATCH", "SERIAL"] = None,
    ) -> UpdateDetectorModelResponseTypeDef:
        """
        [Client.update_detector_model documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.update_detector_model)
        """

    def update_input(
        self,
        inputName: str,
        inputDefinition: "InputDefinitionTypeDef",
        inputDescription: str = None,
    ) -> UpdateInputResponseTypeDef:
        """
        [Client.update_input documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/iotevents.html#IoTEvents.Client.update_input)
        """
