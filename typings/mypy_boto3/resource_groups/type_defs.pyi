"""
Type annotations for resource-groups service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/type_defs.html)

Usage::

    ```python
    from mypy_boto3_resource_groups.type_defs import CreateGroupInputRequestTypeDef

    data: CreateGroupInputRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import (
    GroupConfigurationStatusType,
    GroupFilterNameType,
    QueryErrorCodeType,
    QueryTypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CreateGroupInputRequestTypeDef",
    "CreateGroupOutputTypeDef",
    "DeleteGroupInputRequestTypeDef",
    "DeleteGroupOutputTypeDef",
    "FailedResourceTypeDef",
    "GetGroupConfigurationInputRequestTypeDef",
    "GetGroupConfigurationOutputTypeDef",
    "GetGroupInputRequestTypeDef",
    "GetGroupOutputTypeDef",
    "GetGroupQueryInputRequestTypeDef",
    "GetGroupQueryOutputTypeDef",
    "GetTagsInputRequestTypeDef",
    "GetTagsOutputTypeDef",
    "GroupConfigurationItemTypeDef",
    "GroupConfigurationParameterTypeDef",
    "GroupConfigurationTypeDef",
    "GroupFilterTypeDef",
    "GroupIdentifierTypeDef",
    "GroupQueryTypeDef",
    "GroupResourcesInputRequestTypeDef",
    "GroupResourcesOutputTypeDef",
    "GroupTypeDef",
    "ListGroupResourcesInputRequestTypeDef",
    "ListGroupResourcesItemTypeDef",
    "ListGroupResourcesOutputTypeDef",
    "ListGroupsInputRequestTypeDef",
    "ListGroupsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PendingResourceTypeDef",
    "PutGroupConfigurationInputRequestTypeDef",
    "QueryErrorTypeDef",
    "ResourceFilterTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceQueryTypeDef",
    "ResourceStatusTypeDef",
    "ResponseMetadataTypeDef",
    "SearchResourcesInputRequestTypeDef",
    "SearchResourcesOutputTypeDef",
    "TagInputRequestTypeDef",
    "TagOutputTypeDef",
    "UngroupResourcesInputRequestTypeDef",
    "UngroupResourcesOutputTypeDef",
    "UntagInputRequestTypeDef",
    "UntagOutputTypeDef",
    "UpdateGroupInputRequestTypeDef",
    "UpdateGroupOutputTypeDef",
    "UpdateGroupQueryInputRequestTypeDef",
    "UpdateGroupQueryOutputTypeDef",
)

_RequiredCreateGroupInputRequestTypeDef = TypedDict(
    "_RequiredCreateGroupInputRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateGroupInputRequestTypeDef = TypedDict(
    "_OptionalCreateGroupInputRequestTypeDef",
    {
        "Description": str,
        "ResourceQuery": "ResourceQueryTypeDef",
        "Tags": Dict[str, str],
        "Configuration": List["GroupConfigurationItemTypeDef"],
    },
    total=False,
)

class CreateGroupInputRequestTypeDef(
    _RequiredCreateGroupInputRequestTypeDef, _OptionalCreateGroupInputRequestTypeDef
):
    pass

CreateGroupOutputTypeDef = TypedDict(
    "CreateGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResourceQuery": "ResourceQueryTypeDef",
        "Tags": Dict[str, str],
        "GroupConfiguration": "GroupConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupInputRequestTypeDef = TypedDict(
    "DeleteGroupInputRequestTypeDef",
    {
        "GroupName": str,
        "Group": str,
    },
    total=False,
)

DeleteGroupOutputTypeDef = TypedDict(
    "DeleteGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedResourceTypeDef = TypedDict(
    "FailedResourceTypeDef",
    {
        "ResourceArn": str,
        "ErrorMessage": str,
        "ErrorCode": str,
    },
    total=False,
)

GetGroupConfigurationInputRequestTypeDef = TypedDict(
    "GetGroupConfigurationInputRequestTypeDef",
    {
        "Group": str,
    },
    total=False,
)

GetGroupConfigurationOutputTypeDef = TypedDict(
    "GetGroupConfigurationOutputTypeDef",
    {
        "GroupConfiguration": "GroupConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupInputRequestTypeDef = TypedDict(
    "GetGroupInputRequestTypeDef",
    {
        "GroupName": str,
        "Group": str,
    },
    total=False,
)

GetGroupOutputTypeDef = TypedDict(
    "GetGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupQueryInputRequestTypeDef = TypedDict(
    "GetGroupQueryInputRequestTypeDef",
    {
        "GroupName": str,
        "Group": str,
    },
    total=False,
)

GetGroupQueryOutputTypeDef = TypedDict(
    "GetGroupQueryOutputTypeDef",
    {
        "GroupQuery": "GroupQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsInputRequestTypeDef = TypedDict(
    "GetTagsInputRequestTypeDef",
    {
        "Arn": str,
    },
)

GetTagsOutputTypeDef = TypedDict(
    "GetTagsOutputTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGroupConfigurationItemTypeDef = TypedDict(
    "_RequiredGroupConfigurationItemTypeDef",
    {
        "Type": str,
    },
)
_OptionalGroupConfigurationItemTypeDef = TypedDict(
    "_OptionalGroupConfigurationItemTypeDef",
    {
        "Parameters": List["GroupConfigurationParameterTypeDef"],
    },
    total=False,
)

class GroupConfigurationItemTypeDef(
    _RequiredGroupConfigurationItemTypeDef, _OptionalGroupConfigurationItemTypeDef
):
    pass

_RequiredGroupConfigurationParameterTypeDef = TypedDict(
    "_RequiredGroupConfigurationParameterTypeDef",
    {
        "Name": str,
    },
)
_OptionalGroupConfigurationParameterTypeDef = TypedDict(
    "_OptionalGroupConfigurationParameterTypeDef",
    {
        "Values": List[str],
    },
    total=False,
)

class GroupConfigurationParameterTypeDef(
    _RequiredGroupConfigurationParameterTypeDef, _OptionalGroupConfigurationParameterTypeDef
):
    pass

GroupConfigurationTypeDef = TypedDict(
    "GroupConfigurationTypeDef",
    {
        "Configuration": List["GroupConfigurationItemTypeDef"],
        "ProposedConfiguration": List["GroupConfigurationItemTypeDef"],
        "Status": GroupConfigurationStatusType,
        "FailureReason": str,
    },
    total=False,
)

GroupFilterTypeDef = TypedDict(
    "GroupFilterTypeDef",
    {
        "Name": GroupFilterNameType,
        "Values": List[str],
    },
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef",
    {
        "GroupName": str,
        "GroupArn": str,
    },
    total=False,
)

GroupQueryTypeDef = TypedDict(
    "GroupQueryTypeDef",
    {
        "GroupName": str,
        "ResourceQuery": "ResourceQueryTypeDef",
    },
)

GroupResourcesInputRequestTypeDef = TypedDict(
    "GroupResourcesInputRequestTypeDef",
    {
        "Group": str,
        "ResourceArns": List[str],
    },
)

GroupResourcesOutputTypeDef = TypedDict(
    "GroupResourcesOutputTypeDef",
    {
        "Succeeded": List[str],
        "Failed": List["FailedResourceTypeDef"],
        "Pending": List["PendingResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGroupTypeDef = TypedDict(
    "_RequiredGroupTypeDef",
    {
        "GroupArn": str,
        "Name": str,
    },
)
_OptionalGroupTypeDef = TypedDict(
    "_OptionalGroupTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class GroupTypeDef(_RequiredGroupTypeDef, _OptionalGroupTypeDef):
    pass

ListGroupResourcesInputRequestTypeDef = TypedDict(
    "ListGroupResourcesInputRequestTypeDef",
    {
        "GroupName": str,
        "Group": str,
        "Filters": List["ResourceFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGroupResourcesItemTypeDef = TypedDict(
    "ListGroupResourcesItemTypeDef",
    {
        "Identifier": "ResourceIdentifierTypeDef",
        "Status": "ResourceStatusTypeDef",
    },
    total=False,
)

ListGroupResourcesOutputTypeDef = TypedDict(
    "ListGroupResourcesOutputTypeDef",
    {
        "Resources": List["ListGroupResourcesItemTypeDef"],
        "ResourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "NextToken": str,
        "QueryErrors": List["QueryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsInputRequestTypeDef = TypedDict(
    "ListGroupsInputRequestTypeDef",
    {
        "Filters": List["GroupFilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

ListGroupsOutputTypeDef = TypedDict(
    "ListGroupsOutputTypeDef",
    {
        "GroupIdentifiers": List["GroupIdentifierTypeDef"],
        "Groups": List["GroupTypeDef"],
        "NextToken": str,
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

PendingResourceTypeDef = TypedDict(
    "PendingResourceTypeDef",
    {
        "ResourceArn": str,
    },
    total=False,
)

PutGroupConfigurationInputRequestTypeDef = TypedDict(
    "PutGroupConfigurationInputRequestTypeDef",
    {
        "Group": str,
        "Configuration": List["GroupConfigurationItemTypeDef"],
    },
    total=False,
)

QueryErrorTypeDef = TypedDict(
    "QueryErrorTypeDef",
    {
        "ErrorCode": QueryErrorCodeType,
        "Message": str,
    },
    total=False,
)

ResourceFilterTypeDef = TypedDict(
    "ResourceFilterTypeDef",
    {
        "Name": Literal["resource-type"],
        "Values": List[str],
    },
)

ResourceIdentifierTypeDef = TypedDict(
    "ResourceIdentifierTypeDef",
    {
        "ResourceArn": str,
        "ResourceType": str,
    },
    total=False,
)

ResourceQueryTypeDef = TypedDict(
    "ResourceQueryTypeDef",
    {
        "Type": QueryTypeType,
        "Query": str,
    },
)

ResourceStatusTypeDef = TypedDict(
    "ResourceStatusTypeDef",
    {
        "Name": Literal["PENDING"],
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

_RequiredSearchResourcesInputRequestTypeDef = TypedDict(
    "_RequiredSearchResourcesInputRequestTypeDef",
    {
        "ResourceQuery": "ResourceQueryTypeDef",
    },
)
_OptionalSearchResourcesInputRequestTypeDef = TypedDict(
    "_OptionalSearchResourcesInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class SearchResourcesInputRequestTypeDef(
    _RequiredSearchResourcesInputRequestTypeDef, _OptionalSearchResourcesInputRequestTypeDef
):
    pass

SearchResourcesOutputTypeDef = TypedDict(
    "SearchResourcesOutputTypeDef",
    {
        "ResourceIdentifiers": List["ResourceIdentifierTypeDef"],
        "NextToken": str,
        "QueryErrors": List["QueryErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagInputRequestTypeDef = TypedDict(
    "TagInputRequestTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
    },
)

TagOutputTypeDef = TypedDict(
    "TagOutputTypeDef",
    {
        "Arn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UngroupResourcesInputRequestTypeDef = TypedDict(
    "UngroupResourcesInputRequestTypeDef",
    {
        "Group": str,
        "ResourceArns": List[str],
    },
)

UngroupResourcesOutputTypeDef = TypedDict(
    "UngroupResourcesOutputTypeDef",
    {
        "Succeeded": List[str],
        "Failed": List["FailedResourceTypeDef"],
        "Pending": List["PendingResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagInputRequestTypeDef = TypedDict(
    "UntagInputRequestTypeDef",
    {
        "Arn": str,
        "Keys": List[str],
    },
)

UntagOutputTypeDef = TypedDict(
    "UntagOutputTypeDef",
    {
        "Arn": str,
        "Keys": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGroupInputRequestTypeDef = TypedDict(
    "UpdateGroupInputRequestTypeDef",
    {
        "GroupName": str,
        "Group": str,
        "Description": str,
    },
    total=False,
)

UpdateGroupOutputTypeDef = TypedDict(
    "UpdateGroupOutputTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGroupQueryInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGroupQueryInputRequestTypeDef",
    {
        "ResourceQuery": "ResourceQueryTypeDef",
    },
)
_OptionalUpdateGroupQueryInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGroupQueryInputRequestTypeDef",
    {
        "GroupName": str,
        "Group": str,
    },
    total=False,
)

class UpdateGroupQueryInputRequestTypeDef(
    _RequiredUpdateGroupQueryInputRequestTypeDef, _OptionalUpdateGroupQueryInputRequestTypeDef
):
    pass

UpdateGroupQueryOutputTypeDef = TypedDict(
    "UpdateGroupQueryOutputTypeDef",
    {
        "GroupQuery": "GroupQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
