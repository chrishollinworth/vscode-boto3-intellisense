"""
Type annotations for backupsearch service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_backupsearch/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_backupsearch.type_defs import BackupCreationTimeFilterOutputTypeDef

    data: BackupCreationTimeFilterOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ExportJobStatusType,
    LongConditionOperatorType,
    ResourceTypeType,
    SearchJobStateType,
    StringConditionOperatorType,
    TimeConditionOperatorType,
)

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
    "BackupCreationTimeFilterOutputTypeDef",
    "BackupCreationTimeFilterTypeDef",
    "CurrentSearchProgressTypeDef",
    "EBSItemFilterOutputTypeDef",
    "EBSItemFilterTypeDef",
    "EBSResultItemTypeDef",
    "ExportJobSummaryTypeDef",
    "ExportSpecificationTypeDef",
    "GetSearchJobInputTypeDef",
    "GetSearchJobOutputTypeDef",
    "GetSearchResultExportJobInputTypeDef",
    "GetSearchResultExportJobOutputTypeDef",
    "ItemFiltersOutputTypeDef",
    "ItemFiltersTypeDef",
    "ItemFiltersUnionTypeDef",
    "ListSearchJobBackupsInputPaginateTypeDef",
    "ListSearchJobBackupsInputTypeDef",
    "ListSearchJobBackupsOutputTypeDef",
    "ListSearchJobResultsInputPaginateTypeDef",
    "ListSearchJobResultsInputTypeDef",
    "ListSearchJobResultsOutputTypeDef",
    "ListSearchJobsInputPaginateTypeDef",
    "ListSearchJobsInputTypeDef",
    "ListSearchJobsOutputTypeDef",
    "ListSearchResultExportJobsInputPaginateTypeDef",
    "ListSearchResultExportJobsInputTypeDef",
    "ListSearchResultExportJobsOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LongConditionTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ResultItemTypeDef",
    "S3ExportSpecificationTypeDef",
    "S3ItemFilterOutputTypeDef",
    "S3ItemFilterTypeDef",
    "S3ResultItemTypeDef",
    "SearchJobBackupsResultTypeDef",
    "SearchJobSummaryTypeDef",
    "SearchScopeOutputTypeDef",
    "SearchScopeSummaryTypeDef",
    "SearchScopeTypeDef",
    "SearchScopeUnionTypeDef",
    "StartSearchJobInputTypeDef",
    "StartSearchJobOutputTypeDef",
    "StartSearchResultExportJobInputTypeDef",
    "StartSearchResultExportJobOutputTypeDef",
    "StopSearchJobInputTypeDef",
    "StringConditionTypeDef",
    "TagResourceRequestTypeDef",
    "TimeConditionOutputTypeDef",
    "TimeConditionTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
)

class BackupCreationTimeFilterOutputTypeDef(TypedDict):
    CreatedAfter: NotRequired[datetime]
    CreatedBefore: NotRequired[datetime]

TimestampTypeDef = Union[datetime, str]

class CurrentSearchProgressTypeDef(TypedDict):
    RecoveryPointsScannedCount: NotRequired[int]
    ItemsScannedCount: NotRequired[int]
    ItemsMatchedCount: NotRequired[int]

class LongConditionTypeDef(TypedDict):
    Value: int
    Operator: NotRequired[LongConditionOperatorType]

class StringConditionTypeDef(TypedDict):
    Value: str
    Operator: NotRequired[StringConditionOperatorType]

class TimeConditionOutputTypeDef(TypedDict):
    Value: datetime
    Operator: NotRequired[TimeConditionOperatorType]

class EBSResultItemTypeDef(TypedDict):
    BackupResourceArn: NotRequired[str]
    SourceResourceArn: NotRequired[str]
    BackupVaultName: NotRequired[str]
    FileSystemIdentifier: NotRequired[str]
    FilePath: NotRequired[str]
    FileSize: NotRequired[int]
    CreationTime: NotRequired[datetime]
    LastModifiedTime: NotRequired[datetime]

class ExportJobSummaryTypeDef(TypedDict):
    ExportJobIdentifier: str
    ExportJobArn: NotRequired[str]
    Status: NotRequired[ExportJobStatusType]
    CreationTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    StatusMessage: NotRequired[str]
    SearchJobArn: NotRequired[str]

class S3ExportSpecificationTypeDef(TypedDict):
    DestinationBucket: str
    DestinationPrefix: NotRequired[str]

class GetSearchJobInputTypeDef(TypedDict):
    SearchJobIdentifier: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class SearchScopeSummaryTypeDef(TypedDict):
    TotalRecoveryPointsToScanCount: NotRequired[int]
    TotalItemsToScanCount: NotRequired[int]

class GetSearchResultExportJobInputTypeDef(TypedDict):
    ExportJobIdentifier: str

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListSearchJobBackupsInputTypeDef(TypedDict):
    SearchJobIdentifier: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class SearchJobBackupsResultTypeDef(TypedDict):
    Status: NotRequired[SearchJobStateType]
    StatusMessage: NotRequired[str]
    ResourceType: NotRequired[ResourceTypeType]
    BackupResourceArn: NotRequired[str]
    SourceResourceArn: NotRequired[str]
    IndexCreationTime: NotRequired[datetime]
    BackupCreationTime: NotRequired[datetime]

class ListSearchJobResultsInputTypeDef(TypedDict):
    SearchJobIdentifier: str
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSearchJobsInputTypeDef(TypedDict):
    ByStatus: NotRequired[SearchJobStateType]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListSearchResultExportJobsInputTypeDef(TypedDict):
    Status: NotRequired[ExportJobStatusType]
    SearchJobIdentifier: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceArn: str

class S3ResultItemTypeDef(TypedDict):
    BackupResourceArn: NotRequired[str]
    SourceResourceArn: NotRequired[str]
    BackupVaultName: NotRequired[str]
    ObjectKey: NotRequired[str]
    ObjectSize: NotRequired[int]
    CreationTime: NotRequired[datetime]
    ETag: NotRequired[str]
    VersionId: NotRequired[str]

class StopSearchJobInputTypeDef(TypedDict):
    SearchJobIdentifier: str

class TagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceArn: str
    TagKeys: Sequence[str]

class SearchScopeOutputTypeDef(TypedDict):
    BackupResourceTypes: List[ResourceTypeType]
    BackupResourceCreationTime: NotRequired[BackupCreationTimeFilterOutputTypeDef]
    SourceResourceArns: NotRequired[List[str]]
    BackupResourceArns: NotRequired[List[str]]
    BackupResourceTags: NotRequired[Dict[str, str]]

class BackupCreationTimeFilterTypeDef(TypedDict):
    CreatedAfter: NotRequired[TimestampTypeDef]
    CreatedBefore: NotRequired[TimestampTypeDef]

class TimeConditionTypeDef(TypedDict):
    Value: TimestampTypeDef
    Operator: NotRequired[TimeConditionOperatorType]

class EBSItemFilterOutputTypeDef(TypedDict):
    FilePaths: NotRequired[List[StringConditionTypeDef]]
    Sizes: NotRequired[List[LongConditionTypeDef]]
    CreationTimes: NotRequired[List[TimeConditionOutputTypeDef]]
    LastModificationTimes: NotRequired[List[TimeConditionOutputTypeDef]]

class S3ItemFilterOutputTypeDef(TypedDict):
    ObjectKeys: NotRequired[List[StringConditionTypeDef]]
    Sizes: NotRequired[List[LongConditionTypeDef]]
    CreationTimes: NotRequired[List[TimeConditionOutputTypeDef]]
    VersionIds: NotRequired[List[StringConditionTypeDef]]
    ETags: NotRequired[List[StringConditionTypeDef]]

class ExportSpecificationTypeDef(TypedDict):
    s3ExportSpecification: NotRequired[S3ExportSpecificationTypeDef]

class ListSearchResultExportJobsOutputTypeDef(TypedDict):
    ExportJobs: List[ExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartSearchJobOutputTypeDef(TypedDict):
    SearchJobArn: str
    CreationTime: datetime
    SearchJobIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSearchResultExportJobOutputTypeDef(TypedDict):
    ExportJobArn: str
    ExportJobIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchJobSummaryTypeDef(TypedDict):
    SearchJobIdentifier: NotRequired[str]
    SearchJobArn: NotRequired[str]
    Name: NotRequired[str]
    Status: NotRequired[SearchJobStateType]
    CreationTime: NotRequired[datetime]
    CompletionTime: NotRequired[datetime]
    SearchScopeSummary: NotRequired[SearchScopeSummaryTypeDef]
    StatusMessage: NotRequired[str]

class ListSearchJobBackupsInputPaginateTypeDef(TypedDict):
    SearchJobIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSearchJobResultsInputPaginateTypeDef(TypedDict):
    SearchJobIdentifier: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSearchJobsInputPaginateTypeDef(TypedDict):
    ByStatus: NotRequired[SearchJobStateType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSearchResultExportJobsInputPaginateTypeDef(TypedDict):
    Status: NotRequired[ExportJobStatusType]
    SearchJobIdentifier: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSearchJobBackupsOutputTypeDef(TypedDict):
    Results: List[SearchJobBackupsResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ResultItemTypeDef(TypedDict):
    S3ResultItem: NotRequired[S3ResultItemTypeDef]
    EBSResultItem: NotRequired[EBSResultItemTypeDef]

class SearchScopeTypeDef(TypedDict):
    BackupResourceTypes: Sequence[ResourceTypeType]
    BackupResourceCreationTime: NotRequired[BackupCreationTimeFilterTypeDef]
    SourceResourceArns: NotRequired[Sequence[str]]
    BackupResourceArns: NotRequired[Sequence[str]]
    BackupResourceTags: NotRequired[Mapping[str, str]]

class EBSItemFilterTypeDef(TypedDict):
    FilePaths: NotRequired[Sequence[StringConditionTypeDef]]
    Sizes: NotRequired[Sequence[LongConditionTypeDef]]
    CreationTimes: NotRequired[Sequence[TimeConditionTypeDef]]
    LastModificationTimes: NotRequired[Sequence[TimeConditionTypeDef]]

class S3ItemFilterTypeDef(TypedDict):
    ObjectKeys: NotRequired[Sequence[StringConditionTypeDef]]
    Sizes: NotRequired[Sequence[LongConditionTypeDef]]
    CreationTimes: NotRequired[Sequence[TimeConditionTypeDef]]
    VersionIds: NotRequired[Sequence[StringConditionTypeDef]]
    ETags: NotRequired[Sequence[StringConditionTypeDef]]

class ItemFiltersOutputTypeDef(TypedDict):
    S3ItemFilters: NotRequired[List[S3ItemFilterOutputTypeDef]]
    EBSItemFilters: NotRequired[List[EBSItemFilterOutputTypeDef]]

class GetSearchResultExportJobOutputTypeDef(TypedDict):
    ExportJobIdentifier: str
    ExportJobArn: str
    Status: ExportJobStatusType
    CreationTime: datetime
    CompletionTime: datetime
    StatusMessage: str
    ExportSpecification: ExportSpecificationTypeDef
    SearchJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSearchResultExportJobInputTypeDef(TypedDict):
    SearchJobIdentifier: str
    ExportSpecification: ExportSpecificationTypeDef
    ClientToken: NotRequired[str]
    Tags: NotRequired[Mapping[str, str]]
    RoleArn: NotRequired[str]

class ListSearchJobsOutputTypeDef(TypedDict):
    SearchJobs: List[SearchJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListSearchJobResultsOutputTypeDef(TypedDict):
    Results: List[ResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

SearchScopeUnionTypeDef = Union[SearchScopeTypeDef, SearchScopeOutputTypeDef]

class ItemFiltersTypeDef(TypedDict):
    S3ItemFilters: NotRequired[Sequence[S3ItemFilterTypeDef]]
    EBSItemFilters: NotRequired[Sequence[EBSItemFilterTypeDef]]

class GetSearchJobOutputTypeDef(TypedDict):
    Name: str
    SearchScopeSummary: SearchScopeSummaryTypeDef
    CurrentSearchProgress: CurrentSearchProgressTypeDef
    StatusMessage: str
    EncryptionKeyArn: str
    CompletionTime: datetime
    Status: SearchJobStateType
    SearchScope: SearchScopeOutputTypeDef
    ItemFilters: ItemFiltersOutputTypeDef
    CreationTime: datetime
    SearchJobIdentifier: str
    SearchJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

ItemFiltersUnionTypeDef = Union[ItemFiltersTypeDef, ItemFiltersOutputTypeDef]

class StartSearchJobInputTypeDef(TypedDict):
    SearchScope: SearchScopeUnionTypeDef
    Tags: NotRequired[Mapping[str, str]]
    Name: NotRequired[str]
    EncryptionKeyArn: NotRequired[str]
    ClientToken: NotRequired[str]
    ItemFilters: NotRequired[ItemFiltersUnionTypeDef]
