"""
Main interface for workmailmessageflow service type definitions.

Usage::

    ```python
    from mypy_boto3_workmailmessageflow.type_defs import GetRawMessageContentResponseTypeDef

    data: GetRawMessageContentResponseTypeDef = {...}
    ```
"""
import sys
from typing import IO

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("GetRawMessageContentResponseTypeDef",)

GetRawMessageContentResponseTypeDef = TypedDict(
    "GetRawMessageContentResponseTypeDef", {"messageContent": IO[bytes]}
)
