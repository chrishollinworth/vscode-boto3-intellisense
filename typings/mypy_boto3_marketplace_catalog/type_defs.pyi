"""
Main interface for marketplace-catalog service type definitions.

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import ChangeSetSummaryListItemTypeDef

    data: ChangeSetSummaryListItemTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChangeSetSummaryListItemTypeDef",
    "ChangeSummaryTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeDef",
    "ErrorDetailTypeDef",
    "CancelChangeSetResponseTypeDef",
    "ChangeTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "DescribeEntityResponseTypeDef",
    "FilterTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ListEntitiesResponseTypeDef",
    "SortTypeDef",
    "StartChangeSetResponseTypeDef",
)

ChangeSetSummaryListItemTypeDef = TypedDict(
    "ChangeSetSummaryListItemTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": Literal["PREPARING", "APPLYING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "EntityIdList": List[str],
    },
    total=False,
)

ChangeSummaryTypeDef = TypedDict(
    "ChangeSummaryTypeDef",
    {
        "ChangeType": str,
        "Entity": "EntityTypeDef",
        "Details": str,
        "ErrorDetailList": List["ErrorDetailTypeDef"],
    },
    total=False,
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

_RequiredEntityTypeDef = TypedDict("_RequiredEntityTypeDef", {"Type": str})
_OptionalEntityTypeDef = TypedDict("_OptionalEntityTypeDef", {"Identifier": str}, total=False)


class EntityTypeDef(_RequiredEntityTypeDef, _OptionalEntityTypeDef):
    pass


ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef", {"ErrorCode": str, "ErrorMessage": str}, total=False
)

CancelChangeSetResponseTypeDef = TypedDict(
    "CancelChangeSetResponseTypeDef", {"ChangeSetId": str, "ChangeSetArn": str}, total=False
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef", {"ChangeType": str, "Entity": "EntityTypeDef", "Details": str}
)

DescribeChangeSetResponseTypeDef = TypedDict(
    "DescribeChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": Literal["PREPARING", "APPLYING", "SUCCEEDED", "CANCELLED", "FAILED"],
        "FailureDescription": str,
        "ChangeSet": List["ChangeSummaryTypeDef"],
    },
    total=False,
)

DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
    },
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "ValueList": List[str]}, total=False)

ListChangeSetsResponseTypeDef = TypedDict(
    "ListChangeSetsResponseTypeDef",
    {"ChangeSetSummaryList": List["ChangeSetSummaryListItemTypeDef"], "NextToken": str},
    total=False,
)

ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {"EntitySummaryList": List["EntitySummaryTypeDef"], "NextToken": str},
    total=False,
)

SortTypeDef = TypedDict(
    "SortTypeDef", {"SortBy": str, "SortOrder": Literal["ASCENDING", "DESCENDING"]}, total=False
)

StartChangeSetResponseTypeDef = TypedDict(
    "StartChangeSetResponseTypeDef", {"ChangeSetId": str, "ChangeSetArn": str}, total=False
)
