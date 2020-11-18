"""
Main interface for identitystore service type definitions.

Usage::

    ```python
    from mypy_boto3_identitystore.type_defs import GroupTypeDef

    data: GroupTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GroupTypeDef",
    "UserTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "FilterTypeDef",
    "ListGroupsResponseTypeDef",
    "ListUsersResponseTypeDef",
)

GroupTypeDef = TypedDict("GroupTypeDef", {"GroupId": str, "DisplayName": str})

UserTypeDef = TypedDict("UserTypeDef", {"UserName": str, "UserId": str})

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef", {"GroupId": str, "DisplayName": str}
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef", {"UserName": str, "UserId": str}
)

FilterTypeDef = TypedDict("FilterTypeDef", {"AttributePath": str, "AttributeValue": str})

_RequiredListGroupsResponseTypeDef = TypedDict(
    "_RequiredListGroupsResponseTypeDef", {"Groups": List["GroupTypeDef"]}
)
_OptionalListGroupsResponseTypeDef = TypedDict(
    "_OptionalListGroupsResponseTypeDef", {"NextToken": str}, total=False
)


class ListGroupsResponseTypeDef(
    _RequiredListGroupsResponseTypeDef, _OptionalListGroupsResponseTypeDef
):
    pass


_RequiredListUsersResponseTypeDef = TypedDict(
    "_RequiredListUsersResponseTypeDef", {"Users": List["UserTypeDef"]}
)
_OptionalListUsersResponseTypeDef = TypedDict(
    "_OptionalListUsersResponseTypeDef", {"NextToken": str}, total=False
)


class ListUsersResponseTypeDef(
    _RequiredListUsersResponseTypeDef, _OptionalListUsersResponseTypeDef
):
    pass
