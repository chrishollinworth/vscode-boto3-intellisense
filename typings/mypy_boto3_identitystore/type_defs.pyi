"""
Type annotations for identitystore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_identitystore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_identitystore.type_defs import AddressTypeDef

    data: AddressTypeDef = {...}
    ```
"""

import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AddressTypeDef",
    "AlternateIdentifierTypeDef",
    "AttributeOperationTypeDef",
    "CreateGroupMembershipRequestRequestTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteGroupMembershipRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeGroupMembershipRequestRequestTypeDef",
    "DescribeGroupMembershipResponseTypeDef",
    "DescribeGroupRequestRequestTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeUserRequestRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "EmailTypeDef",
    "ExternalIdTypeDef",
    "FilterTypeDef",
    "GetGroupIdRequestRequestTypeDef",
    "GetGroupIdResponseTypeDef",
    "GetGroupMembershipIdRequestRequestTypeDef",
    "GetGroupMembershipIdResponseTypeDef",
    "GetUserIdRequestRequestTypeDef",
    "GetUserIdResponseTypeDef",
    "GroupMembershipExistenceResultTypeDef",
    "GroupMembershipTypeDef",
    "GroupTypeDef",
    "IsMemberInGroupsRequestRequestTypeDef",
    "IsMemberInGroupsResponseTypeDef",
    "ListGroupMembershipsForMemberRequestRequestTypeDef",
    "ListGroupMembershipsForMemberResponseTypeDef",
    "ListGroupMembershipsRequestRequestTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MemberIdTypeDef",
    "NameTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberTypeDef",
    "ResponseMetadataTypeDef",
    "UniqueAttributeTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UserTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "StreetAddress": str,
        "Locality": str,
        "Region": str,
        "PostalCode": str,
        "Country": str,
        "Formatted": str,
        "Type": str,
        "Primary": bool,
    },
    total=False,
)

AlternateIdentifierTypeDef = TypedDict(
    "AlternateIdentifierTypeDef",
    {
        "ExternalId": "ExternalIdTypeDef",
        "UniqueAttribute": "UniqueAttributeTypeDef",
    },
    total=False,
)

_RequiredAttributeOperationTypeDef = TypedDict(
    "_RequiredAttributeOperationTypeDef",
    {
        "AttributePath": str,
    },
)
_OptionalAttributeOperationTypeDef = TypedDict(
    "_OptionalAttributeOperationTypeDef",
    {
        "AttributeValue": Dict[str, Any],
    },
    total=False,
)

class AttributeOperationTypeDef(
    _RequiredAttributeOperationTypeDef, _OptionalAttributeOperationTypeDef
):
    pass

CreateGroupMembershipRequestRequestTypeDef = TypedDict(
    "CreateGroupMembershipRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
        "MemberId": "MemberIdTypeDef",
    },
)

CreateGroupMembershipResponseTypeDef = TypedDict(
    "CreateGroupMembershipResponseTypeDef",
    {
        "MembershipId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateGroupRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
    },
)
_OptionalCreateGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateGroupRequestRequestTypeDef",
    {
        "DisplayName": str,
        "Description": str,
    },
    total=False,
)

class CreateGroupRequestRequestTypeDef(
    _RequiredCreateGroupRequestRequestTypeDef, _OptionalCreateGroupRequestRequestTypeDef
):
    pass

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "GroupId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateUserRequestRequestTypeDef = TypedDict(
    "_RequiredCreateUserRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
    },
)
_OptionalCreateUserRequestRequestTypeDef = TypedDict(
    "_OptionalCreateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "Name": "NameTypeDef",
        "DisplayName": str,
        "NickName": str,
        "ProfileUrl": str,
        "Emails": List["EmailTypeDef"],
        "Addresses": List["AddressTypeDef"],
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "UserType": str,
        "Title": str,
        "PreferredLanguage": str,
        "Locale": str,
        "Timezone": str,
    },
    total=False,
)

class CreateUserRequestRequestTypeDef(
    _RequiredCreateUserRequestRequestTypeDef, _OptionalCreateUserRequestRequestTypeDef
):
    pass

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupMembershipRequestRequestTypeDef = TypedDict(
    "DeleteGroupMembershipRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MembershipId": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "UserId": str,
    },
)

DescribeGroupMembershipRequestRequestTypeDef = TypedDict(
    "DescribeGroupMembershipRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MembershipId": str,
    },
)

DescribeGroupMembershipResponseTypeDef = TypedDict(
    "DescribeGroupMembershipResponseTypeDef",
    {
        "IdentityStoreId": str,
        "MembershipId": str,
        "GroupId": str,
        "MemberId": "MemberIdTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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
        "ExternalIds": List["ExternalIdTypeDef"],
        "Description": str,
        "IdentityStoreId": str,
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
        "ExternalIds": List["ExternalIdTypeDef"],
        "Name": "NameTypeDef",
        "DisplayName": str,
        "NickName": str,
        "ProfileUrl": str,
        "Emails": List["EmailTypeDef"],
        "Addresses": List["AddressTypeDef"],
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "UserType": str,
        "Title": str,
        "PreferredLanguage": str,
        "Locale": str,
        "Timezone": str,
        "IdentityStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EmailTypeDef = TypedDict(
    "EmailTypeDef",
    {
        "Value": str,
        "Type": str,
        "Primary": bool,
    },
    total=False,
)

ExternalIdTypeDef = TypedDict(
    "ExternalIdTypeDef",
    {
        "Issuer": str,
        "Id": str,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "AttributePath": str,
        "AttributeValue": str,
    },
)

GetGroupIdRequestRequestTypeDef = TypedDict(
    "GetGroupIdRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "AlternateIdentifier": "AlternateIdentifierTypeDef",
    },
)

GetGroupIdResponseTypeDef = TypedDict(
    "GetGroupIdResponseTypeDef",
    {
        "GroupId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupMembershipIdRequestRequestTypeDef = TypedDict(
    "GetGroupMembershipIdRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
        "MemberId": "MemberIdTypeDef",
    },
)

GetGroupMembershipIdResponseTypeDef = TypedDict(
    "GetGroupMembershipIdResponseTypeDef",
    {
        "MembershipId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserIdRequestRequestTypeDef = TypedDict(
    "GetUserIdRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "AlternateIdentifier": "AlternateIdentifierTypeDef",
    },
)

GetUserIdResponseTypeDef = TypedDict(
    "GetUserIdResponseTypeDef",
    {
        "UserId": str,
        "IdentityStoreId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupMembershipExistenceResultTypeDef = TypedDict(
    "GroupMembershipExistenceResultTypeDef",
    {
        "GroupId": str,
        "MemberId": "MemberIdTypeDef",
        "MembershipExists": bool,
    },
    total=False,
)

_RequiredGroupMembershipTypeDef = TypedDict(
    "_RequiredGroupMembershipTypeDef",
    {
        "IdentityStoreId": str,
    },
)
_OptionalGroupMembershipTypeDef = TypedDict(
    "_OptionalGroupMembershipTypeDef",
    {
        "MembershipId": str,
        "GroupId": str,
        "MemberId": "MemberIdTypeDef",
    },
    total=False,
)

class GroupMembershipTypeDef(_RequiredGroupMembershipTypeDef, _OptionalGroupMembershipTypeDef):
    pass

_RequiredGroupTypeDef = TypedDict(
    "_RequiredGroupTypeDef",
    {
        "GroupId": str,
        "IdentityStoreId": str,
    },
)
_OptionalGroupTypeDef = TypedDict(
    "_OptionalGroupTypeDef",
    {
        "DisplayName": str,
        "ExternalIds": List["ExternalIdTypeDef"],
        "Description": str,
    },
    total=False,
)

class GroupTypeDef(_RequiredGroupTypeDef, _OptionalGroupTypeDef):
    pass

IsMemberInGroupsRequestRequestTypeDef = TypedDict(
    "IsMemberInGroupsRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MemberId": "MemberIdTypeDef",
        "GroupIds": List[str],
    },
)

IsMemberInGroupsResponseTypeDef = TypedDict(
    "IsMemberInGroupsResponseTypeDef",
    {
        "Results": List["GroupMembershipExistenceResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupMembershipsForMemberRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupMembershipsForMemberRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "MemberId": "MemberIdTypeDef",
    },
)
_OptionalListGroupMembershipsForMemberRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupMembershipsForMemberRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListGroupMembershipsForMemberRequestRequestTypeDef(
    _RequiredListGroupMembershipsForMemberRequestRequestTypeDef,
    _OptionalListGroupMembershipsForMemberRequestRequestTypeDef,
):
    pass

ListGroupMembershipsForMemberResponseTypeDef = TypedDict(
    "ListGroupMembershipsForMemberResponseTypeDef",
    {
        "GroupMemberships": List["GroupMembershipTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "_RequiredListGroupMembershipsRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
    },
)
_OptionalListGroupMembershipsRequestRequestTypeDef = TypedDict(
    "_OptionalListGroupMembershipsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListGroupMembershipsRequestRequestTypeDef(
    _RequiredListGroupMembershipsRequestRequestTypeDef,
    _OptionalListGroupMembershipsRequestRequestTypeDef,
):
    pass

ListGroupMembershipsResponseTypeDef = TypedDict(
    "ListGroupMembershipsResponseTypeDef",
    {
        "GroupMemberships": List["GroupMembershipTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

MemberIdTypeDef = TypedDict(
    "MemberIdTypeDef",
    {
        "UserId": str,
    },
    total=False,
)

NameTypeDef = TypedDict(
    "NameTypeDef",
    {
        "Formatted": str,
        "FamilyName": str,
        "GivenName": str,
        "MiddleName": str,
        "HonorificPrefix": str,
        "HonorificSuffix": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "Value": str,
        "Type": str,
        "Primary": bool,
    },
    total=False,
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

UniqueAttributeTypeDef = TypedDict(
    "UniqueAttributeTypeDef",
    {
        "AttributePath": str,
        "AttributeValue": Dict[str, Any],
    },
)

UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "GroupId": str,
        "Operations": List["AttributeOperationTypeDef"],
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "IdentityStoreId": str,
        "UserId": str,
        "Operations": List["AttributeOperationTypeDef"],
    },
)

_RequiredUserTypeDef = TypedDict(
    "_RequiredUserTypeDef",
    {
        "UserId": str,
        "IdentityStoreId": str,
    },
)
_OptionalUserTypeDef = TypedDict(
    "_OptionalUserTypeDef",
    {
        "UserName": str,
        "ExternalIds": List["ExternalIdTypeDef"],
        "Name": "NameTypeDef",
        "DisplayName": str,
        "NickName": str,
        "ProfileUrl": str,
        "Emails": List["EmailTypeDef"],
        "Addresses": List["AddressTypeDef"],
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "UserType": str,
        "Title": str,
        "PreferredLanguage": str,
        "Locale": str,
        "Timezone": str,
    },
    total=False,
)

class UserTypeDef(_RequiredUserTypeDef, _OptionalUserTypeDef):
    pass
