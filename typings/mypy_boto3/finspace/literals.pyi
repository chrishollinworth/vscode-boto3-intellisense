"""
Type annotations for finspace service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace/literals.html)

Usage::

    ```python
    from mypy_boto3_finspace.literals import EnvironmentStatusType

    data: EnvironmentStatusType = "CREATE_REQUESTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EnvironmentStatusType", "FederationModeType")

EnvironmentStatusType = Literal[
    "CREATED",
    "CREATE_REQUESTED",
    "CREATING",
    "DELETED",
    "DELETE_REQUESTED",
    "DELETING",
    "FAILED_CREATION",
    "FAILED_DELETION",
    "RETRY_DELETION",
    "SUSPENDED",
]
FederationModeType = Literal["FEDERATED", "LOCAL"]
