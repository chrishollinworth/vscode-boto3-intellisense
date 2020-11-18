"""
Main interface for resourcegroupstaggingapi service type definitions.

Usage::

    ```python
    from mypy_boto3_resourcegroupstaggingapi.type_defs import ComplianceDetailsTypeDef

    data: ComplianceDetailsTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

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
    "ResponseMetadata",
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

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
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
    {"Status": str, "S3Location": str, "ErrorMessage": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetComplianceSummaryOutputTypeDef = TypedDict(
    "GetComplianceSummaryOutputTypeDef",
    {
        "SummaryList": List["SummaryTypeDef"],
        "PaginationToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetResourcesOutputTypeDef = TypedDict(
    "GetResourcesOutputTypeDef",
    {
        "PaginationToken": str,
        "ResourceTagMappingList": List["ResourceTagMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetTagKeysOutputTypeDef = TypedDict(
    "GetTagKeysOutputTypeDef",
    {"PaginationToken": str, "TagKeys": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetTagValuesOutputTypeDef = TypedDict(
    "GetTagValuesOutputTypeDef",
    {"PaginationToken": str, "TagValues": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"Key": str, "Values": List[str]}, total=False)

TagResourcesOutputTypeDef = TypedDict(
    "TagResourcesOutputTypeDef",
    {"FailedResourcesMap": Dict[str, "FailureInfoTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UntagResourcesOutputTypeDef = TypedDict(
    "UntagResourcesOutputTypeDef",
    {"FailedResourcesMap": Dict[str, "FailureInfoTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)
