"""
Type annotations for amp service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amp/literals.html)

Usage::

    ```python
    from mypy_boto3_amp.literals import ListWorkspacesPaginatorName

    data: ListWorkspacesPaginatorName = "list_workspaces"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("ListWorkspacesPaginatorName", "WorkspaceStatusCodeType")

ListWorkspacesPaginatorName = Literal["list_workspaces"]
WorkspaceStatusCodeType = Literal["ACTIVE", "CREATING", "CREATION_FAILED", "DELETING", "UPDATING"]
