"""
Type annotations for ivschat service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivschat/literals.html)

Usage::

    ```python
    from mypy_boto3_ivschat.literals import ChatTokenCapabilityType

    data: ChatTokenCapabilityType = "DELETE_MESSAGE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ChatTokenCapabilityType", "FallbackResultType")

ChatTokenCapabilityType = Literal["DELETE_MESSAGE", "DISCONNECT_USER", "SEND_MESSAGE"]
FallbackResultType = Literal["ALLOW", "DENY"]
