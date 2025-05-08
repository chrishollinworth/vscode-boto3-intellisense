"""
Type annotations for identitystore service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_identitystore/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_identitystore.type_defs import AddressTypeDef

    data: AddressTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Any

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AddressTypeDef",
    "AlternateIdentifierTypeDef",
    "AttributeOperationTypeDef",
    "CreateGroupMembershipRequestTypeDef",
    "CreateGroupMembershipResponseTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteGroupMembershipRequestTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeGroupMembershipRequestTypeDef",
    "DescribeGroupMembershipResponseTypeDef",
    "DescribeGroupRequestTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResponseTypeDef",
    "EmailTypeDef",
    "ExternalIdTypeDef",
    "FilterTypeDef",
    "GetGroupIdRequestTypeDef",
    "GetGroupIdResponseTypeDef",
    "GetGroupMembershipIdRequestTypeDef",
    "GetGroupMembershipIdResponseTypeDef",
    "GetUserIdRequestTypeDef",
    "GetUserIdResponseTypeDef",
    "GroupMembershipExistenceResultTypeDef",
    "GroupMembershipTypeDef",
    "GroupTypeDef",
    "IsMemberInGroupsRequestTypeDef",
    "IsMemberInGroupsResponseTypeDef",
    "ListGroupMembershipsForMemberRequestPaginateTypeDef",
    "ListGroupMembershipsForMemberRequestTypeDef",
    "ListGroupMembershipsForMemberResponseTypeDef",
    "ListGroupMembershipsRequestPaginateTypeDef",
    "ListGroupMembershipsRequestTypeDef",
    "ListGroupMembershipsResponseTypeDef",
    "ListGroupsRequestPaginateTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListUsersRequestPaginateTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResponseTypeDef",
    "MemberIdTypeDef",
    "NameTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberTypeDef",
    "ResponseMetadataTypeDef",
    "UniqueAttributeTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateUserRequestTypeDef",
    "UserTypeDef",
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "StreetAddress": NotRequired[str],
        "Locality": NotRequired[str],
        "Region": NotRequired[str],
        "PostalCode": NotRequired[str],
        "Country": NotRequired[str],
        "Formatted": NotRequired[str],
        "Type": NotRequired[str],
        "Primary": NotRequired[bool],
    },
)

class ExternalIdTypeDef(TypedDict):
    Issuer: str
    Id: str

class UniqueAttributeTypeDef(TypedDict):
    AttributePath: str
    AttributeValue: Mapping[str, Any]

class AttributeOperationTypeDef(TypedDict):
    AttributePath: str
    AttributeValue: NotRequired[Mapping[str, Any]]

class MemberIdTypeDef(TypedDict):
    UserId: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateGroupRequestTypeDef(TypedDict):
    IdentityStoreId: str
    DisplayName: NotRequired[str]
    Description: NotRequired[str]

EmailTypeDef = TypedDict(
    "EmailTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[str],
        "Primary": NotRequired[bool],
    },
)

class NameTypeDef(TypedDict):
    Formatted: NotRequired[str]
    FamilyName: NotRequired[str]
    GivenName: NotRequired[str]
    MiddleName: NotRequired[str]
    HonorificPrefix: NotRequired[str]
    HonorificSuffix: NotRequired[str]

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[str],
        "Primary": NotRequired[bool],
    },
)

class DeleteGroupMembershipRequestTypeDef(TypedDict):
    IdentityStoreId: str
    MembershipId: str

class DeleteGroupRequestTypeDef(TypedDict):
    IdentityStoreId: str
    GroupId: str

class DeleteUserRequestTypeDef(TypedDict):
    IdentityStoreId: str
    UserId: str

class DescribeGroupMembershipRequestTypeDef(TypedDict):
    IdentityStoreId: str
    MembershipId: str

class DescribeGroupRequestTypeDef(TypedDict):
    IdentityStoreId: str
    GroupId: str

class DescribeUserRequestTypeDef(TypedDict):
    IdentityStoreId: str
    UserId: str

class FilterTypeDef(TypedDict):
    AttributePath: str
    AttributeValue: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListGroupMembershipsRequestTypeDef(TypedDict):
    IdentityStoreId: str
    GroupId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class GroupTypeDef(TypedDict):
    GroupId: str
    IdentityStoreId: str
    DisplayName: NotRequired[str]
    ExternalIds: NotRequired[List[ExternalIdTypeDef]]
    Description: NotRequired[str]

class AlternateIdentifierTypeDef(TypedDict):
    ExternalId: NotRequired[ExternalIdTypeDef]
    UniqueAttribute: NotRequired[UniqueAttributeTypeDef]

class UpdateGroupRequestTypeDef(TypedDict):
    IdentityStoreId: str
    GroupId: str
    Operations: Sequence[AttributeOperationTypeDef]

class UpdateUserRequestTypeDef(TypedDict):
    IdentityStoreId: str
    UserId: str
    Operations: Sequence[AttributeOperationTypeDef]

class CreateGroupMembershipRequestTypeDef(TypedDict):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberIdTypeDef

class GetGroupMembershipIdRequestTypeDef(TypedDict):
    IdentityStoreId: str
    GroupId: str
    MemberId: MemberIdTypeDef

class GroupMembershipExistenceResultTypeDef(TypedDict):
    GroupId: NotRequired[str]
    MemberId: NotRequired[MemberIdTypeDef]
    MembershipExists: NotRequired[bool]

class GroupMembershipTypeDef(TypedDict):
    IdentityStoreId: str
    MembershipId: NotRequired[str]
    GroupId: NotRequired[str]
    MemberId: NotRequired[MemberIdTypeDef]

class IsMemberInGroupsRequestTypeDef(TypedDict):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    GroupIds: Sequence[str]

class ListGroupMembershipsForMemberRequestTypeDef(TypedDict):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class CreateGroupMembershipResponseTypeDef(TypedDict):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(TypedDict):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(TypedDict):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupMembershipResponseTypeDef(TypedDict):
    IdentityStoreId: str
    MembershipId: str
    GroupId: str
    MemberId: MemberIdTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupResponseTypeDef(TypedDict):
    GroupId: str
    DisplayName: str
    ExternalIds: List[ExternalIdTypeDef]
    Description: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupIdResponseTypeDef(TypedDict):
    GroupId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupMembershipIdResponseTypeDef(TypedDict):
    MembershipId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserIdResponseTypeDef(TypedDict):
    UserId: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserRequestTypeDef(TypedDict):
    IdentityStoreId: str
    UserName: NotRequired[str]
    Name: NotRequired[NameTypeDef]
    DisplayName: NotRequired[str]
    NickName: NotRequired[str]
    ProfileUrl: NotRequired[str]
    Emails: NotRequired[Sequence[EmailTypeDef]]
    Addresses: NotRequired[Sequence[AddressTypeDef]]
    PhoneNumbers: NotRequired[Sequence[PhoneNumberTypeDef]]
    UserType: NotRequired[str]
    Title: NotRequired[str]
    PreferredLanguage: NotRequired[str]
    Locale: NotRequired[str]
    Timezone: NotRequired[str]

class DescribeUserResponseTypeDef(TypedDict):
    UserName: str
    UserId: str
    ExternalIds: List[ExternalIdTypeDef]
    Name: NameTypeDef
    DisplayName: str
    NickName: str
    ProfileUrl: str
    Emails: List[EmailTypeDef]
    Addresses: List[AddressTypeDef]
    PhoneNumbers: List[PhoneNumberTypeDef]
    UserType: str
    Title: str
    PreferredLanguage: str
    Locale: str
    Timezone: str
    IdentityStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UserTypeDef(TypedDict):
    UserId: str
    IdentityStoreId: str
    UserName: NotRequired[str]
    ExternalIds: NotRequired[List[ExternalIdTypeDef]]
    Name: NotRequired[NameTypeDef]
    DisplayName: NotRequired[str]
    NickName: NotRequired[str]
    ProfileUrl: NotRequired[str]
    Emails: NotRequired[List[EmailTypeDef]]
    Addresses: NotRequired[List[AddressTypeDef]]
    PhoneNumbers: NotRequired[List[PhoneNumberTypeDef]]
    UserType: NotRequired[str]
    Title: NotRequired[str]
    PreferredLanguage: NotRequired[str]
    Locale: NotRequired[str]
    Timezone: NotRequired[str]

class ListGroupsRequestTypeDef(TypedDict):
    IdentityStoreId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListUsersRequestTypeDef(TypedDict):
    IdentityStoreId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Filters: NotRequired[Sequence[FilterTypeDef]]

class ListGroupMembershipsForMemberRequestPaginateTypeDef(TypedDict):
    IdentityStoreId: str
    MemberId: MemberIdTypeDef
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupMembershipsRequestPaginateTypeDef(TypedDict):
    IdentityStoreId: str
    GroupId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupsRequestPaginateTypeDef(TypedDict):
    IdentityStoreId: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsersRequestPaginateTypeDef(TypedDict):
    IdentityStoreId: str
    Filters: NotRequired[Sequence[FilterTypeDef]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupsResponseTypeDef(TypedDict):
    Groups: List[GroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class GetGroupIdRequestTypeDef(TypedDict):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifierTypeDef

class GetUserIdRequestTypeDef(TypedDict):
    IdentityStoreId: str
    AlternateIdentifier: AlternateIdentifierTypeDef

class IsMemberInGroupsResponseTypeDef(TypedDict):
    Results: List[GroupMembershipExistenceResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupMembershipsForMemberResponseTypeDef(TypedDict):
    GroupMemberships: List[GroupMembershipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGroupMembershipsResponseTypeDef(TypedDict):
    GroupMemberships: List[GroupMembershipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListUsersResponseTypeDef(TypedDict):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
