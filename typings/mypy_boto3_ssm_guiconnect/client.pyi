"""
Type annotations for ssm-guiconnect service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ssm_guiconnect.client import SSMGUIConnectClient

    session = Session()
    client: SSMGUIConnectClient = session.client("ssm-guiconnect")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    DeleteConnectionRecordingPreferencesRequestTypeDef,
    DeleteConnectionRecordingPreferencesResponseTypeDef,
    GetConnectionRecordingPreferencesResponseTypeDef,
    UpdateConnectionRecordingPreferencesRequestTypeDef,
    UpdateConnectionRecordingPreferencesResponseTypeDef,
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

__all__ = ("SSMGUIConnectClient",)

class Exceptions(BaseClientExceptions):
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]

class SSMGUIConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-guiconnect.html#SSMGUIConnect.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SSMGUIConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-guiconnect.html#SSMGUIConnect.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-guiconnect/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-guiconnect/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/client/#generate_presigned_url)
        """

    def delete_connection_recording_preferences(
        self, **kwargs: Unpack[DeleteConnectionRecordingPreferencesRequestTypeDef]
    ) -> DeleteConnectionRecordingPreferencesResponseTypeDef:
        """
        Deletes the preferences for recording RDP connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-guiconnect/client/delete_connection_recording_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/client/#delete_connection_recording_preferences)
        """

    def get_connection_recording_preferences(
        self,
    ) -> GetConnectionRecordingPreferencesResponseTypeDef:
        """
        Returns the preferences specified for recording RDP connections in the
        requesting Amazon Web Services account and Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-guiconnect/client/get_connection_recording_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/client/#get_connection_recording_preferences)
        """

    def update_connection_recording_preferences(
        self, **kwargs: Unpack[UpdateConnectionRecordingPreferencesRequestTypeDef]
    ) -> UpdateConnectionRecordingPreferencesResponseTypeDef:
        """
        Updates the preferences for recording RDP connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm-guiconnect/client/update_connection_recording_preferences.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ssm_guiconnect/client/#update_connection_recording_preferences)
        """
