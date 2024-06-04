"""
Type annotations for identitystore service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/literals.html)

Usage::

    ```python
    from mypy_boto3_identitystore.literals import ListGroupMembershipsForMemberPaginatorName

    data: ListGroupMembershipsForMemberPaginatorName = "list_group_memberships_for_member"
    ```
"""

import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "ListGroupMembershipsForMemberPaginatorName",
    "ListGroupMembershipsPaginatorName",
    "ListGroupsPaginatorName",
    "ListUsersPaginatorName",
)

ListGroupMembershipsForMemberPaginatorName = Literal["list_group_memberships_for_member"]
ListGroupMembershipsPaginatorName = Literal["list_group_memberships"]
ListGroupsPaginatorName = Literal["list_groups"]
ListUsersPaginatorName = Literal["list_users"]
