"""
Type annotations for memorydb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_memorydb/literals.html)

Usage::

    ```python
    from mypy_boto3_memorydb.literals import AZStatusType

    data: AZStatusType = "multiaz"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AZStatusType",
    "AuthenticationTypeType",
    "InputAuthenticationTypeType",
    "ServiceUpdateStatusType",
    "ServiceUpdateTypeType",
    "SourceTypeType",
)

AZStatusType = Literal["multiaz", "singleaz"]
AuthenticationTypeType = Literal["no-password", "password"]
InputAuthenticationTypeType = Literal["password"]
ServiceUpdateStatusType = Literal["available", "complete", "in-progress", "scheduled"]
ServiceUpdateTypeType = Literal["security-update"]
SourceTypeType = Literal["acl", "cluster", "node", "parameter-group", "subnet-group", "user"]
