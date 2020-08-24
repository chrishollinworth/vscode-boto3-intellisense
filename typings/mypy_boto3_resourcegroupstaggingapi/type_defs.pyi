"""
Main interface for resourcegroupstaggingapi service type definitions.

Usage::

    ```python
    from mypy_boto3_resourcegroupstaggingapi.type_defs import ComplianceDetailsTypeDef

    data: ComplianceDetailsTypeDef = {...}
    ```
"""
import sys
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
    "ComplianceDetailsTypeDef",
    "FailureInfoTypeDef",
    "ResourceTagMappingTypeDef",
    "SummaryTypeDef",
    "TagTypeDef",
    "DescribeReportCreationOutputTypeDef",
    "GetComplianceSummaryOutputTypeDef",
    "GetResourcesOutputTypeDef",
    "GetTagKeysOutputTypeDef",
    "GetTagValuesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "TagFilterTypeDef",
    "TagResourcesOutputTypeDef",
    "UntagResourcesOutputTypeDef",
)

ComplianceDetailsTypeDef = TypedDict(
    "ComplianceDetailsTypeDef",
    {
        "NoncompliantKeys": List[str],
        "KeysWithNoncompliantValues": List[str],
        "ComplianceStatus": bool,
    },
    total=False,
)

FailureInfoTypeDef = TypedDict(
    "FailureInfoTypeDef",
    {
        "StatusCode": int,
        "ErrorCode": Literal["InternalServiceException", "InvalidParameterException"],
        "ErrorMessage": str,
    },
    total=False,
)

ResourceTagMappingTypeDef = TypedDict(
    "ResourceTagMappingTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
        "ComplianceDetails": "ComplianceDetailsTypeDef",
    },
    total=False,
)

SummaryTypeDef = TypedDict(
    "SummaryTypeDef",
    {
        "LastUpdated": str,
        "TargetId": str,
        "TargetIdType": Literal["ACCOUNT", "OU", "ROOT"],
        "Region": str,
        "ResourceType": str,
        "NonCompliantResources": int,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

DescribeReportCreationOutputTypeDef = TypedDict(
    "DescribeReportCreationOutputTypeDef",
    {"Status": str, "S3Location": str, "ErrorMessage": str},
    total=False,
)

GetComplianceSummaryOutputTypeDef = TypedDict(
    "GetComplianceSummaryOutputTypeDef",
    {"SummaryList": List["SummaryTypeDef"], "PaginationToken": str},
    total=False,
)

GetResourcesOutputTypeDef = TypedDict(
    "GetResourcesOutputTypeDef",
    {"PaginationToken": str, "ResourceTagMappingList": List["ResourceTagMappingTypeDef"]},
    total=False,
)

GetTagKeysOutputTypeDef = TypedDict(
    "GetTagKeysOutputTypeDef", {"PaginationToken": str, "TagKeys": List[str]}, total=False
)

GetTagValuesOutputTypeDef = TypedDict(
    "GetTagValuesOutputTypeDef", {"PaginationToken": str, "TagValues": List[str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"Key": str, "Values": List[str]}, total=False)

TagResourcesOutputTypeDef = TypedDict(
    "TagResourcesOutputTypeDef",
    {"FailedResourcesMap": Dict[str, "FailureInfoTypeDef"]},
    total=False,
)

UntagResourcesOutputTypeDef = TypedDict(
    "UntagResourcesOutputTypeDef",
    {"FailedResourcesMap": Dict[str, "FailureInfoTypeDef"]},
    total=False,
)
