"""
Type annotations for ec2-instance-connect service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2_instance_connect/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ec2_instance_connect.type_defs import ResponseMetadataTypeDef

    data: ResponseMetadataTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
else:
    from typing import Dict
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ResponseMetadataTypeDef",
    "SendSSHPublicKeyRequestTypeDef",
    "SendSSHPublicKeyResponseTypeDef",
    "SendSerialConsoleSSHPublicKeyRequestTypeDef",
    "SendSerialConsoleSSHPublicKeyResponseTypeDef",
)

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SendSSHPublicKeyRequestTypeDef(TypedDict):
    InstanceId: str
    InstanceOSUser: str
    SSHPublicKey: str
    AvailabilityZone: NotRequired[str]

class SendSerialConsoleSSHPublicKeyRequestTypeDef(TypedDict):
    InstanceId: str
    SSHPublicKey: str
    SerialPort: NotRequired[int]

class SendSSHPublicKeyResponseTypeDef(TypedDict):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SendSerialConsoleSSHPublicKeyResponseTypeDef(TypedDict):
    RequestId: str
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef
