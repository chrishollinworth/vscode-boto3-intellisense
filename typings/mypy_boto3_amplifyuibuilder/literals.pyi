"""
Type annotations for amplifyuibuilder service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/literals.html)

Usage::

    ```python
    from mypy_boto3_amplifyuibuilder.literals import ExportComponentsPaginatorName

    data: ExportComponentsPaginatorName = "export_components"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ExportComponentsPaginatorName",
    "ExportFormsPaginatorName",
    "ExportThemesPaginatorName",
    "FixedPositionType",
    "FormActionTypeType",
    "FormButtonsPositionType",
    "FormDataSourceTypeType",
    "ListComponentsPaginatorName",
    "ListFormsPaginatorName",
    "ListThemesPaginatorName",
    "SortDirectionType",
    "TokenProvidersType",
)

ExportComponentsPaginatorName = Literal["export_components"]
ExportFormsPaginatorName = Literal["export_forms"]
ExportThemesPaginatorName = Literal["export_themes"]
FixedPositionType = Literal["first"]
FormActionTypeType = Literal["create", "update"]
FormButtonsPositionType = Literal["bottom", "top", "top_and_bottom"]
FormDataSourceTypeType = Literal["Custom", "DataStore"]
ListComponentsPaginatorName = Literal["list_components"]
ListFormsPaginatorName = Literal["list_forms"]
ListThemesPaginatorName = Literal["list_themes"]
SortDirectionType = Literal["ASC", "DESC"]
TokenProvidersType = Literal["figma"]
