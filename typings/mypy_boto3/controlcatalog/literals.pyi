"""
Type annotations for controlcatalog service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_controlcatalog/literals.html)

Usage::

    ```python
    from mypy_boto3_controlcatalog.literals import ListCommonControlsPaginatorName

    data: ListCommonControlsPaginatorName = "list_common_controls"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListCommonControlsPaginatorName",
    "ListDomainsPaginatorName",
    "ListObjectivesPaginatorName",
)

ListCommonControlsPaginatorName = Literal["list_common_controls"]
ListDomainsPaginatorName = Literal["list_domains"]
ListObjectivesPaginatorName = Literal["list_objectives"]
