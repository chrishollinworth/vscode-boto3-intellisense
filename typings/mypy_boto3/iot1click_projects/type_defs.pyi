"""
Type annotations for iot1click-projects service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot1click_projects.type_defs import AssociateDeviceWithPlacementRequestRequestTypeDef

    data: AssociateDeviceWithPlacementRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AssociateDeviceWithPlacementRequestRequestTypeDef",
    "CreatePlacementRequestRequestTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "DeletePlacementRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DescribePlacementRequestRequestTypeDef",
    "DescribePlacementResponseTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DeviceTemplateTypeDef",
    "DisassociateDeviceFromPlacementRequestRequestTypeDef",
    "GetDevicesInPlacementRequestRequestTypeDef",
    "GetDevicesInPlacementResponseTypeDef",
    "ListPlacementsRequestRequestTypeDef",
    "ListPlacementsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementDescriptionTypeDef",
    "PlacementSummaryTypeDef",
    "PlacementTemplateTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePlacementRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
)

AssociateDeviceWithPlacementRequestRequestTypeDef = TypedDict(
    "AssociateDeviceWithPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceId": str,
        "deviceTemplateName": str,
    },
)

_RequiredCreatePlacementRequestRequestTypeDef = TypedDict(
    "_RequiredCreatePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)
_OptionalCreatePlacementRequestRequestTypeDef = TypedDict(
    "_OptionalCreatePlacementRequestRequestTypeDef",
    {
        "attributes": Dict[str, str],
    },
    total=False,
)

class CreatePlacementRequestRequestTypeDef(
    _RequiredCreatePlacementRequestRequestTypeDef, _OptionalCreatePlacementRequestRequestTypeDef
):
    pass

_RequiredCreateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalCreateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateProjectRequestRequestTypeDef",
    {
        "description": str,
        "placementTemplate": "PlacementTemplateTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class CreateProjectRequestRequestTypeDef(
    _RequiredCreateProjectRequestRequestTypeDef, _OptionalCreateProjectRequestRequestTypeDef
):
    pass

DeletePlacementRequestRequestTypeDef = TypedDict(
    "DeletePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)

DescribePlacementRequestRequestTypeDef = TypedDict(
    "DescribePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)

DescribePlacementResponseTypeDef = TypedDict(
    "DescribePlacementResponseTypeDef",
    {
        "placement": "PlacementDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "project": "ProjectDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceTemplateTypeDef = TypedDict(
    "DeviceTemplateTypeDef",
    {
        "deviceType": str,
        "callbackOverrides": Dict[str, str],
    },
    total=False,
)

DisassociateDeviceFromPlacementRequestRequestTypeDef = TypedDict(
    "DisassociateDeviceFromPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceTemplateName": str,
    },
)

GetDevicesInPlacementRequestRequestTypeDef = TypedDict(
    "GetDevicesInPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
    },
)

GetDevicesInPlacementResponseTypeDef = TypedDict(
    "GetDevicesInPlacementResponseTypeDef",
    {
        "devices": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListPlacementsRequestRequestTypeDef = TypedDict(
    "_RequiredListPlacementsRequestRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalListPlacementsRequestRequestTypeDef = TypedDict(
    "_OptionalListPlacementsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

class ListPlacementsRequestRequestTypeDef(
    _RequiredListPlacementsRequestRequestTypeDef, _OptionalListPlacementsRequestRequestTypeDef
):
    pass

ListPlacementsResponseTypeDef = TypedDict(
    "ListPlacementsResponseTypeDef",
    {
        "placements": List["PlacementSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "nextToken": str,
        "maxResults": int,
    },
    total=False,
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
        "nextToken": str,
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

PlacementDescriptionTypeDef = TypedDict(
    "PlacementDescriptionTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)

PlacementSummaryTypeDef = TypedDict(
    "PlacementSummaryTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)

PlacementTemplateTypeDef = TypedDict(
    "PlacementTemplateTypeDef",
    {
        "defaultAttributes": Dict[str, str],
        "deviceTemplates": Dict[str, "DeviceTemplateTypeDef"],
    },
    total=False,
)

_RequiredProjectDescriptionTypeDef = TypedDict(
    "_RequiredProjectDescriptionTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)
_OptionalProjectDescriptionTypeDef = TypedDict(
    "_OptionalProjectDescriptionTypeDef",
    {
        "arn": str,
        "description": str,
        "placementTemplate": "PlacementTemplateTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)

class ProjectDescriptionTypeDef(
    _RequiredProjectDescriptionTypeDef, _OptionalProjectDescriptionTypeDef
):
    pass

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {
        "arn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass

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

_RequiredUpdatePlacementRequestRequestTypeDef = TypedDict(
    "_RequiredUpdatePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)
_OptionalUpdatePlacementRequestRequestTypeDef = TypedDict(
    "_OptionalUpdatePlacementRequestRequestTypeDef",
    {
        "attributes": Dict[str, str],
    },
    total=False,
)

class UpdatePlacementRequestRequestTypeDef(
    _RequiredUpdatePlacementRequestRequestTypeDef, _OptionalUpdatePlacementRequestRequestTypeDef
):
    pass

_RequiredUpdateProjectRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)
_OptionalUpdateProjectRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateProjectRequestRequestTypeDef",
    {
        "description": str,
        "placementTemplate": "PlacementTemplateTypeDef",
    },
    total=False,
)

class UpdateProjectRequestRequestTypeDef(
    _RequiredUpdateProjectRequestRequestTypeDef, _OptionalUpdateProjectRequestRequestTypeDef
):
    pass
