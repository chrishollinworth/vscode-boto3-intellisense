"""
Type annotations for kendra-ranking service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra_ranking/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kendra_ranking.type_defs import CapacityUnitsConfigurationTypeDef

    data: CapacityUnitsConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import RescoreExecutionPlanStatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "CapacityUnitsConfigurationTypeDef",
    "CreateRescoreExecutionPlanRequestRequestTypeDef",
    "CreateRescoreExecutionPlanResponseTypeDef",
    "DeleteRescoreExecutionPlanRequestRequestTypeDef",
    "DescribeRescoreExecutionPlanRequestRequestTypeDef",
    "DescribeRescoreExecutionPlanResponseTypeDef",
    "DocumentTypeDef",
    "ListRescoreExecutionPlansRequestRequestTypeDef",
    "ListRescoreExecutionPlansResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RescoreExecutionPlanSummaryTypeDef",
    "RescoreRequestRequestTypeDef",
    "RescoreResultItemTypeDef",
    "RescoreResultTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRescoreExecutionPlanRequestRequestTypeDef",
)

CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef",
    {
        "RescoreCapacityUnits": int,
    },
)

_RequiredCreateRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Description": str,
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateRescoreExecutionPlanRequestRequestTypeDef(
    _RequiredCreateRescoreExecutionPlanRequestRequestTypeDef,
    _OptionalCreateRescoreExecutionPlanRequestRequestTypeDef,
):
    pass

CreateRescoreExecutionPlanResponseTypeDef = TypedDict(
    "CreateRescoreExecutionPlanResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "DeleteRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "DescribeRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeRescoreExecutionPlanResponseTypeDef = TypedDict(
    "DescribeRescoreExecutionPlanResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": RescoreExecutionPlanStatusType,
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDocumentTypeDef = TypedDict(
    "_RequiredDocumentTypeDef",
    {
        "Id": str,
        "OriginalScore": float,
    },
)
_OptionalDocumentTypeDef = TypedDict(
    "_OptionalDocumentTypeDef",
    {
        "GroupId": str,
        "Title": str,
        "Body": str,
        "TokenizedTitle": List[str],
        "TokenizedBody": List[str],
    },
    total=False,
)

class DocumentTypeDef(_RequiredDocumentTypeDef, _OptionalDocumentTypeDef):
    pass

ListRescoreExecutionPlansRequestRequestTypeDef = TypedDict(
    "ListRescoreExecutionPlansRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

ListRescoreExecutionPlansResponseTypeDef = TypedDict(
    "ListRescoreExecutionPlansResponseTypeDef",
    {
        "SummaryItems": List["RescoreExecutionPlanSummaryTypeDef"],
        "NextToken": str,
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

RescoreExecutionPlanSummaryTypeDef = TypedDict(
    "RescoreExecutionPlanSummaryTypeDef",
    {
        "Name": str,
        "Id": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": RescoreExecutionPlanStatusType,
    },
    total=False,
)

RescoreRequestRequestTypeDef = TypedDict(
    "RescoreRequestRequestTypeDef",
    {
        "RescoreExecutionPlanId": str,
        "SearchQuery": str,
        "Documents": List["DocumentTypeDef"],
    },
)

RescoreResultItemTypeDef = TypedDict(
    "RescoreResultItemTypeDef",
    {
        "DocumentId": str,
        "Score": float,
    },
    total=False,
)

RescoreResultTypeDef = TypedDict(
    "RescoreResultTypeDef",
    {
        "RescoreId": str,
        "ResultItems": List["RescoreResultItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

_RequiredUpdateRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Id": str,
    },
)
_OptionalUpdateRescoreExecutionPlanRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRescoreExecutionPlanRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
    },
    total=False,
)

class UpdateRescoreExecutionPlanRequestRequestTypeDef(
    _RequiredUpdateRescoreExecutionPlanRequestRequestTypeDef,
    _OptionalUpdateRescoreExecutionPlanRequestRequestTypeDef,
):
    pass
