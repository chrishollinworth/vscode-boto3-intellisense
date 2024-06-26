"""
Type annotations for lexv2-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_lexv2_runtime.literals import ConfirmationStateType

    data: ConfirmationStateType = "Confirmed"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConfirmationStateType",
    "DialogActionTypeType",
    "IntentStateType",
    "InterpretationSourceType",
    "MessageContentTypeType",
    "SentimentTypeType",
    "ShapeType",
    "StyleTypeType",
)

ConfirmationStateType = Literal["Confirmed", "Denied", "None"]
DialogActionTypeType = Literal[
    "Close", "ConfirmIntent", "Delegate", "ElicitIntent", "ElicitSlot", "None"
]
IntentStateType = Literal[
    "Failed", "Fulfilled", "FulfillmentInProgress", "InProgress", "ReadyForFulfillment", "Waiting"
]
InterpretationSourceType = Literal["Bedrock", "Lex"]
MessageContentTypeType = Literal["CustomPayload", "ImageResponseCard", "PlainText", "SSML"]
SentimentTypeType = Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]
ShapeType = Literal["Composite", "List", "Scalar"]
StyleTypeType = Literal["Default", "SpellByLetter", "SpellByWord"]
