"""
Type annotations for route53profiles service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53profiles/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53profiles.type_defs import AssociateProfileRequestRequestTypeDef

    data: AssociateProfileRequestRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ProfileStatusType, ShareStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateProfileRequestRequestTypeDef",
    "AssociateProfileResponseTypeDef",
    "AssociateResourceToProfileRequestRequestTypeDef",
    "AssociateResourceToProfileResponseTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteProfileResponseTypeDef",
    "DisassociateProfileRequestRequestTypeDef",
    "DisassociateProfileResponseTypeDef",
    "DisassociateResourceFromProfileRequestRequestTypeDef",
    "DisassociateResourceFromProfileResponseTypeDef",
    "GetProfileAssociationRequestRequestTypeDef",
    "GetProfileAssociationResponseTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetProfileResourceAssociationRequestRequestTypeDef",
    "GetProfileResourceAssociationResponseTypeDef",
    "GetProfileResponseTypeDef",
    "ListProfileAssociationsRequestRequestTypeDef",
    "ListProfileAssociationsResponseTypeDef",
    "ListProfileResourceAssociationsRequestRequestTypeDef",
    "ListProfileResourceAssociationsResponseTypeDef",
    "ListProfilesRequestRequestTypeDef",
    "ListProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ProfileAssociationTypeDef",
    "ProfileResourceAssociationTypeDef",
    "ProfileSummaryTypeDef",
    "ProfileTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProfileResourceAssociationRequestRequestTypeDef",
    "UpdateProfileResourceAssociationResponseTypeDef",
)

_RequiredAssociateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateProfileRequestRequestTypeDef",
    {
        "Name": str,
        "ProfileId": str,
        "ResourceId": str,
    },
)
_OptionalAssociateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateProfileRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class AssociateProfileRequestRequestTypeDef(
    _RequiredAssociateProfileRequestRequestTypeDef, _OptionalAssociateProfileRequestRequestTypeDef
):
    pass

AssociateProfileResponseTypeDef = TypedDict(
    "AssociateProfileResponseTypeDef",
    {
        "ProfileAssociation": "ProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateResourceToProfileRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateResourceToProfileRequestRequestTypeDef",
    {
        "Name": str,
        "ProfileId": str,
        "ResourceArn": str,
    },
)
_OptionalAssociateResourceToProfileRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateResourceToProfileRequestRequestTypeDef",
    {
        "ResourceProperties": str,
    },
    total=False,
)

class AssociateResourceToProfileRequestRequestTypeDef(
    _RequiredAssociateResourceToProfileRequestRequestTypeDef,
    _OptionalAssociateResourceToProfileRequestRequestTypeDef,
):
    pass

AssociateResourceToProfileResponseTypeDef = TypedDict(
    "AssociateResourceToProfileResponseTypeDef",
    {
        "ProfileResourceAssociation": "ProfileResourceAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProfileRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Name": str,
    },
)
_OptionalCreateProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProfileRequestRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateProfileRequestRequestTypeDef(
    _RequiredCreateProfileRequestRequestTypeDef, _OptionalCreateProfileRequestRequestTypeDef
):
    pass

CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "Profile": "ProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)

DeleteProfileResponseTypeDef = TypedDict(
    "DeleteProfileResponseTypeDef",
    {
        "Profile": "ProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateProfileRequestRequestTypeDef = TypedDict(
    "DisassociateProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "ResourceId": str,
    },
)

DisassociateProfileResponseTypeDef = TypedDict(
    "DisassociateProfileResponseTypeDef",
    {
        "ProfileAssociation": "ProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResourceFromProfileRequestRequestTypeDef = TypedDict(
    "DisassociateResourceFromProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
        "ResourceArn": str,
    },
)

DisassociateResourceFromProfileResponseTypeDef = TypedDict(
    "DisassociateResourceFromProfileResponseTypeDef",
    {
        "ProfileResourceAssociation": "ProfileResourceAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileAssociationRequestRequestTypeDef = TypedDict(
    "GetProfileAssociationRequestRequestTypeDef",
    {
        "ProfileAssociationId": str,
    },
)

GetProfileAssociationResponseTypeDef = TypedDict(
    "GetProfileAssociationResponseTypeDef",
    {
        "ProfileAssociation": "ProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileRequestRequestTypeDef = TypedDict(
    "GetProfileRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)

GetProfileResourceAssociationRequestRequestTypeDef = TypedDict(
    "GetProfileResourceAssociationRequestRequestTypeDef",
    {
        "ProfileResourceAssociationId": str,
    },
)

GetProfileResourceAssociationResponseTypeDef = TypedDict(
    "GetProfileResourceAssociationResponseTypeDef",
    {
        "ProfileResourceAssociation": "ProfileResourceAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "Profile": "ProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfileAssociationsRequestRequestTypeDef = TypedDict(
    "ListProfileAssociationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ProfileId": str,
        "ResourceId": str,
    },
    total=False,
)

ListProfileAssociationsResponseTypeDef = TypedDict(
    "ListProfileAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "ProfileAssociations": List["ProfileAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListProfileResourceAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredListProfileResourceAssociationsRequestRequestTypeDef",
    {
        "ProfileId": str,
    },
)
_OptionalListProfileResourceAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalListProfileResourceAssociationsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ResourceType": str,
    },
    total=False,
)

class ListProfileResourceAssociationsRequestRequestTypeDef(
    _RequiredListProfileResourceAssociationsRequestRequestTypeDef,
    _OptionalListProfileResourceAssociationsRequestRequestTypeDef,
):
    pass

ListProfileResourceAssociationsResponseTypeDef = TypedDict(
    "ListProfileResourceAssociationsResponseTypeDef",
    {
        "NextToken": str,
        "ProfileResourceAssociations": List["ProfileResourceAssociationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfilesRequestRequestTypeDef = TypedDict(
    "ListProfilesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListProfilesResponseTypeDef = TypedDict(
    "ListProfilesResponseTypeDef",
    {
        "NextToken": str,
        "ProfileSummaries": List["ProfileSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

ProfileAssociationTypeDef = TypedDict(
    "ProfileAssociationTypeDef",
    {
        "CreationTime": datetime,
        "Id": str,
        "ModificationTime": datetime,
        "Name": str,
        "OwnerId": str,
        "ProfileId": str,
        "ResourceId": str,
        "Status": ProfileStatusType,
        "StatusMessage": str,
    },
    total=False,
)

ProfileResourceAssociationTypeDef = TypedDict(
    "ProfileResourceAssociationTypeDef",
    {
        "CreationTime": datetime,
        "Id": str,
        "ModificationTime": datetime,
        "Name": str,
        "OwnerId": str,
        "ProfileId": str,
        "ResourceArn": str,
        "ResourceProperties": str,
        "ResourceType": str,
        "Status": ProfileStatusType,
        "StatusMessage": str,
    },
    total=False,
)

ProfileSummaryTypeDef = TypedDict(
    "ProfileSummaryTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "ShareStatus": ShareStatusType,
    },
    total=False,
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "Arn": str,
        "ClientToken": str,
        "CreationTime": datetime,
        "Id": str,
        "ModificationTime": datetime,
        "Name": str,
        "OwnerId": str,
        "ShareStatus": ShareStatusType,
        "Status": ProfileStatusType,
        "StatusMessage": str,
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Dict[str, str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)

_RequiredUpdateProfileResourceAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProfileResourceAssociationRequestRequestTypeDef",
    {
        "ProfileResourceAssociationId": str,
    },
)
_OptionalUpdateProfileResourceAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProfileResourceAssociationRequestRequestTypeDef",
    {
        "Name": str,
        "ResourceProperties": str,
    },
    total=False,
)

class UpdateProfileResourceAssociationRequestRequestTypeDef(
    _RequiredUpdateProfileResourceAssociationRequestRequestTypeDef,
    _OptionalUpdateProfileResourceAssociationRequestRequestTypeDef,
):
    pass

UpdateProfileResourceAssociationResponseTypeDef = TypedDict(
    "UpdateProfileResourceAssociationResponseTypeDef",
    {
        "ProfileResourceAssociation": "ProfileResourceAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
