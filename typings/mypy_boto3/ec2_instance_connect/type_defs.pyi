"""
Type annotations for ec2-instance-connect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ec2_instance_connect.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "SendSSHPublicKeyRequestRequestTypeDef",
    "SendSSHPublicKeyResponseTypeDef",
    "SendSerialConsoleSSHPublicKeyRequestRequestTypeDef",
    "SendSerialConsoleSSHPublicKeyResponseTypeDef",
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SendSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "SendSSHPublicKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InstanceOSUser": str,
        "SSHPublicKey": str,
        "AvailabilityZone": str,
    },
)

SendSSHPublicKeyResponseTypeDef = TypedDict(
    "SendSSHPublicKeyResponseTypeDef",
    {
        "RequestId": str,
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSendSerialConsoleSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "_RequiredSendSerialConsoleSSHPublicKeyRequestRequestTypeDef",
    {
        "InstanceId": str,
        "SSHPublicKey": str,
    },
)
_OptionalSendSerialConsoleSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "_OptionalSendSerialConsoleSSHPublicKeyRequestRequestTypeDef",
    {
        "SerialPort": int,
    },
    total=False,
)

class SendSerialConsoleSSHPublicKeyRequestRequestTypeDef(
    _RequiredSendSerialConsoleSSHPublicKeyRequestRequestTypeDef,
    _OptionalSendSerialConsoleSSHPublicKeyRequestRequestTypeDef,
):
    pass

SendSerialConsoleSSHPublicKeyResponseTypeDef = TypedDict(
    "SendSerialConsoleSSHPublicKeyResponseTypeDef",
    {
        "RequestId": str,
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
