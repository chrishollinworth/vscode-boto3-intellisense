"""
Type annotations for connectcases service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectcases/literals.html)

Usage::

    ```python
    from mypy_boto3_connectcases.literals import CommentBodyTextTypeType

    data: CommentBodyTextTypeType = "Text/Plain"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "CommentBodyTextTypeType",
    "DomainStatusType",
    "FieldNamespaceType",
    "FieldTypeType",
    "OrderType",
    "RelatedItemTypeType",
    "SearchCasesPaginatorName",
    "SearchRelatedItemsPaginatorName",
    "TemplateStatusType",
)

CommentBodyTextTypeType = Literal["Text/Plain"]
DomainStatusType = Literal["Active", "CreationFailed", "CreationInProgress"]
FieldNamespaceType = Literal["Custom", "System"]
FieldTypeType = Literal["Boolean", "DateTime", "Number", "SingleSelect", "Text", "Url"]
OrderType = Literal["Asc", "Desc"]
RelatedItemTypeType = Literal["Comment", "Contact"]
SearchCasesPaginatorName = Literal["search_cases"]
SearchRelatedItemsPaginatorName = Literal["search_related_items"]
TemplateStatusType = Literal["Active", "Inactive"]
