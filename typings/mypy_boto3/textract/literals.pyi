"""
Type annotations for textract service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/literals.html)

Usage::

    ```python
    from mypy_boto3_textract.literals import BlockTypeType

    data: BlockTypeType = "CELL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "BlockTypeType",
    "ContentClassifierType",
    "EntityTypeType",
    "FeatureTypeType",
    "JobStatusType",
    "RelationshipTypeType",
    "SelectionStatusType",
    "TextTypeType",
)

BlockTypeType = Literal[
    "CELL", "KEY_VALUE_SET", "LINE", "PAGE", "SELECTION_ELEMENT", "TABLE", "WORD"
]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
EntityTypeType = Literal["KEY", "VALUE"]
FeatureTypeType = Literal["FORMS", "TABLES"]
JobStatusType = Literal["FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCEEDED"]
RelationshipTypeType = Literal["CHILD", "COMPLEX_FEATURES", "VALUE"]
SelectionStatusType = Literal["NOT_SELECTED", "SELECTED"]
TextTypeType = Literal["HANDWRITING", "PRINTED"]
