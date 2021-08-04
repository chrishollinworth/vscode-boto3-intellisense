"""
Type annotations for identitystore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_identitystore.type_defs import DescribeGroupRequestRequestTypeDef

    data: DescribeGroupRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DescribeGroupRequestRequestTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "FilterTypeDef",
    "GroupTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ResponseMetadataTypeDef",
    "UserTypeDef",
)

DescribeGroupRequestRequestTypeDef = TypedDict(
    "DescribeGroupRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
    },
)

DescribeGroupResponseTypeDef = TypedDict(
    "DescribeGroupResponseTypeDef",
    {
        "GroupId": str,
        "DisplayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserRequestRequestTypeDef = TypedDict(
    "DescribeUserRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "UserId": str,
    },
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef",
    {
        "UserName": str,
        "UserId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "AttributePath": str,
        "AttributeValue": str,
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "GroupId": str,
        "DisplayName": str,
    },
)

_RequiredListGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupsRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
    },
)
_OptionalListGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class ListGroupsRequestRequestTypeDef(
    _RequiredListGroupsRequestRequestTypeDef, _OptionalListGroupsRequestRequestTypeDef
):
    pass

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListUsersRequestRequestTypeDef = TypedDict(
    "_RequiredListUsersRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
    },
)
_OptionalListUsersRequestRequestTypeDef = TypedDict(
    "_OptionalListUsersRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class ListUsersRequestRequestTypeDef(
    _RequiredListUsersRequestRequestTypeDef, _OptionalListUsersRequestRequestTypeDef
):
    pass

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserName": str,
        "UserId": str,
    },
)
