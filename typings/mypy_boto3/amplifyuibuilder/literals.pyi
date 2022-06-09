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
    "ExportThemesPaginatorName",
    "ListComponentsPaginatorName",
    "ListThemesPaginatorName",
    "SortDirectionType",
    "TokenProvidersType",
)

ExportComponentsPaginatorName = Literal["export_components"]
ExportThemesPaginatorName = Literal["export_themes"]
ListComponentsPaginatorName = Literal["list_components"]
ListThemesPaginatorName = Literal["list_themes"]
SortDirectionType = Literal["ASC", "DESC"]
TokenProvidersType = Literal["figma"]
