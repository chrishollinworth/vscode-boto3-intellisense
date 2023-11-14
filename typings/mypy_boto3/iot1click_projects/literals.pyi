"""
Type annotations for iot1click-projects service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/literals.html)

Usage::

    ```python
    from mypy_boto3_iot1click_projects.literals import ListPlacementsPaginatorName

    data: ListPlacementsPaginatorName = "list_placements"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListPlacementsPaginatorName", "ListProjectsPaginatorName")

ListPlacementsPaginatorName = Literal["list_placements"]
ListProjectsPaginatorName = Literal["list_projects"]
