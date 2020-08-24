"""
Main interface for ec2-instance-connect service type definitions.

Usage::

    ```python
    from mypy_boto3_ec2_instance_connect.type_defs import SendSSHPublicKeyResponseTypeDef

    data: SendSSHPublicKeyResponseTypeDef = {...}
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("SendSSHPublicKeyResponseTypeDef",)

SendSSHPublicKeyResponseTypeDef = TypedDict(
    "SendSSHPublicKeyResponseTypeDef", {"RequestId": str, "Success": bool}, total=False
)
