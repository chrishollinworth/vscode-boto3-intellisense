"""
Type annotations for cloud9 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloud9.type_defs import CreateEnvironmentEC2RequestRequestTypeDef

    data: CreateEnvironmentEC2RequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ConnectionTypeType,
    EnvironmentLifecycleStatusType,
    EnvironmentStatusType,
    EnvironmentTypeType,
    ManagedCredentialsStatusType,
    MemberPermissionsType,
    PermissionsType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateEnvironmentEC2RequestRequestTypeDef",
    "CreateEnvironmentEC2ResultTypeDef",
    "CreateEnvironmentMembershipRequestRequestTypeDef",
    "CreateEnvironmentMembershipResultTypeDef",
    "DeleteEnvironmentMembershipRequestRequestTypeDef",
    "DeleteEnvironmentRequestRequestTypeDef",
    "DescribeEnvironmentMembershipsRequestRequestTypeDef",
    "DescribeEnvironmentMembershipsResultTypeDef",
    "DescribeEnvironmentStatusRequestRequestTypeDef",
    "DescribeEnvironmentStatusResultTypeDef",
    "DescribeEnvironmentsRequestRequestTypeDef",
    "DescribeEnvironmentsResultTypeDef",
    "EnvironmentLifecycleTypeDef",
    "EnvironmentMemberTypeDef",
    "EnvironmentTypeDef",
    "ListEnvironmentsRequestRequestTypeDef",
    "ListEnvironmentsResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEnvironmentMembershipRequestRequestTypeDef",
    "UpdateEnvironmentMembershipResultTypeDef",
    "UpdateEnvironmentRequestRequestTypeDef",
)

_RequiredCreateEnvironmentEC2RequestRequestTypeDef = TypedDict(
    "_RequiredCreateEnvironmentEC2RequestRequestTypeDef",
    {
        "name": str,
        "instanceType": str,
    },
)
_OptionalCreateEnvironmentEC2RequestRequestTypeDef = TypedDict(
    "_OptionalCreateEnvironmentEC2RequestRequestTypeDef",
    {
        "description": str,
        "clientRequestToken": str,
        "subnetId": str,
        "imageId": str,
        "automaticStopTimeMinutes": int,
        "ownerArn": str,
        "tags": List["TagTypeDef"],
        "connectionType": ConnectionTypeType,
    },
    total=False,
)

class CreateEnvironmentEC2RequestRequestTypeDef(
    _RequiredCreateEnvironmentEC2RequestRequestTypeDef,
    _OptionalCreateEnvironmentEC2RequestRequestTypeDef,
):
    pass

CreateEnvironmentEC2ResultTypeDef = TypedDict(
    "CreateEnvironmentEC2ResultTypeDef",
    {
        "environmentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "CreateEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
        "permissions": MemberPermissionsType,
    },
)

CreateEnvironmentMembershipResultTypeDef = TypedDict(
    "CreateEnvironmentMembershipResultTypeDef",
    {
        "membership": "EnvironmentMemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
    },
)

DeleteEnvironmentRequestRequestTypeDef = TypedDict(
    "DeleteEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

DescribeEnvironmentMembershipsRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsRequestRequestTypeDef",
    {
        "userArn": str,
        "environmentId": str,
        "permissions": List[PermissionsType],
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

DescribeEnvironmentMembershipsResultTypeDef = TypedDict(
    "DescribeEnvironmentMembershipsResultTypeDef",
    {
        "memberships": List["EnvironmentMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentStatusRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentStatusRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)

DescribeEnvironmentStatusResultTypeDef = TypedDict(
    "DescribeEnvironmentStatusResultTypeDef",
    {
        "status": EnvironmentStatusType,
        "message": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEnvironmentsRequestRequestTypeDef = TypedDict(
    "DescribeEnvironmentsRequestRequestTypeDef",
    {
        "environmentIds": List[str],
    },
)

DescribeEnvironmentsResultTypeDef = TypedDict(
    "DescribeEnvironmentsResultTypeDef",
    {
        "environments": List["EnvironmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnvironmentLifecycleTypeDef = TypedDict(
    "EnvironmentLifecycleTypeDef",
    {
        "status": EnvironmentLifecycleStatusType,
        "reason": str,
        "failureResource": str,
    },
    total=False,
)

_RequiredEnvironmentMemberTypeDef = TypedDict(
    "_RequiredEnvironmentMemberTypeDef",
    {
        "permissions": PermissionsType,
        "userId": str,
        "userArn": str,
        "environmentId": str,
    },
)
_OptionalEnvironmentMemberTypeDef = TypedDict(
    "_OptionalEnvironmentMemberTypeDef",
    {
        "lastAccess": datetime,
    },
    total=False,
)

class EnvironmentMemberTypeDef(
    _RequiredEnvironmentMemberTypeDef, _OptionalEnvironmentMemberTypeDef
):
    pass

_RequiredEnvironmentTypeDef = TypedDict(
    "_RequiredEnvironmentTypeDef",
    {
        "type": EnvironmentTypeType,
        "arn": str,
        "ownerArn": str,
    },
)
_OptionalEnvironmentTypeDef = TypedDict(
    "_OptionalEnvironmentTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "connectionType": ConnectionTypeType,
        "lifecycle": "EnvironmentLifecycleTypeDef",
        "managedCredentialsStatus": ManagedCredentialsStatusType,
    },
    total=False,
)

class EnvironmentTypeDef(_RequiredEnvironmentTypeDef, _OptionalEnvironmentTypeDef):
    pass

ListEnvironmentsRequestRequestTypeDef = TypedDict(
    "ListEnvironmentsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListEnvironmentsResultTypeDef = TypedDict(
    "ListEnvironmentsResultTypeDef",
    {
        "nextToken": str,
        "environmentIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
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
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
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
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

UpdateEnvironmentMembershipRequestRequestTypeDef = TypedDict(
    "UpdateEnvironmentMembershipRequestRequestTypeDef",
    {
        "environmentId": str,
        "userArn": str,
        "permissions": MemberPermissionsType,
    },
)

UpdateEnvironmentMembershipResultTypeDef = TypedDict(
    "UpdateEnvironmentMembershipResultTypeDef",
    {
        "membership": "EnvironmentMemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEnvironmentRequestRequestTypeDef",
    {
        "environmentId": str,
    },
)
_OptionalUpdateEnvironmentRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEnvironmentRequestRequestTypeDef",
    {
        "name": str,
        "description": str,
    },
    total=False,
)

class UpdateEnvironmentRequestRequestTypeDef(
    _RequiredUpdateEnvironmentRequestRequestTypeDef, _OptionalUpdateEnvironmentRequestRequestTypeDef
):
    pass
