# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import,unused-argument,super-init-not-called
"""
Main interface for ec2-instance-connect service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ec2_instance_connect import EC2InstanceConnectClient

    client: EC2InstanceConnectClient = boto3.client("ec2-instance-connect")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_ec2_instance_connect.type_defs import SendSSHPublicKeyResponseTypeDef

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
    InvalidArgsException: Type[BotocoreClientError]
    ServiceException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class EC2InstanceConnectClient:
    """
    [EC2InstanceConnect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.generate_presigned_url)
        """

    def send_ssh_public_key(
        self, InstanceId: str, InstanceOSUser: str, SSHPublicKey: str, AvailabilityZone: str
    ) -> SendSSHPublicKeyResponseTypeDef:
        """
        [Client.send_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.16.20/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_ssh_public_key)
        """
