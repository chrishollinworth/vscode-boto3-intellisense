"""
Type annotations for appconfigdata service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_appconfigdata import AppConfigDataClient

    client: AppConfigDataClient = boto3.client("appconfigdata")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    GetLatestConfigurationResponseTypeDef,
    StartConfigurationSessionResponseTypeDef,
)

__all__ = ("AppConfigDataClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class AppConfigDataClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appconfigdata.html#AppConfigData.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        AppConfigDataClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appconfigdata.html#AppConfigData.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appconfigdata.html#AppConfigData.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/client.html#close)
        """
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appconfigdata.html#AppConfigData.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/client.html#generate_presigned_url)
        """
    def get_latest_configuration(
        self, *, ConfigurationToken: str
    ) -> GetLatestConfigurationResponseTypeDef:
        """
        Retrieves the latest deployed configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appconfigdata.html#AppConfigData.Client.get_latest_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/client.html#get_latest_configuration)
        """
    def start_configuration_session(
        self,
        *,
        ApplicationIdentifier: str,
        EnvironmentIdentifier: str,
        ConfigurationProfileIdentifier: str,
        RequiredMinimumPollIntervalInSeconds: int = None
    ) -> StartConfigurationSessionResponseTypeDef:
        """
        Starts a configuration session used to retrieve a deployed configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/appconfigdata.html#AppConfigData.Client.start_configuration_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appconfigdata/client.html#start_configuration_session)
        """
