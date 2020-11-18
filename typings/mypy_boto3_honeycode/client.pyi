# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for honeycode service client

Usage::

    ```python
    import boto3
    from mypy_boto3_honeycode import HoneycodeClient

    client: HoneycodeClient = boto3.client("honeycode")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_honeycode.type_defs import (
    GetScreenDataResultTypeDef,
    InvokeScreenAutomationResultTypeDef,
    VariableValueTypeDef,
)

__all__ = ("HoneycodeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AutomationExecutionException: Type[BotocoreClientError]
    AutomationExecutionTimeoutException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    RequestTimeoutException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class HoneycodeClient:
    """
    [Honeycode.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/honeycode.html#Honeycode.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/honeycode.html#Honeycode.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/honeycode.html#Honeycode.Client.generate_presigned_url)
        """

    def get_screen_data(
        self,
        workbookId: str,
        appId: str,
        screenId: str,
        variables: Dict[str, VariableValueTypeDef] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> GetScreenDataResultTypeDef:
        """
        [Client.get_screen_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/honeycode.html#Honeycode.Client.get_screen_data)
        """

    def invoke_screen_automation(
        self,
        workbookId: str,
        appId: str,
        screenId: str,
        screenAutomationId: str,
        variables: Dict[str, VariableValueTypeDef] = None,
        rowId: str = None,
        clientRequestToken: str = None,
    ) -> InvokeScreenAutomationResultTypeDef:
        """
        [Client.invoke_screen_automation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/honeycode.html#Honeycode.Client.invoke_screen_automation)
        """
