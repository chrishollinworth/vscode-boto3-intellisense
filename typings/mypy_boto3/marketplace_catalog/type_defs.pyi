"""
Type annotations for marketplace-catalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import CancelChangeSetRequestRequestTypeDef

    data: CancelChangeSetRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from .literals import ChangeStatusType, FailureCodeType, OwnershipTypeType, SortOrderType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelChangeSetRequestRequestTypeDef",
    "CancelChangeSetResponseTypeDef",
    "ChangeSetSummaryListItemTypeDef",
    "ChangeSummaryTypeDef",
    "ChangeTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DescribeChangeSetRequestRequestTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "DescribeEntityRequestRequestTypeDef",
    "DescribeEntityResponseTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeDef",
    "ErrorDetailTypeDef",
    "FilterTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListChangeSetsRequestRequestTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ListEntitiesRequestRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SortTypeDef",
    "StartChangeSetRequestRequestTypeDef",
    "StartChangeSetResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

CancelChangeSetRequestRequestTypeDef = TypedDict(
    "CancelChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

CancelChangeSetResponseTypeDef = TypedDict(
    "CancelChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeSetSummaryListItemTypeDef = TypedDict(
    "ChangeSetSummaryListItemTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "EntityIdList": List[str],
        "FailureCode": FailureCodeType,
    },
    total=False,
)

ChangeSummaryTypeDef = TypedDict(
    "ChangeSummaryTypeDef",
    {
        "ChangeType": str,
        "Entity": "EntityTypeDef",
        "Details": str,
        "DetailsDocument": Dict[str, Any],
        "ErrorDetailList": List["ErrorDetailTypeDef"],
        "ChangeName": str,
    },
    total=False,
)

_RequiredChangeTypeDef = TypedDict(
    "_RequiredChangeTypeDef",
    {
        "ChangeType": str,
        "Entity": "EntityTypeDef",
    },
)
_OptionalChangeTypeDef = TypedDict(
    "_OptionalChangeTypeDef",
    {
        "EntityTags": List["TagTypeDef"],
        "Details": str,
        "DetailsDocument": Dict[str, Any],
        "ChangeName": str,
    },
    total=False,
)

class ChangeTypeDef(_RequiredChangeTypeDef, _OptionalChangeTypeDef):
    pass

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeChangeSetRequestRequestTypeDef = TypedDict(
    "DescribeChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

DescribeChangeSetResponseTypeDef = TypedDict(
    "DescribeChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "FailureCode": FailureCodeType,
        "FailureDescription": str,
        "ChangeSet": List["ChangeSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityRequestRequestTypeDef = TypedDict(
    "DescribeEntityRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityId": str,
    },
)

DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
        "DetailsDocument": Dict[str, Any],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntitySummaryTypeDef = TypedDict(
    "EntitySummaryTypeDef",
    {
        "Name": str,
        "EntityType": str,
        "EntityId": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Visibility": str,
    },
    total=False,
)

_RequiredEntityTypeDef = TypedDict(
    "_RequiredEntityTypeDef",
    {
        "Type": str,
    },
)
_OptionalEntityTypeDef = TypedDict(
    "_OptionalEntityTypeDef",
    {
        "Identifier": str,
    },
    total=False,
)

class EntityTypeDef(_RequiredEntityTypeDef, _OptionalEntityTypeDef):
    pass

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "ValueList": List[str],
    },
    total=False,
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListChangeSetsRequestRequestTypeDef = TypedDict(
    "_RequiredListChangeSetsRequestRequestTypeDef",
    {
        "Catalog": str,
    },
)
_OptionalListChangeSetsRequestRequestTypeDef = TypedDict(
    "_OptionalListChangeSetsRequestRequestTypeDef",
    {
        "FilterList": List["FilterTypeDef"],
        "Sort": "SortTypeDef",
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class ListChangeSetsRequestRequestTypeDef(
    _RequiredListChangeSetsRequestRequestTypeDef, _OptionalListChangeSetsRequestRequestTypeDef
):
    pass

ListChangeSetsResponseTypeDef = TypedDict(
    "ListChangeSetsResponseTypeDef",
    {
        "ChangeSetSummaryList": List["ChangeSetSummaryListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListEntitiesRequestRequestTypeDef = TypedDict(
    "_RequiredListEntitiesRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityType": str,
    },
)
_OptionalListEntitiesRequestRequestTypeDef = TypedDict(
    "_OptionalListEntitiesRequestRequestTypeDef",
    {
        "FilterList": List["FilterTypeDef"],
        "Sort": "SortTypeDef",
        "NextToken": str,
        "MaxResults": int,
        "OwnershipType": OwnershipTypeType,
    },
    total=False,
)

class ListEntitiesRequestRequestTypeDef(
    _RequiredListEntitiesRequestRequestTypeDef, _OptionalListEntitiesRequestRequestTypeDef
):
    pass

ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "EntitySummaryList": List["EntitySummaryTypeDef"],
        "NextToken": str,
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
        "ResourceArn": str,
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

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Policy": str,
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

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "SortBy": str,
        "SortOrder": SortOrderType,
    },
    total=False,
)

_RequiredStartChangeSetRequestRequestTypeDef = TypedDict(
    "_RequiredStartChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSet": List["ChangeTypeDef"],
    },
)
_OptionalStartChangeSetRequestRequestTypeDef = TypedDict(
    "_OptionalStartChangeSetRequestRequestTypeDef",
    {
        "ChangeSetName": str,
        "ClientRequestToken": str,
        "ChangeSetTags": List["TagTypeDef"],
    },
    total=False,
)

class StartChangeSetRequestRequestTypeDef(
    _RequiredStartChangeSetRequestRequestTypeDef, _OptionalStartChangeSetRequestRequestTypeDef
):
    pass

StartChangeSetResponseTypeDef = TypedDict(
    "StartChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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
        "ResourceArn": str,
        "TagKeys": List[str],
    },
)
