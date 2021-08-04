"""
Type annotations for sdb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/literals.html)

Usage::

    ```python
    from mypy_boto3_sdb.literals import ListDomainsPaginatorName

    data: ListDomainsPaginatorName = "list_domains"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListDomainsPaginatorName", "SelectPaginatorName")

ListDomainsPaginatorName = Literal["list_domains"]
SelectPaginatorName = Literal["select"]
