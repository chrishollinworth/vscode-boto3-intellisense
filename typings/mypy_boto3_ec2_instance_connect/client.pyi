# pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin,too-many-locals,unused-import
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

from botocore.exceptions import ClientError as Boto3ClientError

from mypy_boto3_ec2_instance_connect.type_defs import SendSSHPublicKeyResponseTypeDef

__all__ = ("EC2InstanceConnectClient",)


class Exceptions:
    AuthException: Type[Boto3ClientError]
    ClientError: Type[Boto3ClientError]
    EC2InstanceNotFoundException: Type[Boto3ClientError]
    InvalidArgsException: Type[Boto3ClientError]
    ServiceException: Type[Boto3ClientError]
    ThrottlingException: Type[Boto3ClientError]


class EC2InstanceConnectClient:
    """
    [EC2InstanceConnect.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client)
    """

    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.generate_presigned_url)
        """

    def send_ssh_public_key(
        self, InstanceId: str, InstanceOSUser: str, SSHPublicKey: str, AvailabilityZone: str
    ) -> SendSSHPublicKeyResponseTypeDef:
        """
        [Client.send_ssh_public_key documentation](https://boto3.amazonaws.com/v1/documentation/api/1.14.47/reference/services/ec2-instance-connect.html#EC2InstanceConnect.Client.send_ssh_public_key)
        """
