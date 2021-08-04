"""
Type annotations for codestar service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/literals.html)

Usage::

    ```python
    from mypy_boto3_codestar.literals import ListProjectsPaginatorName

    data: ListProjectsPaginatorName = "list_projects"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListProjectsPaginatorName",
    "ListResourcesPaginatorName",
    "ListTeamMembersPaginatorName",
    "ListUserProfilesPaginatorName",
)

ListProjectsPaginatorName = Literal["list_projects"]
ListResourcesPaginatorName = Literal["list_resources"]
ListTeamMembersPaginatorName = Literal["list_team_members"]
ListUserProfilesPaginatorName = Literal["list_user_profiles"]
