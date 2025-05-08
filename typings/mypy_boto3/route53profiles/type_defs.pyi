"""
Type annotations for route53profiles service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_route53profiles.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime

from .literals import ProfileStatusType, ShareStatusType

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
    "AssociateProfileRequestTypeDef",
    "AssociateProfileResponseTypeDef",
    "AssociateResourceToProfileRequestTypeDef",
    "AssociateResourceToProfileResponseTypeDef",
    "CreateProfileRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteProfileRequestTypeDef",
    "DeleteProfileResponseTypeDef",
    "DisassociateProfileRequestTypeDef",
    "DisassociateProfileResponseTypeDef",
    "DisassociateResourceFromProfileRequestTypeDef",
    "DisassociateResourceFromProfileResponseTypeDef",
    "GetProfileAssociationRequestTypeDef",
    "GetProfileAssociationResponseTypeDef",
    "GetProfileRequestTypeDef",
    "GetProfileResourceAssociationRequestTypeDef",
    "GetProfileResourceAssociationResponseTypeDef",
    "GetProfileResponseTypeDef",
    "ListProfileAssociationsRequestPaginateTypeDef",
    "ListProfileAssociationsRequestTypeDef",
    "ListProfileAssociationsResponseTypeDef",
    "ListProfileResourceAssociationsRequestPaginateTypeDef",
    "ListProfileResourceAssociationsRequestTypeDef",
    "ListProfileResourceAssociationsResponseTypeDef",
    "ListProfilesRequestPaginateTypeDef",
    "ListProfilesRequestTypeDef",
    "ListProfilesResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProfileAssociationTypeDef",
    "ProfileResourceAssociationTypeDef",
    "ProfileSummaryTypeDef",
    "ProfileTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateProfileResourceAssociationRequestTypeDef",
    "UpdateProfileResourceAssociationResponseTypeDef",
)

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ProfileAssociationTypeDef(TypedDict):
    CreationTime: NotRequired[datetime]
    Id: NotRequired[str]
    ModificationTime: NotRequired[datetime]
    Name: NotRequired[str]
    OwnerId: NotRequired[str]
    ProfileId: NotRequired[str]
    ResourceId: NotRequired[str]
    Status: NotRequired[ProfileStatusType]
    StatusMessage: NotRequired[str]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AssociateResourceToProfileRequestTypeDef(TypedDict):
    Name: str
    ProfileId: str
    ResourceArn: str
    ResourceProperties: NotRequired[str]

class ProfileResourceAssociationTypeDef(TypedDict):
    CreationTime: NotRequired[datetime]
    Id: NotRequired[str]
    ModificationTime: NotRequired[datetime]
    Name: NotRequired[str]
    OwnerId: NotRequired[str]
    ProfileId: NotRequired[str]
    ResourceArn: NotRequired[str]
    ResourceProperties: NotRequired[str]
    ResourceType: NotRequired[str]
    Status: NotRequired[ProfileStatusType]
    StatusMessage: NotRequired[str]

class ProfileTypeDef(TypedDict):
    Arn: NotRequired[str]
    ClientToken: NotRequired[str]
    CreationTime: NotRequired[datetime]
    Id: NotRequired[str]
    ModificationTime: NotRequired[datetime]
    Name: NotRequired[str]
    OwnerId: NotRequired[str]
    ShareStatus: NotRequired[ShareStatusType]
    Status: NotRequired[ProfileStatusType]
    StatusMessage: NotRequired[str]

class DeleteProfileRequestTypeDef(TypedDict):
    ProfileId: str

class DisassociateProfileRequestTypeDef(TypedDict):
    ProfileId: str
    ResourceId: str

class DisassociateResourceFromProfileRequestTypeDef(TypedDict):
    ProfileId: str
    ResourceArn: str

class GetProfileAssociationRequestTypeDef(TypedDict):
    ProfileAssociationId: str

class GetProfileRequestTypeDef(TypedDict):
    ProfileId: str

class GetProfileResourceAssociationRequestTypeDef(TypedDict):
    ProfileResourceAssociationId: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListProfileAssociationsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ProfileId: NotRequired[str]
    ResourceId: NotRequired[str]

class ListProfileResourceAssociationsRequestTypeDef(TypedDict):
    ProfileId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    ResourceType: NotRequired[str]

class ListProfilesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ProfileSummaryTypeDef(TypedDict):
    Arn: NotRequired[str]
    Id: NotRequired[str]
    Name: NotRequired[str]
    ShareStatus: NotRequired[ShareStatusType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateProfileResourceAssociationRequestTypeDef(TypedDict):
    ProfileResourceAssociationId: str
    Name: NotRequired[str]
    ResourceProperties: NotRequired[str]

class AssociateProfileRequestTypeDef(TypedDict):
    Name: str
    ProfileId: str
    ResourceId: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateProfileRequestTypeDef(TypedDict):
    ClientToken: str
    Name: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class AssociateProfileResponseTypeDef(TypedDict):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateProfileResponseTypeDef(TypedDict):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileAssociationResponseTypeDef(TypedDict):
    ProfileAssociation: ProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileAssociationsResponseTypeDef(TypedDict):
    ProfileAssociations: List[ProfileAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceToProfileResponseTypeDef(TypedDict):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceFromProfileResponseTypeDef(TypedDict):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResourceAssociationResponseTypeDef(TypedDict):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileResourceAssociationsResponseTypeDef(TypedDict):
    ProfileResourceAssociations: List[ProfileResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class UpdateProfileResourceAssociationResponseTypeDef(TypedDict):
    ProfileResourceAssociation: ProfileResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileResponseTypeDef(TypedDict):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteProfileResponseTypeDef(TypedDict):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProfileResponseTypeDef(TypedDict):
    Profile: ProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProfileAssociationsRequestPaginateTypeDef(TypedDict):
    ProfileId: NotRequired[str]
    ResourceId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProfileResourceAssociationsRequestPaginateTypeDef(TypedDict):
    ProfileId: str
    ResourceType: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProfilesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListProfilesResponseTypeDef(TypedDict):
    ProfileSummaries: List[ProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
