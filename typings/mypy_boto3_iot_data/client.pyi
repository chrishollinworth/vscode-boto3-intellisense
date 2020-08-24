# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
"""
Main interface for iot-data service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iot_data import IoTDataPlaneClient

    client: IoTDataPlaneClient = boto3.client("iot-data")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_iot_data.type_defs import (
    DeleteThingShadowResponseTypeDef,
    GetThingShadowResponseTypeDef,
    ListNamedShadowsForThingResponseTypeDef,
    UpdateThingShadowResponseTypeDef,
)

__all__ = ("IoTDataPlaneClient",)


class Exceptions:
    ClientError: Type[Boto3ClientError]
    ConflictException: Type[Boto3ClientError]
    InternalFailureException: Type[Boto3ClientError]
    InvalidRequestException: Type[Boto3ClientError]
    MethodNotAllowedException: Type[Boto3ClientError]
    RequestEntityTooLargeException: Type[Boto3ClientError]
    ResourceNotFoundException: Type[Boto3ClientError]
    ServiceUnavailableException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]
    UnauthorizedException: Type[Boto3ClientError]
    UnsupportedDocumentEncodingException: Type[Boto3ClientError]


class IoTDataPlaneClient:
    """
    [IoTDataPlane.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot-data.html#IoTDataPlane.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot-data.html#IoTDataPlane.Client.can_paginate)
        """

    def delete_thing_shadow(
        self, thingName: str, shadowName: str = None
    ) -> DeleteThingShadowResponseTypeDef:
        """
        [Client.delete_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot-data.html#IoTDataPlane.Client.delete_thing_shadow)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot-data.html#IoTDataPlane.Client.generate_presigned_url)
        """

    def get_thing_shadow(
        self, thingName: str, shadowName: str = None
    ) -> GetThingShadowResponseTypeDef:
        """
        [Client.get_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot-data.html#IoTDataPlane.Client.get_thing_shadow)
        """

    def list_named_shadows_for_thing(
        self, thingName: str, nextToken: str = None, pageSize: int = None
    ) -> ListNamedShadowsForThingResponseTypeDef:
        """
        [Client.list_named_shadows_for_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot-data.html#IoTDataPlane.Client.list_named_shadows_for_thing)
        """

    def publish(self, topic: str, qos: int = None, payload: Union[bytes, IO[bytes]] = None) -> None:
        """
        [Client.publish documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot-data.html#IoTDataPlane.Client.publish)
        """

    def update_thing_shadow(
        self, thingName: str, payload: Union[bytes, IO[bytes]], shadowName: str = None
    ) -> UpdateThingShadowResponseTypeDef:
        """
        [Client.update_thing_shadow documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/iot-data.html#IoTDataPlane.Client.update_thing_shadow)
        """
