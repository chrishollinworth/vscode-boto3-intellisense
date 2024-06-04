"""
Type annotations for repostspace service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_repostspace/type_defs.html)

Usage::

    ```python
    from mypy_boto3_repostspace.type_defs import CreateSpaceInputRequestTypeDef

    data: CreateSpaceInputRequestTypeDef = {...}
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import ConfigurationStatusType, TierLevelType, VanityDomainStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateSpaceInputRequestTypeDef",
    "CreateSpaceOutputTypeDef",
    "DeleteSpaceInputRequestTypeDef",
    "DeregisterAdminInputRequestTypeDef",
    "GetSpaceInputRequestTypeDef",
    "GetSpaceOutputTypeDef",
    "ListSpacesInputRequestTypeDef",
    "ListSpacesOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterAdminInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SendInvitesInputRequestTypeDef",
    "SpaceDataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSpaceInputRequestTypeDef",
)

_RequiredCreateSpaceInputRequestTypeDef = TypedDict(
    "_RequiredCreateSpaceInputRequestTypeDef",
    {
        "name": str,
        "subdomain": str,
        "tier": TierLevelType,
    },
)
_OptionalCreateSpaceInputRequestTypeDef = TypedDict(
    "_OptionalCreateSpaceInputRequestTypeDef",
    {
        "description": str,
        "roleArn": str,
        "tags": Dict[str, str],
        "userKMSKey": str,
    },
    total=False,
)

class CreateSpaceInputRequestTypeDef(
    _RequiredCreateSpaceInputRequestTypeDef, _OptionalCreateSpaceInputRequestTypeDef
):
    pass

CreateSpaceOutputTypeDef = TypedDict(
    "CreateSpaceOutputTypeDef",
    {
        "spaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSpaceInputRequestTypeDef = TypedDict(
    "DeleteSpaceInputRequestTypeDef",
    {
        "spaceId": str,
    },
)

DeregisterAdminInputRequestTypeDef = TypedDict(
    "DeregisterAdminInputRequestTypeDef",
    {
        "adminId": str,
        "spaceId": str,
    },
)

GetSpaceInputRequestTypeDef = TypedDict(
    "GetSpaceInputRequestTypeDef",
    {
        "spaceId": str,
    },
)

GetSpaceOutputTypeDef = TypedDict(
    "GetSpaceOutputTypeDef",
    {
        "arn": str,
        "clientId": str,
        "configurationStatus": ConfigurationStatusType,
        "contentSize": int,
        "createDateTime": datetime,
        "customerRoleArn": str,
        "deleteDateTime": datetime,
        "description": str,
        "groupAdmins": List[str],
        "name": str,
        "randomDomain": str,
        "spaceId": str,
        "status": str,
        "storageLimit": int,
        "tier": TierLevelType,
        "userAdmins": List[str],
        "userCount": int,
        "userKMSKey": str,
        "vanityDomain": str,
        "vanityDomainStatus": VanityDomainStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSpacesInputRequestTypeDef = TypedDict(
    "ListSpacesInputRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListSpacesOutputTypeDef = TypedDict(
    "ListSpacesOutputTypeDef",
    {
        "nextToken": str,
        "spaces": List["SpaceDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
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

RegisterAdminInputRequestTypeDef = TypedDict(
    "RegisterAdminInputRequestTypeDef",
    {
        "adminId": str,
        "spaceId": str,
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

SendInvitesInputRequestTypeDef = TypedDict(
    "SendInvitesInputRequestTypeDef",
    {
        "accessorIds": List[str],
        "body": str,
        "spaceId": str,
        "title": str,
    },
)

_RequiredSpaceDataTypeDef = TypedDict(
    "_RequiredSpaceDataTypeDef",
    {
        "arn": str,
        "configurationStatus": ConfigurationStatusType,
        "createDateTime": datetime,
        "name": str,
        "randomDomain": str,
        "spaceId": str,
        "status": str,
        "storageLimit": int,
        "tier": TierLevelType,
        "vanityDomain": str,
        "vanityDomainStatus": VanityDomainStatusType,
    },
)
_OptionalSpaceDataTypeDef = TypedDict(
    "_OptionalSpaceDataTypeDef",
    {
        "contentSize": int,
        "deleteDateTime": datetime,
        "description": str,
        "userCount": int,
        "userKMSKey": str,
    },
    total=False,
)

class SpaceDataTypeDef(_RequiredSpaceDataTypeDef, _OptionalSpaceDataTypeDef):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Dict[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": List[str],
    },
)

_RequiredUpdateSpaceInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSpaceInputRequestTypeDef",
    {
        "spaceId": str,
    },
)
_OptionalUpdateSpaceInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSpaceInputRequestTypeDef",
    {
        "description": str,
        "roleArn": str,
        "tier": TierLevelType,
    },
    total=False,
)

class UpdateSpaceInputRequestTypeDef(
    _RequiredUpdateSpaceInputRequestTypeDef, _OptionalUpdateSpaceInputRequestTypeDef
):
    pass
