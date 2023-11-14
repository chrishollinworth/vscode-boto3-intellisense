"""
Type annotations for dynamodbstreams service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodbstreams/literals.html)

Usage::

    ```python
    from mypy_boto3_dynamodbstreams.literals import KeyTypeType

    data: KeyTypeType = "HASH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "KeyTypeType",
    "OperationTypeType",
    "ShardIteratorTypeType",
    "StreamStatusType",
    "StreamViewTypeType",
)

KeyTypeType = Literal["HASH", "RANGE"]
OperationTypeType = Literal["INSERT", "MODIFY", "REMOVE"]
ShardIteratorTypeType = Literal[
    "AFTER_SEQUENCE_NUMBER", "AT_SEQUENCE_NUMBER", "LATEST", "TRIM_HORIZON"
]
StreamStatusType = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
StreamViewTypeType = Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
