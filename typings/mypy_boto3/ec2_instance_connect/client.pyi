"""
Type annotations for ec2-instance-connect service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ec2_instance_connect.client import EC2InstanceConnectClient

    session = Session()
    client: EC2InstanceConnectClient = session.client("ec2-instance-connect")
    ```
"""

from __future__ import annotations

import sys
from typing import Any

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .type_defs import (
    SendSerialConsoleSSHPublicKeyRequestTypeDef,
    SendSerialConsoleSSHPublicKeyResponseTypeDef,
    SendSSHPublicKeyRequestTypeDef,
    SendSSHPublicKeyResponseTypeDef,
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

__all__ = ("EC2InstanceConnectClient",)

class Exceptions(BaseClientExceptions):
    AuthException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    EC2InstanceNotFoundException: Type[BotocoreClientError]
    EC2InstanceStateInvalidException: Type[BotocoreClientError]
    EC2InstanceTypeInvalidException: Type[BotocoreClientError]
    EC2InstanceUnavailableException: Type[BotocoreClientError]
    InvalidArgsException: Type[BotocoreClientError]
    SerialConsoleAccessDisabledException: Type[BotocoreClientError]
    SerialConsoleSessionLimitExceededException: Type[BotocoreClientError]
    SerialConsoleSessionUnavailableException: Type[BotocoreClientError]
    SerialConsoleSessionUnsupportedException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class EC2InstanceConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EC2InstanceConnectClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client/#generate_presigned_url)
        """

    def send_ssh_public_key(
        self, **kwargs: Unpack[SendSSHPublicKeyRequestTypeDef]
    ) -> SendSSHPublicKeyResponseTypeDef:
        """
        Pushes an SSH public key to the specified EC2 instance for use by the specified
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect/client/send_ssh_public_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client/#send_ssh_public_key)
        """

    def send_serial_console_ssh_public_key(
        self, **kwargs: Unpack[SendSerialConsoleSSHPublicKeyRequestTypeDef]
    ) -> SendSerialConsoleSSHPublicKeyResponseTypeDef:
        """
        Pushes an SSH public key to the specified EC2 instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2-instance-connect/client/send_serial_console_ssh_public_key.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client/#send_serial_console_ssh_public_key)
        """
