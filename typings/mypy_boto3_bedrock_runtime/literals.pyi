"""
Type annotations for bedrock-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_bedrock_runtime.literals import ConversationRoleType

    data: ConversationRoleType = "assistant"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ConversationRoleType",
    "ImageFormatType",
    "StopReasonType",
    "ToolResultStatusType",
    "TraceType",
)

ConversationRoleType = Literal["assistant", "user"]
ImageFormatType = Literal["gif", "jpeg", "png", "webp"]
StopReasonType = Literal["content_filtered", "end_turn", "max_tokens", "stop_sequence", "tool_use"]
ToolResultStatusType = Literal["error", "success"]
TraceType = Literal["DISABLED", "ENABLED"]
