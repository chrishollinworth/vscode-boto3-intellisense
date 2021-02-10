"""
Main interface for servicecatalog-appregistry service type definitions.

Usage::

    ```python
    from mypy_boto3_servicecatalog_appregistry.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "AttributeGroupSummaryTypeDef",
    "AttributeGroupTypeDef",
    "ResourceInfoTypeDef",
    "AssociateAttributeGroupResponseTypeDef",
    "AssociateResourceResponseTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateAttributeGroupResponseTypeDef",
    "DeleteApplicationResponseTypeDef",
    "DeleteAttributeGroupResponseTypeDef",
    "DisassociateAttributeGroupResponseTypeDef",
    "DisassociateResourceResponseTypeDef",
    "GetApplicationResponseTypeDef",
    "GetAttributeGroupResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListAssociatedAttributeGroupsResponseTypeDef",
    "ListAssociatedResourcesResponseTypeDef",
    "ListAttributeGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "SyncResourceResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateAttributeGroupResponseTypeDef",
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

AttributeGroupSummaryTypeDef = TypedDict(
    "AttributeGroupSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

AttributeGroupTypeDef = TypedDict(
    "AttributeGroupTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ResourceInfoTypeDef = TypedDict("ResourceInfoTypeDef", {"name": str, "arn": str}, total=False)

AssociateAttributeGroupResponseTypeDef = TypedDict(
    "AssociateAttributeGroupResponseTypeDef",
    {"applicationArn": str, "attributeGroupArn": str},
    total=False,
)

AssociateResourceResponseTypeDef = TypedDict(
    "AssociateResourceResponseTypeDef", {"applicationArn": str, "resourceArn": str}, total=False
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef", {"application": "ApplicationTypeDef"}, total=False
)

CreateAttributeGroupResponseTypeDef = TypedDict(
    "CreateAttributeGroupResponseTypeDef", {"attributeGroup": "AttributeGroupTypeDef"}, total=False
)

DeleteApplicationResponseTypeDef = TypedDict(
    "DeleteApplicationResponseTypeDef", {"application": "ApplicationSummaryTypeDef"}, total=False
)

DeleteAttributeGroupResponseTypeDef = TypedDict(
    "DeleteAttributeGroupResponseTypeDef",
    {"attributeGroup": "AttributeGroupSummaryTypeDef"},
    total=False,
)

DisassociateAttributeGroupResponseTypeDef = TypedDict(
    "DisassociateAttributeGroupResponseTypeDef",
    {"applicationArn": str, "attributeGroupArn": str},
    total=False,
)

DisassociateResourceResponseTypeDef = TypedDict(
    "DisassociateResourceResponseTypeDef", {"applicationArn": str, "resourceArn": str}, total=False
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "associatedResourceCount": int,
        "tags": Dict[str, str],
    },
    total=False,
)

GetAttributeGroupResponseTypeDef = TypedDict(
    "GetAttributeGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "attributes": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {"applications": List["ApplicationSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListAssociatedAttributeGroupsResponseTypeDef = TypedDict(
    "ListAssociatedAttributeGroupsResponseTypeDef",
    {"attributeGroups": List[str], "nextToken": str},
    total=False,
)

ListAssociatedResourcesResponseTypeDef = TypedDict(
    "ListAssociatedResourcesResponseTypeDef",
    {"resources": List["ResourceInfoTypeDef"], "nextToken": str},
    total=False,
)

ListAttributeGroupsResponseTypeDef = TypedDict(
    "ListAttributeGroupsResponseTypeDef",
    {"attributeGroups": List["AttributeGroupSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SyncResourceResponseTypeDef = TypedDict(
    "SyncResourceResponseTypeDef",
    {"applicationArn": str, "resourceArn": str, "actionTaken": Literal["START_SYNC", "NO_ACTION"]},
    total=False,
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef", {"application": "ApplicationTypeDef"}, total=False
)

UpdateAttributeGroupResponseTypeDef = TypedDict(
    "UpdateAttributeGroupResponseTypeDef", {"attributeGroup": "AttributeGroupTypeDef"}, total=False
)
