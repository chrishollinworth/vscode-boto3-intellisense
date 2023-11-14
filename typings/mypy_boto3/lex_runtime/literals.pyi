"""
Type annotations for lex-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_lex_runtime.literals import ConfirmationStatusType

    data: ConfirmationStatusType = "Confirmed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConfirmationStatusType",
    "ContentTypeType",
    "DialogActionTypeType",
    "DialogStateType",
    "FulfillmentStateType",
    "MessageFormatTypeType",
)

ConfirmationStatusType = Literal["Confirmed", "Denied", "None"]
ContentTypeType = Literal["application/vnd.amazonaws.card.generic"]
DialogActionTypeType = Literal["Close", "ConfirmIntent", "Delegate", "ElicitIntent", "ElicitSlot"]
DialogStateType = Literal[
    "ConfirmIntent", "ElicitIntent", "ElicitSlot", "Failed", "Fulfilled", "ReadyForFulfillment"
]
FulfillmentStateType = Literal["Failed", "Fulfilled", "ReadyForFulfillment"]
MessageFormatTypeType = Literal["Composite", "CustomPayload", "PlainText", "SSML"]
