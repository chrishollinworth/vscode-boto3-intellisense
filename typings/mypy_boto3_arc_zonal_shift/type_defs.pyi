"""
Type annotations for arc-zonal-shift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_arc_zonal_shift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_arc_zonal_shift.type_defs import CancelZonalShiftRequestRequestTypeDef

    data: CancelZonalShiftRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import AppliedStatusType, ZonalShiftStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CancelZonalShiftRequestRequestTypeDef",
    "GetManagedResourceRequestRequestTypeDef",
    "GetManagedResourceResponseTypeDef",
    "ListManagedResourcesRequestRequestTypeDef",
    "ListManagedResourcesResponseTypeDef",
    "ListZonalShiftsRequestRequestTypeDef",
    "ListZonalShiftsResponseTypeDef",
    "ManagedResourceSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "StartZonalShiftRequestRequestTypeDef",
    "UpdateZonalShiftRequestRequestTypeDef",
    "ZonalShiftInResourceTypeDef",
    "ZonalShiftSummaryTypeDef",
    "ZonalShiftTypeDef",
)

CancelZonalShiftRequestRequestTypeDef = TypedDict(
    "CancelZonalShiftRequestRequestTypeDef",
    {
        "zonalShiftId": str,
    },
)

GetManagedResourceRequestRequestTypeDef = TypedDict(
    "GetManagedResourceRequestRequestTypeDef",
    {
        "resourceIdentifier": str,
    },
)

GetManagedResourceResponseTypeDef = TypedDict(
    "GetManagedResourceResponseTypeDef",
    {
        "appliedWeights": Dict[str, float],
        "arn": str,
        "name": str,
        "zonalShifts": List["ZonalShiftInResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListManagedResourcesRequestRequestTypeDef = TypedDict(
    "ListManagedResourcesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListManagedResourcesResponseTypeDef = TypedDict(
    "ListManagedResourcesResponseTypeDef",
    {
        "items": List["ManagedResourceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListZonalShiftsRequestRequestTypeDef = TypedDict(
    "ListZonalShiftsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "status": ZonalShiftStatusType,
    },
    total=False,
)

ListZonalShiftsResponseTypeDef = TypedDict(
    "ListZonalShiftsResponseTypeDef",
    {
        "items": List["ZonalShiftSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredManagedResourceSummaryTypeDef = TypedDict(
    "_RequiredManagedResourceSummaryTypeDef",
    {
        "availabilityZones": List[str],
    },
)
_OptionalManagedResourceSummaryTypeDef = TypedDict(
    "_OptionalManagedResourceSummaryTypeDef",
    {
        "arn": str,
        "name": str,
    },
    total=False,
)

class ManagedResourceSummaryTypeDef(
    _RequiredManagedResourceSummaryTypeDef, _OptionalManagedResourceSummaryTypeDef
):
    pass

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

StartZonalShiftRequestRequestTypeDef = TypedDict(
    "StartZonalShiftRequestRequestTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiresIn": str,
        "resourceIdentifier": str,
    },
)

_RequiredUpdateZonalShiftRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateZonalShiftRequestRequestTypeDef",
    {
        "zonalShiftId": str,
    },
)
_OptionalUpdateZonalShiftRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateZonalShiftRequestRequestTypeDef",
    {
        "comment": str,
        "expiresIn": str,
    },
    total=False,
)

class UpdateZonalShiftRequestRequestTypeDef(
    _RequiredUpdateZonalShiftRequestRequestTypeDef, _OptionalUpdateZonalShiftRequestRequestTypeDef
):
    pass

ZonalShiftInResourceTypeDef = TypedDict(
    "ZonalShiftInResourceTypeDef",
    {
        "appliedStatus": AppliedStatusType,
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "zonalShiftId": str,
    },
)

ZonalShiftSummaryTypeDef = TypedDict(
    "ZonalShiftSummaryTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "status": ZonalShiftStatusType,
        "zonalShiftId": str,
    },
)

ZonalShiftTypeDef = TypedDict(
    "ZonalShiftTypeDef",
    {
        "awayFrom": str,
        "comment": str,
        "expiryTime": datetime,
        "resourceIdentifier": str,
        "startTime": datetime,
        "status": ZonalShiftStatusType,
        "zonalShiftId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
