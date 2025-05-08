"""
Type annotations for resourcegroupstaggingapi service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_resourcegroupstaggingapi.type_defs import ComplianceDetailsTypeDef

    data: ComplianceDetailsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys

from .literals import ErrorCodeType, GroupByAttributeType, TargetIdTypeType

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Mapping, Sequence
else:
    from typing import Dict, List, Mapping, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "ComplianceDetailsTypeDef",
    "DescribeReportCreationOutputTypeDef",
    "FailureInfoTypeDef",
    "GetComplianceSummaryInputPaginateTypeDef",
    "GetComplianceSummaryInputTypeDef",
    "GetComplianceSummaryOutputTypeDef",
    "GetResourcesInputPaginateTypeDef",
    "GetResourcesInputTypeDef",
    "GetResourcesOutputTypeDef",
    "GetTagKeysInputPaginateTypeDef",
    "GetTagKeysInputTypeDef",
    "GetTagKeysOutputTypeDef",
    "GetTagValuesInputPaginateTypeDef",
    "GetTagValuesInputTypeDef",
    "GetTagValuesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagMappingTypeDef",
    "ResponseMetadataTypeDef",
    "StartReportCreationInputTypeDef",
    "SummaryTypeDef",
    "TagFilterTypeDef",
    "TagResourcesInputTypeDef",
    "TagResourcesOutputTypeDef",
    "TagTypeDef",
    "UntagResourcesInputTypeDef",
    "UntagResourcesOutputTypeDef",
)

class ComplianceDetailsTypeDef(TypedDict):
    NoncompliantKeys: NotRequired[List[str]]
    KeysWithNoncompliantValues: NotRequired[List[str]]
    ComplianceStatus: NotRequired[bool]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class FailureInfoTypeDef(TypedDict):
    StatusCode: NotRequired[int]
    ErrorCode: NotRequired[ErrorCodeType]
    ErrorMessage: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class GetComplianceSummaryInputTypeDef(TypedDict):
    TargetIdFilters: NotRequired[Sequence[str]]
    RegionFilters: NotRequired[Sequence[str]]
    ResourceTypeFilters: NotRequired[Sequence[str]]
    TagKeyFilters: NotRequired[Sequence[str]]
    GroupBy: NotRequired[Sequence[GroupByAttributeType]]
    MaxResults: NotRequired[int]
    PaginationToken: NotRequired[str]

class SummaryTypeDef(TypedDict):
    LastUpdated: NotRequired[str]
    TargetId: NotRequired[str]
    TargetIdType: NotRequired[TargetIdTypeType]
    Region: NotRequired[str]
    ResourceType: NotRequired[str]
    NonCompliantResources: NotRequired[int]

class TagFilterTypeDef(TypedDict):
    Key: NotRequired[str]
    Values: NotRequired[Sequence[str]]

class GetTagKeysInputTypeDef(TypedDict):
    PaginationToken: NotRequired[str]

class GetTagValuesInputTypeDef(TypedDict):
    Key: str
    PaginationToken: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class StartReportCreationInputTypeDef(TypedDict):
    S3Bucket: str

class TagResourcesInputTypeDef(TypedDict):
    ResourceARNList: Sequence[str]
    Tags: Mapping[str, str]

class UntagResourcesInputTypeDef(TypedDict):
    ResourceARNList: Sequence[str]
    TagKeys: Sequence[str]

class DescribeReportCreationOutputTypeDef(TypedDict):
    Status: str
    S3Location: str
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagKeysOutputTypeDef(TypedDict):
    TagKeys: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]

class GetTagValuesOutputTypeDef(TypedDict):
    TagValues: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]

class TagResourcesOutputTypeDef(TypedDict):
    FailedResourcesMap: Dict[str, FailureInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourcesOutputTypeDef(TypedDict):
    FailedResourcesMap: Dict[str, FailureInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetComplianceSummaryInputPaginateTypeDef(TypedDict):
    TargetIdFilters: NotRequired[Sequence[str]]
    RegionFilters: NotRequired[Sequence[str]]
    ResourceTypeFilters: NotRequired[Sequence[str]]
    TagKeyFilters: NotRequired[Sequence[str]]
    GroupBy: NotRequired[Sequence[GroupByAttributeType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTagKeysInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetTagValuesInputPaginateTypeDef(TypedDict):
    Key: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetComplianceSummaryOutputTypeDef(TypedDict):
    SummaryList: List[SummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]

class GetResourcesInputPaginateTypeDef(TypedDict):
    TagFilters: NotRequired[Sequence[TagFilterTypeDef]]
    TagsPerPage: NotRequired[int]
    ResourceTypeFilters: NotRequired[Sequence[str]]
    IncludeComplianceDetails: NotRequired[bool]
    ExcludeCompliantResources: NotRequired[bool]
    ResourceARNList: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class GetResourcesInputTypeDef(TypedDict):
    PaginationToken: NotRequired[str]
    TagFilters: NotRequired[Sequence[TagFilterTypeDef]]
    ResourcesPerPage: NotRequired[int]
    TagsPerPage: NotRequired[int]
    ResourceTypeFilters: NotRequired[Sequence[str]]
    IncludeComplianceDetails: NotRequired[bool]
    ExcludeCompliantResources: NotRequired[bool]
    ResourceARNList: NotRequired[Sequence[str]]

class ResourceTagMappingTypeDef(TypedDict):
    ResourceARN: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    ComplianceDetails: NotRequired[ComplianceDetailsTypeDef]

class GetResourcesOutputTypeDef(TypedDict):
    ResourceTagMappingList: List[ResourceTagMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    PaginationToken: NotRequired[str]
