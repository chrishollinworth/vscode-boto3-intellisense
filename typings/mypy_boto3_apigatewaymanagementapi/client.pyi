"""
Type annotations for apigatewaymanagementapi service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_apigatewaymanagementapi.client import ApiGatewayManagementApiClient

    session = Session()
    client: ApiGatewayManagementApiClient = session.client("apigatewaymanagementapi")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    DeleteConnectionRequestTypeDef,
    EmptyResponseMetadataTypeDef,
    GetConnectionRequestTypeDef,
    GetConnectionResponseTypeDef,
    PostToConnectionRequestTypeDef,
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

__all__ = ("ApiGatewayManagementApiClient",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GoneException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PayloadTooLargeException: Type[BotocoreClientError]

class ApiGatewayManagementApiClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        ApiGatewayManagementApiClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi.html#ApiGatewayManagementApi.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client/#generate_presigned_url)
        """

    def delete_connection(
        self, **kwargs: Unpack[DeleteConnectionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the connection with the provided id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi/client/delete_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client/#delete_connection)
        """

    def get_connection(
        self, **kwargs: Unpack[GetConnectionRequestTypeDef]
    ) -> GetConnectionResponseTypeDef:
        """
        Get information about the connection with the provided id.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi/client/get_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client/#get_connection)
        """

    def post_to_connection(
        self, **kwargs: Unpack[PostToConnectionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sends the provided data to the specified connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/apigatewaymanagementapi/client/post_to_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigatewaymanagementapi/client/#post_to_connection)
        """
