"""
Type annotations for sso service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/literals.html)

Usage::

    ```python
    from mypy_boto3_sso.literals import ListAccountRolesPaginatorName

    data: ListAccountRolesPaginatorName = "list_account_roles"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListAccountRolesPaginatorName", "ListAccountsPaginatorName")

ListAccountRolesPaginatorName = Literal["list_account_roles"]
ListAccountsPaginatorName = Literal["list_accounts"]
