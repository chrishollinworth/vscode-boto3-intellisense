"""
Type annotations for ec2-instance-connect service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ec2_instance_connect import EC2InstanceConnectClient

    client: EC2InstanceConnectClient = boto3.client("ec2-instance-connect")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import SendSerialConsoleSSHPublicKeyResponseTypeDef, SendSSHPublicKeyResponseTypeDef

__all__ = ("EC2InstanceConnectClient",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
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
    ServiceException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]

class EC2InstanceConnectClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EC2InstanceConnectClient exceptions.
        """
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#can_paginate)
        """
    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#close)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#generate_presigned_url)
        """
    def send_serial_console_ssh_public_key(
        self, *, InstanceId: str, SSHPublicKey: str, SerialPort: int = None
    ) -> SendSerialConsoleSSHPublicKeyResponseTypeDef:
        """
        Pushes an SSH public key to the specified EC2 instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_serial_console_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#send_serial_console_ssh_public_key)
        """
    def send_ssh_public_key(
        self,
        *,
        InstanceId: str,
        InstanceOSUser: str,
        SSHPublicKey: str,
        AvailabilityZone: str = None
    ) -> SendSSHPublicKeyResponseTypeDef:
        """
        Pushes an SSH public key to the specified EC2 instance for use by the specified
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.28.85/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/client.html#send_ssh_public_key)
        """
