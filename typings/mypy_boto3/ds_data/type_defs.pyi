"""
Type annotations for ds-data service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ds_data/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_ds_data.type_defs import AddGroupMemberRequestTypeDef

    data: AddGroupMemberRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from typing import Union

from .literals import GroupScopeType, GroupTypeType, MemberTypeType, UpdateTypeType

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
    "AddGroupMemberRequestTypeDef",
    "AttributeValueOutputTypeDef",
    "AttributeValueTypeDef",
    "AttributeValueUnionTypeDef",
    "CreateGroupRequestTypeDef",
    "CreateGroupResultTypeDef",
    "CreateUserRequestTypeDef",
    "CreateUserResultTypeDef",
    "DeleteGroupRequestTypeDef",
    "DeleteUserRequestTypeDef",
    "DescribeGroupRequestTypeDef",
    "DescribeGroupResultTypeDef",
    "DescribeUserRequestTypeDef",
    "DescribeUserResultTypeDef",
    "DisableUserRequestTypeDef",
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "ListGroupMembersRequestPaginateTypeDef",
    "ListGroupMembersRequestTypeDef",
    "ListGroupMembersResultTypeDef",
    "ListGroupsForMemberRequestPaginateTypeDef",
    "ListGroupsForMemberRequestTypeDef",
    "ListGroupsForMemberResultTypeDef",
    "ListGroupsRequestPaginateTypeDef",
    "ListGroupsRequestTypeDef",
    "ListGroupsResultTypeDef",
    "ListUsersRequestPaginateTypeDef",
    "ListUsersRequestTypeDef",
    "ListUsersResultTypeDef",
    "MemberTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveGroupMemberRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SearchGroupsRequestPaginateTypeDef",
    "SearchGroupsRequestTypeDef",
    "SearchGroupsResultTypeDef",
    "SearchUsersRequestPaginateTypeDef",
    "SearchUsersRequestTypeDef",
    "SearchUsersResultTypeDef",
    "UpdateGroupRequestTypeDef",
    "UpdateUserRequestTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
)

class AddGroupMemberRequestTypeDef(TypedDict):
    DirectoryId: str
    GroupName: str
    MemberName: str
    ClientToken: NotRequired[str]
    MemberRealm: NotRequired[str]

class AttributeValueOutputTypeDef(TypedDict):
    BOOL: NotRequired[bool]
    N: NotRequired[int]
    S: NotRequired[str]
    SS: NotRequired[List[str]]

class AttributeValueTypeDef(TypedDict):
    BOOL: NotRequired[bool]
    N: NotRequired[int]
    S: NotRequired[str]
    SS: NotRequired[Sequence[str]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class DeleteGroupRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: NotRequired[str]

class DeleteUserRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: NotRequired[str]

class DescribeGroupRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    OtherAttributes: NotRequired[Sequence[str]]
    Realm: NotRequired[str]

class DescribeUserRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    OtherAttributes: NotRequired[Sequence[str]]
    Realm: NotRequired[str]

class DisableUserRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: NotRequired[str]

class GroupSummaryTypeDef(TypedDict):
    GroupScope: GroupScopeType
    GroupType: GroupTypeType
    SAMAccountName: str
    SID: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListGroupMembersRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    MaxResults: NotRequired[int]
    MemberRealm: NotRequired[str]
    NextToken: NotRequired[str]
    Realm: NotRequired[str]

class MemberTypeDef(TypedDict):
    MemberType: MemberTypeType
    SAMAccountName: str
    SID: str

class ListGroupsForMemberRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    MaxResults: NotRequired[int]
    MemberRealm: NotRequired[str]
    NextToken: NotRequired[str]
    Realm: NotRequired[str]

class ListGroupsRequestTypeDef(TypedDict):
    DirectoryId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Realm: NotRequired[str]

class ListUsersRequestTypeDef(TypedDict):
    DirectoryId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Realm: NotRequired[str]

class UserSummaryTypeDef(TypedDict):
    Enabled: bool
    SAMAccountName: str
    SID: str
    GivenName: NotRequired[str]
    Surname: NotRequired[str]

class RemoveGroupMemberRequestTypeDef(TypedDict):
    DirectoryId: str
    GroupName: str
    MemberName: str
    ClientToken: NotRequired[str]
    MemberRealm: NotRequired[str]

class SearchGroupsRequestTypeDef(TypedDict):
    DirectoryId: str
    SearchAttributes: Sequence[str]
    SearchString: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Realm: NotRequired[str]

class SearchUsersRequestTypeDef(TypedDict):
    DirectoryId: str
    SearchAttributes: Sequence[str]
    SearchString: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    Realm: NotRequired[str]

class GroupTypeDef(TypedDict):
    SAMAccountName: str
    DistinguishedName: NotRequired[str]
    GroupScope: NotRequired[GroupScopeType]
    GroupType: NotRequired[GroupTypeType]
    OtherAttributes: NotRequired[Dict[str, AttributeValueOutputTypeDef]]
    SID: NotRequired[str]

class UserTypeDef(TypedDict):
    SAMAccountName: str
    DistinguishedName: NotRequired[str]
    EmailAddress: NotRequired[str]
    Enabled: NotRequired[bool]
    GivenName: NotRequired[str]
    OtherAttributes: NotRequired[Dict[str, AttributeValueOutputTypeDef]]
    SID: NotRequired[str]
    Surname: NotRequired[str]
    UserPrincipalName: NotRequired[str]

AttributeValueUnionTypeDef = Union[AttributeValueTypeDef, AttributeValueOutputTypeDef]

class CreateGroupResultTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResultTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGroupResultTypeDef(TypedDict):
    DirectoryId: str
    DistinguishedName: str
    GroupScope: GroupScopeType
    GroupType: GroupTypeType
    OtherAttributes: Dict[str, AttributeValueOutputTypeDef]
    Realm: str
    SAMAccountName: str
    SID: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserResultTypeDef(TypedDict):
    DirectoryId: str
    DistinguishedName: str
    EmailAddress: str
    Enabled: bool
    GivenName: str
    OtherAttributes: Dict[str, AttributeValueOutputTypeDef]
    Realm: str
    SAMAccountName: str
    SID: str
    Surname: str
    UserPrincipalName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsForMemberResultTypeDef(TypedDict):
    DirectoryId: str
    Groups: List[GroupSummaryTypeDef]
    MemberRealm: str
    Realm: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGroupsResultTypeDef(TypedDict):
    DirectoryId: str
    Groups: List[GroupSummaryTypeDef]
    Realm: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListGroupMembersRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    MemberRealm: NotRequired[str]
    Realm: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupsForMemberRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    MemberRealm: NotRequired[str]
    Realm: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupsRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    Realm: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListUsersRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    Realm: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchGroupsRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    SearchAttributes: Sequence[str]
    SearchString: str
    Realm: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class SearchUsersRequestPaginateTypeDef(TypedDict):
    DirectoryId: str
    SearchAttributes: Sequence[str]
    SearchString: str
    Realm: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGroupMembersResultTypeDef(TypedDict):
    DirectoryId: str
    MemberRealm: str
    Members: List[MemberTypeDef]
    Realm: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListUsersResultTypeDef(TypedDict):
    DirectoryId: str
    Realm: str
    Users: List[UserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchGroupsResultTypeDef(TypedDict):
    DirectoryId: str
    Groups: List[GroupTypeDef]
    Realm: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SearchUsersResultTypeDef(TypedDict):
    DirectoryId: str
    Realm: str
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class CreateGroupRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: NotRequired[str]
    GroupScope: NotRequired[GroupScopeType]
    GroupType: NotRequired[GroupTypeType]
    OtherAttributes: NotRequired[Mapping[str, AttributeValueUnionTypeDef]]

class CreateUserRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: NotRequired[str]
    EmailAddress: NotRequired[str]
    GivenName: NotRequired[str]
    OtherAttributes: NotRequired[Mapping[str, AttributeValueUnionTypeDef]]
    Surname: NotRequired[str]

class UpdateGroupRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: NotRequired[str]
    GroupScope: NotRequired[GroupScopeType]
    GroupType: NotRequired[GroupTypeType]
    OtherAttributes: NotRequired[Mapping[str, AttributeValueUnionTypeDef]]
    UpdateType: NotRequired[UpdateTypeType]

class UpdateUserRequestTypeDef(TypedDict):
    DirectoryId: str
    SAMAccountName: str
    ClientToken: NotRequired[str]
    EmailAddress: NotRequired[str]
    GivenName: NotRequired[str]
    OtherAttributes: NotRequired[Mapping[str, AttributeValueUnionTypeDef]]
    Surname: NotRequired[str]
    UpdateType: NotRequired[UpdateTypeType]
