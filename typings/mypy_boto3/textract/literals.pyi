"""
Type annotations for textract service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_textract/literals.html)

Usage::

    ```python
    from mypy_boto3_textract.literals import AdapterVersionStatusType

    data: AdapterVersionStatusType = "ACTIVE"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AdapterVersionStatusType",
    "AutoUpdateType",
    "BlockTypeType",
    "ContentClassifierType",
    "EntityTypeType",
    "FeatureTypeType",
    "JobStatusType",
    "ListAdapterVersionsPaginatorName",
    "ListAdaptersPaginatorName",
    "RelationshipTypeType",
    "SelectionStatusType",
    "TextTypeType",
    "ValueTypeType",
)

AdapterVersionStatusType = Literal[
    "ACTIVE", "AT_RISK", "CREATION_ERROR", "CREATION_IN_PROGRESS", "DEPRECATED"
]
AutoUpdateType = Literal["DISABLED", "ENABLED"]
BlockTypeType = Literal[
    "CELL",
    "KEY_VALUE_SET",
    "LAYOUT_FIGURE",
    "LAYOUT_FOOTER",
    "LAYOUT_HEADER",
    "LAYOUT_KEY_VALUE",
    "LAYOUT_LIST",
    "LAYOUT_PAGE_NUMBER",
    "LAYOUT_SECTION_HEADER",
    "LAYOUT_TABLE",
    "LAYOUT_TEXT",
    "LAYOUT_TITLE",
    "LINE",
    "MERGED_CELL",
    "PAGE",
    "QUERY",
    "QUERY_RESULT",
    "SELECTION_ELEMENT",
    "SIGNATURE",
    "TABLE",
    "TABLE_FOOTER",
    "TABLE_TITLE",
    "TITLE",
    "WORD",
]
ContentClassifierType = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
EntityTypeType = Literal[
    "COLUMN_HEADER",
    "KEY",
    "SEMI_STRUCTURED_TABLE",
    "STRUCTURED_TABLE",
    "TABLE_FOOTER",
    "TABLE_SECTION_TITLE",
    "TABLE_SUMMARY",
    "TABLE_TITLE",
    "VALUE",
]
FeatureTypeType = Literal["FORMS", "LAYOUT", "QUERIES", "SIGNATURES", "TABLES"]
JobStatusType = Literal["FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCEEDED"]
ListAdapterVersionsPaginatorName = Literal["list_adapter_versions"]
ListAdaptersPaginatorName = Literal["list_adapters"]
RelationshipTypeType = Literal[
    "ANSWER",
    "CHILD",
    "COMPLEX_FEATURES",
    "MERGED_CELL",
    "TABLE",
    "TABLE_FOOTER",
    "TABLE_TITLE",
    "TITLE",
    "VALUE",
]
SelectionStatusType = Literal["NOT_SELECTED", "SELECTED"]
TextTypeType = Literal["HANDWRITING", "PRINTED"]
ValueTypeType = Literal["DATE"]
