"""
Type annotations for amplifyuibuilder service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifyuibuilder/literals.html)

Usage::

    ```python
    from mypy_boto3_amplifyuibuilder.literals import ListComponentsPaginatorName

    data: ListComponentsPaginatorName = "list_components"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListComponentsPaginatorName",
    "ListThemesPaginatorName",
    "SortDirectionType",
    "TokenProvidersType",
)

ListComponentsPaginatorName = Literal["list_components"]
ListThemesPaginatorName = Literal["list_themes"]
SortDirectionType = Literal["ASC", "DESC"]
TokenProvidersType = Literal["figma"]
